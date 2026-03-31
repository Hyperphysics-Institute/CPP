# Mechanism — QM-1: Schrödinger Equation from DI-Bit Hopping

**Paper:** QM-1 (cpp2040a_v31.tex)
**Series position:** First paper — establishes the quantum wavefunction and its equation of motion from CPP primitives
**Last updated:** 31 March 2026

---

## Part 1: The DI-Bit Amplitude

**Step 1 — Each Grid Point carries a complex DI-bit amplitude.**
In CPP, Displacement Increment (DI) bits are relational quanta exchanged between Conscious Points. Each DI bit at Grid Point i carries both a number density ρᵢ and a geometric phase φᵢ accumulated at velocity c = l_P/t_P along its propagation path. The complex amplitude:

    ψᵢ = √ρᵢ × e^{iφᵢ}

is the CPP wavefunction at site i. The probability density |ψᵢ|² = ρᵢ is the local DI-bit number density — the Born rule is built into the definition, not postulated separately.

**Step 2 — Phase accumulates deterministically along lattice edges.**
As a DI bit hops from Grid Point i to neighbour j, it accumulates phase Δφ = m_CP × c × Δs / ħ, where Δs = l_P is the edge length and m_CP is the CP's mass. This is the same phase accumulation as the standard quantum mechanical propagator e^{iS/ħ}, with S the classical action along the hop. The phase is geometric — it is determined by the lattice structure and the CP's energy, not by any separate quantum postulate.

---

## Part 2: The Lattice Hopping Equation

**Step 3 — The discrete evolution equation.**
At each Absolute Moment, the DI-bit amplitude at site i evolves by hopping from all 12 nearest neighbours:

    ψᵢ(t + Δt) = ψᵢ(t) − (iΔt/ħ) Σⱼ Hᵢⱼ ψⱼ

where Hᵢⱼ = −T for nearest-neighbour pairs (j ~ i) and 0 otherwise, with the hopping amplitude T = ħ²/(4mΔs²). This is the tight-binding model on the 600-cell graph — a deterministic evolution rule involving no probability.

**Step 4 — The 600-cell graph Laplacian appears.**
For the 600-cell with coordination number z = 12, the sum Σⱼ(ψⱼ − ψᵢ) over all 12 neighbours equals 2Δs² ∇²ψ + O(Δs⁴) in the continuum limit — the discrete graph Laplacian converges to the continuous Laplacian. This is proved in QM-1 Appendix A using the exact 600-cell vertex coordinates.

---

## Part 3: The Continuum Limit — Schrödinger Equation

**Step 5 — The Schrödinger equation is the continuum limit of DI-bit hopping.**
THEO-QM-1: In the limit Δs → 0 with TΔs² = ħ²/(4m) held fixed, the discrete hopping equation becomes:

    iħ ∂ψ/∂t = −(ħ²/2m)∇²ψ + V(r)ψ

where V(r) = −k_PSR × Δ|SSV(r)| is the external potential sourced by the SSV field at position r. This is the time-dependent Schrödinger equation with a mechanically derived potential: V arises from Voronoi cell compression by local SSV gradients (the same PSR mechanism as SR-1). The Schrödinger equation is not postulated in CPP; it is the continuum-limit description of DI-bit hopping on the 600-cell lattice.

**Step 6 — The Madelung decomposition connects CPP to quantum hydrodynamics.**
Writing ψ = √ρ × e^{iS/ħ} and substituting into the Schrödinger equation gives the Madelung equations: a continuity equation ∂ρ/∂t + ∇·(ρv) = 0 (DI-bit number conservation — the CPP Nexus law), and an Euler-like equation with a quantum pressure term −ħ²/(2m) × ∇²(√ρ)/√ρ. The quantum pressure is not an extra postulate; it is the curvature of the DI-bit density field.

---

## Part 4: Lattice Corrections and Predictions

**Step 7 — Lattice corrections are suppressed by (l_P/λ)².**
The discrete-to-continuum derivation introduces corrections at order (l_P/λ)² relative to the leading term, where λ is the de Broglie wavelength of the DI-bit. For optical wavelengths, (l_P/λ)² ~ 10⁻⁵⁸ — far beyond any current or foreseeable measurement. The Schrödinger equation is exact at all laboratory scales.

**Step 8 — The lattice dispersion relation has a Planck-scale correction.**
The energy-frequency relation E = hν acquires a correction from the 600-cell lattice: E = hν[1 − (ν/ν_P)²] + O(ν/ν_P)⁴, where ν_P = c/l_P is the Planck frequency. This deviation from E = hν is a falsifiable prediction at Planck-scale energies.

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Steps 1–2: DI-bit amplitude and phase | §2 (DI-Bit Complex Amplitude) |
| Steps 3–4: lattice hopping and Laplacian | §3 (Lattice Hopping Hamiltonian), Appendix A |
| Step 5: Schrödinger equation | THEO-QM-1, §4, Eq. (Schrodinger) |
| Step 6: Madelung decomposition | §5 (Madelung Decomposition) |
| Steps 7–8: lattice corrections | §6 (Predictions) |
