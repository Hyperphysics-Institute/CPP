#!/usr/bin/env python3
"""4252 -- TODO-4222-CRITIC item (ii): what, if anything, still rests on 4219 (counter-imprint wake, 'item 4 passes') and
4220 (reverted: wake unknown). A record audit, not a computation: the checks are greps, listed with their results."""
checks=[
 ("4219 s2 'item 4 passes by the persistent counter-imprint'", "RETIRED at 4228: the sign is the created singlet's; 4219's mechanism appears only in the arc's own records (4219, 4226-4228, where it is retired) and todolist history; no paper, registry or later derivation uses it"),
 ("4219 s1 founder clarifications: quark spin = orbital L of its DP about the core; nubar's L = the mutual spin of its DP's two CPs", "VALID and consistent with 4228/4229: the released orbital, unanchored, IS a mutual spin about the pair's centre (SF-4's unanchored ZBW, r = hbar c / m_nu)"),
 ("4220 s2 'lambda magnitude and sign both go to the wake mechanism (CONJ-FP-1)'", "SUPERSEDED at 4228 (|lambda| = 1 at the vertex; 1.275 is nucleon structure) and 4244 (the breath, g_A = 1.406): CONJ-FP-1 carries nothing of lambda now"),
 ("PRED-O-42 row (predictions.md, registered 4219)", "STALE on three points -> amended in this patch: basis names G-EW-INHERIT-4205 (superseded in the allocation clause by G-EW-SWAP-4228); item 4 'UNTESTED' (passed 4228); nubar = 'refill partner' (it is the released orbital)"),
 ("SF-2 v1.08 s5.7.1", "already rewritten at 4228 (steps 3, 5, 6, postdiction); no 4219 wording found (grep 'counter-imprint', 'wake': 0 hits)"),
 ("TODO-4203-GA", "re-scoped at 4228; nothing of 4219 remains in it"),
]
for a,b in checks: print(f"- {a}\n    -> {b}")
print("\nVERDICT: 4220's reversion was correct and complete; 4219 leaves no load-bearing residue; the one stale artefact was the")
print("PRED-O-42 row, now amended. Item (ii) closed.")
