# ACTIVATION runbook — Capture-and-Audit Protocol

The protocol is **canonical** but **not yet operational**. This runbook flips it live. Three things: a capture
path, the nightly scheduler, and your morning review. Full design: `templates/capture_and_audit_protocol.md`.

---

## 0. Prerequisite — a capture path that emits the contract
Something must drop each session's verbatim transcript into `Development/transcripts/` in the format contract
(`Development/transcripts/README.md`). Two options:
- **Best-effort (works today):** at session close, run `scripts/capture_session.sh --slug <slug> --patch <n>`
  with the transcript on stdin or `--file`. This is the §3.1 *backstop*, not the zero-touch mechanism.
- **True zero-touch (the §3.1 target, TLA/Isak):** an always-on, non-bypassable export that writes the same
  contract with no manual step. Until this exists, capture is best-effort and the keystone guarantee is partial
  (the doc says so honestly).

Either way the macro is indifferent — it parses the contract, not the producer.

---

## 1. The nightly scheduler (Windows Task Scheduler)
The entry point is `scripts/run_nightly_audit.sh` (pulls → runs the audit `--apply` → logs to
`~/cpp_audit_runs/<date>.log`). It is **stage-only**: it stages under `Development/staging/` and clears
`Registries_pending/`, but never commits or pushes — you do that in the morning.

**Exact task (run in an elevated `cmd` / PowerShell; confirm your bash path first with `where bash`):**
```
schtasks /Create /TN "CPP Nightly Audit" ^
  /TR "\"C:\Program Files\Git\bin\bash.exe\" -lc \"~/Documents/GitHub/CPP/scripts/run_nightly_audit.sh\"" ^
  /SC DAILY /ST 03:00 /F
```
Then, in Task Scheduler (GUI) on that task → Properties:
- **Conditions → Wake the computer to run this task** ✓ (so a sleeping machine still runs it).
- **General → Run only when user is logged on** (simplest on a personal machine; the alternative needs stored
  credentials). The machine must be on/awake at 03:00.

**Test it now:** `schtasks /Run /TN "CPP Nightly Audit"`, then check `~/cpp_audit_runs/<today>.log` and confirm a
new line landed in `Development/audit_log.md`.

> If the machine that hosts Isak's content-audits is the intended host, confirm it has the repo at
> `~/Documents/GitHub/CPP` and can pull/push — same environment need (real tools, not the container).

---

## 2. Your morning review (the blocking step, §4.2)
Do this before opening any work window:
1. `cd ~/Documents/GitHub/CPP`
2. **Heartbeat check:** `tail -3 Development/audit_log.md` — confirm a line for **last night's date** exists. A
   **missing** line is a LOUD flag: the audit didn't run — check `~/cpp_audit_runs/<date>.log`.
3. **Review `Development/staging/<date>/`:**
   - `founders/<date>_founders.md` — each candidate is `[AUTO]` or `[REVIEW:<trigger>]`. Approve/edit, then
     paste approved entries (verbatim) into `founders_vision.md`.
   - `registry/*.delta` — one file per registry; apply each staged action to its canonical registry.
   - `registry/_REVIEW.txt` — schema-rejected deltas; resolve by hand.
   - `freeform_pending/<date>_pending.txt` — transcripts awaiting the (optional) free-form mining pass.
4. **Clear the `[REVIEW]` queue** — resolve every flagged item before new work (this *is* the §4.2 owner step).
5. **Commit + push once** — the audit's staging/cleared-pending **plus** your canonical applications, in a single
   commit. This is the only push; it also publishes the cleared `Registries_pending/` so other windows see fresh
   state.

> **If you skip a morning:** the next night's `git pull --rebase` fails on the un-committed staging, so the audit
> is skipped and its heartbeat goes missing — a loud flag to catch up. That is the intended blocking discipline.
> If you'd rather the audit keep running regardless, switch `run_nightly_audit.sh` to commit (not push) its
> operational output before exiting (Mode B); you still push in the morning.

---

## 3. Go-live checklist
- [ ] A capture path emits the contract into `Development/transcripts/` (best-effort helper wired, or zero-touch).
- [ ] `bash scripts/test_overnight_audit.sh` → `PASS=20 FAIL=0`.
- [ ] `bash scripts/overnight_extraction_audit.sh` (dry-run) runs clean from the repo root.
- [ ] Local machine has the repo at `~/Documents/GitHub/CPP` and can pull/push.
- [ ] Task created; `schtasks /Run` test produced a log + a heartbeat line.
- [ ] Decide the free-form pass: leave pluggable (flag-only) or wire an LLM mining step.
- [ ] **Flip the activation markers** (a TLA status move): change "pending activation" → "ACTIVE" across
      `capture_and_audit_protocol.md` (STATUS), `operating_system.md` (§4, §6), `bootup.md`,
      `paper_completion_checklist.md`. Ask the worker window for this patch once the boxes above are checked.

Once the markers are flipped, every window — DM-1 included — runs under the protocol: capture by day, this audit
by night, your review each morning.
