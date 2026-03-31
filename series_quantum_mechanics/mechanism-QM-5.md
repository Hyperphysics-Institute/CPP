# Mechanism — QM-5: Quantum Field Theory from 600-Cell Eigenmode Excitations

**Paper:** QM-5 (cpp2040e_v31.tex)
**Last updated:** 31 March 2026

---

## Part 1: Field Operators from Lattice Eigenmodes

**Step 1 — DI-bit amplitudes are expanded in the 600-cell eigenmodes.**
The 600-cell adjacency matrix has 120 orthonormal eigenvectors u_k(i) (k = 1,...,120) with the six distinct eigenvalues. Any DI-bit amplitude configuration on the lattice can be expanded:

    ψᵢ = Σₖ aₖ uₖ(i)

where aₖ are the mode amplitudes. Quantising by promoting aₖ to operators â_k with [â_k, â†_k'] = δ_{kk'} (bosonic) or {â_k, â†_k'} = δ_{kk'} (fermionic), the field operator becomes:

    φ̂(rᵢ) = Σₖ (âₖ uₖ(i) + â†ₖ u*ₖ(i))

This is second quantisation — but here it emerges from the lattice eigenmode expansion, not from a postulated field theory.

**Step 2 — Commutation relations follow from eigenmode orthonormality.**
The canonical commutation relations [φ̂(rᵢ), π̂(rⱼ)] = iħ δᵢⱼ follow directly from the orthonormality of the 600-cell eigenmodes: Σₖ uₖ(i) u*ₖ(j) = δᵢⱼ. The commutation relations are not postulated; they are a consequence of the completeness of the lattice eigenfunction basis.

---

## Part 2: Statistics from Lattice Occupancy

**Step 3 — Fermions and bosons from lattice occupancy constraints.**
The 600-cell lattice has a maximum occupancy of one CP per Grid Point (from AXIM-1 and THEO-1: CP non-persistent co-occupation). Applying this exclusion constraint to the mode occupation numbers gives the Pauli exclusion principle — fermionic statistics for CP aggregates. Modes without exclusion (DP Sea modes, photon modes) are bosonic. The spin-statistics connection emerges from the lattice occupancy rule, not from the PCT theorem or relativistic QFT.

---

## Part 3: Free-Field Hamiltonian and Propagators

**Step 4 — The free-field Hamiltonian is the 600-cell adjacency operator.**
The lattice hopping Hamiltonian (QM-1) in the mode basis becomes:

    Ĥ = Σₖ ħωₖ â†ₖ âₖ,   ωₖ = T × λₖ

where λₖ are the 600-cell adjacency matrix eigenvalues. The six distinct eigenvalues produce six distinct frequency modes. The free propagators are the Green's functions of the lattice Laplacian — discrete versions of the standard QFT Feynman propagators, recovering the continuum propagators in the limit l_P/λ → 0.

---

## Part 4: Finite Renormalisation and the Hierarchy Problem

**Step 5 — The 600-cell provides a natural UV cutoff at the Planck scale.**
The lattice has a maximum wavevector k_max = π/l_P (Planck momentum). All loop integrals in QFT are cut off at this scale. The electron self-energy:

    Σ|_CPP ≈ (e²/4π²)E_P² + (e²m/4π²) ln(E_P²/m²) + O(m²/E_P²)

**Honest assessment of the hierarchy problem:** The correction is finite (not infinite, as in the cutoff-free SM) but still large (~E_P²). The bare mass must still be finely tuned to cancel this large correction. CPP converts the hierarchy problem from an infinite fine-tuning to a finite fine-tuning — a logical improvement, not a complete resolution.

---

## Part 5: The Eigenvalue Bridge to EW and QM Sectors

**Step 6 — The six 600-cell eigenvalues appear in both QM-5 and the EW series.**
The six distinct eigenvalues {12, 1+φ, φ−1, 1−φ, −φ, −(1+φ)} determine both the free-field dispersion relations in QM-5 (step 4) and the three electroweak boson topologies in EW-1 through EW-5. The suggestive 6 = 3×2 coincidence (3 fermion generations × 2 members per generation) is noted in QM-5 but not yet derived as a theorem. This is the eigenvalue bridge: the same six numbers govern QM field modes and EW boson masses.

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Steps 1–2: field operators and commutators | §2–4 (Complex DI-Bit Amplitudes, Field Operators, Commutation Relations) |
| Step 3: statistics from lattice | §5 (Fermions and Bosons from Lattice Occupancy) |
| Step 4: Hamiltonian and propagators | §6 (Free-Field Hamiltonian and Propagators) |
| Step 5: finite renormalisation | §7 (Finite Renormalization and the Hierarchy Problem) |
| Step 6: eigenvalue bridge | §8 (Six Eigenvalues and Three SM Generations) |
