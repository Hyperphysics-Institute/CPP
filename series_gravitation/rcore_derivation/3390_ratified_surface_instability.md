# β_SR1 = ½ ratified — and the surface it implies (8M/3) makes the even-sector trace wall UNSTABLE: the arc has a stability problem, located

**Patch 3390, Session 161, 2 Sep 2026.** Verify `code/3390_ratified_surface_poles_verify.py` (11/11; 3383/3384 machinery at `r_w = 8M/3`). Founder ruling R-PSR-LAW-LOG. Reasoning `reasoning/3390.md`.

**Standing:** the ruling is ENACTED. The surface move is COMPUTED and HELD. Nothing enters a paper.

## §1 What the ratified law implies for the surface

`PSR/l_P = (1 − v/2)/(1 + v/2)` (log form, second order fixed; third order assumed). The floor `l_P/2` is reached at `v = 2/3`: isotropic `r̄ = 1.5μ`, **areal `8μ/3 = 2.667 M = 1.33 r_S`**, lapse ½, `z = 1`, Level-A cavity 0.70 ms. Inside the CONV-038 window (`v > 0.536` light ring; `v ≤ 1` Buchdahl) with margin.

## §2 The poles at 8M/3 (62 M_⊙)

| sector / wall | Mω | Hz | Q |
|---|---|---|---|
| even Dirichlet (reference) | 0.3855 − 0.204 i | 201 | 0.9 |
| even Neumann (diagnostic) | 0.3905 − 0.060 i | 204 | 3.3 |
| **even, derived trace-Robin β₂(ω)** | **0.5199 + 0.034 i** | 271 | **Im > 0 — GROWING** |
| even ℓ = 3, derived | 0.7665 + 0.036 i | 399 | **GROWING** |
| odd Dirichlet X = 0 (reference) | 0.4592 − 0.199 i | 239 | 1.2 |
| **odd, registered shear, J = 6.75** | **0.4000 − 0.025 i** | **208** | **7.9** |

The odd sector is healthy: a sharp line at 208 Hz. **The even sector's derived wall supports exponentially growing modes** (growth time ≈ 29 M ≈ 9 ms at 62 M_⊙). r0-independent to 10⁻¹⁵: not numerics.

## §3 Why

`β_ℓ(ω) = b₀ − b₂ω²` is, in the time domain, the boundary law `∂_r* Z = b₀ Z + b₂ ∂²_t Z` — a wall with a boundary **mass** `b₂`. At `9M/4` (3383), `b₂ > 0`: positive mass, damped modes, Q 25 and 92. At `8M/3`, **both `b₀` and `b₂` are negative** (3383 found the sign flip beyond ≈ 2.4M): a *negative* boundary mass — energetically unstable, and the poles say so. The stability boundary of the trace-pinned even wall is the radius where `β_ℓ` diverges: **areal 2.38 M, `v = 0.856`**. The ratified floor sits at `v = 2/3` — outside it.

## §4 What this means, honestly

Three registered results collide at second order:
- **R-PSR-LAW-LOG** (ratified today) puts the floor at `v = 2/3`.
- **The trace-pinned even wall** (3378, CONV-039 SOUND-WITH-CAVEATS) is stable only for `v > 0.856`.
- **The window** (CONV-038) allows both.

So either (a) the trace-Dirichlet is the wrong *limit* of the surface — it was the zero-compliance limit of the one-Moment-delay surface (3375/3376), and the O(kd) compliance the arc has been deferring may be exactly what regularizes a negative boundary mass; or (b) the register that saturates is not `v`-indexed the way 3389 §4 assumed, and the floor sits inside 2.38 M after all (the third-order coefficient γ, still open, moves the floor: `s(v) = ½` needs `γ ≈ 0` for `v = 0.856`); or (c) the physical R-core is *unstable* to even-parity perturbations at its ratified surface — which would be a prediction, and a strange one. The worker does not choose. **OPEN-GR-SURFACE-STABILITY-1** minted with the three branches.

## §5 What is enacted and what is not
- Enacted: R-PSR-LAW-LOG; SR-1 corrigendum registered as owed (ledger B1: β_SR1 = ½ supersedes the Padé's second order; γ open).
- **Held:** the surface move, GR-1c Corrigendum 4, GR-2's paragraph, PRED-O-39 — until SURFACE-STABILITY-1 resolves. The flagship keeps V1.8's sentence: no Kerr echo frequency is yet derived. It is now also true at a = 0 for the even sector.

## §6 Next (worker's, not exhaustion)
1. The 3376 compliance term as a regulator: does a finite one-Moment compliance turn `b₂ < 0` stable? (A boundary condition with `∂_t` terms from the Moment delay.)
2. The floor with γ open: the range of γ for which the floor sits inside 2.38 M.
3. Founder picture: is there a reason the surface must be where the even wall is stable — i.e. is *stability* what locates the surface, with the PSR law's third order following from it?
