# Mechanism — SF-3: The Quark Sector from 600-Cell Geometry

## Mechanism 1: The cage-mass hierarchy (`V^{7/3}` scaling)

**What it explains:** why four quark masses spanning four orders of magnitude sit
on a single geometric progression.

**The picture:** a quark is a colour-charged cage of Conscious Points occupying
one of the four bonded distance-shells of the 600-cell, with vertex count
`V ∈ {4, 12, 20, 30}` for (s, c, b, t). The cage's vertex count sets its mass
through the `V^{7/3}` scaling: the exponent `7/3` counts displacement-increment
pair interactions times the linear cage dimension (SM-9), so a larger cage
stores proportionally more SSV field energy. The anchor `M_0 = m_e z/φ ≈ 3.79
MeV` ties the whole spectrum to the single electron-mass calibration.

**Verifiable:** `code/1500_verify_sf3_core.py` reproduces all four masses at RMS
2.1% from `m_e` + geometry alone, with `m_c = 1249 MeV` (−1.6%) appearing as a
*prediction*, not an input.

**Why it matters:** what conventional physics records as four unrelated quark
masses is, in CPP, one cage-scaling law on one lattice.

## Mechanism 2: The top relay (`z·C_F = 16`)

**What it explains:** why the top quark sits a factor ~16 above where the bare
`V^{7/3}` progression alone would place it.

**The picture:** the top quark's icosidodecahedral shell (`V = 30`) relays its
self-energy across all `z = 12` nearest neighbours, weighted by the colour
Casimir `C_F = 4/3`. The product `z·C_F = 16` is the colour-Casimir-weighted
coordination factor. Both `z` and `C_F` are inherited structural outputs (SM-9,
SS-2), not tunable parameters — no calibration hides here.

## Mechanism 3: Mode complementarity (one spectrum, two couplings)

**What it explains:** why the strong coupling and the Weinberg angle are not two
independent inputs but two harmonics of one substrate vibration.

**The picture:** the 600-cell adjacency spectral trace partitions into modes.
`α_s = 5/(8φ)` is the share carried by *face* (`A³`) modes — oriented
face-adjacency walks, the colour-flux relays across cage faces. `sin²θ_W =
3/(8φ)` is the share carried by *edge* (`A²`) modes — edge round-trips. Their
sum is fixed at `1/φ` by the propagation-efficiency factor `η = 1/φ`, giving the
exact complementarity `sin²θ_W + α_s = 1/φ` and the topological ratio
`α_s/sin²θ_W = F/E = 1200/720 = 5/3`.

**Important honesty:** within SM-6/SM-7 these are *structural correspondences* —
mode fractions of the adjacency spectrum that numerically match the measured
couplings — **not** gauge couplings obtained from renormalization-group running.
The lattice discreteness is *smoothed* only in the running-coupling comparison,
where `α_s = 5/(8φ)` is matched to a scheme-dependent effective value at the
charm scale.

## Mechanism 4: The isotropic self-energy shift (the quark Koide phase)

**What it explains:** the quark Koide phase `θ_quark = 124.04°` (vs PDG 124.09°,
0.05%).

**The picture:** the bare K₃ eigenphase is `cos θ_0 = −K = −2/3`. Quarks carry
colour, so their K₃ cage faces feel the strong coupling on all `z = 12` bonds,
producing a negative isotropic shift `ε_S = −z α_s/(z+1)`, alongside the same
electroweak shift the leptons feel, `ε_EW = +3/(52φ)`. The net shift
`ε = −27/(52φ)` rotates the eigenphase:
`cos θ_quark = −(2/3)(1 + ε/2) ≈ −0.5597 ⇒ θ_quark = 124.04°`.

**The bookkeeping separation (Proposition 5.1):** this phase depends only on
`{α_s, sin²θ_W, z}` — never on the mass amplitude `A_q` or the charm mass `m_c`,
because `A_q` is an overall scale that cancels from the phase ratio. The
independence holds *because* `α_s` is the structural value `5/(8φ)`; a
charm-scale running-coupling fit would re-introduce `m_c`. So the phase stands
whichever mass route is used — no re-grounding on the derived `m_c` is needed.

## Mechanism 5: Antipodal identification (three generations, no fourth quark)

**What it explains:** exactly three generations; no fourth-generation quark.

**The picture:** the four bonded shells exhibit a palindrome symmetry in the full
600-cell shell sequence; antipodal identification in the tessellated lattice
limits the Standard Model to three *effective* generations (SM-8). The count is
*selected within* this model — a model-dependent selection, not a uniqueness
theorem — and the same identification predicts no fourth quark. This is a clean
falsifier: a fourth-generation quark would directly contradict the mechanism.
