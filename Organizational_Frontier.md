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

## OPEN-ORG-004: SS-5, SS-6, SS-7 migration to per-paper subfolder convention

**Status:** OPEN — deferred to opportunistic trigger
**Identified:** 23 April 2026, during SS-8 v0.1 pre-drafting planning
**Priority:** LOW (existing papers functional; convention applies forward)

**Originating context:** Per-paper subfolder convention adopted 22 April 2026 (`operating_system.md` §11). SS-8 was the first paper drafted under the new convention, with `series_strong/papers/SS-8/` containing `sketches/`, `founders_voice/`, `reviews/`, `documentation_suite/`, `letters/`, `scripts/`. Earlier papers (SS-5, SS-6, SS-7) predate the convention and have their artifacts distributed across `series_strong/` at a different level of organization.

**Problem:** Inconsistent organization. A researcher navigating `series_strong/` sees SS-5/SS-6/SS-7 artifacts at one level of structure and SS-8 artifacts at another. When SS-9 or SS-10 is drafted, it will follow SS-8's pattern, widening the asymmetry.

**Proposed fix:** Migrate SS-5, SS-6, SS-7 to per-paper subfolder structure:
- Create `series_strong/papers/SS-5/`, `series_strong/papers/SS-6/`, `series_strong/papers/SS-7/` with the six standard subfolders each.
- `git mv` existing artifacts (sketches, reviews, transcripts, problem histories) from their current locations to the appropriate per-paper subfolders.
- Update any cross-references in `INDEX.md`, `paper_catalog.md`, README files, and the papers themselves (bibliography paths, figure paths).

Approximate effort: 2–3 hours (primary cost is the cross-reference audit and update, not the git mv itself).

**Trigger condition:** Any session where a substantive edit to SS-5, SS-6, or SS-7 is planned anyway (e.g., retroactive §4.1A/B addition per OPEN-ORG-005, or an SS-7 script refactor per OPEN-ORG-006). Migrate the paper being edited at that time, so the migration work piggybacks on work already happening. Three separate opportunistic triggers; migrate one paper at a time rather than all three at once.

**Blocking dependencies:** None.
**Blocks:** Completion of OPEN-ORG-005 and OPEN-ORG-006 for SS-5/6/7 specifically (those items can be done without migration, but combining them is more efficient per this item's trigger condition).

**History:**
- 22 Apr 2026 — Per-paper subfolder convention adopted.
- 23 Apr 2026 — Thomas's ruling: "Let's take territory first" — defer migration until SS-8 v0.1 complete.
- 24 Apr 2026 — Registered here with explicit opportunistic trigger during OPEN-ORG inaugural population.

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

## OPEN-ORG-007: Repository-level `.gitignore` for Python build artifacts

**Status:** OPEN — workable in next dev session
**Identified:** 24 April 2026, during SS-8 v0.2 session patch-staging
**Priority:** LOW (manual unstaging handled the issue twice, but will recur)

**Originating context:** During patches 0006 and 0009, `series_strong/papers/__pycache__/` appeared in `git status` as an untracked directory because Python script execution during the session created bytecode caches. Both times, the pycache was manually unstaged with `git restore --staged` and deleted with `rm -rf` before the commit. A repo-level `.gitignore` would prevent the recurrence.

**Problem:** `__pycache__` directories appear whenever Python scripts are executed from the sandbox. Without a `.gitignore` entry, each occurrence requires manual intervention. With ~5–10 dev sessions per month, this accumulates to a small but persistent friction item, and occasionally one such pycache may slip into a commit if the staging step is not carefully checked.

**Proposed fix:** Create repo-level `/.gitignore` with standard Python ignores:
```
# Python build artifacts
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.egg-info/

# Jupyter notebook checkpoints
.ipynb_checkpoints/

# OS / editor artifacts
.DS_Store
Thumbs.db
*.swp
*.swo
```

Approximate effort: 5 minutes.

**Trigger condition:** Next session where any Python development work happens AND the staging area is clean before the work begins. Essentially "do it at the start of the next dev session before touching anything else."

**Blocking dependencies:** None.
**Blocks:** Nothing. Current workflow handles the issue manually.

**History:**
- 24 Apr 2026 — Registered during SS-8 v0.2 session after second manual unstaging of `__pycache__` during patch preparation.

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

# §4 — Statistics

**As of 24 April 2026 (after patch 0013 OPEN-ORG-008 resolution):**
- Open: 7
- In-progress: 0
- Resolved: 1 (OPEN-ORG-008)
- Deferred indefinitely: 0

**By priority:**
- HIGH: 0
- MEDIUM: 1 (OPEN-ORG-003)
- LOW: 6 (OPEN-ORG-001, -002, -004, -005, -006, -007)

**By trigger type:**
- Between-paper: 1 (OPEN-ORG-001)
- Threshold-triggered: 1 (OPEN-ORG-002)
- Milestone-triggered: 1 (OPEN-ORG-003)
- Opportunistic: 3 (OPEN-ORG-004, -005, -006)
- Next-session: 1 (OPEN-ORG-007)
