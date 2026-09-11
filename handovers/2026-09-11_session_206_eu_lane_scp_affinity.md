# EU-lane Handover — Session 206 Close (11 Sep 2026) — the Poisson warning is broken; the deciding quantity is now the correlation length

**Patch 3895. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3893 at session start; 3894–3895 delivered as patch files. **Next free: 3896.** GR lane: next free 3715.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).

## The single most important next action — worker work, in-lane
**Compute the correlation length of the SCP affinity.** C-5's amplitude debt is now this and nothing else.

> **Short-range affinity** ⇒ the CLT wins over ≥10⁶⁴ SCPs per mode, the field **Gaussianises**, and scale-freedom must come from **H_eff-tracking** rather than clustering. **C-5 survives on the standard route.**
> **Long-range affinity** ⇒ non-Gaussianity **survives the averaging**, and **0730's wall applies to C-5 directly** (scale-free but non-Gaussian by 10²–10³ in excess kurtosis — the cascade's fate).

**This is narrower and more computable than what it replaces.** The question moved from *"is the unstacking random?"* — which the founder has now answered — to *"over what range is it correlated?"*

## What the founder supplied
A walk-and-talk (11 Sep), dictated and transcribed, **converted into a coherent statement at his request** and filed at `founders_voice/founder_mechanism_scp_differential_affinity_2026-09-11.md`. **Kept separate from the assessment**, so his account and the conclusions drawn from it do not blur.

**The mechanism.** An **SCP** is the **entire stack on one GP**, and it carries a **composition** — a proportion of eCPs to qCPs varying site to site, making **each SCP a distinct entity**. Sorting by composition gives **Q-dominant** and **E-dominant**.

> **Q-dominant SCPs attract Q-dominant strongly; Q-to-E is weaker; E-dominant SCPs are indifferent, attracted equally to both.**
> **One class discriminates and the other does not** — *"the Q-dominant SCP is the asymmetric attractor."*

**And a second skew reinforces it** (easy to miss — it arrives late in the dictation): opposite-charge qCPs enter **ZBW oscillation** and form **persistent qDPs**; eCP pairs form eDPs that are *"not faithful"* and **pair-swap** readily; and **qDP pair-swapping binds all three via the strong force** (two minus flanking a centre plus). **Affinity governs what meets what; persistence governs what survives the meeting. Both tilt the same way.**

## What it does to C-5
**It breaks the 3892 Poisson warning — with a mechanism, not a denial.** Differential affinity is **preferential attachment**: a site's propensity to accrete depends on what it has already accreted. **Correlated by construction; cannot be Poisson.** And it is the **right class of process** — rich-get-richer generically produces **power-law, scale-free** statistics, which is exactly what the spectrum needs.

**But it brings the 0730 wall.** Preferential attachment also generically produces **heavy tails**, which is precisely what disqualified the chain-of-chains cascade. **Recorded now, while the mechanism is fresh and attractive, rather than after work is built on it.**

**The escape is arithmetical, not hopeful:** at the pivot, H⁻¹ = 5.2×10⁴ l_P ⇒ 1.4×10¹⁴ Planck spheres per Hubble volume × 1.8×10⁷⁴ CPs each = **2.6×10⁸⁸ CPs per observable mode**, hence **≥10⁶⁴ SCPs per mode for any plausible stack number.** CLT flattens heavy tails at that multiplicity **unless correlations reach far enough to defeat it.**

*(The stack number was again carried as a parameter, not invented — **third session running** on that quantity.)*

## C-5's debts, current
1. ~~The referent~~ — discharged 3890.
2. ~~The reservoir~~ — discharged 3892.
3. **The amplitude — now the correlation length of the affinity. THE GATE, and in-lane.**
4. **Adiabaticity** vs Planck's isocurvature bound.

## Owed (elsewhere)
- **Isak:** recompile **EU-1 (V1.6)** and GR-2 (V2.11).
- **Maintainer:** CONV-046 — **the sector has a live candidate with a derived ζ and a stated microphysics**; the amended DE escalation (3858); cosmic-web owed piece (3833); `DM_project_map.md` stale (3884).
- **EU-1 V1.7 (bundle):** 3854 VSL clarification; 3876 §5 as qualified by 3878. **Do not add C-5.**

**Anti-priorities:** **do not report C-5 as working**; **do not let scale-freedom carry Gaussianity** — they are separate tests and 0730 is the precedent for failing the second while passing the first; **no calibration against an observable** (PD-007); **never supply the stack number**; follow **§0.5 D-1…D-6**; no cross-lane edits without sanction; do not retire 3710; **nothing in this arc refutes n_s** — PRED-C-96 reads 0.9654 (V1.6).

## §15 Steps A–H
- **A** `session_logs/2026-09-11_session_206_log.md` (3895). **B** transcript row 3894. **C** development vignette (Session 206).
- **D** Tier 4: `reasoning/3894_scp_affinity.md`.
- **E** Registries: `research_frontier.md` (3894 prepend); `id_block_registry.md` (next free 3896); `future_projects.md`; in-place answer at `reservoir_mechanism.md` §6b. N/A: `predictions.md`, `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md` — **C-5 is live, not adopted**; nothing moved.
- **F** none (no panel). **G** no PD minted; founder mechanism converted and registered. **H** this file.

## Governance note
**Two things were done deliberately and should be repeated.**

**The conversion was kept separate from the assessment.** A dictated proposal turned into prose is easy to blend with the worker's conclusions about it; filing his account in `founders_voice/` and the evaluation in `eu1_derivation/` keeps the boundary legible to whoever reads next.

**The new risk was recorded in the same patch as the good news.** Preferential attachment buys scale-freedom and threatens Gaussianity by the same property. Writing the second half while the first is fresh is the only reliable time to do it — after a session or two of momentum, a known hazard reads as pessimism rather than bookkeeping.
