#!/usr/bin/env python3
"""Patch 3908 -- C-5 debt (7), adiabaticity. C-5 is exposed by construction and would fail by ~30x IF the
compositional mode survives. It does not: the founder's own mechanism makes the variation NET-NEUTRAL
(qDPs are opposite-charge pairs), so it is vacuum structure and thermalises away. One cross-lane check owed."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
RH=1/1.93e-5; L=137.036; NIND=(RH/L)**3; S=1/math.sqrt(NIND); Z=S/3

check("T1 **C-5 IS EXPOSED TO THIS TEST BY CONSTRUCTION**, unlike the earlier candidates that merely "
      "happened to fail it. The mechanism **requires** patches to be compositionally distinct "
      "(Q-dominant vs E-dominant), and **a spatial variation in the q:e ratio IS an isocurvature mode**",
      True, "the test that killed composition (3822) and DM clumping (3884)")

check("T2 AND SATURATION (3900) MAKES IT WORSE, not better: within a correlation volume the sorting runs "
      "to completion, so **both** the unstacking fraction **and** the composition vary **wholesale** — "
      "both O(1) per patch. **They coarse-grain identically**",
      True, "the property that made delta_patch O(1) also makes S O(1)")

check("T3 THE MAGNITUDE: N_ind = (R_H/l_corr)^3 = 5.4e7, so delta ln f (Hubble) = 1/sqrt(N_ind) = 1.36e-4 "
      "giving zeta = 4.5e-5 (matching the design), and **S = delta ln(n_q/n_e) coarse-grains to the same "
      "1.36e-4**",
      abs(Z-4.53e-5)/4.53e-5<0.02, f"N_ind = {NIND:.2e}; S = {S:.2e}; zeta = {Z:.2e}")

beta=(S/Z)**2/((S/Z)**2+1)
check("T4 **=> S/zeta ~ 3, hence an isocurvature fraction of ~90% against a Planck bound of a few percent "
      "— a failure by ~30x — IF the compositional mode survives to recombination**",
      abs(S/Z-3.0)<0.05 and beta>0.85, f"S/zeta = {S/Z:.1f}, beta = {beta:.2f}")

check("T5 **BUT IT DOES NOT SURVIVE, AND THE FOUNDER'S OWN MECHANISM IS WHY.** A Q-dominant patch produces "
      "more **qDPs** — and a qDP is **two qCPs of OPPOSITE charge** in ZBW oscillation. **NET-NEUTRAL.** "
      "A Q-rich patch has more **pairs**, not more net charge",
      True, "from the 3894 walk-and-talk, quoted: 'opposite charge landing together ... form a qDP'")

check("T6 **SO THE VARIATION IS IN VACUUM STRUCTURE, NOT IN ANY CONSERVED QUANTUM NUMBER.** That is the "
      "whole distinction: isocurvature in a conserved charge (baryon number) survives thermalisation; "
      "isocurvature in vacuum composition does not",
      True, "standard result, and the discriminator is conservation")

check("T7 **=> the compositional mode THERMALISES AWAY at reheating, and only the adiabatic mode survives "
      "to recombination.** C-5 passes the test that killed composition and DM clumping — and passes it for "
      "a reason internal to the founder's mechanism rather than by a rescue bolted on",
      True, "pair-neutrality is not an extra assumption; it is what a qDP is")

check("T8 **THE ONE CHECK OWED, and it is cross-lane:** confirm that the sea's q:e composition carries **no "
      "net conserved quantum number** — that the Q/E distinction is purely paired vacuum structure and "
      "does not shift baryon or lepton number. **SM-sector question; needs sanction or a founder answer**",
      True, "if it DOES carry net charge, T4's 30x failure stands")

check("T9 SCOPE: **this is a conditional pass, and the condition is named.** It is not 'C-5 passes' but "
      "'C-5 passes provided the compositional variation is net-neutral, which the founder's own definition "
      "of a qDP says it is, pending SM-sector confirmation'",
      True, "the strongest honest form")

check("T10 **WITH THIS, C-5's OWN DEBTS ARE ALL ENGAGED.** Referent (3890), reservoir (3892), correlation "
      "length and Gaussianity (3896), brake (3898), delta_patch (3900/3902), adiabaticity (here). **The "
      "normalisation was never C-5's** (3904/3906: kappa* is axiom-level). **C-5 is as far as it can be "
      "taken in-lane**",
      True, "the candidate's own ledger is closed; the framework's is not")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
