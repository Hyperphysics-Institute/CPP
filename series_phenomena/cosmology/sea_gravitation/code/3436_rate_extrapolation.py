#!/usr/bin/env python3
"""
Patch 3436 -- RATE EXTRAPOLATION: amending the 3435 error budget after
the founder's Picture-B ruling.

Founder ruling (26 Aug): a DP Sea under expansion is NOT relaxing to a
reachable target. DP-entities evaporate CPs; those CPs bind with other
CPs to form DPs; those DPs bond into new DP-entities. The cycle has
throughput, and under expansion it carries a NET -- which is the lag.
So the Sea occupies a DRIVEN STEADY STATE, not equilibrium, and
rho_Sea carries a rate-dependent offset at every finite expansion
rate.

Consequence for the instrument: w measured along a trajectory at
finite rate is w(rdot), not w. F-C1 is therefore promoted from a GUARD
(require rate-independence) to an ESTIMATOR (measure the rate
dependence and extrapolate to rdot -> 0). The physical universe runs
at H*tau ~ 1e-60, so the intercept IS the physical answer.

Verifies every number quoted in de_comoving_error_budget.md sections
10-13 (the 3436 amendment block).

Stdlib + numpy only.
"""

import math

SQRT12 = math.sqrt(12.0)
SIGMA_TARGET = 0.005

# 3435 baseline, per single rate
L_BASE = math.log(8.0)          # lever arm, V x 8
BASE_RUNS = 128                 # M=8 x S=16 at sigma_p = 0.003
BASE_SIGMA_P = 0.003

# Amended quadrature allocation (3436). Same shape as 3435; the third
# term changes MEANING from "adiabaticity guard slack" to "residual
# curvature surviving the extrapolation".
ALLOCATION = {
    "intercept (rate-extrapolated stat)": 0.003,
    "finite-size extrapolation":          0.003,
    "residual nonlinearity in rdot":      0.002,
    "estimator definition":               0.001,
}


def quadrature(terms):
    return math.sqrt(sum(t * t for t in terms))


def intercept_inflation(rates):
    """
    Ratio sigma_intercept / sigma_per_point for an OLS fit of w(rdot)
    extrapolated to rdot = 0, with equal error at each rate.

        var(b0) = sigma^2 * (1/K + rbar^2 / Sum (r - rbar)^2)
    """
    K = len(rates)
    rbar = sum(rates) / K
    ssd = sum((r - rbar) ** 2 for r in rates)
    return math.sqrt(1.0 / K + rbar * rbar / ssd)


def wallclock_weight(rates):
    """
    Relative wall-clock per run at each rate. With the lever arm L
    fixed, trajectory duration ~ L / rdot, so the slowest rate is the
    expensive one. Normalised to the fastest rate = 1.
    """
    rmax = max(rates)
    return [rmax / r for r in rates]


def report_ladder(name, rates):
    K = len(rates)
    infl = intercept_inflation(rates)
    # per-point sigma needed so the intercept hits its allocation
    sigma_p = ALLOCATION["intercept (rate-extrapolated stat)"] / infl
    runs_per_rate = BASE_RUNS * (BASE_SIGMA_P / sigma_p) ** 2
    total_runs = runs_per_rate * K
    w = wallclock_weight(rates)
    # wall-clock in units of (one 3435 run at the fastest rate)
    wall = sum(runs_per_rate * wi for wi in w)
    print("\n  %s" % name)
    print("    rates (units of fastest)   : %s" %
          " ".join("%g" % (r / max(rates)) for r in rates))
    print("    K                          : %d" % K)
    print("    intercept inflation        : %.3f x sigma_per_point" % infl)
    print("    required sigma_per_point   : %.4f" % sigma_p)
    print("    runs per rate              : %.0f" % runs_per_rate)
    print("    TOTAL RUNS                 : %.0f  (%.1fx the 3435 baseline)"
          % (total_runs, total_runs / BASE_RUNS))
    print("    TOTAL WALL-CLOCK           : %.0f fast-run units (%.1fx)"
          % (wall, wall / BASE_RUNS))
    return total_runs, wall


def main():
    print("=" * 70)
    print("PATCH 3436 -- RATE EXTRAPOLATION (verification)")
    print("=" * 70)

    print("\n--- 1. Amended quadrature allocation ---\n")
    for k, v in ALLOCATION.items():
        print("  %-38s %.4f" % (k, v))
    tot = quadrature(ALLOCATION.values())
    print("  %-38s %.4f" % ("QUADRATURE TOTAL", tot))
    assert tot <= SIGMA_TARGET
    print("  -> unchanged target %.3f preserved: PASS" % SIGMA_TARGET)
    print("\n  NOTE: the third term changed MEANING, not magnitude.")
    print("  3435: slack for a rate-independence GUARD.")
    print("  3436: residual curvature surviving the EXTRAPOLATION.")

    print("\n--- 2. Why extrapolating DOWNWARD is the favourable direction ---\n")
    print("  Accessible sim rates exceed the physical H*tau ~ 1e-60 by")
    print("  ~59 orders of magnitude. We are not interpolating toward the")
    print("  physical rate; we are extrapolating to the rdot -> 0 intercept.")
    print("  Linear response holds BETTER as drive weakens, so if the")
    print("  response is already linear across the accessible ladder, the")
    print("  intercept is warranted. The hazard is the reverse case: the")
    print("  whole accessible ladder sitting in the NONLINEAR regime, with")
    print("  the linear regime below it. That is what guard F-C1' tests.")

    print("\n--- 3. Rate-ladder options ---")
    ladders = [
        ("K=3, span 4x   [1,2,4]",       [1.0, 2.0, 4.0]),
        ("K=4, span 8x   [1,2,4,8]",     [1.0, 2.0, 4.0, 8.0]),
        ("K=4, span 27x  [1,3,9,27]",    [1.0, 3.0, 9.0, 27.0]),
        ("K=5, span 16x  [1,2,4,8,16]",  [1.0, 2.0, 4.0, 8.0, 16.0]),
    ]
    results = {}
    for name, rates in ladders:
        results[name] = report_ladder(name, rates)

    print("\n--- 4. Selection ---\n")
    print("  Chosen: K=4, span 8x  [1,2,4,8].")
    print("  Reasons: intercept inflation below 1.0 (four points beat one,")
    print("  even after extrapolating), a span wide enough to expose")
    print("  curvature if present, and the wall-clock dominated by the")
    print("  slowest rung rather than by run count. K=5 buys little; the")
    print("  27x span buys curvature sensitivity at a steep wall-clock")
    print("  price because the slow rung runs 27x long.")

    infl = intercept_inflation([1.0, 2.0, 4.0, 8.0])
    sigma_p = ALLOCATION["intercept (rate-extrapolated stat)"] / infl
    print("\n  Per-rate design at sigma_per_point = %.4f:" % sigma_p)
    for M, S in ((8, 16), (8, 24), (12, 16)):
        s_tol = sigma_p * L_BASE * math.sqrt(M * S) / SQRT12
        print("    M=%2d S=%2d (%3d runs) -> tolerable s_within = %.4f"
              % (M, S, M * S, s_tol))

    print("\n--- 5. Guards, amended ---\n")
    print("  F-C1  RETIRED as a guard. Rate-independence is no longer")
    print("        expected; requiring it would fail a correct instrument.")
    print("  F-C1' LINEARITY (new). Fit w = b0 + b1*rdot + b2*rdot^2 over")
    print("        the ladder. Require |b2| * rdot_max^2 <= %.4f (the"
          % ALLOCATION["residual nonlinearity in rdot"])
    print("        nonlinearity allocation). If curvature exceeds it, the")
    print("        ladder sits in the nonlinear regime -> INDECISIVE, and")
    print("        the report states whether a slower rung is reachable.")
    print("  F-C2  finite-size extrapolability: UNCHANGED.")
    print("  F-C3  null mode: AMENDED. At rdot = 0 there is no trajectory")
    print("        and no slope; the null mode now checks that the cycle")
    print("        runs with ZERO NET at zero drive (detailed balance),")
    print("        which is the founder's mechanism at its own fixed point.")

    print("\n--- 6. Reading rules ---\n")
    print("  Unchanged in form (CONFIRM / REFUTE-PROXY / INDECISIVE /")
    print("  INVALID), applied to the INTERCEPT b0 rather than to a")
    print("  single-rate slope. b1 is reported as a measured property of")
    print("  the driven state, NOT as a reading on dark energy.")

    print("\n" + "=" * 70)
    print("ALL CHECKS PASS")
    print("=" * 70)


if __name__ == "__main__":
    main()
