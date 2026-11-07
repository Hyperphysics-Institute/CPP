"""Patch 4463 -- founder: (1) the energy of an orbital is the totality of the orbital, not its radius; each swing may start and end anywhere;
only the total must equal the interval; colours come out in order of the energy difference.  (2) the decay statistics reflect the stimulated
system, not the shape of the swing sequence; no 1:1 correlation.  (3) the photon is an organized volume of the DP sea, its active portion about a
metre across, held together by mutual reinforcement; any growth in its radius with distance would be from microlensing by mass along the path;
its coherence from the light-speed mutual interaction of the DP arc-separations.

Part 1. His statistical-start reading: each photon a packet of its own length l, starting at an exponentially random time (mean tau) after
        excitation.  Two photons from separate atoms, arriving with independent random starts, overlap |<psi1|psi2>|^2 = (max(0, l-|s1-s2|)/l)^2
        for flat packets (slow detector).  Mean overlap against l/tau, and how far the detection-time histogram (start + uniform over
        the packet) departs from the measured exponential (largest difference in the cumulative share, a Kolmogorov distance; for packets up to tau
        long it is mainly a delayed, rounded start).  The overlap is integrated over the packet (slow detector); it stands for either detector.
Part 2. Spreading in the lab: Gaussian beams of 1 mm waist radius (2 mm across), red 633 nm and violet 405 nm, after 10 m; divergence lambda/(pi w0) depends on colour.
        Gravitational lensing deflects all colours alike.
Part 3. Coherence length c x lifetime: Lyman-alpha (1.60 ns), Ba+ 493 nm (6P1/2, about 7.9 ns), sodium D (16.2 ns).
"""
import numpy as np
rng = np.random.default_rng(2)
n = 10**6
s1, s2 = rng.exponential(1, n), rng.exponential(1, n)
for l in (0.1, 0.3, 1, 3, 10):
    ov = np.mean((np.maximum(0, l - np.abs(s1 - s2))/l)**2)
    t = np.sort(s1 + rng.uniform(0, l, n)); grid = np.linspace(0, 15, 1501)
    cdf = np.searchsorted(t, grid)/n; dev = np.max(np.abs(cdf - (1 - np.exp(-grid))))
    print(f"Part 1  packet length {l:>4} tau with random starts: mean two-photon overlap {ov:.3f}; histogram departs from exponential by {dev:.3f}")
for lam in (633e-9, 405e-9):
    w0, z = 1e-3, 10.0
    zR = np.pi*w0**2/lam
    print(f"Part 2  {lam*1e9:.0f} nm, 1 mm waist: Rayleigh range {zR:.2f} m, radius at 10 m {w0*np.sqrt(1+(z/zR)**2)*1e3:.2f} mm")
c = 2.99792458e8
for name, tau in (("Lyman-alpha", 1.596e-9), ("Ba+ 493 nm", 7.9e-9), ("sodium D", 16.2e-9)):
    print(f"Part 3  {name}: c x lifetime = {c*tau:.2f} m")
