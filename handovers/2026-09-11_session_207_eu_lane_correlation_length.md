# EU-lane Handover — Session 207 Close (11 Sep 2026) — Gaussianity cleared; the amplitude is one number; the question inverts to saturation

**Patch 3897. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3895 at session start; 3896–3897 delivered as patch files. **Next free: 3898.** GR lane: next free 3715.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).

## The single most important next action — worker work, in-lane
**Find C-5's saturation mechanism: what arrests the SCP-affinity correlation at ≈138 PSR?**

**Three candidates, none evaluated** — and the ordering is deliberate:
1. **The eDP pair-swapping channel (3894).** *Start here.* It destroys correlation as fast as the q-channel builds it, which is a **natural competing rate**, and it comes from **the founder's own mechanism** rather than from outside it.
2. **The PSR's contraction under load** (3837's B2 floor) — a shortening reach as occupancy rises.
3. **Horizon exit**, if the affinity propagates slower than 1 PSR per Moment.

> **PD-007 WARNING, and this is now the live risk:** the figure **138 came from the observed amplitude**. It is a **requirement, not a prediction**. Any saturation mechanism must be **derived from the dynamics and then compared** against it — **never tuned to land on it.** A candidate with a number to hit is exactly the condition under which that bar gets quietly violated.

## What was established
**The bare range is a protocol fact, not an estimate.** The affinity is mediated by **arriving DI-bits** (SSV_net), and **AP-4/AP-4c give the DI-bit a hard reach** — deposit at the PSR shell, near field by the hop cascade within. **Bare correlation length = 1 PSR.** At the pivot R_H = 5.2×10⁴ l_P ⇒ **1.4×10¹⁴ independent patches per Hubble volume.**

### Gaussianity clears — by eleven orders
Excess kurtosis of a sum of N independent patches goes as **κ_patch/N**. Even a **cascade-like patch kurtosis of 10³** gives a **mode kurtosis of 7.2×10⁻¹²**, against Planck's f_NL bound of O(5–10).

> **0730's wall does not apply to C-5.**
>
> **This is the first time in this arc that a candidate has PASSED a test which killed a predecessor**, rather than failing the same one by a smaller margin. The reason is **structural, not lucky**: a cascade at observable scales is *one correlated object*, while C-5's affinity is microscopic and gets averaged over 10¹⁴ independent patches before anything observable forms.

### The amplitude fails at the bare range — by 3 orders, not 40
Matching ζ ≈ 4.6×10⁻⁵ would need a **per-patch δ ln f of 1.6×10³**; a log-fraction fluctuation within one correlation volume cannot plausibly exceed **O(1)**. So **ζ(1 PSR) = 2.8×10⁻⁸ — short by ~1600×.** Still a failure. Also the **first three-order failure in a sequence of forty-order ones.**

### The target — one number, and it is sharp
> **ζ = ⅓ · (ℓ_corr/R_H)^{3/2} ⇒ ℓ_corr ≈ 138 PSR.**

| ℓ_corr | ζ/ζ_obs |
|---|---|
| 1 PSR | 6×10⁻⁴ |
| 10 PSR | 1.9×10⁻² |
| **138 PSR** | **1.0** |
| 500 PSR | 6.9 |
| R_H | 7.3×10³ |

**Sharp, not a window** (ζ ∝ ℓ^{3/2}). **And Gaussianity is still safe there** (mode kurtosis 1.9×10⁻⁵) — **both tests pass at the same correlation length**, which was not guaranteed.

### The question inverts
**Reachability is trivial:** correlations grow ~1 PSR per Moment, there are 5.2×10⁴ Moments per e-fold, so **138 PSR takes 0.0027 e-folds.** The system has 64.

> **That is the problem, not the solution.** Unchecked, correlations run to R_H, N_ind → 1, and **ζ overshoots by 7×10³.** **C-5 needs a brake, not a driver.**

## C-5's debts, current
1. ~~Referent~~ (3890). 2. ~~Reservoir~~ (3892). 3. ~~Correlation length~~ — **computed here; Gaussianity cleared, target set.**
4. **The saturation mechanism** — **NOW THE GATE.**
5. **Adiabaticity** vs Planck's isocurvature bound.

## Owed (elsewhere)
- **Isak:** recompile **EU-1 (V1.6)** and GR-2 (V2.11).
- **Maintainer:** CONV-046 — **the package now carries a live candidate with a derived ζ, a stated microphysics, and one observational test cleared**; the amended DE escalation (3858); cosmic-web owed piece (3833); `DM_project_map.md` stale (3884).
- **EU-1 V1.7 (bundle):** 3854 VSL clarification; 3876 §5 as qualified by 3878. **Do not add C-5.**

**Anti-priorities:** **do not report C-5 as working** — one test cleared is not four; **do not tune a saturation mechanism to 138** (PD-007, now the live risk); **never supply the stack number**; follow **§0.5 D-1…D-6**; no cross-lane edits without sanction; do not retire 3710; **nothing in this arc refutes n_s** — PRED-C-96 reads 0.9654 (V1.6).

## §15 Steps A–H
- **A** `session_logs/2026-09-11_session_207_log.md` (3897). **B** transcript row 3896. **C** development vignette (Session 207).
- **D** Tier 4: `reasoning/3896_correlation_length.md`.
- **E** Registries: `research_frontier.md` (3896 prepend); `id_block_registry.md` (next free 3898); `future_projects.md`; in-place update at `scp_differential_affinity.md` §5b. N/A: `predictions.md`, `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md` — **C-5 is live, not adopted.**
- **F** none (no panel). **G** no PD minted; no founder ruling needed. **H** this file.

## Governance note
**The inversion is the thing to carry.** The instinct on reaching a target number is to ask whether it is attainable; here attainability was trivial and the difficulty was the opposite — **nothing in the picture stops the growth.** Had the reachability question been answered and the session closed there, C-5 would have been recorded as clearing the amplitude when it does no such thing.

**When a mechanism must produce a specific scale, check what bounds it from above before celebrating that it can reach it.**
