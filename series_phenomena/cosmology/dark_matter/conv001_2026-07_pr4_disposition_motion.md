# CONV-001 — PR4 DISPOSITION MOTION (Patch 2816)

**A motion, not a results packet. The worker has found that a FROZEN
promotion criterion may be unmeetable by any route, and the criterion
sits on the founder's prime-goal path. Only the panel may amend
PR1–PR7 (kinetic1_returns_adjudication §5: "amendable only through a
new panel motion"). The worker therefore brings the finding and the
options, and explicitly declines to choose among them.**

## §1 — The finding (source: `pr4_analytic_route_scoping.md`, Patch 2815)

PR4's frozen text permits either a Moment-rule automaton **or an
analytically equivalent derivation from the explicit Moment
transition law**. Both routes are now characterised:

- **Automaton route: BOUNDED.** AUTOMATON-1 returned NOT-GIBBS 3/3 R.
  AUTOMATON-2 closed at the FEM boundary; its own limitation L-2
  (ratified 5–0 at W5') bars citing its Maxwell–Boltzmann result for
  PR4.
- **Analytic route: TRACTABLE, ANSWER NEGATIVE.** The bare Moment
  rule **conserves no energy functional** — measured along a
  deterministic trajectory, the lattice-Coulomb H ranges
  [−9.96, +9.16] (spread 19.12) where typical configuration energies
  are O(5). A Gibbs measure is *defined relative to a conserved
  energy* and is stationary under H-conserving dynamics or under
  bath coupling; the bare rule supplies neither (C24's
  fluctuation–dissipation cycle belongs to the *completed* rule, not
  the specified one). **PR4's question is therefore ill-posed for the
  bare rule: no candidate energy exists for a marginal to be
  Gibbsian in.**

This upgrades A1's empirical NOT-GIBBS from "we looked and did not
find" to "there was nothing to find."

**Worker-side failures disclosed (same-font):** two structural
hypotheses advanced during the scoping FAILED their own tests —
H-CONTRACT (the relay kernel has non-decaying zone-boundary modes;
two runs with different initial fields DIVERGED rather than merged)
and H-FINITE (the field is real-valued, so the state space is not
finite). The negative answer rests on the energy result alone and
requires neither.

## §2 — The consequence

PR4 becomes answerable exactly when the rule acquires a conserved
energy functional — i.e. when the founder's C23 (inertia stored in
the Sea's arc configuration) and C24 (conservative two-channel cycle)
are specified quantitatively enough that an energy can be written and
its conservation checked. **The blocker is a specification before it
is a compute problem.** Until then, PR4 as frozen appears unmeetable
by any route — and PR1–PR7 must ALL be met before Candidate (B)
promotion, which is the upstream dependency of the DM-1/DM-3 revision
and therefore of the entire release chain (audit, Patch 2814).

## §3 — Dispositions (the panel's to choose; the worker declines)

1. **HOLD PR4 AS FROZEN.** Promotion waits on the C23/C24
   specification and its verification. Honest and conservative;
   possibly a long wait, and it leaves a criterion on the books that
   no currently-specified physics can satisfy.
2. **AMEND PR4 BY MOTION.** E.g.: PR4 is met by an *analytic
   demonstration that the bare Moment rule admits no energy-only
   Gibbsian stationary marginal*, together with a named open
   condition on the completed (C23/C24) rule, carried honestly in
   the papers. Precedent offered for the panel's own weighing: DM-2
   traversed release-readiness carrying an open field-equation
   condition — the release plan's own gate language distinguishes a
   KILL (blocks) from an open condition honestly carried (does not).
3. **RULE PR4 INAPPLICABLE** to a candidate whose screening claims
   rest on Metropolis/HNC. **The worker flags against this option:**
   PR4's own sentence, "Metropolis or HNC concordance cannot satisfy
   PR4," was written precisely to foreclose it.

**Worker recommendation, marked as such and not acted upon: option
2** — on the ground that PR4's PURPOSE (preventing unearned reliance
on the Metropolis machinery) is *served* rather than evaded by an
analytic demonstration of what the bare rule cannot supply: it tells
every downstream consumer exactly what the Metropolis results are
worth and what would license them. The worker notes its own conflict
of interest plainly: option 2 is the disposition that unblocks the
founder's prime goal, and a worker who both discovers a blocking
criterion and chooses its amendment has retargeted. Hence this
motion.

## §4 — Questions

**M1.** Do you accept the §1 finding — that the bare Moment rule
conserves no energy and that PR4's question is consequently ill-posed
for it?
**M2.** Which disposition (1, 2, or 3), with wording if you amend?
**M3.** If disposition 2: what exactly must the named open condition
say, and must the analytic demonstration be written up as a
submittable artifact before PR4 is marked met?
**M4.** Independently of PR4: PR2's frozen text asks for κ_eff/κ_D
"consistent with 1 within total uncertainty ≤ 3%." PR2-PHYS returned
1.0349 ± 0.0194 — consistent with 1 at 1.8σ, total uncertainty
1.94% ≤ 3%. The [0.97, 1.03] band was a WORKER operationalization in
the 2795 prereg, stricter than PR2's own text. **Which reading
governs?** The worker has seen the number and therefore declines to
rule; the directed statistics extension proceeds either way.

## §5 — Execution-integrity note (protocol change, worker-side)

Per the 2813 lesson, this dispatch **withholds a challenge key**: a
specific unpublished value computable only by executing the committed
scoping code. Any seat claiming execution should report **the value
of H at Moment 50 of the Patch-2815 scoping trajectory** (M = 12,
R = 3, N = 24, rng seed 11, `code/2802_automaton2_engine.py`
lineage). The expected value is deliberately **not computed or
committed** until a seat returns one — it will be verified on return.
Seats that do not execute should simply declare
REASONED-UNVERIFIED, which carries no penalty and is the honest path.
