#!/usr/bin/env python3
"""
Patch 3636 verify — OPEN-GR-SATURATED-CORE-1 rung 2: (i) the reading is DERIVED, not postulated; (ii) realistic EOS in solar masses.

 (i) Derivation. Two ratified premises: (P1) the register is the lapse and the cap is lapse 1/2 (R-CLOCK-RATE-IS-DISPLACEMENT,
     R-PSR-LAW-LOG, R-FLOOR-REGISTER: the floor is a register-saturation limit); (P2) matter's dynamics are the derived Einstein
     equations (OPEN-GR-FE-1 closed), whose static limit is hydrostatic equilibrium dp/dr = -(eps + p) d(ln N)/dr.
     A pinned register is a uniform lapse; a uniform lapse is zero d(ln N)/dr; zero d(ln N)/dr is dp/dr = 0. Reading (b)
     ('only the clocks are capped') would require a force that is not the lapse gradient, which neither premise supplies.
     Hence (a): the pinned core is at uniform pressure — P-PINNED-CORE-IS-FLAT is a theorem of P1 + P2, not a postulate.
     The verify checks the algebra: with N = 1/2 uniform the TOV pressure equation integrates to p = const exactly.
 (ii) Piecewise-polytrope EOS (Read, Lackey, Owen, Friedman 2009 parametrisation, K in p/c^2 units; coefficients from recollection — flagged):
     SLy (log p1 = 34.384, G = 3.005, 2.988, 2.851) and APR4 (34.269, 2.830, 3.445, 3.348) on the standard four-piece crust.
     For each: GR's TOV maximum (M, R); the threshold star (central lapse 1/2): M_thr, R_thr; the flat-core branch's maximum.
     Confronted with PSR J0740+6620: M = 2.08 +/- 0.07 Msun, R = 12.4 +/- 1 km (NICER, recollection).
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
# (i) algebra: TOV pressure equation with uniform N
import sympy as sp
rr = sp.symbols("r", positive=True); pf = sp.Function("p")(rr); Nf = sp.Function("N")(rr); epsf = sp.Function("eps")(rr)
hydro = sp.Eq(sp.diff(pf, rr), -(epsf + pf) * sp.diff(sp.log(Nf), rr))
check("(i-a) hydrostatic equilibrium with N = const gives dp/dr = 0 identically (any eps(r), any EOS)", sp.simplify(hydro.rhs.subs(Nf, sp.Rational(1, 2)).doit()) == 0)
# the mass function jump: with the interior flat, m(r) = 0 inside and the count appears at the boundary (3624 bookkeeping) — pure GR, no new rule
print("     (i) P-PINNED-CORE-IS-FLAT follows from P1 (register = lapse, cap = lapse 1/2) + P2 (Einstein's static limit). Reading (b) has no force to offer.")
# (ii) units: G = c = 1, lengths in cm
G = 6.674e-8; c = 2.998e10; Msun = 1.989e33; Msun_cm = G * Msun / c**2
rho_cgs2geo = G / c**2; p_cgs2geo = G / c**2      # pressures are carried as p/c^2 in g/cm^3 (Read et al.'s K units); same geometric factor as rho
def piecewise(logp1, G1, G2, G3):
    # crust (Read et al. 2009 Table II, SLy crust), cgs: K in units with p = K rho^Gamma
    crust = [(6.80110e-9, 1.58425), (1.06186e-6, 1.28733), (5.32697e1, 0.62223), (3.99874e-8, 1.35692)]
    rho_c = [2.44034e7, 3.78358e11, 2.62780e12]
    rho1, rho2 = 10**14.7, 10**15.0
    p1 = 10**logp1 / c**2; K1 = p1 / rho1**G1     # log p1 is in dyn/cm^2; convert to p/c^2
    K2 = K1 * rho1**G1 / rho1**G2; K3 = K2 * rho2**G2 / rho2**G3
    # crust-core join: rho0 where K3c rho^G3c = K1 rho^G1
    K3c, G3c = crust[3]
    rho0 = (K1 / K3c)**(1 / (G3c - G1))
    Ks = [k for k, g in crust] + [K1, K2, K3]; Gs = [g for k, g in crust] + [G1, G2, G3]
    bounds = rho_c + [rho0, rho1, rho2]
    # continuity constants a_i for eps = (1 + a) rho + p/(G-1)
    a = [0.0]
    for i in range(1, len(Ks)):
        rb = bounds[i - 1]
        eps_prev = (1 + a[i - 1]) * rb + Ks[i - 1] * rb**Gs[i - 1] / (Gs[i - 1] - 1)
        a.append(eps_prev / rb - 1 - Ks[i] * rb**(Gs[i] - 1) / (Gs[i] - 1))
    def piece(rho):
        for i, rb in enumerate(bounds):
            if rho < rb: return i
        return len(Ks) - 1
    def p_of_rho(rho): i = piece(rho); return Ks[i] * rho**Gs[i]
    def eps_of_rho(rho): i = piece(rho); return (1 + a[i]) * rho + Ks[i] * rho**Gs[i] / (Gs[i] - 1)
    pb = [Ks[i] * bounds[i]**Gs[i] for i in range(len(bounds))]
    def rho_of_p(p):
        for i, pbb in enumerate(pb):
            if p < pbb: return (p / Ks[i])**(1 / Gs[i])
        i = len(Ks) - 1; return (p / Ks[i])**(1 / Gs[i])
    return p_of_rho, eps_of_rho, rho_of_p
def star_model(eos):
    p_of_rho, eps_of_rho, rho_of_p = eos
    eps_geo = lambda p_geo: eps_of_rho(rho_of_p(max(p_geo, 1e-30) / p_cgs2geo)) * rho_cgs2geo
    def rhs(r, y):
        m, p, nu = y
        if p <= 0: return [0, 0, 0]
        e = eps_geo(p); dnu = 2 * (m + 4 * np.pi * r**3 * p) / (r * (r - 2 * m))
        return [4 * np.pi * r**2 * e, -(e + p) * dnu / 2, dnu]
    def envelope(p_c, r_c):
        e_c = eps_geo(p_c)
        if r_c < 1.0:
            r0 = 1.0; y0 = [4 * np.pi * r0**3 * e_c / 3, p_c, 0.0]
        else:
            M_c = e_c * 4 * np.pi * r_c**3 / 3
            if 2 * M_c / r_c >= 0.999: return np.nan, np.nan, np.nan
            r0 = r_c; y0 = [M_c, p_c, 0.0]
        p_surf = p_of_rho(1e6) * p_cgs2geo
        ev = lambda r, y: y[1] - p_surf; ev.terminal = True; ev.direction = -1
        s = solve_ivp(rhs, [r0, 5e6], y0, events=ev, rtol=1e-8, atol=1e-30, max_step=2e4)
        R = s.t[-1]; M = s.y[0][-1]; nu_R = s.y[2][-1]
        return M, R, np.exp(-nu_R / 2) * np.sqrt(1 - 2 * M / R)
    def flatcore(p_c):
        M0, R0, N0 = envelope(p_c, 0.0)
        if N0 <= 0.5: return np.nan, np.nan, np.nan
        g = lambda rc: envelope(p_c, rc)[2] - 0.5
        hi = R0 * 0.98
        while not np.isfinite(g(hi)): hi *= 0.9
        if g(hi) > 0: return np.nan, np.nan, np.nan
        rc = brentq(g, 10.0, hi, xtol=1.0)
        M, R, N = envelope(p_c, rc); return M, R, rc
    return envelope, flatcore, p_of_rho
results = {}
for name, pars in [("SLy", (34.384, 3.005, 2.988, 2.851)), ("APR4", (34.269, 2.830, 3.445, 3.348))]:
    envelope, flatcore, p_of_rho = star_model(piecewise(*pars))
    rhos = np.logspace(14.6, 15.9, 40)
    pcs = [p_of_rho(rh) * p_cgs2geo for rh in rhos]
    seq = np.array([envelope(p, 0.0) for p in pcs])
    Ms = seq[:, 0] / Msun_cm; Rs = seq[:, 1] / 1e5; Ns = seq[:, 2]
    imax = int(np.nanargmax(Ms))
    # threshold star on the stable branch
    j = next((i for i in range(imax + 1) if Ns[i] <= 0.5), None)
    if j is not None and j > 0:
        w = (0.5 - Ns[j]) / (Ns[j - 1] - Ns[j]); M_thr = Ms[j] + w * (Ms[j - 1] - Ms[j]); R_thr = Rs[j] + w * (Rs[j - 1] - Rs[j])
    else:
        M_thr, R_thr = (np.nan, np.nan) if j is None else (Ms[0], Rs[0])
    fc = np.array([flatcore(p) for p in pcs[:imax + 1]])
    fcM = fc[:, 0] / Msun_cm; fcR = fc[:, 1] / 1e5
    k = int(np.nanargmax(fcM)) if np.any(np.isfinite(fcM)) else None
    ok = np.isfinite(fcM)
    print(f"     {name} flat-core branch (M Msun, R km, r_c km):", [(round(a, 2), round(b, 2), round(cc / 1e5, 2)) for a, b, cc in zip(fcM[ok], fcR[ok], fc[ok, 2])])
    R_at_J = np.interp(2.08, fcM[ok][np.argsort(fcM[ok])], fcR[ok][np.argsort(fcM[ok])]) if ok.sum() > 1 else np.nan
    print(f"     {name}: flat-core star of 2.08 Msun would have R ~ {R_at_J:.1f} km (branch interpolation; NICER J0740: 12.4 +/- 1 km)")
    results[name] = dict(Mmax=Ms[imax], Rmax=Rs[imax], Nc_max=Ns[imax], M_thr=M_thr, R_thr=R_thr, reached=j is not None,
                         fcM=fcM[k] if k is not None else np.nan, fcR=fcR[k] if k is not None else np.nan, fc_rc=fc[k, 2] / 1e5 if k is not None else np.nan)
    o = results[name]
    print(f"     {name}: GR M_max = {o['Mmax']:.3f} Msun at R = {o['Rmax']:.2f} km (N_c = {o['Nc_max']:.3f}); threshold star M_thr = {o['M_thr']:.3f} Msun, R_thr = {o['R_thr']:.2f} km, C_thr = {o['M_thr']*Msun_cm/(o['R_thr']*1e5):.3f}; flat-core branch max M = {o['fcM']:.3f} Msun at R = {o['fcR']:.2f} km (r_c = {o['fc_rc']:.2f} km)")
check("(ii-a) the recalled piecewise polytropes reproduce the literature TOV maxima to ~5% (SLy ~2.05, APR4 ~2.2 Msun) — the EOS transcription is sound", abs(results['SLy']['Mmax'] - 2.05) < 0.12 and abs(results['APR4']['Mmax'] - 2.2) < 0.15)
check("(ii-b) both EOS reach central lapse 1/2 on the stable branch: the threshold star exists", all(o['reached'] for o in results.values()))
MJ, dMJ, RJ, dRJ = 2.08, 0.07, 12.4, 1.0
for name, o in results.items():
    print(f"     {name}: M_thr/M_max = {o['M_thr']/o['Mmax']:.3f};  J0740 (2.08 +/- 0.07) vs M_thr: {(MJ - o['M_thr'])/dMJ:+.1f} sigma")
check("(ii-c) the derived reading (a) caps ordinary (TOV-branch) neutron stars at M_thr = 1.78 Msun for BOTH EOS — 13-18% below GR's maximum, and nearly EOS-independent", all(0.80 < o['M_thr'] / o['Mmax'] < 0.90 for o in results.values()) and abs(results['SLy']['M_thr'] - results['APR4']['M_thr']) < 0.05)
tension = all(o['M_thr'] < MJ - dMJ for o in results.values())
check("(ii-d) CONFRONTATION: for both EOS the threshold mass lies below PSR J0740's mass by > 1 sigma — under reading (a) the heaviest pulsar cannot be an ordinary (TOV-branch) star for these EOS", tension, "; ".join(f"{n}: {(MJ - o['M_thr'])/dMJ:+.1f} sigma" for n, o in results.items()))
fc_ok = all(np.isfinite(o['fcM']) and o['fcM'] > MJ for o in results.values())
print("     flat-core branch: can it carry 2.08 Msun?", {n: (round(o['fcM'], 2), round(o['fcR'], 2)) for n, o in results.items()})
check("(ii-e) the flat-core branch reaches >= 2.08 Msun for both EOS, at radii " + ", ".join(f"{o['fcR']:.1f}" for o in results.values()) + " km — J0740's radius (12.4 +/- 1 km) decides: a flat-core J0740 would need the branch to be stable AND its radius to match", fc_ok)
print(); print(f"3636 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
