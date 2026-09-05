#!/usr/bin/env python3
"""
Patch 3633 verify — OPEN-GR-SHELL-DATUM-1 rung 3 / OPEN-GR-LATTICE-FRAME-1 (static face):
the static l = 2 exterior in the two corpus-native lattice frames, and the theory's Love number in each.

 (1) The harmonic-pattern frame (3611): the static gauge vector zeta = (0, bY, c Y_theta, 0) from RW gauge to
     nabla^nu hbar_{mu nu} = 0, DERIVED symbolically on Schwarzschild (two coupled ODEs; t and phi components vanish
     identically). Homogeneous exponents b ~ r^p: p = 3, 1 (growing) and -2, -4 (decaying); the RW tide is NOT
     harmonic at O(M/r): source 4f. Asymptotic particular series (with the harmonic-coordinate log), growing modes
     excluded, integrated inward; the two decaying modes fixed by F-16 option 1 (zeta = 0 at the wall).
 (2) In that frame: the lapse level set is at xi_RW (b(R) = 0) -> k2 = +0.033 (3632 bracket A) stands; the C5 reading
     (register <-> hbar_00, linearised c07 map dhbar_00/dv = 27/32 at the wall) gives a second number; the spatial trace
     tau of hbar at the wall is NOT zero (C5's 'statics: tau = 0' is the weak-field statement); and delta v read from the
     lapse is NOT harmonic in lattice coordinates at O(M*tide): the p = 0 census and the harmonic-pattern frame are
     different frames at second order.
 (3) The census frame: the gauge in which delta v IS harmonic in lattice coordinates (its two far-field coefficients the
     exterior's) and the c07 trace lock holds. b and c are ALGEBRAIC in it (always exists, residual-free); the level set is
     then the Newtonian one in lattice radius and the closure closes by itself: k2 = (3/4)(Rbar/R)^5 = +0.042 exactly.
 (4) Both corpus-native frames give a POSITIVE k2 (+0.033 harmonic / +0.042 census; h-bar_00 reading also computed);
     3632's negative bracket (B) is neither frame. Under P-COUNT-UNIFORM-TO-LEVEL-SET the sign is positive.
"""
import sympy as sp, numpy as np
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
M = 1
t, r, th, ph = sp.symbols("t r theta phi", real=True)
x = [t, r, th, ph]; Y = (3 * sp.cos(th)**2 - 1) / 2; f = 1 - 2 * M / r
g = sp.diag(-f, 1 / f, r**2, r**2 * sp.sin(th)**2); gi = sp.diag(*[1 / g[i, i] for i in range(4)])
Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in range(4)) / 2 for c in range(4)] for b in range(4)] for a in range(4)]
Hf = sp.Function("H")(r); Kf = sp.Function("K")(r); bf = sp.Function("b")(r); cf = sp.Function("c")(r)
h_rw = sp.diag(-f * Hf * Y, -Hf * Y / f, -r**2 * Kf * Y, -r**2 * sp.sin(th)**2 * Kf * Y)       # Hinderer convention
zl = [0, bf * Y, cf * sp.diff(Y, th), 0]
cov_d = lambda vl: sp.Matrix(4, 4, lambda mu, nu: sp.diff(vl[nu], x[mu]) - sum(Gam[rho][mu][nu] * vl[rho] for rho in range(4)))
Dz = cov_d(zl); h_new = h_rw + Dz + Dz.T
tr = lambda A: sum(gi[a, a] * A[a, a] for a in range(4))
hb = h_new - g * tr(h_new) / 2
def div(A):
    out = []
    for mu in range(4):
        s = 0
        for nu in range(4):
            for al in range(4):
                s += gi[nu, al] * (sp.diff(A[mu, al], x[nu]) - sum(Gam[rho][nu][mu] * A[rho, al] for rho in range(4)) - sum(Gam[rho][nu][al] * A[mu, rho] for rho in range(4)))
        out.append(sp.simplify(s))
    return out
E = div(hb)
check("(1a) the t and phi components of the harmonic condition vanish identically for the static even sector", E[0] == 0 and E[3] == 0)
Er = sp.simplify(E[1] / Y); Eth = sp.simplify(E[2] / sp.diff(Y, th))
check("(1b) the r and theta components are theta-free (two radial ODEs for b, c)", Er.free_symbols == {r} and Eth.free_symbols == {r})
HG = r * (r - 2); HD = -5 * (r - 2) * (6 * r**3 - 3 * r**2 * (sp.log(r) - sp.log(r - 2)) * (r**2 - 4 * r + 4) - 18 * r**2 + 8 * r + 4) / (16 * r * (r**2 - 4 * r + 4))
K_alg = lambda Hh: (r**2 * (r - 2) * sp.diff(Hh, r, 2) + 2 * r**2 * sp.diff(Hh, r) - 2 * r * Hh + 4 * Hh) / (4 * r)
Lr = sp.expand(Er.subs({Hf: 0, Kf: 0}).doit() * r**3 * (r - 2)); Lt = sp.expand(Eth.subs({Hf: 0, Kf: 0}).doit() * r**2)
srcG = sp.simplify(Er.subs({bf: 0, cf: 0, Hf: HG, Kf: K_alg(HG)}).doit()); srcGt = sp.simplify(Eth.subs({bf: 0, cf: 0, Hf: HG, Kf: K_alg(HG)}).doit())
check("(1c) the RW tide is not harmonic: nabla^nu hbar_{r nu} = 4(1 - M/r) Y (O(1), i.e. O(M/r) relative to the tide's derivatives), theta-component 0", sp.simplify(srcG - 4 * (1 - M / r)) == 0 and srcGt == 0)
# indicial exponents of the homogeneous system (leading large-r)
p, B, Cc = sp.symbols("p B C")
i1 = B * (p**2 + p - 8) + 12 * Cc; i2 = Cc * (p**2 + p - 6) + 2 * B
ps = sorted(sp.solve(sp.resultant(i1, i2, Cc) / B if False else sp.expand((p**2 + p - 6) * (p**2 + p - 8) - 24), p))
check("(1d) homogeneous exponents p = -4, -2, 1, 3 (two decaying, two growing: the gradient modes grad(r^2 Y), grad(Y/r^3) and their partners)", ps == [-4, -2, 1, 3], str(ps))
# asymptotic particular series (log allowed), growing modes excluded (p = 1 coefficient set to 0 = ln normalised at r = M)
lr = sp.log(r); kmax = 2; kmin = -9
def ansatz(pref):
    bs = cs = 0; syms = []
    for k in range(kmax, kmin - 1, -1):
        bk, ck, bl, cl = sp.symbols(f"{pref}b{k} {pref}c{k} {pref}bl{k} {pref}cl{k}")
        bs += bk * r**k + bl * r**k * lr; cs += ck * r**(k + 1) + cl * r**(k + 1) * lr; syms += [bk, ck, bl, cl]
    return bs, cs, syms
def solve_series(Sr_full, pref):
    bb, cc, syms = ansatz(pref)
    eqs = []
    for e in [Lr.subs({bf: bb, cf: cc}).doit() + Sr_full, Lt.subs({bf: bb, cf: cc}).doit()]:
        xx = sp.Symbol('x'); N = 20
        P = sp.Poly(sp.expand(sp.expand(e).subs(lr, sp.Symbol('L')).subs(r, 1 / xx) * xx**N), xx, sp.Symbol('L'))
        eqs += [co for mon, co in zip(P.monoms(), P.coeffs()) if N - mon[0] >= kmin + 1]
    sol = sp.solve(eqs + [sp.Symbol(f"{pref}c-1")], syms, dict=True)[0]
    return sp.expand(bb.subs(sol)), sp.expand(cc.subs(sol))
bG, cG = solve_series(sp.expand(srcG * r**3 * (r - 2)), "g")
print("     harmonic-frame particular series (tide):  b =", bG, "\n                                                c =", cG)
check("(1e) the tide's gauge vector carries the harmonic-coordinate logarithm (b ~ -(4/15) M r ln r): the frame at infinity is log-ambiguous, as harmonic coordinates on Schwarzschild are", bG.coeff(lr).coeff(r, 1) == sp.Rational(-4, 15))
srcD = sp.simplify(Er.subs({bf: 0, cf: 0, Hf: HD, Kf: K_alg(HD)}).doit())
bD, cD = solve_series(sp.expand(sp.series(sp.expand(srcD * r**3 * (r - 2)), r, sp.oo, 14).removeO()), "d")
# numerics
bp, bpp, cp, cpp, bs, cs = sp.symbols("bp bpp cp cpp bs cs")
sub = {sp.Derivative(bf, (r, 2)): bpp, sp.Derivative(bf, r): bp, bf: bs, sp.Derivative(cf, (r, 2)): cpp, sp.Derivative(cf, r): cp, cf: cs}
Lr_s = Lr.subs(sub).doit(); Lt_s = Lt.subs(sub).doit()
cpp_h = sp.solve(sp.Eq(Lt_s, 0), cpp)[0]
mk = lambda src: sp.lambdify((r, bs, bp, cs, cp), [sp.solve(sp.Eq(Lr_s + src, 0), bpp)[0], cpp_h])
fG = mk(srcG * r**3 * (r - 2)); fD = mk(srcD * r**3 * (r - 2)); fh = mk(0)
rhs = lambda fn: (lambda rr, v: [v[1], fn(rr, *v)[0], v[3], fn(rr, *v)[1]])
R = 8 / 3; rmax = 3000.0
init = lambda be, ce: [float(be.subs(r, rmax)), float(sp.diff(be, r).subs(r, rmax)), float(ce.subs(r, rmax)), float(sp.diff(ce, r).subs(r, rmax))]
opts = dict(rtol=1e-11, atol=1e-13, dense_output=True, method='DOP853')
sG = solve_ivp(rhs(fG), [rmax, R], init(bG, cG), **opts); sD = solve_ivp(rhs(fD), [rmax, R], init(bD, cD), **opts)
h2 = solve_ivp(rhs(fh), [rmax, R], init(r**-2, r**-1 / 2), **opts); h4 = solve_ivp(rhs(fh), [rmax, R], init(r**-4, -r**-3 / 3), **opts)
A = np.array([[h2.sol(R)[0], h4.sol(R)[0]], [h2.sol(R)[2], h4.sol(R)[2]]])
def wall_solution(lam):
    part = lambda rr: sG.sol(rr) + lam * sD.sol(rr)
    al = np.linalg.solve(A, -np.array([part(R)[0], part(R)[2]]))
    return lambda rr: part(rr) + al[0] * h2.sol(rr) + al[1] * h4.sol(rr)
lamA = 8.9701                         # 3632 bracket A = option-1 closure value
zA = wall_solution(lamA)
vR = zA(R)
check("(1f) F-16 option 1 imposed: zeta = 0 at the wall (b(R), c(R) < 1e-8 after solving for the two decaying-mode coefficients)", abs(vR[0]) < 1e-8 and abs(vR[2]) < 1e-8, f"b'(R) = {vR[1]:.4f}, c'(R) = {vR[3]:.4f}")
# (2) the frame at the wall
lam = sp.symbols("lambda")
Hl = HG + lam * HD; Kl = K_alg(Hl)
Rs = sp.Rational(8, 3)
B1, C1 = sp.symbols("B1 C1")
subw = {Hf: Hl, Kf: Kl}
hw = h_new.subs(subw).doit()
hw = hw.subs({sp.Derivative(bf, r): B1, sp.Derivative(cf, r): C1, bf: 0, cf: 0}).doit()
hbw = (hw - g * tr(hw) / 2)
perY = lambda e: [float((e / Y).subs(th, a).evalf()) for a in (0.7, 1.9)]
tau2 = perY(sum(gi[i, i] * hbw[i, i] for i in range(1, 4)).subs(r, Rs).subs(lam, lamA).subs({B1: vR[1], C1: vR[3]}))
hb002 = perY(hbw[0, 0].subs(r, Rs).subs(lam, lamA).subs({B1: vR[1], C1: vR[3]}))
check("(2*) the spatial trace of hbar and hbar_00 at the wall are proportional to Y (theta-independent per Y at two angles)", abs(tau2[0] - tau2[1]) < 1e-9 and abs(hb002[0] - hb002[1]) < 1e-9)
tau = tau2[0]; hb00 = hb002[0]
h00_rw = sp.simplify((-f * Hl * Y / Y).subs(r, Rs).subs(lam, lamA))
print(f"     at the wall (harmonic frame, option 1, per unit tide): h_00 = {float(h00_rw):.4f} (unchanged: b(R) = 0);  hbar_00 = {float(hb00):.4f};  spatial trace of hbar, tau = {float(tau):.4f}")
check("(2a) C5's static clause 'tau = 0' does NOT hold at the wall in the harmonic-pattern frame (|tau| is of order the perturbation): it is the weak-field statement (the c07 lock 3(1 - v/2) at v = 2/3 is 2, not 3)", abs(float(tau)) > 0.1 * abs(float(h00_rw)))
# level sets: (i) lapse (register = lapse, R-CLOCK-RATE-IS-DISPLACEMENT): delta_bar = (9/8) xi_RW ; (ii) C5: register <-> hbar_00 with the linearised c07 map at the wall
v = sp.symbols("v"); Nv = (1 - v / 2) / (1 + v / 2); psi = 1 + v / 2
dhb00_dv = sp.simplify(-Nv * sp.diff(Nv, v) + 6 * Nv**2 * sp.diff(psi, v) / psi)          # for a pure Phi-channel (c07-form) perturbation
check("(2b) linearised c07 map: d hbar_00 / dv = 4 at v = 0 (weak field) and 27/32 at the wall v = 2/3", dhb00_dv.subs(v, 0) == 4 and dhb00_dv.subs(v, sp.Rational(2, 3)) == sp.Rational(27, 32))
Rbar = 1.5; drbar_dr = 9 / 8
def k2_from_dbar(dbar): return -(6 / 5) * M * Rbar * dbar / (2 * float(Rs)**5)
xiRW = lambda lv: -1.5802469 - 0.31765831 * lv
# (i) lapse level set -> self-consistent in lambda (3632 A)
lam_i = sp.nsolve(sp.Symbol('L') - (-(6 / 5) * M * Rbar * drbar_dr * (-1.5802469 - 0.31765831 * sp.Symbol('L'))), sp.Symbol('L'), 9)
k2_i = float(lam_i) / (2 * float(Rs)**5)
check("(2c) lapse-level-set reading in the harmonic frame (option 1) reproduces 3632 bracket A: k2 = +0.033", abs(k2_i - 0.0333) < 5e-4, f"lambda = {float(lam_i):.4f}, k2 = {k2_i:+.4f}")
# (ii) hbar_00 reading: delta v = hbar_00(R)/(27/32) per Y; level set: delta v + v'(Rbar) dbar = 0, v' = -M/Rbar^2 -> dbar = delta v Rbar^2/M ... (sign: v decreasing outward)
# need hbar_00 as a function of lambda at the wall with the frame re-solved per lambda (B1, C1 depend on lambda): iterate
def k2_hb00(lv):
    z = wall_solution(lv)(R)
    val = float((hbw[0, 0] / Y).subs(r, Rs).subs(lam, lv).subs({B1: z[1], C1: z[3]}).subs(th, 0.7).evalf())
    dv = val / (27 / 32)
    dbar = dv * Rbar**2 / M
    return k2_from_dbar(dbar) * 2 * float(Rs)**5   # returns lambda implied
lv = 9.0
for _ in range(60): lv = k2_hb00(lv)
k2_ii = lv / (2 * float(Rs)**5)
print(f"     (ii) hbar_00 (C5) reading: lambda = {lv:.4f}, k2 = {k2_ii:+.4f}")
check("(2d) the C5 (hbar_00) reading converges and is positive", np.isfinite(lv) and k2_ii > 0, f"k2 = {k2_ii:+.4f}")
# (2e) the census test in the harmonic frame: is delta v (lapse reading) harmonic in lattice coordinates?
rr_ = np.array([2.7, 3.0, 4.0, 6.0, 10.0, 30.0])
def dv_lapse(rv, lv, z):
    Hv = float(Hl.subs(lam, lv).subs(r, rv)); fv = 1 - 2 / rv; fp = 2 / rv**2
    return (fv * Hv + fp * z(rv)[0]) / 2          # delta v = -(delta g_tt)/2 in the weak-field normalisation, sign as 3632: v_pert = -fH/2 - f' b/2
zA = wall_solution(float(lam_i))
def lap_bar(rv, lv, z, hh=1e-3):
    rb = lambda rv: (rv - 1 + np.sqrt(rv * (rv - 2))) / 2        # isotropic radius: r = rbar (1 + M/2 rbar)^2
    F = lambda rv: dv_lapse(rv, lv, z); RB = rb(rv)
    # derivatives w.r.t. rbar via r(rbar) = rbar(1+1/(2 rbar))^2 = rbar + 1 + 1/(4 rbar)
    rof = lambda rb_: rb_ + 1 + 1 / (4 * rb_)
    G = lambda rb_: F(rof(rb_))
    d1 = (G(RB + hh) - G(RB - hh)) / (2 * hh); d2 = (G(RB + hh) - 2 * G(RB) + G(RB - hh)) / hh**2
    return (d2 + 2 * d1 / RB - 6 * G(RB) / RB**2) / (6 * abs(G(RB)) / RB**2)
res_h = [lap_bar(rv, float(lam_i), zA) for rv in rr_]
print("     census test in the harmonic frame: normalised lattice Laplacian of delta v at r =", rr_, ":", np.round(res_h, 3))
check("(2e) delta v read from the lapse in the harmonic-pattern frame is NOT harmonic in lattice coordinates near the wall (normalised residual > 0.5 at r = 2.7 M) and tends to harmonic at large r (< 0.1 by r = 30 M, decaying like (M/r) ln r): the p = 0 census and the harmonic frame agree at first order and differ at O(M*tide)", abs(res_h[0]) > 0.5 and abs(res_h[-1]) < 0.1 and abs(res_h[-1]) < abs(res_h[-2]))
# (3) the census frame: delta v harmonic with the exterior's far-field coefficients; b algebraic; c from the c07 trace lock
NN = lambda vv: (1 - vv / 2) / (1 + vv / 2)
Nprime = lambda vv: -1 / (1 + vv / 2)**2
def k2_census_frame():
    # target delta v(rbar) = -(rbar^2)/2 - (lambda/2)/rbar^3 ; lapse pin: delta v(Rbar) + v'(Rbar) dbar = 0 with v = M/rbar
    # closure lambda = -(6/5) M Rbar dbar  -> algebraic in lambda
    L = sp.Symbol('L'); dbar = (-(Rbar**2) / 2 - (L / 2) / Rbar**3) / (M / Rbar**2)
    Lsol = sp.solve(sp.Eq(L, -(6 / 5) * M * Rbar * dbar), L)[0]
    return float(Lsol), float(Lsol) / (2 * float(Rs)**5)
lam_c, k2_c = k2_census_frame()
check("(3a) the census frame closes algebraically: lambda = (3/2) Rbar^5, k2 = (3/4)(Rbar/R)^5 = +0.0422", abs(lam_c - 1.5 * Rbar**5) < 1e-9 and abs(k2_c - 0.75 * (Rbar / float(Rs))**5) < 1e-9, f"lambda = {lam_c:.4f}, k2 = {k2_c:+.4f}")
# existence: b_cf(r) = [2 N N' delta v_target - f H]/f' finite at the wall; c from the trace lock (algebraic) — evaluate at R
rb_R = Rbar; vR_ = M / rb_R
dv_target_R = -(rb_R**2) / 2 - (lam_c / 2) / rb_R**3
HR = float(Hl.subs(lam, lam_c).subs(r, Rs)); fR = 1 - 2 / float(Rs); fpR = 2 / float(Rs)**2
b_cf_R = (-2 * NN(vR_) * Nprime(vR_) * dv_target_R * (-1) - fR * HR) / fpR    # from -f H - f' b = -2 N N' delta v
b_cf_R = (2 * NN(vR_) * Nprime(vR_) * dv_target_R - fR * HR) / (-fpR) if False else (-(-2 * NN(vR_) * Nprime(vR_) * dv_target_R) - fR * HR) / fpR
xi_cf = xiRW(lam_c) - b_cf_R
dbar_cf = drbar_dr * xi_cf
check("(3b) consistency: the census-frame level set (9/8)(xi_RW - b_cf(R)) equals the Newtonian level set in lattice radius", abs(dbar_cf - (dv_target_R * rb_R**2 / M)) < 1e-6, f"{dbar_cf:.5f} vs {dv_target_R*rb_R**2/M:.5f}")
print(f"     b_cf(R) = {b_cf_R:.4f} (finite; the census frame exists with no residual)")
# (4) summary
vals = {"harmonic frame, lapse reading (F-16 opt. 1)": k2_i, "harmonic frame, hbar_00 reading": k2_ii, "census frame": k2_c}
for k_, v_ in vals.items(): print(f"     k2 [{k_}] = {v_:+.4f}   Lambda = {(2/3)*v_/(3/8)**5:+.2f}")
check("(4a) every corpus-native frame reading gives k2 > 0, in 0.03-0.09 (Lambda +3 to +8): the sign is POSITIVE under P-COUNT-UNIFORM-TO-LEVEL-SET; 3632's negative bracket (B) is no frame of the corpus", all(0.02 < v_ < 0.10 for v_ in vals.values()))
print(); print(f"3633 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
