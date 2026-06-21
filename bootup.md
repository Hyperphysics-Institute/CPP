# CPP Session Bootup Guide

**Location:** `/CPP/bootup.md`
**Purpose:** Load this file at the start of every new AI session working on CPP. It provides everything needed to continue productive work.
**Maintenance principle:** This file is infrastructure. It should rarely be updated — only when conventions, repository structure, or orientation protocols change. For current state (results, active problems, papers in progress), follow the pointers in §4 to the living tracking documents; do not rely on bootup for current state.

---

## How to Use This File

**Thomas says:** "Pull the CPP repo and read `bootup.md`"

**AI assistant does:**

**Programme-state staleness audit (adopted 11 May 2026, patch 0344):** This file (`bootup.md`) is *infrastructure* — patterns, conventions, repository structure — not *current state*. Current results, predictions, theorem counts, paper versions, axiom counts, and open-problem status drift over time and are not maintained here. The authoritative current-state pointers are in §§4, 5, 8, 9, 13, and 9.5 below; follow them rather than reading any current-state-looking numbers in this file as authoritative. Hard-coded numbers in this file may be from older programme states (e.g., the patch-number reference in §3 is a deliberately occasional update).

If you see a discrepancy between numbers / dates / status in this file and the live tracking documents, **trust the live tracking documents** (`paper_catalog.md`, `theorem-registry.md`, `predictions.md`, `research_frontier.md`, `master_glossary.md`, `axiom-registry.md`, `programme_orientation.md` Part VIII Predictions Scorecard) — they are updated per-paper and per-architecture event; this file is updated only when conventions, structure, or protocols change.


### Step 0 — BEFORE READING ANYTHING ELSE: clone the repo locally

Every file referenced in this guide lives in the CPP repo. Many Claude session environments have a fetcher with a URL whitelist that rejects `raw.githubusercontent.com` sub-paths even within domains the session has already touched — the bootup file itself can be fetched (because the user pasted that exact URL), but every subsequent file referenced inside the bootup will return a permissions error. The reliable access path is `git clone`, then read locally via view/bash. `github.com` is in the standard allowed-domains list for Claude container environments with a bash tool.

Run this first, in the container working directory (typically `/home/claude`):

    git clone https://github.com/Hyperphysics-Institute/CPP.git
    cd CPP
    git pull   # if the repo was cloned in an earlier turn

After cloning, every subsequent file referenced in this bootup (and in §9.5, and in every handover document) is read from the local clone using filesystem tools — NOT via web_fetch. URL patterns shown in this document and in §9.5 are reference paths; the actual reads happen against the cloned working tree.

If `git clone` fails (no bash tool, network restriction, github.com unreachable), STOP and tell Thomas — do not attempt to bootstrap by fetching individual `raw.githubusercontent` URLs. That path works for the bootup file itself and then fails opaquely on everything downstream.

### Step 1: Read these files IN ORDER (from the local clone)

| Priority | File | What it gives you | Time | Don't skip |
|----------|------|-------------------|------|-----------|
| 1 | `bootup.md` | THIS FILE — orientation, structure, conventions | 5 min | **§3** — patch generation and commit flow. If you generate `.patch` files this session, the canonical apply macro is in §3. Do NOT reconstruct from `conversation_search`. |
| 2 | `programme_orientation.md` | **THE THEORY** — complete narrative from first principles through all results | 15 min | — |
| 3 | `theory-overview.md` | Reference card — formulas, scorecard, key numbers | 5 min | — |
| 4 | `founders_vision.md` | Thomas's physical intuition — the WHY behind every equation | 10 min | — |
| 5 | `research_frontier.md` | **THE DASHBOARD** — every open problem, conjecture, and proposition with status and dependencies | 10 min | — |
| 6 | `theorem-registry.md` | What we've proved — all theorems by series with axiom dependencies | 5 min | — |
| 7 | `templates/operating_system.md` | Complete workflow manual — multi-AI review, transcripts, recovery | 10 min | §4 (Four-Tier Documentation Discipline) — required reading before producing reasoning/development/transcript artifacts. **§15 (Session-Close Handover Protocol)** — the canonical 8-step sequence Thomas invokes with "execute handover protocol" or equivalent. If Thomas asks for the handover at session-close, **execute Steps A–H exactly as specified**; do not improvise the sequence or substitute a chat summary for Step H's paste-ready handover document. |
| 8 | `templates/AI_team_expectations.md` | Team-level conventions, per-AI expectations, identified failure modes | 5 min | — |

**Also check `organizational_frontier.md` §1** for any open organizational items (`OPEN-ORG-NNN`) that may bear on the current session. Items registered there have been deferred awaiting their trigger condition; if you are at a natural pause point with capacity, scan whether any are workable.

**For sessions involving open problem work or repo restructuring**, also read:
- `templates/research_frontier_architecture.md` — the three-layer architecture (dashboard → problem histories → papers)

**For any session that will produce a physics/derivation patch**, also read:
- `templates/reasoning_capture_protocol.md` — the per-patch verbatim-reasoning + verify-script capture protocol, bound to the patch-presentation contract (§3). §9 carries the clone-first precondition and the line-1 BLOCKING handover-gate rule. (Registered Session 146 Patches 0608/0610.)

### Step 2: Check what happened last

- **The canonical handover lives in `handovers/` at the repo root.** Open the folder and read the most recent file — that's the current "what's next" pointer for the programme. The folder is the single, sortable index for all handover documents per the migration that landed 17 May 2026, Patch 0422 (`templates/operating_system.md` §15 "Handover file location and naming convention"). Filename pattern: `YYYY-MM-DD_session_NNN_<scope>.md`; `ls handovers/` shows chronological order with the most recent file last. If the most recent file is paper-scoped or trajectory-scoped and doesn't match the work to be done in the new session, look back at the previous most-recent file with matching scope. See `handovers/README.md` for the folder-level convention and migration history.
- **If Thomas names a specific paper (e.g., "SS-8", "SS-2", "SM-10")**, the most recent paper-scoped handover for that paper is found by `ls handovers/ | grep <paper-id-lowercase>` (e.g., `ls handovers/ | grep sf-2` returns the SF-2 campaign launch + SF-2 v1.0 SHIP handovers in chronological order). The handover is the **canonical session-continuity state record**, preserved verbatim at each session close per `templates/operating_system.md` §15. It supersedes any summary from training data or prior-session compaction. See §9.5 below for the full rule.
- Per-paper subfolders also contain `documentation_suite/development-[ID].md` (session vignettes, append-only) and optionally `documentation_suite/transcript-[ID].md` (transaction-indexed pointer-map). The handover in `handovers/` is the one to read first; `documentation_suite/` files are deeper context if needed.
- **Also read `todolist.md` at repo root** (introduced 7 May 2026 Session 33). This is the carried-over deferred items list. The next paper does NOT start until P1 — Must clear before next paper is empty. New items get added there as they're identified; cleared items move to "Cleared items (history)" with date and patch number for audit. Check the P1 list at session start so any deferred items relevant to the work being done are visible.
- If no paper is named, check `/mnt/transcripts/` for raw conversation logs.
- Check if Thomas has Grok/Copilot exchanges to share.

### Step 3: Proceed with the queued work

Unless Thomas redirects in his opening message, proceed with the next-session items listed at the end of the handover document read in Step 2. A handover whose final section is titled something like "Ready-to-execute work for next session" or "Next-session task list" is giving you the default action. Execute it. If the handover has no such list, or if Thomas's opening message gives a different direction, follow that instead.

If `todolist.md` P1 has items, the queued work in the handover may be the work to clear them, or the work to clear them may be next after the handover's queue. Defer to Thomas's opening message if there's any ambiguity.

### If resuming after buffer overflow:

Read the compacted summary at the top of the conversation, then the transcript file referenced there.

---

## 1. What CPP Is (30-second summary)

Conscious Point Physics derives the Standard Model from the geometry of the 600-cell polytope (V=120, E=720, F=1200, C=600, z=12). Conscious Points on the lattice exchange DI-bits via SSV gradients. All particles are geometric cage structures. All forces emerge from the lattice mode spectrum. The golden ratio φ = (1+√5)/2 appears throughout because it's built into the 600-cell geometry.

---

## 2. Repository Location and Access

**Step 0 of the bootup** is to run `git clone https://github.com/Hyperphysics-Institute/CPP.git` in the container working directory. If you have not yet cloned, stop reading this file and clone now — see the Step 0 block in the "How to Use This File" section above for rationale.

```
GitHub: https://github.com/Hyperphysics-Institute/CPP
Clone: git clone https://github.com/Hyperphysics-Institute/CPP.git
OSF:   https://osf.io/9dfya/
DOI:   10.17605/OSF.IO/JXE8D
Web:   https://hyperphysics.com
```

Always `git pull` before starting work. Thomas pushes frequently.

**For Claude-generated patches and Thomas's apply workflow**, see §3 below — the patch-generation and commit-flow section. If you are generating `.patch` files this session, read §3 in full before composing the apply macro.

---

## 3. Patch Generation and Commit Flow — READ FIRST IF GENERATING PATCHES

> **MANDATORY PATCH PRESENTATION CONTRACT.** Every `.patch` file Claude presents to Thomas via `present_files` MUST be immediately followed by an apply-and-push bash code block. Presenting a patch without the macro is an incomplete deliverable, not a stylistic choice. This rule is unconditional — it applies whether Thomas asks for the macro or not, whether the patch is large or small, whether the session has generated one patch or many. The canonical macro forms are given below ("The canonical apply macro — chained-with-fail-fast form" for multi-patch sessions; "Single-patch variant" for one-patch sessions). For multiple patches in one session: combine into one macro with sequential `git am` lines between the `git pull` and `git push`. If you (Claude) are about to call `present_files` on a `.patch` file, your next output block after that tool call MUST be the apply-and-push macro — no exceptions, no waiting to be asked. (Backstopped by user-memory entry registered Session 132 Patch 0436; this section is the in-repo authority for the deliverable contract.)
>
> **REASONING-CAPTURE RIDER (registered Session 146 Patch 0610; see `templates/reasoning_capture_protocol.md`).** Every *physics/derivation* patch bundles, in the SAME `git am`, the artifact PLUS a verbatim reasoning fragment (`<paper>/.../reasoning/<patch>.md` or the DSL `documentation_suite/reasoning-*.md`) AND a verify script (`<paper>/.../code/<patch>.py`) if any computation was done. This rider binds capture to the patch-presentation contract precisely because the contract is the one habit reliably honored unasked; an uncaptured physics patch is an incomplete deliverable, exactly like a patch presented without the apply macro. Pure-bookkeeping/organizational patches are exempt. At-patch capture is verbatim; later reconstruction carries a `STATUS: reconstructed` header.

> **If you (Claude) are about to produce `.patch` files for Thomas to apply, read this section in full BEFORE writing the apply macro you hand him. Do not reconstruct the macro from `conversation_search` or chat history. The canonical form below is battle-tested across ~165+ patches; any reconstruction is a near-miss risk that creates downstream rebase work for Thomas.**
>
> **Failure mode this section addresses:** Multiple consecutive Opus sessions have, on first attempt, searched prior conversations for the apply macro instead of reading this section. The result is 2–5 wasted exchanges per session burned on rediscovering documented procedure, plus occasional format-drift risk. If you notice yourself reaching for `conversation_search` to find the macro, STOP and re-read this section instead. (Registered as OPEN-ORG-013 in `organizational_frontier.md`; this section is its resolution.)

### Where Thomas works locally

When Claude generates files, patches, or document edits during a session, Thomas commits them from his local clone — NOT from the Claude container. The container is ephemeral; Thomas's local clone is the source of truth that gets pushed to GitHub.

**Standard local path (Thomas's machine):**

```
~/Documents/GitHub/CPP
```

### Standard commit flow for Claude-generated patches

Claude produces git mailbox-format patch files (numbered `00NN-description.patch`) using `git format-patch`, places them under `/mnt/user-data/outputs/patches/`, and presents them via the `present_files` tool so Thomas can download to `~/Downloads/`. Thomas then applies them via `git am`. This preserves authorship, timestamps, and commit messages exactly as Claude composed them.

### The canonical apply macro — chained-with-fail-fast form

For multi-patch sessions (this is the typical case — a session typically produces 4–10 patches), use the chained `&&` form so a failed `git am` aborts the chain before pushing partial state:

```bash
cd ~/Documents/GitHub/CPP && git pull origin main && \
  git am ~/Downloads/0NNN-first-patch.patch && \
  git am ~/Downloads/0NNN-second-patch.patch && \
  git am ~/Downloads/0NNN-third-patch.patch && \
  git push origin main
```

Three pieces in order:
1. **`cd ~/Documents/GitHub/CPP`** — switch to Thomas's local working clone (must always be the first step).
2. **`git pull origin main`** — cheap insurance; should be a no-op if Claude generated the patches against the current `main` HEAD, but catches the rare race where Thomas pushed unrelated work between Claude's last sync and patch generation.
3. **`git am ~/Downloads/0NNN-*.patch`** — one line per patch, in numerical order. Order matters because later patches frequently reference content added by earlier patches; out-of-order application causes `git am` to fail with hash-mismatch errors.
4. **`git push origin main`** — only fires if every preceding step succeeded (the `&&` chain short-circuits on the first failure).

If any `git am` fails, the chain stops there. Thomas can run `git am --abort` to revert the failed patch's partial state, then report the failure to Claude for diagnosis. **Do not push partial state under any circumstance.**

### Single-patch variant (organizational deliverables, etc.)

For a single-patch session:

```bash
cd ~/Documents/GitHub/CPP && git pull origin main && \
  git am ~/Downloads/0NNN-description.patch && \
  git push origin main
```

### Patch numbering convention

Continue from the highest existing patch number in the repo's commit history. Run `git log --oneline | head -20` in the in-container clone to verify the current highest number. Patches are numbered sequentially across all sessions; the numbering does not reset. (As of 11 May 2026 Session 81 close, the highest committed patch is 0344; check `git log --oneline | head -1` for the actual current.) **Sub-commits between patches**: the Binary Artifact Workflow (adopted Session 78, patch 0339; documented in `templates/operating_system.md` §13 Binary Artifact Workflow) produces non-numbered ClearPC-local PDF-recompile commits between numbered Claude patches — these are PDF-only commits that don't receive a patch number. When determining "highest committed patch", read the highest `Patch NNNN:` in commit messages, not the highest commit SHA.

### Generating the patch files in the container

After committing locally in `/home/claude/CPP`:

```bash
git format-patch -N HEAD~N..HEAD -o /tmp/p_outdir/
```

Then rename each file from `git format-patch`'s default `0001-`, `0002-`, ... numbering to the global sequence (e.g., `0167-`, `0168-`, ...) and move them under `/mnt/user-data/outputs/patches/`. Finally, surface them with the `present_files` tool so they appear in Thomas's download menu. **Patches that exist in the outputs folder but are not surfaced via `present_files` are invisible to Thomas — both steps are required.**

### Commit author convention

Claude's commits are authored as `Opus <opus@cpp.local>`:

```bash
GIT_AUTHOR_NAME="Opus" GIT_AUTHOR_EMAIL="opus@cpp.local" \
GIT_COMMITTER_NAME="Opus" GIT_COMMITTER_EMAIL="opus@cpp.local" \
git commit -m "..."
```

This keeps Claude-authored commits visually distinct from Thomas's own commits in `git log`.

### When `git am` flow is NOT appropriate

For trivial single-line edits Thomas wants to make himself, or for files Claude generates that don't need preserved authorship metadata, the simpler `git add` + `git commit` + `git push` flow can be used instead. Claude defaults to `git am` for any substantive deliverable (file additions, multi-line edits to existing files, anything with a meaningful commit message).

### When to use the in-container clone vs. Thomas's local clone

Claude reads files from the in-container clone at `/home/claude/CPP` (or wherever Step 0 placed it). Claude does NOT push to the in-container clone; the in-container clone is read-only from Thomas's perspective. All commits and pushes happen from Thomas's local clone at `~/Documents/GitHub/CPP` after the patches are downloaded and applied via `git am`.

After Thomas confirms a successful push, sync the in-container clone before continuing work in the same session:

```bash
cd /home/claude/CPP && git fetch origin main && git reset --hard origin/main
```

This ensures the in-container clone reflects the canonical state on GitHub.

---

## 3.5. Lightweight-Bootup Modes — for surgical registry-update sessions

> **MOTIVATION (registered 25 May 2026 Session 143 Patch 0573, after Thomas reported ~6 context restarts + 3 new windows during Phase 7B execution of F.1 v1.0 SHIP):** the full Step-1 priority read list (§Step 1 of this file) is the right protocol for physics work, paper development, and discovery sessions — but is **overkill for surgical registry-update sessions** (Phase 7B work after a flagship paper v1.0 SHIP). Quantified diagnostic: full priority read = ~7,000 lines bootup; plus the relevant paper's `.tex` + doc suite = another ~4,500 lines; plus all Phase 7B target registries = another ~6,000 lines; total ~17,500+ lines of context input before any substantive patch work begins, which exhausts the working budget for the substantive work itself. The mode below replaces the full priority read with a curated minimum (~1,000–2,500 lines) for sessions whose entire scope is one surgical registry edit. It does NOT replace the full priority read for physics, derivation, theorem-development, paper-drafting, or open-problem-exploration sessions — those still need the full Step 1 read.

### Phase-7B mode (post-SHIP programme-level registry updates)

**Use when:** the session's entire scope is updating ONE programme-level registry to reflect a recently-shipped flagship paper's v1.0 SHIP state, AND a Phase 7B content pack exists at `flagship_papers/<paper>/phase_7B_content_pack.md` for that paper.

**Minimal read list (replaces Step 1 for this session only):**

1. `bootup.md` §3 (patch contract) + this §3.5 (Phase-7B-mode directive) — ~100 lines
2. The most recent handover at `handovers/` for the relevant paper — typically 100–200 lines for routine handovers, longer for milestone-trajectory handovers
3. The paper's Phase 7B content pack: `flagship_papers/<paper>/phase_7B_content_pack.md` — typically 400–800 lines; contains pre-staged registry insertion blocks + anti-collision anchors + per-registry sanity checks
4. The ONE target registry being updated — varies 200–2000 lines
5. (Optional, only if anti-collision diagnostic needed) `templates/operating_system.md` §15 Step E + §16 anti-collision — grep-extract only, ~200 lines

**Total: ~1,000–2,500 lines.** Leaves comfortable headroom for substantive patch production.

**What to SKIP in Phase-7B mode (vs full Step 1):**

- `programme_orientation.md` — full read NOT needed; the content pack carries the F.1-specific orientation summary at its §0. Only re-read if writing the programme_orientation patch itself (Patch 0583 in F.1's case), and even then read only the sections being edited.
- `theory-overview.md` — NOT needed; surgical registry edits do not require theory-scorecard refresh in working memory.
- `founders_vision.md` — NOT needed for registry updates.
- `research_frontier.md` (1850 lines for F.1's case) — NOT a Step-1 read; only read when its update is the patch's target (Patch 0584 in F.1's case), and even then read only the anchor section being edited.
- `theorem-registry.md` (289 lines, with massive "Last updated" header) — same logic; read only when its update is the patch's target.
- `templates/AI_team_expectations.md` — NOT needed; reviewer protocol is implicit in the handover.
- The paper's `.tex` source — NOT needed; the content pack has pre-extracted all paper content. If a sanity check requires verifying a claim against the `.tex`, grep for the specific claim, do NOT read the full paper.
- The paper's documentation suite (mechanism/glossary/phenomena/philosophy/reviews/keywords companion files) — NOT needed; their content is pre-extracted into the content pack.

### Phase-7B mode session protocol (Steps 1–4)

1. **Bootup** — read the minimal list above (~5–10 minutes).
2. **Anti-collision audit** — read the content pack's "Anti-collision note" section for the target registry. Verify no concurrent session is editing the same target. If any other Opus window is active on the same registry, route around to a different target or coordinate at the user level.
3. **Patch production** — make ONE surgical `str_replace` on the target registry per the content pack's pre-staged block. Use the anti-collision anchors (grep-stable inline content) rather than line numbers. Commit. `git format-patch`.
4. **Session close** — flip the content pack's `Landing status: PENDING` to `Landing status: LANDED at Patch 05NN` in a small follow-up `str_replace` to the content pack itself, optionally bundled in the same patch or as a sub-patch (e.g., 05NNa). Update the next-session pointer in the handover or carry it forward.

### When NOT to use Phase-7B mode

- Physics work, derivation, theorem development → full Step 1 priority read.
- Open problem exploration, conjecture work → full Step 1 priority read.
- Paper drafting, reviewer-cycle response work → full Step 1 priority read.
- Repo housekeeping or restructuring → full Step 1 priority read + `templates/research_frontier_architecture.md`.
- Recovery / context-overflow recovery → full Step 1 priority read.

### Future variants (placeholder)

The lightweight-bootup-mode pattern templates similar modes for other recurring narrow-scope session types. Candidates registered as future work (not implemented at this patch):

- **Phase-7C mode** (OSF deposit + anthology chapter + H1–H5 verification): minimal read list anchored on the same content pack + `templates/anthology_chapter_template.md`.
- **Handover-only mode** (session-close handover production after a non-substantive session): minimal read list anchored on `templates/operating_system.md` §15 only + recent session log.
- **Single-companion-file mode** (one SHIP-time companion file production in Phase 7A): minimal read list anchored on `templates/documentation-suite.md` + relevant reference-implementation file.

These variants are not formally registered as open organizational items at this patch; they emerge if the corresponding session-type recurs with overflow symptoms.

---

## 4. Complete Repository Structure

```
CPP/
├── README.md                         ← Public-facing overview
├── INDEX.md                          ← Directory map
├── paper_catalog.md                  ← Paper list with IDs and status
│
├── ── THE THEORY ──
├── programme_orientation.md                 ← ** THE BOOK — complete theory narrative **
├── theory-overview.md                ← Reference card — formulas, scorecard
├── founders_vision.md                ← Thomas's physical intuition (the WHY)
├── axiom-registry.md                 ← Axiom tracking, prediction counts
├── master_glossary.md                ← All CPP terms, acronyms, particles, forces
├── predictions.md                    ← Every quantitative prediction with status
├── research_frontier.md              ← ** THE DASHBOARD — all open problems, conjectures, propositions **
├── theorem-registry.md               ← All proved theorems by series with axiom dependencies
├── nomenclature.md                   ← ID code legend (AXIM, THEO, PROP, FALS...)
├── future_projects.md                ← Prioritised research targets with status
│
├── ── WORKFLOW ──
├── operating_system.md               ← ** COMPLETE WORKFLOW MANUAL **
├── paper_production_workflow.md       ← 9-phase paper pipeline
│
├── templates/
│   ├── paper-formatting.md           ← LaTeX formatting standard
│   └── documentation-suite.md        ← 7-file companion template per paper
│
├── bibliography/
│   └── cpp_references.bib            ← BibTeX references for all papers
│
├── problem_histories/                ← Problem narratives — the drama of discovery
│   └── [PH-[ID].md files]
│
├── ── PAPER SERIES ──
├── series_standard_model/            ← SM-N papers (Standard Model, includes mass sector)
│   ├── papers/                       ← .tex, .pdf, .bib files
│   │   └── [PAPER-ID]/               ← per-paper subfolder (created early — see §4.5 below)
│   │       ├── reviews/              ← verbatim reviewer correspondence
│   │       ├── letters/              ← correspondence from Claude (synthesis, review requests)
│   │       ├── sketches/             ← derivation notes, findings, exploratory analyses
│   │       ├── scripts/              ← Python verification scripts
│   │       ├── founders_voice/       ← Thomas's recorded intuitions and organizational notes
│   │       └── documentation_suite/  ← four-tier documentation discipline (see §4.5)
│   │           ├── reasoning-[ID].md       ← Tier 4: verbatim Opus reasoning (canonical)
│   │           ├── development-[ID].md     ← Tier 3: curated paragraph-form vignettes
│   │           ├── transcript-[ID].md      ← Tier 2: transaction pointer-map
│   │           └── (seven companion files: mechanism/glossary/phenomena/
│   │                philosophy/keywords/reviews/FAQ — produced at Trigger 2)
│   ├── [type]-SM-N.md                ← 7 documentation suite files per paper (flat, for pre-subfolder papers)
│   ├── figures/figures-SM-N/         ← SVG + PDF figures
│   ├── notebooks/                    ← Verification notebooks
│   └── development-transcripts/      ← Curated conversation logs (legacy location)
│
├── series_electroweak/               ← EW-N papers
├── series_quantum_mechanics/         ← QM-N papers
├── series_relativity/                ← SR-N papers
├── series_strong/                    ← SS-N papers (Strong Sector)
├── series_foundations/               ← SD-N papers (foundations/superdeterminism)
│
└── archive/                          ← Superseded material
```

---

## 4.5 Four-Tier Documentation Discipline (per-paper subfolder convention)

When you produce work that will become or modify a paper, that work is preserved across **four tiers** of artifacts. The discipline is codified in `templates/operating_system.md` §4 "Four-Tier Documentation Discipline." Brief tour:

**Tier 1 — Per-session warm-start summaries.** Session logs in `session_logs/` (Template A or Template B) plus Thomas-verbatim insights in `series_<name>/papers/<ID>/founders_voice/`. Session-bounded, written for the next Opus's orientation.

**Tier 2 — Paper-level transaction pointer-map.** `series_<name>/papers/<ID>/documentation_suite/transcript-<ID>.md`. A numbered transaction log indexing every substantive transaction across the paper's full development arc. Each entry is a single line pointing to the artefact, vignette, or reasoning section that holds its substance. The transcript file is empty of substance; substance lives at the pointer targets. Append-only across sessions.

**Tier 3 — Curated paper-level vignettes.** `series_<name>/papers/<ID>/documentation_suite/development-<ID>.md`. Curated narrative vignettes summarizing each substantive transaction in finished prose (typically 1–3 paragraphs per vignette). Append-only across sessions; accumulates as the paper develops.

**Tier 4 — Verbatim Opus reasoning (the canonical record).** `series_<name>/papers/<ID>/documentation_suite/reasoning-<ID>.md`. Opus's substantive reasoning preserved verbatim across the full development arc, with housekeeping excluded but no summarization or compression of substantive content. **This is the canonical source from which all other tiers are derived.** Append-only at session close.

What goes in Tier 4 (and what is excluded as housekeeping):

- **Included:** multi-paragraph reasoning turns where Opus is doing analysis, testing a hypothesis, working through an argument, articulating a structural observation, considering alternatives, revising an earlier framing, flagging uncertainty, pushing back on a framing, or otherwise engaging in substantive theoretical or methodological work.
- **Excluded:** tool-call narration ("let me check"), status confirmations ("got it"), procedural housekeeping ("should I commit now"), tool-output narration, verbatim quotations from existing repository files (recoverable from sources).

**When the per-paper subfolder is created.** Early. As soon as in-progress work accumulates beyond a single session log — when there are two or more session logs, a working draft, a sketch, a founders_voice insight, or a registered open problem specific to the candidate paper, the subfolder is created with the four-tier `documentation_suite/` plus `founders_voice/`, `sketches/`, `scripts/`, `letters/`, `reviews/` (empty subfolders carry `.gitkeep` placeholders). Pre-paper subfolder creation is correct and encouraged; deferring to v1.0 forces retroactive curation that loses fidelity. SS-9 was the first paper created under early-subfolder discipline (26 April 2026 Session 3, ahead of any v0.x paper text).

**At Trigger 2 (genuinely-final shipped version, regardless of version label),** the seven companion documentation-suite files (mechanism/glossary/phenomena/philosophy/keywords/reviews/FAQ) are synthesized from the Tier 4 verbatim reasoning + Tier 3 curated vignettes, with Tier 1 session logs and Tier 2 pointer-map as supporting reference. The Tier 4 reasoning files remain alongside as the verbatim source after the synthesis.

**"v1.0" is not the operative trigger.** Trigger 2 fires when the paper is unambiguously done, whatever the version number happens to be. Defer if the version label is provisional; fire when the version is unambiguously final. The per-session Trigger 1 work (four-tier accumulation) captures everything session-window-bounded, so deferring Trigger 2 does not lose information.

See `templates/operating_system.md` §4 "Four-Tier Documentation Discipline" for the full codification.

---

## 5. All Key Files — What Each Does

### Theory documents (read for physics context)

| File | Purpose | Update when |
|------|---------|-------------|
| `programme_orientation.md` | The complete theory in connected prose — the "Kindle book" | Every session with new physics |
| `theory-overview.md` | Reference card: formulas, prediction scorecard, key numbers | After each paper |
| `founders_vision.md` | Thomas's physical intuition — 22+ catalogue entries | Every session with new physics |
| `axiom-registry.md` | All axioms, all predictions, growth tracking | After each paper |
| `master_glossary.md` | Every CPP term, acronym, particle, force, process | Scan during Phase 7 of paper production |
| `predictions.md` | Quantitative predictions with PDG comparison | After each paper |
| `research_frontier.md` | **The dashboard** — all open problems, conjectures, propositions with status and dependencies | After each paper |
| `theorem-registry.md` | All proved theorems by series, with axiom dependencies | After each paper |
| `future_projects.md` | 12+ prioritised research targets with status | After each session |
| `nomenclature.md` | ID code legend | Rarely |

### Workflow documents (read for procedures)

| File | Purpose | Update when |
|------|---------|-------------|
| `operating_system.md` | **THE COMPLETE WORKFLOW** — multi-AI review, transcripts, recovery, roles | When procedures change |
| `paper_production_workflow.md` | 9-phase pipeline from vision to OSF | When pipeline changes |
| `templates/paper-formatting.md` | LaTeX standard (16 sections) | When formatting changes |
| `templates/documentation-suite.md` | 7-file companion template per paper | When template changes |

### Navigation documents (read for orientation)

| File | Purpose | Update when |
|------|---------|-------------|
| `README.md` | Public landing page, paper table, key results | After each paper |
| `INDEX.md` | Complete file listing | After each paper |
| `paper_catalog.md` | All papers with ID, title, version, status | After each paper |
| `series_[name]/README.md` | Per-series overview | After each series paper |

### Reference folders

| Folder | Contents |
|--------|----------|
| `bibliography/` | `cpp_references.bib` — BibTeX for all cited works |
| `problem_histories/` | Narrative histories of major open problems — the drama of discovery |
| `templates/` | Paper formatting standard, documentation suite template, bootup, workflow |
| `archive/` | Superseded versions, old drafts, pre-frontier problem files |

---

## 6. The AI Team

| AI | Primary role | How Thomas communicates |
|----|-------------|------------------------|
| Claude Opus | Primary collaborator — computation, drafting, integration | Direct chat (claude.ai) |
| Grok (xAI) | Independent verifier, novel contributions | Pastebin links, raw GitHub URLs |
| Copilot (Microsoft) | Referee-grade review, framework building | Pastebin links, direct chat |
| ChatGPT (OpenAI) | Triage-pressure / verdict-honesty review | Pastebin links, direct chat |
| Gemini (Google) | Optional breadth review (confirmatory; use for a fourth read) | Prompted via Claude |

**Full details on roles, strengths, limitations:** See `operating_system.md` Section 12.
**The review cycle:** Opus → ChatGPT / Grok / Copilot (panel) → Opus. A hostile pass can be
requested from any panel member ("find every flaw"); there is no dedicated hostile reviewer
(Claude Sonnet 4.0 retired). Gemini optional for breadth. See `operating_system.md` Section 5.

---

## 7. Session Types

| Type | Goal | Key procedure |
|------|------|---------------|
| Physics Discovery | Explore, compute, derive | Capture Thomas's intuition FIRST. Papers can emerge unexpectedly. |
| Paper Production | Draft and finalise a paper | Follow 9-phase pipeline. Use multi-AI review cycle. |
| Housekeeping | Audit and fix repo | Check INDEX.md against actual files. Update stale docs. |
| Transcript Curation | Convert raw history to curated records | Read `/mnt/transcripts/`, produce `[Paper]_transcript_[N]_[AI].md` |

**Full protocol for each type:** See `operating_system.md` Section 3.

---

## 8. Current Results

For current headline results, strongest predictions, and scorecard, read:

- **`README.md`** — public-facing results table (updated each paper)
- **`predictions.md`** — every quantitative prediction with PDG comparison and status
- **`theory-overview.md`** — reference card (formulas, scorecard, key numbers)

Do not rely on bootup for current result values. Results drift between papers; the authoritative sources drift with them.

---

## 9. Current Active Open Problems

For the live dashboard of open problems, conjectures, and propositions with status and dependencies:

- **`research_frontier.md`** — the canonical dashboard for all open problems across series
- **`future_projects.md`** — prioritised research targets
- **`problem_histories/`** — narrative histories of major open problems

Do not rely on bootup for the open-problem list. Active problems are created, resolved, and consolidated frequently; `research_frontier.md` is the single source of truth.

---

## 9.5 Active Work Pointer — read the paper's handover document first

**When Thomas names a specific paper at session start (e.g., "SS-8", "SM-10", "EW-3"), read that paper's session-handover document from your local clone as the first concrete action, BEFORE attempting any substantive work. (Per Step 0 you should already have a local clone — if not, clone now.)**

### Path pattern (repo-relative, read with view/bash from the local clone)

Single canonical pattern, in effect since 17 May 2026 (Patch 0422):

```
handovers/YYYY-MM-DD_session_NNN_<scope>.md
```

All handover documents live in `handovers/` at the repo root, regardless of paper or scope. `<scope>` is a short snake_case descriptor such as `programme`, `capotauro_v1.0_ship`, `reading_c_closure_trajectory`, `sf2_v1.0_ship`. Paper IDs in scope use lowercase with hyphens (`ss-9`, not `SS-9`). The `YYYY-MM-DD` prefix sorts chronologically when listed; the most recent file is the current handover. See `handovers/README.md` for the folder-level convention and the migration correspondence table mapping pre-Patch-0422 locations to their new canonical paths.

**Discoverability rule.** At new-session bootup, list `handovers/` and read the most recent file. If the most recent file is paper-scoped or trajectory-scoped and doesn't match the work to be done, look back at the previous most-recent file with matching scope. To find a paper-scoped handover quickly: `ls handovers/ | grep <paper-id-lowercase>` returns all handovers for that paper in chronological order.

**Pre-Patch-0422 legacy locations.** Before 17 May 2026, handovers were scattered across four patterns: per-paper `<series>/papers/<PAPER-ID>/documentation_suite/handover-<PAPER-ID>.md`, root-level `SESSION_NN_HANDOVER_FOR_NEXT_CONTEXT.md`, per-trajectory `flagship_papers/<paper>/sketches/<trajectory>_handover.md`, per-problem `session_logs/OPEN-<X>_handover.md`. All migrated to `handovers/` with date-prefixed naming via `git mv` per Patch 0422; the migration was pure-mechanical, no content changed. Active sketches and session logs written before the migration may still contain references to the old paths — see `handovers/README.md` for the correspondence table.

### Equivalent raw URLs (reference only — for documentation, citation, and external readers)

The same files served via raw GitHub. **Do not use these as the access path inside a Claude session; the fetcher whitelist will reject them after the bootup file itself.** Use the local clone.

```
https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/handovers/YYYY-MM-DD_session_NNN_<scope>.md
```

### Why this matters

The handover document is the **canonical session-continuity state record** — produced and committed at each session close per `operating_system.md` §15 Step H. It names:
- What paper or trajectory is active and what state it is in
- What section-end or milestone was most recently closed
- What open items are queued for next session (with priority ordering)
- What registry updates are pending ratification
- Pointers to verbatim artefacts (reviews, letters, sketches, scripts) that hold the substantive content

There are two scales of handover by triggering event: routine session-close (~80–120 lines, the paste-ready concentrated form) and milestone-trajectory (typically 300–1500 lines for v1.0 SHIP, archival-deposit-quality, or multi-session closure arcs; carries enough verbatim content for downstream paper-completion work — doc suite, registers, book chapters — to proceed without re-deriving context). Both scales live at the same canonical `handovers/` location. See `templates/operating_system.md` §15 Step H for the full specification.

For retrospective narrative of how the paper arrived at current state, the per-paper-subfolder convention provides the four-tier documentation discipline (see §4.5): `documentation_suite/development-[ID].md` (Tier 3 — curated paragraph-form vignettes), `documentation_suite/transcript-[ID].md` (Tier 2 — transaction-indexed pointer-map), and `documentation_suite/reasoning-[ID].md` (Tier 4 — verbatim Opus reasoning, the canonical record from which the other tiers derive). Handover files no longer live in `documentation_suite/`; they live in `handovers/` per Patch 0422.

**Compaction summaries and training data do NOT preserve these specifics.** Numerical results get rounded, decision rationales get compressed, and registry statuses get flattened. If you start substantive work from a compaction summary without reading the handover, you will either (a) ask Thomas to re-explain state he already documented, or (b) guess wrong about the current conditional-theorem tiers, consolidated open problems, or reviewer positions.

### If no handover document exists yet for the named paper

Some papers haven't reached the handover-document stage yet. If `ls handovers/ | grep <paper-id-lowercase>` returns nothing, fall back to:
1. The paper's `.tex` file and its `documentation_suite/changelog-<paper>.md` (per the version-archaeology architecture rule in `operating_system.md`).
2. `research_frontier.md` for related open problems.
3. Ask Thomas directly: "I don't see a handover document for this paper in `handovers/` — can you point me to where the current state lives?"

**Do not improvise state from training data.** A paper named but without a handover document is a signal that either the paper is very early or the document hasn't been created yet — both cases warrant asking rather than guessing.

### Maintenance rule for handover documents

Update the transcript at each section-end commit and at every context-pressure crossing (per `operating_system.md`'s context-pressure preservation checklist). Curate directly from the active session — do NOT regenerate from a session summary, which is lossy by design.

---

## 10. What to Update After Every Paper

**TRIGGER:** Run this checklist after completing the documentation suite (Phase 7), BEFORE pushing to GitHub.

**Authoritative atomic checklist:** `templates/paper_completion_checklist.md`. Run that file end-to-end; the table below is an abbreviated quick-reference covering only content and navigation updates. The full checklist additionally covers companion documentation suite (Section A), verification notebooks (B), development transcripts (E), OSF registration (F), git commit/push (G), and final verification (H). Per-file reference procedures live in `operating_system.md` §10.

| Document | What to update |
|----------|----------------|
| `programme_orientation.md` | Add results to chapter, update scorecard |
| `theory-overview.md` | Add results, update formula card |
| `axiom-registry.md` | Check axioms, add predictions, update ratio |
| `theorem-registry.md` | Add new theorems with axiom dependencies; update theorem count |
| `research_frontier.md` | Update status of problems addressed; move resolved items to §5; add new problems |
| `master_glossary.md` | Scan paper for new terms, add in alphabetical order |
| `founders_vision.md` | Add new physical intuitions from this session |
| `predictions.md` | Add new predictions with PDG comparison |
| `future_projects.md` | Mark completed, add new targets, re-prioritise |
| `problem_histories/` | Update history files for any problems touched this session |
| `README.md` | Add paper to table, update counts |
| `INDEX.md` | Add all new files |
| `paper_catalog.md` | Add paper entry |
| `series_[name]/README.md` | Add to series |
| `bibliography/cpp_references.bib` | Add BibTeX entry for new paper |

### Post-Session Quick Checklist (for discovery sessions that don't produce a full paper)

- Update `founders_vision.md` with any new physical insights
- Create/update development transcript
- Update `future_projects.md` if priorities changed
- Note any new open problems in `research_frontier.md`; update `problem_histories/` if significant work done
- Push to GitHub

---

## 11. The Documentation Suite (7 files per paper)

Every completed paper gets 7 companion `.md` files stored in `series_[name]/`:

| File | Purpose | Content |
|------|---------|---------|
| `mechanism-[S]-[N].md` | How the physics works | Step-by-step mechanism, mathematical correspondence table |
| `glossary-[S]-[N].md` | Paper-specific terms | All new terms with definitions, organised by category |
| `phenomena-[S]-[N].md` | What the paper explains | PHEN-E (empirical), PHEN-P (predictions), PHEN-V (consilience) |
| `philosophy-[S]-[N].md` | Epistemological framing | What level of certainty, relationship to SM, falsifiability |
| `development-[S]-[N].md` | Development history | Version timeline, key decisions, dead ends, transcript links |
| `reviews-[S]-[N].md` | All reviews + FAQ | Part 1: formal reviews (ChatGPT/Grok/Copilot; Gemini optional). Part 2: FAQ |
| `keywords-[S]-[N].md` | Keywords and registry | Primary/secondary keywords, cross-references, axiom/theorem entries |

Each file should note the paper version it documents (e.g., "Paper: SM-8 v4.1").

---

## 12. Conventions

**Paper IDs:** `[SERIES]-[NUMBER]` (SM-8, EW-3, QM-1, SR-1, SS-1, SD-5). Paper numbers are assigned sequentially within a series as new papers enter the repository.
**Filenames:** `SM-8_quark_generation_600cell_shells.tex` — lowercase slug, no version number in filename
**Versions:** `vX.Y` shown in the .tex `\title{}` block (rendered on PDF title page); version archaeology lives in `documentation_suite/changelog-<paper>.md` (per version-archaeology architecture rule, `operating_system.md`). ONE .tex file per paper, overwritten — Git history preserves all versions. Never create `_v1`, `_v2` copies.
**Codes:** AXIM (axiom), THEO (theorem), CORO (corollary), CONJ (conjecture), OPEN (open problem), FALS (falsified). See `nomenclature.md`.
**LaTeX:** Follow `templates/paper-formatting.md`
**Axiom numbering:** When two reviewers independently propose axiom entries (e.g., Grok proposes A9', Copilot proposes A8'), reconcile into one entry when updating `axiom-registry.md`. The registry is the single source of truth for axiom IDs.
**Problem numbering is independent of paper numbering.** A problem is registered once with a fixed number (e.g., OPEN-SS-5) and retains that number as it progresses through the registry: OPEN-SS-5 → CONJ-SS-5 → (eventually) THEO-SS-5, or OPEN-SS-5 → FALS-SS-5 on falsification. Papers that address a problem carry their own independent sequential paper number. Example: the paper SS-4 (fourth paper in the Strong Sector series) may register the conjecture CONJ-SS-5, which originated as problem OPEN-SS-5. This retention rule is documented in `templates/nomenclature.md` §OPEN.

---

## 13. Papers in the Programme

For the current paper list with IDs, titles, versions, and OSF status:

- **`paper_catalog.md`** — master catalog across all series
- **`README.md`** — public paper table
- **`series_[name]/README.md`** — per-series overview

Series codes: SM (Standard Model), SS (Strong Sector), EW (Electroweak), QM (Quantum Mechanics), SR (Relativity), SD (Foundations/Superdeterminism). See §12 for naming conventions.

Do not rely on bootup for paper counts or versions; `paper_catalog.md` is the single source of truth.

---

## 14. OSF Registration

1. Prepare PDF + .tex + .bib + figures
2. Write metadata (title, abstract, keywords, dependencies, version)
3. Upload to OSF component under CPP project
4. OSF auto-assigns DOI
5. Update `paper_catalog.md` and `README.md`

---

*This file is self-sufficient. A new AI reading ONLY this file knows: what CPP is, where everything lives, what to read next, who the team is, what the results are, and what to do. For the full workflow manual, read `operating_system.md`. For the complete theory, read `programme_orientation.md`.*
