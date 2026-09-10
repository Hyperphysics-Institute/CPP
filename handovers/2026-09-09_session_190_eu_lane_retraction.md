# EU-lane Handover — Session 190 Close (9 Sep 2026) — 3860 half two retracted; 3816 restored; the arc's base is intact

**Patch 3863. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3861 at session start; 3862–3863 delivered as patch files. **Next free: 3864.** GR lane: next free 3715.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).

## Read this before anything else
**3860's half-two failure is RETRACTED. 3816 stands. The arc's base is intact.** If you inherited a summary saying the Moment-1 count is unsupported, that summary is one patch out of date.

## The single most important next action
**OPEN-EU-BATH-DEPTH-1** — the last substantial item that is local, unblocked and needs nothing from outside the lane. It owns **κ = kT_bath/E_Pl**, which is exactly what T-2's residual reduces to (3850 §5): T-2 delivered λ = α/κ, so every remaining uncertainty in the O(α) correction — and hence in EU-1's quoted theory error — is κ's.

Everything else in the lane is **maintainer-gated**: CONV-046 dispatch; the amended DE escalation (3858); `cosmic_web_generation_constraints.md` owed-piece 1 (3833).

## What was done this session
**3862 — retraction**, founder-directed ("check the axioms and founders_voice … see if that leaves any ambiguity").

**The mechanism was on file for a month:**
- **R-OUTWARD-FANOUT** (founder clarification, Patch 3135, 14 Aug): *at every **hop** a GP's received DI-bit count splits equally among all outward-radial neighbours*; the ~10% shell thickness is variation in **hop count** from GP_origin to GP_PSR. **Propagation is a multi-hop cascade, and the hops are WITHIN the Moment** — the PSR *is* the per-Moment reach.
- **D-SUBPSR-FIELD pass 3** (same patch; verify `scripts/3133_subpsr_cascade.py`) **computed it**: N = 6–22 hops, band σ_r/⟨r⟩ = 0.093–0.076 reproducing the founder's ~10%, and the profile stated outright — **"the steady-state signal MAXIMIZES inward, 1/s²-class."** OPEN-SUBPSR-1 is recorded as *substantially RESOLVED at the field-profile level*.

**Two retractions:**
1. 3860 §2's *"the relay requires prior-Moment content, so it cannot operate at Moment 1"* — **wrong**. Within-Moment hop cascade; no prior content needed.
2. 3860 §3's *"the sub-Moment escape is closed by founder ruling"* — **misread**. The ruling says only that **ZBW** is not sub-Moment; it is silent on propagation hops.

**And the Moment-1 count is positively supported:** AP-4 has every GP emit **the same fixed number of DI-bits every Moment** — unconditional, independent of what was received — and SSV_abs is **count-like**. **n̄ is a count**, so what Moment-1 contact must deliver is exactly what the unconditional emission plus the hop cascade do deliver.

**⇒ 3816 RESTORED; its §6 check returns POSITIVE; n̄_init = N_CP is a derivation, not a posit; N_* = ⅓ln N_CP stands; 3823, 3825, 3835 and 3837 inherit no conditionality.** In-place flags at `occupancy_regrounding.md` §2c and `c4_mass_bound.md` §3b **corrected**. 3860's founder picture question **withdrawn** — answered before it was asked.

**3860 half one STANDS** and remains that patch's real contribution: "deposit exactly once" is **forced** by emission-budget conservation, and the shell locus gives **1/r² from counting alone**.

**Residual (narrow, recorded not inflated):** at Moment 1 the E and S vectors are previous-Moment snapshots, so first-Moment bits carry **count without direction**. Bears on ignition *dynamics*, not on n̄.

## Forward queue
1. **OPEN-EU-BATH-DEPTH-1** (above). The last substantial local item.
2. **Maintainer:** CONV-046 dispatch; the amended DE escalation; the cosmic-web owed piece.
3. **EU-1 V1.7 (small, bundle):** the §Background VSL clarification (3854). **No repair note is needed — 3816 stands.**
4. **Residual observation** (first-Moment directional content) — an ignition-dynamics question; not urgent.

**Anti-priorities:** no calibration against an observable (PD-007); **do not re-open 3816's basis**; no cross-lane edits without sanction; do not retire 3710; do not report anything in this arc as a refutation of n_s — **PRED-C-96 has never moved.**

## §15 Steps A–H
- **A** `session_logs/2026-09-09_session_190_log.md` (3863). **B** transcript row 3862. **C** development vignette (Session 190).
- **D** Tier 4: `reasoning/3862_ap4_retraction.md`.
- **E** Registries: `research_frontier.md` (3862 prepend, verified single); `id_block_registry.md` (next free 3864); `future_projects.md`; in-place corrections at `occupancy_regrounding.md` §2c and `c4_mass_bound.md` §3b. N/A: `predictions.md` (never moved), `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md`.
- **F** none (no panel). **G** no PD minted; founder direction recorded. **H** this file.

## Governance note — the rule that needed strengthening
**Three times in this arc the corpus already held what a session set out to establish:** C-4 (3847 — the chirality sector held the refutation before C-4 was proposed); VSL (3854 — the premise had been withdrawn seven patches before it was named as the escape); and this one.

**This third instance is the most serious**, because the first two merely wasted a session while this one **produced a false negative against sound work** and annotated two documents with it before the founder caught it.

The 3854 discipline — *re-read the patch that registered an item* — **is not sufficient**. The strengthened rule:

> **Before declaring any protocol failure, search the corpus for the MECHANISM the clause names — not merely the item's history.** AP-4c names "the relay recursion"; a search on that phrase would have found R-OUTWARD-FANOUT and D-SUBPSR-FIELD in one step.
