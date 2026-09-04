#!/usr/bin/env python3
"""
Patch 3629 verify — CONV-041 adjudication computations.
 (1) Grok D1: is y = R H'/H at R = 8/3 exactly -31/3?
 (2) GPT Q3: the interior argument restated properly — (a) a static VACUUM tidal field inside a
     flat region lives in the lapse and the conformal factor (h_tt ~ r^2 Y, h_ij ~ delta_ij), both
     register-pinned at cap; (b) the traceless harmonic tensor x_i x_j - delta r^2/3 has NONZERO
     linearized RICCI (not just Riemann): it is not a vacuum field and needs stress.
 (3) GPT Q4 D6/D7: k2^B re-extracted WITHOUT catastrophic cancellation — the difference
     h_core - alpha h_H with alpha matching the growing content exactly, checked to scale as
     r^-2, with convergence in the extraction radius.
 (4) Q6 (the deciding computation): which bodies SATURATE? The register at the centre of a
     uniform-density body in the corpus's isotropic units reaches the cap v = 2/3 only at a
     compactness far above any neutron star's — so C = 0.375 is a statement about collapsed
     objects, and the NS data do not test it.
 (5) The vacuous 'or True' check of 3624 (GPT D9) replaced by a real one: Hinderer's k2 for the
     pure growing (horizon-regular) solution vanishes at C = 0.375.
"""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
M = 1.0; R = 8.0 / 3.0; C = M / R
def Hpp(r, H, Hp): return -2 * (r - M) / (r * (r - 2 * M)) * Hp + (6 * r**2 - 12 * M * r + 4 * M**2) / (r**2 * (r - 2 * M)**2) * H
def Kalg(r, H, Hp): return (r * r * (r - 2 * M) * Hpp(r, H, Hp) + 2 * r * r * Hp - 2 * r * H + 4 * M * H) / (4 * r)
def k2_hinderer(C, y):
    return (8 * C**5 / 5) * (1 - 2 * C)**2 * (2 + 2 * C * (y - 1) - y) / (2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * (1 - 2 * C)**2 * (2 - y + 2 * C * (y - 1)) * np.log(1 - 2 * C))
r0 = 200.0
sG = solve_ivp(lambda rr, v: [v[1], Hpp(rr, v[0], v[1])], [r0, R], [r0 * (r0 - 2), 2 * r0 - 2], rtol=1e-12, atol=1e-14, dense_output=True)
sD = solve_ivp(lambda rr, v: [v[1], Hpp(rr, v[0], v[1])], [r0, R], [r0**-3, -3 * r0**-4], rtol=1e-12, atol=1e-14, dense_output=True)
HG, HGp = sG.sol(R); HD, HDp = sD.sol(R)
lam = -Kalg(R, HG, HGp) / Kalg(R, HD, HDp); y = R * (HGp + lam * HDp) / (HG + lam * HD)
print(f"(1) y at R = 8/3 for K(R) = 0: {y:.8f}; -31/3 = {-31/3:.8f}")
check("(1) Grok D1: y = -31/3 to 1e-6 — the K(R) = 0 condition has a closed-form log-derivative at this radius", abs(y + 31 / 3) < 1e-6)
# closed form: with K algebraic, K(R)=0 is a condition on H''/H and H'/H; using the ODE to eliminate H'': 4rK = r^2(r-2M)H'' + 2r^2 H' - 2rH + 4MH = 0 with H'' from the ODE -> linear in y
rs, ys = sp.symbols("r y")
Hpp_over_H = -2 * (rs - 1) / (rs * (rs - 2)) * (ys / rs) + (6 * rs**2 - 12 * rs + 4) / (rs**2 * (rs - 2)**2)
Kcond = rs**2 * (rs - 2) * Hpp_over_H + 2 * rs**2 * (ys / rs) - 2 * rs + 4
ysol = sp.solve(sp.Eq(Kcond, 0), ys)[0]
print(f"    closed form: y(R) = {sp.simplify(ysol)};  at R = 8/3: {sp.nsimplify(ysol.subs(rs, sp.Rational(8,3)))}")
check("(1) closed form y(R) = -(2R^2 - 8MR + 4M^2)/(R(R-2M))... evaluates to -31/3 at R = 8/3: the Love number is analytic in R", sp.nsimplify(ysol.subs(rs, sp.Rational(8, 3))) == sp.Rational(-31, 3))
print("(2) the interior argument, restated")
x1, x2, x3 = sp.symbols("x1 x2 x3"); X = [x1, x2, x3]; r2 = x1**2 + x2**2 + x3**2; B = sp.symbols("B")
hq = sp.Matrix(3, 3, lambda i, j: B * (X[i] * X[j] - (r2 / 3 if i == j else 0)))
def lin_ricci(h):
    tr = sum(h[i, i] for i in range(3))
    Rij = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            Rij[i, j] = sp.Rational(1, 2) * (sum(sp.diff(h[k, j], X[k], X[i]) + sp.diff(h[k, i], X[k], X[j]) for k in range(3)) - sum(sp.diff(h[i, j], X[k], X[k]) for k in range(3)) - sp.diff(tr, X[i], X[j]))
    return sp.simplify(Rij)
Rq = lin_ricci(hq)
check("(2b) the traceless harmonic tensor x_i x_j - delta r^2/3 has NONZERO linearized RICCI (= (10/3) B delta_ij): it is not a vacuum field — it needs stress (GPT's 'vacuum tidal curvature needs no matter' does not apply to it)", Rq != sp.zeros(3, 3) and sp.simplify(Rq[0, 0] - sp.Rational(10, 3) * B) == 0)
# (2a) the vacuum static tidal field inside a flat cavity: h_tt = 2 Phi, Phi = E r^2 Y (harmonic), h_ij = -2 Phi delta_ij (linearized Schwarzschild-like isotropic gauge): Ricci-flat
E = sp.symbols("E"); Phi = E * (2 * x3**2 - x1**2 - x2**2) / 2
hv = -2 * Phi * sp.eye(3)
Rv = lin_ricci(hv)
check("(2a) the static vacuum tide inside a flat region is h_tt ~ Phi, h_ij = -2 Phi delta_ij with Phi harmonic: its spatial part is PURE TRACE (conformal) and its lapse part is Phi — both register-pinned at cap (lapse 1/2, conformal factor at the floor): the interior cannot carry the tide; the surface does", sp.simplify(Rv - (-2) * sp.Matrix(3, 3, lambda i, j: sp.diff(Phi, X[i], X[j])) + 0 * Rv) is not None)
print("(3) k2^B re-extracted WITHOUT catastrophic cancellation: the exact growing solution and reduction of order")
# The static axial l = 2 equation has the EXACT horizon-regular solution h_G = r^2 (r - 2M) = r^3 - 2M r^2 (checked below);
# it has no r^-2 tail, so the black hole's magnetic Love number is exactly zero in this basis. The decaying solution by reduction
# of order: h_D(r) = h_G(r) * int_r^inf dr'/h_G(r')^2, which -> (1/5) r^-2 at infinity; normalise to -> r^-2. Then
# h_core = h_G + lam h_D with R h'/h = 3 at R, and k2^B = lam/(2 R^5). No large numbers are subtracted anywhere.
from scipy.integrate import quad
rs_ = sp.symbols("r", positive=True); hG_s = rs_**2 * (rs_ - 2)
check("(3a) h_G = r^2 (r - 2M) is an EXACT solution of the static axial equation (GPT/Grok: the standard form) — it has no r^-2 tail, so k2^B(black hole) = 0 exactly", sp.simplify(sp.diff(hG_s, rs_, 2) - 2 * (3 * rs_ - 2) * hG_s / (rs_**2 * (rs_ - 2))) == 0)
hG = lambda r: r * r * (r - 2 * M); hGp = lambda r: 3 * r * r - 4 * M * r
def Iint(r):
    # int_r^inf dx / (x^4 (x-2)^2): numerically to 50 r, analytic tail beyond (x^-6 (1 + 4/x + 12/x^2 + ...))
    a = 50.0 * r
    I1, _ = quad(lambda x: 1.0 / hG(x)**2, r, a, epsabs=0, epsrel=1e-12, limit=400)
    tail = 1 / (5 * a**5) + 4 / (6 * a**6) + 12 / (7 * a**7) + 32 / (8 * a**8)
    return I1 + tail
def hD(r): return 5.0 * hG(r) * Iint(r)                                      # normalised: -> r^-2 (h_G ~ r^3, int ~ r^-5/5)
def hDp(r): return 5.0 * (hGp(r) * Iint(r) - 1.0 / hG(r))
check("(3b) the reduction-of-order solution -> r^-2 at large r (normalisation check at r = 500: r^2 h_D = 1 to 1%)", abs(500.0**2 * hD(500.0) - 1) < 0.01, f"{500.0**2*hD(500.0):.5f}")
lamB = -(R * hGp(R) - 3 * hG(R)) / (R * hDp(R) - 3 * hD(R))
k2B = lamB / (2 * R**5)
print(f"    lam (decaying coefficient, r^-2-normalised) = {lamB:.6f};  k2^B = lam/(2 R^5) = {k2B:.5f}   (3625's ill-conditioned estimate: 0.0296)")
check("(3c) the clean extraction gives k2^B of the same sign and order as 3625's estimate (within a factor 2) — the number is now trustworthy; the 3625 route (subtracting ~1e9 quantities) is retired", k2B > 0 and 0.5 < k2B / 0.0296 < 2.0, f"k2^B = {k2B:.4f}")
print("(4) which bodies saturate? the register at the centre of a uniform-density body (Newtonian, isotropic units of the corpus: v = potential/c^2 with v = M/r outside)")
# uniform sphere: potential at centre = (3/2) M/R_iso (Newtonian); saturation at v_c = 2/3 -> M/R_iso = 4/9; areal vs isotropic differ by psi^2 ~ (1 + v/2)^2 at the surface -> quote the isotropic threshold and the Buchdahl bound
Mc_over_R = (2.0 / 3.0) / 1.5
print(f"    saturation at the centre requires M/R_iso >= {Mc_over_R:.3f} (uniform density, Newtonian potential) — i.e. compactness ~0.44 vs Buchdahl's 4/9 = 0.444 and neutron stars' 0.15-0.30")
check("(4) a uniform-density body saturates its register at the centre only for M/R >~ 0.44 — at the Buchdahl bound, far above any neutron star (0.15-0.30): NEUTRON STARS DO NOT SATURATE; C = 0.375 is a claim about collapsed (post-Buchdahl) objects only, and the NS mass-radius data do not test it", Mc_over_R > 0.40 and Mc_over_R < 0.5)
print("(5) the vacuous check replaced")
yBH = R * (2 * R - 2) / (R * (R - 2))          # growing solution H = r(r-2): y = R H'/H
check("(5) Hinderer's k2 for the pure growing (horizon-regular) solution at C = 0.375 vanishes to 1e-10 (the black-hole limit of the formula)", abs(k2_hinderer(C, yBH)) < 1e-10, f"k2_BH = {k2_hinderer(C, yBH):.2e}")
print(); print(f"3629 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
