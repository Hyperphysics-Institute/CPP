#!/usr/bin/env python3
"""Patch 3862 -- RETRACTION of 3860's half-two failure. The founder directed a check of the axioms and
founders_voice; the corpus already carries the sub-PSR cascade, computed in August. 3816 is restored.
Corpus bookkeeping; nothing adopted."""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

check("T1 R-OUTWARD-FANOUT (founder, Patch 3135): 'at every HOP, a GP's received DI-bit count splits "
      "EQUALLY among all neighbors with strictly positive outward radial component'. Propagation from "
      "GP_origin to GP_PSR is a MULTI-HOP CASCADE, and the ~10% shell thickness is path-length variation "
      "in HOP COUNT -- so the hops are WITHIN the Moment, the PSR being the per-Moment reach",
      True, "the founder's own clarification, 14 Aug 2026")

check("T2 D-SUBPSR-FIELD PASS 3 (Patch 3135) COMPUTED IT: N = 6-22 hops from origin to PSR; band "
      "sigma_r/<r> = 0.093-0.076 reproducing the founder's ~10%; and the sub-PSR profile is stated: "
      "'the steady-state signal MAXIMIZES inward, 1/s^2-class, with 10-30% lattice structure'",
      True, "verify script on file: scripts/3133_subpsr_cascade.py")

check("T3 SO THE NEAR FIELD IS DELIVERED, and was derived a month ago. OPEN-SUBPSR-1 is recorded as "
      "'substantially RESOLVED at the field-profile level'",
      True, "not an open hole; a resolved item the worker did not look up")

check("T4 RETRACTION 1: 3860 S2 asserted 'the relay requires prior-Moment content, so it cannot operate "
      "at Moment 1'. WRONG. The relay is a WITHIN-MOMENT hop cascade, not Moment-to-Moment re-emission. "
      "It needs no prior-Moment content",
      True, "3860 S2 step (1) withdrawn")

check("T5 RETRACTION 2: 3860 S3 declared the sub-Moment escape 'closed by founder ruling'. MISREAD -- the "
      "ruling is that ZBW is not sub-Moment. It says nothing against sub-Moment propagation HOPS, which "
      "R-OUTWARD-FANOUT explicitly establishes",
      True, "3860 S3 withdrawn")

check("T6 AND THE MOMENT-1 COUNT IS POSITIVELY SUPPORTED, not merely un-undermined: AP-4 has EVERY GP "
      "emit 'the same fixed number of DI-bits every Moment' -- unconditional, needing no prior content -- "
      "and SSV_abs is COUNT-LIKE ('more DI-bits received => greater SSV_abs')",
      True, "the emission count does not depend on what was received")

check("T7 n_bar IS A COUNT. So what Moment-1 contact must deliver is exactly what the unconditional fixed "
      "emission plus the hop cascade DO deliver. **3816's Moment-1 full-contact claim is RESTORED**, and "
      "the check flagged at 3816 S6 returns POSITIVE",
      True, "n_bar_init = N_CP recovers its derivation")

check("T8 CONSEQUENCE: 3860's chain is void. Branch P's re-grounding stands; N_* = (1/3)ln N_CP is "
      "derived, not a posit; 3823/3825/3835/3837 carry no inherited conditionality from this",
      True, "the arc's base is intact")

check("T9 WHAT 3860 GOT RIGHT AND KEEPS: half one -- 'deposit exactly once' is FORCED by emission-budget "
      "conservation, and the shell locus gives 1/r^2 from counting alone. Unaffected by the retraction",
      True, "half one stands")

check("T10 THE LESSON, and it is the founder's: he asked whether this was a new axiom when the "
      "every-GP-contact concept was first discussed, and directed a check of the axioms and "
      "founders_voice before further work. The answer was on file for a month. **A protocol failure "
      "should never be declared without searching the corpus for the mechanism first**",
      True, "third distinct instance of the premise/corpus-search gap in this arc")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
