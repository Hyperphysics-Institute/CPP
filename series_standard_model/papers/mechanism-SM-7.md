# Mechanism — SM-7: The Heavy Quark Mass Spectrum and Strong Coupling from 600-Cell Lattice Geometry

**Paper:** SM-7_heavy_quark_mass_spectrum.tex (v2.2)
**Last updated:** 3 April 2026 (verified against .tex on GitHub)

*Sequential cause-and-effect account of the physical mechanisms in SM-7.
For term definitions see glossary-SM-7.md; for proofs see the paper.
Section numbers in [brackets] reference the paper.*

---

## Overview

SM-7 answers two questions: What determines the strength of the strong
force? What determines the masses of the heavy quarks? Both answers emerge
from the face geometry of the 600-cell, through the same spectral trace
formula that SM-6 used for the Weinberg angle.

The paper has four stages: (1) physical axioms explaining why edges are
abelian and faces are non-abelian, (2) face-mode counting → α_s,
(3) the projector lemma → bond-count asymmetry, (4) the combined
ε-shift → quark Koide phase → mass predictions.

---

## Stage 1: Why Edges Are Abelian and Faces Are Non-Abelian [§3]

Before counting modes, SM-7 establishes the physical reason that edges
carry U(1) and faces carry SU(3). This is the content of Axioms A6 and A7.

**Axiom A6 (Edge Abelianity).** An edge is a one-dimensional object. A qDP
bond transport along an edge changes one scalar degree of freedom (bond
tension). Reversing the path undoes the transport. Composition of any two
paths between the same endpoints is commutative. This realises U(1).

**Axiom A7 (Face-Bond Circulation).** A triangular face is a two-dimensional
closed loop of three qDP bonds. Tensioning one bond generates a displacement
pulse that circulates through the shared vertices. The key physics: each
vertex response depends on the instantaneous SSV_abs local frame, which
has already been modified by the preceding pulse. Successive displacements
are therefore order-dependent, realising SU(3). The eight independent
standing-wave patterns on the triangle correspond to the eight Gell-Mann
matrices.

**The Walk-Dimension Gauge Principle (Remark 3.3)** unifies both: the
dimensionality of the lattice walk determines commutativity. 1D → abelian.
2D → non-abelian.

---

## Stage 2: Face-Mode Counting → α_s [§2, §4]

### Step 2.1 — The 600-cell spectral traces

The 600-cell adjacency matrix A defines two mode counts [§2, Assumption S1]:

- ℰ = Tr(A²) = 2E = 1440 (edge-mode walks)
- ℱ = Tr(A³)/3 = 2F = 2400 (face-circulation walks)
- N = ℰ + ℱ = 3840 (total mode count)

### Step 2.2 — The strong coupling as face-mode fraction

By analogy with SM-6's sin²θ_W = (η × ℰ)/N, the strong coupling is
defined as [Definition 4.1]:

    α_s ≡ (η × ℱ) / N

where η = 1/φ is the universal propagation efficiency (Assumption S3).
Substituting: α_s = (1/φ) × 2400/3840 = 5/(8φ) ≈ 0.3863 [Theorem 4.2].

### Step 2.3 — Mode complementarity

Two corollaries follow immediately:

**Coupling ratio** [Corollary 4.3]: α_s / sin²θ_W = ℱ/ℰ = F/E = 5/3.
This is a topological invariant — it depends only on face and edge counts,
not on the metric or energy scale.

**Sum rule** [Corollary 4.4]: sin²θ_W + α_s = 3/(8φ) + 5/(8φ) = 1/φ.
At the bare level, 3/8 + 5/8 = 1: every vacuum mode is either edge or
face. Both sectors are reduced by the same η, giving total 1/φ.

This is mode complementarity, not GUT unification [Remark 4.5]. The
bare values are 3/8 and 5/8 (not equal). The sum rule is a partition
identity.

---

## Stage 3: The Projector Lemma — 2 vs 12 Bonds [§5]

### Step 3.1 — Why the bond counts differ

The key distinction between leptons and quarks is the number of K₃ cage
bonds affected by each force. The projector lemma (Lemma 5.1) derives
this from two assumptions about the self-energy operators:

**A1 (Edge locality):** The EW self-energy Σ_EW = P_C P_E A P_E† P_C†
has support on internal K₃ edges only. Edge modes live on individual
edges; the only edges connecting two cage vertices are the 2 internal
bonds. → EW correction acts on 2 bonds.

**A2 (Face saturation):** The strong self-energy Σ_S = P_C P_F A P_F† P_C†
has support on all bonds incident to K₃ vertices. Face-circulation modes
touching a K₃ vertex use one of the z = 12 incident bonds; summing over
all such modes touches every bond without exception. → Colour correction
acts on all 12 bonds.

### Step 3.2 — Physical interpretation

Edge modes are 1D transports (Axiom A6) — they couple only to internal
bonds. Face-circulation modes are 2D transports (Axiom A7) — displacement
pulses propagate around closed loops, touching every incident bond. The
factor-of-6 bond difference is the Walk-Dimension Gauge Principle applied
to the 600-cell adjacency.

---

## Stage 4: The Quark Koide Phase → Mass Predictions [§6–7]

### Step 4.1 — The combined ε-shift

The net isotropic shift on a quark K₃ face is [Theorem 6.1]:

    ε = (2 sin²θ_W − z α_s) / (z + 1)
      = (6/(8φ) − 60/(8φ)) / 13
      = −54/(104φ) = −27/(52φ)

The three terms: +2 sin²θ_W (repulsive EW on 2 bonds from Lemma 5.1a),
−12 α_s (attractive colour on 12 bonds from Lemma 5.1b), and z + 1 = 13
(closed-neighbourhood normalisation, same as SM-6).

### Step 4.2 — The quark Koide phase

cos θ_quark = −(2/3)(1 − 27/(104φ)) ≈ −0.5597, giving θ = 124.035°.
PDG value: 124.09°, agreement 0.048%.

The lepton–quark comparison: both have the form cos θ = −(2/3)(1 + n/(104φ)).
Leptons: n = +3. Quarks: n = −27. The ratio −9 has a transparent physical
origin: 12 × (5/3) = 20 colour bonds in EW-equivalent units, minus 2 EW
bonds = 18, and 18/2 = 9.

### Step 4.3 — Mass predictions

Using the standard Koide parametrisation with θ = 124.035° and calibrating
to m_c = 1.27 GeV (the single quark-sector input):

    √m_i = (S/3)(1 + √2 cos(θ + 2πi/3))

Predictions: m_b = 4.24 GeV (PDG 4.18, 1.4%), m_t = 169.8 GeV (PDG 172.7,
1.7%). Less precise than leptons (1–2% vs 0.15–0.18%) because quark masses
are scheme-dependent.

### Step 4.4 — Mutual reinforcement

α_s extracted from the observed quark Koide phase: 0.383. From face-mode
counting: 0.386. Agreement: 0.7%, no shared calibration.

---

## What SM-7 Depends On

| Paper | What SM-7 inherits |
|-------|--------------------|
| SM-6  | sin²θ_W = 3/(8φ), ε-shift method, self-energy isotropy (THEO-SM-5), η = 1/φ |
| SM-3  | K₃ spectral theorem, Koide parametrisation |
| SM-2  | Empirical K ≈ 2/3 for heavy quarks |
| SS-1  | SU(3)_c from face permutations (establishes S2), β₀ = 7 |
| SR-1  | SSV/PSR mechanism → η = 1/φ |

## What SM-7 Enables

- **Light quark masses (u, d, s):** Chiral condensate dominance at low mass
  requires new physics beyond the ε-shift framework.
- **CKM matrix:** If quark K₃ eigenvectors are misaligned with flavour
  basis (parallel to SM-5 for PMNS).
- **α_s running:** Connecting bare 0.386 to α_s(M_Z) = 0.118 via CPP
  RG mechanism (OPEN-P-SM-7-1; see SS-1 β₀ = 7).

## Parameter Count (§10)

Combined SM-6 + SM-7: 2 calibration constants (m_e, m_c) and 0 shape
parameters produce 2 coupling constants + 6 fermion masses. The Standard
Model requires 8 independent parameters for the same quantities.

---

*Mechanism file prepared by Claude Opus (Anthropic), 3 April 2026 MDT.
Verified against SM-7_heavy_quark_mass_spectrum.tex (v2.2) on GitHub.*
