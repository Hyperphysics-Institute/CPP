<!--
  Extracted from Research_Frontier.md lines 1385-1578
  Source range: §2 Conjectures Under Investigation
  Extraction date: 2026-05-25
  Master dashboard: Research_Frontier.md
-->

# §2 — Conjectures Under Investigation (CONJ)

Proposed answers that exist but are not yet proved from CPP axioms.

---

### CONJ-EW-1: sin²θ_W = 3/(8φ) from 600-Cell Spectral Traces
**Status:** CONJECTURE — mechanism identified, independently validated; formal proof not written
**Sector(s):** EW
**Priority:** HIGHEST (gates CONJ-SM-6)
**One-line statement:** sin²θ_W = Tr(A²)/[φ(Tr(A²)+Tr(A³)/3)] = 3/(8φ) = 0.23176. PDG: 0.23121. Agreement: 0.24%, zero parameters.
**What a solution looks like:** Derive edge/face mode separation and 1/φ scale ratio from hDP bit-flow master equation + PSR formula.
**Dependencies:** OPEN-EW-3 (loop density)
**Current best lead:** Bare ratio 3/8 = E/(E+F) proved from spectral traces. φ correction from SSV/PSR scale separation (Grok). Dead end identified: g_E/g_F = 1/φ squared-coupling route gives 0.186, not 0.232. The 1/φ enters as linear prefactor, not squared ratio.
**Registered:** 1 April 2026

---

### CONJ-EW-2: sin²θ_W ≈ 3/13 = K₃ vertices/(z+1)
**Status:** CONJECTURE
**Sector(s):** EW
**Priority:** MEDIUM
**One-line statement:** Alternative formula: 3/13 = 0.23077; brackets PDG from below (CONJ-EW-1 from above). Agreement: 0.19%.
**What a solution looks like:** Determine if 3/13 is coincidence or distinct mechanism.
**Registered:** 1 April 2026

---

### CONJ-EW-W0: Neutral W Boson (W⁰) as Catalyst Substrate
**Status:** CONJECTURE — registered 9 May 2026 Session 41 architectural-revision conversation per `flagship_papers/electroweak/README.md`. Novel CPP particle prediction; not in Standard Model phenomenology.
**Sector(s):** EW, FP / SF-2
**Priority:** HIGH (gate to SF-2 v0.1 drafting; forced-choice prediction inclusion-criterion fit for SF-2)
**One-line statement:** A neutral massive boson with a 12-CP bracelet/open-configuration cage structure exists as the substrate upon which the W± charged states form when an electron (W⁻) or positron (W⁺) binds to it; the W⁰ functions as a catalyst in SM particle transformations.
**What a solution looks like:** Derive from CPP cage-stability primitives (a) the bracelet/open-configuration cage geometry as a stable 12-CP arrangement distinct from the Z's closed icosahedron, (b) the W⁰ mass prediction from cage-stability mechanics, (c) the bound-charge mechanism by which an electron/positron binds to the W⁰ to produce the W± states (the eCP/qCP hDP combination forming on the W⁰ substrate), and (d) the experimental signature distinguishing the W⁰ from existing SM channels — what collider data would show evidence of the W⁰ as distinct from W± direct production, and what kinematic signatures the catalyst-role would imply.
**Dependencies:** SM-1 (cage stability), CONJ-EW-1 / CONJ-EW-2 (Weinberg angle for EW-sector consistency), the cage-shape derivations underlying SF-2 (icosahedral Z, dodecahedral H, bracelet W⁰).
**Cross-sector connections:** SF-2 hosts the derivation. The W⁰ as catalyst-substrate may have implications for weak-interaction reaction rates and for the CKM/PMNS mixing-angle phenomenology (since the W⁰-substrate hypothesis says the W± transitions go through a W⁰ intermediary, potentially modifying transition matrix elements). Cross-checking against existing CKM/PMNS measurements is part of the experimental-signature derivation.
**Current best lead:** The 12-CP bracelet-shape conjecture is anchored in the same cage-shape taxonomy that produces the icosahedral Z (12-CP closed) and dodecahedral H (20-CP closed); the W⁰ would be the open/bracelet-shape complement at 12 CPs. Sub-shell-shape derivations during SF-2 pre-survey work will determine whether the bracelet shape derives as a stable cage or is excluded by cage-stability arguments. If excluded, CONJ-EW-W0 falsified at the substrate level; if derived, CONJ-EW-W0 advances.
**Falsification route:** (a) If cage-stability analysis at the 12-CP scale rules out the bracelet/open-configuration shape, CONJ-EW-W0 falsified. (b) If the bracelet shape is stable but the predicted W⁰ mass + experimental signature do not match any observable feature of existing collider data within reasonable mass ranges, CONJ-EW-W0 in tension with experiment. (c) If precision tests of W± production agree with SM (no W⁰-intermediary signature) at the precision currently achieved, CONJ-EW-W0 in tension; experimental-signature derivation should account for why direct W⁰ effects are not observed at current precision.
**Paper(s):** SF-2 (planned). Sub-derivation work to begin during SF-2 pre-survey session.
**Registered:** 9 May 2026 Session 41 architectural-revision (patch 0301).

---

### CONJ-SM-1: 30-Vertex Shell as Top Quark Fourth Cage
**Status:** CONJECTURE
**Sector(s):** SM, SS
**Priority:** HIGH
**One-line statement:** The d²=2 shell (30 vertices) is the top quark cage.
**Dependencies:** OPEN-SS-1 (mass formula using this shell must match PDG)
**Registered:** March 2026

---

### CONJ-SM-2: θ_Koide Is Determined by the Electroweak Sector
**Status:** CONJECTURE (supported by THEO-SM-5 structural impossibility + CONJ-SM-6 conditional theorem)
**Sector(s):** SM, EW
**Priority:** HIGH
**One-line statement:** The Koide phase θ cannot come from the lepton cage (K₃+SSV); it originates in the electroweak sector.
**Dependencies:** OPEN-SM-7d (Koide phase), CONJ-EW-1, EW series development
**Cross-sector connections:** CONJ-SM-6 (if CONJ-EW-1 proved, gives θ to 0.003%)
**Registered:** March 2026

---

### CONJ-SM-3: Neutrino Masses from σ = 120^{−d} Suppression
**Status:** CONJECTURE — supported by Session 41 partial closure work (see OPEN-FP-SF-4-1). The suppression mechanism originally posited as $\sigma = 120^{-d}$ has been refined at Session 41 to $\sigma = z^{-2 d_{\text{eff}}}$ with $z = 12$ and $d_{\text{eff}} = 5$ (equivalently $\sigma = 144^{-5} = z^{-10} \approx 1.62 \times 10^{-11}$, matching empirical target $1.59 \times 10^{-11}$ to within 2%); three candidate physical pictures converge on the per-channel $z^{-2}$ form. Substrate-connection insight (the 600-cell vertex count is structurally meaningful) preserved; specific $N_k = \{1, 4, 12\}$ bound-mode counts of original sketch superseded by Candidate-C cage-shell assignment. Theorem-level closure pending v0.1 SF-4 drafting.
**Sector(s):** SM, FP / SF-4
**Priority:** HIGH (now active via OPEN-FP-SF-4-1 work; was MEDIUM)
**One-line statement:** Derive Δm² and the absolute neutrino mass scale from 600-cell suppression formula. (Per Session 41 closure work, the formula refined to $\sigma = z^{-2 d_{\text{eff}}}$ with $d_{\text{eff}} = 5$ from {3 spatial + 1 ZBW phase + 1 orientation} channels.)
**Dependencies:** OPEN-FP-SF-4-1 (active closure work), SF-4 (target paper).
**Cross-sector connections:** OPEN-FP-SF-4-2 (K3-Cage-Shell Consistency Theorem) for K3-eigenstructure preservation; SM-5 PMNS derivation must continue to hold under the suppression structure.
**Registered:** March 2026 (original conjecture); active closure registered 9 May 2026 (Sessions 39-41, OPEN-FP-SF-4-1).

---

### CONJ-SM-4: m_u/m_e = φ³ Exactly
**Status:** CONJECTURE
**Sector(s):** SM, SS
**Priority:** MEDIUM
**One-line statement:** Quark-lepton baseline ratio from cage volume. Confirmed to 0.2% (PS-1).
**Dependencies:** OPEN-SS-1
**Registered:** March 2026

---

### CONJ-SM-5: TBM Corrections from Capotauro Bias
**Status:** CONJECTURE
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** θ₁₃ and 10% corrections to tribimaximal mixing arise from Capotauro.
**Dependencies:** OPEN-SM-4 (Capotauro formalisation)
**Registered:** March 2026

---

### CONJ-SM-6: Koide Phase from K₃ + EW + Bond Counting → CONDITIONAL THEOREM
**Status:** CONDITIONAL THEOREM — complete derivation contingent on CONJ-EW-1
**Sector(s):** SM, EW
**Priority:** HIGHEST
**One-line statement:** cos(θ_Koide) = −(2+ε)/3 where ε = 2sin²θ_W/(z+1) = 3/(52φ). θ = 132.731°; PDG: 132.732°. Match: 0.003%, zero parameters.
**What a solution looks like:** Prove CONJ-EW-1; the rest is proved.
**Dependencies:** CONJ-EW-1
**Current best lead:** Bond-counting derivation complete. Isotropic shift mechanism resolves the paradox (correction changes eigenvalue RATIO, not directions). Predicted masses: m_μ = 105.47 MeV (0.18%), m_τ = 1774.1 MeV (0.15%).
**Registered:** 1 April 2026

---

### CONJ-SM-7: Symmetric-Cage ↔ Trimaximal Flavor Correspondence
**Status:** CONJECTURE (leading structural hint for OPEN-FP-SF-4-FLAVORBASIS; not derived)
**Sector(s):** SM, FP/SF-4
**Priority:** MEDIUM (sub-hint of OPEN-FP-SF-4-FLAVORBASIS SC-2)
**One-line statement:** Under U_TBM, the most symmetric mass cage maps to the most symmetric flavor combination: the icosahedron (V=12, full I_h) ↔ the trimaximal state ν₂ = (νₑ+ν_μ+ν_τ)/√3; the V=30 cage ↔ the μ–τ antisymmetric, eDP-decoupled state ν₃ = (ν_μ−ν_τ)/√2; V=4 ↔ the eDP-weighted remainder ν₁ = (2νₑ−ν_μ−ν_τ)/√6.
**What a solution looks like:** Derive the substrate overlaps ⟨V=12 | eDP⟩ = ⟨V=12 | qDP⟩ = ⟨V=12 | hTetra⟩ = 1/√3 from the icosahedron's I_h symmetry, fixing the ν₂ column of U from geometry alone; extend to the full matrix.
**Dependencies:** OPEN-FP-SF-4-FLAVORBASIS (umbrella), SM-5 (TBM from K3), THEO-SF-4-5.
**Falsification route:** If the symmetry-derived overlaps do not reproduce the TBM column structure, the geometric correspondence is coincidental and SC-2 must proceed by the explicit S₃→S₂ branching route without the symmetry shortcut.
**Registered:** 30 May 2026 Session 149, Patch 0572a.

---

### CONJ-SM9-1: α = 7/3 from V² × V^(1/3)
**Status:** CONJECTURE (partially derived)
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** Scaling exponent from pair counting times linear cage dimension.
**Dependencies:** OPEN-SM-10-FEM (full rigorous derivation)
**Registered:** April 2026

---

### CONJ-SM9-2: EW Feedback ε ≈ α_geom/z²
**Status:** CONJECTURE
**Sector(s):** SM, EW
**One-line statement:** Correction to scaling exponent from electroweak sector (~0.003).
**Registered:** April 2026

---

### CONJ-SS-1: W₀ Bracelet Locally-Linear Coupling Face
**Status:** CONJECTURE
**Sector(s):** SS, EW
**One-line statement:** W bracelet presents tangent-line coupling to qCP, driving polarity inversion.
**Dependencies:** OPEN-SS-12
**Registered:** 29 March 2026

---

### CONJ-SS-2: Universal qCP Polarity Switching
**Status:** CONJECTURE — observed universally across all known decay pathways
**Sector(s):** SS, EW
**One-line statement:** Every quark flavor transition involves qCP polarity inversion. No exception found.
**Dependencies:** OPEN-SS-12 (formal proof)
**Registered:** 29 March 2026

---

### CONJ-SS-2-1: String Tension σ = M₀zπ/(φ l_edge)
**Status:** CONJECTURE
**Sector(s):** SS
**One-line statement:** Physically motivated formula (z bonds × π orbit × 1/φ attenuation) giving σ = 243 MeV/fm.
**Dependencies:** OPEN-SS-5
**Registered:** March 2026

---

### CONJ-SS-10: Deuteron Binding Energy $B_d = M_0/\varphi$
**Status:** SUPERSEDED by CONJ-SS-11 (SS-5 v0.2, 17 April 2026). The v0.1 formula $B_d = M_0/\varphi = 2.343$ MeV is recovered as the $A=2$ special case of the cascade formula. Retained in registry for provenance.
**Sector(s):** SS (nuclear physics)
**One-line statement:** Deuteron binding from a single open-vertex bond (v0.1 mechanism). Superseded by the base-to-base three-chain K$_3$-reduced mechanism in v0.2.
**Paper(s):** SS-5 v0.1 (16 April 2026) — superseded
**Registered:** 16 April 2026
**Superseded:** 17 April 2026

---

### CONJ-SS-11: Light-Nuclei Cascade Binding Formula
**Status:** CONJECTURE — central claim of SS-5 v0.2
**Sector(s):** SS (nuclear physics)
**One-line statement:** $B(A,Z) = (A{-}1) n_{np} (M_0/\varphi) - n_{pp} \alpha_{em}\hbar c/(1.2 A^{1/3}) - (n_{pp}+n_{nn}) M_0/\varphi^3 + \delta_{A,4} M_0/\varphi$ reproduces the binding energies of $d$, $^3$H, $^3$He, $^4$He at $\leq 5.3\%$ error with zero fitted parameters.
**Mechanism:** Base-to-base nucleon configuration with three qq DP chains across the contact face, K$_3$-reduced to one collective pair quantum $B_{\text{pair}} = M_0/\varphi$. Cascade factor $(A-1)$ multiplies each pair by the number of closed-polytope completions. Pauli penalty $M_0/\varphi^3$ per like-nucleon pair. Closure bonus $M_0/\varphi$ activated at $A=4$ (tetrahedral polytope).
**Dependencies:** SS-2 (nucleon structure), SM-8 ($M_0$), SS-3 (K$_3$ collective-mode template), CONJ-SS-11 itself registers the $(A-1)$ multiplicity and the Pauli coefficient as working conjectures requiring rigorous derivation (see OPEN-SS-19).
**Cross-sector connections:** OPEN-SS-18 (heavy-nuclei alpha-cluster regime); OPEN-SS-16 (Layer B closure).
**Current best lead:** Numerical verification across $d$ ($+5.3\%$), $^3$H ($-0.09\%$), $^3$He ($-1.0\%$), $^4$He ($-1.4\%$), and qualitative unboundness of $^5$He, $^5$Li, $^8$Be (all confirmed empirically, including the 92 keV near-threshold of $^8$Be).
**Falsification route:** Independent verification of the $(A-1)$ multiplicity (currently motivated by closed-polytope completion counting but not rigorously derived); alternative Pauli coefficients $M_0/\varphi^2$ or $M_0/\varphi^4$ would shift predictions out of band.
**Paper(s):** SS-5 v0.2 (17 April 2026)
**Registered:** 17 April 2026

---

### CONJ-P-SS-1: ZBW Orbital Frequency Ratio (CORRECTED — formerly "2:1")
**Status:** RECOVERED + CORRECTED — the "2× frequency" statement is **superseded as recorded**. The original derivation has been located (chat ee212abb, 19 Mar 2026; recovered to `series_strong/papers/recovery-SS-1-spin-zbw-frequency.md`, Patch 0572b) and it gives a **radius ratio of 2** and an **angular-frequency ratio of 2√2**, NOT a frequency ratio of 2. Registered as **THEO-SPIN-1** (v1.1, multi-AI confirmed 3/3, Patch 0572f).
**Sector(s):** SS, QM
**One-line statement (CORRECTED):** A captured DP at Mode-2 standing-wave nodes has r_out/r_in = 2 (exact). Under 1/r² force balance (ω² ∝ 1/r³) this gives inner/outer orbital angular-frequency ratio ω_in/ω_out = (r_out/r_in)^(3/2) = 2√2 ≈ 2.828 (exact). Spin-½ follows universally from {1/r² force, r_out = 2 r_in, L = ℏ/2}. The inner radial ZBW runs at the Compton frequency ν_C = m_e c²/ℏ and phase-locks the orbits.
**The "2:1" error:** the earlier statement (Grok-origin, Sonnet-confirmed; entered as a working convention) conflated the **radius** ratio (2) with a **frequency** ratio. A frequency ratio of exactly 2 requires equal orbital speeds (v_in = v_out), which is not force-balanced — the derivation gives v_in/v_out = √2.
**Current best lead → RESOLVED as THEO-SPIN-1 (v1.1, confirmed 3/3, Patch 0572f).** The recovered derivation is registered as THEO-SPIN-1 and multi-AI confirmed (Grok CONFIRM; Copilot CONFIRM-WITH-CALIBRATION; ChatGPT RESTATE-TO-v1.1). Scope per the v1.1 restatement: the theorem establishes the force-balanced captured-DP geometry *compatible with* the spin-½ condition and corrects ω_in/ω_out from 2 to 2√2, but does **NOT derive spin-½** (L = ℏ/2 is an imposed input), the inner-radial-ZBW phase-lock is a **foundational model postulate**, and universality across fermion types + photon is a **template**. The foundational input reviewers pressed: the two-poles-at-different-ω picture held from winding by the ZBW phase-lock. See `series_strong/papers/review/reviews-THEO-SPIN-1.md`.
**Downstream impact:** SF-4 uses only the phase-*lock* (Picture A channel-merge → d_eff = 5), not the numeric value, so σ_ν = z⁻¹⁰ is unaffected; only SF-4's "2:1 frequency" wording is corrected to "phase-locked, ratio 2√2" at v1.1 (Patch 0572c). Picture B (not selected) depended on the literal value 2; the correction strengthens the Picture-A-over-B argument.
**Registered:** 29 March 2026 (as "2:1 proposed postulate"). **Recovered + corrected:** 30 May 2026 Session 149, Patch 0572b.

---

### SC-6: φ¹¹ and φ¹⁷ Lepton Mass Ratio Exponents
**Status:** CONJECTURE (empirical observation)
**Sector(s):** SM
**One-line statement:** m_μ/m_e ≈ φ¹¹ (3.8%), m_τ/m_e ≈ φ¹⁷ (2.7%). Exponents: 11 = z−1, 17 = z+5.
**Dependencies:** Geometric derivation from coordination structure
**Registered:** 24 March 2026

---

### CONJ-CHIR-1: The Substrate Chiral-Vacuum Transition Is Electroweak Symmetry Breaking
**Status:** CONJECTURE — registered 30 May 2026 (Session 150 Patch 0662) at the opening of the CHIR ↔ electroweak bridge (`chirality_derivations/sketches/chir_ew_bridge_scoping.md`). Proposed cross-sector identification; not proved from CPP axioms.
**Sector(s):** CHIR, EW, SM
**Priority:** HIGH (the grand-unification route for the chirality primitive/emergent-status headline; co-owned with OPEN-SM-4)
**One-line statement:** The substrate chiral-vacuum transition (STATUS-2's H₄ → H₄⁺, an index-2 ℤ₂ quotient with order parameter `sign(n̂)` = FI-C-9) is the Capotauro chirality-activation event of OPEN-SM-4 (registered as [600-cell] × ℤ₂ → [600-cell]), and this event is electroweak symmetry breaking — so FI-C-9 is the substrate face of EW parity violation (P-face), `sign(δ)` is the substrate face of SM CP/T-violation (T-face; one structure by CPT, TARROW-1), and the magnitude χ = φ⁻³ sets δ_CP (≈193–195°) and Δp_LR (= χ/6 ≈ 0.0394).
**What a solution looks like:** show the STATUS-2 ℤ₂ and the OPEN-SM-4 ℤ₂ are the same reflection (the §4.3 ℤ₂-match), then derive δ_CP and Δp_LR from χ = φ⁻³ (= FI-C-9) via OPEN-SM-4 sub-claims (a)/(b). If established, chirality is **fully emergent (V2/W2) via the SM** (both substrate primitives reabsorbed); the headline status question is answered at its deepest level.
**Dependencies:** STATUS-2 (the H₄→H₄⁺ ℤ₂), TARROW-1 (the CPT P-face/T-face unification, assumes substrate CPT-invariance), CHI-1 (χ = φ⁻³ = FI-C-9), CAP-1 / OPEN-SM-4 sub-claim (c) (Δp_LR = χ/6, shipped); the deep engine 1d-β-ii / OPEN-SM-4 sub-claims (a)/(b) behind F.1 §14.17.
**Cross-sector connections:** OPEN-CHIR-3 ∪ 1d-β-v (the bridge, CHIR side); OPEN-SM-4 (the bridge, SM/SR side; the chirality-activation event + δ_CP); OPEN-FI-C-9-FP-MECHANISM (Reading-C `n̂`, sub-claim (b)); audit E26 (SM parity link).
**Falsification routes:** (a) the STATUS-2 ℤ₂ and the OPEN-SM-4 ℤ₂ are structurally distinct (the ℤ₂-match fails); (b) χ = φ⁻³ does not set δ_CP / Δp_LR once OPEN-SM-4 (a)/(b) are derived; (c) substrate CPT-invariance fails (severs the P-face/T-face unification — TARROW-1 falsifier T5).
**Registered:** 30 May 2026 (Patch 0662)

---

### OPEN-COSMO-DM-1: Tetra-Gravity Dark-Matter Derivation (umbrella work item)
**Status:** OPEN — umbrella work item opened 31 May 2026 (Session 149, Patch 0700) at the opening of the tetra-gravity dark-matter arc. Far-frontier; gated. Co-located here in CONJ.md pending a dedicated `frontier_sectors/COSMO.md` split (deferred until the arc grows past registration).
**Sector(s):** COSMO, SR, SS, SM
**Priority:** MEDIUM (far-frontier; the stated publication target of the arc, but gated behind the falsification sequence below)
**[Patch 1103 — R2 ↔ CC umbrella pointer.** The R2 sea-gravitation gate (Step 2 below; `series_phenomena/cosmology/dark_matter/R2_sea_gravitation_scoping.md`) is the DM end of the cosmological-constant reconciliation now run by the CC umbrella (`series_umbrella/series_cosmological_constant_arc/`, Patch 1101): the same excess-sourcing that suppresses the uniform-Sea vacuum (SR-5, dynamical) delivers R2's uniform-Sea-inert / swirls-gravitate split. The umbrella records that R2's uniform-Sea-inert half is essentially in hand (SR-5 Steps A–D; DM-1 manuscript 0844), conditional on the c08 closed field equation. The R2 file's stale "unbuilt sector" framing (Patch 0705, pre-Steps-A–D) is owed an update **in the DM lane**; not edited from the CC window. Pointer only; no verdict moved.]**

**[Patch 1117 — the op:einstein (a) cap on R2/CC resolves to a NECESSARY spin-bit axiom.** Per the `op_einstein_closure` arc (1107–1116): the excess-sourcing / uniform-Sea-inert half (b/b′) is conditionally closed (600-cell symmetry, 1108); the nonlinear GR-recovery (a) — the spin-2 tensor-GW sector — is open and now shown to require a **fundamental rank-2 d.o.f.**: the emergent-graviton calculation (1116) yields helicity {0,0,±1} only from the scalar+vector substrate, no spin-2 for any couplings. R2's uniform-Sea-inert leg is unaffected; the full GR-recovery requires the spin-bit axiom. See `series_relativity/op_einstein_closure/`. No verdict moved.]**
**One-line statement:** Establish, by a hard-ordered falsification-first sequence, whether net-neutral concentrations of qDP + hTetra (seeded by early-universe radial-expansion "swirls") behave as cold collisionless dark matter under CPP's SSV-gravity mechanism.
**Closure plan (falsification-first; no paper/anthology framing until Steps 1 AND 2 are computed and survive):**
- Step 0 — confirm the c05/c07 weak-field Newtonian force law (F = G m m'/r²) superposes cleanly to a diffuse, extended, low-density galactic-halo mass distribution and yields v²(r) = G M(r)/r for collisionless test-mass orbits (audit, not a new derivation; see TODO-014 on the G-scale framing caveat).
- Step 1 — Gate 1 quantitative (CHEAPEST KILL): short-range bonding momentum-transfer cross-section integrated over halo-density encounter rates; show σ/m ≲ ~1 cm²/g (SIDM bound). **[Patch 0703 — DONE, NO KILL.** Order-of-magnitude: σ/m ≈ 4×10⁻³ cm²/g (qDP, light/worst-case) to 8×10⁻⁴ (hTetra), ~250–1250× below the bound; ~0.02 collisions/particle/Hubble time; survives even ×100 nucleon-like resonant enhancement. **Gate-1 closure now reduces to: bound the residual qDP/hTetra scattering length (rule out a ×~10³ near-threshold resonance in the light channel) + pin the constituent mass.** See `series_phenomena/cosmology/dark_matter/step1_sigma_over_m_SIDM.md`.]
- Step 2 — bookkeeping (SECOND KILL): free qDP/hTetra vs qDP/hTetra already bound into baryons; the free population must be ~5× baryonic mass without double-counting the hybrid-tetrahedral content of nucleons. **[Patch 0704 — DONE. NO kill, NO clean pass.** Abundance is not the constraint (Sea reservoir ρ_Sea ~3×10¹⁹ kg/m³ ~10²× nuclear; swirl overdensity for all DM δ~7×10⁻⁴⁷). Double-counting is a ~19% effect, cleanly avoidable. The ~5:1 ratio is **not derived** — it is the free primordial swirl amplitude, relocating ΛCDM's coincidence (§6c: "relative abundances are empirical questions"). **Real open requirement (R2): the uniform Sea must NOT gravitate cosmologically (else Ω_Sea~10⁴⁵–10¹²⁰, vacuum catastrophe) while its swirl-inhomogeneities do — GATED on OPEN-SR-5 (cosmological constant). Cross-link OPEN-COSMO-DM-1 ↔ OPEN-SR-5.** See `series_phenomena/cosmology/dark_matter/step2_bookkeeping.md`.] **[R2 SCOPED, Patch 0705 — NOT a kill; raises the ceiling. c05 gravity is gradient-sourced (uniform Sea locally inert by construction); the c08 dev-notes estimate that the uniform Sea = Λ opens a dark-energy↔dark-matter unification (same Sea: uniform mode → suppressed Λ, inhomogeneities → DM). BUT that Λ estimate's (l_P/R_H)² suppression is a coincidence-restatement (swings ~10× on horizon choice), not derived. Requirement now lives in OPEN-SR-5 (elevated to scoped): one mechanism yielding suppressed-Λ + unsuppressed-inhomogeneity-gravity + Friedmann. Hard prerequisite for Steps 4–5. See `series_phenomena/cosmology/dark_matter/R2_sea_gravitation_scoping.md`.]
- Step 3 — coldness (velocity dispersion at decoupling). Step 4 — power spectrum from "swirl" seeds. Step 5 — quantitative halo/rotation curve (ρ∝1/r² or NFW). **[Step 3 — Patch 0706, DONE: SURVIVES (cold by a wide margin) — qDP/hTetra at ~0.3–1.5 GeV are ~10⁵–10⁶× above the ~3 keV warm-DM bound, non-relativistic since the QCD era, v/c~10⁻⁴–10⁻⁵ by matter-radiation equality; rests only on the GeV mass scale, not on OPEN-SR-5. See `step3_coldness.md`.] [OPEN-SR-5 UPDATE, Patch 0723: the cosmological sector arc A→D is traversed with NO KILL (conditional capstone) — Steps 4 & 5 are UNBLOCKED (conditionally). **[Step 5 — Patch 0724, DONE: PASS (representative galaxy).** c05's zero-parameter force law (G=ℏc/m_P²) + a collisionless qDP/hTetra halo give an approximately flat rotation curve (~220 km/s, v(solar)=214), baryons-only declines Keplerian, M_halo/M_baryon≈4.5 (matches ~5:1 + Step-2 reservoir). **c08 exposure LOW** — rides on c05 *local* gravity, NOT the cosmological field equation (the earlier "rotation curve needs the cosmological-scale force law" framing was too pessimistic; the local Newtonian limit suffices). **HONEST:** flat curves are GENERIC to any collisionless halo — not CPP-discriminating; CPP content = derived G + no-new-sector halo + Steps 1-3 consistency. The discriminating test (derive ρ(r) from swirl dynamics; predict Tully-Fisher/core sizes) is NOT done and overlaps Step 4. See `step5_rotation_curve.md`; verify `scripts/0724_rotation_curve.py`.]** Only **Step 4 (power spectrum)** remains — the harder, most c08-exposed (needs the conditional cosmological background), most discriminating step.]** **[Step 4 — Patch 0725, DONE: SERIOUS TENSION (NOT pass, NOT clean kill) — the arc's weakest link.** Split: (Q1 growth) given near-scale-invariant adiabatic seeds, CPP inherits the standard transfer/growth and reproduces P(k) (BBKS turnover at k_eq, slopes k^n_s→k^(n_s-4)) — fine, conditional on Step D. (Q2 seed origin) the swirl mechanism is prima facie CAUSAL/active-source → hits the wall that killed cosmic-string/defect models: cannot make the observed super-horizon adiabatic correlations (horizon at recombination subtends ℓ_H~157, yet the SW plateau ℓ~2-50 and the TE anti-peak ℓ~100-150 are super-horizon — the textbook acausal signature), and gives incoherent/smeared acoustic peaks. **LIVE ESCAPE (why not a clean kill):** CPP's atemporal Nexus enforces non-local coordination independent of light-cones → could seed acausal/super-horizon correlations (a horizon-problem resolution active-source models lack) — but it is undeveloped, CPP-flagged as "lacking physical grounding," and must be shown to yield n_s~0.96 adiabatic specifically. **VERDICT: CPP does NOT reproduce the observed power spectrum; CONJ-COSMO-1 is NOT confirmed; structure formation is its dominant open problem.** Registered OPEN-COSMO-DM-2. See `step4_power_spectrum.md`; verify `scripts/0725_power_spectrum.py`.]**
**Dependencies:** Gravity foundation already built — c05 (Newtonian, G = ℏc/m_P²) + c07 (weak-field GR). No OPEN-GRAV-SSV-GR-EXTENSION prerequisite is required (this supersedes the founders_vision §6c lines 924/928 deferral; see Patch 0701). CONJ-DPS-1/2/3 supply the population microphysics.
**Cross-sector connections:** CONJ-COSMO-1 (the conjecture this work item tests); CONJ-DPS-1/2/3; CONJ-SS-1 (W₀ bracelet, via CONJ-DPS-3).
**Falsification routes:** any of Steps 1–5 failing; in particular Step 1 (σ/m above SIDM bound → at best collisional/SIDM, not cold collisionless) or Step 2 (free population cannot reach ~5:1 without double-counting).
**Source of record:** `founders_vision.md` Part V §6c (Patch 0672a). **Working home:** `series_phenomena/cosmology/dark_matter/`. **Arc handover:** `handovers/2026-05-31_session_149_tetra_gravity_dark_matter_arc_kickoff.md`.
**Registered:** 31 May 2026 (Patch 0700)

---

### OPEN-COSMO-DM-2: Acausal Seed / Scale-Invariance Origin (the structure-formation problem)
**Status:** SUBSTANTIALLY RESOLVED (Patch 2004; arc 2001–2005) — *superseding the original OPEN verdict, preserved below.* The structure-formation barrier decomposes into Q1 (growth→P(k)) and Q2 (seed origin). Q1 was always inherited (Step 4, given seeds); Q2 was the only barrier, and at 0725 its sole candidate (causal swirl seeds) failed the cosmic-string wall. The **EU-1 arc (0738–0785) resolved Q2 by a route that postdates this entry**: VSL horizon (0738; Δc-filter 0739 → "not falsified, reduced to a decidable μ↔ε symmetry") + ZBW-stack δN spectrum → n_s=0.9649 = PRED-C-96 = shipped paper EU-1 v1.0. The Step-1 no-de-Sitter result (0729) is *not contradicted* — CPP solves the horizon by VSL, not de Sitter. Residual ledger: **R1** (explicit P(k)) DONE — Patch 2001 computes CPP's P(k) from EU-1's own spectrum (turnover/slopes/tilt reproduced, σ₈ O(1)); **R2** (VSL μ↔ε falsifier) PASS-conditional on the single-oscillator structure — Patch 2002 (Z₀ geometric via the harmonic virial mechanism; clean-kill exposure removed); **R3** (A_s) adopted, parity with inflation, reduced to the posited H-axiom boost coupling κ (target ~2×10⁻⁷), Poisson route excluded — Patches 2003/2004; **R4** (OPEN-EU-1 derivation depth) unchanged. None of R1–R4 is a live framework threat. **[Patch 2046 — R2 current state (refreshing the stale "single-oscillator / Patch 2002" line above): R2 is now at **conditional-PASS at the audited LSP field-content level**, panel-confirmed (ChatGPT, corrected re-dispatch) — (i) VTD-1 cleared at SR-1 strength (2037/2038), (ii) f(C,Σ) closed at field-content level (2028 scalar channel / 2029 ~11-order locality / 2030–2031 no-rank-2, + A3′ OB-3 static-null theorem). Unconditional PASS remains gated on **OPEN-SR-9** (the from-substrate optical computation, which currently leans FAIL — see R2-STATUS.md + the OPEN-SR-9 handover). Canonical ladder: `series_relativity/development/mu_eps_closure/R2-STATUS.md` (Updates 2025→2041).]** See `series_phenomena/cosmology/dark_matter/pk_closure/`, `series_relativity/development/mu_eps_closure/`, `series_phenomena/cosmology/early_universe/as_amplitude_closure/`, and `handovers/2026-06-21_session_*_open_cosmo_dm2_arc_close.md`. *Historical record (original verdict) preserved:* **Status:** OPEN — registered 1 June 2026 (Patch 0725). **[Step 1 (the cheapest kill) DONE — Patch 0729: CONDITIONAL NO-GO on the generation half.** Pursuing OPEN-SR-7 (the GP-exclusion EoS) inside the recovered Step-D Friedmann framework: constant-H (scale-invariant generation) needs a non-diluting source (w=−1); CPP's only such component (uniform Sea) is non-gravitating by excess-sourcing (Gate 1); the emergent ZBW DP-oscillation source is a fast-oscillating DILUTING medium (w∈[0,1/3]; w=−1 needs a frozen field, the antithesis of the fastest mode in CPP) → comoving Hubble radius GROWS → no mode freezing → no scale-invariant spectrum generated. So CPP early dynamics admits NO scaling/quasi-de-Sitter phase, **conditional on Gate 1**. The Nexus (correlation half) cannot supply generation; this kills the generation half. **Residual escape — CLOSED Patch 0731:** CPP expands by DP-Sea dilution on a FIXED lattice scaffold (no lattice-growth DOF; founders L33); a hypothetical intrinsic growth law fails on over-determination + Planck-rate/no-exit + mode-range/Gaussianity. The verdict-moving frontier collapses to Gate-1/c08 alone. See `series_phenomena/cosmology/early_universe/step1_scaling_phase_kill.md`; verify `scripts/0729_scaling_phase_nogo.py` (19/19).]** The dominant open problem for CONJ-COSMO-1, surfaced by Step 4. **The requirement:** a CPP mechanism that produces a near-scale-invariant (n_s ≈ 0.965), adiabatic, super-horizon-coherent primordial perturbation spectrum with amplitude A_s ≈ 2.1×10⁻⁹ — i.e. what inflation supplies in ΛCDM. **Why it's hard:** the swirl-seed mechanism is causal/active-source, and causal seeds generically fail the two cleanest discriminators — they cannot produce the observed super-horizon adiabatic correlations (the Sachs-Wolfe plateau; the TE anti-peak at ℓ~100-150, with the horizon at recombination only reaching ℓ_H~157) and they give incoherent/smeared acoustic peaks rather than the observed harmonic series. This is the same wall that ruled out cosmic-string/defect models as the primary structure source.
**Candidate handle (CPP-native, undeveloped):** the **atemporal Nexus** — non-local coordination of all CPs independent of light-cones at each absolute Moment — could in principle seed acausal/super-horizon correlations, resolving the horizon problem without inflation. Must be (a) developed into a derived perturbation spectrum, (b) shown to be scale-invariant + adiabatic, (c) reconciled with CPP's own note that the Nexus "lacks physical grounding."
**Decomposition (sharpening, Patch 0726) — the Nexus is at most HALF an answer:** the problem splits into two separable halves. (1) **Horizon/correlation** (why super-horizon regions are correlated): the Nexus is a *candidate* (non-local coordination → super-horizon correlation without inflation) — though even this is unshown, since the Nexus conserves DI-bit/CP state and that it yields the observed thermal uniformity is not established. (2) **Perturbation generation + scale-invariance** (what *generates* the 10⁻⁵ departures, and why equal power per log-interval): **the Nexus does NOT address this** — coordination is not fluctuation-generation. The swirls were the intended generator but are causal (Step 4 fail). Inflation supplies generation+scale-invariance via inflaton quantum fluctuations stretched in a de-Sitter (scaling-symmetric) phase; **CPP has no analog**. **THE REAL BARRIER IS HALF (2), NOT HALF (1).** A CPP route likely needs an early de-Sitter-like / scaling-symmetric phase — candidate hook: OPEN-SR-6 (Big Bang from CP/GP density ratio) — undeveloped. Until then CONJ-COSMO-1 is at best a DM *microphysics* candidate that does not account for the origin of structure.
**Sector(s):** COSMO, SR · **Priority:** HIGH (gates CONJ-COSMO-1 confirmation).
**Cross-sector connections:** CONJ-COSMO-1 (this is its weakest link); OPEN-SR-6 (Big Bang from CP/GP density ratio — likely the shared origin of any CPP early-universe perturbation mechanism); CONJ-COSMO-3 (qCP-chain cosmic web — the morphology/processing picture conditional on this generation problem; Patch 0730); the horizon problem generally. **Generation-vs-processing analysis + the three owed pieces:** `series_phenomena/cosmology/early_universe/cosmic_web_generation_constraints.md`.
**Falsification routes:** if the Nexus cannot yield a scale-invariant adiabatic super-horizon spectrum (or yields isocurvature / non-scale-invariant), CONJ-COSMO-1 fails as a primary structure-formation model and the swirl seeds are at best a sub-dominant DM-only component.
**Source of record:** `series_phenomena/cosmology/dark_matter/step4_power_spectrum.md` (+ reasoning/0725). 
**Registered:** 1 June 2026 (Patch 0725)

---

### CONJ-DPS-1: DP-Sea Skew + eDP:qDP 1:1 Conservation Lock + Color-Screening Driver
**Status:** CONJECTURE — registered 31 May 2026 (Session 149, Patch 0700). NEW sector prefix DPS (Dipole-Sea population). Near-frontier (internally checkable).
**Sector(s):** DPS, SS, SM
**Priority:** MEDIUM
**One-line statement:** As the post–Big-Bang substrate cools, the qCP–qCP/color binding channel (in addition to the electric channel) skews DP formation toward the doubly-bound qDP; with equal initial {±eCP, ±qCP} inventories and near-total pairing, charge conservation forces n(eDP) = n(qDP) exactly (eDP as the conservation echo of the qDP skew) and n(hDP-A) = n(hDP-B) = N − n(qDP); the likely driver is the unscreened color attribute of the lone qCP in a hybrid carrying a large standing energy penalty.
**Dependencies:** Load-bearing — the qCP–qCP force is attractive in the +qCP/−qCP configuration (deepens the qDP well rather than fighting electric binding); equal initial eCP:qCP inventory + roughly symmetric skimming into fermion cores (the 1:1 lock also tests this creation symmetry). Driver mechanism leans on color confinement at CP level (c15).
**Cross-sector connections:** c14 (qDP chaining), c15 (SU(3) color from 600-cell — the skew driver + the sign of the qCP–qCP force); CONJ-DPS-2; CONJ-SS-2 (qCP polarity switching).
**Falsification routes:** (a) the qCP–qCP force is repulsive or negligible in the relevant configuration (skew collapses); (b) measured/derived eDP:qDP departs materially from 1:1 (creation asymmetry or asymmetric skimming); (c) color is screened in the hybrid (no standing energy penalty → no hard skew).
**Source of record:** `founders_vision.md` §6c (Opus scope notes "conservation lock" + "color screening as likely driver").
**Registered:** 31 May 2026 (Patch 0700)

---

### CONJ-DPS-2: hTetra Sink + Freeze-Out Ordering + hTetra Binding > 2× hDP
**Status:** CONJECTURE — registered 31 May 2026 (Session 149, Patch 0700). Near-frontier.
**Sector(s):** DPS, SS, SM
**Priority:** MEDIUM
**One-line statement:** hDP-A and hDP-B are consumed into Hybrid Tetrahedra (hTetra) — the cornerstone of the charm quark, muon, tau-neutrino frame, and baryons — rather than suppressed to extinction; "scarce free hDPs + available hTetras" falls out without fine-tuning iff the hTetra is a deeper well than its parts (super-additive tetrahedral closure: hTetra binding > 2× hDP binding), with the universe selected by the hDP→hTetra freeze-out ordering (hTetra-above / together / hTetra-below give materially different relic populations).
**Dependencies:** The binding inequality hTetra > 2× hDP; the 1:1 lock (CONJ-DPS-1) is a hot/thermal-equilibrium statement while the hTetra sink is a kinetic freeze-out statement — the two must not be conflated. Yields feed Step 2 (bookkeeping) and Step 3 (coldness).
**Cross-sector connections:** CONJ-DPS-1; c04 (ZBW → masses for the freeze-out yields), c14/c15 (yields); the hTetra is the baryon/charm/muon frame (bookkeeping gate double-counting risk).
**Falsification routes:** (a) hTetra binding ≤ 2× hDP (no super-additive closure → free hDPs not scarce, or hTetras not common); (b) freeze-out ordering inconsistent with the observed baryon/relic abundances.
**Source of record:** `founders_vision.md` §6c ("The hTetra sink" + Opus scope note "freeze-out ordering and the binding inequality").
**Registered:** 31 May 2026 (Patch 0700)

---

### CONJ-DPS-3: On-Demand Locally-Generated hDP / W-Bracelet Beta Decay
**Status:** CONJECTURE — registered 31 May 2026 (Session 149, Patch 0700). Near-frontier. Cross-links CONJ-SS-1.
**Sector(s):** DPS, SS, EW
**Priority:** MEDIUM
**One-line statement:** Ordinary nuclear beta decay needs no standing hDP reservoir: when the local superposition of SSVs is momentarily sufficient in a stressed nuclear environment, ambient eDPs and qDPs reorganize into a W bracelet that catalyzes the flavor transformation — explaining why beta decay is rare and localized (it waits for a sufficient SSV fluctuation, so its rate should track the SSV-superposition probability, not ambient hDP concentration).
**Dependencies:** The W₀-bracelet mechanism (CONJ-SS-1); ubiquitous eDP/qDP supply. High-energy hDP needs (heavy quarks, τ, Z, Higgs) remain environment-supplied, distinct from this on-demand STP picture.
**Cross-sector connections:** CONJ-SS-1 (W₀ bracelet locally-linear coupling face); CONJ-DPS-2 (the freeze-out vs on-demand distinction).
**Falsification routes:** beta-decay rate tracks ambient hDP concentration rather than local SSV-superposition probability.
**Source of record:** `founders_vision.md` §6c ("hDPs on demand — beta decay without a standing reservoir").
**Registered:** 31 May 2026 (Patch 0700)

---

### OPEN-COSMO-PBH-1: Occupancy-Retention PBH Seed Mass Function — REGISTERED & CLOSED (null, same patch)
**Status:** CLOSED (NULL) — registered and disposed together at Patch 1903, recording the 1900–1902 little-red-dot (LRD) arc. Proposed Patch 1901; gating computation executed Patch 1902; registry close-out here. **Not a live work item** (no tracking owed; swarm count unchanged).
**The question (1901):** does CPP's occupancy-retention picture of black-hole formation — a PBH = a co-moving region whose DP-Sea occupancy *fails to dilute* below a retention threshold while the background dilutes (founders L33 / Patch 0731), unifying the PBH channel with the same dilution dynamics that drive expansion — yield an early-universe *seed* mass function for the JWST LRD / GLIMPSE-17775 population (M ~ 10²–10⁵ M_⊙) that DIFFERS from standard astrophysical seeding (Pop III remnants / direct collapse) or standard-inflation PBH formation?
**The answer (1902, gating Sub-target 2): NO.** Extrapolating the *adopted* EU-1 spectrum (n_s = 1 − 2/N_*, α_s = −2/N_*², A_s ≈ 2.1×10⁻⁹ — the smooth δN result of Patch 0742, NOT the rejected on/off "cliff" of 0741) to seed scales gives curvature amplitude P_R ~ 1.3×10⁻⁹, σ_δ ~ 3.5×10⁻⁵, hence collapse fraction β ~ exp(−8×10⁷) — zero. Even a deliberately permissive rare-seed target β ~ 10⁻²⁰ needs σ ~ 0.05 (P_R ~ 2×10⁻³): a ~6-order P_R deficit, ~10⁸ in −ln β. The threshold (Sub-target 1) and QCD-EoS (Sub-target 3) levers act only on the O(1) prefactor δ_c *inside* the exponent and cannot close a 10⁸ gap (δ_c 0.45→0.30 still leaves exp(−3.6×10⁷)); Sub-targets 1/3/4/5 mooted. This is the textbook reason a near-scale-invariant spectrum makes no PBHs without a dedicated small-scale enhancement, which EU-1 lacks — and the only spectral feature (the 0741/0742 final-e-fold crash) is a SUPPRESSION at the lightest scales: wrong sign, wrong scale.
**Disposition:** CPP, like ΛCDM, seeds early SMBHs astrophysically, not via PBHs. The CPP-native REFRAME (PBH = occupancy-retention region) survives as correct but phenomenologically empty at seed scales; the discriminating PREDICTION does not exist. **Net result of the LRD arc (1900 + 1902): GLIMPSE-17775 / little red dots are fully compatible with CPP and NON-DISCRIMINATING top to bottom** — accretion side (1900: the "black hole star" spectrum is processing-regime accretion + radiative transfer, CPP ≡ ΛCDM) and seeding side (1902: no PBH seeds, CPP ≡ ΛCDM). A clean closed-loop null. NO THEO (negative), NO prediction, NO verdict moved.
**Sector(s):** COSMO, SR · **Priority:** CLOSED (null).
**Cross-sector connections:** OPEN-COSMO-DM-2 (the related — and also negative — structure-*generation* barrier); CONJ-COSMO-1; the 0741–0747 n_s / roll-off arc in SR.md (the spectrum the null is computed from); c08 / c10 (the BH sector — exact Schwarzschild exterior + Planck-remnant core, untouched by an accreting z=3.5 SMBH); EU-1 (the adopted spectrum).
**Files:** `series_phenomena/cosmology/early_black_holes/` — `pbh_seed_mass_function_scoping.md` (1901), `pbh_seed_subtarget2_closure.md` + `scripts/1902_pbh_seed_amplitude.py` (1902); `series_phenomena/cosmology/early_universe/glimpse17775_lrd_compatibility.md` (1900).
**Registered & closed:** 20 June 2026 (Patch 1903).

---

### CONJ-COSMO-1: Tetra-Gravity Dark Matter
**Status:** CONJECTURE — **structure-formation role RESTORED to conditional-PASS (Patch 2004), superseding the 0729 "conditional false" verdict below.** The 0729 kill applied only to the *swirl/native-scaling* route; it predates the EU-1 arc (0738–0785), which supplies the seeds by a different mechanism (VSL horizon + ZBW-stack δN → n_s=0.9649 = PRED-C-96 = shipped EU-1 v1.0). With EU-1 seeds + the always-inherited growth, CPP reproduces P(k) (Patch 2001), so CONJ-COSMO-1's structure-formation gate is now MET at the EU-1 conditional/grounded level — *not* falsified. Residual = R2/R3/R4 per OPEN-COSMO-DM-2 (none a live threat). **[Patch 2046 — R2 is at conditional-PASS at the audited field-content level (panel-confirmed), unconditional gated on OPEN-SR-9 (which currently leans FAIL from the substrate); see the OPEN-COSMO-DM-2 entry pointer above and `mu_eps_closure/R2-STATUS.md`.]** *Historical record (superseded verdict) preserved below.* **Status:** CONJECTURE — **NOT CONFIRMED; structure-formation role now a CLEAN CONDITIONAL FALSE (Patch 0729).** Registered 31 May 2026 (Session 149, Patch 0700). NEW sector prefix COSMO (cosmology). FAR-FRONTIER. The cheap kills survived (Step 1 σ/m, Step 2 bookkeeping, Step 3 coldness) and the rotation-curve gate is consistent (Step 5, c05-solid) — but these are the admission bar, not discriminating wins. The most discriminating gate, **Step 4 (power spectrum), is a SERIOUS TENSION (Patch 0725)**: the swirl seeds are a causal/active-source mechanism and hit the cosmic-string/defect wall. **[Patch 0729 — the OPEN-COSMO-DM-2 Step-1 kill (pursuing OPEN-SR-7): CPP early dynamics admits NO scaling/quasi-de-Sitter phase (conditional on Gate-1 excess-sourcing) — the only constant-H source (uniform Sea) is non-gravitating, GP exclusion is emergent from ZBW DP oscillation → the early substrate is a fast-oscillating diluting medium (w∈[0,1/3]) → comoving horizon grows → no mode freezing. So the generation half cannot be supplied, and CONJ-COSMO-1 FAILS as a *primary structure-formation* model — a clean conditional false. This kills only the structure-formation ROLE; the microphysics/rotation-curve gates (Steps 1–3, 5) still pass, so CONJ-COSMO-1 survives as a DM *microphysics* candidate. **Residual escape CLOSED (Patch 0731):** no lattice-growth DOF (DP-Sea dilution on a fixed scaffold; founders L33). The verdict-moving frontier collapses to Gate-1/c08 alone.]** Survival as a primary structure source hinged on developing the atemporal Nexus into an acausal seed mechanism that yields a near-scale-invariant adiabatic spectrum (OPEN-COSMO-DM-2) — now shown unavailable from CPP early dynamics within the Friedmann framework. **The conjecture is structurally coherent on microphysics but conditionally falsified on structure formation.**
**Sector(s):** COSMO, SR, SS, SM
**Priority:** MEDIUM
**One-line statement:** Because the four DP species emit different SSV (eDP < qDP < hTetra), a compositional inhomogeneity in the vacuum is automatically a gravitational inhomogeneity; net-neutral cold collisionless concentrations of qDP + hTetra — seeded by early-universe radial-expansion "swirls" and clustered by gravitational instability — are the entity now called dark matter.
**Gate status (per §6c 31-May Update):** Gate 1 (collisionless) survivable — forces act at different ranges; only long-range force on a net-neutral structure is gravity; subquantum cross-section ⇒ negligible cloud-cloud collision rate (Bullet Cluster). Gate 2 (EM-quiet) clear — net-neutral ⇒ dark at range. Gate 3 (halo profile) survivable — collisionless ⇒ non-dissipative ⇒ extended dispersion-supported halo; ρ∝1/r²/NFW is generic to collisionless dynamics. Bookkeeping gate open.
**Dependencies:** SR-1 SSV-gravity + c05/c07 (force law — built; NO GR-extension prerequisite, superseding §6c 924/928, see Patch 0701); CONJ-DPS-1/2/3 (population). Consistency caveat: do NOT simultaneously lean on bonding for halo nucleation and call it negligible for collisionlessness — gravitational instability does the clustering, bonding off-stage at halo density.
**Cross-sector connections:** OPEN-COSMO-DM-1 (its closure plan); CONJ-DPS-1/2/3.
**Falsification routes:** (i) σ/m above the SIDM bound; (ii) velocity dispersion at decoupling not cold; (iii) free-vs-baryon-bound ratio cannot reach ~5:1 without double-counting; (iv) "swirl" seeds cannot reproduce the matter power spectrum; (v) the c05/c07 force law fails to reproduce flat rotation curves quantitatively.
**Source of record:** `founders_vision.md` §6c (the dark-matter conjecture + the 31-May Update). **Working home:** `series_phenomena/cosmology/dark_matter/`. **Arc handover:** `handovers/2026-05-31_session_149_tetra_gravity_dark_matter_arc_kickoff.md`.
**Registered:** 31 May 2026 (Patch 0700)

---

### CONJ-COSMO-2: Dark-Energy ↔ Dark-Matter Unification from the One Dipole Sea
**Status:** CONJECTURE — **CONDITIONALLY SUPPORTED (Patch 0723)**: the OPEN-SR-5 falsification-first sequence A→D is traversed with NO KILL (A survives 0720, B delivered 0721, C partial 0722, D conditional capstone 0723). The DE↔DM unification is structurally coherent and the standard expansion history is recovered, **conditional on two named gaps — neither a kill, both derivation targets**: (1) the c08 field-equation reduction G_μν=8πG/c⁴·T_μν[LSP] (c08's central unproven conjecture; the D2 ground-state-exclusion check rests on it) — **DISCHARGED Patch 1161** (the op:einstein closure: A3′ derives the field equation at λ=16πG/c⁴ zero params, DG-3 3/3; 1107–1108 ground the excess-sourcing in 600-cell symmetry, absolute-|SSV| monopole annihilated; falsifier D2-1 refuted); (2) the event-horizon selection for the Λ IR scale (D3 resolves the dynamics to the future event horizon, but WHY the Sea coherence scale is the event horizon is underived) — **remains the sole open condition**. Registered 1 June 2026 (Session 153-cosmo, Patch 0720). FAR-FRONTIER. Sector prefix COSMO. **NOT promoted to a derived result.** Condition (2) advanced (Patch 1164, 2-ii): the residual is a zero-point **coherence mode** (D3-1 does not fire on the precondition), and A4 gives a coherent **event-horizon** rationale (particle horizon defeated; uniqueness *not* derived; F-COST-1 addressed in principle). **Reviewed as a unit (Patches 1165–1166, ChatGPT/Grok/Copilot): 3/3 confirm the conditional-support calibration** (magnitude/dynamics independently reproduced, no tuning). Routing adjudicated (architect-approved) to the **correlation-length route**: derive the Sea ground-state two-point function ξ(t) — which subsumes the domain-fragmentation cheaper-kill and yields ρ_Λ~1/ξ² — with the A4 coordinable-region construction as fallback; target = the **self-consistency relation** (Li-analog ODE) landing ξ/`R_h` on the event horizon. Promotion still requires deriving the IR scale (ξ→event horizon) + producing that relation.
**Sector(s):** COSMO, SR, SM
**Priority:** MEDIUM
**One-line statement:** A single CPP Dipole Sea sources both dark energy (its uniform-mode residual → suppressed Λ) and dark matter (its inhomogeneity/swirl mode → unsuppressed local-gradient gravity), distinguished only by uniform-mode vs gradient-mode — unifying two of cosmology's three dark puzzles from one substrate.
**Mechanism (one criterion, not three assumptions):** CPP gravity couples to the SSV excess ΔSSV above the local Sea ground state (c05 gradient-sourcing), not to absolute energy density (Step B, Patch 0721). The uniform Sea ground state sources zero gravity despite Planck-scale absolute density (no CC catastrophe); matter/radiation/Sea-swirls are excesses that gravitate; Λ is the residual non-uniformity of the ground state.
**Dependencies:** OPEN-SR-5 (the cosmological Sea-gravitation sector — hard prerequisite); OPEN-SR-5a (Step A, SURVIVES, Patch 0720), OPEN-SR-5b (Step C, Λ suppression, PARTIAL — scaling+coefficient derived, dynamical w(z)→Step D, Patch 0722), OPEN-SR-5c (Step B, DELIVERED, Patch 0721); c05/c07 force law; CONJ-COSMO-1 (the DM half).
**Cross-sector connections:** CONJ-COSMO-1 (Tetra-Gravity Dark Matter — the DM half); OPEN-COSMO-DM-1 (bidirectional); OPEN-SR-5 ↔ OPEN-SM-6 (the CC problem from the SM side — will be the same theorem when solved; coordinate so the two are not derived inconsistently).
**Falsification routes (post-traversal status):** (i) Step A killing the gradient-only cosmology — did NOT (SURVIVES, 0720); (ii) **RESOLVED (Patch 1161)** — the closed CPP field equation is now *derived* (A3′ completes G_μν=8πG/c⁴·T_μν[LSP]) and sources curvature from the LSP excess Δ|SSV|, with the absolute-|SSV| monopole annihilated by 600-cell icosahedral symmetry (spherical 5-design, Σv̂=0; 1107–1108) → the ground state does not gravitate (falsifier D2-1/B1 refuted — formerly the single most load-bearing risk); (iii) Step C deriving the Λ scaling — DONE ((1/8π)ρ_P(l_P/R_H)², 0722); (iv) Step D recovering the Friedmann history — DONE conditionally (D1, 0723); (v) **LIVE** — CPP physics forces the Hubble/causal scale rather than the event horizon, so the residual cannot be the observed dark energy (falsifier D3-1). **One live condition remains (the event-horizon selection, falsifier D3-1); the c08 condition is discharged (Patch 1161); the unification is conditionally supported, not claimed.**
**Source of record:** `series_phenomena/cosmology/sea_gravitation/` (stepA/stepB findings + reasoning/0720,0721). **Arc handover:** `handovers/2026-05-31_session_149_open_sr5_cosmological_sector_arc_kickoff.md`.
**Registered:** 1 June 2026 (Patch 0720)
---

### CONJ-COSMO-3: qCP-Chain Cosmic Web — Inflationary Filaments as Substrate Carrier of Structure
**Status:** CONJECTURE — **MORPHOLOGY / STRUCTURE-PROCESSING only; explicitly DOWNSTREAM OF and CONDITIONAL ON an unsolved seed-generation mechanism. Registered 1 June 2026 (Session 153, Patch 0730).** FAR-FRONTIER. Sector prefix COSMO. Captures Thomas's qCP-chain cosmic-web vision (founders_vision.md §6d): qCP–qCP bonding forms chains (meson-flux-tube analogue) in the inflationary epoch; inflation stretches them to cosmic length; each qCP is a precipitation nidus; post-inflation qDP/hTetra/baryons accrete along the chains → filaments + voids; all species inherit the one qCP-bonding pattern (the framing that targets adiabaticity).
**What it explains well (the processing/morphology role):** why cosmic structure is *filamentary rather than blobby*; the qCP-chain → chain-of-chains recursion gives scale-free clustering — CONFIRMED numerically (Patch 0730 toy: power-law P(k), R²≈0.93). Pairs with the §6c viscosity ordering for differential baryon-vs-DM infall and halo assembly.
**What it does NOT yet do (the generation role — three owed pieces, leverage order):**
1. **Near-constant-H epoch (the blocker).** "During inflation" presupposes a quasi-de-Sitter freezing geometry; Patch 0729 (Step 1) shows CPP early dynamics has none (uniform Sea non-gravitating; ZBW substrate w∈[0,1/3]). Stretching ≠ scale-invariance. Gate-1/c08-adjacent.
2. **Species-agnostic total-density modulation (adiabaticity, the real test).** The qCP-bonding perturbation must modulate *total* ρ pointwise (δ(n_b/n_qDP)=0), not lay a qDP-specific scaffold others trace → else isocurvature. NB the word-trap: thermodynamic adiabaticity (energy isolation, true) ≠ perturbation adiabaticity (common curvature mode, the constraint).
3. **Gaussian, pinned-tilt spectrum.** Patch 0730 toy: the chain-of-chains recursion is scale-free but its slope is a *free dial* (can even mimic scale-invariance — so a "600-cell ratio = 0.96" match settles nothing) and the field is **non-Gaussian by orders of magnitude** (kurtosis ~10²–10³ vs ~0 primordial) — the multifractal signature of *clustered* matter, not *primordial* Gaussian seeds. Decisive, slope-robust.
**Corollary wall (applies to all sub-horizon mechanisms in this family):** thermal mixing, viscosity-differential infall, gravitational instability, and chain stretching are all causal/sub-horizon → cannot make the observed super-horizon adiabatic correlations (SW plateau; TE anti-peak ℓ~100–150 vs ℓ_H~157). Same wall that killed cosmic-string/defect models as primary source.
**Sector(s):** COSMO, SR · **Priority:** LOW-MEDIUM (morphology value; verdict-moving work is upstream at OPEN-COSMO-DM-2 / OPEN-SR-6).
**Dependencies:** OPEN-COSMO-DM-2 (the generation barrier this is conditional on); OPEN-SR-6 (near-constant-H phase, owed-piece 1); CONJ-COSMO-1 (the DM microphysics it would process); §6c viscosity ordering.
**Cross-sector connections:** OPEN-COSMO-DM-2 (parent open problem); CONJ-COSMO-1; CONJ-DPS-1/2 (qDP/hTetra species).
**Falsification / derivation routes:** (i) extend the Patch-0730 toy toward a CPP-specific (golden-ratio-branching) cascade and test whether ANY version yields a *Gaussian* flat-Δ² field (toy says generic recursion does not); (ii) the three owed pieces above — closing (1) is the only thing that reopens generation; (2) and (3) do not matter until (1) exists. If a CPP near-constant-H phase is shown impossible (OPEN-SR-6 unconditional kill), this conjecture is permanently confined to the processing role.
**Source of record:** founders_vision.md §6d (vision); `series_phenomena/cosmology/early_universe/cosmic_web_generation_constraints.md` (constraint reasoning); `scripts/0730_chain_recursion_power_spectrum.py` (7/7 PASS). **[Patch 0732: the most concrete generation candidate — Thomas's Axiom H (PSR-superposition inflation engine) — was evaluated and does not supply generation without overriding the SR-1 speed-of-light ceiling (super-c PSR) + a free parameter + a separate e-fold source; saturation-dilution gives ln(occupancy)≪60 e-folds. See `axiom_h_inflation_engine_evaluation.md` / founders §6e. CONJ-COSMO-3 stays morphology/processing-only.]** **[Patch 0733 — CORRECTION: 0732's super-c objection is withdrawn (it mis-read `l_P` as the grid step; `l_P` is the baseline PSR ≈ 10³⁰ sub-Planck GPs per c07/glossary/c01). Inflation reframed as an OPEN Variable-Speed-of-Light question. The spectrum (Gaussianity + scale-invariance) remains the deepest owed piece, unchanged.]**
**Registered:** 1 June 2026 (Patch 0730)
