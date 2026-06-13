#!/usr/bin/env bash
# build_figures.sh — regenerate PDF figures from committed SVG sources.
# Repo ignores *.pdf, so figure PDFs are build artifacts. Run before compiling
# a paper whose .tex does \includegraphics{...pdf}.  Requires cairosvg.
set -euo pipefail
cd "$(dirname "$0")"
shopt -s nullglob
svgs=( *.svg )
[ ${#svgs[@]} -eq 0 ] && { echo "No .svg here; nothing to build."; exit 0; }
PY=""
for cand in python3 python py; do
  if command -v "$cand" >/dev/null 2>&1 && "$cand" -c "import cairosvg" >/dev/null 2>&1; then PY="$cand"; break; fi
done
[ -z "$PY" ] && { echo "ERROR: no Python with cairosvg (tried python3, python, py). Install: python -m pip install cairosvg"; exit 2; }
echo "Using interpreter: $PY"
for s in "${svgs[@]}"; do
  pdf="${s%.svg}.pdf"
  "$PY" -c "import cairosvg; cairosvg.svg2pdf(url='$s', write_to='$pdf')" && echo "  [ok] $pdf" || { echo "  [FAIL] $s"; exit 1; }
done
echo "Done: ${#svgs[@]} figure(s) built."
