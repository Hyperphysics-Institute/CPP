#!/usr/bin/env python3
r"""
0766_ns_epoch_gamma.py
======================
Pins the n_s-epoch plasma coupling Gamma using the scales the CPP corpus actually grounds, and
CORRECTS a scale error in 0765.

Grounded from corpus (master_glossary):
  * Grid-Point spacing a = l_P (the Planck length): "The spacing between Grid Points is the Planck length".
  * PSR = l_P per Absolute Moment (rest frame): a CP displaces ~l_P each Absolute Moment at speed c
    -> Absolute Moment = l_P/c = t_P (Planck time) -> the substrate energy quantum is
       hbar c / a = hbar c / l_P = hbar / t_P = E_Pl  (Planck energy ~ 1.22e19 GeV).
  So ChatGPT's condition kT ~ hbar c/a becomes, in CPP-native terms, kT ~ E_Pl.

Coupling: Gamma = (Coulomb energy at spacing a)/(kT) = [alpha * hbar c / a]/kT = alpha * E_Pl / kT
        = alpha / kappa,  with  kappa := kT_bath / E_Pl  (bath temperature in Planck units).

CORRECTION to 0765: 0765 anchored q^2/a at the COMPTON spacing (q^2/a ~ alpha*m_e c^2 ~ 3.7 keV,
giving a "fail below ~84 eV" threshold). The corpus-grounded inter-CP spacing is the GP/Planck scale
l_P, not the Compton scale -- so q^2/a ~ alpha*E_Pl ~ 1e17 GeV and the threshold is ~1e15 GeV. The
STRUCTURE (Gamma = alpha/kappa, PASS for weak coupling) is unchanged; the anchor scale was wrong.
"""

import numpy as np

alpha = 1/137.036
E_Pl_GeV = 1.22e19
c_DH = 1/np.sqrt(3)
ln_nbar = 170.0

def mu_kT(G):
    return c_DH*G**1.5 if G <= 1 else 0.9*G

def main():
    print("="*86)
    print("n_s-epoch Gamma from GROUNDED scales: a = l_P, hbar c/a = E_Pl  ->  Gamma = alpha/kappa")
    print("="*86)
    print(f"  alpha = {alpha:.5f}, E_Pl = {E_Pl_GeV:.2e} GeV, kappa = kT_bath/E_Pl.")
    G_fail = (ln_nbar/c_DH)**(2/3)
    kT_fail = alpha/G_fail*E_Pl_GeV
    print(f"  Weak-coupling PASS needs Gamma <~ {G_fail:.0f}  ->  kappa >~ {alpha/G_fail:.1e}"
          f"  ->  kT_bath >~ {kT_fail:.1e} GeV.\n")

    print(f"  {'reading of the n_s-epoch bath':>40} | {'kT_bath':>12} | {'kappa':>9} | {'Gamma':>9} | {'|mu|/kT':>9} | verdict")
    print("  " + "-"*104)
    rows = [
        ("ZBW/substrate bath ~ E_Pl (bath-clause)", E_Pl_GeV,        ),
        ("near-substrate (kT ~ 0.01 E_Pl)",         1e-2*E_Pl_GeV,   ),
        ("PASS/FAIL threshold",                     kT_fail,         ),
        ("macroscopic inflation T_dS ~ 1e13 GeV",   1e13,            ),
        ("radiation era kT ~ 1 GeV",                1.0,             ),
    ]
    for label, kT in rows:
        kappa = kT/E_Pl_GeV
        G = alpha/kappa
        mu = mu_kT(G)
        verdict = "PASS" if mu < 0.1*ln_nbar else ("~threshold" if mu < 3*ln_nbar else "FAIL (weak-coupling form)")
        print(f"  {label:>40} | {kT:>9.1e} GeV | {kappa:>9.1e} | {G:>9.1e} | {mu:>9.1e} | {verdict}")

    print("\n" + "="*86)
    print("HONEST ASSESSMENT (epoch-pinning deepens, not fully closes)")
    print("="*86)
    print(f"""  GROUNDED: a = l_P and hbar c/a = E_Pl (c-edge-Absolute-Moment locking). So Gamma = alpha/kappa,
  and the whole question is the n_s-epoch bath temperature in Planck units, kappa.

  Reading A -- the bath is the ZBW/substrate dynamics (this is what the 0750 bath clause identifies as
  the bath). The ZBW operates at the substrate clock (~ c/l_P), so kT ~ E_Pl, kappa ~ 1, Gamma ~ alpha
  ~ {alpha:.3f}  ->  |mu|/kT ~ {c_DH*alpha**1.5:.1e} << 170. PASS, with ~{np.log10(1/(alpha/G_fail)):.0f} orders of margin in kappa.

  Reading B -- the relevant bath is a much colder MACROSCOPIC temperature (e.g. inflationary de Sitter
  T_dS ~ 1e13 GeV). Then kappa ~ 1e-6, Gamma ~ 1e3-1e4 (STRONG coupling). The naive weak-coupling form
  would FAIL -- BUT two CPP-specific features can still rescue it:
    (i)  STACKING geometry: if the relevant spacing is the FIXED GP spacing l_P (not a continuum
         a = n^-1/3), then Gamma is n-INDEPENDENT, so mu_ex/kT is a constant offset that does NOT tilt
         (the tilt is d/d ln n). The sqrt(n)/Debye tilt-contamination assumed a continuum a = n^-1/3.
    (ii) NEUTRALITY (0756): for a charge-neutral plasma the strong-coupling Madelung energy is a
         near-constant offset, again largely non-tilting.
  Neither (i) nor (ii) is established here; both are plausible and would need their own analysis.

  NET: the corpus grounds a = l_P and hbar c/a = E_Pl; the bath-clause reading (A) gives Gamma ~ alpha
  -> PASS; the conservative macroscopic reading (B) needs the stacking-geometry or neutrality-Madelung
  argument to also PASS. This is a CONDITIONAL PASS. The remaining CPP-specific inputs are: (1) the
  n_s-epoch bath temperature kappa (cosmology arc), and (2) whether the relevant geometry is fixed-GP
  (Gamma n-independent, non-tilting) or continuum. Both are well-posed and tractable next steps.

  CORRECTION owned: 0765's "fail below ~84 eV / 4-orders margin" used the COMPTON spacing for q^2/a;
  the corpus-grounded spacing is the GP/Planck scale l_P, giving a threshold ~1e15 GeV. The structure
  (Gamma = alpha/kappa, PASS in the weak/substrate-bath reading) is unchanged.""")

if __name__ == "__main__":
    main()
