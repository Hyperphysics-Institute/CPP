# PRE-REGISTRATION — DIFFERENTIAL DRESSED DRIVE, ROUND 3 (SYMMETRIC CLASSES, MIRRORED-JITTER ENSEMBLE)

**Patch 2907. Committed BEFORE any round-3 leg is executed or read.
Observable and bands carry over from `mobile_sea_differential_amendment.md`
verbatim except where explicitly amended below (the signal-quality
criterion, for a stated reason). Implements the §3 design direction of
the round-2 record.**

---

## §1 — DESIGN, RESPONDING TO THE ROUND-2 DIAGNOSIS

The round-2 systematic was finite-domain asymmetry about off-centre
source positions. Round 3 eliminates it **by construction**:

1. **Two symmetric grid classes, transits centred on x = 0.**
   Class A: the committed on-plane grid (pair-centre xs = 2.5k).
   Class B: a mid-cell grid (pair-centre xs = ±1.25 + 2.5k), symmetric
   about 0 by construction. Both are exactly reflection-symmetric about
   the transit centre; their washboard phases differ by half a period, so
   the class average cancels the washboard fundamental.
2. **Mirror-symmetrised seeded jitter.** Initial pair separations are
   jittered d₀ᵢ = 0.6 + U(−0.05, +0.05), seeded, with **mirror pairs
   (x ↔ −x) receiving identical jitter**, so every initial configuration
   is exactly x-reflection symmetric. Consequences, stated as predictions
   the run itself must verify (§3): at β = 0 with the source at x = 0 the
   entire evolution is symmetric and the axial drive vanishes to floating
   point — for the MOBILE leg as well as the frozen one; the ZBW chatter's
   axial component cancels pairwise; and for β > 0 the only
   symmetry-breaking agent is the source's motion — i.e. the signal.
   Jitter decorrelates ZBW phases across pairs and seeds, giving a true
   ensemble. K = 3 seeds per class.
3. **Detrending is diagnostic only.** The primary estimator stays the raw
   window mean (bands unchanged); a per-leg linear-detrended mean is
   recorded alongside as a diagnostic of accretion drift.

Ensemble: per β ∈ {0, 0.05, 0.10, 0.20}: 2 classes × 3 seeds paired
(mobile, frozen) legs, round-1 grid-matched windows (100/100/75/63),
T_eq = 40. **ΔD(β) = the 6-member mean of the pairwise differences;**
SE(β) = the 6-member standard deviation / √6.

## §2 — BANDS (one amendment, reasoned in advance)

The floor construction 5·ΔF₀ becomes vacuous if the symmetrisation works
(ΔF₀ → floating-point zero would let arbitrarily small noise "pass").
**Amended signal-quality criterion, frozen now:**

> Q₃: |ΔD(β)| > max( 5·ΔF₀ , 3·SE(β) ) at every β, else INCONCLUSIVE.

All else verbatim from the amendment: sign uniform in β required;
β²-only fit ΔD/β = k(1 − c_sub β²); **CANCELLATION |c_sub| < 0.05 /
RETAINED c_sub ∈ [0.10, 0.30] / DRAG SIGN ΔD < 0 ∀β / else
INCONCLUSIVE**; any banded outcome PROVISIONAL pending the original §5
convergence variations; the frozen null-interpretation note stands (a
ΔD consistent with zero at all β is the LW-like-dressing catastrophe,
not cancellation).

## §3 — IN-ROUND VALIDITY GATES (frozen)

- **Symmetry gate:** every β = 0 leg (mobile and frozen, both classes,
  all seeds) must read |D| < 1×10⁻¹² or the symmetrisation is broken and
  the round ABORTS before any β > 0 leg is read.
- **Kernel path:** the gated 2906 kernel, unchanged.

**Worker expectation, declared a fifth time: CANCELLATION — with the
standing caveat (reasoning 2906) that this expectation has gone three
rounds without support and rests solely on the Patch-2900 steady-state
argument.**
