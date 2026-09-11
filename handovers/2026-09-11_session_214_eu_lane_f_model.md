# EU-lane Handover — Session 214 Close (11 Sep 2026) — last in-lane caveat closed; **the lane's own work on C-5 is finished**

**Patch 3911. Lane: EU, block 3900–3999. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3909 at session start; 3910–3911 delivered as patch files. **Next free: 3912.** GR lane: next free 3715.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).

## Read first — there is no in-lane C-5 item left, and that is the result
**The lane's own work on C-5 is finished.** Every debt and every caveat that could be addressed without leaving the EU lane has been. **Do not look for an eighth item.**

**The two outstanding items are both outside this lane:**
1. **SM-sector conserved-charge check** — does the sea's q:e composition carry a net conserved quantum number? **Gates the 3908 adiabaticity pass**; if it does, the ~30× isocurvature failure stands and **C-5 dies.** Cross-lane; **needs sanction or a founder answer.**
2. **The H ∝ μ assignment** — foundational. **The reason the normalisation is κ\*-gated** (3906).

## ⚠ Carry this exactly — both halves or neither
> **There is now a source with the right spectrum — Gaussian, scale-free, conditionally adiabatic, with a derived microphysics — AND the normalisation is not derivable as the framework stands.**

**And a conditional pass with an unmet condition is not a pass.** Do not write "C-5 works."

## What was closed
**The 3902 §7 model caveat**, which was decisive rather than technical: **f ~ 1/A is the re-stacking-dominated limit** of f = R_out/(R_out + R_in). **In the opposite limit f ≈ 1 independent of A, so f_E/f_Q → 1 and the amplitude chain fails.**

**Settled by f itself, with no new assumption** — 3892 had already fixed f(start) = **1/n₀** and **ln f linear in N_rem**:

> **ln f(pivot) = −(57/64.47)·ln n₀ = −0.884 ln n₀**

| n₀ | f(pivot) | crossover (f = 0.5) |
|---|---|---|
| 10⁶ | 5.0×10⁻⁶ | N_rem = 3.2 |
| 10¹² | 2.5×10⁻¹¹ | N_rem = 1.6 |
| 10²⁴ | 6.0×10⁻²² | N_rem = 0.8 |

> **f(pivot) ≪ 1 for any large n₀ ⇒ deeply re-stacking-dominated ⇒ f ~ 1/A HOLDS — independent of the stack number** (fifth session running that n₀ was carried rather than chosen).
>
> **And the crossover sits in the last one to three e-folds, while observed modes exit at N_rem ≈ 50–60** — more than an order of magnitude away.

**Both limits are traversed, and must be:** the count law closes only if **f → 1** at the end. **The transition is what *ends* the unstacking** — a feature, arriving after the observable window is written. *(This was nearly mis-stated as a problem; it is not.)*

**This closes a caveat, not a debt. The headline does not move.**

## Owed
- **Founder/maintainer:** the **SM-sector conserved-charge check**.
- **Isak:** recompile **EU-1 (V1.6)** and GR-2 (V2.11). **Two versions behind.**
- **Maintainer:** **CONV-046 dispatch — the package is complete and ready.** It carries: the 3835 no-go, 3837 conflict, 3847 closure (negative); T-1 and T-2 (positive); the 3868 PCD audit; the **3902 meta-warning** (three chained near-misses — **weigh as one**); the **3904 narrowing** (C-5 = source-and-shape); the **3906 κ\* ruling** (**A_s is not predicted**); and **C-5's closed ledger** with its one condition. Also: the amended DE escalation (3858); cosmic-web owed piece (3833); `DM_project_map.md` stale (3884).
- **EU-1 V1.7:** 3906's four sentences; 3854's §Background VSL clarification; 3876 §5 as qualified by 3878.

## Forward queue
**No in-lane C-5 item.** **OPEN-EU-LATTICE-EXTENT-1** (3878) remains, non-blocking. Otherwise the lane awaits the two external items and the maintainer's dispatch.

**Anti-priorities:** **do not manufacture an eighth C-5 item**; **do not report C-5 as working**; **do not claim A_s is predicted**; **do not split the headline's two halves**; follow **§0.5 D-1…D-6**; do not retire 3710; **nothing in this arc refutes n_s** — PRED-C-96 reads 0.9654 (V1.6).

## §15 Steps A–H
- **A** `session_logs/2026-09-11_session_214_log.md` (3911). **B** transcript row 3910. **C** development vignette (Session 214).
- **D** Tier 4: `reasoning/3910_f_model_limit.md`.
- **E** Registries: `research_frontier.md` (3910 prepend); `id_block_registry.md` (next free 3912); `future_projects.md`; in-place closure at `affinity_ratio.md` §6b. N/A: `predictions.md`, `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md` — **C-5 is live, not adopted.**
- **F** none (no panel) — **CONV-046 is complete and awaiting dispatch.** **G** no PD minted. **H** this file.

## Governance note
**A quantity derived for one purpose settled a question raised for another.** f was derived at 3892 to give C-5 its perturbation; it turned out to decide, without modification, which limit of the steady state obtains. **That is the third time in this arc an earlier result answered a later question** (T-1 at 3880, the founder's qDP definition at 3908, f here) — and unlike the five *rediscoveries* logged at 3905, these were the corpus's own results doing work, not answers missed and re-found.

**Worth distinguishing in the record:** *rediscovery* is a failure of search; *reuse* is a sign the framework is tightly coupled. **The arc has produced five of the first and three of the second.**
