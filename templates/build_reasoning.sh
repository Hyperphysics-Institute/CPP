#!/usr/bin/env bash
# build_reasoning.sh -- concatenate per-patch reasoning fragments into a
# single readable per-paper/per-bucket view, in patch order.
#
# Part of the Session 146 reasoning-capture protocol
# (templates/reasoning_capture_protocol.md). The compiled output is an
# EPHEMERAL reading convenience; the per-patch fragments remain the canonical
# source of truth and are never replaced by the compiled view.
#
# Usage:
#   bash templates/build_reasoning.sh <reasoning-dir> [> output.md]
#
# Example:
#   bash templates/build_reasoning.sh hardened_theorems/reasoning > /tmp/dsl_full.md
#
# Fragments are sorted by filename, which (because fragments are named by
# zero-padded patch number, e.g. 0605.md, 0605a.md, 0606.md) yields correct
# patch order automatically.

set -euo pipefail

DIR="${1:-}"
if [[ -z "$DIR" || ! -d "$DIR" ]]; then
  echo "usage: bash templates/build_reasoning.sh <reasoning-dir>" >&2
  echo "  (directory of per-patch <patch>.md fragments)" >&2
  exit 2
fi

shopt -s nullglob
frags=( "$DIR"/*.md )
if (( ${#frags[@]} == 0 )); then
  echo "no .md fragments found in $DIR" >&2
  exit 1
fi

# Sort lexicographically: zero-padded patch numbers sort into patch order,
# with suffixed sub-patches (0605a) following their parent (0605).
IFS=$'\n' frags=( $(printf '%s\n' "${frags[@]}" | sort) )
unset IFS

printf '# Compiled reasoning view\n\n'
printf '_Generated %s from %s (%d fragments). EPHEMERAL — do not commit; fragments are canonical._\n\n' \
  "$(date -u +%Y-%m-%dT%H:%MZ)" "$DIR" "${#frags[@]}"
printf -- '---\n\n'

for f in "${frags[@]}"; do
  printf '\n\n<!-- ===== %s ===== -->\n\n' "$(basename "$f")"
  cat "$f"
  printf '\n'
done
