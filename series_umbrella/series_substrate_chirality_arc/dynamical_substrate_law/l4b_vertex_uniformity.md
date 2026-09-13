# 0940 — L4-B of OPEN-FP-F1-2: Mechanism A's vertex-uniformity derived from A11

**Lane:** chirality (09xx). **Patch:** 0940, 13 Sep 2026. **Layer:** 3 (structural derivation from A11 + the primitive n̂; publication-grade candidate, single pass, no panel). **Verify:** `dynamical_substrate_law/code/0940_l4b_vertex_uniformity.py` (7/7 — the 600-cell, its isometries, the vertex stabiliser, the n̂-shells and the MA.2 first-shell sum are all constructed from the lattice). **Reasoning fragment:** `documentation_suite/reasoning-0940.md`.

**Target.** L4-B of the OPEN-FP-F1-2 decomposition (Patch 0646): derive the vertex-uniformity of Mechanism A — that MA.1's `r(ê) = r₀(1 + δ ê·n̂)` carries the *same* `r₀` and `δ` at every substrate vertex, and MA.2's first-shell current construction has the same form at every vertex — from A11 (600-cell substrate), rather than taking it as framework input. F.1 §4.3 states vertex-independence as "operationally important" and assumes it; `frontier_sectors/FP.md` names L4-B "likely the cleanest publication-grade L3 artifact; no F.2."

**Result.** Vertex-uniformity holds, and the argument that establishes it is not the obvious one.

## 1. Why transitivity alone does not do it

The bare substrate is vertex-transitive: its isometry group has order 14400 and acts with a single orbit on the 120 vertices (T2 exhibits, for every vertex v, an explicit isometry carrying v_host to v; T3 confirms the stabiliser has order 120 = 14400/120, the local I_h of Reading C). So in the bare substrate no function of a vertex built from substrate structure alone can distinguish one vertex from another, and any v-dependence of r₀ or δ would be such a function.

But **Mechanism A does not live in the bare substrate.** It lives in (substrate, n̂), and fixing n̂ breaks the transitivity: the 120 vertices split into **nine shells** by the invariant v·n̂ ∈ {±1, ±φ/2, ±1/2, ±1/(2φ), 0}, with populations 1, 12, 20, 12, 30, 12, 20, 12, 1 (T4). A vertex-transitivity argument applied to (substrate, n̂) is therefore invalid as stated — the pair *does* distinguish vertices. This is the gap a one-line "A11 is vertex-transitive, QED" would have papered over.

## 2. The step that closes it

Under vertex-aligned Reading C the residual group is Stab(n̂) = Stab(v_host) ≅ H₃ = I_h, order 120. **Stab(n̂) acts transitively on each of the nine shells** (T5). Consequently every Stab(n̂)-invariant function of a vertex is a function of **v·n̂ alone** — the orbits of the residual group are exactly the level sets of that one invariant, so there is no finer invariant to carry a residual vertex label.

A vertex-dependence of `r₀` or `δ` would have to be precisely such a finer invariant: a Stab(n̂)-invariant function of v that is not a function of v·n̂. **No such function exists.** And v·n̂ is not a hidden channel — it is the quantity MA.1 already carries explicitly in its argument ê·n̂. Hence `r₀(v) ≡ r₀` and `δ(v) ≡ δ`: the parameters are constants, and all vertex dependence of the rate is the explicit, already-stated dependence on the edge direction's projection.

**Corollary for MA.2.** The first-shell multiset {ê·n̂} — the rate law's entire input at a vertex — is constant within each shell and distinct across all nine (T6), and the O(δ¹) current Σ ê (ê·n̂) at any vertex is the group image of its shell representative's (T7). So MA.2's construction has one form everywhere, with its *value* tracking the shell. That is the precise sense in which the construction is vertex-independent, and it is weaker than "the current is the same at every vertex" — which is false, and which F.1 §4.3's wording could be read as claiming.

## 3. Status and scope

- **L4-B discharged** at Layer 3 from A11 + the single primitive n̂ (FI-C-RC-1) + vertex-aligned Reading C (FI-C-RC-2). No appeal to Mechanism A itself, so the argument is not circular; no F.2; no new axiom.
- **It does not discharge Mechanism A.** MA.1's *form* (linearity in ê·n̂, a single scalar δ, no O(δ⁰) tangent term) is **L4-A**, open; MA.2's antisymmetric first-shell construction is **L4-C**, open; the δ–ε magnitude relation is **L4-E**, open. L4-D's chirality half is resolved (0647, MERGE-2, verdict M1-χ), its residual being the T-arrow (OPEN-CHIR-2a, W3). **The conditionality of V3/W3 on Mechanism A therefore stands unchanged** — it lifts only when L4-A and L4-C land too.
- **Wording correction owed to F.1** (paper-level, not a number): §4.3's "vertex-independence … for any host vertex, not just the chosen v_host" should state that the *construction* is vertex-independent while its *value* is shell-dependent, and should cite this derivation in place of the assumption. Exclusion-class entry E1 ("Mechanism A as framework axiom — not derived") narrows: the vertex-uniformity commitment is discharged; the rate-law form and the current construction are not.

**No verdict moves.** V3/W3 stand; THEO-CHIR-CAPACITY-1 untouched; no THEO/ID/prediction registered (a theorem-registry candidacy for L4-A+L4-B+L4-C jointly is the natural unit, not L4-B alone); header counts unchanged.
