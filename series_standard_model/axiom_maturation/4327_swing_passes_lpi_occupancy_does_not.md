# The Swing Passes Local Position Invariance; the Landing Occupancy Does Not — Unless a GP Counts Each Source Once per Moment

**Patch:** 4327. **Lane:** EW → foundations. **Session:** 241.
**Founder:** `founders_voice/4327_ruling_dp_arcs_move_by_ssv_net_scaled_by_ssv_abs.md` (verbatim).
**Verify:** `series_standard_model/code/4327_lpi_occupancy_test.py`.
**Answers:** 4326 §6. **Presses:** 4326's T2 to the end.

## 1. The ruling, and what it settles

*"The CPs in the DP-arcs move because of the SSV_net (V_i), but the scale of their movement is determined by the
absolute space stress (SSV_abs)."* So the swing L is a sum of V_i-driven steps, each measured in the local PSR. **L/PSR
is SSV_abs-invariant to all orders, and the swing part of 4326's T2 passes.** Charge stress (SSV_net) changes the steps
and can shorten the swing relative to the PSR, which is T1's direction.

## 2. Pressed to the end: α has a second factor, and it fails T2 (rows)

α = c·PSR/(2L) (4324) has two factors. L/PSR is now invariant. The other is the **landing occupancy c = N / (GPs of the
landing shell)**. In a gravitational well, SR-1's PSR_eff = l_P/(1 + κ) shrinks, and c07's light-slowing needs the DI-bit
landing radius to shrink with it. AP-4, as the founder stated it at 4311, keeps every GP's emission N the same in any
field. So the shell has fewer GPs, and **c rises as (1 + κ)²**:

```
counting rule at the landing GP                         k_alpha   vs |k_alpha| < 1.6e-06
additive (sum of all DI-bits)                            -2.000   EXCLUDED by ~1e+06
per-source once (origin address, AP-4 payload)           -0.000   allowed
N scales with shell GPs (contra 4311)                    -0.000   allowed
```

**If a CP adds up every DI-bit landing on its GP, α couples to the gravitational potential with k_α = −2, excluded by
atomic clocks (|k_α| < 1.6 × 10⁻⁶, Leefer et al. 2013) by a factor of about a million.** This is not a problem with the
swing; it is a problem with the count.

## 3. The escapes

1. **Per-GP emission rises in a well** (N ∝ the shell's GP count). The founder ruled this out at 4311 (AP-4: *"every GP
   emits the same number of DI-bits, regardless of whether it is in a gravitational field or not"*). Closed unless he
   revisits it.
2. **The DI-bit landing radius does not shrink in a well.** Then light would not slow in a well, contradicting c07 and
   exterior GR. Closed.
3. **A GP registers each source once per Moment.** AP-4's payload carries the origin address, so a GP *can* tell that
   several DI-bits came from the same source. If it registers that source once, the occupancy is capped at 1 wherever
   the shell is fully covered, and **α = PSR/(2L) exactly, everywhere: the swing is the whole of α.** Sums over
   *different* sources are untouched, so superposition of fields still holds, and the founder's 4324 wording (*"the sum
   of all the DI-bits will direct the CP's next displacement"*) survives as a sum over sources. It carries one
   condition: the least-stressed region anywhere must sit exactly at full covering, since any site *less* stressed than
   that baseline would have c < 1 and a smaller α. **No registered rule says a GP dedupes by origin**, so this is a
   counting rule to be decided, at axiom level (the A3′/AP-4 perceive step).

## 4. What I think

The founder's answer passes the part of the test I set, and it moves the problem somewhere sharper. The count-based
α, as built from 4301 to 4326, is **falsified by local position invariance at O(1)** if DI-bits from one source simply
add up at a GP. The only escape that keeps AP-4 as he stated it and keeps gravity bending light is **per-source counting**.
That escape is attractive beyond saving the model: it makes α purely a property of the Planck ZBW's swing, α = PSR/(2L),
with the occupancy fixed at 1 by construction rather than calibrated. That is also the convenient branch, so it is
marked (§6) and put to the founder rather than adopted.

## 5. Founder question (a physical picture)

**When several DI-bits from the same charge land on one grid point in the same Moment, does that grid point count them
all, or does it register that charge once?** In a gravitational well a charge's landing shell is smaller, so each grid
point gets more of its DI-bits. If they all add, α would change with gravitational potential about a million times more
than atomic clocks allow. If a grid point registers each source once (it can tell them apart by their origin address),
α stays fixed everywhere, and it becomes exactly one over twice the swing: α = PSR/(2L).

## 6. PD-008

- **My earlier claim, stated and corrected.** 4326 said T2 "requires SSV_abs to rescale the swing with the PSR". That
  was necessary but not sufficient: it omitted the occupancy factor, which fails T2 at O(1) under additive counting.
- **Convenient branch, marked.** Per-source counting rescues the model and makes α = PSR/(2L), the cleanest form yet.
  It is an axiom-level counting rule with no registration and one cosmological condition (baseline at full covering).
  It is put to the founder, not adopted.
- **Solid:** the (1 + κ)² occupancy scaling under AP-4 + c07; k_α = −2 for additive counting; the exclusion factor.
- **Checked here (D-7): DI-bit transport slows with the PSR.** `frontier_sectors/GR.md` (Patch 3367, Route B): *"AP-4's
  relay carries DI-bits beyond one PSR, so a smaller PSR slows the census but does not truncate it; asserted in
  code."* The landing radius per Moment is the PSR, so it shrinks in a well, as §2 assumes.
- **For the critic in the next window:** (i) whether 0739's symmetric gravity
  channel (μ/ε ratio) and this count-based α can both hold, or whether one supersedes the other; (ii) whether
  per-source counting alters any registered result that assumed additive arrivals (grep "sum of arrivals", Φ = count in
  A3′).

**Note (Patch 4328):** escape 3 is not a new counting rule: the founder's 4308 stepping rule ("GP_empty", clarified at 4328 as empty of the same GP_origin family) already caps a family at one DI-bit per GP; registered as R-DIBIT-FAMILY-EXCLUSION. It prevents stacking but not voids, so LPI also needs the band saturated (fill f_sat, about 0.88 on a toy); then α = f_sat·PSR/(2L). See `series_standard_model/axiom_maturation/4328_family_exclusion_caps_occupancy_lpi_needs_saturation.md`.
