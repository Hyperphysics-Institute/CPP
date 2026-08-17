# F-SW-10 · R-1 + R-3 FINDINGS AND AUDIT CLOSE RECORD (Patch 3204)

**Charter:** `3140_fsw10_post_cc_subpsr_delta_audit_charter.md`.
**This note closes F-SW-10.**

---

## §1 — R-1: OBL-CAL-LABEL exposure (1 PROSE-LAYER site, FIXED)

**Swept against:** R-DS-EQUILIBRIUM / R-CC-CALIBRATE (Patch 3125,
CONV-020-endorsed 5/5). The Sea's spacing is a kinetic equilibrium; Λ's
magnitude is not derivable from first principles at current knowledge;
`d_s^emp = 4.636` is **always** cosmology-calibrated (OBL-CAL-LABEL), distinct
from the measured floor `d_s* = 2.450 ± 0.091`.

**Exposure is a single site.** Grep across `series_relativity` and
`flagship_papers` for cosmological-constant, vacuum-energy, vacuum-density,
dark-energy, `d_s^emp`, `4.636`, `2.450`, and Sea-spacing vocabulary returns
exactly one hit in the shipped `.tex` corpus:

`c07_weak_field_GR.tex` §779, a future-directions item: *"The residual SSV of
the DP sea in the absence of matter is a candidate for the cosmological
constant."*

**Classification: PROSE-LAYER, not overclaim.** The wording is already hedged —
*a candidate for*, not *derives* or *predicts* — so it does not assert the
first-principles magnitude that 3125 withdrew. But a reader meeting it in a
shipped paper after 3125 would reasonably infer the programme still expects to
derive Λ from the substrate, which is precisely the expectation the ruling
retired. The mechanism identification survives; the magnitude expectation must
be explicitly disowned.

**Fix applied (c07 → Version 3.3):** a bracketed calibration label recording
that the item identifies a candidate *mechanism* only; that Λ's *magnitude* is
ruled not first-principles-derivable; that `d_s^emp = 4.636` is
cosmology-calibrated and never predicted, distinct from the measured floor
`d_s* = 2.450 ± 0.091`; and that the withdrawn CONV-020 bracketing language is
neither made nor implied. Mathematics untouched.

## §2 — R-3: fan-out and the ~10% band (1 PROSE-LAYER site, FIXED; 12 sites CONSISTENT BY INHERITANCE)

**Swept against:** R-OUTWARD-FANOUT (Patch 3135). At every hop a GP's received
DI-bit count splits equally among all neighbours with strictly positive outward
radial component (x·d > 0) — radial+tangential admitted, anti-radial excluded —
so total hop count varies with path. **F-E2-3 re-answered option (a): PSR
arrival is genuinely a band; the ~10% thickness is physics, not artifact,
reversing the 3134 §2 disposition.**

**Recon.** Thirteen PSR-shell propagation sites across six shipped papers: c01
(×4), c03, c07 (×3), c10, c14, SR-2 (×3). **No site asserts a sharp front in
those words**, but all describe transmission to "its PSR shell" / "one PSR
shell per Moment" — an exact shell, where 3135 establishes a band.

**Disposition — one fix, not thirteen.** The discrepancy is real but it is
*one conceptual item cited twelve times*, not thirteen independent defects.
c01 (`absolute_moment_postulate.tex`) is where PSR shell propagation is
**defined** for the series; the other twelve are references to that definition.
Amending the definition and marking it as inherited fixes the corpus once.
Editing all thirteen would force version bumps and PDF recompiles on six
shipped papers for a refinement that changes no result, and would add band
qualifications at sites where the leading-order law is the only thing being
invoked. **The proportionate action is to fix the definition, not every
citation of it.**

**Fix applied (c01 → Version 3.3):** band refinement recorded at the
definitional site — the fan-out rule, the ~10% band as substrate physics
(path-length variation), F-E2-3 option (a) and the 3134 §2 reversal — with an
explicit statement that *"one PSR shell per Moment" remains exact as the
leading-order propagation law*, that every result in the series is computed at
that order, that the band refines the arrival profile rather than correcting
the speed, and that **companion-paper shell language inherits this refinement
and is not separately qualified.** Mathematics untouched.

The twelve inheriting sites are classified **CONSISTENT BY INHERITANCE** and
require no edit. Future sweeps should not re-raise them.

## §3 — F-SW-10 CLOSE RECORD

| Item | Ruling | Verdict | Fix |
|---|---|---|---|
| **R-4** photon ontology | 3139 | CONSISTENT (12 sites) | 2 PROSE-LAYER → 3202 |
| **R-2** arc-cancel / turnaround | 3134 §3 | CONSISTENT (zero exposure) | 1 PROSE-LAYER → 3202 |
| **R-5** turnaround terminology | — | CONSISTENT | none owed |
| **R-1** CAL-LABEL exposure | 3125 | CONSISTENT | 1 PROSE-LAYER → 3204 |
| **R-3** fan-out / band | 3135 | CONSISTENT | 1 PROSE-LAYER → 3204 |

**SUBSTANTIVE findings across all five items: ZERO.** No panel round is owed;
nothing rides to CONV-021 from F-SW-10. The five rulings of Session 147 are
consistent with the SR and flagship corpora.

**Papers touched:** SF-6 (v1.3), c06 (2.3), c04 (2.1), c01 (3.3), c07 (3.3).
Mathematics untouched in all five. **PDF recompiles owed on all five** —
founder's mechanical action, batchable with the OSF pass (Patch 3203 manifest).

**Conventions registered during the audit:** CONV-022 (patch-lane reservation),
CONV-023 (turnaround terminology).

**Artifacts removed:** the misnamed c04 shadow copy in `c07_weak_field_GR/duplicates/`
(founder-authorized, Patch 3202).

### Items referred out of the audit (not defects, founder disposition invited)

1. **Arc-cancellation turnaround is unpublished mechanism** (R-2.1). It appears
   in no shipped paper. A publication gap, not a consistency defect.
2. **The founder's synchrotron account** — broad spectrum because no level
   structure constrains aggregation, only statistical opportunity — is a
   genuine explanatory addition not previously in the corpus. Now in SF-6
   §Emission; flagged as a candidate for fuller treatment in an SF-6 phenomena
   companion.
3. **Two surviving draft files** in `c07_weak_field_GR/duplicates/`, byte-identical
   to each other, quarantined pending disposition.
4. **`paper_catalog.md` is two months stale** and is the reason the OSF question
   could not be answered from the repo (Patch 3203 manifest §1).

**F-SW-10 CLOSED, 16 August 2026.**
