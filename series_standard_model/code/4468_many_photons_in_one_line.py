"""Patch 4468 -- founder: the line width is the statistical spread of energies of many photons, not one photon of 10,000 crests.

The measured line is the sum of the photons' own spectra.  Model (independent emitters, random relative phases, so the line is the sum of the photons' own power spectra): each photon is a flat train of N crests whose centre frequency is drawn from a
spread of fractional width s (Gaussian, FWHM s).  The line's half-power width is printed for:
  (a) photons of 1 crest with centre spread s = 1e-4  -> the line is still as wide as one photon's own spread (~0.9 in this sinc^2 model,
      which is crude at one crest; 4467 gives 0.7-1.07): of order one -- a narrow line is impossible;
  (b) photons of 1e5 crests, s = 1e-4               -> width ~ s (the distribution dominates);
  (c) photons of 1e5 crests, s = 0 (all alike)       -> width ~ 0.9e-5 (each photon's own spread).
So a line of width w can be made of many photons of different energies (b) only if most photons are themselves narrower than w, i.e. has at least
~0.9/w crests; short photons (a) cannot make a narrow line however their energies are distributed.
"""
import numpy as np
def run(label, N, s, half_span):
    x = np.linspace(1 - half_span, 1 + half_span, 400001)
    rng = np.random.default_rng(4)
    f0s = 1 + rng.normal(0, s/2.3548, 4000) if s > 0 else np.ones(1)
    S = sum(np.sinc(N*(x - f0)/f0)**2 for f0 in f0s)
    h = x[S >= S.max()/2]
    print(f"{label}: line half-power width {h.max()-h.min():.1e} of the frequency")
run("(a) 1 crest, energies spread 1e-4", 1, 1e-4, 1.0)
run("(b) 1e5 crests, energies spread 1e-4", 1e5, 1e-4, 1e-3)
run("(c) 1e5 crests, all alike", 1e5, 0.0, 1e-4)
