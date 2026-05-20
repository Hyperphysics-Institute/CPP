# §A Shared Substrate-Handle-to-Effective-Coupling Bridge

**Working sketch — Tier-4 reasoning capture for §A shared bridge step (sub-claim (a) closure for both sector legs of the joint paper).**

This sketch opens substantive Layer 4 derivation work for the joint Layer 4 paper following Patch 0484's v0.1 outline + viability decision gate PROCEED verdict. Session 1 (this patch, Patch 0485) establishes:

1. **Theorem 3.1 statement** (Substrate-Handle-to-Effective-Coupling Bridge; THEO-CHIR-CONT-1 candidate) at theorem-level rigor — the sub-claim (a) closure target articulated as a sector-agnostic claim with magnitude inheritance + chirality content preservation + sector-agnosticism conditions.
2. **Proof architecture** in 4 steps: (i) substrate operator identification + sector-agnostic abstraction; (ii) continuum-limit projection setup; (iii) continuum operator identification; (iv) magnitude inheritance verification (topological argument).
3. **Step 1 substantive closure**: the full sector-agnostic abstraction of the substrate-level Wigner-Eckart structure across the three Capotauro-v2.0 sectors (K3-doublet, W-bracelet, qDP/eDP), verifying that the substrate-level matrix element magnitude $\chi/6$ depends only on universal data $(|\chi| = \phi^{-3}, d_\Gamma = 2, V_{\text{cage}} = 12)$ and not on sector-specific data $(\Gamma, \zeta^{\text{sector}}, \hat{C}^{\text{sector}})$.
4. **Step 2 setup**: the continuum-limit projection architecture for Session 2 (Patch 0486 candidate), with the topological-vs-dynamical distinction identified as the key physical insight underwriting magnitude inheritance without renormalization.
5. **Anti-priorities sustained** at substantive-drafting stage: do not modify Capotauro v2.0 or SF-2 v1.0 or SM-2 v1.0 (all v1.0 SHIPPED with .tex source frozen); do not exceed joint-paper scope; do not commit to specific sector-specific kinematic projection content (deferred to §B/§C work at Patches 0488+/0492+).

Bibliography cross-reference key: `abshier_substrate_to_continuum_bridge_sketch`.

---

## §0 Working-session firewall

Subject to revision. Sub-claim (a) closure for both sectors jointly is a **2--3 session trajectory** per the scoping sketches' estimates (Patch 0482 §3.1; Patch 0483 §3.1). The session decomposition for the bridge step:

- **Session 1 (this patch, Patch 0485)**: Theorem 3.1 statement + Step 1 substrate operator identification + sector-agnostic abstraction + Step 2 setup architecture. The substantive content of Session 1 is the sector-agnostic abstraction of the substrate-level Wigner-Eckart structure.
- **Session 2 (Patch 0486 candidate)**: Step 2 continuum-limit projection closure + Step 3 continuum operator identification at sector-agnostic level. The substantive content is the topological-projection argument for magnitude inheritance.
- **Session 3 (Patch 0487 candidate)**: Step 4 magnitude inheritance verification + sub-claim (a) closure announcement + Theorem 3.1 promoted to full theorem-level rigor at the bridge step. The substantive content closes the bridge via the topological-vs-dynamical distinction.

Upon Session 3 closure, sub-claim (a) is closed and the joint paper's §A shared bridge content is ready for v0.3 §B drafting (Patches 0488+) — opening the SF-2 sector closure under Yang-Mills EFT projection with the bridge result as substrate-physics input.

---

## §1 Theorem 3.1 statement (Substrate-Handle-to-Effective-Coupling Bridge; THEO-CHIR-CONT-1 candidate)

### §1.1 Formal statement (target for Session 3 closure)

**Theorem 3.1** (*Substrate-Handle-to-Effective-Coupling Bridge*). Let $\mathcal{O}^{\text{sub}}$ be a chirality-sensitive substrate operator on a substrate object $\mathcal{S}^{\text{sector}}$ sitting on the first-shell icosahedron at a 600-cell host vertex with substrate residual symmetry $H_3 = I_h$, with:

- **Stabilizer subgroup**: $\Gamma \subset I_h$ (sector-specific; $\Gamma = D_6$ for K3-doublet and W-bracelet, $\Gamma = D_{5d}$ for qDP/eDP);
- **Pairing-convention generator**: $\zeta^{\text{sector}} \in \Gamma$ (sector-specific; the $\mathbb{Z}_2 \subset \Gamma$ generator selecting the parity classification);
- **Matter-doublet basis**: $\{|\Psi^{\text{sub}}_+\rangle, |\Psi^{\text{sub}}_-\rangle\}$ spanning a 2D subspace of $\Gamma$-irreps with $\zeta^{\text{sector}}$-EVEN and $\zeta^{\text{sector}}$-ODD components respectively;
- **Chirality operator**: $\hat{C}^{\text{sector}}$ in a $\zeta^{\text{sector}}$-ODD 1D irrep of $\Gamma$;
- **Substrate-level matrix element**: $\langle \Psi^{\text{sub}}_+ | \hat{C}^{\text{sector}} | \Psi^{\text{sub}}_- \rangle = M^{\text{sector}} = \chi/6$, where $\chi = \pm\phi^{-3}$ via chirality-eigenvalue matching from the substrate primitive 4D direction $\hat{n}$ (FI-C-RC-1 + FI-C-RC-2 from Capotauro v2.0; FI-CHIR-CONT-1/2 in this paper) and $1/6 = d_\Gamma/V_{\text{cage}} = 2/12$ from Schur orthogonality on the shared icosahedral cage (FI-CHIR-CONT-3 substrate-locality inheritance).

Then there exists a continuum-limit effective operator $\mathcal{O}^{\text{eff}}$ (in the continuum EFT appropriate to the sector) with:

1. **Magnitude inheritance (topological)**: $\langle \psi^{\text{eff}}_+ | \mathcal{O}^{\text{eff}} | \psi^{\text{eff}}_- \rangle = M^{\text{eff}} = \chi/6$ at leading order, with no renormalization correction at any RG-flow scale between substrate cutoff $\Lambda_{\text{sub}} \sim \ell_{\text{edge}}^{-1}$ and the sector's observable kinematic scale $\mu_{\text{obs}}^{\text{sector}}$.
2. **Chirality content preservation**: $\mathcal{O}^{\text{eff}}$ is $\zeta^{\text{eff,sector}}$-ODD with respect to the continuum-limit projection of the substrate-level $\zeta^{\text{sector}}$ generator. The continuum chirality eigenvalue $\pm\chi$ is inherited from the substrate-level chirality eigenvalue without sign flip or magnitude renormalization.
3. **Sector-agnosticism**: the projection machinery depends only on the universal substrate-level data $(|\chi|, d_\Gamma/V_{\text{cage}})$ and not on the specific choice of stabilizer subgroup $\Gamma$, $\zeta^{\text{sector}}$ generator, chirality operator irrep, or continuum-EFT framework. The substrate-physics handle $\chi/6$ enters the continuum-limit effective coupling as a single universal scalar magnitude.

The continuum operator $\mathcal{O}^{\text{eff}}$ is identified sector-specifically at §B (SF-2 sector closure; Yang-Mills V--A current operator) and §C (SM-2 sector closure; effective free-energy chirality-asymmetric stabilization-energy operator) in the joint paper's main text; this bridge theorem establishes the existence and substrate-magnitude inheritance independent of the sector-specific identification.

### §1.2 Conditional-closure framing

Theorem 3.1 is a **conditional closure** in the conditional-theorem-closure framework established by SS-9 + SF-4 + SF-2 + Capotauro v2.0 (cite: `abshier_conditional_closure`). The conditions are:

- **FI-CHIR-CONT-1** (substrate primitive 4D direction $\hat{n}$ at vertex-aligned Reading C with $\hat{n} = v_{\text{host}}$);
- **FI-CHIR-CONT-2** (substrate chirality magnitude $|\chi| = \phi^{-3}$ from perturbative-distance-ratio constraint);
- **FI-CHIR-CONT-3** (substrate residual symmetry $H_3 = I_h$ at host vertex);
- **FI-CHIR-CONT-9** (Substrate-Locality Theorem of Capotauro v2.0 §sec:substrate\_locality, inherited at theorem level);
- **AXIM-1, AXIM-3, AXIM-4, AXIM-7** (the four CPP axioms inherited from Capotauro v2.0; AXIM-3 axiom of 600-cell substrate structure is load-bearing; AXIM-7 axiom of substrate primitives is the axiomatic foundation for $\hat{n}$).

The theorem statement is **conditional on these inputs being valid**; first-principles closure of the foundational inputs themselves (in particular, the substrate-physics derivation of $\hat{n}$ from CPP primitive axioms via Q1$'$+Q1$'$.A Layer 3 promotion) is registered as future-window work outside this paper's scope (per joint-paper outline §6 honest-scope summary).

### §1.3 What the theorem does NOT establish

- The theorem does NOT derive the substrate-level matrix element magnitude $\chi/6$ from first principles — this is inherited at theorem-level from THEO-SD-CHIR-1 (W-bracelet sector) and THEO-SD-CHIR-2 (qDP/eDP sector) of Capotauro v2.0.
- The theorem does NOT identify the continuum operator $\mathcal{O}^{\text{eff}}$ sector-specifically — this is deferred to §B and §C of the joint paper.
- The theorem does NOT derive the observable kinematic projection from the continuum operator to specific physical observables (Michel parameter $\rho = 3/4$ for SF-2 sector; Linear-ZBW-on-$-$qCP stabilization energy $\Delta F^{qDP}$ for SM-2 sector) — these are sub-claims (b)+(c) of the respective sector closures, deferred to §B and §C.
- The theorem does NOT close the topological-vs-dynamical distinction at first-principles substrate-dynamics level — the topological argument is conditional on the structural identification of $\hat{n}$ as a substrate primitive feature rather than a dynamical degree of freedom, per the framing-choice discussion at Capotauro v2.0 §sec:order\_parameter.

---

## §2 Proof architecture (4-step structure)

The Theorem 3.1 closure proceeds in four steps:

- **Step 1** (this session, §3 below): **Substrate operator identification + sector-agnostic abstraction**. Establish that the substrate-level Wigner-Eckart structure across all three Capotauro-v2.0 sectors reduces to the same universal data $(|\chi|, d_\Gamma, V_{\text{cage}}, \zeta\text{-parity matching})$, with sector-specific content $(\Gamma, \zeta^{\text{sector}}, \hat{C}^{\text{sector}})$ entering only as labels not as load-bearing parameters.
- **Step 2** (Session 2, Patch 0486 candidate, §4 below sets architecture): **Continuum-limit projection setup**. Define the lattice-to-continuum embedding for the substrate object $\mathcal{S}^{\text{sector}}$, identify the topological-vs-dynamical character of $\hat{n}$, and set up the continuum operator $\mathcal{O}^{\text{eff}}$ projection target.
- **Step 3** (Session 2 closure, Patch 0486 candidate): **Continuum operator identification at sector-agnostic level**. Show that the continuum-limit projection of the substrate-level chirality operator $\hat{C}^{\text{sector}}$ produces a chirality-sensitive continuum operator with the same $\zeta^{\text{cont}}$-parity content as the substrate-level operator.
- **Step 4** (Session 3, Patch 0487 candidate): **Magnitude inheritance verification via topological argument**. Show that the substrate-level magnitude $\chi/6$ projects to the continuum-limit effective coupling at leading order without renormalization, by the topological character of $\hat{n}$ as a substrate primitive feature (not a dynamical degree of freedom subject to RG flow).

Upon completion of Step 4, sub-claim (a) is closed and the bridge theorem stands at full theorem-level rigor.

---

## §3 Step 1 — Substrate operator identification (Session 1 substantive content)

This is the substantive content of Session 1 (this patch).

### §3.1 Substrate-level setup recap

The substrate-level chirality matrix element on a substrate object $\mathcal{S}^{\text{sector}}$ is computed via the Wigner-Eckart theorem on the stabilizer subgroup $\Gamma \subset H_3 = I_h$ of the substrate residual symmetry at the host 600-cell vertex. The matrix element factorizes as:

$$M^{\text{sector}} = \langle \Psi^{\text{sub}}_+ | \hat{C}^{\text{sector}} | \Psi^{\text{sub}}_- \rangle = \underbrace{(\pm\chi)}_{\text{chirality eigenvalue}} \cdot \underbrace{\frac{d_\Gamma}{V_{\text{cage}}}}_{\text{cage-shell factor}} = \pm\frac{\chi}{6}$$

with $|\chi| = \phi^{-3} \approx 0.236$ and $d_\Gamma/V_{\text{cage}} = 2/12 = 1/6$. The factorization is the **four-step proof chain** detailed in Capotauro v2.0 (intro §85--88):

1. **Local-$I_h$-preservation** (Theorem thm:local\_ih\_preservation at v\_host): substrate primitive $\hat{n}$-perturbation preserves $I_h$ symmetry locally to $\mathcal{O}(\epsilon)$ in 4D ambient.
2. **Substrate-Locality Unification** (Corollary cor:substrate\_locality\_unification): substrate objects on the first-shell icosahedron inherit substrate-level chirality magnitude $\chi \equiv \epsilon = \phi^{-3}$ from local-$I_h$-preservation; identification holds for K3-doublet, W-bracelet, qDP/eDP, and any future-window first-shell substrate objects.
3. **Cage-shell factor**: $d_\Gamma/V_{\text{cage}} = 2/12 = 1/6$ on the shared icosahedral cage. Universal across sectors: $d_\Gamma = 2$ is the matter-doublet basis dimension (the 2D subspace of $\Gamma$-irreps in which the substrate states sit) and $V_{\text{cage}} = 12$ is the cardinality of the icosahedral cage.
4. **Sector-specific pairing-convention identification**: the $\zeta^{\text{sector}} \in \Gamma$ generator is identified for each sector (K3: 3D-spatial-inversion $\zeta$; W-bracelet: 4D-icosahedral-center-inversion $\zeta^W$; qDP/eDP: combined-$CP$ $\zeta^{qDP}$). The chirality operator $\hat{C}^{\text{sector}}$ is in a $\zeta^{\text{sector}}$-ODD 1D irrep of $\Gamma$ (K3: $B_2(D_6)$; W-bracelet: identified at Capotauro v2.0 §sec:w\_zeta\_inversion; qDP/eDP: $A_{2u}(D_{5d})$). The matter-doublet basis has opposite $\zeta^{\text{sector}}$-parity: one $\zeta$-EVEN, one $\zeta$-ODD.

The bridge step inherits this factorization at theorem level. **The bridge step's task is to show that this same magnitude $\chi/6$ projects through the continuum limit to an effective coupling without renormalization.**

### §3.2 Sector-agnostic abstraction (the substantive load-bearing content of Step 1)

The factorization $M^{\text{sector}} = \pm \chi/6$ contains sector-specific data $(\Gamma, \zeta^{\text{sector}}, \hat{C}^{\text{sector}})$ but the **magnitude** is sector-agnostic. This is the structural identity claim of the joint paper: one substrate handle, three observable manifestations, identical numerical magnitude.

**Definition 3.2.1 (Sector-Agnostic Substrate Wigner-Eckart Datum).** A **sector-agnostic substrate Wigner-Eckart datum** is a tuple
$$\mathcal{D}^{\text{sub}} = (\mathcal{S}, \Gamma, \zeta, \hat{C}, \{|\Psi_+\rangle, |\Psi_-\rangle\}, M)$$
where:

- $\mathcal{S}$ is a substrate object on the first-shell icosahedron at the host 600-cell vertex;
- $\Gamma \subset H_3 = I_h$ is the stabilizer subgroup of $\mathcal{S}$ in the substrate residual symmetry;
- $\zeta \in \Gamma$ is the $\mathbb{Z}_2$ pairing-convention generator;
- $\hat{C}$ is the chirality operator in a $\zeta$-ODD 1D irrep of $\Gamma$;
- $\{|\Psi_+\rangle, |\Psi_-\rangle\}$ is the matter-doublet basis in a 2D subspace of $\Gamma$-irreps with $\zeta$-EVEN and $\zeta$-ODD components respectively;
- $M = \langle \Psi_+ | \hat{C} | \Psi_- \rangle$ is the substrate-level matrix element.

A sector-agnostic substrate Wigner-Eckart datum is **valid** if the matrix element $M$ admits the factorization
$$M = \pm \chi \cdot \frac{d_\Gamma}{V_{\text{cage}}}$$
with universal data $|\chi| = \phi^{-3}$, $d_\Gamma = 2$, $V_{\text{cage}} = 12$, yielding $|M| = \chi/6 \approx 0.0394$.

### §3.3 Validity verification across the three Capotauro-v2.0 sectors

Three sector instantiations of the sector-agnostic substrate Wigner-Eckart datum from Capotauro v2.0:

**Sector K3 (K3-doublet; THEO-CAP-1 at Capotauro v2.0 §sec:composite\_we):**

- $\mathcal{S}^{K3}$ = 3-vertex equilateral triangle on a 600-cell face within the first-shell icosahedron (K3-base).
- $\Gamma^{K3} = D_{3d} \cong S_3 \times \mathbb{Z}_2 \cong D_6$ of order 12.
- $\zeta^{K3} \in \Gamma^{K3}$ = the $\mathbb{Z}_2$ generator (host-CP-related inversion specific to K3-doublet stabilizer).
- $\hat{C}_\chi \in B_2(D_6)$ — $\zeta^{K3}$-ODD 1D irrep (Capotauro v2.0 §691 + Finding C-W11).
- Matter-doublet $\{\Phi_-^{(1)}, \Phi_-^{(2)}\}$ in 2D $E$-irrep subspace of $D_{3d}$ with opposite $\zeta^{K3}$-parity via $\sigma_1\zeta$-EVEN pairing convention (Finding C-W12).
- $M^{K3} = \chi/6$ at machine-precision verification (Capotauro v2.0 Theorem thm:composite\_cap\_we).
- **Validity: ✓ PASS.**

**Sector W (W-bracelet; THEO-SD-CHIR-1 at Capotauro v2.0 §sec:w\_bracelet\_sector):**

- $\mathcal{S}^W$ = 6-vertex Petrie hexagon on the first-shell icosahedron (Finding C-W36).
- $\Gamma^W = D_6$ of order 12 — sub-stabilizer of $H_3 = I_h$ at the Petrie-hexagon symmetry; isomorphic to $\Gamma^{K3}$ but realized differently on the first-shell cage.
- $\zeta^W \in \Gamma^W$ = icosahedral-center inversion in 4D (Definition def:zeta\_w; Capotauro v2.0 §sec:w\_zeta\_inversion).
- $\hat{C}^W$ in the $\zeta^W$-ODD 1D irrep of $D_6$ matching the V--A current's $120°/240°$ phase bias (Capotauro v2.0 §1038 V--A current irrep identification; matter-doublet carrier is $E_2$).
- Matter-doublet $\{|\Psi^W_+\rangle, |\Psi^W_-\rangle\}$ in 2D $E_2$-irrep subspace of $D_6$ with opposite $\zeta^W$-parity.
- $M^W = \chi/6$ via THEO-SD-CHIR-1 cross-sector unification (Capotauro v2.0 Theorem thm:theo\_sd\_chir\_1).
- **Validity: ✓ PASS.**

**Sector qDP (qDP/eDP; THEO-SD-CHIR-2 at Capotauro v2.0 §sec:qdp\_edp\_sector):**

- $\mathcal{S}^{qDP}$ = antipodal-pair $\{v_i, -v_i\}$ on the first-shell icosahedron (Linear-ZBW refined per Q6-PAIRING resolution at Patch 0439).
- $\Gamma^{qDP} = D_{5d}$ of order 20 — sub-stabilizer of $H_3 = I_h$ at the antipodal-pair refinement of single-vertex $C_{5v}$.
- $\zeta^{qDP} \in \Gamma^{qDP}$ = combined $CP$ operation (host-CP-centered spatial inversion + $\hat{n}$-flip + qCP-sign flip; Definition def:zeta\_qdp; Finding C-W46).
- $\hat{C}^{qDP} \in A_{2u}(D_{5d})$ — $\zeta^{qDP}$-ODD 1D irrep.
- Matter-doublet $\{|\Psi^{qDP,(1)}_-\rangle, |\Psi^{qDP,(2)}_-\rangle\}$ in 2D subspace of $A_{1g} \oplus A_{2u}$ in $D_{5d}$ with opposite $\zeta^{qDP}$-parity.
- $M^{qDP} = \chi/6$ via THEO-SD-CHIR-2 closure (Capotauro v2.0 Theorem thm:theo\_sd\_chir\_2).
- **Validity: ✓ PASS.**

### §3.4 Result of Step 1 — sector-agnostic abstraction holds

The three sector instantiations all satisfy the sector-agnostic substrate Wigner-Eckart datum definition (§3.2.1) and produce the same magnitude $|M| = \chi/6$. The stabilizer subgroup differs ($D_6$ vs $D_{5d}$), the $\zeta$ generator differs (3D-spatial-inversion vs 4D-icosahedral-center-inversion vs combined-$CP$), the chirality operator's specific 1D irrep differs ($B_2(D_6)$ vs the V--A-current-carrying $\zeta^W$-ODD 1D irrep of $D_6$ vs $A_{2u}(D_{5d})$), and the matter-doublet's specific 2D-irrep embedding differs ($E$-irrep of $D_{3d}$ vs $E_2$-irrep of $D_6$ vs $A_{1g} \oplus A_{2u}$ subspace of $D_{5d}$). But **all three produce the same magnitude $\chi/6$** because the magnitude depends only on universal data $(|\chi|, d_\Gamma, V_{\text{cage}}) = (\phi^{-3}, 2, 12)$.

**This is the load-bearing content of Step 1**: the substrate-level matrix element magnitude is sector-agnostic. The bridge step (Steps 2--4) operates on the sector-agnostic abstraction, not on the sector-specific instantiations. The continuum-limit projection acts on the universal scalar magnitude $\chi/6$ and produces a continuum-limit effective coupling that inherits this magnitude.

**Step 1 result (Session 1 closure)**: The sector-agnostic substrate Wigner-Eckart datum $\mathcal{D}^{\text{sub}}$ is a valid abstraction across all three Capotauro-v2.0 sectors; the substrate-level magnitude $|M| = \chi/6$ depends only on universal data, with sector-specific data entering only as labels for the operator + irrep + basis identification.

### §3.5 The $\zeta$-parity matching as the load-bearing structural condition

A subtle but load-bearing observation: the non-vanishing of the substrate matrix element requires $\zeta$-parity matching between the operator and the matter-doublet basis. Specifically, with $\hat{C}^{\text{sector}}$ in a $\zeta$-ODD 1D irrep and matter-doublet $\{|\Psi_+\rangle, |\Psi_-\rangle\}$ with $|\Psi_+\rangle$ $\zeta$-EVEN and $|\Psi_-\rangle$ $\zeta$-ODD, the matrix element

$$\langle \Psi_+ | \hat{C} | \Psi_- \rangle$$

is non-vanishing because the integrand under the $\zeta$-action carries $\zeta$-parity $(\text{EVEN}) \otimes (\text{ODD}) \otimes (\text{ODD}) = \text{EVEN}$, which contains the trivial irrep and thus has non-vanishing $\zeta$-invariant component.

If both matter-doublet states were $\zeta$-EVEN or both were $\zeta$-ODD, the matrix element would vanish identically (Schur-orthogonality on $\zeta$ alone). The pairing-convention identification at each sector (sector-specific $\zeta^{\text{sector}}$ generator + matter-doublet basis with opposite $\zeta^{\text{sector}}$-parity) is what makes the matrix element non-vanishing. This is the **register-then-resolve** pattern from Capotauro v2.0 v2.0 cross-sector closure trajectory (Q5-PAIRING for W-bracelet; Q6-PAIRING for qDP/eDP; see Capotauro v2.0 §387).

The bridge step inherits the $\zeta$-parity matching condition as a structural inheritance from the substrate-level closure: the continuum-limit operator $\mathcal{O}^{\text{eff}}$ must also be $\zeta^{\text{eff}}$-ODD with respect to the continuum-limit projection of $\zeta^{\text{sector}}$, and the continuum-limit states $\{|\psi^{\text{eff}}_+\rangle, |\psi^{\text{eff}}_-\rangle\}$ must have opposite $\zeta^{\text{eff}}$-parity. This is the chirality-content-preservation condition of Theorem 3.1.

---

## §4 Step 2 architecture — continuum-limit projection setup (Session 2 target)

This section sets architecture for Session 2 (Patch 0486 candidate). Step 2 substantive closure is deferred to Session 2.

### §4.1 Lattice-to-continuum projection framework

The substrate is a discrete lattice (the 600-cell at the appropriate scale; the host vertex and its first-shell icosahedron live on this lattice). The continuum-limit projection is the standard lattice-to-continuum embedding via:

1. **Continuum embedding of the substrate object**: $\mathcal{S}^{\text{sector}}$ as a discrete subset of the lattice → smooth submanifold of the continuum embedding via lattice-spacing $a \to 0$ limit.
2. **Continuum embedding of the matter-doublet states**: $\{|\Psi^{\text{sub}}_+\rangle, |\Psi^{\text{sub}}_-\rangle\}$ as discrete lattice eigenstates → continuum field excitations via standard Wilson-Fisher-style block-spin renormalization.
3. **Continuum embedding of the stabilizer group**: $\Gamma$ as discrete subgroup of $I_h$ → continuum-limit projection acts via projection of the discrete group action to the continuum field operators.
4. **Continuum embedding of the pairing-convention generator**: $\zeta^{\text{sector}}$ as $\mathbb{Z}_2$ generator → continuum $\zeta^{\text{cont}}$ acts on continuum operators with the same $\mathbb{Z}_2$-content.
5. **Continuum embedding of the chirality operator**: $\hat{C}^{\text{sector}}$ as substrate-lattice operator → continuum $\mathcal{O}^{\text{eff}}$ as continuum-EFT operator (sector-specific identification at §B/§C).

The Session 2 target is to verify that this continuum-limit projection preserves the $\zeta$-parity matching (chirality content preservation of Theorem 3.1) and produces a continuum operator $\mathcal{O}^{\text{eff}}$ that is $\zeta^{\text{cont}}$-ODD with respect to the continuum-limit pairing-convention generator.

### §4.2 The topological-vs-dynamical distinction (the key physical insight)

The load-bearing physical insight for the bridge step's magnitude-inheritance claim is the **topological character of $\chi$**.

The substrate magnitude $|\chi| = \phi^{-3}$ is derived from the perturbative-distance-ratio constraint on $\hat{n}$-induced edge perturbations (Capotauro v2.0 §sec:chi\_resolution + Finding C-W39). Crucially, $\hat{n}$ is a **substrate primitive feature**, not a dynamical degree of freedom: per the framing-choice discussion at Capotauro v2.0 §sec:order\_parameter, $\hat{n}$ is the substrate's chirality-breaking primitive (FI-C-RC-1), and the chirality magnitude $|\chi| = \phi^{-3}$ is its perturbation amplitude — a **structural** quantity derived from substrate geometry, not a **dynamical** quantity derived from substrate field-theoretic action.

This has a critical consequence for the bridge step: **topological / structural quantities of the substrate are preserved across continuum limits without renormalization**, by the same principle that protects:

- Anomaly coefficients in continuum QFT (the chiral anomaly's $1/(16\pi^2)$ is topological and exact at all loop orders);
- Topological charges (winding numbers, Chern-Simons levels) in continuum gauge theory;
- Atiyah-Singer index theorem contributions to physical observables;
- Discrete symmetry generators' parity content (e.g., $CP$, $P$, $T$ parities of operators).

By contrast, **dynamical quantities** (couplings, masses, field amplitudes) are subject to RG flow and require renormalization. The bridge step's claim is that $\chi/6$ is a topological quantity in this sense and projects to the continuum without renormalization corrections at leading order.

### §4.3 Magnitude inheritance argument outline (Session 2 closure target)

The Session 2 substantive content (Step 2 closure + Step 3 setup) will close the magnitude-inheritance argument via:

1. **Identification of $\chi$ as topological in the precise sense above** (i.e., $\chi$ is a structural primitive parameter of the substrate, not a dynamical RG-flow-dependent coupling). This follows from FI-C-RC-1 (substrate primitive 4D direction $\hat{n}$ as a primitive substrate feature) and the perturbative-distance-ratio constraint at Capotauro v2.0 §sec:chi\_resolution (deriving $|\chi| = \phi^{-3}$ from the geometric constraint on $\hat{n}$-induced edge perturbations, not from any substrate-field-theoretic dynamics).
2. **Verification that the continuum-limit projection of a topological substrate primitive preserves its magnitude exactly at leading order** (no anomaly-coefficient-style "one-loop correction"; no RG-flow renormalization between substrate cutoff $\Lambda_{\text{sub}}$ and observable kinematic scale $\mu_{\text{obs}}$). This is the topological-projection argument that closes the bridge step at full theorem-level rigor.
3. **Verification that the cage-shell factor $1/6 = d_\Gamma/V_{\text{cage}} = 2/12$ also projects without renormalization** (the factor depends on the topology of the icosahedral cage, which is preserved under continuum-limit projection at leading order). This factor's topological character is inherited from the Schur-orthogonality structure of the discrete stabilizer-subgroup representation theory, which projects to continuum representation theory of the corresponding Lie group (Lie-group analog of $\Gamma \subset I_h$ at continuum limit) preserving the Schur-orthogonality structure.
4. **Verification that the sector-specific data $(\Gamma, \zeta^{\text{sector}}, \hat{C}^{\text{sector}})$ do not introduce sector-specific renormalization corrections** at the bridge-step level (sector-specific kinematic corrections enter at §B and §C of the joint paper, downstream of the bridge step). This is the sector-agnosticism condition.

The Session 2 closure is technically demanding but conceptually straightforward — the topological argument is the standard one for protected quantities in continuum QFT. The bridge step's substantive content is the **identification** of $\chi/6$ as topological in this sense; once the identification is made, the projection-without-renormalization claim follows from standard continuum-QFT machinery.

---

## §5 Steps 3 + 4 architecture (Sessions 2-3)

**Step 3** (Session 2 closure, Patch 0486 candidate): **Continuum operator identification at sector-agnostic level**. Show that the continuum-limit projection of the substrate-level chirality operator $\hat{C}^{\text{sector}}$ produces a continuum operator $\mathcal{O}^{\text{eff}}$ that is:

- $\zeta^{\text{cont}}$-ODD with respect to the continuum-limit projection of the substrate-level $\zeta^{\text{sector}}$ generator;
- Chirality-sensitive in the sector-appropriate continuum-EFT sense (i.e., acts on continuum chirality-eigenstates of the appropriate continuum-EFT fields);
- Identified specifically at §B (Yang-Mills V--A current operator for the SF-2 sector) and §C (effective free-energy chirality-asymmetric stabilization-energy operator for the SM-2 sector); the sector-specific identification is the natural transition point from the joint paper's §A bridge content to §B + §C sector-specific content.

**Step 4** (Session 3, Patch 0487 candidate): **Magnitude inheritance verification via topological argument**. Complete the topological-projection argument from §4.2 + §4.3 above, verifying that the continuum-limit effective coupling magnitude is exactly $|M^{\text{eff}}| = \chi/6$ at leading order without renormalization correction.

Upon completion of Step 4, **sub-claim (a) is closed**. The bridge theorem Theorem 3.1 stands at full theorem-level rigor with conditional inheritance from the FI-CHIR-CONT-N foundational input stack.

---

## §6 Sector-agnostic vs sector-specific content map

The bridge step content split between sector-agnostic and sector-specific:

| Content | Sector-Agnostic | Sector-Specific (where it enters) |
|---|---|---|
| Substrate magnitude $|\chi| = \phi^{-3}$ | ✓ | — |
| Cage-shell factor $1/6 = d_\Gamma/V_{\text{cage}}$ | ✓ | — |
| Substrate matrix element magnitude $\chi/6$ | ✓ | — |
| Continuum-limit projection of magnitude | ✓ (Step 4) | — |
| Topological-vs-dynamical distinction | ✓ (Step 4 argument) | — |
| Stabilizer subgroup $\Gamma$ | — | §3.3 sector instantiations |
| Pairing-convention generator $\zeta^{\text{sector}}$ | — | §3.3 sector instantiations |
| Chirality operator irrep | — | §3.3 sector instantiations |
| Matter-doublet basis embedding | — | §3.3 sector instantiations |
| Continuum operator identification | — | §B (SF-2 sector); §C (SM-2 sector) of joint paper main text |
| Continuum chirality-eigenstate identification | — | §B (left/right-handed fermion fields); §C (Linear-ZBW-on-$\pm$qCP) |
| Kinematic projection to observable | — | §B sub-claims (b)+(c)+(d); §C sub-claims (b)+(c)+(d) |

**The bridge step's content is sector-agnostic by construction** — it operates on the universal substrate Wigner-Eckart datum and produces a universal continuum-limit magnitude inheritance result. Sector-specific data enters only after the bridge step, in §B and §C of the joint paper, where the universal continuum coupling $\chi/6$ is identified as the V--A coupling strength factor (Sector A) and the chirality-asymmetric stabilization-energy split (Sector B).

This is the **structural efficiency** of the joint paper format that motivated Venue (c) over Venue (b): the load-bearing bridge work is done once at sector-agnostic level, and the sector-specific kinematic projection work proceeds independently in §B and §C using the universal bridge result as a single shared input.

---

## §7 FI dependency mapping

The bridge step inherits the following FI-CHIR-CONT-N foundational inputs (from joint paper outline §3):

**Substrate-level inheritance (shared FI-CHIR-CONT-1/2/3 from FI-CHIR-1/2/3 = FI-CPB-1/2/3)**:

- **FI-CHIR-CONT-1**: substrate primitive 4D direction $\hat{n}$ in ambient $\mathbb{R}^4$ at vertex-aligned Reading C with $\hat{n} = v_{\text{host}}$ (inherited from Capotauro v2.0 FI-C-RC-1 + FI-C-RC-2). Load-bearing for Step 4 topological-projection argument.
- **FI-CHIR-CONT-2**: substrate chirality magnitude $|\chi| = \phi^{-3}$ derived from perturbative-distance-ratio constraint on $\hat{n}$-induced edge perturbations (inherited from Capotauro v2.0 §sec:chi\_resolution + Finding C-W39). Load-bearing for Step 4 magnitude-inheritance claim.
- **FI-CHIR-CONT-3**: substrate residual symmetry $H_3 = I_h$ at host vertex (inherited from Capotauro v2.0 Theorem stab\_Hfour). Load-bearing for Step 1 sector-agnostic abstraction (substrate objects on first-shell icosahedron at $H_3$-symmetric host vertex).

**Cross-sector unification inheritance (FI-CHIR-CONT-9)**:

- **FI-CHIR-CONT-9**: Substrate-Locality Theorem of Capotauro v2.0 §sec:substrate\_locality (Theorem thm:local\_ih\_preservation + Corollary cor:substrate\_locality\_unification). Load-bearing for Step 1 (sector-agnostic abstraction inherits substrate-locality across the three sectors) and Step 4 (substrate-locality preservation under continuum-limit projection at leading order).

**Joint-paper-specific inheritances (FI-CHIR-CONT-10/11/12)**:

- **FI-CHIR-CONT-10**: OPEN-SD-CHIR-PRIMITIVE umbrella context (registered Capotauro v2.0 Patch 0422 Session 130). Frames the bridge step as closing umbrella manifestations (ii) electroweak V--A and (iii) electromagnetic handedness at Layer 4.
- **FI-CHIR-CONT-11**: PD-004 layer architecture mapping (Layer 4 continuum-EFT projection work requires dedicated venue). Frames the bridge step's venue placement under joint Layer 4 paper.
- **FI-CHIR-CONT-12**: SF-4 v4.0 cross-sector-closure-pattern precedent (Session 72 Patch 0333; OPEN-FP-SF-4-2 + SM-5 op:nu\_id joint closure). Methodological precedent for cross-sector closure pattern; templates the bridge step's joint-paper format.

**Axiom inheritances (from Capotauro v2.0 axiom stack)**:

- **AXIM-1, AXIM-3, AXIM-4, AXIM-7** inherited at axiom level. Most load-bearing: AXIM-3 (axiom of 600-cell substrate structure) and AXIM-7 (axiom of substrate primitives).

The bridge step is **inheritance-heavy** by design — it operates on the substrate-physics handle established by Capotauro v2.0 and projects to continuum-EFT level. The bridge step's substantive content is the topological-projection argument (Step 4), which uses the inheritance stack as conditional inputs.

---

## §8 Anti-priorities sustained at Session 1

**Do NOT modify Capotauro v2.0 or SF-2 v1.0 or SM-2 v1.0 .tex source** during this bridge work. All three are at v1.0 SHIPPED with .tex source frozen per the SS-9 v1.0 SHIP precedent.

**Do NOT commit to sector-specific kinematic projection content** during the bridge step. The bridge step operates at sector-agnostic level; sector-specific work (Yang-Mills V--A for SF-2; effective stat-mech for SM-2) enters at §B and §C of the joint paper, at Patches 0488+ and 0492+ respectively. Conflating sector-agnostic bridge content with sector-specific kinematic content is a category error that this anti-priority guards against.

**Do NOT exceed joint-paper scope** during the bridge step. Other OPEN-FP-SF-2-* entries (η, EWSB, loopfactor, shelldens, chaincomp) are NOT in scope; other SM-series open problems are NOT in scope; OPEN-SD-CHIR-PRIMITIVE umbrella manifestations (iv) thermodynamic causal arrow and (v) cosmological-vacuum asymmetry are NOT in scope (future-window).

**Do NOT trigger Venue (b) fallback** during the bridge step. The bridge step is the test of joint-paper viability — if sector-agnostic abstraction surfaces structural obstructions during Steps 1--4, Venue (b) fallback becomes relevant. Otherwise (the expected case), the bridge step closes at Session 3 and §B + §C proceed under joint paper Venue (c).

**Do NOT promote sub-claim (a) closure to theorem-level rigor at Session 1**. The promotion is at Session 3 (Step 4 closure). Sessions 1--2 work at outline + setup level with theorem-statement-as-target framing.

**Do NOT mix Tier-4 reasoning capture with paper main-text drafting**. This sketch is Tier-4 reasoning capture per CPP four-tier documentation discipline. The joint paper main-text drafting opens at v0.3 (Patches 0488+) after the bridge sketch's Sessions 1--3 close sub-claim (a).

---

## §9 Status update at Session 1 end

**Patch**: 0485 (this patch; §A shared bridge work Session 1 — Theorem 3.1 statement + Step 1 substrate operator identification + sector-agnostic abstraction + Step 2 setup architecture).

**Date**: 20 May 2026 (Session 137 continuation, post-Patch 0484 viability decision gate PROCEED verdict).

**Programme state changes**:

1. **§A shared bridge work OPENED at substantive Layer 4 derivation level**: joint paper v0.2 substantive drafting begins. The bridge step's Session 1 deliverable is in hand.
2. **Theorem 3.1 statement ESTABLISHED at theorem-statement level** (THEO-CHIR-CONT-1 candidate registration): Substrate-Handle-to-Effective-Coupling Bridge with three conditions (magnitude inheritance topological; chirality content preservation; sector-agnosticism). Promotion to full theorem-level rigor at Session 3 (Patch 0487 candidate) upon Step 4 closure.
3. **Step 1 substrate operator identification CLOSED at sector-agnostic abstraction level**: the sector-agnostic substrate Wigner-Eckart datum (Definition 3.2.1) is a valid abstraction across the three Capotauro-v2.0 sectors (K3-doublet, W-bracelet, qDP/eDP), with substrate-level magnitude $|M| = \chi/6$ depending only on universal data $(|\chi| = \phi^{-3}, d_\Gamma = 2, V_{\text{cage}} = 12)$.
4. **$\zeta$-parity matching identified as load-bearing structural condition** at Step 1: the non-vanishing of the substrate matrix element requires opposite $\zeta$-parity in the matter-doublet basis + $\zeta$-ODD chirality operator. This structural condition is inherited at the bridge step as the chirality-content-preservation condition of Theorem 3.1.
5. **Step 2 continuum-limit projection architecture ESTABLISHED**: the lattice-to-continuum embedding framework + topological-vs-dynamical distinction (key physical insight) + magnitude-inheritance argument outline. Session 2 closure target: Step 2 substantive closure + Step 3 continuum operator identification at sector-agnostic level.
6. **FI dependency mapping COMPLETE** for the bridge step: FI-CHIR-CONT-1/2/3 (substrate-level inheritance) + FI-CHIR-CONT-9 (Substrate-Locality Theorem inheritance) + FI-CHIR-CONT-10/11/12 (joint-paper-specific inheritances) + AXIM-1/3/4/7 (Capotauro v2.0 axiom stack inheritance). Bridge step is inheritance-heavy by design; substantive content concentrated in Step 4 topological-projection argument.
7. **No theorems registered new** (Theorem 3.1 at theorem-statement level pending Step 4 closure; THEO-CHIR-CONT-1 candidate not yet at registered-theorem status).
8. **No predictions registered new** (substrate-level $|M| = \chi/6$ inherited from THEO-SD-CHIR-1 + THEO-SD-CHIR-2; continuum-limit effective coupling $|M^{\text{eff}}| = \chi/6$ at theorem-statement-level pending Step 4).
9. **No falsifiers registered new** (Capotauro Falsifier 6 + positive-down-type-quark-observation analog registered at v0.1 outline §10 as anticipated-activation-at-v1.0-SHIP for the two sector legs).

**Forward queue post-Patch 0485**:

- **Priority 1 (Patch 0486 candidate)**: §A bridge work Session 2 — Step 2 continuum-limit projection closure + Step 3 continuum operator identification at sector-agnostic level. 1 session estimated.
- **Priority 2 (Patch 0487 candidate)**: §A bridge work Session 3 — Step 4 magnitude inheritance verification + sub-claim (a) closure announcement + Theorem 3.1 promoted to theorem-level rigor. 1 session estimated. **THIS IS THE SUB-CLAIM (a) CLOSURE PATCH** — completes the load-bearing technical step.
- **Priority 3 (Patches 0488+)**: §B Sector A V--A coupling derivation (Yang-Mills EFT projection + Michel parameter $\rho = 3/4$ + massless-helicity-limit 100\% LH preference). v0.3 substantive drafting. 3--5 sessions.

**Anti-priorities preserved**: as enumerated in §8 above. Most critical: do NOT mix sector-agnostic bridge content with sector-specific kinematic content; do NOT promote sub-claim (a) to theorem-level rigor at Session 1; do NOT modify Capotauro v2.0 / SF-2 v1.0 / SM-2 v1.0 .tex source during this bridge work.

**Methodological observation — the bridge step's structural efficiency**: at the end of Session 1, the bridge step is on track to close sub-claim (a) for both sector legs jointly in 3 sessions total (Sessions 1--3 = Patches 0485--0487). Compare to two separate single-sector bridge closures under Venue (b) fallback: each would require its own bridge derivation (~2--3 sessions per sector); total ~4--6 sessions for two separate bridges. The joint paper format saves an estimated ~1--3 sessions on the bridge step alone, with the savings concentrated in the sector-agnostic abstraction (Step 1; done once instead of twice) and the topological-projection argument (Step 4; the universal argument applies to both sectors).

This validates the v0.1 outline §10 viability decision gate's recommendation (PROCEED TO v0.2 SUBSTANTIVE DRAFTING under Venue (c) joint Layer 4 paper) at the first session of substantive derivation work. The bridge step's sector-agnostic structure is intact; the joint paper format is delivering the expected structural efficiency.

---

*Sketch authored by Claude Opus (Anthropic) under Thomas Lee Abshier's direction, 20 May 2026, Session 137 continuation, Patch 0485. Opens substantive §A shared substrate-handle-to-effective-coupling bridge work at the joint Layer 4 paper. Session 1 deliverable: Theorem 3.1 statement + Step 1 substrate operator identification + sector-agnostic abstraction across the three Capotauro-v2.0 sectors + Step 2 setup architecture for Session 2. Sub-claim (a) closure target at Session 3 (Patch 0487 candidate) upon Step 4 topological-projection argument closure. Joint paper v0.2 substantive drafting OPENED.*
