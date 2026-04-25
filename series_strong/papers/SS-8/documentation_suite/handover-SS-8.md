# SS-8 Handover Document

**File:** `handover-SS-8.md`
**Paper:** SS-8 — Interstitial-neutron binding in alpha-cluster nuclei: the 2E/V scaling law from simplicial polytope geometry
**Status:** v1.0 committed and pushed (origin `0a98d80`); first publishable version; Round 1 + Round 2 AI reviews integrated; data infrastructure for reproducibility added via patch 0017
**Role:** Session-continuity state snapshot for the next Claude context window. Bounded (kept short). Replaced (not appended to) at each session close per §15 handover protocol.
**Related files:**
- `transcript-SS-8.md` — transaction-indexed pointer-map, currently at transaction 066 (appended this session)
- `development-SS-8.md` — session vignettes (11 vignettes total; vignette 11 added this session)

**Maintenance rule:** Update at each session close per `templates/operating_system.md` §15 "Session-close Handover Protocol" four-item checklist. Handover triggered by Thomas saying "execute handover protocol" or by Claude-initiated prompt when workflow-shape signals fire.

---

## One-minute orientation for the next Claude

The 25 April 2026 session was substantially programme-wide governance and migration work, not paper-scoped physics. Six patches landed (0015–0020), executing the SS-5/6/7 per-paper-subfolder migration that OPEN-ORG-004 had registered as opportunistic-trigger-deferred work. With this session's completion, **OPEN-ORG-004 is RESOLVED** and the Strong Sector now has uniform per-paper subfolder structure for SS-5, SS-6, SS-7, SS-8. Future SS-9, SS-10 inherit this from SS-8. The structural asymmetry between pre-22-April papers and SS-8/future papers is eliminated.

**Lost-patch recovery resolved this session.** Patch 0009 (AME 2020 data dependency + `{scope}-README.md` convention codification) had been generated in the prior session but never landed on origin/main due to drag-drop misfiling — `series_strong/data/data-README.md` was referenced from SS-8 v1.0 (in CHANGELOG, Appendix B) but the directory it pointed at didn't exist. Caught during patch 0016's audit; recovered against current origin/main as patch 0017. SS-8 v1.0's reproducibility references now resolve correctly. The original patch 0009 file remains in Thomas's Downloads as a historical artifact; do not attempt to apply it (stale parent commit; conflicts likely).

**Two new OPEN-ORG entries registered this session:**
- **OPEN-ORG-009** (MEDIUM) — bootup-orientation-completeness audit. Same root-cause class as OPEN-ORG-008: documented protocols not firing reliably due to visibility/active-working-set issues. Dedicated execution session.
- **OPEN-ORG-010** (LOW) — 11 tracked `.ipynb_checkpoints` files (10 orphaned, in SM-8 territory). Cleanup deferred for Thomas-judgment about whether any contain unrecoverable work.

**Two OPEN-ORG entries RESOLVED this session:**
- **OPEN-ORG-004** — SS-5/6/7 per-paper-subfolder migration (patches 0018, 0019, 0020).
- **OPEN-ORG-007** — repository-level `.gitignore` (patch 0016).

The §15 Session-close Handover Protocol fired for the second time at the end of this session (first firing was at the end of the prior session, captured in vignette 10). This handover replacement, the development-SS-8.md vignette 11, and the transcript-SS-8.md transactions 060–066 are the artifacts produced.

The Strong Sector programme remains in a between-paper state. Three programmatic decisions remain in force:
- **PD-001** — CP/GP Signature (§4.1A) and Swarm-Validation Contribution (§4.1B) required subsections in every paper.
- **PD-002** — Three-tier verification taxonomy for reviewer numerical claims; first empirical firing observed in vignette 10's session.
- **PD-003** — Organizational Frontier Registry for reflexive-drop capture of organizational improvement items.

The Organizational Frontier registry at `/CPP/Organizational_Frontier.md` has 6 open and 3 resolved entries. Scan it against current state at session start.

---

## Current state

### Paper
- SS-8 v1.0 committed and pushed (origin `0a98d80`).
- 1183 lines (was 1182 at end of prior session; +1 from patch 0017's Appendix B reproducibility paragraph and surrounding whitespace).
- Three theorems, 42 zero-parameter predictions. Conditional on C1–C4 (inherited from SS-7) and D1–D3 (D1 at conditional-theorem tier).
- All Round 1 + Round 2 AI-review polishing items inside PD-001 scope are integrated. Curriculum-phase deepening of §§5/6 deferred per PD-001 (no priority).
- Appendix B Data Sources now contains a reproducibility paragraph pointing readers at `series_strong/data/data-README.md` for AME 2020 download instructions (added in patch 0017).
- Known placeholder unchanged: Table 4 (N_ex > 2 residuals) caption flags regeneration as post-v1.0 Thomas-side task; data infrastructure now actually exists at `series_strong/data/`.

### Repository structure (changed substantially this session)
- **Strong Sector papers** all live in per-paper subfolders: `series_strong/papers/SS-5/`, `SS-6/`, `SS-7/`, `SS-8/`. Each has the six standard subfolders (documentation_suite, founders_voice, letters, reviews, scripts, sketches), populated as appropriate.
- **`{scope}-README.md` convention** codified in `templates/operating_system.md` §11 (patch 0017). New READMEs use this convention; legacy READMEs (e.g., `README.md` in SS-8, `series_strong_README.md` with underscore) are candidates for retroactive normalization under OPEN-ORG-001.
- **`documentation_suite/` folder location** codified in `templates/documentation-suite.md` (patch 0015) for both the 7-file canonical doc-suite and the 2-file lab-notebook trio additions (handover, transcript). Up to 10 file types per paper folder.
- **AME 2020 data infrastructure** at `series_strong/data/` with `data-README.md` as single source of truth for external-data provenance (patch 0017). Loader at `series_strong/papers/ame2020_loader.py` defaults to repo-relative path with informative `FileNotFoundError` pointing at the README.
- **Repo-level `.gitignore`** at `/.gitignore` covering Python build artifacts, Jupyter checkpoints, OS/editor artifacts including `desktop.ini` (patch 0016).
- **Three filename normalizations** during migration: `SS-5_development_transcript.md` → `transcript-SS-5.md`; `SS-7_development_transcript.md` → `transcript-SS-7.md`; `SS-7_v1.2_handover.md` → `handover-SS-7.md`. All match the SS-8 lab-notebook-trio convention `[type]-[S]-[N].md`.

### Operating system (changed this session)
- §11 — new "README files — `{scope}-README.md` convention" subsection between filename rules and version management (via patch 0017 / lost-patch recovery).
- No other operating-system changes this session beyond what was codified in patches 0015 and 0017.

### Registry (Research_Frontier.md, Strong Sector — unchanged this session)
- **OPEN-SS-23** — inherited from SS-7; partially addressed by SS-8 (on-chain N_ex ≤ 8 covered).
- **OPEN-SS-24** — inherited; unchanged.
- **OPEN-SS-26** — partially resolved (Level 1/2 conditional theorem for D1 delivered); Level 3 remains open.
- **OPEN-SS-27** — opened in v0.1; expanded scope.
- **OPEN-SS-28** — opened in v0.1 (D3 bulk-regime averaging + residual decomposition).

### Organizational Frontier (changed substantially this session)
- 6 open, 3 resolved.
- Resolved this session: OPEN-ORG-004 (SS-5/6/7 migration via patches 0018/0019/0020), OPEN-ORG-007 (.gitignore via patch 0016).
- Registered this session: OPEN-ORG-009 (bootup orientation audit, MEDIUM), OPEN-ORG-010 (.ipynb_checkpoints cleanup, LOW).
- Required-before-SS-9: OPEN-ORG-003 (`predictions.md` swarm-tally header).
- Dedicated-execution-session item: OPEN-ORG-009 (bootup audit, 30–60 min).

---

## Ready-to-execute work for next session

**Priority order** based on attention-payoff for programme advancement:

1. **Scan `Organizational_Frontier.md` against current state** (60 seconds). 6 open entries. Start-of-session discipline per PD-003.

2. **OPEN-ORG-003 execution** — required **before SS-9 drafting can properly produce §4.1B**. If SS-9 is the next paper, sequence is: OPEN-ORG-003 first (swarm-tally header in `predictions.md`), then SS-9 draft.

3. **SS-9 planning and drafting.** Natural target paper for OPEN-SS-28 closure (first-principles derivation of D3 uniform averaging plus residual decomposition into H3'/H4'/H5'). Would supersede the provisional H3' transport in SS-8 §3.5 with a derived-tier mechanism. Other plausible SS-9 targets: dripline-asymptotic regime (extends OPEN-SS-23), off-chain-cores extension (full OPEN-SS-23 closure).

4. **Table 4 regeneration** (Thomas-side; requires local AME 2020 data per `series_strong/data/data-README.md`). Independent of SS-9 sequencing. Data infrastructure now fully in place; this is purely a download-place-run sequence Thomas can execute when convenient.

5. **OPEN-ORG-009** — bootup orientation completeness audit. Dedicated 30–60 min session. Best executed when no paper-drafting is in flight.

6. **OPEN-ORG-010** — `.ipynb_checkpoints` cleanup in SM-8 territory. Requires Thomas-judgment on 10 orphan checkpoint files before any `git rm`. Opportunistic; could combine with any SM-8 work.

7. **Round 3 SS-8 review** — not currently planned. v1.0 is the publishable baseline; further reviewer engagement on SS-8 is contingent on Thomas choosing to circulate it externally.

---

## Context the next session may want to revisit

- **Catalog-staleness pattern.** Two staleness findings caught during this session's audit work: SS-6 was at v0.2 in the .tex header but listed as v0.1 in INDEX.md and paper_catalog.md (corrected in patch 0018); SS-7 was missing from INDEX.md entirely — no row in the paper table, not in the pending-papers list (corrected in patch 0020). The pattern: catalog files drift behind reality when paper updates happen but the catalog edit step is skipped. Worth a future audit pass to check SS-1 through SS-4 entries against actual file state. Not registered as OPEN-ORG (size unclear; could fit OPEN-ORG-001 README normalization scope or could be its own item).

- **Stale references to non-existent files.** `paper_catalog.md` previously claimed three reviewer verification responses for SS-7 v1.2 were archived at `series_strong/papers/SS-7_v1.2_*_verification_response.md`. Those files do not exist as standalone artifacts — the verification *letter* is preserved at `letters/SS-7_v1.2_reviewer_verification_letter.md`, but the responses themselves were received in chat and never persisted. Catalog updated to reflect actual state; if these reviewer responses are valuable for audit, they could be reconstructed from chat history into letters/ in a future session.

- **Naming asymmetry preserved.** `series_strong/papers/SS-7/documentation_suite/SS-7_v1.2_transcript.md` retains its version-suffixed name alongside `transcript-SS-7.md`. The two are non-overlapping in scope (broader v0.1→v1.1 narrative vs. v1.2-cycle-specific narrative covering symmetric-honesty retirement). Consolidation into a single transcript file with section dividers is possible but not pressing; deferred to preserve git history cleanly.

- **PD-002 first-firing observation** (carried forward from prior handover). Grok's Round 2 Verification Tier Statement is on the empirical record. Worth checking whether Copilot and ChatGPT adopt similar three-tier framing in their next reviews.

- **§15 second-firing observation.** The protocol fired a second time this session-close. This was on Thomas's explicit "execute handover protocol" command rather than Claude's proactive prompt — the user-initiated trigger. Both firings have now been validated. Watch for the §14-vs-§15 boundary failure mode noted in vignette 10.

- **Curriculum-phase deepening** of SS-8 §§5 and §6 remains deferred per PD-001. No priority. If SS-8 is later circulated externally to a non-CPP audience, this becomes higher-priority.

---

## Commits from this session (25 April 2026)

Session produced six commits across governance infrastructure and the SS-5/6/7 migration arc, plus this handover:

- `1f46db5` — OPEN-ORG-009 registered + documentation_suite folder location codified (patch 0015)
- `61e5f97` — OPEN-ORG-007 RESOLVED, repo-level `.gitignore` + desktop.ini cleanup, OPEN-ORG-010 registered (patch 0016)
- `0b69687` — AME 2020 data dependency (recovered from lost patch 0009) (patch 0017)
- `416d60d` — SS-6 migration to per-paper subfolder (patch 0018)
- `82bbc91` — SS-5 migration to per-paper subfolder (patch 0019)
- `f335b03` — SS-7 migration; OPEN-ORG-004 RESOLVED (patch 0020)
- **[this patch 0021 — handover preservation; commit hash assigned at commit time]**

All commits on `origin/main`.

---

## How to use this file

**If you are the next Claude reading this:** You have 30 seconds of orienting text above and 5 minutes of detail below it. For deeper context, read `development-SS-8.md` vignette 11 (the most recent session's reasoning that wasn't captured elsewhere). For paper substance, go straight to `SS-8_interstitial_neutron_2EV_scaling.tex` and its CHANGELOG header. For governance context, read PD-001 through PD-003 in order of date, then `templates/operating_system.md` §§14–15.

**If Thomas wants the current state:** The one-minute orientation above is designed for you too. State is SS-8 v1.0 publishable, OPEN-ORG-004 RESOLVED (Strong Sector now uniformly per-paper-subfolder), data infrastructure operational, governance queue at 6 open / 3 resolved.

**If you are triaging what to do next:** Scan `Organizational_Frontier.md`, check whether SS-9 is the next paper (and if so, sequence OPEN-ORG-003 before drafting), and use the priority list above. The previous "next-session-eligible" queue is now empty (OPEN-ORG-007 was the only such item, resolved this session). Next major work items are SS-9 planning + OPEN-ORG-003 prerequisite, or one of the dedicated-execution-session items (OPEN-ORG-009).
