# Grok Review of THEO-DSL-9 (Patch 0615) — face-aligned $V_4$/2-D correction to THEO-DSL-8

## Metadata

- **Reviewer**: Grok (xAI)
- **Subject reviewed**: THEO-DSL-9 (candidate) — `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/hardened_theorems/o_delta_two_face_aligned_coefficient.tex` (Patch 0615) — and the embedded structural correction to THEO-DSL-8 (Patch 0597) registered there.
- **Subject version commit**: `8893f86` (Patch 0616 origin/main head)
- **Review session**: Session 147
- **Review archived by**: Patch 0617 (this file)
- **Review delivered**: 28 May 2026 (Session 147 multi-AI review cycle for the THEO-DSL-8 $C_s\to V_4$ correction)
- **Reviewer panel position**: Round 1 of the THEO-DSL-9 / THEO-DSL-8-correction review cycle. Grok occupies the secondary-reviewer position (between ChatGPT primary and Copilot tertiary); the vocabulary-contamination concerns from earlier sessions (cf. Patch 0410+ history) are not in evidence in this review.
- **Review character**: **Decisive CONFIRMED verdict with full independent numeric reconstruction from first principles**. Built the 120-vertex 600-cell from scratch using the explicit construction (16-cell + tesseract + snub 24-cell with even-permutation parity check), located the face combinatorially, extracted $\hat n_{\perp 3}$ via SVD null-space of the $3\times 4$ matrix $[v_h; u_i; u_j]$, and produced the **clean explicit witness $\sigma_F = \mathrm{diag}(1,1,1,-1)$** for the canonical host $v_h = (1,0,0,0)$ — making the 600-cell automorphism property immediately visible (the construction is manifestly coordinate-symmetric). Independently verified all five questions: Q1 (vertex set stability of $\sigma_F$ to 10 decimals) ✓; Q2 ($V_4$ group structure + rank-2 averaging projector) ✓; Q3 (basis degeneracy analytically + Gram singular value $\sim 10^{-16}$ numerically) ✓; Q4 (144-path sum reproducing $\alpha_2^{(\rho)} = -7/\phi^2$ and $\alpha_2^{(\text{ax})} = -6+2\phi$ to machine precision, plus the $-9/\phi^2$ vertex cross-check) ✓; Q5 (orbit-stabilizer $|I_h|/30 = 4$ saturates $V_4$; no larger group found) ✓. **No errors or ambiguities noticed.** Per-shell-class B.1–B.4 decomposition explicitly verified to match the paper's table.
- **Programme-level reviewer ranking**: Grok delivers the strongest independent numeric verification of the cycle — producing the explicit $\sigma_F$ matrix that any subsequent reviewer can re-derive and check trivially. The review closes the load-bearing Q1 gap left by Copilot's analytic-only assessment.
- **Verdict-state classification**: **EXPLICIT CONFIRMED (numeric independent)**. The most decisive of the three reviewer letters. Combined with ChatGPT's CONFIRMED (numeric independent, also Q5 host-stabilizer enumeration) and Copilot's PARTIAL/UNCERTAIN (analytic-confirm-conditional-on-Q1, no refutation), overall cross-reviewer position is **THREE-FOR-THREE no-refutation with two independent numeric confirmations**. THEO-DSL-9's $V_4$/2-D/$1\!\to\!2\!\to\!2$ correction stands as multi-AI confirmed.

---

## Reviewer letter (verbatim)

**CONFIRMED** (THEO-DSL-9 correction holds; V₄/2-D invariant subspace and α₂ coefficients are correct; THEO-DSL-8 is superseded as stated in the anti-erasure remark).

**Methods (all independent first-principles verification, no reliance on the paper's verify script or any external repository):**

- **Q1 (decisive):** Numeric. Explicitly generated the full set of 120 unit vectors exactly as defined (8 coordinate-axis, 16 half-integer, 96 even-permutation-of-(±φ/2, ±1/2, ±1/(2φ), 0) using `itertools.permutations` + parity check on inversions). Picked convenient host `vₕ = (1,0,0,0)` (or equivalently `(-1,0,0,0)` in cross-checks). Located a concrete triangular face `{vₕ, uᵢ, uⱼ}` among the 12 neighbours (dot product = φ/2) by brute-force search over neighbour pairs. Formed the 3×4 matrix M = stack(vₕ, uᵢ, uⱼ), extracted `n̂_{⊥3}` as the right singular vector of the zero singular value (`np.linalg.svd(M, full_matrices=True)[2][-1]`), normalized. Built Householder `σ_F = I₄ – 2 n̂_{⊥3} n̂_{⊥3}ᵀ`. Transformed all 120 vertices; the image set equals the original set (rounded to 10 decimals for exact-set equality). By construction `σ_F` fixes the 3-flat span{vₕ, uᵢ, uⱼ} pointwise and therefore fixes `n̂_{F⊥}` (and vₕ).
  Concrete matrix for the chosen face: `n̂_{⊥3} = (0,0,0,1)`, so
  **σ_F = diag(1,1,1,–1)** (reflection through the first three coordinates). This visibly preserves the coordinate symmetries of the 600-cell vertex set.

- **Q2:** Numeric + group theory. Built the companion `σ_E = I – 2 n̂_diff n̂_diffᵀ` (n̂_diff = normalize(uᵢ – uⱼ)). Formed C₂ = σ_E σ_F. All four elements {I, σ_E, σ_F, C₂} are distinct, each squares to I, they commute (normals n̂_diff ⊥ n̂_{⊥3} by the claimed orthonormal frame), and their common +1 eigenspace is exactly span{n̂_ρ, n̂_ax} (rank-2 projector obtained by averaging over the group has rank 2). The two reflections annihilate n̂_diff and n̂_{⊥3} respectively, as required.

- **Q3:** Analytic (also confirmed numerically). By definition of the radial projection:
  **uᵢ + uⱼ = (uᵢ·vₕ + uⱼ·vₕ) vₕ + P_{vₕ^⊥}(uᵢ + uⱼ) = φ vₕ + P_{vₕ^⊥}(uᵢ + uⱼ)**.
  The perpendicular part is exactly parallel to n̂_ax by its definition in the prompt. Therefore
  **n̂_{F⊥} ∝ vₕ + uᵢ + uⱼ ∈ span{n̂_ρ, n̂_ax}**.
  Numerically the 3×3 Gram matrix of {n̂_ρ, n̂_ax, n̂_{F⊥}} has determinant ≈ 0 (rank 2, singular value ≈ 10⁻¹⁶).

- **Q4:** Numeric. Assembled the 144 directed 2-edge paths exactly as defined (for each of the 12 u ∈ S₁, loop over all 12 neighbours v′ of u; ê₁ = normalize(u – vₕ), ê₂ = normalize(v′ – u)). Accumulated
  **j₂ = Σ (ê₁·n̂_{F⊥})(ê₂·n̂_{F⊥}) ê₁**.
  Projected onto the four-frame basis. The n̂_{⊥3} and n̂_diff components are identically zero (≈ 10⁻¹⁵–10⁻¹⁷ floating-point noise). The surviving coefficients match the claimed closed forms to machine precision:
  **α₂^(ρ) ≈ –2.67376 = –7/φ²**, **α₂^(ax) ≈ –2.76393 = –6 + 2φ**.
  The vertex-aligned sanity check (replace n̂_{F⊥} by vₕ) reproduces exactly **–9/φ² ≈ –3.43769** along n̂_ρ (perpendicular residuals < 10⁻¹⁶). The decomposition into B.1–B.4 shell classes also reproduces the paper's per-class table exactly.

- **Q5:** Numeric + orbit-stabilizer. The four elements of V₄ are automorphisms fixing (vₕ, n̂_{F⊥}). No additional host-fixing automorphism preserving n̂_{F⊥} was found (the full point-stabilizer Iₕ has order 120; there are 30 incident faces per vertex, so the unordered-face stabiliser has order exactly 120/30 = 4 by orbit-stabilizer; V₄ saturates it). None of σ_E, σ_F, C₂ fails to be an automorphism.

**Vertices/matrices/arithmetic relied upon (cross-checkable):**
- vₕ = (1, 0, 0, 0) (or (–1,0,0,0)), one explicit face with uᵢ, uⱼ ∈ S₁ satisfying the three dot products = φ/2.
- n̂_{⊥3} = (0,0,0,1) (or equivalent up to sign/choice of face).
- σ_F = diag(1,1,1,–1) as above.
- All 120 vertices generated exactly as in the prompt; set-equality after transformation is literal (no floating-point loophole).
- All inner products, norms, and the 144-term sum use double-precision; agreement to 10⁻¹⁵ or better.

**Errors/ambiguities noticed:** None. All definitions are self-contained and unambiguous. The "even permutations" clause is precisely the standard generating set for the 96 vertices; the frame is confirmed orthonormal; the rate-function preservation follows immediately once σ_F ∈ Aut(600-cell) and n̂_{F⊥} is fixed. The setup is clean and the claims survive adversarial numeric scrutiny.

The V₄ residual symmetry, the 2-dimensional invariant subspace span{n̂_ρ, n̂_ax}, the degeneracy of the old 3-vector basis, the corrected 1→2→2 growth pattern, and the exact α₂ coefficients are all confirmed. The anti-erasure correction in the submitted LaTeX artifact is valid.
