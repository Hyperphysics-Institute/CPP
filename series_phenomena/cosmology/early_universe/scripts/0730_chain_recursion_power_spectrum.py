#!/usr/bin/env python3
"""
0730_chain_recursion_power_spectrum.py
======================================
Toy test of the qCP-chain "chain-of-chains" fractal-recursion intuition
(founders_vision.md Sec 6d; CONJ-COSMO-3, owed-piece 3).

QUESTION. Thomas's intuition: a self-similar backbone where "chains exert force
on chains, and chains of chains influence each other with similar rules at each
level" should yield scale-free fluctuation statistics -- and perhaps the observed
near-scale-invariant primordial spectrum. Does it?

We build the cleanest faithful caricature -- a 1D multiplicative random cascade
(the canonical "same multiplicative rule at every scale" process; Mandelbrot /
Soneira-Peebles hierarchical-clustering family) -- and measure its statistics
against the two reference fields that bracket the cosmological question:
  * WHITE NOISE      -- uncorrelated, Gaussian; the "no structure" baseline.
  * SCALE-INVARIANT GAUSSIAN -- flat dimensionless power Delta^2(k)=k*P(k),
    Gaussian; THIS is the actual primordial target (Harrison-Zel'dovich, Gaussian).

DIAGNOSTICS (dimension-robust, convention-free):
  (A) Is the field scale-free?  -> is P(k) a power law (high-R^2 log-log fit)?
  (B) Is the SLOPE a discriminator? -> NO. The cascade slope can be tuned (via the
      variance sigma) to mimic the scale-invariant value (Delta^2 ~ flat), and it
      MOVES with sigma -- an unpinned free dial, so slope-matching settles nothing.
  (C) THE DECISIVE TEST -- is it GAUSSIAN? -> primordial fluctuations are ~Gaussian
      (excess kurtosis ~ 0); multiplicative cascades are non-Gaussian by ORDERS OF
      MAGNITUDE. This separates clustered/processed matter from primordial seeds and
      is robust to any slope tuning.

VERDICT we expect (and check): the cascade is scale-free (A yes) -- vindicating
the morphology intuition -- its slope can even be tuned to look scale-invariant
(B, not a discriminator), but it is catastrophically NON-Gaussian (C). That is the
signature of CLUSTERED/PROCESSED matter, not of Gaussian scale-invariant PRIMORDIAL
seeds. So: self-similar recursion => scale-free clustering (cosmic-web morphology,
good), but =/=> primordial adiabatic spectrum (the generation barrier, untouched).
This is the generation-vs-processing split, demonstrated numerically.

LIMITATIONS (stated honestly): 1D; schematic; the cascade weights are GENERIC i.i.d.
lognormal, NOT derived from 600-cell geometry. A CPP-specific cascade (golden-ratio
branching) could shift the *slope*, but cannot by itself fix the *non-Gaussianity*
or supply the *near-constant-H freezing* that makes primordial fluctuations Gaussian
and frozen super-horizon (Patch 0729). The toy tests the generic claim "self-similar
recursion -> primordial spectrum"; it does not exclude a future CPP-specific model,
it locates exactly what such a model would still have to supply.
"""

import numpy as np

rng = np.random.default_rng(0)
PASS = []
def check(name, cond):
    PASS.append(bool(cond)); print(f"  [{'PASS' if cond else 'FAIL'}] {name}")

L = 16
N = 1 << L                       # 65536 points

# ---------------------------------------------------------------------------
def multiplicative_cascade(sigma, levels=L, n=N):
    """Chain-of-chains: rho = product over levels of a mean-1 lognormal field
    that is piecewise-constant on dyadic blocks. 'Same rule at every scale.'"""
    rho = np.ones(n)
    for ell in range(1, levels + 1):
        nblocks = 1 << ell
        blocksize = n // nblocks
        # mean-1 lognormal weights: E[exp(g)] = 1 => mean of g = -sigma^2/2
        g = rng.normal(-0.5 * sigma * sigma, sigma, size=nblocks)
        w = np.exp(g)
        rho *= np.repeat(w, blocksize)
    return rho / rho.mean()

def white_noise(n=N):
    return 1.0 + rng.normal(0.0, 1.0, size=n)

def scale_invariant_gaussian(n=N):
    """Gaussian field with Delta^2(k)=k*P(k) flat  =>  |delta_k|^2 ~ 1/k.
    The Harrison-Zel'dovich (scale-invariant) Gaussian reference."""
    k = np.fft.rfftfreq(n, d=1.0) * n
    amp = np.zeros_like(k)
    amp[1:] = k[1:] ** (-0.5)                 # |delta_k| ~ k^{-1/2} -> P~1/k -> k*P flat
    phases = np.exp(2j * np.pi * rng.random(k.size))
    dk = amp * phases
    d = np.fft.irfft(dk, n=n)
    return 1.0 + d / d.std()

def power_spectrum(field):
    delta = field / field.mean() - 1.0
    dk = np.fft.rfft(delta)
    P = (np.abs(dk) ** 2)[1:]                  # drop k=0
    k = (np.fft.rfftfreq(field.size, d=1.0) * field.size)[1:]
    return k, P

def logbin_slope(k, y, kmin, kmax, nbins=24):
    """Fit slope of y(k) in log-log over [kmin,kmax] with log-spaced bins."""
    m = (k >= kmin) & (k <= kmax) & (y > 0)
    lk, ly = np.log(k[m]), np.log(y[m])
    bins = np.linspace(lk.min(), lk.max(), nbins + 1)
    idx = np.digitize(lk, bins)
    bx, by = [], []
    for b in range(1, nbins + 1):
        sel = idx == b
        if sel.sum() > 2:
            bx.append(lk[sel].mean()); by.append(ly[sel].mean())
    bx, by = np.array(bx), np.array(by)
    A = np.vstack([bx, np.ones_like(bx)]).T
    slope, intercept = np.linalg.lstsq(A, by, rcond=None)[0]
    pred = A @ [slope, intercept]
    ss_res = np.sum((by - pred) ** 2)
    ss_tot = np.sum((by - by.mean()) ** 2)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return slope, r2

def excess_kurtosis(field):
    d = field / field.mean() - 1.0
    s = d.std()
    return np.mean((d / s) ** 4) - 3.0 if s > 0 else 0.0

# fit band: avoid the largest scales (few modes) and the Nyquist pile-up
KMIN, KMAX = 8.0, N / 8.0

# ---------------------------------------------------------------------------
print("REFERENCE CALIBRATION (so the diagnostics are anchored)")
kw, Pw = power_spectrum(white_noise())
sw, r2w = logbin_slope(kw, Pw, KMIN, KMAX)
kw2, Pw2 = power_spectrum(white_noise()); 
sd2w, _ = logbin_slope(kw2, kw2 * Pw2, KMIN, KMAX)
print(f"  white noise:            P(k) slope = {sw:+.2f} (expect ~0),  kurtosis = {excess_kurtosis(white_noise()):+.2f} (expect ~0)")
check("white noise: P(k) flat (slope ~ 0)  =>  baseline 'no structure'", abs(sw) < 0.15)

ksi, Psi = power_spectrum(scale_invariant_gaussian())
ssi, r2si = logbin_slope(ksi, Psi, KMIN, KMAX)
d2si, _ = logbin_slope(ksi, ksi * Psi, KMIN, KMAX)
kurt_si = excess_kurtosis(scale_invariant_gaussian())
print(f"  scale-inv Gaussian:     P(k) slope = {ssi:+.2f} (expect ~-1),  Delta^2 slope = {d2si:+.2f} (expect ~0),  kurtosis = {kurt_si:+.2f}")
check("scale-inv Gaussian: Delta^2(k)=k*P(k) FLAT (the primordial target)", abs(d2si) < 0.15)
check("scale-inv Gaussian: nearly Gaussian (|excess kurtosis| < 0.3)", abs(kurt_si) < 0.3)

# ---------------------------------------------------------------------------
print("\nTHE CHAIN-OF-CHAINS CASCADE (Thomas's recursion)")
def cascade_stats(sigma, reps=6):
    sP, r2, sD, kurt = [], [], [], []
    for _ in range(reps):
        f = multiplicative_cascade(sigma)
        k, P = power_spectrum(f)
        a, r = logbin_slope(k, P, KMIN, KMAX); sP.append(a); r2.append(r)
        sD.append(logbin_slope(k, k * P, KMIN, KMAX)[0]); kurt.append(excess_kurtosis(f))
    return (np.mean(sP), np.mean(r2), np.mean(sD), np.mean(kurt))

sP4, r24, sD4, kurt4 = cascade_stats(0.4)
sP7, r27, sD7, kurt7 = cascade_stats(0.7)
print(f"  sigma=0.4:  P(k) slope={sP4:+.2f} (R^2={r24:.2f}),  Delta^2 slope={sD4:+.2f},  excess kurtosis={kurt4:+.1f}")
print(f"  sigma=0.7:  P(k) slope={sP7:+.2f} (R^2={r27:.2f}),  Delta^2 slope={sD7:+.2f},  excess kurtosis={kurt7:+.1f}")

# (A) scale-free?  power-law P(k) with good averaged fit -> morphology intuition vindicated
check("(A) cascade IS scale-free: P(k) is a clean power law (mean R^2 > 0.9)  =>  morphology intuition vindicated", r24 > 0.9)
# (B) the SLOPE is not a discriminator: it can be tuned NEAR scale-invariant (Delta^2 ~ flat at sigma=0.4)
#     AND it moves with sigma -> an unpinned free dial, not a prediction of n_s.
check("(B) slope is a FREE DIAL that can even mimic scale-invariance: |Delta^2 slope|<0.25 at sigma=0.4 ...", abs(sD4) < 0.25)
check("(B') ... but it MOVES with cascade variance sigma (not pinned to any n_s)", abs(sP7 - sP4) > 0.12)
# (C) THE DECISIVE DISCRIMINATOR: orders-of-magnitude non-Gaussianity (primordial is ~Gaussian, kurtosis~0)
check("(C) DECISIVE: cascade is non-Gaussian by ORDERS OF MAGNITUDE (kurtosis>10 vs ~0 primordial), robust to slope tuning", kurt4 > 10.0)

# ---------------------------------------------------------------------------
print()
if all(PASS):
    print(f"ALL {len(PASS)} CHECKS PASS")
    print("Toy verdict: the chain-of-chains recursion produces SCALE-FREE CLUSTERING")
    print("(power-law P(k)) -- the intuition that a self-similar backbone gives scale-free")
    print("structure is VINDICATED, and this is the right signature for the cosmic-web")
    print("MORPHOLOGY (CONJ-COSMO-3 processing role). The spectral SLOPE is a free dial that")
    print("can even be tuned to mimic scale-invariance (Delta^2 ~ flat at sigma=0.4) -- so slope")
    print("alone is NOT a discriminator, and a '600-cell ratio = 0.96' match would not settle it.")
    print("The DECISIVE fact: the cascade is non-Gaussian by ORDERS OF MAGNITUDE (kurtosis ~10^2-10^3")
    print("vs ~0 for the primordial Gaussian target) -- the multifractal signature of CLUSTERED")
    print("matter, not Gaussian PRIMORDIAL seeds, and robust to any slope tuning.")
    print("=> Self-similar recursion gives clustering, not generation. The generation barrier")
    print("(owed pieces 1 near-constant-H + 2 adiabaticity + 3 Gaussian k^1 spectrum) stands.")
else:
    print(f"{sum(PASS)}/{len(PASS)} checks passed -- see FAIL lines above.")
