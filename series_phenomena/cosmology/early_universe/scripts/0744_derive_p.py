#!/usr/bin/env python3
"""
0744_derive_p.py
================
The decisive computation: derive p (in n_s = 1 - p/N_*) from the CPP substrate,
rather than leaving it free (0742). If the substrate gives p=2, n_s=0.965 becomes
a genuine CPP prediction and the spectrum thread closes. Run honestly -- report
whatever p comes out, even if it is not 2.

THE REDUCTION (delta-N formalism, rigorous).
The curvature perturbation is the fluctuation in the number of e-folds:
    zeta = delta-N = (1/3)(delta_nbar / nbar)   [since N_rem = (1/3) ln nbar].
Frozen at horizon crossing, the dimensionless power is P ~ H_eff^2 (amplitude set
by the expansion rate), so
    n_s - 1 = d ln P / d ln k = 2 d ln H_eff / dN   (at crossing).
Therefore p is fixed ENTIRELY by how the expansion rate H_eff depends on the
superposition state -- i.e. by the boost rule's dependence on occupancy nbar.
With nbar(N) = nbar_init e^{-3N} and N_rem = (1/3) ln nbar:

   H_eff coupling          d ln H_eff/dN        n_s - 1          p (n_s=1-p/N_*)
   ---------------------    ------------------   --------------   ---------------
   depth-INDEPENDENT        0                    0                0   (n_s=1)
   (per-GP: boost iff
    superposed, regardless
    of how many CPs)
   LOG of occupancy         -1/N_rem             -2/N_rem         2   (n_s=1-2/N_*)
   (H_eff ~ ln nbar
    ~ N_rem: expansion
    winds down linearly
    toward the end)
   LINEAR in occupancy      -3                   -6               6*N_rem (huge)
   (per-CP: boost once per
    superposed CP)

So p is set by the boost rule. The question: which coupling is the CPP axiom?
"""

import numpy as np

NS_PLANCK, NS_ERR = 0.9649, 0.0042
N_CP, N_GP_INIT = 1e80, 13
N_star = (1.0 / 3.0) * np.log(N_CP / N_GP_INIT)


def nbar(N):
    return (N_CP / N_GP_INIT) * np.exp(-3.0 * N)


def ns_for_coupling(coupling, N):
    """n_s = 1 + 2 d ln H_eff/dN for a given H_eff(nbar) coupling."""
    h = 1e-4
    lnH = lambda x: np.log(coupling(nbar(x)))
    return 1.0 + 2.0 * (lnH(N + h) - lnH(N - h)) / (2 * h)


def main():
    print("=" * 74)
    print("DERIVING p: which boost-depth coupling does the CPP axiom give?")
    print("=" * 74)
    print(f"  n_s = 1 + 2 d ln H_eff/dN  (delta-N: zeta=(1/3)(d_nbar/nbar); P~H_eff^2)")
    print(f"  N_* = {N_star:.1f} (CP count).  Planck n_s = {NS_PLANCK} +- {NS_ERR}\n")

    # observable pivot crosses ~57 e-folds BEFORE the end => N_rem ~ 57,
    # i.e. EARLY in inflation (N ~ N_star - 57 ~ 3.5), NOT near the end.
    Npivot = N_star - 57.0
    N_rem_pivot = N_star - Npivot
    print(f"  pivot at N={Npivot:.1f} (N_rem={N_rem_pivot:.0f}, ln nbar={np.log(nbar(Npivot)):.0f})\n")
    couplings = {
        "depth-INDEPENDENT (per-GP: boost iff superposed)":
            (lambda nb: 1.0, "p=0"),
        "LOG of occupancy  (H_eff ~ ln nbar ~ N_rem)":
            (lambda nb: np.log(max(float(nb), 1.0 + 1e-9)), "p=2"),
        "LINEAR in occupancy (per-CP: boost once per CP)":
            (lambda nb: float(nb), "p=6 N_rem"),
        "weak power  H_eff ~ nbar^q, q=0.006 (tuned)":
            (lambda nb: float(nb) ** 0.006, "tuned"),
    }
    print(f"  {'boost-depth coupling':>50} | {'n_s':>8} | verdict")
    print("  " + "-" * 84)
    for label, (cpl, plabel) in couplings.items():
        ns = float(ns_for_coupling(cpl, Npivot))
        if abs(ns - 1.0) < 1e-6:
            verdict = "n_s=1 (HZ) -- EXCLUDED ~8sigma  [the literal axiom]"
        elif abs(ns - NS_PLANCK) < 3 * NS_ERR:
            verdict = "MATCHES Planck"
        elif ns < 0.9:
            verdict = "far too red -- EXCLUDED"
        else:
            verdict = "near Planck (by construction/tuning)"
        print(f"  {label:>50} | {ns:>8.4f} | {verdict}")

    print("\n" + "=" * 74)
    print("VERDICT -- reported straight")
    print("=" * 74)
    print("""  p is fixed by how the per-tick boost depends on superposition DEPTH, and
  the answer hinges on whether the graceful EXIT is a smooth wind-down or a cliff:

    * LITERAL axiom (per-GP: a GP boosts its PSR once if superposed, regardless
      of stack depth) is depth-INDEPENDENT => H_eff = const until the fraction f
      cliffs at the very end (the 0741 result) => p=0 => n_s=1 (Harrison-
      Zel'dovich), EXCLUDED at ~8 sigma. A CLIFF gives the wrong (zero) tilt.

    * per-CP (each stacked CP boosts) is LINEAR in depth => H_eff ~ nbar
      => n_s wildly red, EXCLUDED.

    * The data value p=2 (n_s = 1 - 2/N_* = 0.9649, on the nose) corresponds to
      H_eff ~ ln(nbar) ~ N_rem: the expansion rate winds DOWN LINEARLY with
      e-folds-remaining. That is a SMOOTH graceful exit -- and it is exactly the
      canonical slow-roll form (the m^2 phi^2 value, n_s = 1 - 2/N). It tracks the
      mean stack DEPTH (which declines smoothly as e^{-3N}) rather than the
      superposed FRACTION f (which cliffs).

  HONEST CONCLUSION: n_s=0.965 is NOT yet a clean CPP prediction, but deriving p
  has SHARPENED the question to a single, physically natural fork:
     does the superposition depletion drive a SMOOTH wind-down of H_eff
     (tracking depth ln nbar ~ N_rem  =>  n_s = 0.9649, canonical slow-roll),
     or the literal CLIFF (tracking fraction f  =>  n_s = 1, EXCLUDED)?
  The bare on/off axiom gives the cliff (excluded). A realistic smooth graceful
  exit gives 0.9649 exactly. The mean depth nbar DOES decline smoothly (unlike f),
  so a depth-tracking H_eff is plausible -- but the bare axiom is fraction-based,
  and the depth-coupling H_eff ~ ln(nbar) is NOT derived. So: plausibly favorable,
  not proven. The remaining computation: show CPP's H_eff tracks ln(depth), not f.""")


if __name__ == "__main__":
    main()
