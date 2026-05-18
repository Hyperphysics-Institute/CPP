# PD-003: Organizational Frontier Registry and Reflexive-Drop Protocol

**Date:** 24 April 2026
**Session:** SS-8 v0.2 closing phase (post-commit `d8e0b22`)
**Status:** Adopted. Registry established at `/CPP/organizational_frontier.md` with 7 inaugural entries.
**Scope:** Programme-wide — governs the capture, storage, retrieval, and execution of organizational/infrastructural improvement items across all CPP programme work.
**Companion artifacts:**
- `organizational_frontier.md` (the registry itself, structurally parallel to `research_frontier.md`)
- `templates/operating_system.md` §12 "Organizational Frontier Registry" (the operational documentation)

---

## Context

During the SS-8 v0.2 session (24 April 2026), Thomas identified a specific and chronic governance failure mode affecting CPP programme work. The failure mode was articulated as follows (paraphrased from the exchange):

> Every time we do something, we have the option of fractalizing our effort and getting lost in a spiral of ever-branching options and detail. The common response is "handle that in the next session," which becomes "OK, write that out" — and then there is information degradation and focus-priority drift on that end. All these good ideas for programme improvement, sharpening of calculation accuracy, etc. end up risking being forgotten, only to be rediscovered when the failure mode arises again.

The specific failure mode has three components:

1. **Degradation across compaction.** Session handovers preserve pending-item summaries but lose the originating reasoning. "Retroactive README normalization" in a handover list loses the context of *why* (drag-drop misfiling, parallel-edit failures, the 17 existing inconsistencies) unless that reasoning was separately committed somewhere durable.

2. **Single-session scope.** A pending item identified in session 4 that's still pending in session 8 gets re-copied four times, each time slightly paraphrased, each time more detached from original intent. By session 12 it either gets done from momentum or drops off the list entirely as "probably not important."

3. **Retrieval failure.** When a real failure mode recurs — say, a drag-drop misfiling happens again in session 15 — there is no mechanism to say "this was a known failure mode, we already designed the fix, where is it?" The fix lives buried in a pending-list from session 4 that would have to be excavated via chat search or git log archaeology.

## Diagnosis

The programme has registries for two kinds of open items:

- **Theoretical/physics problems:** `research_frontier.md` with `OPEN-SS-N`, `OPEN-SM-N`, etc. entries. Single file, persistent identifiers, reviewed at each paper's completion, individual problems assigned to papers as they become workable.
- **Programmatic decisions once resolved:** `programmatic_decisions/PD-NN-*.md` records what was decided and why, after the fact.

The programme has *no* registry for open *organizational improvements that have been identified but not yet acted on*. Those currently live in exactly one place: the closing "Pending for next session" list of each session's final message. This list has the three failure modes above.

The diagnosis suggests the solution: parallel `research_frontier.md`'s approach at organizational scope. A single file, `OPEN-ORG-NNN` persistent identifiers, structured entries with enough context to act on without session-memory reconstruction, reviewed at programme milestones.

## The critical design element: trigger conditions

Most organizational improvements don't need to be done immediately; they need to be done *at the right moment*. The value of capturing them in a registry only manifests if future sessions can reliably identify which items have become workable without re-deriving their context.

The registry adopts three natural trigger types:

1. **Between-paper trigger.** "Do this during any gap between paper-drafting sessions. Low urgency, low dependency, pure infrastructure." Example: README normalization. These items can accumulate and batch.

2. **Threshold-triggered.** "Do this when programme state crosses a specified threshold." Example: restructure `operating_system.md` when it exceeds ~1500 lines. Avoids the false-priority trap where infrastructure work gets done before anyone needs it.

3. **Opportunistic / combine-with.** "Do this combined with some other work that's going to happen anyway." Example: SS-7 script refactor combined with SS-7 subfolder migration. Piggybacks on existing work rather than requiring its own session slot.

4. **Milestone-triggered.** "Do this when the programme reaches a specified milestone." Example: swarm-tally header in `predictions.md` before SS-9 drafting begins.

5. **Next-session.** "Do this immediately at the next available opportunity." Rare — used for items where recurring friction makes deferral costly.

The trigger condition is what distinguishes the registry from a generic "TODO list." A TODO list demands attention each time it's reviewed (should I do this? is it still relevant?). A trigger-condition registry can be scanned in 60 seconds against current state, with all non-fired items remaining silent.

## The reflexive-drop protocol

The operational discipline the registry supports: when an organizational improvement idea surfaces during active work, the correct action is not to act on it immediately (disrupting current scope) nor to carry it in session memory (losing it to compaction), but to:

1. Stop for 60–90 seconds
2. Open `organizational_frontier.md`
3. Add an entry using the template — with full fidelity reasoning, not a summary
4. Commit (or stage for the next batched commit)
5. Return to current work

The attention loop closes immediately at step 5; the infrastructure loop was closed at step 3–4. The idea is preserved at full fidelity; the current session's focus is not disrupted.

This is structurally identical to how theoretical problems already work. When an SS-8 drafting session notices that D3 deserves its own first-principles derivation, it doesn't pause SS-8 — it registers OPEN-SS-28, notes that SS-9 or SS-10 will address it, and returns to SS-8. The registry machinery makes the preservation cheap.

## Relationship to existing handover mechanism

The "Pending for next session" list at the close of each session continues to exist, but its role changes. Previously: primary storage location for pending items, with all context inline. Now: short pointer list referencing entries in `organizational_frontier.md`, without content duplication. A session-close handover reads:

> OPEN-ORG registry current; OPEN-ORG-{N} became workable this session (deferred due to time); OPEN-ORG-{M} newly registered this session. Next session should scan registry against current state.

Not:

> Pending items: retroactive README normalization (17 files need renaming because the convention is new and some used underscores, some used leading-README format, and there are three different conventions, and the data one is the only correctly-named one currently...).

The content lives in the registry file (durable, retrievable, version-controlled). The handover just points at it.

## Inaugural population (7 entries, 24 April 2026)

The registry is populated on creation with seven entries covering pending items accumulated across SS-7 v1.2, SS-8 v0.1, SS-8 v0.2, and the PD-001 through PD-003 governance work of the last four sessions. Each entry is written at full fidelity — originating context, problem, proposed fix, trigger condition, dependencies, history — rather than summarized, because the reasoning behind each one is currently in Claude Opus's session memory and will degrade at compaction if not captured.

The seven inaugural entries:

1. **OPEN-ORG-001:** Retroactive README naming normalization (17 files across three inconsistent conventions)
2. **OPEN-ORG-002:** `operating_system.md` restructuring when it exceeds ~1500 lines
3. **OPEN-ORG-003:** `predictions.md` cumulative swarm-tally header (required before SS-9 drafting)
4. **OPEN-ORG-004:** SS-5, SS-6, SS-7 migration to per-paper subfolder convention
5. **OPEN-ORG-005:** Retroactive §4.1A (CP/GP Signature) and §4.1B (Swarm-Validation) subsections in existing papers
6. **OPEN-ORG-006:** SS-7 script refactor — AME 2020 loader-based rather than hardcoded values
7. **OPEN-ORG-007:** Repository-level `.gitignore` for Python build artifacts (`__pycache__` recurrence)

Each is registered with a specific trigger condition: between-paper, threshold-triggered, milestone-triggered, opportunistic, or next-session.

## Programme-level significance

This decision codifies the programme's answer to a governance question that parallels the one PD-001 and PD-002 addressed:

- **PD-001** answered: *How do we maintain the programme's epistemological strategy across many papers?* (CP/GP signature and swarm-validation required subsections.)
- **PD-002** answered: *How do we maintain integrity of empirical claims in a multi-AI review environment?* (Three-tier verification taxonomy.)
- **PD-003** (this decision) answers: *How do we prevent the programme's organizational ideas from degrading or being lost as work volume accumulates?* (Structured registry with trigger conditions and reflexive-drop protocol.)

All three share the same underlying design principle: **durable infrastructure beats session memory.** Session memory is high-fidelity but ephemeral. File-based infrastructure is lower-fidelity per-bit but persistent, versioned, searchable, and retrievable. The correct trade is to capture the reasoning while it's high-fidelity (reflexive-drop into the registry at the moment of insight), then retrieve at lower-fidelity later (scan against current state, act when triggered). The registry is the translation layer between the two.

## The meta-irony noted

This decision is itself a piece of governance-infrastructure accretion of exactly the kind that triggered the need for the registry in the first place. Claude Opus flagged this irony during the design conversation, and Thomas approved proceeding anyway on the grounds that PD-003 creates a *container for* governance-infrastructure items rather than being one more governance-infrastructure item itself (it's a meta-tool, not another rule).

That said, the registry itself can grow unwieldy at sufficient scale. If OPEN-ORG grows to hundreds of entries, a consolidation pass will be needed, and the registry may need its own restructuring — an irony noted here so that future sessions can see the meta-level was anticipated from the start. The expected lifecycle: 10–50 entries for years, consolidation/archiving at 100+, structural restructuring at 250+.

## Implementation path

1. **This decision record** (`programmatic_decisions/PD-003-organizational-frontier-registry.md`) — committed in the same patch that establishes the registry.
2. **`organizational_frontier.md`** at programme root — created and populated with 7 inaugural entries at full fidelity.
3. **`templates/operating_system.md` §12 "Organizational Frontier Registry"** — operational documentation for reflexive-drop protocol, entry template, review cadence, and registry-maintenance protocol. Part of the same patch.
4. **Future sessions** — use the reflexive-drop protocol when organizational ideas surface. Session-close handovers become pointer lists rather than content-duplication lists.
5. **Future paper milestones** — registry reviewed at each v1.0 milestone alongside `research_frontier.md`. Entries whose triggers have fired get queued for execution; items accumulate resolutions in §3 of the registry file.

## Forward discipline for Claude (any future Opus)

When the following patterns occur during active session work, the correct response is reflexive-drop, not defer-to-handover:

- "We should eventually X" → register OPEN-ORG-NNN, return to current work.
- "This is a good idea but out of scope now" → register OPEN-ORG-NNN, return to current work.
- "Noting this for later" → register OPEN-ORG-NNN, return to current work.
- "Future Opus should Y" → register OPEN-ORG-NNN, return to current work.
- "At some point we need to Z" → register OPEN-ORG-NNN, return to current work.

Each of these phrases, when uttered in a session, is a signal that an organizational improvement has been identified but is about to be carried in session memory instead of in durable infrastructure. The correct response is always the same: spend 60–90 seconds, register the entry at full fidelity, return to the work you were doing. The cost is small; the degradation risk is eliminated.
