# 0951 — C3's K_lift recomputed with the residual on: it clears. All three CAPACITY-1 conditions are robust; the restatement now needs a panel, not a computation

**Lane:** chirality (09xx). **Patch:** 0951, 13 Sep 2026, Opus. **Layer:** 2/3 bookkeeping. **Verify:** `chirality_derivations/code/0951_c3_klift_recompute.py` (5/5), run in **0821's own machinery** — same η-field, same orientation weights, same correlator-vs-graph-distance estimator — rather than a reconstruction. **Closes:** the single item Patch 0950 left between V3 and unconditional-on-the-residual.

## Result

**K_lift is essentially unmoved by the residual, and C3 clears on both channels with wide margins.**

| case | K_lift | /K_c uniform (1/12) | /K_c staggered (1/3.708) |
|---|---|---|---|
| A = 0 (0821 baseline, reproduced) | 0.0532 | 0.64 | 0.20 |
| A = δ, worst κ | 0.0532 | 0.64 | 0.20 |
| A = 0.5, worst κ | 0.0530 | 0.64 | 0.20 |
| A = 1.0, worst κ | 0.0526 | 0.63 | 0.20 |

**Worst case over everything tested: 0.0532 — margin 36% (uniform), 80% (staggered).** The η-correlator also stays short-range throughout, |C_d2/C_d1| ≤ 0.008 (T5), so the nearest-neighbour confinement that C1's shared-edge step relies on is undisturbed.

## How the residual enters, and why it barely matters

In 0821 the per-edge variable is `x_e = δ·bias_e + N(0,1)` with `bias_e = ê·n̂` — the rate law's tilt appears as a per-edge **mean shift**, and that tilt is *reversal-odd*. The residual `A (m·n̂)` is **reversal-even**: it multiplies both traversal directions of an edge equally, so it cannot shift that mean. It enters instead as a per-edge **scale** on the edge's fluctuation, `x_e = δ·bias_e + (1 + κ·A·m_e·n̂)·N(0,1)`. The proportionality κ between rate modulation and d.o.f. scale is **not on file**, so it was scanned over κ ∈ {±0.5, ±1, ±2} and the worst case reported rather than a value assumed.

The insensitivity has a structural reason worth recording: **η is a sign.** `η_v = sign(Σ_e w_e x_e)` is invariant under positive rescaling of its argument, so a per-edge scale modulation affects the correlator only through the *relative* weighting within a single vertex's read — a second-order effect on the shared-d.o.f. fraction ρ that sets `C_nn = (2/π)arcsin(ρ)`. A reversal-even perturbation is close to the worst possible way to try to move a sign-valued order parameter.

**A correction to 0950.** Patch 0950 flagged this as a live risk on the strength of a 10.9% shift in the stationary measure π. That flag was right to raise but aimed slightly off: K_lift is not computed from π. It is computed from the correlator of the η-field over the edge d.o.f., and the 10.9% figure does not transfer to it. The recompute was still worth doing — "not computed from π" needed checking, not asserting — but the honest record is that 0950 over-weighted the risk.

## Where V3 now stands

All three of CAPACITY-1's discharged conditions have been checked against L4-A's named residual:

- **C1 — robust** (0950): per-edge independence survives because both residual terms are per-edge functions; and the 0828 refined-chord bound never references the rate law, being built from the observable's weights under the pointwise floor. 0828 was specifically hardened for n̂-dependent non-uniform rules, which is what A ≠ 0 produces.
- **C2 — robust where it claims** (0950): a constant A promotes the small-δ steady-current scaling from δ³ to ~A²δ, a real effect; but C2 is stated at the physical bias, and at δ = φ⁻³ the magnitude spread across A ∈ [0,1] is a factor of 2 with O(J²) ≤ 1.1×10⁻⁹. Divergence-free and T-odd throughout.
- **C3 — robust** (this patch): K_lift unmoved, both channels clear with 36% / 80% margins, correlator still short-range.

**So the computational case is complete: THEO-CHIR-CAPACITY-1 does not consume L4-A's residual.** Its Mechanism-A conditionality is on derived content only — MA.1's reversal-odd first harmonic, which Patch 0949 showed is *forced and unique*.

## What is NOT done here, and why

**I am not restating CAPACITY-1's conditionality, and no verdict moves.** Restating a registered theorem's conditionality is verdict-adjacent, and CONV-001 requires a multi-reviewer panel for that class of move. A single window cannot close it, and this one has run one pass with no panel. What this patch establishes is that **the restatement is now a review question rather than a research question** — the computations it would need are done and on file.

The proposed restatement, for whoever runs the panel:

> THEO-CHIR-CAPACITY-1 is conditional on **MA.1's reversal-odd first harmonic** — `r(ê) = r₀(1 + δ ê·n̂)` with δ ≡ B — together with per-edge independence and pointwise non-degeneracy of the dynamical η. It is **not** conditional on A = 0 or on first-harmonic truncation. The reversal-odd first harmonic is derived, not assumed (Patch 0949).

Note that **piece 1 — pointwise non-degeneracy of the dynamical η — is untouched by any of this** and remains CAPACITY-1's live conditionality, exactly as 0924's Q5 framed it. That is the residual that would still stand after the restatement, and it is a different question from L4-A's.

## Disposition

- **C3 recompute: done, clears.** The 0950 item is closed.
- **No verdict moves. CAPACITY-1 untouched. No THEO registered.** Single pass, no panel.
- **Owed:** the CONV-001 panel for the conditionality restatement (packet would assemble 0949 + 0950 + 0951); piece-1 non-degeneracy remains open and unaffected.
- **W3 unaffected** throughout: `sign(δ) = sign(B)` is O(δ¹).
