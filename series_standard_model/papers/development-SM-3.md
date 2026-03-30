# Development History: SM-3 — The Koide Relation from the Colour Cage Base Graph

**Series:** 600-Cell Standard Model Emergence
**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet (Anthropic)
**Document type:** Development narrative — laboratory notebook record
**Last updated:** 30 March 2026


## Origins: The Koide Formula as a Target

The Koide formula K = 2/3 was identified early in the CPP programme as a high-priority target. It is the most precisely tested unexplained empirical relation in particle physics — holding to 11 ppm across a mass range of 3477. If CPP could derive it from geometric first principles, that derivation would be the strongest quantitative confirmation of the framework available before collider experiments.

Thomas Lee Abshier ND had noted the Koide formula's potential connection to the K₃ cage base from early work on the CPP cage hierarchy. The three-vertex structure of the cage base — the equilateral triangle {V₁, V₂, V₃} — was already known to produce δ = 1/3 from its combinatorial symmetry. The question was whether its spectral structure could also produce K = 2/3.


## Phase 1: The Basic Algebraic Insight

The fundamental algebraic identity was established first: K = (1 + ρ²/2)/3, so K = 2/3 ⟺ ρ = √2. The Koide formula reduces to proving that the modulation depth in the parametrisation √mᵢ = A(1 + ρcos φᵢ) equals exactly √2.

The connection to the K₃ spectrum was then identified: the eigenvalue ratio λ_max/|λ_min| = 2/1 for K₃ is exactly the ratio that, via thermal equipartition (P3), gives ρ² = 2 and hence ρ = √2. The algebraic chain was clear: K₃ eigenvalue ratio → occupation ratio → ρ → K.

This gave the theorem's skeleton. The remaining work was establishing the physical justification for each step — the three propositions.


## Phase 2: Deriving P1 (Sessions A–B)

P1 — that the ZBW Hamiltonian equals ℏω₀ × A_{K₃} — was the first proposition to be established rigorously. Two inputs are needed: (a) C3 symmetry forces equal hopping amplitudes on all three K₃ edges, and (b) the SSV potential at the confinement radius sets the hopping energy to ℏω₀ = sea_strength × ℏc/r_conf.

Part (a) follows directly from SM-1 Theorem 1 (C3 cage symmetry). Part (b) requires connecting the SSV hopping amplitude to the existing sea_strength derivation from SS-1 §8. The connection was established: ℏω₀ = sea_strength × ℏc/r_conf ≈ 87.8 MeV is the ZBW hopping energy at the confinement scale. This is consistent with SS-1 Theorem 6 (the DP binding energy E_eDP = ℏω₀/φ² where the 1/φ² factor is the Voronoi volume projection). P1 was declared derived.


## Phase 3: Deriving P2 (Session C)

P2 — mass proportional to |ψᵢ|² — was derived from the CPP DI-bit visit rate. The argument: the ZBW orbital spends a fraction |ψᵢ|² of its time at vertex Vᵢ (standard quantum mechanics in the finite K₃ system). DI-bits are processed at rate proportional to time at Vᵢ. Mass energy is organisational energy stored per DI-bit processed. Therefore mᵢ ∝ |ψᵢ|².

Each step in the chain follows from either standard quantum mechanics applied to K₃ or from CPP axioms. P2 was declared derived.


## Phase 4: P3 and the θ Problem (Sessions D–L)

P3 — equal eigenstate occupation — was the most problematic proposition. Early versions of SM-3 stated P3 as an independent postulate ("assume the three K₃ eigenstates are equally populated"). This was scientifically unsatisfactory — a postulate with no CPP derivation.

Simultaneously, multiple sessions attempted to derive the Koide phase θ = 132.73°, hoping that the mechanism for θ might also provide P3's derivation. Session B attempted Aharonov-Bohm flux through the cage triangle — the C3 symmetry prevents the flux from breaking the degeneracy. Session C attempted spin-orbit coupling within the cage. Session E attempted Löwdin downfolding from K₄ to K₃ — the fourth vertex V₄ is dark to the antibonding modes (⟨φ₋|v⟩ = 0 exactly). Session F attempted Aharonov-Bohm in the 4D 600-cell embedding. Session G computed all 600 tetrahedral cells of the 600-cell and confirmed that C3 is preserved exactly in 4D — no embedding breaks the degeneracy. Session K tested self-consistent ZBW mass feedback — the fixed-point iteration converges to θ = 180° (trivial), not 132.73°.

After 11 mechanisms were tested and falsified, the structural impossibility theorem emerged: no mechanism acting on the K₃ cage base that respects C3 symmetry can select θ. This negative result was formulated as a theorem in SM-4 (Theorem 2) and registered as OPEN-P-SM-7d.

The P3 derivation was found independently of the θ work. The key observation: the DP Sea is at the Planck temperature. The ZBW energy scale is ℏω₀ ≈ 88 MeV. The ratio kT_P/ℏω₀ ≈ 10²⁰. In this limit, the Boltzmann distribution assigns equal weight to all eigenstates — state-counting equipartition. P3 is derived from the physical temperature ratio, not postulated. Session D established this derivation and elevated SM-3 from a conditional theorem to a full derivation.


## Phase 5: Harmonisation to v5 (26 March 2026)

Version 5 incorporated eight harmonisation corrections:

H1: Series ID SM-3 added to title; series name corrected to "600-Cell Standard Model Emergence Series." H2: Author line updated to include Claude Sonnet (Anthropic); institution block added. H3: Bibliography added (Koide 1982, PDG 2024, SS-1, SM-1, SM-4). H4: Acknowledgements section added. H5: Date updated to Version 5, 26 March 2026. H6: hyperref package added for cross-references. H7: OPEN-P-SM-7d registered with formal \openproblem LaTeX environment. H8: siunitx and graphicx packages added.

The harmonisation also added the scope table in §6, which explicitly marks each result as Proved, Derived, Calibrated, or Open. This table is the clearest single summary of SM-3's status and was identified as essential for readers evaluating the paper's claims.


## Current Status (30 March 2026)

SM-3 is submission-ready at v5. It is the strongest theorem paper in the SM series: K = 2/3 proved with zero free parameters, all three propositions derived from CPP axioms, and the structural impossibility of deriving θ documented as a theorem rather than a gap.

The six SM-3 documentation files were written on 30 March 2026.


## Key Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| Early 2026 | Target Koide formula as highest-priority | Most precise unexplained SM relation; CPP triangle structure natural fit |
| Session A | P1 derived from C3 + SSV hopping | C3 forces equal hopping; SSV sets amplitude to ℏω₀ |
| Session C | P2 derived from DI-bit visit rate | Mass = ZBW energy ∝ time at vertex ∝ |ψ|² |
| Sessions B–K | 11 θ mechanisms attempted and falsified | Each failure narrowed the derivation space |
| Session G | Structural impossibility of θ from K₃+SSV | C3 makes antibonding subspace degenerate; θ requires EW sector |
| Session D | P3 derived from DP Sea thermal limit | kT_P/ℏω₀ ≈ 10²⁰; state-counting equipartition in high-T limit |
| 26 Mar 2026 | Harmonisation to v5 | Series consistency: title, authors, bibliography, scope table |
