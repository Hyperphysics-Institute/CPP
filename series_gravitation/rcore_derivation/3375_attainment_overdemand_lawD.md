# OPEN-GR-FLOOR-1(a) — Attainment is a theorem for the INTERIOR; and OPEN-GR-ROT-1 rung 2 — the over-demanded core (law D), whose linear limit is the 3297 mirror

**Patch 3375, Session 161, 2 Sep 2026.** Verify `code/3375_attainment_overdemand_lawD_verify.py` (22/22). Reasoning `reasoning/3375.md`. Inputs: R-FLOOR-REGISTER (the register records `min(demand, cap)`), R-FLOOR-FINITE, R-COOCCUPATION-FORCED, GR-1a shell broadcast (1/r kernel, relay-carried without truncation — 3367 Check 7).

**Standing:** the interior-attainment theorem is DERIVED (elementary; two premises). Law (D) is DERIVED in its two limits and BRACKETED between them; the peeling dynamics is rung 3. The *value* `u_max` is unchanged: OPEN (FLOOR-1(c)), window 0.536 < u_max ≤ 1.

## §1 The panel's "attainment" was two questions, and one of them closes

CONV-038 stripped "attainment" from 3367 as an asserted extremality step. Patch 3374 then showed attainment chooses the echo morphology. Separating the two meanings:

- **Attainment of the value** — is `u_max = 1` exactly (the Buchdahl-extremal value)? **Still open.** This is FLOOR-1(c), the cap's magnitude, on which the founder has no picture.
- **Attainment inside the body** — does the interior register sit *at* the cap, or below it with headroom? **Closed, as a theorem:**

> **Theorem (interior over-demand).** Let the register record `R = min(DEMAND, cap)`, where DEMAND is the 1/r-kernel census of all sources (non-negative, spherically symmetric, relay-carried). Then `d|DEMAND|/dr = −M(r)/r² ≤ 0`: demand is non-decreasing inward for *any* non-negative source. The surface of a saturated body is where `DEMAND = cap`. Hence `DEMAND > cap` at every interior point: the interior register is at the cap everywhere, with a strictly positive **excess** `e(r) = DEMAND(r) − cap` that grows inward (uniform core: `e = (u_max/2)(1 − r²/R²)`, `e(0) = u_max/2`, `e′(R) = −u_max/R`).

So law (A) of 3374 (headroom inside) requires an *unsaturated* body — a star, not an R-core — and law (B) (at cap with *zero* excess) requires the interior source to vanish. For the R-core the interior is at cap and over-demanded. Neither (A) nor (B); a fourth law.

## §2 Law (D): the over-demanded core

A perturbation `δ` of the demand changes the register only where `|δ|` exceeds the local excess:

- **Compression (`δ > 0`):** refused everywhere — no headroom above the cap. **Exact Dirichlet at the surface, phase π.** (Obstacle argument: with `R ≤ cap` on the half-space, an incident push meets `R = cap` at the surface and nothing enters; verify Check 4.)
- **Rarefaction (`δ < 0`):** the register unpins only where `e(r) < |δ|` — a **skin** of depth `d(δ)` with `e(d) = |δ|`, i.e. `d = R·(δ/u_max)` to first order (exact 0.1056 R at δ = 0.1 u_max). Beyond the skin the register stays pinned. The skin is a register **peeled off a ceiling** it is pressed against by `e(r)`; its reflection is that of a moving contact line — **rung 3** — and lies between two computed brackets: Dirichlet at the surface (delay 0) and Dirichlet at the skin floor (delay `2d/c_*`), both at phase π (Checks 3–4).

**The linear limit.** As `δ → 0`, `d → 0`: both signs reflect promptly at phase π. **`X = 0`, `|R| = 1`, phase π — the 3297 mirror — is recovered as the small-amplitude limit of law (D).** What 3297 got wrong was the *reason* (a two-sided clamp from the retired postulate); what it got right was the *limit*. GR-2's flagship line, computed with `X = 0`, is the linear-response prediction, and it now has a derivation.

## §3 The size of the nonlinear correction

The correction is one-sided (rarefaction half-cycles only), amplitude-dependent, and shrinks with the ringdown:

| δ/u_max | skin d/R | rarefaction delay upper bound (62 M_⊙; three c_*-clock maps) |
|---|---|---|
| 10⁻³ | 0.0010 | 1–4 μs — the mirror |
| 10⁻² | 0.0101 | 12–41 μs |
| 10⁻¹ | 0.1056 | **0.13–0.43 ms** — 6–20% of the 2.15 ms cavity |

At ringdown-onset strain near the remnant (`δ/u ~ 0.1`), the rarefaction half-cycles of the *first* echo lag by up to ~0.1–0.4 ms and carry harmonics; by the third or fourth echo the amplitude has fallen enough that the mirror is exact to the instrument. **The 3374 two-timescale train is not the generic prediction:** the full core round trip belongs to laws (A)/(B), which the R-core does not obey. The generic prediction is the mirror plus an early-echo, one-sided distortion.

## §4 What this changes in the record

- **GR-2 caveat (a)** ("boundary-phase shift uncomputed"): now *bounded* — phase π + O(kd), delay ≤ 2d/c_*, rarefaction-only, amplitude-dependent; to be written into V1.8/V2.0 once rung 3 pins the peel reflection.
- **3374 §4** (two echo timescales): downgraded to the (A)/(B) cases — non-generic for the R-core.
- **Q4(i) caveats** (mode conversion, intra-Moment absorption): untouched by this rung.
- **OPEN-GR-FLOOR-1:** (a) interior attainment CLOSED (theorem); (a′) value attainment — merged into (c), OPEN; (b) the interior bridge — the over-demand theorem *is* the bridge: `u` inside is the register at cap (flat), while the demand is the metric-side potential (rising); GPT's equivocation resolves as "two quantities, not two meanings of one symbol" — record and leave to the panel.

## §5 Rung 3 (owed)

The peeling-contact reflection: 1D string pressed to a ceiling by `e(x) = e′x`, pulled by a rarefaction wavelet; free boundary at the contact line; compute `R(ω, δ)` between the brackets. Then the spherical ℓ = 2 version with the RW potential and lapse. Then rotation.
