# Founder ruling — Reading C's ℓ is a directed traversal cost

**Date:** 14 September 2026. **Authority:** PD-006(a) — a physics question framed in a physical picture.
**Registered:** Patch 0976, chirality lane. **Source of the question:** Patches 0972, 0973.

## The question put to the founder

Reading C writes `ℓ(ê) = ℓ₀(1 + ε ê·n̂)` and calls it an effective edge length. But `ê·n̂` is
reversal-**odd**: traversing the same edge the other way sends `ê ↦ −ê` and returns a different
value (0.999691 vs 1.000309 at the physical bias). A metric is a symmetric bilinear form, so every
length built from an inner product is reversal-even on any lattice whatever — verified over 200
arbitrary positive-definite metrics, forward-minus-backward exactly 0.0.

Two options, and only two (0972 T4):

1. Relabel `ℓ` as a **directed traversal cost** (equivalently a hop time). The equation stands; only
   its description was wrong.
2. Defend `ℓ` as a genuine reversal-even length — in which case `r = c/ℓ` is reversal-even, generates
   the `A`-term, and `δ = 0` exactly.

## The ruling

> **Relabel accepted.**

## What it commits the programme to, and what it does not

- **It is not a new field.** The 1-form permitting a directed cost is a Randers/Finsler `β = ε n̂`,
  built from `n̂`, which is already a substrate primitive (FI-C-RC-1). What changes is whether `n̂`
  enters as a direction (even structure only) or as a 1-form (odd structure available).
- **The substrate is not non-reciprocal in space.** Its geometry stays reciprocal. Its *dynamics* are
  non-reciprocal *in time*, which is what an arrow of time means. Detailed-balance violation comes
  entirely from the reversal-odd part: the even term `A(m̂·n̂)` gives maximum cycle affinity exactly
  zero at A = 0.3, 0.5 and 1.0, while the odd term violates on 420 of 1200 faces (0973, verify 6/6).
- **The non-reciprocity is the T-arrow the arc already carries as W3.** With THEO-CHIR-MERGE-2
  (`sign(δ)` is P-even and T-odd — an arrow, not a chirality), `costs more one way` ⟺ `detailed
  balance violated` ⟺ `not time-reversible`. Nothing is added to the ontology.
- **No verdict moves and no count changes.** This is a description, not a result.

## Where it is written into the corpus

`capotauro.tex` (footnote at the Reading C edge-perturbation equation) and
`dynamical_substrate_law.tex` §"Structural connection to Reading C" plus the §"not pinned" paragraph,
both at Patch 0976.
