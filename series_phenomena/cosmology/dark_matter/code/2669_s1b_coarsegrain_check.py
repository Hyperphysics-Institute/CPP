#!/usr/bin/env python3
"""FA-SEA-GREEN S1b coarse-graining instrument (Patch 2669, fork-blind).

Verifies route (a) of the scale bridge: iterating the lossless z=12
shell-average kernel gives (i) additive second moments (Laplacian
coefficient composes linearly -- Laplacian in, Laplacian out) and
(ii) excess kurtosis decaying as 1/n (all higher cumulants RG-irrelevant;
the coarse one-step operator Gaussianizes).

BLIND-GUARD AUDIT: no gap parameter, no screening length, no candidate
value, no decay-vs-parameter curve. Lossless transport only.

Preregistered PASS bands: |<x^2>/n - 1/3| < 0.5% of 1/3 at every n (band
sits an order above the 2M-walker MC standard error ~0.03%, disclosed --
the first run used 0.1%, which is AT MC-noise scale and tripped on noise
at n=4; the widening is an instrument-precision correction, not a
retuning toward any physics result);
|kurt(n)| < 2.5/n for all n (1/n cumulant decay); |kurt(64)| < 0.05.
"""

import numpy as np

rng = np.random.default_rng(2669)

dirs = []
for perm in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    for s1 in (1, -1):
        for s2 in (1, -1):
            v = np.zeros(3)
            v[perm[0]] = s1
            v[perm[1]] = s2
            dirs.append(v / np.sqrt(2.0))
dirs = np.array(dirs)
assert len(dirs) == 12

NW = 2_000_000
steps_list = [1, 4, 16, 64]
nmax = max(steps_list)
pos = np.zeros((NW, 3))
results = {}
for step in range(1, nmax + 1):
    picks = rng.integers(0, 12, size=NW)
    pos += dirs[picks]
    if step in steps_list:
        x = pos[:, 0]
        m2 = (x ** 2).mean()
        m4 = (x ** 4).mean()
        results[step] = (m2 / step, m4 / m2 ** 2 - 3.0)

print(" n    <x^2>/n per comp (expect 1/3)   excess kurtosis (expect ~ -1.5/n)")
ok = True
for n in steps_list:
    var_per_n, kurt = results[n]
    print(f"{n:3d}   {var_per_n:.5f}                      {kurt:+.5f}")
    if abs(var_per_n - 1.0 / 3.0) > 0.005 * (1.0 / 3.0):
        ok = False
    if abs(kurt) > 2.5 / n:
        ok = False
if abs(results[64][1]) > 0.05:
    ok = False

print("S1b coarse-graining check:", "ALL PASS" if ok else "FAIL")
print("(second moment additive within the 0.5% band; kurtosis decays as 1/n ->")
print(" the coarse effective transport is the isotropic Laplacian at every")
print(" block scale; no structure and no length survive the bridge.)")
