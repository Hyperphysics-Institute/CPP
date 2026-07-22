# C2R-L2 RECORD — the near-core χ(r) correction is NON-PERTURBATIVE at the operating point: the founder-specified distributed-response profile, computed through the frozen operator on A0/A1, moves the readout by **δℓ/ℓ_LO = +220% ± 78%** (D3 ≫ W = 3.1%), DESTROYS the staggered mode (nn-flip 0.44 → 0.07), and degrades the envelope fit (R² 0.57–0.70) — the committed 50% honesty bound FIRES: the first-order number is NOT quotable as ℓ_derived, and the shape's self-consistent closure is inseparable from the underived short-distance per-site response (the KINETIC-1-adjacent remainder L1 named) — adverse-direction, reported in full

**Patch 2773, 22 July 2026. Prereg: `c2r_l2_prereg.md` (2772, frozen
before execution; route followed with no amendment). Verify:
`code/2773_c2r_l2_profile.py` (deterministic, no seeds; every number
below is script output). Reasoning: `reasoning/2773.md`. Fences
F1–F3 in force; 79.5% not in scope. The campaign class fires only
at L4.**

## §1 — Execution (route steps 1–4, as committed)

Corrected operator (I + αG̃), G̃_ij = (1−e^(−κr_ij))/r_ij,
G̃_ii = κ (the responding r < a self-medium; ακ = 0.4502, effective
stiffness 1.4502). Arenas A0 (FCC ball) and A1 (HCP ball), R = 7
and 9, sanity-gated (all PASS: min chord = a, interior z = 12).
Baseline re-solved in the same run; paired extraction on the three
frozen windows.

| Arena | staggering base → L2 (nn-flip / neg-frac) | ℓ_base band (fm) | ℓ_L2 band (fm) | δℓ/ℓ |
|---|---|---|---|---|
| A0 | 0.442/0.535 → **0.067/0.922** | 0.0885–0.0928 (R² 0.88–0.95) | 0.192–0.343 (R² 0.59–0.70) | +211% ± 67% |
| A1 | 0.421/0.480 → **0.077/0.902** | 0.0880–0.0914 (R² 0.95–0.97) | 0.196–0.371 (R² 0.57–0.61) | +230% ± 86% |

R=7 ≡ R=9 to four decimals in both operators (boundary-blindness
holds — the corrected decay is still short against the arena). All
twelve paired variants: **δℓ/ℓ_LO = +220.5% ± 77.8%;
D3 = 220% ≫ W = 3.1%.** The CONFIRM path is dead (condition 2
decisively unmet); whether CORRECTED or OBSTRUCTED fires is L4's
call under §3 below.

## §2 — Deliverable (i): the profile, and what the correction does structurally

χ(r) = Σ_j q_j ρ̂(|r−r_j|) evaluated on the nn axis (A0, R=9,
table in script output). **Structural finding, same-font:** in the
CORRECTED solution the staggering collapses (neg-frac 0.92 — the
field sits in single-sign lobes), so no opposite-sign adjacent pair
exists near the probe and the near-probe superposition is
same-sign-reinforcing. The founder's oppositely-signed adjacent
curves are realized in the BASELINE staggered mode (where adjacent
q_j alternate); the corrected operator exits the staggered regime —
consistent with the 2688 three-regime map (effective coupling
α/(1+ακ) = 0.690α crosses the staggering threshold) and with the
analytic cross-check: the homogenized corrected closure has complex
poles k² = κ²(−1 ± i√3)/2, i.e. decay length 0.2102 fm with a long
oscillation wavelength 2.287 fm. The lattice ℓ_L2 values (0.19–0.37
fm, strongly window-dependent, degraded R²) bracket the analytic
decay and show exactly the symptom a slow oscillation superposed on
decay produces in a log-linear fit. The computation is faithfully
reporting the corrected operator's physics; this is not an
instrument defect.

## §3 — The committed honesty bound FIRES (binding for L4)

The prereg committed: the cloud shape is the LEADING-ORDER
self-consistent profile, and if |δℓ/ℓ_LO| > 50% the shape-iteration
question is NAMED rather than absorbed. At +220% the correction is
O(1): distributing the leading-order cloud and re-solving
re-screens already-screened response, and no small parameter exists
at κ·a = 2 (ακ = 0.45). Consequences, stated for L4's mechanical
class evaluation:

1. **The first-order ℓ_L2 is NOT a derived screening length.** It
   is the first term of an expansion the result itself shows
   non-convergent at the operating point. Quoting
   ℓ_LO × (1 + 2.20) = 0.29 fm as ℓ_derived would ship exactly the
   "approximately closes with an unstated gap" failure the frozen
   classes exist to prevent.
2. **The named obstruction.** Closing χ(r) requires the true
   short-distance response profile of a Sea site — the self-
   consistent fixed point of the response shape, which is governed
   by the same per-site stiffness structure behind κ·a = 2 that the
   L1 record's honesty bound already flagged as underived and
   KINETIC-1-adjacent. The concrete question (for registration at
   L4 if OBSTRUCTED fires): *what is the actual profile over which
   a Sea site's every-Moment response is distributed — equivalently,
   the short-distance closure of χ_static — given that neither the
   point idealization (baseline) nor the leading-order cloud
   (this leg) is self-consistent at κ·a = 2?*
3. **What survives regardless:** the leading-order point-response
   readout ℓ_LO = 0.0904 ± 0.0028 fm stands as the committed
   envelope of the frozen operator (L1: its α is the unique
   occupied-core closure); the profile correction is demonstrated
   LARGE and structure-changing, which is a real, adverse-direction
   finding about the proxy branch's normalization sensitivity — in
   the same direction as, and now mechanistically deeper than, the
   L4/2688 J3-REVISE finding.

## §4 — Deliverables ledger

(i) χ(r) nn-axis profile — script output table (structural caveat
§2). (ii) δℓ/ℓ_LO = +220% ± 78%, sign positive, error = 1σ across
12 paired variants; NOT quotable as a derived correction (§3.1).
(iii) A0/A1 numerical evaluation both executed; analytic
continuum cross-check consonant (OBS-class). No stochastic
elements; no seeds; route followed without amendment.
