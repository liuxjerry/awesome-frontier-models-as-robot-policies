#!/usr/bin/env python3
"""Gather everything the daily maintainer needs to look at. Never edits entries.json / results.json.

  python3 scripts/collect.py                    # -> candidates.json + summary on stdout
  python3 scripts/collect.py --refresh-stars    # also rewrite star counts in data/related.json
  python3 scripts/collect.py --baseline         # mark every arXiv id in the related lists as seen (one-off)

Sources
  arxiv      narrow arXiv searches (scripts/arxiv_watch.py), last --days days
  citations  new papers citing the list's anchor papers (Semantic Scholar, best effort)
  upstream   arXiv ids that appeared in the related awesome lists (data/related.json)
  updates    existing preprints whose arXiv comment / journal-ref now mentions a venue

Anything already in data/entries.json or data/seen.json is skipped, so each paper is shown once.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import arxiv_watch  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
UA = "awesome-list-collector/1.0"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
ARXIV_ID = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", re.I)
# Recent, on-topic papers whose citers are likely to belong in the list.
ANCHORS = ["amp1", "openrua", "cap-x", "agent-as-policy", "faea", "robolab", "robodojo", "show-harness",
           "gemini-robotics-1-5", "harness-vla", "justrua"]
VENUE = re.compile(r"\b(accepted|to appear|published|camera[- ]ready|ICRA|IROS|RSS|CoRL|NeurIPS|ICLR|ICML|CVPR|"
                   r"ECCV|ICCV|AAAI|IJCAI|RA-?L|T-?RO|Science Robotics|Nature)\b", re.I)


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def save(name, obj):
    text = json.dumps(obj, indent=2, ensure_ascii=False)
    if name == "seen.json":  # keep the long baseline id list on one line
        text = re.sub(r'"baseline": \[(.*?)\]', lambda m: '"baseline": [' + ", ".join(
            x.strip() for x in m.group(1).split(",") if x.strip()) + "]", text, flags=re.S)
    (DATA / name).write_text(text + "\n", encoding="utf-8")


def default_days() -> int:
    """Days since the last successful daily run (+1), at least 3, so a skipped day is never lost."""
    import subprocess
    try:
        last = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--grep=^daily:", "--format=%cs"],
                              capture_output=True, text=True, timeout=10).stdout.strip()
        return max(3, (dt.date.today() - dt.date.fromisoformat(last)).days + 1)
    except Exception:  # noqa: BLE001  no git, no daily commit yet
        return 3


def get(url, accept_json=False, tries=3):
    headers = {"User-Agent": UA}
    if url.startswith("https://api.github.com/") and os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=headers)
            raw = urllib.request.urlopen(req, timeout=60).read()
            return json.loads(raw) if accept_json else raw.decode("utf-8", "replace")
        except urllib.error.HTTPError as ex:
            if ex.code in (429, 500, 502, 503) and i < tries - 1:
                time.sleep(5 * (i + 1))
                continue
            raise


def arxiv_meta(ids):
    """title / abstract / dates / comment / journal_ref for a list of arXiv ids."""
    out = {}
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"id_list": ",".join(chunk), "max_results": len(chunk)})
        root = ET.fromstring(get(url))
        for e in root.findall("a:entry", NS):
            full = e.find("a:id", NS).text.split("/abs/")[-1]
            aid = re.sub(r"v\d+$", "", full)
            def t(tag):
                n = e.find(tag, NS)
                return " ".join(n.text.split()) if n is not None and n.text else ""
            out[aid] = {"id": aid, "version": full[len(aid):] or "v1", "title": t("a:title"),
                        "date": t("a:published")[:10], "updated": t("a:updated")[:10],
                        "abstract": t("a:summary"), "comment": t("arxiv:comment"),
                        "journal_ref": t("arxiv:journal_ref")}
        time.sleep(3)
    return out


def upstream_ids(related):
    found = {}
    for r in related["lists"]:
        raw = f'https://raw.githubusercontent.com/{r["name"]}/HEAD/README.md'
        try:
            for aid in set(ARXIV_ID.findall(get(raw))):
                found.setdefault(aid, []).append(r["name"])
        except Exception as ex:  # noqa: BLE001
            print(f"  upstream {r['name']}: {ex}", file=sys.stderr)
    return found


def citations(entries):
    by_id = {e["id"]: e for e in entries}
    found = {}
    for a in ANCHORS:
        aid = by_id.get(a, {}).get("arxiv")
        if not aid:
            continue
        url = (f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{aid}/citations?"
               "fields=title,externalIds,publicationDate&limit=200")
        try:
            data = get(url, accept_json=True)
        except Exception as ex:  # noqa: BLE001
            print(f"  citations of {a}: {ex}", file=sys.stderr)
            continue
        for c in data.get("data", []):
            p = c.get("citingPaper") or {}
            cid = (p.get("externalIds") or {}).get("ArXiv")
            if cid:
                found.setdefault(cid, []).append(a)
        time.sleep(2)
    return found


def refresh_stars(related):
    """Update stars / last push. Leaves the file untouched unless every repo was read."""
    fresh = {}
    for r in related["lists"]:
        try:
            d = get(f'https://api.github.com/repos/{r["name"]}', accept_json=True)
            fresh[r["name"]] = (d["stargazers_count"], d["pushed_at"][:10])
        except Exception as ex:  # noqa: BLE001
            print(f"  stars {r['name']}: {ex}", file=sys.stderr)
    if len(fresh) < len(related["lists"]):
        print("  stars: not all repos readable; related.json left unchanged", file=sys.stderr)
        return
    for r in related["lists"]:
        r["stars"], r["pushed"] = fresh[r["name"]]
    related["_snapshot"] = f"Stars and last push read from the GitHub API on {dt.date.today().isoformat()}."
    save("related.json", related)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=None, help="look-back window (default: since last daily run, min 3)")
    ap.add_argument("--out", default=str(ROOT / "candidates.json"))
    ap.add_argument("--refresh-stars", action="store_true")
    ap.add_argument("--stars-only", action="store_true", help="refresh related.json stars and exit (GitHub Action)")
    ap.add_argument("--baseline", action="store_true")
    args = ap.parse_args()

    entries, related = load("entries.json"), load("related.json")
    seen = load("seen.json")
    listed = {e["arxiv"] for e in entries if e.get("arxiv")}
    skip = listed | set(seen.get("baseline", [])) | {k.split(":", 1)[1] for k in seen["items"] if k.startswith("arxiv:")}
    today = dt.date.today().isoformat()

    if args.baseline:
        new = sorted(set(upstream_ids(related)) - skip)
        seen["baseline"] = sorted(set(seen.get("baseline", [])) | set(new))
        save("seen.json", seen)
        n = len(new)
        print(f"baseline: marked {n} upstream arXiv ids as seen")
        return 0

    if args.refresh_stars or args.stars_only:
        refresh_stars(related)
        if args.stars_only:
            return 0
    status = {}

    cand: dict[str, dict] = {}

    def add(aid, source, detail):
        if aid in skip:
            return
        c = cand.setdefault(aid, {"id": aid, "sources": {}})
        c["sources"].setdefault(source, []).extend(detail if isinstance(detail, list) else [detail])

    args.days = args.days or default_days()
    cutoff = (dt.date.today() - dt.timedelta(days=args.days)).isoformat()
    ok = 0
    for q in arxiv_watch.QUERIES:
        try:
            for p in arxiv_watch.search(q):
                if p["date"] >= cutoff:
                    add(p["id"], "arxiv-search", q)
            ok += 1
        except Exception as ex:  # noqa: BLE001
            print(f"  arxiv query failed: {q}: {ex}", file=sys.stderr)
            if ok == 0 and q == arxiv_watch.QUERIES[1]:
                break  # first two failed: the host is unreachable, stop hammering it
        time.sleep(3)
    status["arxiv-search"] = f"{ok}/{len(arxiv_watch.QUERIES)} queries ok"
    cites = citations(entries)
    status["cites"] = f"{len(cites)} citing papers read" if cites else "unreachable or empty"
    for aid, who in cites.items():
        add(aid, "cites", who)
    up = upstream_ids(related)
    status["related-list"] = f"{len(up)} arXiv ids read" if up else "unreachable"
    for aid, lists in up.items():
        add(aid, "related-list", lists)

    try:
        meta = arxiv_meta(sorted(cand)) if cand else {}
        status["arxiv-metadata"] = "ok"
    except Exception as ex:  # noqa: BLE001
        meta = {}
        status["arxiv-metadata"] = f"unreachable ({ex}); papers listed by id only, open them to triage"
    papers = []
    for aid, c in cand.items():
        m = meta.get(aid) or {"id": aid, "title": "", "date": "", "abstract": "",
                              "url": f"https://arxiv.org/abs/{aid}"}
        text = (m["title"] + " " + m["abstract"]).lower()
        m.update(c, score=sum(text.count(b) for b in arxiv_watch.BOOST) + 3 * len(c["sources"]))
        papers.append(m)
    papers.sort(key=lambda p: (-p["score"], p["date"]))

    updates = []
    pre = [e for e in entries if e.get("arxiv") and e.get("status") in ("preprint", "code")]
    try:
        pre_meta = arxiv_meta([e["arxiv"] for e in pre])
        status["venue-updates"] = "ok"
    except Exception as ex:  # noqa: BLE001
        pre_meta, status["venue-updates"] = {}, f"unreachable ({ex})"
    for aid, m in pre_meta.items():
        e = next(x for x in pre if x["arxiv"] == aid)
        hint = " ".join(filter(None, [m["journal_ref"], m["comment"]]))
        key = f"update:{aid}:{m['version']}"
        if VENUE.search(hint) and key not in seen["items"] and not e.get("venue"):
            updates.append({"entry": e["id"], "arxiv": aid, "version": m["version"], "journal_ref": m["journal_ref"],
                            "comment": m["comment"], "seen_key": key})

    out = {"generated": today, "window_days": args.days, "source_status": status,
           "papers": papers, "entry_updates": updates}
    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{len(papers)} new papers, {len(updates)} possible venue updates -> {args.out}")
    for k, v in status.items():
        print(f"  source {k}: {v}")
    for p in papers[:40]:
        print(f"  [{p['score']:>2}] {p['id']} {p['date']} {p['title'][:90]}  <{', '.join(p['sources'])}>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
