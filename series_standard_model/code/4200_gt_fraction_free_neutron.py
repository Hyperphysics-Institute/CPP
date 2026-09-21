#!/usr/bin/env python3
"""4200 -- how much of FREE-neutron decay is Gamow-Teller (spin-1 lepton pair) vs Fermi (spin-0).
Rate ratio GT:F = 3 g_A^2 : 1  (three spin-1 projections; g_A = 1.2754 measured, PDG)."""
gA = 1.2754
gt = 3 * gA**2
print(f"g_A = {gA};  GT:F = 3 g_A^2 : 1 = {gt:.2f} : 1")
print(f"fraction of free-neutron decays with PARALLEL lepton spins (GT) = {gt/(1+gt):.3f}")
print(f"fraction with anti-parallel lepton spins (Fermi)                = {1/(1+gt):.3f}")
