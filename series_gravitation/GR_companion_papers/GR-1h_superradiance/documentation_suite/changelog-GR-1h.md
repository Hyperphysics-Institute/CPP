# Changelog — GR-1h: Superradiance and Boson Clouds

**Paper:** `series_gravitation/GR_companion_papers/GR-1h_superradiance/GR-1h_superradiance.tex`
**Convention:** canonical filename never carries a version suffix.

**STATUS: reconstructed** at the Session 152 suite pass.

---

## V1 — 18 March 2026

Sole recorded version. Written as part of the March batch with c11
(GR-1f) and c12 (GR-1g); authoring history not captured.

## Re-identification — 19 August 2026, Patch 3230 (Session 149)

Moved into `series_gravitation/GR_companion_papers/` and re-identified
**c13 → GR-1h** (OPEN-ORG-023 Item 2, founder-approved layout).

## PD-001 formatting — 20 August 2026, Patches 3273–3274 (Session 150)

W-A: CP/GP Signature subsection added. **W-A2: a legacy compile defect
repaired** — the Planck-energy macro `\EP` was used but never defined;
defined alongside `\mP`. Compile: 0 errors.

## Documentation suite — 20 August 2026, Patch 3291 (Session 152)

OPEN-GR-PPP-1 W-B row 11 — **the final row; W-B is COMPLETE.** Ten-file
suite produced; this changelog created. **No staleness finding:** all
four open problems are genuinely open, and three of them turn on the
Planck-core reflectivity that GR-1d also needs and nobody has computed.
No .tex change.

## V1.1 — 20 August 2026 (Patch 3308) — RCORE delivery notes + F-R1/C* dependency audit

Occasion: the W-B shared-bottleneck finding (3 of this paper's 4 open
problems reduce to the Planck-core reflectivity) was DISCHARGED by
OPEN-GR-RCORE-1 (Patch 3297; CONV-030 5–0; founder-ratified). Notes
per the W-D form (original verbatim): OP-1 amplification — |R|=1 +
Dirichlet DELIVERED as input, wall relocated to the exclusion surface;
still open as posed (Teukolsky on the underived Kerr surface;
tensor/polar wall, RCORE-2(iii)/(iv)). OP-2 — "Planck-core bomb"
RE-FRAMED as the ergoregion instability of a horizonless spinning
perfect reflector (RCORE-2(iv), load-bearing for spinning-object
viability); scalar/vector wall open. OP-3 — reflectivity input
delivered, geometry input changed, saturation unposed against amended
geometry. OP-4 untouched (genuinely open, outside the arc). One
dependency-audit note at the threshold derivation (horizon-defined
Ω_+; c-vs-c_*; exterior Teukolsky agreement fenced). Compile: 0
errors, 10pp.

## V1.2 — 21 August 2026, Patch 3328 (Session 156)

Settled notes on founder-ratified CONV-032 (5/5). Two settled notes
appended beside the V1.1 status notes (originals verbatim,
anti-erasure): (1) the load-bearing ergoregion-instability item
("Planck-core bomb") RESOLVED at derivation-conditional grade — the
censorship theorem (Patch 3320) places the exclusion surface strictly
outside the ergosphere at every spin, so the gain loop cannot be
assembled at any spin or reflectivity, conditional on A1–A3; the
falsifier-shaped tension with observed BH spins is discharged on this
channel; the load moves to the conditionality itself (OPEN-GR-RCORE-4;
the panel's weighted-norm counterexample recorded in the note);
scalar/vector wall condition remains open (RCORE-2(iii)); Zel'dovich
surface channel named as the survivor with growth-time bounds
committed under amended RCORE-3. (2) Boson-cloud saturation — the
spinning geometry input is delivered (the derived co-rotating
saturation surface as inner boundary); the problem remains unposed,
only its geometry is now available. Compile gate: pdflatex ×2,
0 errors, 0 undefined refs, 11 pages.
