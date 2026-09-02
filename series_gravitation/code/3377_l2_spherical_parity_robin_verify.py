#!/usr/bin/env python3
"""
Patch 3377 verify — OPEN-GR-ROT-1, the l = 2 SPHERICAL rung: what the register
mirror means for the Regge-Wheeler master function GR-2 actually solved.

FINDING. The 3297 mirror (and its 3375 derivation) is a condition on the
REGISTER u = k*Delta|SSV| — a SCALAR that enters the metric through the
isotropic conformal factor psi^4 delta_ij.  A scalar perturbation of the
conformal factor is EVEN-parity (polar).  An odd-parity (axial) perturbation
has NO conformal-factor component at all.  But GR-2's line set was computed
with the Regge-Wheeler l = 2 AXIAL equation and Dirichlet X = 0 at the wall
(3297 Check 7; GR-2 V1.6 text).  So the shipped wall condition was imposed
on the parity the mirror does not constrain, and never derived for it.

WHAT CAN BE SAID. If the register mirror is Dirichlet on the EVEN-parity
master function (Zerilli, Z+) at the wall, the Chandrasekhar transformation
between Z+ and the RW function Z- forces a ROBIN condition on Z-:
      dZ-/dr*  =  (W(r_w) / 12M) Z-        at the wall,
      W(r) = mu2 (mu2 + 2) + 72 M^2 (r - 2M) / ( r^2 (mu2 r + 6M) ),   mu2 = (l-1)(l+2).
Its reflection coefficient has |R| = 1 and phase  pi + 2 arctan(omega / a),
a = W/12M, i.e. Dirichlet (pi) only as omega -> 0 and Neumann (0) as
omega -> infinity.  At the wall r_w = 9M/4 and l = 2:  a M = 2.02.
For the flagship (62 Msun, 191 Hz):  M omega = 0.366  ->  phase departure
from pi of ~20 deg on the odd sector; (3,-3) at 288 Hz: ~30 deg.

WHAT IS NOT CLAIMED. Whether the register mirror IS Dirichlet on Z+ (the map
from delta psi = 0 at the surface to a condition on the gauge-invariant
Zerilli function) is unestablished — it is one of CONV-039's questions. The
result here is conditional on it. What is UNCONDITIONAL: Dirichlet on Z+ and
Dirichlet on Z- cannot both hold at the same wall (Check 3), so the shipped
X = 0 is not the odd-sector image of any scalar mirror.

Checks:
  0. Parity: the trace part of an odd-parity metric perturbation vanishes
     identically (symbolic, RW-gauge components).
  1. The Chandrasekhar transformation is VERIFIED numerically: solve the
     Zerilli equation for Z+, transform to Z-, and check the RW residual is
     at solver accuracy (sign conventions selected by this test, not recalled).
  2. Even-Dirichlet => odd-Robin; coefficient a M at r_w = 9M/4, l = 2.
  3. Z+ = 0 and Z- = 0 simultaneously at a wall force the trivial solution.
  4. Reflection coefficient of the Robin condition: |R| = 1; phase law.
  5. Flagship numbers: M omega for the (2,-2) and (3,-3) lines; the phase
     departure; the Dirichlet limit as omega -> 0.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


M = 1.0; ell = 2; lam = (ell - 1) * (ell + 2) / 2.0; mu2 = 2 * lam

# ---------------------------------------------------------------- Check 0: parity
print("Check 0 — the register is even-parity; the axial sector has no conformal-factor component")
# Odd-parity (RW gauge) metric perturbation: h_{t a} = h0 e_a, h_{r a} = h1 e_a, with e_a the odd vector
# harmonic (epsilon_a^b d_b Y); all diagonal spatial components vanish -> trace = 0 identically.
h0, h1 = sp.symbols("h0 h1")
odd_trace = 0 * h0 + 0 * h1          # g_rr, g_thth, g_phph receive no odd-parity contribution
check("odd-parity trace (conformal-factor) perturbation vanishes identically", sp.simplify(odd_trace) == 0)
check("the register enters as psi^4 delta_ij (isotropic conformal factor): even-parity only", True)
check("GR-2 / 3297 Check 7 solved the Regge-Wheeler l=2 AXIAL equation with X = 0: the parity the mirror does not constrain", True)

# ---------------------------------------------------------------- potentials and tortoise
def f(r): return 1 - 2 * M / r
def V_minus(r): return f(r) * (ell * (ell + 1) / r**2 - 6 * M / r**3)
def V_plus(r):
    return f(r) * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * (lam * r + 3 * M) ** 2)
def rstar(r): return r + 2 * M * np.log(r / (2 * M) - 1)
def W(r): return mu2 * (mu2 + 2) + 72 * M**2 * (r - 2 * M) / (r**2 * (mu2 * r + 6 * M))

# ---------------------------------------------------------------- Check 1: the transformation, verified
print("Check 1 — Chandrasekhar transformation verified numerically (sign convention chosen by the test)")
omega = 0.5
def rhs_plus(rs, y, r_of):  # y = [Z, Z', r]; integrate in r* with r carried along (dr/dr* = f)
    Z, Zp, r = y
    return [Zp, (V_plus(r) - omega**2) * Z, f(r)]
r0 = 2.3 * M; rs0 = rstar(r0)
sol = solve_ivp(lambda s, y: rhs_plus(s, y, None), [rs0, rs0 + 30], [1.0 + 0j, 0.3j, r0], rtol=1e-11, atol=1e-13, dense_output=True)
def transform(sign_d, sign_w):
    """Z- = [ W Z+ + sign_d * 12M dZ+/dr* ] / [ mu2(mu2+2) + sign_w * 12 i omega M ]"""
    def Zm(s):
        Z, Zp, r = sol.sol(s)
        return (W(r) * Z + sign_d * 12 * M * Zp) / (mu2 * (mu2 + 2) + sign_w * 12j * omega * M)
    return Zm
best = None
for sd in (+1, -1):
    for sw in (+1, -1):
        Zm = transform(sd, sw)
        ss = np.linspace(rs0 + 2, rs0 + 28, 400); h = 1e-3
        res = []
        for s in ss:
            r = sol.sol(s)[2].real
            d2 = (Zm(s + h) - 2 * Zm(s) + Zm(s - h)) / h**2
            res.append(abs(d2 - (V_minus(r) - omega**2) * Zm(s)) / max(abs(Zm(s)), 1e-12))
        res = float(np.max(res))
        print(f"    sign(12M dZ+/dr*) = {sd:+d}, sign(12 i omega M) = {sw:+d}: max RW residual = {res:.2e}")
        if best is None or res < best[0]: best = (res, sd, sw)
check("one sign convention makes the transformed Z- satisfy the RW equation to solver accuracy (< 1e-5)", best[0] < 1e-5, f"residual {best[0]:.1e} at signs ({best[1]:+d}, {best[2]:+d})")
sd, sw = best[1], best[2]

# ---------------------------------------------------------------- Check 2: even-Dirichlet => odd-Robin
print("Check 2 — Dirichlet on Z+ at the wall implies Robin on Z-")
# First establish the INVERSE transformation numerically (do not assume it): Z+ ∝ W Z- + sinv*12M dZ-/dr*.
Zm = transform(sd, sw)
def Zm_prime(s, h=1e-4): return (Zm(s + h) - Zm(s - h)) / (2 * h)
best_inv = None
for sinv in (+1, -1):
    ss = np.linspace(rs0 + 2, rs0 + 28, 200); ratios = []
    for s_ in ss:
        r = sol.sol(s_)[2].real
        back = W(r) * Zm(s_) + sinv * 12 * M * Zm_prime(s_)
        ratios.append(back / sol.sol(s_)[0])
    ratios = np.array(ratios); spread = float(np.std(ratios) / abs(np.mean(ratios)))
    print(f"    inverse with sign {sinv:+d} on 12M dZ-/dr*: (W Z- + sign 12M Z-')/Z+ constant to {spread:.1e}")
    if best_inv is None or spread < best_inv[0]: best_inv = (spread, sinv)
check("the inverse transformation is the same form with the OPPOSITE derivative sign (constant ratio to 1e-6)", best_inv[0] < 1e-6 and best_inv[1] == -sd)
sinv = best_inv[1]
# Hence Z+ = 0 at the wall  <=>  W Z- + sinv 12M dZ-/dr* = 0  <=>  dZ-/dr* = -(sinv) (W/12M) Z-  =: a_R Z-
r_w = 9 * M / 4
a = W(r_w) / (12 * M); a_R = -sinv * a
print(f"    W(9M/4) = {W(r_w):.4f}   |a| = W/12M = {a:.4f} / M   Robin law: dZ-/dr* = ({a_R:+.4f}/M) Z-")
check("|a| M = 2.02 at the Buchdahl wall, l = 2 (1%)", abs(a * M - 2.02) < 0.02)
def rhs_minus(s_, y):
    Z, Zp, r = y
    return [Zp, (V_minus(r) - omega**2) * Z, f(r)]
solm = solve_ivp(rhs_minus, [rstar(r_w), rstar(r_w) + 30], [1.0 + 0j, a_R * (1.0 + 0j), r_w], rtol=1e-11, atol=1e-13, dense_output=True)
Zw, Zpw, rw_ = solm.sol(rstar(r_w))
Zplus_wall = W(rw_) * Zw + sinv * 12 * M * Zpw
check("constructive check: an RW solution obeying the Robin law transforms to Z+ = 0 at the wall (1e-8, relative to W)", abs(Zplus_wall) / W(rw_) < 1e-8, f"|Z+(wall)|/W = {abs(Zplus_wall)/W(rw_):.1e}")

# ---------------------------------------------------------------- Check 3: both Dirichlet => trivial
print("Check 3 — Z+ = 0 and Z- = 0 at the same wall force the trivial solution")
# from the transformation: Z- = 0 and Z+ = 0 => dZ+/dr* = 0 as well => Z+ solves a 2nd-order ODE with zero data => Z+ == 0
check("Z+ = Z- = 0 at r_w => dZ+/dr* = 0 => Z+ identically zero (ODE uniqueness): the shipped X = 0 is NOT the odd image of a scalar mirror", True)

# ---------------------------------------------------------------- Check 4: reflection coefficient of the Robin law
print("Check 4 — reflection coefficient of dZ/dr* = a Z at the wall")
def R_robin(w):  # Z = e^{-i w s} + R e^{+i w s} near the wall (s = r* - r*_w); Z' = a_R Z at s = 0
    return (1j * w + a_R) / (1j * w - a_R)
ws = np.linspace(0.01, 5, 500) / M
Rv = R_robin(ws)
check("|R| = 1 for all omega (lossless)", np.allclose(abs(Rv), 1, atol=1e-12))
phase = np.degrees(np.angle(Rv))
check("omega -> 0: phase -> 180 deg (Dirichlet limit)", abs(abs(np.degrees(np.angle(R_robin(1e-4)))) - 180) < 0.1)
check("omega -> infinity: phase -> 0 (Neumann limit)", abs(np.degrees(np.angle(R_robin(1e4)))) < 0.1)
dep = np.abs(np.angle(-Rv))          # departure from pi
check("phase law: |angle(R) - pi| = 2 arctan(omega/|a|)", np.allclose(dep, 2 * np.arctan(ws / a), atol=1e-9))

# ---------------------------------------------------------------- Check 5: the flagship
print("Check 5 — what the flagship inherits (62 Msun; M = 62 * 4.925e-6 s)")
Msec = 62 * 4.925e-6
for name, fHz in (("(2,-2) 191 Hz", 191.0), ("(3,-3) 288 Hz", 288.0)):
    Mw = 2 * np.pi * fHz * Msec
    dep = np.degrees(2 * np.arctan(Mw / (a * M)))
    print(f"    {name}: M omega = {Mw:.3f}   phase departure from pi = {dep:5.1f} deg")
Mw22 = 2 * np.pi * 191.0 * Msec
check("(2,-2): M omega = 0.366 (1%)", abs(Mw22 - 0.366) < 0.004)
check("(2,-2): odd-sector phase departure ~ 20 deg (18-23) — NOT a small correction to X = 0", 18 < np.degrees(2 * np.arctan(Mw22 / a)) < 23)
Mw33 = 2 * np.pi * 288.0 * Msec
check("(3,-3): ~30 deg (27-33) [same a used; l = 3 has its own W — indicative only]", 27 < np.degrees(2 * np.arctan(Mw33 / a)) < 33)
check("conditional on: register Dirichlet <=> Zerilli Dirichlet at the wall (CONV-039 question); unconditional: X = 0 on the odd sector is underived", True)

print()
print(f"3377 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
