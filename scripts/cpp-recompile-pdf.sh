#!/bin/bash
# cpp-recompile-pdf.sh — Compile a flagship/SS/SM paper's PDF and commit it
#
# Usage:
#   cpp-recompile-pdf.sh <paper-directory> [--no-push]
#
# Arguments:
#   <paper-directory>   Path (absolute or relative) to a directory
#                       containing exactly one .tex paper file.
#                       Example: flagship_papers/neutrinos
#   --no-push           Compile and commit locally but do not push.
#                       Use this on travel machines (Surface) where
#                       the PDF is for local verification only.
#
# Behavior:
#   1. cd into <paper-directory>
#   2. Identify the .tex file (one per directory expected)
#   3. Run pdflatex twice (cross-reference resolution)
#   4. Clean auxiliary files (.aux, .log, .toc, .out)
#   5. git add the resulting .pdf
#   6. Commit with auto-generated message referencing source HEAD
#   7. Push to origin (unless --no-push)
#
# Canonical compile machine:
#   ClearPC is the designated canonical machine for flagship paper
#   PDFs (adopted 11 May 2026 after the patch 0336 binary-blob
#   friction). Other machines may run this script with --no-push
#   for local verification but should not commit PDFs to origin.
#   See operating_system.md § Binary Artifact Workflow.
#
# Exit codes:
#   0   Success (compiled, committed, optionally pushed)
#   1   Usage error or compilation failure
#   2   No PDF changes to commit (already up-to-date)

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <paper-directory> [--no-push]"
  exit 1
fi

DIR="$1"
NOPUSH=0
if [ "${2:-}" = "--no-push" ]; then
  NOPUSH=1
fi

if [ ! -d "$DIR" ]; then
  echo "ERROR: directory not found: $DIR"
  exit 1
fi

# Resolve absolute paths before cd
DIR_ABS=$(cd "$DIR" && pwd)
REPO_ROOT=$(git rev-parse --show-toplevel)

cd "$DIR_ABS"

# Find the .tex file (expects exactly one)
TEXFILE=$(ls *.tex 2>/dev/null | head -1)
if [ -z "$TEXFILE" ]; then
  echo "ERROR: no .tex file in $DIR_ABS"
  exit 1
fi
BASENAME=$(basename "$TEXFILE" .tex)
PDFFILE="$BASENAME.pdf"

echo "=== Compiling $TEXFILE (pass 1 of 2) ==="
if ! pdflatex -interaction=nonstopmode "$TEXFILE" > /tmp/pdflatex_pass1.log 2>&1; then
  echo "ERROR: pdflatex pass 1 failed. Last 20 lines of log:"
  tail -20 /tmp/pdflatex_pass1.log
  exit 1
fi

echo "=== Compiling $TEXFILE (pass 2 of 2) ==="
if ! pdflatex -interaction=nonstopmode "$TEXFILE" > /tmp/pdflatex_pass2.log 2>&1; then
  echo "ERROR: pdflatex pass 2 failed. Last 20 lines of log:"
  tail -20 /tmp/pdflatex_pass2.log
  exit 1
fi

if [ ! -f "$PDFFILE" ]; then
  echo "ERROR: expected $PDFFILE not produced"
  exit 1
fi

PAGES=$(grep "Output written on" /tmp/pdflatex_pass2.log | grep -oE '[0-9]+ pages' | head -1)
SIZE=$(stat -c %s "$PDFFILE" 2>/dev/null || stat -f %z "$PDFFILE" 2>/dev/null || wc -c < "$PDFFILE")
echo "=== Compiled: $PDFFILE ($PAGES, $SIZE bytes) ==="

# Clean up auxiliary files
rm -f *.aux *.log *.toc *.out *.fdb_latexmk *.fls *.synctex.gz

# Stage from repo root
cd "$REPO_ROOT"
RELPDF=$(realpath --relative-to="$REPO_ROOT" "$DIR_ABS/$PDFFILE")
git add "$RELPDF"

if git diff --cached --quiet; then
  echo "No changes to commit ($PDFFILE bytes match what was already tracked)."
  exit 2
fi

SHORTSHA=$(git rev-parse --short HEAD)
COMMITMSG="Recompile ${BASENAME}.pdf locally to match source at ${SHORTSHA} — ${PAGES}, ${SIZE} bytes"
git commit -m "$COMMITMSG"

echo "=== Committed: $COMMITMSG ==="

if [ $NOPUSH -eq 1 ]; then
  echo "Skipping push (--no-push). Local commit ready; do not push from non-canonical machine."
else
  echo "=== Pushing to origin ==="
  git push origin main
  echo "=== Done. New HEAD: $(git rev-parse --short HEAD) ==="
fi
