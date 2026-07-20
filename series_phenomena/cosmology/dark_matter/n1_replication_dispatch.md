# N1 hostile-replication dispatch (spine item 5): two seats, spec-only, independent implementations — the packet

**Patch 2595, 20 July 2026. Status: PACKET BUILT; dispatch on the founder's paste. Trigger:
the 2590-accepted Grok condition (independent implementation before promotion-adjacent use);
placement per the 2593-registered recommendation, founder-ratified this session. Seats:
ChatGPT and DeepSeek, in parallel, separate sessions, no cross-visibility. Channel-echo
protocol applies (prefix each returned paste "Seat N response:"). Optional third leg on
return: Isak executes one seat's returned code on independent hardware.**

**Founder instructions:** after pushing this patch, paste the block below verbatim to each of
the two seats in separate sessions. Do not identify the seat. Return each response prefixed
by its channel. The seats' returned CODE is part of the deliverable (for the hardware leg).

---

```
You are performing an INDEPENDENT REPLICATION of a registered computational claim from a
pre-registered research programme (Conscious Point Physics, dark-matter sector). You are
given the specification ONLY — no reference code, no expected numeric values beyond gate
definitions. Write your own implementation from scratch, run it, and report your numbers.
The claim's direction is known to you (that is normal for replication); the evidentiary
value lives entirely in the independence of your implementation.

THE CLAIM UNDER REPLICATION: a 4-particle "square" configuration (specified below) is
dynamically stable — it holds together, with bounded internal motion, when every particle
moves freely under the specified forces with no external pinning.

SPECIFICATION (complete; SI-free natural units: energies MeV, lengths fm, velocities in
units of c, time in fm/c; hbar*c = 197.3 MeV*fm):

1. PARTICLES: 4 point particles ("qCPs"), each of mass m = 132 MeV/c^2, carrying charges
   q = (+1, -1, +1, -1) respectively.

2. GEOMETRY (initial positions, at rest): a square of side D = 1.15 fm in the z = 0 plane,
   corners at (+D/2, +D/2, 0), (-D/2, +D/2, 0), (-D/2, -D/2, 0), (+D/2, -D/2, 0), with the
   charges assigned in the order listed (adjacent corners carry opposite charges).

3. FORCES (pairwise, between every pair i,j):
   (a) ELECTRIC-LIKE (soft-core Coulomb): U_e(r) = w^2 * q_i * q_j * 197.3 / sqrt(r^2 + a^2)
       with w^2 = 5/(8*phi) where phi = (1+sqrt(5))/2 (so w^2 = 0.38627124...; corrected
       Patch 2597 -- an earlier parenthetical carried a transcription error; the formula
       was and remains authoritative), and softening
       length a = 197.3/264 = 0.7473 fm. Force = -dU_e/dr along the pair vector.
   (b) STRONG (Morse, charge-INDEPENDENT, acts between every qCP pair):
       U_s(r) = E * [ (1 - exp(-beta*(r - D)))^2 - 1 ]
       with E = w^2 * 197.3 / D = 66.25 MeV, D = 1.15 fm, and TWO width cases to run
       separately: beta*D = 2 (soft) and beta*D = 4 (steep). Force = -dU_s/dr.

4. DYNAMICS: plain Newtonian point dynamics, semi-implicit (symplectic) Euler:
       V <- V + (F_total/m)*dt   then   X <- X + V*dt
   No damping, no thermostat, no constraint. Time step: run all three of
   dt = tau/200, tau/100, tau/50 where tau = 2*pi*197.3/264 = 4.696 fm/c.
   Total duration: T = 60*tau (~281.8 fm/c).

5. GATE (run FIRST; report before the claim; TWO cells per beta case as of the Patch
   2597 strengthening -- (a) at r_eq, (b) starting at separation 1.1*r_eq, same
   classifier, must remain bounded): two particles only, charges (+1, -1), masses
   as above, both force terms active, placed at rest at the separation r_eq that minimizes
   U_e + U_s (find it numerically; report your r_eq for each beta case — you should find
   it near 1.07-1.13 fm). Over the final 25% of the run, the pair's RMS distance from its
   centroid must stay within [0.5, 2.0] x its initial value, with no particle exceeding
   3x the initial maximum centroid distance. Report HOLD or otherwise, per dt, per beta.
   Also report total energy (KE + U_e + U_s) drift over the run at each dt.

6. THE CLAIM'S TEST: the 4-particle square, at rest at the specified geometry, all forces
   active, no pinning. Same classifier as the gate (final-25% RMS radius within [0.5, 2.0]
   of initial; max centroid distance < 3x initial max). Run: both beta cases x all three
   dt = 6 cells. Report per cell: verdict (HOLD / DISPERSE [radius grows past bands] /
   COLLAPSE [radius shrinks below 0.5x]), the final-window mean RMS radius ratio, and the
   max-distance ratio.

7. ROBUSTNESS SPOT-CHECK (one cell): displace every particle by an independent random
   vector of magnitude 0.05*D (any seed; report it), beta*D = 4, dt = tau/100. Report the
   verdict and ratios.

RESPOND WITH: (i) your r_eq values and gate results per cell with energy drifts; (ii) the
six claim cells with verdicts and both ratios; (iii) the robustness cell; (iv) your
complete runnable code; (v) anything in this specification you found ambiguous or had to
decide yourself — list every such decision explicitly (your decisions are data for us).
```

---

## Consolidation contract (frozen now)

Replication SUCCEEDS iff both seats independently report: the gate HOLD at every cell with
dt-convergent energy drift; the six claim cells HOLD; ratios within [0.5, 2.0] (their
absolute values need not match ours — their instruments lack our choreography layer, so
their bounded-motion bands are the claim's core, not our R = 0.78–0.86). Divergence between
seats, or any non-HOLD, routes to a defect hunt on BOTH sides (theirs and ours) with no
presumption. The seats' ambiguity lists (item v) are first-class deliverables — every
decision they had to make is a hole in our specification, and holes in specifications are
where irreproducibility lives. On success + the optional Isak hardware leg: spine item 5
CLEARS and the win's promotion-adjacent fence lifts per 2590.

## Bookkeeping

79.5% untouched. This dispatch shares nothing with N2-A but the calendar.
