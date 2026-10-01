# The Black-Hole Floor Fixes the DI-bit Count: the Landing Band Is 4.4% of the PSR; and α's Far-Field LPI Now Needs Something Else

**Patch:** 4356. **Lane:** EW → foundations (with GR). **Session:** 241.
**Founder:** `founders_voice/4356_ruling_black_hole_is_the_one_bit_per_gp_limit.md`.
**Verify:** `series_standard_model/code/4356_bh_floor_calibrates_dibit_count.py` (output `…count.out`).
**Answers:** 4355 §3. **Registers:** R-DIBIT-COUNT-AT-FLOOR.

## 1. The ruling, joined to the corpus

The founder: one DI-bit per GP holds for any PSR down to maximum compression, where the GPs enclosed by the PSR equal a
GP's DI-bit count N. The corpus already places maximum compression: the R-core (black-hole) surface is where the PSR
reaches its floor **l_P/2, at lapse ½** (R-PSR-LAW-LOG; R-CLOCK-RATE-IS-DISPLACEMENT; the AP-5 cap, where saturation
layers switch on). So:

    N = number of GPs inside a ball of radius PSR_floor = PSR₀/2   (R-DIBIT-COUNT-AT-FLOOR)

= 1/8 of the GPs inside a flat-space PSR. This fits AP-5: below the floor exclusion would fail, and that is exactly where
AP-5's deeper layers take over.

## 2. Consequence 1, a check that passes: the band depth

With N one-eighth of the ball, R-DIBIT-INWARD-FILL fills the outer eighth of the PSR volume:

```
continuum: inner edge (7/8)^(1/3) = 0.9565 PSR  -> band depth 4.35% of the PSR
lattice R0 = 16, 24, 32 GPs: inner edge 0.956 PSR (N/ball = 0.124)
well 1+κ = 1.1: inner edge 0.94 PSR;   1+κ = 1.5: 0.83 PSR;   at the floor (1+κ = 2): the whole ball
```

**4.35% is inside the 2–10% PSR-shell width the founder gave independently** (4323, 4325, 4328). Not a fit: it follows
from the floor at l_P/2 alone.

## 3. Consequence 2: N in absolute terms (one relation, owed a second)

N = (4π/3)(PSR₀/2a)³, with a the GP spacing. GR-1j carries PSR₀/a as an open input. The founder's ruling turns N and PSR₀/a
into one unknown. A second black-hole relation is needed to fix both (his "other known factors about a black hole");
a candidate is the horizon's entropy (area/4l_P² — a count of something per Planck area), not yet tested against the
corpus's R-core (TODO-4356-NCALIB).

## 4. Consequence 3, which goes against the convenient branch: α's far-field LPI

The ruling means **N is smaller than the ball everywhere above the floor**: in ordinary space a charge's family is a
4.4% band with an empty core. 4355 showed that under the registered relay a fixed injected count is diluted over the GPs
in a PSR volume, so in a well the far field rises as (1+κ)³: **k_α = −3**, excluded by ~10⁸ (Lange 2021). The full-ball
escape of 4355 is reached only at the floor itself. **4355's escape is closed by this ruling.**

So the far-field coupling needs a factor that scales with the GPs per PSR volume. The candidate I find is physical,
not a new rule: **the DP-Sea's screening.** If the Sea is packed the same per PSR-sized volume everywhere (it is matter;
its own rulers shrink with the PSR), a well puts (1+κ)³ more Sea dipoles on each GP. If the vacuum is *strongly*
polarisable (screening ε ≫ 1, ε proportional to the Sea dipoles per GP), the far field is divided by the same (1+κ)³
and α stays fixed. Two conditions, both open: the Sea's density is fixed per PSR volume, and ε ≫ 1 with ε ∝ that
density (ε = 1 + χ with χ small would not cancel). This also ties item 5's other open line, OPEN-FP-6-CONSTANTS
(ε₀ from the Sea), to α's LPI.

## 5. Question to the founder (physical picture)

In a gravitational well, each PSR-sized region holds fewer grid points. Does the DP-Sea keep the same number of dipoles
per PSR-sized region, so that each grid point carries more of them? And is it the Sea's dipoles, turning to face a
charge, that weaken its push far away, so that more dipoles per grid point means more weakening?

## 6. PD-008

- **The convenient branch this refuses:** reading the ruling as "the PSR sphere fills solid, so LPI passes." It does
  the opposite: the sphere fills solid only at the black-hole floor; everywhere else it is a band, and 4355's escape
  closes.
- **Mine, not ruled:** the identification of maximum compression with the corpus's l_P/2 floor (it is the corpus's own
  black-hole surface, but the founder named no number); the Sea-screening candidate (§4).
- **For the critic:** (i) does the R-core surface condition (lapse ½) correspond to PSR = PSR₀/2 exactly, or to lapse
  through R-CLOCK-RATE-IS-DISPLACEMENT with another map? A different ratio changes the 4.35% (ratio r → band depth
  1 − (1 − r³)^(1/3)); (ii) check 2–10% is cited as the founder's own statement in 4323/4325/4328 and not derived from
  an earlier toy.
