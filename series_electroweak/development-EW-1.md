# Development History — EW-1: Electroweak Bosons from 600-Cell Eigenvalue Topology

**Paper:** EW-1 (cpp_ew1_intro_v3.tex)
**Series position:** Introductory paper — establishes the eigenvalue bridge and the Weinberg angle derivation
**Last updated:** 30 March 2026

---

## Paper Identity

**Full title:** EW-1: Electroweak Bosons from 600-Cell Eigenvalue Topology
**Series:** 600-Cell Standard Model Emergence Series — Electroweak
**Version at documentation:** v3
**Authors:** Thomas Lee Abshier ND and Grok (xAI)
**Status:** Submission-ready pending OSF preregistration

---

## Central Results

**Derived (no free parameters):**
- sin²θ_W(M_Z) = 0.2312 ± 0.0003 (PDG: 0.23121 ± 0.00004, agreement 0.004%)
- Eigenvalue-topology correspondence: three boson topologies from six 600-cell eigenvalues
- φ⁻³ geometric dilution factor from shell-radius scaling
- No stable boson between m_Z and m_H (eigenvalue gap prediction)

**Reproduced (η calibrated):**
- m_W = 80.377 GeV, m_Z = 91.188 GeV, m_H = 125.10 GeV
- Decay widths Γ_W and Γ_Z

---

## Version History

**v1–v2 (early 2026):** The eigenvalue bridge was identified connecting the six 600-cell adjacency matrix eigenvalues to the three electroweak bosons. The mapping W ↔ {1+φ, φ-1}, Z ↔ 12, H ↔ -(1+φ) was established from physical arguments (reactivity, mass ordering, spin). The Weinberg angle formula using the four-layer phase interference and p_k = (1-k/5)² weights was derived. Monte Carlo over 10⁶ configurations confirmed sin²θ_W = 0.2312 ± 0.0003.

**v3 (current):** The three boson theorems were stated as formal theorems (Theorems 1–3). The distinction between derived and reproduced results was clarified throughout — specifically, the "Derived" label for sin²θ_W and "Reproduced" labels for masses were added to the predictions table in explicit acknowledgment that η is calibrated. The open problems were formally numbered and registered. The W⁰/W± distinction was added as a section and identified as the most novel CPP-specific structural prediction.

---

## Key Constants and Parameters

    Six eigenvalues: {12, 1+φ, φ−1, 1−φ, −φ, −(1+φ)}  where φ = (1+√5)/2 ≈ 1.618
    φ⁻³ ≈ 0.236  (geometric dilution, derived)
    η ~ 10⁻¹⁷     (Planck-to-weak reduction, calibrated — OPEN-P-EW-1)
    hybrid_weak_factor = 1.5  (3 weak layers / 2 EM polarities)
    sea_strength = 0.185  (from neutron charge neutrality)
    sin²θ_W = 0.2312 ± 0.0003  (derived, Monte Carlo confirmed)

---

## Open Problems Registered

- OPEN-P-EW-1: Planck-to-weak-scale reduction η from first principles
- OPEN-P-EW-2: Self-consistent mass formula with single integration range
- OPEN-P-EW-3: Coupling constants g and g' from vertex counting without calibration factor
- OPEN-P-EW-4: Mass ratios m_H/m_Z and m_Z/m_W from eigenvalue ratios

---

## Connection to Other Series

**QM Paper 6:** The six eigenvalues were first identified in the QM series as mapping to three SM generations. EW-1 repurposes the same eigenvalues to select electroweak boson topologies. This cross-series use of the same geometric structure is the eigenvalue bridge — the primary unification result of the EW series.

**SS-1 connection:** The φ⁻³ geometric dilution factor uses the same 1:φ:φ² shell-radius scaling that appears in SS-1's Voronoi geometry and α_geom derivation. The 600-cell's golden-ratio structure is not sector-specific.

**EW-5 connection:** EW-1 presents the Weinberg angle result and the broad framework. EW-5 provides the full proofs of the four theorems (SU(2)_L algebra, Nexus invariance, Yang-Mills limit, Weinberg angle). Readers needing the full derivations should consult EW-5.
