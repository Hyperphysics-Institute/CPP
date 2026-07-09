# CONV-001 FLASH VERIFICATION BRIEF — the 2375 full-distribution grade (Q3b-1 candidate kill)

**Round type:** FLASH (2354/2367 pattern) — one computation, five items, fast turnaround.
**Patch under review:** 2375 (`code/2375_q3b1_full_distribution_grade.py` + `2375_results.json` +
`2375b_verdict_robustness.json` + `2375_unit_counts.json`; arc doc §Q3b-1 in
`sN_arc_2370_cost_estimate.md`; `reasoning/2375.md`).
**Assembled:** Patch 2376, 9 July 2026 (founder "Recommend and proceed.").

## The stakes, stated plainly
2375 is a **candidate kill of the equilibrium-shaped (Flory/isodesmic) small-N population
family** — the successor family that survived Q1 (2371) and the corrected Q2 corridor (2374c).
If verified, the OPEN-DM-DSPH-1 lane's derivation demand narrows to a single sharp question
(can substrate kinetics produce a strongly non-Flory, near-bidisperse distribution?) and Q3b-2's
weeks-scale investment is either aimed or abandoned on that answer. If refuted, the equilibrium
family reopens and Q3b-2's target changes entirely. No release date is at risk (DM-2 shipped
alone on the 20th per 2369/2364-superseded; DM-1/DM-3 remain KILLED-NOT-REWRITTEN). **No verdict
has moved; this round decides whether one may.**

## What was computed (one paragraph)
The Flory (isodesmic equilibrium) family w(N) = N x^(N−1)(1−x)², parameterized by ⟨N⟩ₙ, was
graded in BOTH channels: (i) the summed-spectrum XQC per-bin criterion (the 2374c correction,
verbatim) at the corridor floor (S_c = 0.012; ρ ∈ {0.2, 0.3}; both signs), species N = 1–32 with
a hurting-direction additive tail bound — a 1-D viability curve over ⟨N⟩ₙ ∈ [1.5, 12], exhaustive
on a 0.25 grid, scan-independent; and (ii) the anchor suite at the audited frames via the exact
N-species generalization of 2344's own two-species eff() (σ/m = Σᵢⱼ wᵢwⱼ sᵢⱼ Kᵢⱼ,
Kᵢⱼ = (1/Mᵢ+1/Mⱼ)/2), coupling law g²(N) = g₀²(N/4)^p (the registered strain family), scanned
over (⟨N⟩ₙ, g₀², p, R_s). Results: XQC — NO ⟨N⟩ₙ viable at ANY surviving corridor point
(closest ×1.214, repulsive/ρ=0.2/⟨N⟩ₙ=6; ×2.593 attractive/ρ=0.3; binding bin 36–128 eV
throughout); anchor — the central frame refuses Flory outright (best ×1.043), the extended frame
admits passes (⟨N⟩ₙ ≈ 9.6, p ≈ 5.9; verdict-robust to N_cut = 192) — all at XQC-unviable ⟨N⟩ₙ.

## The five items (grade each: VERIFIED / REFUTED-with-the-error-named / INDETERMINATE-with-the-check-named)

**V1 — the eff() distribution generalization (a load-bearing construction).** Is
σ/m = Σᵢⱼ wᵢwⱼ sᵢⱼ Kᵢⱼ with Kᵢⱼ = (1/Mᵢ+1/Mⱼ)/2 and sᵢⱼ = R_s²·Fi(gᵢgⱼ/(0.5 μᵢⱼ b R_s)) the
correct N-species extension of 2344's two-species expression under the registered J4 pairwise
additivity? The two-species limit reproduces stored 2371 totals to 2.6e-16 (both compositions).
Challenge invited: name any defensible alternative (number- vs mass-fraction weighting, cross-
channel kinematic factors, a different diagonal convention) that changes either the central-frame
refusal or the extended-frame pass structure — and show the direction of the change.

**V2 — the summed-XQC criterion + the tail bound (the kill's load-bearing channel).** (a) Is the
summed-spectrum per-bin criterion carried verbatim from 2374c (single-species limit reproduces
stored 2366b exactly: viol = 3, total 642.219095)? (b) Is the additive tail bound —
tail_mass × ρ × max_N c_N(bin) added to every bin before grading — genuinely conservative
(hurting the kill, i.e. favoring survival is the required direction: does the bound only ever
make a PASS harder to claim and never easier)? (c) The monomer (N = 1) uses the POINT potential
(L = 0; the folded shell is undefined there) — is that convention sound and disclosed?

**V3 — truncation handling and the V-c discharge (process integrity).** Two events are owned in
`reasoning/2375.md` §2: a first-run N_cut = 32 truncation artifact (a fake extended-frame pass at
⟨N⟩ₙ = 11.1) caught by V-c BEFORE recording, and the final V-c FAILING its pre-registered 0.5%
totals tolerance at 1.03% (96→128) — reported as FAIL — with the decisive content discharged by
executed check: the PASS verdict invariant at N_cut 96/128/192 plus a 2500-step anneal AT
N_cut = 128 converging to the same point (`2375b_verdict_robustness.json`). Is the discharge
sound, or does the 1% totals sensitivity hide anything verdict-relevant?

**V4 — scan adequacy (aim here only after V2).** The anchor scan ran 30k wide + 6k×2 anneal
(reduced from 150k/20k for tractability, DISCLOSED; seed-stability clean) over ⟨N⟩ₙ ∈ [1.5, 12],
g₀² ∈ [1e-6, 1e3], p ∈ [0, 14], R_s ∈ [20, 100]. Could an anchor pass be hiding (wider p, larger
⟨N⟩ₙ, a coupling law inside the strain family's registered spirit)? NOTE THE JOINT STRUCTURE
before spending effort here: the XQC verdict is scan-independent (an exhaustive 1-D curve), and
XQC unviability at every corridor point is what does the killing — a missed anchor pass at
XQC-unviable ⟨N⟩ₙ changes nothing. A finding here is verdict-relevant ONLY if it names an
⟨N⟩ₙ that ALSO escapes V2's gate.

**V5 — consequence mapping and containment.** (a) Does the computed scope (Flory = ONE
equilibrium shape; g₀²(N/4)^p on the anchor side; floor grid points on the XQC side, higher S_c
standing excluded from 2374c's two-species grade) support the claimed sharpening — "the corridor
hosts near-bidisperse populations only; death mode (ii) rearmed: critical nucleus N_c ≥ 3 AND a
stiff ceiling above N ≈ 6, or the third kill lands fully derived"? (b) Is the containment right
(CANDIDATE only; no verdict moved; no paper touched; the 2371 two-species points explicitly
still passing both channels at central-repulsive)? (c) Cite the rows if you dispute the
consequence chain.

## Rules of the round
- **Rent rule on saves:** any proposed rescue of the equilibrium family must name its mechanism
  and pay its rent — an alternative distribution shape must still be equilibrium-derivable, or
  it concedes 2375's point and belongs to Q3b-2's non-equilibrium demand.
- **Halting:** REFUTED on any of V1–V3 HALTS the candidate kill (the computation is wrong and the
  round completes on the corrected number). A V4 REFUTED that survives its own V2 joint reopens
  the family. V1–V5 VERIFIED = adjudication-ready for the founder.
- **Deliverable per panelist:** five grades + at most 2 ranked findings. Re-ran-vs-audited
  disclosure required (state whether you executed code or audited it).
- **Seats:** five (2363 mapping discipline: seat-blank relay labels R1–R5; self-IDs are claims,
  founder mapping governs; Copilot seat — paste files directly per the standing 2368 fix).

## NO VERDICT MOVED. The founder's adjudication block opens when the returns land.
