# PD-005: Four-Tier Documentation Subsumption for SF-Line Flagships

**Date:** 14 May 2026
**Session:** SF-2 v1.0 SHIP follow-on documentation discipline (Session 83 close, Patch 0373)
**Status:** Adopted as observed-pattern programme guidance for SF-line flagship documentation discipline.
**Scope:** SF-line flagship papers (SF-1 through SF-7) specifically. Series papers (SS, SM, EW, QM, SR, SD) retain full discretion to ship at v1.0 with either four-tier-only or the canonical 8-file documentation suite per `templates/documentation-suite.md`.
**Origin:** Empirical observation that SS-9 v1.0 (Session 32, Patch 0282), SF-4 v1.0 (Session 54, Patch 0314), and SF-2 v1.0 (Session 83, Patch 0368) all shipped at v1.0 with only the four-tier documentation suite (handover + reasoning + development + transcript) — the canonical 7-file companion suite (glossary, mechanism, phenomena, philosophy, reviews, keywords, FAQ/lay-summary) was deferred in each case with the substantive content subsumed into the four-tier files plus programme-level registries.
**Companion artifacts:**
- `templates/documentation-suite.md` (the canonical 8-file template; retained as the documentation ideal for series papers)
- `PD-004-publication-pathway.md` (the five-layer publication-pathway strategy; PD-005 governs the documentation infrastructure that supports PD-004's external rollout)

---

## Context

The canonical CPP documentation suite per `templates/documentation-suite.md` specifies up to 8 companion `.md` files per paper:

1. `development-[S]-[N].md` — intellectual laboratory notebook
2. `glossary-[S]-[N].md` — technical terminology + status labels
3. `mechanism-[S]-[N].md` — physical mechanisms with intuitive explanations
4. `phenomena-[S]-[N].md` — what the paper explains and predicts
5. `philosophy-[S]-[N].md` — conceptual content, type classification, honest assessment
6. `reviews-[S]-[N].md` — external reviews received, critiques addressed
7. `keywords-[S]-[N].md` — SEO / web tooling / search
8. `FAQ-[S]-[N].md` — anticipated questions and clear answers (legacy-allowed; not required for papers adopted ≥ 22 April 2026)

The four-tier session-continuity discipline per `operating_system.md` §15 adds three more files:

- `handover-[S]-[N].md` — current-state orientation document
- `transcript-[S]-[N].md` — transaction-indexed pointer-map
- `reasoning-[S]-[N].md` — Tier 4 verbatim reasoning capture

The `development-[S]-[N].md` file is shared between the canonical doc-suite and the four-tier discipline (same file, dual purpose). So the full canonical artifact set per `templates/documentation-suite.md` and `operating_system.md` §15 is **10 files** per paper at v1.0+.

## The observed pattern across SS-9, SF-4, and SF-2

Three v1.0 SHIPS over the last ~30 days have followed an identical pattern at v1.0:

**SS-9 v1.0 (Session 32, Patch 0282, 7 May 2026)**: shipped with four-tier suite only (handover, reasoning, development, transcript). The 7-file companion suite was registered as TODO-001 in `todolist.md` and **DEFERRED per Two-Triggers discipline pending external-feedback window**. SS-9 has remained at four-tier-only through Sessions 33-83 with no companion-suite work.

**SF-4 v1.0 (Session 54, Patch 0314, 9 May 2026)**: shipped with four-tier suite only. v4.4 (Session 81 archival-deposit-quality) is still at four-tier-only. No companion suite produced across Sessions 54-81 despite four version-revision campaigns (v2.0, v3.0, v4.0, v4.4).

**SF-2 v1.0 (Session 83, Patch 0368, 14 May 2026)**: shipped with four-tier suite at Patches 0369 (handover) + 0371 (reasoning) + 0372 (development + transcript). Patch 0373 (this patch) is the decision point.

Three out of three v1.0 SHIPS have not produced the 7-file companion suite at SHIP time. This is now a sufficiently stable observed pattern to warrant codification as programme strategy specifically for the SF-line where the pattern has been most consistent.

## The decision

**For SF-line flagships, the four-tier documentation suite (handover + reasoning + development + transcript) is the canonical documentation deliverable at v1.0 SHIP. The 7-file companion suite (glossary, mechanism, phenomena, philosophy, reviews, keywords, FAQ/lay-summary) is deferred-by-default with subsumption into the four-tier files plus programme-level registries.**

This is the observed-pattern codification of what has happened three times (SS-9, SF-4, SF-2). It is not a prohibition against producing the 7-file suite for SF-line papers — authors retain discretion to build the full suite if specific content justifies it. But the default for SF-line flagships is four-tier subsumption, not 7-file suite production.

### Why the subsumption pattern works

Each of the 7 canonical companion-suite slots has a natural home in the four-tier + programme-level registries:

| Suite slot | Subsumed into |
|---|---|
| **glossary** | Programme-level `master_glossary.md` per-paper terminology section (e.g., the SF-2 v1.0 W⁰ catalyst framework terms section added at Patch 0370 has 10 entries covering the same content a `glossary-SF-2.md` would have carried) |
| **mechanism** | Paper main-text §5 W⁰ catalyst framework + `reasoning-[S]-[N].md` Section 1 (mechanism reasoning at Tier 4 verbatim) + `reasoning-[S]-[N].md` Section 5 (PROP-SF-2-1 mass-degeneracy structural reasoning) |
| **phenomena** | Programme-level `predictions.md` Section 2 entries (e.g., PRED-O-21 through PRED-O-24 for SF-2) + Section 6 by-paper row + paper main-text §6 (predictions summary) |
| **philosophy** | `reasoning-[S]-[N].md` Section 1 (insight-arc narrative) + Section 10 (what v1.0 means / does not mean) + paper main-text §11 (EWSB framing, philosophical-discussion section) |
| **reviews** | Multi-reviewer-incorporation patch commit messages (in SF-2's case Patches 0359, 0360, 0361, 0363, 0364, 0366, 0367 with per-review-point disposition) + paper title-block CHANGELOG entries (per version, with reviewer attributions); `reasoning-[S]-[N].md` Section 7 narrates the three-reviewer convergence pattern |
| **keywords** | Companion paper §2 glossary (when a Companion paper exists, as for SF-2) + paper abstract + programme-level `master_glossary.md` entries; SEO/web tooling is post-public-posting concern |
| **FAQ / lay-summary** | Anthology chapter at Rovelli/SciAm register (e.g., SF-2 anthology chapter planned at Patch 0374); the anthology chapter is the lay-accessible companion at programme level (~5000-6000 words per chapter) |

The four-tier suite plus programme-level registries plus the anthology chapter therefore deliver the full content scope of the 8-file documentation suite, distributed across files whose canonical purposes match naturally.

### Triggers for upgrading to full 7-file suite

The subsumption is the default but not absolute. The Two-Triggers discipline (per SS-9 TODO-001 deferral framing) defines two specific conditions under which the deferred-companion-suite work activates:

**Trigger 1 — External-feedback substantive enough to warrant dedicated companion files.** If a peer reviewer or external collaborator engages substantively enough with a paper to produce content the four-tier subsumption cannot accommodate (e.g., a sustained correspondence about a specific mechanism that would naturally live in `mechanism-[S]-[N].md`), the companion suite work activates for that specific file. Trigger 1 is **incremental**: the activation produces the specific file the correspondence motivates, not the full 7-file suite simultaneously.

**Trigger 2 — v1.x revision producing substantive new content.** If a paper's v1.0 source receives a v1.x revision that adds substantive new content (e.g., resolving an OPEN-FP problem at theorem level), the new content may justify a dedicated companion file. Trigger 2 activates with the v1.x revision and is generally one-file-at-a-time.

In the absence of either trigger, the four-tier suite plus programme-level registries plus anthology chapter remain the canonical documentation deliverables. No periodic forced-build of the 7-file companion suite.

### Why the pattern is specifically right for SF-line

The SF-line is the apex layer of the CPP programme. SF-line flagships:

1. **Synthesize completed work from the series sectors**: SF-2 synthesizes SM-6 (Weinberg-angle inheritance) + SM-7/8/9 (mass-formula machinery) + SS-1 (binary icosahedral group structure) + EW-series (electroweak corpus); SF-4 synthesizes SM-1/3/5 (K3 + four-cage taxonomy) + SM-7/8/9 (mass machinery) + SR-1/QM-1 (substrate frameworks). The companion-suite content (mechanism, phenomena, philosophy) would significantly overlap with the series-paper companion-suite content the SF-line inherits from.

2. **Are subject to PD-004 layered-rollout framing**: SF-line papers explicitly occupy Layer 2 + Layer 3 (and sometimes Layer 4 proof-outline level) per PD-004. The Layer 4 work — full continuum-EFT derivations — is registered as dedicated future papers, NOT as companion-suite additions to the flagship. The mechanism/phenomena content for the SF-line is therefore naturally distributed: paper-main-text + reasoning Tier 4 + future Layer 4 dedicated paper, not concentrated into companion-suite files.

3. **Are heavy-lift original-contribution papers**: each SF-line paper takes 20-50 patches across multiple sessions, with multi-reviewer convergence cycles consuming significant reasoning capacity. Production of the 7-file companion suite at v1.0 SHIP would extend the campaign by 7-10 additional patches without producing content that isn't already captured in the four-tier + registries + anthology.

4. **Have a natural "lay-summary" home in the anthology**: the Rovelli/SciAm-register anthology chapters (SS-7, SS-8, SS-9, SF-4 each have one; SF-2's is planned at Patch 0374) deliver the lay-accessible companion content at programme level — the same audience that `lay-summary-[S]-[N].md` would target gets served by the anthology chapter. Production of both would be redundant.

For series papers (SS, SM, EW, QM, SR, SD), the calculus may differ. Series papers are individually narrower in scope, may not have an anthology chapter, and may produce content that genuinely benefits from dedicated mechanism/phenomena/philosophy companion files. Series papers retain full discretion per `templates/documentation-suite.md`.

## Implementation guidance for SF-line flagships at v1.0 SHIP

At v1.0 SHIP, the SF-line flagship's documentation_suite/ folder contains exactly four files:

```
flagship_papers/[sector]/documentation_suite/
├── handover-SF-N.md       (Session-close orientation per operating_system §15 Step H)
├── reasoning-SF-N.md      (Tier 4 verbatim reasoning capture per §4 Four-Tier discipline)
├── development-SF-N.md    (Vignettes per development arc per §4 Four-Tier discipline)
└── transcript-SF-N.md     (Per-patch transactions per §4 Four-Tier discipline)
```

Plus programme-level registries updated (per the registers-freeze pattern; SS-9 Session 33, SF-4 Session 54, SF-2 Session 83):

- `theorem-registry.md` SF-line section updated
- `master_glossary.md` per-paper terminology section appended
- `predictions.md` Section 2 + Section 6 per-paper entries added
- `Research_Frontier.md` per-paper OPEN-FP entries + last-updated header
- Per-OPEN-FP `problem_histories/PH-OPEN-FP-*.md` files created
- `paper_catalog.md` per-paper row + Documentation paragraph
- `INDEX.md` per-paper row
- `flagship_papers/[sector]/README.md` v1.0 SHIPPED status

Anthology chapter at Rovelli/SciAm register at a subsequent patch (typically 4-5 patches after v1.0 SHIP). TATWD integration at a subsequent patch. Public posting (Zenodo + arXiv) at Thomas's discretion.

## Implementation for SS-9, SF-4, SF-2

**SS-9 v1.0**: confirmed four-tier suite at `series_strong/papers/SS-9/documentation_suite/` (handover + reasoning + development + transcript). TODO-001 `series_strong/papers/SS-9/documentation_suite/` 7-file suite deferred. Status: subsumption complete per PD-005.

**SF-4 v4.4**: confirmed four-tier suite at `flagship_papers/neutrinos/documentation_suite/` (handover + reasoning + development + transcript). No companion suite produced through v4.4. Status: subsumption complete per PD-005.

**SF-2 v1.0**: confirmed four-tier suite at `flagship_papers/electroweak/documentation_suite/` (handover Patch 0369 + reasoning Patch 0371 + development+transcript Patch 0372). Programme-level registries complete at Patch 0370. Status: subsumption complete per PD-005 at Patch 0373.

## Reversal pathway

If at any point the observed pattern fails — for example, if a future SF-line flagship produces multi-reviewer correspondence that genuinely cannot be subsumed into the four-tier files, or if external feedback on a published flagship surfaces content gaps that the 7-file suite would naturally fill — this PD-005 should be reconsidered, not silently overridden. The reversal pathway:

1. Document the specific gap the subsumption pattern fails to cover.
2. Add a new programmatic decision (PD-006+) revising or superseding PD-005.
3. Retroactively produce the relevant companion-suite files for prior SF-line flagships that the pattern failure affects.

The subsumption is a default, not an absolute rule. The discipline is to ship cleanly at v1.0 with the four-tier suite, defer companion-suite work, and reactivate that work only on Two-Triggers.

## Cross-references

- `templates/documentation-suite.md` — the canonical 8-file template; retained as the documentation ideal for series papers; legacy and forward-discretionary
- `templates/operating_system.md` §4 — Four-Tier Documentation Discipline
- `templates/operating_system.md` §15 — Session-continuity discipline (handover + transcript + development as lab-notebook trio)
- `PD-004-publication-pathway.md` — Five-layer publication-pathway strategy; PD-005 governs the documentation infrastructure that supports PD-004's external rollout
- `series_strong/papers/SS-9/documentation_suite/` — SS-9 four-tier exemplar
- `flagship_papers/neutrinos/documentation_suite/` — SF-4 four-tier exemplar
- `flagship_papers/electroweak/documentation_suite/` — SF-2 four-tier exemplar (current patch)
