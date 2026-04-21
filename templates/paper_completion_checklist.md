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

**Deliverables:** 7 companion documentation files + N verification
notebooks + updates to up to 12 registry files + updates to 3 navigation
files + curated transcripts + OSF registration + git commit/push +
verification pass.

**Filename pattern:** `[S]-[N]` is the paper identifier (e.g., `SS-7`).
`[S]` is the series prefix (`SS`, `SM`, `EW`, `QM`, `SD`). `[N]` is the
paper number. Canonical filenames never include version suffixes (per
`operating_system.md` §11); version lives in the internal CHANGELOG only.

**Do NOT duplicate this content elsewhere.** The prior drift that caused
`problem_histories/` to be missed in SS-7 v1.1 Phase 7 was produced by
three parallel enumerations of the same content. This file is now the
sole source of truth for atomic tasks. Reference procedures live in
`operating_system.md` §10; atomic tasks live here.

---

## A. Companion documentation suite (7 files)

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

## B. Verification notebooks

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

## C. Registry updates — repository-root content documents

Each item atomic; cite the reference procedure in `operating_system.md`
§10 for how to execute. Trigger conditions noted per item — skip items
whose trigger is not met.

- [ ] **C1.** `theory-overview.md` — update if the paper produced new
  quantitative results, new formulas, resolved/new open problems, or
  changed series status. Procedure: `operating_system.md` §10
  "theory-overview.md update procedure."

- [ ] **C2.** `axiom-registry.md` — update if the paper used any axiom
  not yet in the registry, consolidated axioms, or introduced new
  predictions. Procedure: `operating_system.md` §10 "axiom-registry.md
  update procedure." Note the reviewer-ID reconciliation rule in that
  procedure.

- [ ] **C3.** `theorem-registry.md` — update if the paper introduced or
  referenced new theorems or corollaries, or resolved a problem tracked
  in the theorem registry's Open Problems table. Procedure:
  `operating_system.md` §10 "theorem-registry.md update procedure."

- [ ] **C4.** `master_glossary.md` — update if the paper introduced any
  term, acronym, particle, cage structure, or mechanism not already in
  the glossary. Also scan `founders_vision.md` for new terms. Procedure:
  `operating_system.md` §10 "master_glossary.md update procedure."

- [ ] **C5.** `Research_Frontier.md` — update if the paper addressed any
  OPEN-*, CONJ-*, or PROP-* entry (status change, resolution, falsification,
  new registration, dependency graph change). Procedure:
  `operating_system.md` §10 "Research_Frontier.md update procedure."

- [ ] **C6.** `predictions.md` — update if the paper produced any new
  quantitative prediction or changed the status of an existing one.
  Procedure: `operating_system.md` §10 "predictions.md update procedure."

- [ ] **C7.** `paper_catalog.md` — always update on paper completion.
  Add or refresh the paper row: version, date, status, reviewer verdicts,
  open-problem registrations, target for next paper. Update total paper
  count. Procedure: `operating_system.md` §10 "paper_catalog.md update
  procedure."

- [ ] **C8.** `founders_vision.md` — update if the paper represents a
  significant programme advance OR if new physical intuitions were
  captured during the sessions that produced the paper. Write a
  one-paragraph milestone note for significant advances. Procedure:
  `operating_system.md` §7 "Founders Vision Protocol" (referenced from
  §10).

- [ ] **C9.** `future_projects.md` — update if the paper closed a target,
  shifted priorities, or surfaced new research targets. Procedure:
  `operating_system.md` §10 "future_projects.md update procedure." Check
  the "current #1 priority" line for staleness.

- [ ] **C10.** `CPP_the_theory.md` — update if the paper produced new
  results that belong to any chapter (always the case for substantive
  papers). Add results in connected prose (not bullets). Update the
  Prediction Scorecard in Part VI. Procedure: `operating_system.md`
  §10 "CPP_the_theory.md update procedure."

- [ ] **C11.** `bibliography/cpp_references.bib` — add a BibTeX entry for
  the new CPP paper; add BibTeX entries for any external works newly
  cited; verify cite keys match the paper's `.tex`. Procedure:
  `operating_system.md` §10 "bibliography/cpp_references.bib update
  procedure." **Easy to miss: this file lives in `bibliography/`, not
  at the repo root.** Do not add entries to deprecated per-series or
  per-paper `.bib` files.

- [ ] **C12.** `problem_histories/` — update if the paper resolved (fully
  or partially) or substantially advanced any OPEN-*, CONJ-*, or PROP-*
  entry, OR if it registered a new entry with substantive narrative arc
  beyond bare birth-registration. Create or update `PH-[ID].md` per the
  procedure. Apply the symmetric-honesty threshold: document what the
  resolution did NOT do, not only what it did. Procedure:
  `operating_system.md` §10 "problem_histories/ update procedure."
  **Easy to miss: `problem_histories/` is a registry-adjacent directory,
  not in the repo root alongside the other content documents. This is
  the item that drove the 20 April 2026 consolidation. Do not skip C12.**

---

## D. Navigation updates

These files track structure rather than substance. All three are typically
updated on every paper completion.

- [ ] **D1.** `README.md` — add the paper to the Registered Papers table;
  update paper count; add to Strongest Results if the paper produced a
  headline result; update axiom summary line if axiom count changed.
  Procedure: `operating_system.md` §10 "README.md update procedure."

- [ ] **D2.** `INDEX.md` — add every new file created during this paper's
  production (the `.tex`/`.pdf`/`.bib`, companion suite files, development
  transcripts, new figures, notebooks, problem-history files). Group
  under correct folder sections; add folder headings if new folders were
  created. Procedure: `operating_system.md` §10 "INDEX.md update
  procedure."

- [ ] **D3.** `series_[name]/README.md` — add the paper to the series
  paper table; update series description if scope changed; add new
  cross-references between papers in the series. Procedure:
  `operating_system.md` §10 "series_[name]/README.md procedure."

---

## E. Development transcripts

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

## F. OSF registration

- [ ] **F1.** If the paper has no OSF DOI yet: create a new OSF project,
  obtain a pending DOI, attach the final PDF.

- [ ] **F2.** If the paper has an existing OSF DOI from an earlier
  version: update the OSF project with the new PDF and a CHANGELOG
  summary.

- [ ] **F3.** Update the paper's `.tex` CHANGELOG to reference the OSF
  DOI.

- [ ] **F4.** Update `paper_catalog.md` row with the current OSF DOI
  status (this partially overlaps C7; executing C7 after F4 captures it
  naturally).

---

## G. Repository commit

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

## H. Final verification

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
  the paper appears in `Research_Frontier.md` with current status.

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
