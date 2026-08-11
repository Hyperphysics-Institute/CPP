# D-SEA-SELFCONSIST STAGE 2 — THE SELF-CONSISTENT DILUTE SEA: three regimes, a shape-universal η_z ≈ 0.2, the fidelity boundary at d_s* ≈ 6–7 GP, and a derived constraint on the step quantum

**Patch 3079 (11 Aug 2026). The stand-in dials of Stage 1 are retired:
the environment is now derived from the array's own dipole fields
(⟨E²⟩ = 2p²/r⁶ with p = q·δ carrying the SAME ⟨δ²⟩ being solved for;
C₆ = 14.4539 computed exactly for the FCC reference; one-component
projection /3; anti-mirrored member frame), correlation time from the
measured regeneration time and traversal time, re-capture at the
poaching radius d_s/2 with velocity kept and history cleared
(R-SWAP-EQUIV). Fixed point iterated per spacing, damped, seeded,
robustness-checked. Verify: `scripts/3079_selfconsist_stage2.py`.
No band quantity anywhere.**

## §1 — Results

| d_s (GP) | state (sub-quantum dynamics) | η_z = ⟨δ²⟩/d_s² | f_switch | T_reg (Moments) |
|---|---|---|---|---|
| 4 | RUNAWAY (plasma collapse, f_sw → 1) | — | 1.000 | — |
| 6 | MARGINAL (transitional) | 6.45 (non-converged) | 0.816 | 1.5 |
| 7 | jittering | 0.239 | 0.144 | 3.4 |
| 8 | jittering | 0.226 | 0.134 | 3.7 |
| 16 | jittering | 0.190 | 0.100 | 4.5 |
| 32 | jittering | 0.207 | 0.099 | 6.7 |
| 64 | jittering | 0.254 | 0.070 | 11.9 |
| any (hard 1-GP quantum) | **FROZEN** | — | — | — |

Seed robustness (d_s = 8): η_z = 0.227 vs 0.226; f_sw = 0.143 vs 0.134.

## §2 — Findings

- **G1 (three regimes):** plasma runaway below d_s ≈ 5–6 (self-
  amplifying jitter — the founder's plasma collapse exhibited as a
  real instability); a stable jittering branch above ≈ 7; and, under
  a hard 1-GP step quantum, a FROZEN Sea at every scanned spacing —
  the self-consistent fields are sub-quantum, so with a hard 1-GP
  minimum the vacuum cannot sustain its own ZBW. **The founder's
  FQ-4.3 caveat is now a derived requirement:** either the effective
  minimum increment is far below 1 GP, or the vacuum jitter is
  externally seeded (matter/photon fields). Founder ruling invited.
- **G2 (shape universality):** on the jittering branch η_z ≈
  0.19–0.25 across a factor 8 in spacing. **φ₃ is robust to the d_s
  determination** — the cycle-average shape is a property of the
  dynamics, not of the density.
- **G3 (fidelity exhibited):** the switch fraction is small and falls
  with dilution (0.14 → 0.07): the founder's 3072 statement
  ("swapping frequency small compared to monogamous fidelity") is now
  a computed fact.
- **G4 (the boundary):** d_s* ≈ 6–7 GP at Stage-2 resolution. If the
  founder rules reading (α) — the Sea sits at its own stability
  boundary — then the spacing is DERIVED, zero parameters, and φ₁'s
  census follows.

## §3 — Caveats (Stage-2 resolution; Stage 3 retires them)

1D radial reduction; anti-mirrored environment approximation; poach
reset keeps velocity and clears retarded history; C₆ from the FCC
reference for what is physically a disordered sea; T = 6000 per
iteration, damped fixed point. The Stage-3 explicit array (many DPs,
real geometry, no mean-field closure) is the cross-check.

## §4 — Standing founder decision points

- **FQ-5.1 (the quantum):** sub-GP effective steps (continuum below
  1 GP) or externally seeded jitter — which is the vision?
- **FQ-5.2 (where the Sea sits):** at the stability boundary d_s*
  (reading α — derived spacing), or elsewhere on the jittering branch
  (reading β — spacing separately ruled)? η_z barely cares; the
  ρ_Λ ∝ 1/d² anchoring cares greatly.
