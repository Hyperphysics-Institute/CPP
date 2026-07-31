# CORRECTION TO PATCH 2890 — THE STATIC-SLOPE COLUMN USED A BAD ESTIMATOR

**Patch 2891. Self-caught on cross-check while attempting the λ-window
test. Patch 2890 is already applied; this correction is issued
immediately rather than at session close.**

---

## §1 — WHAT IS WRONG

Patch 2890 §3 reported a "static slope" column and concluded that at
σ = 1.0 the family produces *"essentially 1/r (−0.97)."* **That number is
an artifact of the fitting method and the conclusion is WITHDRAWN.**

The estimator used was a **per-voxel log-log fit**: every voxel in the
radial mask contributes one point to `polyfit(log r, log F)`. That is a
bad estimator for a radial profile, for two compounding reasons:

1. **Voxel count grows as r²**, so the outermost shells dominate the fit
   by sheer multiplicity.
2. **Within-shell scatter is large** because of lattice ray structure, and
   scatter in log-space biases the slope.

The correct estimator is a **shell-mean profile**: average F over each
radial shell, then fit the means.

## §2 — THE NUMBERS (σ = 1.0, M = 48, T = 80)

Shell-mean profile:

| r | ⟨F⟩ |
|---|---|
| 3 | 4.623e−02 |
| 4 | 3.710e−02 |
| 5 | 2.178e−02 |
| 6 | 1.629e−02 |
| 8 | 7.372e−03 |
| 10 | 3.916e−03 |

| fit range | per-voxel (2890's method) | **shell-mean (correct)** |
|---|---|---|
| [3, 6] | −0.276 | **−1.564** |
| [3, 10] | **−0.970** ← reported at 2890 | **−2.067** |

**The −0.970 landed near −1 by coincidence.** The same data under a sound
estimator gives −2.07 over that range.

**Robustness:** removing the neutralising background changes the
shell-mean slope by < 0.5% (−2.067 → −2.067 at [3,10]), while it changes
the per-voxel slope from −0.970 to −2.339. **The correct estimator is
stable against a change the bad one is wildly sensitive to** — which is
itself the diagnostic.

## §3 — WHAT THIS DOES AND DOES NOT AFFECT

**UNAFFECTED — the G1 ratified result stands.** G1 was measured on the
actual AUTOMATON-2 engine against a **Ewald reference**, pointwise, to
±0.4%, with Δp = 0.010. It did **not** use this crude power-law fit. **The
error here is in the Patch 2890 σ-family exploration, not in the ratified
gate.** P-A2-1 CONFIRMED is untouched.

**UNAFFECTED — the light-cone invariance.** edge/t = 1.0607 identical
across all σ was a direct maximum-extent measurement with no fitting. That
was the load-bearing finding of 2890 and it survives intact.

**UNAFFECTED — the bulk-exponent trend.** Measured from ⟨r⟩ vs t, monotone
1.34 → 0.63. The absolute offset was already flagged at 2890; the trend
stands.

**WITHDRAWN — that σ = 1 reproduces 1/r statics.** Not established. The
profile is not a clean power law over [3,10]; it **steepens with radius**
(−1.56 over [3,6] to −2.07 over [3,10]), which is consistent with either
non-convergence to steady state or a boundary effect at M = 48, and I have
not separated those.

**CONSEQUENTLY UNRESOLVED — the λ-window question.** Patch 2890 §4 claimed
both prior results could hold simultaneously if λ falls between the
inertia scale (r ~ 1–2) and the Coulomb scale (r ∈ [3,6]). **That test
cannot be run with a broken statics estimator, and it has not been run.**
It remains exactly as unestablished as 2890 flagged it.

## §4 — A SECOND BROKEN OBSERVABLE, CAUGHT IN THE SAME RUN

The anisotropy measure built to detect surviving ray structure returned
**CV = 0.000 exactly** at r = 1.4142 and r = 2.8284 for every σ, including
σ = 0 (pure rays, maximally anisotropic).

**Cause:** those radii are √2 and 2√2 — shells containing only
**lattice-symmetry-equivalent sites**. All members carry identical values
by symmetry, so the coefficient of variation is identically zero
regardless of the physics. **The observable measures lattice symmetry
class, not anisotropy.** Discarded; a ray-structure detector must compare
across inequivalent directions at fixed radius, or use an angular
multipole decomposition.

## §5 — WHY THIS WAS CAUGHT

Cross-checking a new measurement against a committed one. The λ-window run
reported σ = 1.0 → slope −0.259, against 2890's −0.970 for the same
construction. **Two of my own numbers disagreeing by a factor of four is
what forced the diagnostic.** Neither was reported onward until the
disagreement was resolved.

**This is the third estimator/interpretation error self-caught in this arc**
(after the c_lat misreading at 2887 and the "no light cone" overclaim
corrected at 2890). The common failure mode: **a number that lands close
to a physically expected value gets accepted without checking the
estimator that produced it.** −0.97 was accepted because 1/r was expected.

## §6 — STANDING

**Ledger untouched:** 1B OPEN; PR7 PARTIAL; six of seven; B7 holds
DM-1/DM-2/DM-3; Candidate (B) 79.5%. **G1 and P-A2-1 stand.**

**CONJ-FP-1 Condition B: OPEN.** The λ-window question: **OPEN and not yet
tested.**
