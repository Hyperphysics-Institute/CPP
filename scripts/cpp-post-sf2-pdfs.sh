#!/bin/bash
# cpp-post-sf2-pdfs.sh — Compile + post both SF-2 PDFs (main + Companion)
#                       to flagship_papers/electroweak/ in a single commit.
#
# Usage:
#   cpp-post-sf2-pdfs.sh [--no-push]
#
# Arguments:
#   --no-push   Compile and commit locally but do not push. Use on travel
#               machines (Surface) where the PDFs are for local verification
#               only.
#
# Behavior:
#   1. cd into flagship_papers/electroweak
#   2. Compile sf-2_electroweak.tex (main paper) — pdflatex × 2
#   3. Compile sf-2_companion.tex (Companion) — pdflatex × 2
#   4. Clean auxiliary files (.aux, .log, .toc, .out, .fdb_latexmk, .fls)
#   5. git add both PDFs from repo root
#   6. Commit with auto-generated message referencing source HEAD + version
#   7. Push to origin/main (unless --no-push)
#
# Why this script exists:
#   SF-2 is the first CPP flagship to ship in the two-paper Companion format
#   (programme-strategic guidance per PD-005 for future SF-line flagships).
#   The existing scripts/cpp-recompile-pdf.sh expects exactly one .tex file
#   per directory and cannot handle the two-paper case directly. This script
#   is the SF-2-specific Binary Artifact Workflow companion script; analogous
#   scripts will be needed for future SF-line flagships that adopt the
#   Companion architecture (SF-3, SF-5, SF-6, SF-7).
#
# Canonical compile machine:
#   ClearPC is the designated canonical machine for flagship paper PDFs
#   (adopted 11 May 2026 after the patch 0336 binary-blob friction, codified
#   in operating_system.md § Binary Artifact Workflow). Other machines may
#   run this script with --no-push for local verification only.
#
# Exit codes:
#   0   Success (compiled, committed, optionally pushed)
#   1   Usage error or compilation failure
#   2   No PDF changes to commit (PDFs match what is already tracked)

set -euo pipefail

NOPUSH=0
if [ "${1:-}" = "--no-push" ]; then
  NOPUSH=1
fi

REPO_ROOT=$(git rev-parse --show-toplevel)
SF2_DIR="$REPO_ROOT/flagship_papers/electroweak"

if [ ! -d "$SF2_DIR" ]; then
  echo "ERROR: SF-2 directory not found at $SF2_DIR"
  exit 1
fi

cd "$SF2_DIR"

# Verify both .tex sources exist
if [ ! -f sf-2_electroweak.tex ]; then
  echo "ERROR: sf-2_electroweak.tex not found in $SF2_DIR"
  exit 1
fi
if [ ! -f sf-2_companion.tex ]; then
  echo "ERROR: sf-2_companion.tex not found in $SF2_DIR"
  exit 1
fi

# --- Compile main paper ---
echo "=== Compiling sf-2_electroweak.tex (main paper, pass 1 of 2) ==="
if ! pdflatex -interaction=nonstopmode sf-2_electroweak.tex > /tmp/sf2_main_p1.log 2>&1; then
  echo "ERROR: main paper pdflatex pass 1 failed. Last 25 lines:"
  tail -25 /tmp/sf2_main_p1.log
  exit 1
fi

echo "=== Compiling sf-2_electroweak.tex (main paper, pass 2 of 2) ==="
if ! pdflatex -interaction=nonstopmode sf-2_electroweak.tex > /tmp/sf2_main_p2.log 2>&1; then
  echo "ERROR: main paper pdflatex pass 2 failed. Last 25 lines:"
  tail -25 /tmp/sf2_main_p2.log
  exit 1
fi

if [ ! -f sf-2_electroweak.pdf ]; then
  echo "ERROR: sf-2_electroweak.pdf not produced"
  exit 1
fi

MAIN_PAGES=$(grep "Output written on" /tmp/sf2_main_p2.log | grep -oE '[0-9]+ pages' | head -1)
MAIN_SIZE=$(stat -c %s sf-2_electroweak.pdf 2>/dev/null || stat -f %z sf-2_electroweak.pdf 2>/dev/null)
MAIN_UNDEF=$(grep -c 'undefined' /tmp/sf2_main_p2.log || true)
echo "=== Main paper compiled: $MAIN_PAGES, $MAIN_SIZE bytes, $MAIN_UNDEF undefined refs ==="

# --- Compile Companion ---
echo "=== Compiling sf-2_companion.tex (Companion, pass 1 of 2) ==="
if ! pdflatex -interaction=nonstopmode sf-2_companion.tex > /tmp/sf2_comp_p1.log 2>&1; then
  echo "ERROR: Companion pdflatex pass 1 failed. Last 25 lines:"
  tail -25 /tmp/sf2_comp_p1.log
  exit 1
fi

echo "=== Compiling sf-2_companion.tex (Companion, pass 2 of 2) ==="
if ! pdflatex -interaction=nonstopmode sf-2_companion.tex > /tmp/sf2_comp_p2.log 2>&1; then
  echo "ERROR: Companion pdflatex pass 2 failed. Last 25 lines:"
  tail -25 /tmp/sf2_comp_p2.log
  exit 1
fi

if [ ! -f sf-2_companion.pdf ]; then
  echo "ERROR: sf-2_companion.pdf not produced"
  exit 1
fi

COMP_PAGES=$(grep "Output written on" /tmp/sf2_comp_p2.log | grep -oE '[0-9]+ pages' | head -1)
COMP_SIZE=$(stat -c %s sf-2_companion.pdf 2>/dev/null || stat -f %z sf-2_companion.pdf 2>/dev/null)
COMP_UNDEF=$(grep -c 'undefined' /tmp/sf2_comp_p2.log || true)
echo "=== Companion compiled: $COMP_PAGES, $COMP_SIZE bytes, $COMP_UNDEF undefined refs ==="

# --- Clean auxiliary files ---
rm -f *.aux *.log *.toc *.out *.fdb_latexmk *.fls *.synctex.gz

# --- Extract version marker for commit message ---
VERSION=$(grep -oE 'Version [0-9]+\.[0-9]+ SHIPPED' sf-2_electroweak.tex | head -1 | grep -oE 'v?[0-9]+\.[0-9]+' || echo "v?.?")
VERSION="v${VERSION#v}"

# --- Stage from repo root ---
cd "$REPO_ROOT"
git add flagship_papers/electroweak/sf-2_electroweak.pdf
git add flagship_papers/electroweak/sf-2_companion.pdf

if git diff --cached --quiet; then
  echo "No PDF changes to commit (both PDFs byte-identical to what is already tracked)."
  exit 2
fi

SHORTSHA=$(git rev-parse --short HEAD)
COMMITMSG="Binary artifact: SF-2 ${VERSION} PDFs (main + Companion) compiled locally on $(hostname -s)

Binary Artifact Workflow per operating_system §13:
- Source HEAD: ${SHORTSHA}
- Main paper:  ${MAIN_PAGES}, ${MAIN_SIZE} bytes
- Companion:   ${COMP_PAGES}, ${COMP_SIZE} bytes
- Both PDFs compiled cleanly from .tex source at HEAD
- Undefined refs: main=${MAIN_UNDEF}, companion=${COMP_UNDEF}"

git commit -m "$COMMITMSG"

echo "=== Committed: SF-2 ${VERSION} PDFs (main: ${MAIN_PAGES}, companion: ${COMP_PAGES}) ==="

if [ $NOPUSH -eq 1 ]; then
  echo "Skipping push (--no-push). Local commit ready; do not push from non-canonical machine."
else
  echo "=== Pushing to origin/main ==="
  git push origin main
  echo "=== Done. New HEAD: $(git rev-parse --short HEAD) ==="
fi
