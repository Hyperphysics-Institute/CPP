#!/usr/bin/env python3
"""
0749_stack_entropy_test.py
==========================
Tests the swarm's (Copilot) stack-entropy proposal: drive H by the configurational
entropy of n CPs on a GP, S(n), with H ~ dS/dn (chemical potential). Claim:
Omega(n) ~ n! "generically" => S ~ ln(n!) => dS/dn ~ ln n => H ~ ln n => n_s=0.9649.

The CONVERGENCE is correct (0748 showed: only microstate counting can give the log).
But "Omega ~ n! generically" is the unchecked step. Compute n_s for the candidate
entropy forms and see which microstate-counting actually gives ln n -- and which
gives the EXCLUDED cliff.

Map (0742): H_eff(n) ~ chemical potential mu(n) ~ dS/dn; n_s-1 = 2 d ln H_eff/dN,
nbar = nbar_init e^{-3N}, pivot N_rem ~ 57. Need H_eff ~ ln n (any positive coeff;
the tilt p=2 is coefficient-INDEPENDENT since d ln(ln n)/dN = -1/N_rem).
"""

import numpy as np

N_CP, N_GP_INIT = 1e80, 13
N_star = (1.0/3.0)*np.log(N_CP/N_GP_INIT)
Np = N_star - 57.0
nb = (N_CP/N_GP_INIT)*np.exp(-3.0*Np)


def ns_from_H(Hfun):
    eps = max(nb*1e-6, 1.0)
    lnH = lambda x: np.log(abs(Hfun(x)))
    # d ln H/dN = d ln H/d ln n * d ln n/dN, d ln n/dN = -3
    dlnH_dlnn = (lnH(nb+eps)-lnH(nb-eps))/(np.log(nb+eps)-np.log(nb-eps))
    return 1.0 + 2.0*dlnH_dlnn*(-3.0)


def main():
    print("="*78)
    print("STACK-ENTROPY TEST: which microstate count actually gives ln n?")
    print("="*78)
    print(f"  pivot nbar ~ {nb:.1e}; need H_eff ~ ln n for n_s=0.9649.\n")

    # H ~ chemical potential mu ~ dS/dn for each entropy model
    s0 = 1.7  # arbitrary per-CP phase entropy (ln q), value irrelevant to the tilt
    models = [
        ("DISTINGUISHABLE labels  Omega=q^n   S=n*ln q",
         "extensive",  lambda n: s0),                       # dS/dn = ln q = const
        ("INDISTINGUISHABLE ideal gas (fixed V=1 GP)",
         "concentration", lambda n: np.log(n)),             # mu ~ ln(n/V) ~ ln n
        ("orderings counted  Omega=n!  S=ln(n!)",
         "Gibbs/orderings", lambda n: np.log(n)),           # dS/dn = ln n (Stirling)
    ]
    print(f"  {'stack entropy model':>46} | {'H_eff(n)':>13} | {'n_s':>8} | verdict")
    print("  "+"-"*82)
    for label, kind, Hf in models:
        val = ns_from_H(Hf)
        if abs(val-1.0) < 1e-3:
            v = "n_s=1 (CLIFF) -- EXCLUDED"
            heff = "const"
        else:
            v = "*** 0.9649 ***" if abs(val-0.9649)<0.02 else "off"
            heff = "~ ln n"
        print(f"  {label:>46} | {heff:>13} | {val:>8.4f} | {v}")

    print("\n" + "="*78)
    print("THE CATCH (computed, not asserted)")
    print("="*78)
    print("""  Omega ~ n! is NOT generic. The microstate count decides everything, and the
  TWO natural readings split:

   * DISTINGUISHABLE CPs (distinct ZBW phases, as Copilot's mechanism states):
     each CP independently carries one of q phase-states => Omega = q^n =>
     S = n*ln q, EXTENSIVE. Then the chemical potential dS/dn = ln q = CONSTANT
     => H_eff = const => n_s = 1, the Harrison-Zel'dovich CLIFF. EXCLUDED.
     >>> Copilot's stated mechanism (distinguishable phase arrangements) gives the
         CLIFF, not the log. <<<

   * INDISTINGUISHABLE CPs (identical particles, standard Gibbs): the ln n comes
     from the n! DIVISOR in Z = z^n/n! (fixed-volume concentration). mu ~ ln(n/V)
     ~ ln n => H_eff ~ ln n => n_s = 0.9649.

  These are OPPOSITES. The log requires INDISTINGUISHABILITY (the Gibbs n! divisor /
  fixed-volume concentration chemical potential), which is the standard chemical
  potential of an over-concentrated species. Copilot invoked ZBW phase to make the
  CPs DISTINGUISHABLE so there would be microstates to count -- but distinguishable
  labels give the EXTENSIVE entropy and the CLIFF. The ZBW phases are a red herring
  for the log; if anything they push toward the excluded answer.""")

    print("\n" + "="*78)
    print("VERDICT")
    print("="*78)
    print("""  WHAT'S RIGHT (real convergence with 0748): entropy is the ONLY route to the log;
  geometry/placement/packing all give power laws (excluded). Copilot reached this
  correctly.

  WHAT'S RIGHT ABOUT THE LOG: it IS a chemical potential -- specifically the standard
  chemical potential of n IDENTICAL (indistinguishable) CPs over-concentrated in the
  fixed volume of one GP: mu ~ ln(n/V) ~ ln n. That is well-motivated, standard, and
  gives n_s = 0.9649 with the tilt p=2 INDEPENDENT of any coefficient. Good.

  WHAT'S WRONG / MUDDLED: 'Omega ~ n! generically' and 'distinguishable ZBW-phase
  arrangements'. Distinguishable labels give Omega = q^n -> extensive S -> CONSTANT
  chemical potential -> the n_s=1 CLIFF (excluded). The log comes from the OPPOSITE
  (indistinguishability), and does NOT need ZBW phase microstates at all.

  WHAT IT COSTS (the honest structural commitment): getting the indistinguishable-
  concentration chemical potential requires treating a CP stack as a genuine
  thermodynamic ENSEMBLE -- a CPP 'temperature'/statistics at the stack level. CPP's
  primitives are deterministic PCD; whether they support a real stack ensemble (so
  that mu ~ ln(n/V) is legitimate) is the open commitment. If yes -> n_s=0.9649 is
  DERIVED from the standard concentration chemical potential (coefficient-free p=2),
  and the spectrum thread closes. If CPP has no stack thermodynamics -> the log has
  no home and n_s stays favored-but-not-derived.

  STATUS: the entropy route is correct and the log = the standard concentration
  chemical potential of INDISTINGUISHABLE CPs (not distinguishable phases). The sole
  remaining question is now sharp and physical: does a CP stack constitute a
  thermodynamic ensemble in CPP (a temperature / Gibbs statistics), so that mu ~
  ln(n/V) is a real quantity? That -- not a placement rule, not phase labels -- is
  what makes 0.9649 derived or not.""")


if __name__ == "__main__":
    main()
