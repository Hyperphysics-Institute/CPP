# CONV-024 DISPATCH — K-MEM ROUTE C: THE DISPOSITION ROUND (Patch 3161)

**Patch 3161 (17 Aug 2026). CONV-001 format: the single fenced block below goes
verbatim to each of the five reviewers (GPT, Grok, Gemini, DeepSeek, Copilot).
Adversarial review explicitly invited. Returns land in
`conv024_2026-08_returns_adjudication.md`. This is the round the frontier has
reserved for Route C since Patch 3146 ("Route C outranks everything and gets its
OWN round on arrival"). Standing going in: DISP-I3 INSTRUMENT, evidentiary
standing NONE. The DM ledger does not move in any branch of this round without
the panel's own adjudication.**

Source record: `routeC_completion_and_disposition_record.md` (Patch 3160).
Reasoning: `reasoning/3160.md`. Prereg: `kmemC_routeC_prereg_v2.md` (Patch
3055) + v2.1 window amendment (Patch 3057).

The block:

````
CPP MULTI-AI REVIEW — ROUND CONV-024: THE K-MEM ROUTE C DISPOSITION
You are one of five independent AI reviewers (GPT, Grok, Gemini, DeepSeek, Copilot) for Conscious Point Physics (CPP). This block is self-contained; judge only what is in it. Adversarial review is explicitly invited: your job is to find what is wrong, not to be agreeable. Please answer independently — a previous round returned two verbatim-identical seats.

== A. CONTEXT (minimal) ==
CPP is a discrete substrate programme: point entities on a fine lattice execute per-Moment cycles; pairs form dipoles; the vacuum is a dilute weave ("Dipole Sea"). The dark-matter sector has a candidate, Candidate (B), an N=8 CDM-like ring at 11.264 GeV, currently at six of seven requirements (79.5%). Requirement 7 / ledger item 1B turns on an INDICTMENT: an earlier campaign (Route B) found a tail artifact that, if it survives domain-robust control-valid testing, sinks the candidate. K-MEM ROUTE C is the campaign built to retire or sustain that indictment. Its design isolates the artifact geometrically: four ISOLATION arms at differing detuning Δ (two at Δ=0, one at Δ=−12, one at Δ=+6) plus one MARGIN arm (AK) carrying a systematic-uncertainty coefficient κ_sys. The falsifier logic: the artifact should appear at Δ=0 and NOWHERE else; a significant tail at any Δ≠0 arm means the effect is not the Δ=0 mechanism and the indictment is SUSTAINED.

== B. WHAT WAS FROZEN, BEFORE ANY LEG RAN (prereg v2, Patch 3055; window amendment v2.1, Patch 3057) ==
STATISTICS. S3-C control (all arms): a Route B recipe with the acceptance band scaled by β/0.10 from a reference SUST_REF0 = 2.6e-3, giving band [1.30e-03, 5.20e-03] at the four β=0.10 isolation arms and [7.80e-03, 3.12e-02] at AK (β=0.60). MINORITY CLAUSE: "a failing INFERENTIAL arm is PROSPECTIVELY NON-INTERPRETABLE and drops from inference." S1-C tail (isolation arms only): Route B S1 recipe verbatim. κ_sys (AK primary): fit window [t_post, T_END − baseline) with t_post = t_step + 1.5·x_half + 6 and baseline = max(12, min(48, (T_END − t_post)//3)).
PASS CONDITIONS. P-ISO: S1-C SIGNIFICANT at BOTH Δ=0 arms AND c.w.z. at every valid Δ≠0 arm. P-κ: AK resolves on BRANCH-FIT with κ_sys^{U99} < 1.
DISPOSITION TREE (total; EVALUATED IN ORDER; standing NONE until this round):
 1. Fewer than TWO isolation arms pass S3-C, or AK fails S3-C → DISP-I3 (instrument; panel).
 2. S1-C SIGNIFICANT in ANY valid Δ≠0 arm → DISP-T: THE FALSIFIER FIRES — indictment SUSTAINED; item 1B FAILS; Candidate (B) fails requirement 7.
 3. P-ISO ∧ P-κ → DISP-R: RETIREMENT FINALIZED + MARGIN CERTIFIED → item 1B DISCHARGES → SEVEN OF SEVEN.
 4. P-ISO ∧ ¬P-κ → DISP-P: PARTIAL. 5. ¬P-ISO because the artifact fails to reproduce at A0 → DISP-X. 6. ¬P-ISO because A0 shows it but A0′ does not → DISP-G. 7. else → DISP-M3 IMPASSE.
ALSO FROZEN: no interim looks; the analysis refuses incomplete manifests; NO RETUNE AFTER LAUNCH; ONE panel round on completion.
V2.1 AMENDMENT DISCLOSED: v2 froze the stationary baseline at a flat 48 Moments. On AK (deliberately the shortest arm, T_END=104) that inverted the fit window to −16 points and the pilot crashed on an empty slice — an arithmetic slip in the same family as an earlier v1 exit-time error, and caught the same way, by an executable gate rather than by reading. The amended rule is scale-free, leaves every isolation arm bit-identical at baseline 48, and gives AK baseline 12 with 20 fit points (≥ the frozen 8-point BRANCH-FIT minimum). Pre-launch, evidence-excluded pilot legs only.

== C. EXECUTION (10–17 Aug 2026, Kila6, 32 cores, committed CPU engine, no GPU) ==
2048 legs completed: a0 256, a0p 256, a1 256, a2 256, AK 1024 — every arm at its EXACT preregistered allocation, no overrun, no shortfall. ≈3900 CPU-h against a ≈3720 CPU-h estimate. Per-leg wall times stable to <1% within each arm across the whole campaign.
INTEGRITY SWEEP, run on the complete set before the analysis: zero unpaired legs (every pair index has both ctrl and step); zero truncated files; zero unparseable files. This sweep was run specifically because the machine suffered SIX hard halts mid-campaign (frozen console, hard power-cycle required; Kernel-Power 41 + EventLog 6008 with NO WHEA-Logger entries at any halt). Diagnosis: a motherboard auto-overclock enhancer holding all-core boost past stock under sustained load — a CPU hard-hang, not power delivery (1200 W supply, package 60–70 °C). Disabling it took clean uptime from ≈8 h to ≈36 h; factory-optimized defaults carried the campaign home. Leg-level checkpointing means each halt cost only in-flight legs, recomputed from scratch. Attack this if you think a hard-hang can corrupt an already-written leg that still parses and pairs.

== D. A CODE DEFECT AND ITS CORRECTION, MADE BLIND TO ALL RESULTS ==
The frozen analysis aborted on its first invocation: KeyError: 'beta_f' at line 40, `beta_f = rep['beta_f']`, where rep = pilot_report.json (contents: arm, N_projected=512, peakD, sd_pair, SNR=32.35, status=OK — it has never carried a beta_f key). The assigned name is NEVER READ AGAIN: every use of β is the per-arm `beta` unpacked from the module-level ARMS table, and only one enters arithmetic — `band = SUST_REF0 * beta / 0.10`. The 3054→3055 diff shows the provenance: the predecessor had a flat ARMS tuple with one global β context; the v2 rewrite moved β per-arm and orphaned the pilot-report fetch. THE CORRECTION WAS DELETION OF THE LINE — nothing substituted, nothing re-sourced — which is provably behavior-preserving because the target was never read. Two alternatives were considered and rejected: adding beta_f to the committed pilot report (post-launch modification of a committed input), and re-sourcing a scalar β from calibration.json (β is per-arm — 0.10×4, 0.60 at AK — so any scalar would either be unused or would silently apply one arm's drive to every arm, corrupting the very band at issue). ORDERING, STATED: diagnosed and applied BEFORE any statistic, arm result, or disposition had been computed or seen by worker or founder. Judge this as Q6.

== E. THE FROZEN OUTPUT, VERBATIM ==
[a0 |iso|Δ=+0 ] pairs 128/128  S3-C: sust=1.095e-03 band[1.30e-03,5.20e-03] -> FAIL  S1-C: tail= 7.690e-03 (scale 1.769e-04) -> SIGNIFICANT  kappa_sys[BOUND]=0.9985 99%CI[0.6545,1.0288]
[a0p|iso|Δ=+0 ] pairs 128/128  S3-C: sust=4.575e-04 band[1.30e-03,5.20e-03] -> FAIL  S1-C: tail= 3.643e-03 (scale 1.526e-04) -> SIGNIFICANT  kappa_sys[BOUND]=1.0049 99%CI[0.6510,1.0643]
[a1 |iso|Δ=-12] pairs 128/128  S3-C: sust=3.389e-05 band[1.30e-03,5.20e-03] -> FAIL  S1-C: tail= 1.898e-04 (scale 1.489e-04) -> c.w.z.       kappa_sys[BOUND]=0.9925 99%CI[0.7348,1.0146]
[a2 |iso|Δ=+6 ] pairs 128/128  S3-C: sust=1.451e-04 band[1.30e-03,5.20e-03] -> FAIL  S1-C: tail= 5.551e-03 (scale 2.849e-04) -> SIGNIFICANT  kappa_sys[BOUND]=1.0290 99%CI[0.9333,1.0407]
[ak |mgn|Δ=+6 ] pairs 512/512  S3-C: sust=7.627e-05 band[7.80e-03,3.12e-02] -> FAIL  S1-C: tail=-1.179e-03 (scale 1.956e-05) -> SIGNIFICANT  kappa_sys[BOUND]=0.9928 99%CI[0.7353,1.0059]
DISPOSITION: DISP-I3 INSTRUMENT — fewer than two isolation arms pass S3-C, or AK fails S3-C; no standing; panel.

== F. WHAT THE WORKER READS IN IT (all of it offered for attack, none of it adopted) ==
1. TREE ITEM 1 FIRES ON BOTH LIMBS INDEPENDENTLY. All five arms FAIL S3-C. The failure is UNIVERSAL AND ONE-DIRECTIONAL — every arm undershoots its band's lower edge, none overshoots, none lands inside. Ratios sust/band-low: a0 0.84, a0p 0.35, a1 0.026, a2 0.11, AK 0.0098. Arms differing in geometry (x_half 16–32), horizon (T_END 104–504) and drive (β 0.10 vs 0.60) failing the same way in the same direction across two orders of magnitude is the signature DISP-I3 exists to catch. AK's ratio is most extreme because its band is 6× by the frozen β/0.10 scaling. NOTE a0 misses by only 16% — a near-miss a modest band or window error would flip.
2. THE PRE-EMPTION — THE MOST CONSEQUENTIAL FACT IN THIS ROUND, STATED UP FRONT. The tree is evaluated in order. a2 is a Δ=+6 arm and returned S1-C SIGNIFICANT (5.551e-03 against scale 2.849e-04). HAD ITEM 1 NOT FIRED, ITEM 2 WOULD HAVE FIRED DISP-T: THE FALSIFIER FIRES — indictment SUSTAINED, item 1B FAILS, Candidate (B) FAILS REQUIREMENT 7. DISP-I3 is therefore the only thing standing between the corpus and a fired falsifier against its own leading dark-matter candidate. The worker states this plainly because it is exactly the circumstance in which a worker would be tempted to prefer the instrument reading, and exactly the verdict a panel should scrutinize hardest. The worker's only defence is that it made no choice: the order was frozen in Patch 3055 before any leg ran, and item 1's trigger is not marginal (five of five arms fail, one by a factor of 100).
3. THE MINORITY-CLAUSE KNOT. §4 says a failing inferential arm is PROSPECTIVELY NON-INTERPRETABLE and drops from inference. a2 failed S3-C. If the clause governs, a2 is not a "valid" Δ≠0 arm and item 2 never had a trigger at all. If it does not, the falsifier evidence survives the instrument verdict and awaits a clean re-read. The clause was drafted for a MINORITY of failing arms; here ALL FIVE failed. The worker declines to extend a minority clause to a unanimity by construction, and sends the question rather than resolving it in the direction that happens to favour the corpus. This is Q3.
4. P-ISO FAILS AS PRINTED. SIGNIFICANT at both Δ=0 arms — satisfied. c.w.z. at every valid Δ≠0 arm — a1 (Δ=−12) yes, a2 (Δ=+6) no. Conditional on Q3.
5. P-κ FAILS AS PRINTED, MARGINALLY — AND A WORKER ERROR IS OWNED HERE. The condition is κ_sys^{U99} < 1. AK returns point estimate 0.9928 with 99% CI upper bound 1.0059 — the bound exceeds 1 by 0.6%, so the condition is NOT met. In first reading the output to the founder the worker stated that P-κ was satisfied; it read the point estimate and spoke past the condition. Corrected in the record before dispatch and surfaced here as Q4 rather than buried, because a 0.6% overshoot on a bound is precisely the margin a worker is tempted to round in its favour.
6. TWO ANOMALIES FLAGGED, NOT INTERPRETED. (i) AK's S1-C tail is NEGATIVE (−1.179e-03) yet flagged SIGNIFICANT against a very small scale (1.956e-05). Per §4 the S1-C tail is an ISOLATION-arm statistic and AK is class margin, so this line is non-gating — but it is printed and it is anomalous. (ii) The S3-C band derives from SUST_REF0 = 2.6e-3, a ROUTE B reference transplanted into Route C geometry and scaled only by β. Nothing in this campaign tested that transplant.
7. TWO COMPETING HYPOTHESES FOR THE UNIVERSAL S3-C FAILURE, NEITHER ADOPTED, RATED EQUALLY. (a) THE WINDOW: t_post = t_step + 1.5·x_half + 6 with baseline max(12, min(48, (T_END − t_post)//3)) — this arithmetic already produced one pre-launch defect corrected at v2.1, caught by an executable gate rather than by reading; a second defect in the same family is live. A window opening after the sustained response has substantially decayed would produce exactly a universal one-directional undershoot. (b) THE BAND DOES NOT TRANSPLANT: if SUST_REF0 is simply wrong for Route C geometry, then a0 (16% miss) and possibly a0p were never failing arms, and the DISP-I3 trigger is itself an artifact of a mis-sited band. NOTE WHAT (b) IMPLIES: if the band is wrong and a0+a0p actually pass, tree item 1 does not fire, item 2 does, and DISP-T FIRES AGAINST THE CANDIDATE. The worker flags that the hypothesis LEAST favourable to the corpus is the one it cannot rule out. NEITHER hypothesis was acted on: no retune after launch, and a repair chosen after seeing which repair yields which disposition is not a repair.

== G. WHAT YOU SHOULD ATTACK (non-exhaustive) ==
The order-of-evaluation design itself (does a tree whose first item is an instrument check systematically shield candidates?); whether a universal S3-C failure should have been an EXECUTABLE PRE-LAUNCH GATE rather than a disposition branch (the pilot ran only AK); the Route B → Route C band transplant and the β/0.10 scaling; whether S1-C's "scale" normalization is comparable across arms with different T_END; the AK sign inversion; whether 128 pairs at the isolation arms is adequate given AK needed 512; the v2.1 amendment's scale-free rule (does baseline 12 at AK make AK's κ_sys and its S3-C non-comparable to the isolation arms by construction?); whether the beta_f deletion could have masked an intended-but-unwired per-arm β check; whether six hard machine halts can produce a leg that parses, pairs, and is still wrong; the worker's P-κ misreading as evidence about the worker's reliability elsewhere in this record.

== H. ADJUDICATION QUESTIONS — answer ALL, using EXACTLY this verdict vocabulary ==
Q1 THE PRE-EMPTION: does DISP-I3 at item 1 legitimately pre-empt DISP-T at item 2? [UPHOLD-PREEMPTION | OVERTURN-TO-DISP-T (state the rule misapplied) | UNDERDETERMINED (name what decides)]
Q2 THE UNIVERSAL S3-C FAILURE: what does five-of-five one-directional undershoot indicate? [WINDOW-DEFECT | BAND-TRANSPLANT-INVALID | GENUINE-ABSENCE-OF-SUSTAINED-RESPONSE | OTHER (specify operationally)]
Q3 THE MINORITY CLAUSE: is a2's S1-C SIGNIFICANT interpretable given a2 failed S3-C? [NON-INTERPRETABLE (clause governs; item 2 had no trigger) | INTERPRETABLE (falsifier evidence stands pending clean re-read) | UNDERDETERMINED]
Q4 P-κ: κ_sys^{U99} = 1.0059 against a < 1 condition. [FAILS-AS-PRINTED | the 0.6% overshoot warrants specified alternative treatment (specify — and say why that is not post-hoc widening)]
Q5 THE AK SIGN INVERSION: a negative tail flagged SIGNIFICANT in the margin arm. [INSTRUMENT-DEFECT (specify) | PHYSICAL (specify) | NON-GATING-IGNORE | UNDETERMINED]
Q6 THE CODE CORRECTION: the blind deletion of an unread assignment. [SOUND | SOUND-WITH-CAVEATS (state them) | COMPROMISED (state the specific contamination path)]
Q7 THE PATH: what legitimately opens next? [REPAIR-AND-RERUN (name the specific defect that must be fixed AND state how a re-run avoids being a retune) | RE-ANALYZE-EXISTING-LEGS (the 2048 legs stand; name the corrected statistic) | ACCEPT-DISP-I3-AND-STOP (item 1B stays open indefinitely) | NO-PATH (argue it)]
BINDING NOTE: Q1 and Q3 jointly govern whether the DM ledger moves. A majority OVERTURN-TO-DISP-T on Q1, or a majority INTERPRETABLE on Q3 combined with any Q1 answer other than UPHOLD-PREEMPTION, sends item 1B to FAILURE and Candidate (B) to failing requirement 7. A majority UPHOLD-PREEMPTION with NON-INTERPRETABLE leaves the ledger at six of seven with item 1B OPEN. The worker will not select among these branches; whatever the panel returns is recorded as returned.
````

---

## Dispatch-day checklist (worker)

- [x] CLONE-FIRST GATE executed; CONV-024 verified free (highest prior CONV-023);
      patch IDs 3160/3161 verified free.
- [x] Source record and reasoning fragment committed BEFORE dispatch (3160).
- [x] Verbatim frozen output reproduced without edit.
- [x] Worker's own P-κ misreading disclosed in the block, not only in the record.
- [x] The pre-emption stated in the block's own §F item 2, up front, unhedged.
- [x] The hypothesis least favourable to the corpus (band-transplant → DISP-T)
      stated explicitly as unresolvable by the worker.
- [x] Independence requested (CONV-021's duplicate return precedent).
- [ ] Five pastes; returns → `conv024_2026-08_returns_adjudication.md`.
