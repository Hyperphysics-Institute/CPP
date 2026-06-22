#!/usr/bin/env bash
# Sweep FOUNDER CONTRIBUTION (verbatim — TLA) blocks across reasoning fragments and flag which
# are not yet promoted into founders_vision.md. READ-ONLY. Promotion is the integrator's call.
# Usage:  bash templates/sweep_founder_contributions.sh [repo_root]   (default: .)
set -uo pipefail
ROOT="${1:-.}"
VISION="$ROOT/founders_vision.md"
MARK='FOUNDER CONTRIBUTION (verbatim'

echo "=================================================================="
echo " Founder-contribution sweep (Reasoning-Capture Protocol §10)"
echo "=================================================================="
[ -f "$VISION" ] || echo "WARN: $VISION not found — every block will read as ORPHAN."

files=$(grep -rl "$MARK" "$ROOT" --include="*.md" 2>/dev/null | grep "/reasoning/" | sort)
if [ -z "$files" ]; then echo "No FOUNDER CONTRIBUTION blocks found in any /reasoning/ fragment yet."; exit 0; fi

orphans=0; total=0
while IFS= read -r f; do
  [ -z "$f" ] && continue
  # one summary line per marker occurrence in the file; snippet = first ~10 words of the next quoted line
  nblocks=$(grep -c "$MARK" "$f")
  snippet=$(grep -A8 "$MARK" "$f" | grep -m1 '^>' | sed 's/^>[[:space:]]*//;s/^"//' | tr -s ' ' | cut -d' ' -f1-10)
  status="ORPHAN — promote me"; total=$((total+1))
  if [ -n "$snippet" ] && [ -f "$VISION" ] && grep -qF "$snippet" "$VISION" 2>/dev/null; then
    status="promoted ✓"
  else
    orphans=$((orphans+1))
  fi
  echo ""
  echo "── $f   (${nblocks} block(s))"
  echo "   first-quote: ${snippet:-<no quoted '>' line found — check formatting>}"
  echo "   status     : $status"
done <<< "$files"

echo ""
echo "------------------------------------------------------------------"
echo "Files with blocks: $total   |   orphaned (not yet in founders_vision.md): $orphans"
echo "Promote orphans into founders_vision.md (dated, attributed, verbatim) and re-run."
echo "Note: files with >1 block are summarised by their FIRST quote; open them to promote all."
echo "------------------------------------------------------------------"
