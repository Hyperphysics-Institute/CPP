# OBL-CC-2 STAGE 2 (C-PROF) — EXECUTED: the profile coefficient DERIVED (k₂ = 2, fore-aft field suppression under radial recession), the dipole geometric factor exact (g_d = 2), and the UV anchor ELIMINATED by the exact lattice sum; the coefficient formula assembled with two named unknowns

**Patch 3066 (11 Aug 2026). Executes plan §2 (`oblcc2_coefficient_
derivation_plan.md`). Verify: `scripts/3066_stage2_profile_lattice.py`.
No cosmological input anywhere: every number below is substrate
geometry, special-relativistic kinematics, or exact lattice
arithmetic.**

## §1 — The deficit weight: k₂ = 2, derived then verified

A Sea pair at distance r recedes RADIALLY (the founder's expansion
picture) with β = Hr/c. The received field of a radially receding
charge is the fore-aft boosted-Coulomb value E = (1−β²)·E_static
(the standard along-the-motion suppression; the (1−β²sin²ψ)^{−3/2}
factor is unity on the line of motion up to O(β²δ²/r²)). The pair's
received field inherits the overall (1−β²); its quadratic content is
suppressed by (1−β²)² ≈ 1−2β²: **deficit weight = k₂β² with k₂ = 2
exactly** (analytic; numerically 1.9996 at β = 0.02 with common
random numbers — the first CRN-less attempt's instability is on the
record in the script header as a methods note). First-order Doppler
never enters the quadratic content; no angular-average convention is
needed because the recession direction is geometrically fixed.

## §2 — The dipole factor: g_d = 2, exact

Orientation-averaged squared dipole field ⟨E²⟩ = 2p²/r⁶ — an exact
angular integral, computed by deterministic quadrature (2.000000).
Methods note on the record: the committed script's first run
estimated this by Monte Carlo and tripped its own tolerance (3/4) —
an exact integral should never be sampled; corrected in-place.

## §3 — The lattice sum: the UV anchor eliminated

The continuum integral n·4π∫dr/r² required an arbitrary lower
anchor. Replaced by the EXACT sum over pair sites: S₄ = Σ_{i≠0}
1/r_i⁴, convergent (nearest-site dominated). Computed at the engine
lattice convention (spacing a = 2.5): **S₄(cubic) = 0.41663**,
bracketed by S₄(FCC) = 0.15886 (dimensionless lattice constants
C₄ = 16.274 cubic / 6.206 FCC). The true Sea lattice type is a
substrate question REGISTERED for founder ruling (the 600-cell
projection lineage suggests neither simple choice is final); the
lattice-type factor is a discrete, enumerable input — not a tuning
dial.

## §4 — The assembled coefficient (engine units)

  **ρ_Λ = K·q²/R_h²,  K = (g_d k₂ / 8π)·δ²·S₄ = (1/2π)·δ²·S₄**

with δ = D0 = 0.6 (the engine pair separation): K_cubic = 0.023871,
K_fcc = 0.009102 (engine units, q = 1). Two named unknowns remain,
both sky-blind: **(U1)** q², the physical per-arrival imprint
normalization — the Stage-3 static engine measurement; **(U2)** the
lattice-unit → physical calibration (the SM-11 chain) + the
lattice-type ruling. Nothing else is free.

## §5 — Stage-3 protocol (FROZEN before execution)

Engine measurement M-q²: committed 2902 engine, static configuration
(no β step, mobile_sea as committed), single source at the origin of
a small ideal Sea (a = 2.5, the committed jitter convention DISABLED
for the static normalization run — disclosed deviation, normalization
only); record the imprint amplitude at receiver GPs vs distance over
r ∈ [5, 15]; fit the 1/r² envelope; q² ≡ the fitted envelope constant
in engine units. Calibration C-cal: the SM-11 lattice-scale chain
maps (a, δ, q²)_engine → physical; executed as arithmetic on the
SHIPPED SM-11 constants (no new fits). Assembly (plan §4) only after
both freeze; then the full w(z)/H(z) curve freezes; then the
full-shape trial. If K_physical lands outside the viable band,
**F-CLI-1 FIRES** and the record will say so in those words.
