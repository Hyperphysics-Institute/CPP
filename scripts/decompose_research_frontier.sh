#!/usr/bin/env bash
# decompose_research_frontier.sh
#
# One-shot extraction tool: splits Research_Frontier.md into 11 per-sector
# files under frontier_sectors/. Does NOT modify Research_Frontier.md.
# The dashboard rewrite of Research_Frontier.md ships as a follow-up patch
# after the user verifies the extraction produced here.
#
# Run from CPP repo root:
#     bash scripts/decompose_research_frontier.sh
#
# Line ranges are pinned to the file structure as of 2026-05-25 (1852 lines).
# Script aborts if Research_Frontier.md has drifted significantly from that
# size, to avoid silently extracting wrong content.

set -euo pipefail

SOURCE="Research_Frontier.md"
DEST_DIR="frontier_sectors"
EXPECTED_LINES_MIN=1800
EXPECTED_LINES_MAX=1900

# ---- Preflight checks ----------------------------------------------------

if [[ ! -f "$SOURCE" ]]; then
    echo "ERROR: $SOURCE not found in current directory." >&2
    echo "       Run this script from the CPP repo root:" >&2
    echo "           cd ~/Documents/GitHub/CPP" >&2
    echo "           bash scripts/decompose_research_frontier.sh" >&2
    exit 1
fi

LINE_COUNT=$(wc -l < "$SOURCE" | tr -d ' ')
if (( LINE_COUNT < EXPECTED_LINES_MIN || LINE_COUNT > EXPECTED_LINES_MAX )); then
    echo "ERROR: $SOURCE has $LINE_COUNT lines, expected ${EXPECTED_LINES_MIN}-${EXPECTED_LINES_MAX}." >&2
    echo "       File may have been modified since this script's line ranges were pinned." >&2
    echo "       Re-survey the file with:" >&2
    echo "           wc -l Research_Frontier.md" >&2
    echo "           grep -n '^#' Research_Frontier.md" >&2
    echo "       and update the line ranges in this script before re-running." >&2
    exit 1
fi

if [[ -d "$DEST_DIR" ]]; then
    echo "ERROR: $DEST_DIR/ already exists." >&2
    echo "       To redo extraction, remove it first:" >&2
    echo "           rm -rf $DEST_DIR" >&2
    echo "       Then re-run this script." >&2
    exit 1
fi

mkdir -p "$DEST_DIR"

# ---- Extraction helper ---------------------------------------------------

extract_sector() {
    local name="$1"
    local start="$2"
    local end="$3"
    local label="$4"
    local outfile="$DEST_DIR/${name}.md"

    {
        echo "<!--"
        echo "  Extracted from Research_Frontier.md lines ${start}-${end}"
        echo "  Source range: $label"
        echo "  Extraction date: $(date +%Y-%m-%d)"
        echo "  Master dashboard: Research_Frontier.md"
        echo "-->"
        echo ""
        sed -n "${start},${end}p" "$SOURCE"
    } > "$outfile"

    local extracted_lines
    extracted_lines=$(wc -l < "$outfile" | tr -d ' ')
    printf "  %-10s lines %4d-%4d  ->  %s (%d lines out)\n" \
        "$name" "$start" "$end" "$outfile" "$extracted_lines"
}

# ---- Run extraction ------------------------------------------------------

echo "Source:      $SOURCE ($LINE_COUNT lines)"
echo "Destination: $DEST_DIR/"
echo ""
echo "Extracting 11 sector files:"
echo ""

# §1 — Active Open Problems (sectors)
extract_sector "FP"        38   190    "Flagship Papers"
extract_sector "SS"        191  864    "Strong Sector (incl. SS-specific props/conjectures at 796-864)"
extract_sector "SM"        865  1019   "Standard Model Emergence"
extract_sector "EW"        1020 1100   "Electroweak Sector"
extract_sector "QM"        1101 1164   "Quantum Mechanics"
extract_sector "SR"        1165 1265   "Special Relativity / Gravity"
extract_sector "SD"        1266 1342   "Foundations / Superdeterminism"
extract_sector "GLOBAL"    1343 1369   "Cross-Series Problems"
extract_sector "WORKFLOW"  1370 1384   "Workflow / Infrastructure"

# §2 — Conjectures Under Investigation
extract_sector "CONJ"      1385 1578   "§2 Conjectures Under Investigation"

# §3 — Propositions In Progress
extract_sector "PROP"      1579 1649   "§3 Propositions In Progress"

echo ""
echo "Extraction complete."
echo ""
echo "Verification:"
echo "  - Total lines extracted: $(wc -l "$DEST_DIR"/*.md | tail -1 | awk '{print $1}')"
echo "  - Master file Research_Frontier.md was NOT modified ($LINE_COUNT lines, unchanged)"
echo ""
echo "Next steps:"
echo "  1. Inspect frontier_sectors/ — open a few sector files and confirm content looks correct"
echo "  2. Confirm to Claude that extraction looks right"
echo "  3. Apply follow-up patch to rewrite Research_Frontier.md as the thin dashboard"
