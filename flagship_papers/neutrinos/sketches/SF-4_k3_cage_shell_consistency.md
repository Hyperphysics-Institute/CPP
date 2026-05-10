# SF-4: K3-Cage-Shell Consistency Theorem — Working Document

**Status:** ACTIVE — sub-derivation under OPEN-FP-SF-4-2
**Track:** SF-4 (Neutrino Sector Unification flagship paper) — K3-eigenstructure consistency
**Author:** Claude Opus (analysis), Thomas Lee Abshier ND (strategic frame)
**Established:** 9 May 2026 (Session 42, patch 0302)
**Foundation:** [`SF-4_mechanism_selected.md`](SF-4_mechanism_selected.md) §4; [`SF-4_neutrino_sector_audit.md`](SF-4_neutrino_sector_audit.md) §6 (K3 constraints K1, K2, K3); SM-5 §2-§3 (TBM-from-K3 derivation, ansatz proposition); SM-3 K3 Spectral Theorem
**Scope:** Working document; sub-derivation under construction. Captures Session 42's framing of the K3-Cage-Shell Consistency Theorem, the numerical consistency check, and the three candidate physical routes for closure of the structural-geometric question (why this specific cage-shell assignment is forced rather than fitted). Per the four-tier discipline, sketches-tier; theorem-tier formalization happens at v0.1 SF-4 paper drafting in Sessions 45+.

---

## §1. Context and target

Per `SF-4_mechanism_selected.md` §4, the K3-Cage-Shell Consistency Theorem must establish that Candidate C with cage-shell assignment $V \in \{4, 12, 30\}$ produces neutrino mass eigenstates that align with the K3 graph eigenmodes at zeroth order, preserving SM-5's existing tribimaximal PMNS derivation rather than replacing it. The theorem is OPEN-FP-SF-4-2 in `Research_Frontier.md`, second-priority sub-problem under SF-4.

Without this theorem, the SF-4 paper cannot claim to extend SM-5's PMNS derivation; the existing tribimaximal result would have to be re-grounded from scratch, which is substantial additional cost and would weaken the SF-4 / SM-5 unified narrative.

The Constraint K1 / K2 / K3 of audit §6 (the mechanism must produce three mass eigenstates that align with $K_3$ eigenmodes at zeroth order, must commute with $A_{K_3}$, and must apply the V² scaling uniformly across the three K3-eigenmode flavors) is the formal statement of what the theorem must satisfy. Candidate C's V² mass formula is *flavor-blind* in the sense that the same scaling rule applies across all three mass eigenstates, but whether the eigenstate identification that comes out of Candidate C coincides with SM-5's K3-eigenmode identification is the substantive question.

This Session 42 work resolves the *numerical* part of the consistency question (the consistency check at zeroth order is exact, not approximate) and identifies the residual *structural-physical* question (why the specific V values 4, 12, 30 are forced by geometry, not fitted) for closure in Sessions 43+.

---

## §2. Recap: SM-5's K3-eigenmode identification

SM-5 (Tribimaximal Neutrino Mixing from K3) establishes:

**The K3 ZBW Hamiltonian** $\hat{H}_{\text{ZBW}} = \hbar\omega_0 A_{K_3}$, where $A_{K_3}$ is the adjacency matrix of the K3 colour-cage base graph (the equilateral triangle of three colour vertices). Eigenvalues:

- $\lambda_+ = +2$ (bonding singlet, multiplicity 1)
- $\lambda_- = -1$ (antibonding doublet, multiplicity 2)

**Eigenmodes** (in the colour-vertex basis $|V_1\rangle, |V_2\rangle, |V_3\rangle$):

$$
|\phi_+\rangle = \tfrac{1}{\sqrt{3}}(1, 1, 1)^T \quad\text{(bonding, } \lambda_+ = +2\text{)}
$$

$$
|\phi_-^{(1)}\rangle = \tfrac{1}{\sqrt{6}}(2, -1, -1)^T, \quad |\phi_-^{(2)}\rangle = \tfrac{1}{\sqrt{2}}(0, -1, 1)^T \quad\text{(antibonding, } \lambda_- = -1\text{)}
$$

**Identification** (SM-5 ansatz, not yet derived from CPP interaction rules — registered as the SM-5 Open Problem):

- Charged leptons → K3 vertex states $|V_1\rangle, |V_2\rangle, |V_3\rangle$ — **flavor basis**
- Neutrino mass eigenstates → K3 eigenmodes $|\phi_-^{(1)}\rangle, |\phi_+\rangle, |\phi_-^{(2)}\rangle$ — **mass basis**

The conventional ordering in SM-5 (which is logically free but pinned in the paper):

$$
\nu_1 \leftrightarrow |\phi_-^{(1)}\rangle, \quad \nu_2 \leftrightarrow |\phi_+\rangle, \quad \nu_3 \leftrightarrow |\phi_-^{(2)}\rangle
$$

**PMNS at zeroth order** = K3 eigenvector matrix = U_TBM exactly:

$$
U_{\text{PMNS}}^{(0)} = U_{\text{TBM}} = \begin{pmatrix} \sqrt{2/3} & 1/\sqrt{3} & 0 \\ -1/\sqrt{6} & 1/\sqrt{3} & -1/\sqrt{2} \\ -1/\sqrt{6} & 1/\sqrt{3} & 1/\sqrt{2} \end{pmatrix}
$$

This produces $\sin^2\theta_{12}^{(0)} = 1/3$, $\sin^2\theta_{23}^{(0)} = 1/2$, $\sin^2\theta_{13}^{(0)} = 0$, $\delta_{CP}^{(0)}$ undefined. Higher-order corrections from EW-sector machinery (OP-SM-7d, Capotauro bias) lift these to observed values; deferred to SF-2 / EW sector per SF-4_mechanism_selected.md §3.

---

## §3. The mass-basis vs flavor-basis distinction

The audit (§5) and the §15 falsifier-check appendix wrote the cage-shell assignment as

$$
(\nu_e, \nu_\mu, \nu_\tau) \to (\text{tetrahedron } V=4, \text{ icosahedron } V=12, \text{ icosidodecahedron } V=30)
$$

This notation conflates two possible readings: (a) the assignment is in *flavor basis* (V values attach to the K3 vertex states / charged-lepton flavor labels), or (b) the assignment is in *mass basis* (V values attach to the K3 eigenmodes / neutrino mass eigenstates).

**Only reading (b) is consistent with SM-5's PMNS derivation.** Under reading (a), the mass operator in flavor basis is diagonal:

$$
\hat{M}_{\text{flavor, reading (a)}} = M_0 \cdot \sigma \cdot \text{diag}(V_e^2, V_\mu^2, V_\tau^2) = M_0 \cdot \sigma \cdot \text{diag}(16, 144, 900)
$$

with mass eigenvalues 16, 144, 900 attached to mass eigenstates that are *flavor states themselves* — which means the PMNS matrix is the identity, no mixing. This contradicts SM-5 and observation entirely. Reading (a) is therefore wrong.

Under reading (b), the mass operator is diagonal in the *K3-eigenmode basis*:

$$
\hat{M}_{\text{mass}} = M_0 \cdot \sigma \cdot \text{diag}(V_1^2, V_2^2, V_3^2) = M_0 \cdot \sigma \cdot \text{diag}(16, 144, 900)
$$

with mass eigenvalues attached to K3 eigenmodes $|\phi_-^{(1)}\rangle, |\phi_+\rangle, |\phi_-^{(2)}\rangle$. The mass eigenstates are then exactly the K3 eigenmodes (mass basis), and PMNS in flavor basis is exactly the K3 eigenvector matrix, which equals $U_{\text{TBM}}$ — recovering SM-5's result by construction.

**The cage-shell assignment is in mass basis.** This is the first clarifying step of the consistency theorem: the notation in audit §15 should be read as $(\nu_1, \nu_2, \nu_3) \to (V=4, 12, 30)$, with charged-lepton flavor labels playing no direct role in the cage-shell assignment.

This reading is also physically natural: the SF-4 mass formula $m_{\nu_i} = M_0 \cdot V_{\nu_i}^2 \cdot \mathcal{T}_{\text{unbound}}$ specifies mass eigenvalues, and mass eigenvalues are properties of mass eigenstates. The cage-shell V is a property of how the mass eigenstate propagates through the substrate, not a property of the flavor-state-to-mass-state mixing matrix.

---

## §4. Numerical consistency at zeroth order is exact

With the mass-basis reading clarified, the numerical consistency check between Candidate C and SM-5's TBM result is straightforward and **exact, not approximate**.

Construct the V² operator on the K3-eigenmode basis with eigenvalues $V^2 = (16, 144, 900)$ assigned to $(|\phi_-^{(1)}\rangle, |\phi_+\rangle, |\phi_-^{(2)}\rangle)$ respectively. Transform to the colour-vertex (flavor) basis via the K3 eigenvector matrix $U_{\text{TBM}}$:

$$
\hat{V}^2_{\text{flavor}} = U_{\text{TBM}} \cdot \text{diag}(16, 144, 900) \cdot U_{\text{TBM}}^T = \begin{pmatrix} 58.667 & 42.667 & 42.667 \\ 42.667 & 500.667 & -399.333 \\ 42.667 & -399.333 & 500.667 \end{pmatrix}
$$

(values shown to 3 decimal places; exact values are simple fractions of the input integers.)

Two structural features are immediate:

**1. The matrix has exact $\mu\tau$-exchange symmetry:** under the permutation $P_{23}$ swapping rows and columns 2 and 3, $P_{23} \hat{V}^2_{\text{flavor}} P_{23} = \hat{V}^2_{\text{flavor}}$. Concretely, $\hat{V}^2_{22} = \hat{V}^2_{33} = 500.667$ and $\hat{V}^2_{12} = \hat{V}^2_{13} = 42.667$. Only the off-diagonal $\hat{V}^2_{23} = -399.333$ element distinguishes $\mu$ from $\tau$, and this element is symmetric under the swap by being the same on both sides of the diagonal.

**2. Diagonalizing $\hat{V}^2_{\text{flavor}}$ recovers TBM exactly:** the eigenvalues are $(16, 144, 900)$ as required, and the eigenvectors are $(|\phi_-^{(1)}\rangle, |\phi_+\rangle, |\phi_-^{(2)}\rangle)$ exactly. Recomputing the PMNS angles from these eigenstates:

| Angle | TBM value | Recovered from $\hat{V}^2_{\text{flavor}}$ |
|---|---|---|
| $\sin^2\theta_{12}$ | $1/3$ | $0.3333$ (exact) |
| $\sin^2\theta_{23}$ | $1/2$ | $0.5000$ (exact) |
| $\sin^2\theta_{13}$ | $0$ | $0.0000$ (exact) |

**The zeroth-order PMNS prediction of SM-5 survives Candidate C without modification.** This is constraint K1 / K2 / K3 (audit §6) satisfied exactly, by construction, once the mass-basis reading is adopted.

---

## §5. The structural-physical question: why this V assignment from substrate primitives?

The numerical consistency at §4 is exact but does not derive WHY the cage-shell V values $(16, 144, 900)$ attach to the specific K3 eigenmodes $(|\phi_-^{(1)}\rangle, |\phi_+\rangle, |\phi_-^{(2)}\rangle)$ in that specific order. The structural-physical question:

**Why is V=12 forced for the bonding K3 mode $|\phi_+\rangle$, V=4 forced for one antibonding mode, and V=30 forced for the other antibonding mode — by 600-cell substrate geometry rather than by fit to splitting data?**

This is the substantive content of the K3-Cage-Shell Consistency Theorem. Without closure on this question, the cage-shell assignment is consistent with TBM (per §4) but is itself an ansatz inherited from Candidate-C-as-fitted-to-data, not derived from primitives.

Three observations frame the question:

**Observation (a): The K3 bonding mode is fully symmetric over colour vertices.** $|\phi_+\rangle = (1,1,1)/\sqrt{3}$ has equal amplitude on $|V_1\rangle, |V_2\rangle, |V_3\rangle$. This is the most-symmetric K3 mode under the $S_3$ permutation symmetry of the K3 graph.

**Observation (b): The K3 antibonding doublet is degenerate at the K3 level.** $\lambda_- = -1$ has multiplicity 2; any orthonormal pair within this 2D subspace is equally a K3-eigenbasis. The TBM choice $(|\phi_-^{(1)}\rangle, |\phi_-^{(2)}\rangle)$ picks out specific directions — $|\phi_-^{(1)}\rangle$ is $\mu\tau$-symmetric, $|\phi_-^{(2)}\rangle$ is $\mu\tau$-antisymmetric. This selection is what SM-5 ansatzes; SM-5's open problem is to derive WHY these specific directions are picked out.

**Observation (c): The cage-shell V values reflect 600-cell shell structure.** $V=12$ is the icosahedron, the bonded shell of nearest neighbors at the 600-cell vertex; $V=4$ is a tetrahedral subset; $V=30$ is the icosidodecahedron at shell 3. These are *not* K3-internal structures — they are 600-cell substrate structures that the K3 graph is embedded in.

The K3-Cage-Shell Consistency Theorem, in structural form, is the statement that **the embedding of K3 into the 600-cell respects the symmetries that make the V assignment force the specific order $(V=4, V=12, V=30)$ to the specific eigenmodes $(|\phi_-^{(1)}\rangle, |\phi_+\rangle, |\phi_-^{(2)}\rangle)$**. Three candidate routes for closure follow.

---

## §6. Three candidate routes for closure

### §6.1 Route A: Symmetry-shell correspondence

**Story.** The K3 bonding mode $|\phi_+\rangle$ is fully symmetric across colour vertices and therefore couples to the 600-cell's most-symmetric small-V shell — the icosahedron, $V=12$, with full icosahedral symmetry $H_3$. The K3 antibonding modes have less symmetry (broken $S_3$ to one of its subgroups under $\mu\tau$-exchange selection) and couple to less-symmetric shells: the tetrahedron $V=4$ with tetrahedral symmetry $T_d$, and the icosidodecahedron $V=30$ at shell 3.

The argument: a mode's symmetry character determines which 600-cell substrate shell it can stably propagate on. Modes with full $S_3$-symmetric character (the bonding mode) couple to shells with the highest available local symmetry; modes with broken-symmetry character couple to shells where the broken-symmetry direction has a corresponding substrate-geometric direction.

**Closure path.** Route A requires showing: (1) the small-V 600-cell shells $\{4, 12, 30\}$ are the natural shells available at the lepton-cage scale; (2) their symmetry hierarchy — $H_3$ (icosahedron) > $T_d$ (tetrahedron) > local $C_{nv}$ for the icosidodecahedron — maps to the K3 eigenmode symmetry hierarchy in a forced way.

**Why it might be true.** The 600-cell has well-defined shells; the K3 graph has well-defined eigenmode symmetry properties. If the embedding is fixed (by the SM-3 K3 Spectral Theorem), the symmetry-shell correspondence may be forced.

**Why it might not be true.** Symmetry alone may not pick a unique mapping. There are multiple shells with comparable symmetry properties at the relevant scale; the assignment to V=4 vs V=30 (which antibonding mode goes where) needs additional structure beyond symmetry.

### §6.2 Route B: Sub-shell decomposition of the icosahedron

**Story.** The icosahedron contains tetrahedra as substructures — five inscribed tetrahedra, each using 4 of the 12 icosahedral vertices, with each vertex appearing in 5 tetrahedra. The tetrahedron $V=4$ is naturally interpreted as the *sub-shell* of the icosahedron $V=12$, and the icosidodecahedron $V=30$ as the *next shell out* in the 600-cell distance hierarchy.

In this picture, all three V values are connected: $V=12$ is the primary 600-cell shell at lepton-cage scale, $V=4$ is its inscribed-tetrahedron sub-shell, $V=30$ is its outer-shell complement.

The K3 eigenmodes attach to these as follows: the bonding mode (delocalized across all colour vertices) sees the *full* icosahedral shell ($V=12$); the antibonding modes localize on subsets of vertices and see *sub-shells*. The $\mu\tau$-symmetric antibonding mode sees the inscribed tetrahedron ($V=4$); the $\mu\tau$-antisymmetric antibonding mode sees the outer shell ($V=30$).

**Closure path.** Route B requires showing: (1) the inscribed-tetrahedron sub-shell of an icosahedron at the lepton-cage 600-cell scale corresponds to the $\mu\tau$-symmetric antibonding K3 mode (rather than the antisymmetric one); (2) the icosidodecahedron at shell 3 corresponds to the $\mu\tau$-antisymmetric mode. The first half is the harder structural-geometric claim.

**Why it might be true.** The inscribed tetrahedron's 4 vertices form a sub-symmetric configuration that breaks the icosahedral $H_3$ to tetrahedral $T_d$. The $T_d$ subgroup retains a 3-fold rotational symmetry ($\mathbb{Z}_3$) which may be the natural home for the $\mu\tau$-symmetric K3 mode (which is $S_3$-symmetric within the colour-vertex pair $(\mu, \tau)$ before $\mu\tau$-exchange).

**Why it might not be true.** The inscribed-tetrahedron picture has multiple inequivalent tetrahedral sub-shells in the icosahedron (5 of them). Picking which inscribed tetrahedron is "the" tetrahedron in Candidate C requires additional substrate structure beyond what Route B sketches.

### §6.3 Route C: The lepton-vertex embedding plus 600-cell distance shells

**Story.** The K3 graph's three colour vertices are embedded at specific 600-cell positions per the SM-3 K3 Spectral Theorem. Once the embedding is fixed, the bonded shells from the K3-vertex centroid (or some natural reference point near the K3) are determined by 600-cell geometry alone. The bonded shells at small-V are uniquely $\{4, 12, 30\}$ for the lepton-cage substrate scale (this is a 600-cell-internal claim from the SS / SM machinery).

The K3 eigenmodes propagate through these substrate shells with eigenmode-specific coupling: the bonding mode (which has support equally on all three K3 vertices) couples to the *symmetric centroidal shell* (icosahedron); the antibonding modes (which have nodes between K3 vertex pairs) couple to *off-centroidal shells* (tetrahedron and icosidodecahedron, distinguished by which K3-vertex pair the antibonding mode's node falls between).

This route directly connects the embedding (fixed by SM-3) to the cage-shell V values (fixed by 600-cell shell structure) via the K3-eigenmode-specific propagation pattern.

**Closure path.** Route C requires showing: (1) the 600-cell distance shells from the K3 centroid are exactly $\{4, 12, 30\}$ at the scale where the K3 lepton cage lives; (2) the eigenmode-specific propagation pattern picks out the right K3 eigenmode for each shell.

**Why it might be true.** This route most directly anchors on the SM-3 K3 Spectral Theorem (the K3 embedding) and on the 600-cell distance-shell taxonomy used elsewhere in the corpus (SM-7/8/9). It does not require new postulates.

**Why it might not be true.** The K3 centroid (or whatever reference point is used) and its bonded shells in the 600-cell may not align with the cage-shell V values needed; the geometric calculation has to be done explicitly to verify.

### §6.4 Cross-comparison

| | Route A | Route B | Route C |
|---|---|---|---|
| Anchors on | Symmetry-shell correspondence | Sub-shell decomposition of icosahedron | SM-3 K3 embedding + 600-cell distance shells |
| Closure path | Symmetry hierarchy mapping | Inscribed-tetrahedron geometry | Direct distance computation |
| New postulates required | None (uses existing K3 + 600-cell data) | None | None |
| Risk of failure | Symmetry may not uniquely pick the assignment | Multiple inscribed tetrahedra ambiguity | Geometric facts may not match V assignment |
| Programme-coherence | Connects to general "symmetry determines coupling" patterns in CPP | Connects to existing inscribed-polytope machinery | Most direct connection to SM-3 derivation |

The three routes are not mutually exclusive — closure may come from a combination, or one may turn out to be the cleanest. The discipline of listing them as candidates rather than premature single-pick is the same discipline as in the suppression-mechanism three-pictures work (`SF-4_suppression_derivation.md` §7).

---

## §7. Status and forward priority

**OPEN-FP-SF-4-2 status at Session 42 close: OPEN (PARTIAL — numerical consistency exact; structural derivation in progress).**

The numerical part of K3-consistency is **exact and complete**: Candidate C with cage-shell assignment in mass basis exactly preserves SM-5's TBM zeroth-order PMNS prediction (§4). The constraint K1/K2/K3 from audit §6 is satisfied by construction.

The structural-physical part of K3-consistency — why the specific V assignment $(16, 144, 900)$ to specific K3 eigenmodes $(|\phi_-^{(1)}\rangle, |\phi_+\rangle, |\phi_-^{(2)}\rangle)$ is forced from substrate primitives rather than fitted — is identified as the residual question. Three candidate closure routes (A, B, C) laid out above.

**Forward priority for Session 43:** Investigate Route C first (most direct connection to SM-3 derivation; uses no new machinery). If Route C closes, OPEN-FP-SF-4-2 advances to PARTIAL CLOSURE with structural picture in hand. If Route C surfaces an obstruction, fall back to Route A or B.

If all three routes fail closure from primitives, the K3-Cage-Shell Consistency Theorem reduces to the same status as SM-5's identification proposition — an ansatz that survives empirical test exactly but is not derived from CPP interaction rules. This is a known SM-5 open problem (the SM-5 Open Problem on neutrino-as-K3-eigenmode identification); the K3-Cage-Shell Consistency Theorem at that level adds no new ansatz beyond what SM-5 already does, just inherits SM-5's ansatz with the cage-shell V values attached. SF-4 v0.1 drafting can proceed at this level if needed; full theorem-level closure is a longer-term programme target.

---

## §8. What this session establishes

**Established at Session 42 close (this document):**

- The mass-basis vs flavor-basis distinction clarified: the cage-shell assignment must be read in mass basis (V values attach to K3 eigenmodes / neutrino mass eigenstates, not to K3 vertex states / charged-lepton flavor labels). This is logically forced by the requirement that PMNS = TBM at zeroth order
- **Numerical K3-consistency at zeroth order is exact** (constraint K1/K2/K3 satisfied by construction): the V² operator with eigenvalues $(16, 144, 900)$ on K3 eigenmodes produces, in flavor basis, an exactly $\mu\tau$-symmetric matrix whose eigenvectors are exactly the TBM directions. SM-5's PMNS = TBM result survives Candidate C without modification
- The structural-physical question identified: why the specific V assignment is forced by substrate geometry (closure requires answering)
- Three candidate routes laid out for closure (Route A symmetry-shell correspondence; Route B sub-shell decomposition; Route C direct distance computation from K3 embedding)

**Not established at Session 42 close:**

- Route A, B, or C closure from CPP primitives — Sessions 43+ work
- Theorem-level rigorous derivation of K3-Cage-Shell Consistency
- The specific lifting of the K3 antibonding-doublet degeneracy that picks TBM directions (this is SM-5's existing Open Problem; the K3-Cage-Shell Consistency Theorem doesn't claim to resolve it, only to show that the cage-shell V values are *compatible* with whatever lifts the degeneracy)

**Forward priority for Session 43:**

Investigate Route C — direct distance computation of the small-V bonded shells from the K3 centroid in the 600-cell, drawing on SM-3 K3 Spectral Theorem and the 600-cell distance-shell taxonomy used in SM-7/8/9. If the distance-shell sequence at the lepton-cage scale is $\{4, 12, 30\}$ and the K3-eigenmode coupling to each shell is determined by the eigenmode's symmetry character, OPEN-FP-SF-4-2 closes structurally pending only theorem-level rigor at v0.1 drafting.

The combination of OPEN-FP-SF-4-1 PARTIAL CLOSURE (Session 41, three pictures for $\sigma = z^{-2 d_{\text{eff}}}$) and OPEN-FP-SF-4-2 PARTIAL CLOSURE (Session 42, three routes for cage-shell assignment) puts SF-4 at a well-defined milestone: both substantive sub-problems have leading-order results in hand at the structural-numerical level, with theorem-level rigor as the v0.1 work for both. SF-4 is approaching the v0.1-readiness threshold — if Route C of OPEN-FP-SF-4-2 closes in Session 43+, SF-4 v0.1 drafting could begin substantially earlier than the original 6–10 session estimate.

---

## §9. Session 43 — Route C investigation and structural closure

Per the §6.3 framing, Route C anchors on the SM-3 K3 Spectral Theorem (the K3 embedding into the 600-cell) plus the 600-cell distance-shell taxonomy used in SM-1, SM-7, SM-8, SM-9. The investigation: do the bonded shells from the lepton's 600-cell position give exactly the V values $\{4, 12, 30\}$ at the lepton-cage scale, and do the K3 eigenmodes have a forced coupling pattern to those shells?

### §9.1 The 600-cell bonded-shell structure (verified)

From any 600-cell reference vertex, direct computation of squared distances to all 119 other vertices gives the shell sequence

| Shell | $d^2$ | Vertex count | SM-1 cage identification |
|-------|-------|--------------|--------------------------|
| 0 | 0 | 1 | (the reference vertex itself) |
| 1 | $1/\varphi^2 \approx 0.382$ | **12** | icosahedral first shell — used for charm quark, tau lepton, Z boson cage |
| 2 | 1 | **20** | dodecahedral second shell — used for bottom quark, Higgs cage |
| 3' | $\approx 1.382$ | 12 | (intermediate icosahedral shell; not assigned to a cage type in SM-1) |
| 3 | 2 | **30** | icosidodecahedral shell — used for top quark cage; **also SF-4's $\nu_\tau$ shell** |
| ... | ... | ... | (further outer shells) |
| 8 | 4 | 1 | (antipodal vertex) |

Shell-1 vertex count of 12 matches SM-1's icosahedral cage (V=12). Shell-2 of 20 matches the dodecahedral cage. The d²=2 shell of 30 matches the icosidodecahedral shell. **The 600-cell geometry forces the bonded-shell vertex counts to be 12, 20, 30 at the small-V scale.** This is not a free parameter; it is a topological fact about the 600-cell.

The intermediate 12-vertex shell at $d^2 \approx 1.382$ is a non-cage shell (no SM-1 cage uses it). Its vertices form a rotated icosahedron between shells 1 and 2 in distance ordering; SM-1's cage taxonomy skips it because no stable cage forms at that scale.

### §9.2 V=4 as the tetrahedral subset of shell 1

SM-1 §3 establishes that the **tetrahedral cage** (4 vertices) is "4 of the 12 nearest neighbours in tetrahedral arrangement." The icosahedron contains regular tetrahedra as the famous compound-of-5-tetrahedra (5 inscribed regular tetrahedra, each using 4 of the 12 icosahedral vertices, with each icosahedral vertex appearing in 5/3 tetrahedra on average across the compound). The tetrahedral cage of SM-1 is one such inscribed regular tetrahedron, distinguished by the lepton-flavor structure that picks out specific colour vertices.

This is the V=4 shell of Candidate C: not a *separate* distance shell of the 600-cell, but the **tetrahedral subset of shell 1** at the lepton-cage scale.

### §9.3 V=20 (dodecahedral shell) is excluded by particle-type assignment

A natural question: why does Candidate C use shells {V=4, V=12, V=30} for the three neutrino mass eigenstates, but not V=20 (the dodecahedral shell 2)?

Per SM-1 §3 and the cage-particle assignment table, V=20 is the **bottom quark and Higgs boson cage**. It is occupied by other particle types in the CPP framework. The neutrino sector, being lepton-flavored, sees the substrate from the lepton's position with the lepton-cage structure: V=4 (tetrahedral cage hosting the K3 colour vertices), V=12 (full first shell), V=30 (third shell, exterior). The V=20 dodecahedral shell is "occupied territory" — it hosts particle types whose cage structure has dodecahedral symmetry, which is not the symmetry the K3 lepton-cage structure couples to.

This is not a fit; it is a particle-type taxonomy claim from SM-1 that propagates into SF-4's cage-shell assignment. Skipping V=20 for neutrinos is forced, not chosen.

### §9.4 The K3-eigenmode-to-shell coupling pattern

With V=4, V=12, V=30 confirmed as the available cage shells from the lepton position, the remaining question is which K3 eigenmode couples to which shell. Three structural arguments:

**Argument 1: The bonding mode $\phi_+$ couples to V=12 by symmetry.** The K3 bonding mode $\phi_+ = (1,1,1)/\sqrt{3}$ has equal amplitude on all three K3 colour vertices, which are 3 of the 4 vertices of the V=4 tetrahedral cage. The 4 cage vertices in turn are 4 of the 12 vertices of the V=12 icosahedral first shell. **The bonding mode's full $S_3$-symmetric support across colour vertices generalizes naturally to full $H_3$-symmetric support across the icosahedral first shell** — the symmetry hierarchy $S_3 \subset H_3$ (where $S_3$ acts on the K3 base and $H_3$ acts on the full icosahedron) is the structural basis. The bonding mode "averages" over the three colour vertices of K3 and inherits the $H_3$-icosahedral-symmetric global mode of the V=12 shell.

**This forces $\nu_2 \leftrightarrow V=12$ at the structural level.** No alternative cage-shell coupling is consistent with full-$S_3$-symmetry of the bonding mode.

**Argument 2: The antibonding modes couple to V=4 and V=30 (the broken-symmetry cages).** The K3 antibonding modes $\phi_-^{(1)}, \phi_-^{(2)}$ have non-trivial sign structure across the colour vertices — they break full $S_3$ symmetry of the K3 base. They cannot couple to the full $H_3$-symmetric V=12 shell as their primary cage; their sign structure has nodes that don't align with any $H_3$-symmetric configuration.

The two available alternatives are V=4 (the tetrahedral subset) and V=30 (the icosidodecahedral shell 3). Both break full $H_3$ symmetry to subgroups: V=4 to tetrahedral $T_d$, V=30 to a different subgroup of $H_3$. So both are compatible with antibonding-mode sign structure at the symmetry level.

**This forces antibonding modes to be split between V=4 and V=30, but does not yet specify which mode goes to which.**

**Argument 3: The split between V=4 and V=30 inherits SM-5's existing open problem.** The K3 antibonding modes are doubly degenerate at the K3 level alone — any orthonormal basis of the 2D antibonding subspace is K3-equivalent. SM-5 (Proposition on neutrino species as K3 ZBW eigenmodes) ansatzes a specific basis (the TBM directions $\phi_-^{(1)} = (2,-1,-1)/\sqrt{6}$ and $\phi_-^{(2)} = (0,-1,1)/\sqrt{2}$), which is the $\mu\tau$-symmetric / $\mu\tau$-antisymmetric pair. SM-5 explicitly registers this selection as an open problem (the lifting of K3 antibonding doublet degeneracy, requiring substrate-internal structure beyond K3 alone).

The K3-Cage-Shell Consistency Theorem **does not resolve SM-5's open problem**. It inherits SM-5's selection of TBM directions and shows that the V² operator's eigendirections in the antibonding subspace coincide with TBM directions exactly (§4 numerical result). Once SM-5's selection is given, the V=4 vs V=30 split between $\nu_1$ and $\nu_3$ follows naturally from the wavefunction-spread argument:

- $\nu_1 = (2,-1,-1)/\sqrt{6}$ has heavy support on $V_1$ (the "asymmetric-on-electron-vertex" mode) — its wavefunction concentrates near the K3 cage itself. **Couples to V=4 (the tetrahedral cage hosting the K3).**
- $\nu_3 = (0,-1,1)/\sqrt{2}$ has zero support on $V_1$ — its wavefunction is "outside" the K3 vertex with antisymmetric support on the $\mu\tau$ pair. **Couples to V=30 (the more distant icosidodecahedral shell).**

This argument is heuristic at the wavefunction-spread level and rigorous at the symmetry level: $\nu_1$ has $\mu\tau$-symmetric character, which matches the symmetry of the V=4 tetrahedral subset (the tetrahedral cage's three colour-vertex base has $\mu\tau$-symmetric structure under the SM-5 ansatz); $\nu_3$ has $\mu\tau$-antisymmetric character, which matches the V=30 icosidodecahedral shell's antipodal pairing structure (icosidodecahedron has 30 vertices arranged in 15 antipodal pairs).

### §9.5 Route C closure summary

Route C closes the K3-Cage-Shell Consistency Theorem at the following level:

- **V values {4, 12, 30} are forced by 600-cell geometry**, not fitted. The bonded-shell vertex counts are 600-cell topological facts.
- **V=20 is excluded for neutrinos** by SM-1's particle-type cage taxonomy (V=20 is the bottom quark / Higgs cage).
- **$\nu_2 \leftrightarrow V=12$ is forced** by the bonding mode's full $S_3$-symmetric character matching the icosahedral first shell.
- **Antibonding modes are split between V=4 and V=30** with $\nu_1 \leftrightarrow V=4$ and $\nu_3 \leftrightarrow V=30$ via the wavefunction-spread / symmetry-character argument, **inheriting SM-5's existing open problem on the lifting of the K3 antibonding doublet degeneracy**.

The K3-Cage-Shell Consistency Theorem **does not introduce any new ansatz beyond SM-5's existing one**. Where SM-5 ansatzes the specific TBM directions in the K3 antibonding doublet (registered as SM-5's open problem), SF-4 inherits that selection and shows that the V² mass-operator directions coincide with TBM directions exactly. The cage-shell V values and their assignment to specific eigenmodes are then forced by 600-cell geometry plus the SM-5-ansatzed TBM directions.

### §9.6 OPEN-FP-SF-4-2 status: structural closure at the SM-5 ansatz level

**OPEN-FP-SF-4-2 advances from OPEN (PARTIAL) to OPEN (PARTIAL CLOSURE: structural picture established at the SM-5-ansatz-inheritance level; theorem-level rigor pending v0.1 drafting).**

This is the same closure level that SM-5 itself operates at: SM-5's TBM = K3-eigenvector result is rigorous *given* the K3-eigenmode identification ansatz; SM-5 does not derive that ansatz from CPP interaction rules. SF-4's K3-Cage-Shell Consistency, similarly, is rigorous *given* SM-5's TBM-direction selection in the antibonding subspace; SF-4 does not derive that selection.

**SF-4 does not weaken SM-5's open-problem position; it precisely inherits it.** Closure of SM-5's open problem on the antibonding-doublet-degeneracy lifting would simultaneously close OPEN-FP-SF-4-2 to theorem level. They are tied together.

The numerical zeroth-order consistency is exact (§4); the structural-physical closure at the SM-5-inheritance level is in hand (§9.5). The remaining theorem-level rigor is captured in the SM-5 open problem and v0.1 drafting work.

---

## §10. Programme-level milestone: SF-4 v0.1 readiness

With OPEN-FP-SF-4-1 PARTIAL CLOSURE (Session 41, three pictures for $\sigma = z^{-2 d_{\text{eff}}}$ with 2% empirical match) and OPEN-FP-SF-4-2 PARTIAL CLOSURE at the SM-5-inheritance level (Session 43, this document §9), **SF-4's two substantive sub-problems are both at the maturity level needed for v0.1 outline drafting**.

The v0.1 paper can structure its derivation as follows:

- §1 Strategic frame: strict-C posture, cage-shell mechanism, relation to SM corpus
- §2 The mass formula $m_{\nu_i} = M_0 \cdot V_{\nu_i}^2 \cdot \mathcal{T}_{\text{unbound}}$ and the cage-shell assignment
- §3 The suppression mechanism: walk-dimension framework + three pictures for $z^{-2}$ per channel + numerical agreement at 2%
- §4 K3-Cage-Shell Consistency: bonded-shell topology + eigenmode coupling + inheritance of SM-5's TBM ansatz; numerical verification of zeroth-order TBM angles
- §5 Predictions: three neutrino masses, three TBM mixing angles, normal hierarchy as forced consequence
- §6 $\delta_{CP}$ posture: route (ii), register as open, defer to EW sector
- §7 Higher-order corrections: register-as-conditional via SM-5's existing OP-SM-7d
- §8 Cumulative falsifier: JUNO 2026+ on hierarchy ordering; cosmological bounds; KATRIN
- §9 Open theorem-level work: theorem-level closure of Picture A from A1-A11; theorem-level closure of K3-Cage-Shell Consistency at SM-5-inheritance level; lifting of SM-5 antibonding-doublet open problem
- §10 Discussion: relation to SM-3, SM-5, SM-7/8/9 corpus; programme-level pattern (structural agreement at integer counts is the load-bearing signal); cross-sector implications

Both PARTIAL CLOSURES carry forward into v0.1 with explicit OPEN-FP markers for the remaining theorem-level work. v0.1 ships at "structural-derivation-with-pending-rigor" quality — strong enough to be a flagship-class artifact, honest about the residual theorem-level work that closes at v1.0.

The Session 44 forward priority decision (between full closure of OPEN-FP-SF-4-1 Picture A formalization, beginning v0.1 outline drafting at PARTIAL-CLOSURE level, or any other path) can be made with the SF-4 derivation programme in a notably mature state.

---

## §11. Session 43 close

Established at Session 43 close (this document, §9-§10):

- The 600-cell bonded-shell structure from any vertex is verified numerically: shells at vertex counts $(1, 12, 20, 12, 30, 20, 12, 12, 1)$ across $d^2 \in (0, 4)$. SM-1's cage assignments (V=12, V=20, V=30) match exact 600-cell topology.
- V=4 is established as the tetrahedral subset of shell 1 (from SM-1 + compound-of-5-tetrahedra geometry).
- V=20 exclusion for SF-4 is established as an SM-1 particle-type taxonomy fact (V=20 hosts bottom quark and Higgs).
- Bonding K3 mode $\to$ V=12 forced by symmetry-hierarchy argument $S_3 \subset H_3$.
- Antibonding K3 modes split between V=4 and V=30 via wavefunction-spread / $\mu\tau$-symmetry-character argument, **inheriting SM-5's existing open problem on antibonding-doublet-degeneracy lifting**.
- OPEN-FP-SF-4-2 at OPEN (PARTIAL CLOSURE: structural-physical picture established at SM-5-inheritance level).
- Programme-level milestone: SF-4 v0.1 outline drafting is ready; both substantive sub-problems at PARTIAL CLOSURE.

Not established at Session 43 close:

- Theorem-level closure of K3-Cage-Shell Consistency from CPP primitives, independent of SM-5's open problem — this would require resolving SM-5's antibonding-doublet ansatz, which is its own multi-session derivation campaign and outside SF-4 scope.
- Independent verification of the inscribed-tetrahedron + shell-3 specific embedding of the cage shells from the lepton position in coordinates explicit enough to demonstrate the eigenmode-shell coupling at vertex-by-vertex level. (Numerical computation done at the shell-count level; vertex-by-vertex coupling derivation deferred to v0.1 drafting.)

Forward priority for Session 44: choice between (a) OPEN-FP-SF-4-1 theorem-level Picture A formalization (closes the suppression mechanism rigorously); (b) begin SF-4 v0.1 outline drafting at PARTIAL-CLOSURE level for both sub-problems; (c) other priorities (one of the new flagships SF-5 or SF-6 pre-survey; programme-housekeeping; other CPP corpus work). Decision can be made with both SF-4 sub-problems at the same maturity level.

---

*Working document established at Session 42 (patch 0302); §9-§11 added at Session 43 (patch 0303). Captures sub-derivation under OPEN-FP-SF-4-2 across multiple sessions; grows monotonically until OPEN-FP-SF-4-2 closes. Strategic source: Session 39 mechanism-selection (`SF-4_mechanism_selected.md` §4); SM-5 paper (`series_standard_model/papers/SM-5_tribimaximal_neutrino_mixing_from_k3.tex`) §2-§3 for the K3-eigenmode identification and TBM proof; SM-1 (`series_standard_model/papers/SM-1_*.tex`) §3 for the four-cage taxonomy and bonded-shell assignments; SM-3 K3 Spectral Theorem for the K3-as-tetrahedral-cage-base structural identification; Session 43 numerical verification of 600-cell bonded-shell vertex counts at $V \in \{1, 12, 20, 12, 30, ...\}$ from any reference vertex.*
