# K-MEM-MEAS-3 (TAIL-1 ROUTE B) — EXECUTION RECORD — Patch 3047

**Executed 9 Aug 2026 under the FROZEN preregistration
`kmem_meas3_routeB_prereg.md` (Patch 3027, §1–§3 untouched; gate as
amended Patch 3025). Script `code/3028_kmem3_analysis.py` run VERBATIM,
exit 0, against the founder-committed `data/kmem3` (384/384 legs,
Kila6, committed 9 Aug 2026). Evidentiary standing: NONE until
panel-adjudicated. Per the Patch 3025 economy ruling, DISP-I is
round-worthy (instrument-fail = genuine impasse requiring diagnosis);
this record plus the Route A record (`kmem_tail1_record.md`, Patch 3026)
go to the panel in ONE round.**

## §1 — Manifest audit

384/384 legs present: 128 × d24, 128 × d28, 128 × d32.
Engine-fault exclusions: NONE (all 64 pairs × 3 domains × 2 branches
finite). No pair voided.

## §2 — Verbatim stdout

```
pairs used 64/64; engine-fault exclusions: none (voids the pair in ALL domains)
S1 d24 (x_half=24.0): tail = 6.631e-03 (scale 6.273e-04, nb=108, ntail=10) -> SIGNIFICANT; S2 peak period P = 17 Moments (in lowest ntail bins: False)
S1 d28 (x_half=28.0): tail = 5.426e-04 (scale 4.429e-04, nb=108, ntail=10) -> consistent with zero; S2 peak period P = 45 Moments (in lowest ntail bins: True)
S1 d32 (x_half=32.0): tail = 1.516e-04 (scale 5.614e-04, nb=108, ntail=10) -> consistent with zero; S2 peak period P = 16 Moments (in lowest ntail bins: False)
S1 ratios (matched bootstrap, 16 chunks x 4, NBOOT=10000, seed 30281001): R(28/24) 99% CI [-0.668, 1.911] (contains 1: True); R(32/28) 99% CI [-51.212, 62.539] (contains 1: True)
S2 peak periods ['17', '45', '16'] -> AMBIG
S3 d24: S_sust = 1.022e-03 (99% CI [4.499e-04, 1.605e-03]) detected=True, within factor 2 of 2.6e-03: False
S3 d28: S_sust = 1.625e-03 (99% CI [1.190e-03, 2.180e-03]) detected=True, within factor 2 of 2.6e-03: True
S3 d32: S_sust = 8.329e-04 (99% CI [3.007e-04, 1.360e-03]) detected=True, within factor 2 of 2.6e-03: False
S3 positive control (pass criterion = x=24 domain): FAIL
----------------------------------------------------------------------
DISPOSITION: DISP-I INSTRUMENT/EXPECTATION — the sustained-response positive control failed; no tail interpretation issues from this campaign; route = instrument diagnosis; the falsifier is untouched; no retune.
Evidentiary standing: NONE until panel-adjudicated (prereg 3027; single-round rule per Patch 3025).
```

## §3 — Enacted disposition: DISP-I INSTRUMENT/EXPECTATION

Per the frozen §3 tree (first branch, evaluated first): S3 FAILS →
DISP-I. **No tail interpretation issues from this campaign. The
registered exportable falsifier is untouched.** T-3 §6 / B-1 L-4 /
L-6 remain INDICTED-PENDING-DISPOSITION (unchanged from Route A).

## §4 — Facts of record (stated without interpretive upgrade; weight
is the panel's to assign at the round)

1. **S3 at x=24 detected but out of band:** S_sust = 1.022e-3 (99% CI
   [4.50e-4, 1.61e-3]) — DETECTED (CI excludes zero), but 2.55× below
   the lower bound of the factor-2 band around 2.6e-3 (band =
   [1.3e-3, 5.2e-3]). The pre-vs-post construction CAN see the
   sustained response, but the measured value is approximately 2.5×
   smaller than the 2918 scale.
2. **S3 at x=28 passes:** S_sust = 1.625e-3 (CI [1.19e-3, 2.18e-3])
   — detected AND within the factor-2 band. S3 at x=32: 8.33e-4,
   detected, out of band low. The instrument does not give a consistent
   reading across domains.
3. **S1 tail collapses across domains:** d24 significant (6.631e-3),
   d28 not (5.426e-4), d32 not (1.516e-4) — a monotone drop spanning
   two orders of magnitude from x=24 to x=32. This is a new pattern
   not present in Route A (which had a sign inversion at 2× domain
   change; here a finer grid shows the tail is concentrated at x=24
   and essentially absent by x=28).
4. **S2 AMBIG:** peak periods [17, 45, 16] Moments — no monotone trend,
   no lowest-bins pattern. The absence of a systematic S2 class is
   consistent with DISP-I (the pattern is noise-level at x=28/32 and
   a single-domain artifact at x=24).
5. **Ratio CIs are extremely wide:** R(32/28) 99% CI [−51, +63]
   reflects that both d28 and d32 tails are near zero — dividing two
   near-zero quantities with bootstrap noise gives a nearly uninformative
   ratio. This is consistent with the tail being a single-domain
   phenomenon.
6. **Instrument diagnostic hypothesis:** the x=24 domain may be
   geometrically special — at x_half = 24, the source travel distance
   is 36 Moments (= T_BALL, the frozen ballistic window), meaning the
   source exits the domain at exactly the ballistic/post-transient
   boundary. This could concentrate edge-reflection or boundary-mode
   energy into the x=24 PSD at a specific frequency (period ~17
   Moments), producing a domain-specific artifact the S3 out-of-band
   reading corroborates. This is a diagnosis candidate FOR THE PANEL,
   not a worker ruling.

## §5 — Panel round remit (single round, Route A + Route B together)

The panel receives:
- `kmem_tail1_record.md` (Patch 3026, Route A, DISP-C): transient-
  artifact hypothesis FALSIFIED; tail inverts sign in the doubled
  domain; T-D-EXPECTATION-DEFECT (D̄ scale did not apply as assumed);
  domain discriminator 2.080 uninformative (noise/noise).
- This record (Patch 3047, Route B, DISP-I): S3 positive control
  fails at the required domain (x=24); S1 tail collapses from x=24
  to x=28; ratio CIs uninformative; S2 AMBIG.

The panel's combined remit: (A) diagnose the instrument/expectation
defect (the S3 out-of-band reading and the S1 single-domain tail are
consistent with a geometric x=24 edge artifact, but this is a panel
determination); (B) assess whether any of the Route A or Route B
findings independently bear on the L-4/L-6 indictment; (C) determine
whether a Route C (corrected instrument) is warranted or whether
the geometric diagnosis retires the tail question. No retune before
the round.

## §6 — Ledger

Untouched: 1B OPEN (HOLD final); six of seven; PR7 PARTIAL; B7; 79.5%;
2855 PROVISIONAL; d_DP ceiling ACTIVE. Nothing here computes any value
of ξ₂, ζ, η, d_DP, n_DP, or N. Kila6 campaign total: ~663 CPU-h
(under the 721 estimate). Next patch: 3048.
