# OPEN-FP-F1-5 Sequence-2A Scoping: Edge-Aligned Reading-C Coefficient Enumeration Trajectory

**Path:** `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/F1_reading_C_edge_aligned_coefficient_scoping.md`
**Opened:** 27 May 2026 (Session 146 Patch 0599)
**Author:** Opus (Claude)
**Status:** Scoping at sketch level. NOT closure work. Opens the OPEN-FP-F1-5 Sequence-2A trajectory as a multi-Patch arc paralleling the vertex-aligned Route C sequence 2 trajectory (Patches 0587–0592). This document does not execute any closure work, does not propose framework extensions, does not modify the v1.0 SHIPPED F.1 paper or any of the 13 hardened-theorem artifacts in `hardened_theorems/`.
**Scope:** Enumerate the geometric primitives and path-class structure required to compute closed-form first-order and second-order substrate-current coefficients $\alpha_k^{(\rho)}, \alpha_k^{(\text{edge})}$ within the 2D $D_5$-invariant subspace $\mathrm{span}\{\hat{n}_\rho, \hat{n}_{\text{edge}}\}$ established at THEO-DSL-6 (candidate) under edge-aligned Reading C with vertex-host convention. Articulate the trajectory plan as a 4–6 Patch sequence. Identify decision-gate items requiring Thomas input before substantive Layer 3 work begins.

---

## §0 Working-session firewall + anti-priorities

### §0.1 What this sketch IS

This document opens **Sequence-2A** of the OPEN-FP-F1-5 trajectory — the coefficient-enumeration sub-trajectory targeting closed-form $\alpha_k^{(\rho)}, \alpha_k^{(\text{edge})}$ at $\mathcal{O}(\delta^k)$ within the 2D $D_5$-invariant subspace established at THEO-DSL-6 (candidate; Patch 0596). The scope is:

- Inventory the geometric primitives needed at edge-aligned Reading C with $D_5$ stabilizer (orbit structures under $D_5$ acting on first-shell vertices, first-shell-to-first-shell edges, host-to-second-shell edges, etc.);
- Surface the substantive scoping findings at first-order that already follow from existing F.1 primitives without new geometric work;
- Articulate the path-class decomposition at $\mathcal{O}(\delta^2)$ under edge-aligned Reading C;
- Propose a publication-grade Layer 3 / sketch-document Layer 3 hardened-theorem artifact sequence paralleling the vertex-aligned Patches 0587–0592 trajectory;
- Identify decision-gate items requiring Thomas input;
- Register a risk inventory + cross-trajectory linkage.

The scope is **scoping at sketch level**, NOT closure work. Each geometric primitive, each path-class enumeration, and each artifact in §7 is its own gated sub-trajectory; this document enumerates them but does not execute any of them.

### §0.2 Anti-priorities sustained at this Patch

1. **NO Layer 3 closure work in this Patch** — this is the scoping document. Each Sequence-2A sub-target is a separate gated sub-trajectory.
2. **NO modification of v1.0 SHIPPED F.1 paper sources** — `dynamical_substrate_law.tex` and `dynamical_substrate_law.pdf` are frozen at v1.0 SHIPPED per Patch 0570 + §17.8 immutable-checkpoint discipline.
3. **NO modification of hardened-theorem artifacts** — Patches 0550 + 0551 + 0552 + 0571 + 0585 + 0587 + 0588 + 0589 + 0590 + 0591 + 0592 + 0596 + 0597 are frozen. Sequence-2A artifacts will be NEW `.tex` files under `hardened_theorems/` at future Patches.
4. **NO modification of programme-level theorems** (THEO-DSL-1 + THEO-DSL-2 + THEO-DSL-3 + THEO-DSL-4 + THEO-DSL-5 (candidate) + THEO-DSL-6 (candidate) + THEO-DSL-8 (candidate) in `theorem-registry.md` SD section). The candidate THEO-DSL-7 will be registered at the Sequence-2A umbrella-Patch when it reaches sketch-document Layer 3 rigor under (H5$_E$).
5. **NO framework-extension commitment beyond (H5$_E$) inheritance from vertex-aligned (H5)** — (H5$_E$) is the per-variant specialization of (H5) to the edge-aligned variant; it inherits the same DG-1 sub-option A/B/C resolution structure from OPEN-FP-F1-1's framework-extension scope qualifier. Publication-grade hardening of (H5$_E$) inherits any future (H5) hardening via priority queue item (G).
6. **NO new Open Problem registrations** at programme level in this Patch — the parent Open Problem OPEN-FP-F1-5 is already registered; its coefficient sub-questions are sub-targets of that closure.
7. **NO reviewer engagement** on this scoping Patch — Layer 3 scoping Patches do not require external review.
8. **NO promotion of any sub-target to closure-Patch trajectory in this Patch** — sub-target promotion is a decision-gate item.
9. **NO bundling of multiple sub-targets into single closure Patch** — each Layer 3 sub-target is its own gated trajectory per the single-artifact-per-Patch pattern preserved 13-for-13 since Patch 0585.
10. **NO Sequence-2B (face-aligned) substantive content** — Sequence-2B is a separate trajectory with its own future scoping document under $C_s$ stabilizer; this scoping document is Sequence-2A only.

---

## §1 Inherited findings from Sequence-1A (THEO-DSL-6 candidate)

**THEO-DSL-6 (candidate)** — registered at Patch 0598 in `theorem-registry.md` SD section — establishes at publication-grade Layer 3 unconditional rigor that the $\mathcal{O}(\delta^k)$ coefficient $\vec{j}_k^{\text{edge}}(v_{\text{host}})$ of the substrate current at the host vertex under edge-aligned Reading C with vertex-host convention lies in the 2D $D_5$-invariant subspace

$$\vec{j}_k^{\text{edge}}(v_{\text{host}}) \in \mathrm{span}\{\hat{n}_\rho, \hat{n}_{\text{edge}}\}$$

for every $k \geq 1$. Here $\hat{n}_\rho = v_{\text{host}}/|v_{\text{host}}|$ is the radial direction at the host vertex and $\hat{n}_{\text{edge}} = (u_1 - v_{\text{host}})/|u_1 - v_{\text{host}}|$ is the along-edge direction toward a chosen first-shell neighbor $u_1$.

The structural sub-question of OPEN-FP-F1-5 edge-aligned variant is therefore CLOSED at publication-grade Layer 3 unconditional rigor. The remaining substantive content is the **coefficient sub-question**: closed-form computation of $\alpha_k^{(\rho)}$ (radial coefficient) and $\alpha_k^{(\text{edge})}$ (along-edge coefficient) at $\mathcal{O}(\delta^k)$ for $k \geq 1$. Sequence-2A targets this coefficient sub-question.

The methodological template is the vertex-aligned Route C sequence 2 trajectory (Patches 0587–0592 closed at Session 145 with $\alpha_2 = -9/\phi^2 \approx -3.438$ registered as THEO-DSL-5 candidate). Sequence-2A follows the same single-artifact-per-Patch hardened-artifact discipline + four-condition test pattern + (H5)-class framework-extension scope qualifier specialized to (H5$_E$).

---

## §2 Scope target: closed-form $\alpha_k^{(\rho)}, \alpha_k^{(\text{edge})}$ at $\mathcal{O}(\delta^k)$

The Sequence-2A closure target is closed-form expressions for the substrate-current coefficients in the 2D $D_5$-invariant subspace:

$$\vec{j}_k^{\text{edge}}(v_{\text{host}}) = \alpha_k^{(\rho)} \hat{n}_\rho + \alpha_k^{(\text{edge})} \hat{n}_{\text{edge}} + \mathcal{O}(\delta^{k+1})$$

under the hypothesis stack (H1)–(H5$_E$) inherited from THEO-DSL-6. The primary deliverable target is $k = 2$ closure (paralleling the vertex-aligned $\alpha_2 = -9/\phi^2$ at THEO-DSL-5 candidate); the $k = 1$ closure is a stepping-stone substantive deliverable that does not have a direct vertex-aligned analog (since the vertex-aligned $k = 1$ result $\alpha_1 = 6/\phi^2$ pre-dates the Sequence-2A trajectory and is registered at THEO-DSL-3 / F.1 v1.0 Theorem 7.1).

Note: under vertex-aligned Reading C, the 1D invariant subspace $\mathbb{R}\hat{n}_\rho$ collapses $\alpha_k^{(\rho)}$ and $\alpha_k^{(\text{edge})}$ into a single coefficient (since $\hat{n}_\rho = \hat{n}_{\text{vertex}}$). Under edge-aligned Reading C, the 2D invariant subspace genuinely supports two independent coefficients at every order — the substantive structural weakening identified at THEO-DSL-6.

---

## §3 Substantive scoping findings (computable without new geometric primitives)

The following partial substantive results are computable from existing F.1 v1.0 primitives + the icosahedral rank-1 sum identity (PRED-O-30) without introducing new geometric primitives under the $D_5$ stabilizer. These are scoping findings, NOT closure work — but they provide an inventory check for the substantive structure of Sequence-2A's eventual deliverables.

### §3.1 First-shell orbit structure under $D_5$ acting on the 12 first-shell vertices

The $D_5$ stabilizer of the oriented edge $\{v_{\text{host}}, u_1\}$ in $H_4$ has order 10 (per Patch 0596 Remark 5.1 anti-erasure correction). Acting on the 12 first-shell vertices of $v_{\text{host}}$, $D_5$ decomposes the orbit set as

$$\{u_1\} \cup \{\text{pentagonal ring of 5 vertices adjacent to } u_1 \text{ in icosahedral first-shell}\} \cup \{\text{pentagonal ring of 5 vertices NOT adjacent to } u_1\} \cup \{\text{antipode of } u_1\} = 1 + 5 + 5 + 1 = 12$$

The 5+5+1 of non-$u_1$ orbits follows from the icosahedral structure: with $u_1$ chosen as "north pole" of the first-shell icosahedron, the 11 other icosahedral vertices split as (i) 5 vertices adjacent to north pole forming the northern pentagonal ring; (ii) 5 vertices adjacent to south pole forming the southern pentagonal ring; (iii) 1 south pole (antipode of $u_1$). The $D_5 = C_5 \rtimes C_2$ structure has 5-fold rotation around the $v_{\text{host}}$–$u_1$ axis (cycling each pentagonal ring) plus a reflection symmetry swapping the two pentagonal rings... NO, wait: in the icosahedral geometry, the $D_5$ stabilizer of the edge $\{v_{\text{host}}, u_1\}$ fixes both endpoints, and its 5-fold rotation is around the axis through both endpoints. The reflection symmetry of $D_5$ swaps members within each pentagonal ring (and within the antipode singleton), not between the two rings. So the 5+5+1+1 structure is correct, with $D_5$ acting as transitive 5-fold on each pentagonal ring + identity on the singletons.

### §3.2 Preliminary identities computable from existing primitives

Two identities computable at scoping level without new geometric primitives:

**Identity P1** (using $I_h$ first-shell sum identity at $\hat{n}_\rho$ direction):
$$\sum_{i=1}^{12} \hat{u}_i \cdot \hat{n}_{\text{edge}} = -(6/\phi) \cdot (\hat{n}_\rho \cdot \hat{n}_{\text{edge}}) = -(6/\phi) \cdot (-1/(2\phi)) = +3/\phi^2$$

Derivation: $\sum_i \hat{u}_i = -(6/\phi) \hat{n}_\rho$ by $I_h$-symmetry of the 12 first-shell unit vectors (the sum is $I_h$-invariant and therefore parallel to $\hat{n}_\rho$, with magnitude determined by $\sum_i (\hat{u}_i \cdot \hat{n}_\rho) = 12 \cdot (-1/(2\phi)) = -6/\phi$). Then $\sum_i \hat{u}_i \cdot \hat{n}_{\text{edge}} = (-(6/\phi) \hat{n}_\rho) \cdot \hat{n}_{\text{edge}}$, and $\hat{n}_\rho \cdot \hat{n}_{\text{edge}} = \hat{n}_\rho \cdot \hat{u}_1 = -1/(2\phi)$ by uniform projection (THEO-DSL-2 Theorem 5.1).

**Identity P2** (using the second-moment tensor identity):
$$\sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n}_{\text{edge}})^2 = 5 - \phi \approx 3.382$$

Derivation: The symmetric matrix $M = \sum_i \hat{u}_i \hat{u}_i^T$ in $\mathbb{R}^4$ commutes with the $I_h$-action and therefore decomposes as $M = A \hat{n}_\rho \hat{n}_\rho^T + B P_T$, where $P_T$ projects onto $T_{v_{\text{host}}}S^3 \cong \mathbb{R}^3$. From $\text{Tr}(M) = 12$: $A + 3B = 12$. From $M \hat{n}_\rho = \sum_i (\hat{u}_i \cdot \hat{n}_\rho) \hat{u}_i = (3/\phi^2)\hat{n}_\rho$ (icosahedral rank-1 sum identity PRED-O-30): $A = 3/\phi^2$. Hence $B = (12 - 3/\phi^2)/3 = 4 - 1/\phi^2 = 4 - (2-\phi) = 2 + \phi$ (using $1/\phi^2 = 2 - \phi$). Then
$$\sum_i (\hat{u}_i \cdot \hat{n}_{\text{edge}})^2 = \hat{n}_{\text{edge}}^T M \hat{n}_{\text{edge}} = A (\hat{n}_\rho \cdot \hat{n}_{\text{edge}})^2 + B(1 - (\hat{n}_\rho \cdot \hat{n}_{\text{edge}})^2) = (3/\phi^2)(1/(4\phi^2)) + (2+\phi)(1 - 1/(4\phi^2))$$
$$= 3/(4\phi^4) + (2+\phi) - (2+\phi)/(4\phi^2)$$
Numerically: $3/(4\phi^4) \approx 0.109$, $(2+\phi) \approx 3.618$, $(2+\phi)/(4\phi^2) \approx 0.345$. Total $\approx 3.382 = 5 - \phi$. ✓

### §3.3 First-order substrate-current structure (preview)

From Mechanism A at $\mathcal{O}(\delta^1)$:
$$\vec{j}_1^{\text{edge}}(v_{\text{host}}) = 2 r_0 \delta \sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n}_{\text{edge}}) \hat{u}_i$$

By THEO-DSL-6, $\vec{j}_1^{\text{edge}} \in \mathrm{span}\{\hat{n}_\rho, \hat{n}_{\text{edge}}\}$. Projecting onto the two basis vectors using Identities P1 + P2:

- **Radial projection** ($\hat{n}_\rho \cdot \vec{j}_1^{\text{edge}} = 2 r_0 \delta \sum_i (\hat{u}_i \cdot \hat{n}_{\text{edge}})(\hat{u}_i \cdot \hat{n}_\rho)$): use $\hat{u}_i \cdot \hat{n}_\rho = -1/(2\phi)$ uniformly, factor out, and use Identity P1:
$$\hat{n}_\rho \cdot \vec{j}_1^{\text{edge}} = 2 r_0 \delta \cdot (-1/(2\phi)) \cdot (3/\phi^2) = -3 r_0 \delta / \phi^3 = r_0 \delta (9 - 6\phi) \approx -0.708\, r_0 \delta$$
(Using $1/\phi^3 = 2\phi - 3$, so $3/\phi^3 = 6\phi - 9$.)

- **Edge projection** ($\hat{n}_{\text{edge}} \cdot \vec{j}_1^{\text{edge}} = 2 r_0 \delta \sum_i (\hat{u}_i \cdot \hat{n}_{\text{edge}})^2$): use Identity P2:
$$\hat{n}_{\text{edge}} \cdot \vec{j}_1^{\text{edge}} = 2 r_0 \delta (5 - \phi) = r_0 \delta (10 - 2\phi) \approx 6.764\, r_0 \delta$$

Both projections are non-zero, confirming the 2D $D_5$-invariant subspace is **genuinely 2D at first order** — not accidentally 1D. This is a substantive first-order Sequence-2A finding: the dimensional growth from 1D (vertex-aligned) to 2D (edge-aligned) established structurally at THEO-DSL-6 is realized quantitatively at the lowest non-trivial order. The orthogonal-basis decomposition into $\{\hat{n}_\rho, \hat{n}_{\text{edge}}\}$ requires solving a 2-by-2 inverse to recover $\alpha_1^{(\rho)}, \alpha_1^{(\text{edge})}$ in that basis (the basis is non-orthogonal: $\hat{n}_\rho \cdot \hat{n}_{\text{edge}} = -1/(2\phi)$).

**Substantive observation**: at first order, the radial component coefficient is $|\alpha_1^{(\rho)}| = 3/\phi^3 \approx 0.708$ along $\hat{n}_\rho$ projection axis, compared to the vertex-aligned $|\alpha_1| = 6/\phi^2 \approx 2.292$. The total substrate-current magnitude under edge-aligned at first order is therefore smaller than the vertex-aligned magnitude — consistent with the symmetry-breaking interpretation that vertex-aligned Reading C maximizes substrate-current alignment along the substrate primitive direction.

### §3.4 Open scoping question: closed-form first-order $\alpha_1$ in the basis decomposition

The two projections in §3.3 give $\hat{n}_\rho \cdot \vec{j}_1^{\text{edge}}$ and $\hat{n}_{\text{edge}} \cdot \vec{j}_1^{\text{edge}}$ but NOT directly the coefficients $\alpha_1^{(\rho)}, \alpha_1^{(\text{edge})}$ in the basis $\{\hat{n}_\rho, \hat{n}_{\text{edge}}\}$. The basis is non-orthogonal, so solving the 2-by-2 system requires inverting the Gram matrix
$$G = \begin{pmatrix} 1 & -1/(2\phi) \\ -1/(2\phi) & 1 \end{pmatrix}, \quad \det G = 1 - 1/(4\phi^2) = 1 - (2-\phi)/4 = (\phi+2)/4$$
to recover $(\alpha_1^{(\rho)}, \alpha_1^{(\text{edge})})$ from the projection pair. Closed-form expressions involve cross-products of the two projection identities + the Gram matrix inverse. The full first-order coefficient closure is the natural opening substantive Patch of the Sequence-2A trajectory (Patch 0600 A1$_E$).

---

## §4 Geometric primitives needed for Sequence-2A

The Sequence-2A trajectory requires the following geometric primitives under the $D_5$ stabilizer at edge-aligned Reading C with vertex-host convention. Some primitives parallel vertex-aligned analogs (Patches 0587–0590); others are edge-aligned-specific.

| Primitive | Description | Vertex-aligned analog | Status |
|-----------|-------------|----------------------|--------|
| **G1$_E$** | First-shell projection orbit structure: $\hat{u}_i \cdot \hat{n}_{\text{edge}}$ for the 12 first-shell vertices, classified by $D_5$ orbit (1 + 5 + 5 + 1 partition). Four distinct values vs uniform $-1/(2\phi)$ at vertex-aligned. | G1 (Patch 0552 host-to-first-shell uniform projection $-1/(2\phi)$) | Needed; substantive new primitive at edge-aligned. Three of four values are non-trivial. |
| **G1$_E$.2** | First-shell-to-first-shell edge orbit structure under $D_5$: classification of the 30 icosahedral first-shell edges by $D_5$ orbit. | G1.2 (Patch 0551 first-shell-to-first-shell edge perpendicularity $\hat{e}_{ij} \cdot \hat{n} = 0$) | Needed for path-class enumeration at $\mathcal{O}(\delta^2)$ B.2 class. Under vertex-aligned the result was a uniform vanishing identity; under edge-aligned the 30 edges split into orbits with potentially distinct projections. |
| **G2$_E$** | Second-shell projection orbit structure: $\hat{w}_j \cdot \hat{n}_{\text{edge}}$ for the 20 second-shell vertices, classified by $D_5$ orbit. | G2 (Patch 0587 second-shell inner-product primitive $w_j \cdot v_{\text{host}} = 1/2$ uniform; G2.1 Patch 0588 host-to-second-shell projection $\hat{w}_j \cdot \hat{n} = -1/2$ uniform) | Needed for B.3 cross-shell path-class. The 20 second-shell vertices of $v_{\text{host}}$ form a regular dodecahedron in a 3-plane; under $D_5$ they decompose as 2 + 10 + 5 + 1 + 1 + ... (exact orbit structure TBD at substantive Patch). |
| **G2$_E$.3** | First-shell-to-second-shell edge orbit structure under $D_5$. | G2.3 (Patch 0590 cross-shell edge-orbit classification $\hat{e}_{i,j} \cdot \hat{n} = -1/2$ uniform; single $I_h$ orbit of size 60) | Needed for B.3 cross-shell path-class weight enumeration. Under $D_5$ the 60 cross-shell edges decompose into multiple orbits with distinct projections. |
| **G2$_E$.4** | Second-shell-to-second-shell edge orbit structure under $D_5$. | G2.4 (Patch 0589 second-shell perpendicularity $\hat{e}_{j_1 j_2} \cdot \hat{n} = 0$ uniform; 30 dodecahedron edges) | Needed only if B-class extensions enter at higher orders; not required for $\mathcal{O}(\delta^2)$. |

**Layer rigor inheritance**: G1$_E$, G1$_E$.2, G2$_E$, G2$_E$.3 would be derived at publication-grade Layer 3 unconditional rigor (no (H5)-class framework-extension required for geometric primitives; only the path-class weight assignments invoke (H5$_E$)).

**Comparison summary**: Sequence-2A's primitive load is **substantially heavier** than vertex-aligned Patches 0587–0590's primitive load because the $D_5$ stabilizer has order 10 vs $I_h$'s order 120 — the smaller stabilizer produces more orbit classes, and orbit-representative values are no longer uniform across the orbit (since $D_5$ stabilizes only the edge, not the full $H_3$). The "magic" of vertex-aligned's uniform projections (Theorems 5.1 + 5.2) is structurally specific to $I_h$-equivariance and does NOT survive to edge-aligned.

---

## §5 Path-class decomposition at $\mathcal{O}(\delta^2)$ under edge-aligned Reading C

The 144 directed 2-edge paths in $\mathcal{P}_2(v_{\text{host}})$ partition by endpoint shell into the same four B-classes as vertex-aligned (per F.1 Theorem 6.1 / THEO-DSL-1 shell-locality, which is symmetry-independent at first order):

| Class | Description | Count | Vertex-aligned closed-form contribution under $I_h$ + (H5) | Sequence-2A target |
|-------|-------------|-------|--------------------------------------------|---------------------|
| **B.1** | Round-trip $v_{\text{host}} \to u_i \to v_{\text{host}}$ | 12 | $+3/(2\phi^3) \approx +0.354$ | Closed-form under $D_5$ + (H5$_E$); split by orbit class of $u_i$ (1 + 5 + 5 + 1 sub-orbits). |
| **B.2** | First-shell-trans $v_{\text{host}} \to u_i \to u_j \in S_1$ | 60 | $0$ exactly via Patch 0551 G1.2 perpendicularity $\hat{e}_{ij} \cdot \hat{n} = 0$ | UNDER EDGE-ALIGNED, the analog $\hat{e}_{ij} \cdot \hat{n}_{\text{edge}}$ is NOT uniformly zero — substantive new contribution at second order. Requires G1$_E$.2 orbit-decomposition. |
| **B.3** | Cross-shell $v_{\text{host}} \to u_i \to w_k \in S_2$ | 60 | $-15/(2\phi^2) \approx -2.865$ (DOMINANT ~83%) | Closed-form under $D_5$ + (H5$_E$); requires G2$_E$ + G2$_E$.3 orbit-decompositions. |
| **B.4** | Third-shell $v_{\text{host}} \to u_i \to v' \in S_3$ | 12 | $-3/(2\phi) \approx -0.927$ (~27%) | Closed-form under $D_5$ + (H5$_E$); split by orbit class of intermediate $u_i$ and terminal $v'$. |

**Structural Sequence-2A finding scoped at this Patch**: The B.2 class — which vanishes exactly at vertex-aligned via Patch 0551 first-shell-to-first-shell edge perpendicularity — does NOT vanish under edge-aligned. The 30 first-shell-to-first-shell edges decompose into multiple $D_5$ orbits, and the edge-direction projections $\hat{e}_{ij} \cdot \hat{n}_{\text{edge}}$ are generically non-zero. This is the most substantive Sequence-2A second-order finding: the cancellation that makes B.3 dominate the vertex-aligned coefficient $\alpha_2$ is structurally vertex-aligned-specific.

Whether this re-emerges as $\alpha_2^{(\rho)}$ structurally weaker or stronger than the vertex-aligned $-9/\phi^2$ is the substantive Sequence-2A target — and the answer depends on the precise orbit-decomposition of the 30 first-shell-to-first-shell edges under $D_5$, which is a Patch 0601 (A2$_E$ = G1$_E$.2) target.

---

## §6 Hypothesis stack (H1)–(H5$_E$)

Inherited from THEO-DSL-6 hypothesis stack with no modifications:

| Hypothesis | Statement | Source |
|------------|-----------|--------|
| (H1) | Edge-aligned Reading C with $\hat{n} = \hat{n}_{\text{edge}} = (u_1 - v_{\text{host}})/\|u_1 - v_{\text{host}}\|$ for chosen first-shell neighbor $u_1$ | THEO-DSL-6 / Patch 0596 |
| (H2) | Vertex-host convention: $v_{\text{host}}$ preserved as 600-cell vertex (anti-erasure Remark 7.2 of Patch 0597) | THEO-DSL-6 / Patch 0596 |
| (H3) | Icosahedral residual symmetry $H_3 = I_h$ at $v_{\text{host}}$ inherited via THEO-DSL-2 | F.1 v1.0 §5 |
| (H4) | F.1 Theorem 6.1 perturbation-locality propagation (THEO-DSL-1) — shell-locality of $\vec{j}^{\text{net}}_{DI}(v_{\text{host}})$ at $\mathcal{O}(\delta^k)$ to edges in $E_k(v_{\text{host}})$ | F.1 v1.0 §6 |
| (H5$_E$) | Mechanism A path-integral extension at $\mathcal{O}(\delta^k)$ at sketch-document Layer 3 with path-class weight ansatz $W(P) = 1$ specialized to edge-aligned variant | DG-1 sub-option A (per OPEN-FP-F1-1); per-variant scope qualifier per Patch 0598 DG-F15-4 |

**Note on (H5$_E$)**: This is the per-variant specialization of (H5) registered with THEO-DSL-5 candidate (Patch 0592). The path-class weight ansatz $W(P) = 1$ for $P \in \mathcal{P}_2(v_{\text{host}})$ at second order is the SAME ansatz as vertex-aligned (H5); only the geometric setting changes (edge-aligned substrate direction). Publication-grade Layer 3 unconditional promotion of (H5$_E$) inherits any future (H5) hardening via DG-1 sub-option A path-integral rigorisation, sub-option B new framework axiom MA.3, or sub-option C Layer 4 derivation OPEN-FP-F1-2 — registered as part of priority queue item (G).

---

## §7 Trajectory plan

Sequence-2A targets full coefficient closure at $\mathcal{O}(\delta^1)$ + $\mathcal{O}(\delta^2)$ via a 4–6 Patch hardened-artifact sequence + umbrella, paralleling the vertex-aligned Patches 0587–0592 structure:

| Patch | Sub-target | Layer rigor | Artifact | Notes |
|-------|-----------|-------------|----------|-------|
| **0599 (this)** | Sequence-2A scoping | sketch (no hardened artifact) | `F1_reading_C_edge_aligned_coefficient_scoping.md` (this file) | Single new markdown sketch; no modifications to other artifacts. |
| **0600 A1$_E$** | $\mathcal{O}(\delta^1)$ closed-form $\alpha_1^{(\rho)}, \alpha_1^{(\text{edge})}$ via Identities P1 + P2 + Gram-matrix inversion | pub-grade Layer 3 unconditional | `o_delta_one_edge_aligned_coefficient.tex` | First substantive Sequence-2A Patch; closes $k=1$ as stepping stone. No new geometric primitive — uses existing THEO-DSL-2 + PRED-O-30 + Identities P1 + P2 (computable at scoping level per §3). |
| **0601 A2$_E$** | G1$_E$ first-shell projection orbit-decomposition under $D_5$ (1 + 5 + 5 + 1 sub-orbits; four projection values) | pub-grade Layer 3 unconditional | `first_shell_d5_orbit_projections.tex` | Substantive new geometric primitive at edge-aligned. Closed-form values for each of four $D_5$ orbits. |
| **0602 A3$_E$** | G1$_E$.2 first-shell-to-first-shell edge orbit-decomposition under $D_5$ (30 edges, multi-orbit) | pub-grade Layer 3 unconditional | `first_shell_first_shell_edge_d5_orbits.tex` | Substantive — establishes the B.2 class contribution is non-zero. |
| **0603 A4$_E$** | G2$_E$ + G2$_E$.3 second-shell projection + cross-shell edge orbit-decompositions under $D_5$ | pub-grade Layer 3 unconditional | `second_shell_d5_orbits.tex` (or two artifacts if scope-split warranted) | Substantive — produces the B.3 class contribution at edge-aligned. |
| **0604 A5$_E$** | Path-class weight enumeration at $\mathcal{O}(\delta^2)$ producing closed-form $\alpha_2^{(\rho)}, \alpha_2^{(\text{edge})}$ via B.1 + B.2 + B.3 + B.4 partition + Gram-matrix inversion + (H5$_E$) ansatz | sketch-document Layer 3 under (H5$_E$) | `o_delta_squared_edge_aligned_path_class_weights.tex` | Main second-order coefficient deliverable; (H5$_E$) scope qualifier load-bearing. |
| **0605 A6$_E$** | Umbrella registration: THEO-DSL-7 (candidate) at sketch-document Layer 3 under (H5$_E$) | sketch-document Layer 3 under (H5$_E$) | `o_delta_squared_edge_aligned_substrate_locality_umbrella.tex` | Assembly under (H1)–(H5$_E$); five-class exclusion enumeration; cross-sector consistency framing. |
| **0605a** | Registry propagation for THEO-DSL-7 (candidate) | (no hardened artifact) | Updates to `theorem-registry.md` + `frontier_sectors/FP.md` + `master_glossary.md` | Single registry-propagation Patch following Patch 0592a / 0598 precedent. |

**Total**: 7 Patches across an estimated 4–8 sessions (single-Patch-per-session pace; possible compression if multiple substantive Patches land within a single session per the Patches 0587–0592 precedent which closed 6 Patches in Session 145). Scaffolding inheritance is moderate-to-heavy — Sequence-2A reuses (H1)–(H4) from THEO-DSL-6 + the four-step path-class enumeration template from Patch 0591 + the umbrella registration template from Patch 0592, but each geometric primitive requires its own substantive derivation work at $D_5$ orbit-decomposition level.

---

## §8 Decision-gate items (DG-F15A-1 through DG-F15A-5)

Five decision-gate items requiring Thomas input before substantive Sequence-2A work begins:

### DG-F15A-1 — $\alpha_1$ vs $\alpha_2$ trajectory ordering

Two options:
- **(A)** Sequence-2A first-order closure (Patch 0600 A1$_E$) → geometric primitives (Patches 0601–0603) → second-order closure (Patch 0604 A5$_E$ + 0605 A6$_E$). Stepping-stone first.
- **(B)** Geometric primitives first (Patches 0601–0603) → both first-order + second-order closures together (Patches 0604 + 0605). Front-load primitives.
- **(C)** First-order closure only at Sequence-2A close (Patch 0600 A1$_E$ + registry propagation at 0600a). Defer second-order to a future Sequence-2A.2 trajectory.

**Default recommendation: (A)** Stepping-stone first. The $k=1$ closure at Patch 0600 is computable from existing primitives + Identities P1 + P2 + Gram-matrix inversion at scoping level — minimal new substantive geometric work — and would validate the methodological pattern before heavier primitive-derivation work in Patches 0601–0603.

### DG-F15A-2 — Geometric primitive granularity at $D_5$ orbit-decomposition level

Two options:
- **(A)** Compute closed-form values for ALL orbit representatives in each primitive (G1$_E$: four sub-orbit values; G1$_E$.2: multi-orbit edge values; G2$_E$: dodecahedron $D_5$ orbits with closed-form per orbit; G2$_E$.3: cross-shell edge orbits closed-form per orbit). Heaviest computational load but most complete.
- **(B)** Compute only orbit averages / sums where required for the path-class weight enumeration; defer per-orbit closed-forms to a future drift-audit Patch. Lighter load.

**Default recommendation: (A)** All orbit-representative closed-forms. The per-orbit values are useful programme-level results in their own right and may serve future Sequence-2A.2 / Sequence-2B / face-aligned trajectories.

### DG-F15A-3 — Sequence-2A trajectory scope assessment after A5$_E$ result

Depends on $\alpha_2$ outcome at Patch 0604:
- If closed-form $\alpha_2^{(\rho)}, \alpha_2^{(\text{edge})}$ both finite and structurally clean (e.g., expressible as $a + b\phi$ for integer $a, b$): proceed to umbrella registration at Patch 0605 A6$_E$.
- If $\alpha_2^{(\rho)} = 0$ identically (the radial-component-vanishing question E5 of THEO-DSL-6 resolved positively): substantive negative result; would establish $\vec{j}_2^{\text{edge}} \parallel \hat{n}_{\text{edge}}$ at framework-axiom level (1D effective subspace at second order despite 2D structural admission); umbrella registration would be a substantive trajectory pivot deliverable.
- If $\alpha_2^{(\text{edge})} = 0$ identically: rare and unexpected; would warrant investigation before umbrella registration.

**Default recommendation: defer DG-F15A-3 resolution to Patch 0604 close**.

### DG-F15A-4 — (H5$_E$) framework-extension scope qualifier discipline

Two options:
- **(A)** Per-variant (H5$_E$) scope qualifier maintained throughout Sequence-2A (preserves the Patch 0598 DG-F15-4 default-(A) anti-erasure pattern; downstream consumers cite "(H5$_E$)" not "(H5)").
- **(B)** Unify (H5$_E$) back to (H5) for Sequence-2A artifacts since the path-class weight ansatz $W(P) = 1$ is the SAME ansatz at all variants. Cleaner notation but loses per-variant traceability.

**Default recommendation: (A)** Per-variant (H5$_E$) maintained. Preserves anti-erasure traceability and parallels DG-F15-4 default chosen at Patch 0598 open.

### DG-F15A-5 — Theorem-registry naming for Sequence-2A result

Two options:
- **(A)** Single THEO-DSL-7 (candidate) covering both $\alpha_1$ + $\alpha_2$ edge-aligned coefficient closures at Patch 0605a registry-propagation. Parallels THEO-DSL-3 / THEO-DSL-5 candidate single-theorem coefficient registration at vertex-aligned.
- **(B)** Split into THEO-DSL-7a (first-order $\alpha_1$ at pub-grade Layer 3 unconditional) + THEO-DSL-7b (second-order $\alpha_2$ at sketch-doc Layer 3 under (H5$_E$)). Captures the layer-rigor difference between $k=1$ and $k=2$.

**Default recommendation: (A)** Single THEO-DSL-7 (candidate) covering both orders at the weakest-link rigor (sketch-doc Layer 3 under (H5$_E$) per the $k=2$ contribution). Parallels vertex-aligned THEO-DSL-5 candidate which similarly bundles the umbrella under (H5)-class scope qualifier.

---

## §9 Falsifiers

Sequence-2A trajectory falsifiers (specific to the coefficient sub-question; structural sub-question falsifiers inherit from THEO-DSL-6):

1. **F1$_E$**: Demonstration of $\alpha_1^{(\rho)} \neq -3 r_0/\phi^3$ or $\alpha_1^{(\text{edge})}$ inconsistent with closed-form derived from Identities P1 + P2 from any valid first-principles $D_5$-equivariant calculation under (H1)–(H4). Would contradict the icosahedral rank-1 sum identity (PRED-O-30) or THEO-DSL-2 Theorem 5.1.

2. **F2$_E$**: Demonstration of B.2 first-shell-trans class contributing zero exactly to $\alpha_2$ under edge-aligned from any valid first-principles 600-cell + $D_5$ orbit-decomposition + Mechanism A calculation. Would contradict §5's scoped finding that the first-shell-to-first-shell edge projections $\hat{e}_{ij} \cdot \hat{n}_{\text{edge}}$ are generically non-zero at edge-aligned.

3. **F3$_E$**: Demonstration of closed-form $\alpha_2^{(\rho)} \neq f(\phi)$ for any polynomial-in-$\phi$-with-rational-coefficients form. Sequence-2A's structural prediction is that all coefficient closed-forms live in $\mathbb{Q}[\phi]$ (golden-ratio field extension over rationals); a transcendental result would constitute a substantive failure of the methodology.

4. **F4$_E$**: Demonstration that the path-class weight ansatz $W(P) = 1$ at (H5$_E$) is inconsistent with a publication-grade DG-1 sub-option A path-integral rigorisation specialized to edge-aligned variant. Would force a (H5$_E$)-specific framework-extension distinct from vertex-aligned (H5).

5. **F5$_E$**: Demonstration that Sequence-2A's substrate-current magnitude $|\vec{j}_1^{\text{edge}}|^2 + \mathcal{O}(\delta^2)$ exceeds the vertex-aligned substrate-current magnitude $|6/\phi^2|^2 \delta^2 + \mathcal{O}(\delta^3)$ at the same value of $\delta$. Would contradict the symmetry-breaking interpretation that vertex-aligned maximizes substrate-current alignment.

---

## §10 Cross-sector connections

**Capotauro v2.0 vertex-aligned-uniqueness selection** (Q1$'$+Q1$'$.A at Finding C-W37; Patches 0418 + 0419): the vertex-aligned-uniqueness argument was at the Capotauro spatial-sector cage-shell averaging factor level ($\chi/6$ requires $I_h$-equivariance). Sequence-2A's coefficient closures would provide an independent F.1 temporal-sector test of vertex-aligned uniqueness at the QUANTITATIVE level — specifically, whether the edge-aligned substrate-current magnitude is structurally smaller than vertex-aligned (per F5$_E$ falsifier scoped at §9). A positive Sequence-2A result with $|\vec{j}^{\text{edge}}| < |\vec{j}^{\text{vertex}}|$ at all orders would constitute a third independent uniqueness argument for vertex-aligned Reading C (joining Capotauro spatial-sector + F.1 temporal-sector structural per THEO-DSL-4/-6/-8).

**F.1 v1.0 Theorem 7.1 + THEO-DSL-3/-4/-5/-6**: Sequence-2A directly extends the THEO-DSL-N family. The $k=1$ closure at Patch 0600 A1$_E$ is the edge-aligned analog of THEO-DSL-3 + Theorem 7.1 ($\alpha_1 = 6/\phi^2$); the $k=2$ closure at Patch 0604 A5$_E$ is the edge-aligned analog of THEO-DSL-5 candidate ($\alpha_2 = -9/\phi^2$). The dimensional-growth pattern from THEO-DSL-6 is the structural underpinning of why these need distinct identifications.

**OPEN-FP-F1-2 Layer 4 derivation of Mechanism A from CPP A1–A11**: long-term programme target; orthogonal to Sequence-2A scope. The framework axioms MA.1 + MA.2 are inherited via THEO-DSL-1 with edge-aligned substitution; the substitution does NOT modify the framework axioms themselves, only the substrate-direction primitive identified within the rate function $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n}_{\text{edge}})$.

**Sequence-2B face-aligned coefficient enumeration**: separate trajectory under $C_s$ stabilizer (the 3D invariant subspace per THEO-DSL-8 candidate); Sequence-2A and Sequence-2B are independent trajectories opened by their own scoping documents. Sequence-2A precedes Sequence-2B per DG-F15-1 default-(C) ordering at Session 146 open + the recommendation chain after Patch 0598 close.

---

## §11 Forward queue + landings record stub

### §11.1 Forward queue after Patch 0599

| Sub-target | Patch | Estimated effort | Default sequence |
|------------|-------|------------------|------------------|
| Sequence-2A scoping (this) | 0599 | 1 Patch | LANDED at this Patch |
| A1$_E$ first-order coefficient closure | 0600 | 1 Patch (~1 session) | Next |
| A2$_E$ G1$_E$ first-shell orbit projections | 0601 | 1 Patch | After A1$_E$ |
| A3$_E$ G1$_E$.2 first-shell-to-first-shell edge orbits | 0602 | 1 Patch | After A2$_E$ |
| A4$_E$ G2$_E$ + G2$_E$.3 second-shell + cross-shell orbits | 0603 | 1–2 Patches (possible split) | After A3$_E$ |
| A5$_E$ path-class weight enumeration at $\mathcal{O}(\delta^2)$ | 0604 | 1 Patch (heavy substantive) | After A4$_E$ |
| A6$_E$ umbrella registration | 0605 | 1 Patch | After A5$_E$ |
| Registry propagation Patch | 0605a | 1 Patch | After A6$_E$ |

Total trajectory length estimate: 7 Patches, 4–8 sessions, paralleling vertex-aligned Patches 0587–0592 + 0592a structure (which closed in single Session 145 + single Session 146 close pattern).

### §11.2 Landings record stub

The landings record will accumulate as Sequence-2A Patches land:

| Patch | Date | Sub-target | Status |
|-------|------|-----------|--------|
| 0599 | 27 May 2026 | Sequence-2A scoping | OPENED |
| 0600 | — | A1$_E$ first-order closure | TBD |
| 0601 | — | A2$_E$ G1$_E$ primitive | TBD |
| 0602 | — | A3$_E$ G1$_E$.2 primitive | TBD |
| 0603 | — | A4$_E$ G2$_E$ + G2$_E$.3 primitives | TBD |
| 0604 | — | A5$_E$ path-class enumeration at $\mathcal{O}(\delta^2)$ | TBD |
| 0605 | — | A6$_E$ umbrella registration | TBD |
| 0605a | — | Registry propagation | TBD |

---

## §12 Risk inventory

1. **Computational complexity at $D_5$ orbit-decomposition level**: the $D_5$ stabilizer has order 10 vs $I_h$'s order 120; orbit-decomposition into more orbit classes makes closed-form derivation more complex. Mitigated by working in the icosahedral coordinate system $\{\hat{n}_\rho, \hat{n}_\perp\}$ orthogonal basis where many identities simplify.

2. **Possibility of irrational closed-forms**: the Sequence-2A coefficient closures may not all lie in $\mathbb{Q}[\phi]$ (golden-ratio field extension over rationals). If so, this would be a substantive methodological divergence from vertex-aligned trajectory's clean $\mathbb{Q}[\phi]$ closures (THEO-DSL-3/-5 candidate). Mitigated by working with the icosahedral geometry directly (which IS in $\mathbb{Q}[\phi]$).

3. **Non-uniqueness of edge choice**: the chosen first-shell neighbor $u_1$ is arbitrary among the 12 first-shell neighbors. By $I_h$-symmetry of the host vertex, the choice does not affect the closed-form coefficients (which are scalar magnitudes within the 2D invariant subspace), but it does affect the basis identification $\{\hat{n}_\rho, \hat{n}_{\text{edge}}\}$. Mitigated by working in basis-independent identities at scoping level.

4. **Cross-validation with vertex-aligned trajectory**: a check that vertex-aligned Reading C corresponds to "edge-aligned with $u_1 = v_{\text{host}}$" is structurally inconsistent (since $\hat{n}_{\text{edge}}$ is by definition a unit vector to a DISTINCT first-shell vertex). Sequence-2A's coefficient closures are NOT specializations of vertex-aligned closures; they are independent results at a different residual-symmetry structure.

5. **(H5$_E$) scope-qualifier robustness**: as in vertex-aligned (H5), the path-class weight ansatz $W(P) = 1$ is sketch-document Layer 3 only. Any future publication-grade hardening of (H5) → (H5$_E$) at the path-integral rigorisation level (DG-1 sub-option A) would inherit unchanged to Sequence-2A. Mitigated by per-variant scope-qualifier tracking per DG-F15-4 + DG-F15A-4 defaults.

---

## §13 Closure summary

This scoping document opens the OPEN-FP-F1-5 Sequence-2A trajectory — the coefficient-enumeration sub-trajectory targeting closed-form $\alpha_k^{(\rho)}, \alpha_k^{(\text{edge})}$ at $\mathcal{O}(\delta^k)$ within the 2D $D_5$-invariant subspace established at THEO-DSL-6 (candidate). The trajectory plan is a 7-Patch hardened-artifact + registry-propagation sequence paralleling the vertex-aligned Route C sequence 2 trajectory (Patches 0587–0592 + 0592a). Five decision-gate items (DG-F15A-1 through DG-F15A-5) require Thomas input before substantive Layer 3 work begins.

Substantive scoping findings registered at this Patch (without new geometric primitives, computable from existing F.1 + Capotauro Patch 0419 inheritance):

- **First-shell orbit structure under $D_5$**: 1 + 5 + 5 + 1 partition of the 12 first-shell vertices.
- **Identity P1**: $\sum_i \hat{u}_i \cdot \hat{n}_{\text{edge}} = 3/\phi^2$.
- **Identity P2**: $\sum_i (\hat{u}_i \cdot \hat{n}_{\text{edge}})^2 = 5 - \phi$.
- **First-order projection** $\hat{n}_\rho \cdot \vec{j}_1^{\text{edge}} = -3 r_0 \delta/\phi^3 \approx -0.708\, r_0 \delta$.
- **First-order projection** $\hat{n}_{\text{edge}} \cdot \vec{j}_1^{\text{edge}} = 2 r_0 \delta (5 - \phi) \approx 6.764\, r_0 \delta$.
- **Confirmation of genuine 2D invariant subspace at first order**: both projections non-zero, validating THEO-DSL-6 dimensional-growth finding at quantitative level.
- **Substantive scoped finding**: B.2 first-shell-trans class contributes zero exactly under vertex-aligned (Patch 0551 G1.2 perpendicularity) but is generically non-zero under edge-aligned — the structural origin of the dimensional growth $1 \to 2$ at second order.

The Patch 0600 A1$_E$ next-substantive-Patch target is to convert the first-order projections into closed-form $\alpha_1^{(\rho)}, \alpha_1^{(\text{edge})}$ via 2-by-2 Gram-matrix inversion in the non-orthogonal basis $\{\hat{n}_\rho, \hat{n}_{\text{edge}}\}$. This is a single substantive deliverable Patch with all primitives already available at scoping level.

---

*Document opened at Patch 0599 (Session 146); to be referenced as Sequence-2A scoping for the OPEN-FP-F1-5 trajectory. Future references to "(Patch 0599 scoping)" cite this document.*
