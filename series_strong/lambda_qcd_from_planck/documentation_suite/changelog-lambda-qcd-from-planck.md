# Changelog — Λ_QCD-from-Planck arc

All notable changes to this derivation arc, newest first. One block per patch.

## Patch 1002 — 2026-06-10 — Route B opened: framework + sensitivity theorem

- **Added** `1002_routeB_discreteness_running.md` — Route B framework: Λ_QCD as the IR Landau pole
  of a flow fixed entirely by the UV boundary `α_s(E_P)`; PSR saturation (`rem:psr`) shown to fix
  the **sign** (`α_s(E_P) → 0`, asymptotic freedom from CPP); quantitative target `α_s(E_P) ≈ 0.0197`.
- **Proved** the **sensitivity theorem**: `dΛ/Λ = (N/α_UV) dα_UV`, amplification ≈ 2300× ⇒ `α_s(E_P)`
  must be derived to sub-percent (an *exact* relation); coincidence-matching at ~1% is ruled out as a
  method (2π² / S³-volume futility demo → Λ off by −33%).
- **Sharpened** Route B's target to: derive `α_s(E_P)` from the `PSR_eff → l_P/2` approach rate /
  600-cell mode structure, falsification-first.
- **Added** `code/verify_uv_sensitivity.py` — framework facts A–D, exit 0; carries a standing guard
  assertion that 1%-level factor matches are insufficient.
- **Added** `reasoning/1002.md`.
- **NOT closed**; no THEO/PRED; SS-1 and DP-Sea appendix untouched.
- **Next (Patch 1003):** derive the discreteness profile `g(Q)` / `PSR_eff → l_P/2` approach rate
  from the 600-cell mode count; read off `α_s(E_P)`; decide closure vs falsifier at the §4 precision.

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
