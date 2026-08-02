# THE REGISTERED PREDICTION c₄ → 0 UNDER FULL SELF-CONSISTENCY IS REFUTED FOR THE DISPLACEMENT-FIELD FIXED-POINT CLOSURE — SELF-CONSISTENCY MAKES THE β⁴ PATHOLOGY WORSE

**Patch 2928 (1 Aug 2026). Confronts the Patch 2900 registered
prediction at its anticipated test. The 2900 reasoning fragment wrote:
"the steady-state argument … predicts c₄ → 0 under full
self-consistency. That prediction is registered before the fixed-point
code exists, so it can fail in public." The fixed-point code now
exists. The prediction failed in public. Model, variants, and verdict
bands PRE-REGISTERED in session chat before execution. Verify script:
`code/2928_sc_entrainment_c4_confrontation.py` (all checks PASS,
exit 0).**

---

## §1 — THE MODEL AND THE PRE-REGISTRATION

The one-shot 2900 model displaces each DP once, using undisplaced
geometry. The self-consistent (SC) closure solves

    δ = ε · amp(y+δ) · û(y+δ)

by fixed-point iteration (tol 10⁻¹², divergence-guarded) — the DP's
displacement responds to the retarded CP field at the DP's **actual**
position. Two return conventions isolate the modeling fork rather than
silently choosing: **V1** keeps 2900's convention F = amp(y)·G(y+δ*)
(displacement-only self-consistency — clean ablation); **V2** fully
displaces the response strength, F = amp(y+δ*)·G(y+δ*).

Pre-registered verdicts at the SC cancellation point ε\*_SC (c = 0):
CONFIRMED |c₄| < 0.03; REFUTED |c₄| > 0.15; PARTIAL between; NO-ZERO
if c never crosses zero in the convergent region. Side prediction from
the O(ε²) advection structure (∇h)[h], h = amp·û: SC amplifies the
inward displacement, so ε\*_SC < 0.0589.

## §2 — RESULTS (reference config m = 2, r = [1, 12])

| | ε\*_SC | k(ε\*_SC) | **c₄(ε\*_SC)** | verdict |
|---|---|---|---|---|
| one-shot (2900) | 0.05893 | −16.96 | −0.373 | — |
| **V1 (SC)** | 0.04222 | −16.62 | **−0.923** | **REFUTED** |
| **V2 (SC)** | 0.02070 | −16.44 | **−0.612** | **REFUTED** |

**Self-consistency drives the β⁴ pathology deeper, not to zero** —
V1's |c₄| is 2.5× the one-shot value. The c₄ = 0 and c = 0 points do
not coincide in either variant: one dial cannot meet the all-orders
requirement in the SC closure either, and self-consistency widens the
miss. Both side observations confirmed: ε\*_SC < 0.0589 in both
variants (advection amplifies; the measured advection term at β = 0.1
is (D_SC − D_os)/ε² = −3.76), and c₄'s verdict is grid-robust
(−0.923 → −0.878 at 960×1440, same band).

**Structure of the map itself:** the fixed point exists only for
ε < ε_conv ≈ 0.0658 at this configuration — the SC closure has a
finite basin (inward displacement → larger amp → more displacement →
runaway). ε_conv is identical across V1/V2 (they share the
displacement map; internal check). Two notable placements: the
one-shot cancellation point 0.0589 sits **barely inside** the basin,
and both SC cancellation points sit well inside it — the refutation is
not a boundary artifact.

## §3 — SCOPE: WHAT IS REFUTED AND WHAT REMAINS LIVE

**Refuted:** the registered prediction at its anticipated test — the
fixed point of the displacement field, in both return conventions. The
steady-state argument's premise (the curvature is a transient of the
undressed background, removable by dressing the displacement field) is
not realized in this closure class.

**Remains live, now sharply separated:** the stronger reading of
"full self-consistency" — a travelling steady state, time-independent
in the co-moving frame, with Sea-side (DP–DP) coupling. This model
class contains no DP–DP interaction and imposes no co-moving
stationarity condition; the 2928 result proves those ingredients are
not decorative: **whatever delivers exact linearity for direction (A),
it is not displacement-field dressing.** This connects directly to
OPEN-EW-ANTISCREEN-1 — the measured many-body inversion is precisely
the kind of Sea-side collective physics absent from this closure — and
to the founder's constant-SSV_net picture, which is a statement about
travelling steady states of the *coupled* system (the 2900 fragment's
"different theorems" remark, now with a measured teeth mark).

**What this does NOT mean:** direction (A) is not dead — its cheap
version is. Newton I's status is unchanged; the B1 obstruction stands,
exact (2926), with the one-dial and dressed-one-dial routes now both
closed by measurement. Ledger untouched. No frontier items opened or
closed; completion note in `frontier_sectors/EW.md` (sketch-tier per
the 2926 PD-006 scope ruling).

## §4 — HONEST RESIDUALS

1. ε_conv ≈ 0.0658 was located at one configuration; its scaling
   (presumably ~r³_min like everything else at this order) is
   unmeasured — registered as a natural follow-on, not claimed.
2. The advection term's exact coefficients (Δχ₁, Δχ₃ — the SC
   correction to the 2927 closed forms at O(ε²)) are derivable by the
   same contraction machinery but were NOT derived this patch; the
   numeric constancy check (Part A) confirms SC = one-shot at O(ε)
   and measures the advection magnitude only. Queued, not claimed.
3. The [1, β², β⁴] fit truncation biases c₄ at the few-percent level
   (2926 §4); the verdict margin (0.92 vs the 0.15 band) is ~6× that
   bias. The verdict does not depend on fit forensics.
