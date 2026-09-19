# TEST-A3G-1 — Vacuum Magnetisation. Falsifier does not fire; one claimed payoff does not materialise.

**Patch:** 4121. **Lane:** EW. **First of the three falsifiers** in the suite Thomas authorized
at 4115, now run against the provisionally adopted axiom (4120).
**Verify:** `series_standard_model/code/4121_a3g1_vacuum_magnetisation.py`.

---

## Result

| sea configuration | \|Σ A\| | verdict |
|---|---|---|
| **antiparallel (DP-CAL-1)** | **exactly 0**, every N, no fluctuation | non-magnetic, exactly |
| parallel + isotropic | mean 0, RMS ~ √N; density ~ 1/√N → 0 | non-magnetic **on average only** |
| parallel + aligned | grows as N | **ferromagnetic vacuum — excluded** |

**A3G-1 DOES NOT FIRE.** The axiom does not force a magnetised vacuum: the aligned branch is
excluded by the sea's own isotropy, and the isotropic branch gives a magnetisation density
falling as 1/√N, which vanishes for any macroscopic region.

## The honest finding — and it is the convenient branch that fails

Only **DP-CAL-1 (antiparallel spins)** gives exact, pointwise, fluctuation-free cancellation.
Without it the vacuum is non-magnetic only *statistically*, and the cancellation is not exact
at any finite scale.

> **The adopted axiom does NOT make DP-CAL-1 dispensable. DP-CAL-1 remains load-bearing for
> F2, exactly as it was at Patch 4107.**

**This retracts a payoff I claimed at 4111.** In the scoping I listed, as payoff 5, that the
axiom would let DP-CAL-1 *"be derived or refuted instead of calibrated"* because it would give
the spin attribute a formal referent. On this test that does not materialise: the axiom supplies
the **referent** but not the **derivation**. Having a formal A_i does not tell you how the two
CPs in a DP orient relative to one another — that remains the founder's assumption from 4107,
still carried as a calibration.

Marked per PD-008: the convenient branch was "the axiom absorbs the calibration." It does not.

## What this changes

- **F2 status unchanged:** HOLDS under DP-CAL-1. It does not upgrade to derived.
- **The 4111 payoff list is now 4 items, not 5.** Spin-½/Pauli doubling, the THEO-SPIN-1
  referent, the fermion/boson assignment and the ⟨L̂+2Ŝ⟩ spin half all stand; DP-CAL-1
  promotion is withdrawn pending A3G-9, which should now be expected to return the same way.
- **A3G-9 should be re-scoped or retired.** It asked exactly this question from the other end;
  this result largely answers it negatively in advance.

## Remaining falsifiers

**A3G-2** (spin-dependent fifth force vs torsion-balance / comagnetometer bounds) and
**A3G-3** (EM parity re-derived from the axiom alone, without DP-CAL-1) are still live. **A3G-3
is now the sharper of the two**, since this result shows the axiom alone does not carry the
sea's cancellation — A3G-3 asks whether that shortfall reaches an observable.

No verdict moved. χ₄ remains provisionally adopted; nothing here withdraws it.
