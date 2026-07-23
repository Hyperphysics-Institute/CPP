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

---

## LEG 2 — X3: clean replication at both tension points (Patch 2789)

**Executed 2026-07-23 under the frozen 2786 prereg §1 + PA-1.
Machinery: `code/2789_x3_execution.py` — the committed 2761 clean
pipeline verbatim except the licensed RUNS table (X3-R04:
686/0.04/seed 20260803/eq 600/4800 sw; X3-R02: 432/0.02/seed
20260804/eq 400/3200 sw), the CONV-005 v2 gate upgrade the prereg
mandates, and PA-1 per-sample S_zz archival. Analysis:
`code/2789_x3_analysis.py` (frozen 24×2000 block bootstrap wrapping
the committed 2761 Yukawa extraction on the frozen windows).
Reasoning: `reasoning/2789.md`. Data archived: `data/x3x4/`.**

**Gate v2 (BLOCKING, quoted):** X3-R04 — 400 checks, worst
|ΔH_inc − ΔH_full| rel = 8.427e−13, worst antisymmetry = 1.456e−14 →
PASS. X3-R02 — 400 checks, worst 7.403e−13 / 1.776e−14 → PASS.
Production licensed. S-drift ≤ 2.4e−12 at every chunk boundary;
acceptance 0.93 / 0.91; 960 / 640 samples.

**Committed F1 results (frozen extraction + frozen bootstrap; all
five chains under the SAME model for the pooling rule):**

| Chain | κ_fit/κ_D | boot σ | vs DH |
|---|---|---|---|
| X3-R04 (new) | 0.9084 | 0.0187 | −4.90σ |
| X3-R02 (new) | 0.9122 | 0.0223 | −3.93σ |
| RV-MAIN-A | 0.9066 | 0.0184 | −5.08σ |
| RV-MAIN-B | 0.8924 | 0.0176 | −6.10σ |
| RV-CORE | 0.8726 | 0.0218 | −5.84σ |

Frozen class conditions: (a) both new chains < 1: TRUE. (b)
consistency with RV counterparts: 0.40σ and 1.27σ combined — both
consistent. (c) pooled below-DH significance: a_s = 0.04 pool
0.9021 ± 0.0105 (9.30σ); a_s = 0.02 pool 0.8920 ± 0.0156 (6.93σ);
Stouffer combined 11.47σ ≥ 3σ.

**X3 FROZEN VERDICT: REPLICATED.** The below-DH near-window residual
is a reproducible property of the clean pipeline — fresh seeds,
doubled lengths, both a_s points, sub-1.3σ agreement with the
archived chains. No PR1 enactment in any branch (frozen); feeds the
consolidated S4-X report.

**SAME-FONT FLAG F-EM (error-model dependence of significance):**
the pooled 9.3σ/6.9σ/11.5σ figures are computed under the FROZEN
bootstrap model, which yields per-chain σ ≈ 0.018–0.022 — roughly 3×
tighter than the error model behind the committed RV-ledger figure
(F1 2.56σ, which used the SEM-weighted fit covariance ⊕ the ±1.5%
HNC floor, and compared to the HNC reference 1.0206 rather than to
DH = 1). The dramatic significance increase over the ledger is
therefore PRIMARILY an error-model and reference-choice difference,
not new data: what X3 adds evidentially is REPRODUCIBILITY (fresh
seeds land within ≤ 1.3σ of the archive), not a larger anomaly.
Which model and reference feed PR1's ≤ 2σ bar is panel business at
the consolidated report; the ledger's 2.56σ remains the PR1 number
of record until then. Read jointly with requirement-7 (no
conjugate-space counterpart, adopted Q6 wording): a reproducible
residual with no k-space image STRENGTHENS the
extraction/profile-shape-systematic reading — reproducible does not
mean physical. The X4 window map, two-component test, and
moving-feature discriminant are the designed arbiters and run next.

**Next legs:** X4 rung completions ascending in cost (0.02: 686 +
1024; then 0.01; then 0.005), gate-gated, PA-1 archival throughout.
