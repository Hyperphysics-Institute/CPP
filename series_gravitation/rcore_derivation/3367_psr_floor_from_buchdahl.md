# OPEN-GR-FLOOR-1 — The PSR floor l_P/2 re-derived from Buchdahl's bound (Route A) — **DERIVED-CONDITIONAL**

**Patch 3367, Session 161, 1 Sep 2026.** Verify: `code/3367_psr_floor_from_buchdahl_verify.py` (25/25). Reasoning: `reasoning/3367.md`. Founder rulings: `founders_voice/founder_ruling_exclusion_retired_register_floor_2026-09-01.md`.

**Standing:** DERIVED-CONDITIONAL on P3 (Einstein's equations holding in the saturated interior = OPEN-GR-FE-1 at saturation = **OPEN-GR-RCORE-4**). CONV-038 owed. HALT-GR-1C-FLOOR fired against the *proof text* of GR-1c Thm 2 (value preserved; premise void); no `.tex` touched.

---

## §0 Why this record exists

GR-1c Theorem 2 states `PSR_eff ≥ l_P/2` and proves it from the CP Exclusion Rule ("no two CPs may occupy the same GP" ⇒ minimum lattice spacing). Founder ruling **R-EXCL-RETIRED** (31 Aug–1 Sep 2026): that rule was eliminated earlier as unnecessary, replaced by ZBW + next-Moment SSV_net displacement, and one-CP-per-GP is "inconsistent with reality." No retirement was ever recorded; the GR lane inherited the rule as live from GR-1b and built the R-core arc on it (3297 |R| = 1, the Buchdahl relocation, 3320 Kerr surface, 3339/3359 wall modes, GR-2 V1.6, PRED-O-39).

Consequence: the floor's only derivation is void. The number `1/2` — the most-cited number in the lane — had, as of 3366, no standing at all. This record gives it one.

The proof in GR-1c also misreads `l_P` as the grid step; Patch 0733 already withdrew that reading for the inflation case (`l_P` is the baseline PSR, ~10³⁰ sub-Planck GPs; c01 "the true grid is sub-Planck (~l_P/10³⁰) by nesting"). A one-per-GP packing floor would therefore sit at ~10⁻³⁰ l_P, not l_P/2 — the packing premise gets the wrong number even on its own terms (verify Check 6).

## §1 Premises — and the one that is NOT here

- **P1 (exterior).** Exact Schwarzschild in isotropic coordinates with the ratified dictionary `u ≡ k·Δ|SSV| = μ/r̄`, `PSR_eff = l_P/(1+u)`, `μ = GM/c²`. [GR-1c Thm 1; T-1 CHARTER lattice ≡ isotropic, Patch 3262.]
- **P2 (incompressibility).** The saturated interior holds the SSV_abs register at a fixed maximum `u_max` throughout; density non-increasing outward. [Founder ruling R-FLOOR-REGISTER: "the register is just the value of the SSV_abs"; the floor is a register limit.]
- **P3 (static Einstein-consistent interior).** The saturated body is a static configuration on which the CPP field equation — shown equal to Einstein's at OPEN-GR-FE-1 closure — holds. **This is the conditional step.** GR-1c's own text says the `μ/r̄` form "ceases to apply" inside the core; whether FE-1 holds *at saturation* is exactly OPEN-GR-RCORE-4 (the substrate census functional), the A1–A3 conditionality the entire spin sector already inherits. Under P2 + P3, Buchdahl's theorem binds.
- **P4 (extremality).** The register saturates at the *largest* value admissible under P1–P3. Physical reading: the exterior register `u = μ/r̄` grows inward and stops only where continuing would leave no static configuration. This is a stated premise, not a derived one — see §5.

**Not a premise:** the CP Exclusion Rule, one-CP-per-GP, any occupancy statement. The verify script asserts in code that its premise-bearing region contains none (Check 6).

## §2 Buchdahl's bound — derived, not cited

For the uniform-density Schwarzschild interior solution (G = c = 1), with `s ≡ √(1 − 2M/R)`:

    p_c / ρ = (1 − s) / (3s − 1),        e^{ν(0)} = (3/2) s − 1/2.

The central pressure diverges and the central lapse vanishes at `s = 1/3`, i.e. **`R = 9M/4 = (9/8) r_S`**. Buchdahl (1959) proved `R ≥ 9M/4` for *any* static spherically symmetric Einstein-consistent body with non-increasing density; the uniform case saturates it. (Verify Check 0.)

## §3 The bound in the saturation variable

Areal radius of the surface, with the surface at `r̄_s = μ/u_max` (P1 matched to P2):

    R(u) = r̄ (1 + μ/2r̄)² |_{r̄ = μ/u} = (μ/u)(1 + u/2)².

Buchdahl `R(u) ≥ 9μ/4` is, after clearing denominators,

    **u² − 5u + 4 ≥ 0   ⟺   u ≤ 1  or  u ≥ 4.**

`R(u)` has its minimum at `u = 2`, where `R = 2μ = r_S` — the horizon. The exterior (physical) branch is `u < 2`; the root `u = 4` sits at `r̄ = μ/4 < μ/2`, inside the horizon's isotropic image, censored. Hence on the exterior branch:

    **u_max ≤ 1.**

(Verify Checks 1–3.)

## §4 The floor

By P4, `u_max = 1`, so

    **PSR_floor = l_P / (1 + 1) = l_P/2.**

The surface then sits at areal `9μ/4`, lapse `1/3`, redshift `z = 2`, `c_*(surface) = c/2` — the 3297 numbers, now as **consequences** of the floor rather than of a rule. (Verify Checks 4–5.)

## §5 What this does and does not establish

**Establishes.** Given a register that saturates and an exterior that is exactly Schwarzschild, the saturation value is forced to `u_max = 1` by the requirement that a static body exist at all. The `1/2` is not free and not postulated; it is the smaller root of a quadratic whose larger root is behind the horizon.

**Does not establish.** (i) *Why* the register saturates — what in the substrate caps SSV_abs. That is the substrate-internal derivation, and it is the open half of FLOOR-1. (ii) The extremality step P4 is asserted; a derivation would show the register cannot stop *below* the admissible maximum. (iii) P3 is conditional on RCORE-4.

**Not a triangulation.** The founder asked for one (R-MIRROR-KEPT: "if it solves all the problems consistently, that's the triangulation"). This record supplies *one* derivation. A second, from inside the substrate without invoking FE-1 in the interior, would complete it — and would make Buchdahl's bound a *prediction* of CPP rather than an input. Until then: DERIVED-CONDITIONAL, not DERIVED.

## §6 Route B — closed, negative

Proposed 31 Aug: a census-reach fixed point `PSR = l_P/(1 + k·N_sources(PSR))`, on the idea that a smaller PSR reaches fewer sources. **It does not close.** Under AP-4 the DI-bit relay recursion carries messengers beyond one PSR; a smaller PSR slows the census (`c_* = PSR/(√3 t_P)`, T-1) but does not truncate the source set. The interior register of a uniform body under the 1/r census kernel is the ordinary interior potential, `(3R² − r²)/(2R³)`, with no PSR dependence and its maximum at the *centre* (3/2 of the surface value) — the opposite of a reach-limited profile. Asserted in code (Check 7) so the negative result cannot rot into a prose claim of "under investigation."

The worker set this route up wrongly on 31 Aug and says so here.

## §7 Owed

- **CONV-038** — panel audit of P1–P4, the conditionality, the corrigenda scope, and whether the 3297 mirror survives a one-Moment-delay compliant wall (R-EXCL-RETIRED's boundary condition).
- **Corrigenda** (after CONV-038; anti-erasure by dated note): GR-1c Thm 2 proof; GR-1b definitions + §"Effective Horizon and the GP Exclusion Rule"; W-C ch. 2; RCORE_derivation.md §3.
- **The substrate-internal derivation** — the second leg.
- **OPEN-GR-ROT-1** and the wall condition on the founder's picture (ruling file §4).
