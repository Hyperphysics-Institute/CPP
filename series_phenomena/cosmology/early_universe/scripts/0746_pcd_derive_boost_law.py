#!/usr/bin/env python3
"""
0746_pcd_derive_boost_law.py
============================
THE decisive PCD-level derivation: does the over-occupation relaxation boost h(n)
come out ENTROPIC (~ ln n -> n_s=0.9649) or MECHANICAL (~n^q -> excluded)? Run
honestly -- derive from CPP's actual displacement mechanism, report whatever wins.

CPP GROUNDING (master_glossary):
  - Displacement / drift is driven by SSV_net = the VECTOR sum of stress
    contributions (gravity = SSV_net gradient; c07).
  - SSV_abs = the MAGNITUDE; it sets PSR and the time rate (the gravity/clock
    channel), and does NOT cancel.
  - The DP Sea and the early cohort are net-NEUTRAL (dipoles; balanced mix).

So the relevant scalings of a stack of n CPs/DPs on one GP:
  (A) SSV_abs  ~ n            (every contribution adds in magnitude; never cancels)
  (B) SSV_net  ~ sqrt(n)      (a NEUTRAL stack: monopoles cancel, but residual
                              charge/multipole fluctuations random-walk to ~sqrt(n);
                              ~ n if charge-IMBALANCED)
  (C) entropic ~ ln n         (configurational chemical potential of dispersal,
                              charge-blind, NOT sourced by SSV)

H_eff (the expansion rate) is whatever DOMINATES the boost. n_s - 1 = 2 d ln H_eff/dN,
nbar(N)=nbar_init e^{-3N}, pivot N_rem~57 (nbar ~ e^171 ~ 1e74).

The question is NOT just "which form gives 0.965" (0745 answered: only ln n). It is:
when several channels are present, WHICH ONE DOMINATES H_eff at the pivot?
"""

import numpy as np

N_CP, N_GP_INIT = 1e80, 13
N_star = (1.0/3.0)*np.log(N_CP/N_GP_INIT)
Np = N_star - 57.0
nbar_pivot = (N_CP/N_GP_INIT)*np.exp(-3.0*Np)


def ns_for(power_or_log, N):
    eps = 1e-4
    nbar = lambda x: (N_CP/N_GP_INIT)*np.exp(-3.0*x)
    if power_or_log == "log":
        H = lambda x: np.log(max(nbar(x), 1+1e-9))
    else:
        q = power_or_log
        H = lambda x: nbar(x)**q
    lnH = lambda x: np.log(H(x))
    return 1.0 + 2.0*(lnH(N+eps)-lnH(N-eps))/(2*eps)


def main():
    print("="*76)
    print("PCD DERIVATION: which channel drives the over-occupation boost h(n)?")
    print("="*76)
    print(f"  pivot: nbar ~ {nbar_pivot:.1e}  (ln nbar = {np.log(nbar_pivot):.0f}, "
          f"N_rem = {np.log(nbar_pivot)/3:.0f})\n")

    print("  Channel magnitudes at the pivot (which is BIGGEST drives H_eff):")
    print(f"    SSV_abs   ~ n        = {nbar_pivot:.1e}")
    print(f"    SSV_net   ~ sqrt(n)  = {np.sqrt(nbar_pivot):.1e}   (neutral-stack residual)")
    print(f"    entropic  ~ ln n     = {np.log(nbar_pivot):.1e}")
    print(f"  => SSV_net (~1e37) DWARFS entropic (~1e2) by ~35 orders. A stress channel,")
    print(f"     once present, DOMINATES the configurational/entropic channel.\n")

    print(f"  {'channel drives H_eff':>34} | {'scaling':>10} | {'n_s':>8} | verdict")
    print("  "+"-"*76)
    rows = [
        ("SSV_abs (magnitude)",     "n",       ns_for(1.0, Np)),
        ("SSV_net (neutral, ~sqrt n)","n^1/2",  ns_for(0.5, Np)),
        ("SSV_net (imbalanced, ~n)", "n",       ns_for(1.0, Np)),
        ("entropic / configurational","ln n",   ns_for("log", Np)),
    ]
    for label, scal, ns in rows:
        if abs(ns-0.9649) < 0.02:
            v = "-> n_s=0.965 (only if this ALONE drives H_eff)"
        elif ns < 0.5:
            v = f"-> n_s={ns:.1f}  EXCLUDED (mechanical)"
        else:
            v = "-> off"
        print(f"  {label:>34} | {scal:>10} | {ns:>8.4f} | {v}")

    print("\n"+"="*76)
    print("VERDICT -- reported straight (a genuine FORK)")
    print("="*76)
    print("""  This sharpens to ONE structural question: what does the boost couple to?
  Key fact: the boost acts on PSR_BASE, the SSV-INDEPENDENT baseline reach
  (PSR_eff = PSR_base/(1 + alpha*SSV_abs); SSV only modulates PSR_base DOWN). Two
  readings of the over-occupation boost follow:

   (i) COUNT-DRIVEN / configurational: the baseline reach relaxes by the OCCUPATION
       COUNT n (how over-stacked), decoupled from the instantaneous SSV field --
       natural BECAUSE PSR_base is SSV-independent by construction. The dispersal
       drive of a count is the configurational chemical potential ~ ln(n)
       -> n_s = 0.9649. The residual-fluctuation problem does NOT apply (count-
       driven, not field-driven).

  (ii) SSV-STRESS-DRIVEN: the boost tracks the stress the stack sources -> MECHANICAL.
       SSV_abs ~ n (n_s=-5); or even for a NEUTRAL stack, SSV_net ~ sqrt(n) from
       residual charge/multipole fluctuations (n_s=-2). EXCLUDED. And the charge-
       neutrality hope of 0745 does NOT rescue this: neutrality cancels the monopole,
       but the residual sqrt(n) stress DWARFS the entropic ln(n) by ~35 orders at the
       pivot. If stress-mediated, excluded regardless of neutrality.

  HONEST VERDICT -- a genuine FORK, neither clean win nor clean kill:
    * The data REQUIRE reading (i): count-driven configurational ln(n) -> 0.9649.
    * Reading (i) is STRUCTURALLY DEFENSIBLE: the boost acts on the SSV-INDEPENDENT
      baseline PSR_base, so its growth being occupation/count-driven (not a stress
      response) is natural.
    * Reading (ii), the 'everything-is-SSV-mediated' default, gives EXCLUDED
      mechanical, and 0745's charge-neutrality rescue specifically FAILS for it.

  NEW, decisive content this patch adds: (a) IF the boost is stress-mediated it is
  EXCLUDED and neutrality cannot save it (the sqrt(n) residual buries the log);
  (b) the escape is the COUNT-DRIVEN reading, legitimate precisely because PSR_base
  is the SSV-independent baseline. So n_s=0.9649 is VIABLE iff the PSR_base boost is
  count-driven/configurational rather than SSV-stress-driven.

  REMAINING (the single coupling question that decides everything): do the PCD rules
  grow PSR_base from the occupation COUNT (-> ln n -> 0.965) or from the SSV STRESS
  field (-> mechanical -> excluded)? Scaling-level analysis, not a closed PCD solution
  -- a sharpened fork, with a defensible path to 0.965.""")


if __name__ == "__main__":
    main()
