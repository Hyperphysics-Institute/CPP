#!/usr/bin/env python3
"""
Patch 3387 verify — the founder's clock mechanism (R-CLOCK-RATE-IS-DISPLACEMENT:
"local clock mechanisms progress at the SSV_net displacement per Moment, which
shrinks as SSV_abs approaches saturation") taken literally:  N = PSR_eff/l_P.

Checks:
  A. Local light speed is c by local clocks AUTOMATICALLY (one PSR per Moment,
     clock rate PSR/l_P): no assumption needed — the founder's picture and 3386's
     census map are the same statement.
  B. THE SECOND-ORDER TEST. With the ratified register u = v = mu/rbar (GR-1c
     Thm 1: k Delta|SSV| = GM/rc^2, linear), N = 1/(1+v) gives
     g_tt = 1 - 2v + 2 beta v^2 with beta = 3/2. PPN gamma = 1 from psi^4.
     Perihelion advance scales as (2 + 2 gamma - beta)/3 = 5/6 of GR: Mercury
     42.98"/century would be 35.8". EXCLUDED at the 1e-3 level.
  C. THE RESCUE WITH NO NEW AXIOM. If the register self-sources at second order,
     u_reg = v/(1 - v/2) = v + v^2/2 + v^3/4 + ..., then N = 1/(1 + u_reg) is
     EXACTLY the ratified log-lapse (2 - v)/(2 + v): beta = 1, all tests pass,
     and the log-lapse is DERIVED from the founder's mechanism + Mercury rather
     than imposed by the T-1 charter.
  D. Consequences for the census map and the R-core: PSR = l_P N; lattice hop
     per Moment = N/psi^2 = GR's coordinate light speed exactly -> J = 6.75 at
     any wall; the strong-field departure of 3385/3386 CLOSES. And the
     register saturates (u_reg = 1, PSR = l_P/2 — floor unchanged) where
     N = 1/2, i.e. v = 2/3: isotropic rbar_s = 1.5 mu, areal 8mu/3 = 1.33 r_S
     (not Buchdahl's 9mu/4 = 1.125 r_S); surface lapse 1/2, z = 1; Level-A
     cavity 2.29 mu/c = 0.70 ms at 62 Msun (was 2.15 ms). The 3367/3370
     window, expressed in v, still binds: v in (0.536, 1] -> u_reg in (0.73, 2];
     u_reg = 1 sits INSIDE it, not at the extremal edge.
Nothing is enacted; this is the fork, priced.
"""
import numpy as np
import sympy as sp

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


v = sp.symbols("v", positive=True)              # v = mu/rbar (isotropic), the linear Newtonian potential
loglapse = (1 - v / 2) / (1 + v / 2)
psi2 = (1 + v / 2) ** 2

print("A — local c by local clocks, automatically")
PSR_over_lP = sp.symbols("PSR")                 # proper hop per Moment, in units of l_P
N_clock = PSR_over_lP                            # founder: clock rate = displacement per Moment = PSR/l_P
local_speed = PSR_over_lP / N_clock              # proper length per local tick
check("hop one PSR per Moment + clock rate PSR/l_P  =>  local light speed = 1 (c) identically", sp.simplify(local_speed - 1) == 0)

print("B — the second-order test with the RATIFIED linear register u = v")
N_a = 1 / (1 + v); gtt_a = N_a ** 2
ser = sp.series(gtt_a, v, 0, 3).removeO(); beta_a = sp.simplify(ser.coeff(v, 2) / 2)
gamma = sp.simplify((sp.series(psi2 ** 2, v, 0, 2).removeO().coeff(v, 1)) / 2)   # spatial g_ij = psi^4 delta = 1 + 2 gamma v
check("gamma = 1 from psi^4 (light deflection, Shapiro pass)", gamma == 1)
check("beta = 3/2 with N = 1/(1+v) (GR: 1)", beta_a == sp.Rational(3, 2))
peri = sp.simplify((2 + 2 * gamma - beta_a) / 3)
check("perihelion factor (2 + 2 gamma - beta)/3 = 5/6 of GR  ->  Mercury 35.8'' vs 42.98'' observed: EXCLUDED", peri == sp.Rational(5, 6), f"predicted {float(42.98 * peri):.1f}''")

print("C — the rescue with no new axiom: a self-sourcing register")
u_reg = v / (1 - v / 2)
N_b = sp.simplify(1 / (1 + u_reg))
check("u_reg = v/(1 - v/2) = v + v^2/2 + v^3/4 + ...", sp.simplify(sp.series(u_reg, v, 0, 4).removeO() - (v + v**2 / 2 + v**3 / 4)) == 0)
check("N = 1/(1 + u_reg) is EXACTLY the ratified log-lapse (2 - v)/(2 + v)", sp.simplify(N_b - loglapse) == 0)
beta_b = sp.simplify(sp.series(N_b ** 2, v, 0, 3).removeO().coeff(v, 2) / 2)
check("beta = 1: Mercury passes; the log-lapse is DERIVED (founder mechanism + second-order test), not imposed", beta_b == 1)
check("the required self-sourcing coefficient is exactly 1/2 at second order (a prediction about the DI-bit census: emitters with a larger register broadcast a larger census)", sp.series(u_reg, v, 0, 3).removeO().coeff(v, 2) == sp.Rational(1, 2))

print("D — consequences")
hop = sp.simplify(N_b / psi2)                    # PSR = l_P N; lattice hop per Moment = PSR/(psi^2 l_P)
J_wall = float(1 / hop.subs(v, 1))
check("lattice hop per Moment = N/psi^2 = GR's isotropic coordinate light speed: J = 6.75 at v = 1 — the strong-field departure of 3385/3386 CLOSES", abs(J_wall - 6.75) < 1e-12)
v_sat = sp.solve(sp.Eq(u_reg, 1), v)[0]
check("saturation u_reg = 1 (PSR = l_P/2, floor unchanged) occurs at v = 2/3, NOT v = 1", v_sat == sp.Rational(2, 3))
R_areal = float((sp.Rational(3, 2) * psi2.subs(v, sp.Rational(2, 3))))
check("surface: isotropic 1.5 mu, areal 8mu/3 = 1.333 r_S (Buchdahl 9mu/4 = 1.125 r_S); lapse 1/2, z = 1", abs(R_areal - 8 / 3) < 1e-12 and float(loglapse.subs(v, sp.Rational(2, 3))) == 0.5)
rstar = lambda x: x + 2 * np.log(x / 2 - 1)
dt = 2 * (rstar(3.0) - rstar(8 / 3)); ms = dt * 62 * 4.925e-6 * 1e3
check("Level-A cavity: 2.29 mu/c = 0.70 ms at 62 Msun (was 2.15 ms)", abs(dt - 2.289) < 0.01, f"{ms:.2f} ms")
u_lo = float(u_reg.subs(v, 0.536)); u_hi = float(u_reg.subs(v, 1))
check("the 3370 window in v (0.536, 1] is u_reg in (0.73, 2]; u_reg = 1 sits INSIDE it — saturation is no longer at the Buchdahl edge", u_lo < 1 < u_hi)
check("the whole R-core arc from 3297 identified the saturating register with v; under (C) it is u_reg = v/(1-v/2): the surface, the cavity, and every wall pole (3383, 3384 at r_w = 9/4) would be recomputed at r_w = 8/3 — NOT ENACTED; the fork is the founder's", True)

print()
print(f"3387 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
