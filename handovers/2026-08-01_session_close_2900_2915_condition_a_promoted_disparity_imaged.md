# SESSION CLOSE — PATCHES 2900–2915: CONDITION A PROMOTED; THE FORE/AFT DISPARITY IMAGED; CURVATURE PIPELINE LOADED

**Session of 31 Jul – 1 Aug 2026. Worker: Claude (new context window,
inheriting the 2899 inertia-arc handover). This file is the canonical
"what's next" pointer.**

---

## §1 — WHAT'S NEXT (single pointer)

**Execute HYBRID PIPELINE ROUND 2 exactly as frozen at Patch 2914 §4**
(`flagship_papers/electromagnetism/sketches/hybrid_stage1_stage2_record.md`):
fresh seeds {4–9} × classes {A,B} × five β {0.04, 0.07, 0.10, 0.14,
0.20}, instrumented legs via `code/2914_response_field.py` (windows:
round multiples of 2.5/β capped to [60,125]), χ²/dof < 1.5 collapse
gate on the FRESH data only, then Stage 2 via
`code/2914_stage2_integral.py` (β,β³ fit, 200-fold bootstrap), against
the UNCHANGED bands of `hybrid_pipeline_prereg.md` §3 (CANCELLATION
|c_hyb| < 0.05 / RETAINED [0.10, 0.30] / INTERMEDIATE / INCONCLUSIVE;
σ_c ≤ 0.05 required; static-Sea target is c = 1/5 EXACTLY, Patch 2900).
If σ_c > 0.05 again: frozen escalation is seeds {10–15}, then a
conditioning re-assessment. Roughly 60 legs ≈ 45 min compute; batch legs
in a SINGLE python process (numba JIT recompiles per process, ~60 s;
disk cache is disabled — see §5).

## §2 — HEADLINE RESULTS OF THIS SESSION

1. **The B1 curvature coefficient is EXACTLY 1/5** (2900): the 2897
   value 0.20129 was β⁴ contamination; c = 0.200008 invariant across
   all robustness variants; c₄ = 0.02916 also invariant (7/240
   candidate, unclaimed). Analytic derivation still queued.
2. **Entrainment cancels the curvature in the toy** (2900, pre-registered):
   c(ε) crosses zero at ε* = 0.0589 with the drive healthy; one dial
   kills β² only (c₄ flips sign). The ε*·|k| = 1 "identity" was killed
   as a normalization accident by pre-registered cross-variant test
   (2901) — the arc's 8th convenient convergence to die.
3. **Mobile-Sea shell-broadcast engine built from spec** (2902): exact
   pairwise retarded solve, per-CP primitive, state-independent
   emission; PAIR BINDING EMERGES (ZBW 0.4–0.6 oscillation, no bond
   term). Founder rulings captured verbatim (constant-SSV_net direction;
   one-primitive/no-arc-compliance) in `founders_voice/` same-patch.
4. **Three pre-registered inconclusives** (2903/2904/2906), each buying
   a diagnosis: washboard transit-lock; finite-domain asymmetry (proven
   by chatter-free frozen legs: 6e-18 at the symmetric phase, −2.4e-3
   off it); and finally —
5. **The ZBW Sea is deterministically CHAOTIC** (2908): Lyapunov ≈
   0.56/Moment (e-folding 1.8 Moments), measured by twin-run
   divergence; round 3 aborted at its own symmetry gate. Ensembles
   thereby fully legitimised; **power wall named**: direct curvature
   measurement needs 1e7–1e8 Moments — infeasible; sign is feasible.
6. **CONJ-FP-1 CONDITION A: HOLDS — PROMOTED** (2909–2912): sign round
   +1.62e-3 at 5.7σ (17/18 positive, floors clean); 1.3× domain
   variation first refused promotion at 1.95σ vs frozen 2.0 (the line
   is the line), then the pooled 18-value extension cleared at 5.36σ
   (16/18, β=0.2 alone at 12.5σ). Both substrate conditions of the
   volume-transfer mechanism now hold (B closed 2895). Condition table
   appended to the CONJ-FP-1 sketch.
7. **THE FORE/AFT DISPARITY IMAGED DIRECTLY** (2914): the axial
   induced-dipole field around the moving charge is coherently positive
   aft / negative fore — an antisymmetric polarization wave co-moving
   with the source, amplitude ~0.4β inner ring. First substrate-level
   picture of the founder's arc disparity.
8. **Hybrid pipeline validated in the loop** (2913/2914): Stage-2
   integral over the measured pattern reproduces the directly measured
   drive (k_h = +0.0106 vs k_Δ ≈ +0.014, same sign, ~25%). Curvature
   round 1 INCONCLUSIVE (σ_c = 27.7; 3 β points give the cubic 1 dof);
   my collapse R-gate was noise-blind (indicted by χ² = 0.41–1.02,
   retired with disclosure; corrected χ² gate judges fresh data only).

## §3 — FOUNDER INTERACTION STATE

- Two rulings captured verbatim (CONV-009): constant-SSV_net /
  co-moving-arcs direction, and one-primitive/no-arc-compliance/
  emission-state-independence (2900, 2901 patches).
- **Arcs question** ("displacement pattern vs charging state as
  disparity carrier") was DELEGATED; worker ruling recorded at 2913 §0:
  position is the only stored primitive state, so the displacement
  field is the complete carrier; full vector tabulated as insurance.
  **Correctable — capture any founder correction same-patch.**
- PD-006 in force throughout: no sign-offs requested; founder does
  mechanical applies only; every turn carries a Plain Language Summary.

## §4 — LEDGER (unchanged all session)

1B OPEN; PR7 PARTIAL (OPEN-K1-MEMORY-1); six of seven; **B7 holds
DM-1/2/3 release banners**; Candidate (B) 79.5% PROVISIONAL-FAVORABLE.
G1 and P-A2-1 stand. Statics suspension (2892) stands. 7 July
no-carried-velocity ruling stands — and is now VINDICATED in spirit:
the velocity memory demonstrably lives in the Sea's co-moving
polarization pattern (§2.7), not in the CP.

## §5 — ENVIRONMENT / PROCESS NOTES FOR THE NEXT WORKER

- **Tool-call compute cap ≈ 300 s.** Long runs MUST checkpoint
  (drivers 2904/2907/2911 do; exact-state pickle, bit-identical resume).
- **numba disk cache is DISABLED** (cache=True broke across processes:
  ModuleNotFoundError '<dynamic>'). Each process pays ~60 s JIT — so
  batch many legs per python process; never one-leg-per-subprocess.
- **Kernel gate:** any change to the retardation kernel must re-pass
  the 10-Moment dynamic agreement gate (≤1e-10 vs the numpy reference
  in `2902_mobile_sea_engine.py`). The gate has caught one inverted
  bisection branch (2906) that static V1 could not see.
- **Commit hygiene rule (twice burned):** every commit gets
  `git format-patch` + `present_files` + an outputs-directory listing
  IN THE SAME TURN. 2903 and 2905 were committed without presented
  files; both required founder round-trips to repair.
- **/tmp is working state** (results JSON, checkpoints); everything
  verdict-relevant is archived under
  `flagship_papers/electromagnetism/data/` in the patches.
- Analysis refuses incomplete ensembles by construction (KeyError on
  missing legs) — keep it that way; it converted an infrastructure bug
  into a delay instead of a distortion (2912).

## §6 — OPEN ITEMS BEYOND THE POINTER

Analytic derivation of c = 1/5 (and c₄ = 7/240 candidate) from the
round-trip angular moments — queued since 2900, cheap, high value.
LINK 2, LINK 3: open. Statics rebuild: suspended per 2892. KINETIC-1
stiffness: untouched this session. OPEN-K1-MEMORY-1 (PR7 clause 2):
untouched; B7 banners remain the founder's decision gate.
