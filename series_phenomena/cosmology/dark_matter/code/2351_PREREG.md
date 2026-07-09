# PRE-REGISTRATION — Patch 2351, G3 per-dSph likelihood (written before any computation)

**Question (gate G3 of 2346/F3; the rigorous version of the 2345 synthesis):** does
the G1/G2-passing population satisfy the PER-GALAXY dSph demands — Correa-class
gravothermal modeling with Gaia pericentre-informed orbits — rather than merely the
aggregated window?

**Source, fixed now:** Correa 2021 (MNRAS 503, 920; arXiv:2007.02958), read in full
this session. Her per-dSph preferred σ/m ranges (Table 2, verbatim; ranges already
include her adopted factor-2 gravothermal-vs-N-body uncertainty) with core collision
velocities ⟨v⟩ given in-text for three dwarfs — these three are the EXACT anchors:
- **LeoII: ⟨v⟩ ≈ 21 km/s, σ/m ∈ [90, 150] cm²/g**
- **Carina: ⟨v⟩ ≈ 48 km/s, σ/m ∈ [40, 50] cm²/g**
- **Draco: ⟨v⟩ ≈ 58 km/s, σ/m ∈ [20, 30] cm²/g**
Her global fit (computed from her verbatim parameters, NOT digitized): σ_C(v) =
σ₀/(1+(v/w)²) with m_χ = 0.648±0.154 GeV, m_φ = 0.636±0.055 MeV, α_χ = 0.01 ⇒
σ₀ ≈ 109 cm²/g, w ≈ 29.4 km/s (±1σ propagated in-code). Her stated systematics,
adopted as the demand-side tolerance: C/b calibration ×1.5 (her ranges are LOWER
limits in this direction), t_trunc ×1.13, MW mass ×1.2, v_T orbital errors moving
per-dwarf demands by 50% to order-of-magnitude. **Pre-registered per-anchor
tolerance U = 2** (each anchor window widened to [lo/2, 2·hi]); **demand-curve band
[σ_C/2, 3σ_C]** (asymmetric: her caveats are lower-limit-weighted).

**Strand statement, registered before running because the arithmetic is visible:**
the Correa demand is the COLLAPSE STRAND — the steep end of the demand heterogeneity
the L4 audit (2345) mapped. The isothermal strand (Valli & Yu 0.1–40; RKVY-class
3–40) is the strand the audited frames already embody, and G1/G2 passed it. Rough
arithmetic on the stored passing curves (σ(30) ≈ 10–17) vs the Correa central demand
(σ_C(30) ≈ 53) suggests a ×2–5 shortfall at the collapse strand; the scan decides
whether the kinetic knob box can close it jointly with pin/LSB/cluster. This is
stated now so a strand-split result cannot be retro-narrated as expected-all-along
without the record showing it was.

**Protocol, fixed now:**
1. **Shape leg:** the ⟨v⟩-ordering of the three anchors (LeoII > Carina > Draco in σ,
   inverse in v) is the density–pericentre anticorrelation's imprint; our curves
   must be monotone decreasing over [21, 58] km/s to reproduce it.
2. **As-stored evaluation (2345 P4 discipline):** the G1/G2 passing points evaluated
   against the three anchors (with U = 2) and the demand band BEFORE any re-tuning;
   per-anchor violation r_i = max(lo_i/(U·σ(v_i)), σ(v_i)/(U·hi_i), 1).
3. **Joint re-search:** over the G1 knob box (α ∈ [10⁻²,10⁶], log₁₀S₀ ∈ [−6,2],
   p ∈ [0,16], R_s ∈ [20,120]), objective = max(three Correa anchors at U = 2;
   pin/LSB/cluster windows) — run at BOTH frame variants of pin/LSB (central,
   extended); dSph aggregate window replaced by the per-dwarf anchors (that is the
   point of G3). Envelope-on evaluation of the best point as a robustness row
   (full envelope re-search out of scope, stated).
4. **Strand grading:** the audited-frame (isothermal-strand) per-dwarf status is
   inherited from G1/G2 window passes; G3 grades the collapse strand and reports
   the measured gap.

**Pre-registered outcomes:**
- **(i) PASS-both-strands:** a kinetic population satisfies all three Correa anchors
  (U = 2) jointly with pin/LSB/cluster at either audited frame variant. The
  population is robust to the strand choice; G3 clears unconditionally.
- **(ii) STRAND-SPLIT-quantified:** collapse-strand anchors missed by a measured
  factor at every point of the box while the isothermal strand holds (inherited).
  G3 then delivers a quantified strand-dependence: the F3 auto-proposal goes to the
  founder carrying the measured cost of the frame choice — adopting the audited
  frames is adopting the isothermal strand, with the collapse-strand gap stated in
  numbers. Gate status: CLEARED-conditional-on-strand (the founder's frame decision
  subsumes the strand decision; no computation can arbitrate between published
  strands).
- **(iii) FAIL-both:** the box misses the per-dwarf demands under both strands
  (including the audited-frame inheritance failing re-examination) → G3 fails and
  the F3 path stops.

**No verdict moves regardless of outcome:** v1 kill final; G3 gates frame adoption
and the papers' population section only.
