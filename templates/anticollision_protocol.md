# Anti-Collision Protocol (lightweight multi-window) — invocation alias

**Location:** `templates/anticollision_protocol.md`
**Invoke:** paste **"run the anti-collision protocol"** into each Claude window when more than one
window is open against the shared tree.
**Status:** ACTIVE. This file is now a **thin alias.** The full, canonical lightweight protocol —
collision surface, the five rules, the interface contract, recovery, the kickoff block, and the
current band map — lives in **`templates/new_window_protocol.md`**. Read that file; this one only
preserves the trigger phrase and gives the per-write quick-reference.

> Why one canonical file: the lightweight protocol used to be split across this file and
> `new_window_protocol.md` with overlapping content. As of Session 161 the substance is consolidated
> into `new_window_protocol.md` (which now carries the Tier-A/B/C collision-file taxonomy and the
> STOP-and-warn 5-step that used to live here). The heavy lease-board mechanism remains separate in
> `parallel_dev/multi_window_protocol.md`.

---

## What invoking this protocol means (quick reference)

Setup it assumes: **one shared working tree, one `origin/main`, one integrator (Thomas).** Every
window is a worker; **only Thomas runs `git am` / `git push`.** Windows generate patches and hand
them over, rebased on current `origin/main`.

**Per contested write** (any Tier-A/B file or another window's owned path — full tier list in
`new_window_protocol.md` §1):

1. **Manifest** every patch (one line per path it touches) before generating it.
2. For any **contested** path: **STOP-and-warn** — name the exact path + line region + change, and wait.
3. Thomas **freezes** that file across windows and replies **"run the check."**
4. **Check:** `git fetch` → sync to current HEAD → re-read the target → rebuild the patch **on current
   HEAD** → present with the apply macro.
5. Thomas **applies immediately** before unfreezing.

**Always:** stay in your own patch band and owned subtree; keep shared-registry edits **batched** into
a flagged integration patch applied after a refresh; and end every patch-delivery reply with a
**last-paragraph collision line**. Recovery on a context error against a clean tree ⇒ stale base ⇒
`git am --3way <file>.patch`.

**Canonical reference:** `templates/new_window_protocol.md`.

## Origin-lag divergence check (adopted Patch 3249, from the Session-149 near-miss)

**Failure mode (observed Patch 3247, first build):** the founder's
outputs-file delivery and his patch application are SEPARABLE acts — he may
paste a dispatch block to reviewers (or otherwise act on a delivered file)
without yet applying/pushing the patch that registers it. `origin/main` then
lags the programme's true state, and a worker sync (`reset --hard
origin/main`) silently drops the worker's own immediately-prior commit from
the base.

**Rule:** before building any patch that DEPENDS on the immediately-prior
patch of the same session, verify the dependency is present on the current
base (`git log --oneline -3` after sync). If origin lags, re-apply the
worker's own staged patch from `/mnt/user-data/outputs/patches/` locally
(`git am`), note the divergence in the commit message, and give the founder
the conditional apply macro (two-patch vs one-patch, keyed on his
`git log --oneline -1`).

**Tripwire that caught it:** the guard-assertion habit (`count(old) == 1`)
on every registry edit. Keep it universal.
