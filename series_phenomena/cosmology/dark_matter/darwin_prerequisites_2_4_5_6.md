# DARWIN RESTORATION — PREREQUISITES 2, 4, 5, 6 (Patch 2847)

**Filed 2026-07-27 against the panel's six prerequisites (2845 R3).
Items 1 (normalised source, 2843) and 3 (causal response law, 2846)
were supplied previously. This note addresses the remaining four.
**Worker does NOT declare the bound restored** — restoration is a
panel act, and §5 states what remains genuinely open.**

## Prerequisite 2 — Local continuity: SATISFIED IDENTICALLY

With the bound-charge/bound-current pair
**ρ_b = −∇·P** and **J_b = ∂P/∂t**:

> ∂ρ_b/∂t + ∇·J_b = −∂(∇·P)/∂t + ∇·(∂P/∂t) = **0**, identically,
> by equality of mixed partials.

Continuity is not an additional assumption — it is automatic once the
Sea's response is described by a polarization field, which is exactly
the description C23 supplies (poles displaced along the arriving
field). **Free charge:** CPs are conserved by the Moment rule, which
displaces them and neither creates nor destroys them (C19). Both
sectors satisfy continuity.

## Prerequisite 4 — The scalar–transverse combination in the reduced force

The force on a test charge is **F = q(E + u × B)** with u the test
charge's velocity. Eliminating the field:
- **E** carries the retarded scalar sector: O(1) Coulomb plus
  corrections;
- **u × B** carries the transverse sector, and since B ∝ v/c (2843:
  curl B = (1/ε₀c²)∂P/∂t), the magnetic term enters at
  **O(u·v/c²) = O(v²/c²)**.

**The magnetic contribution to the force is therefore second order by
construction** — it cannot produce an O(v/c) term at all. Any
first-order term could only come from the scalar sector's retardation
expansion, which prerequisite 5 addresses.

## Prerequisite 5 — Explicit O(v/c) cancellation: VERIFIED

For a uniformly moving charge the exact retarded (Liénard–Wiechert)
field is
**E = q(1−β²) r̂ / [r²(1−β²sin²θ)^{3/2}]**, with **r̂** to the
**instantaneous** position. Its fractional deviation from
instantaneous Coulomb, measured:

| v/c | θ = 90° | θ = 45° | θ = 0° | ratio to previous row |
|---|---|---|---|---|
| 0.200 | +0.020621 | −0.010463 | −0.040000 | — |
| 0.100 | +0.005038 | −0.002528 | −0.010000 | **4.093** |
| 0.050 | +0.001252 | −0.000627 | −0.002500 | **4.023** |
| 0.025 | +0.000313 | −0.000156 | −0.000625 | **4.006** |

**Halving v/c divides the deviation by ≈ 4, not by 2** (a first-order
term would give 2.0; second-order gives 4.0), converging on 4.000 as
β → 0. **Every O(v/c) term cancels; the leading deviation is
O(v²/c²), at all three angles, with the correct sign structure
(β²[(3/2)sin²θ − 1]).**

This is the cancellation the Darwin argument requires, exhibited
rather than asserted.

## Prerequisite 6 — The second-order coefficient C₂: DERIVED, worst case 1

From the Darwin interaction (q₁q₂/2c²r)[**v₁**·**v₂** +
(**v₁**·r̂)(**v₂**·r̂)] against Coulomb q₁q₂/r, the ratio is
½[**v̂₁**·**v̂₂** + (**v̂₁**·r̂)(**v̂₂**·r̂)]·(v²/c²):

| configuration | C₂ |
|---|---|
| parallel velocities, along the separation | **1.000** |
| parallel velocities, perpendicular to it | 0.500 |
| antiparallel, along the separation | **1.000** |
| mutually perpendicular | 0.000 |

> **C₂ ∈ [0, 1], worst case C₂ = 1.**

The 2838 estimate "C₂ = O(1), natural range 0.5–1" is confirmed and
tightened: **1 is a hard ceiling**, not a conservative guess.
Consequence for the bar: δ_mem ≤ 0.15 requires **v/c ≤ 0.387** at the
worst case.

## §5 — What remains genuinely open (stated so the panel need not find it)

**All six prerequisites now have supplied content**, but two carry
conditions the worker cannot discharge alone:

1. **Prerequisites 4–6 are electrodynamic results.** They follow once
   CPP's field sector *is* Maxwellian. 2843 established the source
   relation in tested geometries; S1's R1 amendment (adopted 5–0)
   explicitly left the **general** dynamical Maxwell–Ampère derivation
   conditional on the response law and continuity. Continuity is now
   supplied (prereq 2) and the response law is supplied (2846) — but
   the *general* derivation across arbitrary trajectories, with derived
   units and density normalisation for **P**, has not been performed.
2. **Prerequisite 3's route-3 branch carries a 1/Q suppression**, and
   Q's physical value remains unestablished (2846 §4). The
   conservative branch (route 1) needs no Q, but rests on C24's
   conservativity holding for the individual DP, not merely in total.

**Worker's reading:** the six prerequisites are met *conditionally on
CPP's field sector being Maxwellian in general*, which the panel
already flagged as the open item at R1. **The Darwin bound is
therefore restorable on the panel's judgement of that conditional —
not on any further calculation the worker can perform unilaterally.**

1A MET · 1B OPEN · Darwin bound WITHDRAWN-PENDING-CONSTITUTIVE-CLOSURE
· PR7 PARTIAL · six of seven · B7 holds.
