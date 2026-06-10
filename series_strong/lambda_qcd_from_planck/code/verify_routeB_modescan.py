#!/usr/bin/env python3
"""
verify_routeB_modescan.py
Project C / Route B (Patch 1003).

Falsification-first test of the hypothesis:

  "A natural invariant of the 600-cell graph-Laplacian spectrum supplies
   alpha_s(E_P) = 0.01974... to the sub-percent precision the sensitivity
   theorem (Patch 1002) requires."

Method: enumerate a FIXED, pre-declared set of natural candidate values
(spectral invariants, golden-ratio powers, sea_strength, and the PSR-motivated
g0 = 1/2), interpret each as the bare coupling, and record the resulting
Lambda_QCD error. NO denominator is fitted to the target; reverse-fitted
"exact" matches are deliberately EXCLUDED (they prove nothing -- see the doc).

Honest verdict (asserted below): NO natural candidate lands within 20% on
Lambda. The closest principled one, g0 = 1/2 (echoing PSR_eff -> l_P/2), gives
Lambda ~ 0.31 GeV (+42%) -- a real parameter-free order-of-magnitude-plus
result, but failing the sub-percent bar. => Route-B-by-invariant-matching does
NOT close. This is the finding the patch records.

No PDG Lambda_QCD is an INPUT; 0.218 GeV is only the comparison target.
"""

import math

PHI   = (1 + 5 ** 0.5) / 2
E_P   = 1.220890e19
BETA0 = 7.0
LAM_TARGET = 0.218
GAP   = 6 / PHI ** 2          # 600-cell Laplacian spectral gap
LMAX  = 12 + 6 / PHI          # largest Laplacian eigenvalue


def lambda_err(g0_sq):
    """Lambda_QCD relative error if the BARE coupling squared is g0_sq."""
    alpha = g0_sq / (4 * math.pi)
    if alpha <= 0:
        return float("inf")
    lam = E_P * math.exp(-2 * math.pi / (BETA0 * alpha))
    return lam / LAM_TARGET - 1


# pre-declared natural candidates for the BARE coupling g0^2 (NOT fitted)
CANDIDATES = {
    "g0 = 1/2  (PSR_eff->l_P/2 echo)": 0.25,
    "g0^2 = phi^-3":                   PHI ** -3,
    "g0^2 = sea_strength = 0.185":     0.185,
    "g0^2 = 1/(2 phi^2)":              1 / (2 * PHI ** 2),
    "g0^2 = gap/9":                    GAP / 9,
    "g0^2 = gap/lambda_max":           GAP / LMAX,
    "g0^2 = 2/lambda_max":             2 / LMAX,
    "g0^2 = 5/(8 phi)/phi":            (5 / (8 * PHI)) / PHI,
}

TOL = 0.20    # "within 20% on Lambda" = the loosest bar the sensitivity theorem allows


def main():
    target_alpha = 2 * math.pi / (BETA0 * math.log(E_P / LAM_TARGET))
    print("=" * 70)
    print("Patch 1003  Route B mode-structure scan (falsification-first)")
    print("=" * 70)
    print(f"target alpha_s(E_P) = {target_alpha:.6f}  (g0^2 = {4*math.pi*target_alpha:.5f})")
    print(f"600-cell Laplacian: gap = 6 phi^-2 = {GAP:.5f},  lambda_max = {LMAX:.5f}")
    print()
    print(f"{'candidate (bare g0^2)':38s} {'g0^2':>8s} {'Lambda':>10s} {'err':>8s}")
    print("-" * 70)
    results = []
    for name, g2 in CANDIDATES.items():
        e = lambda_err(g2)
        lam = LAM_TARGET * (1 + e)
        results.append((abs(e), name, g2, e))
        flag = "" if abs(e) > TOL else "  <-- within 20%"
        print(f"{name:38s} {g2:8.5f} {lam:9.4g}G {100*e:+7.0f}%{flag}")
    print()

    results.sort()
    best_abs, best_name, best_g2, best_e = results[0]
    print(f"closest principled candidate: {best_name}")
    print(f"  -> Lambda = {LAM_TARGET*(1+best_e):.4f} GeV  ({100*best_e:+.0f}% vs target)")
    print()

    within = [r for r in results if r[0] <= TOL]
    print("=" * 70)
    if not within:
        print("VERDICT: NO natural invariant within 20% on Lambda.")
        print("Route-B-by-invariant-matching does NOT close. Strongest positive")
        print("residue: g0=1/2 -> Lambda~0.31 GeV (+42%), a real parameter-free")
        print("order-of-magnitude result. Sub-percent closure NOT achieved.")
    else:
        print("VERDICT: a candidate landed within 20% -- escalate to swarm review,")
        print("do NOT declare closure (sensitivity theorem: need an exact identity).")
    print("=" * 70)

    # the patch's finding is the NEGATIVE result: assert it explicitly
    return 0 if not within else 1


if __name__ == "__main__":
    raise SystemExit(main())
