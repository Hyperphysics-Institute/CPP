# Mechanism — QM-4: Quantum Measurement and Decoherence from the DP Sea

**Paper:** QM-4 (cpp2040d_v31.tex)
**Last updated:** 31 March 2026

---

## Part 1: The DP Sea as Decoherence Bath

**Step 1 — The DP Sea is an infinite-temperature Markovian bath.**
The Dipole Sea fills all of space with randomly-oriented dipole pairs oscillating at f_ZBW ≈ 1/(2t_P). Each Sea DP interacts with any nearby CP aggregate via SSV exchange. The Sea has a continuous spectrum of oscillation frequencies (from 0 to ≈ 1/(2t_P)), an effectively infinite temperature (kT_P >> ħω₀ for all relevant ω₀), and no memory (correlation time ≈ t_P — one Absolute Moment). These three properties make the DP Sea a Markovian bath satisfying the Born-Markov approximation.

**Step 2 — The interaction Hamiltonian is an SSV projection operator.**
When a DI-bit qubit (the "system") is coupled to the DP Sea (the "environment"), the interaction is:

    H_int = Σⱼ gⱼ(aⱼ + aⱼ†) ⊗ σ̂_z

where aⱼ, aⱼ† are DP Sea mode creation/annihilation operators for mode j, gⱼ is the SSV coupling strength, and σ̂_z is the system's spin projection. This interaction tags the system state with a phase imprinted on the Sea — the physical mechanism of which-path information (QM-2, Step 6) at the formal level.

---

## Part 2: The Lindblad Master Equation

**Step 3 — Applying the Born-Markov approximation gives the Lindblad equation.**
THEO-QM-6 (Lindblad from DP Sea scattering): Under the Born-Markov approximation (weak coupling, short correlation time), the reduced density matrix ρ of the DI-bit qubit satisfies:

    dρ/dt = −(i/ħ)[H_S, ρ] + γ(σ̂_z ρ σ̂_z − ρ)

where the dephasing rate:

    γ = (sea_strength)² × E_P / ħ

The dephasing rate is not a free parameter — it is expressed entirely in terms of sea_strength (THEO-SS-6, derived from 600-cell geometry to 3.8%) and the Planck energy E_P. This is the first Lindblad derivation in CPP that gives an explicit, calculable dephasing rate from the theory's geometric constants.

---

## Part 3: Pointer States and Apparent Collapse

**Step 4 — SSV eigenstates are the pointer basis.**
The Lindblad equation has preferred basis states — the pointer basis — in which decoherence is slowest. For the dephasing interaction H_int ∝ σ̂_z, the pointer states are the eigenstates of σ̂_z: the spin-up and spin-down states. This is not arbitrary — it follows from the SSV field's projection axis being the measurement axis. The physical meaning: the DP Sea selects the measurement outcomes by preferentially decohering superpositions relative to eigenstates.

**Step 5 — Measurement is apparent collapse, not true collapse.**
The Nexus enforces global unitarity throughout the decoherence process. The total quantum state (system + Sea) evolves unitarily at all times. What appears as "wavefunction collapse" from the perspective of the system alone is decoherence: the off-diagonal elements of ρ decay to zero as the system entangles with the Sea. The CPP measurement problem is solved by identifying collapse as the environmental entanglement of the DI-bit state with the DP Sea degrees of freedom.

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Steps 1–2: DP Sea as bath and H_int | §2 (DP Sea as Decoherence Bath), §3 |
| Step 3: Lindblad derivation | THEO-QM-6, §3, Eq. (lindblad) |
| Step 4: pointer states | §4 (Pointer Basis: SSV Eigenstates) |
| Step 5: apparent collapse | §5–§6 (Global Unitarity and the Nexus) |
