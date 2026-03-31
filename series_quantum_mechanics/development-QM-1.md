# Development History — QM Series: Quantum Mechanics from 600-Cell DI-Bit Dynamics

**Papers:** QM-1 through QM-6 (cpp2040a–f)
**Series version at documentation:** v3.1 (all six papers)
**Last updated:** 31 March 2026

---

## Series Identity

**Full titles:**
- QM-1 (cpp2040a): Schrödinger Equation from DI-Bit Hopping on the 600-Cell Lattice
- QM-2 (cpp2040b): Superposition and Interference from Multi-Path DI-Bit Propagation
- QM-3 (cpp2040c): Entanglement and Bell Inequality Violation in CPP
- QM-4 (cpp2040d): Quantum Measurement from DP Sea Decoherence
- QM-5 (cpp2040e): Emergent QFT and Finite Renormalisation from the 600-Cell Lattice
- QM-6 (cpp2040f): Capstone — All of QM from Four Primitives

**Authors:** Thomas Lee Abshier ND and Grok (xAI)

---

## Series-Level Proved Theorems (all from v3.1)

| ID | Theorem | Paper |
|----|---------|-------|
| THEO-QM-1 | Schrödinger equation from DI-bit hopping (continuum limit) | QM-1 |
| THEO-QM-2 | Born rule from DI-bit density | QM-2 |
| THEO-QM-3 | Non-separability of the singlet | QM-3 |
| THEO-QM-4 | Tsirelson bound in CPP: |S| = 2√2 | QM-3 |
| THEO-QM-5 | No-signaling in CPP | QM-3 |
| THEO-QM-6 | Lindblad from DP Sea scattering; γ = sea_strength² × E_P/ħ | QM-4 |
| THEO-QM-7 | Field operator commutation from eigenmode orthonormality | QM-5 |
| THEO-QM-8 | Fermion statistics from CP non-co-occupation | QM-5 |

---

## Version History

**v2 (early 2026):** Initial versions of all six papers. The core physical ideas were established: DI bits as the wavefunction substrate, 600-cell graph Laplacian as the source of the Schrödinger equation, singlet non-separability from the Nexus constraint, DP Sea as decoherence bath.

**v3 (March 2026):** Theorems formalised. The non-separability proof (THEO-QM-3) and the Tsirelson bound derivation (THEO-QM-4) were added as formal theorems with explicit proofs. The Lindblad derivation (THEO-QM-6) was worked out with the specific dephasing rate γ = (sea_strength)² × E_P/ħ — the first QM series result that gives a numerical prediction from sea_strength.

**v3.1 (current):** All papers in the QM series are at v3.1. The eigenvalue bridge section was added to QM-5 (§8, Six Eigenvalues and Three SM Generations), explicitly connecting the QM series to the EW series. The capstone paper QM-6 was revised to include the Nexus role table and the consolidated predictions table.

---

## Key Cross-Series Connections

**Eigenvalue bridge (QM-5 → EW-1 through EW-5):** The six 600-cell adjacency matrix eigenvalues {12, 1+φ, φ-1, 1-φ, -φ, -(1+φ)} appear in both QM-5 (as free-field dispersion modes) and the EW series (as boson topology selectors). The QM-5 paper notes this connection and registers it as the starting point for the EW series. Both series are reading the same six numbers from the same geometric object.

**Dephasing rate (QM-4) ↔ sea_strength (SS-1):** The Lindblad dephasing rate γ = (sea_strength)² × E_P/ħ uses sea_strength from SS-1 THEO-SS-6. This is a direct quantitative connection between the strong-sector geometry (sea_strength ≈ 0.178 derived from α_geom) and the quantum-mechanical decoherence rate. The same lattice constant that governs QCD coupling also governs quantum decoherence.

**Nexus roles (QM-6 Table):** The QM-6 capstone synthesises the Nexus's role at each of the five QM levels. This table is the QM series' most important single result for understanding CPP's ontology: the Nexus is not several different mechanisms but one mechanism (global DI-bit conservation) manifesting at different levels.

---

## Open Problems from the QM Series

- OPEN-P-QM-1 (Derive ħ from CPP statistics): The ZBW random walk (PROP-1) should produce ħ from first principles. Not yet computed.
- OPEN-P-QM-6 (Derive SWE from DP chain standing waves): An alternative derivation of the Schrödinger equation via DP chain standing waves rather than DI-bit hopping. OPEN-P-QM-6 in the QM-new series.
- OPEN-P-QM-new (Partner-switching series, 30 March 2026): Nine open problems from the PROP-1 through PROP-15 session; see propositions.md and open_problems/README.md.
