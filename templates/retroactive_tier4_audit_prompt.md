# Retroactive Tier-4 Verbatim Reasoning Audit — Paste-Ready Prompt

**Purpose:** Paste-ready prompt for auditing prior context windows for verbatim Tier-4 reasoning preservation per `templates/operating_system.md` §4 Four-Tier Documentation Discipline. Distinct from §15 Session-close Handover Protocol audits (which produce summary artifacts but do NOT guarantee verbatim Tier-4 preservation).

**When to use:** When Thomas wants to verify that prior Opus windows preserved verbatim physics reasoning into `reasoning-<paper>.md` files rather than only landing conclusions in registries.

**Provenance:** Created 20 May 2026 (Patch 0481O) after the Session 135 retroactive-audit conversation that noted §15 handover completion does not imply §4 Four-Tier completion. The motivating concern: a window may answer "yes I executed handover protocol" while still having Tier-4 gaps because §15 audits registries and produces concentrated handovers, but does not walk substantive reasoning moves against the canonical Tier-4 file content.

**Companion documents:**
- `templates/operating_system.md` §4 (Four-Tier Documentation Discipline — the discipline being audited)
- `templates/operating_system.md` §15 (Session-close Handover Protocol — the protocol distinct from this audit)
- `templates/operating_system.md` §16 (SHIP Trigger Protocol — anti-collision strategy referenced by this prompt)
- `templates/paper_completion_checklist.md` (Phase 7A/7B/7C structure with anti-collision strategy and patch-number collision recovery)

---

## The prompt (copy from the line below through the closing horizontal rule)

---

# Retroactive Tier-4 Verbatim Reasoning Audit

Thomas is auditing prior context windows for verbatim Tier-4 reasoning preservation per `templates/operating_system.md` §4 Four-Tier Documentation Discipline. The motivating concern: the §15 Session-close Handover Protocol produces summary artifacts, but it does NOT guarantee that verbatim Tier-4 reasoning made it into `reasoning-<paper>.md` before compaction. Many windows may have closed cleanly per §15 while still leaving Tier-4 gaps.

This audit is distinct from §15. Don't conflate them.

## Pre-step (mandatory): read the files, don't trust your memory

Before answering anything, identify your session's primary scope (which paper / sector / OPEN-* trajectory) and read the relevant Tier-4 file in full:

- For flagship paper work: `flagship_papers/<paper>/documentation_suite/reasoning-<paper>.md`
- For series paper work: `series_<name>/companions/reasoning-<S>-<N>.md`
- For programme-level OPEN-* trajectory work without a paper venue yet: check whether a `reasoning-<OPEN-ID>.md` or equivalent exists; if not, this is itself a gap to register

Also read the relevant `development-<paper>.md` (Tier 3 vignettes) and `transcript-<paper>.md` (Tier 1 per-patch index) for comparison.

**Your compacted memory of "I preserved that reasoning" is unreliable.** Memory says you preserved it; the file is the only source of truth for what's actually there. Read the file first; answer second.

## Step 1: Classify this window's session type

- [ ] **Physics-discovery window** — substantive new theorem proofs, mechanism derivations, OPEN-* trajectory advancement, finding registration, decision-point recognition
- [ ] **Reviewer/polish window** — review-cycle work, polish revisions, formatting, citation cleanup, no new physics reasoning
- [ ] **SHIP-closeout window** — paper-completion-sequence work post-SHIP (registry updates, doc-suite refreshes, handovers)
- [ ] **Hybrid** — combination of the above; classify by dominant mode

If purely reviewer/polish OR purely SHIP-closeout with no new physics reasoning: skip to Step 6 (§15 handover audit only). The Tier-4 question doesn't apply.

## Step 2: Walk the substantive reasoning moves

For each substantive physics reasoning move made in this session (work attributed to this window across all of its sessions, not just the most recent), list:

1. **The decision point or recognition event** in one sentence (e.g., "Q5-PAIRING resolution at Layer 3 via Wigner-Eckart factorization on unique A_2 generator", "decision to refute the I_4 = H_4+ stabilizer claim", "vertex-aligned Reading C introduced as Layer 2 anchor")
2. **The patch number(s)** where it manifested in committed work
3. **Whether the *reasoning chain* (premises → derivation steps → conclusion) is captured, vs only the *conclusion* (the resulting theorem/finding/registry entry)**

Item (3) is the audit's load-bearing distinction. Registries record conclusions. Tier-4 files record the reasoning chain that produced them. "The theorem was registered" ≠ "the reasoning was preserved." If you only know the conclusion appears in a registry, that's not Tier-4 preservation.

## Step 3: Map each move to file location and check preservation

For each move from Step 2, fill in this table:

| Move | Patch | Should be in (file) | Actually preserved verbatim? | If yes: section/line citation |
|------|-------|---------------------|------------------------------|-------------------------------|
| 1    | …     | reasoning-<paper>.md §X | yes/no/wrong-file | … |

"Wrong-file" means: the content exists in the repo but in the wrong tier file (e.g., synthesis vignette in Tier-4 when it should be verbatim; or full reasoning chain in development.md when it belongs in reasoning.md).

Cite section headings or approximate line ranges from the files you actually read in the Pre-step. Don't guess.

## Step 4: Categorize each gap honestly

For each "no" or "wrong-file" entry from Step 3:

- **Recoverable verbatim** — the reasoning is still in your accessible context (visible above the compaction line, in this session's chat history). You can produce verbatim text from source.
- **Compaction-lost verbatim** — the reasoning was produced in this window's prior session(s) but is no longer in your accessible context. You can only produce a synthesis vignette, not verbatim text.
- **Wrong-file** — content exists but in wrong tier file; recovery is a migration patch.

The honest-labeling discipline matters here. **A synthesis vignette dressed up as verbatim reasoning is worse than an acknowledged gap.** If you can't produce verbatim from accessible source, say so; produce Tier-3 synthesis instead.

## Step 5: Produce recovery patches

For each gap from Step 4, draft a patch (commit it locally; do not just generate patch files speculatively):

- **Recoverable verbatim** → append to `reasoning-<paper>.md` as a new dated section header. Reproduce the reasoning chain in the language and texture of when the work was done. Date stamp = the original session date, not today's audit date.

- **Compaction-lost verbatim** → append to `development-<paper>.md` as a Tier-3 vignette. **Mark explicitly** with a header tag such as `[Tier 3 retrospective synthesis; verbatim reasoning lost to compaction in original session]`. The vignette captures what *was decided* and what *trajectory was followed*, not what the verbatim reasoning was.

- **Wrong-file** → produce a migration patch moving the content to the correct file, preserving original attribution and date stamps.

For each patch:

1. Anchor on **stable inline content** or **end-of-file H2 section appends**. AVOID prepending at "Last updated:" header tops if other Opus windows may be running this same audit concurrently (per §16 anti-collision strategy).

2. **Patch numbering**: confirm with Thomas before committing if uncertain. Default to alpha-suffix continuation of the most recent campaign sequence and confirm with Thomas. **Do not invent new patch numbers without confirming.**

3. Commit message must identify: (a) the file modified, (b) the original session/work that produced the content, (c) whether the captured content is **verbatim** or **synthesis** (use those exact words in the commit message — they are auditable signal).

## Step 6: §15 handover protocol confirmation (separate from Tier-4)

Independent of the Tier-4 audit above:

- [ ] Was the §15 Session-close Handover Protocol (8-step sequence Steps A–H) executed at this window's most recent session close?
- [ ] If yes, file path: `handovers/YYYY-MM-DD_session_NNN_<scope>.md`
- [ ] If no, this is a §15 failure separate from the Tier-4 question — note explicitly. Thomas will direct recovery.

## Output format — produce in this order

1. **Pre-step confirmation** — which files you read; one line per file
2. **Step 1 classification** with one-sentence rationale
3. **Step 2 enumeration** as a numbered list
4. **Step 3 mapping table** (the table above, filled in)
5. **Step 4 gap categorization** per move
6. **Step 5 patch deliverables** — committed patches with apply-and-push bash blocks per Thomas's standard delivery pattern (`cd ~/Documents/GitHub/CPP && git pull origin main && git am ~/Downloads/<patch>.patch && git push origin main`)
7. **Step 6 §15 confirmation** as a final paragraph

## Discipline reminders

- **Do not short-circuit Steps 1–4 by jumping to Step 5.** The walk through Steps 1–4 is what makes the audit useful. Patches without the walk are just "Claude wrote some content"; patches with the walk are auditable evidence that the gap was real.
- **Do not produce a Pattern-A reassurance answer** ("all reasoning is preserved, no gaps found") without showing the Step 3 mapping table with file citations. Reassurances without evidence get re-audited.
- **Verbatim means verbatim.** If you cannot produce verbatim from accessible source, the honest answer is Tier-3 synthesis with the synthesis label attached. Don't dress synthesis as verbatim to look complete.
- **One window's audit should not stomp on another window's audit.** If multiple windows are running this audit concurrently and producing patches against the same `reasoning-<paper>.md` file, anchor on end-of-file H2 section appends rather than mid-file inserts; Thomas can apply patches in any order without conflict.

---

## End of paste-ready prompt

---

## Audit campaign operational notes (for Thomas, not for the audited windows)

The notes below are for Thomas's planning and are NOT part of the prompt pasted into windows.

### Order of operations

Audit oldest-first (Window 50 before Window 100 before Window 130). If Window 100 built on Window 50's reasoning, you want Window 50's verbatim landing first so Window 100 can cite the proper anchor rather than reproducing a degraded copy.

### Filter audit list

Windows that did purely reviewer-cycle or polish work have no Tier-4 content to preserve — paste the prompt anyway but expect Step 1 to route to Step 6 immediately. Save attention for the physics-discovery windows: ones that closed major theorem registrations, opened OPEN-FI-C-9 trajectory work, did SF-2 Layer 4 EFT scoping, ran the Capotauro Reading C closure trajectory, etc.

### Three response patterns to watch for

- **Pattern A — Reassurance without evidence** ("all preserved, no gaps") with sparse Step 3 table → re-audit; the window is hand-waving.
- **Pattern B — Gaps found, patches produced** → the win condition; apply patches per usual workflow.
- **Pattern C — Gaps found, compaction-lost, Tier-3 synthesis only** → the honest answer when verbatim is genuinely gone. Accept Tier-3 with the synthesis label — better than reconstructed-pseudo-verbatim.

### Apply-time discipline

If many windows produce patches simultaneously, you'll get serial `git am` work. Consider applying in batches grouped by file (all `reasoning-SF-4.md` patches together, all `reasoning-capotauro.md` patches together) so cross-window collisions resolve in one sitting rather than one-patch-at-a-time.

### What this campaign reveals

- **If most windows report Pattern B**: the §4 Four-Tier Discipline mostly fires correctly; this audit is a one-time catch-up.
- **If most windows report Pattern C**: the discipline isn't firing reliably during sessions; consider a §4 amendment with a mid-session Tier-4 checkpoint (analogous to §16's mandatory immediate-execution rule for SHIPs).
- **If most windows report Pattern A**: re-audit those windows with sharper prompts asking for file citations. Pattern A frequency is also itself signal that windows under-value Tier-4 discipline and need a §4 reinforcement.

---

## Document history

- **20 May 2026 (Patch 0481O)**: Created in response to Thomas's retroactive-audit conversation in Session 135 follow-up. Codifies the audit prompt as a stable template artifact so future audits (or extensions of this campaign) can re-use it without re-deriving the prompt design. Patch numbering 0481O continues the Session 135 alpha-suffix sequence per §16's anti-collision discipline (point 7 patch-number collision recovery via alpha-suffix continuation) since forward-integer numbers 0482–0484 are claimed by concurrent windows.
