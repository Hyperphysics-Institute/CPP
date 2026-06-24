# Reasoning capture — Patch 2104: overnight extraction audit skeleton (Step 4)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

Step 4: wrote `scripts/overnight_extraction_audit.sh`, the nightly extraction audit, modeled on Isak's
`consolidate_bibliography.sh`. Skeleton scope: the phase structure, the preflight GATE, `--dry-run` (default),
the founder's-voice `[REVIEW]` policy, the heartbeat, and clean-tree-on-every-exit are REAL and tested; the
judgment-heavy extraction (turn-splitting, discipline classification, registry-delta detection) is STUBBED with
explicit output contracts — honest TODOs, not faked intelligence. Tested in-clone: dry-run runs clean and writes
nothing; `--apply` aborts on a dirty tree; `--only` scopes correctly; heartbeat emits in the 2103-pinned format.

## The founder's-voice `[REVIEW]` trigger set (TLA delegated this choice)
TLA: "go ahead and choose the trigger set as you see best for Founders voice." Decision recorded so the panel can
audit the reasoning, not just the list.

**Stance: precision over recall on the AUTO path.** The catastrophic failure mode is fabricating TLA's voice —
putting words in his mouth or misattributing the worker's words as his. So auto-promote ONLY the unambiguous
case and flag everything else. This costs nothing in completeness: the `[REVIEW]` queue is *lossless* — nothing
is discarded, it only waits for TLA's eye. A candidate is AUTO only if it is a single, cleanly-bounded,
unambiguously-attributed, verbatim, novel TLA passage with a clean context anchor and no normalization. Any of
these forces `[REVIEW]`:
1. **BOUNDS** — verbatim start/end can't be cleanly delimited.
2. **ATTRIBUTION** — span not confidently TLA's own words.
3. **MULTIPLICITY** — more than one distinct candidate passage in the fragment.
4. **CROSS-TURN** — passage stitched across more than one turn.
5. **PARAPHRASE** — only a reconstructed/paraphrased version exists (founders_vision is verbatim-only).
6. **DUPLICATE** — substantial overlap with an existing founders_vision entry.
7. **CONTEXT** — no accurate one-line context attachable without inferring intent.
8. **NORMALIZATION** — extraction needed more than trivial-whitespace cleanup ("fixing" his words is the drift).

**Global default (the keystone):** any detector that is uncertain or still stubbed resolves to `[REVIEW]`, never
AUTO. In the skeleton, only the cheap DUPLICATE detector runs (reusing the `sweep_founder_contributions.sh`
promoted-vs-orphan idea); every other path returns `REVIEW:DEFAULT-CONSERVATIVE`. As each detector lands it
flips to a real test, but the default must stay REVIEW. This is what makes "automate it" safe rather than
voice-fabricating.

## v1 stages everything; v2 is the auto target
Per protocol §4 and the repo's "canonical edits deferred to TLA" rule, the v1 audit does NOT write canonical
files. founders_vision promotion and registry merges are produced as a STAGED plan under
`Development/staging/<date>/` for TLA to review and apply. The only direct write is the heartbeat (operational,
not canonical). v2 (direct canonical writes for the AUTO class) is gated on the `[REVIEW]` rail being proven over
time and is explicitly NOT ENABLED in the skeleton. The `AUTO` vs `[REVIEW]` labels in v1 are exactly the
boundary v2 would act on — so the rail gets validated against real runs before it ever writes.

## First-run carry-over is a documented one-shot, not the daily path
The five 2049–2058 contributions (build-plan §D / handover §6) live in `reasoning/`, not in
`Development/transcripts/` (they predate the scaffold). The script marks this as a one-shot sweep reading from
`reasoning/`, NOT merged into the daily transcript path. The older 1–22 June backlog stays with its own window.

NO THEO. Owned this patch: `scripts/overnight_extraction_audit.sh`, this fragment. No status move; no canonical
edit; no founders_vision/registry write. DRAFT campaign — protocol still pending CONV-001 panel.

Next: Step 5 — wire the raw-capture rule + the registry READ protocol into `operating_system.md`/bootup (drafted
by this window, TLA-applied). Then Step 6 — CONV-001 panel review of the protocol before canonical.

Track: WORKFLOW
