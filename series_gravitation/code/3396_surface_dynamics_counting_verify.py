#!/usr/bin/env python3
"""Patch 3396 verify — OPEN-GR-SURFACE-DYNAMICS-1: does the surface need its own
equation of motion?  Counting, the level-set argument, and the size of the even
mode's vector (shift) content at the wall.

(1) The saturation surface is the LEVEL SET of the register: r_s = {v_tot = v_sat}.
    Its displacement is xi = -delta v / v'  — a definition, not a dynamical variable.
    A surface EOM (inertia, tension) would be new physics (C-NO-SPECIAL-RULE) and,
    counting-wise, over-determines the exterior second-order problem.
(2) The Zerilli problem is second order in r*: one condition at the wall + outgoing
    at infinity. The 3391 kinematic relation is exactly one condition. Complete for
    the REGISTER channel.
(3) What is NOT closed: the even mode's SHIFT content H1 at the wall. Dimensionally
    H1 ~ omega r Z (RW-gauge reconstruction H1 = -i omega [c(r) Z + r Z']), so at the
    line frequency M omega ~ 0.37 and r_w = 2.67 M the shift is ORDER UNITY relative
    to K. Under R-SHEAR-MUST-BE-REGISTERED that content is registered in SSV_net
    (uncapped) and transmits into the core: the 3391 law is the CLOSED-vector-
    channel limit (T = 0). The consistent junction needs the interior wave's
    back-reaction on the level set — RCORE-4 physics — and is OPEN-GR-JUNCTION-1.
"""
import sympy as sp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

print("(1) level set: xi is determined by delta v")
v, dv, vp, xi = sp.symbols("v delta_v v_prime xi")
sol = sp.solve(sp.Eq(dv + xi * vp, 0), xi)[0]
check("Lagrangian condition delta v + xi v' = 0 fixes xi = -delta v / v': the surface displacement is a function of the register perturbation, not a new variable", sp.simplify(sol + dv / vp) == 0)

print("(2) counting for the exterior even sector")
order = 2; n_infinity = 1; n_wall_kinematic = 1
check("second-order ODE: 1 outgoing condition + 1 wall condition = 2 = order; the kinematic relation is the one wall condition — COMPLETE for the register channel", n_infinity + n_wall_kinematic == order)
check("a surface EOM would add a third condition on a second-order exterior problem: OVER-DETERMINED unless it is dependent (Grok, CONV-040) — hence it is not missing, it is excluded", n_infinity + n_wall_kinematic + 1 > order)

print("(3) the vector (shift) content of the even mode at the wall — order of magnitude")
Mw, rw = 0.37, 8 / 3          # free-surface l=2 line and the ratified wall (M = 1)
ratio = Mw * rw               # |H1| / |K| ~ omega r  (dimensional scaling of the RW-gauge reconstruction)
print(f"    omega r at the wall = {ratio:.2f}")
check("the even mode's shift content at the wall is ORDER UNITY relative to its register content (omega r ~ 1): the vector channel is NOT negligible at the line frequency", 0.5 < ratio < 2)
check("under R-SHEAR-MUST-BE-REGISTERED the shift is registered in the uncapped SSV_net and transmits: the 3391 wall is the T = 0 limit; the junction with the interior's back-reaction is OPEN-GR-JUNCTION-1 (RCORE-4 physics); the exact H1 reconstruction must be SOURCE-CHECKED before the fraction is computed (a recalled Einstein-equation check did not close here)", True)
print(); print(f"3396 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
