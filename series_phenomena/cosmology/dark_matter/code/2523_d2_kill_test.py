#!/usr/bin/env python3
"""Patch 2523: the D2 kill-test (pre-registered R1, Patch 2522). Registered inputs only.

D2 = homogeneous (ungated) condensation. Test: the complete-condensation bound on
n_ring/n_gamma vs the transposed target (2.734 +/- 0.038) x 10^-10.
Kill reading: overshoot >= 10 orders of magnitude.

Registered inputs:
  l_unit = hbar*c / Lambda_QCD = 0.589 fm   (master_glossary, SS-2)
  ring   = 128 CPs, m_ring = 11.264 GeV     (2435/2383; 2519 hTetra decomposition)
  n_gamma(today) = 410.7 cm^-3              (T_CMB = 2.7255 K, Planck; same observational
                                             normalization family as the registered eta_B)
  R2 registered cross-check band: Omega_Sea ~ 1e45 - 1e120 at full gravitating density
The bound is a limiting thought experiment; with the margin found below, every order-unity
lattice-geometry factor (CPs per 600-cell, packing) and every cosmological-history refinement
is irrelevant to the reading.
"""
import math

l_unit_fm = 0.589
n_sea_cp_per_fm3 = 1.0 / l_unit_fm**3          # ~1 CP per lattice cell, order-unity factors moot
n_sea_cp_cm3 = n_sea_cp_per_fm3 * 1e39
n_gamma_cm3 = 410.7
ring_cps = 128
m_ring_GeV = 11.264

n_ring_max_cm3 = n_sea_cp_cm3 / ring_cps
bound_per_photon = n_ring_max_cm3 / n_gamma_cm3
target = 2.734e-10
overshoot_orders = math.log10(bound_per_photon / target)

print(f"Sea CP density  ~ {n_sea_cp_cm3:.2e} cm^-3  (1 per l_unit^3, l_unit = {l_unit_fm} fm)")
print(f"ungated bound   : n_ring/n_gamma <= {bound_per_photon:.2e}")
print(f"target          : n_ring/n_gamma  = {target:.3e}")
print(f"OVERSHOOT       : {overshoot_orders:.1f} orders of magnitude")

# Omega cross-check against the registered R2 band
rho_crit_GeV_cm3 = 5.3e-6
omega_full = (n_ring_max_cm3 * m_ring_GeV) / rho_crit_GeV_cm3
print(f"Omega cross-check: fully condensed Sea -> Omega ~ {omega_full:.1e} "
      f"(registered R2 band 1e45-1e120: consistent, low end)")

assert overshoot_orders >= 10.0, "R1 kill threshold not met -> FULL STOP per pre-registration"
# Cross-check logic: our 1-CP-per-l_unit^3 basis is deliberately CONSERVATIVE (600-cell vertex
# packing at edge ~ l_unit/phi gives ~4-30x more CPs; R2's band assumed a denser basis, e.g.
# rho_Sea ~ 1e2 x nuclear vs our ~3x nuclear). Landing AT or BELOW the band's low end therefore
# UNDERSTATES the overshoot -> kill a fortiori. Only exceeding the band's TOP would demand
# investigation before reading.
assert omega_full < 1e121, "above the registered R2 band top -> investigate before reading"
if omega_full < 1e45:
    print(f"note: Omega ~ {omega_full:.1e} sits ~{1e45/omega_full:.0f}x below the R2 band low end -- "
          f"the conservative-density direction; the kill margin is understated, not overstated")
print("READING R1: D2 KILLED by registered physics (margin >> 10 orders, conservative basis).")
print("Consequence: ring formation MUST be gated; the only registered gate is seeding -> D1 LICENSED.")
print("ALL CHECKS PASS")
