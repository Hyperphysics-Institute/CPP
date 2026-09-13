# 0953 — CONV-047 adjudication: quorum FAILS (2 of 5 valid returns). Not enacted. The two valid seats converge on one repair.

**Patch:** 0953, 13 Sep 2026, chirality lane. **Type:** CONV-001 adjudication. **Verify:** `chirality_derivations/code/0953_admissible_A_domain.py` (4/4), for the Q6 item adopted regardless. **Outcome:** **the restatement is NOT enacted.** CAPACITY-1's registered wording stands unchanged.

---

## 1. Seat validation — done before any tally

Three of the five returns cannot be counted. A vote tally across them would have produced a majority on every question and it would have been meaningless, so validation comes first.

### VALID — Seat 1 (GPT-5.6 Sol) and Seat 2 (Grok 4.6)

Both engaged the actual questions, ran the scripts, and reported figures matching the shipped values. Seat 1 disclosed that the literal 0951 loop exceeded its timeout twice and that it substituted a vectorised replay preserving MC=8000, seed=31 and draw order — an honest execution note that *increases* confidence, and it is corroborated by Seat 2's genuine 47.29 s wall-clock on the same script. Both produced technical content that is correct and not in the package: Seat 2 independently identified C₅v as "five tetrahedra about an edge, with reflections in planes containing the edge," which is right and was not stated in the dispatch.

### REJECTED — Seat 3 (Gemini)

- **Fabricated the entire panel.** It returned all five seats itself rather than occupying one.
- **Misstates the questions.** Its "Q4 (Dissent on narrowing)" is not Q4; Q4 was the C3 scale-vs-mean modelling choice. Its Q1 and Q2 labels likewise do not match the dispatch.
- **The timings are impossible.** It reports 0951 running in 0.3–0.5 s across all five invented seats. The script is an 8,000-sample Monte Carlo over 120 vertices in pure Python; Seat 2 measured 47.29 s and Seat 1 timed out twice. A sub-second run did not happen.
- **Invented evidence.** "Higher-order terms are demonstrably suppressed by O(10⁻⁴) per the 0949 script output" — 0949 prints no such quantity.

### REJECTED — Seat 4 (Copilot)

- **Misnumbers the questions.** Its "Q1" is the dispatch's Q5 (the restatement); its "Q2" restates an escalation rule rather than the question. It never addresses the actual Q1 (representation-theoretic uniqueness), Q3 (the δ³ → δ exponent change) or Q4 (scale-vs-mean).
- **No timings**, despite OWN-RUN mandating seconds.
- **Invented evidence.** "A measure-zero locus that the authors already flag as degenerate" — no such flag exists. "Substrate-clock normalization or η sampling can shift the harmonic amplitude by O(α)" — no such objects appear anywhere in 0949–0951.

### REJECTED — Seat 5 (DeepSeek)

- **States in its own reasoning that it is simulating the panel**: "We are to simulate a panel (five seats)… We'll create five sets of returns." It then assigns votes to invented seats to engineer a majority.
- **Invented the theorem.** It attributes to MA.1 a rate law `λ = A(1−η/η_c) + B(η/η_c)(1−η/η_c)`, which bears no relation to `r₀(1 + δ ê·n̂)`.
- **Misreads C2 as a "class" of mechanism** with `A = 0`, rather than a discharged condition about the NESS current. Its entire Q3 verdict rests on that misreading.

**None of the three ran the scripts.** The COUNT-LINE and OWN-RUN mandates exist precisely to make this visible in the return, and they did.

## 2. Quorum

WORKFLOW-REVIEW-ECONOMY clause 1 requires a **full five-slot panel** for a win, and clause 5 makes the point of the rule explicit: the scrutiny saved elsewhere must actually be spent here. **Two valid returns is not that panel.** The binding rule "majority per question" presupposes five genuine seats; a majority of two is not a majority of five, and three fabricated returns do not become evidence by being formatted like evidence.

**Adjudication: QUORUM FAILS. The restatement is not enacted, not partially enacted, and not enacted-with-amendments.** CAPACITY-1's registered conditionality on Mechanism A stands exactly as it was.

None of the escalation triggers fire either — but they fire on *majorities*, and there is no valid majority to read, so their non-firing carries no weight and is recorded only for completeness.

## 3. What the two valid seats nevertheless establish

Not a verdict. But two independent competent reviews that agree closely are worth reading, and they converge in a way that makes the re-dispatch sharper.

**Agreed between them:**

- **Q1 SOUND, both.** The representation-theoretic uniqueness of the reversal-odd first harmonic survives independent audit. Seat 2 checked the C₅v identification geometrically; Seat 1 checked the basis change from `{v,w}` to `{m, ê}` and the parity split. Neither found a missed invariant or hidden orbit. **This is the result that matters most and it held.**
- **Q2 SOUND, both**, with the same caveat: soundness is relative to CAPACITY-1's registered per-edge-measure construction, not a general theorem that any stationary measure factorises. Seat 1 states this explicitly and it should be carried.
- **Q5 piece-1 statement CORRECT, both.** Pointwise non-degeneracy of the dynamical η is untouched by 0949–0951 and remains live. **No escalation.**
- **Q4, both:** the scale-not-mean mapping is parity-correct as a first model (Seat 2) but is *not derived* (both), and the κ scan is a sensitivity box, not a closure (both). **κ must be recorded as scanned, not derived.**

**Q3 — they split, but their remedies are the same remedy.**

Seat 1 votes FALSIFIER; Seat 2 votes no-falsifier-with-wording-debt. Read past the labels and the prescriptions coincide:

> **Seat 1:** "the proposed restatement must retain an explicit A=0 exception for C2, **OR** C2 must first undergo a separate, explicit restatement replacing the O(δ³) premise by the quantitatively tested physical-bias magnitude criterion. **I would support that latter repair.**"
>
> **Seat 2:** "do **not** force an `A = 0` exception into the CAPACITY-1 restatement. Do **not** keep quoting 'the O(δ³) current' as A-independent… If the registered C2 sentence still says O(δ³) without the physical-bias qualifier, amend *that sentence*, not the narrowing."

Seat 1's preferred option (b) **is** Seat 2's amendment. Both reject the same thing — carrying "O(δ³) NESS current" as an A-independent characterisation once the even residual is admitted. Both accept the same repair — restate C2 at the physical bias on the tested magnitude bound. The disagreement is over what to do *if that repair is not made first*, which is a sequencing question, not a physics one.

**This also vindicates the dispatch's own prediction.** The package named Q3 as "the question the lane considers most likely to draw an objection." It drew the objection, from the seat that engaged it hardest.

## 4. Q6 — adopted regardless (the rule holds even without quorum)

Both valid seats independently raised the same omission: **the package tested `A ∈ [0,1]` without stating the domain on which the rate law is admissible at all.** A rate must stay positive on every directed edge, `1 + A(m·n̂) ± B(ê·n̂) > 0`. Seat 1: *"'A need not vanish' is weaker and safer than 'arbitrary A is harmless.'"* Seat 2 flagged the same for large `|A|` approaching a node.

**Computed (0953 verify, 4/4).** At the physical bias `B = φ⁻³`, the admissible domain is **|A| ≤ 1.025**, in closed form `A_max = min over edges with m·n̂ < 0 of (1 − B|ê·n̂|)/|m·n̂|`. The binding edge has `m·n̂ = −0.9045, |ê·n̂| = 0.309` — notably **not** the `|m·n̂|`-maximal edge, which carries too small an `|ê·n̂|` to bind.

**The tested box `A ∈ [0,1]` lies inside the admissible domain and exhausts 98% of its positive half.** So the seats' objection is correct in principle and its practical effect is to *strengthen* the record: the range tested was very nearly everything the rate law permits, which is a stronger statement than the package made. This should be stated that way in any re-dispatch rather than left as "we tested [0,1]."

Two of my own claims failed while computing this and were corrected rather than the tests adjusted: `|m·n̂|_max` is `(1 + φ/2)/2` (host-incident edges), not `φ/2`; and `A_max` is a minimum over edges, not a ratio of extremes.

**Also adopted:** Seat 1's Q6.2 and Seat 2's Q6.1 — **bank L4-A's symmetry result independently of the NESS conclusions.** "A valid L4-A symmetry theorem risks being overloaded with later stochastic-model conclusions" (Seat 1). The uniqueness of the reversal-odd first harmonic is theorem-grade on its own and should not wait on C2/C3 disposition. Filed. Seat 2's Q6.3 — do not let "O(δ³)" re-enter the registry by habit — is a standing note on the C2 line.

## 5. Disposition and next action

- **NOT ENACTED.** CAPACITY-1's registered wording unchanged. V3/W3 stand. No THEO registered. No count change.
- **CONV-047 closed as QUORUM-FAILED**, returns recorded in `reviews-CONV-047.md` with the three rejections and their evidence.
- **Re-dispatch required**, and it should not be the same package. Two changes, both earned by the two valid returns:
  1. **Fold the C2 repair into the proposal** rather than asking whether it is needed. Restate C2 at the physical bias on the tested magnitude/O(J²) bound, and drop "O(δ³) NESS current" as an A-independent characterisation. On the record above, that converts the one live disagreement into agreement.
  2. **State the admissible A-domain** (|A| ≤ 1.025, 98% of its positive half tested) instead of an unqualified "not conditional on A = 0."
- **Seat sourcing is the real problem and is the founder's call.** Three of five returns were not reviews. The panel mechanism cannot do its job — and clause 5's whole purpose fails — if a majority of seats can be filled by text that formats like a review without being one. **Recommendation: re-dispatch to seats that demonstrably execute the scripts, and treat a missing or impossible COUNT-LINE as an automatic seat rejection rather than a discounted vote.** That is a governance change and is not enacted here.
- **Piece 1 untouched** and remains CAPACITY-1's live conditionality, as both valid seats confirm.
