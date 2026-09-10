# EU-lane Handover — Session 185 Close (9 Sep 2026) — EU-1 V1.6 shipped; the quoted value moves; one substantial item left

**Patch 3853. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3851 at session start; 3852–3853 delivered as patch files. **Next free: 3854.** GR lane: next free 3715.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile** — note the version, it is no longer V1.5). GR-2 V2.11 (**Isak owes the recompile**).
**Parallel windows:** none known.

## The single most important next action
**OPEN-EU-EFOLD-BUDGET-1 — the VSL horizon computation.** This is the last substantial item in the lane. The 3823 audit found the re-grounded count delivers ~64.5 e-folds against a requirement of ~75 to inflate the pre-ignition ball to the observable universe — a **~10.5 e-fold shortfall**, with the whole ball landing at 0.39 Mpc today against an observable 14,260 Mpc.

That audit assumed a **fixed-c horizon integral**. EU-1's background is explicitly FRW/**VSL**, and a varying signal speed changes the horizon integral — it is the only route that moves the *requirement* rather than the supply. It has been owed since 3823 and repeatedly deferred behind the amplitude arc, which is now finished.

The other routes are worse and are recorded at 3823 §4: lower reheating raises the requirement (so 75 is a floor); the only non-VSL fix is a GP hierarchy ≥ ~10³² per l_P against an unverified 10³⁰ estimate that yields just 70.4.

## What was done this session
**3852 — EU-1 V1.6, substantive.** The first version in this arc to change the paper's headline rather than its scaffolding.

- **(a) T-2 enacted (3850).** Abstract and title block rewritten. λ = α/κ *exactly*; κ ≤ 1 because the bath runs on the substrate clock, so λ ≥ α; at the bath clause λ = α, η = 1.43×10⁻², **Δn_s = +5.0×10⁻⁴**, and η > 0. **Quoted value: 0.9649 ± 5×10⁻⁴ → n_s = 0.9654** (0.12σ_Planck — agreement unchanged in quality, but a different claim). A §Problem Status note carries the derivation, the empirical by-product **kT_bath ≳ 0.1 E_Pl**, and the point that the residual is κ, already a counted leg — **no new theory error, framework legs stay three**.
- **(b) The amplitude closure entered the paper (3847).** A second dated note: the spectator prescription has no identified mechanism; all seven candidates named and closed; the structural obstruction stated; three exits, **none a candidate search**. States explicitly, twice, that **the tilt is untouched** and this concerns A_s only.
- **Registry propagation, deliberately deferred from 3850 so the registry follows the paper:** `predictions.md` PRED-C-96 → **0.9654 (one-sided)** with the prior value preserved in place, plus a dated log line; `changelog-EU-1.md` V1.6; `paper_regeneration_ledger.md` A5 → 1.6; `paper_catalog.md` → 1.6.
- **Compile:** pdflatex ×2, **16 pages, 0 errors, 0 undefined**.
- **Unchanged:** the tilt derivation, Eq. Nstar, the count law, every section structure, and the swarm count.

## Charter status
**All three of OPEN-EU-1's frozen targets are discharged** — T-1 (3820), T-2 (3850), T-3 closed negative (3847) — and both the positive and the negative are now in the paper. The charter arc is complete.

## Forward queue
1. **The VSL horizon computation** (above). Last substantial item.
2. **CONV-046 dispatch — maintainer's call.** The package now carries **T-1 and T-2 as positives** alongside the 3835 no-go, the 3837 conflict and the 3847 closure. A panel seeing only the negative would get a skewed picture of a ten-session arc that produced two delivered targets and one characterised gap.
3. **AP-4's shell-clause derivation** — still owed; load-bearing for the Moment-1 count.
4. **OPEN-EU-BATH-DEPTH-1** — now more valuable: κ is what T-2's residual reduces to, and this item owns κ.

**Cross-lane: one item outstanding** — `cosmic_web_generation_constraints.md` owed-piece 1 (3833).

**Anti-priorities:** no calibration against an observable (PD-007 — the kT_bath bound is an observation *bounding* a parameter, not a fit); **do not open an eighth amplitude candidate** (3835 forbids exactly that reflex); no cross-lane edits without sanction; do not retire 3710; do not report the amplitude closure as a refutation of n_s.

## §15 Steps A–H
- **A** `session_logs/2026-09-09_session_185_log.md` (3853). **B** transcript row 3852. **C** development vignette (Session 185).
- **D** Tier 4: N/A — 3852 is an enactment of results derived and captured at 3847 and 3850; no new derivation, so no new reasoning fragment. (Reasoning rider satisfied by `reasoning/3847_chir_excursion.md` and `reasoning/3850_t2_coefficient.md`.)
- **E** Registries: `predictions.md` (PRED-C-96 row + dated log line — **the deferred item from 3851 §E is now discharged**); `research_frontier.md` (3852 prepend, verified single); `changelog-EU-1.md`; `paper_regeneration_ledger.md`; `paper_catalog.md`; `id_block_registry.md` (next free 3854); `future_projects.md`. N/A: `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md`.
- **F** none (no panel). **G** no PD minted; no founder ruling. **H** this file.

## Governance notes
- **The registry followed the paper, not the reverse.** 3851 flagged that `predictions.md` still carried the old value and deliberately left it; 3852 moved it once the paper said so. Worth keeping as the pattern.
- **When a number in print changes, change it in print.** The abstract and title block were rewritten rather than leaving the old value standing with a note appended somewhere later.
- **Isak's owed recompile is now V1.6, not V1.5.** Two versions have landed since the last canonical build.
