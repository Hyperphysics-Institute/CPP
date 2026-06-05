# Reasoning capture — Patch 0753: minimal-PCD Monte Carlo spec (bath-clause test)

*Session 154. Specifies the MC that would establish/falsify HALF 1 (the bath) of CAND-AX-EU-1.
Writeup: `.../development/macrocp_mc_spec.md`. Reference skeleton: `.../scripts/0753_macrocp_mc_reference.py`
(baseline PASSES). NO THEO. Thomas confirmed: no imprinted per-CP history; full history in the SSV
hologram (occupation field) -- the spec is built on exactly that.*

## What the MC tests (and the discipline that keeps it honest)
- Tests HALF 1 ONLY (the bath: stack reaches Gibbs equilibrium << e-fold, A1-invariant, no
  tilt-contaminating interaction). Does NOT test the log (= A1 occupation-number counting, guaranteed,
  not measured).
- A1 DISCIPLINE: physical state = per-GP occupation counts n+,n- only; no per-CP labels/histories.
  Particle->site arrays are scaffolding; every observable goes through bincount (counts), never indices.
  This is what makes the measured statistics the indistinguishable (Gibbs) ones and forecloses the 0749/
  0752 distinguishable-label cliff.

## Minimal rule set (all four phenomena from ONE occupation-dependent hop)
macro-CP = high-occupation GP (emergent); inter-GP hop with Metropolis weight exp(-dE/kT), dE from a
pluggable ssv_energy(n+,n-,site); +/- splitting emerges if ssv_energy makes same-sign crowding costly and
+/- co-location favourable; evaporation/re-stacking = occupation-dependent drain of over-full GPs.
Initial condition = all CPs piled on the 13-GP cohort (violent early state).

## Observables + pass/fail
(i) tau_eq (seed-GP fraction relaxes to within 5% of 13/M).
(ii) stationary occupation = Poisson (mean~var~lambda) -- Gibbs signature.
(iii) mu_excess(nbar) via Widom insertion; ideal part kT ln(nbar/z1) NOT measured (A1-guaranteed); test is
      whether interactions add a term ~nbar (would contaminate the tilt -> excluded branch).
(iv) R = tau_eq/t_efold, t_efold=1/H from the H-engine. PASS needs R<<1 (target <=0.1, >=10
     re-thermalizations/e-fold).
PASS = R<<1 + Poisson + mu_excess no ~nbar term, WITH interactions on. FAIL = R>~1 (no thermalization) /
non-Poisson (clustering) / mu_excess~nbar (interaction-contaminated tilt).

## The subtle failure mode I made explicit
Even with PERFECT thermalization, a mean-field SSV interaction can make mu_excess ~ nbar, which adds a
linear term to H_eff and contaminates the tilt toward the excluded 0746 mechanical column. So 'thermalizes
fast' is necessary but NOT sufficient; the interactions must also leave the chemical potential effectively
ideal. Widom insertion is the clean probe for this.

## Reference skeleton (baseline, runs)
ssv_energy=0, M=200, 4000 +/- CPs, lambda=20, seed 13 GPs: seed fraction 1.000->0.072 (eq 0.065), tau_eq
~28k Moments, mean 20.00 var 20.5 (Poisson YES), mu_excess~0, R~0.028 (H=1e-6) -> baseline PASS. Baseline
shows methodology + ideal reference; swarm's real test = switch ssv_energy on.

## Honesty calibration
- Scoped strictly to HALF 1; repeated that a PASS is 'MC establishes bath; A1 carries log; 0746 carries
  coupling', NOT 'MC derives n_s'.
- Surfaced the mean-field contamination failure mode (thermalization necessary, not sufficient).
- Named the real risk plainly (R>~1) and called it worth risking.
- Built the whole state on no-per-CP-history (Thomas's confirmed postulate); A1-invariance enforced via
  counts-only observables.

## Pointer
- Swarm runs interacting version (ssv_energy on), reports (i)-(iv)+verdict. PASS -> register dissolution
  (n_s zero-new-axiom); FAIL -> 0751 working-postulate path stands. Clear of chirality.
  PCD = Perceive/Compute/Displace.
