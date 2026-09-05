#!/usr/bin/env python3
"""
Patch 3631 verify — OPEN-GR-SHELL-DATUM-1: Israel's second junction condition written out for
the static l = 2 tide on the R-core (flat interior at cap, lapse 1/2 uniform; exterior
Schwarzschild in RW gauge, Hinderer's convention g_tt = -f(1+HY), g_rr = (1-HY)/f,
g_ang = r^2 (1-KY); surface = the level set of the register).

 (1) Background: the shell's stress from [K^a_b] — sigma = 1/(8 pi R), P = sigma/4 at R = 8M/3;
     4 pi R^2 sigma = 4M/3 (3624's bookkeeping) — the Israel machinery checked on the known case.
 (2) The exterior, from the linearised Einstein equations (no recall): (r,theta) gives K';
     (theta,theta) with K' eliminated gives 3624's algebraic K; (tt) with K eliminated IS the
     master ODE; the growing solution H_G = r(r-2M) (K_G = r^2 - 2M^2) and the decaying solution
     H_D in CLOSED FORM by reduction of order (no numerical integration, no cancellation).
 (3) The first junction, done properly: the lapse pin (level set) fixes the exterior displacement
     xi = -f H / f'; the areal-radius match DEFINES the interior displacement xi_in = xi - R K/2.
     It does NOT constrain K(R). 3624's K(R) = 0 was the extra assumption xi_in = xi.
 (4) The second junction: (delta sigma, delta P, Pi) — the shell's isotropic and shear stress
     response — from the perturbed extrinsic-curvature jump, affine in the one free exterior
     coefficient lambda (the decaying amplitude = the Love number).
 (5) Shell conservation with the lapse pinned: delta P = 2 Pi / R^2, an identity in lambda that
     holds only with the exterior field equations imposed (Bianchi). Corollary: a shell with no
     shear (Pi = 0) has delta P = 0 but delta sigma != 0 — a barotropic fluid shell cannot sit
     statically in the tide. The R-core's surface must carry shear stress.
 (6) The family: k2 for each candidate closure — black hole (lambda = 0); K(R) = 0 (3624: y = -31/3,
     k2 = -0.080); delta sigma = 0 (count per proper area fixed at cap); delta r_areal = 0 (surface
     intrinsically rigid); Pi = 0 = delta P (no shear). One closure = one Love number; the
     register has to name one — that is the datum, now written in the register's own variables.
"""
import numpy as np, sympy as sp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

M = 1
Rn = sp.Rational(8, 3)
r, th, ph, t, eps, xi, xin = sp.symbols("r theta phi t epsilon xi xi_in", real=True)
Rs = sp.symbols("R", positive=True)
Y = (3 * sp.cos(th)**2 - 1) / 2                      # P_2(cos theta), m = 0
f = 1 - 2 * M / r
x4 = [t, r, th, ph]

# ---------- (2) exterior from the field equations ----------
def ricci_lin(g):
    """first-order-in-eps Ricci components of a diagonal metric g(t, r, theta, phi)."""
    n = 4; ginv = sp.diag(*[1 / g[i, i] for i in range(4)])
    G = [[[(ginv[a, a] * (sp.diff(g[a, b], x4[c]) + sp.diff(g[a, c], x4[b]) - sp.diff(g[b, c], x4[a]))) / 2
           for c in range(n)] for b in range(n)] for a in range(n)]
    out = {}
    for (b, c) in [(0, 0), (1, 1), (2, 2), (3, 3), (1, 2)]:
        e = sum(sp.diff(G[a][b][c], x4[a]) - sp.diff(G[a][b][a], x4[c])
                + sum(G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a] for d in range(n)) for a in range(n))
        out[(b, c)] = sp.simplify(sp.diff(e, eps).subs(eps, 0))
    return out
Hf = sp.Function("H")(r); Kf = sp.Function("K")(r)
metric = lambda H, K: sp.diag(-f * (1 + eps * H * Y), (1 - eps * H * Y) / f, r**2 * (1 - eps * K * Y), r**2 * sp.sin(th)**2 * (1 - eps * K * Y))
Ric = ricci_lin(metric(Hf, Kf))
check("(2a) (theta,theta) - (phi,phi)/sin^2 vanishes identically: H0 = H2 = H is consistent", sp.simplify(Ric[(2, 2)] - Ric[(3, 3)] / sp.sin(th)**2) == 0)
Kp_rel = sp.simplify(sp.solve(sp.Eq(Ric[(1, 2)], 0), sp.Derivative(Kf, r))[0])
check("(2b) (r,theta): K' = H' + 2MH/(r(r-2M))  [3624]", sp.simplify(Kp_rel - (sp.diff(Hf, r) + 2 * M * Hf / (r * (r - 2 * M)))) == 0)
Kpp_rel = sp.diff(Kp_rel, r)
thth = Ric[(2, 2)].subs(sp.Derivative(Kf, (r, 2)), Kpp_rel).subs(sp.Derivative(Kf, r), Kp_rel)
K_alg = sp.simplify(sp.solve(sp.Eq(thth, 0), Kf)[0])
K_3624 = (r**2 * (r - 2 * M) * sp.diff(Hf, r, 2) + 2 * r**2 * sp.diff(Hf, r) - 2 * r * Hf + 4 * M * Hf) / (4 * r)
check("(2c) (theta,theta) with K' eliminated: 4rK = r^2(r-2M)H'' + 2r^2 H' - 2rH + 4MH  [3624's algebraic K]", sp.simplify(K_alg - K_3624) == 0)
master = sp.diff(Hf, r, 2) + 2 * (r - M) / (r * (r - 2 * M)) * sp.diff(Hf, r) - (6 * r**2 - 12 * M * r + 4 * M**2) / (r**2 * (r - 2 * M)**2) * Hf
tt = Ric[(0, 0)].subs(sp.Derivative(Kf, (r, 2)), Kpp_rel).subs(sp.Derivative(Kf, r), Kp_rel).subs(Kf, K_alg).doit()
ratio = sp.simplify(tt / master)
check("(2d) (tt) with K eliminated IS the master ODE (ratio H-independent)", not (ratio.free_symbols & {Hf}) and ratio.atoms(sp.Derivative) == set(), str(ratio))
HG = r * (r - 2 * M)
HD = sp.simplify(HG * sp.integrate(1 / HG**3, r))                  # reduction of order, W = 1/H_G
HD = sp.simplify(HD - sp.limit(HD / HG, r, sp.oo) * HG)
HD = sp.simplify(HD / sp.limit(r**3 * HD, r, sp.oo))
check("(2e) H_G = r(r-2M) solves the master ODE; K_G = r^2 - 2M^2", sp.simplify(master.subs(Hf, HG).doit()) == 0 and sp.simplify(K_alg.subs(Hf, HG).doit() - (r**2 - 2 * M**2)) == 0)
check("(2f) closed-form H_D solves the master ODE, r^3 H_D -> 1, no growing admixture", sp.simplify(master.subs(Hf, HD).doit()) == 0 and sp.limit(r**3 * HD, r, sp.oo) == 1 and sp.limit(HD / HG, r, sp.oo) == 0)
print("     H_D(r) =", HD)

# ---------- extrinsic curvature of r = R + eps*disp*Y on either side (surface data as symbols) ----------
H0, H1, H2, K0, K1, K2 = sp.symbols("H0 H1 H2 K0 K1 K2")
Hp = H0 + H1 * (r - Rs) + H2 * (r - Rs)**2 / 2
Kp = K0 + K1 * (r - Rs) + K2 * (r - Rs)**2 / 2
def side(g, disp):
    n = 4; ginv = sp.diag(*[1 / g[i, i] for i in range(4)])
    G = [[[(ginv[a, a] * (sp.diff(g[a, b], x4[c]) + sp.diff(g[a, c], x4[b]) - sp.diff(g[b, c], x4[a]))) / 2
           for c in range(n)] for b in range(n)] for a in range(n)]
    Phi = r - Rs - eps * disp * Y
    dPhi = [sp.diff(Phi, v) for v in x4]
    nlow = [d / sp.sqrt(sum(ginv[a, a] * dPhi[a]**2 for a in range(n))) for d in dPhi]   # outward unit normal
    ys = [t, th, ph]; X = [t, Rs + eps * disp * Y, th, ph]
    E = [[sp.diff(X[mu], ya) for mu in range(n)] for ya in ys]
    Dn = [[sp.diff(nlow[nu], x4[mu]) - sum(G[rho][mu][nu] * nlow[rho] for rho in range(n)) for nu in range(n)] for mu in range(n)]
    on = lambda e: e.subs(r, Rs + eps * disp * Y)
    lin = lambda e: (sp.simplify(e.subs(eps, 0)), sp.simplify(sp.diff(e, eps).subs(eps, 0)))
    K0m = sp.zeros(3, 3); K1m = sp.zeros(3, 3); g0 = sp.zeros(3, 3); g1 = sp.zeros(3, 3)
    for a in range(3):
        for b in range(3):
            K0m[a, b], K1m[a, b] = lin(on(sum(E[a][mu] * E[b][nu] * Dn[mu][nu] for mu in range(n) for nu in range(n))))
            g0[a, b], g1[a, b] = lin(on(sum(E[a][mu] * E[b][nu] * g[mu, nu] for mu in range(n) for nu in range(n))))
    gi = g0.inv()
    return gi * K0m, (gi * K1m - gi * g1 * gi * K0m).applyfunc(sp.simplify), g0, g1     # mixed K^a_b to O(eps)
Ke0, Ke1, ge0, ge1 = side(metric(Hp, Kp), xi)
g_int = sp.diag(-sp.Rational(1, 4), 1, r**2, r**2 * sp.sin(th)**2)                     # flat at cap, lapse 1/2 uniform
Ki0, Ki1, gi0, gi1 = side(g_int, xin)

# ---------- (1) background ----------
fR = 1 - 2 * M / Rs; fpR = sp.diff(f, r).subs(r, Rs)
tr = lambda Km: Km[0, 0] + Km[1, 1] + Km[2, 2]
S0 = -((Ke0 - Ki0) - sp.eye(3) * tr(Ke0 - Ki0)) / (8 * sp.pi)         # Israel: S^a_b = -([K^a_b] - delta [K])/8pi
sigma0 = sp.simplify(-S0[0, 0]); P0 = sp.simplify(S0[1, 1])
check("(1a) background sigma = (1 - sqrt f)/(4 pi R) (thin shell around M, flat inside)", sp.simplify(sigma0 - (1 - sp.sqrt(fR)) / (4 * sp.pi * Rs)) == 0)
sig_R = sp.simplify(sigma0.subs(Rs, Rn)); P_R = sp.simplify(P0.subs(Rs, Rn))
check("(1b) at R = 8M/3: sigma = 1/(8 pi R), P = sigma/4, isotropic", sig_R == 1 / (8 * sp.pi * Rn) and P_R == sig_R / 4 and sp.simplify(S0[1, 1] - S0[2, 2]) == 0, f"sigma = {sig_R}, P = {P_R}")
check("(1c) 4 pi R^2 sigma = 4M/3 (GR's rest mass of the count at cap; 3624)", sp.simplify(4 * sp.pi * Rn**2 * sig_R) == sp.Rational(4, 3))

# ---------- (3) first junction ----------
c_tt = sp.simplify((ge1[0, 0] - gi1[0, 0]) / Y); c_th = sp.simplify((ge1[1, 1] - gi1[1, 1]) / Y)
check("(3a) g_tt continuity = the lapse pin: xi f'(R) + f(R) H(R) = 0 (the level set; 3624 §2)", sp.simplify(c_tt / (xi * fpR + fR * H0)).free_symbols <= {Rs})
xin_from = sp.solve(sp.Eq(c_th, 0), xin)[0]
check("(3b) g_thth continuity DEFINES xi_in = xi - R K(R)/2 — it does NOT constrain K(R)", sp.simplify(xin_from - (xi - Rs * K0 / 2)) == 0)
print("     => 3624's K(R) = 0 is the assumption xi_in = xi (equal coordinate displacements on the two sides), not a consequence of the first junction.")
xi_sol = -fR * H0 / fpR; xin_sol = xin_from.subs(xi, xi_sol)

# ---------- (4) second junction ----------
S1 = -((Ke1 - Ki1) - sp.eye(3) * tr(Ke1 - Ki1)) / (8 * sp.pi)
S1 = S1.applyfunc(lambda e: sp.simplify(e.subs({xi: xi_sol, xin: xin_sol})))
dsigma = sp.simplify(-S1[0, 0] / Y)
dP = sp.simplify((S1[1, 1] + S1[2, 2]) / 2 / Y)
Pi = sp.simplify((S1[1, 1] - S1[2, 2]) / (3 * sp.sin(th)**2) * Rs**2)   # S^th_th - S^ph_ph = Pi (Y'' - cot Y')/R^2 = 3 Pi sin^2/R^2
check("(4a) delta sigma, delta P, Pi are theta-free: the (Y, Y delta_AB, Y_:AB) decomposition closes", all(v.free_symbols <= {Rs, H0, H1, H2, K0, K1, K2} for v in [dsigma, dP, Pi]))
print("     kinematic (any exterior):  delta sigma =", dsigma); print("                                delta P     =", dP); print("                                Pi          =", Pi)
# impose the exterior field equations at R: H'' from the master ODE, K and K' from (2b)/(2c)
h = sp.Function("h")(r)
H2_ode = sp.solve(sp.Eq(master.subs(Hf, h).doit(), 0), sp.Derivative(h, (r, 2)))[0].subs({sp.Derivative(h, r): H1, h: H0}).subs(r, Rs)
K0_ode = sp.simplify(K_3624.subs(Hf, h).doit().subs({sp.Derivative(h, (r, 2)): H2_ode * 0 + sp.Symbol("H2")}).subs({sp.Derivative(h, r): H1, h: H0}).subs(r, Rs).subs(sp.Symbol("H2"), H2_ode))
K1_ode = sp.simplify(H1 + 2 * M * H0 / (Rs * (Rs - 2 * M)))
vac = {H2: H2_ode, K0: K0_ode, K1: K1_ode}
dsigma_v, dP_v, Pi_v = [sp.simplify(v.subs(vac)) for v in [dsigma, dP, Pi]]
lam = sp.symbols("lambda")
Hlam = HG + lam * HD
H0l = Hlam.subs(r, Rs); H1l = sp.diff(Hlam, r).subs(r, Rs)
at = lambda v: sp.simplify(v.subs({H0: H0l, H1: H1l}).subs(Rs, Rn))
dsig_l, dP_l, Pi_l, K0_l, xi_l = [at(v) for v in [dsigma_v, dP_v, Pi_v, K0_ode, xi_sol]]
dr_areal_l = sp.simplify(xi_l - Rn * K0_l / 2)          # areal radius of the surface 2-sphere = xi_in
print("     at R = 8M/3, per unit tidal amplitude (H_G normalised to r(r-2M)), affine in lambda:")
for nm, v in [("delta sigma", dsig_l), ("delta P", dP_l), ("Pi", Pi_l), ("K(R)", K0_l), ("xi", xi_l), ("delta r_areal", dr_areal_l)]:
    print(f"       {nm:14s} = {sp.N(v, 8)}")
check("(4b) every response is affine in lambda: one free exterior coefficient = one free datum", all(sp.Poly(sp.expand(v), lam).degree() <= 1 for v in [dsig_l, dP_l, Pi_l, K0_l, dr_areal_l]))
check("(4c) the responses are NOT all proportional to each other: the datum is a genuine second condition, not a normalisation", sp.simplify(dsig_l.diff(lam) * dP_l.subs(lam, 0) - dP_l.diff(lam) * dsig_l.subs(lam, 0)) != 0)

# ---------- (5) conservation ----------
check("(5a) delta P = 2 Pi / R^2 identically in (H, H', R) once the field equations are imposed — shell conservation D_a S^a_B = 0 with the lapse uniform (level set)", sp.simplify(dP_v - 2 * Pi_v / Rs**2) == 0)
check("(5b) the same combination is NOT zero kinematically (before the field equations): it is Bianchi, not tautology", sp.simplify(dP - 2 * Pi / Rs**2) != 0)
lam_Pi0 = sp.solve(sp.Eq(Pi_l, 0), lam)[0]
check("(5c) Pi = 0 (no shear) forces delta P = 0 at the same lambda but leaves delta sigma != 0: no barotropic fluid shell sits statically in the tide — the surface MUST carry shear stress", sp.simplify(dP_l.subs(lam, lam_Pi0)) == 0 and sp.simplify(dsig_l.subs(lam, lam_Pi0)) != 0, f"delta sigma at Pi=0: {sp.N(dsig_l.subs(lam, lam_Pi0), 6)}")

# ---------- (6) the family ----------
Cn = M / Rn
def k2_hinderer(C, y):
    C = float(C); y = float(y)
    return (8 * C**5 / 5) * (1 - 2 * C)**2 * (2 + 2 * C * (y - 1) - y) / (2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * (1 - 2 * C)**2 * (2 - y + 2 * C * (y - 1)) * np.log(1 - 2 * C))
y_of = lambda lv: sp.simplify((Rn * H1l / H0l).subs(Rs, Rn).subs(lam, lv))
closures = [("black hole (lambda = 0)", sp.Integer(0)),
            ("K(R) = 0  [3624: xi_in = xi]", sp.solve(sp.Eq(K0_l, 0), lam)[0]),
            ("delta sigma = 0  [count per proper area fixed]", sp.solve(sp.Eq(dsig_l, 0), lam)[0]),
            ("delta r_areal = 0  [surface intrinsically rigid]", sp.solve(sp.Eq(dr_areal_l, 0), lam)[0]),
            ("Pi = 0 = delta P  [no shear]", lam_Pi0)]
rows = {}
print("     closure                                            lambda       y          k2       Lambda   dsigma    dP        Pi       K(R)     dr_areal  mu_eff=Pi*R/dr_areal")
for nm, lv in closures:
    yv = y_of(lv); k2 = k2_hinderer(Cn, yv); Lam = (2 / 3) * k2 / float(Cn)**5
    vals = [float(v.subs(lam, lv)) for v in [dsig_l, dP_l, Pi_l, K0_l, dr_areal_l]]
    mu = vals[2] * float(Rn) / vals[4] if abs(vals[4]) > 1e-12 else float("inf")
    rows[nm] = (float(lv), float(yv), k2, Lam, vals, mu)
    print(f"     {nm:50s} {float(lv):8.4f} {float(yv):9.4f} {k2:9.4f} {Lam:8.2f}  " + " ".join(f"{v:8.4f}" for v in vals) + f"  {mu:8.3f}")
lamK = closures[1][1]
check("(6a) K(R) = 0 reproduces 3624/3629: y = -31/3 exactly, k2 = -0.080", sp.simplify(y_of(lamK) + sp.Rational(31, 3)) == 0 and abs(rows[closures[1][0]][2] + 0.080) < 0.001)
check("(6b) the black-hole member (lambda = 0) has k2 = 0 to 1e-10", abs(rows[closures[0][0]][2]) < 1e-10)
k2s = [rows[nm][2] for nm, _ in closures[1:4]]
check("(6c) the shear-carrying closures give DISTINCT Love numbers, of BOTH signs — the datum is physical, and the SIGN of k2 is closure-dependent (3624/3626's negative sign was the K(R) = 0 closure's)", len({round(v, 4) for v in k2s}) == len(k2s) and min(k2s) < 0 < max(k2s), ", ".join(f"{v:+.4f}" for v in k2s))
check("(6d) |k2| in 1e-2..1e-1 across the shear-carrying closures (3629: magnitude robust); the no-shear member is excluded by (5c) and would sit at k2 ~ 8", all(0.005 < abs(v) < 0.2 for v in k2s) and rows[closures[4][0]][2] > 1)
# the datum is ONE number: delta sigma. Pi and delta P are set by the tide (their lambda-coefficients are ~1e-4 of the constants)
check("(6e) Pi and delta P are set by the tide, not by the closure: their lambda-slopes are < 1e-3 of the black-hole values — the second junction reduces to ONE datum, delta sigma (how the count per proper area responds)", abs(float(Pi_l.diff(lam)) / float(Pi_l.subs(lam, 0))) < 1e-3 and abs(float(dP_l.diff(lam)) / float(dP_l.subs(lam, 0))) < 1e-3, f"Pi slope/const = {float(Pi_l.diff(lam))/float(Pi_l.subs(lam,0)):.2e}")
lam_of_dsig = sp.solve(sp.Eq(dsig_l, sp.Symbol("ds")), lam)[0]
print("     lambda(delta sigma) =", sp.N(lam_of_dsig, 6), "   -> k2 is a linear-fractional function of the one datum delta sigma")

# ---------- (7) the register's own closure: the CENSUS (Newtonian limit) ----------
# The corpus's dictionary (GR-1c; R-PSR-LAW-LOG, 3390; 3629 Q5): M = the count at cap; the register v is the 1/r census of the
# count (v = M/r_iso outside); the surface is the level set v = 2/3; the interior is uniformly at cap. So the register does NOT
# need a stress law: the exterior perturbation is the CENSUS of a uniform-count region bounded by the moved level set.
# Newtonian limit, self-consistently: density rho, radius R, tide E r^2 P2, boundary R + d P2, level set of (self + tide).
G_, rho, Rb = sp.symbols("G rho R_b", positive=True); E, d = sp.symbols("E d", real=True)
g_surf = sp.Rational(4, 3) * sp.pi * G_ * rho * Rb                       # surface gravity of the ball
dPhi_layer_at_R = -4 * sp.pi * G_ * rho * d * Rb / 5                     # potential of the l = 2 surface layer sigma = rho d P2 at r = R
level = sp.Eq(g_surf * d + dPhi_layer_at_R + E * Rb**2, 0)               # Phi_0(R + dP2) + dPhi + Phi_tide = const
d_sol = sp.solve(level, d)[0]
Q_ind = 4 * sp.pi * rho * Rb**4 * d_sol / 5                                # mass quadrupole of the moved boundary
k2_census = sp.simplify(-G_ * Q_ind / (E * Rb**5))                         # dPhi_ext = -G Q P2 / r^3 = k2 E R^5 P2 / r^3  ... sign: k2 = -G Q/(E R^5)
check("(7a) Newtonian census closure (uniform count inside the register's level set): k2 = 3/2, Kelvin's homogeneous-body Love number; h2 = 1 + k2 = 5/2", sp.simplify(k2_census - sp.Rational(3, 2)) == 0, f"k2 = {k2_census}")
check("(7b) the census closure is POSITIVE and O(1) in the Newtonian limit — opposite in sign to the K(R) = 0 member and ~20x its magnitude; the relativistic census at C = 0.375 (the corpus's v = M/r_iso law, level set v = 2/3) is the next act", k2_census > 0)
print(); print(f"3631 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
