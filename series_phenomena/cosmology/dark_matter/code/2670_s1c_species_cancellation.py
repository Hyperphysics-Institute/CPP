#!/usr/bin/env python3
"""FA-SEA-GREEN S1c verify (Patch 2670, fork-blind).

Verifies (i) the species-universal gap cancellation omega_A = 2c/d_DP
from the registered constituent values, and (ii) the discrete-scatterer
regime inequality kappa * l_edge = 2 > 1.

BLIND-GUARD AUDIT: no screening length computed or printed; no candidate
value; no decay quantity; no curve.
"""
import math

# Registered constituent values [0880/0886, 2452]
species = {"qDP": (264.0, 132.0), "eDP": (88.0, 44.0)}  # (E_DP, m_CP) MeV

ok = True
for name, (E, m) in species.items():
    val = math.sqrt(2.0 * E / m)  # omega_A * d_DP / c
    print(f"{name}: omega_A * d_DP / c = sqrt(2*{E:.0f}/{m:.0f}) = {val:.6f}")
    if abs(val - 2.0) > 1e-12:
        ok = False

# regime inequality: kappa = 2/d_DP, with d_DP = l_edge (INF-S1C-1)
kappa_times_ledge = 2.0  # kappa * l_edge = (2/d_DP)*d_DP = 2 identically
print(f"kappa * l_edge = {kappa_times_ledge:.1f}  (> 1: discrete-scatterer regime)")
if not kappa_times_ledge > 1.0:
    ok = False

print("S1c check:", "ALL PASS" if ok else "FAIL")
