<!--
  Extracted from Research_Frontier.md lines 1165-1265
  Source range: Special Relativity / Gravity
  Extraction date: 2026-05-25
  Master dashboard: Research_Frontier.md
-->

## Special Relativity / Gravity (SR) — 8 problems

### OPEN-SR-1: PSR Reduction Formula from 600-Cell Geometry
**Status:** OPEN
**Sector(s):** SR
**Priority:** HIGH
**One-line statement:** Derive PSR_eff = l_P/(1 + k·ΔSSV) from Voronoi cell volume under SSV stress.
**Dependencies:** OPEN-SR-2 (k constant)
**Cross-sector connections:** Foundation of all SR quantitative predictions
**Paper(s):** SR-1
**Last updated:** 23 March 2026

---

### OPEN-SR-2: Derive k = l_P³/E_P from Voronoi Integral
**Status:** OPEN
**Sector(s):** SR
**Priority:** HIGH
**One-line statement:** Derive a single consistent k value from 600-cell Voronoi cell structure.
**Dependencies:** None blocking
**Cross-sector connections:** Blocks all SR quantitative predictions
**Current best lead:** Two inconsistent estimates exist; integral "in preparation."
**Paper(s):** SR-1
**Last updated:** 23 March 2026

---

### OPEN-SR-3: SSV Dimensional Definition
**Status:** OPEN
**Sector(s):** SR
**Priority:** HIGH
**One-line statement:** Provide unambiguous mathematical definition of SSV: type, units, relationship to DP Sea energy density.
**Dependencies:** None blocking (conceptual/definitional)
**Cross-sector connections:** Blocks all rigorous SR/GR derivations
**Current best lead:** Inconsistent usage across SR paper versions.
**Paper(s):** SR series
**Last updated:** 23 March 2026

---

### OPEN-SR-4: Full Einstein Field Equations from CPP
**Status:** OPEN
**Sector(s):** SR
**Priority:** HIGH
**One-line statement:** Prove CPP self-consistency condition equivalent to G_μν + Λg_μν = (8πG/c⁴)T_μν.
**Dependencies:** OPEN-SR-3 (SSV definition)
**Cross-sector connections:** GR programme
**Current best lead:** Weak-field GR derived rigorously; full nonlinear GR not yet proved.
**Paper(s):** GR companion
**Last updated:** 23 March 2026

---

### OPEN-SR-5: Cosmological Constant from Vacuum DP Sea
**Status:** OPEN
**Sector(s):** SR
**Priority:** MEDIUM
**One-line statement:** Same physical problem as OPEN-SM-6 from GR perspective.
**[DM-arc Sea-gravitation scope — added 31 May 2026, Patch 0705; elevates this stub to a scoped problem; status OPEN → OPEN (scoped).]** The DM arc (CONJ-COSMO-1) exposed that this is not just "the CC problem from the GR side" but the *shared* foundation of CPP's dark sector. Cross-link: **OPEN-COSMO-DM-1 (bidirectional)** — the DM Sea-gravitation requirement R2 is gated on this; see `series_phenomena/cosmology/dark_matter/R2_sea_gravitation_scoping.md`. A single CPP cosmological sector must yield, from ONE mechanism (not three assumptions): **(i)** uniform Sea mode → vacuum/Λ suppressed to ~observed magnitude with the suppression factor **derived** — NOT the inserted (l_P/R_H)² of the c08 dev-notes estimate, which is a Λ~1/R_H² coincidence-restatement (swings ~10× on horizon choice; `scripts/0705_lambda_sea_estimate.py`) and R_H(t)-dynamical ("why now"); **(ii)** Sea inhomogeneities (swirls) → unsuppressed local-gradient gravity of DM amplitude (c05: gravity = gradient of net SSV, so the uniform Sea is locally inert by construction; the swirl spectrum also sets the DM/baryon ratio, DM-arc R1); **(iii)** the Friedmann expansion history recovered (uniform matter/radiation gravitate cosmologically even though the uniform *Sea* mode is suppressed — a principled Sea-vacuum-mode vs matter-overdensity distinction). The prize: (i)+(ii) is a dark-energy↔dark-matter unification from one substrate. Hard prerequisite for DM Steps 4–5; likely warrants its own arc.
**Dependencies:** OPEN-SR-3
**Cross-sector connections:** OPEN-SM-6 (will be same theorem when solved)
**Paper(s):** GR companion
**Last updated:** 1 June 2026 (Patch 0720 — **COSMOLOGICAL SEA-GRAVITATION ARC OPENED**; sub-items 5a/5b/5c registered below; falsification-first sequence begun. Step A (5a) confronted → SURVIVES, Patch 0720; Step B (5c) delivered, Patch 0721. Work under `series_phenomena/cosmology/sea_gravitation/`.)

#### OPEN-SR-5a: Homogeneous-source / Friedmann reconciliation (Step A) — **SURVIVES (conceptual kill-gate cleared, Patch 0720)**
**Status:** ADDRESSED (conceptual; full Friedmann recovery = Step D, open). Gradient-sourced gravity (c05, F ∝ ∇(ΔSSV)) gives zero force for uniform density — but this is Seeliger's paradox, identical to Newtonian gravity (which c05/c07 establish CPP reduces to), resolved since Milne–McCrea (1934): the shell theorem (clean 1/r² + linear SSV superposition) makes a comoving sphere's dynamics depend only on interior mass → ä/a = −(4π/3)Gρ (matter-era Friedmann acceleration). "Uniform Sea locally inert" (zero absolute force at a point) and "uniform matter drives expansion" (nonzero *relative* deceleration) are the same fact two ways; no BBN/CMB conflict. The (l_P/R_H)² horizon factor is **relocated to Step C** (Λ suppression), not needed for expansion sourcing. See `sea_gravitation/stepA_homogeneous_source.md`; verify `scripts/0720_milne_mccrea_check.py`. Falsifier A1: if the CPP GR limit forces ground-state vacuum energy to gravitate at full density, the gradient-only picture breaks (tracked under 5c forward check).
**Last updated:** 1 June 2026 (Patch 0720)

#### OPEN-SR-5b: Derived Λ suppression (Step C) — OPEN
**Status:** OPEN. Replace the inserted (l_P/R_H)² of the c08 dev-notes estimate (coincidence-restatement; swings ~10× on horizon choice; R_H(t)-dynamical "why now") with a CPP-derived suppression factor; resolve the horizon ambiguity; target ~observed Λ as a derived output. Per Step B, Λ = the residual non-uniformity of the Sea ground state (NOT its full energy). Step-C hook: the mixed-Sea equilibrium (eDP<qDP<hTetra; bonding–debonding) sets the ground-state SSV level, which drifts as the Sea dilutes — a candidate horizon-tracking dynamical residual. **Do NOT register the c08 estimate as a result.**
**Cross-sector connections:** OPEN-SM-6 (will be same theorem when solved)
**Last updated:** 1 June 2026 (Patch 0720)

#### OPEN-SR-5c: Sea-vs-matter distinction (Step B) — **DELIVERED (structural, Patch 0721)**
**Status:** ADDRESSED (structural; magnitude = 5b/Step C). One mechanism, not three assumptions: CPP gravity couples to the SSV **excess** ΔSSV above the local Sea ground state (c05 gradient-sourcing), not to absolute energy density. So the uniform Sea — however Planck-scale its absolute density — sources zero gravity (no CC catastrophe); matter/radiation are localized excesses (ΔSSV>0) that gravitate and drive expansion; Sea swirls are excesses → DM; Λ is the tiny residual non-uniformity of the ground state. Matter, DM, and Λ all gravitate by the same mechanism, differing only in what the gradient is. **Load-bearing forward check (gates Step D):** does the CPP GR limit (c07/c08) correctly exclude ground-state vacuum energy from the gravitating part of T_μν while keeping the equivalence principle for excess energy? This is a departure from naive GR and the real place the arc can break (falsifier B1). See `sea_gravitation/stepB_sea_vs_matter.md`; verify `scripts/0721_gradient_source_distinction.py`.
**Last updated:** 1 June 2026 (Patch 0721)

---

### OPEN-SR-6: Big Bang from CP/GP Density Ratio
**Status:** OPEN
**Sector(s):** SR
**Priority:** MEDIUM
**One-line statement:** Derive initial expansion rate from CP/GP ratio at the initial Moment.
**Dependencies:** OPEN-SR-7 (GP exclusion)
**Cross-sector connections:** Cosmology series; Capotauro timing
**Paper(s):** GR companion
**Last updated:** 23 March 2026

---

### OPEN-SR-7: GP Exclusion Principle
**Status:** OPEN
**Sector(s):** SR
**Priority:** MEDIUM
**One-line statement:** Formalise the GP packing density limit and its consequences for extreme physics.
**Dependencies:** None blocking
**Cross-sector connections:** Black holes, Big Bang, CP superposition
**Paper(s):** GR companion
**Last updated:** 23 March 2026

---

### OPEN-SR-8: Equivalence Principle from SSV Geometry
**Status:** OPEN
**Sector(s):** SR
**Priority:** MEDIUM
**One-line statement:** Prove ΔSSV_kinetic(v) = ΔSSV_gravitational(Φ) when ½mv² = m|Φ|.
**Dependencies:** OPEN-SR-3
**Cross-sector connections:** Foundation of GR in CPP
**Paper(s):** SR-1, GR companion
**Last updated:** 23 March 2026

---

