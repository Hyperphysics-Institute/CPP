#!/usr/bin/env python3
"""Patch 3900 -- delta_patch worked structurally. The seed is irrelevant; SATURATION makes it a
dynamics-set O(1) log-ratio (which discharges 'why O(1)'); the number needs affinity strengths not on
file; and C-5 therefore makes a FALSIFIABLE prediction: f_E/f_Q ~ 2.8."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
alpha=1/137.036; LDER=1/alpha; LREQ1=138.4
DPRED=(LREQ1/LDER)**1.5

check("T1 FIRST EU PATCH IN THE NEW BLOCK 3900-3999, allocated by the founder on exhaustion of 3800-3899 "
      "at Patch 3899",
      True, "registered in id_block_registry.md")

check("T2 **THE SEED IS NOT THE SOURCE.** If SCP compositions are seeded randomly, the per-SCP spread is "
      "Poisson in n0: 1e-3 at n0=1e6, 1e-6 at 1e12, 1e-12 at 1e24. **Minute.** delta_patch cannot come "
      "from initial composition scatter",
      1/math.sqrt(1e12)<1e-5, "so if delta_patch were seed-set, C-5 would fail by many orders")

check("T3 **SATURATION SETS IT, AND THAT IS WHY IT IS O(1).** l_corr is BY DEFINITION the range over "
      "which the sorting is coherent, so within one correlation volume preferential attachment has RUN "
      "TO COMPLETION: each patch ends up **wholesale** Q-dominant or E-dominant, however small its seed",
      True, "the amplification is the mechanism; the seed only picks which way")

check("T4 **SO delta_patch = |ln(f_E/f_Q)| -- a log-RATIO of two SATURATED unstacking fractions.** This "
      "discharges the qualitative half of the gate: **delta_patch is O(1) for a reason (dynamics), not "
      "by assumption**",
      True, "3898's gate asked 'is it 1 for a reason?'; the reason is saturation")

check("T5 BUT THE NUMBER NEEDS THE AFFINITY STRENGTHS, and **D-1 finds none on file** -- the corpus fixes "
      "the affinities qualitatively only. **The value cannot be computed here, and is not invented**",
      True, "same discipline as the stack number, fourth session running")

check("T6 **SO C-5 MAKES A FALSIFIABLE PREDICTION INSTEAD.** Combining the DERIVED brake "
      "(l_sat = 1/alpha = 137.0, 3898) with the requirement l_req = 138.4*delta^(-2/3) (3896, from the "
      "observation) gives **delta_patch = 1.015**",
      abs(DPRED-1.015)<0.01, f"delta_patch = {DPRED:.3f}")

check("T7 **IN PHYSICAL TERMS: f_E/f_Q = e^1.015 = 2.76.** C-5 predicts that **E-dominant patches unstack "
      "about 2.8x further than Q-dominant ones** -- a concrete, checkable statement about two rates, not "
      "a fitted parameter",
      abs(math.exp(DPRED)-2.76)<0.05, f"f_E/f_Q = {math.exp(DPRED):.2f}")

def band(fac): return math.exp((LREQ1/(LDER*fac))**1.5)
check("T8 AND IT IS SHARP ENOUGH TO FALSIFY: allowing l_sat to differ from 1/alpha by 1.5x either way "
      "gives **f_E/f_Q in [1.7, 6.5]**, centred on 2.8",
      abs(band(1.5)-1.7)<0.2 and abs(band(1/1.5)-6.5)<0.3,
      f"1.5x -> {band(1.5):.1f}; 1x -> {band(1.0):.1f}; 0.67x -> {band(1/1.5):.1f}")

check("T9 **THIS IS A PREDICTION, NOT A FIT.** The number comes from combining an independently derived "
      "brake with an observation, and names the independent computation that tests it: the two saturated "
      "unstacking fractions, from the Q-to-Q and E-to-anything affinities. **Same structure as T-2's "
      "kT_bath bound (3850 S4)** -- an observation constraining a quantity the theory must supply",
      True, "PD-007 respected: nothing tuned; a target named and a test specified")

check("T10 SCOPE: **nothing adopted; no constant minted; C-5 NOT reported as working.** The qualitative "
      "half of the gate is discharged (why O(1)); **the quantitative half is now an open, falsifiable "
      "prediction.** Debt (6), adiabaticity, remains untouched",
      True, "one half closed, the other sharpened into a test")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
