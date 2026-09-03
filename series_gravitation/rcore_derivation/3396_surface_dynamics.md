# OPEN-GR-SURFACE-DYNAMICS-1 — The surface needs no equation of motion: it is the level set of the register, and an EOM would both be a new rule and over-determine. What IS missing is the junction: the even mode's shift content is order unity at the wall and, under the founder's rule, transmits — the 3391 wall is the closed-vector-channel limit

**Patch 3396, Session 161, 3 Sep 2026.** Verify `code/3396_surface_dynamics_counting_verify.py` (5/5). Reasoning `reasoning/3396.md`. Resolves SURFACE-DYNAMICS-1 as asked; mints **OPEN-GR-JUNCTION-1** as what the panel's caveat was actually pointing at.

## §1 No surface equation of motion — by construction and by counting

The saturation surface is **where the register reaches its cap**: `r_s = {v_tot = v_sat}`. Its displacement under a perturbation is `ξ = −δv/v′` — a *definition*, not a dynamical variable. The surface is not a membrane with inertia or tension; it is a contour of a field the theory already evolves (the register, slaved to the demand each Moment — 3376). Adding a surface EOM would be a new rule (C-NO-SPECIAL-RULE) — and, as Grok argued at CONV-040, it would **over-determine**: the exterior even sector is a second-order problem, one outgoing condition at infinity and one at the wall complete it, and the 3391 kinematic relation is that one condition. A third condition is not missing; it is excluded. **SURFACE-DYNAMICS-1: closed — the kinematic law is complete for the register channel.**

## §2 What the caveat was really about: the junction

The exterior even-parity mode is one degree of freedom (`Z⁺`), but at the wall it presents three components: `K` and `H₂` (which the register's two dictionaries see) and **`H₁`, the shift** (the even *vector* harmonic). The 3391 law used the first two and said nothing about the third. Dimensionally `H₁ ~ ωr·Z` (RW-gauge reconstruction `H₁ = −iω[c(r)Z + rZ′]`); at the line frequency `Mω ≈ 0.37` and `r_w = 2.67M`, `ωr ≈ 1`: **the even mode's vector content at the wall is order unity.**

By the founder's rule R-SHEAR-MUST-BE-REGISTERED (3382), vector content arriving as DI-bits is registered in `SSV_net`, which is uncapped; the surface does not refuse it; it transmits into the core and returns from the centre — exactly as the odd sector does (3384). So the even sector at the surface has **two channels**: the register channel (level set → reflection, 3391) and the vector channel (SSV_net → transmission). The 3391 wall is the **closed-vector-channel limit (T = 0)**.

## §3 Why this is a junction problem and not a boundary-condition problem

Exterior: one amplitude (R). Interior: one vector-wave amplitude (T), regular at the centre. Two surface conditions — the level set (register) and `SSV_net` continuity (vector) — for two unknowns: **well-posed, not over-determined.** But: the level-set condition alone already fixes R with |R| = 1 (3391), while the vector condition fixes T ≠ 0 — energy is then created unless the interior wave **back-reacts on the level set** (the returning interior vector wave contributes to the surface register's *demand*, moving ξ). That back-reaction is the interior-side dictionary — how an `SSV_net` wave inside the core feeds the register at the surface — which is **RCORE-4 physics not in the corpus**. This is precisely "junction / surface stress-energy" (GPT, CONV-040 defect 4), correctly named and now located: **OPEN-GR-JUNCTION-1.**

## §4 What it would do to the lines

If the vector channel is open with the interior back-reacting consistently: the even sector's |R| < 1 at the surface; the transmitted part returns after the core round trip (`J = 6.75`, spacing `π/(Jμ)`); the sharp 195/292 lines become a two-timescale structure like the odd sector's (3384), broader and shifted. The 1% agreement with V1.6 could evaporate — or could be what survives after the vector part transmits. **Unknown until the junction is built.** The V1.9 language ("poles of the kinematic wall model") already carries this: it is the model with the vector channel closed.

## §5 What would build it
1. **Source-check the `H₁` reconstruction** (a recalled Einstein-equation check did not close in this patch — Q7 item; no formula is claimed).
2. **Compute the vector fraction** `|H₁|²/(|K|² + |H₂|²)` at the wall for the free-surface mode.
3. **The interior-side dictionary** — founder picture (F-5 below), then the flat-core vector wave (3384 machinery) coupled to the level set through the back-reaction.
4. Rerun the a = 0 even poles with the open channel.

## §6 F-5 to the founder
At the saturated surface, the register's demand is a census of arriving DI-bits. **Do DI-bits arriving from *inside* the core — the returning vector wave — count in the surface register's demand the same way exterior ones do?** If yes, the interior wave moves the surface (the junction closes energetically and the even sector is a transmission problem). If the interior is opaque to the surface register (pinned interior re-emits no register deviation, 3376), then the vector wave passes through without touching the level set — and the even sector's register channel and vector channel are independent, which would be the T ≠ 0 with |R| = 1 case: energy is then supplied by the surface's displacement being decoupled from what it transmits, and something is wrong with the picture.
