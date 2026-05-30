#!/usr/bin/env python3
"""
verify_bii_chi_normalization.py
B-ii magnitude-anchors scope sketch (Patch 0669, Session 151) verification.

Scope sketch: chir_bii_magnitude_anchors_scoping.md
Target: confirm the chi "phi^-1 vs phi^-3" reconciliation is a documentation
        artifact, not a physics tension -- by machine-checking the arithmetic that
        underlies the resolution.

This script derives NO new physics. It verifies already-registered identities
(CHI-1, CAP-1) to demonstrate that:
  - phi^-1 (the first-shell DISTANCE) and phi^-3 (the chirality MAGNITUDE) are
    genuinely different numbers (so they cannot be two normalizations of one
    quantity -- one is distance, one is bias);
  - CHI-1's symmetric-bias map sends the input distance phi^-1 to the output
    magnitude phi^-3 EXACTLY: (1 - phi^-1)/(1 + phi^-1) = phi^-3;
  - the algebra 1 - phi^-1 = phi^-2 and 1 + phi^-1 = phi (the golden-ratio
    identities CHI-1 uses);
  - the shipped P-face anchor Delta p_LR = chi/6 = phi^-3/6 ~ 0.0394 uses phi^-3
    (NOT phi^-1), consistent within ~2% of the empirical anchor ~0.04;
  - the dead-end value phi^-1 ~ 0.618 is the edge-length scale (C-1 geometric
    inconsistency) and does NOT match the empirical anchor (C-2).

No verdict moves (chirality stays V3/W3). B-ii is supporting evidence only.
"""

PHI = (1.0 + 5.0 ** 0.5) / 2.0
TOL = 1e-12

inv1 = PHI ** -1   # phi^-1  ~ 0.618  : first-shell DISTANCE / edge-length scale
inv2 = PHI ** -2   # phi^-2  ~ 0.382
inv3 = PHI ** -3   # phi^-3  ~ 0.236  : the chirality MAGNITUDE chi = FI-C-9


def main():
    print("=" * 68)
    print("B-ii chi normalization reconciliation  (phi^-1 vs phi^-3)")
    print("=" * 68)
    ok = True

    # CHECK 1: phi^-1 and phi^-3 are different numbers (distance vs magnitude)
    c1 = abs(inv1 - inv3) > 0.3
    ok &= c1
    print(f"\n[1] phi^-1={inv1:.6f} (distance)  !=  phi^-3={inv3:.6f} (magnitude)")
    print(f"    distinct quantities, not two normalizations of one -> {'PASS' if c1 else 'FAIL'}")

    # CHECK 2: golden-ratio identities CHI-1 uses
    c2a = abs((1 - inv1) - inv2) < TOL          # 1 - phi^-1 = phi^-2
    c2b = abs((1 + inv1) - PHI) < TOL           # 1 + phi^-1 = phi
    ok &= (c2a and c2b)
    print(f"\n[2] 1 - phi^-1 = phi^-2 : {1-inv1:.6f} vs {inv2:.6f}  {'ok' if c2a else 'FAIL'}")
    print(f"    1 + phi^-1 = phi    : {1+inv1:.6f} vs {PHI:.6f}  {'ok' if c2b else 'FAIL'}")
    print(f"    -> {'PASS' if (c2a and c2b) else 'FAIL'}")

    # CHECK 3: the symmetric-bias map sends the distance phi^-1 to the magnitude phi^-3
    bias = (1 - inv1) / (1 + inv1)              # = phi^-2 / phi = phi^-3
    c3 = abs(bias - inv3) < TOL
    ok &= c3
    print(f"\n[3] chi = (1 - phi^-1)/(1 + phi^-1) = {bias:.6f}  vs  phi^-3 = {inv3:.6f}")
    print(f"    CHI-1 builds the magnitude phi^-3 FROM the distance phi^-1 -> {'PASS' if c3 else 'FAIL'}")

    # CHECK 4: shipped P-face anchor uses phi^-3, matches empirical anchor
    dplr = inv3 / 6.0
    anchor = 0.04
    c4 = abs(dplr - anchor) / anchor < 0.02 + 1e-9   # within ~2%
    ok &= c4
    print(f"\n[4] Delta p_LR = chi/6 = phi^-3/6 = {dplr:.6f}  vs anchor ~{anchor}")
    print(f"    rel. dev = {abs(dplr-anchor)/anchor*100:.2f}%  (uses phi^-3, NOT phi^-1) -> {'PASS' if c4 else 'FAIL'}")

    # CHECK 5: the dead-end phi^-1 does NOT match the anchor (C-2) and is the edge scale (C-1)
    dplr_dead = inv1 / 6.0
    c5 = abs(dplr_dead - anchor) / anchor > 1.5      # badly off
    ok &= c5
    print(f"\n[5] if (wrongly) chi=phi^-1: chi/6 = {dplr_dead:.6f}, rel.dev {abs(dplr_dead-anchor)/anchor*100:.0f}%")
    print(f"    dead-end value fails the empirical anchor (C-2); phi^-1=edge scale (C-1) -> {'PASS' if c5 else 'FAIL'}")

    print("\n" + "=" * 68)
    print("RESULT:", "ALL CHECKS PASS" if ok else "FAILURE")
    print("No live phi^-1-vs-phi^-3 tension: phi^-3 is the magnitude (live),")
    print("phi^-1 the distance it is built from + the retired conjecture (C-1/C-2/C-3).")
    print("No verdict move (chirality stays V3/W3).")
    print("=" * 68)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
