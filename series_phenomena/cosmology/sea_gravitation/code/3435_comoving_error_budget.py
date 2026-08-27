#!/usr/bin/env python3
"""
Patch 3435 -- COMOVING BUILD, ERROR BUDGET (frozen before any sizing).

Verifies every number quoted in de_comoving_error_budget.md.

Estimator under test
--------------------
Under true (staged) expansion the equation-of-state parameter is read
DIRECTLY off the substrate rather than inferred from a fixed-box
temperature scan:

    rho ~ a^{-3(1+w)},  V ~ a^3   =>   1 + w = - d ln rho_Sea / d ln V

The instrument is a paired/trajectory design: each seed is carried
THROUGH the expansion, ln rho_Sea is recorded at M stage points spaced
uniformly in ln V over a lever arm L = ln(V_final/V_initial), and the
per-seed OLS slope is averaged over S seeds.

For uniformly spaced design points the OLS slope error is

    sigma_slope = sigma_within / (sqrt(M) * sd(lnV)),  sd(lnV) -> L/sqrt(12)

so, pooling S independent seeds,

    sigma_w = sqrt(12) * s_within / (L * sqrt(M*S))

s_within (the residual scatter of ln rho_Sea about the trajectory fit)
is the ONE input this budget cannot supply from the corpus. Measuring
it is the pilot's job. Everything else is frozen here.

Stdlib + numpy only. No scipy dependency (scipy 1.18.1 is present on
VideoCPU but nothing here needs it).
"""

import math

SQRT12 = math.sqrt(12.0)

# ---------------------------------------------------------------- targets
# Standing bound from Patch 3419 (entity-concentration route):
STANDING_BOUND = 0.0198          # |w+1| <= 0.0198  =>  w in [-1.020, -0.980]
# Live hypotheses the instrument must be able to adjudicate:
DESI_W0 = -0.90                  # DESI-preferred  => |w+1| = 0.100
FW1_W = -1.023                   # F-W-1 (demoted at 3422) => |w+1| = 0.023
# Frozen total-error target (justified in sigma_target_rationale()):
SIGMA_TARGET = 0.005

# Frozen quadrature allocation of the total budget:
ALLOCATION = {
    "statistical (seeds x stages)": 0.003,
    "finite-size extrapolation":    0.003,
    "expansion-rate / adiabaticity": 0.002,
    "estimator definition":         0.001,
}


def quadrature(terms):
    return math.sqrt(sum(t * t for t in terms))


def sigma_w(s_within, L, M, S):
    """Statistical error on w for the paired trajectory design."""
    return SQRT12 * s_within / (L * math.sqrt(M * S))


def required_s_within(sigma_stat, L, M, S):
    """Largest per-point ln(rho) scatter compatible with sigma_stat."""
    return sigma_stat * L * math.sqrt(M * S) / SQRT12


def required_MS(s_within, L, sigma_stat):
    """Total runs M*S needed to reach sigma_stat at a measured s_within."""
    return (SQRT12 * s_within / (L * sigma_stat)) ** 2


def sigma_target_rationale():
    out = []
    out.append("Discrimination power at sigma_total = %.3f:" % SIGMA_TARGET)
    for name, w in (("DESI-preferred w0=-0.90", DESI_W0),
                    ("F-W-1 w=-1.023", FW1_W)):
        n_sigma = abs(w + 1.0) / SIGMA_TARGET
        out.append("  %-26s |w+1| = %.3f  ->  %5.1f sigma" %
                   (name, abs(w + 1.0), n_sigma))
    out.append("  %-26s |w+1| = %.4f ->  %5.1f sigma  (tightening factor)" %
               ("standing 3419 bound", STANDING_BOUND,
                STANDING_BOUND / SIGMA_TARGET))
    return "\n".join(out)


def main():
    print("=" * 70)
    print("PATCH 3435 -- COMOVING BUILD ERROR BUDGET (verification)")
    print("=" * 70)

    print("\n--- 1. Why sigma_total = %.3f is the frozen target ---\n"
          % SIGMA_TARGET)
    print(sigma_target_rationale())

    print("\n--- 2. Frozen quadrature allocation ---\n")
    for name, val in ALLOCATION.items():
        print("  %-32s %.4f" % (name, val))
    total = quadrature(ALLOCATION.values())
    print("  %-32s %.4f" % ("QUADRATURE TOTAL", total))
    assert total <= SIGMA_TARGET, "allocation exceeds the frozen target"
    print("  -> within target %.3f: PASS" % SIGMA_TARGET)

    sigma_stat = ALLOCATION["statistical (seeds x stages)"]

    print("\n--- 3. Design surface: largest tolerable s_within ---")
    print("    (per-stage-point residual scatter in ln rho_Sea, for")
    print("     sigma_stat = %.3f; L = ln volume lever arm)\n" % sigma_stat)
    header = "  %-22s" % "lever arm L" + "".join(
        "%10s" % ("M=%d,S=%d" % (M, S)) for M, S in
        ((6, 8), (8, 16), (12, 24), (12, 48)))
    print(header)
    for label, L in (("V x 4   (a x 1.59)", math.log(4.0)),
                     ("V x 8   (a x 2)", math.log(8.0)),
                     ("V x 27  (a x 3)", math.log(27.0)),
                     ("V x 64  (a x 4)", math.log(64.0))):
        row = "  %-22s" % label
        for M, S in ((6, 8), (8, 16), (12, 24), (12, 48)):
            row += "%10.4f" % required_s_within(sigma_stat, L, M, S)
        print(row)

    print("\n--- 4. Inverse: total runs M*S needed at a measured s_within ---")
    print("    (baseline lever arm L = ln 8; pilot supplies s_within)\n")
    L8 = math.log(8.0)
    print("  %-16s%12s%12s" % ("s_within", "M*S needed", "runs/core*"))
    for s in (0.01, 0.02, 0.035, 0.05, 0.10):
        ms = required_MS(s, L8, sigma_stat)
        print("  %-16.3f%12.1f%12.1f" % (s, ms, ms / 24.0))
    print("  * 24 logical cores on VideoCPU; a 'run' is one seed at one")
    print("    stage point, and trajectory seeds parallelise cleanly.")

    print("\n--- 5. Worked baseline (the design the spec will start from) ---\n")
    L, M, S = math.log(8.0), 8, 16
    s_tol = required_s_within(sigma_stat, L, M, S)
    print("  lever arm      : V x 8  (scale factor x 2), L = %.4f" % L)
    print("  stage points M : %d" % M)
    print("  seeds S        : %d" % S)
    print("  total runs     : %d" % (M * S))
    print("  tolerable s_within : %.4f  (%.1f%% scatter in rho_Sea)"
          % (s_tol, 100 * s_tol))
    print("  achieved sigma_stat at that s_within : %.4f"
          % sigma_w(s_tol, L, M, S))
    assert abs(sigma_w(s_tol, L, M, S) - sigma_stat) < 1e-12
    print("  -> round-trip consistent: PASS")

    print("\n--- 6. Guard thresholds (frozen with the budget) ---\n")
    print("  F-C1 rate guard      : |w(fast) - w(slow)| <= 3*sigma_total"
          " = %.4f" % (3 * SIGMA_TARGET))
    print("     with the two rates separated by >= 4x in dlnV/dt")
    print("  F-C2 finite-size     : >= 3 values of N; extrapolated intercept")
    print("     uncertainty folded into the %.3f finite-size allocation"
          % ALLOCATION["finite-size extrapolation"])
    print("  F-C3 null-mode       : with expansion frozen (L = 0) the engine")
    print("     must reproduce the fixed-box 3419 result inside its own error")

    print("\n--- 7. Reading rules (frozen before first run) ---\n")
    print("  CONFIRM      : |w_hat + 1| <= 3*sigma_total AND sigma_total <= %.3f"
          % SIGMA_TARGET)
    print("  REFUTE-PROXY : |w_hat + 1| >  3*sigma_total AND sigma_total <= %.3f"
          % SIGMA_TARGET)
    print("                 (magnitude is NOT a reading; needs a new prereg)")
    print("  INDECISIVE   : sigma_total > %.3f -- report achieved sigma and"
          % SIGMA_TARGET)
    print("                 the binding resource; no reading issued")
    print("  INVALID      : F-C1, F-C2 or F-C3 fails -- no reading issued")

    print("\n" + "=" * 70)
    print("ALL CHECKS PASS")
    print("=" * 70)


if __name__ == "__main__":
    main()
