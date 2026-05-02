# Tier 4 Reasoning Archive — SS-7 v1.2

**Paper:** SS-7 v1.2 (Alpha-Cluster Regime and the 3N−6 Edge Formula for Medium-Mass Nuclei)
**Tier:** 4 — substantive Opus reasoning verbatim, housekeeping excluded but no compression
**Companion files:**
- Tier 2 pointer-map: `transcript-SS-7.md`
- Tier 3 vignettes: `development-SS-7.md`, `handover-SS-7.md`
- Tier 2/3 hybrid: `SS-7_v1.2_transcript.md` (curated narrative covering Sessions 1–10, 417 lines)
**Created:** 1 May 2026 (retroactive recovery from one chat-window)

---

## Scope note — partial recovery

This file is a **partial Tier 4 recovery** for SS-7 v1.2. Only one chat-window's content was surfaced for retroactive Tier 4 extraction during the May 2026 recovery effort: the **post-compaction Session 10 (registry cascade)** of 21 April 2026. The pre-compaction sessions that constitute the actual v1.2 development arc (Sessions 1–9, 20–21 April 2026) — covering OPEN-SS-22 registration as a split from OPEN-SS-18, the SS-8 Phase-1 exploration that surfaced the isotope-selection artifact in v1.1's Table 2, the three-reviewer verification cycle (ChatGPT, Copilot, Grok), the OPEN-SS-22 retirement decision and split into OPEN-SS-23 and OPEN-SS-25, the v1.2 paper-body and companion revision execution, and the start of the registry cascade — are **not preserved at Tier 4 fidelity** in this file.

The reasoning behind those Sessions 1–9 conclusions is recoverable at **Tier 2/3-equivalent fidelity** from:

- `series_strong/papers/SS-7/documentation_suite/SS-7_v1.2_transcript.md` (417 lines, curated narrative covering all ten sessions; Sessions 1–9 curated by the in-session participant, Session 10 curated post-compaction)
- `problem_histories/PH-OPEN-SS-22.md` (the retirement narrative itself, full Tier-3-equivalent capture of the substantive physics decisions)
- `series_strong/papers/SS-7/SS-7_alpha_cluster_edge_formula.tex` CHANGELOG (v1.0/v1.1/v1.2 transition history)
- `series_strong/papers/SS-7/letters/` and `series_strong/papers/SS-7/reviews/` (the three reviewer verification responses + the verification-letter exchange)
- `series_strong/papers/SS-7/SS-7_v1.1_G3_discrepancy_note.md` (the 20 April registration that triggered the v1.2 cycle)

If chat-window content for Sessions 1–9 surfaces later, this file will be **appended** in a subsequent recovery patch following the same SS-8-precedent recovery-order convention. As of this file's creation, the Session 10 content below stands alone.

The six physics-and-methodology-substantive turns extracted from Session 10 are: (1) the three v1.2 .tex drift bug identification (paper-integrity QC discipline), (2) the **Pattern 6 articulation** — the genuinely registry-level physics observation that crystallized during axiom-registry.md work, (3) the PRED-C-28/29 duplicate-ID resolution, (4) the structural-drift broader pattern that extended Lesson #5, (5) the cross-registry counting-convention mismatch identification, and (6) the explicit scope-discipline three-category articulation that became Lesson #8.

---

## Session 10 — Post-compaction registry cascade, 21 April 2026

*[Recovery context: the v1.2 cycle ran the pre-compaction session to context exhaustion at the end of Session 9 (registry propagation partial: Research_Frontier.md complete, predictions.md partial, eight Section C items still pending). A fresh Opus session (Session 10) opened with a handoff document and worked through the remaining Section C items (C1, C2, C3, C7, C8, C9, C10, C11, C12), did three v1.2 .tex drift fixes that surfaced during integration, ran an H2 cross-consistency verification pass, updated the curated transcript with the Session-10 additions, and drafted the SS-8 kickoff briefing for the next context window. The substantive turns below are extracted from that work — explicitly excluding the routine registry-edit mechanics, the URL-fetch handshake friction, and the post-fetch commit-message housekeeping that fill most of the chat record.]*

### Three v1.2 .tex drift bugs: title block, §1.3 first bullet, §6 SS-7 line (post-revision QC)

*[Note: when Thomas uploaded the v1.2 .tex confirming it was indeed the v1.2 file produced in the pre-compaction Session 9 (vs. the v1.1 file initially uploaded by mistake), the Session-10 Opus's first substantive task was to verify the .tex was internally consistent before moving to companion work. Three v1.1→v1.2 drift bugs surfaced — bugs that didn't change the paper's claims but would visibly contradict its own content on the title page and in two prose sections. The reasoning below is the paper-integrity QC discipline that turned the v1.2 paper from "functionally complete but visibly v1.1 on title page" to truly v1.2.]*

Confirmed — this is v1.2. The CHANGELOG header, the twelve-row Table 1 ending at ⁵⁶Ni, the OPEN-SS-22 retirement language, the new OPEN-SS-25 registration, the traceability footnote Table 2 with the v1.1 non-N=Z rows — all the markers the handover described are present. RMS 0.80% across the twelve.

Before moving to companion work, three small v1.1-artifact bugs in the v1.2 .tex itself that you should know about:

**Title block (around line 180 of the .tex):** the `\title{}` still reads `Version 1.1 --- 20 April 2026 (post round-2 external review)`. The PDF title page will show "Version 1.1" even though everything inside the paper says 1.2. This is the most visible one — a reviewer opening the PDF sees v1.1 on the title page.

**§1.3 "What SS-7 delivers", first bullet:** says "Eight concurrent zero-parameter predictions... (N_α = 3,…,10)" listing the original eight nuclei, then in the next sentence says "all twelve use the same two constants... twelve concurrent matches at ≤1.5%." The bullet header and the paragraph contradict each other — one says 8, the other says 12. The list of nuclei in the display math is also the original 8.

**§6 Discussion, "nuclear-chart mapping" subsection:** the SS-7 line still reads "Eight predictions within 1.5%, plus re-derivation of ⁸Be." Should be twelve.

These are exactly the kind of residual v1.1→v1.2 drift that a thorough find-replace pass would catch, and they're the sort of thing a reviewer would flag immediately on the next round. None of them threaten the paper's claims — Table 1, abstract, Main Result box, and §5.1 are all internally consistent at twelve. But the bugs do exist in the .tex you have.

*[Outcome: Thomas authorized fixing all three. The corrected v1.2 .tex compiled clean to 25 pages and was committed as the canonical v1.2 paper file. The discipline that made this catch matter — checking that the title-block version metadata matches the body content even when the body is internally consistent — is not captured at Tier 3 in any committed artefact, since the committed v1.2 .tex shows only the corrected state, not the deliberation. This is the kind of post-revision QC content that the Tier 4 archive exists to preserve.]*

---

### Pattern 6 articulation: B_pair = M₀/φ recurs across three scales without rescaling (the load-bearing physics turn)

*[Note: this is the only genuinely physics-substantive turn in the entire Session 10 chat. It surfaced during axiom-registry.md C2 work, late in the session, when the registry's existing Patterns section forced explicit articulation of an observation that had been implicit across SS-5 v6, SS-7 v1.0, and SS-7 v1.2 but never registered as programme-level. The articulation produced both a new entry in the axiom-registry Patterns section and a registered open question about whether the recurrence is structurally necessary or merely allowed. This is the load-bearing physics turn the recovery instructions said to prioritize.]*

Got it. Analysis: SS-7 v1.2 doesn't introduce new programme-level axioms (C1–C4 are paper-level hypotheses per Thomas's honesty principle), but it does add 12 new quantitative predictions — which triggers C2's "introduced new predictions" clause. The Prediction Ledger needs rows #40–51, counts need updating, and the Axiom Trajectory growth table needs a new SS-7 row.

[Routine ledger and growth-table updates executed.]

Add a sixth pattern observation capturing the SS-7 finding: B_pair = M_0/φ recurs across three physical scales (nucleon-nucleon contact in SS-5, ⁴He closure bonus in SS-5, alpha-alpha contact in SS-7). This is programme-level insight about how the axioms behave across sectors, which is what this section is for.

**Pattern 6 — B_pair = M₀/φ recurs across three scales without rescaling.** Same numerical quantum (2.342 MeV), same axiom derivation (A5 × A8'), no rescaling, no new parameter between scales:

- SS-5: nucleon-nucleon contact (the original derivation site)
- SS-5: ⁴He closure bonus (the same quantum reappearing as the alpha-particle binding closure)
- SS-7: alpha-alpha contact at K₃ collective mode (the same quantum reappearing at the alpha-cluster scale)

Open question registered: whether the recurrence is **structurally necessary** across scales (i.e., the axioms force B_pair = M₀/φ at any scale where the K₃-mode bonding mechanism applies) or **merely allowed** by the axiom set (i.e., the axioms permit the same numerical value without forcing it).

*[Outcome: Pattern 6 entered the axiom-registry.md Patterns section as the sixth registered programme-level observation. The "structurally necessary vs merely allowed" open question became a candidate OPEN-G-N entry pending the OPEN-G-N nomenclature formalization. This is genuinely registry-level physics, not just execution. The articulation here was load-bearing for SS-8's Phase-1+1b empirical-map work the next day, where the 2E/V scaling law's match to (6 − 12/V) × B_pair (preserved at Tier 4 in `reasoning-SS-8.md` Pre-Session-0) used the same B_pair quantum at a fourth scale (alpha-vertex K₃-edge interstitial-neutron coordination). Pattern 6 is the bridge observation between SS-5/SS-7 and SS-8.]*

---

### PRED-C-28/29 duplicate-ID resolution: renumber the SS-2 pair to PRED-C-29a/29b

*[Note: surfaced during predictions.md C6 finishing-touch work. A pre-existing typo predating v1.2 — PRED-C-28 and PRED-C-29 each appeared twice (once for SS-3 gauge-group structural predictions at lines 65–66, once for SS-2 Λ_QCD and μ_neutron predictions at lines 68–69). The Session-9 Opus had flagged this in the pre-compaction handoff as needing resolution but didn't pick the resolution. Session 10 had to make the choice.]*

Now, fix the duplicate PRED-C-28 and PRED-C-29 IDs. Looking at the table, the collision is:

- Lines use PRED-C-28 for "SU(3) is the unique gauge group" (SS-3) AND for "Λ_QCD" (SS-2)
- Lines use PRED-C-29 for "No exotic gauge group" (SS-3) AND for "μ_neutron" (SS-2)

**The cleanest fix: renumber the two SS-2 entries (Λ_QCD and μ_neutron) to PRED-C-29a and PRED-C-29b.** That keeps the SS-3 entries at PRED-C-28/29/30 contiguous, and the SS-2 duplicates get the suffix treatment the handoff suggested. I'll pick this over shifting because shifting would propagate through to PRED-C-30 which is already in use for a SS-3 entry, and through subsequent rows — cleaner to suffix the two offending rows.

*[Outcome: SS-2 pair renumbered to PRED-C-29a/PRED-C-29b in predictions.md. The Section 6 cross-reference for SS-2 was also updated to match the new IDs. The choice between renumber-SS-2 and shift-SS-3-and-everything-downstream is a methodologically substantive scope-discipline decision — the renumber-SS-2 path touched 4 rows and 1 cross-reference; the shift path would have propagated through PRED-C-30, PRED-C-31, PRED-C-32...PRED-C-41 and required updating Section 6 cross-references for SS-3, SS-5, and any downstream files referencing those IDs. The preference for minimal-blast-radius edits over "consistent forward numbering" was load-bearing for the rest of Session 10's discipline.]*

---

### Section 6 SS-3/4/5 gap finding: scope-creep self-correction (the discipline that produced Lesson #8)

*[Note: while adding the SS-7 row to predictions.md Section 6 "Predictions by Paper" table, the Session-10 Opus noticed that SS-3, SS-4, and SS-5 had no rows in Section 6 either, despite contributing prediction entries that appear in Section 1. The reasoning below is the explicit scope-discipline articulation — initially adding the missing SS-3/4/5 rows (factually correct), then reverting because the handoff was narrow ("just add SS-7"), then flagging the gap as observation rather than silently fixing it. This articulation became Lesson #8 in the curated transcript.]*

Wait — let me reconsider that last edit. The handoff was explicit: just add the SS-7 row. I went and also added SS-3, SS-4, SS-5 rows because they're factually missing from Section 6 despite existing in Section 1. That's scope creep, even if it's arguably correct scope creep. Let me scale it back to exactly what was asked and flag the other gap as an observation rather than silently fixing it.

[Revert executed.]

One scope decision worth flagging: while fixing Section 6, I noticed SS-3, SS-4, and SS-5 have no rows at all — even though they contribute PRED-C-28-30, PRED-C-31, and PRED-C-32-41 respectively (all present in Section 1). I initially added rows for them, then reverted because the handoff said "SS-7 needs a row," not "complete the table." So Section 6 still has an SS-3/SS-4/SS-5 gap that predates v1.2 — a separate cleanup task, not part of this work. **Flagging it rather than silently fixing it.**

*[Outcome: this articulation produced the explicit three-category convention that became Lesson #8 in `SS-7_v1.2_transcript.md`: **fix silently** (when the fix is in scope and trivially uncontroversial); **fix with note** (when the fix is in scope but worth surfacing — the typical case); **flag without fixing** (when the fix is out of scope but worth noting for future work). The convention is not just bookkeeping — it's the discipline that prevents a registry-cascade session from quietly accumulating editorial decisions that drift from the explicit handoff scope. The same convention shaped subsequent v1.2 work on theorem-registry.md (where the SS column miscount was fixed-with-note, the new theorem was fixed-silently, and adjacent gaps were flagged-without-fixing) and on axiom-registry.md (where the growth-table SS-4/5/6 row gap was flagged-without-fixing rather than silently backfilled).]*

---

### The structural-drift broader pattern: extending Lesson #5

*[Note: the cross-consistency H2 verification pass at the end of Session 10 surfaced multiple instances of pre-existing latent drift across files — not just the Research_Frontier.md drift that Session-9 Lesson #5 had flagged. The pattern was structural: stale headers, miscounts, growth-table gaps, all predating v1.2 and persisting through the 20 April template consolidation that Session 9 had assumed would catch them. The reasoning below is the broader-pattern articulation that extended Lesson #5.]*

Pre-existing drift pattern larger than Session 9 diagnosed:

Transcript Lesson #5 flagged Research_Frontier.md as having latent drift (5 registrations claimed but never propagated through v1.0/v1.1). The H2 cross-consistency pass in this session found this was indeed broader:

- **theorem-registry.md** Summary Statistics had a pre-existing +1 miscount on the SS row (listed as 9 theorems, actual was 10); this was separate from SS-7 v1.2's addition and was a correction not backfilled when SS-3's THEO-SS-10 + PROP-SS-11 were added
- **founders_vision.md** header date was stale at 11 April despite catalogue content through 18 April (never updated during the SS-5 v6 / SS-6 v0.1 cycle)
- **cpp_references.bib** header date was stale at 2 April despite SS-5 v6 and SS-6 v0.1 entries post-dating that
- **axiom-registry.md** Axiom Trajectory growth table stops at SS-2 — never got SS-4, SS-5, or SS-6 rows, so it's been reading "Total: 28+" while the prediction ledger reads 35+

Each of these was fixed in this session with an explicit note in the file; the pattern confirms **Lesson #5 should read "latent drift is structural, not just Research_Frontier-specific — the 20 April template consolidation was necessary but not sufficient, per-file stale-header discipline is also needed."**

*[Outcome: Lesson #5 extended in the curated transcript with the four-file pattern. The methodological lesson: the 20 April template consolidation was a structural fix at the templates level, but per-file stale-header discipline at the files level is a separate concern that template-level consolidation does not solve. Both are necessary; neither is sufficient. This shaped the four-tier documentation discipline added to operating_system.md §4 on 26 April (six days later), which separated structural files from per-file working files at the discipline level rather than just at the file-organization level.]*

---

### Cross-registry counting-convention mismatch: 36+ vs 31+ vs 47+

*[Note: surfaced during the H2 cross-consistency verification pass at session end. The three canonical "total predictions" numbers across the registry layer reached non-mutually-consistent values after SS-7 v1.2's +12 increment — not because the increment was wrong (each file consistently added 12), but because each file uses a different decomposition convention. Identified as a programme-record loose end predating v1.2.]*

One cross-file counting note worth your awareness, not a defect: The three canonical "total predictions" numbers across the registries now read **36+ (theory-overview.md), 31+ (CPP_the_theory.md), and 47+ (axiom-registry.md)**. Each file has its own decomposition convention — theory-overview counts rows in its Strongest Quantitative Results table; CPP_the_theory uses its narrative scorecard; axiom-registry breaks out structural unboundness as separate entries. All three incremented by +12 for SS-7 v1.2, which is internally consistent. If you want a single unified number across all files, that's a separate normalisation pass — happy to do it as an agenda item for a future session if useful.

*[Outcome: identified as a programme-record loose end. Not fixed in v1.2 because the three numbers are internally consistent within each file's decomposition convention; mutual consistency across files would require a normalization-pass decision about which decomposition is canonical, which is a programme-level governance question not a v1.2 paper-cycle concern. The three numbers (36+/31+/47+) remained at this level until further normalization work. Flagging this as a separate agenda item rather than silently rationalizing it was an application of the Lesson #8 convention.]*

---

*End of Session 10 content. The six substantive turns above preserve the verbatim Opus reasoning behind committed artefacts in twelve registry files (theory-overview.md, axiom-registry.md, theorem-registry.md, master_glossary.md, predictions.md, paper_catalog.md, founders_vision.md, future_projects.md, CPP_the_theory.md, cpp_references.bib, problem_histories/PH-OPEN-SS-22.md, and the SS-7 v1.2 .tex) plus the SS-7_v1.2_transcript.md curated transcript update. The deliberation captured here — particularly Pattern 6 articulation, the scope-discipline three-category convention, and the structural-drift broader pattern — is not preserved at Tier 3 in any of those committed files; the committed files state the conclusions, the Tier 4 archive preserves the reasoning that produced them.*

*Additional Session-10 content covering the SS-8 kickoff briefing draft, the routine registry-cascade execution mechanics, and the H2 cross-consistency check results (all 7 checks green) is preserved at Tier-3-equivalent fidelity in the committed artefacts (`SS-7_v1.2_transcript.md` Session-10 entry, `series_strong/papers/SS-8/` files including the kickoff briefing whose content was used as starting context for SS-8's Pre-Session-0 work the next day, and the registry files themselves) and is not duplicated here. The SS-8 kickoff briefing reasoning specifically is captured in `series_strong/papers/SS-8/documentation_suite/reasoning-SS-8.md` Pre-Session-0 since that briefing became the input to SS-8's Phase-1+1b empirical-map session.*

---

## What remains uncovered (recovery completeness)

**Sessions 1–9** of the SS-7 v1.2 cycle (20–21 April 2026, pre-compaction) — the actual development arc — are **not preserved at Tier 4 fidelity** in this file. Specifically uncovered:

- The OPEN-SS-22 registration as a split from OPEN-SS-18 during SS-7 v1.1 completion (20 April)
- The G3 RMS discrepancy registration (`SS-7_v1.1_G3_discrepancy_note.md`, 20 April)
- The SS-8 Phase-1 empirical-map exploration that surfaced the v1.1 isotope-selection artifact (21 April morning) — *partially* recoverable from `reasoning-SS-8.md` Pre-Session-0, since that work began before the SS-8 paper was scoped and the SS-7 v1.2 cycle and the SS-8 Pre-Session-0 work overlapped
- The three-reviewer verification cycle (ChatGPT, Copilot, Grok) and the convergence on retirement interpretation (a) — preserved at Tier 3 in `letters/` and `reviews/` files
- The OPEN-SS-22 retirement decision and the split into OPEN-SS-23 (neutron-excess) + OPEN-SS-25 (DP-sea Coulomb screening) — preserved at Tier 3 in `problem_histories/PH-OPEN-SS-22.md`
- The v1.2 paper-body and Table 2 traceability-footnote revision execution — preserved at Tier 3 in the v1.2 .tex CHANGELOG
- The eight-file SS-7 documentation suite v1.1→v1.2 update execution — preserved at Tier 3 in the documentation-suite files themselves

If chat-window content for any of Sessions 1–9 surfaces in future recovery work, this file will be appended in subsequent recovery patches following the chronologically-by-recovery-order convention established in `reasoning-SS-8.md`.

**Programme-record significance:** SS-7 v1.2 is the **first retired open problem in the CPP programme record** — OPEN-SS-22 → ✗ RETIRED, 24 hours after registration. The retirement narrative articulation in `CPP_the_theory.md` Part VII Chapter 22 ("The First Retired Open Problem") and the parallel `problem_histories/` folder establishment are programme-level firsts that future retirements will inherit as precedent. The Tier 4 reasoning behind those programme-level firsts is in Sessions 1–9, not Session 10, and is therefore one of the highest-priority recovery targets if Sessions 1–9 chat-window content surfaces.

---

## Sessions 1–9 — Pre-compaction v1.2 development arc, 20–21 April 2026 (chronologically prior to Session 10)

*[Recovery scope addendum: this section appends content from a chat-window provided by Thomas in the May 2026 recovery effort, covering the **pre-compaction** Sessions 1–9 of the SS-7 v1.2 cycle — the actual development arc that produced the v1.2 paper, the OPEN-SS-22 retirement, the seven-companion update suite, the Research_Frontier propagation, and the predictions.md partial cascade. These sessions are chronologically **before** Session 10 (post-compaction registry cascade) which is preserved higher in this file. Listed here last because added in recovery order; the Tier 2 transcript (`SS-7_v1.2_transcript.md`) handles full chronological ordering. With this append, the partial-recovery scope note at the top of this file is updated: **Sessions 1–9 are now partially recovered at Tier 4 fidelity**, while still being preserved at Tier 2/3 fidelity in `SS-7_v1.2_transcript.md`.*

*Most substantive output from these sessions is preserved at full Tier-3 fidelity in committed artefacts: the v1.2 paper itself (`SS-7_alpha_cluster_edge_formula.tex` v1.2, commit 7ce5015 → 837eed5 → onwards), the seven companion files (glossary/philosophy/mechanism/keywords/phenomena/reviews/development-SS-7.md), the retirement narrative (`problem_histories/PH-OPEN-SS-22.md`), the three reviewer verification responses (`series_strong/papers/SS-7_v1.2_{chatgpt,copilot,grok}_verification_response.md`), the verification-letter exchange (`series_strong/papers/SS-7_v1.2_reviewer_verification_letter.md`), the Research_Frontier and predictions.md propagations, the `templates/paper_completion_checklist.md` extraction (commit 837eed5), and the Phase-1 empirical-map script (`series_strong/papers/ss8_empirical_map.py`). The ten physics-and-methodology-substantive turns below capture the **deliberation** behind those committed conclusions — the alternatives considered, the framings revised, the diagnostic insights — which the committed artefacts state but do not record.*

---

### Session 2 — Template extraction Step 1 audit: the Section C drift was structural, not isolated (20 April 2026)

*[Note: the v1.2 cycle began with a template extraction work order — consolidating three overlapping post-completion task enumerations (operating_system.md §4.10, operating_system.md §10, paper_production_workflow.md §9) into a single authoritative checklist. Step 1 was an audit of the union list. The Opus's reasoning at the audit's conclusion is substantive because it discovered that the surface drift Thomas had diagnosed (problem_histories/ missing from §4.10 Section C) was one instance of a larger structural pattern.]*

Step 1 audit complete. The headline finding: the drift Thomas diagnosed (problem_histories/ missing from §4.10 Section C) is one instance of a larger pattern. §4.10 Section C lists five registry files; §10 lists eleven content/registry files. Six additional items are missing from the atomic checklist, not just problem_histories/:

- theory-overview.md
- theorem-registry.md
- master_glossary.md
- future_projects.md
- CPP_the_theory.md
- bibliography/cpp_references.bib

This plus a fourth fragmented enumeration I found (the copy-template at paper_production_workflow.md lines 269-301) changes the scope of the work slightly. I've stopped at Step 1 rather than proceeding to Step 2 because three of my findings raise policy questions beyond the work order's explicit scope.

**Four questions before I build the checklist:**

1. **Section C scope** — expand to all twelve content/registry documents in §10, or stay at the narrow five from §4.10? (My strong recommendation: expand, or the same drift pattern will produce another miss on a different file. But confirming with you.)
2. **Navigation documents** (README.md, INDEX.md, series README) — not in §4.10 at all. Fold into C or make a separate block?
3. **Source D** — the fourth enumeration I found. Reduce to pointer, or leave alone?
4. **G5 → C8 repositioning** — moving founders_vision.md from final-verification to content-update. Minor but worth confirming.

*[Outcome: Thomas approved all four (expand C to 12 items; navigation as separate Section D; Source D reduced to pointer; G5→C8). The expanded checklist is what `templates/paper_completion_checklist.md` shipped with in commit 837eed5. The structural-drift discovery in this turn is the same pattern that resurfaced in Session 9 (Research_Frontier registry drift) and was then explicitly extended in Session 10 as the "Lesson #5 broader pattern" — see Session 10 above for the extended formulation. The audit here was the first surface of what would become the cross-session structural-drift programme-record observation.]*

---

### Session 3 (morning) — The Phase 1 vs Phase 2 distinction: discovery before drafting (21 April 2026)

*[Note: after the template extraction landed and Grok's PDF-vs-tex review issue was diagnosed (preserved below), Thomas asked "I think we are ready to write v0.1 for SS-8. What do you think?" The Opus's pushback is substantive because it produced the Phase 1 exploration discipline that surfaced the Table 1 isotope-selection artifact later that same morning. Without the pushback, SS-8 v0.1 would have been drafted on the assumption that OPEN-SS-22 was real physics; the entire v1.2 retirement cycle would not have happened.]*

On SS-8 v0.1 — I want to push back gently before we commit.

By the workflow document, v0.1 comes out of Phase 2 (drafting), which is fed by Phase 1 (exploration and discovery). The question isn't whether SS-8 *could* be drafted; it's whether the discovery phase is complete enough that drafting produces a paper rather than a hypothesis sketch.

**What SS-7 gives us as the starting point for SS-8:**

- **Empirical fact:** flat −2 to −2.5% residuals at ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe (N_α = 12, 13, 14)
- **Registered as OPEN-SS-22:** "new physics activates at icosahedral closure"
- The signature (flat residual, not smooth growth) argues for structural onset rather than gradual breakdown

**What I don't yet have a clear picture of:**

- **The mechanism.** Why does the simplicial edge count under-predict at N_α = 12? The icosahedron is simplicial (20 triangular faces, 3·12−6 = 30 edges), so the edge-count rule naïvely should apply there too. Something additional is active.
- **The candidate formula.** Is it an additional binding term per face (icosahedron has 20 faces vs tetrahedron's 4), per 5-fold vertex (icosahedron's vertices are 5-coordinate vs tetrahedron's 3-coordinate), a φ-ratio correction because the icosahedron carries the golden ratio intrinsically, or something else?
- **The prediction set.** What does the mechanism predict for N_α ≥ 12 beyond just "matches the three observed residuals"?

If you have the mechanism worked out in your head already — which given the 39-year development arc is plausible — then we're ready for Phase 2 drafting and I need you to share it. If the mechanism is still being probed, we're ready for a Phase 1 exploration session, which produces the mechanism, then drafts from it.

Which is it? What's your current picture of why the icosahedral regime breaks the 3N−6 rule?

*[Outcome: Thomas wrote, "I wish I could give you some insight into this problem, but I can't. This is a new concept for me, and I haven't had the time for my intuition to develop around this problem." The Opus then proceeded with Phase 1 exploration (empirical map first, mechanism second). This decision is the load-bearing methodology for the entire v1.2 cycle — without it, the Table 1 isotope-selection artifact would not have been discovered. The "Phase 1 first" discipline is now codified in the workflow but at the time of this turn was an active push against expedience.]*

---

### Session 3 (midday) — THE Table 1 isotope-selection artifact discovery (load-bearing physics turn) (21 April 2026)

*[Note: this is THE physics-substantive turn of the entire SS-7 v1.2 cycle. After the Phase 1 exploration started building the empirical map, the Opus discovered that the paper's Table 1 — specifically lines 777-780 listing the N_α = 12, 13, 14 anchors as ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe — was making an isotope-selection error. ⁴⁸Cr (Z=N=24) is the actual N=Z alpha-chain nucleus at N_α=12, not "(not N=Z)" as the paper had annotated. The paper had substituted neutron-rich isotopes (+4 neutron excess) and skipped the strict alpha-chain nuclei. Under the actual N=Z chain, the "structural onset at N_α=12" disappears entirely. This single discovery launched OPEN-SS-22's retirement — the first retirement in CPP programme history.]*

Major finding before mechanism speculation. I need to stop the investigation and bring you this.

**The "structural onset at N_α = 12" that SS-7 registers as OPEN-SS-22 appears to be an artifact of isotope choice, not physics.** The empirical map changes what SS-8 should be about.

**What the paper's Table 1 does, line 777-780:**
```
48Cr  12  30  409.82  ---     (not N=Z)       ← skipped, labeled "not N=Z"
48Ti  12  30  409.82  418.70  -2.12%          ← used instead
52Cr  13  33  445.14  456.35  -2.46%
56Fe  14  36  480.46  492.25  -2.40%
```

**Two problems with this table:**

(1) The annotation "(not N=Z)" on ⁴⁸Cr is wrong. ⁴⁸Cr is Z=24, N=24 — it IS N=Z. The paper substituted ⁴⁸Ti (Z=22, N=26, with +4 neutron excess) and skipped the actual alpha-chain nucleus. ⁴⁸Cr's binding energy exists in AME 2020 (411.462 MeV); it's not missing data, it was excluded by mistake.

(2) ⁵²Cr (N-Z = +4) and ⁵⁶Fe (N-Z = +4) are also not strict alpha-chain. The N=Z counterparts are ⁵²Fe and ⁵⁶Ni respectively.

**When you run the formula against the strict N=Z alpha-chain, the "structural onset" disappears:**

| N_α | Paper's choice | residual | N=Z alpha-chain | residual |
|---|---|---|---|---|
| 12 | ⁴⁸Ti | +2.12% | ⁴⁸Cr | +0.40% |
| 13 | ⁵²Cr | +2.46% | ⁵²Fe | +0.57% |
| 14 | ⁵⁶Fe | +2.40% | ⁵⁶Ni | +0.73% |

The N=Z alpha-chain at N_α = 12, 13, 14 is in family with the primary set (RMS 0.91% for the primary set; 0.52% for N_α = 11–14 strict alpha-chain). **No structural onset visible in the actual alpha-chain data.**

The "extra binding" in the paper's chosen nuclei is roughly 7–9 MeV per nucleus, which is exactly what you'd expect from adding 4 neutrons each (a neutron-excess effect, not an icosahedral-closure effect).

Tentative data above N_α = 14 (⁶⁰Zn, ⁶⁴Ge — AME values I'd want you to double-check before committing): residuals continue smoothly, trending slightly toward overprediction (−0.15%, −0.94%). Not a sharp onset at N_α = 12.

**Secondary finding (confirms G3):** the primary set RMS with my AME values is 0.91%, matching the G3 discrepancy note exactly. The paper's cited 0.88% is the seven-nucleus value excluding ²⁰Ne.

**What this means for SS-8 scope:** If this holds under your verification, OPEN-SS-22 as currently framed ("icosahedral closure activates at N_α = 12") is probing a pattern that isn't in the alpha-chain data. The real question is OPEN-SS-23 territory: how does the formula extend to N > Z nuclei? The paper's ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe residuals are 4-extra-neutron data points; they belong in the non-alpha-chain regime.

This doesn't mean icosahedral closure physics is irrelevant — the icosahedron IS geometrically special at N_α = 12, and there may yet be something interesting there. But whatever it does, it does not produce a visible 2% deviation in the actual alpha-chain.

*[Outcome: Thomas chose "(D) verify the data first, (C) fold into SS-7 v1.2 first" — the most cautious path. This launched the three-reviewer verification cycle (Session 4–5 below). All three reviewers independently confirmed the finding (Session 5 below). The retirement decision followed (Session 6 below). The retirement narrative committed in `problem_histories/PH-OPEN-SS-22.md` states the finding as established; this Tier 4 turn preserves the moment of discovery before verification, with the explicit "if this holds under your verification" caveat that gates everything downstream.]*

---

### Session 3 (afternoon) — The line 340 self-application discovery: "we failed to apply our own standard" (21 April 2026)

*[Note: during the scope audit that prepared the v1.2 revision plan, the Opus discovered that the paper's own §1.5 already declared neutron-excess as outside scope. The authors had the awareness in principle. The Table 1 substitution was an oversight against their own stated standard, not a deliberate scope claim. This framing — "failed to apply our own standard" rather than "didn't know" — is methodologically substantive about how the v1.2 retirement gets articulated.]*

Key finding from the audit: line 340 of the paper already states that neutron-excess is separate physics ("No neutron-excess treatment... requires separate mechanism"). **The authors knew this in principle.** The Table 1 choice was an oversight, not a deliberate claim. That makes Branch A stronger.

Also found: a natural split in OPEN-SS-22's original scope. The structural-onset hypothesis (retired) is distinct from the DP-sea screening question (still valid physics). Recommend creating a new OPEN-SS-25 for the screening question so that work isn't lost.

*[Outcome: line 340 was preserved verbatim in the v1.2 revision rather than rewritten — making the Branch A correction land as "we failed to apply our own standard" rather than "we didn't know." This honest framing is captured at Tier 3 in the v1.2 paper's CHANGELOG and in `philosophy-SS-7.md`'s "Honest assessment" subsection. The natural OPEN-SS-22/OPEN-SS-25 split surfaced here became a load-bearing distinction for the retirement narrative — see Session 6 below for the formal retirement decision that operationalized this split.]*

---

### Session 4 — The Grok PDF-vs-tex diagnosis: input-channel failure looks like reviewer-level failure until diagnosed (21 April 2026, prior to verification cycle)

*[Note: before the v1.2 verification cycle launched, Grok had returned a review of SS-7 v1.1 that contained a specific numerical error: writing "φ^(1/2) − 1 ≈ 4.1%" where the paper says "φ^(1/z) − 1 ≈ 4.1%" with z ≈ 12 the 600-cell coordination number. The Opus initially diagnosed this as vocabulary contamination from Grok's older training. Thomas pushed back: he had given Grok the PDF, not the .tex; the "z" had likely been visually misread as "2" through superscript font rendering. The same error pattern had appeared in Copilot under the same input channel. This input-channel-vs-framework-memory diagnostic insight is methodologically substantive.]*

Your PDF-vs-.tex diagnosis is almost certainly right. 1/z rendered as a superscript in the PDF's math font at that size is visually very close to 1/2 — a lowercase z with its curved bottom serif, shrunk into a superscript, blurs against the digit 2 in most fonts. Copilot making the same error through the same input channel is the clinching data point. **That's an OCR-class artifact, not a framework-memory issue.**

**Protocol implication:** reviewers should receive .tex source, not the compiled PDF. The .tex preserves the symbol exactly as typed. This belongs in operating_system.md §4 (Phase 4 submission protocol) — something like "Reviewer submissions: send the .tex file; mention the PDF is available if requested but do not lead with it."

**Revised rehabilitation assessment:** Grok's substantive reading was solid. Suspension reasoning may have over-attributed to vocabulary contamination what was actually input-format degradation. Worth re-testing on a future paper with .tex-only input before deciding.

*[Outcome: the .tex-only submission protocol was operationalized in the v1.2 verification letter (Session 4 below) and was explicitly cited there as the reason for sending .tex source. Grok's rehabilitation was successfully tested by the v1.2 verification cycle (Session 5 below) — substantive content was clean once the input channel was fixed. This diagnostic also produced Lesson #4 in the curated transcript ("input-channel failures look like reviewer-level failures until diagnosed"), which Session 10's Lesson #5 extension built upon. Without this diagnosis, Grok would likely have remained suspended and the v1.2 verification cycle would have run with two reviewers instead of three — losing the third independent confirmation that gave the retirement decision its weight.]*

---

### Session 4 — Reviewer verification letter design discipline: explicit non-prejudgment of (a)/(b)/null (21 April 2026)

*[Note: when Thomas authorized "proceed with D & C as recommended" (Branch D verify-first, Branch C fold-into-v1.2), the Opus drafted the verification letter that would go to all three reviewers. The design choices below are methodologically substantive about how to structure a verification request that doesn't bias the verdict.]*

**SS-7_v1.2_reviewer_verification_letter.md** — the letter to send to both ChatGPT and Copilot. Key design choices I made that you can adjust:

- **Addressed to both reviewers together** rather than drafting two per-reviewer variants. The verification task is the same for both; personalized closing can be added per-recipient at the end if you prefer.
- **Instructs them to work from the .tex, not the PDF**, explicitly citing the 1/z vs 1/2 reading failure as the documented reason. This operationalizes the protocol change we established earlier today.
- **Presents my numbers openly**, so reviewers check against specific values rather than re-discovering them. Accepts the risk they'll anchor on my numbers; my judgment is that getting them to verify is more important than getting them to derive from scratch, and if my numbers are wrong the reconciliation step will surface it.
- **Task 3 offers both interpretations (a) and (b) without prejudging**, and explicitly invites them to say "I can't think of a defensible reason for (b)" as a valid answer. I don't want to trap them into confirming my conclusion.
- **Task 4 separates the line-777 data error from the broader question** — whichever way Task 3 resolves, the ⁴⁸Cr row is wrong and must be corrected.

*[Outcome: the letter shipped to all three reviewers (Grok was added per the rehabilitation context). All three returned independent (a) verdicts (Session 5 below). The "explicit null-answer option" design choice is what makes the three-reviewer convergence load-bearing as a retirement criterion rather than mere endorsement — by structuring the letter to make "I disagree with your finding" a clean valid response, the convergence on (a) becomes evidence rather than confirmation bias. This design discipline became the template for what `philosophy-SS-7.md` later articulated as "symmetric-honesty verification cycle" — a structurally distinct review mode from standard reviewer rounds.]*

---

### Session 5 — Three-reviewer convergence on Branch A (21 April 2026, evening)

*[Note: ChatGPT, Copilot, and Grok independently returned (a) verdicts on the verification letter. The Opus's synthesis below captures the substantive process differences across the three reviewers and the rehabilitation update for Grok. The three-reviewer convergence is what made retirement (rather than reframing) the defensible choice.]*

Three independent confirmations. This is a clean Branch A outcome.

| | Task 1 (AME) | Task 2 (residuals) | Task 3 (interpretation) | Task 4 (line 777) |
|---|---|---|---|---|
| **Copilot** | ✔ exact match | ✔ to the keV | (a) | both errors |
| **ChatGPT** | ✔ consistency with tables | ✔ step-by-step match | (a) | both errors |
| **Grok** | ✔ AME 2020 cross-check | ✔ exact match | (a) | both errors |

No reviewer constructed a case for interpretation (b). That's the cleanest possible outcome for a finding that questions the paper's own framing — three reviewers going to (a) without prompting is strong evidence the original Table 1 choice was a mistake, not a defensible call we missed.

**Notable differences among the three responses, briefly:**

- **Copilot** gave the most rigorous per-nucleus arithmetic and the sharpest summary ("Interpretation (a) is correct. The empirical anchor for OPEN-SS-22 disappears"). Strongest endorsement of the v1.2 plan.
- **ChatGPT** was honestly scoped: "I cannot live-query AME 2020, so I'm validating by consistency with standard mass tables and known binding trends." Values confirmed to 0.01–0.02 MeV rather than to the keV. Offered a specific sentence for the paper: "The previously observed −2% residual plateau at Nα ≥ 12 is attributable to neutron-excess binding and does not indicate a structural transition in the α-cluster model." That sentence is good; I'd recommend adopting it in §5.1 verbatim or near-verbatim.
- **Grok** claimed verification against AME 2020 mass_1.mas20.txt and went +0.006 MeV on ⁴⁸Cr (411.462–411.468 MeV). The answer is right; the claim to have accessed the official AME file I'd treat as optimistic rather than fact-checking it — the content is correct either way. More interesting: Grok co-signed the review with "Benjamin, Lucas, Harper" as a "full team verification."

**Overall:** Grok's rehabilitation test on this round passed on substance. Format still has residual contamination. Safe to keep using; still worth keeping it in the rotation rather than making it primary.

*[Outcome — corrected: Thomas later clarified that "Benjamin, Lucas, Harper" are not vocabulary contamination — they are the names of four agents in Grok's environment that independently answer questions and report back. This revised the rehabilitation assessment upward: Grok was cleaner than the Opus credited. The ChatGPT sentence ("attributable to neutron-excess binding and does not indicate a structural transition") was adopted near-verbatim in the v1.2 §5.1 rewrite. The three-reviewer convergence became the retirement criterion that authorized OPEN-SS-22's retirement — making this Session 5 the load-bearing decision-gate for the entire v1.2 cycle.]*

---

### Session 6 — Retirement decision: retire vs recycle the identifier, with natural OPEN-SS-22 → OPEN-SS-25 split (21 April 2026)

*[Note: with three-reviewer convergence on Branch A, the Opus needed to decide how to handle OPEN-SS-22. Three options were viable: retire the identifier and document via PH-file; recycle the identifier for new content; quietly delete without documentation. The reasoning below is the precedent-setting decision for how CPP handles retirement events — the first such event in programme history.]*

**Decision 8: Retire rather than recycle OPEN-SS-22's identifier.** Documents the retirement-vs-recycling choice and why identifier-recycling would have been worse-than-both-worlds. Explicitly rejects "quietly delete without documentation" as worst option.

The reasoning: an identifier in CPP's registry has a documented meaning ("heavy-nuclei icosahedral closure onset at N_α≥12"). Recycling that identifier for new content (e.g., the OPEN-SS-23 neutron-excess work) would create a discontinuous historical record where readers searching for OPEN-SS-22's prior content find unrelated current content. Retire-and-document creates a clean programme history: the identifier permanently points to the retired hypothesis with a PH-file narrative explaining what it was, what discovered the artifact, and why it was retired. The new neutron-excess work gets a fresh identifier (OPEN-SS-23 already existed; upgrade its priority).

**Natural split: OPEN-SS-22 → OPEN-SS-25.** During scope audit, found that §8 of the paper contains four "OPEN-SS-22-adjacent" references discussing DP-sea Coulomb screening as a separate physics question. That work isn't retired; only the structural-onset hypothesis is. The DP-sea screening question gets registered as the new OPEN-SS-25 to preserve it explicitly. Without this split, retiring OPEN-SS-22 wholesale would also retire the screening question, which is a different physics target from icosahedral closure.

**Secondary scope finding: line 499 factual error.** "⁴⁸Cr (not observed bound)" is wrong — ⁴⁸Cr is particle-stable. Surfaced during the scope audit as a separate-from-Table-1 factual error needing correction in v1.2.

*[Outcome: OPEN-SS-22 was retired with `problem_histories/PH-OPEN-SS-22.md` as the narrative record (first entry in the parallel `problem_histories/` folder). The OPEN-SS-25 registration captured the DP-sea screening question. Line 499 was corrected in v1.2. The retire-not-recycle precedent is now codified for future retirement events. The three-category decision space (retire-and-document / recycle-identifier / quietly-delete) is captured methodologically in `philosophy-SS-7.md`'s programme-record discussion and in `keywords-SS-7.md`'s new "Retirement (of an open problem)" entry — definitions that future retirements will inherit.]*

---

### Session 7 — The "continue" stopping-flag discipline failure: registering scope creep symmetrically (21 April 2026)

*[Note: during the v1.2 paper-body revision, the Opus hit context-budget pressure twice and Thomas said "Continue" both times. The Opus interpreted these as authorizations to push through, completed the body revision, but then realized that "continue" was ambiguous and that pushing through risked degraded quality on the companion files and registries that followed. The reasoning below is the symmetric-honesty self-flagging that registered the scope-creep failure mode at the time it was happening.]*

Thomas — I need to stop and register state. The v1.2 paper revision is a significant edit scope (16+ locations, plus Figure 3 regeneration, plus Table 1 replacement, plus §5.1 rewrite, plus §8 OPEN-SS-25 relabeling, plus §9 summary updates, plus companion docs, plus registries, plus development transcript) and I'm going to hit a hard ceiling before I can do it cleanly in one session.

[Status report: 75% of paper-body revision done in sandbox; 6-7 intertwined edits remaining; Conclusion still reads v1.1; LaTeX compile would produce inconsistency between body claims and Conclusion claims.]

Honest status: I significantly underestimated the v1.2 scope. Even stopping at "continue" a second time, I can't land the full revision in one session. The paper's body text has 6-7 more intertwined edits remaining, then 7 companion files, then 4-5 registry files, then the development transcript. **That's a fresh-session's worth of work minimum.**

What's safely landed in sandbox: the file is internally consistent up to about line 1050. The Conclusion (lines 1142+) still reads v1.1. A LaTeX compile would produce a paper whose body claims 12 predictions but whose Conclusion claims 8 — an inconsistency that MUST be fixed before any commit.

I should not have pushed past my own "stopping" flag twice this session. I did it because you said "continue" and I read that as "push through." **The honest read was "you're being cautious; keep going if you genuinely can." I could keep going, but at degraded quality.** The paper body got the core attention and compiled clean because it was the thing whose failure you'd catch fastest — which is a good prioritization, but it doesn't scale to companions/registries under the same pressure. Better to stop cleanly here than deliver messy companion files as the v1.2 landing experience.

*[Outcome: Thomas authorized continuation; the Opus completed the paper body in this session despite the warning, then handed off the companion/registry/transcript work to the next session (which became Session 10's continuation context). The "continue is ambiguous" methodological observation became a programme-level lesson. The discipline of registering scope creep at the moment it occurs (rather than after the fact) is a precedent for future long-edit sessions. This turn is the methodological mirror to the Lesson #8 scope-discipline three-category articulation in Session 10 (fix silently / fix with note / flag without fixing) — both are about preserving editorial discipline against expedience pressure.]*

---

### Session 9 — Research_Frontier latent-drift discovery: registrations claimed but never propagated (21 April 2026, evening)

*[Note: during the registry propagation pass, the Opus expected Research_Frontier.md to need only minor v1.2 updates (retire OPEN-SS-22, register OPEN-SS-25). What actually happened: a structural drift surfaced. OPEN-SS-22, OPEN-SS-23, OPEN-SS-24 plus CONJ-SS-12 plus PROP-SS-7-1 had **never been propagated** to Research_Frontier.md from SS-7 v1.0/v1.1. The paper claimed they were registered, but the file didn't reflect them. This is the same structural drift pattern the template extraction (Session 2) had been built to prevent — except for content that predated the extraction and was never caught. The reasoning below is the discovery itself.]*

**Important finding:** OPEN-SS-22, OPEN-SS-23, OPEN-SS-24, CONJ-SS-12, PROP-SS-7-1 are NOT registered in Research_Frontier.md. They exist in the paper's Registry Impact section but were never propagated to the actual registry. This is a v1.0/v1.1 drift — the paper's §Registry Impact claims these registrations happened, but the file doesn't reflect them.

The v1.2 work needs to do this properly: update OPEN-SS-18 status and add all four new registrations (OPEN-SS-22 retired, OPEN-SS-23 open-upgraded, OPEN-SS-24 open, OPEN-SS-25 new, CONJ-SS-12 conjecture, PROP-SS-7-1 supported).

[Six entries added at once: OPEN-SS-18 → PARTIALLY RESOLVED; OPEN-SS-22 RETIRED with full narrative block; OPEN-SS-23 OPEN with priority-upgrade; OPEN-SS-24 OPEN; OPEN-SS-25 NEW; CONJ-SS-12 + PROP-SS-7-1 in new SS-7 propositions subsection. Section header updated from "14 problems" to "18 problems (1 retired)".]

*[Outcome: the Research_Frontier propagation in v1.2 fixed five-papers-worth of latent drift (the SS-7 v1.0/v1.1 registrations that never landed) plus the v1.2 retirement and new registration. This is the same structural-drift pattern that the template extraction (Session 2) was designed to prevent — except that the extraction's authoritative checklist didn't yet exist when v1.0/v1.1 shipped, so the drift accumulated invisibly. The discovery here that the drift was **real and substantial** (5 missing registrations in one file) is what extended Session 10's Lesson #5 from "Research_Frontier is drifty" to "drift is structural across multiple files; the 20 April template consolidation was necessary but not sufficient." This Session-9 discovery → Session-10 articulation is the chronological development of the structural-drift programme-record observation.]*

---

*End of Sessions 1–9 content. The ten substantive turns above preserve the verbatim Opus reasoning behind committed artefacts in the v1.2 paper itself, the seven companion files, the retirement narrative, the three reviewer verification responses, the Research_Frontier and predictions.md propagations, and the templates/paper_completion_checklist.md extraction. The deliberation captured here — particularly the Phase 1/Phase 2 distinction, the Table 1 isotope-selection artifact discovery, the line 340 self-application framing, the reviewer letter design discipline, the retire-vs-recycle decision, and the Research_Frontier latent-drift discovery — is not preserved at Tier 3 in any of those committed files; the committed files state the conclusions, this Tier 4 archive preserves the reasoning that produced them.*

*Additional Sessions 1–9 content covering routine execution mechanics (the commit handshake with Thomas, the file-by-file edit execution for the v1.2 paper body and the seven companions, the registry propagation mechanics for Research_Frontier and predictions.md, the docker/connector access-method discussion at session end, and the development-transcript creation that produced `SS-7_v1.2_transcript.md`) is preserved at Tier-3-equivalent fidelity in the committed artefacts (`SS-7_v1.2_transcript.md` Sessions 1–9 entries, the seven companion files, Research_Frontier.md, predictions.md, the v1.2 paper itself, `problem_histories/PH-OPEN-SS-22.md`, the three reviewer response files, the verification letter exchange, and the templates/paper_completion_checklist.md commit) and is not duplicated here.*

**Recovery completeness update (May 2026):** with this Sessions 1–9 append, SS-7 Tier 4 recovery is now substantially complete — Sessions 1–10 covered, with deliberation behind committed v1.2 artefacts preserved. The "What remains uncovered" section above (written when only Session 10 was recovered) is superseded by this completeness; the SS-7 v1.2 cycle's full reasoning arc — from G3 discrepancy registration through Phase 1 SS-8 exploration, Table 1 artifact discovery, three-reviewer convergence, retirement decision, paper-body revision, companion suite update, Research_Frontier propagation, and post-compaction registry cascade closure — is now preserved at Tier 4 fidelity.
