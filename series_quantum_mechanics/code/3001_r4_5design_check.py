#!/usr/bin/env python3
"""Patch 3001 — R-4 plane-stability verify script.

Checks, numerically:
 (1) DESIGN: the 12 icosahedral neighbor directions form a spherical
     5-design — moments of order 1..5 are exactly isotropic (odd ones
     vanish by parity); the order-6 moment carries the first
     anisotropy (nonzero residual).
 (2) CLOSURE-A: the scalar (component-diagonal) tight-binding stencil
     — the transport class the shipped QM-1 dynamics uses — maps
     in-plane vector fields to in-plane vector fields EXACTLY
     (out-of-plane output at machine zero), for a randomly oriented
     plane.
 (3) SCALING-B: for a direction-coupled transport kernel
     T(v) = alpha*I + beta*v v^T (the general single-edge form), with
     an in-plane field varying ONLY in-plane, the out-of-plane
     generation scales as (k*s)^4 — the 5-design suppression of the
     lattice-anisotropic channel (isotropic pieces, built from deltas
     alone, cannot manufacture an out-of-plane direction).
 (4) CONTRAST-B2: same kernel, field varying ALSO along the plane
     normal — the isotropic grad-div channel activates at (k*s)^2,
     confirming the case split (that channel is the longitudinal/
     transverse physics, not lattice leakage).

NEGATIVE CONTROL: replacing the icosahedron with a 6-vertex
octahedron (only a 3-design; first anisotropy at order 4) must move
the SCALING-B slope from 4 to 2 — the suppression is a property of
the icosahedral design order, not of the test harness.
"""
import numpy as np

rng = np.random.default_rng(31001)
PHI = (1 + 5**0.5) / 2

def icosahedron():
    v = []
    for s1 in (1,-1):
        for s2 in (1,-1):
            v += [(0, s1, s2*PHI), (s1, s2*PHI, 0), (s2*PHI, 0, s1)]
    v = np.array(v, float)
    return v / np.linalg.norm(v[0])

def octahedron():
    return np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]], float)

def sym_iso_projection(M):
    """Project a fully symmetric even-rank tensor onto the isotropic
    (delta-built) subspace by lsq over symmetrized delta products."""
    n = M.ndim
    idx = list(range(n))
    import itertools
    # build basis of symmetrized products of deltas over pairings
    pairings = []
    def pairs(rem):
        if not rem: yield []
        else:
            a = rem[0]
            for i in range(1, len(rem)):
                b = rem[i]
                rest = [x for x in rem[1:] if x != b]
                for p in pairs(rest): yield [(a,b)] + p
    basis = []
    for p in pairs(idx):
        T = np.zeros_like(M)
        it = np.nditer(T, flags=['multi_index'])
        for _ in it:
            mi = it.multi_index
            val = 1.0
            for (a,b) in p:
                val *= 1.0 if mi[a]==mi[b] else 0.0
            T[mi] = val
        basis.append(T)
    A = np.stack([b.ravel() for b in basis], axis=1)
    coef, *_ = np.linalg.lstsq(A, M.ravel(), rcond=None)
    iso = (A @ coef).reshape(M.shape)
    return iso

def moment(V, n):
    M = np.zeros((3,)*n)
    for v in V:
        T = v
        for _ in range(n-1):
            T = np.multiply.outer(T, v)
        M += T
    return M

def design_report(V, name):
    print(f"--- DESIGN CHECK: {name} ({len(V)} vertices) ---")
    first_aniso = None
    for n in range(1, 7):
        M = moment(V, n)
        if n % 2 == 1:
            r = np.linalg.norm(M)/max(1e-300, len(V))
            ok = r < 1e-12
            print(f" order {n}: odd moment |M|/N = {r:.3e}  ({'ZERO (parity)' if ok else 'NONZERO'})")
            if not ok and first_aniso is None: first_aniso = n
        else:
            iso = sym_iso_projection(M)
            rel = np.linalg.norm(M - iso)/np.linalg.norm(M)
            ok = rel < 1e-12
            print(f" order {n}: anisotropic residual (rel) = {rel:.3e}  ({'ISOTROPIC' if ok else 'ANISOTROPIC'})")
            if not ok and first_aniso is None: first_aniso = n
    print(f" first anisotropic order: {first_aniso}")
    return first_aniso

def random_plane():
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    a = np.cross(n, rng.normal(size=3)); a /= np.linalg.norm(a)
    b = np.cross(n, a)
    return n, a, b

def stencil_out_of_plane(V, ks, beta, inplane_variation_only, n, a, b, alpha=1.0, npts=200):
    """Apply K f(0) = sum_j T(v_j) f(s v_j) with f an in-plane field.
    f(r) = a*cos(k.r) + b*sin(k.r), |k| = ks (units s=1). Return max
    |n . K f| over random k of the stated class / |K f|."""
    worst = 0.0
    for _ in range(npts):
        if inplane_variation_only:
            th = rng.uniform(0, 2*np.pi)
            k = ks*(np.cos(th)*a + np.sin(th)*b)
        else:
            k = rng.normal(size=3); k = ks*k/np.linalg.norm(k)
        out = np.zeros(3)
        for v in V:
            f = a*np.cos(k@v) + b*np.sin(k@v)
            T = alpha*f + beta*v*(v@f)
            out += T
        denom = np.linalg.norm(out)
        if denom > 1e-300:
            worst = max(worst, abs(n@out)/denom)
    return worst

def slope_fit(V, beta, inplane_only, n, a, b, label):
    kss = np.array([0.3, 0.1, 0.03, 0.01])
    vals = np.array([stencil_out_of_plane(V, ks, beta, inplane_only, n, a, b) for ks in kss])
    # guard against exact zeros
    vals = np.maximum(vals, 1e-300)
    sl = np.polyfit(np.log(kss), np.log(vals), 1)[0]
    print(f" {label}: out-of-plane fraction at ks={kss.tolist()} -> {['%.3e'%x for x in vals]}; log-log slope = {sl:.2f}")
    return sl, vals

print("="*70)
ICO = icosahedron()
fa_ico = design_report(ICO, "icosahedron (600-cell 3D neighbor shell, z=12)")
assert fa_ico == 6, "FAIL: icosahedron first anisotropy expected at order 6 (5-design)"
print(" PASS: 5-design confirmed (first anisotropy at order 6)\n")

n, a, b = random_plane()
print(f"--- CLOSURE-A: scalar stencil (beta=0), random plane, normal n = {np.round(n,4).tolist()} ---")
w = stencil_out_of_plane(ICO, 0.5, beta=0.0, inplane_variation_only=False, n=n, a=a, b=b)
print(f" max out-of-plane fraction (any k direction, ks=0.5): {w:.3e}")
assert w < 1e-12, "FAIL: scalar stencil must preserve the plane exactly"
print(" PASS: component-diagonal transport preserves the plane EXACTLY (all k)\n")

print("--- SCALING-B: direction-coupled kernel (beta=1), in-plane-only variation ---")
sl_b, _ = slope_fit(ICO, beta=1.0, inplane_only=True, n=n, a=a, b=b, label="icosahedron")
assert 3.5 < sl_b < 4.6, f"FAIL: expected ~(ks)^4 anisotropic suppression, got slope {sl_b:.2f}"
print(" PASS: lattice-anisotropic out-of-plane channel suppressed as (ks)^4 (5-design)\n")

print("--- CONTRAST-B2: same kernel, variation including the plane normal ---")
sl_b2, _ = slope_fit(ICO, beta=1.0, inplane_only=False, n=n, a=a, b=b, label="icosahedron/3D-k")
assert 1.6 < sl_b2 < 2.5, f"FAIL: expected (ks)^2 grad-div (isotropic) channel, got slope {sl_b2:.2f}"
print(" PASS: the (ks)^2 channel is the isotropic grad-div (longitudinal) physics, present only with normal-direction variation\n")

print("--- NEGATIVE CONTROL: octahedron (3-design; first anisotropy at order 4) ---")
OCT = octahedron()
fa_oct = design_report(OCT, "octahedron (z=6)")
assert fa_oct == 4, "FAIL: octahedron first anisotropy expected at order 4"
n2, a2, b2 = random_plane()
sl_o, _ = slope_fit(OCT, beta=1.0, inplane_only=True, n=n2, a=a2, b=b2, label="octahedron")
assert 1.6 < sl_o < 2.6, f"FAIL: control expected ~(ks)^2 on the 3-design, got slope {sl_o:.2f}"
print(" PASS: control confirms the exponent tracks the DESIGN ORDER (icosahedron 4 vs octahedron 2)\n")

lp_over_lc = 1.616e-35 / 2.426e-12   # l_P / lambda_C(electron)
eps = (2*np.pi*lp_over_lc)**4
print(f"--- BOUND MAGNITUDE --- (Delta s <= l_P; lambda >= lambda_C(e))")
print(f" relative anisotropic leakage per refresh  <= (2 pi l_P/lambda_C)^4 = {eps:.3e}")
print("="*70)
print("ALL ASSERTIONS PASS")
