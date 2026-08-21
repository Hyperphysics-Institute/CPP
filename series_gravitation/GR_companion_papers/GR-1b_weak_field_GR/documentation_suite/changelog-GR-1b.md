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
(committed **as SVG only** — this file's original wording said "matplotlib
→ PDF, committed", which was a reconstruction error; see the V3.4 entry
below): the four-component LSP channel map with
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

---

## V3.4 — 20 August 2026, Patch 3293 (Session 153) — **figures actually render**

**The W-A2 figure work was incomplete, and this changelog mis-stated
it.** Patch 3274 created the three figures the paper had always cited
without possessing — but committed them **as SVG only**, while switching
the .tex from the `svg` package to `graphicx`. `pdflatex` cannot read
SVG. Compounding it, the `\includegraphics` calls name bare filenames
(`fig1_lsp_metric.pdf`) while the assets live in `figures/`, and no
`\graphicspath` was set.

**Consequence: the paper has never rendered its figures.** It compiled
with three `pdftex.def` "file not found" errors and three draft-mode
placeholder boxes — including at the moment W-A2 recorded "compile:
0 errors," which was measured before the graphics switch took effect or
in a context where the errors were not surfaced.

**Fix (this patch):** the three SVGs converted to PDF (cairosvg) and
committed alongside them; `\graphicspath{{figures/}}` added after the
`graphicx` load. Nothing else touched.

**Verification:** compile gate run **before** the edit (3 errors,
16 pages, 267 KB) and after (**0 errors**, 14 pages, 532 KB). The page
count *dropping* while the file size doubles is the confirmation that
matters — draft-mode placeholder boxes were larger than the real
figures, so the count falling proves the images are now actually being
included rather than stubbed. One `natbib` undefined-citation warning is
**pre-existing** and unchanged by this patch (present in the baseline
log); it is not addressed here and is recorded for a future pass.

**Also corrected above:** this file's V3.3/W-A2 entry, written during the
Patch-3283 suite pass, stated the figures were committed as PDF. That
was a reconstruction error on my part — the repository contained only
SVGs — and the sentence is amended in place rather than deleted.

---

## V3.5 — 20 August 2026, Patch 3294 (Session 153) — **W-D status notes**

OPEN-GR-PPP-1 **W-D**, executed on the scope the W-B pass established.
Dated status notes added to Open Problems (1)–(3), anti-erasure: the
original item text is retained **verbatim** and each note is appended
beside it, naming the delivering companion *and its limits*.

- **(1) Full nonlinear Einstein equations** — STILL OPEN as stated, and
  substantially advanced (T-1 from the messenger census, CONV-027;
  GR-1c's corrected Proposition proven equivalent). What this item names
  — producing the Ricci tensor — is untouched. `op:einstein`.
- **(2) Exact Schwarzschild** — DELIVERED, GR-1c Theorems 1 and 2. The
  note also records that **neither theorem has been externally
  reviewed**, since CONV-027 examined GR-1c's field-equation Proposition
  only.
- **(3) Kerr metric** — DELIVERED, GR-1f (with GR-1g for Kerr–Newman),
  carrying forward the caveat that GR-1f shows consistency at all orders
  rather than deriving Σ and Δ (`op:allorders`, open).

**(4) Big Bang, (5) cosmological constant, and (6) qDP chaining are
untouched** — (4) and (6) are genuinely open and outside this arc, and
(5) already carries its own V3.3 calibration label, which says more than
a status note would.

Compile gate clean (0 errors, 14 pages). No technical content changed.
