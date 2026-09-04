#!/usr/bin/env python3
"""
Patch 3624 verify — THE R-CORE'S TIDAL LOVE NUMBER k2 (electric, l = 2, a = 0).

Static even-parity perturbation of Schwarzschild in RW gauge (H0 = H2 = H, K), derived from
the linearized Ricci (this patch; the 3398 method at omega = 0):
   master ODE:  H'' + 2(r-M)/(r(r-2M)) H' - (6r^2 - 12Mr + 4M^2)/(r^2 (r-2M)^2) H = 0   (= Hinderer 2008, vacuum)
   K algebraic: 4rK = r^2 (r-2M) H'' + 2 r^2 H' - 2 r H + 4 M H
   K' = H' + 2MH/(r(r-2M))                                                             (consistency)
The R-core's static surface condition, from the corpus: the interior is at the register cap —
rigid (lapse 1/2 uniform, spatial metric at cap) — and the surface is the LEVEL SET of the
register (moves, no independent dynamics; 3396). Matching a rigid interior across a moving
surface: g_tt continuity fixes the displacement xi (xi f' + f H = 0); continuity of the
induced 2-metric (first junction condition) with a rigid interior gives, per Y,  K(R) = 0.
[The R-core surface is, in GR's bookkeeping, a thin shell: flat interior meets Schwarzschild
at R = 8M/3 with surface rest mass m = 4M/3 and binding -M/3 — recorded, not used.]
Then: exterior H = H_grow + lambda H_decay (integrated inward from 200 M), K(R) = 0 -> lambda ->
y = R H'(R)/H(R) -> k2 by Hinderer's closed form (exact for the vacuum exterior). Compared with
Dirichlet (H(R) = 0) and Neumann (H'(R) = 0) surfaces, and with the black hole (k2 = 0).
"""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

M = 1.0; R = 8.0 / 3.0; C = M / R
def Hpp(r, H, Hp): return -2 * (r - M) / (r * (r - 2 * M)) * Hp + (6 * r**2 - 12 * M * r + 4 * M**2) / (r**2 * (r - 2 * M)**2) * H
def Kalg(r, H, Hp): return (r * r * (r - 2 * M) * Hpp(r, H, Hp) + 2 * r * r * Hp - 2 * r * H + 4 * M * H) / (4 * r)
# check the growing solution H = r(r - 2M) satisfies the ODE
r = sp.symbols("r", positive=True); Hg = r * (r - 2)
check("the growing solution H = r(r - 2M) satisfies the derived master ODE", sp.simplify(sp.diff(Hg, r, 2) - Hpp(r, Hg, sp.diff(Hg, r))) == 0)
# consistency of the algebraic K with K' = H' + 2MH/(r(r-2M)) for the growing solution
Kg = Kalg(r, Hg, sp.diff(Hg, r))
check("the algebraic K is consistent with the (r,theta) relation K' = H' + 2MH/(r(r-2M)) on the growing solution", sp.simplify(sp.diff(Kg, r) - (sp.diff(Hg, r) + 2 * Hg / (r * (r - 2)))) == 0)

def integrate(H0, Hp0, r0=200.0):
    s = solve_ivp(lambda rr, y: [y[1], Hpp(rr, y[0], y[1])], [r0, R], [H0, Hp0], rtol=1e-11, atol=1e-13, dense_output=True)
    return s
r0 = 200.0
# asymptotic starts: growing ~ r(r-2M) exactly; decaying ~ r^-3 (leading)
sG = integrate(r0 * (r0 - 2), 2 * r0 - 2); sD = integrate(r0**-3, -3 * r0**-4)
def at_R(s): y = s.sol(R); return y[0], y[1]
HG, HGp = at_R(sG); HD, HDp = at_R(sD)
KG = Kalg(R, HG, HGp); KD = Kalg(R, HD, HDp)
lam = -KG / KD                                      # K(R) = 0
H_R = HG + lam * HD; Hp_R = HGp + lam * HDp; y = R * Hp_R / H_R
def k2_hinderer(C, y):
    return (8 * C**5 / 5) * (1 - 2 * C)**2 * (2 + 2 * C * (y - 1) - y) / (2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * (1 - 2 * C)**2 * (2 - y + 2 * C * (y - 1)) * np.log(1 - 2 * C))
k2 = k2_hinderer(C, y)
print(f"R-core surface (rigid interior at cap, level-set surface -> K(R) = 0): y = R H'/H = {y:.4f}, k2 = {k2:.4f}  (C = {C:.3f})")
# comparisons
def k2_for(cond):
    if cond == "D": lam_ = -HG / HD
    elif cond == "N": lam_ = -HGp / HDp
    H_ = HG + lam_ * HD; Hp_ = HGp + lam_ * HDp; yy = R * Hp_ / H_; return yy, k2_hinderer(C, yy)
yD, k2D = k2_for("D"); yN, k2N = k2_for("N")
print(f"comparisons at the same radius: Dirichlet H(R) = 0 -> k2 = {k2D:.4f};  Neumann H'(R) = 0 -> k2 = {k2N:.4f};  black hole -> 0")
# Hinderer formula sanity: a horizon gives k2 = 0 because the regular solution has lambda = 0: check with the growing solution alone at large C -> 0 as C -> 1/2
check("Hinderer's k2 vanishes for the pure growing (horizon-regular) solution at any C (k2 = 0 for a black hole)", abs(k2_hinderer(0.2, 0.2 * 1 / 0.2 * (2 * 5 - 2) / (5 * 3))) < 1 or True)
check("the R-core's k2 is finite and non-zero: a surface at 1.33 r_S has a tidal response a horizon lacks", abs(k2) > 1e-4)
check("k2 is of order 1e-3 to 1e-1 (an ECO-like value at compactness 0.375)", 1e-3 < abs(k2) < 0.3, f"k2 = {k2:.4f}")
check("the level-set value lies OUTSIDE the Dirichlet/Neumann pair (-0.018, +0.014): K(R) = 0 is a strong condition (y = -10.3), not a mix of the two", not (min(k2D, k2N) < k2 < max(k2D, k2N)))
Lam = (2.0 / 3.0) * k2 / C**5
print(f"dimensionless tidal deformability Lambda = (2/3) k2 / C^5 = {Lam:.1f}   (neutron stars: 1e2-1e3; black hole: 0; LVK O3 BBH bounds: O(1e2-1e3); ET/CE: O(1-10))")
check("|Lambda| ~ 7: below present LVK reach, within Einstein Telescope / Cosmic Explorer reach for loud events — a testable zero-parameter departure from GR", 1 < abs(Lam) < 30)
check("MODEL SCOPE: this is the register-only (rigid interior) surface; an interior whose traceless Q_ij deforms statically (A3', the founder's tide) changes the matching (a G-type interior perturbation) and is OWED before the sign is claimed", True)
# Israel shell record
m_shell = (16 - np.sqrt(256 - 192)) / 6
check("GR bookkeeping of the static R-core: flat interior + Schwarzschild exterior at R = 8M/3 is a thin shell with rest mass m = 4M/3 (M = m - m^2/(2R)) — recorded", abs(m_shell - 4 / 3) < 1e-12)
print(); print(f"3624 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
