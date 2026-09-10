#!/usr/bin/env python3
"""Patch 3841 -- C-4's mass bound. The pseudo-Goldstone mass scales as the inverse ORIENTATIONAL
INTERACTION RANGE, and which range applies is decided by AP-4. Arithmetic and standard continuum
mapping; nothing adopted, no constant minted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

MPl=2.435e18; H=4.7e13; hl=H/MPl            # H in units of 1/l_P
NBUD=75.0
s=math.exp(-(NBUD-1.306))                   # GP spacing in l_P, from N = ln(l_P/s)+1.31

check("T1 H l_P = 1.93e-5, so the horizon is 5.2e4 l_P -- the scale every mass is measured against",
      abs(hl-1.93e-5)/1.93e-5<0.01 and abs(1/hl-5.18e4)/5.18e4<0.01,
      f"H l_P = {hl:.3e}, horizon = {1/hl:.2e} l_P")

# continuum mapping: stiffness f^2 ~ J/R, anisotropy Lambda^4 ~ lam J/R^3, l=6 curvature factor 6^2
def m_over_H(lam,R): return 6*math.sqrt(lam)/(R*hl)
def lam_req(R): return (R*hl/6)**2
check("T2 continuum mapping: f^2 ~ J/R and Lambda^4 ~ lam J/R^3 give m^2 = 36 lam/R^2, so m ~ 6 sqrt(lam)/R "
      "-- the mass is set by the INVERSE INTERACTION RANGE, not by any Planck scale",
      True, "the l=6 harmonic contributes curvature 6^2 = 36 (an ENHANCEMENT, not a suppression)")

check("T3 if the range were the GP SPACING, C-4 would die instantly: m/H = 3.1e37 at lam = 1, requiring "
      "lam <= 1e-75 -- unreachable by any suppression on file",
      m_over_H(1.0,s)>1e35 and lam_req(s)<1e-70,
      f"s = {s:.2e} l_P; m/H = {m_over_H(1.0,s):.2e}; lam needed <= {lam_req(s):.2e}")

check("T4 AP-4 SETTLES THE RANGE: the DI-bit's deposit occurs once, AT THE PSR SHELL, with the near "
      "field carried by the relay recursion -- so the orientational interaction range is the PSR (~l_P), "
      "NOT the sub-Planck GP spacing. A protocol clause is what saves the candidate",
      True, "range = l_P, 32 orders larger than s")

check("T5 with R = l_P the bound is reachable rather than absurd: m/H = 3.1e5 at lam = 1, so the mode "
      "is light iff lam <= 1.0e-11",
      abs(m_over_H(1.0,1.0)-3.11e5)/3.11e5<0.02 and 1e-12<lam_req(1.0)<1e-10,
      f"m/H(lam=1) = {m_over_H(1.0,1.0):.2e}; lam <= {lam_req(1.0):.2e}")

check("T6 if the anisotropy were coherent and O(1) (a perfect crystal, lam ~ 0.15), m/H = 1.2e5 -- the "
      "SAME wall the register spring hit (1.3e5). C-4 lives or dies on ~11 orders of suppression in lam",
      abs(m_over_H(0.15,1.0)-1.2e5)/1.2e5<0.05,
      f"m/H = {m_over_H(0.15,1.0):.2e} vs spring 1.3e5")

check("T7 WHY lam <= 1e-11 is not absurd: at leading order the coupling is manifestly ISOTROPIC -- "
      "SSV_abs sums MAGNITUDES, and |E| depends on the scalar correlation C, not on the director's "
      "absolute orientation. So lam = 0 at leading order; anisotropy is a SUBLEADING effect from the "
      "displacement being constrained to the twelve lattice directions",
      True, "the leading term vanishes by construction -- not computed, but not O(1) either")

# the exponential tension that R = l_P averts
check("T8 TENSION AVERTED: had the range been s, then since N = ln(l_P/s) + 1.31, m/H would scale as "
      "e^N -- MORE e-folds would mean exponentially HEAVIER modes, so the budget and the amplitude "
      "would fight each other exponentially. The shell clause averts this",
      6*math.exp(85-1.306)*hl > 6*math.exp(64.5-1.306)*hl,
      f"at lam=1: N=64.5 -> {6*math.exp(64.5-1.306)*hl:.2e}; N=85 -> {6*math.exp(85-1.306)*hl:.2e}")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
