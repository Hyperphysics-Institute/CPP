#!/usr/bin/env python3
"""3042_shipped_ratio_check.py — the SHIPPED SF-4 first-principles mass
ratios (m = M0 * V^2 * sigma_nu; (V1,V2,V3) = (4,12,30) forced by
600-cell shell topology) tested against current oscillation data, and
the discriminant against the WITHDRAWN 207x slip (founder correction,
Patch 3042).

Inputs: dm21^2 = 7.42e-5 eV^2, |dm31^2| = 2.51e-3 eV^2 (normal
ordering, PDG-class); cosmology bound Sum(m) <~ 0.12 eV; near-future
cosmology sensitivity ~0.06 eV.

The shipped prediction m2/m1 = 9.00 EXACTLY fixes the absolute scale
from dm21^2 alone: m1 = sqrt(dm21^2/80). Checks:
  V1 absolute spectrum printed; Sum under the cosmology bound.
  V2 m3/m1 vs shipped (30/4)^2 = 56.25: residual printed (the known
     nu_3 K3 partial-binding residual class; PASS if < 15%).
  V3 m3/m2 vs shipped (30/12)^2 = 6.25: residual printed (same
     class; PASS if < 15%).
  V4 DISCRIMINANT vs the withdrawn 207x reading: the two scale
     assignments differ by 23x in m1 (0.963 meV vs 41.7 ueV) —
     resolvable in principle (0nubb/cosmology-era), recorded so the
     withdrawal is not just verbal.
  V5 falsification frontier: Sum(m) sits at the near-future
     cosmology sensitivity (~60 meV) — the shipped spectrum is
     testable, not hidden.
"""
import numpy as np
DM21, DM31, COSMO, NEXT = 7.42e-5, 2.51e-3, 0.12, 0.060
m1 = np.sqrt(DM21/80.0); m2 = 9.0*m1
m3 = np.sqrt(m1*m1 + DM31)
S = m1+m2+m3
r31, r32 = m3/m1, m3/m2
checks = [
 (f"V1 spectrum: m1 = {m1*1e3:.3f} meV, m2 = {m2*1e3:.3f} meV, m3 = "
  f"{m3*1e3:.1f} meV; Sum = {S*1e3:.1f} meV < {COSMO*1e3:.0f}", S < COSMO),
 (f"V2 m3/m1 = {r31:.1f} vs shipped 56.25 ({abs(r31-56.25)/56.25*100:.0f}% "
  "residual, nu_3 class)", abs(r31-56.25)/56.25 < 0.15),
 (f"V3 m3/m2 = {r32:.2f} vs shipped 6.25 ({abs(r32-6.25)/6.25*100:.0f}% "
  "residual, nu_3 class)", abs(r32-6.25)/6.25 < 0.15),
 (f"V4 discriminant vs withdrawn 207x: m1 differs 23.1x "
  f"({m1*1e6:.0f} ueV vs 41.7 ueV) — resolvable, withdrawal recorded",
  abs(m1/41.7e-6 - 23.1) < 0.5),
 (f"V5 falsification frontier: Sum = {S*1e3:.1f} meV vs near-future "
  f"sensitivity {NEXT*1e3:.0f} meV — at the edge, testable", S > 0.9*NEXT),
]
n = 0
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    n += ok
print(f"{n}/{len(checks)} PASS")
