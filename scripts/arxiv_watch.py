#!/usr/bin/env python3
"""Find new arXiv papers that might belong in the list. Never edits entries.json.

  python3 scripts/arxiv_watch.py --days 7 > candidates.md

Prints a Markdown checklist of candidates not already in data/entries.json,
for a human to triage (the daily GitHub Action posts it to an issue).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "awesome-list-arxiv-watch/1.0"
NS = {"a": "http://www.w3.org/2005/Atom"}

# Each query is an arXiv API search_query. Keep them narrow; precision beats recall here.
QUERIES = [
    'abs:"agent as policy" AND cat:cs.RO',
    'abs:"robot-use agent" OR abs:"robot-use agents"',
    'abs:"LLM as policy" AND cat:cs.RO',
    'abs:"agentic manipulation"',
    'abs:"code as policies" AND abs:"coding agent"',
    'abs:"frontier model" AND abs:manipulation AND cat:cs.RO',
    'abs:"frontier models" AND abs:robot AND abs:"zero-shot"',
    'abs:"general-purpose" AND abs:"robot policy" AND abs:"language model" AND cat:cs.RO',
    'abs:"System 1" AND abs:"System 2" AND abs:"vision-language-action"',
    'abs:harness AND abs:robot AND abs:agent AND cat:cs.RO',
]
# Score boost terms: more hits = higher in the list.
BOOST = ["frontier", "agent", "harness", "zero-shot", "system 1", "system 0", "gpt", "claude", "gemini",
         "astra", "opus", "coding agent", "without demonstrations", "no task-specific", "latency"]


def search(q: str, max_results: int = 50):
    url = ("http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": max_results}))
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=90).read())
    for e in root.findall("a:entry", NS):
        yield {
            "id": re.sub(r"v\d+$", "", e.find("a:id", NS).text.split("/abs/")[-1]),
            "title": " ".join(e.find("a:title", NS).text.split()),
            "date": e.find("a:published", NS).text[:10],
            "abstract": " ".join(e.find("a:summary", NS).text.split()),
        }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    args = ap.parse_args()
    known = {e.get("arxiv") for e in json.loads((ROOT / "data/entries.json").read_text(encoding="utf-8"))}
    cutoff = (dt.date.today() - dt.timedelta(days=args.days)).isoformat()
    found: dict[str, dict] = {}
    for q in QUERIES:
        try:
            for p in search(q):
                if p["date"] >= cutoff and p["id"] not in known:
                    p.setdefault("queries", []).append(q)
                    found.setdefault(p["id"], p)
        except Exception as ex:  # noqa: BLE001
            print(f"<!-- query failed: {q}: {ex} -->")
        time.sleep(3)
    for p in found.values():
        text = (p["title"] + " " + p["abstract"]).lower()
        p["score"] = sum(text.count(b) for b in BOOST)
    ranked = sorted(found.values(), key=lambda p: (-p["score"], p["date"]))
    print(f"### arXiv candidates since {cutoff} ({len(ranked)})\n")
    if not ranked:
        print("_No new candidates._")
    for p in ranked:
        snippet = p["abstract"][:280] + ("…" if len(p["abstract"]) > 280 else "")
        print(f"- [ ] **[{p['title']}](https://arxiv.org/abs/{p['id']})** · {p['date']} · relevance {p['score']}\n"
              f"  <sub>{snippet}</sub>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
