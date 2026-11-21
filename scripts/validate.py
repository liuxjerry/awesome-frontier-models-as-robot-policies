#!/usr/bin/env python3
"""Validate data/*.json.

  python3 scripts/validate.py            # schema / cross-reference checks (offline)
  python3 scripts/validate.py --arxiv    # + compare every arXiv id's title with the arXiv API
  python3 scripts/validate.py --links    # + check that every URL resolves
Exit code 1 on any error. Warnings never fail the run.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
UA = "awesome-list-validator/1.0"
REQUIRED = ["id", "name", "title", "date", "kind", "status", "section", "links", "mode", "system1", "summary"]
DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def norm_title(t: str) -> str:
    t = unicodedata.normalize("NFKD", t)
    t = re.sub(r"\$[^$]*\$", "", t)          # drop LaTeX math such as $\pi_{0.5}$
    t = re.sub(r"[^a-z0-9 ]", " ", t.lower())
    return " ".join(t.split())


def check_schema(entries, tax, results):
    errors, warnings = [], []
    enums = tax["enums"]
    sections = {s["id"] for s in tax["sections"]}
    seen = set()
    for i, e in enumerate(entries):
        where = f'entry[{i}] {e.get("id", "?")}'
        for f in REQUIRED:
            if f not in e or e[f] in (None, ""):
                errors.append(f"{where}: missing required field '{f}'")
        if not ID_RE.match(e.get("id", "")):
            errors.append(f"{where}: id must be kebab-case")
        if e.get("id") in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(e.get("id"))
        if e.get("added") and not re.match(r"^\d{4}-\d{2}-\d{2}$", e["added"]):
            errors.append(f"{where}: added must be YYYY-MM-DD")
        if e.get("date") and not DATE_RE.match(e["date"]):
            errors.append(f"{where}: date must be YYYY, YYYY-MM or YYYY-MM-DD")
        for field in ("kind", "status", "mode", "system1"):
            if e.get(field) and e[field] not in enums[field]:
                errors.append(f"{where}: {field}='{e[field]}' not in {enums[field]}")
        if e.get("eval") and e["eval"] not in enums["eval"]:
            errors.append(f"{where}: eval='{e['eval']}' not in {enums['eval']}")
        if e.get("section") not in sections:
            errors.append(f"{where}: unknown section '{e.get('section')}'")
        for a in e.get("also", []):
            if a not in sections:
                errors.append(f"{where}: unknown 'also' section '{a}'")
            if a == e.get("section"):
                warnings.append(f"{where}: 'also' repeats the primary section")
        links = e.get("links") or {}
        if not links:
            errors.append(f"{where}: needs at least one link")
        for k, u in links.items():
            if not str(u).startswith("https://"):
                errors.append(f"{where}: link '{k}' must be https://")
        if e.get("arxiv") and links.get("paper") and e["arxiv"] not in links["paper"]:
            errors.append(f"{where}: arxiv id does not match paper link")
        if links.get("paper", "").startswith("https://arxiv.org/abs/") and not e.get("arxiv"):
            warnings.append(f"{where}: arXiv paper link but no 'arxiv' field (title check skipped)")
        if e.get("status") == "secondary" and not e.get("caveats"):
            warnings.append(f"{where}: secondary source should say where the primary is")
    ids = {e["id"] for e in entries}
    for b in results["benchmarks"]:
        for r in b["rows"]:
            if r["source"] not in ids:
                errors.append(f"results/{b['id']}: unknown source '{r['source']}'")
            if not r.get("measured_by"):
                errors.append(f"results/{b['id']}: row '{r['system']}' needs measured_by")
    for r in results["speed"]["rows"]:
        if r["source"] not in ids:
            errors.append(f"results/speed: unknown source '{r['source']}'")
    return errors, warnings


def check_arxiv(entries):
    errors = []
    todo = [e for e in entries if e.get("arxiv")]
    ns = {"a": "http://www.w3.org/2005/Atom"}
    got = {}
    for i in range(0, len(todo), 50):
        chunk = [e["arxiv"] for e in todo[i:i + 50]]
        url = f"http://export.arxiv.org/api/query?id_list={','.join(chunk)}&max_results=100"
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        root = ET.fromstring(urllib.request.urlopen(req, timeout=90).read())
        for en in root.findall("a:entry", ns):
            aid = en.find("a:id", ns).text.split("/abs/")[-1]
            aid = re.sub(r"v\d+$", "", aid)
            got[aid] = " ".join(en.find("a:title", ns).text.split())
        time.sleep(3)  # arXiv API etiquette
    for e in todo:
        t = got.get(e["arxiv"])
        if t is None:
            errors.append(f"{e['id']}: arXiv {e['arxiv']} not found")
            continue
        a, b = norm_title(t), norm_title(e["title"])
        if a != b and not (a in b or b in a):
            errors.append(f"{e['id']}: title mismatch\n    arXiv: {t}\n    ours : {e['title']}")
    print(f"arXiv: checked {len(todo)} ids")
    return errors


def check_links(entries):
    urls = sorted({u for e in entries for u in (e.get("links") or {}).values()})

    def probe(u):
        for method in ("HEAD", "GET"):
            try:
                req = urllib.request.Request(u, method=method, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=30) as r:
                    return u, r.status
            except urllib.error.HTTPError as ex:
                if method == "GET":
                    return u, ex.code
            except Exception as ex:  # noqa: BLE001
                if method == "GET":
                    return u, f"{type(ex).__name__}"
        return u, "?"

    with ThreadPoolExecutor(8) as pool:
        res = list(pool.map(probe, urls))
    # 401/403/429 usually mean bot-blocking (X, RedNote, some CDNs), so they are warnings, not errors.
    bad = [(u, s) for u, s in res if not (isinstance(s, int) and s < 400)]
    errors = [f"link {s}: {u}" for u, s in bad if s not in (401, 403, 429)]
    warns = [f"link {s} (possibly bot-blocked): {u}" for u, s in bad if s in (401, 403, 429)]
    print(f"links: checked {len(urls)} urls")
    return errors, warns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arxiv", action="store_true")
    ap.add_argument("--links", action="store_true")
    args = ap.parse_args()
    entries, tax, results = load("entries.json"), load("taxonomy.json"), load("results.json")
    errors, warnings = check_schema(entries, tax, results)
    ids = {e["id"] for e in entries}
    if (DATA / "changelog.json").exists():
        for c in load("changelog.json"):
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", c.get("date", "")):
                errors.append(f"changelog: bad date {c.get('date')!r}")
            for i in c.get("added", []) + c.get("updated", []):
                if i not in ids:
                    errors.append(f"changelog {c.get('date')}: unknown entry id '{i}'")
    if args.arxiv:
        errors += check_arxiv(entries)
    if args.links:
        e2, w2 = check_links(entries)
        errors += e2
        warnings += w2
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(entries)} entries · {len(errors)} errors · {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
