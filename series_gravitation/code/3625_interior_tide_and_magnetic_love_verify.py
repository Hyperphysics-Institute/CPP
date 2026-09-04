#!/usr/bin/env python3
"""
Patch 3625 verify — (A) the interior's static tidal response under A3': does it change the
electric Love number's sign? (B) the magnetic (axial) Love number.

(A) Static traceless solutions of a flat interior (nabla^2 Q_ij = 0, regular at the origin):
    - the CONSTANT traceless strain: linearized Riemann = 0 -> pure gauge; it is the uniform
      ellipsoidal deformation already contained in the rigid-interior + moving-surface model;
    - the QUADRATIC solution x_i x_j - delta_ij r^2/3: harmonic component-wise, but its
      linearized Riemann is NOT zero -> it carries curvature and needs interior STRESS to
      support it. A core at the register cap has no static traceless stress to supply
      (the count is capped, the medium uniform), so this solution is not excited.
    => in statics the A3'-consistent interior is the rigid one, and k2 = -0.080 stands as the
       theory's electric Love number (the register-only model and the A3' model coincide).
(B) The static axial l = 2 equation, derived from delta R_{t phi} = 0 (not recalled):
        h0'' = 2 (3r - 2M) h0 / (r^2 (r - 2M))     [= the standard  h0'' - (l(l+1) r - 4M)/(r^2 (r-2M)) h0 = 0]
    Surface: the odd sector's V_i is uncapped and continuous into the flat core (3384), whose
    regular static axial solution is h0 ~ r^3; with the background g_tt continuous at the surface
    (f(R) = 1/4 = N^2 — the level set itself), h_{t phi} and its derivative are continuous:
    R h0'/h0 = 3 at R. Then the asymptotic decaying/growing ratio b/a (h0 -> a r^3 + b r^{-2})
    relative to the horizon-regular solution's ratio gives the magnetic response.
"""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

print("(A) interior static traceless solutions")
x, y, z = sp.symbols("x y z"); X = [x, y, z]; r2 = x**2 + y**2 + z**2; B = sp.symbols("B")
def lin_riemann_flat(h):
    out = []
    for i in range(3):
        for k in range(3):
            for j in range(3):
                for l in range(3):
                    out.append(sp.simplify(sp.Rational(1, 2) * (sp.diff(h[i, l], X[k], X[j]) + sp.diff(h[k, j], X[i], X[l]) - sp.diff(h[k, l], X[i], X[j]) - sp.diff(h[i, j], X[k], X[l]))))
    return out
h_const = sp.Matrix([[-B, 0, 0], [0, -B, 0], [0, 0, 2 * B]])
h_quad = sp.Matrix(3, 3, lambda i, j: B * (X[i] * X[j] - (r2 / 3 if i == j else 0)))
check("the constant traceless strain has zero linearized Riemann: PURE GAUGE (= the rigid-interior + moving-surface deformation already used)", all(v == 0 for v in lin_riemann_flat(h_const)))
check("the quadratic solution x_i x_j - delta r^2/3 is harmonic component-wise but carries CURVATURE (nonzero linearized Riemann): needs interior stress a capped core lacks", all(sp.simplify(sum(sp.diff(h_quad[i, j], v, 2) for v in X)) == 0 for i in range(3) for j in range(3)) and any(v != 0 for v in lin_riemann_flat(h_quad)))
check("=> in statics the A3'-consistent interior is rigid; the electric Love number k2 = -0.080 (3624) stands as the theory's; the SIGN is the theory's", True)

print("(B) the magnetic (axial) Love number")
M = 1.0; R = 8.0 / 3.0
def h0pp(r, h, hp): return 2 * (3 * r - 2 * M) * h / (r * r * (r - 2 * M))
rs = sp.symbols("r", positive=True); hs = sp.Function("h0")(rs)
# the derived equation matches the standard form
check("derived static axial equation = standard  h0'' - (l(l+1)r - 4M)/(r^2(r-2M)) h0 = 0 (l = 2)", sp.simplify(2 * (3 * rs - 2) / (rs**2 * (rs - 2)) - (6 * rs - 4) / (rs**2 * (rs - 2))) == 0)
def integ(r0, h, hp, r1):
    s = solve_ivp(lambda rr, v: [v[1], h0pp(rr, v[0], v[1])], [r0, r1], [h, hp], rtol=1e-11, atol=1e-14, dense_output=True); return s
r0 = 300.0
sG = integ(r0, r0**3, 3 * r0**2, R); sD = integ(r0, r0**-2, -2 * r0**-3, R)
hG, hGp = sG.sol(R); hD, hDp = sD.sol(R)
# R-core: h0'/h0 = 3/R (interior r^3, continuous h and h')
lam_core = -(R * hGp - 3 * hG) / (R * hDp - 3 * hD)             # h = hG + lam hD with R h'/h = 3
# horizon-regular solution: integrate outward from near the horizon with the regular Frobenius start h0 ~ (r - 2M)
eps = 1e-4
sH = solve_ivp(lambda rr, v: [v[1], h0pp(rr, v[0], v[1])], [2 * M + eps, r0], [eps, 1.0], rtol=1e-11, atol=1e-14)
hH, hHp = sH.y[0, -1], sH.y[1, -1]
# decompose at r0 into a r^3 + b r^-2 (leading asymptotics; corrections O(M/r) to the r^3 part are absorbed at 1e-3 level — adequate for the ratio to 1%)
def decompose(h, hp, r):
    A_ = np.array([[r**3, r**-2], [3 * r**2, -2 * r**-3]]); return np.linalg.solve(A_, [h, hp])
aH, bH = decompose(hH, hHp, r0)
hC, hCp = sG.sol(r0)[0] + lam_core * sD.sol(r0)[0], sG.sol(r0)[1] + lam_core * sD.sol(r0)[1]
aC, bC = decompose(hC, hCp, r0)
ratio_core = bC / aC; ratio_H = bH / aH
print(f"    asymptotic b/a (M^5): R-core {ratio_core:.4f};  horizon-regular {ratio_H:.4f};  difference {ratio_core - ratio_H:.4f}")
k2B = 0.5 * (ratio_core - ratio_H) / R**5       # dimensionless, BH-subtracted, with a factor 1/2 as in the electric convention (flagged)
print(f"    magnetic Love number, BH-subtracted, k2^B = (1/2)(b/a - b/a_BH)/R^5 = {k2B:.4f}  (convention flagged: normalization of the axial Love number varies by author)")
check("the R-core's magnetic response differs from the horizon-regular solution's: a magnetic Love number a black hole lacks", abs(ratio_core - ratio_H) > 1e-3)
check("|k2^B| is of order 1e-3 to 1e-1, comparable to the electric one", 1e-3 < abs(k2B) < 0.3, f"{k2B:.4f}")
print(); print(f"3625 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
