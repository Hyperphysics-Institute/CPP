# OP-SS-13: Quantitative ZBW Mechanism for $\delta = 1/3$ Charge Screening

**Priority:** MEDIUM
**Status:** OPEN — physical picture clear, quantitative calculation absent
**Series:** SS-1, SM-1
**Registered:** 29 March 2026
**Source:** Session discussion 29 March 2026; mechanism-SS-1.md Steps 28–30
**Depends on:** OP-SS-9 (SOLVED — the C₃ proof is the authoritative result)

---

## Statement

The C₃ geometric proof (SM-1 Theorem 1, OP-SS-9 — now solved) establishes
$\delta = 1/3$ exactly from the cage topology. The ZBW orbital mechanism
provides a *physical* account of how the screening arises: the inner
orbital qCP spends an increased fraction of its time in the tightly-bound
$1/r^3$ dipole configuration due to relativistic time dilation at small
orbital radius, partially neutralising the central qCP charge.

**What needs to be proved:** Show from the ZBW orbital dynamics that the
fraction of time spent in the $1/r^3$ configuration is **exactly $1/3$**,
in quantitative agreement with the C₃ topological proof.

This is an independent physical derivation that should converge to the
same result. If it does, the two routes (topological and mechanical)
mutually confirm each other. If they don't, one of them is wrong — and
the discrepancy would identify a gap in the CPP framework.

---

## The Physical Picture

Every quark carries an inner orbital ZBW dipole pair oscillating at
twice the frequency of the outer orbital (2:1 frequency ratio, same
as the electron's spin-generating orbital). The inner orbital executes
a tight orbit at small radius around the central qCP.

At small orbital radius $r_{\rm in}$, the centripetal acceleration
$a = v^2/r_{\rm in}$ is very large — of order $v^2/r_{\rm in} \sim c^2/r_{\rm in}$.
By the equivalence principle (or its CPP analog via SSV compression),
this large centripetal acceleration is equivalent to a strong local
gravitational field. The inner orbital DP therefore experiences
enhanced time dilation: its clock runs slow relative to the outer
region.

The effect on the dipole configuration: the inner orbital DP spends
more time per oscillation cycle in the tightly-bound $1/r^3$ phase
(where it is closest to the central qCP and most strongly attracted)
than in the $1/r^2$ phase (where it is at larger separation and
less strongly attracted). This asymmetric time distribution means
the inner orbital effectively screens more charge per cycle than it
would in a symmetric oscillation.

The screening fraction $\delta$ equals the time-averaged fraction
of the oscillation cycle spent in the $1/r^3$ configuration.

---

## What Needs to Be Computed

1. **The orbital trajectory:** Solve the equation of motion for the
   inner orbital DP in the combined SSV field of the central qCP
   (Coulomb-like at large $r$, transitioning to $1/r^3$ at the ZBW
   inner radius). This requires the CPP analog of the Dirac equation
   for the orbital — or equivalently, the ZBW Schrödinger equation
   in the central field.

2. **The time fraction:** Compute
   $$f_{1/r^3} = \frac{\tau_{1/r^3}}{\tau_{\rm total}}$$
   where $\tau_{1/r^3}$ is the time spent per oscillation cycle
   at separations where the $1/r^3$ term dominates, and $\tau_{\rm total}$
   is the full oscillation period.

3. **The charge screening:** Identify the relationship
   $\delta = f_{1/r^3}$ and verify that the computed value equals
   $1/3$.

---

## Key Intermediate Result to Establish

The C₃ proof gives $\delta = 1/3$ unconditionally. For the ZBW
mechanism to agree, the calculation must produce:

$$f_{1/r^3} = \frac{1}{3}$$

This is equivalent to saying that the inner orbital spends 1/3 of
its time in the inner ($1/r^3$) phase and 2/3 of its time in the
outer ($1/r^2$) phase — a 1:2 time ratio between the two phases.

The 2:1 ZBW inner-to-outer frequency ratio may be directly relevant
here: if the inner orbital executes 2 oscillations for every 1 outer
oscillation, the time spent at the inner turning point vs the outer
turning point would have a ratio set by the frequency ratio. Whether
this gives 1:2 time allocation (and therefore $\delta = 1/3$) depends
on the specific orbit shape.

---

## Approach

The most direct route:

1. Model the inner orbital as a particle in a 1D effective potential
   combining the SSV Coulomb term ($\sim 1/r$) and the hard-wall
   confinement at $r_{\rm conf}$.

2. Use WKB approximation for the oscillation: the time spent in
   each phase is proportional to the classical period in that
   potential region.

3. Compute the ratio $\tau_{1/r^3} : \tau_{1/r^2}$ and verify it
   equals 1:2.

4. Identify the CPP parameters (sea\_strength, ZBW frequency ratio,
   orbital radius) that set this ratio, and confirm they are
   consistent with the values derived in SS-1 and SM-1.

---

## Why This Matters Even Though OP-SS-9 Is Solved

The C₃ proof is the authoritative and exact result. But a theory
that has only a topological proof for its most important charge
prediction, without a mechanical account, is incomplete. The ZBW
mechanism is what makes the topology physically intelligible:
it explains *why* the screening is 1/3 in terms of
orbital dynamics that a physicist can visualise and test.

A successful ZBW derivation would also:
- Confirm the 2:1 ZBW frequency ratio is physically consistent
  with $\delta = 1/3$
- Connect the strong-sector charge screening to the SR-1 ZBW
  treatment (the orbital dynamics are the same mechanism)
- Provide a derivation pathway for $\delta$ in regimes where
  C₃ symmetry might be broken (e.g., at very high temperature
  or in exotic cage configurations)

---

## Feeds Into

- OP-SS-1 (quark mass formula — the ZBW orbital is part of the
  mass-generating mechanism)
- Philosophy-SS-1.md §3 (the relationship between topological
  and mechanical proofs)
- Candidate for a short companion paper or appendix to SM-1
