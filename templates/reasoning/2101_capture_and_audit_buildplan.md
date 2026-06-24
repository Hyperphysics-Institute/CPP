# Reasoning capture — Patch 2101: Capture-and-Audit Protocol — Round-1 recon + formal build plan

**STATUS: verbatim (captured at-patch).** Window: 2100-band (owns 2100–2149). Opus worker; integrator = TLA.
**Campaign:** the Capture-and-Audit Protocol (seed handover: `templates/2100_HANDOVER_capture_and_audit_protocol.md`, Patch 2100).
**Round 1 scope:** recon only — no status moves, no THEO, no scaffolding written. Deliverable = this plan. Panel review before canonical.

**Clone gate (handover §0) — CLEARED.** Cloned fresh; grepped the band; **2100 consumed by the handover, 2101 free, 2100–2149 otherwise clear.** The 2058–2099 Lorentz lane terminates at 2080 (OPEN-SR-10 → RESOLVED-W2); both live lanes are disjoint from this band. Lease note below (§B).

`Track: WORKFLOW`

---

## A. Recon findings (§5.1 reads, and what each gives the campaign)

Read in full this round: `templates/2100_HANDOVER_capture_and_audit_protocol.md`, `frontier_sectors/WORKFLOW.md`, `scripts/consolidate_bibliography.sh`, `templates/reasoning_capture_protocol.md` (§0–§10), `templates/reasoning/2034_founder_capture_protocol.md`, `templates/reasoning/2048_project_tracking_protocol.md`, `templates/sweep_founder_contributions.sh`, `templates/founder_backlog_verbatim_recovery_handover.md`.

1. **Isak's `consolidate_bibliography.sh` is the proof-of-concept whose *shape* §2C inherits — not its content.** The load-bearing pattern to copy: numbered phases (0 preflight → 1 → 2 → 3 → Done); a hard preflight GATE (repo-root + tool presence + **clean-tree-or-`--dry-run`**); **`--dry-run` first** and narrowing flags (`--only`); **verify-after-act** (it asserts the edit actually took rather than trusting a downstream artifact); **auto-revert-and-flag-`[REVIEW]`** on any ambiguity / non-loss-free change; **clean-tree on *every* exit path** (SKIP/REVERT/ERROR/REVIEW all restore state); **never commits**; ends with a `Next:` handoff block; **runs locally, not in-container** (needs real tools). Per handover §4, Isak's actual WORKFLOW-1/2/3 jobs stay as-is — we point the same discipline at raw transcripts.

2. **The founder-promote step is half-built already — and it is the campaign's single highest-risk element.** `sweep_founder_contributions.sh` already greps every `FOUNDER CONTRIBUTION (verbatim — TLA)` block and flags promoted-vs-orphan by testing whether the first-quote snippet appears in `founders_vision.md`. It is deliberately **READ-ONLY**. §2C escalates it from a *reader* into the **sole authorized automated writer of a canonical file** (handover §7). That is the riskiest line in the whole design: the catastrophic failure mode is *fabricating the founder's voice*. The `[REVIEW]` rail (auto-flag anything whose verbatim bounds or attribution are not clean; never silently guess) is the one thing that makes "automate it" safe rather than dangerous, and it deserves the tightest implementation and the heaviest panel scrutiny. See §C-Q3.

3. **The 1–22 June backlog is OUT of scope and must stay out.** `founder_backlog_verbatim_recovery_handover.md` owns that retrieval-heavy recovery in its own dedicated window (it needs `recent_chats`/`conversation_search` against transcripts the repo doesn't hold). The handover §6 is explicit: this campaign's first audit run sweeps **only** the 2049–2058 carry-over (the five un-promoted contributions below). Merging the June backlog in here would re-create the overload that fragmented the original work.

4. **The design philosophy is already proven one level up (Patch 2048).** The project-tracking protocol made the same move this campaign makes: *mechanical-over-judgment, render-on-demand-not-hand-maintain.* Its key line — "git history already IS the per-patch, every-window, append-only, collision-free ledger" — is directly relevant: where the audit needs a ledger (heartbeat history, what-was-promoted-when), prefer git/append-only over a hand-maintained shared file. The write-partitioned `Registries_temp/<slug>.md` design (§2B) is the same anti-shared-file-collision instinct.

---

## B. Lease / anti-collision (correction to "take the band")

The lease board (`parallel_dev/lease_board.md`) is **single-writer — only the integrator (TLA) edits it**; worker windows read their lease and report status in chat (this is the board's own collision-avoidance invariant). So this window cannot *take* 2100–2149 by editing the board. What is true and verified: the band is clear, and this window is operating inside it. **Owed to TLA:** add the live-round row for this campaign (base_ref = `acbd97b4`, the 2100 handover commit) so the board stops trailing reality (its last live row is still Round 1, 2026-06-08; the entire 2050–2099 Lorentz lane lived only in git).

---

## C. The formal build plan

Six steps, following handover §5. Each lists deliverable, owned path(s), suggested patch sub-range within 2100–2149, and acceptance criteria. Steps 4–6 are gated on the open questions in §C-Q being answered by TLA/Isak first.

### Step 1 — Recon (THIS round) — DONE
- Deliverable: this note (Patch 2101).
- Acceptance: §5.1 reads complete; plan written; clone gate cleared. ✓

### Step 2 — Canonical protocol doc · suggested 2102–2104
- Deliverable: `templates/capture_and_audit_protocol.md` — the authoritative protocol. Written as a **peer of** `reasoning_capture_protocol.md`, which it *extends and supersedes for the capture pathway* but does **not delete**: it references the per-patch §10 capture as the now-best-effort foreground, with raw transcript as the ground-truth backstop. Must state the honest cost framing verbatim from handover §3 (storage-for-reliability; real-time→overnight-batch; **NOT zero overhead; the batch can fail**).
- Owned: `templates/capture_and_audit_protocol.md` (new, greenfield).
- Acceptance: doc covers all four pieces (2A/2B/2C/2D), the new READ protocol, the cost framing, and a clone-gate line-1 per `reasoning_capture_protocol.md` §9. Does not yet claim canonical status (that's Step 6).

### Step 3 — Scaffold the two trees · suggested 2105–2107
- Deliverable: `Development/transcripts/` and `Registries_temp/`, each with a `README.md` stating the rules:
  - `Development/transcripts/README.md`: filename contract `YYYY-MM-DD_HHMM_p<patch>_<window-slug>.md`; **window-slug, never discipline, is the collision key**; content = full verbatim turn, every round, exclude only pure procedural turns; this tree is ground-truth backstop, discipline-filing is the audit's job.
  - `Registries_temp/README.md`: one file per window `<window-slug>.md`; **append only to your own**; never a shared target; the new READ protocol (check canonical AND glob `Registries_temp/*.md`); the audit merges + clears.
  - `Development/audit_log.md`: seeded with a header explaining the heartbeat contract (missing entry = LOUD/blocking flag at next bootup).
- Owned: `Development/`, `Registries_temp/` (both new, greenfield).
- Acceptance: trees exist with READMEs; `.gitkeep` where needed; no canonical file touched.

### Step 4 — Overnight extraction audit skeleton · suggested 2108–2115  *(gated on Q1, Q2, Q3)*
- Deliverable: `scripts/overnight_extraction_audit.sh`, modeled on `consolidate_bibliography.sh` — phases: (0) preflight gate (repo root, tools, clean-tree-or-dry-run), (1) read `Development/transcripts/*` for the day, (2) split-and-file: founder contributions → `founders_vision.md` *verbatim, with the `[REVIEW]` rail*; reasoning → sector `reasoning/`; scripts → `verify/`, (3) merge `Registries_temp/*.md` → canonical, clear temps, (4) **auto-promote-or-`[REVIEW]`** for founders_vision, (5) heartbeat line → `Development/audit_log.md`. **`--dry-run` first; never auto-commits the canonical writes without the gate; runs locally, not container.** Reuse the `sweep_founder_contributions.sh` promoted-vs-orphan logic as the seed for step (4).
- Owned: `scripts/overnight_extraction_audit.sh` (new).
- Acceptance: `--dry-run` produces a correct plan-of-record against a seeded test transcript without writing; every ambiguous founder block resolves to `[REVIEW]`, never a silent guess; clean tree on every exit path. **First-run target: sweep the §6 carry-over** (the five 2049–2058 contributions in §D).

### Step 5 — Wire the standing rules into the OS · suggested 2116–2118  *(gated on Step 2/4 stable)*
- Deliverable: edits to `templates/operating_system.md` (+ the bootup pointer) adding (a) the raw-capture rule, (b) the new registry READ protocol (canonical + glob temps). **These are canonical-file edits → deferred to TLA to apply** (worker drafts the patch; TLA integrates), per handover §7.
- Owned (draft only): patch against `operating_system.md`, bootup pointer.
- Acceptance: all future windows inherit raw-capture + the temp-glob read; TLA has applied.

### Step 6 — CONV-001 panel review → canonical · suggested 2119–2120
- Deliverable: single-block CONV-001 dispatch of the protocol doc to the swarm (it changes how every window works). Only after panel + TLA ratification is `capture_and_audit_protocol.md` declared canonical and the scattered per-patch capture rules pointed at it.
- Acceptance: panel verdicts banked; TLA ratifies; canonical flag set.

---

## C-Q. Open questions that gate Steps 4–6 (need TLA/Isak before building)

**Q1 — How is raw capture *actually* mechanical?** This is the crux of whether the diagnosis holds. 2A says "capture EVERYTHING raw... a mechanical act that cannot fail because it needs no judgment." But if a *worker window must remember to append its transcript every turn*, that is still a memory/judgment step — the root cause reappears one level down. Truly mechanical capture wants an **export/dump** (Thomas pastes or a tool exports the raw conversation log flat into `Development/transcripts/`), with the worker's in-the-moment §10 capture remaining the *foreground best-effort* and the dump the *backstop*. **Recommend: the capture step must not depend on the worker choosing to write each turn.** Need TLA's decision on the actual capture mechanism (manual paste at window close? export tool? per-turn worker append accepted as best-effort-only?).

**Q2 — Who/what schedules the nightly run, and where?** The audit "runs while TLA sleeps" on the local machine (real tools, not container). On Windows/Git Bash that means Task Scheduler invoking the `.sh`, or a manual `bash scripts/overnight_extraction_audit.sh` at day's end. The §2D heartbeat only protects against silent failure if *something* is expected to run on a cadence. Need TLA/Isak to confirm the scheduling mechanism and that the machine hosting Isak's content-audits can host this one (handover §4 asks for exactly this confirmation).

**Q3 — The auto-write-to-canonical risk envelope.** `founders_vision.md` is canonical and §2C makes the audit its sole automated writer. Before Step 4 ships, pin down: (a) the precise `[REVIEW]` trigger set (can't cleanly bound TLA's verbatim words; attribution ambiguous; multiple candidate quotes; quote spans turns); (b) does an auto-promote *commit*, or stage-for-TLA-confirm? (the safest v1 stages a diff and lets TLA confirm, mirroring the rest of the repo's "canonical edits deferred to TLA" rule, with full automation as a later hardening once the `[REVIEW]` rail is proven). Recommend v1 = stage + heartbeat, not auto-commit, of canonical writes.

---

## D. First-run carry-over sweep (handover §6) — the debt that triggered this

The 2049–2058 (Lorentz/inertia) session left these §10 founder contributions captured in `reasoning/` but **not promoted** to `founders_vision.md`. The first audit run sweeps exactly these — and nothing older:
- (a) scalar-SSV ruling — Patch 2050
- (b) velocity-emergence-not-axiom reframe — Patch 2052
- (c) inertia = B-field/DP-Sea adjudication — Patch 2055
- (d) rigid-bolus correction — Patches 2056/2057
- (e) exact-emergent-Lorentz campaign DECISION reasoning (the Quixote-vs-hard call + probability calibration) — **no verbatim home yet**; the audit must locate/bound it or `[REVIEW]`-flag it.

The older 1–22 June backlog stays with `founder_backlog_verbatim_recovery_handover.md` — do **not** merge it here.

---

## E. What this round did NOT do (discipline)

No status moves; no THEO; no canonical-registry edit; no scaffolding written yet (Steps 3+ are gated). The lease-board row is owed to TLA (§B). The protocol is **not** canonical until Step 6. Per handover §7: founders_vision auto-promotion (when built) is the sole authorized automated canonical write and only via the `[REVIEW]`-flagged audit; everything else canonical stays deferred to TLA.

**Next:** TLA reviews this plan + answers Q1–Q3; adds the lease-board round (base_ref `acbd97b4`); then Step 2 (protocol doc) opens at 2102.
