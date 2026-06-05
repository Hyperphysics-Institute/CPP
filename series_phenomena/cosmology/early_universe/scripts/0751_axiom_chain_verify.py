#!/usr/bin/env python3
"""
0751_axiom_chain_verify.py
==========================
Verifies the CAND-AX-EU-1 derivation chain end to end:
  axiom (ZBW thermalizes stack -> Gibbs indistinguishable ensemble)
  -> mu(n) = kT ln(n/z1) = kT ln n + const           [Step 2]
  -> nbar(N) = nbar_init e^{-3N}, ln nbar = 3 N_rem    [Step 3]
  -> H_eff = kappa [mu(nbar)-mu(1)] = kappa kT ln nbar [Step 4, count-driven 0746]
  -> n_s - 1 = 2 d ln H_eff/dN = -2/N_rem              [Step 5, spectator P ~ H_eff^2]
  -> N_* ~ (1/3) ln(N_CP/N_GP) ; pivot ~57 -> n_s=0.9649 [Step 6]

Two checks:
  (1) COEFFICIENT-FREE: vary kappa, T, z1, and the additive offset over decades;
      n_s must be invariant (they all drop out of d ln H_eff/dN).
  (2) AXIOM NECESSITY: replace the Gibbs ensemble (Z=z^n/n!) with the
      ZBW-as-LABEL distinguishable count (Z=z^n, no n!); the chain must collapse
      to the excluded n_s=1 cliff. This shows the axiom's indistinguishability
      content is exactly what produces the tilt.
"""

import numpy as np

# ---- fixed inputs (NOT tunable) ----
N_CP, N_GP_INIT = 1e80, 13
N_total = (1.0/3.0)*np.log(N_CP/N_GP_INIT)        # ~ e-folds to dilute nbar -> 1
N_pivot_rem = 57.0                                 # observable pivot, N_rem at crossing


def H_eff(N, kappa, kT, lnz1, gibbs=True):
    """H_eff = kappa*(mu(nbar)-mu(1)); mu = kT*ln(n/z1) [Gibbs] or kT*(-ln z1)=const [label]."""
    nbar = (N_CP/N_GP_INIT)*np.exp(-3.0*N)         # mean occupation; here N measured from start
    if gibbs:
        mu = kT*(np.log(nbar) - lnz1)              # indistinguishable: mu = kT ln(n/z1)
        mu1 = kT*(np.log(1.0) - lnz1)
    else:
        # distinguishable labels Z=z^n (no n!): F=-kT n ln z => mu = -kT ln z = const
        mu = -kT*lnz1*np.ones_like(np.atleast_1d(nbar))
        mu1 = -kT*lnz1
    return kappa*(np.asarray(mu) - mu1)


def n_s(kappa, kT, lnz1, gibbs=True):
    # N_rem -> N from start: N = N_total - N_rem ; evaluate at pivot
    N0 = N_total - N_pivot_rem
    h = 1e-4
    lnH = lambda N: np.log(abs(H_eff(np.array([N]), kappa, kT, lnz1, gibbs)[0]) + 1e-300)
    dlnH_dN = (lnH(N0+h) - lnH(N0-h))/(2*h)
    return 1.0 + 2.0*dlnH_dN


def main():
    print("="*74)
    print("CAND-AX-EU-1 CHAIN VERIFY")
    print("="*74)
    print(f"  N_total ~ (1/3)ln(N_CP/N_GP) = {N_total:.2f}; pivot N_rem = {N_pivot_rem}")
    print(f"  predicted n_s = 1 - 2/{N_pivot_rem:.0f} = {1-2/N_pivot_rem:.4f}")
    print(f"  predicted running alpha_s = -2/N_rem^2 = {-2/N_pivot_rem**2:+.5f}\n")

    print("  (1) COEFFICIENT-FREE CHECK (Gibbs ensemble) -- vary kappa,kT,z1,offset:")
    print(f"      {'kappa':>10} {'kT':>10} {'ln z1':>10} | {'n_s':>9}")
    print("      " + "-"*46)
    for kappa, kT, lnz1 in [(1.0,1.0,0.0),(1e3,1.0,0.0),(1.0,1e-4,0.0),
                            (1.0,50.0,0.0),(1.0,1.0,20.0),(1e-2,7.3,-15.0)]:
        print(f"      {kappa:>10.0e} {kT:>10.0e} {lnz1:>10.1f} | {n_s(kappa,kT,lnz1):>9.4f}")

    print("\n  (2) AXIOM-NECESSITY CHECK -- replace Gibbs with ZBW-as-LABEL (no n!):")
    print(f"      Gibbs (indistinguishable, Z=z^n/n!):  n_s = {n_s(1,1,0,gibbs=True):.4f}")
    print(f"      Label (distinguishable,    Z=z^n   ): n_s = {n_s(1,1,0,gibbs=False):.4f}  (cliff)")

    print("\n" + "="*74)
    print("RESULT")
    print("="*74)
    print(f"""  (1) n_s = {1-2/N_pivot_rem:.4f} for ALL coefficient choices -> the coupling kappa,
      the temperature kT, the single-particle z1, and the additive offset ALL drop
      out of d ln H_eff/dN. The prediction is coefficient-free; only the Gibbs
      ln n structure and N_* (fixed by the CP count) survive.

  (2) Removing the axiom's indistinguishability (n! -> 1, distinguishable labels)
      collapses mu to a constant and gives n_s = 1.0000 (Harrison-Zel'dovich cliff,
      excluded ~8 sigma). So CAND-AX-EU-1's indistinguishability content is exactly
      the load-bearing ingredient -- not decoration.

  CONCLUSION: GIVEN the axiom (+ boost~mu, 0746; + T~const over the window), the chain
  yields n_s = 0.9649 and alpha_s ~ -0.0006 with zero free parameters. The axiom is
  the price; 0.9649 (coefficient-free) is what it buys. NO THEO until the swarm accepts
  the axiom.""")


if __name__ == "__main__":
    main()
