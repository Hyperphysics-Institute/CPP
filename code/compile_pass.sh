#!/bin/bash
# compile_pass.sh -- Patch 4343 (in-folder build since 4344). Compile every deposit candidate (osf_deposit_manifest.json) twice with pdflatex in a
# scratch copy of its folder and report the number of LaTeX errors ("^!" lines) and the two most frequent kinds.
# Nothing in the repository is written. Usage: bash code/compile_pass.sh > compile_status_raw.txt
# Output lines: errors|path|top error kinds. Isak's deposit build needs 0 for every paper.
cd "$(dirname "$0")/.."
ROOT=$(pwd)
one() {
  # 4344: compile IN the paper's own folder (relative \graphicspath and \input resolve as in a real build);
  # auxiliary files go to a scratch -output-directory, so the tree is not written.
  f=$1; d=$(dirname "$f"); b=$(basename "$f" .tex); W=$(mktemp -d)
  cd "$ROOT/$d"
  for i in 1 2; do TEXINPUTS=".:$W:" BIBINPUTS=".:" timeout 150 pdflatex -interaction=nonstopmode -output-directory="$W" "$b.tex" >/dev/null 2>&1; done
  e=$(grep -c '^!' "$W/$b.log" 2>/dev/null); k=$(grep '^!' "$W/$b.log" 2>/dev/null | sed 's/(U+.*//' | sort | uniq -c | sort -rn | head -2 | tr -s ' ' | tr '\n' ';')
  echo "${e:-NA}|$f|$k"; cd /; rm -rf "$W"
}
export -f one; export ROOT
python3 -c "import json;print('\n'.join(p['rel'] for p in json.load(open('osf_deposit_manifest.json'))['papers']))" \
  | xargs -P 8 -I{} bash -c 'one "$@"' _ {} | sort -t'|' -k1 -nr
