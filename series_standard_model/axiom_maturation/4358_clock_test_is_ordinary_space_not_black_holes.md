# The α Test Is in Ordinary Space, Not in Black Holes: One DI-bit per GP, Kept as It Is, Predicts an Annual α Swing 10⁸ Too Large

**Patch:** 4358. **Lane:** EW → foundations. **Session:** 241.
**Founder:** `founders_voice/4358_thoughts_no_rule_change_bh_interior_alternating_cp_lattice.md`.
**Verify:** `series_standard_model/code/4358_clock_prediction_k_minus_3.py` (output `…3.out`).

## 1. A misunderstanding of mine to clear (my 4356 §5 wording)

The founder read the DP-Sea question as being about black holes. It was about **ordinary space**. The failing test is
an atomic clock on Earth, where the PSR is smaller than in deep space by about one part in 10⁹, nowhere near filling.
No rule change at a filled PSR was proposed, and none is needed: one DI-bit per GP (R-DIBIT-FAMILY-EXCLUSION, R-DIBIT-
INWARD-FILL, R-DIBIT-COUNT-AT-FLOOR) stays exactly as ruled.

## 2. His question answered: what "never more than one DI-bit per GP", unchanged, predicts

Yes, it makes a prediction, and the prediction contradicts the clocks. With the count N fixed and the band never
full outside a black hole, the registered relay (4355) spreads a charge's influence over the GPs in a PSR-sized volume.
Lower in a gravity well each PSR holds slightly fewer GPs, so the far push per PSR is slightly stronger: α rises by three
times the fractional deepening of the potential (k_α = −3).

The cleanest test is the Earth's elliptical orbit: the Sun's potential at a laboratory swings every year.

```
Sun's potential at 1 au                    9.87e-9 c^2;  annual swing (peak to peak) 3.30e-10 c^2
predicted annual swing in alpha (k = -3)   9.9e-10
allowed (Lange et al. 2021, Yb+ vs Cs, 2σ) 1.2e-17
excess                                     ~8e7
```

So the rules as they stand are contradicted by the clocks by about eight orders of magnitude. Something else in the
ordinary-space picture must cancel the (1+κ)³.

## 3. The DP-Sea in ordinary space (the question restated)

The candidate is the same thing 4331 needs for α's running: the DP-Sea's polarisation around a charge (the cloud that
makes α grow at short distance is the Sea's dipoles partly facing the charge and screening it at long distance). If the
Sea holds the same number of dipoles per PSR-sized region everywhere, a well puts more dipoles on each GP; if the
screening is strong and grows with that number, it cancels the (1+κ)³. In ordinary space the Sea is not close-packed:
its DPs (or DP-arcs) can turn, which is what the running needs anyway. The founder's black-hole objection (§4) does not
bear on this.

## 4. His black-hole interior picture (recorded; reconciled in outline)

He pictures a saturated interior as a close-packed lattice of alternating ± CPs, no functional pairs (no DPs), each CP
oscillating in the cage of its own DI-bit zone, with information stored in that oscillation. Against the corpus:

- **Consistent:** 3703's DRAIN puts the matter in a Planck-density speck; his lattice is a picture of what the speck is
  made of. 3701's lockstep result (all CPs displacing together) fits a caged lattice that oscillates but does not
  exchange positions.
- **To reconcile:** R-EXCL-RETIRED (1 Sep) retired one CP per GP, so "close-packed" must mean packed at the PSR floor
  (one CP per l_P/2 cell, ~10⁹⁰ GPs each), not one per GP. And AP-5 D4 ("storage in layer registers, nothing
  discarded") already places a black hole's stored information in registers; his caged oscillation is a candidate
  for what those registers are. Registered as TODO-4358-BHLATTICE.

## 5. PD-008

- **The convenient branch this refuses:** letting the black-hole discussion stand in for the ordinary-space test. The
  clock contradiction is computed (§2) and stays open.
- **Mine:** the restated Sea question (§3) and the outline reconciliation (§4).

---
**Withdrawal (Patch 4359).** §2's "contradicted by ~8×10⁷" is withdrawn. An independent critic found that the premise (a fixed-count source, read without a
lapse or medium dictionary) would also make Newton's constant vary with position in gravity, failing lunar laser ranging
by ~10⁴; A3′'s metric coupling gives k_α = 0 by construction. The result is withdrawn as established; the source rule is
owed for all channels together (TODO-4359-SOURCERULE). See `4359_sea_cannot_fix_alpha_and_4355_premise_would_break_gravity.md`.
