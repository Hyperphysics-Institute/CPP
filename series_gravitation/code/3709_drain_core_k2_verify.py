#!/usr/bin/env python3
"""
Patch 3709 verify — AP-5 owed item 9 (low stakes): the tidal Love number of a saturated-core neutron star under DRAIN.
Background: 3704's DRAIN star (APR4; hydrostatics scaled by chi = min(1, cap/v_sea) in the core; metric GR's sourced by
rho, p). Perturbation: Hinderer's y-equation with the fluid's compressional response term 4 pi (e + p)/(dp/de)
multiplied by chi(r) in the core — the perturbed force matter acts on is the same K-of-D fraction (estimate-grade,
labelled). k2 from the standard closed form; Lambda = (2/3) k2 C^-5.
 T1  Unsaturated star (1.4 Msun): DRAIN = GR exactly (chi = 1 everywhere).
 T2  2.08 Msun on APR4: k2 and Lambda under GR (chi = 1) vs DRAIN; the change is small (|d ln Lambda| < 30 %).
 T3  Sign and size recorded; below any current or near-future BNS sensitivity for a 2.08 Msun component
     (Lambda ~ few tens; GW170817's 1.4 Msun bound ~ 190 +390/-120 on Lambda-tilde is a different mass).
"""
import numpy as np
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(n, c, d=""):
    global PASS, FAIL; ok = bool(c); PASS += ok; FAIL += (not ok); print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  — {d}" if d else ""))
G = 6.674e-8; c = 2.998e10; Msun = 1.989e33; Msun_cm = G * Msun / c**2; geo = G / c**2; CAP = 2 / 3
def piecewise(logp1, G1, G2, G3):
    crust = [(6.80110e-9, 1.58425), (1.06186e-6, 1.28733), (5.32697e1, 0.62223), (3.99874e-8, 1.35692)]
    rho_c = [2.44034e7, 3.78358e11, 2.62780e12]; rho1, rho2 = 10**14.7, 10**15.0
    p1 = 10**logp1 / c**2; K1 = p1 / rho1**G1; K2 = K1 * rho1**G1 / rho1**G2; K3 = K2 * rho2**G2 / rho2**G3
    K3c, G3c = crust[3]; rho0 = (K1 / K3c)**(1 / (G3c - G1))
    Ks = [k for k, g in crust] + [K1, K2, K3]; Gs = [g for k, g in crust] + [G1, G2, G3]; bounds = rho_c + [rho0, rho1, rho2]
    a = [0.0]
    for i in range(1, len(Ks)):
        rb = bounds[i - 1]; eps_prev = (1 + a[i - 1]) * rb + Ks[i - 1] * rb**Gs[i - 1] / (Gs[i - 1] - 1)
        a.append(eps_prev / rb - 1 - Ks[i] * rb**(Gs[i] - 1) / (Gs[i] - 1))
    def piece(rho):
        for i, rb in enumerate(bounds):
            if rho < rb: return i
        return len(Ks) - 1
    pb = [Ks[i] * bounds[i]**Gs[i] for i in range(len(bounds))]
    def rho_of_p(p):
        for i, pbb in enumerate(pb):
            if p < pbb: return (p / Ks[i])**(1 / Gs[i])
        i = len(Ks) - 1; return (p / Ks[i])**(1 / Gs[i])
    def eps_of_p(p): rho = rho_of_p(p); i = piece(rho); return (1 + a[i]) * rho + p / (Gs[i] - 1)
    def dpde_of_p(p): rho = rho_of_p(p); i = piece(rho); G_ = Gs[i]; return (G_ * p) / ((1 + a[i]) * rho + G_ * p / (G_ - 1))  # dp/de = Gamma p / (e + p)
    return eps_of_p, dpde_of_p, Ks[0] * 1e6**Gs[0]
def star(eos, p_c, mode):
    eps_of_p, dpde_of_p, p_surf_cgs = eos; p_surf = p_surf_cgs * geo
    e_geo = lambda p: eps_of_p(max(p, 1e-30) / geo) * geo
    def run(Nc):
        def rhs(r, y):
            m, p, nu, yt = y
            if p <= 0: return [0, 0, 0, 0]
            e = e_geo(p); f = 1 - 2 * m / r; dnu = 2 * (m + 4 * np.pi * r**3 * p) / (r * (r - 2 * m))
            N = Nc * np.exp(nu / 2)
            if mode == "GR" or N >= 0.5: chi = 1.0
            else: v = 2 * (1 - N) / (1 + N); chi = min(1.0, CAP / v)
            dpde = dpde_of_p(max(p, 1e-30) / geo)
            F = (1 - 4 * np.pi * r**2 * (e - p)) / f
            Q = 4 * np.pi * (5 * e + 9 * p + chi * (e + p) / max(dpde, 1e-9)) / f - 6 / (r**2 * f) - (dnu / 2 * 2 * (m + 4 * np.pi * r**3 * p) / (r**2 * f)) * 0  # last term below
            Q -= (2 * (m + 4 * np.pi * r**3 * p) / (r**2 * f))**2
            dy = -(yt**2 + yt * F + r**2 * Q) / r
            return [4 * np.pi * r**2 * e, -(e + p) * dnu / 2 * chi, dnu, dy]
        r0 = 1.0; y0 = [4 * np.pi * r0**3 * e_geo(p_c) / 3, p_c, 0.0, 2.0]
        ev = lambda r, y: y[1] - p_surf; ev.terminal = True; ev.direction = -1
        s = solve_ivp(rhs, [r0, 5e6], y0, events=ev, rtol=1e-8, atol=1e-30, max_step=2e4)
        R = s.t[-1]; M = s.y[0][-1]; nuR = s.y[2][-1]; yR = s.y[3][-1]
        return M, R, np.sqrt(1 - 2 * M / R) * np.exp(-nuR / 2), yR
    Nc = 1.0
    for _ in range(30):
        M, R, Nn, yR = run(Nc)
        if abs(Nn - Nc) < 1e-6: Nc = Nn; break
        Nc = 0.5 * (Nc + Nn)
    M, R, Nc, yR = run(Nc)
    C = M / R; y = yR
    num = (8 / 5) * C**5 * (1 - 2 * C)**2 * (2 + 2 * C * (y - 1) - y)
    den = (2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * (1 - 2 * C)**2 * (2 - y + 2 * C * (y - 1)) * np.log(1 - 2 * C))
    k2 = num / den; Lam = (2 / 3) * k2 / C**5
    return M / Msun_cm, R / 1e5, Nc, k2, Lam
eos = piecewise(34.269, 2.830, 3.445, 3.348)
def find(mode, Mt):
    pcs = np.logspace(34.3, 36.0, 40) / c**2 * geo; best = None
    for pc in pcs:
        r = star(eos, pc, mode)
        if best is None or abs(r[0] - Mt) < abs(best[0] - Mt): best = r
    return best
print("T1 — 1.4 Msun (unsaturated)")
g14, d14 = find("GR", 1.4), find("DRAIN", 1.4)
print(f"    GR:    M = {g14[0]:.3f}, R = {g14[1]:.2f} km, N_c = {g14[2]:.3f}, k2 = {g14[3]:.4f}, Lambda = {g14[4]:.0f}")
print(f"    DRAIN: M = {d14[0]:.3f}, R = {d14[1]:.2f} km, N_c = {d14[2]:.3f}, k2 = {d14[3]:.4f}, Lambda = {d14[4]:.0f}")
check("T1 DRAIN = GR for an unsaturated star (|dLambda/Lambda| < 1e-6)", abs(d14[4] / g14[4] - 1) < 1e-6)
print("\nT2 — 2.08 Msun on APR4")
g2, d2 = find("GR", 2.08), find("DRAIN", 2.08)
print(f"    GR:    M = {g2[0]:.3f}, R = {g2[1]:.2f} km, N_c = {g2[2]:.3f}, k2 = {g2[3]:.4f}, Lambda = {g2[4]:.1f}")
print(f"    DRAIN: M = {d2[0]:.3f}, R = {d2[1]:.2f} km, N_c = {d2[2]:.3f}, k2 = {d2[3]:.4f}, Lambda = {d2[4]:.1f}")
dl = d2[4] / g2[4] - 1
check("T2 change in Lambda at 2.08 Msun is modest (|d ln Lambda| < 0.3)", abs(dl) < 0.3, f"{dl*100:+.1f} %")
print("\nT3 — sensitivity")
check("T3 Lambda(2.08) ~ tens: below any current BNS sensitivity for a heavy component", d2[4] < 200)
print(f"\n{PASS}/{PASS+FAIL} PASS")
