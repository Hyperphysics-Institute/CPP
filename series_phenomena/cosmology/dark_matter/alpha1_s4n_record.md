# ALPHA-1 S4-N RECORD — the founder-ordered numerical hardening step: **S4-N PASS (P1 ∧ P2 ∧ P3, as frozen at 2708)** — the directly simulated two-species Sea at the closed parameters (θ = 35.15 MeV, q = e, Γ = 0.2251) screens MONOTONICALLY with **κ_fit = 1.017 × κ_D on the main run** (5.589 vs 5.494 /fm); no charge layering in any run; the S4-analytic verdict is numerically confirmed and the robustness axis behaves physically

**Patch 2709, 21 July 2026. Executed under the frozen 2708
preregistration; nothing renamed after results. Verify:
`code/2709_alpha1_s4n_simulation.py` (seeded, deterministic; full
output quoted in §3). 79.5% not in scope. Reasoning:
`reasoning/2709.md`.**

## §1 — Result against the frozen conditions

| Run | N | a_s (fm) | character | κ_fit (/fm) | κ_fit/κ_D |
|---|---|---|---|---|---|
| MAIN | 686 | 0.04 | MONOTONIC (0 significant alternations) | 5.589 | **1.017** |
| ROB-a | 432 | 0.02 | MONOTONIC (0) | 5.040 | 0.917 |
| ROB-b | 432 | 0.08 | MONOTONIC (0) | 4.392 | 0.799 |

**P1 PASS** (no significant sign alternation anywhere in the frozen
window, any run). **P2 PASS** (main-run κ_fit within 1.7% of κ_D —
far inside the ±25% gate). **P3 PASS** (character identical across the
a_s axis and both sizes; κ_fit inside the robustness window, with the
soft-core trend physically sensible: a larger a_s weakens short-range
response and mildly lengthens the fitted decay). **S4-N PASS.**

## §2 — What is now established, and its conditionality ledger

The continuous two-species Sea, at the parameters closed entirely from
registered objects (0764 Coulomb kernel with q = e → θ = 35.15 MeV;
geometry → Γ = 1/(√2π)), screens a charge disturbance **smoothly and
exponentially at ℓ = 1/κ_D = 0.1820 fm = d_DP/2**, with no oscillatory
layering — confirmed both analytically (S4, DH-controlled with the
Γ^{3/2} = 11% bound) and now by direct simulation (S4-N, three runs,
two sizes, three regularizations). Conditionality carried honestly:
(i) q = e inherits 0764's panel-pending status; (ii) minimum-image
truncated Coulomb is a disclosed approximation (κL = 10.7–12.5 makes
it controlled; the Ewald upgrade is offered to the seats); (iii)
FG-OTHER reclassification remains PROVISIONAL — panel property, moved
in the consolidated packet (2710), enacted only at their returns.

## §3 — Verify output (verbatim)

frozen params: theta=35.1495 MeV, q^2=1.43996 MeV·fm, n_CP=58.636/fm³,
kappa_D=5.4942/fm, Gamma=0.2251. MAIN N=686 a_s=0.04 L=2.270 fm
acc=0.92 samples=400: P1 window (0.080,0.546) fm alternations=0 →
MONOTONIC; kappa_fit=5.589 (ratio 1.017); profile ρ_z(r):
+0.20656±0.00958 (0.105 fm), +0.08103±0.00529 (0.185), +0.03223±0.00319
(0.285), +0.00710±0.00242 (0.405), +0.00184±0.00174 (0.555),
+0.00277±0.00142 (0.695). ROB-a N=432 a_s=0.02: alternations=0,
kappa_fit=5.040 (0.917). ROB-b N=432 a_s=0.08: alternations=0,
kappa_fit=4.392 (0.799). P1=PASS P2=PASS P3=PASS → **S4-N PASS**.
