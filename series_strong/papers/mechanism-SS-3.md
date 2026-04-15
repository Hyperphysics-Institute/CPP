# Mechanism — SS-3: Uniqueness of SU(3) from the Tetrahedral Cage

**Paper:** SS-3 v1.1
**Last updated:** 14 April 2026

---

## Overview

SS-3 proves that SU(3) is the unique Lie algebra of the tetrahedral cage. The mechanism has two layers: an algebraic layer (the uniqueness proof) and a physical layer (the 4+4 mode decomposition identifying what the 8 generators are).

---

## The Algebraic Mechanism (Sections 2–3)

### Step 1: Count the degrees of freedom

A traceless Hermitian 3×3 matrix has 3²−1 = 8 real parameters. This is a fixed consequence of the colour space dimension N = 3, which is itself fixed by the 600-cell's tetrahedral cell geometry (3 base vertices per tetrahedron).

### Step 2: Recognise the algebra

The vector space of traceless Hermitian 3×3 matrices, equipped with the commutator bracket [X,Y] = i(XY − YX), IS su(3) by definition. This is not a derivation — it is the definition of su(3).

### Step 3: Verify the CPP operators span the space

The 8 CPP tetrahedral hopping operators (6 off-diagonal from edge hopping + 2 diagonal from phase differences) form a rank-8 system (Gram matrix determinant 3.9×10⁻³ ≠ 0). They are therefore a basis for the full 8-dimensional space and generate su(3) necessarily.

### Why no alternative is possible

Any alternative set of 8 traceless Hermitian 3×3 operators that is linearly independent generates the same algebra su(3) — just in a different basis (different structure constants, same algebra up to isomorphism). Any set with fewer than 8 independent operators generates a proper subalgebra (at most su(2) or u(1), dimension ≤ 3). su(3) is simple — it has no 8-dimensional competitors.

---

## The Physical Mechanism (Sections 5–6)

### The polarity structure

The full tetrahedron has 4 vertices with definite polarities in a baryon: 1(+), 2(+), 3(−), 4(−). Of the 6 edges, 4 are opposite-polarity (carrying DP chains) and 2 are same-polarity (repulsive, no chain).

### Group A: 4 linear bond modes

Each of the 4 opposite-polarity DP chains oscillates longitudinally — the chain compresses and extends along its edge. These are the single-bond vibrational modes.

| Mode | Bond | Type |
|------|------|------|
| L₁ | V₁(+)–V₃(−) | Linear oscillation |
| L₂ | V₁(+)–V₄(−) | Linear oscillation |
| L₃ | V₂(+)–V₃(−) | Linear oscillation |
| L₄ | V₂(+)–V₄(−) | Linear oscillation |

### Group B: 4 coupled harmonic junction modes

At each vertex, exactly 2 opposite-polarity chains meet. The two chains oscillate as a coupled pair — when one compresses, the other extends.

| Mode | Junction | Path | Pattern |
|------|----------|------|---------|
| H₁ | V₃(−) | 1(+)–3(−)–2(+) | (+)(−)(+) |
| H₂ | V₁(+) | 4(−)–1(+)–3(−) | (−)(+)(−) |
| H₃ | V₂(+) | 4(−)–2(+)–3(−) | (−)(+)(−) |
| H₄ | V₄(−) | 1(+)–4(−)–2(+) | (+)(−)(+) |

### The count

4 linear + 4 harmonic = 8 = dim(su(3)).

### The relationship between the two bases

The mathematical basis (Gell-Mann: 6 off-diagonal + 2 diagonal) and the physical basis (4 linear + 4 harmonic) are both valid bases for the same 8-dimensional vector space. They are related by a linear transformation. The mathematical basis is convenient for computation; the physical basis tells you what is vibrating.

---

## Mathematical Correspondence Table

| CPP Element | Mathematical Object | Physical Meaning |
|-------------|-------------------|-----------------|
| 3 base vertices | ℂ³ colour space | 3 colour states |
| 8 independent operators | Basis for su(3) | 8 oscillation modes |
| Linear independence (rank 8) | Spanning condition | All modes are distinct |
| Commutator bracket | Lie algebra structure | Coupled oscillation dynamics |
| C₃ symmetry | Inner automorphism | Basis convention (Gell-Mann) |
| Tracelessness | No U(1) component | No colour-singlet gluon |
| Hermiticity | Observable operators | Modes have real energy |
