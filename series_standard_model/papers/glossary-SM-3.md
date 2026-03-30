# Glossary — SM-3: The Koide Relation from the Colour Cage Base Graph

**Paper:** SM-3_k3_spectral_theorem_koide_formula.tex (v5)
**Last updated:** 30 March 2026

Terms defined as they function in SM-3 specifically. SM-3 is a precision proof paper — it uses mathematical objects precisely and the glossary entries reflect that precision. Several terms (K₃, spectrum, eigenvalue, Koide formula) are standard mathematics that SM-3 applies to CPP; those entries explain the standard definition and then clarify exactly what role they play in the CPP argument.


## Section 1: The K₃ Graph

**K₃ (the colour cage base graph)**
The complete graph on three vertices: three vertices V₁, V₂, V₃ with an edge connecting every pair. In the 600-cell lattice, K₃ is the equilateral base triangle of the tetrahedral cage — the three colour vertices from which the quarks' colour states get their identity (SM-1, SS-1) and around which the lepton's ZBW orbital hops. The adjacency matrix of K₃ is the 3×3 matrix with 0 on the diagonal and 1 everywhere else. The K₃ graph is the minimal symmetric graph that supports both the charge quantisation result δ = 1/3 (from its combinatorial symmetry, SM-1 Theorem 1) and the Koide result K = 2/3 (from its spectral structure, SM-3 Theorem). These two derivations are independent of each other.

**Adjacency matrix (A_{K₃})**
The matrix encoding K₃'s connectivity: entry (i,j) = 1 if vertices i and j are connected by an edge, 0 if not. For K₃ with three vertices, every off-diagonal entry is 1 and every diagonal entry is 0. In SM-3, this matrix is the ZBW Hamiltonian (up to the energy scale ℏω₀): Ĥ_ZBW = ℏω₀ × A_{K₃}. The fact that the Hamiltonian equals the adjacency matrix (scaled) is derived from C3 symmetry and SSV hopping, not assumed.

**C3 symmetry of K₃**
The rotational symmetry V₁ → V₂ → V₃ → V₁ that is an exact isometry of the equilateral triangle. C3 symmetry was already established in SM-1 (charge quantisation proof) as a consequence of the three base vertices being equidistant from the apex V₄ and from each other. In SM-3, C3 symmetry does additional work: it forces the ZBW hopping Hamiltonian to have equal off-diagonal elements (all three edges have the same hopping amplitude), which means Ĥ_ZBW must equal t × A_{K₃} for some energy t. C3 symmetry is the bridge from "equilateral triangle" to "adjacency matrix Hamiltonian."


## Section 2: Spectral Theory

**Adjacency spectrum**
The set of eigenvalues of the adjacency matrix. For K₃, the spectrum consists of two eigenvalues: λ_max = +2 (the bonding eigenvalue, multiplicity 1) and λ_min = −1 (the antibonding eigenvalue, multiplicity 2). The spectrum is a property of the graph's structure, not of the physical system that uses the graph. Knowing the spectrum of K₃ is knowing the allowed ZBW energy levels once P1 establishes that the Hamiltonian equals ℏω₀ × A_{K₃}.

**Bonding eigenvalue (λ_max = +2)**
The largest eigenvalue of A_{K₃}, with eigenvector (1,1,1)/√3. The bonding eigenstate has equal amplitude at all three cage vertices — the ZBW orbital is symmetrically distributed. The name "bonding" follows the analogy with molecular orbital theory: the symmetric (bonding) orbital lowers the total energy. In SM-3, the bonding sector corresponds to the baseline mass contribution that is common to all three lepton generations.

**Antibonding eigenvalue (λ_min = −1)**
The smaller eigenvalue of A_{K₃}, with multiplicity 2. Any vector orthogonal to (1,1,1) is an antibonding eigenvector. There are two linearly independent antibonding states because the two-dimensional subspace orthogonal to (1,1,1) in ℝ³ is two-dimensional. The two antibonding states have asymmetric amplitude distributions across the three vertices — the ZBW orbital is not uniformly distributed. In SM-3, the antibonding sector is what differentiates the three lepton generations from each other: each generation corresponds to a different phase relationship in the antibonding subspace.

**Eigenvalue ratio**
The ratio λ_max/|λ_min| = 2/1 = 2. This is the critical number in the proof. The ratio 2 is not chosen and not calibrated — it is a theorem of graph theory applied to the equilateral triangle. For K_N (the general complete graph on N vertices), the eigenvalue ratio is (N−1)/1 = N−1. For K₃ specifically, this ratio is 2. The entire proof that K = 2/3 hinges on this ratio being exactly 2.


## Section 3: The Three Propositions

**P1 — ZBW Hamiltonian**
The statement that the ZBW Hamiltonian of the lepton orbital is Ĥ_ZBW = ℏω₀ × A_{K₃}. This is derived from two independent CPP facts: (a) C3 symmetry forces equal hopping amplitudes on all three K₃ edges; (b) the SSV hopping energy at the confinement radius sets the amplitude to ℏω₀ = sea_strength × ℏc/r_conf ≈ 87.8 MeV. P1 is the physical identification of the cage base graph with the ZBW energy landscape. Without P1, the K₃ adjacency matrix is just a mathematical object with no physical connection to lepton masses. P1 is the bridge.

**P2 — ZBW Born Rule**
The statement that the mass contribution of lepton generation i is proportional to |ψᵢ|², the squared wavefunction amplitude at colour vertex Vᵢ. This is derived from the CPP DI-bit visit rate: the ZBW orbital spends a fraction |ψᵢ|² of its time at vertex Vᵢ, and mass = stored ZBW energy ∝ time spent at each vertex. P2 is the CPP account of the Born rule for mass — not for probability of detection but for mass distribution across the cage vertices. The relation mᵢ ∝ |ψᵢ|² has the same mathematical form as the quantum mechanical Born rule |ψ|² = probability density, applied to mass instead of probability.

**P3 — Thermal equipartition**
The statement that all three K₃ eigenstates are equally occupied: |cₙ|² = 1/3 for each eigenstate n = 1, 2, 3. This follows from the ZBW orbital coupling to the DP Sea at the Planck temperature, which is enormously larger than the ZBW energy scale (kT_P/ℏω₀ ≈ 10²⁰). In this limit, the Boltzmann distribution assigns equal weight to all eigenstates regardless of their energies — a high-temperature state counting. One bonding state and two antibonding states, each with equal weight 1/3, gives |c₊|² = 1/3 and |c₋|² = 2/3. P3 is state-counting equipartition, not energy equipartition.

The distinction between state-counting and energy equipartition is important: energy equipartition would give equal energy to each mode (E_n = kT/2 per quadratic mode), but the relevant quantity here is eigenstate occupation probability, not energy. State-counting equipartition assigns equal probability 1/N to each of the N eigenstates.

**Hopping amplitude (ℏω₀)**
The energy scale for a single ZBW hop between adjacent cage base vertices, given by ℏω₀ = sea_strength × ℏc/r_conf. With sea_strength ≈ 0.178 and r_conf ≈ 0.16 fm, ℏω₀ ≈ 87.8 MeV. This is a derived quantity (from SS-1 §8 and SM-1 §7), not a calibration constant of SM-3. It enters P1 as the energy scale of the ZBW Hamiltonian. The individual lepton masses are not equal to ℏω₀ — they are set by ρ (from P3), θ (open), and the scale A (calibrated in SM-4).


## Section 4: The Koide Formula

**Koide formula (empirical)**
The relation K = (m_e + m_μ + m_τ)/(√m_e + √m_μ + √m_τ)² = 2/3, first noted empirically by Yoshio Koide in 1982. It holds to 11 ppm using current PDG masses. No Standard Model explanation exists for why the three charged lepton masses should satisfy this relation. SM-3 derives it from the K₃ spectral structure.

The Koide formula is not dimensionally trivial — it involves a ratio of (mass)¹ to (mass)², so it is dimensionless and scale-invariant. It holds regardless of what units the masses are measured in. This scale invariance is a clue: the formula is constraining the relative values of the three masses, not their absolute scale. SM-3's proof confirms this interpretation: the K₃ spectral structure determines K = 2/3 independently of the mass scale A, which is calibrated separately in SM-4.

**K (Koide ratio)**
The dimensionless number K defined by the Koide formula. K = 2/3 for the three charged leptons to 11 ppm. SM-3 proves K = 2/3 exactly from the K₃ spectrum. The proof shows that K depends only on ρ through the algebraic identity K = (1 + ρ²/2)/3, and ρ is determined by the eigenvalue ratio of K₃ via P3.

**Koide parametrisation**
The standard way to write lepton masses satisfying the Koide formula: √mᵢ = A(1 + ρ cos φᵢ), where φᵢ = θ + 2πi/3 (i = 1,2,3 for electron, muon, tau). Here A is the overall mass scale, ρ is the modulation depth (how much the masses differ from each other), and θ is the Koide phase (which sets where electron is, vs muon, vs tau on the Koide circle). SM-3 proves ρ = √2 exactly. SM-4 calibrates A to the electron mass. The Koide phase θ = 132.73° is open (OPEN-P-SM-7d).

**Modulation depth (ρ)**
A dimensionless parameter measuring the spread of the three lepton masses around their geometric mean. ρ = 0 means all three leptons have equal mass (degenerate). ρ = √2 gives the observed lepton mass hierarchy. SM-3 derives ρ = √2 from the K₃ eigenvalue ratio: ρ² = |c₋|²/|c₊|² = 2 (from P3), so ρ = √2. The large spread of lepton masses — the tau is 3477× heavier than the electron — is encoded in ρ = √2 being the specific modulation depth corresponding to the K₃ eigenvalue ratio 2:1.

**Koide phase (θ)**
The angle in the Koide parametrisation that sets the position of each lepton on the Koide circle. θ = 132.73° places the electron as the lightest, the muon as intermediate, and the tau as the heaviest. SM-3's proof does not determine θ — C3 symmetry leaves the antibonding subspace degenerate, so any θ is compatible with K = 2/3. The derivation of θ requires the electroweak sector (OPEN-P-SM-7d). This is the primary open problem of the SM series.

**Koide circle**
A geometric representation of the Koide constraint: the three values √mᵢ lie on a circle of radius ρA centered on A, with C3-symmetric angular spacing. All mass triplets satisfying K = 2/3 with a given A and ρ lie on this circle. The Koide phase θ rotates the triplet around the circle — it determines which specific point on the circle corresponds to the electron, which to the muon, and which to the tau.


## Section 5: The ZBW Resonator

**ZBW resonator**
The physical system described by SM-3: the lepton's orbital ZBW DP hopping between the three K₃ vertices under the Hamiltonian Ĥ_ZBW = ℏω₀ × A_{K₃}. This is a finite quantum system with three states (the three cage vertices), three ZBW energy levels (the K₃ eigenvalues scaled by ℏω₀), and thermal coupling to the DP Sea. The ZBW resonator is not a separate physical object — it is the lepton's own ZBW orbital described in the K₃ basis. Calling it a "resonator" emphasises that it is a coherent oscillating system that can be in superpositions of its eigenstates, coupled to a thermal bath.

**Thermal bath coupling**
The Caldeira-Leggett system-bath coupling between the ZBW resonator and the DP Sea. Every CP exchanges DI-bits with the surrounding Sea at each Absolute Moment — this is the microscopic mechanism of the coupling. The coupling drives the ZBW resonator toward the thermal equilibrium state of the bath (the DP Sea at T ≈ T_Planck). The coupling is strong (relaxation time much shorter than the ZBW period), ensuring that P3's thermal equipartition is achieved within each ZBW cycle.

**High-temperature limit**
The regime kT_P/ℏω₀ ≈ 10²⁰ >> 1 that justifies P3. In this limit, the Boltzmann factor e^{−Eₙ/kT} ≈ 1 − Eₙ/kT ≈ 1 for all eigenstate energies Eₙ, so all eigenstates are equally occupied. The high-temperature limit is not an approximation in SM-3 — it is an excellent approximation because the ratio kT_P/ℏω₀ is so large. Departures from K = 2/3 would only appear for temperatures kT ≲ ℏω₀ ≈ 88 MeV, far above any temperature accessible to stable lepton systems.


## Section 6: Why Quarks Do Not Satisfy Koide

**Strong-sector mass contamination**
The reason the quark Koide ratios (K(d,s,b) = 0.731, K(u,c,t) = 0.849) differ from 2/3. Quarks carry qDP chain binding energy, inter-cage bonding energy, and cage-depth scaling — mass contributions that are absent for leptons. These contributions are not governed by the K₃ spectral structure; they break the C3 mass symmetry. The observed deviations of 10% and 27% are consistent with CPP's prediction that the Koide formula applies only to leptons.

The deviations are not random: they are positive (quarks have K > 2/3) and the up-type quarks deviate more than the down-type. This is consistent with the CPP picture that up-type quarks (bare +qCPs, no linear ZBW DP) have stronger cage-depth scaling than down-type quarks, producing larger deviations from the lepton spectral picture.

**Lepton purity**
The property of leptons that makes the Koide theorem apply to them and not to quarks. Leptons are eCPs with no colour charge and no qDP chain binding. Their masses are determined purely by the K₃ ZBW resonator — P1, P2, and P3 hold exactly for leptons. Quarks carry additional mass contributions that contaminate the K₃ spectral structure. The theorem is a lepton theorem precisely because leptons are spectrally pure in a sense that quarks are not.


## Section 7: Open Problems

**OPEN-P-SM-7d — Koide phase θ**
The derivation of θ = 132.73° from CPP dynamics. The K₃ spectral theorem proves K = 2/3 and ρ = √2, but leaves θ undetermined. Any value of θ is compatible with the K₃ spectrum — the C3 symmetry that forces K = 2/3 also makes the antibonding subspace degenerate (both antibonding states have the same eigenvalue −1), so nothing in the K₃ spectrum prefers one θ over another. A structural theorem (proved in SM-4 Theorem 2) shows that no mechanism within the K₃+SSV framework can break this degeneracy. The derivation of θ requires the electroweak sector.

**Open connection — the K₃ thermal picture and SM-2's VEV framework**
SM-3 derives the lepton mass scale from ℏω₀ = sea_strength × ℏc/r_conf ≈ 87.8 MeV. SM-2 calibrates the lepton masses using k ≈ 0.0185 applied to the Planck energy. These two energy scales should be consistent. The relationship between ℏω₀ (the ZBW hopping energy from SS-1 sea_strength) and the SM-2 VEV framework (the Planck energy suppressed by N⁴) is an open derivation. Establishing this connection would unify the two mass generation frameworks under a single geometric picture.
