# SS-8 Transaction-Indexed Transcript

**File:** `transcript-SS-8.md`
**Paper:** SS-8 — Interstitial-neutron binding in alpha-cluster nuclei
**Role:** Transaction-indexed pointer-map for every substantive transaction in SS-8's development. Each entry names the transaction and points to the artefact that holds its verbatim content. The transcript is a roadmap, not an archive — the substance lives at the pointer targets.
**Companion files:** `handover-SS-8.md` (current state), `development-SS-8.md` (session vignettes). See `templates/operating_system.md` §11 for the three-file convention.

---

## Conventions

**Transaction ID:** three-digit zero-padded, monotonically increasing, never reused (`001`, `002`, ...).
**Entry format:** `[ID] [date] — [one-line description] → [pointer or "see vignette N"]`
**Pointer target:** a committed file, or a vignette ID in `development-SS-8.md`, or "(no artefact — decision recorded inline)."
**Append-only.** Transactions are never renumbered. If a transaction is later invalidated, record the invalidation as a new transaction pointing back to the invalidated ID.

---

## Transaction log

### Phase 1 / Phase 1b (20–21 April 2026)

- `001` 20 April — Phase 1 empirical map produced (12×5 grid + odd-A + Ca chain + ⁶Li) → `scripts/ss8_empirical_map_extended.py`, `scripts/ame2020_loader.py`, `scripts/ss8_polytope_enumeration.py`, `sketches/SS-8_Phase1_extended_map_findings.md`
- `002` 20 April — Framing decision (B + C; interstitial alongside valence-pair; light-side in scope) → see vignette 1
- `003` 21 April — Phase 1b identifies 2E/V = 6 − 12/V scaling law; Model A inventoried → see vignette 2
- `004` 21 April — Deltahedra gap at N_α = 11 noted; C4 refined as graph-simplicial not polytope-deltahedral → see vignette 2

### H2' derivation note and Round 1 (21 April 2026)

- `005` 21 April — Axiom verification discipline applied; initial A5+A8'+A11 shorthand discovered wrong on verbatim reading → see vignette 3
- `006` 21 April — H2' derivation note written with three-layer epistemic split → `sketches/SS-8_H2prime_derivation_note.md`
- `007` 21 April — OPEN-SS-26, OPEN-SS-27, OPEN-SS-28 opened as structural sub-problems → recorded in sketch §10
- `008` 21 April — Round 1 Copilot review received → `reviews/round1_copilot.md`
- `009` 21 April — Round 1 Grok review received → `reviews/round1_grok.md`
- `010` 21 April — Round 1 ChatGPT review received; H2'/²H notation collision misread identified → `reviews/round1_chatgpt_initial.md`
- `011` 21 April — ChatGPT re-review request letter drafted and sent → `letters/SS-8_chatgpt_rereview_request_letter.md`
- `012` 21 April — ChatGPT Round 1 re-review received; error acknowledged, retraction and re-review against correct target delivered → `reviews/round1_chatgpt_corrected.md`
- `013` 21 April — Case 2 archived in `templates/relationship_protocol.md` → see templates/relationship_protocol.md §6

### OPEN-SS-26 attack (22 April 2026)

- `014` 22 April — Dual-model approach designed (Model A counting, Model B Yukawa) → see vignette 5
- `015` 22 April — Script `ss8_ssv_minimization_sketch.py` produces gap factors ≥ 1.5× across both polytopes and both models → `scripts/ss8_ssv_minimization_sketch.py`
- `016` 22 April — D1 SSV-minimization sketch written; D1 proposed as conditional theorem → `sketches/SS-8_D1_ssv_minimization_sketch.md`
- `017` 22 April — D1-D2 coupling identified; OPEN-SS-26 → OPEN-SS-27 consolidation proposed (but not adopted) → recorded in sketch §5
- `018` 22 April — Commit-cadence rule adopted in `templates/operating_system.md` (section-end + context-pressure triggers) → see templates/operating_system.md §11 "Commit cadence"

### Round 2 review cycle (22 April 2026)

- `019` 22 April — Round 2 review request letter drafted with Q1–Q7 → `letters/SS-8_Round2_review_request.md`
- `020` 22 April — Round 2 Copilot review received (Q1–Q7 answered) → `reviews/round2_copilot_on_review_request.md`
- `021` 22 April — Round 2 Grok review received (Q1–Q7 answered) → `reviews/round2_grok_on_review_request.md`
- `022` 22 April — Round 2 ChatGPT reviews of D1 sketch, review request letter, and Q2 analysis target received → `reviews/round2_chatgpt_on_D1_sketch.md`, `reviews/round2_chatgpt_on_review_request.md`
- `023` 22 April — ChatGPT document-mismatch noted; ChatGPT reviewed Case 2 re-review letter instead of Round 2 request (context-conflation pattern, distinct from Case 2's notation-collision) → see vignette 7
- `024` 22 April — ChatGPT document-mismatch correction letter drafted; NOT sent due to Thomas-side workflow skip (feedback-discipline failure, see `AI_team_expectations.md` §1.1) → artefact exists in session transcript only; not committed

### Q2 algebraic reduction test (22 April 2026)

- `025` 22 April — ChatGPT's Q2 test executed; Model B shown non-reducible to Model A on three discriminators → `scripts/ss8_Q2_algebraic_reduction_test.py`
- `026` 22 April — Q2 algebraic reduction analysis written → `sketches/SS-8_D1_Q2_algebraic_reduction_analysis.md`
- `027` 22 April — Round 2 Q2-analysis review received from Grok → `reviews/round2_grok_on_Q2_analysis.md`
- `028` 22 April — Round 2 Q2-analysis review received from Copilot → `reviews/round2_copilot_on_Q2_analysis.md`
- `029` 22 April — Round 2 Q2-analysis review received from ChatGPT; Level-1/2/3 independence decomposition proposed → `reviews/round2_chatgpt_on_Q2_analysis.md`

### Round 2 closure (22 April 2026)

- `030` 22 April — Level-1/2/3 refinement adopted across sketch, Q2 analysis, H2' note → see vignette 7
- `031` 22 April — Round 2 synthesis letter drafted → `letters/SS-8_Round2_synthesis_letter.md`
- `032` 22 April — OPEN-FRONTIER question registered conceptually (not yet added to Research_Frontier.md): "Can D1 be derived from a non-proximity-based mechanism?" → pending in handover-SS-8.md as next-session item

### Context-pressure preservation + structure cleanup (22 April 2026)

- `033` 22 April — Context-pressure preservation checklist adopted in `templates/operating_system.md` → see templates/operating_system.md §11
- `034` 22 April — Intermediate registry-suite triggers adopted in `templates/operating_system.md` → see templates/operating_system.md §11
- `035` 22 April — Curated development narrative committed (file `development-SS-8.md` at flat location; renamed in transaction 040) → see vignette 8
- `036` 22 April — bootup.md §8.5 Active Work Pointer rule adopted (partial fix for chronic turnover problem) → see bootup.md §8.5
- `037` 22 April — Fresh-context Claude critique of bootup §8.5 identifies remaining stale-content issues → see vignette 8
- `038` 22 April — bootup.md demotion of stale §7/§8/§12 to pointers; §3 generic; series_masses removed → see bootup.md
- `039` 22 April — Per-paper subfolder convention adopted in `templates/operating_system.md` §11; SS-8 first paper → see templates/operating_system.md §11 "Per-paper subfolder convention"
- `040` 22 April — Three-file documentation-suite convention adopted (handover / development / transcript) → see templates/operating_system.md §11
- `041` 22 April — SS-8 fully migrated to per-paper subfolder; `development-SS-8.md` renamed to `handover-SS-8.md` → this file and sibling files
- `042` 22 April — `templates/AI_team_expectations.md` created with initial entries → `templates/AI_team_expectations.md`
- `043` 22 April — 10 verbatim reviewer files committed to `SS-8/reviews/` with catalog README → `reviews/`, `reviews/README.md`
- `044` 22 April — Git-Bash-Patch workflow documented in `templates/operating_system.md` §13 → see templates/operating_system.md §13
- `045` 22 April — Documentation-continuity three-hierarchies rule adopted in `templates/operating_system.md` §11 → see templates/operating_system.md §11 "Documentation continuity"

---

## How to use this file

**Looking for a specific piece of content?** Scan the transaction descriptions and follow the pointer. Most substantive content lives in standalone artefacts.

**Reconstructing chronology?** Transactions are date-ordered. For narrative of reasoning and choices, read `development-SS-8.md` vignettes. For specific reviewer wording, go to the `reviews/` files pointed at by transactions 008–012 and 020–029.

**Adding a new transaction?** Append with the next sequential ID. Never renumber. If the transaction invalidates a prior one, point back to the invalidated ID rather than editing the original.

**Missing pointer (e.g., transaction 024).** Indicates an artefact that was drafted in session but never committed. These are flagged for a future recovery session; the session transcript retains the content but outside git. Recovery action should be logged as a new transaction pointing back to the original.
