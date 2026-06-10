# Energetic EoS from the residual color potential — no self-bound saturation; the weak residue keeps the medium diffuse *and* collisionless

**Patch:** 0832 (Session 156, 10 June 2026) · **Type:** first-pass computation / scaffold; **includes a correction to 0830's framing and to my own earlier "core falls out" suggestion.** · **Lane:** DM-2 / `dark_matter/`.
**Builds on:** 0830 (geometric saturation + σ/m window), 0831 (no near-threshold resonance). **Verify:** `code/0832_qdp_energetic_eos.py`.

---

## What this layer was supposed to do, and what it actually shows

The plan (flagged by 0830/0831): turn the same residual color potential into the binding energy per qDP and the `E/N(ρ)` minimum, replacing 0830's geometric `ρ_sat` with a derived one, and let the core density fall out. **Doing it honestly changes that picture in two ways**, both recorded here.

`E/N(ρ) = T(ρ) + (z/2)·V_res(d(ρ))`, nearest-neighbor cell sum, `d = ρ^{-1/3}`, `z = 12`, residual potential from 0831 (hard core `r_c = 1.0 fm` + attractive color Yukawa, range `λ = 1.3 fm`, depth `V₀ = f·E_qDP`). Because the many-body kinetic depends on the (unsettled) qDP phase/statistics, two brackets straddle the truth: a **cell model** (particle localized in the free spacing `L = d − r_c`; solid-like, upper bound on kinetic) and a **free Fermi gas** (`T = (3/5)E_F`; delocalized, lower bound, most bindable).

**min E/N over ρ, vs the residual depth fraction f** (m_qDP = 0.30 GeV):

| f | V₀ [MeV] | min E/N cell | min E/N fermi | |
|---|---|---|---|---|
| 0.05 | 13 | +87 | +26 | diffuse (both > 0) |
| 0.10 | 26 | +86 | +24 | diffuse (both > 0) |
| 0.20 | 53 | +82 | +21 | diffuse (both > 0) |
| 0.35 | 92 | +77 | +14 | diffuse (both > 0) |
| 0.50 | 132 | +73 | −104 | bracket-split |
| 1.00 | 264 | +56 | −578 | bracket-split |

Self-binding threshold (Fermi bracket): **f_crit ≈ 0.38** (V₀ ≈ 100 MeV).

## Result 1 — there is no self-bound saturation density; the weak residue keeps the medium diffuse

At a **realistic** residual depth (f ~ 0.05–0.2 — the van-der-Waals residue, by the nuclear-force analogy), the medium does **not** self-bind in *either* bracket: `E/N > 0` with no negative minimum. It is a quantum-pressure-stiff, gravitationally-bound, **diffuse gas** — no nuclear-density "dark nuggets," no collapse toward the confinement density.

Self-binding (in the most-bindable Fermi bracket) needs f ≳ 0.38, i.e. a residual approaching the qDP's *own* color binding. **The same residual-force hierarchy that excludes the scattering resonance (0831: residual < E_qDP) keeps the medium below the self-binding threshold.** The residue being weak is what makes the dark matter *both* collisionless (0831) *and* diffuse (here) — one physical fact, two phenomenological requirements.

So 0830's geometric `ρ_sat` is **not** a self-bound equilibrium. It is a hard-core close-packing *ceiling* reached only under extreme external (gravitational) compression. The energetic EoS replaces "the medium saturates at ρ_sat" with: **no equilibrium density; quantum pressure plus the hard core set a compression ceiling that stays below confinement.** Glueball-avoidance is thereby *reinforced* — quantum pressure resists compression toward ρ_conf (≈100s of MeV per particle would be required), on top of 0830's geometric hard core.

## Result 2 — correction: the halo core-vs-cusp is the SIDM core, not this

The saturation/compression scale here is nuclear (ρ ~ 0.1–1 fm⁻³ ~ 10¹³–10¹⁴ g/cm³). An observed DM halo core is ~10⁻²⁴ g/cm³ — **~40 orders of magnitude less dense.** So the saturation/EoS density is *not* the observed core. **My earlier suggestion that "the core density falls out as a number, the core-vs-cusp signature" conflated two different cores.** The halo core-vs-cusp signature is the **SIDM core** set by the self-interaction σ/m (0830/0831), at halo density — a separate mechanism. The energetic EoS does not produce the halo core; correcting that is part of this result.

## Scope and caveats

First-pass / scaffold. **No closure, no THEO/ID, no verdict.** The realistic-f conclusion (diffuse, no self-binding) is robust because *both* kinetic brackets agree there. The brackets straddle by a large factor for f ≳ 0.5; settling that edge (and whether a marginally-bound nugget phase exists near f ~ 1) needs the proper hard-core quantum many-body treatment (Jastrow correlations, and the qDP statistics — itself an open question in the arc). Identical-qDP statistics, higher partial waves, and the exact `r_c`/`λ`/coordination are refinements. Hybrid throughout (gravity drives the diffuse halo; the residual force governs micro-scale collisionality, not a self-bound core). Conditional on the qDP/hTetra-DM conjecture and the Mechanism-A measure.
