# Glossary — EW Series: Electroweak Bosons from 600-Cell Topology

**Papers:** EW-1 through EW-5 (cpp_ew1_intro_v3.tex through cpp_ew5_unification_v3.tex)
**Last updated:** 30 March 2026

*This glossary covers all EW-series-specific terms. General CPP terms (CP, Dipole Sea, SSV, ZBW, Grid Point, Absolute Moment) are in the CPP master glossary. Terms shared with the QM series (eigenvalues, adjacency matrix) are defined here in the EW context.*

---

## 600-Cell Adjacency Matrix

The 120×120 matrix A where A_{ij} = 1 if vertices i and j of the 600-cell are nearest neighbours (connected by an edge of length a = 1/φ) and 0 otherwise. Each vertex has exactly 12 nearest neighbours, so A has row sum 12, and λ = 12 is the largest eigenvalue. The six distinct eigenvalues of A are {12, 1+φ, φ−1, 1−φ, −φ, −(1+φ)}, arising from the icosahedral H₄ symmetry of the lattice.

The adjacency matrix is the EW series' primary structural object. It bridges the QM series (QM Paper 6 established the six eigenvalues) and the EW series (the same eigenvalues select the three electroweak boson topologies).

---

## A₅ Symmetry

The alternating group on 5 elements, of order 60. A₅ is the symmetry group of the icosahedron and the dodecahedron in 3D. In the EW series, A₅ symmetry of the dodecahedral 20-vertex shell forces the Higgs-like resonance to be a scalar (spin 0): A₅ contains no preferred axis (no subgroup isomorphic to Z₂ in the relevant representation), so it is impossible to define a polarisation direction, and the resonance must be spin-0.

---

## Axial-Vector Coupling (Z boson)

The coupling structure of the Z boson, in which both vector (V) and axial-vector (A) components contribute with equal weight. In CPP, this follows from the icosahedral loop's four-layer phase interference: the closed icosahedral geometry sums over symmetric vector and axial components equally, producing the V+A and V−A combination. In standard electroweak theory, the Z coupling to fermions is gf = T₃ − Q sin²θ_W, which includes both left- and right-handed components. The CPP account explains why the Z couples differently from the W.

---

## Bracelet (W boson topology)

The specific hDP substructure of the W⁰ boson: a closed 6-cycle ring of 6 hybrid Dipole Pairs (12 Conscious Points total: 3×+eCP, 3×−eCP, 3×+qCP, 3×−qCP, net Q = 0). The bracelet is topologically distinct from both the icosahedral loop (Z) and the dodecahedral shell (H): it is a 1-dimensional ring embedded in the 600-cell subgraph, not a 2-dimensional polyhedral surface. This gives it an open interior through which external CPs can approach — the physical cause of the W's reactivity and its role as a charged-current mediator.

---

## Eigenvalue Bridge

The identification connecting the six 600-cell adjacency matrix eigenvalues to the three Standard Model electroweak bosons. Established in EW-1 as the foundation of the entire EW series. The bridge works because the eigenvalue of a closed subgraph determines the phase coherence of hDP circulation around it, which determines the confinement energy, which determines the mass. The same six eigenvalues appear in QM Paper 6 in the context of three SM generations — the eigenvalue bridge connecting the QM and EW sectors is a CPP cross-series consilience result.

---

## Eigenvalue–Topology Correspondence

The theorem (EW-1 Theorem 1–3) that each stable closed subgraph of the 600-cell is selected by a specific eigenvalue or eigenvalue pair of the adjacency matrix:

| Eigenvalue | Topology | Boson | Vertices |
|-----------|---------|-------|---------|
| λ = 12 | Icosahedral loop | Z | 12 |
| λ = {1+φ, φ−1} | Bracelet | W | 12 |
| λ = −(1+φ) | Dodecahedral shell | Higgs-like | 20 |

The eigenvalue determines the phase relationship between adjacent hDPs in the subgraph. High positive λ → in-phase → symmetric → low confinement energy → low mass. Most negative λ → anti-phase → frustrated → high confinement energy → high mass.

---

## Geometric Dilution Factor (φ⁻³)

The ratio of a boson's subgraph volume to the full 600-cell volume:

    V_subgraph / V_600-cell = φ⁻³ ≈ 0.236

This follows from the 1:φ:φ² shell-radius scaling of the 600-cell and is the derived component of the holographic mass reduction. The geometric factor φ⁻³ applies to all three bosons (W, Z, H) because all three subgraphs are drawn from the same 600-cell geometry. It reduces the Planck-scale confinement energy by a factor of ~4, but the remaining ~10¹⁷ reduction (from Planck to weak scale) requires the η factor.

---

## Holographic Dilution

The two-step reduction from Planck-scale confinement energy to weak-scale boson masses:

    m_boson = E_conf × (V_subgraph/V_600-cell) × η = E_conf × φ⁻³ × η

The first factor φ⁻³ is derived from 600-cell geometry. The second factor η ~ 10⁻¹⁷ is attributed to holographic spreading of bit flux across N ~ 10⁶¹ cosmic-horizon Grid Points — the idea that the boson's SSV field is diluted over the entire cosmic lattice. This second factor is currently calibrated to reproduce the known boson masses and is the central open problem of the EW series (OPEN-P-EW-1).

---

## hybrid_weak_factor

A dimensionless factor = 1.5, arising from the ratio of weak interaction layers (3) to electromagnetic polarities (2). It enters the geometric factor f_geom for each boson's mass formula. It is a fixed parameter shared across all EW papers, independent of the boson topology. Its value 3/2 reflects that the weak interaction involves three layers of phase interference (SU(2)_L triplet) while EM involves two polarities (eCP/−eCP). It is reproduced from the vertex structure, not independently derived from first principles.

---

## Loop Density Factor (Z boson, ℓ_Z)

A multiplicative factor in the Z boson's geometric contribution to its mass, arising from the constructive interference of hDP bit flows around the closed icosahedral loop. The ideal geometric estimate from the loop closure is ℓ_Z^ideal = 1 + 1/12^(1/3) ≈ 1.437. The effective value used in Monte Carlo after 4D projection effects is ℓ_Z ≈ 1.2. The discrepancy (1.437 vs 1.2) is attributed to 4D projection losses in the stereographic mapping from the 600-cell's 4D coordinates to 3D physical space but has not been derived analytically. Registered as OPEN-P-EW-3.

---

## Neutral W⁰ Boson

The CPP-specific neutral virtual particle that is the precursor to the observed W±. The W⁰ is a closed bracelet of 6 hDPs assembled spontaneously from the DP Sea at STP conditions on the λ = {1+φ, φ−1} subgraph. Net charge = 0. It has no SM analog. The W⁰ is distinct from the observed W± in that it carries no charge of its own; charge is acquired from the surrounding reaction when the W⁰ mediates a quark or lepton flavor transition in a high-energy collision.

The W⁰/W± distinction is the most novel CPP-specific prediction in the electroweak series. Experimental detection of the W⁰ would require precision Dipole Sea background measurements — currently beyond experimental reach.

---

## Phase Interference Layers

The four successive levels of hDP bit-flow interaction in the 600-cell that produce the Weinberg mixing angle. Each layer corresponds to a specific phase shift:

- Layer 1: direct flows along the central tetrahedron (phase 0)
- Layer 2: first reflections at 120° (second tetrahedron)
- Layer 3: second reflections at 240° (third tetrahedron)
- Layer 4: 360° modulo closure from loop-completing geodesics

The overlap probabilities decay as p_k ~ (1 − k/5)², k = 1,2,3,4, from the golden-ratio scaling of the 600-cell vertex positions. These four layers are the CPP mechanism underlying the Weinberg angle — they are the geometric source of the SU(2)_L/U(1)_Y mixing.

---

## Planck-to-Weak-Scale Reduction (η)

The factor η ~ 10⁻¹⁷ by which the Planck-scale confinement energy (after applying the φ⁻³ geometric factor) must be further reduced to give the observed boson masses at the weak scale (~80–125 GeV). Currently calibrated to match PDG masses. Physically attributed to holographic spreading — each bit of SSV flux propagating outward from the boson is diluted over all N ~ 10⁶¹ Grid Points within the cosmic horizon. The derivation of η from first principles is OPEN-P-EW-1, the central open problem of the EW series. Until this is derived, m_W, m_Z, m_H are reproduced (fitted) rather than derived.

---

## Shell Density Factor (Higgs, s_H)

A multiplicative enhancement in the Higgs-like resonance's mass arising from the higher vertex density of the 20-vertex dodecahedral shell compared to the 12-vertex icosahedral Z loop. The ideal geometric estimate from the icosahedron-dodecahedron duality is s_H^ideal = √(20/12) × φ^(−1/2) ≈ 1.014. The effective Monte Carlo value after 4D projection is s_H ≈ 1.4. The gap between ideal and effective is unresolved — registered as OPEN-P-EW-3 (loop/shell density factors from 4D projection).

---

## Spectral Ordering and Mass Hierarchy

The principle that the EW boson masses follow the spectral ordering of the 600-cell adjacency matrix. The three bosons are ordered:

    λ = 12 (most positive) → Z (lightest, 91 GeV)
    λ = {1+φ, φ−1} (intermediate) → W (intermediate, 80 GeV)
    λ = −(1+φ) (most negative) → Higgs (heaviest, 125 GeV)

This ordering is a theorem of the eigenvalue-topology correspondence. The mass hierarchy $m_Z < m_W < m_H$ is not fitted to the observed masses but follows from the eigenvalue structure. Note: in terms of eigenvalue magnitude, |λ_Z| = 12 is largest, but in terms of frustration (anti-correlation energy), λ = −(1+φ) is most frustrated and produces the heaviest boson.

---

## SU(2)_L (Weak Isospin Group)

The symmetry group of the weak charged current. In CPP (EW-5), SU(2)_L emerges from the 600-cell's 120°/240° phase bias structure. The interference operators I^a(φ_i, φ_j) = cos(Δφ_{ij}) × SSV-gradient for cyclic 120° vertex separations satisfy [I^a, I^b] = iε^{abc} I^c (proved in EW-5 Theorem 1). The left-handed preference (~75% from the 120°/240° asymmetry) reproduces the V−A structure of weak charged currents.

---

## U(1)_Y (Weak Hypercharge Group)

The Abelian symmetry group of the weak neutral current. In CPP (EW-5), U(1)_Y emerges from the radial shell structure of the 600-cell: the three shells with radius ratios r:rφ:rφ² give an Abelian polarisation gradient with no angular non-commutativity. The ratio g'/g ≈ (40/64)φ⁻¹ ≈ 0.387 from the outer/inner shell vertex ratio, within ~30% of the PDG value. Full derivation requires solving OPEN-P-EW-2.

---

## Weinberg Angle (sin²θ_W)

The weak mixing angle that parametrises the mixing between the SU(2)_L and U(1)_Y gauge bosons to produce the observed W, Z, and photon. PDG value: sin²θ_W(M_Z) = 0.23121 ± 0.00004. CPP derived value: 0.2312 ± 0.0003 (agreement 0.004%). The Weinberg angle is the only quantity in the EW series that is fully derived from 600-cell geometry without a calibration factor — it follows from the four-layer phase interference eigenvalue weighting formula in EW-1 and EW-5.

---

## Yang-Mills EFT Limit

The result (EW-5 Theorem 3) that the discrete CPP bit-exchange dynamics converge to the Yang-Mills effective Lagrangian ℒ_eff = −(1/4)F^aμν F_{aμν} + (D_μΦ)†(D^μΦ) − V(Φ) in the coarse-graining limit l_P/L → 0. The convergence rate is |A_μ^discrete − A_μ^continuum| ~ O(l_P/L) → 0 as L >> l_P. The discrete plaquette sum recovers the Wilson gauge action with β = 2N_c/g². This theorem establishes that standard gauge field theory is the long-wavelength limit of CPP's bit-exchange dynamics, not a separate postulate.
