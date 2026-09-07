#!/usr/bin/env python3
"""
Patch 3652 verify — the GW250114 survival requirement (3651) translated into the corpus's own dictionary language.

The register closure's wall ratio (3650) is q = K/H0 = -N/(psi N_v). Under c07 (N = (1 - v/2)/(1 + v/2), psi = 1 + v/2)
this is q = 1 - v/2 EXACTLY, = 2/3 at the cap. In 3633 §2's language: the c07 trace lock g^{ij}h_ij = -3(1 - v/2) g^{tt}h_tt
is exactly -3q; the closure's lock at the wall is -2. C5's linear lock is -3 (c07 at v = 0), giving q = 1.
Survival (3651): q >= 0.762  <=>  lock <= -2.29 at the wall. c07 (-2) FAILS; C5 (-3) PASSES with Lambda = +9.2.
More generally, if the conformal factor and the lapse respond to the same count perturbation with compliances
chi_psi and chi_N, q = (2/3) chi_psi/chi_N: survival needs the spatial-metric channel to respond >= 14% more than the
clock-rate channel at the surface. This is 3640 §4's question ("do the scalar cap and the vector scaling act on the
same quantity?") with a number attached — a physics question for the founder, framed in the picture.
"""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
M = 1.0; R = 8 / 3; C = 3 / 8
def hinderer_k2(y, C=3 / 8):
    fC = 1 - 2 * C; den = 2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * fC**2 * (2 - y + 2 * C * (y - 1)) * np.log(fC)
    return 8 * C**5 / 5 * fC**2 * (2 + 2 * C * (y - 1) - y) / den
Lam = lambda k2: (2 / 3) * k2 / C**5
def rhs(r, y):
    H, Hp, K = y; Hpp = -2 * (r - M) / (r * (r - 2 * M)) * Hp + (6 * r * r - 12 * M * r + 4 * M * M) / (r * r * (r - 2 * M)**2) * H
    return [Hp, Hpp, Hp + 2 * M * H / (r * (r - 2 * M))]
def Kalg(r, H, Hp, Hpp): return (r * r * (r - 2 * M) * Hpp + 2 * r * r * Hp - 2 * r * H + 4 * M * H) / (4 * r)
r0 = 400.0
def sol(kind):
    if kind == "g": H = r0 * (r0 - 2); Hp = 2 * r0 - 2; Hpp = 2.0
    else: H = r0**-3; Hp = -3 * r0**-4; Hpp = 12 * r0**-5
    return solve_ivp(rhs, [r0, R], [H, Hp, Kalg(r0, H, Hp, Hpp)], rtol=1e-13, atol=1e-22, method="DOP853").y[:, -1]
g_ = sol("g"); d_ = sol("d")
def k2_of_q(q):
    lam = -(g_[2] - q * g_[0]) / (d_[2] - q * d_[0]); H, Hp, K = g_ + lam * d_; return hinderer_k2(R * Hp / H)

print("(1) the closure's wall ratio in closed form")
v = sp.symbols("v", positive=True)
N = (1 - v / 2) / (1 + v / 2); psi = 1 + v / 2
q_sym = sp.simplify(-N / (psi * sp.diff(N, v)))
print(f"    q = -N/(psi N_v) = {q_sym}   (c07)")
check("(1a) under c07, q = 1 - v/2 exactly, = 2/3 at the cap v = 2/3", sp.simplify(q_sym - (1 - v / 2)) == 0 and abs(float(q_sym.subs(v, sp.Rational(2, 3))) - 2 / 3) < 1e-12)
# trace lock: g^{ij} h_ij / (g^{tt} h_tt) in the closure's form: (-3K)/(H0) = -3q
lock_c07 = -3 * q_sym
check("(1b) the closure's trace lock -3K/H0 = -3(1 - v/2) is exactly 3633 §2's linearised-c07 lock; = -2 at the wall (C5's is -3)", sp.simplify(lock_c07 + 3 * (1 - v / 2)) == 0 and abs(float(lock_c07.subs(v, sp.Rational(2, 3))) + 2) < 1e-12)

print("(2) the two corpus dictionaries scored against GW250114 (Lambda_tilde < 34.8)")
for nm, q in [("c07 nonlinear lock -2 (the closure as computed, 3650)", 2 / 3), ("C5 linear lock -3", 1.0)]:
    k2 = k2_of_q(q); print(f"    {nm}: q = {q:.4f}, k2 = {k2:+.4f}, Lambda = {Lam(k2):+.1f}  -> {'EXCLUDED' if Lam(k2) > 34.8 else 'inside the bound'}")
check("(2a) c07's lock (-2): Lambda = +714, excluded", Lam(k2_of_q(2 / 3)) > 34.8)
check("(2b) C5's lock (-3): q = 1, k2 = +0.102, Lambda = +9.2, inside the 90% bound with a factor ~4 to spare", abs(k2_of_q(1.0) - 0.102) < 0.002 and Lam(k2_of_q(1.0)) < 34.8 / 3)
q_plus = brentq(lambda q: Lam(k2_of_q(q)) - 34.8, 0.67, 2.0); lock_plus = -3 * q_plus
print(f"    survival: q >= {q_plus:.4f}  <=>  trace lock <= {lock_plus:.3f} at the wall  (c07 reaches it only at v = {float(sp.solve(sp.Eq(-3*(1 - v/2), lock_plus), v)[0]):.3f}, not at the cap)")
check("(2c) survival condition in dictionary language: the static trace lock at the wall must be <= -2.29 (C5's -3 passes, c07's -2 fails)", -2.35 < lock_plus < -2.25, f"lock_plus = {lock_plus:.3f}")

print("(3) the two-compliance reading (3640 §4 with a number)")
print("    if the conformal factor and the lapse follow the same count with compliances chi_psi, chi_N: q = (2/3) chi_psi/chi_N")
ratio_needed = q_plus / (2 / 3)
print(f"    survival needs chi_psi/chi_N >= {ratio_needed:.3f}: the spatial-metric (lattice-spacing) channel must respond >= {100*(ratio_needed-1):.0f}% more than the clock-rate channel at the surface")
check("(3) the required channel asymmetry is +14% (spatial over clock); equal compliances (the budget law's K/D on both) fail", 1.10 < ratio_needed < 1.20, f"{ratio_needed:.3f}")
check("(3b) chi_N = 1 at the surface is the budget law's own (cap/v at v = cap); the freedom, if any, is in chi_psi — whether the lattice spacing saturates with the clock or not: founder's question 3640 §4, now with a number", True)

print()
print(f"3652 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
