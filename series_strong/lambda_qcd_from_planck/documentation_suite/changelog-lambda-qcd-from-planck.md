# Changelog — Λ_QCD-from-Planck arc

All notable changes to this derivation arc, newest first. One block per patch.

## Patch 1001 — 2026-06-10 — Scaffold + step-0 framing

- **Added** arc folder `series_strong/lambda_qcd_from_planck/` (1000-series parallel lane).
- **Added** `README.md` — target (Λ_QCD ≈ 0.218 GeV + DP spectrum from l_P + sea_strength, no PDG
  input), mechanism (PSR saturation, `rem:psr`), Routes A/B with **B (non-log/discreteness) set as
  primary**, falsifier, C14 convention flag, on-success path.
- **Added** `1001_step0_uv_boundary_framing.md` — reduces the project to one open number,
  `α_s(E_P)`; shows the IR end self-consistent; fixes Route B's target reframing.
- **Added** `code/verify_ir_anchor_selfconsistency.py` — 3 framing checks, all consistent:
  (1) `5/(8φ)` ↔ Q ≈ 2.2 GeV IR anchor; (2) one-loop UV boundary `α_s(E_P) ≈ 0.0197`;
  (3) C14 `α_s ≈ 0.118` ≠ lattice `0.386`.
- **Added** `reasoning/1001.md` — verbatim reasoning (capture protocol).
- **No** THEO/PRED registered; **no** edit to SS-1 or the DP-Sea appendix (STOP-and-warn files).
- **Next (Patch 1002):** open Route B — lattice-discreteness-corrected flow from `PSR_eff → l_P/2`.
