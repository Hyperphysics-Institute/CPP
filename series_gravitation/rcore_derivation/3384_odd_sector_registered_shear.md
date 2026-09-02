# OPEN-GR-ODDWALL-1 — The axial sector under R-SHEAR-MUST-BE-REGISTERED, priced under both c_* brackets: under the CPP map the shipped axial line survives to 0.1%; under the Schwarzschild map it drops 5% and a second echo family appears in band

**Patch 3384, Session 161, 2 Sep 2026.** Verify `code/3384_odd_sector_registered_shear_verify.py` (14/14). Reasoning `reasoning/3384.md`.

**Standing:** COMPUTED at a = 0 under the founder's rule (3382), with the one unminted input — the strong-field c_* map — carried as a parameter `J = dr*/dr̄|_wall` and evaluated at both brackets. The Dirichlet reference reproduces 3356 (0.44859 − 0.11749i) to 1e-4.

## §1 The rule as a boundary condition

The shear is registered in SSV_net (uncapped); the surface does not refuse it; the axial wave enters the flat-register core and returns by regularity at the centre. Interior: `ψ_in = x j_ℓ(x)`, `x = k r̄` (Riccati–Bessel). Interface at `r̄ = μ`: `ψ` and `dψ/dr̄` continuous. With `J = dr*/dr̄` at the surface and unit speed in `r*`, `k = Jω`, and the wall law on the exterior RW function is

    (dψ/dr*)/ψ = (1/J)·k·g(kμ),   g(x) = (x j_ℓ)′/(x j_ℓ).

Real on the real axis (lossless: |R| = 1); `→ (ℓ+1)/J` as ω → 0. **The entire odd-sector wall depends on one number, J:** bracket I (CPP, `c_* = c/(1+u)`) `J = 2`; bracket II (Schwarzschild isotropic dictionary `N/ψ²`) `J = 6.75`. These are 3374's 4 μ/c and 13.5 μ/c rows; the 9 μ/c row was a mixed convention and is dropped.

## §2 The poles (ℓ = 2, M = 1, 62 M_⊙)

| wall | Mω | Hz | Q | shift |
|---|---|---|---|---|
| Dirichlet `X = 0` (shipped) | 0.44859 − 0.11749 i | 233.8 | 1.91 | — |
| **derived, J = 2 (CPP map)** | **0.44896 − 0.09497 i** | 234.0 | 2.36 | **+0.1%** |
| **derived, J = 6.75 (Schwarzschild map)** | **0.42512 − 0.04018 i** | 221.6 | 5.29 | **−5.2%** |

**Under the CPP map the shipped axial position survives.** A Robin coefficient of 1.5/M at the barrier top acts like Dirichlet; the shipped `X = 0` was, for this bracket, an accident that landed within 0.1% of the derived answer (the width narrows a little). Under the Schwarzschild map the line drops 5% and sharpens.

**The interior-cavity family** (the "second timescale"): for J = 6.75, leaky interior modes at Mω = 0.83 (433 Hz, Q 1.7) and 1.35 (702 Hz), spacing π/(Jμ) = 0.47 — a second echo family *in band*. For J = 2 the family sits above Mω ≈ 2.9 — effectively absent.

## §3 What the c_* map is now worth

The unminted NOTE-GR-CSTAR-STRONGFIELD decides: (a) whether the axial line moves 0% or 5%; (b) whether a second echo family exists in the LIGO band; (c) the 3374 core round-trip (1.2 ms vs 4.1 ms). Three consequences from one number. **It should be minted** — the T-1 charter question "what is the coordinate census speed at the surface in absolute time, and how does it map to a far observer's clock" is now the single most valuable open input in the arc, and it is a *scalar dictionary* question (the exterior kinematic map, R-CSTAR-MAP, ratified at 3262 for the weak field), not a reconstruction.

## §4 The two sectors side by side (a = 0)

| | even (Zerilli) | odd (RW) |
|---|---|---|
| register | SSV_abs (capped; over-demanded) | SSV_net (uncapped) |
| wall | trace-Dirichlet → Robin `β_ℓ(ω)` (3378) | transmit → interior regularity, Robin `(1/J)k g(kμ)` |
| ℓ = 2 pole | 0.4116 − 0.0082i, Q 25 (3383) | 0.449 − 0.095i, Q 2.4 (J=2) / 0.425 − 0.040i, Q 5.3 (J=6.75) |
| shipped X = 0 | wrong sector; wrong law | right sector; law survives under the CPP map |

The two halves of the wave see two different surfaces because they live in two different registers. The even sector is the sharp one.

## §5 Owed
- Mint the c_* map (T-1 charter; founder picture likely needed: "does a DI-bit hop one PSR per Moment in the *lattice* or in *proper* distance?").
- The O(kd) skin term (even sector, amplitude).
- Kerr: both sectors, OPEN-GR-KERRWALL-1.
- GR-2: one paragraph at the next version (3383 poles + this table).
