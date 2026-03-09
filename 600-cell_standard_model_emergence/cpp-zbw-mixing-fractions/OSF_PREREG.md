# OSF Preregistration: Prospective Prediction of the Muon g-2 Anomaly  
in Conscious Point Physics (CPP) via 600-Cell Lattice ZBW Mixing Fractions

**Registration Date**: February 08, 2026  
**Preregistrant**: [Your Name / tlabshier]  
**Project Link**: https://github.com/tlabshier/CPP/tree/main/standard_model_emergence_in_the_600-cell_lattice/cpp-zbw-mixing-fractions  
**Study Type**: Theoretical model prediction / computational validation against independent future-published experimental result  
**Template Basis**: OSF Preregistration (general-purpose)  
**Status**: Prospective – prediction locked prior to awareness or use of any final Fermilab muon g-2 result beyond interim values available as of Feb 2026. No post-hoc adjustment of the predicted range will be performed.

## 1. Study Information

**Working Title**  
Prospective CPP Prediction for the Anomalous Muon Magnetic Moment (g-2) Deviation via Orbital Zitterbewegung (ZBW) Mixing Fractions in the 600-Cell Quasicrystalline Lattice

**Description / Background / Purpose**  
The muon anomalous magnetic moment a_μ = (g-2)/2 exhibits a long-standing deviation from Standard Model (SM) expectations. This work uses the Conscious Point Physics (CPP) framework — modeling fundamental particles as emergent orbital patterns in a 4D 600-cell lattice with zitterbewegung (ZBW) — to predict the size of the non-SM contribution δμ ≈ a_μ^{exp} - a_μ^{SM}.  

The prediction derives from fractional mixing between "quark-like" dark photon (qDP) and "hadron-like" dark photon (hDP) components in the muon's orbital ZBW current, calibrated against known lepton and meson properties without fitting to the muon g-2 anomaly itself.  

This registration prospectively locks the predicted range and falsification criteria before consulting any final Fermilab combination result (expected full precision already published in 2025, but prospective use here assumes no knowledge of post-interim adjustments or interpretations used in model refinement).

## 2. Research Questions / Hypotheses

**Primary Research Question**  
Does the CPP 600-cell lattice model, via ZBW fractional mixing, quantitatively account for the observed muon g-2 deviation within a narrow predicted range?

**Primary Hypothesis**  
The non-SM deviation δμ will fall within (2.0 – 3.0) × 10^{-7}, arising partially (~fractional) from qDP-hDP mixing in the muon's orbital ZBW.

**Predicted Value**  
δμ ≈ (2.0 – 3.0) × 10^{-7}  
(with nominal central value ~2.5 × 10^{-7} and computational uncertainty ±1–2% from Monte Carlo sampling of lattice orbits)

## 3. Design Plan

**Study Design**  
Computational / theoretical prediction only. No new experimental data collected.  
The "study" consists of running the existing CPP simulation code to compute mixing fractions f_qDP and f_hDP, then applying the fixed formula:

δμ ≈ C × (f_qDP + 0.7 × f_hDP)

where C is a theoretically derived prefactor independent of the muon g-2 value.

**Study Type**  
Prospective theoretical prediction tested against an independent, already-collected but (for this purpose) prospectively-evaluated experimental result (Fermilab Muon g-2 final average).

**Materials / Apparatus / Code**  
- Custom C++/Python code in repository: https://github.com/tlabshier/CPP/blob/main/standard_model_emergence_in_the_600-cell_lattice/cpp-zbw-mixing-fractions  
- Key scripts: orbital ZBW simulation, mixing fraction calculator, Monte Carlo uncertainty estimation  
- Dependencies: standard numerical libraries (no exotic installs required)

**Procedure / How to Reproduce**  
See README.md in the repository for exact run instructions, including:  
- Compilation/execution steps  
- Input parameters (fixed for this prediction)  
- Output: f_qDP, f_hDP, computed δμ range

## 4. Data Collection / Source

**Data Source**  
No new data collected. Prediction will be compared to the published Fermilab Muon g-2 experimental world average for a_μ (most recent full-precision value as of late 2025 / early 2026 publications).  
Interim values were known but not used to tune the model; the prediction range is locked prospectively.

**Sample Size / Stopping Rule**  
Not applicable (computational; fixed runs with MC for uncertainty).

## 5. Analysis Plan

**Variables**  
- Independent / model-derived: f_qDP, f_hDP (mixing fractions from lattice ZBW orbits)  
- Dependent / predicted: δμ (non-SM contribution to a_μ)  
- Comparison value: δμ_exp = a_μ^{exp} - a_μ^{SM} (using published central values and uncertainties)

**Primary Analysis**  
Compute δμ from the fixed formula and report whether the experimental δμ_exp lies within the predicted [2.0, 3.0] × 10^{-7} interval (accounting for combined model + experimental uncertainties).

**Success / Falsification Criteria**  
- Success: δμ_exp ∈ [2.0 – 3.0] × 10^{-7} (within 1σ combined uncertainty if quoted)  
- Partial / suggestive: within ~2–3σ  
- Falsification: outside >3σ of the predicted range → model requires fundamental revision (post-hoc versioning)

**Uncertainty Estimation**  
Monte Carlo variation over lattice orbit parameters (±1–2% on δμ); full propagation to be reported.

**No p-hacking / Flexibility**  
The prediction range and formula coefficients are fixed before result consultation. No post-hoc parameter tuning will adjust the preregistered range.

## 6. Other

**Contingencies / Deviations**  
Any deviation from this plan (e.g., if code bug found) will be timestamped and documented in an updated version of this file or the OSF registration (noting that files are immutable but wiki/log can track changes).

**References / Related Work**  
- CPP model papers (linked in repository README)  
- Fermilab Muon g-2 final publications (2025): e.g., Phys. Rev. Lett. (final 127 ppb result)

**License**  
Content: CC-BY-4.0; Code: MIT (see repository)

This preregistration is prospective and time-stamped on OSF submission (February 08, 2026). The prediction is blind to any post-2025 interpretations that might retroactively influence model tuning.
