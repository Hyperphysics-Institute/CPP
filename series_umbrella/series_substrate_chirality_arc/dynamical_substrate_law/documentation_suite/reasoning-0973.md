# reasoning-0973 (verbatim, captured late — see chirality_derivations/reasoning/0942.md header note; same provenance)

The founder asked what field could cause a directed traversal cost, and said: "We are just looking at a lattice… I think we are just talking about the lattice's geometry. Am I correct?"

**He was correct, and that is what resolved it.** Checked his premise first rather than reaching for an answer: over 200 arbitrary positive-definite metrics on the 600-cell, forward and backward edge lengths differ by exactly zero. Necessarily — a metric is symmetric, so `g(−v,−v) = g(v,v)` identically. **Pure geometry cannot produce a directed cost on any lattice.**

So his instinct was not a gap in his understanding; it was the proof that the asymmetry is not geometric.

**What the "field" is, mathematically:** the only way to get a direction-dependent length is a term linear in direction — a 1-form. That is a Randers/Finsler structure, `F(v) = √(g(v,v)) + β(v)` with β = ε n̂. Real, and named. **But not a new field:** β is built from n̂, already a primitive. What changes is whether n̂ enters as a *direction* (even structure only) or as a *1-form* (odd structure available).

**The identification, which is the patch.** Tested where the time-asymmetry comes from: the reversal-**even** term produces max cycle affinity **exactly 0.0** at A = 0.3, 0.5 and 1.0 — zero at any magnitude — while the odd term violates on 420 of 1200 faces. So "costs more one way" ⟺ "detailed balance violated" ⟺ "not time-reversible". With MERGE-2 (sign(δ) is P-even, T-odd — an arrow, not a chirality), **the non-reciprocity IS the T-arrow**, already carried as W3.

He was looking for a spatial cause because the formula is written as a spatial quantity. There is none, because the asymmetry was never spatial. The geometry stays reciprocal; the *dynamics* do not, which is what an arrow of time means.

MERGE-2 and TARROW-2 each held half of this. His question is what joined them.
