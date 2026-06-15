# SF-3 v0.4 — Review: adversarial line-by-line pass

**Reviewer:** panel adversarial pass (labelled Copilot in Thomas's relay; inline-recompute style) · **Verdict:** ready after 3 small "blocking" framing fixes · **Date:** 14 June 2026 · **Reviewed:** sf-3_quarks.tex v0.4

---

**1. Fidelity — mostly faithful, two residual over-claims.**
- (A) Generation count: SM-8 presents antipodal identification as the mechanism that *limits* shells; it does not prove uniqueness/inevitability in a strict mathematical sense. "Selected by the mechanism" is better than "forced" but still slightly over-strong. Recommend "selected within the SM-8 lattice-identification model" / "under the SM-8 antipodal-identification assumption."
- (B) "One spectral trace gives both couplings": SM-6 treats the edge-mode fraction as a *candidate* for sin^2 theta_W, SM-7 the face-mode fraction as a *candidate* for alpha_s; neither claims a necessary/unique mapping. v0.4 wording improved ("within the inherited SM-6/SM-7 framework") but should add that these are *structural correspondences*, not derived gauge couplings (RGE).
- (C) SM-10 representation: faithful.

**2. Proposition 5.1 — true, with one nuance to state.** Koide parametrisation m_i = A_q(1 + sqrt2 cos(theta + 2pi i/3)); the isotropic shift modifies theta, not A_q; A_q cancels from the cos-theta ratio; shift uses only z, alpha_s, sin^2 theta_W. Therefore theta_quark is independent of m_c — PROVIDED alpha_s is the structural value 5/(8 phi). **If alpha_s were taken from a PDG running-coupling fit at m_c, m_c would re-enter indirectly.** SF-3 adopts the structural alpha_s, so independence holds. Recommend stating this nuance explicitly.

**3. Single-m_e calibration — clean, with caveats to acknowledge.** z*C_F inherited (not tunable); PDG scheme affects comparison only; the only subtlety is the MeV scale via the lattice-scale grounding axiom identifying the electron cage with the physical electron — the *same* calibration as SF-1/SF-4. Recommend a one-sentence MeV-scale clarification in the ledger.

**4. Numbers — right.** RMS = sqrt[(3.1^2+1.6^2+1.6^2+1.8^2)/4] = 2.12% (paper 2.1%, correct); 3/(8 phi)=0.2319, 5/(8 phi)=0.3865, sum 0.6184 vs 1/phi 0.6180 (within rounding); eps=-27/(52 phi)=-0.3217, cos=-0.55943, theta=124.05 deg (paper 124.04, correct to rounding).

**5. CKM / delta_CP — honest.** "Parallel of posture, not difficulty"; 7/8 vs masses+generation; both leave a mixing-sector CP observable open. Accurate and safe.

**Additional v0.4 issues:** "zero-parameter prediction" used many times — true for masses and Koide phase, but alpha_s = 5/(8 phi) and sin^2 theta_W = 3/(8 phi) are *structural values*, not empirical-fit predictions; avoid implying first-principles RGE derivation. The "macroscopic shadow" paragraph is rhetorically strong; consider "within the CPP ontology."

**Blocking (before v0.5):** (1) soften "selected by" -> "selected within the SM-8 antipodal-identification model"; (2) state the alpha_s-structural nuance on Prop 5.1; (3) clarify the spectral-trace mapping is a structural correspondence, not a dynamical unification. **Non-blocking:** MeV-scale clarification; "within the CPP ontology" on the macroscopic-shadow paragraph; optional SM-7 isotropic-shift appendix.
