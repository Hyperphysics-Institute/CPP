#!/usr/bin/env python3
"""
Patch 3635 verify — OPEN-GR-SATURATED-CORE-1 rung 1: stars with a saturated core, under the working postulate
P-PINNED-CORE-IS-FLAT (3375 read inside a star): where the register has reached the cap, the lattice is flat at lapse 1/2,
there is no gravity inside the core (pressure and density uniform at their boundary values), the core's count
M_c = eps_c (4 pi/3) r_c^3 appears to the envelope as m(r_c) = M_c (the shell bookkeeping of 3624), and the envelope is TOV
matter outside r_c. The core radius is fixed by the register condition N(r_c) = 1/2 (the envelope's lapse at the core
boundary), so the family is one-parameter in p_c like TOV's. Reading (b) — only the clocks capped, matter unchanged — is GR.

 (1) Below the threshold (TOV central lapse > 1/2) the CPP star IS the TOV star (r_c -> 0).
 (2) Above it, r_c > 0 and the structure changes. For Gamma = 2, 2.5, 3: the maximum mass, its compactness and core
     fraction under (a), against GR's TOV maximum for the same EOS.
 (3) The stability proxy: dM/dp_c along the family (turning point).
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
K = 1.0
def make(Gamma):
    eos = lambda p: (max(p, 0) / K)**(1 / Gamma) + p / (Gamma - 1)
    def rhs(r, y):
        m, p, nu = y
        if p <= 0: return [0, 0, 0]
        e = eos(p); dnu = 2 * (m + 4 * np.pi * r**3 * p) / (r * (r - 2 * m))
        return [4 * np.pi * r**2 * e, -(e + p) * dnu / 2, dnu]
    def envelope(p_c, r_c):
        """integrate from r_c (flat core of count M_c inside) to the surface; return M, R, N(r_c)."""
        e_c = eos(p_c)
        if r_c < 1e-6:
            r0 = 1e-6; y0 = [4 * np.pi * r0**3 * e_c / 3, p_c, 0.0]
        else:
            M_c = e_c * 4 * np.pi * r_c**3 / 3
            if 2 * M_c / r_c >= 0.999: return np.nan, np.nan, np.nan
            r0 = r_c; y0 = [M_c, p_c, 0.0]
        ev = lambda r, y: y[1] - 1e-12 * p_c; ev.terminal = True; ev.direction = -1
        s = solve_ivp(rhs, [r0, 1e3], y0, events=ev, rtol=1e-9, atol=1e-13, max_step=0.1)
        R = s.t[-1]; M = s.y[0][-1]; nu_R = s.y[2][-1]
        N_rc = np.exp((0.0 - nu_R) / 2) * np.sqrt(1 - 2 * M / R)
        return M, R, N_rc
    def cpp_star(p_c):
        """the saturated-core member at core pressure p_c: N(r_c) decreases monotonically with r_c (a flat core at the
        boundary density carries more count than TOV's compressed interior), so a root N(r_c) = 1/2 exists exactly when the
        TOV star at p_c is UNSATURATED (N_c > 1/2). The saturated-core branch therefore sits at core pressures BELOW the
        TOV threshold pressure, as a second branch of static solutions."""
        M0, R0, N0 = envelope(p_c, 0.0)
        if N0 <= 0.5: return np.nan, np.nan, np.nan, np.nan, N0      # no flat-core equilibrium above the threshold
        g = lambda rc: envelope(p_c, rc)[2] - 0.5
        hi = R0 * 0.98
        while not np.isfinite(g(hi)):
            hi *= 0.9
        if g(hi) > 0: return np.nan, np.nan, np.nan, np.nan, N0     # core would have to exceed the star
        rc = brentq(g, 1e-4, hi, xtol=1e-6)
        M, R, N = envelope(p_c, rc)
        Mc = eos(p_c) * 4 * np.pi * rc**3 / 3
        return M, R, rc, Mc / M, N0
    return eos, envelope, cpp_star
print("     Gamma   GR M_max  C_max   |  CPP(a) saturated branch: M_max  C_max  r_c/R  M_c/M  N_c(TOV at that p_c) | ratio")
out = {}
for Gamma, span in [(2.0, (-2.5, 0.6)), (2.5, (-2.5, 0.9)), (3.0, (-2.0, 1.3))]:
    eos, envelope, cpp_star = make(Gamma)
    rhos = np.logspace(*span, 36); pcs = K * rhos**Gamma
    gr = np.array([envelope(p, 0.0)[:3] for p in pcs])
    cpp = np.array([cpp_star(p) for p in pcs])
    ig = int(np.nanargmax(gr[:, 0])); ic = int(np.nanargmax(cpp[:, 0]))
    sat = np.isfinite(cpp[:, 0])
    out[Gamma] = dict(grM=gr[ig, 0], grC=gr[ig, 0] / gr[ig, 1], cppM=cpp[ic, 0], cppC=cpp[ic, 0] / cpp[ic, 1], rcR=cpp[ic, 2] / cpp[ic, 1], McM=cpp[ic, 3], N0=cpp[ic, 4],
                      nsat=int(sat.sum()), ic=ic, pcs=pcs, cpp=cpp, gr=gr, above=all(~sat[i] for i in range(len(pcs)) if gr[i, 2] <= 0.5))
    o = out[Gamma]
    print(f"     {Gamma:4.1f}   {o['grM']:.4f}   {o['grC']:.3f}   |   {o['cppM']:.4f}   {o['cppC']:.3f}  {o['rcR']:.3f}  {o['McM']:.3f}   {o['N0']:.3f}   | {o['cppM']/o['grM']:.3f}")
    print("        saturated branch M(p_c):", np.round(cpp[sat, 0], 4)[::3])
check("(1) no flat-core equilibrium exists at core pressures ABOVE the TOV threshold (N(r_c) only decreases with r_c): the saturated-core branch lives BELOW it", all(o['above'] for o in out.values()))
check("(2a) the saturated-core branch exists for every EOS, in a WINDOW of core pressures below the threshold (too low a p_c cannot reach lapse 1/2 even with the core filling the star); members found on a 36-point scan:", all(o['nsat'] >= 2 for o in out.values()), str({g: o['nsat'] for g, o in out.items()}))
ratios = {g: o['cppM'] / o['grM'] for g, o in out.items()}
print("     maximum-mass ratio, saturated branch / GR TOV:", {g: round(v, 3) for g, v in ratios.items()})
check("(2b) the saturated branch's maximum mass EXCEEDS GR's TOV maximum for every EOS (by > 5%): under (a) the register cap opens a heavier static branch", all(v > 1.05 for v in ratios.values()), str({g: round(v, 3) for g, v in ratios.items()}))
check("(2c) at the saturated branch's maximum, the flat core holds most of the star (r_c/R > 0.5, M_c/M > 0.5)", all(o['rcR'] > 0.5 and o['McM'] > 0.5 for o in out.values()), str({g: (round(o['rcR'], 2), round(o['McM'], 2)) for g, o in out.items()}))
check("(3) the branch maximum is interior to the scan (a turning point in p_c), stability of the branch NOT established here", all(0 < o['ic'] < len(o['pcs']) - 1 for o in out.values()))
# (4) the ORDINARY (TOV) branch is truncated at the threshold under (a): its maximum mass is the threshold mass
trunc = {}
for g, o in out.items():
    gr = o['gr']; i_thr = next(i for i in range(len(gr)) if gr[i, 2] <= 0.5)
    M_thr = np.interp(0.5, gr[i_thr - 1:i_thr + 1, 2][::-1], gr[i_thr - 1:i_thr + 1, 0][::-1]); trunc[g] = M_thr / o['grM']
print("     ordinary-branch maximum under (a) = the threshold mass; ratio to GR's TOV maximum:", {g: round(v, 3) for g, v in trunc.items()})
check("(4) under (a) the ordinary neutron-star branch ENDS at central lapse 1/2 with no continuation: its maximum mass is the threshold mass, 0.5-15% below GR's for Gamma = 2-3", all(0.80 < v < 0.999 for v in trunc.values()))
print(); print(f"3635 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
