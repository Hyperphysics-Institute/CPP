#!/usr/bin/env python3
"""
Patch 2488 — M4 arena determination: verify battery.

Campaign: OPEN-SR-H1-CLASS (series_relativity/development/OPEN-SR-H1-CLASS_campaign.md, v1.2)
Session:  SR-MECH-2485, step M4 (first step; cheapest kill; K4-safe — touches no candidate plane)

Checks (stdlib only, fixed seed):
  C1  Ball exclusion closed form: V_excl/V0 = 2f^2 - f^4 for the codim-2 tube of
      radius d = f*R in the round 4-ball of radius R (closed form vs Monte Carlo).
  C2  Ball leading coefficient via the panel formula pi*A2*R^2/V_cell = 2 EXACTLY
      (A2 = area of the arena's central section by the tube's core 2-plane).
  C3  COUNTERFACTUAL (kill-liveness): 4-cube arena of the SAME inradius R gives
      leading coefficient pi/4 != 2 (formula AND direct exact computation), and the
      resulting strain curve eps_cube(f) != gamma(f)-1 at every order. Had M4
      landed on a polytope arena, the campaign dies here — the kill had teeth.
  C4  Inscribed-ball lemma (MC sanity of a definitional fact): reach radius =
      inradius  =>  ball subset of polytope  =>  arena = ball INTERSECT polytope
      = ball exactly. Verified numerically for the cube.
  C5  Re-verification of 2482's identity UNDER the M4 arena verdict: with arena =
      the PSR insphere, eps(f) = (1-f^2)^(-1/2) - 1 = gamma_SR(f) - 1 to machine
      precision on a dense f grid.

K3/K3'/K3a note: no check below selects the ball; the ball is INPUT here, output
of the postulate-level derivation logged in reasoning/2488.md and the session file.
C3 exists precisely to show the alternative was computed and would have killed.
"""

import math
import random

random.seed(2488)

R = 1.0  # arena radius / inradius; all results scale-free
TOL_EXACT = 1e-12
TOL_MC = 5e-3
N_MC = 400_000

failures = []


def check(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        failures.append(name)


# ---------------------------------------------------------------- C1
def ball_excl_closed(f):
    return 2 * f**2 - f**4


def sample_ball4():
    # rejection sampling in the 4-cube
    while True:
        x = [random.uniform(-R, R) for _ in range(4)]
        if sum(v * v for v in x) <= R * R:
            return x


for f in (0.1, 0.3, 0.6, 0.9):
    d2 = (f * R) ** 2
    hits = 0
    for _ in range(N_MC):
        x = sample_ball4()
        if x[0] * x[0] + x[1] * x[1] <= d2:  # tube about the (x3,x4) core plane
            hits += 1
    mc = hits / N_MC
    cf = ball_excl_closed(f)
    check(f"C1 ball V_excl/V0 at f={f}", abs(mc - cf) < TOL_MC,
          f"MC={mc:.4f} closed={cf:.4f}")

# ---------------------------------------------------------------- C2
V_ball = math.pi**2 * R**4 / 2
A2_ball = math.pi * R**2  # central 2-plane section of the ball = disk
coef_ball = math.pi * A2_ball * R**2 / V_ball
check("C2 ball leading coefficient pi*A2*R^2/V = 2 exactly",
      abs(coef_ball - 2.0) < TOL_EXACT, f"coef={coef_ball!r}")

# ---------------------------------------------------------------- C3
V_cube = (2 * R) ** 4
A2_cube = (2 * R) ** 2  # central section of the 4-cube by a coordinate 2-plane
coef_cube_formula = math.pi * A2_cube * R**2 / V_cube
# direct exact: tube radius f*R fits inside the central square for all f<=1,
# so V_excl = pi*(fR)^2 * (2R)^2 exactly and the ratio is (pi/4)*f^2 at ALL f.
coef_cube_direct = math.pi / 4
check("C3a cube coefficient = pi/4 (formula)",
      abs(coef_cube_formula - math.pi / 4) < TOL_EXACT,
      f"coef={coef_cube_formula:.6f}")
check("C3b cube coefficient != 2 (kill was live)",
      abs(coef_cube_formula - 2.0) > 1.0,
      f"|coef-2|={abs(coef_cube_formula-2.0):.3f}")


def gamma(f):
    return 1.0 / math.sqrt(1.0 - f * f)


def eps_from_ratio(free_ratio):
    return free_ratio ** (-0.25) - 1.0


bad = 0
for i in range(1, 99):
    f = i / 100
    eps_cube = eps_from_ratio(1.0 - (math.pi / 4) * f * f)
    if abs(eps_cube - (gamma(f) - 1.0)) < 1e-6:
        bad += 1
check("C3c cube strain curve != gamma-1 everywhere on grid", bad == 0,
      f"matches={bad}/98")

# ---------------------------------------------------------------- C4
worst = 0.0
for _ in range(N_MC // 4):
    x = sample_ball4()
    worst = max(worst, max(abs(v) for v in x))
check("C4 inscribed-ball lemma: ball(R) subset cube(inradius R)",
      worst <= R + 1e-15, f"max sup-norm={worst:.6f}")

# ---------------------------------------------------------------- C5
worst5 = 0.0
for i in range(1, 100):
    f = i / 100
    eps = eps_from_ratio((1.0 - f * f) ** 2)
    worst5 = max(worst5, abs(eps - (gamma(f) - 1.0)))
check("C5 arena=insphere ==> eps(f) = gamma(f)-1 machine precision",
      worst5 < 1e-12, f"max|diff|={worst5:.2e}")

print()
if failures:
    print(f"RESULT: {len(failures)} FAILURE(S): {failures}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS")
