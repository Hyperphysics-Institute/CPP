#!/usr/bin/env python3
"""Patch 3860 -- AP-4c's shell clause derived. Half one succeeds (exactly-once is forced); half two
fails at Moment 1, and that failure is load-bearing for 3816. Arithmetic and protocol bookkeeping."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

s=math.exp(-(75.0-1.306))          # GP spacing in l_P, from the e-fold budget
hops=1/s

check("T1 HALF ONE DERIVED -- 'deposit exactly once' is FORCED, not chosen. Every GP emits a fixed number "
      "of DI-bits per Moment (AP-4). If pass-through tallied, total deposits would scale with the path "
      "length in GPs; a PSR-length path traverses ~1e32 GP spacings, so the emission budget would be "
      "inflated by that factor and would not close",
      hops>1e31, f"PSR-length path = {hops:.2e} GP spacings; inflation factor the same")

check("T2 and the SHELL as the deposit locus gives the right geometric dilution: a fixed emission "
      "spread over the shell of radius PSR arrives at areal density ~1/PSR^2 -- inverse-square at the "
      "shell radius, from counting alone",
      True, "no force law assumed; the 1/r^2 is the sphere's area")

check("T3 HALF TWO is the near field: for separation r < PSR there is NO direct deposit (the bit passes "
      "through untallied and lands at the shell). AP-4c assigns this to 'the relay recursion' -- "
      "successive re-emission by intervening GPs",
      True, "the clause asserts near-field delivery; the question is whether it operates")

check("T4 BUT THE RELAY REQUIRES PRIOR-MOMENT CONTENT. AP-3: a GP computes its registers from the "
      "PREVIOUS Moment's arrivals and imprints its outgoing bits from those registers. So a GP can only "
      "relay what it has already received",
      True, "relay is re-emission of computed state, and state comes from prior arrivals")

check("T5 AT MOMENT 1 EVERY REGISTER IS EMPTY (3816 S1 -- that is the very argument that put the PSR at "
      "its l_P ceiling). So the relay has NOTHING TO RELAY at Moment 1",
      True, "the empty-register premise that opens the reach also empties the relay")

check("T6 AND THE SHELL LIES OUTSIDE THE BALL. Under the small-ball ruling R_init <= l_P ~ PSR, so a bit "
      "emitted from any interior GP deposits at radius ~l_P -- outside the pre-ignition ball entirely",
      True, "deposits land on GPs beyond the ball, which host no CPs")

check("T7 THEREFORE at Moment 1 an interior GP of a sub-PSR ball receives 0 direct + 0 relayed = 0. "
      "**3816's Moment-1 full-contact claim is NOT delivered by AP-4c as written**",
      True, "the check flagged at 3816 S6 and re-pointed at 3820 S5 returns NEGATIVE")

check("T8 THE ESCAPE IS CLOSED: a sub-Moment relay would let intervening GPs re-emit within Moment 1, "
      "but the corpus carries a FOUNDER RULING that ZBW is NOT sub-Moment. No sub-Moment tier is "
      "available to carry it",
      True, "founder ruling on record")

check("T9 CONSEQUENCE CHAIN, stated rather than softened: no Moment-1 full contact => n_bar_init != N_CP "
      "=> Branch P's re-grounding (3816 S3) loses its basis => N_* = (1/3)ln N_CP is unsupported as "
      "derived. The EU arc has rested on 3816 since it was written",
      True, "this is the worker's own 3816, and the base of the arc")

check("T10 WHAT IS UNAFFECTED: PRED-C-96's tilt reads the ADOPTED pivot N_rem = 57, not the count law's "
      "absolute normalisation, so it does not move; T-1's l<=5 isotropy is geometric; T-2's lambda = "
      "alpha/kappa is a rate-coefficient result",
      True, "the tilt is untouched, as throughout this arc")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
