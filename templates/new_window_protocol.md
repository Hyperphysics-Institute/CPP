# CPP Lightweight Multi-Window Protocol

**Location:** `/CPP/templates/new_window_protocol.md`
**Purpose:** The operating rules for running several Claude windows in parallel against the single shared CPP working tree, coordinated by **one operator's serialized attention** rather than by a mechanism. Use this to open a new worker window and to tell each window how to interface with Thomas so collisions don't happen. Includes a fill-in kickoff block (§5) Thomas can paste to spawn a window.
**Status:** ACTIVE — the in-use protocol for day-to-day parallel work (Sessions 156+).
**Last updated:** 15 June 2026 (Session 161).

> **This is the canonical multi-window reference — read it top to bottom for everyday parallel work.** Its in-session collision-discipline companion, `templates/anticollision_protocol.md` (trigger phrase: *"run the anti-collision protocol"*), is a thin pointer back to this file. The heavy mechanism — lease board + `collision_audit.sh` — lives in `parallel_dev/multi_window_protocol.md` and is only for the escalation case in §0.

---

## Current band map (live windows — operator confirms status)

One century-block per window. Patch numbers are labels (git does **not** enforce them); each window draws **only** from its own band and greps `git log` for the next free number before using it. Consumed singletons stay consumed.

| Band | Window / lane | Notes |
|------|---------------|-------|
| 1000–1099 | Project C — `lambda_qcd_from_planck` | from 1001 |
| 1100–1199 | CC umbrella — `series_cosmological_constant_arc` | from 1101 |
| 1300–1399 | SF-7 grand-unification window | dispatcher of the SF-line windows |
| 1400–1499 | SF-1 charged-leptons window | from 1400 |
| 1500–1599 | SF-3 quark window → **SF-5 successor** | SF-3 v1.3 deposit-ready (closing); SF-5 continues in this band, next free ≈ 1520 |
| 08xx / 09xx | DM lane / chirality lane | earlier arcs — confirm whether still live |

When opening a window, confirm its band's first number is free and **reconcile this map with the operator** — some lanes above may have closed.

---

## 0. When to use this vs. the heavy lease-board protocol

There are two parallel-development protocols in the repo. Pick by who the workers are:

| | **This file — lightweight** | `parallel_dev/multi_window_protocol.md` — heavy (Phase 0 lease board) |
|---|---|---|
| Collision-freedom comes from | one operator's serialized attention + each window's discipline | a **mechanism**: leases + single-writer board + `collision_audit.sh` |
| Overhead | near-zero (no board edits, no audit step) | real (lease assignment, board upkeep, per-round audit) |
| Right when | **Thomas alone** runs all windows and can serialize applies; work is mostly **greenfield** files | untrusted/agentic workers, or multiple windows must edit the **same shared registry concurrently** |
| Failure mode it tolerates | none if the operator is attentive | none even if the operator is careless (that's the point it's proving) |

**Default to lightweight.** Escalate a given round to the heavy board only when two windows genuinely must mutate the **same** shared registry at the same time and the operator can't serialize them. The two protocols are not rivals — lightweight is the everyday mode; the board is the proving ground for the day real workers arrive.

---

## 1. The collision surface (what actually goes wrong)

All windows share **one** working tree (`~/Documents/GitHub/CPP`), **one** `origin/main`, and **one** global patch-number label space. Three things break:

1. **Patch-number collision** — two windows grab the same "next patch" number (observed live: two `0785`s). → Fixed by §2 rule **A** (disjoint bands).
2. **Shared-registry collision** — two windows both append to a registry; the second `git am` conflicts. → Fixed by §2 rules **C/E** (greenfield + defer-and-batch) and the §3 last-paragraph warning.
3. **Stale-base collision** — a window builds a patch on an old HEAD; after an earlier patch lands it no longer applies. → Fixed by §2 rule **D** (refresh before push) and the §4 recovery note.

The shared registries (the collision-hot files — never edit casually), in tiers by contention:

**Tier A — shared root registries + sector frontier files** (any window may need them; the second writer's `git am` conflicts):
`theorem-registry.md`, `predictions.md`, `master_glossary.md`, `paper_catalog.md`, `research_frontier.md`, `future_projects.md`, `README.md`, `INDEX.md`, and every `frontier_sectors/*.md` (`CONJ.md`, `SR.md`, `SM.md` are the most cross-lane — DM + cosmology + CC all touch them).

**Tier B — cross-lane flagship `.tex` hazards** (any flagship two lanes both cite; these also need a **physics sign-off** from Thomas, not just a collision check): e.g. the DP-Sea appendix `series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex`, the SS-1 strong-sector flagship.

**Tier C — coordination:** `parallel_dev/lease_board.md` — single-writer (Thomas only); never write it from a window even in light mode.

A write is **private-lane** (announce in your reply and proceed, no STOP) when it is a brand-new uniquely-named path, or inside your own window's owned subtree, numbered in your own band. **Never edit another window's owned subtree** — propose the change to that window / the integrator instead.

---

## 2. The five rules every window obeys

**A — Own your band.** Each window is assigned a disjoint patch-number band (window → `NNxx`). It draws every patch number from its own band, in order, and **never reuses a label already in `git log`**. Disjoint bands make patch-number collisions impossible by construction. Current band assignments live in the dispatch handover for each window (and informally in the operator's head); the convention is one century-block per window (1300–1399, 1400–1499, …).

**B — Clone-and-grep first.** Line 1 of every window: clone/pull a clean tree, `cd ~/Documents/GitHub/CPP`, and confirm the first number in your band is free (`git log --oneline | grep -E '^[a-f0-9]+ <NNNN>'` empty). No ID registered, file placed, or coefficient computed before this.

**C — Work greenfield.** Produce new own-files under your scope's folder wherever possible. Greenfield files never collide. Reframing/assembly work (e.g., a flagship `.tex` from shipped sources) is naturally greenfield.

**D — Refresh before commit/push.** You produce patches; **you never push autonomously.** Thomas applies them. He will ask you to refresh against `origin/main` before he pushes — especially before any registry edit — because he moves between windows and HEAD may have advanced. After you confirm your patch still applies on the refreshed tree, he pushes with the git macro.

**E — Defer and batch shared-registry edits.** Don't scatter registry edits across patches. Collect them into **one flagged integration patch** at a milestone (a paper ship, a verdict move), applied **after** a refresh. Worker patches touch only the window's own files; the integration patch is where the registry truth lands.

---

## 3. The interface contract — how a window talks to Thomas

This is the heart of the lightweight protocol: **the operator's attention is the synchronization primitive, and the window's job is to make that attention easy to apply correctly.**

> **THE LAST-PARAGRAPH WARNING (non-negotiable).** Any time a task would make you modify a file at collision risk — a shared registry (§1), or another window's owned files — you **state it in the LAST paragraph of your reply**, plainly, so Thomas cannot miss it. Name the exact file(s). Then he serializes:
> - If he's only on this window right now → he applies immediately.
> - If he's been moving between windows → he tells you to refresh (pull `origin/main`) so you rebuild the patch on current HEAD before he applies.

Corollaries:

- **Every patch-delivery reply ends with a collision line** — even if the line is just "Collision watch: new own-file under `<scope>/`, zero risk." Make its absence impossible to overlook by making its presence the habit.
- **No silent registry edits.** If you find yourself about to edit `theorem-registry.md` / `predictions.md` / `frontier_sectors/*` / `master_glossary.md` / `paper_catalog.md`, stop and surface it first.
- **Scope-in-filename for handovers.** Dispatch/handover files go in `handovers/` named `YYYY-MM-DD[_session_NNN]_<scope>.md`. The scope in the name lets a parallel window booting up tell at a glance that a newest-file dispatch belongs to a different window and look back for its own — so one window's dispatch never misdirects another.

### 3.1 Per-contested-write procedure (the STOP-and-warn 5-step)

When a patch *must* touch a Tier-A/B file (or another window's owned path), don't just warn in passing — run this:

1. **Manifest (window).** Before generating *any* patch, post a one-line-per-path manifest of everything it creates/modifies. Private-lane paths: note and proceed. If **any path is contested**, do **not** generate the patch yet → step 2.
2. **STOP-and-warn (window → Thomas).** Name the exact contested path(s) **and the line region** you intend to change, and what the change is. Then wait.
3. **Freeze (Thomas).** On a warn, do nothing with that file in any other window until this window's patch lands. Other disjoint work continues. He replies **"run the check."**
4. **Check + present (window).** "Run the check" = `git fetch origin` → sync to current `origin/main` HEAD → **re-read the target file(s) at current HEAD** → confirm the edit still fits and clashes with nothing new → build the patch **on current HEAD** → present with the apply macro. (Building on current HEAD kills the stale-base collision; re-reading catches a same-file edit another window just landed.)
5. **Apply immediately (Thomas).** Run the macro before unfreezing that file elsewhere. If two windows warn on the **same** file at once, he applies one, then tells the other to re-run the check against the new HEAD.

The honest caveat: this guarantee rests on Thomas **serializing** when he sees a warn — a discipline, not a mechanism (the deliberate trade vs. the heavy board). For 2–3 active windows with one attentive integrator it is sufficient; it is the mode the live SF-line and lane windows already run without a collision.

---

## 4. Recovery — when a refresh shows your base moved

If, after `git pull --rebase origin main`, your patch no longer applies cleanly with `git am`:

- First try the merge engine: `git am --3way <file>.patch`. It uses a real merge and **no-ops correctly if the patch already landed**.
- If it still conflicts, the collision is real: the overlapping file is one another window also touched. Resolve by hand if trivial; otherwise re-derive your patch on the new HEAD and re-deliver. Report the overlap to Thomas so the band/scope assignment can be tightened.

On Windows (Git Bash / MINGW64): case-only renames use `git format-patch --no-renames` (delete+add form); `git am --3way` is the standard recovery path for context errors on a clean tree.

---

## 5. Spawn-a-window kickoff block (Thomas fills this in)

Paste into a fresh window to open a worker. Fill the four `<…>` slots.

```
Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at
https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the
line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any
coefficient (clone the repo and grep the registry first).

This is a parallel worker window under the LIGHTWEIGHT multi-window protocol
(templates/new_window_protocol.md). Read that file's §2 (the five rules) and §3 (the
interface contract) before any work.

- This window's scope:      <e.g. SF-3 quark flagship assembly>
- This window's patch band:  <e.g. 1500–1599>  (confirm first number free via git log)
- Read first, in order:      <dispatch handover path>, then <outline path>, then
                             <structural-core path>, then templates/paper-formatting.md
- Other live windows:        <list — so you know whose territory to avoid>

Rules you obey: own your band; clone-and-grep first; work greenfield; never push
(produce patches, Thomas applies); defer+batch any shared-registry edit into a flagged
integration patch after a refresh; and WARN in the LAST paragraph of every reply whenever
a task needs a file at collision risk (theorem-registry.md, predictions.md,
frontier_sectors/*, master_glossary.md, paper_catalog.md, lease_board.md, or another
window's files). End every patch-delivery reply with a one-line collision watch.

Then tell me what you recommend as the first move.
```

---

## 6. One-line summary

**Disjoint bands + greenfield files + defer-and-batch registry edits + a last-paragraph collision warning on every reply + refresh-before-push.** That is the whole protocol: the operator serializes; the windows make serialization easy and never surprise him with a registry edit.

---

*Companion to `parallel_dev/multi_window_protocol.md` (the heavy lease-board / Phase-0 mechanism). This lightweight file is the everyday operating mode; escalate to the board only when concurrent same-registry edits can't be serialized.*
