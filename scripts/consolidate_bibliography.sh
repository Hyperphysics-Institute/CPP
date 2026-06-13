#!/usr/bin/env bash
# =============================================================================
# consolidate_bibliography.sh  —  OPEN-WORKFLOW-1 remediation (central-bib)
# v4 (13 Jun 2026): operator-accept + clean-tree —
#   (ADD --accept-review ID[,ID]) for a named paper, if Phase-2 finds the rendered
#           .bbl CHANGED (a [REVIEW]), KEEP the repoint and archive the legacy bib
#           (an operator-approved correction) instead of reverting. The diff is
#           still printed first. Use only after eyeballing a prior run's [REVIEW]
#           diff and confirming the change is a correction/enrichment, not a loss.
#   (FIX C) clean tree on non-accept: pdflatex rewrites the paper PDF non-
#           deterministically (timestamps) on every compile, so any processed
#           paper's *.pdf showed up 'modified' even when its .tex was reverted ->
#           left uncommittable residue. Now restores the tracked PDF (git checkout)
#           on every SKIP/ERROR/REVERT/REVIEW-revert path; only accepted/OK papers
#           keep their rebuilt-against-master PDF.
# v3 (13 Jun 2026): correctness fixes over v2 —
#   (FIX A) repoint substitution: the path contains '/', which collided with
#           perl's s/// delimiter -> substitution errored and SILENTLY no-op'd,
#           yet the .bbl came out identical (because nothing changed) and the
#           script printed a FALSE [OK] while archiving the local bib -> would
#           orphan the .tex. Now uses a delimiter that can't appear in the path
#           and applies the edit in python (no shell/regex-escaping hazard).
#   (FIX B) post-repoint VERIFICATION: after editing, assert the .tex actually
#           contains the new \bibliography{<relmaster>} and NO longer cites the
#           local bib. If the edit did not take, ABORT that paper as [ERROR]
#           (revert .tex, keep local bib) instead of trusting .bbl identity.
# v2 carried: forward-slash path, non-halt baseline compile (2 passes, judge on
#   .bbl), CRLF-normalized .bbl diff.
# RUN LOCALLY (needs working pdflatex+bibtex). Does NOT commit.
# Usage: --dry-run | --only ID[,ID] | --accept-review ID[,ID] | --keep-artifacts
# =============================================================================
set -uo pipefail
DRY_RUN=0; KEEP_ART=0; ONLY=""; ACCEPT_REVIEW=""
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --keep-artifacts) KEEP_ART=1 ;;
    --only) ONLY="${2:-}"; shift ;;
    --accept-review) ACCEPT_REVIEW="${2:-}"; shift ;;
    -h|--help) sed -n '2,28p' "$0"; exit 0 ;;
    *) echo "unknown flag: $1" >&2; exit 2 ;;
  esac; shift
done

MASTER="bibliography/cpp_references.bib"
ARCHIVE="archive/pre_consolidation_2026-04-15"
RC=0
say(){ printf '%s\n' "$*"; }
hr(){ printf -- '----------------------------------------------------------------------\n'; }

say "=== Phase 0: preflight ==="
[ -f "$MASTER" ] && [ -d .git ] || { echo "ERROR: run from the CPP repo root (need $MASTER and .git)."; exit 2; }
for t in pdflatex bibtex python3 git; do command -v "$t" >/dev/null 2>&1 || { echo "ERROR: '$t' not found on PATH."; exit 2; }; done
if [ "$DRY_RUN" -eq 0 ] && [ -n "$(git status --porcelain)" ]; then
  echo "ERROR: working tree is not clean. Commit/stash first."; exit 2
fi
say "  repo root OK; tools present; tree clean (or --dry-run)."

bib_keys(){ python3 - "$1" <<'PY'
import re,sys
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
for m in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,', t): print(m.group(1))
PY
}
bib_unique_entries(){ python3 - "$1" "$2" <<'PY'
import re,sys
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
have=set(l.strip() for l in open(sys.argv[2],encoding='utf-8') if l.strip())
out=[]; i=0; n=len(src)
while True:
    m=re.compile(r'@\w+\s*\{\s*([^,\s]+)\s*,').search(src,i)
    if not m: break
    key=m.group(1); start=m.start()
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

# Repoint every \bibliography{...} in a .tex to a given target (python, no regex-delim hazard).
# Prints "CHANGED" if it modified the file, "NOCHANGE" otherwise.
repoint_tex(){ python3 - "$1" "$2" <<'PY'
import re,sys
texpath, target = sys.argv[1], sys.argv[2]
s=open(texpath,encoding='utf-8',errors='replace').read()
new=re.sub(r'\\bibliography\{[^}]*\}', r'\\bibliography{%s}' % target, s)
if new!=s:
    open(texpath,'w',encoding='utf-8',newline='').write(new)
    print("CHANGED")
else:
    print("NOCHANGE")
PY
}
# Assert the .tex now cites target and cites no other \bibliography{...}. exit 0 ok.
verify_repoint(){ python3 - "$1" "$2" <<'PY'
import re,sys
texpath, target = sys.argv[1], sys.argv[2]
s=open(texpath,encoding='utf-8',errors='replace').read()
cites=re.findall(r'\\bibliography\{([^}]*)\}', s)
sys.exit(0 if cites and all(c==target for c in cites) else 1)
PY
}

declare -a PAIRS=()
while IFS= read -r b; do
  [ -f "$b" ] || continue
  name="$(basename "$b" .bib)"; id="${name%_references}"
  case "$name" in cpp_references) continue;; esac
  [ -n "$ONLY" ] && { case ",$ONLY," in *",$id,"*) :;; *) continue;; esac; }
  tex="$(grep -rl "bibliography{$name}" --include='*.tex' "$(dirname "$b")" 2>/dev/null | head -1)"
  [ -n "$tex" ] && PAIRS+=("$id|$b|$tex") || say "  [skip] $b — no .tex cites \\bibliography{$name}"
done < <(find series_relativity/papers series_standard_model/papers -maxdepth 1 -name '*_references.bib' 2>/dev/null | sort)
[ "${#PAIRS[@]}" -gt 0 ] || { say "No per-paper bibs to process."; exit 0; }
say "  targets: ${#PAIRS[@]} paper(s)."

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
    bib_keys "$MASTER" | sort -u > "$MKEYS"
  fi
done

hr; say "=== Phase 2: repoint + verify (.tex actually edited AND rendered .bbl identical) ==="
[ "$DRY_RUN" -eq 0 ] && mkdir -p "$ARCHIVE"
compile(){ ( cd "$1" \
    && pdflatex -interaction=nonstopmode "$2.tex" >/dev/null 2>&1; \
       bibtex "$2" >/dev/null 2>&1; \
       pdflatex -interaction=nonstopmode "$2.tex" >/dev/null 2>&1; \
       pdflatex -interaction=nonstopmode "$2.tex" >/dev/null 2>&1 ); }
norm(){ tr -d '\r' < "$1"; }
clean_art(){ [ "$KEEP_ART" -eq 1 ] && return; ( cd "$1" && rm -f "$2".aux "$2".bbl "$2".blg "$2".log "$2".out "$2".toc 2>/dev/null ); }
# pdflatex rewrites the PDF on every compile; restore the tracked copy when we did
# not accept the repoint, so a non-converting run leaves a clean working tree.
restore_pdf(){ git checkout -- "$1/$2.pdf" >/dev/null 2>&1 || true; }

for pair in "${PAIRS[@]}"; do
  IFS='|' read -r id b tex <<< "$pair"
  dir="$(dirname "$tex")"; base="$(basename "$tex" .tex)"
  relmaster="$(python3 -c "import os;print(os.path.relpath('${MASTER%.bib}', '$dir').replace('\\\\','/'))")"
  say ""; say "  [$id] $tex"
  if [ "$DRY_RUN" -eq 1 ]; then
    say "        would: baseline-compile -> repoint to \\bibliography{$relmaster} -> VERIFY edit took -> recompile -> diff .bbl (CRLF-norm) -> (identical) archive $b"
    continue
  fi
  compile "$dir" "$base"
  if [ ! -f "$dir/$base.bbl" ]; then
    say "        [SKIP] baseline produced no .bbl (inline \\bibitem, or genuine compile failure). Left untouched."; clean_art "$dir" "$base"; restore_pdf "$dir" "$base"; RC=1; continue
  fi
  base_bbl="$(mktemp)"; norm "$dir/$base.bbl" > "$base_bbl"
  cp "$tex" "$tex.wf1bak"
  ch="$(repoint_tex "$tex" "$relmaster")"
  if ! verify_repoint "$tex" "$relmaster"; then
    say "        [ERROR] repoint did NOT take (edit='$ch'); .tex still cites a local/other bib. Reverting; NOT archiving."
    mv -f "$tex.wf1bak" "$tex"; clean_art "$dir" "$base"; restore_pdf "$dir" "$base"; rm -f "$base_bbl"; RC=1; continue
  fi
  compile "$dir" "$base"
  if [ ! -f "$dir/$base.bbl" ]; then
    say "        [REVERT] recompile against master produced no .bbl. Restoring .tex."; mv -f "$tex.wf1bak" "$tex"; clean_art "$dir" "$base"; restore_pdf "$dir" "$base"; rm -f "$base_bbl"; RC=1; continue
  fi
  new_bbl="$(mktemp)"; norm "$dir/$base.bbl" > "$new_bbl"
  if diff -q "$base_bbl" "$new_bbl" >/dev/null 2>&1; then
    rm -f "$tex.wf1bak"; git mv "$b" "$ARCHIVE/$(basename "$b")" 2>/dev/null || mv "$b" "$ARCHIVE/"
    say "        [OK] .tex repointed (verified) AND rendered .bbl identical -> legacy bib archived. No OSF re-deposit."
  else
    say "        [REVIEW] rendered .bbl CHANGED after repoint. Diff:"
    diff "$base_bbl" "$new_bbl" | sed 's/^/            /' | head -60
    case ",$ACCEPT_REVIEW," in
      *",$id,"*)
        rm -f "$tex.wf1bak"; git mv "$b" "$ARCHIVE/$(basename "$b")" 2>/dev/null || mv "$b" "$ARCHIVE/"
        say "        [ACCEPTED-REVIEW] operator-approved ($id): repoint KEPT + legacy bib archived. Confirm OSF re-deposit per convention (reference-list cosmetics typically need none)."
        ;;
      *)
        say "        -> reverting (not in --accept-review). After confirming the diff is a correction/enrichment, re-run with: --accept-review $id"
        mv -f "$tex.wf1bak" "$tex"; restore_pdf "$dir" "$base"; RC=1
        ;;
    esac
  fi
  clean_art "$dir" "$base"; rm -f "$base_bbl" "$new_bbl"
done

hr; say "=== Phase 3: stray duplicate cleanup ==="
STRAY="series_standard_model/papers/cpp_references.bib"
if [ -f "$STRAY" ]; then
  if grep -rlq "bibliography{cpp_references}" --include='*.tex' series_standard_model 2>/dev/null; then
    say "  [keep] $STRAY IS referenced by a .tex — not removing (investigate)."
  elif [ "$DRY_RUN" -eq 1 ]; then say "  [dry-run] would remove unreferenced stray $STRAY"
  else git rm -q "$STRAY" 2>/dev/null || rm -f "$STRAY"; say "  [removed] unreferenced stray $STRAY"; fi
else say "  (no stray cpp_references.bib present)"; fi

hr; say "=== Done ($([ "$DRY_RUN" -eq 1 ] && echo DRY-RUN || echo APPLIED)) ==="
say "Next: review 'git diff'; for any [ACCEPTED-REVIEW] paper run 'bash scripts/publication_audit.sh <ID>', then commit (repointed .tex + archived bib + rebuilt PDF)."
say "Any plain [REVIEW] left? eyeball its diff, then re-run with --accept-review <ID> to apply it."
[ "$RC" -eq 0 ] && say "Result: clean." || say "Result: attention needed (see [SKIP]/[REVERT]/[REVIEW]/[ERROR] above; [ACCEPTED-REVIEW] is expected & committable)."
rm -f "$MKEYS" 2>/dev/null
exit $RC
