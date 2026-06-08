#!/usr/bin/env python3
"""
0809_step2b_symmetry.py -- DM-2 Step 2(b): is the bulk ZBW statistically symmetric?

The net-broadcast lemma condition (b). The Step-1 cubic source averages, over a
closed/periodic patch, to a pure THIRD MOMENT of the ZBW field:
    F = 2 k^2 d^2 d''  ->  <F>_bulk = -4 k^2 <d d'^2>.
d*d'^2 is ODD under the field-amplitude flip d -> -d, so <F>_bulk vanishes iff the
bulk ZBW distribution is symmetric (zero skew / vanishing 3rd moment), and is
nonzero for a SKEWED (non-Gaussian, detailed-balance-violating) bulk.

Verdict (detail in dm2_step2b_symmetry.md): CONDITIONAL. The substrate is a NESS
(chirality lane: detailed balance violated at O(delta^3), Patch 0689), so symmetry
is NOT automatic; whether the O(delta^3) current yields a net bulk residual is the
(H-NESS) lift -- the SAME gate blocking the chirality mu^2-sign.
"""
import numpy as np

rng = np.random.default_rng(1)
N = 2**14; L = 2*np.pi
xx = np.linspace(0, L, N, endpoint=False)
kf = np.fft.rfftfreq(N, d=L/N)*2*np.pi

def make_field(skew):
    amp = np.exp(-(kf-8)**2/8.0)
    ph = rng.uniform(0, 2*np.pi, len(kf))
    g = np.fft.irfft(amp*np.exp(1j*ph), N); g /= g.std()
    return g + skew*(g**2 - 1.0)               # skew=0 -> symmetric (d->-d); >0 -> skewed

def third(d):
    dp = np.gradient(d, xx)
    return np.mean(d*dp*dp)

print("="*64)
print("ENSEMBLE <d d'^2> (the bulk residual source) vs skew, averaged over M realizations")
print(f"{'skew':>6s}{'mean <d d^prime^2>':>22s}{'std/sqrt(M)':>16s}{'mean skewness':>16s}")
M = 400
for sk in [0.0, 0.1, 0.3, 0.8]:
    vals, skews = [], []
    for _ in range(M):
        d = make_field(sk); vals.append(third(d))
        skews.append(((d-d.mean())**3).mean()/d.std()**3)
    vals = np.array(vals)
    print(f"{sk:6.1f}{vals.mean():22.4e}{vals.std()/np.sqrt(M):16.2e}{np.mean(skews):16.3f}")
print("  => symmetric bulk (skew=0): ensemble <d d'^2> -> 0 (consistent w/ Step-1 parity).")
print("     skewed bulk: nonzero, growing with the 3rd moment. Condition (b) is real.")

print("="*64)
print("LOAD-BEARING: if the bulk O(delta^3) skew is unsuppressed at the Planck scale,")
print("<F>_bulk ~ Planck density (CC catastrophe). Clean horizon-only Lambda REQUIRES")
print("the bulk skew to vanish/suppress. The substrate IS a NESS (chirality 0689:")
print("detailed balance violated at O(delta^3)) -> symmetry is NOT automatic ->")
print("the question is the (H-NESS) lift = the same gate as the chirality mu^2-sign.")
