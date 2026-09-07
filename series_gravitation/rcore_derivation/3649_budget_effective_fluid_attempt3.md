# OPEN-GR-SURFACE-IMPEDANCE-1 attempt 3 FAILS, informatively — and answers 3640 §4 on the way. The budget interior's effective stress-energy, read off its own metric: a positive-density body of mass M whose density rises outward (0.005 → 0.028), p_r → 0 at the surface (the C¹ join), **anisotropic** with p_t(R⁻) = 0.0070 ≠ 0 — the interior is held static by tangential stress (3638's load moved inward, not removed). p_r has an interior maximum at r̄ = 0.86, so GR's barotropic closure is singular there: the static even-parity master equation (derived here for an anisotropic star; isotropic limit = Hinderer exactly; pipeline validated to k₂ → 3/4 on an incompressible star) has a diverging coefficient (ρ + p_r)/c_s². The budget medium is not a fluid. The interior's one even-parity law must be the register closure — attempt 3b named

**Patch 3649, Session 163, 6 Sep 2026.** Verify `code/3649_budget_effective_fluid_attempt3_verify.py` (16/16; everything symbolic re-derived in the script, nothing recalled except Hinderer's equation as the check target). Reasoning `reasoning/3649.md`. No paper touched.

## §1 The effective stress-energy of the budget interior
`G_μν` of `ds² = −N² dt² + ψ⁴(dr̄² + r̄² dΩ²)`, `N = N(v_eff)`, `ψ = ψ(v_eff)`, `v_eff = 2·cap − cap²/v`. The same operator on the exterior profile gives zero (vacuum), as it must.

| r̄ | ρ | p_r | p_t |
|---|---|---|---|
| 0 | 0.00500 | 0.00133 | 0.00133 |
| 0.8 | 0.00754 | 0.00141 | 0.00204 |
| 1.25 | 0.01504 | 0.00117 | 0.00398 |
| 1.5⁻ | 0.02798 | 0 | 0.00699 |

- `m(R) = M` to 10⁻⁶; areal `R = 8M/3`. `p_r(R) = 0`: the C¹ join of 3640 §3 from the matter side.
- **Anisotropic.** `p_t > p_r` everywhere inside, isotropic only at the centre; `p_t(R⁻) = 0.0070` while `p_r(R⁻) = 0`. **3640 §4's question — what holds the budget interior static — is answered: tangential stress.** The clamp's thin shell (3624 §2, 3638's `P = σ/4`) did not vanish under the budget law; it became a volume distribution of tangential stress, densest at the surface. The density profile says the same: the mass sits near the surface (a smeared shell).
- `p_r` rises to a maximum at `r̄ = 0.86` (areal 1.73 M) and falls to zero; `ρ` rises monotonically. So `p_r(ρ)` is double-valued and `dp_r/dρ < 0` outside the maximum: the barotropic sound speed is imaginary in the outer half.

## §2 The anisotropic static master equation (derived)
Areal RW gauge, `g = diag(−e^{2Φ}(1 + HY), e^{2Λ}(1 − HY), r²(1 − KY), …)`, `δT^μ_ν = diag(−δρ, δp_r, δp_t, δp_t)Y`, closure `δp_r = c_s² δρ`, `δp_t = δp_r + δσ`. From the linearised Einstein equations: (θθ)−(φφ) vanishes identically for any such T (H₀ = H₂ consistent); (rθ) gives `K′ = H′ + 2Φ′H`; (θθ) is algebraic in δρ; (rr) algebraic in K; (tt) is then the master equation `H″ + A H′ + B H = S`, `S ∝ δσ`. With `p_t = p_r` and TOV, A and B are Hinderer's exactly. The anisotropy enters only through `p_r′` (kept explicit) and the closure. Pipeline check: incompressible star, `y_in = 2`, surface jump `−3`, `k₂ = 0.7475` at `C = 0.001` (Newtonian 3/4).

## §3 Attempt 3, closure (a): FAILS
The only zero-parameter fluid closure is `δσ = 0` with `c_s² = dp_r/dρ` from the background. On the budget background `(ρ + p_r)/c_s² = (ρ + p_r)ρ′/p_r′` passes through ±∞ at the `p_r` maximum (+26.8 → −26.8 across 0.01 M). The regular solution from the centre reaches `r = 1.71 M` with `y = −7.8` and meets a singular point it cannot cross. **No static tidal solution exists under GR's fluid closure.** This is the background's property, not the perturbation's: the medium is not a barotropic fluid.

## §4 What it says
1. The effective fluid was the natural thing to try after 3648 (one law for (H₂, K), C¹). It cannot be that law, because the budget medium's equation of state is not a function `p_r(ρ)`. The register is not matter; `ρ, p_r, p_t` are what GR *reads*, not what the medium *is*.
2. Therefore the interior's one even-parity law must be the **register closure**: the whole interior metric perturbation follows from the perturbed count, `δg = (∂g/∂v_eff)·χ(v)·δv`, with `δv` obeying the count's own (sourceless, C3) equation. That closure has no `c_s²`, and permits `T^θ_θ ≠ T^φ_φ` (it is not a fluid) — which is where the A3′ tensor content sits. Its static face is 3633/3647's computation; **attempt 3b (named):** carry it out in one gauge, areal RW, with the perturbed `r̄ → r` map and the surface displacement, statically first (arbitrating row 6's 3648 caveat), then at ω ≠ 0 with 3643's count wave equation as the interior law — that is the coupled junction of 3648 §3 built as one field with a metric map, not two laws. If it reproduces the horizon admittance's small real part, OPEN-GR-SURFACE-IMPEDANCE-1 closes; if it gives the transparent wall again, the hypothesis stays a hypothesis and the missing piece is the tensor channel's dynamics (OPEN-GR-CORE-DISSIPATION-1) inside the register closure.
3. For the corpus's statics: the budget R-core's interior is a self-supported anisotropic body in GR's reading. OPEN-GR-SATURATED-CORE-1's "clock floor only" reading (3640 §5) is unaffected — stars have real pressure; the R-core's support is the register's own.

## §5 Standing
- OPEN-GR-SURFACE-IMPEDANCE-1: attempts 1, 2a, 2b, **3 failed**; attempt 3b named. H-SURFACE-IMPEDANCE unchanged.
- Row 6 caveat (3648 §4): arbiter is now attempt 3b's static run. Row 7 unchanged.
- New, derived, standing: the budget interior's `(ρ, p_r, p_t)`; the anisotropic static master equation (reusable for any corpus interior).
