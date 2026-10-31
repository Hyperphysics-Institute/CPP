"""Patch 4458 -- founder: the photon is an elongated pattern fixed at emission (like a dipole antenna's standing profile), which cannot modify
itself after creation; its electron-CP source radiates a ZBW carrier whose amplitude (DP arc-separation displacement) varies with the energy;
two photons superpose to give the difference; the DP-arc-separation amplitude is the parameter that gives the wavelength/frequency.

Part 1. No internal clock at c: for anything moving at c, the internal elapsed time (proper time) along its path is zero; nothing happens
        inside it.  (Propagation still reshapes it deterministically: diffraction, spreading, redshift.)  Time-dilation factor near c.
Part 2. A fast carrier (rate F) whose amplitude is modulated at a slow rate f (scaled here: F = 100, f = 1).
        (a) The signal itself contains only F and F +/- f: a grating sorting the signal itself would see the carrier, not f.
        (b) A response to the averaged strength (square, averaged over the carrier) contains f, but it is never negative.
Part 3. Why (b) is not enough: a signed field and a non-negative strength, two copies half a wavelength out of step.  The signed fields cancel
        (dark fringe); the strengths only add.  Light has dark fringes, zero-mean fields that change sign, and polarization.
"""
import numpy as np
for v in (0.9, 0.99, 0.999999):
    print(f"Part 1  speed {v}c: internal clock runs at {np.sqrt(1 - v**2):.2e} of the outside rate (at c: zero; the pattern is frozen)")
F, f, m = 100.0, 1.0, 0.8
t = np.linspace(0, 64, 2**18, endpoint=False)
s = (1 + m*np.cos(2*np.pi*f*t))*np.cos(2*np.pi*F*t)
fr = np.fft.rfftfreq(t.size, t[1] - t[0])
def peaks(x, label):
    S = np.abs(np.fft.rfft(x - x.mean()))
    top = fr[np.argsort(S)[-3:]]
    print(f"Part 2  {label}: strongest components at {sorted(np.round(top, 2))}")
peaks(s, "(a) the signal itself      ")
k = int(round((1/F)/(t[1] - t[0])))                     # average the square over one carrier period
sq = np.convolve(s**2, np.ones(k)/k, mode="same")
S2 = np.abs(np.fft.rfft(sq - sq.mean()))
print(f"Part 2  (b) averaged strength: strongest component at {fr[np.argmax(S2[fr < 10])]:.2f} (the modulation rate f = {f})")
print(f"Part 2  (b) averaged strength ranges {sq[k:-k].min():.3f} to {sq[k:-k].max():.3f}: never negative")
x = np.linspace(0, 4, 4000)
field1, field2 = np.cos(2*np.pi*x), np.cos(2*np.pi*x + np.pi)
str1, str2 = 0.5*(1 + np.cos(2*np.pi*x)), 0.5*(1 + np.cos(2*np.pi*x + np.pi))
print(f"Part 3  signed fields half a wavelength apart: sum max |{np.max(np.abs(field1 + field2)):.2e}| (cancel to zero)")
print(f"        non-negative strengths half a wavelength apart: sum min {np.min(str1 + str2):.3f} (never cancel)")
