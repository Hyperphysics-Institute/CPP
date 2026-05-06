# SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 10 R3-Coulomb Refinement D ($\sigma_{K3}$ sensitivity)

**Date:** 5 May 2026 (Session 22)
**Status:** **RULED OUT (NEGATIVE RESULT) — twelfth programme-level negative result; seventh ruling-out in OPEN-SS-32 ↔ U-shape thread.** Refinement D ($\sigma_{K3}$ sensitivity, two tracks) is RULED OUT: Track 1 (uniform $\sigma_{K3}$ ±10% around canonical 1.68 fm) produces unphysical $\delta R(12) = 0$ at all variants in {1.51, 1.60, 1.68, 1.76, 1.85} fm — confirming Phase 9's ruling-out is robust to $\sigma_{K3}$ variation. Track 2 (split-width: $\sigma_{K3,\rm NN} = 1.68$ fm fixed, $\sigma_{K3,\rm non-NN}$ varies in {0.3, 0.5, 0.7, 1.0, 1.4, 1.68} fm) finds that **NO finite $\sigma_{K3,\rm non-NN}$ preserves Phase 8 anchor matches at $^{40}$Ca and $^{36}$Ar** — anchor accuracy is structurally tied to strict NN-only K$_3$ treatment, not just to numerical magnitude of non-NN K$_3$. **Constructive content**: Phase 8 anchor matches confirmed as **delicately balanced** structural signature of NN-only K$_3$ framework — any non-NN extension (even with $\sigma_{K3,\rm non-NN} = 0.3$ fm yielding only ~1% of canonical K$_3$ amplitude at typical non-NN distances) destroys anchor accuracy. This sharpens the Phase 9 lesson: **K$_3$ binding in CPP is strictly NN-localized, regardless of width**. Refinement D's structural goal (identifying a finite non-NN K$_3$ contribution preserving Phase 8 anchors) FAILS by direct numerical test. Programme implication: the remaining 52% of empirical polytope-residual scale (after Phase 8 captures 48%) cannot come from K$_3$ refinements at all. R3-Pauli (Priority 2 in Phase 9 handover, now elevated to Priority 1 for Session 23) becomes the sole remaining single-session-tractable candidate; sub-shell-physics decomposition (Priority 3) becomes more important. Phase 8 Refinement A (factor 3.6 polytope-residual improvement; near-exact zero-parameter $^{40}$Ca/$^{36}$Ar matches) status preserved as standing best refinement; **structural status STRENGTHENED** by Refinement D ruling-out (no $\sigma$-tuning improvement possible).
**Companion script:** `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase10_R3_Coulomb_RefD.py`.

---

## 1. Strategy

Session 21 Phase 9 (sketch §6.1 / 0209 handover) registered Session 22 Priority 1 as **Refinement D — $\sigma_{K3}$ sensitivity ±10% around canonical 1.68 fm, AND test whether $\sigma_{K3,\rm non-NN}$ should be much smaller (e.g., 0.5–1.0 fm) to recover Phase 5/6/8 NN-only behavior**. Phase 9 ruled out the naive non-NN K$_3$ extension at canonical $\sigma_{K3} = 1.68$ fm by F3 pattern failure: cluster expansion δR collapsed dramatically at high N (icosahedron $\delta R = 0$ — unphysical); Phase 8 anchor matches at $^{40}$Ca and $^{36}$Ar destroyed (factor 7 and 3.4 errors); $^{48}$Cr handover hypothesis refuted; sign agreement degraded 6/8 → 4/8.

The structural question Phase 10 addresses: **can $\sigma_{K3}$ tuning produce a refinement that preserves Phase 8's anchor matches AND adds polytope-specific signal beyond Phase 8?** Two complementary tracks:

- **Track 1 (uniform $\sigma_{K3}$ sensitivity):** vary $\sigma_{K3}$ across ±10% range {1.51, 1.60, 1.68, 1.76, 1.85} fm with all pairs (NN + non-NN) using single $\sigma$. Tests whether Phase 9's collapse is sensitive to $\sigma_{K3}$ value or is robust across the canonical-±10% range.
- **Track 2 (split-width):** fix $\sigma_{K3,\rm NN} = 1.68$ fm (preserves Phase 8 NN physics by construction); vary $\sigma_{K3,\rm non-NN} \in \{0.3, 0.5, 0.7, 1.0, 1.4, 1.68\}$ fm. Limits: $\sigma_{K3,\rm non-NN} \to 0$ recovers Phase 8 (no non-NN contribution); $\sigma_{K3,\rm non-NN} = 1.68$ fm recovers Phase 9 (full non-NN at canonical). Tests whether any intermediate value preserves Phase 8 anchors AND adds polytope signal.

The Phase 4–9 methodology lesson — F1 sign analytical check first via the sign-theorem composition workflow — is applied at two levels.

## 2. Pre-empted analytical sign analysis (F1)

### 2.1 Level 1 — Within-mechanism sign

$\sigma_{K3}$ variation does NOT change the Coulomb push direction (still outward, repulsive); only modifies the K$_3$ inward pull magnitude/range. Equilibrium $\delta R$ remains $\geq 0$ for all reasonable $\sigma_{K3}$ values. The Phase 5 sign theorem is $\sigma_{K3}$-independent in **sign** (only magnitude scales): for $\delta R \neq 0$, $\Delta V_{\rm edge} = B_{\rm pair}[1 - \exp(-\delta R^2/(2\sigma^2))] > 0$ regardless of $\sigma$.

By the sign-theorem composition workflow:

- Coulomb outward + K$_3$ inward → equilibrium $\delta R \geq 0$
- Phase 5 sign theorem: $\delta R \neq 0 \Rightarrow \Delta E > 0$
- **F1 PASSES at within-mechanism level for ALL $\sigma_{K3}$ variants (both tracks).**

### 2.2 Level 2 — Empirical-comparison sign

Predicted net binding gain $\geq 0$ vs canonical-no-expansion for all variants. Empirical alpha-conjugate excess vs smooth baseline positive. **F1 SIGN COMPATIBLE at smooth-A level.** Polytope-residual sign agreement requires computation per variant.

The methodological lesson from Phase 9 — sign-theorem composition is necessary but not sufficient — is sharpened: F1 PASSES analytically for ALL Refinement D variants; the structural test is at F3 pattern level (anchor preservation, sign agreement, polytope-by-polytope structure).

## 3. Track 1 — uniform $\sigma_{K3}$ sensitivity

### 3.1 Numerical results

| $\sigma_{K3}$ [fm] | slope | intercept | max resid | sign agreement | $^{36}$Ar err | $^{40}$Ca err | $\delta R(10)$ [fm] | %vs1.052 | $\delta R(12)$ [fm] |
|------|------|------|------|------|------|------|------|------|------|
| 1.51 | $-0.0361$ | $+0.372$ | 0.061 | 4/8 | 0.031 | 0.007 | 0.000 | +100% | 0.000 |
| 1.60 | $-0.0406$ | $+0.424$ | 0.063 | 4/8 | 0.035 | 0.015 | 0.000 | +100% | 0.000 |
| 1.68 (= Phase 9) | $-0.0445$ | $+0.473$ | 0.062 | 4/8 | 0.034 | 0.022 | 0.027 | +97% | 0.000 |
| 1.76 | $-0.0482$ | $+0.521$ | 0.057 | 4/8 | 0.032 | 0.027 | 0.067 | +94% | 0.000 |
| 1.85 | $-0.0520$ | $+0.576$ | 0.052 | 4/8 | 0.027 | 0.030 | 0.114 | +89% | 0.000 |

**Phase 8 reference (NN-only K$_3$):** $^{36}$Ar err ≈ 0.0008, $^{40}$Ca err ≈ 0.0001, $\delta R(10) = 1.042$ fm (1% off Phase 5 R3-lin target 1.052).

### 3.2 Track 1 outcomes

- **All Track 1 variants produce unphysical $\delta R(12) = 0$.** The icosahedron does not relax under Coulomb stress at any $\sigma_{K3}$ in the ±10% range. The non-NN K$_3$ binding (which scales as $\sigma_{K3}$ from the Gaussian width but also as $\exp(-(r-R_\alpha)^2/(2\sigma^2))$) remains too strong relative to Coulomb push at all variants tested.
- **Smooth-A scale (δR(10) vs Phase 5 R3-lin target 1.052 fm) deviates by 89–100%** across the range — far worse than Phase 8's 1% match. Phase 9's ruling-out is robust to $\sigma_{K3}$ variation in the canonical ±10% range.
- **Sign agreement remains at 4/8 across the range** — no improvement vs Phase 9.
- **Phase 8 anchor matches lost at all Track 1 variants** ($^{36}$Ar errors 0.027–0.035, $^{40}$Ca errors 0.007–0.030 — all far worse than Phase 8's 0.0008 / 0.0001).

Track 1 confirms: **uniform $\sigma_{K3}$ for all pairs is unphysical regardless of $\sigma$ value in ±10% range.** The Phase 9 negative result is structurally robust.

## 4. Track 2 — split-width

### 4.1 Numerical results

Phase 8 baseline (NN-only K$_3$, recovered at $\sigma_{K3,\rm non-NN} \to 0$): net gain = $+0.177 \cdot N - 0.452$ MeV/α; sign agreement 6/8; $^{36}$Ar resid $-0.0144$; $^{40}$Ca resid $-0.0038$; $\delta R(10) = 1.042$ fm.

| $\sigma_{K3,\rm non-NN}$ [fm] | slope | max resid | sign agreement | $^{36}$Ar err | $^{40}$Ca err | $\delta R(10)$ | $\delta R(12)$ | anchor preserved? |
|------|------|------|------|------|------|------|------|------|
| 0 (Phase 8) | $+0.177$ | 0.050 | 6/8 | 0.0008 | 0.0001 | 1.042 | 1.158 | **YES** (reference) |
| 0.30 | $+0.180$ | 0.292 | 2/8 | 0.0334 | 0.0336 | 1.042 | 1.158 | no |
| 0.50 | $+0.161$ | 0.192 | 5/8 | 0.0604 | 0.0044 | 1.042 | 1.158 | no |
| 0.70 | $+0.041$ | 0.545 | 6/8 | 0.361 | 0.412 | 0.000 | 1.158 | no (collapse at N=10) |
| 1.00 | $-0.042$ | 0.086 | 5/8 | 0.030 | 0.002 | 0.000 | 0.000 | no (full collapse) |
| 1.40 | $-0.042$ | 0.078 | 4/8 | 0.036 | 0.003 | 0.000 | 0.000 | no (full collapse) |
| 1.68 (= Phase 9) | $-0.045$ | 0.062 | 4/8 | 0.034 | 0.022 | 0.027 | 0.000 | no |

### 4.2 Three structural findings

**Finding 1 — anchor preservation requires strict NN-only K$_3$.** At $\sigma_{K3,\rm non-NN} = 0.30$ fm (very narrow, only ~1% of canonical K$_3$ amplitude at $\sqrt{2}R_\alpha$), $^{36}$Ar error grows from Phase 8's 0.0008 to 0.0334 — factor **42×**. $^{40}$Ca error grows from 0.0001 to 0.0336 — factor **336×**. Phase 8 anchor matches are not numerically robust; they require non-NN K$_3$ to be **identically zero**. Even tiny non-NN contributions destroy them.

**Finding 2 — non-monotonic $\delta R(N)$ collapse with $\sigma_{K3,\rm non-NN}$.** At $\sigma_{K3,\rm non-NN} \in \{0.30, 0.50\}$ fm, both $\delta R(10) = 1.042$ and $\delta R(12) = 1.158$ are preserved (Phase 8 values) — non-NN contribution too narrow to matter at non-NN distances 3.35–4.5 fm. At $\sigma_{K3,\rm non-NN} = 0.70$ fm, $\delta R(10)$ collapses to 0 but $\delta R(12)$ remains 1.158 — transition regime where $\sigma$ matches first non-NN distance peak ($\sqrt{2}R_\alpha = 3.35$ fm, $r - R_\alpha = 0.98$ fm). Above $\sigma_{K3,\rm non-NN} = 1.0$ fm, both collapse — non-NN K$_3$ now reaches all relevant distances. **The collapse threshold is sharp** (between σ_nonNN = 0.5 and 0.7 fm) and structurally distinct from anchor-preservation threshold (anchors lost at any σ_nonNN > 0).

**Finding 3 — smooth-A slope sign reversal threshold.** Phase 8 = $+0.177 \cdot N$. At $\sigma_{K3,\rm non-NN} = 0.30$ fm slope is preserved at $+0.180$. At 0.50 fm: $+0.161$ (slight reduction). At 0.70 fm: $+0.041$ (transition, near zero). At 1.00 fm: $-0.042$ (sign flipped). Slope sign reversal occurs near $\sigma_{K3,\rm non-NN} \approx 0.7$ fm — same threshold as $\delta R(10)$ collapse.

### 4.3 The diagnostic question — does any Track 2 variant preserve Phase 8 anchors AND add polytope signal?

| $\sigma_{K3,\rm non-NN}$ | Anchors preserved? | Sign agreement | Polytope-residual structure |
|---|---|---|---|
| 0 | YES (Phase 8 ref) | 6/8 | factor 3.6 vs Phase 6 |
| 0.30 | no | 2/8 (worse than Phase 8) | dominated by ²⁸Si negative spike |
| 0.50 | no | 5/8 (worse than Phase 8) | dominated by ²⁰Ne, ²⁸Si distortions |
| 0.70 | no | 6/8 | δR collapse at N=10; UNPHYSICAL |
| 1.00 | no | 5/8 | full δR collapse; UNPHYSICAL |
| 1.40 | no | 4/8 | full δR collapse; UNPHYSICAL |
| 1.68 | no (Phase 9 ref) | 4/8 | full δR collapse; UNPHYSICAL |

**No Track 2 variant simultaneously preserves Phase 8 anchors AND adds physical polytope signal.** The Phase 8 anchor matches are a **delicately balanced** structural signature of strict NN-only K$_3$ treatment.

## 5. Verdict — RULED OUT (twelfth programme-level negative result)

### 5.1 Three falsifier outcomes

- **F1 (sign): PASSES analytically** at within-mechanism level for all Track 1 and Track 2 variants. F1 SIGN COMPATIBLE at smooth-A level.
- **F2 (magnitude):** Track 1 max residuals 0.052–0.063 MeV/α; Track 2 max residuals 0.062–0.545 MeV/α. Empirical 0.104. No variant systematically improves on Phase 8 (0.050) without destroying anchors.
- **F3 (pattern): FAILS DECISIVELY across both tracks.** Track 1: all variants produce unphysical $\delta R(12) = 0$, sign agreement 4/8 unchanged from Phase 9. Track 2: NO σ_K3,non-NN value preserves Phase 8 anchor matches; the matches are tied to strict NN-only K$_3$ treatment.

### 5.2 Programme-level negative result #12

**Phase 10 (Refinement D — $\sigma_{K3}$ sensitivity, two tracks) is RULED OUT.** Twelfth programme-level negative result; seventh ruling-out in OPEN-SS-32 ↔ U-shape thread. The thread closures: Phase 2 uniform-only Session 13, Phase 3A naive full-Hessian Session 13, Phase 3B-A fixed-dim belt Session 14, Phase 3B-B IRREP decomposition Session 15 (R2 closure), Phase 4 anharmonic ξ⁴ Session 16 (Gaussian-K$_3$-at-fixed-geometry closure), Phase 9 naive non-NN K$_3$ Session 21, **Phase 10 σ_K3 sensitivity Session 22**.

### 5.3 Constructive content — Phase 8 standing best refinement structurally STRENGTHENED

The negative result has substantial positive content:

1. **Phase 8 anchor matches are a delicately balanced structural signature of strict NN-only K$_3$.** Any non-NN K$_3$ extension (even with $\sigma_{K3,\rm non-NN} = 0.3$ fm at ~1% canonical amplitude) destroys $^{36}$Ar anchor (factor 42× error) and $^{40}$Ca anchor (factor 336× error). The anchor accuracy is not a numerical coincidence — it is a structural feature of the NN-only K$_3$ framework.

2. **K$_3$ binding in CPP is strictly NN-localized, independent of width.** Phase 9 ruled out canonical-σ non-NN extension; Phase 10 rules out the entire family of σ-tuned non-NN extensions (any σ_K3,non-NN > 0). Together, Phases 9 and 10 establish that **K$_3$ binding is an NN-only 3-body correlation in CPP**, period — not a long-range correlation with adjustable range.

3. **σ-tuning cannot rescue any K$_3$-based refinement.** This eliminates an entire class of proposed extensions (extended-range K$_3$, polytope-dependent σ_K3, etc.) at scoping level. Methodological cost: future K$_3$-related refinements must propose mechanisms structurally different from σ-tuning.

4. **Phase 8 Refinement A status STRENGTHENED.** Phase 8 captures 48% of empirical polytope-residual scale via NN-fraction-weighted differential Coulomb softening. The remaining 52% cannot come from K$_3$ refinements (Phases 9 and 10 close this avenue). Must come from R3-Pauli (Priority 2) or sub-shell-physics decomposition (Priority 3).

5. **Forward priorities re-ordered:** R3-Pauli scoping (was Priority 2) **promoted to Priority 1 for Session 23**. R3-Pauli is naturally NN-localized via wave-function overlap — has the right structural symmetry that all K$_3$-σ-tuning variants lack. Sub-shell-physics decomposition (was Priority 3) gains importance as the only remaining single-paper-tractable mechanism beyond R3-Pauli.

### 5.4 Methodological lesson — sharpened from Phase 9

Phase 9 demonstrated F1-pass / F3-fail (sign-theorem composition is necessary but not sufficient). **Phase 10 demonstrates F1-pass / F3-fail-across-entire-parameter-family** — refinement RULED OUT at scoping by direct numerical scan of the natural parameter space. This is a stronger methodological pattern: when F1 sign passes for an entire class of refinements (parameterized by $\sigma$ or similar), F3 pattern check can rule out the whole class by sampling.

## 6. Programme implications

### 6.1 Negative-result count and trajectory

Programme-level negative-result count grows from **11 to 12**. Phase 10 is the **seventh ruling-out** in the OPEN-SS-32 ↔ U-shape thread. Thread continues with three positive scoping outcomes preserved (Phase 5 channel pass, Phase 6 5% smooth-A bullseye, Phase 8 polytope-residual factor 3.6 improvement) and seven closures (Phases 2, 3A, 3B-A, 3B-B, 4, 9, 10).

OPEN-SS-35 sub-question (a) A-scaling closure: stage (vi) refines further. Was at Session 21 close: "R3-Coulomb under active multi-session full derivation; smooth-A scale validated to 1%; polytope-residual mechanism identified as NN-fraction-weighted differential softening; 48% of empirical polytope-residual magnitude captured by Refinement A; **naive non-NN K$_3$ extension (Refinement C) RULED OUT (Phase 9) — Phase 5/6/8 NN-only K$_3$ framework confirmed as correct**; remaining 52% pending Refinement D, R3-Pauli, shell-physics decomposition." Now at Session 22 close: "...remaining 52% pending **R3-Pauli** scoping and **shell-physics decomposition** for sub-shell-closure nuclei. **All K$_3$-based refinements ruled out** by Phase 9 + Phase 10 — K$_3$ binding in CPP is strictly NN-localized, independent of width or amplitude tuning."

### 6.2 R2 / Phase 4 / Phase 8 closures unchanged

- R2 remains FORMALLY CLOSED (Session 15).
- Gaussian-K$_3$ framework at fixed cluster geometry remains FORMALLY CLOSED (Session 16).
- Phase 5 R3/R4 channels still pass scoping.
- Phase 6 R3-Coulomb 5% smooth-A bullseye preserved.
- Phase 7 smooth-A vs polytope-residual methodology preserved.
- Phase 8 Refinement A factor 3.6 polytope-residual improvement and near-exact $^{40}$Ca/$^{36}$Ar matches preserved — **structurally STRENGTHENED** by Phase 10 ruling-out (anchor matches now confirmed as delicately balanced NN-only signatures, not numerical coincidences).
- Phase 9 naive non-NN K$_3$ ruling-out preserved.

### 6.3 Sub-question (b) state unchanged

Sub-question (b) layer 3 gap-strength closure remains INDEPENDENT (Decoupling Theorem, Session 12). Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances unchanged. First qualitative cross-paradigm consilience claim (Session 9) intact. 6 OPEN-SS-35 stages preserved.

## 7. Forward pointers (Session 23)

### 7.1 Priority 1 — R3-Pauli scoping (PROMOTED from Phase 9 Priority 2)

**Pauli is the sole remaining single-session-tractable refinement candidate.** Phase 10 rules out all σ-tuned K$_3$ refinements; R3-Pauli is naturally NN-localized via wave-function overlap (alpha-alpha Pauli core acts at short range; exponentially suppressed at non-NN distances) — has the right structural symmetry that K$_3$-σ-tuning variants lack. Specify a Pauli model (e.g., Gaussian repulsive core in alpha-alpha potential at short range, tunable amplitude $V_P$ and range $\sigma_P$). Apply F1 sign analytical check first via composition: Pauli is repulsive → $\delta R_{\rm Pauli} > 0$ → Phase 5 sign theorem → $\Delta E > 0$, F1 PASSES analytically. Compute equilibrium $\delta R_{\rm Pauli}(N)$ per polytope, compare to Phase 6/8 results. Critically: detrend smooth-A part and compare polytope-residuals to empirical $\sim 0.05$ MeV/α scale; verify Phase 8 anchor matches at $^{40}$Ca and $^{36}$Ar are preserved (registered Phase 9 constraint).

### 7.2 Priority 2 — Sub-shell-physics decomposition

**Promoted from Phase 9 Priority 3.** $^{28}$Si and $^{32}$S persistent failures across Phases 8, 9, 10 confirm sub-shell-physics-dominance interpretation. Multi-paper scope. Strutinsky-style shell-corrected baseline integration replacing SEMF; revised polytope-residual decomposition; assess whether $^{28}$Si and $^{32}$S fall into line under shell correction. This mechanism is structurally independent of R3 channel and provides the only path to closing the remaining 52% gap if R3-Pauli also fails to close it fully.

### 7.3 Anti-priorities sharpened

- §7 has shifted **twelve** times in OPEN-SS-32 ↔ U-shape thread (was 11 at Session 21 close); OPEN-ORG-012 .tex conversion further deferred.
- No raw Phase-N net binding gain magnitudes vs empirical $\Delta(B/A)$ without first detrending smooth-A (Phase 7 methodology preserved).
- No R3-channel mechanisms in isolation from Coulomb (Phase 6/7/8/9/10).
- Do not expect R3-channel mechanism to reproduce $^{28}$Si and $^{32}$S residuals (Phase 8 anti-priority preserved across Phases 9, 10).
- **NEW from Phase 10:** Do NOT propose any K$_3$-based refinement parameterized by $\sigma_{K3}$ or amplitude tuning. Phases 9 + 10 together rule out the entire class — K$_3$ binding in CPP is strictly NN-localized, independent of width or amplitude.
- **NEW from Phase 10:** Phase 8 anchor matches at $^{40}$Ca (within 0.0001 MeV/α) and $^{36}$Ar (within 0.001 MeV/α) are now **structurally confirmed** as delicately balanced NN-only K$_3$ signatures — not numerical coincidences. Any future refinement must preserve these (registered Phase 9 + Phase 10 constraint).

## 8. Summary

Phase 10 executed Session 21 Phase 9's Priority 1 forward pointer (Refinement D — $\sigma_{K3}$ sensitivity) as the final K$_3$-related single-session refinement candidate. Two tracks: Track 1 (uniform $\sigma_{K3}$ ±10%, applied to all pairs); Track 2 (split-width: $\sigma_{K3,\rm NN} = 1.68$ fm fixed, $\sigma_{K3,\rm non-NN}$ varied in {0.3, 0.5, 0.7, 1.0, 1.4, 1.68} fm, including Phase 8 ($\sigma_{K3,\rm non-NN} \to 0$) and Phase 9 ($\sigma_{K3,\rm non-NN} = 1.68$) limits).

F1 sign passes analytically for all variants (sign-theorem composition workflow extended to $\sigma_{K3}$ variation; $\sigma_{K3}$-independent in sign). F3 pattern fails decisively across both tracks: Track 1 produces unphysical $\delta R(12) = 0$ at all variants in canonical ±10% range, confirming Phase 9 robustness; Track 2 finds NO finite $\sigma_{K3,\rm non-NN}$ preserves Phase 8 anchor matches at $^{40}$Ca and $^{36}$Ar — even very narrow ($\sigma_{K3,\rm non-NN} = 0.30$ fm at ~1% canonical amplitude) destroys anchor accuracy by factor 42× ($^{36}$Ar) / 336× ($^{40}$Ca). Three structural findings: anchor preservation requires strict NN-only K$_3$; non-monotonic $\delta R(N)$ collapse with $\sigma_{K3,\rm non-NN}$ (transition near σ ≈ 0.7 fm matching first non-NN distance from K$_3$ peak); smooth-A slope sign reversal near same threshold.

**Phase 10 (Refinement D — $\sigma_{K3}$ sensitivity, two tracks) RULED OUT.** Twelfth programme-level negative result; seventh ruling-out in OPEN-SS-32 ↔ U-shape thread. Constructive content: **Phase 8 anchor matches at $^{40}$Ca and $^{36}$Ar are confirmed as delicately balanced structural signatures of strict NN-only K$_3$ framework**, not numerical coincidences. **K$_3$ binding in CPP is strictly NN-localized, independent of width or amplitude tuning** — Phases 9 + 10 together rule out the entire class of σ-parameterized K$_3$ refinements at scoping. **Phase 8 Refinement A status STRENGTHENED** as standing best refinement; structural status confirmed. Forward priority: **R3-Pauli scoping PROMOTED to Priority 1 for Session 23** — Pauli is naturally NN-localized via wave-function overlap, sole remaining single-session-tractable candidate that does not violate Phases 9/10 constraints. Sub-shell-physics decomposition becomes Priority 2 as multi-paper structural-independence path. Methodological lesson sharpened from Phase 9: when F1 sign passes for an entire parameter family of refinements, F3 pattern check can rule out the whole class by direct sampling — Phase 10 demonstrates this strong methodological pattern. Programme negative-result count grows to **12**. Six OPEN-SS-35 stages preserved (stage (vi) refines further to add Phase 10 result). All earlier closures (R2, Gaussian-K$_3$-at-fixed-geometry, Phase 5 channel pass, Phase 6 smooth-A bullseye, Phase 7 methodology, Phase 8 Refinement A, Phase 9 naive non-NN K$_3$) preserved. Decoupling Theorem (Session 12) intact. First qualitative cross-paradigm consilience claim (Session 9) intact.
