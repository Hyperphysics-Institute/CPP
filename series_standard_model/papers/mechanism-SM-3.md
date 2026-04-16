# Mechanism — SM-3: The Koide Relation from the Colour Cage Base Graph

**Paper:** SM-3_k3_spectral_theorem_koide_formula.tex (v6)
**Last updated:** 16 April 2026

This file provides a sequential cause-and-effect account of why K = 2/3. Each step identifies the actor, the cause, and the consequence. The proof has a specific logical architecture: three propositions feed into a four-step algebraic argument that forces K = 2/3 exactly. P1 and P2 are derived from CPP axioms (Layer A); P3 is conditional on imported open-system thermalisation formalism (Layer B). The mechanism essay walks through both the derivation chain and the physical picture behind each step. For term definitions see glossary-SM-3.md; for the formal proofs see the paper itself.


## Part 1: The Setup — What the K3 Graph Is

The tetrahedral cage of the electron (and of all charged leptons) has a central CP surrounded by four compensating CPs at the tetrahedral vertices. Three of those four vertices — the base triangle V₁, V₂, V₃ — form an equilateral triangle. This triangle has three vertices, three edges connecting every pair of vertices, and perfect three-fold rotational symmetry (C3). In graph theory this structure is called K₃, the complete graph on three vertices.

The K₃ graph is the same object that SM-1 used for charge quantisation (δ = 1/3 from C3 symmetry and cage completeness). SM-3 uses the same triangle but a completely different property of it: not its combinatorial symmetry but its adjacency spectrum — the eigenvalues of the matrix that encodes the graph's connectivity. The same triangle encodes two independent physical results from two independent mathematical properties.


## Part 2: The Three Propositions

The theorem requires three propositions. P1 and P2 are derived from CPP axioms (Layer A). P3 is conditional on an imported thermalisation model (Layer B).

**Proposition AXIM-1 — The ZBW Hamiltonian equals the K₃ adjacency matrix scaled by ℏω₀.**

The ZBW orbital of the lepton hops between the three base vertices of the cage. The energy of each hop is set by the SSV interaction at the confinement radius. C3 symmetry forces all three hopping amplitudes to be equal (the three edges are geometrically identical). A Hamiltonian that is C3-symmetric and has equal hopping amplitudes on all three K₃ edges is exactly ℏω₀ × A_{K₃}, where A_{K₃} is the adjacency matrix of the triangle. The hopping energy ℏω₀ = sea_strength × ℏc/r_conf = 0.178 × 197.3/0.16 = 219.5 MeV follows from the SSV potential at the confinement radius. Note: the per-vertex DP binding energy E_eDP = ℏω₀/φ² ≈ 83.9 MeV (≈ 87.8 MeV to 4.5%) — these two quantities were mislabeled in SM-3 v5 eq:hop_amp, which wrote 87.8 MeV as ħω₀; the correct labeling is given here. The K = 2/3 theorem is unaffected: the thermal limit kT_P/ħω₀ ≈ 5.6 × 10¹⁹ >> 1 holds for either energy scale.

The derivation: C3 symmetry forces equal off-diagonal elements t₁₂ = t₂₃ = t₃₁ ≡ t. Setting the on-site energy to zero (energy origin choice) gives Ĥ_ZBW = t × A_{K₃}. The SSV hopping amplitude t = sea_strength × ℏc/r_conf identifies t = ℏω₀. AXIM-1 is derived, not postulated.

**Proposition AXIM-2 — Lepton mass is proportional to the squared ZBW wavefunction amplitude at each colour vertex.**

In CPP, mass is organisational energy stored in a stable cage configuration. For leptons, this energy is the ZBW kinetic energy of the orbital DP visiting each cage base vertex. The rate at which the ZBW orbital visits vertex Vᵢ is proportional to |ψᵢ|² — the squared wavefunction amplitude at that vertex. The mass contribution from vertex i is therefore proportional to |ψᵢ|². This is derived from the CPP DI-bit visit rate: the number of DI-bits processed at Vᵢ per Absolute Moment is proportional to the probability of the ZBW orbital being at Vᵢ, which is |ψᵢ|².

**Proposition AXIM-3 — The K₃ eigenstates are equally occupied (thermal equipartition) — Layer B.**

The ZBW orbital is coupled to the Dipole Sea thermal bath at temperature T ≈ T_Planck. The Planck temperature is enormously larger than the ZBW energy scale ℏω₀ ≈ 88 MeV — the ratio kT_P/ℏω₀ ≈ 10²⁰. In this high-temperature limit, the Boltzmann factors e^{−Eₙ/kT} become equal for all eigenstates (they all approach 1 as kT → ∞). Thermal equilibrium therefore distributes equal weight to each of the three K₃ eigenstates: |c_n|² = 1/3 for each eigenstate n = 1, 2, 3. This is state-counting equipartition (equal weight per eigenstate, not per energy level), following from the high-temperature Gibbs limit.

**Epistemic status (v6):** The statistical mechanics of the high-temperature limit is standard. What is imported (Layer B) is the chain from CPP's DI-bit exchange mechanism to the Gibbs state: (B1) Caldeira–Leggett system-bath coupling form, (B2) rapid thermalisation τ_relax ≪ τ_ZBW, and (B3) full canonical Gibbs equilibration rather than dephasing only. These are standard physical assumptions consistent with CPP but not yet derived from CPP primitives. Deriving them is the target of SS-4.

**Robustness (v6):** At finite temperature, the exact departure from equal occupation is |c₋|²/|c₊|² = 2e^{3x} where x = ℏω₀/kT_P ~ 10⁻²⁰. The correction to K = 2/3 is of order 10⁻²⁰ — algebraically tiny, nine orders of magnitude below the 11 ppm experimental precision.


## Part 3: The Eigenvalue Structure of K₃

The adjacency matrix of the equilateral triangle has exactly two distinct eigenvalues.

The bonding eigenvalue is λ_max = +2, with eigenvector (1,1,1)/√3. This state has equal amplitude at all three vertices — the ZBW orbital is symmetrically distributed across all three colour vertices simultaneously.

The antibonding eigenvalue is λ_min = −1, with multiplicity 2. Any vector perpendicular to (1,1,1) is an antibonding eigenvector. These states have unequal amplitudes at the three vertices — the ZBW orbital is asymmetrically distributed, constructively interfering at some vertices and destructively at others.

The eigenvalue ratio is λ_max/|λ_min| = 2/1. This specific ratio — 2 to 1 — is the number that drives the entire proof. It is not a free parameter; it is a theorem of linear algebra applied to the equilateral triangle graph.


## Part 4: The Four-Step Proof

**Step 1 — The lepton state is a superposition of bonding and antibonding modes.**

From AXIM-1, the lepton's ZBW wavefunction is a superposition of K₃ eigenstates: |ψ_g⟩ = c₊|φ₊⟩ + c₋|φ₋^(g)⟩, where g = 1, 2, 3 labels the three lepton generations (electron, muon, tau), and the C3 phase structure gives the three generation phases φᵢ = θ + 2πi/3.

**Step 2 — Thermal equipartition sets the amplitude ratio.**

From AXIM-3, the bonding and antibonding sectors receive equal weight per eigenstate. There is one bonding eigenstate and two antibonding eigenstates. Equal occupation per eigenstate gives: |c₊|² = 1/3 (one bonding state out of three) and |c₋|² = 2/3 (two antibonding states out of three).

**Step 3 — The amplitude ratio determines the modulation depth ρ.**

The Koide formula uses the parametrisation √mᵢ = A(1 + ρ cos φᵢ) with C3 phases φᵢ = θ + 2πi/3. The modulation depth ρ measures the asymmetry between bonding and antibonding contributions. From the amplitude ratio: ρ² = |c₋|²/|c₊|² = (2/3)/(1/3) = 2, therefore ρ = √2.

**Step 4 — The modulation depth forces K = 2/3.**

This is a pure algebraic identity that holds for any C3-symmetric mass triplet with modulation depth ρ: K = (1 + ρ²/2)/3. Substituting ρ = √2: K = (1 + 2/2)/3 = (1 + 1)/3 = 2/3. Exactly. No approximation, no calibration, no free parameters.

The chain is: K₃ graph → eigenvalue ratio 2:1 → AXIM-3 equipartition → |c₋|²/|c₊|² = 2 → ρ = √2 → K = 2/3.


## Part 5: Why This Is Specific to N=3

The argument above used only the eigenvalue structure of K₃. For the general complete graph K_N (N vertices, every vertex connected to every other), the eigenvalues are N−1 (once, bonding) and −1 (N−1 times, antibonding). The same equipartition argument gives |c₊|² = 1/N and |c₋|² = (N−1)/N. The modulation depth becomes ρ² = N−1, and the Koide-type formula gives:

K = (N+1)/(2N)

For N=1: K = 1. For N=2: K = 3/4. For N=3: K = 2/3. For N=4: K = 5/8. Only N=3 gives K = 2/3.

The three-colour structure of the lepton cage base — specifically, that the base triangle has exactly three vertices — is the precise reason the Koide ratio is 2/3 and not some other fraction. The fact that quarks and gluons exhibit SU(3) colour (three colours) and the fact that the lepton Koide ratio is 2/3 are both consequences of the same underlying object: the K₃ equilateral triangle cage base.


## Part 6: What the Theorem Does Not Prove

The theorem proves K = 2/3 exactly. It does not determine the individual lepton masses. To find m_e, m_μ, m_τ from the theorem, two additional inputs are needed: the scale A (calibrated to the electron mass in SM-4) and the Koide phase θ = 132.73° (which sets the relative positions of the three masses along the Koide circle). The phase θ is not determined by the K₃ spectral structure. The C3 symmetry that forces K = 2/3 also leaves the antibonding subspace degenerate — it cannot distinguish between different values of θ. The derivation of θ requires the electroweak sector and is registered as OPEN-P-SM-7d.

The theorem also does not apply to quarks. Quarks carry qDP chain binding energy, inter-cage bonding, and cage-depth scaling — strong-sector mass contributions that are absent for leptons. These contributions break the K₃ spectral symmetry that underlies the theorem. The observed deviations are K(d,s,b) = 0.731 (9.7% above 2/3) and K(u,c,t) = 0.849 (27% above 2/3), consistent with the CPP prediction that quarks should not satisfy the lepton Koide formula.


## Part 7: The Two K₃ Results from One Triangle

The same equilateral triangle K₃ produces two independent physical results:

The charge fraction δ = 1/3 from combinatorial symmetry: three equivalent vertices, each contributing 1/3 of the total screening.

The Koide ratio K = 2/3 from spectral structure: two antibonding eigenstates to one bonding eigenstate, giving |c₋|²/|c₊|² = 2, forcing ρ = √2 and K = 2/3.

These two derivations are logically independent — neither uses the other — yet they draw on properties of the same geometric object. The triangle's combinatorics produce δ = 1/3; the triangle's spectrum produces K = 2/3. Two distinct Standard Model results from two distinct mathematical properties of one equilateral triangle. This is the strongest single piece of consilience evidence in the SM series.


## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|---------------|
| K₃ graph definition | §2, Definition (colour cage base graph) |
| Eigenvalue spectrum | §2, Lemma (K₃ adjacency spectrum) |
| Uniqueness of N=3 | §2, Remark (K=2/3 unique to N=3) |
| Layer A/B/C decomposition | §3, Epistemic Layer Structure |
| Layer B assumptions (B1–B3) | §3.2, Remark (Status of Layer B) |
| AXIM-1 derivation (Layer A) | §4, Proposition (C3 symmetry forces Ĥ = ℏω₀ A_{K₃}) |
| AXIM-2 derivation (Layer A) | §4, Proposition (DI-bit flow rate gives mᵢ ∝ |ψᵢ|²) |
| AXIM-3 derivation (Layer B) | §4, Proposition (DP Sea thermalisation gives |cₙ|² = 1/3) |
| Robustness calculation | §4, Remark (Finite-temperature robustness) |
| Main theorem proof | §5, Theorem (K3 spectral origin of Koide formula) |
| Physical driver statement | §5, Remark (Physical driver) |
| Two K₃ results | §5, Corollary (common K₃ origin of δ=1/3 and K=2/3) |
| Quarks do not satisfy Koide | §6, Remark |
| Scope and open problems | §7, Scope table, Open Problem OPEN-P-SM-7d |
