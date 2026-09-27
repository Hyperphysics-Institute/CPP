#!/usr/bin/env python3
"""4311 -- with AP-4 (fixed emission per GP) and mass = organised emitters, GR-1a's hierarchy reads
alpha_G/alpha = (m_e/m_P)^2 / alpha: gravity couples at Planck strength per Planck mass, charge at alpha per unit charge.
In counts (4301: coupling = N s/(4 pi PSR)):  N_charge = 4 pi alpha R,  N_Planck-mass = 4 pi R  (R = PSR/s)."""
import numpy as np
alpha=1/137.035999; me=9.1093837015e-31; mP=2.176434e-8
print(f"alpha_G/alpha = (m_e/m_P)^2/alpha = {(me/mP)**2/alpha:.3e}   (GR-1a eq. hierarchy)")
for R in (1e30,1e32):
    print(f"R = {R:.0e}: N_charge = {4*np.pi*alpha*R:.2e},  N_Planck-mass = {4*np.pi*R:.2e},  ratio = 1/alpha = {1/alpha:.2f}")
print("Testable relation: a Planck mass organises 1/alpha = 137.04 times the DI-bit emission of a unit charge.")
print("Equivalently, one unit charge organises alpha x (a Planck mass's emission): the electron's gravitational source")
print(f"is (m_e/m_P) = {me/mP:.2e} Planck units, its electric source alpha = {alpha:.5f} of a Planck-strength unit.")
