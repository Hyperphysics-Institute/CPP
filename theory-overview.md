# CPP Theory Overview — Current State

**Location:** `/CPP/theory-overview.md`
**Purpose:** Snapshot of all CPP results, open problems, and next targets. Read at the start of each session.
**Last updated:** 17 April 2026 (after SS-5 v0.2)

---

## The Theory in One Paragraph

Conscious Point Physics derives the Standard Model from the 600-cell polytope (120 vertices, 720 edges, 1200 faces, 600 cells, coordination z=12). All gauge couplings are mode fractions of the lattice weighted by η = 1/φ. All fermion masses follow from the K₃ eigenvalue structure (bonding eigenvalue +2, antibonding −1) perturbed by isotropic gauge shifts, and from the zero-parameter cage mass formula M = m_e(z/φ)V^(7/3). The theory has 9 axioms (7 core + A8' + A11), 2 calibration constants (m_e, m_c), and 0 shape parameters. It predicts 24+ independent quantitative results and 6 qualitative QM results.

---

## Registered Papers (13 on OSF or pending)

| ID | Title | Key Result | Version |
|----|-------|------------|---------|
| SS-1 | Strong Sector from 600-Cell | SU(3) exact; β₀ = 7; 9 theorems | v2 |
| SM-1 | Binding Mechanisms and Cage Stability | Tetrahedral cage; δ = 1/3; SSV₀ | v6 |
| SM-2 | Mass Generation from Geometric Hierarchies | Semi-empirical framework; k ≈ 0.0185 | v30 |
| SM-3 | K3 Spectral Theorem and Koide Formula | K = 2/3 exact from K₃ eigenvalues (conditional on Layer B) | v6 |
| SM-4 | Charged Lepton Masses from K3 | 11 ppm; θ cannot come from K3+SSV alone | v5 |
| SM-5 | Tribimaximal Neutrino Mixing | U_PMNS = U_TBM from K₃ eigenvectors | v1 |
| SR-1 | Mechanistic Derivation of Relativistic Effects | Lorentz factor from Voronoi compression; k derived | v18 |
| SM-6 | Charged Lepton Mass Spectrum | sin²θ_W = 3/(8φ); Koide phase derived; μ 0.18%, τ 0.15% | v3 |
| SM-7 | Heavy Quark Mass Spectrum + Strong Coupling | α_s = 5/(8φ); quark Koide phase; m_b 1.4%, m_t 1.7% | v2.2 |
| SM-8 | Quark Generation Structure from 600-Cell Distance Shells | Zero-param quark masses; 3-generation theorem; RMS 2.1% | v4.1 |
| SM-9 | The Quark Mass Scaling Exponent | V^(7/3) derivation; Symmetry Degeneracy Theorem | v2.2 |
| SM-10 | First-Principles Quark Mass from FEM Chain Network | Cascade mechanism; two-regime physics; organised DP density | v0.1 |
| SS-2 | Lattice-Scale Grounding and Nucleon Structure | l_unit = 0.589 fm; r_proton = 0.883 fm (+5%, 0 params) | v1.0 |
| SS-3 | Uniqueness of SU(3) from Tetrahedral Cage | SU(3) unique; 4+4 physical mode basis; det(M) = 2/√3 | v1.3 |
| SS-4 | String Tension from 600-Cell Face-Mode Multiplicity | σ = M₀z²/(φ l_edge) = 926.5 MeV/fm (+1.8% vs Cornell) | v0.1 |
| SS-5 | Light-Nuclei Binding Energies from Open-Vertex Cascade | $B_d, B_{^3H}, B_{^3He}, B_{^4He}$ all $\leq 5.3\%$ zero-param; $^5$He/$^5$Li/$^8$Be unbound ✓ | v0.2 |

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
| m_s (zero-param) | m_e(z/φ)V^(7/3) | 96.3 MeV | 93.4 | +3.1% | 0 | SM-8 |
| m_c (zero-param) | m_e(z/φ)V^(7/3) | 1,249 MeV | 1,270 | −1.6% | 0 | SM-8 |
| m_b (zero-param) | m_e(z/φ)V^(7/3) | 4,115 MeV | 4,180 | −1.6% | 0 | SM-8 |
| m_t (zero-param) | m_e(z/φ)V^(7/3)×16 | 169,571 MeV | 172,760 | −1.8% | 0 | SM-8 |
| r_proton | Distorted tet + ZBW smearing | 0.883 fm | 0.841 | +5.0% | 0 | SS-2 |
| μ_proton | Constituent quark model | 2.789 μ_N | 2.793 | −0.1% | 0 | SS-2 |
| α_s(m_H) | Running from α_geom=1/√5 | 0.1132 | 0.1130 | +0.2% | 0 | SS-2 |
| σ (string tension) | M₀z²/(φ l_edge) | 926.5 MeV/fm | ~910 | +1.8% | 0 | SS-4 |
| B_d (deuteron binding) | M₀/φ cascade A=2 | 2.342 MeV | 2.22457 | +5.3% | 0 | SS-5 |
| B(³H) (triton) | Cascade A=3, 0 Coul, 1 Pauli | 8.474 MeV | 8.482 | −0.09% | 0 | SS-5 |
| B(³He) | Cascade A=3, 1 Coul, 1 Pauli | 7.642 MeV | 7.718 | −1.0% | 0 | SS-5 |
| B(⁴He) | Cascade A=4, 1 Coul, 2 Pauli, +closure | 27.90 MeV | 28.30 | −1.4% | 0 | SS-5 |
| ⁵He, ⁵Li, ⁸Be unbound | Closed-polytope gap A=5,8 | Unbound | Unbound ✓ | qual. exact | 0 | SS-5 |
| Diproton / dineutron unbound | K₃ charge-misalignment | Unbound | Unbound | exact (qual.) | 0 | SS-5 |

**Net scorecard:** 24+ independent predictions from 9 axioms and 2 calibrations. SM requires 19+ parameters for the same quantities.

---

## The Axiom Set (Post–SS-3)

| ID | Name | Statement (short) |
|----|------|--------------------|
| A1 | CP existence | Conscious Points with polarity and position |
| A2 | 600-cell topology | CPs on 600-cell lattice (V=120, E=720, F=1200, z=12) |
| A3 | DI-bit propagation | Complex amplitudes propagate at c = l_P/t_P |
| A4 | Nexus | Global consistency constraint at each Absolute Moment |
| A5 | Propagation efficiency | η = l_edge/R_circ = 1/φ |
| A6' | Walk-Dimension Gauge Principle | Walk dimensionality determines gauge structure; z=12 post-gap multiplier |
| A10 | Colour attraction | Colour self-energy is negative (attractive binding) |
| A8' | Cage-Volume Scaling | M ∝ m_e(z/φ)V^(7/3); pair counting × cage dimension |
| A11 | Lattice-Scale Grounding | l_unit = ℏc/Λ_QCD = 0.589 fm from α_geom = 1/√5 running |

**Potential reductions:** A5→A2, A10→A2+A6'. If both succeed: 9→7 axioms.

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

Zero-Parameter Quark Mass Formula (SM-8 v4.1 / SM-9 v2.2):
  M_q = m_e (z/φ) V^(7/3)              q = s, c, b
  M_t = m_e (z/φ) V_t^(7/3) × z·C_F   q = t
  M₀ = m_e z/φ = 3.790 MeV, V ∈ {4, 12, 20, 30}
  z × C_F = 16 (post-gap multiplier), RMS = 2.1%

Lattice-Scale Grounding (SS-2):
  l_unit = ℏc/Λ_QCD = 0.589 fm
  σ = M₀zπ/(φ l_edge) = 243 MeV/fm [CONJ]
  r_p = 0.883 fm (distorted tet + ZBW, ε = 1.94)

SU(3) Uniqueness (SS-3):
  dim(traceless Hermitian 3×3) = 8 = dim(su(3))
  Gell-Mann orthogonality: Tr(λ^a λ^b) = 2δ^{ab} → analytic independence
  Physical basis: 4 linear bond modes + 4 junction modes = 8
  Change-of-basis: det(M) = 2/√3; T³ = ½(L₂−L₄); T⁸ = (√3/2)(L₂+L₄)
  OPEN-SS-11 → THEO-SS-10
```

---

## Derivation Chains

### SM-6 (Leptons): 600-cell → K₃ → K=2/3 → traces → 3/8 → η=1/φ → sin²θ_W=3/(8φ) → ε=3/(52φ) → θ=132.73° → masses

### SM-7 (Quarks): Same chain + α_s=5/(8φ) from face modes + 12-bond colour coupling → ε=-27/(52φ) → θ=124.04° → masses

### SS-1 (Strong): K₃ face permutations → 8 Gell-Mann generators → SU(3) exact → β₀=7
### SS-3 (Strong): SU(3) is the UNIQUE algebra of 3 colour vertices (THEO-SS-10). 4+4 physical mode basis identified.

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
| OPEN-P-SM-cage-1 | Rigorous derivation of α = 7/3 from cage geometry | PARTIALLY RESOLVED — SM-9 pair decomposition; FEM (SM-10) pending |
| OPEN-P-SM-10-FEM | First-principles quark mass from FEM chain network simulation | IN PROGRESS — Phase 1-2 (CPU) complete; Phase 3 (GPU) pending. **#1 priority** |
| OPEN-P-SD-lattice-scale | Lattice spacing and physical scale | PARTIALLY RESOLVED — SS-2: l_unit = 0.589 fm; σ derivation open |
| OPEN-P-SM-7-1 | Running of α_s from 0.386 to α_s(M_Z)=0.118 | Connection to SS-1 β₀=7 needed |
| OPEN-P-SM-7-2 | Rigorous proof of face saturation from Green's function | Projector lemma provides framework |
| OPEN-P-SM-7-5 | Length-4 cell modes — Higgs? Gravity? | Unexplored |
| — | Light quark masses (u,d,s) | Chiral condensate dominates; new axiom likely needed |
| — | W/Z/Higgs boson masses | EW series has structural models; need quantification |
| — | Derive σ from lattice mode spectrum | Would promote CONJ-SS-2-1 to theorem |
| OPEN-SS-10 | Nuclear Binding Energy V(r) | **RESOLVED at A=2,3,4 by SS-5 v0.2 (CONJ-SS-11); full V(r) shape remains** |
| OPEN-SS-17 | Light-nuclei binding curve | PARTIALLY RESOLVED by SS-5 v0.2 at A=2,3,4; A≥6 → OPEN-SS-18 |
| OPEN-SS-18 (new) | Heavy-nuclei alpha-cluster regime A≥6 | OPEN — future SS-series paper |
| OPEN-SS-19 (new) | Rigorous derivation of (A-1) cascade factor and Pauli coefficient | OPEN |

---

## Series Status

| Series | Papers | Compliance | PDFs | Doc suite | README | Keywords |
|--------|--------|-----------|------|-----------|--------|----------|
| SM (1-10) | 10 | ✅ | ✅ | ✅ (SM-1–10) | ✅ | ✅ |
| SS (1-5) | 5 | ✅ | ✅ | ✅ | ✅ | ✅ |
| EW (1-5) | 5 | ✅ | ✅ | ✅ | ✅ | ✅ |
| QM (1-6) | 6 | ✅ | ✅ | ✅ | ✅ | ✅ |
| SR-1 | 1 | ✅ | ✅ | ✅ | ✅ | ✅ |
| SD (1-5) | 5 | ✅ | ✅ | ✅ | ✅ | ✅ |

**29 papers total. SM-1–7 on OSF; SM-8 v4.1, SM-9 v2.2, SM-10 v0.1, SS-2 v1.0, SS-4 v0.1, SS-5 v0.2 pending OSF registration.**

---

## Pending Tasks (not urgent)

- [ ] Register SM-8, SM-9, SM-10, SS-2 on OSF
- [ ] Curate SM-8/9/10/11 development transcripts
- [ ] Generate SM-8/9 verification notebooks (retroactive)
- [ ] Regenerate site-wide cpp_references.bib from all local .bib files
- [ ] Fill remaining sections of founders_vision.md (CP, DI-bit, Nexus, Vision, Theology)

---

*This document is updated after each paper production cycle. It is the AI's primary orientation document for new sessions.*
