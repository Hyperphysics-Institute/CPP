# The Greedy "Advance Farthest" Rule Sends DI-Bits Down Twelve Rays With No Band; Crowding Ends at Exactly 4304's PSR_min; a 10% Band Cannot Arise From Independent Walkers at 10³⁰ Steps

**Patch:** 4308. **Lane:** EW → foundations. **Session:** 240.
**Founder:** `founders_voice/4308_ruling_di_bit_greedy_radial_step_rule.md`. He asks whether Claude's cell idea is natural
or contrived, and postulates the DI-bit increment rule: step to the empty neighbour that advances farthest in radius,
never reverse, stop when the summed edges equal the PSR.
**Verify:** `series_standard_model/code/4308_greedy_walk_band.py`.

## 1. The cell idea: contrived, withdrawn

4307 §4 proposed sharing at a coarser level of the 600-cell hierarchy so that a PSR would be about ten hops. It was
constructed to rescue the 10% band, nothing more. The founder's rule replaces it, and it is dropped.

## 2. The founder's rule, simulated as stated (rows)

```
icosahedral 12  : landing radius / PSR spans 1.0000..1.0000;  rms/mean = 0.0000
FCC 12          : landing radius / PSR spans 1.0000..1.0000;  rms/mean = 0.0000
```

An uncrowded DI-bit that always takes the neighbour advancing farthest in radius **locks onto a straight lattice ray**:
once it has moved along a neighbour direction d, its radial direction aligns with d and d stays the farthest-advancing
choice. Landing radius = PSR exactly, in every direction. **No band.** And every DI-bit ends on one of the **twelve
neighbour directions**: a volley is twelve pencil beams, not a spherical shell. No 1/r² spreading, therefore no Coulomb
1/r law. Of the two sub-Moment rules on file, only R-OUTWARD-FANOUT (equal shares to all outward neighbours, 3135)
produces a sphere; the greedy rule does not.

## 3. Crowding, and 4304's PSR_min recovered

The empty-GP requirement deflects bits sideways only until each has a GP of its own on a shell, at r = √(N/4π) GPs:

```
  R = 1e+30: fill radius = 8.54e+13 GPs = 8.5e-17 PSR  (= 4304's PSR_min = sqrt(alpha s PSR))
```

**This is exactly the black-hole PSR that 4304 predicted from the founder's surface count**, N = 4π(PSR_min/s)². His
"one DI-bit per GP on a one-GP-deep surface at the smallest PSR" is the crowding radius of his own step rule, arrived at
independently. Beyond it, under the greedy rule, the bits go straight; under the sharing rule, they keep spreading.

## 4. Why the 10% band is closed

With about 10³⁰ steps per PSR, independent walkers' relative spread from path-length variation averages away as the
number of steps grows. What survives at any scale is direction-dependent progress, the lattice's fixed anisotropy: rms
6.2% (FCC) or 5.4% (icosahedral) at most (4306), and zero under the greedy rule. **A 10% band cannot arise from
independent DI-bits at CPP's own GP count.** The 10% (E-2, passes 3–4) was a toy-scale artefact, as 4307 concluded; this
closes the line.

## 5. Where α stands

- The per-layer route (α = f/4π) needed f = 9.2% and cannot get it: **closed.**
- What stands: α = N s/(4π PSR) (4301), with N the emission count per GP per Moment, and the founder's surface count
  now giving N its meaning: the number of GPs on the shell where crowding ends, N = 4π(PSR_min/s)². The two are one
  relation, α = PSR_min²/(s PSR); PSR_min ≈ 10⁻¹⁶ PSR is its prediction, not a check.
- **Everything reduces to what fixes N.** That is the same open item as in 4301.

## 6. Founder question (a physical picture)

**Which rule do DI-bits follow between GPs: "take the neighbour that advances farthest" (twelve straight beams), or
"share among all outward neighbours" (a spreading sphere)?** The Coulomb field's isotropy seems to require the second. If
it is the second, the band's thickness is set by the sub-Moment hop count, which you have said is not a calculated
quantity, and at one GP per hop it is about 10⁻¹²; nothing then depends on a 10% band except the retention geometry that
was minted on it (D-ARC-GAMMA, per 4012), which is flagged.

## 7. PD-008

- **Convenient branch refused.** The cell idea is withdrawn; the 10% band is not rescued.
- **What is solid.** The greedy rule's lock-on and beam collapse (both lattices); the crowding radius; its identity with
  4304's PSR_min; the averaging argument in §4.
- **Downstream flag (D-6).** D-ARC-GAMMA (retention geometry) was built on F-E2-3's 10%; the GR/sea lane should check
  what changes at ≤ 5%.
