# Rung 3b — Leaver Kerr validated against tables; the ℓ = 2 gravitational angular gap closed; and the first EXACT Kerr wall spectrum (scalar sector)

**Patch 3358, 30 Aug 2026 — Session 157, on Fable.** Verify:
`code/3358_kerr_wall_modes_verify.py`, **9/9 PASS**.

## §1 Part A — validation before anything new

Leaver's coupled Kerr continued fractions (angular + radial, s = −2),
both written from memory, against **tabulated** (2,2) Kerr QNMs:
a/M = 0, 0.5, 0.7, 0.9 all reproduced to ≤ 1.2e−4. That validates the
s = −2 angular sector for *all* (ℓ,m) — including ℓ = 2, which 3357 had
to exclude — because Leaver's series absorbs the pole exponent into its
prefactor. **The ℓ = 2 gap is closed:** A(2,−2; c = 0.2688) = 4.665 for
s = −2 (vs 5.989 scalar, 6.25 eikonal; the +0.68 beyond the −2 offset
matches the first-order +8c/(ℓ+1) = 0.72 prediction from 3357).

Cross-instrument: Leaver's s = 0 angular CF agrees with 3353's
finite-difference eigenvalue at real c to 1e−6.

## §2 Part B — the first exact Kerr wall resonances

Direct inward integration of the **scalar** Kerr radial Teukolsky
equation from a numerically-fitted outgoing series to the derived wall
(r_w = 2.2668 M), root-finding on R(r_w) = 0. Validation ladder,
asserted: (B1) at a = 0 it reproduces the Schwarzschild s = 0 wall mode
from the independent rung-2 code to five decimals (0.56473 − 0.13886i,
two codes, one number); (B2) root independent of r₀ = 30/40/50 to
2e−8; (B3) zero sharp (contrast 5e−8).

| mode | ω (M = 1) | f @ 62 M_⊙ | Q | eikonal top (3334/3354) | exact vs top |
|---|---|---|---|---|---|
| **(2,−2)** | **0.48085 − 0.11668i** | **250.6 Hz** | **2.06** | 0.3953 | **+21.6%** |
| (3,−3) | 0.62812 − 0.07843i | 327.4 Hz | 4.00 | 0.5528 | +13.6% |
| (2,+1) | ~~0.63877 − 0.30216i~~ **WITHDRAWN (Patch 3359)** | — | — | 0.5643 | — |

**CORRECTION (Patch 3359, anti-erasure):** the (2,+1) entry above is
**WITHDRAWN**. It never received the r₀-independence and sharpness
tests that (2,−2) did, and 3359 found that direct inward integration
cannot locate Q ~ 1 modes at all (|Im ω| ≈ 0.3 → e^27 instability
growth; the root-finder returns its own guess). The value was a
non-converged guess, not a root. Every claim below that leaned on
(2,+1) — the exact-grade ordering test B6 — is downgraded accordingly.
The (2,−2) and (3,−3) entries stand (both fully validated).

## §3 What this says about the shipped prediction

- **The retrograde-keyed (2,−2) line is a broad top-of-barrier
  feature — no trapped comb at ℓ = 2, now exactly.** Q ≈ 2, consistent
  with 3356's Q = 1.9 at χ = 0 and confirming that Leg A's Q ≈ 5 was
  the outlier.
- **The above-top shift is +21.6% at Kerr**, not the +15–17% of the
  χ = 0 anchor. The band CONV-034 withdrew (~247–344 Hz) sat close to
  the scalar-exact answer — it was withdrawn correctly anyway, because
  it was *unearned*; now the number is computed.
- ~~GR-2's retrograde-keyed ordering survives at exact grade~~ **WITHDRAWN
  (3359)**: the (2,+1) comparator was unvalidated; the ordering test
  remains at eikonal-WKB grade.
- **(3,−3) at Q = 4 is the sharpest line** — a spectroscopically
  better target than the dominant (2,−2), though weaker-excited.

## §4 Fence and what remains

Part B is **s = 0**. It is the exact version of the grade every lane
census has been at, not the gravitational spectrum. The s = −2 wall
requires the boundary condition on the Sasaki–Nakamura variable — **rung
3c, the last item**, and the one with the largest recall risk (SN's
functions must be validated by reducing to Regge–Wheeler at a = 0).

**PRED-O-39 / GR-2:** the orientation-scale tops now have exact
scalar-sector counterparts. Registered here; **not enacted** —
changing a flagship prediction's quoted frequencies warrants a panel
round (CONV-036) once s = −2 lands, since the gravitational numbers are
what the prediction is about.
