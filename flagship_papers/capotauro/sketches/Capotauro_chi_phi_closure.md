# Capotauro Mechanism Closure: 600-Cell Chirality Activation and CP Violation at Cross-Sector Closure Level

**Working sketch document — Tier-4 reasoning capture per CPP four-tier documentation discipline.**

This document grows monotonically across Sessions 84+ as the Capotauro closure campaign progresses. It captures verbatim reasoning per Tier-4 discipline and is the canonical source for the closure derivation. The Capotauro mechanism is registered programme-side as **OPEN-SM-4** (Research_Frontier.md §1 SM sector, last updated 23 March 2026). It is *also* the candidate venue for cross-sector closure with **OPEN-FP-SF-2-CHIR** (V-A coupling at the massless helicity limit; registered at SF-2 v1.0 SHIP Patch 0370). This sketch targets joint theorem-level closure of both, on the methodological template established by SF-4 v4.0's Composite K3-Cage-Shell Coupling Theorem (Finding β-10, the first cross-sector closure in CPP).

---

## §0 Working-session firewall

Subject to revision. Concepts may be relabeled. Sub-claim decomposition may evolve as understanding develops. The final closure structure is not pre-committed. The χ-value resolution (§2.3, §4.2) and the mechanism-selection (§3) in particular are open and depend on physical-intuition input from Thomas and on first-pass calculational work in subsequent sessions.

The SF-4 OPEN-FP-SF-4-2 closure precedent (Sessions 68–73, Patches 0329–0334) demonstrates the methodological pattern: working sketch document → sub-claim decomposition → theorem-level closure per sub-claim → composite theorem → verification flag discharge → paper integration → programme-level registration. The Capotauro closure follows the same pattern but with an additional layer of cross-sector entanglement (touching SM-4, SM-5, SF-2, and SF-4 simultaneously).

This document is paired with Patch 0367's W⁰ neutrino scattering centroid-decoupling sketch (`flagship_papers/electroweak/sketches/W0_neutrino_scattering_centroid_decoupling.md`), which captures a candidate substrate-level mechanism for chirality emergence. The two sketches are companions: this one is the global-closure document; the centroid-decoupling sketch is the local-mechanism candidate.

---

## §1 Setup

### §1.1 Programme-level labeling housekeeping note

The recent SF-line documentation (Sessions 67–83 SF-4 v3.0/v4.0 and SF-2 v1.0 patches) consistently refers to the cross-sector closure target as "**OP-SM-7d** Capotauro mechanism." `Research_Frontier.md` registry however lists:

- **OPEN-SM-4: Formalise the Capotauro Mechanism** (Status OPEN, Priority HIGH, last updated 23 March 2026) — "Derive the lattice chirality-activation event that establishes χ ≈ φ⁻¹ and produces CP violation." This is the Capotauro mechanism entry. Its `What a solution looks like` field specifies: "Symmetry breaking [600-cell] × ℤ₂ → [600-cell]; derive χ = φ⁻¹; reproduce δ_CP ≈ 195°, sin²θ₁₃ ≈ 0.022, and baryon asymmetry."
- **OPEN-SM-7d: Derive the Koide Phase θ** — a different problem in the lepton-mass sector (charged-lepton Koide phase θ ≈ 132.73°), tied to OPEN-SM-7 (K=2/3) closure and the lepton series.

These are distinct open problems. The recent SF-line shorthand "OP-SM-7d Capotauro" appears to be a propagated labeling error originating in SF-4 v0.4 §6.2 / §11.2 (Patch 0308, Session 48) where the Capotauro mechanism was referenced as the source of TBM corrections for the missing 8/8 prediction (δ_CP), but indexed under the wrong open-problem number. The error then propagated through Sessions 48–83 SF-line documents, including the Research_Frontier.md last-updated headers, the master_glossary.md "Cross-sector closure" entry, the SF-4 v4.0 paper §11.2 outlook, the SF-2 v1.0 paper §13, the development-SM-5.md cross-sector note, the SF-4 anthology chapter "Where Two Problems Met," and the SF-2 anthology chapter "The Bracelet's Catalyst."

**Resolution before paper drafting begins.** Before Capotauro paper drafting opens, the labeling should be cleaned up in one of two ways: (i) rename throughout the SF-line corpus to use OPEN-SM-4 consistently (the correct registry ID); or (ii) confirm an intent-decision that the two registry entries should be merged into a unified "OP-SM-Chiral-and-Koide-Phase" cross-sector target (which I doubt is what was intended, since the Koide phase θ and the CP phase δ_CP are different observable phases on different sectors), and reflect that merger explicitly in the registries. **Default recommendation: rename to OPEN-SM-4 throughout.** This is a 1-patch housekeeping fix that should be done at or before the start of the Capotauro paper drafting campaign, since the paper will name its closure target on every page.

This sketch uses **OPEN-SM-4** throughout to refer to the Capotauro mechanism, in alignment with the canonical Research_Frontier.md registry entry.

### §1.2 The closure target

The Capotauro mechanism is proposed as a substrate-level dynamical event that activates the 600-cell lattice's intrinsic 4D chirality, breaking the racemic [600-cell] × ℤ₂ symmetry of the un-activated lattice down to a single chiral [600-cell] orientation. The proposal originates in Thomas's SM Paper 2 Appendix H (`series_standard_model/papers/SM-2_mass_generation_geometric_hierarchies.tex` §Quark Charge Asymmetry and Capotauro, lines 456–470) and was developed in archived Grok exploratory work covering charge-screening asymmetries, neutrino mixing angles, and full cosmology (`archive/grok-exploratory-SM/p2-charge-screening-and-asymmetries/capotauro-bias.md`, `archive/grok-exploratory-SM/p2-neutrino-mixing-angles/{capotauro-bias.md, delta-cp-phase-derivation.md, lattice-subgroups.md}`, `archive/grok-exploratory-SM/p2-full-cosmology/big-bang-to-capotauro.md`).

**OPEN-SM-4 closure target.** Derive from CPP primitives + named FIs:

**(i) Mechanism existence.** A substrate-level dynamical primitive whose action on the racemic lattice [600-cell] × ℤ₂ selects a single chiral orientation. The mechanism must be CPP-axiomatic (built from A1–A11 + substrate dynamics) and not require new postulates beyond those already in the corpus.

**(ii) Chiral bias magnitude.** Derive the chiral coupling constant χ from the geometry of the 600-cell. The Grok exploratory work proposed χ ≈ φ⁻¹ ≈ 0.618 ("polarity coupling"); the OP-SM-4 sub-problem 2 direct edge-ratio calculation gives χ = φ⁻² ≈ 0.382. These are numerically distinct (factor 1.618 apart) and the discrepancy is registered as the central numerical resolution-target. See §2.3 and §4.2.

**(iii) δ_CP closure.** Reproduce the Standard Model CP-violating phase δ_CP. Current Grok-stage estimate: δ_CP ≈ 180° + (χ × 360°/φ² − 180°) ≈ 195°, matching NuFIT 6.0 preferred central value 195° ± 40°. The proposal is partial — it inherits the 180° "base phase from lattice dual inversion" as motivated but not derived, and uses χ at the explicitly-conflicted value 0.618. Theorem-level closure requires both inputs derived.

**(iv) sin²θ₁₃ closure.** Reproduce the reactor angle sin²θ₁₃ ≈ 0.022. Current Grok-stage estimate: sin²θ₁₃ ≈ φ⁻² / [coefficient] where the coefficient is identified in development-SM-5.md as the target for OP-SM-4 derivation, currently fitted at approximately 1/1.6 = 5/8. Theorem-level closure requires the coefficient derived from 600-cell geometry.

**(v) Baryon asymmetry η_B closure.** Reproduce η_B ≈ 6 × 10⁻¹⁰. Current Grok-stage estimate: not yet computed quantitatively. This is the hardest target (a fifteen-order-of-magnitude scale) and is registered as the most ambitious sub-target. Likely conditional closure at order-of-magnitude rather than precision level for a v1.0 ship.

**(vi) OPEN-FP-SF-2-CHIR closure (cross-sector).** The W bracelet's $D_6$ phase structure delivers 75% V-A coupling at framework level via PROP-SF-2-5; the remaining 25% to reach 100% V-A at the massless helicity limit is OPEN-FP-SF-2-CHIR. The Capotauro chirality activation, if it is the *same* global event that imprints chirality on the W bracelet's centroid-localized dynamics (Picture B below), should close OPEN-FP-SF-2-CHIR jointly with OPEN-SM-4. The W⁰ neutrino scattering centroid-decoupling sketch (Patch 0367) is the proposed local-mechanism instantiation.

Closure at theorem level on all six sub-targets simultaneously closes (a) OPEN-SM-4 (Capotauro mechanism formalization), (b) OPEN-FP-SF-2-CHIR (V-A coupling derivation; cross-sector), and arguably contributes partial closures to (c) OPEN-SM-5 (PMNS analytic derivation; θ₁₃ and δ_CP sub-targets) and (d) the matter-antimatter asymmetry track in the cosmology side of the programme. This is therefore a *multi-sector* closure rather than a single-pair cross-sector closure. The methodological pattern from SF-4 v4.0 (Finding β-10) generalizes: cross-sector entanglement turns into structural advantage when foundational inputs from multiple sectors collectively determine the closure.

### §1.3 Foundational inputs

The closure rests on the following foundational inputs (CPP-internal but not derivable from A1–A11 within OPEN-SM-4 scope):

- **(FI-C-1) 600-cell chiral structure**: The 600-cell polytope is chiral as an oriented 4D regular polytope. Its full symmetry group $H_4$ has order 14400; the rotation subgroup (the 600-cell's chiral subgroup) has order 7200. The two enantiomorphic forms [600-cell]_L and [600-cell]_R are related by a ℤ₂ reflection that is not an element of the rotation subgroup. Inherited from standard polytope theory (Coxeter 1973); coverage-confirmed by `flagship_papers/electroweak/sketches/SF-2_W0_derivation.md` §3 distance-shell + symmetry-orbit classification of 600-cell substructures.

- **(FI-C-2) K3 base structure and four-cage taxonomy**: $K_3 = \{V_1, V_2, V_3\}$ is the equilateral triangle with three colour vertices and exact $C_3$ symmetry (SM-1 Theorem 1, FI-K-3 of SF-4 v4.0). Four-cage taxonomy: tetrahedral V=4, icosahedral V=12, dodecahedral V=20, icosidodecahedral V=30 (SM-1).

- **(FI-C-3) K3 antibonding doublet structure and TBM-aligned basis at theorem level**: The K3 ZBW Hamiltonian has eigenvalues $\lambda_+ = +2$ (bonding, once) and $\lambda_- = -1$ (antibonding, doubly degenerate). The TBM-aligned basis $\{|\phi_-^{(1)}\rangle = (2,-1,-1)/\sqrt{6}, |\phi_-^{(2)}\rangle = (0,-1,1)/\sqrt{2}\}$ is selected at theorem-level rigor by the standard $S_3 \to S_2$ representation-theory branching rule applied to the residual stabilizer of the charged-lepton K3-vertex occupation. Inherited from SF-4 v4.0 Composite K3-Cage-Shell Coupling Theorem (THEO-SF-4-5), which closes op:nu_id at theorem level. *This is the FI that was not available when the Grok exploratory work on δ_CP from Capotauro bias was originally done in March 2026 — that work pre-dated both SF-4's existence and the first cross-sector closure. The TBM-basis-at-theorem-level FI changes the substrate for the Capotauro derivation substantially.*

- **(FI-C-4) W bracelet $D_6$ stabilizer + W⁰ catalyst framework**: The W bracelet is the unique 1200-orbit of induced 6-cycles in the 600-cell graph under $H_4$ with $D_6$ stabilizer (THEO-SF-2-1). The W⁰ catalyst framework (six propositions PROP-SF-2-1 through PROP-SF-2-6) establishes the bracelet as the substrate for W± charged-current weak interactions, with the centroid as SSV-gradient minimum (PROP-SF-2-2) and $D_6$-symmetric phase structure (PROP-SF-2-5 V-A 75% from 120°/240° phase bias). Inherited from SF-2 v1.0 paper (`flagship_papers/electroweak/sf-2_electroweak.tex`).

- **(FI-C-5) Z icosahedral cage and H dodecahedral cage**: Z is the unique 12-vertex first distance shell with $I_h$ stabilizer (THEO-SF-2-2); H is the unique 20-vertex second distance shell with $I_h$ stabilizer via Platonic duality (THEO-SF-2-3); electroweak mass-gap forbids intermediate cages (THEO-SF-2-4). Inherited from SF-2 v1.0.

- **(FI-C-6) Cage-shell mass formula at theorem level**: $m_\text{unbound} = M_0 \cdot V^2 \cdot \sigma_\nu$ at leading order (THEO-SF-4-4); bound-mode formula $m_\text{bound} = M_0 \cdot V^{7/3}/N_\text{links}$ inherits from SM-9 cascade structure. Inherited from SF-4 v3.0.

- **(FI-C-7) DP species taxonomy + qDP/hDP/eDP linear ZBW screening**: The four DP-Sea species qDP, hDP-A, hDP-B, eDP and their role in linear ZBW screening of charge (SM-1 four-cage taxonomy + SM-2 quark charge asymmetry mechanism). Linear ZBW screening produces the $\delta = 1/3$ charge quantization (SM-1 Theorem 1) and is the input to the up/down quark asymmetry that Capotauro is hypothesized to coordinate with chirality activation.

- **(FI-C-8) Empirical SM phase data at NuFIT 6.0 / global-fit central values**: $\delta_{CP} = 195° \pm 40°$ (NuFIT 6.0 with octant ambiguity), $\sin^2\theta_{13} = 0.02203 \pm 0.00056$, $\eta_B = (6.12 \pm 0.04) \times 10^{-10}$ (Planck 2018 + BBN constraints). These are the empirical targets, not foundational inputs to the derivation, but enumerated here for completeness of the closure-target specification.

Eight foundational inputs, of which seven are elsewhere-derived (FI-C-1 from polytope theory; FI-C-2 from SM-1; FI-C-3 from SF-4 v4.0; FI-C-4 from SF-2 v1.0; FI-C-5 from SF-2 v1.0; FI-C-6 from SF-4 v3.0; FI-C-7 from SM-1 + SM-2) and one is empirical reference data (FI-C-8). The OPEN-SM-4 closure is heavier on cross-sector inheritance than SF-4 K3-Cage-Shell closure (6 FIs) — reflecting the multi-sector entanglement (touching SM-1, SM-2, SM-4, SM-5, SF-2, SF-4 simultaneously).

### §1.4 CPP axioms available

A1 through A11 are all available. The closure proof will identify which axioms are load-bearing as the derivation develops. Initial expectation based on the mechanism candidates in §3:

- **A1 DI-bit exchange substrate primitive**: load-bearing for all substrate-dynamics arguments (the chirality activation must reduce to A1-level dynamics).
- **A3 substrate orientation field**: very likely load-bearing — a chirality is an oriented structure, and A3 is the CPP primitive that gives orientation.
- **A4 substrate isotropy at vertex level**: load-bearing as a foil — the activation event must break A4-style isotropy at the global level while preserving it locally.
- **A6' Walk-Dimension Gauge Principle**: load-bearing for the propagation of the broken-symmetry signal across the substrate (per Picture A in §3).
- **A7 substrate-stress framework**: likely load-bearing as the medium that carries the chirality-activation pressure.
- **A9 mass-energy primitive**: load-bearing if the activation event has an energy cost (Picture D substrate-thermodynamic).
- **A10 orbital-substrate coupling**: load-bearing for the χ → coupling to PMNS sector through K3 antibonding eigenmodes.

Most load-bearing TBD. The mechanism candidates §3 differ in which subset of A1–A11 they prioritize.

### §1.5 Cross-sector entanglement structure

The Capotauro closure has *four* cross-sector entanglements, each adding structural constraints and potential leverage:

**Entanglement 1: SM-4 ↔ SM-5 PMNS sector.** Capotauro's χ-bias on the K3 doublet directly modulates θ₁₃ and δ_CP, which are PMNS observables. SM-5 v1.0 established TBM at zeroth order; the Capotauro closure must produce the *corrections* to TBM that the empirical data require (sin²θ₁₃ ≈ 0.022, sin²θ₁₂ shift, sin²θ₂₃ shift). SM-5 development notes already identify the Capotauro mechanism as the leading candidate. *This entanglement was registered before SF-4 v4.0, before the K3 antibonding doublet was lifted at theorem level. With the doublet now theorem-level-lifted via the $S_3 \to S_2$ branching rule (FI-C-3), the Capotauro action becomes a perturbation on an already-derived basis rather than an ansatz-selecting trick on an undefined basis. This is a substantial simplification.*

**Entanglement 2: SM-4 ↔ SF-2 W⁰ catalyst framework.** SF-2 v1.0 PROP-SF-2-5 establishes V-A at 75% from the W bracelet's $D_6$ 120°/240° phase bias as *structural preference*. The 100% V-A at massless limit is OPEN-FP-SF-2-CHIR. Capotauro's chirality activation, if it imprints on the W bracelet centroid-localized phase structure, provides the substrate-level mechanism for V-A → 100% chirality. The Patch 0367 W⁰ neutrino scattering centroid-decoupling sketch is the proposed local instantiation.

**Entanglement 3: SM-4 ↔ SF-4 v4.0 neutrino sector.** SF-4 v4.0 delivers 7/8 zero-parameter predictions; δ_CP is the eighth (deferred to SF-2 EW flagship per route ii). Capotauro closure of δ_CP delivers SF-4 8/8 prediction count. This is structural: the SF-4 v4.0 §6.1 master predictions table left δ_CP explicitly registered-as-open pending the EW-sector / Capotauro derivation.

**Entanglement 4: SM-4 ↔ SM-2 quark charge asymmetry / baryon asymmetry.** SM-2 Appendix H proposes Capotauro as the mechanism for up/down quark distinction (qDP linear ZBW screening on −qCP vs no screening on +qCP). The same chirality activation event, if it preferentially stabilizes linear ZBW extras on one polarity, produces the matter-antimatter asymmetry through the standard sphaleron-style mechanism (or its CPP analog through DP-chain composition statistics in W±-mediated processes). η_B closure inherits from this entanglement.

These four entanglements are not parallel — they form a *coupled* closure web. Capotauro closure does not just resolve OPEN-SM-4; it provides the missing structural element across a multi-paper region of the programme. This is the strongest argument for the prioritization: the closure has compounding value across SM-2, SM-4, SM-5, SF-2, SF-4 simultaneously.

### §1.6 Scope: what this sketch commits to and does not commit to

**Commits to.**
- A formal mechanism statement for Capotauro at substrate-dynamics level (mechanism candidates §3).
- Resolution of the χ = φ⁻¹ vs φ⁻² inconsistency (§4.2).
- Sub-claim decomposition for theorem-level closure.
- Connection to OPEN-FP-SF-2-CHIR through W⁰ centroid-decoupling sketch.

**Does not commit to.**
- Cosmological timing of Capotauro (the OP-SM-4 entry mentions "~120 Myr post-Big Bang"). The cosmological timing was a separate sub-problem in the original Grok-exploratory work; it depends on substrate-thermodynamic framework and cosmological expansion-rate calculation (OPEN-SR-6). For the v1.0 paper, the Capotauro mechanism's *physics content* (chirality activation producing δ_CP, sin²θ₁₃, η_B) is separable from "when did it happen cosmologically." A flagship paper can deliver the physics content without committing to the cosmological timing, which is a downstream consequence to be addressed separately. *Programme observation: the 120 Myr post-Big Bang figure is wildly later than the conventional electroweak symmetry-breaking epoch (~10⁻¹² s post-BB) and warrants independent re-derivation before being inherited; this is registered as a sub-task for the cosmology side of the programme.*
- Specific numerical coefficient for sin²θ₁₃ at theorem level (this is the central sub-claim (d) deliverable; first-pass attempt §5).
- The η_B precision-level closure (likely conditional at order-of-magnitude for v1.0).

---

## §2 The empirical landscape

### §2.1 Empirical targets

| Observable | Current best | Source | Tolerance for v1.0 closure |
|---|---|---|---|
| $\delta_{CP}$ | $195° \pm 40°$ | NuFIT 6.0 (Esteban et al. 2024, arXiv:2410.05380) | ±20° desirable, ±40° acceptable |
| $\sin^2\theta_{13}$ | $0.02203 \pm 0.00056$ | NuFIT 6.0 | ±5% desirable, ±10% acceptable |
| $\eta_B$ | $(6.12 \pm 0.04) \times 10^{-10}$ | Planck 2018 + BBN | order-of-magnitude for v1.0; precision target for v1.x |
| $\sin^2\theta_{12}$ (corrected) | $0.307 \pm 0.013$ | NuFIT 6.0 | TBM zeroth order 0.333; correction ~9% needed |
| $\sin^2\theta_{23}$ (corrected) | $0.572^{+0.018}_{-0.022}$ NO | NuFIT 6.0 | TBM zeroth order 0.500; correction ~14% needed |

Note that θ₁₂ and θ₂₃ also deviate from TBM at the 10-14% level; the development-SM-5.md notes register these as "Capotauro mechanism corrections" alongside θ₁₃. The full Capotauro closure should account for all three deviation patterns, not just θ₁₃ and δ_CP. *Sub-claim coverage check: this means the closure must produce three correction coefficients with a single mechanism + single coupling χ — over-determined by a factor of three if χ is the only free input.*

### §2.2 Prior numerical attempts

**Grok exploratory δ_CP formula** (`archive/grok-exploratory-SM/p2-neutrino-mixing-angles/delta-cp-phase-derivation.md`):

$$\delta_{CP} \approx 180° + \left(\chi \times \frac{360°}{\phi^2} - 180°\right) \cdot \text{sign}(\text{bias})$$

With χ ≈ φ⁻¹ ≈ 0.618 → δ_CP ≈ 180° + (0.618 × 137.5° − 180°) ≈ 180° + (84.97° − 180°) ≈ 84.97°.

*Note: that does not actually give 195° on direct evaluation. The Grok derivation in the archive reports δ_CP ≈ 195° but the formula as written gives a different value. Let me recompute. The "golden angle" is 360°/φ² ≈ 137.5° (= 360° × (1 − 1/φ)). With χ = 0.618: 0.618 × 137.5° = 84.97°. Subtracting 180° gives −95.03°. Adding 180° gives 84.97°. Multiplying by sign(bias) and adding to 180° gives either 180° + 84.97° = 264.97° (if sign = +1) or 180° − 84.97° = 95.03° (if sign = −1). Neither is 195°.*

**The Grok formula does not, on direct evaluation, give the claimed δ_CP ≈ 195°.** Either the formula in the archive is mis-stated, or the "sign(bias)" / "(...) − 180°" structure is being applied in a way I'm not reading correctly. *This is a registered Finding C-1: the prior Grok numerical claim of δ_CP ≈ 195° from χ ≈ φ⁻¹ via this formula needs to be re-derived from scratch; it is not currently verified.*

**Grok exploratory sin²θ₁₃ formula** (same source + lattice-subgroups.md):

$$\sin^2\theta_{13} \approx \frac{\phi^{-2}}{\text{coefficient}}$$

where coefficient ≈ 1.6 (i.e., sin²θ₁₃ ≈ 0.382/1.6 ≈ 0.239 from this formula — *which is 10× too large compared to empirical 0.022*).

*Wait, that's wrong by a factor of 10. The intended formula is presumably $\sin^2\theta_{13} \approx \phi^{-2} / [\text{coefficient}]$ with coefficient ≈ 17.4 or similar to land at 0.022. Or alternatively $\sin^2\theta_{13} \approx \phi^{-n}$ for $n = 9$ ($\phi^{-9} \approx 0.0213$, which is within 3% of empirical). Or some other combination. Without seeing Grok's derivation script, I cannot verify the exact functional form intended.*

*This is registered as Finding C-2: the prior Grok numerical claim of sin²θ₁₃ ≈ 0.022 from φ⁻² is not currently verified at the formula level. The claim may be true with a different coefficient or a different formula; first-pass closure attempt in §5 will re-derive from scratch.*

**Implication.** The Grok-stage numerical claims in the archives may be useful as targets and as inspiration, but they should not be inherited as derivations. The Capotauro closure campaign needs to re-derive from CPP primitives + named FIs, using the SF-4 v3.0/v4.0 methodology stack rather than the Grok-stage exploratory style. This is in fact what symmetric-honesty discipline requires.

### §2.3 The χ = φ⁻¹ vs χ = φ⁻² inconsistency

The OP-SM-4 archive explicitly registers this inconsistency as sub-problem 2:

> "The bias $\chi = \phi^{-1} \approx 0.618$ appears in the δ_CP calculation. [...] The 600-cell edge lengths come in two types with ratio $\phi : 1$. After Capotauro, the bias between the two types is: $\chi = (\phi^{-1} - \phi^{-2})/(\phi^{-1} + \phi^{-2}) = (1 - \phi^{-1})/(1 + \phi^{-1}) = \phi^{-1}/\phi = \phi^{-2} \approx 0.382$. This gives χ ≈ 0.382, not 0.618. The discrepancy suggests χ is either φ⁻¹ (direct edge ratio) or φ⁻² (the reciprocal), and the current statement needs clarification."

The direct edge-length-ratio bias calculation is unambiguous: if the lattice has two edge types with ratio φ:1 and the chirality activation breaks the symmetry between them, the natural normalized bias parameter is

$$\chi_{\rm edge-ratio} = \frac{\phi - 1}{\phi + 1} = \frac{1/\phi}{\phi} = \frac{1}{\phi^2} = \phi^{-2} \approx 0.382$$

The φ⁻¹ value used in the Grok exploratory work appears to come from a different normalization or from a different geometric structure (not the edge-ratio bias). Candidate interpretations:

**Interpretation A: φ⁻¹ is the direct edge-length ratio without normalization.** $\phi^{-1} \approx 0.618$ is the length of a short edge relative to a long edge in the 600-cell. The "bias" between the two enantiomorphs, if measured by this length ratio rather than the normalized fractional bias, is φ⁻¹ — but this is not a dimensionless symmetric bias parameter in the conventional sense.

**Interpretation B: φ⁻¹ refers to a different geometric quantity.** The 600-cell has multiple φ-quantities: edge-to-circumradius ratios, dual lengths, golden-section dihedrals. The relevant "polarity coupling" χ may refer to a different ratio (e.g., the ratio of one symmetry-broken vertex-orbit size to another).

**Interpretation C: φ⁻¹ and φ⁻² are both correct, in different sub-mechanisms.** χ ≈ φ⁻¹ controls one aspect of the CP-violation effect (e.g., the δ_CP phase shift via the golden angle 360°/φ² calculation), and χ ≈ φ⁻² controls another (e.g., the θ₁₃ correction magnitude via the squared-amplitude relation sin²θ₁₃ ∼ χ ∼ φ⁻²).

**Interpretation D: One of the two is empirically corroborated and the other is the artifact of a notation slip.** Direct calculation: $\sin^2\theta_{13} \approx 0.022$ vs $\phi^{-2} \approx 0.382$ — factor 17 off. $\phi^{-2}$ doesn't directly give the right magnitude. *On the other hand*: $\phi^{-9} \approx 0.0213$ which is within 3% of $\sin^2\theta_{13}$, and similar $\phi^{-n}$ relations also work numerically. Notably also: $\phi^{-1}/(\phi^4 + 1) \approx 0.618/7.85 \approx 0.0787$ — not right. And: $(\phi - 1)^2/\phi^2 = \phi^{-4} \approx 0.146$ — not right. The φ-numerology landscape is large and the right relation is not obvious by inspection.

**Working hypothesis to verify in §4.2.** χ as defined in OP-SM-4 means the *symmetry-broken bias parameter* in the conventional dimensionless sense, which gives $\chi = \phi^{-2}$ from the edge-ratio derivation. The δ_CP and sin²θ₁₃ formulas in the Grok archive may need re-derivation under this corrected χ value. Whether the corrected χ produces the right δ_CP and sin²θ₁₃ at zeroth order is itself the key test of the closure attempt — and is exactly what sub-claim (b) in §4.2 needs to deliver.

**This resolution is the single most important target of the first one or two Capotauro sketch sessions.** Until the χ-value is fixed at theorem level, the down-stream sub-claims (c, d, e, f) all sit on an undetermined input. The χ-value resolution is the equivalent of SF-4 Session 40's "leading-order $\sigma = z^{-10}$ result" — the first quantitative numerical alignment that validates the framework can deliver.

### §2.4 The empirical signature constraints summarized

For the closure to be empirically corroborated, it must simultaneously deliver:

1. **A χ-value** that is either φ⁻¹, φ⁻², or some derivable composite, justified from CPP 600-cell geometry at theorem level.
2. **A δ_CP formula** of the form $\delta_{CP}(\chi, \phi, \text{lattice constants})$ that lands within ±20° of NuFIT 6.0 central value 195°.
3. **A sin²θ₁₃ formula** that lands within ±10% of NuFIT 6.0 central value 0.0220.
4. **Corrections to sin²θ₁₂ and sin²θ₂₃** that land within ±20% of the NuFIT 6.0 deviations from TBM.
5. **A baryon asymmetry η_B formula** that lands within an order of magnitude of $6 \times 10^{-10}$ (order-of-magnitude tolerance for v1.0; precision target for v1.x).
6. **A bridge to OPEN-FP-SF-2-CHIR** showing that the same χ-bias produces V-A → 100% at the massless helicity limit.

These six empirical signatures form the F3 pattern check for the Capotauro closure (using the F1/F2/F3 falsifier-criteria framework from the SS-7 OPEN-SS-32 → U-shape thread, Phase 5 onwards). F1 sign-theorem checks at the symmetry-breaking level should be analytical; F2 magnitude checks should target ±20% on δ_CP and ±10% on sin²θ_ij; F3 pattern check across the six observables jointly.

---

## §3 Mechanism candidates

Four candidate mechanisms are laid out, in the spirit of SF-4 Picture A/B/C laying out three convergent suppression mechanisms in Session 41. The Capotauro closure does not require a unique mechanism at v1.0; if two or more candidates converge on the same χ-value and the same δ_CP formula, the convergence itself is the closure (analogous to SF-4 v1.0's three convergent pictures for σ_ν = z⁻¹⁰).

### §3.1 Picture A — Global lattice racemization breaking

**Mechanism statement.** The un-activated lattice is the direct product [600-cell] × ℤ₂, where the ℤ₂ acts as the enantiomorph-exchange (reflection between [600-cell]_L and [600-cell]_R). At Capotauro, a substrate-level dynamical event spontaneously selects one of the two enantiomorphs globally. The selection is *not* energy-driven in the conventional Higgs-mechanism sense (there is no degenerate-vacuum potential whose minimum lifts the symmetry); instead it is *kinetic / topological* — once one enantiomorph is locally selected anywhere in the substrate, the selection propagates faster than the substrate can locally re-racemize, and the entire substrate freezes into a single chirality.

**Closure path under A1–A11.**

- *A1 DI-bit exchange:* In the racemic state, DI-bit exchanges between adjacent CPs are equally weighted across both enantiomorph orientations. The Capotauro event introduces a global preference: DI-bit exchange amplitudes acquire a multiplicative weight $e^{i\eta(\hat{r})}$ where $\eta(\hat{r})$ is an orientation-dependent phase tied to the selected enantiomorph.
- *A3 substrate orientation field:* The orientation-dependent phase $\eta(\hat{r})$ is the substrate orientation field acquiring a non-zero global expectation value. Before Capotauro: $\langle \eta \rangle = 0$. After: $\langle \eta \rangle \neq 0$ with a specific functional form determined by the 600-cell chirality.
- *A6' Walk-Dimension Gauge Principle:* Walk-dimension reductions on the activated lattice acquire chirality-dependent signs; this is what propagates the bias into observable phenomena.
- *A4 substrate isotropy at vertex level:* preserved locally — the activation is a *global* event that does not break local isotropy at any single vertex.

**Numerical content.** χ in this picture is the magnitude of $\langle \eta \rangle$ at the activated state, derivable from the 600-cell geometry as the ratio of the two enantiomorph-volumes' bias parameter. If the bias is the normalized edge-ratio difference, χ = φ⁻². If it is the un-normalized edge-length itself, χ = φ⁻¹.

**Why this is CPP-axiomatic.** Picture A uses only A1, A3, A4, A6' — no new postulates. The "kinetic / topological" framing is the natural CPP interpretation of spontaneous symmetry breaking without an explicit Higgs potential, and aligns with the substrate-thermodynamic register the programme has been developing.

**Why it might fail.** No dynamical mechanism is yet specified for what initiates the global enantiomorph-selection — i.e., what plays the role of the "first fluctuation" that breaks the symmetry. Cosmological framings (early-universe density fluctuations) are external to CPP; substrate-internal framings need to be developed. *This is the analog of SF-4 Session 55–60's Picture A formalization: structurally promising, but the "first-fluctuation" mechanism is the load-bearing piece that needs theorem-level closure.*

### §3.2 Picture B — W⁰ bracelet centroid-decoupling as local manifestation of global chirality

**Mechanism statement.** The Capotauro chirality activation imprints on the substrate-level dynamics of *every* localized cage structure in the lattice, not just the global racemization. The W⁰ bracelet, with its $D_6$ stabilizer and SSV-gradient-minimum centroid, is a privileged site for the chirality activation to be visible: a spinning DP or hybrid tetrahedron transiting through the bracelet centroid experiences a momentary decoupling from the surrounding DP Sea, and the post-centroid orientation distribution is biased by the activated lattice chirality. The bias is *the same* χ-coupling as in Picture A — but realized as a *local* phenomenon at the W⁰ centroid rather than as a *global* substrate orientation field.

**Closure path under A1–A11.**

- This is the Patch 0367 W⁰ neutrino scattering insight made fully explicit. The three-Layer development requirements from Patch 0367 carry over: (1) operational definition of centroid passage; (2) quantification of post-emergence direction selection; (3) phenomenology bridge to V-A asymmetric scattering distributions.
- Picture B uses A1 (DI-bit exchange), A4 (substrate isotropy as foil — broken locally at the centroid), A7 (substrate-stress in the SSV-gradient depth), A10 (orbital-substrate coupling for the spinning DP / h-tet).

**Numerical content.** χ in this picture is the magnitude of the centroid-decoupling-induced direction bias. The $D_6$ stabilizer of the W bracelet has 12 elements (six rotations + six reflections); after Capotauro, the reflection-elements acquire chirality-dependent weights, and the post-centroid direction distribution becomes asymmetric under $\hat{r} \to -\hat{r}$ + reflection across the bracelet plane. The asymmetry parameter is the local χ-coupling.

**Why this is the bridge to OPEN-FP-SF-2-CHIR.** PROP-SF-2-5 gives V-A at 75% from the $D_6$ phase bias *without* Capotauro activation (i.e., considering only the six rotation elements of $D_6$ acting on the 120°/240° phase structure). When Capotauro is included, the six reflection elements no longer commute with the chirality activation and produce a residual V-A bias. The total V-A becomes 75% (rotational, framework-level) + 25% (chiral, from Capotauro) = 100% at the massless helicity limit. **This closes OPEN-FP-SF-2-CHIR jointly with OPEN-SM-4.**

**Why this is CPP-axiomatic.** Picture B uses A1, A4, A7, A10 — no new postulates. The substrate-stress framework (A7) provides the SSV-gradient-minimum centroid mechanism without any new structure.

**Why it might fail.** The "centroid decoupling" mechanism is intuitive but operationally undefined at Tier-4 reasoning level. The 600-cell graph has the W bracelet centroid as a geometric point but not as a vertex; what it means for a DP to "transit through" a non-vertex point in a discrete lattice is the central operational definition required. Three options: (i) the centroid is identified with the time-symmetric midpoint of a DI-bit exchange between bracelet vertices, in which case the centroid is event-defined rather than location-defined; (ii) the centroid is identified with a virtual interior vertex at the bracelet center, in which case the 600-cell graph is augmented with virtual centroid points; (iii) the centroid is identified with the spatial mean position of the six bracelet vertices, in which case the DP transit is a coarse-grained continuum-limit phenomenon. Option (i) is most CPP-axiomatic but operationally trickiest; option (iii) is most accessible but requires continuum-limit machinery.

### §3.3 Picture C — H₄ → I rotational subgroup selection at K3-coupling level

**Mechanism statement.** The full symmetry group $H_4$ of the 600-cell (order 14400) contains the rotation subgroup of order 7200 — call this $I_4$ (the rotational $H_4$). The Capotauro activation is interpreted as the spontaneous selection of $I_4$ over the full $H_4$ in the substrate dynamics: the reflective elements of $H_4$ become forbidden (or kinetically suppressed) at the activated state. This is *symmetry breaking by selection of a subgroup*, in the same sense as the K3 doublet's $S_3 \to S_2$ breaking via charged-lepton vertex occupation (FI-C-3) — but at the global $H_4$ level rather than the local K3 level.

**Closure path under A1–A11.**

- *A1 DI-bit exchange:* In the racemic state, DI-bit exchanges respect full $H_4$. After Capotauro, exchanges respect only $I_4$ (the rotational subgroup). The reflective elements become forbidden; this is the structural content of the symmetry breaking.
- The branching rule analogous to $S_3 \to S_2$ — call it $H_4 \to I_4$ branching — must be analyzed: every $H_4$ irrep decomposes into a sum of $I_4$ irreps, and the "after Capotauro" Hilbert space is the subspace where each state lives in a definite $I_4$ irrep.
- The χ-coupling in this picture is the *intertwiner coefficient* between $H_4$ and $I_4$ representations — a specific group-theoretic quantity that should be computable in closed form once the branching rule is fully unpacked.

**Numerical content.** χ in this picture is determined by the $H_4 / I_4$ index ratio (= 2, since $|H_4|/|I_4| = 14400/7200 = 2$) modulated by the K3-doublet Clebsch-Gordan-style intertwiner on the antibonding eigenspace. This should be a *purely* geometric number, derivable without any free parameter. If the resulting χ matches the OP-SM-4 target value (φ⁻¹ or φ⁻²), this is a strong validation.

**Why this is CPP-axiomatic.** Picture C uses A1 + representation theory at the $H_4$ level. It is *the most directly analogous* to SF-4 v4.0's $S_3 \to S_2$ branching rule (FI-C-3) at the K3 level, and inherits the same theorem-level rigor: the branching rule itself is a standard mathematical result, applied to a CPP-named substrate.

**Why it might fail.** The "reflective elements become forbidden" framing requires a dynamical justification: what is the substrate-level mechanism that disallows reflective $H_4$ operations after Capotauro? Picture A's "global enantiomorph selection" is one such mechanism; Picture C is more like a kinematic constraint than a dynamical event. Picture C may turn out to be the *consequence* of Picture A rather than an independent mechanism — in which case Picture A is the right level of mechanism and Picture C is the right level of representation-theoretic machinery.

### §3.4 Picture D — Substrate-thermodynamic phase transition at critical SSV gradient

**Mechanism statement.** The Capotauro activation is a substrate-thermodynamic phase transition occurring when the substrate-internal energy density (or some equivalent thermodynamic variable) drops below a critical threshold. Above the threshold (early lattice, high-energy state), the lattice is in the racemic-symmetric phase; below, it spontaneously breaks chirality. The critical temperature $T_C$ is set by the 600-cell internal energy scale; the chirality activation is the order parameter undergoing second-order phase transition.

**Closure path under A1–A11.**

- This picture requires the substrate-thermodynamic framework that ChatGPT v1.3 review identified as "currently undefined." Picture D therefore depends on first developing the substrate-thermodynamic framework (registered as OPEN-FP-SF-2-EWSB closure path among others).
- A9 (mass-energy primitive) becomes load-bearing here: the substrate temperature is identified with the average mass-energy density per CP in the DP Sea.

**Numerical content.** χ in this picture is determined by the order parameter at $T = 0$ relative to the order parameter at $T = T_C$ — a standard Landau-Ginzburg-style critical-exponent calculation, modulated by the 600-cell geometric coefficients. The χ-value is the (zero-temperature) saturated chirality bias.

**Why this is CPP-axiomatic in principle.** Picture D is the most physically intuitive mechanism (parallels electroweak phase transition mechanism in conventional cosmology). The substrate-thermodynamic framework, if developed, gives the cleanest derivation of the "first fluctuation" that Picture A leaves implicit.

**Why it might fail / why it is not the first-priority candidate.** Substrate-thermodynamic framework is currently undefined. To use Picture D, the Capotauro closure must wait for OPEN-FP-SF-2-EWSB closure path (or equivalent substrate-thermodynamic foundational work). This is multi-paper scope. *Picture D is therefore a deferred candidate: register it as the eventual most-rigorous derivation venue, but do not block the v1.0 Capotauro paper on its closure.*

### §3.5 Cross-comparison

| Picture | Mechanism style | Most CPP-axiomatic | Closure timeline | Empirical content delivery |
|---|---|---|---|---|
| A | Global enantiomorph selection via substrate orientation field | Most aligned to A3 axiom | Direct: closeable at v1.0 with extant FIs | Delivers χ as orientation-field magnitude |
| B | Local W⁰ centroid-decoupling, global through universality | Aligned to A4 + A7 + A10 | Requires Patch 0367 sketch development (3 layers) | Delivers χ as local bias + bridge to CHIR closure |
| C | $H_4 \to I_4$ representation-theoretic branching | Most rigorous, parallel to SF-4 v4.0 $S_3 \to S_2$ | Direct: closeable at v1.0 with extant FIs | Delivers χ as intertwiner coefficient (purely geometric) |
| D | Substrate-thermodynamic critical phase transition | Most physically intuitive | Deferred: requires substrate-thermodynamic framework | Delivers χ as order-parameter saturation value |

**Initial reading.** Picture A is the closest analog to the original SM-4 / Grok mechanism statement. Picture C is the closest analog to the SF-4 v4.0 methodology and is the most directly cross-validating against the K3-doublet closure. Picture B is the bridge to OPEN-FP-SF-2-CHIR. Picture D is the deferred most-rigorous derivation venue.

**Recommended closure architecture for v1.0.** Pursue Pictures A + B + C jointly as three convergent mechanism candidates (parallel to SF-4 v1.0 closure mode). If all three converge on the same χ-value (whether φ⁻¹, φ⁻², or some composite), the convergence is the closure. Picture D is registered as the eventual Layer 4-style continuum-EFT-style derivation venue, deferred to a future paper.

This is the analog of SF-4 v1.0's three-Picture closure (A: two-sided DI-bit exchange; B: two ZBW half-cycles; C: edge-straddling), which delivered partial closure at v1.0 SHIP with Picture A formalized later at theorem level (Sessions 55–60, v2.0 SHIP).

---

## §4 Sub-claim decomposition

The closure decomposes into six sub-claims that, jointly closed at theorem level, deliver full OPEN-SM-4 + OPEN-FP-SF-2-CHIR cross-sector closure:

### §4.1 Sub-claim (a): Chirality-activation event as substrate-level dynamical primitive

**Statement.** There exists a substrate-level dynamical primitive — call it the **Capotauro operator** $\hat{C}$ — acting on the racemic 600-cell substrate that selects a single chiral enantiomorph globally. The operator $\hat{C}$ is constructible from CPP axioms A1–A11 without new postulates.

**Closure target.** Specify $\hat{C}$ at the substrate-dynamics level using the most CPP-axiomatic of Pictures A, B, C, D. Show that $\hat{C}$ commutes with the residual $I_4$ symmetry (rotations) but anti-commutes with the broken ℤ₂ symmetry (reflections). Show that the action of $\hat{C}$ on the racemic state produces a single chiral state with well-defined χ-coupling.

**Working hypothesis.** $\hat{C}$ is the substrate orientation field $\eta(\hat{r})$ (Picture A) acquiring a non-zero global expectation value. Three potential mechanisms for the activation event (the "first fluctuation"): (a-i) cosmological substrate density fluctuation; (a-ii) substrate-thermodynamic phase transition (Picture D); (a-iii) topological soliton nucleation from substrate primitives. Mechanism (a-iii) is the most CPP-axiomatic but requires solitonic dynamics not yet developed in the corpus.

**Difficulty estimate.** Hardest sub-claim. May require multi-session work and substrate-thermodynamic framework development. Comparable in difficulty to SF-4 Sessions 55–60 Picture A axiomatic closure.

### §4.2 Sub-claim (b): The chiral bias χ value

**Statement.** The chiral bias χ produced by the Capotauro activation is uniquely determined by 600-cell geometry as:

$$\chi = \chi_{\rm CPP}(600\text{-cell}, \text{normalization choice})$$

at zero free parameters. Specifically, the OP-SM-4 archive sub-problem 2 inconsistency between χ ≈ φ⁻¹ and χ ≈ φ⁻² is resolved at theorem level by identifying which normalization is correct.

**Closure target.** Derive χ at theorem level. Resolve whether χ = φ⁻¹, χ = φ⁻², or some other combination of 600-cell golden-ratio quantities. The derivation must inherit only from FIs (no fitted parameters) and must be self-consistent with the down-stream sub-claims (c, d, e).

**Working hypothesis.** Based on the edge-ratio bias calculation in the OP-SM-4 archive: χ = φ⁻² ≈ 0.382 at the dimensionless symmetric-bias level. The φ⁻¹ value used in the Grok exploratory work is likely the un-normalized edge-length ratio, used implicitly in formulas that should have been normalized. The φ⁻² value is consistent with the sin²θ₁₃ scaling and with the canonical Landau-Ginzburg-style order-parameter normalization.

**Difficulty estimate.** Tractable in one session. The edge-ratio derivation is direct; the normalization-choice analysis is straightforward; the only difficulty is verifying consistency with down-stream sub-claims (which is iterative).

**This is the highest-priority first-pass closure target.** Resolution of χ at theorem level is the equivalent of SF-4 Session 40's leading-order $\sigma = z^{-10}$ result: it is the first quantitative numerical alignment that validates the framework can deliver. The whole Capotauro campaign should open with this sub-claim.

### §4.3 Sub-claim (c): χ couples to the PMNS sector through the K3 antibonding doublet

**Statement.** The Capotauro chirality activation, via the global χ-coupling, modulates the K3 antibonding doublet eigenspace structure (inherited at theorem level via FI-C-3). Specifically, the activation introduces a *χ-dependent perturbation* on the TBM-aligned basis $\{|\phi_-^{(1)}\rangle, |\phi_-^{(2)}\rangle\}$ that lifts their effective masses and rotates the TBM mixing angles by χ-controlled amounts.

**Closure target.** Specify the perturbation operator $\hat{V}_\chi$ acting on the K3 eigenspace. Show that $\hat{V}_\chi$ is the natural representative of the global substrate orientation field on the K3-doublet subspace (via FI-C-3 + FI-C-7). Compute the χ-corrections to TBM angles to leading order in χ.

**Working hypothesis.** $\hat{V}_\chi$ in the TBM-aligned basis is a 2×2 matrix of the form
$$\hat{V}_\chi = \chi \begin{pmatrix} v_{11} & v_{12} \\ v_{12}^* & v_{22} \end{pmatrix}$$
where $v_{ij}$ are 600-cell geometric coefficients determined by the K3-doublet's $\mu\tau$-symmetric / $\mu\tau$-antisymmetric structure (Wigner-Eckart-style) and the chirality-activation phase $e^{i\eta}$. The leading TBM corrections are:
- $\Delta(\sin^2\theta_{12}) \sim \chi \cdot v_{12}$
- $\Delta(\sin^2\theta_{23}) \sim \chi \cdot (v_{22} - v_{11})$
- $\sin^2\theta_{13} \sim \chi^2 \cdot |v_{12}|^2$
- $\delta_{CP} \sim \arg(v_{12})$ shifted by χ-phase

**Why this is theorem-level tractable.** The FI-C-3 derivation of the TBM-aligned basis at theorem level is the load-bearing piece; it was the open problem of CPP since SM-5 v1.0 (March 2026) and only closed at SF-4 v4.0 (May 2026). With that closure in place, sub-claim (c) becomes a Wigner-Eckart-style perturbation calculation rather than an ansatz selection. *This is exactly the kind of cross-sector leverage that makes Capotauro closure tractable now and not earlier.*

**Difficulty estimate.** 2–3 sessions. Standard rep-theory perturbation calculation; the difficulty is identifying $v_{ij}$ from 600-cell geometry.

### §4.4 Sub-claim (d): Quantitative reproduction of δ_CP, sin²θ₁₃, and TBM corrections

**Statement.** Substituting the χ-value from sub-claim (b) into the perturbation framework of sub-claim (c) produces:
- $\delta_{CP} = 195° \pm \text{(derivable error band)}$
- $\sin^2\theta_{13} = 0.022 \pm \text{(derivable error band)}$
- $\sin^2\theta_{12}$ and $\sin^2\theta_{23}$ corrections matching NuFIT 6.0 deviations from TBM.

**Closure target.** Run the calculation. If the numbers come out right, the closure validates the framework. If they don't, the χ-value or the perturbation structure needs revision.

**Working hypothesis.** With χ = φ⁻² and the Wigner-Eckart coefficients from sub-claim (c), the leading-order TBM corrections should land within ±20% of the empirical deviations. *This is the central F1/F2/F3 falsifier checkpoint for the Capotauro closure: if the numbers don't come out within tolerance, the mechanism needs to be revised.*

**Difficulty estimate.** 1 session after sub-claim (c) is in place. Direct calculation.

### §4.5 Sub-claim (e): Closure of OPEN-FP-SF-2-CHIR via W⁰ centroid-decoupling

**Statement.** The same Capotauro chirality activation event that produces χ in the global lattice produces a *local* chirality bias at the W⁰ bracelet centroid. Combined with PROP-SF-2-5's 75% V-A from the $D_6$ rotational phase bias, the Capotauro chirality bias adds the remaining 25% V-A at the massless helicity limit, delivering V-A = 100% at the framework level required by Standard Model phenomenology.

**Closure target.** Specify the W⁰ centroid-decoupling mechanism (Picture B) at substrate dynamics level. Show that the chirality bias from Capotauro, when imprinted on the bracelet's $D_6$ reflection elements, breaks the framework-level 75% V-A symmetry to deliver the missing 25% at massless limit.

**Working hypothesis.** The W⁰ centroid hosts the SSV-gradient minimum (PROP-SF-2-2). At this minimum, a transiting DP/h-tet momentarily decouples from the surrounding DP Sea. In the un-activated state, the $D_6$ stabilizer's six reflection elements and six rotation elements equally weight the post-centroid direction distribution, giving the 75% V-A. After Capotauro, the six reflection elements acquire chirality-dependent suppression weights of order χ; this breaks the equal weighting and delivers the missing 25% V-A as a χ-dependent correction.

**Difficulty estimate.** 2–3 sessions, with significant overlap to sub-claim (a) work. Requires the Picture B centroid-decoupling operational definition to be sharpened (per Patch 0367 three-Layer development requirement).

### §4.6 Sub-claim (f): Baryon asymmetry η_B from Capotauro-mediated DP species preference

**Statement.** The Capotauro chirality activation, through the chirality-dependent suppression of one polarity over the other at the substrate level, preferentially stabilizes linear ZBW screening on negative qCP centers (down-type quarks per SM-2 Appendix H). This produces the matter-antimatter asymmetry through the DP-chain composition statistics in W±-mediated processes (FI-C-7), with η_B emerging at the chirality-weighted DP-chain branching ratios.

**Closure target.** Compute η_B from the chirality-dependent DP-chain composition. Match to $6 \times 10^{-10}$.

**Difficulty estimate.** Hardest sub-claim after (a). For v1.0, target order-of-magnitude closure ($\eta_B \sim 10^{-10}$ within a factor of 3–10); precision target for v1.x. Likely depends on the DP-chain composition framework (OPEN-FP-SF-2-chaincomp) which itself depends on substrate thermodynamics.

---

## §5 First-pass partial-closure attempts

*Placeholder for Sessions 85+ work. The next session begins with sub-claim (b) χ-value resolution.*

### §5.1 Session 85 priority: sub-claim (b) χ resolution

**Plan.**

1. Verify the edge-ratio bias calculation in OP-SM-4 sub-problem 2 from first principles using the 600-cell vertex coordinates. Confirm $\chi_{\rm edge-ratio} = \phi^{-2}$.
2. Identify alternative dimensionless bias parameters that could be intended in the Grok exploratory work (volume ratios, dihedral angles, vertex-orbit size ratios). For each, compute the value and check whether any gives φ⁻¹ ≈ 0.618 from a *normalized* (dimensionless symmetric bias) construction.
3. Re-derive the Grok δ_CP formula $\delta_{CP} \approx 180° + (\chi \times 360°/\phi^2 - 180°)$ from scratch. Identify whether (i) the formula structure is correct but χ should be φ⁻², (ii) the formula structure needs revision (with χ = φ⁻²), or (iii) both.
4. Tabulate the down-stream sub-claims' χ-dependence and identify what value of χ makes them simultaneously consistent with empirical data.
5. Register Finding C-3 with the resolved χ-value and the dimensionless construction it represents.

### §5.2 Session 86–87 priority: sub-claim (c) K3-doublet perturbation framework

**Plan.**

1. With χ resolved, construct $\hat{V}_\chi$ as a 2×2 matrix in the TBM-aligned basis. Identify the $v_{ij}$ coefficients from 600-cell geometry (using FI-C-2, FI-C-3, FI-C-4, FI-C-5 cross-coupling).
2. Compute leading TBM angle corrections.
3. F1 sign check: do the signs of the corrections match the empirical NuFIT 6.0 deviations?
4. F2 magnitude check: are the corrections within ±20% of empirical?

### §5.3 Sessions 88+: sub-claims (a, e, f) in parallel

(Detailed plan deferred to after sub-claims b + c are in hand.)

---

## §6 Open questions for Thomas (physical intuition required)

The following are questions where Thomas's physical intuition is the load-bearing input and the closure direction depends on his judgment. These should be addressed before sub-claim (a) closure is attempted:

**Q1. Which mechanism Picture is the most physically primary?** Picture A (global enantiomorph selection via substrate orientation field) is closest to your SM Paper 2 Appendix H statement. Picture B (W⁰ centroid-decoupling) is the local manifestation of the same physics and is the bridge to OPEN-FP-SF-2-CHIR closure. Picture C ($H_4 \to I_4$ branching) is the most rigorous methodologically. Picture D (substrate-thermodynamic phase transition) is the most physically intuitive but requires undeveloped framework. Which picture do you read as the *primary* mechanism, with the others as consequences or refinements?

**Q2. What is the "first fluctuation" that initiates the activation event?** In conventional electroweak symmetry breaking, the first fluctuation comes from quantum-thermal fluctuations near the critical temperature. In CPP, what is the analogous primitive? Three candidates:
- (a) A cosmological substrate density fluctuation (cosmology-external to CPP).
- (b) A substrate-thermodynamic critical-density crossing (Picture D, requires framework not yet built).
- (c) A topological soliton nucleation event (Picture A's "kinetic / topological" framing, requires solitonic dynamics not yet developed).

**Q3. Is the χ-value φ⁻¹ or φ⁻²?** The direct edge-ratio bias derivation gives χ = φ⁻². The Grok exploratory work used χ = φ⁻¹. Is there a substrate-mechanical reason to prefer one over the other? Or do both quantities have well-defined geometric meanings, and the Capotauro effect involves both at different sub-mechanisms (Interpretation C in §2.3)?

**Q4. What is the W⁰ centroid operationally?** Picture B (centroid-decoupling) requires an operational definition. Three options laid out in §3.2 — (i) time-symmetric DI-bit exchange midpoint event-defined; (ii) virtual interior vertex location-defined; (iii) spatial-mean position continuum-coarse-grained. Which reading is the CPP-axiomatic one?

**Q5. Is the cosmological "120 Myr post-Big Bang" timing intended as a precise prediction or a placeholder estimate?** This sketch defers the cosmological-timing question (per §1.6 scope). But if you have intuition on whether the timing is precise enough to be a falsifiable prediction in the v1.0 paper, that affects whether we should include cosmological consequences in the paper or defer them to a companion.

**Q6. Should the W bracelet's $D_6$ structure be re-examined under Capotauro?** PROP-SF-2-5's 75% V-A from $D_6$ phase bias was derived in SF-2 v1.0 *without* Capotauro activation. If Capotauro is the source of the remaining 25%, then the PROP-SF-2-5 framework needs to be re-examined at the joint $D_6$ + Capotauro level — and the 75% / 25% split needs to be explicitly justified rather than assumed. Is this a load-bearing concern, or is the 75% / 25% split robust to the order of derivations?

---

## §7 Next session priorities

*Status as of Session 85 close (Patch 0378). Sub-claim (b) χ-value resolution work is partially advanced: the OP-SM-4 archive arithmetic error is corrected (Finding C-3), the 600-cell distance structure is verified computationally (Finding C-4), and the candidate χ table is enumerated (§9). Sub-claim (b) is not yet closed at theorem level — the perturbation framework of sub-claim (c) needs to validate which candidate is the right $\chi$ for the closure.*

1. **OPEN-SM-4 vs OPEN-SM-7d labeling housekeeping**: 1-patch fix renaming throughout the SF-4 + SF-2 + (newly) Research_Timeline.md corpus to use OPEN-SM-4 consistently. Should happen before paper drafting opens. *Updated note: Patch 0377 (Research_Timeline.md) propagated the "OP-SM-7d" labeling into the new medium-term scheduling artifact — Priority 1 entry. The housekeeping rename should cover this new file as well, plus the same six SF-line artifacts listed in §1.1.*

2. **Sub-claim (c) Wigner-Eckart perturbation framework setup** (promoted from Session 86-87 priority to Session 86 priority following the Session 85 χ-candidate enumeration): construct the $\hat{V}_\chi$ perturbation operator on the TBM-aligned basis at theorem level, identify the Wigner-Eckart coefficients $v_{ij}$ from 600-cell geometry, and compute the leading TBM angle corrections. The sub-claim (c) calculation determines which of the candidate χ-values from §9 is consistent with the empirical data, replacing pattern-matching with derivation.

3. **Confirmation from Thomas on the six open questions in §6**: should ideally happen at start of next session before §5.2 work begins. Q3 in particular (is χ φ⁻¹, φ⁻², φ⁻³, 1/√5, or something else?) now has a sharper computational ground: the bias parameter from the edge-to-1 ratio is $\phi^{-3}$, but Picture A/B/C/D may motivate a different χ via mechanism-specific arguments.

4. **Picture B Patch 0367 sketch advancement** (deferred priority): the W⁰ centroid-decoupling sketch needs the three-Layer development (operational definition + post-emergence direction quantification + V-A phenomenology bridge) before sub-claim (e) closure work begins.

---

## §8 Findings registered to date

- **Finding C-1.** The Grok exploratory δ_CP formula $\delta_{CP} \approx 180° + (\chi \times 360°/\phi^2 - 180°)$, when evaluated directly with $\chi = \phi^{-1} \approx 0.618$, does not give 195°; it gives 84.97° (if sign(bias) = +1) or 264.97° (if sign(bias) = −1). The claim δ_CP ≈ 195° from this formula needs re-derivation from scratch. The formula may be mis-stated in the archive, or the sign/structure may be applied in a way not visible from the document.
- **Finding C-2.** The Grok exploratory sin²θ₁₃ formula $\sin^2\theta_{13} \approx \phi^{-2}/[\text{coefficient}]$ does not give the right magnitude under simple coefficient values. The intended formula needs re-derivation or the coefficient needs identification from CPP geometry.
- **Finding C-3 (REGISTERED Session 85).** The OP-SM-4 archive's derivation of $\chi = \phi^{-2}$ from the edge-ratio symmetric-bias calculation contains an arithmetic error in the final simplification step. The archive wrote "$(1 - \phi^{-1})/(1 + \phi^{-1}) = \phi^{-1}/\phi = \phi^{-2}$", but the correct simplification using $\phi - 1 = 1/\phi$ and $\phi + 1 = \phi^2$ gives $(1 - \phi^{-1})/(1 + \phi^{-1}) = (1/\phi)/\phi^2 = \mathbf{\phi^{-3}} \approx 0.236$. The error lost one factor of $1/\phi$ in the simplification. The corrected dimensionless symmetric-bias χ from the φ:1 length-ratio in the 600-cell is $\chi = \phi^{-3}$, not $\phi^{-2}$. See §9 for the verification and §10 for what this implies for the down-stream sub-claims.
- **Finding C-4 (REGISTERED Session 85).** The 600-cell has **eight distinct pairwise distances** at unit circumradius — not two, as the OP-SM-4 archive's "two edge types with ratio φ:1" framing implied. The eight distances are $\{1/\phi, 1, \sqrt{3-\phi}, \sqrt{2}, \phi, \sqrt{3}, \sqrt{(5+\sqrt{5})/2}, 2\}$. All 720 edges have a *single* length $1/\phi$; the polytope is regular and edge-uniform. The φ:1 ratio that motivates Capotauro's bias parameter is the edge-to-first-non-edge-distance ratio ($1/\phi$ to $1$), not a "two edge types" structure. See §9 for the full distance table.
- **Finding C-5 (Session 85 numerical observation; not derivation).** With the corrected $\chi = \phi^{-3}$, the formula $\delta_{CP} = 180° + \arctan(\chi)$ evaluates to $193.28°$, within $2°$ of the NuFIT 6.0 empirical central value $195° \pm 40°$. This is a numerical proximity observation, not a derivation; the actual $\delta_{CP}$ formula must come from the sub-claim (c) Wigner-Eckart-style perturbation calculation, not from pattern-matching. Registered as a numerical signpost that supports the corrected $\chi = \phi^{-3}$ value but does not validate it.
- **Finding C-6 (RETRACTED Session 85).** *Earlier working claim that $\sin^2\theta_{13} \approx \phi^{-9} \approx 0.021$ matches the empirical value $0.0220$ at 3%.* Direct computation gives $\phi^{-9} \approx 0.0132$, a 40% deviation from empirical, not 3%. The pattern-match claim is withdrawn. No simple $\phi^{-n}$ power matches $\sin^2\theta_{13}$ at the 5%-or-better level. The sin²θ₁₃ value must come from the sub-claim (c) Wigner-Eckart calculation, not from $\chi^n$ pattern-matching.

---

## §9 Session 85 computational findings — 600-cell distance structure and corrected χ derivation

This section captures the Session 85 computational verification work targeting §5.1 sub-claim (b) χ-value resolution. The computations are based on standard 600-cell vertex coordinates at unit circumradius:

- **Class 1 (8 vertices):** $(\pm 1, 0, 0, 0)$ and the 7 other axis permutations.
- **Class 2 (16 vertices):** $(\pm \tfrac{1}{2}, \pm \tfrac{1}{2}, \pm \tfrac{1}{2}, \pm \tfrac{1}{2})$.
- **Class 3 (96 vertices):** even permutations of $(0, \pm \tfrac{1}{2\phi}, \pm \tfrac{1}{2}, \pm \tfrac{\phi}{2})$, with the 2³ = 8 sign combinations on the three non-zero positions.

Total $8 + 16 + 96 = 120$ ✓; all on the unit 3-sphere.

### §9.1 Distance spectrum (Finding C-4)

Direct computation of all $\binom{120}{2} = 7140$ pairwise distances yields **eight distinct values**, with the following multiplicities:

| Distance | Closed form | Number of vertex pairs | Identification |
|---:|:---:|---:|:---|
| 0.618034 | $1/\phi$ | 720 | **edge** (all 720 edges, single length) |
| 1.000000 | $1$ | 1200 | first non-edge shell |
| 1.175571 | $\sqrt{3 - \phi}$ | 720 | second non-edge shell |
| 1.414214 | $\sqrt{2}$ | 1800 | $90°$ apart on the 3-sphere |
| 1.618034 | $\phi$ | 720 | median shell |
| 1.732051 | $\sqrt{3}$ | 1200 | golden-section apart |
| 1.902113 | $\sqrt{(5+\sqrt{5})/2}$ | 720 | near-antipodal shell |
| 2.000000 | $2$ | 60 | **antipodal pairs** (each vertex with its antipode) |

Vertex degree under the edge relation: 12 for all 120 vertices (verified). Total edges: 720 ✓ (consistent with the 600-cell's known $V=120, E=720, F=1200, C=600$ structure).

**Finding C-4 implication.** The "two edge types with ratio $\phi : 1$" framing in the OP-SM-4 archive sub-problem 2 is factually imprecise. The 600-cell is a regular polytope with a single edge length. The $\phi : 1$ ratio that motivates the symmetric-bias parameter is the **edge-to-first-non-edge-distance** ratio ($1/\phi$ to $1$), not a "two edge types" structure. The bias parameter is well-defined; the original framing was loose.

### §9.2 The χ arithmetic correction (Finding C-3)

The OP-SM-4 archive computes:
$$\chi = \frac{\phi^{-1} - \phi^{-2}}{\phi^{-1} + \phi^{-2}} = \frac{1 - \phi^{-1}}{1 + \phi^{-1}} = \frac{\phi^{-1}}{\phi} = \phi^{-2}$$

The final equality is the error. The correct simplification uses two golden-ratio identities:
- $\phi - 1 = 1/\phi$ (the defining property of the golden ratio)
- $\phi + 1 = \phi^2$ (since $\phi^2 = \phi + 1$ is the golden-ratio quadratic)

Substituting:
$$\frac{1 - \phi^{-1}}{1 + \phi^{-1}} = \frac{(\phi - 1)/\phi}{(\phi + 1)/\phi} = \frac{\phi - 1}{\phi + 1} = \frac{1/\phi}{\phi^2} = \frac{1}{\phi^3} = \boxed{\phi^{-3}}$$

Numerical verification: $1/\phi^3 = 0.236068$. The archive's claimed value $\phi^{-2} = 0.381966$ is off by exactly one factor of $1/\phi$ (the ratio $0.236068 / 0.381966 = 0.618034 = 1/\phi$ confirms the missing factor).

**Finding C-3 conclusion.** The dimensionless symmetric-bias parameter from the edge-to-first-non-edge length ratio in the 600-cell is $\chi = \phi^{-3} \approx 0.236$. The archive's $\chi = \phi^{-2}$ is an arithmetic error. The $\phi^{-1}$ value used elsewhere in the Grok exploratory work is *not* a normalized bias parameter; it is the bare edge length in unit-circumradius normalization, which is a length not a dimensionless ratio.

### §9.3 Candidate χ enumeration from natural geometric pairs

A more systematic enumeration: for each pair (edge length, other-shell distance), compute the dimensionless symmetric-bias $\chi = (L_\text{long} - L_\text{short})/(L_\text{long} + L_\text{short})$. With $L_\text{short} = 1/\phi$ fixed (edges):

| $L_\text{long}$ | $L_\text{long} / L_\text{short}$ | $\chi$ | Closed form | Numerical |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | $\phi$ | $(\phi - 1)/(\phi + 1)$ | $\phi^{-3}$ | 0.236068 |
| $\sqrt{3 - \phi}$ | $\phi\sqrt{3-\phi}$ | (mixed) | — | 0.310847 |
| $\sqrt{2}$ | $\phi\sqrt{2}$ | (mixed) | — | 0.391773 |
| $\phi$ | $\phi^2$ | $(\phi^2 - 1)/(\phi^2 + 1) = \phi / (\phi + 2)$ | $1/\sqrt{5}$ | 0.447214 |
| $\sqrt{3}$ | $\phi\sqrt{3}$ | (mixed) | — | 0.474033 |
| $\sqrt{(5+\sqrt{5})/2}$ | $\phi\sqrt{(5+\sqrt{5})/2}$ | (mixed) | — | 0.509525 |
| $2$ (antipodal) | $2\phi$ | $(2\phi - 1)/(2\phi + 1) = \sqrt{5}/(2+\sqrt{5})$ | $5 - 2\sqrt{5}$ | 0.527864 |

The cleanest closed-form values are at the "natural" geometric pairs: $\chi = \phi^{-3}$ (edge-to-1), $\chi = 1/\sqrt{5}$ (edge-to-φ), and $\chi = 5 - 2\sqrt{5}$ (edge-to-antipode). The other entries (`mixed`) are not simple φ-quantities.

**Observation.** The value $\phi^{-2} \approx 0.382$ that the OP-SM-4 archive intended for χ does not correspond to *any* of these natural bias-pair calculations. The closest natural value is $\phi^{-2} \approx 0.382$ vs $\phi\sqrt{2}/(\phi\sqrt{2}+\text{...}) \approx 0.392$ (the edge-to-$\sqrt{2}$ bias) — but these differ by 3%, and $\sqrt{2}$ is not a "natural" partner for the chirality bias (it is the $90°$-apart inner-product distance, which is geometrically uncorrelated to the chiral structure). The $\phi^{-2}$ value should be retired as a candidate.

### §9.4 Numerical observations on δ_CP and sin²θ₁₃ candidate formulas

With $\chi = \phi^{-3}$ in hand, several numerical proximity-checks are worth running as *signposts*, not derivations:

**δ_CP via $180° + \arctan(\chi)$ pattern.** Three candidate χ-values plugged into $\delta_{CP} = 180° + \arctan(\chi)$:

| $\chi$ | $\arctan(\chi)$ | $180° + \arctan(\chi)$ | Distance from empirical 195° |
|:---:|:---:|:---:|:---:|
| $\phi^{-3} \approx 0.236$ | $13.28°$ | **$193.28°$** | $1.72°$ |
| $\phi^{-2} \approx 0.382$ | $20.91°$ | $200.91°$ | $5.91°$ |
| $1/\sqrt{5} \approx 0.447$ | $24.09°$ | $204.09°$ | $9.09°$ |

The $\chi = \phi^{-3}$ candidate gives the closest match by a factor of 3–5 over the other candidates. **Finding C-5 registered as a numerical signpost.** This does *not* validate the $180° + \arctan(\chi)$ formula at theory level — the formula must come from the sub-claim (c) Wigner-Eckart calculation. But the numerical proximity is supportive of the corrected $\chi = \phi^{-3}$ value.

**sin²θ₁₃ via $\chi^n$ patterns.** With $\chi = \phi^{-3}$, the simple powers give:
- $\chi^2 = \phi^{-6} = 0.0557$ — 2.5× too large vs empirical 0.0220.
- $\chi^3 = \phi^{-9} = 0.0132$ — 40% too small vs empirical 0.0220.

**No simple $\chi^n$ power matches sin²θ₁₃ at the 5%-or-better level.** This is **Finding C-6 (retracted): my earlier working claim that $\sin^2\theta_{13} \approx \phi^{-9}$ at 3%** was numerically wrong (I conflated $\phi^{-9} \approx 0.013$ with empirical $\approx 0.022$; the actual gap is 40%). The numerical-coincidence path for sin²θ₁₃ is closed; the value must come from sub-claim (c) Wigner-Eckart calculation with explicit cage-shell overlap factors, not from pattern-matching.

### §9.5 What the corrected χ resolution does and does not deliver

**Delivered at Session 85 close.**
- The OP-SM-4 archive arithmetic error is identified and corrected: $\chi = \phi^{-3}$, not $\phi^{-2}$.
- The 600-cell distance structure is computationally verified: eight distinct pairwise distances, all 720 edges at single length $1/\phi$.
- The candidate χ-table from natural geometric pairs is enumerated; three have clean closed forms ($\phi^{-3}$, $1/\sqrt{5}$, $5-2\sqrt{5}$).
- A numerical signpost for δ_CP at $\chi = \phi^{-3}$: $180° + \arctan(\phi^{-3}) = 193.28°$, within $2°$ of empirical $195°$.
- Two prior Grok-exploratory numerical claims are now resolved at the "needs proper derivation" level (Findings C-1, C-2, C-6).

**NOT delivered at Session 85 close.**
- The χ-value at *theorem level*. The corrected $\phi^{-3}$ is a candidate; the sub-claim (c) Wigner-Eckart calculation has to validate that this is indeed the χ that the K3-doublet perturbation responds to. Other candidates from §9.3 remain in play until the perturbation framework is constructed.
- The $\delta_{CP}$ formula at theorem level. The $180° + \arctan(\chi)$ proximity is a numerical observation, not a derivation. The actual formula must emerge from sub-claim (c).
- The $\sin^2\theta_{13}$ formula at any level. Pattern-matching is closed; only sub-claim (c) can deliver it.

---

## §10 Implications for sub-claim (c) and the closure architecture

The Session 85 χ-resolution work sharpens sub-claim (c) in three ways:

**One.** The candidate χ-values to test against the Wigner-Eckart matrix elements are now down to three cleanly-derived values ($\phi^{-3}$, $1/\sqrt{5}$, $5 - 2\sqrt{5}$) rather than the loosely-stated archive value $\phi^{-2}$ plus the un-normalized edge-length $\phi^{-1}$. The numerical signpost for δ_CP favors $\phi^{-3}$. Sub-claim (c) should compute the perturbation matrix elements explicitly and verify which χ candidate is selected by the geometric overlap structure.

**Two.** The Wigner-Eckart calculation has a specific input it needs from §3 mechanism candidates: which geometric pair (edge-to-1, edge-to-φ, or edge-to-antipodal) corresponds to the "chirality-broken" symmetric bias in the substrate-level mechanism Thomas selects from Q1 of §6. Picture A (global enantiomorph selection) most naturally corresponds to a *global* symmetric bias which would use the longest characteristic ratio — likely edge-to-antipodal $\chi = 5 - 2\sqrt{5}$. Picture C ($H_4 \to I_4$ branching) corresponds to a *symmetry-orbit* bias which would use the natural orbit-size ratio — likely the edge-to-φ $\chi = 1/\sqrt{5}$, since $|H_4| / |I_4| = 2$ and the φ-quantities in $I_4$ are mediated by $1/\sqrt{5}$ (related to the eigenvalues of the icosahedral group representation). Picture B (W⁰ centroid-decoupling) corresponds to a *local* bias which would use the nearest-neighbor ratio — edge-to-1 $\chi = \phi^{-3}$. **The δ_CP numerical proximity at $\chi = \phi^{-3}$ favors Picture B as the source of the chirality bias visible in PMNS-sector observables.** This is a substantive structural finding: it points the closure architecture toward the W⁰ centroid-decoupling local-mechanism story (the Patch 0367 sketch), even though Picture A (global enantiomorph selection) is the more familiar Capotauro framing.

**Three.** The closure architecture recommendation from §3.5 (pursue Pictures A + B + C jointly as three convergent candidates) is partially refined: Picture B is now indicated as the primary mechanism for the PMNS-observable content, with Picture A potentially as the *substrate-level cause* of the local bias Picture B describes, and Picture C as the *representation-theoretic machinery* for the perturbation. This is the SF-4 v4.0 pattern at a different level — multiple mechanism candidates converging on a single closure when they describe complementary facets of the same underlying physics.

**Implication for the Capotauro paper structure (when drafting begins).** The dedicated paper should likely follow the SF-4 v4.0 architecture: open with the substrate-level mechanism (Picture A), develop the local manifestation (Picture B = W⁰ centroid-decoupling), and execute the representation-theoretic perturbation at the K3-doublet level (Picture C → Wigner-Eckart). The χ-value $\phi^{-3}$ enters as the dimensionless coupling at the bridge between Picture A and Picture B. Each Picture contributes a clause to the composite closure theorem; the cross-sector closure with OPEN-FP-SF-2-CHIR rides on Picture B specifically.

---


## §11 Scope and external references

**This sketch document is the canonical Tier-4 reasoning capture for the Capotauro closure campaign.** It is paired with:

- The OP-SM-4 archive file: `archive/pre_frontier_2026-04-12/open_problems/OP-SM/OP-SM-4_capotauro_mechanism.md` (original problem statement, sub-problems, observable targets).
- The Grok exploratory work: `archive/grok-exploratory-SM/p2-neutrino-mixing-angles/{delta-cp-phase-derivation.md, lattice-subgroups.md, capotauro-bias.md}` and `archive/grok-exploratory-SM/p2-charge-screening-and-asymmetries/capotauro-bias.md` and `archive/grok-exploratory-SM/p2-full-cosmology/big-bang-to-capotauro.md`.
- SM-2 Appendix H: `series_standard_model/papers/SM-2_mass_generation_geometric_hierarchies.tex` §Quark Charge Asymmetry and Capotauro (lines 456–470).
- SF-4 v4.0 Composite K3-Cage-Shell Coupling Theorem closure sketch: `flagship_papers/neutrinos/sketches/SF-4_open_fp_sf_4_2_closure.md` (the methodological template).
- SF-2 v1.0 W⁰ catalyst framework: `flagship_papers/electroweak/sf-2_electroweak.tex` §5 (PROP-SF-2-1 through PROP-SF-2-6).
- W⁰ neutrino scattering centroid-decoupling sketch: `flagship_papers/electroweak/sketches/W0_neutrino_scattering_centroid_decoupling.md` (Patch 0367; Picture B local-mechanism candidate).
- Cross-sector closure framework: `templates/conditional_closure_framework.md` (PD-005 four-tier subsumption; Finding β-10 cross-sector closure pattern).

**This sketch makes no claim of theorem-level closure at Session 85.** All sub-claims (a) through (f) are open. The sketch establishes the setup, foundational inputs, mechanism candidates, sub-claim decomposition, and first-pass work plan; Session 85 (§9–§10) advances sub-claim (b) χ-resolution work with the corrected $\chi = \phi^{-3}$ derivation and the candidate enumeration. Subsequent sessions develop each sub-claim toward conditional theorem-level closure on the SF-4 v4.0 methodology template.

**Maintainer:** Claude Opus 4.7 (computation + structural arguments), Thomas Lee Abshier ND (physical intuition + strategic frame + mechanism prioritization). Established Session 84 (Patch 0376, 14 May 2026). Extended Session 85 (Patch 0378, 15 May 2026) with §9 + §10 χ-resolution computational findings.
