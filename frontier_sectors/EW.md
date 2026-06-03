<!--
  Extracted from Research_Frontier.md lines 1020-1100
  Source range: Electroweak Sector
  Extraction date: 2026-05-25
  Master dashboard: Research_Frontier.md
-->

## Electroweak Sector (EW) — 6 problems

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
