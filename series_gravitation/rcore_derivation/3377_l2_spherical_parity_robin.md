# OPEN-GR-ROT-1, the ℓ = 2 spherical rung — The mirror is even-parity; GR-2's ladder is odd-parity; a scalar mirror forces a ROBIN wall on the Regge–Wheeler function, not X = 0

**Patch 3377, Session 161, 2 Sep 2026.** Verify `code/3377_l2_spherical_parity_robin_verify.py` (16/16). Reasoning `reasoning/3377.md`.

**Standing:** the parity finding is UNCONDITIONAL. The Robin law and its 20° number are CONDITIONAL on one map (register-Dirichlet ⟺ Zerilli-Dirichlet at the wall), which is CONV-039's question. Nothing is claimed about the O(kd) skin term (3376).

## §1 The finding

The 3297 mirror — and its derivation at 3375 — is a condition on the **register** `u = k·Δ|SSV|`, a *scalar* that enters the metric through the isotropic conformal factor `ψ⁴ δ_ij`. A scalar perturbation of the conformal factor is **even-parity** (polar). An odd-parity (axial) perturbation has no conformal-factor component at all (Check 0).

GR-2's line set was computed with the **Regge–Wheeler ℓ = 2 axial** equation and Dirichlet `X = 0` at the wall (3297 Check 7; GR-2 V1.6 text; 3359's Teukolsky `s = −2` reduces to RW at `a = 0` "pointwise"). So the shipped wall condition was imposed on the parity the mirror does not constrain, and was never derived for it. This is independent of everything else in the arc: it would have been true at 3297 with the Exclusion Rule intact.

## §2 What a scalar mirror does to the odd sector

The even and odd master functions are related by the Chandrasekhar transformation. It is **verified numerically here, not recalled**: a Zerilli solution `Z⁺` is integrated, transformed, and the transformed function satisfies the RW equation to residual `6 × 10⁻⁸` for exactly one sign convention (Check 1); the inverse has the opposite derivative sign (Check 2):

    [μ²(μ²+2) − 12iωM] Z⁻ = W(r) Z⁺ − 12M dZ⁺/dr*,      W(r) = μ²(μ²+2) + 72M²(r − 2M) / (r²(μ²r + 6M)),   μ² = (ℓ−1)(ℓ+2).

Hence **if** the register mirror is Dirichlet on `Z⁺` at the wall, the odd sector obeys a **Robin** law there:

    dZ⁻/dr* = −(W(r_w)/12M) · Z⁻,        W(9M/4)/12M = 2.020 / M   (ℓ = 2).

Constructive check: an RW solution launched with this slope transforms to `Z⁺ = 0` at the wall to `10⁻¹⁶` (Check 2). And **unconditionally**: `Z⁺ = 0` and `Z⁻ = 0` at the same wall force `dZ⁺/dr* = 0` too, hence `Z⁺ ≡ 0` — the shipped `X = 0` is *not* the odd-sector image of any scalar mirror (Check 3).

## §3 The reflection coefficient of the Robin wall

    R(ω) = (iω + a_R)/(iω − a_R),   a_R = −2.020/M:   |R| = 1;   |arg R − π| = 2 arctan(ω/|a|).

Dirichlet (π) as `ω → 0`; Neumann (0) as `ω → ∞` (Check 4). The wall is a mirror at low frequency and transparent-phase at high frequency, with the crossover at `Mω ~ 2`.

## §4 What the flagship inherits — conditionally

| Line | f (Hz) | Mω (62 M_⊙) | odd-sector phase departure from π |
|---|---|---|---|
| (2,−2) | 191 | 0.366 | **20.6°** |
| (3,−3) | 288 | 0.553 | ~30° (same `a`; ℓ = 3 has its own W — indicative) |

Twenty degrees is not a small correction to `X = 0`. It shifts the top-of-barrier resonance the ladder found. **Conditional** on the map `δψ = 0 at the surface ⟹ Z⁺ = 0 at the wall`, which is a gauge-invariant statement nobody in the arc has written down (the register pins the conformal factor; the Zerilli function is a combination of `K` and `H₂` and their derivatives; Dirichlet on `K` alone is a Robin-type condition on `Z⁺` in general). That map is **CONV-039 Q-parity**.

## §5 The three possibilities CONV-039 must sort

1. Register-Dirichlet ⟹ `Z⁺ = 0`: then the odd sector is Robin with `a = 2.02/M` and the (2,−2) line moves by O(20°) of boundary phase — **recompute the ladder with the Robin wall** (GR-2 V2.0 content).
2. Register-Dirichlet ⟹ a Robin law on `Z⁺` itself: then the odd law is a different Robin — compute from the map.
3. The odd sector is governed not by the register but by the **SSV_net (vector) sector**, which has no wall ruling at all (the founder's "average SSV_net is zero at cap" is a statement about the mean, not the perturbation): then `X = 0` on the odd sector is a *separate* physical assumption needing its own derivation — or the odd sector is transparent and the echo lives in the even sector only.

## §6 What this does and does not change

- The mirror as the small-amplitude limit of the register (3375): unchanged.
- GR-2 V1.7 caveat (a) ("boundary-phase shift uncomputed"): now has a *candidate value* (20°) on one branch and a *parity gap* on all branches. The caveat's wording will change at V1.8/V2.0; not enacted here (ledger unchanged).
- The 3376 O(kd) skin term: orthogonal — it is an amplitude correction on the even sector; this is a parity correction on the odd sector at linear order.

## §7 Owed

CONV-039 package: Q-numerical (3376 formulation), Q-parity (the register→Zerilli map; the odd-sector rule), Q-recompute (the ladder under the Robin wall as a scoped deliverable). Then GR-2 V2.0.
