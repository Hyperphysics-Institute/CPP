# FAQ — SM-2

*Extracted from the original reviews-SM-2.md. These are anticipated questions and answers for general readers.*

---

## Category A: On the Calibration

### A1. "You have one calibration constant and 15 particles. That's
### 14 free predictions — or is k just a scale factor?"

k is a scale factor that sets the absolute mass scale. Once k is
fixed to the electron mass, all other masses are determined by the
cage geometry assignments (N_k) and the suppression formula σ = 120^{-d}.

The honest accounting: one calibration constant (k) plus geometric
structural assignments (N_k per particle). The N_k values are
motivated by the 600-cell cage hierarchy but are not yet derived
from it — they are calibrated to PDG. So SM-2 has one free parameter
(k) plus 15 N_k assignments that are constrained by cage geometry
but not fully derived. This is more constrained than the Standard
Model (which has ~19 free parameters), but it is not yet
parameter-free.

The path to making it parameter-free is OP-SS-1: derive the N_k
values from the cage-specific SSV geometry without calibrating to
PDG masses. Until that derivation exists, SM-2 should be read as
a semi-empirical framework demonstrating that one geometric scale
factor propagates through consistent rules to reproduce all SM masses.

---

### A2. "If k is just calibrated to the electron mass, you're just
### rescaling. Why is this different from standard QFT Yukawa
### couplings, which are also fit to data?"

Two differences.

First, the Standard Model has one Yukawa coupling per fermion — 12
free Yukawa parameters for 12 fermions. SM-2 has one parameter k
for all 15 SM particles. The constraint ratio is 15:1 vs 1:1. Even
if the N_k values are treated as free parameters, SM-2 has fewer
total free parameters than QFT for the same mass table.

Second, the N_k values are not freely chosen — they are constrained
to be positive integers (or simple geometric combinations) consistent
with the cage shell structure. You cannot set N_k = 137 for the
electron to fit some data; N_k = 1 is forced by the cage geometry.
The freedom is in the inter-shell bonding and DP cloud corrections,
not in the leading cage term.

The goal is to derive the N_k values from geometry entirely, removing
all calibration beyond k. That is OP-SS-1. Until it is solved, SM-2
is a demonstration that the geometric framework is internally
consistent, not a claim that it is parameter-free.

---

### A3. "Why should the suppression factor be 120^{-d}? The number
### 120 is the vertex count of the 600-cell — why is that the
### relevant suppression?"

Because 120 is the number of distinct computational positions
available to a CP in one 600-cell. A particle with d unbound spatial
dimensions distributes its ZBW energy equally across all accessible
lattice positions in those d dimensions. The total number of such
positions is 120^d (120 per dimension, d dimensions). The energy per
position is therefore the ZBW energy divided by 120^d — which is
the suppression σ = 120^{-d}.

For a neutrino (d=3): its ZBW mode samples all three spatial
dimensions of the macroscopic lattice freely. The energy is diluted
across 120³ ≈ 1.7 × 10⁶ positions, giving σ ≈ 5.8 × 10⁻⁷ and
hence neutrino masses in the meV range. For an electron (d=0): its
ZBW mode is bound by the cage — it does not sample the macroscopic
lattice. The full ZBW energy is concentrated in one cage — σ = 1.

The derivation of σ = 120^{-d} from the 600-cell geometry is
motivated but not yet rigorously proved from first principles.
This is an open problem.

---

## Category B: On the Quark Masses

### B1. "The effective occupancies N_k for quarks (30, 180, 3000,
### 30000) bear no obvious relation to the cage vertex counts
### (4, 12, 20, 30). Where do these numbers come from?"

They are calibrated to PDG masses via the SM-2 formula, not
derived from cage geometry. The cage vertex counts (4, 12, 20, 30)
give the leading-order cage binding energy. The effective N_k values
absorb the contributions from inter-layer bonding, DP cloud energy,
and the radial qDP composition gradient — contributions that SM-2
models but does not yet derive from first principles.

The ratio N_k(strange)/N_k(electron) = 30/1 should, when OP-SS-1 is
solved, be derivable from the ratio of cage binding energies plus
corrections. The current N_k values are best understood as targets
that the first-principles calculation must reproduce, not as inputs
to the theory.

---

### B2. "The light quark masses (u, d, s) are non-perturbative in
### QCD. How does SM-2 handle this?"

SM-2 does not correctly handle the light quarks from first principles.
The up quark (N_k ≈ 1, bare qCP) and down quark (N_k ≈ 2.5) masses
are calibrated rather than derived — the cage framework gives the
right order of magnitude but the non-perturbative ZBW Schrödinger
equation in V(r) = −sea × ℏc/r with cage boundary conditions would
be needed for a rigorous calculation.

The K3 thermal picture (SM-3) works well for heavy quarks (c, b, t):
K(c,b,t) = 2/3 to 0.42%, consistent with the Koide spectral structure
showing through when cage binding >> current mass. For light quarks,
the cage binding and current mass are comparable and the perturbative
cage picture is insufficient. This is explicitly noted in SM-2 §9
(conclusion) as the open problem.

---

## Category C: On the Gauge Bosons

### C1. "The W, Z, Higgs masses are assigned cage structures
### (linear hDP chain, icosahedral cage, dodecahedral cage)
### somewhat arbitrarily. How are these justified?"

The assignments are motivated by two criteria: (1) consistency with
the fermion cage hierarchy (the Z's icosahedral cage matches the
charm quark's outer shell, the Higgs's dodecahedral cage matches the
bottom quark's third shell — both at the same energy scale), and
(2) consistency with the EW physics (the W's open-chain structure
matches its polarity-inverting behavior; the Z's symmetric icosahedral
cage matches its parity-conserving coupling; the Higgs's dodecahedral
cage is the heaviest closed structure, consistent with it being the
mass-giving field).

These are motivated assignments, not derived ones. The full EW series
papers derive the W, Z, and Higgs structures from the CPP EW framework.
SM-2 uses them as inputs for the mass calculation.

---

### C2. "The Higgs boson is a scalar (spin-0) in the SM. How does
### a dodecahedral cage produce spin-0?"

A closed polyhedral cage with full icosahedral symmetry (the
dodecahedron is the dual of the icosahedron — both have full I_h
symmetry) has no preferred rotational axis in any direction. The
ground state of the dodecahedral cage has zero orbital angular
momentum — the hDPs in the cage cancel each other's angular momenta
due to the symmetric arrangement. This gives spin-0. This is
consistent with the SM Higgs being a scalar, but the derivation from
the CPP cage structure is a qualitative argument; the full proof
belongs to the EW series.

---

## Category D: On SM-2's Scientific Status

### D1. "Is SM-2 a real physics paper or is it numerology?"

The honest answer is that SM-2 is between the two. It is not
numerology — the framework has a specific physical mechanism
(cage binding energy from SSV gradients), a specific geometric
substrate (the 600-cell), and specific derivations that have been
falsified and corrected (C₆₀ is gone, 1/φ² is replaced by the exact
result, the Koide mechanism is corrected). Numerology is unfalsifiable;
SM-2 has been falsified on several predictions and corrected.

It is not yet a full physics paper in the sense of making
parameter-free predictions for the quark masses. The N_k values
are calibrated to PDG, making SM-2 a semi-empirical framework
rather than a pure prediction.

The scientific status will change when OP-SS-1 is solved. A
first-principles derivation of all N_k values from cage geometry —
with no PDG calibration — would convert SM-2 from semi-empirical
to predictive. Until then, SM-2 demonstrates internal consistency
and motivates the derivation, which is genuine scientific value.

---

*Document prepared by Thomas Lee Abshier ND and Claude Sonnet
(Anthropic), 30 March 2026.*
