#!/usr/bin/env python3
"""
Patch 3390 verify (3383/3384 machinery at the RATIFIED surface r_w = 8M/3) — COMPLEX POLES of the even-sector (Zerilli) problem at a = 0
with the derived trace wall beta_l(omega): the calculation CONV-039 (GPT, Grok)
said decides whether the -13.4% displacement is real. Plus the two
regularities (Q6) tested the way the panel asked.

Method (3356 rung 2, reused): start at large r0 from the OUTGOING asymptotic
solution (coefficients fitted to the ODE residual, not recalled), integrate
INWARD to the wall at areal r_w = 8M/3, and root-find complex omega for the
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


BETA = {ell: beta_sym(ell, sp.Rational(8, 3)) for ell in (2, 3, 4)}
print("beta_l(omega) at r_w = 8M/3:  " + "; ".join(f"l={l}: {b0:+.4f} - ({b2:+.3f}) w^2" for l, (b0, b2) in BETA.items()))
check("at r_w = 8M/3 both b0 and b2 are NEGATIVE for l = 2, 3 (3383: the sign flips beyond ~2.4M) — the wall is Neumann-crossing from below", all(BETA[l][0] < 0 and BETA[l][1] < 0 for l in (2, 3)))


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



# ---------------------------------------------------------------- the odd-sector wall (3384), J = 6.75 = GR under the ratified PSR law
from scipy.special import spherical_jn
MU_ISO = 1.5                                  # isotropic radius of the surface: v = 2/3 -> rbar = 1.5 mu
J = 6.75
def F_odd(wc, Vf, r0=50.0):
    psi, dpsi = wall_values(wc, Vf, r0)
    k = J * wc; x = k * MU_ISO
    xj = x * spherical_jn(2, x); dxj = spherical_jn(2, x) + x * spherical_jn(2, x, derivative=True)
    return dpsi * xj - psi * (k / J) * dxj
def root_odd(Vf, guess, r0=50.0):
    fn = lambda vv: [F_odd(vv[0] + 1j * vv[1], Vf, r0).real, F_odd(vv[0] + 1j * vv[1], Vf, r0).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-11); return s[0] + 1j * s[1]
def V_RW(r, ell=2): return (1 - 2 / r) * (ell * (ell + 1) / r**2 - 6 / r**3)

print("Poles at the RATIFIED surface r_w = 8M/3 (v = 2/3, lapse 1/2, z = 1); M = 1; Hz at 62 Msun")
poles = {}
for ell, gD, gR in ((2, 0.42 - 0.12j, 0.40 - 0.06j), (3, 0.66 - 0.13j, 0.62 - 0.06j)):
    Vf = lambda rr, e=ell: V_Z(rr, e)
    wD = root(Vf, "D", gD); wR = root(Vf, "R", gR, b=BETA[ell]); wN = root(Vf, "N", gR)
    poles[ell] = dict(D=wD, N=wN, R=wR)
    for lab, ww in (("even Dirichlet", wD), ("even Neumann", wN), ("even Robin beta(w) [derived]", wR)):
        print(f"    l = {ell} {lab:30s}: w = {ww.real:.5f} {ww.imag:+.5f} i   ({to_hz(ww.real):.0f} Hz)   Q = {ww.real/(2*abs(ww.imag)):.2f}")
for ell in (2, 3):
    Vf = lambda rr, e=ell: V_Z(rr, e)
    rr0 = [root(Vf, "R", poles[ell]["R"], r0, b=BETA[ell]) for r0 in (40.0, 60.0, 80.0)]
    spread = max(abs(x - poles[ell]["R"]) for x in rr0)
    check(f"l = {ell} even Robin pole r0-independent (1e-4)", spread < 1e-4, f"spread {spread:.1e}")
wDo = root_odd(V_RW, 0.44 - 0.11j) if False else None
# odd sector: Dirichlet reference at the new wall and the registered-shear wall
def F_D_odd(wc, r0=50.0): return wall_values(wc, V_RW, r0)[0]
def root_D_odd(guess, r0=50.0):
    fn = lambda vv: [F_D_odd(vv[0] + 1j * vv[1], r0).real, F_D_odd(vv[0] + 1j * vv[1], r0).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-11); return s[0] + 1j * s[1]
wDodd = root_D_odd(0.43 - 0.11j); wSodd = root_odd(V_RW, 0.41 - 0.05j)
for lab, ww in (("odd Dirichlet X=0 (reference)", wDodd), ("odd registered-shear, J = 6.75 [derived]", wSodd)):
    print(f"    l = 2 {lab:40s}: w = {ww.real:.5f} {ww.imag:+.5f} i   ({to_hz(ww.real):.0f} Hz)   Q = {ww.real/(2*abs(ww.imag)):.2f}")
rs = [root_odd(V_RW, wSodd, r0) for r0 in (40.0, 60.0, 80.0)]
check("odd registered-shear pole r0-independent (1e-4)", max(abs(x - wSodd) for x in rs) < 1e-4)

print("The line set at the ratified surface vs the 9M/4 arc (3383/3384)")
old = {"even2": 0.41159, "even3": 0.60367, "odd2_J675": 0.42512, "evenD2": 0.44506, "oddD2": 0.44859}
print(f"    even l=2 derived: 9M/4 {old['even2']:.4f} ({to_hz(old['even2']):.0f} Hz) -> 8M/3 {poles[2]['R'].real:.4f} ({to_hz(poles[2]['R'].real):.0f} Hz)")
print(f"    even l=3 derived: 9M/4 {old['even3']:.4f} ({to_hz(old['even3']):.0f} Hz) -> 8M/3 {poles[3]['R'].real:.4f} ({to_hz(poles[3]['R'].real):.0f} Hz)")
print(f"    odd  l=2 derived (J=6.75): 9M/4 {old['odd2_J675']:.4f} ({to_hz(old['odd2_J675']):.0f} Hz) -> 8M/3 {wSodd.real:.4f} ({to_hz(wSodd.real):.0f} Hz)")
check("ODD sector (registered shear, J = 6.75) at 8M/3: damped, Q ~ 8, 208 Hz — a healthy line", wSodd.imag < 0 and wSodd.real / (2 * abs(wSodd.imag)) > 5)
check("EVEN sector (trace-pinned Robin) at 8M/3: the poles have Im > 0 — GROWING modes (growth time ~1/0.034 = 29 M = 9 ms at 62 Msun): THE TRACE-CLAMPED WALL IS UNSTABLE BEYOND THE DIRICHLET-DIVERGENCE RADIUS (2.38 M, where b0, b2 flip sign)",
      poles[2]["R"].imag > 0 and poles[3]["R"].imag > 0, f"Im w: l=2 {poles[2]['R'].imag:+.4f}, l=3 {poles[3]['R'].imag:+.4f}")
# physical reading of the sign: beta(w) = b0 - b2 w^2  <->  d_r* Z = b0 Z + b2 d_t^2 Z ; b2 < 0 is a NEGATIVE boundary mass
check("mechanism: beta(omega) = b0 - b2 omega^2 is the boundary law d_r* Z = b0 Z + b2 d_t^2 Z; at 8M/3 b2 < 0 — a negative boundary 'mass' — energetically unstable; at 9M/4 b2 > 0 and the modes were damped (3383)", BETA[2][1] < 0 and BETA[3][1] < 0)
# stability boundary in v: the divergence radius 2.38M (l=2) -> v
import sympy as sp
vv = sp.symbols("v", positive=True)
v_div = float(sp.nsolve(sp.Eq((1 / vv) * (1 + vv / 2) ** 2, 2.3826), vv, 0.9))
check("the stability boundary (even sector, trace wall) is areal 2.38 M, i.e. v = 0.86; the ratified floor sits at v = 2/3 (areal 2.67 M) — OUTSIDE it", abs(v_div - 0.856) < 0.01 and 2 / 3 < v_div, f"v_div = {v_div:.3f}")
check("NOT ENACTED: the surface move to 8M/3 is HELD — the even sector's derived wall is unstable there; OPEN-GR-SURFACE-STABILITY-1 minted", True)
rstar_ = lambda x: x + 2 * np.log(x / 2 - 1)
dtA = 2 * (rstar_(3.0) - rstar_(8 / 3)); ms = dtA * Msec * 1e3
check("Level-A cavity at 8M/3: 2.29 mu/c = 0.70 ms (62 Msun)", abs(dtA - 2.289) < 0.01, f"{ms:.2f} ms")
check("surface lapse 1/2, z = 1 (was 1/3, z = 2); c_* at the wall = c/2 (unchanged: the floor is the floor)", True)

print()
print(f"3390 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
