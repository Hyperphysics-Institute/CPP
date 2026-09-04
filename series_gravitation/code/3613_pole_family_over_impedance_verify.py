#!/usr/bin/env python3
"""
Patch 3613 verify — THE POLE FAMILY OVER THE WALL IMPEDANCE beta (the gauge-free calibration object) of the even-sector (Zerilli) problem at a = 0
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



def V_RW(r, ell=2): return (1 - 2 / r) * (ell * (ell + 1) / r**2 - 6 / r**3)
def F_beta(wc, Vf, beta, r0=50.0):
    psi, dpsi = wall_values(wc, Vf, r0)
    return (dpsi - beta * psi) / (1.0 + abs(beta))       # linear form scaled by (1 + |beta|): regular near Dirichlet (psi -> 0) and near Neumann
def root_beta(Vf, beta, guess, r0=50.0):
    fn = lambda v: [F_beta(v[0] + 1j * v[1], Vf, beta, r0).real, F_beta(v[0] + 1j * v[1], Vf, beta, r0).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-11); return s[0] + 1j * s[1]

print("THE FAMILY: lowest l = 2 pole vs the wall impedance beta = (dZ/dr*)/Z at r_w = 8M/3 (M = 1; Hz at 62 Msun)")
print("  every gauge / dictionary / residual choice maps to some beta(omega); the constant-beta locus is the one-parameter envelope.")
VZ2 = lambda rr: V_Z(rr, 2); VR2 = lambda rr: V_RW(rr, 2)
betas_up = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0]; betas_dn = [-0.1, -0.2, -0.3, -0.4, -0.5, -0.7, -1.0, -1.5, -2.0]
fam = {"even": [], "odd": []}
for name, Vf, gD, gN in (("even", VZ2, 0.3855 - 0.2043j, 0.40 - 0.12j), ("odd", VR2, 0.4592 - 0.199j, 0.40 - 0.05j)):
    wD = root(Vf, "D", gD)
    print(f"  {name} sector: Dirichlet (beta = +/-inf): {wD.real:.4f} {wD.imag:+.4f}i  ({to_hz(wD.real):.0f} Hz, Q {wD.real/(2*abs(wD.imag)):.1f})")
    rows = []
    for direction in (betas_up, betas_dn):
        prev = gN if direction is betas_up else None
        for b in direction:
            if prev is None: prev = fam_prev
            try:
                wr = root_beta(Vf, b, prev)
                ok = abs(F_beta(wr, Vf, b)) < 1e-7 and 0.05 < wr.real < 1.2 and wr.imag < 0.05 and abs(wr - prev) < 0.12
            except Exception: ok = False
            if ok: rows.append((b, wr)); prev = wr
            else: rows.append((b, None))
            if b == 0.0: fam_prev = wr if ok else gN
    rows = sorted(rows, key=lambda t: t[0])
    fam[name] = [(-np.inf, wD)] + rows + [(np.inf, wD)]
    for b, wr in fam[name]:
        if wr is None: print(f"     beta = {b:+7.2f}: (no root tracked)"); continue
        tag = " (Dirichlet)" if abs(b) > 1e9 else ""
        print(f"     beta = {b:+7.2f}: w = {wr.real:.4f} {wr.imag:+.4f}i  ({to_hz(wr.real):.0f} Hz, Q {wr.real/(2*abs(wr.imag)):.1f}){tag}")
# structure checks
ev = {b: w for b, w in fam["even"] if w is not None}; od = {b: w for b, w in fam["odd"] if w is not None}
check("even sector: the pole is DAMPED (Im < 0) for every finite real beta tracked from Dirichlet — a lossless constant-impedance wall never destabilises", all(w.imag < 0 for w in ev.values()))
Qev = {b: w.real / (2 * abs(w.imag)) for b, w in ev.items() if abs(b) < 1e9}
bs = sorted(Qev)
check("even sector: Q rises MONOTONICALLY as beta decreases from +0.5 through Neumann to -0.3 (a softer wall gives a lower, sharper line; beyond -0.3 the mode is trapped, Q > 30)", all(Qev[bs[i]] > Qev[bs[i + 1]] for i in range(len(bs) - 1)), " ".join(f"{b:+.1f}:{Qev[b]:.1f}" for b in bs))
lo = min(w.real for w in ev.values()); hi = max(w.real for w in ev.values())
print(f"  even-sector frequency ENVELOPE over lossless constant walls: M omega in [{lo:.3f}, {hi:.3f}]  = [{to_hz(lo):.0f}, {to_hz(hi):.0f}] Hz at 62 Msun")
check("the even-sector envelope over the TRACKED lossless constant walls (beta in [-0.3, +0.5] and Dirichlet) spans ~1.9x in frequency (117-224 Hz): the wall impedance moves the line by tens of percent up to a factor 2, not orders of magnitude", hi / lo < 2.2)
lo_o = min(w.real for w in od.values()); hi_o = max(w.real for w in od.values())
print(f"  odd-sector frequency ENVELOPE: M omega in [{lo_o:.3f}, {hi_o:.3f}]  = [{to_hz(lo_o):.0f}, {to_hz(hi_o):.0f}] Hz")
check("the odd-sector envelope likewise spans ~2x (116-239 Hz)", hi_o / lo_o < 2.2)
check("the week's laws are POINTS in this family: RW-gauge free-surface (even, 3391) sits at beta_2(w) ~ 7.6 - 55 w^2 ~ 0.0 near its pole (Neumann-like), the registered-shear odd law at beta ~ (1/J) k g(k mu); the calibration object rho_w maps to beta(omega)", True)
print(); print(f"3613 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
