# Reasoning capture — Patch 2120: cap.sh accepts paste-into-terminal (heredoc/stdin)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

TLA pasted the turn block directly into the bash prompt (the natural instinct) instead of copy→`cap`-from-
clipboard; bash tried to execute the text. Fixed cap.sh to match the instinct: `cap` now prefers piped/heredoc
stdin (`[[ ! -t 0 ]]`) over the clipboard, so `cap <<'CAPTURE_EOF' ...lines... CAPTURE_EOF` pasted+run as one
block captures correctly. Bare interactive `cap` still falls back to /dev/clipboard. Tested both.

Going forward the worker emits each turn as a ready-to-run `cap <<'CAPTURE_EOF' ... CAPTURE_EOF` block: copy the
whole block, paste into the terminal, Enter. No mode confusion, no syntax errors from parens in the prose.

NO THEO. Owned: scripts/cap.sh, this fragment. No status move; no canonical value changed.

Track: WORKFLOW
