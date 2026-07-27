# PR4 ANALYTIC ROUTE — SCOPING PASS (Patch 2815)

**Filed 2026-07-26 per the 2814 audit's §5.1 recommendation. PR4's
frozen text (kinetic1_returns_adjudication §5) permits "a direct
registered Moment-rule automaton **— or an analytically equivalent
derivation from the explicit Moment transition law —**" demonstrating
that the uniform Sea's stationary marginal is energy-only and
Gibbsian. The automaton route is bounded (arc closure §2, L-2). This
pass scopes the analytic route. SCOPING ONLY — no PR4 verdict is
enacted here; enactment is panel business.**

## §1 — Result of the scoping: the analytic route is TRACTABLE, and it returns a NEGATIVE answer for the bare rule

**The decisive structural fact: the Moment rule conserves no energy
functional.** Measured along a deterministic trajectory (M = 12,
R = 3, N = 24, 120 Moments), the lattice-Coulomb Hamiltonian
H = Σ_{i<j} σ_iσ_j/d_min(i,j) — the same functional the A1
deliverable battery used — ranges over [−9.96, +9.16], a spread of
19.12 in units where typical configuration energies are O(5).
H is not conserved, not monotone, and not bounded to a shell.

**Why this settles PR4's question rather than merely answering part
of it.** A Gibbs measure is μ(x) ∝ e^{−βH(x)}: it is *defined
relative to a conserved energy*. Such a measure is stationary under
(i) dynamics that conserve H (microcanonical/ergodic route), or
(ii) dynamics coupled to a bath at temperature 1/β
(fluctuation–dissipation route). **The bare Moment rule provides
neither**: it conserves no H (measured above), and it contains no
bath — C24's fluctuation–dissipation cycle is a property of the
*completed* rule (arc inertia storing and returning energy), not of
the rule as currently specified. **PR4's question — "is the
stationary marginal energy-only and Gibbsian?" — is therefore
ill-posed for the bare rule: there is no candidate energy function
with respect to which the marginal could be Gibbsian.**

This is the analytic counterpart of AUTOMATON-1's empirical
NOT-GIBBS verdict, and it explains it: the automaton did not fail to
find a Gibbs measure through insufficient sampling or an unlucky
regime — no Gibbs measure exists to find.

## §2 — Hypotheses tested and NOT supported (recorded against the worker's interest)

Two structural hypotheses were advanced during this pass and both
FAILED their own tests. Recorded because a scoping pass that reports
only its successes is worthless.

- **H-CONTRACT (field forgetting):** predicted that
  Q_{t+1} = W ∗ (Q_t + inj) contracts all nonzero modes, making the
  map non-injective and its attractors measure-zero. **NOT
  SUPPORTED.** The relay kernel is probability-normalised
  (Ŵ(0) = 1) but max|Ŵ(k)| over k ≠ 0 measures to 1.000000 at
  display precision — the shell kernel admits non-decaying modes at
  zone-boundary wavevectors. Empirically, two runs with different
  initial fields and identical initial positions did **not**
  converge: |Q₁ − Q₂|_max persisted at ≈ 0.07–0.10 over 60 Moments
  and the position trajectories DIVERGED. The field does not forget;
  the dynamics is sensitive to it. The non-injectivity argument
  fails on this route.
- **H-FINITE (forced periodicity):** predicted that a finite state
  space forces eventual periodicity. **NOT APPLICABLE AS STATED.**
  CP positions are finite, but the field Q is real-valued, so the
  full state space is continuous; no exact recurrence appeared
  within 600 Moments. The observed low-period attractors (A1 fixed
  point, A2 period-4) are empirical facts about the regimes tested,
  not consequences of finiteness.
- **Co-location merging (Test C)** remains a valid non-injectivity
  mechanism on the physical (multiset) state space, but it is
  regime-dependent (it disappears at PSR ≫ spacing per the 2810
  diagnosis) and cannot carry a general argument.

**Net:** the negative PR4 answer rests on the energy result alone,
which is sufficient and does not depend on either failed hypothesis.

## §3 — What would make PR4 answerable

PR4 becomes well-posed exactly when the rule acquires a conserved
energy functional. In the founder's own commitments that is C23
(inertia stored in the Sea's arc configuration) plus C24
(conservative two-channel fluctuation–dissipation cycle): kinetic
energy stored in DP arc rotation, returned on discharge, with
KE + PE conserved. **The blocker is therefore not computing power
alone.** It is a specification: the arc dynamics must be stated
precisely enough that (a) an energy functional can be written down
and (b) its conservation can be checked. Compute is the *second*
obstacle; specification is the first.

## §4 — Consequence for the release chain (stated, not enacted)

**PR4 as frozen may be unsatisfiable by ANY route — automaton or
analytic — until the C23/C24 completion is specified quantitatively.**
This is a materially different statement from "PR4 awaits more
compute," and it is the panel's to weigh. Three dispositions are
available to them, none of which the worker may choose:
1. **Hold PR4 as frozen** — promotion waits on the C23/C24
   specification and its verification. Honest; possibly a long wait.
2. **Amend PR4** by panel motion (its text is amendable only so) —
   e.g. to require the *analytic demonstration that no energy-only
   Gibbsian marginal exists for the bare rule*, plus a stated
   condition on the completed rule, converting an unmeetable
   requirement into a met one plus a named open condition carried
   honestly in the papers (the DM-2 precedent: papers may carry an
   open condition; a KILL blocks, an open condition does not).
3. **Rule PR4 inapplicable** to a candidate whose screening claims
   rest on Metropolis/HNC — noting PR4's own sentence that
   "Metropolis or HNC concordance cannot satisfy PR4," which was
   written precisely to prevent that move.

**Worker recommendation: option 2**, on the grounds that the frozen
text's purpose — to prevent unearned reliance on the Metropolis
machinery — is *served*, not evaded, by an analytic demonstration
that the bare rule cannot supply Gibbs statistics: it tells the
consumer exactly how much the Metropolis results are worth and what
would license them. But this is the panel's motion to make, and the
worker's recommendation is flagged as such.

## §5 — Cost

The scoping pass cost one session. A full analytic write-up (the
energy non-conservation theorem stated cleanly, with the
regime-independence check the empirical measurement above does not
yet supply) is a small paper's worth of work — days, not campaigns —
and would be the artifact submitted under disposition 2.
