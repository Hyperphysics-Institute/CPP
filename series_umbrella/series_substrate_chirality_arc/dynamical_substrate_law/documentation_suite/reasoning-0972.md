# reasoning-0972 (verbatim, captured late — see chirality_derivations/reasoning/0942.md header note; same provenance)

L4-E, expected small. The lead from 0949 was δ = −ε under constant-speed traversal, and the job looked like confirming it.

Read Reading C's formula properly before computing, and that is where it turned. `ℓ(ê) = ℓ₀(1 + ε ê·n̂)`, described as "edges acquire effective lengths". **But ê·n̂ is reversal-odd.** So the same edge gets two different lengths depending on traversal direction — 0.999691 one way, 1.000309 the other.

A length is a property of the undirected edge. A metric is a symmetric bilinear form. **A length cannot do this.** So Reading C's ℓ is not a length; it is a directed traversal cost, and the substrate it describes is non-reciprocal. The equation has said so since it was written; the prose has always said "length".

**The counterfactual is the finding, and I nearly did not run it.** Having confirmed δ = −ε I could have stopped. Instead asked: what if ℓ *were* a genuine reversal-even length, depending on the midpoint? Then `r = c/ℓ` is reversal-even and generates **the A-term, not δ** — measured A = −ε, δ = 0 exactly. **So MA.1's reversal-odd first harmonic cannot come from a metric length perturbation at all. Its form requires non-reciprocity.** That is stronger than the magnitude relation L4-E asked for.

**Bonus, and it bears on the residual carried since 0955:** the same expansion fixes the second-order coefficient at +ε²(ê·n̂)² — reversal-**even**. So the reversal-odd quadratic has **coefficient zero in the Reading-C realisation**. First positive statement about that channel rather than a bound. Did not over-claim it: absent in this realisation is not absent in all.

Two masking bugs hit along the way — division by zero on the equatorial edges where m·n̂ = 0, and again where ê·n̂ = 0. Masked rather than perturbed, since those edges are genuinely unperturbed rather than numerically awkward.
