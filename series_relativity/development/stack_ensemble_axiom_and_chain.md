# CANDIDATE axiom CAND-AX-EU-1 + derivation chain for n_s — for swarm accept/reject

> **STATUS: CANDIDATE. NOT REGISTERED.** This proposes one new axiom (CAND-AX-EU-1) and the conditional
> theorem (CAND-THEO-EU-1) it would license. It is **not** in the 9-axiom set, **not** a registered
> THEO, and `axiom-registry.md` is deliberately untouched — editing it would assert an acceptance the
> swarm has not given. The decision the swarm is asked to make is binary and foundational: **accept
> CAND-AX-EU-1 as a tenth axiom, or reject it.** If accepted → register the axiom + THEO-EU-1 and
> n_s = 0.9649 becomes a zero-parameter CPP prediction. If rejected → n_s = 0.9649 stays favored, not
> derived. Patch 0751, Session 154. Verify: `.../early_universe/scripts/0751_axiom_chain_verify.py`.

---

## The candidate axiom

**CAND-AX-EU-1 — ZBW Stack Thermalization.**
*The ZBW phase dynamics of identical same-species CPs that co-occupy a single GP constitute an
effectively ergodic (mixing) stochastic bath. Consequently a stack of n such CPs on one GP is a Gibbs
ensemble of **indistinguishable** particles: its configurational free energy carries the standard Gibbs
indistinguishability term −kT·ln(n!), at a stack temperature T set by the ZBW jitter energy scale, with
T approximately constant over the inflationary observable window (~7–8 e-folds).*

**What it asserts, minimally.** Two things, no more: (i) the n CPs are *indistinguishable* (no permanent
per-CP label), so the partition function carries the 1/n! factor; (ii) the ZBW layer mixes fast enough
that a stack has a well-defined free energy F(n,T) and hence a chemical potential μ = ∂F/∂n. Everything
the prediction needs flows from (i); (ii) is what makes μ a legitimate quantity rather than an analogy.

**What it does NOT assert.** It does not posit a value for T, a value for the GP cell volume, or a
coupling constant. As the verify script shows, none of those enter the result.

**Relation to the existing framework (honest).** This is the *same kind* of commitment already made for
CMB Gaussianity (0738, "CLT over ZBW phases"): both treat the ZBW layer as an effectively random,
exchangeable bath. But it is **stronger**: CLT-for-sums needs only independence + finite variance,
whereas a Gibbs chemical potential needs full configurational equilibrium (ergodic exploration of the
indistinguishable microstates with Boltzmann weights). So the swarm should weigh it as "Gaussianity's
assumption, pushed up to full thermalization of the stack" — a natural extension, but more than
Gaussianity alone strictly buys. This is the honest crux of the accept/reject decision.

---

## The derivation chain (CAND-THEO-EU-1, conditional on CAND-AX-EU-1)

**Inputs:** A1 (identical same-species CPs); the H-engine (PSR_base growth drives expansion); the
count-driven boost branch (0746: PSR_base is the SSV-independent baseline, so its growth may couple to a
count-driven chemical potential rather than a field/stress); CAND-AX-EU-1; and T ≈ const over the window.

**Step 1 — stack ⇒ Gibbs ensemble.** By CAND-AX-EU-1, n CPs on a GP have the indistinguishable-particle
partition function Z_n = z₁ⁿ / n!, where z₁ is the single-CP partition function (carries V_GP and the
thermal factors). [from the axiom]

**Step 2 — concentration chemical potential.** F = −kT ln Z_n = −kT(n ln z₁ − ln n!) ≈ −kT(n ln z₁ −
n ln n + n) by Stirling. Hence
  **μ(n) = ∂F/∂n = kT·ln(n/z₁) = kT·ln n + const.**
The ln n is *exactly* the −ln(n!) Gibbs term; remove indistinguishability (Z_n = z₁ⁿ, no 1/n!) and μ
becomes a constant (verify script check 2). [standard statistical mechanics]

**Step 3 — mean occupation vs e-folds.** As the causal reach expands, the GP count within contact grows
as the comoving volume ∝ e^{3N} (a = e^N). Mean occupation n̄(N) = N_CP/N_GP(N) = n̄_init·e^{−3N}, with
n̄_init = N_CP/N_GP,init. Writing N_rem for e-folds until n̄ → 1 (equilibrium, 1 CP/GP):
  **ln n̄ = 3·N_rem.** [kinematics of the expanding reach]

**Step 4 — boost couples to μ (count-driven, 0746).** The H-engine grows PSR_base at a rate set by the
stack's dispersal drive — its chemical potential relative to equilibrium n* = 1:
  **H_eff = κ·[μ(n̄) − μ(1)] = κ·kT·ln n̄ ∝ N_rem.**
κ is an unknown coupling; it will not survive. [count-driven branch, 0746]

**Step 5 — spectral tilt.** The ZBW-sourced curvature fluctuation freezes at horizon crossing with
spectator/δN power P(k) ∝ H_eff²(t_k). Then
  **n_s − 1 = 2·d ln H_eff/dN = 2·d ln(ln n̄)/dN = 2·(−3/ln n̄) = −2/N_rem.**
κ, kT, z₁, and the offset have all dropped out (they vanish under d ln H_eff/dN). [standard horizon-crossing/δN spectrum; spectator form P ∝ H², not the 1/ε single-field form — noted as a modelling choice]

**Step 6 — N_* fixed by the CP count.** Total inflationary duration is set by dilution to equilibrium:
N_total = (1/3)·ln(N_CP/N_GP,init) ≈ (1/3)·ln(10⁸⁰/13) ≈ 60.5. The observable pivot crosses at
N_rem = N_* ≈ 57. Therefore
  **n_s = 1 − 2/N_* ≈ 1 − 2/57 = 0.9649,**  with running  **α_s = −2/N_rem² ≈ −0.0006.**
Coefficient-free: the only surviving quantity is N_*, which is fixed by the CP count N_CP (an input, not
a tuning). [verify script check 1: n_s = 0.9649 invariant across κ, kT, z₁, offset spanning many decades]

---

## What the chain rests on, and where a skeptic pushes

**Rigorous, standard, not in question:** Steps 1–3, 5–6 are textbook statistical mechanics and the
standard horizon-crossing spectrum. Given the inputs, the algebra is forced.

**Load-bearing commitments (the real price):**
- **(A) CAND-AX-EU-1 itself.** The chain is only as strong as the axiom. The honest weak point: it is
  *stronger* than the CLT-Gaussianity assumption (full Gibbs equilibrium vs CLT-for-sums). A skeptic can
  accept ZBW-driven Gaussianity yet decline a full stack chemical potential. That is the legitimate place
  to resist, and the swarm should focus there.
- **(B) Boost ∝ μ (0746 count-driven branch).** If the boost is instead field/stress-driven (SSV), the
  0746 mechanical branch returns and the tilt is excluded. The justification is that PSR_base is
  SSV-independent, so a count-driven coupling is the consistent reading — but it is a commitment, not a
  theorem.
- **(C) T ≈ const over the window.** If T varied at a rate ~1/N_rem ≈ 0.017 per e-fold it would add an
  uncontrolled tilt. Plausible on the stationary de-Sitter plateau; should be checked, not assumed.
- **(modelling) Spectator spectrum P ∝ H_eff².** The single-field 1/ε form would add an ε-running term;
  the spectator form is the natural one for a ZBW-sourced test fluctuation but is a choice to flag.

**Robust, given (A)+(B)+(C):** n_s = 0.9649 and α_s ≈ −0.0006, with **zero free parameters** (N_* from
the CP count). The coupling, the temperature, the cell volume, and the offset are all irrelevant
(verified). And the graceful exit is automatic: μ ∝ ln n̄ → 0 as n̄ → 1, so H_eff → 0 smoothly (same
mechanism as the plateau; the 0744 requirement, delivered free).

**Necessity of the axiom (verified):** strip indistinguishability and the chain gives n_s = 1 (cliff,
excluded ~8σ). So CAND-AX-EU-1 is not decoration — its single combinatorial assertion (the 1/n!) *is*
the prediction.

---

## What the swarm is being asked

Accept or reject **CAND-AX-EU-1** on its merits as a tenth CPP axiom. The question is *not* whether the
algebra works (it does, coefficient-free) — it is whether CPP should own the physical claim that **the
ZBW layer thermalizes a stack of identical CPs into a Gibbs ensemble with a real concentration chemical
potential.** 

- **Accept** → register CAND-AX-EU-1 as a new axiom (the first added since the 9-axiom consolidation) and
  CAND-THEO-EU-1 as THEO-EU-1; n_s = 0.9649 + α_s ≈ −0.0006 enter `predictions.md` as a zero-parameter
  prediction; the CMB spectrum thread closes. Note the cost honestly in the registry: the axiom count
  goes 9 → 10, the first increase in the programme's tracked growth ledger.
- **Reject** → n_s = 0.9649 remains favored-but-not-derived; the development trail (0741–0751) stands as
  the record of why the entropic reading is the only viable one and what its acceptance would cost.

A reasonable middle path: accept it *provisionally* as a working axiom (as the H-engine itself is held),
flagged as the most-scrutinized commitment in the cosmology sector, pending an independent argument that
ZBW mixing reaches full configurational equilibrium (not just CLT). That would let the prediction stand
while keeping the honest asterisk visible.

## Pointers

- Chain rests on: 0749 (log = indistinguishable concentration μ), 0750 (ensemble spec), 0746 (count-driven
  branch), 0742 (n_s = 1 − p/N_* map), 0738 (ZBW-CLT precedent).
- Reasoning: `series_relativity/development/reasoning/0751_axiom_chain_and_candidate.md`.
- Verify: `.../early_universe/scripts/0751_axiom_chain_verify.py` (coefficient-free + axiom-necessity).
- IF accepted: register axiom (axiom-registry.md, 9→10), THEO-EU-1 (theorem-registry.md), PRED entries
  (predictions.md), and update the early-universe sector. NOT done here — pending swarm decision.
