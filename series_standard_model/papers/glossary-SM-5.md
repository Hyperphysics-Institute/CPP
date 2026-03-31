# Glossary — SM-5: Tribimaximal Neutrino Mixing from the K3 Cage Base Graph

**Paper:** SM-5_tribimaximal_neutrino_mixing_from_k3.tex (v1)
**Last updated:** 30 March 2026

Terms defined as they function in SM-5. SM-5 introduces the neutrino identification ansatz, the PMNS matrix derivation, the TBM result, and the open correction problems. Several terms (PMNS, TBM, mixing angles) are standard neutrino physics; those entries explain the standard definition and then clarify how they appear in the CPP context. Terms defined in earlier papers that appear here unchanged are cross-referenced.


## Section 1: The Neutrino Identification

**Neutrino mass eigenstate**
A neutrino state that propagates with definite frequency and definite mass. In standard neutrino physics, neutrino mass eigenstates (ν₁, ν₂, ν₃) are defined as the states that diagonalise the neutrino mass matrix. They are related to the flavour eigenstates (ν_e, ν_μ, ν_τ — the states produced in weak interactions with a definite charged lepton) by the PMNS matrix.

In SM-5, the three neutrino mass eigenstates are identified with the three eigenmodes of the K3 ZBW Hamiltonian (Ĥ_ZBW = ℏω₀ × A_{K₃} from SM-3). This identification is an ansatz, not a derivation. Its physical motivation: neutrinos carry no electric or colour charge, so they are not pinned to any specific K3 vertex. They propagate as global oscillation modes of the cage base — the eigenmodes of the Hamiltonian rather than specific vertex states. The formal derivation of why neutral, colourless particles occupy the eigenmode basis is OPEN-P-SM-nu-id.

**Neutrino flavour eigenstate**
A neutrino produced at a weak interaction vertex alongside a definite charged lepton: ν_e is produced with an electron, ν_μ with a muon, ν_τ with a tau. In SM-5, each flavour eigenstate is identified with the corresponding charged lepton's vertex state: ν_e ↔ |V₁⟩ (the electron's vertex), ν_μ ↔ |V₂⟩, ν_τ ↔ |V₃⟩. This identification follows from the SM-4 assignment of lepton generations to K3 vertices and does not require a separate ansatz.

**Neutrino identification ansatz**
The central assumption of SM-5: the three neutrino mass eigenstates are the three eigenmodes of the K3 ZBW Hamiltonian:
- ν₁ ↔ |φ₋^(1)⟩ = (2,−1,−1)/√6
- ν₂ ↔ |φ₊⟩ = (1,1,1)/√3
- ν₃ ↔ |φ₋^(2)⟩ = (0,−1,1)/√2

This is labelled an ansatz because it has not been derived from CPP postulates. It is motivated by the physical distinction between locally-coupled particles (charged leptons, which source SSV gradients at specific vertices and are therefore pinned to vertex states) and globally-coupled particles (neutrinos, which source no SSV and propagate as cage eigenmodes). The formal derivation is OPEN-P-SM-nu-id.

**Vertex basis vs eigenmode basis**
The two natural orthonormal bases of the K3 cage base. The vertex basis {|V₁⟩, |V₂⟩, |V₃⟩} is the basis of localised states — each state is concentrated at one vertex. The eigenmode basis {|φ₊⟩, |φ₋^(1)⟩, |φ₋^(2)⟩} is the basis of delocalised states — each state spreads over all three vertices. These two bases are not aligned. The matrix that converts between them is the TBM mixing matrix. The physical principle selecting which basis a particle uses is the locality of its coupling: charged leptons (localised SSV source) → vertex basis; neutrinos (no SSV source) → eigenmode basis.


## Section 2: The PMNS Matrix

**PMNS matrix (Pontecorvo-Maki-Nakagawa-Sakata matrix)**
The unitary 3×3 matrix that relates neutrino flavour eigenstates (ν_e, ν_μ, ν_τ) to neutrino mass eigenstates (ν₁, ν₂, ν₃):

(ν_e, ν_μ, ν_τ)^T = U_PMNS × (ν₁, ν₂, ν₃)^T

Its matrix elements U_{αi} are the mixing amplitudes: U_{αi} is the amplitude for lepton flavour α to produce neutrino mass eigenstate νᵢ. In SM-5, U_{αi} = ⟨V_α | φᵢ⟩ — the inner product of the charged lepton vertex state with the neutrino eigenmode. This is the change-of-basis matrix from the eigenmode basis to the vertex basis of K3.

**Zeroth-order PMNS matrix**
SM-5's result U_PMNS^(0) = U_TBM is explicitly a zeroth-order result — it holds in the limit where Capotauro corrections and charged-lepton diagonalisation corrections are zero. The observed PMNS matrix deviates from U_TBM at the 10–30% level in the angles, and at the 30σ level in sin²θ₁₃. These deviations are the second-order corrections registered as OPEN-P-SM-4 and OPEN-P-SM-5.

**CKM matrix (for comparison)**
The analogous mixing matrix in the quark sector. The CKM matrix is close to the identity — quark mixing is small (the largest angle is the Cabibbo angle, sin θ_C ≈ 0.22). The PMNS matrix has large mixing angles (sin²θ₁₂ ≈ 0.30, sin²θ₂₃ ≈ 0.57). The Standard Model does not explain why lepton mixing is large and quark mixing is small. CPP's explanation: quarks carry colour charge and are cage vertex-localised in the strong sector, producing small mixing; neutrinos carry no charge and use the eigenmode basis, producing large mixing. The quark mixing is small because the K3 vertex basis is nearly the mass eigenstate basis for quarks; the neutrino mixing is large because the K3 eigenmode basis is far from the vertex basis.


## Section 3: Tribimaximal Mixing

**Tribimaximal mixing (TBM)**
The specific PMNS mixing pattern with angles sin²θ₁₂ = 1/3, sin²θ₂₃ = 1/2, sin²θ₁₃ = 0. The name "tribimaximal" combines "trimaximally mixed" (the atmospheric angle θ₂₃ = 45° is maximally mixed for two flavours) and "bimaximal" (the solar angle gives equal tripartite mixing). TBM was proposed as an empirical pattern by Harrison, Perkins, and Scott (2002) and derived from the A₄ discrete symmetry group by Ma and collaborators.

TBM is excluded as an exact experimental result — the Daya Bay measurement of sin²θ₁₃ = 0.022 is incompatible with TBM's prediction of sin²θ₁₃ = 0 at more than 30 standard deviations. SM-5 treats TBM as the zeroth-order result, with corrections from the Capotauro mechanism and charged-lepton diagonalisation.

**TBM mixing matrix (U_TBM)**
The explicit 3×3 matrix:

U_TBM = |  √(2/3)    1/√3    0   |
         |  −1/√6     1/√3   −1/√2|
         |  −1/√6     1/√3   +1/√2|

This matrix is exactly the change-of-basis matrix from the K3 eigenmode basis to the K3 vertex basis — U_{αi} = ⟨V_α|φᵢ⟩. The specific numerical values (√(2/3), 1/√3, 1/√2, 1/√6) are all simple radicals arising from the normalisation of the K3 eigenvectors. No free parameters enter.

**Solar mixing angle (θ₁₂)**
The mixing angle governing ν_e ↔ ν₂ oscillations, measured in solar neutrino experiments. TBM value: sin²θ₁₂ = 1/3. Observed: sin²θ₁₂ = 0.304 ± 0.012. The TBM value exceeds the observed value by 2.4σ. The correction Δ(sin²θ₁₂) = −0.029 is attributed to charged-lepton mass matrix diagonalisation.

**Atmospheric mixing angle (θ₂₃)**
The mixing angle governing ν_μ ↔ ν₃ oscillations, measured in atmospheric neutrino experiments. TBM value: sin²θ₂₃ = 1/2. Observed: sin²θ₂₃ = 0.570 ± 0.024. The TBM value is lower than observed by 2.9σ. The correction Δ(sin²θ₂₃) = +0.070 is attributed to both charged-lepton diagonalisation and Capotauro bias.

**Reactor mixing angle (θ₁₃)**
The mixing angle governing ν_e ↔ ν₃ oscillations, measured in reactor neutrino experiments (Daya Bay, RENO, Double Chooz). TBM value: sin²θ₁₃ = 0 exactly. Observed: sin²θ₁₃ = 0.0220 ± 0.0006. The deviation of 30σ makes θ₁₃ the most significant correction to TBM. The CPP candidate: sin²θ₁₃ ≈ φ⁻²/1.6 (Capotauro mechanism, OPEN-P-SM-4). The coefficient 1/1.6 = 5/8 is not yet derived.

**CP-violating phase (δ_CP)**
The complex phase in the PMNS matrix that produces CP violation in neutrino oscillations. TBM has sin θ₁₃ = 0, so the Jarlskog invariant (which measures CP violation) is proportional to sin θ₁₃ and vanishes — δ_CP is undefined at zeroth order. The observed value is δ_CP ≈ 195° ± 25°. This is a next-order effect requiring the electroweak sector, connected to the Koide phase θ through OPEN-P-SM-7d (both are electroweak quantities that cannot be derived from K3+SSV alone).


## Section 4: The Correction Mechanisms

**Capotauro mechanism**
The proposed mechanism for generating corrections to TBM, particularly sin²θ₁₃ ≠ 0. Named after the chiral symmetry-breaking event in CPP cosmology (the "Capotauro" event) that distinguishes up-type from down-type quarks and imprints a chirality bias on the 600-cell lattice. The mechanism proposes a ZBW phase bias χ ∼ φ⁻¹ that mixes the ν_e–ν_τ sector, generating θ₁₃ ≠ 0.

The numerical motivation: sin²θ₁₃ ≈ φ⁻²/1.6 ≈ 0.022 (observed) with φ = 1.618 (golden ratio). The φ⁻² scaling suggests a connection to the 600-cell golden ratio geometry. The coefficient 1/1.6 = 5/8 is not yet derived from 600-cell first principles and is the primary target of OPEN-P-SM-4.

**Charged-lepton diagonalisation correction**
A correction to the PMNS matrix arising from the fact that the charged lepton mass matrix may not be perfectly diagonal in the K3 vertex basis at finite order. This is the standard mechanism in flavour physics for generating deviations from TBM: if the charged lepton mass matrix has off-diagonal contributions of order ε, the PMNS matrix receives corrections of order ε from the diagonalisation of that matrix. The corrections to θ₁₂ and θ₂₃ are attributed primarily to this mechanism (OPEN-P-SM-5).


## Section 5: Connections to Discrete Symmetry Models

**A₄ symmetry (for comparison)**
The alternating group on four elements (the rotation group of the tetrahedron), which has been used extensively in neutrino mass model building to derive TBM. Ma and Rajasekaran (2001) showed that A₄ symmetry with appropriate symmetry breaking predicts TBM. The K3 adjacency matrix A_{K₃} generates the regular representation of ℤ₃, a subgroup of A₄. The TBM matrix elements arise as the Clebsch-Gordan coefficients of this representation.

The CPP relationship to A₄: the relevant symmetry is C3 (the ℤ₃ rotation symmetry of the equilateral triangle), which is a subgroup of A₄. In A₄ models, A₄ is postulated as a flavour symmetry with no deeper explanation. In CPP, the C3 symmetry is derived from the 600-cell cage geometry (SM-1 Theorem 1). The physical grounding is the CPP contribution — not a new mathematical structure but a geometric explanation for why the structure exists.

**Discrete flavour symmetry (general)**
Any finite symmetry group imposed on the lepton mass matrix to constrain the mixing angles. Many groups (A₄, S₄, A₅, T′, Δ(27)) have been used in the literature. All have the character of external inputs — symmetries chosen to reproduce observed patterns. CPP's claim: the relevant symmetry (C3 of K3) is not an external input but a geometric consequence of the 600-cell lattice, derived rather than imposed.


## Section 6: Open Problems Specific to SM-5

**OPEN-P-SM-nu-id — Neutrino identification: why eigenmodes?**
Derive from CPP interaction rules why the neutrino mass eigenstates are diagonal in the K3 eigenmode basis while charged-lepton mass eigenstates are diagonal in the K3 vertex basis. This is the foundational open problem of the CPP neutrino sector. Its resolution likely requires the electroweak sector, because the distinction between localised (vertex) and delocalised (eigenmode) coupling is determined by how electroweak interactions couple to K3.

**OPEN-P-SM-5 — Corrections to TBM mixing angles**
Derive the corrections Δ(sin²θ₁₂) = −0.029, Δ(sin²θ₂₃) = +0.070, and sin²θ₁₃ = 0.022 from CPP mechanisms — primarily charged-lepton diagonalisation and the Capotauro bias. These corrections are of order sea_strength ≈ 0.178, consistent with being first-order corrections to the TBM result.

**OPEN-P-SM-4 — Capotauro mechanism for θ₁₃**
The reactor angle sin²θ₁₃ = 0.022 ≈ φ⁻²/1.6. Derive the Capotauro ZBW phase bias χ ∼ φ⁻¹ from 600-cell geometry, compute the resulting θ₁₃ correction, and determine whether the coefficient 5/8 = 1/1.6 is a geometric invariant of the 600-cell or a derived numerical value.

**Neutrino masses and mass splittings (SM-6, planned)**
The absolute neutrino masses and mass-squared splittings Δm²₂₁ and |Δm²₃₂| are not derived in SM-5. These require connecting the K3 eigenvalue structure to the σ = 120^{-3} geometric suppression from SM-1 §8. The identification of neutrino mass eigenstates with K3 eigenmodes gives the mixing matrix; the mass splittings require the additional input of how the eigenvalues +2 and −1 translate to physical masses through the suppression formula.
