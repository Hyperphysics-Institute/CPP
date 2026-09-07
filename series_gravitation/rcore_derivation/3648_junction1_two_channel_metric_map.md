# OPEN-GR-SURFACE-IMPEDANCE-1 attempt 2b FAILS, informatively: JUNCTION-1 proper — the count and tensor channels imposed each on its own component through A3′'s metric map (3378's reconstruction), not summed. At ω_QNM the two channel demands on the one wall value Z′/Z differ by 0.92 (the whole target is 0.116); no frequency near the ringdown satisfies both; each alone is outside the box. Verdict: a sharp wall with two independently-lawed channels is not the junction — the interior must supply ONE even-parity law for (H₂, K) together. Attempt 3 named: the budget medium's own linearized equations (its effective ρ, P from the budget metric), matched C¹. Static by-product: the wall-law route at ω = 0 disagrees with 3647's level-set reading — OPEN-GR-LATTICE-FRAME-1's static face, now with numbers; row 6 carries the caveat

**Patch 3648, Session 163, 6 Sep 2026.** Verify `code/3648_junction1_two_channel_metric_map_verify.py` (10/10; execs 3644's machinery; 3378's reconstruction re-derived symbolically). Reasoning `reasoning/3648.md`. No paper touched.

## §1 What "coupled through the metric map" means, concretely
3378: `K = f Z′ + A Z`, `H₂ − K = c₁(ω, r) Z + c₂(r) Z′`. The register (count) channel is the spatial trace `T = H₂ + 2K` (`δ ln ψ⁴ = T/3`); the tensor channel is the traceless part `D = H₂ − K`. 3643/3644 imposed the budget interior's count law on **Z itself** — i.e. treated the Zerilli function as the count field. 2b imposes each law on its own component: `(dT/dr*)/T = β_c(ω)` with `β_c` = the budget interior's lossless law (3643/3644), and `(dD/dr*)/D = β_t(ω) = −iω` (the tensor content absorbed by the core, 3609–3610/3621). With `Z″` eliminated by the Zerilli equation, each is a Robin law on `Z`. Sanity: the `β_c → ∞` limit (trace pinned, `T = 0`) recovers the 3390 clamp's law at 8M/3, `b₀ = −2.57`.

## §2 The numbers at ω_QNM (a = 0, ℓ = 2, 8M/3)
| law on Z′/Z (in r*) | value | note |
|---|---|---|
| target `β_hor` | +0.008 − 0.116 i | the horizon's admittance at 8M/3 (3644) |
| hypothesis `−iω/3.22` | −0.028 − 0.116 i | H-SURFACE-IMPEDANCE |
| 3644: budget law on Z | +0.413 + 0.081 i | fails (transparent) |
| **2b count channel T** | **+0.405 + 0.137 i** | nearly the same as putting it on Z: the map changes little |
| **2b tensor channel D** | **−0.086 − 0.638 i** | absorbs **5.5×** the target |
| `|lawC − lawT|` | **0.92** | two demands on one number |

- Poles, each law alone: count-channel wall `0.4919 − 0.1769 i` (+31.6% / −49.7%), tensor-channel wall `0.3615 − 0.1612 i` (−3.3% / −44.8%). Both outside the box.
- Compatibility locus `lawC(ω) = lawT(ω)`: **no root** in `0.05 < Re ω < 1`, `−0.6 < Im ω < 0.05`.

## §3 What the failure says
1. Putting the count law on the trace component instead of on Z moves the answer by < 0.06: the count field, however it is placed in the RW reconstruction, is not where the target's structure lives. The real-part problem of 2a (the trace element's large `Re β`) is the count channel's, in every placement.
2. The tensor channel absorbed at the exterior's local speed over-absorbs by 5.5×. The core does not take the tensor content at the exterior's rate — it takes it slower. That is the *direction* of the hypothesis (`s ≈ 3` slower), stated here from the tensor side; it is not a derivation of `s`.
3. **A sharp wall with two independently-lawed channels is overdetermined**: one exterior even mode has one `Z′/Z`; two channel laws are two demands on it, and they never agree near the ringdown. The junction cannot be a pair of scalar laws at a surface. **The interior must present one even-parity law for `(H₂, K)` jointly** — the linearized field equations of the budget medium itself. Under σ = P = 0 (3640, C¹) that is exactly what GR's junction requires: continuity of `(H₂, K)` and their normal derivatives against an interior solution of the interior's own perturbation equations. 3643's scalar proxy was a stand-in for that interior law; 2a/2b show the stand-in cannot be made to carry the tensor channel by any surface rule.

**Attempt 3 (named, not executed):** read the budget metric's effective stress-energy `(ρ(r̄), P(r̄))` from `G_μν` (3640 already has `m(r̄)`), perturb it with the standard even-parity stellar equations (Lindblom–Detweiler at ω ≠ 0; Hinderer at ω = 0), and match C¹ to the Zerilli exterior. No constant enters; the interior's dissipation (OPEN-GR-CORE-DISSIPATION-1) is the one thing the effective fluid does not contain and would have to be added as an equation-of-state statement. The same computation gives the static Love number in one framework (§4).

## §4 Static by-product: OPEN-GR-LATTICE-FRAME-1's static face, with numbers
At ω → 0, mapped to Hinderer's `y = R H′/H` through the same reconstruction: count-channel law `y = +28.3` (`k₂ = −0.012`), tensor-channel law `y = −9.15` (`k₂ = −0.111`). 3647's level-set reading: `y = −3.22`, `k₂ = +0.042`. The Robin-on-trace route at ω = 0 and the level-set route disagree. Both say "the count is free at the surface"; they differ in what the RW-gauge trace at the wall has to do with the lattice count — 3633 §2's c07/C5 discrepancy at O(v). **Row 6's `+0.042` stands as the level-set reading and now carries the caveat**: the wall-law reading through the RW map does not reproduce it. Attempt 3 (the effective-fluid k₂) is the arbiter — it is gauge-invariant. Also corrected: Hinderer's `k₂ > 0` band at C = 3/8 is `y* = −6.81 < y < 5` (numerator zero at y = 5), not all `y > y*` as 3647 §4 wrote.

## §5 Standing
- OPEN-GR-SURFACE-IMPEDANCE-1: attempts 1 (3645), 2a (3646), **2b (3648) failed**; attempt 3 named (effective-fluid interior, C¹). H-SURFACE-IMPEDANCE unchanged (3/3 descriptive; Kerr, overtone, static member owed).
- Ledger row 7: unchanged (fails as written; requirement recorded). Row 6: passes as the level-set reading; **STATIC-FRAME caveat (3648 §4)** attached; arbiter = attempt 3.
- Owed, unchanged: KERRWALL-1; odd-sector re-run at 8M/3 with J = 32/9; Leaver solver for the overtone.
