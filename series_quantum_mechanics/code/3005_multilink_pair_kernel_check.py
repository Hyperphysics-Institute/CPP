#!/usr/bin/env python3
"""Patch 3005 — OPEN-QMRG-R4-MULTILINK verify script: pair-kernel
plane-leakage taxonomy on the icosahedral shell.

Complements the registry exclusion argument (see
sketches/3005_multilink_refresh_law_analysis.md): the ratified
protocol (A3' additive vector-sum register formation + per-Moment
reset + AP-2 minimal DI-bit content) forces the single-edge kernel
class. This script maps what WOULD happen in the excluded classes:

 (1) CROSS-SUM: for any SYMMETRIC pair weight w(v_a.v_b), the chiral
     cross sum  sum_{a!=b} w(v_a.v_b)(v_a x v_b)  vanishes
     IDENTICALLY on the shell (antisymmetry under a<->b) — machine
     zero for several w.
 (2) SEPARABLE-PAIR SCALING: a separable pair kernel (factorizing
     into single-vertex moment factors) INHERITS the design
     suppression — anisotropic component-mixing needs an order->=6
     moment in a single factor; measured out-of-plane slope >= 4 for
     in-plane fields varying in-plane.
 (3) NON-SEPARABLE CHIRAL CONTROL: an asymmetric-weight cross-product
     pair kernel (the class the ratified protocol EXCLUDES) leaks the
     plane at low order (slope <= 2) — demonstrating the excluded
     class is genuinely dangerous, which is what gives the registry
     exclusion its force.

KEY-DESIGN-RULE COMPLIANCE (registered Patch 3004): after all printed
checks, the RNG stream advances to generate a SENTINEL configuration
(fresh random plane, random beta in [0.5,1.5], unprinted ks) whose
out-of-plane fraction is computed into the variable `sentinel_value`
and NEVER printed, logged, or stored. It is not on any printed curve
and cannot be reconstructed from printed data (it depends on the
post-checks RNG state). A future dispatch may define a withheld key
as this sentinel (to stated precision); obtaining it requires
executing this file.
"""
import numpy as np
rng = np.random.default_rng(31005)
PHI = (1 + 5**0.5) / 2

def icosahedron():
    v = []
    for s1 in (1,-1):
        for s2 in (1,-1):
            v += [(0, s1, s2*PHI), (s1, s2*PHI, 0), (s2*PHI, 0, s1)]
    v = np.array(v, float)
    return v / np.linalg.norm(v[0])

V = icosahedron()

print("="*70)
print("--- (1) CROSS-SUM: symmetric-weight chiral sums vanish identically ---")
for name, w in [("w=1", lambda c: 1.0),
                ("w=(va.vb)", lambda c: c),
                ("w=(va.vb)^2", lambda c: c*c)]:
    S = np.zeros(3)
    for i in range(len(V)):
        for j in range(len(V)):
            if i == j: continue
            S += w(V[i]@V[j]) * np.cross(V[i], V[j])
    r = np.linalg.norm(S)
    print(f" {name}: |sum_(a!=b) w (va x vb)| = {r:.3e}")
    assert r < 1e-12, f"FAIL: symmetric-weight cross sum must vanish ({name})"
print(" PASS: symmetric pair weights cannot source a chiral vector on the shell\n")

def random_plane():
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    a = np.cross(n, rng.normal(size=3)); a /= np.linalg.norm(a)
    b = np.cross(n, a)
    return n, a, b

def out_frac(kernel, ks, n, a, b, npts=200):
    worst = 0.0
    for _ in range(npts):
        th = rng.uniform(0, 2*np.pi)
        k = ks*(np.cos(th)*a + np.sin(th)*b)   # in-plane variation only
        out = kernel(k, a, b)
        d = np.linalg.norm(out)
        if d > 1e-300:
            worst = max(worst, abs(n@out)/d)
    return worst

def slope_fit(kernel, n, a, b, label):
    kss = np.array([0.3, 0.1, 0.03, 0.01])
    vals = np.maximum([out_frac(kernel, ks, n, a, b) for ks in kss], 1e-300)
    sl = np.polyfit(np.log(kss), np.log(vals), 1)[0]
    print(f" {label}: out-of-plane fraction {['%.3e'%v for v in vals]}; slope = {sl:.2f}")
    return sl

n, a, b = random_plane()

print("--- (2a) SEPARABLE-PAIR, isotropic coupling factor: EXACT preservation ---")
M2 = sum(np.outer(v, v) for v in V)   # order-2 moment factor (exactly isotropic by the design)
def sep_kernel_iso(k, ea, eb):
    f = lambda r: ea*np.cos(k@r) + eb*np.sin(k@r)
    acc = np.zeros(3)
    for vb in V:
        acc += f(vb)                   # component-diagonal deposit factor
    return (M2 @ acc) / len(V)
w = out_frac(sep_kernel_iso, 0.3, n, a, b)
print(f" M2 x scalar-stencil: max out-of-plane fraction at ks=0.3 = {w:.3e}")
assert w < 1e-12, "FAIL: isotropic-coupling separable kernel must preserve the plane exactly"
print(" PASS: an isotropic (order<=5 moment) coupling factor cannot leak AT ALL —")
print("       exact, stronger than suppression; the design makes the factor a multiple of I\n")

print("--- (2b) SEPARABLE-PAIR, direction-coupled deposit: inherits the (ks)^4 class ---")
def sep_kernel_beta(k, ea, eb):
    # separable: [order-2 moment factor] x [single-edge beta stencil]
    f = lambda r: ea*np.cos(k@r) + eb*np.sin(k@r)
    acc = np.zeros(3)
    for vb in V:
        acc += vb * (vb @ f(vb))       # direction-coupled per-edge deposit
    return (M2 @ acc) / len(V)
sl2 = slope_fit(sep_kernel_beta, n, a, b, "separable (M2 x beta-stencil)")
assert sl2 > 3.5, f"FAIL: separable direction-coupled pair kernel should inherit the 4th-order class, got {sl2:.2f}"
print(" PASS: separable pair kernels inherit the single-edge suppression —")
print("       anisotropy still needs an order>=6 moment INSIDE one factor\n")

print("--- (3) NON-SEPARABLE CHIRAL control: the excluded class leaks at low order ---")
n0 = rng.normal(size=3); n0 /= np.linalg.norm(n0)  # fixed asymmetry axis
def chiral_kernel(k, ea, eb):
    f = lambda r: ea*np.cos(k@r) + eb*np.sin(k@r)
    acc = np.zeros(3)
    for i in range(len(V)):
        for j in range(len(V)):
            if i == j: continue
            wij = 1.0 if (V[i]@n0) > 0 else 0.0    # ASYMMETRIC weight: breaks a<->b cancellation
            acc += wij * np.cross(V[i], V[j]) * (V[j] @ f(V[j]))
    return acc / len(V)**2
sl3 = slope_fit(chiral_kernel, n, a, b, "non-separable chiral (excluded class)")
assert sl3 < 3.0, f"FAIL: excluded chiral class should leak at low order, got slope {sl3:.2f}"
print(" PASS: the excluded non-separable cross-product class is genuinely dangerous —")
print("       the registry exclusion (A3' additivity + AP-2 minimality) is load-bearing\n")

# ---- SENTINEL (unprinted; see docstring / KEY-DESIGN RULE) ----
sn, sa, sb = random_plane()
s_beta = rng.uniform(0.5, 1.5)
def sent_kernel(k, ea, eb):
    f = lambda r: ea*np.cos(k@r) + eb*np.sin(k@r)
    acc = np.zeros(3)
    for v in V:
        fv = f(v)
        acc += fv + s_beta * v * (v @ fv)
    return acc
sentinel_value = out_frac(sent_kernel, 0.017, sn, sa, sb)   # deliberately unprinted
_ = sentinel_value

print("="*70)
print("ALL ASSERTIONS PASS")
