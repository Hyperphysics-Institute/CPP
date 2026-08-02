<!--
  Extracted from Research_Frontier.md lines 1020-1100
  Source range: Electroweak Sector
  Extraction date: 2026-05-25
  Master dashboard: Research_Frontier.md
-->

## Electroweak Sector (EW) — 8 problems

### OPEN-EW-1: Derive η ~ 10⁻¹⁷ (Planck-to-Weak Scale Ratio)
**Status:** OPEN
**Sector(s):** EW
**Priority:** HIGHEST
**One-line statement:** Derive the hierarchy ratio η = l_P/r_EW from CPP, solving the hierarchy problem.
**What a solution looks like:** First-principles expression for η from 600-cell geometry.
**Dependencies:** None blocking (hardest single problem)
**Cross-sector connections:** OPEN-G-2
**Current best lead:** None strong. "Requires new scaling argument."
**Paper(s):** EW-2
**Last updated:** 23 March 2026

---

### OPEN-EW-2: Unified Boson Mass Formula
**Status:** OPEN
**Sector(s):** EW
**Priority:** HIGH
**One-line statement:** Single formula M_X = (sea_strength · ℏc/l_P) · f_geom(X) for all four EW bosons from subgraph geometry.
**What a solution looks like:** f_geom derivable from vertex counts and loop structure; W, Z, H at <1%; γ, g = 0.
**Dependencies:** OPEN-EW-3 (loop density), OPEN-EW-4 (mass ratios)
**Cross-sector connections:** OPEN-SS-6 (glueball shares same formula)
**Current best lead:** W, Z, H masses already reproduced at <1%.
**Paper(s):** EW-1–5
**Last updated:** 23 March 2026

---

### OPEN-EW-3: Loop Density 4D Projection Factor
**Status:** OPEN
**Sector(s):** EW
**Priority:** MEDIUM
**One-line statement:** Derive the numerical value of the 4D→3D projection factor in f_geom for the W bracelet.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-EW-2, CONJ-EW-1
**Current best lead:** Currently calibrated rather than derived.
**Paper(s):** EW-2
**Last updated:** 23 March 2026

---

### OPEN-EW-4: EW Boson Mass Ratios from Eigenvalue Ratios
**Status:** OPEN
**Sector(s):** EW
**Priority:** HIGH
**One-line statement:** Prove M_W : M_Z : M_H equals the relevant 600-cell eigenvalue combination.
**Dependencies:** None blocking
**Cross-sector connections:** sin²θ_W derivation
**Current best lead:** φ/(φ+1) = φ⁻¹ ≈ 0.618 does not match M_W/M_Z ≈ 0.882. Precise combination needed.
**Paper(s):** EW-3
**Last updated:** 23 March 2026

---

### OPEN-EW-5: W⁰ Virtual Particle — Quantitative Properties
**Status:** OPEN
**Sector(s):** EW
**Priority:** MEDIUM
**One-line statement:** Derive mass, width, and coupling of CPP W⁰ before Weinberg mixing.
**Dependencies:** CONJ-EW-1
**Cross-sector connections:** sin²θ_W derivation
**Paper(s):** EW-4
**Last updated:** 23 March 2026

---

### OPEN-EW-6: Chirality from Eigenvalue-Weighted Phase Bias
**Status:** OPEN
**Sector(s):** EW
**Priority:** MEDIUM
**One-line statement:** Prove weak interaction chirality arises from phase bias in icosahedral eigenvalue-weighted loop traversal.
**Dependencies:** None blocking
**Cross-sector connections:** Parity violation, OPEN-G-2
**Current best lead:** Only one helicity couples to W loop geometry; mechanism proposed but not proved.
**Paper(s):** EW-5
**Last updated:** 23 March 2026

---

**[Patch 0743 — physical cartoon recorded (not yet absorbed): B field as rotating DPs.** A moving charge radially polarizes the DPs (radial pole displacement = E) and swings each DP's like-pole around an axis (rotation = B) — so there is no separate B field, only rotating DPs; E and B are two motions of one DP response (hence μ₀,ε₀ share one stiffness, reinforcing the Patch 0740 Z₀-geometric result). The mathematical form exists in the corpus (EW-5 SSV-curl field strength; c06 B=curl-of-pattern); the **mechanical cartoon does NOT** — captured in `series_electroweak/development/b_field_as_rotating_dp_physical_cartoon.md` (Thomas's interpretation, w/ Grok). Small EM-sector task to fold it formally into EW-1 (Maxwell derivation) / c06 as the physical paragraph under the math.]**

**[Patch 2926 — arc queue item CLOSED: c = 1/5 DERIVED ANALYTICALLY.** The 2884/2900 round-trip drive admits an exact closed form — the outgoing-leg discriminant is a perfect square, d_out = r(1+2βμ+β²)/(1−β²), radial/angular dependence factorizes exactly (deriving the measured m- and r-range invariance), and D(β) = 2πR_m Σ 8β^{2n+1}/[(2n−1)(2n+1)(2n+3)] — the second difference of the even sphere moments. **c = 1/5 EXACT; c₄ = 1/35 exact (7/240 candidate REFUTED — fit-truncation artifact, explained to 3×10⁻⁵); c_{2n} = 3/[(2n−1)(2n+1)(2n+3)].** Confronted with the banked direct bound c = +0.91 ± 2.40 (Patch 2924): consistent. Sharper targets inherited by the entrainment cancellation programme and OPEN-HYB-SHAPE-1. Record: `flagship_papers/electromagnetism/sketches/c_one_fifth_analytic_derivation.md`; script `code/2926_c_one_fifth_derivation.py`. Sketch-tier per arc precedent; no items opened/closed; ledger untouched.]**

**[Patch 2927 — entrainment cancellation NON-UNIVERSAL; entrained drive closed-form through O(ε²).** The 2900 cancellation point ε* = 0.0589 was measured at one configuration; across the six robustness configs it spans 0.00735–0.44620 (×61). Exact theory: D(β;ε) = 2π[R_mΦ + εR_{m+3}Ψ + ε²R_{m+6}X] + O(ε³) with ψ₃(m) = −8(4m+1)/3, χ₃(m) = −4(m+1)(113m+22)/15; ε* = smallest positive root of R_mφ₃ + εR_{m+3}ψ₃ + ε²R_{m+6}χ₃ = 0 — a structure-tuned condition coupling the kinematic rationals to where the Sea's response lives (effective expansion parameter ~ε/r³ₘᵢₙ). Direction (A)'s burden is now a fixed-point statement against exact targets at all β-orders. Record: `flagship_papers/electromagnetism/sketches/entrainment_nonuniversality_record.md`; script `code/2927_entrainment_nonuniversality.py`. Sketch-tier; no items opened/closed; ledger untouched.]**

### OPEN-EW-ANTISCREEN-1: Collective Anti-Screening of the Bonded ZBW Sea
**Status:** OPEN
**Sector(s):** EW, SD
**Priority:** HIGH
**One-line statement:** The bonded ZBW Sea's persistent static response to a +1 source is polarization-REVERSED (+ member leans toward the source) while an isolated pair polarizes normally — derive the many-body inversion mechanism.
**Dependencies:** None blocking (measured; convention audited clean at Patch 2918)
**Cross-sector connections:** Statics rebuild (suspended 2892); ε₀/screening story of SF-6; the β⁰ core of the co-moving pattern (Patch 2917–2922 anatomy)
**Current best lead:** Founder-physics question candidate — what in the pair–pair ZBW bonding inverts the collective polarization? Data: `flagship_papers/electromagnetism/data/2918_control_fields.json`.
**Paper(s):** SF-6 successor / SF-8
**Registered:** Patch 2918; frontier entry Patch 2925.
**Last updated:** 1 August 2026

---

### OPEN-HYB-SHAPE-1: Hybrid Pipeline High-β Shape Failure — Mechanism Unidentified
**Status:** OPEN
**Sector(s):** EW, WORKFLOW
**Priority:** MEDIUM (deprioritized: the direct instrument answers the arc's question)
**One-line statement:** The hybrid Stage-2 drive turns over at β ≈ 0.15 while the direct measurement shows sustained growing drive through β = 0.30 (12σ sign-level refutation at Patch 2924) — identify the hybrid's high-β failure mechanism.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-K1-MEMORY-1 adjacency (pattern-window convergence); the parity-defect class (Patch 2920)
**Current best lead:** Prime suspect (window-support truncation growing with β) tested and KILLED at Patch 2924 §2. Remaining candidates: co-moving pattern non-convergence at short T; β³ basis leakage; kernel-weighted truncation.
**Paper(s):** none yet
**Registered:** Patch 2924; frontier entry Patch 2925.
**Last updated:** 1 August 2026

---
