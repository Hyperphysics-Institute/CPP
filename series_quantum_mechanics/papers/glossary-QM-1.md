# Glossary — QM Series: Quantum Mechanics from 600-Cell DI-Bit Dynamics

**Papers:** QM-1 through QM-6 (cpp2040a–f, v3.1)
**Last updated:** 31 March 2026

---

## Born Rule

The quantum mechanical rule that the probability of finding a particle at position r is proportional to |ψ(r)|². In standard QM the Born rule is postulated. In CPP it follows directly from the definition of the DI-bit amplitude ψ = √ρ × e^{iφ}: the modulus squared |ψ|² = ρ is the DI-bit number density at that lattice site, and detection probability equals local DI-bit density. The Born rule is not a new postulate in CPP; it is built into the definition of ψ.

---

## Decoherence Rate (γ)

The rate at which off-diagonal elements of a qubit's reduced density matrix decay due to interaction with the DP Sea bath. Derived in QM-4 (THEO-QM-6):

    γ = (sea_strength)² × E_P / ħ

With sea_strength = 0.178 (THEO-SS-6) and E_P ≈ 1.956 × 10⁹ J:

    γ ≈ 5.9 × 10⁴² s⁻¹

This is the CPP prediction for the fundamental quantum-to-classical decoherence rate. It is so fast that macroscopic superpositions decohere in ~10⁻⁴³ s — far faster than any observable quantum coherence in macroscopic systems, explaining why the classical world is classical. Unlike phenomenological decoherence models, γ is fixed by the theory's geometric constant sea_strength with no additional parameters.

---

## Displacement Increment (DI) Bit

The fundamental relational quantum in CPP — the unit of information exchanged between Conscious Points. Each DI bit carries a complex amplitude ψᵢ = √ρᵢ × e^{iφᵢ} at Grid Point i, where ρᵢ is the bit density (proportional to detection probability) and φᵢ is the deterministic geometric phase accumulated at velocity c = l_P/t_P along the propagation path. DI bits are not particles and not fields; they are information quanta whose collective behaviour produces quantum mechanics.

---

## Eigenmode Expansion (QFT)

The decomposition of DI-bit amplitudes on the 600-cell in terms of the 120 orthonormal eigenvectors of the adjacency matrix: ψᵢ = Σₖ aₖ uₖ(i). Quantising the mode amplitudes aₖ → â_k gives the field operators of QFT. The commutation relations [â_k, â†_k'] = δ_{kk'} follow from eigenmode orthonormality. This is how second quantisation emerges in CPP: from the completeness of the lattice eigenfunction basis, not from a separate postulate.

---

## Entanglement (CPP account)

The non-separability of a joint DI-bit state — the impossibility of writing the state as a product of individual-particle states. In CPP, entanglement arises from the Nexus's global phase constraint: when two CPs are created in a conserved total state, the Nexus enforces correlations between their DI-bit phases that cannot be factored into local states. Entanglement is not a mysterious non-local influence; it is a consequence of the global Nexus constraint built into the lattice dynamics from the beginning.

---

## Fock Space

The Hilbert space of QFT, built from states with definite numbers of excitations. In CPP, Fock space emerges from the 600-cell eigenmode expansion (QM-5): the vacuum state is the DP Sea with no coherent mode excitations; n-particle states are states with n modes occupied above the vacuum. The total excitation number is conserved by the Nexus (enforcing DI-bit number conservation), which is why Fock space has a definite particle-number structure.

---

## Graph Laplacian

The discrete differential operator on the 600-cell lattice: (Lψ)ᵢ = Σⱼ~ᵢ (ψⱼ − ψᵢ), summing over all 12 nearest neighbours j of site i. Proved in QM-1 Appendix A: Lψ = 2Δs² ∇²ψ + O(Δs⁴) in the continuum limit. This is the key mathematical result connecting the 600-cell discrete lattice to the continuous Laplacian operator of standard quantum mechanics and QFT.

---

## Hierarchy Problem (CPP resolution)

The naturalness problem in the SM — why the Higgs mass is ~125 GeV rather than ~10¹⁹ GeV (the Planck scale) when quadratic divergences from loop corrections push it toward the Planck scale. In CPP, the 600-cell lattice imposes a natural UV cutoff at the Planck scale. Loop integrals are finite rather than infinite. The electron self-energy: Σ|_CPP ≈ (e²/4π²)E_P² + (e²m/4π²) ln(E_P²/m²). The self-energy is finite but still ~E_P² — the hierarchy problem is converted from an infinite fine-tuning problem to a finite one. CPP does not solve the hierarchy problem but improves its character.

---

## Lindblad Master Equation

The quantum master equation governing the time evolution of a system's reduced density matrix when it is weakly coupled to a Markovian environment. In standard QM this equation is derived by tracing over bath degrees of freedom; it is exact only under the Born-Markov approximation. In CPP (QM-4, THEO-QM-6), the Lindblad equation with dephasing rate γ = (sea_strength)² × E_P/ħ is derived from the explicit coupling of the DI-bit qubit to the DP Sea modes via the SSV interaction Hamiltonian. The derivation makes the approximations used (Born-Markov) explicit rather than hiding them.

---

## Madelung Decomposition

The polar form of the Schrödinger wavefunction: ψ = √ρ × e^{iS/ħ}, where ρ = |ψ|² is the probability density and S is the phase (action). Substituting into the Schrödinger equation gives the Madelung equations: a continuity equation (Nexus DI-bit conservation) and a modified Euler equation (containing the quantum pressure term). The Madelung decomposition is the direct bridge between the DI-bit density/phase description (CPP) and the wavefunction description (standard QM).

---

## Measurement Problem (CPP resolution)

The question of why quantum superpositions appear to collapse when observed, even though unitary evolution never produces definite outcomes from superpositions. In CPP (QM-4), the measurement problem is resolved by identifying collapse as decoherence: the DI-bit qubit entangles with the DP Sea modes during interaction, causing the off-diagonal elements of the qubit's reduced density matrix to decay exponentially (Lindblad evolution). The global state (qubit + Sea) remains unitarily evolved throughout; collapse is apparent from the subsystem perspective. The Nexus enforces global unitarity at every Absolute Moment — there is no true collapse.

---

## No-Signaling

The property that Alice's measurement outcome probabilities are independent of Bob's measurement settings in an entangled pair, and vice versa. Proved in QM-3 (THEO-QM-5): for the singlet state, P(A=+1) = 1/2 regardless of Bob's axis. The Nexus, although non-local (it acts globally at each Absolute Moment), enforces no-signaling because it enforces conservation laws — it redistributes information between already-correlated parts of the global state without creating new correlations across spacelike separations.

---

## Path Integral (CPP account)

The Feynman path integral in standard QFT postulates that the amplitude for a particle to travel from source s to detector d is the sum over all paths of e^{iS_path/ħ}. In CPP (QM-2), this sum arises naturally from the Nexus conservation law: DI bits propagate simultaneously along all available lattice geodesics, each accumulating a deterministic phase. The discrete Feynman sum ψ(d) = Σₖ A₀ e^{iφₖ} over lattice paths is not postulated — it is what the Nexus conservation of DI-bit number produces automatically.

---

## Pointer States

The preferred basis states in a system-environment interaction — the states that decohere slowest and therefore appear as the classical outcomes of measurements. In CPP (QM-4), the pointer states are the eigenstates of the SSV projection operator σ̂_z in the Lindblad interaction: these are the states that do not entangle with the DP Sea modes and therefore maintain their coherence longest. The pointer states are selected dynamically by the SSV coupling, not chosen arbitrarily.

---

## Spin-Statistics Connection

The rule that fermions (half-integer spin) obey the Pauli exclusion principle (antisymmetric wavefunctions) while bosons (integer spin) do not (symmetric wavefunctions). In standard QFT this follows from the PCT theorem and Lorentz invariance. In CPP (QM-5), it follows from the CP non-co-occupation theorem (THEO-1): CPs cannot persistently occupy the same Grid Point. Since CP aggregates (particles) are built from CPs, their states are antisymmetric under exchange of constituent CPs — fermionic statistics. DP Sea modes (gluons, photons) are not CP aggregates but open-path propagating modes, and they are bosonic. The spin-statistics connection follows from the lattice occupancy rule rather than from Lorentz invariance.

---

## Tsirelson Bound

The maximum value of the CHSH Bell parameter S in quantum mechanics: |S|_max = 2√2. In standard QM this is derived from the properties of the quantum correlation function E(â,b̂) = −cos θ. In CPP (QM-3, THEO-QM-4), the Tsirelson bound is derived from the singlet DI-bit state and the Nexus global phase constraint. The derivation uses no quantum axioms beyond the non-separability of the singlet (proved from the Nexus constraint) and the deterministic phase accumulation of DI bits.

---

## ZBW Helix

The Zitterbewegung oscillation of a CP aggregate — a helical trajectory on the 600-cell lattice arising from the ZBW oscillation frequency f_ZBW ≈ 1/(2t_P) (THEO-1 + CORL-1a). The helix axis defines the spin quantisation direction for spin-½ CP aggregates. The ZBW helix encodes quantum spin as a geometric property of the CP aggregate's trajectory — not a separate internal degree of freedom but the spatial structure of the aggregate's motion through the lattice.
