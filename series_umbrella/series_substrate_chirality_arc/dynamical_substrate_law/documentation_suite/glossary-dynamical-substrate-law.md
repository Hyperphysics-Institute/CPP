# Glossary — F.1 Dynamical Substrate Law: Substrate-Locality of DI-Bit Currents at Vertex-Aligned Reading C in the 600-Cell

> **v1.0 SHIPPED STATUS NOTE (Patch 0572d, 24 May 2026, Session 143)**: This file is written at F.1 v1.0 SHIPPED state (Patch 0570, Session 142, 24 May 2026). All entries are at v1.0 SHIPPED definition state; status-label entries (publication-grade Layer 3, sketch-document Layer 3, framework axiom, etc.) reflect the v1.0 SHIP Layer status of each item per the explicit Layer hierarchy table at §8.2 of the paper. Future paper-version increments may extend entries (e.g., G1 hardening at OPEN-FP-F1-3 closure would promote G1 from sketch-document Layer 3 to publication-grade Layer 3) but will not modify existing entries' v1.0 SHIP definitions.

**Paper:** `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/dynamical_substrate_law.tex` (v1.0 SHIPPED 24 May 2026, Session 142 Patch 0570)
**Last updated:** 24 May 2026 (Session 143 Patch 0572d)

---

## Constants

### $\phi$ — golden ratio
$\phi = (1+\sqrt{5})/2 \approx 1.618$. Reciprocals: $1/\phi = \phi - 1 \approx 0.618$; $1/\phi^2 = 2 - \phi \approx 0.382$. Appears throughout 600-cell first-shell geometry via the icosahedral residual symmetry $H_3 = I_h$ and the first-shell-edge dihedral angle $\cos(36°) = \phi/2$. First use: §3.2 (600-cell substrate at vertex-aligned Reading C). Related: $1/(2\phi)$ structural constant; $6/\phi^2$ umbrella-theorem coefficient.

### $-1/(2\phi)$ — host-to-first-shell uniform projection constant
The structural constant proven in Theorem 5.1: for any first-shell unit vector $\hat{u}_i = (v_i - \vhost)/|v_i - \vhost|$ where $v_i$ is one of the 12 first-shell neighbours of host vertex $\vhost$, the inner product $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ — uniformly across all 12 first-shell neighbours at vertex-aligned Reading C. First use: §5.3 (Theorem 5.1 statement + proof). **Shared with Capotauro v2.0 §3 spatial-sector substrate-locality theorem.** Related: $\phi$, Theorem 5.1, host vertex, first-shell, vertex-aligned Reading C.

### $6/\phi^2$ — substrate-locality umbrella coefficient
The structural constant for the closed-form first-order substrate current: $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$. Derives from the icosahedral rank-1 sum identity $\sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n})\,\hat{u}_i = (3/\phi^2)\,\hat{n}$ multiplied by Mechanism A's per-edge contribution factor of 2. Numerically $6/\phi^2 \approx 2.293$. First use: §7.2 (Theorem 7.1 closed-form result). Related: Theorem 7.1, $\phi$.

### $\delta$ — propagation-rate asymmetry parameter
The small parameter ($|\delta| \ll 1$) controlling the magnitude of Mechanism A's directional bias. The substrate-locality result Theorem 7.1 is at first order in $\delta$; higher orders ($\mathcal{O}(\delta^2)$, $\mathcal{O}(\delta^3)$, etc.) are deferred to OPEN-FP-F1-1. First use: §4.1 (Mechanism A axiom MA.1 statement). Related: Mechanism A, propagation rate $r(\hat{e})$, OPEN-FP-F1-1.

### $r_0$ — base propagation rate
The vertex-uniform DI-bit propagation rate in the unperturbed limit ($\delta = 0$). Appears as the prefactor in Mechanism A's propagation rate $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$. First use: §4.1. Related: Mechanism A, propagation rate $r(\hat{e})$.

### $z = 12$ — 600-cell first-shell coordination number
The number of first-shell neighbours of any vertex in the 600-cell. Equivalently, the number of edges incident to any vertex. First use: §3.2 (600-cell substrate). The 12 first-shell neighbours form a regular icosahedron at distance $1/\phi$ from the host vertex. Related: 600-cell, first-shell, regular icosahedron, $H_3 = I_h$ residual symmetry.

### $\sqrt{7-\phi}$ — first-shell-vertex current magnitude factor
The structural constant appearing in the per-vertex DI-bit current magnitude at first-shell vertices: $|\vec{j}(v_i)| = 2 r_0 \delta \sqrt{7-\phi}$ uniform across all 12 first-shell vertices (foundations work sub-question B.1.q4). Numerically $\sqrt{7-\phi} \approx 2.317$. Not used in the paper body; appears in the foundations-work sketch + `verify_b1q4_first_shell_current_sum.py`. Related: B.1.q4 verification script.

---

## Structural terms (polytope-theoretic + geometric)

### 600-cell
The regular 4-polytope $\{3,3,5\}$, also called the hexacosichoron. Embedded on the unit 3-sphere $S^3 \subset \mathbb{R}^4$. Has 120 vertices, 720 edges, 1200 triangular faces, 600 tetrahedral cells. Symmetry group $H_4$ of order 14400 (the largest finite reflection group in 4D). First use: paper title + §3.2. Coxeter regular polytopes reference for canonical vertex coordinates. Related: $H_4$ symmetry, vertex, edge graph, first-shell.

### $H_4$ — 600-cell symmetry group
The Coxeter reflection group of the 600-cell, order 14400. Equivalently the full automorphism group of the regular 4-polytope $\{3,3,5\}$. Acts transitively on the 120 vertices. First use: §3.2. Related: 600-cell, $H_3 = I_h$ (residual symmetry at host vertex).

### $H_3 = I_h$ — icosahedral residual symmetry at host vertex
The stabilizer subgroup of any vertex in the 600-cell under $H_4$ action. $H_3$ is the icosahedral Coxeter group, isomorphic to the full icosahedral symmetry group $I_h$ (order 120). Permutes the 12 first-shell neighbours transitively as the vertices of a regular icosahedron. First use: §3.2. **Load-bearing for Theorem 5.1 + Theorem 5.2** (the residual symmetry forces the uniform projection + edge perpendicularity). Related: 600-cell, $H_4$, regular icosahedron, host vertex, first-shell.

### Host vertex $\vhost$
A chosen 600-cell vertex at which the substrate physics is computed. Vertex-aligned Reading C identifies $\vhost$ with the substrate-direction primitive: $\hat{n} = \vhost / |\vhost| = \vhost$ on the unit 3-sphere. First use: §3.2. Related: vertex-aligned Reading C, substrate-direction primitive $\hat{n}$, first-shell.

### First-shell
The set of 12 600-cell vertices adjacent to $\vhost$ via an edge. They form a regular icosahedron at distance $1/\phi$ from $\vhost$. Denoted $\{v_i\}_{i=1}^{12}$ in the paper. First use: §3.2. Related: 600-cell, host vertex, $H_3 = I_h$, regular icosahedron, first-shell unit vector.

### Second-shell
The set of 20 600-cell vertices at graph-distance 2 from $\vhost$ (i.e., adjacent to first-shell but not first-shell themselves and not $\vhost$). They form a regular dodecahedron at distance $\sqrt{2 - 2\cos(72°)} = (1/\phi)\sqrt{3-\phi}$ from $\vhost$. First use: §9 (Open Problem OPEN-FP-F1-1 statement). Second-shell content is not used at first order in $\delta$ (substrate-locality at $\mathcal{O}(\delta^1)$ is to first-shell only); second-shell becomes relevant at OPEN-FP-F1-1 closure ($\mathcal{O}(\delta^2)$ extension). Related: first-shell, edge graph, OPEN-FP-F1-1.

### Edge graph (of the 600-cell)
The graph with 120 vertices (the 600-cell vertices) and 720 edges (the 600-cell edges). Defines the graph-distance metric on the substrate. First use: §3.4 (DI-bit current and Mechanism A framework). Connectivity guaranteed by Coxeter; this is exclusion class E2 of the perturbation-theory propagation rule. Related: 600-cell, $n$-ball, graph-distance.

### $n$-ball $E_n(\vhost)$
The set of edges within graph-distance $n$ from $\vhost$ in the 600-cell edge graph. $E_1(\vhost) = \{$12 host-to-first-shell edges$\} \cup \{$30 first-shell-to-first-shell edges$\}$. $E_2(\vhost)$ extends to include the 60 first-shell-to-second-shell edges and second-shell-to-second-shell edges. The substrate-locality result Theorem 7.1 confines the $\mathcal{O}(\delta^1)$ substrate current to $E_1(\vhost)$. First use: §6.4 (Theorem 6.1 perturbation-locality propagation rule). Related: perturbation-theory propagation rule, edge graph, shell-locality corollary.

### Vertex-aligned Reading C
The choice of substrate-direction primitive $\hat{n}$ that aligns with a host-vertex radial direction: $\hat{n} = \vhost / |\vhost| = \vhost$ on $S^3$. This is the most-symmetric Reading C variant (residual symmetry $H_3 = I_h$); two other variants (edge-aligned with $D_3$ residual symmetry, face-aligned with $D_2$) are out of scope at the present paper. First use: paper title + §3.2. Imported as foundational input FI-C-RC-2 from Capotauro v2.0. Related: Reading C variants, $\hat{n}$, FI-C-RC-2.

### Edge-aligned Reading C / face-aligned Reading C
The two non-vertex-aligned Reading C variants in the 600-cell substrate. Edge-aligned: $\hat{n}$ along a 600-cell short-edge direction, giving residual symmetry $D_3$ at the edge midpoint. Face-aligned: $\hat{n}$ perpendicular to a triangular face, giving residual symmetry $D_2$ at the face centroid. Out of scope at this paper; extension is OPEN-FP-F1-5. First use: §9 (OPEN-FP-F1-5 statement). Related: vertex-aligned Reading C, OPEN-FP-F1-5.

### Regular icosahedron
The 12-vertex polyhedron in 3D with full icosahedral symmetry $I_h = H_3$. Forms the geometric structure of the first-shell. First-shell-edge dihedral angle $\cos(36°) = \phi/2$. First use: §3.2. Related: first-shell, $H_3 = I_h$, dihedral angle.

### First-shell unit vector $\hat{u}_i$
The unit vector from $\vhost$ to the $i$-th first-shell neighbour: $\hat{u}_i = (v_i - \vhost)/|v_i - \vhost|$. There are 12 such vectors forming a regular icosahedron of unit vectors. Theorem 5.1: $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ uniform. First use: §3.3. Related: first-shell, host vertex, Theorem 5.1.

### First-shell-to-first-shell edge $\hat{e}_{ij}$
An edge of the 600-cell connecting two first-shell vertices $v_i$ and $v_j$ (necessarily sharing an icosahedral edge). 30 such edges total. Edge direction $\hat{e}_{ij}$ is perpendicular to $\hat{n}$ at vertex-aligned Reading C: $\hat{e}_{ij} \cdot \hat{n} = 0$ (Theorem 5.2). First use: §5.4. Related: first-shell, Theorem 5.2.

### G1 — first-shell inner-product primitive
The structural identity that the first-shell unit-vector inner-product matrix $\{\hat{u}_i \cdot \hat{u}_j\}_{i,j=1}^{12}$ takes a fixed icosahedral-symmetric form determined by the 600-cell first-shell-edge dihedral angle $\cos(36°) = \phi/2$ + unit-vertex normalization on $S^3$ + icosahedral residual symmetry $H_3 = I_h$. **Status: sketch-document Layer 3** (imported from Patch 0541 §3.1 derivation). Publication-grade hardening is OPEN-FP-F1-3 (RECOMMENDED first post-Phase-7 substantive physics Patch). First use: §3.3. Related: G2, OPEN-FP-F1-3, Theorem 5.1, Theorem 5.2, exclusion class E1.

### G2 — first-shell edge-direction projection primitive
The structural identity that first-shell-to-first-shell edge directions $\hat{e}_{ij}$ are perpendicular to $\hat{n}$. Follows from the icosahedral first-shell structure + the fact that the 30 first-shell-to-first-shell edges lie in the "equatorial" 3-plane perpendicular to the host vertex. First use: §3.3. Related: G1, Theorem 5.2, first-shell-to-first-shell edge.

---

## Mechanism terms

### DI-bit
**Discrete Information bit.** The fundamental quantum of substrate information transfer in CPP, transferred between adjacent vertices of the 600-cell substrate along edges via Polarize-Capture-Depolarize (PCD) cycle dynamics. First use: §3.4. Related: PCD cycle, propagation rate, DI-bit current.

### DI-bit current $\vec{j}_{DI}^{\text{net}}(v)$
The net flow of DI-bits at vertex $v$ summed over incident edges, weighted by the orientation-asymmetry-weighted Mechanism A propagation rates. The substrate-locality result Theorem 7.1 gives the closed-form expression $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$ at the host vertex at first order. First use: paper title + abstract + §3.4. Related: DI-bit, Mechanism A, substrate-locality, Theorem 7.1.

### Mechanism A
The propagation-rate-asymmetry primitive taken as framework axiom at Layer 3 input. Two-part axiom: **MA.1** (Propagation-rate asymmetry): for an oriented edge with unit-direction $\hat{e}$, the DI-bit propagation rate is $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$. **MA.2** (Framework-local current construction): at first order in $\delta$, the DI-bit current contribution from edges at a vertex is constructed locally via the orientation-asymmetry-weighted rates. Layer 4 axiomatic derivation from CPP primitive axioms A1–A11 is OPEN-FP-F1-2. First use: §4 (Mechanism A as framework axiom). Related: propagation rate, $\delta$, framework axiom, OPEN-FP-F1-2.

### Propagation rate $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$
The DI-bit propagation rate along an oriented edge with unit-direction $\hat{e}$. Encodes Mechanism A's directional bias: edges parallel to $\hat{n}$ propagate at rate $r_0(1+\delta)$ (faster); anti-parallel at $r_0(1-\delta)$ (slower); perpendicular at $r_0$ (base rate). First use: §4.1 (Mechanism A axiom MA.1). Related: Mechanism A, $\delta$, $r_0$, edge orientation.

### Substrate-direction primitive $\hat{n}$
A primitive 4D direction (unit vector on $S^3$) that selects the substrate's preferred orientation. The chirality continuum architecture (Capotauro v2.0 + F.1) treats $\hat{n}$ as a foundational structural input from which spatial-sector manifestations (i)–(iii) and temporal-sector manifestation (iv) derive. At vertex-aligned Reading C, $\hat{n} = \vhost$. Imported as foundational input FI-C-RC-1 from Capotauro v2.0. First use: §3.2. Related: vertex-aligned Reading C, FI-C-RC-1, OPEN-SD-CHIR-PRIMITIVE.

### Substrate-locality structure
The property that the substrate physics at any vertex depends only on a topologically local region of the substrate (here: first-shell content at first order in $\delta$). The substrate-locality theorem (Theorem 7.1) makes this structure quantitative at the closed-form level. **Not synonymous with thermodynamic-arrow emergence**, which is the candidate mechanism narrative *supported by* substrate-locality but explicitly *not derived from* it at the present paper's scope (§10 disclaimer). First use: abstract + §1. Related: Theorem 7.1, thermodynamic causal arrow, manifestation (iv), §10 disclaimer.

### OPEN-SD-CHIR-PRIMITIVE
The CPP open-problem umbrella registering the substrate-direction primitive $\hat{n}$ as a research target. Manifestations (i)–(iv) closed at Layer 3 (Capotauro v2.0 closes (i)–(iii) at spatial sector; F.1 closes (iv) at temporal sector at sketch-document Layer 3). Manifestation (v) is OPEN-FP-F1-4 (Sector-5 schema instantiation). First use: §2.1 (Manifestation (iv) of OPEN-SD-CHIR-PRIMITIVE). Related: chirality continuum, manifestation (iv), OPEN-FP-F1-4.

### Manifestation (iv) — thermodynamic causal arrow
The fourth of five registered manifestations of OPEN-SD-CHIR-PRIMITIVE. The thermodynamic causal arrow is the manifestation closed at sketch-document Layer 3 by F.1 via the substrate-locality structure of Theorem 7.1. **Closure at substrate-locality level only**: the candidate mechanism narrative for thermodynamic-arrow emergence (entropy production / coarse-graining / macroscopic irreversibility) is *supported by* but *not derived from* the closure. First use: §1 + §2.1. Related: OPEN-SD-CHIR-PRIMITIVE, substrate-locality structure, thermodynamic-arrow emergence disclaimer (§10).

### Chirality continuum
The CPP programme's structural architecture organizing OPEN-SD-CHIR-PRIMITIVE's five manifestations under a common substrate-direction primitive $\hat{n}$. Established at Capotauro v2.0 + chirality continuum sketch document. F.1 instantiates manifestation (iv); manifestations (i)–(iii) instantiated at Capotauro v2.0; manifestation (v) is open as OPEN-FP-F1-4. First use: §1.1. Related: OPEN-SD-CHIR-PRIMITIVE, Capotauro v2.0, manifestation hierarchy.

### Minimal-local-first-order realization framework
The methodological framework establishing three minimality constraints (locality + first-order in $\delta$ + single-direction primitive $\hat{n}$) that jointly identify the unique Mechanism A framework form. Operationalises the "minimal" character of the propagation-rate-asymmetry primitive. First use: §2.4. Related: Mechanism A, framework axiom.

### Conscious Point (CP) / DI-bit / PCD cycle
The three CPP primitive substrate constructs (per A1 + A6′ of the CPP primitive axioms). **CP**: the fundamental conscious-substrate quantum. **DI-bit**: the discrete-information unit transferred between CPs. **PCD cycle**: the Polarize-Capture-Depolarize discrete-time elementary process. Not derived in F.1 (they are A1 + A6′ inputs); referenced as the underlying substrate physics from which Mechanism A would derive at Layer 4 (OPEN-FP-F1-2). First use: §3.1 (CPP primitive axioms A1–A11 recap). Related: A1, A6′, OPEN-FP-F1-2.

---

## Methodology terms

### Sketch Layer 1 / Layer 2 / Layer 3 / Layer 4 hierarchy
The CPP corpus's four-Layer epistemic hierarchy for derivation rigor:

- **Layer 1**: structural / suggestive identification of the question; informal scoping.
- **Layer 2**: substantive derivation work with explicit hypothesis tracking; sketch-document level.
- **Layer 3**: complete derivation at publication-grade rigor (with explicit hypothesis tracking + five-class exclusion enumeration). Two sub-tiers: sketch-document Layer 3 (umbrella assembly without independent hardening) vs publication-grade Layer 3 (independently hardened).
- **Layer 4**: axiomatic derivation from CPP primitive axioms A1–A11 alone (no framework axioms).

First use: §1.3 (Sketch Layer 2 to Layer 3 trajectory recap). Related: anti-erasure discipline, Layer-distinction discipline.

### Sketch-document Layer 3
A derivation result that is structurally complete and at Layer 3 rigor *in the sketch-document sense* (e.g., assembly of publication-grade Layer 3 inputs without independent hardening of the assembly itself). Theorem 7.1 (substrate-locality umbrella) is at sketch-document Layer 3; Lemma "G1 first-shell inner-product primitive" is also at sketch-document Layer 3. Status preserved transparently per the anti-erasure discipline. First use: §1.3. Related: publication-grade Layer 3, anti-erasure discipline, Theorem 7.1, G1.

### Publication-grade Layer 3
A Layer 3 derivation result independently hardened in a dedicated `hardened_theorems/*.tex` artifact with explicit hypothesis tracking + five-class exclusion enumeration + integration as direct building block into the umbrella theorem. The F.1 trio at `hardened_theorems/` (Patches 0550 + 0551 + 0552) supplies the publication-grade Layer 3 inputs (perturbation-locality + first-shell-to-first-shell perpendicularity + host-to-first-shell uniform projection) to Theorem 7.1. First use: §5.1 (Theorem 5.1 statement parenthetical). Related: sketch-document Layer 3, hardened-theorem artifact, hardened_theorems trio.

### Hardened-theorem artifact
A self-contained `.tex` file under `hardened_theorems/` directory providing a publication-grade Layer 3 derivation with explicit hypothesis tracking + isolation of structural inputs + five-class exclusion enumeration. Three F.1 hardened-theorem artifacts exist at v1.0 SHIP: Patch 0550 (perturbation-locality), Patch 0551 (first-shell-to-first-shell perpendicularity), Patch 0552 (host-to-first-shell uniform projection); 741 lines LaTeX combined. Pattern established for F-line flagship trajectories. First use: §5.1. Related: publication-grade Layer 3, five-class exclusion enumeration.

### Five-class exclusion enumeration
The publication-grade Layer 3 standard requiring identification of five structural exclusion conditions that, if violated, would invalidate the derivation. For F.1's perturbation-locality artifact (Patch 0550), the five classes are: E1 G1 dependency, E2 edge-graph connectivity, E3 path-amplitude expansion convergence, E4 perturbation-theory orientation consistency, E5 Mechanism A locality. First use: §6.6. Related: hardened-theorem artifact, exclusion class E1.

### Exclusion class E1 (shared G1 dependency)
The exclusion class shared between Theorems 5.1 and 5.2 (and via §5 trio also Theorem 7.1): both theorems are conditional on G1 (first-shell inner-product primitive) being valid. If G1 fails (e.g., the icosahedral first-shell structure is somehow invalid), both Theorems 5.1 + 5.2 fail. OPEN-FP-F1-3 closure (G1 publication-grade hardening) would discharge this conditionality. First use: §5.5. Related: G1, OPEN-FP-F1-3, Theorems 5.1 + 5.2.

### Framework axiom
A substrate-physics commitment taken as input at Layer 3 derivation level, distinct from the CPP primitive axioms A1–A11 (Layer 4 inputs). Mechanism A (MA.1 + MA.2) is the canonical example for F.1; Layer 4 axiomatic derivation of Mechanism A from A1–A11 is OPEN-FP-F1-2. First use: §4.3. Related: Mechanism A, OPEN-FP-F1-2, Layer 4.

### Anti-erasure discipline
The methodological discipline of preserving (a) the Layer distinction between publication-grade L3 trio and sketch-document L3 umbrella, (b) the conditionality of Theorems 5.1 + 5.2 on G1, and (c) the explicit open higher-order questions during paper polishing. Named explicitly at §8.3 ("anti-erasure discipline") + operationalised at three concrete points in §10. Emerged from ChatGPT R2–R6 reviewer pressure: *"Do not erase the uncertainty structure during paper polishing. That would be a mistake."* First use: §1.4 (Paper roadmap and Layer-distinction discipline). Related: Layer-distinction discipline, calibration discipline.

### Calibration discipline
The Patch-level discipline of preserving theorem statements, proofs, Open Problems, hardened-theorem artifacts, bibliography, abstract, body, and author block content unchanged during reviewer-cycle response Patches. Sustained across Patches 0568 → 0570 (entire v0.9 → v1.0 SHIP cycle); the 5-Open-Problem body §9 commitment preserved end-to-end. First use: §1.4. Related: anti-erasure discipline, reviewer-cycle protocol.

### Layer-distinction discipline
The structural commitment to maintain the publication-grade vs sketch-document Layer 3 distinction visible at theorem-statement, paper-section, and table-row granularity. Operationalised at §8.2 (per-theorem Layer hierarchy explicit table) + parenthetical Layer labels in every theorem statement. First use: §1.4. Related: anti-erasure discipline, §8.2 Layer hierarchy table, sketch-document Layer 3.

### Structurally-grounded sketch-document Layer 3 flagship framework preprint
The paper-type declaration for F.1 v1.0 SHIP, captured in the title-page scope subtitle (Variant b `\date{}` line scope-framing). Four claims compressed: (1) "structurally-grounded" — the paper rests on the explicit Layer 3 trio; (2) "sketch-document Layer 3" — the umbrella theorem is at sketch-document Layer 3 only; (3) "flagship framework preprint" — F-line flagship trajectory paper, not a finished publication; (4) "publication-grade hardened components but non-publication-grade umbrella theorem" — the Layer-distinction structure made first-reader-visible. First use: title-page `\date{}` line + §1 + abstract. Related: anti-erasure discipline, paper-type declaration, scope-framing subtitle convention.

### Anti-priorities (sustained throughout SHIP cycle)
Items explicitly held NOT-to-be-done during reviewer-cycle work: theorem-statement modifications, proof modifications, Open Problem modifications, hardened-theorem artifact modifications, bibliography body modifications, governance-language reduction (declined per all three R1 reviewers' praise of the Layer-distinction discipline). First use: methodology applied throughout Patches 0568–0570 reviewer cycle. Related: calibration discipline.

### Reviewer-pause cycle
The CPP corpus methodology for closure-milestone external review before flagship paper assembly. Specified at `templates/operating_system.md` §17 + `templates/paper_completion_checklist.md` "Reviewer-Pause Cycle Precondition for Flagship-Paper-Trajectory Work" section. F.1 trajectory is the canonical worked example: Patches 0531–0537 closed seven sub-questions at sketch Layer 2 → Patch 0538 calibration response → Patch 0539 status upgrade → further calibration cycles + Layer 3 promotion → flagship paper assembly Patches 0554–0570. First use: handover §5 + sketch documents. Related: foundations work, Layer 3 promotion, flagship-paper-trajectory.

### Foundational input (FI)
A structural input registered at programme level that grounds a derivation without being itself derived at the present paper's scope. F.1 uses FI-C-RC-1 (primitive 4D direction $\hat{n}$) + FI-C-RC-2 (vertex-aligned reading) inherited from Capotauro v2.0's Reading C closure trajectory. First use: §3.1. Related: Capotauro v2.0, vertex-aligned Reading C, $\hat{n}$.

---

## Status labels

### PROVED at Layer N
A theorem with complete derivation at the specified Layer rigor. F.1 has 4 theorems PROVED at publication-grade Layer 3 (Theorems 5.1, 5.2, 6.1, Corollary 6.2; the first two conditional on G1) + 1 theorem PROVED at sketch-document Layer 3 (Theorem 7.1).

### CONDITIONAL on X
A theorem whose derivation depends on an unproven input X. Theorems 5.1 + 5.2 are conditional on G1. Promotion to unconditional pending G1 hardening (OPEN-FP-F1-3).

### FRAMEWORK AXIOM
A substrate-physics commitment taken as input at Layer 3 rigor; not derivable from A1–A11 at the present paper's scope. Mechanism A axioms MA.1 + MA.2 are framework axioms. Layer 4 axiomatic derivation is OPEN-FP-F1-2.

### OPEN-FP-F1-N
A registered Open Problem in the F.1 paper's body §9. Five registered at body §9: OPEN-FP-F1-1 ($\mathcal{O}(\delta^2)$ extension), OPEN-FP-F1-2 (Layer 4 axiomatic derivation), OPEN-FP-F1-3 (G1 publication-grade hardening), OPEN-FP-F1-4 (Sector-5 schema instantiation), OPEN-FP-F1-5 (non-vertex-aligned Reading C variants). OPEN-FP-F1-6 (prose-density tightening) registered separately at Patch 0569e from R6 follow-up. F.1 sub-question itself is **CLOSED at sketch-document Layer 3** at v1.0 SHIP.

### CLOSED at Layer N
A previously-open programme question whose closure has been registered at the specified Layer rigor. F.1 closes manifestation (iv) of OPEN-SD-CHIR-PRIMITIVE at sketch-document Layer 3 via Theorem 7.1.

### REGISTERED (THEO-DSL-1 / 2 / 3 candidates)
A theorem registered as a candidate for the programme-level theorem-registry at Phase 7B Patch 0573-ish. Three candidates from F.1: THEO-DSL-1 (Theorem 6.1 + Corollary 6.2; publication-grade Layer 3 unconditional); THEO-DSL-2 (Theorems 5.1 + 5.2; publication-grade Layer 3 conditional on G1); THEO-DSL-3 (Theorem 7.1; sketch-document Layer 3). Theorem-registry update is DEFERRED to Phase 7B per handover §6 Step E.

---

*Glossary file created Session 143 Patch 0572d (24 May 2026) as the fifth SHIP-time companion documentation file in Phase 7A. Per `templates/documentation-suite.md` §2 + checklist §A A2 (Constants + Structural + Mechanism + Methodology categories + Status labels) + Capotauro reference implementation `glossary-capotauro.md` category structure. Source priorities per docsuite.md §32: items 1 + 2 + 9 (sketches + reasoning + `.tex` source). This file is maintained continuously from this Patch forward; future paper-version increments trigger entry extensions (e.g., G1 publication-grade hardening at OPEN-FP-F1-3 closure would promote G1 status from sketch-document Layer 3 to publication-grade Layer 3) but do not modify existing v1.0 SHIP definitions.*
