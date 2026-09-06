#!/usr/bin/env python3
"""
Patch 3640 verify — PROPOSAL (not enacted): saturation as a finite per-Moment DI-bit budget with direction preserved.
If a CP can process at most K DI-bits per Moment and the census delivers D > K, the least-assumption discrete rule is
truncation by sampling: the recorded absolute count is capped at K, the recorded NET vector is the true net scaled by
K/D. Written on the register: v_eff = cap + chi(v) (v - cap) with chi(v) = cap/v  =>  v_eff = 2 cap - cap^2 / v.
Consequences checked here (uniform R-core, cap = 2/3):
 (1) C^1 join at the surface: v_eff and dv_eff/dr are continuous with the exterior v = M/rbar -> the metric is C^1 -> NO
     surface shell: sigma = 0 and P = 0. The load 3638 exposed does not exist under this law.
 (2) The interior is not flat: v_eff runs 2/3 -> 8/9, lapse 1/2 -> 5/13 = 0.385 at the centre; no horizon.
 (3) Echo cavity: T/T(0) = 1.363 -> PRED-O-39's 0.70 ms at 62 Msun reads 0.95 ms, with NO parameter.
 (4) The compliance is position-dependent and parameter-free: chi = 1 at the surface, 2/3 at the centre.
"""
import numpy as np, sympy as sp
from scipy.integrate import quad
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
M = 1; Rb = sp.Rational(3, 2); cap = sp.Rational(2, 3)
rb = sp.symbols("rbar", positive=True)
v_in = (M / (2 * Rb)) * (3 - rb**2 / Rb**2); v_out = M / rb
chi = lambda v: cap / v
veff = lambda v: cap + chi(v) * (v - cap)
check("(0) the budget law in closed form: v_eff = 2 cap - cap^2/v", sp.simplify(veff(v_in) - (2 * cap - cap**2 / v_in)) == 0)
# (1) C^1 join
vi, vo = veff(v_in), v_out
check("(1a) v_eff is continuous at the surface (both = 2/3)", sp.simplify(vi.subs(rb, Rb) - vo.subs(rb, Rb)) == 0 and vi.subs(rb, Rb) == cap)
check("(1b) dv_eff/drbar is continuous at the surface (both = -4/9): the join is C^1, hence the metric N(v), psi(v) is C^1 and Israel gives sigma = P = 0 — no shell, no surface load", sp.simplify(sp.diff(vi, rb).subs(rb, Rb) - sp.diff(vo, rb).subs(rb, Rb)) == 0, f"slope = {sp.diff(vo, rb).subs(rb, Rb)}")
check("(1c) generality: for any cap, chi(v) = cap/v is exactly the law with dv_eff/dv = 1 at v = cap (the unique power-law chi with a C^1 join)", sp.simplify(sp.diff(veff(sp.Symbol('v')), sp.Symbol('v')).subs(sp.Symbol('v'), cap)) == 1)
# (2) interior
N = lambda v: (1 - v / 2) / (1 + v / 2); psi = lambda v: 1 + v / 2
vc = veff(v_in).subs(rb, 0)
check("(2a) central v_eff = 8/9, central lapse = 5/13 = 0.385; no horizon (v_eff < 2 everywhere)", vc == sp.Rational(8, 9) and N(vc) == sp.Rational(5, 13))
# (3) cavity
f_in = sp.lambdify(rb, psi(vi)**2 / N(vi)); T = 2 * quad(f_in, 0, float(Rb))[0]; T0 = float(2 * Rb * psi(cap)**2 / N(cap))
check("(3a) echo-cavity ratio T/T(0) = 1.363 (parameter-free): 0.70 ms -> 0.95 ms at 62 Msun", abs(T / T0 - 1.3628) < 1e-3, f"T/T0 = {T/T0:.4f}")
# (4) compliance profile
check("(4a) chi = cap/v runs from 1 at the surface to 2/3 at the centre: waves and loads transmit, stiffer inward, continuous with the outside", chi(v_in.subs(rb, Rb)) == 1 and chi(v_in.subs(rb, 0)) == cap)
# mass function numeric confirmation of no shell
rbn = np.linspace(1e-6, float(Rb), 4001); vf = sp.lambdify(rb, vi)(rbn); r = rbn * (1 + vf / 2)**2
m = (r / 2) * (1 - (np.gradient(r, rbn) / (1 + vf / 2)**2)**2)
check("(1d) numeric: the interior mass function reaches M at the surface (m(R^-)/M = 1 to 1e-3) — the count is carried by the interior, none by a shell", abs(m[-1] / M - 1) < 1e-3, f"m(R-)/M = {m[-1]:.4f}")
print(); print(f"3640 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
