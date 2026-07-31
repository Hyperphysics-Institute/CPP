# FOUNDER RULING — RE-RADIATION IS COHERENT, NOT PARTICULATE SCATTERING

**2 August 2026, Patch 2892. Captured in the same patch that acts on it,
per CONV-009.**

---

## §1 — THE RULING

Worker question: what physically sets the DI-bit scattering probability —
does a bit encountering a DP continue on its heading, or get absorbed and
re-emitted? Founder, verbatim:

> There is no scattering in the particulate sense, only scattering in the
> re-radiation sense at each CP at each Moment. The superimposition
> (subtraction and addition of the fore and aft SSV of both volumes) keeps
> the inertial energy (the SSV_net) conserved.

## §2 — WHY THIS IS DECISIVE (worker note)

**Re-radiation at every CP every Moment is Huygens' principle**, and
Huygens does NOT produce diffusion. Every point on a wavefront re-radiates
and the front nonetheless stays sharp, because secondary wavelets cancel
backward and reinforce forward. **The difference between that and a random
walk is COHERENCE.**

The founder's second sentence settles it: *"subtraction and addition …
keeps the SSV_net conserved."* **Signed superposition with a conserved net
vector.**

**The worker's σ-family (Patch 2890) got this wrong.** At σ = 1 the
re-radiation was isotropic in *amplitude*, discarding the incoming
direction — incoherent scattering, hence the diffusion. **Conserving
SSV_net requires the re-emission to carry the net vector forward.**

## §3 — THE RULE, DERIVED NOT CHOSEN

Require the outgoing distribution at each CP to conserve **both** the
total and the net vector. With 12 FCC directions,
Σ_d d̂ = 0 and Σ_d d̂_i d̂_j = 4δ_ij. Writing w_d = S/12 + k(V·d̂):

    Σ_d w_d   = S + k V·Σd̂ = S                        ✓ (any k)
    Σ_d w_d d̂ = k Σ_d (V·d̂)d̂ = 4kV   ⟹  k = 1/4

> **w_d = S/12 + (V·d̂)/4**

**Note the backward channel goes NEGATIVE** for a directed pulse: with all
amplitude in one direction, S = |V| and w_back = S/12 − S/4 = −S/6. **That
negative weight is the founder's "subtraction," and it is exactly the
backward cancellation that distinguishes a wave from a random walk.**

## §4 — MEASURED (code/2892_coherent_reradiation_rule.py)

| rule | bulk p | ⟨r⟩ at t = 10 | edge/t |
|---|---|---|---|
| **coherent (SSV_net conserved)** | **0.650** | **8.73** | 1.4142 |
| incoherent (amplitude only) | 0.369 | 4.14 | 1.4142 |

**Coherence roughly doubles the transport range and raises the bulk
exponent by 0.28.** The founder's correction is doing real physical work.

**Light cone identical (√2) — third independent confirmation of
σ-invariance.**

**But p = 0.65 is not ballistic (1.0).** Diagnosis: the rule keeps only
the 0th and 1st angular moments — this is the **P1 closure** of radiative
transfer, whose continuum limit is the telegraph equation: wave-like at
short times, diffusive at long. Discarding higher angular moments is what
leaves residual diffusion.

**QUESTION FOR THE FOUNDER, in physical terms:** when a CP re-radiates,
does its emission pattern depend on the *full angular pattern* of what
arrived, or only on the *net* SSV vector? If only the net, we are at P1
and residual diffusion is intrinsic. If the full pattern is retained, the
relay is ballistic.

## §5 — STATICS: NOT MEASURABLE IN THE PRESENT SETUP. ALL ARC CLAIMS SUSPENDED.

Convergence study, M = 24 (relaxation ~144 Moments), T out to 1600
(`code/2892_convergence_stability.py`):

| rule | T=100 | T=200 | T=400 | T=800 | T=1600 |
|---|---|---|---|---|---|
| coherent | −0.000 | +0.071 | +0.035 | +0.017 | **+0.008** |
| incoherent | −1.269 | −1.037 | −0.793 | −0.546 | **−0.339** |

**Both converge toward a FLAT profile (slope → 0), not 1/r.**

**Cause — unambiguous.** The neutralising background **accumulates as a
uniform component**. |Q| becomes dominated by it, so the 1/r variation
near the source is a small perturbation on a large constant and the
log-log slope of |Q| tends to zero. **Longer runs make this worse, not
better** — which is why the T=60 vs T=120 comparison drifted.

**This is the same background contamination diagnosed at Patch 2889 for
the LW observable. The lesson was not carried across to the statics
observable.**

**CONSEQUENTLY SUSPENDED as unmeasured:** every statics slope in this arc
— the Patch 2890 σ-family column (already withdrawn at 2891 for a
*different* reason, the per-voxel estimator), the 2891 shell-mean
diagnostic values, and the §4 numbers above. **Two independent defects
were present simultaneously: a bad estimator AND a contaminated
observable. Fixing the estimator at 2891 did not fix the observable.**

**Required before any statics claim:** subtract the spatial mean (or fit
the *deviation* field rather than |Q|), verify convergence explicitly at
two box sizes, and only then fit.

**UNAFFECTED: G1 and P-A2-1 stand.** Measured on the real engine against a
pointwise Ewald reference, not by profile fitting.

## §6 — A GENUINE FINDING IN PASSING: STABILITY

max|F| over the convergence run: **coherent DECAYS** (0.183 → 0.126,
settling); **incoherent GROWS** (0.292 → 0.404, still rising at T = 1600).

**The coherent rule reaches a bounded steady state; the incoherent one
does not appear to.** That is a substantive difference in favour of the
founder's specification and it was not anticipated.

## §7 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds; Candidate
(B) 79.5%. **G1 and P-A2-1 stand.** CONJ-FP-1 Condition B: OPEN.
λ-window: OPEN, and now blocked on a trustworthy statics observable rather
than on physics.
