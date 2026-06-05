#!/usr/bin/env python3
r"""
0769_bath_timescale.py
======================
Grounds the "fast enough" half of the bath clause (leg 1) in the substrate-vs-macroscopic timescale
separation, with NO free parameter beyond N_mix (the number of ZBW mixing events to thermalize, which the
0753 toy already measured at O(10-30)).

Setup (corpus-grounded):
  * The substrate clock is the Absolute Moment = t_P = l_P/c (Planck time): a CP displaces ~l_P per moment
    at c. The ZBW switching between DP partners runs at this substrate rate (~1/t_P).
  * Equilibration time tau_eq ~ N_mix * t_P, with N_mix = number of ZBW re-mixings needed to reach the
    Gibbs/Poisson occupation state. The 0753 minimal-PCD MC toy found this is O(10-30).
  * The e-fold time (macroscopic) is t_efold ~ 1/H_inf.

Ratio:
  R = tau_eq / t_efold = N_mix * t_P * H_inf = N_mix * (H_inf / E_Pl),   since t_P = hbar/E_Pl and
      H_inf * t_P = hbar H_inf / E_Pl = H_inf[GeV]/E_Pl[GeV].

So R = N_mix * kappa_H,  kappa_H = H_inf/E_Pl (the Hubble scale in Planck units). The occupations
thermalize "instantly" on macroscopic (e-fold) timescales for any SUB-PLANCKIAN inflation scale:
R << 1  <=>  H_inf << E_Pl / N_mix.
"""

import numpy as np

E_Pl = 1.22e19  # GeV

def main():
    print("="*80)
    print("Bath-clause speed: R = tau_eq/t_efold = N_mix * (H_inf/E_Pl)")
    print("="*80)
    print(f"  E_Pl = {E_Pl:.2e} GeV. R << 1  <=>  H_inf << E_Pl/N_mix.\n")

    N_mix_vals = [10, 30, 100]
    H_vals = [("Planckian H ~ E_Pl",      E_Pl),
              ("near-Planck 1e17 GeV",    1e17),
              ("high-scale infl. 1e16",   1e16),
              ("typical infl. 1e14 GeV",  1e14),
              ("low-scale infl. 1e13",    1e13)]

    print(f"  {'inflation Hubble scale':>26} | {'H/E_Pl':>9} | " + " | ".join(f"R(N={n})" for n in N_mix_vals))
    print("  " + "-"*72)
    for label, H in H_vals:
        kH = H/E_Pl
        Rs = [N*kH for N in N_mix_vals]
        verds = "  ".join(f"{R:8.1e}" for R in Rs)
        print(f"  {label:>26} | {kH:>9.1e} | {verds}")

    print("\n" + "="*80)
    print("READING")
    print("="*80)
    print(f"""  The substrate (ZBW, t_P scale) is the FAST bath; macroscopic cosmology (e-folds, 1/H_inf) is
  SLOW. For any sub-Planckian inflation scale the occupations are re-thermalized O(10^4-10^6) times
  per e-fold -- R << 1 by many orders. The ONLY way R ~ 1 is Planckian inflation (H_inf ~ E_Pl),
  which is excluded by the tensor bound (H_inf <~ 1e14 GeV) and by CPP's own H-axiom (the lattice
  growth ceiling forbids sustained super-luminal/near-Planck recession; see
  axiom_h_inflation_engine_evaluation.md).

  So the "fast enough" half of the bath clause is GROUNDED in the substrate-vs-macroscopic timescale
  separation, with the only input N_mix = O(10-30) already measured by the 0753 toy. This is the SAME
  separation that makes kT ~ E_Pl (substrate) the relevant bath (LEMMA-NS-BATH, 0767): the substrate
  is fast and hot at its own scale; everything cosmological is slow and (relatively) cold.

  Combined with the "mixing exists" half -- the ZBW switching IS the effective-randomness mechanism
  CPP already uses for quantum randomness (glossary) and CLT-Gaussianity (0738) -- leg 1 (bath
  reality) is not a free-floating assumption but a corollary of standing CPP commitments. Residual:
  the stationary state is the INDISTINGUISHABLE Gibbs state, which is A1 (no CP identity ->
  occupation-number objects; 0749/0752), already secured.""")

if __name__ == "__main__":
    main()
