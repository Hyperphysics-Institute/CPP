#!/usr/bin/env bash
# =============================================================================
# cap.sh  --  low-friction per-turn verbatim capture from chat.
#
# Source it once from ~/.bashrc:
#     source ~/Documents/GitHub/CPP/scripts/cap.sh
#
# Per-turn loop (every round, every word):
#   1. Copy the turn block the worker prints at the end of its reply.
#   2. Type:  cap        (reads the clipboard, appends to today's transcript)
# At session end:
#   3. Type:  cap-push   (one commit + push of the day's transcript)
#
# The macro (overnight_extraction_audit.sh) + a worker fragmentation pass then
# split the transcript into founder / reasoning / script / registry fragments.
# Optional:  cap-slug <name>   to tag a session (default "chat").
# =============================================================================
CPP_REPO="${CPP_REPO:-$HOME/Documents/GitHub/CPP}"

cap() {
  local dir="$CPP_REPO/Development/transcripts"
  mkdir -p "$dir" || { echo "cap: cannot reach $dir"; return 1; }
  local slug="${CAP_SLUG:-chat}"
  local f="$dir/$(date +%Y-%m-%d)_session_${slug}.md"
  if [[ ! -f "$f" ]]; then
    printf -- '---\nwindow-slug: %s\npatch: %s\nopened: %s\nformat: structured\n---\n\n' \
      "$slug" "${CAP_PATCH:-0}" "$(date '+%Y-%m-%d %H:%M %Z')" > "$f"
  fi
  if [[ -r /dev/clipboard ]]; then
    cat /dev/clipboard >> "$f"
  else
    echo "cap: no /dev/clipboard here — paste the block, then press Ctrl-D:"
    cat >> "$f"
  fi
  printf '\n' >> "$f"
  echo "captured -> ${f#$CPP_REPO/}   ($(grep -c '^### \[' "$f") turn-lines so far)"
}

cap-slug() { export CAP_SLUG="$1"; echo "capture slug = ${1:-chat}"; }

cap-push() {
  ( cd "$CPP_REPO" || return 1
    git add Development/transcripts/ \
      && git commit -m "transcript: $(date +%Y-%m-%d) session capture (${CAP_SLUG:-chat})" \
      && git push origin main \
      && echo "pushed today's transcript." )
}
