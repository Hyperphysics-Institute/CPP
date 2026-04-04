# Glossary — SM-7: The Heavy Quark Mass Spectrum and Strong Coupling from 600-Cell Lattice Geometry

**Paper:** SM-7_heavy_quark_mass_spectrum.tex (v2.2)
**Last updated:** 3 April 2026 (verified against .tex on GitHub)

*This glossary defines every technical term introduced or given specialised
meaning in SM-7. For terms inherited from earlier papers, see the glossaries
for SM-1 (cage binding), SM-3 (K₃ spectral theorem), and SM-6 (charged
lepton masses). Cross-references are in [brackets].*

---

## 1. Mode-Counting and Coupling Terms

**Edge mode (edge-mode walk).**
A closed walk of length 2 on the 600-cell adjacency graph — traversing a
single edge out and back. The count is ℰ = Tr(A²) = 2E = 1440, where
E = 720 is the edge count. Edge modes correspond to the abelian electroweak
sector (U(1)_Y / EM), as established in SM-6. [Assumption S1.]

**Face-circulation mode (face-mode walk).**
A closed walk of length 3 on the 600-cell adjacency graph — traversing a
triangular face. The count is ℱ = Tr(A³)/3 = 2F = 2400, where F = 1200
is the face count. Face-circulation modes correspond to the non-abelian
colour sector (SU(3)_c), as established in SS-1. [Assumption S2; Axiom A7.]

**Total mode count (N).**
N = ℰ + ℱ = 1440 + 2400 = 3840. The denominator in both the Weinberg angle
and strong coupling definitions. [Assumption S1.]

**Mode fraction.**
The share of N carried by a given mode type, weighted by the propagation
efficiency η = 1/φ. Edge-mode fraction → sin²θ_W = 3/(8φ). Face-mode
fraction → α_s = 5/(8φ).

**Face-mode fraction (α_s).**
The strong coupling as defined operationally in CPP (Definition 4.1):

    α_s ≡ (η × ℱ) / N = (1/φ) × 2400/3840 = 5/(8φ) ≈ 0.3863

The bare (topological) fraction is ℱ/N = 5/8; the physical coupling is
5/8 reduced by η = 1/φ.

**Propagation efficiency (η).**
η = l_edge / R_circ = 1/φ, from SR-1 (SSV/PSR metric correction). Both
sin²θ_W and α_s are reduced by this common factor. [Assumption S3.]

**Mode complementarity.**
Edge and face modes partition the total mode capacity at the cage scale.
Bare level: 3/8 + 5/8 = 1 (every vacuum mode is either edge or face).
Physical level: sin²θ_W + α_s = 1/φ. This is a partition identity, not
GUT-scale unification. [Corollary 4.4; Remark 4.5.]

**Coupling ratio.**
α_s / sin²θ_W = ℱ/ℰ = F/E = 1200/720 = 5/3. A topological invariant
preserved by any metric operator satisfying S4. Does not run with energy
scale. [Corollary 4.3.]

**Coupling sum rule.**
sin²θ_W + α_s = 1/φ ≈ 0.6180. [Corollary 4.4.]

---

## 2. Explicit Assumptions (§2)

**S1 (600-cell adjacency and traces).** Defines ℰ = 1440, ℱ = 2400, N = 3840.
**S2 (Mode–sector identification).** Edge → EW (SM-6). Face → colour (SS-1).
**S3 (Propagation efficiency).** η = 1/φ weights both mode fractions.
**S4 (Metric compatibility).** Metric preserves the ratio F/E = 5/3.

---

## 3. Physical Axioms for Gauge Structure (§3, v2.2)

**Axiom A6: Edge Abelianity — Electromagnetic Sector.**
Edge-based interactions are one-dimensional transport along qDP bond chains.
Single scalar degree of freedom per step. Path composition is commutative:
U(γ₁)U(γ₂) = U(γ₂)U(γ₁). Realises abelian gauge structure (U(1)-type).
Physically: linear push–pull force, no internal orientation, no route memory.

**Axiom A7: Face-Bond Circulation — Strong Sector.**
Face-based interactions are displacement propagation on the three qDP bonds
forming a closed triangular K₃ loop. Tensioning one bond generates a
circulating pulse through the shared vertices. Eight independent standing-wave
patterns (analogous to the eight Gell-Mann matrices). Order-dependent because
each vertex response depends on the SSV_abs local frame modified by the
preceding pulse: U(γ₁)U(γ₂) ≠ U(γ₂)U(γ₁). Non-abelian gauge structure
(SU(3)-type). Energy confined within the loop until transferred or broken
(hadronisation).

**Walk-Dimension Gauge Principle (Remark 3.3).**
Walk dimensionality determines commutativity. 1D edge chains → commutative.
2D face loops → non-commutative (Lorentzian frame shift between steps).

---

## 4. Projector Lemma Terms (§5)

**Projector lemma (Lemma 5.1).**
Derives bond-count asymmetry (2 EW vs 12 colour) from projector structure.
Uses P_C (vertex projector onto K₃ cage, |C| = 3), P_E (edge-mode projector),
P_F (face-mode projector).

**A1 (Edge locality).** Σ_EW = P_C P_E A P_E† P_C† has support on internal
K₃ edges only. → 2 internal bonds per K₃ vertex.

**A2 (Face saturation).** Σ_S = P_C P_F A P_F† P_C† has support on all
bonds incident to each K₃ vertex. → All z = 12 bonds per K₃ vertex.

---

## 5. Koide Phase and Mass Terms (§6–7)

**Isotropic shift (ε).** Net perturbation to K₃ eigenvalues (Theorem 6.1):

    ε = (2 sin²θ_W − z α_s) / (z + 1) = −27/(52φ) ≈ −0.3209

Components: +2 sin²θ_W (repulsive EW, 2 bonds), −z α_s = −12 × 5/(8φ)
(attractive colour, 12 bonds), z + 1 = 13 (normalisation).

**Quark Koide phase (θ_quark).** cos θ_quark = −(2/3)(1 − 27/(104φ)),
θ = 124.035°. PDG: 124.09°, agreement 0.048%.

**The n-notation.** cos θ = −(2/3)(1 + n/(104φ)). Leptons: n = +3.
Quarks: n = −27. Ratio −9 = (12 × 5/3 − 2)/2.

**Koide parametrisation.** √m_i = (S/3)(1 + √2 cos(θ + 2πi/3)),
calibrated to m_c = 1.27 GeV (MS-bar at m_c). Predicts m_b = 4.24 GeV
(PDG 4.18, 1.4%), m_t = 169.8 GeV (PDG 172.7, 1.7%).

**Multi-channel isotropy (Remark 6.2).** Combined ε = ε_EW + ε_S inherits
isotropy from THEO-SM-5: antibonding degeneracy preserved.

**Mutual reinforcement.** α_s from quark Koide phase inversion = 0.383;
from lattice face-mode counting = 0.386. Agreement 0.7%, no shared
calibration.

---

## 6. Scheme Terms

**Bare coupling vs running coupling.** SM-7's 0.386 = bare cage-scale value.
PDG α_s(M_Z) = 0.1179. SM-7's value consistent with α_s(m_c) ≈ 0.35–0.40.
CPP RG running: OPEN-P-SM-7-1. SS-1's β₀ = 7 governs CPP asymptotic freedom.

**MS-bar vs pole mass.** SM-7 uses MS-bar (c, b at respective scales) and
pole (top, PDG convention). Best Koide fit is MS-bar at respective scales
(Appendix B, Table 4).

---

## 7. Open Problems

**OPEN-P-SM-7-1:** RG running — connecting bare α_s = 0.386 to α_s(M_Z) = 0.118.
**OPEN-P-SM-7-2:** Rigorous face saturation — constructing Σ_S from 600-cell
Green's function (analogous to THEO-SM-5 isotropy proof in SM-6).

---

*Glossary prepared by Claude Opus (Anthropic), 3 April 2026 MDT.
Verified against SM-7_heavy_quark_mass_spectrum.tex (v2.2) on GitHub.*
