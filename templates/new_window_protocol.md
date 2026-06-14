# CPP Lightweight Multi-Window Protocol

**Location:** `/CPP/templates/new_window_protocol.md`
**Purpose:** The operating rules for running several Claude windows in parallel against the single shared CPP working tree, coordinated by **one operator's serialized attention** rather than by a mechanism. Use this to open a new worker window and to tell each window how to interface with Thomas so collisions don't happen. Includes a fill-in kickoff block (§5) Thomas can paste to spawn a window.
**Status:** ACTIVE — the in-use protocol for day-to-day parallel work (Sessions 156+).
**Last updated:** 14 June 2026.

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

The shared registries (the collision-hot files — never edit casually):

```
theorem-registry.md   predictions.md   master_glossary.md
paper_catalog.md      frontier_sectors/*   parallel_dev/lease_board.md
```

Plus `README.md` / `INDEX.md` and any other window's owned paths.

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
