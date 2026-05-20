# §C Sector B SM-2 Chiral-Polarity-Bias Derivation — Working Sketch

**Joint Layer 4 paper §C (Sector B = SM-2 chiral-polarity-bias / electromagnetic-handedness)**
**Opened**: 20 May 2026 (Session 137 continuation, Patch 0492 — §C Session 1)
**Status at open**: §A bridge work CLOSED at theorem-level rigor via THEO-CHIR-CONT-1 (Patch 0487); §B Sector A V–A coupling derivation CLOSED at theorem-level rigor via THEO-CHIR-CONT-2 (Patch 0491); §C substantive drafting opens with this patch under inheritance from §A bridge theorem
**Sketch home**: `flagship_papers/chirality_continuum/sketches/sector_b_chiral_polarity_bias.md`

This sketch opens substantive Tier-4 reasoning work for the joint paper's §C Sector B (SM-2 chiral-polarity-bias derivation). §C inherits THEO-CHIR-CONT-1's sector-agnostic continuum operator structure and applies sector-specific effective-free-energy / partition-function framework identification appropriate to the SM-2 sector to derive the chirality-asymmetric stabilization-energy operator $\Delta F^{qDP}$ + downstream observable predictions (Linear-ZBW-on-$\pm$qCP stabilization-energy asymmetry; thermodynamic-scale exclusion bound; SM cross-validation).

---

## §0 Session 1 working-session firewall and scope

This section opens Session 1 of §C Sector B work (Patch 0492). §A bridge step is CLOSED at theorem-level rigor (THEO-CHIR-CONT-1 + sub-statements registered at theorems #65 + sub-#65.1/.2/.3); §B Sector A is CLOSED at theorem-level rigor (THEO-CHIR-CONT-2 + sub-statements registered at theorem #66). §C substantive drafting opens with this patch under inheritance from §A.

**Session 1 substantive scope** (Patch 0492):

1. **Theorem C.1 statement** (§1 below): articulate sector-specific theorem for §C closure — Sector B Effective Free-Energy Framework Chiral-Polarity-Bias Derivation. Four sub-claims targeted across Sessions 1–4 of §C (Patches 0492–0495+ candidates analog of §B closure trajectory).

2. **Proof architecture** (§2 below): 4-step proof structure for Theorem C.1 — (i) sector-specific continuum operator identification; (ii) substrate-level stabilization energy calculation; (iii) exclusion bound at observable thermodynamic scales; (iv) SM cross-validation framing.

3. **Step 1 closure** (§3 below): sector-specific continuum operator identification — show that the bridge theorem's sector-agnostic continuum operator $\mathcal{O}^{\text{eff,qDP}} = \Phi_*\hat{C}^{qDP}$ identifies as the chirality-asymmetric stabilization-energy operator $\Delta F^{qDP}$ in the effective free-energy / partition-function framework appropriate to the SM-2 sector.

4. **Steps 2–4 setup architecture** (§4 + §5 + §6 below): articulate what Sessions 2 + 3 + 4 of §C will close.

**Anti-priorities at Session 1 of §C** (in addition to programme-level + §A + §B anti-priorities):

- Do NOT close Steps 2–4 of §C at Session 1 (substrate-level stabilization energy + exclusion bound + SM cross-validation — all deferred to Sessions 2–4).
- Do NOT modify SM-2 v1.0 .tex source during §C drafting — SM-2 v1.0 SHIPPED with .tex source frozen; §C content lives at `flagship_papers/chirality_continuum/` not at SM-2 paper home.
- Do NOT modify Patch 0483 SM-2 scoping sketch at `flagship_papers/electroweak/sketches/SM-2_chiral_polarity_bias_layer4_closure.md` — preserved at historical location; §C working sketch is THIS file.
- Do NOT modify §A bridge work (`substrate_to_continuum_bridge.md`) or §B Sector A work (`sector_a_va_coupling.md`) during §C drafting. §A and §B are CLOSED.
- Do NOT mix §C sector-specific content with §B sector-specific content. §B is CLOSED; §C is a parallel derivation at the SM-2 sector inheriting §A.
- Do NOT introduce new FI-CHIR-CONT-N entries at §C Session 1 beyond sector-specific to §C (FI-CHIR-CONT-13/14/15 expected at §C analog of FI-CHIR-CONT-10/11/12 at §B; FI inventory finalized at v0.1 outline + 3 sector-specific each for §B and §C for maximum 6 sector-specific FIs).
- Do NOT promote Theorem C.1 to programme-level registered-theorem status at Session 1 (registration at end of §C Session 4 when sub-claims (f)+(g)+(h)+(i) all close; expected THEO-CHIR-CONT-3 candidate).

---

## §1 Theorem C.1 statement — Sector B Effective Free-Energy Chiral-Polarity-Bias Derivation

**Theorem C.1** (*Sector B Effective Free-Energy Framework Chiral-Polarity-Bias Derivation*; THEO-CHIR-CONT-3 candidate). Under THEO-CHIR-CONT-1 + sub-statements THEO-CHIR-CONT-1.1/-1.2/-1.3 (joint Layer 4 paper §A bridge theorem with sector-agnostic continuum operator at magnitude $\chi/6$ at leading order) + qDP/eDP sector specialization (substrate object as Linear-ZBW configuration on host vertex's first-shell icosahedron with stabilizer $D_{5d}$, $\zeta^{qDP} = \text{combined } CP$ (host-CP-centered spatial inversion + $\hat{n}$-flip + qCP-sign flip), chirality operator $\hat{C}^{qDP} \in A_{2u}(D_{5d})$ per THEO-SD-CHIR-2 finding C-W46) + SM-2 v1.0 §10 chiral-polarity-bias framework (effective free-energy / partition-function continuum framework for thermodynamic-scale Linear-ZBW vs Orbital-ZBW selection on $\pm$qCP centers), the bridge theorem's sector-agnostic continuum operator $\mathcal{O}^{\text{eff,qDP}} = \Phi_*\hat{C}^{qDP}$ has four sector-specific consequences:

1. **(f) Sector-specific operator identification**: $\mathcal{O}^{\text{eff,qDP}}$ identifies as the **chirality-asymmetric stabilization-energy operator** $\Delta F^{qDP}$ in the continuum effective free-energy / partition-function framework — the energy difference between Linear-ZBW configurations on $+$qCP vs $-$qCP centers. The continuum-limit projection of the substrate-level matter-doublet $\{|\Psi_-^{qDP,(1)}\rangle, |\Psi_-^{qDP,(2)}\rangle\}$ identifies as the continuum Linear-ZBW chirality-eigenstate pair $\{|\text{LZBW},+\rangle, |\text{LZBW},-\rangle\}$ via:
   - $|\Psi_-^{qDP,(1)}\rangle$ ($\zeta^{qDP}$-EVEN) $\to$ $|\text{LZBW},+\rangle$ (combined-$CP$-EVEN; chirality-positive Linear-ZBW configuration on $+$qCP center)
   - $|\Psi_-^{qDP,(2)}\rangle$ ($\zeta^{qDP}$-ODD) $\to$ $|\text{LZBW},-\rangle$ (combined-$CP$-ODD; chirality-negative Linear-ZBW configuration on $-$qCP center)
   - $\zeta^{\text{cont,qDP}} \to$ combined $CP$ at continuum level

2. **(g) Substrate-level stabilization energy calculation**: under the bridge theorem's magnitude inheritance (THEO-CHIR-CONT-1.3), the chirality-asymmetric stabilization-energy operator $\Delta F^{qDP}$ has substrate-handle-inherited magnitude $|M^{\text{eff,qDP}}| = \chi/6 \approx 0.0394$ at leading order, expressed in dimensionless ratio form $\Delta F^{qDP} / F^{eDP}_{\text{ref}}$ where $F^{eDP}_{\text{ref}}$ is the chirality-neutral Orbital-ZBW reference free energy.

3. **(h) Exclusion bound at observable thermodynamic scales**: the chirality-asymmetric stabilization-energy magnitude $\chi/6$ produces a structural exclusion bound on observable Linear-ZBW-on-$\pm$qCP polarization asymmetry $\Delta p_{LR} \approx \chi/6 \approx 0.0394$ at thermodynamic-scale observable precision. Inherits PRED-O-25 leptogenesis CP-asymmetry as primary observable, plus sector-specific extensions to electromagnetic-handedness polarization asymmetry observables.

4. **(i) SM cross-validation**: the chirality-asymmetric stabilization-energy operator $\Delta F^{qDP}$ is cross-validated against SM-2 v1.0 §10 chiral-polarity-bias mechanism (substrate-level framework) and against complementary Sector A V–A coupling derivation (cross-sector unification at magnitude $\chi/6$). Connects SM-2 + SF-2 sector closures at observable scales under joint paper's cross-sector unification framing.

This is the theorem at full theorem-statement level. The proof architecture below outlines 4 steps; **Step 1 closure (sub-claim (f)) at this patch (Patch 0492; Session 1 of §C)**, with Steps 2-4 (sub-claims (g)+(h)+(i)) deferred to Sessions 2+3+4 of §C (Patches 0493+, 0494+, 0495+ candidates).

---

## §2 Proof architecture — 4-step structure for Theorem C.1

The proof of Theorem C.1 proceeds in 4 steps mirroring the §B sector-specific 4-step structure (Step 1 sector-specific operator identification → Step 2 substrate-level magnitude derivation → Step 3 observable-scale exclusion bound → Step 4 cross-validation framing), but with effective-free-energy / partition-function content replacing Yang-Mills EFT V–A kinematic content.

**Step 1 (this patch; §3 below)**: **Sector-specific continuum operator identification** — identify the abstract continuum operator $\mathcal{O}^{\text{eff,qDP}}$ from bridge theorem THEO-CHIR-CONT-1.2 with the specific physical operator $\Delta F^{qDP}$ in the effective free-energy / partition-function framework. The identification matches:
- Group-theoretic structure (continuum-limit $\zeta^{\text{cont,qDP}}$-ODD content $\leftrightarrow$ combined-$CP$-ODD content)
- Algebraic structure (qDP's $D_{5d}$ stabilizer + $A_{2u}$-irrep operator $\leftrightarrow$ continuum effective free-energy chiral-asymmetric structure)
- Matter-doublet content (continuum projection of qDP matter-doublet $\leftrightarrow$ continuum Linear-ZBW chirality-eigenstate pair)

Sub-claim (f) of Theorem C.1 CLOSED at end of Step 1.

**Step 2 (Session 2 target; Patch 0493+ candidate)**: **Substrate-level stabilization energy calculation** — derive the substrate-level magnitude $|M^{\text{eff,qDP}}| = \chi/6$ from bridge theorem's THEO-CHIR-CONT-1.3 topological-projection argument applied to qDP/eDP sector. Inherits THEO-SD-CHIR-2 Finding C-W46 composite matrix element factorization at substrate level: $|M^{qDP}| = |M_{\text{amp}}^{qDP}| \cdot |M_\perp^{qDP}| = \chi \cdot (1/6) = \chi/6$.

Sub-claim (g) of Theorem C.1 CLOSED at end of Step 2.

**Step 3 (Session 3 target; Patch 0494+ candidate)**: **Exclusion bound at observable thermodynamic scales** — connect substrate-handle stabilization-energy magnitude $\chi/6$ to observable Linear-ZBW polarization asymmetry $\Delta p_{LR} \approx \chi/6 \approx 0.0394$. Inherits PRED-O-25 as primary observable; extends to electromagnetic-handedness polarization-asymmetry observables. Quantify falsification thresholds at current + future observational precision.

Sub-claim (h) of Theorem C.1 CLOSED at end of Step 3.

**Step 4 (Session 4 target; Patch 0495+ candidate)**: **SM cross-validation framing** — cross-validate $\Delta F^{qDP}$ identification against SM-2 v1.0 §10 chiral-polarity-bias mechanism + complementary Sector A V–A coupling derivation. Connect SM-2 + SF-2 sector closures at observable scales under joint paper's cross-sector unification framing.

Sub-claim (i) of Theorem C.1 CLOSED at end of Step 4. Theorem C.1 promoted to programme-level registered-theorem status as **THEO-CHIR-CONT-3** at end of §C Session 4 (analog of THEO-CHIR-CONT-2 promotion at end of §B Session 4).

---

## §3 Step 1 — Sector-specific continuum operator identification (Session 1 substantive content)

This section closes Step 1 of Theorem C.1: identify the bridge theorem's abstract sector-agnostic continuum operator $\mathcal{O}^{\text{eff,qDP}}$ with the specific physical chirality-asymmetric stabilization-energy operator $\Delta F^{qDP}$ in the effective free-energy / partition-function framework appropriate to the SM-2 sector.

### §3.1 Inheritance from THEO-CHIR-CONT-1

The bridge theorem THEO-CHIR-CONT-1 delivers (sector-agnostic):

- Continuum-limit projection map $\Phi$ (Definition 11.2.1; Wilson-Fisher block-spin renormalization at substrate cutoff $\Lambda_{\text{sub}} = \ell_{\text{edge}}^{-1}$).
- Continuum-limit Wigner-Eckart datum $\mathcal{D}^{\text{cont}} = (\mathcal{S}^{\text{cont}}, \Gamma^{\text{cont}}, \zeta^{\text{cont}}, \mathcal{O}^{\text{eff}}, \{|\psi^{\text{eff}}_+\rangle, |\psi^{\text{eff}}_-\rangle\}, M^{\text{eff}})$ with group-theoretic structure inherited via Lemma 4.1 + Corollary 4.1.1.
- Continuum operator $\mathcal{O}^{\text{eff}} = \Phi_*\hat{C}$ as the unique (up to overall scalar multiple) $\zeta^{\text{cont}}$-ODD 1D-irrep operator on the continuum-limit 2D $\Gamma^{\text{cont}}$-irrep matter-doublet subspace (Theorem 4.2; THEO-CHIR-CONT-1.2).
- Matrix element magnitude $|M^{\text{eff}}| = \chi/6 \approx 0.0394$ at leading order (Theorem 15.3.1; THEO-CHIR-CONT-1.3).

For sector-specific identification at qDP/eDP, we inherit the qDP/eDP sector instantiation from THEO-SD-CHIR-2 Finding C-W46:

- Substrate object $\mathcal{S}^{\text{sub,qDP}}$: Linear-ZBW configuration on host vertex's first-shell icosahedron with antipodal-pair refinement.
- Stabilizer subgroup $\Gamma^{qDP} = D_{5d}$ (order 20; antipodal-pair $D_{5d}$ refinement of $C_{5v}$).
- $\zeta^{qDP} = \text{combined } CP$ — host-CP-centered spatial inversion ($v \to -v$) combined with $\hat{n}$-flip ($\hat{n} \to -\hat{n}$) combined with qCP-sign flip ($\pm \to \mp$).
- Matter-doublet basis $\{|\Psi_-^{qDP,(1)}\rangle, |\Psi_-^{qDP,(2)}\rangle\}$ with opposite-$\zeta^{qDP}$-parity (2D subspace of $A_{1g} \oplus A_{2u}$ in $D_{5d}$).
- Chirality operator $\hat{C}^{qDP} \in A_{2u}(D_{5d})$ (1D ungerade, character $(1,1,1,-1,-1,-1,-1,1)$ on 8 $D_{5d}$ classes) sourced from $\hat{n}$'s pseudoscalar structure.

### §3.2 SM-2 effective free-energy / partition-function framework — anchor reference

The continuum-limit EFT framework for the SM-2 sector is the **effective free-energy / partition-function framework** — a thermodynamic/statistical-mechanical framework appropriate for ZBW configuration stability + chiral-polarity selection on $\pm$qCP centers. Unlike the Yang-Mills $SU(2)_L \times U(1)_Y$ EFT framework appropriate to §B Sector A (SF-2 V–A coupling), the SM-2 sector operates in a different effective-field-theoretic regime — thermodynamic-scale free energies of Linear-ZBW vs Orbital-ZBW configurations rather than gauge-field-coupling structures.

The framework anchor references:

1. **SM-2 v1.0 §10** (Chiral-Polarity-Bias Mechanism): establishes the chiral-polarity-bias mechanism at substrate level — Capotauro chirality bias preferentially stabilizes Linear-ZBW configurations on $-$qCP centers (over $+$qCP centers; or vice versa per $\zeta^{qDP}$-parity convention) with magnitude $\chi/6$ at substrate level.

2. **SM-2 v1.0 §5+§6+Glossary**: substrate characterization of Linear vs Orbital ZBW configurations as ZBW-configuration-types on host vertex's first-shell icosahedron. Orbital ZBW (eDP, $d=0$): full $I_h$ stabilizer at host CP; chirality-neutral reference. Linear ZBW (qDP, $d=1$): selects 1-vertex first-shell subset with $C_{5v} \subset I_h$ stabilizer (refined to $D_{5d}$ at antipodal-pair level per THEO-SD-CHIR-2 Finding C-W45).

3. **THEO-SD-CHIR-2 Finding C-W46**: composite matrix element factorization at substrate level $|M^{qDP}| = \chi/6$ via amplitude factor $\chi$ + cage-shell factor $1/6$. Inherits SM-2 v1.0 §10 chiral-polarity-bias at substrate-physics rigor.

In this effective free-energy framework, the continuum-limit physical content is:

- Continuum Linear-ZBW configurations on $\pm$qCP centers $|\text{LZBW},\pm\rangle$ as continuum-EFT states.
- Continuum free-energy operator $F^{eDP}_{\text{ref}}$ for the chirality-neutral Orbital-ZBW reference configuration (full $I_h$ stabilizer at host CP).
- Continuum chirality-asymmetric stabilization-energy operator $\Delta F^{qDP}$ measuring the free-energy difference between Linear-ZBW configurations on $+$qCP vs $-$qCP centers — equivalently, the chirality-bias measure.
- Combined $CP$ operation at continuum level: $\zeta^{\text{cont,qDP}}$ implements the chirality-flipping action on continuum Linear-ZBW configurations by simultaneously flipping spatial position + $\hat{n}$ direction + qCP-sign.

The chirality-asymmetric stabilization-energy operator is:
$$\Delta F^{qDP} = F[\text{LZBW},+] - F[\text{LZBW},-]$$
where $F[\text{LZBW},\pm]$ denotes the effective free energy of the Linear-ZBW configuration on $\pm$qCP center at continuum thermal-equilibrium scales. Its parity content under combined $CP$:
$$\zeta^{\text{cont,qDP}}\, [\Delta F^{qDP}]\, (\zeta^{\text{cont,qDP}})^{-1} = -\Delta F^{qDP}$$
i.e., $\Delta F^{qDP}$ is combined-$CP$-ODD. This combined-$CP$-parity structure is the key continuum-EFT signature for chirality-sensitive operators in the SM-2 sector.

### §3.3 Identification map — substrate qDP/eDP to continuum effective free-energy

The identification of the bridge theorem's sector-agnostic outputs with the SM-2 effective-free-energy physical content proceeds via three identifications (analog of §B Step 1 three identifications for Sector A):

**Identification 1**: Continuum-limit $\zeta^{\text{cont,qDP}}$ identifies as combined $CP$ at continuum level.

The substrate-level $\zeta^{qDP} = \text{combined } CP$ (host-CP-centered spatial inversion + $\hat{n}$-flip + qCP-sign flip; THEO-SD-CHIR-2 Finding C-W46) is a chirality-flipping $\mathbb{Z}_2$ involution combining three flips: $v \to -v$ + $\hat{n} \to -\hat{n}$ + $\pm \to \mp$. Under the continuum-limit projection map $\Phi$ + Lemma 4.1 (THEO-CHIR-CONT-1.1), $\zeta^{qDP}$ projects to $\zeta^{\text{cont,qDP}}$ — a continuum-limit $\mathbb{Z}_2$ generator with the same combined-$CP$ structure on the continuum-limit Linear-ZBW configuration pair.

In the effective free-energy framework, the chirality-flipping $\mathbb{Z}_2$ generator on continuum Linear-ZBW configurations is combined $CP$ at continuum level — the natural continuum-EFT lift of substrate-level combined $CP$ preserving its $\mathbb{Z}_2$ structure ($(\zeta^{\text{cont,qDP}})^2 = 1$) and chirality-flipping action on configuration chirality.

The identification:
$$\zeta^{\text{cont,qDP}} \leftrightarrow \text{combined } CP \text{ at continuum level}$$
matches structure (combined-$CP$ chirality-flipping involution; $\mathbb{Z}_2$ generator) and action (preserves chirality-EVEN/ODD content via combined-$CP$-EVEN/ODD content).

**Identification 2**: Continuum-limit matter-doublet $\{|\Psi_-^{qDP,(1)}\rangle, |\Psi_-^{qDP,(2)}\rangle\}$ identifies as Linear-ZBW chirality-eigenstate pair $\{|\text{LZBW},+\rangle, |\text{LZBW},-\rangle\}$.

The substrate-level matter-doublet has opposite-$\zeta^{qDP}$-parity (THEO-SD-CHIR-2 Finding C-W46; spans 2D subspace of $A_{1g} \oplus A_{2u}$ in $D_{5d}$). The continuum-limit projection $\{|\psi^{\text{eff}}_+\rangle, |\psi^{\text{eff}}_-\rangle\}$ has opposite-$\zeta^{\text{cont,qDP}}$-parity (Lemma 4.1 (5) parity-matching preservation under $\Phi$).

In the effective free-energy framework, the natural opposite-combined-$CP$-parity pair is the Linear-ZBW chirality-eigenstate pair $\{|\text{LZBW},+\rangle, |\text{LZBW},-\rangle\}$ where:
- $|\text{LZBW},+\rangle$ = Linear-ZBW configuration on $+$qCP center (combined-$CP$-EVEN; chirality-positive)
- $|\text{LZBW},-\rangle$ = Linear-ZBW configuration on $-$qCP center (combined-$CP$-ODD; chirality-negative)

The identification:
$$|\Psi_-^{qDP,(1)}\rangle \leftrightarrow |\text{LZBW},+\rangle, \quad |\Psi_-^{qDP,(2)}\rangle \leftrightarrow |\text{LZBW},-\rangle$$
matches parity content under Identification 1 ($\zeta^{qDP}$-EVEN $\leftrightarrow$ combined-$CP$-EVEN $\leftrightarrow$ chirality-positive Linear-ZBW; $\zeta^{qDP}$-ODD $\leftrightarrow$ combined-$CP$-ODD $\leftrightarrow$ chirality-negative Linear-ZBW).

**Identification 3**: Continuum-limit chirality-sensitive operator $\mathcal{O}^{\text{eff,qDP}}$ identifies as chirality-asymmetric stabilization-energy operator $\Delta F^{qDP}$.

Under Identifications 1 + 2, the bridge theorem's sector-agnostic continuum operator structure (Theorem 4.2; THEO-CHIR-CONT-1.2: $\mathcal{O}^{\text{eff,qDP}}$ is $\zeta^{\text{cont,qDP}}$-ODD with non-vanishing matrix element between opposite-$\zeta^{\text{cont,qDP}}$-parity matter-doublet states) translates to the continuum effective-free-energy requirement:

- The continuum-EFT chirality-sensitive operator is combined-$CP$-ODD;
- The operator has non-vanishing matrix element between $|\text{LZBW},+\rangle$ and $|\text{LZBW},-\rangle$;
- The operator transforms as a (free-energy) scalar under continuum Lorentz at thermal-equilibrium scales (inheriting from effective-free-energy framework's reduction to thermodynamic potentials).

These three properties uniquely identify the operator (up to overall scalar normalization) as the chirality-asymmetric stabilization-energy operator $\Delta F^{qDP} = F[\text{LZBW},+] - F[\text{LZBW},-]$ in the effective free-energy / partition-function framework:

$$\boxed{\mathcal{O}^{\text{eff,qDP}} \leftrightarrow \Delta F^{qDP}}$$

up to overall normalization fixed by the bridge theorem's magnitude inheritance THEO-CHIR-CONT-1.3 at leading order: matrix element magnitude $|M^{\text{eff,qDP}}| = \chi/6 \approx 0.0394$ corresponds to the dimensionless stabilization-energy asymmetry ratio $\Delta F^{qDP} / F^{eDP}_{\text{ref}}$ at the substrate handle's projection level.

### §3.4 Chirality-asymmetric stabilization-energy operator — sector-specific physical content

With Identification 3 in place, the chirality-asymmetric stabilization-energy operator $\Delta F^{qDP}$ inherits the bridge theorem's properties at SM-2 sector-specific physical level:

1. **Combined-$CP$-ODD parity structure**: the parity content (Identification 1 + Theorem 4.2) guarantees combined-$CP$-ODD. A hypothetical combined-$CP$-EVEN component would not contribute to chirality bias and is structurally excluded.

2. **Magnitude inheritance at leading order**: $|\Delta F^{qDP} / F^{eDP}_{\text{ref}}| = \chi/6 \approx 0.0394$ at leading order via THEO-CHIR-CONT-1.3 topological-projection argument. Sub-leading corrections enter at $(a/L)^n$ for $n \geq 1$, negligible at SM-2 thermodynamic scale ($a/L \ll 1$ in deep-infrared regime).

3. **Effective free-energy / partition-function context**: $\Delta F^{qDP}$ enters the SM-2 chiral-polarity-bias mechanism at thermal-equilibrium scales — Linear-ZBW configurations on $-$qCP centers preferentially stabilized relative to Linear-ZBW configurations on $+$qCP centers (or vice versa per $\zeta^{qDP}$-parity convention) with magnitude $\chi/6$ producing observable chirality bias at thermodynamic scales.

4. **Scalar structure**: $\Delta F^{qDP}$ is a (free-energy) scalar at continuum thermal-equilibrium scales, inheriting from effective-free-energy framework's reduction of full-spacetime-symmetric continuum-EFT to thermodynamic potentials at thermal-equilibrium scales.

### §3.5 Step 1 closure — what is in hand at end of §C Session 1

Sub-claim (f) of Theorem C.1 (sector-specific continuum operator identification) CLOSED:

- $\mathcal{O}^{\text{eff,qDP}}$ identifies as $\Delta F^{qDP}$ chirality-asymmetric stabilization-energy operator in effective free-energy / partition-function framework.
- Identification via three matched structural conditions: combined-$CP$-parity content (Identification 1); opposite-parity matter-doublet content (Identification 2); combined-$CP$-ODD non-vanishing-matrix-element structure (Identification 3).
- Sub-leading corrections suppressed by deep-infrared regime at SM-2 thermodynamic scale.
- Sector-specific physical properties inherited at leading order: combined-$CP$-ODD parity structure; coupling magnitude $\chi/6$; effective free-energy / partition-function thermodynamic context; scalar structure.

The continuum-EFT chirality-asymmetric stabilization-energy operator is now established as the physical operator that the bridge theorem's abstract continuum operator identifies as in the SM-2 sector. Steps 2–4 of §C build on this identification to derive substrate-level magnitude + observable-scale exclusion bound + SM cross-validation.

---

## §4 Step 2 setup architecture — Substrate-level stabilization energy calculation (Session 2 target; Patch 0493+ candidate)

Session 2 of §C closes sub-claim (g) of Theorem C.1: derive the substrate-level stabilization-energy magnitude $|M^{\text{eff,qDP}}| = \chi/6$ from THEO-CHIR-CONT-1.3 topological-projection argument applied to qDP/eDP sector.

**Setup**:

- THEO-SD-CHIR-2 Finding C-W46 establishes substrate-level composite matrix element $|M^{qDP}| = |M_{\text{amp}}^{qDP}| \cdot |M_\perp^{qDP}| = \chi \cdot (1/6) = \chi/6$ at full Layer 3 rigor.
- Amplitude factor $\chi$: chirality-eigenvalue matching analog of K3 + W-bracelet, matter-doublet's $S_3$-like amplitude structure within $\zeta^{qDP}$-pairing produces spectral radius $\sqrt{3}$ identified with substrate primitive chirality eigenvalues $\pm\chi$.
- Cage-shell factor $1/6$: $d_\Gamma/V_{\text{cage}} = 2/12 = 1/6$ via cage-shell averaging on shared icosahedral cage at host CP.
- Under THEO-CHIR-CONT-1.3 (Theorem 15.3.1; Magnitude Inheritance via Topological Projection), the substrate magnitude $\chi/6$ projects through $\Phi$ to continuum-limit effective coupling $|M^{\text{eff,qDP}}| = \chi/6$ at leading order without renormalization.

**Session 2 substantive content**: confirm THEO-CHIR-CONT-1.3 applies to qDP/eDP sector via topological-projection argument (Claim 15.1.2 + Claim 15.2.1 + Definition 15.1.1 sector-agnostic structure); verify $\chi$ remains topological substrate quantity at qDP/eDP sector; verify $1/6 = d_\Gamma/V_{\text{cage}}$ remains topological cage-shell factor under $\Phi$; confirm sub-leading $(a/L)^n$ corrections negligible at SM-2 thermodynamic scale.

**Anti-priority at Session 2**: do NOT re-derive substrate-level magnitude from scratch — inherit THEO-SD-CHIR-2 Finding C-W46 as established Layer 3 closure; §C Step 2 task is bridge-theorem-application not substrate-level derivation.

---

## §5 Step 3 setup architecture — Exclusion bound at observable thermodynamic scales (Session 3 target; Patch 0494+ candidate)

Session 3 of §C closes sub-claim (h) of Theorem C.1: connect substrate-handle stabilization-energy magnitude $\chi/6$ to observable Linear-ZBW polarization asymmetry $\Delta p_{LR} \approx \chi/6 \approx 0.0394$ at thermodynamic-scale observable precision.

**Setup**:

- Substrate-handle magnitude $\chi/6 \approx 0.0394$ propagates to observable scale via THEO-CHIR-CONT-1.3 magnitude inheritance + thermodynamic-scale linear-response framework.
- Observable: Linear-ZBW-on-$\pm$qCP polarization asymmetry $\Delta p_{LR}$ at thermal-equilibrium scales — directly observable via baryogenesis / leptogenesis CP-asymmetry measurements (PRED-O-25 inheritance from THEO-CAP-1 + THEO-SD-CHIR-1+2).
- Prediction at leading order: $\Delta p_{LR}^{\text{predicted}} = \chi/6 \approx 0.0394$.
- Empirical anchor: $\Delta p_{LR}^{\text{obs}} \sim 0.04$ from BAU back-derivation (Davidson, Nardi, Nir 2008). Match within 2%.

**Session 3 substantive content**: walk through substrate-handle-to-observable projection at thermodynamic scales; quantify falsification thresholds at current + future observational precision; connect to PRED-O-25; identify secondary observables (electromagnetic-handedness polarization-asymmetry observables) for sector-specific extension. Note: Threshold (C) at §B (leptogenesis CP-asymmetry) is the same observable as primary §C threshold — both sectors converge on the same direct test of substrate-handle magnitude inheritance.

**Anti-priority at Session 3**: do NOT duplicate Threshold (C) discussion from §B Step 4 (Patch 0491 §18.2) — §C Step 3 should focus on SM-2-specific framing (Linear-ZBW polarization asymmetry as the observable name in SM-2 framework) and complementary observable channels.

---

## §6 Step 4 setup architecture — SM cross-validation framing (Session 4 target; Patch 0495+ candidate)

Session 4 of §C closes sub-claim (i) of Theorem C.1: cross-validate $\Delta F^{qDP}$ identification against SM-2 v1.0 §10 chiral-polarity-bias mechanism + complementary Sector A V–A coupling derivation.

**Setup**:

- Cross-validation against SM-2 v1.0 §10: confirm $\Delta F^{qDP}$ identification at this patch is consistent with SM-2 v1.0 §10's substrate-level chiral-polarity-bias mechanism; identify how §C Step 1 identification elevates SM-2 substrate-level mechanism to Layer 4 continuum-EFT observable level.
- Cross-sector unification with §B: connect §C (SM-2 sector closure; THEO-CHIR-CONT-3 candidate) to §B (SF-2 sector closure; THEO-CHIR-CONT-2). Both inherit THEO-CHIR-CONT-1 sector-agnostic bridge and produce sector-specific Layer 4 closures with same substrate-handle magnitude $\chi/6$.
- Joint paper §D (cross-sector unification framing; Patches 0496+) builds on §C Step 4 cross-validation as preparation.

**Session 4 substantive content**: explicit cross-validation discussion connecting §C SM-2 closure to §B SF-2 closure at observable scales; identify cross-sector unification observable predictions (e.g., both sectors predict same magnitude $\chi/6$ for leptogenesis CP-asymmetry — Threshold (C) of §B Step 4 = primary observable of §C Step 3); promote Theorem C.1 to programme-level registered-theorem status as THEO-CHIR-CONT-3 at end of Session 4.

**Anti-priority at Session 4**: do NOT extend cross-sector unification framing into joint paper §D content (Patches 0496+ scope). §C Step 4 closes Theorem C.1 cross-validation at §C scope; §D opens broader cross-sector unification + paper polish at v0.5 scope.

---

## §7 Sector-agnostic vs sector-specific content map

Inherited from THEO-CHIR-CONT-1 (sector-agnostic):

- Continuum-limit projection map $\Phi$ (Definition 11.2.1).
- Continuum-limit Wigner-Eckart datum $\mathcal{D}^{\text{cont}}$ (Corollary 4.1.1).
- Continuum operator $\mathcal{O}^{\text{eff,sector}}$ as $\zeta^{\text{cont,sector}}$-ODD 1D-irrep operator (Theorem 4.2; THEO-CHIR-CONT-1.2).
- Matrix element magnitude $|M^{\text{eff,sector}}| = \chi/6$ at leading order (Theorem 15.3.1; THEO-CHIR-CONT-1.3).
- Definition 15.1.1 (Topological Substrate Quantity) as programme-level concept.

Sector-specific to §C (this sketch):

- Step 1: identification $\mathcal{O}^{\text{eff,qDP}} \leftrightarrow \Delta F^{qDP}$ + identifications $\zeta^{\text{cont,qDP}} \leftrightarrow$ combined $CP$ at continuum + matter-doublet $\leftrightarrow \{|\text{LZBW},+\rangle, |\text{LZBW},-\rangle\}$.
- Step 2: substrate-level magnitude $\chi/6$ inheritance via THEO-CHIR-CONT-1.3 + THEO-SD-CHIR-2 Finding C-W46.
- Step 3: observable Linear-ZBW polarization asymmetry $\Delta p_{LR} = \chi/6$ at thermodynamic scales.
- Step 4: SM cross-validation framing against SM-2 v1.0 §10 + §B Sector A cross-sector unification.

The sector-agnostic content (§A bridge) does the heavy lifting on continuum-limit projection structure + magnitude inheritance; the sector-specific content (§C Sector B) does the sector-specific physical-operator identification + substrate-handle-to-observable projection + cross-validation.

---

## §8 FI dependency mapping for §C Sector B

Inherited from THEO-CHIR-CONT-1 (the bridge theorem):

- **FI-CHIR-CONT-1** (substrate primitive 4D direction $\hat{n}$).
- **FI-CHIR-CONT-2** (substrate chirality magnitude $|\chi| = \phi^{-3}$).
- **FI-CHIR-CONT-3** (substrate residual symmetry $H_3 = I_h$).
- **FI-CHIR-CONT-9** (Substrate-Locality Theorem of Capotauro v2.0).

Sector-specific to §C Sector B (the qDP/eDP sector + effective free-energy framework):

- **FI-CHIR-CONT-13** (qDP/eDP sector specialization: substrate object as Linear-ZBW configuration on host vertex's first-shell icosahedron with antipodal-pair refinement, stabilizer $D_{5d}$, $\zeta^{qDP} = \text{combined } CP$, chirality operator $\hat{C}^{qDP} \in A_{2u}(D_{5d})$ — inherited from THEO-SD-CHIR-2 sector instantiation).
- **FI-CHIR-CONT-14** (SM-2 effective free-energy / partition-function framework: continuum-limit effective framework for SM-2 sector as thermodynamic/statistical-mechanical free-energy formalism — inherited from SM-2 v1.0 §10 chiral-polarity-bias framework + §5+§6+Glossary ZBW characterization).
- **FI-CHIR-CONT-15** (continuum-EFT combined-$CP$-parity structure: combined $CP$ at continuum level as chirality-flipping involution on continuum Linear-ZBW configurations with combined-$CP$-EVEN / ODD projection structure — inherited from standard effective-free-energy framework + Capotauro mechanism's three-way coupling structure per SM-2 v1.0 §10).

CPP axioms most load-bearing for §C Sector B:

- **AXIM-1**: CP existence (load-bearing for FI-CHIR-CONT-1 + FI-CHIR-CONT-15 combined-$CP$-parity structure + qCP-sign as intrinsic CP property).
- **AXIM-2**: 600-cell topology (load-bearing for FI-CHIR-CONT-13 qDP/eDP sector + FI-CHIR-CONT-3 + FI-CHIR-CONT-9; antipodal-pair $D_{5d}$ structure + $I_h \to D_{5d}$ branching).
- **AXIM-3**: Dipole Sea / DI-bit propagation (load-bearing for FI-CHIR-CONT-14 effective-free-energy framework via dipole-sea-mediated thermal-equilibrium structure).
- **AXIM-4**: SSV interaction / Nexus (load-bearing for FI-CHIR-CONT-9 Substrate-Locality + cage-shell averaging via FI-C-10 on shared icosahedral cage at host CP).
- **AXIM-7**: Substrate-stress (load-bearing for FI-CHIR-CONT-1 substrate primitive direction sourcing chirality operator + Capotauro mechanism's three-way coupling structure under Picture B framework).

---

## §9 Anti-priorities for §C sector-specific work (programme-level)

In addition to Session-1-specific anti-priorities in §0 above:

- **Do NOT exceed Sector B (SM-2) scope**: §C closes chiral-polarity-bias derivation for SM-2 sector specifically; other strong-sector or standard-model sub-claims (e.g., QCD vacuum structure beyond chiral-polarity-bias; nuclear strong-force chirality beyond SM-2 §10) are NOT in §C scope. Such sub-claims if needed have their own future-window venues at SM-2 v2.0+ or strong-sector follow-up papers.

- **Do NOT modify Capotauro v2.0 + SF-2 v1.0 + SM-2 v1.0 .tex sources** during §C drafting: all v1.0 SHIPPED with .tex source frozen. §C references SM-2 v1.0 §10 + THEO-SD-CHIR-2 + Capotauro v2.0 + THEO-CHIR-CONT-1 as inheritance points; modifications to those papers happen at v2.0+ via separate publication-pathway windows.

- **Do NOT promote Theorem C.1 to programme-level registered-theorem status at §C Session 1**: registration at end of §C Session 4 when all four sub-claims (f)+(g)+(h)+(i) close. Premature promotion at Sessions 1–3 would violate the four-condition test pattern.

- **Do NOT introduce new FI-CHIR-CONT-N entries beyond FI-CHIR-CONT-13/14/15 at §C**: the FI inventory is at v0.1 outline + 3 sector-specific (§B; FI-CHIR-CONT-10/11/12) + 3 sector-specific (§C; FI-CHIR-CONT-13/14/15) for maximum 6 sector-specific FIs.

- **Do NOT mix §C sector-specific content with §B sector-specific content**: §C (this sketch) is SM-2 chiral-polarity-bias derivation; §B (`sector_a_va_coupling.md`) is SF-2 V–A coupling derivation. The two sector closures use parallel structure (bridge inheritance + sector-specific identification + downstream projection + cross-validation) but with different EFT frameworks (effective free-energy for §C; Yang-Mills EFT for §B).

- **Do NOT undo §A / §B closure in §C drafting**: the bridge theorem THEO-CHIR-CONT-1 + Sector A theorem THEO-CHIR-CONT-2 are fixed; §C inherits from THEO-CHIR-CONT-1 without modification and runs parallel to §B without affecting §B closure.

---

## §10 Status update at §C Session 1 end

**Patch**: 0492 (this patch; §C Sector B Session 1 — Sketch OPENED + Step 1 sector-specific continuum operator identification CLOSED).

**Date**: 20 May 2026 (Session 137 continuation, post-Patch 0491 §B CLOSURE).

**Programme state changes**:

1. **§C Sector B working sketch OPENED** at `flagship_papers/chirality_continuum/sketches/sector_b_chiral_polarity_bias.md` (this file, ~430 lines).
2. **Theorem C.1 statement ESTABLISHED** at theorem-statement level (THEO-CHIR-CONT-3 candidate): Sector B Effective Free-Energy Framework Chiral-Polarity-Bias Derivation theorem with four sub-claims (f)+(g)+(h)+(i). Sub-claim (f) sector-specific continuum operator identification CLOSED at this patch via §3 Step 1 closure.
3. **Step 1 of Theorem C.1 closure ACHIEVED**: sector-specific continuum operator identification — $\mathcal{O}^{\text{eff,qDP}} \leftrightarrow \Delta F^{qDP}$ in effective free-energy / partition-function framework via three structural identifications (Identification 1: $\zeta^{\text{cont,qDP}} \leftrightarrow$ combined $CP$ at continuum level; Identification 2: matter-doublet $\leftrightarrow \{|\text{LZBW},+\rangle, |\text{LZBW},-\rangle\}$ Linear-ZBW chirality-eigenstate pair; Identification 3: $\mathcal{O}^{\text{eff,qDP}} \leftrightarrow \Delta F^{qDP}$ chirality-asymmetric stabilization-energy operator).
4. **Sector-specific physical content inherited at leading order**: combined-$CP$-ODD parity structure; magnitude inheritance $\chi/6$; effective-free-energy thermodynamic context; scalar structure at thermal-equilibrium scales.
5. **Steps 2–4 setup architecture ARTICULATED** for Sessions 2+3+4 of §C (Patches 0493+, 0494+, 0495+ candidates): Step 2 substrate-level stabilization energy calculation via THEO-CHIR-CONT-1.3 + THEO-SD-CHIR-2 Finding C-W46; Step 3 observable Linear-ZBW polarization asymmetry $\Delta p_{LR} = \chi/6$ at thermodynamic scales; Step 4 SM cross-validation framing against SM-2 v1.0 §10 + §B cross-sector unification.
6. **FI dependency mapping COMPLETE** for §C Sector B: FI-CHIR-CONT-1/2/3/9 (substrate-level inheritance from THEO-CHIR-CONT-1) + FI-CHIR-CONT-13/14/15 (sector-specific to §C: qDP/eDP sector specialization + SM-2 effective-free-energy framework + continuum-EFT combined-$CP$-parity structure) + AXIM-1/2/3/4/7 (CPP axiom stack inheritance).
7. **NO theorems registered new at programme level** (THEO-CHIR-CONT-3 candidate at theorem-statement level only; registration at end of §C Session 4 upon sub-claims (f)+(g)+(h)+(i) all closing).
8. **NO predictions registered new** (substrate-level stabilization energy + observable Linear-ZBW polarization asymmetry + SM cross-validation are sub-claim targets pending Sessions 2+3+4 of §C; PRED-O-25 inherited at substrate-handle level from THEO-CAP-1 + THEO-SD-CHIR-1+2 + THEO-CHIR-CONT-1).
9. **NO falsifiers registered new** (Capotauro Falsifier 6 already ACTIVATED at §B Step 4 Patch 0491; §C Step 3 will provide complementary observable-scale anchor at SM-2 sector).
10. **NO conjecture registrations**.

**Forward queue post-Patch 0492**:

- **Priority 1 (Patch 0493+ candidate)**: §C Sector B Session 2 — Step 2 substrate-level stabilization energy calculation via THEO-CHIR-CONT-1.3 + THEO-SD-CHIR-2 Finding C-W46. 1 session estimated.
- **Priority 2 (Patch 0494+ candidate)**: §C Sector B Session 3 — Step 3 exclusion bound at observable thermodynamic scales. 1 session estimated.
- **Priority 3 (Patch 0495+ candidate)**: §C Sector B Session 4 — Step 4 SM cross-validation + Theorem C.1 promotion to programme-level registered-theorem status as THEO-CHIR-CONT-3. 1 session estimated. **§C SUB-CLAIM (f)+(g)+(h)+(i) CLOSURE PATCH**.
- **Subsequent (Patches 0496+)**: §D cross-sector unification framing + paper polish; v0.5; 1–2 sessions.
- **Subsequent (Patches 0498+)**: v0.6–v0.9 reviewer cycle; v1.0 SHIP at Patch 0503+.

**Anti-priorities preserved**: as enumerated in §0 + §9 above. Most critical for Session 1 → Session 2 transition of §C: do NOT close Steps 2–4 at Session 1 (deferred to Sessions 2–4 of §C); do NOT promote Theorem C.1 to programme-level registered-theorem status at Session 1 (registration at end of §C Session 4 patch).

**Methodological observation — §C Step 1 closure inherits cleanly from §A bridge theorem + §B precedent**: the sector-specific operator identification §C Step 1 closure followed the structural template established at §B Step 1 (Patch 0488) — three identifications across structural / algebraic / matter-doublet content lines fully closing the sector-specific identification. The cleanness of this inheritance — applied at SM-2 sector with different EFT framework (effective free-energy vs Yang-Mills V–A) but identical structural pattern — confirms the joint paper format's two-layer architecture works as designed: §A delivers sector-agnostic substrate-handle-to-effective-coupling bridge; §B + §C apply sector-specific identification and downstream projection at parallel structural template.

---

*Sketch authored by Claude Opus (Anthropic) under Thomas Lee Abshier's direction, 20 May 2026, Session 137 continuation, Patch 0492 (Session 1 of §C Sector B SM-2 chiral-polarity-bias derivation). Opens substantive §C sector-specific work at the joint Layer 4 paper post §B CLOSURE. Session 1 deliverable: Theorem C.1 statement + Step 1 sector-specific continuum operator identification + Steps 2–4 setup architecture. Sub-claim (f) (sector-specific operator identification) CLOSED at this patch via three structural identifications ($\zeta^{\text{cont,qDP}} \leftrightarrow$ combined $CP$ at continuum; matter-doublet $\leftrightarrow \{|\text{LZBW},+\rangle, |\text{LZBW},-\rangle\}$; $\mathcal{O}^{\text{eff,qDP}} \leftrightarrow \Delta F^{qDP}$ chirality-asymmetric stabilization-energy operator). Sub-claims (g)+(h)+(i) closure target at Sessions 2+3+4 of §C (Patches 0493+, 0494+, 0495+ candidates). THEO-CHIR-CONT-3 candidate at theorem-statement-with-Step-1-closed level; registration at programme theorem-registry at end of §C Session 4.*
