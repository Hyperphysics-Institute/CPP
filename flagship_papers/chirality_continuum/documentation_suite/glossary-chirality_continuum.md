# Glossary: Chirality Continuum

**Series:** Flagship paper (Chirality Continuum line)
**Last updated:** 20 May 2026 (Patch 0511 — chirality continuum v1.0 SHIPPED companion suite production)

This glossary defines paper-specific terms used in the chirality continuum joint paper. Terms inherited from CPP framework-level vocabulary (Conscious Point, Dipole Sea, polytope substrate, etc.) are defined in `master_glossary.md` at the repo root; this file defines terms introduced or sharpened in the chirality continuum paper.

---

## A. Constants

### $\chi$ (substrate chirality magnitude)
Dimensionless substrate-level chirality parameter on the 600-cell polytope substrate. Value: $|\chi| = \varphi^{-3}$ where $\varphi = (1+\sqrt{5})/2$ is the golden ratio. Equivalently $|\chi| \approx 0.23607$. **First-use:** §3 + §3.2; Capotauro v2.0 §sec:chi_resolution + Finding C-W39 (substrate-level identification). **Related:** $\varphi$ (golden ratio); $\hat{n}$ (substrate primitive 4D direction); FI-CHIR-CONT-2 (foundational input postulating $|\chi| = \varphi^{-3}$).

### $\chi/6$ (substrate-handle magnitude)
The unified substrate-handle magnitude across three Capotauro v2.0 sectors. Value: $|\chi|/6 = \varphi^{-3}/6 \approx 0.0394$. Identified as substrate-level chirality matrix element magnitude $|M^{\text{sector}}| = \chi/6$ in K3-doublet (THEO-CAP-1), W-bracelet (THEO-SD-CHIR-1), and qDP/eDP (THEO-SD-CHIR-2) sectors. Survives continuum-limit projection at leading order via topological-projection argument (Theorem 3.3 = THEO-CHIR-CONT-1.3). **First-use:** §3 + §3.3 + §3.4. **Related:** cage-shell factor $1/6$; topological substrate quantity (Definition 3.3).

### $\Delta p_{LR}$ (leptogenesis CP-asymmetry, primary observable)
The primary empirical observable of the chirality continuum joint paper. Defined as polarization asymmetry $\Delta p_{LR} = (N[\text{LZBW},-] - N[\text{LZBW},+])/(N[\text{LZBW},-] + N[\text{LZBW},+])$ in SM-2 v1.0 §10 framework; observable channel = leptogenesis CP-asymmetry $\epsilon_{CP}$ via Davidson, Nardi, Nir 2008. Predicted value at leading order: $\Delta p_{LR} = \chi/6 \approx 0.0394$; empirical anchor $\Delta p_{LR}^{\text{obs}} \sim 0.04$ from BAU back-derivation; match within 2%. **First-use:** §1 + §1.2 + §5 + §6. **Related:** PRED-O-25 (primary substrate-handle prediction); Capotauro Falsifier 6 Threshold (C).

### $1/6$ (cage-shell factor)
Dimensionless cage-shell averaging factor $d_\Gamma/V_{\text{cage}} = 2/12$ where $d_\Gamma = 2$ is the matter-doublet effective dimension and $V_{\text{cage}} = 12$ is the icosahedral cage vertex count. Common across all three Capotauro v2.0 sector instantiations. Topological substrate quantity per Claim 3.2.1 (integer-valued representation-theoretic + polytope-topological invariants). **First-use:** §3.3 + §3.4. **Related:** Schur orthogonality cage-shell averaging; $\chi/6$ unified substrate-handle magnitude.

### $\hat{n}$ (substrate primitive 4D direction)
The 4-dimensional direction picked out as substrate's chirality-breaking primitive at vertex-aligned Reading C. Identified $\hat{n} = v_{\text{host}}$ a 600-cell vertex direction per Capotauro v2.0 Finding C-W37 by three converging arguments. **First-use:** §3 + §3.2; Capotauro v2.0 §sec:primitive_direction. **Related:** FI-CHIR-CONT-1 (foundational input postulating $\hat{n}$); Q1$'$+Q1$'$.A Layer 3 promotion programme (the dynamical-substrate-law gate).

---

## B. Structural terms

### Substrate handle
Dimensionless substrate-level magnitude (here $\chi/6 \approx 0.0394$) carrying physical information that propagates to observable scales via continuum-limit projection. The chirality continuum paper establishes the propagation via topological-projection argument: the substrate handle is preserved at leading order across all RG-flow scales between the substrate cutoff $\Lambda_{\text{sub}} = \ell_{\text{edge}}^{-1}$ and observable kinematic scales $\mu_{\text{obs}}^{\text{sector}}$. **First-use:** §1.

### Bridge theorem
Theorem 3.4 of the joint paper = THEO-CHIR-CONT-1: the Substrate-Handle-to-Effective-Coupling Bridge Theorem. Establishes existence + magnitude inheritance + chirality content preservation of the continuum operator $\mathcal{O}^{\text{eff,sector}} = \Phi_*\hat{C}^{\text{sector}}$ at sector-agnostic level. Sector-specific identifications follow at §4 (V–A coupling) and §5 (chiral-polarity-bias). **First-use:** §3.

### Sector-agnostic bridge
Architectural property of THEO-CHIR-CONT-1: the projection machinery depends only on universal substrate data $(|\chi|, d_\Gamma/V_{\text{cage}}) = (\varphi^{-3}, 1/6)$ not on sector-specific $(\Gamma, \zeta^{\text{sector}}, \hat{C}^{\text{sector}})$ beyond labels. Single bridge theorem closes the substrate-to-effective-coupling step for all sectors simultaneously; sector-specific kinematic projections (V–A current operator + effective free-energy stabilization-energy operator) become applications of the same bridge. **First-use:** §3.

### Continuum-limit projection map $\Phi$
Definition 3.2 of the joint paper. Wilson-Fisher block-spin renormalization at substrate cutoff $\Lambda_{\text{sub}} = \ell_{\text{edge}}^{-1}$ with equivariance, block-spin commutativity, and well-defined continuum-limit existence conditions. Projects substrate-level structure (group $G = I_h$, stabilizer $\Gamma$, generator $\zeta$, matter-doublet, chirality operator $\hat{C}^{\text{sector}}$) to continuum-limit structure ($G^{\text{cont}}, \Gamma^{\text{cont}}, \zeta^{\text{cont}}, \psi^{\text{eff}}, \mathcal{O}^{\text{eff,sector}}$). **First-use:** §3.2; introduced as Definition 11.2.1 of the joint paper §3 working sketch (Session 137 Patch 0486); promoted to paper-level Definition 3.2 at Patch 0498. **Related:** METH-CHIR-CONT-2.

### Topological substrate quantity
Definition 3.3 of the joint paper. Programme-level concept (Definition 15.1.1 of joint paper §3 working sketch). A dimensionless substrate-level quantity determined entirely by combinatorial-geometric structure + primitive feature identifications without substrate-field-theoretic dynamics or RG-flow scale parameters. Standard QFT analogs: anomaly coefficients $1/(16\pi^2)$ exact at all loop orders per Adler-Bardeen; topological charges $n \in \mathbb{Z}$ in $\theta$-vacuum sectors; Chern-Simons levels $k \in \mathbb{Z}$; Atiyah-Singer index theorem contributions; discrete symmetry parities $\mathbb{Z}_2$-valued; polytope-geometric invariants. **First-use:** §3.3. **Related:** METH-CHIR-CONT-3.

### Sector-agnostic substrate Wigner-Eckart datum
Definition 3.1 of the joint paper. Mathematical object packaging the universal substrate-level data $(|\chi|, d_\Gamma, V_{\text{cage}}, \zeta\text{-parity matching})$ reusable across Capotauro v2.0 sector instantiations. First introduced as Definition 3.2.1 of the joint paper §3 working sketch (Session 137 Patch 0485); promoted to paper-level Definition 3.1 at Patch 0498. **Related:** METH-CHIR-CONT-1.

---

## C. Mechanism terms

### V–A coupling
Vector-minus-axial-vector coupling structure at electroweak interactions. Pure-V–A current operator $\bar{\psi}_L\gamma^\mu\psi_L = \frac{1}{2}\bar{\psi}\gamma^\mu(1-\gamma_5)\psi$ is the unique $\gamma_5$-ODD vector operator with non-vanishing matrix element between opposite-$\gamma_5$-parity matter-doublet (left-handed + right-handed Weyl spinors). Identified at THEO-CHIR-CONT-2 as the sector-specific continuum operator for the SF-2 W-bracelet sector. **First-use:** §1 + §4. **Related:** Michel parameter $\rho = 3/4$; massless helicity limit; SF-2 v1.0 §sec:YM_EFT_thm.

### Chiral-polarity-bias
SM-2 v1.0 §10 mechanism: the 600-cell's intrinsic chirality preferentially stabilizes Linear ZBW (LZBW) configurations on negative qCP centers via combined-$CP$-asymmetric effective free-energy $\Delta F^{qDP} = F[\text{LZBW},+] - F[\text{LZBW},-]$. Sector-specific continuum operator identified at THEO-CHIR-CONT-3 for the SM-2 qDP/eDP sector. **First-use:** §1 + §5. **Related:** Linear vs Orbital ZBW; combined-$CP$ involution; effective free-energy framework.

### K3-doublet
Capotauro v2.0 sector instantiation. K3 is a substrate object on the 600-cell with stabilizer $\Gamma^{K3} = D_{3d}$ at vertex-aligned Reading C; matter-doublet basis spans $\{|\Psi_-^{K3,(1)}\rangle, |\Psi_-^{K3,(2)}\rangle\}$; chirality operator $\hat{C}^{K3} \in A_2(D_{3d})$. Substrate-level matrix element $|M^{K3}| = \chi/6$ via THEO-CAP-1 (Composite Capotauro Wigner-Eckart Theorem). **First-use:** §3 + §3.4 (in cross-validation third-sector instantiation context). **Related:** Capotauro mechanism; mass-mixing sector.

### W-bracelet
Capotauro v2.0 sector instantiation. W-bracelet is the 6-vertex Petrie hexagon of the 600-cell with stabilizer $\Gamma^W = D_6$ at vertex-aligned Reading C; $\mathbb{Z}_2$ generator $\zeta^W = r^3$ (icosahedral-center inversion in 4D ambient with linear part $-I$ chirality-flipping); matter-doublet basis $\Psi_-^{W,(1)} \in E_2(D_6)$ + $\Psi_-^{W,(2)} \in E_1(D_6)$ spans 2D subspace of $E_2 \oplus E_1$; chirality operator $\hat{C}^W \in B_2(D_6)$. Substrate-level matrix element $|M^W| = \chi/6$ via THEO-SD-CHIR-1. **First-use:** §3 + §4. **Related:** electroweak V–A sector; SF-2 v1.0; Capotauro v2.0 §sec:w_bracelet.

### qDP/eDP
Quark Dipole / electron Dipole — Dipole Point configurations in SM-2 v1.0 §5 + §6 + Glossary. qDP = quark-flavor Dipole Point with charge ±1/3 or ±2/3 elementary charges; eDP = electron-flavor Dipole Point with charge ±1. The Linear-ZBW configuration of qDP at center $\pm$qCP is the substrate object characterized at $D_{5d}$ stabilizer; combined-$CP$ $\zeta^{qDP}$ as $\mathbb{Z}_2$ generator. Substrate-level matrix element $|M^{qDP}| = \chi/6$ via THEO-SD-CHIR-2. **First-use:** §3 + §5. **Related:** Linear vs Orbital ZBW; SM-2 §10 chiral-polarity-bias mechanism.

### Linear ZBW (LZBW) vs Orbital ZBW (OZBW)
Zitterbewegung configuration types per SM-2 v1.0 §5 + §6 + Glossary. Linear ZBW = qDP-on-qCP center with $d = 1$ first-shell vertex subset stabilizer $C_{5v}$ (chirality-asymmetric configuration); Orbital ZBW = eDP-on-eCP center with $d = 0$ full $I_h$ stabilizer (chirality-neutral reference configuration). Distinct ZBW-configuration types stabilize differently under combined-$CP$-asymmetric $\Delta F^{qDP}$ stabilization-energy operator. **First-use:** §5 + Glossary. **Related:** Capotauro mechanism; chiral-polarity-bias; SM-2 v1.0 §5 + §6.

### Capotauro Falsifier 6
Programme-level falsifier registered at Capotauro v2.0 §sec:falsifiers as anticipated-activation-at-v1.0-SHIP for the joint paper's sector legs; activated at v1.0 SHIPPED via three thresholds:
- **(A)** Michel $|\rho^{\text{obs}} - 3/4| > 3 \times 10^{-3}$ at PDG 2024 current precision $\sigma = 0.0010$
- **(B)** massless-helicity $|a_{\text{V+A}}|^2 > 3 \times 10^{-2}$ at LEP + LHC combined sensitivity
- **(C)** leptogenesis $|\Delta p_{LR}^{\text{obs}} - 0.0394| > 0.015$ at BAU back-derivation precision $\sigma \sim 0.005$ — **sharpest direct test of substrate-handle magnitude inheritance bypassing kinematic intermediaries**

Falsification cascade structure: deviation at any threshold (A)+(B)+(C) at $> 3\sigma$ significance cascades backward to question Lemma 4.1 (THEO-CHIR-CONT-1.1) / Theorem 4.2 (THEO-CHIR-CONT-1.2) / Theorem 15.3.1 (THEO-CHIR-CONT-1.3) / Definition 15.1.1 / Capotauro v2.0 substrate-handle identification. **First-use:** §1.4 + §4 + §9. **Related:** falsifiability inventory.

---

## D. Methodology terms

### Joint-paper format
Methodology adopted at Patch 0484 (v0.1 outline viability decision gate). Combines two sector-specific Layer 4 closures (SF-2 V–A coupling + SM-2 chiral-polarity-bias) into a single flagship paper with shared §3 sector-agnostic bridge work + sector-specific §4 + §5 + cross-sector unification §6. Saves estimated 4–11 sessions across §A + §B + §C trajectory vs Venue (b) fallback of two separate single-sector papers. Reviewer-validated as publication-grade methodology at chirality continuum v1.0 SHIP. **Related:** SF-4 v4.0 first cross-sector closure precedent (10 May 2026).

### Cross-sector convergence at observable level
Structural prediction of the joint-paper format: single primary empirical observable simultaneously validates two sector-specific Layer 4 closures of the same substrate-handle magnitude. At chirality continuum v1.0: leptogenesis CP-asymmetry $\Delta p_{LR} \approx 0.0394$ validates both §4 Layer 4 closure (THEO-CHIR-CONT-2 Threshold (C)) and §5 Layer 4 closure (THEO-CHIR-CONT-3 primary observable) at substrate-handle level $\chi/6$ via different physical channels (V–A coupling kinematics vs chiral-polarity-bias thermodynamic stabilization). Framed as falsifiable structural prediction at §6.5 of joint paper rather than emergent empirical coincidence. **Related:** structural-prediction framing; falsifiability inventory.

### Topological-projection argument
Proof technique introduced at Theorem 15.3.1 of joint paper §3 working sketch + §15.4 connection to standard QFT protection-of-topological-quantities principle. Establishes magnitude inheritance $|M^{\text{sub}}| = |M^{\text{eff}}|$ at leading order via topological-substrate-quantity character of $\chi$ + cage-shell factor $1/6$. Closed-form at leading order; generalizable to other substrate-handle inheritance closures. **First-use:** §3.3. **Related:** METH-CHIR-CONT-4; protection-of-topological-quantities principle.

### Four-condition test pattern
Programme-level theorem-registration discipline established at Patch 0397 (THEO-CAP-1 registration precedent). To register a programme-level theorem, the four conditions must all be satisfied: (i) rigorous proof chain; (ii) numerical verification at machine precision; (iii) empirical prediction validated against observation; (iv) honest scope-limitation framing identifying what the theorem does NOT do. THEO-CHIR-CONT-1 + -2 + -3 all pass the four-condition test. **Related:** conditional theorem closure; honest scope-limitation framing.

### Conditional theorem closure
Programme-level closure discipline established at SF-4 v4.2 + codified at `templates/conditional_closure_framework.md`. A theorem closes its claim **conditional on** specified foundational inputs (FIs). Promotion to unconditional closure requires deriving the FIs from CPP primitive axioms. THEO-CHIR-CONT-1 conditional on FI-CHIR-CONT-1 + FI-CHIR-CONT-2 + FI-CHIR-CONT-3 + FI-CHIR-CONT-9 + AXIM-1/2/3/4/7; THEO-CHIR-CONT-2 conditional on THEO-CHIR-CONT-1 + FI-CHIR-CONT-10/11/12; THEO-CHIR-CONT-3 conditional on THEO-CHIR-CONT-1 + FI-CHIR-CONT-13/14/15. **Related:** Layer 1 promotion; dynamical-substrate-law gate.

### Dynamical-substrate-law gate
External-reviewer-confirmed defining next programme gate identified at chirality continuum v1.0 SHIP. Q1$'$+Q1$'$.A Layer 3 promotion of $\hat{n}$ + $|\chi| = \varphi^{-3}$: derive substrate primitive 4D direction $\hat{n}$ and substrate chirality magnitude $|\chi|$ as unique values picked out by CPP primitive axioms AXIM-1 through AXIM-9 at substrate-physics scale via Layer 3 substrate-dynamics machinery. Closure would promote FI-CHIR-CONT-1 + FI-CHIR-CONT-2 from Layer 2 to Layer 1 status and contract the framework's foundational input stack by two. **First-use:** §1.4 + §8.1 + §9.3. **Related:** Layer 1 promotion; FI-CHIR-CONT-1; FI-CHIR-CONT-2.

### OPEN-SD-CHIR-PRIMITIVE umbrella
Programme-level open-problem umbrella registered at Patch 0422 in `research_frontier.md`. Covers cross-sector substrate-chirality-primitive unification work across five observable manifestations: (i) mass-mixing chirality; (ii) electroweak V–A; (iii) electromagnetic handedness; (iv) thermodynamic causal arrow; (v) cosmological-vacuum asymmetry. The chirality continuum joint paper closes manifestations (i) + (ii) at Layer 4 via THEO-CHIR-CONT-2 and (iii) at Layer 4 via THEO-CHIR-CONT-3. Manifestations (iv) + (v) remain at substrate-level closure under THEO-SD-CHIR-N convention pending Layer 4 promotion via THEO-CHIR-CONT-4 + -5 candidates as future-window work. **First-use:** §1. **Related:** Capotauro v2.0 §sec:umbrella_registration; future-window manifestations (iv) + (v).

---

## E. Inherited terms (defined elsewhere; appearing in this paper)

| Term | Defined in |
|---|---|
| Conscious Point (CP) | `master_glossary.md` |
| Dipole Point (DP) | `master_glossary.md` |
| Dipole Sea | `master_glossary.md` |
| Zitterbewegung (ZBW) | `master_glossary.md` + SM-2 v1.0 §5 + §6 + Glossary |
| 600-cell polytope | `master_glossary.md` |
| Wigner-Eckart theorem | standard quantum mechanics; cited per Cheng & Li Ch. 11 |
| Wilson-Fisher block-spin renormalization | standard QFT; cited per Wilson & Kogut 1974 |
| Schur orthogonality | standard finite-group representation theory |
| Composite Capotauro Wigner-Eckart Theorem | THEO-CAP-1 (Capotauro v1.0 + v2.0 paper) |
| Three-way cross-sector substrate unification | Capotauro v2.0 §sec:three_way_unification |
| Reading C / vertex-aligned interpretation | Capotauro v2.0 §sec:reading_c |
| Local-$I_h$-preservation theorem | Capotauro v2.0 §sec:local_ih_preservation (Finding C-W39) |
| Substrate-Locality Theorem | Capotauro v2.0 §sec:substrate_locality (Finding C-W40) |
| Composite matrix element factorization | Capotauro v2.0 §sec:composite_factorization (Finding C-W46) |
| Foundational Input (FI-X) | `templates/conditional_closure_framework.md` |
| Theorem-registry sub-prefix conventions | `theorem-registry.md` Patch 0434 + 0440 + 0487 + 0491 + 0495 |
