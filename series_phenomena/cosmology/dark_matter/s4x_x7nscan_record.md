# S4-X X7-NSCAN RECORD (DRIVE-AUDIT-1, second act) — executed under the frozen 2749 prereg: **FORK G4 (PARTIAL; extend)** — the enhancement is ALREADY PRESENT at N = 128 (r = 1.72 ± 0.26) and the curve is consistent with a PLATEAU ≈ 1.4–1.7 from 128 through the 432 anchor — **the onset lies in (64, 128]**, below every scanned size; no scanned size resembles the N = 64 baseline; the frozen fork's extension clause fires and X7-NSCAN-EXT is chartered into (64, 128) in the same patch

**Patch 2750, 21 July 2026. Runs archived (`data/x7nscan/`). All six
ensembles completed at full frozen length (1k eq + 16k sampling, 1600
samples each, frozen seeds 20260783–788). Reasoning:
`reasoning/2750.md`. 79.5% not in scope.**

## §1 — The curve

| N | ⟨A⟩_UND | Var(A) | linear | tilt_A | ⟨A⟩_DRV | r = DRV/tilt | class (frozen bands) |
|---|---------|--------|--------|--------|---------|--------------|----------------------|
| 64 (anchor, X5-FE) | — | 16.7 | −1.14 | −1.247 ± 0.092 | −1.412 ± 0.124 | **1.13 ± 0.12** | baseline |
| 128 | +0.217 ± 0.166 | 22.99 | −1.569 | −1.359 ± 0.172 | −2.338 ± 0.200 | **1.720 ± 0.263** | ENHANCED |
| 216 | −0.082 ± 0.200 | 29.29 | −2.000 | −2.140 ± 0.228 | −2.939 ± 0.198 | **1.373 ± 0.173** | INTERMEDIATE |
| 320 | +0.157 ± 0.219 | 36.41 | −2.486 | −2.362 ± 0.227 | −4.001 ± 0.242 | **1.694 ± 0.192** | ENHANCED |
| 432 (anchor, X3-LONG) | — | — | — | — | — | **1.70** | enhanced |

Classification per the frozen bands: {128 ENHANCED, 216 INTERMEDIATE,
320 ENHANCED} → no UNENHANCED size, non-monotonic point estimates →
**G4: PARTIAL; extend with intermediate sizes before any reading.**

## §2 — What the curve establishes (and what it does not)

1. **The onset is in (64, 128].** Every scanned size sits at or near
   the enhanced level; none is consistent with the N = 64 baseline
   posture. The 64 → 128 jump is 2.04σ — suggestive of a sharp rise,
   not yet dispositive.
2. **The curve above 128 is consistent with a plateau.** The 216 "dip"
   (1.373 ± 0.173) is 1.10σ below 128 and 1.24σ below 320 — not a
   significant structure; 216 itself is 2.16σ above unity. Reading the
   five points together: rise somewhere in (64, 128], then ≈ 1.6–1.7
   flat through 432.
3. **No shape reading is enacted.** A jump-then-plateau would be
   (b)-like (finite-size-onset ergodicity failure); but G4's extension
   clause governs — the discrimination now lives in (64, 128), which
   the original scan did not sample. Candidates (a)/(b)/(c) remain
   unranked.
4. The N = 64 exoneration (X5-FE F3) and the large-N non-Boltzmann
   proof (un-tilt on X3-LONG) both stand exactly as recorded; this
   scan tightens the confinement of the anomaly's onset by a factor
   ≈ 3.4 in N (from "(64, 432]" to "(64, 128]").

## §3 — X7-NSCAN-EXT PREREGISTRATION (frozen HERE, before any EXT run)

**Purpose:** localize the onset inside (64, 128) and read its shape at
the resolution where it actually lives.

**Design (frozen):**
- Sizes: N ∈ {80, 96, 112} (even 50/50 splits), same protocol as X7
  in every respect (same density law, a_s, ε, mode, k-set, α, r_c,
  step, 1k + 16k sweeps, sample every 10).
- Code: `code/2749_s4x_x7nscan.py` extended by these sizes only (seed
  table addition; no physics-line change — diff-verifiable).
- Seeds (frozen): 80-DRV 20260789, 80-UND 20260790, 96-DRV 20260791,
  96-UND 20260792, 112-DRV 20260793, 112-UND 20260794.
- Readout and classification bands: identical to the 2749 prereg.

**Frozen fork (using anchors r(64) = 1.13 ± 0.12 and
r(128) = 1.72 ± 0.26):**
- **H1 — ONSET BRACKETED:** an UNENHANCED size with an ENHANCED size
  above it and no inversion across {64, 80, 96, 112, 128} → onset
  localized to the bracketing interval; sharp-threshold ((b)-like)
  shape reading recorded (not enacted); **B-CHECK charters at the
  smallest ENHANCED N** (cost scales as N² for the brute-force
  sampler — cheapest at the onset).
- **H2 — ALL ENHANCED:** onset in (64, 80]; B-CHECK at 80.
- **H3 — ALL UNENHANCED:** contradicts the 128 anchor's posture →
  the transition is compressed into (112, 128] (very sharp) OR the
  128 point is a fluctuation; one A-path replicate at 128 (fresh
  seed 20260795 pair) becomes the instrument before any reading.
- **H4 — OTHER** (INTERMEDIATE mixtures, inversions) → the rise is
  gradual across the window ((a)-compatible smooth-drift reading
  recorded, not enacted); AUTOMATON-1 remains arbiter-of-record.

**Power:** at these sizes σ_r ≈ 0.15–0.25 per point (X7-observed
scaling); the 64-vs-128 anchor gap is ≈ 2σ — individual-point
classification will be honest about INTERMEDIATE outcomes; the
five-point pattern (two anchors + three new) is the instrument, not
any single point.

## §4 — Ledger

Execution discipline: all six X7 ensembles ran at full frozen length
from the frozen seeds; checkpointed chunked execution (container
constraint) with per-chunk state carry — chain accounting verified
(sample counts exactly (sweeps − eq)/10 at every checkpoint). One
operational anomaly disclosed: a background driver process from the
session's first execution attempt persisted and advanced two
checkpoints between foreground calls; because the chain state (RNG
included) lives wholly in the checkpoint, the chains are identical
regardless of executing process — verified by the exact sample-count
accounting; the phantom was killed before the final N320 chunks.
Standing physics untouched: the septuply-consistent spectrum, X6
shape finding, monotonic character, all caps and fences, **79.5%
untouched**. The anomaly remains confined to the driven-MEAN
instrument, now at N ≥ ~(64, 128] onset — which no standing claim
consumes.
