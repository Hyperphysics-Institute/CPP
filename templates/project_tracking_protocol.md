# Project-Tracking Protocol — the per-patch development ledger

**Location:** `templates/project_tracking_protocol.md`
**Status:** ACTIVE (Patch 2048, 23 June 2026).
**Why it exists:** a window booting on a half-finished track — after a dozen other windows have touched
things — needs to see, in one place, the whole development trail of that track: every patch, in order,
across all windows, and the last patch worked. The failure that motivated this (Patch 2047): a *hand-written
summary* (the OPEN-SR-9 scope file) lagged the real ladder and stated a verdict three patches stale, and a
reader trusted the stale summary. The fix is to stop trusting hand-written summaries as the source of truth.

---

## The one idea

**Git history IS the canonical per-patch ledger** — every patch is one commit, every window pushes to the
same `main`, it is append-only and collision-free by construction, and it already exists. We don't build a
second ledger that can drift; we **tag each commit with its track** and **render** the project-grouped view
from git on demand. The rendered file (`project_ledger.md`) is a *cached view*, never the source of truth:
a stale render is never *wrong*, only *old*, and refreshing is one command.

This is the same shape as reasoning-capture and founder-contribution: a cheap, mandatory, per-patch
discipline that rides the work instead of being a separate thing to remember.

## The discipline (per patch — mandatory, every window)

1. **Tag the commit with its track.** Add a trailer line to the commit message body:
   ```
   Track: R2
   ```
   Use the project's short canonical name (R2, DM-2, SR-2, EU-1, Project-C, DSL, SF-5, Chirality, WORKFLOW…).
   A patch that genuinely spans two tracks may carry two `Track:` lines. Routine no-op turns (no commit)
   tag nothing. **This is element 6 of the per-patch contract** (alongside `.tex`/finding + reasoning
   fragment + verify script + the founder-contribution block + the collision line).
2. **That's the whole per-patch cost.** No shared file is edited; the tag lives in your own commit, so there
   is zero cross-window contention. The trailer is what makes the rendered ledger group cleanly; without it
   the renderer falls back to inferring the track from the paths the patch touched (works, but coarser).

## The render (on demand / at checkpoints — collision-free)

`scripts/render_project_ledger.py` reads git log and writes `project_ledger.md`:
- a **Dashboard** — last patch worked per track, most-recent first (the "where is everything" view);
- **Full trails** — every patch per track, in order (the "what happened on this track" view).

Run it any time: `python3 scripts/render_project_ledger.py` (optionally `--max N` for depth). Because it is
*derived*, two windows never collide on it — if it's out of date, regenerate. **Commit a refreshed
`project_ledger.md` at the collision-safe checkpoints only** (handover, paper-production audit, or on
request when other high-collision shared files are being updated) — never per-patch, since the per-patch
currency already lives in git via the trailer. Check `git pull` first before committing a refresh.

## Single source of truth (the rule that prevents the 2047 bug)

- **Git history is the trail's truth.** `project_ledger.md` is a render of it.
- **Per-track status files** (e.g. `R2-STATUS.md`) remain valuable for the *current standing + next step* of
  a verdict-bearing track — but they obey two rules: (a) a **current-status top-line that is bumped on every
  status-moving patch** so it always equals the latest ladder entry (the 2047 sub-bug was R2-STATUS's header
  reading "2010 / REVISE" over a ladder that had reached "2041 / conditional-PASS"); and (b) append-only
  history below the header.
- **Every other file points; it does not restate.** Scope files, `frontier_sectors/*`, `CONJ.md`, `README`
  carry a **pointer** to the status ladder, never a duplicated verdict. A pointer can't go stale when the
  verdict moves; a restated verdict can. Duplicated verdicts are the drift surface — forbid them.

## Cross-track forks (insights that belong to another project)

Work on one track routinely throws off something for another. Two cases, two homes:
- **An owed *action* on another track** → a `todolist.md` TODO (existing mechanism).
- **A *status/verdict change another track depends on*** → write the cross-reference into **both** tracks'
  ledgers/status at once (a one-line "→ affects DM-2: …" in this track and the mirror in DM-2), so a
  dependency cannot move on one side without the other side seeing it. Lighter than a central dependency
  graph, and it fails safe.

## One-line summary

**Tag every commit with `Track:`; render the project-grouped ledger from git on demand; keep status-file
headers current and make every other file point to the ladder rather than restate the verdict.** The git
history is the one append-only, collision-free, all-windows ledger we already have — this protocol just makes
it readable per project and forbids the hand-written summaries that drift.
