# Reasoning capture — Patch 2119: low-friction per-turn capture helper (cap.sh) + fragmentation hook

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

## FOUNDER CONTRIBUTION (verbatim — TLA, 2026-06-25)
> "I am trying to capture everything. Every round, capture every word. I realize this is maximum friction, but I
> think it will save time in the long run because I spend so much time trying to reprogram and implement more
> solutions that don't work; at least we would have something that works."

TLA chose per-turn, every-word capture, accepting friction, explicitly preferring a working thing over repeated
re-engineering. Honored the decision; added one refinement that preserves "every word" while cutting per-turn cost
from a full git cycle to a single command.

Built:
- `scripts/cap.sh` — sourced from ~/.bashrc. `cap` reads /dev/clipboard (Git Bash exposes it) and appends the
  copied turn block to today's `Development/transcripts/<date>_session_<slug>.md` (front matter auto-created on
  first call); `cap-push` commits+pushes the day's transcript once at session end; `cap-slug` tags a session.
  Per-turn loop = copy the worker's end-of-reply block, type `cap`. No pull/push/conflict per turn.
- `bootup.md` — transcript fragmentation hook: if an un-fragmented session transcript is present, a window
  fragments it (deterministic split = macro; rich split = AI pass over the transcript -> categorized fragment
  patches staged for review), then writes `<transcript>.fragmented`. This is the "morning command" TLA asked for.

Honest division recorded: per-turn capture from chat REQUIRES a per-turn TLA action (the only door from a
non-persistent chat worker to TLA's disk is something TLA runs); cap.sh makes that action minimal. The worker
prints a ready-to-copy verbatim turn block at the end of each reply (its own answer captured as prose; the
delivery block omitted to avoid recursion). Forward-only; cannot recover compacted past turns.

NO THEO. Owned this patch: `scripts/cap.sh`, `bootup.md` hook, this fragment. No status move; no canonical value
changed. Next: worker emits the per-turn capture block each reply; DM-1 resumes (0859 pivot, loop-size linchpin).

Track: WORKFLOW
