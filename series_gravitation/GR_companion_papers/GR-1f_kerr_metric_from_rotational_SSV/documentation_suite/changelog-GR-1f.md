# Changelog — GR-1f: The Kerr Metric from Rotational SSV

**Paper:** `series_gravitation/GR_companion_papers/GR-1f_kerr_metric_from_rotational_SSV/GR-1f_kerr_metric.tex`
**Convention:** canonical filename never carries a version suffix.

**STATUS: reconstructed** at the Session 152 suite pass.

---

## V1 — 18 March 2026

Sole recorded version; the `\date` line reads Version 1. Authoring
history not captured contemporaneously.

## Re-identification — 19 August 2026, Patch 3230 (Session 149)

Moved into `series_gravitation/GR_companion_papers/` and re-identified
**c11 → GR-1f** (OPEN-ORG-023 Item 2, founder-approved layout).

## PD-001 formatting — 20 August 2026, Patch 3273 (Session 150)

W-A: CP/GP Signature subsection added. Compile clean.

## Documentation suite — 20 August 2026, Patch 3289 (Session 152)

OPEN-GR-PPP-1 W-B row 9: ten-file suite produced; this changelog
created. **Staleness finding registered** (see `phenomena-GR-1f.md`):
two of the paper's four open problems were delivered by sibling
companions — the Kerr–Newman extension by GR-1g and superradiance by
GR-1h — both apparently written within days of this paper, with the open
problems never updated afterward. No .tex change; scoped to the proposed
W-D pass.

## V1.1 — 20 August 2026 (Patch 3306) — W-D status notes + F-R1/C* dependency audit

Per the fixed W-D form (reasoning/3294.md) and CONV-030 adoption 4
(audit BEFORE notes). Audit findings, each carried as a dated inline
note (original text verbatim): thm:kerr_bound consumes evaluation AT
the outer horizon AND the c-vs-c_* ceiling (both flagged; weak-field
LT/GP-B unaffected; bound's horizonless status open with RCORE-2(iv));
sec:horizons table tabulates would-be surfaces (r_± never reached;
ergosphere row survives; Kerr exclusion-surface geometry underived);
Penrose "falling into the horizon" re-read as surface
absorption/reflection with the |R|=1 ergoregion question live. W-D
notes: OP-2 Kerr–Newman DELIVERED by GR-1g (same-batch cross-reference
finding repaired); OP-3 Kerr echoes — Schwarzschild baseline CHANGED
(GR-1d V3), (a/r_S)² estimate unverified against amended baseline;
OP-4 superradiance DELIVERED at mechanism level by GR-1h with the
horizon-defined threshold flagged. op:allorders untouched (correctly
open). Compile: 0 errors, 10pp.

## V1.2 — 21 August 2026, Patch 3327 (Session 156)

Settled notes on founder-ratified CONV-032 (5/5,
`review/conv032_adjudication.md` v1.0). Three settled notes appended
beside the V1.1 dependency-audit notes (originals verbatim,
anti-erasure): (1) thm:kerr_bound — the Kerr-analog exclusion surface
is derived (Patch 3320, conditional on A1–A3); the bound relocates to
the derived surface as a register-capacity statement; the c-vs-c_*
question folds into the same conditionality. (2) Horizon-structure
table — the ergosphere row does not survive: the derived surface lies
strictly outside the ergosphere at every spin/latitude (min clearance
0.25 M); prograde photon ring buried for χ ≳ 0.55. (3) Penrose /
ergoregion-stability — resolved by the censorship theorem; no
exterior ergoregion at any spin or reflectivity; rotational-energy
extraction survives only via the Zel'dovich surface channel. All
settled content explicitly conditional-on-A1–A3 per the panel-adopted
prose law (OPEN-GR-RCORE-4 carries the substrate derivation).
Compile gate: pdflatex ×2, 0 errors, 0 undefined refs, 11 pages.
