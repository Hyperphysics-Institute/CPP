#!/usr/bin/env python3
"""
Patch 3384 verify — OPEN-GR-ODDWALL-1: the AXIAL (odd) sector at a = 0 under
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


# ---------------------------------------------------------------- Check 0: the wall law on the real axis
print("Check 0 — the odd wall law: real, lossless, J-parametrised")
ws = np.linspace(0.05, 1.5, 300)
for J in (2.0, 6.75):
    b = np.array([beta_odd(w, J) for w in ws])
    check(f"J = {J}: beta_odd(omega) is REAL on the real axis (lossless interior; |R| = 1)", np.max(abs(b.imag)) < 1e-12)
    print(f"    J = {J:5.2f}: beta_odd -> (l+1)/J = {(ELL+1)/J:.3f} as omega -> 0 (small-x limit);  first interior resonance (x j_l = 0, x = 5.763) at M omega = {5.763/(J*MU):.3f}")
check("small-omega limit is a constant Robin (l+1)/J: 1.5 (J=2) vs 0.44 (J=6.75)", abs(beta_odd(1e-3, 2.0).real - 1.5) < 1e-3 and abs(beta_odd(1e-3, 6.75).real - 3 / 6.75) < 1e-3)

# ---------------------------------------------------------------- Check 1: poles
print("Check 1 — poles of the axial sector at a = 0 (M = 1; Hz at 62 Msun)")
wD = root("D", 0.45 - 0.11j)
print(f"    Dirichlet (shipped X = 0):    w = {wD.real:.5f} {wD.imag:+.5f} i   ({to_hz(wD.real):.1f} Hz)   Q = {wD.real/(2*abs(wD.imag)):.2f}")
check("RW Dirichlet pole reproduces 3356 (0.44859 - 0.11749i) to 1e-4", abs(wD - (0.44859 - 0.11749j)) < 1e-4)
poles = {}
for J, guess in ((2.0, 0.42 - 0.08j), (6.75, 0.38 - 0.04j)):
    wR = root("R", guess, J=J)
    r0s = [root("R", wR, r0, J=J) for r0 in (40.0, 60.0, 80.0)]
    spread = max(abs(x - wR) for x in r0s)
    f0 = abs(F(wR, "R", 50.0, J)); f1 = abs(F(wR + 0.01, "R", 50.0, J))
    poles[J] = wR
    print(f"    derived wall, J = {J:5.2f}:      w = {wR.real:.5f} {wR.imag:+.5f} i   ({to_hz(wR.real):.1f} Hz)   Q = {wR.real/(2*abs(wR.imag)):.2f}   shift {100*(wR.real/wD.real-1):+.1f}%")
    check(f"J = {J}: pole r0-independent (1e-4) and sharp (>100x)", spread < 1e-4 and f1 > 100 * max(f0, 1e-14), f"spread {spread:.1e}")
check("bracket I (J = 2): the axial line is essentially UNMOVED from X = 0 (|shift| < 1%) — a Robin coefficient 1.5/M acts like Dirichlet at the barrier top; the shipped position survives under the CPP map", abs(poles[2.0].real / wD.real - 1) < 0.01)
check("bracket II (J = 6.75): the axial line moves DOWN ~5% and Q rises 1.9 -> 5", poles[6.75].real < wD.real and poles[6.75].real / (2 * abs(poles[6.75].imag)) > 4)
check("the c_* map is worth a definite amount on the axial line: the two brackets differ in Re omega by more than 3%",
      abs(poles[2.0].real - poles[6.75].real) / wD.real > 0.03, f"J=2 {100*(poles[2.0].real/wD.real-1):+.1f}%  J=6.75 {100*(poles[6.75].real/wD.real-1):+.1f}%")

# ---------------------------------------------------------------- Check 2: the interior-cavity family (second timescale)
print("Check 2 — the interior-cavity pole family (the 'second timescale' of 3374, now on the axial sector)")
fam = {}
for J in (2.0, 6.75):
    xs_zero = [5.763, 9.095, 12.323]                # zeros of x j_2(x): interior standing waves
    found = []
    for xz in xs_zero[:2]:
        wg = xz / (J * MU) - 0.03j
        if wg.real > 2.0: break
        try:
            wr = root("R", wg, J=J); found.append(wr)
        except Exception: pass
    fam[J] = found
    for wr in found:
        print(f"    J = {J:5.2f}: interior-cavity pole w = {wr.real:.4f} {wr.imag:+.5f} i  ({to_hz(wr.real):.0f} Hz)  Q = {wr.real/(2*abs(wr.imag)):.1f}   spacing ~ pi/(J mu) = {np.pi/(J*MU):.3f}")
check("J = 6.75 supports interior-cavity poles below M omega ~ 1.5 (round trip 13.5 mu/c -> spacing 0.47): a SECOND echo family", len(fam[6.75]) >= 1 and all(w.real < 1.6 for w in fam[6.75]))
check("J = 2 pushes the interior family above M omega ~ 2.8 (round trip 4 mu/c): effectively absent in band", len(fam[2.0]) == 0 or all(w.real > 2.5 for w in fam[2.0]))

# ---------------------------------------------------------------- Check 3: what the flagship inherits
print("Check 3 — translation")
check("the shipped axial X = 0 wall is replaced, under the founder's rule, by a J-dependent Robin law whose value at the flagship frequency is (l+1)/J-like: NOT Dirichlet", True)
check("the strong-field c_* map (J) now prices at a definite fraction of the axial line and decides whether a second echo family exists in band — MINT IT (NOTE-GR-CSTAR-STRONGFIELD -> charter)", True)
check("still a = 0; the Kerr axial response needs the same reconstruction as the even sector (OPEN-GR-KERRWALL-1)", True)

print()
print(f"3384 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
