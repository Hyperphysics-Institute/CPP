# reasoning-0949 (verbatim, at-patch) — L4-A rate-law form

**Lane:** chirality (09xx), Patch 0949, 13 Sep 2026. **Artifact:** `l4a_rate_law_form.md`. **Verify:** `code/0949_l4a_rate_law_form.py` (8/8).

Took this one on Fable because the founder asked, and because I had told him it was the one where a wrong answer propagates. The temptation was obvious from the start: L4-B and L4-C had gone well, and a clean "MA.1 is forced" would have lifted both arc verdicts. I want to record that I checked for that outcome and did not find it, and that the finding is better than the temptation.

First step was to ask what the two verdicts actually consume, because "discharge Mechanism A" is only meaningful relative to consumers. CHIR.md line 145 answered it: the NESS work (0694's π, 1100's μ²-sign) runs the Mechanism-A Markov process with MA.1's exact rates and finds the steady current at O(δ³). So some results use the rate law beyond first order. That fixed the shape of an honest answer before any computation: whatever representation theory forces must be split against what order each consumer works at.

The representation theory itself was clean. Directed edges, H₄-covariance, harmonics in n̂, Frobenius reciprocity → count stabiliser invariants. Arc-transitivity gives r₀ as one constant (commitment iii — genuinely derived, and trivially so; it was never a faith point, only stated as one). The directed-edge stabiliser is C₅v of order 10 with fixed subspace span{v, w} — I had expected exactly this from 0937's C₅v discussion, and the SVD confirmed dim 2. So the first-harmonic family is two-dimensional, not one: A m·n̂ + B ê·n̂. That was the moment the "MA.1 is forced" outcome died. What survived is sharper: the reversal-odd part is one-dimensional, and it is MA.1's form exactly.

Then the part that makes the result useful rather than deflating: the A-term cancels in the antisymmetric current at all 120 vertices for any A (T4), and α₁ = 6/φ² is untouched with A = 0.5 in (T4b). So everything at O(δ¹) — which is most of the arc — sees only B. But T5 shows A does not cancel in the detailed-balance ratio, so the NESS consumes A = 0. And T6 shows quadratic harmonics are available (Sym² invariants: dim 4), so "linear exact" is a truncation. Both residuals land on the same consumers: 0694, 1100, the O(δ³) current, TARROW-2's cross-check.

I deliberately did not claim V3 lifts. CAPACITY-1's conditionality is phrased around per-edge independence and pointwise non-degeneracy of η, and per-edge independence holds for the two-parameter family — so it is possible V3 consumes only the derived content. But possible is not shown, and I have not read 0927 in this window. Filed as a re-read for whoever holds it.

T7 was unplanned. Checking that Reading C's ε ê·n̂ is the same covariant led to the constant-speed map δ = −ε, which the paper says is "not pinned." The forms cannot be independent; the values might be. That is L4-E's question and I labelled it a lead.

Not registered as a theorem, though it is theorem-grade: single pass, no panel, and the registry numbering is a place to get bookkeeping wrong. Owed and filed. The gate will hold me to it.
