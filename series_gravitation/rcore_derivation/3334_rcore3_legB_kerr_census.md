# OPEN-GR-RCORE-3 — Leg B: The Kerr Cavity Census — the Comb Is Not Restored

**Patch 3334, 21 Aug 2026 — Session 156.** Verify:
`code/3334_rcore3_legB_kerr_wkb_verify.py`, **7/7 PASS** (all checks
FAST — no time-domain evolution in this instrument). Charter: the
Leg-B question minted at Patch 3333 — does the longer Kerr retrograde
cavity restore a multi-resonance echo comb? It decides PRED-O-39's
refined search target.

---

## §1 THE LEG-B ANSWER: no. The comb is not restored at any astrophysical spin — the signature is a multi-LINE set of top-of-barrier resonances plus early transients

Instrument (§3): geodesic-eikonal radial WKB. For each mode (ℓ,m)
the Carter constant is fixed (Q = (ℓ+½)² − m²), the radial
wavevector is k = √R/Δ from the Kerr Hamilton–Jacobi radial function
R(r;ω), and the Bohr–Sommerfeld phase Φ(ω) = ∫ k dr between the
Dirichlet wall and the turning point counts trapped resonances:
N = #{n : Φ(ωₙ) = (n+¾)π}. The comb question becomes a computed
integer.

**Census at χ = 0.68, equatorial wall r = 2.2668 M:**

| Mode | ω_top [1/GM] | f_top @ 62 M_⊙ | +17% Leg-A calib. | Φ_max/π | N_trapped |
|---|---|---|---|---|---|
| (2,−2) | 0.4055 | 211 Hz | ~247 Hz | 0.245 | **0** |
| (2,−1) | 0.4477 | 233 Hz | ~273 Hz | 0.138 | 0 |
| (2, 0) | 0.4996 | 260 Hz | ~305 Hz | 0.056 | 0 |
| (2,+1) | 0.5643 | 294 Hz | ~344 Hz | 0.007 | 0 |
| (3,−3) | 0.5601 | 292 Hz | ~342 Hz | 0.366 | 0 |

Every exposed mode's Φ_max sits far below the ¾π threshold for even
one trapped resonance. The spin scan (check 6) closes the question
across the astrophysical range: for the retrograde-keyed (2,−2),
max Φ_max/π = 0.247 (at χ = 0.52) over χ ∈ [0.30, 0.98] — **N ≥ 1
nowhere**. The intuition from Patch 3333 was correct and is now
computed: the Kerr retrograde cavity is longer, but its barrier is
correspondingly lower (ω_top falls monotonically with spin, check
7: 0.4425 → 0.3846 across χ = 0.30 → 0.95), and the phase volume
never accumulates a trapped mode.

**The refined search target at this grade (χ ≈ 0.68, M ≈ 62 M_⊙):**
not a 381 Hz comb, but (a) **a small set of damped resonance lines**,
one per exposed (ℓ,m) mode, at ~211/233/260/294 Hz eikonal-top
(~247–344 Hz with the +17% Leg-A position calibration), with
Leg-A-calibrated quality factors Q ~ 5; the retrograde-keyed (2,−2)
line is the lowest and strongest-coupled to the ringdown; plus
(b) **the early broadband transient pair(s)** at the retrograde
eikonal delay 2.624 ms (GR-2's Δt survives exactly there). Retrograde
keying survives as the ordering of the line set — the (ℓ,ℓ)
corotating branch is absent (buried), so the lowest line sits at the
*retrograde* top, not the prograde one: the discriminator persists
in line-set form.

## §2 The wave-side confirmation of burial

For (2,+2) at χ = 0.68 the forbidden region R < 0 begins **at the
wall itself** for every ω < 0.642 (e.g. R(wall) = −5.4 at ω = 0.05),
and above 0.642 no barrier exists anywhere: the wall sits inside the
mode's forbidden zone at all frequencies that have one. That is the
wave-instrument restatement of the Patch-3333 geodesic burial
verdict — no propagating cavity exists for the corotating dominant
mode at any frequency, so nothing can key a prograde comb or line.

## §3 Instrument validation

Check 1 is the designed-to-fail anchor: at a → 0 the instrument must
reproduce Leg A, and does — ω_top = 0.4811 matches the closed form
(ℓ+½)/√27 to <1%, and Φ_max/π = 0.178 < ¾ gives N = 0, exactly
consistent with the Leg-A FD finding that the lone χ = 0 resonance
sits ABOVE the barrier top. Wall-position sensitivity (check 5):
moving the wall to the smallest surface radius the (2,−2) orbit's
latitude band sees (2.1897 M — the longest-cavity bound) raises
Φ_max/π only to 0.304; N unchanged. Grade statement: eikonal-WKB
throughout; resonance positions above the top are quoted as ω_top
with the +17% Leg-A calibration; exact line positions and widths are
full-Teukolsky work (the remaining RCORE-3 computational upgrade),
as is the surface co-rotation boundary condition (committed item
(b)) and the Zel'dovich growth-time bounds (item (d)).

## §4 Registry impact

- **OPEN-GR-RCORE-3: Leg B DISCHARGED at eikonal-WKB grade.** The
  comb-restoration question is answered (NO, at any spin). REMAINS
  OPEN: full-Teukolsky line positions/widths; co-rotation BC;
  Zel'dovich bounds.
- **PRED-O-39 — PROVISIONAL refinement text registered here, NOT
  executed in predictions.md:** "GW150914-class remnant: no
  horizon-keyed comb; instead a line set at ~247–344 Hz (grade:
  eikonal-top +17% calibration, Q ~ 5), lowest line retrograde-keyed,
  plus early transients at 2.624 ms ± the GR-2 error budget; the
  corotating (ℓ,ℓ) lines are absent (burial)." Execution of the
  predictions.md amendment and the GR-2 amendment set (Leg-A pointer,
  onset 0.665, thin margin, line-set restatement) awaits a panel
  round — **CONV-034 (RCORE-3 Legs A+B audit) is the natural next
  dispatch** — and founder ratification, per the paper-edit and
  prediction-edit discipline.

## §5 Honest limits

Eikonal-WKB grade end to end; Q fixed by the eikonal correspondence
(exact only as ℓ → ∞); line positions above-top by an amount
calibrated at one point (Leg A, +17%); wall treated as
non-corotating Dirichlet (item (b) open); no amplitude, SNR, or
waveform statement; the burial verdicts inherit A1–A3 conditionality
(OPEN-GR-RCORE-4). The census integer N = 0 is robust across the
wall band and the spin scan, and is the load-bearing result.
