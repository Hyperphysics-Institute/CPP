# ROUTE C S3-C INSTRUMENT DIAGNOSTIC — FROZEN BEFORE THE RUN

**Patch 3163, 17 August 2026. Economy-rule disposition: NO PANEL ROUND.**

Per `templates/review_economy_protocol.md` §3, characterizing a defective
instrument is worker territory; §4's pre-commitment discipline substitutes for
the round and is applied in full below. **This diagnostic produces NO
disposition and moves NO ledger item.** It measures properties of the S3-C
statistic itself. The frozen tree, the DISP-I3 standing from CONV-024, and item
1B's OPEN status are untouched in every branch.

---

## §1 — What is already established (Patch 3162 + the corrected recomputation)

**(a) The window hypothesis is REFUTED by its own correction.** Replacing the
hard-coded `60:100` with the per-arm `t_post:t_post+40` moved the isolation arms
negligibly:

| arm | Δ | old sust | corrected sust | band low |
|-----|---|----------|----------------|----------|
| a0  | 0   | 1.095e-03 | 9.757e-04 | 1.30e-03 |
| a0p | 0   | 4.575e-04 | 4.533e-04 | 1.30e-03 |
| a1  | −12 | 3.389e-05 | 6.118e-05 | 1.30e-03 |
| a2  | +6  | 1.451e-04 | 1.477e-04 | 1.30e-03 |
| ak  | +6  | 7.627e-05 | 1.208e-04 | 7.80e-03 |

a0 moved *down*. The worker's leading hypothesis at CONV-024 §4 is dead, killed
by the correction the worker itself proposed. Recorded as a refuted hypothesis,
not quietly dropped.

**(b) AK CANNOT MECHANICALLY PASS S3-C — the campaign was unwinnable by
construction.** Clean Moments available between the post-transient boundary and
the stationary baseline, per arm:

| arm | T_END | t_post | baseline | clean Moments | 40-wide window fits? |
|-----|-------|--------|----------|---------------|----------------------|
| a0  | 384 | 66 | 48 | 270 | yes |
| a0p | 264 | 54 | 48 | 162 | yes |
| a1  | 384 | 78 | 48 | 258 | yes |
| a2  | 504 | 72 | 48 | 384 | yes |
| **ak** | **104** | **72** | **12** | **20** | **NO** |

Under the original code AK's sustained window (60:100) overlapped its baseline
(92:104) by 8 points; under the correction (72:104 after truncation) it overlaps
by 12. **No window definition repairs this — the arm is too short for the
statistic.** Frozen tree item 1 reads "...or AK fails S3-C → DISP-I3," so
**DISP-I3 was determined before any leg ran.** The v2.1 amendment (Patch 3057)
caught precisely this hazard — AK's short horizon inverting a window — repaired
it for κ_sys, and never checked whether S3-C carried the same defect in the same
arm. That is the programme's error, recorded plainly.

## §2 — DISCLOSURE OF PRIOR KNOWLEDGE (anti-extraction)

The corrected point estimates in §1(a) **are already known to worker and
founder.** They are reproduced above rather than concealed. The Δ-ordering
visible in them (Δ=0 largest, |Δ|=6 smaller, |Δ|=12 smallest) is therefore NOT
new information and the worker does not get to claim it as a blind prediction.

**What this diagnostic adds that is genuinely unknown: the uncertainties.** No
bootstrap CI has been computed on any corrected sust value. Whether the apparent
ordering survives its own error bars is unknown to everyone, and that — not the
ordering — is what the frozen readings below adjudicate.

## §3 — THE THREE MEASUREMENTS AND THEIR FROZEN READINGS

### D-1: β-scaling of the sustained response (matched Δ, matched geometry)

a2 and ak share x_half = 28.0 and Δ = +6, differing in β by 6× (0.10 vs 0.60).
The S3-C band assumes `band ∝ β/0.10`. **Matched-window requirement:** AK admits
only 20 clean Moments, so BOTH arms are measured on `t_post : T_END − baseline`
truncated to a common 20-Moment width (72:92) so the comparison is
window-identical. Statistic: `R = sust(ak) / sust(a2)`, with 2000-resample
bootstrap CI on R.

**FROZEN READINGS (declared before the run):**
- 99% CI on R contains 6.0 and excludes 1.0 → **BETA-SCALING-CONFIRMED**
  (the band's β scaling is sound; AK's band is correctly sited).
- 99% CI on R contains 1.0 and excludes 6.0 → **BETA-SCALING-FALSIFIED**
  (the band's β scaling is unsupported; AK's band is ~6× mis-sited and every
  AK S3-C reading in the corpus inherits the error).
- CI contains both, or neither → **BETA-SCALING-UNRESOLVED** (underpowered;
  no claim either way, and the successor campaign must measure it directly).

### D-2: Detuning dependence of the sustained response (isolation arms, β fixed)

All four isolation arms share β = 0.10. Regress sust on |Δ| ∈ {0, 0, 6, 12}
(a0, a0p, a2, a1). Statistic: the ordering `mean(Δ=0 arms) > sust(|Δ|=6) >
sust(|Δ|=12)`, each with bootstrap CIs.

**FROZEN READINGS:**
- Ordering holds AND the Δ=0 mean is separated from the |Δ|=12 arm at
  non-overlapping 99% CIs → **DETUNING-DEPENDENT** (S3-C measures a physically
  detuning-sensitive quantity; a single Δ-independent band applied to all four
  arms is MIS-SPECIFIED and required the detuned arms to fail).
- Ordering fails, or all four CIs mutually overlap → **DETUNING-INDEPENDENT**
  (the band's Δ-independence is defensible; the undershoot needs another
  explanation entirely).
- Ordering holds but CIs overlap → **DETUNING-SUGGESTIVE** (insufficient to
  convict the band; successor must measure it with more pairs).

### D-3: AK's honest sustained value on a clean non-overlapping window

AK measured on 72:92 (20 points, zero overlap with the 92:104 baseline) — the
first uncontaminated AK sustained reading in the campaign. Reported with CI. **No
pass/fail is computed and no band comparison is made**, because D-1 may show
AK's band to be mis-sited and comparing to a suspect band would be circular.

## §4 — EXHAUSTION TRIGGER (declared now)

If D-1 returns BETA-SCALING-UNRESOLVED **and** D-2 returns
DETUNING-INDEPENDENT, the worker has no principled account of the universal
undershoot, the avenue is exhausted under §2.2, and the matter goes to the panel
rather than to further worker hypotheses.

## §5 — WHAT THIS DIAGNOSTIC MAY NOT DO

It may not re-site the band. It may not re-run the disposition tree. It may not
re-read the falsifier. **A band recentred on the same legs it will then judge is
circular by construction**, and the worker will not do it — the corrected band
must come from a dedicated calibration campaign with a lengthened AK horizon,
frozen before its own testing data exists.

**GPT's CONV-024 symmetry condition remains binding on everything downstream:
the repair must be capable of killing Candidate (B) as readily as saving it.**
On the present evidence it is more likely to kill it — S1-C is length-adaptive,
was untouched by every defect found here, and returned SIGNIFICANT at a2
(Δ = +6).

## §6 — Script

`code/3163_routeC_s3c_diagnostic.py`. Runs on the existing 2048 legs. No new
compute. Read-only; writes nothing to `data/`.
