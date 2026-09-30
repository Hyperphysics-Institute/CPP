#!/usr/bin/env python3
"""overview_staleness_gate.py -- Patch 4335 (founder, 29 Sep 2026: theory-overview.md "was supposed to be updated after
every advance in the theory").

theory-overview.md is the programme's scorecard.  It must be refreshed whenever a SCORECARD-BEARING registry changes:
predictions.md, theorem-registry.md, axiom-registry.md, paper_catalog.md.  (research_frontier.md changes every patch and
is deliberately NOT a trigger: refreshing the overview every turn is the D-8 failure.)

The gate compares the last commit touching theory-overview.md with the last commit touching any trigger file, and counts
the trigger commits since the overview was last refreshed.  Exit 1 (STALE) if any trigger file changed after the
overview; exit 0 (PASS) otherwise.  Run at boot (with the other gates) and at the §15 session close.
"""
import subprocess, sys

REPO = "."
OVERVIEW = "theory-overview.md"
TRIGGERS = ["predictions.md", "theorem-registry.md", "axiom-registry.md", "paper_catalog.md"]

def last(path):
    out = subprocess.run(["git", "log", "-1", "--format=%H %cs", "--", path], cwd=REPO,
                         capture_output=True, text=True).stdout.split()
    return (out[0], out[1]) if out else (None, None)

def since(sha, paths):
    if not sha:
        return []
    out = subprocess.run(["git", "log", "--format=%h %cs %s", f"{sha}..HEAD", "--"] + paths, cwd=REPO,
                         capture_output=True, text=True).stdout.strip().splitlines()
    return out

ov_sha, ov_date = last(OVERVIEW)
behind = since(ov_sha, TRIGGERS)
print(f"overview_staleness_gate: {OVERVIEW} last refreshed {ov_date} ({ov_sha[:8] if ov_sha else '-'})")
for p in TRIGGERS:
    sha, d = last(p)
    print(f"   {p:22s} last changed {d}")
if behind:
    print(f"STALE: {len(behind)} scorecard-registry commit(s) since the overview was refreshed; newest:")
    for line in behind[:5]:
        print("   " + line[:150])
    print("Refresh theory-overview.md per templates/operating_system.md 'theory-overview.md update procedure'.")
    sys.exit(1)
print("PASS")
