# Tier-4 reasoning — GR-1 (canonical pointer map)

The verbatim at-patch reasoning fragments are the canonical Tier-4
record for this paper (per the reasoning-capture rider, each committed
in the same `git am` as its work). Single source of truth — read these,
in order:

- `../../reasoning/3228.md` — V0 assembly: the scoping decision
  (series parent, flagship deferred); the solutions-not-equations claim
  discipline and why it was adopted before anyone demanded it; the
  results-only tests table; the 8/8 verify including the two documented
  numerical traps (φ-accumulation drift; crossing-overshoot).
- `../../reasoning/3232.md` — companion re-identification (c05, c07–c13
  → GR-1a–h) and the collisions it dissolved.
- `../../reasoning/3247.md` — the CONV-026 cycle close: the confirmation
  pass, the cross-label recurrence, and the sequencing near-miss owned
  (origin-lag divergence caught by a registry guard assertion).
- `../../reasoning/3270.md` — V1.0 ship: what was updated to the closed
  state and what was deliberately left alone. Read this one beside
  `3276.md`, which records what that judgment missed.
- `../../reasoning/3271.md` — the founder's PPP audit answered honestly
  (V1.0 shipped without Keywords/PLS/Signature); the tool-chain incident
  owned (hard-sync discarded a local commit; reflog recovery).
- `../../reasoning/3276.md` — V1.0.2: the epistemic ledger found
  contradicting the paper's own abstract; why it was corrected under
  PD-006 rather than escalated; the anti-erasure form; the title-version
  defect class flagged corpus-wide.

For the equation layer this paper registered and later closed, the FE-1
arc fragments `../../reasoning/3254.md` through `../../reasoning/3267.md`
are the derivation record; `GR-1j`'s own suite is their pointer map.

**Session-close narrative.** GR-1 was assembled in Session 149 as the
parent the eight-companion arc had never had, restated once under panel
pressure in Session 150, shipped V1.0 the same session once both of its
registered open problems were discharged by dedicated companions, and
corrected twice post-ship — first for missing PD-001 formatting (founder
audit), then for a stale ledger (in-house, during this suite pass).
Both corrections are recorded rather than folded silently into a version
bump; the changelog carries them at the same weight as the ship.
