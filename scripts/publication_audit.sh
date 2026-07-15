#!/usr/bin/env bash
# publication_audit.sh — end-of-sequence completion audit for a CPP paper SHIP.
#
# Usage:   bash scripts/publication_audit.sh <PAPER-ID>
#   e.g.   bash scripts/publication_audit.sh EU-1
#
# Purpose
#   The paper-completion checklist (templates/paper_completion_checklist.md) lists
#   every Phase-7A/7B artifact a SHIP must touch. A checklist catches "did you INTEND
#   each step"; it does NOT catch "did each step actually LAND." This script is the
#   mechanical backstop: it greps every mandated artifact for the paper ID and reports
#   PASS / MISSING per file, then runs the paper's verification script and (if available)
#   a LaTeX compile. It cannot be fooled by good intentions.
#
#   This is the Phase-7C completion audit (checklist item H6). It is DISTINCT from
#   parallel_dev/scripts/collision_audit.sh: that audits a parallel ROUND for COLLISIONS
#   (windows stepping on each other); this audits a single paper's SHIP for OMISSIONS
#   (mandated integration that silently dropped out). Complementary, not overlapping.
#
# Exit codes: 0 = PASS (all REQUIRED present + verify ok) · 1 = FAIL · 2 = usage.
#
# Runs on Git Bash (MINGW64); uses only POSIX text tools (no grep -P). Run from repo root.

set -u

ID="${1:-}"
if [ -z "$ID" ]; then
  echo "usage: bash scripts/publication_audit.sh <PAPER-ID>   (e.g. EU-1)"
  exit 2
fi

if [ ! -e "predictions.md" ] || [ ! -d ".git" ]; then
  echo "ERROR: run this from the CPP repository root (predictions.md / .git not found here)."
  exit 2
fi

echo "==================================================================="
echo " CPP publication-completion audit   paper: ${ID}"
echo "==================================================================="
echo

FAIL=0
WARN=0

# present <file> <label> <required:REQ|ADV>
# Greps <file> for the paper ID token; reports PASS / MISSING / (missing-file).
present () {
  f="$1"; label="$2"; req="$3"
  if [ ! -f "$f" ]; then
    if [ "$req" = "REQ" ]; then
      printf '  [FAIL] %-46s file not found: %s\n' "$label" "$f"; FAIL=1
    else
      printf '  [warn] %-46s file not found: %s\n' "$label" "$f"; WARN=$((WARN+1))
    fi
    return
  fi
  if grep -Fq "$ID" "$f"; then
    printf '  [PASS] %-46s %s\n' "$label" "$f"
  else
    if [ "$req" = "REQ" ]; then
      printf '  [FAIL] %-46s NOT referenced in %s\n' "$label" "$f"; FAIL=1
    else
      printf '  [warn] %-46s not referenced in %s\n' "$label" "$f"; WARN=$((WARN+1))
    fi
  fi
}

# --- locate the paper directory and .tex -----------------------------------
echo "--- Locating paper materials ---"
TEX=$(find . -path ./.git -prune -o -iname "${ID}_*.tex" -print 2>/dev/null | head -1)
if [ -n "$TEX" ]; then
  PAPERDIR=$(dirname "$TEX")
  printf '  [PASS] %-46s %s\n' "paper .tex" "$TEX"
else
  PAPERDIR=$(find . -path ./.git -prune -o -type d -iname "$ID" -print 2>/dev/null | head -1)
  printf '  [FAIL] %-46s no %s_*.tex found\n' "paper .tex" "$ID"; FAIL=1
fi
echo

# --- Phase 7B: programme-level registries & orientation docs (REQUIRED) -----
echo "--- Phase 7B: programme registries & orientation (REQUIRED) ---"
present "predictions.md"          "predictions.md (registered prediction)" REQ
present "paper_catalog.md"        "paper_catalog.md (C7)"                   REQ
present "theory-overview.md"      "theory-overview.md (C1)"                 REQ
present "programme_orientation.md" "programme_orientation.md (C10)"         REQ
present "README.md"               "README.md (D1)"                          REQ
present "INDEX.md"                 "INDEX.md (D2)"                           REQ
echo

# --- Phase 7B: advisory registries (paper-dependent) ------------------------
echo "--- Phase 7B: advisory (fire only if the paper touches them) ---"
present "master_glossary.md"      "master_glossary.md (C4)"                 ADV
present "axiom-registry.md"       "axiom-registry.md (C2, count ledger)"    ADV
present "future_projects.md"      "future_projects.md (C9)"                 ADV
present "bibliography/cpp_references.bib" "bibliography (C11)"               ADV
echo

# --- Phase 7A: per-paper materials ------------------------------------------
echo "--- Phase 7A: per-paper materials ---"
DOCSUITE="$PAPERDIR/documentation_suite"
if [ -d "$DOCSUITE" ]; then
  n=$(find "$DOCSUITE" -maxdepth 1 -type f -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
  if [ "$n" -ge 7 ]; then
    printf '  [PASS] %-46s %s (%s files)\n' "documentation suite (>=7) (A)" "$DOCSUITE" "$n"
  else
    printf '  [FAIL] %-46s %s (only %s files; expect >=7)\n' "documentation suite (A)" "$DOCSUITE" "$n"; FAIL=1
  fi
else
  printf '  [FAIL] %-46s no documentation_suite/ under %s\n' "documentation suite (A)" "$PAPERDIR"; FAIL=1
fi
# anthology chapter (advisory: flagship-class papers)
if ls book_project/chapters/${ID}_*.md >/dev/null 2>&1; then
  printf '  [PASS] %-46s %s\n' "anthology chapter (advisory)" "$(ls book_project/chapters/${ID}_*.md | head -1)"
else
  printf '  [warn] %-46s none book_project/chapters/%s_*.md\n' "anthology chapter (advisory)" "$ID"; WARN=$((WARN+1))
fi
# problem history (advisory: only if the paper opened an OPEN-<ID>)
if grep -Fq "OPEN-$ID" predictions.md 2>/dev/null || ls problem_histories/PH-OPEN-${ID}*.md >/dev/null 2>&1; then
  if ls problem_histories/PH-OPEN-${ID}*.md >/dev/null 2>&1; then
    printf '  [PASS] %-46s %s\n' "problem history (OPEN-$ID opened)" "$(ls problem_histories/PH-OPEN-${ID}*.md | head -1)"
  else
    printf '  [warn] %-46s OPEN-%s referenced but no PH-OPEN-%s.md\n' "problem history" "$ID" "$ID"; WARN=$((WARN+1))
  fi
fi
echo

# --- bibliography compliance (central-only, OS §10; BLOCKING) ---------------
echo "--- Bibliography compliance (central-only, OS §10) ---"
if [ -n "${PAPERDIR:-}" ] && [ -d "$PAPERDIR" ]; then
  LOCALBIB=$(find "$PAPERDIR" -maxdepth 1 -name "${ID}_references.bib" 2>/dev/null)
  if [ -n "$LOCALBIB" ]; then
    echo "  [FAIL] per-paper bibliography present (OS §10 central-only violation):"
    printf '%s\n' "$LOCALBIB" | sed 's/^/        /'; FAIL=1
  else
    echo "  [PASS] no ${ID} per-paper .bib (central-only)"
  fi
fi
if [ -n "${TEX:-}" ] && grep -Eq "bibliography\{[^}]*${ID}_references" "$TEX" 2>/dev/null; then
  echo "  [FAIL] .tex cites a per-paper bib; use \\bibliography{../../bibliography/cpp_references}"; FAIL=1
fi
# per-SERIES bib usage — OS §10 deprecates these too (blind-spot closed 2026-06-13,
# OPEN-WORKFLOW-1): the per-paper check above missed \bibliography{cpp_*_series},
# letting a new paper silently re-adopt a deprecated series bib. Basename-match so
# the central cpp_references is never flagged.
if [ -n "${TEX:-}" ]; then
  BIBTGT=$(grep -oE 'bibliography\{[^}]*\}' "$TEX" 2>/dev/null | head -1 | sed -E 's/.*\{([^}]*)\}/\1/; s#.*/##')
  case "$BIBTGT" in
    cpp_references) : ;;  # central bib — compliant
    cpp_*_series|gr_companion|references)
      echo "  [FAIL] .tex cites a per-series bib ($BIBTGT); OS §10 central-only — use \\bibliography{../../bibliography/cpp_references} (OPEN-WORKFLOW-1)"; FAIL=1 ;;
  esac
fi
echo

# --- placeholder-text scan in the paper dir (H2) ----------------------------
echo "--- Placeholder scan (H2: no TODO / [TO BE WRITTEN] / TBD left behind) ---"
if [ -n "${PAPERDIR:-}" ] && [ -d "$PAPERDIR" ]; then
  PH=$(grep -rIl -e 'TO BE WRITTEN' -e 'TODO' -e '\[TBD\]' -e 'PLACEHOLDER' "$PAPERDIR" 2>/dev/null)
  if [ -n "$PH" ]; then
    echo "  [warn] placeholder tokens found in:"; printf '%s\n' "$PH" | sed 's/^/        /'; WARN=$((WARN+1))
  else
    echo "  [PASS] no placeholder tokens in $PAPERDIR"
  fi
fi
echo

# --- verification script (H: run it) ----------------------------------------
echo "--- Verification script ---"
# Normalize the ID for filename matching: lowercase, strip dashes (EU-1 -> eu1, SF-4 -> sf4).
IDNORM=$(printf '%s' "$ID" | tr 'A-Z' 'a-z' | tr -d '-')
VSCRIPT=$(find . -path ./.git -prune -o -name "*${IDNORM}*numeric*.py" -print 2>/dev/null | head -1)
[ -z "$VSCRIPT" ] && VSCRIPT=$(find . -path ./.git -prune -o -name "*${IDNORM}*.py" -print 2>/dev/null | head -1)
if [ -n "$VSCRIPT" ] && [ -f "$VSCRIPT" ]; then
  printf '  running %s ...\n' "$VSCRIPT"
  if python3 "$VSCRIPT" >/tmp/pubaudit_vscript.log 2>&1 || python "$VSCRIPT" >/tmp/pubaudit_vscript.log 2>&1; then
    echo "  [PASS] verification script exited 0"
  else
    echo "  [FAIL] verification script exited non-zero (see /tmp/pubaudit_vscript.log)"; FAIL=1
  fi
else
  echo "  [warn] no verification script matching *$IDNORM*numeric*.py found"; WARN=$((WARN+1))
fi
echo

# --- Integrity gate (Patch 2477; OPEN-WORKFLOW-PREDICTION-AUDIT) ------------
# Checks the ARTIFACTS, not the prose: cited scripts exist / parse / are not
# stubs / carry no elision markers / declare non-stdlib imports; paper prose
# carries no live dimensional-necessity or withdrawn zero-parameter billing.
# Registered after the SR-1 triage (Patches 2471-2475). BLOCKING.
echo "--- Integrity gate (scripts/integrity_audit.py; BLOCKING) ---"
if command -v python3 >/dev/null 2>&1 || command -v python >/dev/null 2>&1; then
  PY=$(command -v python3 || command -v python)
  if "$PY" scripts/integrity_audit.py --paper "$ID"; then
    echo "  [PASS] integrity gate"
  else
    echo "  [FAIL] integrity gate (see findings above)"; FAIL=1
  fi
else
  echo "  [FAIL] no python interpreter found — integrity gate cannot run"; FAIL=1
fi
echo

# --- LaTeX compile (optional; skip cleanly if no pdflatex) ------------------
echo "--- LaTeX compile (optional) ---"
if [ -n "${TEX:-}" ] && command -v pdflatex >/dev/null 2>&1; then
  ( cd "$PAPERDIR" && pdflatex -interaction=nonstopmode -halt-on-error "$(basename "$TEX")" >/tmp/pubaudit_tex.log 2>&1 )
  if [ $? -eq 0 ]; then echo "  [PASS] pdflatex compiled (1 pass; run x3 for final refs/ToC)";
  else echo "  [FAIL] pdflatex error (see /tmp/pubaudit_tex.log)"; FAIL=1; fi
else
  echo "  [skip] pdflatex not available here — compile-check is the integrator's local/OSF step"
fi
echo

echo "==================================================================="
if [ "$FAIL" -eq 0 ]; then
  echo " PUBLICATION AUDIT: PASS   ($WARN advisory warning(s) — review, not blocking)"
  echo "==================================================================="
  exit 0
else
  echo " PUBLICATION AUDIT: FAIL   (resolve [FAIL] item(s) above before declaring SHIP complete)"
  echo "==================================================================="
  exit 1
fi
