# S4-X X3/X4 EXECUTION RECORD (appended per completed leg; frozen 2786 prereg)

## LEG 1 — Requirement-7: high-resolution S_zz(k) vs HNC on archived clean chains (Patch 2787)

**Executed 2026-07-23. Zero new simulation — archived `data/rv2714/`
accumulations only, per the panel's own binding text (2765 item 7).
HNC = the committed 2721/2761 solver verbatim; self-validation gate
re-fired and PASSED before any comparison was read (slopes
1.0206/1.0042 vs committed 1.0206/1.0042; conv ≤ 9.9e−10). Script:
`code/2787_x3x4_req7_szz_hnc.py`. Reasoning: `reasoning/2787.md`.**

**DEVIATION DEV-1 (disclosed same-font; panel ratification
requested):** the 2786 prereg operationalized req-7 errors as
per-sample bootstrap; the archived szz arrays are time-averaged
accumulations with no per-sample record, so bootstrap is
unimplementable on the archive. Implemented error model (maximal
honest, matching the RV-3 battery's own precedent): between-chain
half-spread where two independent chains share a geometry (MAIN-A/B),
in quadrature with the committed ±1.5% HNC closure floor; single-chain
geometries report Δ(k) with the floor only, marked ADVISORY, no σ
quoted. Nothing about the frozen k-shell set, the HNC reference, or
the persistence criterion was altered.

**Result (verdict-grade, MAIN-A/B combined, N = 686, a_s = 0.04, 24
shells n² ≤ 27, k = 2.77–14.38 /fm — all inside the committed
k ≤ 2π/0.08 cut):** Δ(k) = S_zz^sim/S_zz^HNC is consistent with 1
across the full shell set. Extremes: mean Δ from 0.9715 ± 0.0178
(n² = 4, 1.60σ) to 1.0413 ± 0.0194 (n² = 12, 2.13σ). Exactly ONE
shell exceeds 2σ (n² = 12, k = 9.588, ABOVE unity — the opposite sign
to the real-space deficit); among 24 independent shells one > 2σ
excursion is the chance expectation. **Persistent > 2σ deficit
k-range: NONE.**

Advisory single-chain sweeps: SIZE-S worst |Δ−1| = 6.5% (n² = 4);
SIZE-L worst 7.3% (n² = 4, below unity at small k but within
single-chain scatter); CORE (a_s = 0.02) worst 5.3% (n² = 1) — no
coherent pattern across geometries; the n² = 4 shell is low in S and
L but high in the MAIN box, arguing shell-noise, not physics.

**Reading offered for adjudication (not enacted):** the F1 real-space
near-window deficit (2.56σ / 2.82σ) has NO conjugate-space
counterpart — S_zz(k) is HNC-consistent over the entire range dual to
the near window. This is the discriminant S2 requested, and it points
the same way as the majority physics read at 2764 §4
(extraction/profile-shape systematic favored over new physics): a
genuine screening-strength shift would appear in S_zz(k); a
window-localized profile-shape artifact would not. X3 (replication)
and the X4 sliding-window/two-component/moving-feature instruments
remain the arbiters; no PR line moves on this leg alone.

**Next legs (frozen order):** X3-R04 + X3-R02 chains (gate v2 first,
chunked); then X4 rung completions ascending in cost.
