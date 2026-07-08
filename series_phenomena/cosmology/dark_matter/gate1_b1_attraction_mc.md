# The attraction MC: the closure confirmed by measurement — and the killed candidate is not what we said it was (Patch 2336, 7 July 2026)

**What this patch is:** the founder-directed belt-and-suspenders measurement behind the
2335 in-prior closure. **Measurement:** `code/2336_attraction_mc.py` (results in
`code/2336_results.json`); **grading:** `code/2336_attraction_mc_grading.py` (6/6).
**NO VERDICT MOVED.** One superseded sentence in the KILL-branch record, corrected here.

## 1. What was run

The 1871 pinned-geometry elastic MC (N = 18, d = 1.15 fm, repulsive coat, all protocol
inherited), plus the **registered** attractive screened E_qq residual in exactly the
1858 capture-pipeline form — V(r) = −(0.3 MeV·fm/r)·e^(−r/R_s), R_s = 1/χ = 25.42 fm —
applied CM-central, no cutoff, with sampling geometry extended per velocity to cover the
focusing radius. Integrator: the first run failed honestly (400% energy drift on
attraction-fed plunges — local speeds reach ~30× asymptotic and the fixed dt·v grid
under-resolves the coat wall; caught by the inherited drift monitor). Final integrator:
KDK/float64 with wall-speed-bucketed substeps at the 1871-validated resolution
h·v = 0.03 fm. Drift ≤ 8.7×10⁻² worst-trajectory at 30 km/s, ≤ 3×10⁻⁵ at ≥1150;
dt-halving robustness seed at the pin consistent (5.77±1.36 vs 6.02±0.56).

## 2. The measured curve

σ_T/m (coat + attraction, one measurement): **9.31±1.21 (30 km/s) | 6.02±0.56 (50) |
0.679±0.108 (200) | 0.029±0.010 (1150) | 0.019±0.006 (1500) cm²/g** — monotone falling,
×486 dynamic range. The never-evaluated channel produces a real, strong velocity
dependence.

**The 2335 bars, measured:** r1 = σ(30)/σ(50) = 1.55 against ≥4 (×2.6 short);
r2 = σ(50)/σ(200) = 8.86 against ≤7.14 (×1.24 over). Measured low-velocity slope
s(30–50) = 0.85 — *below* even the s = 2 envelope: the screening cut predicted in-prior
is real and stronger than the envelope. **The 2335 closure is confirmed by measurement.**

**Windows:** dSph 9.3 vs [20,100] — **FAIL ×2.1** (8.8σ below the edge; decisive);
pin 6.02 vs [1,5] — over the top ×1.20; LSB 0.68 vs [0.7,2.5] — grazes the low edge,
PASS-marginal; group 0.029 — inside the F1 prediction band (F1 character unchanged);
cluster 0.019 vs ≤0.13 — PASS ×6.8. Suite verdict: **FAILS**, on dSph decisively and on
the pin/LSB simultaneity (the r2 excess).

## 3. The texture correction (the measurement's honest yield)

The 2324 KILL-branch sentence "the candidate reverts to a flat quasi-collisionless relic
at the 0.046 floor" is **superseded**: the no-capture candidate, with the elastic
focusing of its own registered residual finally computed, is a **velocity-dependent
elastic SIDM object** — cluster-safe ×6.8, LSB-grazing, pin-over ×1.2, and **×2.1 short
at the classical dSphs**. The gap between the killed candidate and the full suite is a
factor of ~2 at the dwarf end, not ×100–1000. G4 = KILL-on-suite **stands** — this
measurement is the confirmation of its elastic flank — but what the killed candidate
*is* has changed materially, and the 20-July input should carry the corrected texture.

## 4. Caveats, named

(i) **Classical-protocol flag now load-bearing:** λ_dB = 336–560 fm ≫ rod and R_s at
30–50 km/s — inherited from 1870/1871, but at a ×2 margin a quantum s-wave treatment
could move a near-miss in either direction. (ii) The 1500 km/s value sits ×2 below
1871's repulsive-only number (drift 3×10⁻⁵ here vs 2×10⁻³ there) — an
integrator-fidelity note against the *old floor's absolute numbers*; no verdict touched.
(iii) CM-central attraction = the registered 1858 rod-level reduction. (iv) **S_ATT(N)
is unregistered** — 0.3 MeV·fm is the N = 18 point; at a ×2 dwarf gap, the N-scaling of
the residual (and with it any N-population story) becomes a well-posed, founder-gated
follow-up. Not pursued here; named only.

## 5. Ledger

2335 closure CONFIRMED-by-measurement (upgraded from in-prior). 2324 KILL-branch texture
corrected (flat-relic sentence superseded; suite-failure factors at the dwarf end revise
from ×130–1100 to ×2.1 under the full registered elastic force). NO VERDICT MOVED. The
CONV-001 package now carries three flanks: the kill (2333, self-red-teamed 2334), the
elastic closure (2335, measured 2336), and the corrected identity of what survives.
Founder-gated items on the table: panel timing; the S_ATT(N) follow-up; the quantum
s-wave treatment of the near-miss.
