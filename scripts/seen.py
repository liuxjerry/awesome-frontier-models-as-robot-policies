#!/usr/bin/env python3
"""Record a triage decision so collect.py never shows the item again.

  python3 scripts/seen.py rejected arxiv:2611.01234 "VLA with no frontier-model angle"
  python3 scripts/seen.py added    arxiv:2611.05678 "-> entry foo-bar"
  python3 scripts/seen.py rejected url:https://example.com/blog/post "marketing, no method"
  python3 scripts/seen.py noted    update:2611.09892:v2 "venue already recorded"
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from collect import save, today  # noqa: E402  (save keeps the baseline list on one line)

PATH = Path(__file__).resolve().parent.parent / "data" / "seen.json"
DECISIONS = {"added", "rejected", "noted", "baseline"}


def main() -> int:
    if len(sys.argv) < 3 or sys.argv[1] not in DECISIONS or ":" not in sys.argv[2]:
        print(__doc__)
        return 2
    decision, key, note = sys.argv[1], sys.argv[2], " ".join(sys.argv[3:])
    seen = json.loads(PATH.read_text(encoding="utf-8"))
    seen["items"][key] = {"date": today().isoformat(), "decision": decision, "note": note}
    seen["items"] = dict(sorted(seen["items"].items()))
    save("seen.json", seen)
    print(f"{decision}: {key}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
