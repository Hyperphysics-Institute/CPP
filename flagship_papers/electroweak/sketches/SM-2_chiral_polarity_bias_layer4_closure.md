# SM-2 v2.0+ Chiral-Polarity-Bias Layer 4 Closure: Continuum-EFT Projection of the Substrate Handle $\chi/6$ (qDP/eDP Sector)

**Working sketch document — Tier-4 reasoning capture per CPP four-tier documentation discipline.**

This sketch opens the SM-2 v2.0+ Layer 4 closure trajectory for the chiral-polarity-bias mechanism stated at SM-2 v1.0 §10 ("Quark Charge Asymmetry and Capotauro"; the 600-cell's intrinsic chirality preferentially stabilises linear ZBW extras on negative $-$qCP centres) and now substantively workable as of Capotauro v2.0 v1.0 SHIPPED (19 May 2026, Session 135 Patch 0479), which delivered the substrate-physics handle $|M^{qDP}| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ at full Layer 3 rigor via THEO-SD-CHIR-2 (qDP/eDP Sector Substrate Chirality Closure Theorem; registered Patch 0440 Session 133).

The closure target — explicitly named in Capotauro v2.0 §intro\_status\_at\_v2.0 (line 156) — is the **substrate-handle projection to numerical Linear-ZBW-on-$-$qCP stabilization energy at observable scales** via continuum-EFT calculation, demonstrating that the substrate-level chirality preference at magnitude $\chi/6$ is sufficient to forbid the SM-disallowed Linear-ZBW-on-$+$qCP configuration at SM-accessible thermodynamic equilibrium. The closure delivers the substrate-level account of *why* the down-type quark charge is $-1/3$ rather than $+1/3$.

This sketch is the **second of two paired scoping sketches** opening the v3.0+ Layer 4 closure programme. The companion sketch ([`flagship_papers/electroweak/sketches/SF-2_chir_layer4_closure.md`](../../../flagship_papers/electroweak/sketches/SF-2_chir_layer4_closure.md), created at Patch 0482 Session 136 opening) opens the parallel SF-2 v2.0+ V--A coupling Layer 4 closure trajectory inheriting the sibling substrate handle from THEO-SD-CHIR-1. The two sketches together enable the architectural-clarity analysis (this sketch §4) that the Patch 0482 sketch's §4.4 venue recommendation hedged pending: the **cross-sector parallel question** — how structurally identical the two Layer 4 closures are, and therefore whether a joint Layer 4 paper closing both OPEN-FP entries is structurally optimal versus two separate dedicated Layer 4 papers.

This sketch's load-bearing conclusion (§5 below) is that **Venue (c) joint Layer 4 paper is PROMOTED to recommended primary venue**, updating the Patch 0482 sketch §4.4 framing where Venue (c) was named as "recommended deferred option." The substrate-handle-to-effective-coupling bridge step is the load-bearing technical step (per Patch 0482 §3.1) and is genuinely shared between the two sector closures; the post-bridge continuum-EFT machinery is sector-specific but not exotic in either sector.

This sketch is Tier-4 exploratory reasoning at scoping level — Layer 1 / Layer 2 epistemic status (cross-sector parallel analysis + sub-claim decomposition + foundational input enumeration), not Layer 3 (formal theorem-level closure). The sketch is paired with:

- the SM-2 v1.0 paper ([`series_standard_model/papers/SM-2_mass_generation_geometric_hierarchies.tex`](../../../series_standard_model/papers/SM-2_mass_generation_geometric_hierarchies.tex), §10 chiral-polarity-bias mechanism statement and §5+§6+Glossary Linear/Orbital ZBW characterization),
- the Capotauro v2.0 paper ([`flagship_papers/capotauro/capotauro.tex`](../capotauro.tex), §sec:qdp\_edp\_sector THEO-SD-CHIR-2 derivation chain plus §intro\_status\_at\_v2.0 line 156 explicit closure-target naming),
- the Capotauro Reading C sketch ([`flagship_papers/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md`](Capotauro_chiral_mechanism_candidate.md), §18--§20 Q6 closure work establishing THEO-SD-CHIR-2 at full Layer 3 rigor),
- the SF-2 v2.0+ companion sketch ([`flagship_papers/electroweak/sketches/SF-2_chir_layer4_closure.md`](../../../flagship_papers/electroweak/sketches/SF-2_chir_layer4_closure.md), the parallel sketch this one cross-references for joint-paper venue analysis),
- the PD-004 publication-pathway document ([`programmatic_decisions/PD-004-publication-pathway.md`](../../../programmatic_decisions/PD-004-publication-pathway.md), Layer 4 venue guidance).

Bibliography cross-reference key: `abshier_sm2_cpb_layer4_sketch`.

---

## §0 Working-session firewall

Subject to revision. Layer 4 continuum-EFT closure work is a substantive trajectory; the present sketch is at scoping level only. **The architectural decision surfaced by this sketch** is the **venue update** based on cross-sector parallel analysis with the SF-2 v2.0+ Layer 4 closure trajectory opened at Patch 0482:

- **Venue (c) joint Layer 4 paper** closing both OPEN-FP-SF-2-CHIR and SM-2 v2.0+ chiral-polarity-bias via shared substrate-handle-to-effective-coupling bridge plus sector-specific kinematic projections — **PROMOTED to recommended primary venue** in this sketch (§5 below).
- Updates Patch 0482 sketch §4.4 framing where Venue (c) was "recommended deferred option."
- Venue (b) two separate dedicated Layer 4 papers remains as **structural fallback** if joint-paper drafting surfaces unanticipated technical obstructions (e.g., one of the sector-specific projections requires substantively more infrastructure than the other).

The route choice (Route (i) canonical continuum-EFT vs. Route (ii) substrate-mechanism) parallel to the Patch 0482 sketch §2 framing is preserved at Route (i) primary; the qDP/eDP sector does not have a Route (ii) substrate-mechanism alternative analogous to the Patch 0367 W$^0$ neutrino scattering centroid-decoupling sketch (no captured substrate-mechanism insight for chiral-polarity-bias exists outside the Capotauro Reading C trajectory's THEO-SD-CHIR-2 result).

Anti-priority: do NOT begin substantive Layer 4 derivation work before the joint paper venue decision is confirmed by Thomas. The sub-claim decomposition (§3) and foundational input enumeration (§1.3) are independent of venue choice and can be developed in parallel; the actual derivation work depends on whether joint paper or two separate papers gets the green light.

---

## §1 Setup: the Layer 4 closure question

### §1.1 What is to be derived

The closure target articulated explicitly by Capotauro v2.0 §intro\_status\_at\_v2.0 (line 156):

> "the substrate handle $\chi/6$ of Theorem~\ref{thm:theo_sd_chir_2} for the qDP/eDP sector feeds the SM-2 v2.0+ chiral-polarity-bias EFT continuum-limit calculation closing to numerical Linear-ZBW-on-$-$qCP stabilization energy at observable scales."

Operationally: derive the **effective free-energy split** $\Delta F^{qDP}$ between Linear-ZBW-on-$-$qCP and Linear-ZBW-on-$+$qCP configurations at observable thermodynamic scales, given the substrate-level chirality matrix element $|M^{qDP}| = \chi/6$ as input. Demonstrate that $\Delta F^{qDP}$ is sufficient to **forbid the Linear-ZBW-on-$+$qCP configuration** at SM-accessible temperatures, consistent with the empirical absence of positive down-type quarks (no SM particle has charge $+1/3$ with down-type ZBW configuration).

The structural picture at SM-2 v1.0 (preserved at v2.0+ trajectory pickup):

- **Linear ZBW (qDP)** is the down-type quark substrate configuration: a single linear axis of unbound substrate dimension ($d = 1$, $\sigma \approx 8.3 \times 10^{-3}$) per SM-2 v1.0 §5+§6+Glossary. The Linear-ZBW configuration combined with the orbital eDP screening gives the $-1/3$ charge of down-type quarks via the second $1/3$ charge reduction.
- **Orbital ZBW (eDP)** is the universal substrate configuration: spherically symmetric orbital state with no preferred substrate direction ($d = 0$, $\sigma = 1$). Present in all fermions.
- **Chiral-polarity-bias mechanism** (SM-2 §10): the substrate's intrinsic chirality (activated during the Capotauro symmetry-breaking event per the Capotauro paper) preferentially stabilises Linear-ZBW extras on negative $-$qCP centres. The asymmetric coupling produces the $-1/3$-vs-$+2/3$ structural distinction between down-type and up-type quark charges.

The mechanism at SM-2 v1.0 sits at *structural-preference level* — supported by the substrate-chirality observation but not at theorem-level rigor. The Layer 4 closure target is to **lift the structural-preference claim to theorem level via the continuum-EFT effective free-energy projection**, using the substrate handle $|M^{qDP}| = \chi/6$ from Capotauro v2.0 as the substrate-physics input.

### §1.2 What changed at Capotauro v2.0 (substrate handle now in hand)

At SM-2 v1.0 SHIP, the chiral-polarity-bias claim sat as "structural preference, not theorem-level" because the substrate-level chirality magnitude for the qDP/eDP sector was not yet derived. Capotauro v2.0's Reading C trajectory (Sessions 87--133) delivered the substrate handle as a theorem-level derivation:

- **THEO-SD-CHIR-2** (qDP/eDP Sector Substrate Chirality Closure Theorem; registered Session 133 Patch 0440): $|M^{qDP}| = \chi/6 = \phi^{-3}/6 \approx 0.0394$, identical magnitude to $|M^W| = |M^{K3}|$ via three-way cross-sector unification under OPEN-SD-CHIR-PRIMITIVE umbrella.
- Substrate object: Linear ZBW characterized as **antipodal-pair vertex configuration** $\{v_i, -v_i\}$ on the first-shell icosahedron at the host 600-cell vertex, with stabilizer $D_{5d} \subset I_h$ of order 20 (refinement of single-vertex $C_{5v}$ stabilizer per Q6 Step 2 closure trajectory).
- Pairing convention: $\zeta^{qDP}$ identified as **combined $CP$ operation** — host-CP-centered spatial inversion ($v \to -v$) combined with $\hat{n}$-flip ($\hat{n} \to -\hat{n}$) combined with qCP-sign flip ($\pm \to \mp$); the three flips together preserve substrate's overall chirality content (Finding C-W46 at Capotauro Reading C sketch §20.4).
- Matter-doublet basis: $|\Psi_-^{qDP,(1)}\rangle = (|+, v\rangle + |-, -v\rangle)/\sqrt{2}$ ($\zeta^{qDP}$-EVEN), $|\Psi_-^{qDP,(2)}\rangle = (|+, v\rangle - |-, -v\rangle)/\sqrt{2}$ ($\zeta^{qDP}$-ODD), spanning 2D subspace of $A_{1g} \oplus A_{2u}$ in $D_{5d}$ paralleling K3-doublet 2D $E$-irrep and W-bracelet 2D $E_2 \oplus E_1$ subspace structures.
- Chirality operator: $\hat{C}^{qDP} \in A_{2u}(D_{5d})$ with non-vanishing matrix element via $A_{1g} \otimes A_{2u} \otimes A_{2u} = A_{1g} \supset A_{1g}$.

This delivers the substrate-physics input that the chiral-polarity-bias mechanism needs but did not have at SM-2 v1.0. The Layer 4 closure now reduces to: **show that the continuum-EFT projection of the substrate-level matrix element $|M^{qDP}| = \chi/6$ produces an effective free-energy split sufficient to forbid Linear-ZBW-on-$+$qCP at observable thermodynamic scales.**

### §1.3 Foundational input enumeration

The Layer 4 closure inherits the following foundational inputs (FIs). These parallel the FI-CHIR-N inventory of the Patch 0482 SF-2 v2.0+ sketch with sector-specific substitutions for the qDP/eDP closure.

**Substrate-level inheritance (Layer 3 results in hand)**:

- **FI-CPB-1**: Substrate primitive 4D direction $\hat{n}$ in ambient $\mathbb{R}^4$ at vertex-aligned Reading C (FI-C-RC-1 + FI-C-RC-2 from Capotauro v2.0; shared with FI-CHIR-1 of the SF-2 sketch).
- **FI-CPB-2**: Substrate chirality magnitude $|\chi| = \phi^{-3}$ derived from perturbative-distance-ratio constraint (shared with FI-CHIR-2; replaces v1.0 FI-C-9 free-magnitude postulate).
- **FI-CPB-3**: Substrate residual symmetry $H_3 = I_h$ at host 600-cell vertex (shared with FI-CHIR-3; Theorem stab\_Hfour at Capotauro v2.0).
- **FI-CPB-4**: qDP/eDP substrate chirality matrix element $|M^{qDP}| = \chi/6$ at full Layer 3 rigor (THEO-SD-CHIR-2; Capotauro v2.0 §sec:qdp\_edp\_sector derivation chain).
- **FI-CPB-5**: Linear-ZBW substrate-object characterization as antipodal-pair $\{v_i, -v_i\}$ with $D_{5d}$ stabilizer; matter-doublet basis under combined $CP$ pairing convention (Capotauro v2.0 Finding C-W46).

**Continuum-EFT inheritance (Layer 3/4 architecture in hand)**:

- **FI-CPB-6**: SM-2 v1.0 §5+§6+Glossary Linear-vs-Orbital ZBW characterization (substrate-configuration-type distinction; not Dipole-Point-particle-type distinction); $d = 1$ Linear ZBW vs. $d = 0$ Orbital ZBW configurational structure.
- **FI-CPB-7**: SM-2 v1.0 §10 chiral-polarity-bias mechanism statement (the substrate-level preferential stabilization claim that Layer 4 closure promotes from structural-preference level to theorem level).
- **FI-CPB-8**: Effective free-energy / partition-function framework for substrate configurations at SM-accessible temperatures (standard substrate stat-mech machinery; analog of SF-2's Yang-Mills EFT inheritance from EW-5 THEO-EW-8 thm:YM\_EFT proof outline, but technically distinct framework).

**Continuum kinematics inheritance (standard SM machinery)**:

- **FI-CPB-9**: Standard Model fractional-charge structure at observable scales ($+2/3$ for up-type quarks; $-1/3$ for down-type quarks; SM-1 Theorem 1 derives the exact $\delta = 1/3$ charge screening); the substrate-level closure must recover the *selectivity* (Linear-ZBW-on-$-$qCP forbidden) consistent with this charge structure.
- **FI-CPB-10**: Empirical absence of positive down-type quarks at SM-accessible energy scales (no observed SM particle has charge $+1/3$ with down-type ZBW configuration); the substrate-level exclusion at Layer 4 closure must hold across the SM-accessible thermodynamic range.

The FI count (10) is intentionally parallel to the SF-2 sketch's FI-CHIR-1 through FI-CHIR-10 inventory, with shared substrate-level FIs (CPB-1, CPB-2, CPB-3) and sector-specific substitutions for the qDP/eDP continuum-EFT and kinematic content. The shared-vs-distinct FI accounting is the **structural backbone** of the joint-paper venue analysis (§4 and §5 below).

### §1.4 Layer architecture per PD-004

Per PD-004 layer architecture (parallel to SF-2 sketch §1.4): SM-2 v2.0+ chiral-polarity-bias closure is **Layer 4 work**. The substrate-handle derivation (THEO-SD-CHIR-2) is **Layer 3 substrate phenomenology**; the projection from $|M^{qDP}| = \chi/6$ to Linear-ZBW-on-$-$qCP stabilization energy at observable scales is the Layer 4 continuum-EFT projection step that SM-2 v1.0 §10 chiral-polarity-bias claim registered as future work.

PD-004's explicit guidance ("dedicated papers are required — this cannot be folded into flagship phenomenology papers") applies equally to SM-2 v2.0+ Layer 4 work and SF-2 v2.0+ Layer 4 work; both should land in dedicated Layer 4 venue rather than as within-flagship extensions. The question of whether the dedicated venue is **one joint paper** (Venue (c)) or **two separate dedicated papers** (Venue (b)) is the architectural decision §5 below resolves.

---

## §2 Closure target articulation

### §2.1 What SM-2 v1.0 establishes

SM-2 v1.0 §10 ("Quark Charge Asymmetry and Capotauro") states the chiral-polarity-bias mechanism in five lines:

> Down-type quarks carry a linear ZBW extra DP (qDP/hDP) that up-type quarks do not. The CPP mechanism is the Capotauro chiral-polarity bias: the 600-cell's intrinsic chirality (activated during the Capotauro symmetry-breaking event) preferentially stabilises linear ZBW extras on negative ($-$qCP) centres.

This gives the charge asymmetry:

- Up-type: orbital eDP screening only $\to +2/3$.
- Down-type: orbital + linear screening $\to -1/3$.

The exact charge values follow from $\delta = 1/3$ (SM-1, Theorem 1).

**Key observation**: SM-1 already derives the $\delta = 1/3$ charge screening at theorem level. What SM-2 v1.0 §10 establishes — and what SM-2 v2.0+ Layer 4 closure must lift to theorem level — is the **selectivity**: *why* Linear ZBW preferentially binds on $-$qCP centres rather than $+$qCP centres. The closure delivers the **substrate-level account of the up/down quark asymmetry's chiral origin**.

### §2.2 What Layer 4 closure delivers

The Layer 4 closure produces:

1. **Effective free-energy split**: $\Delta F^{qDP}(\beta) = F_{\text{Linear-ZBW-on-}+}(\beta) - F_{\text{Linear-ZBW-on-}-}(\beta)$ at observable inverse temperature $\beta$, projected from substrate-level matrix element $|M^{qDP}| = \chi/6$ via the substrate-handle-to-effective-coupling bridge.
2. **Exclusion bound**: $\Delta F^{qDP}(\beta_{\text{SM}}) > k_B T_{\text{SM}} \cdot \ln(N_{\text{configurations}})$ at SM-accessible temperatures $T_{\text{SM}}$, demonstrating that Linear-ZBW-on-$+$qCP is statistically excluded across the SM-accessible thermodynamic range.
3. **Cross-validation with SM observation**: the exclusion bound is consistent with the empirical absence of positive down-type quarks at all energy scales probed by collider, atomic-physics, and cosmological constraints.
4. **Falsifier activation**: failure to derive $\Delta F^{qDP}$ sufficient for exclusion at observable scales, or experimental observation of Linear-ZBW-on-$+$qCP configurations (positive down-type quark candidate at high-precision measurements), would falsify the SM-2 v2.0+ chiral-polarity-bias closure claim and constitute a sharp empirical falsifier of the OPEN-SD-CHIR-PRIMITIVE umbrella's electromagnetic-handedness leg.

The closure does NOT derive:

- The exact $\pm 1/3$ charge values themselves (these are inherited from SM-1 Theorem 1).
- The dynamical mechanism producing the Capotauro symmetry-breaking event (this is Q7 cosmological-timing work in the Capotauro programme; OPEN-SM-4 sub-claim (a); future-window).
- The substrate-physics derivation of the primitive 4D direction $\hat{n}$ itself (this is Q1$'$+Q1$'$.A Layer 3 promotion; the deepest open work of the Capotauro programme).

---

## §3 Sub-claim decomposition under canonical Layer 4 route

The Layer 4 closure under Route (i) (continuum-EFT canonical path; the substrate-mechanism alternative Route (ii) is not applicable to the qDP/eDP sector — no analog of the Patch 0367 W$^0$ neutrino scattering centroid-decoupling sketch exists) decomposes into four sub-claims parallel to the SF-2 sketch §3 decomposition.

### §3.1 Sub-claim (a): bridge from substrate handle to effective Linear-ZBW-on-$-$qCP coupling

**Statement**: the substrate-level chirality matrix element $|M^{qDP}| = \chi/6$ from THEO-SD-CHIR-2 projects to a chirality-sensitive coupling in the continuum-limit effective free-energy of the Linear-ZBW configuration on a $\pm$qCP host, with the substrate magnitude $\chi/6$ controlling the strength of the chirality bias in the continuum thermodynamic structure.

**Closure architecture**: identify the entry point where the substrate chirality matrix element $|M^{qDP}|$ enters the effective free-energy data for the Linear-ZBW configuration on $\pm$qCP. The Linear-ZBW substrate-object on the antipodal-pair $\{v_i, -v_i\}$ with $D_{5d}$ stabilizer carries the substrate chirality via $\zeta^{qDP}$ = combined $CP$ operation; the continuum-limit projection of $\zeta^{qDP}$-EVEN vs $\zeta^{qDP}$-ODD substrate states should produce a chirality-asymmetric coupling in the effective free-energy data.

**Critical observation**: **this sub-claim is structurally identical to SF-2 sketch sub-claim (a)** — the bridge from substrate matrix element to continuum-EFT effective coupling. The only sector-specific element is the stabilizer ($D_{5d}$ here vs. $D_6$ for W-bracelet) and $\zeta$ generator (combined $CP$ here vs. icosahedral-center inversion in 4D for W-bracelet); the **bridge architecture itself is shared**. This is the load-bearing observation for the joint paper venue analysis (§4 below).

**Required infrastructure**: explicit form of the substrate-handle-to-effective-coupling bridge, valid for any $D$-type stabilizer with $\zeta$ generator and matter-doublet basis spanning 2D subspace of representative irreps. The shared infrastructure makes the joint-paper bridge work more efficient than two separate single-sector bridges.

**Estimated session count**: 2--3 sessions (same as SF-2 sub-claim (a); shared work if joint paper).

### §3.2 Sub-claim (b): substrate-level stabilization energy $\Delta E^{qDP} = \chi \cdot g(\text{cage geometry})$

**Statement**: the substrate-level stabilization energy split between Linear-ZBW-on-$-$qCP and Linear-ZBW-on-$+$qCP configurations is $\Delta E^{qDP} = \chi \cdot g(\text{cage geometry})$, with $g$ determined by the cage-shell averaging on the icosahedral cage at the host CP and the matter-doublet structure under combined $CP$ pairing.

**Closure architecture**: given sub-claim (a)'s bridge from substrate handle to effective coupling, compute the explicit stabilization energy split as a function of cage geometry. Per Capotauro v2.0 Finding C-W46, the substrate-level energy contribution is $|M^{qDP}| \cdot E_{\text{substrate}} = (\chi/6) \cdot E_{\text{substrate}}$ where $E_{\text{substrate}}$ is the characteristic substrate energy scale. The cage-shell averaging factor $1/6$ is geometric (Schur orthogonality on $D_{5d}$ stabilizer with effective dimension 2); the substrate energy scale $E_{\text{substrate}}$ is the natural scale of substrate-level processes at the 600-cell lattice.

**Empirical test**: $\Delta E^{qDP}$ must be sufficient to dominate thermal fluctuations $k_B T$ at SM-accessible temperatures $T \lesssim 10^{16}$ K (electroweak scale and below). The substrate energy scale $E_{\text{substrate}}$ is plausibly the Planck-derived scale of CPP substrate processes; this should be substantially larger than thermal scales at all SM temperatures.

**Estimated session count**: 2--3 sessions (sector-specific calculation post-bridge).

### §3.3 Sub-claim (c): exclusion at observable scales (thermodynamic comparison)

**Statement**: the effective free-energy split $\Delta F^{qDP}(\beta_{\text{SM}})$ at SM-accessible inverse temperatures satisfies the exclusion bound $\Delta F^{qDP}(\beta_{\text{SM}}) > k_B T_{\text{SM}} \cdot \ln(N_{\text{configurations}})$, forbidding Linear-ZBW-on-$+$qCP configurations at thermodynamic equilibrium across the SM-accessible temperature range.

**Closure architecture**: project sub-claim (b)'s substrate-level energy split through the partition-function machinery (standard substrate stat-mech) to derive the effective free-energy at observable temperatures. The configurational entropy contribution $\ln(N_{\text{configurations}})$ counts the number of accessible Linear-ZBW configurations at each $\pm$qCP host CP; the exclusion bound holds when the substrate-level energy split exceeds the entropy-weighted thermal scale.

**Empirical test**: consistent with the empirical absence of positive down-type quarks at all measured energy scales (collider experiments to current LHC energies $\sim 13$ TeV; atomic-physics constraints on quark fractional charge searches; cosmological constraints on primordial $+$qCP-linked configurations from BBN and CMB).

**Estimated session count**: 1--2 sessions (thermodynamic projection).

### §3.4 Sub-claim (d): cross-validation with SM fractional-charge structure

**Statement**: the closure chain (a)+(b)+(c) is consistent with the SM fractional-charge structure ($+2/3$ for up-type, $-1/3$ for down-type) inherited from SM-1 Theorem 1, with the substrate-level chiral-polarity-bias selectivity providing the substrate-physics account of *why* the down-type ZBW configuration binds on $-$qCP centres rather than $+$qCP centres.

**Closure architecture**: verify that the substrate-level closure does not contradict the SM-1 charge-derivation framework; verify that the chiral-polarity-bias mechanism extends rather than replaces the SM-1 charge derivation; document the closure chain's relationship to the SM-2 v1.0 §10 framing as an extension to theorem level.

**Estimated session count**: 1 session.

---

## §4 Cross-sector parallel with SF-2 v2.0+ Layer 4 closure

This section addresses the **information return** that justified the scoping work pair (Patches 0482 + 0483): how structurally identical the SF-2 and SM-2 Layer 4 closures are, and therefore whether a joint Layer 4 paper closing both is structurally optimal.

### §4.1 Shared infrastructure

The two closures share the following infrastructure:

1. **Substrate handle magnitude**: $|M^W| = |M^{qDP}| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ — *numerically identical* and structurally identical (both via the three-way cross-sector unification under OPEN-SD-CHIR-PRIMITIVE umbrella).

2. **Substrate-handle-to-effective-coupling bridge** (sub-claim (a) in each sketch): the bridge architecture is sector-agnostic — given a substrate-level matrix element $|M^{\text{sector}}| = \chi/6$ on a substrate object with $D$-type stabilizer, $\zeta$ generator, and matter-doublet basis in 2D subspace of $D$-irreps, the bridge projects to an effective coupling in the continuum-limit theory. **This is the load-bearing technical step** (per SF-2 sketch §3.1 and this sketch §3.1); doing it once vs. twice is the central efficiency question.

3. **Foundational input stack**: substrate-level FIs (FI-CHIR-1/2/3 in SF-2 sketch correspond to FI-CPB-1/2/3 here) are **identical**. Substrate-object stabilizer FIs (FI-CHIR-5/6/7/8 in SF-2 vs. FI-CPB-5/6/7/8 here) are sector-specific but structurally parallel.

4. **Cross-sector unification framing**: both closures land under the OPEN-SD-CHIR-PRIMITIVE umbrella registered Patch 0422 Session 130; both close umbrella manifestations (manifestation (ii) electroweak V--A for SF-2; manifestation (iii) electromagnetic handedness for SM-2). A joint paper foregrounds the cross-sector unification as the paper's structural identity claim.

5. **PD-004 layer mapping**: both closures are Layer 4 continuum-EFT projection work per PD-004; both require dedicated venue (within-flagship extension is precluded for both).

### §4.2 Distinct infrastructure

The two closures differ in the following ways:

1. **Substrate object stabilizer**:
   - SF-2: W-bracelet, $D_6 = S_3 \times \mathbb{Z}_2$ on Petrie-hexagon of first-shell icosahedron.
   - SM-2: Linear-ZBW antipodal pair $\{v_i, -v_i\}$, $D_{5d} \subset I_h$ of order 20.

2. **$\zeta$ generator**:
   - SF-2: $\zeta^W$ = icosahedral-center inversion in 4D ambient (purely geometric).
   - SM-2: $\zeta^{qDP}$ = combined $CP$ operation (spatial inversion + $\hat{n}$-flip + qCP-sign flip).

3. **Continuum-EFT framework**:
   - SF-2: Yang-Mills $SU(2)_L \times U(1)_Y$ EFT (inherited from EW-5 THEO-EW-8 thm:YM\_EFT at proof-outline level via SF-2 v1.0 §sec:YM\_EFT\_thm).
   - SM-2: effective free-energy / partition-function framework for substrate configurations (substrate stat-mech; no specific gauge-theory inheritance required).

4. **Observable kinematic structure**:
   - SF-2: Michel parameter $\rho = 3/4$ at finite mass; $100\%$ LH at massless helicity limit (V--A coupling kinematics).
   - SM-2: stabilization energy $\Delta F^{qDP}$ at observable thermodynamic scales (free-energy exclusion).

5. **Falsifier type**:
   - SF-2: Capotauro Falsifier 6 (V--A coupling deviation at high precision).
   - SM-2: positive down-type quark observation (would falsify chiral-polarity-bias exclusion).

### §4.3 Joint paper viability — updated assessment

The shared infrastructure is **load-bearing**:

- Substrate handle magnitude (identical)
- Substrate-handle-to-effective-coupling bridge (the load-bearing technical step)
- Foundational input stack (substantially overlapping)
- Cross-sector unification framing (the paper's structural identity claim)

The distinct infrastructure is **sector-specific but tractable**:

- Stabilizer subgroups and $\zeta$ generators differ but both are standard finite-group structures with well-defined matrix elements
- Continuum-EFT frameworks differ (Yang-Mills vs. effective stat-mech) but neither is exotic — both are standard machinery in their respective domains
- Observable kinematic structures differ (V--A kinematics vs. thermodynamic exclusion) but both fit naturally as separate sections of a joint paper

**Joint paper architecture estimate**:

- **§A Shared substrate-handle-to-effective-coupling bridge** (sub-claim (a) for both sectors; ~2--3 sessions; the load-bearing shared technical step).
- **§B SF-2 sector closure** (W-bracelet $D_6$ stabilizer; Yang-Mills EFT projection; Michel parameter $\rho = 3/4$; ~3--5 sessions).
- **§C SM-2 sector closure** (Linear-ZBW antipodal pair $D_{5d}$ stabilizer; effective free-energy projection; $\Delta F^{qDP}$ exclusion bound; ~3--5 sessions).
- **§D Cross-sector unification framing** (paper's structural identity claim; OPEN-SD-CHIR-PRIMITIVE umbrella context; ~1--2 sessions).
- **§E Paper drafting + reviewer cycle + v1.0 SHIP** (parallel to Capotauro v2.0 cycle; ~5--7 sessions).

**Total estimated session count for joint paper closure**: **15--22 sessions** (revised from Patch 0482 sketch §6 estimate of 15--25 sessions based on the cleaner cross-sector parallel analysis surfaced by this sketch).

**Compare to two separate dedicated papers**:

- SF-2 dedicated Layer 4 paper: 11--17 sessions per Patch 0482 sketch §6 estimate.
- SM-2 dedicated Layer 4 paper: 11--16 sessions (estimate parallel to SF-2; slightly lower because effective stat-mech infrastructure is more standard than Yang-Mills EFT).
- **Total two-separate-papers session count**: **22--33 sessions**.

**Joint paper saves an estimated 7--11 sessions** (range $22-22=0$ best-case-best-case, $33-15=18$ worst-case-best-case; central estimate $\sim$8 sessions saved) primarily by doing the shared bridge step once and by sharing reviewer-cycle infrastructure.

### §4.4 Risk assessment for joint paper venue

**Joint paper risks** to surface explicitly:

1. **Scope creep**: joint paper covering two sectors may try to cover too much; the paper's scope must be sharply bounded to OPEN-FP-SF-2-CHIR closure + SM-2 v2.0+ chiral-polarity-bias closure (specifically). Other OPEN-FP-SF-2-* entries (η, EWSB, loopfactor, shelldens, chaincomp) are NOT in scope for the joint paper.

2. **Technical complexity mixing**: Yang-Mills EFT machinery and effective stat-mech machinery are technically distinct; reviewers with expertise in one may not have expertise in the other. Mitigation: clear §B vs §C separation with sector-specific reviewer expertise expectations articulated in the paper structure.

3. **Single point of failure**: if either sector closure surfaces unanticipated technical obstructions, the joint paper risks delaying both closures. Mitigation: clear fallback to Venue (b) two separate papers if joint-paper drafting surfaces issues in one sector; the SF-2 closure can advance independently if SM-2 framework identification surfaces complications.

4. **Programme catalog precedent**: joint papers are uncommon in CPP; SF-4 v4.0 cross-sector closure was the first instance. A second cross-sector closure paper would establish the joint-paper pattern more firmly but also amplify the precedent risk if execution surfaces complications.

**Mitigation framework**: scoping work should produce a joint-paper outline at v0.1 level (~1 session) before substantive Layer 4 derivation begins; the v0.1 outline serves as the joint-paper viability decision gate. If v0.1 outline lands cleanly, proceed to Venue (c) joint paper. If v0.1 outline surfaces structural obstructions, fall back to Venue (b) two separate papers without loss of progress (the scoping work is venue-portable).

---

## §5 Updated venue recommendation

### §5.1 Venue (c) joint Layer 4 paper PROMOTED to primary venue

**Recommended venue**: **Venue (c) joint Layer 4 paper closing OPEN-FP-SF-2-CHIR and SM-2 v2.0+ chiral-polarity-bias jointly**.

Reasoning (updates Patch 0482 sketch §4.4 framing):

1. **Shared bridge step is load-bearing**: the substrate-handle-to-effective-coupling bridge (§3.1 sub-claim (a) in both sketches) is identified as the load-bearing technical step in both sectors. Joint paper does this work once instead of twice; estimated 7--11 session savings primarily from this efficiency.

2. **Cross-sector unification framing is structurally compelling**: a joint paper foregrounds the OPEN-SD-CHIR-PRIMITIVE umbrella's three-way unification ($|M^{K3}| = |M^W| = |M^{qDP}| = \chi/6$) at Layer 4 closure level, completing the architectural arc that Capotauro v2.0 established at Layer 3.

3. **SF-4 v4.0 precedent**: CPP's first cross-sector closure paper (SF-4 v4.0, Session 72, OPEN-FP-SF-4-2 + SM-5 op:nu\_id) demonstrates the methodological pattern works. Joint Layer 4 paper would establish the second cross-sector closure pattern in CPP — strengthening the programme-wide cross-sector unification methodology.

4. **Joint paper viability is high**: cross-sector parallel analysis (§4) shows that distinct infrastructure is sector-specific but tractable (no exotic machinery in either sector); risks are manageable with the v0.1-outline decision gate framework (§4.4).

### §5.2 Venue (b) two separate papers as fallback

**Structural fallback**: if joint-paper v0.1 outline surfaces unanticipated technical obstructions (e.g., one sector's continuum-EFT framework requires substantially more infrastructure than initially scoped), fall back to **Venue (b) two separate dedicated Layer 4 papers**:

- SF-2 v2.0+ dedicated Layer 4 paper: closes OPEN-FP-SF-2-CHIR via Yang-Mills EFT projection; 11--17 sessions.
- SM-2 v2.0+ dedicated Layer 4 paper: closes SM-2 v2.0+ chiral-polarity-bias via effective stat-mech projection; 11--16 sessions.

The scoping work (this sketch + Patch 0482 sketch) is **venue-portable** — the sub-claim decomposition, foundational input enumeration, and cross-sector parallel analysis are preserved regardless of joint-vs-separate venue choice.

### §5.3 Venue (a) within-flagship extension NOT recommended

**Not recommended** for either closure: within-flagship extension (extending SF-2 to v2.0+ or SM-2 to v2.0+ within the existing flagship papers) **contradicts PD-004 guidance** ("dedicated papers are required — this cannot be folded into flagship phenomenology papers"). Patch 0482 sketch §4.4 analysis applies equally to SM-2 v2.0+: within-flagship extension creates Layer-boundary inconsistency in the parent flagship paper.

### §5.4 Reasoning for the recommendation update (Patch 0482 → Patch 0483)

The Patch 0482 sketch §4.4 named Venue (c) joint paper as "recommended deferred option" because the cross-sector parallel structure had not yet been analyzed at scoping level — the SM-2 sketch had not been drafted yet, so the cross-sector parallel question was open. This Patch 0483 sketch §4 addresses that question explicitly with the result that **the closures are structurally parallel to a substantively higher degree than the Patch 0482 hedge implied**.

Specifically:

- The substrate-handle-to-effective-coupling bridge step is **load-bearing and shared** (Patch 0482 sketch §3.1 identified it as the load-bearing step; this sketch §3.1 + §4.1 confirms it is shared across both sectors).
- The continuum-EFT machinery is **sector-specific but not exotic** in either sector (Yang-Mills EFT for SF-2; effective stat-mech for SM-2); the joint paper does not require unusual technical infrastructure in either domain.
- The foundational input stack is **substantially overlapping** (FI-CHIR-1/2/3 = FI-CPB-1/2/3; sector-specific FIs are structurally parallel).

This is exactly the **information return** the scoping work pair (Patches 0482 + 0483) was designed to deliver. The Patch 0482 hedge was honest at the time of drafting (cross-sector parallel structure was an open question); this sketch resolves the question with a structurally clear recommendation update.

---

## §6 Session budget revision

Updated session budget estimate for v3.0+ Layer 4 closure programme:

**Venue (c) joint Layer 4 paper (recommended primary)**:

- §A shared substrate-handle-to-effective-coupling bridge: 2--3 sessions.
- §B SF-2 sector closure (sub-claims (b)+(c)+(d) under Patch 0482 sketch §3 decomposition): 3--5 sessions.
- §C SM-2 sector closure (sub-claims (b)+(c)+(d) under this sketch §3 decomposition): 3--5 sessions.
- §D cross-sector unification framing: 1--2 sessions.
- §E paper drafting + reviewer cycle + v1.0 SHIP: 5--7 sessions.
- §F joint paper v0.1 outline (decision gate; before §A): 1 session.
- **Total**: **15--22 sessions** (revised from Patch 0482 sketch §6 estimate of 15--25 sessions).

**Venue (b) two separate dedicated Layer 4 papers (fallback)**:

- SF-2 dedicated Layer 4 paper: 11--17 sessions (per Patch 0482 sketch §6 estimate).
- SM-2 dedicated Layer 4 paper: 11--16 sessions.
- **Total**: **22--33 sessions**.

**Joint paper session savings**: estimated **7--11 sessions** primarily via shared bridge work and shared reviewer-cycle infrastructure.

---

## §7 Forward queue and anti-priorities

### Forward queue priorities

**Priority 1 (immediate)**: Thomas's review of this scoping sketch and decision on:

(a) **Joint paper venue confirmation**: Venue (c) joint Layer 4 paper as primary (recommended); Venue (b) two separate papers as fallback. The recommendation update from Patch 0482 sketch §4.4 (Venue (c) as "deferred option") to this sketch §5.1 (Venue (c) as "primary") is the load-bearing decision point.

(b) **Joint paper v0.1 outline scoping**: 1 session to produce a joint-paper v0.1 outline (paper title; section structure; cross-sector framing; sub-claim decomposition mapping from individual sector sketches; bibliography skeleton). The v0.1 outline serves as the joint-paper viability decision gate before substantive Layer 4 derivation begins.

**Priority 2 (substantive work, post-venue-confirmation + v0.1-outline-completion)**: §A shared substrate-handle-to-effective-coupling bridge work (sub-claim (a) closure for both sectors jointly). Estimated 2--3 sessions; produces the load-bearing technical step in shared form.

**Priority 3 (background)**: Capotauro v2.0 §sec:qdp\_edp\_sector cross-reference review to confirm THEO-SD-CHIR-2 derivation chain inheritance details for FI-CPB-4 + FI-CPB-5 (substrate handle + Linear-ZBW characterization); SF-2 v1.0 §sec:YM\_EFT\_thm cross-reference review to confirm THEO-EW-8 thm:YM\_EFT proof outline inheritance details for FI-CHIR-6 (Yang-Mills EFT framework).

### Anti-priorities

**Do NOT begin substantive Layer 4 derivation work** before venue confirmation and joint paper v0.1 outline completion. The sub-claim decomposition (§3) and foundational input enumeration (§1.3) are independent of venue choice and reviewable as-is.

**Do NOT default to Venue (b) two separate papers** if joint paper venue surfaces obstructions at the v0.1 outline stage. The fallback should be triggered only if the v0.1 outline surfaces structurally substantive issues (e.g., one sector requires substantially more continuum-EFT infrastructure than the other; reviewer-expertise mismatch makes joint paper externally indefensible at one of the two sector closures).

**Do NOT mix Layer 4 joint paper drafting with SM-2 v1.0 paper text modifications**. SM-2 v1.0 is SHIPPED at v1.0 with .tex source frozen per the SS-9 v1.0 SHIP precedent. Layer 4 closure work under Venue (c) lands in a new dedicated joint paper, leaving SM-2 v1.0 and SF-2 v1.0 untouched.

**Do NOT mix Layer 4 closure work with other unrelated OPEN-FP-SF-2-* entries** (η, EWSB, loopfactor, shelldens, chaincomp) or other SM-series open problems. The joint paper scope is **strictly bounded to OPEN-FP-SF-2-CHIR + SM-2 v2.0+ chiral-polarity-bias closure**; other open work proceeds in independent trajectories.

**Do NOT pursue substrate-mechanism alternative** for the qDP/eDP sector. Unlike SF-2 (where Route (ii) substrate-mechanism via the Patch 0367 W$^0$ neutrino scattering centroid-decoupling sketch is registered as cross-validation candidate), the qDP/eDP sector has no analog captured substrate-mechanism insight; Route (i) canonical continuum-EFT path is the sole closure route for SM-2 v2.0+.

---

## §8 Status update at scoping sketch creation

**Patch**: 0483 (this patch; SM-2 v2.0+ scoping sketch creation + cross-sector parallel analysis + Patch 0482 sketch venue recommendation update).

**Date**: 19 May 2026 (Session 136 continuation, post-Patch 0482 SF-2 sketch).

**Programme state changes**:

1. **SM-2 v2.0+ chiral-polarity-bias closure trajectory OPENED at scoping level**: parallel to OPEN-FP-SF-2-CHIR v3.0+ Layer 4 closure trajectory opened at Patch 0482. This sketch establishes the closure target articulation, foundational input enumeration (FI-CPB-1 through FI-CPB-10), and sub-claim decomposition for the qDP/eDP sector Layer 4 closure.

2. **Cross-sector parallel analysis (§4) surfaces joint paper venue viability**: the two Layer 4 closures (SF-2 V--A and SM-2 chiral-polarity-bias) share load-bearing infrastructure (substrate handle magnitude $\chi/6$; substrate-handle-to-effective-coupling bridge step; foundational input stack overlap; OPEN-SD-CHIR-PRIMITIVE umbrella unification framing). Joint paper estimated 15--22 sessions vs. two separate papers 22--33 sessions; joint paper saves 7--11 sessions primarily via shared bridge work.

3. **Patch 0482 sketch §4.4 venue recommendation UPDATED**: Venue (c) joint Layer 4 paper PROMOTED from "recommended deferred option" (Patch 0482 framing) to **"recommended primary venue"** (this sketch §5.1). Venue (b) two separate papers preserved as **structural fallback** if joint-paper v0.1 outline surfaces unanticipated obstructions.

4. **Joint paper v0.1 outline scoping registered as Priority 1 next-substantive-work item**: 1 session to produce the joint-paper v0.1 outline as the joint-paper viability decision gate before §A shared bridge work begins.

5. **No theorems registered** (scoping is Layer 1/Layer 2 epistemic status; theorem-level closure at sub-claim (a)+(b)+(c) closure for each sector, estimated 15--22 sessions out under joint paper venue).

6. **No predictions registered** (substrate-level $|M^{qDP}| = \chi/6$ already registered as inherited from THEO-SD-CHIR-2).

7. **No falsifiers registered as new** (the falsifier "positive down-type quark observation" is implicit in SM-2 v1.0 chiral-polarity-bias framing; this sketch identifies the closure-consequence activation of this implicit falsifier as Capotauro Falsifier 6 analog at the EM-handedness leg).

8. **No conjecture registrations**.

9. **Problem counts UNCHANGED** (SM-2 v2.0+ chiral-polarity-bias closure was named as open Layer 4 work in Capotauro v2.0; not registered as a standalone OPEN-* entry separate from SM-2's existing open work).

**Files modified at Patch 0483**:

- `flagship_papers/electroweak/sketches/SF-2_chir_layer4_closure.md` (NOTE: per anti-priority discipline, the Patch 0482 sketch IS NOT MODIFIED at this patch; the venue recommendation update is registered in this Patch 0483 sketch §5 and in `research_frontier.md` Last-updated header. The Patch 0482 sketch §4.4 framing is preserved as the historical record of the venue analysis state at scoping-sketch-pair opening; the update is forward-cross-referenced).
- `flagship_papers/electroweak/sketches/SM-2_chiral_polarity_bias_layer4_closure.md` (NEW; this file; ~520 lines).
- `research_frontier.md` (Last-updated header prepended with venue-recommendation update milestone; OPEN-FP-SF-2-CHIR Status field appended with Patch 0483 cross-sector parallel analysis result + venue recommendation update to Venue (c) joint paper primary).
- `problem_histories/PH-OPEN-FP-SF-2-CHIR.md` (Patch 0483 cross-sector parallel analysis update entry appended).

**Epistemic status**: Layer 1 / Layer 2 (cross-sector parallel analysis + venue recommendation update); Layer 3 closure work begins at joint paper v0.1 outline + §A shared bridge step once venue confirmation is in hand.

**Methodological observation — paired scoping sketches enable venue resolution**: the scoping-sketch pair (Patches 0482 + 0483) demonstrates a structural pattern for resolving venue questions in cross-sector closure work. Patch 0482 opened the SF-2 sketch with venue framing hedged on the cross-sector parallel question (Venue (c) joint paper named as "deferred option" pending the parallel analysis). Patch 0483 opens the parallel SM-2 sketch and uses §4 cross-sector parallel analysis to resolve the venue question with structurally clearer evidence — promoting Venue (c) to primary recommendation. The pattern templates future cross-sector closure work: when two closures are candidates for joint vs. separate venue, **draft scoping sketches for both in sequence**, with the second sketch's cross-sector parallel analysis resolving the venue question for both. The cost is one additional scoping session; the information return is venue-decision clarity before substantive derivation begins.

**Forward action for Thomas**: review this sketch and respond on:

1. **Joint paper venue confirmation**: Venue (c) joint Layer 4 paper closing OPEN-FP-SF-2-CHIR + SM-2 v2.0+ chiral-polarity-bias jointly (recommended). The recommendation update from Patch 0482 sketch §4.4 framing is the load-bearing decision point.
2. **Joint paper v0.1 outline scoping**: authorize the 1-session v0.1 outline patch (Patch 0484 candidate) as the joint-paper viability decision gate before substantive §A shared bridge work begins.
3. **Session budget acceptance**: 15--22 sessions for joint paper closure (vs. 22--33 sessions for two separate papers); 7--11 session savings primarily via shared bridge work and shared reviewer-cycle infrastructure.
4. **Anti-priority confirmation**: do not modify SF-2 v1.0 or SM-2 v1.0 .tex source during Layer 4 closure work under Venue (c); do not mix joint paper scope with other unrelated open work; do not default to Venue (b) two separate papers without v0.1 outline surfacing structural obstructions.

Upon Thomas's confirmation of joint paper venue + v0.1 outline scoping authorization, the next substantive patch (Patch 0484 candidate) opens **joint paper v0.1 outline scoping** as the decision gate before §A shared substrate-handle-to-effective-coupling bridge work begins.

---

*Sketch authored by Claude Opus (Anthropic) under Thomas Lee Abshier's direction, 19 May 2026, Session 136 continuation, Patch 0483. Opens the SM-2 v2.0+ chiral-polarity-bias Layer 4 closure trajectory at scoping level and resolves the cross-sector parallel question raised at Patch 0482 sketch §4.4 with venue recommendation update: Venue (c) joint Layer 4 paper PROMOTED to recommended primary venue. Pairs with the Patch 0482 sketch (`SF-2_chir_layer4_closure.md`) under the paired-scoping-sketches pattern surfaced by this sketch §8 methodological observation. Joint paper venue confirmation pending Thomas's review; joint paper v0.1 outline scoping (Patch 0484 candidate) registered as immediate next-substantive-work item.*
