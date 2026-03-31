# Phenomena — QM-1 through QM-6: Quantum Mechanics from 600-Cell DI-Bit Dynamics

**Papers:** QM-1 through QM-6 (cpp2040a–f, v3.1)
**Last updated:** 31 March 2026

---

## Section 1: Explained Phenomena (PHEN-E)

### PHEN-QM-E1. The Time-Dependent Schrödinger Equation Governs Quantum Evolution (QM-1)

**Observation:** All quantum systems evolve according to iħ ∂ψ/∂t = Ĥψ. This is confirmed to extraordinary precision across atomic, molecular, nuclear, and condensed matter physics. In standard QM it is an axiom.

**CPP account:** THEO-QM-1: The Schrödinger equation is the continuum limit of DI-bit hopping on the 600-cell lattice. The tight-binding evolution rule ψᵢ(t+Δt) = ψᵢ(t) − (iΔt/ħ)ΣⱼHᵢⱼψⱼ on the 600-cell graph converges to the Schrödinger equation as Δs → 0 via the graph Laplacian. The external potential V(r) = −k_PSR × Δ|SSV(r)| is the SSV field from SR-1 — the same field that produces time dilation also produces quantum potentials.

**Primary paper:** QM-1


### PHEN-QM-E2. Quantum Interference Is Wave-Like Despite Particle-Like Detection (QM-2)

**Observation:** In double-slit experiments, individual particles build up an interference pattern — each particle is detected at a point, but the probability distribution has wave-like fringes. This wave-particle duality is one of the deepest puzzles of quantum mechanics.

**CPP account:** DI bits from source s propagate simultaneously along all available geodesics to detector d, each accumulating a deterministic geometric phase φₖ. The total amplitude ψ(d) = Σₖ A₀ e^{iφₖ} produces constructive interference (large |ψ|²) where phases align and destructive interference where they cancel. Detection is a single event (one CP absorbs the DI-bit density at d) but the probability is determined by |ψ(d)|² = the sum-over-paths density. Wave-particle duality is not a paradox in CPP; it is the natural result of DI-bit path summation.

**Primary paper:** QM-2


### PHEN-QM-E3. Bell Inequalities Are Violated — Quantum Correlations Are Non-Classical (QM-3)

**Observation:** Bell inequality experiments (Aspect 1982, Hensen 2015, and many others) confirm that the CHSH parameter |S| can reach 2√2, violating the classical bound |S| ≤ 2. This rules out all local hidden variable theories.

**CPP account:** The singlet DI-bit state |Ψ⁻⟩ is non-separable (THEO-QM-3) due to the Nexus global phase constraint. The correlation function E(â,b̂) = −cos(θ) follows from the ZBW helix spin encoding and the non-separable joint state. The CHSH parameter |S| = 2√2 is derived (THEO-QM-4). The Nexus is not an LHV — it is a global constraint, not a local influence. No-signaling is proved (THEO-QM-5).

**Primary paper:** QM-3


### PHEN-QM-E4. Quantum Decoherence Produces Classical Behaviour (QM-4)

**Observation:** Macroscopic objects do not exhibit quantum superpositions. The transition from quantum (coherent superposition) to classical (definite state) is explained by decoherence — entanglement of the quantum system with its environment. This is experimentally confirmed through atomic and molecular decoherence measurements.

**CPP account:** THEO-QM-6: The DP Sea acts as a Markovian decoherence bath, producing Lindblad evolution with dephasing rate γ = (sea_strength)² × E_P/ħ ≈ 5.9 × 10⁴² s⁻¹. The pointer states (SSV eigenstates) decohere slowest and appear as classical measurement outcomes. Collapse is apparent — the Nexus maintains global unitarity throughout. The decoherence rate is a specific numerical prediction from the theory's geometric constant sea_strength.

**Primary paper:** QM-4


### PHEN-QM-E5. Quantum Field Theory — Second Quantisation and the Fock Space (QM-5)

**Observation:** Quantum field theory — the framework combining quantum mechanics with special relativity — describes all particle physics to extraordinary precision. Its mathematical structure (field operators, Fock space, propagators, Feynman diagrams) requires separate postulation in standard approaches.

**CPP account:** QFT emerges from the 600-cell eigenmode expansion of DI-bit amplitudes. Field operators from eigenmode amplitudes, commutation relations from eigenmode orthonormality, fermion statistics from CP non-co-occupation, free propagators from the lattice Green's function. The Yang-Mills Lagrangian is the continuum limit of CPP bit-exchange dynamics (THEO-EW-8). QFT is not a separate framework in CPP — it is what CPP looks like at scales l_P << λ.

**Primary paper:** QM-5


### PHEN-QM-E6. The Measurement Problem — Why Quantum Systems Appear to Collapse (QM-4)

**Observation:** When a quantum system is measured, the wavefunction appears to "collapse" to a definite eigenstate. This apparent collapse has puzzled physicists for a century. The measurement problem is one of the deepest unresolved issues in the foundations of quantum mechanics.

**CPP account:** Collapse is apparent decoherence, not true collapse. The DI-bit qubit entangles with DP Sea modes during measurement, causing the off-diagonal density matrix elements to decay. The global state (qubit + Sea) remains unitarily evolved; only the reduced density matrix of the subsystem appears to collapse. The Nexus enforces global unitarity throughout. The measurement problem does not exist in CPP in the same form because the theory's ontology (DI bits, Nexus, DP Sea) makes the decoherence mechanism physically explicit.

**Primary papers:** QM-4, QM-6


---

## Section 2: Novel Predictions (PHEN-P)

### PHEN-QM-P1. Lattice Dispersion Correction to the Energy-Frequency Relation

**Prediction:** The 600-cell lattice modifies the de Broglie energy-frequency relation at Planck-scale frequencies:

    E = hν[1 − (ν/ν_P)²] + O(ν/ν_P)⁴

where ν_P = c/l_P ≈ 2 × 10⁴³ Hz is the Planck frequency. At optical frequencies (ν ~ 10¹⁵ Hz), the correction is (ν/ν_P)² ~ 2 × 10⁻⁵⁷ — completely unobservable. At Planck-scale energies, the correction reaches order 1 and the lattice discreteness is directly manifested.

**Status:** PRED-O — future Planck-scale accelerators or GRB gamma-ray timing.


### PHEN-QM-P2. Specific Decoherence Rate from sea_strength

**Prediction:** The fundamental quantum-to-classical transition rate is γ = (sea_strength)² × E_P/ħ ≈ 5.9 × 10⁴² s⁻¹. This is a specific numerical prediction from sea_strength, distinct from all phenomenological decoherence models. No current experiment can measure the decoherence rate at this timescale, but the prediction that γ scales as sea_strength² × E_P/ħ distinguishes CPP from any theory with a different coupling or Planck-scale factor.

**Status:** PRED-O — not currently testable; conceptually falsifiable if the decoherence rate's energy dependence can be measured.


### PHEN-QM-P3. Bell Correlations Receive Planck-Scale Lattice Corrections

**Prediction:** The quantum correlation function E(â,b̂) = −cos θ acquires corrections at order (l_P/d)² where d is the measurement separation:

    E_CPP(â,b̂) = −cos θ + O(l_P/d)²

For d = 1 metre, (l_P/d)² ~ 10⁻⁷⁰ — completely unobservable. The standard Bell correlation is exact at all accessible scales.

**Status:** PRED-O — confirms standard QM at all accessible scales; correction unobservable.


---

## Section 3: Validated Phenomena — Consilience (PHEN-V)

### PHEN-QM-V1. Bell = 2√2 Confirmed Across All Experiments

**The observation:** All precision Bell tests from Aspect (1982) to loophole-free tests (2015–present) confirm |S_max| = 2√2, the quantum Tsirelson bound, to within experimental precision.

**CPP:** THEO-QM-4 derives |S| = 2√2 from the singlet non-separability and DI-bit phase correlations. Fully consistent.


### PHEN-QM-V2. Decoherence Explains Classical World — Consistent with CPP Scale

**The observation:** Macroscopic objects decohere to classical states in timescales shorter than any observable quantum coherence. For a dust grain (10⁻⁷ kg) in air, the decoherence time is ~10⁻³⁰ s.

**CPP:** The fundamental decoherence rate γ ~ 10⁴² s⁻¹ is far faster than any macroscopic coherence time. The classical world is classical because the DP Sea decoheres any macroscopic superposition in ~10⁻⁴³ s. CPP predicts a classical world — it does not need to explain why quantum coherence breaks down at large scales; the decoherence rate makes it inevitable.


### PHEN-QM-V3. The Eigenvalue Bridge — Same Six Numbers in QM and EW

**The observation:** The six 600-cell adjacency eigenvalues {12, 1+φ, φ-1, 1-φ, -φ, -(1+φ)} appear in QM-5 as the free-field dispersion frequencies, and in EW-1 through EW-5 as the three electroweak boson topologies. The same six numbers from the same mathematical object.

**CPP significance:** This is the CPP eigenvalue bridge — the unification of quantum mechanics and the electroweak force through a shared geometric structure. It is a prediction: the six eigenvalues that govern quantum field modes at the Planck scale are the same six that select the three macroscopic EW bosons. If additional eigenvalues were discovered in either sector, both would need revision simultaneously.


### PHEN-QM-V4. Schrödinger Equation Exact at All Laboratory Scales

**The observation:** The Schrödinger equation has been verified to extraordinary precision across all laboratory quantum systems — from single atoms to condensed matter systems with 10²³ particles.

**CPP:** THEO-QM-1 derives the Schrödinger equation as the continuum limit of DI-bit hopping. Lattice corrections are O(l_P/λ)² ~ 10⁻⁵⁸ at optical scales. The Schrödinger equation is exact at all accessible energies. This is complete consistency with all existing quantum mechanics experiments.


*Document prepared by Thomas Lee Abshier ND and Claude Sonnet (Anthropic), 31 March 2026.*
