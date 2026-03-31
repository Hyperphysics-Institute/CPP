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


### Q1. "The W± charge is 'borrowed from the reaction.' Doesn't that mean the W isn't really charged — it's just a charge carrier?"

This is a meaningful distinction and CPP makes it explicitly. The W± does carry charge ±e in the sense that it propagates with that charge from the production vertex to the decay vertex. But the charge is not an intrinsic property of the bracelet topology — the bracelet is topologically a Q = 0 object. The ±e is acquired from the quark flavor transition and returned to the decay products. This is distinct from the electron, where the charge −e is an intrinsic property of the central −eCP. In CPP, the W charge is relational and emergent; the lepton charge is intrinsic and structural.

---

### Q2. "If the W⁰ exists, why hasn't it been detected? It should leave traces in electroweak precision observables."

The W⁰ contributes to vacuum polarisation diagrams — it circulates as a virtual particle in loops. Since it is neutral and has no SM analog, its contribution to precision observables is not separately enumerated in SM calculations. In CPP, it is expected to contribute at the same order as the W± in radiative corrections (since it has the same geometry), but with different sign for some terms because of its net zero charge. Whether the existing electroweak precision data can already constrain the W⁰ contribution is an open question connected to OPEN-P-EW-5.

---

### Q3. "The V−A coupling gives 75% left-handed preference. The SM has exact V−A (100% left-handed). How does CPP get from 75% to 100%?"

The 75% is the phase-space preference from the geometric bias. In the continuum limit (l_P/L → 0, many lattice sites averaged), the effective left-handed coupling becomes a structural property of the continuum field. The discrete 75% / 25% split averages to an effective coupling g_L >> g_R in the continuum limit because the right-handed contribution carries the phase penalty of 240° vs 120°. For massless particles (which have definite helicity), the 120°/240° asymmetry becomes the distinction between left-handed and right-handed helicity states, and the coupling to the W bracelet vanishes for right-handed helicity exactly in the massless limit. The 75%/25% becomes 100%/0% at masslessness. For massive fermions there is a small residual right-handed coupling proportional to m/E — consistent with SM radiative corrections.


*Document prepared by Thomas Lee Abshier ND and Claude Sonnet (Anthropic), 31 March 2026.*
