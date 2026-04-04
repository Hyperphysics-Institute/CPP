# Philosophy — SM-7: The Heavy Quark Mass Spectrum and Strong Coupling from 600-Cell Lattice Geometry

**Paper:** SM-7_heavy_quark_mass_spectrum.tex (v2.2)
**Last updated:** 3 April 2026 (verified against .tex on GitHub)

*Examines the conceptual content of SM-7 — what kind of explanation it
offers, what philosophical commitments it carries, where it is strong,
and where it is honest about weakness.*

---

## 1. What Kind of Paper Is SM-7?

SM-7 is a **derivation paper with empirical confirmation**: it derives
α_s from 600-cell face geometry, derives the quark Koide phase from the
combined EW + colour ε-shift, and checks both against PDG data.

The paper also contains a **structural discovery**: the coupling sum rule
sin²θ_W + α_s = 1/φ and the coupling ratio 5/3. These were not predicted
in advance — they emerged when the face-mode calculation was compared to
the earlier edge-mode result. This genuine surprise is absent in SM-6.

SM-7 introduces **physical axioms** (A6 Edge Abelianity, A7 Face-Bond
Circulation, and the Walk-Dimension Gauge Principle) with implications
beyond the strong sector. These claim that the Standard Model gauge group
SU(3) × SU(2) × U(1) is determined by the topology of the lattice walks.
This is the most philosophically significant content of the paper.

---

## 2. Proposition Maturity Classification

**Theorem-level (T):**
- Coupling ratio α_s/sin²θ_W = 5/3 [Corollary 4.3]. Pure graph combinatorics.
- α_s = 5/(8φ) [Theorem 4.2]. Follows from S1–S3.
- Sum rule sin²θ_W + α_s = 1/φ [Corollary 4.4]. Arithmetic.

**Corollary-level (C):**
- Quark Koide phase cos θ = −(2/3)(1 − 27/(104φ)) [Theorem 6.1].
  Follows from the ε-shift formula given A1, A2, and the coupling values.
- Multi-channel isotropy [Remark 6.2]. Inherits from THEO-SM-5.

**Proposition-level (P):**
- The projector lemma (Lemma 5.1). Structurally sound, but A2 (face
  saturation) has a proof sketch rather than a fully rigorous construction.
  Registered as OPEN-P-SM-7-2.
- Axiom A7 (Face-Bond Circulation). Physically intuitive and consistent
  with the SU(3) algebra proved in SS-1, but formulated as an axiom
  rather than derived from more primitive CPP postulates.

**Conjecture-level (J):**
- The bare α_s = 0.386 connects to α_s(M_Z) = 0.118 via CPP RG running
  (OPEN-P-SM-7-1).

---

## 3. What SM-7 Does Well

**Parameter reduction.** SM-6 + SM-7 together: 2 calibration constants
(m_e, m_c) and 0 shape parameters → 2 coupling constants + 6 fermion
masses. The Standard Model needs 8 independent parameters. This is the
single most important metric for a theory-of-everything candidate.

**Internal consistency.** Mutual reinforcement (0.7% agreement between
two independent α_s determinations) is the gold-standard test.

**Surprise predictions.** The sum rule and coupling ratio were not designed.
They emerged from the calculation and turned out to be simple expressions
in φ — the hallmark of discovering structure rather than fitting parameters.

**Honest axiomatics.** The v2.2 Physical Axioms block (§3) makes the
logical structure explicit. Assumptions S1–S4, Axioms A6–A7, and
the projector assumptions A1–A2 are all clearly labelled. The attack
surface (§9) identifies exactly where to push.

---

## 4. What SM-7 Does Not Do (Honest Weaknesses)

**A2 (face saturation) has a proof sketch, not a proof.** The claim that
Σ_S has support on all z = 12 incident bonds rests on a physical argument
about face-mode coverage. A rigorous proof requires constructing Σ_S from
the 600-cell Green's function (OPEN-P-SM-7-2). The paper is explicit
about this: §9 calls A2 "the weakest link."

**No RG running.** SM-7's bare coupling is 0.386; the PDG value at M_Z
is 0.118. The CPP version of asymptotic freedom (β₀ = 7 from SS-1) has
not been connected to the standard running. This is OPEN-P-SM-7-1.

**Light quarks are out of scope.** The ε-shift framework applies only to
quarks whose mass is well above Λ_QCD. The light quarks (u, d, s) are
chiral-condensate dominated. SM-7 is honest about this limitation.

**The 1.7% top mass discrepancy.** Small enough for scheme ambiguity,
large enough to be real. The top is unique — the only quark above the
EW scale, the only one that decays before hadronising. Whether this
signals new physics or convention is flagged but unresolved.

**Mass scheme dependence.** The Koide ratio and phase are scheme-dependent
for quarks (Appendix B). The MS-bar scheme at respective quark scales
gives the best match, which is consistent with the interpretation but not
independently derived.

---

## 5. Philosophical Significance

### 5.1 The gauge group problem

The deepest question in particle physics: why SU(3) × SU(2) × U(1)?
The Standard Model treats this as empirical input. GUTs embed it in a
larger group but must explain the breaking pattern.

SM-7's Axioms A6–A7 and the Walk-Dimension Gauge Principle offer a
structural answer: the gauge group is determined by the topology of
the lattice walks. 1D walks → abelian. 2D walks → non-abelian. The
gauge group is a property of the geometry, not a symmetry of the laws.

### 5.2 Mode complementarity vs grand unification

The sum rule sin²θ_W + α_s = 1/φ resembles unification but has opposite
conceptual content. In GUTs, forces merge. In CPP, forces are permanently
distinct (edges and faces cannot be deformed into each other). The sum
rule is a budget constraint, not a convergence. The coupling ratio 5/3
is exact at all scales — testable with precision measurement.

### 5.3 The ε-shift as universal mechanism

SM-6 and SM-7 use the same mechanism — isotropic perturbation of K₃
eigenvalues — to determine both lepton and quark mass spectra. The only
difference is which forces participate and on how many bonds. This
structural unity, with the common form cos θ = −(2/3)(1 + n/(104φ)),
is the strongest argument that the 600-cell lattice is tracking something
real about nature.

---

*Philosophy file prepared by Claude Opus (Anthropic), 3 April 2026 MDT.
Verified against SM-7_heavy_quark_mass_spectrum.tex (v2.2) on GitHub.*
