#!/usr/bin/env bash
# =============================================================================
# overnight_extraction_audit.sh  --  the nightly extraction audit (Step 4)
#
# Capture-and-Audit Protocol §4. Runs on the LOCAL machine (real tools, not the
# container). Reads the day's Development/transcripts/* + Registries_pending/*,
# stages the deliberate/structured outputs for TLA's morning review, flags the
# free-form remainder, and writes a completeness-aware heartbeat.
#
# DETERMINISTIC core (implemented + tested):
#   - corpus-integrity check (C6): validate every transcript; flag malformed/orphaned.
#   - founder staging from @@FOUNDER: markers, via the §4.1 [REVIEW] policy.
#   - Registries_pending/ merge -> STAGED diff for TLA (canonical edits stay TLA-applied).
#   - schema-validation of pending deltas (C7) before staging.
#   - completeness-aware heartbeat (C2) + partial-night handling (C7).
# PLUGGABLE (safe default): free-form mining of un-marked prose is NOT done here;
#   such transcripts are FLAGGED to staging/freeform_pending (never dropped). An LLM
#   pass can slot in later.
#
# v1 STANCE: stages, never auto-commits canonical. founders_vision + registries are
# applied by TLA from the staging area (§4.1/§4.2). Only the heartbeat is written direct.
# =============================================================================
set -euo pipefail

DRY_RUN=1
RUN_DATE="$(date +%Y-%m-%d)"
ONLY=""
TRANSCRIPTS_DIR="Development/transcripts"
PENDING_DIR="Registries_pending"
AUDIT_LOG="Development/audit_log.md"
STAGING_ROOT="Development/staging"
FOUNDERS_CANON="founders_vision.md"
KNOWN_REGISTRIES="theorem-registry axiom-registry predictions paper_catalog research_frontier master_glossary theory-overview future_projects problem_histories README INDEX bibliography todolist research_timeline TATWD founders_vision"
# §6.1 temp-THEO-handle permanentize (Patch 2117)
ALIAS_MAP="Development/theo_alias_map.md"
GRACE_DAYS=2
TMP_RE='THEO-[A-Z0-9-]*-TMP-p[0-9]+(-[0-9]+)?'

# counters
T_SEEN=0; T_MALFORMED=0; ORPHAN_DELTAS=0
F_STAGED=0; F_REVIEW=0
R_STAGED=0; R_REVIEW=0
H_SEEN=0; H_PERM=0; H_ALIAS=0; H_REVIEW=0
FREEFORM=0
RUN_STATUS="OK"

log()  { printf '%s\n' "$*"; }
plan() { printf '  [PLAN] %s\n' "$*"; }
act()  { printf '  [STAGE] %s\n' "$*"; }

usage() {
  cat <<'EOF'
Usage: overnight_extraction_audit.sh [--apply] [--date YYYY-MM-DD] [--only KIND]
  (default)   dry-run: print the plan-of-record, write NOTHING.
  --apply     stage outputs under Development/staging/<date>/ + write heartbeat;
              clears processed Registries_pending files. Does NOT write canonical.
  --date D    audit transcripts/deltas for date D (default today).
  --only KIND founders | registry | freeform | integrity | permanentize
EOF
}

# front-matter value extractor: fm_get <file> <key>
fm_get() {
  awk -v key="$2" '
    NR==1 && $0=="---" {infm=1; next}
    infm && $0=="---" {exit}
    infm { p=index($0,": "); if (p>0){ k=substr($0,1,p-1); if(k==key){print substr($0,p+2); exit} } }
  ' "$1"
}

STAGE_DIR=""
stage_init() {
  STAGE_DIR="$STAGING_ROOT/$RUN_DATE"
  if [[ $DRY_RUN -eq 0 ]]; then
    rm -rf "$STAGE_DIR"   # idempotent: a re-run regenerates this date's staging cleanly
    mkdir -p "$STAGE_DIR/founders" "$STAGE_DIR/registry" "$STAGE_DIR/freeform_pending" "$STAGE_DIR/permanentize"
  fi
  return 0
}

# ---------------------------------------------------------------------------
# PHASE 0 -- preflight gate
# ---------------------------------------------------------------------------
phase0_preflight() {
  log "== Phase 0: preflight =="
  [[ -d .git && -f templates/capture_and_audit_protocol.md ]] || { log "ABORT: run from CPP repo root."; exit 2; }
  for t in git grep sed awk find date; do command -v "$t" >/dev/null 2>&1 || { log "ABORT: missing tool: $t"; exit 2; }; done
  [[ -d "$TRANSCRIPTS_DIR" ]] || { log "ABORT: $TRANSCRIPTS_DIR missing."; exit 2; }
  [[ -f "$AUDIT_LOG" ]]       || { log "ABORT: $AUDIT_LOG missing."; exit 2; }
  if [[ $DRY_RUN -eq 0 && -n "$(git status --porcelain)" ]]; then
    log "ABORT: working tree not clean (--apply needs to distinguish its own staging writes)."; exit 2
  fi
  log "  preflight OK (mode: $([[ $DRY_RUN -eq 1 ]] && echo DRY-RUN || echo APPLY), date: $RUN_DATE)"
}

# ---------------------------------------------------------------------------
# PHASE 1 -- corpus integrity (C6)
# ---------------------------------------------------------------------------
TRANSCRIPTS=()
phase1_integrity() {
  log "== Phase 1: corpus integrity =="
  local namerx='^[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{4}_p[0-9]+_[A-Za-z0-9._-]+\.md$'
  while IFS= read -r f; do
    [[ -z "$f" ]] && continue
    T_SEEN=$((T_SEEN+1))
    local base; base="$(basename "$f")"
    local bad=""
    [[ "$base" =~ $namerx ]] || bad="filename"
    # front matter closed + has slug + (raw OR >=1 turn) => not truncated
    local slug fmt; slug="$(fm_get "$f" window-slug)"; fmt="$(fm_get "$f" format)"
    [[ -n "$slug" ]] || bad="${bad:+$bad,}frontmatter"
    if [[ "$fmt" != "raw" ]] && ! grep -qE '^### \[[0-9]+\] (TLA|WORKER)\b' "$f"; then
      bad="${bad:+$bad,}no-turns"
    fi
    if [[ -n "$bad" ]]; then
      T_MALFORMED=$((T_MALFORMED+1)); log "  MALFORMED [$bad]: $base"
    fi
    TRANSCRIPTS+=("$f")
  done < <(find "$TRANSCRIPTS_DIR" -maxdepth 1 -type f -name "${RUN_DATE}_*.md" | sort)
  # orphaned deltas: a pending file whose slug has no same-day transcript
  if [[ -d "$PENDING_DIR" ]]; then
    while IFS= read -r p; do
      [[ -z "$p" ]] && continue
      local pslug; pslug="$(basename "$p" .md)"
      if ! ls "$TRANSCRIPTS_DIR/${RUN_DATE}_"*"_${pslug}.md" >/dev/null 2>&1; then
        ORPHAN_DELTAS=$((ORPHAN_DELTAS+1)); log "  ORPHAN-DELTA (no same-day transcript): $(basename "$p")"
      fi
    done < <(find "$PENDING_DIR" -maxdepth 1 -type f -name '*.md' ! -name 'README.md' 2>/dev/null | sort)
  fi
  log "  transcripts seen=$T_SEEN malformed=$T_MALFORMED orphan-deltas=$ORPHAN_DELTAS"
  return 0
}

# ---------------------------------------------------------------------------
# PHASE 3 -- founder staging from @@FOUNDER: markers (§4.1 [REVIEW] policy)
# ---------------------------------------------------------------------------
# classify a (quote, context): echoes AUTO or REVIEW:<trigger>
classify_founder() {
  local q="$1" ctx="$2"
  [[ -n "$q" && -n "$ctx" ]] || { echo "REVIEW:MALFORMED"; return; }
  # DUPLICATE: first 60 chars of the quote already present verbatim in canonical
  if [[ -f "$FOUNDERS_CANON" ]]; then
    local probe="${q:0:60}"
    grep -qF -- "$probe" "$FOUNDERS_CANON" 2>/dev/null && { echo "REVIEW:DUPLICATE"; return; }
  fi
  echo "AUTO"
}
phase3_founders() {
  [[ -n "$ONLY" && "$ONLY" != "founders" ]] && return 0
  log "== Phase 3: founder staging (@@FOUNDER markers) =="
  local out="$STAGE_DIR/founders/${RUN_DATE}_founders.md"
  [[ $DRY_RUN -eq 0 ]] && : > "$out"
  for f in "${TRANSCRIPTS[@]:-}"; do
    [[ -z "$f" ]] && continue
    while IFS= read -r line; do
      [[ -z "$line" ]] && continue
      # @@FOUNDER: "quote" | context: ctx
      local q ctx verdict
      q="$(sed -n 's/.*@@FOUNDER:[[:space:]]*"\([^"]*\)".*/\1/p' <<<"$line")"
      ctx="$(sed -n 's/.*context:[[:space:]]*\(.*\)$/\1/p' <<<"$line")"
      verdict="$(classify_founder "$q" "$ctx")"
      if [[ "$verdict" == "AUTO" ]]; then F_STAGED=$((F_STAGED+1)); else F_REVIEW=$((F_REVIEW+1)); fi
      if [[ $DRY_RUN -eq 1 ]]; then
        plan "founder [$verdict] from $(basename "$f"): \"${q:0:48}...\""
      else
        { printf '## [%s] %s\n' "$verdict" "$(basename "$f")"
          printf '> %s\n\n' "$q"
          printf '_context:_ %s\n\n' "$ctx"; } >> "$out"
      fi
    done < <(grep -h '@@FOUNDER:' "$f" 2>/dev/null || true)
  done
  log "  founders: staged(AUTO)=$F_STAGED review=$F_REVIEW"
  [[ $DRY_RUN -eq 0 ]] && act "founder candidates -> $out (TLA reviews/applies; nothing written to $FOUNDERS_CANON)"
  return 0
}

# ---------------------------------------------------------------------------
# PHASE 3.5 -- temporary-THEO-handle permanentize (§6.1, Patch 2117)
# Claim-driven (family+patch are read from the pending claim, never guessed from
# the handle, which sidesteps family-vs-display-guess ambiguity like THEO-SF-4).
# v1 stance: STAGES the corpus rename + theorem-registry registrations for TLA's
# morning apply; directly maintains the operational alias map (like the heartbeat).
# Auto-applying the corpus rename is a v2 graduation (explicit TLA action), mirroring
# the §4.1 founders posture. Safe to stage-not-apply because the handle is already
# unambiguous (the rename is cosmetic).
# ---------------------------------------------------------------------------
theo_family_max() {  # highest existing THEO-<fam>-<n> in the registry (0 if none)
  local fam="$1" m=0 n
  [[ -f theorem-registry.md ]] || { echo 0; return; }
  while IFS= read -r n; do [[ -n "$n" ]] && (( n > m )) && m=$n; done \
    < <(grep -oE "THEO-${fam}-[0-9]+([^0-9]|$)" theorem-registry.md 2>/dev/null | grep -oE '[0-9]+' || true)
  echo "$m"
}
theo_taken() { grep -qE "THEO-$1-$2([^0-9]|\$)" theorem-registry.md 2>/dev/null; }  # taken OR reserved

alias_expire() {  # drop alias entries past their grace window (ISO dates string-compare)
  [[ -f "$ALIAS_MAP" ]] || { printf '# THEO temp→permanent alias map (§6.1, auto-maintained)\n# Entries expire %s nights after assignment.\n\n' "$GRACE_DAYS" > "$ALIAS_MAP"; return 0; }
  local tmpf; tmpf="$(mktemp)"; local e
  while IFS= read -r l; do
    if [[ "$l" == \|*expires:* ]]; then
      e="$(sed -n 's/.*expires:\([0-9-]*\).*/\1/p' <<<"$l")"
      [[ -n "$e" && "$e" < "$RUN_DATE" ]] && continue   # expired -> drop
    fi
    printf '%s\n' "$l" >> "$tmpf"
  done < "$ALIAS_MAP"
  mv "$tmpf" "$ALIAS_MAP"
}

phase_permanentize() {
  [[ -n "$ONLY" && "$ONLY" != "permanentize" ]] && return 0
  log "== Phase 3.5: temp-THEO-handle permanentize (§6.1; STAGED + alias-map) =="
  [[ -d "$PENDING_DIR" ]] || { log "  (no $PENDING_DIR)"; return 0; }
  local plan_file="$STAGE_DIR/permanentize/${RUN_DATE}_rename_plan.md"
  local apply_file="$STAGE_DIR/permanentize/${RUN_DATE}_apply_rename.sh"
  local reg_delta="$STAGE_DIR/registry/theorem-registry.delta"
  local excl=(--exclude-dir=.git --exclude-dir=Development --exclude-dir=Registries_pending --exclude-dir=scripts --exclude-dir=templates --exclude-dir=node_modules)

  declare -A C_FAM C_PATCH C_SEQ C_STMT C_SRC
  local order=() h fam pat stmt seq

  # 1) gather TMP claims from pending files (claim = authoritative family + patch)
  while IFS= read -r p; do
    [[ -z "$p" ]] && continue
    local pslug; pslug="$(basename "$p" .md)"
    while IFS= read -r line; do
      [[ "$line" == *-TMP-p* ]] || continue
      h="$(grep -oE "$TMP_RE" <<<"$line" | head -1 || true)"; [[ -z "$h" ]] && continue
      fam="$(sed -n 's/.*family:[[:space:]]*\([A-Za-z0-9-]*\).*/\1/p' <<<"$line")"
      pat="$(sed -n 's/.*patch:[[:space:]]*\([0-9]*\).*/\1/p' <<<"$line")"
      stmt="$(sed -n 's/.*|[[:space:]]*"\([^"]*\)".*/\1/p' <<<"$line")"
      seq="$(sed -n 's/.*-TMP-p[0-9]\{1,\}-\([0-9]\{1,\}\)$/\1/p' <<<"$h")"; seq="${seq:-0}"
      H_SEEN=$((H_SEEN+1))
      if [[ -z "$fam" || -z "$pat" ]]; then          # schema gate (§4.3)
        H_REVIEW=$((H_REVIEW+1))
        [[ $DRY_RUN -eq 0 ]] && printf '%s | from=%s | REVIEW:SCHEMA(missing family/patch)\n' "$line" "$pslug" >> "$STAGE_DIR/permanentize/_REVIEW.txt"
        continue
      fi
      [[ -z "${C_FAM[$h]:-}" ]] && order+=("$h")
      C_FAM[$h]="$fam"; C_PATCH[$h]="$pat"; C_SEQ[$h]="$seq"; C_STMT[$h]="$stmt"; C_SRC[$h]="$pslug"
    done < "$p"
  done < <(find "$PENDING_DIR" -maxdepth 1 -type f -name '*.md' ! -name 'README.md' 2>/dev/null | sort)

  # 2) orphan handles: in the corpus but no claim -> REVIEW (family unknown, never guess)
  while IFS= read -r h; do
    [[ -z "$h" || -n "${C_FAM[$h]:-}" ]] && continue
    H_SEEN=$((H_SEEN+1)); H_REVIEW=$((H_REVIEW+1))
    [[ $DRY_RUN -eq 0 ]] && printf '%s | REVIEW:ORPHAN(no pending claim)\n' "$h" >> "$STAGE_DIR/permanentize/_REVIEW.txt"
  done < <(grep -rEoh "${excl[@]}" "$TMP_RE" . 2>/dev/null | sort -u || true)

  # 3) assign permanents per family, deterministic (patch then seq); stage plan+delta, alias direct
  if [[ $DRY_RUN -eq 0 ]]; then
    alias_expire
    { printf '# Temp-handle rename plan — %s (STAGED; apply with %s, then commit+push)\n\n' "$RUN_DATE" "$(basename "$apply_file")"; } > "$plan_file"
    { printf '#!/usr/bin/env bash\n# Staged temp-handle permanentization (§6.1). Review, run from repo root, commit+push.\nset -euo pipefail\ncd "$(git rev-parse --show-toplevel)"\n'; } > "$apply_file"
  fi
  local fams; fams="$(for h in "${order[@]:-}"; do [[ -n "$h" ]] && echo "${C_FAM[$h]}"; done | sort -u || true)"
  while IFS= read -r fam; do
    [[ -z "$fam" ]] && continue
    local sorted; sorted="$(for h in "${order[@]:-}"; do [[ -n "$h" && "${C_FAM[$h]}" == "$fam" ]] && printf '%s\t%s\t%s\n' "${C_PATCH[$h]}" "${C_SEQ[$h]}" "$h"; done | sort -k1,1n -k2,2n | cut -f3 || true)"
    local nextn; nextn=$(( $(theo_family_max "$fam") + 1 ))
    while IFS= read -r h; do
      [[ -z "$h" ]] && continue
      while theo_taken "$fam" "$nextn"; do nextn=$((nextn+1)); done   # skip taken/reserved slots
      local perm="THEO-${fam}-${nextn}"
      H_PERM=$((H_PERM+1))
      if [[ $DRY_RUN -eq 1 ]]; then
        plan "permanentize $h -> $perm (family $fam, patch ${C_PATCH[$h]})"
      else
        local occ; occ="$(grep -rEln "${excl[@]}" -- "$h" . 2>/dev/null | sort -u || true)"
        { printf '## %s  ->  %s   _(family %s, patch %s)_\n' "$h" "$perm" "$fam" "${C_PATCH[$h]}"
          if [[ -n "$occ" ]]; then printf '%s\n' "$occ" | sed 's/^/  - /'; else printf '  - (no corpus occurrence; alias-only)\n'; fi
          printf '\n'; } >> "$plan_file"
        if [[ -n "$occ" ]]; then
          while IFS= read -r ofile; do [[ -n "$ofile" ]] && printf 'sed -i "s/%s/%s/g" %q\n' "$h" "$perm" "$ofile" >> "$apply_file"; done <<<"$occ"
        fi
        printf -- '- register %s : permanentized from %s (patch %s) — "%s"\n' "$perm" "$h" "${C_PATCH[$h]}" "${C_STMT[$h]}" >> "$reg_delta"
        local exp; exp="$(date -d "$RUN_DATE +${GRACE_DAYS} days" +%Y-%m-%d 2>/dev/null || echo "$RUN_DATE")"
        printf '| %s | %s | assigned:%s | expires:%s |\n' "$h" "$perm" "$RUN_DATE" "$exp" >> "$ALIAS_MAP"
        H_ALIAS=$((H_ALIAS+1))
      fi
      nextn=$((nextn+1))
    done <<<"$sorted"
  done <<<"$fams"

  # 4) consume the TMP claim lines so Phase 4 doesn't re-see them (non-TMP deltas survive)
  if [[ $DRY_RUN -eq 0 ]]; then
    while IFS= read -r p; do
      [[ -z "$p" ]] && continue
      if grep -q -- '-TMP-p' "$p" 2>/dev/null; then
        local tf; tf="$(mktemp)"; grep -v -- '-TMP-p' "$p" > "$tf" || true; mv "$tf" "$p"
        act "consumed TMP claims from $(basename "$p")"
      fi
    done < <(find "$PENDING_DIR" -maxdepth 1 -type f -name '*.md' ! -name 'README.md' 2>/dev/null | sort)
    [[ $H_PERM -gt 0 ]] && act "rename plan + apply script -> $STAGE_DIR/permanentize/ ; alias map -> $ALIAS_MAP (TLA applies rename)"
  fi
  log "  permanentize: seen=$H_SEEN permanentized=$H_PERM aliased=$H_ALIAS review=$H_REVIEW"
  return 0
}

# ---------------------------------------------------------------------------
# PHASE 4 -- Registries_pending merge -> STAGED diff (C7 schema-validate first)
# ---------------------------------------------------------------------------
known_registry() { grep -qw -- "$1" <<<"$KNOWN_REGISTRIES"; }
phase4_registry() {
  [[ -n "$ONLY" && "$ONLY" != "registry" ]] && return 0
  log "== Phase 4: registry merge (STAGED for TLA; canonical not written) =="
  [[ -d "$PENDING_DIR" ]] || { log "  (no $PENDING_DIR)"; return 0; }
  while IFS= read -r p; do
    [[ -z "$p" ]] && continue
    local pslug; pslug="$(basename "$p" .md)"
    while IFS= read -r line; do
      [[ "$line" =~ ^-[[:space:]] ]] || continue
      [[ "$line" == *-TMP-p* ]] && continue   # §6.1 temp-handle claims belong to Phase 3.5
      local reg act_str
      reg="$(sed -n 's/^-[[:space:]]*registry=\([^ |]*\).*/\1/p' <<<"$line")"
      act_str="$(sed -n 's/.*action="\([^"]*\)".*/\1/p' <<<"$line")"
      # schema validation
      if [[ -z "$reg" || -z "$act_str" ]] || ! known_registry "$reg"; then
        R_REVIEW=$((R_REVIEW+1))
        if [[ $DRY_RUN -eq 1 ]]; then plan "registry [REVIEW:SCHEMA] from $pslug: ${line:0:60}"
        else printf '%s | from=%s | %s\n' "$line" "$pslug" "REVIEW:SCHEMA" >> "$STAGE_DIR/registry/_REVIEW.txt"; fi
        continue
      fi
      R_STAGED=$((R_STAGED+1))
      if [[ $DRY_RUN -eq 1 ]]; then
        plan "registry [$reg] <= \"$act_str\" (from $pslug)"
      else
        printf -- '- %s | from=%s\n' "$act_str" "$pslug" >> "$STAGE_DIR/registry/${reg}.delta"
      fi
    done < "$p"
    # processed all lines (valid->staged, invalid->_REVIEW): clear the file. Re-run safe
    # because staging is regenerated per-run (stage_init) and the file is now empty.
    if [[ $DRY_RUN -eq 0 ]]; then
      { printf -- '---\nwindow-slug: %s\n---\n# Pending registry deltas — %s   (cleared by audit %s)\n' "$pslug" "$pslug" "$RUN_DATE"; } > "$p"
      act "merged + cleared $PENDING_DIR/$(basename "$p")"
    fi
  done < <(find "$PENDING_DIR" -maxdepth 1 -type f -name '*.md' ! -name 'README.md' 2>/dev/null | sort)
  log "  registry: staged=$R_STAGED review=$R_REVIEW"
  return 0
}

# ---------------------------------------------------------------------------
# PHASE 5 -- free-form pass (PLUGGABLE; safe default = flag, never drop)
# ---------------------------------------------------------------------------
phase5_freeform() {
  [[ -n "$ONLY" && "$ONLY" != "freeform" ]] && return 0
  log "== Phase 5: free-form pass (flag for mining; not extracted in v1) =="
  local ptr="$STAGE_DIR/freeform_pending/${RUN_DATE}_pending.txt"
  [[ $DRY_RUN -eq 0 ]] && : > "$ptr"
  for f in "${TRANSCRIPTS[@]:-}"; do
    [[ -z "$f" ]] && continue
    # a transcript needs mining if it has substantive (non-@@FOUNDER, non-procedural) content
    # v1 heuristic: flag every transcript that carries any non-marker body; conservative = flag all.
    FREEFORM=$((FREEFORM+1))
    if [[ $DRY_RUN -eq 1 ]]; then plan "freeform-pending: $(basename "$f")"
    else printf '%s\n' "$f" >> "$ptr"; fi
  done
  log "  freeform-pending transcripts=$FREEFORM (awaiting LLM/manual mining pass)"
  return 0
}

# ---------------------------------------------------------------------------
# heartbeat (C2 completeness-aware)
# ---------------------------------------------------------------------------
write_heartbeat() {
  local now status line open_review
  now="$(date +%H:%M)"; local tz; tz="$(date +%Z)"
  status="$([[ $DRY_RUN -eq 1 ]] && echo "DRY-RUN" || echo "$RUN_STATUS")"
  open_review=$((F_REVIEW + R_REVIEW + H_REVIEW))
  line="${RUN_DATE} ${now} ${tz} | run=${status} | transcripts=${T_SEEN}(malformed:${T_MALFORMED},orphan-deltas:${ORPHAN_DELTAS}) | filed=reasoning:0,scripts:0,registry:${R_STAGED} | founders=staged:${F_STAGED},review:${F_REVIEW},promoted:0 | temp_handles=seen:${H_SEEN},perm:${H_PERM},alias:${H_ALIAS},review:${H_REVIEW} | open_review=${open_review} | freeform_pending=${FREEFORM} | notes=v1-deterministic"
  log "== heartbeat =="
  if [[ $DRY_RUN -eq 1 ]]; then plan "would append: $line"; else printf '%s\n' "$line" >> "$AUDIT_LOG"; act "heartbeat -> $AUDIT_LOG"; fi
  return 0
}

# ---------------------------------------------------------------------------
# partial-night handling: FAIL heartbeat on error (recoverable; a MISSING line is the loud case)
# ---------------------------------------------------------------------------
on_exit() {
  local rc=$?
  if [[ $rc -ne 0 && $rc -ne 2 ]]; then
    RUN_STATUS="FAIL"
    log "!! errored (rc=$rc) -- writing FAIL heartbeat; un-cleared pending files retry next run."
    [[ $DRY_RUN -eq 0 ]] && { write_heartbeat || true; }
  fi
}
trap on_exit EXIT

# ---- args + run -------------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --apply) DRY_RUN=0; shift;;
    --date)  RUN_DATE="$2"; shift 2;;
    --only)  ONLY="$2"; shift 2;;
    -h|--help) usage; exit 0;;
    *) log "unknown arg: $1"; usage; exit 2;;
  esac
done

log "### overnight extraction audit -- $RUN_DATE ($([[ $DRY_RUN -eq 1 ]] && echo DRY-RUN || echo APPLY)) ###"
phase0_preflight
stage_init
phase1_integrity
phase3_founders
phase_permanentize
phase4_registry
phase5_freeform
write_heartbeat
log ""
log "Next:"
log "  - Review Development/staging/$RUN_DATE/: founders/ (apply approved -> founders_vision.md, push),"
log "    registry/*.delta (apply -> canonical registries, push), freeform_pending/ (mine later)."
log "  - Clear resolved [REVIEW] items (founders + registry/_REVIEW.txt) as a blocking morning step (§4.2)."
log "  - Re-run is retry-safe: un-cleared pending files are reprocessed; a missing heartbeat is the loud case."
