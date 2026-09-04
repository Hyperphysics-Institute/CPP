# Will this work? As stated, no — it is the vector sum again, and a vector sum is blind to "more along one axis than across it." With one addition it can: keep the second moment of the same DI-bit addresses. Then statics is automatically satisfied (it is a coordinate choice), and the coefficient is fixed by the wave

**Patch 3608, Session 161, 4 Sep 2026.** Verify `code/3608_rank2_register_from_addresses_verify.py` (5/5). Founder proposal P-DIRECTION-VIA-ADDRESSES. Reasoning `reasoning/3608.md`.

## §1 The proposal as stated — rank 1

The story: every DI-bit carries its origin's address; `SSV_net` is computed from them; its direction and magnitude "embed θ and φ implicitly"; `SSV_net` is compared to `SSV_abs` along its own direction. Every step is ratified AP-4 (the payload is {origin address, E, S}; the founder's "EE_q and EE_e" was resolved on 19 Aug as shorthand for that payload — no AP-5). But the direction enters only through **the vector sum**, and a vector sum has a blind spot exactly where the gravitational wave lives:

- A census arriving **equally from +x and −x** has net vector **zero** — the same as an isotropic census. `SSV_net` cannot tell "squeezed along x" from "uniform." (Computed: |net| = 0 for the ±x census; ~0.01 for a random isotropic one.)
- A gravitational wave's pattern at a GP is *exactly* that: the census arriving more along one axis than across it, with no net direction. The `+` polarization is a ±x/±y asymmetry with zero vector sum.

So the story, as told, is rank 1 and cannot carry a GW — the 3606 theorem again, from the register's side. "Compare `SSV_net` to `SSV_abs` in its direction" still yields one scalar and one vector.

## §2 The one addition — the second moment of the same addresses

Nothing new has to arrive at the GP. The DI-bits' addresses are already there. The register keeps their zeroth moment (`SSV_abs = Σ|E|`) and their first (`SSV_net = Σ E`). Keep also their **second**:

    Q_ij = Σ |E| · (n_i n_j − δ_ij/3),   n = the arrival direction of each DI-bit.

For the ±x census, `Q = |E|·diag(+2/3, −1/3, −1/3)` — it sees the squeeze the vector sum cannot. It is symmetric, traceless (it carries no count — no breathing), rank 2: **the object a gravitational wave needs.** The perception radius then depends on direction — the founder's original anisotropic sphere, now *derived from the DI-bit addresses* rather than assumed:

    PSR_ij = l_P [ (1 − k·Δ|SSV|) δ_ij − k₂·Q_ij ] + …

— shrinking most along the axis the excess census came from. That is the restoration with the DI-bits included, which is what the founder asked for. Whether "the GP keeps Q_ij and the payload carries it" is the founder's to rule (it is an amendment to AP-4's *computed* registers, not to emission or to the payload's origin-address structure).

## §3 Statics: automatically satisfied — it is a coordinate choice

With a rank-2 register, a single static mass gives `PSR_r ≠ PSR_⊥`. Does that break GR-1? No. Computed: Schwarzschild's spatial geometry in **areal** coordinates needs `(kΔ, k₂Δ) = (u/3, u)`; in **isotropic** coordinates it needs `(u, 0)`. Both are Schwarzschild. **Statics fixes only the combination consistent with the geometry — a one-parameter family that is the choice of lattice coordinatization.** Every GR-1 result survives with any `k₂`; the rank-2 coefficient is fixed by **the wave** (its speed, its amplitude, its luminosity), not by any static test. This is 3607 §2 as an equation, and it is the reason the isotropic simplification passed everything: it chose `k₂ = 0`, i.e. isotropic coordinates, which is allowed for statics and wrong for radiation.

## §4 Then the charter, in order — each a computation once §2 is ruled
1. **Relay.** `Q_ij` relayed component-wise by the T-1 mechanism (the shell mean) obeys the same wave operator as the count → a symmetric traceless tensor wave at `c_*`; its transverse-traceless components propagate. Spin-2 waves exist. *(Immediate, once Q_ij is in the payload.)*
2. **Source.** Near a binary, the direct arrival-direction quadrupole from the pair is `~(d/r)²` × count — it falls as `1/r³`, exactly the Newtonian tide (3605). The `1/r` wave is what the relay makes *of* that tide — as in GR, where the near-zone tide sources the radiation. *(The T-1 template with a tensor source.)*
3. **Amplitude and luminosity.** The coefficient `k₂` and the relay normalisation give `h_ij^TT` at `1/r`; the target is `(2G/c⁴r)Q̈^TT` and the quadrupole-formula luminosity to 0.2% (Hulse–Taylor). *(This is where `k₂` is fixed — or where the theory fails.)*
4. **The scalar leftover.** With `Q_ij` traceless the tensor wave carries no count; the count's own radiation (3604) must still come in under 0.2% — a separate T-1 computation.
5. **Statics re-check.** With `k₂` fixed by (3), the lattice coordinatization is determined; GR-1 is then Schwarzschild in *that* coordinatization — a consistency check, not a risk.

## §5 So: will it work?
- **As stated: no.** The vector sum is blind to the pattern.
- **With the second moment kept: it can.** The addresses are already in the register; the second moment is one more sum; statics cannot object; the wave decides `k₂`; and the founder's original anisotropic PSR is recovered *from the DI-bits* rather than postulated beside them.
- **What decides it is (3):** whether the relay of `Q_ij` delivers GR's amplitude and luminosity with a `k₂` that also passes (4) and (5). That is a derivation with numbers attached, not a picture — and it is the one the lane exists to do next.

## §6 F-15 to the founder (a ruling, not a picture)
**May the GP register keep the second moment of its DI-bit addresses — `Q_ij` — and may the payload carry the origin's `Q_ij` as it carries its `E` and `S`?** This is an amendment to AP-4's *computed* registers (rank 0 and 1 → rank 0, 1 and 2), nothing else. If ruled, TENSOR-1 becomes a T-1-shaped derivation and the lane starts it.
