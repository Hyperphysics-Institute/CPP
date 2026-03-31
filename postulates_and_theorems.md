# CPP Postulates and Theorems Registry

**Last updated:** 30 March 2026
**Purpose:** Source of truth for what CPP assumes (postulates) and what it has proved (theorems). The ratio of theorems to postulates measures theoretical progress. The goal is maximum theorems from minimum postulates.

*30 March 2026 update: AXIM-5 (ZBW oscillations, formerly AXIM-5 (demoted)) demoted from axiom to theorem THEO-1 + corollary CORL-1a. Axiom count reduced from 7 to 6. Propositions PROP-1 through PROP-15, Theorem THEO-1, Corollaries CORL-1a/1b, and Open Problems OPEN-P-QM-new-1 through OPEN-P-QM-new-8 added from partner-switching session. See propositions.md for full derivations.*

---

## Vocabulary

**Postulate (= Axiom):** An assumption declared without proof. Cannot be derived from anything more fundamental *within* CPP. The irreducible commitments of the theory.

**Definition:** A naming convention. Gives precise meaning to a term. Not proved or assumed — chosen. Definitions are not theoretical claims.

**Lemma:** A small proved result used as a step toward a theorem. Important but not the main point.

**Theorem:** A major proved result. Derived from postulates and definitions by logical argument (including mathematical calculation). This is the primary unit of theoretical progress.

**Corollary:** A result that follows immediately from a theorem, requiring little or no additional argument.

**Proposition:** A proved result, less central than a theorem. Often an intermediate result or a supporting claim.

**Conjecture:** A proposed theorem not yet proved. Must be testable (falsifiable) and clearly stated.

**Falsified:** A conjecture or claim that has been tested and found wrong. Recorded so it is not tried again.

---

## CPP Core Postulates

These are the irreducible assumptions of CPP. Everything else should be derived from them.

| ID | Name | Statement | Status |
|----|------|-----------|--------|
| **AXIM-1** | Conscious Points | Conscious Points (CPs) exist as the fundamental information-processing units of reality. Each CP has: polarity (+/−), type (eCP or qCP), a position on the 600-cell lattice, and the capacity to emit and receive DI-bits according to universal rules. | Core axiom |
| **AXIM-2** | 600-cell lattice | Space consists of a tiling of 600-cell polytopes. The 120 vertices of each cell are the only allowed CP positions. CPs move by hopping between vertices. There is no continuous space between vertices. | Core axiom — discreteness of space |
| **AXIM-3** | Dipole Sea | All of space is filled with randomly oscillating dipole pairs (DPs). The sea maximises entropy by default. Particles are stable departures from this randomness. | Core axiom — the vacuum |
| **AXIM-4** | SSV interaction | CPs generate a Space Stress Vector field that falls off as 1/r². Opposite polarities attract; like polarities repel. The SSV is the unified source of all four fundamental forces in different limits. | Core axiom — the force law |
| **[DEMOTED → THEO-1]** | ZBW oscillations | **[DEMOTED TO THEOREM — 30 March 2026]** The ZBW oscillation of bound DP pairs is a derived consequence of the SSV force law (AXIM-4) on a discrete lattice (AXIM-2). Opposite-polarity CPs approach under monotonically increasing SSV_net attraction to superimposition; at superimposition, intra-pair SSV direction vanishes; bulk SSV drives opposite displacements. Period ≈ 2t_P → f_ZBW ≈ 1/(2t_P) as a theorem. See THEO-1 and CORL-1a. | Demoted — derivable from AXIM-2+AXIM-4 |
| **AXIM-5** | Mass as organisational energy | Rest mass is the energy cost of imposing stable order on the Dipole Sea. A particle is a stable configuration of CPs that locally organises the sea against its tendency toward maximum entropy. | Core axiom — ontology of mass |
| **AXIM-6** | Absolute Moment | At each Planck time step (Absolute Moment), every CP evaluates its incoming DI-bits and updates its state according to universal deterministic rules. The universe is computed, not evolved continuously. | Core axiom — computational ontology |

**Current axiom count: 6 (AXIM-1 through AXIM-6)** (AXIM-5/ZBW demoted to THEO-1 on 30 March 2026; formerly 7 axioms)

---

## Theorems — Strong Sector (SS)

All from the Strong Sector paper (SS-1). Proved from AXIM-1–AXIM-6 and the 600-cell lattice geometry.

| ID | Theorem | Result | Key postulates used | Paper |
|----|---------|--------|--------------------|----|
| **THEO-SS-1** | SU(3) from tetrahedral hopping | The three colour-charge hopping operators on the K3 base graph generate the su(3) Lie algebra exactly. Gell-Mann matrices reproduced. | AXIM-1, AXIM-2, AXIM-4 | SS-1, Theorem 1 |
| **THEO-SS-2** | Gluon masslessness | Open hDP chain paths cannot acquire a mass gap. Gluons are massless. | AXIM-2, AXIM-3, AXIM-4 | SS-1, Theorem 2 |
| **THEO-SS-3** | β₀ = 7 | The one-loop QCD beta function coefficient β₀ = 7 follows from the Casimir structure of the tetrahedral cage. | AXIM-1, AXIM-2, AXIM-4 | SS-1, Theorem 3 |
| **THEO-SS-4** | α_geom exact | α_geom = 3(11+5√5)√(5+√5)/320 ≈ 0.5594 (exact closed form from 600-cell Voronoi geometry). | AXIM-2 | SS-1, Theorem 4 |
| **THEO-SS-5** | k_SM derived | k_SM = α_geom / (12φ²) ≈ 0.01781. Derived from α_geom and coordination number z=12. | AXIM-2 | SS-1, Theorem 5 |
| **THEO-SS-6** | sea_strength derived | sea_strength = 10 × k_SM ≈ 0.1780. Factor 10 = N_lattice/z = 120/12. | AXIM-2 | SS-1, Theorem 6 |
| **THEO-SS-7** | GMO mass formula | The Gell-Mann–Okubo mass relation for baryons follows from SU(3) representation theory applied to the tetrahedral cage. | AXIM-1, AXIM-2, AXIM-4 | SS-1, Theorem 7 |
| **THEO-SS-8** | Hadron decuplet equal spacing | Equal mass spacing in the baryon decuplet follows from the SU(3) algebra. The Ω⁻ prediction is reproduced. | AXIM-1, AXIM-2 | SS-1, Theorem 8 |
| **THEO-SS-9** | Quark mass strict ordering | m_u < m_d < m_s < m_c < m_b < m_t follows from the cage depth model: each additional shell contributes positive binding energy. | AXIM-1, AXIM-2, AXIM-5 | SS-1, Theorem 9 |

---

## Theorems — Standard Model Emergence (SM)

| ID | Theorem | Result | Key postulates used | Paper |
|----|---------|--------|--------------------|----|
| **THEO-SM-1** | Charge quantisation | δ = 1/3 **exactly**. From C3 cage symmetry (all three base vertices equivalent) and cage completeness (all hDP chains terminate on base vertices): δ₁ = δ₂ = δ₃ and δ₁+δ₂+δ₃ = 1, so δ = 1/3. Corollary: q_up = +2/3 e, q_down = −1/3 e, q_lepton = −e. | AXIM-1, AXIM-2, AXIM-4 | SM-1, Theorem 1 |
| **THEO-SM-2** | Koide ratio | K = 2/3 **exactly**. From the K3 spectral theorem: the eigenvalue ratio λ₊/|λ₋| = 2/1 forces K = 2/3. | AXIM-1, AXIM-2, CORL-1a, AXIM-5 | SM-3, central theorem |
| **THEO-SM-3** | K3 postulates derived | All three postulates of the K3 spectral theorem (AXIM-1: thermal ZBW, AXIM-2: DI-bit visit rate, AXIM-3: DP Sea thermalisation) are derived from CPP axioms AXIM-1–AXIM-6. Zero free postulates remain in SM-3. | AXIM-1–AXIM-6 | SM-3, v5 |
| **THEO-SM-4** | TBM neutrino mixing | U_PMNS⁽⁰⁾ = ⟨K3 vertex | K3 eigenstate⟩ = U_TBM **exactly**. sin²θ₁₂ = 1/3, sin²θ₂₃ = 1/2, sin²θ₁₃ = 0. This is the zeroth-order result; corrections are open (OPEN-P-SM-5). | AXIM-1, AXIM-2, CORL-1a | SM-5 |
| **THEO-SM-5** | θ cannot come from K3+SSV | Any mechanism acting on the tetrahedral cage in 3D or the full 4D 600-cell embedding that respects C3 symmetry cannot select the Koide phase θ in the antibonding subspace. Proved by exhaustion of 11 candidate mechanisms. | AXIM-1, AXIM-2, AXIM-4 | Sessions B,E,F,G — registered in OPEN-P-SM-7d |

---

## Corollaries

| ID | Corollary | Follows from | Paper |
|----|-----------|-------------|-------|
| **CORL-SM-1** | q_up = +2/3 e, q_down = −1/3 e | THEO-SM-1 (δ = 1/3) | SM-1 |
| **CORL-SM-2** | Three lepton generations correspond to three K3 eigenmodes | THEO-SM-2 + K3 structure | SM-3 |
| **CORL-SM-3** | Neutrinos are the K3 eigenmode excitations; charged leptons are the vertex excitations | THEO-SM-4 | SM-5 |
| **CORL-SM-4** | K(c,b,t) ≈ 2/3 (0.42%) — K3 thermal structure shows through for heavy quarks | THEO-SM-2 + cage perturbation theory | PS-1 (thermal session) |

---

## Theorem — Partner-Switching Mechanics (30 March 2026)

| ID | Theorem | Result | Key postulates used | Source |
|----|---------|--------|--------------------|--------|
| **THEO-1** | CP Non-Persistent Co-Occupation | Two CPs cannot persistently occupy the same Grid Point. Same-polarity: repulsive SSV prevents approach. Opposite-polarity: at superimposition, intra-pair SSV direction is undefined; bulk SSV drives opposite displacements on the next Absolute Moment. Superimposition is transient (one Absolute Moment). **The CP Exclusion Postulate is redundant — it is a theorem.** | AXIM-1, AXIM-2, AXIM-4 | CPP-propositions-addendum.md §1 |

---

## Corollaries — Partner-Switching Mechanics (30 March 2026)

| ID | Corollary | Follows from | Source |
|----|-----------|-------------|--------|
| **CORL-1a** | ZBW Turning Point at Grid Point Superimposition — turning point occurs at superimposition, not before; f_ZBW ≈ 1/(2t_P) is derived, not postulated | THEO-1 | CPP-propositions-addendum.md §1 |
| **CORL-1b** | Stochastic Partner Exchange — DP pair identities are not persistent; each CP's next partner is determined by dominant SSV_net at post-superimposition Grid Point | THEO-1, CORL-1a | CPP-propositions-addendum.md §1 |

---

## Propositions — Partner-Switching Mechanics (30 March 2026)

*Full statements in CPP-propositions-addendum.md §2. Abbreviated here.*

| ID | Proposition | Summary | Status |
|----|-------------|---------|--------|
| **PROP-1** | Random Walk and Quantum Position Uncertainty | Central CP random walk over ZBW cycles produces |ψ(x)|² without Born rule postulate | Physically motivated; OPEN-P-QM-new-1 |
| **PROP-2** | Solitonic (Rogue Wave) Tunneling | Constructive superposition of Sea SSV_net vectors produces rare large-amplitude spike displacing central CP across barrier; reproduces WKB exponential | Physically motivated; OPEN-P-QM-new-3 |
| **PROP-3** | Tetrahedral Cage as Unique Minimum Stable Cage | N=4 tetrahedron uniquely satisfies both energetic stability (U < 0) and geometric completeness (T_d cancels all multipole moments); N=12 icosahedron is energetically unbound | Proved (energetic argument in addendum) |
| **PROP-4** | Elastic Tunneling via Cage Dissolution and Reformation | Central −eCP crosses barrier via rogue wave; cage dissolves isotropically (no photon); cage reforms identically from Sea CPs on far side; energy conserved exactly | Physically motivated; OPEN-P-QM-new-3 |
| **PROP-5** | Radial DP Chain Equilibrium Length | Four radial chains reach r_chain ~ d_Sea/√sea_strength, CPP candidate for classical electron radius | Physically motivated; OPEN-P-QM-new-4 |
| **PROP-6** | Relativistic DP Chain Compaction = de Broglie Wavelength | High velocity → SSV_abs → PSR compression → chain compaction → spatial period = λ_dB; wave-particle duality is continuous mechanical compaction | Physically motivated; connects to SR-1 |
| **PROP-7** | Cage Reformation from Partner-Transitioning Sea CPs | Cage +eCPs are transitioning Sea CPs intercepted by new central CP; cage is persistent geometry, not persistent collection of specific CPs | Follows from CORL-1b |
| **PROP-8** | Dual Stable Configurations of Central −eCP | Configuration A (DP enrollment, E ≈ SSV₀/2) vs Configuration B (4-vertex cage, E = 2 SSV₀ = m_e c²); pair creation/annihilation = correlated A↔B transitions | Thermodynamic argument |
| **PROP-9** | Atomic Orbital Probability Density as DP Chain Standing Waves | Three mechanisms: KE polarisation, nuclear SSV landscape, self-reinforcing chain standing waves; nodes/antinodes = orbital nodes/antinodes | Physically motivated; OPEN-P-QM-new-6 |
| **PROP-10** | Electron Identity Transfer and Orbital Born Rule | "The electron" = sequence of Grid Points occupying central cage role via CP identity transfer; |ψ|² = time-average of these positions; Born rule derived from SSV landscape statistics | Follows from CORL-1b |
| **PROP-11** | Virtual Particles and Gauss's Law | VPs are transient Sea configurations without persistent nucleation seed; Gauss's law ensures compensating anti-configuration always present; τ_VP = t_P/p_dissipate; energy-time uncertainty derived | Gauss's law argument |
| **PROP-12** | Critical Separation Distance for Real Pair Production | r_crit = d_Sea/√sea_strength; below r_crit: VP (recombination favoured); above r_crit: real particles (independent cages); r_crit = CPP candidate for Compton wavelength | Physically motivated; OPEN-P-QM-new-7 |
| **PROP-13** | Photon Pair Production via Lorentzian Asymmetry | Nuclear SSV breaks photon chain symmetry; separates +/− CP to r > r_crit; nucleus absorbs recoil; excess energy → KE | Physically motivated; OPEN-P-QM-new-7 |
| **PROP-14** | Mass as Thermodynamic Nucleation-Dissipation Boundary | Rest mass = ground-state organisational energy at r_crit; corollaries: temperature-dependent mass, relativistic mass = chain compaction, second law from DP organisation | Definitional; extends AXIM-5 |
| **PROP-15** | Pair Annihilation: Isentropic vs Non-Isentropic | Low velocity: quasi-static dissolution → two back-to-back photons (isentropic); high velocity: incomplete dissolution → jets + entropy (non-isentropic); testable: ortho:para = 1:1000 from cage dissolution geometry | Physically motivated |

---

## Conjectures (proposed but not yet proved)

| ID | Conjecture | What would prove it | Blocking open problem |
|----|------------|--------------------|-----------------------|
| **CONJ-SM-1** | The 30-vertex shell (d²=2) is the top quark fourth cage | Derive the mass formula using this shell and match PDG | OPEN-P-SS-1 |
| **CONJ-SM-2** | θ_Koide is determined by the electroweak sector | Derive θ from EW cage structure | OPEN-P-SM-7d, EW series |
| **CONJ-SM-3** | Neutrino masses follow from σ = 120^{−d} suppression | Derive Δm² from the 600-cell suppression formula | Paper 6 (planned) |
| **CONJ-SM-4** | m_u/m_e = φ³ exactly | Derive from cage volume ratio or ZBW baseline | OPEN-P-SS-1 |
| **CONJ-SM-5** | TBM corrections arise from Capotauro bias (Capotauro mechanism) | Derive θ₁₃ and 10% corrections from OPEN-P-SM-4 | OPEN-P-SM-4 |

---

## Falsified Conjectures

These were proposed, tested, and found wrong. Recorded to prevent re-testing.

| ID | Falsified conjecture | Why it fails | Session |
|----|---------------------|-------------|---------|
| **FALS-C-SM-1** | C₆₀ (60 vertices) as top quark cage | No 60-vertex distance shell exists in the 600-cell | PS-1, March 2026 |
| **FALS-C-SM-2** | φ^(3(l-1)) quark mass scaling | Actual shell volumes deviate by 3–8× | PS-1, March 2026 |
| **FALS-C-SM-3** | AB loop as origin of θ_Koide | C3 symmetry prevents degeneracy breaking; numerics also fail | Session F |
| **FALS-C-SM-4** | 4D 600-cell embedding breaks C3 for θ | All 600 tetrahedral cells computed; C3 preserved exactly in 4D | Session G (PS-3b) |
| **FALS-C-SM-5** | Self-consistent ZBW mass feedback selects θ | Fixed-point iteration converges to θ = 180° (trivial); not 132.73° | Session L |
| **FALS-C-SM-6** | Löwdin downfolding (K4→K3) breaks antibonding degeneracy | V4 is dark to antibonding modes; ⟨φ₋|v⟩ = 0 exactly | Session E |

---

## Open Problems Cross-Reference

The postulates and theorems connect to the open problems register as follows:

| Theorem | Depends on open problem | Status |
|---------|------------------------|--------|
| THEO-SM-2 (Koide K=2/3) | OPEN-P-SM-7d (θ_Koide) | K=2/3 proved; θ open |
| THEO-SM-4 (TBM mixing) | OPEN-P-SM-4 (Capotauro), OPEN-P-SM-5 (TBM corrections) | Zeroth order proved; corrections open |
| THEO-SS-9 (quark ordering) | OPEN-P-SS-1 (quark mass formula) | Ordering proved; exact values open |

---

## The Minimum Postulate Target

The long-range goal is to derive as many of AXIM-1–AXIM-6 as possible from deeper principles, reducing the postulate count. Current status (30 March 2026):

- **AXIM-1 (Conscious Points):** Foundational — likely irreducible
- **AXIM-2 (600-cell lattice):** Foundational — the core geometric hypothesis of CPP
- **AXIM-3 (Dipole Sea):** Potentially derivable from AXIM-1+AXIM-2 as an equilibrium state
- **AXIM-4 (SSV):** Potentially derivable from AXIM-1+AXIM-2 (SSV as the natural interaction of AXIM-2 geometry)
- **CORL-1a (ZBW) [DEMOTED 30 Mar 2026]:** ✅ Derived from AXIM-2+AXIM-4 as THEO-1 + CORL-1a. Postulate count reduced to 6.
- **AXIM-5 (mass):** Partially extended by PROP-14 (thermodynamic definition); still a core axiom pending derivation from AXIM-3+CORL-1a
- **AXIM-6 (Absolute Moment):** Foundational — the discrete time structure of CPP

**Current axiom count: 6 (AXIM-1 through AXIM-6)** (down from 7; CORL-1a derived 30 March 2026)

If AXIM-3–AXIM-4 and AXIM-5 can be derived from AXIM-1, AXIM-2, and AXIM-6, the postulate count would reduce to 3. This is the long-range theoretical goal.

---

*See also: `open_problems/` register, `potential_solutions.md`, development logs.*  
*Last updated: 26 March 2026*
