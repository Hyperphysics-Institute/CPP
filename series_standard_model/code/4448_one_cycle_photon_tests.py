"""Patch 4448 -- founder: a photon may be a single event lasting one wavelength; higher-energy photons shorter and stronger.

Two measurable consequences of a one-cycle photon:
Part 1. Spectral width.  A pulse N cycles long has a fractional spread of frequencies of about 1/N (here 1/(pi N), Gaussian-like).
        One cycle -> a spread comparable to the colour itself; measured lines are sharp.
Part 2. Coherence length.  Split a photon in an interferometer: fringes survive only while the arms differ by less than the
        packet length.  One cycle -> fringes lost beyond about one wavelength.
Part 3. Beat notes between two light sources last over many beat periods only if each source's oscillation is steady over many cycles.
"""
import numpy as np
c = 2.998e8
lines = (("H Lyman-alpha (121.6 nm)", 121.6e-9, 4.0e-8),)
for name, lam, measured in lines:
    print(f"Part 1  {name}: one-cycle spread ~ {1/np.pi:.2f} (1/pi) to {0.44:.2f} (Gaussian FWHM) of the frequency; natural width measured ~ {measured:.0e}")
lamHa = 656e-9; fHa = c/lamHa
for name, frac in (("1/pi", 1/np.pi), ("Gaussian FWHM 0.44", 0.44)):
    lo, hi = c/(fHa*(1 + frac/2)), c/(fHa*(1 - frac/2))
    print(f"Part 1  H-alpha 656 nm as a one-cycle pulse ({name}): spread {lo*1e9:.0f} to {hi*1e9:.0f} nm")
for name, lam, tau in (("H Lyman-alpha natural packet", 121.6e-9, 1.6e-9), ("single atom in a cavity (order 1 us packets, illustrative)", 780e-9, 1e-6)):
    L = c*tau
    print(f"Part 2  {name}: packet {L:.2f} m = {L/lam:.1e} wavelengths; one-cycle photon would lose fringes beyond {lam*1e9:.0f} nm of arm difference")
df = 1e6
print(f"Part 3  two lasers {df:.0e} Hz apart beat with period {1/df*1e6:.1f} us; a steady beat over 1 ms needs each oscillation steady over"
      f" ~{1e-3*c/500e-9:.1e} cycles at 500 nm")
