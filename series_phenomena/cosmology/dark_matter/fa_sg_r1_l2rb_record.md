# FA-SG-R1 L2-RB EXECUTION RECORD (Patch 2785) — same-font

**Executed 2026-07-23 under the FROZEN 2784 prereg. Verdicts up front:**

- **P-RB1 (structural class): all six committed realizations STAGGERED
  by wide margins — but the committed verdict is VOID-BY-PREREG-DEFECT
  (D1, below) and the results are offered to the panel as DISCLOSED
  evidence, not blind-preregistered evidence.**
- **P-RB2 (I1-native quantitative): FAIL on the frozen criteria — 0/4
  amplitude ratios inside the envelope, sign mismatch at g2 — and the
  FAIL is robust to the one tolerance-construction defect found (D2):
  under the D2 repair the miss count is unchanged and the sign
  disagreement strengthens (g2 AND g5).**
- **No class consequence attaches in any branch (frozen fence);
  R1-SHIFT stands independently via J3-REVISE; the original L2R FAIL
  stays in the ledger.**

CONV-003 provenance: every number below computed by
`code/2785_l2rb_execution.py` (defect-repair analysis:
`code/2785_defect_check.py`) from the frozen 2694-lineage constants
(L_UNIT = 0.589 fm, a = L_UNIT/φ, α = a/(π√2), kernel 1/D). Verbatim
reasoning: `reasoning/2785.md`.

---

## §1 — DEFECT REGISTER (author-side, disclosed same-font)

**D1 — gate/realization inconsistency in the frozen prereg (freeze
defect, RB-1).** The 2784 prereg froze construction-audit-gate
criterion (ii) as "shortest torus lattice vector ≥ 3 × nn" and in the
same section asserted the six committed realizations were "all
gate-verified at freeze time." That assertion was FALSE: the pilot
FCC(5,3,2) has min|L| = 2.83 nn and fails criterion (ii). The freeze
error is the author's: the reconnaissance script printed the min|L|
values, the ≥3 nn threshold was drafted as a margin criterion without
being re-checked against the committed set. Consequence, per the
prereg's own defect clause: the RB-1 committed verdict is VOID; the
results are reported in full below as DISCLOSED evidence, and the panel
adjudicates their standing. **The repair choice is a panel question,
not an author's post-hoc call:** (a) relax criterion (ii) to
min|L| > 2 nn (physically justified — z = 12-for-all-sites already
precludes nn-level self-image contamination, and > 2 nn precludes a
site being its own nn image; 2.83 nn passes), noting that NO FCC torus
with 120 sites can satisfy 3 nn (4abc = 120 with all dims ≥ 2 forces
(5,3,2) uniquely, min box 2 cells); or (b) hold 3 nn and drop the
exact-count FCC match from the family. Under either repair the results
table is identical; what differs is only whether the exact-count-match
datapoint is admissible.

**D2 — tolerance construction ill-defined at the singleton shell
(freeze defect, RB-2).** The frozen deletion-resampling rule ("deleted
vertex excluded from its shell mean") did not anticipate deletion of
g5's single member (the antipodal vertex, id 15): those 3 runs produce
an empty shell mean → nan → the ρ₄ envelope was [nan, nan], mechanically
scoring ρ₄ outside. Repair analysis (envelopes recomputed with the 3
antipode-deletion runs excluded): ρ₄ envelope becomes [0.0025, 0.0621]
— observed 8.329 remains outside by ~134×; all other envelopes
unchanged to the digit; the miss count stays 0/4; and g5's predicted
sign becomes determinate (+1) against observed −1, so P-RB2(i) fails at
two shells instead of one. **D2 does not rescue any criterion; it
mildly strengthens the FAIL.**

No other departures from the frozen prereg occurred. The disclosed
pilot readout (2784 §0) matched exactly at execution (neg-frac 0.429).

---

## §2 — L2-RB-1 results (DISCLOSED evidence per D1)

Committed datapoints (source = committed orbit origin site; both frozen
metrics; thresholds neg-frac ≥ 0.10 AND nn-flip ≥ 0.10):

| Realization | N | gate | neg-frac | nn-flip | class |
|---|---|---|---|---|---|
| FCC(5,3,2) [disclosed pilot] | 120 | **FAIL (D1: 2.83 nn)** | 0.429 | 0.525 | STAGGERED |
| FCC(3,3,3) | 108 | PASS (4.24 nn) | 0.421 | 0.434 | STAGGERED |
| HCP(5,6)×4 | 120 | PASS (3.27 nn) | 0.496 | 0.435 | STAGGERED |
| HCP(3,6)×6 | 108 | PASS (3.00 nn) | 0.383 | 0.418 | STAGGERED |
| dhcp(5,3)×8 | 120 | PASS (3.00 nn) | 0.395 | 0.435 | STAGGERED |
| dhcp(3,3)×12 | 108 | PASS (3.00 nn) | 0.327 | 0.462 | STAGGERED |

Robustness axes (reported, not committed): HCP(5,6)×4 B-layer source —
0.496 / 0.435 (identical to committed source, consistent with
single-orbit HCP); dhcp(5,3)×8 h-orbit source — 0.395 / 0.412.

I1 side (recomputed same-font): chord neg-frac 0.723 / nn-flip 0.203;
geodesic neg-frac 0.597 / nn-flip 0.525.

**Substantive reading (offered for adjudication):** in the honestly
matched family — boundaryless, all-z = 12, count-matched — site-level
staggering is UNIVERSAL, at 3–5× the committed thresholds, across three
stacking structures, two counts, and both site orbits. The gate-passing
five alone (any repair branch) already show this. The original L2's
19-site CLEAN arena is thereby localized as a scattering-depth artifact,
consistent with the panel's own diameter-vs-count diagnosis (2766 §2b)
— while noting same-font that this evidence is disclosed, not blind.

---

## §3 — Onset ladder (CHARACTERIZATION-ONLY; no prediction, no class consequence, no 3D→4D transfer)

| FCC torus | N | neg-frac | nn-flip |
|---|---|---|---|
| (2,2,2) | 32 | 0.613 | 0.467 |
| (3,2,2) | 48 | 0.532 | 0.507 |
| (3,3,2) | 72 | 0.493 | 0.448 |
| (4,3,2) | 96 | 0.453 | 0.461 |
| (3,3,3) | 108 | 0.421 | 0.434 |
| (5,3,2) | 120 | 0.429 | 0.525 |
| (4,4,2) | 128 | 0.465 | 0.534 |
| (3,3,4) | 144 | 0.399 | 0.399 |
| (4,4,3) | 192 | 0.382 | 0.432 |
| (4,4,4) | 256 | 0.380 | 0.449 |

Characterization: **there is no sub-threshold regime anywhere in the
scanned range** — staggering is present at every rung down to N = 32,
with neg-frac gently DECREASING in N (0.61 → 0.38) rather than
switching on. In the boundaryless family the "onset" of the 2694 ball
scan does not exist; the ball-family N* was a boundary-dilution effect
(boundary sites at z < 12 diluting the staggered mode), consistent with
the dimension-obstruction reading. Recorded as characterization for the
KINETIC-1 / K1-S1 consumers only.

---

## §4 — L2-RB-2 results: FAIL (frozen criteria; defect-robust)

Predictor (chord metric, geodesic-shell aggregation per the frozen
coarsening map; nominal): shell means {+0.8951, +0.02529, −3.55e−4,
−1.30e−5, +2.87e−7}. Perturbation set: α × {0.969, 1.000, 1.031} ×
(nominal + 119 single-vertex deletions) = 360 runs.

Predicted sign sequence: {+, +, INDETERMINATE-PREDICTOR, −,
INDETERMINATE-PREDICTOR} (g3 and g5 sign-unstable under the frozen
perturbations; under the D2 repair g5 becomes determinate +).

Target (geodesic metric, nominal): shell means {+1.0820, −0.01976,
+0.01875, −0.04209, −0.35059}. Observed signs {+, −, +, −, −}.

| Ratio | observed | frozen envelope | D2-repaired envelope | in (either) |
|---|---|---|---|---|
| ρ₁ | 0.0183 | [0.0213, 0.0484] | unchanged | NO |
| ρ₂ | 0.9486 | [0.0006, 0.0349] | unchanged | NO |
| ρ₃ | 2.2452 | [0.0087, 0.9091] | unchanged | NO |
| ρ₄ | 8.3292 | [nan, nan] (D2) | [0.0025, 0.0621] | NO |

**P-RB2(i) FAIL** — determinate-shell mismatch at g2 (frozen) and at
g2 + g5 (repaired). **P-RB2(ii) FAIL** — 0/4 inside under either
envelope, with ρ₂/ρ₃/ρ₄ outside by factors ~27× / ~2.5× / ~134×.
**P-RB2 overall: FAIL, defect-robust.**

**Substantive reading (adverse, informative):** the two I1-native
operators disagree qualitatively in depth structure. The chord
operator's staggered response decays steeply (four orders of magnitude
across the geodesic shells); the geodesic operator's response
CONCENTRATES at the antipode (|f̄_g5| = 0.351, larger than every
non-source shell except g1 — against a chord-predicted ~3e−7). The
staggered CLASS is metric-robust (both metrics OSC, of record since
2694); the quantitative staggered structure is NOT metric-transportable
even within I1 itself. This is the same lesson as R1-SHIFT, now
established at fixed arena: the readout is representation-dependent at
quantitative resolution. Any future consumer of an I1 evanescent scale
must carry the metric/operator choice as an explicit representation
label.

---

## §5 — Standing and dispatch

- No class consequence attaches (frozen fence; chartered 5–0 at 2766).
  R1-SHIFT stands. The original L2R FAIL stays in the ledger; this
  record joins it, same-font.
- The pair {0.0904 ± 0.0028 fm | ≈ 0.168 fm premise-rejected} under
  rider v2.7 is untouched by this leg.
- **Questions for the panel (CONV-001 dispatch to follow):**
  - **Q1:** standing of the §2 RB-1 evidence given D1 (disclosed vs
    blind) — does the structural-class conclusion stand?
  - **Q2:** D1 repair branch — relax gate (ii) to > 2 nn with the
    z = 12 justification, or hold 3 nn and drop exact-count FCC?
  - **Q3:** disposition of RB-2's defect-robust FAIL — does it CLOSE
    L2-RB adversely (quantitative non-transportability recorded), or
    warrant a repaired RB-2R with a differently-constructed
    quantitative target? Author-side note, same-font: the author sees
    no repaired construction that would not amount to retargeting
    after an adverse result, and recommends adverse closure.
  - **Q4:** whether the §3 no-sub-threshold characterization should be
    forwarded to the K1-S1 arc as a named input.

---

## §6 — PANEL DISPOSITION (Patch 2788; adjudication: `conv001_2026-07_l2rb_x3x4_batch_adjudication.md`)

**Q1 (5–0 on substance, amended wording adopted):** RB-1 COMMITTED
VERDICT VOID under D1; DISCLOSED evidence nevertheless supports that
the earlier 19-site non-staggering result was a
compact-boundary/scattering-depth artifact, not evidence for an
intrinsic population threshold; not promoted to
preregistered-confirmation grade. Downstream citations must carry the
disclosed-evidence label.

**Q2 (split, reasoned adjudication):** repaired gate for FUTURE
structural-class tests: z = 12 exactly; min|L| ≥ 3 d_nn; frozen count
bracket N ∈ [0.9, 1.1]·N_target replacing exact-count matching; ≥2
counts per stacking family where constructible. No retroactive RB-1
verdict.

**Q3 (5–0): RB-2 CLOSED ADVERSE** — staggered class metric-robust on
I1; shell amplitudes, signs, decay structure, and antipodal
concentration NOT quantitatively transportable chord → geodesic; D2
does not alter the disposition. RB-2R only under a fresh prereg with
an independently derived mapping. **THE L2-RB ARC IS CLOSED.**

**Q4 (5–0):** onset-ladder characterization forwarded to K1-S1 under
provenance tag "L2-RB onset ladder characterization (2784–2785)",
characterization-only, adopted wording in the adjudication record.

**MACHINE-READABLE D1 NOTE (S4 action item 1):**
```json
{"defect":"D1","type":"jointly-unsatisfiable-frozen-constraints",
 "constraint_a":"min_boxvector >= 3*d_nn",
 "constraint_b":"FCC torus with exactly 120 sites (4abc=120, all dims>=2)",
 "proof":"4abc=120, a,b,c>=2 => {a,b,c}={5,3,2} uniquely; min dim 2 cells => min|L|=2*sqrt(2)*d_nn=2.828*d_nn < 3*d_nn",
 "consequence":"committed RB-1 verdict void; results stand as disclosed evidence",
 "repair_adopted":"z=12 exact; min|L|>=3*d_nn; count bracket [0.9,1.1]*N_target; >=2 counts per stacking family (future tests only)",
 "d2_repair_artifact":"code/2785_defect_check.py (immutable, committed Patch 2785)"}
```
