# AP-5 owed item 8: the saturated-core neutron star under DRAIN. The core is not flat — it carries a pressure gradient at χ = cap/v_sea (≈ 0.78 at 2.08 M☉) of GR's — and the branch above the 1.78 M☉ threshold is a TOV-like sequence with reduced gravity: M_max rises 27–31% over GR at fixed EOS (SLy 2.05 → 2.61; APR4 2.19 → 2.87), radii at 2.08 M☉ change by < 0.15 km, and 3636's "rising radii above the knee" does NOT survive (dR/dM < 0, shallower than GR). The threshold stands; the knee is smoothed; stability is ordinary. The one surviving neutron-star fingerprint — a maximum mass ~30% above GR's for the same EOS — is degenerate with EOS stiffness at present. NS.2–NS.5 re-scored; GR-2 §(iv) owed a restatement (V2.9)

**Patch 3704, Session 166, 8 Sep 2026.** Verify `code/3704_saturated_core_under_drain_verify.py` (7/7, ~4 min). Reasoning `reasoning/3704.md`. EOS as transcribed at 3636 (Read et al. 2009 piecewise polytropes, recollection-flagged). Modes compared: GR (χ = 1), DRAIN (χ = min(1, cap/v_sea) in the core, matter lapse pinned at ½), STOP (χ = 0 in the core; 3636's flat core) for scale. The sea lapse is found by fixed-point iteration on the central lapse.

## §1 What DRAIN does to a star
Inside the region where the sea's lapse is below ½, matter acts on the K-of-D sample of the true force: dp/dr = −(e + p)(dν/2) χ with χ = cap/v_sea. For a 2.08 M☉ star the central χ ≈ 0.78. The core therefore keeps a pressure gradient — three-quarters of GR's — and the flat core of 3636 (χ = 0) is the STOP reading's artefact. The clock (matter lapse ½, 3703) is unaffected by and does not affect the statics.

## §2 Numbers (T1–T4)
| | SLy GR | SLy DRAIN | SLy STOP | APR4 GR | APR4 DRAIN | APR4 STOP |
|---|---|---|---|---|---|---|
| M_max (M☉) | 2.05 | **2.61** | 3.59 | 2.19 | **2.87** | 3.70 |
| M_thr (N_c = ½) | 1.77 | 1.77 | 1.77 | 1.78 | 1.78 | 1.78 |
| R at 2.08 M☉ (km) | — | 10.55 | 11.33 | 10.64 | 10.78 | 11.15 |
| dR/dM above the knee (km/M☉) | −5.0 | −2.0 | (rising) | −2.7 | −1.0 | (rising) |
- **The threshold stands** (it is the star on the ordinary branch at N_c = ½, before the cap acts).
- **The knee is smoothed:** DRAIN's branch continues the ordinary one with a shallower, still-negative dR/dM — the "radii rise with mass" signature of 3636/3637 belonged to STOP and is withdrawn.
- **M_max rises ~30% at fixed EOS** (×1.27 SLy, ×1.31 APR4): a soft EOS like SLy, which cannot make J0952 (2.35 M☉) in GR, makes it under DRAIN.
- **Radii at 2.08 M☉ are GR's within 0.15 km.** J0740's NICER radius (12.4 ± 1 km) is 1.6–1.9σ above both GR and DRAIN on these soft tables — the tension is the EOS's, and DRAIN neither creates nor relieves it.
- **Stability is ordinary:** M(ρ_c) rises to a maximum on a TOV-like sequence; 3637's "constrained equilibrium held by the cap" was STOP's problem and does not arise.

## §3 The sheet, re-scored
NS.1 threshold: **stands** (1.78 M☉), but not as an observable knee. NS.2 stability: **passes** (ordinary). NS.3 radius: **GR's** (no signature). NS.4 M_max: **~2.6–2.9 M☉, ×1.3 GR's** — the surviving fingerprint. NS.5 flat core: **withdrawn** (χ ≈ 0.78 gradient). NS.6, NS.7 unchanged (the core is a fluid with pressure under DRAIN; its k₂ is computable by 3685's machinery with χ — owed, low stakes). **What can test AP-5 in neutron stars now:** only the M_max boost, and only with an independent handle on the EOS (e.g., a radius measurement precise enough to pin the EOS, plus a mass above that EOS's GR maximum). Degenerate today; a definite target for NICER/XMM radii + heavy pulsar masses.

## §4 Consequences upstream
- GR-2 V2.8 §(iv) ("radii rising above the knee, maximum near 2.9") is wrong as printed; PRED-O-40's withdrawal (3703) also awaits the paper. **V2.9 owed** — one restatement carrying both.
- 3634 (threshold) stands; 3635–3637 (flat-core stars, EOS study, stability) are superseded by this patch's DRAIN branch; their records are kept as the STOP reading's results.
- AP-5 v1.0 owed list: items 4, 5, 6, 7 remain; item 8 done; add **9: the DRAIN core's k₂** (low stakes); **10: GR-2 V2.9.**
