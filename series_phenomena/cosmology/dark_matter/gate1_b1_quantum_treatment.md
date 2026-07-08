# The quantum door: real, opened, walked through, and empty (Patch 2338, 8 July 2026)

**What this patch is:** founder-gated follow-up 2 — the partial-wave quantum treatment
of the screened-residual elastic channel, the single door the 2337 family closure left
open. **Engine:** `code/2338_quantum_engine.py` (Numerov, vectorized over ℓ; validated
exact on hard-sphere ℓ=0/ℓ=1 and to 0.1% on weak-coupling Born — validators that caught
a real matching bug before any physics ran). **Grading:**
`code/2338_quantum_grading.py` (6/6). **NO VERDICT MOVED.**

## 1. Why this computation was necessary

λ_dB = 336–560 fm ≫ R_s at dwarf velocities: the entire classical chain (1870/71,
2336/37) is outside its formal validity exactly where the suite is decided. And the
well is genuinely quantum-interesting: dimensionless strength 2μSR_s/(ħc)² ≈ 5 supports
a near-threshold s-wave bound state, so the low-velocity cross-section is
threshold-dominated — capable of structure the classical F(ε) cannot represent.

**The door was real.** Sweeping S across the OPEN-SS-43 band drags the bound state
through threshold: σ(30 km/s) swings ×443 — down through a Ramsauer-like minimum
(S ≈ 0.39, zero scattering length) and up through a threshold resonance
(S ≈ 0.51–0.57) that *reaches dSph magnitude*. Running 2338 was necessary, not
decorative.

## 2. The answer

**Zero passing configurations in 520 quantum evaluations.**

- **Registered point (S = 0.30, R_s = 25.42), four core variants:** every variant
  fails the suite — but *which* anchor fails swings with the core. The physically
  motivated soft-coat variant (yuk, using the registered N·E_ee coat strength) and hs2
  fail **only dSph** (×5.5–5.9 short; pin, LSB, cluster all PASS); hs10 *passes dSph*
  but fails the pin ×4.9 and grazes the cluster bound. Core sensitivity at 30 km/s:
  ×15. The rod coat has no registered central quantum reduction — this is the named,
  bounded systematic.
- **Band scan** (S ∈ [0.15, 0.60] × R_s ∈ [15, 30] × 4 cores, 448 points): zero pass;
  best violation ×1.74. The resonance delivers dSph magnitude but is too energy-broad
  to separate 63 eV (30 km/s) from 176 eV (50 km/s): σ(50) rides up with σ(30), and
  LSB simultaneously runs over near resonance.
- **Fine-grid refinement** (ΔS = 0.01 around the resonance, 68 points): zero pass;
  **max achievable r1 = σ(30)/σ(50) = 3.40 anywhere, against the bar of 4.** No narrow
  feature hides between scan points — s-wave threshold features are generically broad
  (no centrifugal barrier), and the refinement measures that at the most promising
  corner.

**Grade: CLOSED-scanned** — a dense-scan exclusion with the core systematic bounded by
variants that all fail; not a theorem, and not claimed as one. The honest residual: a
registered rod-level quantum reduction would sharpen *which* anchor fails, but the
variant envelope contains no passing configuration.

## 3. What the quantum picture adds to the founder's texture

Quantum-mechanically, the killed candidate at its most defensible reduction (yuk core,
registered point) **passes the dwarf pin, the LSB window, the group prediction, and the
entire cluster ladder — and fails only the classical dSph cores, by ×5.5**. The
classical picture (2337) had it failing the dwarf pair ×1.6–1.8 in opposite directions.
Either way the suite fails and the verdict stands; but the object being reported to the
20-July decision is a one-anchor-short SIDM candidate under every treatment tried, with
the shortfall localized to the heterogeneous dSph window in the quantum picture.

## 4. Ledger

Follow-up 2 RESOLVED (quantum door closed-scanned). Both founder-gated follow-ups are
now complete. G4 = KILL-on-suite-conditional stands, closed on every flank: derivation
(2333), self-red-team (2334), elastic in-prior closure (2335), classical measurement +
correction chain (2336–37), classical family closure (2337), quantum band scan (2338).
Named residuals carried forward: rod-level quantum reduction (core systematic, bounded);
identical-boson symmetrization convention (O(1), consistent with the classical chain,
flagged). **The CONV-001 package is fully ready** — panel pointers, in order: axis
exhaustiveness (2334), A3′ memorylessness reading (2334), the family-closure
log-concavity structure (2337), and this patch's core-systematic envelope.
