# Reasoning capture — Patch 2114: activation runbook + nightly wrapper (Step 4c)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

Wrote the activation runbook and the Task Scheduler entry point — the last build artifact before the protocol
goes operational. After this, what remains is environment (a capture path + scheduling) + a TLA status move (flip
the activation markers), not code.

Built:
- `scripts/run_nightly_audit.sh` — Task Scheduler/cron entry point. Pulls, runs the audit `--apply`, logs OUTSIDE
  the repo (`~/cpp_audit_runs/<date>.log`) so run logs never dirty the tree. **Stage-only:** stages + clears
  pending, does NOT commit or push (TLA does, in the morning).
- `Development/ACTIVATION.md` — runbook: (0) capture-path prerequisite, (1) exact `schtasks` entry + wake/logon
  settings + test command, (2) morning review (heartbeat check → review staging → clear [REVIEW] → single
  commit+push), (3) go-live checklist incl. the activation-marker flip.
- Pointer added in protocol §9.

Design decisions (flagged):
- **Stage-only nightly, TLA pushes in the morning** — honors TLA's "I do the commit and push." Consequence: a
  skipped morning review leaves an uncommitted staging tree, so the next night's `pull --rebase` fails and the
  audit is skipped → missing heartbeat → loud flag. Documented as the intended §4.2 blocking discipline, with a
  Mode-B alternative (commit-not-push the operational output) for those who want the audit to keep running.
- **Logs outside the repo** (`~/cpp_audit_runs/`) so run logs never dirty the working tree or need gitignoring.
- The **activation-marker flip is a separate TLA status move**, listed as the last checklist item — the worker
  writes that patch only when TLA confirms go-live. Not done here (not yet activated).

NO THEO. Owned this patch: `scripts/run_nightly_audit.sh`, `Development/ACTIVATION.md`, protocol §9 pointer, this
fragment. No status move; no canonical value changed. Protocol stays canonical/pending-activation.
The code build is COMPLETE (2112 contracts/helper, 2113 macro/tests, 2114 runbook/scheduler). Remaining to go
live: capture path + scheduled task + the marker flip.

Track: WORKFLOW
