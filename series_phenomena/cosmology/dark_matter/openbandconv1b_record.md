# **OPEN-BAND-CONV-1b EXECUTED — NO ARM COMPARISON IS ADMISSIBLE AT ANY β**: on the campaign's own geometry F_JIT = 1.59e-04 / 3.03e-04 / 3.21e-04 (β = 0.05/0.10/0.20), but the frozen falsifier fires UNSTABLE at all three — **and it fires for the OPPOSITE reason it fired at 3186, which exposes a defect in the worker's own rule: the two-floor RATIO test is DIRECTION-BLIND.** At 3186 it caught a real hazard (systematic class spread ≫ statistical floor); here it fires because the across-seed scatter is NEGLIGIBLE (1.8e-07 against an archive floor of 1.2e-04) — **a healthy configuration failing a test designed to catch its opposite.** The corrected one-directional rule is stated for a FUTURE freeze and is **NOT applied here**, because rescuing a frozen criterion after seeing its output is the exact extraction this programme refuses; **so the anomaly's status against a valid comparator is UNRESOLVED, and 3186's IN-BAND stays withdrawn**

**Patch 3188 (22 Aug 2026). Executes `openbandconv1b_prereg.md`
(Patch 3187, committed BEFORE this ran). Container only.**

## §1 — The comparator on the geometry the arms actually used

| β | F_JIT | across-seed SE | archive floor | ratio | §3 verdict |
|---|---|---|---|---|---|
| 0.05 | **1.5912e-04** | 1.75e-07 | 1.194e-04 | 681 | **UNSTABLE** |
| 0.10 | **3.0258e-04** | 3.32e-07 | 1.084e-04 | 327 | **UNSTABLE** |
| 0.20 | **3.2130e-04** | 3.86e-07 | 7.861e-05 | 204 | **UNSTABLE** |

252 of 828 pairs fall inside the binned domain (the jittered Sea
extends to x = ±28, far beyond the map's ±12 window); the rest take
zero increment per the frozen method.

**Geometry dependence, against 3186's symmetric-Sea values:**
F_JIT/F_SYM = **1.14× (β=0.05), 0.51× (0.10), 0.39× (0.20)**. The
prereg's §5 threshold (>2× or <0.5×) is met only at β = 0.20.
**Worker's pre-declared expectation — "differ by more than 2×" —
is SCORED NOT-CONFIRMED** as a general claim: the geometries differ
by roughly a factor of two to two-and-a-half at the upper βs, and
barely at all at the lowest. Fourth consecutive pre-declaration not
confirmed as stated; all four stand in the record.

## §2 — THE RULE DEFECT (the worker's own, found by its own output)

The frozen falsifier asks whether the two floors disagree by more
than 3×, **in either direction**. That conflates two opposite
situations:
- **3186 (β = 0.20): systematic ≫ statistical.** A real hazard — the
  class A/B split meant one scalar was hiding two physics.
- **3188 (all β): systematic ≪ statistical.** The six jittered seeds
  agree to four digits because the geometry is large and
  self-averaging. **That is the instrument behaving well**, and the
  rule condemns it.

**The corrected rule, stated for a future freeze and NOT applied
here:** flag UNSTABLE only when the SYSTEMATIC floor exceeds the
statistical floor by > 3× (one-directional); when the systematic
floor is far *smaller*, the statistical floor alone governs and the
comparator is usable if that floor is below the band width being
tested. **Applying that now would be rescuing a criterion after
seeing what it did to my numbers — the same move refused at 3155
(the coin-on-edge SATURATED reading) and at 3175 (endpoint
re-siting). The refusal is the point.**

## §3 — INADMISSIBLE arithmetic, printed and marked

Following the 3182 precedent for BLIND statistics — show the number,
mark it, attach no reading:
- β = 0.10: measured 9.14e-04 vs band [1.51e-04, 6.05e-04] → **3.02×
  above** → would read ABOVE-BAND. **INADMISSIBLE.**
- β = 0.20: measured 1.44e-03 vs band [1.61e-04, 6.43e-04] → **4.48×
  above** → would read ABOVE-BAND. **INADMISSIBLE.**
Had they been admissible the aggregate would have read
**ANOMALY-INVERTS** — the arms sitting ABOVE a valid comparator, the
opposite sign to DISP-I3's undershoot. **Not declared. Not adopted.**

## §4 — What the numbers do establish

1. **The dominant uncertainty is now identified and it is not
   geometry:** it is the archive map's own per-bin statistical error,
   which is **25–75% of F** at these βs. Geometry scatter is four
   orders of magnitude smaller. **Reducing it requires re-running
   2914 legs — engine work, not a re-read** — and that is the honest
   cost of a decisive comparator.
2. **The transfer assumption is now the second open item** (3187 §2):
   the a1 profile was measured in the symmetric Sea and applied to the
   jittered one. The ~2× geometry difference found here is consistent
   with transfer being imperfect, and cannot distinguish that from a
   genuine geometry effect.
3. **DISP-I3 remains in question and un-re-adjudicated**;
   COEFFICIENT-OVERPREDICTED remains SUSPENDED; the ledger, Candidate
   (B) at 79.5%, and item 1B are untouched.

## §5 — Honest state of S1

S1 asked whether the arms fail against a valid comparator. **After two
patches: a comparator now exists on the right geometry, and it is not
yet precise enough to judge the arms** — its own statistical floor is
comparable to the band it would define. The strategy's third outcome
("the conversion is too uncertain to compare at all") is the one
that fired, at least until the map is re-measured. **Nothing should
run on Kila6 on the strength of a comparison this patch declined to
make.**
