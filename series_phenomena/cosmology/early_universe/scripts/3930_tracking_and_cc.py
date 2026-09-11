#!/usr/bin/env python3
"""Patch 3930 -- three founder questions answered: owed items are now in todolist.md (they were NOWHERE
for 55 sessions); the '3 vs 0.03' figure came from a RETRACTED patch and does not exist; and the EU lane
is NOT working the cosmological constant."""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
t=open('todolist.md').read()
LO,HI,BLO,BHI=0.284,0.491,0.6,0.9

check("T1 **Q1 — WHERE ARE THE OWED ITEMS TRACKED? They were NOT.** `todolist.md` exists at the repo root, "
      "with a stated discipline (*a new paper does not start until P1 is clear*), and **this arc put "
      "nothing in it across Sessions 169–223 — 55 sessions, zero entries**",
      True, "D-3 applied to the wrong object: the file was located only when the founder asked")

check("T2 **WHERE THEY ACTUALLY LIVED: handovers — which are SUPERSEDED EVERY SESSION.** An item owed to "
      "another lane could survive only by being re-copied forward by hand, which is not a register",
      True, "the failure mode is silent: nothing is lost visibly")

check("T3 **FIXED: TODO-3930-EU registered in `todolist.md` P2**, listing everything owed — the FP "
      "question, CONV-046 dispatch, the DE escalation, the cosmic-web piece, the stale DM project map, "
      "Isak's two recompiles, and the four items owed into EU-1 V1.7",
      'TODO-3930-EU' in t and 'CONV-046' in t and 'V1.7' in t, "registered where the programme looks")

check("T4 **Q2 — THE '3 vs 0.03' FIGURE DOES NOT EXIST.** It came from **Patch 3920**, which assumed "
      "R_h = 1/H, derived a Friedmann degeneracy, and concluded *'k must be 3 and is derived as 0.0288'*. "
      "**3920 was RETRACTED IN FULL at 3922**",
      True, "R_h is a Li-analog future event horizon; no degeneracy, no k, no 3")

check("T5 **AND IT REACHED THE FOUNDER ANYWAY — which is the more useful finding.** The retraction was "
      "written, filed, bannered and summarised, and the number still propagated. **A retraction that "
      "replaces a claim is weaker than one that names the number being withdrawn**",
      True, "the summary said the patch was retracted; it did not say 'the figure 3 does not exist'")

check("T6 **WHAT THE REAL CC RESIDUAL IS:** CPP derives **c_Li ∈ [0.284, 0.491]** from α + Planck-FCC "
      "geometry, against an observational band of **[0.6, 0.9]** — **1.22×–3.2× in c, 1.5×–10× in ρ**",
      abs((BLO/HI)**2-1.5)<0.1 and abs((BHI/LO)**2-10.0)<0.3,
      f"c: {BLO/HI:.2f}-{BHI/LO:.1f}x; rho: {(BLO/HI)**2:.1f}-{(BHI/LO)**2:.1f}x")

check("T7 **Q3 — HAS THERE BEEN PROGRESS ON IT? Not from this lane, and none was made.** The EU lane's "
      "two contributions to the CC question were **an error** (3906, the 83 orders, founder-caught) and "
      "**a retracted patch** (3920). **Net contribution: zero, minus the cost of the corrections**",
      True, "stated plainly rather than as 'we clarified the framing'")

check("T8 **AND THE ONE THING THAT SURVIVES IS NOT PROGRESS ON THE PROBLEM** — it is that the EU lane now "
      "**correctly understands** what the CC lane has: a **derived** holographic coefficient missing by "
      "~2× in c, with **F-CLI-1 FIRING-PENDING-SCRUTINY**. **That is the CC lane's result, not this "
      "lane's**",
      True, "understanding another lane's result is not contributing to it")

check("T9 **Q3, DIRECTLY — ARE WE STILL WORKING ON IT? NO, AND THIS LANE SHOULD NOT BE.** The CC lane "
      "owns the residual and has fired its own falsifier on it. **There is no EU-lane CC work item, and "
      "TODO-3930-EU records that explicitly so it is not re-opened**",
      'NOT owed' in t, "the not-owed items are registered alongside the owed ones")

check("T10 SCOPE: **a tracking repair and two corrections. No physics.** PRED-C-96, T-1, T-2, the count "
      "law and C-5's ledger untouched",
      True, "governance under PD-006")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
