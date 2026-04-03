# Reviews and FAQ — EW-2: The W⁰ Bracelet and W± Boson

**Paper:** EW-2 (cpp_ew2_W_v3.1.tex)
**Document type:** Living review record and FAQ
**Last updated:** 31 March 2026


# PART 1: FORMAL REVIEWS


## Review 1: Development Review (March 2026)

**Context:** EW-2 underwent an internal review during the development of the Monte Carlo verification script mc_weinberg_unification.py, which revealed a significant error in the v3 uncertainty propagation. The review was conducted in parallel with the development of v3.1.

**Overall verdict:** Paper is internally coherent; mass is reproduced not derived; the W⁰/W± distinction is genuine and testable in principle; v3 error was caught and corrected.


### C1 — RESOLVED: v3 Uncertainty Propagation Was Circular

**The error:** v3 EW-2 reported error sensitivities of ±0.010, ±0.008, ±0.004 GeV for sea_strength (±5%), vertex count (±1), and r_eff (±2%). These values were back-calculated to sum in quadrature to the PDG uncertainty ±0.012 GeV — a circular procedure that validated the theory against the answer it was computing.

**The correction in v3.1:** The correct formula-derived parameter sensitivities are:

    sea_strength ±5%:    δm_W = ±4.02 GeV  (formula sensitivity)
    vertex count ±1:     δm_W = ±6.19 GeV  (formula sensitivity)
    r_eff ±2%:           δm_W = ±1.61 GeV  (formula sensitivity)

The Monte Carlo SEM at N = 10⁶ events is ±0.004–0.007 GeV, well within PDG precision. The crucial distinction, now made explicit in v3.1, is between formula sensitivity (how much the predicted mass shifts when a parameter changes) and Monte Carlo SEM (the statistical precision of the mean estimate over many bracelet configurations). The v3 numbers were the latter quantity misidentified as the former.

**Scientific significance:** This error was symptomatic of a deeper issue — the boson masses are reproduced by calibrating η, which means the formula sensitivity is dominated by η rather than by the geometric parameters. The ±4–6 GeV sensitivities to sea_strength and vertex count correctly reflect that the mass formula is not robustly predictive without knowing η from first principles.

**Status: RESOLVED (v3.1)** — development-EW-2.md records the full correction history.


### C2 — OPEN: W⁰ Detection Path Not Quantified

**The concern:** The W⁰ neutral bracelet is the most novel CPP-specific prediction in EW-2, but the paper describes its detectability only qualitatively ("in principle detectable via precision DP Sea background measurements"). No cross-section estimate or experimental observable is specified.

**Assessment: VALID — prediction is genuine but needs quantification**

The W⁰ is a real prediction of the bracelet topology — it is not inserted by hand but follows directly from the same topology that gives the correct Weinberg angle and V−A chirality. Quantifying its production cross-section would require understanding the rate at which DP Sea hDPs spontaneously organise into the 6-cycle bracelet geometry. This is connected to OPEN-P-EW-1 (η derivation) — once the Planck-to-weak scale is understood, the W⁰ formation rate from the Sea can be estimated.

**Status: OPEN** — registered as OPEN-P-EW-5 (W⁰ quantitative properties).


## Summary Table

| # | Issue | Assessment | Status |
|---|-------|-----------|--------|
| C1 | v3 uncertainties back-calculated | Error | Resolved (v3.1) |
| C2 | W⁰ detection path not quantified | Valid | Open — OPEN-P-EW-5 |


# PART 2: FAQ

---

*FAQ content has been moved to FAQ-EW-2.md.*
