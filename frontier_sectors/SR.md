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
**Status:** OPEN — **arc opened (Patch 0729); Step 1 (scaling-phase kill-check) DONE: conditional no-go.** Reframed by the early-universe audit: GP spacing is fixed at l_P; CPP expands by DP-Sea occupancy DILUTION on a FIXED lattice scaffold (founders L33; Patch 0731), the initial Moment = the GP-exclusion-saturated state (near-100% occupancy), and OPEN-SR-6 is the law governing dilution from saturation. GP exclusion is EMERGENT from ZBW DP oscillation (P5 demoted axiom→theorem), not primitive. **[Step 1, Patch 0729 — does CPP early dynamics admit ANY scaling-symmetric/quasi-de-Sitter phase? CONDITIONAL NO (on Gate-1 excess-sourcing).** Within the recovered Step-D Friedmann framework: constant H needs a non-diluting source (w=−1); the only such CPP component (uniform Sea) is non-gravitating by excess-sourcing (c08 D2); the emergent ZBW DP-oscillation source is a fast-oscillating DILUTING medium (w∈[0,1/3]; reaching w=−1 needs a frozen field, the antithesis of the fastest mode in CPP) → comoving Hubble radius grows → modes enter, nothing freezes → no scale-invariant generation. ⇒ CONJ-COSMO-1 fails as a *primary structure-formation* model. **Residual escape — CLOSED Patch 0731:** the only escape was a non-Friedmann lattice-growth law, but CPP expands by DP-Sea dilution on a FIXED scaffold (no lattice-growth DOF; founders L33), and a hypothetical one fails on over-determination + Planck-rate/no-exit + mode-range/Gaussianity. See `lattice_growth_escape_closure.md`; verify `scripts/0731_lattice_growth_escape_closure.py` (12/12). **Next sub-step:** characterise the OPEN-SR-7 lattice-growth law and test for double-counting vs the Step-D Friedmann recovery (empties the escape → clean unconditional false on the structure role, or exhibits a self-consistent window → verdict reverts to open, proceed to Step 2). See `series_phenomena/cosmology/early_universe/step1_scaling_phase_kill.md`; verify `scripts/0729_scaling_phase_nogo.py` (19/19).]**
**Sector(s):** SR, COSMO
**Priority:** HIGH (gates the CONJ-COSMO-1 dark-matter verdict via OPEN-COSMO-DM-2)
**One-line statement:** Derive the initial expansion / lattice-growth law from the CP/GP packing ratio at the initial Moment; decide whether it admits a self-similar (constant-H) window (the DM-2 generation gate).
**Dependencies:** OPEN-SR-7 (GP exclusion); Gate 1 = c08 closed field equation (the Step-1 verdict is conditional on excess-sourcing)
**Cross-sector connections:** Cosmology series; Capotauro timing; **OPEN-COSMO-DM-2** (DM-2 generation barrier — OPEN-SR-6 is the shared hook); CONJ-COSMO-1
**Paper(s):** GR companion
**Last updated:** 1 June 2026 (Patch 0731 — Step-1 residual escape CLOSED; ZBW grounding; frontier collapses to Gate-1/c08)
**[Patch 0732 — Axiom H (the PSR-superposition inflation engine) evaluated:** a proposed new primitive for native inflation. Grounded against SR-1 (PSR_eff=l_P/(1+kΔSSV) ⇒ max PSR=l_P=c), it delivers de Sitter ONLY by allowing PSR>l_P (super-c traversal, ~12c in the toy), overriding the speed-of-light ceiling that underpins the SR/SM sector; the SR-1-consistent capped engine gives at most LINEAR expansion (H falls), and saturation-dilution caps e-folds at ln(occupancy)≪60. Third view of the 0729/0731 obstruction: a fixed-lattice, c-capped theory cannot stretch its metric super-luminally, which inflation requires. See `series_phenomena/cosmology/early_universe/axiom_h_inflation_engine_evaluation.md`; verify `scripts/0732_axiom_h_inflation_engine.py` (10/10).]**
**[Patch 0733 — CORRECTION: the 0732 super-c argument is WITHDRAWN.** It mis-read `l_P` as the lattice spacing; the corpus (c07 sub-Planck spacing; glossary `l_P`=unstressed baseline PSR; c01 ~10³⁰ GPs/Planck-length) establishes `l_P` = baseline PSR ≈ 10³⁰ sub-Planck GPs, so "one PSR/Moment" is fast but sub-luminal. 0729/0731/0732 all assumed a fixed present-day c; the inflation question is properly a Variable-Speed-of-Light question (epoch-dependent baseline PSR), now OPEN. Owed piece unchanged: the primordial spectrum (Gaussianity + scale-invariance), which VSL does not supply. SR-1 rederivation pass to pin the GP-spacing / baseline-PSR / PSR_eff three-level distinction is the agreed next program.]**
**[Patch 0736 — SR-1 rederivation Brick #2: Q1 (grid resolution) SETTLED CANONICALLY = the NESTED 600-CELL HIERARCHY.** Reconciles the two corpus readings by assigning them to two scales of one structure: COARSE (single-600-cell motif = l_P-scale tile, where R/a=φ, V₀, insphere→l_P, and k=l_P³/E_P live; l_P = per-Moment reach ceiling, c=l_P/t_P) and FINE (self-similar nesting to true GP spacing ~l_P/10³⁰ = the effective sub-Planck resolution, which supplies the velocity gradation l_P·(v/c) that the coarse step alone cannot represent — the load-bearing reason for the nested reading). VERIFIED: R/a=φ and k=l_P³/E_P are coarse-motif statements; the resolution choice enters NO prediction formula, so all five SR predictions + muon-bound are unchanged. Declared in new SR-1 §"Grid Resolution" (`sec:grid_resolution`); propagated to c01 (reach semantics), c02 (stiffness-integral scale), c07 (canonical cross-ref on its existing sub-Planck statement). NO THEO (semantics/grounding). Reasoning: `series_relativity/development/reasoning/0736_q1_canonical_resolution.md`. Q2 (fixed vs variable metric/VSL) remains OPEN → Brick #3.]**
**[Patch 0737 — SR-1 rederivation Brick #3: Q2 (metric variability) POSED as an explicit, testable fork** (`series_relativity/development/q2_metric_variability_fork.md`). Branch F (fixed-metric): c=l_P/t_P constant ⇒ first-moment infinity DISSOLVED (finite bare-600-cell ceiling, H-axiom unnecessary) BUT no native inflation (linear at c). Branch V (variable-metric/VSL): l_P = medium-set physical reach on the fixed graph (NOT graph growth, so NOT closed by 0731) ⇒ inflation route OPENS BUT first-moment infinity RETURNS (needs a regulator/floor or the H-axiom) and owes constant-H sustainability (0729 must be redone at variable c) + spectrum. **Anti-correlation is the crux:** the choice that kills the infinity forecloses inflation and vice-versa. Disambiguation introduced: l_P's two roles (timelike advance per Moment = invariant graph operation; spatial reach = medium-set, the thing that varies under V). **Empirical discriminant:** F predicts null Δc, V predicts bounded Δc → testable against varying-constants bounds (quasar-α, Oklo, atomic clocks, BBN, CMB). Present-epoch SR/SM predictions untouched under either branch. NO THEO (conditional posing). Reasoning: `series_relativity/development/reasoning/0737_q2_fork_posing.md`. Branch choice + first-moment story = Brick #4.]**
**[Patch 0738 — SR-1 rederivation Brick #4: BRANCH V ADOPTED + primordial-spectrum GATE PASSED (toy)** (`series_relativity/development/brick4_branch_v_adoption_and_toy_spec.md`). Construction = fixed UNIT `l_P_base` (preserves present-epoch anchoring: unboosted+baseline-SSV ⇒ l_P_eff=l_P_base, k=l_P_base³/E_P, five SR predictions intact) + variable PSR_base/c_eff (Branch V — fixing the unit is NOT Branch F) + finite-patch IC (~13 GPs; regulator+seed, kills the first-moment infinity without an axiom) + always-on H-engine (PSR_base ×(1+H) per superposed tick, graceful self-exit) + CLT-over-ZBW source (Gaussian statistics) + qCP/qDP morphology. **Reframe:** horizon solved by early high c_eff (no e-folds needed); inflation repurposed as the SPECTRUM generator. **Toy gate** (`scripts/0738_brick4_spectrum_gate.py`, all PASS): (A) additive ZBW exc-kurtosis −0.012 vs multiplicative ~1.6e5 — CLT decisively beats the 0730 cascade; (B) interlock (stationary CLT injection + constant-H freezing) gives n_s=1.000 flat, tunable to n_s≈0.965 via a modest end-roll-off, small f_NL — n_s−1=dlnσ²/dN confirmed analytically; (C) N_efold=(1/3)ln(N_CP/13) ⇒ observable-universe CP count ~1e80 → ~60 e-folds (depth sets total, H sets rate). **HONESTY:** PASS = capability+coherence, NOT a parameter-free n_s prediction (tilt roll-off + A_s remain tunings, as in standard inflation). H-axiom status: evaluated-not-adopted (0732) → adopted-as-working-engine, gate-passed-at-toy. NO THEO. Reasoning: `series_relativity/development/reasoning/0738_brick4_branch_v_gate.md`. Live debts: first-principles roll-off (n_s tuning→prediction), A_s, Δc bound (cheap filter, run first — could falsify density-dependent c_eff), flatness, reheating, degeneracy-pressure quantitative match (HIGH RISK; keep distinct from 0731 occupancy f→1).]**

---

### OPEN-SR-7: GP Exclusion Principle
**Status:** OPEN — **partial result (Patch 0729/0731): cosmological EoS + growth-law character pinned.** GP exclusion is EMERGENT from ZBW DP oscillation (P5 demoted axiom→theorem T-CPP-1), NOT a primitive packing axiom. The early substrate is a Sea of fast-oscillating bound DPs; by the virial result ⟨w⟩=(n−2)/(n+2) its EoS is **w∈[0,1/3]** (matter↔radiation), never near −1 (which needs a frozen field). **[Patch 0731 — the lattice-growth law is resolved at the cosmological level:** founders L33 grounds CPP expansion as DP-Sea occupancy dilution on a FIXED lattice scaffold (the lattice does NOT grow; 'CP/GP ratio' = occupancy fraction f, near-saturation at the Big Bang). So there is no independent lattice-growth DOF — the expansion rate is the Friedmann content-dilution — and the OPEN-SR-6/DM-2 residual escape is CLOSED. The micro-scale n_max (black-hole-interior near-100% occupancy) remains a separate quantitative target, no longer load-bearing for the DM structure verdict.]**
**Sector(s):** SR, COSMO
**Priority:** MEDIUM → HIGH (now load-bearing for the dark-matter structure-formation verdict)
**One-line statement:** Formalise the GP packing density limit and its consequences for extreme physics (black holes, Big Bang); derive the explicit lattice-growth law and saturation density n_max.
**Dependencies:** None blocking
**Cross-sector connections:** Black holes, Big Bang, CP superposition; **OPEN-SR-6 / OPEN-COSMO-DM-2** (the packing EoS feeds the early-universe scaling-phase question)
**Paper(s):** GR companion
**Last updated:** 1 June 2026 (Patch 0731 — GP exclusion confirmed emergent-from-ZBW, EoS w∈[0,1/3]; growth law grounded as DP-Sea dilution on a fixed scaffold; residual escape CLOSED)

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

