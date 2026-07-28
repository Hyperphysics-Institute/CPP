# THE AMBIENT SEA v/c BOUND — SCOPING (Patch 2851)

**Filed 2026-07-27. The last gap in 1B is one number: the ambient DP
Sea's centre-of-mass v/c, which must clear the OPERATIVE bar
v/c ≤ 0.15 (2850). This note scopes what would establish it, reports
one derivation attempt, and reports why that attempt CANNOT be used.
No bound is asserted.**

## §1 — Which velocity, precisely

**Not the CP velocity.** A bonded CP cycles through ZBW at speeds that
may approach c. **The quantity 1B needs is the DP CENTRE's
translational speed** — the *slow* variable, per the 2846 derivation
where ω = v/d_DP is the drive frequency and the DP's internal ZBW is
ω₀ = c/d_DP. Confusing the two would substitute a large number for a
small one, in the direction that fails the bar. **This distinction is
the first thing any bound must fix.**

## §2 — A derivation attempt, and why it FAILS its own test

CPP's primitive gives v/c ≡ |SSV_net|/SSV_abs (C20). For N
uncorrelated contributions within a PSR, the vector sum grows as √N
while the scalar sum grows as N, so

> **v/c ~ 1/√N** — clearing 0.15 for **N > 44** per PSR.

Since the physical Sea's Planck sphere contains astronomically many
DPs, this would clear the bar by many orders of magnitude and close
1B on the spot.

**IT DOES NOT SURVIVE ITS OWN CHECK.** Against the AUTOMATON
measurements (fill 1/8):

| PSR occupancy | measured ratio | 1/√N prediction |
|---|---|---|
| 13.4 | 0.154 | 0.273 |
| 160.1 | **0.364** | 0.079 |

**The measured ratio RISES with occupancy; the uncorrelated scaling
says it must FALL.** The prediction is wrong in *direction*, not
merely magnitude — a factor-4.6 discrepancy at the denser point.

**Two readings, and the worker cannot distinguish them:**
(a) the AUTOMATON values are regime artifacts (Patch 2810 established
exactly this for PSR/spacing ≈ 1.5, and 2843's L-1 forbids using them
for physical inference), so the scaling may hold in the real Sea; or
(b) the Sea is strongly **correlated** — bonded pairs, not
independent contributions — so uncorrelated statistics never applied
and the scaling is simply wrong physics.

**Reading (b) is the more likely.** C26 commits the Sea to *dedicated
bonded pairs*, which is the opposite of the independence the √N
argument assumes; a CP's SSV_net is dominated by its own partner, not
by a random sum. **The derivation was built on a premise the framework
explicitly denies.** It is recorded here as a failed attempt so that
no future session re-derives it and stops at the flattering step.

## §3 — What would actually establish the bound (three routes, none executed)

1. **Equipartition route.** If the Sea has a temperature θ and the DP
   centre an effective inertial mass, v_centre/c follows from
   ½m⟨v²⟩ ~ θ. **Blocked:** the arc-inertia mass is exactly what
   PR4-COMPLETED's C23/C24 specification does not supply.
2. **Correlated-Sea derivation.** Compute ⟨|SSV_net|/SSV_abs⟩ for the
   *bonded* configuration rather than the uncorrelated one — the
   partner's dominant contribution largely cancels at superposition,
   leaving a residual whose size is the answer. Analytic, plausibly
   tractable, and **the recommended next attempt.**
3. **Direct measurement at honest scale.** Measure the DP-centre drift
   in a Sea with PSR ≫ spacing. **Blocked** by the same FEM boundary as
   OPEN-C23-TRANSVERSE-VALIDATION.

## §4 — The structural fact worth stating

**All three remaining obstacles now sit at or behind the same wall:**
- **PR4-COMPLETED** (OPEN-PR4-C23C24) — needs the C23/C24
  quantitative specification;
- **OPEN-C23-TRANSVERSE-VALIDATION** — needs a dynamically responding
  Sea;
- **1B's ambient bound**, via routes 1 and 3 — needs the same.

**Route 2 is the only path that does not run into that wall**, which
makes it the single highest-value next artifact. If route 2 fails, the
honest conclusion is that PR7 and PR4 are one obstacle wearing two
names, and the programme's remaining work is the arc-inertia
specification the founder has already identified as FEM-class.

## §5 — Standing

Nothing asserted. 1A MET · CPP-DARWIN RESTORED-CONDITIONAL (conditioned
on transverse validation) · 1B OPEN, operative bar v/c ≤ 0.15 · PR7
PARTIAL · six of seven · B7 holds.
