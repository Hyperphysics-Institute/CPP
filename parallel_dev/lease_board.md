# CPP Parallel-Development Lease Board

**Location:** `/CPP/parallel_dev/lease_board.md`
**Purpose:** Per-round coordination ledger for multi-window parallel development. Assigns each active window a theorem, a disjoint patch-number range, and a disjoint owned-file set, so collisions are prevented by construction. Procedure: `parallel_dev/multi_window_protocol.md`.

> **SINGLE WRITER — READ THIS.** Exactly one person — the integrator (Thomas) — edits this file. Worker windows **read** their lease and **report status in chat**; they never edit this board. This single-writer rule is what keeps the board from becoming a collision point.
>
> **This is ephemeral coordination state, NOT a registry.** It records who-owns-what right now. Physics truth lives in `theorem-registry.md`, `predictions.md`, `frontier_sectors/`, `master_glossary.md` — never here.

**Status legend:** `LEASED` (assigned, not started) · `ACTIVE` (window working) · `PATCHED` (patch produced, awaiting apply) · `APPLIED` (landed on main) · `DONE` (round audited).

---

## Round template (copy this block for each new round)

```
### Round N — <date>  | base_ref: <commit before round> | audit: PENDING

| Window | Theorem | Patch-number lease | Owned files / paths (disjoint) | Status |
|--------|---------|--------------------|--------------------------------|--------|
| W1 | <theorem id/name> | 07xx–07xx | <path(s) only this window edits> | LEASED |
| W2 | <theorem id/name> | 07xx–07xx | <path(s)> | LEASED |
| W3 | <theorem id/name> | 07xx–07xx | <path(s)> | LEASED |
| INT | (integrator) registry-integration patch | 07xx | theorem-registry.md, predictions.md, frontier_sectors/*, master_glossary.md (batched) | LEASED |

Audit: `bash parallel_dev/scripts/collision_audit.sh <base_ref>` → record PASS/FAIL here.
```

**Rules when filling a round:**
- Owned-file sets must be **pairwise disjoint**. No path appears in two worker rows.
- Patch-number ranges must be **disjoint** and not reuse any label already in `git log`.
- Workers never list a shared registry in their owned files — those go only in the `INT` row.

---

## Worked example (illustrative — not a live round)

```
### Round 0 (EXAMPLE) — 2026-06-06 | base_ref: bbb4be7 | audit: PASS

| Window | Theorem | Patch-number lease | Owned files / paths | Status |
|--------|---------|--------------------|---------------------|--------|
| W1 | LEMMA-EX-A | 0790–0791 | series_x/theorems/LEMMA-EX-A/ | DONE |
| W2 | LEMMA-EX-B | 0792–0793 | series_x/theorems/LEMMA-EX-B/ | DONE |
| W3 | LEMMA-EX-C | 0794–0795 | series_y/theorems/LEMMA-EX-C/ | DONE |
| INT | registry integration | 0796 | theorem-registry.md, frontier_sectors/SR.md | DONE |

Audit: PASS — 0 worker-file collisions, 0 duplicate patch numbers, 0 duplicate IDs, tree clean.
```
### Round 0 (DRY RUN) — 2026-06-07 | base_ref: a585a3d | audit: PENDING

| Window | Theorem/task | Patch-number lease | Owned files / paths | Status |
|--------|--------------|--------------------|---------------------|--------|
| W1 | dry-run marker | 0800–0899 | parallel_dev/dryrun/w1/ | LEASED |
| W2 | dry-run marker | 0900–0999 | parallel_dev/dryrun/w2/ | LEASED |
| W3 | dry-run marker | 1000–1099 | parallel_dev/dryrun/w3/ | LEASED |
---

## Live rounds

*(Integrator: add the first real round below once the Phase 0 theorem set is chosen. Pick `base_ref` = current `git rev-parse HEAD` before dispatching windows.)*

### Round 1 — 2026-06-07 | base_ref: <paste hash> | audit: PENDING

| Window | Theorem/task | Patch lease | Owned path (disjoint) | Status |
|--------|--------------|-------------|------------------------|--------|
| W1 | μ²-sign → THEO-CHIR-CAPACITY-1 (chirality capacity) | 1100–1199 | series_umbrella/series_substrate_chirality_arc/chirality_derivations/ (new files only) | LEASED |
| W2 | DM-candidate identification sub-lemma (σ/m + coldness consolidation) | 1200–1299 | series_phenomena/cosmology/dark_matter/ (new files only) | LEASED |
| W3 | OPEN-EU-1 leg-2: DP-pair neutrality grounded→derived attempt | 1300–1399 | series_phenomena/cosmology/early_universe/ (new files only) | LEASED |
| INT | registry/frontier integration (batched) | 1400 | theorem-registry.md, frontier_sectors/CHIR.md, frontier_sectors/SR.md, lease_board.md | LEASED |
