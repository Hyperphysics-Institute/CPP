#!/usr/bin/env bash
# collision_audit.sh — Phase 0 GATE 0 verifier for CPP multi-window parallel development.
#
# Usage:   bash parallel_dev/scripts/collision_audit.sh <base_ref>
#   Audits every commit in <base_ref>..HEAD (one parallel round).
#   <base_ref> is the commit that existed just BEFORE the round began
#   (e.g. the value recorded in the lease board's base_ref field).
#
# Exit codes: 0 = GATE 0 PASS · 1 = FAIL · 2 = usage / nothing to audit.
#
# Checks:
#   1. Worker-file collisions  (FAIL) — a non-shared file touched by >1 commit.
#   2. Patch-number collisions (FAIL) — two commit subjects with the same 4-digit label.
#   3. Duplicate new IDs       (WARN) — an ID token added by >1 commit (review needed).
#   4. Tree clean / pushed     (FAIL/INFO) — working tree clean; HEAD vs origin/main.
#
# Runs on Git Bash (MINGW64); uses only git + POSIX text tools (no grep -P).

set -u

BASE="${1:-}"
if [ -z "$BASE" ]; then
  echo "usage: bash parallel_dev/scripts/collision_audit.sh <base_ref>"
  echo "       (audits <base_ref>..HEAD — one parallel round)"
  exit 2
fi

if ! git rev-parse --verify "$BASE" >/dev/null 2>&1; then
  echo "ERROR: '$BASE' is not a valid git ref."
  exit 2
fi

# Files that are SHARED by design — an integration commit may touch these, so
# they are excluded from the worker-file collision check.
SHARED_REGEX='^(theorem-registry\.md|predictions\.md|axiom-registry\.md|master_glossary\.md|research_frontier\.md|frontier_sectors/|todolist\.md|future_projects\.md|paper_catalog\.md|research_timeline\.md|organizational_frontier\.md|theory-overview\.md|programme_orientation\.md|README\.md|INDEX\.md|parallel_dev/lease_board\.md)'

COMMITS=$(git rev-list --reverse "${BASE}..HEAD")
if [ -z "$COMMITS" ]; then
  echo "Nothing to audit: no commits in ${BASE}..HEAD."
  exit 2
fi

echo "==================================================================="
echo " CPP Phase 0 collision audit   range: ${BASE}..HEAD"
echo "==================================================================="
git log --oneline "${BASE}..HEAD"
echo

FAIL=0
TMP=$(mktemp)
trap 'rm -f "$TMP" "$TMP".ids "$TMP".nums' EXIT

# ---- Check 1: worker-file collisions ------------------------------------
echo "--- Check 1: worker-file collisions ---"
: > "$TMP"
for c in $COMMITS; do
  git diff-tree --no-commit-id --name-only -r "$c" | while IFS= read -r f; do
    [ -z "$f" ] && continue
    if ! printf '%s\n' "$f" | grep -Eq "$SHARED_REGEX"; then
      printf '%s\n' "$f"
    fi
  done >> "$TMP"
done
DUP1=$(sort "$TMP" | uniq -d)
if [ -n "$DUP1" ]; then
  echo "FAIL: worker file(s) touched by more than one commit this round:"
  printf '%s\n' "$DUP1" | sed 's/^/    /'
  FAIL=1
else
  echo "PASS: no worker file touched by more than one commit."
fi
echo

# ---- Check 2: patch-number collisions -----------------------------------
echo "--- Check 2: patch-number label collisions ---"
: > "$TMP".nums
for c in $COMMITS; do
  # first 4-digit token in the subject line
  git log -1 --format='%s' "$c" | grep -oE '[0-9]{4}' | head -1
done >> "$TMP".nums
DUP2=$(sort "$TMP".nums | uniq -d)
if [ -n "$DUP2" ]; then
  echo "FAIL: duplicate patch-number label(s) in this round:"
  printf '%s\n' "$DUP2" | sed 's/^/    /'
  FAIL=1
else
  echo "PASS: every commit carries a distinct patch-number label."
fi
echo

# ---- Check 3: duplicate new IDs (warn) ----------------------------------
echo "--- Check 3: duplicate new IDs (review) ---"
: > "$TMP".ids
for c in $COMMITS; do
  # added lines only (leading '+'), pull recognised ID tokens, dedupe within the commit
  git show "$c" --unified=0 --format= 2>/dev/null \
    | grep '^+' \
    | grep -oE '(THEO|LEMMA|CORO|CONJ|PRED|OPEN|AXIM|PROP|FALS)-[A-Za-z0-9_-]+' \
    | sort -u
done >> "$TMP".ids
DUP3=$(sort "$TMP".ids | uniq -d)
if [ -n "$DUP3" ]; then
  echo "WARN: ID token(s) added by more than one commit — confirm these are"
  echo "      cross-references, not duplicate registrations:"
  printf '%s\n' "$DUP3" | sed 's/^/    /'
else
  echo "PASS: no ID token added by more than one commit."
fi
echo

# ---- Check 4: tree clean / pushed ---------------------------------------
echo "--- Check 4: working tree & push state ---"
if [ -n "$(git status --porcelain)" ]; then
  echo "FAIL: working tree is not clean (uncommitted changes present)."
  FAIL=1
else
  echo "PASS: working tree clean."
fi
if git rev-parse --verify origin/main >/dev/null 2>&1; then
  AHEAD=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "?")
  if [ "$AHEAD" = "0" ]; then
    echo "INFO: HEAD is level with origin/main (round pushed)."
  else
    echo "INFO: HEAD is $AHEAD commit(s) ahead of origin/main — remember to push."
  fi
else
  echo "INFO: origin/main not available locally (skipping push check)."
fi
echo

echo "==================================================================="
if [ "$FAIL" -eq 0 ]; then
  echo " GATE 0: PASS   (review any WARN above before clearing the round)"
  echo "==================================================================="
  exit 0
else
  echo " GATE 0: FAIL   (resolve the FAIL item(s) above; do not start next round)"
  echo "==================================================================="
  exit 1
fi
