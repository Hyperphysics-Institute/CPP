# SS-9 Working Draft v0.3 — Conditional C4 Closure on Refined-C1 Foundation

**Status:** Working draft, in iteration. Replaces the v0.2 working draft (`OPEN-SS-24_phase1_v0.2_working_draft.md`) at the level of the proof structure. v0.2 remains in this folder as the historical artifact recording the Steinitz pivot (Session 2) and the strict-C1/degree-5 inconsistency that motivated the off-track refined-C1 work (Session 3). v0.3 inherits the v0.2 setup and Theorem-conclusion target but replaces the Lemma B argument with a graph-theoretic version that bypasses the centroid-hull supporting-hyperplane gap.

**Version:** 0.3
**Working in:** `/home/claude/CPP/` (sandbox; commit/push handled by Thomas via `git am`)
**Foundation:** SS-7 v1.3 §2.1 refined-C1 with multi-faceted rigidity facets (a)/(b)/(c).

**Substantive change from v0.2 → v0.3.** v0.2's Lemma B attempted to derive contact-graph = 1-skeleton-of-convex-hull-of-centroids by a supporting-hyperplane construction at the shared face $F_{ij}$. On re-examination the v0.2 argument has a real gap: the contact face $F_{ij}$ has nucleon-position vertices, not centroid vertices, so $F_{ij}$ does not directly bound $H = \text{conv}(c_1, \ldots, c_{N_\alpha})$, and rigid packing alone does not deliver the supporting hyperplane the construction needs. (Rigid packing forbids other alphas from intersecting the segment $\overline{c_i c_j}$, but does not forbid the convex hull of other centroids from crossing it.) v0.3 sidesteps this gap by adding **C7 (contact-graph planarity)** as a paper-level hypothesis at the same tier as C5 and C6, and using Steinitz's theorem as a black box on the contact graph viewed graph-theoretically. The deltahedron identification at the listed $N_\alpha$ values then comes from the FvdW classification combined with C2 (uniform alpha-alpha contact distance). The role of refined-C1 facet (b) becomes load-bearing in clause (iv) of the Theorem (existence of geometric realization at $N_\alpha \geq 7$ where strict-C1 cannot host degree-5 vertices), completing the structural integration of the Session 3 refinement into the SS-9 closure.

---

## §1. Setup and notation

Let $N_\alpha \in \mathbb{N}$ with $N_\alpha \geq 3$. An **$N_\alpha$-alpha cluster configuration** is a tuple $\mathcal{C} = (\alpha_1, \ldots, \alpha_{N_\alpha})$ of distinct rigid tetrahedral units in $\mathbb{R}^3$ ("alphas"), each at LO an approximately regular tetrahedron of edge length $L_\alpha$ (the SS-5-derived alpha-internal scale).

By **C1$'$** (refined alpha rigidity, inherited from SS-7 v1.3 §2.1), each $\alpha_i$ is a closed approximately regular 3-simplex with three structurally independent rigidity facets:
- **Facet (a):** Internal LO rigidity. At LO the alpha is a regular tetrahedron with four equilateral triangular outer faces, with a $\sim 5\%$ residual band per the SS-5 LO-rigidity remark.
- **Facet (b):** Vertex-hosting accommodation at degree-$\geq 5$ cluster vertices. When cluster topology requires the alpha to participate in $\geq 5$ contacts, the additional contacts beyond four are hosted within the LO rigidity envelope via [mechanism TBD; candidates include face-edge hybrid contact, K$_3$ delocalization across adjacent faces, partial-overlap docking].
- **Facet (c):** Cluster-level collective oblate-deformation slip-plane mode (provisional, OPEN-SS-32). Activates at belt/seam-supporting cluster shapes with binding contribution $\sim +B_\text{pair} \times \text{attenuation factor}$.

For Lemma A, Lemma B$'$, Lemma C, and the Theorem below, the load-bearing content of C1$'$ is facet (a) plus facet (b). Facet (c) corrections enter as an NLO addition to the binding formula and are accounted for separately at OPEN-SS-32 closure tier; facet (c) does **not** affect the LO geometric proof structure of this paper.

By **C2** (base-to-base contact, inherited from SS-7), the **contact relation** $\sim$ on $\{\alpha_1, \ldots, \alpha_{N_\alpha}\}$ is defined: $\alpha_i \sim \alpha_j$ iff there exist faces $F_i \subset \alpha_i$ and $F_j \subset \alpha_j$ such that $F_i \equiv F_j$ as triangular regions of $\mathbb{R}^3$. Under C1$'$ facet (a), each contact at LO has centroid-centroid separation $R_{\alpha\alpha}$ (the SS-7-calibrated alpha-alpha contact distance set by the K$_3$ collective-mode minimization).

Define:
- The **contact graph** $G(\mathcal{C}) = (V, E)$ with $V = \{\alpha_1, \ldots, \alpha_{N_\alpha}\}$ and $E = \{\{\alpha_i, \alpha_j\} : \alpha_i \sim \alpha_j\}$.
- The **convex hull of centroids** $H(\mathcal{C}) = \text{conv}(c_1, \ldots, c_{N_\alpha}) \subset \mathbb{R}^3$, where $c_i$ is the LO centroid of $\alpha_i$.
- The **binding energy** at LO $B(\mathcal{C}) = N_\alpha B_\alpha + |E| B_\text{pair}$, with $B_\alpha = 28.296$ MeV and $B_\text{pair} = M_0/\varphi = 2.342$ MeV inherited from SS-5/SS-7.

By **C3** (K$_3$ collective mode at each contact, inherited from SS-7), each contact $\alpha_i \sim \alpha_j$ contributes one collective bonding mode at energy $B_\text{pair}$.

The remaining paper-level structural hypotheses (the conditionals under which the Theorem closes):

**C5 (ground-state energy minimization).** Among all $N_\alpha$-alpha cluster configurations $\mathcal{C}$ that are physically realizable (no alpha-alpha interpenetration; cluster connected through $G$), the realized ground state minimizes total energy, equivalently maximizes $B(\mathcal{C})$. *Programme-level closure registered as OPEN-SS-29 candidate.*

**C6 (cluster surface-realization).** All centroids $c_i$ lie on the boundary $\partial H$ of the convex hull $H$. Equivalently: no alpha is interior to the cluster. *Programme-level closure registered as OPEN-SS-30 candidate.*

**C7 (contact-graph planarity, NEW in v0.3).** The contact graph $G(\mathcal{C})$ is planar — it admits an embedding in the plane (equivalently, on $S^2$) without edge crossings. *Programme-level closure registered as OPEN-SS-33 candidate (new this session).*

**Physical motivation for C7.** Under C6, the cluster is a "shell" of alphas with no interior member; under C1$'$ + rigid packing, the cluster is a contractible connected 3D region (no internal voids in the standard nuclear physics interpretation of an alpha cluster). Each alpha contributes outer faces to the cluster's exterior 2-surface $\Sigma$, with $\Sigma \cong S^2$ topologically (boundary of a contractible 3D region). The contact graph admits a natural embedding on $\Sigma$ via the alpha-dual construction (each alpha as a point on its own outer-face region, each contact as an arc through the shared interior face). This embedding makes $G$ planar. The C7 hypothesis records this topological inheritance from C6 + cluster contractibility, abstracted from the geometric details of the embedding so that Steinitz's theorem can be invoked directly. C7's first-principles closure from CPP primitives is the OPEN-SS-33 question; physical motivation alone justifies it as a paper-level hypothesis at the C5/C6 tier.

C5, C6, C7 are **paper-level structural hypotheses at the SS-7 inheritance tier**. None is derived from CPP axioms A1–A11 in this paper; each is registered as an OPEN-SS-2X candidate for follow-up programme-level closure.

We additionally assume **3D-non-degeneracy** (the alpha centroids do not all lie in a single plane) and **rigid packing** (no alpha-alpha interpenetration). 3D-non-degeneracy excludes the $N_\alpha = 3$ planar case (handled separately in §6); rigid packing is a definitional consequence of the rigid-tetrahedral construction.

---

## §2. Lemma A: Pairwise triangular contact

**Lemma A.** *Under C1$'$ and C2, for every $\{\alpha_i, \alpha_j\} \in E$, the contact face $F_{ij} = F_i \equiv F_j$ is an equilateral triangle of edge length $L_\alpha$ at LO.*

**Proof.** By C1$'$ facet (a), every face of $\alpha_i$ at LO is an equilateral triangle of edge length $L_\alpha$. By C2, $F_{ij}$ is the coincidence $F_i \equiv F_j$ as regions of $\mathbb{R}^3$. The intersection $F_i \cap F_j$ under full LO coincidence is exactly $F_i$ (and equally $F_j$), an equilateral triangle of edge length $L_\alpha$. Facet (b) accommodation modes at degree-$\geq 5$ vertices may produce sub-LO deviations from strict triangular coincidence (face-edge hybrid, partial overlap), but the LO triangular character is preserved. $\square$

**Remark A.1 (unchanged from v0.2).** Lemma A is essentially a definitional consequence of the LO rigidity and full-coincidence aspects of C1$'$ facet (a) + C2. Its content is the *exclusion* of partial-overlap-only, edge-only, or vertex-only contact configurations as C2-contacts. These excluded configurations are not impossible geometrically, but C2 explicitly restricts the contact relation to face-to-face full-coincidence cases; non-face contacts do not realize the K$_3$ collective mode of C3 and therefore do not contribute $B_\text{pair}$ binding.

**Remark A.2 (replaces v0.2 Remark A.2).** Lemma A establishes that every edge of $G$ corresponds to a triangular contact face between two alphas. In v0.2 this fed into a Lemma B that argued planarity + 3-connectedness from rigid-packing geometry; in v0.3, planarity is hypothesized at C7 and Lemma A's role is to ensure the contact graph is *simple* (one edge per pair) and that each edge has the LO triangular geometry that C2 + C3 require.

---

## §3. Lemma C: Energy minimization picks max edges

*[Promoted from v0.2 §4; same statement and proof as v0.2.]*

**Lemma C.** *Under C3 and C5, the ground-state contact graph $G(\mathcal{C}_\text{ground})$ has the maximum possible $|E|$ among all physically realizable contact graphs on $N_\alpha$ vertices satisfying Lemma A's hypotheses.*

**Proof.** By the SS-7 binding formula and C3, $B(\mathcal{C}) = N_\alpha B_\alpha + |E(\mathcal{C})| B_\text{pair}$ at LO. Since $B_\text{pair} > 0$, $B$ is strictly monotone increasing in $|E|$ at fixed $N_\alpha$. By C5, the ground state minimizes energy (equivalently, maximizes $B$), so the ground state has maximum $|E|$. $\square$

---

## §4. Lemma B$'$: Contact graph is 1-skeleton of convex 3-polytope

*[Replaces v0.2 §3 Lemma B. The two argumentative gaps in v0.2 (forward-direction supporting-hyperplane at $F_{ij}$; reverse-direction implicit C5 dependency) are dissolved by routing through C7 + Steinitz rather than through the centroid-hull identification that v0.2 attempted.]*

**Lemma B$'$.** *Let $\mathcal{C}$ be a ground-state $N_\alpha$-alpha cluster configuration with $N_\alpha \geq 4$, satisfying C1$'$, C2, C3, C5, C6, C7, rigid packing, and 3D-non-degeneracy. Then the contact graph $G(\mathcal{C})$ is the 1-skeleton (vertex-edge graph) of a simplicial convex 3-polytope, with $|E(\mathcal{C})| = 3 N_\alpha - 6$ and every face of the polytope a triangle.*

**Proof.**

*Step 1: $G$ is simple.* By C1$'$ facet (a) + C2 (Lemma A), for any pair $\{\alpha_i, \alpha_j\}$ there is at most one shared LO triangular face. Hence at most one edge in $G$ between any two vertices. ✓

*Step 2: $G$ is planar.* By C7. ✓

*Step 3: $|E| = 3 N_\alpha - 6$ and every face of the planar embedding is a triangle.* By Lemma C, $G$ has maximum $|E|$ among realizable contact graphs on $N_\alpha$ vertices. By Euler's formula applied to a connected planar graph on $N_\alpha$ vertices: $V - E + F = 2$, where $F$ is the face count of the planar embedding. Each face has at least three edges (no face is a 2-gon in a simple graph), and each edge is shared by exactly two faces, so $\sum_{f} |\partial f| = 2|E|$ with $|\partial f| \geq 3$, giving $3|F| \leq 2|E|$, i.e., $|F| \leq 2|E|/3$. Substituting into Euler: $N_\alpha - |E| + 2|E|/3 \geq 2$, i.e., $|E| \leq 3 N_\alpha - 6$, with equality iff every face is a triangle. By Lemma C the ground-state $G$ achieves this maximum, so $|E| = 3 N_\alpha - 6$ and every face of the planar embedding is a triangle. ✓

*Step 4: $G$ is 3-vertex-connected.* By Step 3, $G$ is a triangulation of $S^2$ (every face of the planar embedding is a triangle, and the embedding is on $S^2$ by the standard one-point compactification of $\mathbb{R}^2$). Standard result (Diestel, *Graph Theory*, 4.5; Whitney 1932): every triangulation of $S^2$ on $N \geq 4$ vertices is 3-vertex-connected. ✓

*Step 5: Apply Steinitz's theorem.* By Steinitz (1922; cf. Ziegler, *Lectures on Polytopes*, Theorem 4.1): a graph $G$ is the 1-skeleton of a convex 3-polytope iff $G$ is simple, planar, and 3-vertex-connected. By Steps 1, 2, 4, $G$ is the 1-skeleton of a convex 3-polytope $P$. By Step 3, $P$ is simplicial (every 2-face triangular) with $|E| = 3 N_\alpha - 6$. ✓

$\square$

**Remark B$'$.1 (the role of refined-C1 facet (b)).** Lemma B$'$ delivers a graph-theoretic conclusion: the contact graph is the 1-skeleton of *some* convex 3-polytope $P$. The polytope $P$ is determined up to its abstract combinatorial structure by Steinitz, but the *geometric realization* of $P$ in $\mathbb{R}^3$ — specifically, whether $P$ can be realized with vertices at the alpha centroids — is a separate question handled in the Theorem (§5) below. Refined-C1 facet (b) enters the Theorem at clause (iv): at $N_\alpha \geq 7$, the FvdW deltahedron has degree-5 vertices, and only facet (b)'s vertex-hosting accommodation makes the geometric realization at the centroids possible (strict-C1 with each alpha presenting four outer faces cannot host five face-coincident contacts at one alpha). This is the structural integration of Session 3's refined-C1 work into the SS-9 closure: facet (b) is load-bearing for clause (iv), not just for dissolving the strict-C1 inconsistency.

**Remark B$'$.2 (relation to the v0.2 supporting-hyperplane approach).** v0.2's Lemma B sought to derive contact-graph-equals-1-skeleton from a direct supporting-hyperplane construction at the contact face $F_{ij}$, drawing on rigid-packing + C6 alone. On re-examination this construction has a substantive gap: $F_{ij}$ has nucleon-position vertices (not centroid vertices), so it does not directly bound $H = \text{conv}(c_i)$. Rigid packing forbids other *alphas* from intersecting $\overline{c_i c_j}$, but the convex hull of other *centroids* can in principle cross $\overline{c_i c_j}$ (if other centroids surround the bipyramid $\alpha_i \cup \alpha_j$ on multiple sides), and v0.2's hypothesis stack does not exclude this. v0.3 sidesteps the gap by elevating the topological content the supporting-hyperplane argument was *implicitly* relying on (planarity of the contact graph) into an explicit hypothesis (C7). The cost is one new candidate open problem (OPEN-SS-33: programme-level closure of C7 from A1–A11). The benefit is a clean conditional Theorem with no remaining argumentative gaps in the Lemma stack.

---

## §5. Main Theorem

**Theorem (Conditional C4 closure on refined-C1 foundation).** *Let $\mathcal{C}$ be the ground-state alpha-cluster configuration of $N_\alpha \in \{4, 5, 6, 7, 8, 9, 10, 12\}$ alphas, under C1$'$, C2, C3, C5, C6, C7, rigid packing, and 3D-non-degeneracy. Then:*

*(i) $G(\mathcal{C})$ is the 1-skeleton of a simplicial convex 3-polytope.*

*(ii) $|E(\mathcal{C})| = 3 N_\alpha - 6$.*

*(iii) Every face of the polytope is a triangle.*

*(iv) The polytope is realized geometrically as the unique Freudenthal–van der Waerden convex deltahedron at $N_\alpha$, with vertices at the alpha LO centroids and uniform edge length $R_{\alpha\alpha}$ (the C2-fixed alpha-alpha contact distance).*

**Proof.**

*Clauses (i)–(iii):* Direct consequence of Lemma B$'$.

*Clause (iv):* By (i)–(iii), $G$ is the 1-skeleton of a simplicial convex 3-polytope $P$. By C2, every contact in the ground state has centroid-centroid separation $R_{\alpha\alpha}$ at LO, so every edge of $P$ has the same length $R_{\alpha\alpha}$ (after centroid-realization). A simplicial convex 3-polytope on $N_\alpha$ vertices with all-equilateral-triangular faces and uniform edge length is, by definition, a convex deltahedron of edge length $R_{\alpha\alpha}$. By the Freudenthal–van der Waerden theorem (1947): convex deltahedra exist on exactly $N \in \{4, 5, 6, 7, 8, 9, 10, 12\}$ vertices, and at each of these $N$ values the convex deltahedron is unique up to isometry. So $P$ is realized as the FvdW deltahedron at $N_\alpha$.

*Geometric realizability at $N_\alpha \geq 7$ via refined-C1 facet (b):* At $N_\alpha \in \{7, 8, 9, 10, 12\}$, the FvdW deltahedron has at least one vertex of degree $\geq 5$ (pentagonal bipyramid: 2 apex degree-5; snub disphenoid: 4 of 8 vertices degree 5; triaugmented triangular prism: 6 of 9 vertices degree 5; gyroelongated square bipyramid: 8 of 10 vertices degree 5; icosahedron: all 12 vertices degree 5). Strict-C1 with each alpha presenting four outer faces cannot host five face-coincident contacts at a single vertex. Refined-C1 facet (b) provides the accommodation modes (face-edge hybrid contact, K$_3$ delocalization across adjacent faces, partial-overlap docking — specific mechanism TBD) under which the additional degree-$\geq 5$ contacts are hosted within the LO rigidity envelope. Without facet (b), clause (iv) would be vacuous at $N_\alpha \geq 7$ because no rigid-tetrahedral realization of the FvdW deltahedron at those values exists. With facet (b), the realization exists at LO, with sub-LO corrections in the rigidity band (and registered separately as facet (c)'s slip-plane bonus accounting for the empirical Regime B excess in SS-7 Table 1).

$\square$

---

## §6. Scope notes (deltahedra-gap, $N_\alpha = 3$ degenerate, Coulomb)

*[Largely unchanged from v0.2 §6, with light edits to reflect v0.3 framing.]*

The Freudenthal–van der Waerden enumeration of convex deltahedra has exactly **eight members**, at $V \in \{4, 5, 6, 7, 8, 9, 10, 12\}$. There is no convex deltahedron at $V = 11$ or at $V \geq 13$ for finite $V$. For $N_\alpha \in \{11, 13, 14\}$, clause (iv) of the Theorem does not apply: no FvdW deltahedron exists to realize. Lemma B$'$'s graph-theoretic conclusions (clauses (i)–(iii)) still hold — the contact graph remains a planar 3-connected simplicial graph, the 1-skeleton of *some* convex 3-polytope — but that polytope must have non-uniform edge lengths (since uniform-edge-length simplicial convex polytopes on those $N$ values do not exist). The empirical record (SS-7 Table 1: ${}^{44}$Ti at $-0.26\%$, ${}^{52}$Fe at $-0.57\%$, ${}^{56}$Ni at $-0.73\%$ deviation from the LO formula) confirms that the $|E| = 3 N_\alpha - 6$ edge count is preserved at these $N_\alpha$ values, supporting the v0.2-flagged resolution that the contact distance is allowed a small range around $R_{\alpha\alpha}$ per option (a) of v0.2 §6, or that the cluster is graph-simplicial but not strictly polytope-deltahedral per option (c). Resolution between options is registered as **OPEN-SS-31** (deltahedra-gap structural realization at $N_\alpha \in \{11, 13, 14\}$).

For the **$N_\alpha = 3$ degenerate case** (${}^{12}$C as planar triangle), the cluster is 3D-degenerate, so Lemma B$'$ (which assumes 3D-non-degeneracy) does not apply directly. The formula $|E| = 3 N_\alpha - 6 = 3$ correctly gives 3 edges, matching the planar-triangle realization. Treat as a separate degenerate case in the SS-9 paper proper.

**Coulomb screening at the deltahedral surface** (per SS-7 §6.2): screened in bound polytopes per OPEN-SS-25. Not affected by the v0.2 → v0.3 restructuring.

---

## §7. Honest assessment of closure status under v0.3

**What v0.3 delivers (after Lemma B$'$ closes):**

- Theorem statement and proof for $N_\alpha \in \{4, 5, 6, 7, 8, 9, 10, 12\}$: C4 holds as a theorem, conditional on **C1$'$ + C2 + C3 + C5 + C6 + C7 + rigid packing + 3D-non-degeneracy**. The hypothesis stack has **one new entry** relative to v0.2 (C7), tracked at OPEN-SS-33 candidate.
- Graph-simplicial extension at $N_\alpha \in \{11, 13, 14\}$: clauses (i)–(iii) of Theorem hold; clause (iv) does not. Same status as v0.2 §6, registered as OPEN-SS-31.
- $N_\alpha = 3$ planar degenerate: handled by direct edge count.
- Refined-C1 facet (b) integrated as load-bearing in Theorem clause (iv). Without facet (b), clause (iv) is vacuous at $N_\alpha \geq 7$.
- Refined-C1 facet (c) (slip-plane bonus, OPEN-SS-32) treated as NLO addition to the LO binding formula; v0.3 Theorem unchanged by facet (c) in the LO accounting.

**What v0.3 does NOT deliver (compared to v0.2's stated targets):**

- Programme-level closure of C5 from A1–A11. Same as v0.2 (OPEN-SS-29 candidate).
- Programme-level closure of C6 from A1–A11. Same as v0.2 (OPEN-SS-30 candidate).
- Programme-level closure of C7 from A1–A11. **NEW (OPEN-SS-33 candidate).**
- Resolution of the deltahedra-gap at $N_\alpha \in \{11, 13, 14\}$. Same as v0.2 (OPEN-SS-31 candidate).
- First-principles derivation of facet (b)'s mechanism (face-edge hybrid? K$_3$ delocalization? partial overlap?). Mentioned but not derived. Could fold into OPEN-SS-32 derivation if facets (b) and (c) share Layer-3 ancestry as the same K$_3$ scale-recurrence operating at different geometric venues.
- First-principles derivation of facet (c) attenuation factor. Same as Session 3 status (OPEN-SS-32 candidate).
- Polytope-uniqueness argument (whether CPP forces simpliciality vs. it being a property of any C1$'$-C7 framework). The Theorem proof is a graph-theoretic argument plus FvdW classification; both are independent of CPP-uniqueness, so any framework satisfying C1$'$-C7 gets the same conclusion.

**Net effect on programme scorecard:**

- C4 promoted from "structural hypothesis" (B-tier in SS-7's Layer A/B/C/D classification) to **"conditional theorem at C5+C6+C7 inheritance tier on the refined-C1 foundation."**
- 54 of 55 conditional D-N entries promote conditionally: now C5+C6+C7+C1$'$+C2+C3-conditional, instead of C4+C1+C2+C3-conditional. Net change relative to v0.2: one additional conditional (C7); relative to pre-v0.2: one structural hypothesis (C4) replaced by three new structural hypotheses (C5, C6, C7).
- Unconditional promotion would require closing all of OPEN-SS-29, OPEN-SS-30, **OPEN-SS-33 (NEW)**, OPEN-SS-31, plus the existing OPEN-SS-26, OPEN-SS-27, OPEN-SS-28 (for D1, D2, D3) at SS-8.

---

## §8. Gaps that remain to close before SS-9 ships

*[Updated for v0.3 framing.]*

1. **C7 motivation argument** (§1, "Physical motivation for C7"): The verbal argument that C7 follows from C6 + cluster contractibility + the natural alpha-dual embedding on $\Sigma$ is plausible but not a formal proof. For SS-9 v1.0 ship, either (a) tighten the argument into a formal sub-lemma showing C6 + cluster contractibility ⇒ C7, or (b) accept C7 as a separate paper-level hypothesis with OPEN-SS-33 registered for first-principles closure. Option (b) is the conservative path consistent with how C5 and C6 are handled.

2. **C7 first-principles derivation (OPEN-SS-33 candidate, NEW):** Programme-level closure of C7 from A1–A11. The derivation route most likely involves the cluster-shell topology being forced by CPP lattice geometry under the rigid-packing constraint of C1$'$ — i.e., that any A1–A11-respecting alpha cluster has a contractible shell topology. Worth investigating whether C7 is an independent hypothesis or follows from C5 + C6 under additional CPP-specific constraints (in which case OPEN-SS-33 closes for free).

3. **Facet (b) mechanism identification:** Three candidate mechanisms registered in SS-7 v1.3 §2.1 (face-edge hybrid contact, K$_3$ delocalization across adjacent faces, partial-overlap docking). Distinguishing them is testable via predicted contact-distance distributions at degree-5 sites, accessible to AMD or Brink–Bloch cluster-model calculations. Likely closes with OPEN-SS-32 if facets (b) and (c) share Layer-3 ancestry.

4. **3D-non-degeneracy:** Stated as an assumption. Should ideally be derived from "cluster is genuinely 3-dimensional at $N_\alpha \geq 4$" via the maximum-edge selection (planar arrangements have fewer edges than 3D arrangements at $N_\alpha \geq 4$, so C5 picks 3D). Worth verifying as a sub-lemma.

5. **C5 well-definedness:** "Ground-state energy minimization" requires defining the configuration space over which to minimize. The space includes all rigid-packing-compatible arrangements at fixed $N_\alpha$ under C1$'$. Need to verify this space is well-defined and that minima exist (compactness argument).

6. **Empirical validation of clause (iv) at $N_\alpha \geq 7$:** The SS-7 Table 1 residual fingerprint (Regime B flat plateau at $+0.55 \, B_\text{pair}$, icosahedron suppressed at $+0.30 \, B_\text{pair}$) is consistent with the LO geometric realization of the FvdW deltahedron via facet (b) accommodation, with facet (c) slip-plane providing the NLO correction. The numerical agreement is supporting evidence but not direct verification. A more direct verification would be: predict the contact-distance distribution at degree-5 vertices of the realized FvdW deltahedron under each candidate facet (b) mechanism, and test against AMD calculations.

---

## §9. Phase 4 candidate — programme-level closure attempts (sketch)

*[Same as v0.2 §9, with C7 added to the closure target list.]*

Once Phase 1+3 (the conditional theorem under v0.3 hypotheses) is solid, Phase 4 attempts to derive C5, C6, and C7 from CPP primitives.

**C5 derivation (sketch from v0.2):** C5 says the bound configuration minimizes total energy among physically realizable ones. Minimizing this is straightforward at the level of the formula. The deeper question is: does CPP's lattice Hamiltonian generate this formula structure exactly (each contact face contributes $-B_\text{pair}$, additively, with no inter-face couplings beyond what C3 captures)? Likely outcome: Phase 4 reduces "C5 from A1–A11" to "the SS-7 binding formula structure (additivity of $B_\text{pair}$ contributions across edges) is itself derivable from CPP primitives," which is essentially the formula-derivation question that SS-7 §6.2 already gestures at.

**C6 derivation (sketch):** C6 says no alpha is interior to the cluster. The derivation route is likely energetic: an interior alpha is "shielded" from external Coulomb but loses some of its $B_\text{pair}$ contribution channels to other alphas (since fewer faces are exposed for additional contacts in a hypothetical larger cluster); on net, surface configurations are energetically preferred. Working this out from CPP primitives is the OPEN-SS-30 question.

**C7 derivation (sketch, NEW for v0.3):** Under C6 + cluster contractibility, the cluster's outer 2-surface $\Sigma \cong S^2$ topologically. The alpha-dual embedding maps the contact graph onto $\Sigma$. A formal version of this argument (rigorously deriving planarity of the contact graph from the cluster topology) would close OPEN-SS-33 modulo the auxiliary "cluster is contractible" assumption. The contractibility itself follows from the CPP lattice geometry under bound-state assumptions: a non-contractible cluster (e.g., toroidal) would have an internal void at lower density than the surrounding $\text{DP}$-sea, which is energetically unfavorable. Working this out rigorously is the OPEN-SS-33 question.

This is consistent with the theme that emerges across the strong-sector programme: the K$_3$ scale-recurrence (Pattern 6) is the deep structural mystery, and programme-level closure of any specific result tends to reduce to "Pattern 6 holds by construction" or "Pattern 6 is itself the open problem." C5/C6/C7 are all candidates for closure-via-Pattern-6-articulation.

---

## §10. Changelog from v0.2

**Structural changes:**
- v0.2 Lemma B (centroid-hull supporting-hyperplane construction) removed; v0.3 Lemma B$'$ (graph-theoretic via Steinitz) added in its place.
- New paper-level hypothesis C7 (contact-graph planarity) added at the C5/C6 inheritance tier.
- New candidate open problem OPEN-SS-33 registered for programme-level closure of C7.
- Refined-C1 (SS-7 v1.3 §2.1 facets a/b/c) imported as C1$'$ replacing v0.2's strict-C1.
- Refined-C1 facet (b) made load-bearing in Theorem clause (iv): without facet (b), the FvdW deltahedron at $N_\alpha \geq 7$ has no rigid-tetrahedral realization.

**Argumentative gaps closed:**
- v0.2 forward-direction supporting-hyperplane gap at $F_{ij}$: dissolved by routing through C7 + Steinitz.
- v0.2 reverse-direction implicit C5 dependency: now explicit in Lemma C + Lemma B$'$ Step 3 (max-edge ⇒ triangulation ⇒ contact graph realizes 1-skeleton of simplicial polytope, with the K$_3$ binding contribution exactly counting 1-skeleton edges).

**Argumentative gaps preserved (registered for follow-up):**
- C5 first-principles derivation (OPEN-SS-29).
- C6 first-principles derivation (OPEN-SS-30).
- C7 first-principles derivation (OPEN-SS-33, NEW).
- Deltahedra-gap structural realization at $N_\alpha \in \{11, 13, 14\}$ (OPEN-SS-31).
- Facet (b) mechanism identification (OPEN-SS-32-adjacent).
- Facet (c) attenuation factor derivation (OPEN-SS-32).

**Numerical content:** unchanged. The LO binding formula $B = N_\alpha B_\alpha + (3 N_\alpha - 6) B_\text{pair}$ is the same in v0.2 and v0.3; the SS-7 Table 1 predictions are the same; no new fitted parameters are introduced.

**Empirical scope:** unchanged. Theorem holds at $N_\alpha \in \{4, 5, 6, 7, 8, 9, 10, 12\}$; deltahedra-gap range and degenerate $N_\alpha = 3$ handled separately.
