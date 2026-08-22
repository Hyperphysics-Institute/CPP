# PREREGISTRATION — **OPEN-BAND-CONV-1 (S1): THE FULL-FIDELITY POLARIZATION→FORCE CONVERSION** using the ACTUAL archived a1 map, not a parity assumption

**Patch 3185, 22 August 2026. Container. Frozen before the
computation runs.** Successor to 3176, which computed the factor under
two ASSUMED parities (uniform, odd) and disclosed: *"the full a1
spatial profile is not archived in a form this script can read."*

## §1 — The correction to that disclosure

**The profile IS archived.**
`flagship_papers/electromagnetism/data/2914_response_fields.json`
holds the co-moving response map as **72 bins = 24 ξ-bins (−12…+12,
width 1) × 3 ρ-rings ([1,3], [3,5], [5,8])**, with per-bin `m`
(mean p_x), `se`, `N`, and `ux`, at **β ∈ {0.05, 0.10, 0.20}** — the
exact structure `2914_response_field.py` writes. 3176's bounds
(inner-only vs all-ring, uniform vs odd) can therefore be **replaced
by the measured profile itself**, sign structure included. This is
what S1 was chartered to do.

## §2 — Method (frozen)

1. Build the 2914 Sea (`build_sea_sym`, classes A and B, seeds 4,5,6 —
   the 2918 grid), exactly as 3176 did; same engine force law
   (`amp = 1/(4π(R²+SOFT2))`), same exact two-member sum, source at
   the origin.
2. For each pair, compute its baseline (ξ, ρ) and look up **its own
   bin's measured p_x** from the archive at that β. Pairs outside the
   binned domain get **zero** increment (the map does not cover them;
   assuming otherwise would re-import the error 3176 caught).
3. Impose δp_x = (that bin's m) on each pair — the MEASURED profile,
   with its own signs — and recompute the source's axial force.
4. **F_MAP(β) ≡ ΔF_x** — the axial source force actually implied by
   the measured polarization map. This is the corrected comparator,
   in force units, directly comparable to `sust_B`.

## §3 — Frozen statistic, floor, falsifier (§9 hygiene)

- **Statistic:** F_MAP(β) for β ∈ {0.05, 0.10, 0.20}, in engine force
  units, reported as the mean over the six (class, seed) geometries.
- **Resolution floor:** the across-geometry standard error, reported
  beside every value; PLUS the archive's own per-bin `se` propagated
  as a second, independent floor. **Both reported.**
- **Falsifier / abort:** if the two floors disagree by more than 3×,
  or if F_MAP's sign is not stable across the six geometries, the
  comparator is declared **UNSTABLE** and no arm re-comparison is
  performed — the outcome the strategy named as "conversion too
  uncertain, retire the comparator permanently."

## §4 — Frozen readings for the re-comparison (only if §3 passes)

Against the corrected comparator F_MAP(β), each existing arm's
measured sustain value is classified:
- **IN-BAND** iff |measured| ∈ [F_MAP/2, 2·F_MAP] (the corpus's
  standing factor-2 convention, frozen here, NOT inherited).
- **ABOVE-BAND** / **BELOW-BAND** otherwise, with the ratio quoted.
Aggregate readings, frozen:
- **ANOMALY-DISSOLVES** iff a majority of arms are IN-BAND ⇒ DISP-I3's
  evidentiary basis is void and it must be re-adjudicated.
- **ANOMALY-INVERTS** iff a majority are ABOVE-BAND ⇒ a new
  one-directional signature, opposite in sign to DISP-I3's, needing
  its own account.
- **ANOMALY-SURVIVES** iff a majority are BELOW-BAND ⇒ DISP-I3's
  pattern stands against a valid comparator for the first time.

## §5 — Hazard direction (declared)

**ANOMALY-SURVIVES is favourable to the DM programme; ANOMALY-DISSOLVES
destroys five campaigns' headline reading.** The worker's pre-declared
expectation: **ANOMALY-INVERTS or ANOMALY-DISSOLVES** — because 3176
found the transplanted band too large by ≥130×, and a corrected
comparator that much smaller will sit far below arms that were
previously called undershoots. Recorded before F_MAP exists. The
worker's last two pre-declarations were scored NOT-CONFIRMED and
WRONG; this one is exposed identically.

## §6 — Fence

No engine legs, no new campaign, no Kila6 time. Nothing here moves
DISP-I3, the ledger, Candidate (B), or any DE-lane quantity. The
suspended COEFFICIENT-OVERPREDICTED finding stays suspended
regardless of outcome — this patch supplies a comparator, not a
coefficient verdict.
