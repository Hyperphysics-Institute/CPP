# Integrity audit report

## Summary (fabrication-class first)

| Paper | fabrication-class F | repro-class F | warns | verdict |
|---|---|---|---|---|
| DM-1 | 0 | 6 | 6 | fail (repro) |
| DM-2 | 0 | 2 | 3 | fail (repro) |
| DM-3 | 0 | 1 | 1 | fail (repro) |
| EU-1 | 0 | 0 | 2 | warn |
| EW-1 | 0 | 1 | 1 | fail (repro) |
| EW-2 | 0 | 1 | 1 | fail (repro) |
| EW-3 | 0 | 1 | 1 | fail (repro) |
| EW-4 | 0 | 1 | 1 | fail (repro) |
| EW-5 | 0 | 1 | 1 | fail (repro) |
| QM-1 | 0 | 0 | 0 | clean |
| QM-2 | 0 | 0 | 0 | clean |
| QM-3 | 0 | 0 | 0 | clean |
| QM-4 | 0 | 0 | 0 | clean |
| QM-5 | 0 | 0 | 0 | clean |
| QM-6 | 0 | 0 | 0 | clean |
| SD-1 | 0 | 0 | 0 | clean |
| SD-2 | 1 | 0 | 0 | **FAIL** |
| SD-3 | 0 | 0 | 0 | clean |
| SD-4 | 0 | 0 | 0 | clean |
| SD-5 | 0 | 0 | 0 | clean |
| SF-1 | 2 | 0 | 1 | **FAIL** |
| SF-2 | 5 | 0 | 4 | **FAIL** |
| SF-3 | 0 | 0 | 0 | clean |
| SF-4 | 0 | 0 | 1 | warn |
| SF-5 | 0 | 2 | 1 | fail (repro) |
| SF-6 | 0 | 0 | 0 | clean |
| SF-7 | 0 | 0 | 1 | warn |
| SM-1 | 0 | 3 | 1 | fail (repro) |
| SM-10 | 0 | 3 | 1 | fail (repro) |
| SM-2 | 0 | 3 | 1 | fail (repro) |
| SM-3 | 0 | 3 | 1 | fail (repro) |
| SM-4 | 0 | 3 | 1 | fail (repro) |
| SM-5 | 0 | 3 | 1 | fail (repro) |
| SM-6 | 0 | 4 | 3 | fail (repro) |
| SM-7 | 0 | 3 | 1 | fail (repro) |
| SM-8 | 0 | 3 | 1 | fail (repro) |
| SM-9 | 0 | 3 | 1 | fail (repro) |
| SR-1 | 8 | 6 | 3 | **FAIL** |
| SR-2 | 4 | 4 | 3 | **FAIL** |
| SS-1 | 0 | 4 | 1 | fail (repro) |
| SS-1A | 0 | 4 | 2 | fail (repro) |
| SS-1B | 0 | 4 | 1 | fail (repro) |
| SS-1C | 0 | 4 | 1 | fail (repro) |
| SS-1D | 0 | 4 | 1 | fail (repro) |
| SS-1E | 0 | 4 | 1 | fail (repro) |
| SS-1F | 0 | 4 | 1 | fail (repro) |
| SS-2 | 0 | 4 | 1 | fail (repro) |
| SS-3 | 0 | 4 | 3 | fail (repro) |
| SS-4 | 0 | 4 | 1 | fail (repro) |
| SS-5 | 0 | 0 | 1 | warn |
| SS-6 | 0 | 0 | 0 | clean |
| SS-7 | 0 | 2 | 1 | fail (repro) |
| SS-8 | 0 | 3 | 2 | fail (repro) |
| SS-9 | 3 | 12 | 12 | **FAIL** |
| TP-1 | 0 | 2 | 0 | fail (repro) |

## DM-1  [FAIL]  (6 fail / 6 warn)  series_phenomena/cosmology/dark_matter/DM-1

- **FAIL** `F3-NONSTDLIB` `series_phenomena/cosmology/dark_matter/scripts/0849_residual_potential.py` — non-stdlib imports: matplotlib, numpy (undeclared)
- **WARN** `W-NONSTDLIB-DECLARED` `series_phenomena/cosmology/dark_matter/scripts/0850_specific_dwarf_fit.py` — non-stdlib imports: matplotlib, numpy
- **WARN** `W-NONSTDLIB-DECLARED` `series_phenomena/cosmology/dark_matter/scripts/0851_core_radius_vs_sigma.py` — non-stdlib imports: matplotlib, numpy, scipy
- **FAIL** `F3-NONSTDLIB` `series_phenomena/cosmology/dark_matter/code/1859_collision_energy_reconciliation.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W4-CIRCULARITY?` `series_phenomena/cosmology/dark_matter/code/1865_empirical_dwarf_pin_recalibration.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_phenomena/cosmology/dark_matter/code/1870_soft_rod_mc.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_phenomena/cosmology/dark_matter/code/1871_soft_rod_mc_pinned_geometry.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_phenomena/cosmology/dark_matter/code/1878_confront3_baryon_sector_scoping.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_phenomena/cosmology/dark_matter/code/1879_xqc_recomputation.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_phenomena/cosmology/dark_matter/code/1881_j12_island_residuals.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_phenomena/cosmology/dark_matter/code/1888_si2_scan_and_predictions.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W5-IDENTITY-BILLING` `series_phenomena/cosmology/dark_matter/DM-1/DM-1_substrate_dark_matter_candidate.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## DM-2  [FAIL]  (2 fail / 3 warn)  series_phenomena/cosmology/sea_gravitation/DM-2

- **FAIL** `F3-NONSTDLIB` `series_phenomena/cosmology/sea_gravitation/scripts/0720_milne_mccrea_check.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W4-CIRCULARITY?` `series_phenomena/cosmology/sea_gravitation/scripts/0721_gradient_source_distinction.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_phenomena/cosmology/sea_gravitation/scripts/0721_gradient_source_distinction.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W-NONSTDLIB-DECLARED` `series_phenomena/cosmology/sea_gravitation/scripts/0723_horizon_wz.py` — non-stdlib imports: numpy, scipy
- **WARN** `W5-IDENTITY-BILLING` `series_phenomena/cosmology/sea_gravitation/DM-2/DM-2_sea_gravitation_dark_sector.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## DM-3  [FAIL]  (1 fail / 1 warn)  series_phenomena/cosmology/dark_matter/DM-3

- **WARN** `W4-CIRCULARITY?` `series_phenomena/cosmology/dark_matter/code/2302_dm3_sigma_v_shape_discriminant.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_phenomena/cosmology/dark_matter/DM-3/code/2359_f5_halo_sensitivity.py` — non-stdlib imports: numpy (undeclared)

## EU-1  [WARN]  (0 fail / 2 warn)  series_phenomena/cosmology/early_universe/EU-1

- **WARN** `W2-ABSORB-BILLING` `series_phenomena/cosmology/early_universe/EU-1/EU-1_primordial_spectral_index.tex` — absorption language cohabits with zero-parameter billing
- **WARN** `W5-IDENTITY-BILLING` `series_phenomena/cosmology/early_universe/EU-1/EU-1_primordial_spectral_index.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## EW-1  [FAIL]  (1 fail / 1 warn)  series_electroweak/papers

- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## EW-2  [FAIL]  (1 fail / 1 warn)  series_electroweak/papers

- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## EW-3  [FAIL]  (1 fail / 1 warn)  series_electroweak/papers

- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## EW-4  [FAIL]  (1 fail / 1 warn)  series_electroweak/papers

- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## EW-5  [FAIL]  (1 fail / 1 warn)  series_electroweak/papers

- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## QM-1  [clean]  (0 fail / 0 warn)  series_quantum_mechanics/papers


## QM-2  [clean]  (0 fail / 0 warn)  series_quantum_mechanics/papers


## QM-3  [clean]  (0 fail / 0 warn)  series_quantum_mechanics/papers


## QM-4  [clean]  (0 fail / 0 warn)  series_quantum_mechanics/papers


## QM-5  [clean]  (0 fail / 0 warn)  series_quantum_mechanics/papers


## QM-6  [clean]  (0 fail / 0 warn)  series_quantum_mechanics/papers


## SD-1  [clean]  (0 fail / 0 warn)  series_foundations/series_superdeterminism


## SD-2  [FAIL]  (1 fail / 0 warn)  series_foundations/series_superdeterminism

- **FAIL** `F1-MISSING` `series_foundations/series_superdeterminism/SD-2_h4_angular_structure.tex` — cited script not found in repo: CPP/series_foundations/compute_h4_angles.py

## SD-3  [clean]  (0 fail / 0 warn)  series_foundations/series_superdeterminism


## SD-4  [clean]  (0 fail / 0 warn)  series_foundations/series_superdeterminism


## SD-5  [clean]  (0 fail / 0 warn)  series_foundations/series_superdeterminism


## SF-1  [FAIL]  (2 fail / 1 warn)  flagship_papers/charged_leptons

- **FAIL** `F1-MISSING` `flagship_papers/charged_leptons/reasoning/1402.md` — cited script not found in repo: scripts/1402.py
- **FAIL** `F1-MISSING` `flagship_papers/charged_leptons/reasoning/1403.md` — cited script not found in repo: scripts/1403.py
- **WARN** `W5-IDENTITY-BILLING` `flagship_papers/charged_leptons/sf-1_charged_leptons.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## SF-2  [FAIL]  (5 fail / 4 warn)  flagship_papers/electroweak

- **WARN** `W-NONSTDLIB-DECLARED` `flagship_papers/electroweak/code/dp_chain_monte_carlo.py` — non-stdlib imports: numpy, torch
- **WARN** `W-NONSTDLIB-DECLARED` `flagship_papers/electroweak/code/oblique_parameters_framework.py` — non-stdlib imports: numpy, torch
- **WARN** `W-NONSTDLIB-DECLARED` `flagship_papers/electroweak/code/oblique_parameters_sensitivity_scan.py` — non-stdlib imports: numpy, torch
- **FAIL** `F1-MISSING` `flagship_papers/electroweak/sketches/SF-2_W0_derivation.md` — cited script not found in repo: compute_shells.py
- **FAIL** `F1-MISSING` `flagship_papers/electroweak/sketches/SF-2_W0_derivation.md` — cited script not found in repo: find_substructures.py
- **FAIL** `F1-MISSING` `flagship_papers/electroweak/sketches/SF-2_W0_derivation.md` — cited script not found in repo: home/claude/compute_600cell_spectrum.py
- **FAIL** `F1-MISSING` `flagship_papers/electroweak/review/sf2_deltacp_scoping_review_package_v1.0.md` — cited script not found in repo: verify_sf2_deltacp_scoping_context.py
- **FAIL** `F1-MISSING` `flagship_papers/electroweak/review/sf2_portfolio_scoping_review_package_v1.0.md` — cited script not found in repo: verify_sf2_portfolio_scoping_inventory.py
- **WARN** `W5-IDENTITY-BILLING` `flagship_papers/electroweak/sf-2_companion.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## SF-3  [clean]  (0 fail / 0 warn)  flagship_papers/quarks


## SF-4  [WARN]  (0 fail / 1 warn)  flagship_papers/neutrinos

- **WARN** `W5-IDENTITY-BILLING` `flagship_papers/neutrinos/sf-4_neutrinos.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## SF-5  [FAIL]  (2 fail / 1 warn)  flagship_papers/strong

- **FAIL** `F3-NONSTDLIB` `flagship_papers/strong/code/2200_verify_g1a_scalefree_ratio.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `flagship_papers/strong/code/2201_verify_g1a_ponderomotive.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W-NONSTDLIB-DECLARED` `flagship_papers/strong/code/2202_verify_g1a_screening_pin.py` — non-stdlib imports: numpy

## SF-6  [clean]  (0 fail / 0 warn)  flagship_papers/electromagnetism


## SF-7  [WARN]  (0 fail / 1 warn)  flagship_papers/unification

- **WARN** `W5-IDENTITY-BILLING` `flagship_papers/unification/sf-7_grand_unification.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## SM-1  [FAIL]  (3 fail / 1 warn)  series_standard_model/papers

- **FAIL** `F3-NONSTDLIB` `series_standard_model/notebooks/SM-8_quark_generation_600cell_shells.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## SM-10  [FAIL]  (3 fail / 1 warn)  series_standard_model/papers

- **FAIL** `F3-NONSTDLIB` `series_standard_model/notebooks/SM-8_quark_generation_600cell_shells.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## SM-2  [FAIL]  (3 fail / 1 warn)  series_standard_model/papers

- **FAIL** `F3-NONSTDLIB` `series_standard_model/notebooks/SM-8_quark_generation_600cell_shells.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## SM-3  [FAIL]  (3 fail / 1 warn)  series_standard_model/papers

- **FAIL** `F3-NONSTDLIB` `series_standard_model/notebooks/SM-8_quark_generation_600cell_shells.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## SM-4  [FAIL]  (3 fail / 1 warn)  series_standard_model/papers

- **FAIL** `F3-NONSTDLIB` `series_standard_model/notebooks/SM-8_quark_generation_600cell_shells.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## SM-5  [FAIL]  (3 fail / 1 warn)  series_standard_model/papers

- **FAIL** `F3-NONSTDLIB` `series_standard_model/notebooks/SM-8_quark_generation_600cell_shells.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## SM-6  [FAIL]  (4 fail / 3 warn)  series_standard_model/papers

- **FAIL** `F3-NONSTDLIB` `series_standard_model/notebooks/SM-8_quark_generation_600cell_shells.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W4-CIRCULARITY?` `series_standard_model/notebooks/nb01_SM6_verification.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_standard_model/notebooks/nb01_SM6_verification.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W5-IDENTITY-BILLING` `series_standard_model/papers/SM-6_lepton_mass_spectrum.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## SM-7  [FAIL]  (3 fail / 1 warn)  series_standard_model/papers

- **FAIL** `F3-NONSTDLIB` `series_standard_model/notebooks/SM-8_quark_generation_600cell_shells.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## SM-8  [FAIL]  (3 fail / 1 warn)  series_standard_model/papers

- **FAIL** `F3-NONSTDLIB` `series_standard_model/notebooks/SM-8_quark_generation_600cell_shells.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## SM-9  [FAIL]  (3 fail / 1 warn)  series_standard_model/papers

- **FAIL** `F3-NONSTDLIB` `series_standard_model/notebooks/SM-8_quark_generation_600cell_shells.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_electroweak/notebooks/mc_weinberg_unification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **FAIL** `F3-NONSTDLIB` `series_electroweak/notebooks/mc_weinberg_unification.py` — non-stdlib imports: numpy (undeclared)

## SR-1  [FAIL]  (14 fail / 3 warn)  series_relativity/papers

- **FAIL** `F3-NONSTDLIB` `series_relativity/op_einstein_closure/spin2_construction/code/1123_task2_completion_check.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_relativity/op_einstein_closure/spin2_construction/code/1124_task3_quadrupole_verification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **WARN** `W-NONSTDLIB-DECLARED` `series_relativity/op_einstein_closure/spin2_construction/code/1124_task3_quadrupole_verification.py` — non-stdlib imports: numpy
- **FAIL** `F3-NONSTDLIB` `series_relativity/op_einstein_closure/spin2_construction/code/1125_task4_tt_response_energy.py` — non-stdlib imports: numpy, sympy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_relativity/op_einstein_closure/spin2_construction/code/1127_eccentric_energy_ledger.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F5-ELISION` `series_relativity/notebooks/600-cell-monte-carlo-k-fit.py` — marker "For brevity"
- **FAIL** `F4-STUB` `series_relativity/notebooks/600-cell-monte-carlo-k-fit.py` — For  body is a bare pass (line 43)
- **FAIL** `F3-NONSTDLIB` `series_relativity/notebooks/600-cell-monte-carlo-k-fit.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F4-STUB` `series_relativity/notebooks/SR-2_figures.py` — 'raw = []/{}' never filled but used 1x (SR-1 fabricated-MC pattern)
- **FAIL** `F3-NONSTDLIB` `series_relativity/notebooks/SR-2_figures.py` — non-stdlib imports: matplotlib, numpy (undeclared)
- **FAIL** `F4-STUB` `series_relativity/notebooks/600cell_monte_carlo_voronoi_k_fit.py` — 'vertices = []/{}' never filled but used 1x (SR-1 fabricated-MC pattern)
- **FAIL** `F3-NONSTDLIB` `series_relativity/notebooks/600cell_monte_carlo_voronoi_k_fit.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F6-DIMFORCE` `series_relativity/papers/mechanism-SR-1.md` — dimensional analysis forces the prefactor
- **FAIL** `F6-DIMFORCE` `series_relativity/papers/development-SR-1.md` — Dimensional analysis forces the prefactor
- **FAIL** `F6-DIMFORCE` `series_relativity/papers/glossary-SR-1.md` — dimensional analysis forces the prefactor
- **WARN** `W5-IDENTITY-BILLING` `series_relativity/papers/SR-1_special_relativity_emergence.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)
- **FAIL** `F7-CONTRADICTION` `series_relativity/papers/SR-1_special_relativity_emergence.tex` — frontier records withdrawal (frontier_sectors/SR.md:27) but the paper still bills zero-parameter

## SR-2  [FAIL]  (8 fail / 3 warn)  series_relativity/papers

- **FAIL** `F3-NONSTDLIB` `series_relativity/op_einstein_closure/spin2_construction/code/1123_task2_completion_check.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W1-HARDCODED-PRINT` `series_relativity/op_einstein_closure/spin2_construction/code/1124_task3_quadrupole_verification.py` — print() of a string literal carrying >=6-sig-fig decimals (fabricated-output signature; verify the number is computed)
- **WARN** `W-NONSTDLIB-DECLARED` `series_relativity/op_einstein_closure/spin2_construction/code/1124_task3_quadrupole_verification.py` — non-stdlib imports: numpy
- **FAIL** `F3-NONSTDLIB` `series_relativity/op_einstein_closure/spin2_construction/code/1125_task4_tt_response_energy.py` — non-stdlib imports: numpy, sympy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_relativity/op_einstein_closure/spin2_construction/code/1127_eccentric_energy_ledger.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F4-STUB` `series_relativity/notebooks/SR-2_figures.py` — 'raw = []/{}' never filled but used 1x (SR-1 fabricated-MC pattern)
- **FAIL** `F3-NONSTDLIB` `series_relativity/notebooks/SR-2_figures.py` — non-stdlib imports: matplotlib, numpy (undeclared)
- **WARN** `W5-IDENTITY-BILLING` `series_relativity/papers/SR-2_spin_bit_axiom_quadrupole_formula.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)
- **FAIL** `F6-DIMFORCE` `series_relativity/papers/mechanism-SR-1.md` — dimensional analysis forces the prefactor
- **FAIL** `F6-DIMFORCE` `series_relativity/papers/development-SR-1.md` — Dimensional analysis forces the prefactor
- **FAIL** `F6-DIMFORCE` `series_relativity/papers/glossary-SR-1.md` — dimensional analysis forces the prefactor

## SS-1  [FAIL]  (4 fail / 1 warn)  series_strong/papers

- **WARN** `W4-CIRCULARITY?` `series_strong/notebooks/mc_su3_algebra.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/mc_su3_algebra.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `archive/SM-11 rename to SS-2 archive/SM-11_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/parameters_600cell.py` — non-stdlib imports: numpy (undeclared)

## SS-1A  [FAIL]  (4 fail / 2 warn)  series_strong/papers

- **WARN** `W-PLANNED-SCRIPT` `series_strong/papers/SS-1a_cage_geometry_eigenvalue_bridge.tex` — cited script marked planned, not yet in repo: CPP/series_strong/mc_hadron_mass.py
- **WARN** `W4-CIRCULARITY?` `series_strong/notebooks/mc_su3_algebra.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/mc_su3_algebra.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `archive/SM-11 rename to SS-2 archive/SM-11_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/parameters_600cell.py` — non-stdlib imports: numpy (undeclared)

## SS-1B  [FAIL]  (4 fail / 1 warn)  series_strong/papers

- **WARN** `W4-CIRCULARITY?` `series_strong/notebooks/mc_su3_algebra.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/mc_su3_algebra.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `archive/SM-11 rename to SS-2 archive/SM-11_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/parameters_600cell.py` — non-stdlib imports: numpy (undeclared)

## SS-1C  [FAIL]  (4 fail / 1 warn)  series_strong/papers

- **WARN** `W4-CIRCULARITY?` `series_strong/notebooks/mc_su3_algebra.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/mc_su3_algebra.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `archive/SM-11 rename to SS-2 archive/SM-11_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/parameters_600cell.py` — non-stdlib imports: numpy (undeclared)

## SS-1D  [FAIL]  (4 fail / 1 warn)  series_strong/papers

- **WARN** `W4-CIRCULARITY?` `series_strong/notebooks/mc_su3_algebra.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/mc_su3_algebra.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `archive/SM-11 rename to SS-2 archive/SM-11_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/parameters_600cell.py` — non-stdlib imports: numpy (undeclared)

## SS-1E  [FAIL]  (4 fail / 1 warn)  series_strong/papers

- **WARN** `W4-CIRCULARITY?` `series_strong/notebooks/mc_su3_algebra.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/mc_su3_algebra.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `archive/SM-11 rename to SS-2 archive/SM-11_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/parameters_600cell.py` — non-stdlib imports: numpy (undeclared)

## SS-1F  [FAIL]  (4 fail / 1 warn)  series_strong/papers

- **WARN** `W4-CIRCULARITY?` `series_strong/notebooks/mc_su3_algebra.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/mc_su3_algebra.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `archive/SM-11 rename to SS-2 archive/SM-11_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/parameters_600cell.py` — non-stdlib imports: numpy (undeclared)

## SS-2  [FAIL]  (4 fail / 1 warn)  series_strong/papers

- **WARN** `W4-CIRCULARITY?` `series_strong/notebooks/mc_su3_algebra.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/mc_su3_algebra.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `archive/SM-11 rename to SS-2 archive/SM-11_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/parameters_600cell.py` — non-stdlib imports: numpy (undeclared)

## SS-3  [FAIL]  (4 fail / 3 warn)  series_strong/papers

- **WARN** `W4-CIRCULARITY?` `series_strong/notebooks/mc_su3_algebra.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/mc_su3_algebra.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W4-CIRCULARITY?` `series_strong/papers/SS-3_su3_uniqueness.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **WARN** `W-NONSTDLIB-DECLARED` `series_strong/papers/SS-3_su3_uniqueness.py` — non-stdlib imports: numpy
- **FAIL** `F3-NONSTDLIB` `archive/SM-11 rename to SS-2 archive/SM-11_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/parameters_600cell.py` — non-stdlib imports: numpy (undeclared)

## SS-4  [FAIL]  (4 fail / 1 warn)  series_strong/papers

- **WARN** `W4-CIRCULARITY?` `series_strong/notebooks/mc_su3_algebra.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/mc_su3_algebra.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `archive/SM-11 rename to SS-2 archive/SM-11_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-2_lattice_scale_nucleon.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/notebooks/parameters_600cell.py` — non-stdlib imports: numpy (undeclared)

## SS-5  [WARN]  (0 fail / 1 warn)  series_strong/papers/SS-5

- **WARN** `W5-IDENTITY-BILLING` `series_strong/papers/SS-5/SS-5_light_nuclei_open_vertex_cascade.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## SS-6  [clean]  (0 fail / 0 warn)  series_strong/papers/SS-6


## SS-7  [FAIL]  (2 fail / 1 warn)  series_strong/papers/SS-7

- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-7/scripts/SS-7_alpha_cluster_edge_formula.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `archive/SS-7_versioned_drafts/SS-7_alpha_cluster_edge_formula_v1.1.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W5-IDENTITY-BILLING` `series_strong/papers/SS-7/SS-7_alpha_cluster_edge_formula.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## SS-8  [FAIL]  (3 fail / 2 warn)  series_strong/papers/SS-8

- **WARN** `W-NONSTDLIB-DECLARED` `series_strong/papers/SS-8/scripts/ss8_Q2_algebraic_reduction_test.py` — non-stdlib imports: numpy
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-8/scripts/ss8_ssv_minimization_sketch.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-8/scripts/ss8_empirical_map_extended.py` — non-stdlib imports: ame2020_loader (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-8/scripts/ss8_polytope_enumeration.py` — non-stdlib imports: ame2020_loader (undeclared)
- **WARN** `W5-IDENTITY-BILLING` `series_strong/papers/SS-8/SS-8_interstitial_neutron_2EV_scaling.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## SS-9  [FAIL]  (15 fail / 12 warn)  series_strong/papers/SS-9

- **FAIL** `F1-MISSING` `series_strong/papers/SS-9/letters/SS-9_post_ship_OSF_arXiv_submission_guide.md` — cited script not found in repo: SS-9_OPEN-SS-32_Ushape_anharmonic_phase4.py
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase10_R3_Coulomb_RefD.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase11_R3_Pauli.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W-NONSTDLIB-DECLARED` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase4_anharmonic_K3_xi4.py` — non-stdlib imports: numpy, scipy
- **WARN** `W4-CIRCULARITY?` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase5_geometric_shift_R3_R4.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **WARN** `W-NONSTDLIB-DECLARED` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase5_geometric_shift_R3_R4.py` — non-stdlib imports: numpy, scipy
- **WARN** `W-NONSTDLIB-DECLARED` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase6_R3_Coulomb.py` — non-stdlib imports: numpy, scipy
- **WARN** `W-NONSTDLIB-DECLARED` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase7_R3_Coulomb_empirical.py` — non-stdlib imports: numpy, scipy
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase8_R3_Coulomb_RefA.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase9_R3_Coulomb_RefC.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W-NONSTDLIB-DECLARED` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase2.py` — non-stdlib imports: numpy, scipy
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase3a.py` — non-stdlib imports: numpy, scipy (undeclared)
- **WARN** `W4-CIRCULARITY?` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase3b_a.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase3b_a.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase3b_b.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_scoping.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W4-CIRCULARITY?` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_a.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_a.py` — non-stdlib imports: numpy (undeclared)
- **WARN** `W-NONSTDLIB-DECLARED` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_a_Ascaling.py` — non-stdlib imports: numpy, scipy
- **WARN** `W4-CIRCULARITY?` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_a_Ascaling_R1.py` — target/expected/reference variable assigned a literal; check the input data is not generated from it
- **WARN** `W-NONSTDLIB-DECLARED` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_a_Ascaling_R1.py` — non-stdlib imports: numpy, scipy
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer1.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3_cluster_surface_phase1.py` — non-stdlib imports: numpy, scipy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_strong/papers/SS-9/scripts/SS-9_alpha_chain_extended.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F1-MISSING` `series_strong/papers/SS-9/sketches/SS-9_table1_residual_fingerprint.md` — cited script not found in repo: scripts/SS-9_table1_residual_decomposition.py
- **FAIL** `F1-MISSING` `series_strong/papers/SS-9/documentation_suite/reasoning-SS-9.md` — cited script not found in repo: series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_anharmonic_phase4.py
- **WARN** `W5-IDENTITY-BILLING` `series_strong/papers/SS-9/SS-9_simplicial_alpha_polytope_connectivity.tex` — identity language + prediction billing in one file (gamma-bridge pattern; adjudicate)

## TP-1  [FAIL]  (2 fail / 0 warn)  series_phenomena/quantum_optics/photon_truncation/TP-1

- **FAIL** `F3-NONSTDLIB` `series_phenomena/quantum_optics/photon_truncation/scripts/1700_truncation_regularization.py` — non-stdlib imports: numpy (undeclared)
- **FAIL** `F3-NONSTDLIB` `series_phenomena/quantum_optics/photon_truncation/scripts/1701_divergence_class.py` — non-stdlib imports: numpy (undeclared)

