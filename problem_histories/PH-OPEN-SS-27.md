# PH-OPEN-SS-27 — Problem History

**Problem:** OPEN-SS-27 — D2 (K₃-edge coupling at host vertex) derivation via A6′ extension
**Status at time of this file:** OPEN (registered as paper-level conditional theorem in SS-8 v1.0; structural-derivation target deferred to a future paper, SS-9 candidate)
**Sector:** SS (nuclear physics)
**Location in registry:** `research_frontier.md` §1, Strong Sector (SS)
**File created:** 26 April 2026
**Purpose:** Record the extended narrative of OPEN-SS-27's registration during the SS-8 development cycle, the structural relationship to SS-7's per-edge $B_\text{pair}$ accounting, and the candidate derivation path via an A6′ extension framework.

---

## Why this file exists

OPEN-SS-27 was opened during the SS-8 H2′ derivation note work (21 April 2026) as one of three structural sub-problems needed to promote H2′ (the 2E/V alpha-vertex scaling law) from a layered hypothesis structure to a derived result. D2 is the middle of the three: D1 says *which* vertex the interstitial localizes at, D2 says *how* it couples to its surroundings once localized, and D3 says *how* the per-vertex calculation averages over the polytope. Of the three, D2 is the cleanest structural claim — it asserts that each K₃-contact face edge incident at the host vertex contributes binding strength $B_\text{pair}$, no more and no less — but its derivation requires extending axiom A6′ (SS-5's base-to-base K₃-reduced collective-mode framework) from a per-face statement to a per-edge statement that operates locally around each polytope vertex.

The structural picture is empirically supported across SS-7 and SS-8: SS-7's twelve-nucleus $3N_\alpha - 6$ formula assumes one $B_\text{pair}$ per polytope edge; SS-8's interstitial 2E/V law assumes the same per-edge accrual at each contact face incident at the host vertex. Both results work. The OPEN-SS-27 question is *why* this works — what CPP lattice-level dynamics make the per-edge $B_\text{pair}$ accounting structurally forced rather than empirically successful.

This file records the registration narrative and the candidate derivation path. It does not contain the derivation itself.

---

## Timeline

| Date | Event | Artefact |
|------|-------|----------|
| 21 April 2026 | OPEN-SS-27 opened in H2′ derivation note §10 alongside OPEN-SS-26 and OPEN-SS-28 | `series_strong/papers/SS-8/sketches/SS-8_H2prime_derivation_note.md` |
| 22 April 2026 | Round 2 review of D1 sketch (Models A/B) implicitly invokes D2 — Model A's K₃-edge counting depends on D2 holding. ChatGPT and Copilot Round 2 reviews flag D2 as the next derivation target if Model A is the path forward for closing OPEN-SS-26 Level-3. | `series_strong/papers/SS-8/reviews/round2_chatgpt_on_D1_sketch.md`, `round2_copilot_on_review_request.md` |
| 23 April 2026 | Formal `research_frontier.md` entry created for OPEN-SS-27 with priority MEDIUM-HIGH ("two-for-one — closure delivers D1 automatically via simplicial combinatorics under Model A") | `research_frontier.md` |
| 24 April 2026 | SS-8 v1.0 carries D2 as a paper-level structural hypothesis at proposition tier. Theorem `thm:h2prime` (the 2E/V scaling law, registered as THEO-SS-15 in `theorem-registry.md`) is conditional on D2 unchanged from this registration. | `series_strong/papers/SS-8/SS-8_interstitial_neutron_2EV_scaling.tex` |
| 26 April 2026 | OPEN-SS-27 paper reference cleaned to "SS-9 candidate (shares structural-polytope machinery with OPEN-SS-24)" per Session 1 high-priority registry update (patch 0027) | `research_frontier.md` |

---

## What we know now

**The empirical story across SS-7 and SS-8 supports D2 strongly but does not prove it.** SS-7's twelve-nucleus $3N_\alpha - 6$ alpha-chain formula achieves RMS 0.80% agreement with AME 2020 binding energies under the assumption of one $B_\text{pair}$ per polytope edge — that is, D2 in its SS-7 form. SS-8's interstitial 2E/V law extends the same per-edge accounting to interstitial-host coupling and reproduces ${}^{26}$Mg and ${}^{42}$Ca to under 1% with no additional parameters. The empirical agreement across two papers and 54 zero-parameter predictions (12 from SS-7 + 42 from SS-8) is strong circumstantial evidence that D2 is structurally correct. But none of this is a derivation.

**The candidate derivation path is an A6′ extension.** Axiom A6′ (CPP `axiom-registry.md`) currently establishes the K₃-reduced collective-mode framework at the SS-5 base-to-base nucleon-nucleon contact face. The framework has three structural elements that would need to be extended to the per-edge polytope setting:

1. **Local K₃ at each polytope edge.** SS-5's K₃ is the three-vertex graph of nucleon-nucleon pair connections at a single contact face. The polytope extension treats each edge of the alpha-polytope as carrying its own K₃ structure (the three pair-connections across the alpha-alpha contact face at that edge). Tile-correctness — that the local K₃ structures glue together consistently around each polytope vertex — is the first structural condition that must be verified.

2. **Eigenvalue replication.** SS-5's K₃ eigenvalue calculation produces the $1/\varphi$ factor that gives $B_\text{pair} = M_0/\varphi$. The polytope extension requires the same eigenvalue calculation to replicate at each edge of the alpha-polytope, producing the same $B_\text{pair}$ unrescaled. The Pattern 6 scale-recurrence observation (`axiom-registry.md`) supports this empirically; the structural condition is that the eigenvalue is a property of the K₃ graph, not of the physical scale at which K₃ is realized.

3. **Vertex-degree-dependent enhancement at D1 alpha-vertex sites.** When an interstitial neutron localizes at vertex $v$ (per D1), the contributions from the K₃-contact face edges incident at $v$ must add coherently to give $\deg_v \cdot B_\text{pair}$. The "coherent addition" piece is the third structural condition — there must be no destructive interference or higher-order coupling that prevents the per-edge contributions from summing to the predicted total.

A clean derivation would extend A6′ to deliver all three conditions simultaneously, possibly by treating the alpha-polytope as a graph with alpha-vertices and K₃-edge contacts and verifying that the SS-5 collective-mode structure tiles correctly over the polytope. This may require an explicit DP-sea redistribution calculation at polytope edges, which would relate the OPEN-SS-27 work to OPEN-SS-24 (simplicial connectivity from primitives) and OPEN-SS-25 (DP-sea Coulomb screening) methodologically.

**The two-for-one observation.** The Round 2 review consensus (ChatGPT, Copilot) was that closing OPEN-SS-27 would automatically deliver D1 under Model A — Model A's K₃-edge counting depends on D2 holding, so a derivation that produces D2 from primitives also produces Model A's prediction of D1. This makes OPEN-SS-27 a high-leverage closure target: one paper would convert two of the three SS-8 paper-level structural hypotheses (D1 under Model A, plus D2 itself) from proposition tier to derived theorem tier.

---

## Methodological observations

**The K₃ tiling condition is the load-bearing structural claim.** D2 stands or falls on whether the SS-5 K₃ collective-mode structure tiles consistently across an alpha-polytope's edge set. This is a graph-theoretic question with a definite answer for any specific polytope, and a structural answer for the simplicial 3-polytope class generally. A paper attacking OPEN-SS-27 should start by stating the tile-correctness condition explicitly and verifying it on the easiest cases (tetrahedron at $N_\alpha = 4$, octahedron at $N_\alpha = 6$) before scaling to the harder ones.

**The per-edge accounting is what makes SS-7's $3N_\alpha - 6$ formula and SS-8's 2E/V law structurally aligned.** SS-7 sums $B_\text{pair}$ over edges to get a polytope-level binding; SS-8 distributes the same per-edge contributions across vertex-incident face edges to get a per-neutron interstitial accrual. The structural alignment between these two accountings is built into D2's wording. A derivation of D2 would simultaneously verify that SS-7's per-edge sum and SS-8's per-vertex-incident sum are consistent rather than independent assumptions — strengthening both papers.

**OPEN-SS-27 is methodologically simpler than OPEN-SS-26 Level-3.** OPEN-SS-26 Level-3 is a question about *physical-principle independence* — can D1 be derived without invoking proximity-binding? — which has the structure of needing a constructive proof of existence (find a third model) or a no-go theorem. OPEN-SS-27 is a question about *structural compatibility* — does A6′ extend correctly to the per-edge setting? — which has the structure of a direct calculation that either succeeds or fails. The latter is more tractable.

---

## What's needed to close OPEN-SS-27

A paper would need to:

1. State the per-edge K₃ tile-correctness condition explicitly and verify it on at least three distinct alpha-polytope realizations covering the easy ($N_\alpha = 4$ tetrahedron), medium ($N_\alpha = 6$ octahedron), and harder-symmetry ($N_\alpha = 12$ icosahedron) cases.
2. Demonstrate that the SS-5 K₃ eigenvalue calculation replicates locally at each edge of these polytopes, producing $B_\text{pair} = M_0/\varphi$ unrescaled.
3. Show that the per-edge contributions add coherently (no destructive interference, no higher-order coupling shifts) at vertices to give $\deg_v \cdot B_\text{pair}$.
4. Either derive the extension as a corollary of A6′ as currently stated, or upgrade A6′ to A6″ (a per-edge formulation) and document the upgrade per axiom-registry.md procedure.
5. Update SS-7 and SS-8's THEO statuses: closure of OPEN-SS-27 would convert THEO-SS-15 (the 2E/V scaling law) from "conditional on D2" to "conditional on D1 + D3" (one fewer hypothesis), and would convert SS-7's per-edge $3N_\alpha - 6$ formula from empirical-anchor-supported to derived.

A paper closing OPEN-SS-27 would automatically also close most of OPEN-SS-26 (D1 under Model A becomes a theorem, leaving Model B redundant or supporting). This is the two-for-one observation noted in the Research Frontier registry.

---

## Cross-references

- `research_frontier.md` § OPEN-SS-27 — the formal registry entry
- `axiom-registry.md` — A6′ definition; Pattern 6 scale recurrence observation
- `theorem-registry.md` — THEO-SS-12 (Euler edges), THEO-SS-14 (D1 conditional), THEO-SS-15 (2E/V scaling) — all conditional on D2 in their current statements
- `series_strong/papers/SS-8/SS-8_interstitial_neutron_2EV_scaling.tex` v1.0 §3 — D2 statement and discussion
- `series_strong/papers/SS-7/SS-7_alpha_cluster_edge_formula.tex` v1.2 — the SS-7 per-edge accounting that SS-8's D2 inherits
- `problem_histories/PH-OPEN-SS-26.md` — sibling problem history; Models A/B for D1 both invoke D2-related machinery
- `future_projects.md` Project 0f — OPEN-SS-27 as SS-9 candidate (rank 4 of 7 by leverage; "two-for-one" with OPEN-SS-26)

---

*Problem history file maintained per `templates/research_frontier_architecture.md` problem-history format. Append new dated entries to the timeline as the problem evolves; do not retroactively edit prior entries.*
