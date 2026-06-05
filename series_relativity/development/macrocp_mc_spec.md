# Minimal-PCD Monte Carlo spec: testing the BATH clause (HALF 1) of CAND-AX-EU-1

*Patch 0753, Session 154. Specifies the Monte Carlo that would establish — or falsify — the one thing
the emergence track (0752) still needs: that macro-CP PCD dynamics thermalize a CP stack to Gibbs
equilibrium on sub-e-fold timescales, with A1-invariant microstates and without generating an interaction
term that spoils μ ∝ ln n. Runnable reference skeleton:
`series_phenomena/cosmology/early_universe/scripts/0753_macrocp_mc_reference.py` (baseline PASSES). NO THEO.*

## Scope (what this MC does and does not decide)

The emergence track (0752) split CAND-AX-EU-1 into: the **log** (μ ∝ ln n — already entailed by A1's
occupation-number ontology, not tested here) and the **bath** (the stack actually reaches Gibbs
equilibrium fast — the only open dynamical question). **This MC tests the bath clause, HALF 1, only.** A
PASS dissolves the tenth axiom: n_s = 0.9649 becomes A1 (log) + emergent ergodicity (this MC) + the 0746
boost coupling, with the axiom count staying at 9. A FAIL means the bath cannot be assumed and the axiom
(or a weaker working postulate) is still required.

## State (A1-invariant by construction)

The only physical variables are per-GP occupation counts: n₊(g), n₋(g) for the two polarities on each GP
g. **No per-CP labels, histories, or identities exist in the state** — consistent with A1 (a CP is only
polarity, type, position) and with Thomas's postulate that the full configurational history lives in the
SSV hologram (the occupation field), not on individual CPs. In code, particle→site arrays are permitted as
scaffolding, but **every observable reads occupation counts only** (`bincount`), never a particle index.
This is what guarantees the measured statistics are the indistinguishable (Gibbs) ones.

## The PCD rules (macro-CP dynamics from one occupation-dependent hop)

All four phenomena Thomas names emerge from a single rule, so the model stays minimal:

1. **Macro-CP formation** — not a separate object; a "macro-CP" is just a GP with high occupation. It
   forms automatically from the violent seed and dissolves as the stack relaxes.
2. **Inter-GP hop (the engine)** — at each Moment a random CP leaves its GP and re-stacks on a GP chosen
   by the local SSV field, accepted with Metropolis weight exp(−ΔE/kT), where ΔE is the change in SSV
   configurational energy `ssv_energy(n₊, n₋, ·)` and kT is the ZBW jitter scale.
3. **± splitting** — emerges when `ssv_energy` makes same-polarity crowding costly and ± co-location
   favourable: + and − CPs preferentially separate onto different GPs, exactly as the early ± story
   requires. (Baseline `ssv_energy ≡ 0` → no splitting; the swarm switches it on — see below.)
4. **Evaporation / re-stacking** — over-full GPs have higher outward hop acceptance (more CPs to move,
   higher SSV pressure), so they drain and re-stack elsewhere; the proto-ZBW oscillation is the ± species
   sloshing between GPs under this rule.

**Initial condition:** pile all CPs onto the **13-GP cohort** (central + icosahedral shell) — the violent
over-stacked early universe — and let the dynamics run.

## Observables

- **(i) Equilibration time τ_eq.** Track the fraction of CPs still on the original 13 seed GPs; τ_eq is the
  Moment-count at which it relaxes to within 5% of the equilibrium fraction (13/M). (Equivalently: KL
  divergence of the occupation histogram from the stationary distribution dropping below threshold.)
- **(ii) Stationary distribution.** The equilibrium occupation histogram must be **Gibbs/Poisson**:
  mean ≈ variance ≈ λ (= N_tot/M). A non-Poisson stationary state (clustering/condensation) signals that
  the effective μ is not ∝ ln n.
- **(iii) Excess chemical potential μ_excess(n̄).** By Widom test-particle insertion,
  μ_excess = −kT·ln⟨e^{−ΔE_insert/kT}⟩, measured across several mean concentrations n̄ (= λ). The **ideal**
  part μ_ideal = kT·ln(n̄/z₁) is guaranteed by A1 counting and is *not* measured; the MC measures whether
  interactions add an **excess**. The log survives iff μ_excess has **no significant term linear in n̄**.
- **(iv) Adiabaticity ratio R = τ_eq / t_efold.** t_efold = 1/H is the e-fold time set by the H-engine's
  inflationary rate (in Moments). R ≪ 1 means the stack re-thermalizes many times within each e-fold, so
  the quasi-static chemical-potential picture the chain uses is valid.

## Pass / fail

**PASS (bath clause established → tenth axiom dissolves):**
- R ≪ 1 (target ≤ 0.1, i.e. ≥ 10 re-thermalizations per e-fold), with interactions **on**;
- stationary occupation Gibbs/Poisson (mean ≈ var ≈ λ);
- μ_excess(n̄) ≈ 0 with no significant ∝ n̄ term across the scanned λ range.

**FAIL modes:**
- **R ≳ 1** → no thermalization within an e-fold; the bath cannot be assumed (the strongest risk, and the
  thing worth risking).
- **non-Poisson stationary state** → condensation/clustering; effective μ ≠ kT ln n.
- **μ_excess ∝ n̄** → the SSV interactions generate a mean-field term that contaminates the tilt and pushes
  it toward the excluded power-law branch (the 0746 mechanical column). This is the subtle, important
  failure: even with perfect thermalization, a mean-field interaction can spoil the log.

## Reference skeleton result (baseline)

The skeleton runs the non-interacting baseline (`ssv_energy ≡ 0`), M = 200 GPs, 4000 ± CPs, λ = 20, seeded
on 13 GPs. It relaxes (seed fraction 1.000 → 0.072 vs equilibrium 0.065; τ_eq ≈ 28,000 Moments), reaches
the Poisson stationary state (mean 20.00, var 20.5), has μ_excess ≈ 0, and for an example inflationary
H = 10⁻⁶ t_P⁻¹ gives R ≈ 0.028 (~36 re-thermalizations per e-fold) → **baseline PASS**. The baseline only
shows the methodology and the ideal reference; **the real test is to switch on `ssv_energy`** (the ±
attraction/repulsion + same-sign crowding model) and confirm (i)–(iv) survive with interactions on.

## What a PASS would mean, stated honestly

A PASS does **not** show "the MC derives n_s." It shows the bath clause: macro-CP dynamics reach Gibbs
equilibrium ≪ Hubble with A1-invariant microstates and without tilt-contaminating interactions. Combined
with A1 (which supplies the log) and the 0746 coupling (μ-driven boost), that is sufficient for
n_s = 0.9649 as a **zero-NEW-axiom** prediction. The honest claim is "MC establishes the bath; A1 carries
the log; 0746 carries the coupling."

## Panel addendum (Patch 0755 — from the 0754 reviews)

Two upgrades from the AI panel (full integration: `series_phenomena/cosmology/early_universe/panel_integration_0754_reviews.md`):

- **Observable (v) — structure factor / compressibility (ChatGPT).** Add the long-wavelength structure
  factor S(k→0) (operationally the block-count Fano factor, var/mean of coarse-grained block occupations).
  It detects inter-site correlations that the single-site Poisson check can miss: ideal S(0) ≈ 1,
  clustered (attractive mean field) S(0) > 1, dispersed (repulsive) S(0) < 1. **PASS now also requires
  S(0) ≈ 1 under interactions** — a sharper equation-of-state probe (κ_T = ∂n̄/∂μ ∝ S(0)) than the
  one-point histogram alone.
- **Stage 0 — factorization-first protocol (ChatGPT).** Before the ± SSV detail, run generic single-site
  hopping r(i→j) = f(nᵢ)·g(nⱼ) and test whether the stationary state factorizes, P({nᵢ}) = ∏ p(nᵢ); if so
  extract p(n) and read whether ∂ln p/∂n ⇒ μ ∝ ln n. This isolates which dynamics preserve the ideal log
  before the specific interaction is introduced.

Both reviewers (ChatGPT, Grok) also asked that the A1→occupation-number step be an explicit argument; it
is written out in the integration note §2. Grok independently built an MC that converges on the same four
observables and pass/fail.

## Pointers

- Implements the bath-clause test from 0752; rests on 0749 (log = A1 indistinguishability), 0751
  (candidate axiom + chain), 0746 (count-driven coupling).
- Reference skeleton: `.../scripts/0753_macrocp_mc_reference.py` (pluggable `ssv_energy`, default 0).
- Reasoning: `series_relativity/development/reasoning/0753_macrocp_mc_spec.md`.
- Next: the swarm runs the interacting version (`ssv_energy` on) and reports (i)–(iv) + verdict. PASS →
  register the dissolution (n_s zero-new-axiom); FAIL → the working-postulate path of 0751 stands.
