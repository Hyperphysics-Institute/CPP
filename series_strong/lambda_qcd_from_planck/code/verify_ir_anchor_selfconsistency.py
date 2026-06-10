#!/usr/bin/env python3
"""
verify_ir_anchor_selfconsistency.py
Project C / SS-1 op:lambda_psr  -- Patch 1001 (step 0, framing).

Purpose
-------
Lock in what is ALREADY solid before touching the open UV-boundary problem.
This script records three numerical facts that frame the whole derivation; it
does NOT yet attempt the derivation (that is Patch 1002+, Route B).

  (1) IR-anchor self-consistency.  SM-7's lattice coupling alpha_s = 5/(8 phi)
      ~= 0.386, run with the SS-1 one-loop relation (beta0 = 7) down to the
      target Lambda_QCD = 0.218 GeV, lands at a scale Q ~ 2.2 GeV -- exactly
      where physical alpha_s sits at a charmonium-scale.  => the IR end of the
      flow is self-consistent; the picture is not order-of-magnitude wrong.

  (2) The UV boundary condition is the ONE undetermined number.  Inverting the
      same one-loop relation, reproducing Lambda_QCD from the Planck energy
      E_P requires alpha_s(E_P) ~= 0.0197.  The known CPP coupling 5/(8 phi)
      ~= 0.386 is an IR value (see (1)), NOT this.  Closing op:lambda_psr =
      producing ~0.0197 (or its non-log equivalent, Route B) from l_P +
      sea_strength alone, with no PDG input.

  (3) C14 alpha_s-convention flag.  The C14 self-consistent point
      (r_conf = 0.161 fm, sigma = 0.900 GeV/fm) implies alpha_s ~= 0.118
      (the M_Z value), NOT the lattice 0.386.  Feeding 0.386 into C14 gives
      r_conf ~= 0.29 fm.  => op:sigma must state WHICH running alpha_s enters
      C14 before sigma-from-sea_strength can be chained.

NONE of these inputs is the PDG Lambda_QCD; the 0.218 GeV target is used here
only as the value to be reproduced, exactly as the falsifier demands.
"""

import math

# ---- constants (no PDG Lambda_QCD used as INPUT; 0.218 is the TARGET) -------
PHI    = (1 + 5 ** 0.5) / 2          # golden ratio
HBARC  = 0.1973269804                # GeV * fm
E_P    = 1.220890e19                 # GeV  (gravitational Planck energy, l_P route)
BETA0  = 7.0                         # SS-1 thm:beta0 (exact: 11 - 4)
LAM_TARGET = 0.218                   # GeV  TARGET (SS-1 op:lambda_psr)

ALPHA_LATTICE = 5 / (8 * PHI)        # SM-7 lattice coupling ~= 0.386
SIGMA  = 0.900                       # GeV/fm  (C14 self-consistent)
R_CONF = 0.161                       # fm      (C14 self-consistent)

TOL = 0.05                           # 5% bands for the self-consistency checks


def one_loop_alpha(Q, Lam, beta0=BETA0):
    return 2 * math.pi / (beta0 * math.log(Q / Lam))


def one_loop_scale(alpha, Lam, beta0=BETA0):
    """Scale Q at which the running coupling equals `alpha`."""
    return Lam * math.exp(2 * math.pi / (beta0 * alpha))


def check(name, value, expected, tol=TOL, ratio=False):
    if ratio:
        ok = abs(value / expected - 1) <= tol
    else:
        ok = abs(value - expected) <= tol * abs(expected)
    print(f"  [{'PASS' if ok else 'FLAG'}] {name}: {value:.5g} (cf {expected:.5g})")
    return ok


def main():
    print("=" * 68)
    print("Patch 1001 step-0 framing checks  (Project C / op:lambda_psr)")
    print("=" * 68)
    print(f"phi = {PHI:.6f}   5/(8 phi) = {ALPHA_LATTICE:.5f}")
    print(f"E_P = {E_P:.4e} GeV   beta0 = {BETA0:g}   target Lambda = {LAM_TARGET} GeV")
    print()

    results = []

    # (1) IR anchor: where does alpha_s = 5/(8 phi) live?
    print("(1) IR-anchor self-consistency  (the encouraging fact)")
    Q_anchor = one_loop_scale(ALPHA_LATTICE, LAM_TARGET)
    print(f"      5/(8 phi) sits at Q = {Q_anchor:.3f} GeV under beta0=7 -> Lambda=0.218")
    results.append(check("    Q_anchor ~ 2.2 GeV (charmonium scale)", Q_anchor, 2.23))
    print()

    # (2) The UV boundary condition that 1-loop demands
    print("(2) UV boundary condition  (the ONE open number)")
    L = math.log(E_P / LAM_TARGET)
    alpha_uv = one_loop_alpha(E_P, LAM_TARGET)
    print(f"      ln(E_P/Lambda) = {L:.3f}")
    print(f"      required alpha_s(E_P) = 2pi/(beta0*L) = {alpha_uv:.5f}")
    landau_if_lattice_at_EP = E_P * math.exp(-2 * math.pi / (BETA0 * ALPHA_LATTICE))
    print(f"      (feeding 0.386 at E_P instead -> Landau pole at "
          f"{landau_if_lattice_at_EP:.3e} GeV, useless)")
    results.append(check("    required alpha_s(E_P) ~ 0.0197", alpha_uv, 0.0197))
    print()

    # (3) C14 alpha_s-convention flag
    print("(3) C14 alpha_s-convention flag  (settle before chaining op:sigma)")
    alpha_c14 = SIGMA * R_CONF ** 2 / HBARC
    r_from_lattice = math.sqrt(ALPHA_LATTICE * HBARC / SIGMA)
    print(f"      alpha_s implied by (r_conf=0.161, sigma=0.900) = {alpha_c14:.4f}")
    print(f"      r_conf implied by feeding lattice 0.386         = {r_from_lattice:.4f} fm")
    results.append(check("    C14 alpha_s ~ 0.118, NOT 0.386", alpha_c14, 0.118))
    print()

    print("=" * 68)
    if all(results):
        print("ALL FRAMING CHECKS CONSISTENT — IR end solid; UV boundary is the open arc.")
    else:
        print("ONE OR MORE FLAGS — see above (expected for items needing resolution).")
    print("=" * 68)
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
