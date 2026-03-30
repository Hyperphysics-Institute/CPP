# CPP Postulates and Theorems Registry

**Last updated:** 30 March 2026
**Purpose:** Source of truth for what CPP assumes (postulates) and what it has proved (theorems). The ratio of theorems to postulates measures theoretical progress. The goal is maximum theorems from minimum postulates.

*30 March 2026 update: P5 (ZBW oscillations) demoted from postulate to theorem (T-CPP-1 + C-CPP-1a). Postulate count reduced from 7 to 6. Propositions P-CPP-1 through P-CPP-15, Theorem T-CPP-1, Corollaries C-CPP-1a/1b, and Open Problems OP-QM-new-1 through OP-QM-new-8 added from partner-switching session. See propositions.md for full derivations.*

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
| **P1** | Conscious Points | Conscious Points (CPs) exist as the fundamental information-processing units of reality. Each CP has: polarity (+/−), type (eCP or qCP), a position on the 600-cell lattice, and the capacity to emit and receive DI-bits according to universal rules. | Core axiom |
| **P2** | 600-cell lattice | Space consists of a tiling of 600-cell polytopes. The 120 vertices of each cell are the only allowed CP positions. CPs move by hopping between vertices. There is no continuous space between vertices. | Core axiom — discreteness of space |
| **P3** | Dipole Sea | All of space is filled with randomly oscillating dipole pairs (DPs). The sea maximises entropy by default. Particles are stable departures from this randomness. | Core axiom — the vacuum |
| **P4** | SSV interaction | CPs generate a Space Stress Vector field that falls off as 1/r². Opposite polarities attract; like polarities repel. The SSV is the unified source of all four fundamental forces in different limits. | Core axiom — the force law |
| **P5** | ZBW oscillations | **[DEMOTED TO THEOREM — 30 March 2026]** The ZBW oscillation of bound DP pairs is a derived consequence of the SSV force law (P4) on a discrete lattice (P2). Opposite-polarity CPs approach under monotonically increasing SSV_net attraction to superimposition; at superimposition, intra-pair SSV direction vanishes; bulk SSV drives opposite displacements. Period ≈ 2t_P → f_ZBW ≈ 1/(2t_P) as a theorem. See T-CPP-1 and C-CPP-1a. | Demoted — derivable from P2+P4 |
| **P6** | Mass as organisational energy | Rest mass is the energy cost of imposing stable order on the Dipole Sea. A particle is a stable configuration of CPs that locally organises the sea against its tendency toward maximum entropy. | Core axiom — ontology of mass |
| **P7** | Absolute Moment | At each Planck time step (Absolute Moment), every CP evaluates its incoming DI-bits and updates its state according to universal deterministic rules. The universe is computed, not evolved continuously. | Core axiom — computational ontology |

**Current postulate count: 6** (P5 demoted to theorem 30 March 2026; was 7)

---

## Theorems — Strong Sector (SS)

All from the Strong Sector paper (SS-1). Proved from P1–P7 and the 600-cell lattice geometry.

| ID | Theorem | Result | Key postulates used | Paper |
|----|---------|--------|--------------------|----|
| **SS-T1** | SU(3) from tetrahedral hopping | The three colour-charge hopping operators on the K3 base graph generate the su(3) Lie algebra exactly. Gell-Mann matrices reproduced. | P1, P2, P4 | SS-1, Theorem 1 |
| **SS-T2** | Gluon masslessness | Open hDP chain paths cannot acquire a mass gap. Gluons are massless. | P2, P3, P4 | SS-1, Theorem 2 |
| **SS-T3** | β₀ = 7 | The one-loop QCD beta function coefficient β₀ = 7 follows from the Casimir structure of the tetrahedral cage. | P1, P2, P4 | SS-1, Theorem 3 |
| **SS-T4** | α_geom exact | α_geom = 3(11+5√5)√(5+√5)/320 ≈ 0.5594 (exact closed form from 600-cell Voronoi geometry). | P2 | SS-1, Theorem 4 |
| **SS-T5** | k_SM derived | k_SM = α_geom / (12φ²) ≈ 0.01781. Derived from α_geom and coordination number z=12. | P2 | SS-1, Theorem 5 |
| **SS-T6** | sea_strength derived | sea_strength = 10 × k_SM ≈ 0.1780. Factor 10 = N_lattice/z = 120/12. | P2 | SS-1, Theorem 6 |
| **SS-T7** | GMO mass formula | The Gell-Mann–Okubo mass relation for baryons follows from SU(3) representation theory applied to the tetrahedral cage. | P1, P2, P4 | SS-1, Theorem 7 |
| **SS-T8** | Hadron decuplet equal spacing | Equal mass spacing in the baryon decuplet follows from the SU(3) algebra. The Ω⁻ prediction is reproduced. | P1, P2 | SS-1, Theorem 8 |
| **SS-T9** | Quark mass strict ordering | m_u < m_d < m_s < m_c < m_b < m_t follows from the cage depth model: each additional shell contributes positive binding energy. | P1, P2, P6 | SS-1, Theorem 9 |

---

## Theorems — Standard Model Emergence (SM)

| ID | Theorem | Result | Key postulates used | Paper |
|----|---------|--------|--------------------|----|
| **SM-T1** | Charge quantisation | δ = 1/3 **exactly**. From C3 cage symmetry (all three base vertices equivalent) and cage completeness (all hDP chains terminate on base vertices): δ₁ = δ₂ = δ₃ and δ₁+δ₂+δ₃ = 1, so δ = 1/3. Corollary: q_up = +2/3 e, q_down = −1/3 e, q_lepton = −e. | P1, P2, P4 | SM-1, Theorem 1 |
| **SM-T2** | Koide ratio | K = 2/3 **exactly**. From the K3 spectral theorem: the eigenvalue ratio λ₊/|λ₋| = 2/1 forces K = 2/3. | P1, P2, P5, P6 | SM-3, central theorem |
| **SM-T3** | K3 postulates derived | All three postulates of the K3 spectral theorem (P1: thermal ZBW, P2: DI-bit visit rate, P3: DP Sea thermalisation) are derived from CPP axioms P1–P7. Zero free postulates remain in SM-3. | P1–P7 | SM-3, v5 |
| **SM-T4** | TBM neutrino mixing | U_PMNS⁽⁰⁾ = ⟨K3 vertex | K3 eigenstate⟩ = U_TBM **exactly**. sin²θ₁₂ = 1/3, sin²θ₂₃ = 1/2, sin²θ₁₃ = 0. This is the zeroth-order result; corrections are open (SM-C1). | P1, P2, P5 | SM-5 |
| **SM-T5** | θ cannot come from K3+SSV | Any mechanism acting on the tetrahedral cage in 3D or the full 4D 600-cell embedding that respects C3 symmetry cannot select the Koide phase θ in the antibonding subspace. Proved by exhaustion of 11 candidate mechanisms. | P1, P2, P4 | Sessions B,E,F,G — registered in OP-SM-7d |

---

## Corollaries

| ID | Corollary | Follows from | Paper |
|----|-----------|-------------|-------|
| **SM-C1** | q_up = +2/3 e, q_down = −1/3 e | SM-T1 (δ = 1/3) | SM-1 |
| **SM-C2** | Three lepton generations correspond to three K3 eigenmodes | SM-T2 + K3 structure | SM-3 |
| **SM-C3** | Neutrinos are the K3 eigenmode excitations; charged leptons are the vertex excitations | SM-T4 | SM-5 |
| **SM-C4** | K(c,b,t) ≈ 2/3 (0.42%) — K3 thermal structure shows through for heavy quarks | SM-T2 + cage perturbation theory | PS-1 (thermal session) |

---

## Theorem — Partner-Switching Mechanics (30 March 2026)

| ID | Theorem | Result | Key postulates used | Source |
|----|---------|--------|--------------------|--------|
| **T-CPP-1** | CP Non-Persistent Co-Occupation | Two CPs cannot persistently occupy the same Grid Point. Same-polarity: repulsive SSV prevents approach. Opposite-polarity: at superimposition, intra-pair SSV direction is undefined; bulk SSV drives opposite displacements on the next Absolute Moment. Superimposition is transient (one Absolute Moment). **The CP Exclusion Postulate is redundant — it is a theorem.** | P1, P2, P4 | propositions.md §1 |

---

## Corollaries — Partner-Switching Mechanics (30 March 2026)

| ID | Corollary | Follows from | Source |
|----|-----------|-------------|--------|
| **C-CPP-1a** | ZBW Turning Point at Grid Point Superimposition — turning point occurs at superimposition, not before; f_ZBW ≈ 1/(2t_P) is derived, not postulated | T-CPP-1 | propositions.md §1 |
| **C-CPP-1b** | Stochastic Partner Exchange — DP pair identities are not persistent; each CP's next partner is determined by dominant SSV_net at post-superimposition Grid Point | T-CPP-1, C-CPP-1a | propositions.md §1 |

---

## Propositions — Partner-Switching Mechanics (30 March 2026)

*Full statements in propositions.md §2. Abbreviated here.*

| ID | Proposition | Summary | Status |
|----|-------------|---------|--------|
| **P-CPP-1** | Random Walk and Quantum Position Uncertainty | Central CP random walk over ZBW cycles produces |ψ(x)|² without Born rule postulate | Physically motivated; OP-QM-new-1 |
| **P-CPP-2** | Solitonic (Rogue Wave) Tunneling | Constructive superposition of Sea SSV_net vectors produces rare large-amplitude spike displacing central CP across barrier; reproduces WKB exponential | Physically motivated; OP-QM-new-3 |
| **P-CPP-3** | Tetrahedral Cage as Unique Minimum Stable Cage | N=4 tetrahedron uniquely satisfies both energetic stability (U < 0) and geometric completeness (T_d cancels all multipole moments); N=12 icosahedron is energetically unbound | Proved (energetic argument in addendum) |
| **P-CPP-4** | Elastic Tunneling via Cage Dissolution and Reformation | Central −eCP crosses barrier via rogue wave; cage dissolves isotropically (no photon); cage reforms identically from Sea CPs on far side; energy conserved exactly | Physically motivated; OP-QM-new-3 |
| **P-CPP-5** | Radial DP Chain Equilibrium Length | Four radial chains reach r_chain ~ d_Sea/√sea_strength, CPP candidate for classical electron radius | Physically motivated; OP-QM-new-4 |
| **P-CPP-6** | Relativistic DP Chain Compaction = de Broglie Wavelength | High velocity → SSV_abs → PSR compression → chain compaction → spatial period = λ_dB; wave-particle duality is continuous mechanical compaction | Physically motivated; connects to SR-1 |
| **P-CPP-7** | Cage Reformation from Partner-Transitioning Sea CPs | Cage +eCPs are transitioning Sea CPs intercepted by new central CP; cage is persistent geometry, not persistent collection of specific CPs | Follows from C-CPP-1b |
| **P-CPP-8** | Dual Stable Configurations of Central −eCP | Configuration A (DP enrollment, E ≈ SSV₀/2) vs Configuration B (4-vertex cage, E = 2 SSV₀ = m_e c²); pair creation/annihilation = correlated A↔B transitions | Thermodynamic argument |
| **P-CPP-9** | Atomic Orbital Probability Density as DP Chain Standing Waves | Three mechanisms: KE polarisation, nuclear SSV landscape, self-reinforcing chain standing waves; nodes/antinodes = orbital nodes/antinodes | Physically motivated; OP-QM-new-6 |
| **P-CPP-10** | Electron Identity Transfer and Orbital Born Rule | "The electron" = sequence of Grid Points occupying central cage role via CP identity transfer; |ψ|² = time-average of these positions; Born rule derived from SSV landscape statistics | Follows from C-CPP-1b |
| **P-CPP-11** | Virtual Particles and Gauss's Law | VPs are transient Sea configurations without persistent nucleation seed; Gauss's law ensures compensating anti-configuration always present; τ_VP = t_P/p_dissipate; energy-time uncertainty derived | Gauss's law argument |
| **P-CPP-12** | Critical Separation Distance for Real Pair Production | r_crit = d_Sea/√sea_strength; below r_crit: VP (recombination favoured); above r_crit: real particles (independent cages); r_crit = CPP candidate for Compton wavelength | Physically motivated; OP-QM-new-7 |
| **P-CPP-13** | Photon Pair Production via Lorentzian Asymmetry | Nuclear SSV breaks photon chain symmetry; separates +/− CP to r > r_crit; nucleus absorbs recoil; excess energy → KE | Physically motivated; OP-QM-new-7 |
| **P-CPP-14** | Mass as Thermodynamic Nucleation-Dissipation Boundary | Rest mass = ground-state organisational energy at r_crit; corollaries: temperature-dependent mass, relativistic mass = chain compaction, second law from DP organisation | Definitional; extends P6 |
| **P-CPP-15** | Pair Annihilation: Isentropic vs Non-Isentropic | Low velocity: quasi-static dissolution → two back-to-back photons (isentropic); high velocity: incomplete dissolution → jets + entropy (non-isentropic); testable: ortho:para = 1:1000 from cage dissolution geometry | Physically motivated |

---

## Conjectures (proposed but not yet proved)

| ID | Conjecture | What would prove it | Blocking open problem |
|----|------------|--------------------|-----------------------|
| **SM-CJ1** | The 30-vertex shell (d²=2) is the top quark fourth cage | Derive the mass formula using this shell and match PDG | OP-SS-1 |
| **SM-CJ2** | θ_Koide is determined by the electroweak sector | Derive θ from EW cage structure | OP-SM-7d, EW series |
| **SM-CJ3** | Neutrino masses follow from σ = 120^{−d} suppression | Derive Δm² from the 600-cell suppression formula | Paper 6 (planned) |
| **SM-CJ4** | m_u/m_e = φ³ exactly | Derive from cage volume ratio or ZBW baseline | OP-SS-1 |
| **SM-CJ5** | TBM corrections arise from Capotauro bias (Capotauro mechanism) | Derive θ₁₃ and 10% corrections from OP-SM-4 | OP-SM-4 |

---

## Falsified Conjectures

These were proposed, tested, and found wrong. Recorded to prevent re-testing.

| ID | Falsified conjecture | Why it fails | Session |
|----|---------------------|-------------|---------|
| **SM-FC1** | C₆₀ (60 vertices) as top quark cage | No 60-vertex distance shell exists in the 600-cell | PS-1, March 2026 |
| **SM-FC2** | φ^(3(l-1)) quark mass scaling | Actual shell volumes deviate by 3–8× | PS-1, March 2026 |
| **SM-FC3** | AB loop as origin of θ_Koide | C3 symmetry prevents degeneracy breaking; numerics also fail | Session F |
| **SM-FC4** | 4D 600-cell embedding breaks C3 for θ | All 600 tetrahedral cells computed; C3 preserved exactly in 4D | Session G (PS-3b) |
| **SM-FC5** | Self-consistent ZBW mass feedback selects θ | Fixed-point iteration converges to θ = 180° (trivial); not 132.73° | Session L |
| **SM-FC6** | Löwdin downfolding (K4→K3) breaks antibonding degeneracy | V4 is dark to antibonding modes; ⟨φ₋|v⟩ = 0 exactly | Session E |

---

## Open Problems Cross-Reference

The postulates and theorems connect to the open problems register as follows:

| Theorem | Depends on open problem | Status |
|---------|------------------------|--------|
| SM-T2 (Koide K=2/3) | OP-SM-7d (θ_Koide) | K=2/3 proved; θ open |
| SM-T4 (TBM mixing) | OP-SM-4 (Capotauro), OP-SM-5 (TBM corrections) | Zeroth order proved; corrections open |
| SS-T9 (quark ordering) | OP-SS-1 (quark mass formula) | Ordering proved; exact values open |

---

## The Minimum Postulate Target

The long-range goal is to derive as many of P1–P7 as possible from deeper principles, reducing the postulate count. Current status (30 March 2026):

- **P1 (Conscious Points):** Foundational — likely irreducible
- **P2 (600-cell lattice):** Foundational — the core geometric hypothesis of CPP
- **P3 (Dipole Sea):** Potentially derivable from P1+P2 as an equilibrium state
- **P4 (SSV):** Potentially derivable from P1+P2 (SSV as the natural interaction of P2 geometry)
- **P5 (ZBW) [DEMOTED 30 Mar 2026]:** ✅ Derived from P2+P4 as T-CPP-1 + C-CPP-1a. Postulate count reduced to 6.
- **P6 (mass):** Partially extended by P-CPP-14 (thermodynamic definition); still a core axiom pending derivation from P3+P5
- **P7 (Absolute Moment):** Foundational — the discrete time structure of CPP

**Current postulate count: 6** (down from 7; P5 derived 30 March 2026)

If P3–P4 and P6 can be derived from P1, P2, and P7, the postulate count would reduce to 3. This is the long-range theoretical goal.

---

*See also: `open_problems/` register, `potential_solutions.md`, development logs.*  
*Last updated: 26 March 2026*
