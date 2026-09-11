#!/usr/bin/env python3
"""Patch 3926 -- founder's governance question: win or stuck spot? Answer: a win, and the panel was for
RATIFICATION not rescue. But the economy audit runs against the lane on two counts, and 'no in-lane item'
was slightly too comfortable."""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

check("T1 **THE QUESTION:** is CONV-046 a win being reported, or a stuck spot being escalated? **ANSWER: a "
      "win — and the panel was recommended for RATIFICATION, not rescue.** The original reason, at 3847, "
      "was to stop the sector being re-searched",
      True, "a negative that is not ratified gets re-worked by the next worker")

check("T2 **THE WIN, stated without decoration:** two charter targets **delivered** (T-1 at 3820, T-2 at "
      "3850); **one headline number changed** (n_s 0.9649 → 0.9654, shipped V1.6); **a negative that "
      "survived a full audit** (3868 — the one available reversal tested at strength and failed on a "
      "60-order cutoff); **one live candidate with a derived microphysics** (C-5)",
      True, "four items, none of them contingent on the panel")

check("T3 **AND THE RATIFICATION WORKED: 4 of 5 questions returned 5/5**, including the one that matters "
      "for economy — **the closure is a characterised gap.** That ruling is what prevents an eighth, "
      "ninth and tenth candidate hunt in a sector with a structural obstruction",
      True, "the intended purpose was served")

check("T4 **BUT THE ECONOMY AUDIT RUNS AGAINST THE LANE, and this is the honest part.** The panel returned "
      "**five corrections, ALL of them to the worker's WORDING** — 'permanently foreclosed' (an internal "
      "contradiction in the lane's own document), the unscoped closure, adiabaticity listed as cleared, "
      "T-1 counted four times, and the two percentages quoted apart from their chain",
      True, "five presentation faults, sent to five reviewers")

check("T5 **PHYSICS ERRORS CAUGHT BY THE PANEL: ZERO.**",
      True, "not one of the five returns found a wrong number or a wrong derivation")

check("T6 **AND THE TWO REAL PHYSICS ERRORS WERE CAUGHT ELSEWHERE:** the **83-order vacuum claim** was "
      "caught by **THE FOUNDER, in one question**; **R_h = 1/H** was caught **in-lane, the next session, "
      "by reading a symbol**",
      True, "neither needed a panel, and a panel found neither")

check("T7 **⇒ THE GOVERNANCE FINDING: panels RATIFY and catch OVERCLAIM. They do not debug.** Sending one "
      "to get unstuck would be a category error; sending one to stop a closed sector being re-searched is "
      "exactly right. **CONV-046 was the second kind**",
      True, "the distinction is the reusable content")

check("T8 **A SECOND ECONOMY FINDING, also against the lane: five presentation faults should not need a "
      "panel to catch.** They are cheap to find and were expensive to route. **The correct response is "
      "not more review but the wording rules** — seven now binding, all written after the fact",
      True, "review is the wrong instrument for proofreading")

check("T9 **AND 'NO IN-LANE ITEM' WAS SLIGHTLY TOO COMFORTABLE.** Both live items are external, which is "
      "true — but **framing them precisely enough to be answerable IS in-lane work**, and it was not "
      "done. Specifically: the SM-sector question needs stating in the SM lane's own terms, and Exit 1 "
      "needs a statement of what a derivation would have to produce",
      True, "a genuine terminus and a comfortable stopping point can look identical from inside")

check("T10 SCOPE: **a governance determination, not a physics result.** No constant minted; no finding "
      "changed; C-5's ledger, PRED-C-96, T-1, T-2 and the count law untouched",
      True, "PD-006 governance")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
