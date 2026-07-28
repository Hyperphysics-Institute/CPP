# CONV-001 — DARWIN RESTORATION MOTION (Patch 2844)

**Five questions (R1–R5). The worker withdrew the second-order bound
at 2840 on a frozen test outcome, then derived at 2843 the very input
that test was meant to supply. **The worker declines to restore its
own withdrawal.** This motion asks the panel to rule.**

## §1 — The sequence, stated so the conflict is visible

1. **2838** — Darwin argument: for a field-mediated charge system the
   first order in v/c cancels by gauge structure, so
   δ_mem ≤ C₂(v/c)² with C₂ = O(1). **Conditional on CPP reproducing
   the transverse sector at the correct order.**
2. **2839/2840** — the worker's own transverse test returned
   TRANSVERSE-FAIL. Frozen consequence enacted: **second-order bound
   WITHDRAWN**; 1B reverts to δ_mem ≤ C_mem(v/c), ambient bar
   v/c ≲ 0.15.
3. **2841** — scoping correction: the test used a *static* jellium
   background, so it contained **no Sea, no DP poles, no arcs**. It
   measured the bare relay's scalar sector alone. Verdict valid for
   the relay; **not** a refutation of C23. Withdrawal held anyway.
4. **2842** — the magnetic curl derived: ω_arc = (v × r̂)/r matches
   Biot–Savart direction to **0.00°** at five geometries, purely
   azimuthal (dot 1.000000 at six azimuths), vanishing on-axis,
   reversing across it. Radial law mismatched (1/r vs 1/r²).
5. **2843** — mismatch resolved: ω carries **no charge**, so it never
   could have been B. **B is SOURCED by the Sea's response:
   curl B = (1/ε₀c²)∂P/∂t**, verified exact (0.000°, ratio 1.00000)
   at five geometries. ∂P/∂t = **arc** (transverse) + **stretch**
   (longitudinal, along r̂); the stretch vanishes identically at
   closest approach, which is why the founder's arc-only picture felt
   complete.

**The conflict:** step 5 supplies exactly the normalisation step 1's
conditional required, hours after step 2 removed the bound. Restoring
it on the worker's own derivation, after two prior overclaims required
this panel to adjudicate to a minority against the worker (2817 M1;
2837 K3), would be indistinguishable from motivated reasoning **even
if correct**.

## §2 — Questions

**R1.** Accept the normalisation resolution — B is not the Sea's
response but what it sources, curl B = (1/ε₀c²)∂P/∂t, with ∂P/∂t
decomposing into arc + stretch?

**R2.** Accept the proposed C23 refinement — *"the arc is the
transverse part of the Sea response that SOURCES the magnetic
field,"* replacing *"the arcing motion IS the magnetic field"*?
(Founder ruling also required; this asks the panel's view.)

**R3.** **Does R1 discharge 2838's conditional, and should the
second-order (Darwin) bound be RESTORED?** If yes, 1B's requirement
returns to δ_mem ≤ C₂(v/c)² and the ambient bar relaxes from
v/c ≲ 0.15 to ≈ 0.3.

**R4.** If R3 is yes: does 1B then close on (a) fixing C₂ from the
normalised structure and (b) an ambient-Sea v/c bound — with **no
FEM** and **no further transverse measurement**?

**R5 — objection the worker raises against its own case.** The
2843 derivation assumes the DP polarisation is **instantaneous and
linear in E**. CPP has not established either: C23 gives the
mechanism qualitatively, and the relay is strictly retarded, so a
polarisation that lags its driving field would alter ∂P/∂t and could
reintroduce a first-order term. **Should R3 be conditioned on
establishing the polarisation response law?** The worker judges this
the strongest available objection to its own derivation and would
rather the panel weigh it than discover it later.

## §3 — Standing

Nothing enacted. 1A MET · 1B OPEN at δ_mem ≤ C_mem(v/c) · PR7 PARTIAL
· six of seven · B7 holds. A yes on R3 does not by itself close 1B;
it changes which bound 1B must meet.

## §4 — Execution integrity

**Withheld challenge key** (2837 rule: computable from committed
artifacts, value appearing in NO committed document and NO linked
document — the flaw that voided the 2832 key): any seat claiming
execution should report **the TOTAL number of k-vectors returned by
`make_k(L, nmax=5)`** in `code/2829_pr3r2_founder_run_v2c.py`. The
worker has **deliberately not computed this value** and will compute
it only on a seat's return. Non-executing seats declare
REASONED-UNVERIFIED — no penalty; four consecutive clean rounds.
