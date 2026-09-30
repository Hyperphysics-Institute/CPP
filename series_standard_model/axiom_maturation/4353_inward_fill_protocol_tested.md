# The Founder's Inward-Fill Landing Protocol, Tested: It Gives a Solid Band Pinned to the PSR If a Blocked Bit Spreads Sideways First

**Patch:** 4353. **Lane:** EW → foundations. **Session:** 241.
**Answers:** `founders_voice/4353_proposal_inward_fill_landing_protocol.md`.
**Verify:** `series_standard_model/code/4353_founder_inward_fill_protocol.py` (output `…protocol.out`, 43 s), on the
4330 lattices (FCC; GLASS = random dense packing), PSR radius P = 8 and 12 lattice units, N = 0.5×, 1.5× and 3× the
number of sites in the outermost unit shell; "well" = the same N with the PSR shrunk to 0.9 P.

## 1. What replaces what

4352 showed the outward random walk (4328/4329, rule as ruled) never packs the band: fill 0.72–0.80, and at high N the
band sits where crowding puts it, not at the PSR. The founder's protocol replaces the walk with a straight flight to
the PSR and an inward fill: one DI-bit per GP, the outer edge at the PSR. The exclusion rule (R-DIBIT-FAMILY-EXCLUSION)
is unchanged; what is new is where a blocked bit goes.

## 2. Three readings of "moves inward … the most radial position available in that set of GPs"

| Reading | What a blocked bit does | Fill of the band [r_in, P] | Holes |
|---|---|---|---|
| **F** (literal: its own ray) | slides down its own line toward the origin to the outermost free GP near that line | 0.14–0.54 at N ≤ 1.5× shell; 0.68–0.99 at 3× | many: radial **spokes** with empty wedges between |
| **F2** (neighbourhood of the blocked GP_PSR) | looks at the GPs around its GP_PSR, ring by ring; takes the most radial free one in the first ring with space | 0.31–0.50 at 0.5×; 0.72–0.80 at 1.5×; **0.93–1.00 at 3×** | few once N ≥ 3× shell |
| **S** (simplest, order-free) | the family occupies the free GPs nearest the PSR from inside, outermost first | **0.85–0.99 FCC, 1.000 GLASS**, every N | none beyond the partly filled innermost shell |

In every reading the outer edge is **at the PSR**, and in the well it **moves in with the PSR** (F2 and S: outer edge
7.14 / 7.20 at 0.9 × 8; 10.77 / 10.80 at 0.9 × 12). That is the property 4352 found missing: the band is now placed
by the PSR, not by crowding.

## 3. Answers to the two questions

- **Does it work?** Yes for the outer edge in every reading. For "solid, one per GP": not under the literal ray reading
  (F leaves spokes); yes under the neighbourhood reading (F2) once the family has about three times as many bits as the
  outermost shell has GPs; always under S.
- **A simpler protocol?** S: *the family's DI-bits fill the free GPs inside the PSR from the outside in.* It needs no
  directions, no submoment count and no order of arrival; F2 at large N converges to it. The 12-per-submoment flight
  can stay as the physical process; S is what it produces when blocked bits spread sideways before they go deeper.

## 4. What this does and does not settle

- **Near field (the band):** with F2 or S the band is solid and its outer edge tracks the PSR in a well, so the landing
  radius scales with the PSR. That restores the premise of 4327 (occupancy scales with the PSR) *as a protocol*, not as a
  derived property of the walk.
- **Not settled:** OPEN-ALPHA-FARFIELD-1 (4352 §3). Beyond the band occupancy still thins as N/R², and clocks measure α at
  atomic distances. The protocol concerns where bits land, not the flux beyond the band.
- **Band width:** set by N (the family's bit count) and the lattice, not by the PSR alone; the inner edge moves in a well
  (e.g. F2 FCC P = 12, N = 3375: r_in 9.85 → 8.37).

## 5. PD-008

- **The convenient branch this refuses:** registering S as "the founder's protocol". His words say a blocked bit moves
  *inward*; whether it first spreads sideways at the same radius is his call, and it decides between F (spokes) and F2/S
  (solid). The question goes to him as a physical picture; the rule is registered only after his answer
  (TODO-4353-LANDINGRULE).
- **Modelling choices of mine, stated:** the 12 directions per submoment are an icosahedral set under a random rotation;
  F's "near the line" is perpendicular distance 0.6 lattice units (widened by 0.25 when exhausted); F2's rings are
  lattice-neighbour hops. One seed per case; F2 and S are near-deterministic, F varies with the rotation draws.
