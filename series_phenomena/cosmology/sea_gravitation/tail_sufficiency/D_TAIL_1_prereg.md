# PREREGISTRATION — **D-TAIL-1: IS VARIANCE A SUFFICIENT DESCRIPTION OF THE DRIVE?** The assumption every instrument in this corpus makes, never once tested — matched variance, different tail structure, and ask whether the Sea's equilibrium can tell the difference

**Patch 3192, 22 August 2026. Container. Frozen before any
computation.** Power gate first, per the 3182 discipline.

## §1 — The unexamined assumption

Every drive in this programme is specified by ONE number: σ_n. The
calibration, the response campaigns, the β-ladder's forcing, the
Phase B installation — all describe the shaking of the Sea by its
variance alone. **If the Sea's equilibrium depends on the drive's TAIL
STRUCTURE as well as its variance, then a single number is an
incomplete specification, and two instruments agreeing on σ_n may be
driving the Sea differently.** That would be a corpus-wide fact about
every instrument, not a fact about one campaign.

Three findings this week make the question live rather than
academic:
- The Sea's ambient field is **self-generated** (σ_amb = 0.271 at
  ZERO drive; 3181 §2).
- The engine's own force series is **intermittent**, at 20–110× the
  Gaussian rate of extreme Moments (3183 §2).
- The Gaussian surrogate **suppresses** that intermittency
  monotonically (3184 §1) — so our instruments have been driving with
  the one tail structure the Sea does not natively have.
- And the founder's DM diagnosis (3177 §2.3) rests on exactly this:
  *"intermittent and smooth driving give materially different
  response statistics even at matched variance."* **Never tested.**

## §2 — Design

At the calibrated cell (d_s = 4.636, n = 5), seeds {5, 11, 17, 23},
four drives **matched in per-axis variance** and differing only in
tail structure:
- **G** — Gaussian, σ = 0.30 (the operating drive).
- **S2** — saltatory, 2% of Moments bursting, amplitude set so total
  variance = 0.30² exactly.
- **S05** — saltatory, 0.5% bursting, same total variance (rarer,
  larger).
- **U** — uniform (SHORT tails, the opposite direction from
  saltatory), same variance. **Included so the test can detect
  difference in EITHER direction and is not a one-sided search for
  the founder's picture.**
Variance matching is verified numerically per drive and printed.

## §3 — POWER GATE (blocking, per 3182)

Before any equilibrium reading: the same statistics are applied to a
deliberate **positive control** — drive G at σ = 0.30 vs σ = 0.45 (a
50% variance change, which the Sea's known insensitivity says should
still be detectable in SOME observable). **If no statistic separates
the control pair at ≥ 3 SE, every statistic is BLIND and D-TAIL-1 is
VOID** — the instrument cannot detect drive changes at all and the
tail question is unanswerable here.

## §4 — Statistics and frozen readings

Primary: **f_b** (first-moment, seed agreement ~0.001 — the most
precise observable in the corpus). Secondary, all reported:
ρ_swap, f_dwell, σ_amb.
- **TAIL-SENSITIVE** iff any matched-variance pair differs in f_b by
  ≥ 3 SE (seeds pooled) **and** the control pair was detectable.
- **VARIANCE-SUFFICIENT** iff all matched-variance pairs agree within
  3 SE while the control pair separates. This is the **negative**
  result and it is the one that simplifies the corpus: variance would
  then be a complete drive specification.
- **UNRESOLVED** otherwise.

## §5 — Hazard direction (declared)

**TAIL-SENSITIVE supports the founder's DM diagnosis and complicates
every instrument** (each would need its drive's tail structure
specified, not just σ). **VARIANCE-SUFFICIENT undercuts the mechanism
the founder's DM diagnosis rests on** — the under-response account
would lose its proposed cause — **while simplifying the corpus.**
Both outcomes are substantive; neither is a null.

**Worker's pre-declared expectation: VARIANCE-SUFFICIENT.** Reason
recorded before the run: 3131 §4 measured d_s^emp insensitive to σ_n
across a 9× range, and 3181 §2 found σ_amb flat from zero to 4×
arrival amplitude — a Sea that ignores the drive's SIZE that
thoroughly is unlikely to notice its SHAPE. **This expectation runs
AGAINST the founder's picture, and against the worker's own recent
enthusiasm for intermittency.** The worker's last four
pre-declarations scored WRONG, NOT-CONFIRMED, UNSCORED, and
NOT-CONFIRMED.

## §6 — Fence

No Phase C content; nothing touches Λ, d_s^emp, or the four rates.
No DM claim — this measures the INSTRUMENT's sensitivity, and any DM
implication requires its own freeze. Engine dynamics untouched; the
drive channel is the switchable one installed at 3179 with
bit-identity verified.
