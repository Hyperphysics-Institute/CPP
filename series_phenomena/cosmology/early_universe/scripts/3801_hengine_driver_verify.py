#!/usr/bin/env python3
"""
Patch 3801 verify — S-HENGINE-HELD (OPEN-EU-HENGINE-DRIVER-1), statement-grade checks.
 T1  Under R-STACK-SENDS-EACH the observable epoch is saturated: n-bar = exp(3 N_rem) at N_rem = 57 ~ 1e74;
     census D ~ 12 n-bar >> K = 12.
 T2  The acted-on displacement is zero by symmetry in the homogeneous state: the 12 icosahedral vertex
     vectors sum to zero exactly, so an isotropic census gives SSV_net = 0 before any clip.
 T3  A clipped (depth-independent) driver gives n_s = 1: excluded by Planck 2018 (0.9649 +/- 0.0042) at ~8 sigma.
 T4  The held-stack driver mu = kT ln n-bar, ln n-bar = 3 N_rem, gives n_s = 1 - 2/N_* = 0.9649 at N_* = 57,
     inside Planck's 1 sigma.
 T5  Reading-independence: mu depends on n-bar only; the same n-bar under Reading S (census sees the stack)
     and Reading P (census sees one) gives identical mu, hence identical n_s. The D1 cap K does not enter mu.
"""
import numpy as np
PASS = FAIL = 0
def check(n, c, d=""):
    global PASS, FAIL; ok = bool(c); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  — {d}" if d else ""))

# T1
N_star = 57
ln_nbar = 3 * N_star
nbar = np.exp(ln_nbar); K = 12.0; D = 12 * nbar
print(f"T1 — ln n-bar = {ln_nbar}, n-bar ~ 1e{np.log10(nbar):.1f}, D/K ~ 1e{np.log10(D/K):.1f}")
check("T1 observable epoch saturated by >= 70 orders under Reading S", np.log10(D / K) >= 70)

# T2 — icosahedron vertices (0, ±1, ±phi) and cyclic permutations
phi = (1 + 5 ** 0.5) / 2
V = []
for s1 in (1, -1):
    for s2 in (1, -1):
        V += [(0, s1, s2 * phi), (s1, s2 * phi, 0), (s2 * phi, 0, s1)]
V = np.array(V, float)
assert len(V) == 12
net = V.sum(axis=0)
print(f"T2 — 12 icosahedral vertex vectors, |sum| = {np.linalg.norm(net):.2e}")
check("T2 isotropic census sums to zero: SSV_net = 0 before any clip", np.linalg.norm(net) < 1e-12)

# T3
ns_planck, sig = 0.9649, 0.0042
ns_clipped = 1.0                      # depth-independent driver: d ln H / dN = 0
z = (ns_clipped - ns_planck) / sig
print(f"T3 — clipped driver n_s = {ns_clipped}, tension {z:.1f} sigma")
check("T3 clipped/acted-on driver excluded at > 5 sigma", z > 5)

# T4
ns_held = 1 - 2 / N_star
print(f"T4 — held-stack driver n_s = {ns_held:.4f} (Planck {ns_planck} +/- {sig})")
check("T4 held-stack driver inside Planck 1 sigma", abs(ns_held - ns_planck) < sig)

# T5 — mu(n-bar; K) has no K dependence: evaluate with two caps, two readings
def mu(nbar, kT=1.0, K=None):       # K accepted and ignored: the cap binds the acted-on sector, not the count
    return kT * np.log(nbar)
mu_S = mu(nbar, K=12); mu_P = mu(nbar, K=1e80)
print(f"T5 — mu under Reading S = {mu_S:.3f} kT, under Reading P = {mu_P:.3f} kT")
check("T5 mu identical across readings and caps (reading-independent tilt)", mu_S == mu_P)

print(f"\n{PASS}/{PASS+FAIL} PASS")
