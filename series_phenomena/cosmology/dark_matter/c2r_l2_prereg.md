# C2R-L2 PREREG (FROZEN) — near-core correction: χ(r) by the founder's superposition specification, realized as the derived closure's own distributed response cloud, and the correction δℓ/ℓ_LO COMPUTED through the frozen operator on arenas A0/A1 (not scaled from any input-side figure)

**Patch 2772, 22 July 2026. Charter: `fa_c2_rederivation_charter.md`
§2 (C2R-L2). Frozen before execution. Physics inputs: the 2767
founder ruling §2 verbatim (fence F3); the L1 closure κ² = 4πnα
(2770). Reasoning: `reasoning/2772.md`. Fences F1–F3 in force;
79.5% not in scope.**

## Fidelity mapping (founder clause → model element; committed)

The 2767 §2 specification is realized with NO ingredient beyond the
L1-derived closure plus linearity:

1. *"Every charge will be surrounded by a DP Sea … create a gradient
   of eCP plus-minus radial distribution to produce the Gauss's law
   gradient effect"* → the medium's linear response to a unit charge
   is the self-consistent induced-charge cloud of the derived
   screened equation: **ρ̂(r) = κ² e^(−κr)/(4πr)** (normalized to
   unit total). Near the charge the governing field is the
   inverse-square 1/r² Coulomb field (the founder's "inverse square
   law … change in radial polarization gradient with radius");
   the enclosed induced charge inside radius r is
   1 − (1+κr)e^(−κr), smoothly 0 → 1 — the Gauss's-law
   enclosed-charge criterion holds analytically on every closed
   surface.
2. *"With the two charges next to each other, there will be a
   superimposition of the two curves with opposite polarities, and
   so that superimposition will be the net radial polarization
   gradient"* → the site-attributed responses q_j carry the cloud
   shape and superpose linearly: **χ(r) = Σ_j q_j ρ̂(|r−r_j|)**.
   Adjacent sites in the staggered solution carry oppositely-signed
   q_j, so the between-sites profile IS the superposition of
   oppositely-signed curves. Deliverable (i) is this profile
   evaluated on the nn axis between adjacent sites and around a
   site.
3. *Occupancy (2767 §4.1–4.2)* → the r < a medium responds; in the
   operator this enters as (a) the softened off-diagonal kernel and
   (b) the site's own near-field cloud acting at its GP (a finite
   r > 0 contribution — NOT the excluded point-like same-GP
   self-superposition).

**Readings considered and rejected (committed):** (a) bare 1/r²
polarization with a hard core cutoff — violates the Gauss
normalization and re-introduces an exclusion radius the 2767 ruling
rejects; (b) modulating the per-site χ by the static plus/minus
density asymmetry — second order in the weak bias, outside linear
response, not chartered.

## Route (committed)

1. **Corrected operator.** Leading order idealized each site's
   response as a point. L2 distributes it as q_j ρ̂(r−r_j). The
   potential of the normalized cloud is g(r) = (1 − e^(−κr))/r,
   with g(0) = κ finite. The site system becomes
   **(I + α G̃) ψ = ψ_ext**, G̃_ij = g(r_ij) for i ≠ j,
   G̃_ii = g(0) = κ. External source: unchanged point at the
   central vertex (the frozen assembly's probe; the founder spec
   governs the responding medium, not the probe).
2. **Analytic cross-check (deliverable iii, analytic side).**
   Homogenized, the corrected closure reads
   ψ̂ = ψ̂_ext / [1 + κ⁴/(k²(k²+κ²))]; its poles are complex,
   k² = κ²(−1 ± i√3)/2 — the corrected continuum medium itself
   screens with damped oscillation. The predicted continuum decay
   rate Im(k) and wavelength are computed and compared OBS-class
   (non-adjudicative) with the lattice readout.
3. **Lattice execution (deliverable ii + iii, numerical side).**
   Arenas A0 (FCC ball) and A1 (HCP ball) — the charter-named
   pair — at R = 7 and 9, constructed by the committed 2685
   builders, sanity-gated identically (N, min chord, interior
   z = 12). For each (arena, R): solve baseline (I + αG)φ = 1/r₀
   and corrected (I + αG̃)φ̃ = 1/r₀ in the SAME script; extract ℓ
   with the frozen windows [0.45,1.3], [0.55,1.6], [0.7,1.8] fm,
   bin-mean |f| observable, identical fit machinery to 2685.
   Staggering statistics (nn sign-flip, negative fraction over
   r ∈ [0.4, 2.0] fm) reported for both operators same-font.
4. **The correction, paired.** δ(arena, R, window) =
   ℓ_L2/ℓ_base − 1 on matched variants (pairing cancels shared
   instrument systematics). **δℓ/ℓ_LO = mean ± 1σ across the 12
   variants**; per-arena sub-bands quoted. Sign, magnitude, error —
   the deliverable (ii) statement.

## Decision quantities (frozen; feed charter §3)

- **D3 = |δℓ/ℓ_LO|** vs **W = 3.1%** (charter §3). D3 ≤ W →
  second CONFIRM condition met (L1 already met the first);
  D3 > W → C2R-CORRECTED fires at L4 with ℓ_derived =
  ℓ_LO × (1 + δℓ/ℓ_LO).
- **Structural report (same-font, non-optional):** whether the
  staggering survives the corrected operator. Effective on-site
  stiffness rises to 1 + ακ = 1.4501 (α_eff/α ≈ 0.690), which the
  2688 three-regime ℓ(α) map says can cross the staggering
  threshold; if the corrected medium exits the staggered regime,
  that is a structural finding of the correction, reported in full,
  and the envelope is fit on whatever decay form the field shows
  (committed fallback: same log-linear r·|f| fit; R² quoted).
- **Honesty bound (committed):** the cloud shape ρ̂ is the
  leading-order self-consistent profile; iterating the shape at the
  corrected operator (one order beyond) is NOT chartered. If
  |δℓ/ℓ_LO| > 50%, the iteration question is NAMED in the record as
  a concrete open item rather than silently absorbed. This route
  cannot hit C2R-OBSTRUCTED by construction unless the corrected
  solve fails to produce a fittable decay on both arenas — in which
  case the leg stops and reports, no partial number.

## Verify script (committed spec)

`code/2773_c2r_l2_profile.py`, deterministic, no seeds beyond the
committed 2685 builder constants: builds A0/A1 at R = 7, 9; solves
both operators; prints per-variant ℓ, R², staggering; prints the
paired δ table, δℓ/ℓ_LO band, the χ(r) nn-axis profile table
(deliverable i), and the analytic complex-pole comparison. All
record numbers quote script output.
