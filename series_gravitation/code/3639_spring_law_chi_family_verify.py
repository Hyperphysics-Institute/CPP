#!/usr/bin/env python3
"""
Patch 3639 verify — founder picture R-CAP-SPRING (5 Sep 2026): the loaded register settles (elastic), not creeps.
The minimal law consistent with it: register = demand for demand <= cap; cap + chi (demand - cap) above it, 0 <= chi <= 1
(chi = 0 rigid cap, chi = 1 no cap = the PSR log law continued = isotropic Schwarzschild everywhere).
Note: the corpus's PSR law N = (1 - v/2)/(1 + v/2) IS isotropic Schwarzschild's lapse and continues smoothly past v = 2/3
to N = 0 at v = 2; the floor at v = 2/3 is an added rule, and 'third order assumed' (3390) is exactly where a spring lives.
 (1) R-core interior under the chi-law (uniform count, census v(rbar) = (M/2Rbar)(3 - rbar^2/Rbar^2), Rbar = 3M/2):
     v_eff = 2/3 + chi (v - 2/3); lapse N(v_eff), conformal psi(v_eff). The surface stays at v = 2/3 (areal 8M/3) for every
     chi (the exterior demand is unchanged). Central lapse: 1/2 at chi = 0 -> 1/3 at chi = 1.
 (2) The echo cavity: coordinate light-crossing time of the interior diameter, T(chi) = 2 int_0^Rbar psi^2/N drbar, relative
     to the flat-at-1/2 cavity (chi = 0). PRED-O-39's 0.70 ms (62 Msun) scales by T(chi)/T(0).
 (3) The interior mass bookkeeping: with chi > 0 the interior carries curvature; the fraction of M appearing as interior
     mass function vs the surface shell — the shell load P/sigma decreases with chi (the spring shares the load).
"""
import numpy as np, sympy as sp
from scipy.integrate import quad
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
M = 1.0; Rbar = 1.5 * M
N = lambda v: (1 - v / 2) / (1 + v / 2); psi = lambda v: 1 + v / 2
v_census = lambda rb: (M / (2 * Rbar)) * (3 - rb**2 / Rbar**2)          # uniform ball, lattice coordinates
v_eff = lambda rb, chi: 2 / 3 + chi * (v_census(rb) - 2 / 3)
check("(1a) the census at the surface is exactly the cap: v(Rbar) = 2/3, surface at areal Rbar psi^2 = 8M/3 for every chi", abs(v_census(Rbar) - 2 / 3) < 1e-12 and abs(Rbar * psi(2 / 3)**2 - 8 / 3) < 1e-12)
check("(1b) central lapse: 1/2 at chi = 0, 1/3 at chi = 1 (v_c = 1: the isotropic-Schwarzschild continuation)", abs(N(v_eff(0, 0)) - 0.5) < 1e-12 and abs(N(v_eff(0, 1)) - 1 / 3) < 1e-12)
check("(1c) the interior lapse never vanishes for any chi in [0, 1] (no horizon forms: v_eff <= 1 < 2)", all(N(v_eff(0, ch)) > 0 for ch in np.linspace(0, 1, 11)))
# (2) light-crossing time (coordinate t): dt = psi^2/N drbar for radial null in the census metric -N^2 dt^2 + psi^4 d x^2
T = lambda chi: 2 * quad(lambda rb: psi(v_eff(rb, chi))**2 / N(v_eff(rb, chi)), 0, Rbar)[0]
T0 = T(0)
check("(2a) chi = 0 reproduces the flat-at-1/2 cavity: T(0) = 2 Rbar psi(2/3)^2 / (1/2) = 2 (8M/3) / (1/2) = 32M/3", abs(T0 - 32 / 3) < 1e-9, f"T(0) = {T0:.6f} M")
chis = [0, 0.1, 0.25, 0.5, 0.75, 1.0]
ratios = [T(ch) / T0 for ch in chis]
print("     echo-cavity time ratio T(chi)/T(0):", {ch: round(r, 4) for ch, r in zip(chis, ratios)})
check("(2b) T(chi) increases monotonically with chi (a softer floor deepens the interior and lengthens the cavity)", all(np.diff(ratios) > 0))
check("(2c) the full-yield cavity is ~1.5x the flat one: T(1)/T(0) in [1.3, 1.7] — PRED-O-39's 0.70 ms would read 0.70 ms x T(chi)/T(0); an echo delay measures chi", 1.3 < ratios[-1] < 1.7, f"{ratios[-1]:.3f}")
# (3) interior mass function from the census metric's spatial geometry: areal radius r = rbar psi^2, m(r) = (r/2)(1 - (dr/dl)^2) with dl = psi^2 drbar
def m_interior(chi):
    rb = np.linspace(1e-6, Rbar, 4001); ve = v_eff(rb, chi); r = rb * psi(ve)**2
    drdrb = np.gradient(r, rb); dl_drb = psi(ve)**2
    return r, (r / 2) * (1 - (drdrb / dl_drb)**2)
fracs = {}
for ch in [0, 0.25, 0.5, 1.0]:
    r, m = m_interior(ch); fracs[ch] = m[-1] / M
print("     interior mass function at the surface, m(R^-)/M (the rest is the surface shell):", {ch: round(v, 3) for ch, v in fracs.items()})
check("(3a) chi = 0: the interior is flat, m(R^-) = 0 — all of M is the shell (3624's 4M/3 rest-mass bookkeeping)", abs(fracs[0]) < 1e-6)
check("(3b) the interior mass function grows with chi: the spring takes up part of the count and the surface shell's share falls", fracs[0.25] > 0 and fracs[0.5] > fracs[0.25] and fracs[1.0] > fracs[0.5])
print(); print(f"3639 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
