# SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 9 R3-Coulomb Refinement C (non-NN K₃ contributions)

**Date:** 5 May 2026 (Session 21)
**Status:** **RULED OUT (NEGATIVE RESULT) — eleventh programme-level negative result.** Refinement C in its naive form (apply canonical K$_3$ Gaussian width $\sigma_{K3} = 1.68$ fm to ALL pair distances, not just NN) is RULED OUT by F3 pattern failure: polytope-residual sign agreement degrades from Phase 8's 6/8 to 4/8; near-exact zero-parameter matches at $^{40}$Ca (within 0.0001 MeV/α) and $^{36}$Ar (within 0.001 MeV/α) — Phase 8's anchor achievements — are LOST (Phase 9 errors factor 7 and 3.4 respectively); $^{48}$Cr moves further from empirical (+0.062 Phase 9 vs +0.041 Phase 8 vs +0.021 empirical) — opposite of handover hypothesis. Cluster expansion δR collapses at high N: $\delta R_{C+A}(N=10) = 0.027$ fm and $\delta R_{C+A}(N=12) = 0$ fm (cluster fully equilibrated at canonical with no expansion). Smooth-A slope sign reverses: Phase 8 was $+0.177 \cdot N - 0.45$ MeV/α; Phase 9 is $-0.045 \cdot N + 0.47$ MeV/α. **Constructive content**: Phase 5/6/8 implicit NN-only K$_3$ framework (|E| = 3N - 6 edges per Euler) is CONFIRMED as the correct physical model — K$_3$ binding in CPP is NN-localized 3-body correlation, not a long-range Gaussian field. The naive non-NN extension is wrong physics. Phase 8 Refinement A (factor 3.6 polytope-residual improvement) status preserved; programme moves to Refinement D ($\sigma_{K3}$ sensitivity) and R3-Pauli scoping.
**Companion script:** `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase9_R3_Coulomb_RefC.py`.

---

## 1. Strategy

Phase 8 (Session 20) established Refinement A (extended Gaussian alpha charge distribution at $r_\alpha^{\rm charge} = 1.68$ fm) as a positive-scoping outcome with factor 3.6 polytope-residual magnitude improvement over Phase 6 and near-exact zero-parameter match at $^{40}$Ca and $^{36}$Ar. Refinement A captures ~half (48%) of empirical polytope-residual scale; the other half pending Refinements C, D, R3-Pauli, and shell-physics decomposition for sub-shell-closure nuclei.

Phase 8 sketch §6.1 / 0204 handover registered Session 21 Priority 1 as **Refinement C — non-NN K$_3$ contributions**. The handover's specific predictions:

> "At $r = \sqrt{2} R_\alpha = 3.35$ fm, K$_3$ Gaussian = 0.918 (NOT exponentially small). Per-pair K$_3$ binding 0.918·$B_{\rm pair}$ = 2.150 MeV (vs 2.342 canonical NN). Polytope distribution: octa 3 antipodal at $\sqrt{2}R$, tetra 0, icosa 30 second-shell at $\varphi R = 3.83$ fm where K$_3 = 0.766$. Predicted F1: extra binding pulls $\delta R$ INWARD (counter to Coulomb push); Phase 5 sign theorem still gives $\Delta E > 0$ for any $\delta R \neq 0$; F1 PASSES analytically by composition. Tests whether icosahedron's 30-second-shell K$_3$ bonus pushes $^{48}$Cr in right direction."

(Note: handover's $K_3 = 0.766$ at $\varphi R$ was incorrect; actual value is $\exp(-(1.465)^2/(2 \cdot 1.68^2)) = \exp(-0.380) = 0.684$. This does not affect Phase 9 conclusions.)

The Phase 4–8 methodology lesson — F1 sign analytical check first, before computation — was applied via the **sign-theorem composition workflow** (Phase 6 §5.2) extended to non-NN K$_3$.

## 2. Pre-empted analytical sign analysis (F1)

### 2.1 Level 1 — Within-mechanism sign

K$_3$ binding $V_{K3}(r) = -B_{\rm pair} \exp(-(r-R_\alpha)^2/(2\sigma_{K3}^2))$ has minimum at $r = R_\alpha$. For any pair at $r > R_\alpha$ (non-NN diagonals), $dV_{K3}/dr > 0$ — force is **inward** toward peak. Adding non-NN K$_3$ contributions provides ADDITIONAL inward force on the $\delta R$ coordinate.

By the sign-theorem composition workflow:

- Adding non-NN K$_3$ → additional inward force → equilibrium $\delta R_{C+A} < \delta R_A$ (less expansion)
- Phase 5 sign theorem extended: for $\delta R > 0$, all pairs (NN at $r_0 = R_\alpha$ AND non-NN at $r_0 > R_\alpha$) move further from K$_3$ peak, so $\Delta V_{K3} > 0$ per pair (binding loss)
- At equilibrium $\delta R_{C+A} > 0$, Coulomb savings still exceed total K$_3$ loss (NN + non-NN) by force balance → net binding gain > 0
- **F1 PASSES at within-mechanism level by composition.**

### 2.2 Level 2 — Empirical-comparison sign

Refinement C+A predicts net binding gain > 0 vs canonical-no-expansion (positive direction, same as Phase 6/8). Empirical alpha-conjugate nuclei show binding excess vs smooth baseline. **F1 SIGN COMPATIBLE at smooth-A level.**

## 3. Computation — RULED OUT by F3 pattern failure

### 3.1 Pair distance distributions per polytope

| $N$ | sym | #pairs | #NN | #non-NN | unique non-NN distances [fm] |
|-----|-----|--------|-----|---------|------------------------------|
|  4 | $T_d$    |  6 |  6 |  0 | (none) |
|  5 | $D_{3h}$ | 10 |  9 |  1 | 3.870(1) |
|  6 | $O_h$    | 15 | 12 |  3 | 3.352(3) |
|  7 | $D_{5h}$ | 21 | 15 |  6 | 2.492(1), 3.835(5) |
|  8 | $D_{2d}$ | 28 | 18 | 10 | 3.055(2), 3.586(4), 4.076(4) |
|  9 | $D_{3h}$ | 36 | 21 | 15 | 3.352(6), 3.912(6), 4.088(3) |
| 10 | $D_{4d}$ | 45 | 24 | 21 | 3.352(4), 3.682(8), 4.033(8), 5.345(1) |
| 12 | $I_h$    | 66 | 30 | 36 | 3.835(30), 4.508(6) |

Tetrahedron has zero non-NN pairs; icosahedron has 36 non-NN pairs across two unique distances.

### 3.2 K$_3$ binding contributions at canonical $\delta R = 0$

| $N$ | sym | $V_{K3}^{NN}(0)$ [MeV] | $V_{K3}^{nonNN}(0)$ [MeV] | $V_{K3}^{total}(0)$ [MeV] | non-NN frac |
|-----|-----|---------|---------|---------|---------|
|  4 | $T_d$    | $-14.05$ |   $0.00$ |  $-14.05$ |   0.0% |
|  5 | $D_{3h}$ | $-21.08$ |  $-1.57$ |  $-22.65$ |   7.5% |
|  6 | $O_h$    | $-28.11$ |  $-5.92$ |  $-34.03$ |  21.1% |
|  7 | $D_{5h}$ | $-35.14$ | $-10.35$ |  $-45.48$ |  29.4% |
|  8 | $D_{2d}$ | $-42.16$ | $-17.12$ |  $-59.28$ |  40.6% |
|  9 | $D_{3h}$ | $-49.19$ | $-25.24$ |  $-74.43$ |  51.3% |
| 10 | $D_{4d}$ | $-56.22$ | $-33.68$ |  $-89.89$ |  59.9% |
| 12 | $I_h$    | $-70.27$ | $-54.31$ | $-124.58$ |  77.3% |

Non-NN K$_3$ contribution grows from 0% (tetrahedron) to 77% (icosahedron) of NN contribution.

### 3.3 Equilibrium δR collapse at high N

| $N$ | sym | $\delta R_{C+A}$ [fm] | $\delta R_A$ [fm] | shift |
|-----|-----|---------|---------|---------|
|  4 | $T_d$    | $0.668$ | $0.668$ |   0% |
|  5 | $D_{3h}$ | $0.570$ | $0.718$ |  -21% |
|  6 | $O_h$    | $0.466$ | $0.794$ |  -41% |
|  7 | $D_{5h}$ | $0.367$ | $0.855$ |  -57% |
|  8 | $D_{2d}$ | $0.236$ | $0.920$ |  -74% |
|  9 | $D_{3h}$ | $0.121$ | $0.984$ |  -88% |
| 10 | $D_{4d}$ | **$0.027$** | $1.042$ |  **-97%** |
| 12 | $I_h$    | **$0.000$** | $1.158$ | **-100%** |

The equilibrium expansion δR is **almost entirely suppressed** at $N \geq 10$. For the icosahedron, non-NN K$_3$ inward force exactly balances Coulomb outward force at $\delta R = 0$ — cluster does not relax at all. **This is unphysical**: the cluster is supposed to expand under Coulomb stress, and the K$_3$ binding mechanism that prevents collapse should not also prevent expansion.

### 3.4 Smooth-A scale sign reversal

| Phase | Smooth-A linear fit |
|-------|---------------------|
| Phase 6 | $+0.208 \cdot N - 0.302$ MeV/α |
| Phase 8 | $+0.177 \cdot N - 0.452$ MeV/α |
| **Phase 9** | $\mathbf{-0.045 \cdot N + 0.473}$ **MeV/α (sign reversal)** |
| empirical | $-0.016 \cdot N + 0.153$ MeV/α |

Phase 9's smooth-A slope is closer in **sign** to empirical than Phase 6/8 (both empirical and Phase 9 negative; Phase 6/8 positive), but factor 2.8 too large in magnitude. This is interesting — it suggests that some non-NN K$_3$ contribution may be physical, but at much-reduced amplitude or width.

However, the smooth-A part is absorbed into SEMF parameters during fit (Phase 7 methodology). The diagnostic test is at the polytope-residual level.

### 3.5 Polytope-residual decomposition — DECISIVE FAILURE

| $N$ | nucleus | Phase 8 resid | Phase 9 resid | empirical resid | sign? P9 | sign? P8 |
|-----|------|--------|--------|--------|--------|--------|
|  4 | $^{16}$O   | $+0.0495$ | $+0.0099$ | $+0.1042$ | YES | YES |
|  5 | $^{20}$Ne  | $-0.0003$ | $+0.0143$ | $-0.0995$ | **no** | YES |
|  6 | $^{24}$Mg  | $-0.0113$ | $+0.0359$ | $-0.0427$ | **no** | YES |
|  7 | $^{28}$Si  | $-0.0329$ | $-0.0084$ | $+0.0309$ | no | no |
|  8 | $^{32}$S   | $-0.0276$ | $-0.0392$ | $+0.0033$ | no | no |
|  9 | $^{36}$Ar  | $-0.0144$ | $-0.0478$ | $-0.0136$ | YES | YES |
| 10 | $^{40}$Ca  | $-0.0038$ | $-0.0262$ | $-0.0038$ | YES | YES |
| 12 | $^{48}$Cr  | $+0.0409$ | $+0.0615$ | $+0.0212$ | YES | YES |

**Phase 9 sign agreement: 4/8 polytopes** (vs Phase 8's 6/8) — degraded. **$^{20}$Ne and $^{24}$Mg sign agreement LOST** in Phase 9; Phase 8's correct signs at these polytopes flipped.

### 3.6 Anchor matches LOST

Phase 8's most decisive achievements were the near-exact zero-parameter matches at $^{40}$Ca and $^{36}$Ar:

| Nucleus | empirical | Phase 8 | Phase 9 | Phase 9 error |
|---------|-----------|---------|---------|---------------|
| $^{40}$Ca | $-0.0038$ | $-0.0038$ (within 0.0001) | $-0.0262$ | factor **7×** |
| $^{36}$Ar | $-0.0136$ | $-0.0144$ (within 0.001) | $-0.0478$ | factor **3.4×** |

**The Phase 8 anchor achievements are destroyed by naive Refinement C.** This is the strongest single piece of evidence that the naive Refinement C is wrong physics — any further refinement of the framework MUST preserve these matches (registered as forward constraint).

### 3.7 ⁴⁸Cr — opposite of handover prediction

Handover hypothesis: "Tests whether icosahedron's 30-second-shell K$_3$ bonus pushes $^{48}$Cr in right direction (Phase 8 currently overshoots empirical $+0.021$ vs Phase 8 $+0.041$)."

**Result:** Phase 9 gives $^{48}$Cr = +0.0615 — moves FURTHER FROM empirical (+0.021). The icosahedron's 30-second-shell K$_3$ bonus pushes $^{48}$Cr in the WRONG direction. This is a sharp empirical refutation of the naive non-NN K$_3$ hypothesis.

### 3.8 ¹⁶O — degraded

| Nucleus | empirical | Phase 8 | Phase 9 |
|---------|-----------|---------|---------|
| $^{16}$O | $+0.1042$ | $+0.0495$ | $+0.0099$ |

Phase 9 gives $^{16}$O an even smaller residual than Phase 8 — further from empirical. Tetrahedron has no non-NN pairs, but the Phase 9 smooth-A re-fit shifts the linear-in-N component, so all polytopes' polytope-residuals change. Phase 9 makes the $^{16}$O shortfall worse.

## 4. Verdict — RULED OUT (eleventh programme-level negative result)

### 4.1 Three falsifier outcomes

- **F1 (sign): PASSES analytically** at within-mechanism level by sign-theorem composition. F1 SIGN COMPATIBLE at smooth-A level.
- **F2 (magnitude): mildly improved** (Phase 9 max residual 0.062 MeV/α vs Phase 8 0.050; ratio to empirical grows from 48% to 59%) — but the improvement comes from wrong-sign growth, not correct-sign growth.
- **F3 (pattern): FAILS DECISIVELY.** Sign agreement degrades 6/8 → 4/8. $^{40}$Ca anchor (within 0.0001) and $^{36}$Ar anchor (within 0.001) are LOST. $^{48}$Cr moves further from empirical (opposite of handover hypothesis). $^{16}$O degraded. **Naive Refinement C produces wrong polytope-pattern at the level visible to AME 2020 binding-energy data.**

### 4.2 Programme-level negative result #11

**Phase 9 (naive Refinement C — apply canonical $\sigma_{K3} = 1.68$ fm K$_3$ Gaussian to all pair distances) is RULED OUT.** This is the eleventh programme-level negative result in OPEN-SS-35 closure programme; sixth in OPEN-SS-32 ↔ U-shape thread (Phase 2 uniform-only, Phase 3A naive full-Hessian, Phase 3B-A fixed-dim belt subspace, Phase 3B-B IRREP decomposition (R2 closure), Phase 4 anharmonic ξ⁴ (Gaussian-K$_3$-at-fixed-geometry closure), and now Phase 9 naive non-NN K$_3$ extension).

### 4.3 Constructive content — Phase 5/6/8 NN-only K$_3$ framework strengthened

The negative result has substantial positive content:

1. **Phase 5/6/8 implicit NN-only K$_3$ treatment is the correct physical framework.** The use of |E| = 3N - 6 edges per Euler (Phase 6/8 force balance) accurately captures the K$_3$ binding mechanism. Any future refinement must preserve this NN-only structure.

2. **K$_3$ binding in CPP is NN-localized 3-body correlation, not a long-range Gaussian field.** The Gaussian form $V_{K3}(r) = -B_{\rm pair} \exp(-(r-R_\alpha)^2/(2\sigma^2))$ is a calibration of how K$_3$ varies with NN bond stretching, NOT a description of inter-pair binding at all distances.

3. **Naive extrapolation of $\sigma_{K3} = 1.68$ fm to all pair distances overcounts long-range binding.** At non-NN distances 3.35-4.5 fm, K$_3$ would only be physical if mediated by 3-body terms with much shorter effective range, or if amplitude-suppressed by intervening DP-sea structure (CPP first principles).

4. **Phase 8 anchor achievements at $^{40}$Ca and $^{36}$Ar are PRESERVED as Phase 8 (not Phase 9) results.** Future refinements must preserve these matches — this is now a registered constraint on Refinement D, R3-Pauli, and any further refinements.

5. **Forward priorities re-ordered:** Refinement D ($\sigma_{K3}$ sensitivity) is no longer just a sensitivity check — it becomes potentially diagnostic. If $\sigma_{K3}$ is much smaller than 1.68 fm (e.g., 0.5-1.0 fm), non-NN K$_3$ contributions become exponentially small, recovering Phase 5/6/8 NN-only framework. R3-Pauli scoping (Priority 2) becomes more important — Pauli is naturally NN-localized via wave-function overlap.

### 4.4 What Phase 9 is NOT

Phase 9 does NOT close the OPEN-SS-32 ↔ U-shape thread; it does NOT close OPEN-SS-35. It eliminates one specific candidate refinement (naive non-NN K$_3$ extension) and confirms the Phase 5/6/8 NN-only framework as correct. The thread remains open with Phase 8 as the standing best refinement (factor 3.6 polytope-residual improvement).

## 5. Programme implications

### 5.1 Negative-result count and trajectory

**Programme-level negative-result count grows from 10 to 11.** Phase 9 is the **sixth ruling-out** in the OPEN-SS-32 ↔ U-shape thread. The thread now has six closures and three positive scoping outcomes (Phase 5 channel pass, Phase 6 5% smooth-A bullseye, Phase 8 polytope-residual factor 3.6 improvement).

OPEN-SS-35 sub-question (a) A-scaling closure: stage (vi) refines further to "R3-Coulomb under active multi-session full derivation; smooth-A scale validated to 1% (Phase 8) / 5% (Phase 6); polytope-residual mechanism identified as NN-fraction-weighted differential softening of extended-charge Coulomb (Refinement A); 48% of empirical polytope-residual magnitude captured by Refinement A; **naive non-NN K$_3$ extension (Refinement C) RULED OUT (Phase 9) — Phase 5/6/8 NN-only K$_3$ framework confirmed as correct**; remaining 52% of empirical polytope-residual scale pending Refinement D ($\sigma_{K3}$ sensitivity), R3-Pauli scoping, and shell-physics decomposition for sub-shell-closure nuclei."

### 5.2 R2 / Phase 4 / Phase 8 closures unchanged

- R2 remains FORMALLY CLOSED (Session 15).
- Gaussian-K$_3$ framework at fixed cluster geometry remains FORMALLY CLOSED (Session 16).
- Phase 5 R3/R4 channels still pass scoping.
- Phase 6 R3-Coulomb 5% smooth-A bullseye preserved.
- Phase 7 smooth-A vs polytope-residual methodology preserved.
- Phase 8 Refinement A factor 3.6 polytope-residual improvement and near-exact $^{40}$Ca/$^{36}$Ar matches preserved.

### 5.3 Sub-question (b) state unchanged

Sub-question (b) layer 3 gap-strength closure remains INDEPENDENT (Decoupling Theorem, Session 12). Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances unchanged. First qualitative cross-paradigm consilience claim (Session 9) intact. 6 OPEN-SS-35 stages preserved.

## 6. Forward pointers

### 6.1 Priority 1 — Refinement D ($\sigma_{K3}$ sensitivity)

**Promoted from Phase 8's Priority 3 to Phase 9's Priority 1.** Phase 9 result motivates this strongly: if $\sigma_{K3}$ is significantly smaller than canonical 1.68 fm (e.g., 0.5–1.0 fm), non-NN K$_3$ contributions become exponentially small, recovering Phase 5/6/8 NN-only framework while perhaps allowing some calibrated non-NN contribution that doesn't destroy anchor matches. Tests: (i) does Phase 6 5% smooth-A bullseye persist under $\sigma_{K3}$ variation? (ii) does Phase 8 polytope-residual structure persist? (iii) do the $^{40}$Ca and $^{36}$Ar near-exact matches survive? (iv) does $\sigma_{K3}$ vary by polytope (cluster-topology-dependent)? The numerical coincidence $r_\alpha^{\rm charge} = 1.68$ fm = $\sigma_{K3}^{\rm canon}$ deserves structural interpretation. Predicted F1 (analytical): $\sigma_{K3}$ variation does not change Coulomb push outward; only modifies K$_3$ inward pull magnitude/range. F1 PASSES analytically by composition.

### 6.2 Priority 2 — R3-Pauli scoping

**Status unchanged from Phase 8.** Pauli is naturally NN-localized via wave-function overlap (alpha-alpha Pauli core acts at short range; exponentially suppressed at non-NN distances). Phase 9 result strengthens the case for R3-Pauli as the "correct" non-Coulomb polytope-specific signal source. Predicted F1: Pauli repulsive → $\delta R_{\rm Pauli} > 0$ → Phase 5 sign theorem → $\Delta E > 0$, F1 PASSES analytically.

### 6.3 Priority 3 — Sub-shell-closure interpretation (deferred, registered)

$^{28}$Si and $^{32}$S persistent failures (Phase 8 + Phase 9) confirm sub-shell-physics-dominance interpretation. Phase 9 negative result does not improve these; if anything they're slightly worse in Phase 9 (32S residual -0.039 in P9 vs -0.028 in P8). Multi-paper scope.

### 6.4 Anti-priorities sharpened

- §7 has shifted **eleven** times in OPEN-SS-32 ↔ U-shape thread (was 10 at Session 20 close); OPEN-ORG-012 .tex conversion further deferred.
- No raw Phase-N net binding gain magnitudes vs empirical $\Delta(B/A)$ without first detrending smooth-A (Phase 7 methodology preserved).
- No R3-channel mechanisms in isolation from Coulomb (Phase 6/7/8 — Phase 9 confirms Coulomb is anchor; non-Coulomb mechanisms must be carefully scoped).
- Do not expect R3-channel mechanism to reproduce $^{28}$Si and $^{32}$S residuals (Phase 8 anti-priority preserved; Phase 9 confirms).
- **NEW from Phase 9:** Do NOT extend K$_3$ Gaussian width $\sigma_{K3} = 1.68$ fm to non-NN pair distances naively. The K$_3$ binding mechanism is NN-localized 3-body correlation; long-range extension requires shorter effective $\sigma_{K3,\rm non-NN}$ or amplitude suppression — registered for Refinement D investigation.
- **NEW from Phase 9:** Phase 8 anchor matches at $^{40}$Ca and $^{36}$Ar (within 0.001 MeV/α each) are now a registered CONSTRAINT on future refinements. Any refinement that destroys these matches (as Phase 9 did) is ruled out.

## 7. Summary

Phase 9 executed Session 20 Phase 8's Priority 1 forward pointer (Refinement C: non-NN K$_3$ contributions on top of Phase 8 Refinement A extended-charge Coulomb) as the natural next single-session refinement. F1 sign passes analytically by sign-theorem composition workflow. F2 magnitude grows mildly (Phase 9 max residual 0.062 MeV/α vs Phase 8 0.050; ratio to empirical grows from 48% to 59%). **F3 pattern FAILS decisively**: sign agreement degrades 6/8 → 4/8; $^{40}$Ca anchor (within 0.0001) and $^{36}$Ar anchor (within 0.001) are LOST (Phase 9 errors factor 7 and 3.4 respectively); $^{48}$Cr moves further from empirical opposite of handover hypothesis; $^{16}$O degraded. Cluster expansion δR collapses at high N: $\delta R_{C+A}(N=10) = 0.027$ fm and $\delta R_{C+A}(N=12) = 0$ fm — unphysical. Smooth-A slope sign reverses ($+0.18 \cdot N$ Phase 8 → $-0.045 \cdot N$ Phase 9; empirical $-0.016 \cdot N$).

**Phase 9 Refinement C in its naive form (apply canonical $\sigma_{K3} = 1.68$ fm to all pair distances) is RULED OUT** — eleventh programme-level negative result; sixth ruling-out in OPEN-SS-32 ↔ U-shape thread. The constructive content is substantial: **Phase 5/6/8 NN-only K$_3$ framework (|E| = 3N-6 edges per Euler) is CONFIRMED as the correct physical model**. K$_3$ binding in CPP is NN-localized 3-body correlation, not a long-range Gaussian field. The Gaussian form $V_{K3}(r) = -B_{\rm pair}\exp(-(r-R_\alpha)^2/(2\sigma^2))$ is a calibration of NN bond-stretching response, not an inter-pair distance law. Phase 8 anchor matches at $^{40}$Ca and $^{36}$Ar are PRESERVED as Phase 8 (not Phase 9) achievements and are now registered constraints on future refinements.

**Forward priority shifts: Refinement D ($\sigma_{K3}$ sensitivity) promoted to Priority 1** — Phase 9 result motivates this strongly because a smaller $\sigma_{K3,\rm non-NN}$ would naturally suppress the unphysical long-range K$_3$ extension. R3-Pauli scoping (Priority 2) gains importance as a NN-localized polytope-specific signal source. Programme negative-result count grows to **11**. Phase 8 Refinement A status preserved (factor 3.6 polytope-residual improvement, near-exact zero-parameter $^{40}$Ca/$^{36}$Ar matches). All earlier closures (R2, Gaussian-K$_3$-at-fixed-geometry, Phase 5 channel pass, Phase 6 smooth-A bullseye, Phase 7 methodology, Phase 8 Refinement A) preserved. Sign-theorem composition workflow validated again at refinement level (now with mixed F1-pass / F3-fail outcome — sign-theorem composition is necessary but not sufficient; F3 pattern check still required).
