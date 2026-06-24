# `Development/` — raw capture + audit infrastructure

This tree is the operational ground for the **Capture-and-Audit Protocol**
(`templates/capture_and_audit_protocol.md`). It holds the things produced and
consumed by the daytime-capture / nightly-audit cycle — **not** physics or
registries (those live in their canonical homes).

| Path | What it is | Written by | Read by |
|------|-----------|-----------|---------|
| `transcripts/` | Flat, verbatim, by-window raw capture — GROUND TRUTH | automatic daytime capture | the nightly audit |
| `audit_log.md` | The heartbeat log — one dated line per nightly run | the nightly audit | the next bootup (missing line = LOUD flag) |

**The one rule that makes this work:** nothing here is judged or filed during the
day. Capture is mechanical; all splitting, attribution, discipline-filing, and
registry-merge happen overnight in `scripts/overnight_extraction_audit.sh`. See
the protocol doc for the full diagnosis and design.

> Status: scaffolded at Patch 2103 (Step 3 of the 2100-band campaign). The
> nightly audit script (Step 4) does not exist yet, so no audit has run — see
> `audit_log.md`.
