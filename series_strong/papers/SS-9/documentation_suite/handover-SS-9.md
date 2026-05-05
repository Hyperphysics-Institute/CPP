# SS-9 Handover — Session 16 Phase 4 Close (5 May 2026)

**Repository state at session close:** `origin/main` will be at patch 0184 once Thomas applies and pushes the five-patch chain (0180–0184). As of this document's creation, in-container HEAD is at patch 0183 (`78f3d99`); patch 0184 is committed locally pending export and represents this Step H file itself.
**Active paper:** SS-9 — *Conditional Derivation of Simplicial Alpha-Polytope Connectivity from CPP Lattice Geometry* (working title; final TBD).
**Paper state:** Pre-paper / active development. v0.3 working draft at `session_logs/OPEN-SS-24_phase1_v0.3_working_draft.md` (218 lines; complete §1–§6 + Lemmas A/B$'$/C + Theorem with four clauses). No `.tex` file yet (registered as OPEN-ORG-012, awaiting U-shape investigation §7 stability — §7 has now shifted **six times** in the OPEN-SS-32 ↔ U-shape thread, with Session 16 Phase 4 requiring substantial §7 rewrite to reflect the Gaussian-K$_3$ framework programme-level closure layered on top of Phase 3B-B's R2 closure).

## One-paragraph state

SS-9 has two parallel threads. The **OPEN-SS-24 closure target** is the original paper goal — a conditional theorem on refined-C1 + C2 + C5 + C6 + C7 hypothesis stack via Steinitz + Fáry-van der Waerden. v0.3 working draft is mature; v0.1 `.tex` conversion is registered as OPEN-ORG-012 awaiting natural pause point (now further deferred — §7 needs rewrite for Gaussian-K$_3$ framework closure). The **OPEN-SS-35 cross-paradigm closure programme** (derive nuclear shell-model magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ from CPP primitives) has been the active development front since Session 5. Through Session 16 Phase 4 the programme has produced **10 programme-level negative results** (Routes D, B-γ, 1b, Path (i), R1, Phase 2 model (a), Phase 3A naive full-Hessian, Phase 3B-A fixed-dim belt-subspace, Phase 3B-B full C$_n$ IRREP decomposition, **Phase 4 anharmonic K$_3$ $\xi^4$ + all-orders Gaussian via sign theorem**), **1 qualitative cross-paradigm consilience claim** (Session 9), **1 Decoupling Theorem** (Session 12), **1 formal R2 closure** (Session 15), and now **1 programme-level closure of the Gaussian-K$_3$ framework at fixed cluster geometry** (Session 16 via the §2.4 sign theorem). Session 16 ruled out anharmonic K$_3$ corrections at order $\xi^4$ in the Gaussian expansion as the U-shape mechanism on a third falsifier (sign) that the original Session 15 scoping plan did not anticipate; the closure was strengthened from "first-order $\xi^4$ ruled out" to "**all-orders Gaussian-K$_3$ perturbative correction at fixed geometry rigorously ruled out by Rayleigh–Ritz variational argument**". The **sign theorem** (Phase 4 sketch §2.4): $f(s) \equiv (1+s)^{-1/2} - 1 + s/2$ satisfies $f(0) = 0$ and $f'(s) = (1/2)[1 - (1+s)^{-3/2}] > 0$ for $s > 0$, hence $f(s) > 0$ for $s > 0$, hence $\Delta E_{\rm anharm}^{\rm all\text{-}orders} = -B_{\rm pair} f(s) < 0$ universally. By Rayleigh–Ritz the true cluster ground state energy in the full Gaussian Hamiltonian is provably *more* bound than the harmonic estimate, never less. Empirical U-shape requires the opposite. **The U-shape mechanism cannot live within the Gaussian-K$_3$ framework at fixed cluster geometry — provably.** Phase 3B-B (Session 15) closed harmonic-Hessian-belt-IRREP family at canonical $\sigma$; Phase 4 (this session) closes perturbative-correction family at canonical geometry; together they exhaust the framework. The U-shape mechanism must be sought in geometric-shift channels beyond R1 (channels R3 = N-dependent boundary conditions on $R_\alpha$; R4 = cluster shape distortion) or out-of-framework (inelastic excitations including Hoyle-state mixing; surface-energy shape dependence; Coulomb cluster-arrangement effects). Sub-question (b) layer 3 gap-strength closure is INDEPENDENT of Phase 4 by Decoupling Theorem (Session 12), unaffected.

## Forward queue

**Priority 1 (substantive new investigation):** Cluster-geometry shift mechanisms beyond R1 — channels R3 (N-dependent boundary conditions on $R_\alpha$) and R4 (cluster shape distortion). With the Gaussian-K$_3$ framework at fixed canonical geometry now provably closed (Phase 3B-B + Phase 4), the next natural candidate channel is geometric-shift mechanisms not captured by R1. R1 (Session 12) tested the specific surface-tension-motivated $R_\alpha(A)$ form and ruled it out for sign + U-shape pattern + Decoupling Theorem grounds. R3 and R4 are different geometric-shift forms not yet tested. **R3 mechanism:** cluster compression or expansion driven by N-dependent boundary conditions; each J-solid has different "surface" (number of edges per vertex, boundary topology), and equilibrium $R_\alpha$ may shift accordingly; would manifest as $R_{\alpha,{\rm eff}}(N)$ values close to but not equal to 2.37 fm. **R4 mechanism:** cluster shape distortion beyond rigid J-solid assumption; the J-solid geometry minimizes pair-K$_3$ energy assuming uniform edge length, but with anisotropic perturbations the equilibrium shape may distort. Both R3 and R4 are single-session-tractable as scoping investigations: parameterize the geometric shift, compute resulting K$_3$ binding shift, compare sign / magnitude / pattern against empirical. Critical sign check: empirical wants $\Delta E > 0$ (cluster grows → less binding) in J-solid range; F1 (sign) is the dispositive falsifier per the Phase 4 lesson learned.

**Priority 2 (substantive new investigation):** Inelastic / out-of-framework channels — Hoyle-state mixing, surface-energy shape dependence, Coulomb cluster-arrangement effects (Phase 4 sketch §6.2). Each is multi-session by scope but single-session scoping feasible to identify which channel matches empirical sign/pattern. Hoyle-state $0^+_2$ mixing acts via spectral repulsion that *could* reduce effective binding (since Hoyle is below cluster ground state in some kinematic windows) — sign-compatible candidate. Surface-energy shape dependence (Strutinsky-like) varies with deformation and could produce monotonic-in-$N$ pattern across J-solids of different surface complexity. Coulomb cluster-arrangement effects: sensitivity to specific geometric arrangement not captured by edge count alone.

**Priority 3 (deferred):** OPEN-SS-32 attenuation-factor derivation reformulation — depends on Priority 1 / Priority 2 success.

**Priority 4 (parallel, deferred):** OPEN-SS-16 Layer B closure work — deepest open problem at programme level; multi-session by scope.

**Priority 5 (parallel, registered):** Reading B literature check — empirical $41/A^{1/3}$ A-range of validity (does it exclude $A = 16, 24$?). Independent of Priority 1.

**Anti-priorities (sharpened from Session 15):**

- Do **not** initiate SS-9 v0.3 → v0.1 `.tex` conversion (OPEN-ORG-012) until §7 is reformulated for the Gaussian-K$_3$ framework closure layered on top of R2 — §7 has now shifted **six times** in the OPEN-SS-32 ↔ U-shape thread (Phase 1 prior-art read; Phase 2 ruled out; Phase 3A ruled out + bracketing; Phase 3B-A ruled out + pattern-shape constraint; Phase 3B-B ruled out + R2 formal closure; **Phase 4 ruled out + Gaussian-K$_3$ framework closure via sign theorem**).
- Do **not** pursue further perturbative anharmonic refinement (ξ⁶, ξ⁸, hybrid PT, second-order $\xi^4$) within Gaussian-K$_3$ at fixed geometry — **universally closed by Phase 4 §2.4 sign theorem**. Any improvement of harmonic K$_3$ at fixed geometry within the Gaussian framework is *more*-binding-direction, never less; empirical U-shape needs less binding.
- Do **not** pursue further belt-IRREP-projection variants within the K$_3$-Gaussian-Hessian framework — n-vs-N structural argument rules out the entire class (Phase 3B-B closure).
- Do **not** pursue full point group D$_{nh}$/D$_{nd}$ extension with reflections and improper rotations — n-vs-N argument applies.
- Do **not** pursue energy-weighted IRREP filtering or higher-$m$ harmonics within K$_3$-Gaussian-Hessian framework — n-vs-N argument applies.
- Do **not** pursue further $V_{\rm SO}$ refinement within simple K$_3$ Gaussian-modulated mean field + HO + L·S framework (Session 11 Phase 1 ruled this out).
- Do **not** pursue further $R_\alpha(A)$ in the specific surface-tension form (R1, Session 12) — though *new* geometric-shift forms R3/R4 are different and remain Priority 1.

## Computation reproduction notes

**Phase 4 script:** `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase4_anharmonic_K3_xi4.py` (370 lines). Reuses Phase 3B-B's polytope construction, edge construction, and Hessian build verbatim. New: per-edge harmonic-Hessian variance accumulation (per_edge_msd), first-order anharmonic energy correction with Wick contraction, all-orders Gaussian-average extension, F1/F2/F3 falsifier output, eight-row verification table.

**Phase 4 sketch:** `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_phase4_anharmonic_K3_xi4.md`. Full §1 (strategy) — §7 (summary), with §2.4 sign theorem proof. The proof is one paragraph and should be incorporated into any future SS-9 §7 reformulation as the formal closure tool for Gaussian-K$_3$ framework refinements.

**Constants (verbatim from Phase 3B-B):** $B_{\rm pair} = M_0/\varphi = 2.342$ MeV; $R_\alpha = 2.37$ fm; $\sigma_{K3} = 1.68$ fm (canonical); $m_\alpha = 3727.4$ MeV/c²; $\hbar c = 197.327$ MeV·fm. Per-edge spring $k_{\rm edge} = B_{\rm pair}/\sigma^2 = 0.830$ MeV/fm². Anharmonic prefactor $3 B_{\rm pair}/(8 \sigma^4) = 0.1103$ MeV/fm⁴.

**Numerical results (first-order $\xi^4$, J-solid range $N = 5$–$10$):**

| $N$ | sym | $\langle s \rangle$ | $\Delta E^{(1)}$ [MeV] | $\Delta E^{(1)}/\alpha$ [MeV] | $\Delta E^{(1)}/B_{K3}$ % | $-d_{\rm emp}$ % |
|-----|-----|---------------------|------------------------|------------------------------|---------------------------|------------------|
| 5  | $D_{3h}$ | 0.853 |  $-5.75$  | $-1.15$ | $-27.28$ | $-23.86$ |
| 7  | $D_{5h}$ | 0.848 |  $-9.48$  | $-1.35$ | $-26.97$ | $-29.50$ |
| 8  | $D_{2d}$ | 0.851 | $-11.44$  | $-1.43$ | $-27.13$ | $-31.81$ |
| 9  | $D_{3h}$ | 0.849 | $-13.31$  | $-1.48$ | $-27.05$ | $-33.14$ |
| 10 | $D_{4d}$ | 0.847 | $-15.14$  | $-1.51$ | $-26.92$ | $-33.58$ |

All-orders Gaussian average reduces magnitude by factor $\sim 0.59$ (polytope-independent because $\langle s \rangle$ near-constant) but preserves negative sign. Sign theorem proves the sign preservation rigorously for all $s > 0$.

## Lesson for future scoping investigations

The Phase 4 result carried a methodology lesson worth registering. The Session 15 forward pointer specified two falsifiers (magnitude, pattern) but did not include the analytical sign check. The sign argument is one paragraph and immediately decisive — but it was not pre-empted before scoping computational work. Future scoping investigations should always include the analytical sign check as F1 alongside magnitude (F2) and pattern (F3). For the K$_3$ Gaussian framework the relevant sign check involves: which way do the relevant Taylor coefficients go, and what does Wick's theorem do to expectation values in the harmonic ground state?

## Cumulative state — programme-level

- **10 programme-level negative results** (was 9 at Session 15 close); 5 in OPEN-SS-32 ↔ U-shape thread.
- **R2 (cluster-scale ↔ alpha-scale unification at canonical $\sigma_{K3}$) FORMALLY CLOSED** (Session 15 Phase 3B-B, n-vs-N structural argument) — unchanged.
- **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED** (Session 16 Phase 4, sign theorem + Rayleigh–Ritz) — *new this session*.
- **OPEN-SS-35 sub-question (a) A-scaling closure**: both registered candidates (R1, R2) ruled out; entire Gaussian-K$_3$ framework at fixed geometry now provably empty of viable closures. Mechanism must be R3/R4 geometric-shift or out-of-framework.
- **OPEN-SS-35 sub-question (b) layer 3 gap-strength closure**: independent by Decoupling Theorem (Session 12), unaffected.
- **First qualitative cross-paradigm consilience claim** (Session 9, magic-number sequence reproduced from CPP first principles) intact.
- **Decoupling Theorem** (Session 12): A-scaling closure and gap-strength closure are independent open problems — intact.
- **Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances** unchanged.
- **6 programme-level OPEN-SS-35 stages preserved**; Phase 4 refines stage (vi) further with rigorous Gaussian-K$_3$ framework closure.

## Relationship to prior sessions

Phase 4 is the **fifth sequential closure** in the OPEN-SS-32 ↔ U-shape thread, following Phase 2 (Session 13), Phase 3A (Session 13), Phase 3B-A (Session 14), Phase 3B-B (Session 15). Phase 3B-B's R2 closure exhausted one mechanistic class (belt-IRREP-projection within harmonic Hessian); Phase 4's sign-theorem closure exhausts a different mechanistic class (perturbative correction at any order in Gaussian expansion at canonical geometry). The two together exhaust the Gaussian-K$_3$ framework at fixed cluster geometry. Subsequent sessions must move *outside* this framework — geometric-shift channels (R3, R4) or out-of-framework physics ((b), (c)).

The lesson-learned about including the analytical sign check as a default falsifier (F1) in scoping investigations should propagate to future Priority-1-style forward pointers.

---

*Step H paste-ready handover per `templates/operating_system.md` §15 protocol.*
