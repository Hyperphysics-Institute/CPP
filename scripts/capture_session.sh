#!/usr/bin/env bash
# =============================================================================
# capture_session.sh  --  best-effort raw transcript capture (the §3.1 backstop)
#
# Capture-and-Audit Protocol. Writes a session's verbatim transcript into
# Development/transcripts/ under the filename + format contract
# (Development/transcripts/README.md), so the overnight audit can parse it.
#
# THIS IS THE BEST-EFFORT BACKSTOP, NOT the §3.1 zero-touch mechanism. §3.1
# requires always-on / zero-touch / non-bypassable / fsync-durable capture; a
# manually-run helper does not satisfy that (it re-imports human-compliance-under-
# load). A true zero-touch integration (TLA/Isak, environment) MUST emit the SAME
# contract this script does, so the macro is indifferent to which produced a file.
# Until then this helper preserves the ground-truth raw material so nothing is lost.
#
# Usage:
#   scripts/capture_session.sh --slug <slug> --patch <n> [--opened "<ts>"] \
#       (--file <path> | < stdin)
#   echo "...transcript..." | scripts/capture_session.sh --slug dm-1 --patch 850
# =============================================================================
set -euo pipefail

SLUG=""; PATCH=""; OPENED=""; INFILE=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --slug)   SLUG="$2"; shift 2;;
    --patch)  PATCH="$2"; shift 2;;
    --opened) OPENED="$2"; shift 2;;
    --file)   INFILE="$2"; shift 2;;
    -h|--help) sed -n '2,20p' "$0"; exit 0;;
    *) echo "unknown arg: $1"; exit 2;;
  esac
done

# ---- preflight --------------------------------------------------------------
[[ -d .git && -f templates/capture_and_audit_protocol.md ]] || { echo "ABORT: run from the CPP repo root."; exit 2; }
[[ -d Development/transcripts ]] || { echo "ABORT: Development/transcripts/ missing (run the Step-3 scaffold)."; exit 2; }
[[ -n "$SLUG" ]]  || { echo "ABORT: --slug required."; exit 2; }
[[ -n "$PATCH" ]] || { echo "ABORT: --patch required."; exit 2; }
# slug must be filename-safe and collision-key clean (no spaces/slashes/quotes)
[[ "$SLUG" =~ ^[A-Za-z0-9._-]+$ ]] || { echo "ABORT: --slug must be [A-Za-z0-9._-] (it is the collision key)."; exit 2; }
[[ "$PATCH" =~ ^[0-9]+$ ]]         || { echo "ABORT: --patch must be numeric."; exit 2; }
[[ -n "$OPENED" ]] || OPENED="$(date '+%Y-%m-%d %H:%M %Z')"

# ---- read the body (file or stdin) -----------------------------------------
if [[ -n "$INFILE" ]]; then
  [[ -f "$INFILE" ]] || { echo "ABORT: --file not found: $INFILE"; exit 2; }
  BODY="$(cat "$INFILE")"
else
  [[ -t 0 ]] && { echo "ABORT: no --file and no stdin. Pipe the transcript or pass --file."; exit 2; }
  BODY="$(cat)"
fi
[[ -n "${BODY//[$' \t\n']/}" ]] || { echo "ABORT: empty transcript body."; exit 2; }

# ---- detect format: structured (### [n] ROLE) vs raw ------------------------
if grep -qE '^### \[[0-9]+\] (TLA|WORKER)\b' <<<"$BODY"; then
  FORMAT="structured"
else
  FORMAT="raw"   # the macro routes raw files to the free-form pass, never silently drops
fi

# ---- compose the filename per the contract ---------------------------------
DATE="$(date -d "$OPENED" '+%Y-%m-%d' 2>/dev/null || date '+%Y-%m-%d')"
TIME="$(date -d "$OPENED" '+%H%M'      2>/dev/null || date '+%H%M')"
OUT="Development/transcripts/${DATE}_${TIME}_p${PATCH}_${SLUG}.md"
[[ -e "$OUT" ]] && { echo "ABORT: refusing to overwrite existing $OUT (pick a distinct slug/time)."; exit 2; }

# ---- write with front matter; fsync via sync -------------------------------
{
  printf -- '---\n'
  printf 'window-slug: %s\n' "$SLUG"
  printf 'patch: %s\n'       "$PATCH"
  printf 'opened: %s\n'      "$OPENED"
  printf 'format: %s\n'      "$FORMAT"
  printf -- '---\n\n'
  printf '%s\n' "$BODY"
} > "$OUT"
sync "$OUT" 2>/dev/null || sync

echo "captured: $OUT   (format=$FORMAT)"
[[ "$FORMAT" == "raw" ]] && echo "note: unstructured body -> the audit will route it to the free-form pass (flagged, not dropped)."
echo "Next: commit + push as usual; the overnight audit will mine it when built/scheduled."
