# SUSTAINED-RESPONSE ESTABLISHMENT TIME — FROZEN BEFORE THE RUN

**Patch 3165, 17 August 2026. Economy-rule disposition: NO PANEL ROUND.**
`review_economy_protocol.md` §6 checklist applied and the §2.2 trigger found NOT
to hold: further unilateral work is a MEASUREMENT, not a guess. **The CONV-025
dispatch drafted at Patch 3164 §6 is WITHDRAWN** — see §1(c).

---

## §1 — What Patch 3164's run established, and the archaeology that followed

**(a) The corrected statistic works and the arms agree.** Under the Route B
recipe `sust_B = D[LATE] − D[PRE(12:24)]`, signed, all four isolation arms
DETECT (99% CI excludes zero) — where the old `abs()`-wrapped test had been a
no-op. Magnitudes collapsed from a 32× spread to a factor-2 cluster:

| arm | old (defective) | corrected sust_B | 99% CI |
|-----|-----------------|------------------|--------|
| a0  | 1.0948e-03 | **1.0840e-03** | [6.578e-04, 1.501e-03] |
| a0p | 4.5753e-04 | **5.5014e-04** | [1.726e-04, 9.424e-04] |
| a1  | 3.3887e-05 | **1.0555e-03** | [6.375e-04, 1.490e-03] |
| a2  | 1.4511e-04 | **7.7125e-04** | [3.529e-04, 1.187e-03] |
| ak  | 7.6268e-05 | **−1.5629e-04** | [−5.503e-04, 2.392e-04] |

All five arms ADEQUATE on the §3 resolution-floor test (half-widths ~3.8–4.3e-4
against band/2 = 1.3e-3).

**RETRACTION: Patch 3163's D-2 DETUNING-SUGGESTIVE reading is DEAD.** Under the
corrected statistic the Δ-ordering vanishes — a1 at |Δ| = 12 gives 1.0555e-3,
statistically indistinguishable from a0 at Δ = 0 (1.0840e-3). The apparent
detuning dependence was an artifact of the decay statistic. **This is the
worker's second refuted hypothesis of the arc** (window refuted at 3163;
detuning refuted here). Recorded, not dropped.

**(b) THE DEFECT IS A RECURRENCE OF ONE THE CORPUS ALREADY NAMED.** Patch 3026
registered **T-D-EXPECTATION-DEFECT** in these words: MEAS-2's frozen
`resp_S = mean(F[60:100]) − mean(F[200:240])` takes both windows POST-step, so
*"a sustained shift cancels EXACTLY; only decay between the windows registers."*
Route C's S3-C is `|D[60:100] − D[LATE]|` — **the same defect, carrying MEAS-2's
literal window indices `60:100`.** The programme diagnosed this class at 3026
and reintroduced it at 3055 under Route B's name and Route B's band. Recorded as
a process finding against the programme: a named, adjudicated defect class was
not added to any pre-launch executable check.

**(c) THE BAND IS A THEORY PREDICTION, AND IT HAS NOW FAILED IN TWO INDEPENDENT
CAMPAIGNS.** MEAS-1 §4.1 defines 2.6e-3 as `0.026·β` — the **predicted**
sustained motion response from the 2918 decomposition. It is not an empirical
calibration. Route B (MEAS-3) measured against it with the CORRECT POST−PRE
statistic and also failed it:

| campaign | arm | measured sustained | in band? |
|---|---|---|---|
| Route B | d24 | 1.022e-3 | no |
| Route B | d28 | 1.625e-3 | yes |
| Route B | d32 | 8.329e-4 | no |
| Route C | a0  | 1.084e-3 | no |
| Route C | a1  | 1.056e-3 | no |
| Route C | a2  | 7.712e-4 | no |
| Route C | a0p | 5.501e-4 | no |

**Seven arms, two campaigns, two codebases, clustered 0.55–1.63e-3 against a
prediction of 2.6e-3.** Route C's corrected values REPRODUCE Route B's. The
instrument agrees with itself across independent implementations; the prediction
does not agree with the instrument.

**This is why CONV-025 is withdrawn.** The worker is no longer without an
account. The account is: *the 2918 coefficient 0.026 overpredicts the sustained
motion response by ≈2.5–3×; the measured value is ≈0.010·β.* That is a physics
finding about CPP, obtained from CPP's own engine, and it is testable rather
than a guess. **It is NOT adopted here** — §4 below is what would test it, and
this patch does not perform that test either.

## §2 — THE ONE REMAINING ANOMALY, AND WHY IT IS MEASURABLE

AK returns **−1.5629e-04, CI spanning zero** — no detected sustained response —
while carrying **6× the drive** of four arms that all detect at ~8.6e-4. Two
explanations remain, and Patch 3163 D-1 could not separate them (R interval
[0.011, 76], UNRESOLVED):

- **H-HORIZON:** the sustained response takes time to establish. AK's LATE window
  sits at 92:104 — **68 Moments past the step** — against 312 for a0/a1, 240 for
  a0p, 432 for a2. If establishment needs ≳ 80 Moments, AK structurally cannot
  see it, and AK's null says nothing about β.
- **H-BETA:** the response genuinely fails to scale with β, so the band's
  `β/0.10` factor is wrong and AK's band is ~6× mis-sited.

**These are separable on the existing legs**, because the isolation arms span
T_END 264–504 and each one's own time series contains the establishment curve.
Measuring *when* the response establishes is a measurement, not a choice — which
is precisely why §2.2 does not fire.

## §3 — THE MEASUREMENT (frozen here, before computation)

For each isolation arm, slide a fixed-width 24-Moment window `W(t)` across
`t ∈ [t_post, T_END − 24]` in steps of 12, and compute against the SAME frozen
pre-step baseline:

```
g(t) = D[:, t : t+24].mean() − D[:, PRE(12:24)].mean()        # signed
```

`g(t)` is the establishment curve: the sustained response as a function of how
long after the step you look. Bootstrap over PAIRS, 2000 resamples, seed
30530811, 99% CI at each t. **No free parameter**: width 24 = the Route B PRE
window width; step 12 = the minimum baseline length already frozen at v2.1;
baseline = Route B's PRE, unchanged.

**Derived quantity — establishment time τ:** the smallest `t − T_STEP` at which
`g(t)`'s 99% CI first excludes zero AND remains excluding zero at every
subsequent t in that arm. Reported per arm.

**AK is measured on the same curve** over its available range (`t ∈ [72, 80]`,
one or two windows only) and is reported WITHOUT a τ, since a curve that short
cannot establish one.

## §3a — WHAT τ MEASURES, AND WHAT IT DOES NOT (smoke-tested BEFORE the run)

The measure was smoke-tested against synthetic responses with KNOWN
establishment times before being pointed at any leg. **Result: a linear ramp
establishing over 40 Moments and one establishing over 150 Moments BOTH returned
τ = 42.**

**τ is therefore time-to-first-detectable-signal, NOT physical establishment
time.** It is dominated by statistical power — pair count and noise — because a
slow ramp still crosses detectability long before it saturates. Recorded here,
before the run, as a limitation of the worker's own instrument.

**Why the test still answers the AK question — and why it answers it
conservatively.** The question is not "how long does the response take to
saturate" but "could AK have DETECTED a response within its 68-Moment horizon."
Time-to-first-detection is exactly the right quantity for that, and the
comparison is conservative in AK's disfavour for a reason worth stating:
**AK carries 512 pairs against the isolation arms' 128 — a factor 2 better
standard error.** AK is therefore MORE sensitive than the arms whose τ it is
being compared against, not less. If an isolation arm detects at 128 pairs by
τ ≤ 68, AK should detect more easily still within the same horizon.

**Consequence for the readings.** H-HORIZON-CONFIRMED requires every isolation
arm's τ to EXCEED 68 despite those arms being the less sensitive ones — a
demanding bar, correctly so. H-HORIZON-REFUTED, by contrast, is reached
easily, and if it fires the worker may NOT read it as proof that the response
saturates quickly; it establishes only that a detectable signal existed within
AK's window and AK did not report one.

## §4 — FROZEN READINGS

- **H-HORIZON-CONFIRMED** — every isolation arm's τ exceeds 68 Moments (AK's
  entire post-step horizon). AK could not have seen the response regardless of
  β; AK's null is uninformative about β-scaling and its S3-C reading must be
  withdrawn from the item-1 test rather than counted as a failure.
- **H-HORIZON-REFUTED** — some isolation arm's τ is ≤ 68 Moments. AK had time to
  see a response and did not; H-BETA survives as the live explanation and the
  band's β scaling is implicated.
- **H-ESTABLISHMENT-MIXED** — τ values straddle 68 Moments across arms. Neither
  explanation is eliminated; the successor campaign must lengthen AK's horizon
  AND vary β independently, and this patch says so rather than choosing.
- **H-NO-CURVE** — no arm's `g(t)` establishes a stable exclusion of zero. The
  sustained response is not a step-and-hold phenomenon at all and the entire
  S3-C control design is mis-conceived; **exhaustion trigger fires → panel.**

## §5 — EXHAUSTION TRIGGER

H-NO-CURVE only. Every other reading leaves the worker with a determinate next
action and therefore does NOT warrant a round (§3: "repairing a defective
instrument whose defect has a known, principled remedy").

## §6 — WHAT THIS PATCH MAY NOT DO

It may not re-site the band, re-run the frozen tree, re-read the falsifier, or
adopt the §1(c) coefficient finding. **Re-siting the band on these legs is
circular by construction** and remains forbidden; a corrected band must be
re-derived from the 2918 decomposition at source, or measured in a dedicated
calibration campaign frozen before its own data exists.

**The direction of the hazard is unchanged and is restated because it has not
weakened:** S1-C is length-adaptive, was untouched by every defect in this arc,
and returned SIGNIFICANT at a2 (Δ = +6). Every repair in this sequence moves
toward tree item 2 firing **DISP-T against Candidate (B)**. The worker is
repairing in the direction that convicts the programme's leading dark-matter
candidate, and has been throughout.

## §7 — Script

`code/3165_establishment_curve.py`. Existing legs, no new compute, read-only.
