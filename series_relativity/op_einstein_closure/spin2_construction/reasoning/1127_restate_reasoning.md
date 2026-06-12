# Reasoning capture — Patch 1127 (DG-3 round-1 integration + RESTATE)

**Protocol:** reasoning capture + review dispatch §6. Session 156 lane (11xx), 11 June 2026.

## The integration judgment (why RESTATE despite 2–1 CONFIRM)

ChatGPT's T1(iii) objection is *correct on the merits*: P4 proved TT flux = luminosity; it did not
prove the separate channels carry no independent energy. Grok/Copilot verified the computations
(rightly) but their T1(iii) "pass" endorsed the stronger claim the computations didn't establish.
Verdict-honesty + the protocol (verdict-flipping objection on top triage → restate) both point the
same way; vote-counting would have been the wrong integration rule. Conceded explicitly in the
aggregation file.

## Why the fix is a lemma + computation, not wording

The objection's scenario (channel drains energy with zero strain response) is real physics — it is
exactly what kills Brans–Dicke-with-strong-coupling. The discharge has to identify CPP's structural
blocker: **premise (ii) — C5 is the only field→matter coupling.** Emission is work done on matter
(there is no other emitter); absorption is work done by the metric (no other absorber). Both ends
are functionals of the assembled metric = linearized GR. The "bare-channel Hamiltonian" is then a
definition with no operational content — and premise (iv) (channels are generated broadcasts, no
independently-initialized modes in the ontology) blocks the phase-space version of the question.
The computation (Script 4) closes the loop where it could still hide: the *eccentric* budget. If
any channel drained energy, TT flux alone could not balance the full Peters f(e)-enhanced decay.
Ratio 1.000640 — it balances.

Honest scope note kept: the substrate-microscopic energy functional remains the declared
refinement, now *constrained* by the lemma (any candidate must reproduce the operational ledger).

## Discipline notes
Built on pushed 1126. Private-lane only. Reviewer attribution per dispatch steers (architect to
correct if mis-mapped). One performance fix in-session: initial Script-4 resolution exceeded the
sandbox time limit; reduced (orbit steps 200k→40k, sphere 80×160→40×80); ratio accuracy ~6×10⁻⁴,
adequate. NO VERDICT MOVED — registration still gated on round-2 3/3 + sign-off.
