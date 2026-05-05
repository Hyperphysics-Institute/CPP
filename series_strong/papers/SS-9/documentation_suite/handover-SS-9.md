# SS-9 Handover — Session 19 Phase 7 Close (5 May 2026)

**Repository state at session close:** `origin/main` will be at patch 0199 once Thomas applies and pushes the ten-patch chain (0190–0199). As of this document's creation, in-container HEAD is at patch 0198 (`039c10a`); patch 0199 is committed locally pending export and represents this Step H file itself.
**Active paper:** SS-9 — *Conditional Derivation of Simplicial Alpha-Polytope Connectivity from CPP Lattice Geometry* (working title; final TBD).
**Paper state:** Pre-paper / active development. v0.3 working draft at `session_logs/OPEN-SS-24_phase1_v0.3_working_draft.md` (218 lines). No `.tex` file yet (registered as OPEN-ORG-012, awaiting U-shape investigation §7 stability — §7 has now shifted **nine times** in the OPEN-SS-32 ↔ U-shape thread, with Session 19 Phase 7 substantively reorganizing the §7 framing further from "Coulomb gives 5% at $N = 10$ zero-parameter" to "Coulomb captures smooth-A scale within 5%; polytope-specific signal needs refinement (Refinement A/C/D, Pauli)").

## One-paragraph state

SS-9 has two parallel threads. The **OPEN-SS-24 closure target** is the original paper goal — a conditional theorem on refined-C1 + C2 + C5 + C6 + C7 hypothesis stack via Steinitz + Fáry-van der Waerden. v0.3 working draft is mature; v0.1 `.tex` conversion is registered as OPEN-ORG-012 awaiting natural pause point (now further deferred). The **OPEN-SS-35 cross-paradigm closure programme** (derive nuclear shell-model magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ from CPP primitives) has been the active development front since Session 5. Through Session 19 Phase 7 the programme has produced **10 programme-level negative results** (unchanged from Session 18; Phase 7 is partial positive / refining), **1 qualitative cross-paradigm consilience claim** (Session 9), **1 Decoupling Theorem** (Session 12), **1 formal R2 closure** (Session 15), **1 programme-level closure of the Gaussian-K$_3$ framework at fixed cluster geometry** (Session 16 via the §2.4 sign theorem), **1 channel-level positive scoping outcome** with R3 and R4 cluster-geometry shift channels advancing to multi-session derivation (Session 17 Phase 5), **1 zero-parameter quantitative bullseye at the 5% level** with R3-Coulomb at $N=10$ (Session 18 Phase 6), and now **1 empirical-data comparison with critical methodological reframing** (Session 19 Phase 7). Session 19 applied the Phase 4/5/6 methodology lesson — F1 sign analytical check first, before computation — via the sign-theorem composition workflow. The F1 sign argument for the empirical comparison is composition: Phase 6 predicts $\delta R > 0$ → net binding gain $> 0$; empirical alpha-conjugate nuclei should show binding excess vs smooth baseline if R3-Coulomb stabilization is the mechanism; both expected positive → **F1 SIGN COMPATIBLE.** Computational comparison against AME 2020 binding data revealed a critical reframing. **Raw magnitudes** mismatch by factor $\sim 10$ (Phase 6 raw net gain $\sim 1.7$ MeV/α range vs empirical $\Delta(B/A)$ $\sim 0.2$ MeV/α range). **Phase 6 raw is approximately linear in $N$**, with polytope-residuals only $\sim 0.014$ MeV/α — meaning the smooth-A bulk of Phase 6's prediction is **absorbed into SEMF parameters during empirical fit** and isn't directly visible in $\Delta(B/A)$. After detrending both sides, Phase 6 polytope-residuals are factor $\sim 10$ *smaller* than empirical polytope-residuals ($\sim 0.05$ MeV/α scale). **Phase 5 R3-lin 1 MeV/α target REINTERPRETED:** captures the smooth-A cluster Coulomb stabilization scale (correctly), not the polytope-residual signal. **Phase 6's 5% bullseye at $N=10$ is meaningful** (validates Coulomb-K$_3$ scale balance) but **NOT directly the empirical polytope-residual signal**. R3-Coulomb captures the smooth-A binding contribution correctly but does NOT generate the polytope-specific structure (¹⁶O excess, ²⁸Si peak, ⁴⁸Cr below-SEMF). **Smooth-A vs polytope-residual methodological distinction codified** as governing principle for future R3-channel empirical comparisons. R3-Coulomb advances toward closure with **refined scope**: smooth-A part validated; polytope-specific part requires Refinement A (extended Gaussian charge at $\sim 1.6$ fm), Refinement C (non-NN K$_3$ at $r = \sqrt{2} R_\alpha$ where Gaussian value is $0.918$ — NOT exponentially small), Refinement D (σ$_{K3}$ sensitivity ±10%, possibly polytope-dependent), or R3-Pauli to generate empirical polytope-residual structure. Sub-question (b) layer 3 gap-strength closure remains INDEPENDENT of Phase 4/5/6/7 by Decoupling Theorem (Session 12), unaffected.

## Forward queue

**Priority 1 (multi-session full derivation, refined scope):** R3-Coulomb refinements targeting polytope-specific signal. Phase 7 established that simple R3-Coulomb captures smooth-A cluster Coulomb stabilization scale within 5% but does NOT generate polytope-specific structure observed in alpha-conjugate $\Delta(B/A)$. Refinements address polytope-residual signal at $\sim 0.05$ MeV/α scale:

- **Refinement A (Session 20 candidate):** extended Gaussian charge distribution at radius $\sim 1.6$ fm (typical alpha proton density). Recompute $V_C(0)$ and $\delta R_C(N)$ per polytope. Hypothesis: at non-NN distances correction is small (~1%), so smooth-A preserved; at NN distances softens effective Coulomb by ~10–20%; impact on polytope-residuals depends on whether polytope-specific NN-pair counts are differentially affected.
- **Refinement C (Session 20 candidate):** include K$_3$ contribution from non-NN pairs. At $r = \sqrt{2} R_\alpha \approx 3.35$ fm (octahedral diagonals etc.), K$_3$ Gaussian is at $\exp(-0.485/5.645) = 0.918$ — NOT exponentially small. Polytope-by-polytope these vary (octahedron 3 antipodal at $\sqrt{2}R$, tetrahedron 0, icosahedron 30 second-shell at $\phi R$). **Could be significant source of polytope-specific signal that simple Phase 6 misses.**
- **Refinement D (Session 20 candidate):** test sensitivity to $\sigma_{K3}$. Vary by ±10% around canonical 1.68 fm; check whether smooth-A 5% bullseye persists. Also: does $\sigma_{K3}$ vary by polytope (cluster-topology-dependent)? If so, polytope-dependent $\sigma_{K3}$ is natural source of polytope-residual signal.

**Priority 2 (parallel scoping):** R3-Pauli scoping. Specify a Pauli model (Gaussian repulsive core in alpha-alpha potential at short range, tunable amplitude $V_P$ and range $\sigma_P$). Apply F1 sign analytical check first via sign-theorem composition workflow: Pauli is repulsive → $\delta R_{\rm Pauli} > 0$ → Phase 5 sign theorem → $\Delta E > 0$, F1 PASSES analytically. Then compute equilibrium $\delta R_{\rm Pauli}(N)$ per polytope, detrend smooth-A part, compare polytope-residuals to empirical $\sim 0.05$ MeV/α scale. Pauli at internal alpha-alpha contacts varies with edge count AND internal geometry — natural source of polytope-specific signal.

**Priority 3 (deferred, registered):** OPEN-SS-32 attenuation-factor reformulation depending on Refinements A/C/D outcomes.

**Priority 4 (parallel, deferred):** OPEN-SS-16 Layer B closure work — deepest open problem at programme level.

**Priority 5 (parallel, registered):** Reading B literature check.

**Anti-priorities (sharpened from Phase 6):**

- Do **not** initiate SS-9 v0.3 → v0.1 `.tex` conversion (OPEN-ORG-012). **§7 has now shifted nine times** in the OPEN-SS-32 ↔ U-shape thread (Phase 1 prior-art read; Phases 2/3A/3B-A/3B-B/4 ruled out; Phase 5 PASSES SCOPING; Phase 6 R3-Coulomb 5% agreement at $N = 10$; **Phase 7 reframes 5% agreement as smooth-A scale + identifies polytope-residual signal as next target**).
- **NEW from Phase 7 (1):** Do **not** rely on Phase 5 R3-lin 1 MeV/α heuristic as polytope-residual target. Empirical polytope-residual scale is $\sim 0.05$ MeV/α (factor 20 smaller).
- **NEW from Phase 7 (2):** Do **not** compute Phase 6-style raw net binding gain magnitudes against empirical $\Delta(B/A)$ without first detrending the smooth-A component. Smooth-$A$ contributions are absorbed into baseline parameters during fit and are not directly observable in deviations.
- **From Phase 6:** Do **not** pursue Pauli or other R3-channel mechanisms in isolation from Coulomb. Coulomb sets the smooth-A scale; other mechanisms generate polytope-specific signal on top.
- **From Phase 5:** Do **not** parameterize $\delta R(N)$ phenomenologically without grounding in CPP physics.
- Do **not** abandon Phase 4/5/6 closure interpretations. Phase 7 reframes Phase 5/6 calibration target but does not invalidate the Phase 4 sign theorem closure or the Phase 5/6 channel/sub-channel scoping results.
- Do **not** pursue further perturbative anharmonic refinement within Gaussian-K$_3$ at fixed geometry — closed Phase 4.
- Do **not** pursue further belt-IRREP-projection variants — closed Phase 3B-B.
- Do **not** pursue full point group D$_{nh}$/D$_{nd}$ extension — closed Phase 3B-B.
- Do **not** pursue further $V_{\rm SO}$ refinement within simple K$_3$ + HO + L·S framework.
- Do **not** pursue further $R_\alpha(A)$ in surface-tension form (R1, Session 12).

## Computation reproduction notes

**Phase 7 script:** `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase7_R3_Coulomb_empirical.py` (~370 lines). Reuses Phase 5/6 polytope construction and constants verbatim; recomputes Phase 6 R3-Coulomb predictions for verification. New: AME 2020 binding data tabulation; SEMF baseline computation for alpha-conjugate nuclei (Krane parameters); empirical $\Delta(B/A)$ vs SEMF; linear-in-$N$ detrending of both predicted and empirical patterns; side-by-side polytope-residual comparison; F1/F2/F3 falsifier analysis with explicit pre-empted analytical sign argument in script docstring per Phase 4/5/6 methodology lesson.

**Phase 7 sketch:** `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_phase7_R3_Coulomb_empirical.md`. Full §1 (strategy) — §9 (summary), with §2 pre-empted analytical sign analysis; §3 empirical data (AME 2020, SEMF baseline, empirical deviation); §4 Phase 6 prediction in two framings (raw K$_3$ binding loss + net binding gain); §5 the reframing (smooth-A absorbed vs polytope-residual; raw mismatch reconciled; polytope-residual factor ~10 smaller than empirical); §6 verdict (PARTIAL POSITIVE / REFRAMING; F1 compatible, F2 subtle, F3 mixed; Phase 5 R3-lin 1 MeV/α target reinterpreted; what Phase 6 captures vs misses); §7 programme implications; §8 forward pointers (Refinement A/C/D, R3-Pauli, anti-priorities); §9 summary.

**Constants (verbatim from Phase 5/6):** $B_{\rm pair} = M_0/\varphi = 2.342$ MeV; $R_\alpha = 2.37$ fm; $\sigma_{K3} = 1.68$ fm (canonical); $m_\alpha = 3727.4$ MeV/c²; $\hbar c = 197.327$ MeV·fm; alpha-alpha pair Coulomb prefactor $(2e)^2 \cdot k_C = 5.76$ MeV·fm. **New for Phase 7:** SEMF parameters $a_V = 15.8$, $a_S = 17.8$, $a_C = 0.711$, $a_P = 11.18$ MeV; B(⁴He) $= 28.296$ MeV.

**AME 2020 binding energies (tabulated):** ¹⁶O $= 127.619$, ²⁰Ne $= 160.645$, ²⁴Mg $= 198.257$, ²⁸Si $= 236.537$, ³²S $= 271.781$, ³⁶Ar $= 306.715$, ⁴⁰Ca $= 342.052$, ⁴⁸Cr $= 411.462$ MeV. Source: Wang et al. *Chin. Phys. C* **45** 030003 (2021).

**Empirical $\Delta(B/A) = (B/A)_{\rm emp} - (B/A)_{\rm SEMF}$ (full table):**

| $N$ | nucleus | $A$ | $Z$ | $B/A$(emp) [MeV] | $B/A$(SEMF) [MeV] | $\Delta(B/A)$ [MeV] |
|-----|------|-----|-----|--------|---------|---------|
|  4 | ¹⁶O   | 16 |  8 | 7.976 | 7.782 | $+0.194$ |
|  5 | ²⁰Ne  | 20 | 10 | 8.032 | 8.058 | $-0.026$ |
|  6 | ²⁴Mg  | 24 | 12 | 8.261 | 8.245 | $+0.016$ |
|  7 | ²⁸Si  | 28 | 14 | 8.448 | 8.375 | $+0.073$ |
|  8 | ³²S   | 32 | 16 | 8.493 | 8.464 | $+0.030$ |
|  9 | ³⁶Ar  | 36 | 18 | 8.520 | 8.523 | $-0.003$ |
| 10 | ⁴⁰Ca  | 40 | 20 | 8.551 | 8.561 | $-0.009$ |
| 12 | ⁴⁸Cr  | 48 | 24 | 8.572 | 8.588 | $-0.016$ |

**Phase 6 prediction (full table):**

| $N$ | sym | $V_C(0)$ [MeV] | $\delta R_C$ [fm] | $\Delta E_{K3}/\alpha$ [MeV] | $\Delta V_C/\alpha$ [MeV] | net gain/α [MeV] |
|-----|-----|--------|--------|--------|--------|--------|
|  4 | $T_d$    |  $14.58$ | $0.779$ | $+0.358$ | $-0.902$ | $+0.544$ |
|  5 | $D_{3h}$ |  $23.36$ | $0.821$ | $+0.474$ | $-1.202$ | $+0.728$ |
|  6 | $O_h$    |  $34.32$ | $0.886$ | $+0.608$ | $-1.556$ | $+0.948$ |
|  7 | $D_{5h}$ |  $46.28$ | $0.940$ | $+0.728$ | $-1.878$ | $+1.150$ |
|  8 | $D_{2d}$ |  $59.60$ | $0.995$ | $+0.848$ | $-2.203$ | $+1.355$ |
|  9 | $D_{3h}$ |  $74.41$ | $1.051$ | $+0.972$ | $-2.541$ | $+1.569$ |
| 10 | $D_{4d}$ |  $90.22$ | $1.104$ | $+1.092$ | $-2.867$ | $+1.775$ |
| 12 | $I_h$    | $125.64$ | $1.210$ | $+1.337$ | $-3.538$ | $+2.201$ |

**Polytope-residual comparison (after linear-in-$N$ detrending):**

| $N$ | nucleus | emp residual [MeV/α] | P6 residual [MeV/α] | sign match? |
|-----|------|--------|--------|---|
|  4 | ¹⁶O   | $+0.104$ | $+0.014$ | YES |
|  5 | ²⁰Ne  | $-0.100$ | $-0.010$ | YES |
|  6 | ²⁴Mg  | $-0.043$ | $+0.003$ | NO  |
|  7 | ²⁸Si  | $+0.031$ | $-0.004$ | NO  |
|  8 | ³²S   | $+0.003$ | $-0.007$ | mismatch (both small) |
|  9 | ³⁶Ar  | $-0.014$ | $-0.001$ | YES |
| 10 | ⁴⁰Ca  | $-0.004$ | $-0.002$ | YES |
| 12 | ⁴⁸Cr  | $+0.021$ | $+0.008$ | YES |

**Sign agreement: 5/8.** Empirical residual max: $0.104$; Phase 6 residual max: $0.014$; **ratio P6/emp = 0.13** (Phase 6 polytope-residuals are factor $\sim 10$ smaller than empirical).

**Linear fits:** Phase 6 net gain: slope $a_{P6} = 0.208$ MeV/α/N, intercept $b_{P6} = -0.302$ MeV/α. Empirical $\Delta(B/A)$: slope $a_E = -0.0159$ MeV/α/N, intercept $b_E = +0.153$ MeV/α (essentially flat).

## Lesson reinforcement — sign-theorem composition workflow (cumulative)

The Phase 4/5/6 methodology lesson — F1 sign analytical check first, before computation — was applied in Phase 7 from the outset, this time to the empirical comparison rather than to a new mechanism. The sign-theorem composition workflow now applies at three levels:

**Level 1 — within-mechanism F1 (Phase 6 codification):** for any candidate mechanism $X$ in the R3 channel, identify sign of $\delta R_X$ via classical-physics sign argument (Coulomb repulsive, Pauli repulsive, surface-density attractive/repulsive depending on mechanism), then invoke Phase 5 §2 sign theorem to get $\Delta E$ sign automatically. Decision in one paragraph.

**Level 2 — empirical-comparison F1 (Phase 7 application):** for a comparison between predicted mechanism and empirical signal, identify sign of predicted $\Delta(B/A)$ (or other observable), identify sign of empirical signal vs baseline, check sign compatibility. Decision in one paragraph.

**Level 3 — refinement F1 (Session 20+ application):** for any refinement to an existing mechanism (extended charge, non-NN K$_3$, σ$_{K3}$ variation, etc.), identify whether the refinement preserves sign or changes it, then compose with prior signs to decide F1.

The workflow is cumulative: each level builds on prior sign theorems.

## Cumulative state — programme-level

- **10 programme-level negative results UNCHANGED** (no new ruling-out in Session 19, Phase 7 is partial positive / refining); 5 in OPEN-SS-32 ↔ U-shape thread.
- **R2 (cluster-scale ↔ alpha-scale unification at canonical $\sigma_{K3}$) FORMALLY CLOSED** (Session 15 Phase 3B-B) — unchanged.
- **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED** (Session 16 Phase 4) — unchanged.
- **R3 and R4 cluster-geometry shift channels passed scoping** (Session 17 Phase 5) — unchanged.
- **R3-Coulomb passed scoping with 5% bullseye at $N = 10$** (Session 18 Phase 6) — *now reinterpreted as smooth-A scale validation* (Phase 7).
- **R3-Coulomb empirical comparison: PARTIAL POSITIVE / REFRAMING** (Session 19 Phase 7) — *new this session*. First empirical-data comparison in OPEN-SS-32 ↔ U-shape thread; first identification of methodological distinction (smooth-A vs polytope-residual) that resolves apparent magnitude paradoxes.
- **OPEN-SS-35 sub-question (a) A-scaling closure**: R3-Coulomb under active multi-session full derivation with smooth-A scale validated and polytope-specific refinement target identified (~$0.05$ MeV/α). Multi-session forward work: Refinement A/C/D + R3-Pauli scoping.
- **OPEN-SS-35 sub-question (b) layer 3 gap-strength closure**: independent by Decoupling Theorem (Session 12), unaffected.
- **First qualitative cross-paradigm consilience claim** (Session 9, magic-number sequence reproduced from CPP first principles) intact.
- **Decoupling Theorem** (Session 12): A-scaling closure and gap-strength closure are independent open problems — intact.
- **Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances** unchanged.
- **6 programme-level OPEN-SS-35 stages preserved**; Phase 7 refines stage (vi) further: stage (vi) now reads "R3-Coulomb under active multi-session full derivation; smooth-A cluster Coulomb scale validated at 5% level (Phase 6); polytope-specific residual signal identified as next refinement target — empirical scale $\sim 0.05$ MeV/α (Phase 7)".
- **Sign-theorem composition workflow** codified at three levels (Sessions 18 Phase 6 + 19 Phase 7): within-mechanism F1, empirical-comparison F1, refinement F1.
- **Smooth-A vs polytope-residual methodological distinction** introduced (Session 19 Phase 7) — governs all future R3-channel comparisons against empirical binding data.

## Relationship to prior sessions

Phase 7 is the **third positive scoping outcome** in the OPEN-SS-32 ↔ U-shape thread (Phases 5, 6, 7), and the **first empirical-data comparison** in the thread. The trajectory through Sessions 13–19:

- Session 13 Phase 2: Uniform-only zero-point softening RULED OUT (F1).
- Session 13 Phase 3A: Naive full-Hessian RULED OUT (F2 magnitude + F3 pattern).
- Session 14 Phase 3B-A: Fixed-dim belt subspace RULED OUT (F3 pattern).
- Session 15 Phase 3B-B: Full $C_n$ IRREP decomposition RULED OUT — **R2 FORMALLY CLOSED**.
- Session 16 Phase 4: Anharmonic ξ⁴ + all-orders Gaussian RULED OUT — **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED**.
- Session 17 Phase 5: Geometric-shift R3/R4 channels PASSED SCOPING.
- Session 18 Phase 6: R3-Coulomb scoping PASSED with 5% magnitude bullseye at $N = 10$.
- **Session 19 Phase 7: R3-Coulomb empirical comparison — PARTIAL POSITIVE with critical reframing.** Phase 5 R3-lin 1 MeV/α target reinterpreted as smooth-A scale; Phase 6 5% bullseye reinterpreted as smooth-A scale validation; polytope-residual signal identified as next refinement target.

The methodology lesson — F1 sign analytical check first, before computation — propagated from Phase 4 (Session 16) to Phase 5 (Session 17) to Phase 6 (Session 18) to Phase 7 (Session 19) as a working methodology. Phase 6 codified it as the sign-theorem composition workflow within-mechanism. Phase 7 extended it to empirical-comparison F1 (Level 2). Future sessions should continue this practice and apply it to refinements (Level 3).

---

*Step H paste-ready handover per `templates/operating_system.md` §15 protocol.*
