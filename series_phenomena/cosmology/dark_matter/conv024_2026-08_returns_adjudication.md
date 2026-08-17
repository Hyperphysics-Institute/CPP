# CONV-024 RETURNS — ADJUDICATION

**Patch 3162, 17 August 2026. Five returns received (GPT, Grok, Gemini,
DeepSeek, Copilot). INDEPENDENCE: all five returns are substantively distinct —
no duplicates this round (the CONV-021 defect did not recur).**

**OUTCOME IN ONE LINE: DISP-I3 STANDS. The DM ledger does NOT move. Item 1B
remains OPEN. Candidate (B) remains at six of seven; 79.5%.**

---

## §1 — Tallies

| Q | Result | Split |
|---|--------|-------|
| Q1 PRE-EMPTION | **UPHOLD-PREEMPTION — UNANIMOUS** | 5–0 |
| Q2 S3-C FAILURE | **WINDOW-DEFECT (majority)** | 3–2 vs BAND-TRANSPLANT-INVALID |
| Q3 MINORITY CLAUSE | **NON-INTERPRETABLE (majority)** | 3–1–1 |
| Q4 P-κ | **FAILS-AS-PRINTED — UNANIMOUS** | 5–0 |
| Q5 AK SIGN INVERSION | **UNDETERMINED-BY-SPLIT** | 2–2–1 |
| Q6 CODE CORRECTION | **SOUND in substance — UNANIMOUS** | 3 SOUND, 2 SOUND-WITH-CAVEATS, 0 COMPROMISED |
| Q7 PATH | **REPAIR-AND-RERUN (majority)** | 3–2 vs RE-ANALYZE-EXISTING-LEGS |

**Per seat:**

- **Q1** — GPT, Grok, Gemini, DeepSeek, Copilot: all UPHOLD-PREEMPTION.
- **Q2** — WINDOW-DEFECT: Grok, DeepSeek, Copilot. BAND-TRANSPLANT-INVALID: GPT,
  Gemini. **Zero seats chose GENUINE-ABSENCE-OF-SUSTAINED-RESPONSE.** The panel
  is unanimous that the failure is instrumental in kind; it splits only on which
  instrument.
- **Q3** — NON-INTERPRETABLE: GPT, Grok, Gemini. INTERPRETABLE: DeepSeek.
  UNDERDETERMINED: Copilot.
- **Q4** — all five FAILS-AS-PRINTED. No seat entertained alternative treatment.
- **Q5** — NON-GATING-IGNORE: Grok, Gemini. INSTRUMENT-DEFECT: DeepSeek, Copilot
  (both naming scale/normalization on the short-baseline margin arm).
  UNDETERMINED: GPT. No majority.
- **Q6** — SOUND: Grok, Gemini, DeepSeek. SOUND-WITH-CAVEATS: GPT, Copilot.
- **Q7** — REPAIR-AND-RERUN: GPT, DeepSeek, Copilot. RE-ANALYZE-EXISTING-LEGS:
  Grok, Gemini.

## §2 — The binding note resolves

The dispatch bound Q1 and Q3 jointly. **Q1 UNANIMOUS UPHOLD-PREEMPTION + Q3
MAJORITY NON-INTERPRETABLE ⇒ the ledger does not move.** Item 1B is neither
discharged nor failed; it stays OPEN. The falsifier did not fire, and it was not
retired either. DISP-I3 INSTRUMENT is the round's standing verdict.

The worker recorded the branch as returned and selected nothing, as declared.

## §3 — A WORKER ERROR SUSTAINED (GPT and Grok, concurring)

GPT filed a concrete error against the dispatch's §F.3, and Grok made the same
point independently. **The finding is SUSTAINED and the worker owns it.**

The dispatch asserted that the minority clause "was drafted for a MINORITY of
failing arms." The operative frozen text — *"a failing INFERENTIAL arm is
PROSPECTIVELY NON-INTERPRETABLE and drops from inference"* — contains no such
condition. "Minority clause" is the rule's **label**, not a textual scope
restriction. As GPT put it, calling unanimity a reason not to apply the clause
imports an unstated exception after outcomes are known; unanimity changes the
*campaign* disposition through DISP-I3, it does not restore interpretability to
an individual arm.

The worker accepts this in full. Note for the record that the erroneous reading
was the one **less** favourable to the corpus — it kept the falsifier alive
rather than shielding the candidate — so it was not self-serving. It was still
an unsupported reading of a frozen rule, and reading scope into a rule's title
is exactly the class of error the programme's discipline exists to prevent.
**Corpus-wide correction adopted: the clause is arm-level and categorical, with
no cardinality condition.**

## §4 — A DECISIVE POST-HOC FINDING ON THE S3-C WINDOW (worker; disclosed as post-hoc)

**Stated first: this finding was made AFTER the disposition was printed and
after the returns were read. It is a code-versus-specification comparison
verifiable by reading, not a repair, and nothing has been altered. It is
reported because concealing it would be worse than the post-hoc label.**

Q7 turned on a factual dispute between seats. Copilot voted REPAIR-AND-RERUN on
the explicit premise that *"the 2048 legs cannot be re-analyzed because the
window defect affects the measurement slice itself, not a downstream statistic
that can be recomputed from stored data."* Grok voted RE-ANALYZE on the opposite
premise. **The premise is checkable, and Copilot's is false.** Each leg stores
the complete series `F`; the analysis loads it whole
(`F[(p,br,tag)] = np.array(json.load(open(pth))['F'])`) and applies every window
at analysis time. The window is entirely post-processing. The 2048 legs are
sufficient for any corrected statistic.

Checking that premise surfaced the following.

**(a) The S3-C sustained window is HARD-CODED and arm-independent.** The
statistic is

```python
sust = np.abs(D[:, 60:100].mean() - D[:, LATE].mean(axis=1).mean())
```

The literal slice `60:100` is applied to every arm. The script computes
`t_post, base = windows(x_half, T_END)` — but **S3-C never uses `t_post`.** Only
κ_sys does. Per-arm geometry:

| arm | x_half | T_END | t_post | base | LATE | S3-C window | 60:100 starts before t_post by | overlap with LATE |
|-----|--------|-------|--------|------|------|-------------|-------------------------------|-------------------|
| a0  | 24 | 384 | 66 | 48 | 336:384 | 60:100 | 6  | 0 |
| a0p | 16 | 264 | 54 | 48 | 216:264 | 60:100 | 0  | 0 |
| a1  | 32 | 384 | 78 | 48 | 336:384 | 60:100 | 18 | 0 |
| a2  | 28 | 504 | 72 | 48 | 456:504 | 60:100 | 12 | 0 |
| ak  | 28 | 104 | 72 | 12 | 92:104  | 60:100 | 12 | **8** |

**(b) On AK the sustained window and the late baseline OVERLAP.** AK's LATE
slice is 92:104 and its sustained slice is 60:100 — they share indices 92–100,
8 of the sustained window's 40 points. S3-C subtracts the late-baseline mean
from the sustained mean; on AK it is partially subtracting a region from itself,
which drives `sust` toward zero. **AK returned the campaign's most extreme
undershoot, 0.0098 of band-low.** This is the single unambiguous defect in the
record and it is arm-specific to the shortest arm — the same arm whose short
horizon produced the v2.1 pre-launch defect.

**(c) Four of five arms measure "sustained" response starting before their own
post-transient boundary,** by 6 to 18 Moments.

**Honest limit on this finding.** The ratios do not order monotonically with
misalignment: a0p is the only arm whose window sits entirely after `t_post` yet
returns 0.35, while a0 (6 Moments early) returns the best 0.84. So the window
defect is **necessary to explain AK and plausibly implicated elsewhere, but it
is not by itself a complete account of the universal undershoot.** The panel's
two Q2 hypotheses may in fact be one: the Route B S3-C recipe appears to have
been transplanted wholesale — reference value *and* hard-coded window indices —
into Route C geometries spanning T_END 104 to 504, where neither was validated.
That reading reconciles the 3–2 split rather than deciding it.

**THE STING, STATED PLAINLY.** S1-C is length-adaptive (`F[...][T_STEP:]` with
`nb = int(0.6 * Sp.shape[1])`), so it is far less exposed to this defect than
S3-C. **If a corrected S3-C restores two or more isolation arms to band, tree
item 1 does not fire, item 2 does, and DISP-T FIRES AGAINST CANDIDATE (B).**
The worker's diagnosis therefore makes the falsifier MORE likely to fire on a
corrected read, not less. GPT anticipated exactly this and made it a condition
of legitimacy: *the repair must be capable of validating a2 and killing
Candidate (B) just as readily as invalidating it.* **That condition is ADOPTED
as binding on any successor round.**

## §5 — Panel findings adopted

1. **The tree-ordering design flaw (Gemini, DeepSeek).** An instrument check
   placed first erases a falsifier's trigger rather than qualifying its
   confidence, so any systemic calibration error grants the favoured candidate a
   stay. Recorded as a **design finding against the programme, not against this
   execution.** Future disposition trees must state whether an instrument branch
   suspends or extinguishes downstream branches.
2. **Universal-failure gates must be executable and pre-launch (GPT, Grok).**
   The pilot ran AK only. An S3-C sanity gate across all arms, executed
   pre-launch, would have caught this before ~3900 CPU-h were spent. Adopted.
3. **Band and window transplants require domain validation (all five in
   substance).** No Route B statistic may be carried into a new route without a
   validation campaign in the new geometry. Adopted.
4. **Refactor-orphan audit (GPT, Copilot caveats on Q6).** The orphaned
   `beta_f` fetch is evidence of incomplete v2 refactoring; audit that every
   arm's β and every per-arm parameter propagates to every intended statistic.
   §4(a) above is the first fruit of exactly that audit. Adopted.
5. **Isolation-arm allocation (Grok).** 128 pairs against AK's 512 is thin.
   Recorded for future design; not actionable here.
6. **Q5 remains UNDETERMINED-BY-SPLIT.** Two seats independently name
   scale/normalization on the short-baseline margin arm; that is not a majority
   and no diagnostic is mandated, but it is folded into finding 4's audit scope.

## §6 — Standing after this round

- **DISP-I3 INSTRUMENT stands.** Evidentiary standing on the physics: NONE.
- **DM ledger: six of seven; 79.5%. Item 1B OPEN.** Unmoved in either direction.
- **P-κ FAILS as printed** (κ_sys^{U99} = 1.0059), unanimously affirmed.
- The 2048 legs **stand and are sufficient** for a corrected re-analysis; the
  contrary premise in one Q7 return is factually refuted above.
- Q7's 3–2 majority is REPAIR-AND-RERUN, **but one of the three votes rests on
  the refuted premise.** The worker records the vote as cast and does NOT
  re-tally it — re-weighting a seat's ballot on the worker's own after-the-fact
  finding would be precisely the kind of outcome-conditioned adjudication this
  round exists to prevent. The discrepancy is placed before the founder and the
  panel instead.
- **No repair is executed.** No retune after launch. The §4 finding is a
  diagnosis handed forward, and any successor round must freeze its corrected
  statistic BEFORE re-reading the legs, under GPT's adopted symmetry condition.

**Founder decision owed (physics-picture, not process):** whether to open a
successor round at all, given that the worker's own diagnosis points toward a
corrected read that is more likely to fire the falsifier against Candidate (B)
than to retire it.
