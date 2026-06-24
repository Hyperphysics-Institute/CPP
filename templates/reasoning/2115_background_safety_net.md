# Reasoning capture — Patch 2115: solo background safety-net mode (Step 4d)

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

## FOUNDER CONTRIBUTION (verbatim — TLA, 2026-06-24)
> "I'm not working with Isak right now; I just want to get the system up and running in the background so I don't
> have to do anything but develop the papers that I am working on. Please do what you need to do to make that
> happen."

TLA wants hands-off background operation, solo. Configured for exactly that, with three honest constraints stated
to TLA rather than papered over:
1. I cannot create the Windows scheduled task on his machine — that is the one irreducible TLA action (one
   command, once). I cannot reach his machine.
2. Zero-touch verbatim RAW-transcript capture is not self-provisionable here (/mnt/transcripts empty in-container;
   the conversation lives platform-side). It needs a platform export or an Isak integration. Best-effort helper
   remains the bridge. BUT his essentials — reasoning + founder's voice — are ALREADY captured verbatim per-patch
   every session (reasoning fragments + FOUNDER CONTRIBUTION blocks), zero setup. So his core fear is already
   addressed independent of this system.
3. Flipping the FULL protocol to ACTIVE would ADD daily friction (pending-delta writes + mandatory morning
   review) — the opposite of "do nothing but develop papers." That discipline is for parallel-window collision
   safety; TLA is solo. So I did NOT flip full activation. Background safety-net instead.

Built:
- `scripts/run_nightly_audit.sh` -> background self-sustain: after `--apply`, commit the OPERATIONAL output
  LOCALLY (transcripts/staging/heartbeat/cleared-pending), NOT canonical, NOT pushed. Keeps the tree clean so the
  audit never stalls on un-reviewed staging — runs every night with zero attention. TLA reviews staging + pushes
  on his own cadence (or never; raw is preserved).
- `Development/ACTIVATION.md` -> new top "SOLO BACKGROUND MODE" section: the single one-time `schtasks` command
  front-and-center, wake setting, test command, the honest capture limit, and the explicit "do NOT flip full
  activation when solo" steer. Full multi-window runbook retained below for the Isak scenario.

Decisions (flagged): local auto-commit by TLA's own scheduled job is sanctioned by "do what you need to do" and is
necessary for unattended self-sustaining operation; it stays LOCAL (no auto-push) so pushes remain TLA's. Canonical
(founders_vision, registries) still STAGED for review, never auto-written — the ratified safety model is intact.
Protocol stays canonical/pending-activation (background mode does not require the ACTIVE flip; paper development
continues as current practice, friction-free).

NO THEO. Owned this patch: `scripts/run_nightly_audit.sh`, `Development/ACTIVATION.md`, this fragment. No status
move; no canonical value changed.
TLA's one action: run the schtasks command once. Then it is background. DM-1 proceeds under current practice in
parallel; not blocked by any of this.

Track: WORKFLOW
