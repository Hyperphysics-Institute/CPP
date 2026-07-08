# The formation rent check: the kinetics pay — and the dimer was never the point (Patch 2349)

**What this is:** frame-adoption gate **G1** (2346/F3; the 2344 rent's first leg),
founder-directed as the session's first computation. *Namespace note: this is the
frame-adoption G1, not Gate-1/B1's G1 (2313) — files carry the `dsph_` prefix.*
**Pre-registration:** `code/2349_PREREG.md`, written before the engine ran.
**Verify:** `code/2349_g1_grading.py` (6/6); engine `code/2349_g1_engine.py`,
audits `code/2349_g1_audits.py`, data `2349_results.json` / `2349_audits.json` /
`2349_naturalness.json`. **NO VERDICT MOVED.**

## 1. The question and the protocol

The 2344 rent as written: *"the 1855–56 aggregation kinetics either produce dimer
dominance or they don't."* The pre-registered operationalization: solve the **full
population balance** of the registered 1855 mechanism (burst pool; irreversible dimer
nucleation α·c₁²; monomer-addition growth at two ends; no coalescence; single knob
α = k_n/k_g), assign couplings by a single-valued law S(N) = S₀(N/2)^p, and evaluate
the resulting mass distribution on the **identical 2344 rig** (validator: reproduces
the stored 2344 totals to <10⁻⁹). Knob box fixed in advance: α ∈ [10⁻², 10⁶],
S₀ ∈ [10⁻⁶, 10²], p ∈ [0, 16], R_s ∈ [20, 120] fm. 66,759 coarse configurations +
per-frame refinement + depth, steepness-profile, naturalness, channel, and truncation
audits.

## 2. Outcome (i) fires — with a reframe the pre-registration anticipated

**The kinetic family passes both audited frames, strictly in-box:**

- **Audited-extended: DEEP and UNSTRAINED.** Passes at **natural α = 1** (the 1855
  "all E_qq ends alike" point) and across 1855's own quoted α ~ 0.01–0.1 range;
  minimum interior margin ×2.18; **p_min = 0 — even a flat S(N) passes**. The
  carrying structure is the broad short-rod population itself (N ~ 3–25, unimodal),
  channels distributed, no extrapolation, floors negligible except under the cluster
  ceiling where they belong.
- **Audited-central: SHALLOW and STRAINED.** Best depth ×1.032 (grazes the dSph low
  edge); natural α = 1 misses by ×1.064; needs α ≈ 3–6 (a factor-few nucleation
  bias — mild) **and p ≥ 13**: the S(N) steepness demand is now *measured*, one
  power worse than 2344's named N¹² strain.

**The dimer reframe.** f₂ = 0.99 is reachable (α_99 ≈ 989, measured) but **not
required**: the 2344 "dimer + trace-N≈5" object was the two-delta parametrization's
way of expressing the demand, not the demand itself. The kinetics' unimodal
Poisson-mixture family — which *cannot* realize the two-delta gap (pre-registered
structural sub-question, confirmed) — finds its own passing corners. The rent is
**DISCHARGED-reframed**.

## 3. The verdict-favorable face, stated because it must be

At the **registered v1 frame** the formation-realizable family does *worse* than the
unconstrained mixture: best violation **×1.189 vs ×1.074**. Formation kinetics push
the population *farther* from passing at v1 — the kill is strengthened, not
threatened, exactly where it was graded.

## 4. What this gates and what it doesn't

G1 = **PASSED-with-texture**. Under F3's terms, one of three gates for the v2
adoption auto-proposal is cleared; **G2 (satellite survival) and G3 (per-dSph
likelihood) remain owed**. The texture matters for the papers: if the audited frame
is *extended*, the population story is natural end-to-end (un-tuned kinetics, no
S(N) steepness demand); if *central*, it carries two named strains (α ≈ 3–6,
S ~ N¹³). Inverse-coefficient ledger gains: α_pass(central) ≈ 3–6; p_min(central)
= 13; α_99 ≈ 989. The S(N) rent leg (survive derivation at the required steepness)
now has its bar measured per frame — 13 at central, none at extended.

## 5. Honest caveats

(i) S(N) power-law form assumed — the family 2344's physicality audit named; a
derived S(N) outside power-law form re-poses the question (bounded: p_min profiles
are smooth). (ii) The rig inherits every 2344 assumption (F(ε) central-potential
family, √(S_iS_j) mixing, velocity floors from the repulsive coat). (iii) 1856's
transport-efficiency suppression is not applied; at the central pass (N ~ 2–6) rods
are near-spherical and ε ≈ 1, but the extended pass leans on N ~ 15–25 where the
1856 fork could bite — **named follow-up, feeds G2**. (iv) Integer N used (physical
case); 2344's continuous-N optimum was never reachable by formation anyway.
