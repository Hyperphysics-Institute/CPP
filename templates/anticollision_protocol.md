# Anti-Collision Protocol (lightweight multi-window)

**Location:** `templates/anticollision_protocol.md`
**Invoke:** paste **"run the anti-collision protocol"** into each Claude window when more than one
window is open against the shared tree. Each window then operates under the rules below for the rest
of the session.
**Mode:** this is the **light** protocol — no lease board, no base_ref capture, no audit script. It
is the right tool when **one human (Thomas) is the sole integrator** running 2–3 windows and holding
the global view. (The heavy `parallel_dev/multi_window_protocol.md` exists for onboarding real
workers; do not run both.)

---

## The setup it assumes

- **One shared working tree, one `origin/main`, one integrator (Thomas).** Every window is a worker;
  **only Thomas runs `git am` / `git push`.** Windows generate patches and hand them over.
- Windows' local commits are throwaway — Thomas's `git am` makes the authoritative commits. So
  **every window rebases its thinking onto current `origin/main` before generating a patch.**
- The one failure that actually bites: **two windows modifying the same file between syncs** (the
  second `git am` conflicts), or a patch **built on a stale base** (no longer applies). Both are
  closed below.

## Collision-susceptible files (the "files in question")

A write is **contested** (⇒ STOP-and-warn) if it creates-or-modifies any of these:

**Tier A — shared root registries** (any window may need them; second writer conflicts):
`theorem-registry.md`, `predictions.md`, `future_projects.md`, `todolist.md`,
`research_frontier.md`, `master_glossary.md`, and any root-level catalog/registry
(e.g. a future active `paper_catalog.md`; the current one is archived).

**Tier A — sector frontier files:** every `frontier_sectors/*.md`
(`SR.md SM.md CHIR.md CONJ.md EW.md QM.md SS.md SD.md FP.md PROP.md GLOBAL.md WORKFLOW.md`).
`CONJ.md`, `SR.md`, `SM.md` are the most cross-lane (DM + cosmology + CC all touch them).

**Tier B — cross-lane flagship `.tex` hazards:** `series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex` (the DP-Sea appendix),
the SS-1 strong-sector flagship, and any flagship two lanes both cite. These also need a **physics
sign-off** from Thomas, not just a collision check.

**Tier C — coordination:** `parallel_dev/lease_board.md` (single-writer = Thomas; never write it from
a window, even in light mode).

A write is **private-lane** (⇒ announce in the manifest and proceed, no STOP) if it is:
a **brand-new uniquely-named path**, or inside **your own window's owned subtree**, numbered in
**your own patch band**. Examples of owned subtrees: CC umbrella →
`series_umbrella/series_cosmological_constant_arc/`; Project C → `series_strong/lambda_qcd_from_planck/`;
DM lane → `series_phenomena/cosmology/dark_matter/`. **Never edit another window's owned subtree** —
propose the change to that window / the integrator instead.

## The protocol (per contested write)

1. **Manifest, every patch (window).** Before generating *any* patch, post a one-line-per-path
   manifest of everything it creates/modifies. Private-lane paths: note and proceed. If **any path is
   contested**, do **not** generate the patch yet — go to step 2.
2. **STOP-and-warn (window → Thomas).** Name the exact contested path(s) **and the line region** you
   intend to change, and what the change is. Then wait.
3. **Freeze (Thomas).** On a warn, **do nothing with that file in any other window** until this
   window's patch is applied. (Other *disjoint* work elsewhere may continue.) Reply: **"run the
   check."**
4. **Check + present (window).** "Run the check" =
   `git fetch origin` → sync to current `origin/main` HEAD → **re-read the target file(s) at current
   HEAD** → confirm the intended edit still fits and clashes with nothing new → build the patch **on
   current HEAD** → present it with its apply macro. (Building on current HEAD is what kills the
   stale-base collision; re-reading is what catches a same-file edit another window just landed.)
5. **Apply immediately (Thomas).** Run the provided macro
   (`git pull --rebase` → `git am <file>` → `git push`) **before** unfreezing that file elsewhere.
   Recovery: a context error on a clean tree ⇒ stale base ⇒ `git am --3way <file>`.

**Registry edits stay batched and separate regardless** — not ceremony, but because each registry
change as its own clearly-labeled patch makes Thomas's apply order **order-independent for disjoint
files and cleanly serial for the same file**. Don't fold a registry edit into a content patch.

## Band rule

Patch numbers are labels, not enforced by git, so each window numbers **only in its own band** and
**greps `git log` for the next free number before using one** (`git log --oneline | grep <band>`).
Consumed singletons stay consumed (e.g. 1100/1200/1300/1400 from the 2026-06-08 round). Current live
bands: CC umbrella **1101+**, Project C **1001+**, DM lane **08xx**, chirality lane **09xx**.

## Does this actually prevent collisions?

**Yes, for the failure modes that occur in a solo-integrator setup**, because:
- the warn reaches Thomas **before** any patch is generated (nothing is generated without its
  manifest), so two windows never silently race the same file;
- the **freeze** serializes contested writes to one file — the second window waits;
- the **check rebuilds on current HEAD**, so whatever just landed is already in the base ⇒ the patch
  applies cleanly (no stale base);
- **immediate apply** closes the window between present and land.

**The honest caveat:** the guarantee rests on **Thomas serializing** when he sees a warn — it is a
discipline, not a mechanism (that is the deliberate trade vs. the heavy protocol). If two windows
warn on the **same file at once**, Thomas applies one, then tells the other to **re-run the check**
against the new HEAD (step 4 rebuilds it cleanly). For 2–3 windows with one attentive integrator,
this is sufficient — it is the mode the DM (08xx) and chirality (09xx) lanes already ran without a
single collision.

## One-line invocation (paste into each window)

> **Run the anti-collision protocol** (`templates/anticollision_protocol.md`): multiple windows are
> open on the shared tree, Thomas is sole integrator. Manifest every patch; for any contested file
> (shared registries, `frontier_sectors/*`, the DP-Sea appendix / SS-1, the lease board) STOP-and-warn
> with path + line region and wait; on "run the check," fetch + rebuild on current `origin/main` HEAD,
> then present with an apply macro. Stay in your own band and owned subtree.
