# CPP Theory Overview — Current State

**Location:** `/CPP/theory-overview.md`
**Purpose:** Snapshot of all CPP results, open problems, and next targets. Read at the start of each session.
**Last updated:** 3 April 2026 (after SM-7 registration)

---

## The Theory in One Paragraph

Conscious Point Physics derives the Standard Model from the 600-cell polytope (120 vertices, 720 edges, 1200 faces, 600 cells, coordination z=12). All gauge couplings are mode fractions of the lattice weighted by η = 1/φ. All fermion masses follow from the K₃ eigenvalue structure (bonding eigenvalue +2, antibonding −1) perturbed by isotropic gauge shifts. The theory has 10 axioms, 2 calibration constants (m_e, m_c), and 0 shape parameters. It predicts 9 independent quantitative results and 6 qualitative QM results.

---

## Registered Papers (9 on OSF)

| ID | Title | Key Result | Version |
|----|-------|------------|---------|
| SS-1 | Strong Sector from 600-Cell | SU(3) exact; β₀ = 7; 9 theorems | v2 |
| SM-1 | Binding Mechanisms and Cage Stability | Tetrahedral cage; δ = 1/3; SSV₀ | v6 |
| SM-2 | Mass Generation from Geometric Hierarchies | Semi-empirical framework; k ≈ 0.0185 | v30 |
| SM-3 | K3 Spectral Theorem and Koide Formula | K = 2/3 exact from K₃ eigenvalues | v5 |
| SM-4 | Charged Lepton Masses from K3 | 11 ppm; θ cannot come from K3+SSV alone | v5 |
| SM-5 | Tribimaximal Neutrino Mixing | U_PMNS = U_TBM from K₃ eigenvectors | v1 |
| SR-1 | Mechanistic Derivation of Relativistic Effects | Lorentz factor from Voronoi compression; k derived | v18 |
| SM-6 | Charged Lepton Mass Spectrum | sin²θ_W = 3/(8φ); Koide phase derived; μ 0.18%, τ 0.15% | v3 |
| SM-7 | Heavy Quark Mass Spectrum + Strong Coupling | α_s = 5/(8φ); quark Koide phase; m_b 1.4%, m_t 1.7% | v2.2 |

---

## Strongest Quantitative Results

| Result | Formula | Predicted | PDG | Error | Params | Paper |
|--------|---------|-----------|-----|-------|--------|-------|
| Koide ratio | K₃ eigenvalue ratio | 2/3 | 0.6667 | 11 ppm | 0 | SM-3 |
| Weinberg angle | 3/(8φ) | 0.2318 | 0.2312 | 0.24% | 0 | SM-6 |
| Lepton Koide phase | -(2/3)(1+3/(104φ)) | 132.731° | 132.732° | 0.003% | 0 | SM-6 |
| Muon mass | Koide + m_e calibration | 105.47 MeV | 105.66 | 0.18% | 0 shape | SM-6 |
| Tau mass | Koide + m_e calibration | 1774.1 MeV | 1776.9 | 0.15% | 0 shape | SM-6 |
| Strong coupling | 5/(8φ) | 0.386 | ~0.38 | ~1% | 0 | SM-7 |
| Coupling ratio | F/E | 5/3 | — | topological | 0 | SM-7 |
| Coupling sum | 3/(8φ)+5/(8φ) | 1/φ | — | exact | 0 | SM-7 |
| Quark Koide phase | -(2/3)(1-27/(104φ)) | 124.035° | 124.094° | 0.048% | 0 | SM-7 |
| Bottom mass | Koide + m_c calibration | 4.24 GeV | 4.18 | 1.4% | 0 shape | SM-7 |
| Top mass | Koide + m_c calibration | 169.8 GeV | 172.7 | 1.7% | 0 shape | SM-7 |

**Net scorecard:** 9 independent predictions from 10 axioms and 2 calibrations. SM requires 8 parameters for the same quantities.

---

## The 10 Axioms (from axiom-registry.md)

| ID | Name | Statement (short) |
|----|------|--------------------|
| A1 | CP existence | Conscious Points with polarity and position |
| A2 | 600-cell topology | CPs on 600-cell lattice (V=120, E=720, F=1200, z=12) |
| A3 | DI-bit propagation | Complex amplitudes propagate at c = l_P/t_P |
| A4 | Nexus | Global consistency constraint at each Absolute Moment |
| A5 | Propagation efficiency | η = l_edge/R_circ = 1/φ |
| A6 | Edge Abelianity | Edge transport is 1D, reversible, commutative → U(1) |
| A7 | Face-Bond Circulation | Displacement pulses circulate on K₃ loops, non-commutative → SU(3) |
| A8 | Edge locality | Edge modes couple to internal K₃ bonds only (2 bonds) |
| A9 | Face saturation | Face modes couple to all z incident bonds (12 bonds) |
| A10 | Colour attraction | Colour self-energy is negative (attractive binding) |

**Potential reductions:** A5→A2, A6+A7→A6' (Walk-Dimension Gauge Principle), A8+A9→A8' (minimal coupling), A10→A2+A7. If all succeed: 10→6 axioms.

---

## Key Formulas (reference card)

```
sin²θ_W = η × Tr(A²)/N = (1/φ)(1440/3840) = 3/(8φ) ≈ 0.2318
α_s     = η × [Tr(A³)/3]/N = (1/φ)(2400/3840) = 5/(8φ) ≈ 0.3863

α_s/sin²θ_W = F/E = 1200/720 = 5/3
sin²θ_W + α_s = 1/φ ≈ 0.618

ε_lepton = +2sin²θ_W/(z+1) = +3/(52φ) ≈ +0.0357
ε_quark  = (2sin²θ_W - 12α_s)/(z+1) = -27/(52φ) ≈ -0.3209

cos θ_lepton = -(2/3)(1 + 3/(104φ))     → θ = 132.731°
cos θ_quark  = -(2/3)(1 - 27/(104φ))    → θ = 124.035°

K = λ₊/(λ₊ + |λ₋|) = 2/(2+1) = 2/3     [K₃ eigenvalues: +2, -1, -1]

N = Tr(A²) + Tr(A³)/3 = 1440 + 2400 = 3840
φ = (1+√5)/2 ≈ 1.6180, z = 12, z+1 = 13
```

---

## Derivation Chains

### SM-6 (Leptons): 600-cell → K₃ → K=2/3 → traces → 3/8 → η=1/φ → sin²θ_W=3/(8φ) → ε=3/(52φ) → θ=132.73° → masses

### SM-7 (Quarks): Same chain + α_s=5/(8φ) from face modes + 12-bond colour coupling → ε=-27/(52φ) → θ=124.04° → masses

### SS-1 (Strong): K₃ face permutations → 8 Gell-Mann generators → SU(3) exact → β₀=7

### QM-1→6: DI-bit hopping → Schrödinger → Born rule → Bell S=2√2 → Lindblad → QFT → 3 generations

---

## Physical Mechanisms (from founders_vision.md)

### Electric interaction (edge modes)
Push-pull, attract/repel, linear, reversible. Single qDP bond with one degree of freedom. Composition commutes. U(1).

### Colour interaction (face-bond circulation)
Displacement pulses circulate on closed triangular K₃ loops. 8 standing-wave patterns = 8 Gell-Mann generators. Non-commutative because each pulse changes the vertex SSV_abs. Energy trapped in loop = confinement. SU(3).

### Isotropic shift mechanism
Uniform perturbation ε·I₃ on K₃ preserves C₃ symmetry (eigenvectors unchanged) but shifts the eigenvalue RATIO because {+2,−1,−1} is asymmetric. This changes the Koide phase without breaking the triangle symmetry.

### Walk-Dimension Gauge Principle
1D edge walks commute (Abelian). 2D face loops don't commute in a Lorentzian lattice (non-Abelian). Walk dimensionality determines gauge group.

---

## Open Problems (Top Priority)

| ID | Problem | Status |
|----|---------|--------|
| OPEN-P-SM-7-1 | Running of α_s from 0.386 to α_s(M_Z)=0.118 | Connection to SS-1 β₀=7 needed |
| OPEN-P-SM-7-2 | Rigorous proof of face saturation from Green's function | Projector lemma provides framework |
| OPEN-P-SM-7-3 | Mode-fraction coupling vs perturbative gauge coupling | Operational vs dynamical definition |
| OPEN-P-SM-7-4 | CPP-natural mass scheme for quarks | Candidate: MS-bar at μ=m_q |
| OPEN-P-SM-7-5 | Length-4 cell modes — Higgs? Gravity? | Unexplored |
| — | Light quark masses (u,d,s) | Chiral condensate dominates; new axiom likely needed |
| — | W/Z/Higgs boson masses | EW series has structural models; need quantification |
| — | Neutrino mass values | SM-5 gives mixing matrix; mass ratios open |
| — | Electron g-2 precision | Exploratory material in archive |

---

## Series Status

| Series | Papers | Compliance | PDFs | Doc suite | README | Keywords |
|--------|--------|-----------|------|-----------|--------|----------|
| SM (1-7) | 7 | ✅ | ✅ | ✅ | ✅ | ✅ |
| EW (1-5) | 5 | ✅ | ✅ | ✅ | ✅ | ✅ |
| QM (1-6) | 6 | ✅ | ✅ | ✅ | ✅ | ✅ |
| SR-1 | 1 | ✅ | ✅ | ✅ | ✅ | ✅ |
| SS-1 | 1 | ✅ | ✅ | ✅ | ✅ | ✅ |
| SD (1-5) | 5 | ✅ | ✅ | ✅ | ✅ | ✅ |

**All 25 papers are formatting-compliant with compiled PDFs and complete documentation suites.**

---

## Pending Tasks (not urgent)

- [ ] Curate SM-7 development transcripts (8 files)
- [ ] Generate SM-7 verification notebook
- [ ] Regenerate site-wide cpp_references.bib from all local .bib files
- [ ] Update top-level README.md with SM-7 in tables
- [ ] Fill remaining sections of founders_vision.md (13 of 16 sections empty)

---

*This document is updated after each paper production cycle. It is the AI's primary orientation document for new sessions.*
