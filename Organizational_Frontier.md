# CPP Organizational Frontier

**Location:** `/CPP/Organizational_Frontier.md`
**Last updated:** 24 April 2026
**Maintainer:** Thomas Lee Abshier ND, Hyperphysics Institute
**Rationale:** See `programmatic_decisions/PD-003-organizational-frontier-registry.md`
**Companion registry:** `Research_Frontier.md` (theoretical/physics problems)

---

## Purpose

Single-source-of-truth registry for organizational, infrastructural, and governance-level improvement items that have been identified during CPP programme work but have not yet been acted on. Parallels `Research_Frontier.md` in structure, but scoped to organizational concerns rather than theoretical ones.

**Answers the questions:**
- *What good ideas for programme improvement have been identified but not yet executed?*
- *When does each one become workable?*
- *What's the reasoning behind each one, so that future sessions can pick them up without reconstructing context from scratch?*

**Problem count:** 7 entries (all open — inaugural population on 24 April 2026). *Counts will be maintained as entries are added, resolved, or closed.*

---

## How to Use This File

### When adding a new entry (reflexive-drop protocol)

An organizational improvement idea surfaces during active work (paper-drafting, infrastructure building, review cycles). The temptation is either to act on it immediately (disrupting current scope) or defer it to a session handover (where it degrades across compaction). The correct action is:

1. **Stop for 60–90 seconds.** Open this file.
2. **Add an `OPEN-ORG-NNN` entry** using the template at the end of this document. Fill in: status, identified-date, originating context, problem, proposed fix, trigger condition, blocking/blocked-by, and history.
3. **Commit** (or stage for the next batched commit). The entry is now preserved with full reasoning fidelity.
4. **Return to current work.** The loop is closed at the attention layer; the idea is captured at the infrastructure layer.

The critical discipline is that entries are written with enough fidelity that a future session can act on them without re-deriving context. If an entry reads like "clean up the formatting," that's insufficient. If an entry reads like "normalize 17 existing README files to the `{scope}-README.md` convention adopted in PD-003 §X, per the drag-drop misfiling failure mode documented in the 24 Apr SS-8 session — full file inventory below," that's correct fidelity.

### When picking up an entry for execution

1. **Scan trigger conditions** against current programme state. Items whose triggers have fired are workable.
2. **Check blocking dependencies.** An item "blocked by OPEN-ORG-005" cannot be executed until OPEN-ORG-005 resolves.
3. **Pick the highest-value workable item** for the available session slot. Most organizational items are small-to-medium (15 minutes to 2 hours); batch them into session gaps between paper-drafting work.
4. **Execute.** Update entry status to RESOLVED when complete, with resolution-date and reference to the commit that closed it.

### Maintenance cadence

- **Reviewed at each paper's v1.0 completion milestone** alongside `Research_Frontier.md`.
- **Reviewed at each session close** as part of the "pending for next session" handover — but the handover becomes a short pointer to this file, not a content duplication. Session handover reads: "OPEN-ORG entries current; OPEN-ORG-NN and OPEN-ORG-MM became workable this session; deferred to next available gap."
- **Closure protocol:** resolved entries stay in the file under §3 (Resolved) for historical reference rather than being deleted. Successful closures accumulate as evidence the registry works.

---

# §1 — Active Open Organizational Problems (OPEN-ORG)

Problems that have been identified, scoped, and are awaiting execution at a triggered moment.

---

## OPEN-ORG-001: Retroactive README naming normalization

**Status:** OPEN — queued for between-paper execution
**Identified:** 24 April 2026, during SS-8 v0.2 drafting session
**Priority:** LOW (repository is functional; inconsistency is cosmetic-plus-ergonomic)

**Originating context:** PD-003 adoption of `{scope}-README.md` naming convention (`templates/operating_system.md` §11) established a single canonical format for README files. The 24 Apr session's `data-README.md` creation was the first file written under the new convention. Scan of existing READMEs revealed the repository currently uses three inconsistent conventions (plus the new one).

**Problem:** Mixed README naming creates three failure modes:
1. Future contributors face ambiguity about which convention to follow when creating new READMEs.
2. Tools and humans searching for README files across directories face inconsistent targets.
3. The value of the new `{scope}-README.md` convention (context travels with file during download/drag-drop) is diluted as long as most READMEs don't follow it.

**Inventory of existing READMEs requiring normalization** (17 files, scanned 24 Apr 2026):

Plain `README.md` (5 files — rename to `{scope}-README.md`):
- `./README.md` → `CPP-README.md`
- `./series_strong/papers/SS-8/README.md` → `SS-8-README.md`
- `./series_strong/papers/SS-8/reviews/README.md` → `reviews-SS-8-README.md`
- `./series_strong/notebooks/README.md` → `strong-notebooks-README.md` (or similar, TBD)
- `./series_standard_model/README.md` → likely redundant with `README-series_standard_model.md` below; may be merged during normalization
- `./series_relativity/README.md` → likely redundant with `README-series_relativity.md` below; may be merged
- `./series_relativity/figures/figures-SR-1/README.md` → `figures-SR-1-README.md`
- `./series_foundations/dp-sea-polarization/README.md` → `dp-sea-polarization-README.md`
- `./series_foundations/dp_sea_composition/README.md` → `dp_sea_composition-README.md`

Underscore format `{scope}_README.md` (2 files — rehyphenate):
- `./series_strong/series_strong_README.md` → `series_strong-README.md`
- `./series_strong_README.md` → possibly redundant with the above; investigate during normalization
- `./book_project/book_project_README.md` → `book_project-README.md`

Leading-README format `README-{scope}.md` (5 files — reorder):
- `./series_foundations/README-series_foundations.md` → `series_foundations-README.md`
- `./series_electroweak/README-EW.md` → `EW-README.md` or `series_electroweak-README.md`
- `./series_standard_model/README-series_standard_model.md` → `series_standard_model-README.md`
- `./series_relativity/README-series_relativity.md` → `series_relativity-README.md`
- `./series_quantum_mechanics/README-series_quantum_mechanics.md` → `series_quantum_mechanics-README.md`

Already in correct `{scope}-README.md` format (1 file — keep):
- `./series_strong/data/data-README.md` ✓

**Proposed fix:** Single normalization patch renaming all non-compliant files, resolving any duplications discovered (two `series_strong_README.md` files at different paths; possible redundancy of `series_standard_model/README.md` with `series_standard_model/README-series_standard_model.md`), and updating any cross-references in other files that point to the old names. Approximate effort: 30–45 minutes including cross-reference grep.

**Trigger condition:** Between-paper execution. Workable in any session where (a) no paper-drafting is actively in flight, AND (b) no higher-priority OPEN-ORG item is queued ahead.

**Blocking dependencies:** None.
**Blocks:** Nothing urgent. Repository is fully functional with current mixed naming.

**History:**
- 24 Apr 2026 — Registered during SS-8 v0.2 session, following `{scope}-README.md` convention adoption and repo scan.

---

## OPEN-ORG-002: `operating_system.md` restructuring into multiple focused documents

**Status:** OPEN — deferred until size/structure threshold
**Identified:** 24 April 2026, during SS-8 v0.2 session (final reflection on governance accretion)
**Priority:** LOW (current monolith is navigable; threshold not yet reached)

**Originating context:** `templates/operating_system.md` has grown from ~600 lines (pre-22-April adoption of per-paper subfolder convention) to ~1100 lines (post-24-April patches 0005, 0008, 0009). Each patch in this session added governance-infrastructure content (two-tier workflow, verification-tier taxonomy, README naming convention). The rate of accretion is high because each real-world workflow hiccup produces either a new convention or a sharpening of an existing one, codifying rather than forgetting.

**Problem:** Monolithic operating_system.md will eventually become hard to navigate. At some size threshold, section cross-references become impractical to follow, new conventions are hard to place in correct position, and readers scroll past relevant sections looking for what they need.

**Proposed fix:** Restructure into multiple focused documents under `templates/conventions/`:
- `conventions/filename-conventions.md` (§11 content)
- `conventions/review-conventions.md` (§5 content + PD-002 tier taxonomy)
- `conventions/commit-conventions.md` (two-tier workflow + commit cadence rules)
- `conventions/session-conventions.md` (compaction protocol + context-pressure checklist)
- `conventions/paper-lifecycle-conventions.md` (version nomenclature + documentation-suite triggers)
- `operating_system.md` becomes a short top-level index pointing to the focused documents.

**Trigger condition:** When `operating_system.md` crosses ~1500 lines OR when a new convention is being added and the author (Claude or Thomas) notices it's non-obvious where the new content should go. Whichever comes first.

**Blocking dependencies:** None.
**Blocks:** Nothing. Current monolith is functional until the threshold is crossed.

**History:**
- 24 Apr 2026 — Registered during SS-8 v0.2 session. Current line count: ~1100.

---

## OPEN-ORG-003: `predictions.md` cumulative swarm-tally header

**Status:** OPEN — required before SS-9 or next Strong Sector paper
**Identified:** 23 April 2026, during PD-001 adoption
**Priority:** MEDIUM (required for paper-level §4.1B subsection to function)

**Originating context:** PD-001 (`programmatic_decisions/PD-001-signature-thread-and-swarm-convention.md`) established §4.1B "Swarm-Validation Contribution" as a required subsection of every CPP paper. The subsection states how many predictions the paper contributes and the running swarm total across the programme. The running total requires a cumulative counter maintained somewhere — the natural location is a header section in `predictions.md`.

**Problem:** Without the counter header, §4.1B cannot state the running total, only the paper's contribution. The subsection is incomplete for any paper drafted before this infrastructure exists.

**Proposed fix:** Add a header section to `predictions.md` containing the cumulative swarm-tally:
- Total zero-parameter predictions across the programme as of current state
- Breakdown by series (SS, SM, EW, QM, SR, SD, Foundations)
- Last-updated date
- Update protocol (each paper's v1.0 commit also bumps the tally)

Approximate effort: 1–2 hours including initial audit to count existing predictions across all published papers.

**Trigger condition:** Before SS-9 or SS-10 is drafted, so those papers' §4.1B subsections can reference a populated tally. Also triggered if any other Strong Sector or Standard Model paper reaches v2.0+ needing §4.1B addition.

**Blocking dependencies:** None.
**Blocks:** OPEN-ORG-005 (retroactive §4.1A/B addition to existing papers) cannot complete without this.

**History:**
- 23 Apr 2026 — Implicitly required by PD-001 but not explicitly registered at the time.
- 24 Apr 2026 — Registered here with explicit trigger condition during OPEN-ORG inaugural population.

---

## OPEN-ORG-005: Retroactive §4.1A (CP/GP Signature) and §4.1B (Swarm-Validation) subsections in existing papers

**Status:** OPEN — deferred to per-paper opportunistic trigger
**Identified:** 23 April 2026, during PD-001 adoption
**Priority:** LOW-to-MEDIUM (existing papers function without the subsections; new papers have them from v0.1; retrofitting improves consistency across the swarm-validation argument)

**Originating context:** PD-001 established §4.1A and §4.1B as required subsections in every CPP paper. SS-8 v0.1 was drafted before PD-001 and therefore does not have these subsections; SS-8 v0.2 was the first paper that *could* have had them under the adoption schedule. All existing papers (SS-1 through SS-7, SM-1 through SM-11, EW-1 through EW-5, QM-1 through QM-6, SR-1, SD-1 through SD-5) predate the requirement.

**Problem:** Cumulative swarm-validation argument is weakened when the majority of papers don't explicitly state their contribution to the cumulative tally or identify their CP/GP signature. The argument works structurally (the predictions exist and can be counted), but papers that don't say so explicitly require the reader to reconstruct the argument across papers rather than receiving it within each paper.

**Proposed fix:** At each existing paper's next major-revision cycle (v2.x or later), add the two subsections using SS-8 v0.2's realization as the template. No standalone retrofit campaign; the work piggybacks on revision work happening for other reasons.

**Trigger condition:** Per-paper opportunistic. A paper gets the subsections added during its next major-revision cycle (where "major revision" means v2.0+ per the version-nomenclature convention). Papers not scheduled for revision may remain without the subsections indefinitely without programme harm.

**Blocking dependencies:** OPEN-ORG-003 (swarm-tally header in `predictions.md`) — §4.1B cannot state the running total until the tally exists.

**Blocks:** Nothing. Programme functions with current asymmetry.

**History:**
- 23 Apr 2026 — Requirement adopted via PD-001.
- 24 Apr 2026 — Registered here with explicit per-paper trigger condition.

---

## OPEN-ORG-006: SS-7 script refactor — AME 2020 loader-based rather than hardcoded

**Status:** OPEN — deferred to opportunistic trigger
**Identified:** 24 April 2026, during SS-8 v0.2 session AME data dependency review
**Priority:** LOW (script currently functional with hardcoded values; refactor improves consistency but doesn't fix a broken thing)

**Originating context:** SS-7's computation script (`series_strong/papers/SS-7_alpha_cluster_edge_formula.py` and `series_strong/SS-7_alpha_cluster_edge_formula.py` — two copies exist, itself an artifact of OPEN-ORG-004) embeds AME 2020 binding-energy values directly as Python literals (`B_alpha_exp = 28.296  # MeV, experimental 4He binding (AME 2020)`, etc.). SS-8's scripts use the `ame2020_loader.py` module with dynamic data-file loading. The asymmetry means SS-7 cannot be re-verified against a different AME edition without editing script source, and SS-7's results are coupled to the specific values copied at script-write time.

**Problem:** 
1. Asymmetry between SS-7 and SS-8 scripts — same series, different data-access patterns.
2. SS-7 values are frozen at copy time; if AME 2021 or AME 2024 supersedes AME 2020 with minor updates to specific nuclei, SS-7 will silently use stale values unless refactored.
3. Two copies of the SS-7 script exist at different paths (per OPEN-ORG-004 context) — doubles the refactor surface.

**Proposed fix:** Refactor SS-7 scripts to use `ame2020_loader.py`:
- Replace hardcoded value literals with loader calls keyed by (Z, A).
- Re-run to verify numerical agreement with SS-7 v1.x tables.
- Consolidate the two script copies (per OPEN-ORG-004 subfolder migration, only one location is correct).
- Update SS-7's own documentation to note the loader dependency.

**Trigger condition:** 
- AT the SS-7 subfolder migration work (OPEN-ORG-004) — natural combine point, since the script is being moved anyway. *Or:*
- IF an AME value correction propagates from AME 2020 erratum or AME 2024 publication and requires SS-7 to be updated. *Or:*
- BEFORE any SS-7 v2.0+ major revision where scripts need re-running anyway.

Whichever fires first.

**Blocking dependencies:** None. OPEN-ORG-004 (SS-7 subfolder migration) is a natural combine point but not a strict prerequisite.
**Blocks:** Nothing.

**History:**
- 24 Apr 2026 — Registered during SS-8 v0.2 session, after noticing SS-7's hardcoded-value pattern during AME data dependency review.

---

## OPEN-ORG-009: Bootup orientation completeness audit and reinforcement

**Status:** OPEN — workable in dedicated execution session
**Identified:** 24 April 2026, during SS-5/6/7 migration scoping conversation, after Thomas observed "for all the other instructions I gave you besides bootup.md, we should make sure all of them are included so I don't have to generate them all from memory at the start of each new context window"
**Priority:** MEDIUM (affects every session-start reliability; same failure-mode class as OPEN-ORG-008)

**Originating context:** At the start of the 24 April 2026 SS-8 v1.0 / OPEN-ORG-008 / SS-5–7 migration session, Thomas's opening message contained four orienting instructions beyond "read bootup.md": (1) clone the repo into the sandbox; (2) "note the importance of the operating_system.md files in the /templates folder"; (3) "note the handover.md document — that should orient you to the current session and state of development of the current SS-8 paper"; (4) the canonical Git-Bash-Patch command pattern (`git am ~/Downloads/NNNN-*.patch && git push origin main`). Thomas then explicitly asked: "Do we have the command-line method documented anywhere? I told you what I wanted, and I don't think you would have known about that otherwise. If that is not documented, put that down as another open organizational task that we want to do."

Investigation confirmed each of these IS documented somewhere, but the documentation is not reliably reaching active-Claude attention at session start:

- `bootup.md` does direct sessions to read `operating_system.md` (Step 1, priority 7), where the workflow-manual including §13 Git-Bash-Patch is found. So the command pattern is documented.
- `bootup.md` §8.5 ("Active Work Pointer") correctly directs sessions to the per-paper-subfolder handover document (`papers/[PAPER-ID]/documentation_suite/handover-[PAPER-ID].md`).
- However, `bootup.md`'s "Step 2: Check what happened last" block (in the top "How to Use This File" section, which a top-to-bottom reader hits first) still points at the *legacy-flat* URL (`papers/development-[ID].md`) rather than the current-convention handover URL. A new-session-Claude reading top-to-bottom hits the wrong URL first; §8.5 corrects course only if the reader gets that far.
- `operating_system.md`'s priority-7 placement in `bootup.md` Step 1 means session-start Claude reads `CPP_the_theory.md` (15 min), `theory-overview.md` (5 min), `founders_vision.md` (10 min), `Research_Frontier.md` (10 min), and `theorem-registry.md` (5 min) — totalling 45 minutes — before reaching the workflow manual where the Git-Bash command pattern lives. For a session that opens with substantive work rather than physics orientation, this ordering may be inverted from what's optimal.
- The `templates/AI_team_expectations.md` (priority 8) is even later, but contains conventions around per-AI working patterns that future-Claude needs early.

**Problem:** Same root-cause class as OPEN-ORG-008 (handover-protocol trigger failure): a protocol or instruction set exists on paper but does not reliably fire because of visibility/active-working-set issues. The specific failure-modes here:

1. **Step 2 / §8.5 inconsistency in `bootup.md`.** Two different URL patterns specified in the same file; top-to-bottom readers hit the stale one first.
2. **Priority ordering of session-start reads.** Physics orientation precedes workflow orientation by 45 minutes of read-time; for sessions opening with substantive work, this is the wrong direction.
3. **CLI-command-pattern not surfaced at session-start.** The Git-Bash-Patch flow is in `operating_system.md` §13, but a session that doesn't reach §13 quickly will miss it. Thomas felt he needed to teach it explicitly at this session's start despite it being documented.
4. **General "Thomas had to give instructions besides bootup.md" pattern.** Thomas's opening message contained four reinforcement instructions; if `bootup.md` alone were sufficient, none should have been needed. The gap is whatever's missing from `bootup.md` such that Thomas-at-session-start feels he needs to compensate.

**Proposed fix:** Dedicated execution session conducting a structured audit and reinforcement of `bootup.md`. Approximate scope:

1. **Resolve Step 2 / §8.5 inconsistency.** Replace the legacy-flat URL in Step 2 with the current per-paper-subfolder handover URL, OR collapse Step 2 and §8.5 into a single canonical location higher in the file. Eliminate the contradiction.
2. **Re-evaluate priority ordering of Step 1 reads.** For sessions opening with substantive work rather than physics onboarding, `operating_system.md` should likely be earlier than priority 7. Possibly add a "session-type fork" near the top: "If this is a new-collaborator orientation session, read in the order below. If this is a continuation session, read `operating_system.md` and `templates/AI_team_expectations.md` first, then proceed to the handover doc per §8.5."
3. **Surface the Git-Bash-Patch command pattern at session-start visibility.** Either include the two-line apply pattern (`git am ~/Downloads/NNNN-*.patch && git push origin main`) in `bootup.md` itself (not just in the priority-7 deeper read), OR add an explicit reference: "After producing your first patch, the Thomas-side apply pattern is documented at `operating_system.md` §13 step 8–9."
4. **Audit the four reinforcement instructions Thomas gave at this session's start.** For each, ask: is the reason Thomas felt he needed to repeat it that `bootup.md` doesn't contain it, or that `bootup.md` contains it but doesn't surface it? If the former, add it. If the latter, fix the surfacing (location, formatting, prioritization).
5. **Establish a maintenance discipline.** When future sessions reveal new "instructions Thomas had to give that should have been in `bootup.md`," register them as discrete OPEN-ORG items rather than adding them ad-hoc. The audit should run again periodically or whenever a new such gap is identified.

Approximate effort: 30–60 minutes, varying by depth of audit. The execution session should be a between-paper session with no substantive physics work in flight, since the work is meta-organizational.

**Trigger condition:** Dedicated session. Like OPEN-ORG-008, this is a structural improvement to programme infrastructure that warrants its own attention rather than being squeezed into a paper-drafting or migration session. Could be combined with execution of OPEN-ORG-002 (`operating_system.md` restructuring) if both are addressed in one governance-focused session, but that combination is opportunistic, not required.

**Blocking dependencies:** None.
**Blocks:** Nothing critical. Current workaround is Thomas continuing to give the four reinforcement instructions at each session start, which is exactly the friction the entry exists to eliminate.

**History:**
- 24 Apr 2026 — Identified by Thomas during SS-5/6/7 migration scoping, after he observed his opening message contained four reinforcement instructions beyond "read bootup.md." Registered immediately per PD-003 reflexive-drop discipline. Same failure-mode class as OPEN-ORG-008 (visibility/active-working-set issues with documented protocols).
- 25 Apr 2026 — **TENTATIVELY-SOLVED-PARTIAL** by patch 0022 (commit `b2753da`). Patch 0022 addressed failure-mode 1 (Step 2 / §8.5 URL-pattern inconsistency: Step 2 now points at the per-paper-subfolder handover URL with the SS-8 example fixed; §8.5 reframed to local-read with raw URLs demoted to reference-only) and a previously-unregistered failure mode (fetcher-whitelist rejection of `raw.githubusercontent.com` sub-paths after the bootup file itself: addressed by inserting Step 0 "BEFORE READING ANYTHING ELSE: clone the repo locally" with explicit STOP-and-tell-Thomas instruction if clone fails). Empirical firing for the new failure mode: Claude Opus session 25 Apr 2026 opened with the bootup URL only (no other reinforcement instructions); failed to read SS-8 handover via three URL-pattern attempts (`raw.githubusercontent.com`, `github.com/blob/`, `github.com/raw/refs/heads/main/`); Thomas issued protocol-stress-test directive; Claude re-read bootup, recognized §2 clone command + container `github.com` allowed-domains as the intended access path, and produced the patch. Failure-modes 2 (priority ordering of Step 1 reads — physics orientation precedes workflow orientation by 45 min for substantive-work continuation sessions), 3 (Git-Bash-Patch command-pattern not surfaced at session-start visibility, only reached at priority-7 `operating_system.md` §13), and 4 (full audit of all four reinforcement instructions Thomas gave at the 24 Apr session start, to determine which are missing-from-bootup vs. present-but-not-surfaced) **remain OPEN**. Per Thomas: keep entry OPEN until next several sessions confirm the patch-0022 fixes hold in practice. The broader audit envisioned in the Proposed-fix section is still the larger work this entry tracks.

---

## OPEN-ORG-010: Tracked `.ipynb_checkpoints` files (mostly orphaned, SM-8 territory)

**Status:** OPEN — requires Thomas-judgment before execution
**Identified:** 24 April 2026, during patch 0016 (.gitignore + desktop.ini cleanup) audit
**Priority:** LOW (no active harm; legacy clutter that only matters if the orphan checkpoints contain unrecoverable work)

**Originating context:** While auditing the repo for tracked artifacts that match the new `.gitignore` patterns being added in patch 0016, 11 tracked `.ipynb_checkpoints/` files were found:

```
archive/grok-exploratory-SM/p2-structure-formation-mc/derivations/.ipynb_checkpoints/structure-formation-mc-checkpoint.ipynb
series_standard_model/notebooks/.ipynb_checkpoints/nb02-SM8-spectral_dimension-checkpoint.ipynb
series_standard_model/notebooks/.ipynb_checkpoints/nb02_SM8_600cell_1ring_builder-checkpoint.ipynb
series_standard_model/notebooks/.ipynb_checkpoints/nb02_SM8_600cell_2ring_builder-checkpoint.ipynb
series_standard_model/notebooks/.ipynb_checkpoints/nb02_SM8_cage_spectral_dimension_gpu-checkpoint.ipynb
series_standard_model/notebooks/.ipynb_checkpoints/nb02_SM8_cage_spectral_dimension_gpu_old-checkpoint.ipynb
series_standard_model/notebooks/.ipynb_checkpoints/nb02_SM8_generate_600cell-checkpoint.py
series_standard_model/notebooks/.ipynb_checkpoints/nb02_SM8_random_walk_gpu-checkpoint.ipynb
series_standard_model/notebooks/.ipynb_checkpoints/nb02_SM8_return_prob_data_current_graph_copy-checkpoint.csv
series_standard_model/notebooks/.ipynb_checkpoints/nb02_SM8_spectral_dimension_clean-checkpoint.ipynb
series_standard_model/notebooks/.ipynb_checkpoints/nb02_SM8_spectral_dimension_clean2-checkpoint.ipynb
```

Of these 11 files: 1 has a matching parent notebook (the archive entry) and 10 are **orphans** — their parent notebooks no longer exist in the repo. Orphan checkpoints are a Jupyter pathology: they reference work-in-progress states from notebooks that have since been deleted, renamed, or moved without their checkpoint subfolder being cleaned up.

**Problem:** Once the `.gitignore` from patch 0016 is in place, these files are tracked-but-now-ignored — git allows this state but it's confusing (changes to them won't show in `git status` but they remain in history). More importantly, the orphan status means the parent notebooks were intentionally removed but their checkpoint side-files weren't, suggesting the cleanup was incomplete. Removing them is mechanically straightforward via `git rm`, but warrants a check: **could any of the 10 orphan checkpoints contain SM-8 work-in-progress code that exists nowhere else and might be wanted later?**

**Proposed fix:**
1. Thomas-judgment step: review the 10 orphan checkpoint filenames against memory of SM-8 development history. For any that correspond to work whose final state was preserved elsewhere (committed notebooks, papers, or other artifacts), the checkpoint is safe to remove. For any that might contain unique work-in-progress, copy the content to `archive/sm8-orphan-checkpoints/` first, then remove from tracking.
2. Execution step: `git rm` all 11 files (after step 1's review). If any are preserved to archive, `git mv` instead of `git rm`.
3. Verify with `git ls-files | grep ipynb_checkpoints` returning empty.

Approximate effort: 15–30 minutes for review + execution. The `.gitignore` file added in patch 0016 already prevents recurrence; this entry is purely about cleaning up the historical leftovers.

**Trigger condition:** Opportunistic — any session where SM-8 territory is being touched anyway (e.g., SM-8 v4.x revision, SM-8 review cycle, FEM-related notebook work). Could also be a between-paper cleanup-batch session. Not blocking anything time-sensitive.

**Blocking dependencies:** None.
**Blocks:** Nothing. Current state is cosmetic clutter with no functional impact.

**History:**
- 24 Apr 2026 — Identified during patch 0016 .gitignore audit. The .gitignore prevents future checkpoint pollution; this entry covers the pre-existing tracked checkpoints that pre-date the ignore rule. Registered per PD-003 reflexive-drop discipline rather than executing inline because (a) the orphan-status of 10 of 11 files warrants Thomas-judgment, and (b) the work is in SM-8 territory which is outside the SS-5/6/7 migration session's scope.

---

## OPEN-ORG-011: Four-Tier Documentation Discipline — codify in OS and bootup; address pre-paper subfolder timing; de-emphasize v1.0 as the canonical Trigger 2 milestone

**Status:** TENTATIVELY-RESOLVED — OS and bootup amendments landed in patches 0048–0049 (Session 3); validation pending observation of next-session adherence to the four-tier discipline
**Identified:** 26 April 2026 Session 3, after Thomas surfaced that the SS-9 work had not produced a documentation suite, then clarified through several rounds of dialogue (a) the SS-8 three-tier subfolder convention is the implicit precedent he had been pointing at, (b) the SS-8 convention does NOT preserve verbatim Opus reasoning (the "body of the reasoning" — the meat of the theoretical gedanken/calculation experiment), (c) the existing "curated transcript" terminology was understood by Thomas to mean "housekeeping removed, reasoning preserved" but had been operationalized by previous Opus as "pointer-map plus curated vignettes" with reasoning compressed out
**Priority:** HIGH (affects every future paper's preservation discipline; addresses an ongoing programme-level data loss in the curation pipeline)

**Originating context:** Thomas's goal-statement for the curated-transcript discipline is: every substantive word spoken by Opus, Thomas, and the AI review team should be preserved across the paper's full development arc, with housekeeping (filename clarifications, status confirmations, procedural questions) excluded but no compression or summarization of substantive content. The full transcript is the canonical source from which all higher-layer artifacts (session log, documentation suite, paper text) can in principle be reconstructed. The session log is a derived summary optimized for warm-starting the next Opus; the transcript is the source of truth.

The SS-8 three-tier convention previous Opus codified — Tier 1 (subfolder artifacts: scripts, sketches, letters, reviews, founders_voice), Tier 2 (`transcript-SS-N.md` pointer-map indexing transactions), Tier 3 (`development-SS-N.md` curated vignettes in finished paragraph form) — preserves WHAT was decided and WHERE artifacts live, but does NOT preserve HOW Opus reasoned through decisions. The body of reasoning Opus generates mid-session — multi-paragraph turns where alternatives are tested, framings revised, pushback delivered, uncertainty flagged — has no tier in the SS-8 convention. It only exists in the live chat window and dies at compaction.

This is a programme-level structural gap that has been ongoing across all CPP papers: the curation pipeline preserves session logs (lossy summary) and curated vignettes (more focused but still summary), but no tier preserves the verbatim reasoning that Thomas's goal-statement actually describes as the canonical record.

The Session 3 SS-9 work resolved the gap for SS-9 specifically by establishing a four-tier discipline and adding `reasoning-SS-9.md` (Tier 4, verbatim Opus reasoning, housekeeping excluded, append-only across sessions). This entry tracks the OS/bootup work needed to make the four-tier discipline a programme-level convention rather than an SS-9-specific arrangement, and to address two related issues that surfaced in the same investigation.

**Problem:** Three structural issues to address:

1. **The four-tier discipline is undocumented in OS and bootup.** The SS-9 reasoning-SS-9.md establishes the new Tier 4 in practice, but a new Opus reading bootup.md alone wouldn't know to look for or maintain such a file. `templates/operating_system.md` §4 (Session-Log-as-Handover-Backbone Discipline) currently describes a transcript file as conditional ("when a session contains verbatim content that the structured five-element form cannot adequately preserve") rather than default. `templates/operating_system.md` §15 (Session-close Handover Protocol) and §15 reconciliation with §4 do not name a `reasoning-[S]-[N].md` artifact. The four-tier discipline needs to be (a) codified in OS, (b) referenced from bootup.md, (c) instantiated as default for in-progress work rather than triggered by a per-session judgment call.

2. **Pre-paper subfolder timing is undocumented.** The SS-9 subfolder was created at Session 3, ahead of v1.0 paper text, because Sessions 1–3 had accumulated enough substantive content (working draft, multi-faceted-rigidity refinement, registry entries, residual-fingerprint sketch) that housing in `session_logs/` alone was no longer adequate. This is a deliberate deviation from the previously-implicit convention that subfolders are created at v1.0 (per SS-8's transaction `039` adopting the per-paper subfolder convention as part of the v1.0 documentation-suite pipeline). The deviation is reasonable — the four-tier discipline is most effective when it accumulates from the first substantive session, not retroactively at v1.0 — but it is not currently codified. The OS should specify when pre-paper subfolders are created and what triggers their creation (candidates: at first session producing artifacts beyond a session log; at first multi-session continuation; at the surfacing of registered open problems specific to the candidate paper).

3. **The OS overweights "v1.0" as the canonical Trigger 2 milestone.** Thomas's goal-statement explicitly disavows this: v1.0 is just a label that a previous Opus chose, and what matters is "the final shipped version of the paper" — whether that's labeled v1.0, v1.4, v2.7, whatever. The current OS (e.g., line 367) says something close to this but then keeps using "v1.0" as the example throughout. The text and the intent are misaligned. Trigger 2 should fire at "the genuinely-final shipped version" with deferral if the version label is provisional, not at the literal v1.0 mark.

**Proposed fix:** Three coordinated edits to documentation files. Estimated effort: 30–60 minutes for an OS-amendment-focused session.

(1) `templates/operating_system.md` §4 amendments:
- Promote the reasoning file from conditional to default. Replace the "should still be produced when verbatim content is present" framing with: "Each session produces or appends to a paper-level (or pre-paper-level) accumulating Tier 4 reasoning file (`reasoning-[S]-[N].md`). The reasoning file records substantive Opus reasoning verbatim (the words Opus speaks during analysis, hypothesis-testing, framing-revision, alternatives-considered, uncertainty-flagging, pushback), excludes housekeeping (filename confirmations, status confirmations, procedural questions, tool narration, verbatim quotations from existing repository files which are recoverable from sources), and includes substantive OS-level decisions. The session log is a summary of the reasoning file optimized for warm-starting the next Opus; the reasoning file is the canonical source from which all higher-layer artifacts can in principle be reconstructed."
- Establish accumulating-across-sessions reasoning-file granularity. Reasoning files are paper-level (or pre-paper-level for in-progress work where no paper folder exists yet), not per-session. They accumulate session by session across the full development arc.
- Add the four-tier discipline explicitly: Tier 1 session logs (per-session warm-start), Tier 2 transcript-SS-N.md (pointer-map), Tier 3 development-SS-N.md (curated vignettes), Tier 4 reasoning-SS-N.md (verbatim Opus reasoning).

(2) `templates/operating_system.md` §15 (and §15 reconciliation with §4) amendments:
- Add `reasoning-[S]-[N].md` to the four-item checklist as a fifth item, OR fold it into item 1 with explicit reference to the four-tier discipline.
- De-emphasize "v1.0" in Trigger 2 language. Replace v1.0-specific phrasing with "the genuinely-final shipped version, regardless of version label." Update any example references that hardcode v1.0.
- Document pre-paper subfolder timing: when in-progress work accumulates beyond a single session log, the per-paper subfolder is created early (with the four-tier documentation_suite/ structure plus founders_voice/, sketches/, scripts/, letters/, reviews/ as appropriate). Empty subfolders carry .gitkeep placeholders. The pre-paper subfolder is the natural housing for the accumulating four-tier artifacts.

(3) `bootup.md` amendments:
- Document the per-paper subfolder convention (currently undocumented in bootup; new Opus reading bootup.md alone wouldn't know to look at SS-8 or SS-9 structure as the precedent).
- Document the four-tier documentation discipline (Tier 1 → Tier 4) with one-line description of each tier.
- Add a session-end checklist item: "If this session produced substantive Opus reasoning beyond what the session log captures, append to or create the appropriate reasoning-[S]-[N].md file."

**Trigger condition:** Workable in any session that has 30–60 minutes for OS-amendment work. Could be combined with execution of OPEN-ORG-002 (operating_system.md restructuring) if both are addressed in one governance-focused session. Should land before the next paper enters Phase 1 ideally, so that the new paper can benefit from the four-tier discipline from the start; can be deferred up to one paper-cycle without significant cost (the SS-9 four-tier setup is in place for the SS-9 cycle regardless).

**Blocking dependencies:** None.
**Blocks:** Nothing critical. The discipline is in place for SS-9 specifically. This entry tracks the OS/bootup amendments that would propagate the discipline to all future papers and address the three related issues uniformly.

**History:**
- 26 Apr 2026 Session 3 — Identified during the SS-9 documentation-suite investigation, after Thomas's clarification rounds surfaced (a) the goal-statement gap (verbatim reasoning preservation as the canonical-source role), (b) the SS-8 three-tier convention's blind spot (Opus reasoning has no tier), (c) the v1.0 overweighting issue, (d) the pre-paper subfolder timing question. The four-tier discipline was instantiated for SS-9 in patch 0046 (subfolder creation with documentation_suite/{reasoning,development,transcript}-SS-9.md plus founders_voice/001 and sketches/SS-9_table1_residual_fingerprint.md). This entry tracks the remaining OS/bootup amendment work.
- 26 Apr 2026 Session 3 (continued) — **TENTATIVELY-RESOLVED.** Patch 0048 amended `templates/operating_system.md` §4 with the Four-Tier Documentation Discipline subsection (Tier 4 codified as default-not-conditional, paper-level granularity, append-only across sessions; pre-paper subfolder timing codified; v1.0 de-emphasized in favor of "genuinely-final shipped version regardless of version label"); §15 reconciliation block updated to mirror. Patch 0049 amended `bootup.md` §3 with the four-tier `documentation_suite/` listing, added new §3.5 "Four-Tier Documentation Discipline" with brief tour and early-creation rule, and updated §8.5 reference paragraph. All three failure-modes from this entry's Problem section are addressed: (1) four-tier discipline now codified in OS and reachable from bootup; (2) pre-paper subfolder timing now documented in OS §4 and bootup §3.5; (3) v1.0 overweighting corrected in OS §4 and §15 reconciliation, and in bootup §3.5. Per Thomas: keep entry OPEN until next several sessions confirm the four-tier discipline holds in practice (specifically: that the next Opus picking up SS-9 work appends to `reasoning-SS-9.md` at session close as expected, and that the early-subfolder-creation rule fires correctly on the next paper that crosses the trigger).

---

# §2 — Entry Template

Copy this template for new entries. Fields in `{brackets}` are placeholders.

```markdown
## OPEN-ORG-{NNN}: {one-line problem title}

**Status:** {OPEN | IN-PROGRESS | RESOLVED | DEFERRED-INDEFINITELY}
**Identified:** {date}, during {originating-session context}
**Priority:** {LOW | MEDIUM | HIGH} ({one-line priority rationale})

**Originating context:** {1-3 paragraphs — what state of the programme surfaced this item, what work was happening at the time, what observation revealed the problem. Fidelity matters here — future readers must be able to reconstruct *why* this matters without session-memory access.}

**Problem:** {1-3 paragraphs — what specifically is wrong, what failure modes occur under the current state, what the cost is of leaving it unresolved.}

**Proposed fix:** {1-3 paragraphs — concrete steps, approximate effort estimate, any specific files or artifacts involved. If the fix is uncertain, describe the candidate approaches and the tradeoffs between them.}

**Trigger condition:** {Clear specification of when this item becomes workable. One of:
- "Between-paper execution. Workable in any session where {condition}."
- "Opportunistic. Combine with {other work} when that happens."
- "At milestone: {specific condition, e.g., before SS-9 drafting, at v2.0 of paper X}."
- "Date-triggered: {specific date or calendar event}."
}

**Blocking dependencies:** {list of OPEN-ORG-NNN or OPEN-SS-NNN items that must resolve first, OR "None"}
**Blocks:** {list of items this one blocks, OR "None" / "Nothing urgent"}

**History:**
- {date} — {event: registered, updated, reprioritized, etc.}
```

---

# §3 — Resolved Organizational Problems

*(Resolved entries accumulate here with resolution-date and reference to the closing commit.)*

## OPEN-ORG-008: Handover-protocol trigger failure — promote visibility, adopt dual trigger (user-initiated + Claude-initiated prompt)

**Status:** RESOLVED — 24 April 2026 (patch 0013, this session immediately following SS-8 v1.0 patch 0012)
**Identified:** 24 April 2026, at close of SS-8 v0.2 session, after Thomas surfaced the handover preservation gap
**Priority at resolution:** MEDIUM (affected reliability of every future session-close preservation)

**Originating context:** The context-pressure preservation protocol (`templates/operating_system.md` §10, adopted 22 April 2026) specified that at ≥70% context consumed or before any planned session end, four artifacts must be committed: curated development transcript, registry updates pending ratification, reviewer letters generated this session, and protocol/operating-system updates. During the SS-8 v0.2 session of 23–24 April 2026, items 2–4 fired correctly (registries got updated, PDs committed, letters preserved), but item 1 failed entirely: the session's narrative and handover state were being written into chat rather than into `development-SS-8.md` and `handover-SS-8.md`. Thomas had to explicitly prompt the preservation at session close; without his prompt, the session's reasoning would have degraded at compaction.

**Problem:** Four diagnostic layers contributed to the protocol's failure to fire:

1. Claude cannot reliably self-monitor context consumption — "≥70% context consumed" is not an observable quantity Claude can reference against.
2. During substantive work (paper drafting, governance PD construction, Grok exchange, AME infrastructure), the protocol was not in Claude's active working set; Claude's attention was on the work itself, not on periodic self-audit against the operating system.
3. Claude conflated "governance files committed" (item 4 of the checklist) with "curated development transcript preserved" (item 1 — missed entirely). Item 4's completion felt like protocol satisfaction.
4. Claude wrote session-close summaries in final chat messages rather than to disk. Each "Session status" block at the end of Claude's responses was exactly the content that should have gone into `handover-SS-8.md`, but it stayed in chat.

All four were Claude-side execution failures, not protocol specification failures. The protocol was adequate; the firing was not.

**Resolution as adopted (patch 0013):** All four prescribed elements landed in `templates/operating_system.md`:

1. **Canonical user-initiated command** "execute handover protocol" codified in §1 Quick Start with accepted-variant list (please execute handover protocol / execute handover protocol / execute handover / handover protocol / run the handover / minor variants).
2. **Claude-initiated prompt discipline** on workflow-shape signals documented in §15 with signal list (substantive milestone just completed, long session duration, "we've done a lot today" / "good stopping point" utterances, Claude itself observing a natural seam, topic-shift cues). The signal list is distinguished explicitly from the §14 reflexive-drop signals (which fire for *individual organizational ideas*, not *whole-session shape changes*).
3. **Protocol promoted** from buried §10 subsection (under `### Commit cadence`) to top-level §15 "Session-close Handover Protocol" with TOC entry. The §10 subsection now carries a back-pointer to §15. The `### Intermediate registry-suite triggers` subsection in §10 was updated to reference the §15 location.
4. **Command vocabulary** explicitly enumerated in both §1 and §15.

**Additional gap closed during resolution:** the four-item checklist was extended to name `handover-[S]-[N].md` alongside `development-[S]-[N].md` in item 1, with explicit distinction of their roles (backward-looking record vs. forward-looking orientation document). This addressed the actual failure-mode language Thomas used at the originating session close. The `handover-[S]-[N].md` artifact had been implicitly required by the session-close workflow (one was authored for SS-8 in patch 0011) but was not codified anywhere as a checklist item, leaving its production dependent on memory rather than protocol.

**Closing commit reference:** patch 0013 in this session, immediately following SS-8 v1.0 patch 0012. Single sandbox commit modifies `templates/operating_system.md` (TOC + §1 cross-ref + §10 back-pointer + new §15 + footer update) and `Organizational_Frontier.md` (this entry's status change and relocation; §4 statistics update).

**History:**
- 24 Apr 2026 — Handover-protocol failure-mode diagnosed at session close; Thomas surfaced the gap after noticing development artifacts were not being generated; dual-trigger fix designed during session-close conversation. Registered as OPEN-ORG-008 during the handover-preservation patch itself (patch 0011).
- 24 Apr 2026 — RESOLVED via patch 0013 in the immediately following session. All four prescribed elements landed plus one additional gap closure (handover-[S]-[N].md codification).

---

## OPEN-ORG-007: Repository-level `.gitignore` for Python build artifacts

**Status:** RESOLVED — 24 April 2026 (patch 0016, this session immediately following OPEN-ORG-009 registration in patch 0015)
**Identified:** 24 April 2026, during SS-8 v0.2 session patch-staging
**Priority at resolution:** LOW (manual unstaging had handled the issue twice; .gitignore prevents recurrence)

**Originating context:** During patches 0006 and 0009, `series_strong/papers/__pycache__/` appeared in `git status` as an untracked directory because Python script execution during the session created bytecode caches. Both times, the pycache was manually unstaged with `git restore --staged` and deleted with `rm -rf` before the commit. A repo-level `.gitignore` would prevent the recurrence.

**Problem:** `__pycache__` directories appear whenever Python scripts are executed from the sandbox. Without a `.gitignore` entry, each occurrence required manual intervention. With ~5–10 dev sessions per month, this accumulated to a small but persistent friction item, and occasionally one such pycache could slip into a commit if the staging step was not carefully checked.

**Resolution as adopted (patch 0016):**

1. **Created `/.gitignore` at repo root** with the patterns specified in the original entry plus one minimal addition. Final content covers Python build artifacts (`__pycache__/`, `*.pyc`, `*.pyo`, `*.pyd`, `.Python`, `*.egg-info/`), Jupyter notebook checkpoints (`.ipynb_checkpoints/`), and OS/editor artifacts (`.DS_Store`, `Thumbs.db`, `desktop.ini`, `*.swp`, `*.swo`).
2. **Removed two tracked Windows artifacts** discovered during the .gitignore audit: `series_standard_model/papers/desktop.ini` and `series_strong/papers/desktop.ini` (Windows OS-generated, zero project content). The .gitignore was extended with one pattern (`desktop.ini`) beyond the originally registered set so these don't recreate on Thomas's local checkout.
3. **Registered OPEN-ORG-010** for separate handling of 11 tracked `.ipynb_checkpoints/` files (10 of them orphaned, in SM-8 territory) discovered during the same audit. Cleanup deferred because the orphan-status warrants Thomas-judgment about whether any contain unrecoverable work, and because SM-8 territory was outside the SS-5/6/7 migration session scope.

**Scope expansion disclosure:** the original entry's "Proposed fix" did not include `desktop.ini` in the OS/editor artifacts list; this was added during execution because the same patch removes existing tracked desktop.ini files and the ignore rule is the natural complement. The extension was minimal (one line) and tightly coupled to the cleanup work; documented here for traceability.

**Items not adopted:** LaTeX build artifacts (`.aux`, `.log`, `.out`, `.toc`, `.synctex.gz`, `.bbl`, `.blg`, `.fls`, `.fdb_latexmk`) were not added to the .gitignore. The repo currently has zero tracked LaTeX build artifacts, so prevention is not currently needed. If LaTeX pollution emerges in a future session, a one-line append to `.gitignore` adds them. Not registered as OPEN-ORG because it's preventive-only with no current symptom.

**Closing commit reference:** patch 0016 in this session, sandbox commit hash assigned at commit time.

**History:**
- 24 Apr 2026 — Registered during SS-8 v0.2 session after second manual unstaging of `__pycache__` during patch preparation.
- 24 Apr 2026 — RESOLVED via patch 0016 immediately after OPEN-ORG-009 registration. Adopted at start of SS-5/6/7 migration prep so subsequent migration commits would not stage build artifacts.

---

## OPEN-ORG-004: SS-5, SS-6, SS-7 migration to per-paper subfolder convention

**Status:** RESOLVED — 25 April 2026 (patch 0020 completes SS-7, the third and final paper)
**Identified:** 23 April 2026, during SS-8 v0.1 pre-drafting planning
**Priority at resolution:** LOW (existing papers were functional pre-migration; convention applies forward — completion eliminates structural asymmetry between pre-22-April papers and SS-8/future papers)

**Originating context:** Per-paper subfolder convention adopted 22 April 2026 (`operating_system.md` §11). SS-8 was the first paper drafted under the new convention, with `series_strong/papers/SS-8/` containing `sketches/`, `founders_voice/`, `reviews/`, `documentation_suite/`, `letters/`, `scripts/`. Earlier papers (SS-5, SS-6, SS-7) predated the convention and had their artifacts distributed across `series_strong/` at a different level of organization.

**Problem:** Inconsistent organization. A researcher navigating `series_strong/` saw SS-5/SS-6/SS-7 artifacts at one level of structure and SS-8 artifacts at another. When SS-9 or SS-10 were drafted, they would follow SS-8's pattern, widening the asymmetry.

**Resolution path:** Three sequential migrations executed across patches 0018 (SS-6), 0019 (SS-5), and 0020 (SS-7), in increasing order of complexity. SS-6 (3 files) was the warm-up; SS-5 (19 file moves including 8 archived versioned drafts) was the substantial-volume case; SS-7 (30 file moves including v1.1/v1.2 duplicate cleanup) was the most complex. All three migrations completed in a single dedicated session on 25 April 2026.

**Trigger override note (25 April 2026):** OPEN-ORG-004 was originally registered with an opportunistic trigger ("any session where a substantive edit to SS-5, SS-6, or SS-7 is planned anyway"). Thomas elected to execute the migration as a dedicated batch rather than wait for opportunistic triggers, after the doc-suite folder convention codification (patch 0015) and `.gitignore` baseline (patch 0016) made the work straightforward to batch. The opportunistic-trigger discipline remains the registered design intent for any future similar deferral; this batch was a one-time override with explicit Thomas approval.

**Migration summary by paper:**

- **SS-6 (patch 0018, commit shipped via Thomas's apply on 25 April 2026):** Three files migrated. `.tex` and `.pdf` to `series_strong/papers/SS-6/`, and one Claude-correspondence response file to `letters/`. Five empty subfolders with `.gitkeep`. New `SS-6-README.md` using `{scope}-README.md` convention. Cross-references updated in `INDEX.md` and `paper_catalog.md`; v0.1 → v0.2 version mismatch corrected during audit.
- **SS-5 (patch 0019, shipped via Thomas's apply on 25 April 2026):** Nineteen file moves. Eleven into the new `series_strong/papers/SS-5/` structure (canonical .tex/.pdf, 7 doc-suite files to `documentation_suite/`, `SS-5_development_transcript.md` renamed to `transcript-SS-5.md`, `SS-5_session_bootup_prompt.md` to `founders_voice/`); eight pre-§11-convention versioned drafts (`_v1`/`_v2`/`_v3`/`_v4`, .tex + .pdf each) archived to new `archive/SS-5_versioned_drafts/`. New `SS-5-README.md` and archive subfolder README created.
- **SS-7 (patch 0020, this entry's resolution):** Thirty file moves. Twenty-five into the new `series_strong/papers/SS-7/` structure (canonical v1.2 .tex/.pdf/.py from `series_strong/` root; 8 doc-suite files to `documentation_suite/`; 8 review-cycle letters to `letters/`; 2 sketches; 1 script; `SS-7_development_transcript.md` renamed to `transcript-SS-7.md`; `SS-7_v1.2_handover.md` renamed to `handover-SS-7.md`; `SS-7_v1.2_transcript.md` and `SS-7_OSF_registration_status.md` placed in `documentation_suite/` without rename). Five files archived to `archive/SS-7_versioned_drafts/`: the v1.1 stale paper trio (.tex/.pdf/.py) per Thomas's instruction during scoping, plus two transient v1.2-cycle artifacts (`SS-7_v1.2_apply_instructions.md`, `0003-SS-7-v1.2-partial-paper-body-notebook-PH.patch`). New `SS-7-README.md` and archive README created. INDEX.md and paper_catalog.md cross-references updated; INDEX.md was missing SS-7 entirely (catalog staleness finding), corrected during audit by adding the SS-7 row + including SS-7 in the pending-papers list.

**Cumulative migration totals:** 52 file moves across the three migrations, 3 new paper-folder READMEs, 2 new archive subfolder READMEs, 13 .gitkeep placeholders, ~18 cross-reference updates in `INDEX.md` and `paper_catalog.md`. Three pre-§11-convention naming-asymmetry issues resolved by rename during migration: `SS-5_development_transcript.md` → `transcript-SS-5.md`, `SS-7_development_transcript.md` → `transcript-SS-7.md`, `SS-7_v1.2_handover.md` → `handover-SS-7.md`.

**Naming inconsistencies preserved as audit findings (deferred):** `SS-7_v1.2_transcript.md` retains its version-suffixed name (sits in `documentation_suite/` next to `transcript-SS-7.md`); the two are non-overlapping in scope (broader v0.1→v1.1 narrative vs. v1.2-cycle-specific narrative). The version-suffix violates §11's no-version-suffix-in-filename rule for paper files but the rule does not strictly bind transcript files. Consolidation into a single transcript file or further renaming is left for a future session if desired; not a forcing concern.

**Closing commit reference:** patch 0020 in this session, commit `[hash assigned at commit time]`. SS-7 is the third and final paper in OPEN-ORG-004's scope.

**History:**
- 22 Apr 2026 — Per-paper subfolder convention adopted.
- 23 Apr 2026 — Thomas's ruling: "Let's take territory first" — defer migration until SS-8 v0.1 complete.
- 24 Apr 2026 — Registered here with explicit opportunistic trigger during OPEN-ORG inaugural population.
- 25 Apr 2026 — SS-6 migration completed (patch 0018, 3 files).
- 25 Apr 2026 — SS-5 migration completed (patch 0019, 19 files including 8 archive moves).
- 25 Apr 2026 — RESOLVED via patch 0020 with SS-7 migration (30 files including 5 archive moves; v1.1/v1.2 duplicate cleanup completed). All three papers in OPEN-ORG-004's scope are now under the per-paper subfolder convention; structural asymmetry between pre-22-April papers and SS-8/future papers eliminated.

---

# §4 — Statistics

**As of 25 April 2026 (after patch 0020 SS-7 migration; OPEN-ORG-004 RESOLVED):**
- Open: 6
- In-progress: 0
- Resolved: 3 (OPEN-ORG-004, OPEN-ORG-007, OPEN-ORG-008)
- Deferred indefinitely: 0

**By priority:**
- HIGH: 0
- MEDIUM: 2 (OPEN-ORG-003, OPEN-ORG-009)
- LOW: 5 (OPEN-ORG-001, -002, -005, -006, -010)

**By trigger type:**
- Between-paper: 1 (OPEN-ORG-001)
- Threshold-triggered: 1 (OPEN-ORG-002)
- Milestone-triggered: 1 (OPEN-ORG-003)
- Opportunistic: 3 (OPEN-ORG-005, -006, -010)
- Dedicated execution session: 1 (OPEN-ORG-009)
