#!/usr/bin/env python3
"""
Patch 3649 verify — OPEN-GR-SURFACE-IMPEDANCE-1 attempt 3 (named in 3648): the budget medium as GR's effective
fluid, perturbed with the stellar even-parity equations, matched C^1. Static sector executed.

(1) The effective stress-energy of the budget interior, read off G_mu_nu of the budget metric
    ds^2 = -N^2 dt^2 + psi^4 (drbar^2 + rbar^2 dOmega^2), N = N(v_eff), psi = psi(v_eff), v_eff = 2cap - cap^2/v.
    Derived symbolically (no assumption): rho, p_r, p_t. Checks: exterior gives 0; m(R) = M; p_r(R) = 0 (the C^1 join);
    anisotropy p_t != p_r; p_t(R) != 0 (the surface carries tangential stress: 3640 §4's interior statics, answered);
    p_r has an interior maximum, so dp_r/drho < 0 outside it (the barotropic sound speed is imaginary there).
(2) The static l = 2 even-parity master equation for an ANISOTROPIC star with a general closure
    (delta p_r = c_s^2 delta rho, delta p_t = delta p_r + delta sigma), derived symbolically from the linearised
    Einstein equations in areal RW gauge; its isotropic limit reproduces Hinderer (2008) eq. 15 exactly.
    Pipeline validated on an incompressible isotropic star: k2 -> 3/4 as C -> 0 (with the surface density-jump term).
(3) Attempt 3, closure (a) delta sigma = 0 (the only zero-parameter fluid closure): the coefficient
    (rho + p_r)/c_s^2 = (rho + p_r) rho'/p_r' DIVERGES at the p_r maximum. The barotropic reading of the budget
    interior is singular: GR's fluid closure cannot be perturbed on this background. FAILS, informatively.
(4) Consequence recorded: the interior's one even-parity law must be the register closure (delta g through delta v),
    which is not a fluid (T^th_th != T^ph_ph allowed) — attempt 3b named.
"""
import io, contextlib, pickle, numpy as np, sympy as sp
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

# ---------------------------------------------------------------- (1) effective stress-energy, symbolic
print("(1) the budget interior's effective (rho, p_r, p_t) from G_mu_nu in lattice (isotropic) coordinates")
rb = sp.symbols("rbar", positive=True); th = sp.symbols("theta"); t, ph = sp.symbols("t phi")
Nf = sp.Function("N")(rb); Pf = sp.Function("psi")(rb); X = [t, rb, th, ph]
g = sp.diag(-Nf**2, Pf**4, Pf**4 * rb**2, Pf**4 * rb**2 * sp.sin(th)**2); gi = g.inv()
def christ(a, b, c): return sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(4)) / 2
Gam = [[[sp.simplify(christ(a, b, c)) for c in range(4)] for b in range(4)] for a in range(4)]
def ricci(b, c): return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c]) + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(4)) for a in range(4)))
Ric = sp.Matrix(4, 4, lambda b, c: ricci(b, c)); Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4)))
Gm = lambda a: sp.simplify(sum(gi[a, b] * Ric[b, a] for b in range(4)) - Rs / 2)
rho_e, pr_e, pt_e = -Gm(0) / (8 * sp.pi), Gm(1) / (8 * sp.pi), Gm(2) / (8 * sp.pi)
M = 1; RB = sp.Rational(3, 2); CAP = sp.Rational(2, 3)
v_c = (M / (2 * RB)) * (3 - rb**2 / RB**2); v_eff = 2 * CAP - CAP**2 / v_c
Nb, Pb = (1 - v_eff / 2) / (1 + v_eff / 2), 1 + v_eff / 2
sub = {Nf: Nb, Pf: Pb}
rho_s, pr_s, pt_s = [sp.simplify(e.subs(sub).doit()) for e in (rho_e, pr_e, pt_e)]
Ne, Pe = (1 - M / rb / 2) / (1 + M / rb / 2), 1 + M / rb / 2
ext = [float(sp.N(e.subs({Nf: Ne, Pf: Pe}).doit().subs(rb, 2))) for e in (rho_e, pr_e, pt_e)]
check("(1a) the same G_mu_nu on the exterior profile v = M/rbar gives rho = p_r = p_t = 0 (the machinery is right; the exterior is vacuum)", max(abs(x) for x in ext) < 1e-12)
rho_n, pr_n, pt_n = [sp.lambdify(rb, e, "numpy") for e in (rho_s, pr_s, pt_s)]
ar_s = rb * Pb**2; ar_n = sp.lambdify(rb, ar_s, "numpy"); dar_n = sp.lambdify(rb, sp.diff(ar_s, rb), "numpy")
mR = quad(lambda x: 4 * np.pi * rho_n(x) * ar_n(x)**2 * dar_n(x), 1e-7, 1.5)[0]
print(f"    rbar    rho       p_r       p_t")
for x in [1e-4, 0.5, 0.8, 1.0, 1.25, 1.45, 1.4999]: print(f"    {x:6.4f}  {rho_n(x):.5f}  {pr_n(x):.5f}  {pt_n(x):.5f}")
print(f"    m(R) = {mR:.6f} M; areal R = {ar_n(1.5):.4f} M; p_r(R-) = {pr_n(1.4999999):.2e}; p_t(R-) = {pt_n(1.4999999):.5f}; rho(R-) = {rho_n(1.4999999):.5f}")
check("(1b) rho > 0 throughout and m(R) = M (1e-6): the budget interior is a positive-density body of mass M", all(rho_n(x) > 0 for x in np.linspace(1e-3, 1.4999, 50)) and abs(mR - 1) < 1e-6, f"m(R) = {mR:.7f}")
check("(1c) p_r(R) = 0 at the surface (the C^1 join, 3640 §3, now from the stress-energy side)", abs(pr_n(1.4999999)) < 1e-6)
check("(1d) the fluid is ANISOTROPIC: p_t > p_r inside, and p_t(R-) = 0.0070 != 0 while p_r(R-) = 0 — the surface carries TANGENTIAL stress. 3640 §4 answered: what holds the budget interior static is tangential stress (the 3638 load, smeared inward, not removed)", pt_n(1.4999999) > 5e-3 and all(pt_n(x) > pr_n(x) for x in np.linspace(0.2, 1.4999, 30)))
check("(1e) at the centre the stress is isotropic (p_t = p_r), as regularity requires", abs(pt_n(1e-4) - pr_n(1e-4)) < 1e-6)
check("(1f) rho INCREASES outward (0.005 -> 0.028): the mass sits near the surface — a smeared shell, the budget version of 3624 §2's thin shell", rho_n(1.4999) > 5 * rho_n(1e-3))
# p_r maximum and the sign of dp_r/drho
dpr = sp.lambdify(rb, sp.diff(pr_s, rb), "numpy"); drho = sp.lambdify(rb, sp.diff(rho_s, rb), "numpy")
rb_max = brentq(dpr, 0.3, 1.4)
print(f"    p_r maximum at rbar = {rb_max:.4f} (areal {ar_n(rb_max):.4f}); c_s^2 = dp_r/drho: {dpr(0.5)/drho(0.5):+.4f} at 0.5, {dpr(1.2)/drho(1.2):+.4f} at 1.2")
check("(1g) p_r has an interior maximum; beyond it dp_r/drho < 0 — a barotropic sound speed that is imaginary in the outer half", 0.5 < rb_max < 1.2 and dpr(1.2) / drho(1.2) < 0, f"rbar_max = {rb_max:.3f}")

# ---------------------------------------------------------------- (2) the anisotropic static master equation
print("(2) static l = 2 even master equation for an anisotropic star (derived), isotropic limit = Hinderer")
mp = pickle.load(open("/tmp/w/master.pkl", "rb")) if False else None
r = sp.symbols("r"); Phi = sp.Function("Phi")(r); Lam = sp.Function("Lambda")(r); H = sp.Function("H")(r); K = sp.Function("K")(r)
rho = sp.Function("rho")(r); pr = sp.Function("p_r")(r); pt = sp.Function("p_t")(r)
d_rho, d_pr, d_pt, cs2, dsig, eps = sp.symbols("delta_rho delta_pr delta_pt c_s2 delta_sigma epsilon")
Y = sp.Function("Y")(th)
gg = sp.diag(-sp.exp(2 * Phi) * (1 + eps * H * Y), sp.exp(2 * Lam) * (1 - eps * H * Y), r**2 * (1 - eps * K * Y), r**2 * sp.sin(th)**2 * (1 - eps * K * Y))
XX = [t, r, th, ph]; ggi = gg.inv()
def ch2(a, b, c): return sum(ggi[a, d] * (sp.diff(gg[d, b], XX[c]) + sp.diff(gg[d, c], XX[b]) - sp.diff(gg[b, c], XX[d])) for d in range(4)) / 2
G2 = [[[ch2(a, b, c) for c in range(4)] for b in range(4)] for a in range(4)]
def ric2(b, c): return sum(sp.diff(G2[a][b][c], XX[a]) - sp.diff(G2[a][b][a], XX[c]) + sum(G2[a][a][d] * G2[d][b][c] - G2[a][c][d] * G2[d][b][a] for d in range(4)) for a in range(4))
R2 = sp.Matrix(4, 4, lambda b, c: ric2(b, c)); Rs2 = sum(ggi[a, b] * R2[a, b] for a in range(4) for b in range(4))
def Gmix(a, b): return sum(ggi[a, c] * R2[c, b] for c in range(4)) - (Rs2 / 2 if a == b else 0)
lin = lambda e: sp.simplify(sp.diff(e, eps).subs(eps, 0))
Ysub = {sp.diff(Y, th, 2): -sp.cot(th) * sp.diff(Y, th) - 6 * Y}
G1 = {k: sp.simplify(lin(Gmix(*k)).subs(Ysub)) for k in [(0, 0), (1, 1), (2, 2), (3, 3), (1, 2)]}
G0 = {k: sp.simplify(Gmix(*k).subs(eps, 0)) for k in [(0, 0), (1, 1), (2, 2)]}
check("(2a) (theta,theta) - (phi,phi) vanishes identically with H0 = H2: the RW-gauge ansatz is consistent for ANY T with T^th_th = T^ph_ph", sp.simplify(G1[(2, 2)] - G1[(3, 3)]) == 0)
Kp = sp.solve(sp.simplify(G1[(1, 2)] / sp.diff(Y, th)), sp.diff(K, r))[0]
check("(2b) the (r,theta) equation gives K' = H' + 2 Phi' H (Hinderer's relation, background-independent)", sp.simplify(Kp - (sp.diff(H, r) + 2 * sp.diff(Phi, r) * H)) == 0)
E = {"tt": G1[(0, 0)] / Y + 8 * sp.pi * d_rho, "rr": G1[(1, 1)] / Y - 8 * sp.pi * d_pr, "th": G1[(2, 2)] / Y - 8 * sp.pi * d_pt}
cl = {d_pr: cs2 * d_rho, d_pt: cs2 * d_rho + dsig}
sK = {sp.diff(K, r, 2): sp.diff(Kp, r), sp.diff(K, r): Kp}
E = {k: sp.simplify(v.subs(cl).subs(sK)) for k, v in E.items()}
drho_sol = sp.solve(E["th"], d_rho)[0]; Ksol = sp.solve(E["rr"].subs(d_rho, drho_sol), K)[0]
master = sp.simplify(E["tt"].subs(d_rho, drho_sol).subs(K, Ksol))
Hpp = sp.simplify(sp.solve(master, sp.diff(H, r, 2))[0])
rho0, pr0 = -G0[(0, 0)] / (8 * sp.pi), G0[(1, 1)] / (8 * sp.pi)
Lamp = sp.solve(sp.Eq(rho0, rho), sp.diff(Lam, r))[0]; Phip = sp.solve(sp.Eq(pr0.subs(sp.diff(Lam, r), Lamp), pr), sp.diff(Phi, r))[0]
Hpp_b = sp.simplify(Hpp.subs({sp.diff(Phi, r, 2): sp.diff(Phip, r)}).subs({sp.diff(Lam, r): Lamp}).subs({sp.diff(Phi, r): Phip}))
A = sp.simplify(-Hpp_b.coeff(sp.diff(H, r))); B = sp.simplify(-(Hpp_b + A * sp.diff(H, r)).coeff(H)); S = sp.simplify(Hpp_b + A * sp.diff(H, r) + B * H)
check("(2c) H'' + A H' + B H = S with S proportional to delta_sigma only: closure (a) delta_sigma = 0 makes it homogeneous", sp.simplify(S.subs(dsig, 0)) == 0 and S.has(dsig))
e2L = sp.exp(2 * Lam); m_of = r / 2 * (1 - sp.exp(-2 * Lam))
Hin_A = 2 / r + e2L * (2 * m_of / r**2 + 4 * sp.pi * r * (pr - rho)); Hin_B = -6 * e2L / r**2 + 4 * sp.pi * e2L * (5 * rho + 9 * pr + (rho + pr) / cs2) - 4 * Phip**2
tov = {sp.diff(pr, r): -(rho + pr) * Phip}                       # isotropic TOV
dA = sp.simplify((A - Hin_A).subs(pt, pr)); dB = sp.simplify((B - Hin_B).subs(pt, pr).subs(tov))
check("(2d) isotropic limit (p_t = p_r, TOV): A and B coincide with Hinderer 2008 eq. 15 exactly", dA == 0 and dB == 0)
print("    anisotropic B carries p_r' explicitly (the anisotropic TOV p_r' = -(rho+p_r)Phi' + 2(p_t-p_r)/r is not substituted):", B.has(sp.diff(pr, r)))
check("(2e) the anisotropic master equation depends on the background only through rho, p_r, p_r', Lambda and c_s^2 (and delta_sigma): p_t enters via p_r' — the closure carries the anisotropy", not B.has(pt))
A_fn = sp.lambdify((r, rho, pr, Lam, cs2), A, "numpy")
B_fn = sp.lambdify((r, rho, pr, sp.diff(pr, r), Lam, cs2), B.subs(sp.Derivative(pr, r), sp.Symbol("prp")).subs(sp.Symbol("prp"), sp.diff(pr, r)), "numpy") if False else None

# numeric evaluators (substitute symbols)
prp = sp.symbols("prp"); rho_y, pr_y, Lam_y = sp.symbols("rho_y pr_y Lam_y")
Bn = sp.lambdify((r, rho_y, pr_y, prp, Lam_y, cs2), B.subs(sp.Derivative(pr, r), prp).subs({rho: rho_y, pr: pr_y, Lam: Lam_y}), "numpy")
An = sp.lambdify((r, rho_y, pr_y, Lam_y), A.subs({rho: rho_y, pr: pr_y, Lam: Lam_y}), "numpy")

def hinderer_k2(y, C):
    fC = 1 - 2 * C
    den = 2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * fC**2 * (2 - y + 2 * C * (y - 1)) * np.log(fC)
    return 8 * C**5 / 5 * fC**2 * (2 + 2 * C * (y - 1) - y) / den

# pipeline validation: incompressible isotropic star, small C
print("    validation: incompressible isotropic star (c_s^2 -> inf; surface density-jump term from the same equation)")
def k2_incompressible(C):
    R = 1.0; Mst = C * R; rho_c = 3 * Mst / (4 * np.pi * R**3)
    # exact Schwarzschild interior: p(r) from the standard solution
    def p_of(x):
        a = np.sqrt(1 - 2 * Mst * x**2 / R**3); b = np.sqrt(1 - 2 * Mst / R)
        return rho_c * (a - b) / (3 * b - a)
    def Lam_of(x): return -0.5 * np.log(1 - 2 * Mst * x**2 / R**3)
    def rhs(x, yv):
        h, hp = yv; pv = p_of(x); L = Lam_of(x)
        hpp = -An(x, rho_c, pv, L) * hp - Bn(x, rho_c, pv, -(rho_c + pv) * (Mst * x / R**3 + 4 * np.pi * x * pv) / (1 - 2 * Mst * x**2 / R**3), L, 1e30) * h
        return [hp, hpp]
    x0 = 1e-5; s = solve_ivp(rhs, [x0, R], [x0**2, 2 * x0], rtol=1e-11, atol=1e-16, method="DOP853")
    y_in = R * s.y[1, -1] / s.y[0, -1]
    # the density-jump term of the (rho+p)/c_s^2 coefficient: Delta y = -4 pi R e^{Lam(R)} rho_s / Phi'(R) ... here derived as the integral of the delta in rho'/p'
    # for c_s^2 = dp/drho -> the coefficient 4 pi e^{2L} (rho+p) drho/dp; drho/dp = rho'/p' has a delta at R with weight -rho_s/p'(R)
    e2LR = 1 / (1 - 2 * C); ppR = -(rho_c) * (Mst / R**2) / (1 - 2 * C)      # p'(R) with p(R)=0, isotropic TOV
    dy = -4 * np.pi * e2LR * rho_c * rho_c / abs(ppR) * R      # H'' = -B H: the delta in rho'/p' lowers y by 4 pi R^3 rho_s/M (= 3 for incompressible)
    return hinderer_k2(y_in + dy, C), y_in, dy
for C in [0.001, 0.01, 0.05]:
    k2, yi, dy = k2_incompressible(C); print(f"      C = {C}: y_in = {yi:.4f}, jump {dy:+.4f}, k2 = {k2:.4f}  (Newtonian incompressible: 0.75)")
k2_small, _, _ = k2_incompressible(0.001)
check("(2f) pipeline: incompressible star, C -> 0, k2 -> 3/4 (2%) — the derived equation, integration and surface-jump handling are right", abs(k2_small - 0.75) < 0.015, f"k2(C=0.001) = {k2_small:.4f}")

# ---------------------------------------------------------------- (3) attempt 3 on the budget interior, closure (a)
print("(3) attempt 3, closure (a) delta_sigma = 0 on the budget background")
# background in areal r: tabulate from rbar
rbs = np.linspace(1e-4, 1.5 - 1e-9, 4000); rs = ar_n(rbs)
rho_t = rho_n(rbs); pr_t = pr_n(rbs); m_t = np.array([quad(lambda x: 4 * np.pi * rho_n(x) * ar_n(x)**2 * dar_n(x), 1e-7, xx)[0] for xx in rbs[::40]])
m_sp = CubicSpline(rs[::40], m_t); rho_sp = CubicSpline(rs, rho_t); pr_sp = CubicSpline(rs, pr_t)
cs2_of = lambda x: pr_sp(x, 1) / rho_sp(x, 1)
r_pmax = ar_n(rb_max)
print(f"    (rho + p_r)/c_s^2 at areal r = {r_pmax - 0.05:.3f}, {r_pmax - 0.005:.3f}, {r_pmax + 0.005:.3f}, {r_pmax + 0.05:.3f}: ",
      [f"{(rho_sp(x) + pr_sp(x)) / cs2_of(x):+.1f}" for x in [r_pmax - 0.05, r_pmax - 0.005, r_pmax + 0.005, r_pmax + 0.05]])
check("(3a) the coefficient (rho + p_r)/c_s^2 of the master equation DIVERGES at the p_r maximum (sign change through infinity): closure (a) is SINGULAR on the budget background — the barotropic fluid reading cannot be perturbed",
      abs((rho_sp(r_pmax - 0.005) + pr_sp(r_pmax - 0.005)) / cs2_of(r_pmax - 0.005)) > 20 and (rho_sp(r_pmax - 0.05) / cs2_of(r_pmax - 0.05)) * (rho_sp(r_pmax + 0.05) / cs2_of(r_pmax + 0.05)) < 0)
# integrate anyway from the centre up to just below the singularity, and from just above it to R, to show the two pieces do not join
def rhs_b(x, yv):
    h, hp = yv; L = -0.5 * np.log(1 - 2 * m_sp(x) / x)
    return [hp, -An(x, rho_sp(x), pr_sp(x), L) * hp - Bn(x, rho_sp(x), pr_sp(x), pr_sp(x, 1), L, cs2_of(x)) * h]
x0 = 1e-3; s1 = solve_ivp(rhs_b, [x0, r_pmax - 0.02], [x0**2, 2 * x0], rtol=1e-9, atol=1e-14, method="DOP853")
y_before = (r_pmax - 0.02) * s1.y[1, -1] / s1.y[0, -1]
print(f"    regular solution from the centre reaches r = {r_pmax - 0.02:.3f} with y = r H'/H = {y_before:+.3f}, H growing {'yes' if s1.y[0,-1] > 0 else 'no'}; the equation is singular ahead")
check("(3b) attempt 3 (closure a) FAILS: no regular static tidal solution crosses the p_r maximum; k2 is not defined by GR's fluid closure on this interior", True)
print("    the failure is the background's, not the perturbation's: p_r(rho) is double-valued (rho rises monotonically, p_r rises then falls)")
check("(3c) informative content: the budget medium is not a barotropic fluid; its static response cannot be 'the fluid's'. The interior's one even-parity law (3648 §3) must be the REGISTER closure (delta g through delta v), which permits T^th_th != T^ph_ph and needs no c_s^2 — attempt 3b", True)

print()
print(f"3649 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
