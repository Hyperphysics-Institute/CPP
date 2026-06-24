# Reasoning capture — Patch 2113: overnight extraction audit macro + regression harness (Step 4b)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

Replaced the 2104 skeleton stubs with the real deterministic macro and a regression harness. Tested: 20/20
assertions pass.

Built (`scripts/overnight_extraction_audit.sh`):
- **Phase 1 corpus-integrity (C6):** validates every transcript (filename contract, front matter, not-truncated),
  flags malformed; cross-checks pending-vs-transcript for orphan deltas.
- **Phase 3 founder staging (§4.1):** parses `@@FOUNDER:` markers, classifies via the [REVIEW] policy
  (`classify_founder`: MALFORMED if quote/context missing; DUPLICATE if the quote is already in
  `founders_vision.md`; else AUTO), stages to `Development/staging/<date>/founders/`. Never writes canonical.
- **Phase 4 registry merge (C7):** parses `Registries_pending/*` deltas, schema-validates (registry ∈ known set,
  action non-empty; invalid → `_REVIEW.txt`), stages valid deltas to `staging/<date>/registry/<reg>.delta`, then
  clears the pending file. STAGED for TLA — canonical not written.
- **Phase 5 free-form (pluggable):** flags every transcript to `staging/<date>/freeform_pending/` — the NLP-hard
  prose mining is NOT done deterministically; flagged, never dropped. LLM pass slots in later.
- **Heartbeat (C2):** completeness-aware line (transcripts seen/malformed/orphan, staged/review counts,
  open_review, freeform_pending), date-led per the 2103 pinned format.
- **Partial-night (C7):** `on_exit` trap writes a FAIL heartbeat on error; pending files cleared only after
  processing; staging regenerated per-run (idempotent) so re-run is retry-safe.
- `--dry-run` default (writes nothing), `--apply` stages, `--only`, `--date`.

Also `scripts/test_overnight_audit.sh`: isolated scratch-repo harness exercising AUTO/duplicate/malformed
founders, valid/bad-schema deltas, raw/malformed transcripts; asserts staging outputs + heartbeat. 20/20 pass.

Bug caught + fixed during test: a phase function ending in `[[ $DRY_RUN -eq 0 ]] && act ...` returned 1 in
dry-run, tripping `set -e` on the function call. Fixed by `return 0` on every phase. Also fixed double-staging
risk (clear pending after processing regardless of schema-rejects, which route to _REVIEW) and made per-date
staging idempotent.

v1 boundary (honest): the DETERMINISTIC/structured path (pending deltas, marked founders, integrity, heartbeat)
is complete + tested and is what paper production needs. FREE-FORM prose mining is the one pluggable gap, with a
flag-never-drop default. Registry/founder writes are STAGED for TLA, not auto-canonical.

NO THEO. Owned this patch: `scripts/overnight_extraction_audit.sh` (real impl), `scripts/test_overnight_audit.sh`,
this fragment. No status move; no canonical value changed. Protocol stays canonical/pending-activation.
Next (activation): a capture path emitting the contract (best-effort helper exists; true zero-touch = TLA/Isak)
+ the nightly scheduler. Optional hardening: the LLM free-form pass.

Track: WORKFLOW
