# Reasoning capture — Patch 2102: the Capture-and-Audit Protocol doc (Step 2), simplified by TLA's reframe

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

Step 2 of the campaign: wrote `templates/capture_and_audit_protocol.md`. The doc is materially simpler than the
seed handover because TLA reframed the design and the reframe collapsed the open questions (Q1–Q3 from the
2101 build plan) rather than answering them piecemeal.

The reframe moves ALL judgment out of the daytime path into the nightly macro. Consequences I took:
- Architecture reduces from "three pieces + heartbeat" to **two pieces + heartbeat**: (1) automatic raw capture
  (daytime: record everything, do nothing else); (2) the nightly extraction macro (all splitting/filing/
  promotion/merge). Heartbeat unchanged.
- **2B (write-partitioned registry-temp) collapses.** Its only reason to exist was a collision-free daytime
  write target for registry intentions; with universal raw capture + a macro that extracts registry deltas from
  the transcript, that path is redundant. Its one unique benefit (same-day cross-window read visibility) is
  waived by "don't worry about registries during the day." Recorded in §8, flagged for TLA ratification — I did
  not silently delete the handover's piece; I documented why it folds and how it would return (read-only render)
  if same-day visibility is later wanted.
- **Q1 (is capture mechanical?) resolved toward automatic dump/export**, not per-turn worker action — TLA's
  "record everything automatically if that is possible." I wrote §3 to forbid capture that depends on a worker
  choosing to write each turn, because that is the root cause one level down.
- **Q3 (auto-write-to-canonical risk) resolved as staged-first-then-auto** — TLA confirmed the reviewed-first,
  promote-to-auto-after-it-proves-itself path. Written into §4 as v1 (staged diff for TLA) → v2 (auto once the
  `[REVIEW]` rail is proven).

The doc carries DRAFT status; it is not canonical until the CONV-001 panel reviews it and TLA ratifies (it
changes how every window works). It does not delete `reasoning_capture_protocol.md` — §6 records that what
changes is the owner/timing of judgment (macro/overnight, not worker/in-the-moment), and that protocol's schema
(§0/§4/§10) is what the macro files into.

## FOUNDER CONTRIBUTION (verbatim — TLA, 2026-06-24)
> "I think all of these collapse when we reframe what we are trying to do.
> * Record everything automatically if that is possible.
> * Don't worry about registries, founder's voice, etc., during the day. All of these things are handled as part of the audit and then exported overnight.
> * The decision about where fragments of the verbatim transcript go is delegated to a macro that runs nightly, analyzes all verbatim turns, and separates them into fragments, which are then filed in the appropriate registries or in various files."
*Context:* the design reframe that simplified the protocol from three pieces to two — moving ALL judgment out
of the daytime path into the nightly macro, collapsing the registry-temp write path (§2B → §8) and the
worker-captures-by-day obligation. Shaped the entire structure of `capture_and_audit_protocol.md`. (Promotion
to `founders_vision.md` pending — the sweep / first audit run will catch it.)

NO THEO. Owned this patch: `templates/capture_and_audit_protocol.md`, this fragment. No canonical-registry edit;
no status move. DRAFT pending panel.

Track: WORKFLOW
