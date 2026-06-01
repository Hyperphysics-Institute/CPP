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
**Last updated:** 1 June 2026 (Patch 0720 — **COSMOLOGICAL SEA-GRAVITATION ARC OPENED**; sub-items 5a/5b/5c registered below; falsification-first sequence begun. Step A (5a) confronted → SURVIVES, Patch 0720; Step B (5c) delivered, Patch 0721; Step C (5b) Λ-suppression PARTIAL — scaling+coefficient derived, dynamical w(z)/horizon-choice → Step D, Patch 0722; Step D (5d) CONDITIONAL CAPSTONE — A→D traversed NO KILL, Friedmann recovered, ground-state exclusion consistent, horizon resolved (event horizon); two conditions remain (c08 field equation; event-horizon selection), Patch 0723. Work under `series_phenomena/cosmology/sea_gravitation/`.)

#### OPEN-SR-5a: Homogeneous-source / Friedmann reconciliation (Step A) — **SURVIVES (conceptual kill-gate cleared, Patch 0720)**
**Status:** ADDRESSED (conceptual; full Friedmann recovery = Step D, open). Gradient-sourced gravity (c05, F ∝ ∇(ΔSSV)) gives zero force for uniform density — but this is Seeliger's paradox, identical to Newtonian gravity (which c05/c07 establish CPP reduces to), resolved since Milne–McCrea (1934): the shell theorem (clean 1/r² + linear SSV superposition) makes a comoving sphere's dynamics depend only on interior mass → ä/a = −(4π/3)Gρ (matter-era Friedmann acceleration). "Uniform Sea locally inert" (zero absolute force at a point) and "uniform matter drives expansion" (nonzero *relative* deceleration) are the same fact two ways; no BBN/CMB conflict. The (l_P/R_H)² horizon factor is **relocated to Step C** (Λ suppression), not needed for expansion sourcing. See `sea_gravitation/stepA_homogeneous_source.md`; verify `scripts/0720_milne_mccrea_check.py`. Falsifier A1: if the CPP GR limit forces ground-state vacuum energy to gravitate at full density, the gradient-only picture breaks (tracked under 5c forward check).
**Last updated:** 1 June 2026 (Patch 0720)

#### OPEN-SR-5b: Derived Λ suppression (Step C) — **PARTIAL (Patch 0722)**
**Status:** PARTIAL. The c08 inserted (l_P/R_H)² coincidence-restatement is **replaced** by a substrate mechanism. From Step B, the bulk Sea energy gravitates zero (no CC catastrophe); the only gravitating residual is the field energy of the largest SSV gradient the discrete (UV l_P), finite, causally-bounded (IR R_H) Sea cannot cancel — the horizon-scale mode. With amplitude Φ~c² (SSV↔PSR, SR-1/c05), coherence scale R_H=c/H (info at c per Absolute Moment), and field energy ρ=g²/8πG (c05/c07): **ρ_Λ ~ c⁴/(8πG R_H²) = c²H²/(8πG)**. Since E_P/l_P = c⁴/G exactly, this **= (1/8π)·ρ_P·(l_P/R_H)²** — so the (l_P/R_H)² scaling AND the 1/8π coefficient are DERIVED (not inserted), and the horizon is fixed (in principle) as the causal-coherence Hubble radius (c08 ~10× ambiguity removed). Numerically ρ_Λ^CPP = 2.56×10⁻¹⁰ J/m³ vs observed 5.3×10⁻¹⁰ (factor 2.07); Ω_Λ^CPP = 1/3. **Predicts dynamical Λ (ρ_Λ ∝ H²) → addresses "why now".** **OPEN (→ Step D):** the constant Ω~1/3 (Hubble-scale) conflicts with the observed decel→accel transition (Hsu 2004); the precise coefficient (factor ~2), the IR-scale choice (Hubble vs future event horizon, Li 2004), and w(z) need the full Friedmann dynamics. See `sea_gravitation/stepC_lambda_suppression.md`; verify `scripts/0722_lambda_residual_derivation.py`. Falsifier C1: if the CPP IR scale is the event horizon, the 1/8π coefficient and constant-Ω form shift (the scaling survives). **The c08 estimate is NOT registered as a result — it is replaced.**
**Cross-sector connections:** OPEN-SM-6 (will be same theorem when solved)
**Last updated:** 1 June 2026 (Patch 0722)

#### OPEN-SR-5c: Sea-vs-matter distinction (Step B) — **DELIVERED (structural, Patch 0721)**
**Status:** ADDRESSED (structural; magnitude = 5b/Step C). One mechanism, not three assumptions: CPP gravity couples to the SSV **excess** ΔSSV above the local Sea ground state (c05 gradient-sourcing), not to absolute energy density. So the uniform Sea — however Planck-scale its absolute density — sources zero gravity (no CC catastrophe); matter/radiation are localized excesses (ΔSSV>0) that gravitate and drive expansion; Sea swirls are excesses → DM; Λ is the tiny residual non-uniformity of the ground state. Matter, DM, and Λ all gravitate by the same mechanism, differing only in what the gradient is. **Load-bearing forward check (gates Step D):** does the CPP GR limit (c07/c08) correctly exclude ground-state vacuum energy from the gravitating part of T_μν while keeping the equivalence principle for excess energy? This is a departure from naive GR and the real place the arc can break (falsifier B1). See `sea_gravitation/stepB_sea_vs_matter.md`; verify `scripts/0721_gradient_source_distinction.py`.
**Last updated:** 1 June 2026 (Patch 0721)

#### OPEN-SR-5d: Friedmann recovery + the two load-bearing checks (Step D) — **CONDITIONAL CAPSTONE (Patch 0723)**
**Status:** CONDITIONAL — the falsification-first sequence A→D is **traversed with no kill**; the cosmological sector is structurally complete and consistent, resting on two named conditions. Three strands. **D1 (Friedmann recovery, PASS):** with the GR active mass ρ+3p/c² (c08's "LSP density AND flux"), excess-sourcing reproduces the standard radiation→matter→Λ history; q crosses zero (decel→accel) at z≈0.63 (observed ~0.6–0.7); the Planck ground state is NOT in the source sum. **D2 (ground-state exclusion, CONDITIONAL PASS):** the field-equation source is the LSP perturbation (mass-energy excess, c05 shell-broadcast), not the absolute Sea — so the uniform Sea is the medium, not a T_μν source, and does not de Sitter-expand (no CC catastrophe); a uniform |SSV|_abs is a constant g_tt = zero curvature; all tested GR (excess regimes) is reproduced; conservation is preserved (the covariantly-constant ground state subtracts without violating the Bianchi identity — the standard CC renormalization, physically motivated not tuned). **Condition:** rests on the c08 field-equation reduction G_μν=8πG/c⁴·T_μν[LSP], which c08 states is a **conjecture** ("the central challenge... not yet solved"). Falsifier D2-1: the closed field equation sources from absolute |SSV| → ground state gravitates → break. **D3 (horizon/w(z), RESOLVED + opens a refined question):** the dynamics rule out the Hubble radius (Ω_Λ const, Hsu 2004 — no accel) and **select the future event horizon** (Li 2004: w_Λ(now)≈−1.02, Ω_Λ evolves ~0→0.685→1, accelerates) — resolving Step C's ambiguity and fixing the coefficient (c≈0.8). Refined open question: WHY the CPP Sea coherence scale is the event horizon (its future-dependence is the known cost; not yet derived; falsifier D3-1). See `sea_gravitation/stepD_friedmann_and_checks.md`; verify `scripts/0723_friedmann_recovery.py`, `scripts/0723_horizon_wz.py`. **Two conditions remain (both derivation targets, neither a kill): the c08 field equation, and the event-horizon selection.**
**Last updated:** 1 June 2026 (Patch 0723)

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

