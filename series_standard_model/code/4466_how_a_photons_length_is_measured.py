"""Patch 4466 -- founder: is the 1.6 ns the length of the photon, or the spread of times over which a group's photons are emitted, each received
only as a click?

What each kind of measurement gives, for a fading packet (lifetime tau) versus a short flat burst (length l = 0.05 tau, for illustration)
emitted at a random moment (exponentially spread starts):
Part 1. Lifetime measurement (histogram of click times after excitation): largest gap in the cumulative share between the burst picture and a
        pure exponential -- practically the same histogram (it differs only within the first burst-length after excitation).
Part 2. One photon interfering with itself delayed by d (unbalanced Michelson): fringe visibility |<psi(t) psi(t-d)>|.  Fading packet:
        exp(-d/(2 tau)); flat burst: max(0, 1 - d/l).  For independent emitters with random relative phases and strict adding, terms between
        different photons average out, so V(d) <= fraction of photons at least d long.
Part 3. Two photons, one delayed by d, at a beam splitter: the dip's depth |<psi1|psi2(d)>|^2.  Fading: exp(-d/tau); flat: max(0, 1 - d/l)^2.
Part 4. Hydrogen Lyman-alpha emitted by a room-temperature gas: Doppler width (FWHM) sqrt(8 kT ln2 / (m c^2)) x f, the matching coherence time
        ~1/width, length and cycles -- a lower bound on the photons' length set by the atoms' motion (hotter discharges: shorter).
"""
import numpy as np
rng = np.random.default_rng(3)
tau, l, n = 1.0, 0.05, 10**6
t = np.sort(rng.exponential(tau, n) + rng.uniform(0, l, n)); grid = np.linspace(0, 10, 2001)
gap = np.max(np.abs(np.searchsorted(t, grid)/n - (1 - np.exp(-grid/tau))))
print(f"Part 1  burst-at-random-moment vs fading packet: click-time histograms differ by at most {gap:.3f} in cumulative share")
for d in (0.5, 1.0, 2.0):
    print(f"Part 2/3  delay {d} tau:  self-interference  fading {np.exp(-d/(2*tau)):.2f}, burst {max(0, 1-d/l):.2f};  "
          f"two-photon dip  fading {np.exp(-d/tau):.2f}, burst {max(0, 1-d/l)**2:.2f}")
kT, mH, f, c = 0.025852, 938.783e6, 2.466e15, 2.99792458e8
w = np.sqrt(8*kT*np.log(2)/mH)*f
print(f"Part 4  Lyman-alpha Doppler width at 300 K: {w:.1e} Hz ({w/f:.1e} of f); coherence ~1/width = {1/w*1e12:.0f} ps, "
      f"length ~{c/w*1e3:.0f} mm, ~{f/w:.0e} cycles")
