"""Patch 4454 -- founder: a photon (or particle) may be a bounded cohort of DP arc-separation whose whole structure resonates at a
characteristic frequency set by its total energy, as an enclosed vibration has its own standing-wave frequency; the colour would be
that collective resonance, not any single ZBW rate.

Part 1. A collective mode can be far slower than its parts' own motion: a bell's note (~1e3 Hz) against its atoms' jiggling
        (~1e13 Hz); a photon's 1e15 Hz against the DPs' ZBW-scale ~1e20 Hz.  Ratios.
Part 2 (ILLUSTRATION of the condition; the product is computed, not measured here; measured separately it is the photoelectric
        and Compton result). The condition the resonance must meet: its frequency set by its energy alone, E = h f, so its internal scale (wavelength)
        must shrink as its energy grows: E x lambda = h c = 1239.84 eV nm for every photon.  A bell's pitch does not rise when struck harder.
Part 3. For matter the same holds with momentum: lambda = h / p (electron microscopes resolve finer with more kinetic energy).
"""
import numpy as np
h, c, eV, me = 6.62607015e-34, 2.99792458e8, 1.602176634e-19, 9.1093837e-31
print(f"Part 1  bell note / atomic jiggle ~ {1e3/1e13:.0e};  photon (5e14 Hz) / ZBW-scale ({me*c**2/h:.2e} Hz) ~ {5e14/(me*c**2/h):.0e}")
print("Part 2  photon: energy (eV), wavelength (nm), product (eV nm)")
for name, E in (("radio 100 MHz", h*1e8/eV), ("red H-alpha", 1.889), ("blue-green H-beta", 2.550), ("Lyman-alpha", 10.20), ("X-ray", 8.0e3), ("gamma (Fe-57)", 14.4e3)):
    lam_nm = h*c/(E*eV)*1e9
    print(f"        {name:18s}: {E:10.4g} eV, {lam_nm:12.5g} nm, product {E*lam_nm:.2f}")
for KE in (100, 1e4, 2e5):
    p = np.sqrt((KE*eV)**2 + 2*KE*eV*me*c**2)/c
    print(f"Part 3  electron at {KE:8.0f} eV: de Broglie wavelength {h/p*1e12:.3f} pm")
