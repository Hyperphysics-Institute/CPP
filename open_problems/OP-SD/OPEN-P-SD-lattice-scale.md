# OPEN-P-SD-lattice-scale: CPP Lattice-to-SI Conversion Constant

**Registered:** 10 April 2026
**Priority:** #1 (foundational — blocks experimental scrutiny of CPP)
**Status:** OPEN (5 routes explored, 3 converge at l_unit ≈ 0.59 fm)

---

## Problem Statement

CPP predicts mass RATIOS to 2.1% RMS with zero parameters, but has no anchor converting lattice units to physical units (metres, femtometres). Without this conversion, CPP cannot predict lengths, cross-sections, form factors, or any spatially resolved observable. The theory remains "floating above reality" (Abshier) until the conversion is established.

## What We Need

A single conversion constant: **1 CPP lattice unit (circumradius) = ? fm**

From this, all physical dimensions follow:
- l_edge = (1/φ) × l_unit
- Cage diameters = 2d × l_unit (d ∈ {1/φ, 1/φ, 1.0, √2})
- DP spacing, Sea density, interaction range — all in fm

## Routes Explored (10 April 2026)

| Route | Method | l_unit (fm) | Assumptions |
|-------|--------|------------|-------------|
| R1 | QCD string tension (σ = M₀/l_edge) | 0.007 | Chain = single DP per l_edge (probably wrong) |
| R2 | Confinement radius (ℏc/ΛQCD from f_π) | **0.589** | Bottom cage diameter ≈ confinement diameter |
| R3 | Proton magnetic moment | Not computed | Requires hadron-level model |
| R4 | α_s running (α_geom → α_s(m_Z)) | **0.589** | 1-loop running, α_geom = bare coupling |
| R5 | Nuclear matter density | 0.653 | Strange DP energy density ≈ nuclear energy density |

### Key Finding: Routes 2 and 4 Converge Independently

Both give Λ = 335 MeV → l_unit = ℏc/Λ = 0.589 fm. Route 2 uses pion physics (f_π). Route 4 uses coupling constant evolution (α_geom → α_s). They agree because both recover ΛQCD from independent starting points. This is genuine convergence, not circular.

### Physical Picture at l_unit = 0.59 fm

- Lattice edge: 0.36 fm
- Strange/charm cage diameter: 0.73 fm (fits inside proton)
- Bottom cage diameter: 1.18 fm (proton-scale)
- Top cage diameter: 1.66 fm
- Mean DP spacing (strange): 0.07 fm
- Proton charge radius: 0.87 fm (for comparison)

## Candidate Conversion

**l_unit = ℏc / ΛQCD ≈ 0.59 fm** (from convergence of Routes 2 and 4)

This would mean: the CPP lattice spacing equals the QCD confinement scale. Physically natural — the lattice IS the structure that confines quarks.

## What Would Make This Definitive

1. **Predict the proton charge radius** from u-u-d cage geometry at l_unit = 0.59 fm. Target: 0.87 fm. This uses an observable not involved in any of the 5 routes.

2. **Predict a scattering cross-section** (e.g., DIS structure function) from cage geometry. Comparison to data anchors the scale independently.

3. **Derive l_unit from first principles** — compute ΛQCD from α_geom and the 600-cell mode spectrum without referencing measured ΛQCD.

## Why This Matters

Without this conversion, CPP:
- Cannot predict any length observable
- Cannot be tested against scattering experiments
- Cannot connect to lattice QCD results
- Remains a ratio-prediction framework, not a complete physical theory

With this conversion, CPP:
- Predicts quark cage sizes in fm
- Predicts internal DP densities in fm⁻³
- Can be compared to DIS, form factors, and lattice QCD
- Becomes experimentally testable at existing facilities

## Dependencies

- SM-8 (cage geometry), SM-9 (mass formula), SM-10 (internal structure)
- SS-2 (C_F derivation, α_geom), SS-1 (confinement mechanism)
- SD-series (foundational lattice structure)

## Related Problems

- OPEN-P-SM-10-FEM (FEM simulation — needs l_edge for absolute DP density)
- OPEN-P-SM-cage-1 (derive α = 7/3 — related through V^(1/3) = cage dimension)
- OPEN-P-FV-1 (SSV → Lorentz factor — involves lattice propagator)

---

*Registered by Thomas Lee Abshier ND and Claude Opus (Anthropic), 10 April 2026.*
