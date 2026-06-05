#!/usr/bin/env python3
r"""
0765_gamma_estimate.py
======================
Acts on ChatGPT's calibration: do NOT say the sqrt(n) residual is "impossible"; say it is
COUPLING-BOUNDED -- harmless in the weakly-coupled regime, dangerous only if strongly coupled --
and the load-bearing CPP-specific input is Gamma << 1 (equivalently kT ~ hbar c / a, the
relativistic thermal scale). This script quantifies the margin and makes the conditionality explicit.

Single control parameter: the plasma coupling Gamma = q^2/(a kT) (Coulomb-to-thermal energy ratio).
   weak (Gamma <~ 1):   |mu_excess|/kT = c Gamma^{3/2}      (Debye-Hueckel, c = 1/sqrt(3))
   strong (Gamma >~ 1): |mu_excess|/kT ~ |a_M| Gamma        (neutral-Madelung, |a_M| ~ 0.9 OCP)
Tilt threat: |mu_excess|/kT >~ ln nbar ~ 170.
"""

import numpy as np
c_DH = 1.0/np.sqrt(3)
ln_nbar = 170.0
alpha = 1/137.036


def mu_kT(Gamma):
    return c_DH*Gamma**1.5 if Gamma <= 1 else 0.9*Gamma


def main():
    print("="*84)
    print("Gamma is the single control. CPP-specific question: is the early CP plasma weakly coupled?")
    print("="*84)

    # Threat thresholds
    G_threat_weak = (ln_nbar/c_DH)**(2/3)
    G_threat_strong = ln_nbar/0.9
    print(f"  Tilt fails only if |mu_excess|/kT >~ ln nbar ~ {ln_nbar:.0f}, i.e. Gamma >~ {G_threat_weak:.0f}"
          f" (DH form) / {G_threat_strong:.0f} (Madelung).")
    print(f"  Relativistic hot-plasma expectation: kT ~ hbar c/a  ->  Gamma ~ alpha ~ {alpha:.4f}.\n")

    print(f"  {'plasma regime':>34} | {'Gamma':>10} | {'|mu_ex|/kT':>11} | margin to fail")
    print("  " + "-"*82)
    rows = [
        ("inflationary / ultra-hot (kT>>>EM)", 1e-10),
        ("hot relativistic (kT ~ hbar c/a)",   alpha),
        ("mildly relativistic",                0.1),
        ("moderate (Gamma~1)",                 1.0),
        ("strongly coupled",                   10.0),
        ("FAIL threshold (DH form)",           G_threat_weak),
        ("cold dense crystal (e.g. WD)",       175.0),
    ]
    for label, G in rows:
        mu = mu_kT(G)
        if mu < 0.1*ln_nbar:
            verdict = f"PASS ({ln_nbar/max(mu,1e-30):.0e}x)"
        elif mu < 3*ln_nbar:
            verdict = "~threshold"
        else:
            verdict = "FAIL"
        print(f"  {label:>34} | {G:>10.2e} | {mu:>11.2e} | {verdict}")

    print("\n" + "="*84)
    print("MARGIN IN TEMPERATURE (anchoring the EM coupling energy q^2/a at the corpus SSV scale)")
    print("="*84)
    # Coulomb energy at inter-CP spacing ~ EM scale. Anchor: alpha * (electron rest scale).
    # q^2/a ~ alpha * m_e c^2 ~ alpha * 0.511 MeV ~ 3.7 keV  (Coulomb energy at the Compton/CP scale).
    q2_over_a_keV = alpha*511.0   # keV
    print(f"  EM Coulomb energy at the CP/Compton spacing:  q^2/a ~ alpha*m_e c^2 ~ {q2_over_a_keV:.1f} keV")
    print(f"  Then Gamma = (q^2/a)/kT.  FAIL needs Gamma >~ {G_threat_weak:.0f}  ->  kT <~ (q^2/a)/{G_threat_weak:.0f}"
          f" ~ {q2_over_a_keV/G_threat_weak*1000:.0f} eV.")
    print(f"""
  So the plasma would have to be COLDER than ~{q2_over_a_keV/G_threat_weak*1000:.0f} eV to threaten the tilt -- a cold,
  recombination-era-or-below temperature, the OPPOSITE of the hot epoch that sets n_s. Any
  tilt-setting epoch with kT >~ keV-MeV gives Gamma << 1 and |mu_excess|/kT << 170 by many orders.""")

    print("\n" + "="*84)
    print("HONEST CONDITIONALITY (ChatGPT's calibration)")
    print("="*84)
    print(f"""  NOT: 'the sqrt(n) residual is impossible.'
  INSTEAD: the Debye sqrt(n) residual is bounded by the coupling Gamma; it is harmless in the
  weakly-coupled relativistic regime (Gamma ~ alpha -> |mu|/kT ~ {c_DH*alpha**1.5:.1e} << 170) and would
  threaten the tilt only if the early CP plasma were STRONGLY coupled (Gamma >~ tens) -- i.e. cold/dense,
  not hot. The load-bearing CPP-specific input is therefore Gamma << 1, equivalently kT ~ hbar c/a (the
  relativistic thermal scale).
   * Robust part (corpus + standard physics): kernel = Coulomb; identity B*sqrt(n)=c Gamma^{{3/2}};
     residual coupling-bounded; only threat = strong coupling.
   * Conditional part (the one input): the early CP plasma is weakly coupled. CPP support: the
     tilt-setting epoch is hot (kT >~ keV-MeV >> the EM coupling scale q^2/a ~ keV at the CP spacing),
     so Gamma << 1 with ~4+ orders of temperature margin. This is the standard hot-early-universe
     expectation, NOT a tuning -- but the precise Gamma depends on the relevant inter-CP spacing and the
     ZBW/thermal scale, which the CPP cosmology side should pin to make the PASS unconditional.
   * To FAIL, CPP would have to put the n_s-setting CP plasma in a cold, strongly-coupled (Gamma >~ tens)
     state -- contrary to a hot early universe. Considered unlikely, but it is the falsifiable hinge.""")


if __name__ == "__main__":
    main()
