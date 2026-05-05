# SS-9 Handover — Session 21 Phase 9 Close (5 May 2026)

**Repository state at session close:** `origin/main` will be at patch 0209 once Thomas applies and pushes the five-patch chain (0205–0209). As of this document's creation, in-container HEAD is at patch 0208 (`80efe79`); patch 0209 is committed locally pending export and represents this Step H file itself.
**Active paper:** SS-9 — *Conditional Derivation of Simplicial Alpha-Polytope Connectivity from CPP Lattice Geometry* (working title; final TBD).
**Paper state:** Pre-paper / active development. v0.3 working draft at `session_logs/OPEN-SS-24_phase1_v0.3_working_draft.md` (218 lines). No `.tex` file yet (registered as OPEN-ORG-012, awaiting U-shape investigation §7 stability — §7 has now shifted **eleven times** in the OPEN-SS-32 ↔ U-shape thread, with Session 21 Phase 9 substantively reorganizing the §7 framing further from "Refinement A captures smooth-A to 1% AND 48% of polytope-residual scale" to "Refinement A captures smooth-A to 1% AND 48% of polytope-residual scale with NN-only K$_3$ framework confirmed as correct after Phase 9 ruling-out of naive non-NN K$_3$ extension; remaining 52% pending Refinement D, R3-Pauli, and shell-physics for sub-shell-closure nuclei").

## What Phase 9 accomplished

**Phase 9 Refinement C — non-NN K$_3$ contributions: RULED OUT by F3 pattern failure; eleventh programme-level negative result; sixth ruling-out in OPEN-SS-32 ↔ U-shape thread.** Phase 9 executed Session 20 Phase 8's Priority 1 forward pointer (Refinement C: non-NN K$_3$ contributions on top of Phase 8 Refinement A extended-charge Coulomb) as the natural next single-session refinement. Extended K$_3$ binding from NN pairs only (Phase 6/8 framework) to ALL pair distances using canonical $\sigma_{K3} = 1.68$ fm.

**Sign-theorem composition workflow extended to non-NN K$_3$:**

- **F1 Level 1 (within-mechanism):** $V_{K3}(r) = -B_{\rm pair}\exp(-(r-R_\alpha)^2/(2\sigma^2))$ has minimum at $r = R_\alpha$; for any pair past peak ($r > R_\alpha$, like non-NN diagonals), $dV/dr > 0$ → force inward toward peak; adding non-NN K$_3$ → additional inward force on $\delta R$ coordinate; equilibrium $\delta R_{C+A} < \delta R_A$. Phase 5 sign theorem extended: for $\delta R > 0$, all pairs (NN + non-NN) move further from K$_3$ peak → $\Delta V_{K3} > 0$ per pair. At $\delta R_{C+A} > 0$, Coulomb savings exceed total K$_3$ loss → net binding gain > 0. **F1 PASSES analytically.**
- **F1 Level 2 (empirical-comparison):** F1 SIGN COMPATIBLE at smooth-A level (predicted net gain > 0 same direction as empirical α-cluster excess).

**Non-NN K$_3$ contribution scales dramatically with polytope** — 0% (tetrahedron, no non-NN pairs) to 77.3% (icosahedron — 30 second-shell at $\varphi R_\alpha = 3.835$ fm where K$_3 = 0.684$, plus 6 antipodal at $\sqrt{1+\varphi^2}R_\alpha = 4.508$ fm where K$_3 = 0.445$). Octahedron has 21.1% (3 antipodal at $\sqrt{2}R_\alpha = 3.352$ fm where K$_3 = 0.918$).

**DECISIVE FINDING — equilibrium δR collapses dramatically at high N:**

| $N$ | $\delta R_A$ (Phase 8) [fm] | $\delta R_{C+A}$ (Phase 9) [fm] | shift |
|-----|---------|---------|---------|
|  4 | 0.668 | 0.668 | 0% |
| 10 | 1.042 | **0.027** | **-97%** |
| 12 | 1.158 | **0.000** | **-100%** |

For the icosahedron, non-NN K$_3$ inward force exactly balances Coulomb outward force at $\delta R = 0$ — cluster does NOT relax under Coulomb stress. **This is unphysical.**

**Smooth-A linear fit slope SIGN REVERSAL:** Phase 8 $+0.177 \cdot N - 0.452$ MeV/α → Phase 9 $-0.045 \cdot N + 0.473$ MeV/α (closer in sign to empirical $-0.016 \cdot N + 0.153$ but factor 2.8 too large in magnitude).

**DECISIVE F3 FAILURE — polytope-residual decomposition:**

| $N$ | nucleus | Phase 8 resid | Phase 9 resid | empirical | sign? P9 | sign? P8 |
|-----|------|--------|--------|--------|---------|---------|
|  4 | $^{16}$O   | $+0.0495$ | $+0.0099$ | $+0.1042$ | YES | YES |
|  5 | $^{20}$Ne  | $-0.0003$ | $+0.0143$ | $-0.0995$ | **no** | YES |
|  6 | $^{24}$Mg  | $-0.0113$ | $+0.0359$ | $-0.0427$ | **no** | YES |
|  7 | $^{28}$Si  | $-0.0329$ | $-0.0084$ | $+0.0309$ | no | no |
|  8 | $^{32}$S   | $-0.0276$ | $-0.0392$ | $+0.0033$ | no | no |
|  9 | $^{36}$Ar  | $-0.0144$ | $-0.0478$ | $-0.0136$ | YES | YES |
| 10 | $^{40}$Ca  | $-0.0038$ | $-0.0262$ | $-0.0038$ | YES | YES |
| 12 | $^{48}$Cr  | $+0.0409$ | $+0.0615$ | $+0.0212$ | YES | YES |

**Phase 9 sign agreement: 4/8 polytopes** (vs Phase 8's 6/8) — degraded. $^{20}$Ne and $^{24}$Mg sign agreement LOST.

**Phase 8 anchor matches DESTROYED:**
- $^{40}$Ca: empirical $-0.0038$ vs Phase 8 $-0.0038$ (within 0.0001) vs Phase 9 $-0.0262$ — **factor 7 error**
- $^{36}$Ar: empirical $-0.0136$ vs Phase 8 $-0.0144$ (within 0.001) vs Phase 9 $-0.0478$ — **factor 3.4 error**

**$^{48}$Cr handover hypothesis REFUTED:** Phase 9 $+0.0615$ vs Phase 8 $+0.0409$ vs empirical $+0.0212$. Phase 9 moves FURTHER from empirical, not closer. Icosahedron's 30-second-shell K$_3$ bonus pushes $^{48}$Cr in the WRONG direction.

**$^{16}$O degraded:** Phase 9 $+0.0099$ vs Phase 8 $+0.0495$ vs empirical $+0.1042$ — moves further from empirical.

**$^{28}$Si and $^{32}$S persistent failures continue** (sub-shell-physics-dominated, outside R3 scope per Phase 8 anti-priority). Phase 9 does not improve these; if anything they're slightly worse.

**Phase 9 outcome: RULED OUT by F3 pattern failure. Eleventh programme-level negative result.** F1 PASSES analytically; F3 FAILS DECISIVELY. Sign-theorem composition workflow validated again at refinement level **but with mixed F1-pass / F3-fail outcome** — sign-theorem composition is necessary but not sufficient; F3 pattern check still required.

## Constructive content — Phase 5/6/8 NN-only K$_3$ framework CONFIRMED as correct

The negative result has substantial positive content:

1. **Phase 5/6/8 implicit NN-only K$_3$ treatment is the correct physical framework.** The use of $|E| = 3N - 6$ edges per Euler (Phase 6/8 force balance) accurately captures the K$_3$ binding mechanism. Any future refinement must preserve this NN-only structure.
2. **K$_3$ binding in CPP is NN-localized 3-body correlation, not a long-range Gaussian field.** The Gaussian form $V_{K3}(r) = -B_{\rm pair}\exp(-(r-R_\alpha)^2/(2\sigma^2))$ is a calibration of NN bond-stretching response, NOT a description of inter-pair binding at all distances.
3. **Naive extrapolation of $\sigma_{K3} = 1.68$ fm to all pair distances overcounts long-range binding.** Physical K$_3$ at non-NN distances would require shorter $\sigma_{K3,\rm non-NN}$ or amplitude suppression.
4. **Phase 8 anchor achievements at $^{40}$Ca and $^{36}$Ar are PRESERVED as Phase 8 (not Phase 9) results.** Future refinements must preserve these matches — registered constraint on Refinement D, R3-Pauli, and any further refinements.
5. **Methodological lesson registered:** F1 sign analytical pre-check is gateway, not endorsement. Phase 9 is cleanest demonstration in OPEN-SS-32 ↔ U-shape thread of an F1-pass / F3-fail outcome.

## Programme-level state at Session 21 close

- **11 programme-level negative results** (UP from 10 — Phase 9 adds the eleventh)
- **R2 FORMALLY CLOSED** (Session 15 Phase 3B-B) — unchanged
- **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED** (Session 16 Phase 4) — unchanged
- **R3 and R4 channels passed scoping** (Session 17 Phase 5) — unchanged
- **R3-Coulomb passed scoping with 5% smooth-A bullseye at N=10** (Session 18 Phase 6) — properly reframed in Phase 7
- **Phase 7 reframing** preserved: smooth-A vs polytope-residual distinction; Phase 5 1 MeV/α target captures smooth-A; empirical polytope-residual scale ~0.05 MeV/α
- **Phase 8 Refinement A delivers**: factor 3.6 polytope-residual improvement, 48% of empirical scale captured, 6/8 sign agreement, near-exact $^{40}$Ca and $^{36}$Ar matches (within 0.001 MeV/α each), zero-parameter — STATUS PRESERVED as standing best refinement
- **Phase 9 Refinement C in naive form RULED OUT** — naive non-NN K$_3$ extension wrong physics; Phase 5/6/8 NN-only K$_3$ framework CONFIRMED as correct
- **Three positive scoping outcomes** in OPEN-SS-32 ↔ U-shape thread preserved: Phase 5 channel pass, Phase 6 5% smooth-A bullseye, Phase 8 polytope-residual factor 3.6 improvement
- **Sign-theorem composition workflow** (Phase 6 §5.2) validated at refinement level (Phase 8) and extended to non-NN K$_3$ (Phase 9) — necessary but not sufficient (Phase 9 demonstrates F1-pass / F3-fail)
- **Smooth-A vs polytope-residual methodology principle** (Phase 7) preserved
- **Sub-shell-closure observation** (Phase 8): R3-Coulomb mechanism is sub-shell-blind; $^{28}$Si and $^{32}$S empirical residuals require shell-physics-corrected baseline (Strutinsky-style), outside R3 scope; "good polytopes" = $^{16}$O, $^{20}$Ne, $^{24}$Mg, $^{36}$Ar, $^{40}$Ca, $^{48}$Cr
- **Anchor matches at $^{40}$Ca and $^{36}$Ar (Phase 8)** now registered as CONSTRAINT on future refinements
- **Decoupling Theorem** (Session 12 sub-question b) intact
- **First qualitative cross-paradigm consilience claim** (Session 9) intact
- **6 OPEN-SS-35 stages preserved**; stage (vi) refines to add "naive non-NN K$_3$ extension RULED OUT (Phase 9) — Phase 5/6/8 NN-only K$_3$ framework confirmed as correct"
- **Pattern 6 K$_3$ scale-recurrence** at 7 confirmed instances unchanged
- **§7 of SS-9 v0.3** has shifted **ELEVEN times** in OPEN-SS-32 ↔ U-shape thread

## Session 22 forward queue

**Priority 1 (single-session, PROMOTED from Phase 8 Priority 3):** **Refinement D — $\sigma_{K3}$ sensitivity ±10%** around canonical 1.68 fm, AND test whether $\sigma_{K3,\rm non-NN}$ should be much smaller (e.g., 0.5–1.0 fm) to recover Phase 5/6/8 NN-only behavior. Phase 9 result motivates this strongly: if $\sigma_{K3,\rm non-NN} \ll 1.68$ fm, non-NN K$_3$ contributions become exponentially small, recovering Phase 5/6/8 NN-only framework while perhaps allowing some calibrated non-NN contribution that doesn't destroy anchor matches. Tests: (i) Phase 6 5% smooth-A bullseye persistence; (ii) Phase 8 polytope-residual structure persistence; (iii) $^{40}$Ca and $^{36}$Ar near-exact match survival; (iv) does $\sigma_{K3}$ vary by polytope? Numerical coincidence $r_\alpha^{\rm charge} = 1.68$ fm = $\sigma_{K3}^{\rm canon}$ deserves structural interpretation. Predicted F1: $\sigma_{K3}$ variation does not change Coulomb push outward; only modifies K$_3$ inward pull magnitude/range. F1 PASSES analytically by composition.

**Priority 2 (parallel scoping, status strengthened by Phase 9):** R3-Pauli with specified Pauli model. Phase 9 result strengthens this case — Pauli is naturally NN-localized via wave-function overlap (alpha-alpha Pauli core acts at short range; exponentially suppressed at non-NN distances), avoiding Phase 9's failure mode. Predicted F1: Pauli repulsive → $\delta R_{\rm Pauli} > 0$ → Phase 5 sign theorem → $\Delta E > 0$, F1 PASSES analytically.

**Priority 3 (deferred, registered):** Sub-shell-closure interpretation. $^{28}$Si and $^{32}$S persistent failures (Phase 8 + Phase 9) confirm sub-shell-physics-dominance. Multi-paper scope.

**Anti-priorities sharpened:**
- §7 has shifted ELEVEN times — OPEN-ORG-012 .tex conversion further deferred
- No raw Phase-N net gain vs empirical $\Delta(B/A)$ without first detrending smooth-A (Phase 7)
- No R3-channel mechanisms in isolation from Coulomb (Phase 6/7/8/9)
- Do not expect R3-channel mechanism to reproduce $^{28}$Si and $^{32}$S residuals (Phase 8 anti-priority preserved)
- **NEW Phase 9:** Do NOT extend K$_3$ Gaussian width $\sigma_{K3} = 1.68$ fm to non-NN pair distances naively. K$_3$ binding mechanism is NN-localized 3-body correlation; long-range extension requires shorter effective $\sigma_{K3,\rm non-NN}$ or amplitude suppression — registered for Refinement D investigation.
- **NEW Phase 9:** Phase 8 anchor matches at $^{40}$Ca (within 0.0001 MeV/α) and $^{36}$Ar (within 0.001 MeV/α) are now registered CONSTRAINTS on future refinements. Any refinement that destroys these matches (as Phase 9 did) is ruled out at scoping.

## Apply chain

Five-patch chain `0205–0209` from `a15c97b` (origin/main at Phase 8 close) baseline. To apply:

```bash
cd ~/Documents/GitHub/CPP && \
git pull origin main && \
git am ~/Downloads/0205-Phase-9-R3-Coulomb-Refinement-C-non-NN-K3-RULED-OUT-by-F3-pattern-failure-11th-negative-result-NN-only-K3-framework-confirmed.patch && \
git am ~/Downloads/0206-Phase-9-Step-A-Step-C-session-log-and-Vignette-28.patch && \
git am ~/Downloads/0207-Phase-9-Step-B-Step-D-transcript-and-Tier-4-reasoning.patch && \
git am ~/Downloads/0208-Phase-9-Step-E-Research_Frontier-and-future_projects.patch && \
git am ~/Downloads/0209-Phase-9-Step-H-Session-21-close-handover.patch && \
git push origin main
```

## Cumulative trajectory summary

The OPEN-SS-32 ↔ U-shape thread has now produced nine sequential phases:

- Session 13 Phase 2: Uniform-only zero-point softening RULED OUT (F1).
- Session 13 Phase 3A: Naive full-Hessian RULED OUT (F2 magnitude + F3 pattern).
- Session 14 Phase 3B-A: Fixed-dim belt subspace RULED OUT (F3 pattern).
- Session 15 Phase 3B-B: Full $C_n$ IRREP decomposition RULED OUT — **R2 FORMALLY CLOSED**.
- Session 16 Phase 4: Anharmonic ξ⁴ + all-orders Gaussian RULED OUT — **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED**.
- Session 17 Phase 5: Geometric-shift R3/R4 channels PASSED SCOPING.
- Session 18 Phase 6: R3-Coulomb scoping PASSED with 5% magnitude bullseye at $N = 10$.
- Session 19 Phase 7: R3-Coulomb empirical comparison — PARTIAL POSITIVE with critical reframing (smooth-A vs polytope-residual methodology).
- Session 20 Phase 8: R3-Coulomb Refinement A (extended Gaussian alpha charge) — POSITIVE SCOPING with factor 3.6 polytope-residual improvement and near-exact zero-parameter match at $^{40}$Ca and $^{36}$Ar.
- **Session 21 Phase 9: R3-Coulomb Refinement C (non-NN K$_3$ contributions) — RULED OUT by F3 pattern failure; 11th programme-level negative result; sixth ruling-out in OPEN-SS-32 ↔ U-shape thread; Phase 5/6/8 NN-only K$_3$ framework CONFIRMED as correct.**

The methodology lesson — F1 sign analytical check first, before computation — propagated from Phase 4 (Session 16) through Phases 5, 6, 7, 8 to Phase 9 (Session 21) as a working methodology. Phase 6 codified it as the sign-theorem composition workflow within-mechanism. Phase 7 extended it to empirical-comparison F1 (Level 2). Phase 8 extended it to refinement-level F1 (both levels). **Phase 9 demonstrated that sign-theorem composition is necessary but not sufficient** — F1 PASSES analytically while F3 FAILS DECISIVELY. Methodological lesson: F1 sign analytical pre-check is gateway, not endorsement; F3 pattern check still required at the polytope-residual level. Future sessions should continue F1 first practice but recognize its bounded scope.

---

*Step H paste-ready handover per `templates/operating_system.md` §15 protocol.*
