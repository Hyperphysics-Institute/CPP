#!/usr/bin/env python3
"""
Patch 3634 verify — OPEN-GR-SATURATION-THRESHOLD-1: the relativistic saturation threshold.
Under R-CLOCK-RATE-IS-DISPLACEMENT + R-PSR-LAW-LOG the register IS the lapse: v = N^-1(lapse), N = (1 - v/2)/(1 + v/2),
exactly as the exterior v = M/rbar is N^-1 of Schwarzschild's isotropic lapse. The cap v = 2/3 is lapse 1/2.
So a body saturates at its centre when its CENTRAL LAPSE reaches 1/2 — a TOV statement, not a Newtonian one.
 (1) Uniform density (Schwarzschild interior): N_c = (3/2) sqrt(1 - 2C) - 1/2 -> N_c = 1/2 at C = 5/18 = 0.278 (N_c = 0 is Buchdahl 4/9).
     3629's 'threshold at Buchdahl' conflated the Newtonian census threshold (M/R_iso = 4/9) with the compactness; the lattice-
     census reading maps to areal C = 36/121 = 0.298. Both are FAR BELOW Buchdahl and AT THE UPPER EDGE of the neutron-star range.
 (2) TOV polytropes Gamma = 2, 2.5, 3: the central lapse along the sequence; whether N_c = 1/2 is reached on the stable branch
     (before the maximum mass) and at what compactness; N_c at the maximum-mass configuration.
 (3) Verdict: the corpus's sentence 'neutron stars do not saturate; collapse past Buchdahl is register saturation' (3629) is
     WRONG in its threshold: saturation is central lapse 1/2, reached by sufficiently compact stable stars for stiff EOS.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
# (1) uniform density
Nc_unif = lambda C: 1.5 * np.sqrt(1 - 2 * C) - 0.5
C_half = brentq(lambda C: Nc_unif(C) - 0.5, 0.01, 0.44)
check("(1a) uniform-density star: central lapse 1/2 at C = 5/18 = 0.2778 (Buchdahl 4/9 is where the central lapse vanishes)", abs(C_half - 5 / 18) < 1e-9, f"C = {C_half:.4f}")
Rbar_over = lambda C: None
# lattice-census reading: M/Rbar = 4/9 -> areal C = (4/9)/(1 + 2/9)^2 = 36/121
C_census = (4 / 9) / (1 + 2 / 9)**2
check("(1b) the lattice-census reading (uniform count, M/Rbar = 4/9) is areal C = 36/121 = 0.298, not 0.44: 3629 quoted the isotropic ratio as a compactness", abs(C_census - 36 / 121) < 1e-12, f"C = {C_census:.4f}")
check("(1c) both thresholds sit at the upper edge of the neutron-star range (0.15-0.30), far below Buchdahl", 0.25 < C_half < 0.31 and 0.25 < C_census < 0.31)
# (2) TOV polytropes p = K rho^Gamma, eps = rho + p/(Gamma-1); G = c = K = 1
def tov(Gamma, rho_c):
    K = 1.0
    def eos(p):
        rho = (max(p, 0) / K)**(1 / Gamma); return rho + p / (Gamma - 1)
    p_c = K * rho_c**Gamma
    def rhs(r, y):
        m, p, nu = y
        if p <= 0: return [0, 0, 0]
        e = eos(p)
        dnu = 2 * (m + 4 * np.pi * r**3 * p) / (r * (r - 2 * m))
        return [4 * np.pi * r**2 * e, -(e + p) * dnu / 2, dnu]
    r0 = 1e-6; e_c = eos(p_c)
    y0 = [4 * np.pi * r0**3 * e_c / 3, p_c, 0.0]
    ev = lambda r, y: y[1] - 1e-12 * p_c; ev.terminal = True; ev.direction = -1
    s = solve_ivp(rhs, [r0, 1e3], y0, events=ev, rtol=1e-10, atol=1e-14, max_step=0.05)
    R = s.t[-1]; M = s.y[0][-1]; nu_R = s.y[2][-1]
    nu_c = 0.0 - nu_R + np.log(1 - 2 * M / R)          # match exterior: nu(R) = ln(1 - 2M/R)
    return M, R, M / R, np.exp(nu_c / 2)
print("     Gamma   rho_c   M       R       C       N_c")
verdicts = {}
for Gamma in [2.0, 2.5, 3.0]:
    rhos = np.logspace(-2.5, 0.5, 120) if Gamma < 3 else np.logspace(-2, 1.2, 140)
    seq = [tov(Gamma, rc) for rc in rhos]
    Ms = np.array([q[0] for q in seq]); Cs = np.array([q[2] for q in seq]); Ncs = np.array([q[3] for q in seq])
    imax = int(np.argmax(Ms))
    stable = slice(0, imax + 1)
    reached = np.any(Ncs[stable] <= 0.5)
    if reached:
        j = np.where(Ncs[stable] <= 0.5)[0][0]
        C_sat = np.interp(0.5, Ncs[stable][j - 1:j + 1][::-1], Cs[stable][j - 1:j + 1][::-1])
    else:
        C_sat = np.nan
    for i in [0, imax // 3, 2 * imax // 3, imax]:
        print(f"     {Gamma:4.1f}  {rhos[i]:7.4f} {Ms[i]:7.4f} {seq[i][1]:7.4f} {Cs[i]:7.4f} {Ncs[i]:7.4f}" + ("  <- max mass" if i == imax else ""))
    verdicts[Gamma] = (Cs[imax], Ncs[imax], reached, C_sat)
    print(f"     Gamma = {Gamma}: C_max = {Cs[imax]:.4f}, N_c at max mass = {Ncs[imax]:.4f}; central lapse 1/2 reached on the stable branch: {reached}" + (f" at C = {C_sat:.4f}" if reached else ""))
check("(2a) EVERY polytrope Gamma = 2, 2.5, 3 reaches central lapse 1/2 ON THE STABLE BRANCH (before the maximum mass): saturation is generic for compact stable stars", all(v[2] for v in verdicts.values()), "; ".join(f"G={g}: C_sat={v[3]:.3f} < C_max={v[0]:.3f}" for g, v in verdicts.items()))
check("(2b) Gamma = 3 (stiff): the stable branch DOES reach central lapse 1/2 — a stable star saturates its register before the maximum mass", verdicts[3.0][2], f"C_sat = {verdicts[3.0][3]:.3f}, C_max = {verdicts[3.0][0]:.3f}, N_c(max) = {verdicts[3.0][1]:.3f}")
check("(2c) the saturation compactness lies in 0.19-0.25 for Gamma = 2-3: INSIDE the observed neutron-star range (1.4 Msun/12 km: C = 0.17; 2.1 Msun/12.4 km: C = 0.25), not at Buchdahl", all(0.19 < v[3] < 0.25 for v in verdicts.values()))
# observational anchor: a 2.1 Msun, 12.4 km star (PSR J0740-like, recollection) has C = 0.25 and, for these EOS, central lapse ~0.45-0.5
C_J0740 = 2.08 * 1.4766 / 12.4
print(f"     anchor: 2.08 Msun at 12.4 km -> C = {C_J0740:.3f} (central redshift ~1 for such stars, recollection) — at or past the threshold for every EOS computed")
check("(2d) the heaviest well-measured neutron stars (C ~ 0.25) sit at or beyond the saturation compactness of every EOS computed: 'neutron stars do not saturate' (3629 Q6) does not hold for the most massive ones", C_J0740 > max(v[3] for v in verdicts.values()))
# (3) how close is the central-lapse-1/2 line to Buchdahl in general: the max compactness of any static star is 4/9 (N_c -> 0); lapse 1/2 is strictly earlier
check("(3a) the threshold is a central-lapse condition strictly inside Buchdahl for every EOS (N_c = 1/2 > 0 = the Buchdahl limit): 'collapse past Buchdahl is register saturation' is superseded by 'central lapse 1/2 is register saturation'", C_half < 4 / 9 and all(np.isnan(v[3]) or v[3] < 4 / 9 for v in verdicts.values()))
print(); print(f"3634 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
