# L3-a executed: the p-wave resonances exist, sit in-window, and fail — measured, not inferred (Patch 2343)

**What this is:** the CONV-001 panel's unanimous priority, run the day the returns were
adjudicated. **Engine:** the validated 2338 Numerov machinery, direct δ₁(E) energy scan
(60 log points, 20–600 eV) at each of 60 (S, R_s) band points — a narrow feature cannot
hide between strength-grid points because the *energy axis* is traced at fixed potential.
**Results:** `code/2343_pwave_pole_search.py`, `code/2343_results.json`.

**Findings.** Six rising π/2 crossings of δ₁(E) exist across the band — the
barrier-protected ℓ = 1 door hypothesized at L3-a and by four panelists is **real**. Two
sit inside the SPEC-1 window: (S = 0.45, R_s = 30): **E_res = 83 eV, Γ = 62 eV**;
(S = 0.50, R_s = 27): **E_res = 108 eV, Γ = 90 eV**. Both **fail the suite**: Γ ≈ E_res
— the ℓ = 1 centrifugal barrier at ~100 eV is too shallow to sharpen the feature, so
σ(50) rides up with σ(30) (totals 48–52 vs the pin's ceiling of 5; r1 ≈ 1.1–1.9 vs the
4.08 bar) and LSB runs over (4.6 vs 2.5). The failure mode is the same breadth that
killed the s-wave threshold structure — now measured at the pole rather than inferred
from scan smoothness. Robustness: the in-window hit is stable across the core variant
(E = 83 → 77 eV, Γ = 62 → 57) and dr-halving (identical) — the width is set by the
exterior (attraction + centrifugal), not the core, which also retires the core
systematic *for this question*.

**Verdicts.** L3-a **RESOLVED-closed**: the quantum flank of the kill is now closed at
the pole level for ℓ = 1 within the registered band; DeepSeek's J4 BREAK is discharged
by execution (the resonances it hypothesized exist and fail for a computed reason);
the panel's SHARPEN is satisfied. Honest scope: ℓ ≥ 2 poles are further
barrier-suppressed in coupling to the transport sum and were smooth in the all-ℓ 2338
scans; a targeted δ₂ trace is a cheap completeness item, queued low. **NO VERDICT
MOVED** — G4 stands; the live repair path for the J3 wound (polydisperse mixture scan,
2344) is now the kill's only open flank.
