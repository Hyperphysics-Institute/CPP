# CPP Postulates and Theorems Registry

**Last updated:** 26 March 2026  
**Purpose:** Source of truth for what CPP assumes (postulates) and what it has proved (theorems). The ratio of theorems to postulates measures theoretical progress. The goal is maximum theorems from minimum postulates.

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
| **P5** | ZBW oscillations | Dipole pairs oscillate at f_ZBW ≈ 1/(2t_Pl). One full cycle = attraction phase + repulsion phase over two Planck times. This oscillation is the source of spin and contributes to mass. | Core axiom — the ZBW mechanism |
| **P6** | Mass as organisational energy | Rest mass is the energy cost of imposing stable order on the Dipole Sea. A particle is a stable configuration of CPs that locally organises the sea against its tendency toward maximum entropy. | Core axiom — ontology of mass |
| **P7** | Absolute Moment | At each Planck time step (Absolute Moment), every CP evaluates its incoming DI-bits and updates its state according to universal deterministic rules. The universe is computed, not evolved continuously. | Core axiom — computational ontology |

**Current postulate count: 7**

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

The long-range goal is to derive as many of P1–P7 as possible from deeper principles, reducing the postulate count. Current status:

- **P1 (Conscious Points):** Foundational — likely irreducible
- **P2 (600-cell lattice):** Foundational — the core geometric hypothesis of CPP
- **P3 (Dipole Sea):** Potentially derivable from P1+P2 as an equilibrium state
- **P4 (SSV):** Potentially derivable from P1+P2 (SSV as the natural interaction of P2 geometry)
- **P5 (ZBW):** Potentially derivable from P3+P4 (ZBW as the natural oscillation of the Dipole Sea in the SSV field)
- **P6 (mass):** Potentially derivable from P3+P5 (mass as the ZBW energy above the sea baseline)
- **P7 (Absolute Moment):** Foundational — the discrete time structure of CPP

If P3–P6 can be derived from P1, P2, P4, and P7, the postulate count reduces to 4.
This is a long-range theoretical goal, not a current research priority.

---

*See also: `open_problems/` register, `potential_solutions.md`, development logs.*  
*Last updated: 26 March 2026*
