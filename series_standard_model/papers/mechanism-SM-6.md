# Mechanism — SM-6: The Charged Lepton Mass Spectrum from 600-Cell Lattice Geometry

## Mechanism 1: Mode Counting via Spectral Traces

**What it does:** Separates the vacuum propagation channels of the 600-cell into abelian (edge) and non-abelian (face) sectors and counts them.

**How it works:** Tr(A²) counts closed walks of length 2 — a DI-bit hops to a neighbour and returns along the same edge. This is a linear, 1D process = abelian. Tr(A³) counts closed walks of length 3 — a DI-bit circulates around a triangular face. This involves the K₃ structure that generates SU(2) = non-abelian. The ratio Tr(A²)/(Tr(A²)+Tr(A³)/3) = 3/8 is the bare mode fraction, a topological invariant of the graph.

**Key insight:** The mode counting is exact and does not depend on coupling constants, energy scales, or any physical input beyond the graph structure. It is the same ratio as the SU(5) GUT-scale Weinberg angle, emerging here from discrete geometry rather than Lie algebra normalisation.

## Mechanism 2: Propagation Efficiency and the φ Correction

**What it does:** Corrects the bare mode fraction for the metric difference between edge-scale and face-scale propagation.

**How it works:** Edge modes traverse physical distance l_edge = 1/φ per hop. Face modes circulate at the circumradius scale R = 1. The ratio η = l/R = 1/φ is the propagation efficiency of the edge channel. The Weinberg angle becomes sin²θ_W = η × (bare fraction) = (1/φ)(3/8) = 3/(8φ).

**Why the denominator is fixed:** The denominator Tr(A²)+Tr(A³)/3 = 3840 counts the total number of available propagation channels — a topological invariant. The metric correction affects channel efficiency, not channel existence. This is why the φ enters as a linear multiplicative prefactor, not quadratically through a coupling ratio.

**CPP operational definition:** sin²θ_W = (edge throughput)/(total lattice capacity). This differs from the SM definition g'²/(g²+g'²) because in CPP the mixing is between graph modes (topological) with metric-weighted efficiencies (geometric), not between gauge couplings (dynamic).

## Mechanism 3: The Isotropic Shift

**What it does:** Converts the Weinberg angle into the Koide phase correction without breaking any symmetry.

**How it works:** The EW abelian coupling sin²θ_W is distributed over the z+1 = 13 bonds of each K₃ vertex's closed neighbourhood. Each K₃ vertex has 2 internal bonds (to the other face vertices), contributing δe = 2sin²θ_W per vertex. Normalised by the closed neighbourhood size: ε = 2sin²θ_W/(z+1).

**Why it preserves C₃:** The perturbation δH = ε·I₃ is the same at all three vertices (by face-transitivity of the 600-cell, confirmed by the proved self-energy isotropy THEO-SM-5). The eigenvectors don't change. The antibonding degeneracy is preserved. But the eigenvalue RATIO changes because adding ε to {+2,−1,−1} increases λ₊ and decreases |λ₋|, pushing K upward from 2/3 to (2+ε)/3.

**Resolution of the C₃ paradox:** Every attempt to break C₃ in the antibonding subspace failed (thermal, pentagonal, self-energy — all ruled out). The correct mechanism doesn't break any symmetry. It changes the ratio through a uniform shift that affects +2 and −1 asymmetrically.

## Mechanism 4: The Unified K/θ Origin

**What it does:** Shows that the Koide ratio K and the Koide phase θ are the same number from the same source.

**How it works:** The K₃ eigenvalue ratio λ₊/|λ₋| = 2 gives K = λ₊/(λ₊+|λ₋|) = 2/3 as a rational fraction. The same eigenvalue ratio gives the base Koide phase cos θ₀ = −K = −2/3 as a cosine. The EW correction shifts this to cos θ = −(2+ε)/3 = −K(1+sin²θ_W/(z+1)). The Koide formula's two "independent" parameters have been hiding a self-referential structure for 44 years.
