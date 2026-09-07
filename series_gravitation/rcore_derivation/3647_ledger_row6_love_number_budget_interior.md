# PD-007 ledger ROW 6 — tidal Love number k₂ under the budget interior [PCD-EXT]: k₂ = +0.042, Λ ≈ +3.8. The budget law's level-set surface is maximally compliant (chi_eff = 1 at the level set), identical to the census-frame case. Sign: POSITIVE. Sitting on the FREE branch of Hinderer's formula (y_R = −3.22 > y* = −6.81). H-SURFACE-IMPEDANCE's static sector is OPEN.

**Patch 3647, Session 163, 6 Sep 2026.** Verify `code/3647_ledger_row6_love_number_budget_interior_verify.py` (22/22). Reasoning `reasoning/3647.md`.

## §1 Setup and the physical question

Row 6 carries the tidal electric Love number k₂ of a BBH component modelled as the R-core. The question after Patch 3640 (THEO-PCD-BUDGET) is: what is k₂ under the budget interior with a C¹ surface (σ = P = 0, no Israel shell)?

The previous computation (3624) used the rigid-cap model: interior flat at cap, surface = level-set with K(R) = 0. That gave k₂ = −0.080 (RIGID branch). Patch 3633 then found three positive readings in the census and harmonic-pattern frames, but the budget interior—with its distinct surface law—was still owed.

**Budget law:** `v_eff(v) = 2·cap − cap²/v`, with `cap = 2/3`.

## §2 The chi_eff profile and the key identity

Define the spring compliance parameter as in 3639: `chi_eff(rbar) = (v_eff − cap)/(v − cap)`.

For the budget law:

```
v_eff − cap = (2·cap − cap²/v) − cap = cap − cap²/v = cap(1 − cap/v) = cap·(v − cap)/v
```

So:

```
chi_eff(rbar) = cap(v − cap)/v / (v − cap) = cap/v
```

**chi_eff = cap / v(rbar) at every interior point.**

At the level-set surface (rbar = Rbar, where v = cap):

```
chi_eff|_{surface} = cap/cap = 1  (exactly)
```

The surface is **maximally compliant**. Deep inside, chi_eff(rbar→0) → cap/1 = 2/3.

## §3 The level-set displacement argument

Under a tidal perturbation, the level-set (where v_eff = cap) is displaced by:

```
xi = −delta_v / (dv_eff/drbar)|_{surface}
```

For the budget law:

```
dv_eff/drbar|_{surface} = chi_eff|_{surface} × (dv/drbar)|_{surface} = 1 × (dv/drbar)|_{surface}
```

This is **identical to the census frame** (where chi = 1 everywhere). The level-set displacement under a unit tidal field is the same as in the free / unclamped case computed in 3633.

**Therefore: k₂(budget interior, C¹ matching) = k₂(census frame) = +0.042, Λ = +3.8.**

Verification: `dv/drbar|_{Rbar} = 4/(9·Rbar) = 4/13.5 = 0.4444`, and the ratio `(dv_eff/drbar) / (dv/drbar) = 1.000` to 10⁻⁸ (check 5).

## §4 Hinderer landscape at C = 3/8

Hinderer's closed-form k₂(y, C) (y = R·H'/H at the surface) has a denominator zero at:

```
y* = −6.8051
```

This divides the spring family into two branches:

| branch | y_R range | k₂ sign | example |
|---|---|---|---|
| RIGID | y < y* (= −6.81) | negative | y = −10.33 → k₂ = −0.080 (rigid cap, 3624) |
| FREE | y* < y < 5 (numerator zero at 5; corrected 3648) | positive | y = −3.22 → k₂ = +0.042 (census frame, 3633) |

The budget interior's surface at chi_eff = 1 gives y_R = −3.22 (FREE branch). k₂ = +0.042, Λ = +3.80.

**3633 three-reading bracket:** y = −4.76 (k₂ = +0.088), −3.22 (k₂ = +0.042), −2.57 (k₂ = +0.033). The budget result sits at the middle reading — census frame — which is exact within the C¹ budget-interior matching.

## §5 Spring family bracket and the chi_crit crossover

Using the linear y_R interpolation y_R(chi) = (1−chi)×(−10.33) + chi×(−3.22):

```
chi* = (y* − y_rigid)/(y_free − y_rigid) = (−6.81 − (−10.33))/(−3.22 − (−10.33)) = 3.52/7.11 ≈ 0.496
```

| chi | y_R | k₂ | branch |
|---|---|---|---|
| 0.000 | −10.33 | −0.080 | RIGID |
| 0.250 | −8.55 | −0.143 | RIGID |
| 0.496 ≈ chi* | −6.81 | ±∞ (pole) | — |
| 0.510 | −6.70 | +2.10 | FREE |
| 0.667 | −5.59 | +0.160 | FREE |
| 1.000 | −3.22 | +0.042 | FREE ← **budget surface** |

The **budget surface** (chi_eff = 1 > chi*) is on the FREE branch. The rigid cap (chi = 0 < chi*) is on the RIGID branch. The spring family transitions through a k₂ resonance pole at chi* ≈ 0.50.

## §6 H-SURFACE-IMPEDANCE hypothesis in the static sector

The dynamical wall law β = −iω/s gives β → 0 as ω → 0. This means the hypothesis carries a *wave* impedance but does not directly specify the *static* spring compliance chi_s. Two cases:

- If chi_s > chi* (≈ 0.50): the hypothesis sits on the FREE branch → k₂ > 0
- If chi_s < chi*: RIGID branch → k₂ < 0

The mapping s ↔ chi_s (or equivalently s ↔ y_R,static) requires the junction derivation — the same OPEN-GR-SURFACE-IMPEDANCE-1 problem that the wave attempts failed to crack (3645 attempt 1, 3646 attempt 2a). In the static sector this is JUNCTION-1's two-channel problem at ω = 0.

**The chi* = 0.49 crossover is the observational discriminant**: if the junction derivation gives chi_s < 0.49, PRED-O-40's sign flips (k₂ becomes negative); if chi_s > 0.49, k₂ stays positive. This is the hypothesis' **fifth group member** (pending the junction derivation, labeled OWED).

## §7 PRED-O-40 status

Re-cut (3633): *"Λ consistent with 0 at ±3σ, or a negative k₂, falsifies."*

Under the budget interior (the extension's own model, no hypothesis):
- k₂ = +0.042 > 0: falsifier not triggered.
- Λ = +3.8 ≫ 0 and ≫ 3σ at ET/CE sensitivity.

PRED-O-40 is **strengthened**: the budget interior gives a definite positive k₂, not merely "not negative."

## §8 Standing and owed items

- **Row 6 ledger: COMPUTED.** k₂ = +0.042, Λ = +3.8, y_R = −3.22, FREE branch. [PCD-EXT].
- **Supersedes:** 3624's k₂ = −0.080 (rigid cap; replaced by the budget C¹ matching).
- **Consistent with:** 3633's census-frame reading (+0.042), which is now the definite answer.
- **Owed:** chi_s(s=3.22) from JUNCTION-1 at ω = 0 — the hypothesis' fifth group member.
- **Bracket** from the spring family (for reference): k₂ ∈ [−0.080, +0.042]; the budget surface sits at the free end. With the hypothesis (chi_s < 1), k₂ may shift; the direction depends on chi_s vs chi*.
