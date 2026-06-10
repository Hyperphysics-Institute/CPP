# Patch 1002 — Route B: non-log running near l_P, and the sensitivity bar

**Project C / SS-1 `op:lambda_psr`. Route B opening. NOT a closure — framework + one theorem.**

Step 0 (Patch 1001) reduced the project to a single open number, the UV boundary `α_s(E_P)`.
This patch opens Route B (the lattice-discreteness / PSR-saturation route to that number) by
(1) writing the framework precisely, (2) showing PSR fixes the *sign*, and (3) proving the
**sensitivity theorem** that governs what any closure must achieve. It deliberately stops before
the unjustified quantitative leap.

## 1. Framework: Λ_QCD is the IR Landau pole of a one boundary-value flow

With the exact coefficient `β₀ = 7` (SS-1 `thm:beta0`) and the one-loop relation
`α_s(Q) = 2π/(β₀ ln(Q/Λ_QCD))`, dimensional transmutation gives

```
Λ_QCD = E_P · exp(−2π / (β₀ α_s(E_P))),   E_P = ℏc/l_P ≈ 1.22×10¹⁹ GeV.
```

`Λ_QCD` is not an independent input — it is the IR Landau pole, fixed *entirely* by the UV boundary
value `α_s(E_P)`. So "derive Λ_QCD from l_P" ≡ "fix `α_s(E_P)` from the substrate."

## 2. PSR saturation fixes the sign (the qualitative half, already consistent)

`rem:psr`: as `r → l_P`, `PSR_eff → l_P/2`, the Sea cannot nucleate qDP chains fast enough to
self-collimate, the string tension vanishes, and `α_s → 0`. Short distance `r → l_P` is high
momentum `Q → E_P`. Therefore PSR saturation **predicts `α_s(E_P) → 0`** — asymptotic freedom read
off the CPP substrate. The target value (next section) is small and positive, so PSR fixes the sign
and the smallness correctly. What PSR does *not* yet fix is the precise rate of approach to zero —
and that rate is the whole quantitative game.

## 3. The quantitative target

Reproducing `Λ_QCD = 0.218 GeV` from `E_P` with `β₀ = 7` requires

```
N_target = ln(E_P/Λ_QCD) = 45.47,    α_s(E_P) = 2π/(β₀ N_target) = 0.01974.
```

The genuine CPP coupling `5/(8φ) ≈ 0.386` (SM-7) is **not** this number — it is the IR anchor
(Patch 1001: it sits at `Q ≈ 2.2 GeV` under the same running). The continuum log evaluated from
`0.386` at `E_P` gives a run-length `N = 2.32`, hence `Λ ≈ 10¹⁸ GeV`. This is the rigorous
statement of the "factor-of-huge" obstruction: continuum-log running with the actual lattice
coupling does not produce a QCD scale.

## 4. The sensitivity theorem (the bar every route must clear)

From `Λ = E_P e^{−N}` with `N = 2π/(β₀ α_UV)`:

```
dΛ/Λ = (N/α_UV) · dα_UV.
```

At `N ≈ 45.5`, `α_UV ≈ 0.0197`, the amplification is `N/α_UV ≈ 2.3×10³`. Concretely, `α_UV` must be
pinned to `±9×10⁻⁵` (absolute) — about **±0.5%, i.e. roughly three significant figures** — to fix
`Λ_QCD` to ±20%; a percent-level `Λ` needs `α_UV` to ~0.1%. **Consequence: any closure must supply
an *exact closed-form* relation for `α_UV`. Matching `α_UV` (or an enhancement factor) to a "natural"
constant at the ~1% level is worthless.**

Demonstration (verify §D): the S³ volume `2π² = 19.74` — a tempting enhancement factor, since the
600-cell tiles S³ — lies within ~1% of the ratio `R₀ = N_target/N(0.386) = 19.57` that would be
"needed," yet predicts `Λ = 0.147 GeV`, **−33%** off target. A ~1% error in the geometric factor
becomes a ~33% error in `Λ`. Coincidence-hunting is ruled out *as a method*, not just in this
instance.

## 5. What Route B therefore has to compute (sharpened target)

Route B is now stated precisely and falsifiably:

> Derive `α_s(E_P) = 0.0197…` to **sub-percent / exact-identity** precision from the rate at which
> `PSR_eff → l_P/2` is approached on the 600-cell — i.e. from the lattice mode structure that makes
> the running non-logarithmic in the top decade — using only `l_P`, `sea_strength = 0.185`, and the
> 600-cell geometry, with **no PDG input**.

The non-log/discreteness content enters as a correction `g(Q)` to the running,
`dα_s/d ln Q = −(β₀/2π) α_s² · g(Q)`, with `g → 1` in the IR (continuum recovered) and `g`
deviating near `Q → E_P`. The job of Patch 1003 is to *derive* `g` (equivalently, the
`PSR_eff → l_P/2` approach profile) from the 600-cell mode count — not to posit it — and read off
`α_s(E_P)`. If the derived `g` yields `α_s(E_P)` matching `0.0197…` to the precision §4 demands,
the project closes; if it lands at the wrong value, or only matches at a precision §4 shows to be
insufficient, the falsifier fires.

## 6. Honest status

**Not closed.** This patch reframes a 20-order problem into one sharp, falsifiable, sub-percent
question and proves the precision bar that decides it. It also makes explicit the central tension of
the entire project: deriving a dimensionful IR scale to sub-percent accuracy from a UV coupling is
the generic hard problem of dimensional transmutation, and whether CPP's 600-cell mode structure can
meet that bar — rather than merely being *consistent* at the order-of-magnitude level — is exactly
what separates "derived" from "permanently calibrated" (the falsifier's two terminal outcomes). No
THEO/PRED registered; SS-1 and the DP-Sea appendix untouched.

*(Verify: `code/verify_uv_sensitivity.py` — framework facts A–D, exit 0.)*
