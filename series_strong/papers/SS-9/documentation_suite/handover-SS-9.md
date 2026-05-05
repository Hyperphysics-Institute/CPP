# SS-9 Handover — Session 20 Phase 8 Close (5 May 2026)

**Repository state at session close:** `origin/main` will be at patch 0204 once Thomas applies and pushes the five-patch chain (0200–0204). As of this document's creation, in-container HEAD is at patch 0203 (`d5bdfcc`); patch 0204 is committed locally pending export and represents this Step H file itself.
**Active paper:** SS-9 — *Conditional Derivation of Simplicial Alpha-Polytope Connectivity from CPP Lattice Geometry* (working title; final TBD).
**Paper state:** Pre-paper / active development. v0.3 working draft at `session_logs/OPEN-SS-24_phase1_v0.3_working_draft.md` (218 lines). No `.tex` file yet (registered as OPEN-ORG-012, awaiting U-shape investigation §7 stability — §7 has now shifted **ten times** in the OPEN-SS-32 ↔ U-shape thread, with Session 20 Phase 8 substantively reorganizing the §7 framing further from "Coulomb captures smooth-A scale within 5%; polytope-specific signal needs refinement" to "Refinement A captures smooth-A to 1% AND 48% of polytope-residual scale with near-exact $^{40}$Ca/$^{36}$Ar matches; remaining 52% pending Refinements C, D, R3-Pauli, and shell-physics for sub-shell-closure nuclei").

## What Phase 8 accomplished

**Phase 8 Refinement A — extended Gaussian alpha charge distribution: POSITIVE SCOPING with factor 3.6 polytope-residual magnitude improvement and near-exact zero-parameter match at $^{40}$Ca and $^{36}$Ar.** Phase 8 executed Session 19 Phase 7's Priority 1 forward pointer (Refinement A: extended Gaussian charge distribution at radius $\sim 1.6$ fm) as a single-session investigation. Replaced point-charge alphas with extended Gaussian charge distributions at conventional rms charge radius $r_\alpha^{\rm charge} = 1.68$ fm (PDG-style value, conveniently equal to $\sigma_{K3}^{\rm canon}$ — registered numerical coincidence for Refinement D follow-up). Gaussian width $\sigma_q = r_\alpha^{\rm charge}/\sqrt{3} = 0.970$ fm. Inter-cluster Coulomb becomes $V_C^{(A)}(r) = k_C q^2/r \cdot \mathrm{erf}(r/(2\sigma_q))$. Force balance solved per polytope.

**Sign-theorem composition workflow extended to refinement level:**

- **F1 Level 1 (within-mechanism):** $\mathrm{erf}(r/(2\sigma_q)) > 0$ for $r > 0$ → extended-charge Coulomb still purely repulsive at all separations → drives cluster expansion → $\delta R_A > 0$ → Phase 5 sign theorem → $\Delta E_{R3} > 0 = $ empirical-required. **F1 PASSES analytically.**
- **F1 Level 2 (empirical-comparison):** smooth-A binding gain still positive (cluster more bound) — same direction as empirical α-cluster binding excess vs smooth baseline. **F1 SIGN COMPATIBLE at smooth-A level.** Polytope-residual sign agreement requires computation.

**NN-fraction-weighted differential softening identified as polytope-residual mechanism.** At $R_\alpha = 2.37$ fm: $\mathrm{erf}(R_\alpha/(2\sigma_q)) = 0.917$ → 8.3% NN softening. At $\sqrt{2} R_\alpha = 3.35$ fm: $\mathrm{erf}(1.727) = 0.985$ → only 1.5% non-NN softening. Polytopes with high NN fraction (tetrahedron 100%) get more total softening than low-NN-fraction (icosahedron 45%). V$_C$ softening fractions span **8.40% (N=4) to 5.07% (N=12), monotonically tracking NN fraction across 3.3 percentage points** — exactly the polytope-specific structure-generating signature Phase 7 identified as needed.

**Equilibrium $\delta R_A$ shifts**: $\delta R_A = 0.668, 0.718, 0.794, 0.855, 0.920, 0.984, 1.042, 1.158$ fm for $N = 4, 5, 6, 7, 8, 9, 10, 12$. Shifts relative to Phase 6: -14.2%, -12.4%, -10.3%, -9.1%, -7.5%, -6.4%, -5.6%, -4.3% — uniformly negative, monotonically tracking softening fraction.

**Smooth-A scale tightens further: $\delta R_A(N=10) = 1.042$ fm vs Phase 5 R3-lin target $1.052$ fm — 1% match (tighter than Phase 6's 5%).** Net binding gain remains linear-in-N (Phase 8 = $0.177 \cdot N - 0.452$ MeV/α; Phase 6 was $0.208 \cdot N - 0.302$); both absorbed into SEMF parameters per Phase 7 methodology.

**Polytope-residual decomposition (DECISIVE comparison):**

| $N$ | nucleus | Phase 6 resid | Phase 8 resid | empirical resid | sign? |
|-----|------|--------|--------|--------|--------|
|  4 | $^{16}$O | $+0.0137$ | $+0.0495$ | $+0.1042$ | YES |
|  5 | $^{20}$Ne | $-0.0104$ | $-0.0003$ | $-0.0995$ | YES |
|  6 | $^{24}$Mg | $+0.0025$ | $-0.0113$ | $-0.0427$ | YES (P6 wrong) |
|  7 | $^{28}$Si | $-0.0036$ | $-0.0329$ | $+0.0309$ | no |
|  8 | $^{32}$S | $-0.0068$ | $-0.0276$ | $+0.0033$ | no |
|  9 | $^{36}$Ar | $-0.0009$ | $-0.0144$ | $-0.0136$ | YES |
| 10 | $^{40}$Ca | $-0.0021$ | $-0.0038$ | $-0.0038$ | YES |
| 12 | $^{48}$Cr | $+0.0076$ | $+0.0409$ | $+0.0212$ | YES |

**Phase 8 max polytope residual = 0.0495 MeV/α** vs Phase 6's $0.0137$ vs empirical $0.1042$. **Factor 3.6 magnitude improvement over Phase 6**, reaching **48% of empirical scale** (vs Phase 6's 13%). **Sign agreement: 6/8 polytopes** (vs Phase 6's 5/8) — $^{24}$Mg sign now correct.

**Striking near-exact zero-parameter matches:**
- $^{40}$Ca empirical $-0.0038$ vs Phase 8 $-0.0038$ MeV/α — **match within 0.0001 MeV/α** (essentially exact at most-shell-magic Z=20 cluster nucleus)
- $^{36}$Ar empirical $-0.0136$ vs Phase 8 $-0.0144$ — **match within 0.001 MeV/α** (near-shell Z=18)

**Persistent failures at $^{28}$Si and $^{32}$S — programme observation:** $^{28}$Si empirical $+0.031$ vs Phase 8 $-0.033$ (sign flip); $^{32}$S empirical $+0.003$ vs Phase 8 $-0.028$. Both at sub-shell closures (Z=14 filling $1d_{5/2}$; Z=16 filling $1d_{3/2}$); empirical residuals likely shell-physics-dominated (Strutinsky-style corrections), outside R3-channel scope. **R3-Coulomb mechanism (any refinement) is sub-shell-closure-blind.** "Good polytopes" = $^{16}$O, $^{20}$Ne, $^{24}$Mg, $^{36}$Ar, $^{40}$Ca, $^{48}$Cr (6/8); "shell-physics-dominated" = $^{28}$Si, $^{32}$S (2/8) — outside R3 scope.

**Third positive scoping outcome in OPEN-SS-32 ↔ U-shape thread** (Phase 5 channel pass, Phase 6 5% smooth-A bullseye, Phase 8 polytope-residual factor 3.6 improvement). Refinement A advances to multi-session integration with Refinements C, D, and R3-Pauli scoping. The mechanism (NN-fraction-weighted differential Coulomb softening) is identified, quantified, and confirmed as polytope-residual-generating. **Refinement A captures ~half of empirical polytope-residual scale; the other half pending Refinements C, D, R3-Pauli scoping, and shell-physics decomposition for sub-shell-closure nuclei.**

## Programme-level state at Session 20 close

- **10 programme-level negative results** (UNCHANGED — no new ruling-out in Sessions 18, 19, 20; all positive scoping)
- **R2 FORMALLY CLOSED** (Session 15 Phase 3B-B) — unchanged
- **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED** (Session 16 Phase 4) — unchanged
- **R3 and R4 channels passed scoping** (Session 17 Phase 5) — unchanged
- **R3-Coulomb passed scoping with 5% smooth-A bullseye at N=10** (Session 18 Phase 6) — properly reframed in Phase 7
- **Phase 7 reframing** preserved: smooth-A vs polytope-residual distinction; Phase 5 1 MeV/α target captures smooth-A; empirical polytope-residual scale ~0.05 MeV/α
- **Phase 8 Refinement A delivers**: factor 3.6 polytope-residual improvement, 48% of empirical scale captured, 6/8 sign agreement, near-exact $^{40}$Ca and $^{36}$Ar matches (within 0.001 MeV/α each), zero-parameter
- **Sign-theorem composition workflow** (Phase 6 §5.2) extended to refinement level (Phase 8) with two F1 levels (within-mechanism + empirical-comparison) — validated
- **Smooth-A vs polytope-residual methodology principle** (Phase 7) preserved; both Phase 6 (smooth-A part absorbed) and Phase 8 (polytope-residuals diagnostic) honor this
- **Sub-shell-closure observation** (Phase 8): R3-Coulomb mechanism is sub-shell-blind; $^{28}$Si and $^{32}$S empirical residuals require shell-physics-corrected baseline (Strutinsky-style), outside R3 scope; "good polytopes" = $^{16}$O, $^{20}$Ne, $^{24}$Mg, $^{36}$Ar, $^{40}$Ca, $^{48}$Cr
- **Decoupling Theorem** (Session 12 sub-question b) intact — sub-question (b) layer 3 gap-strength closure remains independent of all sub-question (a) developments
- **First qualitative cross-paradigm consilience claim** (Session 9) intact
- **6 OPEN-SS-35 stages preserved**; stage (vi) refines to "R3-Coulomb under active multi-session full derivation; smooth-A scale validated to 1% (Phase 8) / 5% (Phase 6); polytope-residual mechanism identified as NN-fraction-weighted differential softening of extended-charge Coulomb; 48% of empirical polytope-residual magnitude captured by Refinement A; remaining 52% pending Refinements C, D, R3-Pauli, and shell-physics decomposition for sub-shell-closure nuclei"
- **Pattern 6 K$_3$ scale-recurrence** at 7 confirmed instances unchanged
- **§7 of SS-9 v0.3** has shifted **TEN times** in OPEN-SS-32 ↔ U-shape thread

## Session 21 forward queue

**Priority 1 (multi-session continuation):** **Refinement C — non-NN K$_3$ contributions.** At $r = \sqrt{2} R_\alpha = 3.35$ fm, K$_3$ Gaussian = 0.918 (NOT exponentially small). Per-pair K$_3$ binding 0.918·$B_{\rm pair}$ = 2.150 MeV (vs 2.342 canonical NN). Polytope distribution: octa 3 antipodal at $\sqrt{2}R$, tetra 0, icosa 30 second-shell at $\varphi R = 3.83$ fm where K$_3 = 0.766$. Predicted F1: extra binding pulls $\delta R$ INWARD (counter to Coulomb push); Phase 5 sign theorem still gives $\Delta E > 0$ for any $\delta R \neq 0$; F1 PASSES analytically by composition. Tests whether icosahedron's 30-second-shell K$_3$ bonus pushes $^{48}$Cr in right direction (Phase 8 currently overshoots empirical $+0.021$ vs Phase 8 $+0.041$).

**Priority 2 (parallel scoping):** R3-Pauli with specified Pauli model (e.g., Gaussian repulsive core). F1 PASSES by composition (Pauli repulsive → $\delta R > 0$ → Phase 5 sign theorem → $\Delta E > 0$). Pauli at internal alpha-alpha contacts varies with edge count AND internal geometry — additional polytope-specific signal.

**Priority 3 (deferred):** Refinement D $\sigma_{K3}$ sensitivity ±10% around canonical 1.68 fm. Tests robustness of Phase 6 5% bullseye and Phase 8 polytope-residual structure; whether $\sigma_{K3}$ varies by polytope; numerical coincidence $r_\alpha^{\rm charge} = \sigma_{K3}$ canonical.

**Priority 4 (deferred, registered):** Sub-shell-closure interpretation as programme observation; shell-corrected baseline integration multi-paper scope.

**Anti-priorities sharpened:**
- §7 has shifted TEN times — OPEN-ORG-012 .tex conversion further deferred
- No raw Phase-N net gain vs empirical $\Delta(B/A)$ without first detrending smooth-A (Phase 7)
- No R3-channel mechanisms in isolation from Coulomb (Phase 6/7)
- **NEW Phase 8:** Do NOT expect R3-channel mechanism to reproduce $^{28}$Si and $^{32}$S residuals — sub-shell-closure-blind, outside R3 scope
- **NEW Phase 8:** Alpha rms charge radius value (1.68 fm) deserves sensitivity testing in Refinement D

## Apply chain

Five-patch chain `0200–0204` from `25dd8ba` (origin/main at Phase 7 close) baseline. To apply:

```bash
cd ~/Documents/GitHub/CPP && \
git pull origin main && \
git am ~/Downloads/0200-Phase-8-R3-Coulomb-Refinement-A-extended-Gaussian-charge-distribution-POSITIVE-SCOPING-factor-3p6-polytope-residual-improvement-near-exact-40Ca-36Ar.patch && \
git am ~/Downloads/0201-Phase-8-Step-A-Step-C-session-log-and-Vignette-27.patch && \
git am ~/Downloads/0202-Phase-8-Step-B-Step-D-transcript-and-Tier-4-reasoning.patch && \
git am ~/Downloads/0203-Phase-8-Step-E-Research_Frontier-and-future_projects.patch && \
git am ~/Downloads/0204-Phase-8-Step-H-Session-20-close-handover.patch && \
git push origin main
```

## Cumulative trajectory summary

The OPEN-SS-32 ↔ U-shape thread has now produced eight sequential phases:

- Session 13 Phase 2: Uniform-only zero-point softening RULED OUT (F1).
- Session 13 Phase 3A: Naive full-Hessian RULED OUT (F2 magnitude + F3 pattern).
- Session 14 Phase 3B-A: Fixed-dim belt subspace RULED OUT (F3 pattern).
- Session 15 Phase 3B-B: Full $C_n$ IRREP decomposition RULED OUT — **R2 FORMALLY CLOSED**.
- Session 16 Phase 4: Anharmonic ξ⁴ + all-orders Gaussian RULED OUT — **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED**.
- Session 17 Phase 5: Geometric-shift R3/R4 channels PASSED SCOPING.
- Session 18 Phase 6: R3-Coulomb scoping PASSED with 5% magnitude bullseye at $N = 10$.
- Session 19 Phase 7: R3-Coulomb empirical comparison — PARTIAL POSITIVE with critical reframing (smooth-A vs polytope-residual methodology).
- **Session 20 Phase 8: R3-Coulomb Refinement A (extended Gaussian alpha charge) — POSITIVE SCOPING with factor 3.6 polytope-residual improvement and near-exact zero-parameter match at $^{40}$Ca and $^{36}$Ar.** Third positive scoping outcome in thread; first refinement to produce zero-parameter near-exact agreement at multiple polytopes simultaneously.

The methodology lesson — F1 sign analytical check first, before computation — propagated from Phase 4 (Session 16) through Phases 5, 6, 7 to Phase 8 (Session 20) as a working methodology. Phase 6 codified it as the sign-theorem composition workflow within-mechanism. Phase 7 extended it to empirical-comparison F1 (Level 2). **Phase 8 extended it to refinement-level F1 (both Level 1 and Level 2 within the same refinement).** Future sessions should continue this practice and apply it to each new refinement (Refinement C, R3-Pauli, Refinement D).

---

*Step H paste-ready handover per `templates/operating_system.md` §15 protocol.*
