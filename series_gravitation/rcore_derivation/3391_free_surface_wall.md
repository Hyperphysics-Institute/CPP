# The instability was mine: the register was pinned at a FIXED radius. A saturated surface is a FREE boundary; pinning the register on the moving surface gives one Robin law, stable everywhere — and at the ratified surface the even-sector lines are 195 Hz (Q ≈ 99) and 292 Hz (trapped), within 2% of the numbers GR-2 shipped from a different chain

**Patch 3391, Session 161, 3 Sep 2026.** Verify `code/3391_free_surface_wall_verify.py` (8/8; 3383 machinery at `r_w = 8M/3`). Founder statement OPEN-GR-SEEDS. Reasoning `reasoning/3391.md`. Resolves OPEN-GR-SURFACE-STABILITY-1 (branch e, not on the 3390 list).

## §1 Branch (a) is dead: the one-Moment delay is no regulator
The register responds one Moment late: `β → β(ω)e^{−iωt_P}`, `Im β ≈ −β ω t_P`; at 191 Hz `ω t_P = 6 × 10⁻⁴¹`. It cannot touch a growth rate of 0.034/M.

## §2 The counting error at 3378 — and the correct wall law
The register `v` sets **two** dictionaries: the conformal factor `ψ(v) = 1 + v/2` and, since R-PSR-LAW-LOG + R-CLOCK-RATE-IS-DISPLACEMENT, the lapse `N(v) = (1 − v/2)/(1 + v/2)`. A register perturbation `δv` therefore appears in the even sector twice: in the trace, `(H₂ + 2K)/3 = 4(ψ′/ψ)δv`, and in the lapse, `H₀ = 2(N′/N)δv` — and in RW gauge `H₀ = H₂`. **Pinning the register at a fixed radius** (`δv = 0`, which is what 3378's trace-Dirichlet did, using only the first dictionary) actually imposes *both* `H₂ + 2K = 0` and `H₂ = 0`, i.e. `K = H₂ = 0`: `Z` and `Z′` both fixed — the even sector is **excluded**, not reflected. Enforcing only one of the two (the trace) gave a wall that is a boundary "mass" of the wrong sign beyond 2.38 M — the 3390 instability.

A saturated surface is a **free boundary**: its radius can move, `r_w → r_w + ξ`. The register is pinned *on the moving surface* (Lagrangian condition `δv + ξ v′ = 0`), and the *same* `ξ` enters both dictionaries. Eliminating `ξ`:

    H₂/(2 N′/N) = (H₂ + 2K)/(12 ψ′/ψ)   ⟹   **(4 − 3v/2)·H₂ + 2K = 0**   at the wall.

At the ratified surface `v = 2/3`: `3H₂ + 2K = 0`. (At the old wall `v = 1`: `2.5H₂ + 2K = 0` — so even at 9M/4 the 3378 law `H₂ + 2K = 0` was the fixed-surface limit and is superseded.) Through the Zerilli reconstruction this is one Robin law `β_ℓ^free(ω) = b₀ − b₂ω²` with, at `r_w = 8M/3`: **ℓ = 2: 7.637 − 55.17ω²; ℓ = 3: 196.2 − 627.2ω²** — `b₂ > 0` for both: a *positive* boundary mass. Stable.

## §3 The poles at the ratified surface (62 M_⊙)

| ℓ | Dirichlet (reference) | **free-surface, derived** | Hz | Q |
|---|---|---|---|---|
| 2 | 0.3855 − 0.204 i (Q 0.9) | **0.37487 − 0.00190 i** | **195** | **99** |
| 3 | 0.6284 − 0.207 i (Q 1.5) | **0.55964 − 0.00008 i** | **292** | **~3500** (below the barrier top 0.610: trapped) |

r0-independent to 10⁻¹⁵; residuals < 10⁻⁶. **The even sector at the ratified surface is stable, and it rings.** The Neumann crossings (0.372, 0.559) again sit at/below the barrier tops (0.389, 0.610) — the 3383 regularity, at the new wall and the new law.

## §4 The coincidence, recorded as such
GR-2 V1.6 shipped **191 Hz and 288 Hz** — Kerr χ = 0.68, *odd* sector, `X = 0`, surface at 9M/4. The free-surface *even* sector at a = 0, derived wall, ratified PSR law, surface at 8M/3 gives **195 Hz and 292 Hz.** Within 2%, from a chain that shares almost nothing with the shipped one. It is **not** a confirmation — different spin, different sector, different wall, different radius — and it is too close to ignore. Registered as COINCIDENCE-TO-BE-TESTED: the honest test is the Kerr recompute (OPEN-GR-KERRWALL-1) of *this* wall.

## §5 The odd sector at the ratified surface (3390): unchanged — 208 Hz, Q 7.9 (registered shear, J = 6.75).

## §6 What now stands, and what moves
- The surface: **areal 8μ/3 = 1.33 r_S** (R-PSR-LAW-LOG), lapse ½, z = 1, cavity 0.70 ms — **no longer held**; the stability objection is resolved.
- The even wall: free-surface law `(4 − 3v/2)H₂ + 2K = 0`, supersedes 3378/3383's trace law and CONV-039's Q1 object (the panel audited the fixed-surface limit; the change is strictly a correction of a counting error and is disclosed as such).
- The odd wall: registered shear, unchanged.
- **Enactment owed** (next patch, on the founder's word): GR-1c Corrigendum 4 (surface at 8μ/3), GR-2 V1.9 (the a = 0 line set: even 195/292, odd 208; Kerr still open), PRED-O-39, SR-1 corrigendum (SR lane), ledger.
- **OPEN-GR-SEEDS** minted from the founder's statement.

## §7 To the founder
Nothing to rule; one thing to know. Your answer contained no substrate principle forbidding the instability, and none was needed: the instability was an error in my boundary counting, and the physical statement "a saturated surface is free to move" removed it. The three ideas you offered are the *sources* the echo must be computed from — registered.
