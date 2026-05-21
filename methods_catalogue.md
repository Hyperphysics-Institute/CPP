# Methods Catalogue — Conscious Point Physics Programme

**Status:** Programme-level catalogue of novel methodological techniques established across CPP flagship papers and theorem closures.

**Established:** 20 May 2026 (Session 137 Patch 0498; first programme-level methods catalogue creation; initial population from the chirality continuum joint paper §3 bridge work).

**Last updated:** 20 May 2026 (Session 137 Patch 0509 — **Chirality continuum joint paper v1.0 SHIPPED; METH-CHIR-CONT-1 through -4 paper-of-origin venue final consolidation**). All four METH-CHIR-CONT entries (METH-CHIR-CONT-1 sector-agnostic substrate Wigner-Eckart datum + METH-CHIR-CONT-2 continuum-limit projection map $\Phi$ via Wilson-Fisher block-spin renormalization + METH-CHIR-CONT-3 topological substrate quantity + METH-CHIR-CONT-4 topological-projection argument) have their paper-of-origin venue confirmed at `flagship_papers/chirality_continuum/chirality_continuum.tex` v1.0 SHIPPED §3. METH-CHIR-CONT-3 (topological substrate quantity) and METH-CHIR-CONT-4 (topological-projection argument) carry **programme-level concept** status per theorem-registry entries — available for future cross-sector Layer 4 closures under OPEN-SD-CHIR-PRIMITIVE umbrella manifestations (iv) thermodynamic causal arrow + (v) cosmological-vacuum asymmetry via THEO-CHIR-CONT-4/-5 candidates and applicable to other substrate-handle inheritance closures programme-wide.

**Maintained by:** Programme-level documentation. Updated as new methodological constructs are introduced through flagship paper substantive derivation work.

---

## Purpose

The methods catalogue tracks novel reasoning methods, mathematical techniques, and structural abstractions introduced through CPP substantive derivation work, so that:

1. **Programme-level inheritance**: subsequent work can cite the catalogued method by identifier rather than re-deriving the technique from scratch. Identifiers (METH-N) parallel the theorem registry's THEO-N identifiers for programme-level inheritance discipline.

2. **Cross-paper citation**: methods established in one flagship paper become available infrastructure for subsequent papers. This is the methodological analog of theorem registry inheritance.

3. **Methodological transparency**: novel techniques are surfaced explicitly in papers via methods catalogue references (e.g., `\methref{METH-CHIR-CONT-3}` for the topological substrate quantity concept). Reviewers and readers can locate the precise definition + scope + dependencies + provenance of each technique in one place rather than scanning multiple papers.

4. **Reviewer-cycle anti-priority**: catalogued methods are explicit programme commitments. Reviewers can identify which constructs are novel-to-CPP versus inherited from standard machinery, and direct critique accordingly.

---

## Naming convention

Identifiers follow the pattern `METH-<prefix>-N` where:

- `METH` is the constant prefix marking a methods-catalogue entry (parallel to `THEO` for theorems, `PROP` for propositions, `LEMMA` for lemmas, `FI` for foundational inputs, `PRED` for predictions, `OPEN` for open problems).

- `<prefix>` indicates the source paper / theorem family. Initial conventions:
  - `METH-CHIR-CONT-N`: methods introduced in the chirality continuum joint paper (this catalogue's initial source).
  - Future conventions to mirror theorem registry: `METH-CAP-N` (Capotauro), `METH-SD-N` (SD series), `METH-SF-N` (SF series), `METH-SS-N` (SS series), `METH-EW-N` (EW series), `METH-SM-N` (SM series), `METH-QM-N` (QM series), `METH-SR-N` (SR series).

- `N` is sequential within the prefix.

Retroactive cataloguing of methods from earlier CPP work is permitted as the programme matures; entries can be added in the order they are surfaced rather than the order they were originally developed. Each entry's `Provenance` field records the substantive derivation context where the method first appeared in the programme.

---

## Catalogue structure

Each entry contains:

- **Identifier**: `METH-<prefix>-N`.
- **Name**: short descriptive name suitable for paper-text reference.
- **Statement**: precise formal statement / definition / theorem capturing the methodological construct.
- **Scope**: where the method applies + sector/context restrictions.
- **Dependencies**: foundational inputs + axioms + parent theorems / methods inherited.
- **Provenance**: where the method first appeared (paper / patch / theorem-registry entry).
- **Standard-machinery context**: relationship to standard mathematical/physical machinery; identifies what is novel-to-CPP vs inherited.
- **Cross-paper usage**: subsequent papers / closures that have cited this method via identifier.

---

## Entries

### METH-CHIR-CONT-1: Sector-Agnostic Substrate Wigner-Eckart Datum

**Identifier**: METH-CHIR-CONT-1

**Name**: Sector-Agnostic Substrate Wigner-Eckart Datum

**Statement**: A *sector-agnostic substrate Wigner-Eckart datum* is a tuple
$$\mathcal{D}^{\text{sub}} = (\mathcal{S}, \Gamma, \zeta, \hat{C}, \{|\Psi_+\rangle, |\Psi_-\rangle\}, M)$$
where:
- $\mathcal{S}$ is a substrate object on the first-shell icosahedron at the host 600-cell vertex;
- $\Gamma \subset H_3 = I_h$ is the stabilizer subgroup of $\mathcal{S}$ in the substrate residual symmetry;
- $\zeta \in \Gamma$ is the $\mathbb{Z}_2$ pairing-convention generator;
- $\hat{C}$ is the chirality operator in a $\zeta$-ODD 1D irrep of $\Gamma$;
- $\{|\Psi_+\rangle, |\Psi_-\rangle\}$ is the matter-doublet basis in a 2D subspace of $\Gamma$-irreps with $\zeta$-EVEN and $\zeta$-ODD components respectively;
- $M = \langle \Psi_+ | \hat{C} | \Psi_- \rangle$ is the substrate-level matrix element.

A datum is *valid* if the matrix element admits the factorization
$$M = \pm\chi \cdot \frac{d_\Gamma}{V_{\text{cage}}}$$
with universal data $|\chi| = \varphi^{-3}$, $d_\Gamma = 2$, $V_{\text{cage}} = 12$, yielding $|M| = \chi/6 \approx 0.0394$.

**Scope**: applies to any sector under the OPEN-SD-CHIR-PRIMITIVE umbrella whose substrate object lives on the first-shell icosahedron at a 600-cell host vertex. Verified valid at the three Capotauro v2.0 sectors (K3-doublet via THEO-CAP-1; W-bracelet via THEO-SD-CHIR-1; qDP/eDP via THEO-SD-CHIR-2). Designed to extend to manifestations (iv) thermodynamic causal arrow + (v) cosmological-vacuum asymmetry under same umbrella when substrate-level closures are completed for those manifestations.

**Dependencies**:
- Substrate residual symmetry $H_3 = I_h$ at host vertex (FI-CHIR-CONT-3).
- Substrate primitive 4D direction $\hat{n}$ at vertex-aligned Reading C (FI-CHIR-CONT-1).
- Substrate chirality magnitude $|\chi| = \varphi^{-3}$ (FI-CHIR-CONT-2).
- Substrate-Locality Theorem of Capotauro v2.0 (FI-CHIR-CONT-9).
- THEO-CAP-1 + THEO-SD-CHIR-1 + THEO-SD-CHIR-2 (three sector instantiations supplying universal data $(|\chi|, d_\Gamma, V_{\text{cage}}) = (\varphi^{-3}, 2, 12)$).

**Provenance**: First introduced as Definition 3.2.1 of the joint paper §3 working sketch `flagship_papers/chirality_continuum/sketches/substrate_to_continuum_bridge.md` (Session 137 Patch 0485). Promoted to paper-level Definition 3.1 of `chirality_continuum.tex` at Patch 0498. Load-bearing content of Step 1 of the Theorem 3.4 = THEO-CHIR-CONT-1 proof chain.

**Standard-machinery context**: The Wigner-Eckart structure $(\Gamma, \zeta, \hat{C}, \text{matter-doublet}, M)$ specializes the standard Wigner-Eckart theorem of representation theory \cite{WignerEckart} to the substrate-physics context with a $\mathbb{Z}_2$ pairing-convention generator providing the parity-content bookkeeping. The novel-to-CPP content is the *abstraction across sectors* identifying universal data $(|\chi|, d_\Gamma/V_{\text{cage}})$ as the load-bearing magnitude content with sector-specific data $(\Gamma, \zeta, \hat{C})$ entering only as labels. The abstraction makes possible the sector-agnostic bridge step closure (METH-CHIR-CONT-2 through METH-CHIR-CONT-4).

**Cross-paper usage**: Used at chirality continuum joint paper §3.1 (Definition 3.1 introduction), §3.2 (validity verification across three sectors via Table 3.1), §3.3 (continuum-limit projection setup at sector-agnostic level), §3.4 (Lemma 3.1 = THEO-CHIR-CONT-1.1 inherits abstraction), §3.5 (Theorem 3.2 = THEO-CHIR-CONT-1.2), §3.7 (Theorem 3.3 = THEO-CHIR-CONT-1.3), §3.8 (Theorem 3.4 = THEO-CHIR-CONT-1 statement). Inherited at §4.1 (Sector A W-bracelet sector instantiation), §4.2 (Identification 1 sector-specific operator identification). Inherited at §5.1 (Sector B qDP/eDP sector instantiation), §5.2 (Identification 1 sector-specific operator identification), §5.3 (substrate-level Wigner-Eckart factorization for stabilization energy). Inherited at §6.1 (three sector instantiations validating shared substrate handle), §6.5 (sector-agnostic data abstraction at structural-efficiency mechanism).

---

### METH-CHIR-CONT-2: Continuum-Limit Projection Map $\Phi$ via Wilson-Fisher Block-Spin Renormalization at Substrate Cutoff

**Identifier**: METH-CHIR-CONT-2

**Name**: Continuum-Limit Projection Map $\Phi$ via Wilson-Fisher Block-Spin Renormalization at Substrate Cutoff

**Statement**: For a substrate Wigner-Eckart datum $\mathcal{D}^{\text{sub}}$ on the 600-cell substrate lattice with edge-length $\ell_{\text{edge}}$ setting the substrate cutoff $\Lambda_{\text{sub}} = \ell_{\text{edge}}^{-1}$, the *continuum-limit projection map* is a linear map
$$\Phi: \mathcal{H}^{\text{sub}} \to \mathcal{H}^{\text{cont}}$$
obtained as the standard Wilson-Fisher block-spin renormalization limit \cite{WilsonKogut, KadanoffBlock} as $a \to 0$ keeping observable correlation lengths $L$ fixed, subject to three construction conditions:

- **Block-spin commutativity**: $\Phi$ commutes with discrete symmetry actions by construction (Wilson-Fisher block-spin preserves block symmetries).
- **Continuum-limit existence**: $\Phi$ is well-defined in the $a \to 0$ limit at any fixed continuum scale $\mu < \Lambda_{\text{sub}}$.
- **Equivariance**: For any discrete symmetry $g \in I_h$ acting on substrate states, $\Phi(g \cdot |\Psi^{\text{sub}}\rangle) = g^{\text{cont}} \cdot \Phi(|\Psi^{\text{sub}}\rangle)$ where $g^{\text{cont}}$ is the continuum-limit action of $g$ on $\mathcal{H}^{\text{cont}}$.

The induced map on operators is $\Phi_*: \text{Op}(\mathcal{H}^{\text{sub}}) \to \text{Op}(\mathcal{H}^{\text{cont}})$, $\Phi_*\hat{O}^{\text{sub}} = \Phi \hat{O}^{\text{sub}} \Phi^{-1}$ via standard Wilson-Fisher operator-projection machinery.

**Scope**: applies wherever a discrete substrate lattice projects to a continuum field theory at scales $\mu \ll \Lambda_{\text{sub}}$. In the CPP context, the substrate cutoff $\Lambda_{\text{sub}} = \ell_{\text{edge}}^{-1}$ at the 600-cell edge length sets the natural ultraviolet scale; observable kinematic scales (electroweak $\sim 10^2$ GeV; SM-2 thermodynamic $\sim 10^{-3}$ to $10^{16}$ K) sit in the deep-infrared regime $a/L \ll 10^{-15}$. Method is sector-agnostic by construction.

**Dependencies**:
- Substrate residual symmetry $H_3 = I_h$ at host vertex (FI-CHIR-CONT-3).
- Substrate-Locality Theorem of Capotauro v2.0 (FI-CHIR-CONT-9; ensures substrate locality is preserved under block-spin renormalization).
- Standard Wilson-Fisher block-spin machinery \cite{WilsonKogut, KadanoffBlock} for the underlying renormalization-group framework.

**Provenance**: First introduced as Definition 11.2.1 of the joint paper §3 working sketch (Session 137 Patch 0486). Promoted to paper-level Definition 3.2 of `chirality_continuum.tex` at Patch 0498. Load-bearing content of Step 2 of the Theorem 3.4 = THEO-CHIR-CONT-1 proof chain.

**Standard-machinery context**: Wilson-Fisher block-spin renormalization is a standard tool of statistical-mechanics / lattice-field-theory \cite{WilsonKogut}. The novel-to-CPP content is the specialization to the discrete 600-cell polytope-geometric substrate with the equivariance condition explicitly imposed at construction time. The equivariance condition is what enables Lemma 3.1 (Symmetry-Content Preservation under $\Phi$ = THEO-CHIR-CONT-1.1) and downstream sector-agnostic operator identification (Theorem 3.2 = THEO-CHIR-CONT-1.2). The substrate cutoff identification $\Lambda_{\text{sub}} = \ell_{\text{edge}}^{-1}$ at the 600-cell edge length is CPP-specific and is the cleanest natural choice given AXIM-2.

**Cross-paper usage**: Used at chirality continuum joint paper §3.3 (Definition 3.2 introduction), §3.4 (Lemma 3.1 = THEO-CHIR-CONT-1.1 inherits equivariance), §3.5 (Theorem 3.2 = THEO-CHIR-CONT-1.2 uses $\Phicont\hat{C}^{\text{sector}}$), §3.7 (Theorem 3.3 = THEO-CHIR-CONT-1.3 uses $\Phi$ for topological projection), §3.8 (Theorem 3.4 = THEO-CHIR-CONT-1 statement). Sub-statements THEO-CHIR-CONT-1.1, -1.2, -1.3 all inherit from METH-CHIR-CONT-2. Inherited at §4.2 Identification 1 (sector A continuum-limit projection of $\zeta^W$ to $\gamma_5$). Inherited at §5.2 Identification 1 (sector B continuum-limit projection of $\zeta^{qDP}$ to combined $CP$). Synthesis at §6.1+§6.4+§6.5 references sector-agnostic projection framework.

---

### METH-CHIR-CONT-3: Topological Substrate Quantity Concept

**Identifier**: METH-CHIR-CONT-3

**Name**: Topological Substrate Quantity Concept

**Statement**: A *topological substrate quantity* is a dimensionless substrate-level quantity whose value is determined entirely by:

- The combinatorial-geometric structure of the substrate polytope (vertex counts, edge-length ratios, irrep dimensions, stabilizer-subgroup orders);
- Primitive feature identifications (e.g., $\hat{n} = v_{\text{host}}$);

*without dependence on*:

- Substrate-field-theoretic dynamics (no Lagrangian, no Hamiltonian, no action principle);
- RG-flow scale parameters (no running coupling, no anomalous dimension);
- Dynamical degrees of freedom evolving in time.

A quantity satisfying these conditions is structurally analogous to a topological invariant in continuum quantum field theory: integer-valued topological charges (winding numbers, Chern-Simons levels), index-theorem contributions, anomaly coefficients (with the anomaly coefficient's $1/(16\pi^2)$ structure being the continuum-QFT analog), and discrete symmetry parities. The structural analogy with continuum-QFT topological invariants is what justifies the protection-under-continuum-limit property exploited by METH-CHIR-CONT-4 (Topological-Projection Argument).

**Scope**: applies to any dimensionless substrate-level quantity derived from combinatorial-geometric / representation-theoretic structure of the substrate polytope. In the chirality continuum joint paper, two substrate quantities are catalogued as topological:

- $|\chi| = \varphi^{-3}$: substrate chirality magnitude, derived from substrate primitive 4D direction $\hat{n}$ + 600-cell polytope edge-length ratios via perturbative-distance-ratio constraint (Capotauro v2.0 §sec:chi_resolution + Finding C-W39). Verified at Claim 15.1.2.
- $1/6 = d_\Gamma/V_{\text{cage}} = 2/12$: cage-shell factor, ratio of two integer-valued topological invariants (matter-doublet 2D-irrep dimension + first-shell icosahedron 12-vertex count). Verified at Claim 15.2.1.

Extends naturally to other substrate quantities in CPP framework: edge-length ratios within 600-cell, stabilizer-subgroup orders, irrep dimensions, vertex/face/cell counts of the 600-cell, perturbative geometric corrections of $\mathcal{O}(\epsilon^n)$ for combinatorially-derived $\epsilon$.

**Dependencies**:
- 600-cell substrate topology axiom AXIM-2 (provides the polytope-geometric structure that all topological substrate quantities depend on).
- Substrate primitive 4D direction (FI-CHIR-CONT-1) — for quantities depending on primitive feature identifications.
- Standard QFT protection-of-topological-quantities principle \cite{AdlerBardeen, AtiyahSinger, Witten1983CS} — for the structural analogy that justifies METH-CHIR-CONT-4's continuum-projection-preserves-magnitude inference.

**Provenance**: First introduced as Definition 15.1.1 of the joint paper §3 working sketch (Session 137 Patch 0487). Promoted to paper-level Definition 3.3 of `chirality_continuum.tex` at Patch 0498. Load-bearing concept of Step 4 of the Theorem 3.4 = THEO-CHIR-CONT-1 proof chain. **Programme-level concept** available for future cross-sector Layer 4 closures under any umbrella where substrate magnitudes are derived from combinatorial-geometric structure.

**Standard-machinery context**: The topological-substrate-quantity concept is the CPP-substrate analog of the topological-invariant concept in continuum quantum field theory. In continuum QFT, topological invariants are protected from quantum corrections at all loop orders by index-theorem and cohomological arguments (Adler-Bardeen anomaly nonrenormalization \cite{AdlerBardeen}; Atiyah-Singer index theorem \cite{AtiyahSinger}; Chern-Simons level integrality \cite{Witten1983CS}). The novel-to-CPP content of METH-CHIR-CONT-3 is the *identification* of which substrate quantities qualify as topological in this sense + the *structural justification* for projecting them through the continuum-limit map $\Phi$ without renormalization.

**Cross-paper usage**: Used at chirality continuum joint paper §3.6 (Definition 3.3 introduction; Claims 3.1 + 3.2 establishing topological character of $|\chi|$ and $\dGamma/\Vcage$), §3.7 (Theorem 3.3 magnitude inheritance argument), §3.8 (Theorem 3.4 = THEO-CHIR-CONT-1). Inherited at §4.2 Identification 3 (sector A magnitude inheritance $\chi/6$). Inherited at §5.2 Identification 3 (sector B magnitude inheritance) + §5.3 (topological character of $\chi$ and cage-shell factor at qDP/eDP sector). Synthesis at §6.5 references topological substrate quantity concept. Anticipated future use: any CPP closure that needs to argue a substrate-level dimensionless quantity is preserved under continuum-limit projection (manifestations (iv)+(v) Layer 4 closures via THEO-CHIR-CONT-4/-5 candidates).

---

### METH-CHIR-CONT-4: Topological-Projection Argument

**Identifier**: METH-CHIR-CONT-4

**Name**: Topological-Projection Argument

**Statement**: Let $Q^{\text{sub}}$ be a topological substrate quantity in the sense of METH-CHIR-CONT-3 (Definition 3.3 in paper terms), and let $\Phi$ be the continuum-limit projection map per METH-CHIR-CONT-2 (Definition 3.2 in paper terms). Then $Q^{\text{sub}}$ projects through $\Phi$ to a continuum-limit quantity $Q^{\text{cont}}$ satisfying:

$$Q^{\text{cont}} = Q^{\text{sub}} \cdot (1 + \mathcal{O}((a/L)^n))$$

for some $n \geq 1$, where $a = \ell_{\text{edge}}$ is the substrate cutoff scale and $L = \mu_{\text{obs}}^{-1}$ is the inverse observable scale. In the deep-infrared regime $a/L \ll 1$ — which holds for all standard-model-observable kinematic scales given the substrate cutoff is Planck-scale — the leading-order magnitude $Q^{\text{cont}} = Q^{\text{sub}}$ is preserved exactly.

The argument's substantive content is:

1. **Topological character preservation under $\Phi$**: $\Phi$ preserves topological invariants of the discrete substrate by construction (Wilson-Fisher block-spin commutes with discrete symmetry actions; integer-valued representation-theoretic + polytope-topological invariants are unchanged by block-spin coarse-graining).

2. **No-renormalization-at-leading-order**: dynamical RG-flow corrections would require substrate-field-theoretic content that topological substrate quantities by definition do not have (METH-CHIR-CONT-3). Therefore no dynamical correction at any RG-flow scale between $\Lambda_{\text{sub}}$ and $\mu_{\text{obs}}$.

3. **Structural analogy with standard QFT protection**: the argument is structurally analogous to standard QFT protection-of-topological-quantities — Adler-Bardeen anomaly nonrenormalization, Atiyah-Singer index theorem contributions, Chern-Simons level integrality, discrete symmetry parity preservation — all standard machinery establishing that topological invariants are preserved under continuum limits at leading order.

**Scope**: applies to any topological substrate quantity (METH-CHIR-CONT-3) projecting through the continuum-limit map $\Phi$ (METH-CHIR-CONT-2). The leading-order qualifier acknowledges $\mathcal{O}((a/L)^n)$ subleading corrections; in the deep-infrared regime relevant to all current SM-observable scales, these are negligible ($a/L \lesssim 10^{-18}$ at electroweak scale; suppression $a/L \sim 10^{-7}$ even at the leptogenesis era $T \sim 10^{12}$ GeV).

**Dependencies**:
- METH-CHIR-CONT-2 (Continuum-Limit Projection Map $\Phi$): provides the projection map whose preservation properties the argument exploits.
- METH-CHIR-CONT-3 (Topological Substrate Quantity Concept): provides the characterization of quantities to which the argument applies.
- Standard QFT protection-of-topological-quantities principle (Adler-Bardeen \cite{AdlerBardeen}; Atiyah-Singer \cite{AtiyahSinger}; Chern-Simons level integrality \cite{Witten1983CS}; discrete-symmetry-parity preservation): provides the structural analogy that justifies the inference.

**Provenance**: First introduced as Theorem 15.3.1 (Magnitude Inheritance via Topological Projection) + §15.4 connection to standard QFT protection-of-topological-quantities in the joint paper §3 working sketch (Session 137 Patch 0487). Promoted to paper-level Theorem 3.3 of `chirality_continuum.tex` at Patch 0498. Load-bearing argument of Step 4 of the Theorem 3.4 = THEO-CHIR-CONT-1 proof chain. Promoted to **programme-level technique** at Patch 0487 per theorem-registry entry for THEO-CHIR-CONT-1: "Topological-projection argument established as programme-level technique".

**Standard-machinery context**: The argument is structurally equivalent to the standard QFT protection-of-topological-quantities principle. The novel-to-CPP content is the application to substrate-physics quantities under Wilson-Fisher block-spin projection from a discrete polytope-geometric substrate. Once a substrate quantity is identified as topological in the METH-CHIR-CONT-3 sense, the projection-without-renormalization claim follows from standard continuum-QFT machinery — the substantive insight is in the identification step, not in the projection step.

**Cross-paper usage**: Used at chirality continuum joint paper §3.7 (Theorem 3.3 statement + proof), §3.8 (Theorem 3.4 = THEO-CHIR-CONT-1 condition (1) magnitude inheritance). Inherited at §4.1 (Sector A magnitude inheritance via topological-projection), §4.5 (Capotauro Falsifier 6 Threshold (C) bypass-kinematic-intermediaries framing), §4.6 (Theorem 4.4 = THEO-CHIR-CONT-2 magnitude inheritance). Inherited at §5.1 (Sector B magnitude inheritance), §5.3 (substrate-level stabilization energy magnitude inheritance applied to qDP/eDP sector). Synthesis at §6.1 (Layer 4 elevation framework), §6.4 (Table 6.2 four-level identity topological-projection mechanism). Anticipated future use: any CPP Layer 4 closure that needs to argue a substrate-handle magnitude propagates through continuum-limit projection without renormalization (manifestations (iv)+(v) Layer 4 closures + future cross-sector closure work).

---

## Catalogue maintenance protocol

- **Adding entries**: new methods are added in the order they are surfaced in substantive derivation work. Each entry's Provenance field records the patch/session where the method first appeared.
- **Cross-references**: paper-text references to catalogued methods use the `\methref{METH-XXX-N}` LaTeX command (defined in chirality continuum joint paper's `.tex` preamble at Patch 0498; available for future papers via the same convention).
- **Catalogue updates**: when a method is invoked in a new paper / closure, the Cross-paper usage field of the catalogue entry is extended to record the new usage instance. This is post-hoc bookkeeping not blocking the substantive work.
- **Retroactive cataloguing**: methods from earlier CPP work that should be added retrospectively can be folded into the catalogue at any patch; entries are sortable by identifier rather than chronological order of cataloguing.

---

*Catalogue authored by Claude Opus (Anthropic) under Thomas Lee Abshier's direction, 20 May 2026, Session 137 Patch 0498. Initial population from the chirality continuum joint paper §3 bridge work covering four methodological constructs: Sector-Agnostic Substrate Wigner-Eckart Datum (METH-CHIR-CONT-1); Continuum-Limit Projection Map $\Phi$ via Wilson-Fisher Block-Spin Renormalization at Substrate Cutoff (METH-CHIR-CONT-2); Topological Substrate Quantity Concept (METH-CHIR-CONT-3); Topological-Projection Argument (METH-CHIR-CONT-4). Catalogue is available for retroactive expansion as the programme matures and earlier work is surfaced for cataloguing.*
