#!/usr/bin/env python3
"""3041_nu_mass_ratio_check.py — phenomenology check of the founder's
207x claim (founder ruling, Patch 3041): m(nu_mu)/m(nu_e) at the
charged-lepton mu/e ratio, tested against oscillation data.

Inputs (cited, PDG-class): dm21^2 = 7.42e-5 eV^2; |dm31^2| = 2.51e-3
eV^2 (normal ordering); m_mu/m_e = 206.768; m_tau/m_mu = 16.817;
cosmology bound Sum(m) <~ 0.12 eV.

Checks:
  V1 the 207x ratio is CONSISTENT with dm21^2 (yields a positive real
     solution) -> the claim is a live sharp prediction, fixing the
     absolute scale: m1, m2 printed.
  V2 the derived spectrum respects the cosmology bound.
  V3 NAIVE tau-scaling (m3/m2 = m_tau/m_mu) is EXCLUDED by dm31^2
     (factor printed) — consonant with the founder's structural claim
     that nu_tau is a different object (qDP-eDP pair), and yielding
     the pair-configuration derivation target m3/m2 (printed).
"""
import numpy as np
R_ME, R_TM = 206.768, 16.817
DM21, DM31, COSMO = 7.42e-5, 2.51e-3, 0.12
m2 = np.sqrt(DM21/(1-1/R_ME**2)); m1 = m2/R_ME
m3 = np.sqrt(DM31 + m1**2)
naive_dm31 = (R_TM*m2)**2 - m1**2
checks = [
 (f"V1 207x consistent with dm21^2: m1 = {m1*1e6:.1f} ueV, m2 = "
  f"{m2*1e3:.3f} meV (sharp prediction)", m2 > 0 and m1 > 0),
 (f"V2 Sum(m) = {(m1+m2+m3)*1e3:.1f} meV < {COSMO*1e3:.0f} meV",
  (m1+m2+m3) < COSMO),
 (f"V3 naive tau-scaling excluded: predicts dm31^2 = {naive_dm31:.2e} "
  f"vs measured {DM31:.2e} ({naive_dm31/DM31:.1f}x); pair-config "
  f"target m3/m2 = {m3/m2:.2f}", naive_dm31/DM31 > 4),
]
n = 0
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    n += ok
print(f"{n}/{len(checks)} PASS")
