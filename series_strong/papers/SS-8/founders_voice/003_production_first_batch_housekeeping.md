# Founders Voice 003 — Production first, batch housekeeping at natural seams

**Date:** 22 April 2026
**Session:** SS-8 D1 attack — commit-cadence decision
**Thomas's response to Claude's two-tier (Preservation/Milestone) commit proposal**

---

**Claude's overcomplicated proposal:**

> *Two-tier formulation: Tier P (preservation) triggered by reviewer-cycle settlement / context pressure / session end with substantive work on disk. Tier M (milestone) triggered by paper freeze / version bump / registry change / external submission.*

**Thomas's simpler principle:**

> I was merely saying that we have set aside items with a "Publish this later/at a trigger point" setting. The clearing out I was referring to was simply removing the tag to publish that item, which had been set aside for writing and presentation. Simply removing the tag to print later was all I meant.

> Production/taking territory is more important than documentation. We have a lot of physics to cover. Delay the housekeeping until it can be batch-processed in a session, preferably at the end of the theoretical proof/target section of each paper, or when we have to switch context windows, cause it gets lost/abbreviated/changed/extrapolated if we wait till the next context window.

---

## Why this matters

Claude had proposed a triggering framework with four trigger types across two tiers — reviewer-cycle settlement, context pressure, session end with work on disk, paper freeze, version bump, registry change, external submission. Thomas's version had two triggers: section-end (substantive physics target complete) and context-pressure (before compaction, to prevent summary-loss).

Thomas's reasoning made two structural points that reshaped operating_system.md §11:

1. **Reviewer-cycle settlement is not a commit trigger.** A single reviewer round closing doesn't justify a commit if the work is mid-attack. This kept commits tied to physics-delivery milestones rather than workflow events, which kept the commit history aligned with what was actually accomplished.

2. **Context-pressure commits are mandatory, not optional.** The clause "cause it gets lost/abbreviated/changed/extrapolated if we wait till the next context window" is the reason the context-pressure preservation checklist in operating_system.md §11 explicitly requires four artefact classes be committed before compaction — curated transcript, registry updates, reviewer letters, protocol/op-sys updates produced in session. Transcript summaries are lossy; git commits are verbatim.

The underlying principle: **production is primary, housekeeping is secondary but not optional at session seams.** This is scope discipline applied to the programme's own meta-work.

## Application to the three documentation hierarchies

This principle, extended in a later session, generated the three-hierarchies rule in operating_system.md §11. Section-end commits should sweep all three hierarchies (per-paper docs / programme-level registry / templates-and-conventions) — not to fabricate updates, but to verify that real updates aren't being skipped. The sweep is the discipline; the hierarchy check prevents drift.

## Pattern to record

Thomas's "production first" phrasing is consequential. It's not "neglect documentation"; it's "sequence documentation behind physics but commit fully at natural seams." Claude's tendency to over-engineer trigger frameworks was corrected by this simpler principle with better scaling properties — the simpler rule generalizes to other workflow questions (when to update registries, when to migrate file structures, when to write documentation-suite companions) in ways the four-trigger framework wouldn't have.
