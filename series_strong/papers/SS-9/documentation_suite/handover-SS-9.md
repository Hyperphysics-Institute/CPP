# SS-9 Handover — Session 17 Phase 5 Close (5 May 2026)

**Repository state at session close:** `origin/main` will be at patch 0189 once Thomas applies and pushes the five-patch chain (0185–0189). As of this document's creation, in-container HEAD is at patch 0188 (`6ee1c41`); patch 0189 is committed locally pending export and represents this Step H file itself.
**Active paper:** SS-9 — *Conditional Derivation of Simplicial Alpha-Polytope Connectivity from CPP Lattice Geometry* (working title; final TBD).
**Paper state:** Pre-paper / active development. v0.3 working draft at `session_logs/OPEN-SS-24_phase1_v0.3_working_draft.md` (218 lines). No `.tex` file yet (registered as OPEN-ORG-012, awaiting U-shape investigation §7 stability — §7 has now shifted **seven times** in the OPEN-SS-32 ↔ U-shape thread, with Session 17 Phase 5 substantively reorganizing the §7 framing from "what mechanism within K$_3$-Gaussian-Hessian framework explains U-shape?" to "which CPP-first-principles V$_{\rm other}$ physics drives $\delta R(N)$?").

## One-paragraph state

SS-9 has two parallel threads. The **OPEN-SS-24 closure target** is the original paper goal — a conditional theorem on refined-C1 + C2 + C5 + C6 + C7 hypothesis stack via Steinitz + Fáry-van der Waerden. v0.3 working draft is mature; v0.1 `.tex` conversion is registered as OPEN-ORG-012 awaiting natural pause point (now further deferred — §7 needs rewrite for Phase 5 positive scoping result on top of Phase 4's framework closure on top of Phase 3B-B's R2 closure). The **OPEN-SS-35 cross-paradigm closure programme** (derive nuclear shell-model magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ from CPP primitives) has been the active development front since Session 5. Through Session 17 Phase 5 the programme has produced **10 programme-level negative results** (unchanged from Session 16; Phase 5 is positive scoping, not a new ruling-out), **1 qualitative cross-paradigm consilience claim** (Session 9), **1 Decoupling Theorem** (Session 12), **1 formal R2 closure** (Session 15), **1 programme-level closure of the Gaussian-K$_3$ framework at fixed cluster geometry** (Session 16 via the §2.4 sign theorem), and now **1 positive scoping outcome with R3 and R4 cluster-geometry shift channels advancing to multi-session derivation status** (Session 17). Session 17 applied the Phase 4 methodology lesson — F1 sign analytical check first, before computation — from the outset. The F1 sign argument for both R3 (uniform $R_\alpha(N)$ shift) and R4 (cluster shape distortion) is one paragraph from Gaussian symmetry: the K$_3$ pair potential $V_{\rm pair}(\delta r) = -B_{\rm pair} \exp(-\delta r^2/(2\sigma^2))$ is symmetric in $\delta r$ around equilibrium; for any displacement $\delta r \neq 0$ the per-edge K$_3$ binding loss $\Delta V_{\rm edge} = B_{\rm pair} \cdot [1 - \exp(-\delta r^2/(2\sigma^2))]$ is strictly positive regardless of the sign of $\delta r$. **F1 PASSES universally for both R3 and R4 by Gaussian symmetry alone.** Computational scoping established F2 magnitude capacity ($5.62$ MeV/α maximum at $N = 10$, well above empirical $\sim 1$ MeV/α scale) and F3 pattern monotonicity (passes for any monotonic $\delta R(N)$ or constant $\epsilon_{\rm rms}$). **First non-rule-out outcome in five sequential phases of OPEN-SS-32 ↔ U-shape investigation.** The decisive structural observation is **sign-orthogonal contrast with Phase 4**: Phase 4's anharmonic ξ⁴ correction had $\Delta E < 0$ universally by Wick + negative Taylor coefficient; Phase 5's geometric shift has $\Delta E > 0$ universally by Gaussian symmetry. Same Gaussian function generates both signs in different framings — closure of one motivates opening of the other; effectively partitions OPEN-SS-32 candidate space by sign of predicted ΔE. R3-lin calibration: $\alpha = 0.175$ fm/(N-4 unit), $\delta R(N=10) = 1.05$ fm = $44.4\%$ of $R_{\rm canon}$ as natural target $\delta R$ scale for first-principles derivation. Phase 5 does NOT claim to derive the U-shape mechanism, only that R3/R4 are channel-compatible (sign + magnitude capacity + pattern). R3 and R4 advance to multi-session derivation status; the next phase identifies $\delta R(N)$ from CPP first principles (Coulomb cluster repulsion, Pauli internal blocking, surface-density alternatives, spin-orbit cluster contributions). Sub-question (b) layer 3 gap-strength closure remains INDEPENDENT of Phase 4/5 by Decoupling Theorem (Session 12), unaffected.

## Forward queue

**Priority 1 (multi-session derivation):** Identify $\delta R(N)$ functional form from CPP first principles. Phase 5 established the R3/R4 channels pass scoping at F1/F2/F3 levels and provided the R3-lin calibration $\delta R(N=10) \approx 1$ fm as target. Candidate physics, each requiring multi-session derivation:

- **(R3-Coulomb)** Cluster Coulomb repulsion: $V_C \sim Z^2/A^{1/3}$ pushes $R_\alpha$ outward. CPP-derivable from charge structure of alpha clusters on the 600-cell lattice. Predicts $\delta R(N)$ pattern via dependence on $Z(N) = 2N$ and overall cluster geometry.
- **(R3-Pauli)** Pauli blocking at internal alpha-alpha contacts: scales with edge count, monotonic in $N$. CPP-derivable from Pauli operator on alpha-cluster wavefunctions.
- **(R3-surface)** Alternative surface-density forms — NOT R1's surface-tension form (ruled out Session 12); other surface-coupling mechanisms remain.
- **(R4-shape)** Spin-orbit cluster contributions with shape dependence; or other anisotropic mechanisms driving non-uniform edge distortion.

**Natural Session 18 first move: R3-Coulomb scoping.** Compute the Coulomb-driven equilibrium $\delta R(N)$ using a simplified CPP charge model (alpha clusters at J-solid vertices, charge $+2e$ each, electromagnetic geometry from 600-cell lattice). Compare to Phase 5 R3-lin calibration ($\delta R(10) \approx 1$ fm = $44.4\%$ of $R_{\rm canon}$). Apply F1 sign analytical check first (Phase 4/5 lesson) — Coulomb is repulsive, pushes $R_\alpha$ outward, so $\delta R > 0$ → $\Delta E_{R3-Coulomb} > 0$ by Gaussian symmetry, F1 PASSES. Then compute magnitude and pattern. Falsifier: if Coulomb-driven $\delta R(N)$ comes out wrong magnitude (much smaller or larger than R3-lin target) or wrong functional form (e.g., wrong N-dependence), R3-Coulomb is ruled out and we proceed to R3-Pauli. If Coulomb gives roughly the right scale, this is positive scoping at the next level and motivates a full first-principles CPP-physics derivation.

**Priority 2 (parallel, deferred):** Inelastic / out-of-framework channels (Phase 4 sketch §6.2). Hoyle-state mixing, surface-energy shape dependence, Coulomb cluster-arrangement effects. Less natural Priority 1 than R3-physics-derivation because R3/R4 has known sign/magnitude/pattern compatibility from Phase 5.

**Priority 3 (deferred):** OPEN-SS-32 attenuation-factor derivation reformulation — depends on Priority 1 success.

**Priority 4 (parallel, deferred):** OPEN-SS-16 Layer B closure work — deepest open problem at programme level.

**Priority 5 (parallel, registered):** Reading B literature check.

**Anti-priorities (sharpened from Phase 4):**

- Do **not** initiate SS-9 v0.3 → v0.1 `.tex` conversion (OPEN-ORG-012) until §7 is reformulated for Phase 5 positive scoping result. **§7 has now shifted seven times** in the OPEN-SS-32 ↔ U-shape thread (Phase 1 prior-art read; Phase 2 ruled out; Phase 3A ruled out + bracketing; Phase 3B-A ruled out + pattern-shape constraint; Phase 3B-B ruled out + R2 formal closure; Phase 4 ruled out + Gaussian-K$_3$ framework closure via sign theorem; **Phase 5 PASSES SCOPING + R3/R4 channels open + multi-session derivation pending**).
- **NEW from Phase 5:** Do **not** parameterize $\delta R(N)$ phenomenologically without grounding in CPP physics. Phase 5's R3-lin calibration is a target for first-principles derivation, not a model to be fit. Any future R3-related work should derive $\delta R(N)$ from a specified physical mechanism (Coulomb, Pauli, surface-density, spin-orbit) and compare to the Phase 5 calibration as falsifier.
- Do **not** pursue further perturbative anharmonic refinement (ξ⁶, ξ⁸, hybrid PT, second-order $\xi^4$) within Gaussian-K$_3$ at fixed geometry — universally closed by Phase 4 §2.4 sign theorem.
- Do **not** pursue further belt-IRREP-projection variants within the K$_3$-Gaussian-Hessian framework — closed Phase 3B-B.
- Do **not** pursue full point group D$_{nh}$/D$_{nd}$ extension with reflections and improper rotations — closed Phase 3B-B.
- Do **not** pursue energy-weighted IRREP filtering or higher-$m$ harmonics within K$_3$-Gaussian-Hessian framework — closed Phase 3B-B.
- Do **not** pursue further $V_{\rm SO}$ refinement within simple K$_3$ Gaussian-modulated mean field + HO + L·S framework (Session 11 Phase 1 ruled this out).
- Do **not** pursue further $R_\alpha(A)$ in the specific surface-tension form (R1, Session 12) — though *new* geometric-shift forms R3/R4 are different and remain Priority 1.

## Computation reproduction notes

**Phase 5 script:** `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase5_geometric_shift_R3_R4.py` (~390 lines). Reuses Phase 4's polytope construction and edge construction verbatim. New: R3 uniform-shift energy computation (`r3_per_edge_shift`, `r3_cluster_shift`), R4 Gaussian-rms-distortion energy computation (`r4_per_edge_average_shift`, `r4_cluster_average_shift`), three R3 parameterizations (R3-emp using Session 12 R_pct values, R3-lin calibrated to 1 MeV/α at N=10, R3-edge), two R4 parameterizations (R4-flat constant ε_rms, R4-Nlin linear-in-N ε_rms). Analytical F1 sign argument is pre-empted in script docstring per Phase 4 methodology lesson.

**Phase 5 sketch:** `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_phase5_geometric_shift_R3_R4.md`. Full §1 (strategy) — §7 (summary), with §2 analytical sign argument including §2.1 sign-orthogonal contrast with Phase 4; §3 computational scoping (§3.1 R3-emp, §3.2 R3 magnitude capacity, §3.3 R3-lin, §3.4 R4-flat, §3.5 R4-Nlin, §3.6 F3 pattern); §4 verdict (§4.1 three falsifier outcomes, §4.2 first non-rule-out in 5 phases, §4.3 what passes scoping means and does not); §5 programme implications; §6 forward pointers (§6.1 R3 first-principles derivation = Priority 1, §6.2 inelastic/out-of-framework = Priority 2, §6.3 anti-priorities); §7 summary.

**Constants (verbatim from Phase 4):** $B_{\rm pair} = M_0/\varphi = 2.342$ MeV; $R_\alpha = 2.37$ fm; $\sigma_{K3} = 1.68$ fm (canonical); $m_\alpha = 3727.4$ MeV/c²; $\hbar c = 197.327$ MeV·fm.

**Numerical results (R3-emp, J-solid range):**

| $N$ | sym | $\lvert E\rvert$ | $R_{\rm pct}$ % | $\delta R$ [fm] | $\Delta E_{R3}$ [MeV] | $\Delta E/\alpha$ [MeV] |
|-----|-----|------|------|--------|-------|---------|
|  5 | $D_{3h}$ |  9 | $+14.60$ | $+0.346$ | $0.442$ | $0.088$ |
|  7 | $D_{5h}$ | 15 | $+19.10$ | $+0.453$ | $1.253$ | $0.179$ |
|  8 | $D_{2d}$ | 18 | $+21.10$ | $+0.500$ | $1.827$ | $0.228$ |
|  9 | $D_{3h}$ | 21 | $+22.30$ | $+0.529$ | $2.375$ | $0.264$ |
| 10 | $D_{4d}$ | 24 | $+22.70$ | $+0.538$ | $2.810$ | $0.281$ |

**R3-lin calibration:** $\alpha = 0.1753$ fm/(N-4 unit), $\delta R(N=10) = 1.052$ fm = $44.4\%$ of $R_{\rm canon}$ for $\Delta E/\alpha = 1$ MeV at $N = 10$.

**R4-flat results:** ε_rms = $0.10 \cdot R_{\rm canon} = 0.237$ fm; per-edge $\langle \Delta V \rangle = 0.0230$ MeV (0.98% of $B_{\rm pair}$); cluster total grows linearly with $|E|$.

## Lesson reinforcement

The Phase 4 methodology lesson — **F1 sign analytical check first, before computation** — was applied in Phase 5 from the outset and worked exactly as intended. The analytical sign argument took one paragraph from Gaussian symmetry and decided F1 universally for both R3 and R4 before any code was written. Computational scoping was reserved for F2 magnitude capacity and F3 pattern monotonicity.

For Gaussian-K$_3$-framework-related questions specifically: any positive-ΔE candidate passes F1 trivially via Gaussian symmetry; any negative-ΔE candidate is ruled out by Phase 4's sign theorem. **The Gaussian function's symmetry has effectively partitioned the OPEN-SS-32 candidate space by sign of predicted ΔE**, with Phase 4 closing the negative-ΔE side and Phase 5 opening the positive-ΔE side. Future scoping investigations in this thread can apply the sign argument as F1 to immediately decide which side of the partition any candidate mechanism falls on, before any computation.

## Cumulative state — programme-level

- **10 programme-level negative results UNCHANGED** (no new ruling-out in Session 17, Phase 5 is positive scoping); 5 in OPEN-SS-32 ↔ U-shape thread.
- **R2 (cluster-scale ↔ alpha-scale unification at canonical $\sigma_{K3}$) FORMALLY CLOSED** (Session 15 Phase 3B-B, n-vs-N structural argument) — unchanged.
- **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED** (Session 16 Phase 4, sign theorem + Rayleigh–Ritz) — unchanged.
- **R3 and R4 cluster-geometry shift channels under active scoping** (Session 17 Phase 5, positive F1/F2/F3 result; multi-session $\delta R(N)$ derivation pending) — *new this session*.
- **OPEN-SS-35 sub-question (a) A-scaling closure**: Phase 5 R3 and R4 channels under active scoping investigation; first time since Session 12's R1 closure that the sub-question has a non-ruled-out candidate.
- **OPEN-SS-35 sub-question (b) layer 3 gap-strength closure**: independent by Decoupling Theorem (Session 12), unaffected.
- **First qualitative cross-paradigm consilience claim** (Session 9, magic-number sequence reproduced from CPP first principles) intact.
- **Decoupling Theorem** (Session 12): A-scaling closure and gap-strength closure are independent open problems — intact.
- **Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances** unchanged.
- **6 programme-level OPEN-SS-35 stages preserved**; Phase 5 refines stage (vi) further: stage (vi) now reads "R3/R4 cluster-geometry shift channels under active scoping with positive F1/F2/F3 result; multi-session $\delta R(N)$ derivation from CPP physics in progress".

## Relationship to prior sessions

Phase 5 is the **first non-rule-out outcome** in the OPEN-SS-32 ↔ U-shape thread, following five sequential closures: Phase 2 (Session 13), Phase 3A (Session 13), Phase 3B-A (Session 14), Phase 3B-B (Session 15, R2 formal closure), Phase 4 (Session 16, Gaussian-K$_3$ framework formal closure). Phase 4's closure of negative-ΔE perturbative corrections and Phase 5's opening of positive-ΔE geometric shifts are sign-orthogonal — same Gaussian function, opposite sign by symmetry. Together they have effectively partitioned the OPEN-SS-32 candidate space, leaving R3/R4 (and out-of-framework channels) as the natural next investigation targets.

The lesson-learned about F1 sign analytical check as default propagated from Phase 4 to Phase 5 as a working methodology. Future scoping investigations should continue this practice.

---

*Step H paste-ready handover per `templates/operating_system.md` §15 protocol.*
