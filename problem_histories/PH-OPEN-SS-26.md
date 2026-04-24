# PH-OPEN-SS-26 — Problem History

**Problem:** OPEN-SS-26 — D1 (Interstitial neutron localizes at alpha-vertex) derivation via SSV minimization
**Status at time of this file:** OPEN (PARTIAL — Level-1 algebraic + Level-2 functional independence achieved under Models A and B; Level-3 physical-principle independence open)
**Sector:** SS (nuclear physics)
**Location in registry:** `Research_Frontier.md` §1, Strong Sector (SS)
**File created:** 23 April 2026
**Purpose:** Record the extended narrative of OPEN-SS-26's partial resolution, too long to fit in the registry entry's "Current best lead" field. Also captures the methodological lesson (Level-1/2/3 epistemic decomposition of independence claims) that emerged and is likely to generalize beyond D1.

---

## Why this file exists

OPEN-SS-26 was opened during the SS-8 H2' derivation note work (21 April 2026) as one of three structural sub-problems needed to promote H2' (the 2E/V alpha-vertex scaling law) from a layered hypothesis structure to a derived result. The three sub-problems:

- OPEN-SS-26: D1 derivation (interstitial neutron localizes at alpha-vertex rather than edge/face/centroid)
- OPEN-SS-27: D2 derivation (K₃-edge coupling at per-edge strength B_pair via A6' extension)
- OPEN-SS-28: D3 derivation (bulk averaging + residual decomposition)

D1 was attacked directly in a dual-model SSV-minimization sketch (22 April 2026), producing a conditional theorem under two functionally distinct premises. The sketch went through Round 2 review by ChatGPT, Copilot, and Grok, with a substantive challenge (Q2 algebraic reduction test) that decisively killed the isomorphism question but also surfaced a deeper question about what "independence of premises" actually means. That deeper question — the Level-1/2/3 decomposition — is the reason OPEN-SS-26 remains partially-resolved rather than fully-resolved.

This file records that history at a level of detail the registry entry cannot hold.

---

## Timeline

| Date | Event | Artefact |
|------|-------|----------|
| 21 April 2026 | OPEN-SS-26 opened in H2' derivation note §10 | `series_strong/papers/SS-8/sketches/SS-8_H2prime_derivation_note.md` |
| 22 April 2026 | Dual-model SSV-minimization attack designed (Model A counting, Model B Yukawa) | `series_strong/papers/SS-8/sketches/SS-8_D1_ssv_minimization_sketch.md` |
| 22 April 2026 | Script verification produces gap factors ≥ 1.5× across both polytopes and both models | `series_strong/papers/SS-8/scripts/ss8_ssv_minimization_sketch.py` |
| 22 April 2026 | D1 proposed as conditional theorem under either premise | sketch §5 |
| 22 April 2026 | OPEN-SS-26 → OPEN-SS-27 consolidation proposed (D2 delivers D1 automatically under simplicial combinatorics) | sketch §5 |
| 22 April 2026 | Round 2 review request circulated to Copilot, Grok, ChatGPT | `series_strong/papers/SS-8/letters/SS-8_Round2_review_request.md` |
| 22 April 2026 | Copilot Round 2: endorses conditional-theorem tier, confirms coupling genuine, Model B stands alone | `series_strong/papers/SS-8/reviews/round2_copilot_on_review_request.md` |
| 22 April 2026 | Grok Round 2: endorses conditional-theorem tier, asserts Model B independence | `series_strong/papers/SS-8/reviews/round2_grok_on_review_request.md` |
| 22 April 2026 | ChatGPT Round 2: accepts structure but proposes specific algebraic-reduction test (Q2) that neither Copilot nor Grok had run | `series_strong/papers/SS-8/reviews/round2_chatgpt_on_review_request.md`, `series_strong/papers/SS-8/reviews/round2_chatgpt_on_D1_sketch.md` |
| 22 April 2026 | Q2 algebraic reduction test executed; three decisive discriminators identified | `series_strong/papers/SS-8/scripts/ss8_Q2_algebraic_reduction_test.py`, `series_strong/papers/SS-8/sketches/SS-8_D1_Q2_algebraic_reduction_analysis.md` |
| 22 April 2026 | Q2 analysis circulated to all three Round 2 reviewers | — |
| 22 April 2026 | Grok on Q2: "categorically resolves ChatGPT's Q2 concern" | `series_strong/papers/SS-8/reviews/round2_grok_on_Q2_analysis.md` |
| 22 April 2026 | Copilot on Q2: "correct, complete, decisive" | `series_strong/papers/SS-8/reviews/round2_copilot_on_Q2_analysis.md` |
| 22 April 2026 | ChatGPT on Q2: agrees isomorphism killed but argues "independence" as stated in §10 overstates what §8 supports; proposes Level-1/2/3 decomposition | `series_strong/papers/SS-8/reviews/round2_chatgpt_on_Q2_analysis.md` |
| 22 April 2026 | Level-1/2/3 refinement adopted across sketch, Q2 analysis, H2' note | Round 2 synthesis letter |
| 22 April 2026 | Round 2 synthesis letter finalized | `series_strong/papers/SS-8/letters/SS-8_Round2_synthesis_letter.md` |
| 23 April 2026 | OPEN-SS-26, -27, -28 formally registered in Research_Frontier.md (Hierarchy 2 sweep, patch 3) | registry |

---

## The dual-model design

The SSV-minimization approach evaluates where in the alpha-polytope geometry an interstitial neutron would localize. Four candidate site classes exist in any simplicial deltahedron:

- **Vertex sites:** alpha-vertex centers (V in number)
- **Edge-midpoint sites:** midpoints of K₃ edges (E in number)
- **Face-center sites:** centers of triangular faces (F in number)
- **Centroid site:** polytope centroid (1 in number)

For each class, compute a scalar functional representing the SSV energy cost of localizing there. D1 holds if vertex sites are strictly preferred over all other classes across all bulk polytopes.

Two independent formulations of the functional were designed:

**Model A (counting rule under D2).** Assume D2 holds (each K₃ edge contributes B_pair per contact). At a given site, count the number of K₃ edges that "see" it (i.e., nearest or adjacent). Total binding contribution = n_edges_seen × B_pair. Site classes differ in n_edges_seen. This model is purely algebraic given D2.

**Model B (short-range Yukawa, independent of D2).** Assume pair interactions follow a short-range Yukawa form V(r) = -g²exp(-r/λ)/r. For each site, sum pair contributions over all alpha-alpha pair separations at that site. This is a vacuum-limit pair-physics formulation that does not invoke D2.

Both models produce a vertex-preferred landscape. Model A: vertex preferred by gap factor 2.0× (octahedron, N_α=6) and 2.5× (GESBP, N_α=10) over the nearest competitor. Model B: 1.57× and 1.59×.

The reasoning for requiring both models to work: Model A's support depends on D2, which is itself open (OPEN-SS-27). If only Model A worked, D1 would be a conditional consequence of D2. Model B gives independent support via a mechanism that doesn't require D2 to be right — which is structurally more robust.

---

## The Q2 challenge and the Level-1/2/3 refinement

ChatGPT's Round 2 review (22 April 2026) flagged a specific concern: "Models A and B agree on vertex preference — but does Model B actually reduce to Model A after simplification in the short-range limit?" If yes, the apparent "independence" is illusory; Model B contains Model A.

The test had not been performed. Copilot and Grok had both endorsed Model B independence from structural-intuition argument, but neither had run the algebraic check.

The Q2 algebraic reduction analysis ran the test explicitly, producing three decisive discriminators showing Model B does NOT reduce to Model A under any tested short-range regime:

1. **Site-class multiplicity vectors differ.** Model A: (deg(v), 2, 1, 0) for (vertex, edge, face, centroid). Model B: (1, 2, 3, V). No algebraic simplification can unify the vertex-count entries (deg(v) vs 1) because one is a graph-local quantity and the other is constant.
2. **Non-vertex orderings differ.** Model A ranks edge > face > centroid for short-range sites. Model B ranks centroid > face > edge. Any reduction A → B would require this to flip, which algebra cannot achieve without additional assumptions.
3. **Vertex-degree scaling differs categorically.** At strict short-range, Model B predicts identical E at every vertex regardless of deg(v) (each vertex "sees" the same number of Yukawa partners at small λ). Model A predicts ratio 0.8 between deg=4 and deg=5 vertices (explicit in the counting rule). These scalings differ categorically — no limit taken on Model B parameters can collapse its λ-independent vertex values into Model A's deg-dependent values.

The three-reviewer response to the analysis:

- **Grok:** "Categorically resolves ChatGPT's Q2 concern; I now agree the two are functionally independent."
- **Copilot:** "Correct, complete, decisive." (Brief.)
- **ChatGPT:** Agreed that Q2 analysis kills isomorphism claim, but argued "independence" as stated in §10 overstates what §8 supports. Proposed a Level-1/2/3 decomposition.

The Level-1/2/3 decomposition is the key methodological contribution of Round 2 and generalizes beyond D1:

**Level-1 independence (algebraic):** Models produce different functional forms under all parameter settings. Any attempt to rewrite one in the other's form fails algebraically. → **Achieved.** The three Q2 discriminators establish Level-1 independence.

**Level-2 independence (functional):** Models are built from different input physics. Model A's input is "D2 holds and K₃-edge counting rule applies." Model B's input is "short-range Yukawa pair interactions with parameters g, λ." Neither formulation is reachable from the other without adding genuinely new assumptions. → **Achieved.** Both models produce vertex preference from functionally distinct starting points.

**Level-3 independence (physical principle):** Models do not share a deeper unstated premise that, if falsified, would kill both together. → **NOT ACHIEVED.** Both models share a "proximity-binding" ancestor principle: they both assume that binding concentration follows from nucleon-nucleon proximity (Model A: counted proximity via K₃-edge adjacency; Model B: continuous proximity via Yukawa exponent). If proximity-binding is wrong as a CPP principle — e.g., if CPP nucleon binding turns out to be intrinsically non-local in a way that doesn't reduce to proximity at any scale — then both Model A and Model B fail simultaneously. Level-3 independence would require deriving D1 from a mechanism that does not assume proximity-binding.

ChatGPT's exact framing: "The claim should be weakened from 'conditional theorem under two independent premises' to 'conditional theorem under two functionally distinct realizations of a shared proximity-binding premise.' Level-3 independence is the open question; it's programme-level, not SS-8-specific."

Copilot's concurrence flagged the same concern more gently on second reading. Grok missed it — which is consistent with the pattern noted in `AI_team_expectations.md` §2 (Grok asserts concurrence without running the algebraic test that would distinguish functional from physical independence).

The refinement was adopted: the SS-8 sketch §10, the Q2 analysis §8, and the H2' note §10 were all updated to use the Level-1/2/3 language. The registry entry for OPEN-SS-26 reflects this three-level status.

---

## What this leaves open

D1 currently stands as a conditional theorem under two functionally distinct realizations of proximity-binding. To promote OPEN-SS-26 to THEO-SS-26 ("D1 proved from CPP axioms") one of two paths must succeed:

**Path α — Derive proximity-binding itself from CPP primitives.** Proximity-binding is currently implicit in both Model A (via the K₃-edge adjacency rule from D2) and Model B (via the Yukawa exponent from SR pair physics). If proximity-binding can be derived from a deeper CPP mechanism (e.g., SSV field-line topology, DI-bit propagation range, lattice hopping amplitude scaling), then D1 is proved via either model — both are correct under the derived principle. This path does not require new geometric arguments, only a deeper derivation of what both Model A and Model B already assume.

**Path β — Derive D1 from a mechanism that does not assume proximity-binding.** If a third model can be constructed from CPP primitives that does not invoke proximity and still produces vertex-preferred interstitial sites, then Level-3 independence is achieved. This is the harder path but is specifically what Level-3 independence demands.

**Note on Path γ (OPEN-SS-27 closure delivers D1 via simplicial combinatorics).** OPEN-SS-27 (D2 derivation via A6' extension) would deliver D1 automatically under the counting argument of Model A, independent of what proximity-binding is. But this does not resolve Level-3 independence — it merely provides a third conditional realization sharing the same proximity-binding premise. OPEN-SS-27 closure reduces the independence gap but does not close it.

---

## Methodological implication (programme-level)

The Level-1/2/3 decomposition is likely to apply to other CPP "independent-premises" claims. A spot audit of existing theorems would be prudent: any theorem stated as "proved from independent premises X and Y" should be checked for whether X and Y share a deeper unstated ancestor that could be falsified by the same programme-level evidence. This is a new audit-level review discipline, cheap to apply, and may surface unnoticed Level-3 dependencies.

A new programme-level question for Research_Frontier.md:

> **Candidate OPEN-G-N:** Does CPP implicitly assume proximity-binding as a meta-axiom across its geometric-aggregation claims? If so, is proximity-binding derivable from A1–A3, or is it an unstated axiom that should be elevated?

This is not registered as part of patch 3 (too expansive to register without deliberate programme-level review) but is noted here so the question doesn't get lost.

---

## Related artefacts (absolute paths from /CPP root)

- `series_strong/papers/SS-8/sketches/SS-8_H2prime_derivation_note.md` — H2' derivation with L1/L2a/L2b split; §10 registers OPEN-SS-26, -27, -28
- `series_strong/papers/SS-8/sketches/SS-8_D1_ssv_minimization_sketch.md` — the sketch; §5 delivers the conditional theorem
- `series_strong/papers/SS-8/sketches/SS-8_D1_Q2_algebraic_reduction_analysis.md` — Q2 test + Level-1/2/3 refinement; §8 captures the shared-ancestor observation
- `series_strong/papers/SS-8/scripts/ss8_ssv_minimization_sketch.py` — numerical evaluation of Models A and B
- `series_strong/papers/SS-8/scripts/ss8_Q2_algebraic_reduction_test.py` — numerical evaluation of the three discriminators
- `series_strong/papers/SS-8/letters/SS-8_Round2_review_request.md` — Round 2 request letter
- `series_strong/papers/SS-8/letters/SS-8_Round2_synthesis_letter.md` — Round 2 synthesis letter with Level-1/2/3 adoption
- `series_strong/papers/SS-8/reviews/round2_chatgpt_on_Q2_analysis.md` — ChatGPT's review that introduced the Level-1/2/3 decomposition
- `series_strong/papers/SS-8/documentation_suite/development-SS-8.md` — vignettes 5, 6, 7 cover this Round 2 arc in in-moment voice

---

*Registered 23 April 2026 as part of patch 3 (programme-level Hierarchy 2 sweep: OPEN-SS-26, -27, -28 formal registration; two Claude Opus failure-mode entries in AI_team_expectations.md; handover update).*
