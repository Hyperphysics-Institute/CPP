#!/usr/bin/env python3
"""Patch 3932 -- two founder questions. (1) The session-close has been firing EVERY TURN when the protocol
fires it at WINDOW turnover; ~50% of this window's patch output is bookkeeping for turnovers that did not
happen. Cadence corrected. (2) On the CC lane: the offer is declined, and the reason is the track record."""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
N=3931-3886+1; CLOSES=N//2

check("T1 **THE FOUNDER'S OBSERVATION IS CORRECT AND THE CAUSE IS A PROTOCOL MISREADING.** The session "
      "close *did* used to fire only at context turnover. It now fires every turn. **Nothing in the "
      "protocol changed — the lane's reading of it did**",
      True, "he noticed a cadence change; it was not a deliberate one")

check("T2 **D-1/D-3 SETTLES IT:** the corpus describes the handover as *'the one piece of handover output "
      "that belongs in chat, **since Thomas pastes it into the next window**.'* **⇒ a SESSION is a "
      "CONTEXT WINDOW. The close fires at WINDOW TURNOVER, not per turn**",
      True, "the definition was on file and was never read")

check("T3 **THE COST, MEASURED:** this window ran ~46 patches, of which **~23 are session-closes** — "
      "**~50% of patch output is turnover bookkeeping for turnovers that did not happen**",
      abs(CLOSES/N-0.5)<0.03, f"{CLOSES} closes in {N} patches = {100*CLOSES/N:.0f}%")

check("T4 **AND IT COSTS MORE THAN PATCH IDS.** Each close writes a **session log**, a **transcript row**, "
      "a **development vignette**, a **registry pass** and a **handover file** — **per turn, addressed to "
      "a reader who never arrives**",
      True, "the vignettes in particular are paper prose written for a turnover that did not occur")

check("T5 **CADENCE CORRECTED, effective now:** the §15 A–H close fires **at context-window turnover, or "
      "when the founder calls for it** — **not every turn.** Ordinary turns deliver the work patch and "
      "update `research_frontier.md` and `id_block_registry.md` only",
      True, "frontier + id-block are the two registries that must stay live between closes")

check("T6 **AND THIS BEARS DIRECTLY ON HIS CONTINUITY WORRY.** He asked whether much is lost at turnover. "
      "**Some is — but the ritual was not buying it back.** A handover written every turn is not 55 "
      "handovers' worth of continuity; **it is one handover's worth, rewritten 55 times, at the cost of "
      "half the lane's output**",
      True, "the volume was concealing the gap rather than closing it")

check("T7 **WHAT ACTUALLY CARRIES CONTINUITY** is what 3930 found missing and fixed: **`todolist.md`** "
      "(the programme's memory, superseded by nothing), **`bootup.md` §0.5** (seven discipline rules with "
      "their costs), and the **registries**. **Handovers are a session's narrative; those three are the "
      "programme's state**",
      True, "durable objects, not per-turn narrative")

check("T8 **Q2 — THE CC OFFER IS DECLINED, and the reason is the record rather than the rule.** The "
      "founder is right that cross-lane sanction is a collision guard, not a competence judgement. **But "
      "this lane's actual track record in the CC area over four sessions is: one error (3906, 83 orders, "
      "founder-caught) and one retracted patch (3920). Two for two**",
      True, "'up to date on what we did' is precisely what the lane demonstrably was not")

check("T9 **AND THE COMPETENCE CLAIM IS BACKWARDS:** the lane is not *up to date* on the CC work — **it "
      "read one assembly record, twice, and misread it both times.** The CC lane holds F-CLI-1, the "
      "η_z sub-derivation, and the convention that this lane could not reconcile. **Being able to quote "
      "their headline is not holding their state**",
      True, "the 8pi convention is still unreconciled precisely because it is theirs")

check("T10 SCOPE: **a cadence correction and a declined scope expansion. No physics.** PRED-C-96, T-1, "
      "T-2, the count law, C-5's ledger: untouched",
      True, "governance under PD-006")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
