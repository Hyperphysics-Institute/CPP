# The shift reconstruction, derived — not recalled — from the linearized Einstein equations; and the even mode is 34% "vector" at the ratified wall. The junction is now fully posed except for one dictionary: shift ↔ SSV_net

**Patch 3398, Session 161, 3 Sep 2026.** Verify `code/3398_H1_derived_vector_fraction_verify.py` (8/8, symbolic + numeric). Reasoning `reasoning/3398.md`.

## §1 What "take it from the literature" turned into

The corpus has no network path to the papers. So instead of citing, the record now **derives**: the even-parity, ℓ = 2, RW-gauge perturbation of Schwarzschild is written out, the linearized Ricci tensor is computed symbolically (via `δΓ` and background covariant derivatives), and the separated vacuum equations are extracted. Three of them:

    (t,θ):  2M H₁ + r(r − 2M) H₁′ + iω r²(H₂ + K) = 0
    (r,θ):  iω r² H₁ + 2M H₂ + r(r − 2M)(H₂′ − K′) = 0      [H₀ = H₂]
    (t,r):  a constraint mixing Y and Y″

Solving (r,θ) for `H₁` and inserting the Zerilli–Moncrief `K(Z)`, `H₂(Z)` (mutually consistent; sourced to Lousto–Price/Moncrief by the Grok seat at CONV-039):

    **H₁ = −iω [ (2r² − 6Mr − 3M²)/((r − 2M)(2r + 3M)) · Z + r Z′ ]**

— and this `H₁(Z)`, with `K(Z)`, `H₂(Z)` and the Zerilli equation, satisfies the (t,θ) and (t,r) equations **identically**. All three reconstruction formulas used since 3378 are now verified against the field equations in the record itself. (The formula I had "recalled" at 3396 was correct; the *check* I recalled was wrong. That is a better outcome than a citation: a citation would have told me the formula; the derivation told me the check.)

## §2 The vector fraction at the ratified wall

For the free-surface ℓ = 2 mode (3391 pole, `ω = 0.37487 − 0.0019i`, `r_w = 8M/3`, `Z′/Z` fixed by the wall law):

| | |K| | |H₂| | |H₁| |
|---|---|---|---|
| amplitude (Z = 1) | 0.979 | 0.652 | 0.846 |

**Vector fraction `|H₁|²/(|K|² + |H₂|² + |H₁|²) = 0.34.`** A third of the mode at the wall is shift. 3396's order-of-magnitude (`ωr ≈ 1`) stands; the number is now computed. The vector channel cannot be dropped.

## §3 The junction, now fully posed but for one dictionary

Exterior: `Z⁺` → `(K, H₂, H₁)` at the wall (all three derived). Interior: a vector wave in the flat core (3384 machinery, `J = 6.75`, regular at the origin — the turn-around at `r_t = 0.98 M`, 3397), amplitude `T`. Surface conditions:
1. **Register level set** (3391) with the interior's contribution to the demand (R-REGISTER-COUNTS-BOTH-SIDES; AP-4: a vector arrival adds its magnitude to SSV_abs).
2. **Vector continuity:** the exterior shift `H₁` ↔ the interior `SSV_net` wave at the surface.

Condition 2 needs the one thing the corpus has not stated: **the shift dictionary — how `h_tr` (the even-parity vector harmonic, the census's net flux direction) maps to `δSSV_net`.** The corpus has `ψ(v)` and `N(v)` for the scalar; it has no `h_tr ↔ SSV_net`. Without it the coupling strength is a free parameter, and I will not guess it. **OPEN-GR-SHIFT-DICT-1.**

Physically the candidate is natural and is stated as a candidate only: the shift `h_tr` is the momentum density of the linearized field; in CPP the census's momentum density is the *net direction* of DI-bit arrivals — which is `SSV_net` itself (AP-4: `SSV_net = Σ E_i` as a vector, `SSV_abs = Σ|E_i|`). If `δh_tr ∝ δSSV_net` with a fixed coefficient, the junction closes and the even poles with the channel open are one root-find away.

## §4 What is claimed and what is not
- Claimed: the three reconstructions, derived; the 34% vector fraction at the wall.
- Not claimed: any coupling coefficient; any corrected pole; any statement about whether the 195/292 lines survive the open channel.

## §5 F-6 to the founder (physical picture)
In CPP, the register at a GP holds `SSV_abs` (a count) and `SSV_net` (a vector sum) from the same DI-bits. **A wave that arrives as a *tilt in the direction* of the incoming DI-bits — more from one side than the other, without changing their number — changes `SSV_net` but not `SSV_abs`. Is that the whole of what the metric's "shift" (the `h_tr` component) is in CPP?** If yes, the dictionary is `δh_tr ∝ δSSV_net` and its coefficient is fixed by the exterior (where CPP reproduces GR), and I can close the junction. If the shift has some other substrate meaning, I need that picture.
