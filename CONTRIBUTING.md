# Contributing

Thanks for helping. This list is **data-first**: edit `data/*.json`, never `README.md`.

## What belongs here

**In:** a general-purpose model that was not trained for robotics (GPT, Claude, Gemini, Qwen, …) acts as the robot
policy, writes the code that is the policy, or steers a learned low-level controller in closed loop. Also in, as context:
dual-system VLAs, shared benchmarks where both sides are scored, critiques and retests, and surveys or essays on the
System 1 / System 2 split.

**Out:** robot-specific VLAs with no frontier-model angle; open-loop task planners; demos with no task definition or
success criterion.

## Adding an entry

1. Append an object to `data/entries.json`:

```jsonc
{
  "id": "kebab-case-unique",
  "name": "Short display name",
  "title": "Exact title (must match arXiv if `arxiv` is set)",
  "org": "Lab / company",
  "authors": "First Author et al.",
  "date": "YYYY-MM-DD",               // YYYY-MM or YYYY allowed if unknown
  "kind": "paper",                    // paper | report | blog | essay | benchmark | survey | project | news
  "status": "preprint",               // peer-reviewed | preprint | code | post-only | secondary | unverified
  "venue": "CoRL 2026",               // optional
  "section": "agentic",               // see data/taxonomy.json
  "also": ["self-improving"],         // optional cross-listing
  "links": {"paper": "https://arxiv.org/abs/…", "project": "…", "code": "…", "post": "…", "data": "…"},
  "arxiv": "2611.09892",              // optional; enables the title check
  "models": ["Claude Opus 5.5"],
  "mode": "agentic-code",             // direct-action | agentic-code | orchestrates-learned-policy | self-improving | …
  "system1": "analytic",              // none | analytic | frozen-learned | jointly-trained | trained-by-agent | n/a
  "interface": "What the frontier model emits and what consumes it",
  "eval": "sim+real",                 // sim | real | sim+real | n/a
  "judged_by": "simulator checker / human / the agent itself",
  "trials": "how many",
  "speed": {"latency": "…", "cost": "…"},
  "summary": "1–3 sentences. Numbers quoted verbatim from the source.",
  "caveats": "Limits the authors state, plus known critiques.",
  "milestone": "Optional: one line on why this is a turning point."
}
```

2. If the work reports numbers on a shared benchmark, add rows to `data/results.json`. **Every row needs
   `measured_by`.** Two groups measuring the same system can disagree by 20+ points.
3. Run:

```bash
python3 scripts/validate.py --arxiv
python3 scripts/build_readme.py
```

4. Open a PR with the regenerated README.

## Editorial rules

- **Quote, don't paraphrase, numbers.** Use the exact figure and its setting.
- **Record who judged success**: the simulator's checker, a held-out verifier, a human, or the agent itself.
  Self-declared success and built-in checkers are not the same thing.
- **Sim vs real, and trial counts**, always.
- **Put the authors' own limitations in `caveats`.** Latency, cost, paused simulators and privileged state belong there.
- **Secondary sources** (news, threads) get `status: "secondary"` and a pointer to the primary source.
- Don't add an entry you haven't opened yourself.
