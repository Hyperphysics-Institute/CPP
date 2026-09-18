<!--
  Extracted from Research_Frontier.md lines 865-1019
  Source range: Standard Model Emergence
  Extraction date: 2026-05-25
  Master dashboard: Research_Frontier.md
-->

## Standard Model Emergence (SM) — 11 problems

> **CROSS-LANE NOTE FROM THE GR LANE (Patch 3372, 2 Sep 2026) — SM-11 (line ~568) and SM-12 (line ~986) attribute
> `PSR_eff ≥ l_P/2` to "the CP Exclusion Rule (companion 1)".** That rule is THEO-1 (demoted postulate; constrains
> co-occupation, not the PSR) and c01 never contained it. The `l_P/2` floor is now a **conditional Buchdahl BOUND with an
> open value**, window 0.536 < u_max ≤ 1 (GR-1c Corrigendum 3; CONV-038 5/5; founder R-FLOOR-FINITE / R-CELL-SIZE-OPEN).
> **Owed (SM lane):** dated notes at both sites; and an SM-lane answer to whether asymptotic-freedom attenuation (SM-11)
> and the ĥDP vertex-separation scale (SM-12) are SENSITIVE to the floor value across the window. Sweep:
> `series_gravitation/rcore_derivation/3372_exclusion_dependency_sweep.md`.

### OPEN-SM-3: Derive ε = −0.145 from Lattice Geometry
**Status:** OPEN
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** Derive the perturbative correction ε from multi-layer averaging, entropy weighting, and holographic damping.
**What a solution looks like:** Explicit computation of ε from 600-cell geometry extending α_EM precision.
**Dependencies:** Independent of OPEN-SS-9 (topological δ=1/3 does not use ε)
**Cross-sector connections:** α_EM precision beyond 4 digits
**Current best lead:** Multi-layer entropy average over generations; sign issue identified in α_EM series.
**Paper(s):** SM Paper 2
**Last updated:** 23 March 2026

---

### OPEN-SM-4: Formalise the Capotauro Mechanism
**Status:** OPEN (PARTIAL CLOSURE — sub-claim (c) v1.0 SHIPPED via Capotauro paper v1.0 Session 122 Patch 0415; THEO-CAP-1 registered Session 103 Patch 0397; sub-claims (a) Capotauro nucleation event and (b) substrate chirality mechanism candidate derivation remain open with Reading C geometric-chirality candidate sketch registered Session 121 Patch 0414 as **OPEN-FI-C-9-FP-MECHANISM** in the FP section)
**Sector(s):** SM, SR
**Priority:** HIGH
**One-line statement:** Derive the lattice chirality-activation event that establishes χ = φ⁻³ and produces CP violation. *(φ⁻¹ was the original pre-Session-86 conjecture, superseded at Finding C-3 Patch 0378 — lost-1/φ arithmetic error φ⁻²→φ⁻³; the live magnitude is |χ| = φ⁻³ ≈ 0.236 per FI-C-9 / THEO-CHIR-CHI-1 / Capotauro v1.0–v2.0. Corrected Patch 0670.)*
**What a solution looks like — RESTATED at Patch 4003 (EW lane) after a D-2 premise audit. The 16 May wording is preserved at the end of this block.**

**(i) `derive χ = φ⁻³` is DISCHARGED, not open.** Capotauro v2.0 derives |χ| = φ⁻³ from the perturbative-distance-ratio constraint on n̂-induced edge perturbations, replacing v1.0's free magnitude postulate; CHI-1 builds it as the first-shell distance ratio (1−φ⁻¹)/(1+φ⁻¹) = φ⁻³ **exactly** (verify `series_standard_model/code/4003_sm4_premise_audit.py`). Listing it as work still to do sends a worker after a landed result.

**(ii) The SSB framing is in tension with a review-closed theorem this entry does not cite.** FI-C-9 was reframed at Patch 0413 from *substrate-vacuum broken-symmetry order parameter* to *primitive substrate feature*. More sharply, **THEO-CHIR-VW-1** (Patch 0680; review-closed 3/3 at 0682, v1.1) argues that conditional on **H1** — the DSL measure is reflection-positive — μ² > 0 and η = 0, i.e. **the det-coset ℤ₂ cannot break spontaneously within the substrate axioms at all**, with the observed FI-C-9 ≠ 0 then either V3-by-principle or **bridge-sourced**. So `[600-cell] × ℤ₂ → [600-cell]` read as a spontaneous event is the thing VW-1 closes off, not the target to aim at.

**(iii) What is actually left, restated at Patch 4004.** **(H-NESS) branch (ii) — the "justified single-site reduction" — is CLOSED, and not for want of justification: it is ill-posed.** A susceptibility is a number-*fluctuation*, and for a single walker Var(N_tot) ≡ 0, so Σ_{v,w}⟨n_v n_w⟩_c = 0 identically and χ = 0, m² = ∞ — degenerate at zeroth order, for a reason with nothing to do with the substrate (verify `series_standard_model/code/4004_mu2_occupation_extension.py` T3). There was never a reduction to find. **PD-007 working extension adopted at 4004, labelled `[PCD-EXT]`: the occupation generator on a proper subvolume**, where Var(n_S) = K p_S(1−p_S) > 0 — the definition that makes the recompute well-posed. **A tempting diagnosis was tested and rejected first (T2):** the −π_vπ_w anticorrelation is *not* a hard-core-exclusion artifact and is *not* closed by R-EXCL-RETIRED — an exclusion-free multinomial gives −Kπ_vπ_w, same sign; the negativity comes from the fixed total. **Original 4003 wording:** two named gaps, not an open derivation. Sub-claims (a)/(b) **are** `B-iii` of the CHIR↔EW bridge (Patch 0662), already decomposed and twice reduced: **B-iii-(i) capacity ⟺ sign(μ²)** in a ℤ₂-even Landau potential V(η) (Patch 0668), then **sign(μ²) = sign(m²)** from the symmetric-part η-susceptibility (Patch 1100; λ₁ = 2.2918, graph-Laplacian zero-mode dominated; the O(δ³) current is sign-*perturbing*, not sign-*setting*). The residuals are **(H1)** — is the DSL measure reflection-positive? — and **(H-NESS)** — does the single-walker π's η-susceptibility track the η-field potential curvature sign, and what supplies m² from π?

**(iv) CORRECTED AT PATCH 4004 — the previous wording of this clause was wrong.** 4003 wrote that (H1) and (H-NESS) were *idle since 8 June*, on a grep scoped to `frontier_sectors/` and `todolist.md` whose result was generalised to the whole repo. **Repeated unscoped it is false:** the lift was worked at **0812** (go/no-go), **0813** (Steps 1–2: the 600-cell η and the symmetric χ_η), corrected at **0814/0815** by the DM/F.1 lane, and assessed by the chirality lane at **0904/0905**. 0813 computed χ_η = 0.87–1.01, finite and positive ⇒ μ² > 0, η = 0 stable; **0904 corrected the framing** — μ² > 0 is the *unbroken* branch, so V3 is confirmed and V1-by-condensation is foreclosed on it, inverting 0813's "emergent" label. **But 0904 §3 and 0905 are the live point:** that finiteness follows near-tautologically from a **product (ZRP-template) base that was assumed**, and 0814 found the real Mechanism-A NESS **departs from it, skewed at O(δ)**. So the parked item is a **recompute of χ_η on the real measure**, not a lift. *What survives from 4003: this entry cites none of it, and `todolist.md` carried none of it — a record is not a queue.* **Original 4003 wording:** The gating computation has been CLEARED since June and nobody has run it. Patch 0692: *"the μ²-sign computation is now cleared on the reviewed foundation."* THEO-CHIR-CAPACITY-1, reserved then, was **ENACTED at Patch 0960**, and the two arms that gated it — Mechanism A and pointwise non-degeneracy — were discharged at 0960 and 0968. `H-NESS` occurs in exactly one live file in this repo: `frontier_sectors/CHIR.md`'s 8 June header line. **Three months idle, on what the corpus itself calls the sole verdict-moving engine.**

**(v) Still genuinely open and unrestated:** reproduce δ_CP ≈ 195° (a *signpost only* per B-ii, gated behind (a)/(b)), sin²θ₁₃ ≈ 0.022, and the baryon asymmetry.

*Original 16 May 2026 wording, preserved:* Symmetry breaking [600-cell] × ℤ₂ → [600-cell]; derive χ = φ⁻³; reproduce δ_CP ≈ 195°, sin²θ₁₃ ≈ 0.022, and baryon asymmetry.
**Dependencies:** ~~None blocking (but requires EW development)~~ — **the EW-development condition is MET as of 14 Sep 2026**: the EW lane is open (block 4000–4099, `G-EW-BLOCK-4000`) and holds this item. The live blockers are now **(H1)** and **(H-NESS)** at (iii) above — not a missing lane.
**Cross-sector connections:** OPEN-SM-5 (PMNS), matter-antimatter asymmetry, cosmology; **CHIR ↔ electroweak bridge (Patch 0662): OPEN-SM-4 is the SM/SR co-owner of OPEN-CHIR-3 ∪ 1d-β-v** — the Capotauro chirality-activation event ([600-cell] × ℤ₂ → [600-cell]) is conjectured to be the substrate chiral-vacuum transition STATUS-2 derived (H₄ → H₄⁺, the same index-2 ℤ₂; the "ℤ₂-match" lead) and thereby EWSB (**CONJ-CHIR-1**); FI-C-9 = the P-face (EW parity violation), the T-arrow `sign(δ)` = the T-face (δ_CP), CPT-unified (TARROW-1). δ_CP and Δp_LR = χ/6 = φ⁻³/6 are the magnitude anchors. Scope sketch: `series_umbrella/series_substrate_chirality_arc/chirality_derivations/sketches/chir_ew_bridge_scoping.md`.
**Current best lead:** **Sub-claim (c) v1.0 SHIPPED via Capotauro paper v1.0 Session 122 Patch 0415** (paper at `series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex` v1.0; theorem-registry registration Session 103 Patch 0397 as THEO-CAP-1; first programme-level theorem registered ahead of its own flagship paper publication in the CPP corpus): Composite Capotauro Wigner-Eckart Theorem $|M| = |\langle\Phi_-^{(1)}|\hat{C}_\chi|\Phi_-^{(2)}\rangle| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ on K3-doublet, derived as chirality-eigenvalue matching factor $\chi$ (Session 96, $b = \chi/\sqrt{3}$ from spectral radius of unique $A_2$ generator $S$) times cage-shell averaging factor $1/6$ (Session 97, $d_E/V_\text{cage} = 2/12$). **Primary empirical prediction $\Delta p_{LR} = \chi/6 \approx 0.0394$ validated within 2%** of observed $\sim 0.04$. Conditional theorem closure on FI-C-1 through FI-C-10 + 4 CPP axioms (A1, A3, A4, A7). FI-C-9 substrate primitive chirality magnitude $|\chi| = \phi^{-3}$ registered Session 87 Patch 0381 as foundational input (reframed Session 120 Patch 0413 from "substrate-vacuum broken-symmetry order parameter" to "primitive substrate feature" per CPP core methodological principle that mathematical descriptions are not physical mechanisms — see v0.9 §2 reframe); FI-C-10 cage-shell extension to chirality observables registered Session 97 Patch 0391 as new foundational input. 34 findings registered (C-W1 through C-W34) across 16-session closure trajectory (Sessions 87-102). **Sub-claim (b) candidate mechanism**: Reading C geometric-chirality candidate (a primitive 4D direction $\hat{n}$ in the substrate's ambient 4D space producing direction-correlated edge-length variation at the $\phi^{-3}$ scale) registered Session 121 Patch 0414 with working sketch `series_umbrella/series_substrate_chirality_arc/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md` (296 lines); structural argument that $|\chi| = \phi^{-3}$ is the first viable perturbative-distance-ratio scale forced by the substrate-structure-preservation constraint; H₄ → I₄ algebraic reduction reinterpreted as structural consequence of $\hat{n}$ being primitive rather than dynamical outcome of SSB. Tracked at FP-section as **OPEN-FI-C-9-FP-MECHANISM**. **Sub-claim (a)** Capotauro nucleation event (universe-wide sign-selection event downstream of sub-claim (b) magnitude mechanism) remains open. *(Advisory, NON-BINDING speculation — not a claim, moves no verdict, not reviewed: a founder's-vision discussion of the sign-selection EPOCH — early causal-contact/inflationary imprint vs late precipitation vs R/L domains — mapping the domain-wall constraint (Zel'dovich–Kobzarev–Okun), the matter–antimatter domain-cosmology exclusion (Cohen–De Rújula–Glashow), the inflation + EU-1 contact-era reconciliation, and the live (contested) observational handles (galaxy 4PCF parity tests, CMB birefringence) is recorded at `founders_vision/physical_metaphysical_speculation/2026-06-09_chirality_primitive_QGE_and_imprint_epoch.md`. Advisory only; do NOT lift into the frontier without independent derivation + review.)* **Q11 sin²θ₁₃ derivation from $|M| = \chi/6$ re-scoped to SF-2 v2.0+ work** (Session 101 Patch 0395): standard PMNS perturbation predicts quadratic scaling $\propto |M|^2 \approx 0.001$ (off by factor 21); candidate γ structural observation $\sin^2\theta_{13} = b \cdot m_\perp \approx 0.0227$ matches observation within 1σ but lacks rigorous derivation; wavefunction-level coupling hypothesis ruled out Session 101. Earlier (pre-Session 87): δ_CP ≈ 195° matches NuFIT; mechanism physically motivated but not formalised.
**Paper(s):** **`series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex` v1.0 SHIPPED Session 122 Patch 0415** (46 pages, 601 KB PDF at v0.9; v1.0 SHIP is version-bump only with no content change; cross-reviewer convergence on SHIP-readiness across ChatGPT round-3 + CoPilot round-1 + Grok round-1 at v0.8 Session 119 Patch 0412; v0.9 polish Patch 0413 incorporated 8 ADDRESS items + 2 DISCOVERABILITY items + foundational framing reframe of §2 from SSB to primitive-feature framing); working sketches `series_umbrella/series_substrate_chirality_arc/capotauro/sketches/Capotauro_subclaim_c_wigner_eckart.md` §18 (Theorem 18.1) + §22 (v1.0 closure summary); parent sketch `Capotauro_chi_phi_closure.md` §1.3 (FI-C-9, FI-C-10) + §1.8 (Sessions 87-102 closure trajectory); mechanism candidate sketch `Capotauro_chiral_mechanism_candidate.md` (Session 121 Patch 0414 — Reading C development for sub-claim (b)); SM Paper 2 Appendix H (legacy reference).
**Last updated:** 15 Sep 2026 (Patch 0983, chirality lane — **H1: NEITHER REFUTED NOR CONDITIONALLY RESTORED. The 4022–4062 arc tested the SPATIAL parity on the occupation law; H1 as VW-2 v1.1 defines it is Θ_OS (Euclidean time-reflection) positivity, ⟺ VW-a-4, δ = 0 base case proved.** (H1) as a B-iii residual is **OPEN exactly as it was before 4022**; δ_CP long-horizon contingencies (4059) OPEN on that. 4056/4057 "refuted" and 4062 "open (conditional)" both withdrawn as H1 statements. See `chirality_derivations/reasoning/0983.md`. Previous: Patch 4062, EW lane — **H1 REFUTED → OPEN (CONDITIONAL).** PD-008 critique: 4056/4057's fixing-sector violation is an O(1/K) fixed-total artifact of treating one 600-cell as isolated; conservation is continuity with flux (GR-FE-1) and the substrate is tessellated (A2), and VW-1 locates RP in the CONT-1 limit where the violation is zero. H1 open on (a) non-interacting walkers and (b) Θ-symmetry of the tessellated generator. **(H1) as a B-iii residual is therefore OPEN, not refuted, and the δ_CP long-horizon contingencies (4059) are OPEN.** Convenient branch, marked and submitted. Previous: Patch 4060, the 40-file H1 sweep; VW-1 has three hypotheses H1+H2+H3.)

---

### OPEN-SM-5: PMNS Mixing Angles — Analytic Derivation
**Status:** OPEN
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** Derive PMNS mixing angles analytically from 600-cell subgroup overlaps.
**What a solution looks like:** Exact overlap fractions |G_i ∩ G_j|/|G_i| for all pairs, with normalisation derived (not fitted), matching NuFIT to 3–4 digits.
**Dependencies:** OPEN-SM-4 (Capotauro — needed for θ₁₃ and δ_CP)
**Cross-sector connections:** OPEN-G-1, lepton series
**Current best lead:** MC results match NuFIT to 3–4 digits; normalisation currently fitted. Subgroup overlap analysis: sin²θ₁₂ = 12/40 = 0.300, sin²θ₂₃ = 12/21 ≈ 0.571. **(Patch 1209 SF-2-campaign assessment — `flagship_papers/electroweak/review/C7_PMNS_normalization_closure_route.md`):** sin²θ₁₂ = 0.300 is on a JUNO *falsification* trajectory — JUNO 2025 first result gives sin²θ₁₂ = 0.3092 ± 0.0087 (1.06σ from 0.300 now → ~3σ at JUNO ultimate precision σ ≈ 0.003); 21 ∤ |H₄| = 14400, so 12/21 cannot be a clean overlap fraction |G_i ∩ G_j|/|G_i| (structural confirmation the normalisation is fitted, not derived); and sin²θ₂₃ is a DUNE/T2HK atmospheric target, not a JUNO observable. **Gate before any group-theoretic closure:** test whether the stabiliser-overlap construction *forces* 0.300 (→ falsification risk) or can flex toward JUNO's central 0.309 (→ viable). Until then the OPEN-SM-5 θ₁₂ value is HIGH-RISK for external-validation use.
**Paper(s):** SM Paper 2
**Last updated:** 13 June 2026 (Patch 1211 — SF-2-campaign assessment appended: JUNO-2025 falsification-trajectory + Lagrange-21 diagnostic + lock-to-0.300 gate, from the Patch-1209 C7 route map; original analytic-derivation lead 23 March 2026 unchanged)

---

### OPEN-SM-5b: Lepton Mass Mechanism
**Status:** OPEN
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** Derive charged lepton masses from CPP ZBW dynamics and show Koide relation follows.
**What a solution looks like:** Mass-radius relationship that reproduces m_e, m_μ, m_τ from cage geometry.
**Dependencies:** OPEN-SM-7 (Koide relation), OPEN-SM-7d (Koide phase)
**Cross-sector connections:** Lepton series paper (blocked until resolved)
**Current best lead:** ZBW eigenmode calculation (24 March 2026) gives wrong hierarchy (m_μ/m_e ≈ 965 vs observed 207). Root cause: electron cage radius ~1000× larger than muon cage.
**Paper(s):** Lepton series (planned)
**Last updated:** 24 March 2026

---

### OPEN-SM-6: Cosmological Constant from CPP Vacuum
**Status:** OPEN
**Sector(s):** SM, SR
**Priority:** MEDIUM
**One-line statement:** Derive Λ_obs ≈ 10⁻⁵² m⁻² from DP Sea dynamics, explaining 10⁻¹²⁰ suppression.
**What a solution looks like:** Paired DP cancellation mechanism giving ρ_Λ ∝ E_Planck⁴ × (l_P/R_universe)².
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-SR-5 (same problem from GR perspective)
**[Patch 1103 — CC reconciliation umbrella: SM-6 = SR-5 (one theorem).** The CC umbrella (`series_umbrella/series_cosmological_constant_arc/`, Patch 1101) finds SM-6's paired-DP cancellation and SR-5's excess-sourcing to be the same mechanism two ways: the bulk paired Sea cancels (SM side) ⇔ the uniform Sea is excess-free and inert (GR side, c05), leaving the horizon-scale uncancelled mode ρ_Λ ∝ (l_P/R_H)² — exactly SM-6's expected `E_Planck⁴ (l_P/R)²` form. The suppression is **dynamical**; the DP-Sea static ρ_sea/N⁴ reading is demoted to a present-epoch coincidence. Frontier-tracked, **NO THEO**, conditional on the c08 closed field equation. No verdict moved. See `series_cosmological_constant_arc/1101_cc_reconciliation_scoping.md`.]**
**[Patch 1161 — shared c08 condition DISCHARGED.** SM-6 ≡ SR-5 (one theorem); the CC arc's first condition — the c08 closed field equation that both faces rest on — is closed via the op:einstein closure (A3′ derives G_μν=8πG/c⁴·T_μν[LSP] at zero new params, DG-3 3/3; 1107–1108 ground the excess-sourcing in 600-cell symmetry). SM-6's "paired-DP cancellation residual" = SR-5's excess-sourcing residual now both stand on a *derived* field equation that sources from the excess, not absolute |SSV|. The arc reduces from two conditions to **one** (the event-horizon IR-scale selection). Frontier-tracked, **NO THEO**; not promoted to a derived result. See `series_phenomena/cosmology/sea_gravitation/stepD_friedmann_and_checks.md` (D2 CLOSED).]**
**Current best lead:** Pairing cancellation approach gives ~10⁻¹¹ MeV⁴ (within order of magnitude). Far better than σ=120⁻⁴ approach (~10⁻⁹).
**Paper(s):** SM Paper 2, GR companion
**Last updated:** 23 March 2026

---

### OPEN-SM-7: Derive K = 2/3 (Koide Relation)
**Status:** OPEN (PARTIAL — K3 spectral theorem proved given two postulates)
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** Prove the Koide relation K = 2/3 from CPP first principles.
**What a solution looks like:** Close OPEN-SM-7a (prove H-1) and OPEN-SM-7b (prove ZBW-1).
**Dependencies:** OPEN-SM-7a, OPEN-SM-7b (the two remaining postulates)
**Cross-sector connections:** Charge quantisation (δ=1/3) and Koide (K=2/3) share the same K₃ source
**Current best lead:** K3 spectral theorem: ρ = √(λ_max/|λ_min|) = √2 → K = 2/3. Proved algebraically. Two postulates remain open.
**Paper(s):** k3_spectral_theorem.tex
**Last updated:** 24 March 2026

---

### OPEN-SM-7d: Derive the Koide Phase θ
**Status:** OPEN (structural impossibility proved for K3+SSV; θ is electroweak)
**Sector(s):** SM, EW
**Priority:** HIGH
**One-line statement:** Derive θ_Koide = 132.7323° from CPP, explaining Δθ = 2.267° below 3π/4.
**What a solution looks like:** Identification of the EW mechanism that breaks antibonding degeneracy.
**Dependencies:** CONJ-EW-1 (Weinberg angle), CONJ-SM-6 (conditional theorem)
**Cross-sector connections:** Gates Paper 4 individual mass predictions
**Current best lead:** CONJ-SM-6 gives cos(θ) = −(2+ε)/3 with ε = 2sin²θ_W/(z+1), matching PDG to 0.003%. Conditional on CONJ-EW-1. All 11 cage-geometry candidates FALSIFIED (Sessions B–K).
**Paper(s):** Paper 4 (planned)
**Last updated:** 1 April 2026

---

### OPEN-SM-7e: Why Exactly Three Lepton Generations?
**Status:** OPEN
**Sector(s):** SM
**Priority:** MEDIUM
**One-line statement:** Derive N=3 (K₃ base vertices) from CPP, explaining why 600-cell produces tetrahedra.
**What a solution looks like:** Show tetrahedral cells are the unique structure compatible with CPP interaction rules.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-G-1, OPEN-SS-2
**Current best lead:** K(K_N) = (N+1)/(2N); only N=3 gives 2/3. Why tetrahedra (not cubes) in 600-cell is the deeper question.
**Paper(s):** Paper 3 (K3 theorem)
**Last updated:** 24 March 2026

---

### OPEN-SM-10-FEM: First-Principles Quark Mass from FEM Simulation
**Status:** OPEN
**Sector(s):** SM, SS
**Priority:** #1 forward project
**One-line statement:** Derive V^(7/3) scaling from explicit DP chain dynamics via GPU FEM simulation.
**What a solution looks like:** DP count ratios matching PDG mass ratios to <5% without calibration.
**Dependencies:** SM-8 (cage hierarchy), SM-9 (pair model)
**Cross-sector connections:** OPEN-SS-1 (quark mass formula)
**Current best lead:** GPU FEM: place cage CPs, fill DP Sea, let CPs seek targets, count organised DPs. Cascade (s,c,b) + relay (top) regimes.
**Paper(s):** SM-10 (proposal stage)
**Last updated:** 9 April 2026

---

### OPEN-SM-cage-1: Derive Scaling Exponent α = 2.38
**Status:** OPEN
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** Derive α = 2.38 (or 7/3) from 600-cell geometry for the V^α cage mass scaling.
**Dependencies:** OPEN-SM-10-FEM
**Cross-sector connections:** OPEN-SS-1
**Current best lead:** CONJ-SM9-1 proposes α = 7/3 from V² × V^(1/3) (pair counting × linear cage dimension).
**Paper(s):** SM-9
**Last updated:** 9 April 2026

---

### OPEN-SM-11: CKM Mixing Matrix and Quark CP Phase
**Status:** OPEN — **registered 18 Sep 2026, Patch 4096 (EW/SM cross-lane); corresponds to OPEN-FP-3-CKM from SF-3 §8, which promised frontier entry at ship time but was never filed.**
**Sector(s):** SM, EW
**Priority:** HIGH — **gates χ₄'s F5 filter (chirality axiom maturation, §4 filter table)**
**One-line statement:** Derive the CKM quark mixing matrix elements and the quark CP-violating phase δ_CP ≈ 65.5° from SF-2's generation-transition structure.

**Thomas's instruction (18 Sep 2026, session 233):** *"open a series and lane to refer to SF-2 for the theorem derivation as to why this CP-violating phase would be present in the Corpus."*

**What a solution looks like:** SF-2's generation-transition mechanism (which already produces the Weinberg angle sin²θ_W = 3/(8φ) and the strong coupling α_s = 5/(8φ)) is extended to derive the three CKM mixing angles θ₁₂, θ₁₃, θ₂₃ and the CP phase δ_CP. A zero-parameter derivation of δ_CP would satisfy χ₄'s F5 filter (the chirality axiom needs an O(1) substrate phase near 65.5° to account for J ≈ 3.08×10⁻⁵). A calibrated derivation (one mixing parameter fitted) would at minimum constrain the form.

**What is known (from session 233 empirical reconciliation, Patch 4096):**
- The genuine 120-vertex 600-cell has vertex-vertex angles only at multiples of 36° (36°, 60°, 72°, 90°, 108°, 120°, 144°, 180°). None is within 1.5σ of δ_CP = 65.5° ± 3.3°. **δ_CP does NOT emerge from vertex-vertex 600-cell geometry alone.**
- Two 600-cell angles bracket δ_CP: 60° (−1.67σ) and 72° (+1.97σ). Their mean is 66°. If SF-2's generation structure produces δ_CP as a mixture of these inter-shell transition angles, the magnitude can land in range. This is a conjecture, not a derivation.
- Cabibbo angle 13.04° is also not a 600-cell vertex-vertex angle (closest is 15.5°, 2.5° off).

**F5 connection (χ₄ maturation):** χ₄ conserves CP exactly (§2s, forced by CPT on the polarity clause). Therefore χ₄ gives J = 0 on its own. F5 requires a second source — candidate sign(δ) via CPT (already in corpus at W3/CHIR) **plus** an O(1) phase near 65.5° that must come from the generation-mixing structure. OPEN-SM-11 is the problem whose closure would close F5.

**Parallel structure within the SF series:** SF-3 §8 states this is "structurally parallel to SF-4's open neutrino δ_CP in the limited sense that both flagships derive masses while deferring a mixing-sector CP observable." Both are "masses derived, mixing-sector open."

**Lane assignment:** SM lane for theorem derivation; SF-2 is the primary vehicle (generation-transition structure is SF-2's domain). Cross-connection to SF-3 (quark masses) and SF-4 (neutrino sector, where a parallel PMNS open problem exists at OPEN-SM-5).

**Dependencies:** SF-2 v1.05 generation-transition structure (shipped); OPEN-SM-4 (Capotauro mechanism — δ_CP and Δp_LR = χ/6 are its magnitude anchors, per OPEN-SM-4 cross-sector note)
**Cross-sector connections:** OPEN-SM-4 (Capotauro), OPEN-SM-5 (PMNS — parallel structure), OPEN-FP-3-CKM (SF-3 §8 original registration), χ₄ F5 filter (chirality axiom maturation, EW lane)
**Paper(s):** SF-2 (primary vehicle); SF-3 §8 (original registration as OPEN-FP-3-CKM)
**Last updated:** 18 Sep 2026 (Patch 4096 — initial frontier registration)

---

### OPEN-SD-lattice-scale: CPP Lattice-to-SI Conversion Constant
**Status:** OPEN
**Sector(s):** SD, GLOBAL
**Priority:** #1 (foundational — blocks experimental scrutiny)
**One-line statement:** Determine 1 CPP lattice unit (circumradius) = ? fm.
**What a solution looks like:** 5 routes explored; 3 converge at l_unit ≈ 0.59 fm. Need definitive derivation.
**Dependencies:** None blocking
**Cross-sector connections:** All spatially resolved observables
**Current best lead:** Three independent routes converging at l_unit ≈ 0.59 fm.
**Paper(s):** New
**Last updated:** 10 April 2026

---

