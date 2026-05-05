# CPP Research Frontier

**Location:** `/CPP/Research_Frontier.md`
**Last updated:** 5 May 2026 (Session 16 Phase 4: anharmonic K$_3$ $\xi^4$ corrections in Gaussian expansion — first-order PT and all-orders Gaussian-average extension — RULED OUT via **sign theorem**: Taylor coefficient of $\xi^4$ is negative, $\langle \xi^4 \rangle_0 > 0$ in any harmonic ground state, so first-order shift is negative (more binding); empirical J-solid range needs positive shift (less binding than canonical K$_3$). Computation across all 8 polytopes confirms universal sign failure: $\Delta E^{(1)} < 0$ in all cases. The all-orders Gaussian-average extension (factor $\sim 0.59$ reduction of leading $\xi^4$ estimate, polytope-independent because $\langle s \rangle \approx 0.85$ near-constant across polytopes) preserves the negative sign — proven by **sign theorem**: $f(s) \equiv (1+s)^{-1/2} - 1 + s/2 > 0$ for all $s > 0$ (one-line proof: $f(0) = 0$, $f'(s) = (1/2)[1 - (1+s)^{-3/2}] > 0$, hence $f$ strictly increasing). Combined with Rayleigh–Ritz: true cluster ground state in full Gaussian Hamiltonian is provably *more* bound than harmonic estimate, never less. **Tenth programme-level negative result** in OPEN-SS-35 closure programme; fifth in OPEN-SS-32 ↔ U-shape thread. **Programme-level closure of Gaussian-K$_3$ framework at fixed cluster geometry**: Phase 3B-B (Session 15) closed harmonic-Hessian-belt-IRREP family at canonical $\sigma$; Phase 4 (this session) closes perturbative-correction family at canonical geometry. Together: entire Gaussian-K$_3$ framework at fixed cluster geometry cannot produce empirical U-shape — provably. U-shape mechanism must live in geometric-shift channels beyond R1 (R3 = N-dependent boundary conditions on $R_\alpha$, R4 = cluster shape distortion) or out-of-framework (inelastic excitations, surface shape, Coulomb arrangement). Sub-question (b) layer 3 gap-strength closure INDEPENDENT by Decoupling Theorem (Session 12), unaffected. Earlier 5 May 2026 Session 15 Phase 3B-B: full C$_n$ IRREP decomposition with three belt-IRREP variants RULED OUT via n-vs-N structural argument; **R2 FORMALLY CLOSED**; ninth programme-level negative result; both registered candidates for OPEN-SS-35 sub-question (a) A-scaling closure (R1 Session 12 + R2 Session 15) now ruled out)
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
**Status:** PARTIALLY RESOLVED by SS-8 v1.0 (25 April 2026) for $N_\text{ex} \in [2, 8]$, $N_\alpha \in [3, 14]$ even-even nuclei via the conditional 2E/V scaling law $\Delta_1(N_\alpha) = (6 - 12/N_\alpha) B_\text{pair}$. Remainder (odd-$A$ nuclei, $N_\alpha > 14$, partial-alpha substructures) remains OPEN.
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM (downgraded from HIGH after partial resolution)
**One-line statement:** Extend the SS-7 alpha-chain binding formula to non-$N{=}Z$ isotopes at alpha-chain $N_\alpha$ values, odd-$A$ nuclei with extra-nucleon-bound-to-alpha-core structures, and non-alpha-clustered nuclei.
**What a solution looks like:** A CPP derivation of the $\sim 2$ MeV per extra neutron signal visible in non-$N{=}Z$ isotopes (${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe each with $N - Z = +4$; ${}^{48}$Ca at $N - Z = +8$ as a stress test). A CPP treatment of single-nucleon excess bound to an alpha-polytope core (${}^7$Li, ${}^9$Be, ${}^{11}$B, ${}^{13}$C). A CPP treatment of partial-alpha substructures (${}^6$Li $\approx$ ${}^4$He + d, ${}^{14}$N, ${}^{18}$O, ${}^{30}$Si). Success criterion: the stability valley from ${}^{40}$K through ${}^{208}$Pb reproduced within CPP residual precision.
**Dependencies:** SS-7 v1.2 formula and constants (${}^4$He binding, $B_{\text{pair}} = M_0/\varphi$). CPP treatment of DP-sea behaviour in non-$N{=}Z$ configurations.
**Current best lead:** SS-8 v1.0 derives the conditional 2E/V scaling law for the even-$N_\alpha$ alpha-chain at $N_\text{ex} \in [2, 8]$ (42 conditional zero-parameter predictions; 11 of 12 primary $N_\text{ex} = 2$ rows within 15%, two within 1%). SS-8's residual model (H3′ pair bonus + H5′ small-polytope attenuation) provides a structural template for the remainder. Preliminary SS-7 inspection of ${}^6$Li: residual alpha-deuteron binding 1.47 MeV, approximately $2B_{\text{pair}}/3 \approx 1.56$ MeV — suggestive of an incomplete K$_3$ face at the alpha-d contact.
**Paper(s):** SS-8 v1.0 (primary partial resolution). SS-9 candidate for remainder.
**Registered:** 20 April 2026 in SS-7 v1.0; priority upgraded 21 April 2026 in SS-7 v1.2 to primary SS-8 target; partially resolved 25 April 2026 by SS-8 v1.0; remainder priority downgraded to MEDIUM 26 April 2026.

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
**Cross-link (4 May 2026 Session 12):** The OPEN-SS-25 screening mechanism was used as the candidate physical lever in OPEN-SS-35 sub-question (a) Resolution R1 (R$_\alpha$ scale-dependence as A-scaling closure), tested in Session 12 and **ruled out** on three independent grounds (sign of energetic compression vs required expansion; non-monotonic U-shape pattern that no monotonic $R_\alpha(A)$ law produces; Decoupling Theorem showing A-scaling closure does not affect layer-3 gap-strength deficit). **OPEN-SS-25 itself remains open** — Session 12 does not close it, as the screening mechanism's first-principles CPP derivation is a separate question from whether $R_\alpha$ varies with cluster size. The Session 12 finding instead establishes that DP-sea screening, *whatever its eventual first-principles form*, does not produce A-scaling closure for sub-question (a). See `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a_Ascaling_R1_RULED_OUT.md` §2.
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
**Paper(s):** SS-8 v1.0 (registered the conditional theorem and the Level-1/2/3 decomposition methodology). SS-9 candidate for closure of Level-3 gap.
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
**Paper(s):** Opened in SS-8 v1.0 (formal registry entry added 23 April 2026; SS-8 invoked D2 as a paper-level conditional theorem). Target paper: SS-9 candidate (shares structural-polytope machinery with OPEN-SS-24).
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
**Paper(s):** Opened in SS-8 v1.0 (D3 invoked as paper-level conditional theorem; residual decomposition presented as provisional, not part of the main proof). Target paper: SS-9 candidate or later.
**Registered:** 21 April 2026 in SS-8 H2' derivation note §10 (formal registry entry added 23 April 2026).

---

### OPEN-SS-29: Programme-Level Closure of C5 (Ground-State Energy Minimization)
**Status:** OPEN — registered as candidate, pending ratification (registered 26 April 2026 Session 2 in SS-9 Phase 1 v0.2 working draft scaffold)
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM-HIGH
**One-line statement:** Derive C5 (the bound alpha-cluster ground state minimizes total energy among physically realizable rigid-tetrahedral packing configurations) from CPP primitives A1–A11 without importing energy minimization as a structural assumption.
**What a solution looks like:** A CPP derivation establishing that the lattice-level dynamics of A1–A11 — Conscious Points executing the Polarize-Capture-Depolarize cycle on the 600-cell substrate — drives bound configurations to global energy minima rather than metastable local minima. Likely path: show that the SS-7 binding formula's edge-additivity ($B_{	ext{pair}}$ contributions add cleanly across edges, with no inter-face couplings beyond what C3's K₃ collective mode captures) is itself derivable from CPP primitives, at which point ground-state selection is a generic statistical-mechanics consequence.
**Dependencies:** SS-5 collective-mode machinery (A6' or its successor); the K₃ scale-recurrence (Pattern 6) status as forced-vs-permitted by A1–A11. Likely entanglement with OPEN-SS-27 (D2 derivation) since both reduce to A6' extension questions.
**Cross-sector connections:** A successful C5 closure would also strengthen the D2 (OPEN-SS-27) and D3 (OPEN-SS-28) closures by establishing that bulk averaging procedures reach genuine ground states, not provisional ones. Methodologically, a C5 closure that reduces to "Pattern 6 holds by construction" would be a substantial programme-level result clarifying the structural status of K₃ scale-recurrence across SS-3, SS-5, SS-7, SS-8.
**Current best lead:** SS-9 Phase 1 v0.2 working draft (`session_logs/OPEN-SS-24_phase1_v0.2_working_draft.md`) Lemma C uses C5 as a paper-level conditional. The Phase 4 attempt sketched in §9 of that draft anticipates that programme-level closure of C5 reduces to a Pattern 6 question. Phase 4 is not yet attempted.
**Falsification route:** Demonstration that CPP lattice dynamics permit metastable bound configurations that are not global energy minima at typical formation timescales; or demonstration that the SS-7 binding formula's edge-additivity itself fails at some derivable structural level.
**Paper(s):** SS-9 candidate (registered as paper-level conditional in Phase 1 working draft; programme-level closure target for Phase 4 or later session).
**Registered:** 26 April 2026 Session 2 in SS-9 Phase 1 v0.2 working draft §1 (formal registry entry pending ratification).

---

### OPEN-SS-30: Programme-Level Closure of C6 (Cluster Surface-Realization, No Interior Alphas)
**Status:** OPEN — registered as candidate, pending ratification (registered 26 April 2026 Session 2 in SS-9 Phase 1 v0.2 working draft scaffold)
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM
**One-line statement:** Derive C6 (in bound alpha-cluster ground states at $N_lpha \leq 14$, all alpha centroids lie on the boundary of the cluster's convex hull; no alpha is interior to the cluster) from CPP primitives A1–A11 via direct rigid-tetrahedral packing analysis.
**What a solution looks like:** A finite computational verification, executed at each $N_lpha$ from 4 through 14, showing that minimum-energy rigid-tetrahedral packings under C1+C2+C3 do not place any alpha interior to the convex hull. The verification is finite and tractable; either (a) direct enumeration of candidate configurations at each $N_lpha$, or (b) analytic argument from rigid-packing geometry that interior-alpha configurations are energetically dominated by surface-only configurations at all $N_lpha \leq 14$.
**Dependencies:** None blocking. The verification can proceed independently of OPEN-SS-29; both are required for unconditional closure of OPEN-SS-24, but they are functionally independent (geometric vs. energetic principles).
**Cross-sector connections:** Methodological — sets a precedent for finite computational verification of structural hypotheses in the strong sector. If C6 closes by direct enumeration at each $N_lpha$, the methodology generalizes to similar small-$N$ structural claims elsewhere in the programme.
**Current best lead:** Empirically supported by SS-7 Table 1 (12 strict-$N{=}Z$ alpha-chain nuclei; the eight Freudenthal-van der Waerden convex deltahedra at $N_lpha \in \{4,5,6,7,8,9,10,12\}$ all have all-vertex-on-surface realizations; the deltahedra-gap nuclei at $N_lpha \in \{11,13,14\}$ are conjecturally also all-surface, though the polytope identity is the subject of OPEN-SS-31). Direct computation at small $N_lpha$ should settle the question.
**Falsification route:** Identification of any $N_lpha \leq 14$ at which the minimum-energy rigid-tetrahedral packing places an alpha interior to the convex hull, demonstrated by either explicit construction or exhaustive enumeration.
**Paper(s):** SS-9 candidate (registered as paper-level conditional in Phase 1 working draft; programme-level closure target for Phase 4 or later session).
**Registered:** 26 April 2026 Session 2 in SS-9 Phase 1 v0.2 working draft §1 (formal registry entry pending ratification).

---

### OPEN-SS-31: Structural Realization of Alpha Clusters at the Deltahedra-Gap $N_\alpha \in \{11, 13, 14\}$
**Status:** OPEN — registered as candidate, pending ratification (registered 26 April 2026 Session 2 in SS-9 Phase 1 v0.2 working draft scaffold)
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM
**One-line statement:** Determine the structural realization of bound alpha clusters at $N_lpha \in \{11, 13, 14\}$ — the values where SS-7 Table 1 successfully predicts binding energies (⁴⁴Ti at $-0.26\%$, ⁵²Fe at $-0.57\%$, ⁵⁶Ni at $-0.73\%$) but no convex deltahedron exists per the Freudenthal-van der Waerden enumeration.
**What a solution looks like:** A definitive characterization of which of three resolution options applies at each deltahedra-gap $N_lpha$: (a) small-band edge-length variation around $R_{lpha lpha}$, with the cluster realizing a convex simplicial 3-polytope but with non-uniform edge lengths; (b) weakened convexity at these specific $N_lpha$, with the cluster slightly non-convex but still graph-simplicial; (c) non-3-polytope-realized graph-simpliciality, with the contact graph being a maximal planar graph but the geometric arrangement being a different topological object. The empirical record (sub-1% accuracy at all three nuclei) constrains the resolution but doesn't decide between options.
**Dependencies:** None blocking. Resolution likely informed by the cluster-model literature on ⁴⁴Ti, ⁵²Fe, ⁵⁶Ni geometries.
**Cross-sector connections:** Methodologically related to the SS-7 Remark 2.2 disclaimer on polytope identity — a closure of OPEN-SS-31 may simultaneously strengthen the polytope-identity question (OPEN-SS-31 candidate-adjacent) for the deltahedra-gap nuclei specifically.
**Current best lead:** SS-9 Phase 1 v0.2 working draft §6 registers the three resolution options. The Freudenthal-van der Waerden enumeration of convex deltahedra (8 members at $V \in \{4,5,6,7,8,9,10,12\}$) is well-established classical mathematics; the empirical agreement at $\pm 1\%$ across the gap nuclei is the constraint on resolution. The honest formulation of OPEN-SS-24's closure target separates graph-simpliciality (the weaker claim, what the SS-9 Theorem establishes) from deltahedral realizability (the stronger claim, registered here).
**Falsification route:** Empirical or theoretical demonstration that one of the three options is incompatible with the SS-7 Table 1 binding predictions at $N_lpha \in \{11, 13, 14\}$, or with rigid-tetrahedral packing constraints at these vertex counts.
**Paper(s):** SS-9 candidate (registered as scope question in Phase 1 working draft).
**Registered:** 26 April 2026 Session 2 in SS-9 Phase 1 v0.2 working draft §6 (formal registry entry pending ratification).

---

### OPEN-SS-32: Cluster-Level Collective Oblate-Deformation Mode (Slip-Plane Mechanism)
**Status:** OPEN — registered as candidate, pending ratification (registered 26 April 2026 Session 3 in SS-7 v1.3 refined-C1 facet (c))
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM
**One-line statement:** Derive from CPP primitives the cluster-level collective oblate-deformation mode that activates at alpha-cluster shapes with belt/seam structure and contributes a $+\Bpair \times \text{attenuation factor}$ binding bonus to the leading-order SS-7 edge-sum prediction. This is the SS-7-level analog of SS-8's H3$'$ provisional opposite-polarity pair-bonus mechanism: same $+\Bpair$-attenuated structural form, same provisional-tier registration, same forward-looking derivation target.
**What a solution looks like:** (a) A first-principles derivation of the K$_3$ collective-mode mechanism applied at the cluster-shape scale (rather than at the alpha-alpha contact scale of C3 or the interstitial-host-vertex scale of D2). The derivation should produce the attenuation factor and predict its value as a programme-level quantity (candidate forms: $1/\varphi$, $1/\varphi^2$, $\cos(\theta_{\text{symmetry}})$, or an integer ratio inherited from cluster-physics symmetry analysis). (b) A characterization of which cluster shapes activate the mode (predicted: shapes with axial symmetry that admits oblate deformation, e.g., J-solid deltahedra at $N_\alpha \in \{7, 8, 9, 10\}$; quenched at fully closed shapes like the icosahedron at $N_\alpha = 12$, where I$_h$ symmetry forbids oblate deformation). (c) A quantitative prediction of the binding bonus magnitude across the alpha-chain that reproduces the SS-7 Table~1 residual decomposition: $\approx 0$ at Regime~A ($N_\alpha \in \{3,4,5,6\}$, no degree-5 vertices); $\approx +0.55\,\Bpair$ at Regime~B ($N_\alpha \in \{7,8,9,10\}$, J-solid deltahedra with belt structure); variable at Regime~C ($N_\alpha \in \{11,13,14\}$, deltahedra-gap with restored belt structure); $\approx +0.30\,\Bpair$ at the icosahedron (suppressed by I$_h$ closure).
**Dependencies:** Methodologically parallel to OPEN-SS-28 (SS-8's H3$'$ provisional pair-bonus first-principles derivation). Closure of either OPEN-SS-32 or OPEN-SS-28 may inform the other via the K$_3$ scale-recurrence pattern (Pattern 6). Depends on the refined-C1 facet (c) framing (SS-7 v1.3); strengthens once OPEN-SS-24 closes under the multi-faceted-rigidity reading.
**Cross-sector connections:** The K$_3$ quantum $\Bpair = M_0/\varphi$ now recurs at five identified scales across the strong-sector papers (SS-5 nucleon-pair, SS-5 A=4 closure bonus, SS-7 alpha-alpha edge K$_3$, SS-8 D2 interstitial-host, and SS-7 v1.3 facet (c) cluster-shape). OPEN-SS-32 is the candidate fifth-scale instance pending derivation; closing it would strengthen the Pattern 6 K$_3$ scale-recurrence claim across the programme. The mechanism connects directly to the cluster-physics-literature signatures: oblate deformation in $^{28}$Si (KanadaEn'yo 2011, density wave at edge of oblate state), $^{40}$Ca + $\alpha$ core+halo identification of $^{44}$Ti, alpha-gas behavior in $^{56}$Ni (GANIL inelastic scattering, multiplicity up to 7), and hollow-polytope shape-class distinctions in Tohsaki & Itagaki 2018 (icosahedron and fullerene as "prominent hollow structures").
**Current best lead:** SS-7 Table 1 residual decomposition: residuals computed as effective excess contact count $|E_{\text{actual}}| - (3\Nalpha - 6)$ from $B_{\text{measured}} = \Nalpha\,\Balpha + |E_{\text{actual}}|\,\Bpair$. Observed: Regime A $\approx 0$ (clean LO); Regime B uniformly $\approx +1.3$ MeV $= +0.55\,\Bpair$ (flat plateau across $N_\alpha = 7,8,9,10$ despite degree-5 vertex count varying from 2 to 8 — the flatness rules out per-vertex-cost stories and selects bulk-mode stories); icosahedron $\approx +0.7$ MeV $= +0.30\,\Bpair$ (suppressed); Regime C variable. The $1/\varphi^2$ attenuation factor adopted in SS-8 H3$'$ would predict $\approx +0.38\,\Bpair$ at SS-7's cluster scale; the empirical $+0.55\,\Bpair$ in Regime B is within a factor of $1.5$ of this candidate. Resolution requires either the $1/\varphi^2$ derivation to extend to the cluster-shape scale or a shape-class-specific factor (e.g., $\cos(\theta_{\text{oblate}})$ where $\theta$ is set by the cluster's axial-symmetry-breaking angle).
**Falsification route:** A first-principles derivation that gives a value materially different from $+0.30$ to $+0.55\,\Bpair$ in the relevant regime would falsify the slip-plane reading. Empirical: AME 2020 binding-energy data at higher-$N_\alpha$ alpha-chain nuclei beyond SS-7's current $N_\alpha = 14$ ceiling can test the hierarchical-regime extension via PRED-O-16/17/18; a residual pattern that does not show belt-structure-correlated excess at the predicted magnitude would falsify the mechanism reading. The methodology has been validated by SS-8 H3$'$ at the analogous interstitial scale.
**Paper(s):** SS-7 v1.3 (refined-C1 facet (c)); SS-9 candidate (closure attempt). The first-principles derivation may share the SS-9 paper with the OPEN-SS-24 closure or be a separate SS-10 candidate.
**Cross-link (4 May 2026 Session 12):** OPEN-SS-35 sub-question (a) A-scaling Resolution R1 (Session 12) discovered an independent J-solid mid-range signature: inverting CPP/empirical $\hbar\omega$ ratios to ask "what $R_\alpha(A)$ would close the empirical $A^{-1/3}$ scaling" yields a non-monotonic U-shape with regular polytopes ($N_\alpha = 4, 12$) matching empirical to within $1$–$10\%$ and J-solid mid-range deltahedra ($N_\alpha = 5$–$10$, exactly the OPEN-SS-32 belt/seam regime) requiring $7$–$23\%$ expansion peaking at $N_\alpha = 10$. The U-shape regime coincides exactly with the OPEN-SS-32 oblate-deformation regime: same polytope-shape selection rules ($D_{3h}, O_h, D_{5h}, D_{2d}, D_{3h}, D_{4d}$ active; $T_d, I_h$ inactive), same $N_\alpha$ range, same suppression at the icosahedron. **Forward pointer:** if the J-solid mid-range deltahedra activate an oblate-deformation mode in the binding energy (OPEN-SS-32, $\approx +0.55\,B_{\rm pair}$ excess), they may also activate a *radial-breathing mode* that softens the centroid-to-vertex confinement, lowering $\hbar\omega^*$ at the same regime. This would unify OPEN-SS-32's binding-energy excess and OPEN-SS-35 sub-question (a)'s A-scaling discrepancy under a single J-solid radial-breathing mechanism. **Registered as future-session sub-sub-question of the OPEN-SS-32 ↔ U-shape connection** — multi-session by scope (3–5 sessions); high leverage if successful (could close R2 *and* identify the "additional CPP physics" needed for OPEN-SS-35 layer-3 gap-strength closure). See `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a_Ascaling_R1_RULED_OUT.md` §3 for the U-shape diagnostic and §5.5 for the connection.

**Phase 1 update (4 May 2026 Session 13 prior-art read):** The above cross-link asserts the U-shape and OPEN-SS-32 oblate regimes "coincide exactly." Phase 1 reading establishes the coincidence is **qualitative (six of eight rows) rather than literal**: the octahedron at $N_\alpha = 6$ is inside the U-shape mid-range overshoot ($+12.7\%$ required expansion) but outside the OPEN-SS-32 oblate regime ($O_h$ point-symmetric, no belt/seam, Regime A with $\approx 0$ excess). The remaining seven rows ($N_\alpha = 4, 5, 7, 8, 9, 10, 12$) are consistent. Three readings of the data are admissible: (A) the radial-breathing mode has a broader selection rule than the static oblate deformation, activating at axially-non-trivial cluster shapes generally rather than only at belt/seam structure; (B) the U-shape entry at $N_\alpha = 6$ is an empirical-formula-extrapolation artifact rather than a true U-shape feature; (C) the U-shape and OPEN-SS-32 are two distinct partially-overlapping K$_3$ scale-recurrence mechanisms at the cluster-shape scale. Phase 2 (single-session-tractable computation of the radial-breathing mode at $N_\alpha = 6$) discriminates among A/B/C. The unification hypothesis remains geometrically natural by Pattern 6 + empirical-coincidence + closure-leverage criteria, but its quantitative content is not yet computed. See `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase1.md` for the full Phase 1 prior-art digest, geometric assessment, and Phase 2 work plan.

**Phase 2 update (4 May 2026 Session 13 Phase 2 — uniform-scaling model RULED OUT):** Phase 2 executed the uniform-scaling radial-breathing-mode computation (model (a) of Phase 1 §6.3 step 1) across all eight canonical alpha-chain deltahedra at canonical $\sigma_{K3} = R_{\rm RMS}^\alpha = 1.68$ fm. **Three independent failure modes:** (i) **Wrong magnitude** — predicted fractional $\hbar\omega^*$ softening at $N_\alpha = 10$ (empirical U-shape peak) is $-4.57\%$ vs empirical $-33.6\%$ required; factor 7.4 undershoot. Sensitivity scan over $\sigma_{K3} \in [1.0, 2.5]$ fm yields factor 2.5 variation in magnitude with no qualitative change; closing the empirical magnitude would require $\sigma_{K3} \approx 8$ fm, broader than the cluster itself. (ii) **Wrong pattern** — model is monotonically decreasing in $N_\alpha$ (peak at $N_\alpha = 4$ with $-21\%$, drops to $-3.5\%$ at $N_\alpha = 12$); empirical is U-shaped with peak at $N_\alpha = 10$. Structural origin: $\langle(\Delta\lambda)^2\rangle \sim 1/\sqrt{|E| \cdot \sum |R_i|^2} \sim 1/N$ for deltahedra at fixed edge length; uniform scaling captures bulk-density scaling but not shape-class selection. (iii) **Wrong sign at endpoints** — empirical $N_\alpha = 4, 12$ require near-zero or compressive change; model predicts $-21\%$ and $-3.5\%$ softening respectively. Conclusion: **uniform-scaling radial-breathing model RULED OUT as a complete R2 closure mechanism.** Sixth programme-level negative-result demonstration in OPEN-SS-35 closure programme. The unification hypothesis itself is NOT ruled out — only model (a) is. Phase 1 §6.3 anticipated this branch and registered model (b) symmetry-resolved breathing decomposition as the natural fallback; Phase 3 (model (b)) is multi-session by scope and registered as Session 14 Priority 1. **N_alpha=6 Reading-A test result:** model (a) gives $-10.5\%$ softening at the octahedron — non-zero, structurally trivially consistent with Reading A, but uninformative as a mechanism-discrimination test (every polytope with edges has a breathing mode under uniform scaling). Real A-vs-B/C discrimination requires model (b). R2 status: substantively weakened — the simplest plausible mechanism fails — but not closed pending model (b) test. See `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase2.md` for full Phase 2 sketch and `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase2.py` for the reproducible computation.

**Phase 3 Phase A update (4 May 2026 Session 13 Phase 3A — naive full-Hessian RULED OUT; upper-bound benchmark established):** Phase 3 Phase A executed the full $3N - 6$ vibrational-mode Hessian decomposition (model (b) zeroth-order realization, summed over all modes without IRREP selection) across all eight canonical alpha-chain deltahedra at canonical $\sigma_{K3} = 1.68$ fm. **Three structural findings:** (i) **Flat pattern** — all 8 polytopes give $-85 \pm 1\%$ softening regardless of $N_\alpha$ or symmetry class. Variation across the entire range is only 2% (between $-84.9\%$ at icosahedron and $-86.8\%$ at tetrahedron); empirical varies from $+12\%$ to $-34\%$ (46% range). Naive full-Hessian has no shape-class selection. (ii) **Magnitude factor 2.5 overshoot** at empirical peak ($N_\alpha = 10$, model $-85.15\%$ vs empirical $-33.6\%$). Phase 2 model (a) was factor 7 too small at the same point. **Empirical lies cleanly between Phase 2 (lower bound, $-4.6\%$) and Phase 3A (upper bound, $-85\%$)** — full mode space contains $\sim 2.5$x sufficient zero-point fluctuation to reach empirical magnitudes; appropriate selection of $\sim 40\%$ of available variance would close the magnitude. (iii) **$N_\alpha = 6$ selection rule fails** — octahedron ($O_h$, no belt) gives 1.012× the snub disphenoid ($D_{2d}$, belt-active) softening. **Structural origin of flat pattern:** K$_3$ Gaussian potential at $\sigma_{K3} = 1.68$ fm gives per-edge spring 0.83 MeV/fm²; single-edge zero-point variance ~2.5 fm² is nearly independent of cluster context; vertex-coupling reduces this by only ~2% across all polytopes — edges are nearly independent in this weakly-bound system. **Constructive content:** Phase 3 Phase A establishes the upper-bound benchmark for what model (b) can produce; the empirical U-shape requires not more strength but better selection. Mode space is rich enough; the question is which subset contributes. Phase 3 Phase B (IRREP-selective decomposition with belt-mode projection) is sharply constrained: must produce $\sim 40\%$ of full-mode-space softening at J-solid mid-range polytopes ($N_\alpha = 7-10$), near-zero at regular polytopes ($N_\alpha = 4, 12$), and substantially less at $N_\alpha = 6$ ($O_h$) than at $N_\alpha = 8$ ($D_{2d}$). **Seventh programme-level negative-result demonstration** in OPEN-SS-35 closure programme. R2 severely weakened — two of three plausible realizations failed — but not formally closed pending Phase 3 Phase B. The unification hypothesis itself is now under stronger pressure but remains technically open. See `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase3a.md` for full Phase 3A sketch and `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase3a.py` for the reproducible computation.

**Phase 3 Phase B sub-phase A update (5 May 2026 Session 14 Phase 3B-A — minimal fixed-dim belt-subspace projection RULED OUT; pattern-shape anti-correlation new structural finding):** Phase 3B-A executed the simplest tractable subphase of Phase 3B specified at Phase 3A §6: project full Hessian eigenmodes onto a minimal belt subspace constructed per axial polytope from physical motivation (3D basis: A$_1$ in-plane radial breathing monopole + 2D E$_2$ quadrupole cos/sin patterns), with inertia-tensor classification (DEGEN / PROLATE / OBLATE) determining belt subspace dimensionality. T$_d$ (N=4), O$_h$ (N=6), I$_h$ (N=12) classify as DEGEN with $\dim(B) = 0$ by symmetry, implementing Reading A's structural commitment "no belt-IRREP at fully-symmetric polytopes." Belt fraction per mode $f_k^{\rm belt} = \sum_a |\langle \hat e^a | v_k\rangle|^2$ weights the Phase 3A per-mode variance contribution. **Two structural findings rule the construction out as a complete R2 closure mechanism:** (i) **Magnitude target (a) fails factor 3** — average J-solid mid-range belt fraction 0.135 vs target 0.40; belt-projected softening $-8.2\%$ at $N_\alpha = 10$ vs empirical $-33.6\%$. 3.3× improvement over hypothetical 1D-monopole-only construction ($f_{\rm belt} \approx 0.04$) but still substantively short. (ii) **Pattern shape anti-correlated** within axial polytopes — belt fraction monotonically DECREASES from $N_\alpha = 5$ (0.39) through $N_\alpha = 10$ (0.10); empirical magnitude monotonically INCREASES across same range ($-12\%$ to $-34\%$). Structural origin: the 3-dim belt basis fully spans the 3-vertex belt's radial-displacement subspace at $N_\alpha = 5$ (saturates) but only 3/8 of belt-radial space at $N_\alpha = 10$ (dilutes). Empirical U-shape requires the OPPOSITE scaling. **No fixed-dimension belt subspace can produce the empirical pattern.** This rules out the entire class. (iii) **Targets (b) and (c) pass by symmetry-structural-identity, NOT as differential tests** — DEGEN inertia → dim(B) = 0 → $f_{\rm belt} = 0$ for every mode → $\delta_{\rm belt} = 0$ exactly. Any inertia-degeneracy-aware construction satisfies these automatically; they do not differentially support Reading A. The empirical octahedron softening $-21.3\%$ vs $D_{2d}$ $-31.8\%$ gives ratio 0.67, NOT $\ll 1$ — Reading A's prediction of $\approx 0$ at the octahedron is empirically falsified at this discriminator (the patch-0149 cross-link refinement's qualitative six-of-eight observation). **The $N_\alpha = 5$ overshoot is structurally hardest constraint** — model $-33\%$ vs empirical $-12\%$, factor 2.7 too LARGE. Enlarging belt subspace dimension can only increase $f_{\rm belt}$ at small N (where 3-vertex belt is already fully covered), never decrease it. Any belt-IRREP construction capturing the 3-vertex belt's full radial-displacement subspace at $N_\alpha = 5$ overshoots empirical. **This may indicate the U-shape mechanism is NOT purely belt-IRREP-projection of the K$_3$ Gaussian Hessian.** **Eighth programme-level negative-result demonstration** in OPEN-SS-35 closure programme. R2 reduced to one untested realization — three of four model-(b) realizations now failed (Phase 2 uniform-only, Phase 3A all-modes, Phase 3B-A fixed-dim belt subspace). **Phase 3B-B** (full character-theory IRREP decomposition with belt-IRREP dimension scaling) is sole untested R2 realization with sharpened constraint: must produce non-monotonic-in-belt-size pattern within axial polytopes; small $\delta_{\rm belt}$ at $N_\alpha = 5$ and large at $N_\alpha = 10$. If structurally impossible, R2 formally ruled out and U-shape mechanism must be sought outside the K$_3$-Gaussian-Hessian framework entirely. See `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase3b_a.md` for full Phase 3B-A sketch and `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase3b_a.py` for the reproducible computation.

**Phase 3 Phase B sub-phase B update (5 May 2026 Session 15 Phase 3B-B — full C$_n$ IRREP decomposition RULED OUT via n-vs-N structural argument; R2 FORMALLY CLOSED):** Phase 3B-B executed the natural single-session realization of "full character-theory IRREP decomposition with belt-IRREP dimension scaling" specified at Phase 3B-A close: project full Hessian eigenmodes onto belt-IRREP subspaces using each axial polytope's C$_n$ proper-rotation subgroup, where C$_n$ is the largest cyclic symmetry of the principal axis (detected: $n = 3$ at $N=5,9$; $n = 5$ at $N=7$; $n = 2$ at $N=8$; $n = 4$ at $N=10$). Three natural belt-IRREP variants tested simultaneously: B-B1 "all $m \neq 0$" (broadest, every axially-anisotropic mode, $f_k^{\rm B-B1} = 1 - ||P_0 v_k||^2$); B-B2 "$m = 2$ only" (oblate-quadrupole IRREP per SS-7 OPEN-SS-32 hypothesis, $f_k^{\rm B-B2} = ||P_2 v_k||^2$ for $n \geq 3$); B-B3 "$m \neq 0$ AND in-plane radial" (dimension-scaling generalization of Phase 3B-A's fixed 3-dim belt-radial subspace). The C$_n$ proper-rotation subgroup is a coarser decomposition than the full point group D$_{nh}$/D$_{nd}$ (which include reflections and improper rotations) and gives an UPPER BOUND on the variance content of any belt-IRREP within the full point group — restricting to a finer decomposition can only reduce variance. So C$_n$ negative result generalizes to full point group by bracketing. Sanity checks all pass: Phase 3A reproduction exact to 3 decimals; $\sum_m \text{tr}\,P_m = 3N$ for every polytope; DEGENERATE polytopes get $f_{\rm belt} = 0$ by symmetry. **All three variants RULED OUT against empirical:** B-B1 uniformly overshoots by factor 1.2–2.7 across J-solid range (avg belt fraction 0.65 vs target 0.40); B-B2 undershoots N=7,8,9,10 by factor 1.7–4 (zero at N=8 because $m=2 \equiv m=0$ at $C_2$) but happens to match empirical at N=5 to within 3% — interpretive curiosity at $C_3$ where $P_2 = P_1$ captures the only non-trivial IRREP rather than genuinely-quadrupole content (group-theoretic dilution at small $n$, not physics signal); B-B3 undershoots all J-solids with avg belt fraction 0.184 (38% improvement over Phase 3B-A's 0.135 confirming dimension scaling helps but doesn't suffice; ceiling at ~0.18 is factor 2 below target — K$_3$-Gaussian-Hessian framework lacks sufficient belt-IRREP variance regardless of subspace definition). **DECISIVE NEW STRUCTURAL FINDING (n-vs-N obstacle, class-level argument):** empirical magnitude monotonically increasing in $N$ across J-solid range — $|\delta_{\rm emp}| = 12.16, 29.50, 31.81, 33.14, 33.58\%$ for $N = 5, 7, 8, 9, 10$ — but cyclic symmetry order $n$ non-monotonic in $N$: $n = 3, 5, 2, 3, 4$ (full point group orders also non-monotonic: $|G| = 12, 20, 8, 12, 16$). Any belt-IRREP-projection mechanism's variance content depends on $n$ or $|G|$, so **no function of group-theoretic structure alone can produce a monotonic-in-$N$ pattern when $n$ is non-monotonic in $N$**. This is a class-level structural argument that rules out the entire family of belt-IRREP-projection mechanisms within K$_3$-Gaussian-Hessian framework, not just the three Phase 3B-B variants — extends to full point group decomposition with reflections and improper rotations (orders non-monotonic), energy-weighted IRREP filtering (soft-mode count per IRREP depends on $n$), and higher-$m$ harmonics (existence depends on $n$). **Ninth programme-level negative-result demonstration** in OPEN-SS-35 closure programme — decisively stronger than Phase 3B-A's because structural argument extends beyond specific implementations to entire mechanistic class. **R2 (cluster-scale vs alpha-scale mean-field unification at canonical $\sigma_{K3}$) FORMALLY CLOSED — RULED OUT:** all four plausible model-(b) realizations have failed (Phase 2 uniform-only Session 13 Phase 2; Phase 3A all-modes Session 13 Phase 3A; Phase 3B-A fixed-dim belt subspace Session 14 Phase 3B-A; Phase 3B-B C$_n$ IRREP decomposition this session); structural argument extends closure to all model-(b) variants within framework. Unification hypothesis at canonical $\sigma_{K3}$ FALSIFIED. **Both registered closure candidates for OPEN-SS-35 sub-question (a) A-scaling now ruled out** (R1 Session 12 for sign + U-shape + Decoupling Theorem; R2 Session 15 for class-level structural impossibility within IRREP-projection framework). OPEN-SS-32 attenuation-factor derivation BLOCKED (was conditional on R2 success). Sub-question (b) layer 3 gap-strength closure INDEPENDENT of R2 by Decoupling Theorem (Session 12), unaffected. The U-shape mechanism must be sought OUTSIDE the K$_3$-Gaussian-Hessian framework — candidate mechanisms (each requires independent scoping): (1) anharmonic K$_3$ corrections at order $\xi^4$ in Gaussian expansion (most direct extension of framework, scales with edge count $|E| = 3N - 6$ which IS monotonic in $N$, single-session-tractable, **suggested Session 16 Priority 1**); (2) surface-tension contribution scaling with cluster surface area; (3) Pauli-blocking at internal alpha-alpha contacts (edge count); (4) effective-mass renormalization of nucleon orbitals; (5) Coulomb-screened intra-cluster destabilization revisited. First qualitative cross-paradigm consilience claim (Session 9, magic-number sequence reproduced from CPP first principles) intact. Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances unchanged. Six programme-level OPEN-SS-35 stages preserved. Phase 3B-B refines stage (vi) by formally closing R2; closure is informational not progressional — stage (vi) was previously "unclosed pending R2 verdict"; it is now "R2 ruled out, A-scaling closure mechanism unknown." See `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase3b_b.md` for full Phase 3B-B sketch and `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase3b_b.py` for the reproducible computation.
**Registered:** 26 April 2026 Session 3 in SS-7 v1.3 §2.1 refined-C1 facet (c) (formal registry entry pending ratification).

**Phase 4 update (5 May 2026 Session 16 Phase 4 — anharmonic K$_3$ $\xi^4$ corrections + all-orders Gaussian extension RULED OUT via sign theorem; programme-level closure of Gaussian-K$_3$ framework at fixed cluster geometry):** Phase 4 executed Session 15 Phase 3B-B's Priority 1 forward pointer — anharmonic K$_3$ corrections at order $\xi^4$ in the Gaussian expansion — as a single-session investigation across all eight polytopes ($N = 4, 5, 6, 7, 8, 9, 10, 12$) at canonical $\sigma_{K3} = 1.68$ fm. The investigation yielded a result the original scoping plan did not anticipate: a third falsifier (sign) that resolves the question on dispositive grounds before the originally-planned magnitude (F2) and pattern (F3) criteria are needed.

The K$_3$ pair potential $V_{\rm pair}(\xi) = -B_{\rm pair} \exp(-\xi^2/2)$ Taylor-expands to $-B_{\rm pair} + (B_{\rm pair}/2)\xi^2 - (B_{\rm pair}/8)\xi^4 + \cdots$. Leading anharmonic Taylor coefficient $-(B_{\rm pair}/8) < 0$. In harmonic ground state, $\langle \xi^4 \rangle_0 = 3 \langle \xi^2 \rangle_0^2 > 0$ (Wick). First-order PT shift $\Delta E^{(1)}_{\rm anharm} = -(3 B_{\rm pair}/8) \langle \xi^2 \rangle_0^2 < 0$ (more binding). Empirical J-solid range needs $\Delta E > 0$ (cluster wants to grow → less binding than canonical K$_3$). **Signs uniformly opposite — F1 (sign) fails universally**. Computation across all 8 polytopes confirms: $\Delta E^{(1)}/\alpha = -0.98, -1.15, -1.30, -1.35, -1.43, -1.48, -1.51, -1.57$ MeV for $N = 4, 5, 6, 7, 8, 9, 10, 12$ — all negative.

**Computational surprise:** $\langle s \rangle \equiv \langle \xi^2 \rangle_0 \approx 0.85$ across all polytopes (range only $[0.847, 0.864]$, $\sim 2\%$ variation), much larger than the handover's estimate of $\sim 0.5$. At $s = 0.85$, $\xi_{\rm rms} \approx 0.92$ — near the inflection point of $\exp(-\xi^2/2)$ at $\xi = 1$. The Gaussian Taylor expansion converges slowly, raising the legitimate concern that higher-order Taylor terms might flip the sign of the all-orders correction. The all-orders Gaussian-average extension in the harmonic-GS-trial ansatz is computed in closed form: $\langle V_{\rm pair} \rangle_{\rm HOgs} = -B_{\rm pair} (1+s)^{-1/2}$. Numerical results: factor $\sim 0.59$ reduction from leading $\xi^4$ estimate (polytope-independent because $\langle s \rangle$ near-constant); sign preserved across all 8 polytopes.

**Sign theorem (rigorous all-orders closure):** $f(s) \equiv (1+s)^{-1/2} - 1 + s/2$ is strictly positive for all $s > 0$. One-line proof: $f(0) = 0$, $f'(s) = (1/2)[1 - (1+s)^{-3/2}] > 0$ for $s > 0$, hence $f$ strictly increasing on $(0, \infty)$ from $f(0) = 0$, so $f(s) > 0$. Therefore $\Delta E_{\rm anharm}^{\rm all\text{-}orders} = -B_{\rm pair} f(s) < 0$ universally. **Variational corollary (Rayleigh–Ritz):** $E^{\rm full}_{0,{\rm true}} \le E^{\rm harm}_0 + \Delta E_{\rm anharm}^{\rm all\text{-}orders} < E^{\rm harm}_0$. The true cluster ground state in the full Gaussian Hamiltonian is, with mathematical certainty, *more* bound than the harmonic estimate, never less. No reordering, truncation, or resummation can flip this — it is a structural property of the Gaussian-K$_3$ framework at fixed cluster geometry.

**Programme-level closure of Gaussian-K$_3$ framework at fixed cluster geometry.** Phase 3B-B (Session 15) closed the harmonic-Hessian-belt-IRREP family at canonical $\sigma$ via the n-vs-N structural argument. Phase 4 (this session) closes the perturbative-correction family at canonical geometry via the sign theorem + Rayleigh–Ritz. Together: **the entire Gaussian-K$_3$ framework at fixed cluster geometry cannot produce empirical U-shape — provably**. The empirical U-shape in J-solid range needs shifts of opposite sign than any perturbative or variational improvement of harmonic K$_3$ at canonical geometry can give. Whatever produces empirical U-shape acts on a different physical channel: (R3) cluster compression/expansion driven by N-dependent boundary conditions; (R4) cluster shape distortion beyond the rigid J-solid assumption; (b) coupling to inelastic excitations (Hoyle-state mixing, alpha breathing); (c) physics outside K$_3$ entirely (surface-energy shape dependence, Coulomb cluster-arrangement effects, spin-orbit cluster corrections).

**F2 magnitude and F3 pattern** for completeness, both moot once F1 fails: $|\Delta E^{(1)}/B_{K3}| \approx 27\%$ across all 8 polytopes (near-polytope-independent because $\langle s \rangle$ near-constant); J-solid range ratios to $|d_{\rm emp}|$ are 0.80–1.31 — *would have* passed F2 in isolation. $|\Delta E^{(1)}|/\alpha = 1.15, 1.35, 1.43, 1.48, 1.51$ MeV for $N = 5, 7, 8, 9, 10$ — monotonic in $N$, scales as $(3N-6)/N$, qualitatively consistent with empirical.

**Constructive content from Phase 4:** (i) **sign theorem** as closure tool with broader applicability — any future Gaussian-K$_3$ refinement at fixed geometry must invoke geometry change, inelastic channels, or out-of-framework physics to escape it; (ii) **$\langle s \rangle \approx 0.85$ near-constancy** across all 8 polytopes (range only $\sim 2\%$) is non-trivial empirical observation that mean per-edge zero-point variance is essentially independent of cluster topology in J-solid range — explains why $|\Delta E / B_{K3}|$ is nearly polytope-independent; (iii) **$\xi_{\rm rms} \approx 0.92$ regime** (near inflection point of Gaussian) is quantitative caution flag for any future K$_3$ work assuming small-displacement perturbative expansion.

**Tenth programme-level negative-result demonstration** in OPEN-SS-35 closure programme; **fifth in OPEN-SS-32 ↔ U-shape thread**. The thread now has five sequential closures: Phase 2 uniform-only, Phase 3A all-modes, Phase 3B-A fixed-dim belt, Phase 3B-B IRREP decomposition (R2 formal closure), **Phase 4 anharmonic perturbative correction (sign theorem closing Gaussian-K$_3$ framework at fixed geometry)**. OPEN-SS-32 attenuation-factor derivation reformulation depends on identifying U-shape mechanism *outside* Gaussian-K$_3$ framework at fixed geometry. OPEN-SS-35 sub-question (a) A-scaling closure now requires either geometric-shift mechanisms beyond R1 (channels R3, R4) or out-of-framework physics ((b), (c)). Sub-question (b) layer 3 gap-strength closure INDEPENDENT by Decoupling Theorem (Session 12), unaffected. First qualitative cross-paradigm consilience claim (Session 9) intact. Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances unchanged. Six programme-level OPEN-SS-35 stages preserved. Phase 4 refines stage (vi) further by closing Gaussian-K$_3$ framework rigorously rather than incrementally; stage (vi) is now "Gaussian-K$_3$ framework at fixed geometry empty of viable A-scaling closures, mechanism must be R3/R4 or out-of-framework." Session 17 Priority 1 = cluster-geometry shift mechanisms beyond R1 (channels R3, R4) — single-session-tractable scoping investigations. See `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_phase4_anharmonic_K3_xi4.md` for full Phase 4 sketch including §2.4 sign theorem proof, and `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase4_anharmonic_K3_xi4.py` for the reproducible computation.

---

### OPEN-SS-33: Programme-Level Closure of C7 (Contact-Graph Planarity)
**Status:** OPEN — registered as candidate, pending ratification (registered 2 May 2026 Session 4 in SS-9 v0.3 working draft §1)
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM
**One-line statement:** Derive from CPP primitives (A1–A11) the planarity of the alpha-cluster contact graph $G(\mathcal{C})$ — i.e., that $G$ admits an embedding in the plane (equivalently, on $S^2$) without edge crossings. C7 is the new paper-level structural hypothesis introduced in SS-9 v0.3 §1 to enable the graph-theoretic Lemma B$'$ proof via Steinitz's theorem; OPEN-SS-33 is the corresponding follow-up programme-level closure target at the same tier as OPEN-SS-29 (C5) and OPEN-SS-30 (C6).
**What a solution looks like:** A rigorous derivation that under refined-C1 (SS-7 v1.3 §2.1 facets a/b) plus C2 (base-to-base contact) plus C5 (ground-state energy minimization) plus C6 (cluster surface-realization, no interior alphas), the contact graph $G(\mathcal{C})$ of any A1–A11-realizable bound alpha cluster is planar. Most plausible closure route per SS-9 v0.3 §9 sketch: under C6 + cluster contractibility (no internal voids in the bound-state CPP-lattice configuration), the cluster's outer 2-surface $\Sigma$ is topologically $S^2$; the alpha-dual embedding (each alpha placed at a representative point on its outer-face region; each contact drawn as an arc through the shared interior face) maps $G$ onto $\Sigma$; planarity follows. Closure requires (a) showing that A1–A11 + bound-state assumptions force cluster contractibility (no alpha-cluster torus or higher-genus configuration is energetically preferred); (b) making the alpha-dual embedding rigorous; (c) handling the degree-$\geq 5$ vertex hosting via refined-C1 facet (b) without breaking the embedding's planarity.
**Dependencies:** Inherits from SS-7 v1.3 refined-C1 (facet (b) load-bearing for geometric realizability of degree-5 vertex hosting). Methodologically parallel to OPEN-SS-29 (C5 closure) and OPEN-SS-30 (C6 closure): all three are SS-9 paper-level structural hypotheses pending programme-level derivation. May share Layer-3 ancestry with OPEN-SS-29 and OPEN-SS-30 — all three reduce to Pattern 6 K$_3$ scale-recurrence and CPP lattice-geometry constraints under bound-state assumptions. Closure of OPEN-SS-33 strengthens SS-9's conditional theorem by removing one of the four follow-up open problems.
**Cross-sector connections:** Connects to the broader question of cluster-shell topology in CPP nuclear physics: which alpha-cluster topologies are allowed by A1–A11 under bound-state assumptions, and which are forbidden? A non-planar contact graph would correspond to a cluster topology with handles or higher genus, which is plausibly forbidden by the rigid-tetrahedral packing constraint of C1 plus the energetic considerations of C5. A formal derivation would establish the $S^2$-topology of bound alpha clusters as a programme-level result, with implications beyond SS-9 (e.g., for any future paper deriving cluster-shape predictions from CPP primitives).
**Current best lead:** The §1 motivation paragraph in SS-9 v0.3 working draft sketches the cluster-shell-topology argument: under C6 (no interior alphas, all centroids on $\partial H$) + cluster contractibility (no internal voids), the cluster outer surface $\Sigma$ is contractible-3D-region-boundary $\cong S^2$, and the natural alpha-dual embedding makes $G$ planar. Tightening this into a formal sub-lemma showing C6 + cluster contractibility $\Rightarrow$ C7 would close OPEN-SS-33 modulo "cluster contractibility from A1–A11," which itself would reduce to: a non-contractible cluster (e.g., toroidal) has an internal void at lower DP-density than the surrounding sea, energetically unfavorable under C5. This is a viable closure path.
**Falsification route:** A direct derivation from A1–A11 that yields a non-planar contact graph for some alpha-cluster ground state would falsify C7 and require restructuring SS-9's Lemma B$'$. Empirical: any AME 2020 alpha-chain nucleus whose binding pattern is inconsistent with a planar $|E| = 3\Nalpha - 6$ count would suggest non-planar contact-graph topology in that ground state. None observed at $N_\alpha \leq 14$ per SS-7 Table 1.
**Paper(s):** SS-9 v0.3 working draft (where C7 is registered); SS-9 candidate (closure attempt). The first-principles derivation could share the SS-9 paper with the OPEN-SS-24 closure or be a separate paper.
**Registered:** 2 May 2026 Session 4 in SS-9 v0.3 §1 + §9 sketch (formal registry entry pending ratification).

---

### OPEN-SS-34: Programme-Level Closure of the Deltahedron-Core / Satellite-Regime Mechanism at $N_\alpha \geq 14$
**Status:** OPEN — registered as candidate, pending ratification (registered 2 May 2026 Session 4 follow-up arc, after PRED-O-16/17/18 testing identified the slope-1 satellite regime at $N_\alpha = 15$–$20$)
**Sector(s):** SS (nuclear physics)
**Priority:** MEDIUM
**One-line statement:** Derive from CPP primitives (A1–A11) + refined-C1 (facets a/b/c) why the strict-$N=Z$ alpha-chain undergoes a sharp regime transition at $N_\alpha = 14 \to 15$, from simplicial deltahedron geometry ($|E| = 3 N_\alpha - 6$) to deltahedron-core-plus-satellite-alphas ($|E| = N_\alpha + 22$). The empirical signature is a clean slope-3 → slope-1 discontinuity in the contact-graph effective edge count, observed across $N_\alpha = 14$–$20$ in TOI 98 / AME 2020 data, fit by a one-calibrated-parameter formula at 0.05% relative accuracy.
**What a solution looks like:** A first-principles derivation that accounts for: (a) why ${}^{56}$Ni at $N_\alpha = 14$ is the empirical terminus of the simplicial regime — candidate readings include doubly-magic shell closure ($Z = N = 28$), deltahedra-gap exhaustion at $N = 12$ icosahedron + 2 deltahedra-gap nuclei, or Coulomb-pressure threshold at high-$Z$ destabilizing the simplicial polytope; (b) why the satellite regime has slope-1 (each new alpha adds exactly one face contact on average), suggesting a chain-or-tree topology of satellite alphas attached to the core; (c) what determines $N_\alpha^{(2)\text{crit}}$ — the second regime termination where the satellite picture itself breaks down (likely candidate: ${}^{100}$Sn at $N_\alpha = 25$, doubly-magic $Z = N = 50$). The resolution should produce the empirically-observed integer slope-1 (not a fitted value), the integer-22 intercept (corresponding to a 14-alpha core with $|E_{\text{core}}| = 36$), and the persistent slip-plane bonus $B_{\text{slip}} \approx +4$ MeV from the deltahedron core.
**Dependencies:** Methodologically parallel to OPEN-SS-32 (slip-plane mechanism at $N_\alpha = 7$–$14$). Both arose from clean residual-pattern observations in SS-7 Table 1; both ask how CPP primitives produce empirical regime structure. May share Layer-3 ancestry under Pattern 6 (K$_3$ scale-recurrence) plus CPP lattice geometry under bound-state constraints — the deltahedron core's slip-plane bonus persisting through the satellite regime suggests OPEN-SS-32 and OPEN-SS-34 share mechanism. Inherits from refined-C1 (SS-7 v1.3 §2.1 facets a/b/c).
**Cross-sector connections:** The deltahedron-core / satellite-regime picture, if confirmed by PRED-O-19 testing at $N_\alpha = 21$–$25$, extends the CPP empirical scope from $N_\alpha = 14$ (the SS-7 Table 1 ceiling) to $N_\alpha = 25$ ($^{100}$Sn doubly-magic terminus) — adding up to 11 zero-parameter empirical correspondences to the swarm tally if the satellite formula tracks data through that range. This is the largest single-paper extension of the swarm achievable in the strong-sector at the current programme state.
**Current best lead:** The empirical picture is highly constrained: deltahedron core of $N_\alpha^{\text{core}} = 14$ alphas (corresponding to ${}^{56}$Ni doubly-magic terminus); satellites attach with exactly 1 face contact each (slope-1 in $|E|$ vs $N_\alpha$); persistent slip-plane bonus $B_{\text{slip}} \approx +4$ MeV from the core. The integer slope-1 and integer-22 intercept are *not* fitted — they emerge directly from "deltahedron core + 1-bond satellites" structural picture. Most plausible derivation route: show that under refined-C1 + Coulomb pressure beyond $Z \approx 30$ + doubly-magic core stability, additional alphas in the strict-$N=Z$ chain attach as satellite single-bonds because (i) the deltahedron is no longer the ground-state polytope for $N > 14$ (Coulomb cost too high), and (ii) chain-extension is the next-best alpha addition mode given the rigid-tetrahedral C1 constraint.
**Falsification route:** A direct CPP derivation that gives a different slope (e.g., 0.5 or 2) at $N_\alpha \geq 14$ would falsify this picture. Empirically: PRED-O-19 testing at $N_\alpha = 21$–$25$ (against AME 2020) is the immediate test; deviations $> 1$ MeV at any $N_\alpha$ in that range identify either $N_\alpha^{(2)\text{crit}}$ or a flaw in the satellite picture itself. If the satellite formula tracks data perfectly through $^{100}$Sn at $N_\alpha = 25$, the picture is strongly supported across an 11-nucleus range.
**Paper(s):** SS-9 sketch `series_strong/papers/SS-9/sketches/SS-9_alpha_chain_extended_residuals.md` (where the empirical picture is documented); SS-9 v1.0 candidate or SS-10 candidate (closure attempt). The first-principles derivation may share with OPEN-SS-32 if the K$_3$ scale-recurrence connection materializes.
**Registered:** 2 May 2026 Session 4 follow-up arc, after empirical testing of PRED-O-16/17/18 (formal registry entry pending ratification).
**Update 2 May 2026 Session 4 follow-up 3rd sub-arc:** Level-1 derivation completed under H1–H4 (K$_3$ closure-bonus from SS-5; refined-C1+SS-9 v0.3 hypothesis stack; shell-magic-number sequence 28 and 50 as input H3; Coulomb destabilization at high $Z$ as input H4). Three derivation targets resolved: (T1) deltahedron-core terminus at $N_\alpha=14$ as coincidence of FvdW range top-out + deltahedra-gap exhaustion + ${}^{56}$Ni doubly-magic; (T2) slope-1 satellite topology as forced by core saturation + face-coincidence requirement of C2 + tetrahedral geometry preventing multi-face contact; (T3) satellite-regime terminus at $N_\alpha=25$ as exactly the magic-number gap $(50-28)/2 = 11$ satellites. Level-2 deepest dependency: shell-magic-number sequence registered as OPEN-SS-35 candidate; $B_{\rm slip}$ exact form registered as OPEN-SS-36 candidate. Companion sketch: `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-34_derivation_attempt.md`. OPEN-SS-34 status: Level-1 derived under stated hypotheses (Level-3 closure remains conditional on OPEN-SS-35 and OPEN-SS-36 closures).

---

### OPEN-SS-35: Programme-Level Closure of the Shell-Magic-Number Sequence from CPP Primitives
**Status:** OPEN — sub-question (a) Level-1 partial closure delivered (registered 2 May 2026 Session 4 follow-up 3rd sub-arc; scoping document delivered Session 5 Phase 2; **sub-question (a) Level-1 partial closure delivered 2 May 2026 Session 6 Phase 1** under hypotheses E1, E2: HO mean-field $\hbar\omega^* \in \{14.6, 18.1, 11.1\}$ MeV across regular polytopes $N_\alpha = 4, 6, 12$ matches empirical $41/A^{1/3}$ to within 30% with zero free parameters; icosahedron at $A = 48$ matches to 1%)
**Sector(s):** SS (nuclear physics, Pattern-6 cross-paradigm bridge)
**Priority:** HIGH (deepest dependency in BOTH OPEN-SS-34 and OPEN-SS-36 closures since 4th sub-arc; leverage doubled relative to original 3rd sub-arc registration; cross-paradigm consilience claim if closed)
**One-line statement:** Derive from CPP primitives (A1–A11) the standard nuclear shell-model magic-number sequence ($Z, N \in \{2, 8, 20, 28, 50, 82, 126\}$) at the nucleon-shell-organization scale. The standard derivation depends on spin-orbit coupling splitting the j-shells; the strong magic numbers (28, 50, 82, 126) are spin-orbit-driven. CPP's analog of spin-orbit coupling comes from the 600-cell coordination and ZBW phases. Closure would derive the magic-number sequence as a Pattern-6 phenomenon at a previously-unidentified scale.
**Update 2 May 2026 Session 5 Phase 2 (scoping work begun):** Five candidate routes evaluated; **Route A (3D HO + spin-orbit derived from CPP) adopted as primary** (most tractable). **Route D (direct lattice-shell counting) ruled out** by explicit computation: the 600-cell distance-shell vertex counts from a reference vertex (cumulative: 13, 33, 45, 75, 87, 107, 119, 120) do NOT match the strong magic numbers; magic numbers must emerge from nucleon-orbital structure, not lattice geometry directly. **Level-0 consistency check passes:** CPP's natural HO frequency from $R_\alpha = 2.37$ fm gives $\hbar\omega = (3/2)(\hbar c)^2/(m_n R_\alpha^2) = 11.07$ MeV, matching the empirical Bohr-Mottelson value at $A = 56$ to ~3% with no fitted parameters. CPP's natural spin-orbit ratio $V_{\rm SO}/\hbar\omega \sim 0.10$ from ZBW + nuclear $v/c$ falls in the magic-number-producing range. Three sub-questions registered for sequential closure: (a) rigorous derivation of HO mean-field from K$_3$ collective modes; (b) rigorous derivation of spin-orbit coupling strength from ZBW; (c) proof that $V_{\rm SO}/\hbar\omega$ is in the magic-number-producing range across the bound-nucleon regime. Companion sketch: `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_scoping.md`. Companion script: `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_scoping.py`.

**Update 2 May 2026 Session 6 Phase 1 (sub-question (a) Level-1 partial closure):** Sub-question (a) advanced from "registered" to "Level-1 partial closure under hypotheses E1, E2." The K$_3$ contact mechanism (SS-8) is extended from vertex localization to general nucleon position via $V_{K_3}(\vec r) = -B_{\rm pair} \sum_i \deg(v_i) \exp(-|\vec r - \vec R_i|^2/(2\sigma^2))$ (E1: Gaussian overlap; E2: overlap-weighted binding). A closed-form analytic Hessian gives the spring constant; self-consistent solution for nucleon localization $\sigma = \hbar c/\sqrt{m_n \hbar\omega}$ converges in ~5 iterations. Results across regular polytopes: tetrahedron ($N_\alpha=4$, $A=16$) $\hbar\omega^* = 14.60$ MeV vs empirical 16.27 (ratio 0.90); octahedron ($N_\alpha=6$, $A=24$) $\hbar\omega^* = 18.06$ MeV vs empirical 14.21 (ratio 1.27); icosahedron ($N_\alpha=12$, $A=48$) $\hbar\omega^* = 11.13$ MeV vs empirical 11.28 (ratio 0.99). **Mean ratio CPP/empirical = 1.05; max deviation 27%.** Zero free parameters. **Pattern 6 K$_3$ scale-recurrence: 6 → 7 confirmed instances** (the 7th instance is the K$_3$ quantum producing the harmonic-oscillator mean field at the nucleon-orbital-organization scale). Three new sub-sub-questions registered within sub-question (a) for full closure: E1-closure (derive Gaussian overlap from CPP primitives), E2-closure (rigorous justification of overlap-weighted binding extrapolation), A-scaling (reproduce $A^{-1/3}$ across alpha-chain regime). Companion sketch: `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a.md`. Companion script: `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_a.py`.

**Update 2 May 2026 Session 7 Phase 1 (A-scaling extension):** Sub-question (a) A-scaling sub-sub-question advanced from "registered" to "**substantive Level-0/Level-1 mixed result.**" Session 6 machinery extended from the 3 regular polytopes ($N_\alpha = 4, 6, 12$) to all 8 canonical alpha-chain deltahedra ($N_\alpha = 4, 5, 6, 7, 8, 9, 10, 12$) including triangular bipyramid (D$_{3h}$), pentagonal bipyramid (D$_{5h}$), snub disphenoid (J$_{84}$, D$_{2d}$), triaugmented triangular prism (J$_{51}$, D$_{3h}$), and gyroelongated square bipyramid (J$_{17}$, D$_{4d}$). For lower-symmetry deltahedra, anisotropic Hessian eigenvalues require numerical computation; geometric-mean frequency $\omega_{\rm geo} = (\omega_x \omega_y \omega_z)^{1/3}$ used as scalar comparison. **All 8 deltahedra produce confining harmonic minima at the centroid with positive eigenvalues**: HO form is robust across alpha-chain regime. Mean ratio CPP/empirical = 1.27 (range 0.90–1.51) across all 8 deltahedra. **However, the A-scaling discrepancy is a real finding**: CPP slope $-0.10$ vs empirical $-0.33$ in $\log(\hbar\omega)$ vs $\log A$ fit. Mid-range deltahedra ($N_\alpha = 5$–$10$) cluster around 17–19 MeV (nearly A-independent); icosahedron at $A = 48$ matches empirical to 1% via "centroid moves into a void" physics. Two candidate resolutions registered: (R1) $R_\alpha$ scale-dependence in CPP; (R2) cluster-scale vs alpha-scale mean field interpretation. Sub-question (a) Level-1 partial closure remains valid; sub-question (c) remains pending on both sub-question (b) closure and full A-scaling closure. Companion sketch: `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a_Ascaling.md`. Companion script: `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_a_Ascaling.py`.

**Update 2 May 2026 Session 7 Phase 2 (sub-question (b) scoping):** Sub-question (b) advanced from "registered" to "**scoping work begun, Level-0 consistency check passed; closure remains multi-session.**" Three candidate routes evaluated: Route B-α (ZBW phase coupling via Thomas-precession analog $(v/c)^2 \cdot \hbar\omega$) **adopted as primary**; Route B-γ (K$_3$-mode phase coupling) **ruled out** by magnitude ($V_{\rm SO}/\hbar\omega \sim 10^{-3}$, insufficient for magic numbers); Route B-β (ZBW magnetic moment in cluster field) deprioritized pending unknown CPP magnetic permeability. **Level-0 consistency check passes:** $V_{\rm SO}^{\rm CPP} \sim (v/c)^2 \cdot \hbar\omega \approx 0.09 \cdot 15 \approx 1.4$ MeV at $A \sim 56$, matching empirical $\sim 1.5$ MeV to factor of unity. Ratio $V_{\rm SO}/\hbar\omega \approx 0.09$ falls in the magic-number-producing range $0.10$–$0.15$. The ZBW connection to spin-orbit is through the **relativistic origin** of ZBW (Dirac-equation negative-energy mixing) — exactly the mechanism that conventionally produces Thomas precession and hence spin-orbit. CPP's ZBW machinery is therefore the CPP derivation of the relativistic kinematics underlying spin-orbit. Three sub-sub-questions registered within Route B-α for closure: B-α layer 1 (Fermi velocity $v_F/c \approx 0.27$–$0.30$ from CPP primitives, single-session-tractable for next-session work), B-α layer 2 (operator structure of $\vec L \cdot \vec S$, **depends on OPEN-SS-16**), B-α layer 3 (magic-number production verification given closures of layers 1, 2 + sub-question (a)). Sub-question (b) is now identified as **multi-session by scope** with full closure depending on OPEN-SS-16 (Layer B gap). Companion sketch: `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_b_scoping.md`.

**Update 2 May 2026 Session 8 (B-α layer 1 closure):** Sub-question (b) Route B-α: layer 1 closed at Level-1 partial. Three independent CPP-derived approaches compute $v_F/c$ across the alpha-chain regime: **Approach A** (cluster-averaged density Fermi gas using $R_\alpha$ + 4 nucleons per alpha + deltahedron geometry) gives $v_F/c \in [0.306, 0.392]$ (mean 0.352, upper-bound from rigid-sphere cluster model); **Approach B** (HO virial theorem using CPP $\hbar\omega^*$ from sub-question (a) Level-1 partial closure) gives $v_F/c \in [0.197, 0.266]$ (mean 0.238, lower-bound missing Fermi-pressure contribution); **Approach C** (surface-region Thomas-form density at half-density radius) gives $v_F/c \in [0.278, 0.356]$ (mean 0.319, best match at small/large polytopes). All three approaches **bracket the empirical $v_F/c \approx 0.27$–$0.30$**; geometric mean of Approaches A and B is approximately 0.27 (in empirical range). The Phase 2 scoping document's phenomenological "$v/c \approx 0.3$" is now CPP-derived. The Level-0 estimate $V_{\rm SO} \sim (v_F/c)^2 \cdot \hbar\omega \approx 1.4$ MeV at $A = 56$ is upgraded to **Level-1 partial closure for $V_{\rm SO}$ magnitude** with all CPP-internal inputs ($R_\alpha$, $\hbar\omega^*$, polytope geometry); only the standard 3D Fermi-gas formula and HO virial theorem are imported from textbook nuclear physics. Ratio $V_{\rm SO}/\hbar\omega \approx 0.09$, just below the magic-number-producing range $0.10$–$0.15$ — suggesting either small upward correction (toward Approach A's higher values) or that CPP produces a "softer" spin-orbit consistent with empirical observation that lighter magic numbers (e.g., 28) are softer than heavier ones. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged (spin-orbit is a relativistic-kinematics mechanism, not a K$_3$ collective mode). Sub-question (b) status: "scoping work begun, Level-0 check passed" → "**B-α layer 1 closed; magnitude Level-1 partial under inherited E1 + standard nuclear-physics formulas**". Layer 2 (operator structure of $\vec L \cdot \vec S$) still depends on OPEN-SS-16. Layer 3 (magic-number production verification) is now the natural single-session-tractable next step and does NOT depend on OPEN-SS-16. Companion sketch: `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer1.md`. Companion script: `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer1.py`.

**Update 2 May 2026 Session 9 (B-α layer 3 partial closure + terminology correction):** Sub-question (b) Route B-α: layer 3 reaches **partial closure**. A standard Goeppert-Mayer / Jensen shell-model calculation with CPP-derived inputs ($\hbar\omega = 13$ MeV from sub-question (a) Sessions 6–7; $V_{\rm SO} = 1.17$ MeV from layer 1 Session 8; standard QM L·S operator) produces **all 7 empirical magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ at the empirical cumulative shell-closure positions** — zero free parameters, zero phenomenological inputs. HO-boundary magic gaps (2, 8, 20) match empirical to within 20% (CPP gaps 12.4, 10.7, 9.5 MeV vs empirical 12, 10, 8 MeV). Spin-orbit-driven magic gaps (28, 50, 82, 126) are 23–60% of empirical (all at CPP $V_{\rm SO} = 1.17$ MeV vs empirical 5, 4, 3, 2 MeV) — soft, but present. **The empirical magic-number sequence is now a CPP-derived prediction**, not an external input. The structural reason: the high-l j=l+1/2 orbitals' degeneracies $2(l+1)$ match exactly the empirical magic-number gaps from each HO-magic to the next empirical magic — a structural property of the angular-momentum algebra that any HO+L·S calculation produces for any positive $V_{\rm SO}$; CPP's contribution is the SCALE ($\hbar\omega$, $V_{\rm SO}$ both in the right ballpark). To restore empirical gap STRENGTH hierarchy where magic 50 dominates sub-magic 40 requires $V_{\rm SO}/\hbar\omega \gtrsim 0.20$–$0.25$, about 2–3× CPP layer-1's value 0.09; routes for closure: Approach A's higher $v_F/c$ values (giving $V_{\rm SO}/\hbar\omega \approx 0.12$–$0.15$), centrifugal $l^2$ correction to the K$_3$ HO mean field, higher-order relativistic corrections beyond $(v/c)^2$. **First qualitative cross-paradigm consilience claim of OPEN-SS-35 closure programme**: CPP — derived from 600-cell lattice geometry, K$_3$ alpha-cluster contacts, and SSV-PSR_eff relativistic kinematics — produces the empirical nuclear magic-number sequence at zero free parameters. Sub-question (b) Route B-α status: "B-α layer 1 closed; magnitude Level-1 partial" → "**layer 3 partial closure: shell SEQUENCE reproduced from CPP first-principles; gap magnitudes at soft end of empirical**". **Terminology correction registered:** Session 7 Phase 2 / Session 8 invoked "Dirac negative-energy mixing" for the relativistic origin of spin-orbit. This is conventional QFT terminology not used in CPP; corrected to CPP-native articulation: relativistic kinematics from the SR paper's $\textsf{PSR}_{\rm eff} = l_P/(1 + k\Delta\textsf{SSV})$ machinery, with the leading-order $(v/c)^2$ Thomas-precession factor derived as the SSV-PSR_eff modulation coupling between nucleon orbital motion and ZBW spin (the literal circular orbit of charge CPs in SS-2). Numerical content unchanged. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged. Companion sketch: `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3.md`. Companion script: `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3.py`.

**Update 2 May 2026 Session 10 (B-α layer 3 V_SO refinement: Routes 1a, 1b, 1c):** Sub-question (b) Route B-α layer 3 status refined: "shell SEQUENCE reproduced; gap magnitudes at soft end of empirical" → "**bounded refinement: simple HO + L·S framework saturates at $V_{\rm SO}/\hbar\omega \approx 0.11$; closure of gap-strength match requires cluster-surface Thomas-form spin-orbit or numerical diagonalization beyond Taylor expansion**". **Route 1b (centrifugal correction from K$_3$ Gaussian-modulated mean field) RULED OUT** as a magic-strength enhancement route. The K$_3$ potential expanded near the centroid gives quartic coefficient $C_4 = -m_n\omega^2/(8\sigma^2) < 0$; combined with HO matrix elements $\langle r^4 \rangle_{N, l} = (\hbar/m_n\omega)^2 \cdot f(N, l)$ where $f(N, l)$ is LARGER for low-l than high-l at fixed $N$ ($f(2,0)=18.75 > f(2,2)=15.75$; $f(4,0)=45.75 > f(4,2)=42.75 > f(4,4)=35.75$; $f(6,0)=84.75 > \ldots > f(6,6)=63.75$), this gives WRONG SIGN for empirical centrifugal enhancement: low-l states are lowered MORE by quartic than high-l, opposite of Bohr-Mottelson $D \cdot l(l+1)$ phenomenology where $D > 0$ lowers high-l. Plus first-order perturbation theory FAILS spatially for high-N states ($N = 4, 5, 6$ where spin-orbit-driven magics 28, 50, 82, 126 sit): $|\Delta E| \sim 60$–$140$ MeV exceeds $\hbar\omega = 13$ MeV, signaling that high-N HO wavefunctions extend beyond the Gaussian width and probe the cluster boundary where the K$_3$ potential transitions to its asymptotic form. **Route 1a (refined $v_F/c$ via Approach C surface-region emphasis):** at $A = 56$ between $A = 48$ icosahedron ($v_F/c = 0.307$) and $A = 40$ gyroelongated square bipyramid ($v_F/c = 0.356$), interpolated $v_F/c = 0.32$. $V_{\rm SO}/\hbar\omega = 0.090 \to 0.102$ (+13.8%). **Route 1c (higher-order relativistic via SSV-PSR_eff expansion):** $\textsf{PSR}_{\rm eff}/l_P = 1 - \alpha(v/c)^2 + \alpha^2(v/c)^4 - \ldots$ gives multiplicative correction $1 + \beta(v/c)^2 \approx 1.10$ on $V_{\rm SO}$ at $v_F/c = 0.32$. $V_{\rm SO}/\hbar\omega = 0.102 \to 0.113$ (+10.7%). **Combined Session 10 result: $V_{\rm SO}/\hbar\omega = 0.113$**, a 25% increase over Session 8 baseline 0.090; reaches 56% of empirical strong-magic threshold (0.20–0.25). Remaining gap factor 1.77–2.21. **Identification of missing physics:** (i) cluster-surface Thomas-form spin-orbit $V_{\rm SO}^{\rm surface} = \langle \xi(r) \rangle$ with $\xi(r) \propto -dV/dr$ peaking at cluster boundary; (ii) numerical diagonalization of full K$_3$ Hamiltonian beyond Taylor expansion. Both are multi-session work. Session 10 establishes the BOUND of what the simple HO + L·S framework can achieve. **Third programme-level negative-result demonstration in OPEN-SS-35 closure programme** (after Route D in Session 5 Phase 2 and Route B-γ in Session 7 Phase 2). OPEN-SS-35 closure trajectory: 6 programme-level stages preserved; first qualitative cross-paradigm consilience claim (Session 9) intact. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged. Companion sketch: `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3_VSO_refinement.md`. Companion script: `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3_VSO_refinement.py`.

**Update 2 May 2026 Session 11 Phase 1 (Path (i) cluster-surface Thomas-form spin-orbit RULED OUT):** Sub-question (b) Route B-α layer 3 status further refined: "bounded refinement: simple HO + L·S framework saturates at $V_{\rm SO}/\hbar\omega \approx 0.11$" → "**the K$_3$ Gaussian-modulated mean field framework is fundamentally insufficient for magic-strength gap closure; gap-strength match requires additional CPP physics beyond the smooth Gaussian-bottom mean field**". Phase 1 of the multi-session arc identified in Session 10 as Priority 1 (cluster-surface Thomas-form spin-orbit) tested whether the spherically-averaged K$_3$ Gaussian-modulated mean field at $A = 56$ produces a Thomas-form weight $f_{\rm SO}(r) = (1/r) \cdot dV_{\rm avg}/dr$ that enhances $V_{\rm SO}^{\rm eff}$ for high-l surface-localized states (in the way Bohr-Mottelson Woods-Saxon does). For $N_\alpha = 14$ alphas at $R_{\rm cluster} = 2.37$ fm with $\sigma = 1.7855$ fm, the spherically-averaged shell potential $V_{\rm avg}(r) = -(N_\alpha V_0 \sigma^2)/(2 r R) [\exp(-(r-R)^2/2\sigma^2) - \exp(-(r+R)^2/2\sigma^2)]$ has well depth $V_{\rm avg}(0) = -67.93$ MeV. **Crucially, $f_{\rm SO}(r)$ peaks at the cluster CENTER ($f_{\rm SO}(0) = 8.79$ MeV/fm$^2$) and decreases monotonically outward** ($f_{\rm SO}(R_{\rm cluster}) = 7.18$, $f_{\rm SO}(5\text{ fm}) = 1.53$ MeV/fm$^2$) — opposite of Bohr-Mottelson Woods-Saxon $df/dr/r$ which peaks at the surface. **Matrix elements $\langle f_{\rm SO} \rangle_{0,l}$ in HO basis decrease monotonically with l**: 7.41 (l=0), 6.31 (l=1), 5.24 (l=2), 4.27 (l=3), 3.43 (l=4), 2.72 (l=5), 2.14 (l=6) MeV/fm$^2$ — factor 3.5× reduction from l=0 to l=6. With calibration $K = V_{\rm SO}^{\rm central}/\langle f_{\rm SO} \rangle_{0,0} = 0.158$ fm$^2$ anchored to Session 8 baseline 1.17 MeV at l=0, **$V_{\rm SO}^{\rm eff}(l)$ DECREASES with l**: 1.170 (l=0), 0.997 (l=1), 0.828 (l=2), 0.675 (l=3, magic 28), 0.542 (l=4, magic 50), 0.430 (l=5, magic 82), 0.338 (l=6, magic 126) MeV — V_SO_eff(l=6) is only 29% of central baseline and 13% of empirical strong-magic threshold (0.20). **Worse than Session 9's uniform $V_{\rm SO} = 1.17$ MeV** for the high-l j-shell partners that close empirical magics 28–126. **Structural diagnosis:** the K$_3$ Gaussian-modulated mean field has a *fuzzy* surface ($\sigma/R_{\rm cluster} = 0.75$ at $A = 56$), in contrast to Woods-Saxon's *sharp* surface ($a/R \sim 0.1$ in conventional nuclear physics) — a factor ~7× more diffuse. The geometric deficiency is shape-level, not perturbation-level: cannot be fixed by parameter adjustment within the K$_3$ Gaussian-bottom framework. **Path (i) cluster-surface Thomas-form spin-orbit RULED OUT** as a magic-strength enhancement route. **Fourth programme-level negative-result demonstration in OPEN-SS-35 closure programme** (after Route D in Session 5 Phase 2, Route B-γ in Session 7 Phase 2, Route 1b in Session 10). **Path (ii) numerical diagonalization status: still formally open but with substantially reduced expectations** — the geometric deficiency is shape-level, so numerical refinement of the same shape should not reverse the qualitative conclusion. **Programme implication:** gap-strength closure of OPEN-SS-35 sub-question (b) layer 3 requires CPP physics *outside* the simple K$_3$ Gaussian + HO + L·S + V_SO refinement framework. Candidate avenues: (a) sharper-surface contributions from K$_3$ edge mechanism + Pauli-blocking at the cluster boundary; (b) additional binding terms beyond the Gaussian sum (higher-order K$_3$ modes, color-coupling at cluster-internal scale); (c) L·S operator structure beyond Bohr-Mottelson form (interacts with OPEN-SS-16 Layer B); (d) recognition that empirical magic-strength hierarchy may not be solely a mean-field property (pairing, deformation, other nuclear-structure effects). All four avenues are multi-session by scope. OPEN-SS-35 closure trajectory: 6 programme-level stages preserved (Phase 1 refines stage (vi) but does not advance to a new stage). **First qualitative cross-paradigm consilience claim (Session 9) remains intact**: the empirical magic-number SEQUENCE is reproduced from CPP first-principles. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged. Companion sketch: `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3_cluster_surface_phase1.md`. Companion script: `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3_cluster_surface_phase1.py`.

**Update 4 May 2026 Session 12 (R1 — R$_\alpha$ scale-dependence as A-scaling closure RULED OUT):** Sub-question (a) A-scaling Resolution R1 (registered Session 7 Phase 1 sketch §3.3) tested via the CPP-native DP-sea Coulomb screening mechanism (SS-7 §11, OPEN-SS-25). R1 hypothesizes that internal-contact screening compresses $R_\alpha$ at large clusters and that this compression closes the empirical $\hbar\omega \propto A^{-1/3}$ vs CPP $A^{-0.10}$ discrepancy. **Three findings, all robust:** (i) **Sign of energetic mechanism is wrong.** Force-balance with screened Coulomb $V_{\rm K_3}'(R^*) + f_{\rm eff}^2 \cdot V_{\rm Coul}'(R^*) = 0$ gives $R_\alpha$ COMPRESSION inward at $f_{\rm eff} < 1$, robust across all reasonable K$_3$ well parametrizations ($\sigma \in [1.0, 2.5]$ fm). Empirical match requires $R_\alpha$ to EXPAND with $A$ (lower $\hbar\omega$ = larger $R_c$ = larger $R_\alpha$ at fixed shape). R1 produces compression; the opposite of what's needed. No CPP-native energetic mechanism (DP-sea screening, Pauli blocking at internal contacts, K$_3$ well broadening) gives expansion. (ii) **Pattern is non-monotonic, U-shaped — not power law.** Inverting CPP/empirical ratios to ask "what $R_\alpha(A)$ would close the gap" yields: endpoints (regular polytopes $N_\alpha = 4$: $-5.3\%$; $N_\alpha = 12$: $-0.7\%$) match empirical to within 1-10%; mid-range J-solids ($N_\alpha = 5$-$10$) need 7-23% expansion peaking at $N_\alpha = 10$ ($+22.7\%$). **No monotonic $R_\alpha(A)$ law produces this pattern.** Discrepancy is shape-driven (J-solid mid-range overshoot), not radius-driven. Structural similarity to **SS-7 OPEN-SS-32 J-solid regime** (oblate-deformation activation at $N_\alpha \in \{7, 8, 9, 10\}$, $+0.55 B_{\rm pair}$ excess in SS-7 binding-energy fit) registered as forward pointer for future-session investigation. (iii) **Decoupling Theorem.** In the CPP B-α layer 1 framework, $V_{\rm SO} = (v_F/c)^2 \cdot \hbar\omega$, so the dimensionless ratio $V_{\rm SO}/\hbar\omega = (v_F/c)^2 = 0.090$ is INDEPENDENT of $\hbar\omega$ magnitude. Therefore A-scaling closure (R1 or R2) does NOT touch the layer-3 gap-strength deficit identified in Session 11 Phase 1: even if $\hbar\omega^{\rm CPP}$ were scaled to empirical 10.7 MeV, $V_{\rm SO}^{\rm CPP}$ would also scale (to $0.96$ MeV) and the ratio remains 0.090 — far below empirical 0.14 and threshold 0.20-0.25. The Session 7 sketch §6 implicit assumption that A-scaling closure would benefit layer 3 is refuted; the pathway to gap-strength closure is via $v_F/c$ (or modification of the layer-1 relationship), not via $\hbar\omega$. **R1 RULED OUT** as A-scaling closure. **Fifth programme-level negative-result demonstration in OPEN-SS-35 closure programme** (after Route D in Session 5 Phase 2, Route B-γ in Session 7 Phase 2, Route 1b in Session 10, Path (i) cluster-surface Thomas-form in Session 11 Phase 1). **R2** (cluster-scale vs alpha-scale mean field interpretation, Session 7 sketch §3.3) is the only remaining A-scaling closure candidate; consistent with U-shape diagnostic but multi-session by scope. **Programme effect:** R1 status moves from "candidate resolution" to "RULED OUT". U-shape diagnostic converts the Session 7 "weak A-scaling" finding into a more specific "J-solid mid-range overshoot" diagnostic with structurally-motivated forward pointer to OPEN-SS-32. Decoupling Theorem narrows the gap-strength closure candidate list by removing A-scaling fixes from it (sharpens Session 11 Phase 1 conclusion that "additional CPP physics outside simple K$_3$ Gaussian-modulated mean field framework" is needed for gap-strength closure). **Six programme-level stages preserved**; first qualitative cross-paradigm consilience claim (Session 9) intact; Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances unchanged. Companion sketch: `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a_Ascaling_R1_RULED_OUT.md`. Companion script: `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_a_Ascaling_R1.py`.

**What a solution looks like:** A first-principles derivation that shows under A1–A11 + bound-nucleon assumptions, the nucleon shell-organization recovers the magic-number sequence exactly. **Adopted closure route (Route A):** (a) derive 3D harmonic-oscillator mean-field for nucleons from K$_3$ collective-mode structure of alpha-alpha contacts; (b) derive spin-orbit coupling strength from ZBW phase correlations + nuclear $v/c$; (c) verify $V_{\rm SO}/\hbar\omega$ is in the magic-number-producing range across the bound-nucleon regime. The Level-0 consistency check (Phase 2 work) shows scales align; closure is multi-session but well-motivated.
**Dependencies:** Inherits from SS-1/SS-2/SS-3 (lattice geometry, nucleon structure), SS-5 (K$_3$ closure-bonus mechanism), SS-7 ($R_\alpha$ from alpha-cluster regime), and SS-8 (2$E$/$V$ scaling). Closure of OPEN-SS-35 would unlock OPEN-SS-34 from "Level-1 derived under H3" to "Level-2 derived from CPP primitives" AND unlock OPEN-SS-36 (per 4th sub-arc closure+shell decomposition where $B_{\rm shell}$ requires CPP shell-magic derivation). The two open problems are not independent — OPEN-SS-35 is the single deepest dependency for both.
**Cross-sector connections:** This is the deepest cross-paradigm consilience target the programme has identified. The shell-model magic-number sequence is a load-bearing structural feature of all standard nuclear physics; deriving it from CPP primitives would be a cross-paradigm consilience claim of the same magnitude as deriving the QCD $\beta_0 = 7$ from cage geometry (PRED-C-10) but at the nuclear-shell scale. The Pattern-6 K$_3$ scale-recurrence would extend to a 7th confirmed instance (nucleon-orbital-organization scale) once sub-question (a) closes.
**Current best lead:** Route A (HO + spin-orbit from CPP). Sub-question (a) — derivation of HO mean-field from K$_3$ collective modes — is single-session-tractable for an initial sketch. Empirical reinforcement: Session 5 Phase 1 lookup confirmed $B_{\rm slip}$ acceleration toward ${}^{100}$Sn doubly-magic boundary, validating that shell-closure structure is genuinely active in the alpha-chain regime.
**Falsification route:** A direct CPP derivation that produces a *different* magic-number sequence (e.g., 30, 52, 84 instead of 28, 50, 82) would falsify both the OPEN-SS-34 derivation and CPP's cross-paradigm consistency. Empirical: the standard magic numbers are extensively confirmed in nuclear data (binding-energy peaks, separation-energy discontinuities, etc.), so a CPP derivation must produce these exactly. **Negative-result demonstration:** Route D (direct 600-cell lattice-shell counting) ruled out by explicit computation, ensuring future closure work focuses on nucleon-orbital structure (Route A) rather than lattice geometry.
**Paper(s):** SS-9 sketches `SS-9_OPEN-SS-34_derivation_attempt.md` (where OPEN-SS-35 was first registered), `SS-9_OPEN-SS-36_derivation_attempt.md` (where leverage was doubled), `SS-9_OPEN-SS-35_scoping.md` (this work, Phase 2 scoping with Level-0 consistency check); SS-10+ candidate (closure paper).
**Registered:** 2 May 2026 Session 4 follow-up 3rd sub-arc in OPEN-SS-34 derivation §8 (formal registry entry pending ratification); **scoping document 2 May 2026 Session 5 Phase 2.**

---

### OPEN-SS-36: Programme-Level Closure of $B_{\rm slip}$ Structure — Refined to Closure-Plus-Shell Decomposition
**Status:** OPEN — registered as candidate, Level-1 partial closure + self-correction (registered 2 May 2026 Session 4 follow-up 3rd sub-arc as constant-$\sqrt{3}$ candidate; **REVISED 2 May 2026 Session 4 follow-up 4th sub-arc** to correct the constant-form over-claim)
**Sector(s):** SS (nuclear physics, K$_3$ scale-recurrence)
**Priority:** MEDIUM (now identified as structurally dependent on OPEN-SS-35; closure follows from OPEN-SS-35 closure)
**One-line statement:** Derive from CPP primitives (A1–A11) the structure of $B_{\rm slip}(N_\alpha) = B_{\rm pair} + B_{\rm shell}(N_\alpha)$, where $B_{\rm pair}$ is the universal SS-5-style closure-bonus quantum (Level-1 already established under H1 = K$_3$ closure-bonus mechanism inherited from SS-5) and $B_{\rm shell}(N_\alpha)$ is an N-dependent shell-closure-influence piece growing from $\approx \frac{1}{2} B_{\rm pair}$ at ${}^{56}$Ni to $\approx 1 \, B_{\rm pair}$ at ${}^{88}$Ru as the cluster approaches the ${}^{100}$Sn doubly-magic boundary.
**Self-correction note:** The original 2 May 2026 3rd sub-arc registration proposed $B_{\rm slip} = \sqrt{3} \cdot B_{\rm pair}$ as a constant Pattern-6-natural form via three-K$_3$-mode SU(2) symmetric coupling at the satellite-attachment face. Closer empirical analysis under the OPEN-SS-36 closure attempt (4th sub-arc) showed $B_{\rm slip}$ is NOT constant — it grows from $1.51 \, B_{\rm pair}$ at $N_\alpha = 14$ to $1.94 \, B_{\rm pair}$ at $N_\alpha = 22$. The constant-$\sqrt{3}$ value (=1.73) was a midpoint-fit artifact. Additionally, the SU(2)-coupling argument was geometrically inconsistent with the slope-1 satellite topology established in OPEN-SS-34 (T2): a satellite cannot face-coincide with three core-alphas simultaneously (rigid-tetrahedron geometry forbids it). The constant-$\sqrt{3}$ form is RETIRED in favor of the refined closure+shell decomposition. This is the first programme-level claim retirement since OPEN-SS-22 was retired on 21 April 2026.
**What a solution looks like:** A first-principles derivation that produces (a) the closure-bonus piece $+B_{\rm pair}$ at the deltahedron-core scale (Level-1 already complete via SS-5 generalization); (b) the shell-closure-influence piece $B_{\rm shell}(N_\alpha)$ as an explicit N-dependent function emerging from CPP shell structure. The latter requires CPP closure of the shell-magic-number sequence (OPEN-SS-35); without OPEN-SS-35, $B_{\rm shell}$ is a structural-influence parameter inherited from H3.
**Dependencies:** Inherits from SS-5 (K$_3$ closure-bonus mechanism), SS-7 (alpha-alpha edge K$_3$ contact), and OPEN-SS-34 Level-1 derivation. **Now identified as structurally dependent on OPEN-SS-35.** Closure of OPEN-SS-35 would unlock OPEN-SS-36 by deriving the shell-closure profile from CPP primitives. The two open problems are not independent — OPEN-SS-35 is the deepest dependency.
**Cross-sector connections:** Pattern-6 K$_3$ scale-recurrence at the alpha-cluster scale is preserved at the closure-bonus piece (deltahedron-core closure $+B_{\rm pair}$ is the 6th confirmed instance). The "satellite-attachment $\sqrt{3}$-coupled mode" was the 7th provisional instance in the 3rd sub-arc but is REMOVED from the Pattern-6 catalog with this self-correction (count returns to 6 confirmed + 1 provisional from OPEN-SS-32).
**Current best lead:** The closure-bonus piece is fully derivable under SS-5's mechanism. The shell-closure profile $B_{\rm shell}(N_\alpha)$ requires OPEN-SS-35 closure; in the meantime, the empirical profile (from $\frac{1}{2} B_{\rm pair}$ at ${}^{56}$Ni to $1 \, B_{\rm pair}$ at ${}^{88}$Ru) is approximately linear with the satellite count's distance to the ${}^{100}$Sn doubly-magic boundary at $N_\alpha = 25$.
**Falsification route:** Better-precision binding-energy data on the satellite-regime nuclei (especially ${}^{92}$Pd, ${}^{96}$Cd, where the empirical $B_{\rm shell}$ profile is currently poorly constrained) would discriminate between candidate structural forms. A direct CPP derivation that produces a different N-dependence than observed would falsify OPEN-SS-36 closure.
**Paper(s):** SS-9 sketch `SS-9_OPEN-SS-36_derivation_attempt.md` (this work, with full self-correction); SS-9 sketch `SS-9_OPEN-SS-34_derivation_attempt.md` §6 (the original 3rd sub-arc constant-$\sqrt{3}$ proposal that this work corrects); SS-10+ candidate (full closure attempt likely a separate paper given dependence on OPEN-SS-35).
**Registered:** 2 May 2026 Session 4 follow-up 3rd sub-arc (original constant-$\sqrt{3}$ proposal); REVISED 2 May 2026 Session 4 follow-up 4th sub-arc (refined closure+shell decomposition with $\sqrt{3}$ retirement).

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
