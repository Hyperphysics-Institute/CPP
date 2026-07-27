# OPEN-K1-MEMORY-1 — A SCOPING OBSTACLE RAISED BEFORE PREREGISTRATION (Patch 2833)

**Filed 2026-07-27. The panel adopted route (b) — χ(k, ω) at small ω
on the PR3 apparatus — 5–0. In drafting the prereg the worker
identified a problem with that route that no seat raised and that the
worker did not raise when proposing it. It is surfaced here BEFORE
any freeze rather than discovered afterward.**

## §1 — The obstacle: Metropolis has no physical time

The PR3 apparatus is a **Metropolis Monte Carlo** chain. Its "time"
is measured in sweeps, and sweep-time is an **algorithmic** parameter,
not physical time: the same equilibrium ensemble is reproduced by
Metropolis, heat-bath, or any other update rule satisfying detailed
balance, each with a *different* relaxation spectrum. Driving that
chain at frequency ω therefore measures **χ(k, ω_MC)** — the
finite-frequency response of the SAMPLER — and ω_MC has no
established conversion to any physical frequency in the CPP substrate.

**Why this matters for what clause 2 asks.** The memory
counterexample (S1's, at the K1 adjudication) was directed at whether
the *registered Moment dynamics* admits a gradient-generated
stationary measure. Memory in the Moment rule is the object of
interest. Memory in the Metropolis sampler is an artifact of a
convenience algorithm.

**The sharper form of the difficulty.** The STATIC identity
χ(k,0) = βN S_zz(k) is a purely thermodynamic relation: it holds for
ANY dynamics whose stationary measure is Gibbs, independent of the
dynamics' memory structure. That is exactly why PR3 could pass on
Metropolis machinery and why its passing was meaningful — it tested
the ensemble. But the FINITE-frequency FDT is dynamics-specific.
Measuring it on Metropolis tests Metropolis. **Route (b) as adopted
may therefore be well-posed and cleanly executable while answering a
question adjacent to the one PR7 clause 2 asks.**

**And the deeper tension, stated plainly:** PR4-BARE established that
the bare Moment rule has no identified conserved energy and hence no
Gibbs measure at all. A finite-frequency FDT test presupposes the
very equilibrium structure PR4-BARE found absent. The two results are
in tension about which dynamics clause 2 should be evaluated on.

## §2 — Options (worker declines to choose; all have costs)

1. **Execute route (b) as adopted, with the limitation stated in the
   record.** Result would read: *the Metropolis sampler's
   finite-frequency response departs from its static limit by less
   than X across band B.* Honest, cheap, and a genuine statement
   about the estimator's validity domain — but NOT about Moment-rule
   memory. Risk: a future reader takes it for the latter.
2. **Re-scope clause 2 to the estimator question**, i.e. rule that
   what PR7 needs is confidence that the *bridge as used in the
   screening derivations* is not corrupted by finite-frequency
   effects within the sampler — making route (b) exactly right and
   the label "memory" the misleading part. Requires a panel motion.
3. **Move the test to the Moment rule** (route (a)-like, on automaton
   trajectories). This is the physically faithful reading — but the
   AUTOMATON arc CLOSED at the FEM boundary, and limitation L-2
   forbids citing its statistics for PR4-class claims. Clause 2 would
   then be blocked behind the same C23/C24 specification as
   PR4-COMPLETED, i.e. **PR7 would join PR4 in awaiting founder
   physics rather than compute.**
4. **Split clause 2**, as the panel split PR4: an estimator-level
   part closable now by route (b), and a dynamics-level part carried
   as an open condition alongside OPEN-PR4-C23C24.

**Worker's assessment, offered as such:** option 4 mirrors the
structure the panel itself chose for PR4 and is probably right, but
it has the same shape as the last amendment that unblocked the prime
goal — and the worker proposing it is again the party who benefits.
Hence: raised, not chosen.

## §3 — Why this is filed rather than absorbed

The worker proposed route (b) at 2831 and the panel adopted it 5–0
without this objection being visible to anyone. Discovering it while
drafting and quietly writing a prereg around it — or writing the
prereg as adopted and letting the limitation surface at returns —
would both be worse than saying so now. **No preregistration is
drafted until this is disposed of.** Ledger unchanged: six of seven;
PR7 PARTIAL; B7 holds.
