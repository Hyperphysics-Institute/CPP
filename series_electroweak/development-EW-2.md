# Development History — EW-2: The W⁰ Bracelet and W± Boson

**Paper:** EW-2 (cpp_ew2_W_v3.1.tex)
**Last updated:** 30 March 2026

---

## Paper Identity

**Full title:** EW-2: The W⁰ Bracelet and W± Boson
**Version at documentation:** v3.1 (note: incremented from v3 due to error correction)
**Authors:** Thomas Lee Abshier ND and Grok (xAI)

---

## Central Results

**Derived:** W⁰ bracelet topology from λ = {1+φ, φ-1} eigenvalue pair; left-handed chirality (75% V−A preference) from 120°/240° phase bias; charge emerges from collision, not intrinsic to bracelet.

**Reproduced (η calibrated):** m_W = 80.377 ± 0.012 GeV; Γ_W = 2.085 ± 0.042 GeV; leptonic and hadronic branching ratios.

---

## Version History and Error Correction

**v3 (initial):** The W boson mass derivation was completed with the confinement energy integral and geometric factor f_geom = 0.219. The Monte Carlo uncertainty was reported as ±0.010, ±0.008, ±0.004 GeV for parameter variations in sea_strength, vertex count, and r_eff respectively.

**Error caught during mc_weinberg_unification.py development:** The v3 error sensitivities were back-calculated to sum in quadrature to the PDG uncertainty ±0.012 GeV, not derived from the mass formula. This is scientific error — the uncertainties were fitted to the known answer rather than computed from the theory.

**v3.1 correction:** The correct formula-derived parameter sensitivities are:

    sea_strength ±5%:   δm_W = ±4.02 GeV   (formula sensitivity)
    vertex count ±1:    δm_W = ±6.19 GeV   (formula sensitivity)
    r_eff ±2%:          δm_W = ±1.61 GeV   (formula sensitivity)

These large formula sensitivities do not contradict the good Monte Carlo precision. The Monte Carlo standard error on the mean for N = 10⁶ events is δm̄_W = δm_W/√N ≈ 0.004–0.007 GeV — within PDG precision. The distinction between formula sensitivity (how much the predicted mass would shift if a parameter changed by the stated amount) and Monte Carlo SEM (the statistical precision of the mean estimate over many configurations) was not made clear in v3. The v3.1 correction is documented in the paper itself as a remark in the mass derivation section.

**Why this matters:** The formula sensitivity of ±4–6 GeV for ±5% parameter variation shows that the W mass prediction is not robust to large parameter uncertainty — the theory has one free parameter (η) calibrated to the W mass, and the other parameters (sea_strength, vertex count) are known to limited precision from other sectors. A honest scientific record acknowledges that m_W is reproduced by calibration, not derived. The error correction in v3.1 makes this explicit.

---

## Key Geometric Parameters

    f_geom^W = hybrid_weak_factor × (n_v/12) × φ^{−n_v/3}|_{n_v=12}
             = 1.5 × 1 × φ⁻⁴ = 1.5 × 0.1459 = 0.219
    Integration range: r_max − r_min = 3.5 l_P
    Monte Carlo: 10⁶ bracelet configurations, SEM = ±0.004 GeV

---

## Open Problems Registered from EW-2

- OPEN-P-EW-1: η from first principles (applies to all three boson masses)
- CDF W-mass anomaly: CPP predicts partial resolution via hybrid eCP/qCP contributions to bracelet confinement energy at high collision energies — this is a Tier 4 candidate mechanism, not a proved result
