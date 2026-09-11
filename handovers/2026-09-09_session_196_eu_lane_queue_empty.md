# EU-lane Handover — Session 196 Close (9 Sep 2026) — the last open item is resolved; **the EU queue is empty in fact**

**Patch 3875. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3873 at session start; 3874–3875 delivered as patch files. **Next free: 3876.** GR lane: next free 3715.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).

## Read first
`bootup.md` **§0.5** (Step 1, priority 1.5), then this section.

**Every item the handovers have carried is now delivered, closed with a reason, or resolved.** Previous handovers said the lane's substantive work was complete *while still listing one genuine candidate*; that candidate was worked this session and resolved. **The queue is empty in fact, not only in description.** If you are looking for a task list, there isn't one, and that is the state of the lane rather than an omission.

## What was done this session
**3874 — OPEN-EU-BATH-DEPTH-1 resolved.** The last candidate: does the substrate bath thermalize occupations fast enough at **depth ~10⁷⁴**?

- **D-1 half-paid.** The test is already at **0769 §(b)**: **R = N_mix·(H/E_Pl) ≪ 1**, and with N_mix = O(10–30) toy-measured (0753), R ~ 4×10⁻⁴. **But 0769 established that for the *generic* case.** Depth is the item's whole content, and mixing times generally grow with system size — so the item was **correctly scoped when registered**, and the handovers were right to keep it even while mis-describing what it owned (3866 corrected that).
- **The threshold is sharp and there is no middle ground:** R = 1 at **N_mix = 5.2×10⁴**. O(1) → R = 3.9×10⁻⁴ (2600/e-fold). **O(ln n̄) → R = 3.3×10⁻³ (304/e-fold).** O(√n̄) → fails by **32 orders**. O(n̄) → fails by **69 orders**. Either the margin is large or the bath clause is annihilated and with it the Gibbs ln n̄ the tilt rests on.
- **The resolution is structural, from AP-3.** Per-Moment synchrony (ratified 2982): **every GP executes P→C→D every Moment and every CP displaces every Moment.** The substrate is **massively parallel, one actor per CP** — never serial (no queue, no single agent stepping through occupants) and not single-agent diffusive (all CPs act simultaneously). **Those are exactly the two failing scalings, excluded by construction rather than by assumption.** Parallel mixing of n items by n actors is **O(log n)**, so **N_mix ~ ln n̄ ~ 170**, **R = 3.3×10⁻³**, **~300 re-thermalizations per e-fold at depth 10⁷⁴.** Margin ~300.
- **Detail worth keeping:** the depth penalty is exactly **ln n̄ = 3N_rem** — the count law's own logarithm. Generic → depth 10⁷⁴ costs ≈8.5× in mixing time and nothing else.
- **Scope, graded deliberately:** N_mix's *value* remains toy-measured (0753); this fixes its **scaling**, argued from parallelism rather than simulated at depth. **Grounded, not proven** — the same grade 0769 claimed for the bath clause itself, because a sub-question should not outrank its parent. **Nothing added to the conditionality.**

## Owed — the whole remainder of the lane, and none of it worker work
- **Isak:** recompile **EU-1 (V1.6)** and GR-2 (V2.11). Two versions since the last canonical build.
- **Maintainer:** **CONV-046 dispatch** (the 3835 no-go, 3837 conflict and 3847 closure as the negative; **T-1 and T-2 as positives**; the 3868 audit strengthens the negative); the **amended DE escalation** (3858 — the counting bound with three exits, re-pointed to the DE lane's completion); **`cosmic_web_generation_constraints.md` owed-piece 1** (3833).
- **Founder:** **OPEN-EU-SEA-REFERENT-1's EU half** — does EU-1's n̄ count the DP-Sea itself, or the excess occupancy above a non-diluting sea? A picture question, **load-bearing for the paper's central dilution mechanism**, and the only physics question left open in the lane.
- **EU-1 V1.7 (small; bundle, do not ship for it alone):** the §Background VSL clarification (3854).

## Forward queue
**Empty.** If work is wanted here, it must come from a founder direction or a maintainer decision, not from the queue. **Do not manufacture an item** — the handovers have said "the substantive work is complete" for four sessions while still carrying a candidate; that candidate is now gone, and the honest statement has no hedge left in it.

**Anti-priorities:** follow **§0.5 D-1…D-6**; **do not manufacture an item**; no calibration against an observable (PD-007); do not re-open 3816's basis (restored 3862); do not tidy neighbouring axiom wording (3872's lesson); no cross-lane edits without sanction; do not retire 3710; **nothing in this arc refutes n_s** — PRED-C-96 has never moved and reads **0.9654** (V1.6).

## §15 Steps A–H
- **A** `session_logs/2026-09-09_session_196_log.md` (3875). **B** transcript row 3874. **C** development vignette (Session 196).
- **D** Tier 4: `reasoning/3874_bath_depth.md`.
- **E** Registries: `research_frontier.md` (3874 prepend); `id_block_registry.md` (next free 3876); `future_projects.md`. N/A: `predictions.md`, `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md` — the result is grounded, not a theorem, and adds no conditionality.
- **F** none (no panel). **G** no PD minted; no founder ruling. **H** this file.

## Governance note
**Three items in this arc were resolved not by new physics but by reading the protocol properly** — exactly-once deposit (3860, emission-budget conservation), resident-sourced E (3870, bootstrap impossibility), and now depth-independent mixing (here, per-Moment parallelism). In each case the question was *what must be true for the protocol to work at all*, and in each case the protocol already answered it.

That is the third payoff from the same move, and it is cheaper than any candidate search. **Ask what the protocol forces before asking what mechanism might suffice.**
