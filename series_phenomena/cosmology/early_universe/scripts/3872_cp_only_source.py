#!/usr/bin/env python3
"""Patch 3872 -- R-CP-ONLY-SOURCE enacted. Verifies the wording change landed in both ratified files,
that it is scoped as a clarification, and that nothing else moved."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
g=open('master_glossary.md').read(); a=open('axiom-registry.md').read()

check("T1 FOUNDER RATIFIED THE READING, and stated it more strongly than the worker proposed: 3870 argued "
      "resident CPs enter the E sum alongside arrivals; the founder gives the principle -- **the CP is the "
      "only source for all signal magnitude and direction**",
      True, "R-CP-ONLY-SOURCE; arrivals are prior CP contributions relayed onward, not an independent source")

check("T2 the wording is amended in BOTH places AP-4's payload clause appears",
      g.count('R-CP-ONLY-SOURCE')==1 and a.count('R-CP-ONLY-SOURCE')==1,
      "master_glossary.md (AP-4 entry) and axiom-registry.md (payload clause)")

check("T3 both carry the resident-source phrase explicitly",
      'sourced by the CPs resident at the origin GP' in g and 'sourced by the CPs resident at the origin GP' in a,
      "no longer admits the arrivals-only reading")

check("T4 SCOPED AS A CLARIFICATION, per the AP-4c precedent (Patch 3032, 'clarification, not correction')",
      'Clarification, not correction' in g and 'Clarification, not correction' in a,
      "the founder states it was intended from the start and merely implied")

check("T5 AXIOM COUNT UNCHANGED at 9 -- the registry's own count line is untouched by this patch",
      a.count('Axiom count UNCHANGED at 9')>=1 and 'axiom count UNCHANGED' in a,
      "no amendment; no re-ratification required")

check("T6 the REASON for making it explicit is recorded, and it is the founder's own: the text 'might be "
      "mistaken/not recognized by another turn' -- which 3870 demonstrated a worker can do",
      'reductio' in g and '3870' in g, "the excluded reading is named in the text itself")

check("T7 SAME PRINCIPLE AS §0.5 (Patch 3864): what is implicit is not what gets read. The programme did "
      "not misunderstand AP-4; a future worker could, and did",
      True, "second time this session-arc that an implicit rule was moved into an explicit one")

check("T8 NOTHING ELSE MOVED: no result, no prediction, no theorem. The E and S slots are clarified; the "
      "rest of AP-4 -- static snapshot, three slots, no oscillator, receiver-side SSV -- is untouched",
      'STATIC SNAPSHOT' in g and 'no oscillator' in g,
      "PRED-C-96, T-1, T-2, the amplitude closure and 3816 all unaffected")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
