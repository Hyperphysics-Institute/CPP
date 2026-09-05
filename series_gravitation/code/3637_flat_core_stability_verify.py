#!/usr/bin/env python3
"""
Patch 3637 verify — OPEN-GR-SATURATED-CORE-1 rung 3: stability of the flat-core branch, by what can be decided statically.

 (1) The combined sequence (TOV up to the threshold, then flat core growing) for SLy: gravitational mass M, baryon mass N
     (proper-volume integral of the rest-mass density: flat core 4 pi r^2 dr; envelope 4 pi r^2 dr / sqrt(1 - 2m/r)) and the
     binding M - N along the sequence. Is M(N) single-valued and monotone through the threshold, i.e. no cusp?
 (2) The turning-point theorem (Harrison-Thorne-Wakano-Wheeler; Sorkin) says stability can change only at a cusp of the M-N
     curve, PROVIDED the sequence consists of extrema of M at fixed N. That proviso is tested directly: for flat-core members,
     the one-parameter family 'core radius r_c free, envelope in hydrostatic equilibrium, N fixed' — is M stationary in r_c
     exactly where the register condition N(r_c) = 1/2 holds? If yes, the register condition IS an energy principle and the
     theorem applies: no cusp -> the flat-core branch inherits the TOV branch's stability up to its own mass maximum.
     If no, the flat-core equilibria are not GR-mass extrema and stability needs the dynamical register rule (open).
 (3) The comparison at fixed N: is the flat-core star lower in M than the TOV star of the same N (where both exist)?
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
G = 6.674e-8; c = 2.998e10; Msun = 1.989e33; Msun_cm = G * Msun / c**2; cgs2geo = G / c**2
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
p_of_rho, eps_of_rho, rho_of_p = piecewise(34.384, 3.005, 2.988, 2.851)     # SLy (recalled, 3636)
eps_g = lambda p: eps_of_rho(rho_of_p(max(p, 1e-30) / cgs2geo)) * cgs2geo
rho_g = lambda p: rho_of_p(max(p, 1e-30) / cgs2geo) * cgs2geo
p_surf = p_of_rho(1e10) * cgs2geo
def rhs(r, y):
    m, p, nu, Nb = y
    if p <= 0: return [0, 0, 0, 0]
    e = eps_g(p); dnu = 2 * (m + 4 * np.pi * r**3 * p) / (r * (r - 2 * m))
    return [4 * np.pi * r**2 * e, -(e + p) * dnu / 2, dnu, 4 * np.pi * r**2 * rho_g(p) / np.sqrt(1 - 2 * m / r)]
def star(p_c, r_c):
    """flat core of radius r_c at pressure p_c (uniform), TOV envelope; returns M, R, N_lapse(r_c), Nb (baryon mass), all geometric."""
    e_c = eps_g(p_c)
    if r_c < 1.0:
        r0 = 1.0; y0 = [4 * np.pi * r0**3 * e_c / 3, p_c, 0.0, 0.0]
    else:
        M_c = e_c * 4 * np.pi * r_c**3 / 3
        if 2 * M_c / r_c >= 0.999: return (np.nan,) * 4
        r0 = r_c; y0 = [M_c, p_c, 0.0, rho_g(p_c) * 4 * np.pi * r_c**3 / 3]
    ev = lambda r, y: y[1] - p_surf; ev.terminal = True; ev.direction = -1
    s = solve_ivp(rhs, [r0, 5e6], y0, events=ev, rtol=1e-8, atol=1e-32, max_step=5e4)
    R = s.t[-1]; M = s.y[0][-1]; Nb = s.y[3][-1]
    return M, R, np.exp(-s.y[2][-1] / 2) * np.sqrt(1 - 2 * M / R), Nb
def core_radius(p_c):
    M0, R0, N0, _ = star(p_c, 0.0)
    if N0 <= 0.5: return 0.0 if abs(N0 - 0.5) < 1e-3 else np.nan
    g = lambda rc: star(p_c, rc)[2] - 0.5
    hi = R0 * 0.98
    while not np.isfinite(g(hi)): hi *= 0.9
    if g(hi) > 0: return np.nan
    return brentq(g, 10.0, hi, xtol=100.0)
# (1) the combined sequence
rhos_tov = np.logspace(14.7, 15.4, 16)
tov = []
for rh in rhos_tov:
    pc = p_of_rho(rh) * cgs2geo; M, R, N, Nb = star(pc, 0.0)
    if N <= 0.5: break
    tov.append((pc, 0.0, M, R, Nb))
# threshold
pc_lo, pc_hi = tov[-1][0], p_of_rho(rhos_tov[len(tov)]) * cgs2geo
pc_thr = brentq(lambda p: star(p, 0.0)[2] - 0.5, pc_lo, pc_hi, xtol=pc_lo * 1e-6)
M, R, N, Nb = star(pc_thr, 0.0); tov.append((pc_thr, 0.0, M, R, Nb))
flat = []
for pc in np.geomspace(pc_thr * 0.98, pc_thr * 0.25, 14):
    rc = core_radius(pc)
    if not np.isfinite(rc) or rc <= 0: continue
    M, R, N, Nb = star(pc, rc); flat.append((pc, rc, M, R, Nb))
seq = tov + flat
Ms = np.array([q[2] for q in seq]) / Msun_cm; Nbs = np.array([q[4] for q in seq]) / Msun_cm; rcs = np.array([q[1] for q in seq]) / 1e5; Rs = np.array([q[3] for q in seq]) / 1e5
print("     combined SLy sequence (p_c relative to threshold, r_c km, M, N_b, R km, binding N_b - M):")
for q, Mv, Nv, rcv, Rv in zip(seq, Ms, Nbs, rcs, Rs):
    print(f"       p_c/p_thr = {q[0]/pc_thr:6.3f}  r_c = {rcv:5.2f}  M = {Mv:.3f}  N_b = {Nv:.3f}  R = {Rv:5.2f}  N_b - M = {Nv - Mv:.3f}")
nt = len(tov)
check("(1a) M and N_b both increase monotonically through the threshold onto the flat-core branch (no turning point, no cusp in the M-N plane) up to the branch maximum", np.all(np.diff(Ms[: nt + len(flat) - 1]) > 0) and np.all(np.diff(Nbs[: nt + len(flat) - 1]) > 0), f"M: {Ms[nt-1]:.3f} -> {Ms.max():.3f}")
check("(1b) the binding energy N_b - M stays positive and grows along the flat-core branch (the flat-core stars are bound)", np.all((Nbs - Ms)[nt:] > 0) and (Nbs - Ms)[-1] > (Nbs - Ms)[nt - 1])
# (2) the variational test: at fixed N_b, is M stationary in r_c where the register condition holds?
def M_at_fixed_N(rc, Nb_target, pc_guess):
    f = lambda pc: (lambda v: v if np.isfinite(v) else 1e99)(star(pc, rc)[3] - Nb_target)   # over-massive core -> treat as too much baryon mass
    lo, hi = pc_guess * 0.3, pc_guess * 3.0
    while f(lo) > 0 and lo > pc_guess * 0.02: lo *= 0.7
    while f(hi) < 0: hi *= 2.0
    if not np.isfinite(f(lo)): lo = pc_guess * 0.1
    pc = brentq(f, lo, hi, xtol=pc_guess * 1e-7)
    M, R, N, Nb = star(pc, rc); return M, pc, N
results = []
for q in [flat[1], flat[4], flat[8]]:
    pc0, rc0, M0, R0, Nb0 = q
    drc = 0.03 * rc0
    Mm, _, _ = M_at_fixed_N(rc0 - drc, Nb0, pc0); Mp, _, _ = M_at_fixed_N(rc0 + drc, Nb0, pc0); Mc, _, Nc = M_at_fixed_N(rc0, Nb0, pc0)
    dMdr = (Mp - Mm) / (2 * drc); scale = M0 / rc0
    # where IS M stationary in r_c at this N_b? scan
    rcs_scan = np.linspace(0.5 * rc0, 1.3 * rc0, 7)
    Ms_scan = [M_at_fixed_N(r_, Nb0, pc0)[0] for r_ in rcs_scan]
    Ns_scan = [M_at_fixed_N(r_, Nb0, pc0)[2] for r_ in rcs_scan]
    results.append((rc0 / 1e5, M0 / Msun_cm, dMdr / scale, rcs_scan / 1e5, np.array(Ms_scan) / Msun_cm, Ns_scan))
    print(f"     flat-core member r_c = {rc0/1e5:.2f} km, M = {M0/Msun_cm:.3f}: at fixed N_b, (dM/dr_c)/(M/r_c) = {dMdr/scale:+.4f}")
    print("        r_c scan (km):", np.round(rcs_scan / 1e5, 2)); print("        M (Msun):     ", np.round(np.array(Ms_scan) / Msun_cm, 4)); print("        lapse at r_c: ", np.round(Ns_scan, 3))
stationary = all(abs(r[2]) < 0.02 for r in results)
mono_up = all(np.all(np.diff(r[4]) > 0) for r in results)
check("(2a) FINDING: at fixed baryon mass M is NOT stationary at the register radius — it rises monotonically with the core radius through it (dM/dr_c > 0 for every member): the flat-core equilibria are not extrema of the GR mass functional; the register cap bears a load (the star would lower its GR energy by compressing the core, through configurations with central lapse < 1/2 that the register forbids)", (not stationary) and mono_up and all(r[2] > 0 for r in results), ", ".join(f"{r[2]:+.4f}" for r in results))
check("(2b) the loaded direction is toward the TOV configuration (core shrinking) for every member — no member is a GR-energy minimum against core growth or shrinkage; the stability question is therefore ENTIRELY whether the cap is rigid (R-FLOOR-REGISTER: a saturation limit, hard) or soft", len({np.sign(r[2]) for r in results}) == 1 and results[0][2] > 0)
# constrained turning-point: along the constrained (register-obeying) sequence itself, M(N_b) has no cusp up to the branch maximum (1a); on a rigid constraint manifold the flat-core equilibria are the constrained extrema (envelope hydrostatic, core structureless), so stability is inherited from the TOV branch below the threshold
check("(2c) on the constraint manifold (rigid cap) the sequence has no cusp (1a): the flat-core branch inherits the stability of the sub-threshold TOV branch up to its own mass maximum — CONDITIONAL on the cap being rigid", np.all(np.diff(Ms[:-1]) > 0))
# (3) fixed-N comparison against the GR (TOV) stars beyond the threshold — configurations the register forbids but GR would allow
tov_all = []
for rh in np.logspace(14.7, 15.65, 22):
    pc = p_of_rho(rh) * cgs2geo; M, R, N, Nb = star(pc, 0.0); tov_all.append((M / Msun_cm, Nb / Msun_cm, N))
tov_all = np.array(tov_all); ig = int(np.argmax(tov_all[:, 0])); tovM, tovN = tov_all[:ig + 1, 0], tov_all[:ig + 1, 1]
cmp = [(Nv, Mv, np.interp(Nv, tovN, tovM)) for Nv, Mv in zip(Nbs[nt:], Ms[nt:]) if tovN.min() < Nv < tovN.max()]
print("     fixed-N_b comparison with the GR TOV star of the same baryon mass (N_b, M_flatcore, M_TOV):", [(round(a, 3), round(b, 3), round(cc, 3)) for a, b, cc in cmp])
check("(3) where a GR TOV star of the same baryon mass exists (up to GR's maximum), the flat-core star has the LARGER gravitational mass (less bound) — the register-forbidden TOV configuration is the GR energy minimum; the flat-core star is a constrained equilibrium held by the cap", all(b > cc for _, b, cc in cmp) and len(cmp) >= 3, f"{len(cmp)} members compared; max dM = {max(b - cc for _, b, cc in cmp):.3f} Msun")
print(); print(f"3637 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
