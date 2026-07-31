# B1 — LINEAR STABILITY OF THE COASTING SOLUTION. EXECUTED.

**Patch 2897. B1 was dispatched to the CONV-001 panel TWICE and returned
5–0 REASONED-UNVERIFIED both times: no seat has an execution environment.
It has been open since the SF-6 pin arc and is LINK 3 of CONJ-FP-1. This
is its first execution.**

---

## §1 — THE ANALYTIC CORE

Coasting map, from the CPP primitive d = (|SSV_net|/SSV_abs)·PSR with
v = d per Moment, and the round-trip mechanism SSV_net = D(v):

    v_{n+1} = μ · D(v_n)  ≡  f(v_n),      μ ≡ PSR/SSV_abs

Stability eigenvalue **λ = f′(v*) = μ·D′(v*)**:

| λ | behaviour | verdict |
|---|---|---|
| **= 1** | neutral — every v persists | **NEWTON I** |
| < 1 | attracting — unique preferred speed | Aristotelian; WRONG |
| > 1 | repelling — runaway | WRONG |

**If D is exactly linear** (D = kv): the fixed-point condition forces
μk = 1, and then λ = μk = **1 identically**. Newton I holds for *every* v
— the one-parameter coasting family of CONJ-FP-1 §2.

**If D carries curvature** (D = kv(1 − cv²)): fixed point at
cv*² = 1 − 1/(μk), and

    λ = μ·D′(v*) = μk(1 − 3cv*²) = **3 − 2μk**

Neutrality (λ = 1) then requires μk = 1 — which forces **v* = 0**. No
finite coasting speed exists.

> **NEWTON I REQUIRES THE DRIVE TO BE EXACTLY LINEAR IN v.** Any curvature
> destroys the coasting family. This is the sharp form of LINK 3.

## §2 — IS THE DRIVE EXACTLY LINEAR? CONVERGENCE-TESTED

Patch 2884 reported drive/β drifting from −15.955 to −15.923 (0.2%) and
did not determine whether that was physical or grid error.
`code/2897_b1_stability_convergence.py`:

| grid | β=0.01 | β=0.05 | β=0.10 | β=0.20 | **fractional spread** |
|---|---|---|---|---|---|
| 160×240 (2884) | −15.95484 | −15.94717 | −15.92318 | −15.82668 | **0.00803** |
| 320×480 | −15.65262 | −15.64510 | −15.62158 | −15.52696 | **0.00803** |
| 640×960 | −15.50459 | −15.49714 | −15.47384 | −15.38014 | **0.00803** |

**The absolute magnitude converges properly** (successive deltas +0.302,
+0.148 — halving, first-order convergence). **The fractional spread is
IDENTICAL to five decimals at every resolution.**

> **THE CURVATURE IS PHYSICAL, NOT NUMERICAL. THE DRIVE IS NOT EXACTLY
> LINEAR.**

**Functional form: quadratic in β.** Relative drop is 1.98×10⁻³ at
β = 0.10 and 8.03×10⁻³ at β = 0.20 — ratio **4.06**, i.e. β².

## §3 — THE CURVATURE COEFFICIENT IS A KINEMATIC INVARIANT

Fitting D/β = k(1 − cβ²) across deliberately varied model choices
(`code/2897_b1_curvature_robustness.py`):

| falloff m | r range | k | **c** |
|---|---|---|---|
| 2.0 | [1, 12] | −15.65 | **0.20129** |
| 2.0 | [1, 20] | −16.43 | **0.20129** |
| 2.0 | [2, 12] | −7.05 | **0.20129** |
| 2.0 | [0.5, 12] | −33.35 | **0.20129** |
| 1.0 | [1, 12] | −41.95 | **0.20129** |
| 3.0 | [1, 12] | −8.61 | **0.20129** |

**The amplitude k varies by a factor of 6. The curvature c does not move
in five decimals.** c is a property of the round-trip retardation
geometry — of the (c²−v²) denominator in the doubly-retarded solve — and
is independent of the interaction law and the integration domain.

## §4 — CONSEQUENCE WITH CONSTANT μ: CATASTROPHIC DRAG

Set μk = 1 (the marginality condition, LINK 2). Then

    v_{n+1} = v_n(1 − c v_n²)   ⟹   Δv = −c v³ per Moment

**Third-order drag.** At β = 10⁻³ with c = 0.201, the decay time is
β/|Δβ| ≈ 5×10⁶ Moments ≈ **10⁻³⁷ s**.

> **With a velocity-independent μ, the mechanism does not merely fail to
> give Newton I — it destroys all motion essentially instantaneously.**

## §5 — WHAT B1 ACTUALLY DELIVERS: A SHARP CONSISTENCY CONDITION

Newton I requires μ(v)·D(v) = v for all v. With D = kv(1 − cv²):

> **μ(v) = 1 / [k(1 − c β²)],  c = 0.201**

**This is not optional.** §4 shows a constant μ is excluded by ~37 orders
of magnitude.

**And it is testable against work the programme has already done.**
μ = PSR/SSV_abs, and the SR sector (SR-1, SR-2, SF-6) derives how substrate
quantities behave under motion. **If CPP's independently derived μ(v)
matches 1/(1 − 0.201β²), Newton I follows and this is a strong
zero-parameter consistency check across two sectors. If it does not match,
either the round-trip mechanism or this model of it is wrong.**

**For reference:** the relativistic form γ² = 1/(1 − β²) corresponds to
c = 1. **The required c is 0.201 — same sign, same functional form, five
times weaker.** The worker does NOT claim this is γ²-like in origin; the
comparison is offered because the SR sector is where the answer must come
from.

## §6 — STATUS OF LINK 3

**LINK 3 is no longer open in the vague form "is the coasting family
stable?"** It is now a specific, checkable requirement on μ(v), with a
numerical coefficient that is model-independent.

**Not closed.** Closing it requires the SR sector's μ(v), which this patch
does not compute.

**Caveat, stated rather than buried:** all of this is computed within the
continuum retardation model of Patch 2884, not on the substrate itself.
That model reproduces the Liénard–Wiechert null exactly (Patch 2884 §E.5),
which is its validation, but it is not the automaton. **c = 0.201 is a
property of that model. Whether the substrate reproduces it is untested.**

## §7 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds; Candidate
(B) 79.5%. G1 and P-A2-1 stand. Statics suspension per 2892 stands.
**CONJ-FP-1: Condition B closed (2895); Condition A open; LINK 2 open;
LINK 3 SHARPENED to the μ(v) condition above.**
