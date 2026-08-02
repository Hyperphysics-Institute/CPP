# PRE-REGISTRATION — HYBRID ROUND 3b: PARITY-CLEAN EVALUATOR, SAME DATA, SAME BASIS, SAME GATE, SAME BANDS

**Patch 2921. Committed and presented BEFORE the corrected evaluator
produces any number. Inherits Patch 2919 in full EXCEPT the two
corrections below, both exactness restorations proven necessary at
Patch 2920 §2. NO NEW LEGS; NO band, gate, σ-bar, or basis changes.**

## §1 — CORRECTION 1: SYMMETRIC PATTERN EVALUATION

The pattern at ξ_ret is evaluated by **linear interpolation between
bin centers** (per ring), constant extrapolation forbidden — outside
[−11.5, +11.5] the pattern is 0, as before. This restores exact
mirror parity of the evaluator (frozen verification: the Patch 2920
mirror-pair kernel audit extended to the full drive — an exactly odd
pattern must give |D₀(0)| < 1e-15; this assert ABORTS on failure,
since with interpolation the zero is exact by construction).

## §2 — CORRECTION 2: PARITY PROJECTION OF THE p₀ CHANNEL

The static channel uses the odd part of the fitted p₀ (per ring,
exact by construction) — the β = 0 physics owns this symmetry; the
even residue is noise and is reported (unbanded) as a noise gauge.
p₁ and p₃ are NOT projected: motion legitimately breaks mirror
symmetry.

## §3 — EVERYTHING ELSE INHERITED VERBATIM FROM 2919

Per-bin basis and weights; bin admission (N ≥ 200 in all seven);
adequacy gate χ²/dof < 1.5 (already PASSED at 2920 and unaffected —
the corrections touch Stage 2 only); two channels with the transient
EXCLUDED; 200-fold bootstrap; the §4 bands of 2919 including
STATIC-SEA CONFIRMED/REFUTED vs c₀ = 1/5 and the TOTAL bands with
σ ≤ 0.05; the sanity register; the seeds-{10–15} escalation ladder.

## §4 — FROZEN INTERPRETIVE COMMITMENT

If Round 3b returns c_tot far outside [−0.05, 0.30] WITH σ_{c_tot} ≤
0.05 (i.e., a *measured* large curvature, not an inconclusive), the
result is INTERMEDIATE by the bands and the registered consequence is
physical, not procedural: the perturbative form D = kβ(1 − cβ²) is
declared inadequate on β ∈ [0.04, 0.2], and the next prereg must fit
D(β) non-perturbatively. No amount of band-nudging may convert such a
result into a Newton-I statement in either direction.

## §5 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds
DM-1/2/3; Candidate (B) 79.5%. G1, P-A2-1, statics suspension, 7 July
ruling stand.
