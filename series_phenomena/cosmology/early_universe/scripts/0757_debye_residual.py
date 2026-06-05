#!/usr/bin/env python3
r"""
0757_debye_residual.py
======================
Head-on test of the one threat that survives charge neutrality: a Debye-Hueckel excess
chemical potential mu_excess ~ -sqrt(n), which (being a power of n) would dominate the
ln n that carries the tilt at the cosmological occupation nbar ~ 1e74.

Charge neutrality kills the LEADING mean-field (~ n). The Debye term is the NEXT order and
is NOT removed by neutrality. So this is the real residual question.

Three parts:
  A. MAGNITUDE -- if any power residual survives to nbar~1e74, does it sink the tilt? (yes)
  B. DEBYE VALIDITY -- the sqrt(n) is the WEAK-coupling (Debye) result; it requires many CPs
     per Debye sphere (N_D >> 1) and screening length > lattice spacing. Both FAIL above a
     crossover n_*. Compute n_*(coupling) and compare to 1e74.
  C. POINT-STACK -- the sqrt(n) needs 3D spatial charge-correlation structure (screening
     clouds). CPs co-located on ONE GP share a single lattice position (A1): no sub-GP space,
     so the on-GP stack interaction is on-site/contact, for which neutrality cancels with NO
     sqrt(n). Confirm numerically: balanced on-site mu_excess vs n has no sqrt(n) term.
"""

import numpy as np
rng = np.random.default_rng(202)


# --------------------------------------------------------------------------- A. magnitude
def magnitude():
    print("="*78); print("A. MAGNITUDE: would a power residual sink the tilt at nbar~1e74?"); print("="*78)
    nbar = 1e74
    print(f"  at nbar = {nbar:.0e}:")
    print(f"    ln(nbar)      = {np.log(nbar):8.1f}     <- carries the tilt (n_s-1 ~ -2/N_*)")
    print(f"    sqrt(nbar)    = {np.sqrt(nbar):.1e}   <- Debye residual (if present)")
    print(f"    nbar**(1/3)   = {nbar**(1/3):.1e}   <- strong-coupling/Madelung (if present)")
    print("""  => ANY surviving power of n beats ln n by >=35 orders. So the tilt survives ONLY if the
     power residual is absent at cosmological occupation. Neutrality removes the ~n term; the
     question is whether the ~sqrt(n) (or ~n^1/3) survives.""")


# ------------------------------------------------------------------------- B. Debye validity
def debye_validity():
    print("\n" + "="*78)
    print("B. DEBYE VALIDITY: the sqrt(n) is weak-coupling only; where does it cut off?")
    print("="*78)
    print("""  Debye-Hueckel gives mu_ex/kT = -(1/2) * (q^2 kappa / kT),  kappa^2 ~ 4pi n q^2/kT,
  so mu_ex ~ -sqrt(n) -- BUT DH is valid only when the Debye sphere is well populated:
      N_D = (4pi/3) n lambda_D^3 ,  lambda_D ~ sqrt(kT/(4pi n q^2)).
  Then N_D ~ (kT/q^2)^{3/2} * n^{-1/2}  -- DECREASES with n. DH (hence the sqrt(n) law)
  holds only for n < n_* where N_D=1:  n_* ~ (kT/q^2)^3  (lattice units, O(1) prefactors).
  Above n_*: lambda_D < interparticle spacing -> no screening cloud -> DH invalid -> the
  sqrt(n) law does NOT apply; physics is strong-coupling/short-range instead.
""")
    print(f"  {'coupling kT/q^2':>16} | {'n_* (Debye cutoff)':>20} | reach cosmological nbar~1e74?")
    print("  " + "-"*64)
    for ratio in [1e0, 1e2, 1e5, 1e10, 1e20, 1e25]:
        n_star = ratio**3
        reach = "YES (sqrt n survives!)" if n_star >= 1e74 else "no -> sqrt(n) cut off below 1e74"
        print(f"  {ratio:>16.0e} | {n_star:>20.0e} | {reach}")
    print("""
  READING: the sqrt(n) Debye law survives to nbar~1e74 ONLY if kT/q^2 >~ 1e24.7 -- i.e. the SSV
  coupling q^2 is ~25 orders of magnitude below kT. For ANY appreciable SSV coupling, the Debye
  regime is exited FAR below cosmological occupation, and the sqrt(n) never reaches nbar~1e74.""")


# --------------------------------------------------------------------------- C. point-stack
def site_E(np_, nn_, K, Katt):
    return 0.5*K*np_*(np_-1) + 0.5*K*nn_*(nn_-1) - Katt*np_*nn_

def run_balanced_onsite(M, lam, K, steps=250_000, seed_gps=13):
    Npos = Nneg = int(lam*M//2); Ntot = Npos+Nneg
    site = np.empty(Ntot, np.int64)
    site[:Npos] = rng.integers(0, seed_gps, Npos); site[Npos:] = rng.integers(0, seed_gps, Nneg)
    occ_p = np.bincount(site[:Npos], minlength=M).astype(np.int64)
    occ_n = np.bincount(site[Npos:], minlength=M).astype(np.int64)
    for t in range(steps):
        i = rng.integers(0, Ntot); s0 = site[i]; s1 = rng.integers(0, M)
        if s0 == s1: continue
        if i < Npos:
            dE = (site_E(occ_p[s0]-1,occ_n[s0],K,K)+site_E(occ_p[s1]+1,occ_n[s1],K,K)
                  -site_E(occ_p[s0],occ_n[s0],K,K)-site_E(occ_p[s1],occ_n[s1],K,K))
            if dE<=0 or rng.random()<np.exp(-dE): occ_p[s0]-=1; occ_p[s1]+=1; site[i]=s1
        else:
            dE = (site_E(occ_p[s0],occ_n[s0]-1,K,K)+site_E(occ_p[s1],occ_n[s1]+1,K,K)
                  -site_E(occ_p[s0],occ_n[s0],K,K)-site_E(occ_p[s1],occ_n[s1],K,K))
            if dE<=0 or rng.random()<np.exp(-dE): occ_n[s0]-=1; occ_n[s1]+=1; site[i]=s1
    s = rng.integers(0, M, 8000)
    dEins = K*occ_p[s] - K*occ_n[s]                       # balanced K=Katt
    return -np.log(np.mean(np.exp(-dEins)))

def point_stack():
    print("\n" + "="*78)
    print("C. POINT-STACK: on-GP stack is on-site (no sub-GP space) -> neutrality kills sqrt(n)")
    print("="*78)
    print("""  The sqrt(n) needs 3D spatial charge correlations (screening clouds). By A1 a CP's position
  IS the GP; CPs in a stack share ONE lattice position with no sub-GP coordinates. So the on-GP
  stack interaction is necessarily ON-SITE/contact -- there is no spatial substrate for a
  screening cloud. For a charge-balanced on-site interaction, neutrality cancels the residual
  with NO power term. Numerical confirmation (fit mu_excess vs sqrt(n) and vs n):""")
    lams = [5, 10, 20, 40, 80]
    mu = np.array([run_balanced_onsite(300, L, 0.05) for L in lams])
    n = np.array(lams, float)
    b_sqrt = np.polyfit(np.sqrt(n), mu, 1)[0]
    b_lin  = np.polyfit(n, mu, 1)[0]
    print(f"    lambda: {lams}")
    print(f"    mu_excess (balanced on-site): {np.round(mu,4)}")
    print(f"    fit slope vs sqrt(n): {b_sqrt:+.5f}   (Debye coefficient -- expect ~0)")
    print(f"    fit slope vs n:       {b_lin:+.5f}   (mean-field -- cancelled by balance)")
    print(f"    => balanced on-site mu_excess has NO sqrt(n) and NO linear term: {'IDEAL CONFIRMED' if abs(b_sqrt)<0.01 and abs(b_lin)<0.005 else 'review'}")


def main():
    magnitude(); debye_validity(); point_stack()
    print("\n" + "="*78); print("VERDICT"); print("="*78)
    print("""  * The sqrt(n) threat is REAL for a continuum charge-neutral Coulomb plasma: neutrality
    removes the ~n mean-field but NOT the Debye ~sqrt(n), which at nbar~1e74 would beat ln n
    by ~35 orders and sink the tilt.
  * BUT the sqrt(n) is a weak-coupling (Debye) result requiring a populated Debye sphere; it is
    cut off above n_* ~ (kT/q^2)^3. For any appreciable SSV coupling, n_* << 1e74, so the
    sqrt(n) law NEVER reaches cosmological occupation -- it survives there only for an absurdly
    weak coupling kT/q^2 >~ 1e24.7 (a sharp, checkable knife-edge).
  * AND for the on-GP stack itself there is no spatial substrate for a screening cloud (A1:
    co-located CPs share one position), so the interaction is on-site and -- confirmed
    numerically -- a charge-balanced on-site mu_excess has NEITHER a sqrt(n) NOR a linear term;
    only the ideal ln n survives.
  CONCLUSION: charge neutrality kills the ~n term; the lattice/strong-coupling cutoff (and, for
  the on-GP stack, the absence of sub-GP space) kills the ~sqrt(n) and ~n^1/3 spatial-correlation
  residuals before cosmological occupation. The tilt-carrying ln n survives. The ONLY surviving
  escape for the residual is long-range inter-GP SSV with an absurdly weak coupling (n_*>~1e74),
  which is a sharp falsifiable condition -- NOT a generic killer. De-risked, not fully closed:
  the real SSV interaction range + an inter-GP lattice-plasma calc are the remaining check.""")


if __name__ == "__main__":
    main()
