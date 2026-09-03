# Nothing bounces off the centre: the ℓ = 2 wave turns around at r_t = 0.98 M and never reaches r = 0. And with R-REGISTER-COUNTS-BOTH-SIDES the junction is energetically closed — the even sector's two channels are coupled through one register

**Patch 3397, Session 161, 3 Sep 2026.** Founder ruling R-REGISTER-COUNTS-BOTH-SIDES. Reasoning `reasoning/3397.md`. No new computation beyond the interior geometry (numbers below; 3384 machinery).

## §1 Why the wave comes back — and why it is not a bounce

The founder is right to ask. The record has said "returns from the centre" and "reflects at the centre" since 3374, and neither phrase describes a mechanism, because there isn't one and none is needed.

A wave of angular order ℓ converging on a point carries angular structure that cannot be squeezed into that point. In the interior (flat register, speed set by `J = 6.75`, `k = Jω`), the regular solution is `ψ = x j_ℓ(x)`, `x = kr`, which behaves as `x^{ℓ+1}` near the origin. At the line frequency (`Mω = 0.37`, `k = 2.50/M`):

| quantity | value |
|---|---|
| core isotropic radius | 1.5 M |
| **classical turning radius** `r_t = √(ℓ(ℓ+1))/k` | **0.98 M — 65% of the core radius** |
| amplitude at r = 0 relative to maximum | 3.6 × 10⁻¹⁵ |
| `k·R_core` | 3.75 (< 5.76, the first interior standing-wave root) |

**The wave turns around at two-thirds of the way in and never touches the centre.** In DI-bit terms: the inward-moving stream, carrying an ℓ = 2 pattern, has no configuration in which it piles into one GP; its paths curve around at `r_t` and continue outward. Nothing reflects. AP-4 (fixed emission, no sink) guarantees nothing is absorbed on the way, so what went in comes out. This is the same physics as sound in a rigid sphere or light in a lens: *regularity at the origin*, not reflection from it. The 3384 interior model used exactly this (the Riccati–Bessel regular solution); only the prose was loose. Corrected here; the phrase "reflects at the centre" is withdrawn from the lane's language in favour of "turns around at the centrifugal radius / regular at the origin."

One more thing the numbers say: at this frequency the core is shorter than half an interior wavelength (`kR_core = 3.75 < 5.76`), so the interior is a **single turn-around**, not a resonant cavity. The interior standing-wave family (the 3384 "second timescale") starts at `x = 5.763`, i.e. `Mω = 5.763/(J·1.5) = 0.57` — about 296 Hz at 62 M_⊙ — above the ℓ = 2 line but in band.

## §2 The ruling closes the junction

F-5 asked whether DI-bits arriving from inside count in the surface register. **Yes** — "regardless of whether it is from the center or from outside." Consequences:

- The surface register's demand is `δD = δD_ext + δD_int`, where the interior term is the returning vector wave's *magnitude* (AP-4: SSV_abs counts |E|; a vector arrival loads the scalar register).
- The level set therefore moves with **both** the exterior wave and the returning interior wave: `ξ = −(δv_ext + δv_int)/v′`.
- The 3396 inconsistency (|R| = 1 from the level set alone, while T ≠ 0 carries energy in) is resolved *by the ruling*: the interior wave's return re-loads the register and shifts the reflected wave — the two channels are coupled through one register, and energy flows through the coupling. The problem is a genuine two-channel junction with exterior amplitude R, interior amplitude T, and two conditions (register level set *including the interior term*; SSV_net continuity for the vector content) — well-posed.

## §3 What is needed to compute it (owed, worker's)
1. **A sourced `H₁` reconstruction** (the even mode's shift at the wall) — the one formula the worker could not verify at 3396. Without it the vector fraction is an order-of-magnitude (`ωr ≈ 1`).
2. The interior vector wave (3384 machinery, `J = 6.75`, regular solution) and its magnitude-contribution to the surface register (AP-4 count rule).
3. The coupled root-find: exterior `Z⁺` with level set + `SSV_net` continuity ↔ interior `T`. Then the a = 0 even poles with the channel open.

Expectation, not claim: |R| < 1 on the even sector at the first pass, the 195/292 model poles broaden, and the single interior turn-around adds a delayed component rather than a second line at this frequency.

## §4 Language corrected in the record
"Reflects/bounces at the centre" (3374, 3382, 3384, 3390, 3391, 3396) → "turns around at the centrifugal radius; regular at the origin." Dated note here; the earlier records stand as written with this pointer.
