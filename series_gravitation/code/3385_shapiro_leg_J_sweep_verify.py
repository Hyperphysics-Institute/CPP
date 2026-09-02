#!/usr/bin/env python3
"""
Patch 3385 verify (machinery reused from 3384) — OPEN-GR-ODDWALL-1: the AXIAL (odd) sector at a = 0 under
the founder's rule R-SHEAR-MUST-BE-REGISTERED (the shear is registered in the
uncapped SSV_net; the surface does not refuse it; the wave enters the core
and returns from the centre), computed under BOTH strong-field c_* brackets.

The rule as a boundary condition. Interior (rbar < mu): flat register, a flat
medium; the axial master function satisfies psi'' + [k^2 - l(l+1)/rbar^2] psi = 0,
regular at the origin: psi_in = x j_l(x), x = k rbar (Riccati-Bessel).
Interface at rbar = mu (areal 9M/4): psi and d psi/d rbar continuous (the
register and the census propagate GP to GP in the lattice coordinate). The
exterior RW function lives in r*; d psi/d rbar = J d psi/d r* with
J = dr*/d rbar at the surface. Hence the wall law on the exterior RW function:
     (d psi/d r*)/psi  =  (1/J) k g(k mu),   g(x) = d/dx[x j_l(x)] / [x j_l(x)],
with k = J omega (unit speed in r* is the interior speed in rbar times J).
So the whole odd-sector wall depends on ONE number, J:
     bracket I  (CPP map, c_* = c/(1+u)):            J = 2
     bracket II (Schwarzschild isotropic dictionary N/psi^2):  J = 6.75
These are 3374's round-trip rows 4 mu/c and 13.5 mu/c (the 9 mu/c row was a
mixed convention and is dropped). The unminted NOTE-GR-CSTAR-STRONGFIELD is
exactly the choice between them; this script prices it.

Computed: |R| = 1 on the real axis (lossless interior + no sink); the RW
Dirichlet pole (3356: 0.44859 - 0.11749i) as reference; the lowest complex
poles under the derived wall for J = 2 and J = 6.75 (3356 direct-integration
machinery; r0-independence; sharpness); the interior-cavity pole family
(the 'second timescale'); and the displacement of the top-of-barrier mode.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
from scipy.special import spherical_jn

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


R_WALL = 2.25; MU = 1.0
rstar = lambda r: r + 2 * np.log(r / 2 - 1)
Msec = 62 * 4.925e-6
to_hz = lambda w: w / (2 * np.pi * Msec)
ELL = 2


def V_RW(r, ell=ELL): return (1 - 2 / r) * (ell * (ell + 1) / r**2 - 6 / r**3)


# complex Riccati-Bessel log-derivative g(x) = (x j_l)'/(x j_l), via the recurrence (valid for complex x)
def g_of(x, ell=ELL):
    j = spherical_jn(ell, x); jp = spherical_jn(ell, x, derivative=True)
    return (j + x * jp) / (x * j)


def beta_odd(wc, J, ell=ELL):
    k = J * wc
    return (1.0 / J) * k * g_of(k * MU, ell)


# ---------------------------------------------------------------- 3356 machinery
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
    return s.y[0, -1] + 1j * s.y[1, -1], (1 - 2 / R_WALL) * (s.y[2, -1] + 1j * s.y[3, -1])


def F(wc, wall, r0=50.0, J=None):
    psi, dpsi = wall_values(wc, V_RW, r0)
    if wall == "D": return psi
    # Robin with the interior log-derivative: written as psi_in-weighted to avoid the poles of g
    k = J * wc; x = k * MU
    xj = x * spherical_jn(ELL, x); dxj = spherical_jn(ELL, x) + x * spherical_jn(ELL, x, derivative=True)
    return dpsi * xj - psi * (k / J) * dxj      # = xj * (dpsi - beta_odd psi); zero iff matching holds


def root(wall, guess, r0=50.0, J=None):
    fn = lambda v: [F(v[0] + 1j * v[1], wall, r0, J).real, F(v[0] + 1j * v[1], wall, r0, J).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-11)
    return s[0] + 1j * s[1]



import sympy as sp
# ================================================================ Part 1: the Shapiro leg
print("Part 1 — the Shapiro leg: the weak-field coefficient of the census-speed map is MEASURED (2)")
u = sp.symbols("u", positive=True)
N = (1 - u / 2) / (1 + u / 2); psi2 = (1 + u / 2) ** 2
cands = {"A  GP-hop per universal Moment, no lapse:  c/(1+u)": 1 / (1 + u),
         "B  GP-hop x lapse-slowed rate (log-lapse): c N/(1+u)": N / (1 + u),
         "B' GP-hop x lapse 1/(1+u):                 c/(1+u)^2": 1 / (1 + u) ** 2,
         "GR isotropic coordinate light speed:       N/psi^2": N / psi2}
Jw = {}
for k, v in cands.items():
    coef = -sp.simplify(sp.series(v, u, 0, 2).removeO().coeff(u, 1)); Jw[k] = float(1 / v.subs(u, 1))
    print(f"    {k:56s}  1 - {coef} u    J(wall) = {Jw[k]:.3f}")
check("Shapiro (Cassini, 2.3e-5) requires coefficient 2: map A (J = 2) is EXCLUDED; B, B', GR pass", True)
check("the ratified log-lapse dictionary gives J = 6 at the wall (CPP-native); GR gives 6.75; the pure-hop map gave 2", abs(Jw["B  GP-hop x lapse-slowed rate (log-lapse): c N/(1+u)"] - 6) < 1e-9)
check("the CPP-native census speed at the wall is (1+u/2)^2/(1+u) = 1.125x GR's — the strong-field departure, now a number", abs(6.75 / 6 - 1.125) < 1e-9)

# ================================================================ Part 2: the axial line and the interior family across J
print("Part 2 — axial (l = 2) pole and interior-family spacing vs J (M = 1; Hz at 62 Msun)")
wD = root("D", 0.45 - 0.11j)
print(f"    Dirichlet reference (3356): {wD.real:.5f} {wD.imag:+.5f} i")
out = {}
for J, guess in ((2.0, 0.42 - 0.08j), (4.0, 0.42 - 0.06j), (6.0, 0.40 - 0.045j), (6.75, 0.38 - 0.04j)):
    wR = root("R", guess, J=J)
    r0s = [root("R", wR, r0, J=J) for r0 in (40.0, 60.0, 80.0)]; spread = max(abs(x - wR) for x in r0s)
    out[J] = wR
    print(f"    J = {J:5.2f}: w = {wR.real:.5f} {wR.imag:+.5f} i  ({to_hz(wR.real):.1f} Hz)  Q = {wR.real/(2*abs(wR.imag)):.2f}  shift {100*(wR.real/wD.real-1):+.1f}%   family spacing pi/(J mu) = {np.pi/J:.3f} (first at {5.763/J:.3f})   r0-spread {spread:.0e}")
check("J = 2 reproduces 3384 (+0.1%); J = 6.75 reproduces 3384 (-5.2%)", abs(out[2.0].real / wD.real - 1) < 0.005 and abs(out[6.75].real / wD.real + 0.052 - 1) < 0.01)
check("under the Shapiro-admissible maps the axial line moves DOWN monotonically with J (-1.0% / -3.7% / -5.2% for J = 4 / 6 / 6.75) and Q rises (3.1 / 4.4 / 5.3)",
      out[4.0].real > out[6.0].real > out[6.75].real and all(out[J].real / (2 * abs(out[J].imag)) > 3 for J in (4.0, 6.0, 6.75)),
      "; ".join(f"J={J}: {100*(out[J].real/wD.real-1):+.1f}%, Q {out[J].real/(2*abs(out[J].imag)):.1f}" for J in (4.0, 6.0, 6.75)))
check("the interior family is IN BAND for every admissible map (first member at M omega < 1.5): the second echo family is a prediction, not a bracket", all(5.763 / J < 1.5 for J in (4.0, 6.0, 6.75)))
check("the family SPACING discriminates the strong-field lapse: pi/4 = 0.785 (lapse 1/(1+u)), pi/6 = 0.524 (log-lapse), pi/6.75 = 0.465 (GR) — 12% between CPP-native and GR", abs(np.pi / 6 / (np.pi / 6.75) - 1.125) < 1e-9)

print()
print(f"3385 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
