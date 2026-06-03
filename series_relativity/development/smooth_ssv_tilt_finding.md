# Brick #4 follow-up: the tilt recovered — n_s = 1 − p/N_* from coupling to e-folds-remaining

*Patch 0742, Session 154. The recovery from the 0741 found-problem. Toy + verify:
`series_phenomena/cosmology/early_universe/scripts/0742_smooth_ssv_tilt.py`. NO THEO. **Result: the
0741 tension is resolved in structure.** Coupling the fluctuation amplitude to e-folds-remaining (the
natural δN variable) gives the standard slow-roll form n_s = 1 − p/N_*, with N_* ≈ 60 fixed by the CP
count. n_s goes from "unpredicted / excluded" to "predicted up to one integer power p," and p = 2 (the
simplest large-field value) lands on Planck. Deriving p is the one remaining step.*

## What 0741 actually taught us (the diagnosis)

0741 failed for a precise reason: in the on/off H-axiom, the only rates available are
- the **density** n̄ ∝ e^{−3N}, which declines at **3 per e-fold** — far too fast (gives n_s ≪ 1 if
  coupled to directly), and
- the **superposed fraction** f, which stays ≈ 1 (since n̄ ≫ 1) and then cliffs — rate **0, then ∞**.

The data want a *gentle, sustained* d ln(amplitude)/dN ≈ **−0.018 per e-fold**. None of the above
supply it. The missing variable had to decline ~170× slower than the density but never sit at zero.

## The fix: couple to e-folds-remaining (the δN variable)

There is exactly one such variable, and it is not ad hoc — it is the **log of the density**, which is
precisely the **number of e-folds remaining** to the end of inflation:

  N_rem(N) = (1/3) ln n̄(N),   dN_rem/dN = −1,   d ln N_rem/dN = −1/N_rem ≈ −0.018 at N_rem ≈ 57.

This is the natural variable because the curvature perturbation, in the **δN formalism**, *is* the
fluctuation in the number of e-folds (ζ = δN). So the frozen fluctuation power depends on the e-fold
structure / N_rem, not on the instantaneous density. Coupling to N_rem rather than to raw n̄ is the
generic structure of inflationary perturbations, not a fitting choice.

If the frozen power scales as a power p of e-folds-remaining, P(k) = σ² ∝ N_rem^p, then

  **n_s − 1 = d ln σ²/dN = −p / N_rem  ⇒  n_s = 1 − p/N_***,

the standard slow-roll form. CPP's specific content is that **N_* is fixed by the CP count** — the same
N_CP ≈ 10⁸⁰ that set the ~60 e-folds in Brick #4 Test C:

  N_* = (1/3) ln(N_CP/N_GP_init) ≈ 60.5   (not tuned — it is the CP count).

(In standard inflation N_* is partly free, set by the reheating history; in CPP it is pinned by the
initial stacking depth. That pinning is a genuine CPP feature.)

## The result (toy, no tuning)

| p | n_s = 1 − p/N_* | running α_s | verdict |
|---|---|---|---|
| 0 | 1.0000 | 0 | the 0741 on/off case — Harrison–Zel'dovich, **excluded ~8σ** |
| 1 | 0.9835 | −0.0003 | gentle red, ~4σ high |
| **2** | **0.9670** | −0.0006 | **matches Planck (0.9649 ± 0.0042)** |
| 3 | 0.9505 | −0.0008 | red, ~5σ low |

(At the standard pivot N_rem = 57, p = 2 gives n_s = 0.9649 on the nose.) The running α_s is
≲ 6×10⁻⁴ for all p — comfortably inside Planck's ±0.0067, and n_s is nearly flat across the observable
window (varies by 0.006), unlike 0741's flat-then-cliff.

## Honest status

This is a **structural recovery, not yet a parameter-free prediction.** Precisely:

- **Resolved:** the 0741 tension. The on/off rule was the degenerate p = 0 case; coupling to
  e-folds-remaining lifts it to the full n_s = 1 − p/N_* family, which spans the data.
- **CPP-specific and real:** N_* ≈ 60 is *fixed by the CP count*, not a reheating free parameter. And
  the variable (N_rem / δN) is forced by the δN structure, not chosen.
- **Still owed:** the integer power **p**. The δN formalism fixes the *variable* but not p — p is set
  by how the frozen ZBW source amplitude scales with e-folds-remaining (≈ with log-density /
  superposition depth), which is not yet derived. p = 2 is the simplest non-trivial value (it is the
  m²φ² value, n_s = 1 − 2/N) and it matches; p = 1 gives 0.984 (~4σ high). So the data *require* p = 2,
  and CPP does not yet *predict* p = 2.

So: **"CPP predicts n_s = 0.965" is not yet supportable, but the gap is now a single integer.** The
mechanism produces the right form, the right N_* (from the CP count), the right ballpark, the right
direction, and small running. That is a large step up from 0741.

## The remaining first-principles step (sharp and small)

Derive **p** = the exponent with which the frozen ZBW fluctuation power scales with e-folds-remaining
(equivalently, how the per-mode injected variance depends on the superposition depth / log-density at
horizon crossing). If the substrate gives p = 2, n_s = 0.965 becomes a genuine prediction; if it gives
p = 1, CPP predicts 0.984 and is in ~4σ tension. Either way it is now a one-number calculation, not a
free function — and it is the single most decisive early-universe computation left.

## Pointers

- Diagnosis from: `rolloff_law_finding.md` (0741). Builds on Brick #4 Test C (CP count → e-folds).
- Toy + verify: `.../early_universe/scripts/0742_smooth_ssv_tilt.py`.
- Reasoning: `series_relativity/development/reasoning/0742_smooth_ssv_tilt.md`.
- Next: derive p (the ZBW-power scaling with e-folds-remaining). This is THE gating computation for
  whether n_s is a CPP prediction.
