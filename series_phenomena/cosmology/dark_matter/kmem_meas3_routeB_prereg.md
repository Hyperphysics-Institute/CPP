# K-MEM-MEAS-3 (TAIL-1 ROUTE B) — DOMAIN-STRUCTURE PREREGISTRATION — FROZEN — Patch 3027

**Status: FROZEN AT COMMIT, before the driver or analysis code exists
(2967/2981 discipline; gate = the freeze alone per the Patch 3025
economy ruling — no sanction round; the panel attacks design + result
together at the single round when the disposition RESOLVES). Activated
by DISP-C of the Route A record (`kmem_tail1_record.md`, Patch 3026).
Founder resource commitment: campaign runs on Kila6 (registered this
session). Evidentiary standing of any result: NONE until
panel-adjudicated. No retune anywhere: every constant is carried from
2981/2983/3024 or frozen here before any leg runs.**

**What this resolves.** Route A established as facts of record: the
low-frequency excess is real (survives transient exclusion,
window-robust) and INVERTS SIGN between x_half = 16 and x_half = 32
(pre-registered CI rejects both R = 1 memory-type and R = 2 ballistic).
Route B maps the tail's domain structure across the sign-flip interval
at doubled frequency resolution, with a sustained-response positive
control that the T-D audit showed MEAS-2's statistic was blind to.

## §1 — Frozen design

- **Domains:** x_half ∈ {24, 28, 32} (annulus RHO = (1, 8), spacing
  2.5, aspect unchanged — "domain" = x-extent, as in MEAS-2). The
  MEAS-2 anchors (16, 32 at T_END = 240) remain auxiliary points at
  their own record; the new grid spans the flip interval interior.
- **Legs:** T_STEP = 24, β_F = 0.10, **T_END = 384** (post-step 360 =
  1.67× MEAS-2's frequency resolution), x_src0 = **−18.0** (transit
  β·(T_END−T_STEP) = 36 → ends at +18; margins 6/10/14 ≥ MEAS-2's
  5.2). 2907 jitter convention; identical-sea pairing; step flag the
  only step/ctrl difference; leg-atomic, resumable; control legs full
  window.
- **Pairs:** N = 64 per domain, ONE shared seed list across domains
  (matched pairs across domains): `default_rng(30280001).integers(1e6,
  1e7, size=64)`. Total legs = 64 × 2 × 3 = **384**. Data:
  `data/kmem3/`, `leg_{pair:04d}_{branch}_{d24|d28|d32}.json`.
- **Effort bound (WORKFLOW rule 3(i), pre-committed):** cost model
  measured from the MEAS-2 wall clocks (cost ∝ N_cp^2.06, linear in
  T): estimate ≈ 721 CPU-hours ClearPC-equivalent (per-leg ≈ 4930 /
  6676 / 8668 s at x = 24/28/32). The driver prints a running
  extrapolated total; **if after 24 completed legs the extrapolation
  exceeds 2× the estimate, PAUSE and report** (timing is not data; no
  peek). No mid-campaign result looks of any kind; the analysis
  refuses on an incomplete manifest.

## §2 — Frozen statistics

Analysis-level constants frozen here: bootstrap NBOOT = 10000, seed
**30281001**, CHUNK = 4 pairs (16 chunks at n = 64; deviation from
2983's CHUNK = 8 is set by n and frozen pre-look), CI = 99% percentile,
α = 0.01, Z = 2.576. Tail construction per domain exactly as 2983
(band (0, 0.6·ω_N], ntail = max(3, nb//10)) on F[T_STEP:]; blind
engine-fault exclusions only (NaN/Inf; exclusion voids the pair in ALL
domains).

- **S1 (domain profile):** per-domain tail statistic + significance;
  matched-pair bootstrap ratio CIs **R(28/24)** and **R(32/28)** (same
  chunk draw across domains).
- **S2 (frequency localization):** per domain, the peak-|residual| bin
  in the lower half-band, reported as period P(x) in Moments.
  **S2 = GEOMETRY** if P is strictly monotone in x_half across the
  three domains; **S2 = MEMORY-LOC** if the peak sits in the lowest
  ntail bins for all three; otherwise **S2 = AMBIG**.
- **S3 (sustained-response positive control):** per pair and domain,
  S_sust = [mean F(post window [300, 360)) − mean F(pre window
  [12, 24))]_step − [same]_ctrl. Pass = detected at α = 0.01 (block
  bootstrap) with mean within factor 2 of +2.6e-3 in at least the
  x = 24 domain. This closes the T-D loop: the pre-vs-post construction
  CAN see the sustained response; its absence would indict the
  instrument/expectation chain, not the tail.

## §3 — Frozen disposition tree (total by construction; evaluated in
this order, if / elif / elif / else)

1. **S3 FAILS → DISP-I INSTRUMENT/EXPECTATION.** No tail
   interpretation issues from this campaign; route = instrument
   diagnosis; the falsifier is untouched; no retune.
2. **elif [all three domains tail-significant] ∧ [both S1 CIs contain
   1] ∧ [S2 = MEMORY-LOC] → DISP-B′ MEMORY-CONFIRMED.** The registered
   exportable falsifier FIRES (T-3 §6 + B-1 L-4 + L-6); charter
   revision/HALT routing; the worker does not soften.
3. **elif [S2 = GEOMETRY] ∧ [at least one S1 CI excludes 1] →
   DISP-A′ GEOMETRY-ARTIFACT.** The excess is domain-geometry
   structure, not a memory kernel; the falsifier is UNFIRED; the
   L-4/L-6 indictment LIFTS subject to the panel's design review at
   the single round; OPEN-KMEM-TAIL-1 CLOSES there; the 1B bar re-arms
   pending D-KAPPA.
4. **else → DISP-M′ IMPASSE.** Genuine impasse (conflicted or
   insufficient pattern); the single panel round convenes with both
   instruments' designs and records on the table.

Any DISP class (including 2 and 3) reaches the panel at ONE round with
the Route A record; classes 2, 3, and 4 are all round-worthy under
WORKFLOW-REVIEW-ECONOMY (falsifier / win / impasse respectively);
DISP-I routes to diagnosis first.

## §4 — Ledger

Untouched by this prereg: 1B OPEN (HOLD final); six of seven; PR7
PARTIAL; B7; 79.5%; 2855 PROVISIONAL; d_DP ceiling ACTIVE. Nothing
here computes any value of ξ₂, ζ, η, d_DP, n_DP, or N. Driver and
analysis code commit at the NEXT patch citing this document.
