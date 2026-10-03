#!/usr/bin/env python3
"""Patch 4378 - founder (3 Oct 2026): light bending near the Sun comes from grad SSV_abs; the shell-thickness
change is insignificant there.  Check: how a clock effect from the shell scales against the bending.
GR-1i (L575-577): half of the light-bending index n - 1 comes from the slowed clock rate, so a clock effect
enters the bending directly.  Near the Sun the fill change is first order in U, like the bending itself.
"""
G, M, c, R = 6.674e-11, 1.989e30, 2.998e8, 6.957e8
U = G * M / (c * c * R)
print(__doc__)
print(f"Sun's surface: U = {U:.2e}; fill change dg ~ 3U = {3*U:.1e}")
print("clock effect LINEAR in the fill change, X = 1 - a*dg: its share of the bending ~ a, the same at every U;")
print("   Cassini (|gamma - 1| < 2.3e-5) -> a < ~8e-6 (4373)")
rho = U / 2
print(f"clock effect SQUARE in the stress, X = 1 - rho^2 (Einstein's form): share of the bending ~ rho^2/U = {rho**2/U:.1e}")
print("   -> invisible near the Sun; the founder's 'insignificant' holds for the square-law (stretch) case only.")
