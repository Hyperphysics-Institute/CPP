# CPP_the_theory.md Update — SM-8/SM-9/SM-10 Additions

**Instructions:** Add to the Strong Sector / Quark Mass chapter in connected prose.

---

## The Quark Mass Programme (SM-8, SM-9, SM-10)

### Quark Cages from 600-Cell Distance Shells (SM-8)

The 600-cell polytope contains eight distance shells as measured from any vertex. Of these eight, exactly four possess edges — they form bonded polyhedral cages. Shell 1 is a tetrahedron (V=4, E=6), Shell 2 an icosahedron (V=12, E=30), Shell 4 a dodecahedron (V=20, E=30), and Shell 5 an icosidodecahedron (V=30, E=60). Shell 3 has twelve vertices but zero edges — a gap in the bonded sequence. Shells 5 through 7 are identified with the inner shells of neighbouring cells via the palindrome symmetry of the vertex count sequence (4, 12, 12, 20, 30, 20, 12, 12, 4), leaving exactly four independent cages and hence three quark generations plus a gap — matching the Standard Model's three-generation structure.

Each cage confines a quark flavour: the tetrahedron confines the strange quark, the icosahedron confines charm, the dodecahedron confines bottom, and the icosidodecahedron confines top. The quark mass is determined by the number of Dipole Pairs organised into chain networks within each cage, with each organised DP contributing energy M₀ = m_e z/φ = 3.790 MeV — the electron mass times the coordination number divided by the golden ratio.

### The Scaling Exponent (SM-9)

The quark masses scale as M = M₀ V^(7/3), where V is the cage vertex count. The exponent 7/3 decomposes as V² × V^(1/3): pair counting (every chain interacts with every other, giving C(V,2) ~ V² pairs) times the linear cage dimension (V^(1/3)). This decomposition was established through the angular-weighted pair model, which also produced the Symmetry Degeneracy Theorem: for any vertex-transitive polyhedron inscribed on S², the angular pair sum Σ sin²(θ_ij/2) = V²/4 exactly. This theorem — the strongest purely mathematical result in the CPP programme — proves that angular weighting cannot distinguish between cages; only the edge structure carries mass-relevant information.

The top quark exceeds the V^(7/3) trend by a factor of 16, which decomposes as z × C_F = 12 × 4/3. The twelve coordination bonds of Shell 3 (which has vertices but no edges) serve as relay stations, each carrying the SU(3) vertex factor C_F = 4/3 independently derived in SS-2. The zero-parameter formula M_q = M₀ V^(7/3) × [1 or 16] predicts all four quark masses (strange through top) with 2.1% RMS error across four orders of magnitude.

### The Chain Network Mechanism (SM-10)

The physical mechanism behind V^(7/3) is a cascade of organised Dipole Pairs. A central quark CP launches radial chains toward opposite-polarity cage vertices. Where chains pass near each other, cross-links form, recruiting additional DPs from the Sea. The cascade fills the cage volume through three bonding regions: near the centre (dense cross-linking of converging radials), mid-cage (web mesh of tangential-to-tangential links), and near the surface (upward-arching tangentials terminating on cage vertices).

For the pre-gap quarks (strange, charm, bottom), the cascade rate f₀ increases monotonically: 0.738 (strange), 0.805 (charm), 1.000 (bottom — the percolation threshold). The bottom quark represents the maximum mass achievable by cascade alone. The top quark exceeds this limit through the Shell 3 relay mechanism, where DPs occupy the twelve edgeless Shell 3 positions as bonding stations, amplifying the mass by z × C_F = 16.

The organised DP density follows a universal constant: ρ_org/(V^(7/3)/d³) = 0.24 for all three pre-gap quarks, breaking to 3.9 for the top quark — independent confirmation of the two-regime physics. A strange quark contains approximately 25 organised DPs; the top quark contains approximately 45,600. The chain network is sparse, not continuum-like.

First-principles derivation of the cascade rates from DP-level dynamics requires the DP-DP interaction potential, which belongs to the SS-series (strong sector). Until this interaction law is derived from the lattice mode spectrum, the FEM simulation remains a calibrated geometric model. The V^(7/3) formula, however, is a zero-parameter prediction that stands independently.

## Update Prediction Scorecard — ADD for SM-8/9/10:

| Observable | CPP | Measured | Error | Params | Paper |
|-----------|-----|---------|-------|--------|-------|
| m_s (zero-param) | 96.3 MeV | 93.4 MeV | +3.1% | 0 | SM-8 |
| m_c (zero-param) | 1,249 MeV | 1,270 MeV | −1.6% | 0 | SM-8 |
| m_b (zero-param) | 4,115 MeV | 4,180 MeV | −1.6% | 0 | SM-8 |
| m_t (zero-param) | 169,571 MeV | 172,760 MeV | −1.8% | 0 | SM-8 |
| # Generations | 3 | 3 | exact | 0 | SM-8 |
| Quark mass RMS | 2.1% | — | — | 0 | SM-8/9 |
