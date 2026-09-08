#!/usr/bin/env python3
"""
Patch 3704 verify — AP-5 owed item 8: THE SATURATED-CORE NEUTRON STAR UNDER DRAIN.
Under D1 with the DRAIN reading (3703): inside the saturated core the matter's lapse is pinned at 1/2 (clock), and the
force matter ACTS ON is the K-of-D sample of the true (sea-metric) force: dp/dr = -(e + p)(dnu/2) x chi(r), with
chi = min(1, cap / v_sea(r)), v_sea = 2 (1 - N_s)/(1 + N_s), N_s the GR lapse of the interior solution (normalised to
the exterior at the surface; found by fixed-point iteration on the central lapse). Outside the core chi = 1 and the
star is GR's. Compared: GR (chi = 1 everywhere), DRAIN, and 3636's STOP flat core (chi = 0 in the core) for scale.
EOS: Read et al. 2009 piecewise polytropes SLy and APR4 (as transcribed at 3636, flagged recollection).
 T1  GR maxima reproduced (SLy ~2.05, APR4 ~2.2 Msun) — machinery check.
 T2  The threshold M_thr (central lapse 1/2) is unchanged by construction (the first star the cap touches).
 T3  DRAIN branch above M_thr: M_max, radius at 2.08 Msun, and the sign of dR/dM above the knee, vs GR and vs STOP.
 T4  J0740 (2.08 +/- 0.07 Msun, R = 12.4 +/- 1 km): DRAIN reaches 2.08 on both EOS; its radius there is within 0.3 km of
     GR's own (APR4: 10.78 vs 10.64) — the NICER tension is the EOS's (soft tables), not DRAIN's. The 3636 "rising radii
     above the knee" signature does NOT survive (dR/dM < 0 on the DRAIN branch, shallower than GR). The surviving
     fingerprint is M_max raised ~25-30 % over GR at fixed EOS — degenerate with EOS stiffness at present.
"""
import numpy as np
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL; ok = bool(cond); PASS += ok; FAIL += (not ok); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
G = 6.674e-8; c = 2.998e10; Msun = 1.989e33; Msun_cm = G * Msun / c**2
rho_cgs2geo = G / c**2; p_cgs2geo = G / c**2; CAP = 2 / 3
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
    p_of_rho = lambda rho: Ks[piece(rho)] * rho**Gs[piece(rho)]
    eps_of_rho = lambda rho: (1 + a[piece(rho)]) * rho + Ks[piece(rho)] * rho**Gs[piece(rho)] / (Gs[piece(rho)] - 1)
    pb = [Ks[i] * bounds[i]**Gs[i] for i in range(len(bounds))]
    def rho_of_p(p):
        for i, pbb in enumerate(pb):
            if p < pbb: return (p / Ks[i])**(1 / Gs[i])
        i = len(Ks) - 1; return (p / Ks[i])**(1 / Gs[i])
    return p_of_rho, eps_of_rho, rho_of_p
def make_star(eos, mode):
    p_of_rho, eps_of_rho, rho_of_p = eos
    eps_geo = lambda p_geo: eps_of_rho(rho_of_p(max(p_geo, 1e-30) / p_cgs2geo)) * rho_cgs2geo
    p_surf = p_of_rho(1e6) * p_cgs2geo
    def integrate(p_c, Nc):
        def rhs(r, y):
            m, p, nu = y
            if p <= 0: return [0, 0, 0]
            e = eps_geo(p); dnu = 2 * (m + 4 * np.pi * r**3 * p) / (r * (r - 2 * m))
            N = Nc * np.exp(nu / 2)
            if mode == "GR" or N >= 0.5: chi = 1.0
            else:
                v = 2 * (1 - N) / (1 + N); chi = 0.0 if mode == "STOP" else min(1.0, CAP / v)
            return [4 * np.pi * r**2 * e, -(e + p) * dnu / 2 * chi, dnu]
        r0 = 1.0; y0 = [4 * np.pi * r0**3 * eps_geo(p_c) / 3, p_c, 0.0]
        ev = lambda r, y: y[1] - p_surf; ev.terminal = True; ev.direction = -1
        s = solve_ivp(rhs, [r0, 5e6], y0, events=ev, rtol=1e-8, atol=1e-30, max_step=2e4)
        R = s.t[-1]; M = s.y[0][-1]; nuR = s.y[2][-1]
        return M, R, np.sqrt(1 - 2 * M / R) * np.exp(-nuR / 2)
    def star(p_c):
        Nc = 1.0
        for _ in range(30):
            M, R, Nc_new = integrate(p_c, Nc)
            if not np.isfinite(Nc_new): return np.nan, np.nan, np.nan
            if abs(Nc_new - Nc) < 1e-6: Nc = Nc_new; break
            Nc = 0.5 * (Nc + Nc_new)
        M, R, Nc = integrate(p_c, Nc); return M / Msun_cm, R / 1e5, Nc
    return star
pcs = np.logspace(34.3, 36.2, 46) / c**2 * p_cgs2geo
out = {}
for name, pars in [("SLy", (34.384, 3.005, 2.988, 2.851)), ("APR4", (34.269, 2.830, 3.445, 3.348))]:
    eos = piecewise(*pars); res = {}
    for mode in ("GR", "DRAIN", "STOP"):
        star = make_star(eos, mode); rows = np.array([star(pc) for pc in pcs]); rows = rows[np.isfinite(rows[:, 0])]
        res[mode] = rows
    out[name] = res
    gr, dr, st = res["GR"], res["DRAIN"], res["STOP"]
    thr = gr[np.argmin(abs(gr[:, 2] - 0.5))]
    def at_mass(rows, Mt):
        rows = rows[rows[:, 0] <= rows[np.argmax(rows[:, 0])][0] + 1e-9]  # stable branch up to max
        i = np.argmin(abs(rows[:, 0] - Mt)); return rows[i]
    print(f"\n{name}:")
    print(f"    GR   : M_max = {gr[:,0].max():.3f} Msun; threshold star (N_c = 1/2): M_thr = {thr[0]:.3f}, R = {thr[1]:.2f} km")
    print(f"    DRAIN: M_max = {dr[:,0].max():.3f} Msun; at 2.08 Msun R = {at_mass(dr, 2.08)[1]:.2f} km (GR: {at_mass(gr, 2.08)[1] if gr[:,0].max() >= 2.08 else float('nan'):.2f} km)")
    print(f"    STOP : M_max = {st[:,0].max():.3f} Msun (3636's flat core); at 2.08 Msun R = {at_mass(st, 2.08)[1]:.2f} km")
    above = dr[(dr[:, 0] > thr[0] + 0.02) & (dr[:, 0] < dr[:, 0].max() - 1e-6)]
    slope = np.polyfit(above[:, 0], above[:, 1], 1)[0] if len(above) > 3 else np.nan
    print(f"    DRAIN dR/dM above the knee: {slope:+.2f} km/Msun (GR above 1.78: {np.polyfit(gr[(gr[:,0]>1.78)&(gr[:,0]<gr[:,0].max()-1e-6),0], gr[(gr[:,0]>1.78)&(gr[:,0]<gr[:,0].max()-1e-6),1],1)[0]:+.2f})")
    out[name]["summary"] = dict(Mmax_GR=gr[:, 0].max(), Mmax_DRAIN=dr[:, 0].max(), Mmax_STOP=st[:, 0].max(), Mthr=thr[0], R208=at_mass(dr, 2.08)[1], slope=slope)
print()
s = out["SLy"]["summary"]; a = out["APR4"]["summary"]
check("T1 GR maxima ~2.05 (SLy), ~2.2 (APR4) to ~6 %", abs(s["Mmax_GR"] - 2.05) < 0.13 and abs(a["Mmax_GR"] - 2.2) < 0.15)
check("T2 threshold unchanged ~1.78 Msun (both EOS)", abs(s["Mthr"] - 1.78) < 0.08 and abs(a["Mthr"] - 1.78) < 0.08)
check("T3 DRAIN raises M_max above GR but far less than STOP", s["Mmax_GR"] < s["Mmax_DRAIN"] < s["Mmax_STOP"] and a["Mmax_GR"] < a["Mmax_DRAIN"] < a["Mmax_STOP"])
check("T4a DRAIN reaches 2.08 Msun on both EOS", all(out[n]["summary"]["Mmax_DRAIN"] >= 2.08 for n in out))
gr_a = out["APR4"]["GR"]; i = np.argmin(abs(gr_a[:, 0] - 2.08)); R_gr = gr_a[i, 1]
check("T4b DRAIN radius at 2.08 within 0.3 km of GR's own (APR4): the NICER tension is the EOS's", abs(a["R208"] - R_gr) < 0.3, f"{a['R208']:.2f} vs {R_gr:.2f} km")
check("T4c the 3636 rising-radius signature does NOT survive DRAIN (dR/dM < 0 on both EOS)", s["slope"] < 0 and a["slope"] < 0)
check("T4d surviving fingerprint: M_max boosted 20-40 % over GR at fixed EOS", all(1.2 < out[n]["summary"]["Mmax_DRAIN"] / out[n]["summary"]["Mmax_GR"] < 1.4 for n in out), f"SLy x{s['Mmax_DRAIN']/s['Mmax_GR']:.2f}, APR4 x{a['Mmax_DRAIN']/a['Mmax_GR']:.2f}")
print(f"\n{PASS}/{PASS+FAIL} PASS")
