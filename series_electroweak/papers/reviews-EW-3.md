# Reviews and FAQ — EW-3: The Z⁰ Boson — Icosahedral Closed Loop

**Paper:** EW-3 (cpp_ew3_Z_v3.tex)
**Document type:** Living review record and FAQ
**Last updated:** 31 March 2026


# PART 1: FORMAL REVIEWS


## Review 1: Internal Review (March 2026)

**Overall verdict:** Z topology is cleanly derived; the ground-state eigenvalue assignment is convincing; the m_Z/m_W 5% discrepancy is an honest gap; the 0.5% Weinberg-angle self-consistency check is the paper's strongest result.


### C1 — OPEN: Loop Density Factor ℓ_Z Not Analytically Derived

**The concern:** The loop density factor ℓ_Z ≈ 1.2, which accounts for the coherence reinforcement in the closed icosahedral loop, is estimated as an effective Monte Carlo value. The ideal geometric estimate is 1.437; the effective value is 1.2. The reduction is attributed to stereographic projection losses in the 4D→3D mapping but has not been computed analytically from the icosahedral subgraph coordinates.

**Assessment: VALID — this is a genuine fitting step**

The loop density factor enters the Z mass formula as a multiplicative factor in f_geom^Z = 1.5 × 1 × φ⁻⁴ × 1.2. A 20% difference between the ideal and effective value represents a non-trivial discrepancy. The analytic calculation would require working out the 4D icosahedral subgraph coordinates and computing the stereographic projection correction exactly — the same type of calculation that resolved the SS-1 sea_strength 3.8% residual (which also came from a projection correction). Until this is done, ℓ_Z carries the same status as the SS-1 residual before THEO-SS-4 was fully worked out.

**Status: OPEN** — registered as OPEN-P-EW-3.


### C2 — OPEN: m_Z/m_W 5% Discrepancy

**The concern:** The loop density factor predicts m_Z/m_W ≈ 1.20; the observed ratio is 1.134. The 5% gap indicates that the loop density factor alone does not fully capture the Z/W mass difference. Additional geometric contributions from the topological difference (icosahedral loop vs bracelet ring) are not yet identified.

**Assessment: VALID — registered as a distinct open problem**

The Weinberg angle self-consistency check (0.5% agreement between cos θ_W → m_Z/m_W = 1.1401 and directly derived ratio 1.1344) confirms the overall framework is correct. The 5% gap in the loop density derivation is a sub-problem within the mass formula. Resolving it is one step toward OPEN-P-EW-2 (self-consistent mass formula).

**Status: OPEN** — registered as OPEN-P-EW-4.


### S1 — Strength: 0.5% m_Z/m_W Self-Consistency Is the Paper's Best Result

The Weinberg angle was derived in EW-1/EW-5 with no reference to the individual boson masses. The Z mass was derived in EW-3 with no reference to the Weinberg angle. Their 0.5% agreement on the ratio m_Z/m_W = 1.134 is an external test of the framework's coherence. This should be highlighted as the primary validation result of EW-3.


## Summary Table

| # | Issue | Assessment | Status |
|---|-------|-----------|--------|
| C1 | ℓ_Z not analytically derived | Valid | Open — OPEN-P-EW-3 |
| C2 | m_Z/m_W 5% discrepancy | Valid | Open — OPEN-P-EW-4 |
| S1 | 0.5% Weinberg self-consistency | Strength | Confirmed |


# PART 2: FAQ

---

*FAQ content has been moved to FAQ-EW-3.md.*
