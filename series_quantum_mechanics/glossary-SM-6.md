# Glossary — SM-6: The Charged Lepton Mass Spectrum from 600-Cell Lattice Geometry

## Core Mathematical Objects

**600-cell polytope:** The regular 4-polytope with V=120 vertices, E=720 edges, F=1200 triangular faces, and C=600 tetrahedral cells. Coordination number z=12. Edge length in circumradius units: l = 1/φ. The fundamental lattice of CPP.

**Adjacency matrix (A):** The 120×120 symmetric matrix with A_ij = 1 when vertices i,j share an edge. Has 9 distinct eigenvalues with multiplicities dim²(ρ) for the irreps of the binary icosahedral group 2I.

**K₃ (complete graph on 3 vertices):** The triangular base of each tetrahedral cell. Adjacency eigenvalues: +2 (bonding, multiplicity 1) and −1 (antibonding, multiplicity 2). The lepton cage structure.

**Spectral traces:** Tr(A²) = 2E = 1440 (counts length-2 closed walks = edge back-and-forth). Tr(A³) = 6F = 7200 (counts length-3 closed walks = oriented face circulations). Tr(A³)/3 = 2F = 2400 (face modes with cyclic overcounting removed).

**Closed neighbourhood:** For vertex v: the set {v} ∪ {neighbours of v}. Size = z+1 = 13. The closed-neighbourhood Laplacian is L̃ = (z+1)I − Ã where Ã = A + I.

**Golden ratio (φ):** φ = (1+√5)/2 ≈ 1.6180. Appears as the edge-to-circumradius ratio of the 600-cell, in 4 of the 9 adjacency eigenvalues, and as the metric correction factor for the Weinberg angle.

## Physical Concepts

**Edge mode:** A closed walk of length 2 on the 600-cell (DI-bit hops along an edge and returns). Linear, 1D, abelian. Corresponds to U(1)_Y hypercharge / photon propagation channel.

**Face mode:** A closed walk of length 3 (DI-bit circulates around a triangular face). Circulatory, 2D, non-abelian. Corresponds to SU(2)_L weak isospin / W/Z boson propagation channel.

**Propagation efficiency (η):** The physical distance covered per hop, normalised by the circumradius. For edge modes: η = l_edge/R_circ = 1/φ. For face modes: η = 1 (by convention). The metric correction from SSV/PSR evaluated at the edge vs. circumradius scale.

**Operational Weinberg angle:** In CPP: sin²θ_W = (edge throughput)/(total lattice capacity) = η·Tr(A²)/(Tr(A²)+Tr(A³)/3). The fraction of vacuum disturbances that propagate as photons. NOT the SM formula g'²/(g²+g'²).

**Isotropic shift:** The perturbation δH = ε·I₃ on a K₃ face from the electroweak sector. Shifts all eigenvalues equally, preserving C₃ symmetry, but changes the eigenvalue RATIO because {+2,−1,−1} is asymmetric. ε = 2sin²θ_W/(z+1) = 3/(52φ).

**Koide ratio (K):** K = (Σm_i)/(Σ√m_i)² = 2/3 for charged leptons. In CPP: K = λ₊/(λ₊+|λ₋|) = 2/3 from K₃ eigenvalue ratio. Proved in SM-3 (THEO-SM-2).

**Koide phase (θ):** The angle in the Koide parametrisation √m_i = (S/3)(1+√2 cos(θ+2πi/3)). PDG value: 132.73°. In CPP: cos θ = −(2/3)(1+sin²θ_W/(z+1)) = −(2/3)(1+3/(104φ)). Derived in this paper.

**SSV₀:** The rest-state SSV field energy at the electron mass scale. SSV₀ = m_e c²/2 = 0.2555 MeV. The single calibration constant of the lepton mass derivation.

## Status Labels

**PROVED:** Derived from axioms by exact mathematics (spectral traces, eigenvalue computations, algebraic identities).

**DERIVED:** Follows from proved results plus physical arguments with every step justified by geometry, proved theorems, or standard lattice field theory.

**CONJECTURED:** Numerically confirmed but with at least one step requiring physical reasoning not yet formalised as a proof.
