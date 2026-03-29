# OP-SS-11: Uniqueness of the SU(3) Operator Mapping from Tetrahedral Cage Geometry

**Priority:** HIGH
**Status:** OPEN
**Series:** SS-1
**Registered:** 29 March 2026
**Source:** Reviews-SS-1.md (Genuine Weakness G1); session discussion 29 March 2026

---

## Statement

SS-1 Theorem 1 proves that the eight tetrahedral hopping operators
$T^a$ computed from the cage base $\{V_1, V_2, V_3\}$ equal the
Gell-Mann generators $T^a = \lambda^a/2$ exactly. What is not yet
proved is that this mapping is **unique**: that there is no other
assignment of operators to the tetrahedral cage geometry that yields
a different Lie algebra consistent with the C₃ symmetry constraint.

Formally: prove that the set of eight traceless Hermitian operators
on $\mathbb{C}^3$ with C₃ cage symmetry and the constraint that each
operator corresponds to a single tetrahedral edge (real or imaginary
hopping) or diagonal phase difference is **unique up to overall phase**,
and that the Gell-Mann convention is the standard choice within this
unique family.

---

## Why This Matters

If alternative operator assignments exist that satisfy the same
geometric constraints but yield a different 8-dimensional Lie algebra,
the SS-1 derivation would show that SU(3) *can* emerge from the
tetrahedral cage — but not that it *must*. The theorem would become a
possibility result rather than a necessity result.

A uniqueness proof would elevate Theorem 1 from "SU(3) is consistent
with the tetrahedral cage" to "SU(3) is the unique algebra consistent
with the tetrahedral cage, given the CPP primitives."

---

## Current Evidence for Uniqueness

The C₃ symmetry and 8-count argument jointly suggest uniqueness:

1. **Dimension count is forced:** The 8 independent traceless Hermitian
   operators on $\mathbb{C}^3$ are exactly the dimension of su(3).
   There is no freedom in the count.

2. **Edge structure is canonical:** The real and imaginary hopping
   operators on each of the three edges, plus the two independent
   diagonal phase operators, form a basis that spans all of
   $\mathfrak{su}(3)$. This spanning is a consequence of the
   completeness of the tetrahedral edge structure.

3. **C₃ constraint eliminates alternatives:** Any alternative operator
   assignment must respect C₃ symmetry (the three base vertices are
   geometrically equivalent). The C₃-invariant operators on a
   3-dimensional space form a restricted class, likely too small
   to accommodate a non-SU(3) 8-dimensional algebra.

The argument is plausible but not yet written as a proof.

---

## Suggested Approach

1. Classify all traceless Hermitian operators on $\mathbb{C}^3$ that
   are invariant under C₃ rotation (i.e., commute or transform simply
   under $V_1 \to V_2 \to V_3 \to V_1$).

2. Show that this set has dimension exactly 8.

3. Show that any basis for this set satisfies the SU(3) commutation
   relations (possibly with a different choice of structure constants
   $f^{abc}$, which would correspond to a different convention for
   labelling the generators — equivalent to SU(3) up to relabelling).

4. Conclude that SU(3) is the unique algebra that can be embedded in
   the tetrahedral cage geometry with C₃ symmetry.

This is a finite-dimensional linear algebra argument and should be
tractable in 1–2 pages. The most natural setting is the
representation theory of the cyclic group C₃ acting on $\mathbb{C}^3$.

---

## Recommended Placement

A short uniqueness argument (one paragraph or a brief lemma) should
be added to Section 4.1 of SS-1 as a v4 addition or as part of the
SS-1b companion paper on the SU(3) algebra derivation.

---

## Feeds Into

- SS-1 Theorem 1 (strengthens from possibility to necessity)
- OP-G-2 (full SM derivation — gauge group uniqueness is foundational)
- Any claim that CPP "derives" SU(3) rather than "accommodates" it
