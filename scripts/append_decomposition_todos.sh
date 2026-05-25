#!/usr/bin/env bash
# append_decomposition_todos.sh
#
# Appends three TODO entries (TODO-009, 010, 011) to todolist.md under P2,
# inserted before the "## Cleared items (history)" section header.
# These items are the cleanup-arc registered at the close of the 25 May 2026
# frontier decomposition work (commits a9cbcbf / df9f3c1 / 818ca61 / b2879de).
#
# Run from CPP repo root:
#     bash scripts/append_decomposition_todos.sh
#
# Idempotent: aborts if TODO-009 is already present in todolist.md.

set -euo pipefail

TARGET="todolist.md"
MARKER="^## Cleared items (history)$"

# ---- Preflight ----------------------------------------------------------

if [[ ! -f "$TARGET" ]]; then
    echo "ERROR: $TARGET not found in current directory." >&2
    echo "       Run from CPP repo root." >&2
    exit 1
fi

if grep -q "^### TODO-009" "$TARGET"; then
    echo "ERROR: TODO-009 already present in $TARGET. Aborting to avoid duplicate entries." >&2
    echo "       If you need to re-run, manually remove TODO-009/010/011 first." >&2
    exit 1
fi

if ! grep -q "$MARKER" "$TARGET"; then
    echo "ERROR: Could not find '## Cleared items (history)' header in $TARGET." >&2
    echo "       File structure has drifted from the version this script was written against." >&2
    exit 1
fi

BEFORE_LINES=$(wc -l < "$TARGET" | tr -d ' ')

# ---- Build new content --------------------------------------------------

NEW_FILE="${TARGET}.new"

{
    # Everything up to (but not including) the "## Cleared items" marker
    sed '/'"$MARKER"'/,$d' "$TARGET"

    # New TODO entries
    cat <<'NEW_TODOS'
### TODO-009 — Lowercase `SOURCE=` in frontier decomposition scripts for cross-platform correctness

**Status**: small hygiene fix; not blocking next paper
**Why P2**: Cosmetic issue on Windows; scripts work because Windows filesystem is case-insensitive. Would only fail on Linux/macOS or in a case-sensitive Linux container. Two scripts affected, one line each.
**Deliverable**: Change `SOURCE="Research_Frontier.md"` to `SOURCE="research_frontier.md"` in:
- `scripts/decompose_research_frontier.sh`
- `scripts/rewrite_research_frontier.sh`
**Estimated effort**: 1 small patch, ~5 minutes.
**Registered**: 25 May 2026 (frontier decomposition close, commit `b2879de`).

### TODO-010 — Second-level decomposition of `frontier_sectors/SS.md` (contingent on SS-sector bootup overflow)

**Status**: CONTINGENT — fires only if loading `frontier_sectors/SS.md` (208 KB, ~700 lines) at session bootup overflows the context window. Not currently known to do so.
**Why P2**: Speculative future hygiene. The 25 May 2026 frontier decomposition reduced master `research_frontier.md` from 1852 to 280 lines, solving the bootup overflow. Sector files are loaded on demand, not at bootup, so SS.md's size is only a concern if a session needs to load the full SS sector. If that triggers overflow in future SS-focused sessions, sub-decomposition becomes necessary.
**Trigger**: First session that overflows on `frontier_sectors/SS.md` load.
**Deliverable**: Split `frontier_sectors/SS.md` into sub-topic files following the same pattern as the master decomposition (extraction script + thin index rewrite). Candidate sub-decomposition:
- `frontier_sectors/SS_cage_mechanics.md` — SS-1 through SS-6 (quark mass, generations, condensate, β1, string tension, glueball)
- `frontier_sectors/SS_nuclear_binding.md` — SS-7, SS-8, SS-10 through SS-21 (binding curves, nucleon moments, ZBW mechanisms, deuteron)
- `frontier_sectors/SS_magic_numbers.md` — SS-22 through SS-37 (alpha-cluster regime, OPEN-SS-35 magic-number gap programme, deltahedra-gap closures)
- `frontier_sectors/SS_propositions.md` — SS-specific PROPs/CONJs from SS-5, SS-6, SS-7
**Estimated effort**: 1 dedicated session (~2 hours). Same pattern as 25 May 2026 master decomposition.
**Registered**: 25 May 2026 (frontier decomposition close, flagged from SS.md size observation: 208 KB, dwarfs all other sectors).

### TODO-011 — Structural-heterogeneity normalization pass across all sector files

**Status**: hygiene improvement; not blocking next paper
**Why P2**: `research_frontier.md` accumulated heterogeneity over months of organic growth — some OPEN-XX entries are richly sub-structured with `### Status`, `### Mechanism Required`, `### Route History`, etc.; others are flat single-paragraph prose. This was preserved verbatim in the 25 May 2026 decomposition to keep the extraction deterministic and reviewable. Normalizing every entry to a uniform sub-header skeleton would make sector files easier to grep, easier for AI collaborators to parse uniformly, and easier for new sessions to bootup-into-problem.
**Deliverable**: Standardize every OPEN-XX entry across all 9 sector files in `frontier_sectors/` to use a uniform sub-header skeleton:
- `### Status` — one-line current state
- `### Mechanism Required` — what closure looks like
- `### Acceptance Criteria` — F1/F2/F3 falsifiers or equivalent
- `### Route History` — what has been tried; ruled-out routes preserved
- `### Cross-References` — related OPEN-XX entries, papers, conjectures, propositions

Empty sections marked `(none yet)` to keep the skeleton uniform across heavily-developed and stubbed entries alike.
**Estimated effort**: ~9 patches (one per sector), deliverable as a sequential arc. Could also be done piecemeal as sessions touch specific sectors for unrelated reasons (lazy normalization).
**Registered**: 25 May 2026 (frontier decomposition close, noted from sector-file spot-check when Thomas observed format heterogeneity in extracted files).

---

NEW_TODOS

    # The marker line and everything after
    sed -n '/'"$MARKER"'/,$p' "$TARGET"

} > "$NEW_FILE"

# ---- Atomic replace -----------------------------------------------------

mv "$NEW_FILE" "$TARGET"

AFTER_LINES=$(wc -l < "$TARGET" | tr -d ' ')
ADDED=$((AFTER_LINES - BEFORE_LINES))

echo "Appended three TODO entries to $TARGET:"
echo "  Before: $BEFORE_LINES lines"
echo "  After:  $AFTER_LINES lines"
echo "  Added:  $ADDED lines (TODO-009, TODO-010, TODO-011)"
echo ""
echo "Next steps:"
echo "  1. git diff $TARGET    (review the addition)"
echo "  2. git add $TARGET && git commit && git push origin main"
