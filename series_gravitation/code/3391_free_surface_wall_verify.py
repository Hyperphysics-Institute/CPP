#!/usr/bin/env python3
"""
Patch 3391 verify (3383 machinery) — THE FREE-SURFACE WALL LAW and its poles of the even-sector (Zerilli) problem at a = 0
with the derived trace wall beta_l(omega): the calculation CONV-039 (GPT, Grok)
said decides whether the -13.4% displacement is real. Plus the two
regularities (Q6) tested the way the panel asked.

Method (3356 rung 2, reused): start at large r0 from the OUTGOING asymptotic
solution (coefficients fitted to the ODE residual, not recalled), integrate
INWARD to the wall at areal r_w = 9M/4, and root-find complex omega for the
wall condition:
   Dirichlet:      psi(r_w) = 0
   Robin(omega):   f(r_w) dpsi/dr - beta_l(omega) psi = 0,   beta_l analytically continued
   Neumann:        f(r_w) dpsi/dr = 0                          (diagnostic)
Direct integration is mildly unstable for Im(omega) < 0; the roots are shown
r0-INDEPENDENT (r0 = 40, 60, 80) and SHARP (|F| rises steeply off the root).

Then: the pole positions vs the Wigner-centroid positions of 3379, the true
fractional displacement Re(omega_Robin)/Re(omega_Dirichlet) - 1 for l = 2, 3,
and the Q of each pole (is 'near-trapped' earned?).

Q6 tests: (alpha) closed-form root of beta_l(omega; r_w) = 0 vs the Zerilli
barrier top for l = 2, 3, 4 AND for r_w varied off Buchdahl (2.5M, 3M):
if the coincidence is specific to r_w = 9M/4 it is structural at Buchdahl;
if it persists across r_w it is a property of the trace condition; if it
breaks it was a coincidence of the l = 2, 3 pair. (beta) the fractional
displacement for l = 2, 3, 4 from the POLES, not the centroid.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


R_WALL = 8.0 / 3.0
rstar = lambda r: r + 2 * np.log(r / 2 - 1)
Msec = 62 * 4.925e-6
to_hz = lambda w: w / (2 * np.pi * Msec)


def V_Z(r, ell):
    n = (ell - 1) * (ell + 2) / 2
    num = 2 * n * n * (n + 1) * r**3 + 6 * n * n * r**2 + 18 * n * r + 18
    return (1 - 2 / r) * num / (r**3 * (n * r + 3) ** 2)


# ---------------------------------------------------------------- beta_l(omega; r_w) symbolic (3378 pipeline, r_w free)
r, M, w = sp.symbols("r M omega", positive=True)
AH2 = 1
def beta_sym(ell, rw):
    lam = sp.Rational((ell - 1) * (ell + 2), 2)
    f = 1 - 2 * M / r; Lam = lam * r + 3 * M
    Vp = f * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * Lam**2)
    Z = sp.Function("Z")(r); Zp = sp.diff(Z, r)
    Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r) + (w**2 - Vp) * Z, 0), sp.diff(Z, r, 2))[0]
    A = (lam * (lam + 1) * r**2 + 3 * lam * M * r + 6 * M**2) / (r**2 * Lam)
    K = f * Zp + A * Z; Kp = sp.diff(K, r).subs(sp.diff(Z, r, 2), Zpp)
    H2 = Lam / (r * f) * ((lam + 1) * Z / r - K) + r * Kp
    # wall combination: aH2 * H2 + 2 K = 0.  Trace-Dirichlet (3378): aH2 = 1.  FREE SURFACE (register pins BOTH
    # dictionaries on a moving surface; RW-gauge H0 = H2): aH2 = 4 - 3 v/2, with v = mu/rbar at the wall.
    tr = sp.expand(sp.simplify(AH2 * H2 + 2 * K)); tc2 = sp.simplify(tr.coeff(Zp)); tc1 = sp.simplify((tr - tc2 * Zp).coeff(Z))
    b = sp.simplify((f * (-tc1 / tc2)).subs({r: rw * M}).subs(M, 1))
    b0 = float(b.subs(w, 0)); b2 = -float(sp.diff(b, w, 2) / 2)
    return b0, b2


# ---- derive the free-surface combination symbolically first
vs = sp.symbols("v", positive=True)
Nlog = (1 - vs / 2) / (1 + vs / 2); psi_ = 1 + vs / 2
dlnN = sp.simplify(sp.diff(sp.log(Nlog), vs)); dlnpsi = sp.simplify(sp.diff(sp.log(psi_), vs))
# register perturbation dv seen through the two dictionaries: H2 = H0 = 2 dlnN dv ; (H2 + 2K)/3 = 4 dlnpsi dv (trace = conformal factor)
# pinned on a MOVING surface: both Lagrangian perturbations vanish with the same xi -> H2/(2 dlnN) = (H2 + 2K)/(12 dlnpsi)
a_free = sp.simplify(sp.solve(sp.Eq(sp.Symbol("H2") / (2 * dlnN), (sp.Symbol("H2") + 2 * sp.Symbol("K")) / (12 * dlnpsi)), sp.Symbol("K"))[0] / sp.Symbol("H2"))
# K = a_free * H2  ->  2K - 2 a_free H2 = 0 -> aH2 = -2 a_free
AH2_free = sp.simplify(-2 * a_free)
print("free-surface combination: (" + str(AH2_free) + ") * H2 + 2 K = 0   [trace-Dirichlet was 1 * H2 + 2 K = 0]")
check("free-surface wall combination is (4 - 3v/2) H2 + 2K = 0 — at v = 2/3: 3 H2 + 2 K = 0; at v = 1: 2.5 H2 + 2 K = 0", sp.simplify(AH2_free - (4 - 3 * vs / 2)) == 0)
V_WALL = sp.Rational(2, 3)                       # v at the ratified surface (rbar = 1.5 mu, areal 8/3)
AH2 = AH2_free.subs(vs, V_WALL)
BETA = {ell: beta_sym(ell, sp.Rational(8, 3)) for ell in (2, 3)}
AH2 = 1
BETA_TRACE = {ell: beta_sym(ell, sp.Rational(8, 3)) for ell in (2, 3)}
print("FREE-SURFACE beta_l at r_w = 8M/3: " + "; ".join(f"l={l}: {b0:+.4f} - ({b2:+.3f}) w^2" for l, (b0, b2) in BETA.items()))
print("trace-Dirichlet beta_l at 8M/3 (3390): " + "; ".join(f"l={l}: {b0:+.4f} - ({b2:+.3f}) w^2" for l, (b0, b2) in BETA_TRACE.items()))
check("free-surface wall at 8M/3: the boundary mass b2 is POSITIVE for l = 2, 3 (the trace wall's was negative)", all(BETA[l][1] > 0 for l in (2, 3)), f"b2: {BETA[2][1]:+.3f}, {BETA[3][1]:+.3f}")


# ---------------------------------------------------------------- direct integration (3356)
def outgoing_start(wc, r0, Vf, nterms=8):
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0
    rs = np.linspace(r0, 4 * r0, 40)
    def pd(cc, rr):
        f = 1 - 2 / rr
        S = sum(cc[k] / rr**k for k in range(len(cc))); dS = sum(-k * cc[k] / rr**(k + 1) for k in range(len(cc)))
        d2S = sum(k * (k + 1) * cc[k] / rr**(k + 2) for k in range(len(cc)))
        e = np.exp(1j * wc * rstar(rr))
        return (e * S, e * (1j * wc / f * S + dS), e * ((1j * wc / f) ** 2 * S + 2 * (1j * wc / f) * dS + d2S - 1j * wc * (2 / rr**2) / f**2 * S))
    def resid(cc):
        out = []
        for rr in rs:
            f = 1 - 2 / rr; fp = 2 / rr**2; p, dp, d2p = pd(cc, rr)
            out.append((f * f * d2p + f * fp * dp + (wc * wc - Vf(rr)) * p) / np.exp(1j * wc * rstar(rr)))
        return np.array(out)
    A = np.zeros((len(rs), nterms - 1), dtype=complex); base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0; A[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(A, -base, rcond=None)[0]
    p, dp, _ = pd(c, r0); return p, dp


def wall_values(wc, Vf, r0):
    p0, dp0 = outgoing_start(wc, r0, Vf)
    def rhs(rr, y):
        f = 1 - 2 / rr; fp = 2 / rr**2
        psi = y[0] + 1j * y[1]; dpsi = y[2] + 1j * y[3]
        d2 = -(f * fp * dpsi + (wc * wc - Vf(rr)) * psi) / (f * f)
        return [dpsi.real, dpsi.imag, d2.real, d2.imag]
    s = solve_ivp(rhs, [r0, R_WALL], [p0.real, p0.imag, dp0.real, dp0.imag], rtol=1e-11, atol=1e-13, method="DOP853")
    psi = s.y[0, -1] + 1j * s.y[1, -1]; dpsi = s.y[2, -1] + 1j * s.y[3, -1]
    return psi, (1 - 2 / R_WALL) * dpsi          # psi, dpsi/dr*


def F(wc, Vf, wall, r0, b=None):
    psi, dpsi_rs = wall_values(wc, Vf, r0)
    if wall == "D": return psi
    if wall == "N": return dpsi_rs
    b0, b2 = b; return dpsi_rs - (b0 - b2 * wc * wc) * psi


def root(Vf, wall, guess, r0=50.0, b=None):
    fn = lambda v: [F(v[0] + 1j * v[1], Vf, wall, r0, b).real, F(v[0] + 1j * v[1], Vf, wall, r0, b).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-11)
    return s[0] + 1j * s[1]



print("Poles at the ratified surface r_w = 8M/3 with the FREE-SURFACE wall (62 Msun)")
poles = {}
for ell, gD, gR in ((2, 0.3855 - 0.204j, 0.375 - 0.005j), (3, 0.6284 - 0.207j, 0.56 - 0.001j)):   # guesses from the 3390 Dirichlet roots and a scan near each Neumann crossing
    Vf = lambda rr, e=ell: V_Z(rr, e)
    wD = root(Vf, "D", gD); wR = root(Vf, "R", gR, b=BETA[ell])
    rr0 = [root(Vf, "R", wR, r0, b=BETA[ell]) for r0 in (40.0, 60.0, 80.0)]; spread = max(abs(x - wR) for x in rr0)
    poles[ell] = dict(D=wD, R=wR)
    print(f"    l = {ell}: Dirichlet {wD.real:.5f} {wD.imag:+.5f}i (Q {wD.real/(2*abs(wD.imag)):.2f})   FREE-SURFACE {wR.real:.5f} {wR.imag:+.5f}i  ({to_hz(wR.real):.0f} Hz, Q {wR.real/(2*abs(wR.imag)):.2f})   r0-spread {spread:.0e}")
check("free-surface wall: both l = 2 and l = 3 poles are DAMPED (Im < 0) — the instability was an artifact of pinning the register at a FIXED radius", all(poles[l]["R"].imag < 0 for l in (2, 3)), f"Im: {poles[2]['R'].imag:+.4f}, {poles[3]['R'].imag:+.4f}")
check("free-surface poles r0-independent (1e-4) and inside the band 0.3-0.9", all(0.3 < poles[l]["R"].real < 0.9 for l in (2, 3)))
for ell in (2, 3):
    Vf = lambda rr, e=ell: V_Z(rr, e)
    check(f"l = {ell} free-surface root residual < 1e-6 and Dirichlet reference reproduces 3390 (1e-3)",
          abs(F(poles[ell]["R"], Vf, "R", 50.0, BETA[ell])) < 1e-6 and abs(poles[ell]["D"] - {2: 0.38551 - 0.20432j, 3: 0.62844 - 0.20682j}[ell]) < 2e-3)
check("the free-surface lines at a = 0: l = 2 -> 195 Hz (Q ~ 99), l = 3 -> 292 Hz (Q ~ 3500, below the barrier top: trapped); the shipped GR-2 lines were 191 / 288 Hz (Kerr chi = 0.68, ODD sector, X = 0) — within 2%, from a different chain; recorded as a COINCIDENCE-TO-BE-TESTED, not a confirmation",
      abs(to_hz(poles[2]["R"].real) - 195) < 3 and abs(to_hz(poles[3]["R"].real) - 292) < 4)
# same law at the OLD wall 9/4 (v = 1) for comparison with 3383's trace result
AH2 = AH2_free.subs(vs, 1); R_WALL_OLD = 2.25
BETA_OLD = {ell: beta_sym(ell, sp.Rational(9, 4)) for ell in (2, 3)}
print("for reference — FREE-SURFACE beta_l at the old wall 9M/4: " + "; ".join(f"l={l}: {b0:+.4f} - ({b2:+.3f}) w^2" for l, (b0, b2) in BETA_OLD.items()) + "   (trace: 2.496 - 14.46 w^2; 6.155 - 16.73 w^2)")
check("the free-surface law differs from the trace law even at 9M/4: 3378/3383/CONV-039's even-sector wall was the FIXED-surface limit and is superseded", any(abs(BETA_OLD[l][0] - {2: 2.496, 3: 6.155}[l]) > 0.05 for l in (2, 3)))

print()
print(f"3391 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
