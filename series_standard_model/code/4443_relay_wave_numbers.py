"""Patch 4443 -- founder: what waves is the partner-changing relay (every Moment the CPs swap; the order of the whole is kept);
mass and photons differ only in organization.

What a relayed pattern must carry for the index n^2 = K^2 - K (m/E)^2 (4442); the interferometer tests (2) and gravity's phase, not (1):
  (1) a beat at the rest-energy (Compton) frequency f_C = m c^2 / h, in local time (slowed near a mass as a clock, K^-1/2);
  (2) a phase whose crests along the path are the de Broglie wavelength lambda = h / p;
  (3) the local light speed c/K as the front speed of the relay (light's case, m = 0); a massive wave's phase speed c/n exceeds it
      and its group speed c n/K^2 falls below it.
Part 1. Numbers: Compton frequency and period for the electron and neutron; Planck times per period (the Moment's size
        relative to the Planck time is not fixed here; Planck time is used as a yardstick only).
Part 2. The COW neutron (2.7 km/s): de Broglie wavelength, and its phase rate.
Part 3. The dispersion that (1)-(3) give, omega^2 = (c k / K)^2 + omega_C^2 / K, yields n^2 = K^2 - K (m/E)^2 (check).
"""
import numpy as np, sympy as sp
h, c, tP = 6.62607015e-34, 2.99792458e8, 5.391247e-44
for name, m in (("electron", 9.1093837e-31), ("neutron", 1.67492750e-27)):
    fC = m*c**2/h
    print(f"Part 1  {name}: Compton frequency {fC:.3e} Hz, period {1/fC:.3e} s = {1/fC/tP:.2e} Planck times")
mn, v = 1.67492750e-27, 2.7e3
lam = h/(mn*v)
print(f"Part 2  COW neutron at {v:.0f} m/s: de Broglie wavelength {lam*1e10:.2f} angstrom (COW: 1.445 A at about 2.74 km/s)")
K, k, wC, w = sp.symbols('K k omega_C omega', positive=True)
disp = sp.Eq(w**2, (k/K)**2 + wC**2/K)                     # c = hbar = 1
ksol = sp.solve(disp, k)[0]
n2 = sp.simplify((ksol/w)**2)                             # index^2 = (k/omega)^2, vacuum K = 1 gives k/omega = v
print("Part 3  index^2 from the dispersion:", sp.expand(n2), "  (with omega = E, omega_C = m: K^2 - K (m/E)^2)")
