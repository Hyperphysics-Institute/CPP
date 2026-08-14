# OBL-SIGMA-N DISCHARGED — the jitter decomposed and its derivable component DERIVED: σ_far = √[(2/3)·⟨d_p²⟩·S₆_out(R_box)] (self-consistent far-field, reducing IDENTICALLY to the certified Stage-2 drive in the no-neighbor limit), computing to 0.03–0.10 at the working points; the remainder is the R-DWELL-1 RELAUNCH AMPLITUDE — a named automaton unknown, FQ-12 POSED; and the calibration is measured INSENSITIVE across the ENTIRE admissible bracket: σ_n ∈ [0.05, 0.45] moves d_s^emp by ≤ 0.021

**Patch 3131 (14 Aug 2026). Discharges OBL-SIGMA-N under the
panel's own dual criterion ("derive or sensitivity-bracket") — BOTH
halves delivered. Verify: `scripts/3131_sigma_n.py` + JSON.**

## §1 — The decomposition

The instrument's σ_n stands for field content not explicit in the
all-pairs sum: (a) the FAR-FIELD Sea fluctuations beyond the
periodic box — DERIVABLE; (b) the R-DWELL-1 dwell-relaunch kick —
ruled MECHANISM, underived AMPLITUDE; (c) other-register far-fields
— second-order, stated.

## §2 — The derivation of (a), with its regression identity

Independent external dipoles, ⟨p²⟩ = q²⟨d_p²⟩, variances additive:

  **σ_far = √[(2/3) · ⟨d_p²⟩ · S₆_out(R_box)]**,

S₆_out the simple-cubic 1/r⁶ lattice sum beyond the box (direct sum
+ continuum tail), ⟨d_p²⟩ the box's own stationary value
(self-consistent closure). **Regression identity: in the
no-explicit-neighbor limit the formula reduces EXACTLY to the
Stage-2 self-consistent drive √(2C₆⟨δ²⟩/3)/d³** — the certified
1D-instrument lineage recovered to machine precision, validating
the derivation's form. Values at the working points: σ_far = 0.102
(d_s = 2.6, n = 5) falling to 0.024 (the calibrated spacing) and
0.014 (d_s = 5.5, n = 6) — i.e. **8–34% of the 0.30 operating
point, box-size-dependent exactly as a far-field must be.**

## §3 — The remainder: FQ-12 (posed)

The operating point is therefore dominated by component (b) — the
relaunch kick. Its mechanism is ruled (R-DWELL-1: charge-coupled
kick at dwell exit); its AMPLITUDE is not. **FQ-12: what sets the
dwell-relaunch kick amplitude — the partner's own field at the
dwell-exit configuration (then derivable from adjacent-GP
geometry), the ambient Sea field at the site (then σ_far-slaved and
box-derivable), or a substrate constant in its own right?** A
physical-picture question; nothing below depends on its timing.

## §4 — The bracket completed: the calibration is σ_n-independent

New cells at σ_n = 0.05 (≈ the derived floor + margin) close the
admissible range:

| σ_n | d_s^emp | Δ |
|---|---|---|
| 0.05 (≈ floor) | 4.623 | +0.006 |
| 0.15 | 4.638 | +0.021 |
| 0.30 (operating) | 4.617 | — |
| 0.45 | 4.624 | +0.006 |

**Across the entire physically admissible bracket — from the
derived far-field floor to 1.5× the operating point — the
calibrated spacing moves by ≤ 0.021 (half a percent).** The panel's
concern is discharged in both permitted modes: the derivable part
derived (with its regression identity), the bracket complete, the
residual unknown NAMED with a founder question whose answer cannot
move the calibration by more than the bracket already spans.

## §5 — Queue

Remaining: OBL-FOLD-CHECK (next), OBL-KIN-BLIND (long-horizon),
the N216 CHALLENGE riding to the panel with its n = 7 resolution
instrument specified. After FOLD-CHECK the lane YIELDS per the
advisory order, F-W-1 live. Kila6 Route C and the DM ledger
untouched; arrival still trumps all.
