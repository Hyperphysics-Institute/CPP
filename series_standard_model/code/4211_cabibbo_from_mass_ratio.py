#!/usr/bin/env python3
"""4211 -- the textbook Gatto-Sartori-Tonin relation, as the TARGET a two-basis-misalignment picture of CKM aims at.
Not a CPP derivation. PDG current-quark masses (MSbar, 2 GeV): m_d = 4.70 MeV, m_s = 93.5 MeV, m_u = 2.16 MeV."""
import math
md, ms, mu, mc = 4.70, 93.5, 2.16, 1273.0
print(f"sqrt(m_d/m_s) = {math.sqrt(md/ms):.3f}   measured |V_us| = 0.2243   sin(theta_C)")
print(f"sqrt(m_u/m_c) = {math.sqrt(mu/mc):.3f}   (the up-sector piece; the two enter with a relative phase)")
print("Reading: the Cabibbo angle is the misalignment between the down-type and up-type mass eigenbases,")
print("each = strong-dominated (generation-diagonal) + a K3 ZBW admixture; the admixture sets the angle.")
