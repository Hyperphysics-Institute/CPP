# The Capture-and-Audit Protocol

**STATUS: CANONICAL — ratified Patch 2111 (TLA), after panel RATIFY 4/4 over two CONV-001 rounds (Patch 2106 RATIFY-WITH-CHANGES → 2110 confirmatory RATIFY).** Ratified as the standing spec. **NOT YET OPERATIONAL:** the protocol activates only once the §3.1 automatic-capture mechanism and the Step-4 nightly macro (`scripts/overnight_extraction_audit.sh`) are built and scheduled. Until then, windows continue current capture/registry practice — the deferral channels (`Development/transcripts/`, `Registries_pending/`) are defined but not yet consumed by an audit that does not yet exist.
**Established:** Patch 2102. **Revised:** Patch 2108 — integrated the 4-reviewer change set (C1–C8), the founder-promote posture (T3 = staged-default/never-auto-graduate), the scope boundary (§7), and the deliberate-delta `Registries_pending/` mechanism (§6) that the paper-production protocol (Patch 2107) consumes. **Revised:** Patch 2116 (TLA-ratified) — added §6.1 temporary-THEO-handle late-binding rule (patch-anchored handles → nightly permanentize); the worker-side rule is live, the auditor rebind stage is tracked as a build item (Patch 2117). **Revised:** Patch 2117 — built the §6.1 permanentize stage into `overnight_extraction_audit.sh` (v1-staged: per-family deterministic assignment, staged corpus-rename + registry registrations, alias map with 2-night grace); folded the regression case into the live harness (34/34).
**Peer of:** `operating_system.md`, `reasoning_capture_protocol.md`, `paper_completion_checklist.md`.
**Supersedes (for the capture pathway):** the scattered, real-time, per-patch capture rules. It does **not delete** `reasoning_capture_protocol.md`; it inverts when its judgment happens (see §8).

## 0. BLOCKING CLONE GATE (line 1)
Before placing a file, editing a registry, or running the audit: clone fresh, grep the registries, confirm the band is clear. NO THEO. Status moves and canonical-registry edits are deferred to TLA — with the single, audited exception in §4.1, whose bounds are stated explicitly there.

---

## 1. The diagnosis (one root cause)
Eight months of intermittent capture failures share one cause: **selective extraction was done in real time, in the hot path, under load, across parallel windows.** Deciding *what to file where* is a JUDGMENT act, and judgment is exactly what drops out under compaction and window-switching. Every prior system failed the same way because each asked the worker to judge-and-file in the moment.

## 2. The inversion (the whole protocol in one move)
**Capture everything raw and cheap in the moment — a mechanical act that needs no content judgment. Move ALL judgment to a batched nightly audit with full context and no time pressure.** Raw capture is mechanical; extraction is judgment; the bug was conflating them.

**What this achieves, stated honestly (per panel C1).** This does not make capture "unable to fail" and does not "dissolve the failure class." It **converts irreversible-loss failures into recoverable-processing failures**: a verbatim raw transcript is reconstruction-proof, so a dropout downstream is trivially re-extractable instead of sometimes-impossible. That is a major reliability improvement, not the elimination of failure — and it holds **only if the automatic capture mechanism (§3.1) actually functions.** Absent that mechanism, the root cause reappears one layer down (a worker forgetting to start capture).

This reduces to **two pieces + a heartbeat**, with a precise scope boundary (§7).

---

## 3. Piece 1 — Automatic raw capture (the daytime path: do nothing but record)
- **Record everything, automatically, verbatim, flat.** One tree: `Development/transcripts/`. Filename: `YYYY-MM-DD_HHMM_p<patch>_<window-slug>.md`. The **window-slug — never the discipline — is the collision key.** Discipline-filing is the audit's job (§4).
- **During the day the worker does no capture judgment at all.** No discipline-filing, no founder's-voice capture, no fragment-filing. **No procedural-turn exclusion either (per panel C4):** capture *everything*, including turns that look procedural — deciding what is "procedural" is itself a judgment, and the daytime path must be judgment-free. The macro filters procedural turns in Piece 2.
- **Content:** the full verbatim turn (TLA's words + worker's words), every round. This tree is GROUND TRUTH — every other artifact is derived from it and re-derivable from it.

### 3.1 Automatic Capture Mechanism Requirements (panel C1 — non-negotiable for ratification)
The keystone of §2 holds only if capture is genuinely mechanical. The capture mechanism MUST be:
- **Always-on and auto-started on window creation** — begins capturing without any worker action.
- **Zero-touch / non-bypassable** — no manual trigger, no "remember to export," no per-turn worker write. A worker-triggered script does NOT satisfy this (it re-imports the human-compliance-under-load failure).
- **Immediate and durable** — verbatim turns are persisted to disk as they occur, with fsync-level durability. **No in-memory buffering, no lazy writes** (panel C2/T4): a catastrophic context loss mid-day must not lose the day's transcript before the night's run sees it.
Until a mechanism meeting all three exists, this protocol's guarantee is aspirational; a worker may append as a best-effort backstop. The protocol is ratified as the standing spec, but it is **not operational — and the keystone guarantee is not delivered — until a mechanism meeting all three exists** (the activation gate; see STATUS).

## 4. Piece 2 — The nightly extraction macro (where ALL judgment lives)
A scripted batch job — `scripts/overnight_extraction_audit.sh` — modeled on Isak's `consolidate_bibliography.sh` (§9). Each night it:
1. **transcript-integrity / corpus-completeness check first (panel C6):** enumerate the day's *expected* captures, verify each is present and readable, and flag any missing / truncated / orphaned transcript — recording the result in the heartbeat (§5). The audit does not silently assume the corpus is complete.
2. reads the day's `Development/transcripts/*` and **filters procedural turns** (moved here from the daytime path, C4);
3. **analyzes every remaining verbatim turn and separates it into fragments**, filing each to its home: reasoning → sector `reasoning/<patch>.md`; verification scripts → `verify/`; founder contributions → `founders_vision.md` (verbatim, via §4.1); **registry deltas → canonical** (see the two delta classes in §6);
4. writes a dated **heartbeat** (§5).

**Inherited safety rails (from Isak's pattern — do not reinvent):** `--dry-run` first; verify-after-act; **auto-flag `[REVIEW]` on any ambiguity** and never silently guess; clean tree on every exit path; **runs on the local machine, not the container.**

### 4.1 Founder's-voice promotion (T3 = staged-default; auto NEVER self-graduates)
`founders_vision.md` is canonical, and the audit's write to it is **the single automated exception** to "all canonical edits deferred to TLA." **The bounds of that exception are stated explicitly and narrowly (panel C8):** it applies only to `founders_vision.md`, only via the `[REVIEW]`-gated path below, and to nothing else canonical; the audit stages — it does not push.
- **v1 (standing default): reviewed-first.** Each night the audit writes founder-voice candidates to `Development/staging/<date>/founders/` as a proposed diff, each labelled AUTO-clean or `[REVIEW]:<trigger>`. **Nothing is written to `founders_vision.md`; nothing is pushed.** TLA reviews in the morning (§4.2), approves/edits/rejects, and applies + pushes. The canonical write stays TLA's.
- **v2 (auto-promote) NEVER self-graduates.** It turns on only by **explicit TLA action**, and only after measurable criteria are met: a defined number of consecutive clean nights, **zero false-negatives on an adversarial founder-quote test suite**, and a documented rollback procedure. Even under v2, `[REVIEW]`-flagged candidates still stage for the morning review; only provably-clean AUTO candidates ever write themselves. (TLA's ruling: the machine never decides it has earned the right to write his voice.)
- **The `[REVIEW]` trigger set** (auto-promote only the single/cleanly-bounded/unambiguously-attributed/verbatim/novel passage with a clean context anchor and no normalization; any of these forces `[REVIEW]`): bounds undelimitable; attribution uncertain; multiple candidate passages; quote spans turns; only a paraphrase exists; duplicate/overlap with an existing entry; no accurate one-line context without inferring intent; extraction needed more than whitespace cleanup. **Global default: any uncertain or stubbed detector resolves to `[REVIEW]`, never AUTO.** Seeded by `sweep_founder_contributions.sh`.

### 4.2 `[REVIEW]`-queue ownership (panel C5 — close the silent-drift seam)
Resolving the prior run's `[REVIEW]` flags is a **defined, blocking action**, not an unowned pile:
- **founders_vision candidates** → TLA's morning review of `Development/staging/<date>/founders/` is the owner. Approved entries are applied + pushed by TLA.
- **non-canonical flags** (reasoning/verify/registry-delta ambiguities) → cleared by the next window at bootup as a blocking step before new work, alongside the §5 heartbeat check.
Uncleared flags must not accumulate into silent canonical drift; the heartbeat reports the open-flag count.

### 4.3 Macro implementation requirements (panel C7 — land in the Step-4 build, not this prose)
The macro MUST include, before it is trusted: **schema-validation before any canonical write**; **explicit partial-night handling** (a mid-run crash defines retry / rollback / block — never partial-success-as-success); and a **regression test-suite**. These are build requirements for `overnight_extraction_audit.sh`, tracked with the Step-4 work.

## 5. The heartbeat (anti-silent-rot rail — now completeness-aware, panel C2)
The macro writes one dated line to `Development/audit_log.md` every run. The line reports not just **"did it run?"** but **"did it process all expected inputs?"** — the §4-step-1 integrity result (transcripts expected/seen/missing), fragments filed by class, founders staged/review/promoted, and open `[REVIEW]` count. **A missing line is a LOUD, blocking flag at next bootup; a `run=FAIL` or incomplete-corpus line is recoverable but still surfaced.** Partial success can no longer masquerade as success.

---

## 6. Registry deltas — two classes (NEW, panel-driven + Patch 2107)
Not all registry changes are alike, and the difference decides how each is captured:
- **Incidental deltas** — a mid-reasoning "we should register X" that was never a deliberate, precise registration. The macro **extracts these from the raw transcript** (judgment, overnight). Stale-until-morning is fine; low stakes.
- **Deliberate deltas** — precise, structured registrations the window *knows exactly* (paper-production Phase 5 / Phase 7B: "register THEO-X coeff 3/5; +3 zero-parameter predictions; paper_catalog row 'SF-7 v1.0 SHIPPED'"). These must **NOT** be reconstructed from prose — the window writes the exact delta, in-session, to its **own write-partitioned pending file** `Registries_pending/<window-slug>.md` (append-only to its own file; never a shared target). The macro merges all windows' pending deltas into canonical overnight with full cross-window context, then clears them. **Collision-free by construction.**

**The judgment stays in-session; only the write-to-canonical defers.** This is why the deliberate case scope-revives a write-partitioned pending area where the general incidental case does not (see §10).

**Read-render (same-day visibility).** To see another window's in-flight registrations before the overnight merge — and **REQUIRED before allocating any registry ID** (THEO / PRED / OPEN-problem, to prevent two windows grabbing the same ID) — read canonical **AND glob `Registries_pending/*.md`** (in-flight claims). Read-only; never a shared write target.

### 6.1 Temporary THEO handles — late-binding, collision-free ID allocation (NEW, Patch 2116, TLA-ratified)

A window that must reference a not-yet-permanent theorem mid-session does **NOT** allocate a permanent number in the hot path (that remains a deferred canonical-registry write, §6/§7). It mints a **temporary handle** anchored to the patch/window namespace, which is collision-free by construction.

**Why this is collision-free (the one design point).** A temp token that *guesses the final integer* (e.g. `THEO-DS-7-Temp`) still collides: two windows in the DS family both grep, both see 6 as the max, both mint `-7-Temp`, and the merge cannot tell the two theorems apart — which is what forces a change-order. Anchoring the handle to a namespace that is already collision-free — the patch number (band-partitioned: only one window can ever mint `p08xx`) — makes every handle globally unique regardless of what any window grepped. The nightly rebind is then a **unique → unique** map, the conflict-and-change-order case cannot arise, and **correctness does not depend on the night job** (the handle is already unambiguous; the rename is cosmetic, so a late or skipped audit breaks nothing).

**Implementation status.** The handle format and worker obligations are **live**. The auditor stage is **built (Patch 2117), v1-staged**: each night the macro assigns permanents (deterministic per family, by patch then seq), stages the corpus rename (a ready-to-run apply script) and the `theorem-registry` registrations under `Development/staging/<date>/permanentize/` for TLA's one-command morning apply, and **directly** maintains the alias map (`Development/theo_alias_map.md`, 2-night grace). It does **not** auto-rewrite committed papers — auto-apply is a v2 graduation by explicit TLA action, mirroring the §4.1 founders posture. Safe because the handles are already unambiguous (the rename is cosmetic), so a staged-but-not-yet-applied rename still resolves via the alias map.

**Handle format (canonical form):**

```
THEO-<FAMILY>-TMP-p<patch>[-<seq>]
```

- `<FAMILY>` — sector family (`DS`, `SS`, `CHIR-CONT`, `SM`, `QM`, …). Choosing the family is allowed in-session: families are lane-local and need no global integer.
- `TMP` — literal marker; makes every in-flight handle greppable and unmistakably non-permanent.
- `p<patch>` — originating patch number; band-partitioned, hence globally unique to the minting window.
- `-<seq>` — optional `1,2,3…` when one patch introduces multiple new theorems.

**Optional readability variant (display guess):** `THEO-<FAMILY>-<n>-TMP-p<patch>`, where `<n>` is an optimistic guess at the final number (grep family-max + 1). The auditor keys only on the `-TMP-p<patch>` segment; `<n>` is cosmetic. If `<n>` was free it permanentizes to `THEO-<FAMILY>-<n>`; if two windows both guessed `<n>`, their distinct `p<patch>` segments keep them separate and they permanentize to distinct numbers — no change order.

**Worker obligations (in-session):**
1. Mint the temp handle. No grep-for-a-free-number is required for correctness (grep only to seed the optional display guess).
2. Use the temp handle **uniformly** for that theorem across all documents, papers, and citations.
3. Append the claim to your own `Registries_pending/<window-slug>.md` (append-only to your own file; never a shared target): one line giving the temp handle, family, originating patch, and a one-line theorem statement. The temp handle is the citable form of this pending entry.

**Auditor obligations (nightly, in `overnight_extraction_audit.sh`, under the §4.3 schema-validation-before-canonical-write gate) — build item, Patch 2117:**
1. Collect every unique `*-TMP-*` handle across the corpus and all `Registries_pending/*.md` claims.
2. Per family, assign each unique handle the next free permanent number in a **deterministic order** (by patch number, then `seq`) so assignment is stable across re-runs.
3. Corpus-wide find-replace each unique handle → its permanent `THEO-<FAMILY>-<n>` (v1: staged as a ready-to-run apply script for TLA — see Implementation status). Because handles are unique, each replace is unambiguous (it also updates a *different* window's citation of your in-flight theorem, since that window cited the same global handle).
4. Register the permanent THEO in `theorem-registry.md`; clear the merged pending claims.
5. Write a `temp → permanent` entry to `Development/theo_alias_map.md`, kept for a **grace window (default 2 nights)**, so a citation written from a slightly stale clone still resolves before the final sweep.
6. Log to `audit_log.md`: handles seen, permanentized, aliased, and any optimistic-guess clashes auto-resolved.

**Composition with existing rules:**
- **Reserved slots** (the `THEO-DSL-7` / `THEO-DSL-9` reservations in `reasoning_capture_protocol.md` §8) take precedence: a handle destined for a pre-reserved slot honors the reservation. Pre-reservation and temp-handles compose.
- **Reassignment** ("made permanent or reassigned"): the auditor may bind a handle to a permanent number other than the optimistic guess; the alias map keeps stale citations resolving through the grace window.
- The §6 **read-render** step is still good practice for seeding a sensible display guess, but is **no longer load-bearing for collision-safety** — safety now comes from the handle namespace, not from the read.

**Net:** work in different bands and different filenames; for new theorems, cite a patch-anchored `TMP` handle and let the nightly auditor permanentize it. Collision-free by construction; the rebind is cosmetic; nothing breaks if a night is missed.

## 7. Scope boundary — what this protocol governs vs leaves untouched (NEW, C9)
The protocol governs the **capture layer**, not the **work layer**. It does NOT relegate deliverable work to the overnight run.
- **Untouched (in-session, as today):** all deliberate deliverable work — writing the `.tex`, development logs, reviewer-response docs, the companion documentation suite, verification notebooks, OSF registration, review dispatch. A batch macro cannot do this work; none of it moves overnight.
- **Governed (the capture layer):** the reasoning, founder's-voice, and registry-delta *byproducts* of that work — recorded raw by day, mined overnight.
- **The one interaction with paper production:** the shared repo-root registry edits (Phase 5 + Phase 7B + shared-file 7A items) are written as precise deltas to `Registries_pending/<slug>.md` instead of hand-applied to canonical in-session, then merged overnight (§6). Paper production is otherwise unchanged. See `operating_system.md` §4 "Parallel-window registry discipline" (Patch 2107). Bonus: the raw transcripts make a better substrate for Phase 8 transcript curation than hand-curation did — additive, not in tension.

## 8. Relationship to `reasoning_capture_protocol.md`
That protocol put capture in the per-patch contract — capture-at-patch-time, by the worker. This protocol **inverts when the judgment happens**: the raw transcript is the universal capture and the nightly macro does all splitting/filing/promotion. `reasoning_capture_protocol.md` is not deleted — its §0 (verbatim-only-at-source), §4 (provenance flag), and §10 (founder-contribution *format*) remain the schema the macro files *into*. What changes is the owner and timing of judgment: macro, overnight — not worker, in-the-moment.

## 9. Reuse Isak's pattern — do NOT rewrite his protocol
Isak's WORKFLOW-1/2/3 jobs stay **as-is**. But `scripts/consolidate_bibliography.sh` is the proof-of-concept and template: batched, scripted, local-machine reconciliation of many files into canonical ones, with `--dry-run` and auto-revert-and-flag-`[REVIEW]`-on-ambiguity. The nightly audit = "Isak's audit discipline pointed at raw transcripts." Confirm with Isak/TLA that the machine hosting his audits can host this one, and the nightly scheduler (cron / Windows Task Scheduler) — the §5 heartbeat is the net if it ever fails to run. **Activation runbook (scheduler entry, morning-review steps, go-live checklist): `Development/ACTIVATION.md`.**

## 10. What collapsed under the reframe — and the scoped revival (updated; panel ratified T2 SOUND 4/4)
The seed handover (§2B) proposed a write-partitioned `Registries_temp/<slug>.md` as a **general daytime registry-write path**. The panel ratified collapsing that **general** path 4/4: incidental deltas are extracted from the transcript, and same-day cross-window visibility was waived for the general case. **The 2108 revision scope-revives a write-partitioned pending area for the narrow *deliberate-delta* case only (§6)** — paper-production registrations that are precise and known, where prose-reconstruction would be error-prone. This **refines T2 rather than overturning it**: there is still no general daytime registry-write path, and `Registries_pending/` is per-window (never shared), with a read-only render for the cases that need same-day visibility (the realization of the read-render anticipated when the general path collapsed). *Noted for the panel record.*

## 11. Honest cost framing (do not oversell as "zero overhead")
Trades STORAGE for RELIABILITY (raw transcripts cheap; a dropped founder insight expensive) and relocates overhead from real-time to overnight batch. It is **no real-time overhead, deferred batch overhead — NOT zero overhead.** The batch is unattended but is real work and CAN fail; that is precisely why §5 exists. And per §2/§3.1, the reliability gain is real only when the automatic capture mechanism functions.

## 12. Discipline reminders
- No numerics/script recorded as proof — consistency-evidence only.
- Status moves + canonical-registry edits deferred to TLA. The SOLE automated canonical write is `founders_vision.md` promotion, only via the `[REVIEW]`-gated audit, staged-first (§4.1), with its bounds stated narrowly there; deliberate registry deltas are *staged* in `Registries_pending/` and merged by the audit, not hand-written to canonical mid-day.
- Own errors forward-additively; the CONV-001 panel catches overclaims.
- **Canonical — ratified Patch 2111** (panel RATIFY 4/4, two CONV-001 rounds). Operational once the §3.1 capture mechanism and the Step-4 macro are built + scheduled (the activation gate in STATUS); until then, current capture/registry practice continues.
