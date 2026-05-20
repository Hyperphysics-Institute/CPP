# Paper Completion Checklist — Atomic Task List

**Status:** Single authoritative post-completion checklist for the CPP paper
production pipeline. Created 20 April 2026 by consolidation of three
fragmented enumerations (`operating_system.md` §4.10, `operating_system.md`
§10, `paper_production_workflow.md` §9 and §Checklist-for-each-new-paper).

**Purpose:** This file is the **single-source, all-in-one atomic task list**
for executing the documentation suite, registry updates, navigation updates,
transcript curation, OSF registration, repository commit, and final
verification against a stable paper. A programme principal can run this
checklist end-to-end without reading any other section of
`operating_system.md` and produce the complete, accurate post-completion
state.

**Relationship to other operating documents:**
- `operating_system.md` §4.10 provides the conceptual overview of where
  Phase 7 sits in the 9-phase pipeline. That section points here for the
  atomic task list; this file does not re-state the conceptual overview.
- `operating_system.md` §10 contains the **reference-level update
  procedures** for each file (e.g., "axiom-registry.md update procedure").
  Checklist items below cite §10 sub-procedures by name; executing an
  item means following its §10 procedure.
- `paper_production_workflow.md` §9 and the checklist-template at its
  end both point here for Phase 7–9 execution.
- `templates/documentation-suite.md` contains the full per-file template
  structure for the seven companion documentation files (Section A).
  Section A items below cite this template by section number.

**Trigger condition:** Paper is at v1.0 or later AND has passed round-1
external review AND no mechanism-changing critiques are pending. If any
of these are not met, do NOT execute this checklist; return to Phase 2
or Phase 4 of `operating_system.md` §4.

**Documentation Discipline — Two Triggers (revised 26 April 2026):** This
checklist is the *Trigger 2* work — execute it when the paper is finished
and ready for publication. It does NOT gate the next paper's start. The
brief "Phase 7 Completion Gate" framing codified earlier on 26 April 2026
was repealed the same day; see `operating_system.md` §4 "Documentation
Discipline — Two Triggers" for the discipline now in force. The
session-window-bounded data-loss surface is addressed by *Trigger 1*
(per-paper continuity files at session close per §11; cross-paper session
logs in `session_logs/` for cross-paper work). Trigger 2 fires at the
genuinely-final-version mark — defer firing on a paper that may still
need revision (the OPEN-SS-22 retirement experience shows v1.x can turn
out to need substantive revision). Default to deferring Trigger 2 until
the paper is unambiguously done; the per-session Trigger 1 work captures
session-window-bounded context whether or not Trigger 2 has fired.

**Deliverables:** 7 companion documentation files + N verification
notebooks + updates to up to 12 registry files + updates to 3 navigation
files + curated transcripts + OSF registration + git commit/push +
verification pass.

**Filename pattern:** `[S]-[N]` is the paper identifier (e.g., `SS-7`).
`[S]` is the series prefix (`SS`, `SM`, `EW`, `QM`, `SD`). `[N]` is the
paper number. Canonical filenames never include version suffixes (per
`operating_system.md` §11); version lives in the paper's `documentation_suite/changelog-<paper>.md` file only (per the version-archaeology architecture rule, `operating_system.md`).

**Do NOT duplicate this content elsewhere.** The prior drift that caused
`problem_histories/` to be missed in SS-7 v1.1 Phase 7 was produced by
three parallel enumerations of the same content. This file is now the
sole source of truth for atomic tasks. Reference procedures live in
`operating_system.md` §10; atomic tasks live here.

---

## Phase 7A / 7B / 7C structure (adopted 17 May 2026, Patch 0422D)

Phase 7 is partitioned into three sub-phases by **scope of work**, not by sequence. The partition makes whole-category dropout visible so that program-level documentation work cannot quietly fall off the queue while paper-level work proceeds.

**Phase 7A — Paper-level work.** Updates that touch *this paper's* materials only: companion documentation suite, verification notebooks, bibliography entry for this paper, paper-specific INDEX.md and series-README rows, development transcripts, OSF registration of this paper. These items fire on every paper SHIP and are typically completed within ~1 session.

**Phase 7B — Program-level work.** Updates that touch the *programme's* state and orientation documents: theory-overview, axiom-registry, theorem-registry, master_glossary, research_frontier, predictions, paper_catalog, founders_vision, future_projects, CPP_the_theory (TATWD), problem_histories, and the top-level README.md. Each paper SHIP modifies programme state — new theorems registered, new predictions counted, new open problems opened or closed, ratio updates — and the orientation documents must be re-synced or they go stale. **This is the work most prone to dropout** because it is invisible from inside the paper's directory; the discipline failure that triggered this restructure (theory-overview.md and axiom-registry.md drifting from 26 April 2026 across four flagship SHIPs through 17 May 2026) was a 7B failure.

**Phase 7C — Execution.** Final mechanical work: repository commit + final verification pass.

### Mapping from sections to phases

| Phase | Sections | Contents |
|---|---|---|
| **7A (paper-level)** | A, B, **C11**, **D2**, **D3**, E, F | Companion suite (A), notebooks (B), bibliography entry for this paper (C11), INDEX.md entries for paper-specific files (D2), series-README row update (D3), development transcripts (E), OSF registration (F) |
| **7B (program-level)** | **C1–C10**, **C12**, **D1** | theory-overview (C1), axiom-registry (C2), theorem-registry (C3), master_glossary (C4), research_frontier (C5), predictions (C6), paper_catalog (C7), founders_vision (C8), future_projects (C9), CPP_the_theory TATWD (C10), problem_histories (C12), top-level README (D1) |
| **7C (execution)** | G, H | Repository commit (G), final verification (H) |

**Rationale for the split within Section C and Section D:** Section C (Registry updates) contains 12 items, but they are not uniform in scope. C11 (bibliography/cpp_references.bib) updates a paper-specific BibTeX entry; the entry exists *for this paper* and the work is naturally bucketed with this paper's other paper-level artifacts. C1–C10 and C12 update programme-wide state. Similarly, Section D contains 3 items: D1 (top-level README.md) is a programme-level state document; D2 (INDEX.md) adds entries for *this paper's* new files; D3 (series_[name]/README.md) adds *this paper's* row to its series table.

**Ordering convention:** 7A fires first (paper-level work that benefits from the paper being open in working memory), then 7B (the programme-state-update work that requires a stable paper to attribute), then 7C (execution). 7B's program-level work is **NOT optional** even though it can superficially feel separable from the paper — it is the discipline that makes the programme's ratio claims accurate at every SHIP.

**Discipline-failure mode this structure prevents:** The Phase 7B items can all be skipped without anyone noticing during a single SHIP because none of them are in the paper's own directory; they live at the repo root. Across 4 flagship SHIPs (SS-9 May 7, SF-4 v4.4 May 11, SF-2 v1.0 May 14, Capotauro v1.0 May 16), Phase 7B items C1 (theory-overview), C2 (axiom-registry), and parts of C4/C5/C7 silently drifted while Phase 7A items shipped cleanly. Making 7B explicit as its own phase, rather than scattering its items across Section C and Section D, forces the program-level work into the visible checklist.

---

## A. Companion documentation suite (7 files) — **[Phase 7A — Paper-level]**

Location: `series_[name]/companions/`. Full per-file templates:
`templates/documentation-suite.md`.

- [ ] **A1.** `mechanism-[S]-[N].md` — step-by-step mechanism narrative
  with mathematical-correspondence table. Required sections: Overview;
  Inputs and constants; Step-by-step derivation; Mathematical
  correspondence table (physics claim ↔ equation number ↔ paper section);
  Failure modes (with OPEN-* references). See `documentation-suite.md`
  §3.

- [ ] **A2.** `glossary-[S]-[N].md` — paper-specific terms organized by
  category. Required categories: Constants; Structural terms; Mechanism
  terms; Methodology terms. Each entry: term, definition, first-use
  location, related terms. See `documentation-suite.md` §2.

- [ ] **A3.** `phenomena-[S]-[N].md` — what the paper explains. Three
  required subsections: PHEN-E (empirical facts); PHEN-P (zero-parameter
  predictions with experimental comparison); PHEN-V (consilience with
  other CPP results). See `documentation-suite.md` §4.

- [ ] **A4.** `philosophy-[S]-[N].md` — epistemological framing. Required
  subsections: Certainty level (theorem / empirically supported hypothesis
  / conjecture / scoping); Relationship to Standard Model
  (extends / replaces / reproduces / disagrees); Falsifiability inventory
  (with threshold values); Paper-type declaration (per
  `operating_system.md` §4 taxonomy); Limits of scope. See
  `documentation-suite.md` §5.

- [ ] **A5.** `development-[S]-[N].md` — development history. Required
  subsections: Version timeline; Key decisions (≥3, with alternatives);
  Dead ends (with rejection reason); Contributor roles; Transcript
  references. See `documentation-suite.md` §1 and procedure in
  `operating_system.md` §10 "development-[S]-[N].md procedure."

- [ ] **A6.** `reviews-[S]-[N].md` — all reviews + FAQ. Part 1: formal
  reviews by reviewer and round, with quoted verdict, strengths,
  critiques accepted vs. declined, integration outcomes. Reference
  individual response documents. Part 2: FAQ by category (methodology,
  scope, falsifiability, SM relationship, future work), 5–15 entries.
  See `documentation-suite.md` §6–§7.

- [ ] **A7.** `keywords-[S]-[N].md` — keywords and registry cross-refs.
  Required sections: Primary keywords (5–10); Secondary keywords (10–20);
  Cross-references to other CPP papers; Axiom/theorem/conjecture entries
  registered or resolved (with OPEN-*, CONJ-*, PROP-* IDs). See
  `documentation-suite.md` §8.

---

## B. Verification notebooks — **[Phase 7A — Paper-level]**

Location: `series_[name]/notebooks/`.

- [ ] **B1.** Enumerate every numerical quantity cited in the paper:
  predicted values, extracted constants, experimental values compared
  against, derived intermediates, numerical stress-test results.

- [ ] **B2.** For each quantity, create or confirm a reproducible standalone
  Python script at `series_[name]/notebooks/[S]-[N]_[description].py` with
  the required header:
  ```python
  # ============================================================
  # [S]-[N]: [Description]
  # Paper: [Full paper title]
  # Computation: [What this notebook computes]
  # Key result: [The number(s) this produces, cited in the paper]
  # Author: [AI name], [date]
  # ============================================================
  ```

- [ ] **B3.** Each script must run from scratch with only standard
  dependencies (numpy, scipy, matplotlib, itertools) and print or plot
  the cited result. Test each script independently before archiving.

- [ ] **B4.** Skip notebook creation for: LaTeX compilation, file
  management, trivial arithmetic verifiable by hand.

- [ ] **B5.** Add each notebook to `INDEX.md` inside
  `series_[name]/notebooks/`.

---

## C. Registry updates — repository-root content documents + book project infrastructure — **[Phase 7B paper-level for most items + Phase 7A for C11]**

**Phase split (adopted Patch 0422D):** Items C1–C10 and C12 update **programme-wide state** documents and are **Phase 7B (program-level)** work. Item C11 updates the paper-specific BibTeX entry in `bibliography/cpp_references.bib` and is **Phase 7A (paper-level)** work. The split makes the program-level dropout risk visible — items C1–C10 are the most-skipped items across the programme's SHIP history and are the discipline-failure mode this restructure addresses.

Each item atomic; cite the reference procedure in `operating_system.md`
§10 for how to execute. Trigger conditions noted per item — skip items
whose trigger is not met.

- [ ] **C1.** **[7B]** `theory-overview.md` — update if the paper produced new
  quantitative results, new formulas, resolved/new open problems, or
  changed series status. Procedure: `operating_system.md` §10
  "theory-overview.md update procedure."

- [ ] **C2.** **[7B]** `axiom-registry.md` — update if the paper used any axiom
  not yet in the registry, consolidated axioms, or introduced new
  predictions. Procedure: `operating_system.md` §10 "axiom-registry.md
  update procedure." Note the reviewer-ID reconciliation rule in that
  procedure.

- [ ] **C3.** **[7B]** `theorem-registry.md` — update if the paper introduced or
  referenced new theorems or corollaries, or resolved a problem tracked
  in the theorem registry's Open Problems table. Procedure:
  `operating_system.md` §10 "theorem-registry.md update procedure."

- [ ] **C4.** **[7B]** `master_glossary.md` — update if the paper introduced any
  term, acronym, particle, cage structure, or mechanism not already in
  the glossary. Also scan `founders_vision.md` for new terms. Procedure:
  `operating_system.md` §10 "master_glossary.md update procedure."

- [ ] **C5.** **[7B]** `research_frontier.md` — update if the paper addressed any
  OPEN-*, CONJ-*, or PROP-* entry (status change, resolution, falsification,
  new registration, dependency graph change). Procedure:
  `operating_system.md` §10 "research_frontier.md update procedure."

- [ ] **C6.** **[7B]** `predictions.md` — update if the paper produced any new
  quantitative prediction or changed the status of an existing one.
  Procedure: `operating_system.md` §10 "predictions.md update procedure."

- [ ] **C7.** **[7B]** `paper_catalog.md` — always update on paper completion.
  Add or refresh the paper row: version, date, status, reviewer verdicts,
  open-problem registrations, target for next paper. Update total paper
  count. Procedure: `operating_system.md` §10 "paper_catalog.md update
  procedure."

- [ ] **C8.** **[7B]** `founders_vision.md` — update if the paper represents a
  significant programme advance OR if new physical intuitions were
  captured during the sessions that produced the paper. Write a
  one-paragraph milestone note for significant advances. Procedure:
  `operating_system.md` §7 "Founders Vision Protocol" (referenced from
  §10).

- [ ] **C9.** **[7B]** `future_projects.md` — update if the paper closed a target,
  shifted priorities, or surfaced new research targets. Procedure:
  `operating_system.md` §10 "future_projects.md update procedure." Check
  the "current #1 priority" line for staleness.

- [ ] **C10.** **[7B]** `programme_orientation.md` (TATWD) — **MANDATORY at every
  paper v1.0 SHIP** and at every programme-architecture event
  (cross-sector closure, new methodology framework, sector synthesis).
  Add results in connected prose (not bullets). Add a new chapter if
  the paper synthesizes a sector or methodology pattern (e.g., SS-9
  v1.0 added Chapter 22c; SF-4 v4.4 added Chapter 22d). Update the
  Predictions Scorecard in Part VIII with new zero-parameter
  correspondences. Move any resolved open problems from Part VII to
  the relevant chapter and add new ones to Part VII. Procedure:
  `operating_system.md` §10 "programme_orientation.md update procedure."
  **Cadence calibration adopted 11 May 2026 (patch 0344):**
  - **Mandatory** at v1.0 SHIP of any new paper, at any version that
    adds new theorems / chapters / open problems to the programme,
    and at any programme-architecture event.
  - **Optional** for intra-paper revisions (v_n.x review-cycle
    calibration, archival polish, wording-precision updates) when no
    programme-state changes. Batch deferred updates into the
    dossier-completeness closeout sequence.
  - **Backstop**: the dossier-completeness closeout sequence
    (`operating_system.md` §15) explicitly verifies TATWD integration
    before the campaign closes; any deferred updates get caught
    there. The Session 81 patch 0343 closeout that landed SF-4
    v1.0 → v4.4 TATWD integration in a single batch is the
    precedent — that batch was too large (4 SHIPs accumulated), and
    the cadence-calibration above is designed to prevent recurrence.

  The failure mode this calibration prevents: forward-queueing TATWD
  integration at each SHIP and never executing it. SF-4 had TATWD
  integration listed in the post-SHIP forward queue at v1.0 / v2.0 /
  v3.0 / v4.0 and never executed until Session 81's closeout. The
  new discipline makes the v1.0 SHIP integration mandatory rather
  than aspirational.

- [ ] **C11.** **[7A]** `bibliography/cpp_references.bib` — add a BibTeX entry for
  the new CPP paper; add BibTeX entries for any external works newly
  cited; verify cite keys match the paper's `.tex`. Procedure:
  `operating_system.md` §10 "bibliography/cpp_references.bib update
  procedure." **Easy to miss: this file lives in `bibliography/`, not
  at the repo root.** Do not add entries to deprecated per-series or
  per-paper `.bib` files. **(Phase 7A because the entry is paper-specific
  and naturally bundles with the paper's other artifacts.)**

- [ ] **C12.** **[7B]** `problem_histories/` — update if the paper resolved (fully
  or partially) or substantially advanced any OPEN-*, CONJ-*, or PROP-*
  entry, OR if it registered a new entry with substantive narrative arc
  beyond bare birth-registration. Create or update `PH-[ID].md` per the
  procedure. Apply the symmetric-honesty threshold: document what the
  resolution did NOT do, not only what it did. Procedure:
  `operating_system.md` §10 "problem_histories/ update procedure."
  **Easy to miss: `problem_histories/` is a registry-adjacent directory,
  not in the repo root alongside the other content documents. This is
  the item that drove the 20 April 2026 consolidation. Do not skip C12.**

- [ ] **C13.** **[7B]** `book_project/chapters/<paper-id>_<title>.md` —
  **MANDATORY at every paper v1.0 SHIP.** Create a self-contained
  4,000-5,000-word anthology chapter at Scientific American / Rovelli
  register per `templates/anthology_chapter_template.md`. The chapter
  tells the paper's intellectual journey from problem to result;
  stands on its own; uses 6-8 equations concentrated at recognition
  moments; introduces no more than 3-4 new concepts. The chapter is
  Artifact 1 in the `book_project/five_artifact_taxonomy.md` taxonomy
  and is distinct from the programme orientation document (C10
  update) and the eventual TATWD popular-rigorous book (Artifact 2,
  post-unification — see `book_project/TATWD_book_2_roadmap.md`).

  **Sub-chapter ad-hoc trigger.** A paper may contain sub-stories that
  warrant their own anthology sub-chapter; this is triggered
  ad-hoc by the human collaborator, not automatically. The default
  is one chapter per paper.

  **Cadence and discipline.** Mandatory at v1.0 SHIP (not deferrable to
  intra-paper revisions, not deferrable to post-SHIP catch-up batches).
  The failure mode this discipline prevents: anthology chapters
  produced reactively after retrospective audit catches the gap
  (e.g., Capotauro v1.0 anthology chapter at Patch 0416K, ~1 session
  after v1.0 SHIP; SF-2 v1.0 anthology chapter at Patch 0374 as
  ad-hoc Session 83 close decision). Hard-coding the trigger removes
  the dependency on human-collaborator memory.

  **Backstop.** Session-close handover Step H audit table (per
  `operating_system.md` §15) explicitly verifies C13 at v1.0 SHIP
  before the session-close handover is committed; missing chapter
  blocks session-close completion.

  Procedure: `templates/anthology_chapter_template.md` (craft
  documentation: voice, register, dramatic-centerpiece-finding,
  structural arc, honesty discipline, calibration questions).
  **Source priority for chapter drafting** (updated Patch 0449b
  per OPEN-ORG-017): the chapter is sourced from the paper's
  real-time artifacts (`sketches/*.md` Tier 4 verbatim reasoning,
  `documentation_suite/reasoning-<paper>.md` Tier 4 where separate,
  `documentation_suite/development-<paper>.md` Tier 3 vignettes,
  `founders_voice/NNN_*.md` Thomas's organizational vision) PLUS
  the documentation-suite summary files (mechanism, philosophy,
  reviews, lay-summary) PLUS the `.tex` source. Real-time artifacts
  are READ FIRST because they carry the discovery-narrative
  texture (false starts, recognition moments, PAIRING resolutions)
  that the documentation suite summarizes away. See
  anthology_chapter_template.md "How to use this template" item 3
  for full priority order and rationale.
  **(Phase 7B because the anthology is programme-level book
  infrastructure even though each chapter is paper-specific in
  content; parallels C10's classification of programme_orientation.md
  updates.)**

- [ ] **C14.** **[7B]** `methods_catalogue/methods_catalogue.md` —
  **MANDATORY at every paper v1.0 SHIP.** Audit the paper's full
  Tier-4 reasoning corpus (`documentation_suite/reasoning-<paper>.md`
  + relevant sections of working sketches at `sketches/*.md`) for any
  new or adapted **physics derivation** methods that warrant catalog
  entry per the three-category convention (NEW METHOD / ADAPTED
  METHOD / STRAIGHT REUSE) and threshold rule (reusable across at
  least one other physics-derivation context). The session-close
  audit (§15 Step E methods_catalogue audit line) catches methods at
  per-session granularity; this v1.0 SHIP audit catches methods
  missed at session level and validates that the paper's
  full method usage is reflected in the catalog.

  **Workflow (catalog-first-then-cite, codified Patch 0463):**

  1. **Read the canonical record.** Read the full `reasoning-<paper>.md`
     and relevant `sketches/*.md` sections covering the closure
     trajectory that produced the paper. The verbatim physics
     reasoning is the source for identifying methods — *not* the
     polished `.tex` paper, which preserves the result of method
     application but may compress away the moment of method choice.

  2. **Identify methods used.** For each substantive reasoning move
     in the Tier-4 entries, classify the method: NEW METHOD (no
     existing catalog entry), ADAPTED METHOD (existing entry
     customized with sector-specific content), or STRAIGHT REUSE
     (existing entry applied as-is). Apply the threshold rule before
     classifying as NEW or ADAPTED — single-application techniques
     do not warrant catalog entries; only methods reusable across
     at least one other physics-derivation context do.

  3. **Add catalog entries FIRST.** Before touching the `.tex` paper,
     append any new NEW METHOD or ADAPTED METHOD entries to
     `methods_catalogue.md` per the catalog's format (identifier +
     name + description + canonical citation + example
     applications). Update the status line at top + footer totals.
     This step closes any gap left by the per-session audit at
     §15 Step E.

  4. **Then add inline citations.** Add `[METH-L{layer}-NNN
     method-name]` inline citations to the `.tex` paper at each
     point where the method is invoked, per the inline-citation
     convention specified in `methods_catalogue/README-methods_catalogue.md`.
     Example: "By Schur orthogonality [METH-L1-001 Schur
     orthogonality for cage-shell averaging], the cage-shell factor
     equals $d_E / |I_h| = 2/12 = 1/6$." Every cited method must
     resolve to a registered catalog entry; if a citation is needed
     for a method not yet in the catalog, register the catalog entry
     first per step 3, then add the citation per this step.

  5. **Audit-trail check.** Sweep the `.tex` paper for any remaining
     uncited substantive method invocations. The teaching-tool
     value of the inline-citation convention requires that the
     paper's physics-derivation moves be traceable to named methods
     at the catalog level; ungrouped or implicit method invocations
     defeat the convention's discoverability purpose.

  **Logical ordering note.** C14 should execute BEFORE C13 (anthology
  chapter) because the anthology chapter's drafting may benefit from
  catalog citations as discoverability anchors for the chapter's
  technical asides — though anthology chapters at Rovelli/SciAm
  register typically minimize technical machinery, so catalog
  citations there are optional. C14 must also execute BEFORE F
  (OSF registration) and G (Repository commit) so that the SHIPPED
  paper version on origin/main has the inline citations integrated.

  **Scope reminder (Patch 0461 scope clarification).** This audit is
  for **physics derivation methods only**. Protocol patterns,
  workflow heuristics, handover-discipline observations, and
  operating-system disciplines are OUT OF SCOPE for
  `methods_catalogue` — those belong in `templates/operating_system.md`
  (protocols/workflow patterns), `relationship_protocol.md` (reviewer
  interaction), `founders_voice/` (voice/methodological observations),
  `opus_voice/` (meta-conversation), or `programmatic_decisions/`
  (programmatic decisions). See `methods_catalogue/README-methods_catalogue.md`
  "Scope: physics derivation methods only" section for the explicit
  scope rule + scope test.

  **Failure mode this discipline prevents.** Paper publishes with
  uncited method invocations; future readers (human or AI) cannot
  trace the paper's substantive reasoning moves to named techniques
  in the catalog; the catalog grows incomplete because methods used
  in published papers don't appear in it; the catalog's teaching-
  tool value erodes because new readers can't use it to navigate
  published work. The session-close audit (§15 Step E) catches some
  of this risk in real-time; the v1.0 SHIP audit catches the rest
  before the paper ships.

  **Backstop.** Session-close handover Step H audit table (per
  `operating_system.md` §15) explicitly verifies C14 at v1.0 SHIP
  before the session-close handover is committed; missing
  methods_catalogue audit blocks session-close completion when
  the session contains a v1.0 SHIP. Procedure:
  `methods_catalogue/README-methods_catalogue.md` (format
  conventions + threshold rule + three-category convention +
  inline-citation convention).

  **(Phase 7B because the methods_catalogue is programme-level
  registry infrastructure; the audit ensures both catalog
  completeness and paper-level inline citation integration in a
  single coordinated step.)**

---

## D. Navigation updates — **[Phase 7B for D1; Phase 7A for D2, D3]**

**Phase split (adopted Patch 0422D):** D1 (top-level README.md) is a **programme-state document** — its content reflects total paper count, current axiom set, and headline results across the whole programme; updating it is **Phase 7B** work. D2 (INDEX.md) adds entries for *this paper's* new files and D3 (series-README) adds *this paper's* row to its series table; both are paper-specific work and **Phase 7A**.

These files track structure rather than substance. All three are typically
updated on every paper completion.

- [ ] **D1.** **[7B]** `README.md` — add the paper to the Registered Papers table;
  update paper count; add to Strongest Results if the paper produced a
  headline result; update axiom summary line if axiom count changed.
  Procedure: `operating_system.md` §10 "README.md update procedure."

- [ ] **D2.** **[7A]** `INDEX.md` — add every new file created during this paper's
  production (the `.tex`/`.pdf`/`.bib`, companion suite files, development
  transcripts, new figures, notebooks, problem-history files). Group
  under correct folder sections; add folder headings if new folders were
  created. Procedure: `operating_system.md` §10 "INDEX.md update
  procedure."

- [ ] **D3.** **[7A]** `series_[name]/README.md` — add the paper to the series
  paper table; update series description if scope changed; add new
  cross-references between papers in the series. Procedure:
  `operating_system.md` §10 "series_[name]/README.md procedure."

---

## E. Development transcripts — **[Phase 7A — Paper-level]**

Location: `series_[name]/development-transcripts/`.

- [ ] **E1.** Collect raw transcript files from all sessions that
  contributed to the paper's development. Source: `/mnt/transcripts/`.

- [ ] **E2.** Curate each transcript per `operating_system.md` §6
  protocol: preserve substance and Thomas's verbatim physical-insight
  words; remove tooling noise; keep dead ends and negative results as
  part of the scholarly record.

- [ ] **E3.** Save as `[S]-[N]_transcript_[NN]_[AI].md` in
  `series_[name]/development-transcripts/`. For comprehensive multi-session
  arcs use `[S]-[N]_development_transcript_[AI].md`. Procedure:
  `operating_system.md` §10 "Development transcript procedure."

- [ ] **E4.** Ensure each transcript is referenced in
  `development-[S]-[N].md` (item A5).

---

## F. OSF registration — **[Phase 7A — Paper-level]**

- [ ] **F1.** If the paper has no OSF DOI yet: create a new OSF project,
  obtain a pending DOI, attach the final PDF.

- [ ] **F2.** If the paper has an existing OSF DOI from an earlier
  version: update the OSF project with the new PDF and a changelog
  summary (drawn from `documentation_suite/changelog-<paper>.md`).

- [ ] **F3.** Update the paper's `documentation_suite/changelog-<paper>.md`
  to reference the OSF DOI.

- [ ] **F4.** Update `paper_catalog.md` row with the current OSF DOI
  status (this partially overlaps C7; executing C7 after F4 captures it
  naturally).

---

## G. Repository commit — **[Phase 7C — Execution]**

- [ ] **G1.** `git add` all new and modified files from A–F.

- [ ] **G2.** `git commit` with message following the pattern:
  `[S]-[N] v[X.Y]: documentation suite complete — [brief summary of
  scope]`.

- [ ] **G3.** `git push` to the canonical remote.
  *Note: this is a user-action item when running in environments that
  lack push authentication; defer and flag rather than block.*

- [ ] **G4.** Verify GitHub shows the expected file structure under
  `series_[name]/` and that any new top-level files (e.g., new
  `PH-*.md` files in `problem_histories/`) are visible.

---

## H. Final verification — **[Phase 7C — Execution]**

**Symmetric-honesty reminder.** Apply the same standards to your own
work as to reviewers. Register discrepancies openly when found — in a
dated note file co-located with the paper, with cross-reference from
the paper's development log. See
`series_strong/papers/SS-7_v1.1_G3_discrepancy_note.md` for the template
and `templates/relationship_protocol.md` §2.6 for the underlying
principle. Not exempting your own output is what gives corrections sent
to reviewers their legitimacy.

- [ ] **H1.** Open the paper PDF and confirm it references each companion
  file at least once (either by direct mention or via implicit reference
  through shared terminology).

- [ ] **H2.** Spot-check each companion file for: correct paper version
  noted; internal cross-references valid; no placeholder text
  (`[TO BE WRITTEN]`, `TODO`, etc.) remaining.

- [ ] **H3.** Confirm every numerical value in `predictions.md` and
  `phenomena-[S]-[N].md` matches the paper exactly. **This is the check
  that caught the SS-7 v1.1 RMS discrepancy (0.88% cited vs. 0.91%
  computed).** If a mismatch is found, register it per the symmetric-
  honesty reminder above; do not silently fix the companion to match
  the paper.

- [ ] **H4.** Confirm every OPEN-*, CONJ-*, PROP-* identifier used in
  the paper appears in `research_frontier.md` with current status.

- [ ] **H5.** Confirm no stale references in `README.md` or `INDEX.md`
  (old paper counts, broken links, retired filenames).

---

## Completion criterion

All checkboxes above whose trigger condition was met are marked
complete. The paper's documentation state is stable at v[X.Y]. Future
revisions (v1.2, v2.0) re-run H1–H5 plus whatever items from A–G are
affected by the revision; the full suite does not need re-execution
unless mechanism or main claims change.

**Estimated effort:** 1 full session (~3–5 hours) for A–G with a
prepared paper. Section H is ~30 minutes.

**Failure modes and recovery:**
- Numerical mismatch between companion file and paper: the paper is the
  source of truth; fix the companion. If the *paper* is wrong, register
  the discrepancy and escalate to Thomas for v1.x decision (see
  `SS-7_v1.1_G3_discrepancy_note.md`).
- Companion file must be rewritten mid-execution due to discovered paper
  error: return to Phase 2 (`operating_system.md` §4), produce revised
  paper version, restart this checklist.
- OSF registration fails (network, permissions): complete A–E and G,
  flag F as pending, proceed; do not block the suite on OSF.
- Git push fails in unauthenticated environment: flag G3 as pending
  user-action item in the session handover; proceed with G4 deferred.

**Drift-prevention rule:** If a task needs to be added to this checklist,
add it here and update any downstream pointer (in `operating_system.md`
§4.10 and `paper_production_workflow.md` §9). Do NOT create parallel
enumerations elsewhere. The drift that motivated this extraction came
from three places each thinking they owned the list.

---

## Phase 7 Synthesis (added 17 May 2026, Patch 0422D)

The 32 atomic items (A1-A7, B1-B5, C1-C12, D1-D3, E1-E4, F1-F4, G1-G4, H1-H5) regroup by phase as follows. Use this synthesis as a working checklist at SHIP time:

### Phase 7A — Paper-level (typically 1 session)

Items that touch this paper's materials only. Default-fire on every SHIP.

| Item | Location | Description |
|---|---|---|
| A1-A7 | `series_[name]/companions/` | 7 companion documentation files (mechanism, glossary, phenomena, philosophy, development, reviews, keywords) |
| B1-B5 | `series_[name]/notebooks/` | Verification notebooks for numerical claims |
| **C11** | `bibliography/cpp_references.bib` | BibTeX entry for the new paper + any new external citations |
| **D2** | `INDEX.md` (root) | New file entries for this paper's artifacts |
| **D3** | `series_[name]/README.md` | This paper's row added to series table |
| E1-E4 | `series_[name]/development-transcripts/` | Curated transcripts for this paper's development arc |
| F1-F4 | OSF + `paper_catalog.md` | OSF deposit for this paper |

### Phase 7B — Program-level (typically 1-2 sessions per SHIP, accumulates if skipped)

**THIS IS THE PHASE MOST PRONE TO DROPOUT.** Items update programme-wide orientation documents that live at the repository root (not in the paper's directory). Each item that fires keeps the programme's accounting accurate; each item that silently drops out introduces stale state that an external auditor would catch.

| Item | Location | Description | Drop-out symptom |
|---|---|---|---|
| **C1** | `theory-overview.md` | Programme summary: prediction counts, series status, axiom-to-prediction ratio | File last-updated header drifts; "Last updated: 26 April" while it's 17 May |
| **C2** | `axiom-registry.md` | Per-paper attribution table, growth ledger, conjecture/reduction tracking | Growth-table rows missing for shipped papers; cumulative count stale |
| **C3** | `theorem-registry.md` | Total theorem count, per-paper theorem attribution, dependency graph | Theorem count stale; new THEO-* not registered |
| **C4** | `master_glossary.md` | Programme-wide term/acronym registry | New terms introduced in paper not glossed |
| **C5** | `research_frontier.md` | OPEN-*/CONJ-*/PROP- status tracking, problem count, dependency graph | Problem count stale; new OPEN-* unregistered; resolved problems still marked open |
| **C6** | `predictions.md` | Cumulative Swarm Tally, per-paper prediction count | Cumulative count stale; new PRED-* unregistered |
| **C7** | `paper_catalog.md` | Per-paper row with version/date/status/reviewer/open-problem registration | Paper-catalog row stale; previous version cited instead of current |
| **C8** | `founders_vision.md` | Milestone notes for significant programme advances | Milestone for cross-sector closure or sector synthesis unrecorded |
| **C9** | `future_projects.md` | Research priority tracking | Closed targets still flagged as #1 priority; new targets unregistered |
| **C10** | `programme_orientation.md` (TATWD) | Master narrative across the framework | New chapter unwritten; Predictions Scorecard stale; resolved problems still in Part VII |
| **C12** | `problem_histories/PH-*.md` | Narrative arc per OPEN-*/CONJ-*/PROP- entry | New PH-*.md file uncreated; existing PH file's status field stale |
| **D1** | `README.md` (root) | Top-level programme overview | Paper count stale; headline results missing |

### Phase 7C — Execution (typically 1 hour)

Mechanical close-out work.

| Item | Description |
|---|---|
| G1-G4 | `git add` + `git commit` + `git push` + GitHub verification |
| H1-H5 | Final consistency verification: PDF↔companion cross-references, numerical-value checks, OPEN-*/CONJ-*/PROP- status checks, no-stale-references check |

### Anti-pattern: Phase 7B silent dropout

Across SS-9 (7 May), SF-4 v4.4 (11 May), SF-2 v1.0 (14 May), and Capotauro v1.0 (16 May), Phase 7A items shipped cleanly while Phase 7B items C1 (theory-overview) and C2 (axiom-registry) silently drifted. These were caught only on a 17 May audit (Session 127 Patch 0422 sequence). The 7A/7B/7C structure (this Synthesis section) is designed to make the program-level work visible as a distinct category, so the SHIP cannot be considered complete with only Phase 7A done.

**SHIP gate:** A paper SHIP is complete when **all three phases — 7A, 7B, 7C** — are executed. Skipping 7B items does not block the paper from being declared at v1.0, but the v1.0 SHIP is **only structurally complete when 7B is also done**. If 7B cannot be completed in the same session as the SHIP (e.g., out-of-time, multi-paper accumulation), the deferred 7B items go onto an **explicit deferral list** in the handover document; they do not fall off the queue.

---

## Document history

- **20 April 2026**: Created by consolidation of three fragmented enumerations (`operating_system.md` §4.10, §10, and `paper_production_workflow.md` §9). Initial structure A-H with 12 sub-items in C and 3 in D.
- **26 April 2026**: Two-Triggers discipline framing added (Trigger 1 per-session continuity + Trigger 2 paper SHIP); Phase 7 Completion Gate framing repealed same day.
- **11 May 2026**: C10 (TATWD) cadence calibration added at Patch 0344 in response to SF-4 four-version TATWD accumulation across Sessions 54-81.
- **17 May 2026 (Patch 0422D)**: Phase 7A/7B/7C structure adopted in response to discipline failure observed across SS-9/SF-4/SF-2/Capotauro SHIP sequence where Phase 7B program-level items C1 (theory-overview) and C2 (axiom-registry) silently drifted from 26 April through 17 May despite four paper SHIPs in the interim. Existing A-H section structure preserved with phase tags `[Phase 7A]`/`[Phase 7B]`/`[Phase 7C]` added inline; C and D sections receive header notes explaining the within-section split (C1-C10/C12 = 7B, C11 = 7A; D1 = 7B, D2/D3 = 7A); Phase 7 Synthesis section added with per-phase task tables and explicit dropout-symptom inventory for the 7B items.

- **18 May 2026 (Patch 0434C)**: C10 path reference updated from `CPP_the_theory.md` to `programme_orientation.md` per the rename codified in `book_project/five_artifact_taxonomy.md` (Patch 0434A) that established the five-artifact taxonomy and removed the conflation between Artifact 5 (programme orientation document) and Artifact 2 (TATWD popular-rigorous book). C10 content semantics unchanged; only the path reference updated.

- **18 May 2026 (Patch 0434D)**: **C13 added — anthology chapter as mandatory at v1.0 SHIP.** Previously anthology chapters were produced reactively (e.g., Capotauro chapter at Patch 0416K ~1 session after v1.0 SHIP; SF-2 chapter at Patch 0374 as ad-hoc Session 83 close decision) rather than triggered automatically by the checklist. Hard-coding C13 as [7B] paper-completion item removes the dependency on human-collaborator memory and parallels C10's discipline. Section C header updated to reflect that the section now includes book-project infrastructure (C13) in addition to repository-root content documents. Sub-chapter ad-hoc trigger preserved (one chapter per paper default, sub-chapter ad-hoc human-collaborator-triggered). Procedure: `templates/anthology_chapter_template.md` (craft documentation; established 26 April 2026).

---

## SHIP Trigger Detection and Mandatory Immediate Execution (added 20 May 2026, Patch 0481M)

The 17 May Patch 0422D Phase 7A/7B/7C partition addressed the *dropout symptoms* (which items silently drift). This section addresses the *trigger detection and execution-timing failure* observed at Session 135's Capotauro v2.0 v1.0 SHIP — where Phase 7 work fired reactively when Thomas asked "are the registries updated?" rather than automatically on SHIP detection, producing 12 sequential paper-completion-sequence patches (0481a through 0481L) with audit-driven gap-finding.

### SHIP detection rule (grep-able, no judgment call)

A patch is a **SHIP patch** iff it modifies the paper's `.tex` source title-block version line to land at any of the following terminal states:

- `Version N.0 v1.0 SHIPPED` (e.g., `Version 1.0 SHIPPED`, `Version 2.0 v1.0 SHIPPED`, `Version 4.0 SHIPPED`)
- `Version N.0 (SHIPPED)` (parenthetical SHIPPED marker)
- Equivalent author-customised forms that match the regex `Version [0-9]+\.[0-9]+( v[0-9]+\.[0-9]+)? \(?SHIPPED\)?` in the title block

A version bump that lands at `(DRAFT)`, `(REVIEW)`, `(SHIP-CANDIDATE)`, `(POLISH)`, `(RC)`, or any non-SHIPPED state is **NOT** a SHIP patch — those are reviewer-cycle or polish patches and Phase 7 does not fire.

A patch may be a SHIP patch even if it does no other substantive work (the version-bump-only pattern used at Capotauro v1.0 Patch 0415 and at Capotauro v2.0 v1.0 Patch 0479 is the canonical SHIP-patch form). It may also be a SHIP patch alongside substantive last-mile content edits, provided the title-block change lands at SHIPPED state.

**Operational rule:** before committing any patch that touches a paper's title-block version line, grep the diff for the regex above. If it matches, the patch IS a SHIP patch and the mandatory-immediate-execution rule (below) fires.

### Mandatory immediate-execution rule

Once a SHIP patch is detected (whether being applied to the local repo by the user, or being authored by the assistant), the **very next patch in the same session** must begin Phase 7 execution. Specifically:

1. **Phase 7B is the highest-priority next patch.** The Phase 7B program-level work (theorem-registry / research_frontier / paper_catalog / INDEX / master_glossary / predictions / axiom-registry / README / programme_orientation) MUST land in the same session as the SHIP patch unless context-pressure forces deferral — in which case the deferred items go onto an explicit deferral list in the session-close handover (per the §15 backstop).
2. **Phase 7A paper-level work has flexible timing within the SHIP session.** The 10-file documentation suite (see "Four-Tier Documentation Suite Reconciliation" below), verification notebooks, and curated transcripts may fire in the SHIP session or be batched immediately after — but must not silently drop. If deferred, the deferral list in the session-close handover names each deferred file explicitly.
3. **Phase 7C execution (commit + final verification) closes the SHIP session.** Step H of `operating_system.md` §15 (session-close handover) explicitly verifies Phase 7B completion before the session can close cleanly; the auditable session-close question (below) is the canonical check.

The reactive pattern Session 135 demonstrated (Phase 7B work landing only after user asks "are the registries updated?") is **NOT** acceptable as standard discipline. The mandatory-immediate-execution rule converts "Phase 7B is sometimes done after SHIP" into "Phase 7B is part of every SHIP session, modulo explicit deferral list."

### Auditable session-close question

At every session close that includes a SHIP patch, the §15 Step H handover audit table MUST include the following explicit question, answered with full per-phase status:

> **"Is the post-SHIP protocol complete for the most recent SHIP in this session? Walk Phases 7A, 7B, 7C item-by-item. List any deferred items explicitly with the patch number that introduced the SHIP and the rationale for deferral."**

The session is **NOT** considered cleanly closed until this question is answered. A "yes, all complete" answer requires verification that:

- Phase 7A: 10-file documentation suite written; verification notebooks for new numerical claims; curated transcripts; bibliography entry; INDEX.md paper-artifact entries; series-README row; OSF deposit (or explicit deferral with rationale)
- Phase 7B: theorem-registry + research_frontier + paper_catalog + INDEX + master_glossary + predictions + axiom-registry + README + programme_orientation + anthology chapter (with handovers/ entry) + problem_histories + methods_catalogue (or explicit deferral list)
- Phase 7C: repository commit + push + final verification per H1–H5

A "no, items deferred" answer requires the deferral list to be explicit, machine-readable (item identifier per checklist + reason + estimated patch budget), and inherited into the next-session bootup as priority work.

---

## Four-Tier Documentation Suite Reconciliation (added 20 May 2026, Patch 0481M)

The A1–A7 enumeration in Section A covers the **seven companion documentation files** (mechanism, glossary, phenomena, philosophy, development, reviews, keywords). At the time the checklist was written (20 April 2026), this was the operative documentation suite.

Subsequent corpus evolution (the Four-Tier Documentation Discipline added 26 April Session 3 per `operating_system.md` §4) extended the operative suite to **ten companion documentation files** by adding three Tier-1 / Tier-3 / Tier-4 files:

| File | Tier | Purpose | Section A item | OS reference |
|---|---|---|---|---|
| `mechanism-[S]-[N].md` | (synthesis) | Step-by-step mechanism narrative | A1 | §4 Phase 7 |
| `glossary-[S]-[N].md` | (synthesis) | Paper-specific terms by category | A2 | §4 Phase 7 |
| `phenomena-[S]-[N].md` | (synthesis) | PHEN-E + PHEN-P + PHEN-V inventory | A3 | §4 Phase 7 |
| `philosophy-[S]-[N].md` | (synthesis) | Epistemological framing | A4 | §4 Phase 7 |
| `development-[S]-[N].md` | Tier 3 | Vignettes per development arc; intellectual history | A5 | §4 Four-Tier + §15 |
| `reviews-[S]-[N].md` | (synthesis) | Reviews + FAQ; consolidated review summary | A6 | §4 Phase 7 |
| `keywords-[S]-[N].md` | (metadata) | Keywords + PACS/MSC codes + cross-refs | A7 | §4 Phase 7 |
| **`changelog-[S]-[N].md`** | (chronological) | **Per-version diff narrative; version-archaeology source** | **A8 (NEW)** | **§11 version-archaeology architecture** |
| **`reasoning-[S]-[N].md`** | Tier 4 | **Verbatim Opus reasoning capture (substantive physics decisions)** | **A9 (NEW)** | **§4 Four-Tier Documentation Discipline** |
| **`transcript-[S]-[N].md`** | Tier 1 (pointer-map) | **Per-patch transactions / per-session pointer index into raw transcripts** | **A10 (NEW)** | **§4 Four-Tier + §11** |

**A8, A9, A10 are now part of the mandatory Phase 7A suite.** The seven-file framing in A1–A7 predates the Four-Tier Discipline and is no longer the complete picture. Treat the suite as ten files; the additional three are equally mandatory at SHIP unless explicit deferral applies.

**Where each file lives.** All ten files live in `flagship_papers/<paper>/documentation_suite/` for flagship papers (per the per-paper subfolder structure adopted with SS-9 at Patch 0274) or in `series_<name>/companions/` for series papers (legacy location preserved for SS-1 through SS-8 and SM-1 through SM-10).

**Why this reconciliation matters.** Session 135's paper-completion-sequence patches included substantive content additions across all ten files: 0481b (SHIP markers across 9 files), 0481d (development), 0481e (reasoning), 0481f (transcript), 0481g (reviews), 0481j (5 synthesis files mechanism + glossary + philosophy + phenomena + keywords), with the changelog updated as part of the v2.0 v1.0 SHIP itself at Patch 0479. The actual work fired against the ten-file pattern even though the checklist enumerates seven; codifying the ten-file pattern here removes the ambiguity.

**Trigger 1 vs Trigger 2 reconciliation.** The Tier-3 development file and Tier-4 reasoning file accumulate across sessions per the Trigger 1 per-session discipline (`operating_system.md` §4); they do NOT need to be re-written at SHIP, only audited for completeness through the SHIP session and frozen at the SHIPPED state. The Tier-1 transcript file (per-patch transactions / per-session pointer index) similarly accumulates and audits at SHIP. The other seven files (mechanism, glossary, phenomena, philosophy, reviews, keywords, changelog) are SHIP-time deliverables that may be drafted iteratively but reach their authoritative published state at SHIP.

---

## Anti-Collision Strategy for Concurrent Next-Window Work (added 20 May 2026, Patch 0481M)

The Phase 7B program-level work touches files (theorem-registry.md / research_frontier.md / paper_catalog.md / INDEX.md / master_glossary.md / predictions.md / axiom-registry.md / README.md / programme_orientation.md) that are programme-wide registries. Other Opus windows working on parallel work may concurrently modify the same files. The collision risk concentrates on **"Last updated:" header tops** where every patch prepends a new entry.

**Discipline (codified from Session 135 Patches 0481b–L pattern):**

1. **Identify which programme-level files have concurrent next-window activity.** At SHIP time, the assistant should know (from the cross-window handover seed or from the session-open audit) which programme-level files the next Opus window is actively writing to. As of Session 135 close: the next window (Session 136 Patch 0482) was actively writing to `research_frontier.md` (advancing OPEN-FP-SF-2-CHIR to v3.0+ Layer 4 closure scoping).

2. **For files with active concurrent work: anchor on stable inline content, not "Last updated:" header tops.** The "Last updated:" header at the top of each programme-level file is the high-frequency contested anchor — both Opus windows want to prepend new entries there. Anchoring on the inline content the SHIP patch is actually updating (a specific paper row in `paper_catalog.md`, a specific entry in `INDEX.md`, a specific ledger row in `axiom-registry.md`, a specific PRED-O entry in `predictions.md`) avoids the collision entirely. The cost is a stale "Last updated:" header at the top of the file; this is acceptable because the substantive content IS current and the inline content is the auditable record.

3. **For files without active concurrent work: prepend at the "Last updated:" header top as standard.** README.md, axiom-registry.md, predictions.md, theorem-registry.md, master_glossary.md typically don't have concurrent next-window activity unless the next window is also doing SHIP-adjacent work. For these, the standard header-top prepend pattern applies.

4. **Surgical inline updates beat whole-file rewrites.** A SHIP at v2.0 v1.0 should update the inline Capotauro row in `paper_catalog.md` rather than rewriting the whole table; should update the Capotauro entry in `INDEX.md` rather than restructuring the directory map; should add new ledger entries in `axiom-registry.md` rather than reorganising the per-paper attribution table. The surgical pattern preserves provenance and minimises collision surface.

5. **Bundle related programme-level updates into one patch where the anchor pattern permits.** Patch 0481k bundled `master_glossary.md` + `paper_catalog.md` + `INDEX.md` into a single patch because each used a distinct stable anchor (end-of-file H2 append + inline row + 3 of 5 inline entries respectively); they didn't share anchors with each other or with the next-window patch. Patch 0481L bundled `README.md` + `predictions.md` + `axiom-registry.md` similarly. The bundling reduced patch count while preserving anti-collision safety; the alternative (one patch per file) would have added 5 more patches to Session 135's count without any safety benefit.

6. **If a collision occurs at apply time:** the recovery is to drop the colliding patch and re-author the surgical update against the post-collision state of the file. Session 135's Patch 0481a (research_frontier.md update) was dropped after collision with next-window Patch 0482; the durable content was preserved at the theorem-registry (Patch 0480) + changelog (Patch 0479) + handover (Patches 0481, 0481c) anchors instead.

7. **Patch number collision is a real category.** Programme-level patches (this protocol-update patch series; future cross-window infrastructure work) authored by one Opus window may use patch numbers the other window has already claimed. The convention: when the next forward-integer patch number is taken by a concurrent window, continue the current sequence with alpha-suffix continuation (e.g., 0481M, 0481N when 0482 is taken; 0482a, 0482b when 0483 is taken). The alpha-suffix sequence preserves the "all this work belongs to the same logical campaign" provenance signal that pure integer renumbering would obscure. Session 135's 0481a–L sequence is the established precedent for this discipline.

**Anchor-safety hierarchy (most to least safe):**

| Anchor type | Safety | Example |
|---|---|---|
| End-of-file H2 section append | HIGHEST | master_glossary.md new "## Capotauro v2.0 cross-sector unification terms" section at Patch 0481k |
| Inline content update on unique substring | HIGH | paper_catalog.md Capotauro row version-field update at Patch 0481k |
| Surgical inline entry update | HIGH | INDEX.md entry at line 61 update at Patch 0481k |
| Append after maintainer footer | MEDIUM | axiom-registry.md ledger entries #61, #62 after #60 |
| Prepend at "Last updated:" header top of programme-level file with concurrent next-window activity | LOW | research_frontier.md prepend during concurrent SF-2 v3.0+ scoping work |
| Whole-file rewrite | DO NOT USE for programme-level files unless explicitly authorised |

---

## Session 135 Worked Example (added 20 May 2026, Patch 0481M)

Session 135 produced the largest single-session patch count in the Capotauro paper line and is the canonical worked example for the SHIP protocol's two-phase structure (reviewer/SHIP-closeout phase + paper-completion-sequence phase).

### Phase 1: Reviewer rounds and SHIP closeout (Patches 0466–0481)

16 normal-numbered patches across the v0.9 reviewer cycle and SHIP closeout:

| Patch | Scope | Phase |
|---|---|---|
| 0466–0469 | v0.8.1 round-1 reviewer letters (Grok + CoPilot + ChatGPT) | reviewer cycle |
| 0470–0472 | v0.9 polish incorporating round-1 feedback | reviewer cycle |
| 0473–0476 | v0.9 round-2 reviewer letters + ChatGPT round-2 revised | reviewer cycle |
| 0477–0478 | SHIP closeout protocol setup (Steps 1–2) | SHIP closeout |
| 0479 | **SHIP PATCH** — title block bump to `Version 2.0 v1.0 SHIPPED` | SHIP |
| 0480 | theorem-registry.md Last-updated header advance for paper-publication venue confirmation | Phase 7B |
| 0481 | session-close handover at `handovers/2026-05-19_session_135_capotauro_v2.0_v1.0_SHIPPED.md` | Phase 7C |

### Phase 2: Paper-completion sequence (Patches 0481a–L)

12 paper-completion-sequence patches (alpha-suffix continuation because Patch 0482 was opened by the next Opus window for SF-2 v3.0+ scoping):

| Patch | Scope | Phase | File(s) |
|---|---|---|---|
| 0481a | research_frontier.md (DROPPED due to collision with Patch 0482) | Phase 7B | research_frontier.md |
| 0481b | doc-suite SHIP markers across 9 files | Phase 7A | 9 of 10 documentation_suite files |
| 0481c | cross-window handover seed | Phase 7C | handovers/2026-05-19_session_135_sf2_v2.0_next_window_seed.md |
| 0481d | Tier-3 vignettes 36–40 | Phase 7A | development-capotauro.md |
| 0481e | Tier-4 reasoning §19–§23 | Phase 7A | reasoning-capotauro.md |
| 0481f | per-patch transcript transactions 0466–0481e | Phase 7A | transcript-capotauro.md |
| 0481g | consolidated review summary Part 3 | Phase 7A | reviews-capotauro.md |
| 0481h | anthology chapter v2.0 substantive refresh | Phase 7B | book_project/chapters/capotauro_what_was_always_there.md |
| 0481i | programme_orientation.md Chapter 22f Capotauro v2.0 extension | Phase 7B | programme_orientation.md |
| 0481j | bundled substantive doc-suite refresh (5 files) | Phase 7A | mechanism + glossary + philosophy + phenomena + keywords |
| 0481k | programme-level catalog updates (3 files) | Phase 7B | master_glossary + paper_catalog + INDEX |
| 0481L | stale-registry catch-up (3 files) | Phase 7B | README + predictions + axiom-registry |

**Session 135 total: 28 patches** (16 normal + 12 paper-completion-sequence). All applied cleanly to origin/main except 0481a which was dropped on collision with concurrent next-window Patch 0482.

### What this worked example demonstrates

- The two-phase structure (SHIP + paper-completion-sequence) is the canonical SHIP-session shape.
- The paper-completion sequence took 12 patches because it fired reactively from user audit ("are the registries updated?") rather than as a single planned protocol execution. **Under the mandatory-immediate-execution rule (above), the same content would land in fewer patches** — most of Phase 7B can bundle into 3–4 patches per the anti-collision strategy if planned at SHIP time rather than discovered at audit time.
- Patches 0481a's collision and recovery demonstrate the anti-collision discipline's value: the durable content from the dropped patch was preserved at alternative anchors (theorem-registry + changelog + handovers), so no information was lost; only the routing was adjusted.
- The 28-patch count is **not** a target for future SHIPs. Future SHIP sessions running the mandatory-immediate-execution rule from the SHIP patch itself should target ~20–24 patches total (16 reviewer/SHIP-closeout + 4–8 paper-completion-sequence, depending on whether next-window collision avoidance forces additional bundling).
- **Patch number collision discipline (Patch 0481M precedent).** When this very protocol-update patch was authored, the next forward-integer patch numbers 0482 and 0483 were already claimed by the next Opus window (SF-2 v3.0+ Layer 4 closure trajectory opened at Patch 0482; downstream patches taking 0483 and possibly 0484). The patches that codify the SHIP Trigger Protocol therefore continue the Session 135 alpha-suffix sequence as 0481M and 0481N rather than using 0483/0484. This is the canonical recovery for patch-number collisions with concurrent windows: continue the current logical campaign's alpha-suffix sequence; the suffix preserves the "all this work belongs to the same logical campaign" provenance.

---

- **20 May 2026 (Patch 0481M)**: SHIP Trigger Detection and Mandatory Immediate Execution + Four-Tier Documentation Suite Reconciliation + Anti-Collision Strategy for Concurrent Next-Window Work + Session 135 Worked Example sections added in response to Session 135's reactive paper-completion-sequence pattern (12 sequential patches driven by user audit "are the registries updated?" rather than single-pass protocol execution). The Phase 7A/7B/7C partition from Patch 0422D addressed *which items drop*; this addition addresses *when execution fires* (grep-able SHIP trigger detection + mandatory next-patch Phase 7B fire) and *how the 10-file documentation suite reconciles* with the original A1–A7 enumeration (A8 changelog + A9 reasoning + A10 transcript added). Anti-collision strategy codifies the Patches 0481b–L pattern (anchor-safety hierarchy: end-of-file H2 append > inline content update > surgical entry update > "Last updated:" header prepend with active concurrent work) as standard discipline. Auditable session-close question added to make Phase 7B completeness verifiable from outside the executing context. Patch number 0481M (alpha-suffix continuation of Session 135 sequence) rather than 0483 because Patches 0482+ were claimed by the next Opus window (SF-2 v3.0+ Layer 4 closure trajectory); the alpha-suffix recovery is itself codified as standard discipline in the Anti-Collision Strategy section.
