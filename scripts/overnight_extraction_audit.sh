#!/usr/bin/env bash
# =============================================================================
# overnight_extraction_audit.sh  --  the nightly extraction audit (SKELETON)
#
# Campaign: the Capture-and-Audit Protocol (2100-band). Step 4, Patch 2104.
# Spec: templates/capture_and_audit_protocol.md  (§4 = this script).
# Pattern: modeled on scripts/consolidate_bibliography.sh (Isak) -- inherit its
#          rails (dry-run first, verify-after-act, [REVIEW]-on-ambiguity, clean
#          tree on every exit, NEVER auto-commit). Do not rewrite his protocol.
#
# WHAT THIS DOES (each night, on the LOCAL machine -- NOT the container):
#   reads Development/transcripts/* for the day -> splits every verbatim turn
#   into fragments -> files each to its home (reasoning/, verify/, founders,
#   registry deltas) -> writes a heartbeat to Development/audit_log.md.
#
# v1 SAFETY STANCE (this skeleton): the audit STAGES proposed changes for TLA;
#   it does NOT write canonical files directly. founders_vision.md promotion and
#   registry merges are produced as a staged plan under Development/staging/<date>/
#   for TLA to review and apply. The ONLY direct write is the heartbeat (an
#   operational log, not canonical). v2 (direct canonical writes) is gated on the
#   [REVIEW] rail being proven over time -- see promote_founders() -- and is NOT
#   ENABLED here.
#
# SKELETON SCOPE: the phase structure, the preflight GATE, --dry-run, the
#   founders-voice [REVIEW] POLICY, the heartbeat, and the clean-tree discipline
#   are real. The judgment-heavy extraction steps (turn-splitting, discipline
#   classification, registry-delta detection) are STUBS with explicit output
#   contracts -- they are honest TODOs, not faked intelligence. Every stub whose
#   detector is uncertain resolves CONSERVATIVELY (-> [REVIEW] / -> no write).
# =============================================================================
set -euo pipefail

# ---- config -----------------------------------------------------------------
TZ_LABEL="$(date +%Z)"
RUN_DATE="$(date +%Y-%m-%d)"          # override with --date YYYY-MM-DD
DRY_RUN=1                              # DEFAULT: dry-run. --apply to stage.
ONLY=""                               # --only founders|reasoning|registry|scripts
TRANSCRIPTS_DIR="Development/transcripts"
AUDIT_LOG="Development/audit_log.md"
STAGING_ROOT="Development/staging"
FOUNDERS_CANON="founders_vision.md"

# ---- counters (for the heartbeat line) --------------------------------------
N_TRANSCRIPTS=0
N_REASONING=0; N_SCRIPTS=0; N_REGISTRY=0
N_F_STAGED=0; N_F_REVIEW=0; N_F_PROMOTED=0
RUN_STATUS="OK"

usage() {
  cat <<'EOF'
Usage: overnight_extraction_audit.sh [--apply] [--date YYYY-MM-DD] [--only KIND]
  (default)        dry-run: print the plan-of-record, write NOTHING.
  --apply          stage proposed changes under Development/staging/<date>/ and
                   write the heartbeat. Does NOT touch canonical files (v1).
  --date D         audit transcripts for date D (default: today).
  --only KIND      restrict to one of: founders | reasoning | registry | scripts
  -h, --help       this help.
EOF
}

log()  { printf '%s\n' "$*"; }
plan() { printf '  [PLAN] %s\n' "$*"; }       # dry-run: what WOULD happen
act()  { printf '  [STAGE] %s\n' "$*"; }      # apply: what was staged

# =============================================================================
# PHASE 0 -- preflight GATE (must pass or we abort before touching anything)
# =============================================================================
phase0_preflight() {
  log "== Phase 0: preflight =="
  # 0.1 repo root
  if [[ ! -d .git ]] || [[ ! -f templates/capture_and_audit_protocol.md ]]; then
    log "ABORT: run from the CPP repo root (need .git and the protocol doc)."; exit 2
  fi
  # 0.2 required tools present (this is a real-machine job, not the container)
  for t in git grep sed awk find date; do
    command -v "$t" >/dev/null 2>&1 || { log "ABORT: missing tool: $t"; exit 2; }
  done
  # 0.3 clean tree unless dry-run (we must be able to distinguish OUR staging
  #     writes from pre-existing dirt, exactly as Isak's audit requires)
  if [[ $DRY_RUN -eq 0 ]]; then
    if [[ -n "$(git status --porcelain)" ]]; then
      log "ABORT: working tree not clean. Commit/stash first, or use --dry-run."; exit 2
    fi
  fi
  # 0.4 capture trees exist
  [[ -d "$TRANSCRIPTS_DIR" ]] || { log "ABORT: $TRANSCRIPTS_DIR missing (run Step 3 scaffold)."; exit 2; }
  [[ -f "$AUDIT_LOG" ]]       || { log "ABORT: $AUDIT_LOG missing (run Step 3 scaffold)."; exit 2; }
  log "  preflight OK (mode: $([[ $DRY_RUN -eq 1 ]] && echo DRY-RUN || echo APPLY), date: $RUN_DATE)"
}

# =============================================================================
# PHASE 1 -- read the day's transcripts (REAL)
# =============================================================================
TRANSCRIPTS=()
phase1_read() {
  log "== Phase 1: read transcripts for $RUN_DATE =="
  # filename contract: YYYY-MM-DD_HHMM_p<patch>_<window-slug>.md
  while IFS= read -r f; do TRANSCRIPTS+=("$f"); done < <(
    find "$TRANSCRIPTS_DIR" -maxdepth 1 -type f -name "${RUN_DATE}_*.md" | sort
  )
  N_TRANSCRIPTS=${#TRANSCRIPTS[@]}
  log "  found $N_TRANSCRIPTS transcript(s)"
  for f in "${TRANSCRIPTS[@]:-}"; do [[ -n "$f" ]] && log "    - $f"; done
  if [[ $N_TRANSCRIPTS -eq 0 ]]; then
    log "  (nothing to audit for $RUN_DATE -- will still write a heartbeat)"
  fi
}

# =============================================================================
# PHASE 2 -- split turns into fragments and file by class
#   STUB: turn-splitting + discipline classification is genuine judgment (NLP).
#   Contract each stub must satisfy is documented inline. Conservative default:
#   anything the classifier is unsure about is filed to a [REVIEW] bucket, never
#   guessed into a canonical home.
# =============================================================================
phase2_split_and_file() {
  [[ -n "$ONLY" && "$ONLY" != "reasoning" && "$ONLY" != "scripts" && "$ONLY" != "registry" ]] && return 0
  log "== Phase 2: split + file (reasoning / scripts / registry deltas) =="
  for f in "${TRANSCRIPTS[@]:-}"; do
    [[ -z "$f" ]] && continue
    # CONTRACT (TODO, real impl): parse $f into ordered turns with role markers,
    # then for each turn emit zero+ fragments tagged {reasoning|script|registry|
    # founder|procedural}. Procedural turns are dropped. Each non-founder fragment
    # is staged to its home with a provenance line back to $f.
    plan "split '$f' -> reasoning/, verify/, registry deltas   [STUB: classifier TODO]"
  done
  # counters stay 0 until the classifier lands; honest, not faked.
}

# =============================================================================
# PHASE 3 -- registry-delta merge
#   v1: STAGE deltas for TLA (canonical-registry edits are deferred to TLA).
# =============================================================================
phase3_registry() {
  [[ -n "$ONLY" && "$ONLY" != "registry" ]] && return 0
  log "== Phase 3: registry deltas (STAGED for TLA, not written canonical) =="
  # CONTRACT (TODO): from Phase-2 'registry'-tagged fragments, build a proposed
  # diff per canonical registry (theorem-registry, predictions, frontier sectors,
  # todo) into $STAGING_ROOT/$RUN_DATE/registry/. Never edit canonical here.
  plan "no registry deltas staged   [STUB: depends on Phase-2 classifier]"
}

# =============================================================================
# PHASE 4 -- founder's-voice path  (the high-risk path; policy is REAL)
# =============================================================================
# classify_founder_candidate(): the [REVIEW] policy, encoded.
# Returns "AUTO" only for a single, cleanly-bounded, unambiguously-attributed,
# verbatim, novel TLA passage with a clean context anchor and no normalization.
# ANY trigger below -> "REVIEW". Any uncertain/stubbed detector -> "REVIEW".
# Precision over recall on the AUTO path; the REVIEW queue is lossless.
#
#   1 BOUNDS         verbatim start/end not cleanly delimited
#   2 ATTRIBUTION    span not confidently TLA's own words
#   3 MULTIPLICITY   >1 distinct candidate passage in the fragment
#   4 CROSS-TURN     passage stitched across more than one turn
#   5 PARAPHRASE     only a reconstructed/paraphrased version exists
#   6 DUPLICATE      substantial overlap with an existing founders_vision entry
#   7 CONTEXT        no accurate 1-line context without inferring intent
#   8 NORMALIZATION  extraction needed more than trivial-whitespace cleanup
classify_founder_candidate() {
  # args: $1 = path to a candidate fragment file (staged scratch)
  # SKELETON: detectors are stubs. Per the global default they return REVIEW.
  # As detectors land, each flips to a real test; the DEFAULT must remain REVIEW.
  local cand="$1"
  # --- real, cheap detectors that CAN run now: -----------------------------
  # (6) DUPLICATE: if the candidate's first quoted line already appears verbatim
  #     in founders_vision.md, it's a probable duplicate -> REVIEW (reuse of the
  #     sweep_founder_contributions.sh promoted-vs-orphan idea).
  if [[ -f "$FOUNDERS_CANON" ]]; then
    local firstq
    firstq="$(grep -m1 '^> ' "$cand" 2>/dev/null | sed 's/^> //' | cut -c1-60 || true)"
    if [[ -n "$firstq" ]] && grep -qF -- "$firstq" "$FOUNDERS_CANON" 2>/dev/null; then
      echo "REVIEW:DUPLICATE"; return 0
    fi
  fi
  # (everything else): detectors TODO -> conservative default.
  echo "REVIEW:DEFAULT-CONSERVATIVE"; return 0
}

promote_founders() {
  [[ -n "$ONLY" && "$ONLY" != "founders" ]] && return 0
  log "== Phase 4: founder's-voice (v1 = STAGE for TLA; AUTO is the v2 target) =="
  local stage_dir="$STAGING_ROOT/$RUN_DATE/founders"
  # CONTRACT (TODO): Phase-2 'founder'-tagged fragments are written as candidate
  # blocks (each a verbatim '> ...' quote + a 1-line context) into scratch, then
  # classify_founder_candidate() labels each AUTO or REVIEW:<trigger>.
  # v1 stages BOTH classes into $stage_dir for TLA; AUTO ones are what v2 would
  # write directly once the rail is proven. NOTHING is written to $FOUNDERS_CANON.
  if [[ $DRY_RUN -eq 1 ]]; then
    plan "stage founder candidates -> $stage_dir (AUTO + [REVIEW] labelled)   [STUB: extractor TODO]"
    plan "founders_vision.md is NOT written in v1 (staged-first; AUTO is v2)"
  else
    mkdir -p "$stage_dir"
    act "staged 0 founder candidate(s) -> $stage_dir   [STUB: extractor TODO]"
    # When the extractor lands: for each candidate, verdict=$(classify_founder_candidate "$c")
    # -> increment N_F_STAGED, and N_F_REVIEW when verdict starts with REVIEW.
  fi
  # FIRST-RUN CARRY-OVER (handover §6 / build-plan §D): the five 2049-2058
  # contributions live in reasoning/ (they predate Development/transcripts/), so
  # the first sweep must read THERE, not in transcripts/. Handled as a documented
  # one-shot, NOT auto-merged with the daily path:
  #   (a) scalar-SSV ruling p2050  (b) velocity-emergence reframe p2052
  #   (c) inertia=B-field/DP-Sea p2055  (d) rigid-bolus correction p2056/57
  #   (e) exact-emergent-Lorentz campaign DECISION reasoning (no verbatim home)
  plan "first-run carry-over sweep of 2049-2058 reasoning/ -> staged   [STUB: one-shot TODO]"
}

# =============================================================================
# PHASE 5 -- heartbeat  (REAL; the anti-silent-rot rail)
# =============================================================================
write_heartbeat() {
  local now status line
  now="$(date +%H:%M)"
  status="$([[ $DRY_RUN -eq 1 ]] && echo "DRY-RUN" || echo "$RUN_STATUS")"
  # format pinned in Development/audit_log.md (Patch 2103):
  line="${RUN_DATE} ${now} ${TZ_LABEL} | run=${status} | transcripts=${N_TRANSCRIPTS} | filed=reasoning:${N_REASONING},scripts:${N_SCRIPTS},registry:${N_REGISTRY} | founders=staged:${N_F_STAGED},review:${N_F_REVIEW},promoted:${N_F_PROMOTED} | notes=skeleton"
  log "== Phase 5: heartbeat =="
  if [[ $DRY_RUN -eq 1 ]]; then
    plan "would append to $AUDIT_LOG:"
    log  "    $line"
  else
    printf '%s\n' "$line" >> "$AUDIT_LOG"
    act "appended heartbeat to $AUDIT_LOG"
  fi
}

# =============================================================================
# clean-tree discipline -- restore on EVERY exit path (SKIP/ERROR included)
# =============================================================================
on_exit() {
  local rc=$?
  if [[ $rc -ne 0 && $rc -ne 2 ]]; then
    RUN_STATUS="FAIL"
    log "!! audit errored (rc=$rc) -- a written FAIL heartbeat is recoverable; a MISSING one is the loud case."
    # best-effort heartbeat so the failure is LOUD-but-logged, never silent:
    [[ $DRY_RUN -eq 0 ]] && write_heartbeat || true
  fi
}
trap on_exit EXIT

# ---- arg parse --------------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --apply) DRY_RUN=0; shift;;
    --date)  RUN_DATE="$2"; shift 2;;
    --only)  ONLY="$2"; shift 2;;
    -h|--help) usage; exit 0;;
    *) log "unknown arg: $1"; usage; exit 2;;
  esac
done

# ---- run --------------------------------------------------------------------
log "### overnight extraction audit (skeleton) -- $RUN_DATE ($([[ $DRY_RUN -eq 1 ]] && echo DRY-RUN || echo APPLY)) ###"
phase0_preflight
phase1_read
phase2_split_and_file
phase3_registry
promote_founders
write_heartbeat

log ""
log "Next:"
log "  - DRY-RUN shown above. Re-run with --apply to stage under $STAGING_ROOT/$RUN_DATE/."
log "  - TLA reviews staged candidates; founders_vision.md + registries remain TLA-applied (v1)."
log "  - Build the Phase-2 classifier + Phase-4 extractor to replace the STUBs; keep the"
log "    classify_founder_candidate() DEFAULT at REVIEW until each detector is proven."
log "  - Confirm with TLA/Isak: nightly scheduler (cron / Task Scheduler) + that this runs"
log "    on the local machine, not the container."
