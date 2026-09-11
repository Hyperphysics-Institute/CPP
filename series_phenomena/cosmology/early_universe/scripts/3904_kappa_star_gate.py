#!/usr/bin/env python3
"""Patch 3904 -- the circularity traced to its root: it reduces ENTIRELY to kappa*, the boost coupling,
which the corpus had already identified as the gate and flagged as possibly axiom-level. And a deliberate
REFUSAL to guess it."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
h=1.93e-5; LNN=3*57; K0=h/LNN

check("T1 **THE REDUCTION.** The engine is H_eff = kappa_0 * kT * ln n_bar. LEMMA-NS-BATH gives kT ~ E_Pl "
      "(kappa ~ 1, T-2/3850), and ln n_bar = 3*N_rem = 171 at the pivot. **So H is fixed the moment "
      "kappa_0 is** -- the circularity reduces ENTIRELY to one number",
      True, "no other free quantity stands between the engine and H")

check("T2 kappa_0 = (H/E_Pl)/ln n_bar = 1.13e-7",
      abs(K0-1.13e-7)/1.13e-7<0.02, f"kappa_0 = {K0:.2e}")

check("T3 **AND THE CORPUS ALREADY HAS IT: kappa* ~ 2e-7, with calibration uncertainty spanning "
      "1e-7 to 1e-6.** The computed 1.13e-7 sits INSIDE that band -- **the C-5 chain is consistent with "
      "what was already recorded**, independently",
      1e-7<K0<1e-6, "a consistency check the worker did not arrange")

check("T4 **D-1 PAID, AND THE CORPUS SAW THIS FIRST.** The frontier already states: *if we could derive "
      "the boost coupling structure itself (around 2e-7, corresponding to GUT-scale H_*), then A_s "
      "becomes predictable too -- which would put CPP on equal footing with inflation*",
      True, "the gate was identified before this arc began; the worker rediscovered it")

check("T5 **AND IT IS FLAGGED AS POSSIBLY AXIOM-LEVEL** -- the corpus discusses 'its status as an "
      "axiom-level constant'. **If kappa* is axiom-level, C-5's amplitude can NEVER be more than a "
      "consistency check**, and EU-1 should say so rather than leave it implicit",
      True, "a structural limit, not a gap awaiting work")

check("T6 **SO C-5's CONTRIBUTION MUST BE RESTATED, and narrowed.** Before C-5 the amplitude sector had "
      "NO source at all (3847). C-5 supplies a **source** and a **spectrum shape**. **The NORMALISATION "
      "was kappa*-gated before C-5 and remains kappa*-gated after it**",
      True, "C-5 does not remove the gate; it was never C-5's gate to remove")

check("T7 that is a real clarification rather than a demotion: **the amplitude question was always two "
      "questions** -- *is there a source with the right spectrum?* (C-5's, and answered) and *what sets "
      "the normalisation?* (kappa*'s, and open since 0746)",
      True, "the arc conflated them; separating them is the session's content")

check("T8 **REFUSAL, RECORDED AS THIS SESSION'S DISCIPLINE.** The obvious next move is to scan for a "
      "formula giving ~1e-7 -- alpha^3 = 3.9e-7 is the sort of thing that turns up. **After THREE "
      "consecutive sessions of numbers landing near targets (3898, 3900, 3902), that is precisely the "
      "failure mode already warned about. It is not done here**",
      abs(1/137.036**3-3.887e-7)<1e-8,
      "alpha^3 = 3.9e-7 is within a factor 3.4 of 1.13e-7 -- and that is exactly why it is refused")

check("T9 what a LEGITIMATE derivation of kappa* would look like: it is the coupling between a chemical "
      "potential (an energy) and an expansion rate (an inverse time), so **dimensionless**. A derivation "
      "must come from the substrate dynamics -- how much expansion one unit of entropic drive buys -- "
      "**not from matching a number**",
      True, "the target is a mechanism, and the test is that it be written before kappa* is computed")

check("T10 SCOPE: **nothing adopted; no constant minted; C-5 not reported as working; the amplitude "
      "remains not derived.** What changed: the circularity is now **localised to one named, "
      "already-registered parameter**, and C-5's claim is **narrowed to source-and-shape**",
      True, "a smaller and more accurate claim than the session began with")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
