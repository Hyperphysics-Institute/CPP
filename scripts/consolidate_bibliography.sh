#!/usr/bin/env bash
# =============================================================================
# consolidate_bibliography.sh  —  OPEN-WORKFLOW-1 remediation (central-bib)
# =============================================================================
# Migrates each per-paper local bibliography into the single master
# (bibliography/cpp_references.bib) and repoints the paper's .tex, PROVING the
# rendered bibliography is unchanged by diffing the BibTeX-generated .bbl before
# and after. A paper is only converted if its .bbl is byte-identical post-repoint
# (=> same rendered citations => no OSF re-deposit needed). Any paper whose .bbl
# changes is reverted and flagged for manual review.
#
# RUN THIS LOCALLY (not in the CPP container): it requires a working pdflatex +
# bibtex, and the container cannot reliably compile the legacy papers.
#
# Scope (auto-discovered): per-paper  series_*/papers/<ID>_references.bib  files
# — i.e. SR-1, SM-6..10. The per-series bibs (cpp_*_series, gr_companion,
# references) are NOT touched: they must be content-classified first (see
# OPEN-WORKFLOW-1). The stray, unreferenced series_standard_model/papers/
# cpp_references.bib is removed in Phase 3.
#
# Does NOT commit. It mutates the working tree; you review `git diff` and commit.
#
# Usage:
#   bash scripts/consolidate_bibliography.sh --dry-run   # show plan, change nothing
#   bash scripts/consolidate_bibliography.sh             # do it (per-paper verified)
#   bash scripts/consolidate_bibliography.sh --only SR-1 # restrict to one/some IDs
# Flags:
#   --dry-run        Report the plan; make no changes.
#   --only ID[,ID]   Restrict to specific paper IDs (comma-separated).
#   --keep-artifacts Leave LaTeX build artifacts in place (default: clean them).
# Exit: 0 = all targeted papers converted or cleanly skipped; 1 = a paper needs
#       manual review (rendered refs changed) or a hard error occurred.
# =============================================================================
set -uo pipefail

# ---- flags ------------------------------------------------------------------
DRY_RUN=0; KEEP_ART=0; ONLY=""
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --keep-artifacts) KEEP_ART=1 ;;
    --only) ONLY="${2:-}"; shift ;;
    -h|--help) sed -n '2,40p' "$0"; exit 0 ;;
    *) echo "unknown flag: $1" >&2; exit 2 ;;
  esac
  shift
done

MASTER="bibliography/cpp_references.bib"
ARCHIVE="archive/pre_consolidation_2026-04-15"
RC=0
say(){ printf '%s\n' "$*"; }
hr(){ printf -- '----------------------------------------------------------------------\n'; }

# ---- Phase 0: preflight -----------------------------------------------------
say "=== Phase 0: preflight ==="
[ -f "$MASTER" ] && [ -d .git ] || { echo "ERROR: run from the CPP repo root (need $MASTER and .git)."; exit 2; }
for t in pdflatex bibtex python3 git; do command -v "$t" >/dev/null 2>&1 || { echo "ERROR: '$t' not found on PATH."; exit 2; }; done
if [ "$DRY_RUN" -eq 0 ] && [ -n "$(git status --porcelain)" ]; then
  echo "ERROR: working tree is not clean. Commit/stash first so the consolidation is an isolated, reviewable change."; exit 2
fi
say "  repo root OK; tools present; tree clean (or --dry-run)."

# ---- helper: list entry keys in a .bib (python, brace-aware) ----------------
bib_keys(){ python3 - "$1" <<'PY'
import re,sys
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
for m in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,', t): print(m.group(1))
PY
}

# ---- helper: emit full entries from $1 whose key is NOT in keyfile $2 -------
bib_unique_entries(){ python3 - "$1" "$2" <<'PY'
import re,sys
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
have=set(l.strip() for l in open(sys.argv[2],encoding='utf-8') if l.strip())
out=[]; i=0; n=len(src)
while True:
    m=re.compile(r'@\w+\s*\{\s*([^,\s]+)\s*,').search(src,i)
    if not m: break
    key=m.group(1); start=m.start()
    # find matching close brace from the entry's opening '{'
    b=src.index('{',m.start()); depth=0; j=b
    while j<n:
        c=src[j]
        if c=='{':depth+=1
        elif c=='}':
            depth-=1
            if depth==0: break
        j+=1
    entry=src[start:j+1]; i=j+1
    if key not in have: out.append(entry.strip())
print(("\n\n".join(out)).strip())
PY
}

# ---- discover targets -------------------------------------------------------
declare -a PAIRS=()
while IFS= read -r b; do
  [ -f "$b" ] || continue
  name="$(basename "$b" .bib)"                    # e.g. SR-1_references
  id="${name%_references}"                         # e.g. SR-1
  case "$name" in cpp_references) continue;; esac  # stray handled in Phase 3
  [ -n "$ONLY" ] && { case ",$ONLY," in *",$id,"*) :;; *) continue;; esac; }
  tex="$(grep -rl "bibliography{$name}" --include='*.tex' "$(dirname "$b")" 2>/dev/null | head -1)"
  [ -n "$tex" ] && PAIRS+=("$id|$b|$tex") || say "  [skip] $b — no .tex cites \\bibliography{$name}"
done < <(find series_relativity/papers series_standard_model/papers -maxdepth 1 -name '*_references.bib' 2>/dev/null | sort)

[ "${#PAIRS[@]}" -gt 0 ] || { say "No per-paper bibs to process."; exit 0; }
say "  targets: ${#PAIRS[@]} paper(s)."

# ---- Phase 1: merge unique entries into the master (collisions keep master) -
hr; say "=== Phase 1: merge unique legacy entries into $MASTER ==="
MKEYS="$(mktemp)"; bib_keys "$MASTER" | sort -u > "$MKEYS"
for pair in "${PAIRS[@]}"; do
  IFS='|' read -r id b tex <<< "$pair"
  uniq="$(bib_unique_entries "$b" "$MKEYS")"
  if [ -z "$uniq" ]; then say "  [$id] no unique entries (all keys already in master)."; continue; fi
  cnt="$(printf '%s\n' "$uniq" | grep -cE '^@')"
  if [ "$DRY_RUN" -eq 1 ]; then
    say "  [$id] would merge $cnt unique entr(y/ies): $(printf '%s' "$uniq" | grep -oE '@\w+\{[^,]+' | sed -E 's/@\w+\{//' | paste -sd, -)"
  else
    { printf '\n%% --- merged from %s (OPEN-WORKFLOW-1 consolidation) ---\n%s\n' "$b" "$uniq"; } >> "$MASTER"
    say "  [$id] merged $cnt unique entr(y/ies) into master."
    bib_keys "$MASTER" | sort -u > "$MKEYS"   # refresh so cross-paper dups dedupe
  fi
done

# ---- Phase 2: per-paper repoint + .bbl-identity verification ----------------
hr; say "=== Phase 2: repoint + verify (rendered .bbl must be byte-identical) ==="
[ "$DRY_RUN" -eq 0 ] && mkdir -p "$ARCHIVE"
compile(){ # $1=dir $2=texbase ; runs pdflatex+bibtex+pdflatex in $1, leaves .bbl
  ( cd "$1" && pdflatex -interaction=nonstopmode -halt-on-error "$2.tex" >/dev/null 2>&1 \
      && bibtex "$2" >/dev/null 2>&1 \
      && pdflatex -interaction=nonstopmode -halt-on-error "$2.tex" >/dev/null 2>&1 )
}
clean_art(){ [ "$KEEP_ART" -eq 1 ] && return; ( cd "$1" && rm -f "$2".aux "$2".bbl "$2".blg "$2".log "$2".out "$2".toc 2>/dev/null ); }

for pair in "${PAIRS[@]}"; do
  IFS='|' read -r id b tex <<< "$pair"
  dir="$(dirname "$tex")"; base="$(basename "$tex" .tex)"
  relmaster="$(python3 -c "import os;print(os.path.relpath('${MASTER%.bib}', '$dir'))")"
  say ""
  say "  [$id] $tex"
  if [ "$DRY_RUN" -eq 1 ]; then
    say "        would: baseline-compile -> repoint \\bibliography{$relmaster} -> recompile -> diff .bbl -> (identical) archive $b"
    continue
  fi
  # 1) baseline .bbl (as shipped)
  if ! compile "$dir" "$base"; then
    say "        [SKIP] baseline compile failed as-is (figures/deps?). Left untouched; handle manually."; clean_art "$dir" "$base"; RC=1; continue
  fi
  base_bbl="$(mktemp)"; cp "$dir/$base.bbl" "$base_bbl" 2>/dev/null || { say "        [SKIP] no .bbl produced (paper may use inline \\bibitem). Left untouched."; clean_art "$dir" "$base"; continue; }
  # 2) repoint
  cp "$tex" "$tex.wf1bak"
  perl -0pi -e "s/\\\\bibliography\\{[^}]*\\}/\\\\bibliography{$relmaster}/g" "$tex"
  # 3) recompile against master
  if ! compile "$dir" "$base"; then
    say "        [REVERT] recompile against master failed. Restoring .tex."; mv -f "$tex.wf1bak" "$tex"; clean_art "$dir" "$base"; rm -f "$base_bbl"; RC=1; continue
  fi
  new_bbl="$dir/$base.bbl"
  # 4) verify identical rendered bibliography
  if diff -q "$base_bbl" "$new_bbl" >/dev/null 2>&1; then
    rm -f "$tex.wf1bak"; git mv "$b" "$ARCHIVE/$(basename "$b")" 2>/dev/null || mv "$b" "$ARCHIVE/"
    say "        [OK] rendered .bbl identical -> repointed to master; legacy bib archived. No OSF re-deposit."
  else
    say "        [REVIEW] rendered .bbl CHANGED after repoint -> reverting. Inspect diff; this paper may need an OSF re-deposit:"
    diff "$base_bbl" "$new_bbl" | sed 's/^/            /' | head -40
    mv -f "$tex.wf1bak" "$tex"; RC=1
  fi
  clean_art "$dir" "$base"; rm -f "$base_bbl"
done

# ---- Phase 3: remove the stray, unreferenced master copy --------------------
hr; say "=== Phase 3: stray duplicate cleanup ==="
STRAY="series_standard_model/papers/cpp_references.bib"
if [ -f "$STRAY" ]; then
  if grep -rlq "bibliography{cpp_references}" --include='*.tex' series_standard_model 2>/dev/null; then
    say "  [keep] $STRAY IS referenced by a .tex — not removing (unexpected; investigate)."
  elif [ "$DRY_RUN" -eq 1 ]; then
    say "  [dry-run] would remove unreferenced stray $STRAY"
  else
    git rm -q "$STRAY" 2>/dev/null || rm -f "$STRAY"; say "  [removed] unreferenced stray $STRAY"
  fi
else
  say "  (no stray cpp_references.bib present)"
fi

# ---- summary ----------------------------------------------------------------
hr
say "=== Done ($([ "$DRY_RUN" -eq 1 ] && echo DRY-RUN || echo APPLIED)) ==="
say "Per-series bibs (cpp_*_series, gr_companion, references) were NOT touched —"
say "classify their collisions first (OPEN-WORKFLOW-1), then re-run with the loop"
say "extended to those .tex files, or convert them by hand using the same .bbl-diff check."
say ""
say "Next: review 'git diff' (master grew; .tex bib lines repointed; legacy bibs moved to $ARCHIVE),"
say "re-run 'bash scripts/publication_audit.sh <ID>' for each converted paper (bib-compliance now PASS),"
say "then commit. Any [REVIEW] paper above kept its local bib and needs a manual decision."
[ "$RC" -eq 0 ] && say "Result: clean." || say "Result: attention needed (see [SKIP]/[REVERT]/[REVIEW] above)."
rm -f "$MKEYS" 2>/dev/null
exit $RC
