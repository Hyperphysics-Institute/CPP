# CONV-021 DISPATCH — THE ESTIMATOR IMPASSE AND THE N216 CHALLENGE (founder-initiated ahead of the Route C bundle; the DM verdict gets its own round when Kila6 lands)

**Patch 3146 (15 Aug 2026). CONV-001 single-block format: one fenced
block, verbatim to all five reviewers. Returns →
`conv021_2026-08_returns_adjudication.md`. Binding rules in the
block.**

The block:

````
CPP MULTI-AI REVIEW — ROUND CONV-021: A METHODOLOGICAL IMPASSE (converged finite-size sequence: which estimator?) AND THE N216 CHALLENGE IT GOVERNS
You are one of five reviewers (GPT, Grok, Gemini, Copilot, DeepSeek). This round asks ONE substantive question you are unusually well placed to answer, plus its consequences. Self-contained. The worker has deliberately NOT chosen among the competing readings, because choosing after seeing them would be the exact extraction this programme forbids; that choice is what we are asking you to make or to bound.

== A. THE SETTING (brief) ==
A cosmology-blind lattice campaign locates a substrate phase transition (a "melting" spacing d_s* in Planck units) by susceptibility peaks in microscopic order parameters, then extrapolates to infinite array size. In CONV-019 you mandated this campaign; it ran, and its FROZEN output was d_s* = 2.450, obtained from a pre-declared LINEAR-in-1/n extrapolation over sizes n = 3, 4, 5 (27/64/125 pairs). A later, larger size (n = 6, 216 pairs) produced a four-size linear refit of 2.194, which fell outside the pre-declared +/- 0.182 consistency window and was therefore recorded as a formal CHALLENGE to the frozen number (the frozen 2.450 has NOT been revised; by standing rule a challenge cannot silently revise a frozen result).

== B. WHAT HAS HAPPENED SINCE (two campaigns, both preregistered) ==
1. n = 7 (343 pairs). Resolution instrument, form frozen before the run: critical ansatz d*(n) = d_inf + a*n^(-1/nu), nu by grid search, least squares. RESULT: the search ran to its declared nu ceiling and returned d_inf = -1.159 -- an unphysical (negative) spacing; the combination spread (3.07) also exceeded the campaign's own 0.75 SPLIT guard. The worker declared NO-VERDICT (instrument failure), diagnosed the cause (as nu grows, n^(-1/nu) -> 1 for all n: the design columns become collinear and the intercept is unidentifiable), and did NOT report the mechanical verdict the broken fit implied.
2. The repair was made WITHOUT a review round (per this programme's review-economy rule: rounds are for wins or exhausted avenues, not for formality), and was frozen BEFORE the data that would test it existed. The redesign is INTERVAL-VALUED with no point selection: admissible set A = {nu in [0.40, 4.00] : SSE <= 1.10*SSE_min AND d_inf >= 0}; the estimate is [min, max] of d_inf over A; a secondary refit dropping the smallest size is reported but never substituted; and the rule declared its OWN trigger -- interval width > 1.0 means the avenue is exhausted and goes to you.
3. n = 8 (512 pairs) then ran under that frozen rule. The width gate fired: the avenue is exhausted, which is why you are reading this.

== C. THE DATA (six sizes, both seeds, seed agreement <= 0.002, stationarity ~ 1.00 everywhere) ==
The susceptibility-peak location of the bound-occupancy order parameter, by size:
   n = 3: 3.420
   n = 4: 3.338
   n = 5: 3.106
   n = 6: 2.649
   n = 7: 2.617
   n = 8: 2.614
Successive steps: 0.082, 0.232, 0.457, 0.032, 0.003. The final step is one part in ~900.
THE THREE READINGS NOW ON THE TABLE (the worker has selected NONE):
 (i) PRIMARY, per the frozen interval rule: d_inf in [0.009, 1.281], width 1.272 -- uninformative; the admissible nu range was [1.78, 3.08]; the width gate fired.
 (ii) SECONDARY, per the same rule but dropping n = 3 (the most correction-prone size; reported, never substituted): d_inf in [1.786, 2.405], width 0.619 -- this EXCLUDES the frozen 2.450, by 0.045.
 (iii) DIRECT CONVERGENCE (descriptive, no extrapolation): the sequence appears converged at 2.614; taken as the infinite-size estimate, |2.614 - 2.450| = 0.164, which lies INSIDE the +/- 0.182 consistency window and would CONFIRM the frozen value.
Note the tension plainly: (ii) says the challenge stands; (iii) says it resolves; (i) says nothing.

== D. THE WORKER'S DIAGNOSIS (offered for attack, not as a conclusion) ==
The power-law extrapolation is misspecified for a sequence that has already converged: with no residual drift, nu and d_inf trade off freely, which is exactly what both failures exhibit. Under that reading, direct convergence is the appropriate estimator and (iii) governs. AGAINST that reading: a converged-looking tail at n = 6, 7, 8 could be a plateau that later resumes drifting (larger sizes are affordable: n = 9 and n = 10 are feasible on available hardware, ~4-8 h each); and the abrupt character of the n = 5 -> 6 step (0.457, by far the largest) sits oddly against a smooth approach to a limit -- it may indicate a crossover, a commensuration effect, or that the small sizes and large sizes are in different scaling regimes entirely. There is ALSO a robust unexplained feature at spacing d_s = 2.0: the same order parameter dips sharply there at every size, monotonically deepening (0.232, 0.186, 0.165, 0.156 for n = 5, 6, 7, 8), at both seeds.

== E. WHAT TO ATTACK ==
Whether "converged" is established or merely apparent at these sizes; whether dropping n = 3 is defensible or is itself a post-hoc lever (the worker declared it in advance and reports it always, but you should judge); whether the 10% SSE tolerance and the d_inf >= 0 constraint are reasonable or arbitrary; whether the abrupt n=5 -> 6 step invalidates treating all six sizes as one scaling family; whether the d_s = 2.0 anomaly could be distorting the peak locations themselves; whether an entirely different estimator (data collapse over the full order-parameter curves, Binder-cumulant crossings, or fitting f_b(d_s, n) globally) should replace peak-location extrapolation; and whether the worker's decision to repair the instrument WITHOUT a review round was correct or should have come to you first.

== F. QUESTIONS -- answer ALL with EXACTLY this vocabulary ==
Q1 THE ESTIMATOR (the heart): [DIRECT-CONVERGENCE (reading iii governs) | SECONDARY-INTERVAL (reading ii governs) | NEITHER-SPECIFY (name the estimator you would freeze) | INSUFFICIENT-DATA (name the sizes or diagnostics you would require first)]
Q2 THE N216 CHALLENGE, given your Q1: [RESOLVES-CONFIRMING (the frozen 2.450 stands) | STANDS-QUANTIFIED (state the challenger value your Q1 implies) | REMAINS-OPEN (state what would close it)]
Q3 CONVERGENCE STATUS: is the n = 6,7,8 tail [ESTABLISHED-CONVERGED | APPARENT-ONLY (specify the test or size that would settle it) | CONFOUNDED (name the confound)]
Q4 THE INSTRUMENT REPAIR WITHOUT A ROUND (economy rule applied; redesign frozen before the testing data existed): [PROCEDURALLY-SOUND | SHOULD-HAVE-DISPATCHED (say what a round would have added)]
Q5 THE d_s = 2.0 ANOMALY: [BENIGN (peak locations unaffected) | CONFOUNDING (specify how it would bias the peaks) | UNKNOWN-INVESTIGATE (name the diagnostic)]
Q6 NEXT ACTION, one line: what should be computed next, if anything, before this challenge is closed?

== G. FORMAT ==
(1) Q1-Q6 one line each. (2) Strongest objection (one paragraph). (3) Steelman (one paragraph). (4) Concrete error found, with location, or "none found." Under 700 words.
````

**Binding rules:** majority tallies on Q2–Q5. **Q1 governs Q2:** a
majority Q1 answer FIXES the estimator, which is then FROZEN into
the record before any further analysis is run, and the Q2 verdict
follows from it mechanically. If Q1 splits with no majority, the
estimator question is recorded as UNSETTLED, the frozen 2.450
stands unrevised, and the challenge remains OPEN pending whichever
diagnostics the Q6 majority names. Q6 is advisory. The worker
performs no estimator selection in any branch.
