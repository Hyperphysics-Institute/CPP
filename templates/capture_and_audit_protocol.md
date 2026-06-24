# The Capture-and-Audit Protocol

**STATUS: DRAFT — pending CONV-001 panel review + TLA ratification.** NOT canonical until then.
**Established:** Patch 2102 (Step 2 of the 2100-band campaign; seed handover `templates/2100_HANDOVER_capture_and_audit_protocol.md`).
**Peer of:** `operating_system.md`, `reasoning_capture_protocol.md`, `paper_completion_checklist.md`.
**Supersedes (for the capture pathway):** the scattered, real-time, per-patch capture rules. It does **not delete** `reasoning_capture_protocol.md`; it inverts when its judgment happens (see §6).

## 0. BLOCKING CLONE GATE (line 1)
Before placing a file, editing a registry, or running the audit: clone fresh, grep the registries, confirm the band is clear. NO THEO. Status moves and canonical-registry edits are deferred to TLA — with the single, audited exception in §3.

---

## 1. The diagnosis (one root cause)
Eight months of intermittent capture failures share one cause: **selective extraction was done in real time, in the hot path, under load, across parallel windows.** Deciding *what to file where* is a JUDGMENT act, and judgment is exactly what drops out under compaction and window-switching. Every prior system failed the same way because each asked the worker to judge-and-file in the moment.

## 2. The inversion (the whole protocol in one move)
**Capture everything raw and cheap in the moment — a mechanical act that cannot fail because it needs no judgment. Move ALL judgment to a batched nightly audit with full context and no time pressure.** Raw capture is mechanical; extraction is judgment; the bug was conflating them. Separate them and the failure class dissolves.

**Keystone property:** a verbatim raw transcript is reconstruction-proof. The original is never destroyed, so any dropout is trivially re-extractable instead of sometimes-impossible. (The founder's-voice recovery pain exists *only* because originals were paraphrased before saving. Raw capture ends that permanently.)

This reduces to **two pieces + a heartbeat**.

---

## 3. Piece 1 — Automatic raw capture (the daytime path: do nothing but record)

- **Record everything, automatically, verbatim, flat.** One tree: `Development/transcripts/`. Filename carries everything: `YYYY-MM-DD_HHMM_p<patch>_<window-slug>.md`. The **window-slug — never the discipline — is the collision key**: N windows on N phenomena each write their own slug and never collide, and no one decides "which discipline folder." Discipline-filing is the audit's job (§4).
- **During the day, the worker does nothing else.** No registry edits. No founder's-voice capture. No fragment-filing. The recording is mechanical and is the sole daytime obligation; everything downstream is the nightly audit's job. ("Record everything automatically if that is possible" — the capture must not depend on a worker *choosing* to write each turn, or the root cause reappears one level down. Implement capture as an automatic dump/export of the verbatim turns, not a per-turn worker action.)
- **Content:** the full verbatim turn (TLA's words + worker's words), every round. Exclude only obviously procedural turns (pure "apply this / proceed"). This tree is GROUND TRUTH — every other artifact is derived from it and re-derivable from it.

## 4. Piece 2 — The nightly extraction macro (where ALL judgment lives)

A scripted batch job — `scripts/overnight_extraction_audit.sh` — modeled on Isak's `consolidate_bibliography.sh` (§7). Each night it:
1. reads the day's `Development/transcripts/*`;
2. **analyzes every verbatim turn and separates it into fragments**, filing each to its proper home: reasoning → the right sector `reasoning/<patch>.md`; verification scripts → `verify/`; founder contributions → `founders_vision.md` (verbatim); **registry-worthy deltas → the canonical registries** (theorem-registry, predictions, frontier sectors, todo);
3. writes a dated **heartbeat** (§5).

**Inherited safety rails (from Isak's pattern — do not reinvent):** `--dry-run` first; verify-after-act (assert the write took, don't trust a downstream artifact); **auto-flag `[REVIEW]` on any ambiguity** and never silently guess; clean tree on every exit path; **runs on the local machine, not the container** (needs real tools). The macro produces a plan-of-record under `--dry-run` before any real write.

**Founder's-voice promotion — staged first, auto once proven.** `founders_vision.md` is canonical, and this is the macro's one authorized canonical write. Per TLA: it graduates. **v1 = reviewed-first** — the macro stages a diff (promote-candidate blocks + their `[REVIEW]` flags) for TLA to confirm, exactly as the rest of the repo defers canonical edits to TLA. **v2 = auto-promote** once the `[REVIEW]` rail has demonstrably caught the ambiguous cases and never fabricated a quote. The `[REVIEW]` trigger set: can't cleanly bound TLA's verbatim words; attribution unclear; multiple candidate quotes; quote spans turns. The existing `sweep_founder_contributions.sh` (read-only promoted-vs-orphan detector) is the seed for this step.

## 5. The heartbeat (anti-silent-rot rail)
The macro writes a dated line to `Development/audit_log.md` every run. **If last night's entry is missing, the failure is LOUD, not silent** — a blocking flag at next bootup. This is the guard against the exact rot that killed the old systems: the audit stopping unnoticed.

---

## 6. Relationship to `reasoning_capture_protocol.md`
That protocol put capture in the per-patch contract — capture-at-patch-time, by the worker, in the moment. This protocol **inverts when the judgment happens**: the worker no longer judges-and-files during the day; the raw transcript is the universal capture and the nightly macro does all splitting/filing/promotion. `reasoning_capture_protocol.md` is not deleted — its §0 (verbatim-only-at-source), §4 (verbatim/reconstructed provenance flag), and §10 (founder-contribution *format*) remain the schema the macro files *into*. What changes is the *owner and timing* of the judgment: macro, overnight — not worker, in-the-moment.

## 7. Reuse Isak's pattern — do NOT rewrite his protocol
Isak's WORKFLOW-1/2/3 jobs (bibliography consolidation, DOI harmonization, OSF registry snapshots) are content-audit work and stay **as-is** — not merged, not rewritten. But `scripts/consolidate_bibliography.sh` is the **proof-of-concept and template**: it already does the shape we want — a batched, scripted, local-machine reconciliation of many files into canonical ones, with `--dry-run` and auto-revert-and-flag-`[REVIEW]`-on-ambiguity. The nightly audit = "Isak's audit discipline pointed at raw transcripts instead of bib files." Confirm with Isak/TLA that the machine hosting his audits can host this one (same need: real tools, not the container), and the nightly scheduler (cron / Windows Task Scheduler) — the §5 heartbeat is the net if it ever fails to run.

## 8. What collapsed under the reframe (recorded for the panel)
The seed handover (§2B) proposed a write-partitioned `Registries_temp/<slug>.md` so daytime windows could record registry intentions collision-free. **Under the reframe this is dropped:** with universal raw capture + a macro that extracts registry deltas from the transcript like everything else, the separate write path is redundant. Its one unique benefit — same-day cross-window read visibility of in-flight registry changes — is waived by the "don't worry about registries during the day" decision (canonical-stale-until-morning accepted). If cross-window same-day registry visibility is later wanted, it returns as a *read-only render* (glob the day's transcripts), never a shared write target. **Flagged for TLA ratification.**

## 9. Honest cost framing (do not oversell as "zero overhead")
This trades STORAGE for RELIABILITY (good trade: raw transcripts are cheap; a dropped founder insight is expensive) and relocates overhead from real-time to overnight batch. It is **no real-time overhead, deferred batch overhead — NOT zero overhead.** The batch is unattended but it is real work and it CAN fail; that is precisely why §5 exists.

## 10. Discipline reminders
- No numerics/script recorded as proof — consistency-evidence only.
- Status moves + canonical-registry edits deferred to TLA; `founders_vision.md` promotion is the SOLE authorized automated canonical write, and only via the `[REVIEW]`-flagged audit (staged-first per §4).
- Own errors forward-additively; the CONV-001 panel will catch overclaims.
- Not canonical until CONV-001 panel + TLA ratification (§5.6 of the handover).
