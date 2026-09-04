# The sign is the theory's: under A3′ the static interior is rigid (a uniform strain is pure gauge; the curved interior solution needs stress a capped core lacks), so k₂ = −0.080 stands. And the magnetic Love number: k₂^B ≈ +0.03 (BH-subtracted; convention flagged) — a second static response a horizon lacks

**Patch 3625, Session 161, 4 Sep 2026.** Verify `code/3625_interior_tide_and_magnetic_love_verify.py` (6/6). Reasoning `reasoning/3625.md`.

## §A The interior's static tidal response under A3′ — no new degree of freedom
The interior's traceless register `Q_ij` obeys `∇²Q_ij = 0` statically (sourceless, C3), regular at the origin. Its regular ℓ = 2 solutions:
- **the constant traceless strain** — linearized Riemann identically zero: **pure gauge**. It is the uniform ellipsoidal deformation of the core, i.e. exactly the moving level-set surface of the rigid-interior model (3624). Nothing new.
- **the quadratic solution** `x_i x_j − δ_ij r²/3` — harmonic component-wise, but its linearized Riemann is nonzero: it carries curvature and must be **supported by interior stress**. A core at the register cap has no static traceless stress to supply it (the count is capped; the medium uniform; the founder's tide deforms the *surface*, the interior stays at cap).

So in statics the A3′-consistent interior *is* the rigid one. **The electric Love number `k₂ = −0.080` (`Λ ≈ −7`) is the theory's, sign included.** The negative sign — the induced quadrupole opposing the tide — is the response of a rigid body whose *surface* is a level set of the external potential: the bulge is where the register is fed, and the induced field of that bulge opposes the tide at the exterior order that defines `k₂`. (Negative Love numbers are known for thin-shell ECOs.)

## §B The magnetic (axial) Love number
- The static axial ℓ = 2 equation, derived from `δR_{tφ} = 0`: `h₀″ = 2(3r − 2M)h₀/(r²(r − 2M))` — the standard form. `h₀ = r³` is its flat-space limit, not an exact solution.
- Surface condition from the odd-sector picture (3382/3384): `V_i` is uncapped and continuous into the flat core, whose regular static axial solution is `h₀ ∝ r³`; the background `g_tt` is continuous at the surface (`f(R) = ¼ = N²` — the level set itself), so `h_{tφ}` and its radial derivative are continuous: **`R h₀′/h₀ = 3`** at `R`.
- Exterior: `h₀ = h_grow + λ h_decay` integrated inward from 300 M; the horizon-regular solution integrated outward from `r = 2M + 10⁻⁴` (Frobenius start `h₀ ∝ (r − 2M)`). Asymptotic `b/a` (`h₀ → a r³ + b r⁻²`) for each; the **difference** is the R-core's magnetic response (the common part is the Schwarzschild growing solution's own `M/r` tail, which the two-term decomposition mis-assigns — identical for both and cancelling in the difference):

    `Δ(b/a) = 7.97 M⁵` → **`k₂^B ≡ ½ Δ(b/a)/R⁵ = +0.030`** (normalization convention flagged: axial Love numbers are defined with author-dependent factors; the *ratio to the electric one* and the sign are the content).

- A black hole: 0. The R-core: `k₂^B ≈ +0.03`, positive, about 40% of `|k₂|`.

## §C Standing
- The R-core's static tidal signature, complete at a = 0: **`k₂ = −0.080` (Λ ≈ −7), `k₂^B ≈ +0.03`**; a horizon has 0 and 0. Both within Einstein Telescope / Cosmic Explorer reach for loud events; both zero-parameter.
- Owed: spin dependence (ansatz A's surface); the exact convention for `k₂^B` (a literature read, or a derivation of the axial Love-number definition from the asymptotic metric — the corpus can do the latter); the 5PN phasing coefficient.
- Row 1 of the observable list (3622) is complete.
