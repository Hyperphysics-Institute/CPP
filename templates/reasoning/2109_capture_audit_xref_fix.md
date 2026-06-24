# Reasoning capture — Patch 2109: fix internal cross-references in the protocol v1.0-candidate

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

Pre-dispatch cleanup before the confirmatory CONV-001 pass. The 2108 full rewrite renumbered sections, leaving
four stale cross-references (forward-additive error ownership per protocol §12 — caught on read-through, fixed
before the panel sees it): header "mechanism (§11)" → §6; §4-step-3 "delta classes in §11" → §6; §6
"(see §8)" → §10; §10 "§8's anticipated read-render" reworded to a self-referential phrase. No content change —
only reference targets corrected so the doc going to review has clean internal navigation.

NO THEO. Owned this patch: `templates/capture_and_audit_protocol.md` (xrefs only); this fragment. No status move.
Track: WORKFLOW
