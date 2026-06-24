#!/usr/bin/env bash
# =============================================================================
# run_nightly_audit.sh  --  Task Scheduler / cron entry point for the overnight
# extraction audit. Pulls, runs the audit in --apply (STAGE-ONLY: it stages under
# Development/staging/ and clears Registries_pending/, but does NOT commit or push
# — TLA reviews + commits + pushes in the morning). All output is logged OUTSIDE
# the repo so run logs never dirty the tree.
#
# See Development/ACTIVATION.md for the runbook (scheduler entry, morning review,
# go-live checklist).
# =============================================================================
set -uo pipefail
REPO="$HOME/Documents/GitHub/CPP"
LOGDIR="$HOME/cpp_audit_runs"
mkdir -p "$LOGDIR"
exec >>"$LOGDIR/$(date +%Y-%m-%d).log" 2>&1

echo "=== nightly audit $(date '+%Y-%m-%d %H:%M:%S %Z') ==="
cd "$REPO" || { echo "ABORT: repo not found at $REPO"; exit 2; }

if ! git pull --rebase origin main; then
  echo "ABORT: 'git pull --rebase' failed — usually an un-reviewed/uncommitted staging tree from"
  echo "       a prior night. The audit is SKIPPED, so tonight's heartbeat will be MISSING — that"
  echo "       missing line is the loud flag at next bootup. Review + commit yesterday's staging,"
  echo "       then re-run, or wait for the next scheduled run."
  exit 1
fi

bash scripts/overnight_extraction_audit.sh --apply || { echo "audit returned nonzero — check the FAIL heartbeat in Development/audit_log.md"; exit 1; }

echo "=== done. Review Development/staging/$(date +%Y-%m-%d)/ in the morning, then commit + push. ==="
