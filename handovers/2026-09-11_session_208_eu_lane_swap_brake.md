# EU-lane Handover — Session 208 Close (11 Sep 2026) — the brake derived (consistent, not confirmed); **EU BLOCK EXHAUSTED**

**Patch 3899. Lane: EU, block 3800–3899. Written under PD-006.**

## ⚠ BLOCK EXHAUSTION — read before doing anything
**Patch 3899 is the last ID in the EU block 3800–3899.** **A new EU block must be allocated before the next EU patch can be numbered.** Precedent: the 3600–3699 → 3800–3899 allocation recorded in `id_block_registry.md`. **This is a maintainer action and it blocks all further EU work.**

## Orientation
**Repository state:** origin/main at Patch 3897 at session start; 3898–3899 delivered as patch files. **Next free: NONE — block exhausted.** GR lane: next free 3715.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).

## The single most important next action (once a block exists)
**Compute δ_patch from the dynamics.** It is the one quantity standing between *consistency* and *a result*, and it is **in-lane and computable**.

> δ_patch is the fluctuation in **ln f** within a single correlation volume — set by the **affinity strength** and the **spread of SCP compositions** across sites (3894).
>
> **If it comes out 1 for a reason**, the requirement band collapses onto 138 PSR, the 1% agreement becomes meaningful, and **C-5's amplitude is derived rather than accommodated.**
> **If it comes out 0.3 or 3**, the brake is merely compatible — worth something, not a result.

**PD-007, and this is now the sharpest it has been in the arc: do not tune δ_patch to make 137 land.** Derive it from the affinity, then compare.

## What was derived
**D-1 first: no swap rate is on file.** The corpus fixes the eDP swap **qualitatively only** (*"not faithful … pair-swap readily"*). So it had to be **derived**, as 3896 required.

**Two protocol facts and one inference:**
- **Build (protocol fact):** the hop cascade reaches the PSR **within one Moment** (3862) ⇒ correlation extends **1 PSR per Moment**. Not an estimate.
- **Decay (the single inference):** **pair-swapping is an electromagnetic process between eCPs**, and EM transition rates carry the EM coupling ⇒ **Γ_swap ~ α**.
- **Saturation:** ballistic growth against constant decay gives ℓ = v/Γ ⇒ **ℓ_sat = 1/α = 137.0 PSR.**

**Comparison:** 3896's requirement, from the **observed** amplitude, is **138.4 PSR** — **1.0% agreement.**

## The honest limit — carry this, not the 1%
**The requirement is not sharp to 1%.** δ_patch is **O(1)**, and ℓ_req ∝ δ^{−2/3}:

| δ_patch | required ℓ_corr |
|---|---|
| 0.5 | **220 PSR** |
| 1.0 | 138 PSR |
| 2.0 | **87 PSR** |

> **1/α = 137 sits inside the 87–220 band. CONSISTENT — NOT CONFIRMED.**
>
> **Do not quote the 1% as precision.** A band stated in prose gets remembered as its central value; that is why the table is here.

## Ordering, disclosed
**The worker noticed 138 ≈ 137 before finding the reason.** That is the order that produces numerology, and it is recorded in the finding as well as the reasoning capture.

**The check that makes it reportable:** would the derivation have produced α without the target in view? **Yes** — the swap is electromagnetic and EM rates carry α. Dull, not tailored. **The reasoning is sound; the order was not. Weigh both.**

## C-5's debts, current
1. ~~Referent~~ (3890). 2. ~~Reservoir~~ (3892). 3. ~~Correlation length~~ (3896 — Gaussianity **cleared**). 4. ~~Saturation mechanism~~ — **derived here; consistent, not confirmed.**
5. **δ_patch — THE GATE.**
6. **Adiabaticity** vs Planck's isocurvature bound. **Untouched.**

## Owed
- **Maintainer: ALLOCATE A NEW EU BLOCK** (blocking); CONV-046 — the package now carries a live candidate with a **derived ζ**, a **stated microphysics**, **one observational test cleared**, and a **consistent brake**; the amended DE escalation (3858); cosmic-web owed piece (3833); `DM_project_map.md` stale (3884).
- **Isak:** recompile **EU-1 (V1.6)** and GR-2 (V2.11).
- **EU-1 V1.7 (bundle):** 3854 VSL clarification; 3876 §5 as qualified by 3878. **Do not add C-5.**

**Anti-priorities:** **do not quote the 1% as precision**; **do not report C-5 as working** — four tests cleared is not six; **do not tune δ_patch**; **never supply the stack number**; follow **§0.5 D-1…D-6**; no cross-lane edits without sanction; do not retire 3710; **nothing in this arc refutes n_s** — PRED-C-96 reads 0.9654 (V1.6).

## §15 Steps A–H
- **A** `session_logs/2026-09-11_session_208_log.md` (3899). **B** transcript row 3898. **C** development vignette (Session 208).
- **D** Tier 4: `reasoning/3898_swap_brake.md`.
- **E** Registries: `research_frontier.md` (3898 prepend); **`id_block_registry.md` — BLOCK EXHAUSTION FLAGGED**; `future_projects.md`; in-place update at `correlation_length.md` §5b. N/A: `predictions.md`, `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md` — **no constant minted; C-5 live, not adopted.**
- **F** none (no panel). **G** no PD minted. **H** this file.

## Governance note
**Disclose the order of discovery when a result is a numerical coincidence you noticed first.**

The finding could have been written as a clean derivation ending in 1/α, and it would have read better. It would also have concealed that the target was in view before the mechanism was sought — which is precisely the information a reader needs to weigh it. **The derivation survives the disclosure; that is what makes it reportable.** A derivation that *needed* the concealment would not have been.
