#!/usr/bin/env python3
"""
0747_microrule_audit.py
=======================
Audit of the swarm's (Thomas + Copilot) proposed count-driven H-micro-rules.
The CONCEPTUAL framing is right (0746): drive PSR_base by occupation COUNT,
decoupled from the gravity SSV_abs. The claim is that the proposed local rules
"coarse-grain to ln(n)" and hence give n_s = 0.9649. THIS SCRIPT CHECKS THAT
CLAIM by computing n_s for each rule as written. Run honestly.

Framework (0746): per-tick multiplicative boost PSR_base *= (1 + H(n)); the
expansion rate is H(n), and n_s - 1 = 2 d ln H(nbar)/dN, nbar = nbar_init e^{-3N},
pivot N_rem ~ 57. We need H(n) ~ ln(n) for n_s = 0.9649.

Proposed rules:
  R1  Thomas: "2 CPs -> PSR_base doubled" / boost prop. to over-occupation count
      => H(n) ~ n
  R2  Copilot flux: hop P(i->j) ~ 1/(n_j+eps); gross outward tendency ~ n CPs each
      trying to hop  => H(n) ~ n   (and =0 for a UNIFORM stack: flux needs a gradient)
  R3  Copilot "Pi/n": H(n) ~ (n - 1)/n           (claimed "ln n in disguise")
  R4  harmonic / chemical-potential: k-th stacked CP contributes 1/k (screened)
      => H(n) ~ sum_{k=1..n} 1/k = H_n ~ ln n + gamma   (this is what ln n REQUIRES)
  R5  reference: H(n) ~ ln n directly
"""

import numpy as np

N_CP, N_GP_INIT = 1e80, 13
N_star = (1.0/3.0)*np.log(N_CP/N_GP_INIT)
Np = N_star - 57.0


def nbar(N):
    return (N_CP/N_GP_INIT)*np.exp(-3.0*N)


def ns(Hfun, N):
    eps = 1e-4
    lnH = lambda x: np.log(Hfun(nbar(x)))
    return 1.0 + 2.0*(lnH(N+eps)-lnH(N-eps))/(2*eps)


def harmonic(n):
    # H_n = ln n + gamma + 1/(2n) - ...  (asymptotic; exact-enough for huge n)
    g = 0.5772156649
    n = float(n)
    return np.log(n) + g + 1.0/(2*n)


def main():
    print("="*78)
    print("AUDIT: do the proposed count-driven micro-rules actually give ln(n)?")
    print("="*78)
    print(f"  pivot nbar ~ {nbar(Np):.1e} (N_rem={np.log(nbar(Np))/3:.0f}); "
          f"target n_s = 0.9649. Need H(n) ~ ln n.\n")

    rules = [
        ("R1  Thomas 'doubles per CP'  H~n",          lambda n: float(n)),
        ("R2  Copilot flux (gross)     H~n",          lambda n: float(n)),
        ("R3  Copilot 'Pi/n'           H~(n-1)/n",    lambda n: (float(n)-1)/float(n)),
        ("R4  harmonic/chem-pot        H~sum 1/k",    harmonic),
        ("R5  reference                H~ln n",       lambda n: np.log(max(float(n),1+1e-9))),
    ]
    print(f"  {'proposed rule':>36} | {'n_s':>9} | verdict")
    print("  "+"-"*74)
    for label, H in rules:
        val = float(ns(H, Np))
        if abs(val-0.9649) < 0.02:
            v = "*** gives 0.965 ***"
        elif abs(val-1.0) < 1e-3:
            v = "n_s=1 (HZ cliff) -- EXCLUDED"
        elif val < 0.5:
            v = f"n_s={val:.1f} -- EXCLUDED (mechanical)"
        else:
            v = "off"
        print(f"  {label:>36} | {val:>9.4f} | {v}")

    print("\n" + "="*78)
    print("WHAT THIS SHOWS")
    print("="*78)
    print("""  The conceptual framing (count-driven PSR_base, decoupled from gravity SSV) is
  RIGHT. But the SPECIFIC rules proposed do NOT give ln(n):

    R1 Thomas 'PSR_base doubles per CP' (boost ~ over-occupation count n):
       H ~ n -> n_s = -5. EXCLUDED. (Copilot correctly flagged this one.)

    R2 Copilot flux (P ~ 1/n_j): the GROSS outward tendency ~ n -> n_s = -5,
       EXCLUDED. And worse, the NET flux needs a concentration GRADIENT, so for a
       ~UNIFORM over-dense early patch the net flux ~ 0 -> NO expansion at all.
       Dispersal-flux cannot drive uniform expansion.

    R3 Copilot 'Pi/n' = (n-1)/n: this SATURATES to a constant (~1) for large n,
       so H ~ const -> n_s = 1.000 (Harrison-Zel'dovich CLIFF), EXCLUDED. It is
       NOT 'ln n in disguise' -- it is the on/off cliff in disguise. (n-1)/n -> 1,
       whereas d(ln n)/dn = 1/n -> 0; opposite behaviors.

  Only R4/R5 give 0.9649 -- and NEITHER is among the proposed rules. R5 is just
  'H ~ ln n' asserted. R4 is the one mechanism that PRODUCES ln n from a local
  rule: the k-th stacked CP contributes 1/k (a diminishing/screened contribution),
  so the total is the harmonic sum H_n = sum 1/k ~ ln n.""")

    print("\n" + "="*78)
    print("THE INTERNAL INCONSISTENCY IN THE PROPOSAL (the key point)")
    print("="*78)
    print("""  The proposal asserts BOTH:
     (a) each CP contributes ONE unit of over-occupation potential => potential = n
         ('n increments of SSV'), AND
     (b) the boost H ~ ln(n).
  These are INCOMPATIBLE if the boost is proportional to the potential: potential = n
  and H ~ potential => H ~ n (linear) => n_s = -5, EXCLUDED. You cannot have a
  linear potential AND a log boost UNLESS the boost couples to the CHEMICAL
  POTENTIAL mu(n) = dF/dn ~ ln(n) -- the per-CP entropy derivative -- rather than to
  the raw count. 'Boost ~ count' is linear (excluded); 'boost ~ chemical potential
  of the count' is log (0.965). The proposal conflates these.

  SO THE ln(n) IS STILL NOT DERIVED. To get it you need, specifically:
     H(n)  ~  mu(n)  =  d/dn [ configurational free energy of n CPs on a GP ]  ~ ln n
  equivalently, diminishing per-CP contributions (k-th CP adds ~1/k, harmonic sum).
  None of the proposed micro-rules implement this; 'boost ~ over-occupation count'
  (Thomas's and R1/R2) is linear and excluded; 'Pi/n' (R3) is a saturating cliff.

  HONEST STATUS: architecture right, ln(n)-producing micro-rule NOT yet in hand. The
  real remaining task: a CPP-native reason the per-CP boost DIMINISHES as 1/k (e.g.
  screening of buried CPs in a stack), which is what turns the count into ln(count).
  Until that, n_s = 0.9649 stays 'viable & favored' (0746), not 'derived'.""")


if __name__ == "__main__":
    main()
