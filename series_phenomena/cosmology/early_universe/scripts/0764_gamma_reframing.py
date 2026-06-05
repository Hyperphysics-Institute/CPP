#!/usr/bin/env python3
r"""
0764_gamma_reframing.py
=======================
Determines what the CPP SSV kernel (Coulomb, from the DP-Sea polarization model: F_rep ~ k_e q0^2/r^2)
implies for the long-range residual -- and surfaces that the "B*sqrt(n) ~ 1e37" scare is a PHANTOM.

Key identity. For a Coulomb plasma the Debye-Hueckel excess chemical potential is
    mu_excess/kT = -c * Gamma^{3/2}        (c = O(1); OCP limiting law c = 1/sqrt(3))
where Gamma = q^2/(a kT) is the plasma coupling at the inter-particle spacing a = n^{-1/3}.
Writing a = n^{-1/3} turns this into the "sqrt(n)" form:
    mu_excess/kT = -c (q^2/kT)^{3/2} sqrt(n)   ->  B := c (q^2/kT)^{3/2},  so  B*sqrt(n) = c Gamma^{3/2}.

THEREFORE B*sqrt(n) IS just c*Gamma^{3/2}. Within the DH regime of validity (Gamma <~ 1) it is <~ O(1) --
it can NEVER reach ln nbar ~ 170. The "1e37" comes from holding q^2/kT fixed at an O(1) value and
multiplying by sqrt(1e74)=1e37 -- but at that n, Gamma = (q^2/kT) n^{1/3} ~ 1e24, which is DEEP strong
coupling where the DH formula (and hence B) does not apply. The threat was an extrapolation of a
weak-coupling law into the strong-coupling regime.

This script makes that quantitative and identifies the ONLY genuine residual concern (strong coupling).
"""

import numpy as np

c_DH = 1.0/np.sqrt(3)          # OCP DH limiting-law coefficient (order 1)
ln_nbar = 170.0                # ln(1e74) ~ 170, the tilt-chain logarithm (3*N_rem)


def mu_over_kT_DH(Gamma):
    """DH limiting law (valid Gamma <~ 1): |mu_excess|/kT = c * Gamma^{3/2}."""
    return c_DH * Gamma**1.5


def mu_over_kT_strong(Gamma):
    """Strong-coupling neutral-plasma (Madelung-like) magnitude ~ |a_M| * Gamma, a_M ~ 0.9 (OCP)."""
    return 0.9 * Gamma


def main():
    print("="*86)
    print("SSV kernel = Coulomb (DP-Sea model).  Residual governed by plasma coupling Gamma, not sqrt(n).")
    print("="*86)
    print(f"  Identity:  B*sqrt(nbar)  ==  |mu_excess|/kT  ==  c*Gamma^{{3/2}}   (c = 1/sqrt(3) = {c_DH:.3f})")
    print(f"  Threat condition (dimensionless):  |mu_excess|/kT  >~  ln nbar ~ {ln_nbar:.0f}\n")

    print(f"  {'Gamma':>10} | {'regime':>14} | {'|mu_ex|/kT = B*sqrt(n)':>24} | vs ln nbar~170")
    print("  " + "-"*74)
    for G in [1e-3, 1e-2, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 44.0, 1e2, 1e24]:
        if G <= 1.0:
            mu = mu_over_kT_DH(G); regime = "weak (DH ok)"
        else:
            mu = mu_over_kT_strong(G); regime = "strong (DH X)"
        verdict = "<< 170  PASS" if mu < 0.1*ln_nbar else ("~170 threshold" if mu < 3*ln_nbar else ">> 170  FAIL")
        print(f"  {G:>10.0e} | {regime:>14} | {mu:>24.4e} | {verdict}")

    print("\n" + "="*86)
    print("THE PHANTOM")
    print("="*86)
    # The naive scare: take B at an O(1) value of q^2/kT, multiply by sqrt(1e74).
    q2_over_kT = 1.0
    B_naive = c_DH * q2_over_kT**1.5
    nbar = 1e74
    Bsqrtn_naive = B_naive*np.sqrt(nbar)
    Gamma_at_that_point = q2_over_kT * nbar**(1/3)
    print(f"""  Naive: take q^2/kT = {q2_over_kT} (O(1)) -> B = c*(q^2/kT)^3/2 = {B_naive:.3f};
         B*sqrt(1e74) = {Bsqrtn_naive:.2e}  (the '1e37' scare).
  BUT at nbar=1e74 with q^2/kT={q2_over_kT}, Gamma = (q^2/kT)*nbar^(1/3) = {Gamma_at_that_point:.2e}
         -> deep STRONG coupling; the DH formula used to define B is INVALID there.
  Within the DH regime of validity (Gamma <~ 1), B*sqrt(n) = c*Gamma^3/2 <~ {mu_over_kT_DH(1.0):.2f} -- it
  NEVER reaches 170. The sqrt(n) Debye residual cannot threaten the tilt; the scare was extrapolating a
  weak-coupling law into strong coupling.""")

    print("\n" + "="*86)
    print("WHERE THE REAL (DIFFERENT) THREAT LIVES, AND WHY CPP PASSES")
    print("="*86)
    Gamma_threat_DH = (ln_nbar/c_DH)**(2/3)
    Gamma_threat_strong = ln_nbar/0.9
    print(f"""  The residual reaches ln nbar~170 only at:
    - DH form:     Gamma ~ (170/c)^(2/3) = {Gamma_threat_DH:.0f}  (already outside DH validity)
    - strong form: Gamma ~ 170/0.9      = {Gamma_threat_strong:.0f}
  Either way the ONLY genuine threat is a STRONGLY-coupled plasma, Gamma ~ tens-to-hundreds -- a
  correlation energy of tens-hundreds of kT per CP. That is NOT the sqrt(n) Debye effect (different
  functional form, n^{{1/3}} Madelung), and it is suppressed further by charge neutrality (0756).

  CPP early CP plasma: a HOT, RELATIVISTIC charged plasma has kT ~ hbar c / a, so
    Gamma = q^2/(a kT) ~ (e^2/4pi eps0)/(hbar c) = alpha ~ 1/137 ~ 0.0073  (WEAK coupling).
  Then |mu_excess|/kT ~ c*alpha^{{3/2}} ~ {c_DH*(1/137.0)**1.5:.2e}  <<  170  -- PASS with ~5 orders of margin.
  Plus: on-GP stacking is a CONTACT interaction (A1: no sub-GP space) -> no sqrt(n) at all (0757);
  and charge neutrality cancels the leading mean-field (0756).""")

    print("\n" + "="*86)
    print("VERDICT (analytic, pending panel + Stage A/B numerical confirmation)")
    print("="*86)
    print(f"""  Kernel: Coulomb 1/r (DP-Sea polarization model). SOLID from corpus.
  The dimensionless residual is c*Gamma^{{3/2}} (weak) up to ~Gamma (strong); the sqrt(n) threat is a
  phantom of extrapolating DH into strong coupling. CPP's early plasma is weakly coupled (Gamma~alpha),
  giving |mu_excess|/kT ~ 1e-3 << ln nbar. The corner is very likely CLOSED on the PASS side; recommend
  the panel confirm via Stage A (reproduce DH) + Stage B (crossover n_* = the Gamma=1 line) and check
  that |mu_excess|/kT stays << ln nbar across the relevant Gamma -- which this identity guarantees.""")


if __name__ == "__main__":
    main()
