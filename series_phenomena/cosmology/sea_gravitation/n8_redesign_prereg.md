# ECONOMY RULING APPLIED (WORKFLOW-REVIEW-ECONOMY): NO PANEL ROUND — this is a "we know what to do" case, not an exhausted avenue; the resolution instrument is REDESIGNED BY PRINCIPLE and FROZEN NOW, before the data that will test it exists (n = 8, unrun), which satisfies anti-extraction without spending a panel round or the founder's paste-labor; the redesign is INTERVAL-VALUED (no point selection anywhere), and it carries its OWN exhausted-avenue trigger: if the interval stays wider than 1.0 l_P even with the added leverage, THAT is the impasse the panel exists for

**Patch 3143 (15 Aug 2026). Supersedes the 3140 §2–§3 analysis form
(which failed at 3142) and the 3142 §5 "to CONV-021" disposition
for the instrument question. The 3130 CHALLENGE itself still rides
to CONV-021 with whatever this pass returns.**

## §1 — The governance decision, stated plainly

The founder's standing economy rule: panel rounds are for WINS or
for avenues we have exhausted. The 3142 failure is neither — the
defect (unidentifiable intercept as ν → large) has a known,
principled remedy that does not require adjudication. Sending it
out would consume a review round and the founder's dispatch labor
to be told what the mathematics already says. **Decision: no round;
fix by principle, freeze before the data, and let the CHALLENGE's
substantive verdict — not the instrument's repair — be what the
panel eventually sees.**

## §2 — Why freezing NOW is anti-extraction-clean

The discipline's purpose is preventing data-driven tuning. The
n = 7 peaks are known to the worker, so the redesign is stated as
an INTERVAL rule with NO free choices (§3), and its decisive
application is to a size that DOES NOT YET EXIST (n = 8, 512 pairs,
unrun at the moment of this freeze). The n = 8 numbers cannot have
shaped anything below.

## §3 — The redesigned analysis (frozen; no point selection)

Ansatz unchanged: d*(n) = d*∞ + a·n^(−1/ν).
1. **Admissible set:** A = {ν ∈ [0.40, 4.00] step 0.02 :
   SSE(ν) ≤ 1.10 · SSE_min AND the fitted d*∞ ≥ 0}. (The 10%
   tolerance and the physicality constraint are declared here,
   applied blind.)
2. **Estimate = INTERVAL:** d*∞ ∈ [min, max] over A. No single ν is
   chosen; no point value is quoted as "the" answer.
3. **Sizes:** all with a defined interior peak, n = 3…8. Declared
   SECONDARY (reported always, never substituted): the same
   interval refit dropping n = 3 (the most correction-prone size).
4. **Combination across parameters:** the 3119 rule
   (union of intervals if f_dwell brackets; f_b alone otherwise,
   stated).

## §4 — The frozen verdict rule (with its own panel trigger)

Let I be the primary interval.
- **2.450 ∈ I ⇒ CHALLENGE RESOLVES-CONFIRMING** (the frozen floor
  stands; 3130's discrepancy attributed to the linear form).
- **2.450 ∉ I and width(I) ≤ 1.0 ⇒ CHALLENGE STANDS-QUANTIFIED**,
  the interval being the challenger's value.
- **width(I) > 1.0 ⇒ NO-VERDICT-PERSISTS ⇒ THE AVENUE IS
  EXHAUSTED**, and THAT goes to the panel under the economy rule —
  a genuine impasse, with the ν-profile, both fits, and all six
  sizes attached.
In every branch the frozen d_s* = 2.450 stands unrevised pending
panel, and the calibration is untouched (OBL-CAL-LABEL).

## §5 — Execution (founder labor: one command)

`scripts/3143_n8_runner.py run` on VideoCPU — n = 8 (512 pairs,
1024 CPs), the same v2 instrument, grid {1.5…5.0} × seeds {5, 11},
16 workers (= the cell count: ONE batch, no idle tail; worker count is not a scientific parameter — cells are independent seeded processes, bit-identical at any count), per-cell checkpointing; ≈ 2–3 h wall (scales ~(1024/686)²
per cell), safe to run overnight and resumable. Then
`scripts/3143_n8_runner.py analyze` prints the frozen interval,
both fits, and the verdict in the §4 words — paste-back is the only
other founder action. Kila6 Route C untouched and still trumping
all.
