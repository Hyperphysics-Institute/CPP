"""Patch 4444 -- founder on the double slit: edges as gravitating bodies; no pattern with one slit; light longitudinal;
a particle occupies a volume and part goes through each slit; the longitudinal wavelength sets the fringe spacing.

Part 1. Gravity of a slit edge vs the diffraction angle (illustrative edge: 1 g of material, light passing 1 micron away).
Part 2. Single slit: minima at sin(theta) = m lambda / a (a pattern exists); double-slit fringes lambda L / d inside that envelope.
Part 3. How far apart the two paths can be in measured matter-wave interference (what must span both).
Part 4. Atomic transition frequency vs the Compton frequency (the orbital oscillation is not at the Compton rate).
"""
import numpy as np
G, c, h = 6.674e-11, 2.998e8, 6.626e-34
M, b, lam, d, a, L = 1e-3, 1e-6, 500e-9, 100e-6, 20e-6, 1.0
grav = 4*G*M/(b*c**2)
print(f"Part 1  edge-gravity deflection {grav:.1e} rad vs fringe angle lambda/d {lam/d:.1e} rad: ratio {grav/(lam/d):.0e}")
print(f"Part 2  single slit a = {a*1e6:.0f} um, lambda = {lam*1e9:.0f} nm: minima at {', '.join(f'{np.degrees(np.arcsin(m*lam/a)):.2f} deg' for m in (1,2,3))}")
print(f"        double slit d = {d*1e6:.0f} um, screen {L:.0f} m: fringe spacing {lam*L/d*1e3:.1f} mm, within a central envelope {2*lam*L/a*1e3:.0f} mm wide")
for name, sep in (("electron biprism (Tonomura 1989)", 3e-6), ("neutron interferometer (COW 1975)", 0.03), ("atom interferometer (Kovachy et al. 2015)", 0.54)):
    print(f"Part 3  {name}: paths about {sep:.2g} m apart")
me = 9.109e-31
fC = me*c**2/h
fLya = 13.6*(1 - 1/4)*1.602e-19/h
print(f"Part 4  hydrogen Lyman-alpha {fLya:.2e} Hz vs electron Compton {fC:.2e} Hz: ratio {fLya/fC:.1e} (exactly 3 alpha^2/8 = {3*(1/137.036)**2/8:.1e}, since Lyman-alpha = (3/4) Ry and Ry = alpha^2 m c^2 / 2)")
