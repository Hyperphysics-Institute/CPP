# SF-2 V--A Coupling Layer 4 Closure: Continuum-EFT Projection of the Substrate Handle $\chi/6$

**Working sketch document — Tier-4 reasoning capture per CPP four-tier documentation discipline.**

This sketch opens the v3.0+ Layer 4 closure trajectory for OPEN-FP-SF-2-CHIR — the chirality emergence (V--A coupling derivation) at the W bracelet structure — registered at SF-2 v1.0 SHIP (14 May 2026, Session 83 close, Patch 0370) and now substantively workable as of Capotauro v2.0 v1.0 SHIP (19 May 2026, Session 135 close, Patch 0479), which delivered the substrate-physics handle $|M^W| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ at full Layer 3 rigor via THEO-SD-CHIR-1 (Cross-Sector Substrate Chirality Unification Theorem; K3-doublet $\leftrightarrow$ W-bracelet pair).

The closure target is **the lift of SF-2 v1.0's V--A coupling claim from structural-preference level to theorem level**: showing that the bracelet's $D_6$ phase-bias structure (SF-2 v1.0 §sec:dm\_muon line 921: "the bracelet's $D_6$ alternating-polarity structure produces a 75\% left-handed preference for the released centroid charge, becoming 100\% in the massless helicity limit, per OPEN-FP-SF-2-CHIR continuum-limit derivation") emerges as a derived consequence of the substrate handle $|M^W| = \chi/6$ under the continuum-limit Yang-Mills EFT projection (THEO-SF-2-5 / Theorem 8.3 proof outline).

Closure activates **Capotauro v2.0 Falsifier 6** as a sharp empirical falsifier (per the Capotauro v2.0 §13.4 falsifier ledger): if Layer 4 EFT projection fails to recover the V--A coupling at observable scales from the substrate handle, the cross-sector substrate-chirality unification claim under OPEN-SD-CHIR-PRIMITIVE umbrella is empirically vulnerable at the electroweak leg.

This sketch is Tier-4 exploratory reasoning at scoping level — Layer 1 / Layer 2 epistemic status (route choice + sub-claim decomposition + foundational input enumeration), not Layer 3 (formal theorem-level closure). The sketch is paired with:

- the SF-2 v1.0 paper ([`flagship_papers/electroweak/sf-2_electroweak.tex`](../sf-2_electroweak.tex), §sec:dm\_muon and §sec:YM\_EFT\_thm),
- the Capotauro v2.0 paper ([`series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex`](../../capotauro/capotauro.tex), §17 THEO-SD-CHIR-1 W-bracelet derivation),
- the Capotauro Reading C sketch ([`series_umbrella/series_substrate_chirality_arc/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md`](../../capotauro/sketches/Capotauro_chiral_mechanism_candidate.md), §15--§17 substrate-handle derivation chain),
- the Patch 0367 captured insight ([`flagship_papers/electroweak/sketches/W0_neutrino_scattering_centroid_decoupling.md`](W0_neutrino_scattering_centroid_decoupling.md), centroid-decoupling substrate-mechanism alternative),
- the PD-004 publication-pathway document ([`programmatic_decisions/PD-004-publication-pathway.md`](../../../programmatic_decisions/PD-004-publication-pathway.md), Layer 4 venue guidance).

Bibliography cross-reference key: `abshier_sf2_chir_layer4_sketch`.

---

## §0 Working-session firewall

Subject to revision. Layer 4 continuum-EFT closure work is a substantive trajectory; the present sketch is at scoping level only. **Two architectural decisions are surfaced explicitly for Thomas's review before substantive derivation work begins**:

1. **Route choice**: Route (i) canonical continuum-EFT Layer 4 derivation extending THEO-SF-2-5 proof outline vs. Route (ii) substrate-level mechanism via the Patch 0367 W$^0$ neutrino scattering centroid-decoupling sketch. The two routes are not mutually exclusive — Route (i) is the canonical Layer 4 path inheriting the substrate handle as input; Route (ii) is a substrate-mechanism alternative that could complement Route (i) by sharpening the Layer 1 dynamics. The sketch recommends Route (i) as primary with Route (ii) registered as a cross-validation candidate.

2. **Venue choice**: Venue (a) SF-2 v2.0+ flagship-paper extension (mirrors Capotauro v2.0 within-flagship extension pattern) vs. Venue (b) dedicated Layer 4 continuum-EFT paper per PD-004 ("dedicated papers are required — this cannot be folded into flagship phenomenology papers") vs. Venue (c) joint Layer 4 paper with SM-2 v2.0+ chiral-polarity-bias closure (sibling Layer 4 work feeding from THEO-SD-CHIR-2 substrate handle $\chi/6$ on the qDP/eDP sector). The sketch surfaces structural considerations for each venue and recommends Venue (b) per PD-004 guidance, with Venue (c) joint-Layer-4 framing as a structurally efficient option to consider.

Anti-priority: do NOT begin substantive Layer 4 derivation work before the route and venue decisions are made. The sub-claim decomposition (§3) and foundational input enumeration (§1.3) are independent of route/venue choice and can be developed in parallel; the actual derivation work depends on which route gets the green light.

---

## §1 Setup: the Layer 4 closure question

### §1.1 What is to be derived

OPEN-FP-SF-2-CHIR's one-line statement (from `research_frontier.md`):

> Derive from CPP substrate primitives the 100\% V--A coupling structure of $W^\pm$ gauge boson interactions with fermions at the massless helicity limit.

The structural picture at SF-2 v1.0 (preserved at v3.0+ trajectory pickup):

- **At finite mass**: the bracelet's $D_6$ alternating-polarity structure (SF-2 v1.0 PROP-SF-2-5; the 120°/240° phase bias of the bracelet's six vertices) produces a 75\% left-handed preference for the released centroid charge in $W^\pm$-mediated processes. This is the standard SM Michel parameter $\rho = 3/4$ from the V--A coupling structure at finite mass.
- **At the massless helicity limit**: the kinematic enhancement at zero mass produces 100\% LH preference (standard SM result).

Both claims at SF-2 v1.0 sit at *structural-preference level* — supported by the bracelet's $D_6$ phase-structure observation but not at theorem-level rigor. The Layer 4 closure target is to **lift both claims to theorem level via the continuum-limit Yang-Mills EFT projection**, using the substrate handle $|M^W| = \chi/6$ from Capotauro v2.0 as the substrate-physics input the v1.0 derivation was missing.

### §1.2 What changed at Capotauro v2.0 (substrate handle now in hand)

At SF-2 v1.0 SHIP, the V--A coupling claim sat as "structural preference, not theorem-level" because the substrate-level chirality magnitude was not yet derived. The Patch 0367 sketch (`W0_neutrino_scattering_centroid_decoupling.md`) captured Thomas's W$^0$ neutrino scattering centroid-decoupling insight as a candidate substrate-mechanism closure path but at "captured insight" level only (Layers A/B/C operational development required first).

Capotauro v2.0's Reading C trajectory (Sessions 87--133) delivered the substrate handle as a theorem-level derivation:

- **THEO-SD-CHIR-1** (Cross-Sector Substrate Chirality Unification Theorem; K3-doublet $\leftrightarrow$ W-bracelet pair; registered Session 132 Patch 0434): $|M^W| = |M^{K3}| = \chi/6 = \phi^{-3}/6 \approx 0.0394$.
- The W-bracelet stabilizer $D_6 = S_3 \times \mathbb{Z}_2$ where $\zeta^W$ is the icosahedral-center inversion in 4D ambient $\mathbb{R}^4$ (the central element $r^3$ of the bracelet's dihedral $D_6$ via Petrie-polygon embedding in the first-shell icosahedron at the host 600-cell vertex).
- The matter-doublet basis spans 2D subspace of $E_2 \oplus E_1$ irreps of $D_6$ via Wigner-Eckart factorization analog of K3 paper §5.3--§5.4.
- The chirality operator $\Cchi^W \in B_2(D_6)$ with non-vanishing matrix element via the $\sigma_1^W \zeta^W$-EVEN pairing convention; matrix element factorization at full Layer 3 rigor.

This delivers the substrate-physics input that SF-2 v1.0's continuum-EFT derivation needed but did not have. The Layer 4 closure now reduces to: **show that the Yang-Mills EFT projection of $|M^W| = \chi/6$ to observable scales produces the V--A coupling structure with Michel $\rho = 3/4$ at finite mass and $100\%$ LH at massless helicity limit.**

### §1.3 Foundational input enumeration

The Layer 4 closure inherits the following foundational inputs (FIs). These distinguish "given to closure" (theorem-level results from prior CPP-corpus work) from "derived in closure work" (the Layer 4 deliverable).

**Substrate-level inheritance (Layer 3 results in hand)**:

- **FI-CHIR-1**: Substrate primitive 4D direction $\hat{n}$ in ambient $\mathbb{R}^4$ at vertex-aligned Reading C (FI-C-RC-1 + FI-C-RC-2 from Capotauro v2.0).
- **FI-CHIR-2**: Substrate chirality magnitude $|\chi| = \phi^{-3}$ derived from perturbative-distance-ratio constraint on $\hat{n}$-induced edge perturbations (replaces v1.0 FI-C-9 free-magnitude postulate).
- **FI-CHIR-3**: Substrate residual symmetry $H_3 = I_h$ at host 600-cell vertex (Theorem stab\_Hfour at Capotauro v2.0).
- **FI-CHIR-4**: W-bracelet substrate chirality matrix element $|M^W| = \chi/6$ at full Layer 3 rigor (THEO-SD-CHIR-1; Capotauro v2.0 §17 derivation chain).

**Continuum-EFT inheritance (Layer 3/4 architecture in hand)**:

- **FI-CHIR-5**: SF-2 v1.0 Theorem 4.2 (THEO-SF-2-1) W-bracelet 1200-orbit under $H_4$ action with $D_6$ stabilizer; cage-shape uniqueness at theorem level.
- **FI-CHIR-6**: SF-2 v1.0 Theorem 8.3 (THEO-SF-2-5 / thm:YM\_EFT) Yang-Mills EFT continuum-limit at proof-outline level — the discrete-substrate-to-continuum-EFT bridge architecture inherited from EW-5.
- **FI-CHIR-7**: SF-2 v1.0 PROP-SF-2-5 W$^0$ catalyst framework reorganization probabilities — the 75\% LH preference from bracelet 120°/240° phase bias at structural-preference level.
- **FI-CHIR-8**: $SU(2)_L$ algebra inherited from binary icosahedral group $\Gamma$ at theorem level via THEO-SF-2-5 chain (EW-5 inheritance; SF-2 v1.0 Theorem 7.1 / thm:SU2L).

**Continuum kinematics inheritance (standard SM machinery)**:

- **FI-CHIR-9**: Standard Model V--A coupling structure at the continuum gauge-theory level (gauge-invariance of Yang-Mills EFT plus the chirality structure of fermion bilinears under $SU(2)_L$); the substrate-level magnitude needs to project correctly to this continuum content.
- **FI-CHIR-10**: Michel parameter $\rho = 3/4$ as the standard SM tree-level result for the V--A structure of muon decay (standard PDG kinematic content; the substrate-level derivation needs to recover this).

The FI count (10) is intentionally parallel to the Capotauro v1.0 FI inventory (FI-C-1 through FI-C-10); the v2.0 addition of FI-C-RC-1 + FI-C-RC-2 brought the Capotauro inventory to 12. The Layer 4 closure should aim for a comparable FI inventory — explicit, finite, separately reviewable.

### §1.4 Layer architecture per PD-004

Per PD-004 (Publication Pathway and Layered Rollout Strategy, 14 May 2026), the CPP programme operates at five strategic layers:

- **Layer 1**: Mathematical-combinatorial geometry papers (600-cell, $H_4$, binary icosahedral, polytope/group structure as standalone mathematical contributions).
- **Layer 2**: Symmetry / orbit classification papers (orbit/stabilizer arguments at symmetry-mathematical level).
- **Layer 3**: Discrete substrate phenomenology papers (physical predictions from the discrete substrate with empirical content).
- **Layer 4**: Separate continuum-limit development papers (continuum-EFT bridge as dedicated mathematical-physics problem).
- **Layer 5**: Eventual EFT bridge work (continuum-limit connects to SM EFT structure with explicit Lagrangian matching).

OPEN-FP-SF-2-CHIR closure is unambiguously **Layer 4 work**: it requires the discrete-substrate-to-continuum-EFT projection to be developed beyond the SF-2 v1.0 proof-outline level. Capotauro v2.0's substrate-handle derivation (THEO-SD-CHIR-1) is itself **Layer 3 substrate phenomenology** — it derives the discrete matrix element on the substrate but does not project to continuum observables. The Layer 4 projection from $|M^W| = \chi/6$ to V--A coupling structure at observable scales is the missing link.

PD-004 explicitly states: "This work does *not yet exist* as a dedicated paper. The proof-outline content in SF-2 §8.3 (Theorem 8.3, Yang-Mills EFT emergence) is the current best statement, but the full continuum derivation is registered as future work." And: "Dedicated papers are required — this cannot be folded into flagship phenomenology papers." Both statements are direct guidance for the venue question (§4 below).

---

## §2 Two-route framing

### §2.1 Route (i): canonical continuum-EFT Layer 4 derivation

The canonical Layer 4 path. Architecture:

1. **Substrate handle in hand**: $|M^W| = \chi/6$ from Capotauro v2.0 THEO-SD-CHIR-1, with explicit Wigner-Eckart factorization on the W-bracelet's $D_6 = S_3 \times \mathbb{Z}_2$ stabilizer.
2. **Yang-Mills EFT continuum projection**: extend SF-2 v1.0 Theorem 8.3 (thm:YM\_EFT) proof outline to a full continuum-limit derivation, with the substrate chirality matrix element $|M^W|$ serving as the substrate-physics input the v1.0 proof outline registered as missing.
3. **V--A coupling structure**: show that the continuum-limit projection produces the standard SM V--A structure of the $W^\pm$ gauge-boson coupling to fermion bilinears, with the substrate-level $\chi/6$ magnitude controlling the strength of the chirality bias.
4. **Kinematic projections**: recover Michel $\rho = 3/4$ at finite mass and $100\%$ LH at massless helicity limit as kinematic consequences of the V--A coupling structure at observable scales.

**Strengths of Route (i)**: substrate handle is already at Layer 3 rigor; continuum-EFT architecture is already at proof-outline level (THEO-SF-2-5); the bridge is structurally clear (substrate matrix element $\rightarrow$ effective coupling $\rightarrow$ kinematic projection). The work is mathematically demanding (continuum-limit derivations are technically hard) but architecturally well-defined.

**Risks of Route (i)**: the continuum-limit derivation may surface unanticipated technical obstructions (e.g., regularization-scheme dependence, Lorentz-invariance recovery subtleties, gauge-fixing constraints). The Capotauro v2.0 §13.6 "On the dynamical engine beneath the structural claim" discussion explicitly registers Layer 1 dynamical-engine work as the deepest open work of the programme; Layer 4 continuum-EFT derivation depends in subtle ways on Layer 1 dynamics that have not yet been derived.

### §2.2 Route (ii): substrate-mechanism via centroid-decoupling (Patch 0367 sketch)

The substrate-mechanism alternative. Architecture:

1. **Substrate-mechanism premise**: Thomas's Patch 0367 W$^0$ neutrino scattering insight — a spinning DP or h-tet passing through the W$^0$ bracelet centroid loses its coupling with the DP Sea for an instant, then emerges with direction determined by post-centroid DP Sea allowed directions. The centroid-decoupling mechanism is the substrate-level analog of "free propagation through a chirality-active region."
2. **$D_6$-stabilizer imprint**: if the bracelet's $D_6$ stabilizer imprints chirality-specific anisotropy on the post-emergence direction distribution (Layer B of the Patch 0367 sketch's three-layer development plan), the substrate-mechanism produces V--A-like angular dependence directly from substrate primitives without invoking continuum-EFT projection.
3. **Bridge to V--A phenomenology**: Layer C of the Patch 0367 sketch — either reproduce SM V--A as a derived consequence of centroid-decoupling, or predict deviations from V--A at high precision that constitute a substrate-mechanism falsifier distinct from the continuum-EFT route.

**Strengths of Route (ii)**: substrate-mechanism derivation is closer to CPP's foundational commitment (mathematical descriptions are not themselves physical mechanisms; the substrate-mechanism story is the physical-mechanism layer); avoids the technical difficulties of continuum-limit derivations; produces a CPP-specific empirical prediction (discrete scattering angles, hexagonal anisotropy from $D_6$-stabilizer imprint) that is testable against precision neutrino-scattering data.

**Risks of Route (ii)**: the Patch 0367 sketch is at "captured insight" level only; Layers A (operational definition of centroid passage and decoupling), B (quantification of post-emergence direction selection), and C (bridge to V--A phenomenology) all require substantive development before paper integration. The development path is longer and less architecturally certain than Route (i)'s continuum-EFT canonical path.

### §2.3 Route comparison and recommendation

| Aspect | Route (i) Continuum-EFT | Route (ii) Substrate-mechanism |
|---|---|---|
| Substrate input | Inherits $|M^W| = \chi/6$ from THEO-SD-CHIR-1 directly | Develops new substrate mechanism (centroid-decoupling) |
| Architecture | Proof-outline-level inheritance from THEO-SF-2-5 | Layers A/B/C development required first |
| Closure rigor | Theorem-level (continuum-limit derivation) | Substrate-mechanism-level (substrate primitives) |
| Empirical match | Recovers standard SM V--A | Predicts CPP-specific angular distributions |
| Session budget | 6--10 sessions (estimate) | 10--15 sessions (estimate, with Layer A--C development) |
| Technical risk | Continuum-limit subtleties | Layer A/B/C operational definitions |
| Falsification | Capotauro Falsifier 6 activates | New substrate-mechanism falsifier |

**Recommendation**: pursue **Route (i) as primary closure path** for OPEN-FP-SF-2-CHIR closure. Reasons:

1. The substrate handle $|M^W| = \chi/6$ is in hand at full Layer 3 rigor from THEO-SD-CHIR-1; this is precisely the input the continuum-EFT Layer 4 derivation needs.
2. The continuum-EFT architecture is already at proof-outline level (THEO-SF-2-5); Route (i) builds on existing scaffolding rather than developing new substrate-mechanism architecture from scratch.
3. PD-004 explicitly identifies Layer 4 continuum-limit work as "the single biggest reality constraint on CPP-as-physics"; closure of one Layer 4 piece (V--A coupling) advances the programme's Layer 4 maturity broadly.
4. Route (ii) substrate-mechanism work would still benefit from Route (i)'s continuum-EFT projection as a cross-validation target — if both routes converge on the same V--A coupling structure, the closure is doubly supported; if they diverge, the divergence is itself empirically informative.

Route (ii) should remain registered as a **cross-validation candidate** for future-window work (post-Route-(i) closure), with the Patch 0367 sketch preserved as the canonical capture of Thomas's substrate-mechanism insight.

---

## §3 Sub-claim decomposition under Route (i)

The Layer 4 closure under Route (i) decomposes into four sub-claims, paralleling the SF-4 v3.0 $\alpha$-exponent closure (Sessions 62--67, four sub-claims (a)(b)(c)(d)) and SF-4 v2.0 Picture A axiomatic closure (Sessions 55--60, three sub-claims (a)(b)(c)) precedents.

### §3.1 Sub-claim (a): bridge from substrate handle to effective Lagrangian

**Statement**: the substrate-level chirality matrix element $|M^W| = \chi/6$ from THEO-SD-CHIR-1 projects to a chirality-sensitive coupling in the continuum-limit effective Lagrangian of the W$^\pm$ gauge bosons, with the substrate magnitude $\chi/6$ controlling the strength of the chirality bias in the continuum gauge-coupling structure.

**Closure architecture**: identify the entry point in the Yang-Mills EFT continuum-limit derivation (THEO-SF-2-5 / thm:YM\_EFT) where the substrate chirality matrix element enters the effective gauge-coupling data. The W-bracelet's $D_6 = S_3 \times \mathbb{Z}_2$ stabilizer carries the substrate chirality via the $\zeta^W$ = icosahedral-center inversion in 4D; the continuum-limit projection of $\zeta^W$-EVEN vs $\zeta^W$-ODD substrate states should produce LH vs RH fermion couplings in the continuum EFT.

**Required infrastructure**: explicit form of the SF-2 v1.0 Theorem 8.3 (thm:YM\_EFT) proof-outline mapping, with the substrate matrix elements identified as inputs to the continuum-limit gauge-coupling data. This is the load-bearing technical step of Layer 4 closure work.

**Estimated session count**: 2--3 sessions.

### §3.2 Sub-claim (b): finite-mass Michel parameter $\rho = 3/4$ from substrate handle

**Statement**: the standard SM Michel parameter $\rho = 3/4$ (the V--A structure of muon decay at finite mass) emerges as a derived kinematic consequence of the continuum-EFT V--A coupling structure projected from the substrate handle, with the $75\%$ LH preference (per SF-2 v1.0 §sec:dm\_muon) recovered at theorem level.

**Closure architecture**: given sub-claim (a)'s bridge from substrate handle to continuum-EFT chirality-sensitive coupling, apply the standard SM kinematic-projection machinery for muon decay to extract $\rho = 3/4$. The kinematic projection is standard SM content; the substrate-level derivation provides the V--A coupling structure as input that the standard SM derivation takes as given.

**Empirical test**: $\rho = 0.74979 \pm 0.00026$ (PDG 2024) is matched to the SM prediction $\rho = 3/4$ at the $10^{-4}$ level. The substrate-level derivation must recover this match to confirm the bridge from sub-claim (a) is correctly delivering the V--A coupling structure at the observable level.

**Estimated session count**: 2--3 sessions.

### §3.3 Sub-claim (c): massless helicity limit $100\%$ LH preference

**Statement**: the $100\%$ LH preference at the massless helicity limit (per SF-2 v1.0 abstract and §sec:dm\_muon) emerges as a derived kinematic consequence of the V--A coupling structure at zero mass, with kinematic enhancement at the helicity limit producing pure-LH coupling.

**Closure architecture**: extend sub-claim (b)'s kinematic projection to the massless limit. The transition from $75\%$ LH at finite mass to $100\%$ LH at zero mass is a kinematic enhancement at the helicity limit that is standard SM content; the substrate-level derivation must produce the same transition from the same V--A coupling structure as sub-claim (b).

**Empirical test**: the massless-helicity-limit prediction is consistent with the observed left-handedness of neutrinos at all measured energies (no observed right-handed neutrino at SM-relevant scales).

**Estimated session count**: 1--2 sessions.

### §3.4 Sub-claim (d): Capotauro Falsifier 6 activation

**Statement**: closure of sub-claims (a), (b), (c) at theorem level activates **Capotauro v2.0 Falsifier 6** (per the §13.4 falsifier ledger) as a sharp empirical falsifier of the OPEN-SD-CHIR-PRIMITIVE umbrella's electroweak-leg claim, with explicit prediction-to-observation mapping.

**Closure architecture**: identify the precise empirical content that Falsifier 6 tests (likely the V--A coupling strength at observable scales as a function of the substrate-level handle $\chi/6$; or the energy-dependence of the V--A coupling that emerges from the substrate-to-continuum projection); document the falsifier as theorem-mapped via the closure chain (a)+(b)+(c).

**Empirical content**: deferred to closure-chain construction; the precise empirical handle that becomes operative depends on the bridge identified in sub-claim (a).

**Estimated session count**: 1 session.

---

## §4 Venue question: where Layer 4 closure work lands

Three candidate venues are surfaced by the existing programme architecture. Each carries different implications for the closure trajectory.

### §4.1 Venue (a): SF-2 v2.0+ flagship-paper extension

**Architecture**: extend the SF-2 v1.0 paper to v2.0+ with new Layer 4 sections (extending §8.3 Yang-Mills EFT emergence to full continuum-limit derivation, plus new Layer 4 sub-sections under §5 W$^\pm$ catalyst framework for the V--A projection). The v1.0 paper's calibrated mass-formula PARTIAL CLOSURE is preserved; v2.0+ adds Layer 4 theorem-level closure for the V--A coupling specifically.

**Pattern precedent**: Capotauro v2.0 v1.0 SHIPPED 19 May 2026 (Session 135) extended Capotauro v1.0 within the same flagship paper, adding three new theorems (THEO-SD-CHIR-1, THEO-SD-CHIR-2) and twelve foundational inputs (FI-C-1 through FI-C-10 + FI-C-RC-1 + FI-C-RC-2). The within-flagship extension pattern is established as workable.

**Strengths**: preserves SF-2's narrative coherence as the electroweak cage-boson unification flagship; Layer 4 work is presented as the natural extension of v1.0's Layer 2 + Layer 3 architecture; readers see the full closure story in one paper.

**Risks**: PD-004 explicitly states that Layer 4 work "cannot be folded into flagship phenomenology papers" — Venue (a) directly contradicts PD-004 guidance. The reasoning in PD-004 is that each layer's audience is different (Layer 2/3 readers are phenomenologists; Layer 4 readers are mathematical physicists working on continuum-EFT bridges), and folding both into one paper makes the paper externally indefensible at the layer boundary.

### §4.2 Venue (b): dedicated Layer 4 continuum-EFT paper per PD-004

**Architecture**: create a new dedicated paper at `flagship_papers/electroweak/sf-2-layer-4-continuum.tex` (or equivalent venue; naming TBD) focusing exclusively on the Layer 4 continuum-EFT derivation. The paper inherits substrate-level results from Capotauro v2.0 and SF-2 v1.0 at theorem level; develops the continuum-limit projection as the dedicated technical content; closes OPEN-FP-SF-2-CHIR plus potentially OPEN-FP-SF-2-loopfactor and other Layer 4 OPEN-FP-SF-2-* entries that share the continuum-EFT closure infrastructure.

**Pattern precedent**: SF-4 v1.0 SHIP (Session 54) is a partial-closure flagship paper; SS-9 v1.0 SHIP (Session 32) is a conditional-theorem closure paper. Dedicated Layer 4 paper would follow the conditional-closure-paper framework established by SF-4 and SS-9, with explicit foundational-input enumeration (the 10 FIs of §1.3 here).

**Strengths**: aligns with PD-004 guidance ("dedicated papers are required"); separately defensible to the Layer 4 audience (mathematical physicists working on continuum-EFT bridges); avoids contamination of SF-2 v1.0's Layer 2/3 narrative with Layer 4 technical content.

**Risks**: introduces a new paper in the programme catalog; requires the same documentation suite as other flagship papers (Tier-4 reasoning, development transcripts, four-tier discipline); session count for documentation overhead is non-trivial.

### §4.3 Venue (c): joint Layer 4 paper with SM-2 v2.0+

**Architecture**: a joint Layer 4 continuum-EFT paper closing both OPEN-FP-SF-2-CHIR (electroweak V--A coupling from W-bracelet substrate handle THEO-SD-CHIR-1) and SM-2 v2.0+ chiral-polarity-bias closure (electromagnetic handedness from qDP/eDP substrate handle THEO-SD-CHIR-2). Both substrate handles are $|M| = \chi/6 \approx 0.0394$; both Layer 4 projections take the same form (substrate matrix element $\rightarrow$ effective continuum coupling $\rightarrow$ observable kinematic structure). A joint paper would close two OPEN-FP entries simultaneously and would be the most structurally efficient route to broad Layer 4 maturity.

**Pattern precedent**: SF-4 v4.0 SHIP (Session 72) executed the *first cross-sector closure in CPP* — OPEN-FP-SF-4-2 and SM-5 op:nu\_id closed jointly via a single derivation chain. The methodological pattern (cross-sector entanglement turned into structural advantage when foundational inputs of one closure determine the closure in another sector) directly templates Venue (c) work.

**Strengths**: closes two OPEN-FP entries in one paper; structurally efficient at the trajectory level; SF-4 v4.0 precedent demonstrates the methodological pattern works; the cross-sector unification under OPEN-SD-CHIR-PRIMITIVE umbrella is foregrounded as the paper's structural identity claim.

**Risks**: SM-2 v2.0+ has not yet been drafted; joint paper venue would require SM-2 v2.0+ scoping work to land first or concurrently; technical risk of joint paper failing one of two closures (cross-sector entanglement cuts both ways — entanglement that helps closure also amplifies failure risk).

### §4.4 Recommendation

**Recommended venue**: **Venue (b)** dedicated Layer 4 continuum-EFT paper per PD-004 guidance.

Reasoning:

1. PD-004 explicit guidance: "Dedicated papers are required — this cannot be folded into flagship phenomenology papers." Following PD-004 preserves programme-wide architectural discipline.
2. Layer 4 work is technically distinct from Layer 2/3 phenomenology; mixing layers in one paper makes the paper externally indefensible at the layer boundary.
3. Dedicated Layer 4 paper can later be extended to a joint Layer 4 paper with SM-2 v2.0+ if cross-sector closure becomes structurally available (Venue (c) is reachable from Venue (b) but not from Venue (a)).
4. SF-2 v1.0 remains the canonical reference for the cage-shape uniqueness theorems and the W$^0$ catalyst framework; SF-2's narrative is not disrupted by Venue (b).

**Recommended deferred option**: if Venue (c) becomes structurally available (SM-2 v2.0+ scoping work lands within 1--2 sessions of the Layer 4 paper drafting start), promote from Venue (b) to Venue (c) joint-Layer-4 paper. The joint paper would be the structurally optimal outcome — closes two OPEN-FP entries with shared derivation infrastructure — and would establish a second cross-sector closure pattern in CPP after SF-4 v4.0's first instance.

**Not recommended**: Venue (a) (SF-2 v2.0+ extension) contradicts PD-004; would create a paper that is internally inconsistent at the layer boundary; precedent risk (subsequent Layer 4 work elsewhere in the corpus would be pulled toward within-flagship extension instead of dedicated paper, propagating the architectural error).

---

## §5 Cross-sector dependencies

### §5.1 Capotauro v2.0 substrate handle

THEO-SD-CHIR-1 (Cross-Sector Substrate Chirality Unification Theorem; K3-doublet $\leftrightarrow$ W-bracelet pair; registered Patch 0434 Session 132) is the load-bearing substrate-level input. The theorem's derivation chain is at full Layer 3 rigor:

- Substrate-locality: Theorem `thm:local_ih_preservation` at Capotauro v2.0 §13 (local-$I_h$-preservation at host vertex under vertex-aligned Reading C).
- Cage-shell factor: Schur orthogonality on the W-bracelet's $D_6$ stabilizer, $|M_\perp^W| = d_E/V_{\text{cage}} = 2/12 = 1/6$ (Finding C-W41 at §15; refined interpretation in §17.10 as cage-shell averaging on shared icosahedral cage).
- Pairing-convention: $\sigma_1^W \zeta^W$-EVEN pairing on bracelet's $D_6 = S_3 \times \mathbb{Z}_2$ with $\zeta^W$ = icosahedral-center inversion in 4D (Finding C-W43 at §17; full Layer 3 matrix element factorization analog of K3 paper §5.3--§5.4).

These three elements collectively constitute the substrate-physics handle $|M^W| = \chi \cdot (1/6) = \chi/6 = \phi^{-3}/6 \approx 0.0394$ that Layer 4 closure inherits as FI-CHIR-4 (§1.3 above).

### §5.2 SM-2 v2.0+ chiral-polarity-bias parallel

THEO-SD-CHIR-2 (qDP/eDP Sector Substrate Chirality Closure Theorem; registered Patch 0440 Session 133) delivers the parallel substrate handle for the qDP/eDP sector: $|M^{qDP}| = \chi/6$ at full Layer 3 rigor via the three-step closure pattern (substrate-locality + cage-shell factor + combined-$CP$ pairing convention). The Layer 4 continuum-EFT projection of THEO-SD-CHIR-2 to the SM-2 v2.0+ chiral-polarity-bias EFT continuum-limit calculation is the sibling Layer 4 closure target that Venue (c) joint-paper framing would address jointly with OPEN-FP-SF-2-CHIR.

The two sibling Layer 4 projections share substantial infrastructure: same substrate-handle magnitude $\chi/6$, same continuum-EFT bridge architecture (Yang-Mills EFT for W$^\pm$; gauge-EM EFT for qDP/eDP), same kinematic-projection machinery (kinematic enhancement at helicity limits, finite-mass kinematic structure). The structural efficiency argument for Venue (c) is strong.

### §5.3 EW-5 Yang-Mills EFT inheritance

SF-2 v1.0 inherits three theorems from EW-5 at theorem level (per §sec:su2l, §sec:nexus\_gauge, §sec:YM\_EFT\_thm):

- THEO-EW-6 ($SU(2)_L$ from $\Gamma$): the binary icosahedral group $\Gamma$ provides the $SU(2)_L$ gauge algebra at theorem level.
- THEO-EW-7 (Nexus gauge invariance): the substrate-level origin of local gauge invariance via Nexus phase-fixing.
- THEO-EW-8 / thm:YM\_EFT (Yang-Mills EFT limit): the continuum-limit recovery of standard $SU(2)_L \times U(1)_Y$ Yang-Mills EFT from CPP discrete substrate dynamics, at proof-outline level.

Layer 4 closure of OPEN-FP-SF-2-CHIR depends on lifting THEO-EW-8 from proof-outline level to full continuum-limit derivation (or, more narrowly, lifting the V--A piece of the continuum-limit derivation to theorem level given the substrate handle as input). The full lift of THEO-EW-8 is a much larger programme-level undertaking than OPEN-FP-SF-2-CHIR alone; the closure work here should be scoped to the V--A piece specifically, with the full continuum-limit derivation registered as future Layer 4 work beyond OPEN-FP-SF-2-CHIR.

---

## §6 Session budget and trajectory estimate

Per the SF-4 v3.0 $\alpha$-closure precedent (Sessions 62--67, 6 sessions for four sub-claims plus paper integration) and SF-4 v4.0 cross-sector closure precedent (Sessions 68--73, 6 sessions for three sub-claims plus paper integration), the OPEN-FP-SF-2-CHIR Layer 4 closure trajectory under Route (i) Venue (b) is estimated as:

- **§3.1 Sub-claim (a)** (bridge from substrate handle to effective Lagrangian): 2--3 sessions.
- **§3.2 Sub-claim (b)** (finite-mass Michel $\rho = 3/4$): 2--3 sessions.
- **§3.3 Sub-claim (c)** (massless helicity limit $100\%$ LH): 1--2 sessions.
- **§3.4 Sub-claim (d)** (Capotauro Falsifier 6 activation): 1 session.
- **Dedicated paper drafting** (Venue (b); v0.1 outline + v0.2--v0.5 substantive content + v0.6--v0.9 reviewer cycle + v1.0 SHIP): 4--6 sessions (estimate based on SF-2 v0.1 → v1.0 trajectory at Sessions 81--83 = 3 sessions for the paper itself plus reviewer cycles, with Layer 4 work likely longer than Layer 2/3 SF-2 v0.x drafting due to higher technical complexity).
- **Programme-level registration** (research\_frontier.md + theorem-registry.md + master\_glossary.md + paper\_catalog.md + INDEX.md updates + handover): 1--2 sessions.

**Total estimated session count for full theorem-level closure of OPEN-FP-SF-2-CHIR at v1.0 SHIP**: **11--17 sessions** (likely in the 12--14 range based on precedents).

This is comparable to SF-4 v3.0 $\alpha$-closure (6 sessions for sub-claim work + 1 session for v3.0 paper integration = 7 sessions; but SF-4 v3.0 was within-flagship extension, not dedicated new paper) and Capotauro v2.0 Reading C trajectory (Sessions 87--133 = ~46 sessions; but Capotauro Reading C trajectory was a substrate-physics derivation campaign with multiple Q-questions, not a Layer 4 continuum-EFT projection).

If Venue (c) joint-paper framing is adopted (parallel SM-2 v2.0+ closure), session count increases to **15--25 sessions** for joint paper covering both closures; closes two OPEN-FP entries instead of one.

---

## §7 Forward queue and anti-priorities

### Forward queue priorities

**Priority 1 (immediate)**: Thomas's review of this scoping sketch and decision on:

(a) **Route choice**: Route (i) continuum-EFT canonical (recommended) vs. Route (ii) substrate-mechanism via centroid-decoupling. Default to Route (i) unless Thomas surfaces a substantive reason to pursue Route (ii) first.

(b) **Venue choice**: Venue (a) SF-2 v2.0+ extension vs. Venue (b) dedicated Layer 4 paper per PD-004 (recommended) vs. Venue (c) joint Layer 4 paper with SM-2 v2.0+ (recommended deferred option if SM-2 v2.0+ scoping is available).

**Priority 2 (substantive work, post-route/venue decision)**: §3.1 Sub-claim (a) bridge from substrate handle to effective Lagrangian. This is the load-bearing technical step of Layer 4 closure work; once route/venue decisions are in hand, sub-claim (a) closure is the natural first substantive patch. Estimated 2--3 sessions.

**Priority 3 (background)**: SM-2 v2.0+ scoping at sketch level (parallel substrate-handle Layer 4 projection from THEO-SD-CHIR-2); enables Venue (c) joint-paper promotion if structurally efficient.

### Anti-priorities

**Do NOT begin substantive Layer 4 derivation work** before route/venue decisions are made. The sub-claim decomposition (§3) and foundational input enumeration (§1.3) are independent of route/venue choice and can be reviewed without commitment.

**Do NOT skip the venue decision** and default to within-flagship SF-2 v2.0+ extension. The contradiction with PD-004 is structural; venue (a) creates precedent-risk for subsequent Layer 4 work elsewhere in the corpus.

**Do NOT pursue Route (ii) substrate-mechanism via centroid-decoupling as primary closure path** unless Thomas surfaces a substantive reason to do so. Route (ii) Layers A/B/C development is substantively interesting but is earlier-stage than Route (i)'s continuum-EFT canonical path; the substrate handle inheritance from THEO-SD-CHIR-1 is the cleaner input for Layer 4 work.

**Do NOT modify SF-2 v1.0 paper text** (`flagship_papers/electroweak/sf-2_electroweak.tex`) during Layer 4 closure work under Venue (b). SF-2 v1.0 is SHIPPED at v1.0 with .tex source frozen per the SS-9 v1.0 SHIP precedent (only post-external-feedback v1.x revisions modify the .tex source). Layer 4 closure work under Venue (b) lands in a new dedicated paper, leaving SF-2 v1.0 untouched.

**Do NOT mix Layer 4 closure work with sub-shell-physics work** (the residual 52\% empirical gap in the OPEN-SS-32 ↔ U-shape thread, from the SS-9 v1.0 SHIP forward queue) or other unrelated OPEN-FP-SF-2-* entries (OPEN-FP-SF-2-EWSB, OPEN-FP-SF-2-loopfactor, OPEN-FP-SF-2-shelldens, OPEN-FP-SF-2-chaincomp, OPEN-FP-SF-2-$\eta$). These are independent closure trajectories; mixing them in the Layer 4 closure paper would dilute the paper's focus.

---

## §8 Status update at scoping sketch creation

**Patch**: 0482 (this patch; scoping sketch creation).

**Date**: 19 May 2026 (Session 136 opening, post-Session 135 Capotauro v2.0 v1.0 SHIPPED).

**Programme state changes**:

1. **OPEN-FP-SF-2-CHIR trajectory PROMOTED** from "registered open frontier at SF-2 v1.0 SHIP; closure path identified" (Patch 0370, Session 83) to **"v3.0+ Layer 4 closure trajectory OPENED at scoping level"** (this patch). Status updated in `research_frontier.md` with this patch's Updated entry.
2. **PH-OPEN-FP-SF-2-CHIR.md problem-history file UPDATED** with v3.0+ trajectory pickup entry registering substrate-handle availability from Capotauro v2.0 THEO-SD-CHIR-1 and scoping-sketch creation.
3. **No theorems registered** (scoping work is at Layer 1/Layer 2 epistemic status; theorem-level closure occurs at sub-claim (a)+(b)+(c) closure, estimated 11--17 sessions out).
4. **No predictions registered** (scoping is forward-planning, not new physics; the substrate-level $|M^W| = \chi/6$ prediction is already registered as inherited from THEO-SD-CHIR-1).
5. **No falsifiers registered as new** (Capotauro v2.0 Falsifier 6 already exists in the §13.4 ledger; this sketch identifies its activation as Layer 4 closure consequence rather than registering a new falsifier).
6. **No conjecture registrations**.
7. **Problem counts UNCHANGED** (OPEN-FP-SF-2-CHIR was already registered at SF-2 v1.0 SHIP).

**Files modified at Patch 0482**:

- `flagship_papers/electroweak/sketches/SF-2_chir_layer4_closure.md` (NEW; this file; ~450 lines).
- `research_frontier.md` (Last-updated header prepended; OPEN-FP-SF-2-CHIR Status field appended with v3.0+ trajectory opening).
- `problem_histories/PH-OPEN-FP-SF-2-CHIR.md` (v3.0+ trajectory pickup entry appended).

**Epistemic status**: Layer 1 / Layer 2 (scoping + sub-claim decomposition + foundational input enumeration); Layer 3 closure work begins at sub-claim (a) once route/venue decisions are in hand.

**Methodological observation — scoping sketch precedes derivation work**: this opening sketch establishes the closure-trajectory architecture before substantive derivation work begins. The pattern mirrors SF-4 v3.0 $\alpha$-closure (Session 62 working sketch at Patch 0323 with §0 firewall + §1 setup + §2 four-sub-claim decomposition preceded Session 63--66 derivation work) and SF-4 v4.0 cross-sector closure (Session 68 working sketch at Patch 0329 with §0 firewall + §1 setup + §2 three-sub-claim decomposition preceded Session 69--72 derivation work). The opening sketch's value is architectural clarity: route/venue decisions, sub-claim decomposition, foundational input enumeration, session budget estimates all become explicit and reviewable at sketch level before they get embedded in derivation work where they are harder to surface or revise.

**Forward action for Thomas**: review this sketch and respond on:

1. Route choice (recommend Route (i) continuum-EFT canonical; alternate Route (ii) substrate-mechanism is registered as cross-validation candidate for future-window work).
2. Venue choice (recommend Venue (b) dedicated Layer 4 paper per PD-004; deferred option Venue (c) joint Layer 4 paper with SM-2 v2.0+ if SM-2 v2.0+ scoping work lands concurrently; not recommended Venue (a) SF-2 v2.0+ extension contradicts PD-004).
3. Session budget acceptance or revision (current estimate 11--17 sessions for full theorem-level closure of OPEN-FP-SF-2-CHIR at v1.0 SHIP under Route (i) + Venue (b); 15--25 sessions for joint paper under Venue (c)).
4. Anti-priority confirmation (do not modify SF-2 v1.0 .tex source; do not mix Layer 4 closure with sub-shell-physics work; do not skip venue decision and default to within-flagship extension).

Upon Thomas's confirmation of route + venue, the next substantive patch (Patch 0483 or later) opens **Sub-claim (a) closure work** — the bridge from substrate handle $|M^W| = \chi/6$ to chirality-sensitive coupling in the continuum-limit effective Lagrangian.

---

*Sketch authored by Claude Opus (Anthropic) under Thomas Lee Abshier's direction, 19 May 2026, Session 136 opening, Patch 0482. Opens the v3.0+ trajectory for OPEN-FP-SF-2-CHIR Layer 4 closure under route + venue decisions pending Thomas's review. Mirrors the Capotauro Reading C scoping sketch pattern (`Capotauro_chiral_mechanism_candidate.md` Sessions 121--133) and the SF-4 v3.0/v4.0 closure sketch patterns (`SF-4_alpha_exponent_closure.md` Sessions 62--67; `SF-4_open_fp_sf_4_2_closure.md` Sessions 68--73).*
