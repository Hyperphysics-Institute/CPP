# CPP Programme To-Do List

**Location**: `/CPP/todolist.md` (repo root, parallel to `research_frontier.md`, `future_projects.md`, `paper_catalog.md`).

**Purpose**: Track small carried-over items, deferred protocol steps, and hygiene gaps that don't warrant full `future_projects.md` entries but must be cleared before the next paper begins. The "easy to lose" things — things that compound if not externalized.

**Discipline (introduced 7 May 2026 Session 33 close)**: A new paper does not start until this file's **P1 — Must clear before next paper** section is empty. Items move to **Cleared items (history)** at the bottom when completed (with date and patch number for audit). Items can also be reclassified to `future_projects.md` if they grow into multi-session projects, or deleted as no-longer-applicable with a note.

## How this file relates to other tracking files

- **`future_projects.md`** — registered active projects with full mechanism / falsifier / companion fields. Multi-session work with a clear deliverable. SS-9 anthology chapter (A.3) and TATWD integration (A.4) live there, not here.
- **`research_frontier.md`** — last-updated session-by-session log of the programme's frontier state. Programme-level open problems and their status.
- **`parallel_development_roadmap.md`** — the phased roadmap + to-do for scaling CPP from solo to a collision-resistant parallel theorem-development team (coherence layer, integrity subsystem, Claude Code agentic pilot, escalation triggers). The living plan for the team-scaling initiative; this todolist tracks only its small carried-over items.
- **`session_logs/`** — per-session entries capturing what happened.
- **`todolist.md`** (this file) — *small carried-over items, deferred protocol steps, hygiene gaps*. Kept short on purpose. If an entry here grows beyond a few patches of work, promote it to `future_projects.md`.

A new item belongs here (rather than in `future_projects.md`) if it's: small enough to clear in one or a few patches; not its own multi-session project; or explicitly deferred from a session whose main work was different.

---

## Standing conventions (permanent — do NOT clear)

*Persistent workflow rules. Unlike TODO items, these are never "cleared"; they bind every future session.*

### CONV-001 — Presenting a repo file to the swarm/panel (one single copy block)

When Claude asks Thomas to present any repo file to the AI review panel (swarm), Claude must, **in the
chat response**, provide the whole package as **ONE single fenced copy-paste block** — so Thomas can
one-click-copy and paste it to each panel member without highlighting/copying multiple separate pieces.
That single block contains, in order: (1) the **GitHub links** to the file (blob form
`https://github.com/Hyperphysics-Institute/CPP/blob/main/<path>` and raw form
`https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/<path>`, valid after push); (2) a
**one-paragraph intro** framing the file for the swarm; (3) the **full rendered file content** (rendered
Markdown, NOT the patch/diff). All three inside the *same* fenced block. Rationale: Thomas presents to the
panel by pasting once; multiple separate blocks meant repeated highlight/copy/paste — never make him do
that, and never make him hunt for a file embedded in a patch. Template: `templates/presentation_file.md`.
This single presentation block is separate from the apply-and-push patch block (the patch applies the file;
this block hands it to the swarm). Registered 5 Jun 2026 Session 154; **updated 6 Jun 2026 Session 154 to
the single-block format at Thomas's request** (previously three separate elements).

### CONV-002 — Re-fetch high-risk shared files immediately before committing to them

Before committing any change to a **high-risk shared file**, re-fetch origin and re-read that file's current content, then build the edit on the latest version — never on a copy read earlier in the session. This is the lightweight collision-prevention discipline; for routine solo / few-window work it replaces the heavier post-hoc `collision_audit.sh` pass. High-risk files are the ones multiple work-streams touch, so a stale read is the main way concurrent work clobbers.

Procedure (committer, per high-risk file touched):
1. `git fetch origin && git reset --hard origin/main` (or re-clone) so the working tree matches the latest origin.
2. Re-open and re-read the target file; rebuild the intended edit against its current content.
3. Commit and push. If origin moved again between read and push, repeat.

High-risk shared files = the integration-owned list in `parallel_dev/scripts/collision_audit.sh` (`SHARED_REGEX`): `theorem-registry.md`, `predictions.md`, `axiom-registry.md`, `master_glossary.md`, `research_frontier.md`, `frontier_sectors/*`, `todolist.md`, `future_projects.md`, `paper_catalog.md`, `research_timeline.md`, `organizational_frontier.md`, `theory-overview.md`, `programme_orientation.md`, `README.md`, `INDEX.md`, `parallel_dev/lease_board.md`. The single source of truth for this list is that `SHARED_REGEX` — update it there, not here. Files inside a paper's own folder are low-risk and exempt. Registered 8 Jun 2026 Session 154.

### CONV-003 — Parameter-set provenance for load-bearing numbers (panel-requested, DM-1 v1.1)

Every **load-bearing numerical claim** in a paper, revision notice, registry entry, or review package states the **parameter set (and source patch/ledger) it was computed from**. At any **morphology / mechanism / model pivot**, every number carried across the pivot is **re-derived or explicitly rescaled at the new object's parameters** before being quoted — "same formula, stale parameters" is the failure this convention exists to prevent. Review packages for results with load-bearing numbers **embed runnable (stdlib) verification code**, and reviewers run it before verdict (SCRIPT-EXECUTED).

Origin: DM-1 v1.0 quoted the 0860 hoop ledger's collision energies (~1.95 MeV / ~0.78 keV; N=1183, m=264 MeV) in the Cross-Rod paragraph (N=5–60, m_el=1408 MeV); the paper's central velocity-dependence discriminant rested on a retired morphology's numbers, shipped v1.0, and passed the panel 4/4 — the values were internally plausible but untraced. Caught by in-house audit (Patch 1859) six days post-ship; convention requested independently by all four reviewers at the v1.1 re-ratification (Patch 1862). Author-side failure mode recorded in `templates/AI_team_expectations.md` (Opus). Registered 3 July 2026, Patch 1862.

### CONV-004 — The measured-coefficient (Galilean-layer) discipline (founder-ruled, DM sector first)

Where the substrate physics beneath a result is genuinely unresolved (DP density, lattice occupancy, ZBW
amplitude, cancellation/superposition factors), the programme may claim the STRUCTURE and let DATA fix the
coefficients that encode the unresolved depth — Galileo's law before Newton's mechanism; effective-theory
practice one level below where conventional physics believes anything exists. Rules: (1) every such number
carries a ledger tag — **MEASURED** (inverted from data through the claimed structure), **DERIVED**
(theorem-level from axioms), or **CONJECTURED** — and the tag travels with the number everywhere (CONV-003
provenance extended); (2) a measured coefficient is honest only under **overdetermination** — it must survive
channels it was not fitted to, pre-registered, no refit; the measured-vs-unknown count is kept visible, and
the moment unknowns outnumber measurements the work is curve-fitting and must say so; (3) the discipline
applies ONLY where derivation is premature — sectors holding zero-parameter DERIVED results (the programme's
strongest asset) are NOT re-framed; (4) the derivation layer remains the standing goal: with coefficients
pinned, the later axiomatic derivation is confirmed by overdetermination against numbers it did not fit — a
firewall the tags exist to guarantee (no measured value may silently leak into a "derivation" that then
"confirms" it). Origin: founder methodological ruling, 6 July 2026 (DM sector; D5/F3′ context), verbatim in
`founders_voice/founder_ruling_measured_coefficients_2026-07-06.md`. Registered Patch 1886.

### CONV-005 (v2, panel-ratified 22 Jul 2026 Patch 2764) — Blocking Hamiltonian-identity gate before every Markov-chain production run

Every act that runs (or re-runs) ANY Markov-chain sampler (Metropolis, HMC, or other) executes, BEFORE any
production sweep, a **blocking Hamiltonian-identity gate**, per distinct move type, interaction
implementation, boundary condition, external-field mode, and code path: **≥20 randomly generated states ×
≥20 proposed moves per state**, mandatorily including boundary-crossing moves, near-core moves,
particle-index edge cases (i = 0, i = N−1), deliberately large displacements, and the zero-move identity.
The incremental ΔH is compared against a from-scratch total-energy difference from an independent code
path: **|ΔH_inc − ΔH_full| ≤ 10⁻¹⁰·max(1, |ΔH_full|)** (typical target 10⁻¹²), plus the inverse-move
antisymmetry check ΔH(x→x′) = −ΔH(x′→x). ANY failure blocks production and the session reports the defect
instead. The gate re-runs after ANY change to energy computation, neighbor masks, boundary handling, or
source terms. The gate is written into the act's prereg and its PASS line is quoted in the record.
Invariance checks (permutation, periodic translation, energy/force-gradient consistency) are recommended
where the implementation admits them. Origin (v1, Patch 2758): the 2714 self-pair defect survived five
campaign acts and manufactured a 5.6σ artifact; the first five-move gate (B-CHECK-80, Patch 2754) caught it
before consuming a seed; the fixed re-run (Patch 2756) killed the anomaly at 0.02σ. v2 amendments ratified
by the CONV-001 panel at the S4-X bundle adjudication (Patch 2764): coverage 400 checks vs five; mixed
threshold; edge-case move classes; inverse-move test; all-MCMC scope; re-gate-on-change rule.

### CONV-006 — Authentication-before-adoption for artifacts of interrupted or externally-executed sessions (panel-ratified 22 Jul 2026 Patch 2764)

When a session finds completed computational artifacts it did not itself produce (stalled-window recovery,
parallel-agent output, any uncommitted work of uncertain provenance), the artifacts are NOT adopted on
trust or on memory. Before scientific adoption: (1) SHA-256 manifests for the code and data artifacts are
computed and committed with the authentication record; (2) every quoted number is reproduced by re-running
the frozen analyzers over the immutable raw archives; (3) **at least one full chain per distinct executable
configuration is regenerated from its recorded seed** to the bit-identical-sampling standard (accumulator
residues at the disclosed refresh level permitted), with the chain chosen by a rule stated BEFORE any
comparison is seen (e.g., cheapest); (4) more than one chain regenerates when conclusions depend on
chain-to-chain variance; (5) the authentication record commits BEFORE the artifacts' adoption patch or in
the same push. Clean-environment rerun is recommended, not mandatory (revisit on first discrepancy).
Origin: the RV-2714 stalled-window recovery (Patches 2761/2762); precedent authenticated by deterministic
reproduction; formalized with amendments by the CONV-001 panel at the S4-X bundle adjudication (Patch 2764).

### CONV-007 — Withheld-key admissibility (registered 29 Jul 2026 Patch 2874)

A withheld verification key issued with a CONV-001 dispatch must be a quantity that **(i)** is computable
from a committed artifact whose path is named in the dispatch — S2's requirement, established at Patch 2829
and what made honest verification possible — **AND (ii)** does **not** appear in any commit message,
docstring, README, prose file, or prior adjudication anywhere in the repository. Requirement (ii) must be
checked before the dispatch is issued, by grepping the full history (`git log --all --format=%B`) *and* the
artifact's own source, including its docstring. **A key failing (ii) is VOID and no execution ruling —
neither VERIFIED-EXECUTED nor fabrication — may be made on it.**

Originating failure: the Patch 2873 dispatch nominated the 2868 dt/vf ladders and sign as its key. Both
ladders appear verbatim in Patch 2868's commit message *and* in the target script's own `RESULT` docstring
block, so a seat could return all six values and the sign without executing anything. S2 returned correct
values and could be neither credited nor penalised. Verify script: `series_phenomena/cosmology/dark_matter/code/2874_key_void_check.py`
(6/6 values found in each location). The failure was the worker's, not the seat's — clause (i) was
satisfied and the complementary clause had never been written down.

### CONV-008 — Roster byte-identity check before scoring any CONV-001 round (registered 29 Jul 2026 Patch 2876)

**Before adjudicating any CONV-001 round, compare the returns pairwise for byte-identity or near-identity.**
Any identical pair is counted as **ONE seat position**, and the effective roster size is stated in the
adjudication's header *before any question is scored*. Independent models do not produce multi-thousand-word
identical returns; the near-certain cause is a duplicated paste at dispatch, and **no blame is assigned to any
seat** — the worker requests confirmation and proceeds on the reduced roster.

Originating history: **three occurrences.** Patch 2849 (Darwin final motion) caught it and established the
one-position rule, and requested confirmation before the next round. The SF-6 dispatch's first attempt hit it
again and **the worker did not catch it**, counting two identical declines as two independent positions and
drawing an unsound capability inference from the count. Patch 2876 hit it a third time. Per-round flagging has
failed to prevent recurrence, which is why the check is now a standing convention rather than a habit: the
check is cheap, the failure is silent, and an inflated roster count is indistinguishable from consensus.

---

### CONV-009 — Founder verbatim capture is a patch obligation, not a courtesy (registered 1 Aug 2026 Patch 2881)

**Any turn in which the founder supplies physics — a mechanism, a ruling, a correction, a decision on
scope or status — is captured VERBATIM to `founders_voice/` in the SAME patch that acts on it.** The
capture is the primary source; any conjecture entry, frontier update, paper passage, or panel dispatch
derived from it is secondary and must cite it by path. **The primary source is written FIRST, or at
minimum in the same `git am`. Registering a derivative before its source inverts the dependency and is
the error at Patch 2880.**

**Scope.** Verbatim means verbatim — the founder's own words, block-quoted, not compressed and not
tidied. Worker commentary is permitted but must be visibly separated (`**Worker note:**`) so that a
later reader can always recover what the founder actually said from what the worker made of it.

**Why this is a convention and not a reminder.** The founder reports the capture has been missed in
prior sessions whenever he has asked, i.e. it is a chronic cross-worker failure. The cause is
structural: the worker reasoning fragment rides inside the patch bundle and is carried by the
mechanical workflow, while founder capture has no trigger and therefore depends on memory. This is the
same shape as the roster duplication, which recurred three times under per-round flagging and stopped
only when it became a procedural step (CONV-008). **The founder's verbatim is the one source in the
corpus that cannot be reconstructed from anything else** — and this session demonstrated four separate
times that worker summaries drift from their sources, the source being right every time.

**Companion obligation.** The reasoning-capture rider has no exemption for addenda, corrections, or
adjudication records. Patch 2879 was skipped on the assumption that an addendum is bookkeeping; it
contained an adopted dissent and the re-scoping of an open item. **If a patch makes a judgment, it owes
a fragment.**

---

---

## P1 — Must clear before next paper (SS-10)

*(Empty — gate cleared 7 May 2026 Session 36 close patch 0288. SS-10 may begin.)*

The Session 36 P1 audit found that all originally-P1 items except TODO-002 were either deferred on external triggers (TODO-001) or were historical/programme hygiene that does not actually forward-block SS-10 (TODO-003, 004, 005, 006). Per this file's own escape-valve discipline (*"If a P1 item turns out not to actually block the next paper on reflection, demote it to P2 with a note explaining why"*), they were demoted to P2 and TODO-002 was cleared after its actual completion via patches 0286 + 0287 + commit `55c5986`. Result: P1 genuinely empty; SS-10 begins on a clean slate at the next session.

---

## P2 — At Thomas's discretion (not blocking next paper)

### TODO-001 — SS-9 Phase 7 Section A 7-companion documentation suite

**Status**: DEFERRED pending external-feedback trigger; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: The Two-Triggers discipline (`templates/paper_completion_checklist.md` lines 35-48) defers this until SS-9 is unambiguously done — meaning until either (a) v1.x revision ships and stabilizes after external feedback or (b) a reasonable post-posting window passes with no feedback. The trigger is gated on TODO-007 (public posting) and is *external* in nature, so the item cannot fire on its own and producing the 7 companion files prematurely risks rework. Demotion to P2 acknowledges that the file's own discipline is being honored: this is a deferred item awaiting an external trigger, not an item the next session must clear before starting SS-10.
**Trigger**: After (a) public posting (OSF + arXiv) lands AND (b) external-feedback window settles — either no v1.x revision arrives within Thomas's chosen window, or v1.x ships and stabilizes.
**Deliverable**: 7 companion files per `templates/paper_completion_checklist.md` Section A and `templates/documentation-suite.md`:
- `mechanism-SS-9.md` (A1) — step-by-step mechanism narrative with mathematical-correspondence table
- `glossary-SS-9.md` (A2) — paper-specific terms organized by category
- `phenomena-SS-9.md` (A3) — what the paper explains (PHEN-E empirical, PHEN-P predictions, PHEN-V consilience)
- `philosophy-SS-9.md` (A4) — epistemological framing
- `development-SS-9.md` (A5) — already exists as session-continuity file; may need final consolidation pass at v1.0+ trigger
- `reviews-SS-9.md` (A6) — all reviews + FAQ
- `keywords-SS-9.md` (A7) — keywords and registry cross-refs
**Estimated effort**: 1 dedicated session (~3-5 hours per checklist).
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-003 — Tier 4 reasoning recovery for chat window `a49b320e` (March 19 – April 6, 2026)

**Status**: PROGRAMME-LEVEL DEFERRED multi-session backlog; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: Recovery of substantive Opus reasoning into per-paper `reasoning-[ID].md` files for already-shipped historical papers (16 papers: SR-1, EW-1 through EW-5, SS-1, QM-1 through QM-6, SM-1 through SM-5) is hygiene work on the historical record, not a precondition for new paper work. SS-10's framing and execution do not depend on having recovered reasoning artifacts for unrelated earlier papers. This item should be revisited as a long-term backlog candidate; if it grows into a dedicated multi-session project, it should be promoted to `future_projects.md` rather than carried as a single TODO.
**Issue**: Foundational development of SR-1, EW-1 through EW-5, SS-1, QM-1 through QM-6, SM-1 through SM-5 happened in chat window `a49b320e`; substantive Opus reasoning has not been recovered into per-paper `reasoning-[ID].md` files.
**Deliverable**: Per-paper `reasoning-SR-1.md`, `reasoning-EW-1.md` through `reasoning-EW-5.md`, `reasoning-SS-1.md`, `reasoning-QM-1.md` through `reasoning-QM-6.md`, `reasoning-SM-1.md` through `reasoning-SM-5.md` (16 files). Source: chat window `a49b320e` transcript at `/mnt/transcripts/` if accessible, or `conversation_search` recovery per the `templates/operating_system.md` §6 protocol.
**Estimated effort**: Multi-session — could be ~16 separate small patches (one per paper) or a single large multi-patch chain.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-004 — `reasoning-SM-9.md` (patch 0027, pine-tree model)

**Status**: PROGRAMME-LEVEL DEFERRED; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: Same logic as TODO-003 — historical hygiene for an already-shipped paper, does not gate SS-10.
**Deliverable**: `reasoning-SM-9.md` per the four-tier discipline format used for SS-9.
**Estimated effort**: 1 patch.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-005 — `reasoning-SM-10.md` (patch 0028, FEM journey)

**Status**: PROGRAMME-LEVEL DEFERRED; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: Same logic as TODO-003.
**Deliverable**: `reasoning-SM-10.md` per the four-tier discipline format.
**Estimated effort**: 1 patch.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-006 — OPEN-WORKFLOW-1 legacy `.bib` file cleanup (programme-wide bibliography migration)

**Status**: PROGRAMME-WIDE MIGRATION — scope much larger than originally registered; not a forward blocker for SS-10
**Why P2 (Session 36 demotion + scope expansion)**: The Session 36 audit found **14 stray `.bib` files** across the repo, with most still **actively cited** by ~25 `.tex` files spanning every series. This is not a quick "audit and delete" patch — it's a programme-wide migration touching SR-1, SM-6 through SM-10, EW-1 through EW-5, QM-1 through QM-6, SS-1, SD-1 through SD-5, plus the orphan-or-active `series_strong/papers/cpp_strong_series.bib` and three `series_strong/cpp_strong_series*.bib` files at the series root. SS-7 and SS-9 use inline `\begin{thebibliography}` blocks (no .bib file at all). SS-8 and SM-3 use the canonical `bibliography/cpp_references.bib`. SS-10 can adopt the canonical pattern (like SS-8 did) regardless of what other papers use, so this migration does not forward-block SS-10. **Recommendation for next session**: consider promoting this to `future_projects.md` as a multi-session OPEN-WORKFLOW-1 project, since it's no longer "1 small patch" scope.
**Issue**: Bibliography consolidation policy established `bibliography/cpp_references.bib` as single source of truth; legacy per-series and per-paper `.bib` files are deprecated (per `templates/paper_production_workflow.md` Phase 2 note: "Do NOT create a new per-paper `[ID]_references.bib` file — those are deprecated"). Cleanup audit is registered as OPEN-WORKFLOW-1.
**Stray .bib inventory (Session 36 audit)**: `series_strong/cpp_strong_series.bib`, `series_strong/cpp_strong_series_papers.bib`, `series_strong/cpp_strong_series_root.bib`, `series_strong/papers/cpp_strong_series.bib`, `series_standard_model/papers/cpp_references.bib` (note: NOT canonical path), `series_standard_model/papers/SM-{6,7,8,9,10}_references.bib`, `series_electroweak/papers/cpp_ew_series.bib`, `series_quantum_mechanics/papers/cpp_qm_series.bib`, `series_foundations/series_superdeterminism/cpp_foundations_series.bib`, `series_relativity/papers/SR-1_references.bib`. Active `.tex` consumers identified per audit.
**Deliverable**: Programme-wide migration: (1) merge unique entries from each stray `.bib` into `bibliography/cpp_references.bib`; (2) update `\bibliography{...}` line in each consuming `.tex` to point to `../../../bibliography/cpp_references` (path depth varies by series structure); (3) delete strays; (4) recompile each affected paper to verify no broken citations.
**Estimated effort**: Multi-session if done thoroughly (likely 2-3 sessions); paper-by-paper migration with recompile verification per paper.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2 with scope expansion** 7 May 2026 Session 36 close patch 0288.

### TODO-007 — SS-9 public posting (OSF deposit + arXiv submission)

**Status**: PENDING Thomas's timing decision; OSF complication identified Session 36 (see below)
**Operational protocol**: `series_strong/papers/SS-9/letters/SS-9_post_ship_OSF_arXiv_submission_guide.md` (created Session 33 patch 0268).
**Session 36 update — OSF complication identified**: Thomas's existing Open-Ended Registration `10.17605/OSF.IO/JXE8D` (the "Conscious Point Physics Paper Series" master registration created Mar 31, 2026, listing SS-1, SM-1 through SM-5, SR-1) has been stuck in **"Pending Admin Contributor Approval"** state for 5+ weeks despite the documented 48-hour auto-approval window. Thomas is the only admin contributor listed. Multiple support tickets sent; one received an unhelpful response (about a different registration); subsequent tickets unanswered including a Claude-drafted escalation. The DOI is real and the priority date (Mar 31, 2026) is locked, but the registration is technically not finalized. **Decision Session 36**: Thomas will submit one more diagnostic-specific support ticket framing the issue precisely as "Pending Admin Contributor Approval state stuck >38 days, only one admin contributor, auto-approval timer never fired." Wait 5 business days for OSF response. **If OSF resolves** → add SS-9 as an Update to the existing JXE8D registration (the registration is Open-Ended, designed to be added to over time), and post to arXiv in parallel (categories nucl-th + math-ph). **If OSF still silent after 5 business days** → fallback to depositing SS-9 on **Zenodo** (CERN-run, gives DOI, no comparable workflow issues) plus arXiv, treating OSF as a later catch-up.
**Two original options remain open** (both consistent with rescoped sub-task (e)):
- **Option A**: post now to lock priority date and start external-feedback clock.
- **Option B**: wait until anthology chapter (Session 34) and TATWD integration (Session 35) are complete to present a fuller programme picture at posting time.
Both are now fully available since Sessions 34 and 35 are complete; only the OSF technical issue remains as a delay factor.
**Note**: TODO-001 (SS-9 Phase 7 Section A) trigger depends on this resolving — public posting is the precondition for the external-feedback window.
**Registered**: 7 May 2026 Session 33 close; **OSF complication and fallback plan added** 7 May 2026 Session 36 close patch 0288.

### TODO-008 — OPEN-WORKFLOW-DOCS-CATCHUP (programme-wide documentation-suite discipline-tightening per discipline-tightening-after-precedent principle)

**Status**: REGISTERED — two-part item: (A) flagship documentation-suite backlog catch-up for SF-4 v1.0 and SF-2 v1.0; (B) programme-wide gate-language codification of synchronous-documentation-suite requirement for v1.0 SHIP going forward
**Why P2 (not P1)**: This is hygiene/discipline-tightening work — it does not gate any specific next paper. The flagship papers themselves are already shipped; their documentation-suite backlog is a programme-record-completeness item. The gate-language codification is forward-looking discipline that will apply to future flagships from the next v1.0 SHIP onward. Neither sub-item blocks SS-10 or any other in-flight work.

**Precedent (Capotauro v1.0 SHIP arc)**: Capotauro v1.0 SHIPPED at Patch 0415 Session 122 with **the first complete documentation suite shipped synchronously with a CPP flagship v1.0 SHIP**. The Session 123 doc-suite catch-up arc (Patches 0416–0416L) produced ten documentation files: Section E four-tier discipline (handover ✓ 0416 + development ✓ 0416B + transcript ✓ 0416C + reasoning ✓ 0416D) + Section A six standalone companions (mechanism ✓ 0416E + glossary ✓ 0416F + phenomena ✓ 0416G + philosophy ✓ 0416H + reviews ✓ 0416I + keywords ✓ 0416J) + anthology chapter (✓ 0416K) + TATWD integration (✓ 0416L). This is the reference implementation for the synchronous-documentation-suite discipline. Per the **discipline-tightening-after-precedent principle** (recognized at Session 123 Patch 0416D as a programme-level convention; same pattern as Sessions 115–116 per-paper changelog file convention codification at Patch 0408 reference implementation → Patch 0409 programme-wide codification), the precedent makes credible the codification of synchronous-doc-suite requirement as a programme-wide v1.0 SHIP gate.

**Sub-item (A): Flagship documentation-suite backlog catch-up**

The two flagships that shipped v1.0 before Capotauro (SF-4 v1.0 at 14 May 2026; SF-2 v1.0 at 14 May 2026 jointly with its Companion paper) shipped without Section A standalone companions. Backlog inventory:

- **SF-4 v1.0 documentation-suite backlog: 0/7 standalone companions**
  - Existing: `flagship_papers/neutrinos/documentation_suite/` has development-SF-4.md + handover-SF-4.md + reasoning-SF-4.md + transcript-SF-4.md (Section E four-tier discipline only)
  - Missing: mechanism-SF-4.md (A1) + glossary-SF-4.md (A2) + phenomena-SF-4.md (A3) + philosophy-SF-4.md (A4) + development-SF-4.md final consolidation pass (A5; current file is session-continuity, not the consolidated paper-development file) + reviews-SF-4.md (A6) + keywords-SF-4.md (A7)
  - Estimated effort: 1 dedicated session (~3-5 hours) following the Capotauro template
  - **Trigger**: After SF-4 v4.4 public posting (currently pending Thomas's timing decision per TODO-007-analog for SF-4) AND external-feedback window settles, per Two-Triggers discipline. Same trigger logic as TODO-001 for SS-9.

- **SF-2 v1.0 documentation-suite backlog: 0/7 standalone companions**
  - Existing: `flagship_papers/electroweak/documentation_suite/` has development-SF-2.md + handover-SF-2.md + reasoning-SF-2.md + transcript-SF-2.md (Section E four-tier discipline only); Companion paper documentation status to be audited
  - Missing: mechanism-SF-2.md (A1) + glossary-SF-2.md (A2) + phenomena-SF-2.md (A3) + philosophy-SF-2.md (A4) + development-SF-2.md final consolidation pass (A5) + reviews-SF-2.md (A6) + keywords-SF-2.md (A7)
  - Estimated effort: 1 dedicated session (~3-5 hours) following the Capotauro template; possibly 2 sessions if Companion paper warrants parallel suite
  - **Trigger**: Same Two-Triggers logic as SF-4 — after SF-2 v1.0 public posting + external-feedback window settles.

- **SS-9 v1.0 documentation-suite backlog**: Already tracked at TODO-001 (registered 7 May 2026 Session 33; demoted to P2 Session 36 Patch 0288). The SS-9 trigger logic is the canonical reference for the Two-Triggers discipline. TODO-008 does NOT re-register the SS-9 item; it cross-references TODO-001 as the SS-9 instance of the broader pattern.

**Sub-item (B): Programme-wide gate-language codification**

The Capotauro precedent makes credible a tightening of the v1.0 SHIP gate-language to require synchronous documentation-suite completion. The codification work is a separate downstream item, not bundled with the backlog catch-up:

- **`templates/operating_system.md` §4 Phase 7 (post-SHIP doc-suite work)** — modify gate-language to specify: "A flagship paper does not reach v1.0 SHIPPED status until its Section A 6 standalone companions + Section E 4 four-tier discipline files are complete in `flagship_papers/<paper>/documentation_suite/`. Synchronous completion is the default; the Two-Triggers discipline (`templates/paper_completion_checklist.md` lines 35–48) applies only as an explicit exception for cases where external-feedback gating is more important than synchronous completion (e.g., a paper that may revise substantially after first external review)."
- **`templates/paper_completion_checklist.md` Section A** — modify the Two-Triggers discipline language to clarify that synchronous completion is the new default (per Capotauro precedent), with the Two-Triggers as documented exception path rather than default workflow. The Two-Triggers default should remain available for papers like SS-9 where the v1.0 paper itself is the primary deliverable and the documentation suite can wait for external-feedback shape.
- **Cross-reference**: `book_project/chapters/capotauro_what_was_always_there.md` §"The Method Underneath" + `programme_orientation.md` Chapter 35.5 § Methodological observation as the master-document references for the precedent.
- Estimated effort: 1 patch (~30 minutes) — small editorial codification patches against the two template files. Should be done after Sub-item (A) is at least partially in hand (per discipline-tightening-after-precedent principle: the codification is credible because multiple instances of the discipline now exist).

**Estimated effort total**: 2-3 sessions for Sub-item (A) (SF-4 + SF-2 backlog completion, possibly serialized); 1 small patch for Sub-item (B) (codification).
**Registered**: 16 May 2026 Session 123 close Patch 0416M as the **final patch in the Capotauro doc-suite catch-up arc** (Patches 0416 + 0416A through 0416L preceding this patch). Forward queue: items fire on Two-Triggers external-feedback signal for each affected paper; codification patch can fire any time after Sub-item (A) is partially in hand.

---

### TODO-010 — Second-level decomposition of `frontier_sectors/SS.md` (contingent on SS-sector bootup overflow)

**Status**: CONTINGENT — fires only if loading `frontier_sectors/SS.md` (208 KB, ~700 lines) at session bootup overflows the context window. Not currently known to do so.
**Why P2**: Speculative future hygiene. The 25 May 2026 frontier decomposition reduced master `research_frontier.md` from 1852 to 280 lines, solving the bootup overflow. Sector files are loaded on demand, not at bootup, so SS.md's size is only a concern if a session needs to load the full SS sector. If that triggers overflow in future SS-focused sessions, sub-decomposition becomes necessary.
**Trigger**: First session that overflows on `frontier_sectors/SS.md` load.
**Deliverable**: Split `frontier_sectors/SS.md` into sub-topic files following the same pattern as the master decomposition (extraction script + thin index rewrite). Candidate sub-decomposition:
- `frontier_sectors/SS_cage_mechanics.md` — SS-1 through SS-6 (quark mass, generations, condensate, β1, string tension, glueball)
- `frontier_sectors/SS_nuclear_binding.md` — SS-7, SS-8, SS-10 through SS-21 (binding curves, nucleon moments, ZBW mechanisms, deuteron)
- `frontier_sectors/SS_magic_numbers.md` — SS-22 through SS-37 (alpha-cluster regime, OPEN-SS-35 magic-number gap programme, deltahedra-gap closures)
- `frontier_sectors/SS_propositions.md` — SS-specific PROPs/CONJs from SS-5, SS-6, SS-7
**Estimated effort**: 1 dedicated session (~2 hours). Same pattern as 25 May 2026 master decomposition.
**Registered**: 25 May 2026 (frontier decomposition close, flagged from SS.md size observation: 208 KB, dwarfs all other sectors).

### TODO-011 — Structural-heterogeneity normalization pass across all sector files

**Status**: hygiene improvement; not blocking next paper
**Why P2**: `research_frontier.md` accumulated heterogeneity over months of organic growth — some OPEN-XX entries are richly sub-structured with `### Status`, `### Mechanism Required`, `### Route History`, etc.; others are flat single-paragraph prose. This was preserved verbatim in the 25 May 2026 decomposition to keep the extraction deterministic and reviewable. Normalizing every entry to a uniform sub-header skeleton would make sector files easier to grep, easier for AI collaborators to parse uniformly, and easier for new sessions to bootup-into-problem.
**Deliverable**: Standardize every OPEN-XX entry across all 9 sector files in `frontier_sectors/` to use a uniform sub-header skeleton:
- `### Status` — one-line current state
- `### Mechanism Required` — what closure looks like
- `### Acceptance Criteria` — F1/F2/F3 falsifiers or equivalent
- `### Route History` — what has been tried; ruled-out routes preserved
- `### Cross-References` — related OPEN-XX entries, papers, conjectures, propositions

Empty sections marked `(none yet)` to keep the skeleton uniform across heavily-developed and stubbed entries alike.
**Estimated effort**: ~9 patches (one per sector), deliverable as a sequential arc. Could also be done piecemeal as sessions touch specific sectors for unrelated reasons (lazy normalization).
**Registered**: 25 May 2026 (frontier decomposition close, noted from sector-file spot-check when Thomas observed format heterogeneity in extracted files).

### TODO-013 — Annotate BRIDGE-1 falsifier B4 as resolved-as-documentation (DG-3, carried from Session 151)

**Status**: small hygiene note; not blocking; **do NOT edit the review-closed theorem solely for this** — carry until the next substantive BRIDGE-1 maintenance bump.
**Why P2**: `series_umbrella/series_substrate_chirality_arc/chirality_derivations/theo_chir_bridge_1.tex` (THEO-CHIR-BRIDGE-1) is multi-AI review-closed 3/3 at v1.1 (Patch 0665). Opening it solely to annotate one falsifier is disproportionate and risks re-triggering review; the correct discipline (Session 151 handover DG-3) is to fold the annotation into the *next* version bump that touches the theorem for a substantive reason.
**Issue**: Falsifier **B4** currently reads "the χ normalization is irreconcilable (φ⁻¹ vs φ⁻³)" (`theo_chir_bridge_1.tex` falsifier ledger). That worry was **resolved as a non-tension at Patches 0669 + 0670**: φ⁻³ is the unambiguous live magnitude (FI-C-9 = CHI-1 = Capotauro v1.0/v2.0); φ⁻¹ is both a registered dead-end (Findings C-1/C-2/C-3, Session 86) and the first-shell *distance* from which CHI-1 builds χ = (1−φ⁻¹)/(1+φ⁻¹) = φ⁻³. So B4 as written overstates a live risk.
**Deliverable**: at the next BRIDGE-1 maintenance bump, annotate B4 as "**resolved-as-documentation** (χ φ⁻¹-vs-φ⁻³ reconciled as a non-tension, Patches 0669/0670); **retained only as a forward hook on sub-claim (b)** — re-fires only if a future first-principles |χ| derivation returns φ⁻¹ or φ⁻² as the *magnitude*." No standalone edit, no version bump for this alone.
**Estimated effort**: trivial (one falsifier-line annotation, folded into a future bump).
**Registered**: 30 May 2026 Session 152 Patch 0674 (carried from the Session 151 handover Priority 2 / DG-3; reclassification first noted at Patch 0669).

---

### SR companion-paper set (c01–c22) audit & registry reconciliation
**Added:** 31 May 2026, Session 149, Patch 0672b. **Priority:** P2 (do NOT block the tetra-gravity DM arc — DM publication is the stated higher priority).

The `SR_companion_papers` set (c01–c22) was restored from Archive to `series_relativity/SR_companion_papers/` (origin commit f70bc05, 31 May 2026); it had been archived, probably by accident, and was not visible in the working repo. These are Sonnet-era papers that predate parts of the current OPEN-/THEO-/CONJ- registry and protocol system. Audit + reconcile when convenient:
- **Duplication** — check companion content against current SR-1 / SS / SD / EW / QM papers for overlap or supersession.
- **Stale open problems** — `frontier_sectors/SR.md` still lists OPEN-SR-4 (full field equations) and OPEN-SR-8 (equivalence principle) as OPEN with a "weak-field GR derived; full nonlinear not yet proved" best-lead note, but c05 derives Newtonian gravity (G = ℏc/m_P² exact), c07 derives weak-field GR + equivalence principle + factor-of-2 lensing, and c08 addresses strong-field GR. Reconcile SR.md ↔ companions; retire/downgrade OPEN-SR-8 and re-scope OPEN-SR-4 as warranted.
- **Registry retrofit** — register companion results into `theorem-registry.md` / frontier where they meet the bar (e.g. c05 G = ℏc/m_P², c07 weak-field Schwarzschild + lensing factor-of-2).
- **Spin-paper correction** — c20/c21/c22 may carry the pre-correction "2:1 frequency"; reconcile against THEO-SPIN-1 (v1.1) corrected this session (radius 2 / frequency 2√2).
- **DM-arc tie (added Patch 0702, 31 May 2026):** the tetra-gravity DM arc's Step-0 audit re-confirmed the SR.md staleness — `frontier_sectors/SR.md` (all entries dated 23 March, everything OPEN) does not reflect c05/c07/c08. This bullet (the "Stale open problems" item above) is the home for that reconciliation; no separate TODO was minted to avoid duplication. Step 0 of OPEN-COSMO-DM-1 only *cites* c05/c07 and does not block on this hygiene pass.
- **Effort:** multi-patch; sequence after the DM arc's Gate-1 (σ/m) and Gate-2 (bookkeeping) calculations are in hand.


### TODO-014 — c05 "G = ℏc/m_P², zero free parameters" framing: resolve the Planck-scale circularity before Step 0 leans on it
**Added:** 31 May 2026, Session 149, Patch 0702. **Priority:** P2 (does NOT block the DM arc — framing issue, not a physics blocker).

**Issue.** c05 (`c05_gravity_from_SSV_shell_broadcast.tex` §"The Gravitational SSV Quantum and Newton's G") boxes `G = ℏc/m_P²` and calls it "exact ... no free parameters," verifying numerically by plugging in CODATA `m_P = 2.176×10⁻⁸ kg`. As written this is circular: the Planck mass is *defined* by `m_P ≡ √(ℏc/G)`, so `G = ℏc/m_P²` is an algebraic identity, and the CODATA `m_P` used in the "verification" was itself computed from the measured `G`. It is a genuine zero-parameter *prediction of G* only if the Planck scale (`m_P` / `l_P` / `t_P`) is independently fixed by the 600-cell **without reference to G**.

**What c02 actually establishes (checked Patch 0700).** c02 (`c02_dipole_stiffness_C.tex`) derives a genuinely *dimensionless* geometric constant `α_geom = 3(11+5√5)√(5+√5)/320 ≈ 0.5594` (the Voronoi second-moment efficiency). But every dimensionful quantity is carried by `E_P`, `l_P` taken as given (`SSV_crit ≡ E_P/l_P³` asserted as the Planck energy density). So the lattice fixes dimensionless ratios; the absolute scale is **not** derived there.

**Dimensional-analysis reality (do not promise the impossible).** A dimensionful constant cannot be derived from pure geometry — at least one dimensionful input (the lattice spacing ≡ `l_P`) must set the scale. "Derive G from first principles" therefore cannot literally succeed; pursuing it as stated would be chasing a category error. The honest, defensible target is a **restatement + a verification**, not a derivation of a dimensionful number from numbers.

**Deliverable.**
1. **Verify the calibration is singular and shared** — confirm the whole CPP corpus fixes its absolute scale by exactly *one* dimensionful input (the lattice spacing / `l_P`), used consistently everywhere, with no second hidden scale-setting calibration. (If a second independent dimensionful calibration exists, the "zero free parameters" claims across the corpus need re-auditing, not just c05's.)
2. **Restate c05's claim precisely** — replace "G derived, zero free parameters" with "all *dimensionless* structure (incl. `α_geom`) is fixed by the 600-cell; the single dimensionful scale `l_P` is the one shared calibration; `G = ℏc/m_P²` then follows with **no additional** parameter." This is still a strong result; it is just not "G from nothing."
3. **Trace the upstream chain** — document where `l_P`/`E_P`/`t_P` enter (c02 and any earlier paper) and whether anything purports to fix them independently; if such a derivation is claimed, scrutinize it for a concealed dimensionful input.
4. **Step-0 wording lock** — until (1)–(3) are done, OPEN-COSMO-DM-1 Step 0 cites c05 as "**Newtonian force law recovered**" (the DM arc only needs the Newtonian *form* with a G matching observation, which c05 supplies regardless), NOT "G derived from scratch."

**Estimated effort:** 1–2 patches (an audit + a c05/c02 CHANGELOG framing bump); no new physics required for the restatement, though step (3) may surface a real open question worth its own registry entry.
**Registered:** 31 May 2026 Session 149 Patch 0702 (surfaced during the DM-arc Step-0 GR-foundation check).

### TODO-015 — c08 Open Problem 1 (full nonlinear strong-field Einstein equivalence): standing deep target, NOT blocking DM-2
**Added:** 8 June 2026, Session 156, Patch 0808. **Priority:** P2 (does NOT block the DM-2 / Sea-gravitation arc — see resolution below).

**The problem.** c08 (`c08_strong-field_GR.tex`, Open Problem 1) leaves open whether the full nonlinear feedback term 𝓕 in the CPP field equation reproduces the exact Einstein tensor `G_μν` in the **strong-field** regime — i.e. whether `box(Δ|SSV|) + 𝓕 = G_μν u^μ u^ν` for all spacetimes, or a counterexample exists. c08's weak-field reduction to linearised GR and the exact Schwarzschild solution are proved; the full nonlinear equivalence is the stated central unsolved problem of that paper. This is a genuinely deep target (effectively: derive GR's full nonlinear structure from the substrate).

**Why it is NOT on the DM-2 critical path (resolved, Patches 0805–0806).** The DM-2 Step-1 audit initially tied D2 (ground-state exclusion) to this problem. Step 1 (0805) showed the coupling is separable, and Step 2(a) (0806) closed it: gravitation is **gradient-controlled, not amplitude-controlled** — 𝓕 = [bounded amplitude factor] × [gradient² factor], so the uniform Sea's O(1) absolute SSV sources ~0 (small gradient) and never exercises the strong-**amplitude** nonlinearity OP1 is about. The only large-gradient sources are sub-Planck localized excesses, weak-field by `(m/m_P)² ~ 10⁻³⁹`. So DM-2 proceeds in full **without** OP1; it does not wait on this item. See `series_phenomena/cosmology/sea_gravitation/dm2_step2a_zbw_bound.md`.

**Status / scheduling.** Standing deep target ("in its time"). Belongs to the SR companion-paper set (c01–c22) and is adjacent to the c08 Kerr and discrete-to-continuum open problems. Candidate for promotion to `future_projects.md` if/when pursued as its own arc. Not to be confused with DM-2's net-broadcast lemma (a separate, local, weak-field question).

**Registered:** 8 June 2026 Session 156 Patch 0808 (surfaced and then de-risked during the DM-2 Step-0/1/2a audit).


### TODO-016 — DP-Sea appendix: the DP binding-energy formula is numerically inconsistent with its stated r_min by ~18 orders of magnitude
**Added:** 10 June 2026, Session 156, Patch 0834. **Priority:** P2 (does NOT block DM-2; the *ratio* the DM arc uses is unaffected).

**The problem.** In `series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex` (Appendix, "DP Binding Energy Calculation"), the formula `E_bind = αℏc/r_min` is quoted with `r_min = φ·l_p ≈ 2.61×10⁻³⁵ m` (the golden-ratio-scaled **Planck** length) and is said to yield `E_eDP = αℏc/(φl_p) ≈ 88 MeV`, `E_qDP = 3·E_eDP ≈ 264 MeV`. But `αℏc/(2.61×10⁻³⁵ m) ≈ 5.5×10¹⁹ MeV`, not 88 MeV — the stated r_min and the quoted energies are inconsistent by ~6×10¹⁷. The quoted 88 MeV instead requires `r_min ≈ 0.016 fm = 1.6×10⁻¹⁷ m`, eighteen orders of magnitude larger than the Planck length. So as written the **absolute** eDP/qDP energy scale does not follow from the Planck length; it is calibrated to the constituent/QCD scale and the appendix mislabels its own r_min.

**What is and isn't affected.** The **ratio** `E_qDP/E_eDP = 3` (color factor) is clean and is the only thing the DM-2 Era-2 arc leans on (it gives m_qDP ≈ 3×88 = 264 MeV, used in patches 0830–0833). So this does **not** block DM-2. But the eDP = 88 MeV scale propagates into the whole DP spectrum (hDP = √(E_eDP·E_qDP) ≈ 152 MeV, the cage binding energies, the boson-mass averaging), so the inconsistency should be reconciled at the source.

**The fix (a physics decision, hence Thomas's, not a unilateral flagship edit).** Decide what actually sets r_min ≈ 0.016 fm: (a) is it a genuine CPP length (e.g. the CP grid/lattice spacing, or a derived sub-quantum scale) that should replace "φ·l_p" in the formula and text; or (b) is the 88 MeV scale calibrated to the constituent/QCD scale, in which case the appendix should say so rather than presenting it as Planck-derived? Either way the appendix line and the "2.61×10⁻³⁵ m" value need correcting so the paper is internally consistent.

**Surfaced:** 10 June 2026 Session 156 Patch 0833 (DM-2 Era-2 required-inputs derivation pass, deriving m_qDP). Flagged to Thomas; left for his edit/publish workflow on the flagship.

**Update (Patch 0838 — decision recorded):** Thomas chose **Option C** (Planck → DP/QCD scale via derived suppression). Decisive finding: **C is already SS-1 open problem `op:lambda_psr`** ("Λ_QCD from PSR saturation": derive Λ_QCD ≈ 0.218 GeV from l_P + sea_strength via PSR_eff → l_P/2) plus `op:sigma` (string tension from sea_strength) — SS-1 honestly marks this scale *calibrated* with the Planck derivation *open*, while the DP-Sea appendix wrongly asserts it *done*. Resolution is two-track (see handover): **(1)** correct the appendix now to match SS-1's honest stance + cite `op:lambda_psr` (energies 88/264/152 + ratios retained; drop the false `αℏc/(φl_p)` derivation and the 2.61×10⁻³⁵ m identification); **(2)** pursue C proper = solving SS-1 `op:lambda_psr` (promote to `future_projects.md`), which on success upgrades both flagships from calibrated to derived. Handover updated. **Status: Track 1 awaits a draft+sign-off pass; Track 2 to be promoted to future_projects.md. No flagship edit made yet.**


### TODO-017 — Corpus-wide harmonization review (after the SU(3)/beta-decay/chirality exploratory arc settles)

When the Session-16x exploratory arc (SU(3) mechanism → beta decay → chirality) reaches a sense of completion, run a cross-corpus harmonization sweep: check all papers for internal consistency and number-agreement across the EW, SS, SF sectors and the substrate-chirality arc. Prompted by finding TODO-018 (a genuine error sitting in two shipped EW papers) — if one number-error survived into print, others may have. Scope: an internal-consistency + cross-reference pass, not new derivation. **Registered 18 June 2026.**

### TODO-018 — EW-2 / EW-5 chirality-fraction formula error (genuine bug in two shipped papers) — recommend elevating

Both `series_electroweak/papers/EW-2_w_boson_from_cpp.tex` and `series_electroweak/papers/EW-5_electroweak_unification.tex` carry the line `P_L^eff = 1 − sin²(60°) = 0.25 ⟹ 75% left-handed`, claimed as "matching the V−A structure of weak charged currents." Two faults: **(a) internally inconsistent** — `1 − sin²(60°) = 0.25`, i.e. 25%, but the line concludes 75%; it computes one value and prints another. **(b) physically short** — the weak charged current is ~maximally parity-violating (~100% left-handed; Wu 1957 + Goldhaber 1958), not a 25/75 partial preference, so "75% matching V−A" is wrong regardless of which number is meant. Action: decide the correct intended quantity, fix the formula in both papers, and **check propagation to SF-2** (the electroweak flagship likely inherits it). This is a real error in shipped work, not a hygiene gap — recommend P1. **Registered 18 June 2026.**

### TODO-019 — Mechanism note: the billiard-ball realization of the SU(3) hop (closes `op:strong_primitive` on the mechanism side, if it holds)

Memorialize the Session-16x exploratory result. SS-1b derives the SU(3) *algebra* from three tetrahedral color vertices and explicitly leaves `op:strong_primitive` open — *why* the strong force is tetrahedral hopping. The week's work built the candidate *mechanism* underneath the algebra: color = which base vertex a quark occupies; the eight gluons = the six edge hops + two diagonals among three vertices; each hop physically *carried* by a ZBW / SSV-gradient transition (the trembling is the muscle that performs the hop). Status to register honestly: **picture, not yet derivation** — the mechanism is rich enough to be a candidate carrier but was not shown to *force* the algebra from substrate geometry alone. Write as a standalone mechanism note, separate from the algebra papers (SS-1b / SF-5), and register the open residual. **Registered 18 June 2026.**

### TODO-020 — Chirality visualization writeup → Chirality window (900-series patches)

Write up the new chirality visualization and hand it to the 900-series Chirality window to test whether it helps close the substrate-chirality arc. The picture: a moving charge polarizes the surrounding DP Sea; each dipole's poles swing (opposite pole drawn toward the passing charge, like pole pushed away), turning the dipole about its center; the *sense* of that rotation relative to the charge's line of motion is the right-hand rule. So the magnetic field is the *name for the DP-Sea's rotational response to a moving charge*, not a primitive field — and handedness is *generated* by charge-through-dipoles, with sign set by the charge's polarity. Consequence to flag for the 900 window: this removes the need for a primordial/inflationary chirality imprint — the world's handedness is manufactured fresh by every moving charge. Send as a story/note (Thomas's preferred form) and see whether it advances the substrate-chirality determination. **DONE (18 Jun 2026):** the writeup is committed at `founders_voice/phenomenon_magnetism_and_chirality.md` (edited from TLA's v2; Goldhaber + type-B fixes). It carries both a "For the chirality window (900-series)" section and a "For SF-6 (electromagnetism flagship)" section. **SF-6 and the 900 window should both read it there.** A paste-ready handoff instruction for the chirality window was generated 18 Jun 2026. **Registered 18 June 2026.**

### TODO-021 — Harmonise SS-1b's per-quark-cage exposition with the cageless-quark / bonding-framework realisation

Surfaced while shipping SS-1f v1.0. SS-1b's exposition states "each quark sits inside a tetrahedral cage (four vertices: apex V4 for the qCP, base {V1,V2,V3} for color)" — a **per-quark cage** picture. TLA's clarification (and SS-1f's resolved frame) is that the hTetra is the baryon-level **bonding framework**, that **up and down quarks are cageless** (qCP core + radial ZBW eCP + cloud), and that only the **strange quark carries its own hTetra cage**. SS-1b's *algebra* is frame-agnostic (three labelled colour vertices + hops) and is unaffected; only its *physical-picture wording* is in tension. Two sub-tasks: (i) reconcile SS-1b's expository cage language with the cageless-quark realisation (edit SS-1b's prose, not its theorem); (ii) work out the detailed correspondence between SS-1b's (apex-qCP + three-colour-base) cage and the baryon hTetra's (three-quark + open-eCP-vertex) geometry. Folds into the TODO-017 corpus-harmonisation sweep but is specific and known. **Registered 18 June 2026.**

### TODO-022 — Phenomenon-story programme: a `founders_voice/phenomenon_*.md` behind every paper and glossary item

TLA's standing intent, now structurally established. `founders_voice/` hosts the fully-articulated, expanded, examined version of each paper's Plain Language Summary — the founder's mechanical billiard-ball story behind the mathematics ("this IS my story; the mathematics is what makes it credible"). Convention documented in `founders_voice/founders_voice-README.md` (six-part shape; honest-status discipline; newer conjectures flagged). Rollout: write one phenomenon story per paper (seeded from its PLS) and per major glossary item, on a rolling basis. Started 18 Jun 2026 with `phenomenon_magnetism_and_chirality.md` and `phenomenon_su3_colour_and_quark_switching.md`. Each story must name, in Honest-status, the proven mathematics that grounds it and the derivation still owed. **Registered 18 June 2026.**

### TODO-023 — Sitewide README normalization to the `{scope}-README.md` convention

The OS convention (`operating_system.md` §"README files — `{scope}-README.md` convention") mandates `{scope}-README.md` (scope prefix, hyphen, uppercase README) and notes a "retroactive normalization" cleanup is owed. Audit (18 Jun 2026): **83 non-compliant** README files — 70 plain `README.md`, 2 `{scope}_README.md` (underscore), 11 `README-{scope}.md` (leading-README) — plus 7 already compliant. `founders_voice/README.md` was fixed in passing (→ `founders_voice-README.md`). **The full batch is deferred to a dedicated, low-collision cleanup patch**, NOT folded into window work: it renames files across folders owned by every active window (series_relativity, flagship_papers/\*, series_standard_model, etc.), so it should run when windows are quiesced, as a single `git mv` sweep with a reference-update grep pass (links to `README.md` → `{scope}-README.md`). Content-neutral; the OS marks it non-forcing. Generate the batch script + ref-sweep on request. **Registered 18 June 2026.**

### TODO-024 — SS-1f v1.0 remaining Phase-7B integration items (anti-silent-dropout register)

SS-1f v1.0 production protocol initiated 18 Jun 2026 (patch 1534): the precedent-consistent core is DONE — series_strong sub-family table row (D3, the canonical home where SS-1a–1e live) + bibliography entry (C11, DOI pending Isak's OSF post). The following Phase-7B items are **deferred, not dropped** (per `paper_completion_checklist.md` "Phase 7B silent dropout" anti-pattern), pending a decision call on each because the SS-1x companion-note precedent is that SS-1a–1e are NOT individually carried in these registries:
- **C3 theorem-registry.md** — register SS-1f's Proposition 6.1 (the torus result) as a PROP-SS-* entry? Sub-family precedent = no individual registration (1b–1e absent); registering requires careful SS-header + Summary-Statistics count bumps. **Needs TLA call.**
- **C5 frontier_sectors/SS.md** — op:strong_primitive has no standalone entry in SS.md (the file is dominated by the SS-9 alpha-cluster arc); placing the "frame resolved / forcing open" status needs a deliberate new entry. **Deferred.**
- **D2 INDEX.md** — add SS-1f's files (.tex + reasoning + review artifacts). Low-risk navigation; **deferred.**
- **C10 programme_orientation.md / paper_catalog.md top-level / D1 README.md** — SS-1f is a sub-family mechanism note, not a top-level paper; 1a–1e set the precedent of light/no top-level presence. **Likely N/A; confirm.**
OSF deposit: Isak notified (18 Jun 2026); update C11 `doi` field once the DOI returns. **Registered 18 June 2026.**

### TODO-024 — SS-1f v1.0 remaining Phase-7B integration items — **DONE (18 Jun 2026, patch 1535)**

SS-1f v1.0 production protocol completed. Core (combined patch 1533+1534): series_strong sub-family table row (D3) + bibliography entry (C11, DOI pending Isak's OSF post). Remaining Phase-7B items now also done (patch 1535): **C3** — Proposition 6.1 registered as **PROP-SS-12** in theorem-registry (SS header 1→2 Propositions; no theorem-count / Summary-Statistics / ratio change, since propositions are tracked separately from the 81-theorem total); **C5** — **OPEN-SS-38** added to frontier_sectors/SS.md (the op:strong_primitive forcing problem; frame resolved by SS-1f, forcing open; SS header 19→20 problems); **D2** — SS-1f .tex added to INDEX.md. C10/D1/paper_catalog top-level confirmed N/A (sub-family companion note, per the SS-1a–1e precedent). Outstanding: only the OSF DOI (Isak) → update the C11 `doi` field on return. **Completed 18 June 2026.**

### TODO-025 — `frontier_sectors/CONJ.md` OPEN-COSMO-DM-2 / DM-2 R2 wording is stale (pre-2025 R2 arc) — **CLEARED 22 Jun 2026, Patch 2046**

**Status**: CLEARED (Patch 2046) — DM/cosmo lane was idle, so the two pointer brackets were added directly:
one to the OPEN-COSMO-DM-2 entry and one to CONJ-COSMO-1, both pointing R2's current state at
`mu_eps_closure/R2-STATUS.md` (conditional-PASS at field-content level; unconditional gated on OPEN-SR-9).
The stale "single-oscillator / Patch 2002" lines are left in place (historical record) with the pointer
overriding. *(Original deferral note retained below for audit.)* **Why it had been deferred (Patch 2041)**:
CONJ.md is the hottest cross-lane Tier-A file; the gap was cosmetic/non-verdict, so it waited for a quiet lane.
**What's stale**: the OPEN-COSMO-DM-2 entry (line ~251) and the CONJ-COSMO-1 entry (line ~314) describe R2's
status from before the 2025–2031 μ↔ε arc — e.g. "R2 PASS-conditional on the single-oscillator structure —
Patch 2002." The current state (R2-STATUS.md → Update 2041) is: **R2 conditional-PASS, both conditions met
within the audited LSP field content — (i) VTD-1 cleared at SR-1 strength (2037/2038 + panel P1-SOUND ×4);
(ii) f(C,Σ) closed at the field-content level (2028 scalar channel / 2029 ~11-order locality / 2030-2031
no-rank-2, ChatGPT CONFIRM) + A3′ OB-3 static-null theorem — with the from-substrate optical computation owed
to OPEN-SR-9.**
**The fix (small)**: a single Patch-NNNN bracket pointer appended to the OPEN-COSMO-DM-2 status line (and one
to CONJ-COSMO-1) reading "R2 current state: see R2-STATUS.md Update-2041 — conditional-PASS at field-content
level, unconditional gated on OPEN-SR-9." Do as its own minimal, refreshed edit (CONV-002) when the DM/cosmo
lane is otherwise idle. Precedent: CONJ.md line 233 already records the "R2 file stale framing owed an update
in the DM lane; not edited from another window — pointer only."

## Cleared items (history)

*Items move here with date and patch number when completed. Cleared items are not deleted — they form an audit trail of what was done and when.*

### TODO-009 — Lowercase `SOURCE=` in frontier decomposition scripts — CLEARED 1 June 2026 Session 153 Patch 0728

**Cleared**: 1 June 2026 Session 153 Patch 0728. Lowercased all `Research_Frontier` → `research_frontier` occurrences in `scripts/rewrite_research_frontier.sh` (SOURCE=, BACKUP=, and the printed `git add/diff/Open` instructions) and `scripts/decompose_research_frontier.sh` (SOURCE= + descriptive comments/echoes), giving full cross-platform correctness rather than just the two literal SOURCE= lines. Post-edit grep confirms 0 remaining capitalized refs in either script. Surfaced when Thomas asked whether a rename explained the stale `research_frontier.md` dashboard (Session 153, Patch 0727 Step E); investigation confirmed git tracks one lowercase file with no case-collision, the scripts worked on Windows because the filesystem is case-insensitive (so the rename was NOT the staleness cause — that was the 25-May decomposition shifting updates to sector files + skipped Step-E passes), but the latent portability bug was real and is now closed. **Scope note**: descriptive references to `Research_Frontier.md` elsewhere (frontier_sectors/*.md breadcrumbs, archive scripts) are harmless historical mentions, not functional, and left unchanged per TODO-009's two-script scope.

### TODO-012 — PCD acronym terminology drift cleanup — CLEARED 29 May 2026 Session 148 Patch 0631

**Cleared**: 29 May 2026 Session 148 Patch 0631 via systematic find-and-replace across 15 active files restoring the canonical "Perceive-Compute-Displace" expansion of the PCD acronym. Total occurrences corrected: 46 across 15 files; 0 drift-pattern remaining (verified by post-replace grep audit covering hyphenated form, lowercase form, en-dash form, UTF-8 arrow form, LaTeX `$\to$` arrow form, and "Polarize/Capture/Depolarize phase" PCD-phase-label patterns).

**Resolution narrative**: The Session-146 drift introduced "Polarize-Capture-Depolarize" at commit `311bc1e` in `master_glossary.md` PCD entry without rationalization; the drift propagated to ~15 active files via subsequent work that referenced the master glossary. Patch 0631 applied 5 precise sed patterns: (1) `Polarize-Capture-Depolarize` → `Perceive-Compute-Displace`; (2) lowercase variant; (3) UTF-8 arrow form `Polarize → Capture → Depolarize`; (4) LaTeX-arrow form `Polarize $\to$ Capture $\to$ Depolarize`; (5) en-dash form `Polarize–Capture–Depolarize`. Plus PCD-phase-label substitutions: `Polarize phase` → `Perceive phase`; `Capture phase` → `Compute phase`; `Depolarize phase` → `Displace phase`. Master glossary PCD entry enhanced with descriptive prose explaining the agentic cycle and its distinction from ZBW. Two prose descriptions aligned with canonical Perceive/Compute/Displace meanings (sf-2_companion glossary entry; dynamical_substrate_law §7.3 phase description). Physical-effect verbs ("polarizes the host's internal state", "depolarization") retained where they describe what happens during the cycle, not its name. Historical handover/session_log records preserved unchanged per anti-erasure discipline. CHANGELOG entries added to four SHIPPED papers (capotauro.tex, sf-2_electroweak.tex, sf-2_companion.tex, dynamical_substrate_law.tex) noting the post-SHIP terminology correction with no substantive content change.

**Files touched**: `master_glossary.md` (2 occurrences + entry enhancement); `frontier_sectors/SS.md` (1); `book_project/chapters/capotauro_what_was_always_there.md` (1); `flagship_papers/electroweak/sf-2_companion.tex` (2 + CHANGELOG); `flagship_papers/electroweak/sf-2_electroweak.tex` (2 + CHANGELOG); `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/dynamical_substrate_law.tex` (7 + external changelog entry); `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/F1_subquestion_pcd_orientation_link.md` (deep cleanup, 11+ occurrences including phase labels in §11 cycle structure detail); `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/layer3_promotion/F1_layer3_b1q4_algebraic_derivation.md` (1, en-dash form); `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/documentation_suite/keywords-dynamical-substrate-law.md` (2); `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/documentation_suite/glossary-dynamical-substrate-law.md` (2); `series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex` (3 + external changelog entry); `series_umbrella/series_substrate_chirality_arc/capotauro/documentation_suite/glossary-capotauro.md` (1); `series_umbrella/series_substrate_chirality_arc/capotauro/documentation_suite/reasoning-capotauro.md` (1); `series_umbrella/series_substrate_chirality_arc/capotauro/documentation_suite/philosophy-capotauro.md` (1); `series_umbrella/series_substrate_chirality_arc/chirality_continuum/sketches/F2_F3_viability_decision_gate_2026-05-21.md` (2).

**Historical records preserved unchanged** (anti-erasure discipline): `handovers/2026-05-20_session_137_close_manifestation_iv_next_window_seed.md`; `session_logs/2026-05-24_session_142_extracted_from_frontier.md`; "Earlier last-updated" entries throughout `research_frontier.md` history. Future readers encountering legacy "Polarize-Capture-Depolarize" terminology in archived/historical records can refer to the canonical master_glossary PCD entry or this TODO-012 cleared note for context.

**Forward**: Patch 0632 ships the THEO-CHIR-AUDIT-1 audit artifact under Pattern A sequencing (terminology baseline cleaned first; audit ships from clean baseline). Per Patch 0630 sketch document §5.2, the audit's §3.4 dynamics pass uses the canonical "Perceive, Compute, Displace" expansion throughout.

**Original registration**: 28 May 2026 Session 148 Patch 0630 (THEO-CHIR-AUDIT-1 scope sketch precondition gap §5.2).

### TODO-002 — SS-8 and SS-9 PDF compile (posting prerequisite) — CLEARED 7 May 2026 Session 36

**Cleared**: 7 May 2026 Session 36 via patches 0286 (SS-8.tex `\Kthree` macro `\ensuremath` fix) + 0287 (SS-8.tex `\usepackage{xcolor}` import for `yellow!10` blend) + direct commit `55c5986` (PDFs added to repo: SS-8 31 pages 507596 bytes, SS-9 32 pages 638209 bytes; both visually verified clean before commit; SS-9 compile triggered MiKTeX auto-install of `float.sty` per Phase C MiKTeX setting change).
**Resolution narrative**: First Thomas attempt (without patches 0285+0286+0287) compiled with errors and produced damaged PDFs (SS-8 abstract garbled with run-together italicized text from `\Kthree`-mode-quantum text, mdframed alert box on pages 15-16 rendering as solid black from undefined `yellow!10`). Damaged PDFs were committed as `6e86818` then reverted as `ccb6041` after diagnosis. Patches 0286 (`\Kthree` `\ensuremath` wrapper) and 0287 (`xcolor` package import) were then applied; MiKTeX auto-install set to "Yes"; aux files cleaned; recompile produced clean PDFs verified visually (K₃ subscript renders cleanly, alert box light-yellow as designed). Commit `55c5986` pushed both PDFs to origin successfully.
**Original registration**: 7 May 2026 Session 33 close patch 0274; scope corrected Session 36 patch 0285 to include SS-9.

---

## Maintenance

This file is maintained per session: any session that completes a TODO item moves it to "Cleared items (history)" with the completion date and patch number. Any session that identifies a new deferred item adds it here under the appropriate priority. Sessions that touch only this file (no other substantive work) follow the standard programme practice of session log + research_frontier.md last-updated entry — the documentation suite for a paper is updated only if the cleared item was paper-specific.

If this file's P1 section grows large (more than ~10 items), reconsider whether some items should be promoted to `future_projects.md` as registered multi-session projects rather than carried as to-dos.

If a P1 item turns out not to actually block the next paper on reflection, demote it to P2 with a note explaining why. The discipline is "P1 must be empty before SS-10," not "every deferred item is P1."

- **2026-07-15 (Patch 2502):** OPEN-SR-EPSILON RESOLVED-α (founder-ruled; W2 strength, caveats inherited); OPEN-SR-SF6-RECON-1 RESOLVED; geometric ε-route dead (round-2 unanimous). SR-1 rewrite opened, warm keyword SR1-WARM-2502. Panel next sees SR-1 when the rewrite is a shippable win.
