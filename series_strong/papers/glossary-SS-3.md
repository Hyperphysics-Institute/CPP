# Glossary — SS-3: Uniqueness of SU(3) from the Tetrahedral Cage

**Paper:** SS-3 v1.3
**Last updated:** 15 April 2026

---

## Core Mathematical Objects

**su(3)** — The Lie algebra of traceless Hermitian 3×3 matrices with the bracket [X,Y] = i(XY − YX). Dimension 8. The algebra of the SU(3) gauge group governing the strong force.

**H₀³ (generator space)** — The real vector space of traceless Hermitian 3×3 matrices. Dimension 8. Identical to su(3) as a vector space; becomes su(3) when equipped with the bracket.

**Gram matrix** — The matrix G_{ab} = Tr(T^a T^b) measuring the inner products of the 8 CPP operators. The Gell-Mann orthogonality relation Tr(λ^a λ^b) = 2δ^{ab} gives G_{ab} = δ^{ab}/2 analytically — a diagonal matrix confirming linear independence without numerical computation. (Confirmed to 2.2×10⁻¹⁶ numerically.)

**Change-of-basis matrix M** — The 8×8 matrix defined by P_i = Σ_a M_{ia} T^a, where P = (L₁,...,L₄, H₁,...,H₄) are the physical modes and T^a are the Gell-Mann generators. Has det(M) = 2/√3 ≠ 0, confirming the physical modes form a basis for su(3). Six columns are unit vectors; the nontrivial 2×2 block mixes T³ and T⁸ through the two apex bond modes L₂ and L₄.

**Normalization convention** — Generators are T^a = λ^a/2, giving Tr(T^a T^b) = δ^{ab}/2. This is the standard physics convention under which structure constants f^{abc} take their standard values (e.g., f^{123} = 1, f^{147} = ½).

**Killing–Cartan classification** — The classification of simple Lie algebras into families A_n, B_n, C_n, D_n and exceptional algebras G₂, F₄, E₆, E₇, E₈. Used in the uniqueness proof to establish that su(3) (= A₂) is simple and has no 8-dimensional competitors. Reference: Humphreys (1972).

**Structure constants f^{abc}** — The coefficients in [T^a, T^b] = i·f^{abc}·T^c. Determined uniquely by the algebra and the choice of basis. The Gell-Mann convention uses the standard PDG values.

---

## CPP Terms

**Colour space** — ℂ³ with basis {|r⟩, |g⟩, |b⟩} corresponding to the three base vertices {V₁, V₂, V₃} of the qCP tetrahedral cage.

**Tetrahedral cage** — The fundamental structure of a quark in CPP: a tetrahedron with 4 vertices (1 apex qCP + 3 base vertices carrying colour states), embedded in the 600-cell lattice.

**DP chain** — A longitudinal string of alternating-polarity Dipole Pairs connecting vertices of opposite polarity. The physical objects whose oscillation modes correspond to gluon degrees of freedom.

**Linear bond mode** — An oscillation of a single DP chain along its edge (compression-extension). One of the 4 Group A modes in the 4+4 physical decomposition.

**Coupled harmonic junction mode** — A correlated oscillation of two DP chains meeting at a vertex, where one compresses as the other extends. One of the 4 Group B modes in the 4+4 physical decomposition.

**C₃ symmetry** — The three-fold rotational symmetry V₁ → V₂ → V₃ → V₁ of the cage base. An inner automorphism of su(3) that selects the Gell-Mann basis convention.

---

## Status Labels

**THEO-SS-10** — The theorem proved in this paper: SU(3) is the unique Lie algebra of the tetrahedral cage. (Theorem 3.3 in the paper; registered as THEO-SS-10 in theorem-registry.md.)

**OPEN-SS-11** — The open problem resolved by this paper: prove the uniqueness of the SU(3) operator mapping from tetrahedral cage geometry. Status: OPEN → THEO.

---

## Conventional Physics Terms

**Gell-Mann matrices (λ^a)** — The standard basis for su(3), conventionally denoted λ¹ through λ⁸. The CPP operators T^a = λ^a/2 are the generators in the fundamental representation.

**Gluon** — In QCD, the massless gauge boson mediating the strong force. 8 gluon states correspond to the 8 generators of SU(3). In CPP, these are DP chain oscillation modes on the cage bonds.

**Colour charge** — In QCD, a three-valued quantum number (red, green, blue). In CPP, the label of which base vertex of the tetrahedral cage is occupied.

**Simple Lie algebra** — A Lie algebra with no proper ideals. su(3) is simple, which means it cannot be decomposed into smaller independent subalgebras. This is used in the uniqueness proof.
