# `Registries_pending/` — write-partitioned deliberate registry deltas

This is the collision-free channel for **deliberate** registry edits (Capture-and-Audit
Protocol §6; paper-production discipline, `operating_system.md` §4). Each window writes
**only to its own** file `Registries_pending/<window-slug>.md` — never a shared target —
so N windows never collide. The overnight audit (`scripts/overnight_extraction_audit.sh`)
merges all windows' files and clears them.

> **Pending activation.** This channel goes live only when the overnight audit is built
> and scheduled. Until then, continue applying registry edits in-session (a write here
> would never reach canonical without the merge). See the protocol STATUS line.

## When to write here
A registry edit you would otherwise hand-apply to a **shared repo-root registry**:
Phase 5 (axiom/theorem) and Phase 7B (theory-overview, axiom-registry, theorem-registry,
master_glossary, research_frontier, predictions, paper_catalog, founders_vision,
future_projects, TATWD, problem_histories, top-level README), plus the shared-file 7A
items (C11 bibliography, D2 INDEX.md, D3 series-README). Paper-local files are unaffected —
edit those in-session.

## Delta format (contract — the macro parses this)

```
---
window-slug: <slug>           # must match the filename
---
# Pending registry deltas — <slug>   (append-only; the audit merges + clears)

- registry=theorem-registry | action="register THEO-X coeff 3/5" | paper=DM-1 | patch=850
- registry=predictions | action="+3 zero-parameter PRED-DM-1-{1,2,3}" | paper=DM-1 | patch=850
- registry=paper_catalog | action="row: DM-1 v1.0 SHIPPED" | paper=DM-1 | patch=850
```

Each delta is one `- ` line with `key=value | key=value` fields:
- `registry` — the canonical file/registry the delta targets (one of the shared set).
- `action` — the **precise** instruction, in your words, written while context is fresh.
  The audit applies/stages exactly this; it does NOT reconstruct it from prose.
- `paper` / `patch` — provenance.

**Append only to your own file.** The audit stages the merged result as a diff for TLA
to apply (canonical edits stay TLA-applied), then clears the pending files.

## Read-render (same-day visibility — REQUIRED before allocating a registry ID)
Before claiming any THEO / PRED / OPEN-problem ID, read canonical **AND** glob
`Registries_pending/*.md` — another window may have an in-flight claim not yet merged.
Read-only; never write another window's file.
