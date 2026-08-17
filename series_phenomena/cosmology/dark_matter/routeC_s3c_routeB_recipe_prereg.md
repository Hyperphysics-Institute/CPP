# S3-C CORRECTED TO THE ROUTE B RECIPE — FROZEN BEFORE THE RUN

**Patch 3164, 17 August 2026. Economy-rule disposition: NO PANEL ROUND FOR THE
REPAIR** (`review_economy_protocol.md` §3 — a defective instrument with a known,
principled remedy). §4 pre-commitment applied in full below. **A panel round IS
anticipated downstream on a §2.1 WIN trigger** (a closed falsifier campaign) if
the corrected control restores the arms — see §6.

---

## §1 — THE DEFECT: Route C computes the inverse of the recipe it was told to use

`kmemC_routeC_prereg_v2.md` §4 specifies: *"S3-C control (all arms): **Route B
recipe** with the band scaled by β/0.10."* The Route B recipe is committed at
`code/3028_kmem3_analysis.py`:

```python
PRE_W, POST_W = (12, 24), (300, 360)        # S3 windows, frozen
def sust(br):
    a = F[(p, br, tag)]
    return a[POST_W[0]:POST_W[1]].mean() - a[PRE_W[0]:PRE_W[1]].mean()
Ds.append(sust('step') - sust('ctrl'))
...
lo, hi = np.percentile(boots, [0.5, 99.5])
det = not (lo <= 0.0 <= hi)                  # SIGNED, excludes zero
```

Algebraically, since `sust(step) − sust(ctrl) = D[POST] − D[PRE]` with
`D = S − C`, **Route B measures: late-time level MINUS pre-step level.** That is
a sustained response — how far above its own pre-step baseline the system sits
at late times.

`code/3055_kmemC_analysis.py` implements instead:

```python
sust = np.abs(D[:, 60:100].mean() - D[:, LATE].mean(axis=1).mean())
det  = bool(np.percentile(boots, 0.5) > 0 and sust > 0)
```

**Route C measures: early-post level MINUS late-time level.** Both windows are
post-step. This is a DECAY statistic. It is not the Route B recipe; it is close
to its negative.

### Consequence, stated exactly

**A perfectly sustained (non-decaying) response yields EXACTLY ZERO under the
Route C implementation.** The more genuinely sustained the response, the smaller
the measured statistic. This is a one-directional, geometry-independent,
β-independent downward bias — which is precisely the observed signature: five of
five arms undershooting, none overshooting, none in band, across x_half 16–32,
T_END 104–504, and β 0.10–0.60.

### Two further defects in the same transplant

**(b) `abs()` destroys the detection test.** Every bootstrap replicate is wrapped
in `np.abs`, so all are ≥ 0 and `np.percentile(boots, 0.5) > 0` is trivially
true. Route B's test — whether a SIGNED interval excludes zero — was destroyed.
**The detection half of S3-C has been a no-op for the entire campaign.**

**(c) `abs()` biases the point estimate upward.** The absolute value of a noisy
near-zero quantity has positive expectation. The reported sust values are
therefore inflated relative to the (already wrong) quantity they estimate.

### Retraction owed on Patch 3163 §1(b)

Patch 3163 concluded that AK "cannot mechanically pass S3-C" because 20 clean
Moments cannot host a 40-wide post-transient window. **That is true of the
mis-implemented statistic only.** The Route B recipe requires the stationary
baseline and the fixed pre-step window `12:24` — identical for every arm, since
T_STEP = 24 throughout — and AK has both. **Under the correct recipe AK is
measurable, and the "unwinnable by construction" claim is WITHDRAWN as stated.**
What survives: the implemented statistic was structurally impossible at AK, and
the v2.1 amendment audited κ_sys's window in that arm without auditing S3-C's.

### Worker's hypothesis record, stated plainly

This is the worker's THIRD account of the universal undershoot. The window
hypothesis (CONV-024 §4) was REFUTED by its own correction at Patch 3163. The
β-scaling hypothesis returned UNRESOLVED at Patch 3163 D-1. Both are recorded
as failed. This one is offered as different in kind, and the difference is
checkable rather than rhetorical: it is not a claim about magnitudes but a
demonstrated mismatch between two committed files, verifiable by reading them
side by side. **Making code match a frozen spec is a repair, in the same class
as the `beta_f` deletion at Patch 3160 — not a retune.** The panel is entitled
to reject that characterization.

## §2 — THE CORRECTED STATISTIC (frozen here, before computation)

For each arm, with `D = S − C` over pairs, `base = max(12, min(48, (T_END −
t_post)//3))`, `LATE = slice(T_END − base, T_END)`, `PRE = slice(12, 24)`:

```
sust_B = D[:, LATE].mean() − D[:, PRE].mean()        # SIGNED, no abs()
```

Bootstrap over PAIRS (not over window points), 10000 resamples, seed 30530811.

```
lo, hi = percentile(boots, [0.5, 99.5])
det    = not (lo <= 0.0 <= hi)                        # Route B test restored
inband = band/2 <= |sust_B| <= band*2,  band = 2.6e-3 · β/0.10
s3_pass = det and inband
```

Every element is transcribed from Route B or from the already-frozen v2.1
window rule. **There is no free parameter for the worker to tune.** The band,
the factor-2 width, the β scaling, the bootstrap seed and count, and the
baseline rule are all unchanged from what was frozen before launch.

## §3 — RESOLUTION FLOOR REQUIRED BEFORE ANY INTERPRETATION (§9 claim hygiene)

Adopted from CONV-022 Q5: no positive result may be interpreted before its
statistic's resolution floor is computed. Patch 3163 showed the OLD statistic's
99% CI half-widths (~7e-4 to 1.3e-3) to be comparable to the band's entire lower
edge (1.3e-3) — the control could not resolve what it was asked to judge.

**Per arm the corrected run reports the CI half-width, and any arm whose half-
width exceeds band/2 is labelled UNDERPOWERED. An UNDERPOWERED arm's pass or
fail is uninformative and may not be used in any direction**, including in the
worker's favour.

## §4 — FROZEN READINGS

- **S3C-RESTORED** — ≥ 2 isolation arms `s3_pass` AND `ak` `s3_pass`, with no
  contributing arm UNDERPOWERED. The implemented statistic, not the physics, was
  the source of DISP-I3. Tree item 1 would not have fired. **The tree is NOT
  re-run in this patch** (see §6).
- **S3C-GENUINE-FAILURE** — the corrected statistic still fails, with every arm
  adequately powered. The sustained response is genuinely absent or mis-modelled;
  DISP-I3 stands on its merits and the indictment cannot be adjudicated by this
  campaign.
- **S3C-UNDERPOWERED** — any arm bearing on the item-1 test is UNDERPOWERED.
  The control cannot decide at N = 128; the successor campaign must be sized
  from the measured floor, not guessed.
- **S3C-MIXED** — restoration is partial (e.g. isolation arms restore, AK does
  not, or vice versa). Reported as-is; no branch selected by the worker.

## §5 — EXHAUSTION TRIGGER

If the reading is S3C-GENUINE-FAILURE, the worker has exhausted its accounts
(three hypotheses, all failed) and the matter goes to the panel with that record
stated, rather than to a fourth worker hypothesis.

## §6 — WHAT THIS PATCH MAY NOT DO, AND THE HAZARD RUNNING THE OTHER WAY

**The frozen disposition tree is NOT re-run here.** Re-reading the tree moves
the ledger, and the prereg allots one panel round on completion — CONV-024, now
spent.

**The direction of the hazard is recorded explicitly.** S1-C is length-adaptive,
was untouched by every defect found in this arc, and returned SIGNIFICANT at a2
(Δ = +6). If S3-C is restored, tree item 1 stops firing and **item 2 fires
DISP-T: THE FALSIFIER FIRES — indictment SUSTAINED, item 1B FAILS, Candidate (B)
fails requirement 7.** The worker is therefore repairing an instrument in the
direction that KILLS the programme's leading dark-matter candidate. GPT's
CONV-024 symmetry condition is satisfied not by argument but by the arithmetic:
this repair cannot rescue Candidate (B), it can only convict it or leave it
unadjudicated.

**On an S3C-RESTORED reading, CONV-025 is warranted under §2.1 (a WIN trigger —
"a closed falsifier campaign"), NOT as a definitional round.** The worker will
assemble it; the founder pastes once.

## §7 — Script

`code/3164_s3c_routeB_recipe.py`. Runs on the existing 2048 legs. No new
compute. Read-only. Prints the OLD and CORRECTED statistics side by side, the
resolution floor per arm, and the §4 reading — and prints NO disposition.
