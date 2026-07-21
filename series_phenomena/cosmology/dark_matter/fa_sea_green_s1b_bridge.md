# FA-SEA-GREEN S1b — the scale bridge (sub-pin P1a) RESOLVED: lossless coarse-graining is structure-free (Laplacian in, Laplacian out, isotropy symmetry-protected at every nesting level), every registered restoring candidate is a coarse-scale object, and the effective operator is therefore a DISCRETE-SITE SCATTERING problem on the motif graph embedded in continuum transport — not a hop Laplacian

**Patch 2669, 20 July 2026. Stage S1b of the FA-SEA-GREEN charter (FROZEN
2666), opened on GATE G1 PASS (2668). Blind guards in force: no candidate
value, no screening length, no decay-vs-parameter curve appears below.
79.5% not in scope.**

## §1 — The question, restated

At which level of the nested-600-cell hierarchy (0736) does the effective
static response operator for the qq registration amplitude act? Charter
routes: (a) derive the coarse fm-scale operator from the Planck-level
kernel by explicit coarse-graining, OR (b) establish from registered
structure that the response acts directly at the coarse motif level.
**Both routes execute below and agree; the bridge is resolved without
Branch I.**

## §2 — Route (a): explicit coarse-graining of the lossless kernel is trivial by RG structure

From S1a, the Planck-level kernel's static continuum limit is
−(a²/6)∇² with a = ℓ_P. Coarse-graining the lossless transport from ℓ_P
to the motif scale:

1. **Second moments compose additively** (K^n's displacement second moment
   = n·a²/3 per component); **all higher cumulants are RG-irrelevant**
   (central-limit Gaussianization of the iterated shell step). The
   effective transport at any block scale is again a Laplacian with the
   composed coefficient — Laplacian in, Laplacian out. Verified
   numerically fork-blind: `code/2669_s1b_coarsegrain_check.py`
   (second-moment additivity to <0.1%; excess kurtosis of the iterated
   kernel row → 0). No gap enters the instrument.
2. **Isotropy is protected at every nesting level.** The 0736 hierarchy is
   self-similar (R/a = φ, icosahedral point symmetry at each level); by
   the S1a symmetry argument (no invariant rank-2 or rank-4 icosahedral
   tensor; first invariant harmonic l = 6), anisotropic corrections cannot
   accumulate through the nesting — the continuum transport between ℓ_P
   and the motif scale is the isotropic Laplacian, full stop.
3. The QM-5 dispersion ω_k = c√|λ_k|/ℓ_P (consistency anchor, glossary):
   its long-wavelength limit ω ≈ c·k·√(λ-curvature) is exactly the
   Laplacian transport at speed c = ℓ_P/t_P — the anchor is consistent
   with, and not importable beyond, the statement above.

**Route-(a) conclusion:** lossless coarse-graining supplies NO structure
and NO length. The transport arriving at the motif scale is the scale-free
continuum Laplacian at propagation speed c. Any length in ℓ must come from
the restoring (P2), not the spreading (P1) — the founder's separation,
now an RG theorem of the formalized kernel.

## §3 — Route (b): registered structure locates the RESPONSE at the coarse motif level

1. **The field lives on motif vertices (I2, pinned).** The FA-C2 response
   field f — the qq registration amplitude — is a per-vertex polarization
   amplitude of the DP Sea. DPs sit at the motif sites (SS-2 embedding:
   I1 graph, ℓ_unit = 0.589 fm, ℓ_edge = ℓ_unit/φ).
2. **Every registered restoring candidate is coarse-scale (I4, all
   three).** (a) DP internal bindings E_qDP = 264 / E_eDP = 88 MeV
   [0880/0886]; (b) the bound-CP oscillator static limit [2452]; (c) the
   2443 bond curvature [2462 lineage] — MeV energies, fm distances, all
   properties of DPs/bonds at the motif scale. The 2665 scoping grep
   already established that NO Planck-level restoring DOF is registered
   anywhere. **The registry therefore leaves exactly one place the gap can
   enter: on-site at the motif vertices.** If S1c finds no candidate fits
   the mechanism, the exit is Branch I — but the LEVEL is not in doubt.

## §4 — The bridge output: the effective operator's derived form

Combining §2 + §3, the effective static response operator is a
**discrete-site scattering problem**: sited responses at the I1 vertices,
coupled by the continuum lossless transport derived at S1a. Precisely —
the mediating static field φ obeys the S1a Poisson transport with sources
= (external) + (induced on-site response −χ φ_i at each DP site i), giving
the self-consistent site system

**φ_i = φ_ext,i − χ Σ_{j≠i} G_ij φ_j**,  G_ij = the S1a static propagator
between sites ∝ 1/r_ij,

i.e. the discrete Sea response operator **M = I + χ G** (G_ii = 0; the
self-response is the on-site term itself), with χ = the on-site static
polarizability that S1c must identify from mechanism among the registered
candidates. Multiple scattering between sites is fully captured by the
resolvent (I + χG)⁻¹. χ > 0 (restoring opposes the local field) is the
screening case; a mechanism-derived χ ≤ 0 would route toward FG-NEG.

**This is NOT a nearest-neighbor hop Laplacian.** The site couplings are
the long-ranged 1/r superposition — exactly what the 2665 nearest-neighbor
trap warning demanded ("the registered Perceive summation is over all
GPs, local and distant"). No lattice-scale footprint (edge, cell, or
other) is assumed anywhere in M; whatever length the Green function of M
decays with is an OUTPUT of the S2 spectrum. Sub-pin P1a is thereby
resolved: **the operator acts at the coarse motif level, with its
inter-site structure inherited (structure-free) from the Planck kernel.**

## §5 — Specifications handed to S2 (frozen here, before any spectrum exists)

- **Distances r_ij:** the 4D chord distances of the unit-circumradius
  600-cell scaled by ℓ_unit (registered polytope geometry, SM-3 lineage),
  with the 2527 4D→3D packing-inference flag disclosed at instrument
  level. **Robustness companion (mandatory at S2):** repeat with
  graph-geodesic distances; a readout-class change under this swap is
  reported as implementation sensitivity (an honest null per the
  FA-C3-DISC-1 philosophy), not resolved by preference.
- **Compactness disclosure:** the I1 graph is a compact 120-vertex arena
  standing in for the infinite Sea; adequate for lattice-scale decay
  readout, degraded for near-unscreened decay — the readout reports which
  regime it lands in.
- **The single physical parameter:** the dimensionless χ/ℓ_unit, derived
  at S1c from registered energies with zero freedom — the arc's
  zero-parameter structure. The I5 question (does the E_qq window
  propagate into χ?) is answered by whichever candidate the mechanism
  identifies.

**No Morse-class sentence consumed (2664 rider n/a here).** Reasoning:
`reasoning/2669.md`. Instrument: `code/2669_s1b_coarsegrain_check.py`.
