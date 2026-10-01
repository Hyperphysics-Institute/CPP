# Session 241 detail — the α arc's local position invariance, the DI-bit landing rules, and the black-hole calibration (4352–4362)

Earlier in the window (4335–4351): the pre-deposit list was worked to completion (roadmap items 0, 1, 3, 7), the trial
deposit was recognised as done (its DOIs owed by Isak), the prediction tally (108) was annotated by standing, the claim
wording sweep ran, the compile pass reached 121/122, and R-CP-NO-REST-MASS was registered (4350) and confirmed (4351).
See `pre_deposit_roadmap.md`'s work log.

## The arc, patch by patch
| Patch | What happened | Standing |
|---|---|---|
| 4352 | Independent critic of 4317–4332: 4330 tested the target position, not the step, so its "solid band → LPI passes" was an artefact. Fill 0.72–0.80. Lange 2021 bound adopted; on-shell running; c03 v2.3. | LPI pass withdrawn |
| 4353 | Founder's landing protocol (fly to GP_PSR; blocked bits move inward) tested: literal reading leaves spokes; neighbourhood reading (F2) solid at N ≳ 3× outer shell; simplest order-free rule S. | tested |
| 4354 | Founder: sideways first (F2) → **R-DIBIT-INWARD-FILL**; nothing beyond the PSR; far field by re-radiation. Claude's particle-relay model gave Gauss automatically. | rule registered; cross-section result later withdrawn |
| 4355 | Founder: "look at AP-4". The registered relay (AP-4 snapshot; AP-3/A3′ PSR-shell mean; GR-1j exact statics) makes the window automatic and Gauss a theorem. Claude: far field ∝ Q/R³ → k_α = −3 unless the PSR ball is full. | k_α = −3 withdrawn at 4359 |
| 4356 | Founder: the black hole is the one-bit-per-GP limit → **R-DIBIT-COUNT-AT-FLOOR** (N = GPs in a ball of radius l_P/2); band 4.35% of the PSR. Full-ball route closed. | rule registered |
| 4357 | Founder: 2–10% came from his zigzag-path calculation; 4% needs a reference stress (zero stress). Two clocks explained (3703: Sea lapse → 0, matter lapse ½, c/2). Black-hole density stops in DRAIN's Planck-density speck. N ≈ 5×10⁸⁹ on c01's grid. | recorded |
| 4358 | Claude: the clock test is ordinary space; computed "annual α swing 8×10⁷ above the bound". Founder's black-hole interior picture (TODO-4358-BHLATTICE). | exclusion withdrawn at 4359 |
| 4359 | Founder: DP-Sea uniform, not pulled by gravity; DPs orient → **R-DPSEA-UNIFORM**; Sea screening cannot cancel. **Second critic:** 4355's fixed-count premise would make G vary with position (~10⁴ vs lunar laser ranging); GR-1j never states its source rule; A3′ asserts metric coupling. | 4355–4358 withdrawn; TODO-4359-SOURCERULE |
| 4360 | Founder: nothing pushes the GPs; α is a ratio kept invariant by the Lorentz proportioning the GPs compute; fixed DI-bit count → **R-ALPHA-LORENTZ-RATIO**. Quantified: invariance iff PSR³·SSV_abs constant; first order k·SSV_abs,0 = 1/3; second order 2 vs Mercury's ½. | mechanism registered; checks owed |
| 4361 | Founder: ½ is a calibration; the band gets the same message (4360's effect is per volume). **Third critic:** k is a convention but k·SSV_abs,0 is physical and undetermined (needs 1/3 to 10⁻⁸); ε linear in the harmonic census; exact invariance → β = 5/2; approximate → α swing ~2–3× bound. | tension confirmed |
| 4362 | Founder: the Moment is absolute; one DI-bit hop per Moment, GP_origin → GP_PSR; local time slows by PSR contraction → one PSR does both jobs. Tension stands. Bootup §3 container-hygiene rule. | session close |

## What a critic should look at first
- 4360's (a/R)³ dilution is the premise everything rests on; the source rule (TODO-4359-SOURCERULE) can change it.
- 4357's N ≈ 5×10⁸⁹ vs 4301's 9×10²⁸ (TODO-4362-NRECONCILE).
- 4356's identification of "maximum compression" with the corpus's l_P/2 floor is Claude's, not the founder's number.

## Lessons for the next window
- **Treat mass and charge by one rule** (A3′). Three of Claude's results this window failed because charge was treated
  differently from mass; each was caught only by a fresh critic. Send any result that claims an exclusion to a critic
  before presenting it.
- **The founder's physical pictures are usually already in the registered axioms** (AP-4, AP-5, 3703). Read them before
  modelling.

## §15 Step A–H Completion Audit (Patch 4362, completed at Patch 4363)
- **A (Tier 1 session log):** ✓ `session_logs/2026-10-01_session_241_log.md` (4363).
- **B (Tier 2 transcript pointers):** ✓ `session_logs/transcript-cross-paper.md` entries 079–084 (4363); founder text in `founders_voice/` (edited for clarity per the transcript rule).
- **C (Tier 3 vignette):** N/A — the α/DI-bit work is foundations (axiom_maturation), not paper-scoped; the paper revisions of 4340–4349 and c03 v2.3 were wording/status edits recorded in each paper's version history, not new paper-scoped reasoning.
- **D (Tier 4 reasoning):** ✓ per-patch fragments `series_standard_model/axiom_maturation/4352–4362` with verify scripts `series_standard_model/code/4352–4360` (4359, 4361, 4362 are critic/ruling fragments without scripts).
- **E (registries):** todolist ✓ (deferral gate PASS on all 28 patches; 4351 a legitimate NOTHING-DEFERRED); research_frontier ✓; axiom-registry ✓ (R-CP-NO-REST-MASS, R-DIBIT-INWARD-FILL, R-DIBIT-COUNT-AT-FLOOR, R-DPSEA-UNIFORM, R-ALPHA-LORENTZ-RATIO; count 9); theory-overview ✓ (α row restated at 4359); `frontier_sectors/EW.md` ✓ (4363); `future_projects.md` ✓ (4363); pre_deposit_roadmap ✓; paper_catalog ✓ (4340–4349); OSF queue/manifest ✓ (regenerated at 4352 after c03); predictions N/A (no new prediction; α a calibration); theorem-registry N/A; master_glossary N/A; methods_catalogue N/A (the fresh-critic discipline is protocol, filed as D-14); organizational_frontier N/A.
- **E′ (reasoning-capture audit):** physics patches 4352–4362 all captured. 4335–4351 are programme/paperwork patches; the tools they shipped (`overview_staleness_gate.py`, `claim_wording_sweep.py`, `compile_pass.sh`) are infrastructure. **Named gaps:** 4347 shipped `series_strong/code/4347_ss7_lo_cpp_variant.py` (SS-7 fully-CPP RMS 1.77%) with the finding recorded in SS-7 v1.7 and the roadmap but no fragment; 4341's SF-2 arithmetic erratum is recorded in the paper's erratum only.
- **F (reviewer artifacts):** ✓ the three fresh-context critic returns, verbatim, at `series_standard_model/reviews/2026-09-30_session_241_critic_returns_verbatim.md` (4363).
- **G (protocol/OS):** ✓ bootup §3 container-hygiene rule (4362); bootup §0.5 **D-14** (one rule for every A3′ channel; exclusions to a fresh critic first) (4363).
- **H (handover document):** ✓ boot card + this detail (4362, same-session fix-up at 4363); kickoff line and orientation echoed in chat.

