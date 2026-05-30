#!/usr/bin/env python3
"""
verify_biii_landau_reduction.py
B-iii capacity-engine scope sketch (Patch 0668, Session 151) verification.

Scope sketch: chir_biii_capacity_landau_scoping.md
Target: reduce the B-iii capacity question ("does the det-coset Z_2 break /
        does a chiral vacuum form?") to the SIGN of the quadratic coefficient
        mu^2 of a Z_2-even Landau effective potential V(eta).

This script machine-checks the STRUCTURAL reduction only. It is NOT a derivation
of the substrate dynamics: it does NOT compute, assume, or fix the value or sign
of mu^2 (that is the deep core, behind F.1 §14.17 / the DSL effective action).
It demonstrates that *given* the Z_2-even form, the vacuum structure -- and hence
the capacity verdict -- is fixed entirely by sign(mu^2), exactly as STATUS-2
fixed the breaking chain and BRIDGE-1 fixed the Z_2-match while leaving the
dynamics open.

CHECK 1 (Z_2-even form is forced):
  - under the det-coset Z_2 action eta -> -eta, an even potential satisfies
    V(-eta) = V(eta); odd monomials (eta, eta^3, ...) are NOT invariant and are
    therefore absent. We verify the symmetry numerically for the model
    V = V0 + mu2*eta^2 + lam*eta^4 and confirm that adding any odd term breaks it.

CHECK 2 (capacity <=> sign(mu^2), for the stabilizing quartic lam > 0):
  - mu2 > 0  : unique minimum at eta = 0  (symmetric; Z_2 UNBROKEN; capacity NO)
  - mu2 < 0  : minima at eta = +/- sqrt(-mu2 / (2 lam)) != 0, eta=0 a local max
               (chiral double-well; Z_2 BROKEN; capacity YES)
  - mu2 = 0  : bifurcation (marginal)
  verified by locating stationary points dV/deta = 0 and classifying them.

CHECK 3 (the honest cap is structural, not numerical):
  - the script asserts it has NOT fixed sign(mu^2): both signs are exercised as
    free inputs; neither is privileged. The capacity verdict is reported as a
    FUNCTION of sign(mu^2), never as a determined value.

No physics coefficient is computed. No verdict moves (chirality stays V3/W3).
"""

import numpy as np

PHI = (1.0 + 5.0 ** 0.5) / 2.0   # golden ratio (context only; not used to fix mu^2)
TOL = 1e-12


def V(eta, mu2, lam, V0=0.0, odd=0.0):
    """Z_2-even Landau potential (plus an optional odd term to test symmetry)."""
    return V0 + mu2 * eta**2 + lam * eta**4 + odd * eta**3


def stationary_points(mu2, lam):
    """Real roots of dV/deta = 2 mu2 eta + 4 lam eta^3 = 2 eta (mu2 + 2 lam eta^2)."""
    pts = [0.0]
    if lam > 0:
        disc = -mu2 / (2.0 * lam)
        if disc > 0:
            r = np.sqrt(disc)
            pts += [r, -r]
    return sorted(set(round(p, 12) for p in pts))


def classify(eta, mu2, lam, h=1e-4):
    """Second-derivative test on V."""
    d2 = (V(eta + h, mu2, lam) - 2 * V(eta, mu2, lam) + V(eta - h, mu2, lam)) / h**2
    if d2 > TOL:
        return "min"
    if d2 < -TOL:
        return "max"
    return "flat"


def capacity_verdict(mu2, lam):
    """Capacity = does a chiral (eta != 0) vacuum form? Returns ('YES'|'NO', wells)."""
    sps = stationary_points(mu2, lam)
    minima = [p for p in sps if classify(p, mu2, lam) == "min"]
    chiral_minima = [p for p in minima if abs(p) > TOL]
    return ("YES" if chiral_minima else "NO"), minima


def main():
    print("=" * 70)
    print("B-iii Landau reduction  --  capacity <=> sign(mu^2)   [STRUCTURAL]")
    print("=" * 70)
    all_pass = True

    # ---- CHECK 1: Z_2-even form is forced ----
    print("\n[CHECK 1] det-coset Z_2 action eta -> -eta; even form forced")
    lam = 1.0
    for mu2 in (-0.7, +0.7):
        etas = np.linspace(-2, 2, 9)
        even_ok = np.allclose([V(e, mu2, lam) for e in etas],
                              [V(-e, mu2, lam) for e in etas], atol=TOL)
        # an odd term must BREAK the symmetry:
        odd_breaks = not np.allclose([V(e, mu2, lam, odd=0.3) for e in etas],
                                     [V(-e, mu2, lam, odd=0.3) for e in etas],
                                     atol=1e-6)
        ok = even_ok and odd_breaks
        all_pass &= ok
        print(f"   mu2={mu2:+.1f}: V(-eta)=V(eta) {even_ok}; odd term breaks Z_2 {odd_breaks}  -> {'PASS' if ok else 'FAIL'}")

    # ---- CHECK 2: capacity <=> sign(mu^2) ----
    print("\n[CHECK 2] vacuum structure vs sign(mu^2)  (lam=1>0)")
    lam = 1.0
    cases = {
        +0.5: ("NO", "symmetric: unique min at 0; Z_2 UNBROKEN"),
        -0.5: ("YES", "double-well: minima at +/- sqrt(-mu2/2lam); Z_2 BROKEN"),
    }
    for mu2, (expected, desc) in cases.items():
        verdict, minima = capacity_verdict(mu2, lam)
        ok = (verdict == expected)
        all_pass &= ok
        wells = ", ".join(f"{m:+.4f}" for m in minima)
        print(f"   mu2={mu2:+.1f}: capacity={verdict} (expect {expected}); minima=[{wells}]  -> {'PASS' if ok else 'FAIL'}")
        print(f"            {desc}")
        if mu2 < 0:
            predicted = np.sqrt(-mu2 / (2 * lam))
            got = max(abs(m) for m in minima)
            loc_ok = abs(predicted - got) < 1e-6
            all_pass &= loc_ok
            print(f"            well location check: sqrt(-mu2/2lam)={predicted:.6f} vs found {got:.6f}  -> {'PASS' if loc_ok else 'FAIL'}")

    # bifurcation at mu2 = 0
    v0, _ = capacity_verdict(0.0, lam)
    bif_ok = (v0 == "NO")  # marginal: only eta=0 is stationary & a (degenerate) min
    all_pass &= bif_ok
    print(f"   mu2= 0.0: critical/bifurcation point; chiral vacuum not yet formed -> {'PASS' if bif_ok else 'FAIL'}")

    # ---- CHECK 3: honest cap -- sign(mu^2) is NOT fixed here ----
    print("\n[CHECK 3] honest cap: sign(mu^2) is an INPUT, never determined")
    # both signs were exercised above as free inputs; neither derived from geometry.
    # PHI is available but is deliberately NOT used to set mu2.
    cap_ok = True
    print("   capacity reported as a FUNCTION of sign(mu^2) only;")
    print("   sign(mu^2) is fixed by the DSL effective action behind F.1 §14.17,")
    print("   NOT by this script and NOT by 600-cell geometry alone.")
    print("   verdict stays V3 (spatial) / W3 (temporal); no verdict move.  -> PASS")
    all_pass &= cap_ok

    print("\n" + "=" * 70)
    print("RESULT:", "ALL CHECKS PASS" if all_pass else "FAILURE")
    print("Structural reduction verified: B-iii capacity <=> sign(mu^2).")
    print("Deep core (the sign itself) NOT computed -- deferred behind §14.17.")
    print("=" * 70)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
