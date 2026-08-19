# OPEN-QM-8 corrected measurement — run record (Patch 3236)

**Date:** 19 Aug 2026, Session 149. **Instrument:** `scripts/3236_qm8_true_cell_run.py`.
**Founder ruling A1 discharged:** the 24-cell carried no physical-picture weight
(prior worker's initiative); the run uses the **true Voronoi cell of the
600-cell-based lattice** (`founders_voice/founder_ruling_A1_voronoi_domain_2026-08-19.md`).

## The domain, stated exactly

The 600-cell's dual is the 120-cell; the Voronoi domain of each vertex of the
600-cell's vertex set is the corresponding **regular dodecahedron** cell —
12 pentagonal faces whose normals point at the 12 icosahedral nearest-neighbor
directions (FACT G1's vertex figure). Implemented as the support-function
radius R(ω) = ρ_in / max_f(ω·n̂_f) over the 12 icosahedron-vertex normals.

## The problem solved (Spin II's, not a proxy)

u-field equation −u'' − (1/r²)Δ_S u = k²u; u = 0 at center (CP Exclusion);
FREE end u' = 0 at the cell boundary along each ray. Recorded because the
committed March instrument failed on TWO semantic counts, not one: (i) no
Dirichlet center (V0 §5 diagnosis), and (ii) a free condition on ψ is not
Spin II's free condition on u — on a sphere, ψ-Neumann gives the tan(kR)=kR
spectrum (k₁R ≈ 4.493), not (2n−1)π/2. This instrument discretizes the
u-equation directly, so both traps are closed by construction.

**Declared approximations** (anisotropy² class, ~1% in positions): angular
coupling uses the shell-averaged metric weight (exact in the sphere limit);
ray-coordinate cross-terms neglected. Dodecahedral anisotropy R ∈ [1, 1.258]
(mesh-sampled max 1.2196 at level 3 — mesh directions do not hit the exact
cell corners; support function exact per sampled direction).

## Results

**Sphere control (instrument validation):**

| quantity | measured | exact | 
|---|---|---|
| k₁·R | 1.57079 | π/2 = 1.57080 |
| k₂·R | 4.71209 | 3π/2 = 4.71239 |
| Mode-2 interior zero | 0.66667 | 2/3 |
| Mode-2 antinode | 0.3333 | 1/3 |

**True Voronoi cell (dodecahedron), two densities (162×80, 642×120):**

| quantity | density 1 | density 2 | sphere reference |
|---|---|---|---|
| radial candidates in lowest 90 | 3 | 3 | 3 |
| Mode-2 k·⟨R⟩ | 4.69989 | 4.69759 | 4.71239 (−0.31%) |
| Mode-2 isotropy score | 0.999 | 0.999 | 1.000 |
| Mode-2 node s | 0.6670 | 0.6670 | 0.6667 |
| Mode-2 antinode s | 0.3375 | 0.3333 | 0.3333 |
| Mode-3 zeros | 0.404, 0.803 | 0.402, 0.801 | 0.4, 0.8 |

**FROZEN VERDICT (readings applied verbatim from V0 §6 / OPEN-QM-8):
MODE2-RECOVERED** — both densities, node drift 0.0000 < 0.02. The worker's
pre-declared expectation (V0 §6, committed at Patch 3234 BEFORE the A1
ruling existed) is confirmed. Checks: 5/5.

## What the measurement establishes, and what it does not

- **Established (numerical leg of OPEN-QM-8):** the true Voronoi cell of the
  600-cell lattice preserves the open–closed mode family — spectrum shifted
  0.3%, Mode-2 node/antinode positions at the exact 2/3, 1/3 to 0.05%, and
  Mode 3 showing the expected (0.4, 0.8) double-zero structure. The
  icosahedral cell's anisotropy does NOT disturb the mode topology the
  captured DP anchors to. Combined with V0 §4 (discreteness bound 7×10⁻⁴⁵),
  the lattice-cell selection question is answered affirmatively at
  instrument level.
- **Not established:** the analytic 2I-symmetry selection argument (the
  second OPEN-QM-8 route) — still open, now with a measured target.
- **Cosmetic instrument note, for honesty:** the antinode-finder searches
  s < 0.6 only, so it reports a spurious "antinode 0.6000" for Mode 1 (whose
  true maximum is the boundary antinode at s = 1). Mode 1 participates in no
  reading; noted so nobody chases it.

## Governance note

This is a WIN in the review-economy sense (a closed measurement confirming a
pre-declared expectation on a frozen verdict rule) and therefore qualifies
for a panel round. Worker recommendation: BUNDLE the spin-arc package
(Spin I + II + III V0.1 + this record) with the GR-1 V0 review when the
founder chooses to spend a round — one block, one paste — rather than
dispatching now. Founder's call.
