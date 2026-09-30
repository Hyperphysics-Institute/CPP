# Re-radiation Beyond the PSR Gives Gauss's Law for Free; α Stays Fixed in a Well If a Charge Reads the Net Flow Across Its Own PSR

**Patch:** 4354. **Lane:** EW → foundations. **Session:** 241.
**Founder:** `founders_voice/4354_ruling_sideways_first_and_relay_beyond_psr.md`.
**Verify:** `series_standard_model/code/4354_relay_beyond_psr.py` (output `…psr.out`).
**Answers:** 4353's question; OPEN-ALPHA-FARFIELD-1 (4352 §3) reframed.

## 1. Rulings

- **Landing (choice b):** a blocked DI-bit takes the most radial free GP around its GP_PSR, going deeper only when the
  ring at that radius is full. Registered as **R-DIBIT-INWARD-FILL** beside R-DIBIT-FAMILY-EXCLUSION. By 4353 the band is
  solid (one DI-bit per GP) with its outer edge at the PSR once a family carries about three times the outer shell's GP
  count; the simple order-free statement is *the family fills the free GPs inside the PSR from the outside in.*
- **Beyond the PSR:** no DI-bit of the origin family goes past its GP_PSR. The origin's influence reaches further only
  by re-radiation: GPs holding the origin's DI-bits do what every GP does and radiate again, to their own PSR, and so on.

**Correction to 4352 §3.** The critic's "occupancy beyond the band falls as N/R²" assumed the origin's DI-bits themselves
travel on beyond the band. In the ruled picture they do not; the question is what the relay carries.

## 2. What a relay does (my reading, stated; simulation `4354_relay_beyond_psr.py`)

Model: a unit of influence hops one PSR per relay step in a random direction; each GP passes on exactly what it
received (lossless, isotropic); P = 8 lattice units and the well P = 7.2.

```
per unit emitted from the band         R = 2      4      8      16 PSR
net outward crossings of the sphere     1.000  1.000  1.000  1.000     (both P)
gross crossings / (R/PSR)               2.78   2.62   2.20   1.41      (absorption at 30 PSR bends the tail)
```

- **Gauss's law is automatic.** The net outward flow through every sphere equals what the band emitted, so the net flow
  per unit area falls as 1/R². A lossless isotropic relay is a diffusion, and its steady state obeys Laplace's equation:
  the Coulomb shape needs no extra rule. 4323's Coulomb chain (flux = c·4πR²) is met by the relay without any DI-bit
  travelling beyond the band.
- **Net versus gross.** The raw traffic (all crossings, both ways) falls per unit area as 1/R: the potential's shape.
  The imbalance (from-the-source minus from-behind) falls as 1/R²: the field. A charge that responds to the raw count would
  feel a 1/R force, which is ruled out. So the force must come from the imbalance.
- **The well (local position invariance).** Every length in the relay is a PSR, so in PSR units the well and the flat
  runs are identical. What a test charge reads then depends on its window:

```
test charge reads the net flow through ...   well / flat
one GP of area                                 1.235 = (1+κ)²   → k_α = −2, excluded by ~6×10⁷ (Lange 2021; as in 4327)
its own PSR-sized cross-section                1.000            → k_α = 0
```

## 3. Conditions, stated

The relay passes both tests (Coulomb shape, α fixed in a well) under three conditions:

1. **Lossless:** each GP passes on what it received, no more and no less. If a GP re-emitted a fixed complement
   regardless of what arrived, the far field would grow with the number of relaying GPs; if it lost a fraction per hop,
   the field would fall faster than 1/R², with a loss per PSR that is a new constant.
2. **Every relay length is the PSR** (the hop reaches the relaying GP's own PSR). Consistent with 4327's ruling that step
   scales are set by SSV_abs, i.e. measured in the local PSR.
3. **A charge reads the net flow across its own PSR.** This is the step that decides α's LPI in the far field, the same
   count question as 4327 escape 3, now in relay form.

The relay also has to carry the origin's sign (AP-4's payload carries the origin address, so this is already on file).

## 4. The question to the founder (physical picture)

Far from a charge, a test charge sits in the relayed traffic, which passes it from all sides, a little more from the
source side than from behind. Is it pushed by that difference as it crosses the whole sphere of its own PSR, like wind
on a sail the size of its PSR? Or does it only count what lands on the one grid point where it sits? The first gives
Coulomb's law and an α that does not change in a gravitational well. The second changes α in a well tens of millions
of times more than atomic clocks allow. And second, does each grid point pass on exactly what it received?

## 5. PD-008

- **The convenient branch:** the PSR window (condition 3) is the one that passes, and I have not derived it; it is put to
  the founder, not registered. Condition 1 (lossless) is my reading of "re-radiate"; also put to him.
- **Not claimed:** the relay's constant (how the band's N turns into the unit charge) and the running of α (4331's
  logarithm) — a lossless relay gives a pure 1/R², so the running still needs the DP-arc cloud (TODO-4352-EQUALFORCE and
  4331 stand).
- **For the critic in the next window:** (i) check that a relay with hop = one PSR on the discrete lattice (not the
  continuum used here) still conserves the net flow when the PSR is not a whole number of GP spacings; (ii) check whether
  the solid band of R-DIBIT-INWARD-FILL emits as a sphere of radius PSR or as the whole band depth (it changes the
  near-field constant, not the far-field shape).
