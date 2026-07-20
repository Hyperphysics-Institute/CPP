# FORM-1 Agenda B — registered-instrument holdout arc pre-registration (the FB-MECH A/B discriminator), committed before any run

**Patch 2657, 20 July 2026.** The Tier-3 arc frozen at 2655 §3 / 2656 §4,
instantiated on the REGISTERED instrument. Sequencing disclosure (the G-CONS
precedent, 2588): this prereg is written after the arm-1 negative (2656) and
its motivation includes that negative's diagnosis; the PREDICTIONS it reads
against were frozen at 2656 §4 before any instrument cell existed, and they
are not restated or edited here — they bind by citation.

## 1. Instrument (verbatim, pinned)

`n1_disc2` exactly as 2629: exec-load of `code/2602_hgamma_gates_b1.py`
through the 2609 cut; the 2629 `launch` / `cell` / `reads2` / `classify`
machinery verbatim (exec-load of `code/2629_sink_obs1.py` through its stage
dispatch); B1 geometry b = 0, η = 0.5, TC = 120, v = 0.10c throughout. The
ONLY extensions are width and dt values on the already-registered ladder
pattern — no code path changes, no new classifier, no geometry change.

## 2. Cells (frozen; one pass each; no escalation rungs — any dt-instability registers as data)

- **PIN (mandatory, gates everything):** w ∈ {2, 3, 4} × dtf ∈
  {1/100, 1/200, 1/400} — must reproduce the 2629 P1 printed S_WA row TO THE
  PRINTED DIGIT (149.86/151.10/151.72; 122.68/149.74/161.40;
  228.35/203.85/182.72). Pin failure → the arc STOPS, nothing reads.
- **H2 (the A/B discriminator):** w = 4, dtf ∈ {1/400, 1/800}.
- **H3:** w = 2, dtf ∈ {1/400, 1/800}.
- **H1 (DIAGNOSTIC-QUARANTINED, as w = 3):** w = 2.5, dtf ∈
  {1/100, 1/200, 1/400}. No DM consumer may ever cite a w = 2.5 number.

## 3. Readings (bound by citation to 2656 §4; class lines restated for the execution patch's convenience only)

P-H2: final-inc(w=4, 1/400→1/800) ≤ 5% reads **FB-MECH-A-SUPPORTED**
(re-convergence); ≥ 5% reads **FB-MECH-B-SUPPORTED** (persistent
non-convergence, Branch-U class). P-H3: w = 2 stays ≤ 2.5% (both accounts);
the A-account's cancellation structure additionally expects ≤ the registered
0.41% class. P-H1: A expects < 5%; B unconstrained. **Composite consequence
(frozen):** whichever mechanism class fires, Agenda B's charter composite
remains bounded at **FD-BOUNDARY** (Tier 2 registered UNMET at 2656); the
mechanism classification attaches OBSERVATION-GRADE to the FD-BOUNDARY
registration, the C7-campaign attachment pattern (2653). No schedule
consumer opens under any reading; the DISC amendment's pending clause is
untouched under any reading.

## 4. Fences

Charter §6 verbatim; w ∈ {2.5, 3} quarantined; 2513/2635/2626/2629 records
unedited; C7 untouched; **79.5% untouched.** Verify next patch:
`code/2658_form1_b_holdout.py`, stages pin | h. Reasoning: `reasoning/2657.md`.
