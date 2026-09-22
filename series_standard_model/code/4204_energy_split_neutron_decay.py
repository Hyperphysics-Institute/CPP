#!/usr/bin/env python3
"""4204 -- who carries the released energy in free-neutron decay (allowed spectrum, Fermi function ~1).
m_n - m_p = 1.2933 MeV = m_e + Q,  Q = 0.7823 MeV.  Electron total energy E in [m_e, E0], E0 = 1.2933.
dN/dE  ~  p E (E0 - E)^2."""
import numpy as np
me, E0 = 0.51100, 1.29333
E = np.linspace(me, E0, 20001); p = np.sqrt(E**2 - me**2); w = p * E * (E0 - E)**2
w /= np.trapezoid(w, E)
Te = E - me; Tnu = E0 - E
print(f"energy released (m_n - m_p)      = {E0:.4f} MeV, of which electron rest mass {me:.3f}, shared KE Q = {E0-me:.4f}")
print(f"mean electron KE                 = {np.trapezoid(w*Te,E):.3f} MeV   ({np.trapezoid(w*Te,E)/(E0-me):.0%} of Q)")
print(f"mean antineutrino energy         = {np.trapezoid(w*Tnu,E):.3f} MeV   ({np.trapezoid(w*Tnu,E)/(E0-me):.0%} of Q)")
print(f"fraction of decays where nubar takes MORE than half of Q = {np.trapezoid(w*(Tnu>Te),E):.0%}")
print(f"nubar share ranges continuously from 0% to 100% of Q; its rest mass is < 1e-6 of what it carries.")
