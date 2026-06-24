# Reasoning capture — Patch 2108: Capture-and-Audit Protocol revision (v1.0-candidate)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

Revised `templates/capture_and_audit_protocol.md` to the v1.0-candidate, integrating the 4-reviewer change set
(Patch 2106 review) + TLA's in-session design decisions. Full rewrite (preserving the §0–§10 anchors that
2105 cross-references; added §3.1, §4.1–4.3, §6, §7, and renumbered cost/discipline to §11/§12). Also updated
`operating_system.md` §6 registry-read block (2105) to the active read-render. Bundled the reviews-file
integration record (closes the CONV-001 loop).

Integration map: C1→§2 (overclaim softened: "converts irreversible-loss into recoverable-processing," not
"cannot fail") + §3.1 (mechanism requirements: always-on, zero-touch, non-bypassable, fsync-durable — gates the
keystone). C2→§5 (heartbeat completeness-aware). C3→§4.1 **= TLA's middle** (v1 staged default; v2 never
self-graduates, only explicit TLA enable after measurable criteria incl. zero-false-negative adversarial
founder-quote test + rollback; `[REVIEW]` candidates always stage even under v2). C4→§3/§4-step-2
(procedural-turn exclusion removed from daytime, moved to macro). C5→§4.2 ([REVIEW]-queue ownership = blocking
morning/bootup action). C6→§4-step-1 (transcript-integrity/corpus-completeness). C7→§4.3 (schema-validation,
partial-night handling, regression suite — routed to Step-4 build). C8→§0/§4.1/§12 (canonical-write exception
bounds narrow). C9→§7 (scope boundary). C10→§6 (deliberate-vs-incidental delta split + `Registries_pending/`).

Two judgment calls worth recording:
- **§10 frames C10 as a *refinement* of T2, not an overturn.** The panel ratified collapsing the *general*
  daytime registry-write path 4/4; the revival is scoped to *deliberate* paper-production deltas only, per-window
  (never shared), with a read-only render. The general path stays collapsed. Flagged for the panel record so the
  scoped revival is transparent, not a silent reversal of a ratified verdict.
- **Status held at DRAFT (v1.0-candidate).** The panel said RATIFY-WITH-CHANGES and the changes are now in;
  remaining gate is TLA's formal ratification (or a confirmatory panel pass). The worker does not declare
  canonical — that is TLA's status move.

NO THEO. Owned this patch: rewrite of `templates/capture_and_audit_protocol.md`; `operating_system.md` §6 update;
reviews-file integration record; this fragment. No status move; no canonical-registry value changed.
Next: TLA ratifies (or confirmatory pass) → lift DRAFT markers across the protocol, the 2105 OS wiring, and the
2107 paper-production discipline; then the Step-4 macro build (classifier + extractor + C7 hardening).

Track: WORKFLOW
