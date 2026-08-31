# Rung 3c — the gravitational (s = −2) Kerr wall spectrum: the last item, and it moves the flagship line

**Patch 3359, 30 Aug 2026 — Session 157, on Fable.** Verify:
`code/3359_sn_gravitational_wall_modes_verify.py`, **9/9 PASS**.

## §1 The recall risk, discharged by three tests before any Kerr number

The Sasaki–Nakamura functions (η, α, β, F, U with c₀…c₄) were written
from memory. A wrong term gives plausible wrong QNMs — the worst
failure mode — so three tests ran first:

- **T1:** at a = 0, U_SN + ω² = V_RW pointwise to 1.6e−9 and F ≡ 0 —
  the SN equation reduces exactly to Regge–Wheeler.
- **T2:** in Kerr, U → −ω² as 1/r — short-range, so X = 0 is a
  well-posed node condition.
- **T3 (decisive):** at a = 0 the SN wall instrument reproduces 3356's
  exact RW wall resonance from an independent code:
  0.44859 − 0.11749i, |Δ| = 2.7e−6.

## §2 The gravitational Kerr wall spectrum, χ = 0.68

| mode | ω (M = 1) | **f @ 62 M_⊙** | Q | contrast | r₀-spread |
|---|---|---|---|---|---|
| **(2,−2)** | **0.36694 − 0.08782i** | **191.2 Hz** | **2.09** | 6e−9 | 3e−9 |
| (3,−3) | 0.55333 − 0.06522i | 288.4 Hz | 4.24 | 4e−9 | 3e−10 |
| (2,+1) | **NOT LOCATED** | — | — | 0.75 | — |

Every reported root passed r₀-independence and sharpness
*individually*. The (2,+1) row is the method's limit (§4), not a
result.

## §3 What changed, and it is the flagship line

**The gravitational (2,−2) line is 191 Hz for GW150914** — below every
prior estimate: the eikonal top (211 Hz), the CONV-034-withdrawn +17%
transport (247 Hz), and the exact scalar line (251 Hz, 3358). The
gravitational lines sit **12–24% below** the scalar ones (ratios 0.763
and 0.881), and the a = 0 case already said so (RW/scalar = 0.794) —
the s = −2 effective potential is lower than the s = 0 one, so its
resonances sit lower. **3358's framing that the scalar sector was "the
exact version of the lane's grade" was right for STRUCTURE (no comb,
broad Q ≈ 2 at ℓ = 2) and wrong for POSITIONS.** Corrected here.

Notably, the withdrawn "+17% above the top" transport was **wrong in
sign** for gravitational waves: the (2,−2) line sits 7% *below* the
eikonal geodesic top. CONV-034's withdrawal was more right than anyone
knew.

**What survives at gravitational grade:** no trapped comb at ℓ = 2
(Q = 2.09, a single broad top-of-barrier feature); (3,−3) at Q = 4.2 is
the sharpest line; and 3352/3355's stability conclusions are untouched
(they depend only on R(r_w) < 0 in the superradiant window).

## §4 Method limit found, and a 3358 result withdrawn

Direct inward integration is validated for |Im ω| ≲ 0.12. At Q ≈ 1
(|Im ω| ≈ 0.3) the ingoing contamination grows ~e^27 across the range
and the root-finder cannot move — it returns its own guess with
contrast ≈ 1. **(2,+1) is therefore NOT LOCATED at s = −2.** And
**3358's scalar (2,+1) = 0.63877 − 0.30216i is WITHDRAWN**: it never
received the r₀/sharpness tests and was, on inspection, the same
failure. 3358's record is corrected in place. **Consequence: the
retrograde-keyed *ordering* test is NOT established at exact grade** in
either sector — the prograde-exposed comparator is unlocated — and
remains at eikonal-WKB grade. Very broad modes need a different
instrument (a Leaver-type series with the wall condition, or a
Riccati/contour formulation). Registered as open.

## §5 Registry

- **OPEN-GR-RCORE-3: all chartered items discharged**, at the grades
  stated: finite-ℓ (A/B/C), co-rotation (b), excitation (e),
  Zel'dovich (d), s = −2 angular (3a/3b), radial Kerr (3b/3c).
- **NEW OPEN: very-broad-mode instrument** (Q ≲ 1.5), needed for the
  prograde comparator and the exact-grade ordering test.
- **PRED-O-39 / GR-2 amendment now OWED, and it changes the flagship
  frequency: (2,−2) ≈ 191 Hz (gravitational, exact), Q ≈ 2.1; (3,−3)
  ≈ 288 Hz, Q ≈ 4.2.** This warrants a panel round (**CONV-036**)
  before enactment — a flagship prediction's quoted frequency moves.
- A1–A3 conditionality (OPEN-GR-RCORE-4) is inherited throughout.
