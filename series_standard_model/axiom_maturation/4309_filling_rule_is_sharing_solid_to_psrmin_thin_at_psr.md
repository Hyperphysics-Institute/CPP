# The Filling Rule Is Equal Sharing, Not Farthest Advance: Shells Are Solid Out to PSR_min, and the Landing Band at the PSR Is a Scale-Free 1.9%

**Patch:** 4309. **Lane:** EW → foundations. **Session:** 240.
**Founder:** `founders_voice/4309_clarification_shells_fill_solid_no_beams.md`: the DI-bits fill shell 1 completely, then shell
2 solid, and so on; no twelve beams.
**Verify:** `series_standard_model/code/4309_random_outward_walk.py`.

## 1. Which rule fills shells

"Fill every GP of each successive shell" is what R-OUTWARD-FANOUT does (founder, 14 Aug; 3135): each GP passes its DI-bits
to *all* its outward neighbours. Its whole-bit form is: each DI-bit steps to one outward neighbour chosen at random with
equal probability. In the average every outward GP is reached and no direction is favoured. "Take the neighbour that
advances farthest" (4308) does the opposite: it concentrates every bit onto twelve rays. So the founder's intended
behaviour selects the sharing rule, and 4308's beams were the consequence of the other rule, not of his picture.

## 2. Solid shells, exactly as far as the crowding radius

A volley of N whole DI-bits can fill shell after shell solid only while 4πr² ≤ N, i.e. out to r = √(N/4π) GPs. With α's
N that is 8.5 × 10¹³ GPs, about 10⁻¹⁶ PSR, which is 4304's PSR_min (4308 §3). Beyond it there are more GPs per shell
than DI-bits: the shells are solid **in the average**, one DI-bit per (4πr²/N) GPs, and any given GP receives one only
occasionally, over many Moments. That is the founder's "diffuse, re-radiated" delivery, now quantified.

## 3. The landing band at the PSR (rows)

```
 steps L   <r>/L   rms/<r>
      10  0.6448    0.1018
     100  0.5497    0.0412
    1000  0.5384    0.0221
    3000  0.5375    0.0201
   10000  0.5372    0.0192
   30000  0.5372    0.0189
direction-dependent mean progress per step: spans 0.4588..0.5393, mean 0.4999, rms/mean = 0.0396
```

Under the sharing rule on the icosahedral neighbour set:
- The landing radius is a fixed **0.537** of the summed edge length. (So for a DI-bit to land at one PSR, the edge count
  GP_origin imprints must be about 1.86 PSR of edges; or "the PSR" is defined by the landing, not the path.)
- The relative width of the landing shell settles at **1.9% rms**, scale-free: the same at 10⁴ and 3 × 10⁴ steps, so
  the same at 10³⁰. It comes from the lattice's direction-dependent mean outward progress (4.0% across directions,
  partly averaged by each walker's wander). **This is what decides where in the band a DI-bit lands: the direction it is
  travelling.**
- The band is neither 10% (E-2, passes 3–4: a toy-scale artefact, 4307–4308) nor zero (the greedy rule): about 2%.

## 4. Consequences

- **α:** unchanged. α = N s/(4π PSR) = PSR_min²/(s PSR). The per-layer reading would need 9.2% and the band is 2%, so it
  stays closed. What fixes N remains the open item.
- **The Moment-level picture is now positional and consistent:** a volley fills shells solid out to PSR_min, thins as
  1/r² beyond, and lands in a shell 2% thick at 0.537 of its summed path, isotropically. The founder's 4306 ruling
  (positioning, not calculation) is honoured: nothing here depends on a hop count, only on the lattice's geometry.
- **D-6:** D-ARC-GAMMA (retention geometry) was minted on a 10% band; at 2% it should be re-checked by the sea lane
  (flag raised at 4308, sharpened here).

## 5. Founder question (a physical picture)

**Does a DI-bit's summed edge length equal one PSR, so that it lands at about 0.54 PSR, or does it land at one PSR, so
that GP_origin imprints about 1.86 PSR of edges?** Either is consistent; they differ in what "the PSR" names.

## 6. PD-008

- **No convenient branch here.** The 2% band helps nothing in the α programme; it is reported because it is what the
  rule gives.
- **What is solid.** The sharing rule fills shells; the crowding radius; the scale-free 1.9% band and the 0.537 landing
  ratio on the icosahedral neighbour set (the FCC values will differ slightly and are not computed).

**Note (Patch 4328):** this simulation did not apply the founder's family-exclusion step rule (4308, clarified 4328: each step goes only to a GP empty of the same GP_origin family). Under that rule a family's occupancy is capped at one per GP and the band thickens with N; the 1.9% width should be re-run with it. See `series_standard_model/axiom_maturation/4328_family_exclusion_caps_occupancy_lpi_needs_saturation.md`.
