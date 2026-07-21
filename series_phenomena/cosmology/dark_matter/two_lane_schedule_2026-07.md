# Two-lane task schedule (20 July 2026) — the DM-1/2/3 release completion + the FA-SG-R1 robustness campaign, every task named, ordered, and owner-assigned

**Patch 2681. Founder directive: "It sounds like we need to do both the
FA-SG-R1 and the Release Completion Session to finish up the release of
DM-1,2,3. Schedule each task that needs to be done, and we'll do it."
Sequencing rulings below are the adjudicator's under PD-006. The lanes
are file-disjoint and independent; wall-clock parallelism is exploited
where it is free (red-team returns accumulate on the founder's channel
while sessions run). 79.5% untouched by every task on this schedule.**

## LANE B — DM-1/2/3 joint release completion (release_plan_2026-07-20.md)

| # | Task | Owner | Session | Status / gate |
|---|---|---|---|---|
| B0 | Four-seat red-team dispatch (`red_team_four_seat_dispatch_2026-07.md` paste block → Grok, Gemini, Copilot, DeepSeek) | **Founder** (paste) | none — do now | DISPATCHED this patch; returns accumulate while B1–B3 run |
| B1 | DM-2 + DM-3 deposit records (house per-paper format, `osf-deposit-DM-1.md` as template) | Worker | **RELEASE SESSION** (next dedicated session, fresh bootup) | plan item 3 |
| B2 | Reader's-guide extension — DM-2/DM-3 sections | Worker | RELEASE SESSION | plan item 4 |
| B3 | Arc-wide closing residual scan, INCLUDING the July-campaign no-touch ruling on the record (2674 rider / amended DISC block / Branch-N vs the three resting papers, grep-level consumer check; a found touch = the plan's load-bearing-correction gate fires and pauses) | Worker | RELEASE SESSION | plan item 5 |
| B4 | Adjudicate red-team returns — SECOND WAVE RECEIVED 20 July: five returns registered verbatim (2682), triaged T1–T10; KILL-class T2/T3/T5 = RELEASE SESSION agenda items 1–3 (agenda in the adjudications file §SECOND WAVE) | Worker | RELEASE SESSION | **GATE: deposit (B5–B6) PAUSED-PENDING-ADJUDICATION of T2/T3/T5** |
| B5 | Founder sign-off against the five-box checklist (+ DM-2/DM-3 analogues written at B1) | **Founder** | after B1–B4 | plan item 6; gated on B1–B3 done + all received returns adjudicated |
| B6 | Deposit execution: final PDFs, zip, the 1891 addendum, errata fold as v1.0.1 / v1.4.1 CHANGELOG entries, §§1–4 of each deposit record, DOI backfill | Worker prepares, **Founder** executes OSF upload | DEPOSIT SESSION (may be same day as B5) | plan item 7; the arc ships |

**Ruling:** the RELEASE SESSION (B1–B3, one dedicated session) runs
FIRST — the deposit date is reached, the work is paper-side and
self-contained, and running it now lets the red-team wall-clock overlap
it for free. If any four-seat return lands before or during it, B4 folds
into the same session.

## LANE A — FA-SG-R1 (the candidate-B validation queue-head)

| # | Task | Owner | Session | Status / gate |
|---|---|---|---|---|
| A1 | Execute the frozen charter (`fa_sg_r1_charter.md`, 2679): L1→L3→L2→L4, L5 on trigger; F1–F4 fence in force; concordance criteria and outcome classes as frozen; verify scripts per leg | Worker | **R1 SESSION** (its own fresh session, per the charter's frozen 2527 clause) | charter FROZEN; runs founder-free to the packet |
| A2 | Assemble the R1 CONV-001 packet (results + the [ADJ] operationalizations disclosed votable) | Worker | R1 SESSION close | every outcome class routes here |
| A3 | Dispatch the R1 packet to the five seats | **Founder** (paste) | none | after A2 |
| A4 | Adjudicate the R1 returns: grade-cap ruling on ℓ; consumer propagation; 2674-rider disposition | Worker | ADJUDICATION SESSION | after A3 returns |
| A5 | FA-C2 consumer re-derivation campaign (charter → execute) against whichever ℓ the panel sustains | Worker | subsequent sessions | sequenced BEHIND A4 per 2674 §5 / inputs §4 |

**Ruling:** the R1 SESSION runs immediately after the RELEASE SESSION
(or in parallel on a different day — the lanes never touch the same
files). Recommended order of the next three sessions:
**(1) RELEASE SESSION (B1–B3, +B4 as returns land) → (2) R1 SESSION
(A1–A2) → (3) B5/B6 deposit as soon as the received red-team set is
adjudicated clean — A3/A4 proceed on their own clock.** Standing
founder-placed items (REPL-1, promotion-on-word) are untouched by both
lanes and remain at the founder's word.

**Founder's immediate actions (today, no session needed):** (1) apply
and push this patch; (2) paste the B0 block to each of the four seats;
(3) open the next session with the word RELEASE (or R1 to reorder — the
schedule tolerates either).

---

## LANE B RE-SCOPED (Patch 2683) — the deposit is BLOCKED BY THE RECORD

The 9-July KILL banners (Patch 2369, founder-attested) in DM-1 and DM-3
— found on opening the manuscripts for the B4 adjudications — mark both
NOT-FOR-RELEASE with revision deferred behind OPEN-DM-DSPH-1 by founder
decision. **B5–B6 do not execute for the v1.4/v1.0 texts.** Superseding
rows:

| # | Task | Owner | Status |
|---|---|---|---|
| B4′ | Second-wave adjudications | Worker | **DONE at 2683** — zero confirmed KILLs; five revision-checklist additions; errata items 7–9 |
| B7 | FOUNDER DECISION: release posture — (i) hold all three behind the Candidate-(B) revision path (honest default), (ii) DM-2 standalone (no banner; joint framing dissolves), or (iii) any record-release framing the founder wants scoped | **Founder** | OPEN — the single LANE B act remaining |
| B8 | IF (i): revision checklist executes when the Candidate-(B) arc (R1 → RELIC-1 → promotion) reaches paper-revision maturity; B1–B3 deliverables (deposit records, reader's guide, ledger, scan) produce then, against the revised texts | Worker | parked behind LANE A + the validation campaigns |

LANE A (FA-SG-R1) is UNAFFECTED and remains the standing next fresh-
session act.
