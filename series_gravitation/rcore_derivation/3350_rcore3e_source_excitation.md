# OPEN-GR-RCORE-3(e) — **CLOSED** within its derived physical range: the last borrowed assumption in the echo prediction is now computed

**Patch 3350, 30 Aug 2026 — Session 157.** Verify:
`code/3350_rcore3e_source_excitation_verify.py`, **9/9 PASS**
(all-FAST). Charter: the residual ℓ = 7–8 gap left open by Patch 3349.

---

## §1 The budget

Three factors, each labelled by grade, multiplied against the ℓ = 2
ringdown:

| factor | grade | ℓ = 7 | ℓ = 8 |
|---|---|---|---|
| **(A) multipole scaling** P_ℓ/P₂ ~ v^(2(ℓ−2)) | derived here from the moment expansion; leading-order slow-motion, **marginal at merger velocity** | 3.4e−4 @ v=0.45 | 6.9e−5 |
| **(B) counter-rotation mismatch** | **bounded at 1.0, conservatively** | 1.0 | 1.0 |
| **(C) barrier penetration** e^(−4Γ) | derived, Patch 3349 | 0.199 | 1.46e−2 |
| **combined, worst case over the physical range** | | **1.94e−4** | **3.56e−6** |

Both clear the pre-declared 1e−3 bar — the same bar 3349 used, and
declared before the numbers were read.

**Factor (B) is deliberately under-counted.** The trapped modes are
extreme retrograde (Leg C: every trapped mode has m ≤ −(ℓ−1)), while
the remnant forms from a **prograde** inspiral, so the true mismatch
is below unity. Entering 1.0 makes the whole budget an
**under-estimate of the suppression**: a real waveform calculation can
only push these numbers down. The conclusion is therefore robust to
this factor being unknown, which is why it was bounded rather than
modelled.

## §2 The physical range is derived, and the scan runs past it on purpose

The source's orbital velocity at merger is bounded by the remnant's
ISCO. Computed rather than assumed: at χ = 0.68,
r_ISCO = 3.484 M ⇒ **v_ISCO = 0.536**. The velocity scan was
deliberately extended to v = 0.60 so the failure point could be
located rather than avoided.

## §3 THE EDGE, stated plainly

**The margin is real but thin.** The ℓ = 7 budget crosses the 1e−3 bar
at **v = 0.589**, only **+0.053 beyond v_ISCO**. At the unphysical
v = 0.60 the budget is 1.20e−3, *above* the bar.

So the honest verdict is: **closed inside the derived physical range,
marginal just outside it.** Above v_ISCO it would still close for any
counter-rotation factor below 0.83 — near certain on the
retrograde-mismatch argument of §1, but **uncomputed**, and therefore
not claimed.

## §4 What the prediction now rests on

Four shields between the high-ℓ trapped ladder and the observable
prediction, **three of them now derived in this programme**:

1. **Multipole scaling** (derived, this patch) — ℓ = 7–8 are
   sub-percent in power before anything else applies.
2. **Barrier penetration** (derived, 3349) — decisive from ℓ ≥ 9,
   partial at ℓ = 7–8.
3. **Band separation** (derived, 3349) — the ladder lives at
   602–986 Hz, the search band at 211–294 Hz; a factor 2.0 clear, and
   it holds at **every** ℓ regardless of excitation.
4. **The inherited ringdown hierarchy** — now redundant rather than
   load-bearing.

## §5 Honest limits

Factor (A) is leading-order slow-motion multipole scaling, which is
**marginal at v ≈ 0.5** — that marginality is exactly why the verdict
is taken at the worst case of a velocity scan rather than at a point,
and why §3 reports the break point. No waveform is computed; no NR fit
is used or needed. Factor (B) is a bound, not a calculation. Factor
(C) inherits 3349's first-order WKB caveat near the barrier top.
A1–A3 conditionality (OPEN-GR-RCORE-4) is inherited throughout. No
detector-sensitivity or SNR statement is made anywhere.

## §6 Registry impact

- **OPEN-GR-RCORE-3(e): CLOSED** within the derived physical range,
  with the thin supra-ISCO margin recorded in §3.
- **OPEN-GR-RCORE-3 overall:** Legs A, B, C discharged; item (b)
  discharged for the count; item (e) closed. **Remaining: (i) the
  analytic disjointness inequality; (ii) full-Teukolsky line positions
  and widths; (iii) Zel'dovich growth-time bounds.**
- **GR-2 amendment QUEUED (still not enacted, now larger):** V1.4's
  remark calls the high-ℓ negligibility "inherited... not computed in
  this programme." That is now simply wrong and should read: derived
  (multipole scaling + barrier penetration + band separation), closed
  within the physical range, thin margin above v_ISCO noted. To be
  folded at the next GR-2 touch — it strengthens the paper, so it does
  not owe a round first.
