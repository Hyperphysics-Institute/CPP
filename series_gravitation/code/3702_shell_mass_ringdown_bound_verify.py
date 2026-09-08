#!/usr/bin/env python3
"""
Patch 3702 verify — AP-5 owed item 2 reframed: THE RINGDOWN BOUNDS THE VISIBLE SHELL'S MASS, hence its tidal response.
The 3675 ringdown result continued Schwarzschild(M) from 8M/3 to the wave horizon; that requires the enclosed demand
to be ~M throughout the visible shell (areal 2M -> 8M/3). If a mass fraction mu = M_s/M sits in the shell, the sea's
potential there is weaker and the (2,2) pole shifts. Proxy interior (indicative, not exact): m(r) = M(1-mu) for
r <= r_a = 2.2M, rising linearly to M at R = 8M/3; Zerilli-type potential with M -> m(r), f = 1 - 2m(r)/r; ingoing
at r_+ = 2M(1-mu); matched to the exterior outgoing solution at 8M/3. M = 1.
 T1  mu = 0 reproduces Leaver's l = 2 pole (machinery = 3675).
 T2  Sweep mu in {0.02, 0.05, 0.1, 0.2, 0.3}: df/f and dtau/tau vs GW150914's box (+6.3 %/-4.8 % in f; +24 %/-22 % in tau).
 T3  The largest mu inside the box -> mu_max; the shell's tidal response scales ~ linearly with responding mass at
     fixed radius, so Lambda-tilde(shell) <~ mu_max x 1.7 (estimate-grade scaling of the 3685 full-body bound).
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
PASS = FAIL = 0
def check(n, c, d=""):
    global PASS, FAIL; ok = bool(c); PASS += ok; FAIL += (not ok); print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  — {d}" if d else ""))
R_WALL = 8 / 3; RA = 2.2; ELL = 2
def m_of(r, mu):
    if r <= RA: return 1 - mu
    return 1 - mu + mu * (r - RA) / (R_WALL - RA)
def V_Z(r, m):
    n = (ELL - 1) * (ELL + 2) / 2
    num = 2 * n * n * (n + 1) * r**3 + 6 * n * n * m * r**2 + 18 * n * m * m * r + 18 * m**3
    return (1 - 2 * m / r) * num / (r**3 * (n * r + 3 * m) ** 2)
def rstar_ext(r): return r + 2 * np.log(r / 2 - 1)
def outgoing_start(wc, r0, nterms=8):
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0; rs = np.linspace(r0, 4 * r0, 40)
    def pd(cc, rr):
        f = 1 - 2 / rr
        S = sum(cc[k] / rr**k for k in range(len(cc))); dS = sum(-k * cc[k] / rr**(k + 1) for k in range(len(cc)))
        d2S = sum(k * (k + 1) * cc[k] / rr**(k + 2) for k in range(len(cc))); e = np.exp(1j * wc * rstar_ext(rr))
        return (e * S, e * (1j * wc / f * S + dS), e * ((1j * wc / f) ** 2 * S + 2 * (1j * wc / f) * dS + d2S - 1j * wc * (2 / rr**2) / f**2 * S))
    def resid(cc):
        out = []
        for rr in rs:
            f = 1 - 2 / rr; fp = 2 / rr**2; p, dp, d2p = pd(cc, rr)
            out.append((f * f * d2p + f * fp * dp + (wc * wc - V_Z(rr, 1.0)) * p) / np.exp(1j * wc * rstar_ext(rr)))
        return np.array(out)
    A = np.zeros((len(rs), nterms - 1), dtype=complex); base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0; A[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(A, -base, rcond=None)[0]; p, dp, _ = pd(c, r0); return p, dp
def integrate(wc, mu, r_from, r_to, p0, dp0):
    def rhs(rr, y):
        m = m_of(rr, mu); dm = 0.0 if rr <= RA else mu / (R_WALL - RA)
        f = 1 - 2 * m / rr; fp = 2 * m / rr**2 - 2 * dm / rr
        psi = y[0] + 1j * y[1]; dpsi = y[2] + 1j * y[3]
        d2 = -(f * fp * dpsi + (wc * wc - V_Z(rr, m)) * psi) / (f * f)
        return [dpsi.real, dpsi.imag, d2.real, d2.imag]
    s = solve_ivp(rhs, [r_from, r_to], [p0.real, p0.imag, dp0.real, dp0.imag], rtol=1e-10, atol=1e-12, method="DOP853")
    return s.y[0, -1] + 1j * s.y[1, -1], s.y[2, -1] + 1j * s.y[3, -1]
def ingoing_start(wc, mu, eps=1e-5):
    mc = 1 - mu; rp = 2 * mc; s = -2j * wc * mc   # (r - r+)^{-i w r+ ... } : exponent -2 i w m_c (surface gravity 1/(4 m_c))
    r = rp + eps; x = r - rp
    Z = x**s; dZ = s / x * Z
    return r, Z, dZ
def wronskian(wc, mu, r0=40.0):
    po, dpo = outgoing_start(wc, r0)
    Zo, dZo = integrate(wc, 0.0, r0, R_WALL, po, dpo)           # exterior: vacuum M
    ri, Zi, dZi = ingoing_start(wc, mu)
    Zi2, dZi2 = integrate(wc, mu, ri, R_WALL, Zi, dZi)
    W = Zo * dZi2 - dZo * Zi2
    return W / (abs(Zo) * abs(Zi2) + 1e-300)
def pole(mu, w0):
    F = lambda v: (lambda W: [W.real, W.imag])(wronskian(v[0] + 1j * v[1], mu))
    s = fsolve(F, [w0.real, w0.imag], xtol=1e-10); return s[0] + 1j * s[1]
LEAVER = 0.37367 - 0.08896j
print("T1 — mu = 0")
w0 = pole(0.0, LEAVER); print(f"    pole {w0.real:.5f} {w0.imag:+.5f} i (Leaver {LEAVER.real:.5f} {LEAVER.imag:+.5f} i)")
check("T1 machinery reproduces Leaver at mu = 0 (< 0.1 %)", abs(w0.real / LEAVER.real - 1) < 1e-3 and abs(w0.imag / LEAVER.imag - 1) < 1e-3)
print("\nT2 — sweep the shell mass fraction")
box_f = (-0.048, 0.063); box_tau = (-0.22, 0.24)
mu_max = 0.0; res = []
for mu in (0.02, 0.05, 0.1, 0.2, 0.3):
    w = pole(mu, w0); df = w.real / w0.real - 1; dtau = w0.imag / w.imag - 1
    inside = box_f[0] < df < box_f[1] and box_tau[0] < dtau < box_tau[1]
    res.append((mu, df, dtau, inside)); mu_max = mu if inside else mu_max
    print(f"    mu = {mu:.2f}: df/f = {df*100:+6.2f} %, dtau/tau = {dtau*100:+6.1f} %  {'inside' if inside else 'OUTSIDE'} the GW150914 box")
check("T2 pole moves monotonically with mu (|df| increasing)", all(abs(res[i+1][1]) >= abs(res[i][1]) for i in range(len(res)-1)))
print(f"\nT3 — bound: mu_max (GW150914 box) = {mu_max:.2f};  Lambda-tilde(shell) <~ mu_max x 1.7 = {mu_max*1.7:.2f} (estimate-grade linear scaling)")
check("T3 mu_max recorded and < 1", 0 < mu_max < 1)
print(f"\n{PASS}/{PASS+FAIL} PASS")
