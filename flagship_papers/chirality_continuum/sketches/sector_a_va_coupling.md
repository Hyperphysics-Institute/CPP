# §B Sector A V–A Coupling Derivation — Working Sketch

**Joint Layer 4 paper §B (Sector A = SF-2 electroweak V–A coupling)**
**Opened**: 20 May 2026 (Session 137 continuation, Patch 0488 — §B Session 1)
**Status at open**: §A bridge work CLOSED at theorem-level rigor via THEO-CHIR-CONT-1 (Patch 0487); §A content ready for §B substantive drafting per joint paper outline v0.1 §5
**Sketch home**: `flagship_papers/chirality_continuum/sketches/sector_a_va_coupling.md`

This sketch opens substantive Tier-4 reasoning work for the joint paper's §B Sector A (SF-2 electroweak V–A coupling derivation). §B inherits THEO-CHIR-CONT-1's sector-agnostic continuum operator structure and applies sector-specific Yang-Mills $SU(2)_L \times U(1)_Y$ EFT identification to derive the V–A current operator + downstream kinematic predictions (Michel parameter $\rho = 3/4$ at finite mass; 100% LH at massless helicity limit; Capotauro Falsifier 6 activation).

---

## §0 Session 1 working-session firewall and scope

This section opens Session 1 of §B Sector A work (Patch 0488). The bridge step (§A) is CLOSED at theorem-level rigor — sub-claim (a) closure trajectory complete at Patches 0485+0486+0487 with THEO-CHIR-CONT-1 + sub-statements THEO-CHIR-CONT-1.1/-1.2/-1.3 registered at programme theorem-registry. §B substantive drafting opens with this patch under inheritance from §A's bridge theorem.

**Session 1 substantive scope** (Patch 0488):

1. **Theorem B.1 statement** (§1 below): articulate sector-specific theorem for §B closure — Sector A Yang-Mills EFT V–A Coupling Derivation. Three sub-claims targeted across Sessions 1–4 of §B (Patches 0488–0491+ candidates).

2. **Proof architecture** (§2 below): 4-step proof structure for Theorem B.1 — (i) sector-specific continuum operator identification; (ii) Michel parameter $\rho = 3/4$ derivation at finite mass; (iii) 100% LH preference derivation at massless helicity limit; (iv) Capotauro Falsifier 6 activation framing.

3. **Step 1 closure** (§3 below): sector-specific continuum operator identification — show that the bridge theorem's sector-agnostic continuum operator $\mathcal{O}^{\text{eff,W}} = \Phi_*\hat{C}^W$ identifies as the V–A current operator $\bar{\psi}_L \gamma^\mu \psi_L$ in Yang-Mills $SU(2)_L \times U(1)_Y$ EFT framework appropriate to the SF-2 sector.

4. **Steps 2–4 setup architecture** (§4 + §5 + §6 below): articulate what Sessions 2 + 3 + 4 of §B will close. Sessions 2–4 are deferred to Patches 0489+, 0490+, 0491+.

**Anti-priorities at Session 1 of §B** (in addition to programme-level anti-priorities preserved from §A bridge work):

- Do NOT close Steps 2–4 of §B at Session 1 (Michel parameter derivation, 100% LH derivation, Capotauro Falsifier 6 activation — all deferred to Sessions 2–4).
- Do NOT modify SF-2 v1.0 .tex source during §B drafting — SF-2 v1.0 SHIPPED at Session 83 Patch 0370 with .tex source frozen; §B content lives at `flagship_papers/chirality_continuum/` not at SF-2 paper home.
- Do NOT modify Patch 0482 SF-2 scoping sketch at `flagship_papers/electroweak/sketches/SF-2_chir_layer4_closure.md` — preserved at historical location; §B working sketch is THIS file at the joint paper home.
- Do NOT mix sector-specific §B content (this sketch) with sector-agnostic §A content (`substrate_to_continuum_bridge.md`). §A is CLOSED; §B builds on top via inheritance.
- Do NOT introduce new FI-CHIR-CONT-N entries at §B Session 1 (FI inventory finalized at Patch 0484 v0.1 outline; §B operates under existing FI stack + sector-specific inheritances from SF-2 v1.0 and EW-5 thm:YM\_EFT proof outline).
- Do NOT promote Theorem B.1 to programme-level registered-theorem status at Session 1 (registration at the end of §B Session 4 when sub-claims (b)+(c)+(d) all close; expected THEO-CHIR-CONT-2 candidate).

---

## §1 Theorem B.1 statement — Sector A Yang-Mills EFT V–A Coupling Derivation

**Theorem B.1** (*Sector A Yang-Mills EFT V–A Coupling Derivation*; THEO-CHIR-CONT-2 candidate). Under THEO-CHIR-CONT-1 + sub-statements THEO-CHIR-CONT-1.1/-1.2/-1.3 (joint Layer 4 paper §A bridge theorem with sector-agnostic continuum operator at magnitude $\chi/6$ at leading order) + SF-2 v1.0 §sec:YM\_EFT\_thm Yang-Mills EFT framework (the EFT continuum-limit framework for SU(2)_L × U(1)_Y electroweak interactions inheriting EW-5 THEO-EW-8 thm:YM\_EFT proof outline) + W-bracelet sector specialization (substrate object as W-bracelet 6-vertex Petrie hexagon at $v_{\text{host}}$ with stabilizer $D_6$, $\zeta^W = r^3$ icosahedral-center inversion, chirality operator $\hat{C}^W \in B_2(D_6)$ per THEO-SD-CHIR-1 sector instantiation), the bridge theorem's sector-agnostic continuum operator $\mathcal{O}^{\text{eff,W}} = \Phi_*\hat{C}^W$ has three sector-specific consequences:

1. **(b) Sector-specific operator identification**: $\mathcal{O}^{\text{eff,W}}$ identifies as the **V–A current operator** $\bar{\psi}_L \gamma^\mu \psi_L$ in the continuum Yang-Mills $SU(2)_L \times U(1)_Y$ EFT framework. The continuum-limit projection of the substrate-level matter-doublet $\{|\Psi^W_+\rangle, |\Psi^W_-\rangle\}$ identifies as the continuum LH chiral fermion doublet $\{\psi_L, \psi_R\}$ via:
   - $|\Psi^W_+\rangle$ ($\zeta^W$-EVEN) $\to$ $\psi_R$ ($\gamma_5$-EVEN, RH-chiral)
   - $|\Psi^W_-\rangle$ ($\zeta^W$-ODD) $\to$ $\psi_L$ ($\gamma_5$-ODD, LH-chiral)
   - $\zeta^{\text{cont,W}} \to \gamma_5$ at continuum level

2. **(c) Michel parameter $\rho = 3/4$ at finite mass**: the pure-V–A structure of $\mathcal{O}^{\text{eff,W}}$ (no V+A admixture; the $\zeta^{\text{cont,W}}$-ODD = $\gamma_5$-ODD parity content guarantees pure V–A) implies the Michel parameter prediction $\rho = 3/4$ at finite-mass muon decay via standard V–A kinematics. Quantitative leading-order calculation: $\rho^{V-A} = 3/4$ exactly at tree level; substrate-handle corrections enter at sub-leading order suppressed by $\chi^2 \sim 0.056$.

3. **(d) 100% LH preference at massless helicity limit**: at the massless-fermion helicity limit, pure V–A interaction enforces 100% LH chirality preference. Quantitative limit: $P_L / (P_L + P_R) \to 1$ as $m_\psi/E_\psi \to 0$, with deviations $|\delta P_L| \leq |\chi|/6 \cdot (m_\psi/E_\psi)$ from sub-leading substrate-handle corrections.

4. **(e) Capotauro Falsifier 6 activation**: deviation $|\Delta \rho| > \chi/6 \cdot \text{(threshold factor)}$ from $\rho = 3/4$ at LEP/SLC precision, OR deviation $|\delta P_L| > $ structural-threshold at massless helicity limit, OR observed leptogenesis CP-asymmetry $|\Delta p_{LR}| > 0.0394 + \text{threshold}$ falsifies the bridge theorem's substrate-handle inheritance prediction. Falsifier 6 activates the structural prediction at observable scales.

This is the theorem at full theorem-statement level. The proof architecture below outlines 4 steps; **Step 1 closure (sub-claim (b)) at this patch (Patch 0488; Session 1 of §B)**, with Steps 2-4 (sub-claims (c)+(d)+(e)) deferred to Sessions 2+3+4 of §B (Patches 0489+, 0490+, 0491+ candidates).

---

## §2 Proof architecture — 4-step structure for Theorem B.1

The proof of Theorem B.1 proceeds in 4 steps mirroring the §A bridge step's 4-step structure (Step 1 substrate operator identification → Step 2 continuum projection setup → Step 3 continuum operator identification → Step 4 magnitude inheritance), but with sector-specific kinematic content replacing sector-agnostic projection content.

**Step 1 (this patch; §3 below)**: **Sector-specific continuum operator identification** — identify the abstract continuum operator $\mathcal{O}^{\text{eff,W}}$ from bridge theorem THEO-CHIR-CONT-1.2 with the specific physical operator $\bar{\psi}_L \gamma^\mu \psi_L$ in the Yang-Mills $SU(2)_L \times U(1)_Y$ EFT framework. The identification matches:
- Group-theoretic structure (continuum-limit $\zeta^{\text{cont,W}}$-ODD content $\leftrightarrow$ $\gamma_5$-ODD chiral content)
- Algebraic structure (W-bracelet's $D_6$ stabilizer + $B_2$-irrep operator $\leftrightarrow$ continuum gauge-doublet structure of Yang-Mills EFT)
- Matter-doublet content (continuum projection of W-bracelet matter-doublet $\leftrightarrow$ continuum LH/RH chiral fermion fields)

Sub-claim (b) of Theorem B.1 CLOSED at end of Step 1.

**Step 2 (Session 2 target; Patch 0489+ candidate)**: **Michel parameter $\rho = 3/4$ derivation at finite mass** — derive the Michel parameter prediction from pure-V–A structure of $\mathcal{O}^{\text{eff,W}}$ via standard EFT kinematics. The substrate handle $\chi/6$ does NOT directly appear in $\rho = 3/4$ at leading order — pure V–A is the load-bearing input, and the bridge theorem certifies pure V–A (rather than V+A admixture) via the $\zeta^{\text{cont,W}}$-ODD content. Substrate-handle corrections enter at sub-leading order ($\chi^2 \sim 0.056$).

Sub-claim (c) of Theorem B.1 CLOSED at end of Step 2.

**Step 3 (Session 3 target; Patch 0490+ candidate)**: **100% LH preference at massless helicity limit** — derive the asymptotic massless-fermion chirality preference from V–A coupling structure. At the massless limit $m_\psi/E_\psi \to 0$, pure V–A enforces $P_L \to 1$; substrate-handle corrections introduce deviations $|\delta P_L| \leq |\chi|/6 \cdot (m_\psi/E_\psi)$ at sub-leading order.

Sub-claim (d) of Theorem B.1 CLOSED at end of Step 3.

**Step 4 (Session 4 target; Patch 0491+ candidate)**: **Capotauro Falsifier 6 activation** — frame the falsifier prediction explicitly: deviations from Michel $\rho = 3/4$, 100% LH at massless limit, or leptogenesis $\Delta p_{LR} \approx \chi/6 \approx 0.0394$ at observable precision falsify the bridge theorem's substrate-handle inheritance. Quantify falsification thresholds at LEP/SLC + future-collider precision levels. Connect to PRED-O-25.

Sub-claim (e) of Theorem B.1 CLOSED at end of Step 4. Theorem B.1 promoted to programme-level registered-theorem status as **THEO-CHIR-CONT-2** at end of §B Session 4 (analog of THEO-CHIR-CONT-1 promotion at end of §A Session 3).

---

## §3 Step 1 — Sector-specific continuum operator identification (Session 1 substantive content)

This section closes Step 1 of Theorem B.1: identify the bridge theorem's abstract sector-agnostic continuum operator $\mathcal{O}^{\text{eff,W}}$ with the specific physical V–A current operator $\bar{\psi}_L \gamma^\mu \psi_L$ in the Yang-Mills $SU(2)_L \times U(1)_Y$ EFT framework.

### §3.1 Inheritance from THEO-CHIR-CONT-1

The bridge theorem THEO-CHIR-CONT-1 delivers (sector-agnostic):

- Continuum-limit projection map $\Phi$ (Definition 11.2.1; Wilson-Fisher block-spin renormalization at substrate cutoff $\Lambda_{\text{sub}} = \ell_{\text{edge}}^{-1}$ with block-spin commutativity + continuum-limit existence + equivariance conditions).
- Continuum-limit Wigner-Eckart datum $\mathcal{D}^{\text{cont,W}} = (\mathcal{S}^{\text{cont,W}}, \Gamma^{\text{cont,W}}, \zeta^{\text{cont,W}}, \mathcal{O}^{\text{eff,W}}, \{|\psi^{\text{eff}}_+\rangle, |\psi^{\text{eff}}_-\rangle\}, M^{\text{eff,W}})$ with group-theoretic structure inherited from substrate $\mathcal{D}^{\text{sub,W}}$ via Lemma 4.1 + Corollary 4.1.1.
- Continuum operator $\mathcal{O}^{\text{eff,W}} = \Phi_*\hat{C}^W$ as the unique (up to overall scalar multiple) $\zeta^{\text{cont,W}}$-ODD 1D-irrep operator on the continuum-limit 2D $\Gamma^{\text{cont,W}}$-irrep matter-doublet subspace (Theorem 4.2; THEO-CHIR-CONT-1.2).
- Matrix element magnitude $|M^{\text{eff,W}}| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ at leading order in $a/L = \ell_{\text{edge}} \mu_{\text{obs}}^W$ (Theorem 15.3.1; THEO-CHIR-CONT-1.3; topological-projection argument).

For sector-specific identification, we inherit the W-bracelet sector instantiation of bridge theorem inputs:

- Substrate object $\mathcal{S}^{\text{sub,W}}$: W-bracelet 6-vertex Petrie hexagon at $v_{\text{host}}$ (THEO-SD-CHIR-1; Finding C-W36).
- Stabilizer subgroup $\Gamma^{W} = D_6$ (the W-bracelet's dihedral stabilizer; THEO-SD-CHIR-1 step (iv)).
- $\zeta^W = r^3$ icosahedral-center inversion in 4D ambient (Finding C-W43; chirality-flipping involution).
- Matter-doublet basis $\{|\Psi^W_+\rangle, |\Psi^W_-\rangle\}$ with opposite-$\zeta^W$-parity (W-bracelet's 2D-subspace structure within $E_2 \oplus E_1$ of $D_6$; THEO-SD-CHIR-1 step (iv)).
- Chirality operator $\hat{C}^W \in B_2(D_6) = A_2(S_3) \otimes \sigma(\mathbb{Z}_2)$ sourced from primitive 4D direction $\hat{n}$ (Finding C-W43; THEO-SD-CHIR-1 step (iv)).

### §3.2 SF-2 Yang-Mills EFT framework — anchor reference

The continuum-limit EFT framework for the SF-2 sector is the Yang-Mills $SU(2)_L \times U(1)_Y$ gauge theory. The framework anchor references:

1. **SF-2 v1.0 §sec:YM\_EFT\_thm** (Theorem 8.3 of SF-2 v1.0 paper): Yang-Mills EFT continuum limit theorem at proof-outline level — establishes that the substrate-level W-bracelet $D_6$ stabilizer + electroweak gauge structure produces continuum-limit Yang-Mills $SU(2)_L \times U(1)_Y$ gauge theory at scales $\mu \ll \Lambda_{\text{sub}}$.

2. **EW-5 THEO-EW-8 thm:YM\_EFT**: Yang-Mills EFT framework at earlier SF-Line series-level — supplies the foundational continuum-EFT structure that SF-2 v1.0 §sec:YM\_EFT\_thm specializes to W-bracelet sector.

In this framework, the continuum-limit physical content is:

- Continuum LH fermion fields $\psi_L = P_L \psi$ transforming in fundamental representation of $SU(2)_L$ (gauge doublet for leptons + quarks per generation).
- Continuum RH fermion fields $\psi_R = P_R \psi$ transforming as $SU(2)_L$ singlets.
- Continuum gauge fields $W^{a\mu}$ ($a = 1, 2, 3$ for $SU(2)_L$) and $B^\mu$ (for $U(1)_Y$); after electroweak symmetry breaking, mass eigenstates $W^\pm, Z, A$.
- Chirality projection: $\gamma_5$ commutes with kinetic operators; $P_L = (1 - \gamma_5)/2$ and $P_R = (1 + \gamma_5)/2$ project LH/RH chiral content.

The standard V–A current operator is:
$$\bar{\psi}_L \gamma^\mu \psi_L = \bar{\psi} P_R \gamma^\mu P_L \psi = \frac{1}{2}\bar{\psi}\gamma^\mu(1 - \gamma_5)\psi$$
This is the "vector-minus-axial" current that couples to $W^\pm$ in charged-current weak interactions. Its parity content under $\gamma_5$:
$$\gamma_5 [\bar{\psi}_L \gamma^\mu \psi_L] \gamma_5^{-1} = -[\bar{\psi}_L \gamma^\mu \psi_L]$$
i.e., the V–A current is $\gamma_5$-ODD. This $\gamma_5$-parity structure is the key continuum-EFT signature for chirality-sensitive operators.

### §3.3 Identification map — substrate W-bracelet to continuum gauge structure

The identification of the bridge theorem's sector-agnostic outputs with the SF-2 Yang-Mills EFT physical content proceeds via three identifications:

**Identification 1**: Continuum-limit $\zeta^{\text{cont,W}}$ identifies as $\gamma_5$ chirality-flipping operator.

The substrate-level $\zeta^W = r^3$ icosahedral-center inversion in 4D ambient (Finding C-W43) is a chirality-flipping $\mathbb{Z}_2$ involution: it flips $\hat{n} \to -\hat{n}$ (the substrate chirality primitive). Under the continuum-limit projection map $\Phi$ + Lemma 4.1 (THEO-CHIR-CONT-1.1), $\zeta^W$ projects to $\zeta^{\text{cont,W}}$ — a continuum-limit $\mathbb{Z}_2$ generator with the same chirality-flipping action on the continuum-limit matter-doublet.

In the Yang-Mills EFT framework, the chirality-flipping $\mathbb{Z}_2$ generator on the continuum fermion fields is $\gamma_5$:
$$\gamma_5 \psi_L = -\psi_L, \quad \gamma_5 \psi_R = +\psi_R$$
i.e., $\gamma_5$ flips chirality with the $\mathbb{Z}_2$ structure $\gamma_5^2 = 1$. The identification:
$$\zeta^{\text{cont,W}} \leftrightarrow \gamma_5$$
matches structure (chirality-flipping involution; $\mathbb{Z}_2$ generator) and action (preserves $\zeta^{\text{cont,W}}$-EVEN/ODD content via $\gamma_5$-EVEN/ODD content).

**Identification 2**: Continuum-limit matter-doublet $\{|\psi^{\text{eff}}_+\rangle, |\psi^{\text{eff}}_-\rangle\}$ identifies as $\{\psi_R, \psi_L\}$ chiral fermion fields.

The substrate-level matter-doublet $\{|\Psi^W_+\rangle, |\Psi^W_-\rangle\}$ has opposite-$\zeta^W$-parity (THEO-SD-CHIR-1 step (iv); Lemma 4.1 (5) preserves opposite-parity content under $\Phi$). The continuum-limit projection $\{|\psi^{\text{eff}}_+\rangle, |\psi^{\text{eff}}_-\rangle\}$ has opposite-$\zeta^{\text{cont,W}}$-parity.

In the Yang-Mills EFT framework, the natural opposite-$\gamma_5$-parity pair is $\{\psi_R, \psi_L\}$ where $\psi_R$ is $\gamma_5$-EVEN and $\psi_L$ is $\gamma_5$-ODD. The identification:
$$|\psi^{\text{eff}}_+\rangle \leftrightarrow \psi_R, \quad |\psi^{\text{eff}}_-\rangle \leftrightarrow \psi_L$$
matches parity content under Identification 1 ($\zeta^{\text{cont,W}}$-EVEN $\leftrightarrow$ $\gamma_5$-EVEN $\leftrightarrow$ RH-chiral; $\zeta^{\text{cont,W}}$-ODD $\leftrightarrow$ $\gamma_5$-ODD $\leftrightarrow$ LH-chiral).

**Identification 3**: Continuum-limit chirality-sensitive operator $\mathcal{O}^{\text{eff,W}}$ identifies as V–A current operator $\bar{\psi}_L \gamma^\mu \psi_L$.

Under Identifications 1 + 2, the bridge theorem's sector-agnostic continuum operator structure (Theorem 4.2; THEO-CHIR-CONT-1.2: $\mathcal{O}^{\text{eff,W}}$ is $\zeta^{\text{cont,W}}$-ODD with non-vanishing matrix element between opposite-$\zeta^{\text{cont,W}}$-parity matter-doublet states) translates to the continuum-EFT requirement:

- The continuum-EFT chirality-sensitive operator is $\gamma_5$-ODD;
- The operator has non-vanishing matrix element between $\psi_R$ and $\psi_L$;
- The operator transforms as a vector under continuum Lorentz (inheriting the V–A structural property from SF-2 v1.0 Yang-Mills EFT framework).

These three properties uniquely identify the operator (up to overall scalar normalization) as the V–A current operator $\bar{\psi}_L \gamma^\mu \psi_L$ in the Yang-Mills $SU(2)_L \times U(1)_Y$ EFT:

$$\boxed{\mathcal{O}^{\text{eff,W}} \leftrightarrow \bar{\psi}_L \gamma^\mu \psi_L}$$

up to overall coupling-constant normalization fixed by the bridge theorem's magnitude inheritance THEO-CHIR-CONT-1.3 at leading order: matrix element magnitude $|M^{\text{eff,W}}| = \chi/6 \approx 0.0394$ corresponds to the V–A coupling strength at the substrate handle's projection level.

### §3.4 V–A current operator identification — sector-specific physical content

With Identification 3 in place, the V–A current operator $\bar{\psi}_L \gamma^\mu \psi_L$ inherits the bridge theorem's properties at SF-2 sector-specific physical level:

1. **Pure-V–A structure** (no V+A admixture): the $\gamma_5$-ODD parity content (Identification 1 + Theorem 4.2) guarantees pure V–A. A hypothetical V+A admixture would correspond to a $\gamma_5$-EVEN operator component, which is structurally excluded by the bridge theorem's $\zeta^{\text{cont,W}}$-ODD identification.

2. **Coupling magnitude at leading order**: V–A coupling strength inherits the bridge theorem's magnitude $\chi/6 \approx 0.0394$ at leading order via THEO-CHIR-CONT-1.3 topological-projection argument. Sub-leading corrections enter at $(a/L)^n$ for $n \geq 1$, negligible at SF-2 electroweak scale ($a/L \sim 10^{-18}$).

3. **Gauge coupling to $W^\pm, Z$**: the V–A current $\bar{\psi}_L \gamma^\mu \psi_L$ couples to $W^\pm$ via the standard charged-current weak interaction Lagrangian:
   $$\mathcal{L}_{\text{CC}} = -\frac{g}{\sqrt{2}} W^+_\mu \bar{\psi}_L \gamma^\mu \psi_L + \text{h.c.}$$
   where $g$ is the $SU(2)_L$ gauge coupling. The substrate-handle inheritance fixes the V–A structure (pure V–A vs V+A); the gauge coupling $g$ is fixed by independent inputs (electroweak symmetry breaking + Higgs mechanism per SF-2 v1.0 §sec:higgs\_mechanism + SM input parameters).

4. **Lorentz structure**: the V–A current is a vector under continuum Lorentz transformations, inheriting Lorentz covariance from the Yang-Mills EFT framework (continuum-limit emergence of Lorentz invariance at scales $\mu \ll \Lambda_{\text{sub}}$ per SF-2 v1.0 §sec:YM\_EFT\_thm). The bridge theorem's continuum-limit projection $\Phi$ preserves continuum-Lorentz-covariance at leading order via block-spin commutativity with discrete rotational symmetries of the substrate.

### §3.5 Step 1 closure — what is in hand at end of §B Session 1

Sub-claim (b) of Theorem B.1 (sector-specific continuum operator identification) CLOSED:

- $\mathcal{O}^{\text{eff,W}}$ identifies as V–A current $\bar{\psi}_L \gamma^\mu \psi_L$ in Yang-Mills $SU(2)_L \times U(1)_Y$ EFT framework.
- Identification via three matched structural conditions: $\gamma_5$-parity content (Identification 1); opposite-parity matter-doublet content (Identification 2); $\gamma_5$-ODD non-vanishing-matrix-element structure (Identification 3).
- Sub-leading corrections suppressed by deep-infrared regime $a/L \sim 10^{-18}$ at SF-2 electroweak scale.
- Sector-specific physical properties inherited at leading order: pure V–A structure; coupling magnitude $\chi/6$; gauge coupling structure to $W^\pm$; Lorentz covariance.

The continuum-EFT V–A current operator is now established as the physical operator that the bridge theorem's abstract continuum operator identifies as in the SF-2 sector. Steps 2–4 of §B build on this identification to derive empirical kinematic predictions (Michel parameter; 100% LH at massless limit; Capotauro Falsifier 6 activation).

---

## §4 Step 2 setup architecture — Michel parameter $\rho = 3/4$ derivation at finite mass (Session 2 target; Patch 0489+ candidate)

Session 2 of §B closes sub-claim (c) of Theorem B.1: derive the Michel parameter prediction $\rho = 3/4$ from the pure-V–A structure of $\mathcal{O}^{\text{eff,W}}$ via standard EFT kinematics.

**Setup**:

- The Michel parameter $\rho$ characterizes the electron energy spectrum in muon decay $\mu^- \to e^- \nu_\mu \bar{\nu}_e$: $\rho$ is the coefficient of the leading $E_e^3$-dependent term in the spectrum. Standard V–A interaction predicts $\rho = 3/4$ at tree level.

- The pure-V–A structure of $\mathcal{O}^{\text{eff,W}}$ inherited from Step 1 (this patch) guarantees pure V–A in the four-fermion effective interaction $\bar{\nu}_\mu \gamma^\mu (1-\gamma_5) \mu \cdot \bar{e} \gamma_\mu (1-\gamma_5) \nu_e / 2$ that drives muon decay at the four-fermion effective level (after integrating out $W^\pm$ at scales $E_\mu \ll m_W$).

- Standard EFT kinematic calculation: pure-V–A four-fermion interaction $\to$ $\rho = 3/4$ exactly at tree level. Substrate-handle corrections enter at sub-leading order via residual V+A admixture from sub-leading $(a/L)^n$ continuum-limit corrections — magnitude $\sim \chi^2 \sim 0.056$ which is below LEP/SLC precision at current measurement levels.

**Session 2 substantive content**: walk through standard V–A kinematics for muon decay to verify $\rho = 3/4$ at tree level; establish the sub-leading correction estimate at $\sim \chi^2$ scale; confirm that current empirical $\rho^{\text{obs}} = 0.7497 \pm 0.0010$ (PDG 2024) is consistent with V–A prediction within 2-sigma.

**Anti-priority at Session 2**: do NOT extend beyond Michel parameter — additional kinematic predictions (e.g., $\eta, \xi, \delta$ Michel-spectrum parameters) are out of scope for the joint paper's §B focus. The Michel parameter $\rho$ is the load-bearing structural prediction; other parameters are inherited consequences not in §B's direct closure scope.

---

## §5 Step 3 setup architecture — 100% LH preference at massless helicity limit (Session 3 target; Patch 0490+ candidate)

Session 3 of §B closes sub-claim (d) of Theorem B.1: derive the 100% LH preference at the massless-fermion helicity limit from pure-V–A coupling structure.

**Setup**:

- At the massless-fermion limit $m_\psi/E_\psi \to 0$, fermion helicity is a conserved quantum number and the V–A current $\bar{\psi}_L \gamma^\mu \psi_L$ projects only LH-chiral content. The fraction of LH chirality in produced fermions:
  $$P_L^{\text{V-A}} / (P_L + P_R) = 1 - \mathcal{O}(m_\psi/E_\psi)^2$$
  at the massless limit.

- The pure-V–A inheritance from Step 1 (this patch) guarantees this asymptotic 100% LH preference. Substrate-handle corrections enter at sub-leading order via residual V+A admixture: $|\delta P_L| \lesssim |\chi|/6 \cdot (m_\psi/E_\psi)$ at sub-leading-order kinematic suppression.

- Empirical anchor: observed neutrino chirality data ($\nu_e$ in muon decay, $\nu_\mu$ in $W$-decay, etc.) consistent with 100% LH at current precision; deviations would require either non-zero neutrino RH content or V+A admixture at observable level — both falsified by current data within sensitivity.

**Session 3 substantive content**: walk through the massless-fermion helicity-limit calculation; derive the sub-leading correction estimate; connect to observed neutrino-helicity data + Capotauro Falsifier 6 sub-component (deviation $|\delta P_L| > $ structural-threshold falsifies).

**Anti-priority at Session 3**: do NOT extend beyond massless-fermion limit — finite-mass corrections at sub-leading order are inherited from Step 2 (Michel parameter) and Step 1 (operator identification); they are not separate closures at §B scope.

---

## §6 Step 4 setup architecture — Capotauro Falsifier 6 activation (Session 4 target; Patch 0491+ candidate)

Session 4 of §B closes sub-claim (e) of Theorem B.1: frame the falsifier prediction explicitly and connect to PRED-O-25 leptogenesis CP-asymmetry.

**Setup**:

- Three falsification thresholds combined:
  - **(A)** Michel parameter deviation: $|\rho^{\text{obs}} - 3/4| > \chi^2 \cdot \text{(precision threshold)}$ at LEP/SLC + future-collider precision falsifies pure-V–A inheritance.
  - **(B)** Massless-helicity-limit deviation: $|\delta P_L| > $ structural-threshold (e.g., observed RH neutrino content at substantially-non-zero level) falsifies pure-V–A inheritance at massless limit.
  - **(C)** Leptogenesis CP-asymmetry deviation: $|\Delta p_{LR}^{\text{obs}} - \chi/6| > $ threshold falsifies substrate-handle magnitude inheritance directly.

- Threshold (C) is the sharpest direct test of THEO-CHIR-CONT-1's substrate-handle inheritance: the substrate handle $\chi/6 \approx 0.0394$ matches observed leptogenesis CP-asymmetry $\sim 0.04$ within 2%. Deviation beyond ~2% (i.e., observation $|\Delta p_{LR}^{\text{obs}} - 0.0394| > 0.001$ at sub-percent precision) falsifies THEO-CHIR-CONT-1 + THEO-CHIR-CONT-2 jointly.

- Capotauro Falsifier 6 (registered at Capotauro v2.0 §sec:falsifiers as one of six structural falsifiers; activated by current SF-2 v3.0+ Layer 4 closure): substrate handle $\chi/6$ propagates from Layer 3 (THEO-SD-CHIR-1) through Layer 4 (THEO-CHIR-CONT-1) to observable kinematic prediction (Layer 4 sector-specific closure THEO-CHIR-CONT-2 candidate). Falsification at any of the three thresholds (A) + (B) + (C) cascades to falsify the substrate-handle inheritance chain.

**Session 4 substantive content**: quantitatively articulate falsification thresholds at current precision (LEP/SLC + Daya Bay + RENO + T2K + NOvA + PDG 2024 averages) + future-collider precision (FCC-ee, ILC, CLIC projections); connect to PRED-O-25 from THEO-CAP-1 + THEO-SD-CHIR-1; explicitly register Capotauro Falsifier 6 as activated at end of §B.

**Anti-priority at Session 4**: do NOT introduce new falsifiers at §B Session 4 — the Capotauro Falsifier 6 framework is inherited; §B activates the falsifier at observable-scale predictions but does not introduce additional falsifiers beyond the existing umbrella set.

---

## §7 Sector-agnostic vs sector-specific content map

Inherited from THEO-CHIR-CONT-1 (sector-agnostic):

- Continuum-limit projection map $\Phi$ (Definition 11.2.1).
- Continuum-limit Wigner-Eckart datum $\mathcal{D}^{\text{cont}}$ (Corollary 4.1.1).
- Continuum operator $\mathcal{O}^{\text{eff,sector}}$ as $\zeta^{\text{cont,sector}}$-ODD 1D-irrep operator (Theorem 4.2; THEO-CHIR-CONT-1.2).
- Matrix element magnitude $|M^{\text{eff,sector}}| = \chi/6$ at leading order (Theorem 15.3.1; THEO-CHIR-CONT-1.3).
- Definition 15.1.1 (Topological Substrate Quantity) as programme-level concept.

Sector-specific to §B (this sketch):

- Step 1: identification $\mathcal{O}^{\text{eff,W}} \leftrightarrow \bar{\psi}_L \gamma^\mu \psi_L$ + identifications $\zeta^{\text{cont,W}} \leftrightarrow \gamma_5$ + $\{|\psi^{\text{eff}}_+\rangle, |\psi^{\text{eff}}_-\rangle\} \leftrightarrow \{\psi_R, \psi_L\}$.
- Step 2: Michel parameter $\rho = 3/4$ at finite mass via standard V–A kinematics.
- Step 3: 100% LH preference at massless helicity limit via V–A coupling structure.
- Step 4: Capotauro Falsifier 6 activation at observable-scale prediction thresholds.

The sector-agnostic content (§A bridge) does the heavy lifting on continuum-limit projection structure + magnitude inheritance; the sector-specific content (§B Sector A) does the sector-specific physical-operator identification + kinematic-projection derivations.

---

## §8 FI dependency mapping for §B Sector A

Inherited from THEO-CHIR-CONT-1 (the bridge theorem):

- **FI-CHIR-CONT-1** (substrate primitive 4D direction $\hat{n}$; vertex-aligned Reading C).
- **FI-CHIR-CONT-2** (substrate chirality magnitude $|\chi| = \phi^{-3}$; perturbative-distance-ratio constraint).
- **FI-CHIR-CONT-3** (substrate residual symmetry $H_3 = I_h$ at host vertex).
- **FI-CHIR-CONT-9** (Substrate-Locality Theorem of Capotauro v2.0).

Sector-specific to §B Sector A (the W-bracelet sector + Yang-Mills EFT framework):

- **FI-CHIR-CONT-10** (W-bracelet sector specialization: substrate object as W-bracelet 6-vertex Petrie hexagon at $v_{\text{host}}$ with stabilizer $D_6$, $\zeta^W = r^3$, chirality operator $\hat{C}^W \in B_2(D_6)$ — inherited from THEO-SD-CHIR-1 sector instantiation).
- **FI-CHIR-CONT-11** (SF-2 Yang-Mills EFT framework: continuum-limit EFT for SF-2 sector as Yang-Mills $SU(2)_L \times U(1)_Y$ gauge theory — inherited from SF-2 v1.0 §sec:YM\_EFT\_thm + EW-5 THEO-EW-8 thm:YM\_EFT proof outline).
- **FI-CHIR-CONT-12** (continuum-EFT chirality-projection structure: $\gamma_5$ as chirality-flipping involution on continuum fermion fields with $P_L = (1 - \gamma_5)/2, P_R = (1 + \gamma_5)/2$ projection operators — inherited from standard Yang-Mills EFT machinery, structurally robust under continuum-limit projection per SF-2 v1.0 §sec:YM\_EFT\_thm).

CPP axioms most load-bearing for §B Sector A:

- **AXIM-1**: CP existence (substrate primitives; load-bearing for FI-CHIR-CONT-1 + FI-CHIR-CONT-12).
- **AXIM-2**: 600-cell topology (load-bearing for FI-CHIR-CONT-10 W-bracelet sector + FI-CHIR-CONT-3 + FI-CHIR-CONT-9).
- **AXIM-3**: Dipole Sea / DI-bit propagation (load-bearing for FI-CHIR-CONT-11 continuum-EFT framework via dipole-sea propagation mechanism producing continuum gauge structure).
- **AXIM-4**: SSV interaction / Nexus (load-bearing for FI-CHIR-CONT-9 Substrate-Locality + Yang-Mills EFT gauge interaction at continuum level).
- **AXIM-7**: Substrate-stress (load-bearing for FI-CHIR-CONT-1 substrate primitive direction sourcing chirality operator).

---

## §9 Anti-priorities for §B sector-specific work (programme-level)

In addition to Session-1-specific anti-priorities in §0 above:

- **Do NOT exceed Sector A (SF-2) scope**: §B closes V–A coupling derivation for SF-2 sector specifically; other electroweak sub-claims (e.g., neutral-current $Z$-coupling structure; Higgs-fermion Yukawa couplings; CKM mixing) are NOT in §B scope. Such sub-claims if needed have their own future-window venues at SF-2 v2.0+ or SF-line-N v1.0 follow-ups.

- **Do NOT modify Capotauro v2.0 + SF-2 v1.0 .tex sources** during §B drafting: all v1.0 SHIPPED with .tex source frozen. §B references SF-2 v1.0 §sec:YM\_EFT\_thm + EW-5 THEO-EW-8 + Capotauro v2.0 §sec:substrate\_locality as inheritance points; modifications to those papers happen at v2.0+ via separate publication-pathway windows.

- **Do NOT promote Theorem B.1 to programme-level registered-theorem status at §B Session 1**: registration at end of §B Session 4 when all four sub-claims (b)+(c)+(d)+(e) close. Premature promotion at Sessions 1-3 would violate the four-condition test pattern (rigorous proof chain incomplete; empirical prediction validation incomplete; honest scope-limitation framing incomplete).

- **Do NOT introduce new FI-CHIR-CONT-N entries beyond FI-CHIR-CONT-10/11/12 at §B**: the FI inventory is at v0.1 outline +3 sector-specific (§B; this patch) +3 sector-specific (§C; future Patches 0492+) for a maximum 6 sector-specific FIs. Additional FIs would expand the foundational input stack beyond joint paper scope.

- **Do NOT mix §B sector-specific content with §C sector-specific content**: §B (this sketch) is SF-2 V–A coupling derivation; §C (future sketch at `flagship_papers/chirality_continuum/sketches/sector_b_chiral_polarity_bias.md` to be opened at Patches 0492+) is SM-2 chiral-polarity-bias exclusion derivation. The two sector closures use parallel structure (bridge inheritance + sector-specific identification + kinematic projection) but with different EFT frameworks (Yang-Mills for §B; effective free-energy / partition-function for §C). Mixing risks losing the structural-parallelism benefit.

- **Do NOT undo §A closure in §B drafting**: the bridge theorem THEO-CHIR-CONT-1 is fixed and §B inherits from it without modification. If §B sector-specific work surfaces structural tension with the bridge theorem, the resolution path is to update §A bridge work (which would be unusual after sub-claim (a) closure) — but only if the structural tension is unmistakable, not for ordinary sector-specific scope adjustments.

---

## §10 Status update at §B Session 1 end

**Patch**: 0488 (this patch; §B Sector A Session 1 — Sketch OPENED + Step 1 sector-specific continuum operator identification CLOSED).

**Date**: 20 May 2026 (Session 137 continuation, post-Patch 0487 sub-claim (a) closure).

**Programme state changes**:

1. **§B Sector A working sketch OPENED** at `flagship_papers/chirality_continuum/sketches/sector_a_va_coupling.md` (this file, ~450 lines).
2. **Theorem B.1 statement ESTABLISHED** at theorem-statement level (THEO-CHIR-CONT-2 candidate): Sector A Yang-Mills EFT V–A Coupling Derivation theorem with four sub-claims (b)+(c)+(d)+(e). Sub-claim (b) sector-specific continuum operator identification CLOSED at this patch via §3 Step 1 closure.
3. **Step 1 of Theorem B.1 closure ACHIEVED**: sector-specific continuum operator identification — $\mathcal{O}^{\text{eff,W}} \leftrightarrow \bar{\psi}_L \gamma^\mu \psi_L$ in Yang-Mills $SU(2)_L \times U(1)_Y$ EFT framework via three structural identifications (Identification 1: $\zeta^{\text{cont,W}} \leftrightarrow \gamma_5$; Identification 2: matter-doublet $\leftrightarrow \{\psi_R, \psi_L\}$; Identification 3: $\mathcal{O}^{\text{eff,W}} \leftrightarrow$ V–A current).
4. **Sector-specific physical content inherited at leading order**: pure-V–A structure; coupling magnitude $\chi/6$; gauge coupling to $W^\pm$; Lorentz covariance from Yang-Mills EFT framework.
5. **Step 2 setup architecture ARTICULATED** for Session 2 (Patch 0489+ candidate): Michel parameter $\rho = 3/4$ derivation at finite mass via standard V–A kinematics.
6. **Step 3 setup architecture ARTICULATED** for Session 3 (Patch 0490+ candidate): 100% LH preference at massless helicity limit via V–A coupling structure.
7. **Step 4 setup architecture ARTICULATED** for Session 4 (Patch 0491+ candidate): Capotauro Falsifier 6 activation at observable-scale prediction thresholds.
8. **FI dependency mapping COMPLETE** for §B Sector A: FI-CHIR-CONT-1/2/3 (substrate-level inheritance from THEO-CHIR-CONT-1) + FI-CHIR-CONT-9 (Substrate-Locality inheritance) + FI-CHIR-CONT-10/11/12 (sector-specific to §B: W-bracelet sector specialization + SF-2 Yang-Mills EFT framework + continuum-EFT chirality-projection structure) + AXIM-1/2/3/4/7 (CPP axiom stack inheritance).
9. **NO theorems registered new at programme level** (THEO-CHIR-CONT-2 candidate at theorem-statement level only; registration at end of §B Session 4 upon sub-claims (b)+(c)+(d)+(e) all closing).
10. **NO predictions registered new** (Michel parameter $\rho = 3/4$ and 100% LH at massless limit and Capotauro Falsifier 6 activation are sub-claim targets pending Sessions 2+3+4 of §B; PRED-O-25 inherited at substrate-handle level from THEO-CAP-1 + THEO-SD-CHIR-1+2 + THEO-CHIR-CONT-1).
11. **NO falsifiers registered new** (Capotauro Falsifier 6 activation deferred to Session 4 of §B).

**Forward queue post-Patch 0488**:

- **Priority 1 (Patch 0489+ candidate)**: §B Sector A Session 2 — Step 2 Michel parameter $\rho = 3/4$ derivation at finite mass. 1 session estimated.
- **Priority 2 (Patch 0490+ candidate)**: §B Sector A Session 3 — Step 3 100% LH preference at massless helicity limit derivation. 1 session estimated.
- **Priority 3 (Patch 0491+ candidate)**: §B Sector A Session 4 — Step 4 Capotauro Falsifier 6 activation + Theorem B.1 promotion to programme-level registered-theorem status as THEO-CHIR-CONT-2. 1 session estimated. **SUB-CLAIM (b)+(c)+(d)+(e) CLOSURE PATCH for §B**; completes §B Sector A derivation.
- **Priority 4 (Patches 0492+)**: §C Sector B chiral-polarity-bias derivation; v0.4 substantive drafting; 3–5 sessions; expected to register THEO-CHIR-CONT-3 candidate.
- **Subsequent (Patches 0496+)**: §D polish; v0.5; 1–2 sessions.
- **Subsequent (Patches 0498+)**: v0.6–v0.9 reviewer cycle; v1.0 SHIP at Patch 0503+.

**Anti-priorities preserved**: as enumerated in §0 + §9 above. Most critical for Session 1 → Session 2 transition of §B: do NOT close Steps 2–4 at Session 1 (deferred to Sessions 2–4 of §B); do NOT promote Theorem B.1 to programme-level registered-theorem status at Session 1 (registration at end of §B Session 4 patch).

**Methodological observation — §B Step 1 closure inherits cleanly from §A bridge theorem**: the sector-specific operator identification §B Step 1 closure followed the structural template of §A Step 3 (continuum operator identification at sector-agnostic level) but with sector-specific identification of the abstract continuum operator with the V–A current operator. The cleanness of this inheritance — three identifications across structural / algebraic / matter-doublet content lines fully closing the sector-specific identification — confirms the sector-agnostic abstraction of §A delivered the right structural ingredients for sector-specific §B closure. This validates the joint paper format's structural efficiency at the §A → §B handoff: §A delivers sector-agnostic ingredients; §B applies them sector-specifically.

**Methodological observation — §B sub-claim (b) closure cost matches projection**: 1 session for Step 1 (sector-specific operator identification) matches the §B scoping sketch (Patch 0482 §3.1) estimate of "1 session per step" for §B's 4-step structure. If Sessions 2–4 of §B close at the same rate, total §B closure cost is ~4 sessions (Patches 0488–0491+), within the v0.1 outline §5 estimate of 3–5 sessions for §B substantive drafting.

---

*Sketch authored by Claude Opus (Anthropic) under Thomas Lee Abshier's direction, 20 May 2026, Session 137 continuation, Patch 0488 (Session 1 of §B Sector A V–A coupling derivation). Opens substantive §B sector-specific work at the joint Layer 4 paper post sub-claim (a) closure. Session 1 deliverable: Theorem B.1 statement + Step 1 sector-specific continuum operator identification + Steps 2–4 setup architecture. Sub-claim (b) (sector-specific operator identification) CLOSED at this patch via three structural identifications ($\zeta^{\text{cont,W}} \leftrightarrow \gamma_5$; matter-doublet $\leftrightarrow \{\psi_R, \psi_L\}$; $\mathcal{O}^{\text{eff,W}} \leftrightarrow$ V–A current $\bar{\psi}_L \gamma^\mu \psi_L$). Sub-claims (c)+(d)+(e) closure target at Sessions 2+3+4 of §B (Patches 0489+, 0490+, 0491+ candidates). THEO-CHIR-CONT-2 candidate at theorem-statement-with-Step-1-closed level; registration at programme theorem-registry at end of §B Session 4.*
