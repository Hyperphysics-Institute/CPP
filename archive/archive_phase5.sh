#!/bin/bash
# Phase 5: Archive obsolete files replaced by Research_Frontier.md and theorem-registry.md
# Run from CPP repo root after pulling latest
# Date: 12 April 2026

set -e

echo "=== Phase 5: Archiving obsolete files ==="

# 1. Create archive subdirectory
mkdir -p archive/pre_frontier_2026-04-12

# 2. Archive the three root-level files
echo "Archiving root files..."
git mv propositions.md archive/pre_frontier_2026-04-12/
git mv solution_candidates.md archive/pre_frontier_2026-04-12/
git mv postulates_and_theorems.md archive/pre_frontier_2026-04-12/

# 3. Archive the entire open_problems/ directory
echo "Archiving open_problems/..."
git mv open_problems/ archive/pre_frontier_2026-04-12/open_problems/

echo ""
echo "=== Done. Files moved to archive/pre_frontier_2026-04-12/ ==="
echo ""
echo "Commit with:"
echo '  git add -A'
echo '  git commit -m "Phase 5: Archive files replaced by Research_Frontier.md and theorem-registry.md'
echo ''
echo '  Archived to archive/pre_frontier_2026-04-12/:'
echo '  - propositions.md (absorbed into Research_Frontier.md §3)'
echo '  - solution_candidates.md (absorbed into frontier entries current-best-lead fields)'
echo '  - postulates_and_theorems.md (split into axiom-registry.md + theorem-registry.md + Research_Frontier.md)'
echo '  - open_problems/ (58 files absorbed into Research_Frontier.md §1-§6)'
echo ''
echo '  Canonical locations for all content:'
echo '  - Open problems, conjectures, propositions: Research_Frontier.md'
echo '  - Theorems and corollaries: theorem-registry.md'
echo '  - Axioms: axiom-registry.md (unchanged)'
echo '  - Predictions: predictions.md (unchanged)'
echo '  - Problem narratives: problem_histories/'
echo '"'
