# Mechanism — SM-5: Tribimaximal Neutrino Mixing from the K3 Cage Base Graph

**Paper:** SM-5_tribimaximal_neutrino_mixing_from_k3.tex (v1)
**Last updated:** 30 March 2026

SM-5 is the most structurally transparent paper in the series. The central result — U_PMNS^(0) = U_TBM exactly — follows from a single identification and a one-line calculation. The mechanism essay is therefore shorter than SM-3's, because the computation is simpler. The depth is elsewhere: in understanding why the two natural bases of K3 are misaligned, and what that misalignment means physically.


## Part 1: What SM-5 Builds On

SM-5 is the direct continuation of SM-3 and SM-4. Three results are inherited without re-derivation:

The K3 cage base is the equilateral triangle {V₁, V₂, V₃} with exact C3 symmetry (SM-1 Theorem 1). The ZBW Hamiltonian on this base is Ĥ_ZBW = ℏω₀ × A_{K₃} (SM-3 Proposition P1). The eigenstates of this Hamiltonian are the bonding mode φ₊ = (1,1,1)/√3 (eigenvalue +2) and two antibonding modes φ₋^(1) = (2,−1,−1)/√6 and φ₋^(2) = (0,−1,1)/√2 (eigenvalue −1, multiplicity 2).

From SM-4: the three charged lepton mass eigenstates (electron, muon, tau) correspond to the three vertex states of K3: |V₁⟩ = electron, |V₂⟩ = muon, |V₃⟩ = tau. In the vertex basis, the charged lepton mass matrix is diagonal — lepton generation identity is a vertex identity.

These two inherited facts set up a natural question: what is the natural basis for neutrino mass eigenstates?


## Part 2: The Two Natural Bases of K3

The K3 equilateral triangle has two natural orthonormal bases, both completely determined by the geometry.

The first is the vertex basis: {|V₁⟩, |V₂⟩, |V₃⟩}. Each basis state is localised at one vertex. This is the basis in which charged leptons are diagonal (SM-4). A charged lepton in a definite generation state is localised at a definite vertex.

The second is the eigenmode basis: {|φ₊⟩, |φ₋^(1)⟩, |φ₋^(2)⟩}. Each basis state is delocalised over all three vertices — each eigenvector has support at all three vertices simultaneously. This is the basis in which the K3 Hamiltonian is diagonal. A particle in a definite eigenmode state has a definite ZBW energy.

These two bases are not aligned. They cannot be aligned while maintaining C3 symmetry: the vertex states transform into each other under C3 rotation, while the eigenstates are invariant (the bonding mode) or transform in a specific two-dimensional representation (the antibonding modes). The mismatch between these two bases is precisely what the change-of-basis matrix — the PMNS matrix — measures.


## Part 3: The Neutrino Identification

The central step of SM-5 is an identification, explicitly labelled as an ansatz:

The three neutrino mass eigenstates (ν₁, ν₂, ν₃) are identified with the three K3 eigenmodes:
- ν₁ ↔ |φ₋^(1)⟩ = (2,−1,−1)/√6
- ν₂ ↔ |φ₊⟩ = (1,1,1)/√3
- ν₃ ↔ |φ₋^(2)⟩ = (0,−1,1)/√2

The physical motivation: charged leptons carry electric charge and couple locally to the cage through the SSV gradient at a specific vertex — their mass eigenstates are localised (vertex states). Neutrinos carry neither electric charge nor colour charge. A particle with no localised SSV source is not pinned to any cage vertex; it propagates as a global oscillation mode of the cage structure, coupling to all three vertices simultaneously. The natural mass eigenstates for such a particle are the eigenmodes of the cage Hamiltonian — the modes that propagate with definite frequency.

This physical motivation is compelling but not yet a derivation from CPP axioms. The formal derivation of why neutral, colourless particles use the eigenmode basis requires establishing the CPP interaction rules for such particles, which involves the electroweak sector (OPEN-P-SM-nu-id). The identification is therefore an ansatz: natural, physically motivated, but not yet proved.

The conditional theorem that follows from this ansatz is rigorous and exact.


## Part 4: The PMNS Matrix as a Change of Basis

Given the identification in Part 3, the PMNS mixing matrix U follows immediately from the definition of mixing. The matrix element U_{αi} is the amplitude for a charged lepton of flavour α (produced at a vertex) to oscillate into neutrino mass eigenstate νᵢ (an eigenmode):

U_{αi} = ⟨V_α | φᵢ⟩

This is the inner product of a vertex state with an eigenmode. There are nine such products (three leptons × three neutrinos), and they form the PMNS matrix.

Computing all nine from the explicit vectors:

For the electron row (α = 1, using |V₁⟩ = (1,0,0)):
- U_{e1} = ⟨V₁|φ₋^(1)⟩ = 2/√6 = √(2/3)
- U_{e2} = ⟨V₁|φ₊⟩ = 1/√3
- U_{e3} = ⟨V₁|φ₋^(2)⟩ = 0

For the muon row (α = 2, using |V₂⟩ = (0,1,0)):
- U_{μ1} = ⟨V₂|φ₋^(1)⟩ = −1/√6
- U_{μ2} = ⟨V₂|φ₊⟩ = 1/√3
- U_{μ3} = ⟨V₂|φ₋^(2)⟩ = −1/√2

For the tau row (α = 3, using |V₃⟩ = (0,0,1)):
- U_{τ1} = ⟨V₃|φ₋^(1)⟩ = −1/√6
- U_{τ2} = ⟨V₃|φ₊⟩ = 1/√3
- U_{τ3} = ⟨V₃|φ₋^(2)⟩ = +1/√2

Assembling the matrix:

         U_PMNS^(0) =  |  √(2/3)    1/√3    0   |
                       |  −1/√6     1/√3   −1/√2 |
                       |  −1/√6     1/√3   +1/√2 |

This is the tribimaximal (TBM) mixing matrix, exactly. Unitarity is immediate since the eigenvectors form an orthonormal basis.


## Part 5: The Mixing Angles

Reading off the mixing angles from the TBM matrix:

sin²θ₁₃ = |U_{e3}|² = 0 exactly (the e–ν₃ element is zero)

sin²θ₁₂ = |U_{e2}|² / (1 − |U_{e3}|²) = (1/3) / 1 = 1/3 exactly

sin²θ₂₃ = |U_{μ3}|² / (1 − |U_{e3}|²) = (1/2) / 1 = 1/2 exactly

The CP-violating phase δ_CP is undefined at zeroth order because sin θ₁₃ = 0 (the Jarlskog invariant, which measures CP violation, is proportional to sin θ₁₃).

All three mixing angles are exact rational numbers in terms of simple fractions. No free parameters enter the calculation once the eigenmode identification is accepted.


## Part 6: Status and Corrections

The TBM mixing angles are not consistent with the current experimental values as exact results. The NuFIT 5.3 data gives:
- sin²θ₁₂ = 0.304 ± 0.012 (TBM: 1/3 = 0.333, 2.4σ off)
- sin²θ₂₃ = 0.570 ± 0.024 (TBM: 1/2 = 0.500, 2.9σ off)
- sin²θ₁₃ = 0.0220 ± 0.0006 (TBM: 0, more than 30σ off)

The reactor angle θ₁₃ is the most significant deviation — TBM predicts exactly zero while the measured value is definitively nonzero. TBM is excluded as an exact result by the Daya Bay measurement alone.

CPP treats TBM as the zeroth-order result. The corrections are:
- Δ(sin²θ₁₂) = −0.029 from charged-lepton mass matrix diagonalisation (OPEN-P-SM-5)
- Δ(sin²θ₂₃) = +0.070 from charged-lepton diagonalisation and Capotauro bias
- sin²θ₁₃ = 0.022 from Capotauro mechanism: sin²θ₁₃ ≈ φ⁻²/1.6 (OPEN-P-SM-4)

The corrections are of order sea_strength ≈ 0.178 — appropriate for first corrections to a leading-order result. The Capotauro mechanism is the leading candidate for θ₁₃ but its coefficient (1/1.6 = 0.625) is not yet derived from 600-cell geometry.


## Part 7: The K3 Unification Table

SM-5 completes the K3 subseries. The same equilateral triangle K3 encodes four Standard Model results via four independent mathematical properties:

| Paper | Result | K3 property used |
|-------|--------|-----------------|
| SM-1 | δ = 1/3 (charge quantisation) | C3 combinatorics |
| SM-3 | K = 2/3 (Koide ratio) | Spectral eigenvalue ratio 2:1 |
| SM-4 | Lepton mass constraint | Vertex occupation statistics |
| SM-5 | U_PMNS^(0) = U_TBM (neutrino mixing) | Eigenvector–vertex change of basis |

Each derivation uses a different property of K3 and is independent of the others. The triangle encodes charge, mass ratio, individual mass constraint, and mixing matrix simultaneously — four different physical phenomena from four different mathematical faces of the same geometric object.


## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|---------------|
| Two natural bases of K3 | §1 prerequisites; §3 Remark (why TBM emerges) |
| Neutrino identification | §2 Proposition 2.1 (ansatz, not derived) |
| Physical motivation | §2 proof block |
| PMNS as change of basis | §3 Theorem proof |
| Nine matrix elements | §3 proof (explicit inner products) |
| Mixing angles | §3 Eq. (tbm_angles) |
| Comparison with data | §4 Proposition 4.1 and Remark |
| K3 unification table | §5 Remark |
| Open problems | §5 Open Problems 1–5 |
