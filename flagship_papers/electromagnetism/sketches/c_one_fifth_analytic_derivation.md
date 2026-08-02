# c = 1/5 DERIVED — THE ROUND-TRIP DRIVE IN CLOSED FORM, ALL COEFFICIENTS EXACT, 7/240 REFUTED (c₄ = 1/35)

**Patch 2926 (1 Aug 2026). Closes the arc's queued next item — "the
analytic derivation of c = 1/5 from the round-trip angular moments,"
queued at Patch 2900, promoted to sole affordable precision route at
Patch 2924 (`turnover_test_record.md` disposition). Three checks
PRE-REGISTERED in session chat before any algebra was run; one band
failed as pre-registered and was resolved by its pre-registered
follow-up (§4). Verify script: `code/2926_c_one_fifth_derivation.py`
(all checks PASS, exit 0).**

---

## §1 — THE ALGEBRAIC COLLAPSE

The 2884/2900 geometry (return leg arrives at the CP at t = 0; DP at
r(μ, √(1−μ²)); DP emission time t₂ = −r; outgoing leg solves
|DP − CP(t₁)| = s with t₁ = t₂ − s, CP at βt₁) has a quadratic whose
discriminant is a **perfect square**:

    disc = r²(1 + βμ)²        ⟹        d_out = r(1 + 2βμ + β²)/(1 − β²).

Geometric reading: 1 + 2βμ + β² = |n̂ + β x̂|², the squared length of
the DP direction vector displaced by the velocity vector.

**Consequence 1 — exact factorization.** The drive integrand couples r
and θ only through d_out = r·g(β, μ), so

    D(β) = 2π R_m · (1−β²)² I(β),     R_m = ∫ r⁻ᵐ dr,
    I(β) = ∫₋₁¹ μ dμ / (1 + 2βμ + β²)².

Every dimensionless coefficient of the β-expansion is therefore
**independent of m and of the r-range identically** — the invariance the
2900 robustness grid measured is now *derived*, not observed.

## §2 — CLOSED FORM AND EXACT COEFFICIENTS

The angular integral is elementary. With artanh(β) = ½ln((1+β)/(1−β)):

    D(β) = 2π R_m [ (1−β²)² artanh(β)/β² − (1+β²)/β ]
         = 2π R_m Σ_{n≥0}  8 β^{2n+1} / [(2n−1)(2n+1)(2n+3)].

**Coefficient identity (the promised angular-moment origin):** with
⟨μ^{2k}⟩ = 1/(2k+1) the even moments of the sphere (n = 0 uses the
convention 1/(2·0−1) = −1),

    a_n = ⟨μ^{2n+2}⟩ − 2⟨μ^{2n}⟩ + ⟨μ^{2n−2}⟩

— **the drive is the second difference of the even angular moments.**
Normalizing D/β = k(1 − cβ² − c₄β⁴ − c₆β⁶ − …):

| quantity | exact value | numeric | 2900 measurement |
|---|---|---|---|
| k | −(16π/3)R_m | — | (m, r-range dependent ✓) |
| **c** | **1/5** | 0.200000 | 0.200008 |
| c₄ | **1/35** | 0.028571 | 0.02916 |
| c₆ | 1/105 | 0.009524 | — |
| c₈ | 1/231 | 0.004329 | — |
| c_{2n} | 3/[(2n−1)(2n+1)(2n+3)] | — | — |

The queued heuristic "⟨cos⁴θ⟩ = 1/5" is literally present: c's
numerator is 1 − 2⟨μ²⟩ + ⟨μ⁴⟩ = 8/15, its denominator −a₀ = 8/3, ratio
exactly 1/5. Newton I's required substrate supply is now the closed
function μ(v)·D(v) = v against an exactly known D.

## §3 — PRE-REGISTERED CHECKS (recorded in chat before execution)

**CHECK 1 (identity) — PASS.** Closed form vs the verbatim 2900 numeric
integral: relative error is O(h) (halves per grid doubling: 1.270e-2 →
6.323e-3 → 3.154e-3) and **β-independent to ~1e-7 spread**; it equals
the discrete-radial-sum error (+1.2709e-2 at nr = 480) to four digits.
The discretization error lives entirely in the β-independent radial
constant — which is *why* the 2900 fits could see c to 4×10⁻⁵ through
1% absolute quadrature error.

**CHECK 2 (fit forensics) — SPLIT, resolved (§4).** Refitting the
closed form with the exact 2900 grid and [1, β², β⁴] design:
fit gives c = 0.199993, c₄ = 0.02913. The c₄ band PASSED:
**the β⁶⁺ tail of the exact-1/35 series biases the truncated fit up to
0.0291 — the 7/240 = 0.02917 coincidence is explained. 7/240 is DEAD;
the exact value is 1/35.** (Registered at 2900 as "candidate, NOT
claimed"; the discipline paid.) The c band **FAILED as pre-registered**
(gap 1.5e-5 > the 2e-6 band).

**CHECK 3 (confrontation) — PASS.** c = 1/5 = 0.200 sits inside the
banked direct bound c_direct = +0.91 ± 2.40 (16–84%: −1.5 .. +2.8;
Patch 2924, `code/2924_direct_fit.py` +
`data/2924_turnover_results.json`). Per the 2924 disposition this
confrontation closes the arc's precision question at the level the
direct instrument can decide: **the static-Sea curvature is the exact
kinematic rational 1/5, derived and consistent with every direct
measurement.**

## §4 — THE FAILED BAND AND ITS PRE-REGISTERED RESOLUTION

Before touching any registry, the follow-up (pre-registered in chat:
"convergence toward 0.199993 ⟹ identity holds; convergence to 0.200008
or elsewhere ⟹ the closed form is missing something real") was run —
the numeric fit under grid refinement:

| grid | c (numeric fit) | c₄ (numeric fit) |
|---|---|---|
| 480×720 (2900's) | 0.200008 | 0.02916 |
| 960×1440 | 0.199997 | 0.02914 |
| 1920×2880 | 0.199994 | 0.02913 |
| 3840×5760 | 0.199993 | 0.02913 |

Monotone convergence to the closed-form fit values exactly. The 1.5e-5
was angular quadrature noise in the 2900 run; the 2e-6 band was set
below that run's own noise floor. **Verdict: identity holds; both 2900
residuals (0.200008 vs 1/5, 0.02916 vs 1/35) are fully accounted for as
truncation bias + quadrature noise.**

## §5 — WHAT THIS MEANS, AND WHAT IT DOES NOT

**It means:** (i) the arc's queued item is CLOSED — c = 1/5 is a
theorem of the round-trip model, not a five-decimal measurement;
(ii) the *entire* undressed drive law is now closed-form, so every
future instrument (hybrid, direct, entrained) has an exact β-resolved
confrontation target at all orders, not just β²; (iii) the entrainment
cancellation target of Patch 2900 §2 is sharpened — the mechanism must
cancel the exact series Σ 3β^{2n}/[(2n−1)(2n+1)(2n+3)], term by term or
in sum, and the one-dial one-shot result (kills 1/5, flips 1/35) can be
re-examined against exact coefficients; (iv) OPEN-HYB-SHAPE-1 inherits
a sharper discriminator: the hybrid's static-channel output can be
confronted with the exact function, not a fit.

**It does NOT mean:** Newton I is recovered (the B1 §1 obstruction
stands exactly as before — this derivation makes the obstruction
*exact*, which cuts both ways); nothing here touches the dressed /
entrained / self-consistent Sea; nothing here bears on the β⁰ core,
anti-screening, or the statics suspension. Ledger untouched.

**Scope note (registry ruling under PD-006):** this is a closed-form
property of the 2884/2900 model within the B1 arc — sketch-tier per the
arc's uniform precedent (no THEO registration for 2884–2924 curvature
results); it will enter the theorem registry if and when the B1 /
SF-6-successor paper ships it under the four-condition test. No frontier
items open or close (the queued item lived in the handover queue, never
as an OPEN-ID); dashboard counts unchanged; a bracketed completion note
is recorded in `frontier_sectors/EW.md`.
