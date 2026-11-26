#!/usr/bin/env python3
"""Render README.md from data/*.json.

Usage:
  python3 scripts/build_readme.py           # write README.md
  python3 scripts/build_readme.py --check   # exit 1 if README.md is stale (for CI)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
README = ROOT / "README.md"

_META = json.loads((DATA / "repo.json").read_text(encoding="utf-8"))  # name, description, topics live here
REPO = _META["slug"]
TITLE = _META["title"]

LINK_ORDER = [("paper", "Paper"), ("project", "Project"), ("code", "Code"), ("post", "Post"), ("data", "Data")]
POLICY_SECTIONS = ["direct", "agentic", "orchestrated", "self-improving", "fast"]


def load(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def date_key(e: dict) -> str:
    """Sortable YYYY-MM-DD; a partial date ('2026', '2026-10') sorts before any full date in that period."""
    d = e.get("date") or "0000"
    return d + "-00-00"[len(d) - 4:]


def esc(s: str | None) -> str:
    """Escape characters that break markdown tables."""
    return (s or "").replace("|", "\\|").replace("\n", " ")


def row_sort_key(r: dict):
    """Rank rows of a `"sort": "desc"` benchmark: rows with a success rate (a number followed by %) first, highest
    first; then rows with only another number (e.g. 'Score 50.3'), highest first. Different scales never interleave."""
    v = r.get("value") or ""
    pct = re.search(r"(\d+(?:\.\d+)?)\s*%", v)
    if pct:
        return (0, -float(pct.group(1)))
    num = re.search(r"\d+(?:\.\d+)?", v)
    return (1, -float(num.group())) if num else (2, 0.0)


def primary_url(e: dict) -> str:
    links = e.get("links", {})
    if e.get("kind") in ("blog", "news") and links.get("post"):
        return links["post"]  # an announcement's own page, not the repo it mentions
    for k, _ in LINK_ORDER:
        if links.get(k):
            return links[k]
    return "#"


def gh_stars_badge(e: dict) -> str:
    code = e.get("links", {}).get("code") or ""
    m = re.match(r"https://github\.com/([^/]+)/([^/#?]+)/?$", code)
    if not m:
        return ""
    owner, repo = m.group(1), m.group(2)
    return f" ![stars](https://img.shields.io/github/stars/{owner}/{repo}?style=flat-square&label=%E2%98%85)"


def render_entry(e: dict, tax: dict, sec_titles: dict) -> str:
    badges = tax["status_badges"]
    s1 = tax["system1_labels"]
    lines = [f'<a id="{e["id"]}"></a>', f'- **[{e["title"]}]({primary_url(e)})**']

    byline = [e.get("org") or "—", f'*{e["kind"].capitalize()}*', e.get("date") or "n.d.", f'`{badges[e["status"]]}`']
    if e.get("venue"):
        byline.append(f'🏷️ {e["venue"]}')
    lines.append("  " + " · ".join(byline) + "  ")

    links = " ".join(f"[[{label}]({e['links'][k]})]" for k, label in LINK_ORDER if e.get("links", {}).get(k))
    if links:
        lines.append(f"  {links}{gh_stars_badge(e)}  ")

    lines.append(f'  {e["summary"]}  ')

    facets = []
    if e["section"] in POLICY_SECTIONS or e["mode"] in ("dual-system-vla", "hierarchical-vla", "foundation"):
        if e.get("models"):
            facets.append(f'**Model:** {", ".join(e["models"])}')
        if e.get("system1") and e["system1"] != "n/a":
            facets.append(f'**Below it:** {s1[e["system1"]]}')
        if e.get("interface"):
            facets.append(f'**Interface:** {e["interface"]}')
    if e.get("eval") and e["eval"] != "n/a":
        facets.append(f'**Eval:** {e["eval"]}')
    if e.get("judged_by"):
        facets.append(f'**Judged by:** {e["judged_by"]}')
    if e.get("trials"):
        facets.append(f'**Trials:** {e["trials"]}')
    sp = e.get("speed") or {}
    if sp.get("latency") or sp.get("cost"):
        facets.append("**Speed/cost:** " + "; ".join(x for x in (sp.get("latency"), sp.get("cost")) if x))
    if facets:
        lines.append("  <sub>" + " · ".join(facets) + "</sub>  ")

    if e.get("caveats"):
        lines.append(f'  ⚠️ <sub>{e["caveats"]}</sub>  ')
    if e.get("also"):
        also = ", ".join(f"[{sec_titles[a]}](#{a})" for a in e["also"])
        lines.append(f"  <sub>↪ also in: {also}</sub>")
    return "\n".join(lines)


def render_crossref(e: dict, sec_titles: dict) -> str:
    return f'- ↪ **[{e["name"]}](#{e["id"]})**: {e["title"]} <sub>(listed under [{sec_titles[e["section"]]}](#{e["section"]}))</sub>'


def build() -> str:
    tax = load("taxonomy.json")
    entries = load("entries.json")
    results = load("results.json")
    related = load("related.json")
    changelog = load("changelog.json") if (DATA / "changelog.json").exists() else []
    by_id = {e["id"]: e for e in entries}
    sections = tax["sections"]
    sec_titles = {s["id"]: s["title"] for s in sections}

    primary = {s["id"]: [] for s in sections}
    cross = {s["id"]: [] for s in sections}
    for e in entries:
        primary[e["section"]].append(e)
        for a in e.get("also", []):
            cross[a].append(e)
    for k in primary:
        primary[k].sort(key=date_key, reverse=True)
        cross[k].sort(key=date_key, reverse=True)

    newest = max(date_key(e) for e in entries)[:10]
    n = len(entries)
    out: list[str] = []
    w = out.append

    # ---------- header ----------
    w(f"# {TITLE} [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    w("")
    w(f"![entries](https://img.shields.io/badge/entries-{n}-blue?style=flat-square) "
      f"![newest](https://img.shields.io/badge/newest%20entry-{quote(newest.replace('-', '--'))}-green?style=flat-square) "
      "![license](https://img.shields.io/badge/license-CC0--1.0-lightgrey?style=flat-square)")
    w("")
    w("> **Can a general-purpose frontier model (GPT, Claude, Gemini, Qwen…) *be* the robot policy, "
      "and if so, what is left for the learned System 1?**")
    w(">")
    w("> A curated, data-driven list of papers, reports, benchmarks and critiques on frontier LLMs/VLMs controlling robots "
      "directly, through code, or on top of learned low-level controllers. Every entry records **what sits below the "
      "frontier model**, **how success was judged**, and **how fast and expensive it is**.")
    w("")
    # The figure (assets/) is the visual; the ASCII version stays below it, collapsed, as the text alternative
    # for screen readers, search engines and plain-text viewers.
    w('<p align="center"><img src="assets/question-in-one-picture.jpg" width="100%" alt="The question in one '
      'picture. Left, classic dual-system VLA: System 2, an onboard VLM at about 1 to 10 Hz, passes a latent or '
      'subtask to System 1, a learned policy at 50 to 200 Hz, which drives System 0, joint and torque control. '
      'Right, frontier model as policy (2026): a cloud frontier model at about 0.05 to 0.5 Hz emits code, end-effector '
      'waypoints or skill calls to System 1, which is either a learned VLA or WAM, or nothing, above System 0: IK, '
      'tracker and reflexes."></p>')
    w("")
    left = ["System 2   VLM, ~1-10 Hz, onboard", "   | latent / subtask",
            "System 1   learned policy, 50-200 Hz", "   |", "System 0   joint / torque control"]
    right = ["Frontier model (cloud), ~0.05-0.5 Hz", "   | code / EEF waypoints / skill calls",
             "System 1?  learned VLA/WAM  -or-  nothing", "   |", "System 0   IK / tracker / reflexes"]
    lw, rw = max(map(len, left)) + 2, max(map(len, right)) + 2
    w("<details><summary>Text version of the figure</summary>")
    w("")
    w("```text")
    w(" " + "classic dual-system VLA".center(lw + 2) + "      " + "frontier model as policy (2026)".center(rw + 2))
    w(" +" + "-" * lw + "+      +" + "-" * rw + "+")
    for i, (a, b) in enumerate(zip(left, right)):
        arrow = " ---> " if i == 2 else "      "
        w(f" | {a.ljust(lw - 1)}|{arrow}| {b.ljust(rw - 1)}|")
    w(" +" + "-" * lw + "+      +" + "-" * rw + "+")
    w("```")
    w("")
    w("</details>")
    w("")
    w("**Scope.** In: a general-purpose model that was *not* trained for robotics acts as, or directly steers, the policy. "
      "Also in, as context: the dual-system VLAs being challenged, the benchmarks both sides are scored on, and critiques. "
      "Out: robot-specific VLAs with no frontier-model angle, and pure task planners with no closed-loop control.")
    w("")

    # ---------- latest updates ----------
    if changelog:
        w('<a id="latest-updates"></a>')
        w("## 📰 Latest updates")
        w("")
        for c in changelog[:7]:
            parts = []
            if c.get("added"):
                parts.append("➕ " + ", ".join(f'[{esc(by_id[i]["name"])}](#{i})' for i in c["added"]))
            if c.get("updated"):
                parts.append("✏️ " + ", ".join(f'[{esc(by_id[i]["name"])}](#{i})' for i in c["updated"]))
            if c.get("milestones"):
                parts.append("🏁 " + ", ".join(f'[{esc(by_id[m["id"]]["name"])}](#{m["id"]}) ({m["change"]})'
                                              for m in c["milestones"]))
            if c.get("note"):
                parts.append(esc(c["note"]))
            if c.get("screened"):
                parts.append(f'<sub>{c["screened"]} candidates screened</sub>')
            w(f'- **{c["date"]}** · ' + " · ".join(parts))
        if len(changelog) > 7:
            w(f"- <sub>Older: [data/changelog.json](data/changelog.json)</sub>")
        w("")

    # ---------- contents ----------
    w("## Contents")
    w("")
    if changelog:
        w("- [📰 Latest updates](#latest-updates)")
    w("- [🏁 Milestones](#milestones)")
    w("- [📊 Leaderboards: who measured what](#leaderboards)")
    w("- [🗂️ At a glance: what sits below the frontier model?](#at-a-glance)")
    for s in sections:
        w(f'- [{s["emoji"]} {s["title"]}](#{s["id"]}) ({len(primary[s["id"]])})')
    w("- [Legend](#legend) · [Maintenance](#how-this-list-is-maintained) · [Related lists](#related-lists) · "
      "[Contributing](#contributing) · [Citation](#citation)")
    w("")

    # ---------- milestones ----------
    w('<a id="milestones"></a>')
    w("## 🏁 Milestones")
    w("")
    w("| Date | Work | Why it matters |")
    w("|---|---|---|")
    for e in sorted((e for e in entries if e.get("milestone")), key=date_key):
        w(f'| {e.get("date") or "n.d."} | [{esc(e["name"])}](#{e["id"]}) | {esc(e["milestone"])} |')
    w("")

    # ---------- leaderboards ----------
    w('<a id="leaderboards"></a>')
    w("## 📊 Leaderboards: who measured what")
    w("")
    w(f'> {results["_note"]}')
    w("")
    for b in results["benchmarks"]:
        w(f'### {b["title"]}')
        w("")
        w(f'| System | Model | Type | {b["metric"].capitalize()} | Setting | Measured by | Source |')
        w("|---|---|---|---|---|---|---|")
        rows = sorted(b["rows"], key=row_sort_key) if b.get("sort") == "desc" else b["rows"]  # stable on ties
        for r in rows:
            src = by_id[r["source"]]
            w(f'| {esc(r["system"])} | {esc(r["model"])} | {esc(r["kind"])} | **{esc(r["value"])}** | '
              f'{esc(r["setting"])} | {esc(r["measured_by"])} | [{esc(src["name"])}](#{src["id"]}) |')
        if b.get("note"):
            w("")
            w(f'> {b["note"]}')
        w("")
    sp = results["speed"]
    w(f'### ⏱️ {sp["title"]}')
    w("")
    w("| System | Rate / latency | Cost | Source |")
    w("|---|---|---|---|")
    for r in sp["rows"]:
        src = by_id[r["source"]]
        w(f'| {esc(r["system"])} | {esc(r["rate"])} | {esc(r["cost"])} | [{esc(src["name"])}](#{src["id"]}) |')
    w("")

    # ---------- at a glance ----------
    w('<a id="at-a-glance"></a>')
    w("## 🗂️ At a glance: what sits below the frontier model?")
    w("")
    w("| Work | Date | Frontier model | Role | Below it | Eval | Judged by |")
    w("|---|---|---|---|---|---|---|")
    role = {"direct-action": "direct", "agentic-code": "agentic / code", "orchestrates-learned-policy": "orchestrator",
            "self-improving": "self-improving"}
    policy = [e for e in entries if e["section"] in POLICY_SECTIONS and e["mode"] in role]
    for e in sorted(policy, key=date_key, reverse=True):
        models = ", ".join(e.get("models") or []) or "—"
        w(f'| [{esc(e["name"])}](#{e["id"]}) | {e.get("date") or "n.d."} | {esc(models)} | {role[e["mode"]]} | '
          f'{tax["system1_labels"][e["system1"]]} | {e.get("eval") or "—"} | {esc(e.get("judged_by")) or "—"} |')
    w("")

    # ---------- sections ----------
    for s in sections:
        sid = s["id"]
        w(f'<a id="{sid}"></a>')
        w(f'## {s["emoji"]} {s["title"]}')
        w("")
        w(f'*{s["blurb"]}*')
        w("")
        w(f"<details open><summary><b>{len(primary[sid])} entries</b>"
          + (f" + {len(cross[sid])} cross-listed" if cross[sid] else "") + "</summary>")
        w("")
        for e in primary[sid]:
            w(render_entry(e, tax, sec_titles))
            w("")
        if cross[sid]:
            w("**Cross-listed here:**")
            w("")
            for e in cross[sid]:
                w(render_crossref(e, sec_titles))
            w("")
        w("</details>")
        w("")

    # ---------- legend ----------
    w("## Legend")
    w("")
    w("| Badge | Meaning |")
    w("|---|---|")
    meaning = {
        "peer-reviewed": "Published at a peer-reviewed venue.",
        "preprint": "arXiv / preprint only.",
        "code": "Preprint or report **with** released code, data, or full results.",
        "post-only": "Blog, project page or report with no paper yet.",
        "secondary": "Second-hand report; find and cite the primary source.",
        "unverified": "Not yet checked against the source by a maintainer.",
    }
    for k, v in tax["status_badges"].items():
        w(f"| `{v}` | {meaning[k]} |")
    w("")
    w("**Below it** says what the frontier model's output feeds into: `none`; `analytic` (IK, waypoint interpolation, "
      "scripted controllers); `frozen learned policy` (a VLA, WAM or whole-body tracker it steers but doesn't train); "
      "`jointly trained` (classic dual-system VLA); `trained by the agent` (the frontier model trains its own System 1).")
    w("")

    # ---------- maintenance ----------
    w("## How this list is maintained")
    w("")
    w("- **Data-first.** `README.md` is generated from [`data/entries.json`](data/entries.json), "
      "[`data/results.json`](data/results.json) and [`data/taxonomy.json`](data/taxonomy.json) by "
      "[`scripts/build_readme.py`](scripts/build_readme.py). Don't edit the README by hand.")
    w("- **Verified.** [`scripts/validate.py`](scripts/validate.py) checks the schema, checks every arXiv ID against the "
      "arXiv API title (`--arxiv`), and checks that links resolve (`--links`).")
    w("- **Daily, automated.** A scheduled Claude Code agent runs [`scripts/collect.py`](scripts/collect.py) (arXiv search, "
      "papers citing the anchor papers, new additions to the related lists, venue updates) and scans lab blogs and "
      "announcements, triages every candidate against the scope, edits the data, validates it, and pushes. "
      "Its instructions are in [MAINTAINING.md](MAINTAINING.md); every decision, including rejections, is recorded in "
      "[`data/seen.json`](data/seen.json) and [`data/changelog.json`](data/changelog.json). "
      "A GitHub Action re-validates every push and checks links daily. Spot an error? Open an issue; corrections win.")
    w("- **Editorial rules** (adapted from benchflow-ai/awesome-embodied-agents): numbers are quoted verbatim from the source; "
      "every result row says who measured it; sim vs real, trial counts and the success judge are recorded; "
      "authors' own stated limitations go in the caveats.")
    w("")

    # ---------- related ----------
    w("## Related lists")
    w("")
    w(f'<sub>{related["_snapshot"]}</sub>')
    w("")
    w("| List | ★ | Last push | Angle |")
    w("|---|---|---|---|")
    for r in related["lists"]:
        w(f'| [{r["name"]}]({r["url"]}) | {r["stars"] if r["stars"] is not None else "—"} | {r["pushed"] or "—"} | {esc(r["angle"])} |')
    w("")

    # ---------- contributing / citation ----------
    w("## Contributing")
    w("")
    w("Add or fix an entry in `data/entries.json` (and `data/results.json` for numbers), then run:")
    w("")
    w("```bash")
    w("python3 scripts/validate.py --arxiv      # schema + arXiv title check")
    w("python3 scripts/build_readme.py          # regenerate README.md")
    w("```")
    w("")
    w("See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry schema and editorial rules.")
    w("")
    w("## Citation")
    w("")
    w("```bibtex")
    w("@misc{awesome_frontier_robot_policies,")
    w(f"  title  = {{Awesome Frontier Models as Robot Policies}},")
    w(f"  year   = {{{newest[:4]}}},")
    w(f"  note   = {{https://github.com/{REPO}}}")
    w("}")
    w("```")
    w("")
    w("License: [CC0 1.0](LICENSE). To the extent possible under law, the contributors have waived all copyright to this list.")
    w("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if README.md is out of date")
    args = ap.parse_args()
    text = build()
    if args.check:
        current = README.read_text(encoding="utf-8") if README.exists() else ""
        if current != text:
            print("README.md is stale. Run: python3 scripts/build_readme.py", file=sys.stderr)
            return 1
        print("README.md is up to date.")
        return 0
    README.write_text(text, encoding="utf-8")
    print(f"Wrote {README.relative_to(ROOT)} ({len(text):,} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
