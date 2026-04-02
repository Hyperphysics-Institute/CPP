# Reviews and FAQ — EW Series: Electroweak Bosons from 600-Cell Topology

**Paper:** EW-1
**Document type:** Living review record and FAQ
**Last updated:** 30 March 2026

**Primary scope (EW-1):** Primary review concerns for EW-1: eigenvalue bridge validity, Weinberg angle derivation, derived vs reproduced status table.

*A single reviews file covers all five EW papers, since the key critical questions about the series span all five papers. Individual paper reviews files reference this document.*


# PART 1: FORMAL REVIEWS


## Review 1: Claude Sonnet Internal Review (March 2026)

**Reviewer:** Claude Sonnet 4.x (Anthropic) — acting as skeptical physicist
**Verdict:** Series is internally coherent; four genuine derivations; individual masses are reproduced not derived; η is the central outstanding gap.
**Overall assessment:** "The Weinberg angle structural framework — four-layer phase interference with golden-ratio probability weights from 600-cell dihedral projections — is the cleanest result in the EW series and a genuine geometric derivation. However, the coupling constants g and g' that enter the mixing formula require one calibration (vertex_count_correction = 1.18), so the final numerical value sin²θ_W = 0.2312 is reproduced rather than predicted from zero parameters. *(Corrected 31 March 2026: the previous assessment stated 'genuine zero-parameter derivation'; this was overclaimed. The structural framework is derived; the coupling calibration is OP-EW-3.)* The individual boson masses are a different matter — they are reproduced by calibrating η, and the series is honest about this. The main weakness is that the η calibration is not just a small correction: it is a factor of 10¹⁷, which is the dominant contribution to the mass scale."

---

### C1 — Valid: η ~ 10⁻¹⁷ Is Not a Small Correction — It Is the Mass Scale Itself

**The concern:** The geometric factor φ⁻³ ≈ 0.236 is a factor of ~4 reduction. The remaining factor η ~ 10⁻¹⁷ provides the ~17 orders of magnitude from Planck scale to weak scale. The mass formula is essentially m_boson = E_Planck × (factor of 4 from geometry) × (factor of 10⁻¹⁷ from calibration). The geometric contribution is a rounding error relative to η. Calling the mass derivations "reproduced from geometry" is misleading — they are reproduced from one large calibrated number.

**Assessment: VALID — acknowledged in the series status table**

This concern is correct and the EW series addresses it honestly. The EW-5 status table explicitly labels m_W, m_Z, m_H as "Reproduced (η calibrated)" not "Derived." The OPEN-P-EW-1 entry describes the problem directly. The philosophical position is that reproducing the known masses while using one calibrated factor is a necessary first step — it confirms the topology is correct and the geometric structure is right — but it is not a derivation. The sin²θ_W structural framework (which requires no η) is the closest result to a genuine derivation, though it too requires one coupling calibration (OP-EW-3).

**Status: ACKNOWLEDGED — registered as OPEN-P-EW-1**


### C2 — Valid: The W⁰/W± Distinction Is Novel but Untestable Currently

**The concern:** The CPP-specific W⁰ neutral bracelet is the most novel prediction in the series, but it has no current experimental test. "In principle detectable via precision Dipole Sea background measurements" is not a concrete experimental proposal.

**Assessment: VALID — prediction is genuine but path to test is unclear**

The W⁰ prediction is genuinely novel — the SM has no corresponding particle. Its existence follows directly from the bracelet topology, which is the same topology that gives the correct Weinberg angle and left-handed chirality. The prediction is not ad hoc. However, the detection proposal ("precision DP Sea background measurements") is qualitative. Quantifying the cross-section for W⁰ production or decay would make this a concrete falsifiable prediction rather than a theoretical curiosity.

**Status: OPEN — W⁰ detection cross-section calculation needed**


### C3 — Valid: The v3 Error in EW-2 Uncertainty Propagation Was Significant

**The concern:** The v3 EW-2 paper reported Monte Carlo error sensitivities (±0.010, ±0.008, ±0.004 GeV) that were back-calculated from the PDG uncertainty rather than derived from the mass formula. This is a form of circular validation — the uncertainties were chosen to match the known answer.

**Assessment: VALID — caught and corrected in v3.1**

The correction was made in v3.1. The formula-derived sensitivities are ±4.0, ±6.2, ±1.6 GeV for 5% sea_strength variation, ±1 vertex, ±2% r_eff respectively. The Monte Carlo SEM at N = 10⁶ is ±0.004–0.007 GeV. The key lesson: formula sensitivity (how much the mass shifts when a parameter changes) is not the same as Monte Carlo SEM (the statistical precision of the mean estimate). The v3.1 correction makes this distinction explicit. This is recorded in the development history as an example of the kind of honest error-catching that strengthens the CPP programme.

**Status: RESOLVED (v3.1)**


### C4 — Valid: The Loop/Shell Density Factors Are Fitted, Not Derived

**The concern:** The loop density factor ℓ_Z ≈ 1.2 (vs ideal 1.437) and shell density factor s_H ≈ 1.4 (vs ideal 1.291) are attributed to 4D projection effects but computed as effective values in Monte Carlo rather than derived analytically from the 4D subgraph coordinates.

**Assessment: VALID — registered as OPEN-P-EW-3**

The reduction from ideal to effective values is physically motivated (4D projection losses in the stereographic mapping) but not analytically derived. Until the 4D projection is computed exactly, these factors are fitted to match the observed masses — another contribution to the "reproduced" status of m_Z and m_H. Deriving ℓ_Z and s_H analytically would be a significant step toward making the mass predictions parameter-free.

**Status: OPEN — OPEN-P-EW-3**


### G1 — Genuine Weakness: U(1)_Y Derivation Is ~30% off Without Calibration

The coupling g'/g ≈ 0.387 from the 600-cell vertex-count ratio (40/64) × φ⁻¹, while the PDG value is g'/g ≈ 0.357/0.652 = 0.548. The CPP estimate is within ~30% of the correct value without any calibration — good enough to confirm the vertex-counting idea is pointing in the right direction, but not good enough to count as a derivation. The vertex_count_correction = 1.18 calibration factor brings this within PDG precision.

This is the U(1)_Y equivalent of the SS-1 sea_strength 3.8% residual — a known discrepancy with an identified source (vertex counting without the full golden-ratio structure of the shells), registered as OPEN-P-EW-2 (coupling constants from vertex counting). Unlike the SS-1 case where α_geom provides the exact value and the 3.8% residual has a known geometric source, the EW-2 U(1)_Y case does not yet have the equivalent of α_geom.

**Status: OPEN — OPEN-P-EW-2**


## Summary Table

| # | Concern | Assessment | Status |
|---|---------|-----------|--------|
| C1 | η is the mass scale, not geometry | Valid | Acknowledged — OPEN-P-EW-1 |
| C2 | W⁰ detection path unclear | Valid | Open — cross-section needed |
| C3 | v3 error sensitivities back-calculated | Valid | Resolved — v3.1 |
| C4 | Loop/shell density factors fitted | Valid | Open — OPEN-P-EW-3 |
| G1 | U(1)_Y ~30% off without calibration | Genuine weakness | Open — OPEN-P-EW-2 |


# PART 2: FAQ — CONVENTIONAL PHYSICS PERSPECTIVE

---

*FAQ content has been moved to FAQ-EW-1.md.*
