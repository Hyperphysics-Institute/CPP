# Re-registration under reach-S (founder adjudication 2556) — corrected pin E_close(16) = [+152.7, +156.9] MeV (G1 PASS, G2 fail, tighter); FORM-L corrected table makes the (20, 24) sign change UNION-STABLE; curve-shape classifier sensitivity flagged for the panel

**Patch 2557, 18 July 2026.** Verify: `code/2557_reregistration_reach_s.py` (P1–P3 readings
frozen in the docstring before any run; executed in staged runs, outputs assembled; control
assertion passed: reach-S ≡ reach-G on straight rods — the drift is ring/bent-only, so the
ENDBOND-2 fragment results are untouched).

## 1. Corrected ENDBOND-3 pin (P1)

Curve barrier-free in all six cells under reach-S (κ* = 0, stable — the knob-free
extraction is classifier-robust). **Corrected pin: E_close(16) ∈ [+152.7, +156.9] MeV**
(spread 4.2 vs reach-G's 8.6; ±2 floor rider). Pre-registered re-gating: **G1 [40, 170]
PASS** (nearer the top of the band); **G2 102: FAIL** (midpoint offset +52.8). Status
remains **banked pin**. The reach-G band [+128.9, +137.5] is annotated
superseded-by-correction for ring use; ΔE_close(16) = **[−156.9, −152.7] MeV** — the
correction riders on `endbond3_ra_curve.md` and `rodclose1_ra_statics.md` §7 carry it
downstream (kT_form still NOT collapsed).

## 2. Corrected FORM-L table (P2 — the 2553 frozen readings re-applied verbatim)

L = 8: +83..+84; 10: +122..+137; 12: +122..+125; 14: +141..+147; 16: +153..+157;
20: **+179..+193**; 24: **−13..−19**. Argmax union-stable at L = 20. **The (20, 24) sign
change is now UNION-STABLE in all three dt cells, beyond floor on both sides.** The 2553
§4 upper-cutoff fence still governs in-campaign (re-applied verbatim per P2): the claim
remains fenced; the structure is **promotion-READY** for OPEN-DM-FORM-L-2, which is held
per 2556 §4 pending the founder's read of the why-L=24 explanation. No claims on the
L = 10/12 wiggle (floor-overlapped).

## 3. Flagged for the panel packet (banked observation, no claim)

The curve's *shape* is classifier-sensitive at intermediate κ even though the endpoint
difference is not (ΔE_close moved only ~20 MeV): under reach-S, nearly the full ring
preference appears already at κ/κ_ring = 1/5 (⟨E⟩ drops ~130 MeV from straight to the
first bent point, then runs roughly flat to a modest seam drop), whereas reach-G showed
the collective drop at 3/5 → 4/5. Two candidate readings, neither claimed: the straight
rod is a high-symmetry configuration that any bending unlocks (physical), or reach-set
discreteness at bent geometries moves energy between κ-points (instrumental). The
knob-free conclusions (barrier-free; endpoint pin) are robust to this; intermediate-κ
interpretation is not, and the CONV-001 packet should say so — alongside the standing
invitation to hunt other straight-rod-era operationalizations (2555).

## 4. Bookkeeping

79.5 % untouched (P3; promotion basis — ring−rod sign consistency — strengthened under
correction). Standing disclosure package (now 8 items) updated with the corrected values.
Queue: founder read of the L=24 explanation → FORM-L-2 (if go) → NB-S3a-1 scoping charter
(founder priority) → plane-resident-fraction limb → δ_E → MW-MODES TC-extension. Next
patch: 2558.
