# HANDOVER — Campaign: the Capture-and-Audit Protocol (raw transcript capture + overnight extraction)

**Opened:** Patch 2100, **band 2100–2149** (disjoint from the active 2058–2099 Lorentz lane and the OPEN-SR-10
window). **For:** a fresh, dedicated window. **Integrator/founder:** Thomas (TLA). **Mandate:** replace the
scattered, intermittently-failing per-patch capture rules with one robust system — cheap raw capture in the
moment, all judgment moved to a batched overnight audit. This is foundational infrastructure; treat it with the
care of a registry change, not a worker patch.

## 0. BLOCKING CLONE GATE (line 1)
Clone fresh; grep registries; confirm **2100 free** and the band 2100–2149 clear. Multiple windows are LIVE
(Lorentz campaign in 2058–2099; an OPEN-SR-10 window reached 2080). Do NOT touch their bands. This window owns
2100–2149. NO THEO. Status moves deferred to TLA.

## 1. The diagnosis (why every prior system failed — fix the cause, not the symptom)
Eight months of intermittent capture failures share ONE root cause: **selective extraction was done in
real-time, in the hot path, under load, across parallel windows.** Deciding *what to file where* is a JUDGMENT
act, and judgment is exactly what drops out under compaction / window-switching. Every prior system (file-by-
discipline development folders; the scripts-vs-yours-vs-mine split; per-patch registry edits) failed the same
way because they all asked the worker to judge-and-file in the moment.

**The fix inverts it:** capture EVERYTHING raw and cheap in the moment (a mechanical act that cannot fail
because it needs no judgment); move ALL judgment — splitting, attribution, discipline-filing, registry merge —
to a batched **overnight audit** with full context and no time pressure. Raw capture = mechanical; extraction =
judgment; the bug was conflating them. Separate them and the whole class of failure dissolves. **Keystone
property:** a verbatim raw transcript is reconstruction-proof — the original is never destroyed, so every
dropout becomes trivially re-extractable instead of sometimes-impossible. (TLA's founders_vision recovery pain
exists ONLY because originals were paraphrased before saving. Raw capture ends that permanently.)

## 2. What to BUILD (three pieces + a heartbeat)

### 2A. Flat-by-window raw transcript capture (NOT by discipline)
- One flat tree: **`Development/transcripts/`**. NEVER file the raw transcript by discipline — that ambiguity is
  what broke the original system when papers went cross-disciplinary (judgment in the hot path again).
- Filename carries everything: **`YYYY-MM-DD_HHMM_p<patch>_<window-slug>.md`**. The **window-slug** (not the
  discipline) is the collision key: N workers on N phenomena each write their own slug, never colliding, never
  deciding "which discipline folder." Discipline-filing is the AUDIT's job (§2C), done overnight.
- Content: the full verbatim turn (TLA's words + worker's words), every round. Worker still does best-effort
  in-the-moment §10/reasoning/script capture as today — but the raw transcript is the GROUND TRUTH backstop, so
  any in-the-moment miss is recoverable. Exclude only obviously procedural turns (pure "apply this / proceed").

### 2B. Write-partitioned registry-temp (the multi-window registry fix)
- **NOT a single shared `Registries_temp.md`** — a shared append target is itself the collision problem (two
  windows appending = lost write / conflict; the recovery file corrupts). 
- Instead: **`Registries_temp/<window-slug>.md`**, one file per window, **each window appends ONLY to its own**.
  Zero write contention because no two windows ever touch the same file.
- **Read protocol (new standing rule for ALL windows):** to read any high-access registry (Frontier, theorem-
  registry, todo, predictions), check the canonical file AND glob `Registries_temp/*.md`. You get always-
  available-even-if-stale registry state with no contention.
- The overnight audit merges all per-window temps into the canonical registries and clears them.

### 2C. The overnight extraction audit (reuse Isak's pattern — see §4)
A scripted, runs-on-a-real-machine (not container) batch job that, each night:
1. reads the day's `Development/transcripts/*`;
2. extracts and FILES to discipline folders: founder contributions → `founders_vision.md` (verbatim);
   reasoning → the right sector `reasoning/`; scripts → `verify/`;
3. merges `Registries_temp/*.md` into canonical registries; clears the temps;
4. **founders_vision promotion is AUTOMATED** (TLA's call: "automate it") — BUT anything ambiguous
   (can't cleanly bound TLA's verbatim words, attribution unclear) is auto-flagged **`[REVIEW]`**, never
   silently guessed. No-overhead on the clean majority; only genuine judgment calls reach TLA's eyes. This is
   the one rail that makes "automate it" safe rather than fabricating the founder's voice.
5. writes a dated **heartbeat** to an audit log.

### 2D. Heartbeat (the anti-silent-failure rail)
The audit writes a dated line to `Development/audit_log.md` every run. **If last night's entry is missing, the
failure is LOUD, not silent.** This is the guard against the exact rot that plagued the old systems — the audit
stopping unnoticed. A missing heartbeat is a blocking flag at next bootup.

## 3. Honest cost framing (do not oversell as "zero overhead")
This trades STORAGE for RELIABILITY (good trade: raw transcripts cheap, dropped founder insight expensive) and
relocates overhead from real-time to overnight-batch. It is **no real-time overhead, deferred batch overhead** —
NOT zero overhead. The batch is unattended (runs while TLA sleeps), but it is real work and it CAN fail; hence
the §2D heartbeat. State this honestly in the protocol doc.

## 4. Reuse Isak's pattern — do NOT rewrite his protocol
Isak's existing work (OPEN-WORKFLOW-1 bibliography consolidation, DOI harmonization, OPEN-WORKFLOW-3 OSF registry
snapshots; `frontier_sectors/WORKFLOW.md`) is CONTENT-audit work and is **separate** — it stays as-is, NOT
merged or rewritten. BUT it is the proof-of-concept and template for §2C: `scripts/consolidate_bibliography.sh`
already does exactly the shape you want — a batched, scripted, runs-on-a-real-machine reconciliation of many
files into canonical ones, with **`--dry-run` first** and **auto-revert-and-flag-`[REVIEW]`-on-ambiguity** as
safety rails. The overnight extraction audit = "Isak's audit discipline pointed at raw transcripts instead of
bib files." Inherit his dry-run + REVIEW-flag rails; do not reinvent them. (Confirm with Isak/TLA that the local
machine running his audits can also host the nightly extraction audit — same environment need: real LaTeX/tools,
not the container.)

## 5. Build order (suggested)
1. Recon: read `frontier_sectors/WORKFLOW.md` (Isak's pattern), `templates/reasoning/2048_project_tracking_
   protocol.md`, `templates/reasoning/2034_founder_capture_protocol.md`, `templates/sweep_founder_
   contributions.sh`, `templates/founder_backlog_verbatim_recovery_handover.md`. Capture as recon note.
2. Write `templates/capture_and_audit_protocol.md` — the canonical protocol doc (supersedes scattered per-patch
   capture rules; references, does not delete, the old ones until migration verified).
3. Scaffold `Development/transcripts/` and `Registries_temp/` (with READMEs stating the filename/append rules).
4. Write the overnight audit script skeleton (modeled on `consolidate_bibliography.sh`): transcript→split
   extraction, registry-temp merge, founders_vision auto-promote-or-`[REVIEW]`, heartbeat to
   `Development/audit_log.md`. Local-run (not container), `--dry-run` first.
5. Add the new READ protocol (check canonical + `Registries_temp/*.md`) and the raw-capture rule into
   `templates/operating_system.md` / the bootup so ALL future windows adopt it.
6. Panel-review the protocol (CONV-001) before declaring it canonical — it changes how every window works.

## 6. Carry-over cleanup this campaign should also sweep (the debt that triggered this)
This session (2049–2058, Lorentz/inertia) left §10 founder contributions captured in `reasoning/` but NOT
promoted to `founders_vision.md`: (a) TLA's scalar-SSV ruling (2050); (b) the velocity-emergence-not-axiom
reframe (2052); (c) inertia=B-field/DP-Sea adjudication (2055); (d) the rigid-bolus correction (2056/2057); plus
(e) the exact-emergent-Lorentz campaign DECISION reasoning (the Quixote-vs-hard call, probability calibration) —
which has no verbatim home. The new audit should sweep these from the 2049–2058 transcripts/reasoning on its
first run. (The older 1–22 June backlog stays with its own dedicated window per
`templates/founder_backlog_verbatim_recovery_handover.md` — do not merge that retrieval-heavy job in here.)

## 7. Discipline reminders (hard-won)
- No numerics/script recorded as proof — consistency-evidence only.
- Own errors forward-additively; the CONV-001 panel WILL catch overclaims.
- Status moves + canonical-registry edits deferred to TLA; `founders_vision.md` auto-promotion is the SOLE
  authorized automated canonical write, and only via the `[REVIEW]`-flagged audit.
- Every computation-bearing patch ships its script; re-audit at each handover.
- End patch-delivery with the apply-and-push macro + collision watch.
