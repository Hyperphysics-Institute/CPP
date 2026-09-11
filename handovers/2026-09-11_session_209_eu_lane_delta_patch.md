# EU-lane Handover — Session 209 Close (11 Sep 2026) — new block opened; δ_patch's gate half-closed; C-5 now makes a falsifiable prediction

**Patch 3901. Lane: EU, block 3900–3999 (NEW). Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3899 at session start; 3900–3901 delivered as patch files. **Next free: 3902.** GR lane: next free 3715.
**Block:** **3900–3999, allocated by the founder** on exhaustion of 3800–3899 at Patch 3899. Registered in `id_block_registry.md`.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).

## The single most important next action — worker work, in-lane
**Derive the Q-to-Q and E-to-anything affinity strengths from the SCP composition dynamics, compute f_E/f_Q, and compare against [1.7, 6.5].**

> **C-5 PREDICTS f_E/f_Q ≈ 2.8.** A computed ratio of **1.1 or 20 kills C-5's amplitude outright.**

> ### ⚠ HAZARD, NAMED AND UNAVOIDABLE
> **You will have read this file, so you already know the target is 2.8.** That is the condition under which PD-007 gets violated without anyone deciding to violate it. **Derive the affinities from the composition dynamics and write them down BEFORE computing the ratio.** If you find yourself adjusting an affinity after seeing where the ratio lands, stop and record it.

## What was established
**The seed is not the source.** Randomly seeded SCP compositions give a per-SCP spread **Poisson in n₀** — 10⁻³ at n₀ = 10⁶, 10⁻¹² at 10²⁴. **Minute.** Had δ_patch been seed-set, **C-5 would already be dead by many orders.** Ruling that out was worth the session alone.

**Saturation sets it.** ℓ_corr is **by definition** the range over which the sorting is coherent, so **within one correlation volume preferential attachment has run to completion**: each patch is **wholesale** Q-dominant or E-dominant, **however small its seed.** The amplification *is* the mechanism; the seed only picks which way a patch falls.

> **δ_patch = |ln(f_E/f_Q)| — a log-ratio of two SATURATED unstacking fractions. O(1) by construction, not by hope.**

**⇒ The qualitative half of 3898's gate is DISCHARGED.** It asked whether δ_patch is 1 *for a reason*; **the reason is saturation.** *(Qualitative half only — O(1) is not 1.02.)*

**The number is not on file.** D-1: the corpus fixes the affinities **qualitatively only** (3894). **Not computed, not supplied** — **fourth session running** that a missing parameter has been carried rather than chosen.

## The prediction
> ℓ_sat = 1/α = **137.0** (derived, 3898) + ℓ_req = 138.4·δ^{−2/3} (observed, 3896)
> ⇒ **δ_patch = 1.015** ⇒ **f_E/f_Q = 2.76**

**E-dominant patches unstack ≈2.8× further than Q-dominant ones.** A statement about two rates, not a fitted parameter.

**Direction checks out:** Q-dominant patches self-attract ⇒ re-superimpose more readily ⇒ unstack **less**. ✓

| ℓ_sat vs 1/α | f_E/f_Q |
|---|---|
| 1.5× | **1.7** |
| 1.0× | **2.8** |
| 0.67× | **6.5** |

**Prediction, not fit:** the brake came from α with **no reference to the target**; the requirement came from the sky; their agreement demands a third quantity that has an **independent route**. **Same structure as T-2's kT_bath bound (3850 §4)**, which was accepted.

## C-5's debts, current
1–4. ~~Referent~~ (3890), ~~reservoir~~ (3892), ~~correlation length~~ (3896, Gaussianity **cleared**), ~~saturation brake~~ (3898, **consistent**).
5. **δ_patch — qualitative half discharged (3900); quantitative half now a falsifiable prediction. THE GATE.**
6. **Adiabaticity** vs Planck's isocurvature bound. **Untouched.**

## Owed
- **Isak:** recompile **EU-1 (V1.6)** and GR-2 (V2.11).
- **Maintainer:** CONV-046 — **the package now carries a live candidate with a derived ζ, a stated microphysics, one observational test cleared, a consistent brake, and a falsifiable prediction**; the amended DE escalation (3858); cosmic-web owed piece (3833); `DM_project_map.md` stale (3884).
- **EU-1 V1.7 (bundle):** 3854 VSL clarification; 3876 §5 as qualified by 3878. **Do not add C-5.**

**Anti-priorities:** **do not arrange the affinities to land on 2.8** — the hazard is named and live; **do not report C-5 as working** — five tests engaged is not six cleared; **do not quote 3898's 1%** (band 87–220); **never supply the stack number**; follow **§0.5 D-1…D-6**; no cross-lane edits without sanction; do not retire 3710; **nothing in this arc refutes n_s** — PRED-C-96 reads 0.9654 (V1.6).

## §15 Steps A–H
- **A** `session_logs/2026-09-11_session_209_log.md` (3901). **B** transcript row 3900. **C** development vignette (Session 209).
- **D** Tier 4: `reasoning/3900_delta_patch.md`.
- **E** Registries: **`id_block_registry.md` — new block 3900–3999 registered**; `research_frontier.md` (3900 prepend); `future_projects.md`; in-place update at `swap_brake.md` §6b. N/A: `predictions.md`, `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md` — **no constant minted; C-5 live, not adopted.**
- **F** none (no panel). **G** no PD minted; founder allocated the block. **H** this file.

## Governance note
**Converting an uncomputable number into a falsifiable prediction is a legitimate move, and it has one condition: name the independent route before stating the number.**

This patch did that — the affinities are the route, and they exist independently of the amplitude. Without such a route the same manoeuvre is just a fit wearing a prediction's clothes. **The test of whether a "prediction" is real: could it come out wrong?** Here it can, and the band says how.
