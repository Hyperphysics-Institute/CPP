"""Patch 4465 -- founder asks: what experiment shows a single emission swing gives at most millionths of an eV?

Part 1. The 4464 figure is a calculation, not a measurement: Larmor's rule for one rise and fall (v = v_max sin^2(pi t/T), T = 3.40e-16 s for a
        Lyman-alpha peak) scales as v_max^2: shown for three speeds.  Part 1b: the gamma v (and kinetic energy) that would be needed to
        radiate 10.2 eV in one rise and fall, against the ~2e6 m/s a CP with 10-14 eV of kinetic energy can have.
Part 2. Larmor's rule tested on free charges: (a) a single electron's cyclotron radiation (Project 8, Asner et al. PRL 114, 162501, 2015:
        30.4 keV electrons in ~0.95 T, ~26 GHz, power from the chirp); (b) synchrotron energy loss per turn in an electron ring, U0 = 88.5 keV E[GeV]^4 / rho[m] (LEP at
        104.5 GeV, bending radius 3096 m).
Part 3. The measured emission time, independent of Larmor: Lyman-alpha's lifetime 1.596 ns = 3.9e6 cycles, so the average energy leaving per
        cycle is 10.2 eV / 3.9e6, if each photon is emitted over the lifetime (the 4462-4463 inference).
"""
import numpy as np
e, eps0, c, me, eV = 1.602176634e-19, 8.8541878128e-12, 2.99792458e8, 9.1093837e-31, 1.602176634e-19
K = e**2/(6*np.pi*eps0*c**3)
T = 3.40e-16
for label, v in (("10.2 eV kinetic", np.sqrt(2*10.2*eV/me)), ("hydrogen 1s orbital speed alpha c", c/137.036), ("ten times that", 10*c/137.036)):
    E = K*(v*np.pi/T)**2*(T/2)
    print(f"Part 1  v_max = {v:.2e} m/s ({label}): one rise and fall radiates {E/eV:.1e} eV; distance moved {v*T/2*1e10:.1f} Angstrom")
KE, B = 30.4e3*eV, 0.95
gam = 1 + KE/(me*c**2); beta = np.sqrt(1 - 1/gam**2)
fc = e*B/(2*np.pi*gam*me)
P = e**4*B**2*beta**2*gam**2/(6*np.pi*eps0*me**2*c)
print(f"Part 2a single 30.4 keV electron in 0.95 T, 90 deg pitch: cyclotron {fc/1e9:.1f} GHz, free-space Larmor power {P*1e15:.2f} fW (paper: 1.74 fW predicted; 1.61(4) fW inferred from the measured chirp, in a waveguide)")
U0 = 88.5*104.5**4/3096
print(f"Part 2b LEP at 104.5 GeV: energy loss per turn {U0/1e6:.2f} GeV")
f, tau = 2.466e15, 1.596e-9
print(f"Part 3  Lyman-alpha: {f*tau:.2e} cycles in a lifetime; average {10.2/(f*tau):.1e} eV per cycle")
# Larmor's slow-speed form equals Lienard's straight-line form P = K (d(gamma v)/dt)^2 when v is replaced by gamma v (proper velocity)
u_need = np.sqrt(10.2*eV/(K*(np.pi/T)**2*(T/2)))
gb = u_need/c; g = np.sqrt(1 + gb**2)
print(f"Part 1b to radiate 10.2 eV in one rise and fall of {T:.2e} s needs gamma v = {u_need:.1e} m/s, gamma beta = {gb:.1f}, "
      f"kinetic energy {(g-1)*0.51099895:.1f} MeV; a CP with 10-14 eV is capped near 2e6 m/s")
