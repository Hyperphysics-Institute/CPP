# The Five-Artifact Taxonomy

**Location:** `book_project/five_artifact_taxonomy.md`
**Established:** 18 May 2026 (Session 132 Patch 0434A)
**Purpose:** Distinguish the five distinct artifacts the CPP programme is producing or will produce, so that the operating system, paper-completion workflow, and session-close handovers route work to the correct artifact. Prior to this document, two of the five were conflated under the label "TATWD," producing real friction in session-handover briefs.
**Audience:** Future Opus sessions opening to do post-paper-completion work; human collaborators understanding which artifact is in scope for any given task.

---

## Why this document exists

Until Session 132, the CPP corpus contained ambiguous overlap between (a) the programme's master technical narrative used as a working orientation document for the next-session Opus and end-to-end framework readers, and (b) the eventual popular-rigorous book targeted at educated non-specialists in the *Reality Is Not What It Seems* tradition. Both were labeled "TATWD" (*Tetrahedrons All the Way Down*) because the working title for (b) was *Tetrahedrons All the Way Down* and (a) was envisioned as eventually becoming (b).

The conflation produced a recurring failure mode: session-handover briefs would direct "TATWD integration" at v1.0 SHIP, ambiguous between "update the working orientation document" (tractable, established practice) and "write a chapter of the popular book" (not yet possible — book cannot be written before programme unification). The next-session Opus would either default to orientation-document updates (correct but with a misleading label) or attempt book-chapter work (wrong artifact for the current programme stage).

Session 132 surfaced the ambiguity during organizational work following the Reading C Q5 Layer 3 closure (Sessions 124-131). The resolution: distinguish five artifacts explicitly, each with its own definition, audience, completion criteria, and trigger for work.

---

## The five artifacts

### Artifact 1 — The Anthology (Book 1)

**What it is.** A collection of self-contained 4,000-5,000-word short stories at *Scientific American* / Rovelli register, one chapter per CPP paper. Each chapter tells the paper's intellectual journey from problem to result without forcing it into a larger arc. Each chapter stands on its own; a reader picking up the anthology and reading one chapter receives a complete experience.

**Audience.** Educated non-specialists who want to understand what a paper *did* — the question it attacked, the path the work took, what it found, what it means, what remains open. Readers of Rovelli, Greene, Randall, Carroll.

**Status (18 May 2026).** Six chapters extant: SS-7 (*Eight Nuclei in a Row*), SS-8 (*Octahedron in Magnesium*), SS-9 (*The Polyhedron's Conditions*), SF-4 (*Where Two Problems Met*), SF-2 (*The Bracelet's Catalyst*), Capotauro (*What Was Always There*). All in `book_project/chapters/` at production quality.

**Completion criteria.** The anthology is complete when every shipped v1.0+ paper has a chapter. Currently five flagship v1.0 papers shipped (SS-9, SF-4, SF-2, Capotauro, plus SS-7 v1.2 and SS-8 v1.0+ in the strong-sector series); all six are anthologized. As new flagship papers ship, new chapters are written.

**Trigger.** **Mandatory at v1.0 SHIP** per `paper_completion_checklist.md` C11 (codified 18 May 2026 Patch 0434D). Sub-chapter ad-hoc trigger remains available for sub-stories within a single paper.

**Governance.** `templates/anthology_chapter_template.md` (204 lines of craft documentation — voice, register, dramatic-centerpiece-finding, structural arc, honesty discipline, calibration questions).

**Doable at current programme stage:** YES. Anthology chapters can be produced incrementally as papers ship, with no dependency on programme unification.

---

### Artifact 2 — TATWD: *Tetrahedrons All the Way Down* (Book 2)

**What it is.** A single coherent popular-rigorous book at *Reality Is Not What It Seems* / Rovelli register, tracing the framework's full arc from the originating intuition through axioms, primitives, sector-by-sector results, and unification. Single narrative arc; beginning, middle, end as a coherent journey.

**Audience.** Educated non-specialists reading the whole framework end-to-end, in sequence, as a unified story rather than as discrete papers.

**Status (18 May 2026).** PLANNING. Outlines exist (`TATWD_outline.md` legacy and `TATWD_outline_revised.md` current, ~34 KB). Framing transcript exists (`development_transcript_TATWD_framing.md`, ~17 KB). Chapter arcs scaffolded in `chapter_arcs/`. No chapters drafted.

**Completion criteria.** The book requires the framework's full scope to be settled. "Full scope" means: the SD-line foundational architecture closed at programme level (axioms, conscious-point ontology, dipole-pair sea, 600-cell lattice), every observable sector closed at v1.0+ flagship paper (Strong, Standard Model, Electroweak, Quantum Mechanics, Special/General Relativity, Cosmology), and the unification claims made explicit at theorem-registry level. Until these are in place, the book's middle and end cannot be written; the beginning could be drafted but would likely need rewriting once the rest is in place.

**Trigger.** Programme unification + Thomas's decision to begin drafting. Roadmap maintenance continues as papers ship (chapter pointers updated, scope estimates refined); chapter drafting waits.

**Governance.** `book_project/TATWD_book_2_roadmap.md` (NEW Session 132 Patch 0434B) tracks scope, dependencies, pointer-list of what each chapter will need. `TATWD_outline_revised.md` maintained as the canonical outline.

**Doable at current programme stage:** NO. Premature drafting risks producing prose that needs rewriting after subsequent paper closures. What CAN be done now is roadmap maintenance: refining chapter scope, identifying which paper closures unblock which chapters, tracking dependencies.

---

### Artifact 3 — The Professional Derivation (Book 3)

**What it is.** A compilation of all v1.0+ flagship CPP papers, organized by sector, with editorial transitions between papers and a unifying introduction + conclusion. Effectively the .tex source files bound together with cross-paper segues.

**Audience.** Working physicists wanting the rigorous derivation in its entirety, sector by sector, with cross-paper context provided. Reference work rather than narrative read-through.

**Status (18 May 2026).** PLANNING. The constituent papers exist (SS-7 v1.2, SS-8, SS-9 v1.0, SF-4 v4.4, SF-2 v1.0, Capotauro v1.0); the binding compilation has not been assembled.

**Completion criteria.** Sector coverage at v1.0+ for the framework's full empirical scope (parallels Book 2's requirements) plus pedagogical sequencing decisions (which paper goes in which order; which cross-paper context belongs in segues vs in individual papers' introductions).

**Trigger.** Substantial paper coverage (likely 12-20+ v1.0+ flagships) + Thomas's decision to begin compilation. Could be produced incrementally if a clean per-sector compilation pattern emerges (e.g., Strong-Sector Volume could ship when SS-N papers are complete, with later volumes following per-sector).

**Governance.** No dedicated template yet. Sector-organization decisions follow `paper_catalog.md` structure.

**Doable at current programme stage:** PARTIAL. Per-sector volumes could ship as individual sectors reach completeness; full compilation is post-unification.

---

### Artifact 4 — The Pedagogical Textbook (Book 4)

**What it is.** A textbook that walks a student from conventional physics (Standard Model, GR, QM as taught) to CPP unification. Pedagogical sequencing; problem sets; worked examples; the structure of a physics graduate-level textbook.

**Audience.** Physics students at advanced undergraduate or graduate level; physicists wanting to learn CPP from first principles with the pedagogical scaffolding intact.

**Status (18 May 2026).** NOT STARTED. No outline, no chapter drafts, no design documents.

**Completion criteria.** Programme unification + substantial pedagogical-design phase (which conventional-physics on-ramps to build, what order, what prerequisites, problem-set construction, worked-example selection).

**Trigger.** Programme unification + Thomas's decision to begin design phase. Likely a multi-year project after unification is achieved.

**Governance.** None yet. Will require its own template + outline + chapter-arc planning when triggered.

**Doable at current programme stage:** NO. Both prerequisites (unification + pedagogical design) are post-current-stage.

---

### Artifact 5 — The Programme Orientation Document

**What it is.** `programme_orientation.md` (formerly `CPP_the_theory.md` — renamed Session 132 Patch 0434C to remove conflation with Book 2). A continuously-maintained master technical narrative serving the programme's own orientation needs: new context windows reading it to understand current programme state; human collaborators reading the framework end-to-end at full technical register; cross-paper context preserved in one canonical document.

**Audience.** The next-session Opus opening to work on the programme; human collaborators engaging the full framework at technical register; reviewers and external scientists wanting an end-to-end overview at greater depth than per-paper abstracts.

**Status (18 May 2026).** ACTIVE — maintained continuously. Updated at every v1.0 SHIP and programme-architecture event per `paper_completion_checklist.md` C10 cadence. Patch 0435 (Session 132) integrated Reading C closure + OPEN-SD-CHIR-PRIMITIVE umbrella + THEO-SD-CHIR-1 into the document.

**Completion criteria.** Not a book; never "complete" in a publication sense. Always reflects current programme state. Staleness audit at session-close via comparison with `paper_catalog.md` Last-updated header.

**Trigger.** Mandatory at every v1.0 SHIP and programme-architecture event per `paper_completion_checklist.md` C10 + `operating_system.md` §10 cadence + §15 audit step.

**Governance.** `paper_completion_checklist.md` C10 (mandatory checklist item); `templates/operating_system.md` §10 (cadence calibration) + §15 (audit step); no dedicated craft template yet (calibration is by reading existing content as precedent; a `templates/programme_orientation_update_template.md` could be created if/when the practice has enough invariance to justify codification — deferred per Session 132 decision).

**Doable at current programme stage:** YES. Continuous maintenance is the established practice.

---

## Cross-reference table

| # | Artifact | Audience | Status | Trigger | Doable Now? |
|---|---|---|---|---|---|
| 1 | Anthology (Book 1) | Educated non-specialist, paper-at-a-time | 6 chapters extant | Mandatory at v1.0 SHIP (C11) | YES, paper-by-paper |
| 2 | TATWD (Book 2) | Educated non-specialist, full framework | Planning | Programme unification | NO, roadmap only |
| 3 | Professional derivation (Book 3) | Working physicist, rigorous reference | Planning | Substantial paper coverage | PARTIAL, per-sector volumes possible |
| 4 | Pedagogical textbook (Book 4) | Physics student | Not started | Unification + design phase | NO |
| 5 | Programme orientation document | Next-session Opus, end-to-end technical reader | Active, continuous | Mandatory at v1.0 SHIP + architecture events (C10) | YES, continuous |

---

## What this taxonomy resolves

**Resolution 1 — TATWD integration ambiguity.** "TATWD integration at v1.0 SHIP" (paper_completion_checklist.md C10) now unambiguously refers to Artifact 5 (programme orientation document maintenance), not Artifact 2 (Book 2 chapter authoring). The filename rename `CPP_the_theory.md` → `programme_orientation.md` (Patch 0434C) makes the artifact identity self-evident at the path level.

**Resolution 2 — Anthology chapter as mandatory C-item.** Artifact 1 production is now hard-coded into `paper_completion_checklist.md` C11 (Patch 0434D), removing the failure mode where anthology chapters were produced reactively after retrospective audit caught the gap (Capotauro chapter at Patch 0416K, written ~1 session after v1.0 SHIP; SF-2 chapter at Patch 0374 at v1.0 SHIP itself but as ad-hoc decision rather than automatic trigger).

**Resolution 3 — Book 2 roadmap as separate scheduled artifact.** Artifact 2 roadmap maintenance gets its own document (`book_project/TATWD_book_2_roadmap.md`, Patch 0434B), distinct from Artifact 5 maintenance. Roadmap captures what each future Book 2 chapter will need from the programme, without attempting to draft the chapters prematurely.

**Resolution 4 — Books 3 and 4 deferred but acknowledged.** Artifacts 3 and 4 are explicitly post-unification artifacts; this document is their first repo-level acknowledgment. No work proceeds on them at the current programme stage. Future scheduling decisions reference this taxonomy.

---

## Rationale captured from Session 132 deliberation

The five-artifact taxonomy emerged from a Session 132 conversation that began with Thomas requesting a handover for new physics (Q5 or Q6 derivation) and observed the conversation drifting into methodology work instead. The methodological drift was real and worth naming: a request for physics produced first a handover-system audit, then a handover that pointed at TATWD integration (the conflated artifact), then the next-window Opus attempting work whose definition was undefined.

Thomas's resolution: the four-book taxonomy (Books 1-4) plus recognition that what was being called "TATWD" in `paper_completion_checklist.md` C10 was actually Artifact 5 (programme orientation document). The five-artifact taxonomy + filename rename + mandatory anthology trigger collectively close the failure mode by making each artifact's identity, audience, and trigger unambiguous at the operating-system level.

Methodologically, this is an instance of "the system pointed forward without checking whether the destination existed." Future session-handover briefs should verify that the artifact being targeted has a defined identity before directing work at it. The five-artifact taxonomy is itself the diagnostic instrument: if a handover brief cannot specify which of the five artifacts is in scope, the brief is malformed.

---

**Last updated:** 18 May 2026 (Patch 0434A — initial creation; established five-artifact taxonomy + Session 132 rationale captured).
