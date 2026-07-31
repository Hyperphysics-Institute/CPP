# PRE-REGISTRATION — DIRECTED RELAY: FRONT CLASS AND VOLUME-AVERAGED LW TEST

**Patch 2888. Committed BEFORE execution. The 2885 pre-registration (point-test bands)
cannot govern this test — the reason is stated in §2 and it is NOT re-banding.**

---

## §1 — WHAT IS BEING BUILT AND WHY

The 2887 finding: the AUTOMATON-2 engine implements a DIFFUSIVE relay
(p = 0.478), not a ballistic one, because the translation-invariance
reduction in `moment()` converts the C22 origin-directed spec into an
isotropic convolution that discards propagation direction. Consequence:
the LW question is ill-posed for that engine.

**This test implements the C22 spec directly** — each DI-bit travels in
its initial direction for all time, with no re-spreading at intermediate
points. Twelve directional field components, each advecting rigidly by
one FCC hop per Moment:

    Q_d(x, t+1) = Q_d(x − d, t) + inj(x − d, t) / 12

This is a pure transport equation, not a diffusion. It implements
"origin-directed" at the level of individual bits.

## §2 — WHY THE 2885 POINT-TEST DISCRIMINANT IS ILL-POSED FOR THIS ENGINE
(and why this is NOT re-banding)

The 2885 discriminant measures the field at off-axis test points and
back-projects the field direction. For the directed relay, this fails on
two independent geometric grounds — DERIVED BEFORE RUNNING, not inferred
from a result:

**Ground A — the field is concentrated on 12 discrete rays.** The
directed relay emits bits from the source in 12 FCC directions. Each bit
travels in a straight line. For a moving source over T Moments, the field
is nonzero only at positions s(t_emit) + k·d for each FCC direction d and
emission time t_emit. Off-axis test points (at r/√2 perpendicular offset)
are NOT on these rays for v > 0, so the interpolated field there is
essentially zero. A discriminant computed from near-zero field is
undefined.

**Ground B — for test points ON a ray, back-projection gives A = 0 by
geometry.** For the (1,1,0)/√2 direction and test point at
(x_src + off, M/2 + off, M/2): back-projecting the field direction
(-1,-1,0)/√2 from the test point gives x_aim = x_src + off − off = x_src.
So A = 0 **regardless of whether the relay is retarded or LW** — the
geometry produces A = 0 for any relay in this configuration.

**This is why a new observable is required**, not because the old bands
gave an unfavourable result. The old bands gave INCONCLUSIVE twice — and
the obstacle in both cases was the geometry, not the engine physics.

## §3 — THE NEW OBSERVABLE: VOLUME-AVERAGED LW DISCRIMINANT

Instead of the field direction at a point, measure the **x-displacement
of the field's centre of mass** relative to the current source position:

    ⟨Δx⟩ = Σ_xyz (x − x_src) · |Q(x)| / Σ_xyz |Q(x)|
    ⟨r⟩   = Σ_xyz |x − x_src| · |Q(x)| / Σ_xyz |Q(x)|
    A_vol  = ⟨Δx⟩ / (β · ⟨r⟩)

**Physical interpretation.**
- **LW relay** (field centred on instantaneous source): ⟨Δx⟩ = 0 → A_vol = 0.
- **Fully retarded relay** (field centred on past source positions):
  ⟨Δx⟩ = −v · (T−1)/2, ⟨r⟩ = c_lat · (T−1)/2 (leading order) →
  **A_vol = −v/(β · c_lat) = −1 exactly**, since v = β · c_lat.

This is derivable analytically for the directed relay. Key steps:

- At time T, bit in direction d emitted k Moments ago sits at
  s(T−k) + k·d = s(T) − k·v + k·d. Its Δx from current source = k·(d_x − v).
- Summing over all 12 FCC directions: Σ_d d_x = 0 (4 with d_x = +1,
  4 with d_x = −1, 4 with d_x = 0). So Σ_d (d_x − v) = −12v.
- Per-Moment contribution to ⟨Δx⟩: (1/12) · (−12v) = −v.
- Averaged over k = 0 to T−1: **⟨Δx⟩ = −v · (T−1)/2**.
- ⟨r⟩ per step ≈ c_lat = √2 (leading order, small v).
- **A_vol = −1 exactly.** β cancels. Observable is β-independent.

For finite β, ⟨r⟩ deviates from √2 per step due to the source offset.
At β = 0.40: A_vol ≈ −0.95 (computed analytically from the exact per-direction
distances). The deviation from −1 is 5%.

**WORKER PREDICTION, declared in advance:** A_vol ∈ [−1.05, −0.85] at all
three β values. Spread/|mean| < 0.10.

## §4 — FROZEN BANDS

### Front propagation class (Test 1)
| verdict | criterion |
|---|---|
| **BALLISTIC** | fitted exponent p ∈ [0.95, 1.05] over t = 2..12 |
| **DIFFUSIVE** | p < 0.75 |
| **INCONCLUSIVE** | otherwise |

### Volume-averaged LW discriminant (Test 2)
| verdict | criterion |
|---|---|
| **LW-LIKE** | \|A_vol\| < 0.15 at every β |
| **RETARDED** | A_vol < −0.50 at every β **AND** spread/\|mean\| < 0.30 |
| **INCONCLUSIVE** | otherwise |

**These bands are not the 2885 bands** — they are new, because the
observable is new. The 2885 bands apply to the point-test discriminant
and cannot apply to a different observable.

**IMPORTANT ASYMMETRY.** The BALLISTIC + RETARDED outcome is the one that
supports Condition B. The LW-LIKE or DIFFUSIVE outcome goes against it.
**The worker commits in advance to reporting an adverse outcome as
prominently as a favourable one.** A favourable outcome does NOT establish
the mechanism: it only establishes that the directed relay, IF implemented
as the C22 spec intends, produces a retarded field. Condition A (the sign
of the Sea's response), LINK 2 (the marginality condition), and LINK 3
(stability, B1) all remain open regardless of this result.

## §5 — PARAMETERS

- M = 96 for front test; M = 128 for LW test (avoid periodic wrap)
- NMOV = 40 Moments of source motion before read
- β ∈ {0.10, 0.20, 0.40}
- Source starts at (40, M/2, M/2) moving +x
- Neutralising background −1/M³ per site per Moment (matching 2802 config)
- Injection by trilinear deposition (matching 2886 re-run)

## §6 — STANDING

1B OPEN · PR7 PARTIAL · six of seven · B7 holds DM-1/2/3 · Candidate (B) 79.5%.
