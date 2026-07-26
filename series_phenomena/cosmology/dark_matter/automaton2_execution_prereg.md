# AUTOMATON-2 EXECUTION PREREGISTRATION (FROZEN) — Patch 2801

**Frozen 2026-07-25, BEFORE any Moment is simulated, under the
ratified founder specification (C19–C30, this patch). Worker-stratum
choices are marked [W]; physics is the founder's throughout.**

## §1 — Realization

- **Lattice [W]:** even-parity sublattice of a 24³ cubic torus =
  FCC, 6912 GPs, native 12-neighbor icosahedral adjacency
  ({(±1,±1,0)} permutation family), matching C22's lattice-edge
  relay and the 600-cell's icosahedral vertex figure.
- **Sea [W]:** N = 864 CPs (432 +, 432 −), fill fraction 1/8 — the
  founder's dilute bonded regime; the Sea IS the melee (C23: no
  background medium).
- **Field rule:** one Moment = R directed hop sub-steps (C22,
  c = PSR/Moment; uniform-Sea PSR_eff = R per the A1 DR-2 analog,
  robustness axis R ∈ {2, 3, 4}, three full runs). Implementation
  [W]: by translation invariance the origin-directed R-hop relay
  equals convolution with the directed-front kernel W_R (computed
  once by iterating the directed relay from a point; verified at
  Patch 2800 to place 100% of mass at graph-distance R); field
  recursion Q_t = W_R ∗ (Q_{t−1} + inj_t) with unit-charge injection
  per CP per Moment; SSV_net/SSV_abs from the signed/gross vector
  kernels built on W_R with û taken from the aggregation origin
  (identical structure to the A1 engine that produced emergent
  Coulomb, with the C22-native kernel substituted). Self-parcel
  exclusion structural (front excludes distance 0).
- **CP rule:** C19/C20 verbatim — displacement d = (|SSV_net|/
  SSV_abs)·R along σ_c·SSV_net, nearest-GP snap, co-location
  permitted, zero-net stasis. NOTHING ELSE — no noise term, no
  gradient branch, no exchange rule: aliveness must be EMERGENT
  (C24/C25) or the run fails honestly.
- **Moments [W]:** warm 2×10⁴, production 8×10⁴, sample every 20
  (4000 samples); seeds 2801 + R; checkpointed chunks; per-sample
  archives (PA-1 discipline).

## §2 — Blocking gates, in order (PASS lines quoted; any FAIL → STOP + re-prereg)

- **G1 = P-A2-1 (Coulomb survives the directed relay):** the 2798
  V-1R comparative gate verbatim — jellium monopole, M = 48, the
  verified Ewald reference, window r ∈ [2R+2, 16] — under the W_R
  multi-hop field rule. Bands unchanged: normalized ρ(r) ∈
  [0.90, 1.10] pointwise AND |p_auto − p_Ewald| ≤ 0.15, at ≥ 2 of 3
  R.
- **G2 (conservation/boundedness):** A1 V-2 verbatim on the A2
  melee (10⁴ Moments): exact net-charge conservation; bounded L1.
- **G3 = D-A2-1 (aliveness + chaining, the C30 thermodynamic
  gate):** over the final quarter of a 2×10⁴-Moment melee run [W]:
  mean per-Moment mover fraction ≥ 0.20; clusters = connected
  components at inter-CP distance ≤ 1.5 [W]; ≥ 60% of CPs in
  clusters of size ≤ 2 AND max cluster size ≤ 8 [W]. FAIL here is
  the A1 quench recurring — reported as such, no Gibbs comparison
  runs.

## §3 — Committed measurements (production; 24×2000 block bootstrap on verdict quantities)

- **P-A2-2 (emergent inertia, ballistic test) [W bands]:** after
  equilibration, ONE tagged CP receives a transient bias (ε = 0.05
  added to its own SSV_net only, along +x, for 50 Moments), then
  release. Statistic: post-release net drift along +x over the next
  200 Moments vs the same CP's pre-kick RMS 200-Moment drift.
  Classes: **BALLISTIC** ≥ 3× (near-force-free persistence, C23
  confirmed); **OVERDAMPED** < 1.5× (scalar-drag picture);
  **FROZEN** (no motion; A1 behavior); INTERMEDIATE otherwise.
  Repeated over 24 tag events per R (bootstrap over events); the
  decay of the drift-velocity autocorrelation supplies **D-A2-3**
  (friction coefficient; committed expectation: small at low v —
  large low-v friction falsifies C29).
- **P-A2-3 (detailed balance → Gibbs):** the 2796 §4 deliverable
  battery re-instantiated verbatim on the A2 melee — two-thermometer
  θ_H/θ_κ ∈ [0.9, 1.1]; κ agreement (2σ AND ≤ 10%); energy-split
  L2 ≤ 3× pooled; current asymmetry ≤ 2σ; susceptibility isotropy
  ≤ 2σ with **the torus-safe Resta-phase polarization estimator
  [W]** replacing the defective A1 signed-COM (registered lesson,
  named substitution BEFORE any run); verdict classes
  GIBBS-CONSISTENT / NOT-GIBBS (≥ 2 of 3 R) / MIXED, verbatim.
- **D-A2-2:** velocity-autocorrelation spectrum of per-Moment
  displacements, all CPs — ZBW peak location vs local SSV_abs
  (report-only). **D-A2-4:** time-averaged free-CP fraction (no
  partner within 1.5) — the C27 rate parameter (report-only).
  **D-A2-5 [W]:** CHARACTERIZATION-ONLY density scan, fill ∈
  {1/16, 1/8, 1/4, 1/2} at R = 3, 10⁴ Moments each: pair fraction
  and mean cluster size vs density (the bonded ↔ plasma indicator;
  no prediction attaches).

## §4 — Verdict wiring and freeze declaration

PR4-A2 verdict = the P-A2-3 battery classes, evaluable only if G1–G3
pass; P-A2-2's class is reported alongside as the inertia
discriminator; adverse outcomes report in full (charter); no
promotion from inside; the 79.5% untouchable; the win packet
(emergent Coulomb + A1 quench + A2 results + S4-X chain) assembles
for the panel only after execution completes, per economy
governance. Every size, band, seed, estimator, and class above was
fixed before any A2 Moment ran; machine-checked at freeze: W_R
front kernels exist and are mass-complete at R ∈ {2, 3, 4}; no seed
or registry collisions (CLONE-FIRST grep clean). A discovered defect
voids the affected leg and requires a fresh prereg patch, same-font.
