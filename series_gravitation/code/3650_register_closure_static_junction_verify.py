#!/usr/bin/env python3
"""
Patch 3650 verify — attempt 3b, STATIC run: the register closure matched to the vacuum exterior in ONE gauge.

Both sides in lattice (isotropic) coordinates rbar, RW-type form g = diag(-N^2(1+H0 Y), psi^4(1-H2 Y), psi^4 rbar^2 (1-K Y) Omega).
The budget background joins the isotropic-Schwarzschild exterior C^1 at rbar = 3M/2 (3640). The exterior static l=2 RW
solution (3624's equations) transforms to this form with H0 = H2 = H, K = K. The register closure inside:
delta g = (dg/dv_eff) chi(v) delta v  =>  H0 = 2 N_v chi dv/N,  H2 = K = -2 chi dv/psi  (conformally flat: 3378 part 1).
Junction of the displaced surface rbar = Rbar + xi Y (extrinsic curvature derived symbolically in this script):
  induced metric: [H0] = 0, [K] = 0 (xi drops out: the background is C^1);
  extrinsic:      [dK_tt] = 0  <=> [H0'] = -2 xi [N'']/N ;  [dK_thth] = 0 <=> [K'] = 4 xi [psi'']/psi ;  Y_:AB part: identically 0.
Results: (1) [H0]=0 and the closure force the wall ratio K/H = -N/(psi N_v) = 2/3 EXACTLY (chi- and count-law-independent).
(2) The exterior's pure decaying solution (the static zero mode = Hinderer's pole) has K/H = 0.6615 at 8M/3: the closure
sits 0.8% from a zero-frequency l=2 deformation. Formal k2 = +7.9 (pole-adjacent; NOT a number to carry); the sign of
k2 flips at q = 0.6615, within the corpus's O(v) dictionary uncertainty at the wall (3633 §2). (3) The displacement the
geometry demands, xi/H = -1.21, exceeds the level-set rule's -1.00 by 21%; the two extrinsic conditions leave a residual
0.011 H independent of the interior count law: a small induced l=2 surface layer under a tide. (4) Row 6 re-cut.
"""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
M = 1.0; R = 8 / 3; Rb = 1.5; CAP = 2 / 3
def hinderer_k2(y, C=3 / 8):
    fC = 1 - 2 * C; den = 2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * fC**2 * (2 - y + 2 * C * (y - 1)) * np.log(fC)
    return 8 * C**5 / 5 * fC**2 * (2 + 2 * C * (y - 1) - y) / den

# ---------------- (0) the perturbed extrinsic curvature, derived
print("(0) extrinsic curvature of the displaced surface, first order, isotropic RW form (derived)")
t, rb, th, ph, eps, Rbs, xi = sp.symbols("t rbar theta phi epsilon Rbar xi")
Nf_ = sp.Function("N")(rb); Pf_ = sp.Function("psi")(rb); H0f = sp.Function("H0")(rb); H2f = sp.Function("H2")(rb); Kf = sp.Function("K")(rb); Y = sp.Function("Y")(th)
X = [t, rb, th, ph]
g = sp.diag(-Nf_**2 * (1 + eps * H0f * Y), Pf_**4 * (1 - eps * H2f * Y), Pf_**4 * rb**2 * (1 - eps * Kf * Y), Pf_**4 * rb**2 * sp.sin(th)**2 * (1 - eps * Kf * Y)); gi = g.inv()
def christ(a, b, c): return sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(4)) / 2
Gam = [[[christ(a, b, c) for c in range(4)] for b in range(4)] for a in range(4)]
F = rb - Rbs - eps * xi * Y; dF = [sp.diff(F, x) for x in X]
n = [dF[a] / sp.sqrt(sum(gi[a2, b] * dF[a2] * dF[b] for a2 in range(4) for b in range(4))) for a in range(4)]
Dn = sp.Matrix(4, 4, lambda a, b: sp.diff(n[b], X[a]) - sum(Gam[c][a][b] * n[c] for c in range(4)))
e = {0: [1, 0, 0, 0], 2: [0, eps * xi * sp.diff(Y, th), 1, 0], 3: [0, 0, 0, 1]}
def Kab(a, b): return sum(e[a][m] * e[b][nn] * Dn[m, nn] for m in range(4) for nn in range(4))
def lin(expr):
    ex = expr.subs(rb, Rbs + eps * xi * Y); return sp.simplify(ex.subs(eps, 0).doit()), sp.simplify(sp.diff(ex, eps).subs(eps, 0).doit())
Ktt0, Ktt1 = lin(Kab(0, 0)); Kth0, Kth1 = lin(Kab(2, 2))
Ysub = {sp.diff(Y, th, 2): -sp.cot(th) * sp.diff(Y, th) - 6 * Y}
Ktt1 = sp.simplify(Ktt1.subs(Ysub)); Kth1 = sp.simplify(Kth1.subs(Ysub))
d2 = lambda F_: sp.Derivative(F_, (rb, 2)).subs(rb, Rbs)
d1 = lambda F_: sp.Derivative(F_, rb).subs(rb, Rbs)
pd = lambda e_: sp.powdenest(e_, force=True)
check("(0a) background K_tt = -N N'/psi^2 and K_thth = Rbar psi (psi + 2 Rbar psi'): the standard isotropic-coordinate expressions (machinery right)",
      sp.simplify(pd(Ktt0) - (-Nf_ * d1(Nf_) / Pf_**2).subs(rb, Rbs)) == 0 and sp.simplify(pd(Kth0) - (Rbs * Pf_ * (Pf_ + 2 * Rbs * d1(Pf_))).subs(rb, Rbs)) == 0)
# which quantities can jump: with N, N', psi, psi', H0, H2, K, xi continuous, only N'', psi'', H0', K' can.
jumpers_tt = [s for s in [d2(Nf_), d1(H0f)] if Ktt1.has(s)]; jumpers_th = [s for s in [d2(Pf_), d1(Kf)] if Kth1.has(s)]
check("(0b) delta K_tt carries N'' and H0' (the only discontinuous ingredients); delta K_thth carries psi'' and K'", len(jumpers_tt) == 2 and len(jumpers_th) == 2)
# coefficients: [dK_tt] = 0 <=> [H0'] = -2 xi [N'']/N ;  [dK_thth] = 0 <=> [K'] = 4 xi [psi'']/psi
ctt_N2 = sp.simplify(sp.diff(Ktt1, d2(Nf_))); ctt_H0p = sp.simplify(sp.diff(Ktt1, d1(H0f)))
cth_P2 = sp.simplify(sp.diff(Kth1, d2(Pf_))); cth_Kp = sp.simplify(sp.diff(Kth1, d1(Kf)))
check("(0c) [dK_tt] = 0 reduces to [H0'] = -2 xi [N'']/N", sp.simplify(ctt_N2 / ctt_H0p - (2 * xi / Nf_.subs(rb, Rbs))) == 0)
check("(0d) [dK_thth] = 0 reduces to [K'] = 4 xi [psi'']/psi (the Y_:AB part carries only xi and continuous background: no jump)", sp.simplify(cth_P2 / cth_Kp - (-4 * xi / Pf_.subs(rb, Rbs))) == 0)

# ---------------- (1) exterior static RW solution (3624 equations), transformed to rbar
def rhs(r, y):
    H, Hp, K = y; Hpp = -2 * (r - M) / (r * (r - 2 * M)) * Hp + (6 * r * r - 12 * M * r + 4 * M * M) / (r * r * (r - 2 * M)**2) * H
    return [Hp, Hpp, Hp + 2 * M * H / (r * (r - 2 * M))]
def Kalg(r, H, Hp, Hpp): return (r * r * (r - 2 * M) * Hpp + 2 * r * r * Hp - 2 * r * H + 4 * M * H) / (4 * r)
r0 = 400.0
def sol(kind):
    if kind == "g": H = r0 * (r0 - 2); Hp = 2 * r0 - 2; Hpp = 2.0
    else: H = r0**-3; Hp = -3 * r0**-4; Hpp = 12 * r0**-5
    return solve_ivp(rhs, [r0, R], [H, Hp, Kalg(r0, H, Hp, Hpp)], rtol=1e-13, atol=1e-22, method="DOP853").y[:, -1]
g_ = sol("g"); d_ = sol("d")
print("(1) exterior: growing and decaying static solutions at R = 8M/3")
q_zero = d_[2] / d_[0]; y_zero = R * d_[1] / d_[0]
print(f"    decaying (zero mode): K/H = {q_zero:.5f}, y = {y_zero:.5f};  growing: K/H = {g_[2]/g_[0]:.5f}, y = {R*g_[1]/g_[0]:.5f}")
check("(1a) the pure decaying solution's y = -6.805 IS Hinderer's denominator zero (3647): the pole is the static zero mode", abs(y_zero - (-6.8051)) < 5e-4)
y_grow_exact = (2 * R - 2 * M) / (R - 2 * M)            # H_grow = r(r - 2M) exactly (3624): y = 5 at 8M/3
check("(1b) the exact growing solution H = r(r-2M) has y = 5 = Hinderer's numerator zero (k2 = 0 for a pure tide); the inward-integrated one carries a 1e-3 decaying admixture (harmless: the wall condition fixes the total)", abs(y_grow_exact - 5) < 1e-12 and abs(R * g_[1] / g_[0] - 5) < 5e-3)
lam_r = -g_[2] / d_[2]; y_r = R * (g_[1] + lam_r * d_[1]) / (g_[0] + lam_r * d_[0])
check("(1c) K(R) = 0 (3624's rigid wall) reproduces y = -10.33, k2 = -0.080", abs(y_r + 10.33) < 0.01 and abs(hinderer_k2(y_r) + 0.080) < 0.001)

# ---------------- (2) the register closure at the wall
print("(2) register closure: H0 = 2 N_v chi dv/N, K = -2 chi dv/psi")
Nf = lambda v: (1 - v / 2) / (1 + v / 2); Pf = lambda v: 1 + v / 2
v_in = (M / (2 * Rb)) * (3 - rb**2 / Rb**2); ve_in = 2 * CAP - CAP**2 / v_in; ve_out = M / rb
N_in, P_in, N_out, P_out = Nf(ve_in), Pf(ve_in), Nf(ve_out), Pf(ve_out)
at = lambda e_: float(e_.subs(rb, Rb))
Nv_in = sp.diff(N_in, rb) / sp.diff(ve_in, rb); chi = CAP / v_in
q_closure = at(sp.simplify((-2 * chi / P_in) / (2 * Nv_in * chi / N_in)))
print(f"    K/H0 at the wall = -N/(psi N_v) = {q_closure:.6f}  (N = 1/2, psi = 4/3, N_v = -9/16 -> 2/3 exactly)")
check("(2a) the closure's wall ratio is K/H = 2/3 exactly, chi cancels (any chi > 0), the interior count law does not enter", abs(q_closure - 2 / 3) < 1e-12)
check("(2b) C^1 background: N, N', psi, psi' continuous at the surface (so xi drops out of the induced-metric conditions)",
      all(abs(at(sp.diff(a, rb, k)) - at(sp.diff(b, rb, k))) < 1e-12 for a, b in [(N_in, N_out), (P_in, P_out)] for k in (0, 1)))
jN2 = at(sp.diff(N_out, rb, 2)) - at(sp.diff(N_in, rb, 2)); jP2 = at(sp.diff(P_out, rb, 2)) - at(sp.diff(P_in, rb, 2))
print(f"    second-derivative jumps: [N''] = {jN2:+.5f}, [psi''] = {jP2:+.5f} (the smeared shell's edge)")
check("(2c) N'' and psi'' JUMP at the surface (the background is C^1, not C^2): the extrinsic-curvature conditions see the displacement", abs(jN2) > 0.1 and abs(jP2) > 0.1)

# ---------------- (3) k2 at the closure's wall ratio, and its sensitivity
print("(3) k2 under the closure, and the pole")
def wall(q):
    lam = -(g_[2] - q * g_[0]) / (d_[2] - q * d_[0]); H, Hp, K = g_ + lam * d_; return H, Hp, K, R * Hp / H
H, Hp, K, y_c = wall(2 / 3); k2_c = hinderer_k2(y_c)
print(f"    q = 2/3: y_R = {y_c:.4f}, k2 = {k2_c:+.3f}, Lambda = {(2/3)*k2_c/(3/8)**5:+.0f}   |  zero mode at q = {q_zero:.5f} (0.8% away)")
for q in [0.64, 0.655, 0.66, 0.663, 0.6667, 0.68, 0.70]:
    yy = wall(q)[3]; print(f"      q = {q:.4f}: y_R = {yy:+.4f}, k2 = {hinderer_k2(yy):+.4f}")
check("(3a) the closure's wall condition sits 0.8% from the static zero mode: formal k2 = +7.9 is pole-adjacent", abs(q_closure - q_zero) / q_zero < 0.01 and k2_c > 5)
check("(3b) k2 changes SIGN across q = 0.6615; a 1% shift of the wall ratio (the O(v) dictionary uncertainty at the wall, 3633 §2 found ~30%) flips it: the sign of k2 is NOT determined by the corpus's current static dictionary",
      hinderer_k2(wall(0.655)[3]) < 0 and hinderer_k2(wall(0.68)[3]) > 0)

# ---------------- (4) the displacement and the induced layer
print("(4) the perturbed surface: displacement demanded by the two extrinsic conditions vs the level-set rule")
Nw, Pw = at(N_in), at(P_in)
def law_ii():
    N_n = sp.lambdify(rb, N_in); P_n = sp.lambdify(rb, P_in)
    def rr(x, y):
        h = 1e-6; P = N_n(x) * P_n(x)**2 * x * x
        dP = (N_n(x + h) * P_n(x + h)**2 * (x + h)**2 - N_n(x - h) * P_n(x - h)**2 * (x - h)**2) / (2 * h)
        return [y[1], -(dP * y[1] - 6 * N_n(x) * P_n(x)**2 * y[0]) / P]
    s = solve_ivp(rr, [1e-3, Rb], [1e-6, 2e-3], rtol=1e-11, atol=1e-16, method="DOP853"); return s.y[1, -1] / s.y[0, -1]
s_ii = law_ii(); s_i = 2 / Rb
def junction(q, s):
    Hq, Hqp, Kq, _ = wall(q); Kqp = rhs(R, [Hq, Hqp, Kq])[2]
    f = 1 + s * (rb - Rb); H0i = 2 * Nv_in * chi * f / N_in; Ki = -2 * chi * f / P_in
    ep = Hq / at(H0i); Kres = (ep * at(Ki) - Kq) / Hq
    jH0p = Hqp * 8 / 9 - ep * at(sp.diff(H0i, rb)); jKp = Kqp * 8 / 9 - ep * at(sp.diff(Ki, rb))
    return (-jH0p * Nw / (2 * jN2)) / Hq, (jKp * Pw / (4 * jP2)) / Hq, (-ep / (-4 / 9)) / Hq, Kres
for nm, s in [("(i) flat-lattice harmonic, f'/f = 4/3", s_i), ("(ii) 3643 count law at omega = 0, f'/f = %.4f" % s_ii, s_ii)]:
    a, b, c, kr = junction(2 / 3, s); print(f"    {nm}: xi/H from [dK_tt]=0: {a:+.4f}; from [dK_thth]=0: {b:+.4f}; level-set: {c:+.4f}; [K]/H = {kr:.1e}")
a1, b1, c1, kr1 = junction(2 / 3, s_i); a2, b2, c2, _ = junction(2 / 3, s_ii)
check("(4a) [K] = 0 is automatic once [H0] = 0 (K/H0 = 2/3 inside for any count law)", abs(kr1) < 1e-10)
check("(4b) the two extrinsic conditions demand nearly the same displacement (1%): the closure junction is NEARLY layer-free", abs(a1 - b1) < 0.02 and abs(a2 - b2) < 0.02, f"xi/H = {a1:+.4f} vs {b1:+.4f}")
check("(4c) the residual [xi_tt - xi_thth] = 0.011 H is the SAME for both count laws: no interior law removes it — an induced l = 2 surface layer of that size is the closure's, not the count law's", abs((a1 - b1) - (a2 - b2)) < 1e-4)
check("(4d) the geometry's displacement (xi/H = -1.21) exceeds the level-set rule's (-1.00) by ~20%: under the closure the perturbed surface is NOT the level set v_eff = cap — 3647's argument used the level set", abs(a1 / c1) > 1.15)
q_free = brentq(lambda q: junction(q, s_ii)[0] - junction(q, s_ii)[1], 0.60, 0.66)
print(f"    a fully layer-free junction would need q = {q_free:.4f}, but the closure forces q = 2/3 ([K] would be {junction(q_free, s_ii)[3]:+.3f} H there): no consistent layer-free static junction exists")
check("(4e) the layer-free wall ratio (q = 0.625) is not the closure's (2/3): the register closure + vacuum has no exactly layer-free static junction", abs(q_free - 2 / 3) > 0.02)

print()
print(f"3650 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
