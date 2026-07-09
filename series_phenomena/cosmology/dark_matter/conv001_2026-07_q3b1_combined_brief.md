# CONV-001 COMBINED ROUND — VERIFY THE 2375 CANDIDATE KILL + THE SURVIVAL CHANNEL (Q3b-1)

**Round type:** COMBINED (founder-directed, Patch 2377; supersedes the 2376 flash-only brief
before any submission). Verification items V1–V4 harden the wall; item R asks each panelist
where the door is. **Founder's rationale, on the record:** with no release at risk and the arc
at a genuine impasse, generative capacity is worth engaging — and the prior generative round's
weakness (open-ended "any ideas" inviting rent-free spray) is repaired here by anchoring every
proposal to the computed facts and pricing it with rent.
**Patch under review:** 2375 (`code/2375_q3b1_full_distribution_grade.py` + `2375_results.json`
+ `2375b_verdict_robustness.json`; arc doc §Q3b-1 in `sN_arc_2370_cost_estimate.md`;
`reasoning/2375.md`; the corrected criterion in `code/2374c_summed_criterion_regrade.py`).

## The stakes, stated plainly
2375 is a **candidate kill of the equilibrium-shaped (Flory/isodesmic) small-N population
family** — the successor family that survived Q1 (2371) and the corrected corridor (2374c). If
the verification items hold, the derivation demand narrows to one sharp question (can substrate
kinetics produce a strongly non-Flory, near-bidisperse distribution at the island-floor coupling
in the repulsive channel?) — and the R returns decide whether Q3b-2 has more than one road to
try. **No verdict has moved; no release is at risk** (DM-2 shipped alone; DM-1/DM-3 remain
KILLED-NOT-REWRITTEN).

## What was computed (one paragraph)
The Flory family w(N) = N x^(N−1)(1−x)², parameterized by ⟨N⟩ₙ, graded in BOTH channels:
(i) the summed-spectrum XQC per-bin criterion (2374c, verbatim) at the corridor floor
(S_c = 0.012; ρ ∈ {0.2, 0.3}; both signs), species N = 1–32 with a hurting-direction additive
tail bound — an exhaustive 1-D viability curve over ⟨N⟩ₙ ∈ [1.5, 12]; and (ii) the anchor suite
at the audited frames via the exact N-species generalization of 2344's two-species eff()
(σ/m = Σᵢⱼ wᵢwⱼ sᵢⱼ Kᵢⱼ, Kᵢⱼ = (1/Mᵢ+1/Mⱼ)/2), coupling law g²(N) = g₀²(N/4)^p, scanned over
(⟨N⟩ₙ, g₀², p, R_s). **Results:** XQC — NO ⟨N⟩ₙ viable at ANY surviving corridor point (closest
×1.214 at repulsive/ρ=0.2/⟨N⟩ₙ=6; ×2.593 at attractive/ρ=0.3; binding bin 36–128 eV
throughout); anchor — the central frame refuses Flory outright (best ×1.043); the extended
frame admits passes (⟨N⟩ₙ ≈ 9.6, p ≈ 5.9; verdict-robust to N_cut = 192), all at XQC-unviable
⟨N⟩ₙ. **The contrast:** the 2371 two-species points still pass BOTH channels at the
central-repulsive corner.

## PART I — VERIFICATION (grade each: VERIFIED / REFUTED-error-named / INDETERMINATE-check-named)

**V1 — the eff() distribution generalization (load-bearing construction).** Is
σ/m = Σᵢⱼ wᵢwⱼ sᵢⱼ Kᵢⱼ with Kᵢⱼ = (1/Mᵢ+1/Mⱼ)/2 and sᵢⱼ = R_s²·Fi(gᵢgⱼ/(0.5 μᵢⱼ b R_s)) the
correct N-species extension of 2344's two-species expression under registered J4 pairwise
additivity? (Two-species limit reproduces stored 2371 totals to 2.6e-16, both compositions.)
Challenge: name any defensible alternative (number- vs mass-fraction weighting, cross-channel
kinematics, diagonal convention) that changes the central-frame refusal or the extended-frame
pass structure — with the direction of the change.

**V2 — the summed-XQC criterion + the tail bound (THE load-bearing channel).** (a) Is the
summed-spectrum per-bin criterion carried verbatim from 2374c (single-species limit reproduces
stored 2366b exactly: viol = 3, total 642.219095)? (b) Is the additive tail bound —
tail_mass × ρ × max_N c_N(bin), added to every bin before grading — genuinely conservative in
the required direction (only ever making a PASS harder to claim, never easier)? (c) Is the
monomer point-potential convention (N = 1, L = 0) sound and disclosed?

**V3 — truncation handling + the V-c discharge (process integrity).** Two events owned in
`reasoning/2375.md` §2: a first-run N_cut = 32 truncation artifact (fake extended pass at
⟨N⟩ₙ = 11.1) caught by V-c BEFORE recording; and the final V-c FAILING its pre-registered 0.5%
totals tolerance at 1.03% (96→128) — reported as FAIL — with the decisive content discharged by
executed check (PASS verdict invariant at N_cut 96/128/192; a 128-anneal converges to the same
point). Is the discharge sound, or does the totals sensitivity hide anything verdict-relevant?

**V4 — scan adequacy + consequence mapping + containment (one grade).** (a) The anchor scan ran
30k wide + 6k×2 anneal (reduced from 150k/20k, DISCLOSED; seed-stability clean) over
⟨N⟩ₙ ∈ [1.5, 12], g₀² ∈ [1e-6, 1e3], p ∈ [0, 14], R_s ∈ [20, 100] — could a pass hide? NOTE the
joint structure before spending effort: the XQC channel is scan-independent (exhaustive 1-D
curve) and does the killing; an anchor-side find is verdict-relevant ONLY if it names an ⟨N⟩ₙ
that also escapes V2's gate. (b) Does the computed scope (Flory = ONE equilibrium shape; the
g₀²(N/4)^p family; floor grid points, higher S_c standing excluded from 2374c) support the
stated consequence — "the corridor hosts near-bidisperse populations only; death mode (ii)
rearmed: critical nucleus N_c ≥ 3 AND stiff ceiling above N ≈ 6, or the third kill lands fully
derived"? (c) Is the containment right (CANDIDATE only; no verdict moved; no paper touched)?
Cite rows to dispute.

## PART II — R: THE SURVIVAL CHANNEL (at most ONE proposal per panelist; abstention is honorable)

Each panelist may propose **at most one** mechanism by which a small-N population survives BOTH
channels. Quality over spray: one, priced, or none.

**The computed facts a proposal must push against (evade one, quantitatively):**
| # | Fact | Source |
|---|---|---|
| F-a | Every Flory ⟨N⟩ₙ ∈ [1.5, 12] fails the summed XQC gate at every surviving corridor point; binding bin 36–128 eV; closest miss ×1.214 | 2375 |
| F-b | The central audited frame refuses the Flory shape outright (best ×1.043) | 2375 |
| F-c | The corridor exists only at the island floor: central-repulsive keeps 5.7% of the island at ρ=0.3, 14.7% at ρ=0.2; ρ* = 0.411; attractive-sign corridors hair-thin | 2374c |
| F-d | Joint contamination bounds at the live corner: w(2) < 0.034, w(1) < 0.013 (ρ=0.3) | 2374c/2374 |
| F-e | The two-species points N=(3,6) w=0.064 and N=(4,5) w=0.217 pass BOTH channels at central-repulsive | 2371/2374c/2375 |
| F-f | Freeze-out demand E_bond/kT_form = 23.2–36.2; fragmentation-window closure holds | 2374 |
| F-g | Absolute E_bond is root-blocked on OPEN-FP-SF-2-η; no coupling may be fabricated | 0865/scoping doc |

**RENT (all three, or the proposal is not accepted into the record):**
1. **Names its evasion:** which fact(s) above it evades and HOW, with at least an order-of-
   magnitude quantitative sketch (e.g., "a distribution with support only on N ∈ {5, 6} at
   weights w evades F-a because…" — show the bin arithmetic direction).
2. **Substrate-derivable in principle:** the mechanism must be expressible in registered CPP
   primitives (SSV bonds, PCD kinetics, ring-closure statistics, Sea thermodynamics) with NO
   smuggled free parameters — a shape postulated to fit is a concession, not a save.
3. **Carries its own cheap kill:** a one-session test with the existing machinery (the 2375
   unit-count cache + eff_dist make most distribution shapes gradeable in minutes) that would
   kill the proposal if it fails. State the test and its kill condition.

**Ordering rule:** R-proposals are pursued only against the VERIFIED computation. A panelist who
returns REFUTED on V1–V3 has mooted their own R-proposal until the correction lands — flag it as
conditional if you do both.

**Seed directions a proposal MAY build on (not required, not privileged):** kinetic nucleation
with critical nucleus N_c ≥ 3 (0861 ring-closure bending cost); growth ceilings from geometric
frustration above N ≈ 6; fragmentation–reaggregation steady states pinned away from equilibrium
(0860 velocity trend); two-phase formation (distinct kT_form epochs → bidisperse); Sea-mediated
size selection (R_s(N) resonance per OPEN-SS-43). Each is UNPRICED until someone pays its rent.

## Rules of the round
- REFUTED on any of V1–V3 HALTS the candidate kill; the round completes on the corrected number.
- A V4(a) find counts only past its own V2 joint.
- V1–V4 VERIFIED = the kill is adjudication-ready for the founder; R-proposals that paid rent
  are queued for cheap-kill testing in founder-ruled order.
- **Deliverable per panelist:** four grades + ≤2 ranked findings + at most 1 rent-paid
  R-proposal (or explicit R-abstention) + re-ran-vs-audited disclosure.
- **Seats:** five (2363 seat-blank relay discipline: labels R1–R5; self-IDs are claims, founder
  mapping governs; Copilot seat — paste files directly per the standing 2368 fix).

## NO VERDICT MOVED. The founder's adjudication block opens when the returns land.
