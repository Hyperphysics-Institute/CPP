"""Patch 4467 -- founder asks for the line-width criterion to be explained.

Part 1. A wave train of N crests (flat envelope) has a spread of frequencies (half-power width) of about 0.89/N of its frequency: computed for
        N = 1, 10, 100, 10000.  So a spectrometer's measured width, as a share of the frequency, caps 1/N from above: crests >= ~0.9/(width/f).
Part 2. Motion only widens a line (each atom's light is shifted up or down by its speed toward or away), so a gas's measured width is an upper
        bound on the width of most photons, and the crest count from it is a lower bound.  Lyman-alpha Doppler widths (computed, not
        measured): 300 K (hypothetical; room-temperature hydrogen does not emit Lyman-alpha), 3000 K, and ~2 eV fast atoms from dissociation.
        Flat envelope; other shapes change the 0.9/N factor by about two.
Part 3. The same number from the fringe test: an N-crest train interferes with its own copy delayed by up to N crests (visibility 1 - d/N for
        a flat train), so the path difference at which fringes fade is about N wavelengths.  (Width and fringes are one measurement seen two
        ways, Wiener-Khinchin.)
"""
import numpy as np
for N in (1, 10, 100, 10000):
    n = 2**22; span = 40*N
    t = np.linspace(-span/2, span/2, n, endpoint=False)
    y = np.where(np.abs(t) < N/2, np.cos(2*np.pi*t), 0.0)
    S = np.abs(np.fft.rfft(y))**2; f = np.fft.rfftfreq(n, t[1]-t[0])
    pk = np.argmax(S); half = f[S > S[pk]/2]; band = half[(half > 0.5*f[pk])]
    band = band[(band < 1.5*f[pk])] if N > 1 else half
    extra = ""
    if N == 1:
        lo, hi = half.min()/f[pk], half.max()/f[pk]
        extra = f"; relative to the peak {hi-lo:.2f} ({lo:.2f}-{hi:.2f} x peak; with the peak at Lyman-alpha, {121.6/hi:.0f}-{121.6/lo:.0f} nm)"
    print(f"Part 1  {N:>5} crests: half-power width = {band.max()-band.min():.2e} of the frequency (0.89/N = {0.886/N:.2e}){extra}")
kT_mc2 = 0.025852/938.783e6
lam = 121.567e-9
for T in (300, 3000):
    w = np.sqrt(8*kT_mc2*(T/300)*np.log(2))
    N = 0.886/w
    print(f"Part 2  Lyman-alpha, gas at {T} K: Doppler width {w:.1e} of f -> at least ~{N:.0e} crests, ~{N*lam*1e3:.0f} mm")
v = np.sqrt(2*2.0/938.783e6)          # a 2 eV hydrogen atom from dissociation, v/c
w = 2*v                               # full spread of shifts, +/- v/c
print(f"Part 2  Lyman-alpha, fast atoms of ~2 eV (dissociation): width ~{w:.1e} of f -> at least ~{0.886/w:.0e} crests, ~{0.886/w*lam*1e3:.1f} mm")
for d in (0.25, 0.5, 1.0):
    print(f"Part 3  flat N-crest train delayed by {d} N: self-interference visibility {max(0, 1-d):.2f}")
