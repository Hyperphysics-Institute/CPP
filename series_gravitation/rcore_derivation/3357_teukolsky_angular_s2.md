# Rung 3a — the gravitational (s = −2) angular sector: validated two ways, and 3353's fence is priced

**Patch 3357, 30 Aug 2026 — Session 157.** Verify:
`code/3357_teukolsky_angular_s2_verify.py`, **6/6 PASS** (all-FAST).

## §1 Validation, before any new number

Two independent known checks on the spin-weighted angular operator:

- **K1 (c → 0):** A = ℓ(ℓ+1) − s(s+1) = ℓ(ℓ+1) − 2, reproduced to 1e−7
  relative for every |m| = ℓ, ℓ = 4–12.
- **K2 (first-order slope, sign-sensitive):** dA/dc at c = 0 matches
  the known −2ms²/(ℓ(ℓ+1)) to 5e−4 — the check a c = 0 limit cannot
  see, and the one that would have caught a wrong sign in the 2csx term.

**Endpoint discipline, applied before running** (the 3353 lesson):
S ~ (1−x)^{|m+s|/2}(1+x)^{|m−s|/2}. ℓ ≥ 4 has both exponents ≥ 1 and
converges to machine precision. **ℓ = 3** has one exponent of exactly
½ and converges at **first order** (observed order 0.99) — reported
with a Richardson-extrapolated value and a stated ±9e−4, not dropped
and not passed off as exact. **ℓ = 2 is excluded** with its reason: for
s = −2, |m| = 2, one pole exponent is *zero*, which needs the
endpoint-regularised method. That is the observable line, so the
fence is stated up front.

## §2 The result, and the hypothesis it overturned

| ℓ | c = aω_top | A(s = −2) | A(s = 0) | residual beyond −s(s+1) | 1st-order prediction 8c/(ℓ+1) | relative to A |
|---|---|---|---|---|---|---|
| 3 | 0.3759 | 10.686 | 11.984 | +0.701 | +0.752 | 6.6% |
| 7 | 0.7995 | 54.695 | 55.962 | **+0.732** | +0.800 | **1.3%** |
| 9 | 1.0106 | 88.690 | 89.951 | +0.738 | +0.808 | 0.8% |
| 12 | 1.3270 | 154.679 | 155.935 | +0.744 | +0.817 | 0.5% |

**I expected the residual to shrink with ℓ. It doesn't — it sits at
~+0.7 and grows slightly. The failure was the hypothesis, not the
number.** The residual *is* the first-order spin-weight term
−2ms²c/(ℓ(ℓ+1)) = +8c/(ℓ+1) for m = −ℓ; since c = aω_top grows
~linearly with ℓ while the coefficient falls as 1/ℓ, the product tends
to a constant. The measured residual matches that analytic prediction
to within higher-order corrections at every ℓ.

**Relative to A ~ ℓ² it does shrink** — 6.6% at ℓ = 3, 1.3% at ℓ = 7,
0.5% at ℓ = 12 — the same order as the eikonal error 3354 showed
cancels in Φ.

## §3 What is and is not concluded

- **3353's fence is now priced:** the s = 0 proxy under-shoots the
  gravitational eigenvalue by an O(1) constant ≈ 0.73 across the
  ladder, i.e. ~1.3% at ℓ_crit.
- **Whether that cancels in Φ, as the eikonal error did at 3354, is
  NOT asserted.** The s = −2 census is not a drop-in Q replacement:
  the s = −2 radial operator carries extra −2is(r−M)K/Δ + 4isωr terms.
  That belongs to rung 3b, the heavy build.
- **ℓ = 2 — the observable line — remains open in the angular sector**
  and needs a method change (endpoint regularisation), not a rerun.

## §4 Registry

- RCORE-3 "s = −2 angular": **discharged for ℓ ≥ 3 on the |m| = ℓ
  branch; ℓ = 2 open (method change).**
- **Remaining: rung 3b — the radial Kerr Teukolsky/Sasaki–Nakamura
  build — plus the ℓ = 2 angular regularisation.** Both need the
  higher tier; both start from validated instruments.
