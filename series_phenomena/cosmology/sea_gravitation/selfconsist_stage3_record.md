# D-SEA-SELFCONSIST STAGE 3 — THE EXPLICIT ARRAY: heating diagnosis, the missing energy regulator, and FQ-5.3

**Patch 3080 (11 Aug 2026). The explicit 3D periodic array (27 DPs /
54 CPs, all-pairs Coulomb with minimum image, RETARDED partner
interaction over true stored trajectories, natural closer-at-perigee
switching, no mean-field closure). Continuous-step branch, pending
FQ-5.1 (the hard-quantum branch is provably frozen, Stage 2 G1).
Verify: `scripts/3080_selfconsist_stage3.py`. No band quantity
anywhere.**

## §1 — Results

| d_s | kick | ⟨δ²⟩ early/mid/late | η_late | f_sw | regen | sup. frac | v² drift |
|---|---|---|---|---|---|---|---|
| 6 | 0.5 | 70.6 / 71.7 / 72.1 | 2.001 | 7.46 | 1326 | 0.016 | ×6.9 |
| 6 | 2.0 | 71.0 / 71.9 / 72.1 | 2.002 | 7.48 | 1323 | 0.015 | ×6.0 |
| 8 | 0.5 | 130.5 / 134.2 / 135.2 | 2.113 | 7.59 | 613 | 0.007 | ×6.4 |
| 8 | 2.0 | 131.8 / 134.5 / 134.7 | 2.105 | 7.86 | 609 | 0.007 | ×4.5 |
| 16 | 0.5 | 557 / 562 / 558 | 2.178 | 6.81 | 75 | 0.001 | ×2.4 |
| 16 | 2.0 | 561 / 559 / 567 | 2.215 | 6.41 | 92 | 0.001 | ×1.9 |

Lossy-arc demonstration (d_s = 8): γ = 0.99 → v² drift 0.98 (flat),
η = 2.68, f_sw = 8.5; γ = 0.90 → v² drift 1.00, near-frozen glassy
state (regen = 3, η = 4.0). Neither γ adopted.

## §2 — Findings

- **H1 (the diagnosis):** with perfect-memory inertia (v += F) and no
  back-reaction, the array HEATS and ionises into a partner-random
  gas at every spacing — η_late ≈ 2.0–2.2 is precisely the
  uniform-gas value (L²/4)/d_s² = 2.25 for the periodic box;
  superposed fraction ~1%; switches ≫ regenerations. Retarded
  attraction + lossless inertia pumps energy: the MODEL violates the
  automaton's own O-3 ledger conservation. **Energy regulation is a
  missing ruled ingredient, not a Sea property.** The Stage-2
  stationarity was implicitly imposed by its fixed-point construction
  and is NOT self-sustained in this model class.
- **H2 (the regulator, exhibited as necessary, not sufficient):** the
  lossy-arc reading of R-INERTIA-ARC (inertia = the retarded
  re-encounter of the CP's own arc field, hence slightly imperfect
  memory) CURES the heating (v² drift flat at both γ values tested)
  but does not, in this unannealed run, restore the faithful-pair
  phase — the array relaxes into scrambled/glassy states. Recovering
  the faithful jittering phase requires the ruled loss PLUS proper
  preparation (Stage 3b: annealed start, longer relaxation, loss from
  the ruling rather than a scan).
- **H3 (status of φ₃):** Stage-2's shape-universal η_z ≈ 0.2 stands
  as the best current estimate, now understood as CONDITIONAL on the
  energy-regulated stationary faithful branch, whose regulator FQ-5.3
  pins and whose existence in the explicit array Stage 3b must
  exhibit.

## §3 — The standing founder question set (FQ-5, complete)

- **FQ-5.1 (the quantum):** sub-GP effective steps, or externally
  seeded jitter?
- **FQ-5.2 (where the Sea sits):** at the stability boundary
  (reading α — spacing derived), or elsewhere by separate ruling?
- **FQ-5.3 (the arc's memory — NEW, from H1/H2):** is DP-arc inertia
  perfect memory, or the retarded return of the CP's own emissions —
  lossy, with the loss set (and possibly DERIVABLE) from arc geometry
  and shell dilution? The founder's phrase "establishing the inertial
  magnetic/KE/momentum FIELD" reads naturally as the latter; his
  ruling governs. This single answer decides how the Sea satisfies
  its own O-3 ledger and unlocks Stage 3b.
