#!/usr/bin/env python3
r"""
0770_neutrality_dp_pairs.py
===========================
Grounds leg 2 (charge-neutral effective equation of state) in the DP-pair structure of the substrate.

Corpus (master_glossary):
  * DP (Dipole Pair) = "a bound pair of opposite-polarity CPs (+ and -)"; "a DP is electrically and
    colour-neutral."
  * DP Sea = "all lattice sites occupied by DPs in their ground state" -- the vacuum.

So the substrate / early CP plasma is built ENTIRELY from bound +/- pairs. The occupation that drives the
tilt is a stack of DPs (or, equivalently, of CPs in +/- balance). Therefore:
  * n_+ = n_- exactly at every occupation n (each added unit is a neutral +/- pair),
  * net charge Q(n) = 0 identically,
  * the mean-field Coulomb term (proportional to Q^2) vanishes at every n -> this is exactly the 0756
    "balanced +-, K = K_att" IDEAL case, for which mu_excess is flat (no tilt contamination).

The only n-dependent piece left is the LOCAL Poisson charge fluctuation ~ sqrt(n) per Grid Point, which is
the long-range Debye residual -- already closed PASS in the sqrt(n) thread (0764-0768): bounded by
c*Gamma^{3/2} with Gamma ~ alpha at the substrate bath.
"""

import numpy as np

def main():
    print("="*78)
    print("Leg 2: DP-pair construction forces exact +- balance -> net charge 0 at all n")
    print("="*78)
    print(f"  {'n (CPs)':>9} | {'n_+':>7} | {'n_-':>7} | {'net Q':>6} | {'mean-field (∝Q^2)':>17} | {'local Poisson ~sqrt(n)':>22}")
    print("  " + "-"*82)
    rng = np.random.default_rng(0)
    for n in [10, 100, 1000, 10000, 100000]:
        n_dp = n//2
        n_plus, n_minus = n_dp, n_dp          # each DP contributes one + and one -
        Q = n_plus - n_minus                   # identically zero by construction
        meanfield = Q**2                       # proportional to net charge squared
        # local per-GP fluctuation if charges were placed at random (Poisson): std ~ sqrt(n_per_GP)
        local = np.sqrt(n_dp)                  # the screened/closed sqrt(n) residual scale
        print(f"  {n:>9} | {n_plus:>7} | {n_minus:>7} | {Q:>6} | {meanfield:>17} | {local:>22.1f}")

    print("\n" + "="*78)
    print("READING")
    print("="*78)
    print("""  Global +- balance is EXACT by the DP-pair construction (each DP = one + and one -), so the net
  charge is identically zero at every occupation n and the mean-field Coulomb term vanishes for all n.
  That is precisely the 0756 balanced/ideal case: mu_excess flat, no tilt contamination. Neutrality is
  therefore not an assumption tailored to the n_s result -- it is the +/- pair structure of the DP Sea
  vacuum (glossary), the same structure that makes the vacuum electrically neutral everywhere in CPP.

  The only n-dependent residual is the LOCAL Poisson fluctuation ~ sqrt(n) per Grid Point -- the
  long-range Debye term -- already closed PASS (0764-0768): bounded by c*Gamma^{3/2}, Gamma ~ alpha at
  the substrate bath. So leg 2 (neutrality) is grounded, and it does not reopen the (closed) sqrt(n) leg.

  Caveat (owned): a tiny global charge/matter asymmetry (~1e-9, the baryon-asymmetry scale; Capotauro
  leptogenesis) breaks exact balance at the 1e-9 level -- utterly negligible for the 0756 mean-field
  cancellation, which needs only |imbalance| << 1, not exactly 0.""")

if __name__ == "__main__":
    main()
