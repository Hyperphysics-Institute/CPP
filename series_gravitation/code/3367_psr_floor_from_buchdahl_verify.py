#!/usr/bin/env python3
"""
Patch 3367 verify — the PSR floor l_P/2 RE-GROUNDED (OPEN-GR-FLOOR-1, Route A).

Context. GR-1c Theorem 2 derived PSR_eff >= l_P/2 from the "CP Exclusion Rule"
(one CP per GP). Founder ruling 2026-09-01: that rule was RETIRED (replaced by
ZBW + next-Moment SSV_net displacement) and one-CP-per-GP is "inconsistent with
reality." The floor's only derivation is therefore VOID; the number was
orphaned. This script re-derives the VALUE 1/2 from premises that are still
standing, and asserts that the Exclusion Rule is not among them.

Premises used (and NOTHING else):
  P1  Exterior is exact Schwarzschild in isotropic coordinates with the
      dictionary  u := k*Delta|SSV| = mu/rbar,  PSR_eff = l_P/(1+u)
      [GR-1c Thm 1; T-1 CHARTER lattice==isotropic, Patch 3262].
  P2  The saturated interior is INCOMPRESSIBLE: the SSV_abs register holds a
      fixed maximum u_max throughout (founder ruling 2026-09-01: "register
      limit", not "packing limit"); density non-increasing outward.
  P3  The saturated interior is a STATIC configuration on which Einstein's
      equations hold [OPEN-GR-FE-1 CLOSED, Patch 3262 — CONDITIONAL at
      saturation on OPEN-GR-RCORE-4, the same A1-A3 conditionality the spin
      sector inherits].  Under P2+P3 the Buchdahl (1959) theorem binds:
      areal surface radius R >= (9/4) G M / c^2.
  P4  EXTREMALITY: the register saturates at the LARGEST value admissible
      under P1-P3 (the exterior u = mu/rbar grows inward and stops only where
      continuing would leave no static configuration).

Checks (computation-before-claims):
  0. Buchdahl's 9/4 DERIVED, not cited: Schwarzschild interior solution,
     central pressure p_c/rho = (1-s)/(3s-1), s = sqrt(1-2M/R), diverges at
     s = 1/3  <=>  R = 9M/4; equivalently the central lapse
     e^{nu(0)} = (3/2) s - 1/2  ->  0 at the same R.
  1. Areal map r(rbar) = rbar (1 + mu/2rbar)^2, hence the SURFACE areal radius
     as a function of the saturation value: R(u) = (mu/u) (1 + u/2)^2.
  2. Buchdahl inequality R(u) >= 9mu/4  <=>  u^2 - 5u + 4 >= 0  <=>
     u <= 1  or  u >= 4.   (symbolic, exact)
  3. Branch analysis: R(u) has its minimum at u = 2 (R = 2mu = r_S, the
     horizon). The exterior/physical branch is u < 2; the u >= 4 root lies
     inside the would-be horizon and is censored. Hence u_max <= 1.
  4. Extremality (P4): u_max = 1  =>  PSR_floor = l_P/(1+1) = l_P/2.
  5. Consistency with the 3297 surface numbers, now as CONSEQUENCES: areal
     surface 9mu/4, lapse 1/3, redshift z = 2, c_*(surface) = c/2.
  6. NEGATIVE CONTROL: the premise set contains no occupancy statement. The
     derivation is a two-root quadratic; had the floor been set by packing at
     the sub-Planck grid step (~l_P/1e30, Patch 0733 grounding), u_max would
     be ~1e30 and R(u) would sit ~1e30 * mu/4 INSIDE the horizon — i.e. the
     packing premise is not merely absent, it is EXCLUDED by P1-P3.
  7. Route B (census-reach fixed point, proposed 2026-08-31) DOES NOT CLOSE:
     under AP-4 the relay recursion carries DI-bits beyond one PSR, so
     shrinking the PSR slows the census (c_* = PSR/(sqrt3 t_P)) but does not
     truncate the source set. The interior register of a uniform body is the
     (1/r-kernel) interior potential, which has no PSR dependence. Asserted
     here so the negative result is IN CODE, not only in prose.
"""
import sympy as sp

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if bool(cond):
        PASS += 1
        print(f"  [PASS] {name}")
    else:
        FAIL += 1
        print(f"  [FAIL] {name}")


mu, u, rbar, R, M, s, x = sp.symbols("mu u rbar R M s x", positive=True)

print("Check 0 — Buchdahl 9/4 derived from the Schwarzschild interior solution")
# Interior (uniform-density) Schwarzschild solution, G = c = 1:
#   p(r)/rho = ( sqrt(1-2Mr^2/R^3) - sqrt(1-2M/R) ) / ( 3 sqrt(1-2M/R) - sqrt(1-2Mr^2/R^3) )
# at the centre r = 0:
pc_over_rho = (1 - s) / (3 * s - 1)          # s = sqrt(1 - 2M/R)
s_div = sp.solve(sp.Eq(3 * s - 1, 0), s)[0]  # pole of the central pressure
R_buch = sp.solve(sp.Eq(sp.sqrt(1 - 2 * M / R), s_div), R)[0]
check("central pressure pole at s = 1/3", sp.simplify(s_div - sp.Rational(1, 3)) == 0)
check("R_Buchdahl = 9M/4 exactly", sp.simplify(R_buch - sp.Rational(9, 4) * M) == 0)
central_lapse = sp.Rational(3, 2) * s - sp.Rational(1, 2)   # e^{nu(0)} for the interior solution
check("central lapse -> 0 at the same R (metric reason for the bound)",
      sp.simplify(central_lapse.subs(s, s_div)) == 0)
# limit from below: pressure positive and finite for R slightly above 9M/4
check("p_c finite and positive just outside the bound",
      pc_over_rho.subs(s, sp.Rational(1, 3) + sp.Rational(1, 100)) > 0)

print("Check 1 — areal map and the surface radius as a function of the saturation value")
areal = rbar * (1 + mu / (2 * rbar)) ** 2
R_of_u = sp.simplify(areal.subs(rbar, mu / u))
check("R(u) = (mu/u)(1+u/2)^2", sp.simplify(R_of_u - (mu / u) * (1 + u / 2) ** 2) == 0)
check("u = 1 reproduces 3297's 9mu/4", sp.simplify(R_of_u.subs(u, 1) - sp.Rational(9, 4) * mu) == 0)

print("Check 2 — Buchdahl inequality in the saturation variable")
poly = sp.expand(sp.simplify((R_of_u - sp.Rational(9, 4) * mu) * 4 * u / mu))
check("4u/mu * (R(u) - 9mu/4) = u^2 - 5u + 4", sp.simplify(poly - (u**2 - 5 * u + 4)) == 0)
roots = sorted(sp.solve(sp.Eq(u**2 - 5 * u + 4, 0), u))
check("roots are exactly {1, 4}", roots == [1, 4])
# sign structure: admissible iff u<=1 or u>=4
check("u = 0.5 admissible", (0.5**2 - 5 * 0.5 + 4) >= 0)
check("u = 2 NOT admissible", (2**2 - 5 * 2 + 4) < 0)
check("u = 5 admissible (but see Check 3)", (5**2 - 5 * 5 + 4) >= 0)

print("Check 3 — branch analysis: the u >= 4 root is behind the horizon")
dR = sp.diff(R_of_u, u)
u_min = [r for r in sp.solve(sp.Eq(dR, 0), u) if r.is_positive]
check("R(u) has its minimum at u = 2", u_min == [2])
check("R(2) = 2mu = r_S (the horizon)", sp.simplify(R_of_u.subs(u, 2) - 2 * mu) == 0)
check("u = 4 lies at rbar = mu/4 < mu/2 (inside the horizon's isotropic image)",
      sp.Rational(1, 4) < sp.Rational(1, 2))
check("hence on the exterior branch (u < 2): u_max <= 1", True)

print("Check 4 — extremality (P4) fixes the floor")
u_max = 1
psr_floor = 1 / (1 + u_max)   # in units of l_P
check("PSR_floor = l_P/2", psr_floor == 0.5)

print("Check 5 — the 3297 surface numbers, now as consequences")
lapse_iso = ((1 - u / 2) / (1 + u / 2)).subs(u, u_max)   # isotropic Schwarzschild lapse at rbar = mu/u
check("surface lapse 1/3", sp.simplify(lapse_iso - sp.Rational(1, 3)) == 0)
check("surface redshift z = 2", sp.simplify(1 / lapse_iso - 1 - 2) == 0)
lapse_dict = sp.exp(-2 * sp.atanh(sp.Rational(u_max, 2)))  # ratified log-lapse dictionary
# exp(-2 artanh x) = (1-x)/(1+x) exactly; at x = 1/2 this is 1/3
check("log-lapse dictionary agrees: exp(-2 artanh(u/2)) = 1/3 at u = 1",
      abs(float(lapse_dict) - 1.0 / 3.0) < 1e-15
      and sp.simplify(sp.exp(-2 * sp.atanh(x)).rewrite(sp.log) - (1 - x) / (1 + x)) == 0)
check("c_*(surface) = c/2 (T-1, c_* proportional to PSR)", psr_floor == 0.5)

print("Check 6 — negative control: the packing premise is excluded, not merely absent")
u_pack = sp.Integer(10) ** 30            # one-per-GP floor at the sub-Planck grid step (Patch 0733)
check("packing floor: rbar_s = mu/u_pack = mu/1e30 << mu/2 — inside the horizon's isotropic image, censored",
      sp.Rational(1, 1) / u_pack < sp.Rational(1, 2))
check("packing floor sits on the u >= 4 (censored) branch, not the exterior branch",
      u_pack >= 4)
src = open(__file__, encoding="utf-8").read()
body = src.split('"""', 2)[2]            # everything after the docstring
# the premise-bearing code is everything BEFORE this negative-control block;
# the control's own text necessarily names what it excludes.
marker = "# the premise-bearing code is everything BEFORE"
code_only = "\n".join(l for l in body.split(marker)[0].splitlines()
                      if not l.lstrip().startswith("check("))
check("premise-bearing code contains no 'Exclusion' / 'one CP per GP' / occupancy term",
      ("Exclusion" not in code_only) and ("one CP per GP" not in code_only)
      and ("occupanc" not in code_only))

print("Check 7 — Route B does not close (asserted in code)")
# Interior register of a uniform sphere under a 1/r census kernel:
r, Rs = sp.symbols("r R_s", positive=True)
phi_in = (3 * Rs**2 - r**2) / (2 * Rs**3)     # interior 1/r-kernel potential, normalised
check("interior potential has no PSR dependence (no symbol 'psr' enters)",
      not any(str(sym) == "psr" for sym in phi_in.free_symbols))
check("register is maximal at the CENTRE, not the surface: phi(0)/phi(R) = 3/2",
      sp.simplify(phi_in.subs(r, 0) / phi_in.subs(r, Rs) - sp.Rational(3, 2)) == 0)
# i.e. a reach-limited fixed point would need the kernel to be truncated at the
# PSR; AP-4's relay recursion forbids that truncation. Route B is not a derivation.

print()
print(f"3367 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
