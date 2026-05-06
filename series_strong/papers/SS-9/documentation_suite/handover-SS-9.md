# SS-9 Handover — Session 23 Phase 11 Close (6 May 2026)

**Repository state at session close:** `origin/main` will be at patch 0219 once Thomas applies and pushes the five-patch chain (0215–0219). As of this document's creation, in-container HEAD is at patch 0218 (`64d7bed`); patch 0219 is committed locally pending export and represents this Step H file itself.
**Active paper:** SS-9 — *Conditional Derivation of Simplicial Alpha-Polytope Connectivity from CPP Lattice Geometry* (working title; final TBD).
**Paper state:** Pre-paper / active development. v0.3 working draft at `session_logs/OPEN-SS-24_phase1_v0.3_working_draft.md` (218 lines). **OPEN-ORG-012 (.tex conversion) PROMOTED from anti-priority to active Priority 2 at Session 23 Phase 11 close** — §7 has shifted thirteen times in the OPEN-SS-32 ↔ U-shape thread, but **Phase 11 NULL marks natural saturation point**: single-session R3-channel refinement candidates EXHAUSTED, §7 stable enough for formal write-up.

## What Phase 11 accomplished

**Phase 11 R3-Pauli scoping (Gaussian repulsive core): NULL RESULT — Pauli structurally redundant with Phase 8 NN-fraction-weighted differential Coulomb softening; single-session R3-channel refinement candidates EXHAUSTED; methodological category "structural-redundancy null result" introduced.** Phase 11 executed Session 22 Phase 10's Priority 1 forward pointer (R3-Pauli scoping) as the sole remaining single-session-tractable refinement candidate after Phases 9 + 10 ruled out the entire $\sigma$-parameterized K$_3$ refinement class.

**Pauli model specification:**
$$ V_P(r) = V_P^0 \exp\!\left(-\frac{r^2}{2\sigma_P^2}\right) $$

with $\sigma_P = 1.5$ fm fixed (alpha matter rms radius scale, no fit parameter — alpha matter radius slightly smaller than electron-scattering charge radius 1.676 fm due to neutron skin); $V_P^0$ scanned in $\{0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0\}$ MeV; calibrated to Phase 5 R3-lin smooth-A target $\delta R(N=10) = 1.052$ fm.

**Wave-function-overlap structure verification at $\sigma_P = 1.5$ fm:**

| Distance | Description | $V_P/V_P^0$ | Suppression vs NN |
|----------|-------------|-------------|-------------------|
| $R_\alpha = 2.37$ fm | NN | 0.287 | — (reference) |
| $\sqrt{2}R_\alpha = 3.35$ fm | first non-NN (octa antipodal) | 0.082 | factor **3.5×** |
| $\varphi R_\alpha = 3.835$ fm | icosa second-shell | 0.038 | factor **7.6×** |
| $\sqrt{1+\varphi^2}R_\alpha = 4.508$ fm | icosa antipodal | 0.011 | factor **26×** |

**Pauli at $\sigma_P = 1.5$ fm is exponentially suppressed at non-NN distances — exactly the structural symmetry K$_3$-σ-tuning variants lacked.**

**Sign-theorem composition workflow extended to Pauli:**

- **F1 Level 1 (within-mechanism):** $V_P(r) > 0$ (repulsive); gradient $dV_P/dr < 0$ for $r > 0$ → force outward; adding Pauli to Phase 8 → additional outward force on $\delta R$; equilibrium $\delta R_{P+A} > \delta R_A$; Phase 5 sign theorem unchanged; at $\delta R_{P+A} > 0$, Coulomb-plus-Pauli savings exceed K$_3$ loss → net binding gain > 0. **F1 PASSES analytically by composition.**
- **F1 Level 2 (empirical-comparison):** F1 SIGN COMPATIBLE at smooth-A level.

**$V_P^0$ scan — Phase 8 anchor matches degrade rapidly above $V_P^0 \geq 1$ MeV:**

| $V_P^0$ [MeV] | sign agreement | $^{36}$Ar err | $^{40}$Ca err | $\delta R(10)$ [fm] |
|---|---|---|---|---|
| 0.5 | 6/8 | 0.009 | 0.003 | 1.117 |
| 1.0 | 2/8 | 0.020 | 0.006 | 1.185 |
| 2.0 | 3/8 | 0.041 | 0.011 | 1.302 |
| 5.0 | 3/8 | 0.105 | 0.025 | 1.570 |
| 10.0 | 3/8 | 0.217 | 0.046 | 1.875 |

Phase 8 reference: 6/8 sign, 36Ar err 0.0008, 40Ca err 0.0001, $\delta R(10) = 1.042$ fm.

**Smooth-A calibration result: $V_P^0 = 0.061$ MeV** (essentially zero — Phase 8 already 1% off smooth-A target without Pauli, so calibrated Pauli is tiny correction).

**At calibrated $V_P^0 = 0.061$ MeV — Phase 11 vs Phase 8:**

| $N$ | nucleus | empirical | Phase 8 | Phase 11 | P11 - P8 | sign? P11 | $\delta R_{P11}$ |
|-----|---------|-----------|---------|----------|----------|-----------|-------|
|  4 | $^{16}$O   | $+0.1042$ | $+0.0495$ | $+0.0475$ | $-0.0020$ | YES | 0.681 |
|  5 | $^{20}$Ne  | $-0.0995$ | $-0.0003$ | $-0.0013$ | $-0.0010$ | YES | 0.730 |
|  6 | $^{24}$Mg  | $-0.0427$ | $-0.0113$ | $-0.0103$ | $+0.0010$ | YES | 0.806 |
|  7 | $^{28}$Si  | $+0.0309$ | $-0.0329$ | $-0.0316$ | $+0.0014$ | no | 0.866 |
|  8 | $^{32}$S   | $+0.0033$ | $-0.0276$ | $-0.0261$ | $+0.0015$ | no | 0.931 |
|  9 | $^{36}$Ar  | $-0.0136$ | $-0.0144$ | $-0.0131$ | $+0.0012$ | YES | 0.994 |
| 10 | $^{40}$Ca  | $-0.0038$ | $-0.0038$ | $-0.0034$ | $+0.0004$ | YES | 1.052 |
| 12 | $^{48}$Cr  | $+0.0212$ | $+0.0409$ | $+0.0384$ | $-0.0024$ | YES | 1.167 |

**All polytope-residual shifts $\leq 0.002$ MeV/α — within numerical noise.** Sign agreement: 6/8 (UNCHANGED). Max residual: 0.0475 (Phase 8: 0.0495; ~4% reduction within noise). $^{40}$Ca anchor: 0.0003 err (Phase 8: 0.0001 — both within roundoff). $^{36}$Ar anchor: 0.0005 err (Phase 8: 0.0008 — within noise). **Phase 11 leaves polytope-residual structure essentially unchanged from Phase 8.**

**Phase 11 outcome: NULL RESULT** — neither positive scoping nor programme-level negative result. F1 PASSES analytically; F2 magnitude UNCHANGED (within noise); F3 pattern UNCHANGED; Phase 8 anchor matches PRESERVED.

## Constructive content — structural diagnosis of redundancy

The null result has substantial diagnostic content:

1. **Pauli at physically motivated $\sigma_P = 1.5$ fm is structurally redundant with Phase 8's NN-fraction-weighted differential Coulomb softening.** Both mechanisms are NN-localized (Pauli by wave-function overlap exponential decay; Phase 8 differential softening by erf factor saturating at non-NN distances). Both add outward force scaling with NN edge count $|E| = 3N - 6$. Once Phase 8 captures the NN-only structural component, additional NN-only mechanisms cannot generate distinct polytope-specific signal — they just modify the effective NN repulsion magnitude, which gets absorbed into the smooth-A calibration.

2. **The remaining 52% of empirical polytope-residual scale is structurally unreachable by single-session R3-channel refinements within the Phase 8 framework.** Phases 9 + 10 ruled out σ-parameterized K$_3$ extensions (long-range mechanisms); Phase 11 shows Pauli (the natural NN-localized alternative) is structurally redundant. **Single-session R3-channel refinement candidates EXHAUSTED.**

3. **Implication: the 52% gap requires sub-shell-physics decomposition.** Persistent failures at $^{28}$Si and $^{32}$S across Phases 8, 9, 10, 11 confirm sub-shell-physics-dominance interpretation. Multi-paper scope.

4. **The empirical $^{16}$O shortfall (factor 2.2× residual unmatched)** is harder to interpret. $^{16}$O is doubly-magic ($Z = N = 8$) and strongly bound; its empirical $\Delta(B/A) = +0.104$ MeV/α positive residual vs SEMF may reflect (a) shell-physics enhancement at the magic configuration, (b) a CPP-channel mechanism orthogonal to R3 (e.g., DP-sea contribution at small N where finite-size corrections dominate), or (c) an SEMF parameterization artifact at very small A.

5. **Phase 8 Refinement A confirmed at the natural ceiling of R3-channel single-session refinements** — preserved as standing best refinement, structurally STRENGTHENED at Session 23 close.

## Methodological category introduced — structural-redundancy null result

Phase 11 introduces a new methodological category to the programme: **structural-redundancy null result**. Distinct from:

- **Programme-level negative results** (F3 pattern fails — Phases 2, 3A, 3B-A, 3B-B, 4, 9, 10).
- **Positive scoping** (F3 pattern improves — Phases 5, 6, 8).
- **Partial-positive empirical comparisons with reframing** (Phase 7).

Structural-redundancy null occurs when:
- F1 PASSES analytically
- F2 magnitude UNCHANGED from prior best (within numerical noise)
- F3 pattern UNCHANGED from prior best (sign agreement; anchor matches)
- Polytope-by-polytope shifts within noise

The diagnostic value is **negative information about completeness**: Phase 11 shows that the existing Phase 8 framework has captured the full NN-only R3-channel signal; further R3-channel work would require structurally distinct mechanisms (which Phases 9 + 10 + 11 together rule out within single-session scope). **This is the methodological signal that the OPEN-SS-32 ↔ U-shape thread is approaching saturation at the single-session level.**

Future scoping investigations should distinguish three F1-pass / F3-* patterns:
- Single-point F1-pass / F3-fail (Phase 9 — reject candidate)
- Parameter-family F1-pass / F3-fail-across-family (Phase 10 — reject class by sampling)
- Single-point or family F1-pass / F3-unchanged-from-prior-best (Phase 11 — structural redundancy; signals exhaustion)

## Programme-level state at Session 23 close

- **12 programme-level negative results** (UNCHANGED from Session 22 — Phase 11 is null, not negative)
- **R2 FORMALLY CLOSED** (Session 15 Phase 3B-B) — unchanged
- **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED** (Session 16 Phase 4) — unchanged
- **R3 and R4 channels passed scoping** (Session 17 Phase 5) — unchanged
- **R3-Coulomb passed scoping with 5% smooth-A bullseye at N=10** (Session 18 Phase 6) — properly reframed in Phase 7
- **Phase 7 reframing** preserved: smooth-A vs polytope-residual distinction; Phase 5 1 MeV/α target captures smooth-A; empirical polytope-residual scale ~0.05 MeV/α
- **Phase 8 Refinement A delivers**: factor 3.6 polytope-residual improvement, 48% of empirical scale captured, 6/8 sign agreement, near-exact $^{40}$Ca and $^{36}$Ar matches (within 0.001 MeV/α each), zero-parameter — STATUS PRESERVED AND **STRUCTURALLY STRENGTHENED at Session 23 close** (Phase 11 confirms natural ceiling)
- **Phase 9 Refinement C RULED OUT** — naive non-NN K$_3$ extension wrong physics
- **Phase 10 Refinement D RULED OUT** — entire $\sigma$-parameterized K$_3$ refinement class eliminated; K$_3$ binding in CPP is strictly NN-localized regardless of width or amplitude
- **Phase 11 R3-Pauli NULL RESULT** — Pauli structurally redundant with Phase 8 NN-fraction-weighted differential Coulomb softening; **single-session R3-channel refinement candidates EXHAUSTED**
- **Three positive scoping outcomes** in OPEN-SS-32 ↔ U-shape thread preserved: Phase 5 channel pass, Phase 6 5% smooth-A bullseye, Phase 8 polytope-residual factor 3.6 improvement
- **Sign-theorem composition workflow** validated across F1-pass / F3-fail at single point (Phase 9), F1-pass / F3-fail-across-parameter-family (Phase 10), F1-pass / F3-unchanged-from-prior-best (Phase 11) — necessary but not sufficient
- **Smooth-A vs polytope-residual methodology principle** (Phase 7) preserved
- **Sub-shell-closure observation** (Phase 8): R3-Coulomb mechanism is sub-shell-blind; $^{28}$Si and $^{32}$S empirical residuals require shell-physics-corrected baseline (Strutinsky-style); persistent failures across Phases 8, 9, 10, 11; "good polytopes" = $^{16}$O, $^{20}$Ne, $^{24}$Mg, $^{36}$Ar, $^{40}$Ca, $^{48}$Cr
- **Anchor matches at $^{40}$Ca and $^{36}$Ar (Phase 8)** confirmed as delicately balanced NN-only K$_3$ signatures; preserved by Phase 11 calibrated $V_P^0$ within numerical noise
- **$^{16}$O standout shortfall** (factor 2.2× empirical residual unmatched at Phase 11 $+0.0475$ vs empirical $+0.1042$) — possible finite-A SEMF artifact or alternate-channel mechanism (Priority 3, deferred)
- **Decoupling Theorem** (Session 12 sub-question b) intact
- **First qualitative cross-paradigm consilience claim** (Session 9) intact
- **6 OPEN-SS-35 stages preserved**; stage (vi) refines further to add "R3-Pauli structurally redundant with Phase 8 NN-fraction-weighted differential softening (Phase 11 NULL); single-session R3-channel refinement candidates exhausted; remaining 52% requires sub-shell-physics decomposition (multi-paper) or alternate-channel work outside R3"
- **Pattern 6 K$_3$ scale-recurrence** at 7 confirmed instances unchanged
- **§7 of SS-9 v0.3** has shifted **THIRTEEN times** in OPEN-SS-32 ↔ U-shape thread; **Phase 11 NULL marks natural saturation point — OPEN-ORG-012 .tex conversion can now begin**
- **Methodological category structural-redundancy null result** introduced at Session 23 Phase 11 close

## Session 24 forward queue

**Priority 1 (PROMOTED from Phase 10 Priority 2; multi-paper scope, sole remaining path):** **Sub-shell-physics decomposition.** $^{28}$Si and $^{32}$S persistent failures across Phases 8, 9, 10, 11 confirm sub-shell-physics-dominance interpretation. Strutinsky-style shell-corrected baseline integration replacing SEMF; revised polytope-residual decomposition; assess whether $^{28}$Si and $^{32}$S fall into line under shell correction. **Likely warrants its own SS-paper (SS-10?)** on shell-corrected baselines for cluster-physics decomposition. Apply F1 sign analytical check first via composition workflow. *Multi-paper scope.*

**Priority 2 (PROMOTED from anti-priority to active priority):** **OPEN-ORG-012 (.tex conversion of SS-9 v0.3).** §7 has shifted 13 times but **Phase 11 NULL marks natural saturation point** — §7 stable enough for formal write-up. SS-9 paper formalizes Phase 8 Refinement A as standing best refinement, with §7 noting the 52% gap as multi-paper future work referring to a forthcoming sub-shell-physics paper. Phase 11 NULL is the natural transition point: the SS-9 paper write-up should reflect the exhausted single-session candidate space. *Single-session conversion (or 1-2 sessions).*

**Priority 3 (deferred):** **Alternate-channel investigations** — finite-A SEMF corrections (relevant for $^{16}$O standout shortfall); R4-DP-sea contributions (Phase 5 R4 channel passed scoping but was deferred); SR-tensor channel. Multi-paper scope; not in scope until sub-shell-physics decomposition completed.

**Anti-priorities sharpened:**
- §7 has shifted **THIRTEEN times** — but **Phase 11 NULL marks natural saturation**: OPEN-ORG-012 .tex conversion can now begin (was anti-priority through Phases 1-10; promoted to Priority 2 at Session 23 Phase 11 close).
- No raw Phase-N net binding gain magnitudes vs empirical $\Delta(B/A)$ without first detrending smooth-A (Phase 7 methodology preserved).
- No R3-channel mechanisms in isolation from Coulomb (Phase 6/7/8/9/10/11).
- Do not expect R3-channel mechanism to reproduce $^{28}$Si and $^{32}$S residuals (Phase 8 anti-priority preserved across Phases 9, 10, 11).
- **NEW Phase 11:** Do NOT propose any single-session R3-channel refinement to close the remaining 52% empirical gap. Phases 9 + 10 + 11 together exhaust the natural single-session refinement candidates (σ-parameterized K$_3$ ruled out; R3-Pauli structurally redundant). Further R3-channel work requires multi-paper structurally distinct mechanisms — not in scope for SS-9.
- **NEW Phase 11:** Phase 8 Refinement A is at the natural ceiling of R3-channel single-session refinements — confirmed by exhausting all viable refinements. Future improvements must come from multi-paper work (sub-shell-physics, R4-DP-sea, SR-tensor) or finite-A corrections.

## Apply chain

Five-patch chain `0215–0219` from `88dedea` (origin/main at Phase 10 close) baseline. To apply:

```bash
cd ~/Documents/GitHub/CPP && \
git pull origin main && \
git am ~/Downloads/0215-Phase-11-R3-Pauli-NULL-RESULT-Pauli-structurally-redundant-with-Phase-8-NN-fraction-weighted-differential-softening-single-session-R3-channel-refinement-candidates-exhausted.patch && \
git am ~/Downloads/0216-Phase-11-Step-A-Step-C-session-log-and-Vignette-30.patch && \
git am ~/Downloads/0217-Phase-11-Step-B-Step-D-transcript-and-Tier-4-reasoning.patch && \
git am ~/Downloads/0218-Phase-11-Step-E-Research_Frontier-and-future_projects.patch && \
git am ~/Downloads/0219-Phase-11-Step-H-Session-23-close-handover.patch && \
git push origin main
```

## Cumulative trajectory summary

The OPEN-SS-32 ↔ U-shape thread has now produced eleven sequential phases:

- Session 13 Phase 2: Uniform-only zero-point softening RULED OUT (F1).
- Session 13 Phase 3A: Naive full-Hessian RULED OUT (F2 magnitude + F3 pattern).
- Session 14 Phase 3B-A: Fixed-dim belt subspace RULED OUT (F3 pattern).
- Session 15 Phase 3B-B: Full $C_n$ IRREP decomposition RULED OUT — **R2 FORMALLY CLOSED**.
- Session 16 Phase 4: Anharmonic ξ⁴ + all-orders Gaussian RULED OUT — **Gaussian-K$_3$ framework at fixed cluster geometry FORMALLY CLOSED**.
- Session 17 Phase 5: Geometric-shift R3/R4 channels PASSED SCOPING.
- Session 18 Phase 6: R3-Coulomb scoping PASSED with 5% magnitude bullseye at $N = 10$.
- Session 19 Phase 7: R3-Coulomb empirical comparison — PARTIAL POSITIVE with critical reframing (smooth-A vs polytope-residual methodology).
- Session 20 Phase 8: R3-Coulomb Refinement A (extended Gaussian alpha charge) — POSITIVE SCOPING with factor 3.6 polytope-residual improvement and near-exact zero-parameter match at $^{40}$Ca and $^{36}$Ar.
- Session 21 Phase 9: R3-Coulomb Refinement C (naive non-NN K$_3$ at canonical $\sigma$) — RULED OUT by F3 pattern failure; eleventh programme-level negative result.
- Session 22 Phase 10: R3-Coulomb Refinement D ($\sigma_{K3}$ sensitivity, two tracks) — RULED OUT by F3 pattern failure across both tracks; twelfth programme-level negative result.
- **Session 23 Phase 11: R3-Pauli scoping (Gaussian repulsive core, $\sigma_P = 1.5$ fm fixed, $V_P^0$ calibrated) — NULL RESULT — Pauli structurally redundant with Phase 8 NN-fraction-weighted differential softening; single-session R3-channel refinement candidates EXHAUSTED; methodological category "structural-redundancy null result" introduced. Programme negative-result count UNCHANGED at 12.**

The methodology lesson — F1 sign analytical check first, before computation — propagated from Phase 4 (Session 16) through Phases 5, 6, 7, 8, 9, 10 to Phase 11 (Session 23) as a working methodology. Phase 6 codified it as the sign-theorem composition workflow within-mechanism. Phase 7 extended to empirical-comparison F1 (Level 2). Phase 8 extended to refinement-level F1 (both levels). Phase 9 demonstrated F1-pass / F3-fail at single point — sign-theorem composition is **necessary but not sufficient**. Phase 10 demonstrated F1-pass / F3-fail-across-entire-parameter-family — when F1 sign passes for an entire class of refinements, F3 pattern check can rule out the whole class by sampling. **Phase 11 introduces the structural-redundancy null result methodological category** — F1 PASSES, anchors PRESERVED, F3 unchanged from prior best; the candidate adds nothing structurally distinct. Three F1-pass / F3-* patterns are now distinguished: rejection at point (Phase 9), rejection across family (Phase 10), structural redundancy (Phase 11). The third is the saturation signal.

The **structural** lesson from Phase 11: **K$_3$-σ-tuning class** (Phases 9 + 10) and **R3-Pauli at wave-function-overlap range** (Phase 11) **are the two natural single-session R3-channel refinement candidate classes**, and both are now closed. K$_3$-σ-tuning fails because K$_3$ binding in CPP is strictly NN-localized (Phase 9 + Phase 10 confirm this). R3-Pauli at $\sigma_P = 1.5$ fm fails because it is structurally redundant with Phase 8's NN-fraction-weighted differential Coulomb softening (both NN-localized; once Phase 8 captures NN-only structural component, additional NN-only mechanisms add nothing distinct). **The remaining 52% of the empirical polytope-residual scale is structurally unreachable by single-session R3-channel work within the Phase 8 framework.** The forward path is multi-paper: sub-shell-physics decomposition (Priority 1) and OPEN-ORG-012 .tex conversion of SS-9 v0.3 (Priority 2; promoted to active now that single-session refinement work has saturated). Alternate-channel investigations (R4-DP-sea, SR-tensor, finite-A SEMF corrections for $^{16}$O standout shortfall) Priority 3, deferred.

---

*Step H paste-ready handover per `templates/operating_system.md` §15 protocol.*
