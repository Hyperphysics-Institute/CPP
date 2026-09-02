# OPEN-GR-ROT-1 rung 1 — The R-core is a SLAB, not a wall: three boundary laws, one incident wavelet

**Patch 3374, Session 161, 2 Sep 2026.** Verify `code/3374_rcore_slab_rung1_verify.py` (16/16). Reasoning `reasoning/3374.md`. Founder inputs: R-EXCL-RETIRED, R-FLOOR-REGISTER, R-COOCCUPATION-FORCED, R-FLOOR-FINITE.

**Standing:** rung 1, one-dimensional, flat-space (no RW potential, no lapse), **shape established, numbers bracketed.** Not a recomputation of the line set.

## §1 The first result is that there is no wall

Under the ratified dictionary `c_* = c/(1+u)` with `u` continuous across the surface (exterior `μ/r̄ → 1` at `r̄ = μ`; interior flat at the cap), **the census speed does not jump at the surface.** A linear medium with no impedance discontinuity reflects nothing at its interface. The 3297 mirror — |R| = 1 at phase π *at the surface* — was entirely the Dirichlet assumption, not a property of the medium. (For contrast, a hypothetical speed jump to c/2 from c would give a prompt `r₁₂ = −1/3`; CPP has none.)

## §2 Three boundary laws, same incident zero-mean wavelet (compression lobe + rarefaction lobe)

| Law | Physics | Prompt (at surface) | Delayed (after core round trip) | Phase |
|---|---|---|---|---|
| **(C) old mirror** | Dirichlet at the surface (3297 "clamped register") | **100%** | 0 | π |
| **(A) linear slab** — register *below* cap (attainment fails; FLOOR-1(a) open) | two-sided medium; wave enters, crosses, reflects at the centre (regularity), returns | **0** | **100%** | round-trip delay; sign from the centre |
| **(B) one-sided slab** — register *at* cap (attainment holds) | compression (`δu > 0`) cannot be stored inside → refused; rarefaction (`δu < 0`) propagates | **33%** (this wavelet) | **67%** | prompt part at π; delayed part carries the round trip; **harmonics generated** (rectification) |

All three are lossless in wave energy (FD energy audit constant to <1%; probe flux sums to 1.00 ± 0.01). Law (B) additionally leaves a **static offset** behind — the core admits net rarefaction — a zero-energy *memory* term. Whether that survives in the spherical GR problem (as a metric-memory effect) is not claimed here.

**The panel's Q4 ruling is now concrete.** |R| = 1 survived because the core is lossless, not because the surface is a mirror. The phase π did not survive because under (A) there is no prompt reflection at all, and under (B) only the compression half of the wave sees anything like a clamp.

## §3 Which law is CPP's depends on attainment — FLOOR-1(a) is now physically load-bearing, not just a label

If the register inside the core sits *at* the cap (`u = u_max` exactly, attained), the core is the rectifying medium (B). If it sits *below* the cap with headroom, the core is the linear medium (A). The panel stripped attainment from 3367 as "asserted"; this rung shows the assertion decides the echo morphology. That is the argument for spending a patch on FLOOR-1(a) next rather than never.

## §4 The number — bracketed, not claimed

The **shape** (amplitude split, delay structure, harmonics) is independent of how `c_*` maps to an observer's clock. The **round-trip time** is not, and that map in the strong field is the unminted NOTE-GR-CSTAR-STRONGFIELD (CONV-027, DeepSeek). Three candidates, 62 M_⊙:

| Map | Round trip | ms |
|---|---|---|
| coordinate hop `c/(1+u)` over isotropic radius μ | 4 μ/c | 1.22 |
| proper radius `ψ²μ = 2.25μ` at `c/2` (the 3297 usage) | 9 μ/c | 2.75 |
| GR isotropic coordinate light speed `N/ψ²`, radius μ | 13.5 μ/c | 4.12 |

Every candidate is **comparable to the 2.15 ms cavity delay**. Under (A) or (B) the echo train therefore has *two* timescales — the cavity and the core — not one. This is a change to what the detector should look for, and it is why GR-2 cannot go to V2.0 until the map is minted and the spherical (ℓ = 2, with the RW potential and lapse) version of this rung is computed.

## §5 What rung 2 needs

1. **The c_* → observer-time map at strong field** (NOTE-GR-CSTAR-STRONGFIELD): a T-1-charter question; picks one row of §4.
2. **Attainment** (FLOOR-1(a)): picks (A) vs (B).
3. **Spherical ℓ = 2 with the RW potential and the lapse**, interior regular at the origin, matched at `r̄ = μ`: the actual `R(ω)` the Teukolsky ladder needs, replacing `X = 0`.
4. **Rotation** (the original OPEN-GR-ROT-1): the slab co-rotating at Ω_w — after 1–3.
