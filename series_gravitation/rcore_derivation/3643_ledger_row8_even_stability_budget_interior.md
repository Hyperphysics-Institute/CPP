# Ledger row 8 PASSES [PCD-EXT]: 3390's even-sector instability was the clamp's. Under THEO-PCD-BUDGET the register is not pinned at the surface, the wave transmits inward through the C¹ metric, and the even wall's boundary "mass" is the core's inertia — positive. The ℓ = 2, 3 poles at 8M/3 are damped (0.4586 − 0.1315 i, 239 Hz, Q 1.7; 0.6882 − 0.1027 i, 359 Hz, Q 3.4), and an argument-principle count shows the upper half-plane EMPTY in the band (the trace wall's count is 1: the growing mode). OPEN-GR-SURFACE-STABILITY-1 resolves on branch (a). A convention error found in passing: 3390's odd-sector line at 8M/3 carried J = 6.75, the 9M/4 value; the dictionary gives 32/9 there

**Patch 3643, Session 163, 5 Sep 2026.** Verify `code/3643_ledger_row8_even_stability_budget_interior_verify.py` (24/24). Reasoning `reasoning/3643.md`. No paper touched. CONV-042 held. Ledger `3641_triangulation_ledger.md` row 8 updated to **passes**.

## §1 What row 8 asked
3641 §4 row 8: "Even-sector surface stability (3390's b₂ < 0) — re-run with the C¹ interior (no shell) — a fail here is a fail of the extension." The trace-pinned wall (3378/3383/3390: the count channel clamped at the level set, `H₂ + 2K = 0`, the Robin law `β_ℓ = b₀ − b₂ω²`) has `b₀, b₂ < 0` at the ratified surface 8M/3 and supports growing modes (3390: `0.5199 + 0.034 i`, `0.7665 + 0.036 i`). Under the budget law (3640) there is no clamp: the register keeps recording above the cap at the scaled rate, the metric is C¹ through the surface (σ = P = 0), and the ringdown transmits inward (3639 §4) with the coordinate speed `N/ψ²` of the budget metric (3389). So the even sector becomes what 3384 built for the odd sector — transmit to a regular centre — with a graded interior in place of a flat one.

## §2 The model (least assumption; the arc's own rules)
- Interior master function `u = r̄ Φ`, `Φ` a minimally coupled scalar on the budget metric `−N² dt² + ψ⁴(dr̄² + r̄² dΩ²)`, `N = N(v_eff)`, `ψ = ψ(v_eff)`, `v_eff = 2·cap − cap²/v`, `v(r̄) = (M/2R̄)(3 − r̄²/R̄²)`:
  `(N ψ² r̄² Φ′)′ + [ω² ψ⁶ r̄²/N − N ψ² ℓ(ℓ+1)] Φ = 0`, regular at the centre (`Φ ~ r̄^ℓ`).
- Interface (3384's rule): `u` and `du/dr̄` continuous with the exterior Zerilli function; `du/dr̄ = J du/dr*`, `J = dr*/dr̄|_R`. Wall law on the exterior function: `β(ω) = (1/J)(u′/u)|_R`.
- With `N, ψ` frozen at the surface this is exactly 3384's Riccati–Bessel interior, `k = Jω` (verified to 2·10⁻¹¹): the flat core is the χ = 0 limit of the same computation.
- No channel split: the budget rule scales count and net by the same `K/D` (3640 §4), so the trace and the traceless parts of the even mode transmit together. (The split-channel alternative — count reflected, `Q_ij` transmitted, 3621 §1 — is the *other* reading of A3′; it is not the working extension and is not computed here.)

## §3 What the computation found
1. **J at 8M/3 is 32/9 = 3.556**, from the exterior dictionary `dr*/dr̄ = ψ(1 − v/2)/f`, and the budget interior's `ψ²/N` at the surface is the same number: the wave speed is continuous through the surface — no impedance step, as the C¹ join requires. **In passing: 3390 carried J = 6.75 (the 9M/4 value, 3384) into its odd-sector line at 8M/3.** 3389's "J = 6.75 at any wall" is false under its own dictionary (`N/ψ²` is `4/27` at v = 1 and `9/32` at v = 2/3). The odd-sector pole at 8M/3 (3390: 208 Hz, Q 7.9) is therefore owed a re-run with J = 32/9; it is not row 8 and is not done here. The interior speed under the budget law runs 0.281 (surface) → 0.184 (centre): slower inward, a graded-index core.
2. **The boundary mass is positive.** On the real axis `β` is real (lossless, |R| = 1). Its low-frequency law: ℓ = 2 `β = +0.550 − 0.967 ω²`; ℓ = 3 `+0.736 − 0.725 ω²` (flat-core reference `(ℓ+1)/(Jμ) − Jμω²/(2ℓ+3)` = `0.5625 − 0.762 ω²`, `0.750 − 0.593 ω²`). `b₂ > 0` is the inertia of the core the wave enters. 3390's `b₂ < 0` (`−9.36`, `−8.10` in 3390's convention) was the trace clamp's, and the clamp is not in the theory under the extension.
3. **The poles at 8M/3** (M = 1; Hz at 62 M☉):

| ℓ | wall | Mω | Hz | Q |
|---|---|---|---|---|
| 2 | Dirichlet (reference) | 0.3855 − 0.204 i | 201 | 0.9 |
| 2 | trace-pinned Robin (3390, control) | 0.5199 + 0.034 i | 271 | growing |
| 2 | flat core, J = 32/9 (χ = 0, transmit) | 0.4460 − 0.1411 i | 232 | 1.6 |
| 2 | **budget interior [PCD-EXT]** | **0.4586 − 0.1315 i** | **239** | **1.7** |
| 3 | Dirichlet (reference) | 0.6302 − 0.1801 i | 328 | 1.8 |
| 3 | trace-pinned Robin (3390, control) | 0.7665 + 0.036 i | 399 | growing |
| 3 | flat core, J = 32/9 | 0.6783 − 0.1259 i | 354 | 2.7 |
| 3 | **budget interior [PCD-EXT]** | **0.6882 − 0.1027 i** | **359** | **3.4** |

   r0-independent to 10⁻⁷; sharp (|F| rises 10⁵–10⁷× at +0.01 off the root). The 3390 control poles reproduce to 10⁻⁴.
4. **The upper half-plane is empty.** Winding number of the pole-free wall function `u ψ′ − (u′/J) ψ` around `Re ω ∈ [0.05, 1.2]`, `Im ω ∈ [0.005, 0.4]`: **0.000 (ℓ = 2), 0.000 (ℓ = 3)** under the budget wall; **1.000, 1.000** under the trace wall (the growing mode, counted). No growing even mode anywhere in the band, not merely none near a guess. This is what a lossless, regular, Hermitian interior with outgoing exterior must give; the count confirms the model is that.
5. **The interior cavity.** Optical depth centre → surface `∫ ψ²/N dr̄ = 7.27`, i.e. **1.363 × the flat-core value** — 3640's echo-cavity ratio read from the same geometry a second way. The first interior standing wave (ℓ = 2) sits at Mω ≈ 0.79 (≈ 410 Hz), above the ℓ = 2 line at 0.459: the lossless budget core does **not** split the a = 0 mode (3621's Kerr-surface problem — first resonance at the ringdown frequency — does not recur here at a = 0; whether it recurs at the Kerr surface with the graded profile is KERRWALL-1's, not row 8's).

## §4 What it means for the arc
- **OPEN-GR-SURFACE-STABILITY-1 resolves on branch (a)** (3390 §4): the trace-Dirichlet was the wrong *limit* of the surface — the zero-compliance clamp — and what regularises the negative boundary mass is not an O(kd) skin term but the removal of the clamp itself. Branches (b) (floor inside 2.38 M) and (c) (a physically unstable R-core) are not needed. Closed **[PCD-EXT]**: it stands with the extension.
- **The even-sector line moves from the clamp's sharp 271 Hz / Q 8 (unstable) to a broad 239 Hz / Q 1.7 — Dirichlet-like.** The R-core's even sector under the extension rings like a black hole's to present precision (Kerr's (2,2) at a = 0: 0.374 − 0.089 i for Schwarzschild; the budget line sits at the surface-shifted top-of-barrier value, as the odd sector did under bracket I in 3384). 3383's "near-trapped, Q 25/92" even lines were the clamp's; they do not survive. GR-2 V2.3 inherits this: the sharp even-sector echo lines of 3383/3390 are withdrawn with the clamp; the map statement of 3622's banner (exterior Einstein's, spectrum Kerr-like) is strengthened, not weakened.
- **The ledger:** row 8 **passes**. Order of work continues 7 → 6 → V2.3 → CONV-042 (3641 §5).

## §5 Owed (registered, not done)
- **Odd sector at 8M/3 with J = 32/9** (the 3390 line used the 9M/4 value); and the odd sector under the budget interior (graded, same equation with the RW exterior). One script; it belongs with row 7 (reflectivity), where both sectors' wall laws are needed.
- Row 7: reflectivity from the returned-bit fraction `(D − K)/D = 1 − cap/v = 1 − χ(r̄)`: zero at the surface, 1/3 at the centre — under the budget law the return is *distributed through the interior*, which is what the graded index already does to a wave; whether the returned bits add a sink term to §2's equation (a lossy interior, 3621 §2's requirement) or are the gradient reflection itself is row 7's question.
- Row 6 (Love number as spring deflection, χ = cap/v).
