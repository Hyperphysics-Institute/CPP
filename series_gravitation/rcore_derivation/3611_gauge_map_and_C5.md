# The gauge map, derived and solved: the register's content of the even mode at the wall is gauge-dependent by O(1). And A3′'s clause C5 maps the count to `h̄₀₀` (the lapse), not to the spatial trace. Together they supersede the 3378–3391 wall laws as lattice-frame physics: the even wall must be re-derived under C5. V1.9's a = 0 lines stand only as RW-gauge register-model numbers

**Patch 3611, Session 161, 4 Sep 2026.** Verify `code/3611_rw_to_harmonic_gauge_map_verify.py` (5/5). Reasoning `reasoning/3611.md`. Two findings, both from doing the first step of 3610's order of work instead of asserting it.

## §1 The gauge map — derived and solved

- **Derived** (the 3398 method, nothing recalled): the background-covariant divergence `D_μ = ∇^ν h̄_μν` of the RW-gauge Zerilli mode (per `Y`, `Y′`; `D_θ ∝ H₀ − H₂ = 0`, a derived consistency), and the vector wave operator `(□ξ)_μ` on Schwarzschild for `ξ_μ = (aY, bY, cY_{,θ}, 0)e^{−iωt}` — three coupled radial ODEs, θ-independent after the harmonic identity (checked at two angles).
- **Solved** at the free-surface pole (`Mω = 0.37487 − 0.0019i`, `r_w = 8M/3`, `Z⁺` from the wall law outward) as the two-point problem `□ξ_μ = −D_μ`, **ξ = 0 at the wall** (GPs do not move; absolute time universal there — the lattice-frame choice of the residual) and outgoing at 60 M. Converged.

| at the wall (per Y) | RW gauge | harmonic (lattice-frame residual) |
|---|---|---|
| `H₂` (radial) | −0.650 − 0.052i | + gauge shift `2f b′` = −5.53 − 3.27i |
| `K` (tangential) | 0.976 + 0.079i | unchanged at ξ = 0 |
| r–A component | 0 (RW) | `c′` = −5.65 − 3.46i |
| **trace part** | 1.30 + 0.10i | **−4.23 − 3.16i** |
| radial–tangential anisotropy | −1.63 − 0.13i | −7.16 − 3.40i |

**The register content of one and the same mode at the wall changes by a factor of several between RW gauge and the lattice-frame harmonic gauge.** The trace part — the thing the 3378/3391 level set pinned — flips sign and triples. An r–A component absent in RW gauge appears at O(the RW components). The wall laws of 3378 (trace-Dirichlet), 3391 (free surface), and the poles of 3383/3390/3391 were all written in RW gauge on the tacit assumption that RW gauge is the lattice frame. **It is not.** (CONV-039 T-2 and CONV-040 T-2 both pointed here.)

## §2 What clause C5 says the count is — and it is not the spatial trace

A3′ C5 (12 June): *"h̄₀₀ ← Φ, h̄₀ᵢ ← Vᵢ, h̄ᵢⱼ ← Qᵢⱼ + ⅓δᵢⱼτ, with the spatial trace τ the conservation completion ∇τ = 3(∂ₜh̄₀ᵢ − ∂ⱼQⱼᵢ) … statics: τ = 0 by the virial theorem, reducing exactly to the c07 map."* So in the dynamical sector **the count Φ is the `h̄₀₀` component — the lapse/Newtonian-potential channel — and the spatial trace is not register content at all**; it is a *completion* determined by conservation. The identification "register ↔ spatial conformal factor" used from 3378 onward came from GR-1c's *static* isotropic dictionary (`ψ = 1 + u/2`), which C5 says is the `τ = 0` special case. Extending it to a wave at the wall was the second tacit assumption.

Under C5 the surface conditions are therefore: **the level set on Φ ↔ `h̄₀₀` (one dictionary, the lapse — the two-dictionary elimination of 3391 collapses to one condition on the harmonic-pattern `h̄₀₀` and its surface displacement)**; `Qᵢⱼ` continuity into the core; `Vᵢ` continuity for the odd sector; and the spatial trace supplied by the completion. All in the harmonic-pattern frame.

## §3 Standing — stated without softening

- **3378, 3391 wall laws and the 3383/3390/3391 poles: superseded as lattice-frame physics.** They are correct solutions of *a* boundary-value problem (RW-gauge register pinned), and V1.9 already calls them "poles of the kinematic wall model"; the record now adds the caveat those words did not carry: **the model is the RW-gauge register model, and the lattice frame is the harmonic-pattern one.** The a = 0 line set (195 / 292 / 208) and the indicative Kerr numbers are not lattice-frame predictions.
- **The gauge-invariant results stand:** the parity theorem (3378), the shift reconstruction (3398), the pole machinery (3356/3383), the surface at 8M/3 (3389–3390; a static statement), the odd sector's transmit picture (3382/3384, its numbers likewise RW-gauge).
- **CONV-039's and CONV-040's caveats on the dictionary (T-2) are now findings.** This is the correction their reviewers asked for and the worker did not make until the gauge map was computed.
- **The even wall under C5 is the next computation** — with its ingredients now in hand: the harmonic-pattern exterior mode at the wall (this patch's BVP), the level set on `h̄₀₀`, `Qᵢⱼ` continuity, the completion for τ, the interior tensor wave, the C5 energy ledger. The residual-freedom choice (ξ = 0 at the wall) is a stated assumption to be revisited: the lattice frame fixes it physically, and whether "GPs at rest" means ξᵢ = 0 or the retarded harmonic solution is the founder's picture (F-16).

## §4 GR-2
V1.9 owes a caveat sentence at its next touch: *"the kinematic wall model is expressed in Regge–Wheeler gauge; the lattice frame is the harmonic-pattern assembly of A3′ C5, in which the same mode's register content at the wall differs at O(1); a lattice-frame line set is pending (Patch 3611)."* Not enacted here; recorded as owed (ledger A1). No number in the paper changes.

## §5 F-16 to the founder
The gauge vector is the map between coordinate labels and grid points. At the surface, the residual freedom of the harmonic frame is a homogeneous harmonic pattern. **Does "the GPs do not move" fix that residual — the coordinate displacement ξ vanishes exactly at the wall, as this patch assumed — or is the lattice frame at the wall whatever the relay of the incident wave produces there (the retarded harmonic solution, with no additional pattern from the wall)?** The first is a boundary condition on ξ; the second is a statement that the wall adds no pure-pattern content. They give different register values at the wall (this is the residual-gauge sensitivity the panels flagged), and only one of them is CPP.
