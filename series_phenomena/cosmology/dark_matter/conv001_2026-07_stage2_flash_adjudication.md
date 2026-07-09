# CONV-001 ADJUDICATION — Stage-2 flash verification returns (Patch 2368, 9 July 2026)

**Returns:** five, seat-blank relay, mapped by the standing relay-order convention
(2363): **R1=GPT, R2=Grok, R3=Gemini, R4=Copilot, R5=DeepSeek.** Gemini's self-ID
is CORRECT this round (improvement over 2362 noted in the anomaly register).
Copilot: second consecutive no-access abstention — **standing fix registered: the
Copilot seat must receive the files PASTED, not linked.**

## Fact-checks (run before grading, against code and fresh execution)
- R3's "lmax caps at 10": actual `lmax = max(12, ...)` = 12 at dimer momenta.
  Minor misstatement; verdict unaffected.
- R3's manual kinematics (Hg E_max ≈ 612 eV, Si ≈ 3.6 keV at 818 km/s):
  reproduced exactly. Su verified.
- R5's "~100 events in the low bins" at the weak corner: actual 157.4
  (15.1 + 142.3, per-bin dump in 2368_results.json) — order-consistent with a
  genuine re-run; accepted as substantive.
- R5's V5 citation attributes the 0.94–0.99 requirement to "1888 SI-2 scan" —
  the sentence is DM-3 v1.1 text (Patch 2359) rooted in the 2344/2349 record.
  CITATION MISATTRIBUTION noted; content verified correct against the ledger.
- R5's finding 2 calls DAMIC-M "surface-based" — DAMIC-M is at LSM (4800 mwe,
  underground). Factual error IN THE FINDING; graded down. Its core point
  (only overburden-free instruments probe the strong regime — and XQC already
  did) stands.
- R1's finding 1 (say "above every underground ceiling; straddles surface"):
  verified ALREADY PRESENT in the Stage-2 record verbatim; confirmed, no edit.

## Grades

| Item | R1 GPT | R2 Grok | R3 Gemini | R5 DeepSeek | Resolution |
|---|---|---|---|---|---|
| V1 adaptation | VERIFIED | INDET (check named) | VERIFIED | VERIFIED | **VERIFIED — check EXECUTED** |
| V2 island convention | VERIFIED | VERIFIED | VERIFIED | VERIFIED | **VERIFIED unanimous** |
| V3 criterion (a+b) | VERIFIED | VERIFIED | VERIFIED | VERIFIED | **VERIFIED unanimous** |
| V4 robustness | VERIFIED | VERIFIED | VERIFIED | VERIFIED | **VERIFIED unanimous** |
| V5 consequence | VERIFIED | VERIFIED | VERIFIED | VERIFIED | **VERIFIED unanimous** |

(R4 Copilot: NO-REVIEW abstention throughout, honest and self-declared.)

**R2's V1 check, executed this patch** (`code/2368_v1_convergence_audit.py`,
pass criteria pre-stated in the header): (a) weak-corner XQC total invariant to
≤0.03% with violated-bin count UNCHANGED under h→0.04→0.02, rmax→240, lmax+12;
(b) Born vs partial-wave at weak coupling (1879's own validation method, at the
dimer parameters): 0.134% agreement (<1% criterion). BOTH PASS. The
INDETERMINATE resolves per its own named check.

**Strengthenings contributed by the round** (registered):
- R3's multipole argument: the dimer is the MINIMAL cage → less field
  cancellation than the 18-element rod → the dimer's true S_c is, if anything,
  HIGHER than the rod's island — the 2366 convention was generous to the
  candidate, and the kill survives its generosity.
- R3's quantitative V3(b): the per-bin criterion assumes ZERO background
  subtraction — an absolute upper bound; unattributed background only tightens
  the allowance. Thresholds at the weakest corner: 5 events (29–36 eV, obs 0)
  vs 15.1 predicted; 28.3 (36–128 eV, obs 11) vs 142.3 predicted.
- R2's WOUND (state the background assumption explicitly in the record):
  ACCEPTED — executed as one sentence in the Stage-2 record this patch.

**Rejected:** R2's SCRATCH (Stage-1 ceilings might shift for the dimer's mass)
— misreading: 2365 computed the ceilings AT m_chi = 2.8 GeV (script line
`m_chi = 2.8*GeV`); there is no rod-mass ceiling to shift from.

## RESULT: V1–V5 VERIFIED ACROSS ALL SUBSTANTIVE SEATS.
**THE KILL IS ADJUDICATION-READY.** Per the brief's own rule: V1–V4 verified
with V5 verified makes the kill adjudication-ready for the founder. The
formation-realizable population — dimer-weighted at every passing point of
every audited frame per the 2344/2349 record — is EXCLUDED-class against the
2007 XQC spectrum at every registered island coupling, both signs, the full
abundance bracket, persisting below the island floor, under the pipeline's own
conservative zero-background criterion, with solver validity independently
audited by three seats and convergence-verified by executed check.

## ON THE FOUNDER'S DESK (verbatim blocks; nothing moves without them)

**(A) KILL ADJUDICATION.** If attested, registers: the population branch of
CONJ-COSMO-1's candidate is KILLED at the audited frames (XQC-2007 channel,
Patches 2366–2368) — the campaign's second kill, joining the capture branch's
kill at the registered frame (2333). Clause 1 exit-class event (dimer face,
adverse direction); OPEN-DM-DSPH-1 verdicts UNFROZEN per the attested Clause 1;
the missing-physics search reopens with both candidate branches dead.
> KILL ADJUDICATION (TLA, date): ______

**(B) RELEASE RE-DECISION (the 2364 unified ruling is superseded by events for
DM-1/DM-3; DM-2 is not named by the finding).** Worker recommendation: DM-2
releases ALONE on the 20th as ruled; DM-1/DM-3 are PULLED from the 20th and
revised to record both kills honestly — the dual-kill record (capture at the
registered frame, population at the audited frames, each by the programme's
own instrument) with OPEN-DM-DSPH-1 reopened, re-releasable on a short panel
round when the revisions are ready. This is publishable falsification work of
exactly the kind the programme's operating system was built to produce.
> RELEASE RE-DECISION (TLA, date): ______
