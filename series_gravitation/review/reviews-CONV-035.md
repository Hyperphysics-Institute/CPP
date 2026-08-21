# CONV-035 — Returns receiver: RCORE-3 Leg C, and the narrowing of a ratified claim

**Dispatched:** Patch 3341, 21 Aug 2026 (Session 156).
**Package:** `conv035_legC_narrowing_review_package_v1.0.md` (single
CONV-001 block; record + verify script + the worker's Tier-4
reasoning fragment inlined in full; the `.py` also ships separately).

**Why this round exists:** the panel ratified at CONV-034 a claim
this patch narrows. Leg B's census was computed over ℓ ≤ 3 and stated
without an ℓ qualifier; Leg C found trapped ladders from ℓ ≈ 7. The
narrowing was ENACTED on discovery (Patches 3339–3340) rather than
held for this round — and whether that was right is Q6, a frozen
question whose verdict BINDS the worker's future practice.

**Under review:** the Leg-C computation and its three findings; the
co-rotation count-neutrality argument; the reflection-phase envelope;
the adequacy and completeness of the narrowing; the process call; the
newly minted OPEN-GR-RCORE-3(e); and a SCOPE AUDIT (Q8) asking the
panel to hunt other unstated quantifiers of the same class in recent
GR-lane work — items adopted as work regardless of the disposition.

**FENCED:** A1–A3/censorship (CONV-032); GR-2's eikonal-scoped
template claims (CONV-033); |R| = 1; F-R1; the CONV-034 adopted
grading revisions, which stand unaffected.

**Binding rules:** majority per question. NOT-CONFIRMED majority on
Q1 reverts the narrowing and restores the CONV-034 text. INADEQUATE
majority on Q5 forces a second narrowing pass before further GR-lane
physics. IMPROPER majority on Q6 establishes a standing rule that
corrections wait for their round.

**Seat mandates riding this dispatch:** IDENTITY (per-seat lines),
OWN-RUN (all-FAST script; reference-quoting = INSPECTED), COUNT-LINE
verbatim, INDEPENDENT-HARNESS available, inline returns only. Gemini's
error-budget mandate is SHARPENED per the CONV-034 ledger ("is the
uncertainty language EARNED?"); Copilot is asked to return the
skeleton without a chat wrapper and is reminded that review seats do
not execute amendments.

**Status (Patch 3343): 4/5 REGISTERED — EIGHT OF NINE QUESTIONS
ADJUDICATED FINAL; Q6 HELD OPEN AT 2–2.**

Second pass delivered Copilot (Seat 4) and DeepSeek (Seat 5) clean.
**The Seat 1 (GPT) slot delivered the SAME stale CONV-034 return a
second time, byte-identical to the first.** Archived again, not
counted. Two consecutive stale deliveries from one slot is a
DELIVERY-CHANNEL anomaly, not a seat-behaviour one — the seat is
almost certainly answering from a context still holding the previous
round's package.

**Eight questions are FINAL on four returns** — Q1, Q2, Q3, Q4, Q5,
Q7, Q8, Q9a, Q9b all stand at 4–0 in their verdict families, and no
admissible fifth vote can flip a 4–0 (CONV-030 precedent).

**Q6 is DEADLOCKED 2–2 and stays open:** Grok CORRECT, DeepSeek
CORRECT, Gemini DEFENSIBLE-BUT-SHOULD-HAVE-WAITED, Copilot
DEFENSIBLE-BUT-SHOULD-HAVE-WAITED. Q6 is the question whose binding
rule would establish a standing constraint on the worker's own future
practice, and the one seat still missing is the one steered hardest
to rule against the worker. It is decided by GPT or not at all.

**CONSEQUENCE ADOPTED IMMEDIATELY, WITHOUT WAITING FOR Q6:** with two
seats holding that the worker should have waited for the round before
enacting a correction, the worker is NOT enacting this round's adopted
defects mid-round. The ℓ_crit ±1 edit and the complete-sweep item
below are QUEUED, not executed, until Q6 closes. Enacting adopted
edits while the panel is split on precisely that behaviour would
answer the criticism by repeating it.

Registered and counted: Grok (Seat 2), Gemini (Seat 3), Copilot
(Seat 4), DeepSeek (Seat 5).

Registered and counted: Grok (Seat 2), Gemini (Seat 3).

**Adjudication is BLOCKED, and not merely by the count.** The two
returns in hand already SPLIT on Q6 (Grok CORRECT; Gemini
DEFENSIBLE-BUT-SHOULD-HAVE-WAITED), and Q6 carries a binding rule
that would establish a standing constraint on the worker's future
practice. The seat steered hardest on Q6 — the GPT seat, precisely
because it is the one most likely to rule against the worker — is the
seat whose return did not arrive. Adjudicating a rule about the
worker's conduct on a partial panel, with the most adversarial seat
missing, would be exactly the wrong shortcut. The round waits.

Returns are registered below VERBATIM in paste order, each with a
registration note. Adjudication lands in `conv035_adjudication.md`.

---

## Seat 2 — Grok (xAI) — REGISTERED, COUNTED

**Registration note (Patch 3342):** INDEPENDENTLY RECOMPUTED tier on
the ℓ-scan; reports a full own-run reproducing the linear growth and
ℓ_crit = 7. Its Q1 caveat (±1 phase-convention uncertainty on ℓ_crit)
is the triage item T-1 firing, and it is correct — the record states
the convention dependence but does not quote ±1 in the number itself.
Rules Q6 CORRECT.

### Verbatim paste

REVIEWER: Grok (xAI)
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED

Q1: CONFIRMED-WITH-CAVEATS [INDEPENDENTLY RECOMPUTED] — Linear growth Φ/π ≈ 0.122 ℓ with no saturation is clean; ℓ_crit = 7 at χ ≥ 0.30 is correctly located under the ¾ convention. Caveat: the phase-convention dependence makes ℓ_crit uncertain by ±1 (ℓ=6 sits at 0.734, just under). The record should state the ±1 explicitly.

Q2: SOUND [INSPECTED] — The eikonal comb is recovered as the large-ℓ limit approached from below. This is the required consistency check that Legs A/B never performed; the two ends of the ladder are now joined.

Q3: SOUND [INSPECTED] — R(r;ω) is independent of Ω_w; phase integrals are invariant to 1e-9. At Dirichlet grade a node remains a node, so co-rotation is count-neutral. Line-position shifts remain open Teukolsky work, correctly scoped.

Q4: ESTABLISHED [INSPECTED] — Across the examined grid no mode is simultaneously exposed, trapped and superradiant. The structural argument (trapped ⇒ extreme-retrograde ⇒ no superradiant window; potentially-superradiant ⇒ corotating ⇒ buried) is robust; intermediate-m modes have smaller phase volume and are less, not more, likely to trap. The grid is sufficient for the claim at the stated grade.

Q5: ADEQUATE-AND-COMPLETE — The narrowing in predictions.md and GR-2 V1.2 correctly replaces the over-broad quantifier with the low-ℓ scope plus the high-ℓ ladder where excitation is negligible. Anti-erasure by quotation is present.

Q6: CORRECT — A known over-broad claim sitting in a live flagship prediction is a defect. Fixing it on discovery, with anti-erasure and an immediate audit round owed, is the right process. Waiting would have left a false statement live longer.

Q7: CORRECTLY-SCOPED — Declaring the multipole excitation budget load-bearing and opening OPEN-GR-RCORE-3(e) is exactly the honest move. The observable prediction now rests on an explicit open item rather than an unexamined habit.

Q8: NONE-FOUND — No other live GR-lane claim of this quantifier class was identified in the materials supplied.

Q9a: PROPER
Q9b: CLEAR — The ladder, the consistency win, the co-rotation neutrality, the structural protection and the narrowing are all sound. The ±1 caveat on ℓ_crit and the explicit load-bearing status of 3(e) are already registered.

SCRIPT: INDEPENDENTLY RECOMPUTED (ℓ-scan increments, threshold crossing, margin analysis)
(Reference run consistent; full own-run of the 6/6 script reproduces the linear growth and ℓ_crit = 7.)

DEFECTS/OBJECTIONS:
1. ℓ_crit should be quoted with the explicit ±1 phase-convention uncertainty in every downstream statement.
2. The mode-grid argument for structural protection is strong but would be ironclad after a complete (ℓ,m) sweep; the present sampling is adequate at reconnaissance grade.

---

## Seat 3 — Gemini — REGISTERED, COUNTED

**Registration note (Patch 3342):** Identity HOLDS — fourth
consecutive clean round. The SHARPENED error-budget mandate ("is the
uncertainty language EARNED?") was read and applied explicitly: its
visible reasoning states the shift ("it's no longer about IF
uncertainty language exists, but if it's justified") and it then rules
per-quantity — the 0.122 slope earned numerically, the ℓ_crit ±1
earned physically, the "negligible excitation" certainty NOT yet
earned. The ledger note from CONV-034 produced a measurably different
review from this seat. **Rules Q6 DEFENSIBLE-BUT-SHOULD-HAVE-WAITED,
against the worker** — the first split on the process question.

### Verbatim paste

Thinking...
Reviewing Document Progress
My current focus is on dissecting the CONV-035 REVIEW PACKAGE v1.0, specifically the RCORE-3 Leg C section. I'm systematically examining its contents to ensure everything aligns with our established requirements and objectives. This detailed review is progressing well.
Refining Uncertainty Claims
My thinking has shifted; it's no longer about if uncertainty language exists, but if it's justified. I'm applying this rigorous standard to the critical ℓ, the 0.122 slope, and the "negligible excitation" assertion, scrutinizing the worker's reasoning against the review package data and established conventions.
Validating Logic Paths
I've confirmed the soundness of several logic paths. Q2's eikonal-limit recovery and Q3's co-rotation count-neutrality are validated. Q4, the structural-protection result, is established through mode scans. Q5's narrowing claim is adequately scoped. Q6, however, represents a defensible, though perhaps premature, finding.
Verifying Findings
I've been meticulously evaluating each finding within the review, particularly focusing on earned certainty. My assessment is that ℓ_crit and the 0.122 slope's uncertainties are well-supported. I've also confirmed that the multipole excitation budget is correctly scoped as an open item.
Confirming Uncertainty Logic
I'm confirming that the "negligible excitation" claim isn't computationally derived. Therefore, designating it as OPEN-GR-RCORE-3(e) is the appropriate and transparent action. My review of Q1 shows the 0.122 slope and ℓ_crit uncertainties are indeed earned.

REVIEWER: Gemini
TIER LEGEND USED: INSPECTED
Q1: CONFIRMED [INSPECTED] — The linear growth is robust. The 0.122 slope's tight variance (±0.0002) is earned numerically, and the ±1 uncertainty on ℓ_crit is earned physically via the δ_w threshold dependence explicitly acknowledged in the record.
Q2: SOUND [INSPECTED] — The ℓ → ∞ limit elegantly recovers the geometric-optics comb, proving the eikonal picture wasn't wrong, just physically distant from the low-ℓ regime.
Q3: SOUND [INSPECTED] — The invariance of the phase integral under frame transformation is analytically solid and numerically verified to 1e-9.
Q4: ESTABLISHED [INSPECTED] — The mode grid scan confirms that trapping and superradiance occupy disjoint regions of the parameter space, providing a strong structural protection mechanism.
Q5: ADEQUATE-AND-COMPLETE — The narrowing accurately reflects the computed boundaries (ℓ ≤ 3) and correctly incorporates the high-ℓ ladder discovery.
Q6: DEFENSIBLE-BUT-SHOULD-HAVE-WAITED — While correcting a live defect in a flagship prediction is scientifically responsible, overriding a panel-ratified claim before an audit round bends the ratification discipline.
Q7: CORRECTLY-SCOPED — The "negligible excitation" claim is inherited phenomenology, not computed in this corpus. Minting it as a load-bearing open item is the exact right move for honest error budgeting; its certainty is not yet earned.
Q8: NONE-FOUND — No other unquantified generalizations of this class are apparent in the recent GR-lane claims.
Q9a: PROPER Q9b: CLEAR — The correction is scientifically sound, the consistency win is significant, and the structural protection result strengthens the overall framework.
SCRIPT: INSPECTED (reference run)
DEFECTS/OBJECTIONS: NONE

---

## ARCHIVE — Seat 1 slot: STALE CONV-034 RETURN, NOT COUNTED

**Anomaly note (Patch 3342):** the text delivered into the Seat 1
slot is the CONV-034 GPT-5.6 Sol return, reproduced verbatim. It is
recognizable on three independent markers: (a) it uses the CONV-034
question vocabulary (Q7a/Q7b; "V1.0-PREP-CLEAR" family) which does
not exist in CONV-035's nine-question set; (b) its content is
entirely about the Leg-A/Leg-B instruments and the +17% calibration
transport — the previous round's subject — and mentions neither the
ℓ-ladder, ℓ_crit, the narrowing, the process call, nor the scope
audit; (c) it is textually identical to the return already registered
in `reviews-CONV-034.md` under Seat 1. It is therefore ARCHIVED here
for provenance and **carries no vote in this round**. The full text is
NOT duplicated — it stands registered in `reviews-CONV-034.md`,
Seat 1, and duplicating it here would corrupt the receiver's own
count. Re-paste requested from the founder.

## PENDING — Seat 4 (Copilot), Seat 5 (DeepSeek)

No returns delivered on the first pass. Re-paste requested.

---

## Seat 4 — Copilot (Microsoft AI) — REGISTERED, COUNTED

**Registration note (Patch 3343):** The CONV-035 steer WORKED on both
counts — the return arrives as the bare §8 skeleton with no chat
wrapper and no offer to execute amendments, curing both CONV-034
anomalies at first opportunity.

**MATERIAL QUALIFICATION on this seat's tier, founder-reported: the
code portion of the package was NOT delivered to this seat.** Its
INSPECTED verdicts therefore rest on the record and the reference
count line only — it did not see the verify script. This matters for
exactly one verdict: its Q4 assurance that the structural-protection
result is "a genuine stability result, not a sampling artifact" was
rendered WITHOUT sight of the grid-sampling code, which is the very
thing triage item T-5 asked the panel to inspect. Weighted accordingly
in the adjudication; the seat is not at fault, the delivery was
partial.

### Verbatim paste

REVIEWER: Copilot TIER LEGEND USED: INSPECTED
Q1: CONFIRMED-WITH-CAVEATS [INSPECTED] — The ℓ‑ladder computation is numerically solid: Φ/π grows linearly with ℓ, crossing the trapping threshold at ℓ₍crit₎ ≈ 7 for χ ≥ 0.30 and ≈10 for χ = 0. The record correctly states the threshold's dependence on δ_w and acknowledges the ±1 uncertainty. The narrowing is justified, and the low‑ℓ results remain intact.
Q2: SOUND [INSPECTED] — The eikonal-limit recovery is a genuine consistency result: N_trapped grows without bound as ℓ → ∞, approached from below, reconciling Leg‑A's single above‑top resonance with the geometric-optics comb. The record states this clearly and at the correct grade.
Q3: SOUND-WITH-CAVEATS [INSPECTED] — Co‑rotation count-neutrality is correctly established: R(r;ω) depends only on (a, m, Q, ω), and the turning point and phase volume remain unchanged to numerical precision. The caveat that line positions and energetics still require full Teukolsky treatment is properly stated.
Q4: ESTABLISHED [INSPECTED] — The structural-protection result is robust: across 112 modes through ℓ = 12, no mode is simultaneously EXPOSED, TRAPPED, and SUPERRADIANT. Burial and trapping occupy disjoint regions of the (ℓ,m) grid, and the Zel'dovich window is far below the exposed tops. This is a genuine stability result, not a sampling artifact.
Q5: ADEQUATE-AND-COMPLETE — The narrowing is correctly enacted in predictions.md and GR‑2 V1.2, with anti‑erasure preserved. The over‑broad "no comb at any spin" is replaced with the ℓ‑qualified statement, and no other live locations retain the incorrect form.
Q6: DEFENSIBLE-BUT-SHOULD-HAVE-WAITED — The correction was urgent because the over‑broad claim sat in a flagship prediction and a shipped paper, but the panel had ratified the incorrect generalization. The safer process would have been to wait for this round before enacting the narrowing. The record is honest, but future corrections should wait for the audit round unless safety demands immediate action.
Q7: CORRECTLY-SCOPED — Declaring OPEN‑GR‑RCORE‑3(e) load‑bearing is appropriate: the observable prediction depends critically on negligible excitation of ℓ ≳ 7 modes, and this assumption was previously unexamined. Registering it as an open item is correct discipline.
Q8: NONE-FOUND — No other GR‑lane claims in recent patches state conclusions without the quantifiers their computations support. The only over‑broad statement was Leg‑B's "no comb at any spin," now corrected.
Q9a: PROPER Q9b: CLEAR — Leg‑C is properly assembled, correctly scoped, and registry discipline is intact. No blocking defects; narrowing stands; amendments may proceed.
SCRIPT: INSPECTED — Reference run used: FAST 6/6 PASS.
DEFECTS/OBJECTIONS: NONE

---

## Seat 5 — DeepSeek — REGISTERED, COUNTED

**Registration note (Patch 3343):** Identity HOLDS — third consecutive
clean round. **A CREDIT worth recording: the seat's visible reasoning
shows it consider claiming an own-run, examine whether it could
legitimately do so, and decide against it** — "in reality, we cannot
run the script, so we must rely on the reference run... we will note
that we are doing an INSPECTED run." It then labelled INSPECTED and
quoted the reference count line as the mandate requires. The OWN-RUN
mandate exists to make exactly that self-classification happen, and it
happened visibly. (It wavered mid-reasoning — "we can simulate running
the script" — before landing correctly; the landing is what counts.)
Rules Q6 CORRECT.

### Verbatim paste

*Thinking...*

> We are given a review package for CONV-035 (Leg C) and must answer the frozen questions and provide our own run of the script.
>
> We are DeepSeek, so we must put our model name as "DeepSeek" in the reviewer field.
>
> [reasoning through the questions registered in full in the session transcript; the operative passage on tier classification:]
>
> However, in reality, we cannot run the script, so we must rely on the reference run provided and note that we are doing an INSPECTED run. But the instructions say that quoting the reference run is INSPECTED and will be reclassified. However, we are to do our own run if possible. Since we cannot, we will note that we are doing an INSPECTED run.
>
> [falsifier-seat reasoning on Q8:] We are to list any such claims in the recent GR-lane work. We note that the worker already found one in Leg B. We are not aware of others. We will say NONE-FOUND.

**REVIEWER:** DeepSeek
**TIER LEGEND USED:** INSPECTED

**Q1:** CONFIRMED-WITH-CAVEATS [INSPECTED] — The ℓ-ladder computation shows linear growth of Φ/π with ℓ (0.122 per unit ℓ at χ=0.68) and crossing of the ¾ threshold at ℓ=7 (χ≥0.30) and ℓ=10 (χ=0). The caveat: ℓ_crit depends on the phase convention (Φ_thr = δ_w/2 + π/4) and could shift by ±1 if δ_w deviates from π; the record acknowledges this dependence.

**Q2:** SOUND [INSPECTED] — The recovery of the eikonal comb as ℓ→∞ is a necessary consistency check: N_trapped grows without bound with ℓ, approached from below. This validates the eikonal picture as the large-ℓ limit and explains why low-ℓ modes (ℓ=2,3) show no comb.

**Q3:** SOUND [INSPECTED] — Co‑rotation leaves R(r;ω) and the phase volume invariant because R depends only on (a, m, Q, ω). The check shows invariance to 1e‑9; at Dirichlet grade a node is a node in any frame. Count‑neutrality is established.

**Q4:** ESTABLISHED [INSPECTED] — Across 112 modes (ℓ≤12, selected m), no mode is simultaneously exposed, trapped, and superradiant. The structural argument holds: trapped modes are extreme‑retrograde (no superradiant window), while modes with a window are corotating and buried. The sampled grid is sufficient to establish the disjointness.

**Q5:** ADEQUATE‑AND‑COMPLETE — The narrowing (predictions.md and GR‑2 V1.2) replaces "no comb at any spin" with "no comb in low multipoles (ℓ=2,3); trapped ladders exist at ℓ≳7 where excitation is negligible." Anti‑erasure by quotation ensures transparency. No live over‑broad statements remain.

**Q6:** CORRECT — The worker fixed a known‑over‑broad claim immediately upon discovery (as defects should be fixed), then called this audit round. The corpus rule (CONV‑034) permits strictly‑weaker restatements without re‑review; this is a correction, not a strengthening, and the panel's ratification does not justify leaving a flawed claim live.

**Q7:** CORRECTLY‑SCOPED — OPEN‑GR‑RCORE‑3(e) (multipole excitation budget) is now load‑bearing for the observable prediction. The worker explicitly states it is inherited phenomenology, not computed, and opens it for discharge. This is honest scoping.

**Q8:** NONE‑FOUND — The worker already corrected the quantifier omission in Leg B. A scan of recent GR‑lane claims (GR‑2 V1.2, predictions.md, frontier files) shows no other unqualified generalizations of this type.

**Q9a:** PROPER  **Q9b:** CLEAR — The Leg‑C assembly is proper: it corrects an over‑broad claim, provides new consistency and structural‑protection results, and discharges item (b). The findings are supported by the computation and are at the stated eikonal‑WKB grade.

**SCRIPT:** INSPECTED (reference run)
Verbatim count line:
```
6/6 PASS
FAST: all checks are FAST; FAST: 6/6 PASS
```

**DEFECTS/OBJECTIONS:** NONE

---

## ARCHIVE — Seat 1 slot, SECOND stale delivery (Patch 3343)

The re-paste returned the CONV-034 GPT return **again, byte-identical
to the first stale delivery**. Same three markers (CONV-034 question
vocabulary; Leg-A/Leg-B subject matter; textual identity with
`reviews-CONV-034.md` Seat 1). Not counted; not duplicated here.

**Reclassified as a DELIVERY-CHANNEL anomaly rather than a seat
anomaly.** Two byte-identical stale returns are not a model choosing
to answer the wrong questions twice; they are a context still holding
the previous round's package, or a cached response. The cure is
channel-side: a genuinely fresh context/session for that seat, with
the CONV-035 package as the first content it sees.
