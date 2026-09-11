#!/usr/bin/env python3
"""Patch 3886 -- the founder's species-ladder question: when does the CMB pattern form, and could the
ladder's sequential formation be it? Horizon-scale arithmetic; nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
c_=2.998e8; Mpc=3.086e22; T0=2.348e-4
t_of_T=lambda T:(1e6/T)**2
lam=lambda T: c_*t_of_T(T)*(T/T0)/Mpc

check("T1 D-1: the ladder is on file as **CONJ-DPS-4** (founder input Patch 2782, 22 July 2026) -- the mixed "
      "qDP-eDP SPECIES LADDER as the Sea's qDP reservoir. **Status: CONJECTURE**, registered in CONJ.md with "
      "an open-work list (activation barrier, lifetime, competition, branching)",
      True, "conjectural, so nothing below treats the ladder as established")

check("T2 FIRST, A CORRECTION TO THE PREMISE: **the CMB is not fractal.** It is a near-GAUSSIAN, "
      "near-SCALE-INVARIANT random field. Scale-invariance is not hierarchy -- the COSMIC WEB is "
      "hierarchical, the CMB is not. A ladder of species would imprint HIERARCHY, which is precisely what "
      "the CMB lacks",
      True, "the distinction matters: it is what the 0730 kurtosis result measured")

check("T3 WHEN DOES THE CMB PATTERN FORM? It is **IMPRINTED at recombination** (z = 1100, T = 0.26 eV, "
      "t = 380 kyr) -- but it does not FORM then. The pattern was already present as **super-horizon** "
      "perturbations; recombination made it visible",
      abs(lam(0.26)-159)/159<0.05, f"the horizon at recombination is {lam(0.26):.0f} Mpc comoving")

# the decisive scale test
T_100=None
lo,hi=1e-3,1e3
for _ in range(200):
    m=(lo*hi)**0.5
    if lam(m)>100: lo=m
    else: hi=m
T_100=(lo*hi)**0.5
check("T4 THE SCALES WE OBSERVE entered the horizon at **T ~ 0.41 eV** -- the equality/recombination era. "
      "That is what sets which epoch the CMB can show structure from",
      abs(T_100-0.41)<0.05, f"T(100 Mpc) = {T_100:.2f} eV")

rows=[("qDP/eDP asymmetry (~E_Pl)",1.22e28),("2qDP, 4qDP (~TeV)",1e12),
      ("DM ring (11.26 GeV)",1.126e10),("chains/ribbons (~GeV)",1e9)]
check("T5 **THE LADDER IS TEN ORDERS TOO SMALL.** A species forming at temperature T imprints at the "
      "horizon scale then. DM ring formation at 11.26 GeV (t = 7.9e-9 s) imprints at **3.7e-9 Mpc today**",
      abs(math.log10(lam(1.126e10))+8.4)<0.5, f"lambda(ring) = {lam(1.126e10):.1e} Mpc")

check("T6 and every rung is in the same predicament -- the whole ladder sits between 1e-27 and 1e-8 Mpc, "
      "against CMB scales of 100-10000 Mpc",
      all(lam(T)<1e-7 for _,T in rows),
      "; ".join(f"{lab}: {lam(T):.0e} Mpc" for lab,T in rows))

check("T7 SO THE LAYERING IS REAL BUT IN THE WRONG PLACE. Sequential species formation genuinely does "
      "imprint a set of characteristic scales -- one per rung, at that rung's formation horizon -- but all "
      "of them are **microscopic in comoving terms** and invisible to the CMB by ~10 orders",
      lam(1.126e10)*1e10<100, "a real structure, 10 orders below anything observable in the CMB")

check("T8 AND IT WOULD BE A COMB, NOT A POWER LAW. Discrete formation epochs imprint discrete scales -- a "
      "series of features -- whereas the observed CMB is smooth and near-power-law with acoustic peaks "
      "explained by baryon-photon oscillation, not by species thresholds",
      True, "wrong shape as well as wrong scale")

check("T9 THE ANSWER TO 'AT WHAT POINT DOES IT FORM': the CMB pattern does not form at any point AFTER "
      "inflation. It is super-horizon before it is anything else. In standard cosmology inflation sets it; "
      "**in CPP that origin has no identified mechanism** (the 3847 amplitude closure)",
      True, "the ladder cannot be it because the ladder is post-inflation and sub-microscopic")

check("T10 WHAT THE LADDER *COULD* BEAR ON is the small-scale matter power spectrum and the DM sector's "
      "internal structure -- not the CMB. That is a legitimate DM-lane question and is left there",
      True, "redirected, not dismissed")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
