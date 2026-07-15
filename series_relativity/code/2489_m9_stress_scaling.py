#!/usr/bin/env python3
"""
Patch 2489 — M9 stress-scaling: verify battery.

Campaign: OPEN-SR-H1-CLASS v1.2, session SR-MECH-2485, step 2 (M9).
Companion to code/2486_stressed_arena_fork.py (which pinned the fork's two
branches without resolving them). This script verifies the RESOLUTION derived
forward in development/SR-MECH-2485_mechanism_session.md §Step 2:

  The exclusion radius is the kinematic per-Moment drift d = v_abs*t_P
  (Branch L's formula in ABSOLUTE velocity). c07's pre-target channel
  structure (g_tt sourced by |SSV|_abs magnitude; g_ij sourced by the
  GRADIENT tensor, hence identity under UNIFORM background stress) gives
  v_loc = v_abs*g_bg, under which the same d is IDENTICALLY Branch P's
  formula in LOCAL velocity: d = (v_loc/c)*PSR_eff. The fork's branches are
  one rule in two velocity variables; they are exclusive only if "v" is
  assumed to denote the same variable in both.

Checks (stdlib only):
  V1  Branch-formula identity: (v_abs/c)*l_P == (v_loc/c)*PSR_eff exactly,
      for all g_bg, given v_loc = v_abs*g_bg and PSR_eff = l_P/g_bg.
  V2  f = v_loc/c  ==>  eps = gamma(v_loc) - 1 to machine precision at every
      background stress (the identity survives for stressed aggregates).
  V3  Composition exactly multiplicative: l_P/r_total = g_bg * gamma(v_loc).
  V4  Ceiling consistency: f -> 1 at v_abs = c/g_bg, at which point
      v_loc = c exactly — coordinate ceiling reduced (Shapiro-consistent),
      locally measured ceiling = c.
  V5  KILL COUNTERFACTUAL (liveness): had c07's spatial channel been sourced
      by the |SSV|_abs MAGNITUDE (rods contracting by g_bg under uniform
      stress), then v_loc = v_abs*g_bg^2, f = (v_loc/c)/g_bg, and
      eps != gamma(v_loc) - 1 for every g_bg > 1 — M9 would have killed.
      The derivation's outcome is decided by c07's pre-target structure,
      not by anything selected in this session.

K3/K3'/K3a note: v_loc = v_abs*g_bg is INPUT here, output of the c07 channel
reading logged in reasoning/2489.md; no check below selects it.
"""

import math

l_P = 1.0
c = 1.0
TOL = 1e-12
failures = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        failures.append(name)


def gamma(x):
    return 1.0 / math.sqrt(1.0 - x * x)


G_BG = (1.0, 1.001, 1.1, 2.0, 10.0)
V_ABS_FRACS = (0.05, 0.3, 0.7, 0.99)  # as fractions of the coordinate ceiling c/g_bg

# ---------------------------------------------------------------- V1
worst = 0.0
for g in G_BG:
    psr = l_P / g
    for s in V_ABS_FRACS:
        v_abs = s * (c / g)
        v_loc = v_abs * g
        d_absform = (v_abs / c) * l_P
        d_locform = (v_loc / c) * psr
        worst = max(worst, abs(d_absform - d_locform))
check("V1 branch formulas identical under v_loc = g_bg*v_abs",
      worst < TOL, f"max|diff|={worst:.2e}")

# ---------------------------------------------------------------- V2
worst = 0.0
for g in G_BG:
    psr = l_P / g
    for s in V_ABS_FRACS:
        v_abs = s * (c / g)
        v_loc = v_abs * g
        d = v_abs * l_P / c            # kinematic drift per Moment (t_P = l_P/c)
        f = d / psr                    # exclusion fraction in the M4 arena
        eps = (1.0 - f * f) ** -0.5 - 1.0
        worst = max(worst, abs(eps - (gamma(v_loc / c) - 1.0)))
check("V2 eps = gamma(v_loc)-1 at every background stress",
      worst < TOL, f"max|diff|={worst:.2e}")

# ---------------------------------------------------------------- V3
worst = 0.0
for g in G_BG:
    for s in V_ABS_FRACS:
        v_abs = s * (c / g)
        v_loc = v_abs * g
        f = v_loc / c
        r_total = (l_P / g) / gamma(f)   # stressed arena further reduced by velocity strain
        worst = max(worst, abs(l_P / r_total - g * gamma(f)))
check("V3 composition exactly multiplicative g_bg*gamma(v_loc)",
      worst < TOL, f"max|diff|={worst:.2e}")

# ---------------------------------------------------------------- V4
worst = 0.0
for g in G_BG:
    v_abs_ceiling = c / g
    v_loc_at_ceiling = v_abs_ceiling * g
    d = v_abs_ceiling * l_P / c
    f = d / (l_P / g)
    worst = max(worst, abs(f - 1.0), abs(v_loc_at_ceiling - c))
check("V4 coordinate ceiling c/g_bg is exactly v_loc = c (f = 1)",
      worst < TOL, f"max|diff|={worst:.2e}")

# ---------------------------------------------------------------- V5
alive = True
for g in G_BG:
    if g == 1.0:
        continue
    for s in V_ABS_FRACS:
        v_abs = s * (c / g)
        v_loc_cf = v_abs * g * g       # counterfactual: rods also contract by g_bg
        if v_loc_cf >= c:
            continue
        d = v_abs * l_P / c
        f = d / (l_P / g)              # = (v_loc_cf/c)/g_bg
        eps = (1.0 - f * f) ** -0.5 - 1.0
        if abs(eps - (gamma(v_loc_cf / c) - 1.0)) < 1e-9:
            alive = False
check("V5 counterfactual (magnitude-sourced g_ij) breaks the identity — kill was live",
      alive)

print()
if failures:
    print(f"RESULT: {len(failures)} FAILURE(S): {failures}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS")
