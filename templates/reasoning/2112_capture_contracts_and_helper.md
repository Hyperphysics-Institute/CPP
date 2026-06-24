# Reasoning capture — Patch 2112: capture contracts + best-effort capture helper (build, Step 4a)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

First build patch toward activating the (now-canonical) Capture-and-Audit Protocol. Defines the two format
contracts the macro parses, and a reference best-effort capture path — decoupling the macro build from the
environment-specific capture mechanism (the macro is indifferent to which producer emits a contract-conformant
file).

Built:
- `Development/transcripts/README.md` — appended the **transcript format contract**: front-matter block +
  `### [<n>] <ROLE>` verbatim turns; optional inline `@@FOUNDER:` marker for the deterministic founder path;
  deliberate registry deltas go to Registries_pending, not inline.
- `Registries_pending/README.md` — new write-partitioned channel + the **pending-delta contract**
  (`- registry=... | action="..." | paper=... | patch=...`, one delta per line, append-only to own file).
  Marked "pending activation" (no merge exists yet).
- `scripts/capture_session.sh` — best-effort capture helper that emits the transcript contract (front matter,
  structured-vs-raw auto-detection, slug/patch validation, refuse-overwrite, sync). Tested: structured + raw
  inputs, bad-slug rejection.

Decisions (flagged for TLA):
- **Contracts decouple capture from the macro.** Whatever produces a transcript — this helper, or a future
  zero-touch integration (TLA/Isak environment) — emits the same format, so 2113's macro parses uniformly. This
  removes the §3.1-mechanism dependency from the macro build rather than blocking on it.
- **capture_session.sh is explicitly the §3.1 BACKSTOP, not the mechanism.** It is manually run, so it does NOT
  satisfy §3.1 always-on/zero-touch; it preserves ground truth until a real zero-touch path exists. Stated in
  the script header and the README.
- **raw (unstructured) transcripts are flagged `format: raw`, never dropped** — the macro routes them to the
  (pluggable) free-form pass. Honest handling of the NLP-hard case.
- **Registry-merge will STAGE for TLA** (2113), not auto-write canonical — consistent with the repo's
  canonical-edits-deferred-to-TLA rule and the founder staged-first pattern. Reversible; flagged.

NO THEO. Owned this patch: transcripts README format section, `Registries_pending/README.md`,
`scripts/capture_session.sh`, this fragment. No status move; no canonical-registry value changed. Protocol stays
canonical/pending-activation.
Next: 2113 — the macro implementation (replace stubs: Registries_pending merge -> staged diff; corpus-integrity;
completeness heartbeat; founder staging from `@@FOUNDER:` markers with the [REVIEW] policy; partial-night
handling; schema validation) + a regression test harness. Free-form prose mining = documented pluggable step.

Track: WORKFLOW
