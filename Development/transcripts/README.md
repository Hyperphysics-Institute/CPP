# `Development/transcripts/` — flat, verbatim, by-window raw capture

This is **ground truth**. Every other capture artifact (reasoning fragments,
`verify/` scripts, `founders_vision.md` entries, registry deltas) is *derived*
from these files by the nightly audit, and is re-derivable from them if a
downstream step ever drops something. A verbatim raw transcript is
reconstruction-proof: the original is never destroyed.

## Filename contract (the filename carries everything)

```
YYYY-MM-DD_HHMM_p<patch>_<window-slug>.md
```

- `YYYY-MM-DD_HHMM` — when the window opened (local time).
- `p<patch>` — the patch number the window is working in (e.g. `p2103`). If a
  window spans several patches, use the one it opened on; the audit reads the
  body, not just the name.
- `<window-slug>` — a short identifier for THIS window (e.g. `capture-audit`,
  `lorentz-root`, `sf7-unification`).

**The window-slug — never the discipline — is the collision key.** N windows on
N phenomena each write their own slug and never collide, and no one has to decide
"which discipline folder this belongs in." That discipline decision is exactly
the hot-path judgment that broke every prior system; here it is the *audit's*
job, done overnight (`templates/capture_and_audit_protocol.md` §1–§4).

## What goes in a transcript file

- The **full verbatim turn** — TLA's words *and* the worker's words — every
  round, in order.
- Exclude only obviously procedural turns (pure "apply this" / "proceed").
- **Do not file by discipline. Do not pre-sort, summarize, or paraphrase.** Raw
  and complete is the whole point; the audit does the rest.

## How files get here (capture must be mechanical)

Per protocol §3, capture must **not** depend on a worker remembering to write
each turn — that would reintroduce the root-cause judgment one level down. The
intended mechanism is an automatic dump/export of the verbatim turns into this
tree (export tooling / mechanism TBD with TLA + Isak). Until that is wired, a
window may append here as a best-effort backstop, but the design target is
automatic capture.

## What reads this

`scripts/overnight_extraction_audit.sh` (Step 4) each night reads the day's
files here, splits every turn into fragments, files each to its proper home, and
writes a heartbeat to `../audit_log.md`.
