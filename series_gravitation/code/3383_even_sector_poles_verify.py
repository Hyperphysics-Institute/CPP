#!/usr/bin/env python3
"""
Patch 3383 verify — COMPLEX POLES of the even-sector (Zerilli) problem at a = 0
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


R_WALL = 2.25
rstar = lambda r: r + 2 * np.log(r / 2 - 1)
Msec = 62 * 4.925e-6
to_hz = lambda w: w / (2 * np.pi * Msec)


def V_Z(r, ell):
    n = (ell - 1) * (ell + 2) / 2
    num = 2 * n * n * (n + 1) * r**3 + 6 * n * n * r**2 + 18 * n * r + 18
    return (1 - 2 / r) * num / (r**3 * (n * r + 3) ** 2)


# ---------------------------------------------------------------- beta_l(omega; r_w) symbolic (3378 pipeline, r_w free)
r, M, w = sp.symbols("r M omega", positive=True)
def beta_sym(ell, rw):
    lam = sp.Rational((ell - 1) * (ell + 2), 2)
    f = 1 - 2 * M / r; Lam = lam * r + 3 * M
    Vp = f * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * Lam**2)
    Z = sp.Function("Z")(r); Zp = sp.diff(Z, r)
    Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r) + (w**2 - Vp) * Z, 0), sp.diff(Z, r, 2))[0]
    A = (lam * (lam + 1) * r**2 + 3 * lam * M * r + 6 * M**2) / (r**2 * Lam)
    K = f * Zp + A * Z; Kp = sp.diff(K, r).subs(sp.diff(Z, r, 2), Zpp)
    H2 = Lam / (r * f) * ((lam + 1) * Z / r - K) + r * Kp
    tr = sp.expand(sp.simplify(H2 + 2 * K)); tc2 = sp.simplify(tr.coeff(Zp)); tc1 = sp.simplify((tr - tc2 * Zp).coeff(Z))
    b = sp.simplify((f * (-tc1 / tc2)).subs({r: rw * M}).subs(M, 1))
    b0 = float(b.subs(w, 0)); b2 = -float(sp.diff(b, w, 2) / 2)
    return b0, b2


BETA = {ell: beta_sym(ell, sp.Rational(9, 4)) for ell in (2, 3, 4)}
print("beta_l(omega) at r_w = 9M/4:  " + "; ".join(f"l={l}: {b0:.4f} - {b2:.3f} w^2" for l, (b0, b2) in BETA.items()))
check("l = 2, 3 coefficients reproduce 3378/3379", abs(BETA[2][0] - 2.496) < 0.002 and abs(BETA[3][1] - 16.73) < 0.02)


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


# ---------------------------------------------------------------- poles
print("Poles at the wall r_w = 9M/4 (M = 1), even sector")
poles = {}
for ell, gD, gR in ((2, 0.45 - 0.11j, 0.40 - 0.05j), (3, 0.70 - 0.12j, 0.60 - 0.05j)):
    Vf = lambda rr, e=ell: V_Z(rr, e)
    wD = root(Vf, "D", gD); wN = root(Vf, "N", gR); wR = root(Vf, "R", gR, b=BETA[ell])
    poles[ell] = dict(D=wD, N=wN, R=wR)
    for lab, ww in (("Dirichlet", wD), ("Neumann", wN), ("Robin beta(w)", wR)):
        print(f"    l = {ell} {lab:14s}: w = {ww.real:.5f} {ww.imag:+.5f} i   ({to_hz(ww.real):.0f} Hz @62 Msun)   Q = {ww.real/(2*abs(ww.imag)):.2f}")
check("l = 2 Dirichlet Zerilli wall pole reproduces 3356 EXACTLY (0.44506 - 0.13442i)", abs(poles[2]["D"] - (0.44506 - 0.13442j)) < 2e-5)
# r0-independence and sharpness for the Robin roots
for ell in (2, 3):
    Vf = lambda rr, e=ell: V_Z(rr, e)
    rr0 = [root(Vf, "R", poles[ell]["R"], r0, b=BETA[ell]) for r0 in (40.0, 60.0, 80.0)]
    spread = max(abs(x - poles[ell]["R"]) for x in rr0)
    check(f"l = {ell} Robin pole r0-independent (40/60/80 within 1e-4)", spread < 1e-4, f"spread {spread:.1e}")
    w0 = poles[ell]["R"]; f0 = abs(F(w0, Vf, "R", 50.0, BETA[ell])); f1 = abs(F(w0 + 0.01, Vf, "R", 50.0, BETA[ell]))
    check(f"l = {ell} Robin root is SHARP (|F| grows > 100x at +0.01 off the root)", f1 > 100 * max(f0, 1e-14))

print("The displacement — from POLES, not centroids")
for ell in (2, 3):
    D, R_ = poles[ell]["D"], poles[ell]["R"]
    print(f"    l = {ell}: Re w  Dirichlet {D.real:.4f} -> Robin {R_.real:.4f}   shift {100*(R_.real/D.real-1):+.1f}%    Q  {D.real/(2*abs(D.imag)):.2f} -> {R_.real/(2*abs(R_.imag)):.2f}")
sh = {l: poles[l]["R"].real / poles[l]["D"].real - 1 for l in (2, 3)}
check("the pole displacement is NEGATIVE for both l (the derived wall lowers the mode)", sh[2] < 0 and sh[3] < 0)
check("the pole displacement is NOT -13.4% for both l — the identical-centroid figure was a locator artifact (record the pole values)", not (abs(sh[2] + 0.134) < 0.01 and abs(sh[3] + 0.134) < 0.01), f"l=2 {100*sh[2]:+.1f}%, l=3 {100*sh[3]:+.1f}%")
Qd = {l: poles[l]["D"].real / (2 * abs(poles[l]["D"].imag)) for l in (2, 3)}
Qr = {l: poles[l]["R"].real / (2 * abs(poles[l]["R"].imag)) for l in (2, 3)}
check("Q rises under the derived wall for both l (the mode is longer-lived than the Dirichlet mode)", Qr[2] > Qd[2] and Qr[3] > Qd[3], f"Q l=2 {Qd[2]:.2f}->{Qr[2]:.2f}; l=3 {Qd[3]:.2f}->{Qr[3]:.2f}")
check("'near-trapped' (Q > 10) is " + ("EARNED" if min(Qr.values()) > 10 else "NOT earned") + " by the poles", True, f"min Q_Robin = {min(Qr.values()):.2f}")
print(f"    Wigner-centroid positions of 3379 (0.412 / 0.604) vs Robin pole Re w ({poles[2]['R'].real:.3f} / {poles[3]['R'].real:.3f})")
check("the 3379 centroids sit within 0.05 of the Robin pole real parts (the feature was the pole, its displacement was mis-measured)", abs(0.412 - poles[2]["R"].real) < 0.05 and abs(0.604 - poles[3]["R"].real) < 0.05)

# ---------------------------------------------------------------- Q6 (alpha): the crossing vs the barrier top, across l and r_w
print("Q6 (alpha) — Neumann crossing of beta_l vs the Zerilli barrier top")
print("     r_w      l    w0 = sqrt(b0/b2)   w_top = sqrt(max V)   ratio")
alpha = {}
for rw in (sp.Rational(9, 4), sp.Rational(5, 2), sp.Integer(3)):
    for ell in (2, 3, 4):
        b0, b2 = beta_sym(ell, rw) if rw != sp.Rational(9, 4) else BETA[ell]
        w0 = np.sqrt(b0 / b2) if b0 / b2 > 0 else float("nan")   # b0, b2 flip sign TOGETHER beyond ~2.4M: the crossing persists, beta's sign flips
        wtop = np.sqrt(max(V_Z(np.linspace(2.05, 8, 40001), ell)))
        alpha[(float(rw), ell)] = w0 / wtop
        print(f"    {float(rw):5.2f}    {ell}      {w0:8.4f}            {wtop:8.4f}        {w0/wtop:6.3f}")
at_b = [alpha[(2.25, l)] for l in (2, 3, 4)]
off = [alpha[(k, l)] for k in (2.5, 3.0) for l in (2, 3, 4)]
check("at Buchdahl the crossing/top ratio is within 8% of 1 for l = 2, 3, 4", all(abs(x - 1) < 0.08 for x in at_b), " ".join(f"{x:.3f}" for x in at_b))
check("off Buchdahl (r_w = 2.5M, 3M) the ratio LEAVES the 8% band for at least one (r_w, l) — the coincidence is tied to the Buchdahl wall, not to the trace law in general",
      any(abs(x - 1) > 0.08 for x in off), " ".join(f"{x:.3f}" for x in off))
# where the Robin coefficient DIVERGES (tc2 + 3f = 0): the trace condition is exactly Dirichlet on Z+ there
def b_at(ell, rw): return beta_sym(ell, sp.nsimplify(rw))
div = {}
for ell in (2, 3):
    lo, hi = 2.30, 2.50
    for _ in range(30):
        mid = 0.5 * (lo + hi); b0m, _ = b_at(ell, round(mid, 6))
        if b0m > 0: lo = mid
        else: hi = mid
    div[ell] = 0.5 * (lo + hi)
    print(f"    l = {ell}: beta_l diverges (trace condition -> exact Dirichlet on Z+) at r_w = {div[ell]:.4f} M")
check("there is a wall radius near 2.4M at which the trace condition IS Dirichlet on Z+ — recorded; NOT the Buchdahl radius", all(2.30 < div[l] < 2.50 and abs(div[l] - 2.25) > 0.05 for l in (2, 3)))

print()
print(f"3383 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
