# CPP Research Frontier

**Location:** `/CPP/Research_Frontier.md`
**Last updated:** 23 April 2026
**Maintainer:** Thomas Lee Abshier ND, Hyperphysics Institute
**Architecture:** See `templates/Research_Frontier_Architecture.md`
**Nomenclature:** See `nomenclature.md`

---

## Purpose

One flat file showing the complete landscape of every identified problem, conjecture, proposition, and frontier item in Conscious Point Physics — with status, sector, dependencies, and enough context to assess interconnections.

**Answers the question:** *What is solved, what is open, and what connects to what?*

**Problem count:** 82 entries (49 open, 14 conjectures, 15 propositions, 6 resolved, 6 falsified). *(Counts exclude sub-problems.)*

---

## How to Use This File

- **Finding work:** Scan by sector or priority. Start with the Recommended Attack Order (§7).
- **Starting a problem:** Read the entry here for context, then the history file (when it exists) for what has been tried.
- **After a session:** Update the relevant entry's status, "Current best lead," and "Last updated" fields.
- **After a paper:** Move resolved items to §5. Update dependency graph.

---

# §1 — Active Open Problems (OPEN)

Problems with no candidate solution, or where candidate solutions have been explored but no resolution is in sight.

---

## Strong Sector (SS) — 18 problems (1 retired)

### OPEN-SS-1: Quark Mass Formula M_q(n_layers)
**Status:** OPEN (PARTIAL — Theorems 2–3 proved; full formula open)
**Sector(s):** SS
**Priority:** HIGHEST
**One-line statement:** Express all six quark masses as a single function of cage depth, sea_strength, and φ.
**What a solution looks like:** A formula M_q(n) with zero free parameters matching PDG masses across 5 orders of magnitude.
**Dependencies:** OPEN-SS-5 (r_conf), OPEN-SD-lattice-scale (unit conversion)
**Cross-sector connections:** Feeds OPEN-G-1 (lepton analogy), OPEN-SS-3 (chiral condensate for light quarks)
**Current best lead:** ZBW thermal picture (Thomas); K(c,b,t) = 2/3 to 0.4% suggests heavy quarks dominated by ZBW thermal energy. φ^(3(l-1)) volume scaling FALSIFIED (PS-1). Phase cancellation factors C_n confirmed but insufficient for top quark.
**History file:** `problem_histories/PH-OPEN-SS-1.md` *(to be created)*
**Paper(s):** SS-1, SM-8, SM-9
**Last updated:** 23 March 2026

---

### OPEN-SS-2: Three SM Generations from Cage Geometry
**Status:** OPEN
**Sector(s):** SS
**Priority:** HIGH
**One-line statement:** Prove three quark generations arise from a single 600-cell geometric principle.
**What a solution looks like:** A proof that the six eigenvalues pair into exactly three conjugate pairs matching the cage-depth generation structure.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-G-1 (unified three-generation proof), OPEN-SM-7e (lepton generations)
**Current best lead:** Two independent observations (cage depth grouping and eigenvalue pairing) point the same direction, but neither is a proof.
**Paper(s):** SS-1
**Last updated:** 23 March 2026

---

### OPEN-SS-3: Chiral Condensate ⟨q̄q⟩ from ZBW Dynamics
**Status:** OPEN
**Sector(s):** SS
**Priority:** MEDIUM
**One-line statement:** Derive |⟨q̄q⟩|^(1/3) ≈ 240–250 MeV from CPP ZBW dynamics without calibration.
**What a solution looks like:** ZBW phase coherence integral over DP Sea matching lattice QCD value.
**Dependencies:** OPEN-SS-1 (light quark masses)
**Cross-sector connections:** Pion mass derivation, f_π
**Current best lead:** GOR estimate gives 289 MeV (15% above lattice); offset consistent with tree-level mass limitation.
**Paper(s):** SS-5
**Last updated:** 23 March 2026

---

### OPEN-SS-4: Two-Loop β₁ from CPP qCP Cage Dynamics
**Status:** OPEN
**Sector(s):** SS
**Priority:** MEDIUM
**One-line statement:** Derive β₁ = 102 − 38n_f/3 = 26 from CPP tetrahedral algebra.
**What a solution looks like:** Explicit calculation of quartic gluon vertex + two-loop diagrams giving α_s(M_Z) < 1% of PDG.
**Dependencies:** None (SS-3 algebra is sufficient)
**Cross-sector connections:** OPEN-SS-7 (Λ_QCD)
**Current best lead:** Quartic vertex derivable from (T^a T^b)²; not yet computed.
**Paper(s):** SS-4
**Last updated:** 23 March 2026

---

### OPEN-SS-5: String Tension σ from sea_strength
**Status:** OPEN (PARTIAL — mechanism established; one step remaining)
**Sector(s):** SS
**Priority:** HIGH
**One-line statement:** Derive σ ≈ 0.9 GeV/fm from sea_strength and 600-cell geometry without calibration.
**What a solution looks like:** Express r_conf = f(sea_strength, l_P, φ), then σ = α_s ℏc/r_conf².
**Dependencies:** None blocking (sea_strength now derived)
**Cross-sector connections:** Prerequisite for OPEN-SS-7, OPEN-SS-10, OPEN-SS-14, OPEN-SS-6
**Current best lead:** Bow rigidity mechanism established; self-collimation threshold is the remaining step — a dimensional-analysis calculation.
**Paper(s):** SS-4, C14
**Last updated:** 23 March 2026

---

### OPEN-SS-6: Glueball Mass from Closed Tetrahedral hDP Loop
**Status:** OPEN
**Sector(s):** SS, EW
**Priority:** MEDIUM
**One-line statement:** Compute lightest scalar glueball mass using f_geom formula applied to closed hDP loop.
**What a solution looks like:** Identify the closed-loop subgraph, compute f_geom, get mass in 1.5–2 GeV range.
**Dependencies:** OPEN-SS-5 (energy scale)
**Cross-sector connections:** Would be first shared EW+SS mass formula
**Current best lead:** Same f_geom formula as EW bosons; identify which cell-level subgraph.
**Paper(s):** SS-3
**Last updated:** 23 March 2026

---

### OPEN-SS-7: Λ_QCD from PSR Saturation
**Status:** OPEN
**Sector(s):** SS
**Priority:** MEDIUM
**One-line statement:** Derive Λ_QCD ≈ 0.218 GeV from PSR saturation without PDG input.
**What a solution looks like:** Self-consistent derivation via PSR_eff → l_P/2 threshold.
**Dependencies:** OPEN-SS-5 (r_conf)
**Cross-sector connections:** OPEN-G-2 (closes last strong-sector parameter)
**Current best lead:** Dimensional estimate gives factor-of-13 overshoot; proper RGE needed.
**Paper(s):** SS-4
**Last updated:** 23 March 2026

---

### OPEN-SS-8: Nucleon Magnetic Moments from ZBW Quark Currents
**Status:** OPEN
**Sector(s):** SS
**Priority:** HIGH
**One-line statement:** Derive μ_p = +2.793 μ_N and μ_n = −1.913 μ_N from ZBW orbital dynamics.
**What a solution looks like:** Compute ⟨L̂+2Ŝ⟩_ZBW for u,d quarks from cage geometry; apply SU(6) formula.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-G-2 (lepton anomalous moments by analogy)
**Current best lead:** SU(6) + ZBW mechanism correct; notebook parameters (anomaly_base = 0.792) are fitted, not derived. Benchmark table values (0.03%, 0.16% error) better than notebook (30%, 12%).
**Paper(s):** New (not in SS-1–5)
**Last updated:** 23 March 2026

---

### OPEN-SS-10: Nuclear Binding Energy V(r) from qDP Chain Insertion
**Status:** RESOLVED across A=2,3,4 — by SS-5 v6 (18 April 2026, v0.2/v3 content retained) via the cascade formula CONJ-SS-11; full $V(r)$ shape separately registered as OPEN-SS-20 (short-range) and OPEN-SS-21 (orbital)
**Sector(s):** SS
**Priority:** HIGH
**One-line statement:** Derive nucleon–nucleon potential V(r) from qDP chain insertion dynamics.
**What a solution looks like:** V(r) with correct shape (attraction at 1–3 fm, repulsion below 0.5 fm, ~8 MeV/nucleon saturation).
**Dependencies:** OPEN-SS-5 (r_conf, σ)
**Cross-sector connections:** Nuclear chart series (future), r-process nucleosynthesis
**Current best lead:** SS-5 v6 predicts $B_d$, $B_{^3H}$, $B_{^3He}$, $B_{^4He}$ via base-to-base K$_3$ mechanism with cascade factor $(A-1)$, Pauli penalty $M_0/\varphi^3$, and $A=4$ closure bonus $M_0/\varphi$. All four predictions $\leq 5.3\%$ error, zero parameters. Additionally predicts unboundness of $^5$He, $^5$Li, $^8$Be — all confirmed. Full $V(r)$ shape split into short-range (OPEN-SS-20) and orbital (OPEN-SS-21) subproblems.
**Paper(s):** SS-5 v6 (integrated binding); SS-6 v0.1 registers $V_{\mathrm{SR}}$ and orbital subproblems
**Last updated:** 18 April 2026

---

### OPEN-SS-11: Uniqueness of SU(3) Operator Mapping
**Status:** RESOLVED → **THEO-SS-10** (SS-3, Theorem 3.3, 15 April 2026)
**Sector(s):** SS
**Priority:** HIGH
**One-line statement:** Prove the tetrahedral hopping → SU(3) mapping is unique (not just consistent).
**What a solution looks like:** 1–2 page argument classifying C₃-invariant traceless Hermitian operators on ℂ³, showing dimension 8 and SU(3) commutation uniqueness.
**Resolution:** SS-3 proves SU(3) is the unique Lie algebra of the tetrahedral cage via dimension counting + Gell-Mann orthogonality + simplicity of su(3). Explicit 4+4 physical mode basis with 8×8 change-of-basis matrix (det = 2/√3).
**Dependencies:** None (pure group theory)
**Cross-sector connections:** Strengthens SS-1 Theorem 1 from possibility to necessity
**Current best lead:** Dimension forced (8 independent operators = dim(su(3))); edge structure canonical; C₃ constraint restricts alternatives. Tractable in 1–2 pages.
**Paper(s):** SS-1 (planned v4 addition)
**Last updated:** 29 March 2026

---

### OPEN-SS-12: W Bracelet Polarity Inversion from CPP First Principles
**Status:** OPEN
**Sector(s):** SS, EW
**Priority:** HIGH
**One-line statement:** Derive that W-mediated quark transitions necessarily invert qCP polarity.
**What a solution looks like:** Coupling Hamiltonian showing W bracelet produces asymmetric charge transfer; Z icosahedron produces symmetric (no inversion).
**Dependencies:** Requires reading EW-2 (W bracelet structure)
**Cross-sector connections:** Complete EW-strong unification; quark flavor transition theory
**Current best lead:** Locally-linear coupling face geometry (CONJ-SS-1). Universal polarity switching verified across all known decay pathways (CONJ-SS-2).
**Paper(s):** SS-1, EW-2
**Last updated:** 29 March 2026

---

### OPEN-SS-13: Quantitative ZBW Mechanism for δ = 1/3
**Status:** OPEN
**Sector(s):** SS
**Priority:** MEDIUM
**One-line statement:** Show ZBW orbital time fraction in 1/r³ configuration equals exactly 1/3.
**What a solution looks like:** WKB or equivalent calculation giving τ_{1/r³} : τ_{1/r²} = 1:2.
**Dependencies:** OPEN-SS-9 ✅ SOLVED (topological proof is authoritative; this is the mechanical confirmation)
**Cross-sector connections:** Connects SR-1 ZBW treatment to strong-sector charge screening
**Current best lead:** 2:1 ZBW frequency ratio may directly set 1:2 time allocation; depends on orbit shape.
**Paper(s):** SM-1, SS-1
**Last updated:** 29 March 2026

---

### OPEN-SS-14: QCD Deconfinement Temperature from CPP
**Status:** OPEN
**Sector(s):** SS
**Priority:** MEDIUM
**One-line statement:** Derive T_c ≈ 155 ± 10 MeV from sea_strength and 600-cell geometry.
**What a solution looks like:** k_B T_c = σ · r_conf from thermal disruption of qDP chain self-collimation.
**Dependencies:** OPEN-SS-5 (σ and r_conf)
**Cross-sector connections:** Early universe physics, QGP phase
**Current best lead:** Dimensional estimate gives ~140 MeV (within 10% of lattice QCD).
**Paper(s):** SS-1
**Last updated:** 29 March 2026

---

### OPEN-SS-16: Derive Operator Formalism and System-Bath Coupling from CPP Primitives (Layer B Gap)
**Status:** OPEN
**Sector(s):** SS, SD (programme-wide)
**Priority:** **CRITICAL** — highest-leverage single piece of work remaining
**One-line statement:** Derive complex-linear Hermitian operators, Lie bracket structure, and Caldeira–Leggett system-bath coupling from CPP's DI-bit exchange dynamics.
**What a solution looks like:** A paper (SD-6 or late SS number) showing that DI-bit propagation on the 600-cell lattice forces: (1) complex state space ℂ^N, (2) Hermitian observables, (3) tracelessness for gauge generators, (4) Lie bracket closure, (5) Caldeira–Leggett-type system-bath coupling from DI-bit exchange, (6) rapid thermalisation τ_relax ≪ τ_ZBW, (7) full Gibbs equilibration (not just dephasing). Items 1–4 close the Layer B gap in SS-3; items 5–7 close the Layer B gap in SM-3.
**Dependencies:** None blocking (CPP axioms A1–A3 are sufficient starting points)
**Cross-sector connections:** Closes Layer B across **every** paper in the programme. Specifically: SS-3 (SU(3) uniqueness), SM-3 (Koide K = 2/3), and any future paper that imports quantum-mechanical formalism without deriving it from CPP primitives.
**Current best lead:** The DI-bit exchange mechanism (Axiom A3) provides complex amplitudes propagating at c = l_P/t_P. The PCD (Propagation, Computation, Display) cycle at each Absolute Moment is the natural candidate for operator structure. The DP Sea's Planck-temperature thermal bath is the natural system-bath coupling source. No derivation has been attempted yet.
**Discovery context:** Identified as a programme-level vulnerability by ChatGPT (OpenAI) during independent review of SS-3 and SM-3 (April 2026). Both papers received "Major revision required" on first round, with the same structural critique: imported quantum-mechanical formalism not derived from CPP primitives. The Layer A/B/C epistemic decomposition was applied to both papers to make the gap transparent.
**Paper(s):** SD-6 (or late SS number; note SS-4 is already assigned to string tension)
**Last updated:** 16 April 2026

---

### OPEN-SS-17: Light-Nuclei Binding Curve $B(A, Z)$ from Open-Vertex Combinatorics
**Status:** PARTIALLY RESOLVED by SS-5 v0.2 at A=2,3,4 (see CONJ-SS-11); extension to A>=6 alpha-cluster regime is OPEN-SS-18
**Sector(s):** SS (nuclear physics)
**One-line statement:** Extend the SS-5 open-vertex mechanism to all light nuclei.
**Paper(s):** SS-5 v0.2 covers A=2,3,4 + unboundness at A=5,8. Heavier nuclei → OPEN-SS-18.
**Last updated:** 17 April 2026

---

### OPEN-SS-18: Heavy-Nuclei Alpha-Cluster Regime $B(A, Z)$ for A$\geq$6
**Status:** PARTIALLY RESOLVED (by SS-7 v1.2 at $N_\alpha = 3$ through 14 for strict $N{=}Z$ alpha-chain nuclei, 21 April 2026). Remainder open as OPEN-SS-23.
**Sector(s):** SS (nuclear physics)
**Priority:** HIGH
**One-line statement:** Derive the empirical binding curve for $A \geq 6$ nuclei from coupled-alpha-particle cluster structure within the CPP open-vertex framework.
**What a solution looks like:** A structural account of $^6$Li, $^6$He, $^{12}$C, $^{16}$O, $^{20}$Ne, ..., $^{56}$Fe (peak binding-per-nucleon) that reproduces the empirical binding curve within the CPP residual band. Must include: (a) alpha-alpha residual binding at scale $\sim M_0/\varphi$ per contact, (b) decreasing per-contact binding with increasing $n_\alpha$ (saturation), (c) onset of stability valley and peak at $A=56$, (d) termination of stability at heavy nuclei.
**Dependencies:** CONJ-SS-11 (SS-5 v6 cascade formula); structural theory of alpha-cluster interactions.
**Current best lead:** SS-7 v1.2 formula $B(N_\alpha) = N_\alpha\Balpha + (3N_\alpha-6)B_{\text{pair}}$ resolves the strict $N{=}Z$ alpha-chain at $N_\alpha \in [3, 14]$ (${}^{12}$C through ${}^{56}$Ni) to within $\pm 1.5\%$ against AME 2020; RMS $0.80\%$ across all twelve nuclei. Remainder (non-$N{=}Z$ isotopes, odd-$A$ nuclei, non-alpha-clustered structures) registered as OPEN-SS-23.
**Paper(s):** SS-7 v1.2 (primary resolution). Registrations downstream: CONJ-SS-12, PROP-SS-7-1, OPEN-SS-23, OPEN-SS-24, OPEN-SS-25.
**Registered:** 17 April 2026 (updated 18 April 2026: SS-6 slot reassigned to deuteron-bipyramid scoping, alpha-cluster moved to SS-7; partially resolved 21 April 2026 by SS-7 v1.2, with remainder split to OPEN-SS-23)

---

### OPEN-SS-22: Heavy-Nuclei Icosahedral Closure at $N_\alpha \geq 12$ — RETIRED
**Status:** ✗ **RETIRED 21 April 2026** (SS-7 v1.2). First retired open problem in the CPP programme record. See `problem_histories/PH-OPEN-SS-22.md` for the full retirement narrative.
**Sector(s):** SS (nuclear physics)
**Historical one-line statement (as registered 20 April 2026):** Derive the behavior of the alpha-polytope edge formula at $N_\alpha \geq 12$; proposed activation of an icosahedral closure bonus at $N_\alpha = 12$ analogous to SS-5's ${}^4$He tetrahedral closure.
**Registered:** 20 April 2026 in SS-7 v1.1 §5.1
**Retired:** 21 April 2026 in SS-7 v1.2 §5.1
**Reason for retirement:** The empirical anchor — an apparent $-2$ to $-2.5\%$ residual plateau at $N_\alpha = 12, 13, 14$ — was found to be an isotope-selection artifact. The v1.1 Table 1 used non-$N{=}Z$ isotopes (${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe, each with $N - Z = +4$); the strict $N{=}Z$ counterparts (${}^{48}$Cr, ${}^{52}$Fe, ${}^{56}$Ni) stay in family with the primary set at $+0.40\%, +0.57\%, +0.73\%$ — no structural onset visible. The ~2 MeV/neutron seen in the v1.1 rows is standard neutron-excess binding, outside the alpha-chain formula's scope by construction.
**Verification:** Three-reviewer convergence on interpretation (a) — isotope-selection artifact, no defensible physical reason for the non-$N{=}Z$ choice — established on 21 April 2026 (ChatGPT, Copilot, Grok). Convergence itself is part of the evidence supporting retirement, not author-team choice alone.
**Downstream registration:** The ~2 MeV/neutron signal (neutron-excess physics) is absorbed into OPEN-SS-23, which is now the primary SS-8 target. The DP-sea screening physics previously tagged "OPEN-SS-22-adjacent" in v1.1 is registered as new OPEN-SS-25.
**Programme-level significance:** First retirement precedent in the CPP programme record. Establishes RETIRED as a new open-problem status, distinct from RESOLVED (solution found), PARTIALLY RESOLVED (sub-scope solved), FALSIFIED (claim disproved). Retirement applies when a problem's registered empirical anchor is subsequently found to be an artifact such that no well-defined replacement anchor exists for the hypothesis that motivated registration.

---

### OPEN-SS-23: Non-$N{=}Z$ and Odd-$A$ Extension of the Alpha-Chain Formula
**Status:** OPEN (primary SS-8 target after v1.2 priority upgrade)
**Sector(s):** SS (nuclear physics)
**Priority:** HIGH
**One-line statement:** Extend the SS-7 alpha-chain binding formula to non-$N{=}Z$ isotopes at alpha-chain $N_\alpha$ values, odd-$A$ nuclei with extra-nucleon-bound-to-alpha-core structures, and non-alpha-clustered nuclei.
**What a solution looks like:** A CPP derivation of the $\sim 2$ MeV per extra neutron signal visible in non-$N{=}Z$ isotopes (${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe each with $N - Z = +4$; ${}^{48}$Ca at $N - Z = +8$ as a stress test). A CPP treatment of single-nucleon excess bound to an alpha-polytope core (${}^7$Li, ${}^9$Be, ${}^{11}$B, ${}^{13}$C). A CPP treatment of partial-alpha substructures (${}^6$Li $\approx$ ${}^4$He + d, ${}^{14}$N, ${}^{18}$O, ${}^{30}$Si). Success criterion: the stability valley from ${}^{40}$K through ${}^{208}$Pb reproduced within CPP residual precision.
**Dependencies:** SS-7 v1.2 formula and constants (${}^4$He binding, $B_{\text{pair}} = M_0/\varphi$). CPP treatment of DP-sea behaviour in non-$N{=}Z$ configurations.
**Current best lead:** Preliminary SS-7 inspection of ${}^6$Li: residual alpha-deuteron binding 1.47 MeV, approximately $2B_{\text{pair}}/3 \approx 1.56$ MeV — suggestive of an incomplete K$_3$ face at the alpha-d contact. The ${}^{48}$Ti/${}^{52}$Cr/${}^{56}$Fe block (shown in SS-7 v1.2 footnote Table 2) provides the nearest empirical anchor for the neutron-excess derivation.
**Paper(s):** SS-8 (primary target, per v1.2 retargeting from the retired OPEN-SS-22).
**Registered:** 20 April 2026 in SS-7 v1.0; priority upgraded 21 April 2026 in SS-7 v1.2 to primary SS-8 target.

---

### OPEN-SS-24: First-Principles CPP Derivation of Simplicial Contact Structure
**Status:** OPEN
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM-HIGH
**One-line statement:** Derive assumption C4 of SS-7 (alpha clusters in bound strict-$N{=}Z$ nuclei arrange as vertices of simplicial convex 3-polytopes) from CPP lattice-level dynamics.
**What a solution looks like:** A rigorous demonstration, starting from SS-2's nucleon structure and the CPP 600-cell lattice, that the ground-state configuration of $N_\alpha$ rigid alpha tetrahedra with base-to-base K$_3$ contact faces realizes a convex, triangular-faced, simplicial 3-polytope. Would convert SS-7's assumption C4 from empirically-supported hypothesis to derived structural result. Would also yield $R_{\alpha\alpha}$ as a forward prediction rather than a consistency parameter inverted from ${}^8$Be (Finding 4.1).
**Dependencies:** SS-2 nucleon structure; SS-5 K$_3$ collective-mode machinery; CPP open-vertex closure principles.
**Current best lead:** Physical-intuition arguments present in SS-7 §2.1 (triangular faces from rigid-tetrahedra shared-face geometry; maximal connectivity from thermodynamic selection at fixed vertex count; convexity from rigid-packing constraints). These are suggestive but not rigorous. Full derivation likely requires explicit treatment of the DP-sea reorganization as alpha-polytopes form.
**Paper(s):** SS-9 candidate (future, theory paper).
**Registered:** 20 April 2026 in SS-7 v1.0.

---

### OPEN-SS-25: DP-Sea Screening of Alpha-Alpha Coulomb in Bound Polytopes
**Status:** OPEN
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM
**One-line statement:** Derive the effective Coulomb reduction $V_C^{\rm eff}$ between alphas embedded in a bound polytope from CPP primitives, reproducing the full-Coulomb limit at isolated alpha-alpha contact (${}^8$Be case).
**What a solution looks like:** A CPP derivation of the DP-sea reorganization that occurs when two alphas in contact are surrounded by additional alpha neighbours (as in $N_\alpha \geq 3$ bound polytopes). Must reproduce: (a) full vacuum Coulomb $\sim 2.4$ MeV at isolated contact (recovers SS-7 ${}^8$Be 92 keV unboundness, Finding 4.1); (b) effective Coulomb near zero for embedded contacts (required by SS-7 Table 1 agreement of the Coulomb-free formula within $\pm 1.5\%$ at $N_\alpha \geq 3$); (c) smooth interpolation between the two regimes as $N_\alpha$ grows.
**Dependencies:** SS-7 v1.2 (the 12-nucleus agreement is the empirical evidence that effective Coulomb is strongly reduced in bound polytopes); SS-2 / SS-5 DP-sea machinery; CPP treatment of collective charge redistribution.
**Current best lead:** SS-7 v1.2 §5.4 discussion: qualitative scaling argument and cluster-model comparison support the screening mechanism. Figure 4 is a schematic representation only; the full DP-sea charge profile is not derived. This was tagged "OPEN-SS-22-adjacent" in SS-7 v1.1 §8; registered as its own open problem in v1.2 when the umbrella OPEN-SS-22 was retired.
**Paper(s):** Target paper deferred. Likely uses the same lattice-geometry machinery as OPEN-SS-24.
**Registered:** 21 April 2026 in SS-7 v1.2 (absorbs the DP-sea screening content that was tagged "OPEN-SS-22-adjacent" in v1.1).

---

### OPEN-SS-26: D1 Interstitial Site Localization from SSV Minimization
**Status:** OPEN (PARTIAL — Level-1 algebraic + Level-2 functional independence achieved under Models A/B; Level-3 physical-principle independence open)
**Sector(s):** SS (nuclear physics)
**Priority:** HIGH
**One-line statement:** Derive D1 (an interstitial neutron added to a bulk alpha-polytope localizes at an alpha-vertex rather than at an edge-midpoint, face-center, or centroid site) from CPP primitives via SSV-minimization.
**What a solution looks like:** A CPP derivation establishing that vertex sites minimize the neutron-localization SSV functional across all bulk simplicial deltahedra, from axioms A1–A11 without importing proximity-binding as an unstated assumption. Once D1 is proved at Level-3, the H2' 2E/V scaling law for interstitial neutron binding becomes a geometric corollary of D1 + D2.
**Dependencies:** None blocking for Path α (derive proximity-binding from A1–A3). OPEN-SS-27 closure provides a third conditional realization under D2 but shares the proximity-binding ancestor, so does not close the Level-3 gap.
**Cross-sector connections:** Methodological — the Level-1/2/3 independence decomposition generalizes to any CPP claim stated as "proved from independent premises X, Y." Spot audit of existing theorems against this discipline is a cheap programme-level hygiene check.
**Current best lead:** Dual-model SSV-minimization sketch (22 April 2026) delivers D1 as a conditional theorem under two functionally independent realizations of proximity-binding — Model A (K₃-edge counting under D2) and Model B (short-range Yukawa pair physics). Q2 algebraic reduction test shows Model B does NOT reduce to Model A under any short-range regime (three decisive discriminators: multiplicity vectors, non-vertex orderings, vertex-degree scaling). Both models share a proximity-binding ancestor principle; if that principle fails programme-wide, both models fail together. Level-3 independence remains open: would require either (a) deriving proximity-binding from CPP primitives, or (b) constructing a third model that produces D1 without invoking proximity.
**Falsification route:** Construction of a bulk simplicial deltahedron at which CPP pair-binding physics predicts an interstitial site outside the vertex class, under any plausible proximity-binding mechanism. Or: demonstration that proximity-binding itself is incompatible with a derived CPP axiom.
**History file:** `problem_histories/PH-OPEN-SS-26.md` (captures Round 2 narrative + Level-1/2/3 decomposition methodology)
**Paper(s):** SS-8 (v0.1 target).
**Registered:** 21 April 2026 in SS-8 H2' derivation note §10 (formal registry entry added 23 April 2026).

---

### OPEN-SS-27: D2 K₃-Edge Coupling via A6' Extension
**Status:** OPEN
**Sector(s):** SS (nuclear physics)
**Priority:** HIGH (two-for-one — closure delivers D1 automatically via simplicial combinatorics under Model A)
**One-line statement:** Derive D2 (each K₃-edge contact between adjacent alphas contributes per-edge binding strength $B_{	ext{pair}} = M_0/arphi$ to the interstitial-neutron energy landscape) from CPP primitives via an extension of axiom A6' (SS-5 base-to-base K₃-reduced collective-mode framework).
**What a solution looks like:** A CPP derivation extending A6' from the base-to-base K₃-reduced collective-mode framework (as it operates at alpha-alpha contact faces in SS-5 nucleon binding) to the per-edge framework needed for SS-7 alpha-polytope edge-counting and SS-8 interstitial-neutron localization. Must reproduce: (a) the per-edge $B_{	ext{pair}}$ strength empirically supported by SS-7 v1.2 twelve-nucleus agreement, (b) the vertex-degree-dependent enhancement at D1 alpha-vertex sites, (c) consistency with the CPP A1–A11 axiom set without introducing new structural assumptions.
**Dependencies:** SS-5 collective-mode machinery (A6' or its successor); SS-7 v1.2 empirical anchor; CPP treatment of DP-sea reorganization across polytope edges.
**Cross-sector connections:** Closure automatically delivers D1 as a two-for-one under simplicial combinatorics (Model A). Delivers SS-7's $3N_lpha - 6$ edge formula as a derived structural result rather than an empirical regularity (converts CONJ-SS-12 from conjecture to corollary of THEO-SS-27).
**Current best lead:** SS-5 v6 establishes the base-to-base K₃-reduced mechanism at the alpha-alpha contact face. SS-7 v1.2 extends empirically to per-edge strength in bulk polytopes. The A6' derivation is the structural missing link between the two. Likely approach: treat the alpha-polytope as a graph with alpha-vertices and K₃-edge contacts, express the SS-5 collective-mode structure as local to each K₃ face, verify the local structure tiles correctly over the polytope. May require explicit DP-sea redistribution calculation at polytope edges (related to OPEN-SS-24 and OPEN-SS-25 methodology).
**Paper(s):** Opened in SS-8 H2' derivation note §10 (21 April 2026). Target paper: SS-9 candidate (shares structural-polytope machinery with OPEN-SS-24).
**Registered:** 21 April 2026 in SS-8 H2' derivation note §10 (formal registry entry added 23 April 2026).

---

### OPEN-SS-28: D3 Bulk Averaging and Residual Decomposition
**Status:** OPEN
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM
**One-line statement:** Derive D3 (bulk averaging of the interstitial-neutron SSV landscape reproduces the 2E/V scaling law of H2' with residuals accounted for by a small set of identifiable physical mechanisms) from CPP primitives, and decompose the observed residual in the SS-8 Phase 1 empirical map into its constituent mechanisms.
**What a solution looks like:** (a) A CPP derivation of the bulk averaging procedure showing that over any bulk simplicial deltahedron the average alpha-vertex degree $ar{d}_v = 6 - 12/V$ controls the interstitial-neutron energy to leading order, with explicit error bounds. (b) An identified residual decomposition: given the Phase 1 empirical map's ~0.3–0.5 MeV residual at $N_lpha = 8, 12$ and matching Ca-chain odd-even staggering, isolate the contributions from (i) opposite-polarity $N_	ext{ex} = 2$ pair bonus, (ii) small-polytope attenuation at $N_lpha \leq 4$, (iii) polytope-identity fine structure at non-unique $N_lpha$ (e.g., octahedron vs triangular antiprism at $N_lpha = 6$), and (iv) any additional mechanisms the data require.
**Dependencies:** OPEN-SS-26, OPEN-SS-27 (both feed the averaging derivation); SS-5 pair-bonus mechanism (for residual decomposition).
**Cross-sector connections:** Completes the H2' structural derivation. Residual decomposition is where SS-8 meets the Ca-isotope chain work.
**Current best lead:** Phase 1 empirical map identified k_eff plateau at ~5 matching 2E/V = 6 − 12/V for bulk simplicial polytopes. Residuals at $N_lpha = 4, 8, 12$ are the right size and sign for $B_{	ext{pair}}$-scale opposite-polarity pair bonuses from $N_	ext{ex} = 2$ contributions. The decomposition is empirically suggestive but not yet derived from structural principles.
**Paper(s):** SS-8 (v0.1 target, downstream).
**Registered:** 21 April 2026 in SS-8 H2' derivation note §10 (formal registry entry added 23 April 2026).

---

### OPEN-SS-19: Rigorous Derivation of $(A{-}1)$ Cascade Multiplicity and Pauli Coefficient
**Status:** OPEN
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM-HIGH
**One-line statement:** Derive the two working conjectures at the heart of CONJ-SS-11 — the $(A-1)$ cascade reinforcement factor and the Pauli penalty coefficient $M_0/\varphi^3$ — from CPP primitives. Also derive the NLO correction $\varepsilon_d \approx 0.050$ closing the 5.3% LO residual.
**What a solution looks like:** (a) Rigorous proof that each np pair in a closed $A$-nucleon polytope is reinforced by exactly $A-1$ closed-polytope completion pathways, analogous to SS-3's 4+4 mode-counting proof for internal tetrahedra. (b) Rigorous derivation of the like-nucleon antisymmetrisation cost from the fermion statistics of the lattice ZBW oscillator, matching the empirically-validated value $M_0/\varphi^3$. (c) NLO correction $\varepsilon_d$ from a binding-reducing mechanism (tensor/D-wave, zero-point motion, or spin-orbit) — NOT from base-face K$_3$ asymmetry, which SS-5 v5 Appendix §9 shows gives the wrong sign.
**Dependencies:** OPEN-SS-16 (Layer B gap closure would assist both derivations).
**Current best lead:** SS-5 v6 §5 identifies the $(A-1)$ factor as the natural closed-graph completion count; §5.2 gives a propagation-step-count argument for the Pauli coefficient. Both are motivated but not rigorous. For $\varepsilon_d$: SS-5 v6 Appendix B rules out v4's Möbius cage-distortion mechanism (four independent problems); §9 rules out base-face K$_3$ asymmetry (wrong sign); candidates remaining are tensor/D-wave coupling, zero-point motion, spin-orbit.
**Paper(s):** Future SS-series or part of SS-5 v7+ revisions
**Registered:** 17 April 2026 (updated 18 April 2026 with v4 stress-test outcome and base-face asymmetry result from SS-5 v5/v6)

---

### OPEN-SS-20: Short-Range np Potential $V_{\mathrm{SR}}(r)$ Shape from CPP Primitives
**Status:** OPEN
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM
**One-line statement:** Derive the shape of the short-range nucleon-nucleon potential $V_{\mathrm{SR}}(r)$ as a function of inter-nucleon separation, starting from the base-to-base K$_3$ face structure of SS-5.
**What a solution looks like:** Functional form of $V_{\mathrm{SR}}(r)$ satisfying: (a) $V_{\mathrm{SR}}(0) = -B_{\mathrm{pair}} = -2.342$ MeV at rigid contact, (b) $V_{\mathrm{SR}}(r) \to 0$ as $r \to \infty$, (c) natural CPP length scale $\ell_{\mathrm{edge}} = 0.364$ fm. Candidate forms (Coulombic $\propto -\ell/\sqrt{\ell^2+r^2}$, Yukawa $\propto -e^{-r/\ell}$, smooth cutoff $\propto -\ell/(\ell+r)$) must be selected by a CPP-structural argument, not by fit. Once derived, yields $a_{np}$ beyond zero range, effective range $r_0$ from first principles, singlet-channel $V_{\mathrm{SR}}^{(s)}(r)$ and virtual-state energy, and low-energy phase shifts.
**Dependencies:** CONJ-SS-11 (SS-5 cascade formula), SS-2 (nucleon structure geometry).
**Current best lead:** SS-6 v0.1 PROP-SS-6-2 gives the zero-range Bethe-Peierls relation $a_{np} \approx 1/\kappa = 4.32$ fm from $B_d$ alone ($-20\%$ vs observed 5.425 fm). Finite-range correction closes the gap in the correct direction but requires $V_{\mathrm{SR}}(r)$ shape.
**Paper(s):** SS-6 v0.1 registers the problem; derivation remains future work.
**Registered:** 18 April 2026

---

### OPEN-SS-21: Deuteron Orbital Wavefunction from CPP Framework
**Status:** OPEN
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM
**One-line statement:** Derive the deuteron relative-motion wavefunction $\psi_{np}(r)$ connecting the bipyramid core at $r \lesssim 1$ fm to the orbital extension at $r \sim 2$-$4$ fm.
**What a solution looks like:** Multi-scale wavefunction prediction yielding: $r_d$ and $r_c$ from $\langle r_{np}^2 \rangle$; $P_D$ from $|w(r)|^2$ integrated weight; $Q_d$ from standard quadrupole integrals including both intrinsic bipyramid contribution (oblate, $-0.22$ fm$^2$) and orbital D-wave contribution (prolate, must dominate to produce observed $+0.286$ fm$^2$); $\mu_d$ via $P_D$-dependent magnetic-moment relation.
**Dependencies:** OPEN-SS-20 ($V_{\mathrm{SR}}(r)$ shape), standard scattering theory infrastructure.
**Current best lead:** SS-6 v0.1 establishes the problem: bipyramid core alone gives wrong-sign $Q_d$, confirming $Q_d$ is orbital-dominated. Conventional nuclear physics treats the orbital regime with NN potentials + Schrödinger equation; CPP needs an analog framework. The central unresolved question is how the K$_3$ collective mode extends from rigid contact to finite inter-nucleon separation compatible with the observed orbital size ($r_d \sim 2$ fm, $\langle r_{np}^2 \rangle^{1/2} \sim 4$ fm, $1/\kappa = 4.32$ fm).
**Paper(s):** SS-6 v0.1 registers the problem; derivation remains future work.
**Registered:** 18 April 2026

---

## Propositions registered from SS-6 v0.1 (18 April 2026)

### PROP-SS-6-1: Observed deuteron quadrupole $Q_d$ is orbital-dominated, not bipyramid-dominated
**Status:** SUPPORTED by explicit calculation (SS-6 v0.1 Finding 4.1)
**Sector(s):** SS
**One-line statement:** The rigid base-to-base bipyramid's intrinsic quadrupole moment is $Q_d^{\mathrm{int}} = -0.22$ fm$^2$ (oblate); the observed $Q_d = +0.286$ fm$^2$ (prolate) therefore cannot arise from the bipyramid core alone and must be dominated by the orbital D-wave wavefunction at $r \gtrsim 2$ fm.
**What confirms it:** SS-6 v0.1 §4.1 explicit geometric calculation placing the three net-$+1/3$ charges in the equatorial contact plane at SS-2 edge lengths ($r_{uu}=1.07$ fm, $r_{ud}=0.62$ fm) with neutral-polarity apices along the axis; gives $Q_d^{\mathrm{int}} = -1/3 \cdot [r_{uu}^2/2 + y_3^2] = -0.224$ fm$^2$.
**Implication:** Quantitative CPP prediction of $Q_d$ requires OPEN-SS-21 (orbital wavefunction), not bipyramid geometry alone.
**Registered:** 18 April 2026

---

### PROP-SS-6-2: Zero-range Bethe-Peierls relation gives $a_{np} = 1/\kappa = 4.32$ fm from $B_d$ input alone
**Status:** DERIVED (standard Bethe-Peierls); $-20\%$ agreement with measured $a_{np} = 5.425$ fm
**Sector(s):** SS
**One-line statement:** Using $\Bd = 2.2246$ MeV and $\kappa = \sqrt{2\mu \Bd}/\hbar c = 0.2316$ fm$^{-1}$, the zero-range limit of the effective-range expansion gives $a_{np}^{(0)} = 1/\kappa = 4.318$ fm.
**What confirms it:** Standard two-body scattering theory applied to a loosely-bound state with the observed $\Bd$ as input. No CPP-specific structure required.
**Implication:** CPP's path to a precision $a_{np}$ prediction must supply the finite-range correction via $V_{\mathrm{SR}}(r)$ shape (OPEN-SS-20). The $20\%$ residual measures the distance CPP has to travel beyond zero range.
**Registered:** 18 April 2026

---

## Conjectures and Propositions registered from SS-7 (20-21 April 2026)

### CONJ-SS-12: Alpha-Polytope Edge Formula
**Status:** CONJECTURE — empirically supported by 12 concurrent zero-parameter predictions + 5 hostile-geometry stress tests
**Sector(s):** SS
**One-line statement:** For strict $N{=}Z$ alpha-chain nuclei at $N_\alpha \in [3, 14]$, the binding energy is $B(N_\alpha) = N_\alpha \Balpha + (3N_\alpha - 6) B_{\text{pair}}$ where $\Balpha = 28.296$ MeV (${}^4$He binding, from SS-5), $B_{\text{pair}} = M_0/\varphi = 2.342$ MeV (SS-5 nucleon-pair binding quantum), and $3N_\alpha - 6$ is Euler's edge count for any simplicial convex polytope on $N_\alpha$ vertices.
**What confirms it:** SS-7 v1.2 Table 1 — all twelve predictions within $\pm 1.5\%$ of AME 2020 experimental values; RMS $0.80\%$ across all twelve, $0.91\%$ across the primary set at $N_\alpha \in [3, 10]$. ${}^8$Be's 92 keV unboundness re-derived in-formula from the degenerate $N_\alpha = 2$ ($E = 0$) case plus Coulomb at $R_{\alpha\alpha} = 2.37$ fm. Five hostile-geometry stress tests (cube, square antiprism, wheel-like, monocapped antiprism, pentagonal antiprism) all underperform the simplicial $3N_\alpha - 6$ rule at fixed $(\Balpha, B_{\text{pair}})$.
**Dependencies:** PROP-SS-7-1 (simplicial polytope hypothesis, C4); SS-5 constants; ${}^4$He binding.
**Implication:** Resolves OPEN-SS-18 for the strict $N{=}Z$ alpha-chain at $N_\alpha \in [3, 14]$. Further status upgrade to THEOREM would require resolution of OPEN-SS-24 (first-principles derivation of C4).
**Paper(s):** SS-7 v1.2 (primary); SS-7 v1.0/v1.1 (registered at 8 nuclei; extended to 12 in v1.2).
**Registered:** 20 April 2026 in SS-7 v1.0; support strengthened 21 April 2026 in SS-7 v1.2 (12 predictions rather than 8, extended domain through ${}^{56}$Ni).

---

### PROP-SS-7-1: Alpha Clusters Realize Simplicial Convex 3-Polytopes
**Status:** SUPPORTED — empirically by SS-7 v1.2 Table 1 agreement (12 concurrent zero-parameter matches) and 5 hostile-geometry stress tests; derivation from CPP primitives deferred to OPEN-SS-24
**Sector(s):** SS
**One-line statement:** In strict $N{=}Z$ alpha-chain nuclei with $N_\alpha \in [3, 14]$, the $N_\alpha$ alpha clusters arrange as the vertices of a convex, triangular-faced, simplicial 3-polytope. Each edge of the polytope is one alpha-alpha base-to-base K$_3$ contact, contributing one $B_{\text{pair}} = M_0/\varphi$ quantum.
**What confirms it:** SS-7 v1.2 §6.5 hostile-geometry stress tests — the simplicial edge count $3N_\alpha - 6$ outperforms every plausible lower-edge alternative tested, at fixed $(\Balpha, B_{\text{pair}})$. ${}^{36}$Ar is the single-edge-sensitivity diagnostic: dropping $E$ by 1 degrades agreement from $-0.94\%$ to $-1.70\%$, matching one $B_{\text{pair}}$ quantum.
**Does not assert:** which specific simplicial polytope is realized at each $N_\alpha$ (Remark 2.2 in SS-7). The formula depends only on edge count, not polytope identity — ${}^{24}$Mg could be an octahedron or a triangular antiprism (both 12 edges at $N_\alpha = 6$); SS-7 does not distinguish.
**Implication:** C4 assumption of SS-7 is empirically supported but not derived. OPEN-SS-24 targets the first-principles derivation from CPP lattice geometry.
**Paper(s):** SS-7 v1.2 (§2.1 assumption C4; §6.5 empirical test). SS-9 candidate will target derivation.
**Registered:** 20 April 2026 in SS-7 v1.0; empirical support extended 21 April 2026 in SS-7 v1.2.

---

## Propositions registered from SS-5 (17 April 2026)

[Historical note: PROP-SS-5-2 (base-to-base predominant) and PROP-SS-5-3 (⁵He, ⁵Li, ⁸Be unbound) were registered with the SS-5 v0.2 / v3 session on 17 April 2026. Both remain SUPPORTED / CONFIRMED in v6. See SS-5 v6 §2.1 and §6 respectively.]

---

## Standard Model Emergence (SM) — 11 problems

### OPEN-SM-3: Derive ε = −0.145 from Lattice Geometry
**Status:** OPEN
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** Derive the perturbative correction ε from multi-layer averaging, entropy weighting, and holographic damping.
**What a solution looks like:** Explicit computation of ε from 600-cell geometry extending α_EM precision.
**Dependencies:** Independent of OPEN-SS-9 (topological δ=1/3 does not use ε)
**Cross-sector connections:** α_EM precision beyond 4 digits
**Current best lead:** Multi-layer entropy average over generations; sign issue identified in α_EM series.
**Paper(s):** SM Paper 2
**Last updated:** 23 March 2026

---

### OPEN-SM-4: Formalise the Capotauro Mechanism
**Status:** OPEN
**Sector(s):** SM, SR
**Priority:** HIGH
**One-line statement:** Derive the lattice chirality-activation event that establishes χ ≈ φ⁻¹ and produces CP violation.
**What a solution looks like:** Symmetry breaking [600-cell] × ℤ₂ → [600-cell]; derive χ = φ⁻¹; reproduce δ_CP ≈ 195°, sin²θ₁₃ ≈ 0.022, and baryon asymmetry.
**Dependencies:** None blocking (but requires EW development)
**Cross-sector connections:** OPEN-SM-5 (PMNS), matter-antimatter asymmetry, cosmology
**Current best lead:** δ_CP ≈ 195° matches NuFIT; mechanism physically motivated but not formalised.
**Paper(s):** SM Paper 2 Appendix H
**Last updated:** 23 March 2026

---

### OPEN-SM-5: PMNS Mixing Angles — Analytic Derivation
**Status:** OPEN
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** Derive PMNS mixing angles analytically from 600-cell subgroup overlaps.
**What a solution looks like:** Exact overlap fractions |G_i ∩ G_j|/|G_i| for all pairs, with normalisation derived (not fitted), matching NuFIT to 3–4 digits.
**Dependencies:** OPEN-SM-4 (Capotauro — needed for θ₁₃ and δ_CP)
**Cross-sector connections:** OPEN-G-1, lepton series
**Current best lead:** MC results match NuFIT to 3–4 digits; normalisation currently fitted. Subgroup overlap analysis: sin²θ₁₂ = 12/40 = 0.300, sin²θ₂₃ = 12/21 ≈ 0.571.
**Paper(s):** SM Paper 2
**Last updated:** 23 March 2026

---

### OPEN-SM-5b: Lepton Mass Mechanism
**Status:** OPEN
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** Derive charged lepton masses from CPP ZBW dynamics and show Koide relation follows.
**What a solution looks like:** Mass-radius relationship that reproduces m_e, m_μ, m_τ from cage geometry.
**Dependencies:** OPEN-SM-7 (Koide relation), OPEN-SM-7d (Koide phase)
**Cross-sector connections:** Lepton series paper (blocked until resolved)
**Current best lead:** ZBW eigenmode calculation (24 March 2026) gives wrong hierarchy (m_μ/m_e ≈ 965 vs observed 207). Root cause: electron cage radius ~1000× larger than muon cage.
**Paper(s):** Lepton series (planned)
**Last updated:** 24 March 2026

---

### OPEN-SM-6: Cosmological Constant from CPP Vacuum
**Status:** OPEN
**Sector(s):** SM, SR
**Priority:** MEDIUM
**One-line statement:** Derive Λ_obs ≈ 10⁻⁵² m⁻² from DP Sea dynamics, explaining 10⁻¹²⁰ suppression.
**What a solution looks like:** Paired DP cancellation mechanism giving ρ_Λ ∝ E_Planck⁴ × (l_P/R_universe)².
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-SR-5 (same problem from GR perspective)
**Current best lead:** Pairing cancellation approach gives ~10⁻¹¹ MeV⁴ (within order of magnitude). Far better than σ=120⁻⁴ approach (~10⁻⁹).
**Paper(s):** SM Paper 2, GR companion
**Last updated:** 23 March 2026

---

### OPEN-SM-7: Derive K = 2/3 (Koide Relation)
**Status:** OPEN (PARTIAL — K3 spectral theorem proved given two postulates)
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** Prove the Koide relation K = 2/3 from CPP first principles.
**What a solution looks like:** Close OPEN-SM-7a (prove H-1) and OPEN-SM-7b (prove ZBW-1).
**Dependencies:** OPEN-SM-7a, OPEN-SM-7b (the two remaining postulates)
**Cross-sector connections:** Charge quantisation (δ=1/3) and Koide (K=2/3) share the same K₃ source
**Current best lead:** K3 spectral theorem: ρ = √(λ_max/|λ_min|) = √2 → K = 2/3. Proved algebraically. Two postulates remain open.
**Paper(s):** k3_spectral_theorem.tex
**Last updated:** 24 March 2026

---

### OPEN-SM-7d: Derive the Koide Phase θ
**Status:** OPEN (structural impossibility proved for K3+SSV; θ is electroweak)
**Sector(s):** SM, EW
**Priority:** HIGH
**One-line statement:** Derive θ_Koide = 132.7323° from CPP, explaining Δθ = 2.267° below 3π/4.
**What a solution looks like:** Identification of the EW mechanism that breaks antibonding degeneracy.
**Dependencies:** CONJ-EW-1 (Weinberg angle), CONJ-SM-6 (conditional theorem)
**Cross-sector connections:** Gates Paper 4 individual mass predictions
**Current best lead:** CONJ-SM-6 gives cos(θ) = −(2+ε)/3 with ε = 2sin²θ_W/(z+1), matching PDG to 0.003%. Conditional on CONJ-EW-1. All 11 cage-geometry candidates FALSIFIED (Sessions B–K).
**Paper(s):** Paper 4 (planned)
**Last updated:** 1 April 2026

---

### OPEN-SM-7e: Why Exactly Three Lepton Generations?
**Status:** OPEN
**Sector(s):** SM
**Priority:** MEDIUM
**One-line statement:** Derive N=3 (K₃ base vertices) from CPP, explaining why 600-cell produces tetrahedra.
**What a solution looks like:** Show tetrahedral cells are the unique structure compatible with CPP interaction rules.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-G-1, OPEN-SS-2
**Current best lead:** K(K_N) = (N+1)/(2N); only N=3 gives 2/3. Why tetrahedra (not cubes) in 600-cell is the deeper question.
**Paper(s):** Paper 3 (K3 theorem)
**Last updated:** 24 March 2026

---

### OPEN-SM-10-FEM: First-Principles Quark Mass from FEM Simulation
**Status:** OPEN
**Sector(s):** SM, SS
**Priority:** #1 forward project
**One-line statement:** Derive V^(7/3) scaling from explicit DP chain dynamics via GPU FEM simulation.
**What a solution looks like:** DP count ratios matching PDG mass ratios to <5% without calibration.
**Dependencies:** SM-8 (cage hierarchy), SM-9 (pair model)
**Cross-sector connections:** OPEN-SS-1 (quark mass formula)
**Current best lead:** GPU FEM: place cage CPs, fill DP Sea, let CPs seek targets, count organised DPs. Cascade (s,c,b) + relay (top) regimes.
**Paper(s):** SM-10 (proposal stage)
**Last updated:** 9 April 2026

---

### OPEN-SM-cage-1: Derive Scaling Exponent α = 2.38
**Status:** OPEN
**Sector(s):** SM
**Priority:** HIGH
**One-line statement:** Derive α = 2.38 (or 7/3) from 600-cell geometry for the V^α cage mass scaling.
**Dependencies:** OPEN-SM-10-FEM
**Cross-sector connections:** OPEN-SS-1
**Current best lead:** CONJ-SM9-1 proposes α = 7/3 from V² × V^(1/3) (pair counting × linear cage dimension).
**Paper(s):** SM-9
**Last updated:** 9 April 2026

---

### OPEN-SD-lattice-scale: CPP Lattice-to-SI Conversion Constant
**Status:** OPEN
**Sector(s):** SD, GLOBAL
**Priority:** #1 (foundational — blocks experimental scrutiny)
**One-line statement:** Determine 1 CPP lattice unit (circumradius) = ? fm.
**What a solution looks like:** 5 routes explored; 3 converge at l_unit ≈ 0.59 fm. Need definitive derivation.
**Dependencies:** None blocking
**Cross-sector connections:** All spatially resolved observables
**Current best lead:** Three independent routes converging at l_unit ≈ 0.59 fm.
**Paper(s):** New
**Last updated:** 10 April 2026

---

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

## Quantum Mechanics (QM) — 5 problems

### OPEN-QM-1: Born Rule from CPP Statistics
**Status:** OPEN
**Sector(s):** QM
**Priority:** HIGHEST
**One-line statement:** Prove P(i) = |⟨ψ_i|ψ⟩|² — specifically the square, not another power.
**What a solution looks like:** Derivation from ZBW phase averaging giving exactly the squared amplitude.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-SM-7b (ZBW-1 postulate is a special case)
**Current best lead:** Mechanism identified (DI-bit processing rate ∝ |ψ|²); exact derivation not complete.
**Paper(s):** QM-5
**Last updated:** 23 March 2026

---

### OPEN-QM-3: Spin-½ and Pauli Exclusion from Cage Geometry
**Status:** OPEN
**Sector(s):** QM
**Priority:** HIGH
**One-line statement:** Derive s = 1/2 from ZBW orbital topology; derive Pauli exclusion from hDP chain antisymmetry.
**Dependencies:** None blocking
**Cross-sector connections:** Connects to 2:1 ZBW frequency ratio (candidate postulate P-SS-1)
**Paper(s):** QM-6, QM-7
**Last updated:** 23 March 2026

---

### OPEN-QM-5: Entanglement Decoherence Threshold at ~10¹⁵ eV
**Status:** OPEN
**Sector(s):** QM
**Priority:** MEDIUM
**One-line statement:** Derive E_thresh from Nexus lattice path limits.
**Dependencies:** None blocking
**Cross-sector connections:** Falsifiable prediction
**Paper(s):** QM-4
**Last updated:** 23 March 2026

---

### OPEN-QM-6: Discrete Spectra Deviations at ~10¹⁰ Hz
**Status:** OPEN
**Sector(s):** QM
**Priority:** MEDIUM
**One-line statement:** Compute exact δE_n corrections from 600-cell lattice discreteness.
**Dependencies:** None blocking
**Cross-sector connections:** Falsifiable prediction at accessible frequencies
**Paper(s):** QM-2
**Last updated:** 23 March 2026

---

### OPEN-QM-7: QFT Second Quantisation from Multi-CP Lattice Excitations
**Status:** OPEN
**Sector(s):** QM
**Priority:** MEDIUM
**One-line statement:** Derive field operators, Fock space, creation/annihilation operators from 600-cell normal modes.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-G-2 (formal QFT framework)
**Paper(s):** QM-6, QM-7
**Last updated:** 23 March 2026

---

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
**Dependencies:** OPEN-SR-3
**Cross-sector connections:** OPEN-SM-6 (will be same theorem when solved)
**Paper(s):** GR companion
**Last updated:** 23 March 2026

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

## Foundations / Superdeterminism (SD) — 5 problems

### OPEN-SD-1: Explicit K₀(λ) from Single-CP Integral
**Status:** OPEN
**Sector(s):** SD
**Priority:** HIGH
**One-line statement:** Derive closed-form CPP kernel K₀ (the Feynman propagator equivalent) from SSV field integral.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-SD-2, OPEN-SD-3
**Paper(s):** SD-1, SD-2
**Last updated:** 23 March 2026

---

### OPEN-SD-2: Non-Perturbative Interpolation Proof
**Status:** OPEN
**Sector(s):** SD
**Priority:** HIGH
**One-line statement:** Prove CPP DP Sea update rule interpolates smoothly between QM and classical limits.
**Dependencies:** OPEN-SD-1
**Cross-sector connections:** Validates CPP as complete theory for all field strengths
**Paper(s):** SD-3
**Last updated:** 23 March 2026

---

### OPEN-SD-3: Amplitudes A₅ = φ⁻³/(2π) and A₃/A₅
**Status:** OPEN
**Sector(s):** SD
**Priority:** HIGH
**One-line statement:** Derive icosahedral/tetrahedral amplitude ratio from first principles.
**Dependencies:** OPEN-SD-1, OPEN-SD-2
**Cross-sector connections:** Replaces QFT coupling constants
**Paper(s):** SD-2, SD-3
**Last updated:** 23 March 2026

---

### OPEN-SD-4: Many-Body K for Entangled Multi-Qubit States
**Status:** OPEN
**Sector(s):** SD
**Priority:** MEDIUM
**One-line statement:** Extend single-qubit K to tensor product of entangled states; show Bell violations.
**Dependencies:** OPEN-SD-1, OPEN-SD-2
**Cross-sector connections:** Quantum non-locality interpretation
**Paper(s):** SD-4, SD-5
**Last updated:** 23 March 2026

---

### OPEN-SD-5: Apparatus DP Sea Anisotropy δ₀ from SSV
**Status:** OPEN
**Sector(s):** SD
**Priority:** MEDIUM
**One-line statement:** Derive the measurement-induced anisotropy parameter from apparatus SSV field.
**Dependencies:** OPEN-SD-1
**Cross-sector connections:** Completes CPP measurement theory
**Paper(s):** SD-5
**Last updated:** 23 March 2026

---

## Cross-Series (GLOBAL) — 2 problems

### OPEN-G-1: Three SM Generations — Quarks and Leptons Unified
**Status:** OPEN
**Sector(s):** GLOBAL
**Priority:** HIGHEST
**One-line statement:** Prove 600-cell forces exactly three generations of both quarks and leptons from a single principle.
**Dependencies:** OPEN-SS-2, OPEN-SM-7e
**Cross-sector connections:** Every sector; capstone structural result
**Paper(s):** Cross-series
**Last updated:** 23 March 2026

---

### OPEN-G-2: Full Standard Model from Single 600-Cell
**Status:** OPEN
**Sector(s):** GLOBAL
**Priority:** HIGHEST (capstone)
**One-line statement:** All gauge groups, all masses, all couplings, CKM matrix from one geometric object + sea_strength (now derived).
**Dependencies:** Essentially all other open problems
**Cross-sector connections:** Everything
**Current best lead:** SU(3)_c, SU(2)_L × U(1)_Y derived; sea_strength derived; sin²θ_W = 3/(8φ) conjectured; Koide K=2/3 proved; δ=1/3 proved; quark ordering proved. Mass formula, hierarchy problem, and mixing angles remain.
**Paper(s):** All series
**Last updated:** 23 March 2026

---

## Workflow / Infrastructure (WORKFLOW) — 1 problem

### OPEN-WORKFLOW-1: Consolidate All Bibliography Files
**Status:** OPEN
**Sector(s):** Infrastructure
**Priority:** MEDIUM
**One-line statement:** Merge all 12 per-paper and per-series `.bib` files into `bibliography/cpp_references.bib` as the single master bibliography; update old paper `.tex` files to reference it.
**What a solution looks like:** (1) Audit all 245 existing entries across 12 files; (2) resolve 22 known citation-key collisions (different content with same key); (3) merge 113 unique entries into master; (4) update `\bibliography{}` commands in all existing paper `.tex` files to reference master only; (5) move legacy `.bib` files to `archive/pre_consolidation_2026-04-15/`; (6) verify all papers still compile with same citation output.
**Tractability:** 1 dedicated session (2–3 hours of focused collision resolution and compile verification)
**What was done (15 April 2026):** Policy declared — master file is single source of truth; new papers cite master only; legacy files frozen with deprecation headers. SS-3 bibliography entries (cpp_ss3, humphreys1972) added to master. Stale `cpp_ss3` key in strong-series bibs renamed to `cpp_ss3_old_gluons` to free the namespace.
**Paper(s):** None (infrastructure)
**Last updated:** 15 April 2026

---

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
**Status:** CONJECTURE
**Sector(s):** SM
**Priority:** MEDIUM
**One-line statement:** Derive Δm² from 600-cell suppression formula.
**Dependencies:** Paper 6 (planned)
**Registered:** March 2026

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

### CONJ-P-SS-1 (Candidate Postulate): 2:1 ZBW Orbital Frequency Ratio
**Status:** PROPOSED POSTULATE
**Sector(s):** SS, QM
**One-line statement:** All fermions have inner orbital oscillating at 2× outer frequency. Used implicitly in SS-1; not formally stated or derived.
**Current best lead:** Consistent with spin-½ requirement and SR-1 treatment. Recommend elevating to CPP Postulate P-5a.
**Registered:** 29 March 2026

---

### SC-6: φ¹¹ and φ¹⁷ Lepton Mass Ratio Exponents
**Status:** CONJECTURE (empirical observation)
**Sector(s):** SM
**One-line statement:** m_μ/m_e ≈ φ¹¹ (3.8%), m_τ/m_e ≈ φ¹⁷ (2.7%). Exponents: 11 = z−1, 17 = z+5.
**Dependencies:** Geometric derivation from coordination structure
**Registered:** 24 March 2026

---

# §3 — Propositions In Progress (PROP)

Physically motivated claims with partial demonstration. See `propositions.md` for the full tiered register.

---

### PROP-SS-5-1: Diproton and Dineutron Unbound by Open-Vertex Polarity Mismatch (TIER 1)
**Status:** REFINED by SS-5 v0.2 — the uniform-polarity argument is replaced by the base-to-base K$_3$ charge-misalignment argument, which more accurately accommodates the empirical near-bound ${}^{1}S_{0}$ virtual states at $+66$ keV (pp) and $+118$ keV (nn). pp and nn remain unbound as the virtual states sit above threshold.
**Sector(s):** SS (nuclear physics)
**One-line statement:** Two protons or two neutrons cannot form a bound deuteron-like state due to charge-misaligned K$_3$ contact structure (rotational realignment gives at most 1 of 3 attractive pairs, net near-zero binding).
**Evidence:** No bound diproton state; no bound dineutron state. Near-bound virtual states observed in $^{1}S_{0}$ scattering.
**Dependencies:** SS-2, SS-5 v0.2 base-to-base mechanism
**Paper(s):** SS-5 v0.1 §2.3 (original argument); SS-5 v0.2 §8 (refined argument)
**Registered:** 16 April 2026; refined 17 April 2026

---

### PROP-SS-5-2: Base-to-Base Configuration Predominant in Deuteron Ground State (TIER 1)
**Status:** SUPPORTED by empirical extensibility (cascade to $A \geq 3$ requires outward open vertices) and quantitative match (BB gives +5.3% vs VV +36%)
**Sector(s):** SS (nuclear physics)
**One-line statement:** In the deuteron ground state, the two nucleons arrange base-to-base with triangular quark faces in contact and open vertices pointing outward. The vertex-to-vertex alternative is energetically excluded at the >30% level.
**Evidence:** (1) cascade extensibility to bound $^3$H, $^3$He, $^4$He requires outward open vertices; (2) numerical match $B_d = M_0/\varphi = 2.342$ MeV ($+5.3\%$) vs VV calculation $3.02$ MeV ($+36\%$); (3) absence of racemic-mixture signature in scattering cross-sections.
**Dependencies:** SS-2, SS-5 v0.2
**Paper(s):** SS-5 v0.2 §2 (17 April 2026)
**Registered:** 17 April 2026

---

### PROP-SS-5-3: $^5$He, $^5$Li, $^8$Be Unbound by Closed-Polytope Gap (TIER 1)
**Status:** SUPPORTED — all three predictions confirmed empirically
**Sector(s):** SS (nuclear physics)
**One-line statement:** The absence of a closed polytope at $A=5$ and the cage-separation at $A=8$ predict $^5$He, $^5$Li, $^8$Be unbound. Measured: $S_n(^5$He$) = -0.89$ MeV; $S_p(^5$Li$) = -1.97$ MeV; $S_{^4He}(^8$Be$) = -0.092$ MeV (famous 92-keV triple-alpha bottleneck).
**Evidence:** Direct measurement. All three nuclei are empirically unbound at the level predicted by CPP's closed-polytope structure.
**Dependencies:** SS-5 v0.2 cascade formula; geometric fact that 600-cell has no closed 5-vertex or 8-vertex polytope at the nucleon scale.
**Paper(s):** SS-5 v0.2 §6 (17 April 2026)
**Registered:** 17 April 2026

---

### PROP-3: Tetrahedral Cage as Unique Minimum Stable Cage (TIER 2)
**Status:** PROOF-COMPLETE, FORMALISATION PENDING
**Sector(s):** SS
**One-line statement:** N=4 tetrahedron is the unique cage satisfying both energetic stability and geometric completeness. N=12 icosahedron is unbound (+16.5 SSV₀/r_c).

### PROP-1: Random Walk / Quantum Uncertainty (TIER 3)
**Status:** NEEDS QUANTITATIVE VERIFICATION
**Sector(s):** QM
**One-line statement:** Central CP random walk RMS → Compton wavelength. Would derive ℏ from CPP statistics.

### PROP-2: Solitonic Tunneling (TIER 3)
**Status:** NEEDS QUANTITATIVE VERIFICATION
**Sector(s):** QM
**One-line statement:** Tunneling from rogue-wave SSV_net spike statistics. Must reproduce WKB exp(−2κd).

### PROP-4: Elastic Tunneling via Cage Dissolution (TIER 3)
**Status:** NEEDS QUANTITATIVE VERIFICATION
**Sector(s):** QM
**One-line statement:** Cage dissolves isotropically (no photon); reforms on far side. Photon absence confirmed.

### PROP-5: Radial DP Chain Equilibrium Length (TIER 3)
**Status:** COMPUTED 30 March 2026 — r_chain ≠ r_e; now corollary of α_fine derivation
**Sector(s):** QM, EW
**One-line statement:** r_chain = d_Sea/√sea_strength. Result: r_e = α_fine × ℏc/(2·SSV₀) exactly.

### PROP-6 through PROP-15 (TIER 4 — Candidate Mechanisms)
**Status:** Physically motivated narratives without quantitative verification. See `propositions.md` for full descriptions.

Items: PROP-6 (de Broglie λ from chain compaction), PROP-7 (cage reformation from Sea), PROP-8 (dual −eCP configurations), PROP-9 (atomic orbitals as DP chain standing waves), PROP-10 (electron identity transfer / Born rule), PROP-11 (virtual particles / Gauss's law), PROP-12 (critical separation r_crit), PROP-13 (photon pair production), PROP-14 (mass as thermodynamic boundary), PROP-15 (pair annihilation ortho:para ratio).

---

# §4 — Recently Resolved (THEO)

Kept here for one cycle, then moved to §5.

---

### THEO-SS-9 → OPEN-SS-9: δ = 1/3 Proved (C₃ + Cage Completeness)
**Resolved:** 29 March 2026
**Resolving paper:** SM-1 Theorem 1 (v6)
**Resolved by:** Thomas Lee Abshier ND, Claude Sonnet, Grok
**Summary:** Topological proof: C₃ symmetry forces δ₁ = δ₂ = δ₃; cage completeness forces δ₁+δ₂+δ₃ = 1; therefore δ = 1/3 exactly. Corollary: q_up = +2/3, q_down = −1/3. Integral approach (δ ≈ φ⁻² ≈ 0.382) superseded.

### THEO-SM-1 → OPEN-SM-1: k_SM Derived from 600-Cell Voronoi
**Resolved:** 23 March 2026
**Resolving expression:** k_SM = α_geom/(12φ²) ≈ 0.017805
**Summary:** α_geom = 3(11+5√5)√(5+√5)/320 ≈ 0.55936 from Voronoi stiffness integral. 3.8% residual = stereographic projection correction. Same α_geom appears in SR coupling.

### THEO-SM-2 → OPEN-SM-2: sea_strength = 10 × k_SM
**Resolved:** 23 March 2026
**Resolving expression:** sea_strength = (N_lattice/z) × k_SM = (120/12) × k_SM = 10 × k_SM ≈ 0.17805
**Summary:** Factor of 10 = total vertices / coordination number. Exact geometric ratio. Coupling sector has zero free parameters.

### THEO-QM-2 → OPEN-QM-2: Schrödinger Equation Derived
**Resolved:** 31 March 2026
**Resolving paper:** QM-1 (cpp2040a_v31.tex), THEO-QM-1
**Summary:** Complex DI-bit hopping approach gives exact Schrödinger equation in continuum limit.

### THEO-QM-4 → OPEN-QM-4: Decoherence Timescale
**Resolved:** 31 March 2026 (effectively)
**Resolving papers:** QM-4 THEO-QM-6 (Lindblad) + SD-3 THEO-SD-6 (apparatus)
**Summary:** Single-qubit dephasing rate derived in QM-4; macroscopic decoherence time derived in SD-3.

### THEO-QM-new-9 → OPEN-QM-new-9: r_conf Inconsistency
**Resolved:** 30 March 2026 (same session)
**Summary:** Mislabeling in SM-3 eq:hop_amp. All three constants correct; SM-3 assigned wrong name to computed value.

---

# §5 — Resolved Archive (THEO)

Complete list of all problems that became theorems.

| ID | Resolution | Date | Paper |
|---|---|---|---|
| THEO-SS-9 | δ = 1/3 from C₃ symmetry + cage completeness | 29 Mar 2026 | SM-1 Theorem 1 (v6) |
| THEO-SM-1 | k_SM = α_geom/(12φ²) | 23 Mar 2026 | SS-1 §8 + SR-1 companion |
| THEO-SM-2 | sea_strength = 10 × k_SM | 23 Mar 2026 | SS-1 §8 |
| THEO-QM-2 | Schrödinger equation from lattice dynamics | 31 Mar 2026 | QM-1 v3.1 |
| THEO-QM-4 | Decoherence timescale γ and τ_dec | 31 Mar 2026 | QM-4 + SD-3 |
| THEO-QM-new-9 | r_conf labeling error (not true inconsistency) | 30 Mar 2026 | SM-3 correction |

---

# §6 — Falsified (FALS)

Tested and found wrong. Never deleted. The record of what failed is as valuable as the final solution.

---

### FALS-C-SM-1: C₆₀ (60 Vertices) as Top Quark Cage
**Falsified:** March 2026 (PS-1 session)
**Why it fails:** No 60-vertex distance shell exists in the 600-cell.

### FALS-C-SM-2: φ^(3(l-1)) Quark Mass Scaling
**Falsified:** March 2026 (PS-1 session)
**Why it fails:** Actual shell volumes deviate by 3–8×. Volumes peak at equatorial shell, then decrease (palindromic structure).

### FALS-C-SM-3: AB Loop as Origin of θ_Koide
**Falsified:** Session F (25 March 2026)
**Why it fails:** C₃ symmetry prevents chiral preference on K₃; numerics also fail.

### FALS-C-SM-4: 4D 600-Cell Embedding Breaks C₃ for θ
**Falsified:** Session G (25 March 2026)
**Why it fails:** All 600 tetrahedral cells computed; C₃ preserved exactly in 4D.

### FALS-C-SM-5: Self-Consistent ZBW Mass Feedback Selects θ
**Falsified:** Session L
**Why it fails:** Fixed-point iteration converges to θ = 180° (trivial), not 132.73°.

### FALS-C-SM-6: Löwdin Downfolding (K₄→K₃) Breaks Antibonding Degeneracy
**Falsified:** Session E (24 March 2026)
**Why it fails:** V₄ is dark to antibonding modes; ⟨φ₋|v⟩ = 0 exactly.

### FALS-SC-1 (partial): Hybrid Quark Mass Ladder
**Falsified:** 30 March 2026
**Why it fails:** Top quark mass cannot come from C_n × N_l (103× discrepancy). C_n confirmed as real geometric quantities; formula architecture needs fundamental rethinking for top quark.

---

# §7 — Recommended Attack Order

Ordered by: fewest prerequisites, most tractable, highest leverage on downstream problems.

| Rank | ID | Why | Tractability |
|------|-----|------|-------------|
| ~~1~~ | ~~OPEN-SS-11~~ | ~~Pure group theory; 1–2 pages. Elevates SS-1 to necessity.~~ | ~~1 session~~ **RESOLVED → THEO-SS-10** |
| 1 | OPEN-SS-5 | One dimensional-analysis step. Prerequisite for 4 other problems. | 1 session |
| 2 | OPEN-SS-13 | WKB calculation; confirms C₃ proof mechanically. | 1 session |
| 3 | OPEN-SS-8 | Clear SU(6) + ZBW path. | 1–2 sessions |
| 4 | OPEN-SS-12 | Requires reading EW-2; high physical importance. | 2 sessions |
| 5 | OPEN-SS-1 | Mechanism established; find ZBW-frequency kernel. | Multi-session |
| 6 | OPEN-SS-27 | D2 derivation via A6' extension. Closure auto-delivers D1 under simplicial combinatorics (two-for-one). SS-8 v0.1 drafting target. | 2-3 sessions |
| 7 | OPEN-SD-1 | Resolves superdeterminism amplitude conjecture. | 2 sessions |
| 8 | CONJ-EW-1 | Gates CONJ-SM-6 (which gives θ to 0.003%). | Multi-session |
| 9 | OPEN-SS-3 | ZBW notebooks give starting point. | 2 sessions |
| 10 | OPEN-SM-10-FEM | #1 forward project; GPU implementation. | Multi-session |
| 11 | OPEN-SD-lattice-scale | Foundational; blocks experimental scrutiny. | 2 sessions |
| 12 | OPEN-EW-1 | Hardest single problem; requires new scaling argument. | Unknown |
| 13 | OPEN-G-1/G-2 | Capstone; emerges when sector problems converge. | Depends on all |

---

# §8 — Dependency Graph

```
SOLVED:
  THEO-SS-9 (δ=1/3) ✅ ──────────────────────────────► OPEN-G-2
  THEO-SM-1 (k_SM) ✅ ────────────────────────────────► OPEN-G-2
  THEO-SM-2 (sea_strength) ✅ ────────────────────────► OPEN-G-2
  THEO-QM-2 (Schrödinger) ✅
  THEO-QM-4 (decoherence) ✅

STRONG SECTOR:
  OPEN-SS-5 (σ) ────► OPEN-SS-7 (Λ_QCD) ────────────► OPEN-G-2
                ├──── OPEN-SS-10 (nuclear)
                ├──── OPEN-SS-6 (glueball)
                └──── OPEN-SS-14 (deconfinement T)
  OPEN-SS-1 (M_q) ──► OPEN-SS-3 (chiral) ───────────► OPEN-G-1
                 └──► OPEN-SS-2 (generations) ────────► OPEN-G-1
  OPEN-SS-11 (SU3 unique) ───────────────────────────► SS-1 Thm 1 (strengthens)
  OPEN-SS-12 (W bracelet) ───────────────────────────► OPEN-G-2
  OPEN-SS-8 (μ_N) ───────────────────────────────────► OPEN-G-2
  OPEN-SS-4 (β₁) ────────────────────────────────────► OPEN-G-2

ELECTROWEAK:
  CONJ-EW-1 (sin²θ_W) ──► CONJ-SM-6 (θ_Koide) ─────► OPEN-SM-7d
  OPEN-EW-1 (η) ─────────────────────────────────────► OPEN-G-2
  OPEN-EW-2 (masses) ──► OPEN-EW-4 (ratios) ─────────► OPEN-G-2

STANDARD MODEL:
  OPEN-SM-7 (K=2/3) ─► OPEN-SM-7d (θ) ──────────────► Lepton masses
  OPEN-SM-4 (Capotauro) ──► OPEN-SM-5 (PMNS) ───────► OPEN-G-2
  OPEN-SM-10-FEM ──► OPEN-SM-cage-1 (α=2.38) ────────► OPEN-SS-1

FOUNDATIONS:
  OPEN-SD-1 (K₀) ──► OPEN-SD-2 (interp.) ──► OPEN-SD-3 (A₅, A₃)

RELATIVITY:
  OPEN-SR-3 (SSV def) ──► OPEN-SR-1 (PSR) ──► OPEN-SR-4 (Einstein)
  OPEN-SR-2 (k) ──► OPEN-SR-1

CROSS-SERIES:
  OPEN-SD-lattice-scale ──────────────────────────────► All spatial predictions
```

---

# §9 — Problem Count Summary

| Sector | Total | Open | Conj | Prop | Resolved | Falsified |
|--------|-------|------|------|------|----------|-----------|
| SS (Strong) | 25 | 16 | 4 | 1 | 1 | 1 |
| SM (Standard Model) | 23 | 11 | 6 | 1 | 3 | 5 |
| EW (Electroweak) | 9 | 6 | 2 | 0 | 0 | 0 |
| QM (Quantum Mechanics) | 13 | 5 | 0 | 4 | 3 | 0 |
| SR (Relativity) | 8 | 8 | 0 | 0 | 0 | 0 |
| SD (Foundations) | 7 | 6 | 1 | 0 | 0 | 0 |
| GLOBAL | 2 | 2 | 0 | 0 | 0 | 0 |
| **Total** | **87** | **54** | **13** | **6** | **7** | **6** |

*(Note: Propositions counted only at Tier 2–3 level in this summary. Tier 4 items (10) grouped under PROP-6–15.)*

---

# §10 — Anomalies and Housekeeping Actions

The following issues were identified during the consolidation from `open_problems/` into this file and require action:

### Duplicate files (action: delete the stale copy)
1. **`open_problems/OP-EW/CONJ-SM-6_koide_phase.md`** — duplicate of `OP-SM/CONJ-SM-6_koide_phase.md`. The OP-SM copy has a dead-end correction the OP-EW copy lacks. **Keep OP-SM version; delete OP-EW copy.**
2. **`open_problems/OP-EW/CONJ-EW-1_weinberg_angle.md`** and **`CONJ-EW-1_weinberg_angle_zero_parameter.md`** — two versions of the same conjecture. The former (182 lines) is more complete. **Keep `weinberg_angle.md`; archive `zero_parameter.md`.**

### Misplaced files (action: move to correct location)
3. **`open_problems/OP-EW/development-EW-Weinberg-Koide-session-20260401.md`** — development transcript, not a problem file. **Move to `series_electroweak/development-transcripts/`.**
4. **`open_problems/OP-SS/OP-SS-1_quark_mass_ladder_ps1_analysis.md`** — a .tex paper, not an open problem. **Move to `series_strong/papers/`.**
5. **`open_problems/OPEN-P-SM-10-FEM.md`** — at root of open_problems instead of in OP-SM/. **Moot after archival; noted for record.**

### Naming convention (action: rename on Phase 5 archival)
6. All files in `open_problems/` use `OP-` or `OPEN-P-` prefixes. The new standard is `OPEN-`. Renaming will occur during Phase 5 (consolidation/archival), not now.

### Content absorbed from other files
7. **`propositions.md`** — Tier 1–3 items absorbed into §3 and §4. Tier 4 items referenced by group.
8. **`solution_candidates.md`** — SC-1 through SC-7 absorbed into relevant entries' "Current best lead" fields and the FALS section.
9. **Conjectures from `postulates_and_theorems.md`** — CONJ-SM-1 through CONJ-SM9-2, CONJ-EW-1, CONJ-EW-2, CONJ-SS-2-1 absorbed into §2.
10. **`open_problems/OP-SS/conjectures-SS.md`** — CJ-SS-1, CJ-SS-2, candidate postulate absorbed into §2.

---

*This file consolidates content from: `open_problems/` (63 files), `propositions.md`, `solution_candidates.md`, conjectures from `postulates_and_theorems.md`, and `open_problems/OP-SS/conjectures-SS.md`. No content has been deleted — all items are either in this file or referenced by it. The source files will be archived after verification (Phase 5).*

*Created 12 April 2026 during Phase 1 of the Research Frontier Architecture implementation.*
*Authors: Thomas Lee Abshier ND and Claude Opus (Anthropic).*
