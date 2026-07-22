# S4-X B-CHECK-80B RECORD (DRIVE-AUDIT-1, fourth act, part 2) — executed under the frozen 2755 amended charter: **J1 — THE DEFECT IS THE MECHANISM; candidate (a) CONFIRMED with a named cause (the 2714 self-pair)** — with the one-line fix applied, the driven/tilt enhancement ratio at N = 80 is **r_fix = 0.997 ± 0.160** (unity to 0.02σ, against r_legacy = 1.622 ± 0.237), and the two independently written samplers agree at 0.75σ — the X3-LONG B2 anomaly, the pooled plateau r = 1.461 ± 0.082 (5.6σ), and the X7-NSCAN onset finding in (64, 80] are hereby classified ARTIFACTS of the 2714 self-pair defect; linear response HOLDS in the clean system; frozen remedy: repo-wide reach audit + re-verification charter

**Patch 2756, 22 July 2026. Seeds consumed: 20260795 (B-DRV),
20260796 (A-FIX-UND), 20260797 (A-FIX-DRV) — pool now spent through
…797. Gate v2 PASS (≤10⁻¹⁵) preceded all production. Data archived at
`data/bcheck80b/`. Reasoning: `reasoning/2756.md`. Verdict emitted by
the frozen analyzer in `code/2755_s4x_bcheck80b.py` (no post-hoc
statistic was added). 79.5% not in scope.**

## §1 — What ran (exactly as chartered; no deviations)

Three ensembles at N = 80, protocol constants identical to the frozen
campaign stack (A = 0.589/φ, Θ ≈ 35.149 MeV, a_s = 0.04, ε = 2.4,
full-PREF k-space, KD = (2π/L, 0, 0), step 0.20·A, sample/10 sweeps,
10-block SEM):

| ensemble | sampler | seed | sweeps (eq + prod) | samples |
|---|---|---|---|---|
| A-FIX-UND | 2714-lineage A path, `mn[i]=False` fix | 20260796 | 1000 + 16000 | 1600 |
| A-FIX-DRV | same | 20260797 | 1000 + 16000 | 1600 |
| B-DRV | independent brute-force B (2755 file) | 20260795 | 1000 + 12000 | 1200 |

Gate v2 (blocking, five seed-1 trial moves, threshold 10⁻⁸): PASS with
relative discrepancies ~10⁻¹⁵ on all five — the fixed A increment and
B's from-scratch totals compute the same Hamiltonian.

Execution note (disclosed, no charter bearing): B-DRV ran in
checkpointed foreground chunks (`/tmp/bcheck80b/B-DRV.pkl`, RNG state
carried, E_cur recomputed on resume); an earlier background attempt
died with its shell and contributed nothing.

## §2 — Frozen readout

```
AFIX-UND: <A> = -0.026 ± 0.186   Var = 22.23   linear pred = -1.518
tilt_fix  =  -1.549 ± 0.235   (exp(-βεA) reweighting, jackknife)
AFIX-DRV: <A> = -1.544 ± 0.079
B-DRV:    <A> = -1.424 ± 0.137   Var = 20.65
r_fix     =   0.997 ± 0.160
|r_fix - 1| = 0.02 σ
AFIX-DRV vs B-DRV = 0.75 σ      B-DRV vs tilt_fix = 0.46 σ
```

Frozen fork evaluation: dr = 0.02 ≤ 2 AND dFB = 0.75 ≤ 2 → **J1**.
Neither J2 nor J3 nor J4 was reachable on these numbers by any margin.

Three independent consistencies, all clean-side:
1. **Driven = tilt** (r_fix = 0.997): the driven ensemble reproduces
   the reweighting prediction — the discriminant that legacy chains
   failed at 5.6σ (pooled) is passed at 0.02σ.
2. **Driven = linear response**: A-FIX-DRV −1.544 vs −βε·Var_UND =
   −1.518 (0.3σ) — linear response HOLDS at N = 80, ε = 2.4.
3. **Sampler-independent**: B (totals rebuilt per move, no increment
   machinery at all) lands on the same physics (0.75σ, 0.46σ).

## §3 — How the defect manufactured r_legacy = 1.622

The contamination was NOT one-sided. Clean vs legacy at N = 80:

- tilt side: −1.549 ± 0.235 (clean) vs −1.185 ± 0.144 (legacy) — the
  defect SUPPRESSED the undriven susceptibility (the g-penalty
  stiffens the chain: smaller accepted displacements, under-sampled
  fluctuations, Var and the reweighted tilt both biased low).
- driven side: −1.544 ± 0.079 (clean) vs −1.922 ± 0.157 (legacy) —
  the defect INFLATED the apparent driven response.

A denominator biased low and a numerator biased high jointly produced
a ratio near 1.6 from a true ratio of 1.0. This also retro-explains
the X5-FE N = 64 puzzle (A and B agreeing at the observable level in
one comparison while the ensembles differed elsewhere): the bite of a
detailed-balance violation is observable- and state-point-dependent —
which is exactly why B-CHECK-80B was chartered on the discriminant
quantity rather than on any single expectation value.

## §4 — Classifications (this record's authority: the DRIVE-AUDIT-1 scope only)

**ARTIFACT (caused by the 2714 self-pair; reclassified herewith):**
- X3-LONG B2 anomaly (2737/2740 chains, N = 432/686).
- Pooled plateau r = 1.461 ± 0.082 (5.6σ) — VOID as evidence.
- X7-NSCAN onset finding, window (64, 80] (2749, all twelve series).
- Every r-type enhancement claim from 2714-lineage A-path chains.

**STANDS (clean or non-descendant):**
- 2709 S4-N results (code verified CLEAN in the 2754 gate record).
- The B-CHECK methodology itself, now validated end-to-end.
- Clean-side physics established here: linear response holds; no
  driven-equilibrium enhancement at N = 80, ε = 2.4.

**DEFERRED to the reach audit (frozen remedy; not judged here):**
- Standing-ledger items (septuply-consistent spectrum, X6 shape
  finding, FA-C3 closure, LANE B, RELIC-1, qCP fence): exposure is a
  code-genealogy question — which committed artifacts descend from
  2714's increment path — and is the reach audit's first deliverable.
- X5-FE comparisons (2743/2746): doubly clouded (this defect on the
  A side; the stale half-PREF k-term in the committed 2746 B file).

## §5 — Corrections ledger (accumulating; dispatch per economy rule)

1. **2714 self-pair defect** (entered S4-E Ewald rewrite; inherited
   2737, 2740, 2743, 2746 run_A, 2749): mechanism confirmed J1;
   artifacts reclassified per §4.
2. **Stale 2746 B file**: committed code encodes net 0.5·PREF k-term
   (`*2.0/2.0` identity edit) despite the 2747 record's documented
   fix — the record and the repo disagree; supersede the file.
3. **F3 prose impeached** ("no line-level defect"): the gate found
   one in an afternoon; F3's NUMBERS stand, its assurance does not.

## §6 — Consequences and the frozen remedy

The J1 remedy is fixed by the 2755 charter and is not re-decidable:

1. **REACH-AUDIT-2714** — enumerate every committed artifact whose
   numbers descend from the 2714 increment path; classify each
   CLEAN / CONTAMINATED / INDETERMINATE; deliverable is an exposure
   table over the full standing ledger.
2. **Re-verification charter** — for every CONTAMINATED item still
   load-bearing, a frozen re-run with the fixed code (and gate v2 as
   a standing precondition for ALL future Metropolis acts).

AUTOMATON-1 remains elevated but is NOT triggered (J2 was the
automaton branch; J1 closes the anomaly at the code level, and
inventing work for the arbiter would itself be a process violation).
X4 ladder, OPEN-DM-CHARGE-1, and the FA-C2 tier re-run stay queued
behind the audit. Panel dispatch continues to hold: one bundle —
full S4-X arc + DRIVE-AUDIT-1 + corrections ledger + audit outcome —
after REACH-AUDIT-2714 resolves.

## §7 — Discipline note

Everything that decided this outcome was frozen before any production
sweep: the fork thresholds, the analyzer, the seeds, the fix (one
line, `mn[i]=False`), and the blocking gate. The verdict line printed
by the pre-committed script is the verdict of record. No quantity in
§2 was computed by any code written after the data existed.
