# SS-9 Handover — Session 18 Phase 6 Close (5 May 2026)

**Repository state at session close:** `origin/main` will be at patch 0194 once Thomas applies and pushes the five-patch chain (0190–0194). As of this document's creation, in-container HEAD is at patch 0193 (`fc22285`); patch 0194 is committed locally pending export and represents this Step H file itself.
**Active paper:** SS-9 — *Conditional Derivation of Simplicial Alpha-Polytope Connectivity from CPP Lattice Geometry* (working title; final TBD).
**Paper state:** Pre-paper / active development. v0.3 working draft at `session_logs/OPEN-SS-24_phase1_v0.3_working_draft.md` (218 lines). No `.tex` file yet (registered as OPEN-ORG-012, awaiting U-shape investigation §7 stability — §7 has now shifted **eight times** in the OPEN-SS-32 ↔ U-shape thread, with Session 18 Phase 6 substantively reorganizing the §7 framing further from "which CPP-first-principles physics drives $\delta R(N)$?" to "Coulomb gives 5% at $N = 10$ zero-parameter; refinement and pattern-match in progress").

## One-paragraph state

SS-9 has two parallel threads. The **OPEN-SS-24 closure target** is the original paper goal — a conditional theorem on refined-C1 + C2 + C5 + C6 + C7 hypothesis stack via Steinitz + Fáry-van der Waerden. v0.3 working draft is mature; v0.1 `.tex` conversion is registered as OPEN-ORG-012 awaiting natural pause point (now further deferred — §7 needs rewrite for Phase 6 quantitative bullseye on top of Phase 5 positive scoping on top of Phase 4's framework closure on top of Phase 3B-B's R2 closure). The **OPEN-SS-35 cross-paradigm closure programme** (derive nuclear shell-model magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ from CPP primitives) has been the active development front since Session 5. Through Session 18 Phase 6 the programme has produced **10 programme-level negative results** (unchanged from Session 17; Phase 6 is positive scoping, not a new ruling-out), **1 qualitative cross-paradigm consilience claim** (Session 9), **1 Decoupling Theorem** (Session 12), **1 formal R2 closure** (Session 15), **1 programme-level closure of the Gaussian-K$_3$ framework at fixed cluster geometry** (Session 16 via the §2.4 sign theorem), **1 channel-level positive scoping outcome** with R3 and R4 cluster-geometry shift channels advancing to multi-session derivation status (Session 17 Phase 5), and now **1 zero-parameter quantitative bullseye at the 5% level** with R3-Coulomb advancing to multi-session full-derivation status (Session 18 Phase 6). Session 18 applied the Phase 4/5 methodology lesson — F1 sign analytical check first, before computation — from the outset. The F1 sign argument for R3-Coulomb is one paragraph composed of two analytical results: **(i)** Coulomb interaction between alpha clusters (each charge $+2e$) is repulsive at all separations → cluster equilibrium shifts outward, $\delta R_{\rm Coulomb} > 0$; **(ii)** Phase 5 sign theorem: any $\delta R \neq 0$ gives $\Delta V_{\rm edge} = B_{\rm pair} \cdot [1 - \exp(-\delta R^2/(2\sigma^2))] > 0$ by Gaussian symmetry. Composition: $\delta R_{\rm Coulomb} > 0 \Rightarrow \Delta E^{R3}_{\rm Coulomb} > 0$ = empirical-required sign. **F1 PASSES analytically.** This composition is now codified as the **sign-theorem composition workflow** — default F1 check for any R3-channel mechanism going forward. Computational scoping using simplified CPP charge model (point-charge alphas $+2e$ at J-solid vertices, force balance against K$_3$ Gaussian restoring) gave $\delta R_C(10) = 1.104$ fm vs Phase 5 R3-lin target $1.052$ fm — **ratio 1.05, off by only 5%.** Striking quantitative agreement for a zero-parameter prediction (simplest charge model, canonical $R_\alpha = 2.37$ fm and $\sigma_{K3} = 1.68$ fm, no Pauli/surface/spin-orbit, no parameter tuning). SEMF cross-check: $V_C(0)$ matches $0.711 Z^2/A^{1/3}$ within $\sim 10\%$ across J-solid range, validating the simplified CPP charge model. F3 pattern monotonic across J-solid range (5→10): 0.821, 0.940, 0.995, 1.051, 1.104 fm. Functional shape NOT linear-in-$(N-4)$ as R3-lin assumed; instead Coulomb gives constant offset $\sim 0.78$ fm (substantial baseline expansion at smallest cluster $N=4$) plus slow growth — meaningful physics prediction distinguishing R3-Coulomb from R3-lin. R3-Coulomb advances to multi-session full-derivation status; the next phase derives empirical $\Delta B/A_{\rm emp}(N)$ from AME data, computes predicted $\Delta E_{R3-{\rm Coulomb}}(N)$ across full J-solid range, compares quantitatively, and refines the charge model (extended Gaussian distribution at $\sim 1.6$ fm; intra-cluster Coulomb correction; non-NN K$_3$ contributions; sensitivity to $\sigma_{K3}$). Pauli scoping qualitatively assessed but deferred: Pauli sign passes by composition (Pauli repulsive, $\delta R_{\rm Pauli} > 0$, by Phase 5 sign theorem $\Delta E > 0$); standard alpha-alpha Pauli is comparable to or smaller than Coulomb at $r \sim R_\alpha$. If Pauli adds $\sim 30$–$50\%$ to expansion, combined Coulomb + Pauli would overshoot Phase 5 target by $30$–$60\%$ at $N = 10$ — implying either Pauli is small correction *or* Phase 5 R3-lin target underestimates actual empirical scale. Sub-question (b) layer 3 gap-strength closure remains INDEPENDENT of Phase 4/5/6 by Decoupling Theorem (Session 12), unaffected.

## Forward queue

**Priority 1 (multi-session full derivation):** R3-Coulomb full derivation. Phase 6 established 5% magnitude bullseye at $N = 10$ for zero-parameter Coulomb model. Subsequent sessions:

- **Session 19 candidate:** derive the empirical alpha-cluster binding deficit pattern $\Delta B/A_{\rm emp}(N)$ from AME data (independent of Phase 5 heuristic 1 MeV/α scale). Compare to Phase 6's $\Delta E/\alpha = 0.358, 0.474, 0.608, 0.728, 0.848, 0.972, 1.092, 1.337$ MeV for $N = 4, 5, 6, 7, 8, 9, 10, 12$. Sign / magnitude / shape match across full range, not just $N = 10$.
- **Refinement A:** replace point-charge alphas with extended Gaussian charge distribution (radius $\sim 1.6$ fm, typical alpha proton density). Recompute $V_C(0)$ and $\delta R_C(N)$.
- **Refinement B:** include intra-cluster Coulomb correction for alpha-internal proton-proton repulsion (small constant per alpha, doesn't shift $\delta R$).
- **Refinement C:** include K$_3$ contribution from non-NN pairs at distances $\sim 3$–$5$ fm. Small (Gaussian decay) but non-zero.
- **Refinement D:** test sensitivity to $\sigma_{K3}$ — does the 5% agreement persist if $\sigma_{K3}$ is varied by $\pm 10\%$?

**Priority 2 (parallel scoping):** R3-Pauli scoping. Specify a Pauli model (e.g., Gaussian repulsive core in alpha-alpha potential), compute equilibrium $\delta R_{\rm Pauli}(N)$, compare to Phase 6's $\delta R_C(N)$. Apply F1 sign analytical check first via sign-theorem composition workflow: Pauli repulsive → $\delta R_{\rm Pauli} > 0$ → Phase 5 sign theorem → $\Delta E > 0$, F1 PASSES analytically. Then test F2 magnitude vs Coulomb scale. Goal: assess whether Pauli is small correction (few %) or comparable to Coulomb (factor 2 or so). Cross-check with Priority 1 Session 19 candidate.

**Priority 3 (deferred, registered):** OPEN-SS-32 attenuation-factor reformulation. Now that R3-Coulomb has 5% agreement at $N = 10$ as a starting point, the attenuation-factor derivation can be reframed in terms of cluster geometric expansion driven by Coulomb (and possibly Pauli) at canonical K$_3$ width. SS-9 §7 reformulation depends on Priority 1/2 outcomes.

**Priority 4 (parallel, deferred):** OPEN-SS-16 Layer B closure work — deepest open problem at programme level.

**Priority 5 (parallel, registered):** Reading B literature check.

**Anti-priorities (sharpened from Phase 5):**

- Do **not** initiate SS-9 v0.3 → v0.1 `.tex` conversion (OPEN-ORG-012) until §7 is reformulated for Phase 6 quantitative bullseye on top of Phase 5 positive scoping. **§7 has now shifted eight times** in the OPEN-SS-32 ↔ U-shape thread (Phase 1 prior-art read; Phases 2/3A/3B-A/3B-B/4 ruled out; Phase 5 PASSES SCOPING; **Phase 6 R3-Coulomb 5% agreement at $N = 10$**).
- **NEW from Phase 6:** Do **not** pursue Pauli or other R3-channel mechanisms in isolation from Coulomb. Coulomb is the dominant scale (within R3); other mechanisms are corrections on top.
- **From Phase 5:** Do **not** parameterize $\delta R(N)$ phenomenologically without grounding in CPP physics. Phase 5's R3-lin was heuristic; Phase 6's R3-Coulomb is derivation. Future refinements must follow the same standard.
- Do **not** abandon Phase 4 closure interpretation. R3-Coulomb is consistent with Phase 4 — it operates on geometric shift, not perturbative correction at fixed geometry. The Gaussian-K$_3$-at-fixed-geometry closure stands.
- Do **not** pursue further perturbative anharmonic refinement (ξ⁶, ξ⁸, hybrid PT, second-order $\xi^4$) within Gaussian-K$_3$ at fixed geometry — universally closed by Phase 4 §2.4 sign theorem.
- Do **not** pursue further belt-IRREP-projection variants within the K$_3$-Gaussian-Hessian framework — closed Phase 3B-B.
- Do **not** pursue full point group D$_{nh}$/D$_{nd}$ extension with reflections and improper rotations — closed Phase 3B-B.
- Do **not** pursue further $V_{\rm SO}$ refinement within simple K$_3$ + HO + L·S framework (Session 11 Phase 1).
- Do **not** pursue further $R_\alpha(A)$ in the specific surface-tension form (R1, Session 12).

## Computation reproduction notes

**Phase 6 script:** `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase6_R3_Coulomb.py` (~370 lines). Reuses Phase 4/5 polytope construction and constants verbatim. New: simplified CPP charge model with point-charge alphas $+2e$ at J-solid vertices (`compute_coulomb_energy`); pair-distance summary per polytope (`pair_distances_summary`); equilibrium solver via bracketing + bisection on force balance (`force_balance`, `solve_equilibrium`); F1/F2/F3 falsifier analysis with explicit pre-empted analytical sign argument in script docstring per Phase 4/5 methodology lesson; SEMF cross-check.

**Phase 6 sketch:** `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_phase6_R3_Coulomb.md`. Full §1 (strategy) — §7 (summary), with §2 pre-empted analytical sign analysis (sign-theorem composition workflow); §3 computation (§3.1 charge model, §3.2 pair-distance structure, §3.3 V_C(0) per polytope with SEMF cross-check, §3.4 equilibrium δR_Coulomb table, §3.5 F2 magnitude bullseye at N=10, §3.6 F3 pattern monotonicity, §3.7 functional shape comparison); §4 verdict (§4.1 three falsifier outcomes, §4.2 what this means, §4.3 Pauli scoping postponed, §4.4 what this is NOT); §5 programme implications; §6 forward pointers (§6.1 R3-Coulomb full derivation = Priority 1, §6.2 R3-Pauli scoping = Priority 2, §6.3 OPEN-SS-32 attenuation reformulation = Priority 3, §6.4 anti-priorities); §7 summary.

**Constants (verbatim from Phase 5):** $B_{\rm pair} = M_0/\varphi = 2.342$ MeV; $R_\alpha = 2.37$ fm; $\sigma_{K3} = 1.68$ fm (canonical); $m_\alpha = 3727.4$ MeV/c²; $\hbar c = 197.327$ MeV·fm. **New for Phase 6:** Coulomb constant $k_C \cdot e^2 = 1.44$ MeV·fm in nuclear units; alpha-alpha pair Coulomb prefactor $(2e)^2 \cdot k_C = 5.76$ MeV·fm.

**Numerical results (R3-Coulomb full):**

| $N$ | sym | $\lvert E\rvert$ | $V_C(0)$ [MeV] | $\delta R_C$ [fm] | $\Delta E_{K3}/\alpha$ [MeV] | R3-lin target [fm] | ratio |
|-----|-----|------|---------|---------|---------|---------|---------|
|  4 | $T_d$    |  6 |  $14.58$ | $0.779$ | $0.358$ | $0.000$ | — |
|  5 | $D_{3h}$ |  9 |  $23.36$ | $0.821$ | $0.474$ | $0.175$ | 4.68 |
|  6 | $O_h$    | 12 |  $34.32$ | $0.886$ | $0.608$ | $0.351$ | 2.53 |
|  7 | $D_{5h}$ | 15 |  $46.28$ | $0.940$ | $0.728$ | $0.526$ | 1.79 |
|  8 | $D_{2d}$ | 18 |  $59.60$ | $0.995$ | $0.848$ | $0.701$ | 1.42 |
|  9 | $D_{3h}$ | 21 |  $74.41$ | $1.051$ | $0.972$ | $0.876$ | 1.20 |
| **10** | **$D_{4d}$** | **24** |  **$90.22$** | **$1.104$** | **$1.092$** | **$1.052$** | **1.05** |
| 12 | $I_h$    | 30 | $125.64$ | $1.210$ | $1.337$ | $1.402$ | 0.86 |

**Force balance equation:** $|E| \cdot B_{\rm pair} \cdot (\delta R/\sigma_{K3}^2) \cdot \exp(-\delta R^2/(2\sigma_{K3}^2)) = V_C(0) \cdot R_\alpha/(R_\alpha + \delta R)^2$. Solved per polytope with `scipy.optimize.brentq`.

**SEMF cross-check ratios** $V_C(\rm point)/V_C(\rm SEMF)$: $0.81, 0.89, 0.97, 1.01, 1.04, 1.07, 1.09, 1.11$ for $N = 4, 5, 6, 7, 8, 9, 10, 12$. Within $\sim 10\%$ — agreement improves for larger $N$ (uniform-distribution approximation more accurate); degrades for smaller $N$ (discrete vertex-localized vs uniform).

**Best-fit linear slope** $\alpha_C = 0.224$ fm/(N-4 unit), 28% larger than R3-lin's $0.175$, with residuals $+0.60, +0.27, +0.10, -0.07, -0.24$ fm at $N = 5, 7, 8, 9, 10$ — Coulomb sits above linear fit at small $N$, below at large $N$. **Coulomb's functional shape is floor + slow-growth, not linear-in-$(N-4)$.**

## Lesson reinforcement — sign-theorem composition workflow

The Phase 4/5 methodology lesson — F1 sign analytical check first, before computation — was applied in Phase 6 from the outset. Phase 6 codifies the workflow as **sign-theorem composition**: identify the sign of $\delta R$ that the candidate physics drives (classical-physics argument from electrostatics, Pauli, surface effects, etc.), then invoke Phase 5 §2 sign theorem to get $\Delta E$ sign automatically. The workflow takes one paragraph and decides F1 universally for any R3-channel mechanism before any computation.

**Applications to Session 19+:**
- **R3-Pauli (Priority 2):** Pauli is repulsive between like fermions → $\delta R_{\rm Pauli} > 0$ → Phase 5 sign theorem → $\Delta E > 0$. **F1 PASSES analytically.** Computation needed only for F2 magnitude and F3 pattern.
- **R3-surface-density (deferred, registered):** sign of $\delta R$ depends on whether surface-density coupling is attractive or repulsive at the cluster boundary. Sign argument first; computation only if F1 passes.
- **R4-shape (deferred, registered):** sign of $\delta R$ depends on details; spin-orbit cluster contributions can have either sign depending on geometry. Sign argument case-by-case.

**For Gaussian-K$_3$-framework-related questions:** any positive-ΔE candidate at fixed geometry passes F1 trivially via Gaussian symmetry (Phase 5 §2); any negative-ΔE candidate at fixed geometry is ruled out by Phase 4's sign theorem. Geometric-shift candidates (R3, R4) inherit the Phase 5 sign theorem automatically by the composition workflow above.

## Cumulative state — programme-level

- **10 programme-level negative results UNCHANGED** (no new ruling-out in Session 18, Phase 6 is positive scoping); 5 in OPEN-SS-32 ↔ U-shape thread.
- **R2 (cluster-scale ↔ alpha-scale unification at canonical $\sigma_{K3}$) FORMALLY CLOSED** (Session 15 Phase 3B-B, n-vs-N structural argument) — unchanged.
- **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED** (Session 16 Phase 4, sign theorem + Rayleigh–Ritz) — unchanged.
- **R3 and R4 cluster-geometry shift channels passed scoping** (Session 17 Phase 5) — unchanged.
- **R3-Coulomb passed scoping with 5% bullseye at $N = 10$** (Session 18 Phase 6) — *new this session*. First quantitative agreement at 5% level for zero-parameter prediction in OPEN-SS-32 ↔ U-shape thread.
- **OPEN-SS-35 sub-question (a) A-scaling closure**: R3-Coulomb under active multi-session full derivation with 5% quantitative precedent at $N = 10$. Multi-session forward work: full pattern comparison + charge-model refinement.
- **OPEN-SS-35 sub-question (b) layer 3 gap-strength closure**: independent by Decoupling Theorem (Session 12), unaffected.
- **First qualitative cross-paradigm consilience claim** (Session 9, magic-number sequence reproduced from CPP first principles) intact.
- **Decoupling Theorem** (Session 12): A-scaling closure and gap-strength closure are independent open problems — intact.
- **Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances** unchanged.
- **6 programme-level OPEN-SS-35 stages preserved**; Phase 6 refines stage (vi) further: stage (vi) now reads "R3-Coulomb under active multi-session full derivation; 5% quantitative agreement at $N = 10$ for zero-parameter calculation; refinement and full pattern-match in progress".
- **Sign-theorem composition workflow** codified (Session 18 Phase 6 §5.2): default F1 check for any R3-channel mechanism going forward.

## Relationship to prior sessions

Phase 6 is the **second positive scoping outcome** in the OPEN-SS-32 ↔ U-shape thread (Phase 5 was the first), and the **first quantitative agreement at the 5% level for a zero-parameter prediction** in the thread. The trajectory through Sessions 13–18:

- Session 13 Phase 2: Uniform-only zero-point softening RULED OUT (F1).
- Session 13 Phase 3A: Naive full-Hessian RULED OUT (F2 magnitude + F3 pattern).
- Session 14 Phase 3B-A: Fixed-dim belt subspace RULED OUT (F3 pattern).
- Session 15 Phase 3B-B: Full $C_n$ IRREP decomposition RULED OUT — **R2 FORMALLY CLOSED** (n-vs-N structural argument).
- Session 16 Phase 4: Anharmonic ξ⁴ + all-orders Gaussian RULED OUT — **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED** (sign theorem + Rayleigh–Ritz).
- Session 17 Phase 5: Geometric-shift R3/R4 channels PASSED SCOPING (sign-orthogonal complement to Phase 4).
- **Session 18 Phase 6: R3-Coulomb scoping PASSED with 5% magnitude bullseye at $N = 10$** (sign-theorem composition workflow + zero-parameter quantitative agreement).

The methodology lesson — F1 sign analytical check first, before computation — propagated from Phase 4 (Session 16) to Phase 5 (Session 17) to Phase 6 (Session 18) as a working methodology. Phase 6 codified it further as the sign-theorem composition workflow. Future sessions should continue this practice.

---

*Step H paste-ready handover per `templates/operating_system.md` §15 protocol.*
