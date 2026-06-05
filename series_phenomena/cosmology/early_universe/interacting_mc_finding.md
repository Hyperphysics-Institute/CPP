# Interacting bath-clause MC — result, and the charge-neutrality requirement it surfaces

*Patch 0756, Session 154. First in-house run of the interacting bath-clause Monte Carlo (the real test,
with ± SSV interactions switched on). Script:
`series_phenomena/cosmology/early_universe/scripts/0756_interacting_mc.py`. NO THEO. **A toy of CPP's
dynamics, not the dynamics themselves — a first data point and a methodology check, awaiting independent
confirmation.***

## What was run

A1-invariant occupation-number dynamics (counts only), seeded on the 13-GP cohort, with per-GP site
energy E(n₊,n₋) = (K/2)[n₊(n₊−1)+n₋(n₋−1)] − K_att·n₊·n₋ (same-sign crowding cost; ± co-location bind).
Three configs, each at λ ∈ {10,20,40} to fit the μ_excess slope vs n̄, measuring all five observables
(τ_eq, Poisson, S(0), μ_excess slope, R).

## Result

| config | τ_eq | R | Poisson (mean/var) | S(0) | dμ_excess/dn̄ | verdict |
|---|---|---|---|---|---|---|
| A baseline (ideal) | 38k | 0.038 | YES (20.0/20.1) | 1.23 | +0.0000 | **ideal — PASS (reference)** |
| B unbalanced (repulsion only) | 28k | 0.028 | (20.0/13.7) | 0.70 | **+0.0246** | **CONTAMINATED** |
| C charge-balanced (K=K_att) | 48k | 0.048 | YES (20.0/21.4) | 1.00 | −0.0002 | **ideal — PASS** |

All three thermalize fast (R ≪ 1, ~20–35 re-thermalizations per e-fold). Thermalization is **not** the
discriminator — every config equilibrates. The discriminator is the **chemical potential**:

- **Baseline** is ideal by construction (slope 0, S(0) ≈ 1 up to finite-size).
- **Unbalanced** interaction (like-sign repulsion, no ± bind) **contaminates**: μ_excess acquires a slope
  ∝ n̄ (+0.025), and the structure factor drops to S(0) ≈ 0.70 (dispersed/sub-Poissonian — the repulsion
  signature). This is the §6 failure mode, realised: a perfectly thermalized stack with a *generic* SSV
  interaction does **not** keep μ ∝ ln n.
- **Charge-balanced** (K = K_att): the leading mean-field term (K−K_att)·n̄/2 **cancels**; the slope
  collapses to −0.0002 (≈ 0) and S(0) returns to 1.00. The neutral ± plasma keeps the chemical potential
  ideal and the log survives.

## The decisive point: why the slope must be ~0, and what protects it

The tilt rides on μ(n̄) ∝ ln n̄, and at the cosmological pivot n̄ ~ 10⁷⁴, so ln n̄ ~ 170. A μ_excess slope of
even +0.025 per unit n̄ would contribute ~0.025 × 10⁷⁴ — astronomically larger than 170, dragging the
chemical potential to a pure power of n̄ and the tilt into the excluded branch. So the bath clause's
μ_excess ≈ 0 requirement is **stringent**, and the run shows it is **not automatic**: a generic ± SSV
interaction breaks it. What restores it is **charge balance** — when same-sign repulsion and ±
co-location attraction balance (K = K_att), the mean-field cancels and the chemical potential is ideal
again.

**This is a new, falsifiable physical requirement that the simulation surfaced rather than assumed:**
the protection of n_s = 0.9649 from interaction contamination requires the early CP plasma to be
**effectively charge-neutral** (balanced ±). That is a genuine CPP condition — cosmological charge
neutrality is independently expected — and it is now *load-bearing* for the tilt, not incidental. It also
gives the structure factor S(0) ≈ 1 a clean physical meaning: it is the in-simulation signature that the
plasma is neutral enough for the log to survive.

## Methodology validation

- ChatGPT's observable (v), S(0), earned its place: it cleanly flagged the unbalanced config (0.70,
  dispersed) — a directional read the single-site mean/var gives less sharply.
- The μ_excess-slope probe is the decisive discriminator, exactly as the panel agreed; thermalization
  speed (R) did not distinguish the configs.
- A1 discipline held throughout (observables read occupation counts only).

## Honest caveats

- **Toy, not CPP.** The hop rule and the quadratic site energy are a stand-in for real macro-CP PCD
  dynamics; a clean in-house result is suggestive, not dispositive.
- The specific interaction is one choice; the charge-balance cancellation is generic for symmetric ±
  quadratics but should be checked for the actual SSV form.
- Finite-size: baseline S(0) ≈ 1.23 (not exactly 1) at M=300/75 blocks; the *contrast* between configs
  (0.70 vs 1.00 vs 1.23) is the signal, not the absolute value.
- A residual sub-leading μ_excess (Debye-like, ∝ √n̄) could still matter at cosmological n̄ even when the
  leading term cancels; the toy does not resolve it. Flag for the real-dynamics analysis.

## Status

- Bath clause: **conditionally PASSES** in the toy — fast thermalization (R ≪ 1) and ideal chemical
  potential (μ_excess slope ≈ 0, S(0) ≈ 1) **provided the ± interaction is charge-balanced**.
- New requirement surfaced: **cosmological charge neutrality protects the log**; a generic (unbalanced)
  interaction contaminates the tilt.
- n_s = 0.9649 remains a zero-NEW-axiom prediction *conditional on* (a) the bath (now toy-supported under
  neutrality) and (b) the real SSV interaction being effectively neutral/balanced.
- **Independent confirmation requested** (swarm-facing request:
  `series_phenomena/cosmology/early_universe/swarm_request_interacting_mc.md`).

## Pointers

- Script: `.../scripts/0756_interacting_mc.py`. Builds on 0753 (spec) + 0755 (S(0) observable, Stage 0).
- Reasoning: `.../reasoning/0756_interacting_mc.md`.
