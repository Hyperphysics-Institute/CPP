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
