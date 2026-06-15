# SF-3 v0.1 — Review: Copilot

**Reviewer:** Copilot (Microsoft) · **Verdict:** No structural blocker; fix 5 framing items before multi-AI panel · **Date:** 14 June 2026 · **Reviewed:** sf-3_quarks.tex v0.1 (question-by-question adversarial pass)

---

**1. Fidelity to SM-7/8/9/10 and SS-1/2.** Structurally faithful, but a couple of phrases skate close to over-claim. Mass formula + 7/3 exponent + M_0 correctly attributed to SM-8/SM-9 (not re-derived). alpha_s, sin^2 theta_W, complementarity presented as inherited from SM-6/7. C_F=4/3 and z*C_F top relay treated as structural outputs of SS-1/2, not knobs.
- Over-reach 1: abstract opens "the complete quark mass spectrum ... follow from a single calibration," but the body is explicitly about the FOUR heavy quarks; light u,d excluded. Fix: "complete quark mass spectrum" -> "heavy-quark mass spectrum" (abstract + conclusion).
- Over-reach 2: "substrate-level electroweak–strong unification" is rhetorically strong for a shared spectral partition. Call it a "shared geometric origin" or "mode complementarity"; reserve "unification" for a dynamical mechanism.

**2. Proposition 5.1 — algebraically true inside SF-3.** Given z fixed by the 600-cell and alpha_s, sin^2 theta_W purely geometric, theta_quark depends only on {alpha_s, sin^2 theta_W, z}. Subtle historical question: did SM-7 sneak m_c into alpha_s or the phase by fitting to a PDG-mass-extracted phase? If so there is indirect m_c dependence in the original route. Recommendation: add a sentence cross-referencing the exact SM-7 equations where (i) alpha_s = 5/(8 phi) is obtained without PDG masses and (ii) the phase shift is written purely in terms of alpha_s, sin^2 theta_W, z. That closes the loophole.

**3. Single-m_e calibration — clean, with caveats.** Only dimensionful input to the predictions is m_e (M_0 = m_e z/phi ~ 3.79 MeV). z, phi, C_F, V, z*C_F treated as derived. Skeptic's pokes: is z*C_F truly derived or a post-hoc choice? (programme-level, inherited from SM-8, not SF-3's job — but worth one acknowledging sentence). PDG scheme only for comparison (safe). SM-10's 4 fit params don't enter Table 1 (honest). Letter of "one dimensionful calibration, zero shape parameters" satisfied; spirit depends on how uniquely SM-8/9/SS-2 fix 7/3 and z*C_F — add a sentence noting these are inherited structural choices, not re-argued.

**4. Numerical checks — match.** Verified against 1500_verify_sf3_core.py: M_0 = 3.79 MeV; masses + RMS 2.10%; alpha_s = 5/(8 phi); sin^2 theta_W = 3/(8 phi); sum = 1/phi; ratio = 5/3 = F/E; theta_quark = 124.04 deg. ALL CHECKS PASS. No red flags.

**5. CKM-open / delta_CP-parallel — honest rather than inflated.** A parallel of posture, not a claim SF-4 did more than it did. One of the more honest parts of the paper.

**Would not block v0.1 -> review on anything structural, but fix before the panel:** (1) "complete quark mass spectrum" -> "heavy-quark mass spectrum"; (2) make Prop 5.1's SM-7 provenance explicit; (3) soften "electroweak–strong unification" -> "mode complementarity from a single spectral trace"; (4) versioning consistency (title says v0.1 while changelog/patch note mention v1.0 — pick one and make .tex header and changelog agree); (5) one sentence that 7/3 and z*C_F are inherited from SM-8/9/SS-2, not re-tuned. With those, SF-3 reads as a sharp, honest synthesis with one real new conceptual move, not a stealth derivation paper.
