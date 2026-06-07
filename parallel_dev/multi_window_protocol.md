# CPP Multi-Window Parallel Development — Phase 0 Protocol

**Location:** `/CPP/parallel_dev/multi_window_protocol.md`
**Purpose:** The operating procedure for Phase 0 of the parallel-development roadmap — one human (Thomas) running multiple Claude windows as simulated workers against the single shared working tree, with **mechanically guaranteed** collision-freedom. This is the staging ground; once Phase 0 passes GATE 0, this procedure is folded into `operating_system.md` as the canonical worker protocol (per `parallel_development_roadmap.md` Phase 2). It is **not** a second operating system.
**Status:** PHASE 0 — proof of concept. No human or agentic worker beyond Thomas is onboarded until GATE 0 passes.
**Last updated:** 6 June 2026 (Session 154)

---

## What Phase 0 proves (GATE 0)

> Three windows, three distinct theorems, **zero collisions, clean integration, verified by audit.**

"Verified by audit" means `parallel_dev/scripts/collision_audit.sh` returns PASS over the round's commit range. A round passes GATE 0 when, for that round:
1. no two worker commits touched the same worker file,
2. no two commits carry the same patch-number label,
3. no duplicate new IDs were registered (reviewed), and
4. the tree is clean and all patches are pushed.

The thesis being tested: collision-freedom comes from the **mechanism** (leases + a single-writer board + an audit), not from the operator being careful. If it only works when Thomas is careful, it will not survive real workers.

---

## The collision surface (what actually goes wrong)

All windows share **one** working tree (`~/Documents/GitHub/CPP`), **one** `origin/main`, and **one** global patch-number label space. The real-world failure modes:

- **Patch-number collision** — two windows both produce "the next patch" and grab the same number. *(Already observed in live history: two commits labeled `0785`.)*
- **Shared-registry collision** — two windows both append to `theorem-registry.md` / `predictions.md` / `frontier_sectors/*` / `master_glossary.md`; the second `git am` conflicts.
- **Stale-base collision** — a window builds its patch on an old HEAD; after an earlier patch lands, it no longer applies cleanly.
- **ID / terminology collision** — two windows register the same ID, or name the same concept differently.

Phase 0 closes each of these by rule, below.

---

## Roles

- **Integrator (Thomas, exactly one):** the *single writer* of the lease board and the *only* party that runs `git am` / `git push` / the audit. All integration funnels through one person — this is the whole-theory coherence anchor.
- **Worker window (one Claude conversation = one worker):** owns exactly one theorem and a declared set of files for the round. Reads the board; never writes it; reports status back to the integrator in chat.

---

## The lease board (single writer)

`parallel_dev/lease_board.md` is the coordination ledger. It has **exactly one writer: the integrator.** Worker windows read it to learn their lease; they propose changes in chat and the integrator records them. This single-writer rule is what stops the board itself from becoming a collision point — do not ask a worker window to edit the board.

The board is **ephemeral coordination state, not a registry.** It records who-owns-what *right now*; it never holds physics truth (that lives in `theorem-registry.md`, `predictions.md`, `frontier_sectors/`, etc.).

Each round, the board assigns every active window: a **theorem**, a **disjoint patch-number range**, and an **owned file/path set**.

---

## Round lifecycle (the core procedure)

**Step 1 — Assign (integrator).** Pick the round's theorems. On the lease board, give each window: a theorem, a disjoint patch-number range (e.g. W1 → 0790–0792, W2 → 0793–0795, W3 → 0796–0798), and the file/path set it owns (normally its own theorem folder). Owned sets must be pairwise disjoint.

**Step 2 — Dispatch (integrator → each window).** Open one Claude window per theorem. Give each its lease line verbatim. Each window then:
- honors the **CLONE-FIRST GATE** (clone + grep the registry before registering an ID, placing a file, or computing a coefficient);
- works **only** within its owned paths;
- numbers its patches **only** within its leased range;
- **defers all shared-registry edits** (see Step 4) — a worker patch adds/edits files in its own theorem folder and nothing in the shared registries.

**Step 3 — Apply in board order (integrator).** Apply each window's patch(es) in the order listed on the board, one at a time, with the standard chain:
```
cd ~/Documents/GitHub/CPP && git pull origin main && git am ~/Downloads/<file> && git push origin main
```
Because owned sets are disjoint and registries are frozen, these never conflict. If a patch was built on a stale base, recover with `git am --3way` (the Windows recovery path).

**Step 4 — Batched registry integration (integrator, one patch).** After the worker patches land, apply a **single** integration patch that propagates all the round's shared-registry updates (`theorem-registry.md`, `predictions.md`, `frontier_sectors/*`, `master_glossary.md`, etc.). One writer, one patch, no registry collision by construction. (This mirrors the existing "registry-propagation as a follow-on patch" discipline.)

**Step 5 — Audit (integrator).** Run the GATE 0 verifier over the round's commit range:
```
bash parallel_dev/scripts/collision_audit.sh <base_ref>
```
where `<base_ref>` is the commit just before the round began. PASS ⇒ the round met GATE 0. Record the result on the board and clear the round.

---

## Collision-avoidance invariants (the rules that make it mechanical)

1. **One theorem per window.** Disjoint theorems ⇒ disjoint worker files.
2. **Disjoint owned file sets.** No two windows may list the same path in a round.
3. **Registry freeze during the round.** Workers never edit shared registries; those updates are batched into the Step 4 integration patch (single writer).
4. **Disjoint patch-number leases.** Numbers are labels, not enforced by git — so they must be leased, not chosen.
5. **Pull-before-generate; apply in board order.** Every patch targets current HEAD; conflicts on stale base ⇒ `git am --3way`.
6. **Grep-before-ID.** CLONE-FIRST GATE, per window.
7. **Single writer for board and integration.** Exactly one integrator runs `git am`/`push`/audit and edits the board.

If a round needs two windows to touch the same shared file *as workers*, that is a signal to serialize those two theorems into different rounds — not to relax the freeze.

---

## Recovery procedures

- **`git am` "corrupt patch":** the patch was mangled in transit (chat wrapping/whitespace). Re-request the patch as a downloaded file (real `git format-patch` export), not pasted text.
- **`git am` context conflict (clean tree):** stale base → `git am --3way`. If still failing on a case-only rename, regenerate with `git format-patch --no-renames`.
- **Mid-`am` failure:** `git am --abort` returns to clean `main`; re-dispatch the affected window with the current HEAD as base.
- **Audit FAIL:** do not start the next round. Fix the flagged collision (renumber, re-scope owned files, or split into serial rounds), re-apply, re-audit.

---

## Folding into operating_system.md (Phase 2)

This document is intentionally standalone for Phase 0 so it can iterate fast. When GATE 0 passes, its stable rules migrate into a new `operating_system.md` section and this file becomes a pointer, so the programme keeps **one** operating system. Do not let two protocols persist.

---

## Cheat sheet (per round)

```
Integrator: assign board (theorem | patch-range | owned files) — disjoint
Each window: CLONE-FIRST → work only owned paths → number only in lease → defer registries
Integrator: apply worker patches in board order (pull/am/push; --3way on stale base)
Integrator: apply ONE batched registry-integration patch
Integrator: bash parallel_dev/scripts/collision_audit.sh <base_ref>  → PASS = GATE 0 for the round
```

---

## Operator quickstart (plain language — run a round step by step)

This is the literal click-by-click for the integrator (Thomas). "Window" = one Claude chat. "Git Bash window" = the MINGW64 terminal where every git command is typed.

**Vocabulary, demystified:**
- **base_ref** = the commit hash that is HEAD *right before* the round starts. You capture it once, write it into the round's block on the lease board, and the audit later uses it to know which commits belong to this round.
- **owned paths (disjoint)** = the folders/files each window is allowed to write. "Disjoint" just means no two windows share a path — Window 1 writes only inside its theorem's folder, Window 2 only inside *its* theorem's folder, and so on. Because the folders don't overlap, the patches can't collide.
- **lease line** = the one row you hand a window: its theorem + its patch-number range + its owned paths.
- **board order** = the top-to-bottom order the rows are listed on the board. Apply patches in that order (it does not have to equal the order they were produced; listed order is what keeps it deterministic).

**Step A — capture base_ref (Git Bash window):**
```
cd ~/Documents/GitHub/CPP
git pull origin main
git rev-parse HEAD
```
Copy the 40-character hash it prints. That is your `base_ref`.

**Step B — write the round on the board.** Open `parallel_dev/lease_board.md`, copy the round template, and fill it in. Example using 100-wide blocks:
```
### Round 1 — 2026-06-07 | base_ref: <paste the hash from Step A> | audit: PENDING

| Window | Theorem | Patch-number lease | Owned files / paths (disjoint) | Status |
|--------|---------|--------------------|--------------------------------|--------|
| W1 | <theorem 1> | 0800–0899 | <folder for theorem 1 only>    | LEASED |
| W2 | <theorem 2> | 0900–0999 | <folder for theorem 2 only>    | LEASED |
| W3 | <theorem 3> | 1000–1099 | <folder for theorem 3 only>    | LEASED |
| INT | registry integration | 1100 | (the shared registries, batched) | LEASED |
```
You (the single writer) save the board. The 100-wide blocks are deliberately generous — collisions are impossible across them.

**Step C — open three windows and hand each its lease line.** In each Claude window: have it boot/clone the repo, then paste its row — e.g. *"You are W1. Theorem: <theorem 1>. Your patch numbers are 0800–0899. You may only create/edit files under <its folder>. Do not touch any shared registry. Clone + grep the registry before registering any ID."* Then work the physics with that window until it hands you a patch file (downloads to `~/Downloads`).

**Step D — apply the worker patches in board order (Git Bash window), one at a time:**
```
cd ~/Documents/GitHub/CPP && git pull origin main && git am ~/Downloads/<W1-patch> && git push origin main
```
Repeat for W2's patch, then W3's. If one fails with a context error on a clean tree, it was built on a stale base — re-run that one line with `git am --3way ~/Downloads/<file>`.

**Step E — apply ONE integration patch** that carries all the round's shared-registry updates (theorem-registry, predictions, frontier_sectors, etc.). Same apply line, the `INT` patch. This is the only commit allowed to touch the shared files, so they can't collide.

**Step F — audit (Git Bash window):**
```
bash parallel_dev/scripts/collision_audit.sh <base_ref>
```
(`bash` = run this script; the path = where the script lives; `<base_ref>` = the hash from Step A.) It prints PASS or FAIL per check and a final verdict. PASS = the round met GATE 0. Record PASS/FAIL on the board and clear the round.

**If you want a no-stakes rehearsal first:** run one round where the three "theorems" are throwaway notes (each window creates one file under `parallel_dev/dryrun/wN/`), apply, and audit. You'll see PASS end-to-end and learn the mechanics before spending real physics on it.
