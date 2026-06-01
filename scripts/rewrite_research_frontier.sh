#!/usr/bin/env bash
# rewrite_research_frontier.sh
#
# Second-stage decomposition tool: rewrites research_frontier.md in place,
# converting it from the 1852-line monolithic file into a thin dashboard
# (~280 lines) that points into frontier_sectors/ for sector detail.
#
# Run from CPP repo root:
#     bash scripts/rewrite_research_frontier.sh
#
# Preconditions:
#   - research_frontier.md is the 1852-line pre-decomposition version
#   - frontier_sectors/ exists with the 11 extracted sector files
#     (produced by scripts/decompose_research_frontier.sh)
#
# Behavior:
#   - Saves backup as research_frontier.md.pre-decomposition.bak
#   - Composes new research_frontier.md by concatenating:
#       (a) Lines 1-37 of original (header, Purpose, How to Use, §1 intro)
#       (b) New Sector Index dashboard (table linking into frontier_sectors/)
#       (c) Lines 1650-1852 of original (§4 Recently Resolved through §10)
#   - Does NOT touch git — user commits manually after review

set -euo pipefail

SOURCE="research_frontier.md"
BACKUP="research_frontier.md.pre-decomposition.bak"
SECTORS_DIR="frontier_sectors"
EXPECTED_LINES_MIN=1800
EXPECTED_LINES_MAX=1900

# ---- Preflight checks ----------------------------------------------------

if [[ ! -f "$SOURCE" ]]; then
    echo "ERROR: $SOURCE not found in current directory." >&2
    echo "       Run from CPP repo root." >&2
    exit 1
fi

if [[ ! -d "$SECTORS_DIR" ]]; then
    echo "ERROR: $SECTORS_DIR/ not found." >&2
    echo "       Run scripts/decompose_research_frontier.sh first." >&2
    exit 1
fi

LINE_COUNT=$(wc -l < "$SOURCE" | tr -d ' ')
if (( LINE_COUNT < EXPECTED_LINES_MIN || LINE_COUNT > EXPECTED_LINES_MAX )); then
    echo "ERROR: $SOURCE has $LINE_COUNT lines, expected ${EXPECTED_LINES_MIN}-${EXPECTED_LINES_MAX}." >&2
    echo "       File may already have been rewritten, or has drifted from the" >&2
    echo "       pinned structure. Aborting." >&2
    echo "" >&2
    echo "       If you have already rewritten and want to redo, restore from backup:" >&2
    echo "           cp $BACKUP $SOURCE" >&2
    echo "       and re-run this script." >&2
    exit 1
fi

# Verify expected sector files exist
EXPECTED_SECTORS=(FP SS SM EW QM SR SD GLOBAL WORKFLOW CONJ PROP)
for sector in "${EXPECTED_SECTORS[@]}"; do
    if [[ ! -f "$SECTORS_DIR/${sector}.md" ]]; then
        echo "ERROR: $SECTORS_DIR/${sector}.md not found." >&2
        echo "       Decomposition appears incomplete. Aborting." >&2
        exit 1
    fi
done

# ---- Backup --------------------------------------------------------------

cp "$SOURCE" "$BACKUP"
echo "Backup saved: $BACKUP"

# ---- Compose new dashboard ----------------------------------------------

NEW_FILE="${SOURCE}.new"

{
    # (a) Preserve lines 1-37: header, Purpose, How to Use, §1 intro
    sed -n '1,37p' "$SOURCE"

    # (b) New dashboard middle: sector index table replaces 1612 lines of §1-§3 detail
    cat <<'DASHBOARD_EOF'

## Sector Index — Active Open Problems, Conjectures, and Propositions

The active open problems, conjectures, and propositions are organized by sector under [`frontier_sectors/`](frontier_sectors/). Each sector file contains the full problem statements with status, mechanisms, route history, and acceptance criteria. Load only the sector you are working on.

### §1 — Active Open Problems by Sector

| Sector | File | Scope | Problems |
|--------|------|-------|----------|
| FP | [`frontier_sectors/FP.md`](frontier_sectors/FP.md) | Flagship Papers — apex layer (SF-line) | 9 |
| SS | [`frontier_sectors/SS.md`](frontier_sectors/SS.md) | Strong Sector (includes SS-specific propositions and conjectures from SS-5, SS-6, SS-7) | 18 active, 1 retired |
| SM | [`frontier_sectors/SM.md`](frontier_sectors/SM.md) | Standard Model Emergence | 11 |
| EW | [`frontier_sectors/EW.md`](frontier_sectors/EW.md) | Electroweak Sector | 6 |
| QM | [`frontier_sectors/QM.md`](frontier_sectors/QM.md) | Quantum Mechanics | 5 |
| SR | [`frontier_sectors/SR.md`](frontier_sectors/SR.md) | Special Relativity / Gravity | 8 |
| SD | [`frontier_sectors/SD.md`](frontier_sectors/SD.md) | Foundations / Superdeterminism | 6 |
| GLOBAL | [`frontier_sectors/GLOBAL.md`](frontier_sectors/GLOBAL.md) | Cross-Series (e.g., three SM generations, full SM from single 600-cell) | 2 |
| WORKFLOW | [`frontier_sectors/WORKFLOW.md`](frontier_sectors/WORKFLOW.md) | Workflow / Infrastructure | 1 |

### §2, §3 — Cross-Sector Categories

| Category | File | Description |
|----------|------|-------------|
| §2 Conjectures | [`frontier_sectors/CONJ.md`](frontier_sectors/CONJ.md) | Conjectures under investigation, all sectors |
| §3 Propositions | [`frontier_sectors/PROP.md`](frontier_sectors/PROP.md) | Propositions in progress, all sectors |

### Loading Discipline

- **Bootup** loads this dashboard only (~280 lines). It does NOT load any sector file.
- **Session work** loads the relevant sector file on demand. Working OPEN-SS-35 → load `frontier_sectors/SS.md`. Working SF-4 → load `frontier_sectors/FP.md`. Working PMNS angles (OPEN-SM-5) → load `frontier_sectors/SM.md`.
- **Cross-sector planning** may load multiple sector files, but rarely all eleven. Programme-level questions (e.g., "what closes if SS-35 closes?") use §8 Dependency Graph below as the entry point.

### Decomposition Provenance

- Original monolithic file: 1852 lines (research_frontier.md pre-2026-05-25).
- Decomposition performed 2026-05-25 to resolve repeated context-window overflow at bootup.
- §1 sector content extracted by line-range to `frontier_sectors/<SECTOR>.md`. §2 and §3 extracted to `frontier_sectors/CONJ.md` and `frontier_sectors/PROP.md`.
- §4–§10 (Recently Resolved, Resolved Archive, Falsified, Recommended Attack Order, Dependency Graph, Problem Count Summary, Anomalies) retained in this dashboard below.
- Pre-decomposition snapshot also recoverable from git history.

DASHBOARD_EOF

    # (c) Preserve lines 1650-1852: §4 through §10
    sed -n '1650,1852p' "$SOURCE"

} > "$NEW_FILE"

# ---- Atomic replace ------------------------------------------------------

mv "$NEW_FILE" "$SOURCE"

NEW_LINES=$(wc -l < "$SOURCE" | tr -d ' ')

echo ""
echo "Rewrite complete:"
echo "  Before: $LINE_COUNT lines (monolithic)"
echo "  After:  $NEW_LINES lines (dashboard)"
echo "  Reduction: $(( 100 - (NEW_LINES * 100 / LINE_COUNT) ))% smaller"
echo ""
echo "Backup retained at: $BACKUP"
echo "  (Add to .gitignore or delete manually after verification.)"
echo ""
echo "Next steps:"
echo "  1. Open research_frontier.md and verify dashboard reads correctly"
echo "  2. git diff research_frontier.md  (to see the rewrite)"
echo "  3. If happy: git add research_frontier.md && git commit && git push"
echo "  4. Delete backup: rm $BACKUP"
