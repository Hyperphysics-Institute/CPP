# Changelog — GR-1b: Weak-Field General Relativity from the Two-Component LSP

**Paper:** `series_gravitation/GR_companion_papers/GR-1b_weak_field_GR/GR-1b_weak_field_GR.tex`
**Convention:** canonical filename never carries a version suffix.

**STATUS: partially reconstructed.** This paper predates the
documentation-suite convention; no changelog was kept. V3.2 and V3.3 are
recorded in the .tex `\date` block and are reproduced faithfully below;
the deltas of V1 → V3.2 were not recorded contemporaneously and are not
invented here.

---

## V1 – V3.1 — March–August 2026

Authoring and revision history not recorded. The paper's substance —
the two-component LSP, metric reconstruction, the factor of two, and the
self-consistency condition — is present across this period.

## V3.2 — 8 August 2026

The version standing in the primary `\date` line.

## V3.3 — 16 August 2026, Patch 3204 (F-SW-10 R-1 fix pass)

**OBL-CAL-LABEL applied to the cosmological-constant future-direction
item**, per R-CC-CALIBRATE (Patch 3125, CONV-020-endorsed). The Open
Problems entry (5) now carries the calibration label in full: the
residual DP-Sea SSV identifies a candidate *mechanism* only; the
*magnitude* of Λ is ruled NOT derivable from first principles at current
knowledge; d_s^emp = 4.636 is cosmology-calibrated, never predicted, and
is distinguished from the separately measured floor d_s* = 2.450 ± 0.091.
The earlier "zero-parameter mechanism brackets the observed Λ" language
was **withdrawn at CONV-020**. Mathematics untouched.

## Re-identification — 19 August 2026, Patch 3230 (Session 149)

Moved into `series_gravitation/GR_companion_papers/` and re-identified
**c07 → GR-1b** (OPEN-ORG-023 Item 2, founder-approved layout).

## PD-001 formatting — 20 August 2026, Patches 3273–3274 (Session 150)

W-A: CP/GP Signature subsection added. **W-A2: three figures created.**
The paper's three SVG figure assets had never existed in-repo — the
captions were shipped without the images. Drawn to the shipped captions
(matplotlib → PDF, committed): the four-component LSP channel map with
the equal weak-field potentials; the lensing geometry with α = 4GM/c²b;
the PSR-contraction curve with the exclusion radius. The .tex was
switched from `svg` to `graphicx` (inkscape dependency removed) and a
stray `\svgsetup` dropped. Compile: 0 errors.

## Documentation suite — 20 August 2026, Patch 3283 (Session 152)

OPEN-GR-PPP-1 W-B row 5: ten-file suite produced to the SPIN-3 standard,
and this changelog created. **A staleness finding was registered during
the pass** (see `phenomena-GR-1b.md` and the sector file): the paper's
§Open Problems still lists items (2) exact Schwarzschild and (3) Kerr as
open, both delivered since by GR-1c and GR-1f. No .tex change made —
the correction is scoped to the founder as a proposed W-D pass across
the legacy companions, not executed unilaterally inside a suite patch.
