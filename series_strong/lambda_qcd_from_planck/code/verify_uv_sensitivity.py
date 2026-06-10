#!/usr/bin/env python3
"""
verify_uv_sensitivity.py
Project C / SS-1 op:lambda_psr  -- Patch 1002 (Route B opening).

Route B = the UV boundary alpha_s(E_P) is fixed by lattice-discreteness /
PSR-saturation structure near l_P, not by a continuum-log extrapolation.

This script does NOT claim closure. It establishes the framework and proves
the one result that governs the whole project:

  (A) Dimensional transmutation.  Lambda_QCD = E_P * exp(-2pi/(beta0 alpha_UV)),
      Lambda is the IR Landau pole; alpha_UV = alpha_s(E_P) is the sole free
      number of the flow.

  (B) PSR gives the right QUALITATIVE sign.  rem:psr: as r -> l_P,
      PSR_eff -> l_P/2 and alpha_s -> 0.  r -> l_P is short distance = high Q
      = E_P, so PSR saturation predicts alpha_s(E_P) -> 0 (asymptotic freedom
      from the CPP side).  The target value alpha_UV ~ 0.0197 is indeed small
      and positive -- consistent in sign and smallness.  So PSR fixes the SIGN;
      the open piece is the precise VALUE, set by the RATE PSR_eff -> l_P/2.

  (C) THE SENSITIVITY THEOREM (the bar Route B must clear).
      Lambda = E_P e^{-N}, N = 2pi/(beta0 alpha_UV) = ln(E_P/Lambda).
      d(Lambda)/Lambda = (N/alpha_UV) d(alpha_UV).
      With N ~ 45.5 and alpha_UV ~ 0.0197 the amplification is ~2300:
      alpha_UV must be derived to ~1e-4 ABSOLUTE (4 significant figures) to fix
      Lambda to ~20%.  => closure requires an EXACT relation for alpha_UV;
      numerical coincidence-matching at the 1% level is worthless.

  (D) FUTILITY DEMO.  A "natural" enhancement factor R = 2pi^2 (the S^3 volume,
      tempting because the 600-cell tiles S^3) is within ~1% of the naive ratio
      R0 = N_target / N(alpha=5/(8phi)), yet predicts Lambda off by ~30-50%.
      Concrete proof that 1%-level numerology cannot close this.

No PDG Lambda_QCD is used as INPUT; 0.218 GeV appears only as the comparison
target, per the falsifier.
"""

import math

PHI   = (1 + 5 ** 0.5) / 2
E_P   = 1.220890e19            # GeV (l_P route)
BETA0 = 7.0                    # SS-1 thm:beta0 (exact)
LAM_TARGET = 0.218             # GeV TARGET (op:lambda_psr)
ALPHA_LATTICE = 5 / (8 * PHI)  # SM-7 ~= 0.386


def N_of_alpha(alpha):
    return 2 * math.pi / (BETA0 * alpha)


def lambda_of_alpha(alpha):
    return E_P * math.exp(-N_of_alpha(alpha))


def main():
    print("=" * 70)
    print("Patch 1002  Route B framework + sensitivity theorem")
    print("=" * 70)

    # (A) dimensional transmutation + the target UV value
    N_target = math.log(E_P / LAM_TARGET)
    alpha_UV = 2 * math.pi / (BETA0 * N_target)
    print(f"(A) Lambda = E_P exp(-2pi/(beta0 alpha_UV));  N_target = ln(E_P/Lambda) = {N_target:.3f}")
    print(f"    target alpha_UV = alpha_s(E_P) = {alpha_UV:.5f}")
    print()

    # (B) PSR sign check
    print("(B) PSR sign: rem:psr forces alpha_s(E_P) -> 0 (small, positive).")
    print(f"    target {alpha_UV:.5f} is small and positive -> sign CONSISTENT.")
    print()

    # (C) sensitivity theorem
    amp = N_target / alpha_UV                       # d(Lam)/Lam per unit d(alpha)
    dalpha_for_20pct = 0.20 / amp
    print("(C) SENSITIVITY THEOREM  d(Lam)/Lam = (N/alpha) d(alpha)")
    print(f"    amplification N/alpha = {amp:.0f}x")
    print(f"    alpha_UV must be pinned to +/-{dalpha_for_20pct:.1e} (abs) for Lambda to +/-20%")
    sig = -math.log10(dalpha_for_20pct / alpha_UV)
    print(f"    => ~{sig:.1f} significant figures required on alpha_UV.  EXACT relation needed.")
    print()

    # (D) futility of 1% coincidence matching, using R = 2 pi^2 (S^3 volume)
    print("(D) FUTILITY DEMO: 'natural' enhancement R = 2pi^2 (S^3 volume)")
    N_lattice = N_of_alpha(ALPHA_LATTICE)           # continuum run-length from 0.386
    R0 = N_target / N_lattice                       # ratio that WOULD be needed
    R_candidate = 2 * math.pi ** 2
    print(f"    continuum run-length from 5/(8phi):  N = {N_lattice:.3f}")
    print(f"    needed ratio R0 = N_target/N = {R0:.3f};  candidate 2pi^2 = {R_candidate:.3f}"
          f"  ({100*(R_candidate/R0-1):+.1f}%)")
    lam_from_candidate = E_P * math.exp(-R_candidate * N_lattice)
    err = lam_from_candidate / LAM_TARGET - 1
    print(f"    R=2pi^2 -> Lambda = {lam_from_candidate:.4f} GeV  ({100*err:+.0f}% vs target)")
    print(f"    VERDICT: ~1% error in R -> ~{abs(100*err):.0f}% error in Lambda. "
          f"Numerology at 1% is useless; need an exact identity.")
    print()

    print("=" * 70)
    print("Route B target (sharpened): derive alpha_s(E_P) to ~4 sig figs from the")
    print("PSR_eff -> l_P/2 approach rate / 600-cell mode structure. NOT closed here.")
    print("=" * 70)

    # assertions: these are framework facts, all must hold
    ok = True
    ok &= abs(alpha_UV - 0.01974) < 5e-4
    ok &= alpha_UV > 0
    ok &= amp > 1000
    ok &= abs(err) > 0.20          # the 2pi^2 candidate is decisively off
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
