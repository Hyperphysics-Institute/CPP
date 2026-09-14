# 0959 — Resolving the review-turn count: the final round drops from five seats to two, and the lane takes the cause

**Patch:** 0959, 13 Sep 2026. **Lane:** chirality (09xx). **Founder instruction, 13 Sep:** *"please resolve the number of review turns reasonably. Nine turns is a lot of effort for me."*

---

## 1. Where the nine turns actually came from

Not from the panel. **Every round, the reviewers confirmed and the lane found a new error in its own document.**

| round | reviewer outcome | what forced the next round |
|---|---|---|
| CONV-047 dispatch → adjudication | 2 valid seats, both SOUND on Q1 | 3 seats were non-reviews; package unanswerable from cold |
| reformat → CONV-048 | 3 returns, all ENACT | lane found negative-A untested, second harmonic unidentified |
| addendum → returns | 5/5, GPT withdrew its falsifier | lane found domain not a rectangle, margin overstated, stacking superadditive |

**Three of the four substantive findings came from reviewers — but every *correction to the lane's own text* came from the lane, after dispatch.** The negative-A sweep, the second-order parity check, the joint corner and the positivity recomputation were all cheap, all runnable before dispatch, and all run afterwards. The lane used the founder's dispatch cycles as its debugging loop. **That is the cause, and it is the lane's, not the panel's.**

The asymmetry is the point: an extra round costs the lane a few minutes of compute and costs the founder a full manual dispatch to five seats plus collection. **Treating rigour as free is only possible for the party that isn't paying.**

## 2. Resolving the current campaign: two seats, not five

The final round of Patch 0958 is **reduced from five seats to two**, on the following reasoning rather than on cost alone.

**Three seats' conditions are already satisfied verbatim by the corrections**, so asking them again would be asking a question already answered:

- **Copilot** listed five required edits (C2 numeric worst-case bound; negative-A results; odd-second-order appendix; combined worst-case statement; registry language limited to tested scales). **All five are now in the corrected text** — §A3 supplies the combined bound by scale, the negative-A sweep, and the odd-channel appendix; Part 2 limits the narrowing to tested scales.
- **DeepSeek** required retiring "order δ³", stating the full admissible range tested, naming the odd channel as an open residual, and clarifying that only the first-order odd term is derived. **All four are in.**
- **Gemini** endorsed the disposition and required no edits beyond what is now written.

**Two seats' stated reasoning leaned on a number the joint corner changed**, and they are the two who demanded that corner:

- **GPT** conditioned its withdrawal on the margin: *"Both hostile perturbations remain roughly five or more orders down in the squared-current quantity."* That is now false in the extended regime (~two orders). Its condition was stated against a figure that has moved.
- **Grok** demanded the joint corner and **predicted** it would be additive-in-amplitude. It is superadditive. He also wrote *"that is not enough to flip Q3 into a falsifier"* in advance — but he was reasoning about a case he had not seen.

**So the round goes to GPT and Grok only.** One question each. This is not a cost-driven truncation: it is the observation that only two reviewers' reasoning touches the new finding, and the other three set conditions the corrected text meets.

## 3. Standing rule, enacted now

Two changes, so this does not recur. Both are in the lane's own discipline, not the founder's workload.

**R-1 — The lane runs the hostile pass BEFORE dispatch.** Before any CONV-001 dispatch, the lane must run the tests it would expect an adversarial reviewer to demand: boundary and sign-flipped cases of every free parameter, every parameter *jointly* rather than one at a time, the admissibility domain of the full parameter set rather than one slice, and the next order of any expansion it proposes to truncate. **Had these four been run before CONV-047, the negative-A gap, the odd second harmonic, the non-rectangular domain and the superadditive corner would all have been in the first package.** The reviewers would still have found what they found; the lane would not have spent four of the founder's dispatch cycles correcting itself.

**R-2 — Two dispatches per claim, then a decision.** A claim gets at most **two** full dispatch cycles. If it is not adjudicable after the second, the lane either enacts on the reviewers' stated conditions where the text demonstrably meets them, or abandons the claim and banks whatever stands on its own. A third full dispatch requires an explicit founder decision, made knowing it is a third. Confirmation rounds targeted at named seats whose specific reasoning has been disturbed are not full dispatches and do not count against the two.

**Recorded against the lane, not the panel:** the panel's cost-effectiveness in this campaign was high — three of four findings, and one withdrawn falsifier. The inefficiency was entirely upstream of it.

## 4. Disposition

- **CONV-048 final round: 2 seats (GPT, Grok), one question, per `0958_conv048_final_round.md` unchanged.** The stop rule in that document stands as written.
- **Three seats (Gemini, Copilot, DeepSeek) are not re-asked.** Their conditions are met verbatim by the corrected text and their verdicts carry. Recorded here so adjudication does not read their absence as non-response.
- **R-1 and R-2 enacted** as lane discipline; proposed for the CONV-001 dispatch template generally, which is a governance item for a separate window, not this one.
- **No verdict moves. CAPACITY-1's registered conditionality stands.**
