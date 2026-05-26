# Handovers

This folder holds all CPP handover documents in one place. **One folder, one convention, sortable filenames.**

## Quick rule

**At session bootup, open this folder and read the most recent file.** That's the canonical "what's next" pointer for the programme. If the most recent file is paper-scoped or trajectory-scoped and doesn't match the work you're doing, look back at the previous most-recent file with matching scope.

## What's a handover?

A handover document is a forward-looking artifact written at a session close, paper milestone, or trajectory milestone to orient the next context window. It states:

- **Current state** — what shipped, what's pending, where we are
- **Immediate next priority** — the first piece of work the next session should pick up
- **Bootup instructions** — what files to read first, what's the framing question, what to avoid
- **Trajectory expectation** — how many sessions to closure, what comes after

It is **not** a session log (those go in `session_logs/`), **not** a development vignette (those go in `flagship_papers/*/documentation_suite/development-*.md` or `series_*/papers/*/documentation_suite/development-*.md`), and **not** a transcript (those go in `documentation_suite/transcript-*.md`). A handover is the forward-pointing summary; the historical record lives elsewhere.

## Naming convention

```
YYYY-MM-DD_session_NNN_<scope>.md
```

- **`YYYY-MM-DD`** — programme date of the session being handed off (not the file commit date if they differ; the session is the authoritative anchor)
- **`session_NNN`** — three-digit session number with leading zeros for chronological sort within a date. Omit `session_NNN` only for legacy files where session number is ambiguous (pre-Session-numbering-codification handovers); use `YYYY-MM-DD_<scope>.md` for those.
- **`<scope>`** — short snake_case descriptor. Examples: `programme` (no specific paper/trajectory), `capotauro_v1.0_ship`, `sf4_v4.4_archival`, `reading_c_closure_trajectory`, `ss-9_v1.0_ship`. Use lowercase and hyphens for paper IDs (`ss-9`, not `SS-9`).

The naming gives you sortable + scoped names. `ls handovers/` shows chronological order; the last entry is the most recent. Scope appears in the filename so you can tell at a glance what each handover covers without opening it.

## When to write a handover

Per `templates/operating_system.md` §15 "Session-close Handover Protocol", handover writing fires on either of two triggers:

- **User-initiated**: Thomas says "execute handover protocol" or a minor variant
- **Claude-initiated prompt**: at workflow-shape signals (milestone completed, long session, "good stopping point" cues), Claude asks "Do you want to initiate handover protocol?"

Most sessions do NOT produce a separate handover file. The default convention from §4 is **session-log-as-handover-backbone**: for ongoing-work sessions, append to `session_logs/[YYYY-MM-DD]_session_log.md` and the session log sequence IS the handover. Write a separate handover file in this folder only when:

- A paper reaches v1.0 SHIP or major archival milestone (one handover per such milestone)
- A multi-session closure trajectory makes substantive advance (like the Reading C three-patch arc on OPEN-FI-C-9-FP-MECHANISM)
- A programme-wide juncture warrants explicit forward-pointer (rare; the SESSION_36/54/81 legacy handovers were of this kind)
- Thomas explicitly requests one

## Migration history

This folder was created 17 May 2026 (Session 127 Patch 0422). Before that, handover files were scattered across:

- Root level: `SESSION_36/54/81_HANDOVER_FOR_NEXT_CONTEXT.md` (programme-wide milestones)
- `flagship_papers/<paper>/documentation_suite/handover-<paper>.md` (per-paper)
- `flagship_papers/<paper>/sketches/<trajectory>_handover.md` (per-trajectory; new convention as of Patch 0421)
- `series_<x>/papers/<id>/documentation_suite/handover-<id>.md` (per series paper)
- `session_logs/OPEN-<X>_handover.md` (per open problem; one instance)

This scattering made handover discoverability poor: a new context window had to guess which scope of handover to look for and where each scope lived. The migration consolidated all existing handovers into one chronologically-sorted folder under a single naming convention.

Existing cross-references in historical documents (session logs, transcripts, development vignettes) still point to the old paths. Those references are preserved as historical record; readers following them should find the new location via this README's correspondence table below.

## Migration correspondence table

| Old path | New path |
|---|---|
| `SESSION_36_HANDOVER_FOR_NEXT_CONTEXT.md` | `handovers/2026-05-07_session_036_programme.md` |
| `SESSION_54_HANDOVER_FOR_NEXT_CONTEXT.md` | `handovers/2026-05-09_session_054_sf4_v1.0_ship.md` |
| `SESSION_81_HANDOVER_FOR_NEXT_CONTEXT.md` | `handovers/2026-05-11_session_081_sf2_campaign_launch.md` |
| `series_umbrella/series_substrate_chirality_arc/capotauro/documentation_suite/handover-capotauro.md` | `handovers/2026-05-16_session_122_capotauro_v1.0_ship.md` |
| `series_umbrella/series_substrate_chirality_arc/capotauro/sketches/Reading_C_closure_trajectory_handover.md` | `handovers/2026-05-17_session_127_reading_c_closure_trajectory.md` |
| `flagship_papers/electroweak/documentation_suite/handover-SF-2.md` | `handovers/2026-05-14_session_083_sf2_v1.0_ship.md` |
| `flagship_papers/neutrinos/documentation_suite/handover-SF-4.md` | `handovers/2026-05-11_session_081_sf4_v4.4_archival.md` |
| `series_strong/papers/SS-7/documentation_suite/handover-SS-7.md` | `handovers/2026-04-21_ss-7_v1.2.md` |
| `series_strong/papers/SS-8/documentation_suite/handover-SS-8.md` | `handovers/2026-04-25_ss-8.md` |
| `series_strong/papers/SS-9/documentation_suite/handover-SS-9.md` | `handovers/2026-05-07_session_035_ss-9_v1.0_ship.md` |
| `session_logs/OPEN-SS-24_handover.md` | `handovers/2026-04-26_open-ss-24_trajectory.md` |

## Folder contents discipline

This folder is **append-only at session/milestone close**. Files are not edited after the session they were written for; if a handover's forward queue changes, write a new handover file at the next session close rather than editing the old one. The old file is preserved as the historical handover state at the moment it was written. This ensures the chronological-sort-by-filename property continues to work: the newest file is the current canonical handover.

The single exception is fix-ups within the same session the file was written for (typo corrections, formatting fixes, etc.). Substantive content changes should not be retroactively applied to handover files.

---

*Folder created 17 May 2026 (Session 127 Patch 0422). Convention codified in `templates/operating_system.md` §15.*
