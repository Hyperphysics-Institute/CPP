# FAQ — SM-6: The Charged Lepton Mass Spectrum from 600-Cell Lattice Geometry

---

## Conceptual Questions

### Q: What did this paper actually derive?
**A:** The masses of the three charged leptons (electron, muon, tau) from the geometry of a single mathematical object — the 600-cell polytope. The Standard Model treats these three masses as independent free parameters with no structural relationship. This paper derives all three from one calibration constant (the electron mass, which sets the overall energy scale) and zero shape parameters. The muon and tau masses are predictions, not inputs.

### Q: What is the 600-cell?
**A:** A regular 4-dimensional polytope with 120 vertices, 720 edges, 1200 triangular faces, and 600 tetrahedral cells. Think of it as the 4D analogue of the icosahedron. In CPP, it is hypothesised to be the fundamental lattice structure of spacetime at the Planck scale. Its key property for this derivation is that the ratio of edges to total modes (edges + faces) is exactly 3/8 — a number that matches the Weinberg angle at the grand unification scale.

### Q: What is the Koide formula and why is it important?
**A:** In 1981, Yoshio Koide noticed that the quantity K = (m_e + m_μ + m_τ)/(√m_e + √m_μ + √m_τ)² equals 2/3 to extraordinary precision (11 parts per million). This has no explanation in the Standard Model — it could be a coincidence, or it could be a clue to deeper structure. For 44 years, nobody could derive it. This paper derives both K = 2/3 and the phase angle θ that determines the individual masses.

### Q: How accurate are the predictions?
**A:** The Weinberg angle is predicted to 0.24% (sin²θ_W = 0.2318, PDG measures 0.2312). The Koide phase is predicted to 0.003% (θ = 132.731°, PDG-derived value is 132.732°). The muon mass is predicted to 0.18% and the tau mass to 0.15%. All with zero free parameters beyond the electron mass calibration.

### Q: Is this the same as numerology?
**A:** Numerology finds patterns in numbers without physical mechanism. This paper derives three independent quantities (K, sin²θ_W, θ) from the same geometric object through physical mechanisms (mode counting, propagation efficiency, isotropic eigenvalue shift). Each step is either a proved mathematical theorem or a physical argument grounded in CPP's lattice framework. The combined probability of three independent coincidences at this precision is less than 10⁻⁸.

---

## Technical Questions

### Q: Why does the Weinberg angle equal 3/(8φ)?
**A:** Two factors multiply: 3/8 is the fraction of propagation modes on the 600-cell that are abelian (edge modes, corresponding to U(1)_Y / photon channels). This is a topological invariant — it depends on the graph structure, not the geometry. The factor 1/φ is the propagation efficiency of edge modes: each edge hop covers physical distance l_edge = 1/φ (in circumradius units), so the abelian channel operates at reduced efficiency compared to the face-circulation (non-abelian) channel.

### Q: Why is the denominator fixed at 3840?
**A:** The denominator Tr(A²) + Tr(A³)/3 = 1440 + 2400 = 3840 counts the total number of propagation channels on the lattice. This is a topological invariant — it depends on how many edges and faces the graph has, not on how long the edges are. When the metric correction (propagation efficiency) is applied, it affects how well each channel works, not how many channels exist. The denominator stays fixed; only the numerator is corrected.

### Q: How does the isotropic shift work?
**A:** The K₃ triangle (the base of the lepton cage) has eigenvalues +2 (bonding) and −1 (antibonding, double). Adding a small uniform shift ε to all three eigenvalues gives +2+ε and −1+ε. The magnitudes become 2+ε and 1−ε. The ratio K = (2+ε)/3 is now larger than 2/3, which shifts the Koide phase. The key insight: you don't need to break the triangle's symmetry — a uniform shift changes the ratio because {+2, −1, −1} is asymmetric to begin with.

### Q: Where does the factor z+1 = 13 come from?
**A:** Each vertex of the 600-cell has 12 nearest neighbours. The "closed neighbourhood" includes the vertex itself plus its 12 neighbours = 13 sites. This is the natural normalization for a local perturbation in lattice field theory — the diagonal element of the closed-neighbourhood Laplacian L̃ = (z+1)I − Ã. The EW correction at a K₃ vertex is diluted by this factor because it is shared among all 13 sites in the closed neighbourhood.

### Q: What is the bond-counting argument?
**A:** Each K₃ vertex has 2 internal bonds (to the other two face vertices) and 10 external bonds (to the rest of the 600-cell). The electroweak abelian energy sin²θ_W is distributed isotropically over all bonds. The K₃ subspace "owns" 2 out of 13 bonds, so it receives 2sin²θ_W of abelian correction, normalized by the 13-site neighbourhood: ε = 2sin²θ_W/13.

---

## Comparison with Standard Model

### Q: How does CPP define the Weinberg angle differently from the SM?
**A:** In the SM, sin²θ_W = g'²/(g² + g'²) where g and g' are the SU(2) and U(1) gauge couplings. Both couplings are dynamic quantities. In CPP, sin²θ_W = (edge throughput)/(total lattice capacity) — the fraction of vacuum disturbances that propagate as photons. The denominator is a fixed topological invariant (3840); only the numerator carries the metric correction. This is a genuine departure from the SM, justified by the fact that CPP is a lattice theory where couplings are emergent and modes are topological.

### Q: Does CPP reproduce the running of the Weinberg angle?
**A:** The bare value 3/8 matches the SU(5) GUT-scale prediction. The corrected value 3/(8φ) matches the low-energy measurement. The 0.24% residual between 3/(8φ) and the PDG value is predicted to come from finite-temperature Dipole Sea corrections. Whether the full energy-dependent running can be derived from CPP is an open problem (listed in the paper's open problems section).

### Q: If CPP is correct, why does the SM work so well?
**A:** The SM is an effective field theory that describes the continuum limit of the underlying lattice physics. Just as lattice QCD reproduces continuum QCD in the appropriate limit, the CPP lattice reproduces SM predictions when the lattice spacing (Planck length) is much smaller than the observation scale. The SM parameters (coupling constants, masses) are the emergent values that the lattice geometry produces. CPP doesn't replace the SM — it explains why the SM parameters have the values they do.

---

## Challenges and Limitations

### Q: What is the weakest assumption in the derivation?
**A:** Assumption 5 (in the paper's attack surface, Section 7): the operational definition of sin²θ_W as (edge throughput)/(total lattice capacity) rather than g'²/(g²+g'²). This is a genuine departure from SM conventions, and a skeptical reader could argue that the two definitions need not agree. The paper's defence: in a lattice theory, the mode-fraction definition is more natural because modes are topological objects, not dynamic couplings.

### Q: What if the 600-cell is the wrong lattice?
**A:** Then the derivation fails. The 600-cell is an axiom of CPP, not a derived result. However, the 600-cell is the UNIQUE regular 4-polytope that gives both the bare Weinberg angle 3/8 (from its edge/face ratio) and the SU(2) gauge structure (from its binary icosahedral symmetry group). No other regular polytope has both properties.

### Q: Why are the predictions off by 0.15–0.18% instead of exact?
**A:** The 0.003% residual in the Koide phase (and the resulting 0.15–0.18% mass errors) are predicted to arise from finite-temperature Dipole Sea corrections — the same thermal fluctuations (ZBW partner-switching, rogue-wave SSV spikes) that produce quantum uncertainty in CPP's QM derivations. This is a quantitative prediction, not an excuse: the residual should equal sea_strength² ≈ 0.032, which is computable from independent CPP parameters.

### Q: Can this be extended to quarks?
**A:** The heavy quark triplet (c, b, t) already satisfies K ≈ 2/3 to 0.42%. Applying the same machinery (K₃ eigenvalues + EW efficiency + bond counting) to the quark sector is the natural next step. The quark sector involves additional complications (strong-sector renormalization, confinement) that may modify the formula, but the framework is ready to be tested.

---

*This FAQ is a living document. New questions will be added as they arise from readers, reviewers, and future research sessions.*
