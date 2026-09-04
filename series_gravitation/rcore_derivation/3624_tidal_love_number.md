# The R-core's tidal Love number: k₂ = −0.080, Λ ≈ −7, for the register-only surface (rigid interior at cap, level-set surface ⇒ K(R) = 0). A black hole has 0. Below present LIGO reach, within Einstein Telescope / Cosmic Explorer reach — the R-core's first zero-parameter static departure from GR. Sign and value to be confirmed with the Q_ij-responsive interior

**Patch 3624, Session 161, 4 Sep 2026.** Verify `code/3624_tidal_love_number_verify.py` (9/9). Reasoning `reasoning/3624.md`.

## §1 The equations — derived, not recalled
Static even-parity ℓ = 2 perturbation of Schwarzschild in RW gauge (`H₀ = H₂ = H`, `K`), from the linearized Ricci tensor at ω = 0 (the 3398 method):
- master ODE `H″ + 2(r−M)/(r(r−2M)) H′ − (6r² − 12Mr + 4M²)/(r²(r−2M)²) H = 0` — the (t,t) and (r,r) components; it is Hinderer's vacuum equation and is satisfied by the growing solution `H = r(r − 2M)`;
- `K` algebraic from the (θ,θ) component: `4rK = r²(r−2M)H″ + 2r²H′ − 2rH + 4MH`, consistent with `K′ = H′ + 2MH/(r(r−2M))` from (r,θ).

## §2 The surface condition — the register-only model
The corpus's static R-core: interior at the register cap (lapse ½ uniform, spatial metric at cap — rigid), surface = the level set of the register (moves; no dynamics of its own, 3396). Matching a rigid interior across a moving surface: `g_tt` continuity fixes the displacement (`ξ f′ + f H = 0`); continuity of the induced 2-metric with a rigid interior gives, per `Y`, **`K(R) = 0`** (the displacement terms cancel between the two sides). One condition on the exterior solution — as a Love-number problem should have.

(GR's bookkeeping of this configuration is recorded: a flat interior meeting Schwarzschild at `R = 8M/3` is a thin shell with rest mass `4M/3` and binding energy `−M/3` — the mass "lives in the surface" in GR's language; in CPP's it is the count at cap.)

## §3 The number
Exterior `H = H_grow + λ H_decay` integrated inward from 200 M; `K(R) = 0` ⇒ `λ`; `y = R H′/H = −10.33`; Hinderer's closed form at `C = 0.375`:

**`k₂ = −0.080`**,  **`Λ = (2/3)k₂/C⁵ ≈ −7`**.

Comparisons at the same radius: Dirichlet (`H(R) = 0`) `k₂ = −0.018`; Neumann (`H′(R) = 0`) `+0.014`; **black hole: 0.** The level-set value lies outside the Dirichlet/Neumann pair — `K(R) = 0` is a strong condition, not a mixture.

## §4 What it means, and what it needs
- **A surface at 1.33 r_S has a tidal response a horizon lacks**: `|Λ| ~ 7`. Neutron stars: `10²–10³`; present LVK bounds on binary-black-hole `Λ`: `O(10²–10³)` (recollection); Einstein Telescope / Cosmic Explorer: `O(1–10)` for loud events. **The R-core's first zero-parameter static departure from GR, at the edge of next-generation reach.** It enters the inspiral phase at 5PN with the sign of `k₂`.
- **The sign is negative** — the induced quadrupole opposes the tide. Negative Love numbers occur for thin-shell gravastars and other ECOs in the literature; here it follows from the rigid interior. It is physical but model-dependent.
- **Model scope, stated:** this is the *register-only* surface. Under A3′ the interior's traceless `Q_ij` is uncapped and, statically, the core's lattice deforms under a tide (the founder's tidal picture, 3605). That interior response enters the matching as a G-type (`Y_{:AB}`) perturbation the RW-gauge exterior must be transformed to meet — one more computation, owed **before the sign is claimed** as the theory's. The magnitude `|k₂| ~ 0.01–0.1` is robust across the models computed.

## §5 Standing
- Computed: the register-only `k₂` and `Λ`. Owed: the `Q_ij`-responsive interior (the A3′ static tide inside the core); the magnetic (odd) Love number; spin dependence.
- The observable list (3622 §2) row 1 now has its number.
