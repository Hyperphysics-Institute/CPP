# Reasoning capture — Patch 0752: emergence-track assessment

*Session 154. Assesses Thomas+Copilot's proposal that CAND-AX-EU-1's thermalization is emergent from
existing axioms via macro-CP PCD dynamics (provable by MC). Writeup: `.../development/emergence_track_assessment.md`.
Toy: `.../scripts/0752_emergence_split.py`. NO THEO.*

## Credit
The core instinct -- deterministic micro -> thermal macro under coarse-graining, NO per-CP randomness --
is exactly how stat-mech works (molecular chaos). The macro-CP narrative (13 over-stacked GPs -> +/-
splitting -> violent inter-GP oscillation -> evaporation/re-stacking -> mixing) is a serious physical
story for a genuinely chaotic early ZBW bath. Copilot's standard (it 'wins' only if an MC reproduces
mu ~ ln n) is correct.

## The key analytical move: split the axiom into two clauses of DIFFERENT status
HALF 1 (bath/ergodicity): do exchange dynamics thermalize a stack to Gibbs equilibrium << Hubble?
  Toy: seed 13-GP cohort, random-CP-hop dynamics -> initially-empty GP fills to mean; full array relaxes
  to Poisson (mean~var~lambda). Thermalization EMERGENT & generic. MC-derivable. [progress -- this was
  the clause that felt like a strong assumption.]
HALF 2 (log: absolute concentration mu(n)~ln n, the quantity the n_s chain uses): NOT dynamical. Toy:
  SAME thermalized stack, count two ways -> indistinguishable (A1) -> mu~ln n -> 0.9649; distinguishable
  (per-CP history label) -> mu const -> 1.0000 cliff. Dynamics identical; only the COUNTING differs.
  The log is the Gibbs 1/n! (combinatorial/ontological), not a dynamical output. MC is blind to it.

## Why this is GOOD news
The log's source is already A1: 'CP = polarity + type + position, no individual identity' => same-type
CPs on a GP are occupation-number objects => permutations not distinct => indistinguishability => 1/n! =>
log. HALF 2 needs NO new axiom; entailed by A1. So the emergence track need only (a) supply HALF 1
dynamically and (b) make A1 indistinguishability explicit.

## The trap (0749 in dynamical disguise)
'each CP imprinted by its individual history' taken literally = per-CP distinguishing label =>
distinguishable => cliff. The MORE the story gives each CP a unique history, the FARTHER from the log.
Fix (and Thomas's own better phrasing: spectrum 'does not inherently reside in every CP', acquired
collectively from SSV/environment): keep history in the SSV field/configuration (exchangeable bath), NOT
as CP identity. Then A1 indistinguishability survives. A literal distinguishable-history MC reproduces the
cliff -- useful negative control, trap if misread as 'dynamics predict n_s=1'.

## Honest MC scope
MC CAN derive HALF 1 (Gibbs equilibration << Hubble with A1-invariant microstates). CANNOT derive HALF 2
(log = A1 + combinatorics; MC must assume the indistinguishable counting). MUST avoid tracking
distinguishable per-CP histories as the microstate space (-> cliff). Honest claim: 'MC derives the bath;
the log is A1' -- NOT 'MC derives n_s'.

## Consequence
Splits CAND-AX-EU-1: indistinguishability clause -> A1 (no new axiom); ergodicity clause -> dynamical,
MC-provable; boost~mu -> still 0746. BEST CASE: axiom dissolves -> n_s=0.9649 is a ZERO-NEW-AXIOM
prediction (A1 + emergent ergodicity + 0746 coupling), axiom count stays 9. Reachable IF MC shows
macro-CP mixing -> Gibbs << Hubble (A1-invariant) AND history kept in bath not on CPs.

## Honesty calibration
- Credited the methodology fully (it IS how stat-mech works) and Copilot's correct standard.
- Did NOT accept 'MC derives n_s': split into bath (yes) vs log (no, it's A1+combinatorics), shown by toy.
- Surfaced the distinguishability trap precisely (the more histories-as-labels succeed, the worse) and
  the fix (history in the bath, not on CPs), grounding it in A1's exact wording.
- Reframed as progress (best case dissolves the axiom -> count stays 9) WITHOUT overclaiming (conditional
  on an MC that hasn't been run + the keep-history-in-bath discipline). NO THEO.

## Pointer
- Next (if pursued): minimal-PCD MC scoped to HALF 1 only (Gibbs equilibration << Hubble, A1-invariant
  microstates) + one line that A1 supplies HALF 2. Falsifier: macro-CP dynamics fail to reach Gibbs
  equilibrium sub-Hubble -> bath clause fails -> axiom cannot be dissolved. Clear of chirality.
  PCD = Perceive/Compute/Displace.
