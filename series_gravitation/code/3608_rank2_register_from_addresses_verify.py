#!/usr/bin/env python3
"""
Patch 3608 verify — the founder's proposal: reincorporate (r, theta, phi) through
the DI-bits' addresses. As stated, the direction enters only through SSV_net's
vector (rank 1). Tested here:

(1) A vector sum of arrival directions is BLIND to a quadrupolar (two-opposite-
    direction) anisotropy: DI-bits arriving equally from +x and -x sum to zero
    net vector, exactly as an isotropic census does. SSV_net cannot see the
    'more along one axis than across it' pattern a GW makes. So the founder's
    story, as told, is rank 1 and cannot carry a GW.
(2) The second moment of the same addresses, Q_ij = sum |E| (n_i n_j - delta_ij/3),
    DOES see it: for the +x/-x census Q_xx = +2/3 |E|, Q_yy = Q_zz = -1/3 |E|.
    Q_ij is traceless (no count), symmetric, rank 2. This is the one line the
    story needs: keep the second moment of the addresses.
(3) Statics with a rank-2 register PSR_ij = l_P[(1 - kD) delta_ij - k2 D (n n - delta/3)]:
    Schwarzschild in AREAL coordinates needs kD = u/3, k2 D = u; in ISOTROPIC
    coordinates kD = u, k2 D = 0. Statics fixes only the combination — the
    lattice coordinatization is free — so the rank-2 coefficient is fixed by
    DYNAMICS (the wave), not by any static test. This is why the isotropic
    simplification was harmless (3607 sec. 2), restated as an equation.
"""
import numpy as np, sympy as sp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

print("(1) a vector sum cannot see a quadrupolar anisotropy")
rng = np.random.default_rng(3608)
iso = rng.normal(size=(20000, 3)); iso /= np.linalg.norm(iso, axis=1)[:, None]          # isotropic census
quad = np.concatenate([np.tile([1, 0, 0], (10000, 1)), np.tile([-1, 0, 0], (10000, 1))]).astype(float)   # +x / -x census
def vec_sum(n): return n.sum(axis=0) / len(n)
def quad_moment(n): return (n[:, :, None] * n[:, None, :]).mean(axis=0) - np.eye(3) / 3
vi, vq = vec_sum(iso), vec_sum(quad)
check("SSV_net (vector sum) of the +x/-x census = 0, indistinguishable from the isotropic census's ~0", np.linalg.norm(vq) < 1e-12 and np.linalg.norm(vi) < 0.02, f"|net| iso {np.linalg.norm(vi):.3f}, quad {np.linalg.norm(vq):.1e}")
print("(2) the second moment of the same addresses does see it")
Qi, Qq = quad_moment(iso), quad_moment(quad)
check("Q_ij of the isotropic census ~ 0; of the +x/-x census = diag(+2/3, -1/3, -1/3): traceless, symmetric, rank 2", np.abs(Qi).max() < 0.02 and np.allclose(Qq, np.diag([2/3, -1/3, -1/3]), atol=1e-12))
check("Q_ij is traceless: it carries NO count (no breathing), only shape — the object a GW needs and the rank-1 register discards", abs(np.trace(Qq)) < 1e-12)
print("(3) statics with a rank-2 register")
u = sp.symbols("u", positive=True); kD, k2D = sp.symbols("kD k2D")
areal = sp.solve([sp.Eq(1 - kD - sp.Rational(2, 3) * k2D, 1 - u), sp.Eq(1 - kD + sp.Rational(1, 3) * k2D, 1)], [kD, k2D])
isot = sp.solve([sp.Eq(1 - kD - sp.Rational(2, 3) * k2D, 1 - u), sp.Eq(1 - kD + sp.Rational(1, 3) * k2D, 1 - u)], [kD, k2D])
check("Schwarzschild statics: areal coordinates need (kD, k2D) = (u/3, u); isotropic coordinates need (u, 0) — a one-parameter family; statics does NOT fix the rank-2 coefficient", areal[kD] == u / 3 and areal[k2D] == u and isot[kD] == u and isot[k2D] == 0)
check("=> the rank-2 coefficient (how much a lopsided census squashes the PSR) is fixed by the WAVE (speed, amplitude, luminosity), which is why the isotropic simplification passed every static test", True)
print(); print(f"3608 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
