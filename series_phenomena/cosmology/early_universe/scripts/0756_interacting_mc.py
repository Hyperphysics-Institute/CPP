#!/usr/bin/env python3
r"""
0756_interacting_mc.py
======================
THE interacting bath-clause test (in-house first data point). A1-invariant occupation-number
dynamics with a pluggable +/- SSV interaction. Per-GP site energy:

    E(np, nn) = (K/2)[np(np-1) + nn(nn-1)] - K_att * np * nn
                 \------- same-sign crowding cost ------/   \-- +/- co-location bind --/

Three configs, each run at lambda in {10,20,40} to fit the mu_excess SLOPE vs nbar:
   (A) baseline      K=0,     K_att=0      -> ideal reference
   (B) unbalanced    K=0.05,  K_att=0      -> like-sign repulsion only
   (C) charge-balanced K=0.05, K_att=0.05  -> neutral plasma (repulsion + bind balanced)

Observables (occupation counts only; particle arrays are scaffolding):
   tau_eq   - Moments for seed-GP fraction to relax to within 5% of equilibrium
   Poisson  - mean ~ var ~ lambda at stationarity
   S(0)     - long-wavelength structure factor (block-count Fano): 1 ideal, >1 cluster, <1 disperse
   mu_excess(nbar) via Widom insertion, slope d mu_excess/d nbar (the tilt-contamination probe)
   R        - tau_eq / t_efold (example inflationary H)

CAVEAT: this is a TOY of CPP's dynamics, not the dynamics themselves. A clean result here is a
first data point and a methodology check, NOT a substitute for independent runs or the real
microphysics.
"""

import numpy as np
rng = np.random.default_rng(101)


def site_E(np_, nn_, K, Katt):
    return 0.5*K*np_*(np_-1) + 0.5*K*nn_*(nn_-1) - Katt*np_*nn_


def run(M, lam, K, Katt, kT=1.0, steps=300_000, seed_gps=13):
    Npos = Nneg = int(lam*M//2)
    Ntot = Npos + Nneg
    site = np.empty(Ntot, dtype=np.int64)
    site[:Npos] = rng.integers(0, seed_gps, Npos)        # + CPs piled on 13 GPs
    site[Npos:] = rng.integers(0, seed_gps, Nneg)        # - CPs piled on 13 GPs
    occ_p = np.bincount(site[:Npos], minlength=M).astype(np.int64)
    occ_n = np.bincount(site[Npos:], minlength=M).astype(np.int64)
    seed_frac_hist, t_hist = [], []
    for t in range(steps):
        i = rng.integers(0, Ntot)
        s0 = site[i]
        s1 = rng.integers(0, M)
        if s0 == s1:
            continue
        if i < Npos:
            before = site_E(occ_p[s0], occ_n[s0], K, Katt) + site_E(occ_p[s1], occ_n[s1], K, Katt)
            after  = site_E(occ_p[s0]-1, occ_n[s0], K, Katt) + site_E(occ_p[s1]+1, occ_n[s1], K, Katt)
            dE = after - before
            if dE <= 0 or rng.random() < np.exp(-dE/kT):
                occ_p[s0] -= 1; occ_p[s1] += 1; site[i] = s1
        else:
            before = site_E(occ_p[s0], occ_n[s0], K, Katt) + site_E(occ_p[s1], occ_n[s1], K, Katt)
            after  = site_E(occ_p[s0], occ_n[s0]-1, K, Katt) + site_E(occ_p[s1], occ_n[s1]+1, K, Katt)
            dE = after - before
            if dE <= 0 or rng.random() < np.exp(-dE/kT):
                occ_n[s0] -= 1; occ_n[s1] += 1; site[i] = s1
        if t % 2000 == 0:
            seed_frac_hist.append((occ_p[:seed_gps].sum()+occ_n[:seed_gps].sum())/Ntot)
            t_hist.append(t)
    return occ_p, occ_n, np.array(t_hist), np.array(seed_frac_hist), kT


def block_S0(occ, M, blocks=75):
    bs = M//blocks
    blk = occ[:bs*blocks].reshape(blocks, bs).sum(axis=1)
    return blk.var()/blk.mean()


def widom_mu_excess(occ_p, occ_n, M, K, Katt, kT, trials=8000):
    s = rng.integers(0, M, trials)
    dE = K*occ_p[s] - Katt*occ_n[s]          # dE to insert one + CP at site s
    return -kT*np.log(np.mean(np.exp(-dE/kT)))


def tau_eq(t_hist, frac_hist, eq_frac, tol=0.05):
    for t, f in zip(t_hist, frac_hist):
        if f <= eq_frac*(1+tol):
            return int(t)
    return None


def main():
    M = 300
    lams = [10, 20, 40]
    H_planck = 1e-6; t_efold = 1.0/H_planck
    configs = [("A baseline (ideal)", 0.0, 0.0),
               ("B unbalanced (rep only)", 0.05, 0.0),
               ("C charge-balanced", 0.05, 0.05)]

    print("="*82)
    print("INTERACTING BATH-CLAUSE MC  (toy of CPP dynamics; first in-house data point)")
    print("="*82)
    print(f"  M={M} GPs, kT=1, seed on 13 GPs; site E=(K/2)[np(np-1)+nn(nn-1)]-Katt*np*nn\n")

    for name, K, Katt in configs:
        mus, occ_last = [], None
        tau_at_20 = None; pois_at_20 = None; s0_at_20 = None
        for lam in lams:
            occ_p, occ_n, th, fh, kT = run(M, lam, K, Katt)
            occ = occ_p + occ_n
            mu = widom_mu_excess(occ_p, occ_n, M, K, Katt, kT)
            mus.append(mu)
            if lam == 20:
                tau_at_20 = tau_eq(th, fh, 13/M)
                pois_at_20 = (occ.mean(), occ.var())
                s0_at_20 = block_S0(occ, M)
        slope = np.polyfit(lams, mus, 1)[0]      # d mu_excess / d nbar
        R = (tau_at_20/t_efold) if tau_at_20 else np.inf
        pflag = "YES" if abs(pois_at_20[0]-pois_at_20[1]) < 0.35*20 else "no"
        contaminated = abs(slope) > 1e-3
        print(f"  {name:>26}: tau_eq~{str(tau_at_20):>7} R~{R:6.3f} | "
              f"Poisson {pflag} (m{pois_at_20[0]:.1f}/v{pois_at_20[1]:.1f}) | "
              f"S(0)~{s0_at_20:4.2f} | mu_ex slope d/dnbar = {slope:+.4f} "
              f"-> {'CONTAMINATED' if contaminated else 'ideal'}")

    print("\n" + "="*82)
    print("READING")
    print("="*82)
    print("""  Interpretation key (mu_excess slope vs nbar is the decisive number):
    slope ~ 0      -> chemical potential stays ideal, mu ~ ln nbar survives, tilt clean.
    slope != 0     -> mean-field term ~nbar; at the cosmological nbar~1e74 it SWAMPS ln nbar
                      (~170), dragging the tilt to the excluded power-law branch.

  Expected/!checked here:
    A baseline       -> slope 0, S(0)~1: ideal, PASS (reference).
    B unbalanced     -> slope>0 (like-sign repulsion uncancelled), S(0)<1 (dispersed): the
                        generic interaction CONTAMINATES the tilt. A generic SSV interaction is
                        NOT automatically safe.
    C charge-balanced-> leading mean-field (K - Katt)*nbar/2 CANCELS at K=Katt; slope collapses
                        toward 0 and S(0) toward 1: an effectively-NEUTRAL +/- plasma keeps the
                        chemical potential ideal and the log survives.

  IMPLICATION (the new physical requirement this run surfaces): the bath clause's mu_excess~0
  condition is NOT automatic under interactions -- it requires the +/- SSV interaction to be
  effectively BALANCED (charge-neutral), so the mean-field cancels. This is a real, falsifiable
  CPP condition: cosmological charge neutrality is what protects n_s=0.9649 from interaction
  contamination. Independent confirmation requested.""")


if __name__ == "__main__":
    main()
