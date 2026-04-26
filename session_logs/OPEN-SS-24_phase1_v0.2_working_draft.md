# SS-9 Working Draft v0.2 — Conditional C4 Closure (Phase 1 + Phase 3 combined)

**Status:** Working draft, exploratory. Iteration target: tight Lemma A + Lemma B + Theorem statement, with honest scope notes on the convex-deltahedra gap at N_α ∈ {11, 13, 14}.
**Working in:** /home/claude/ss9_work/ (sandbox; not pushed)

---

## §1. Setup and notation

Let $N_\alpha \in \mathbb{N}$ with $N_\alpha \geq 3$. An *N_α-alpha cluster configuration* is a tuple $\mathcal{C} = (\alpha_1, \ldots, \alpha_{N_\alpha})$ of distinct rigid regular tetrahedra in $\mathbb{R}^3$ ("alphas"), each with edge length $L_\alpha$ (the SS-5-derived alpha-internal scale).

By **C1** (alpha rigidity, inherited from SS-7), each $\alpha_i$ is a closed regular 3-simplex with four congruent equilateral triangular faces. The shape of $\alpha_i$ is invariant under all interactions relevant at the alpha-cluster scale.

By **C2** (base-to-base contact, inherited from SS-7), the *contact relation* $\sim$ on $\{\alpha_1, \ldots, \alpha_{N_\alpha}\}$ is defined: $\alpha_i \sim \alpha_j$ iff there exist faces $F_i \subset \alpha_i$ and $F_j \subset \alpha_j$ such that $F_i \equiv F_j$ as triangular regions of $\mathbb{R}^3$.

Define:
- The **contact graph** $G(\mathcal{C}) = (V, E)$ with $V = \{\alpha_1, \ldots, \alpha_{N_\alpha}\}$ and $E = \{\{\alpha_i, \alpha_j\} : \alpha_i \sim \alpha_j\}$.
- The **alpha-polytope realization** $P(\mathcal{C})$: the geometric realization in $\mathbb{R}^3$ with vertices at alpha centroids $c_i$ and edges as straight segments between $c_i, c_j$ for each $\{\alpha_i, \alpha_j\} \in E$.
- The **binding energy** $B(\mathcal{C}) = N_\alpha B_\alpha + |E| B_\text{pair}$, per SS-7's central formula, with $B_\alpha = 28.296$ MeV (SS-5/AME inherited) and $B_\text{pair} = M_0/\varphi = 2.342$ MeV (SS-5 inherited via C3).

By **C3** (K₃ collective mode at each contact, inherited from SS-7), each contact $\alpha_i \sim \alpha_j$ contributes a single K₃ collective bonding mode at energy $B_\text{pair}$, justifying the $|E| B_\text{pair}$ term.

We introduce two new paper-level hypotheses required for the conditional closure:

**C5 (ground-state energy minimization).** Among all alpha-cluster configurations $\mathcal{C}$ with $N_\alpha$ alphas that are physically realizable (no alpha-alpha interpenetration; all alphas connected through the contact graph), the realized ground-state configuration is one that minimizes total energy, equivalently maximizes binding $B(\mathcal{C})$.

**C6 (cluster surface-realization).** The alpha centroids of the ground-state configuration all lie on the boundary of the convex hull $\text{conv}(c_1, \ldots, c_{N_\alpha})$. Equivalently: no alpha is "interior" to the cluster.

Both C5 and C6 are paper-level structural hypotheses at the SS-7 inheritance tier. Their derivation from programme-level axioms A1–A11 is not attempted in this paper and is registered as new open problems (OPEN-SS-29 and OPEN-SS-30 candidates).

---

## §2. Lemma A: Pairwise triangular contact

**Lemma A.** *Under C1 and C2, for every $\{\alpha_i, \alpha_j\} \in E$, the contact face $F_{ij} = F_i \equiv F_j$ is an equilateral triangle of edge length $L_\alpha$.*

**Proof.** By C1, every face of $\alpha_i$ is an equilateral triangle of edge length $L_\alpha$ (regular tetrahedron property). By C2, $F_{ij}$ is the coincidence $F_i \equiv F_j$ as regions of $\mathbb{R}^3$. The intersection $F_i \cap F_j$ under full coincidence is exactly $F_i$ (and equally $F_j$), which is an equilateral triangle of edge length $L_\alpha$. $\square$

**Remark A.1.** Lemma A is essentially a definitional consequence of the rigidity and full-coincidence aspects of C1+C2. Its content is the *exclusion* of partial-overlap, edge-only, or vertex-only contact configurations as base-to-base contacts. These excluded configurations are not impossible geometrically, but C2 explicitly restricts the contact relation to face-to-face full-coincidence cases; non-face contacts do not realize the K₃ collective mode of C3 and therefore do not contribute $B_\text{pair}$ binding.

**Remark A.2 (why this matters).** Lemma A establishes that every edge of the contact graph $G$ corresponds to a triangular *contact face* between two alphas. This will be the input to Lemma B, where we argue that the geometric arrangement of these triangular contact faces forces planarity of $G$.

---

## §3. Lemma B: Convex 3-polytope realization

**Lemma B.** *Let $\mathcal{C}$ be an $N_\alpha$-alpha cluster configuration with $N_\alpha \geq 4$, satisfying C1, C2, C6, and "no alpha-alpha interpenetration" (rigid-packing constraint). Suppose further that $\mathcal{C}$ is **3D-non-degenerate**: the alpha centroids do not all lie in a single plane. Then the alpha-polytope realization $P(\mathcal{C})$ is a convex 3-polytope, and the contact graph $G(\mathcal{C})$ is the 1-skeleton of $P(\mathcal{C})$. By Steinitz's theorem, $G(\mathcal{C})$ is planar and 3-vertex-connected.*

**Proof.**

*Convex polytope realization.* By C6, all alpha centroids $c_i$ lie on the boundary of the convex hull $H = \text{conv}(c_1, \ldots, c_{N_\alpha})$. Combined with 3D-non-degeneracy, $H$ is a 3-dimensional convex polytope with vertex set exactly $\{c_1, \ldots, c_{N_\alpha}\}$. The alpha-polytope realization $P(\mathcal{C}) = H$ as a point set.

*Contact graph as 1-skeleton.* We need to show that each edge of $G(\mathcal{C})$ corresponds to an edge of $H$, and conversely. 

Forward direction: Suppose $\alpha_i \sim \alpha_j$ in $G(\mathcal{C})$. By C2, the contact face $F_{ij}$ is shared between $\alpha_i$ and $\alpha_j$. The centroids $c_i, c_j$ lie on opposite sides of $F_{ij}$ (one inside each tetrahedron, equidistant from the shared face). The line segment $\overline{c_i c_j}$ passes through the interior of $F_{ij}$. By rigid-packing, no other alpha $\alpha_k$ ($k \neq i, j$) can occupy any region traversed by $\overline{c_i c_j}$, since such occupation would require interpenetration with either $\alpha_i$ or $\alpha_j$ near $F_{ij}$. So $\overline{c_i c_j}$ is a chord of $H$ that does not intersect any other tetrahedron. Furthermore, the contact face $F_{ij}$ lies on the surface of $H$ (it is part of the outer boundary of the cluster), so the segment $\overline{c_i c_j}$ either lies on the surface of $H$ (if no other $c_k$ is closer along $\overline{c_i c_j}$'s projection) or is an internal chord.

[GAP: This argument is incomplete. I need to show specifically that $\overline{c_i c_j}$ is an *edge* of $H$ — i.e., that it is part of the 1-skeleton of $H$, not an internal diagonal. The cleanest argument may be: (i) the segment $\overline{c_i c_j}$ lies entirely in the closed convex hull of two adjacent tetrahedra (since they share the face $F_{ij}$), (ii) this two-tetrahedron region is on the boundary of $H$ where it is not occluded by other alphas, (iii) by the local geometry near the shared face, $c_i$ and $c_j$ are connected by an edge of $H$. This needs sharpening — particularly the case where many alphas surround the $\alpha_i$-$\alpha_j$ pair. Defer to v0.3.]

Reverse direction: Suppose $c_i$ and $c_j$ are connected by an edge of $H$. Then the segment $\overline{c_i c_j}$ lies on the surface of $H$. In particular, $c_i$ and $c_j$ are visible to each other along this segment without any intervening $\alpha_k$. The closest-approach geometry of two non-interpenetrating rigid tetrahedra with centroids on a common surface segment has them in face-contact (by C1 and rigid-packing). So $\alpha_i \sim \alpha_j$.

[GAP: The reverse direction also needs sharpening — specifically the claim that "closest-approach with centroids on common surface segment" forces face-contact rather than edge- or vertex-contact. Edge- and vertex-contacts are excluded by C2, but C2 is about which contacts realize $\sim$, not about which geometrically occur. This needs the additional argument that *only* face-to-face contact is energetically selected (which is C5 + C3 working together: face contact gives $-B_\text{pair}$; edge or vertex contacts give zero contribution; ground state selects face-contact configurations).]

*By Steinitz's theorem* (Steinitz 1922, as in Ziegler "Lectures on Polytopes" Theorem 4.1): A graph $G$ is the 1-skeleton (vertex-edge graph) of a convex 3-polytope iff $G$ is simple, planar, and 3-vertex-connected. Therefore $G(\mathcal{C})$, being the 1-skeleton of $P(\mathcal{C})$, is planar and 3-vertex-connected.

$\square$

**Remark B.1 (status of Lemma B).** Lemma B has two argumentative gaps in this v0.2 draft, both flagged above. Both are about the bidirectional correspondence between alpha-alpha contacts (graph edges) and convex-hull edges (geometric edges). The forward direction needs a clean argument that $\overline{c_i c_j}$ is on the convex hull surface, not internal. The reverse direction needs a clean argument that geometric proximity forces face-contact (not just any contact), which is where C5 enters implicitly. **These gaps are real and need to be closed before SS-9 ships.**

---

## §4. Lemma C: Energy minimization picks max edges

**Lemma C.** *Under C3 and C5, the ground-state contact graph $G(\mathcal{C}_\text{ground})$ has the maximum possible $|E|$ among all physically realizable contact graphs on $N_\alpha$ vertices satisfying Lemma B's hypotheses.*

**Proof.** By the SS-7 binding formula and C3, $B(\mathcal{C}) = N_\alpha B_\alpha + |E(\mathcal{C})| B_\text{pair}$. Since $B_\text{pair} > 0$, $B$ is strictly monotone increasing in $|E|$ at fixed $N_\alpha$. By C5, the ground state minimizes energy (equivalently, maximizes binding $B$), so the ground state has maximum $|E|$. $\square$

---

## §5. Main Theorem

**Theorem (Conditional C4).** *Let $\mathcal{C}$ be the ground-state alpha-cluster configuration of $N_\alpha \in \{4, 5, 6, 7, 8, 9, 10, 12\}$ alphas, under C1–C3 (inherited from SS-7), C5 (ground-state energy minimization), C6 (cluster surface-realization), and 3D-non-degeneracy. Then:*

*(i) $G(\mathcal{C})$ is the 1-skeleton of a convex simplicial 3-polytope.*

*(ii) $|E(\mathcal{C})| = 3 N_\alpha - 6$.*

*(iii) Every face of the alpha-polytope $P(\mathcal{C})$ is a triangle.*

*Furthermore, for $N_\alpha \in \{4, 5, 6, 7, 8, 9, 10, 12\}$, $P(\mathcal{C})$ is realized as a convex deltahedron (a convex polytope with all faces equilateral triangles of edge length $R_{\alpha\alpha}$, the alpha-alpha contact distance set by C2 + C3).*

**Proof.**

By Lemma B, $G(\mathcal{C})$ is the 1-skeleton of a convex 3-polytope $P(\mathcal{C})$, and is planar and 3-vertex-connected.

For any convex 3-polytope $P$ with vertex set $V$, edge set $E$, and face set $F$, Euler's formula $|V| - |E| + |F| = 2$ holds. Each face of $P$ has at least 3 edges (since faces of convex polytopes are at least triangles), and each edge is shared by exactly 2 faces. So $\sum_{f \in F} |\partial f| = 2|E|$, with $|\partial f| \geq 3$ for each face. Hence $3|F| \leq 2|E|$, i.e., $|F| \leq 2|E|/3$.

Substituting into Euler's formula: $|V| - |E| + |F| = 2 \Rightarrow |V| - |E| + 2|E|/3 \geq 2 \Rightarrow |V| - |E|/3 \geq 2 \Rightarrow |E| \leq 3|V| - 6$.

Equality $|E| = 3|V| - 6$ holds iff every face is a triangle (so that $|F| = 2|E|/3$ exactly), i.e., $P$ is simplicial.

By Lemma C and C5, the ground-state $G(\mathcal{C})$ achieves the maximum $|E|$ among realizable configurations on $N_\alpha$ vertices. By the Euler bound just derived, this maximum is $|E| = 3 N_\alpha - 6$, achieved iff $P(\mathcal{C})$ is simplicial. So $P(\mathcal{C})$ is simplicial and $|E| = 3 N_\alpha - 6$, which is (i)–(iii).

For the deltahedral realization claim at $N_\alpha \in \{4, 5, 6, 7, 8, 9, 10, 12\}$: at these $N_\alpha$ values, a convex deltahedron exists (the eight Freudenthal-van der Waerden convex deltahedra). The C2-fixed edge length $R_{\alpha\alpha}$ is consistent with the deltahedral edge length, so the realization is the unique convex deltahedron at that $N_\alpha$ (uniqueness of the Freudenthal-van der Waerden enumeration up to symmetry). $\square$

---

## §6. Scope notes on the deltahedra gap

The Freudenthal-van der Waerden enumeration of convex deltahedra has exactly **eight members**, at $V \in \{4, 5, 6, 7, 8, 9, 10, 12\}$. There is no convex deltahedron at $V = 11$ or at $V \geq 13$ for finite $V$ (the icosahedron at $V=12$ is the largest). This means:

**The Theorem applies cleanly at $N_\alpha \in \{4, 5, 6, 7, 8, 9, 10, 12\}$.** For these values, the ground-state alpha cluster realizes the unique convex deltahedron, with $|E| = 3 N_\alpha - 6$ contact edges.

**The Theorem applies in graph-simplicial form at $N_\alpha \in \{11, 13, 14\}$**, but the polytope cannot be realized as a convex deltahedron (no all-equilateral all-equal-edge convex 3-polytope on 11, 13, or 14 vertices exists). The contact graph remains a planar 3-connected simplicial graph (a maximal planar graph), and Steinitz's theorem still says it is the 1-skeleton of *some* convex 3-polytope — but that polytope necessarily has non-uniform edge lengths.

This is in tension with the strict reading of C2, which fixes $R_{\alpha\alpha}$ uniformly. Resolution options:

(a) **The contact distance is not strictly uniform.** SS-7 inverts $R_{\alpha\alpha} = 2.37$ fm from the ⁸Be data, but the underlying CPP picture allows some range around this (the K₃ collective mode is a soft constraint, not a hard one). At $N_\alpha \in \{11, 13, 14\}$, the cluster realizes a convex simplicial 3-polytope with edge lengths varying within a small band around $R_{\alpha\alpha}$.

(b) **The cluster is not strictly convex at these $N_\alpha$.** A non-convex (but still simplicial-graph) arrangement could satisfy uniform edge lengths. This violates C6, but C6 is itself a paper-level hypothesis, and could be relaxed at specific $N_\alpha$ values.

(c) **The geometry is graph-simplicial but not 3-polytope-realized.** The contact graph is a maximal planar graph, but the geometric arrangement is a different topological object (a "pseudopolytope" or a polytope with non-3-connected structure due to symmetry constraints).

The empirical record (SS-7 Table 1: ⁴⁴Ti at $-0.26\%$, ⁵²Fe at $-0.57\%$, ⁵⁶Ni at $-0.73\%$) shows the binding formula continues to work at $N_\alpha \in \{11, 13, 14\}$ at $<1\%$ accuracy, indicating that whichever resolution is correct, the $|E| = 3N_\alpha - 6$ edge count is preserved.

This is registered as a separate scope question (call it **OPEN-SS-31**: structural realization of alpha clusters at deltahedra-gap $N_\alpha \in \{11, 13, 14\}$).

For the $N_\alpha = 3$ degenerate case (¹²C as planar triangle), the cluster is 3D-degenerate, so Lemma B (which assumes 3D-non-degeneracy) does not apply. The formula $|E| = 3 N_\alpha - 6 = 3$ correctly gives 3 edges, matching the planar-triangle realization. Treat as a separate degenerate case in the SS-9 paper.

---

## §7. Honest assessment of closure status

**What this draft (v0.2) delivers (after gaps closed):**

- Theorem statement and proof for $N_\alpha \in \{4, 5, 6, 7, 8, 9, 10, 12\}$ (the deltahedral range): C4 holds as a theorem, conditional on C1+C2+C3+C5+C6+(rigid packing)+(3D-non-degeneracy).
- Graph-simplicial extension at $N_\alpha \in \{11, 13, 14\}$ with the deltahedra-gap caveat registered as OPEN-SS-31.
- $N_\alpha = 3$ as a degenerate planar case, handled by direct edge count.

**What this draft does NOT deliver:**

- Programme-level closure (C5 from A1–A11). Registered as OPEN-SS-29 candidate.
- Programme-level closure (C6 from A1–A11). Registered as OPEN-SS-30 candidate.
- Resolution of the deltahedra gap. Registered as OPEN-SS-31 candidate.
- Polytope identity at each $N_\alpha$ (consistent with SS-7 Remark 2.2 disclaiming this).
- Programme-uniqueness (whether CPP forces simpliciality vs. it being a property of any rigid-tetrahedral framework with K₃ contacts). Honest framing remaining: this proof is geometric, so any framework with the same C1+C2+C3 gets the same result. Pattern 6's CPP-uniqueness remains contingent.

**Net effect on programme scorecard:**

- C4 promoted from "structural hypothesis" (B-tier in SS-7's Layer A/B/C/D classification) to "conditional theorem at C5+C6 inheritance tier."
- 54 of 55 conditional D-N entries promote conditionally: now C5+C6+C1+C2+C3-conditional, instead of C4+C1+C2+C3-conditional. Net change: one structural hypothesis (C4) replaced by two new structural hypotheses (C5, C6). The new defensive perimeter has more pieces but each piece is more tractable.
- Unconditional promotion would require closing all of OPEN-SS-29, OPEN-SS-30, OPEN-SS-31, plus the existing OPEN-SS-26, OPEN-SS-27, OPEN-SS-28 (for D1, D2, D3). That's a substantial follow-up program.

---

## §8. Gaps that need to close before SS-9 ships

1. **Lemma B forward direction:** Sharpen the argument that contact-edge $\{\alpha_i, \alpha_j\}$ corresponds to a convex-hull edge, not an internal diagonal. Most likely approach: show that the shared face $F_{ij}$ is necessarily on the surface of the convex hull, hence the centroids $c_i, c_j$ are connected by an edge of the polytope.

2. **Lemma B reverse direction:** Sharpen the argument that convex-hull edge corresponds to face-contact. Most likely approach: invoke C5 + C3 + the fact that K₃ contact face is the only alpha-alpha configuration that contributes $B_\text{pair}$ binding (vertex- and edge-contacts give zero), so ground-state selects face-contact.

3. **3D-non-degeneracy:** Stated as an assumption in Lemma B and the Theorem. Should ideally be derived from a "cluster is genuinely 3-dimensional at $N_\alpha \geq 4$" argument. Likely follows from the maximum-edge selection: planar arrangements have fewer edges than 3D arrangements at $N_\alpha \geq 4$, so C5 picks 3D. Worth verifying.

4. **Rigid-packing constraint:** Used implicitly in Lemma B. Should be stated explicitly as a hypothesis, possibly as part of C1 (rigidity as a geometric constraint, not just a binding-energy statement).

5. **C5 well-definedness:** "Ground-state energy minimization" requires defining the configuration space over which to minimize. The space includes all rigid-packing-compatible arrangements at fixed $N_\alpha$. Need to verify this space is well-defined and that minima exist (compactness argument).

---

## §9. Phase 4 candidate — programme-level closure attempt

Once Phase 1 + 3 (the conditional theorem) is solid, Phase 4 attempts to derive C5 from CPP primitives.

Sketch: C5 says the bound configuration minimizes total energy among physically realizable ones. Total energy in the alpha-cluster picture is $-N_\alpha B_\alpha - |E| B_\text{pair}$ (per SS-7) plus Coulomb (which SS-7 §6.2 argues is screened in bound polytopes per OPEN-SS-25). Minimizing this is straightforward at the level of the formula. The deeper question is: does CPP's lattice Hamiltonian generate this formula structure exactly (each contact face contributes $-B_\text{pair}$, additively, with no inter-face couplings beyond what C3 captures)?

Likely outcome: Phase 4 reduces "C5 from A1–A11" to "the SS-7 binding formula structure (additivity of $B_\text{pair}$ contributions across edges) is itself derivable from CPP primitives." This is essentially the formula-derivation question that SS-7 §6.2 already gestures at as open ("recurrence of $M_0/\varphi$ across SS-5 and SS-7 — empirically supported, not structurally derived"). Phase 4's contribution would then be to clarify that "C5 follows from formula additivity" and register the formula-additivity question as the actual open problem.

This is consistent with the theme that emerges across the programme: the K₃ scale-recurrence (Pattern 6) is the deep structural mystery, and programme-level closure of any specific result tends to reduce to "Pattern 6 holds by construction" or "Pattern 6 is itself the open problem."

