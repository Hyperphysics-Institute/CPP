# CONV-013 RETURNS ADJUDICATION — PARTIAL (Patch 3020; Copilot seat pending)

**7 Aug 2026. Four returns received; verbatim archive at
`reviews/conv013_returns/` (Patch 3019). Tally-from-verbatim-only
(Patch 2986): every tally line below cites its archived document.
Citation keys: [GPT] = `s1_gpt_return.md`; [GROK] = `grok_return.md`;
[G?] = `gemini_slot_return_PROVENANCE_PENDING.md`; [DS] =
`deepseek_return.md`; [COP] = `copilot_delivery_event.md`.
Per Patch 2827, panel verdicts enact; this adjudication records and
enacts only what the tallies carry. Items whose tally could change with
the outstanding seat or the [G?] attribution are marked PROVISIONAL;
items marked FINAL cannot change under any completion of the panel.**

---

## §1 — Seats, execution status, delivery events

- **GPT: ACCEPTED** (self-declared; no execution claim, no keys) [GPT].
- **Grok: SCRIPT-EXECUTED-QUALIFIED.** Claims SCRIPT-EXECUTED with both
  keys but attaches no stdout; per the dispatch's own CONV-011 rule,
  keys-without-stdout = QUALIFIED [GROK]. Key verification in §2:
  BOTH KEYS MATCH.
- **[G?]: provenance PENDING.** Delivered by the founder in the Gemini
  slot ("Gemini 3") but self-headed "SEAT: Copilot" with "Fresh
  conversation confirmed" — the Copilot-specific re-seating condition —
  while the actual Copilot window produced the [COP] stall. Execution
  status self-declared REASONED-UNVERIFIED [G?]. **FOUNDER ACTION:
  confirm which model's window produced this return.** If Gemini:
  mislabel event #6 (registered class, ×5 prior). Tallies decided by
  this seat alone are PROVISIONAL.
- **DeepSeek: REASONED-UNVERIFIED** (self-declared) [DS]. Integrity
  event recorded in §5.
- **Copilot: DELIVERY EVENT, NO RETURN — NOT a stale redelivery; the
  third-strike clause does NOT fire.** The [COP] message replays no
  stale content; it is a confirmation stall, and it quotes a PRIOR
  unrelated message in the same window ("obey this commandment...
  biblical concept?"), establishing the paste did not land as the first
  message of a genuinely fresh conversation — a delivery-procedure
  miss, not a seat integrity event. **Remediation ruling (worker
  authority, PD-006): one clean re-paste is authorized** — a brand-new
  Copilot conversation, the single 4-backtick block as the VERY FIRST
  message, nothing before it. If Copilot again stalls for confirmation
  after a clean first-message paste, the founder replies exactly:
  "Confirmed. Proceed with full CONV-013 reviewer returns (Q1–Q5 +
  AUX-1..AUX-4) in the required format." If no return follows a clean
  paste plus that confirmation, the seat records NO-RETURN for CONV-013
  and the round completes on four seats; the stale-redelivery
  third-strike clause is not stretched beyond its text, and any
  seat-status question beyond this round routes to the arc rules.

## §2 — Withheld-key verification (Grok)

Worker recomputed both keys from the committed scripts at HEAD
(deterministic, seeded):

- **KEY-E** (|m1d|, `code/2980_b1_discrete_check.py`): computed
  1.74126535e-02 → six significant figures **1.74127e-02**. Grok
  reported 0.0174127 [GROK]. **MATCH.** Note: this is a
  rounding-boundary case — the 7-figure rendering is 1.7412654e-02, and
  naive truncation of any printed 7-figure string gives 1.74126
  (wrong). Grok's correct 1.74127 requires the underlying value.
- **KEY-F** (r[0], `code/2990_b1_stationarity_check.py`): computed
  5.92857059e-08 → six significant figures **5.92857e-08**. Grok
  reported 5.92857e-08 [GROK]. **MATCH.**
- Post-return reconstructibility re-audit: full-history pickaxe finds
  NO occurrence of either key's 6-figure OR 7-figure rendering anywhere
  in repository history (the dispatch-time disclosure of the benign
  interior-substring collision in `data/kmem2/leg_0453_ctrl_std.json`
  stands and is unrelated to any printable rendering of the key).
  **Both keys were non-reconstructible; the exact matches are decisive
  evidence of actual script execution.** Keys now published here
  post-adjudication, per the standing publish-post-adjudication
  practice.

## §3 — Tallies and rulings

### Q1 — C-5 confirmation (per clause)

- **(i) L-3′:** CONFIRM [GPT], CONFIRM [GROK], CONFIRM [G?], AMEND
  [DS: K-sweep + entireness proof]. **CONFIRM carries 3/5. FINAL**
  (a fifth-seat vote cannot remove the 3). DS's named items recorded as
  non-blocking hardening candidates.
- **(ii) L-2:** CONFIRM [GPT], CONFIRM [GROK], CONFIRM [G?],
  INSUFFICIENT [DS: full-model proof vs toy]. **CONFIRM carries 3/5.
  FINAL.** DS's full-model item recorded.
- **(iii) L-6:** CONFIRM [GROK]; AMEND-text-only [GPT: name the metric,
  the contraction map, and where strict inequality enters];
  INSUFFICIENT [G?: MEAS-2 tail undermines the structural claim];
  INSUFFICIENT [DS: rigorous κ<1 derivation missing]. **CONFIRM does
  not carry (1/5) and cannot carry with the fifth seat (max 2/5).
  C-5(iii) NOT CONFIRMED — FINAL.** Convergent named item across
  [GPT]+[DS]: an explicit contraction argument (metric, map, strict
  inequality) for κ<1. [G?]'s distinct ground is entangled with its Q3
  reading (§3 Q3 below).
- **C-5 as a package: NOT CONFIRMED this round (clause iii). FINAL.**
  The promotion bar's first half is therefore unmet independently of
  everything else.

### Q2 — T-1 v1.3 closure-scope discharge

UPHOLD [GPT, with exhaustive-within-grade wording], UPHOLD [GROK];
AMEND [DS: exhaustiveness proof at grade]; INSUFFICIENT [G?: tail
proves non-exhaustiveness]. **No 3/5; NOT carried; PROVISIONAL**
(the fifth seat could complete UPHOLD to 3). Convergent hardening item
regardless of outcome: state (or prove) the dichotomy's exhaustiveness
explicitly at its grade [GPT][DS].

### Q3 — MEAS-2 ensemble

**(a) Branch tally:** RESOLVED-CONSISTENT [GPT]; RESOLVED-FALSIFIER
[GROK]; RESOLVED-FALSIFIER [G?]; UNRESOLVED-BY-FLOOR [DS]. **No branch
carries 3/5.** The worker additionally records the textual facts
against the FROZEN prereg §3 (process observation, not a physics
ruling): the observed triple — tail significant; discriminator = 2.080
(domain-scaling, i.e. ballistic); D̄ not detected — satisfies **no
frozen branch conjunction**: branch 2 requires a domain-INDEPENDENT
(memory-type) late response (not met); branch 1 requires D̄ DETECTED
and tail consistent with zero (neither met); branch 3 is preregistered
as reachable only via an ENGINE-CONSISTENCY failure (the check passed).
Seat-position departures from the frozen text, recorded factually:
[GPT] ruled branch 1 without its detection and tail-zero clauses;
[GROK] states the frozen language "forces" branch 2, but branch 2 is a
conjunction including domain-independence; [G?] asserts "the
memory-type residual is real" against the discriminator's own reading;
[DS] assigns branch 3 though its sole preregistered trigger did not
fire (and see §5). **Ruling: classification remains OPEN — a
preregistration COVERAGE GAP, registered as OPEN-KMEM-TAIL-1 (§4). No
post-hoc branch is chosen; the no-retune / no-peeking discipline
governs the follow-up.**

**(b) Floor:** the σ_ctrl consistency check passed mechanically
(4.643e-3 within factor 2 of 3.93e-3; stdout, execution record 3017);
[GPT] and [G?] read the floor as cleared, [GROK] "formally cleared...
but the significant tail remains", [DS] not cleared (but on grounds
conflating the tail with the σ_ctrl check — see §5). **The mechanical
floor check PASSED; "floor cleared" as a promotion-bar element remains
entangled with the branch classification and is UNRESOLVED with it.**

**(c) L-4 / L-6 status:** consistent-not-uniquely-confirming [GPT];
open/under-tension [GROK]; refuted [G?]; needs-investigation [DS].
**Recorded status: UNDER TENSION — not refuted (the discriminator is
ballistic), not confirmed (the tail is significant). The registered
cross-falsifier has NOT fired and has NOT been retired.**

### Q4 — E-1 classification

RATIFY [GROK]; AMEND [GPT: preserve the historical
anomaly→negative-control record explicitly]; AMEND [DS: prove the
engine's Moment-boundary address deletion is correct substrate
behavior, else the reclassification is rescue-by-reinterpretation];
REJECT [G?]. **No 3/5; NOT ratified; PROVISIONAL** (fifth seat could
complete RATIFY or an AMEND consensus). Both named amendments carry to
the completion round.

### Q5 — THE PROMOTION RULING

PROMOTE-CONDITIONAL [GPT]; HOLD [GROK: named blocker = the significant
residual tail]; HOLD [G?]; HOLD [DS: C-5 and floor gaps]. **HOLD
carries 3/5 — FINAL** (promotion cannot reach 3 under any completion,
and C-5(iii) NOT-CONFIRMED independently fails the bar's first half).
**ENACTMENT: PR7 clause 2 (OPEN-K1-MEMORY-1, item 1B) remains OPEN.**
Named blockers, from the verbatim returns: (1) disposition of the
significant residual tail [GROK] — now OPEN-KMEM-TAIL-1; (2) the
explicit κ<1 contraction argument for C-5(iii) [GPT][DS].

### AUX batch

- **AUX-1 (OPEN-QMRG-ETA closure):** CLOSE [GROK]; AMEND [GPT:
  grade-labeling]; INSUFFICIENT [G?]; INSUFFICIENT [DS: mode coverage].
  **NOT closed; PROVISIONAL.** The touchpoint batch stays stocked;
  named items: mode coverage beyond the 4-pass check [DS];
  bookkeeping-vs-microscopic grade labeling [GPT].
- **AUX-2 (η-universality discharge):** DISCHARGE [GPT][GROK]; HOLD
  [G?][DS]. **2–2; NOT discharged; PROVISIONAL** (fifth seat decides).
- **AUX-3 (physical ρ-normalization discharge):** DISCHARGE
  [GPT][GROK]; HOLD [G?]; INSUFFICIENT [DS]. **2–2 in effect; NOT
  discharged; PROVISIONAL.**
- **AUX-4 Q-A:** CONFIRM-WITH-AMENDMENTS [GPT][GROK]; CONFIRM [DS];
  BREAK [G?]. **CONFIRM-class carries 3/5 — Q-A: CONFIRM-WITH-
  AMENDMENTS. FINAL as a panel-endorsement input; AP-4 enacts only at
  founder ratification.**
- **AUX-4 Q-B:** no-A3′-amendment [GPT][GROK]; amendment-required
  [G?][DS]. **2–2; UNRESOLVED; PROVISIONAL — to the completion round.**
- **AUX-4 Q-C:** obligations correctly scoped, O-6 SEVERABLE from this
  round's Q5 [GPT][GROK][DS]; NON-SEVERABLE [G?]. **SEVERABLE carries
  3/5 — FINAL.** O-6 (W-MULTILINK-1 re-runs) remains BLOCKING for
  AP-4-dependent shipping, not for this round's (already-HOLD) ruling.
- **AUX-4 Q-D:** preserves zero-parameter posture [GPT][GROK][DS,
  conditional on substrate determination of k]; FAILS [G?].
  **PRESERVES carries 3/5 — FINAL**, with [DS]'s condition recorded:
  k must be substrate-determined, never fit.
- **AUX-4 Q-E:** disclosure sufficient [GPT][GROK][DS]; discount/recuse
  Grok on AUX-4 [G?]. **SUFFICIENT carries 3/5 — FINAL.** The recusal
  motion (1 seat) does not carry and is recorded for founder awareness;
  the founder-ratification step is the structural safeguard.

## §4 — Registration: OPEN-KMEM-TAIL-1

**OPEN-KMEM-TAIL-1** (registry line to QM-adjacent DM sector on the
next frontier sweep; ID collision-checked at HEAD): the K-MEM-MEAS-2
significant tail statistic (1.570e-3, scale 2.805e-5) requires
disposition — controlled ballistic/support artifact vs genuine
long-time component — AND the prereg §3 branch semantics have a
registered coverage gap (significant tail + ballistic discriminator +
no D̄ detection satisfies no frozen branch). **Route (frozen-first
discipline, 2967/2981 lineage): a FRESH FROZEN supplementary
preregistration on the EXISTING kmem2 data — candidate discriminants
to be pre-registered before any further look (e.g., tail-window
support scaling across the dom sub-ensemble; edge-window exclusion
analysis; window-placement sensitivity) — drafted by the worker, then
PANEL-SANCTIONED in the CONV-013 completion round before execution.
Strictly no reanalysis of kmem2 before that freeze. No retune.** The
2918-scale non-detection of D̄ (power analysis predicted z ≈ 10.6; the
measured D̄ is ~100× below the motion-response scale) is recorded
inside OPEN-KMEM-TAIL-1 as a co-registered anomaly for the same
supplementary prereg — it is either physics or a response-statistic /
scale-expectation defect, and the frozen follow-up must say which.

## §5 — Integrity ledger updates

- **Grok: SCRIPT-EXECUTED-QUALIFIED, both keys VERIFIED-MATCH** (§2) —
  the arc's second substantiated execution; stdout omission noted.
- **DeepSeek adverse event #6 (invented-source-text class + stdout
  contradiction):** the founder-delivered transcript's reasoning block
  attributes to the frozen prereg a threshold clause that does not
  exist in it ("The prereg (2981...) says: 'tail statistic: if the
  tail statistic is significant (p<0.01) and the domain discriminator
  is >1.5, then the tail is ballistic; if ... <0.5, then it is
  memory-type.'" — no such text exists in
  `kmem_meas2_ensemble_prereg.md`), and the final return's floor ruling
  ("the floor (sigma_ctrl consistency) is not cleared" [DS]) states the
  opposite of the executed stdout's σ_ctrl result. Prior count ×5
  (latest: access-claim class); now ×6.
- **[G?] provenance question** (§1): pending founder confirmation;
  if Gemini, mislabel event #6.
- **Copilot: delivery event, no integrity event** (§1); remediation
  authorized; strike count unchanged at 2.

## §6 — Ledger after this adjudication

Six of seven; **PR7 PARTIAL — 1B OPEN (HOLD enacted, FINAL), named
blockers: OPEN-KMEM-TAIL-1 + the C-5(iii) contraction argument**; B7
holds; Candidate (B) 79.5% PROVISIONAL-FAVORABLE; 2855 PROVISIONAL;
d_DP ceiling ACTIVE; QM touchpoint batch STAYS STOCKED (AUX-1/2/3 not
discharged, PROVISIONAL); AP-4 panel-endorsement inputs: Q-A CWA,
Q-C severable, Q-D preserves, Q-E sufficient (FINAL as inputs), Q-B
unresolved — **AP-4 does not enact; AP-2/AP-3 stand**; W-MULTILINK-1
watching; O-6 BLOCKING for AP-4-dependent shipping. Nothing minted; no
value of ξ₂, ζ, η, d_DP, n_DP, or N computed.

**Completion round remit (when Copilot returns or records NO-RETURN):**
Q2, Q4, AUX-1/2/3, AUX-4 Q-B; sanction of the OPEN-KMEM-TAIL-1
supplementary prereg; [G?] attribution finalization.

**Founder mechanical actions:** (1) apply/push Patches 3019–3020;
(2) Copilot re-paste per §1 remediation; (3) one-line confirmation of
the [G?] return's source model. Next patch: 3021.
