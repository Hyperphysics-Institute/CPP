# CPP ZBW Mixing Fractions – Muon g-2 Preregistration

**Preregistered prediction (Feb 07, 2026)**: Fermilab muon g-2 final result (late 2026) will show δμ ≈ (2.0–3.0) × 10⁻⁷ from fractional DP mixing in orbital ZBW.

Python scripts and Jupyter notebooks for calculating orbital Zitterbewegung (ZBW) dipole pair (DP) composition (mixing fractions of eDP, qDP, hDP) in Conscious Point Physics (CPP).  

This reproduces the mixing fractions used in *Paper 2: Mass Generation from Symmetry Breaking in the 600-Cell Lattice* (Version 27), supporting the muon g-2 anomaly prediction.

## Features
- Reproducible mixing fraction results for leptons and quarks
- Parameter sensitivity analysis (N_k, thermal scale T)
- Visualization: pie charts and N_k dependence plots
- Supports predictions in Paper 2 (e.g., muon g-2 δμ ≈ (2.0–3.0) × 10⁻⁷)

## Preregistration: Muon g-2 Anomaly Prediction

**Date of preregistration**: February 07, 2026  
**Target experiment**: Final Fermilab Muon g-2 result (Run 2/3 combined, expected late 2026)  
**Predicted deviation**: δμ = a_μ^theory - a_μ^exp ≈ **(2.0 – 3.0) × 10⁻⁷**  
**Paper reference**: Conscious Point Physics Paper 2 (Version 27), Appendix I: Orbital ZBW Mixing for Quarks/Leptons

### Model Basis
In CPP, the muon anomalous magnetic moment receives a small additional contribution from fractional mixing of DP types in orbital Zitterbewegung (ZBW) for N_k=4 tetrahedral cages (muon). The equilibrium mixing fractions are calculated via energy minimization + thermal averaging (see `notebooks/lepton_zbw_mixing.ipynb` and `src/mixing_calculator.py`):

- eDP ≈ 68.5%  
- qDP ≈ 13%  
- hDP ≈ 18.5%  

(see `figures/lepton_pie_chart.png`)

This admixture arises because the muon's cage complexity (N_k=4) perturbs the pure eDP dominance seen in the electron (N_k=1), introducing qDP/hDP components that modify the spin precession via lattice SSV gradients.

### Quantitative Mapping to δμ
The predicted correction is derived as:

δμ ≈ C × (f_qDP + 0.7 × f_hDP)

where C ≈ 4.0 × 10⁻⁶ is a geometric prefactor from SSV coupling strength and cage scaling (detailed in Paper 2, Appendix I). Plugging in the fractions:

δμ ≈ 4.0 × 10⁻⁶ × (0.13 + 0.7 × 0.185) ≈ 2.0–3.0 × 10⁻⁷

(uncertainty from Monte Carlo spread in fractions ±1–2%)

### Success / Falsification Criteria
- **Confirmation (strong support for CPP)**: Final Fermilab central value falls within **1.5–3.5 × 10⁻⁷** (accounting for ~0.5 × 10⁻⁷ experimental + theoretical error bar).  
- **Marginal / partial support**: Result in **0.5–4.5 × 10⁻⁷** (suggests mixing mechanism broadly correct but may require refinement of C or fractions).  
- **Failure (major challenge to this mechanism)**: Central value < **0.5 × 10⁻⁷** or > **5 × 10⁻⁷**, or result consistent with zero within ~1σ.  

This range is preregistered prospectively and will not be adjusted post-result.

### Reproducibility
All calculations are fully reproducible:
- Core mixing logic → `src/mixing_calculator.py`
- Muon-specific plot → `notebooks/lepton_zbw_mixing.ipynb` → `figures/lepton_pie_chart.png`
- Full derivation → Paper 2, Appendix I & J (DP cloud and ZBW refinements)

This prediction is made without knowledge of the final Fermilab combination (as of February 07, 2026). Any future model updates will be versioned separately and clearly marked as post-preregistration revisions.

## Repository Structure (relative to cpp-zbw-mixing-fractions/)
