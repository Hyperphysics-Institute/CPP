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

---

## Transcript file format (contract — the macro parses this)

A transcript is a single Markdown file with a small front-matter block followed by
verbatim turns. **Any capture mechanism — best-effort helper (`scripts/capture_session.sh`)
or a future zero-touch integration — MUST emit exactly this shape**, so the overnight
audit can parse it deterministically.

```
---
window-slug: <slug>            # matches the slug in the filename; the collision key
patch: <n>                     # patch the window opened on
opened: <YYYY-MM-DD HH:MM TZ>  # local time
---

### [1] TLA
<full verbatim turn — TLA's words, unedited>

### [2] WORKER
<full verbatim turn — worker's words, unedited>

### [3] TLA
...
```

Rules the parser relies on:
- Front matter is the first block, fenced by `---` lines, `key: value` pairs.
- Each turn starts with a header line `### [<n>] <ROLE>` where `<ROLE>` ∈ `{TLA, WORKER}`
  and `<n>` is a monotonic turn index. Everything until the next `###` header (or EOF)
  is that turn's verbatim body.
- **No editing, no paraphrase, no procedural-turn exclusion** — capture everything; the
  macro filters (protocol §3/§4). Pure-procedural turns may be included; the macro drops them.

### Optional inline markers (let the deterministic path handle a turn precisely)
A turn body MAY carry inline markers that the macro files deterministically instead of
leaving to the (pluggable) free-form pass:
- `@@FOUNDER: "<verbatim TLA quote>" | context: <one line>` — a founder-voice candidate,
  staged via the protocol §4.1 `[REVIEW]` path. Bounded quote + attribution = clean AUTO
  candidate; anything ambiguous → `[REVIEW]`.
- Deliberate registry deltas do NOT go inline — they go in `Registries_pending/<slug>.md`
  (see that README). Markers are optional; un-marked content falls to the free-form pass.
