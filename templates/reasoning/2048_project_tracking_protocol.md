# Reasoning capture — Patch 2048: project-tracking protocol (the per-patch ledger)

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.

Thomas pushed back on my status-ladder framing and was right to. He told me, plainly, that verdict-shifts
aren't the marker that helps him restart a half-finished project after a dozen windows have touched things —
the granular per-patch trail is. I took his design over mine: a per-patch ledger with an "every turn, no
exceptions" rule, because that has no judgment gap (the judgment about "is this a status-change" is exactly
what failed me at 2047).

The one improvement I folded in: don't hand-maintain the ledger. A shared file every window edits every patch
is the hottest collision surface in the repo AND the same drift-bug we just hit, one level up. But git history
already IS the per-patch, every-window, append-only, collision-free ledger. So: tag each commit with a `Track:`
trailer (cheap, local, zero contention) and render the project-grouped view from git on demand. This gives
Thomas everything he asked for — one location, every patch, every window, grouped by project, last-patch-per-
track — with MORE "every turn" reliability (mechanical) for LESS overhead (no shared-file edit), and it can't
drift-lie: a stale render is just old, refreshable in one command. The git history is the truth; the .md is a
cached view.

## FOUNDER CONTRIBUTION (verbatim — TLA, 23 June 2026)
> what feels more robust is a list that captures a short summary of every patch at every turn... if it's done
> at every turn, it becomes pretty reliable, and when there is a check on the progress of any project, the
> entire development track can be tracked in one location... I haven't seen the project status shifting states
> to be a significant marker that would help us start in the middle of a half-finished project... but the
> mention of a project always being tracked, along with knowing what the track was and the last patch worked
> on, makes scanning the relevant records very granular, and the ability to restart, add in all the insights
> from a dozen different windows, integrate, and continue... that seems really useful.

This is the design call that shaped the protocol: per-patch granularity over status-state as the restart
marker. Promoted to founders_vision pending (sweep will catch it).

First applications in this patch: created the protocol + render script + a snapshot ledger; bumped
R2-STATUS.md's own stale header ("2010/REVISE" → current "2041/conditional-PASS") — the exact sub-bug the
protocol forbids; and pointed operating_system.md at the protocol so all windows inherit it. The OPEN-SR-9
scope file's stale progress notes (the other live instance) are owed the same pointer-not-restate treatment —
flagged for the SR-9 window, not edited here (their territory).

NO THEO. Tier-A this patch: operating_system.md (canonical), R2-STATUS.md (status header). Owned: protocol,
script, ledger snapshot, this fragment.

Track: WORKFLOW
