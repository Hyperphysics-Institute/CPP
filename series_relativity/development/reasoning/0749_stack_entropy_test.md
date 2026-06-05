# Reasoning capture — Patch 0749: stack entropy — the log is indistinguishability, not distinguishable phases

*Session 154. Tests Copilot's stack-entropy proposal. Writeup: `.../development/stack_entropy_test_finding.md`.
Toy: `.../scripts/0749_stack_entropy_test.py`. NO THEO.*

## Convergence acknowledged
Copilot independently reached the 0748 conclusion: only microstate counting gives the log; geometry/
placement/packing are dead. Correct, and the chemical-potential object (H ~ dS/dn) is the right one.

## The check I ran (computed, not asserted)
"Omega ~ n! generically" is the unchecked step. Computed n_s for the candidate entropy forms:
 - DISTINGUISHABLE labels (distinct ZBW phases): Omega=q^n, S=n ln q (extensive), dS/dn=ln q=CONST ->
   H const -> n_s=1 (CLIFF), EXCLUDED.  <-- this is Copilot's stated mechanism, and it gives the cliff.
 - INDISTINGUISHABLE ideal gas (fixed V): mu ~ ln(n/V) ~ ln n -> H ~ ln n -> n_s=0.9649.
 - orderings Omega=n!: dS/dn=ln n -> 0.9649.

## The catch
The log requires INDISTINGUISHABILITY (the Gibbs n! divisor / fixed-volume concentration chemical
potential mu ~ ln(n/V)). Copilot invoked ZBW phase to make CPs DISTINGUISHABLE so there would be
microstates -- but distinguishable labels give Omega=q^n -> extensive -> CONSTANT mu -> the cliff. These
are OPPOSITES. So the proposed microstate mechanism, taken literally, gives the EXCLUDED answer; the log
comes from the opposite property and does not need phase microstates at all.

## What is genuinely right and well-motivated
The log = the standard concentration chemical potential of n IDENTICAL CPs over-concentrated in one GP's
fixed volume: mu ~ ln(n/V). Coefficient-free p=2 (d ln(ln n)/dN = -1/N_rem regardless of constant). This
is textbook stat-mech and gives 0.9649 robustly -- IF a CP stack is a thermodynamic ensemble.

## The honest structural commitment
Requires a CPP 'temperature'/Gibbs statistics at the stack level (a real ensemble), so mu ~ ln(n/V) is
legitimate, not analogy. CPP primitives are deterministic PCD. If a stack is an ensemble -> 0.9649
derived (coefficient-free); if not -> favored, not derived. This is the correctly-posed remaining
question -- NOT phase labels, NOT a placement rule.

## Honesty calibration
- Credited the convergence (entropy is the only route) and the correct core (log is a chemical potential).
- Did NOT accept "Omega ~ n!": computed it; distinguishable -> cliff, indistinguishable -> log.
- Corrected the muddle: the log needs indistinguishability, the OPPOSITE of the stated distinguishable-
  phase mechanism. ZBW phases are a red herring for the log.
- Did not over-claim: 0.9649 derivable IFF stack is a thermodynamic ensemble; that commitment is the
  open question. NO THEO; no prediction registered.

## Pointer
- THE question: is a stack of identical CPs in one GP a thermodynamic ensemble in CPP (temperature/Gibbs
  statistics), so mu ~ ln(n/V) is real? Then 0.9649 is derived (coefficient-free p=2). The log = indistin-
  guishable-particle concentration statistics. Clear of chirality. PCD = Perceive/Compute/Displace.
