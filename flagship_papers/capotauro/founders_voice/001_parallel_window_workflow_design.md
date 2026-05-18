# 001 — Parallel-Window Workflow Design

**Date:** 16 May 2026 (Session 123)
**Speaker:** Thomas Lee Abshier ND
**Context:** Session 123 opened with the retroactive §15 handover work for the Session 122 close that had not produced a Step H artifact. The previous context window had also produced the Patch 0416 retroactive handover + the registry drift fix at Patch 0416A. The question of forward sequencing was open: complete Section E + Section A documentation sequentially in one window, or split work across parallel windows. Thomas proposed the parallel-window approach. This is the methodological innovation that structured the subsequent twelve-patch Capotauro doc-suite catch-up arc (Patches 0416B–0416M) and the parallel physics-window Reading C closure work (Patches 0417+). The pattern is new in the CPP corpus — SS-7, SS-8, SS-9, SF-4, SF-2 campaigns all ran serially.

---

## Thomas's articulation (verbatim)

> "Ok, we are back on track now.
> Here is my proposal:
>
> * I open the handover document in another context window and start working on new physics.
> * I continue working in this context window to do the full documentation suite.
> * The session numbers in this documentation series are numbered 416 A, B, C... AA, BB, CC.. until completed.
> * I will switch back and forth, and that way catch up with the documentation during the processing times when you are working on new physics.
> * Will that work?"

---

## The structural insight, distilled

The parallel-window workflow rests on three observations:

**(1) Documentation work and substantive physics work have asymmetric AI engagement.** When Claude is producing the Capotauro Section E + Section A documentation suite, the work is text generation against a stable physics state (the v1.0 SHIPPED paper). When Claude is doing substantive Reading C closure work on the Q1 group-theoretic verification (or downstream Q1' direction-class resolution), the work is reasoning-intensive theorem-development against a moving frontier. Running these two workstreams sequentially in one context window forces Thomas to wait while one finishes before the other can start.

**(2) Patches naturally serialize into letter-suffix vs integer streams.** The documentation arc's patches are not numbered against the substantive physics work because they don't change scientific content — they are post-SHIP doc production. Letter-suffix patches (0416A, 0416B, ..., 0416M) are the natural namespace for the docs arc; integer-suffix patches (0417, 0418, ...) continue to serve the physics arc. The two namespaces compose without conflict so long as push-pull discipline on shared registry files holds.

**(3) Shared-file conflict is rare and locally fixable.** The two workstreams touch mostly disjoint file sets — documentation files for the docs arc, working sketches and registry entries for the physics arc. The only realistic overlap is `changelog-capotauro.md` (and possibly `master_glossary.md`, `research_frontier.md`, or `theorem-registry.md`) if both arcs need register updates in the same window. The discipline that handles this is push-pull: whoever finishes a patch first pushes immediately; the other window pulls before its next patch.

## The push-pull discipline (developed across the Session 123 arc)

The parallel-window workflow ran cleanly through Patches 0416B–0416M with one observed coordination collision (the physics window's Patch 0417 was pushed between the docs window's Patch 0416G and Patch 0416H apply attempts, causing the docs apply to rebase onto a state that included the physics work). The rebase was clean because the touched files were disjoint at that moment. The collision was empirically resolvable by checking `git log origin/main --oneline` and seeing which patch was at HEAD on origin.

A minor coordination glitch was observed: the physics window's Patch 0417 commit message claimed three drift items were still pending, but they had actually been shipped in the docs window's Patch 0416A. The physics window had read the handover and not noticed the drift had been fixed. This is the expected cost of parallel-window workflow — the handover state at the start of a window's work is the snapshot it acts on, and that snapshot can become stale during the window's lifetime. The right discipline is: the receiving window's commit message should not make claims about other workstreams' states beyond what was true at the time the window opened. The docs window's commit messages did not make claims about the physics window's state; the physics window's commit message did and was partially incorrect. The asymmetry suggests the windows should be informed of cross-arc state at apply time (via `git log` inspection in the handover-bootup step), not relied on handover state to remain current.

## Generalizable pattern

The parallel-window workflow with letter/integer namespacing and push-pull discipline is a programme-wide methodological innovation, not a Capotauro-specific accommodation. It applies whenever a flagship paper reaches v1.0 SHIP and the post-SHIP work splits into (i) documentation-suite production, which is bounded scope and stable substrate, and (ii) substantive forward physics, which is unbounded scope and moving substrate. The proposed convention going forward:

- Letter-suffix patches (N A, N B, N C, ... N Z, N AA, ...) for the documentation arc post-v1.0 SHIP
- Integer-suffix patches (N+1, N+2, ...) for the substantive physics arc post-v1.0 SHIP
- Push-pull discipline on shared registry files (`changelog-X.md`, `master_glossary.md`, `research_frontier.md`, `theorem-registry.md`)
- Each window's commit messages should restrict claims to what was true at the window's open, not what is currently true on origin
- Apply-time `git log` inspection is the canonical signal for which patch is at HEAD when conflicts seem likely

The convention is codifiable in `templates/operating_system.md` as an addition to §15 or as a new §17 Parallel-Window Workflow Discipline. Codification should follow the discipline-tightening-after-precedent principle: the Capotauro arc is the first precedent; one more flagship at v1.0 SHIP using the same pattern would make the codification credible.

---

*This file is a Tier-1 founders_voice artifact per `templates/operating_system.md` §4 Four-Tier Documentation Discipline. The verbatim quotation is from the Session 123 docs-arc transcript at `/mnt/transcripts/2026-05-17-03-24-56-capotauro-v10-docsuite.txt` (Human message turn 2).*
