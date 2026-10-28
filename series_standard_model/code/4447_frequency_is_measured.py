"""Patch 4447 -- founder: the colour is the packet's total energy; frequency is an interpretation (E/h, a count of action
increments), not the carrier's rate; the ZBW oscillations are a modulated carrier.

What is measured independently of energy:
Part 1. Gratings sort light by crest spacing alone: sin(theta) = lambda / d.  Red and blue go to different angles.
Part 2. If the carrier inside every photon ran at the ZBW / Compton rate, every photon would diffract at the Compton wavelength
        (2.43 pm), whatever its colour: visible light would diffract like gamma rays.
Part 3 (illustrative values from the measured slope). Millikan's photoelectric test links two separately measured things: the stopping voltage (energy, measured electrically)
        and the frequency (from the grating).  The slope is h / e.  E = h f is a finding, not a definition.
Part 4. Optical frequency combs count an optical field's cycles against the caesium clock: for hydrogen 1S-2S (Parthey et al. 2011)
        the comb counts the drive laser's cycles (486 nm, doubled to 243 nm; the two-photon transition is at twice the 243 nm
        light's frequency), about 2,466,061,413,187,035 Hz.  This shows an optical oscillation can be counted and the atom answers
        that exact frequency; it is not an independent check of E/h (the level energy is inferred from it).
"""
import numpy as np
h, c, e, me = 6.626e-34, 2.998e8, 1.602e-19, 9.109e-31
d = 1e-3/600                                   # 600 lines per mm
for name, lam in (("red 656 nm", 656e-9), ("blue 486 nm", 486e-9)):
    print(f"Part 1  {name}: first-order angle {np.degrees(np.arcsin(lam/d)):.1f} deg; photon energy {h*c/lam/e:.2f} eV")
lamC = h/(me*c)
print(f"Part 2  Compton wavelength {lamC*1e12:.2f} pm: first-order angle on the same grating {np.degrees(np.arcsin(lamC/d))*3600:.3f} arcsec, for every colour")
for f in (5.5e14, 7.0e14, 1.0e15):
    print(f"Part 3  frequency {f:.1e} Hz (grating) -> maximum photoelectron energy minus work function = h f = {h*f/e:.2f} eV (slope h/e = {h/e:.3e} V s)")
f1s2s = 2466061413187035
print(f"Part 4  H 1S-2S transition frequency from counted drive-laser cycles: {f1s2s:,} Hz (drive laser at {f1s2s/2:,.0f} Hz, 243 nm)")
