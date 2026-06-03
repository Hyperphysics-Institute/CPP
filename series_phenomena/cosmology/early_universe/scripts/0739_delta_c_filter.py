#!/usr/bin/env python3
"""
0739_delta_c_filter.py
======================
The CHEAP FALSIFIER for Brick #4's density-dependent c_eff (the next-step filter
flagged in 0738). Branch V makes c_eff = l_P_eff/t_P depend on local absolute SSV
(qDP density, polarization, ...), so c_eff differs between galactic and
intergalactic space. Question: is that ruled out by the observed near-constancy
of fundamental constants?

THE KEY PHYSICS (why this is a fork, not a simple yes/no).
A position-dependent c that is fully absorbed into the METRIC just reproduces
gravity (GR) -- it is NOT constrained; it is exactly what CPP's c07 weak-field
derivation already does (gravitational time dilation IS a position-dependent
clock/propagation rate). What the data bound is variation of the DIMENSIONLESS
constant alpha = e^2/(4 pi eps0 hbar c). And in CPP the DP Sea IS the
electromagnetic medium: c_eff = 1/sqrt(mu eps), alpha ~ sqrt(mu/eps) (the medium
impedance). So:

    Delta c / c   ~ -1/2 (d_mu + d_eps)      (the PRODUCT mu*eps -> c)
    Delta a / a   ~ +1/2 (d_mu - d_eps)      (the RATIO  mu/eps  -> alpha)

where d_mu, d_eps are the fractional DP-Sea responses of mu, eps to an SSV change.
Define the response ASYMMETRY
    A = (d_mu - d_eps) / (d_mu + d_eps)   =>   Delta a/a = -A * Delta c/c.

So the danger is governed ENTIRELY by A:
  * A = 0  (SSV moves mu and eps symmetrically): c varies, alpha FIXED. This is
    pure metric = gravity = what c07 already matches. SAFE; the galactic/
    intergalactic c difference is just gravitational redshift, real but not novel.
  * A ~ O(1) (asymmetric response): alpha tracks the potential as strongly as c
    does => k_alpha ~ 1, which is ~6 orders above the clock bound => FALSIFIED.

Observational inputs (searched, 2026):
  * Spatial alpha dipole (Webb/King/Murphy, VLT+Keck): amplitude few x 10^-6
    across cosmological distances (~4 sigma, still debated).
  * alpha vs gravitational potential, white dwarf G191-B2B
    (Berengut, Flambaum, Webb, Barrow et al. 2013): Da/a=(4.2+-1.6)e-5 at
    dPhi~5e-5  => k_alpha (= Da/a per unit dPhi) ~ 0.8 +- 0.3  (WEAK: |k_a|<~1).
  * Atomic-clock local-position-invariance (Sr/Dy/Rb-Cs fountains): the TIGHT
    bound, |k_alpha| <~ 1e-6.

This script computes, for the galactic-vs-intergalactic SSV step, the
falsification MARGIN as a function of A, and reports the pass condition.
"""

import numpy as np

# --- gravitational-potential contrasts (dimensionless Phi/c^2) ---------------
PHI_GALAXY = 1e-6      # ~ (200 km/s / c)^2 : Galaxy / solar-neighbourhood well
PHI_CLUSTER = 1e-5     # cluster scale
PHI_WD = 5e-5          # white-dwarf surface (the Berengut probe)

# --- observational bounds on alpha variation ---------------------------------
ALPHA_SPATIAL_DIPOLE = 3e-6     # |Da/a| across Gpc (cosmological, debated)
K_ALPHA_WD = 1.0                # weak bound on Da/a per unit dPhi (white dwarf)
K_ALPHA_CLOCK = 1e-6            # TIGHT bound on Da/a per unit dPhi (clocks/LPI)


def report():
    print("=" * 74)
    print("BRICK #4 Delta-c / LPI FILTER -- does density-dependent c_eff survive?")
    print("=" * 74)

    print("\nFraming: in CPP the DP Sea is the EM medium, so")
    print("   Delta c/c ~ -1/2 (d_mu+d_eps)  [product -> c];  "
          "Delta a/a ~ +1/2 (d_mu-d_eps)  [ratio -> alpha]")
    print("   => Delta a/a = -A * Delta c/c,  A = (d_mu-d_eps)/(d_mu+d_eps)  "
          "(response asymmetry)")
    print("   k_alpha (Da/a per unit dPhi) = A, since the metric part Dc/c ~ dPhi.")

    print("\n--- The fork (A is the single deciding structural number) -------------")
    print(f"{'asymmetry A':>14} | {'k_alpha=A':>10} | {'vs clock 1e-6':>14} | verdict")
    print("-" * 74)
    for A in (0.0, 1e-9, 1e-7, 1e-6, 1e-3, 1.0):
        margin = A / K_ALPHA_CLOCK if K_ALPHA_CLOCK else np.inf
        if A == 0.0:
            verdict = "SAFE (pure metric = gravity = c07/GR)"
        elif A <= K_ALPHA_CLOCK:
            verdict = "PASS (within clock LPI bound)"
        else:
            verdict = f"FAIL by x{margin:.0e} (above clock bound)"
        print(f"{A:>14.0e} | {A:>10.0e} | {margin:>12.1e}x | {verdict}")

    print("\n--- What is ALREADY known about A (narrows the open question) ---------")
    print("  The GRAVITATIONAL SSV channel must be (near-)symmetric: c07 reproduces")
    print("  gravitational time dilation AND LPI holds to k_alpha<~1e-6, so the")
    print("  gravity-driven part of the DP-Sea response already has A_grav <~ 1e-6.")
    print("  => The ONLY open question is the COMPOSITION (qDP-density) channel:")
    print("     does changing qDP density move mu and eps symmetrically too?")

    print("\n--- Numbers for the galactic/intergalactic step -----------------------")
    dPhi = PHI_GALAXY
    print(f"  galactic dPhi/c^2 ~ {dPhi:.0e}  => metric Dc/c ~ {dPhi:.0e} "
          f"(REQUIRED; this is gravity, matches c07)")
    for A, lbl in ((1e-6, "if composition channel symmetric to 1e-6"),
                   (1.0, "if composition channel O(1) asymmetric")):
        da = A * dPhi
        status = "within" if da <= ALPHA_SPATIAL_DIPOLE and A <= K_ALPHA_CLOCK else "ABOVE"
        print(f"    A={A:.0e} ({lbl}): Da/a ~ {da:.0e}  -> {status} bounds")

    print("\n" + "=" * 74)
    print("VERDICT")
    print("=" * 74)
    print("  NOT a clean kill and NOT a free pass. The filter converts the danger")
    print("  into ONE decidable structural question:")
    print("    Does an SSV change move the DP-Sea mu and eps SYMMETRICALLY?")
    print("    * symmetric (A<~1e-6): c varies = gravity, alpha fixed -> SURVIVES all")
    print("      bounds; the galactic/intergalactic c difference is gravitational,")
    print("      real but not novel/dangerous. (And the gravity channel is ALREADY")
    print("      known symmetric from c07+LPI.)")
    print("    * asymmetric (A~O(1)): alpha tracks potential -> k_alpha~1 -> FALSIFIED")
    print("      by ~6 orders vs the clock bound.")
    print("  So Branch V is SAFE *iff* the DP-Sea response to SSV (esp. the qDP-")
    print("  density/composition channel) is mu<->eps symmetric. That symmetry is")
    print("  decidable from the DP-Sea structure (4 species; how SSV polarizes them)")
    print("  -- the next first-principles target. The theory is NOT yet falsified.")


if __name__ == "__main__":
    report()
