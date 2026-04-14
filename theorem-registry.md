# CPP Theorem Registry — What We've Proved

**Location:** `/CPP/theorem-registry.md`
**Purpose:** Complete record of every theorem and corollary proved from CPP axioms, organised by series, with proof references and axiom dependencies.
**Companion file:** `axiom-registry.md` — what we assume.
**Architecture:** See `templates/Research_Frontier_Architecture.md`
**Last updated:** 12 April 2026

---

## Purpose

The axiom-registry tracks what CPP *assumes*. This file tracks what CPP has *proved*. Together they define the deductive structure of the theory. The primary health metric is the ratio:

**Theorems : Axioms = 37 : 6 ≈ 6.2 theorems per axiom**

*(Counting theorems + corollaries. Axiom count uses the 6-axiom set from postulates_and_theorems.md.)*

---

## Axiom Cross-Reference Key

Theorems reference axioms from two numbering systems (to be unified in a future session):

| `postulates_and_theorems.md` | `axiom-registry.md` | Content |
|---|---|---|
| AXIM-1 | A1 | CP existence |
| AXIM-2 | A2 | 600-cell topology |
| AXIM-3 | A3 (approx.) | Dipole Sea / DI-bit propagation |
| AXIM-4 | A4 (approx.) | SSV interaction / Nexus |
| AXIM-5 | — | Mass as organisational energy |
| AXIM-6 | — | Absolute Moment |
| — | A5 | Propagation efficiency η = 1/φ |
| — | A6' | Walk-Dimension Gauge Principle |

---

# Strong Sector (SS) — 9 Theorems

Source: SS-1 (Strong Sector unified paper).

| ID | Name | Result | Axioms Used | Paper Reference |
|----|------|--------|-------------|-----------------|
| **THEO-SS-1** | SU(3) from tetrahedral hopping | The three colour-charge hopping operators on the K₃ base graph generate the su(3) Lie algebra exactly. T^a = λ^a/2 (Gell-Mann matrices) reproduced to machine precision. | AXIM-1, AXIM-2, AXIM-4 | SS-1, Theorem 1 |
| **THEO-SS-2** | Gluon masslessness | Open hDP chain paths have f_geom = 0; gluons are massless. Same topological argument as photon masslessness. | AXIM-2, AXIM-3, AXIM-4 | SS-1, Theorem 2 |
| **THEO-SS-3** | β₀ = 7 | One-loop QCD β-function coefficient: β₀ = 11C_A/3 − 4T_F n_f/3 = 11−4 = 7. From C_A = 3, T_F = 1/2 (both exact), n_f = 6 (cage architecture). | AXIM-1, AXIM-2, AXIM-4 | SS-1, Theorem 3 |
| **THEO-SS-4** | α_geom exact | α_geom = 3(11+5√5)√(5+√5)/320 ≈ 0.5594. Pure 600-cell Voronoi invariant, closed form. Same constant appears in SR coupling and EM stiffness. | AXIM-2 | SS-1, Theorem 4 |
| **THEO-SS-5** | k_SM derived | k_SM = α_geom/(12φ²) ≈ 0.01781. Per-vertex dimensionless coupling from Voronoi stiffness. | AXIM-2 | SS-1, Theorem 5 |
| **THEO-SS-6** | sea_strength derived | sea_strength = (N_lattice/z) × k_SM = 10 × k_SM ≈ 0.1780. Factor 10 = 120/12, exact geometric integer. | AXIM-2 | SS-1, Theorem 6 |
| **THEO-SS-7** | GMO mass formula | Gell-Mann–Okubo baryon mass relation from SU(3) Casimirs. Octet relation holds to 0.6%. | AXIM-1, AXIM-2, AXIM-4 | SS-1, Theorem 7 |
| **THEO-SS-8** | Decuplet equal spacing | Equal mass spacing in baryon decuplet. Ω⁻ prediction: 1681 MeV vs PDG 1672.5 MeV (0.5%). | AXIM-1, AXIM-2 | SS-1, Theorem 8 |
| **THEO-SS-9** | Quark mass strict ordering | m_u < m_d < m_s < m_c < m_b < m_t from cage depth: each shell adds positive binding energy. Direction m_u < m_d from SSV polarity asymmetry. | AXIM-1, AXIM-2, AXIM-5 | SS-1, Theorem 9 |

---

# Standard Model Emergence (SM) — 9 Theorems

Sources: SM-1 through SM-9.

| ID | Name | Result | Axioms Used | Paper Reference |
|----|------|--------|-------------|-----------------|
| **THEO-SM-1** | Charge quantisation | δ = 1/3 exactly. From C₃ symmetry (δ₁ = δ₂ = δ₃) + cage completeness (δ₁+δ₂+δ₃ = 1). Topological, not integral. | AXIM-1, AXIM-2, AXIM-4 | SM-1, Theorem 1 |
| **THEO-SM-2** | Koide ratio K = 2/3 | From K₃ spectral theorem: eigenvalue ratio λ₊/|λ₋| = 2/1 → ρ = √2 → K = 2/3. Algebraically exact. | AXIM-1, AXIM-2, CORL-1a, AXIM-5 | SM-3, central theorem |
| **THEO-SM-3** | K₃ postulates derived | All three K₃ spectral theorem postulates derived from AXIM-1–AXIM-6. Zero free postulates remain in SM-3. | AXIM-1–AXIM-6 | SM-3, v5 |
| **THEO-SM-4** | TBM neutrino mixing | U_PMNS⁽⁰⁾ = U_TBM exactly. sin²θ₁₂ = 1/3, sin²θ₂₃ = 1/2, sin²θ₁₃ = 0 (zeroth order; corrections open). | AXIM-1, AXIM-2, CORL-1a | SM-5 |
| **THEO-SM-5** | θ cannot come from K₃+SSV | Structural impossibility: any C₃-preserving mechanism (3D or 4D) cannot select the Koide phase θ. V₄ is dark to antibonding modes. 11 candidates falsified. | AXIM-1, AXIM-2, AXIM-4 | Sessions B–K; OPEN-SM-7d |
| **THEO-SM8-1** | Bonded shells | Exactly four bonded polyhedral distance shells in the 600-cell: tetrahedron (V=4), icosahedron (V=12), dodecahedron (V=20), icosidodecahedron (V=30). Shell 3 (V=12) has zero edges. | AXIM-2 | SM-8 v4.1, Theorem 3.1 |
| **THEO-SM8-2** | Zero-parameter quark mass | M_q = m_e(z/φ)V^(7/3) × [1 or 16] predicts four heavy quark masses to RMS 2.1%, zero free parameters. | AXIM-2, A8' | SM-8 v4.1, Theorem 6.1 |
| **THEO-SM8-3** | Three generations | Tessellated 600-cell supports exactly four cage types → three quark generations. Outer shells identified with neighbouring cells' inner shells. | AXIM-2 | SM-8 v4.1, Theorem 8.1 |
| **THEO-SM9-1** | Symmetry degeneracy | For vertex-transitive polyhedra on S², Σ_{i<j} sin²(θ_ij/2) = V²/4 exactly. Angular pair sums carry no information beyond vertex count. | AXIM-2 | SM-9 v2.2, Theorem 3.1 |

---

# Electroweak Series (EW) — 8 Theorems

Sources: EW-1 through EW-5.

| ID | Name | Result | Axioms Used | Paper Reference |
|----|------|--------|-------------|-----------------|
| **THEO-EW-1** | W boson subgraph | W⁰ bracelet (6 hDPs, 12 CPs) on λ={1+φ, φ−1} subgraph. Open interior makes it reactive. | AXIM-1, AXIM-2 | EW-1, EW-2 |
| **THEO-EW-2** | Z boson subgraph | Z⁰ icosahedral loop (12 vertices) on λ=12 ground state. Maximally symmetric, inert. | AXIM-1, AXIM-2 | EW-1, EW-3 |
| **THEO-EW-3** | Higgs-like subgraph | Dodecahedral shell (20 vertices) on λ=−(1+φ). Most frustrated, highest confinement, scalar from A₅. | AXIM-1, AXIM-2 | EW-1, EW-4 |
| **THEO-EW-4** | Weinberg angle structure | Four-layer phase interference weights p_k = (1−k/5)² derived from 600-cell dihedral projections. sin²θ_W = 0.2312 (PDG 0.23121, 0.004%). Note: g' requires one calibration (vertex_count_correction = 1.18). | AXIM-2, AXIM-4 | EW-1, EW-5 |
| **THEO-EW-5** | No boson between Z and H | No regular polyhedral closed subgraph with 12 < vertices < 20 exists in the 600-cell. No stable boson between 91 and 125 GeV. | AXIM-2 | EW-1, EW-4 |
| **THEO-EW-6** | SU(2)_L algebra | [I^a, I^b] = iε^{abc} I^c from 120°/240° phase bias operators. Binary icosahedral group Γ closes the algebra. | AXIM-2, AXIM-4 | EW-5 |
| **THEO-EW-7** | Nexus gauge invariance | Local phase transformations ψ→e^{iα(x)}ψ leave all observables invariant. Discrete Ward identity from Nexus DI-bit conservation. | AXIM-1, AXIM-6 | EW-5 |
| **THEO-EW-8** | Yang-Mills EFT limit | CPP bit-exchange → Yang-Mills ℒ_eff = −(1/4)F^a_{μν}F^{aμν} + ... as l_P/L → 0. Convergence O(l_P/L). | AXIM-2, AXIM-4, AXIM-6 | EW-5 |

---

# Quantum Mechanics (QM) — 10 Theorems

Sources: QM-1 through QM-5. Registered 31 March 2026.

| ID | Name | Result | Axioms Used | Paper Reference |
|----|------|--------|-------------|-----------------|
| **THEO-QM-1** | Schrödinger equation | Continuum limit of discrete complex hopping on 600-cell → iℏ ∂ψ/∂t = −(ℏ²/2m)∇²ψ + Vψ exactly. Factor 2 from z/(2d) = 12/6 absorbed. **Solves OP-QM-2.** | AXIM-2, AXIM-4, AXIM-6 | QM-1, Theorem 1 |
| **THEO-QM-2** | Born rule | P(d) = |ψ(d)|² from identification of |ψ|² with local DI-bit number density ρ_bit. Non-circular. | AXIM-1, AXIM-3, AXIM-6 | QM-2 (via companion C3) |
| **THEO-QM-3** | Non-separability of singlet | |Ψ⁻⟩ cannot be written as |φ_A⟩ ⊗ |φ_B⟩. Separability contradicts Nexus total-spin-zero constraint. | AXIM-1, AXIM-6 | QM-3, Theorem 1 |
| **THEO-QM-4** | Tsirelson bound | |S|_CHSH = 2√2 at optimal angles. From E(â,b̂) = −cos θ applied to non-separable singlet. Matches QM exactly. | AXIM-1, AXIM-6, THEO-QM-3 | QM-3, Theorem 2 |
| **THEO-QM-5** | No-signaling | P(A=+1) = 1/2 regardless of Bob's axis. The Nexus is a global constraint, not a signal. | AXIM-6, THEO-QM-3 | QM-3, Theorem 3 |
| **THEO-QM-6** | Lindblad from DP Sea | dρ/dt = −(i/ℏ)[H_S,ρ] + γ(σ̂_zρσ̂_z − ρ) with γ = (sea_strength)² × E_P/ℏ. **Effectively solves OP-QM-4.** | AXIM-3, AXIM-4, AXIM-6 | QM-4, Theorem 1 |
| **THEO-QM-7** | Pointer basis = SSV eigenstates | Robust states are σ̂_z eigenstates (definite SSV phase projection). 12-edge broadcast selects dominant SSV. Stronger than standard einselection. | AXIM-2, AXIM-4 | QM-4, Theorem 2 |
| **THEO-QM-8** | Global unitarity | System + DP Sea + Nexus evolves unitarily at every Absolute Moment. Apparent collapse from tracing over bath. | AXIM-6 | QM-4, Theorem 3 |
| **THEO-QM-9** | Bosonic commutation | [aₖ, aₖ'†] = δₖₖ' from eigenmode orthonormality on 600-cell adjacency matrix. | AXIM-2 | QM-5, Theorem 1 |
| **THEO-QM-10** | Fermion-boson distinction | Charged CP aggregates: Pauli exclusion (one per GP from THEO-1) → fermionic. Neutral DI-bit modes: no restriction → bosonic. Spin-statistics is geometric. | AXIM-1, AXIM-2, THEO-1 | QM-5, Theorem 2 |

---

# Partner-Switching Mechanics — 1 Theorem

Source: CPP propositions session, 30 March 2026.

| ID | Name | Result | Axioms Used | Source |
|----|------|--------|-------------|--------|
| **THEO-1** | CP Non-Persistent Co-Occupation | Two CPs cannot persistently occupy the same Grid Point. Same-polarity: repulsive SSV prevents approach. Opposite-polarity: superimposition lasts exactly one Absolute Moment (bulk SSV drives separation). **CP Exclusion Postulate is redundant — it's a theorem.** Axiom count reduced from 7 to 6. | AXIM-1, AXIM-2, AXIM-4 | propositions.md §1 |

---

# Corollaries — 10 Total

## Standard Model Corollaries

| ID | Corollary | Follows From | Paper |
|----|-----------|-------------|-------|
| **CORL-SM-1** | q_up = +2/3 e, q_down = −1/3 e | THEO-SM-1 (δ = 1/3) | SM-1 |
| **CORL-SM-2** | Three lepton generations = three K₃ eigenmodes | THEO-SM-2 + K₃ structure | SM-3 |
| **CORL-SM-3** | Neutrinos = K₃ eigenmode excitations; charged leptons = vertex excitations | THEO-SM-4 | SM-5 |
| **CORL-SM-4** | K(c,b,t) ≈ 2/3 (0.42%) — K₃ thermal structure shows through for heavy quarks | THEO-SM-2 + cage perturbation theory | PS-1 |

## Quantum Mechanics Corollaries

| ID | Corollary | Follows From | Paper |
|----|-----------|-------------|-------|
| **CORL-QM-1** | Madelung decomposition automatic | THEO-QM-1 → continuity + quantum Hamilton-Jacobi with Q = −ℏ²∇²√ρ/(2m√ρ) | QM-1 |
| **CORL-QM-2** | Quantum pressure not postulated | THEO-QM-1 → Q emerges from complex hopping curvature | QM-1 |
| **CORL-QM-3** | CPP is superdeterministic at foundation but reproduces QM at leading order | THEO-QM-3,4,5 + SD series → SD corrections O(ε) ~ 10⁻²⁶ | QM-3 + SD-1 |

## Partner-Switching Corollaries

| ID | Corollary | Follows From | Source |
|----|-----------|-------------|--------|
| **CORL-1a** | ZBW Turning Point at Superimposition | THEO-1 → f_ZBW ≈ 1/(2t_P) derived, not postulated. AXIM-5/ZBW demoted. | propositions.md |
| **CORL-1b** | Stochastic Partner Exchange | THEO-1 + CORL-1a → DP pair identities are transient; the Sea is a gas of renewed partnerships | propositions.md |
| **CORL-SM-4** | *(listed above)* | | |

---

# Summary Statistics

| Series | Theorems | Corollaries | Total |
|--------|----------|-------------|-------|
| SS (Strong) | 9 | 0 | 9 |
| SM (Standard Model) | 9 | 4 | 13 |
| EW (Electroweak) | 8 | 0 | 8 |
| QM (Quantum Mechanics) | 10 | 3 | 13 |
| Partner-switching | 1 | 2 | 3 |
| **Total** | **37** | **9** | **46** |

---

# Axiom Usage Frequency

How many theorems depend on each axiom:

| Axiom | Theorem Count | Notes |
|-------|--------------|-------|
| AXIM-1 (CP existence) | 20 | Most foundational |
| AXIM-2 (600-cell) | 31 | Used in nearly everything |
| AXIM-3 (Dipole Sea) | 4 | Primarily QM series |
| AXIM-4 (SSV interaction) | 16 | Force law and its consequences |
| AXIM-5 (mass) | 3 | SS-9, SM-2, SM-3 |
| AXIM-6 (Absolute Moment) | 11 | QM series + EW-7,8 |

*(Counts are approximate; some theorems use axioms indirectly via other theorems.)*

---

# Open Problems That Remain After These Theorems

| Proved | Opens / Leaves Open |
|--------|---------------------|
| THEO-SM-1 (δ = 1/3) | Charge quantisation settled; lepton charges follow |
| THEO-SM-2 (K = 2/3) | K proved; θ_Koide remains open (OPEN-SM-7d) |
| THEO-SM-4 (TBM) | Zeroth order; corrections need Capotauro (OPEN-SM-4) |
| THEO-SM8-2 (quark mass) | Heavy quarks at 2.1%; light quarks and full formula open (OPEN-SS-1) |
| THEO-SS-3 (β₀ = 7) | One-loop; two-loop open (OPEN-SS-4) |
| THEO-QM-1 (Schrödinger) | OP-QM-2 **SOLVED** |
| THEO-QM-2 (Born rule) | Stated; rigorous ZBW phase derivation still open (OPEN-QM-1) |
| THEO-QM-6 (Lindblad) | OP-QM-4 **effectively SOLVED** |

---

*This file was extracted from `postulates_and_theorems.md` during Phase 2 of the Research Frontier Architecture implementation (12 April 2026). The source file retains axioms, conjectures, falsified items, and propositions; those items are now tracked in `axiom-registry.md`, `Research_Frontier.md`, and `propositions.md` respectively.*

*After Phase 5 verification, `postulates_and_theorems.md` will be archived.*
