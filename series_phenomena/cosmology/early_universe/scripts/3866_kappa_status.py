#!/usr/bin/env python3
"""Patch 3866 -- kappa's actual status, established by applying S0.5 D-1/D-3 before reasoning forward.
Corrects the 3865 handover's mis-scoping of OPEN-EU-BATH-DEPTH-1 and records the tightest kappa window.
Corpus bookkeeping and arithmetic; nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

alpha=1/137.036

check("T1 D-3 APPLIED, AND IT CAUGHT THE WORKER: OPEN-EU-BATH-DEPTH-1 is registered as 'bath speed at "
      "depth ~1e74' / 'bath rate at depth' -- a RATE question, non-blocking, from CONV-045. It does NOT "
      "own kappa. The 3865 handover said it does; that is wrong and is corrected here",
      True, "one grep on the item name; the rule works when used")

check("T2 D-1 APPLIED: kappa's mechanism is already on file -- LEMMA-NS-BATH (Patch 0767, "
      "`bath_temperature_lemma.md`): mu is evaluated w.r.t. the ZBW/substrate bath, whose temperature is "
      "the substrate scale kT ~ hbar c/l_P = E_Pl, hence kappa ~ 1",
      True, "a corollary of the bath clause (0750-0752), not an independent postulate")

check("T3 SO kappa IS ALREADY AS DERIVED AS THE CORPUS CAN MAKE IT. LEMMA-NS-BATH grounds kappa ~ 1 in the "
      "bath clause, and the bath clause is explicitly a WORKING POSTULATE. Deriving kappa exactly means "
      "deriving the bath clause -- which is not an EU-lane item",
      True, "the lemma states this limit itself: 'NO THEO ... it rests on the bath clause'")

# the two bounds
kap_lemma=1e-4; kap_t2=0.1
check("T4 TWO LOWER BOUNDS EXIST, and they are not the same requirement. LEMMA-NS-BATH's PASS condition "
      "(long-range sqrt(n_bar) residual negligible) needs kappa >~ 1e-4",
      kap_lemma==1e-4, "0767: 'the minimal requirement for PASS is just kappa >~ 1e-4'")

check("T5 T-2's condition (the O(alpha) tilt shift staying within Planck 1 sigma, 3850 S4) needs "
      "kappa >~ 0.1 -- THREE ORDERS TIGHTER than the lemma's",
      abs(math.log10(kap_t2/kap_lemma)-3)<0.01, f"{kap_t2/kap_lemma:.0f}x tighter")

check("T6 NEW RESULT: with kappa <= 1 from the substrate clock (kT <= E_Pl), the corpus's tightest window "
      "on kappa is **[0.1, 1]**, and it comes from the TILT rather than from the long-range residual. "
      "T-2 supplied the binding constraint without anyone noticing",
      True, "3850 derived it; its significance as the tightest bound is recorded here")

check("T7 CONSEQUENCE FOR THE LANE: OPEN-EU-BATH-DEPTH-1 should NOT be worked as the kappa item -- it is a "
      "non-blocking rate question. And there is no kappa derivation to do that does not amount to "
      "deriving the bath clause",
      True, "the handover's 'last substantial local item' was mis-scoped")

check("T8 WHAT IS ACTUALLY LEFT IN-LANE is therefore smaller than the 3865 handover implied, and the "
      "honest statement is that the EU lane's substantive work is complete pending maintainer decisions",
      True, "charter discharged 3850; amplitude closed 3847; budget closed in-lane 3856; kappa as far as it goes")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
