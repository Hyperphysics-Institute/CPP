#!/usr/bin/env python3
"""
0745_depth_based_boost.py
=========================
Tests the depth-based H-boost (Thomas + Copilot): deeper stacks push harder, so
the per-tick fractional PSR boost is h(n), a function of stack depth n, not an
on/off switch. The hope: the relaxation physics hands back a logarithmic h(n) ~
ln(n), which gives p=2 / n_s=0.9649. Run HONESTLY -- derive what each physical
relaxation picture gives, do NOT assume the log because it lands on p=2.

Framework (from 0744): H_eff(N) = h(nbar(N)), and
    n_s - 1 = 2 d ln H_eff/dN,   nbar(N) = nbar_init e^{-3N},   N_rem = (1/3) ln nbar.

Candidate depth-laws h(n), each from a DIFFERENT physical picture of what drives
the boost. The point is to see which physical picture the data select -- and
whether that picture is motivated or reverse-engineered.

  (a) FRACTION / on-off:      h = const            (any superposition, same boost)
  (b) MECHANICAL, linear:     h ~ n                (each stacked CP adds equal push)
  (c) MECHANICAL, pairwise:   h ~ n^2              (pairwise repulsion ~ n(n-1)/2)
  (d) SCREENED / surface:     h ~ n^(2/3)          (only the stack's surface pushes)
  (e) ENTROPIC / chemical-mu: h ~ ln(n)            (dispersal drive = chem. potential
                                                    of an over-concentrated species,
                                                    mu = mu0 + kT ln c -- STANDARD)
  (f) tuned weak power:       h ~ n^q, q=0.0055    (what a power law would NEED)
"""

import numpy as np

NS_PLANCK, NS_ERR = 0.9649, 0.0042
N_CP, N_GP_INIT = 1e80, 13
N_star = (1.0 / 3.0) * np.log(N_CP / N_GP_INIT)


def nbar(N):
    return (N_CP / N_GP_INIT) * np.exp(-3.0 * N)


def ns_for(h_of_n, N):
    eps = 1e-4
    lnH = lambda x: np.log(h_of_n(nbar(x)))
    return 1.0 + 2.0 * (lnH(N + eps) - lnH(N - eps)) / (2 * eps)


def main():
    print("=" * 78)
    print("DEPTH-BASED H-BOOST: which relaxation law does the substrate need?")
    print("=" * 78)
    Np = N_star - 57.0      # observable pivot: N_rem ~ 57 (early crossing)
    print(f"  N_* = {N_star:.1f} (CP count); pivot N_rem = {N_star-Np:.0f}; "
          f"Planck n_s = {NS_PLANCK} +- {NS_ERR}\n")

    laws = [
        ("(a) FRACTION / on-off      h=const",  lambda n: 1.0,
         "any superposition = same boost (the literal axiom)"),
        ("(b) MECHANICAL linear      h~n",      lambda n: float(n),
         "each stacked CP adds equal push"),
        ("(c) MECHANICAL pairwise    h~n^2",    lambda n: float(n) ** 2,
         "pairwise repulsion ~ n(n-1)/2"),
        ("(d) SCREENED / surface     h~n^2/3",  lambda n: float(n) ** (2.0/3.0),
         "only the stack surface pushes"),
        ("(e) ENTROPIC / chem-pot    h~ln n",   lambda n: np.log(max(float(n), 1+1e-9)),
         "dispersal drive mu=mu0+kT ln c (STANDARD stat-mech)"),
        ("(f) tuned weak power       h~n^0.0055", lambda n: float(n) ** 0.0055,
         "what a power law would NEED (fine-tuned)"),
    ]
    print(f"  {'physical picture':>34} | {'n_s':>9} | assessment")
    print("  " + "-" * 74)
    for label, h, note in laws:
        ns = float(ns_for(h, Np))
        if abs(ns - 1.0) < 1e-6:
            a = "n_s=1 HZ -- EXCLUDED"
        elif ns < 0.5:
            a = f"ABSURD (n_s={ns:.1f}) -- wildly EXCLUDED"
        elif abs(ns - NS_PLANCK) < 3 * NS_ERR:
            a = "*** MATCHES Planck ***"
        else:
            a = "off"
        print(f"  {label:>34} | {ns:>9.4f} | {a}")
        print(f"  {'':>34} |           | ({note})")

    print("\n" + "=" * 78)
    print("WHAT THE DATA SELECT")
    print("=" * 78)
    print("""  Among depth-based laws, near-scale-invariance (n_s ~ 1) is a SEVERE filter:
    - mechanical laws (h~n, n^2, n^2/3) give n_s = -5, -11, -3 -- ABSURD, wildly
      excluded. 'Deeper pushes harder' in any POWER-LAW form is ruled out hard.
    - the on/off (fraction) law gives n_s=1 (HZ), excluded.
    - ONLY h ~ ln(n) gives a sensible near-scale-invariant spectrum, and it lands
      on n_s = 1 - 2/N_* = 0.9649 -- Planck on the nose (p=2).
    - a tuned power n^0.0055 also hits 0.965, but the exponent is fine-tuned and
      gives the wrong (constant, not 1/N) running; the log is the natural q->0
      limit and gives the correct small running.

  So the requirement of near-scale-invariance UNIQUELY selects the logarithmic
  depth-law among the physical candidates.""")

    print("\n" + "=" * 78)
    print("IS THE LOG MOTIVATED, OR REVERSE-ENGINEERED?  (the honest question)")
    print("=" * 78)
    print("""  The log is NOT the naive 'deeper pushes harder' -- that is mechanical/power
  (h~n, n^2), which is ABSURDLY excluded here. The log is specifically the
  ENTROPIC / chemical-potential form: the drive to disperse an over-concentrated
  species is mu = mu0 + kT ln(c), logarithmic in concentration -- STANDARD
  statistical mechanics. Thomas's physical story is literally 'the lattice
  relaxing extreme over-occupation toward the 1-CP-per-GP equilibrium' -- i.e. a
  DISPERSAL process, whose drive is the entropic chemical potential ~ ln(n).

  So IF the H-boost is the ENTROPIC dispersal pressure (not a mechanical
  repulsion), then h ~ ln(n) is the natural, standard form -- NOT a tuning -- and
  p=2 / n_s=0.9649 is a CONSEQUENCE. This is favored two ways: (i) physical
  naturalness (chemical potential of dispersal), and (ii) it is the ONLY depth-law
  consistent with near-scale-invariance.

  HONEST STATUS: this is now CONSISTENT-AND-FAVORED, not yet DERIVED. The owed
  step is a PCD-level derivation that the over-occupation relaxation is entropic
  (chemical-potential, ~ln n) rather than mechanical (~n^q). Mechanical -> absurd;
  entropic -> 0.9649. The physical story ('dispersal toward equilibrium') and the
  data (near-scale-invariance) both point to entropic. If a PCD derivation
  confirms the entropic ln(n), then with N_* fixed by the CP count, n_s = 0.9649
  becomes a ZERO-PARAMETER CPP prediction.""")


if __name__ == "__main__":
    main()
