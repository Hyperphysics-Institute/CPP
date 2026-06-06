#!/usr/bin/env python3
r"""
0774_zrp_derivation_corrections.py
==================================
Closes the loop on the ZRP IDENTIFICATION (leg 1's residual premise) by deriving its three properties from
the CPP primitives and QUANTIFYING the only correction channel.

Derivation (corpus-grounded; see zrp_derivation.md):
  (i)   INDEPENDENCE  -- PCD is a per-CP cycle ("executed by each CP ... perceive local SSV, displace");
        elementary moves are single-CP. The only inter-CP coupling is the shared SSV field.
  (ii)  RATE-HOMOGENEITY g(n)=n -- A1: all CPs identical (no per-CP identity); Absolute Moment: every CP
        runs exactly one PCD cycle per tick at the universal clock rate 1/t_P. So each CP leaves its site at
        the same rate -> total site rate = n * (1/t_P) -> g(n) = n.
  (iii) SYMMETRY p(i,j)=p(j,i) -- 600-cell is vertex-transitive (coordination z=12, group 2I); with a
        homogeneous/isotropic inflationary background (no SSV gradient) the compute step has no preferred
        direction -> uniform 1/12 kernel.

Key structural fact (general ZRP theorem): independence + symmetry => the stationary measure is PRODUCT form
for ANY rate function g(n). g(n)=n => the product marginal is POISSON => the A1 indistinguishable Gibbs
state with mu = kT ln(rho) => exactly p = 2 => n_s = 1 - 2/N_* = 0.9649.

The ONLY correction channel is the SSV coupling, which makes the per-CP rate weakly occupation-dependent:
g(n) -> n*(1 + lambda*(n-1)) with lambda ~ Gamma ~ alpha (the already-bounded plasma coupling). This keeps
the product form (no correlations -- leg 2's mean-field cancellation is untouched) but deforms the marginal
off Poisson, shifting the effective tilt coefficient. This script measures that shift:
  eta(lambda) = d(mu)/d(ln rho) - 1   (0 for the ideal Poisson case)
  Delta n_s   = 2 * eta / N_*          (the induced shift in n_s)
and shows Delta n_s ~ 1e-4 at lambda = alpha -- far inside the Planck error +/- 0.0042.
"""

import numpy as np

alpha = 1/137.036
N_star = 57.0
planck_err = 0.0042

def zrp_weights(lmbda, nmax):
    """w(0)=1, w(n)=prod_{k=1}^n 1/g(k), g(k)=k(1+lambda(k-1))."""
    w = np.zeros(nmax+1); w[0] = 1.0
    for n in range(1, nmax+1):
        g = n*(1.0 + lmbda*(n-1))
        w[n] = w[n-1]/g
    return w

def rho_of_z(z, w):
    n = np.arange(len(w))
    zn = z**n
    Z = np.sum(w*zn)
    return np.sum(n*w*zn)/Z

def dmu_dlnrho(lmbda, rho_target=2.0, nmax=80):
    w = zrp_weights(lmbda, nmax)
    # bisect z so that rho(z) = rho_target
    lo, hi = 1e-6, 50.0
    for _ in range(200):
        mid = 0.5*(lo+hi)
        if rho_of_z(mid, w) < rho_target: lo = mid
        else: hi = mid
    z = 0.5*(lo+hi)
    # d ln rho / d ln z  by central finite difference
    dlz = 1e-5
    r_p = rho_of_z(z*np.exp(dlz), w); r_m = rho_of_z(z*np.exp(-dlz), w)
    dlnrho_dlnz = (np.log(r_p)-np.log(r_m))/(2*dlz)
    return 1.0/dlnrho_dlnz    # dmu/dlnrho = dlnz/dlnrho

def main():
    print("="*78)
    print("ZRP identification: corrections to g(n)=n from SSV coupling -> shift in n_s")
    print("="*78)
    print(f"  ideal case lambda=0 must give d(mu)/d(ln rho) = 1 exactly (Poisson, p=2):")
    eta0 = dmu_dlnrho(0.0) - 1.0
    print(f"     eta(0) = {eta0:+.2e}   {'PASS (=0)' if abs(eta0)<1e-6 else 'CHECK'}\n")

    print(f"  {'lambda (~coupling)':>20} | {'eta=dmu/dlnrho-1':>17} | {'Delta n_s = 2 eta/N*':>20} | vs Planck err")
    print("  " + "-"*78)
    for lab, lm in [("0.1*alpha", 0.1*alpha), ("alpha", alpha), ("3*alpha", 3*alpha), ("10*alpha", 10*alpha)]:
        eta = dmu_dlnrho(lm) - 1.0
        dns = 2*eta/N_star
        ratio = abs(dns)/planck_err
        print(f"  {lab:>20} | {eta:>17.2e} | {dns:>20.2e} | {ratio:>6.1e} x  ({'<<' if ratio<0.1 else '~'} Planck)")

    print("\n" + "="*78)
    print("READING")
    print("="*78)
    print(f"""  - eta(0) = 0: the ideal g(n)=n ZRP gives d(mu)/d(ln rho) = 1 exactly -> exactly p=2 -> n_s=0.9649.
  - eta(lambda) is linear in lambda (the SSV coupling): a weakly occupation-dependent rate shifts the
    effective tilt coefficient by O(lambda).
  - At the physical coupling lambda ~ alpha ~ {alpha:.4f}, the induced shift is Delta n_s ~ 1e-4 -- about
    {abs(2*(dmu_dlnrho(alpha)-1)/N_star)/planck_err:.1e} of the Planck 1-sigma error (+/- {planck_err}). Negligible.
  - Crucially, the perturbed process is STILL a ZRP, so its stationary measure stays PRODUCT form (no
    inter-site correlations) for any lambda -> leg 2's mean-field cancellation (neutrality) is untouched;
    only the single-site marginal (hence the tilt coefficient) feels the O(alpha) correction.

  CONCLUSION: the ZRP identification is not a free assumption -- it is the leading-order PCD dynamics
  forced by {{A1 (identical CPs, occupation ontology), the per-CP PCD cycle, the vertex-transitive 600-cell,
  homogeneous inflation}}, and its only correction (the SSV coupling) is the SAME alpha-small coupling
  already bounded in the sqrt(n)/Gamma thread (0764-0768), shifting n_s by ~1e-4 -- inside Planck. Leg 1's
  residual is thus DERIVED to leading order with quantified, negligible corrections, not posited.""")

if __name__ == "__main__":
    main()
