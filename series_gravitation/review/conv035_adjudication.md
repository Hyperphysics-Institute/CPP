# CONV-035 adjudication — PARTIAL-FINAL v1.0 (Patch 3343)

**Round:** RCORE-3 Leg C, and the narrowing of a claim this panel
ratified at CONV-034. Package
`conv035_legC_narrowing_review_package_v1.0.md`; receiver
`reviews-CONV-035.md`, **4/5 registered** (Seat 1 slot delivered the
CONV-034 return twice, byte-identical; archived, not counted).

**Headline: the Leg-C physics clears 4–0 on every question — and the
one question about the WORKER is deadlocked 2–2 and stays open.**

---

## §1 Tally — eight questions FINAL, one HELD

| Q | Verdict | Tally | Status |
|---|---|---|---|
| Q1 ℓ-ladder / ℓ_crit | **CONFIRMED-WITH-CAVEATS** | CONFIRMED-family 4–0 (3 with-caveats, 1 clean) | **FINAL.** Caveat unanimous in substance: ℓ_crit carries ±1 phase-convention uncertainty. |
| Q2 eikonal-limit recovery | **SOUND** | 4–0 | **FINAL.** No seat took the OVERREAD option offered against the worker's most flattering claim. |
| Q3 co-rotation count-neutrality | **SOUND** | SOUND-family 4–0 (1 with-caveats) | **FINAL.** Item (b) discharged for the count. |
| Q4 structural protection | **ESTABLISHED** | 4–0 | **FINAL AT RECONNAISSANCE GRADE** — see §3 for the weighting the adjudication applies. |
| Q5 narrowing adequacy | **ADEQUATE-AND-COMPLETE** | 4–0 | **FINAL.** |
| **Q6 the process call** | **DEADLOCKED** | CORRECT 2 (Grok, DeepSeek) / DEFENSIBLE-BUT-SHOULD-HAVE-WAITED 2 (Gemini, Copilot) | **OPEN.** See §2. |
| Q7 OPEN-GR-RCORE-3(e) | **CORRECTLY-SCOPED** | 4–0 | **FINAL.** |
| Q8 scope audit | **NONE-FOUND** | 4–0 | **FINAL** — with the honest weighting in §4. |
| Q9a / Q9b | **PROPER / CLEAR** | 4–0 | **FINAL.** |

No admissible fifth vote can flip a 4–0 (CONV-030 precedent), so the
eight are closed. Q6 can be flipped by one vote and therefore cannot.

## §2 Q6 — the deadlock, and what the worker does about it

The panel split exactly down the middle on whether enacting the
narrowing before this round was CORRECT or
DEFENSIBLE-BUT-SHOULD-HAVE-WAITED. Both sides argue well. The
CORRECT side (Grok, DeepSeek): a known-over-broad claim in a live
flagship prediction is a defect, the correction was strictly weaker,
and waiting leaves a false statement live longer. The
SHOULD-HAVE-WAITED side (Gemini, Copilot): the panel had *ratified*
the claim, so overriding it pre-audit bends ratification discipline;
Copilot proposes the standing form "future corrections wait for the
audit round unless safety demands immediate action."

**The worker will not break this tie.** Q6's binding rule would
establish a standing constraint on the worker's own conduct; a 2–2
split resolved by the party under examination is not an adjudication.
The missing seat is the one steered hardest to rule against the
worker, which makes self-resolution worse, not better.

**Interim discipline adopted unilaterally, in the stricter
direction (Patch 3343):** with half the delivered panel holding that
corrections should wait, the worker is **not enacting this round's
adopted defects while the round is open.** The ℓ_crit ±1 edit (§3
item 1) and the complete-sweep item (§3 item 2) are QUEUED, not
executed. Enacting adopted edits mid-round, in a round split on
precisely that behaviour, would answer the criticism by repeating it.
This is not a concession that the original call was wrong — it is
what following the stricter reading costs while the question is
undecided, and the cost is small.

## §3 Adopted defects — QUEUED for enactment when Q6 closes

1. **ℓ_crit ±1 (Grok defect 1; Q1 caveat carried by three seats).**
   Every downstream statement of ℓ_crit quotes the ±1
   phase-convention uncertainty in the number itself, not only the
   dependence in prose. Locations: the Leg-C record §1, PRED-O-39's
   amendment note, GR-2's `rem:rcore3`, `frontier_sectors/GR.md`.
   Pre-committed at Patch 3342 as adopted regardless of how the round
   closed; that commitment stands.
2. **Complete (ℓ,m) sweep for the structural-protection result
   (Grok defect 2).** The present grid samples |m| ∈ {0,1,2,ℓ−1,ℓ} at
   selected ℓ. Grok's own words: adequate at reconnaissance grade,
   ironclad only after a complete sweep. **Q4 is therefore recorded
   as ESTABLISHED-AT-RECONNAISSANCE-GRADE**, and the full sweep is
   registered as work under OPEN-GR-RCORE-3.
   *Weighting note applied honestly:* of the four ESTABLISHED votes,
   Copilot's was rendered **without the verify script** (the code
   portion was not delivered to that seat), so its assurance that the
   result is "not a sampling artifact" cannot bear weight on
   precisely the sampling question T-5 posed; DeepSeek's was
   INSPECTED by its own honest classification; Gemini's was
   INSPECTED. **Grok alone recomputed independently — and Grok is the
   seat that asked for the complete sweep.** The unanimity is real
   but thinner than 4–0 looks, and the adjudication records that
   rather than banking it.

## §4 Q8 (scope audit) — NONE-FOUND, recorded with its limits

All four seats found no other claim carrying a quantifier its
computation does not support. The worker registers this as the
round's weakest unanimity: three of four seats worked from the record
alone, one seat lacked the script entirely, and none was given the
broader GR-lane corpus to sweep — they were given Leg C's materials
and asked about "recent GR-lane claims." **NONE-FOUND is therefore
evidence that no such claim is visible in the supplied materials, and
not evidence that none exists in the lane.** A genuine scope audit
across the eleven GR papers is registered as available work; the
worker recommends it be run before the next flagship prediction move
rather than treated as discharged by this vote.

## §5 Seat-conduct ledger

- **GPT (Seat 1):** no CONV-035 return. Two byte-identical stale
  CONV-034 deliveries ⇒ reclassified **DELIVERY-CHANNEL anomaly**,
  not seat misconduct; the cure is a genuinely fresh context. Its
  absence is materially felt: Q6 is deadlocked and Q1's ±1 caveat
  would likely have been sharpened by the seat that has led on
  grading three rounds running.
- **Grok (Seat 2):** the round's only independent recomputation, and
  the source of both adopted defects. Carries the round.
- **Gemini (Seat 3):** identity holds (fourth clean round). The
  CONV-034 mandate sharpening produced a visibly different review —
  per-quantity "earned/not earned" rulings rather than
  per-document. **A ledger note changed a seat's behaviour: the
  mechanism works.**
- **Copilot (Seat 4):** both CONV-034 anomalies CURED at first
  opportunity — bare skeleton, no chat wrapper, no offer to execute.
  Reviewed on a partial package through no fault of its own.
- **DeepSeek (Seat 5):** identity holds (third clean round).
  **Credited:** its visible reasoning shows it consider an own-run
  claim, test whether it could legitimately make one, and decide
  against it, then label INSPECTED. That is the OWN-RUN mandate
  producing honest self-classification in the open.

## §6 Disposition

Leg C's physics stands: the narrowing is adequate and complete, the
ℓ-ladder is confirmed, the eikonal-limit recovery is sound, the
co-rotation item is discharged for the count, and the
structural-protection result is established at reconnaissance grade.
**Q9b CLEAR 4–0 — the GR lane is unblocked for physics.** Two adopted
defects are queued behind Q6's resolution. Nothing else waits.

**Founder mechanical action requested:** one more delivery attempt to
the GPT seat from a genuinely fresh context. If it cannot be
obtained, Q6 closes UNRESOLVED and the worker adopts the stricter
reading (corrections wait for the round unless the claim is
actively misleading a reader) as standing practice by default —
choosing against its own prior position, because a tie should not
resolve in favour of the party who benefits from it.

## CHANGELOG

- v1.0 (Patch 3343, 21 Aug 2026): PARTIAL-FINAL at 4/5. Eight
  questions closed; Q6 held at 2–2; two defects adopted and queued;
  Q4 and Q8 unanimities recorded with their honest weightings.
