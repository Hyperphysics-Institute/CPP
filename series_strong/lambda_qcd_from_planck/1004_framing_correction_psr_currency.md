# Patch 1004 — Framing correction: PSR is the *Planck Sphere Radius*, l_P is an emergent ruler

**Project C. A correction and reinterpretation patch — no new derivation. Triggered by Thomas's
observation that l_P is not the Grid-Point spacing, checked against SR-1 / the c0x companion papers.**

## 1. Naming correction

Patches 1001–1003 glossed **PSR** as "Phase-Space-Restriction." That is wrong. The corpus
(`master_glossary.md`) defines **PSR = Planck Sphere Radius**: the effective displacement a Conscious
Point can achieve per Absolute Moment, with `PSR = l_P` in the rest frame and
`PSR = l_P(1 − kE/V)^(1/3)` shrinking as `SSV_abs` rises (the SR-1 mechanism for time dilation /
the speed limit). The dimensional-transmutation math in 1001–1003 is unaffected, but the physical
gloss mattered here because the whole question turns on what `l_P` *is*. Corrected in the README;
recorded here.

## 2. The category error this exposes

The 1001–1003 framing took `E_P = ℏc/l_P ≈ 10¹⁹ GeV` as a **fundamental UV cutoff** and asked what
fixes a coupling there. On the canonical CPP reading that is the wrong currency, for three reasons,
all from SR-1 / c05 / the glossary:

1. **`l_P` is the rest-frame PSR — an emergent ruler, not the granularity.** It is the per-Moment
   reach ceiling of a single coarse 600-cell motif, not the spacing of the fundamental Grid Points.
2. **`l_P` is environment-dependent.** PSR shrinks with `SSV_abs`, so `l_P` is smaller in a
   high-stress region (near mass) and larger in flat space. A scale that varies with the local Sea
   state is not a fixed fundamental cutoff to run a coupling from.
3. **The Grid-Point spacing is finer than `l_P` (nested-600-cell hierarchy, Patch 0736).** The
   coarse motif is the `l_P`-scale tile; the fine nesting runs to a sub-Planck GP spacing. *(The
   specific "~10³⁰ GPs per l_P" figure is an unverified early estimate — flagged, not relied upon;
   the qualitative sub-Planck nesting is the canonical part.)* Crucially, Patch 0736 verified the
   resolution choice "appears in **none** of the prediction formulae," so it cannot be invoked to
   *derive* Λ_QCD without overturning that finding.

## 3. Why this reinterprets — not retracts — the 1003 negative result

The negative result stands as computed. But its *meaning* changes. The absolute Planck scale is, by
the corpus's own statement (c05: `G = ℏc/m_P²` is the Planck-mass definition rearranged; TODO-014:
"absolute scale is **one shared calibration, not derived**"), a single calibrated anchor — not a
derived quantity. Confinement is set by `PSR_eff → l_P/2`: a *fraction* of baseline PSR, in the same
PSR currency as `l_P`. So the confinement scale and `l_P` are not two independent constants
separated by 20 orders that RG-running must bridge — they are tied by a PSR ratio, both expressed in
the one calibrated anchor.

Therefore **the absolute QCD/DP scale being "calibrated, not Planck-derived" is the same calibration
that `G` and `l_P` already are** — not a separate failure of the strong sector. The 1003 negative
was structural: it asked for an exact derivation of an absolute scale that CPP treats as a shared
calibration everywhere else. Of course it did not close.

## 4. Where the derivable content actually lives (redirect to op:sigma)

What CPP *can* derive is the dimensionless **ratio** — the relationship between the confinement scale
and baseline PSR, and the internal DP-spectrum ratios — not the absolute value of either anchor.
Concretely that is `op:sigma`: the string tension `σ` (and `r_conf`) from `sea_strength` + cage
geometry + the `PSR_eff = l_P/2` fraction, via the C14 self-consistency, at the **IR end** where the
lever arm is short (`ln(2.2 GeV / 0.218 GeV) ≈ 2.3`) and the problem is well-conditioned — exactly
the regime the 1002 sensitivity theorem showed is tractable (`N/α ≈ 6`, not 2300).

Honest forward expectation (to be tested, not assumed): `op:sigma` may *also* bottom out at the
shared calibration, because `σ` in GeV/fm still needs one absolute length, and the only fundamental
length is `l_P` (itself calibrated). If so, the result is: **ratios derivable, absolute scale = the
one shared calibration** — a clean, consistent, non-failure outcome. The run will decide.

## 5. Corpus pointers (for the next run)

- `master_glossary.md` — PSR = Planck Sphere Radius; `PSR = l_P(1−kE/V)^(1/3)`; SSV_abs entries.
- SR-1 + `series_relativity/SR_companion_papers/` (c01, c02, c05 Newtonian gravity from SSV,
  c07 weak-field, c08 strong-field) — the PSR / l_P / SSV / gravity foundations.
- `series_relativity/development/reasoning/0736_q1_canonical_resolution.md` — nested-600-cell
  hierarchy; resolution choice enters no prediction.
- c05 / TODO-014 — `G = ℏc/m_P²`; absolute scale = one shared calibration, not derived.
- SS-1 `thm:sea_strength` (sea_strength ≈ 0.178 geometric), C14 (r_conf/σ self-consistency) — the
  op:sigma inputs.

## 6. Status / housekeeping

Naming corrected (README). Negative result reinterpreted, not retracted. No new derivation; no
THEO/PRED; SS-1 and the DP-Sea appendix untouched. The `master_glossary.md` line that still says
"the spacing between Grid Points is the Planck length l_P" contradicts the canonical 0736 reading and
is flagged for a **separate** correction patch (shared file → STOP-and-warn; carries the 10³⁰
caveat). This patch stays in-lane (`lambda_qcd_from_planck/`).
