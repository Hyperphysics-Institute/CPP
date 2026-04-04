# FAQ — SM-7: The Heavy Quark Mass Spectrum and Strong Coupling from 600-Cell Lattice Geometry

**Paper:** SM-7_heavy_quark_mass_spectrum.tex (v2.2)
**Last updated:** 3 April 2026 (verified against .tex on GitHub)

*Frequently asked questions, organised by category. Each answer is
self-contained for standalone use (e.g., on the Hyperphysics website).*

---

## Category A: The Strong Coupling

### Q1: How does SM-7 derive α_s?

SM-7 defines the strong coupling as the fraction of total lattice mode
walks carried by face-circulation modes, weighted by the propagation
efficiency η = 1/φ. The 600-cell adjacency matrix has ℰ = 1440 edge-mode
walks and ℱ = 2400 face-circulation walks, totalling N = 3840. The strong
coupling is α_s = (η × ℱ)/N = (1/φ) × 2400/3840 = 5/(8φ) ≈ 0.3863.
No free parameters enter the calculation.

### Q2: Is 0.386 really the strong coupling? The PDG says 0.118.

Both values are correct at different energy scales. The PDG value 0.1179
is the running coupling at the Z mass (91 GeV). SM-7's 0.386 is the bare
cage-scale coupling. At the charm mass (~1.3 GeV), the running α_s is
approximately 0.35–0.40, consistent with SM-7's value. Connecting the
bare value to α_s(M_Z) via CPP renormalisation-group running is an open
problem (OPEN-P-SM-7-1). SS-1's β₀ = 7 governs the CPP version of
asymptotic freedom.

### Q3: What is the coupling sum rule?

sin²θ_W + α_s = 1/φ, where φ is the golden ratio. In plain terms:
every vacuum mode in the 600-cell lattice is either an edge mode or a
face mode (bare fractions 3/8 + 5/8 = 1). Both are reduced by the
propagation efficiency 1/φ. The golden ratio appears because the 600-cell
is an icosahedral polytope. No existing theory predicts this sum rule.

### Q4: Does the sum rule mean the forces are unified?

No — the opposite. GUTs predict forces merge at high energy. CPP's sum
rule says they are permanently distinct (edges vs faces are different
geometric objects). The sum rule is a budget constraint, not a convergence.
The coupling ratio α_s/sin²θ_W = 5/3 is exact at all scales.

---

## Category B: Quark Masses

### Q5: How does the quark mass formula work?

SM-7 derives the quark Koide phase θ = 124.035° from the combined EW +
colour ε-shift on the K₃ cage. The masses then follow from the standard
Koide parametrisation: √m_i = (S/3)(1 + √2 cos(θ + 2πi/3)). One
calibration input: m_c = 1.27 GeV. The formula predicts m_b = 4.24 GeV
(1.4% from PDG) and m_t = 169.8 GeV (1.7% from PDG). Zero shape parameters.

### Q6: Why does the quark Koide phase differ from the lepton phase?

Both phases have the form cos θ = −(2/3)(1 + n/(104φ)). For leptons,
n = +3 (EW shift on 2 internal bonds, repulsive). For quarks, n = −27
(EW + colour shift on 2 + 12 bonds, with the attractive colour term
overwhelming the repulsive EW term). The ratio −27/+3 = −9 comes from
12 colour bonds × (5/3) coupling ratio = 20 EW-equivalent bonds,
minus 2 EW bonds = 18 net, 18/2 = 9.

### Q7: Why doesn't the formula work for light quarks (u, d, s)?

Light quark masses are dominated by the chiral condensate — the vacuum
energy of the strong force. The up and down quarks get almost all their
apparent mass from confinement, not from the ε-shift mechanism. SM-7 is
explicit about this limitation: the framework applies to quarks whose mass
is well above Λ_QCD ≈ 200 MeV.

### Q8: Is the 1.7% top mass error a problem?

It is an honest flag. Possible sources: (a) pole-vs-MS-bar scheme
ambiguity (the top is the only quark quoted as a pole mass); (b) the
top is the only quark above the EW scale and may need additional
corrections; (c) the bond-count factor z = 12 may receive small
corrections for the top. The paper notes these possibilities without
claiming resolution (§9, point 6).

---

## Category C: Relation to the Standard Model

### Q9: How does this compare to the SM's treatment?

The SM treats each quark mass as an independent free parameter (Yukawa
coupling). Combined with SM-6, CPP replaces 8 independent SM parameters
(6 Yukawa couplings + sin²θ_W + α_s) with 2 calibration constants
(m_e, m_c) and 0 shape parameters, predicting the remaining 8 quantities.

### Q10: Does SM-7 replace QCD?

No. QCD describes strong force dynamics — jets, decays, cross sections.
SM-7 derives two quantities that QCD takes as inputs: the strong coupling
and the quark masses. SM-7 is upstream of QCD.

### Q11: What would disprove SM-7?

Several things: (a) a precision measurement showing α_s/sin²θ_W ≠ 5/3;
(b) K₃ eigenvalue ratio failing with improved PDG values; (c) a
mathematical error in the spectral trace calculation; (d) a rigorous
derivation of the bond factor giving z ≠ 12. The attack surface (§9)
identifies these explicitly.

---

## Category D: Development Process

### Q12: How was SM-7 developed?

Written in a single intensive session (2–3 April 2026). Five versions
(v1 → v2.2) incorporating six reviews from three AI systems. The
face-mode insight emerged when SM-6's edge-mode framework was combined
with SS-1's face → colour identification. The displacement-circulation
mechanism (Axiom A7) was discovered during the v2.1 → v2.2 cycle.

### Q13: What did the AI reviewers contribute?

Grok: recommended "mode complementarity" framing, flagged SS-1 dependency,
identified the β₀ = 7 connection. Copilot: provided the projector lemma
(Lemma 5.1), tightened assumptions S1–S4, named Axioms A6/A7. Sonnet:
served as hostile referee with REJECT recommendation and 10 objections
(3 valid and incorporated, 4 partial, 3 rejected). Full records in
reviews-SM-7.md and response-to-sonnet-SM-7.md.

---

## Category E: Future Directions

### Q14: What comes after SM-7?

Three natural extensions: (a) light quark masses via CPP chiral symmetry
breaking; (b) CKM mixing matrix from quark K₃ eigenvector misalignment;
(c) connecting bare α_s to running α_s(M_Z) via CPP RG mechanism.

### Q15: What is the Walk-Dimension Gauge Principle?

The single structural principle underlying both Axioms A6 and A7: the
dimensionality of the lattice walk determines whether the gauge structure
is abelian or non-abelian. 1D walks (edges) → commutative → U(1). 2D
walks (face loops) → non-commutative → SU(3). If this principle withstands
scrutiny, it answers why the Standard Model has the gauge group it has.

---

*FAQ prepared by Claude Opus (Anthropic), 3 April 2026 MDT.
Verified against SM-7_heavy_quark_mass_spectrum.tex (v2.2) on GitHub.*
