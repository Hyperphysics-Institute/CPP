# Chirality Continuum v0.1 Outline — Working Document

**Status:** v0.1 outline — drafting at Session 137 Patch 0484; joint-paper viability decision gate before v0.2 substantive drafting begins.
**Track:** Joint Layer 4 closure paper; second cross-sector closure paper in CPP after SF-4 v4.0; not numbered in the SF-line per the Capotauro-precedent for named-flagship-without-SF-N-number papers.
**Working title:** *Cross-Sector Layer 4 Closure of the Substrate Chirality Handle: Electroweak V--A Coupling and Quark Chiral-Polarity-Bias from $|M| = \chi/6$*
**Established:** 20 May 2026 (Session 137 opening, Patch 0484; post Patch 0483 cross-sector parallel analysis + Thomas's Session 136 Venue (c) confirmation).
**Estimated effort to v1.0 SHIP:** 15--22 sessions of v0.x drafting iteration from outline lock through v1.0 SHIP. Compare to Venue (b) two separate dedicated Layer 4 papers (22--33 sessions); joint paper saves 7--11 sessions primarily via shared substrate-handle-to-effective-coupling bridge work and shared reviewer-cycle infrastructure.
**Target venue:** Zenodo (DOI primary) + arXiv hep-ph (if endorsement obtainable) at v1.0 SHIP. OSF deposit (DOI 10.17605/OSF.IO/JXE8D umbrella) at v1.0 SHIP per established programme practice.
**Authors (anticipated):** Thomas Lee Abshier ND + Claude Opus (Anthropic).
**Foundation:** Patch 0482 scoping sketch [`SF-2_chir_layer4_closure.md`](../electroweak/sketches/SF-2_chir_layer4_closure.md) (SF-2 v2.0+ V--A closure trajectory) + Patch 0483 scoping sketch [`SM-2_chiral_polarity_bias_layer4_closure.md`](../electroweak/sketches/SM-2_chiral_polarity_bias_layer4_closure.md) (SM-2 v2.0+ chiral-polarity-bias closure trajectory + cross-sector parallel analysis).

---

## Strategic context

The joint Layer 4 paper is the natural follow-on to Capotauro v2.0 v1.0 SHIPPED (Session 135 Patch 0479). Capotauro v2.0 delivered the **substrate handle**: $|M^W| = |M^{qDP}| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ at full Layer 3 rigor via THEO-SD-CHIR-1 (K3-doublet $\leftrightarrow$ W-bracelet pair) and THEO-SD-CHIR-2 (qDP/eDP sector closure), under the OPEN-SD-CHIR-PRIMITIVE umbrella's three-way cross-sector unification. What Capotauro v2.0 did NOT close is the **Layer 4 projection** from the substrate-level matrix element to observable phenomena at SM-accessible scales. The joint paper closes that gap for two sectors at one cost.

The two sector projections share the **substrate-handle-to-effective-coupling bridge step** as load-bearing common infrastructure (identified at Patch 0482 sketch §3.1 and confirmed at Patch 0483 sketch §3.1). Doing the bridge work once instead of twice is the structural efficiency that motivates the joint-paper venue.

**Why this paper, why now:**

- Capotauro v2.0 v1.0 SHIPPED 19 May 2026 delivered the substrate handle the previous SF-2 v1.0 §sec:dm\_muon line 921 and SM-2 v1.0 §10 explicitly registered as missing.
- The OPEN-SD-CHIR-PRIMITIVE umbrella's three-way unification ($|M^{K3}| = |M^W| = |M^{qDP}| = \chi/6$) at Layer 3 is the structural identity claim that the joint Layer 4 paper extends to observable scales.
- Layer 4 work per PD-004 ("dedicated papers are required — this cannot be folded into flagship phenomenology papers") requires dedicated venue; joint paper is the structurally efficient dedicated venue for the two parallel closures.
- The SF-4 v4.0 first-cross-sector-closure precedent (Session 72; OPEN-FP-SF-4-2 + SM-5 op:nu\_id joint closure) demonstrates the cross-sector closure methodological pattern works; this paper establishes the second instance.
- A successful joint landing strengthens the cross-sector closure pattern as established CPP methodology, available for future cross-sector closure work (e.g., manifestations (iv) thermodynamic causal arrow + (v) cosmological-vacuum asymmetry under the same OPEN-SD-CHIR-PRIMITIVE umbrella).

---

## Headline claim (draft v0.1 — refine before §0 abstract drafting)

> **CPP closes two Standard Model phenomenological features — the V--A coupling structure of $W^\pm$-mediated weak interactions and the chiral-polarity-bias structure of quark charge asymmetry — jointly as Layer 4 continuum-EFT projections of a single substrate-level chirality matrix element $|M| = \chi/6 = \phi^{-3}/6 \approx 0.0394$.** The substrate handle is inherited at full Layer 3 rigor from the Capotauro v2.0 cross-sector unification theorems (THEO-SD-CHIR-1 for the W-bracelet sector; THEO-SD-CHIR-2 for the qDP/eDP sector). The **shared substrate-handle-to-effective-coupling bridge step** is identified as the load-bearing technical content; the two sector-specific kinematic projections proceed via standard SM machinery (Yang-Mills EFT for V--A coupling kinematic projection; effective free-energy partition-function framework for chiral-polarity-bias thermodynamic projection). At v1.0 SHIP, the paper delivers theorem-level closure of both OPEN-FP-SF-2-CHIR (V--A coupling at the massless helicity limit) and SM-2 v2.0+ chiral-polarity-bias EFT continuum-limit (Linear-ZBW-on-$-$qCP stabilization energy at observable scales), constituting the second cross-sector closure in CPP after SF-4 v4.0.

**Single most striking number for abstract:** the identical substrate-level chirality magnitude $\chi/6 \approx 0.0394$ feeding two structurally distinct observable phenomena — the 75\% finite-mass / 100\% massless-helicity-limit V--A coupling at the electroweak scale, and the Linear-ZBW-on-$-$qCP stabilization energy that excludes positive down-type quarks at all SM-accessible energy scales — at zero free parameters in either sector.

---

## §0 v0.1 outline working-session firewall

Subject to revision. The v0.1 outline establishes the paper's architecture and serves as the **joint-paper viability decision gate** before substantive Layer 4 derivation begins (§10 below). v0.1 outline content may be refined or re-scoped during v0.2 substantive drafting based on what the actual derivation work surfaces.

**Anti-priorities preserved at v0.1 outline drafting:**

- Do NOT modify SF-2 v1.0 or SM-2 v1.0 paper text during this paper's drafting (both at v1.0 SHIPPED with .tex source frozen per the SS-9 v1.0 SHIP precedent).
- Do NOT mix joint paper scope with other unrelated OPEN-FP-SF-2-* entries (OPEN-FP-SF-2-$\eta$, OPEN-FP-SF-2-EWSB, OPEN-FP-SF-2-loopfactor, OPEN-FP-SF-2-shelldens, OPEN-FP-SF-2-chaincomp) or other SM-series open problems.
- Do NOT exceed the joint-paper scope: v0.1 outline § structure is bounded to OPEN-FP-SF-2-CHIR + SM-2 v2.0+ chiral-polarity-bias closure specifically.
- Do NOT modify Patches 0482 + 0483 scoping sketches (preserved at historical locations per anti-priority discipline).

---

## §1 Paper structure (10-section architecture)

The joint paper's section structure follows the SM-2 sketch §4.3 five-section architecture (shared bridge + two sector closures + cross-sector framing + paper drafting) extended with paper-framework sections (abstract, intro, predictions/falsifiers, open work, discussion) per the SF-4 v1.0 SHIP precedent.

### §1.1 Abstract

Single paragraph stating: substrate handle inheritance from Capotauro v2.0; joint Layer 4 closure of two sector projections; shared bridge step as load-bearing technical content; sector-specific kinematic projections via standard SM machinery; cross-sector unification identity claim under OPEN-SD-CHIR-PRIMITIVE umbrella; primary empirical content (V--A coupling at massless helicity limit + chiral-polarity-bias exclusion at observable scales); conditional-theorem-closure-paper framing (inherits Capotauro v2.0's conditional-closure discipline).

### §1.2 Plain-language summary

Written for the educated-but-non-specialist reader at the Rovelli/SciAm register established by SS-7/SS-8/SS-9 anthology chapters. Explains: substrate-level chirality as a primitive feature of the 600-cell substrate; one substrate-level number $\chi/6$ controls two seemingly-unrelated phenomena at the Standard Model scale; the joint closure as cross-sector unification at Layer 4 of the CPP architecture.

### §1.3 §1 Introduction

§1.1 The two SM phenomenological features the paper closes (V--A coupling; quark chiral-polarity-bias).

§1.2 Why these are paired: shared substrate handle from Capotauro v2.0; shared bridge architecture; cross-sector unification under umbrella.

§1.3 What this paper delivers: theorem-level closure of two OPEN-FP entries jointly; substrate-physics input from Capotauro v2.0 plus continuum-EFT projection plus standard SM kinematic machinery.

§1.4 Closure status and roadmap: conditional-theorem-closure-paper framing (inherits Capotauro v2.0 + SF-4 v4.0 conditional-closure discipline); closure rests on foundational input stack + CPP axioms + Capotauro v2.0 substrate-handle inheritance.

§1.5 Position in the CPP corpus: second cross-sector closure paper in CPP after SF-4 v4.0; pairs with Capotauro v2.0 (substrate-level chirality framework $\leftrightarrow$ continuum-level chirality framework).

### §1.4 §2 Inheritance: Capotauro v2.0 Substrate-Level Results

§2.1 THEO-SD-CHIR-1 inheritance: K3-doublet $\leftrightarrow$ W-bracelet substrate-level cross-sector unification; $|M^W| = \chi/6$ via four-step proof chain.

§2.2 THEO-SD-CHIR-2 inheritance: qDP/eDP sector closure; $|M^{qDP}| = \chi/6$ via antipodal-pair refinement to $D_{5d}$ with combined-$CP$ pairing convention.

§2.3 The three-way cross-sector unification at substrate level: $|M^{K3}| = |M^W| = |M^{qDP}| = \chi/6 \approx 0.0394$ under OPEN-SD-CHIR-PRIMITIVE umbrella.

§2.4 What Layer 3 delivered (substrate-level chirality matrix elements at full Layer 3 rigor); what Layer 4 must deliver (continuum-EFT projection to observable scales).

### §1.5 §3 The Shared Substrate-Handle-to-Effective-Coupling Bridge

**This is the load-bearing technical step** — sub-claim (a) shared across both sector closures (per Patches 0482 + 0483 sketch §3.1 identification).

§3.1 Bridge architecture: given a substrate-level matrix element $|M^{\text{sector}}| = \chi/6$ on a substrate object with $D$-type stabilizer ($D_6$ for W-bracelet; $D_{5d}$ for qDP/eDP), $\zeta$ generator (icosahedral-center inversion for W-bracelet; combined $CP$ for qDP/eDP), and matter-doublet basis in 2D subspace of representative irreps, project to a chirality-sensitive effective coupling in the continuum-limit theory.

§3.2 Theorem 3.1 (Substrate-Handle Projection Theorem): bridge step at full Layer 3 + Layer 4 rigor.

§3.3 Cross-sector applicability: the bridge architecture is sector-agnostic; sector-specific elements (stabilizer, $\zeta$ generator) plug in as parameters of the bridge.

§3.4 Foundational inputs inherited at this stage: FI-CHIR-CONT-1 through FI-CHIR-CONT-5 (substrate-level FIs shared between sectors).

### §1.6 §4 Sector A: Electroweak V--A Coupling Derivation

§4.1 Inheritance from SF-2 v1.0: W-bracelet $D_6$ stabilizer (THEO-SF-2-1 Theorem 4.2); Yang-Mills EFT proof outline (THEO-SF-2-5 / thm:YM\_EFT); 75\% V--A from bracelet phase bias (PROP-SF-2-5; structural-preference level at v1.0).

§4.2 Yang-Mills EFT projection: extend THEO-SF-2-5 proof outline with substrate handle $|M^W| = \chi/6$ as substrate-physics input; recover continuum gauge-coupling chirality structure.

§4.3 Theorem 4.1 (V--A Coupling at Observable Scales): the substrate handle $|M^W| = \chi/6$ projects through the Yang-Mills EFT continuum-limit to the V--A coupling structure of $W^\pm$-mediated weak interactions at observable scales.

§4.4 Sub-claim (b) Michel parameter $\rho = 3/4$ at finite mass: standard SM kinematic projection of V--A coupling structure to muon decay; empirical match $\rho = 0.74979 \pm 0.00026$ (PDG 2024) vs SM-predicted $\rho = 3/4$ at $10^{-4}$ level.

§4.5 Sub-claim (c) Massless helicity limit 100\% LH preference: kinematic enhancement at zero mass; standard SM result recovered.

§4.6 Sub-claim (d) Capotauro Falsifier 6 activation: explicit empirical-content articulation of the falsifier; closure-consequence mapping.

### §1.7 §5 Sector B: Chiral-Polarity-Bias Derivation

§5.1 Inheritance from SM-2 v1.0: Linear vs Orbital ZBW characterization (§5+§6+Glossary; Linear ZBW $d = 1$ down-type quark substrate configuration; Orbital ZBW $d = 0$ universal substrate configuration); §10 chiral-polarity-bias mechanism statement.

§5.2 Inheritance from Capotauro v2.0: $\zeta^{qDP}$ = combined $CP$ operation; matter-doublet basis $|\Psi_-^{qDP,(1)}\rangle, |\Psi_-^{qDP,(2)}\rangle$ in 2D subspace of $A_{1g} \oplus A_{2u}$ in $D_{5d}$; chirality operator $\hat{C}^{qDP} \in A_{2u}(D_{5d})$.

§5.3 Effective free-energy / partition-function projection: substrate-level matrix element $|M^{qDP}| = \chi/6$ projects to effective free-energy split between Linear-ZBW-on-$\pm$qCP configurations at observable thermodynamic scales.

§5.4 Theorem 5.1 (Linear-ZBW-on-$-$qCP Stabilization Energy): the substrate handle $|M^{qDP}| = \chi/6$ projects to a stabilization energy split $\Delta F^{qDP}(\beta)$ that satisfies the exclusion bound $\Delta F^{qDP}(\beta_{\text{SM}}) > k_B T_{\text{SM}} \ln(N_{\text{configurations}})$ at SM-accessible inverse temperatures $\beta_{\text{SM}}$.

§5.5 Sub-claim (b) substrate-level stabilization energy calculation: $\Delta E^{qDP} = \chi \cdot g(\text{cage geometry})$ via cage-shell averaging on icosahedral cage with $D_{5d}$ stabilizer + matter-doublet structure.

§5.6 Sub-claim (c) exclusion at observable scales: thermodynamic comparison; consistent with empirical absence of positive down-type quarks at all measured energy scales.

§5.7 Sub-claim (d) cross-validation with SM fractional-charge structure: the substrate-level closure does not contradict SM-1 charge-derivation framework (Theorem 1); chiral-polarity-bias mechanism extends rather than replaces SM-1 charge derivation.

### §1.8 §6 Cross-Sector Unification: The Structural Identity Claim

§6.1 The shared substrate handle: $|M^W| = |M^{qDP}| = \chi/6$ from Capotauro v2.0 three-way cross-sector unification; identical magnitude controlling two structurally distinct observable phenomena.

§6.2 The OPEN-SD-CHIR-PRIMITIVE umbrella perspective: this paper closes manifestations (ii) electroweak V--A and (iii) electromagnetic handedness; manifestations (iv) thermodynamic causal arrow and (v) cosmological-vacuum asymmetry registered for future-window work; manifestation (i) mass-mixing closed at Capotauro v2.0.

§6.3 Second cross-sector closure pattern in CPP after SF-4 v4.0: methodological pattern strengthening; templates future cross-sector closure work (manifestations (iv)+(v); analogous cross-sector closures in other sectors).

§6.4 Structural identity claim of the paper: a single substrate primitive (the 4D direction $\hat{n}$ in ambient $\mathbb{R}^4$) with derived magnitude $|\chi| = \phi^{-3}$ controls every parity-sensitive observable in the CPP framework via shared three-step machinery (substrate-locality + cage-shell averaging + sector-specific pairing convention) with sector-specific stabilizer subgroups and $\zeta$ generators.

### §1.9 §7 Predictions and Falsifiers

§7.1 Zero-parameter predictions:

| Prediction | Sector | Predicted Value | Empirical Match | Match Level |
|---|---|---|---|---|
| Substrate-level chirality magnitude | Both | $\chi/6 = \phi^{-3}/6 \approx 0.0394$ | Inherited from THEO-SD-CHIR-1 + THEO-SD-CHIR-2 | Theorem-level (Capotauro v2.0) |
| V--A coupling strength | A (electroweak) | 75\% LH at finite mass; 100\% LH at massless limit | Standard SM result; observed at all scales | Theorem-level (this paper) |
| Michel parameter | A (electroweak) | $\rho = 3/4$ | $\rho = 0.74979 \pm 0.00026$ (PDG 2024) | $10^{-4}$ level |
| Linear-ZBW-on-$-$qCP stabilization | B (EM-handedness) | $\Delta F^{qDP} > $ thermal threshold | Empirical absence of positive down-type quarks at all SM-accessible scales | Exclusion bound (this paper) |
| Cross-sector unification identity | Both | $|M^W| = |M^{qDP}| = \chi/6$ | Substrate-level identity (theorem) | Theorem-level (Capotauro v2.0; inherited) |

§7.2 Six falsifiers:

1. **Layer 4 EFT projection failure**: failure of continuum-EFT to recover V--A coupling at observable scales from substrate handle $|M^W| = \chi/6$ (Capotauro Falsifier 6 activation).
2. **Michel parameter deviation**: experimental observation of deviations from 75\% LH preference at finite-mass muon decay ($\rho \neq 3/4$ beyond standard SM precision).
3. **Right-handed neutrino observation**: experimental observation of right-handed neutrinos coupling to $W^\pm$ at observable energies (V--A coupling breakdown at observable scales).
4. **Positive down-type quark observation**: experimental observation of fractional-charge configurations consistent with Linear-ZBW-on-$+$qCP binding at SM-accessible energy scales (chiral-polarity-bias exclusion fails).
5. **Cosmological constraint on chiral-polarity-bias**: cosmological observation of primordial $+$qCP-linked configurations from BBN/CMB at scales incompatible with substrate-level exclusion (chiral-polarity-bias not active at early universe).
6. **Cross-sector unification breakdown**: experimental observation that the V--A coupling and chiral-polarity-bias effects scale differently with substrate magnitude (would falsify shared-substrate-handle claim under umbrella).

### §1.10 §8 Open Theorem-Level Work

§8.1 Sub-claims under sectoral closures (post-v1.0 SHIP work):

- OPEN-FP-SF-2-CHIR full closure: Layer 4 closure of OPEN-FP-SF-2-CHIR achieved at v1.0 SHIP; deeper closure (Layer 1 substrate-dynamics derivation of $\hat{n}$ itself) registered as future-window work tied to Q1$'$+Q1$'$.A Layer 3 promotion.
- SM-2 v2.0+ chiral-polarity-bias full closure: Layer 4 closure achieved at v1.0 SHIP; deeper closure (Layer 1 substrate-dynamics derivation of chiral-polarity-bias mechanism from CPP axioms A3 + A7) registered as future-window work.

§8.2 OPEN-SD-CHIR-PRIMITIVE umbrella future-window work:

- Manifestation (iv) thermodynamic causal arrow: substrate-level closure pending future-window work; template by three-step closure pattern (substrate-locality + cage-shell factor + sector-specific pairing convention).
- Manifestation (v) cosmological-vacuum asymmetry: substrate-level closure pending future-window work (potentially folded with Capotauro Q7 cosmological-timing sub-questions).

§8.3 Cross-validation candidates:

- Route (ii) substrate-mechanism via Patch 0367 W$^0$ neutrino scattering centroid-decoupling sketch: cross-validation candidate for Sector A V--A coupling derivation; future-window work pending Layers A/B/C operational development.

### §1.11 §9 Discussion

§9.1 Programme-level methodological pattern: paired-scoping-sketches-enable-venue-resolution pattern (Patches 0482 + 0483) + joint-Layer-4-closure-saves-load-bearing-bridge-work pattern (this paper) as durable CPP methodology templates.

§9.2 Cross-sector implications: completes the OPEN-SD-CHIR-PRIMITIVE umbrella's electroweak + EM-handedness legs at Layer 4; templates closure of manifestations (iv)+(v) under the same umbrella; positions CPP for the broader Layer 4 maturity programme per PD-004.

§9.3 Outlook: 2026-2032+ experimental constraints (precision Michel parameter measurements; fractional-charge searches; cosmological constraints) and theoretical extensions (manifestations (iv)+(v) closures; Layer 1 dynamical-engine work for $\hat{n}$ derivation).

### §1.12 §10 References

Bibliography with ~25 entries combining CPP-corpus inheritance (Capotauro v2.0; SF-2 v1.0; SM-2 v1.0; EW-5; SM-1; SF-4 v4.0 for cross-sector-closure-pattern citation) and external references (PDG 2024; muon decay precision measurements; quark fractional-charge constraints; cosmological constraints from BBN/CMB; OPEN-SD-CHIR-PRIMITIVE umbrella registration in research\_frontier.md).

---

## §2 Source-material map (inheritance graph)

| Source paper / artifact | Content drawn | Inheritance level | Section reference in joint paper |
|---|---|---|---|
| Capotauro v2.0 THEO-SD-CHIR-1 | $\|M^W\| = \chi/6$ at full Layer 3 rigor; W-bracelet $D_6$ stabilizer; $\zeta^W$ generator | Theorem-level | §2.1, §4.2, §4.3 |
| Capotauro v2.0 THEO-SD-CHIR-2 | $\|M^{qDP}\| = \chi/6$ at full Layer 3 rigor; antipodal-pair $D_{5d}$ stabilizer; $\zeta^{qDP}$ generator | Theorem-level | §2.2, §5.2, §5.4 |
| Capotauro v2.0 §intro\_status\_at\_v2.0 line 156 | Explicit Layer 4 closure-target articulation for both sectors | Programme-level | §1.2, §10 |
| Capotauro v2.0 FI-C-1 through FI-C-10 + FI-C-RC-1 + FI-C-RC-2 | Substrate-level foundational input stack | FI-inherited | §3.4 |
| SF-2 v1.0 THEO-SF-2-1 (Theorem 4.2) | W-bracelet 1200-orbit under $H_4$ action with $D_6$ stabilizer | Theorem-level | §4.1 |
| SF-2 v1.0 THEO-SF-2-5 (Theorem 8.3 / thm:YM\_EFT) | Yang-Mills EFT continuum-limit proof outline | Proof-outline (lifted to theorem in §4.3 with substrate-handle input) | §3.2, §4.2 |
| SF-2 v1.0 PROP-SF-2-5 | 75\% V--A from bracelet $120°/240°$ phase bias (structural-preference) | Structural-preference (lifted to theorem in §4.3) | §4.1, §4.4 |
| SF-2 v1.0 §sec:dm\_muon line 921 | OPEN-FP-SF-2-CHIR register-as-open for massless-helicity-limit closure | Register-as-open (closed in §4.5) | §1.1, §4.5 |
| SM-2 v1.0 §5+§6+Glossary | Linear vs Orbital ZBW characterization | Inherited as substrate-configuration definition | §5.1 |
| SM-2 v1.0 §10 | Chiral-polarity-bias mechanism statement | Register-as-structural-preference (lifted to theorem in §5.4) | §1.1, §5.1, §5.4 |
| EW-5 THEO-EW-6/7/8 | $SU(2)_L$ from $\Gamma$; Nexus gauge invariance; Yang-Mills EFT limit | Theorem-level inheritance | §4.2 |
| SM-1 Theorem 1 | Charge quantization $\delta = 1/3$ | Theorem-level inheritance (background context for §5.7) | §5.7 |
| SF-4 v4.0 cross-sector closure pattern | First cross-sector closure in CPP (OPEN-FP-SF-4-2 + SM-5 op:nu\_id) | Methodological-precedent inheritance | §6.3, §9.1 |
| PD-004 publication-pathway | Layer 4 venue guidance | Programme-strategic guidance | Throughout |
| OPEN-SD-CHIR-PRIMITIVE umbrella (Patch 0422) | Cross-sector unification umbrella registration | Programme-level registration | §6.2, §6.4 |
| Patch 0482 scoping sketch | SF-2 v2.0+ V--A closure trajectory + four-sub-claim decomposition | Scoping-level | §1, §4 |
| Patch 0483 scoping sketch | SM-2 v2.0+ chiral-polarity-bias closure trajectory + cross-sector parallel analysis + venue recommendation update | Scoping-level | §1, §5, §6 |

---

## §3 Foundational input inventory (merged from scoping sketches)

The foundational input stack inherits and merges the FI-CHIR-N inventory (Patch 0482 sketch §1.3) and FI-CPB-N inventory (Patch 0483 sketch §1.3), with shared substrate-level FIs merged and sector-specific FIs preserved. Naming convention is FI-CHIR-CONT-N for the joint-paper inventory.

**Substrate-level FIs (shared between sectors)**:

- **FI-CHIR-CONT-1**: Substrate primitive 4D direction $\hat{n}$ in ambient $\mathbb{R}^4$ (FI-C-RC-1 from Capotauro v2.0; FI-CHIR-1 = FI-CPB-1 from scoping sketches).
- **FI-CHIR-CONT-2**: Substrate chirality magnitude $|\chi| = \phi^{-3}$ derived from perturbative-distance-ratio constraint (FI-CHIR-2 = FI-CPB-2 from scoping sketches).
- **FI-CHIR-CONT-3**: Substrate residual symmetry $H_3 = I_h$ at host 600-cell vertex (FI-CHIR-3 = FI-CPB-3 from scoping sketches).

**Sector A (electroweak / V--A) FIs**:

- **FI-CHIR-CONT-4A**: W-bracelet substrate chirality matrix element $|M^W| = \chi/6$ at full Layer 3 rigor (THEO-SD-CHIR-1; FI-CHIR-4 from Patch 0482 sketch).
- **FI-CHIR-CONT-5A**: W-bracelet 1200-orbit + $D_6$ stabilizer + Petrie-hexagon-on-first-shell-icosahedron structure (THEO-SF-2-1; FI-CHIR-5 from Patch 0482 sketch).
- **FI-CHIR-CONT-6A**: Yang-Mills EFT continuum-limit at proof-outline level (THEO-SF-2-5 / thm:YM\_EFT; FI-CHIR-6 from Patch 0482 sketch).
- **FI-CHIR-CONT-7A**: 75\% V--A structural preference at finite mass (PROP-SF-2-5; FI-CHIR-7 from Patch 0482 sketch).
- **FI-CHIR-CONT-8A**: $SU(2)_L$ algebra from binary icosahedral group $\Gamma$ at theorem level (THEO-SF-2-2 / THEO-EW-6 inheritance; FI-CHIR-8 from Patch 0482 sketch).

**Sector B (EM-handedness / chiral-polarity-bias) FIs**:

- **FI-CHIR-CONT-4B**: qDP/eDP substrate chirality matrix element $|M^{qDP}| = \chi/6$ at full Layer 3 rigor (THEO-SD-CHIR-2; FI-CPB-4 from Patch 0483 sketch).
- **FI-CHIR-CONT-5B**: Linear-ZBW antipodal pair $\{v_i, -v_i\}$ + $D_{5d}$ stabilizer + combined-$CP$ pairing convention (Finding C-W46 from Capotauro v2.0; FI-CPB-5 from Patch 0483 sketch).
- **FI-CHIR-CONT-6B**: SM-2 v1.0 Linear-vs-Orbital ZBW characterization (FI-CPB-6 from Patch 0483 sketch).
- **FI-CHIR-CONT-7B**: SM-2 v1.0 §10 chiral-polarity-bias mechanism statement (FI-CPB-7 from Patch 0483 sketch).
- **FI-CHIR-CONT-8B**: Effective free-energy / partition-function framework for substrate configurations (FI-CPB-8 from Patch 0483 sketch).

**Continuum kinematics FIs (shared between sectors; standard SM machinery)**:

- **FI-CHIR-CONT-9**: Standard Model V--A coupling structure at continuum gauge-theory level (FI-CHIR-9 from Patch 0482 sketch).
- **FI-CHIR-CONT-10**: Standard Model fractional-charge structure at observable scales (inherited from SM-1 Theorem 1; FI-CPB-9 from Patch 0483 sketch).
- **FI-CHIR-CONT-11**: Empirical absence of positive down-type quarks at SM-accessible energy scales (FI-CPB-10 from Patch 0483 sketch).
- **FI-CHIR-CONT-12**: Michel parameter $\rho = 3/4$ as standard SM tree-level result (FI-CHIR-10 from Patch 0482 sketch).

**Total FI count**: 14 unique FIs (3 substrate-level shared + 5 sector A + 5 sector B + 4 continuum kinematics; sector A and B sector-specific FIs sum to 10; with 4 shared FIs = 14 total). Compare to Capotauro v2.0's 12 FIs; SF-4 v4.0's foundational-input inventory was ~10 across both sectors of its cross-sector closure. The joint paper's 14 FIs is within reasonable range for a conditional-theorem-closure flagship paper.

---

## §4 Pre-emptive reviewer-concern responses

Anticipated reviewer concerns from three audience types (electroweak / mathematical physics, EM-handedness / quark-sector phenomenology, joint Layer 4 work mathematical-physics):

**Concern: "The substrate-handle inheritance from Capotauro v2.0 is doing all the work; the Layer 4 projection looks like dressing."**

Response: §3 (shared bridge step) and §4.3 + §5.4 (sector-specific theorem-level lifts) make explicit the technical content the substrate handle alone does NOT establish — the bridge from substrate-level matrix element to continuum-EFT effective coupling is a non-trivial operation requiring identification of the entry point in the continuum-limit theory, with sector-specific kinematic projections proceeding via standard SM machinery only AFTER the bridge step is in hand. The substrate handle is a necessary input but not a sufficient closure; the bridge work is the load-bearing Layer 4 content.

**Concern: "The Yang-Mills EFT proof outline (THEO-SF-2-5) is itself at proof-outline level, not at full theorem-level rigor; how can you claim theorem-level closure of V--A coupling on a proof-outline foundation?"**

Response: §4.3 (Theorem 4.1) is conditional-theorem closure per the Capotauro v2.0 + SF-4 v4.0 + SS-9 v1.0 conditional-closure framework. Theorem 4.1 holds rigorously *under* the FI-CHIR-CONT-6A assumption that the Yang-Mills EFT continuum-limit proof outline is correct. The v1.0 SHIP framing makes this conditional explicit in §1.4 closure status; full continuum-limit derivation of THEO-SF-2-5 is registered as future Layer 4 work beyond this paper's scope.

**Concern: "The 'effective free-energy / partition-function framework' for the chiral-polarity-bias sector is vague; what specific continuum theory is invoked?"**

Response: §5.3 (Theorem 5.1 derivation) makes explicit the effective free-energy machinery used — substrate stat-mech applied to the Linear-ZBW configuration's coupling-energy structure on $\pm$qCP hosts, with the substrate-level matrix element $|M^{qDP}|$ entering as a contribution to the configurational energy. No exotic continuum theory is invoked; the framework is standard partition-function machinery applied to a substrate-specific configurational degree of freedom.

**Concern: "Why a joint paper instead of two separate dedicated Layer 4 papers? The two sectors are technically distinct."**

Response: §6 (cross-sector unification) makes the joint-paper structural identity claim explicit. The shared substrate-handle-to-effective-coupling bridge step (§3) is the load-bearing technical content; doing it once in a joint paper saves 7--11 sessions vs. doing it twice in two separate papers. The cross-sector unification framing under OPEN-SD-CHIR-PRIMITIVE umbrella is the paper's structural identity claim — the same substrate primitive controlling two structurally distinct observable phenomena is the substantive content, not just a packaging convenience.

**Concern: "How does this paper relate to the broader Layer 4 maturity programme per PD-004?"**

Response: §9.2 (cross-sector implications) and §1.5 (position in CPP corpus) make the relationship explicit. This paper is one node in the Layer 4 maturity programme — specifically, the V--A coupling + chiral-polarity-bias projections. Other Layer 4 work (other OPEN-FP-SF-2-* entries; full continuum-limit derivation of THEO-SF-2-5; manifestations (iv)+(v) under OPEN-SD-CHIR-PRIMITIVE umbrella; etc.) proceeds in separate dedicated Layer 4 papers per PD-004 guidance. This paper does not claim to close all of Layer 4 — it closes two specific Layer 4 projections jointly.

**Concern: "Conditional-theorem-closure framing seems like a way to weaken the rigor claim. Is the paper's theorem content actually rigorous?"**

Response: §1.4 + §10 explicitly distinguish theorem-level claims (derived rigorously from FI stack + CPP axioms via Wigner-Eckart machinery + standard SM kinematic projection) from FI-inherited claims (registered as foundational inputs to closure) from structural-argument-level claims (not at theorem-level rigor; flagged explicitly). The conditional-theorem-closure framework is established in CPP corpus by SS-9 + SF-4 + SF-2 + Capotauro v2.0; it is precisely the rigor discipline that distinguishes "theorem-level under explicit foundational-input assumptions" from "claim at structural-argument level."

---

## §5 Drafting plan and timeline

**v0.1 → v1.0 SHIP trajectory (15--22 sessions estimate):**

- **v0.1 outline** (this patch, Patch 0484): paper architecture established + joint-paper viability decision gate. 1 session.
- **v0.2 §A shared bridge work** (Patches 0485+; first substantive Layer 4 derivation): substrate-handle-to-effective-coupling bridge sub-claim closure (§3 in the eventual paper). 2--3 sessions.
- **v0.3 §B SF-2 sector closure** (Patches 0488+): Yang-Mills EFT projection + Michel parameter $\rho = 3/4$ derivation + massless-helicity-limit 100\% LH preference derivation. 3--5 sessions.
- **v0.4 §C SM-2 sector closure** (Patches 0492+): Effective free-energy projection + stabilization energy calculation + exclusion bound + SM cross-validation. 3--5 sessions.
- **v0.5 §D cross-sector unification framing + paper polish** (Patches 0496+): cross-sector unification §6 + predictions/falsifiers §7 + open work §8 + discussion §9 + abstract + plain-language summary + bibliography. 1--2 sessions.
- **v0.6--v0.9 reviewer cycle** (Patches 0498+): multi-reviewer convergence per the Capotauro v2.0 + SF-2 v1.0 + SF-4 v1.0 precedent (ChatGPT + Grok + CoPilot reviewer rotation; round-1 + round-2 + sign-off rounds). 3--5 sessions.
- **v1.0 SHIP** (Patch 0503+): final polish + title block + CHANGELOG + four-tier documentation suite + programme-level registry updates (theorem-registry.md THEO-CHIR-CONT-1 through -3 candidate; research\_frontier.md OPEN-FP-SF-2-CHIR CLOSED; paper\_catalog.md new joint-paper entry; master\_glossary.md new term additions; INDEX.md new flagship-paper row). 1--2 sessions.

**Estimated total**: 15--22 sessions of v0.x drafting + reviewer cycle + v1.0 SHIP from this v0.1 outline lock. Within the SF-line per-paper estimate (5--14 sessions) extended by the joint-paper cross-sector content (additional 5--8 sessions vs. single-sector closure).

---

## §6 Honest-scope summary

**What the joint paper establishes at v1.0 SHIP:**

- Theorem-level closure of OPEN-FP-SF-2-CHIR (V--A coupling at the massless helicity limit) under explicit FI inventory.
- Theorem-level closure of SM-2 v2.0+ chiral-polarity-bias EFT continuum-limit (Linear-ZBW-on-$-$qCP stabilization energy at observable scales) under explicit FI inventory.
- Cross-sector unification identity: $|M^W| = |M^{qDP}| = \chi/6$ at substrate level controls two structurally distinct observable phenomena via shared substrate-handle-to-effective-coupling bridge + sector-specific kinematic projections.
- Activation of Capotauro v2.0 Falsifier 6 as a sharp empirical falsifier at the electroweak leg.
- Methodological precedent: second cross-sector closure paper in CPP after SF-4 v4.0; templates future cross-sector closure work under OPEN-SD-CHIR-PRIMITIVE umbrella.

**What the joint paper does NOT establish:**

- First-principles derivation of the primitive 4D direction $\hat{n}$ from CPP primitive axioms (Q1$'$+Q1$'$.A Layer 3 promotion; future-window dynamical-engine work; deepest open work of the Capotauro programme).
- First-principles closure of foundational input stack (FI-CHIR-CONT-N entries are explicit inputs to closure; their derivation from CPP primitives is registered as future work).
- Full continuum-limit derivation of Yang-Mills EFT from CPP discrete substrate dynamics (THEO-SF-2-5 inherited at proof-outline level; full derivation registered as future Layer 4 work beyond this paper's scope).
- Closure of other OPEN-FP-SF-2-* entries (OPEN-FP-SF-2-$\eta$, OPEN-FP-SF-2-EWSB, OPEN-FP-SF-2-loopfactor, OPEN-FP-SF-2-shelldens, OPEN-FP-SF-2-chaincomp) — strictly NOT in scope; separate closure trajectories.
- OPEN-SD-CHIR-PRIMITIVE umbrella manifestations (iv) thermodynamic causal arrow and (v) cosmological-vacuum asymmetry — future-window work, not in scope.
- OPEN-SM-4 Capotauro mechanism for $\delta_{CP}$ at electroweak scale — future-window work, not in scope (separate from this paper's V--A coupling closure).
- Derivation of fractional-charge values $\pm 1/3, \pm 2/3$ themselves (inherited from SM-1 Theorem 1; this paper closes the SELECTIVITY of which configuration the down-type ZBW binds on, not the charge values themselves).
- Majorana vs Dirac neutrino character (separate question; not addressed).

**Out-of-scope explicit registrations:**

- $\sin^2\theta_{13}$ derivation (re-scoped to SF-2 v2.0+ flagship per Capotauro v1.0/v2.0; preserved at v2.0+ status).
- $\delta_{CP}$ derivation (downstream sub-claim work per OPEN-SM-4 sub-claim (a) Capotauro nucleation event; future-window).
- Baryon asymmetry $\eta_B$ derivation (downstream sub-claim work; future-window).
- Q7 cosmological-timing sub-questions (Capotauro programme future-window work).

---

## §7 v0.1 outline working notes

**Anti-priorities sustained at v0.1 outline level:**

- Outline preserves the conditional-theorem-closure framing established by SS-9 + SF-4 + SF-2 + Capotauro v2.0; does not over-claim theorem-level rigor where structural-argument or FI-inherited level is the honest framing.
- Outline does not modify any v1.0 SHIPPED paper text (SF-2 v1.0; SM-2 v1.0; Capotauro v2.0).
- Outline preserves Patches 0482 + 0483 scoping sketches at their historical locations under `flagship_papers/electroweak/sketches/`.
- Outline scope is bounded to OPEN-FP-SF-2-CHIR + SM-2 v2.0+ chiral-polarity-bias closure specifically; other OPEN-FP-SF-2-* entries are NOT in scope.

**v0.1 → v0.2 transition triggers:**

- Joint-paper viability decision gate (§10 below) yields "proceed to v0.2 substantive drafting."
- v0.2 first patch (Patch 0485 candidate) opens §A shared substrate-handle-to-effective-coupling bridge work; this is the load-bearing technical step and the next substantive Layer 4 derivation patch.

---

## §8 Cross-references to scoping sketches

- **Patch 0482 sketch** [`SF-2_chir_layer4_closure.md`](../electroweak/sketches/SF-2_chir_layer4_closure.md): SF-2 v2.0+ V--A closure trajectory; 10 foundational input enumeration (FI-CHIR-1 through FI-CHIR-10); four-sub-claim decomposition (a/b/c/d); Route (i) vs Route (ii) framing; §3.1 identifies sub-claim (a) bridge as the load-bearing technical step.

- **Patch 0483 sketch** [`SM-2_chiral_polarity_bias_layer4_closure.md`](../electroweak/sketches/SM-2_chiral_polarity_bias_layer4_closure.md): SM-2 v2.0+ chiral-polarity-bias closure trajectory; 10 foundational input enumeration (FI-CPB-1 through FI-CPB-10); four-sub-claim decomposition parallel to Patch 0482; **§4 cross-sector parallel analysis** identifies shared infrastructure (substrate handle magnitude identical; bridge step shared and load-bearing; FI stack substantially overlapping; cross-sector unification framing under umbrella) and distinct infrastructure (stabilizer subgroups; $\zeta$ generators; continuum-EFT frameworks; observable kinematic structure; falsifier types); **§5 venue recommendation update** promotes Venue (c) joint paper from "deferred option" to "primary venue."

The two sketches together constitute the **paired scoping foundation** for this v0.1 outline. The joint paper's v0.1 outline draws on both sketches' content with shared substrate-level FIs merged (FI-CHIR-CONT-1/2/3) and sector-specific FIs preserved (FI-CHIR-CONT-4A/.../8A + FI-CHIR-CONT-4B/.../8B + FI-CHIR-CONT-9/.../12).

---

## §9 Patch 0484 deliverables

- **NEW** `flagship_papers/chirality_continuum/` directory created.
- **NEW** `flagship_papers/chirality_continuum/README.md` (flagship-paper home-directory README).
- **NEW** `flagship_papers/chirality_continuum/chirality_continuum_outline.md` (this file; ~480 lines; the v0.1 outline document).
- **NEW** `flagship_papers/chirality_continuum/sketches/` placeholder directory for future joint-paper-specific sketches.
- **UPDATE** `research_frontier.md` Last-updated header prepended + OPEN-FP-SF-2-CHIR Status field updated with Patch 0484 v0.1 outline milestone + Venue (c) confirmation.
- **UPDATE** `problem_histories/PH-OPEN-FP-SF-2-CHIR.md` Patch 0484 v0.1 outline entry appended.

---

## §10 v0.1 outline viability decision gate

**This is the load-bearing content of the v0.1 outline.** The decision gate framework is established by Patch 0483 sketch §4.4 + §5; this section operationalizes the decision gate against five viability criteria.

### §10.1 Viability criteria

The joint-paper v0.1 outline is assessed against five criteria:

1. **Section structure coherence**: the 10-section structure (Abstract, plain-language summary, §1 Introduction, §2 Inheritance, §3 Shared Bridge, §4 Sector A V--A, §5 Sector B chiral-polarity-bias, §6 Cross-sector unification, §7 Predictions and Falsifiers, §8 Open Work, §9 Discussion, §10 References) covers both sector closures coherently; the shared content (§2, §3, §6, §7--§9) sits naturally alongside the sector-specific content (§4, §5).
2. **FI inventory manageability**: the 14 FI-CHIR-CONT-N entries are explicit, finite, separately reviewable; within reasonable range for a conditional-theorem-closure flagship paper (compare to Capotauro v2.0's 12 FIs and SF-4 v4.0's ~10 FIs).
3. **Cross-sector framing structural compellingness**: the OPEN-SD-CHIR-PRIMITIVE umbrella + three-way cross-sector unification at substrate level (from Capotauro v2.0) gives the joint paper a genuine structural identity claim, not a contrived packaging convenience. The shared substrate-handle-to-effective-coupling bridge step is load-bearing common infrastructure; doing it once vs. twice is the central efficiency.
4. **Sector-specific complication risk**: SM-2's effective stat-mech machinery is more standard than SF-2's Yang-Mills EFT projection; SF-2 has the load-bearing technical work in the kinematic projection step. No sector dominance issues anticipated; both sectors contribute substantive content to the joint paper.
5. **Reviewer-audience coherence**: mathematical physicists working on substrate-physics + Layer 4 continuum-EFT bridge work + cross-sector unification framing constitute a coherent reviewer audience. The joint paper does not split irreconcilably between electroweak-specialist and EM-handedness-specialist reviewer audiences because the substrate-physics layer is shared and the Layer 4 projection layer is the paper's technical centerpiece.

### §10.2 Viability assessment

**Assessment of each criterion**:

1. **Section structure coherence**: ✓ PASS. The 10-section structure is workable; shared content vs sector-specific content separation is clean; cross-sector unification framing in §6 ties the two sector closures together substantively.

2. **FI inventory manageability**: ✓ PASS. 14 FIs is at the upper end of the conditional-theorem-closure paper range but within reasonable bounds; sector-specific FIs are clearly labeled (-A vs -B suffix).

3. **Cross-sector framing structural compellingness**: ✓ PASS. The Capotauro v2.0 substrate-level three-way unification gives the joint paper genuine structural identity at Layer 3; the joint paper's contribution is extending this unification to Layer 4 closure of two of the three sector projections (the third — mass-mixing K3-doublet — is at substrate-level only without observable-scale projection in this paper's scope).

4. **Sector-specific complication risk**: ✓ PASS. Both sectors are technically tractable; SF-2's Yang-Mills EFT projection is the more demanding technical content but is well-scaffolded by the SF-2 v1.0 §sec:YM\_EFT\_thm proof outline. SM-2's effective stat-mech projection is standard machinery.

5. **Reviewer-audience coherence**: ✓ PASS. The joint paper's reviewer audience is mathematical-physicists / Layer-4-bridge-specialists; the audience is coherent across both sector closures.

**Net assessment**: all five viability criteria PASS. Joint paper viability is HIGH.

### §10.3 Recommendation

**Recommendation**: **PROCEED TO v0.2 SUBSTANTIVE DRAFTING** at Venue (c) joint Layer 4 paper.

The next substantive patch (Patch 0485 candidate) opens **§A shared substrate-handle-to-effective-coupling bridge work** — sub-claim (a) closure for both sectors jointly. This is the load-bearing technical step and is the natural first substantive content patch after v0.1 outline lock.

### §10.4 Fallback to Venue (b) preserved as structural option

If during v0.2+ substantive drafting unanticipated structural obstructions surface (e.g., one sector's continuum-EFT framework requires substantively more infrastructure than scoped at outline level; reviewer-audience splits irreconcilably during the v0.6+ reviewer cycle; cross-sector framing surfaces as contrived during §6 drafting), the fallback to Venue (b) two separate dedicated Layer 4 papers remains a structurally clean option per the Patch 0483 sketch §5.2 framing. The v0.1 outline content is venue-portable — sub-claim decomposition, FI enumeration, theorem-statement structures all preserve under Venue (b) fallback.

The Venue (b) fallback should be triggered ONLY if structural obstructions are substantively unmistakable; otherwise the joint paper proceeds per the Venue (c) recommendation.

---

## §11 v0.1 outline status update

**Patch**: 0484 (this patch; joint paper v0.1 outline creation + viability decision gate).

**Date**: 20 May 2026 (Session 137 opening, post-Patch 0483 Venue (c) confirmation by Thomas).

**Programme state changes**:

1. **Joint Layer 4 paper "Chirality Continuum" OPENED at v0.1 outline level**: paper home directory `flagship_papers/chirality_continuum/` created; README + v0.1 outline + sketches placeholder established.
2. **v0.1 outline viability decision gate operative**: five viability criteria assessed; all five PASS; recommendation is PROCEED TO v0.2 SUBSTANTIVE DRAFTING at Venue (c) joint paper.
3. **OPEN-FP-SF-2-CHIR Status field updated** in `research_frontier.md` with Patch 0484 v0.1 outline + Venue (c) confirmation milestone.
4. **PH-OPEN-FP-SF-2-CHIR.md updated** with Patch 0484 v0.1 outline entry.
5. **No theorems registered** (v0.1 outline is Layer 1/Layer 2 epistemic status; theorem-level closure occurs at sub-claim closure during v0.2--v0.5 drafting, estimated 7--15 sessions out).
6. **No predictions registered** (substrate-level $|M^W| = |M^{qDP}| = \chi/6$ already registered as inherited from THEO-SD-CHIR-1 + THEO-SD-CHIR-2; sector-specific observable predictions register at sub-claim closure).
7. **No falsifiers registered as new** (the six falsifiers enumerated in §1.9 are implicit in the closure-trajectory framing; explicit programme-level registration occurs at v1.0 SHIP).
8. **No conjecture registrations**.
9. **Problem counts UNCHANGED**.

**Files modified at Patch 0484**:

- `flagship_papers/chirality_continuum/README.md` (NEW; ~80 lines).
- `flagship_papers/chirality_continuum/chirality_continuum_outline.md` (NEW; this file; ~480 lines).
- `flagship_papers/chirality_continuum/sketches/.gitkeep` (NEW empty placeholder).
- `research_frontier.md` (Last-updated header prepended; OPEN-FP-SF-2-CHIR Status field appended with Patch 0484 milestone).
- `problem_histories/PH-OPEN-FP-SF-2-CHIR.md` (Patch 0484 v0.1 outline entry appended).

**Epistemic status**: Layer 1 / Layer 2 (paper architecture established; viability decision gate operative); Layer 3 closure work begins at v0.2 substantive drafting with §A shared substrate-handle-to-effective-coupling bridge work (Patch 0485 candidate).

**Methodological observation — v0.1 outline viability decision gate operationalizes joint-paper viability assessment**: the decision gate framework established at Patch 0483 sketch §4.4 + §5 is operationalized here at Patch 0484 against five explicit viability criteria. The pattern templates future joint-paper venue decisions: when joint paper is candidate venue, draft v0.1 outline as decision gate against explicit viability criteria; PASS yields proceed to v0.2; FAIL yields fallback to separate-paper venue. Cost of v0.1 outline is 1 session; information return is venue-decision finality with all v0.1 outline content venue-portable to fallback scenario.

**Forward action for Thomas**: review this v0.1 outline and respond on:

1. **Viability assessment confirmation**: all five viability criteria assessed at PASS; recommendation is PROCEED TO v0.2 SUBSTANTIVE DRAFTING. Confirm or surface viability concerns.
2. **§A shared bridge work authorization**: authorize Patch 0485 candidate to open the substantive §A shared substrate-handle-to-effective-coupling bridge work — sub-claim (a) closure for both sectors jointly. Estimated 2--3 sessions; produces the load-bearing technical step in shared form.
3. **Working title acceptance or revision**: "Cross-Sector Layer 4 Closure of the Substrate Chirality Handle: Electroweak V--A Coupling and Quark Chiral-Polarity-Bias from $|M| = \chi/6$" — accept or refine.
4. **Home directory acceptance or revision**: `flagship_papers/chirality_continuum/` paired with `flagship_papers/capotauro/` — accept or rename.
5. **Anti-priority confirmation**: no modifications to SF-2 v1.0 or SM-2 v1.0 paper text; joint paper scope strictly bounded to OPEN-FP-SF-2-CHIR + SM-2 v2.0+ chiral-polarity-bias closure; venue fallback to Venue (b) preserved as structural option.

Upon confirmation, Patch 0485 candidate opens §A shared substrate-handle-to-effective-coupling bridge work as the load-bearing technical step of the joint Layer 4 closure trajectory.

---

*v0.1 outline authored by Claude Opus (Anthropic) under Thomas Lee Abshier's direction, 20 May 2026, Session 137 opening, Patch 0484. Joint Layer 4 paper "Chirality Continuum" opened at v0.1 outline level with viability decision gate operative across five criteria — all PASS at v0.1 outline review; recommendation is PROCEED TO v0.2 SUBSTANTIVE DRAFTING at Venue (c) joint paper. Substantive §A shared substrate-handle-to-effective-coupling bridge work begins at Patch 0485 candidate post-viability-confirmation.*
