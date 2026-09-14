# Founder question — can multi-hop DI-bit path disparity produce chirality? (14 September 2026)

**Filed verbatim per CONV-009.** Answered at Patch 4011 (EW lane).

## The founder's question, verbatim

> I don't know the details about a 120 point (GP) 4 dimensional space surrounding a center point (GP).
> The question is whether going from one point to another, even though it is the same 120 points around
> each center point, whether going from one GP to the next will there be some type of assymmetry. The
> process and geometry that makes me think that there will some asymmetry somewhere is that each GP puts
> out DI Bits to a PSR shell to GPs that are 10% of the radius of the PSR. Those are then reradiated to
> another PSR shell, etc. forever, and for all GPs. The 120 GPs surrounding each GP may all be identically
> symmetric, but the DI Bits and the 10% shells may have asymmetries between GPs because of the necessity
> of traveling only along edges between GPs to transmit DI-bits. The asymmetry would arise because of the
> discreet nature of the possible paths, and that path length being path dependent, when there is
> disparities in hop/edge length depending on the second and third re-radiation. So the question is
> whether the two or more hop disparity can produce the asymmetry in path length that is needed to produce
> the chiral effect.

## Answer (Patch 4011)

**Two claims, and they separate.**

**(A) The path-length disparity is REAL, and it begins exactly where he said.** Hop count and physical
distance are different functions on the 600-cell, and they come apart from the second re-radiation on:

| hops | vertices reached | Euclidean distances present |
|---|---|---|
| 1 | 12 | 0.61803 |
| **2** | 32 | **1.00000 and 1.17557** |
| **3** | 42 | **1.41421 and 1.61803** |
| **4** | 32 | **1.73205 and 1.90211** |
| 5 | 1 | 2.00000 |

One hop count spans two physical distances from hop 2 onward. *Path length is path dependent* is correct.

**(B) But the disparity cannot produce a chiral effect.** Three separate reasons, and none of them is a
numerical accident:

1. **At two hops it is impossible in principle.** A parity-odd invariant in 4D needs four independent
   vectors. Two steps plus n̂ gives three. No 4D pseudoscalar exists at two hops at all, so the earliest
   candidate is three hops, not two.
2. **At three, four and five hops it cancels exactly.** Summing `w · sign det[u₁, u₂, u₃, n̂]` over all
   non-backtracking paths — with `w` the Mechanism-A tilt weight — gives zero to machine precision at
   δ = 0, 0.10 and 0.35, over 2.1 million paths. Per vertex at three hops: **480 left-handed, 480
   right-handed, 492 degenerate.** Balanced path by path, not merely in total.
3. **The reason is a symmetry, so it holds at every hop count.** `R = diag(1,1,1,−1)` maps the 600-cell to
   itself, has det = −1, **and fixes n̂**. Verified: every mirrored path carries **equal weight and
   opposite sign**. H₄ (order 14400) properly contains its rotation subgroup (7200) at index 2 — the
   polytope is **achiral**, so every path has an exact mirror partner inside the same structure, and the
   Mechanism-A tilt cannot break the pairing because `û·n̂` is preserved by a reflection that fixes n̂.

**Standing:** an achiral substrate cannot manufacture handedness by propagation geometry, however many
re-radiations are chained. This **confirms FI-C-9 = V3** (chirality primitive, not emergent) by a route
independent of the susceptibility line — and it is the same fact as Patch 0973's *sign(δ) is P-even,
T-odd*, reached from path geometry rather than cycle affinity.

**~~Not resolved~~ — RETRACTED AT PATCH 4012.** 4011 wrote that the *"10% of the radius of the PSR"* shell *appears nowhere in the corpus*. **It is false.** The quantity is the **PSR shell radial thickness**, **σ_r/⟨r⟩ ≈ 0.096 — finding F-E2-3** — recomputed at **D-SUBPSR-FIELD pass 3** under **R-OUTWARD-FANOUT** (Patch 3135, 14 Aug 2026) as **σ_r/⟨r⟩ = 0.093–0.076 over N = 6–22 hops**, with **D-ARC-GAMMA** minted as the retention geometry on it, and carried in several `founders_voice/` files. It is **derived, not an estimate.** My 4011 grep covered four paths and searched one string, `10% of`, and missed every one of those names. **Third scoped-grep-generalised error in nine patches** (4003, 4007, 4011); mechanized at 4012 as `code/absence_gate.py`.

**And the question above was already registered, in the founder's own words, a month earlier.** `founder_clarification_outward_fanout_2026-08-14.md`: *"I think this will produce a PSR shell thickness (10% before), as you calculated earlier, **because the total DI-bit hop count varies when it's specified as the path from GP_origin to GP_PSR**."* So 4011's claim (A) was not a finding — the measurement stands, the framing overstated it.

**Answer (B) is unaffected and is now stronger.** 4011 summed over all non-backtracking paths; 4012 re-ran it on the **R-OUTWARD-FANOUT** path set the corpus actually registers (anti-radial excluded) — chirality sum still zero to machine precision at K = 3, 4, 5 and δ = 0, 0.35, and the mirror map was verified to preserve the outward-radial test `x·d` itself. The cancellation survives contact with the real propagation rule.
