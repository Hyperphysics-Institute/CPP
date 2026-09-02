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
**What a solution looks like:** Symmetry breaking [600-cell] × ℤ₂ → [600-cell]; derive χ = φ⁻³; reproduce δ_CP ≈ 195°, sin²θ₁₃ ≈ 0.022, and baryon asymmetry.
**Dependencies:** None blocking (but requires EW development)
**Cross-sector connections:** OPEN-SM-5 (PMNS), matter-antimatter asymmetry, cosmology; **CHIR ↔ electroweak bridge (Patch 0662): OPEN-SM-4 is the SM/SR co-owner of OPEN-CHIR-3 ∪ 1d-β-v** — the Capotauro chirality-activation event ([600-cell] × ℤ₂ → [600-cell]) is conjectured to be the substrate chiral-vacuum transition STATUS-2 derived (H₄ → H₄⁺, the same index-2 ℤ₂; the "ℤ₂-match" lead) and thereby EWSB (**CONJ-CHIR-1**); FI-C-9 = the P-face (EW parity violation), the T-arrow `sign(δ)` = the T-face (δ_CP), CPT-unified (TARROW-1). δ_CP and Δp_LR = χ/6 = φ⁻³/6 are the magnitude anchors. Scope sketch: `series_umbrella/series_substrate_chirality_arc/chirality_derivations/sketches/chir_ew_bridge_scoping.md`.
**Current best lead:** **Sub-claim (c) v1.0 SHIPPED via Capotauro paper v1.0 Session 122 Patch 0415** (paper at `series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex` v1.0; theorem-registry registration Session 103 Patch 0397 as THEO-CAP-1; first programme-level theorem registered ahead of its own flagship paper publication in the CPP corpus): Composite Capotauro Wigner-Eckart Theorem $|M| = |\langle\Phi_-^{(1)}|\hat{C}_\chi|\Phi_-^{(2)}\rangle| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ on K3-doublet, derived as chirality-eigenvalue matching factor $\chi$ (Session 96, $b = \chi/\sqrt{3}$ from spectral radius of unique $A_2$ generator $S$) times cage-shell averaging factor $1/6$ (Session 97, $d_E/V_\text{cage} = 2/12$). **Primary empirical prediction $\Delta p_{LR} = \chi/6 \approx 0.0394$ validated within 2%** of observed $\sim 0.04$. Conditional theorem closure on FI-C-1 through FI-C-10 + 4 CPP axioms (A1, A3, A4, A7). FI-C-9 substrate primitive chirality magnitude $|\chi| = \phi^{-3}$ registered Session 87 Patch 0381 as foundational input (reframed Session 120 Patch 0413 from "substrate-vacuum broken-symmetry order parameter" to "primitive substrate feature" per CPP core methodological principle that mathematical descriptions are not physical mechanisms — see v0.9 §2 reframe); FI-C-10 cage-shell extension to chirality observables registered Session 97 Patch 0391 as new foundational input. 34 findings registered (C-W1 through C-W34) across 16-session closure trajectory (Sessions 87-102). **Sub-claim (b) candidate mechanism**: Reading C geometric-chirality candidate (a primitive 4D direction $\hat{n}$ in the substrate's ambient 4D space producing direction-correlated edge-length variation at the $\phi^{-3}$ scale) registered Session 121 Patch 0414 with working sketch `series_umbrella/series_substrate_chirality_arc/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md` (296 lines); structural argument that $|\chi| = \phi^{-3}$ is the first viable perturbative-distance-ratio scale forced by the substrate-structure-preservation constraint; H₄ → I₄ algebraic reduction reinterpreted as structural consequence of $\hat{n}$ being primitive rather than dynamical outcome of SSB. Tracked at FP-section as **OPEN-FI-C-9-FP-MECHANISM**. **Sub-claim (a)** Capotauro nucleation event (universe-wide sign-selection event downstream of sub-claim (b) magnitude mechanism) remains open. *(Advisory, NON-BINDING speculation — not a claim, moves no verdict, not reviewed: a founder's-vision discussion of the sign-selection EPOCH — early causal-contact/inflationary imprint vs late precipitation vs R/L domains — mapping the domain-wall constraint (Zel'dovich–Kobzarev–Okun), the matter–antimatter domain-cosmology exclusion (Cohen–De Rújula–Glashow), the inflation + EU-1 contact-era reconciliation, and the live (contested) observational handles (galaxy 4PCF parity tests, CMB birefringence) is recorded at `founders_vision/physical_metaphysical_speculation/2026-06-09_chirality_primitive_QGE_and_imprint_epoch.md`. Advisory only; do NOT lift into the frontier without independent derivation + review.)* **Q11 sin²θ₁₃ derivation from $|M| = \chi/6$ re-scoped to SF-2 v2.0+ work** (Session 101 Patch 0395): standard PMNS perturbation predicts quadratic scaling $\propto |M|^2 \approx 0.001$ (off by factor 21); candidate γ structural observation $\sin^2\theta_{13} = b \cdot m_\perp \approx 0.0227$ matches observation within 1σ but lacks rigorous derivation; wavefunction-level coupling hypothesis ruled out Session 101. Earlier (pre-Session 87): δ_CP ≈ 195° matches NuFIT; mechanism physically motivated but not formalised.
**Paper(s):** **`series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex` v1.0 SHIPPED Session 122 Patch 0415** (46 pages, 601 KB PDF at v0.9; v1.0 SHIP is version-bump only with no content change; cross-reviewer convergence on SHIP-readiness across ChatGPT round-3 + CoPilot round-1 + Grok round-1 at v0.8 Session 119 Patch 0412; v0.9 polish Patch 0413 incorporated 8 ADDRESS items + 2 DISCOVERABILITY items + foundational framing reframe of §2 from SSB to primitive-feature framing); working sketches `series_umbrella/series_substrate_chirality_arc/capotauro/sketches/Capotauro_subclaim_c_wigner_eckart.md` §18 (Theorem 18.1) + §22 (v1.0 closure summary); parent sketch `Capotauro_chi_phi_closure.md` §1.3 (FI-C-9, FI-C-10) + §1.8 (Sessions 87-102 closure trajectory); mechanism candidate sketch `Capotauro_chiral_mechanism_candidate.md` (Session 121 Patch 0414 — Reading C development for sub-claim (b)); SM Paper 2 Appendix H (legacy reference).
**Last updated:** 16 May 2026 (Session 122 Patch 0415 — **Capotauro paper v1.0 SHIPPED**: sub-claim (c) v1.0 closure shipped via flagship paper at `series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex`; status preserved as PARTIAL CLOSURE since sub-claims (a) and (b) remain open; sub-claim (b) candidate mechanism Reading C registered as OPEN-FI-C-9-FP-MECHANISM in FP section).

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

