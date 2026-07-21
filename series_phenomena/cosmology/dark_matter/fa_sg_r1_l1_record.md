# FA-SG-R1 LEG L1 RECORD — tessellated multi-motif arena battery: L1 CONCORD — the sign-staggered response and exponential envelope are stable across four independently constructed z=12 arenas, joint band ℓ = 0.0904 ± 0.0028 fm; J2 rider answered: the emergent scale does NOT generically track d_DP — the identity ℓ = d_DP/4 is specific to the committed κ·a = 2 operating point

**Patch 2685, 21 July 2026. Executing the FROZEN FA-SG-R1 charter (2679)
§2 R1-L1 under the frozen [ADJ] operationalizations and the F1–F4 fence.
No input re-tuned; all choice axes were enumerated before results existed
(realization set, windows, observable, sizes — stated in the verify
script header). Verify: `code/2685_r1_l1_arenas.py`. 79.5% not in scope.**

## §1 — Realizations and instrument sanity (all checked BEFORE the operator landed)

Four z=12-equivalent constructions; the FCC ball is the 2671-D2 proxy
(counts as one already-run realization per the frozen [ADJ]); A1–A3 are
genuinely new (two new motifs + one orientation/boundary treatment,
satisfying "at least two genuinely new constructions"):

| Arena | Construction | N (R=9) | min chord | interior z |
|---|---|---|---|---|
| A0 | FCC ball (cubic construction, ball boundary) | 4321 | 1.000 a | 12 (all) |
| A1 | HCP ball (ABAB Barlow stacking) | 4331 | 1.000 a | 12 (all) |
| A2 | Random-stacking Barlow ball (seed 20260721, no adjacent repeats) | 4316 | 1.000 a | 12 (all) |
| A3 | FCC, seeded random orientation (seed 20260722), cubic boundary | 4329 | 1.000 a | 12 (all) |

Every arena PASSED the sanity gate (site count reported; coordination 12;
min chord = the construction's edge length) before any solve.

## §2 — Per-realization report (staggering; envelope form; ℓ with instrument band)

Frozen windows [0.45,1.3], [0.55,1.6], [0.7,1.8] fm; bin-mean |f| observable;
R = 7 and 9. Staggering statistic: nearest-neighbour sign-flip fraction and
negative-site fraction over r ∈ [0.4, 2.0] fm.

| Arena | staggering (nn-flip / neg-frac) | envelope | ℓ (fm) |
|---|---|---|---|
| A0 | 0.442 / 0.535 | exponential (log-lin R² 0.88–0.95) | 0.0909 ± 0.0018 |
| A1 | 0.421 / 0.480 | exponential (R² 0.95–0.97) | 0.0892 ± 0.0016 |
| A2 | 0.449 / 0.490 | exponential (R² 0.92–0.97) | 0.0924 ± 0.0009 |
| A3 | 0.442 / 0.535 | exponential (R² 0.88–0.95) | 0.0909 ± 0.0018 |

R=7 vs R=9 identical to four decimals in every arena — this is the
screening itself (the boundary sits ≥ 15 screening lengths from the fit
window; the field there is e^{-15}-suppressed), and it is why A3's
boundary change is invisible: boundary-insensitivity is a RESULT here,
not a defect. A3's numerical identity with A0 (rotation preserves the
distance matrix; boundary is screened out) makes it a weak-independence
realization; the load-bearing new constructions are A1 and A2, whose
stacking motifs genuinely differ from FCC beyond the second neighbour
shell.

## §3 — Concordance (frozen criteria, charter §4)

Every pairwise |Δℓ| ≤ 2× combined 1σ (worst pair A1–A2: 0.0032 vs
tolerance 0.0036). Every realization staggered; every realization
cleanly exponential over ≥3 windows. **L1 CONCORD.** Joint band
(union-weighted: union of per-realization 1σ bands, centre = midpoint,
construction stated in the script): **ℓ = 0.0904 ± 0.0028 fm**.
Comparators: 2671 band 0.091 ± 0.002; d_DP/4 = 0.0910 fm (OBS-class,
non-adjudicative per the non-elevation clause — carried, not elevated).

## §4 — J2 rider (labeled robustness scan; severed from the N2 coincidence)

The d_DP = ℓ_edge level assignment (INF-S1C-1) re-examined by decoupling
d_DP from the lattice edge a (axis frozen pre-run: d_DP/a ∈ {1/φ, 1, φ};
FCC R=7; α = κ²/(4πn), κ = 2/d_DP, n = √2/a³ local per fence F1):

| d_DP/a | κ·a | ℓ_env (fm) | ℓ/d_DP | 1/(2κ) (fm) | staggered? |
|---|---|---|---|---|---|
| 0.618 | 3.24 | 0.828 | 3.68 | 0.056 | yes (0.41) |
| 1.000 | 2.00 | 0.0914 | 0.251 | 0.0910 | yes (0.54) |
| 1.618 | 1.24 | 0.249 | 0.423 | 0.147 | NO (0.00) |

**J2 report:** the emergent scale does NOT generically track d_DP. The
clean identity ℓ = d_DP/4 = 1/(2κ) holds AT the committed assignment
(κ·a = 2) and fails on both sides of it; below the operating point the
staggering itself disappears. The level assignment is therefore
structurally special — a fact the packet carries to the panel without
elevation in either direction (it neither proves nor disproves
INF-S1C-1; it shows the d_DP/4 pattern is a non-generic signature of the
committed operating point). The full regime structure behind this is
mapped at L4 (`fa_sg_r1_l4_record.md` §3).

**Fence audit:** no cosmic count consumed; "holographic" unused; 0736
number unused; CC arc untouched. Next leg per frozen sequencing: L3.
Reasoning: `reasoning/2685.md`.
