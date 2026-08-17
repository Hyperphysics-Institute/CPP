# K-MEM ROUTE C — CAMPAIGN COMPLETION AND FROZEN DISPOSITION RECORD

**Patch 3160, 17 August 2026. Kila6. Status: CAMPAIGN COMPLETE (2048/2048
legs), manifest verified, frozen analysis executed, disposition printed.
Evidentiary standing: NONE until the single panel round (prereg v2 §5).**

Governed by `kmemC_routeC_prereg_v2.md` (Patch 3055) and its v2.1 window
amendment (Patch 3057). No retune after launch. No interim look was taken:
the analysis was run exactly once, on a complete manifest, after the driver
printed `CAMPAIGN COMPLETE`.

---

## §1 — Execution record

Launched on Kila6 (32 logical cores, CPU engine `2902_mobile_sea_engine.py`
per prereg §7; no GPU port). Wall-clock span 10–17 August 2026.

| Arm | Class | Δ | N (pairs) | Files | Max leg | Status |
|-----|-------|---|-----------|-------|---------|--------|
| a0  | iso   | +0  | 128 | 256  | 0127 | complete |
| a0p | iso   | +0  | 128 | 256  | 0127 | complete |
| a1  | iso   | −12 | 128 | 256  | 0126 | complete |
| a2  | iso   | +6  | 128 | 256  | 0125 | complete |
| ak  | margin| +6  | 512 | 1024 | 0511 | complete |
| **total** | | | **1024** | **2048** | | **complete** |

Per-leg wall times were stable to under 1% within each arm across the whole
campaign (a0p ≈ 2400 s, ak ≈ 2990 s, a0 ≈ 7430 s, a1 ≈ 12900 s, a2 ≈ 14390 s);
the final AK batch ran ≈ 2180 s/leg as the worker pool exceeded the remaining
leg count. Aggregate ≈ 3900 CPU-h, consistent with the prereg §6 estimate of
≈ 3720 CPU-h at full N.

**Interruptions and their disposition.** The campaign survived six hard
machine halts (frozen console, black display, unresponsive input, hard
power-cycle required; Kernel-Power 41 + EventLog 6008 with NO WHEA-Logger
entries at any halt). Diagnosis: an ASUS auto-overclock enhancement gated on a
90 °C threshold, holding all-core boost past stock indefinitely under sustained
load — a CPU hard-hang, not a power-delivery trip (1200 W supply, package temps
60–70 °C throughout). Disabling the enhancer extended clean uptime from ≈ 8 h to
≈ 36 h; a subsequent reset to factory-optimized defaults carried the campaign to
completion. **No leg is affected.** Leg-level checkpointing means each halt cost
only in-flight legs, which were recomputed from scratch on resume. The integrity
sweep below is the evidence, not the assurance.

## §2 — Manifest integrity sweep (run before the analysis, on the complete set)

- File count: **2048** in `data/kmemC/` (`-maxdepth 1`; the 8 evidence-excluded
  pilot legs in `data/kmemC/pilot/` are correctly outside the manifest).
- Per-arm counts: 256 / 256 / 256 / 256 / 1024 — every arm at its exact
  preregistered allocation. No overrun, no shortfall.
- **Unpaired legs: zero.** Every `pair` index carries both `ctrl` and `step`.
- **Truncated files: zero** (no file under 1 KB).
- **Unparseable files: zero** (every file `json.load`s clean).

The pairing and parse checks were run specifically because of the halts: a leg
written while the machine froze mid-write would surface as a short or
unparseable file. None did.

## §3 — Analysis-script defect and its correction (made BLIND to all results)

The first invocation of `code/3055_kmemC_analysis.py` aborted at line 40:

```
KeyError: 'beta_f'
```

**Diagnosis.** Line 40 read `beta_f = rep['beta_f']`, where `rep` is
`data/kmemC/pilot_report.json`. That artifact is arm-specific to AK and carries
projection statistics only — `{arm, N_projected, peakD, sd_pair, SNR, status}`.
It has never contained a `beta_f` key and does not need to. The authoritative
per-arm β lives in `calibration.json` (0.10 × 4 isolation arms, 0.60 at AK) and
is stamped in every leg file.

**The assigned name was never read again.** Every use of β in the script is the
per-arm `beta` unpacked from the module-level `ARMS` table:

- line 43 — `for tag, cls, x_half, T_END, beta, _N, _dt in ARMS:` (loop unpack)
- line 62 — same unpack in the statistics loop
- line 63 — `band = SUST_REF0 * beta / 0.10` — **the only place β enters any
  computed number**, and it is sourced per-arm from `ARMS`, whose β values
  (0.10, 0.10, 0.10, 0.10, 0.60) match `calibration.json` and the leg stamps
  exactly.

**Origin.** The `3054 → 3055` diff shows it: `3054` carried a flat
`ARMS = [(tag, role, n, x)]` with a single global β context. The v2 rewrite moved
β into the per-arm tuple and left the pilot-report fetch behind, orphaned.

**The correction is deletion of line 40 — nothing substituted, nothing
re-sourced.** Because the value was never read, the deletion is provably
behavior-preserving: it cannot alter any computed number. The frozen §4–§5
estimator is untouched. `rep` remains in use for `N_projected`.

**Ordering, stated for the record:** the defect was diagnosed and the deletion
applied BEFORE any statistic, disposition, or arm result had been printed or
seen by worker or founder. This is a code repair, not a retune; it is disclosed
here in full with its diff so the panel may judge it rather than take it on
trust.

## §4 — Frozen output, verbatim

```
[a0|iso|DT=+0] pairs 128/128  S3-C: sust=1.095e-03 band[1.30e-03,5.20e-03] -> FAIL  S1-C: tail=7.690e-03 (scale 1.769e-04) -> SIGNIFICANT  kappa_sys[BOUND]=0.9985 99%CI[0.6545,1.0288]
[a0p|iso|DT=+0] pairs 128/128  S3-C: sust=4.575e-04 band[1.30e-03,5.20e-03] -> FAIL  S1-C: tail=3.643e-03 (scale 1.526e-04) -> SIGNIFICANT  kappa_sys[BOUND]=1.0049 99%CI[0.6510,1.0643]
[a1|iso|DT=-12] pairs 128/128  S3-C: sust=3.389e-05 band[1.30e-03,5.20e-03] -> FAIL  S1-C: tail=1.898e-04 (scale 1.489e-04) -> c.w.z.  kappa_sys[BOUND]=0.9925 99%CI[0.7348,1.0146]
[a2|iso|DT=+6] pairs 128/128  S3-C: sust=1.451e-04 band[1.30e-03,5.20e-03] -> FAIL  S1-C: tail=5.551e-03 (scale 2.849e-04) -> SIGNIFICANT  kappa_sys[BOUND]=1.0290 99%CI[0.9333,1.0407]
[ak|margin|DT=+6] pairs 512/512  S3-C: sust=7.627e-05 band[7.80e-03,3.12e-02] -> FAIL  S1-C: tail=-1.179e-03 (scale 1.956e-05) -> SIGNIFICANT  kappa_sys[BOUND]=0.9928 99%CI[0.7353,1.0059]
----------------------------------------------------------------------
DISPOSITION: DISP-I3 INSTRUMENT — fewer than two isolation arms pass S3-C, or AK fails S3-C; no standing; panel.
Evidentiary standing: NONE until the single panel round (prereg v2, Patch 3055 §5).
```

## §5 — Reading against the frozen tree

**Tree item 1 fires: DISP-I3 (instrument; panel).** All five arms FAIL S3-C —
both limbs of item 1 are satisfied independently (fewer than two isolation arms
pass, AND AK fails).

**The S3-C failure is universal and one-directional.** Every arm undershoots its
band's lower edge; not one overshoots, and not one lands inside:

| Arm | sust | band low | sust / band-low |
|-----|------|----------|-----------------|
| a0  | 1.095e-03 | 1.30e-03 | 0.84 |
| a0p | 4.575e-04 | 1.30e-03 | 0.35 |
| a1  | 3.389e-05 | 1.30e-03 | 0.026 |
| a2  | 1.451e-04 | 1.30e-03 | 0.11 |
| ak  | 7.627e-05 | 7.80e-03 | 0.0098 |

Arms differing in geometry (x_half 16–32), in horizon (T_END 104–504) and in
drive (β 0.10 vs 0.60) failing the same way in the same direction, across two
orders of magnitude of shortfall, is the signature the DISP-I3 branch exists to
catch. AK's band is 6× the isolation band by the frozen `β/0.10` scaling, which
is why its ratio is the most extreme. Note also that a0 misses by only 16% — a
near-miss that a modest band or window error would flip.

**THE PRE-EMPTION — the most consequential fact in this record.** The tree is
evaluated in order. Item 2 reads: *S1-C SIGNIFICANT in ANY valid Δ ≠ 0 arm →
DISP-T: THE FALSIFIER FIRES.* **a2 is a Δ = +6 arm and returned S1-C
SIGNIFICANT** (tail 5.551e-03 against scale 2.849e-04). Had item 1 not fired,
item 2 would have fired DISP-T — domain-robust control-valid tail, indictment
SUSTAINED, item 1B FAILS, Candidate (B) fails requirement 7.

**DISP-I3 is therefore the only thing standing between the corpus and a fired
falsifier against Candidate B.** This is stated plainly and up front because it
is precisely the circumstance in which a worker would be tempted to prefer the
instrument reading. The worker prefers nothing: item 1 fires first by the frozen
order, and the interpretive question — whether a2's tail is real evidence or an
artifact of the same defect that sank S3-C — belongs to the panel.

The §4 minority clause bears directly on it: *a failing INFERENTIAL arm is
PROSPECTIVELY NON-INTERPRETABLE and drops from inference.* a2 failed S3-C. If
the clause governs, a2 is not a "valid" Δ ≠ 0 arm and item 2 never had a
trigger. If it does not, the falsifier evidence stands and merely awaits an
instrument repair to be read cleanly. The clause was written for a minority of
failing arms, not for all five; the worker does not extend it by construction.

**P-ISO FAILS as printed.** S1-C SIGNIFICANT at both Δ = 0 arms (a0 7.690e-03,
a0p 3.643e-03) — satisfied. c.w.z. at every valid Δ ≠ 0 arm — a1 (Δ = −12)
returns c.w.z., a2 (Δ = +6) does not. Conditional on the minority-clause
question above.

**P-κ FAILS as printed, marginally.** The condition is κ_sys^{U99} < 1. AK
returns κ_sys[BOUND] = 0.9928 with 99% CI [0.7353, **1.0059**]. The upper bound
exceeds 1 by 0.6% — the condition is not met. *Correction owed to this record:
the worker's first verbal reading of this line to the founder stated that P-κ
was satisfied. That was wrong — the point estimate sits below 1, the U99 bound
does not, and the frozen condition is on the bound. The error is corrected here
before dispatch and is disclosed to the panel as Q4.*

**Two further features flagged, not interpreted.**
(i) AK's S1-C tail is **negative** (−1.179e-03) yet flagged SIGNIFICANT against
a very small scale (1.956e-05). A sign inversion in the margin arm is not
something the tail statistic was designed to return; per §4 the S1-C tail is an
**isolation-arm** statistic and AK is class `margin`, so this line is
non-gating — but it is printed, and it is anomalous.
(ii) The S3-C band derives from `SUST_REF0 = 2.6e-3`, a Route B reference
transplanted into Route C geometry and scaled only by β. Whether that transplant
is valid across the Route C arms is not something this campaign tested.

**Worker's hypothesis, offered for attack and adopted nowhere:** the fit window.
`t_post = t_step + 1.5·x_half + 6` with baseline `max(12, min(48, (T_END −
t_post)//3))`. The v2.1 amendment (Patch 3057) already corrected one defect in
exactly this arithmetic — caught by an executable gate rather than by reading,
and in the same family as the v1 exit-time error. A universal one-directional
sustained undershoot is consistent with a window that opens after the sustained
response has substantially decayed. This is a hypothesis about where to look,
not a diagnosis, and emphatically not a repair: **no retune after launch.**

## §6 — Standing and disposition

**DISP-I3 INSTRUMENT. Evidentiary standing: NONE until the single panel round.**

Nothing in this record moves the DM ledger. Item 1B neither discharges nor
fails. Candidate (B) requirement 7 is untouched. The ledger remains six of
seven; 79.5%.

Next: CONV-024 dispatch (Patch 3161).
