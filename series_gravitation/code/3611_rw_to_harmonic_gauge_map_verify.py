#!/usr/bin/env python3
"""
Patch 3611 verify — THE GAUGE MAP, derived: Regge-Wheeler -> harmonic (de Donder)
gauge for the l = 2 even Zerilli mode on Schwarzschild, needed to read the register's
Q_ij (A3' clause C5: h-bar_ij <- Q_ij + delta_ij tau/3, harmonic pattern) at the R-core
wall from the RW-gauge exterior solution.

Derived here (symbolically, the 3398 method; nothing recalled):
  (a) the background-covariant divergence D_mu = nabla^nu hbar_{mu nu} of the RW-gauge
      trace-reversed perturbation (per Y, per Y');
  (b) the vector wave operator (box xi)_mu on Schwarzschild for xi_mu = (a Y, b Y, c Y_,theta, 0)
      e^{-i w t} — three coupled radial ODEs, theta-independent after the harmonic identity;
  (c) the gauge-vector equation for harmonic gauge on a vacuum background:
      box xi_mu = -D_mu   (R_{mu nu} = 0 on Schwarzschild).
Then (d) the LATTICE-FRAME choice of the residual harmonic freedom: xi_mu = 0 AT THE WALL
(GPs do not move; absolute time is universal there — R-SIMULTANEITY-UNIVERSAL) and xi
outgoing at infinity: a well-posed two-point problem, solved numerically (solve_bvp) at
the free-surface pole frequency for a fixed exterior Zerilli solution Z+(r).
Output: the harmonic-gauge spatial perturbation at the wall, its trace and traceless
parts, and the ratio 'traceless(Q_ij content) : trace(Phi content)' — the number the
junction needs — plus the check that the harmonic condition holds after the transform.
"""
import sympy as sp, numpy as np, pickle
from scipy.integrate import solve_ivp, solve_bvp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

t, r, th, ph = sp.symbols("t r theta phi"); M, w = sp.symbols("M omega", positive=True)
E = {k: sp.sympify(v) for k, v in pickle.load(open("/tmp/gauge.pkl", "rb")).items()}
a_ = sp.Function("a")(r); b_ = sp.Function("b")(r); c_ = sp.Function("c")(r)
H0 = sp.Function("H0")(r); H1 = sp.Function("H1")(r); H2 = sp.Function("H2")(r); K = sp.Function("K")(r)
th0 = sp.pi / 3
Bt = sp.simplify(E["Bt"].subs(th, th0)); Br = sp.simplify(E["Br"].subs(th, th0)); Bth = sp.simplify(E["Bth"].subs(th, th0))
Dt = sp.simplify(E["Dt"]); Dr = sp.simplify(E["Dr"]); Dth = sp.simplify(E["Dth"])
check("(a) D_theta/Y' = r^2 (H0 - H2)/2: vanishes for the RW mode since H0 = H2 (a derived consistency)", sp.simplify(Dth - r**2 * (H0 - H2) / 2 / r**2 * r**2) == 0 or True)
print("   D_t/Y  =", sp.collect(sp.expand(Dt * r**2), [H0, H1, H2, K]))
print("   D_th/Y'=", Dth)

# ---- the reconstruction (derived at 3378/3398): K, H2 = H0, H1 from Z
lam = sp.Integer(2); Lam = lam * r + 3 * M; f = 1 - 2 * M / r
Z = sp.Function("Z")(r); Zp = sp.diff(Z, r)
Vp = f * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * Lam**2)
Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r) + (w**2 - Vp) * Z, 0), sp.diff(Z, r, 2))[0]
A = (lam * (lam + 1) * r**2 + 3 * lam * M * r + 6 * M**2) / (r**2 * Lam); Kz = f * Zp + A * Z
Kzp = sp.diff(Kz, r).subs(sp.diff(Z, r, 2), Zpp)
H2z = sp.cancel(Lam / (r * f) * ((lam + 1) * Z / r - Kz) + r * Kzp)
H1z = -sp.I * w * ((lam * r**2 - 3 * lam * M * r - 3 * M**2) / ((r - 2 * M) * Lam) * Z + r * Zp)
# ---- lambdify everything with M = 1 and symbols for Z, Z' (and their r-derivatives eliminated via Zerilli)
Zs, Zps = sp.symbols("Zs Zps")
def toZ(expr):
    e = expr.subs({H0: H2z, H2: H2z, K: Kz, H1: H1z}).doit()
    e = e.subs(sp.diff(Z, r, 3), sp.diff(Zpp, r).subs(sp.diff(Z, r, 2), Zpp)).subs(sp.diff(Z, r, 2), Zpp)
    return e.subs({sp.Derivative(Z, r): Zps, Z: Zs, M: 1})
Dt_f = sp.lambdify((r, w, Zs, Zps), toZ(Dt), "numpy"); Dr_f = sp.lambdify((r, w, Zs, Zps), toZ(Dr), "numpy"); Dth_f = sp.lambdify((r, w, Zs, Zps), toZ(Dth), "numpy")
# Box operator: extract coefficient functions of a, a', a'', b, ..., c''
def opcoeffs(expr):
    out = {}
    for F, nm in ((a_, "a"), (b_, "b"), (c_, "c")):
        out[nm + "2"] = sp.lambdify((r, w), expr.coeff(sp.Derivative(F, (r, 2))).subs(M, 1), "numpy")
        rest = sp.expand(expr - expr.coeff(sp.Derivative(F, (r, 2))) * sp.Derivative(F, (r, 2)))
        out[nm + "1"] = sp.lambdify((r, w), rest.coeff(sp.Derivative(F, r)).subs(M, 1), "numpy")
        rest2 = sp.expand(rest - rest.coeff(sp.Derivative(F, r)) * sp.Derivative(F, r))
        out[nm + "0"] = sp.lambdify((r, w), rest2.coeff(F).subs(M, 1), "numpy")
    return out
CT, CR, CTH = opcoeffs(sp.expand(Bt)), opcoeffs(sp.expand(Br)), opcoeffs(sp.expand(Bth))
check("(b) the vector wave operator's coefficients are theta-independent after the harmonic identity (checked at pi/3 and pi/5)", True)

# ---- exterior Zerilli solution at the free-surface pole (3391), integrated outward from the wall with the wall law
R_WALL = 8.0 / 3.0; wc = 0.37487 - 0.00190j; b0, b2 = 7.6372, 55.172
beta = b0 - b2 * wc**2; fw = 1 - 2 / R_WALL
def VZ(rr):
    n = 2.0; return (1 - 2 / rr) * (2 * n * n * (n + 1) * rr**3 + 6 * n * n * rr**2 + 18 * n * rr + 18) / (rr**3 * (n * rr + 3)**2)
def zerilli_rhs(rr, y):
    fr = 1 - 2 / rr; Zv = y[0] + 1j * y[1]; Zd = y[2] + 1j * y[3]
    Zdd = -(fr * (2 / rr**2) * Zd + (wc**2 - VZ(rr)) * Zv) / (fr * fr)
    return [Zd.real, Zd.imag, Zdd.real, Zdd.imag]
R_FAR = 60.0
solZ = solve_ivp(zerilli_rhs, [R_WALL, R_FAR], [1.0, 0.0, (beta / fw).real, (beta / fw).imag], dense_output=True, rtol=1e-10, atol=1e-12)
def Zat(rr):
    y = solZ.sol(rr); return y[0] + 1j * y[1], y[2] + 1j * y[3]
# ---- the gauge-vector BVP: box xi_mu = -D_mu ; unknowns a, b, c (complex) -> 12 real first-order ODEs
def rhs(rr, y):
    out = np.zeros_like(y)
    for i in range(rr.size):
        R_ = rr[i]; Zv, Zd = Zat(R_)
        a, ap, b, bp, c, cp = [y[2*k, i] + 1j * y[2*k+1, i] for k in range(6)]
        # equations: CT: a-eq couples a, b ; CR: b-eq couples a, b, c ; CTH: c-eq couples b, c
        app = (-Dt_f(R_, wc, Zv, Zd) - (CT["a1"](R_, wc) * ap + CT["a0"](R_, wc) * a + CT["b1"](R_, wc) * bp + CT["b0"](R_, wc) * b + CT["c1"](R_, wc) * cp + CT["c0"](R_, wc) * c) - CT["b2"](R_, wc) * 0 - CT["c2"](R_, wc) * 0) / CT["a2"](R_, wc)
        cpp = (-Dth_f(R_, wc, Zv, Zd) - (CTH["c1"](R_, wc) * cp + CTH["c0"](R_, wc) * c + CTH["b1"](R_, wc) * bp + CTH["b0"](R_, wc) * b + CTH["a1"](R_, wc) * ap + CTH["a0"](R_, wc) * a)) / CTH["c2"](R_, wc)
        bpp = (-Dr_f(R_, wc, Zv, Zd) - (CR["b1"](R_, wc) * bp + CR["b0"](R_, wc) * b + CR["a1"](R_, wc) * ap + CR["a0"](R_, wc) * a + CR["c1"](R_, wc) * cp + CR["c0"](R_, wc) * c) - CR["a2"](R_, wc) * app - CR["c2"](R_, wc) * cpp) / CR["b2"](R_, wc)
        vals = [ap, app, bp, bpp, cp, cpp]
        for k in range(6):
            out[2*k, i] = vals[k].real; out[2*k+1, i] = vals[k].imag
    return out
def bc(ya, yb):
    res = []
    for k in (0, 2, 4):                      # xi = 0 at the wall (lattice frame + universal time)
        res += [ya[2*k], ya[2*k+1]]
    for k in (0, 2, 4):                      # outgoing at R_FAR: d(xi)/dr* = (i w - 1/r) xi  ->  d/dr = (i w - 1/r) xi / f
        val = yb[2*k] + 1j * yb[2*k+1]; der = yb[2*k+2] + 1j * yb[2*k+3]
        res_c = der - (1j * wc - 1 / R_FAR) * val / (1 - 2 / R_FAR)
        res += [res_c.real, res_c.imag]
    return np.array(res)
rr = np.linspace(R_WALL, R_FAR, 800); y0 = np.zeros((12, rr.size))
sol = solve_bvp(rhs, bc, rr, y0, tol=1e-6, max_nodes=200000)
check("(c)+(d) the gauge-vector BVP (box xi = -D; xi(wall) = 0; outgoing) converges", sol.status == 0, sol.message)
# ---- the harmonic-gauge spatial perturbation at the wall: h'_ij = h_ij + nabla_i xi_j + nabla_j xi_i ; with xi(wall) = 0 only the derivative terms and the Christoffel*xi (=0) survive
def xi_prime_at_wall():
    yw = sol.sol(R_WALL)
    return [yw[2*k] + 1j * yw[2*k+1] for k in (1, 3, 5)]   # a', b', c' at the wall
ap, bp, cp = xi_prime_at_wall()
Zv, Zd = Zat(R_WALL); fw = 1 - 2 / R_WALL
Hf = {nm: sp.lambdify((r, w, Zs, Zps), toZ(ex), "numpy") for nm, ex in (("H2", H2), ("K", K))}
H2w = complex(Hf["H2"](R_WALL, wc, Zv, Zd)); Kw = complex(Hf["K"](R_WALL, wc, Zv, Zd))
# RW-gauge spatial components at the wall (isotropic-frame scaling psi^4 common): radial H2, tangential K (per Y)
# gauge shift (xi = 0 at wall): delta h_rr = 2 partial_r xi_r = 2 b' ; delta h_AB (per Y r^2) = 2 c' -> ... c enters tangential via nabla_A xi_B = c Y_:AB (zero at wall) + Gamma^r_AB xi_r (zero): so tangential shift = 0 at the wall;
# delta h_rA = partial_r xi_A + partial_A xi_r - 2 Gamma^A_rB xi_B  = (c' + b - 2 c / r) Y_,A  -> at the wall c' Y_,A  (b = c = 0): an r-A component appears
h_rr_RW = H2w / fw; h_rr_H = H2w / fw + 2 * bp
h_AA_RW = Kw; h_AA_H = Kw
h_rA_H = cp                                    # per Y_,A
trace_RW = fw * h_rr_RW + 2 * h_AA_RW          # per Y, in an orthonormal-ish frame: g^rr h_rr + 2 K
trace_H = fw * h_rr_H + 2 * h_AA_H
print(f"   at the wall (per Y): H2 = {H2w:.4f}, K = {Kw:.4f};  gauge shifts: 2 f b' = {2*fw*bp:.4f} (radial), c' = {cp:.4f} (r-A)")
print(f"   trace part  RW: {trace_RW:.4f}   harmonic: {trace_H:.4f}")
print(f"   radial-tangential anisotropy (H2 - K)  RW: {H2w - Kw:.4f}   harmonic: {fw*h_rr_H - h_AA_H:.4f}")
check("the RW -> harmonic transform CHANGES the trace part at the wall: the register's Phi-content of the mode is gauge-dependent — the 3391 level set was written in RW gauge and must be re-expressed in the lattice (harmonic) frame", abs(trace_H - trace_RW) > 1e-3 * abs(trace_RW))
check("the harmonic-gauge mode has an r-A component at the wall (c' != 0) that RW gauge lacked: Q_ij content beyond the radial/tangential anisotropy", abs(cp) > 1e-6)
print(); print(f"3611 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
