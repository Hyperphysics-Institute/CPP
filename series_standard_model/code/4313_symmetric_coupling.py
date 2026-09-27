#!/usr/bin/env python3
"""4313 -- GR-1's hierarchy F_grav/F_EM = (m/m_P)^2/(e/e_P)^2 is quadratic in each source (emitter AND interceptor).
Count rule, symmetric: coupling(A,B) = (emission_A)(interception_B)/(4 pi s PSR), normalised by 4301 so that two unit
charges (one GP each: emission N0, interception s^2) give alpha = N0 s/(4 pi PSR).  Two Planck masses couple at 1:
(G_P N0)(G_P s^2)/(4 pi s PSR) = G_P^2 alpha = 1  ->  G_P = alpha^(-1/2).  4312's linear reading gave 1/alpha; corrected."""
import numpy as np
alpha=1/137.035999; me=9.1093837015e-31; mP=2.176434e-8
GP=alpha**-0.5
print(f"G_P = 1/sqrt(alpha) = {GP:.4f} GPs per Planck unit;  G_P^2 = 1/alpha = {GP*GP:.3f} (the pair coupling, 4312's number)")
print(f"electron: charge = 1.0 GP;  mass = (m_e/m_P) x G_P = {(me/mP)*GP:.2e} GPs coherent")
print(f"GR-1: e/e_P = sqrt(alpha) = {alpha**0.5:.5f} = N0/N_P: one GP's emission over a Planck unit's")
print(f"flag (recorded, not claimed): 1/sqrt(alpha) = {GP:.3f} vs the icosahedral neighbour count 12: {(12/GP-1)*100:.1f}% apart;")
print(f"   G_P = 12 exactly would give alpha = 1/144 ({(1/144/alpha-1)*100:+.1f}% in alpha).")
