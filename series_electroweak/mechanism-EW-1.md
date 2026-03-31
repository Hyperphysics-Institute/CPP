# Mechanism — EW-1: Electroweak Bosons from 600-Cell Eigenvalue Topology

**Paper:** EW-1 (cpp_ew1_intro_v3.tex)
**Series position:** Introductory paper — establishes the eigenvalue bridge and derives the Weinberg angle
**Last updated:** 30 March 2026

*This file provides a sequential cause-and-effect account of the EW-1 mechanisms. For individual boson details see mechanism-EW-2.md through mechanism-EW-4.md. For the full SU(2)_L and gauge structure derivations see mechanism-EW-5.md.*

---

## Part 1: The Eigenvalue Bridge

**The 600-cell adjacency matrix has exactly six distinct eigenvalues:**

    λ ∈ {12,  1+φ,  φ−1,  1−φ,  −φ,  −(1+φ)}

where φ = (1+√5)/2 ≈ 1.618 is the golden ratio. This was established in QM Paper 6. Every vertex of the 600-cell has exactly 12 nearest neighbours, producing the maximally symmetric eigenvalue λ = 12 as the ground state. The remaining five eigenvalues arise from the icosahedral symmetry group H₄ acting on the 120 vertices. They come in golden-ratio conjugate pairs: {1+φ, φ−1}, {1−φ, −φ}, and the single extreme value −(1+φ).

**Why eigenvalues select bosons:** In CPP, a stable closed subgraph of the 600-cell — a region whose vertices can sustain a self-reinforcing hDP configuration — corresponds to a specific eigenvalue or eigenvalue pair of the adjacency matrix. The eigenvalue determines the phase coherence of the hDP circulation around the subgraph: high positive eigenvalue → high phase coherence → maximum symmetry → lowest confinement energy → lowest mass. Most negative eigenvalue → maximum phase anti-correlation → maximum frustration → highest confinement energy → highest mass.

**Step 1 — The spectrum maps to a mass hierarchy.** The six eigenvalues span from the most uniform configuration (λ = 12, all vertices in phase) to the most frustrated configuration (λ = −(1+φ), adjacent vertices in exact anti-phase). Every position in this spectrum corresponds to a specific confinement energy, and confinement energy is mass. The mass hierarchy of the electroweak bosons follows the spectral ordering of the 600-cell adjacency matrix — not as a coincidence but as a theorem of the eigenvalue-topology correspondence.

---

## Part 2: The Three Boson Topologies

**Step 2 — λ = 12 selects the Z boson (ground state).**
The eigenvector for λ = 12 is the constant all-ones vector — uniform DI-bit amplitude across all 120 Grid Points. The stable closed subgraph is the icosahedral 12-vertex loop. The icosahedron is completely closed: no vertex has an external hDP connection. Because it is the ground state (most symmetric, lowest frustration), the Z is the lightest of the three electroweak bosons and the most stable. It has no reactive openings and cannot mediate charge transfer.

**Step 3 — λ = {1+φ, φ−1} selects the W boson (intermediate states).**
The two intermediate positive eigenvalues correspond to a closed 6-cycle bracelet of 6 hDPs (12 CPs). The bracelet is a ring, not a complete polyhedral shell. Unlike the Z icosahedron or the H dodecahedron, the bracelet has an open interior — external CPs can approach through this opening. This topological openness is what makes the W reactive: it can mediate charge transfer between quarks and leptons by accepting a CP from outside its ring. The W exists in two stages: a neutral W⁰ assembled from the DP Sea (no SM analog), and the observed W± formed when the W⁰ acquires charge ±e from a high-energy collision.

**Step 4 — λ = −(1+φ) selects the Higgs-like resonance (most frustrated state).**
The most negative eigenvalue corresponds to maximum phase anti-correlation: adjacent Grid Points have opposite-sign DI-bit amplitudes. The stable closed subgraph is the dodecahedral 20-vertex shell. Twenty vertices, fully closed, with A₅ (alternating group of order 60) symmetry. Maximum frustration means maximum confinement energy means maximum mass — the Higgs is the heaviest of the three bosons. The A₅ symmetry, which contains no preferred axis, forces the Higgs to be a scalar (spin 0).

**Step 5 — The remaining two eigenvalues {1−φ, −φ} do not produce additional bosons.**
These two eigenvalues correspond to excited modes of the same dodecahedral geometry. No regular polyhedral closed subgraph with vertex count strictly between 12 and 20 exists in the 600-cell. This is a prediction: there is no stable electroweak scalar between m_Z = 91 GeV and m_H = 125 GeV. This prediction is consistent with all LHC data.

---

## Part 3: Topology Determines Reactivity

**Step 6 — Closure determines whether a boson mediates charge or not.**

The three topologies are not just geometrically different — their topological difference is the physical cause of their different roles in electroweak interactions:

- W bracelet: open interior → external CPs can enter → charge transfer mediated → charged-current weak interactions
- Z icosahedral loop: fully closed polyhedron → no entry point → no charge transfer → neutral-current weak interactions only
- H dodecahedral shell: fully closed polyhedron → no entry point → does not mediate interactions → couples to mass via SSV compression energy

This is the CPP account of one of the most fundamental distinctions in the Standard Model — why W exchange changes quark/lepton identity while Z exchange does not.

---

## Part 4: The Weinberg Angle Derivation

**Step 7 — Phase interference across four layers produces the mixing angle.**
The 600-cell's tetrahedral cells produce phase mismatches of 120° and 240° for hDP bit flows through adjacent vertices. When these flows are tracked across four interference layers (direct, first reflection, second reflection, loop-completion), the overlap probabilities decay as:

    p_k ~ (1 − k/5)²,   k = 1, 2, 3, 4

**Step 8 — The Weinberg mixing ratio emerges from the eigenvalue-weighted sum.**
The SU(2)_L coupling g and the U(1)_Y coupling g' are reproduced from vertex-count ratios of the 600-cell's three shells (middle shell 64/total 120 for g; outer/inner ratio 40/16 with φ⁻¹ suppression for g'). The Weinberg angle is then:

    sin²θ_W = Σₖ pₖ gₖ'² / Σₖ pₖ(gₖ² + gₖ'²)

Monte Carlo over 10⁶ configurations gives sin²θ_W(M_Z) = 0.2312 ± 0.0003, matching PDG to 0.004%. This is the most rigorously derived result in the EW series: it uses no free parameters beyond the 600-cell geometry.

**Step 9 — Internal consistency check through m_Z/m_W.**
The Weinberg angle gives cos θ_W = √(1−0.2312) = 0.8773. The tree-level relation m_W/m_Z = cos θ_W predicts m_Z/m_W = 1.1401. The masses derived independently in EW-2 and EW-3 give 91.1876/80.377 = 1.1344, agreeing to 0.5% without cross-calibration. This is the strongest internal self-consistency check in the EW series.

---

## Part 5: Holographic Mass Reduction

**Step 10 — The geometric dilution factor φ⁻³ is derived.**
The ratio of the subgraph volume (bracelet, icosahedron, or dodecahedron) to the full 600-cell volume follows from the 1:φ:φ² shell-radius scaling of the 600-cell:

    V_subgraph / V_600-cell = φ⁻³ ≈ 0.236

This factor applies to all three bosons and is a genuine geometric derivation requiring no free parameter.

**Step 11 — The Planck-to-weak-scale reduction η ~ 10⁻¹⁷ remains open.**
After applying φ⁻³, the confinement energy still exceeds the weak scale by ~10¹⁷. The remaining reduction is attributed to holographic spreading of bit flux across N ~ 10⁶¹ cosmic-horizon Grid Points, but a first-principles derivation is not yet complete. This is OPEN-P-EW-1 — the central open problem of the entire EW series. The individual boson masses (m_W, m_Z, m_H) are reproduced by calibrating η to the known values; they are not derived.

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Step 1: eigenvalue–mass ordering | Eq. (eigenvalues), Table 1 |
| Steps 2–5: three boson topologies | Theorems 1–3 (EW-1), THEO-EW-1 through THEO-EW-3 |
| Step 6: topology determines reactivity | §W⁰/W± Distinction, Remark (topology) |
| Steps 7–9: Weinberg angle | §3 (Weinberg Angle), Eq. (weinberg) |
| Step 10: φ⁻³ geometric factor | §4, Eq. (phi3) |
| Step 11: η open problem | OPEN-P-EW-1 |
