# The directional PSR was the founder's original conception — restoring it is a restoration, not a rewrite. And the spherical PSR with retarded superposition cannot reach rank 2: computed for the orbiting pair, the stretch/squeeze content dies as 1/r³ and the scalar radiates nothing face-on

**Patch 3607, Session 161, 3 Sep 2026.** Verify `code/3607_retarded_binary_scalar_hessian_verify.py` (5/5, numerical). Founder statement P-ORIGINAL-DIRECTIONAL-PSR. Reasoning `reasoning/3607.md`.

## §1 Provenance: the isotropic PSR was a simplification of the rewrite

The founder's original theory had azimuth/elevation dependence in the perception radius. The AI rewrite (Sonnet, then Opus) replaced it with a single-radius sphere — `PSR_eff = l_P/(1 + k·Δ|SSV|)`, one number per GP — and built GR-1 and the companions on it. The retained corpus carries only that law (the Grok-era GR-1f notes: "the nonlinear PSR reduction … applied uniformly to the diagonal terms while the directional vector component supplies the cross term" — isotropic plus a *vector* frame-dragging term; nothing rank-2). **The original directional formulation is not in the repository.** It must be restated by the founder (F-14, §5).

What this changes: 3606's "CPP-native candidate" `PSR_ij` is the founder's own idea, older than the corpus. Reincorporating it is not the special rule C-NO-SPECIAL-RULE forbids; it is undoing a simplification the AI made.

## §2 Why the simplification was harmless for everything until now

The founder is right that it is invisible in the GR-1-class tests, and there is a reason. For a **single static mass** the census arrives radially; a directional PSR would shrink more radially than tangentially — `PSR_r ≠ PSR_⊥`. But a static spherically symmetric spatial geometry can be written *either* with an isotropic metric (`ψ⁴δ_ij`, isotropic coordinates — what the isotropic PSR gives, GR-1c Thm 1) *or* with `g_rr ≠ g_θθ/r²` (Schwarzschild coordinates — what a radially-anisotropic PSR would give). Same geometry, two lattice coordinatizations. **Statics cannot distinguish an isotropic PSR from a radially anisotropic one**; every GR-1 result survives either way. The two pictures part company only when the anisotropy has *its own dynamics* — which is exactly the gravitational wave. So the founder's "GR/gravity works with the simplified spherical PSR" is correct for everything static and for the scalar-wave sector; it fails only at rank 2, which is where LIGO lives.

## §3 The second-order question, computed

The retarded scalar field of two point sources in circular orbit, `u(x,t) = Σ_s m_s/|x − x_s(t_ret)|` with per-source retardation at `c` — the full time-delayed superposition the founder describes — evaluated numerically at 10, 30 and 100 wavelengths edge-on, Hessian split into longitudinal (`n·H·n`) and transverse-traceless parts:

| r/λ | longitudinal | TT | TT/longitudinal | `(λ/2πr)²` |
|---|---|---|---|---|
| 10 | 3.8e-6 | 3.9e-10 | 1.0e-4 | 2.5e-4 |
| 30 | 2.2e-7 | 4.2e-12 | 1.9e-5 | 2.8e-5 |
| 100 | 1.4e-8 | 3.4e-14 | 2.4e-6 | 2.5e-6 |

- **The stretch/squeeze content falls as `1/r²` relative to the longitudinal** — at a detector (`r ~ 10¹⁷ λ`) it is `~10⁻³⁴` of the breathing part. Retardation, moving sources, changing distances and delays: all present in the computation, none of it changes the rank. **Complexity of the time dependence cannot manufacture a rank-2 field from a scalar one.**
- **The frequency is 2Ω** — the founder is right, and the computation shows it (dominant harmonic 2).
- **Nonlinearity is irrelevant** at `h ~ 10⁻²¹` (second order `~10⁻⁴²`), and a nonlinear scalar equation still produces scalar fields.
- **A second discriminator, found on the way:** the scalar quadrupole radiation pattern is `∝ sin²θ` — **zero along the orbital axis**, where GR's `+`/`×` are *maximal* (face-on binaries are LIGO's loudest). Edge-on/face-on radiative ratio in the computation: > 30.

So the answer to "is it possible that the spherical PSR would work by superposition at second order" is **no, provably and numerically** — not because superposition is linear, but because the field is scalar. The obstruction is rank, and the founder's original directional PSR is the rank-2 object that removes it.

## §4 What the directional PSR must do (TENSOR-1's charter, unchanged; the object now has provenance)
`PSR_ij(x,t)` relayed by the T-1 mechanism with the census's second moment kept: (i) speed `c`; (ii) statics: reduce to Schwarzschild's spatial geometry in *some* lattice coordinatization (§2 — the isotropic case is the special case already proven); (iii) near a binary: the Newtonian tide (3605); (iv) 1/r amplitude `(2G/c⁴r)Q̈^TT`; (v) luminosity the quadrupole formula to 0.2%; (vi) the scalar (rank-0) radiation from the same source under 0.2% of that (3604). Conditions (ii)–(vi) are all numbers the theory can be checked against once the relay is written.

## §5 F-14 to the founder — the restoration
**How did the original formulation make the PSR depend on direction?** Specifically: for a GP receiving, in one Moment, a census whose arrival directions are not uniform — more DI-bits along one axis than across it — what did the original theory say the perception radius does *in each direction*? (Shrinks along the axis of heaviest arrival? Shrinks in proportion to the census from that direction? Something with a different form?) The answer, in whatever form you wrote it a year ago, is the rank-2 register — and the relay derivation (T-1's template) can start from it.
