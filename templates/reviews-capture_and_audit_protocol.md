# reviews-capture_and_audit_protocol — Multi-AI review of the Capture-and-Audit Protocol (DRAFT, Patch 2102)

**Cycle:** opened Patch 2105 (dispatch); responses integrated Patch 2106 (24 June 2026) · **Panel:** ChatGPT + Grok + Gemini + Copilot (4 independent reads) · **Campaign:** 2100-band, governance artifact (NO THEO)
**Outcome in one line:** **RATIFY-WITH-CHANGES, 4/4.** The central inversion (raw-by-day, judgment-by-night) is endorsed as the correct architectural move; **T2 (the 2B collapse) is ratified SOUND 4/4**; the unanimous required fixes are (C1) soften the "cannot fail" overclaim + hard-require an always-on zero-touch capture mechanism, (C3) specify measurable graduation criteria for founder-voice auto-promotion, and (C4) move procedural-turn filtering out of the daytime path; plus durability/completeness hardening (C2) and two seam-closures (C5 [REVIEW]-queue ownership, C6 corpus-completeness check). **No status moved; awaiting TLA ratification of the change set before the DRAFT markers come off.**

---

## §0. Identity caveat (per `review_dispatch_protocol.md` §4.1)

4 responses received = **4 independent reads, no double-counting.** Attribution is by **TLA's receipt labels (ground truth)**, not self-labels:

| Received doc | Self-label in text | TLA receipt label (ground truth) | Note |
|---|---|---|---|
| 1 | "ChatGPT (OpenAI GPT-5.5)" | **ChatGPT** | self-label matches |
| 2 | "Grok" | **Grok** | self-label matches |
| 3 | "ChatGPT" (with a Gemini-style reasoning trace) | **Gemini** | **cross-wiring** — self-labelled as another engine |
| 4 | "Copilot" | **Copilot** | self-label matches (TLA: "correctly identified") |

Cross-wiring is the known June-2026 failure mode; the in-document IDENTITY instruction reduces but does not eliminate it. **Verdicts are label-independent** (the 4/4 RATIFY-WITH-CHANGES count does not depend on which name attached), so the cycle does not turn on attribution. **One discrepancy flagged for TLA confirmation:** TLA's receipt note described the Gemini response as "identified self as Copilot," but the received text (doc 3) self-labels "ChatGPT." Recorded for steer-accuracy next cycle; does not affect any verdict. Gemini was the optional 4th read (breadth); here it produced full §8 design verdicts at REASONED tier, counted as a genuine fourth read.

---

## Part 1 — Per-reviewer verdicts (condensed; verdict lines preserved)

**ChatGPT — RATIFY-WITH-CHANGES.** T1 CONCERN ("cannot fail" is an overclaim; guarantee depends on the unbuilt automatic substrate). T2 SOUND (staleness tradeoff documented and internally consistent). T3 CONCERN (highest-risk element; "once proven" underspecified; requires measurable graduation criteria + zero-correction corpus). T4 CONCERN (heartbeat detects missed runs after the fact, not same-day loss or partial-failure; better than hot-path but not a complete guard). T5 CONCERN (load-bearing seam: nobody owns validating the *complete expected corpus* was captured/available). Additional: overclaim language throughout; "exclude procedural turns" reintroduces judgment; no semantic-completeness check; the single canonical-write exception needs unusually explicit constraints.

**Grok — RATIFY-WITH-CHANGES.** T1 CONCERN (sound *conditional on implementation*; keystone aspirational until the zero-judgment mechanism is proven). T2 SOUND (disjoint slugs, no daytime writes, deltas extracted overnight; staleness accepted). T3 CONCERN (rail reasonable but no objective "proven" criterion; once auto-enabled, undetected edge cases are permanent; favors stricter default). T4 SOUND (heartbeat adequate low-overhead guard; transcripts remain ground truth/recoverable). T5 CONCERN (core handoff clean; minor gaps: midnight-spanning windows, "procedural turn" definition, clone-gate vs the auto-writer). Change set: add §3 "Automatic Capture Mechanism Requirements"; concrete §4 graduation criteria + opt-in TLA ratification on first use; an "Edge Cases" note.

**Gemini — RATIFY-WITH-CHANGES** (self-labelled "ChatGPT"). T1 CONCERN ("cannot fail" dangerous unless the environment natively auto-saves with zero human intervention). T2 SOUND (correct tradeoff; disjoint phenomena → rare collisions caught by dry-run/[REVIEW]). T3 CONCERN — **strongest position: strike v2 entirely**; `founders_vision.md` should remain permanently staged-for-TLA-signoff; cost of a fabricated quote far outweighs auto-promotion convenience. T4 SOUND (continuous daytime disk writes mean a batch failure delays, not loses; loud bootup flag). T5 CONCERN — **critical seam: the [REVIEW] queue resolution** — protocol never says *who* clears flags or *when*; uncleared flags → silent canonical drift. Additional: "exclude procedural turns" reintroduces micro-judgment into the judgment-free path.

**Copilot — RATIFY-WITH-CHANGES.** T1 CONCERN (true only if the dump/export exists and is mandatory; require always-on, auto-started, non-bypassable). T2 SOUND (visibility-without-write-paths is the correct direction; no structural hazard). T3 CONCERN (right shape; graduation criterion underspecified; add a measurable test). T4 CONCERN (heartbeat necessary not sufficient; new failure class = latent loss *before* the batch runs; require immediate durable/fsync-level persistence). T5 SOUND *conditional* on T1/T4 fixed (no seam between the three given continuous+durable capture, sole-owner macro, blocking heartbeat). Additional: partial-night failure handling (retry/rollback/block) unspecified; schema-validation before any canonical write; regression test-suite for the macro is mandatory.

---

## Part 2 — Cross-reviewer synthesis

| Triage target | ChatGPT | Grok | Gemini | Copilot | Net |
|---|---|---|---|---|---|
| **T1 Keystone** | CONCERN | CONCERN | CONCERN | CONCERN | **4 CONCERN — unanimous** |
| **T2 2B-collapse** | SOUND | SOUND | SOUND | SOUND | **4 SOUND — ratified** |
| **T3 Founder-promote** | CONCERN | CONCERN | CONCERN | CONCERN | **4 CONCERN — unanimous** |
| **T4 Batch-SPOF** | CONCERN | SOUND | SOUND | CONCERN | **2/2 split (reconcilable)** |
| **T5 Decomposition** | CONCERN | CONCERN | CONCERN | SOUND\* | **3 CONCERN / 1 conditional-SOUND** |

**Strong convergence (4/4):**
- **The inversion is correct.** All four endorse raw-by-day / judgment-by-night as the right architectural move and a genuine reliability improvement over the prior hot-path workflow.
- **T2 ratified.** The 2B collapse (drop the registry-temp; accept canonical-stale-until-morning) is SOUND 4/4 — the design call holds; the read-only-render fallback is the right direction if same-day visibility is ever needed.
- **T1 overclaim.** "Cannot fail" / "failure class dissolves" overstate; the guarantee is real only if the capture mechanism is always-on, zero-touch, auto-started, non-bypassable — and that mechanism is unbuilt. The root cause can reappear one layer down ("worker forgot to start capture").
- **T3 unsafe-as-written.** "Once proven" is not a criterion. Three want measurable graduation gates; Gemini wants v2 struck entirely (permanent staged).

**The T4 split reconciles:** the two SOUND verdicts (Grok, Gemini) explicitly *assume* raw transcripts are persisted immediately/durably; the two CONCERN verdicts (ChatGPT, Copilot) say that assumption must be made an explicit requirement (no buffering/lazy writes; fsync-level) and that the heartbeat must detect *partial* success, not just "ran." Making the assumption explicit satisfies all four — there is no genuine disagreement, only an unstated premise.

**The T5 concerns converge on three closable seams:** (i) corpus-completeness — nobody owns checking the full expected transcript set was captured and is readable (ChatGPT, Copilot); (ii) [REVIEW]-queue ownership — nobody owns clearing flags, risking silent drift (Gemini); (iii) the daytime "exclude procedural turns" judgment-leak (ChatGPT, Gemini).

---

## Part 3 — Required change set (mapped to protocol sections) — awaiting TLA ratification

- **C1 (T1, 4/4) → §2/§3.** Replace "cannot fail" with the honest narrower claim (capture needs no *content judgment*, so it is not vulnerable to judgment-dropout, **provided the mechanism functions**). Add a §3 subsection **"Automatic Capture Mechanism Requirements"**: always-on, auto-started on window creation, zero worker trigger, non-bypassable, **immediate durable (fsync-level) writes — no buffering/lazy writes** (folds C2 durability in).
- **C2 (T4, reconciles split) → §4/§5.** Extend the heartbeat from "did it run?" to **"did it process all expected inputs?"** — partial-success / corpus-completeness detection recorded in the heartbeat line.
- **C3 (T3, 4/4) → §4. TLA DECISION REQUIRED (see below).** Either (a) measurable-criteria-gated v2 (N consecutive clean nights + zero false-negatives on an adversarial founder-quote test suite + defined rollback + explicit TLA ratification to first-enable, never auto-graduating); or (b) Gemini's stricter: **strike v2 — `founders_vision.md` stays permanently staged-for-TLA-signoff.**
- **C4 (T5/additional, 3 raised) → §3.** Strike "exclude only obviously procedural turns" from the daytime path; **capture everything**; the macro (Piece 2) filters procedural turns. Removes the last daytime judgment leak.
- **C5 (T5, Gemini) → §4/§5.** Specify **[REVIEW]-queue ownership**: clearing the prior run's `[REVIEW]` flags is a defined, blocking action (TLA for founders_vision; next window at bootup for non-canonical flags) so flags can't pile up into silent drift.
- **C6 (T5, ChatGPT+Copilot) → §4.** Add a **transcript-integrity step** to the nightly audit: enumerate expected captures, verify presence + readability, flag missing/truncated/orphaned, record in heartbeat (overlaps C2).
- **C7 (Copilot, implementation) → Step-4 macro requirements.** The macro MUST include: schema-validation before any canonical write; explicit partial-night handling (retry/rollback/block); a regression test-suite. Protocol doc references these as mandatory; they land in the Step-4 build, not the doc prose.
- **C8 (ChatGPT) → §4/§10.** Make the single automated-canonical-write exception's rationale and bounds unusually explicit (exceptions expand over time).

**Verdict:** panel = **RATIFY-WITH-CHANGES (4/4)**. The protocol stays **DRAFT** until (1) TLA ratifies the change set (and decides C3-a vs C3-b), (2) the revision lands (next patch), (3) TLA declares canonical. **The C3 decision is TLA's** — it concerns automated writes to TLA's own voice in a canonical file, and the panel split between "gate it hard" (3) and "never allow it" (1).

---

## Integration record (Patch 2108)

Change set integrated into the protocol v1.0-candidate (Patch 2108): **C1** (overclaim softened in §2; §3.1 "Automatic Capture Mechanism Requirements" added — always-on/zero-touch/non-bypassable/fsync-durable); **C2** (§5 heartbeat now completeness-aware — "processed all expected inputs?"); **C3 = TLA's middle** (§4.1 — v1 staged is the standing default; v2 never self-graduates, only explicit TLA enable after measurable criteria incl. zero-false-negative adversarial founder-quote test + rollback); **C4** (§3 procedural-turn exclusion removed from the daytime path → filtered by the macro, §4-step-2); **C5** (§4.2 `[REVIEW]`-queue ownership defined as a blocking morning/bootup action); **C6** (§4-step-1 transcript-integrity/corpus-completeness check); **C7** (§4.3 — schema-validation, partial-night handling, regression suite — routed to the Step-4 macro build); **C8** (§0/§4.1/§12 — canonical-write exception bounds stated narrowly). Plus **C9** (§7 scope boundary — work layer vs capture layer; paper production unchanged except deferred shared-registry edits) and **C10** (§6 deliberate-vs-incidental delta split + write-partitioned `Registries_pending/`; §10 records this as a *scoped refinement* of the panel-ratified T2, not an overturn; the read-render realizes §8's anticipated render). Paper-production interaction wired in Patch 2107.

**Remaining gate:** TLA ratifies the v1.0-candidate (or sends it for a confirmatory panel pass) → DRAFT markers come off → canonical. No status moved by the worker.

---

# Round 2 — confirmatory pass (v1.0-candidate, Patch 2108–2109)

**Cycle:** dispatched after 2109; responses integrated Patch 2110 (24 June 2026) · **Panel:** ChatGPT + Grok + Gemini + Copilot · **Outcome in one line:** **RATIFY, 4/4** — every Round-1 concern RESOLVED 4/4, the new R5 (scoped `Registries_pending/` revival) judged **SOUND-REFINEMENT 4/4**; no ratification-blocking new concern. The v1.0-candidate is panel-cleared; the only remaining gate is **TLA's formal ratification** to declare canonical.

## §0. Identity caveat (Round 2)
4 independent reads, attributed by TLA receipt labels. **This round all four self-labels matched the receipt labels** — Gemini's reasoning trace explicitly acknowledged its Round-1 cross-wiring ("I will consistently refer to myself as Gemini") and self-identified correctly. The §4.1 receipt-labelling + in-document IDENTITY instruction held; no mismatch to record.

## Tally

| | ChatGPT | Grok | Gemini | Copilot |
|---|---|---|---|---|
| **OVERALL** | RATIFY | RATIFY | RATIFY | RATIFY |
| R1 Keystone (was T1) | RESOLVED | RESOLVED | RESOLVED | RESOLVED |
| R2 Founder (was T3) | RESOLVED | RESOLVED | RESOLVED | RESOLVED |
| R3 SPOF (was T4) | RESOLVED | RESOLVED | RESOLVED | RESOLVED |
| R4 Seams (was T5) | RESOLVED | RESOLVED | RESOLVED | RESOLVED |
| R5 Pending-revival (NEW) | SOUND-REFINEMENT | SOUND-REFINEMENT | SOUND-REFINEMENT | SOUND-REFINEMENT |

**Every change verified as substantive, not cosmetic** (Copilot and ChatGPT both checked specifically for cosmetic-only integration and found none). The two split/contested Round-1 items closed cleanly: T4 (was 2/2) → RESOLVED 4/4 once durability became a §3.1 requirement and the heartbeat became completeness-aware; T3 → RESOLVED 4/4, including Gemini, who had argued in Round 1 to strike v2 entirely and now judges "never self-graduates + explicit-TLA-enable-only" sufficient ("the machine cannot seize this capability").

## R5 convergence (the new item)
All four independently ruled the scoped revival a **refinement of T2, not an overturn**, for the same reasons: per-window write-partitioning (never a shared target) preserves collision-freedom by construction; it is scoped to *deliberate* precise deltas only (incidental stays collapsed to transcript extraction); the read-render is read-only and answers the same-day ID-allocation problem T2 deferred. The §6/§10 framing was judged accurate and internally consistent.

## Archival cautions (non-blocking; recorded for the panel archive)
- **ChatGPT:** §3.1 now carries substantial load-bearing weight; future governance reviews should treat **implementation verification of §3.1** (always-on / zero-touch / fsync-durable capture) as part of protocol validation, not merely an engineering detail. *(Actionable at the Step-4 / mechanism build.)*
- **ChatGPT:** expects v1-staged to remain the dominant operating mode in practice — consistent with the T3 posture; not a concern, an observation.

## Status
**Panel: RATIFY 4/4 (confirmatory pass clean).** Per the protocol's own gate ("Not canonical until TLA ratifies the v1.0-candidate, or a confirmatory panel pass clears it") the blocker is removed. **The flip to canonical is TLA's status move** — on ratification, the DRAFT markers come off across `capture_and_audit_protocol.md`, the `operating_system.md` §6 wiring (2105) + §4 paper-production discipline (2107), and the bootup heartbeat check.
