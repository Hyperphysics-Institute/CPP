# Problem History: THEO-SS-9 — Charge Quantisation δ = 1/3

**Created:** Pre-2026 (longstanding CPP problem)
**Status:** THEO (proved)
**Resolved:** 29 March 2026
**Resolution paper:** SM-1, Theorem 1 (v6)

---

## The Problem

Prove that the hDP overlap fraction δ = 1/3 exactly, giving quarks their fractional charges: q_up = +2/3 e, q_down = −1/3 e. In the Standard Model, charge quantisation has no geometric explanation — it follows from anomaly cancellation, which itself requires knowing the fermion content. A direct geometric derivation from the 600-cell would be the most striking single prediction of the CPP programme.

---

## The Journey

### Pre-2026 — The Integral Approach (Original CPP Derivation)

The original CPP derivation of δ was an SSV integral approach:

δ = φ⁻² × (outer overlap integral / total overlap integral)

where S(r) = 1/r⁴ (SSV stress density), γ(r) = 1 + kS(r) (Lorentz amplification), and the integration limits were set by the ZBW orbital radius.

**Result:** δ ≈ φ⁻² ≈ 0.382 — the right order of magnitude but carrying a ~15% error from the exact 1/3.

This was the accepted CPP answer for years. The ~15% was attributed to "higher-order corrections" that would eventually close the gap.

### 23 March 2026 — Mathematical Impossibility Identified

During the PS-1 session (600-cell shell analysis), a mathematical analysis proved that no φ-based integral can produce 1/3 exactly. The argument is algebraic: 1/3 is rational, φ is irrational (specifically, algebraic of degree 2 over ℚ), and 1/3 is not in the ring ℤ[φ]. No polynomial in φ with rational coefficients equals 1/3.

**Implication:** The integral approach cannot be the fundamental derivation. The value 1/3 must come from topology, not from continuous integration over φ-geometric quantities.

### 29 March 2026 — The C₃ Topological Proof

**The breakthrough:** Thomas, Claude Sonnet, and Grok identified that δ = 1/3 follows from two elementary observations about the tetrahedral cage:

**Lemma 1 (Cage completeness):** Every hDP chain of a confined qCP terminates on one of the three base vertices {V₁, V₂, V₃}. Proved: the chain cannot extend beyond r_conf without breaking.

**Definition (C₃ symmetry):** The rotation V₁ → V₂ → V₃ → V₁ is an exact isometry of the equilateral cage base.

**Theorem 1:** From C₃ symmetry: δ₁ = δ₂ = δ₃ (all three vertices equivalent). From cage completeness: δ₁ + δ₂ + δ₃ = 1 (exhaustive partition). Therefore **δ = 1/3 exactly**.

**Corollary:** q_up = +e(1 − 1/3) = +2/3 e. q_down = −e(1 − 2/3) = −1/3 e.

The proof is three lines. It uses no calculus, no φ, no integrals. It is purely topological.

### 29 March 2026 — Reconciling the Two Approaches

The integral approach gives δ ≈ φ⁻² ≈ 0.382, which is 15% above 1/3. This is now understood as a *physical motivation*, not a derivation. The SSV integral describes the continuous screening effect of the inner ZBW orbital — it gives the right order of magnitude because the physics is right. But the exact value 1/3 comes from the discrete symmetry, not from the continuous integral.

The 15% discrepancy is explained: φ⁻² ≈ 0.382 = (1/3) × 1.146. The integral overshoots because it does not enforce the discrete boundary condition (cage completeness) that forces the total to exactly 1.

### 29 March 2026 — The Deep Connection

**Corollary discovered same session:** Both charge quantisation (δ = 1/3, from the combinatorial structure of K₃) and the Koide formula (K = 2/3, from the spectral structure of K₃) arise from the same K₃ graph. The two deepest CPP lepton results share one geometric source.

δ = 1/3 uses the *combinatorial* structure (vertex counting under symmetry).
K = 2/3 uses the *spectral* structure (eigenvalue ratio of the adjacency matrix).
Both are exact. Both are derived from the same three-vertex equilateral base.

---

## Status Progression

| Date | Status | Event | Paper |
|------|--------|-------|-------|
| Pre-2026 | OPEN | δ ≈ φ⁻² from SSV integral (~15% error) | C15, CPP-5014 |
| 23 Mar 2026 | OPEN | Mathematical impossibility: no φ-integral can give 1/3 | PS-1 session |
| 29 Mar 2026 | THEO | **C₃ + cage completeness → δ = 1/3 exactly** | SM-1 Theorem 1 (v6) |
| 29 Mar 2026 | THEO | K₃ identified as common source of δ=1/3 and K=2/3 | SM-3 |

---

## Lessons

1. **The right answer can come from the wrong method.** The integral approach gave ~0.38, close enough to suggest 1/3 was the target. But no amount of refinement of the integral would have reached 1/3 exactly, because the answer is topological, not analytic.

2. **Impossibility results are progress.** Proving that φ-arithmetic cannot produce 1/3 was the negative result that redirected the search from integrals to topology.

3. **The simplest proof is often the last one found.** Three lines of algebra (symmetry + completeness + arithmetic) solved what years of integral refinement could not.

---

## Cross-References

- **research_frontier.md entry:** THEO-SS-9 (§4 Recently Resolved, §5 Resolved Archive)
- **Related problems:** OPEN-SS-13 (ZBW mechanical confirmation of 1/3), OPEN-SM-7e (why N=3 vertices)
- **Key connection:** THEO-SM-2 (K = 2/3 from same K₃)
- **Development transcript:** `series_standard_model/development-transcripts/development_transcript_SM-1.md`
- **Source files:** `open_problems/OP-SS/OP-SS-9_charge_quantisation.md`

---

*Problem history created 12 April 2026. Source material: OP-SS-9 problem file (29 March 2026), PS-1 session notes (23 March 2026), SM-1 paper.*
