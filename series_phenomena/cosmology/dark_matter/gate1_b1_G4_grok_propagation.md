# G4 · Grok propagation — the DM-1 anchor suite under the three G4 outcomes (Patch 2324, 7 July 2026)

**Campaign:** Gate-1/B1, post-close item 1 per the 2323 handover ("Grok Propagation" keyword; the last
input the 20-July decision wants). Grok's decisive check (W1, merged into OPEN-DM-CAPTURE-1 at 2311):
re-anchor with capture efficiency P(v) < 1 and propagate. Executed under the 2322 polaron frame —
the one residue is the sub-cone weight w ≡ S(k ~ 1/R_s, ω_enc)/S_max, thresholds per 2321 (unchanged).
**Verify:** `code/2324_g4_grok_propagation.py` (7/7). **No resting paper touched. No verdict moved:
G4 stays UNRESOLVED-QUANTIFIED.** Branch-independent by construction.

## 1. The propagation model (derived, not chosen)

From the registered C-g accounting-B geometry: loss(b) = f_geo(b)·w·E_coat with f_geo ∝ b (path
(2b)(c/v), mfp fixed at k = 1/R_s), against a b-independent bar E_col = ½μv². Capture therefore
fills an **annulus** b ∈ [b_max·(Θ_crit/w), b_max], giving

  **P(v, w) = max(0, 1 − (Θ_crit(v)/w)²)**  (flat-w slice; Θ_crit per 2321).

Because η = χ is zero-parameter, P **multiplies** the published capture term with no refit freedom:
total(v, w) = floor (0.046, measured) + P(v, w)·capture_pub(v). Encounter-frequency ladder:
ħω_enc = 45 eV (dwarf, b = 145 fm) / 417 eV (pin) / 4.25 keV (LSB) — two decades across the suite.

## 2. The three branches against the published anchors

| Anchor (window) | published | KILL (w below all Θ_crit) | PARTIAL, flat w ∈ [~2×10⁻³, 0.66) | SURVIVE (w ≥ 0.66 at 4.2 keV) |
|---|---|---|---|---|
| dSph 10–40 km/s [20,100] | ~15.5 (graze-under) | 0.046 — **FAIL ×435–2170** | ~published (P≈1) | published |
| dwarf pin 50 [1,5] | 4.4–4.9 PASS | 0.046 — **FAIL ×22** | 4.4–4.9 for w ≳ 7×10⁻³ | published |
| LSB 200 [0.7,2.5] | 0.74–0.85 PASS | 0.046 — **FAIL ×15** | 0.046 — **FAIL ×15** | published (P ≥ 0.87) |
| group 1150 (F1) | 0.037–0.05 | unchanged | unchanged | unchanged |
| cluster/Bullet bounds | 0.03–0.05 / ~0.02 | PASS (floor) | PASS | PASS |

- **KILL → the elastic floor/plateau is the entire prediction.** Discriminant I dies at all three
  two-sided anchors; the candidate reverts to a flat quasi-collisionless relic (cluster-safe,
  coreless). The floor itself, being elastic, is G4-independent and survives.
- **PARTIAL (flat spectrum) → EXCLUDED BY EXISTING DATA, not merely disfavored.** The turn-on ladder
  spans five decades (dwarf 6×10⁻⁶ → pin 2–7×10⁻³ → LSB 0.66); any flat w that rescues the dwarfs
  but not the LSB collapses the LSB total to the floor, ×15 below its window's low edge. **There is
  no stable dwarf-weighted resting point on a flat spectrum** — Grok's recalibration regime exists
  only on steeply rising spectra, where it is continuous with SURVIVE.
- **SURVIVE → the LSB anchor is the true bar**, and it is near the physical ceiling: P ≥ 0.87
  requires **w(4.2 keV) ≥ 0.66 AND E_coat ≥ 0.40 MeV** (upper half of the 0.144–0.6 band; at the
  hard end w_req = 2.7 > 1, infeasible). The papers' unit-efficiency assumption is genuinely
  load-bearing exactly here.

## 3. The spectral ask, graded (what Stage-3 must actually deliver)

In bare-Ohmic-tail units: dwarf survival asks ×27–115 (2321's number); **full-suite survival asks
×3×10⁴ at the LSB frequency — ~×10³ harder**. Equivalently: a super-Ohmic rise s ≳ 2.6 between
417 eV and 4.2 keV (bare Ohmic s = 1 falls short ×40 even seeded at the pin threshold), or
near-ceiling plateau weight (ωτ_eff ≳ 1) by ~keV, i.e. configurational components with correlation
times ≳ 10⁵ τ_b. **The Stage-3/DM-4 computation must be evaluated at 4.2 keV, not only at the dwarf
45 eV — and against a ceiling-level bar.**

## 4. What this does to the 20-July decision input (no recommendation)

The open condition sharpens from a graded residue to a **nearly binary** one: either the sub-cone
spectrum reaches near-ceiling weight at keV frequencies (suite survives as published), or the
velocity mechanism fails at all two-sided anchors together (the LSB is not separable from the
dwarfs on any flat spectrum). Two branch-robust facts ride along: the **F1 group falsifier
(0.037–0.05 vs Sagunski 0.5±0.2) is invariant across all three outcomes** (floor-dominated 87%+),
so its adjudicating power is G4-independent; and the elastic floor + cluster/Bullet safety survive
every branch.

**Caveats (named):** flat-w slice evaluated at the b_max frequency (annulus area-weighted toward
b_max; intra-annulus ω-variation higher-order); the P-multiplication maps the gate's coat-cycling
accounting onto the paper's screened-residual capture term one-to-one (same capture event, two
ledgers); dwarf f_geo saturation (×1.9) makes the dwarf column conservative; LSB requirement uses
the published band center (edges move P_min over 0.81–0.94 without changing any conclusion).
