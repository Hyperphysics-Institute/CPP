# Attempt 3b, static run — the register closure joined to the vacuum exterior in ONE gauge. Result: the closure fixes the wall condition K/H = 2/3 exactly (the c07 dictionary at v = cap; χ and the interior count law drop out), and that sits 0.8% from the exterior's static ℓ = 2 zero mode (K/H = 0.6615 = Hinderer's pole). Formal k₂ = +7.9 (Λ ≈ 700) is pole-adjacent and not a number to carry; the sign flips at a 1% shift of the wall ratio, inside the corpus's O(v) dictionary uncertainty at the wall. Robust content: the budget R-core under the register closure is near-marginal against static quadrupolar deformation. The perturbed surface is not the level set (geometry demands 21% more displacement) and carries a small induced layer (1% residual, count-law independent). **Row 6 re-cut: k₂ sign OPEN; PRED-O-40 re-cut; 3647's +0.042 superseded in method**

**Patch 3650, Session 163, 6 Sep 2026.** Verify `code/3650_register_closure_static_junction_verify.py` (17/17; the perturbed extrinsic curvature derived symbolically in the script). Reasoning `reasoning/3650.md`. No paper touched.

## §1 The setup — one coordinate system, one gauge
Both sides in lattice coordinates r̄, RW-type form `g = diag(−N²(1 + H₀Y), ψ⁴(1 − H₂Y), ψ⁴r̄²(1 − KY)Ω)`. The budget background joins isotropic Schwarzschild C¹ at r̄ = 3M/2 (3640 §3). The exterior static solution (3624's equations) transforms tensorially into this form with `H₀ = H₂ = H`, `K = K` (the form factors track g_rr). The register closure inside: `δg = (∂g/∂v_eff) χ(v) δv`, so `H₀ = 2N_vχδv/N`, `H₂ = K = −2χδv/ψ` (conformally flat, 3378 part 1; `H₀ ≠ H₂` allowed: the register is not a fluid, 3649 §4). The surface is displaced to `r̄ = R̄ + ξY`.

## §2 The junction conditions, derived
Extrinsic curvature of the displaced surface to first order (derived in the script; background pieces check against the standard isotropic-coordinate forms):
- induced metric: `[H₀] = 0`, `[K] = 0` — **ξ drops out** because N, N′, ψ, ψ′ are continuous (C¹).
- `[δK_tt] = 0 ⟺ [H₀′] = −2ξ[N″]/N`;  `[δK_θθ] = 0 ⟺ [K′] = 4ξ[ψ″]/ψ`; the `Y_{:AB}` part is identically continuous.
- `[N″] = −0.833`, `[ψ″] = +0.741`: the background is C¹ but not C² (the smeared shell's edge, 3649 §1), so the extrinsic conditions see the displacement.

## §3 What the induced metric forces
`[H₀] = 0` with the closure's `K/H₀ = −N/(ψN_v)` gives the wall condition **`K(R)/H(R) = 2/3` exactly** (`N = ½, ψ = 4/3, N_v = −9/16`). χ cancels; the interior count law does not enter; `[K] = 0` is then automatic. This is the closure's static wall law — the counterpart of the clamp's `K(R) = 0` (3624).

## §4 What the exterior does with it
| wall K/H | y_R | k₂ |
|---|---|---|
| 0 (clamp, 3624) | −10.33 | −0.080 |
| 0.640 | −6.92 | −1.9 |
| 0.655 | −6.84 | −6.3 |
| **0.6615 (pure decaying solution = static zero mode = Hinderer's pole)** | **−6.805** | **±∞** |
| **2/3 (register closure)** | **−6.778** | **+7.9 (Λ ≈ +714)** |
| 0.680 | −6.71 | +2.2 |
| 0.700 | −6.60 | +1.0 |

The closure's condition is 0.8% from the static zero mode. Two consequences: (i) the formal `k₂ = +7.9` is a pole-adjacent value — a ≈1% shift of the wall ratio moves it anywhere from −∞ to +∞ and flips its sign at 0.6615; 3633 §2 found the corpus's linear (C5) and nonlinear (c07) static dictionaries differ by ~30% at the wall, so **the sign of k₂ is not determined at the corpus's current dictionary precision**. (ii) What *is* determined: **the budget R-core under the register closure sits within 1% of a zero-frequency ℓ = 2 deformation** — near-marginal static stability. That is structural, not numerical.

## §5 The displacement and the induced layer
With `[H₀] = [K] = 0` imposed, the two extrinsic conditions each fix ξ: `ξ/H = −1.228` (tt) and `−1.217` (θθ) for the flat-lattice count law; `−1.215 / −1.204` for 3643's count law at ω = 0. They agree to 1%, and the 0.011 H residual is *identical* for both count laws — no interior law removes it: the closure junction carries a small induced ℓ = 2 surface layer under a tide. A fully layer-free junction would need `K/H = 0.625`, which violates `[K] = 0` by 0.04 H: **no exactly layer-free static junction exists for the register closure.** The level-set rule `ξ = −δv/v′` gives `ξ/H = −1.00`: the geometry demands ~20% more. Under the closure the perturbed surface is **not** where `v_eff = cap`; 3647's argument (and 3633's census frame) assumed it was.

## §6 Row 6 re-cut, and standing
- **Row 6: OPEN, sharpened.** 3647's `k₂ = +0.042` is superseded in method (it was the level-set/census-frame reading; the one-gauge junction gives a different wall condition). Under the register closure: `K/H = 2/3` at the wall, near the zero mode; sign of k₂ undetermined by the O(v) dictionary; **the decisive quantity is the static count↔lapse dictionary at the wall to better than 1%** — OPEN-GR-LATTICE-FRAME-1's static face, now with a threshold (0.6615) attached.
- **PRED-O-40 re-cut:** "a BBH component's static quadrupole response far from a black hole's — `|Λ| ≫ 1`, sign open — or a static ℓ = 2 instability; `Λ` consistent with 0 at ±3 falsifies" (LVK's present bounds on BBH `Λ̃` are O(10²–10³), 3624 §4 recollection: a live constraint on the near-pole side, to be checked cold before V2.3).
- **3643 check owed:** a static zero mode 1% away implies a dynamical pole near ω = 0; 3643's argument-principle contour was around the QNM. Re-run the even-sector stability with the *register closure* interior (not the scalar proxy) and a contour that includes ω ≈ 0.
- OPEN-GR-SURFACE-IMPEDANCE-1: attempt 3b's dynamical run is next (the same junction at ω ≠ 0 with 3643's count wave equation), now with the static wall law `K/H = 2/3` as its ω → 0 limit — a fixed point the dynamical law must reproduce.
- The H-SURFACE-IMPEDANCE hypothesis: unchanged.
