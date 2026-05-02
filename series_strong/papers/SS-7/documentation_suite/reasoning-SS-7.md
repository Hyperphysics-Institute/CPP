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
