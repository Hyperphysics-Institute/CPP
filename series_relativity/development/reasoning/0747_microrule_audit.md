# Reasoning capture — Patch 0747: auditing the swarm's H-micro-rules

*Session 154. Audits the count-driven H-micro-rules from the swarm (Thomas + Copilot). Writeup:
`.../development/microrule_audit_finding.md`. Toy: `.../scripts/0747_microrule_audit.py`. NO THEO.*

## Why I audited rather than accepted

Copilot has a repeated pattern: assert "this local rule coarse-grains to ln(n)" by analogy to chemical
potential, without showing it. The proposal this round did the same. I held the standard of computing
n_s for each rule AS WRITTEN rather than trusting the analogy. This is exactly the swarm-validation
honesty Thomas relies on.

## Result (computed, not asserted)

- R1 Thomas "PSR_base doubles per CP" (boost ~ over-occupation count n): H ~ n -> n_s = -5. EXCLUDED.
- R2 Copilot flux (P ~ 1/n_j): gross outward ~ n -> n_s = -5; and net flux ~ 0 for a uniform stack
  (needs a gradient) -> no expansion. EXCLUDED / non-functional for uniform.
- R3 Copilot "Pi/n" = (n-1)/n: SATURATES to a constant -> H ~ const -> n_s = 1 (HZ cliff). EXCLUDED.
  NOT "ln n in disguise"; it is the on/off cliff in disguise. ((n-1)/n -> 1, vs d(ln n)/dn = 1/n -> 0.)
- R4 harmonic (k-th CP ~ 1/k): Sum 1/k ~ ln n -> n_s = 0.9650. WORKS -- but is NOT among the proposed
  rules.
- R5 ln n asserted: 0.9649.

So every PROPOSED rule gives an excluded value; only the (un-proposed) harmonic/chemical-potential form
gives 0.965.

## The crux I identified: an internal inconsistency

The proposal asserts BOTH (a) potential = n (each CP = one unit, "n increments of SSV") and (b) boost
~ ln n. Incompatible if boost ~ potential: then boost ~ n (linear, excluded). The log requires boost ~
CHEMICAL POTENTIAL mu(n) = dF/dn ~ ln n (entropy derivative), NOT ~ the raw count. Relabeling n as
"occupancy SSV" does not fix it. The proposal conflates "couples to occupancy" with "couples to the
chemical potential of occupancy"; only the latter is logarithmic.

## What actually produces ln n
H(n) ~ mu(n) ~ ln n, i.e. diminishing per-CP contributions, k-th CP ~ 1/k -> harmonic sum -> ln n.
Candidate CPP mechanism: SCREENING (the k-th buried CP couples to only the ~1/k unscreened fraction).
Honest: this is a candidate, not a derivation; "why exactly 1/k" needs CPP grounding.

## Honesty calibration
- Credited the architecture as RIGHT (count-driven, decoupled from gravity SSV, multiplicative
  exponential, SSV_net direction) -- real progress, the swarm's contribution.
- Did NOT accept the ln(n) claim; showed the rules give excluded values.
- Did NOT over-kill: the count-driven branch remains viable/favored (0746); only the specific
  micro-rules fail. n_s=0.965 stays "viable & favored, not derived."
- Offered the screening/harmonic candidate constructively but flagged it as un-grounded (not a fit
  substituted for Copilot's fit).
- NO THEO; no prediction registered.

## Pointer
- Remaining task: a CPP-native rule with diminishing per-CP boost (~1/k, e.g. screening) whose
  coarse-graining PROVABLY gives ln n (chemical potential), not asserted. Clear of chirality.
  PCD = Perceive/Compute/Displace.
