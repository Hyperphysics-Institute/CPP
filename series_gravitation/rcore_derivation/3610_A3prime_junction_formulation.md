# The even-sector junction under A3′ — formulated, not yet computed: the trace pins on the level set (Φ capped), the traceless part is Q_ij content (uncapped) and relays into the core; C5's readout fixes the map; the gauge plan and the risks, stated before the numbers

**Patch 3610, Session 161, 4 Sep 2026.** Governance: the AP-4 ↔ A3′ harmonisation note enacted in `axiom-registry.md` (owed since 3609). Physics: formulation only; the numbers follow in the next patches. Reasoning `reasoning/3610.md`.

## §1 The register at the surface under A3′
Per GP: `(Φ, V_i, Q_ij)`. The cap (3375, R-FLOOR-REGISTER) is on **Φ** (`SSV_abs`) only. `V_i` and `Q_ij` are uncapped — they relay through the core with the identical wave operator (A3′ clause C3) at the core's uniform `c_* = c/2` (the ratified floor; `J = 6.75` under R-PSR-LAW-LOG).

## §2 What each sector does at the surface — the complete picture
| sector | register content | at the surface |
|---|---|---|
| even, trace part `(H₂ + 2K)` | Φ | pinned on the moving level set — the 3391 kinematic law (both scalar dictionaries, one displacement) |
| even, traceless spatial part `(H₂ − K)` | Q_ij | uncapped → continuous into the core → interior tensor wave, regular at the origin (turn-around at `√6/k`) |
| odd (axial) | V_i (the curl part; B-type/arc) | uncapped → continuous into the core (3384) |

So the even sector is a **two-channel junction** (as 3396 first said), now axiom-backed, with **no free coefficient**: C5's readout gives the map `h̄_ij ← Q_ij + ⅓δ_ij τ` (trace-reversed, harmonic-pattern assembly), i.e. the traceless spatial metric perturbation *is* `Q_ij`, with the strain-valued convention inherited from c07.

## §3 The gauge plan (where the errors would come from)
The exterior mode is computed in RW gauge (`K, H₂, H₁` from `Z⁺`, all derived at 3378/3398); C5's assembled metric is in the harmonic pattern. The register's `Q_ij` at the wall is the *harmonic-gauge* traceless spatial part. So the matching needs the RW → harmonic gauge transformation of the Zerilli mode at the wall — a known, finite algebraic step (a gauge vector `ξ_μ` solving `□ξ_μ = −∂^ν h_{μν}^{RW}` with the residual harmonic freedom fixed by regularity) — and it is exactly the step at which a recalled formula would be dangerous. **It will be derived, as 3398 was, from the linearized equations directly, and checked by two independent routes** (the trace-reversed harmonic form of `H₂ − K`; and the gauge-invariant Moncrief quantity, which must agree with `Z⁺` up to the known factor).

## §4 The interior tensor wave
An even-parity ℓ = 2 rank-2 field in the flat core: the electric-type tensor harmonics, radial functions regular at the origin (`x j_ℓ(x)`-type, with the tensor-harmonic ladder relating the components). The 3384 machinery applies component-wise (C3: same operator). Two interior amplitudes may appear (the tensor harmonic has two even radial types); regularity fixes their ratio; one amplitude `T` remains.

## §5 The junction equations
Unknowns: exterior reflection `R` (of `Z⁺`), interior amplitude `T`. Conditions: (i) level set `(4 − 3v/2)H₂ + 2K = 0` — **unchanged**, since it constrains the trace channel and Φ's level set does not see Q_ij (traceless); (ii) `Q_ij` continuity: `[H₂ − K]^{harm}_{ext}(Z⁺, Z⁺′) = T·q_ℓ(kr_w)`; (iii) the register counts both sides (3397): the *returning* interior `Q_ij` wave contributes to the count only through `|Q|` — second order in amplitude at the surface — so at linear order (i) is unmodified. Then: **(i) alone fixes `Z⁺′/Z⁺` at the wall and hence `R` with |R| = 1** — as at 3391 — and (ii) fixes `T`. The 3396 "leak" question returns: energy flows into the core through `Q_ij` while the exterior reflects fully?

**Resolution under A3′, stated as the hypothesis to be computed:** the exterior even mode is one DOF; if (i) pins it completely, the interior `T` is *sourced* by the wall's traceless content without back-reaction at linear order — the energy in `T` is not taken from the reflected wave but *is* the part of the incident wave's energy that was in the traceless channel, which |R| = 1 on `Z⁺` does not account for because `Z⁺` is normalised to the *exterior* flux only through the trace-reconstructed components… This is exactly the kind of sentence that must be replaced by a computation. The C5 Operational-Energy Lemma (Patch 1127: absorption is TT-only, no independent channel energy) is the tool: the energy ledger of the junction must close under C5, and whichever of "|R| = 1 with a decoupled interior" or "|R| < 1 with a coupled interior" closes it is the answer. **OPEN-GR-JUNCTION-1's charter is now: close the C5 energy ledger at the wall.**

## §6 Order of work (next patches)
1. RW → harmonic gauge map of the Zerilli mode at the wall, derived and double-checked (the 3398 method).
2. The interior even tensor wave, regular, with `J = 6.75`.
3. The junction with the C5 energy ledger; `R(ω)`, `T(ω)`; the a = 0 even poles with both channels.
4. GR-2 V2.0 candidate line set (a = 0, both sectors, both channels); the Kerr test (KERRWALL-1) after.

## §7 Governance enacted
`axiom-registry.md`: Harmonisation note AP-4 ↔ A3′ — one packet `{address; Φ, V_i (as E, S), Q_ij}`; AP-4d extends to rank 2; no count change; R-RANK-2-REAFFIRMED recorded.
