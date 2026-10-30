"""Patch 4452 -- what fades in a photon, and is it one photon or many?

Simulates the standard single-atom experiment: one atom is excited by a short pulse, emits one photon, and the detector records one
click at one time.  Repeat many times.  The histogram of click times after excitation is the photon's envelope (intensity):
sharp rise at excitation, exponential fall with the lifetime.  The frequency is the same throughout.
Rubidium's 780 nm line (lifetime about 26 ns), as in single-atom experiments (e.g. Darquie et al. 2005).
"""
import numpy as np
rng = np.random.default_rng(3)
tau = 26.2e-9
for N in (10, 100, 10000):
    clicks = rng.exponential(tau, N)
    h, edges = np.histogram(clicks, bins=6, range=(0, 6*tau))
    bars = " ".join(f"{x:5d}" for x in h)
    print(f"{N:6d} repeats, clicks per {tau*1e9:.0f} ns bin: {bars}")
print(f"expected share per bin (exp(-k) - exp(-k-1)): " + " ".join(f"{np.exp(-k)-np.exp(-k-1):.3f}" for k in range(6)))
print("each repeat: one click at one time; the fading envelope appears only in the histogram (as fringes appear dot by dot)")
