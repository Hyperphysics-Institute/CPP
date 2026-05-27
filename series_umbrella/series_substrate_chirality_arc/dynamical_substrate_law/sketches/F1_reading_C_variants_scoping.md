# F.1 OPEN-FP-F1-5 — Non-Vertex-Aligned Reading C Variants Scoping

**Path:** `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/F1_reading_C_variants_scoping.md`
**Opened:** 27 May 2026 (Session 146 Patch 0595)
**Author:** Opus (Claude)
**Status:** Scoping at sketch level. NOT closure work. Opens the OPEN-FP-F1-5 trajectory as a multi-session arc; this document does not execute any closure work, does not propose framework extensions, does not modify the v1.0 SHIPPED F.1 paper or its hardened-theorem artifacts.
**Scope:** Articulate the edge-aligned ($D_3$ stabilizer) and face-aligned ($D_2$ stabilizer) Reading C closure trajectories as systematic replays of the just-completed vertex-aligned ($I_h$ stabilizer) Route C trajectory (Patches 0550 + 0551 + 0552 + 0571 + 0585 + 0587 + 0588 + 0589 + 0590 + 0591 + 0592). Identify the existing-theorem scaffolding that extends by stabilizer substitution; identify the geometric primitives needing variant-specific derivation; surface decision-gate items requiring Thomas input before substantive Layer 3 work begins. Predecessor template: `sketches/F1_o_delta_squared_extension_scoping.md` (Route C sequence 2 scoping, opened at Patch 0571i; closed COMPLETE at Patch 0592a).

---

## §0 Working-session firewall + anti-priorities

### §0.1 What this sketch IS

This document opens the **OPEN-FP-F1-5 trajectory** — the substantive multi-session physics arc that replays F.1's $\mathcal{O}(\delta^1)$ + $\mathcal{O}(\delta^2)$ substrate-locality structure under the two non-vertex-aligned Reading C variants identified in Capotauro v2.0 §2.3 and Patch 0419 Finding C-W37. The scope is:

- Inventory the existing-theorem scaffolding (THEO-DSL-1 through THEO-DSL-5; G1, G2, G2.1, G2.3, G2.4; perpendicularity + projection identities) and identify which extends by stabilizer substitution and which needs variant-specific replay;
- Articulate the stabilizer-structural differences ($I_h$ vs $D_3$ vs $D_2$) at the load-bearing argument levels;
- Surface the THEO-DSL-4 Lemma 2 extension question (does the parallel-to-$\hat{n}$ structural result survive under $D_3$ and $D_2$?);
- Propose a Sequence-1 (symmetry-only structural) + Sequence-2 (geometric primitives + path-class enumeration) trajectory structure for each variant;
- Identify decision-gate items requiring Thomas input;
- Register a risk inventory including the substantive outcome possibilities (full survival / partial survival / vertex-aligned-uniqueness).

The scope is **scoping at sketch level**, NOT closure work. Each substantive theorem and each geometric primitive is its own gated sub-trajectory; this document enumerates them but does not execute any of them.

### §0.2 Anti-priorities sustained at this Patch

Per the cumulative Patch 0571a–0571h + 0585 + 0587–0592 + 0592a discipline + the OPEN-FP-F1-5 scoping window, the following are NOT triggered by this Patch:

1. **NO Layer 3 closure work in this Patch** — this is the scoping document. Each variant-specific geometric identity is a separate gated sub-trajectory.
2. **NO modification of v1.0 SHIPPED F.1 paper sources** — `dynamical_substrate_law.tex` and `dynamical_substrate_law.pdf` are frozen at v1.0 SHIPPED per Patch 0570 + §17.8 immutable-checkpoint discipline. Variant-Reading-C extensions live in this sketch (and subsequent OPEN-FP-F1-5 trajectory Patches) until a future v1.1 or v2.0 micro-revision integrates them.
3. **NO modification of hardened-theorem artifacts** — Patches 0550 + 0551 + 0552 + 0571 + 0585 + 0587 + 0588 + 0589 + 0590 + 0591 + 0592 are frozen. Variant-Reading-C artifacts will be NEW `.tex` files under `hardened_theorems/` at future Patches.
4. **NO modification of F.1's five programme-level theorems** (THEO-DSL-1 + THEO-DSL-2 + THEO-DSL-3 + THEO-DSL-4 + THEO-DSL-5 (candidate) in `theorem-registry.md` SD section). New variant-Reading-C theorems would be registered as THEO-DSL-6 + THEO-DSL-7 + ... at future Patches when they reach publication-grade Layer 3 rigor.
5. **NO modification of OPEN-FP-F1-1 closure status** — OPEN-FP-F1-1 is CLOSED at sketch-document Layer 3 under (H1)–(H5) at Patch 0592 / 0592a. The OPEN-FP-F1-5 trajectory operates orthogonally to F1-1's vertex-aligned scope.
6. **NO reopening of OPEN-FP-F1-1 publication-grade hardening** — that is priority queue item (G) per Session 145 close handover; the OPEN-FP-F1-5 trajectory is independent and does not pre-empt (G).
7. **NO conflation of edge-aligned + face-aligned variants into single substantive Patch** — each variant has its own stabilizer structure ($D_3$ vs $D_2$) and its own geometric-primitive analogs; each is a separate gated sub-trajectory under the F1-5 umbrella.
8. **NO new Open Problem registrations** at programme level in this Patch — the parent Open Problem OPEN-FP-F1-5 is already registered; sub-questions surfaced here are scoping-internal until they crystallize into separately-trackable closure sub-targets.
9. **NO reviewer engagement** on this scoping Patch — Layer 3 scoping Patches do not require external review per `templates/operating_system.md` §17 codified discipline (external reviewers engage at v0.9 → v1.0 SHIP cycles, not at scoping stages).
10. **NO F.2 / F.3 substantive content trajectory opening** — DEFERRED per `manifestation_inventory.md` (manifestations iii and v remain open with no current closure-trajectory machinery; F.2 / F.3 territory is independent of OPEN-FP-F1-5 work).

### §0.3 What this sketch IS NOT

- It is NOT a non-vertex-aligned derivation. The derivations are multi-session substantive physics work; this document scopes that work.
- It is NOT a framework-extension proposal. The framework axioms MA.1 + MA.2 carry over without modification across Reading C variants per their stabilizer-independent statement.
- It is NOT a commitment to closure routes. Stabilizer-specific decisions surfaced as decision-gate items (§8).
- It is NOT a paper-assembly document. OPEN-FP-F1-5 closure (when it lands at sketch-document Layer 3 or publication-grade Layer 3) will eventually integrate into F.1 v1.1 / v2.0 or a dedicated companion paper; the sketch does not prefigure paper assembly.

---

## §1 Purpose and structure

### §1.1 Why scope this trajectory now

OPEN-FP-F1-5 was registered as one of five in-body Open Problems at F.1 v1.0 SHIP (Patch 0570, 24 May 2026). Per FP.md, it is independent of OPEN-FP-F1-1 ($\mathcal{O}(\delta^2)$ extension, CLOSED at Patch 0592 under (H1)–(H5)), OPEN-FP-F1-2 (Layer 4 derivation, long-term programme target), and OPEN-FP-F1-3 (G1 hardening, RESOLVED at Patch 0571). After the F1-1 Route C trajectory closure at Session 145, OPEN-FP-F1-5 is the natural continuation of the substrate-locality programme: with the vertex-aligned variant fully developed across 11 hardened-theorem artifacts, the question "do edge-aligned and face-aligned variants share the same substrate-locality structure?" is the next forward-derivation question.

Reasons OPEN-FP-F1-5 is the right next substantive physics target:

- **Maximum scaffolding density.** The just-completed Route C trajectory provides the entire proof template (THEO-DSL-1 perturbation-locality, THEO-DSL-2 first-shell geometric identities, THEO-DSL-3 substrate-locality umbrella, THEO-DSL-4 symmetry-only structural theorem, THEO-DSL-5 (candidate) closed-form coefficient) plus the hardened-theorem artifact sequence (Patches 0550–0592). The replay-under-alternative-stabilizers structure is well-defined.
- **Stabilizer-substitution is a well-posed group-theoretic question.** $I_h$ at vertex, $D_3$ at edge midpoint, $D_2$ at face centroid (per FP.md line 230). Each is a well-characterized point group; replay of the symmetry-only Lemma 2 argument is mechanical.
- **Substantive new content possible.** The parallel-to-$\hat{n}$ structural result depends on the stabilizer subgroup containing an element acting as inversion on the perpendicular complement (or equivalently, on the perpendicular complement decomposing trivially under the stabilizer's action). For $I_h$, the central inversion $\iota$ provides this; for $D_3$ and $D_2$, the question is more delicate — preliminary group-theoretic analysis (§4) suggests survival but the structural verification is the substantive content of Sequence 1 under each variant.
- **Clean falsifiability story.** If parallel-to-$\hat{n}$ fails for edge-aligned or face-aligned Reading C, that's a substantive negative result establishing vertex-aligned Reading C as uniquely selected — which would substantively strengthen Capotauro's Q1' resolution per Finding C-W37.
- **Cross-paper relevance.** Reading C three-variant framing was opened in Capotauro v2.0 §2.3; OPEN-FI-C-9-FP-MECHANISM was closed at vertex-aligned via Q1' resolution (Patch 0419 Finding C-W37). F1-5 closure complements that by establishing the substrate-direction primitive's manifestation structure across all three Reading C variants.

### §1.2 What "scoping at sketch level" means here

Per the Route C trajectory precedent, the OPEN-FP-F1-5 trajectory budget is estimated at:

- **Sequence 1 (symmetry-only structural theorem)** under each variant: ~1–2 sessions each (per Patch 0585's 1-session closure of vertex-aligned Sequence 1) × 2 variants = **2–4 sessions**
- **Sequence 2 (geometric primitives + path-class enumeration)** under each variant: ~6 Patches each (per Patches 0587–0592's 6-Patch closure of vertex-aligned Sequence 2) × 2 variants = ~12 Patches; conservatively ~**2–4 sessions** at the Session 145 single-artifact-per-Patch discipline

Total trajectory budget: **4–8 sessions** for both variants closed at sketch-document Layer 3 under analogs of (H1)–(H5).

This scoping document opens the trajectory in 1 Patch (this Patch 0595) and identifies the sub-trajectories. The substantive closure work happens at subsequent Patches, gated per the single-artifact-per-Patch pattern.

### §1.3 Document structure ahead

- §2 — Reading C three-variant framing recap.
- §3 — Scaffolding inventory: what extends, what needs replay.
- §4 — Stabilizer analysis: $I_h$ vs $D_3$ vs $D_2$ at the load-bearing argument level.
- §5 — Hypothesis inheritance: which of (H1)–(H5) extend across variants.
- §6 — Sequence 1: symmetry-only structural theorem under $D_3$ and $D_2$.
- §7 — Sequence 2: geometric primitives + path-class enumeration under $D_3$ and $D_2$.
- §8 — Decision-gate items requiring Thomas input.
- §9 — Risk register.
- §10 — Session-close discipline + forward queue.

---

## §2 Reading C three-variant framing recap

### §2.1 The three variants per Capotauro v2.0 §2.3

The substrate-direction primitive $\hat{n}$ is a 4D unit vector at the host vertex. Capotauro v2.0 §2.3 and Patch 0419 Finding C-W37 identify three Reading C variants distinguished by the geometric structure $\hat{n}$ aligns with at the 600-cell vertex $v_{\text{host}}$:

| Variant | Direction of $\hat{n}$ | Residual symmetry at host | Status |
|---|---|---|---|
| **Vertex-aligned** | $\hat{n} = v_{\text{host}} / \|v_{\text{host}}\|$ (radial direction at host vertex) | $H_3 = I_h$ (icosahedral; order 120; contains central inversion $\iota$) | DEVELOPED: F.1 v1.0 §3–§7 + Route C trajectory Patches 0550–0592 |
| **Edge-aligned** | $\hat{n}$ along a 600-cell short-edge direction emanating from $v_{\text{host}}$ | $D_3$ at edge midpoint (per FP.md line 230); order 6 | OPEN: this trajectory's Sequence A |
| **Face-aligned** | $\hat{n}$ perpendicular to a triangular face of the 600-cell incident to $v_{\text{host}}$ | $D_2$ at face centroid (per FP.md line 230); order 4 | OPEN: this trajectory's Sequence B |

The vertex-aligned variant was selected at Q1$'$+Q1$'$.A resolution in Capotauro v2.0 (Patch 0419 Finding C-W37) by three converging arguments. The selection determines the substrate-direction primitive's preferred manifestation at the substrate level; OPEN-FP-F1-5 asks what the substrate-locality structure looks like under the rejected alternatives.

### §2.2 Why the variant question matters at F.1 level

Capotauro v2.0's selection was at the spatial-sector chirality content level. F.1 v1.0's substrate-locality umbrella theorem (Theorem 7.1) is at the temporal-sector DI-bit current level. The same substrate-direction primitive $\hat{n}$ feeds both sectors via the universal cage-shell averaging factor at the 600-cell first-shell. The question "do the alternative Reading C variants produce different substrate-locality structures?" is substantively orthogonal at F.1 level — it's a question about the temporal-sector behavior independent of the spatial-sector chirality argument that selected vertex-aligned at Capotauro.

Three a priori possible outcomes per FP.md OPEN-FP-F1-5 "What a solution looks like" framing:

- **Full survival**: substrate-locality structure (parallel-to-$\hat{n}$ at first order + closed-form coefficient at second order) holds under all three variants with variant-specific values for the structural constants ($6/\phi^2$ at vertex; ??? at edge; ??? at face)
- **Partial survival**: structural sub-question survives (parallel-to-$\hat{n}$) but coefficient sub-question takes a different form (e.g., non-zero tangent component, or no closed form, or different sign pattern)
- **Structural failure**: parallel-to-$\hat{n}$ component fails for one or both alternative variants, e.g., a non-parallel-to-$\hat{n}$ component appears at first order; this would substantively strengthen Capotauro's vertex-aligned uniqueness selection

The OPEN-FP-F1-5 trajectory's substantive content is to determine which outcome obtains.

### §2.3 Independence from OPEN-FP-F1-1 (H5) qualifier

OPEN-FP-F1-1's closure under (H1)–(H5) carries the (H5) load-bearing scope qualifier on path-class weight ansatz $W(P) = 1$. This qualifier is *vertex-aligned-Reading-C-specific* in its current formulation. OPEN-FP-F1-5 would need either its own (H5) analog (specifying path-class weights under $D_3$ and $D_2$) at sketch-document Layer 3, or a publication-grade-Layer 3 path-integral construction that derives the path-class weights from substrate dynamics. The trajectory inherits (H5)'s anti-priorities (downstream consumers MUST cite scope qualifier; publication-grade promotion via DG-1-style sub-options A/B/C is independent) at the variant-Reading-C level.

---

## §3 Scaffolding inventory

The existing F.1 theorem stack and hardened-theorem artifacts split into three categories with respect to OPEN-FP-F1-5 extension:

### §3.1 Theorems extending by stabilizer substitution (mechanical replay)

These theorems have proofs that depend on the residual symmetry group abstractly but not on its specific identification as $I_h$; replay under $D_3$ or $D_2$ is mechanical group-theoretic substitution:

| Theorem | Original artifact | What carries over |
|---|---|---|
| **THEO-DSL-1** (perturbation-locality propagation) | `perturbation_locality_propagation.tex` (Patch 0550) | Full theorem statement and proof; depends only on Mechanism A first-order edge structure (MA.1 + MA.2), not on residual symmetry. **Extends UNCHANGED to edge-aligned and face-aligned Reading C.** |
| **Corollary 6.2** (Shell-locality at $\mathcal{O}(\delta^1)$) | Inherits from THEO-DSL-1 | Same as THEO-DSL-1. **Extends UNCHANGED.** |
| **THEO-DSL-4** (parallel-to-$\hat{n}$ structural theorem at all orders $k \geq 1$) | `second_order_parallel_to_n_structural.tex` (Patch 0585) | Lemma 1 ($I_h$-equivariance under stabilizer of $\hat{n}$) → ($D_3$-equivariance) or ($D_2$-equivariance); same proof structure with stabilizer substitution. Lemma 2 (invariant vectors spanned by $\hat{n}$) → see §4 for the critical group-theoretic verification under $D_3$ and $D_2$. **Extends MODIFIED:** stabilizer-substituted Lemma 1 + Lemma 2 verification at §4. |

### §3.2 Theorems requiring geometric replay (variant-specific primitives)

These theorems depend on variant-specific geometric structure that must be rederived for $D_3$ and $D_2$:

| Theorem | Original artifact | What needs replay |
|---|---|---|
| **THEO-DSL-2** (first-shell geometric identities) parts (a) + (b) | `host_first_shell_uniform_projection.tex` (Patch 0552) + `first_shell_perpendicularity.tex` (Patch 0551) | Part (a) uniform projection $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ across 12 first-shell vertices — depends on $H_3 = I_h$ acting transitively on the icosahedron of first-shell vertices. Under edge-aligned $D_3$, the first shell decomposes into multiple $D_3$ orbits with non-uniform projection values; under face-aligned $D_2$, similar orbit decomposition. Part (b) first-shell-to-first-shell edge perpendicularity $\hat{e}_{ij} \cdot \hat{n} = 0$ — depends on the icosahedron lying in a 3-plane perpendicular to $\hat{n}$ in 4D; this 3-plane structure is vertex-aligned-specific. **Replay needed under $D_3$ and $D_2$.** |
| **THEO-DSL-3** (substrate-locality umbrella at $\mathcal{O}(\delta^1)$) | Assembly in F.1 §7.2 (not independently hardened) | Inherits from THEO-DSL-2; replay needed once THEO-DSL-2 analogs are derived under $D_3$ and $D_2$. |
| **THEO-DSL-5 (candidate)** (closed-form $\alpha_2 = -9/\phi^2$) parts | `o_delta_squared_path_class_weights.tex` (Patch 0591) + `o_delta_squared_substrate_locality_umbrella.tex` (Patch 0592) | The path-class enumeration B.1–B.4 (round-trip / first-shell-trans / cross-shell / third-shell) inherits its enumeration framework but per-class projection values are vertex-specific. Per-vertex sum $S(u_i) = -3$ is a $I_h$-specific golden-ratio algebra result. Icosahedral sum $-6/\phi$ is $I_h$-specific. **Full replay needed under $D_3$ and $D_2$ with variant-specific closed-form coefficients.** |

### §3.3 Geometric primitives requiring variant-specific derivation

These are the geometric primitives at the 600-cell level. Under vertex-aligned Reading C, they are publication-grade Layer 3 unconditional (after Patches 0571 + 0587–0590). Under edge-aligned and face-aligned, they require fresh derivation:

| Primitive | Vertex-aligned artifact | Edge-aligned analog | Face-aligned analog |
|---|---|---|---|
| **G1**: first-shell inner-product primitive | `first_shell_inner_product_primitive.tex` (Patch 0571) | Edge-aligned first-shell analog: inner-product structure of vertices in first shell of edge midpoint under $D_3$ | Face-aligned first-shell analog under $D_2$ |
| **G2**: second-shell inner-product primitive | `second_shell_inner_product_primitive.tex` (Patch 0587) | Edge-aligned second-shell analog under $D_3$ | Face-aligned second-shell analog under $D_2$ |
| **G2.1**: host-to-second-shell uniform projection | `host_second_shell_uniform_projection.tex` (Patch 0588) | Edge-aligned analog (may not be uniform under $D_3$) | Face-aligned analog (may not be uniform under $D_2$) |
| **G2.3**: first-shell-to-second-shell edge orbits | `first_shell_second_shell_edge_orbits.tex` (Patch 0590) | Edge-aligned orbit decomposition under $D_3$ | Face-aligned orbit decomposition under $D_2$ |
| **G2.4**: second-shell-to-second-shell perpendicularity | `second_shell_perpendicularity.tex` (Patch 0589) | Edge-aligned analog (may not be perpendicular under $D_3$) | Face-aligned analog (may not be perpendicular under $D_2$) |
| **G3**: third-shell inner-product primitive | Sketch-document Layer 3 (Coxeter 1973 polytope-theoretic) | Same inheritance under $D_3$ | Same inheritance under $D_2$ |

### §3.4 Framework axioms inheriting unchanged

| Framework axiom | Statement | Extension to variants |
|---|---|---|
| **MA.1** (Mechanism A propagation-rate asymmetry) | $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$ | **Unchanged** — $\hat{n}$ direction varies by variant but the form of $r(\hat{e})$ is variant-independent |
| **MA.2** (framework-local current construction) | $\vec{j}^{\text{net}}(v) = \sum_{w \sim v}(r_{v,w} - r_{w,v})\hat{e}_{vw}$ | **Unchanged** — sum structure is variant-independent |
| **(H1)** vertex-aligned Reading C identification | $\hat{n} = v_{\text{host}}$ | **REPLACED** by variant-specific (H1$_E$): $\hat{n}$ along short-edge direction; (H1$_F$): $\hat{n}$ perpendicular to triangular face |
| **(H2)** 600-cell unit-vertex normalisation | $|v_{\text{host}}| = 1$ | **Unchanged** at edge-aligned; **adapted** at face-aligned (face centroid not on unit sphere) |
| **(H3)** icosahedral residual symmetry $H_3 = I_h$ | $I_h$ stabilizer at $v_{\text{host}}$ | **REPLACED** by variant-specific (H3$_E$): $D_3$ at edge midpoint; (H3$_F$): $D_2$ at face centroid |
| **(H4)** F.1 Theorem 6.1 perturbation-locality | Shell-locality of $\vec{j}_{DI}$ to edges in $E_k(v_{\text{host}})$ | **Unchanged** — Theorem 6.1 holds variant-independently per THEO-DSL-1 |
| **(H5)** Mechanism A path-integral extension at $\mathcal{O}(\delta^k)$ | $W(P) = 1$ for $P \in \mathcal{P}_2(v_{\text{host}})$ | **REPLACED** by variant-specific (H5$_E$) and (H5$_F$) at sketch-document Layer 3; same per-variant scope qualifier discipline as F1-1 closure |

### §3.5 What this inventory implies

The OPEN-FP-F1-5 trajectory cost is dominated by the geometric-replay components of §3.2 + §3.3. Sequence 1 (symmetry-only structural theorem) under each variant is short — it's mostly the Lemma 1+2 replay of THEO-DSL-4 with stabilizer substitution. Sequence 2 (closed-form coefficient) under each variant is the major effort — it requires the full 6-Patch hardened-theorem sequence analog of Patches 0587–0592, but with variant-specific group theory and chord-length computations.

---

## §4 Stabilizer analysis: $I_h$ vs $D_3$ vs $D_2$ at the load-bearing argument level

The critical question for Sequence 1 (symmetry-only structural theorem) is whether the THEO-DSL-4 Lemma 2 argument extends to $D_3$ and $D_2$. Lemma 2 establishes that the $I_h$-invariant subspace of $\mathbb{R}^4$ at $v_{\text{host}}$ is $\mathbb{R}\hat{n}$. Two equivalent arguments exist in the Patch 0585 hardened artifact:

- **Inversion argument** (main proof): the central inversion $\iota \in I_h$ acts as $\text{diag}(1, -1, -1, -1)$ on the $\mathbb{R}\hat{n} \oplus T_{v_{\text{host}}} S^3$ decomposition, forcing any $I_h$-fixed vector $\vec{w} = a\hat{n} + \vec{w}_\perp$ to satisfy $\vec{w}_\perp = -\vec{w}_\perp$, hence $\vec{w}_\perp = \vec{0}$.
- **Schur's lemma alternative** (Remark 3.6): the 3D standard representation of $I_h$ on $T_{v_{\text{host}}} S^3$ is irreducible (one of the two 3D irreps $T_{1g}$ or $T_{1u}$ of $I_h$), so by Schur's lemma the trivial 1-dimensional representation occurs in $\mathbb{R}^4$ with multiplicity 1 at the $\mathbb{R}\hat{n}$ summand.

For the variants, the question becomes: does the stabilizer subgroup have *only* the trivial 1-dimensional representation acting non-trivially on the $\mathbb{R}\hat{n}$ summand (with no further trivial-rep components in the perpendicular complement)?

### §4.1 $D_3$ stabilizer (edge-aligned case)

$D_3$ is the dihedral group of order 6: three rotations ($e$, $C_3$, $C_3^2$) about the principal axis and three reflections ($\sigma_v^{(1)}, \sigma_v^{(2)}, \sigma_v^{(3)}$) through planes containing the principal axis. $D_3 \cong S_3$.

**Inversion argument check**: $D_3$ does NOT contain the inversion $\iota = -I$ as an element. The principal axis ($\hat{n}$) is preserved by rotations and the perpendicular plane is rotated by $C_3$ angles. Reflections preserve $\hat{n}$ and flip a single line in the perpendicular plane. So the inversion argument from Patch 0585 does NOT directly extend.

**Schur's lemma alternative check**: $D_3$ acts on the 3D perpendicular complement $T_{v_{\text{midpt}}} S^3$ of $\hat{n}$ at the edge midpoint. Note that "perpendicular complement" here is 3D in the 4D ambient space; not all 3 dimensions are in the $D_3$-rotation plane. Decompose: one direction along the edge (parallel to $\hat{n}$) which is excluded; one 2D plane perpendicular to $\hat{n}$ in the 3D space tangent at the edge midpoint; and the fourth 4D direction perpendicular to both $\hat{n}$ and the edge's 3D ambient — wait, the edge midpoint is in 4D; the tangent space at the edge midpoint to the 3-sphere through $v_{\text{host}}$ is 3D. Let me re-state: $T_{v_{\text{midpt}}} S^3 = \mathbb{R}^3$, and $\hat{n}$ is along the edge direction within this 3D tangent space. $D_3$ acts on this 3D tangent space with the edge direction as the principal axis.

So $D_3$ acts on the 2D perpendicular complement of $\hat{n}$ within $T_{v_{\text{midpt}}} S^3$ as the standard 2D representation of $D_3$ (which is irreducible — the "$E$" irrep of $S_3$). By Schur's lemma, the trivial representation appears in $\mathbb{R}^4$ at $v_{\text{midpt}}$ with multiplicity 1: the $\mathbb{R}\hat{n}$ component.

But wait — $\mathbb{R}^4$ at the edge midpoint also has the radial direction (toward the 4-sphere center). That's a separate dimension. Let me re-decompose: in the 4D ambient space $\mathbb{R}^4$, the tangent space to $S^3$ at the edge midpoint is 3D. The remaining 1D direction (radial to the polytope center) is fixed by all stabilizer elements. So the $D_3$-action on $\mathbb{R}^4$ decomposes into: 1D radial (trivial rep) + 1D along-edge (trivial rep, since $D_3$ preserves the edge direction) + 2D perpendicular (the "$E$" irrep of $D_3$, irreducible).

So the trivial rep appears with multiplicity 2 in $\mathbb{R}^4$ at the edge midpoint: the radial direction AND the along-edge direction $\hat{n}$.

**Conclusion**: $D_3$-invariant vectors form a 2D subspace, not 1D. This means the THEO-DSL-4 analog under $D_3$ states $\vec{j}_k(v_{\text{midpt}}) \in \text{span}\{\hat{n}_{\text{radial}}, \hat{n}_{\text{edge}}\}$ — a 2D plane, not a 1D line.

This is a **substantive structural difference** from the vertex-aligned case. The substrate current at the edge midpoint at $\mathcal{O}(\delta^k)$ has both an along-edge component (the "parallel to $\hat{n}$" analog) AND a radial component. The single-direction parallel-to-$\hat{n}$ structure fails under edge-aligned Reading C.

⚠️ **This is a finding worth surfacing at Sequence 1 closure** — but its interpretation depends on whether the radial component is independently constrained to vanish by some other consideration (e.g., by the boundary condition that the substrate current at a non-host vertex has no radial contribution; needs careful re-examination of the framework).

### §4.2 $D_2$ stabilizer (face-aligned case)

$D_2$ is the Klein four-group, order 4: identity $e$, three order-2 rotations $C_2^{(1)}, C_2^{(2)}, C_2^{(3)}$ about three mutually perpendicular axes. $D_2 \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.

**Inversion argument check**: $D_2$ does not contain the 4D inversion $\iota = -I$, but the product $C_2^{(1)} C_2^{(2)} C_2^{(3)}$ equals the 3D inversion on the 3-perpendicular-to-the-principal-axis structure. The specifics depend on which axes are stabilized.

**Schur's lemma alternative check**: $D_2$ has four 1-dimensional irreducible representations (the trivial rep $A$ and three sign reps $B_1, B_2, B_3$). On $\mathbb{R}^4$ at the face centroid, $D_2$ acts as: 1D radial (trivial) + 1D along-$\hat{n}$ (trivial, since $\hat{n}$ is perpendicular to the face which is preserved) + 2D in the face plane (some decomposition).

The 2D in-face decomposition under $D_2$: depends on how $D_2$ acts on the face. If $D_2$ is the stabilizer of the triangular face that fixes the centroid and acts non-trivially on the 3 vertices, then... wait, $D_2$ has order 4 and a triangular face has 3 vertices; $D_2$ can permute 3 vertices only as identity + three 2-vertex swaps (but $D_2$ has only three non-identity order-2 elements, so each swaps two vertices and fixes one). This gives a 3-element permutation representation, which decomposes as trivial + 2D irrep. The 2D irrep of $D_2$ — but $D_2$ has no 2D irreps; all its irreps are 1D!

So the 2D in-face decomposition under $D_2$ must decompose as a sum of two 1D irreps, not as a single 2D irrep. This means the trivial rep MIGHT appear in the 2D in-face decomposition with multiplicity 0 or 1, depending on the specific $D_2$ action.

⚠️ **The exact $D_2$ identification needs verification**. The FP.md statement "residual $D_2$ symmetry at face centroid" may correspond to a specific subgroup of $H_4$ (e.g., $D_{2h}$ with inversion, or $C_{2v}$, or $D_2$ proper). The stabilizer of a face in $H_4$ is typically larger than $D_2$ if we include all symmetries fixing the face centroid; the $D_2$ may be a specific subgroup that also fixes a chosen $\hat{n}$ direction.

⚠️ **Pre-emptive risk**: if $D_2$ is the rotational stabilizer only and includes a non-trivial trivial-rep component in the face plane, then the $D_2$-invariant subspace of $\mathbb{R}^4$ is even larger than 2D — the parallel-to-$\hat{n}$ structure may fail at face-aligned in a substantively different way than at edge-aligned.

### §4.3 Implications for Sequence 1

The Sequence 1 substantive content under each variant is more interesting than the vertex-aligned case because the structural conclusion is **not** simply "parallel to $\hat{n}$ analogously." For each variant, the substantive Sequence 1 theorem states:

- **Edge-aligned**: $\vec{j}_k(v_{\text{midpt}})$ lies in the 2D subspace spanned by the radial direction $\hat{n}_{\text{rad}}$ and the along-edge direction $\hat{n}_{\text{edge}}$.
- **Face-aligned**: $\vec{j}_k(v_{\text{ctr}})$ lies in a 1D, 2D, or 3D subspace depending on the precise $D_2$ identification.

The Sequence 1 closure under each variant is therefore a *substantive structural finding* rather than a routine replay. The closure may also surface the additional question of whether the radial / non-along-$\hat{n}$ components vanish by some independent consideration (e.g., framework-axiom-level constraints from MA.1 + MA.2 that go beyond stabilizer-symmetry).

This is the kind of substantive content that distinguishes OPEN-FP-F1-5 from being a pure mechanical replay; it has its own physics content.

---

## §5 Hypothesis inheritance: which of (H1)–(H5) extend across variants

Per §3.4, the framework axioms split as:

- **Variant-independent**: MA.1, MA.2, (H2) (with face-aligned adaptation), (H4).
- **Variant-specific**: (H1), (H3), (H5).

The variant-specific replacements:

| Hypothesis | Vertex-aligned (current F1-1) | Edge-aligned (Sequence A) | Face-aligned (Sequence B) |
|---|---|---|---|
| (H1) | $\hat{n} = v_{\text{host}}$ | (H1$_E$): $\hat{n}$ along a 600-cell short-edge direction; host = edge midpoint | (H1$_F$): $\hat{n}$ perpendicular to a 600-cell triangular face; host = face centroid |
| (H3) | $I_h$ residual symmetry at $v_{\text{host}}$ | (H3$_E$): $D_3$ residual symmetry at edge midpoint | (H3$_F$): $D_2$ residual symmetry at face centroid |
| (H5) | $W(P) = 1$ for $P \in \mathcal{P}_2(v_{\text{host}})$ in 600-cell edge graph | (H5$_E$): $W(P) = 1$ for $P \in \mathcal{P}_2(v_{\text{midpt}})$ in appropriate graph extension | (H5$_F$): $W(P) = 1$ for $P \in \mathcal{P}_2(v_{\text{ctr}})$ in appropriate graph extension |

⚠️ **(H2) adaptation at face-aligned**: in vertex-aligned and edge-aligned cases, $|v_{\text{host}}| = 1$ (vertex on unit sphere) or $|v_{\text{midpt}}| = $ some explicit golden-ratio value derivable from polytope structure. The face centroid is NOT on the unit sphere; its distance from the origin depends on the face structure. This adaptation is mechanical but needs to be made explicit at the Sequence-2 substantive Patch.

⚠️ **(H5) graph-extension at edge-aligned and face-aligned**: the substrate-current path-class enumeration in F1-1 was set up on the 600-cell vertex graph; at edge midpoint or face centroid, the "graph" is a modified graph where the "host" is no longer a vertex. The path-class structure $\mathcal{P}_2(v_{\text{midpt}})$ or $\mathcal{P}_2(v_{\text{ctr}})$ needs a specific definition: directed 2-edge paths from the host emanating through nearest substrate vertices. This is a scoping refinement to address at Sequence-2 substantive Patch.

---

## §6 Sequence 1 — Symmetry-only structural theorem under $D_3$ and $D_2$

### §6.1 Sequence 1A (edge-aligned, $D_3$)

**Target**: hardened-theorem artifact analogous to Patch 0585's `second_order_parallel_to_n_structural.tex`, under (H1$_E$) + (H2) + (H3$_E$) + (H4) + (H5$_E$).

**Result**: $\vec{j}_k(v_{\text{midpt}})$ lies in the 2D $D_3$-invariant subspace of $\mathbb{R}^4$ at the edge midpoint, spanned by $\{\hat{n}_{\text{rad}}, \hat{n}_{\text{edge}}\}$.

**Proof architecture**:
- Lemma 1 ($D_3$-invariance): per Patch 0585 Lemma 1 template, established via three-step argument: (i) $D_3$-equivariance of MA.1 + MA.2 under stabilization of $\hat{n}_{\text{edge}}$; (ii) $D_3$-permutation of the path set $\mathcal{P}_k$; (iii) $O(4)$-equivariance of edge-direction vectors.
- Lemma 2 ($D_3$-invariant subspace identification): §4.1 analysis — $D_3$-invariant vectors form a 2D subspace; identification of the two trivial-rep components (radial + along-edge).
- Main proof: Lemma 1 forces $\vec{j}_k$ into the $D_3$-invariant subspace; Lemma 2 identifies that subspace.

**Estimated effort**: 1 Patch (analogous to Patch 0585's 1-session closure of vertex-aligned Sequence 1).

**Layer rigor target**: publication-grade Layer 3 unconditional for the structural sub-question (no (H5$_E$) dependency at Sequence 1).

**Substantive content beyond mechanical replay**: the 2D-invariant-subspace finding is a *different* structural conclusion from the vertex-aligned 1D result. This is the substantive content of Sequence 1A.

### §6.2 Sequence 1B (face-aligned, $D_2$)

**Target**: hardened-theorem artifact under (H1$_F$) + (H2) (adapted) + (H3$_F$) + (H4) + (H5$_F$).

**Result**: $\vec{j}_k(v_{\text{ctr}})$ lies in the $D_2$-invariant subspace of $\mathbb{R}^4$ at the face centroid — dimension to be determined per §4.2 analysis (likely 2D or 3D).

**Proof architecture**: same template as Sequence 1A with $D_2$ substituted for $D_3$.

**Estimated effort**: 1 Patch (analogous to Patch 0585), but with additional §4.2 verification step that may require an extra Patch if the $D_2$ identification is ambiguous.

**Layer rigor target**: publication-grade Layer 3 unconditional for the structural sub-question (no (H5$_F$) dependency at Sequence 1).

**Substantive content**: dimension of the $D_2$-invariant subspace and identification of which directions span it. The structural-failure outcome (parallel-to-$\hat{n}$ fails categorically at face-aligned) would be a major finding establishing vertex-aligned uniqueness more strongly.

### §6.3 Sequence 1 combined risk register

- ⚠️ The §4.1 finding that $D_3$-invariant vectors form a 2D subspace (radial + along-edge) is preliminary; needs verification at the Sequence 1A substantive Patch with full $H_4$-stabilizer-of-edge-midpoint analysis. If the exact stabilizer at edge midpoint in $H_4$ is larger than $D_3$ (e.g., $D_{3d}$ with inversion), the conclusion may change.
- ⚠️ The §4.2 analysis of $D_2$ at face centroid is preliminary; the exact identification of $D_2$ as a subgroup of $H_4$ needs verification.
- ⚠️ Both variants may have additional radial-direction constraints from framework-level considerations (the substrate current at a non-vertex location may have intrinsic radial-vanishing properties); this is a substantive question for the Sequence 1 closure.

---

## §7 Sequence 2 — Geometric primitives + path-class enumeration under $D_3$ and $D_2$

### §7.1 Sequence 2A (edge-aligned, $D_3$) — geometric primitives

Six-Patch sequence analogous to Patches 0587–0592:

| Patch | Target |
|---|---|
| 2A.1 | Edge-aligned analog of G2 (second-shell inner-product primitive at edge midpoint) — what is the "second shell" at edge midpoint? Likely a $D_3$-orbit decomposition of nearby 600-cell vertices |
| 2A.2 | Edge-aligned analog of G2.1 (host-to-second-shell projection) — may be non-uniform under $D_3$, with multiple projection values across $D_3$-orbits |
| 2A.3 | Edge-aligned analog of G2.4 (second-shell-to-second-shell edge perpendicularity) — may not be perpendicular |
| 2A.4 | Edge-aligned analog of G2.3 (first-shell-to-second-shell edge orbit classification) — likely multiple orbits under $D_3$ |
| 2A.5 | Edge-aligned path-class enumeration at $\mathcal{O}(\delta^2)$ producing closed-form $\alpha_2^E$ (variant-specific) |
| 2A.6 | Umbrella registration of THEO-DSL-6 (candidate) at sketch-document Layer 3 under (H1$_E$)–(H5$_E$) |

**Estimated effort**: 6 Patches in 1–2 sessions (parallel to Patches 0587–0592 single-artifact-per-Patch discipline).

**Layer rigor target**: 4–5 of 6 Patches at publication-grade Layer 3 unconditional (geometric primitives); 1–2 Patches at sketch-document Layer 3 under (H5$_E$).

### §7.2 Sequence 2B (face-aligned, $D_2$) — geometric primitives

Six-Patch sequence analogous to Sequence 2A with $D_2$ substituted. Note that under $D_2$, the orbit decomposition is more granular (more orbits, smaller orbits) than under $D_3$, so the per-orbit projection values are more numerous; the path-class enumeration may have more classes.

**Estimated effort**: 6–8 Patches in 1–2 sessions (slightly larger budget than Sequence 2A due to more granular orbits).

### §7.3 Combined Sequence 2 substantive content

The closed-form coefficients $\alpha_2^E$ (edge-aligned) and $\alpha_2^F$ (face-aligned) are the primary substantive outputs of the OPEN-FP-F1-5 trajectory. Their values, signs, and magnitudes relative to the vertex-aligned $\alpha_2 = -9/\phi^2 \approx -3.438$ are the substantive content.

A priori expectations: by analogy with the vertex-aligned three-factor structure $\alpha_2 = (-1/(2\phi)) \cdot (-3) \cdot (-6/\phi) = -9/\phi^2$, the variant-specific coefficients should factor similarly into (projection factor at first shell) × (per-vertex sum) × (orbit-summation factor at $D_3$/$D_2$), but the per-factor values differ.

**Falsifier**: if either $\alpha_2^E$ or $\alpha_2^F$ does not admit a closed form within the golden-ratio extension of $\mathbb{Q}$, that would substantively distinguish vertex-aligned as the unique "clean" Reading C variant.

**Cross-sector cross-check**: cross-sector parallelism with the Capotauro v2.0 spatial-sector at non-vertex-aligned Reading C variants. If Capotauro's spatial-sector closed-form pattern survives only at vertex-aligned, that would converge with F.1's temporal-sector finding to establish vertex-aligned uniqueness across both sectors.

---

## §8 Decision-gate items requiring Thomas input

Before substantive Sequence 1A work begins (the first physics Patch of the OPEN-FP-F1-5 trajectory), the following decisions need Thomas input:

### §8.1 DG-F15-1: Variant ordering

Three options:

- **(A) Edge-aligned first (Sequence 1A → 2A → 1B → 2B)** — default. Edge-aligned $D_3$ is the smaller-symmetry-breaking step from $I_h$; sequence completion would inform face-aligned scope.
- **(B) Face-aligned first (Sequence 1B → 2B → 1A → 2A)** — face-aligned is the most aggressive symmetry-breaking step; could surface vertex-aligned uniqueness fastest if face-aligned exhibits structural failure.
- **(C) Both Sequence-1s before either Sequence-2 (Sequence 1A → 1B → 2A → 2B)** — front-load the structural findings; if either Sequence-1 surfaces a structural failure or surprising 2D/3D invariant subspace finding, that informs the Sequence-2 scope decision.

**Default recommendation: (C)** — front-loading both structural findings minimizes downstream rework if a structural surprise emerges. Sequence 1A + 1B closure is estimated 2 Patches in 1–2 sessions; Sequence 2A + 2B closure is 12+ Patches in 2–4 sessions.

### §8.2 DG-F15-2: Exact stabilizer identification

Two options for resolving the §4 stabilizer ambiguities:

- **(A) Compute exact stabilizers from first principles** at edge midpoint and face centroid in $H_4$ via explicit subgroup analysis (Coxeter group character tables; polytope-theoretic stabilizer computation). Estimated 0.5 Patch — falls naturally into Sequence 1A's preamble.
- **(B) Adopt FP.md's stated stabilizers ($D_3$ at edge, $D_2$ at face) as given** and verify within Sequence 1 substantive Patches. Lighter weight but risks surfacing a discrepancy late in the trajectory.

**Default recommendation: (A)** — front-load the exact stabilizer identification as a preamble Patch (or merge into Sequence 1A's substantive Patch). This avoids the §4 preliminary uncertainty and ensures the §4.1 finding ($D_3$-invariant subspace is 2D) is rigorously confirmed before Sequence 1A's main theorem.

### §8.3 DG-F15-3: Scope of the trajectory at session-budget level

Two options:

- **(A) Full trajectory (Sequence 1A + 1B + 2A + 2B)** — closure under both variants at sketch-document Layer 3 under (H5$_E$, H5$_F$); estimated 4–8 sessions total.
- **(B) Sequence 1 only (Sequence 1A + 1B)** — structural sub-question closure under both variants at publication-grade Layer 3 unconditional; coefficient sub-question deferred to future trajectory. Estimated 1–2 sessions. Treats the substantive structural-content findings (the §4.1 2D-invariant-subspace finding under $D_3$, plus the analog under $D_2$) as the primary deliverable, and defers the heavier coefficient work.

**Default recommendation: depends on outcome of Sequence 1A**. If the Sequence 1A structural finding is a clean 2D-invariant-subspace result (radial + along-edge) with the radial component identifiable as vanishing by independent framework-axiom-level argument, then proceed to Sequence 2A naturally. If the Sequence 1A finding is structurally surprising (e.g., radial component cannot be ruled out), pause and reassess whether Sequence 2A is well-posed before continuing.

### §8.4 DG-F15-4: Hypothesis qualifier discipline

The (H5$_E$) and (H5$_F$) path-class weight ansatze are variant-specific scope qualifiers at sketch-document Layer 3, analogous to (H5) for F1-1. Two options:

- **(A) Use (H5$_E$) and (H5$_F$) directly** with the same per-variant ansatz $W(P) = 1$ as F1-1's (H5).
- **(B) Generalize (H5) to a stabilizer-independent ansatz** that specializes to (H5$_E$), (H5$_F$), and the original (H5) under stabilizer substitution. This would simplify cross-variant consistency arguments.

**Default recommendation: (A)** — preserve per-variant scope qualifiers per F1-1's anti-erasure discipline. The (H5)/(H5$_E$)/(H5$_F$) trio remains explicit; downstream consumers cite the variant-specific qualifier per the F1-1 convention.

### §8.5 DG-F15-5: Theorem-registry naming

THEO-DSL-6 and THEO-DSL-7 candidates would register the edge-aligned and face-aligned structural and coefficient theorems. Two options:

- **(A) Four separate theorems**: THEO-DSL-6 (edge-aligned structural, Sequence 1A); THEO-DSL-7 (edge-aligned coefficient, Sequence 2A candidate); THEO-DSL-8 (face-aligned structural, Sequence 1B); THEO-DSL-9 (face-aligned coefficient, Sequence 2B candidate). Mirrors the F1-1 THEO-DSL-4 + THEO-DSL-5 (candidate) pattern.
- **(B) Two composite theorems**: THEO-DSL-6 (edge-aligned structural + coefficient, Sequence 1A + 2A bundled); THEO-DSL-7 (face-aligned structural + coefficient, Sequence 1B + 2B bundled). Lighter on registry growth but conflates structural (publication-grade) and coefficient (sketch-document under H5) rigor levels.

**Default recommendation: (A)** — preserve the THEO-DSL-4 (structural) vs THEO-DSL-5 (candidate, coefficient) rigor-level distinction across both variants. Each variant gets two theorem entries, mirroring F1-1's pattern.

---

## §9 Risk register

### §9.1 Substantive risks

- **R1: Structural failure at edge-aligned** — Sequence 1A may surface that $D_3$-invariant subspace is 2D (radial + along-edge) and the radial component is not independently constrained to vanish. In this case, the parallel-to-$\hat{n}$ structure fails at edge-aligned in a substantive sense; the OPEN-FP-F1-5 closure would be at a different structural form than vertex-aligned. *Mitigation*: surface clearly at Sequence 1A close; do not paper over the difference.
- **R2: Stabilizer identification ambiguity** — FP.md states $D_3$ at edge and $D_2$ at face, but exact identifications in $H_4$ may differ. *Mitigation*: DG-F15-2 default recommendation (front-load exact identification).
- **R3: (H5$_E$)/(H5$_F$) sketch-document scope qualifier propagation** — downstream consumers may drop variant-specific qualifiers if discipline lapses. *Mitigation*: DG-F15-4 default recommendation; per-variant qualifier discipline.
- **R4: Cross-sector consistency with Capotauro** — if Capotauro's vertex-aligned selection at Q1$'$+Q1$'$.A is independently re-verified by F1-5's findings (e.g., if face-aligned exhibits structural failure), this strengthens both papers' Reading C framings. Conversely, if F1-5 surfaces a substantive Capotauro-relevant finding at non-vertex-aligned variants, that may warrant Capotauro v2.1 / v3.0 update consideration. *Mitigation*: cross-sector finding inventory at trajectory close.

### §9.2 Workflow risks

- **R5: Trajectory-budget creep** — variant-specific group theory may surface unexpected complications (e.g., $D_2$ identification ambiguities). *Mitigation*: single-artifact-per-Patch discipline per F1-1's 100% compliance precedent; trajectory-budget reset gates at Sequence-1 close.
- **R6: Documentation discipline** — five F-line theorems (THEO-DSL-1 through DSL-5 candidate) already in registry; adding four more (THEO-DSL-6 through DSL-9 candidate) brings F-line total to 9. Anti-priorities-sustainment discipline at each registration. *Mitigation*: standard F1-1 anti-erasure pattern applies.

### §9.3 Substantive-outcome risks (none material — these are research findings, not workflow problems)

- The substantive risk that the closed-form coefficient $\alpha_2^E$ or $\alpha_2^F$ has a non-golden-ratio component would be a substantive *finding* about the framework, not a workflow problem.
- The substantive risk that the radial component of $\vec{j}_k(v_{\text{midpt}})$ does not vanish independently would be a substantive *finding* requiring framework-level analysis.

---

## §10 Session-close discipline + forward queue

### §10.1 What this Patch lands

This Patch (0595) lands the OPEN-FP-F1-5 scoping document at `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/F1_reading_C_variants_scoping.md`. The Patch is a single new file; no modifications to other repository artifacts.

### §10.2 What this Patch does NOT land

- No theorem registrations
- No new geometric primitives
- No paper modifications
- No FP.md status updates
- No registry-propagation Patch (no Patch 0595a needed because no theorem inventory has changed)

### §10.3 Forward queue post-Patch 0595

The decision-gate items (§8) are surfaced for Thomas review at Session 146 close or Session 147 open. After Thomas's accept on:

- DG-F15-1 variant ordering (default (C))
- DG-F15-2 stabilizer identification approach (default (A))
- DG-F15-3 trajectory scope at session-budget level (depends on Sequence 1A outcome)
- DG-F15-4 (H5$_E$)/(H5$_F$) qualifier discipline (default (A))
- DG-F15-5 theorem-registry naming (default (A))

The next substantive Patch opens Sequence 1A (or Sequence 1B per DG-F15-1) with the exact stabilizer identification preamble + structural theorem main proof. Target: 1 Patch per Sequence-1 closure, mirroring Patch 0585's 1-session vertex-aligned Sequence-1 closure pattern.

### §10.4 Patch landings record

- **Patch 0595** (Session 146, 27 May 2026): **scoping document LANDED**. `sketches/F1_reading_C_variants_scoping.md` (this file). Opens the OPEN-FP-F1-5 trajectory at sketch level. Enumerates the scaffolding inheritance from F1-1 Route C; identifies $D_3$ and $D_2$ stabilizer questions; surfaces the §4.1 finding that $D_3$-invariant subspace at edge midpoint is 2D (radial + along-edge) — a substantive structural difference from vertex-aligned; surfaces the §4.2 question about $D_2$ exact identification; registers five decision-gate items DG-F15-1 through DG-F15-5 for Thomas review.

---

*Scoping document opened at Patch 0595 (27 May 2026, Session 146). Discipline references `templates/operating_system.md` §15.10 + `templates/paper_completion_checklist.md` §H + `templates/relationship_protocol.md` §2.6 (symmetric-honesty for stabilizer-substitution trade-off framing). Template precedent: `sketches/F1_o_delta_squared_extension_scoping.md` (Route C sequence 2 scoping; opened at Patch 0571i, closed COMPLETE at Patch 0592a). Trajectory peer references: Capotauro v2.0 §2.3 (Reading C three-variant framing); Patch 0419 Finding C-W37 (vertex-aligned selection); FP.md OPEN-FP-F1-5 entry (lines 226–237).*
