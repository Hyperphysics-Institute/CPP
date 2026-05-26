# Mechanism — F.1 Dynamical Substrate Law: Substrate-Locality of DI-Bit Currents at Vertex-Aligned Reading C in the 600-Cell

> **v1.0 SHIPPED STATUS NOTE (Patch 0572c, 24 May 2026, Session 143)**: This file is written at F.1 v1.0 SHIPPED state (Patch 0570, Session 142, 24 May 2026). The substrate-locality theorem (Theorem 7.1) is at sketch-document Layer 3 with three publication-grade Layer 3 inputs (Theorem 5.1 + Theorem 5.2 + Theorem 6.1 + Corollary 6.2); identity G1 is at sketch-document Layer 3 with G1 publication-grade hardening registered as OPEN-FP-F1-3 (RECOMMENDED first post-Phase-7 substantive physics Patch per ChatGPT R1–R6 convergent priority). Mechanism A is taken as framework axiom (MA.1 + MA.2) with Layer 4 axiomatic derivation registered as OPEN-FP-F1-2. The 5-Open-Problem body §9 commitment is preserved end-to-end; OPEN-FP-F1-6 prose-density tightening registered separately at Patch 0569e from R6 follow-up.

**Paper:** `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/dynamical_substrate_law.tex` (v1.0 SHIPPED 24 May 2026, Session 142 Patch 0570)
**Hardened theorem artifacts:** `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/hardened_theorems/` (Patches 0550 + 0551 + 0552 trio; 741 lines LaTeX combined)
**Verification scripts:** `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/code/` (5 Python scripts; standard library + NumPy only)
**Last updated:** 24 May 2026 (Session 143 Patch 0572c)

---

## One-sentence summary

At vertex-aligned Reading C in the 600-cell substrate, the propagation-rate asymmetry of Mechanism A produces a net DI-bit current at any host vertex that — at first order in the asymmetry parameter $\delta$ — depends only on first-shell content and takes the closed-form value $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$.

The closed-form result is the **substrate-locality structure** that supports the candidate substrate mechanism for the thermodynamic causal arrow (manifestation (iv) of OPEN-SD-CHIR-PRIMITIVE), without yet deriving thermodynamic-arrow emergence (entropy production / coarse-graining / macroscopic irreversibility) in the conventional physics sense — the emergence layer is future work.

---

## Inputs and constants

**Substrate.** The 600-cell — the regular 4-polytope $\{3,3,5\}$, also called the hexacosichoron — embedded on the unit 3-sphere $S^3 \subset \mathbb{R}^4$. The 600-cell has 120 vertices, 720 edges, 1200 triangular faces, and 600 tetrahedral cells, with $H_4$ symmetry group (order 14400). Coxeter regular polytopes reference for the canonical vertex coordinates.

**Reading C orientation.** A primitive 4D direction $\hat{n} \in S^3$ (unit vector) selects the substrate-direction primitive of the chirality continuum (FI-C-RC-1 of Capotauro v2.0). The **vertex-aligned** variant fixes $\hat{n} = \vhost / |\vhost| = \vhost$ for a chosen host vertex $\vhost$ (FI-C-RC-2 of Capotauro v2.0). Two other Reading C variants (edge-aligned with $D_3$ residual symmetry, face-aligned with $D_2$ residual symmetry) are out of scope at this paper — extension is OPEN-FP-F1-5.

**Residual symmetry at the host vertex.** The icosahedral group $H_3 = I_h$ (order 120) stabilizes $\vhost$ within the full $H_4$ symmetry of the 600-cell. The 12 first-shell neighbours $\{v_i\}_{i=1}^{12}$ form a regular icosahedron at distance $1/\phi$ from $\vhost$; $H_3$ permutes them transitively.

**Mechanism A as framework axiom.** Two axioms taken as substrate-physics input (Layer 3 framework axiom level; Layer 4 axiomatic derivation from A1–A11 is OPEN-FP-F1-2):

- **MA.1 — Propagation-rate asymmetry primitive.** For an oriented edge of the 600-cell with unit-direction vector $\hat{e}$, the DI-bit propagation rate is $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$, where $r_0$ is the base propagation rate (vertex-uniform) and $\delta$ is a small asymmetry parameter ($|\delta| \ll 1$).
- **MA.2 — Framework-local current construction.** At first order in $\delta$, the DI-bit current contribution from edges emanating from a vertex $v$ is constructed locally as the sum over edges with their orientation-asymmetry-weighted rates.

**Golden ratio.** $\phi = (1+\sqrt{5})/2 \approx 1.618$. Appears throughout 600-cell first-shell geometry via the icosahedral structure of the first shell. Reciprocals $1/\phi = \phi - 1$ and $1/\phi^2 = 2 - \phi$.

**First-shell geometric primitives (introduced §3.3 of the paper; at sketch-document Layer 3, G1 hardening is OPEN-FP-F1-3):**

- **G1 — First-shell inner-product primitive.** For first-shell unit vectors $\hat{u}_i = (v_i - \vhost)/|v_i - \vhost|$, the inner product $\hat{u}_i \cdot \hat{u}_j$ takes one of a small set of discrete values determined by the icosahedral residual symmetry $H_3$ + the 600-cell first-shell-edge dihedral angle $\cos(36°) = \phi/2$. Imported from Patch 0541 §3.1 derivation.
- **G2 — First-shell edge-direction projection.** First-shell-to-first-shell edge directions $\hat{e}_{ij}$ are perpendicular to $\hat{n}$ for any first-shell pair $(v_i, v_j)$ sharing a 600-cell edge.

---

## The mechanism, step by step

### Step 1: Propagation-rate asymmetry as the substrate-direction primitive

**What it does:** Encodes the chirality continuum's substrate-direction primitive $\hat{n}$ as a substrate-physics commitment about how DI-bit propagation rates depend on edge direction.

**How it works:** Edges of the 600-cell are oriented; DI-bit transfer along an edge happens at rate $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$. Edges parallel to $\hat{n}$ propagate faster; edges anti-parallel propagate slower; edges perpendicular propagate at the base rate $r_0$. The asymmetry parameter $\delta$ controls the magnitude of the directional bias.

**Key insight:** Mechanism A is the *minimal* propagation-rate-asymmetry primitive consistent with the substrate-direction primitive $\hat{n}$. The minimality is operationalised in the "minimal-local-first-order realization framework" of §2.4 — three minimality constraints (locality, first-order in $\delta$, single-direction primitive $\hat{n}$) jointly identify the unique framework form. Higher-order corrections and tangent-direction couplings are deferred (OPEN-FP-F1-1).

### Step 2: Vertex-aligned Reading C selects $\hat{n} = \vhost$

**What it does:** Identifies the substrate-direction primitive with the host-vertex radial direction.

**How it works:** Of the three Reading C variants (vertex-aligned / edge-aligned / face-aligned), the vertex-aligned variant has the maximum residual symmetry $H_3 = I_h$ at the host vertex. The 12 first-shell neighbours form a regular icosahedron permuted transitively by $H_3$. The vertex-aligned choice maximises the algebraic constraints from residual symmetry, which is what makes the first-shell geometric identities (Step 4 + Step 5) clean.

**Key insight:** The Reading C variant choice is a foundational input (FI-C-RC-2) from the chirality continuum architecture, not a derivation choice within F.1. Capotauro v2.0 §2 establishes vertex-aligned Reading C across the chirality continuum's three spatial-sector manifestations; F.1 imports it as a structural input.

### Step 3: First-shell host-to-first-shell uniform projection (Theorem 5.1)

**What it does:** Demonstrates that all 12 first-shell unit vectors have the *same* projection onto $\hat{n}$.

**How it works:** For each first-shell unit vector $\hat{u}_i = (v_i - \vhost)/|v_i - \vhost|$, the inner product with $\hat{n}$ is identically:

$$\hat{u}_i \cdot \hat{n} = -\frac{1}{2\phi}$$

The result is proven (publication-grade Layer 3, conditional on G1) by combining: (a) G1's first-shell inner-product structure with dihedral angle $\cos(36°) = \phi/2$; (b) the unit-vertex normalization on $S^3$; (c) the icosahedral residual symmetry $H_3 = I_h$. Lemma 5.2.1 supplies the tangent-hyperplane chord length argument that anchors the projection geometrically.

**Key insight:** The 12-fold uniformity is the load-bearing geometric fact that makes the first-order substrate current expressible in closed form. Without uniformity, the per-edge contributions would not symmetrize cleanly at the host vertex. The structural constant $-1/(2\phi)$ is the same numerical signature that appears in Capotauro v2.0 §3 spatial-sector substrate-locality — F.1 and Capotauro v2.0 share this projection constant despite their different physical sector contexts.

### Step 4: First-shell-to-first-shell edge perpendicularity (Theorem 5.2)

**What it does:** Demonstrates that all 30 first-shell-to-first-shell edges are perpendicular to $\hat{n}$.

**How it works:** For any 600-cell edge connecting two first-shell vertices $(v_i, v_j)$, the edge direction $\hat{e}_{ij}$ satisfies:

$$\hat{e}_{ij} \cdot \hat{n} = 0$$

This follows from: (a) G2 first-shell edge-direction structure (icosahedral first-shell-to-first-shell edges lie in the "equatorial" 3-plane perpendicular to $\hat{n}$); (b) the same icosahedral residual symmetry $H_3$ that proved Theorem 5.1. The 30 first-shell-to-first-shell edges of the icosahedron all lie in this equatorial 3-plane.

**Key insight:** This perpendicularity is the **same identity Capotauro v2.0 uses for spatial-sector K3-base protection** (Capotauro §3 cross-reference §5.6 of F.1). The shared geometric structure makes F.1's temporal-sector closure parallel to Capotauro v2.0's spatial-sector closure at the structural-constant level, even though the physical sectors differ. The exclusion class E1 of §5.5 is the shared G1-dependency exclusion between Theorems 5.1 and 5.2.

### Step 5: Perturbation-theory propagation rule (Theorem 6.1)

**What it does:** Establishes that the $\mathcal{O}(\delta^n)$ coefficient of the substrate current at any vertex depends only on edges within graph distance $n$ on the 600-cell edge graph.

**How it works:** The proof proceeds via three lemmas:

- **Lemma 6.1.1 — Path-amplitude expansion.** The full DI-bit current is expanded as a power series in $\delta$; each term is indexed by a path in the 600-cell edge graph with the path's contribution weighted by the asymmetry-asymmetry product along the path.
- **Lemma 6.2.1 — Perturbed-step counting.** Each factor of $\delta$ in the expansion corresponds to traversing one "perturbed" edge (an edge whose orientation matters for the asymmetry term); paths with $n$ perturbed steps contribute at order $\delta^n$.
- **Lemma 6.3.1 — Connected-subgraph confinement.** Paths of length $n$ from the host vertex stay within graph-distance $n$ (the 1-ball $E_1$ for $n=1$, 2-ball $E_2$ for $n=2$, etc.). This is the load-bearing combinatorial step that makes shell-locality emerge.

**Key insight:** The propagation rule is **publication-grade Layer 3** (the strongest section of the paper per ChatGPT R1 verbatim). The three lemmas combine to confine each perturbative order to a topologically local region of the 600-cell edge graph. Lemma 6.3.1's proof (ChatGPT R2 "least transparent mathematical step") is hardened in the Patch 0550 `hardened_theorems/perturbation_locality.tex` artifact with explicit hypothesis tracking + five-class exclusion enumeration.

### Step 6: Shell-locality at first order (Corollary 6.2)

**What it does:** Specializes the perturbation-theory propagation rule to first order, confining the $\mathcal{O}(\delta^1)$ contribution to first-shell edges only.

**How it works:** Corollary 6.2 follows directly from Theorem 6.1 at $n=1$: the $\mathcal{O}(\delta^1)$ coefficient $\vec{J}_1(\vhost)$ depends only on edges in the 1-ball $E_1(\vhost) = \{$ 12 host-to-first-shell edges $\} \cup \{$ 30 first-shell-to-first-shell edges $\}$ of the 600-cell edge graph.

**Key insight:** This is the **dynamical confinement engine** that, combined with the geometric identities of Steps 3 + 4, produces the substrate-locality umbrella at Step 8. The shell-locality corollary alone does not yet give a closed-form expression — it only confines the support; the closed form requires Steps 3 + 4 + 7 to evaluate the per-shell contribution.

### Step 7: Five-class exclusion enumeration (paper §6.6)

**What it does:** Documents the five exclusion classes that constrain the proof of the perturbation-theory propagation rule's hypothesis set.

**How it works:** Each class identifies a structural condition that, if violated, would make the propagation rule fail. The five classes:

1. **E1 — G1 dependency** (shared with Theorems 5.1 + 5.2): the first-shell inner-product primitive must hold.
2. **E2 — Edge-graph connectivity:** the 600-cell edge graph must be connected (verified by Coxeter).
3. **E3 — Path-amplitude expansion convergence:** the series must converge in the small-$\delta$ regime.
4. **E4 — Perturbation-theory orientation:** the orientations of edges must be consistent under graph-distance-bound enumeration.
5. **E5 — Mechanism A locality:** the propagation-rate primitive must be edge-local (no nonlocal terms).

**Key insight:** The five-class exclusion enumeration is the **publication-grade rigor signature** of the perturbation-locality artifact at Patch 0550. The hardened-theorems trio convention requires explicit hypothesis tracking + isolation of structural inputs + five-class exclusion enumeration as the publication-grade Layer 3 standard.

### Step 8: Substrate-locality umbrella assembly (Theorem 7.1)

**What it does:** Assembles Steps 3 + 4 + 5 + 6 into the substrate-locality umbrella theorem and computes the closed-form first-order current.

**How it works:** Three-step assembly at §7.3:

- **(i) Shell confinement.** Apply Corollary 6.2 at $n=1$: only the 12 host-to-first-shell + 30 first-shell-to-first-shell edges contribute at $\mathcal{O}(\delta^1)$.
- **(ii) First-shell-to-first-shell perpendicularity zeroes 30 contributions.** Apply Theorem 5.2: each first-shell-to-first-shell edge has $\hat{e}_{ij} \cdot \hat{n} = 0$, so all 30 of these edges contribute zero at $\mathcal{O}(\delta^1)$.
- **(iii) Host-to-first-shell uniform projection + icosahedral sum.** Apply Theorem 5.1: each of the 12 host-to-first-shell edges has $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$. The Mechanism A first-order current contribution from each is $\propto \delta\,(\hat{u}_i \cdot \hat{n})\,\hat{u}_i$. Summing over $i = 1, \ldots, 12$ and using the icosahedral identity $\sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n})\,\hat{u}_i = (3/\phi^2)\,\hat{n}$ (which follows from $\sum_i \hat{u}_i = -(6/\phi)\,\hat{n}$ via the rank-1 projector structure):

$$\boxed{\;\vec{j}_{DI}^{\text{net}}(\vhost) = \frac{6\delta}{\phi^2}\,\hat{n} + \mathcal{O}(\delta^2)\;}$$

**Key insight:** The result is **closed-form, depends only on first-shell content** (substrate-locality), and is **parallel-to-$\hat{n}$** (no tangent-to-$\hat{n}$ contributions at first order). The umbrella theorem is at **sketch-document Layer 3** because the three-step assembly itself has not been independently hardened with explicit hypothesis tracking + five-class exclusion enumeration; independent hardening is the candidate follow-up Patch at §7.4 (not formal Open Problem to preserve 5-OP commitment). The non-publication-grade status is preserved transparently per the anti-erasure discipline.

---

## Mathematical correspondence table

| Physics claim | Equation / Theorem | Paper section | Verification script |
|---|---|---|---|
| Propagation-rate asymmetry primitive | $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$ (Eq. 4.1 / Axiom MA.1) | §4.1 | implicit in `verify_phase1.py` per-edge rate calculation |
| Framework-local current construction | $\vec{j}(v) = 2 r_0 \delta \sum_j (\hat{u}_j \cdot \hat{n})\,\hat{u}_j$ (Eq. 4.2 / Axiom MA.2) | §4.2 | `verify_phase1.py` |
| Host-to-first-shell uniform projection | $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ for $i = 1, \ldots, 12$ (Theorem 5.1) | §5.3 | `verify_phase1.py` identity (1) |
| First-shell unit-vector sum | $\sum_{i=1}^{12} \hat{u}_i = -(6/\phi)\,\hat{n}$ (Lemma 5.2.1 corollary) | §5.3 | `verify_phase1.py` identity (2) |
| First-shell-to-first-shell perpendicularity | $\hat{e}_{ij} \cdot \hat{n} = 0$ for all 30 first-shell edges (Theorem 5.2) | §5.4 | `verify_b1q2_curl_content.py` first-shell-K3-base-protection identity |
| Icosahedral rank-1 sum identity | $\sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n})\,\hat{u}_i = (3/\phi^2)\,\hat{n}$ | §7.3 Step (iii) | `verify_phase1.py` identity (3) |
| Perturbation-theory propagation rule | $\vec{J}_n(\vhost)$ supported in $E_n(\vhost)$ (Theorem 6.1) | §6.4 | implicit in `verify_phase4.py` shell-confinement check |
| Shell-locality at $\mathcal{O}(\delta^1)$ | $\vec{J}_1(\vhost)$ supported in $E_1(\vhost)$ only (Corollary 6.2) | §6.5 | implicit in `verify_phase4.py` |
| Substrate-locality umbrella (closed form) | $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$ (Theorem 7.1) | §7.2 | `verify_phase1.py` identity (4) |
| First-shell-vertex extension (per-vertex current magnitude) | $|\vec{j}(v_i)| = 2 r_0 \delta \sqrt{7-\phi}$ uniform across 12 first-shell vertices | sub-question B.1.q4 (not in paper body) | `verify_b1q4_first_shell_current_sum.py` identity (4) |
| First-shell-vertex sum identity | $\sum_{i=1}^{12} \hat{j}(v_i) = (24/\sqrt{7-\phi})\,\hat{n} \approx 10.345\,\hat{n}$ | sub-question B.1.q4 | `verify_b1q4_first_shell_current_sum.py` identity (5) |
| Discrete curl of $\vec{j}_{DI}^{\text{net}}$ at host vertex | $\nabla \times \vec{j}_{DI}^{\text{net}}(\vhost) = 0$ at $\mathcal{O}(\delta)$ | sub-question B.1.q2 (foundations work) | `verify_b1q2_curl_content.py` |

All identities computed analytically in the paper are computationally cross-verified to floating-point precision at the verification scripts. The scripts use standard library + NumPy only; no external dependencies. Total runtime < 30 seconds for the full verification suite.

---

## Empirical anchor and falsifier

**What the substrate-locality umbrella numerically asserts:** at $\delta = 0.01$ (illustrative small-$\delta$ regime), $\vec{j}_{DI}^{\text{net}}(\vhost) = (6 \cdot 0.01/\phi^2)\,\hat{n} \approx 0.0229\,\hat{n}$ in units of $r_0 \delta$. The factor $6/\phi^2 \approx 2.293$ is the universal structural constant for the temporal sector at vertex-aligned Reading C.

**Empirical regime where this would be observable:** The DI-bit current is an internal substrate-physics quantity, not a directly-observed macroscopic quantity at this paper's scope. The connection to macroscopic thermodynamic-arrow phenomena is the *candidate mechanism narrative supported by* the substrate-locality structure (not derived from it in the conventional physics sense — entropy production / coarse-graining / macroscopic irreversibility are explicit non-derivations per §10).

**Three direct falsifiability channels at the theorem level:**

1. **Theorem 5.1 falsifier.** Demonstration via explicit 600-cell calculation that $\hat{u}_i \cdot \hat{n} \neq -1/(2\phi)$ for some first-shell vertex. This is testable on Coxeter's canonical 600-cell coordinates; the verification script does exactly this check at floating-point precision.
2. **Theorem 5.2 falsifier.** Demonstration via explicit 600-cell calculation that $\hat{e}_{ij} \cdot \hat{n} \neq 0$ for some first-shell-to-first-shell edge. Similarly testable.
3. **Theorem 6.1 falsifier.** Demonstration of a first-order-in-$\delta$ contribution at any vertex beyond first-shell range — i.e., a $\delta^1$ term in the substrate current at a second-shell or further vertex. The shell-locality corollary explicitly excludes this; the falsifier would require either a counterexample calculation or an explicit pathology in the perturbation expansion.

**Mechanism A falsifier (Layer 4 question):** at Layer 4 (OPEN-FP-F1-2 closure), Mechanism A would become derivable from A1–A11 and therefore falsifiable by demonstration that no derivation can produce the propagation-rate asymmetry from primitive axioms. This is itself a research-direction-choosing question at the present paper's scope, not a derivation falsifier.

---

## Failure modes (with OPEN-FP-F1-* references)

| Failure mode | Open Problem | Status at v1.0 SHIP |
|---|---|---|
| $\mathcal{O}(\delta^2)$ corrections deviate from substrate-locality (e.g., second-shell second-order contributions introduce tangent-to-$\hat{n}$ components) | OPEN-FP-F1-1 (extension to $\mathcal{O}(\delta^2)$) | OPEN; substantive geometric and perturbation-theory project at higher order |
| Mechanism A is not derivable from A1–A11 (would block the Layer 4 axiomatic derivation trajectory) | OPEN-FP-F1-2 (Layer 4 axiomatic derivation) | OPEN; long-term programme target; multi-Patch trajectory |
| G1 publication-grade hardening fails (would invalidate Theorems 5.1 + 5.2 conditional Layer 3 publication-grade status) | OPEN-FP-F1-3 (G1 publication-grade hardening) | OPEN; RECOMMENDED first post-Phase-7 substantive physics Patch per ChatGPT R1–R6 convergent priority |
| Manifestation (v) does not exist or is not identifiable (would weaken the chirality continuum architecture's predictive scope) | OPEN-FP-F1-4 (Sector-5 schema instantiation) | OPEN; research-direction-choosing |
| Non-vertex-aligned Reading C variants produce qualitatively different substrate-locality structures (would weaken the universality claim) | OPEN-FP-F1-5 (non-vertex-aligned Reading C variants) | OPEN; methodologically tractable but not yet attempted |
| Prose density makes the paper unsuitable for academic submission (registered post-SHIP from ChatGPT R6 follow-up) | OPEN-FP-F1-6 (prose-density tightening) | OPEN; addressable by a F.1-condensed companion paper trajectory at Theorem 6.1 + Corollary 6.2 + Theorem 7.1 scope with minimal CPP interpretation |

The umbrella theorem (Theorem 7.1) is at **sketch-document Layer 3 only**; independent publication-grade hardening of Theorem 7.1 is a candidate follow-up Patch registered at §7.4 (not formal Open Problem to preserve in-body 5-OP commitment). Its non-publication-grade status is itself a known limitation, transparently preserved per the anti-erasure discipline.

---

## Cross-paper consistency checks

**Capotauro v2.0 §3 spatial-sector parallel.** The structural constant $-1/(2\phi)$ appears identically in Capotauro v2.0 §3's spatial-sector substrate-locality theorem (first-shell host-to-first-shell projection in the K3-doublet spatial sector). F.1 and Capotauro v2.0 share the **same first-shell geometric identities** (G1 + G2 + Theorem 5.1 analog + Theorem 5.2 analog) despite their different physical sector contexts. The chirality continuum architecture's substrate-direction primitive $\hat{n}$ is realized differently in the two sectors (spatial vs temporal) but the underlying geometric structure is shared. This is the methodological pattern of "shared first-shell identities governing both spatial and temporal sectors" that Grok R1 emphasized as a structural payoff.

**OPEN-SD-CHIR-PRIMITIVE manifestation status across the chirality continuum:**

- (i) Parity violation — closed at Layer 3 in Capotauro v2.0 (spatial sector, K3-doublet).
- (ii) Neutrino chirality structure — closed at Layer 3 in Capotauro v2.0.
- (iii) Weak isospin assignment — closed at Layer 3 in Capotauro v2.0.
- **(iv) Thermodynamic causal arrow — closed at sketch-document Layer 3 in F.1 (this paper).**
- (v) Sector-5 schema — OPEN; OPEN-FP-F1-4.

F.1 is the **second flagship trajectory** in CPP corpus to close a manifestation of OPEN-SD-CHIR-PRIMITIVE (after Capotauro v2.0). The methodological pattern (first-shell geometric identities + perturbation-locality on the 600-cell edge graph + framework-axiom Mechanism strategy + 5-OP commitment) is now corpus-established for future F-line flagship trajectories (F.2, F.3, etc.).

**CPP corpus track record (programme epistemic methodology grounding):** SS-7 12 zero-parameter predictions for alpha-chain nuclei within ±1.5%; SS-2 proton charge radius 0.851–0.883 fm; SS-4 string tension 926.5 MeV/fm; SS-5 deuteron binding −0.09%; SM-8 $M_0 = m_e \cdot z/\phi$ derivation; SF-4 v1.0 7/8 zero-parameter neutrino predictions; Capotauro v2.0 three-way cross-sector substrate-chirality unification $|M^{K_3}| = |M^W| = |M^{qDP}| = \chi/6 \approx 0.0394$ at zero free parameters. F.1's substrate-locality umbrella extends this track record into the temporal sector at the sketch-document Layer 3 honesty level.

---

## What's in scope at v1.0 SHIP vs deferred to v2.0+

**In scope at v1.0 SHIP (the present paper's deliverables):**

- Theorem 5.1 host-to-first-shell uniform projection at **publication-grade Layer 3** (conditional on G1).
- Theorem 5.2 first-shell-to-first-shell perpendicularity at **publication-grade Layer 3** (conditional on G1).
- Theorem 6.1 perturbation-theory propagation rule at **publication-grade Layer 3** (unconditional; hardened at Patch 0550 artifact).
- Corollary 6.2 shell-locality at $\mathcal{O}(\delta^1)$ at **publication-grade Layer 3** (immediate corollary of Theorem 6.1).
- Theorem 7.1 substrate-locality umbrella at **sketch-document Layer 3** (assembly of Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2; not independently hardened).
- Three publication-grade hardened-theorem artifacts at `hardened_theorems/` (Patches 0550 + 0551 + 0552; 741 lines LaTeX combined).
- Five Open Problems registered: OPEN-FP-F1-1 through OPEN-FP-F1-5 (in-body §9); OPEN-FP-F1-6 registered separately at Patch 0569e from R6 follow-up.

**Deferred to v2.0+:**

- G1 publication-grade hardening (OPEN-FP-F1-3) — RECOMMENDED first post-Phase-7 substantive physics Patch.
- Extension to $\mathcal{O}(\delta^2)$ (OPEN-FP-F1-1) — substantive geometric + perturbation-theory project at higher order.
- Layer 4 axiomatic derivation of Mechanism A (OPEN-FP-F1-2) — long-term programme target.
- Sector-5 schema instantiation (OPEN-FP-F1-4) — research-direction-choosing.
- Non-vertex-aligned Reading C variants (OPEN-FP-F1-5).
- Prose-density tightening + F.1-condensed companion paper trajectory (OPEN-FP-F1-6).
- Substrate-locality umbrella publication-grade hardening (§7.4 candidate follow-up Patch).
- Thermodynamic-arrow emergence (entropy production / coarse-graining / macroscopic irreversibility) — explicitly disclaimed at §10; future work beyond the present paper's framework qualifiers.

---

*Mechanism file created Session 143 Patch 0572c (24 May 2026) as the fourth SHIP-time companion documentation file in Phase 7A. Per `templates/documentation-suite.md` §3 + checklist §A A1 (mechanism narrative with mathematical-correspondence table + failure modes with OPEN-* references) + Capotauro reference implementation `mechanism-capotauro.md` 8-step structure. Source priorities per docsuite.md §32: items 1 + 2 + 6 + 9 (sketches + reasoning + scripts + `.tex` source). This file is maintained continuously from this Patch forward; future paper-version increments trigger mechanism extensions and additional step sections.*
