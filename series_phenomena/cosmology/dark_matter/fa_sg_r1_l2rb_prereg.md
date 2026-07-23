# FA-SG-R1 L2-RB PREREGISTRATION (FROZEN) — two-test re-execution arc

**Patch 2784. Frozen 2026-07-23, BEFORE execution.** Authority: CONV-001
FA-SG-R1 returns adjudication §2b (Patch 2766) — L2 operationalization
OVERTURNED 4–1, L2-RB chartered as a queued two-test re-execution arc on
S1's frame, folding all seats' specifications. Queued behind FA-C2 (2766
§7); FA-C2 closed at C2R-OBSTRUCTED (Patch 2775, ratified 4–0 at 2778) —
the queue condition is satisfied. Design reconnaissance recorded in the
2783 handover §2; **this prereg was frozen FRESH per the 2783 §4
discipline note** — every reconnaissance assumption was re-checked
computationally before commitment (checks in `code/2784_l2rb_recon_checks.py`,
reasoning in `reasoning/2784.md`). Two reconnaissance assumptions were
found FALSE and are corrected below (§0).

**Standing fences (all frozen, none waivable at execution):**

- **NO class consequence can attach.** R1-SHIFT fires independently via
  J3-REVISE (chartered 5–0 at 2766); every seat concurred L2-RB cannot
  change it. The executed L2R FAIL stays in the ledger regardless of
  outcome (2766 §2b disposition (i)).
- **2694 lessons are frozen constraints:** no 3D→4D numeric onset
  transfer; the 2687 run-clause binary classifier is motif-sensitive and
  BANNED. Committed site-level measures only: neg-frac and nn sign-flip.
- **No direct ℓ fit.** No genuine asymptotic window exists on I1's
  shells (frozen at 2766 §2b).
- **Same-font reporting** of every committed outcome, pass or fail.
- Frozen physics constants and solver: exactly those of
  `code/2694_r1_l2r_execution.py` — L_UNIT = 0.589 fm, a = L_UNIT/φ,
  α = a/(π√2), kernel 1/D, response system (I + αG)f = 1/r₀ with the
  source site excluded from the response set.

---

## §0 — Reconnaissance-check results (what changed between the 2783 sketch and this freeze)

**Check 1 — chord/geodesic shell partitions on I1: NOT identical.**
The 2783 reconnaissance guessed "likely yes" (both metrics monotone in
the 4D angle). FALSE: chord induces 8 shells from v₀ with multiplicities
{12, 20, 12, 30, 12, 20, 12, 1}; graph-geodesic distance is quantized to
edge count and induces only 5 shells {12, 32, 42, 32, 1} — geodesic
shell g merges chord shells per the single-valued coarsening map
**{c1}→g1, {c2,c3}→g2, {c4,c5}→g3, {c6,c7}→g4, {c8}→g5** (verified
exhaustively; chord→geodesic is single-valued, the inverse is not).
RB-2 construction (a) survives but must be defined at the geodesic
(coarser) partition level via this explicit map — see §2.

**Check 2 — torus construction sanity: constructible, with a mandatory
audit gate.** FCC periodic supercells (conventional-cell tiling, 4abc
sites, exact 27-image minimum-image distances) pass all-sites-z = 12 at
every ladder size tested, including (5,3,2) = 120 and (3,3,3) = 108.
BUT two naive close-packed constructions FAIL coordination: 2-layer HCP
stacks (c-period too short — z = 9, self-image contamination) and
dhcp(5,2)×12 (in-plane period too thin — z = 11). Consequence: §1
imposes a **construction audit gate** (frozen, mechanical, runs before
any solve) and the realization set below uses only gate-passing
constructions verified at freeze time.

**Check 3 — RB-2 candidate selection.** Candidate (a) cross-metric is
adopted (§2) with the coarsening map explicit. Candidate (b)
held-out-shell is rejected: the held-out sites' own response is real
physics and no scoring convention avoids silently penalizing it without
introducing an untested estimator. Candidate (c) spectral is rejected:
RB-2 is single-object (I1 only), so a dimensionless spectral observable
has no committed comparison target — it is a measurement, not a test.

**DISCLOSURE — partial unblinding from the reconnaissance smoke test.**
Verifying the minimum-image kernel required one solver run; it exposed
one result-adjacent number: FCC(5,3,2), source site 0, neg-frac = 0.429.
Remedy (frozen here): FCC(5,3,2) is declared the **disclosed pilot**.
The ALL-realizations prediction in §1 still binds it, but the blind
content of L2-RB-1 is: the other five realizations on both metrics, the
pilot's nn-flip metric, and the full onset ladder. No other committed
quantity was observed before this freeze.

---

## §1 — L2-RB-1: structural-class test (class-only prediction)

**Frame (2766 §2b, S1 + S3/S5):** compact arenas matched to I1 by site
count AND coordination depth; multiple independent realizations; an
N_crit staggering-onset scan; class-only prediction.

**Matching argument (frozen):** I1 (600-cell, 120 vertices) is
boundaryless with every site z = 12. Compact 3D balls cannot match this
(boundary sites z < 12 — the 2694/2766 diameter-vs-count obstruction is
the dimension obstruction). The honest matched family is **periodic 3D
close-packed tori** under the exact minimum-image metric: every site
z = 12, matching count AND coordination depth simultaneously.

**Kernel convention (frozen):** D(i,j) = exact minimum over the 27
neighbor images of the torus lattice vectors; kernel 1/D; no image
summation. Non-orthogonal (hexagonal) lattice vectors handled exactly.

**Construction audit gate (frozen, mechanical, pre-solve):** a
realization enters the committed set only if (i) all sites have exactly
z = 12 at the minimum-image nn distance, and (ii) the shortest torus
lattice vector has length ≥ 3 × nn distance. The gate tests geometry
only and runs before any response solve; a gate failure is a
construction defect, not a physics outcome, and is reported as such.

**Committed realization set (six, all gate-verified at freeze time):**

| # | Realization | Sites | Note |
|---|-------------|-------|------|
| 1 | FCC (5,3,2) | 120 | disclosed pilot (see §0 disclosure) |
| 2 | FCC (3,3,3) | 108 | |
| 3 | HCP (5,6)×4 layers (AB) | 120 | |
| 4 | HCP (3,6)×6 layers (AB) | 108 | |
| 5 | dhcp (5,3)×8 layers (ABAC) | 120 | |
| 6 | dhcp (3,3)×12 layers (ABAC) | 108 | |

Ideal close-packing geometry throughout: in-plane nn = a, interlayer
spacing √(2/3)·a, a = L_UNIT/φ.

**Source-site commitments (frozen):** FCC tori are site-transitive —
source = site 0 WLOG. HCP is expected single-orbit under the torus
automorphisms (screw-axis layer exchange) — source = site 0 (layer A,
cell origin); one alternate-layer source is run as a robustness axis,
not a committed datapoint. dhcp has two site orbits (cubic-environment
A-layers vs hexagonal-environment B/C-layers) — **committed source
orbit: the cubic-environment (A-layer) origin site**, per the 2783
reconnaissance rule (commit the source orbit, report the other as a
perturbation axis).

**Committed metrics (frozen, site-level only):**
- **neg-frac**: fraction of response sites with f < 0.
- **nn-flip**: fraction of minimum-image nn edges (both endpoints ≠
  source) whose endpoint responses differ in sign.

**COMMITTED CLASS-ONLY PREDICTION P-RB1 (frozen):** site-level
staggering PRESENT — **neg-frac ≥ 0.10 AND nn-flip ≥ 0.10** — in ALL
six committed realizations at their committed sources, AND in I1 on
both committed metrics. The I1 side is already of record (neg-frac
0.723 chord / 0.597 geodesic, Patch 2694); the live risk is the torus
side. PASS = all six realizations meet both thresholds. FAIL = any
committed realization misses either threshold. Same-font either way.

**Onset scan (CHARACTERIZATION-ONLY, frozen):** FCC-torus ladder,
4abc ∈ {32 (2,2,2), 48 (3,2,2), 72 (3,3,2), 96 (4,3,2), 108 (3,3,3),
120 (5,3,2), 128 (4,4,2), 144 (3,3,4), 192 (4,4,3), 256 (4,4,4)},
source = site 0, both committed metrics reported per rung. NO
prediction attaches; NO class consequence; NO 3D→4D numeric transfer of
any threshold (frozen 2694 lesson). Purpose: measure the coupling
threshold clean of boundary dilution, as characterization for
KINETIC-1/K1-S1 consumers.

---

## §2 — L2-RB-2: I1-native quantitative test (cross-metric prediction)

**Frame (2766 §2b, S1 + S2/S3):** prediction built on the actual I1
distance matrix and topology; tolerances from preregistered
perturbations ON I1; 4D-consistent construction; no direct ℓ fit.

**Construction (frozen — candidate (a) with the §0 coarsening map):**

1. **Predictor side (chord):** solve the frozen response system on I1
   with the chord metric D4 (source v₀ WLOG by vertex transitivity;
   119 response sites). Aggregate: for each geodesic shell g ∈
   {g1..g5}, f̄_g^pred = mean of f over the member vertices of g (per
   the frozen coarsening map — equivalently, the multiplicity-weighted
   mean of the merged chord shells' amplitudes).
2. **Target side (geodesic):** solve the SAME frozen system on I1 with
   the graph-geodesic metric Dg (edge = minimal chord, path lengths ×
   a; exactly the 2694 construction). For each geodesic shell g,
   f̄_g^obs = mean of f over member vertices.
3. **Committed observables:** the geodesic-shell **sign sequence**
   s_g = sign(f̄_g), g = 1..5, and the four **amplitude ratios**
   ρ_k = |f̄_{k+1}| / |f̄_k|, k = 1..4.

This is a genuine cross-operator prediction: the two metrics define
different response operators; the claim under test is that the
staggered evanescent structure is metric-robust in the quantified sense
below. Nothing is fit; both solves are parameter-free under the frozen
constants.

**Tolerance construction (frozen, predictor-side only, mechanical):**
the envelope for each committed observable is the [min, max] over the
perturbation set computed on the CHORD (predictor) side:

- **α-envelope:** α × {0.969, 1.000, 1.031} (the frozen ±3.1%
  W-envelope).
- **Deletion resampling:** delete each single non-source vertex in turn
  (119 runs, 118-site solves); shells remain defined by the undeleted
  geometry from v₀; deleted vertex excluded from its shell mean.

The joint envelope per observable = [min, max] over all 3 × 119 + 1
predictor-side runs. This is a robustness envelope, not a confidence
interval (rider v2.6 relabeling, adopted 5–0).

**COMMITTED PREDICTION P-RB2 (frozen):**
- **(i) Sign sequence:** s_g^obs = s_g^pred for ALL five geodesic
  shells, where s_g^pred must be unanimous across the predictor-side
  perturbation set (if any perturbation run flips a predicted shell
  sign, that shell is reported INDETERMINATE-PREDICTOR and excluded
  from (i), with the exclusion stated same-font).
- **(ii) Amplitude ratios:** ρ_k^obs inside the joint predictor-side
  envelope for **at least 3 of the 4** ratios.

PASS = (i) AND (ii). FAIL = either miss. Same-font either way. No
class consequence attaches in any branch (§ fences).

---

## §3 — Execution and reporting contract

- ONE execution patch: `code/<patch>_l2rb_execution.py` (stdlib +
  numpy/scipy, CONV-003 provenance stated: all numbers from the frozen
  constants above, source patch 2694 lineage) + record file
  `fa_sg_r1_l2rb_record.md` + verbatim `reasoning/<patch>.md`, bundled
  in the same `git am` per the reasoning-capture rider.
- The record reports: gate audit per realization, both metrics per
  committed datapoint, the onset ladder table, both RB-2 observable
  sets with envelopes, P-RB1 and P-RB2 verdicts same-font, and the
  standing note that the original L2R FAIL remains in the ledger.
- Dispatch to the panel afterward follows CONV-001 single-block format;
  distinguishing numbers withheld from any challenge packet per the
  2778 author-side rule.
- No new registry IDs are created by this arc (CLONE-FIRST gate run at
  freeze: no collisions; `L2-RB` lives under the existing FA-SG-R1
  arc).

**Freeze declaration:** every prediction, threshold, realization,
source commitment, coarsening map, tolerance construction, and pass
criterion above was fixed before any committed quantity was computed,
with the single §0-disclosed exception (the pilot's neg-frac). Nothing
in this file may be revised at execution time; a discovered defect
voids the leg and requires a fresh prereg patch, stated same-font.
