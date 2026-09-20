# The Magnitude Half — ⟨b⟩ = (v/c)·cos θ, Derived

**Patch:** 4158. **Lane:** EW. **Session:** 234.
**Discharges:** TODO-4157-CHIRMAG (partially — see §5).
**Verify:** `series_standard_model/code/4158_chirality_magnitude.py`.

---

## 1. The construction

b is a **bit** — sign(A·V), two-valued by A1′. A CP's SSV_disp at any Moment is its **ZBW
circulation** (magnitude ~ c) **plus its drift** (magnitude v):

  **V = c·û(t) + v**,  **b = sign(A·V)**

So b is not constant over a ZBW cycle. It flips whenever the circulation carries A·V through zero,
and the drift **biases the fraction of the cycle spent on each sign**. The observable is that
time-average ⟨b⟩. **Nothing here is free** — the only input is the measure of û on the sphere, i.e.
the ZBW's geometry.

## 2. The result

| β = v/c | isotropic û | circulation ⊥ A | circulation ∋ A | measured |
|---|---|---|---|---|
| 0.05 | 0.0488 | 1.0000 | 0.0322 | 0.05 |
| 0.20 | 0.1998 | 1.0000 | 0.1273 | 0.20 |
| 0.50 | 0.4998 | 1.0000 | 0.3340 | 0.50 |
| 0.80 | 0.8003 | 1.0000 | 0.5912 | 0.80 |
| 0.95 | 0.9500 | 1.0000 | 0.7975 | 0.95 |

**An isotropic ZBW measure gives ⟨b⟩ = v/c exactly, at every speed** — the textbook longitudinal
polarisation, measured since Frauenfelder 1957.

The reason is elementary once seen: for û uniform on the sphere, **A·û is uniform on [−1, 1]**
(Archimedes' hat-box theorem), so

  ⟨b⟩ = P(A·û > −β) − P(A·û < −β) = (1+β)/2 − (1−β)/2 = **β**.

**And the angular law follows with it.** At β = 0.5, ⟨b⟩ tracks β·cos θ to within sampling error at
every angle tested: **⟨b⟩ = (v/c)·cos θ**, the measured V−A angular dependence, with no fitted
parameter.

**The two single-plane alternatives are excluded by the data.** A circulation normal to the spin
axis gives sign(β) — maximal at all speeds, flatly contradicting measurement. One containing the
spin axis gives the arcsine law (2/π)arcsin β, also wrong.

## 3. Maximality — the original question, answered

Why 100% V−A rather than partial chirality? **Because b is a bit.** B3 makes the response linear in
b, and b takes only ±1, so the coupling has no way to be partial — there is no intermediate value to
couple to. A continuous helicity variable would give partial chirality; a two-valued one cannot.

**The coupling is maximal; the observation is diluted.** The measured asymmetry is (v/c)cos θ not
because the coupling weakens at low speed, but because a slow particle's ZBW spends nearly half the
cycle on each sign. As v → c the drift dominates the circulation and ⟨b⟩ → 1 (checked: 0.9990 at
β = 0.999). **That is the same massive/massless split Patch 4143 found** — helicity frame-dependent
for a massive particle, invariant for a massless one — arriving here as a magnitude rather than a
classification.

## 4. What this is worth

THEO-CHIR-1 (4157) said **when** a parity-odd effect is allowed. This says **how big** it is, and
gets the measured law. Between them the two halves are the theorem the founder asked for at 4157.

It is also the session's first genuinely **new derived number**: everything else in patches
4132–4157 was correction, classification, or a selection rule.

## 5. What is derived, what is assumed — the honest split

**Derived:** the form **(v/c)·cos θ**, exactly, from two inputs already in the corpus — b is a sign
(A1′) and the response is linear in b (B3) — plus one geometric input.

**Assumed:** that the ZBW measure is **isotropic on the sphere**. The χ draft axiom says the ZBW is a
*double* rotation — circulation in two orthogonal planes — and two orthogonal circulations at
incommensurate frequencies do sweep the sphere, but **I have not shown they sweep it uniformly.**
That is the gap and it is real.

**But the gap cuts in the corpus's favour**, which is worth stating precisely: both single-plane
alternatives are **excluded by the measured law**, so the (v/c)cos θ result is *evidence for* the χ
draft's double rotation and *against* a single circulation. Filed as **TODO-4158-ZBWMEASURE** —
show that the double rotation's orbit is equidistributed on the sphere (a Weyl equidistribution
argument, if the two frequencies are incommensurate).

**Not derived:** the **sign**. Whether it is −v/c (left-handed) or +v/c is set by the
polarity-to-duality assignment in the χ draft, not by anything here.

## 6. PD-008 — the convenient branch, marked

The convenient branch was to report §2 and §3 and stop: a clean derivation of the measured V−A law
with no free parameters, which is the strongest single result of the session. §5 is the cost — the
isotropy is an assumption, not a theorem, and the whole derivation rests on it. I have also declined
to call the exclusion of the single-plane measures a *confirmation* of the double rotation; it is
evidence, which is weaker, and the equidistribution still has to be shown.

## 7. Status

TODO-4157-CHIRMAG discharged as to form, open as to the isotropy premise.
**OPEN-FP-SF-2-CHIR** should be reread against this: its "100% V−A at the massless helicity limit"
is §3 plus β → 1. No verdict moved. χ₄ provisionally adopted. **F5 remains the blocker.**
