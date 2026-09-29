# The Fill Is Absorbed Into the Swing (α Fixes Only L/f); What Matters Is Saturation, and Both Natural Stop Criteria Approach It

**Patch:** 4329. **Lane:** EW → foundations. **Session:** 241.
**Founder:** `founders_voice/4329_ruling_no_stop_criterion_let_empirics_decide_fill.md` (verbatim).
**Verify:** `series_standard_model/code/4329_stop_criteria_saturation.py`.
**Answers:** 4328 §5. **Recasts:** CAL-ZBW1-SWING as a calibration of L/f.

## 1. The ruling

Only the family-exclusion rule is specified; **no stop criterion is**. So the rule by itself fixes neither a solid band
nor a partly empty one. *"I would let the empirics dictate … if this is a significant variable."*

## 2. Is the fill a significant variable for α? No: it is absorbed

α = f·PSR/(2L) (4328). The fill f and the swing L enter **only as L/f**. So measuring α fixes L/f = PSR/(2α) ≈ 68.5 PSR
and cannot separate them: a solid band with a 68.5-PSR swing and an 88%-filled band with a 60.6-PSR swing give the same
α. **CAL-ZBW1-SWING is recast as a calibration of the effective swing L/f**, which is what α actually measures.
Separating f from L needs a second observable that depends on one without the other, such as the landing band's
thickness or its fill seen some other way. None is on file; that is the empirical route he points to.

## 3. What is significant: saturation (rows)

Local position invariance does not care what f is, only that **f does not change in a well** (4328 §3). Whether it
stays fixed depends on the stop criterion he has left open, so both natural ones are tested. They match 4309's two
readings of the PSR: S1 stops once the summed path reaches P (PSR as path); S2 stops once the distance from GP_origin
reaches R (PSR as landing radius). Each is tested as N grows, and in a "well" (the same N into a shell 10% smaller):

```
crit     N   fill  fill in well (P,R x0.9)   change  band rms
  S1   200  0.204                    0.176   -0.028     0.094
  S1   800  0.591                    0.579   -0.013     0.107
  S1  2000  0.888                    0.885   -0.003     0.132
  S2   200  0.366                    0.445   +0.080     0.040
  S2   800  0.773                    0.780   +0.007     0.068
  S2  2000  0.891                    0.914   +0.023     0.108
```

- **Under both criteria the fill climbs with N and approaches a plateau near 0.89**, and **the well's effect on the
  fill shrinks as the band saturates** (S1: −0.028 → −0.003; S2: +0.080 → +0.023, the latter still visible in these
  single runs).
- **The plateau looks similar under both criteria**, which suggests it is a property of exclusion packing on the
  lattice rather than of the stop rule. That is suggestive only, not shown.
- These are single small runs (a shell of a few hundred GPs); they cannot test invariance at the 10⁻¹⁵ the clocks
  require. What they support is the structural claim: **at saturation the fill is a constant of the rule and the
  lattice, and a well changes the band's depth, not its fill.**

## 4. What I think

His answer is right, and it clarifies what the empirics can and cannot say. **The value of the fill is not a separate
question for α**: it hides inside the calibrated swing. **Whether the band is saturated is the question that matters**,
because local position invariance holds only there. On the toy, both natural stop criteria drive the band toward
saturation as more DI-bits are sent. Real bands, 2–10% of a PSR deep and ~10²⁸ GP-layers thick, would be deep in that
regime if the toy's trend holds. So α's chain is now:

  **α = PSR/(2 L_eff), L_eff = L/f_sat ≈ 68.5 PSR** — one calibrated effective swing, LPI-safe wherever bands are
  saturated, with the sign of α's running already right (4326).

## 5. No founder question this patch

Nothing here needs a physical picture from the founder: the fill is absorbed and the stop criterion is his to leave open
until an observable needs it. The next steps are computational (§6 and the queue).

## 6. PD-008

- **Convenient branch, marked.** "The fill is absorbed" conveniently makes his open question harmless. It follows
  directly from α = f·PSR/(2L), so it stands on the algebra.
- **Not established:** the plateau (single runs, small shells); the well-invariance at saturation (the S2 change is
  still +0.023 at N = 2000); that the plateau is criterion-independent.
- **Solid:** α depends only on L/f; LPI needs saturation, not a particular f; both criteria trend toward saturation on
  the toy.
- **For the critic in the next window:** (i) repeat §3 with several seeds and larger shells, to put error bars on the
  plateau and on the well change; (ii) run the same on the 600-cell's icosahedral neighbourhood rather than FCC;
  (iii) look for a second observable sensitive to f or L separately (the band thickness, D-ARC-GAMMA's retention
  geometry, 4308/4309).
