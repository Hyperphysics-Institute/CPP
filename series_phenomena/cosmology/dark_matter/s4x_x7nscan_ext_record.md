# S4-X X7-NSCAN-EXT RECORD (DRIVE-AUDIT-1, third act) — executed under the frozen 2750 prereg: **FORK H4 (OTHER)** — the point-wise sequence inverts (80 ENHANCED 1.62 ± 0.24, 96 UNENHANCED 1.17 ± 0.17, 112 ENHANCED 1.45 ± 0.22) so no bracket exists at band resolution — but the POOLED post-hoc description is dispositive at the aggregate level: **every size N ≥ 80 combined gives r = 1.461 ± 0.082 (5.6σ above unity, χ²/dof = 6.01/5 for a constant plateau), and a step-at-64 is the best split** — the onset is compressed into **(64, 80]**, the anomaly's confinement tightened from (64, 432] to a factor-1.25 window in two acts; B-CHECK at N = 80 (measured cost ≈ 0.9 h) is the queued discriminant; AUTOMATON-1 remains arbiter-of-record per the frozen clause

**Patch 2751, 21 July 2026. Runs archived (`data/x7nscan/`, six EXT
series alongside the six X7 series). All ensembles at full frozen
length from frozen seeds 20260789–794. Reasoning: `reasoning/2751.md`.
79.5% not in scope.**

## §1 — The EXT points (frozen readout)

| N | ⟨A⟩_UND | Var(A) | tilt_A | ⟨A⟩_DRV | r = DRV/tilt | class (frozen bands) |
|---|---------|--------|--------|---------|--------------|----------------------|
| 80 | +0.105 ± 0.111 | 18.63 | −1.185 ± 0.144 | −1.922 ± 0.157 | **1.622 ± 0.237** | ENHANCED |
| 96 | −0.230 ± 0.145 | 20.15 | −1.611 ± 0.170 | −1.887 ± 0.193 | **1.171 ± 0.172** | UNENHANCED |
| 112 | −0.007 ± 0.214 | 21.84 | −1.504 ± 0.216 | −2.184 ± 0.098 | **1.453 ± 0.219** | ENHANCED |

Sequence across {64, 80, 96, 112, 128}: UNENH → ENH → UNENH → ENH →
ENH. The 80→96 inversion (1.54σ) voids H1's no-inversion condition →
**H4 as frozen: automaton arbiter; no shape reading enacted.**

## §2 — Post-hoc diagnostics (labeled as such; not part of the frozen readout)

1. **Autocorrelation audit.** Integrated autocorrelation time of every
   chain (all 14: X7 + EXT + the X5-FE anchors) is 1.4–1.8 samples at
   the 10-sweep spacing (ESS 890–1155 everywhere). The 10-block SEMs
   are honest; the point-wise oscillation is genuine statistical
   scatter, NOT hidden slow modes inflating the error bars.
2. **Pooled description.** Weighted mean over all six measured sizes
   N ∈ {80, 96, 112, 128, 216, 320}: **r = 1.461 ± 0.082**,
   χ²/dof = 6.01/5 — a single constant plateau fits. Against unity:
   **5.60σ**. Against the N = 64 baseline (1.13 ± 0.12): 2.28σ.
3. **Step-location scan** (step model r = r_lo for N ≤ N★, r_hi
   above): χ² = 6.01 / 8.91 / 5.71 / 6.56 for N★ = 64 / 80 / 96 /
   112 — the split at 64 is equal-best; the data prefer the entire
   enhancement to switch on immediately above 64. The 432 anchor
   (1.70) sits ~1.2σ above the plateau — consistent with scatter or a
   mild continued rise; not resolvable here.
4. Combined statement (post-hoc, recorded not enacted): the driven
   mean exceeds the exact Gibbs tilt response at every size N ≥ 80,
   at a pooled plateau ≈ 1.46, with the transition confined to
   **(64, 80]** — a window of width 16 particles, factor 1.25 in N.

## §3 — What this leaves standing and what it queues

- Candidates (a) numerical pathology / (b) finite-size-onset
  ergodicity failure / (c) unnamed: **still unranked** — but the
  compression of the onset into (64, 80] makes the B-CHECK at N = 80
  maximally cheap and maximally sharp: if the from-scratch sampler
  reproduces r ≈ 1.6 at 80, reading (a) dies at the onset itself and
  (b) becomes the finding (reportable sampler physics). Measured cost
  (20-move benchmark, seed 1, discarded, disclosed): ≈ 0.25 s/sweep
  with carried current-energy (the 2746 B design), ≈ 0.9 h for
  1k + 12k sweeps — one dedicated execution block for the successor.
- AUTOMATON-1 stays arbiter-of-record per the frozen H4 clause and
  the standing elevation; its execution prereg remains charterable in
  parallel on the founder-confirmed specification.
- The N = 64 exoneration (X5-FE F3), the large-N non-Boltzmann proof
  (un-tilt), and the entire standing physics ledger are untouched:
  septuply-consistent spectrum, X6 shape finding, monotonic
  character, all caps and fences, **79.5% untouched**. The anomaly
  remains confined to the driven-MEAN instrument at N ≥ ~(64, 80]
  onset — which no standing claim consumes.

## §4 — Ledger

Discipline: the H-fork executed exactly as frozen (H4, automaton
clause); the pooled plateau and step-scan are disclosed post-hoc
descriptions feeding the next prereg, not reclassifications; the
B-sampler cost benchmark used seed 1 and read no observable; frozen
seeds 20260789–794 consumed as assigned; seed 20260795 (H3 replicate)
unconsumed and returns to the pool. Chain accounting verified as in
2750 (samples = (sweeps − eq)/10 exactly, all six).
