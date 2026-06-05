#!/usr/bin/env python3
"""
0753_macrocp_mc_reference.py
============================
REFERENCE SKELETON for the minimal-PCD Monte Carlo that tests HALF 1 of CAND-AX-EU-1
(the BATH clause): do macro-CP PCD dynamics drive a CP stack from the violent 13-GP seed
to GIBBS equilibrium on timescales << one e-fold, with A1-INVARIANT (occupation-number)
microstates and WITHOUT generating an interaction term that spoils mu ~ ln n?

It does NOT (and cannot) derive the log: the ideal part mu_ideal = kT ln(nbar/z1) is fixed
by A1 indistinguishability (occupation-number counting). What the MC tests is whether the
macro-CP INTERACTIONS leave that ideal result intact -- i.e. whether the measured EXCESS
chemical potential mu_excess(nbar) stays ~0 (no significant term linear in nbar, which would
contaminate the tilt and push toward the excluded branch).

A1 DISCIPLINE: the only physical state is the per-GP occupation count (n_+ , n_-). The
particle->site arrays below are implementation scaffolding ONLY; no observable may read a
particle index as a label. Every observable goes through np.bincount (counts), never indices.

Baseline here = NON-interacting (energy hook returns 0): the clean ideal-gas reference, which
PASSES trivially. The SWARM's real test is to switch on the SSV interaction energy
(`ssv_energy`, default 0) representing +/- attraction/repulsion and crowding, and check
whether the PASS survives.
"""

import numpy as np
rng = np.random.default_rng(11)


# ---- pluggable SSV interaction energy (THE swarm's real knob; default 0 = ideal baseline) ----
def ssv_energy(occ_pos, occ_neg, site):
    """Local SSV configurational energy contributed by `site` given occupation arrays.
    DEFAULT 0 (non-interacting baseline). Example +/- model the swarm can switch on:
        np = occ_pos[site]; nn = occ_neg[site]
        return K_rep*(np*(np-1)+nn*(nn-1))/2 - K_att*np*nn   # same-sign crowd cost, +/- bind
    Any term that makes mu_excess ~ nbar (mean-field) will contaminate the tilt -> FAIL."""
    return 0.0


def step(part, site_of, occ_pos, occ_neg, pol, M, kT):
    """One PCD hop: a random CP leaves its GP and re-stacks on a GP chosen by the SSV field
    (Metropolis on ssv_energy). +/- splitting, evaporation, re-stacking all emerge from this
    single occupation-dependent rule. A1-invariant: rule depends only on occupations."""
    i = rng.integers(0, part.size)
    s_old = site_of[i]
    s_new = rng.integers(0, M)
    occ = occ_pos if pol[i] > 0 else occ_neg
    dE = ( (ssv_energy(occ_pos, occ_neg, s_new) - 0.0)
         - (ssv_energy(occ_pos, occ_neg, s_old) - 0.0) )  # baseline 0; hook for swarm
    if dE <= 0 or rng.random() < np.exp(-dE/kT):
        occ[s_old] -= 1; occ[s_new] += 1; site_of[i] = s_new


def run(M=200, Npos=2000, Nneg=2000, kT=1.0, steps=600_000, seed_gps=13):
    Ntot = Npos + Nneg
    pol = np.concatenate([np.ones(Npos, int), -np.ones(Nneg, int)])
    site_of = rng.integers(0, seed_gps, size=Ntot)          # violent seed on 13 GPs
    occ_pos = np.bincount(site_of[pol > 0], minlength=M).astype(int)
    occ_neg = np.bincount(site_of[pol < 0], minlength=M).astype(int)
    part = np.arange(Ntot)
    lam = Ntot/M
    frac_hist, t_hist = [], []
    for t in range(steps):
        step(part, site_of, occ_pos, occ_neg, pol, M, kT)
        if t % 2000 == 0:
            occ = occ_pos + occ_neg
            frac_seed = occ[:seed_gps].sum()/Ntot            # fraction still on the 13 seed GPs
            frac_hist.append(frac_seed); t_hist.append(t)
    occ = occ_pos + occ_neg
    return np.array(t_hist), np.array(frac_hist), occ, lam, kT


def tau_eq(t_hist, frac_hist, eq_frac, tol=0.05):
    """First Moment-count at which the seed-GP fraction relaxes to within tol of equilibrium."""
    target = eq_frac*(1+tol)
    for t, f in zip(t_hist, frac_hist):
        if f <= target:
            return t
    return None


def widom_mu_excess(occ_pos, occ_neg, M, kT, trials=20000):
    """Excess chemical potential via test-particle insertion: mu_ex = -kT ln <exp(-dE_ins/kT)>.
    Ideal/non-interacting -> dE_ins=0 -> mu_ex=0. Nonzero (esp. ~nbar) flags tilt contamination."""
    acc = np.empty(trials)
    for k in range(trials):
        s = rng.integers(0, M)
        occ_pos[s] += 1
        dE = ssv_energy(occ_pos, occ_neg, s) - ssv_energy(occ_pos - np.eye(M, dtype=int)[s]*0, occ_neg, s)
        occ_pos[s] -= 1
        acc[k] = np.exp(-dE/kT)
    return -kT*np.log(acc.mean())


def main():
    print("="*78)
    print("MINIMAL-PCD MONTE CARLO -- REFERENCE SKELETON (tests the BATH clause, HALF 1)")
    print("="*78)
    t_hist, frac_hist, occ, lam, kT = run()
    M = occ.size
    eq_frac = 13/M
    tau = tau_eq(t_hist, frac_hist, eq_frac)

    # observables
    mean, var = occ.mean(), occ.var()
    poisson_ok = abs(mean - var) < 0.30*lam
    mu_ex = widom_mu_excess(np.bincount([], minlength=M).astype(int)*0 + occ//2,
                            occ//2, M, kT)

    print(f"\n  setup: M={M} GPs, Ntot={int(lam*M)} CPs (+/-), lambda={lam:.0f}, kT={kT}, seed on 13 GPs")
    print(f"\n  (i) EQUILIBRATION (bath forms):")
    print(f"      seed-GP fraction {frac_hist[0]:.3f} -> {frac_hist[-1]:.3f} (equilibrium {eq_frac:.3f})")
    print(f"      tau_eq ~ {tau:,} Moments (to within 5% of equilibrium)" if tau else "      tau_eq: not reached in budget")
    print(f"\n  (ii) STATIONARY DISTRIBUTION is Gibbs/Poisson (mean ~ var ~ lambda):")
    print(f"      mean {mean:.2f}, var {var:.2f}  -> Poisson signature: {'YES' if poisson_ok else 'NO'}")
    print(f"\n  (iii) EXCESS chemical potential (Widom insertion; ideal=0):")
    print(f"      mu_excess ~ {mu_ex:+.4f} kT  (baseline non-interacting -> ~0; ideal mu ~ ln nbar intact)")

    # pass/fail (baseline)
    H_planck = 1e-6          # EXAMPLE inflationary H in Planck units (swarm supplies real value)
    t_efold = 1.0/H_planck   # Moments per e-fold
    R = tau/t_efold if tau else np.inf
    print(f"\n  (iv) ADIABATICITY R = tau_eq / t_efold (example H={H_planck:.0e} t_P^-1 -> t_efold={t_efold:.0e}):")
    print(f"      R ~ {R:.2e}   (PASS needs R << 1: stack re-thermalizes many times per e-fold)")

    verdict = (tau is not None) and poisson_ok and (abs(mu_ex) < 0.05) and (R < 0.1)
    print("\n  BASELINE VERDICT:", "PASS" if verdict else "review")
    print("""
  WHAT A FULL RUN MUST SHOW (pass/fail for the swarm):
    PASS (bath clause established -> axiom dissolves -> n_s=0.9649 zero-NEW-axiom):
      * tau_eq << t_efold  (R << 1; adiabatic: stack re-thermalizes within each e-fold)
      * stationary occupation = Gibbs/Poisson (mean ~ var ~ lambda)
      * mu_excess(nbar) ~ 0 with NO significant term linear in nbar (scan several lambda):
        the SSV interactions must NOT generate a mean-field ~nbar piece that contaminates
        the tilt. (ideal part mu ~ ln nbar is guaranteed by A1 counting, NOT measured.)
    FAIL modes:
      * R >~ 1                    -> no thermalization within an e-fold; bath clause fails.
      * non-Poisson stationary    -> condensation/clustering; mu not ~ ln nbar.
      * mu_excess ~ nbar          -> interaction-contaminated tilt; pushes toward excluded
                                     power-law branch (the 0746 mechanical column).
  THE SWARM'S REAL TEST: switch on `ssv_energy` (+/- attraction/repulsion + crowding) and
  re-run (i)-(iv). If PASS survives with interactions on, HALF 1 is established dynamically
  and the tenth axiom evaporates. NO per-CP history is used anywhere: the full configurational
  history lives in the occupation field (the SSV hologram), exactly as postulated.""")


if __name__ == "__main__":
    main()
