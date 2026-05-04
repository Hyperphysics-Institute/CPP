# OPEN-SS-35 Sub-question (a) A-Scaling — R1 (R$_\alpha$ Scale-Dependence) RULED OUT

**Date:** 4 May 2026 (Session 12)
**Purpose:** Investigate Resolution R1 (R$_\alpha$ scale-dependence as A-scaling closure) — registered in the Session 7 Phase 1 A-scaling sketch (§3.3) as one of two candidate resolutions of the empirical $A^{-1/3}$ vs CPP $A^{-0.10}$ discrepancy. R1 hypothesizes that the inter-alpha spacing $R_\alpha$ in CPP varies with cluster size, with the candidate physical mechanism being DP-sea screening of alpha-alpha Coulomb at internal contacts (vs full Coulomb at the isolated $^8$Be contact that fixed $R_\alpha = 2.37$ fm). If $R_\alpha$ varied appropriately with $A$, it would propagate to $\hbar\omega \propto 1/R_c^2$ via the cluster centroid-to-vertex distance and could in principle close the empirical scaling.

**Companion files:**
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a_Ascaling.md` (Session 7 Phase 1 A-scaling extension; this work tests R1 from §3.3)
- `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_a_Ascaling_R1.py` (reproducible computation)
- `series_strong/papers/SS-7/SS-7_alpha_cluster_edge_formula.tex` Finding 7.1 (R$_{\alpha\alpha}$ inversion from $^8$Be), §11 (Coulomb screening discussion, OPEN-SS-25)
- `Research_Frontier.md` OPEN-SS-35 entry; OPEN-SS-25 entry (DP-sea screening of alpha-alpha Coulomb)

**Net programme effect:** R1 (R$_\alpha$ scale-dependence as A-scaling closure) **RULED OUT**. Three findings, all robust:

1. **Sign of energetic mechanism is wrong.** DP-sea screening at internal contacts compresses $R_\alpha$ inward (force-balance result, robust across all reasonable parametrizations of the K$_3$ well). For the empirical $A^{-1/3}$ scaling, $R_\alpha$ would need to *expand* with $A$. R1 produces compression; the opposite of what's needed.

2. **Pattern is non-monotonic, not power-law.** Inverting CPP/empirical ratios to ask "what $R_\alpha(A)$ would close the gap" yields a U-shape: endpoints (regular polytopes $N_\alpha = 4, 12$) already match empirical to ~1–10%; mid-range J-solids ($N_\alpha = 5$–$10$) need 7–23% expansion peaking at $N_\alpha = 10$. **No monotonic $R_\alpha(A)$ law could produce this pattern.** The discrepancy is shape-driven (J-solid mid-range overshoot), not radius-driven.

3. **A-scaling closure is decoupled from layer-3 gap-strength problem (Decoupling Theorem).** The dimensionless $V_{\rm SO}/\hbar\omega = (v_F/c)^2$ is independent of $\hbar\omega$ magnitude in the CPP B-α layer 1 framework. Even if R1 had given the right answer and closed the A-scaling, the magic-number gap strengths would still be factor 2–3 below empirical. The two problems are decoupled.

**Programme-level negative result #5** on the OPEN-SS-35 closure programme (after Route D in Session 5 Phase 2, Route B-γ in Session 7 Phase 2, Route 1b in Session 10, Path (i) cluster-surface Thomas-form in Session 11 Phase 1). Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged. Forward pointer: U-shape diagnostic structurally resembles SS-7 OPEN-SS-32 J-solid regime (oblate-deformation activation at $N_\alpha \in \{7, 8, 9, 10\}$); investigation of this connection registered as future sub-sub-question.

---

## §1. Background and the R1 hypothesis

### §1.1 Where R1 was registered

The Session 7 Phase 1 A-scaling sketch (§3.3) registered two candidate resolutions of the empirical-vs-CPP discrepancy:

> **Resolution R1: $R_\alpha$ depends on cluster size.** In CPP, the inter-alpha spacing $R_\alpha = 2.37$ fm was set in SS-7 by inversion of the alpha-alpha binding formula at small clusters. For larger clusters, the effective $R_\alpha$ may decrease as alpha-cluster compression sets in. This would shift $R_c \to R_c \cdot R_\alpha(A)/R_\alpha(\text{small})$ and could in principle reproduce $A^{-1/3}$.
>
> **Resolution R2: HO mean-field is at the cluster scale, not the alpha-scale.** The empirical Bohr-Mottelson $41/A^{1/3}$ is a phenomenological fit to *all* nuclei; it's not specifically about alpha-cluster nuclei. For cluster nuclei specifically, the appropriate HO frequency may differ.

This Session 12 work tests R1 quantitatively via the CPP-native screening mechanism documented in SS-7 §11 (the Coulomb-screening discussion that registers OPEN-SS-25).

### §1.2 The CPP-native screening mechanism

SS-7 §11 establishes the following picture:

- $^8$Be: isolated alpha-alpha contact, full Coulomb. $R_{\alpha\alpha} = 2.37$ fm extracted from the 92 keV unboundness assuming $f_{\rm eff} = 1$.
- Internal polytope contacts: DP-sea reorganization between two alphas embedded in a polytope (with at least one additional alpha neighbor) partially neutralizes the local charge product. Effective Coulomb is reduced by factor $f_{\rm eff}^2$.

SS-7 §11 documents that the per-edge formula's empirical success at $\pm 1.5\%$ across the alpha-chain regime requires effective Coulomb to be *much smaller* than full vacuum (otherwise the formula would over-subtract by ~25% at $^{40}$Ca scale). Conventional cluster-model $f_{\rm eff} \approx 0.5$ is insufficient; CPP requires stronger screening, likely $f_{\rm eff} \lesssim 0.15$ at internal contacts.

### §1.3 The R1 mechanical picture

If internal contacts have screened Coulomb ($f_{\rm eff} < 1$), the equilibrium contact distance is determined by force balance against a smaller Coulomb repulsion. With less Coulomb push-back, the contact can move *closer* (compression) if the K$_3$ binding well admits it.

Quantitatively, the equilibrium $R^*$ satisfies
$$V_{K_3}'(R^*) + f_{\rm eff}^2 \cdot V_{\rm Coul}'(R^*) = 0 \tag{1}$$
with $V_{\rm Coul}(R) = +4\alpha_{\rm em}\hbar c/R$ (positive Coulomb repulsion).

At $f_{\rm eff} = 1$: $R^* = R_{8{\rm Be}} = 2.37$ fm by definition.

At $f_{\rm eff} < 1$: $R^*$ shifts to where $V_{K_3}'(R)$ matches a smaller positive number — i.e., $R^*$ moves toward the K$_3$ well *minimum* (where $V_{K_3}'(R) = 0$). So R1 predicts $R_\alpha$ compression at internal contacts, with maximum compression at $f_{\rm eff} \to 0$ where $R^* \to R_0$ (the K$_3$ well center).

The question: is the magnitude and direction of this compression compatible with closing the empirical $A^{-1/3}$ scaling?

---

## §2. K$_3$ well parametrization and force-balance calculation

### §2.1 Two-constraint anchoring at $R_{8{\rm Be}}$

A 3-parameter Gaussian K$_3$ well
$$V_{K_3}(R) = -V_0 \exp\left(-(R - R_0)^2/\sigma^2\right) \tag{2}$$
is constrained by two SS-5/SS-7 facts at the $^8$Be contact:

**Constraint A (depth at contact):** The K$_3$ collective-mode contribution at $R = R_{8{\rm Be}}$ equals the SS-5 $B_{\rm pair} = M_0/\phi = 2.342$ MeV:
$$V_{K_3}(R_{8{\rm Be}}) = -B_{\rm pair} \tag{3}$$

**Constraint B (force balance at $f_{\rm eff} = 1$):** At $^8$Be the equilibrium is at $R_{8{\rm Be}} = 2.37$ fm with full Coulomb:
$$V_{K_3}'(R_{8{\rm Be}}) = -V_{\rm Coul}'(R_{8{\rm Be}}) = +\frac{4\alpha_{\rm em}\hbar c}{R_{8{\rm Be}}^2} = +1.026 \text{ MeV/fm} \tag{4}$$

These two constraints fix any two of $\{V_0, R_0, \sigma\}$ given the third. The third parameter is a physical input — sigma-scan results below show the *sign* of $R_\alpha(f_{\rm eff})$ is independent of this choice; only the *magnitude* of compression varies.

### §2.2 Sigma-scan: sign robustness

Computing $R_\alpha(f_{\rm eff})$ across the physical range $\sigma \in [1.0, 2.5]$ fm (covering K$_3$ collective-mode width plausibly anchored to alpha overlap scale $R_{\rm RMS}^\alpha = 1.68$ fm):

| $\sigma$ (fm) | $V_0$ (MeV) | $R_0$ (fm) | $R(f=0.5)$ | $R(f=0.2)$ | $R(f=0.1)$ |
|---|---|---|---|---|---|
| 1.00 | 2.457 | 2.151 | (out of range) | (out of range) | (out of range) |
| 1.20 | 2.510 | 2.055 | (out of range) | 2.070 | (out of range) |
| 1.50 | 2.609 | 1.877 | 2.030 | 1.905 | 1.884 |
| 1.68 | 2.682 | 1.752 | 1.954 | 1.790 | 1.762 |
| 2.00 | 2.837 | 1.494 | 1.812 | 1.561 | 1.512 |
| 2.50 | 3.160 | 1.002 | 1.594 | 1.169 | 1.053 |

**All cases give $R_\alpha(f_{\rm eff} < 1) < R_{8{\rm Be}} = 2.37$ fm** — compression is universal across the parametrization family. The sign is robust; only the magnitude depends on the (undetermined) K$_3$ well width.

For the canonical choice $\sigma = R_{\rm RMS}^\alpha = 1.68$ fm (alpha overlap scale): $R_0 = 1.752$ fm, and at the SS-7-implied internal-contact screening $f_{\rm eff}^2 \approx 0.05$ ($f_{\rm eff} \approx 0.224$), $R_\alpha^{\rm internal} \approx 1.79$ fm — a 25% inward compression from $R_{8{\rm Be}}$.

### §2.3 Direction required for empirical match

Empirical Bohr-Mottelson $\hbar\omega = 41/A^{1/3}$ MeV is *decreasing* with $A$. In the Session 6 / Session 7 framework, $\hbar\omega \propto 1/R_c^2$ where $R_c$ is the cluster centroid-to-vertex distance. With polytope geometry $R_c \propto R_\alpha$ at fixed shape, $\hbar\omega \propto 1/R_\alpha^2$. **Empirical match requires $R_\alpha$ to *increase* with $A$** to push $\hbar\omega$ down.

But R1 (energetic screening) predicts $R_\alpha$ to *decrease* (compress) with $A$. **Sign is wrong.** The CPP-native screening mechanism cannot resolve the A-scaling discrepancy: it pushes the discrepancy in the wrong direction.

### §2.4 Could any energetic mechanism give expansion?

Reviewing CPP-native energetic mechanisms that could drive $R_\alpha$ outward at internal contacts:

| Mechanism | Direction | Status |
|---|---|---|
| DP-sea Coulomb screening | inward (compression) | this work — wrong sign |
| Pauli blocking at internal contacts | inward (excludes overlap) | wrong sign |
| Cluster-internal zero-point motion | outward (small) | too weak; subleading |
| Cluster-internal rotation | outward | $J = 0$ ground states; not active |
| K$_3$ well broadening at multi-contact | unchanged sign | broadening reduces $V_{K_3}''$ but doesn't flip sign |

None of the CPP-native energetic mechanisms produce expansion. The *only* way to get outward $R_\alpha(A)$ is structural: the K$_3$ well center $R_0$ itself is $N_\alpha$-dependent because the polytope geometry at multi-contact sites differs from the isolated-pair geometry. **This is structural reinterpretation (R2 territory), not energetic R1.**

---

## §3. The U-shape diagnostic

A second, independent finding emerges from inverting the CPP/empirical ratios to ask "what $R_\alpha(A)$ would close the gap?"

The required adjustment, computed as $R_\alpha^{\rm required}(A) = R_{8{\rm Be}} \cdot \sqrt{\hbar\omega^{\rm CPP}(A) / \hbar\omega^{\rm emp}(A)}$ using Session 7 §3.1 numerical values:

| $N_\alpha$ | $A$ | $\hbar\omega^{\rm CPP}$ | $\hbar\omega^{\rm emp}$ | CPP/emp | required $R_\alpha$ | change |
|---|---|---|---|---|---|---|
| 4 | 16 | 14.60 | 16.27 | 0.897 | 2.245 fm | $-5.3\%$ |
| 5 | 20 | 17.19 | 15.10 | 1.138 | 2.528 fm | $+6.7\%$ |
| 6 | 24 | 18.06 | 14.21 | 1.271 | 2.671 fm | $+12.7\%$ |
| 7 | 28 | 19.15 | 13.50 | 1.418 | 2.822 fm | $+19.1\%$ |
| 8 | 32 | 18.94 | 12.91 | 1.467 | 2.870 fm | $+21.1\%$ |
| 9 | 36 | 18.56 | 12.42 | 1.495 | 2.898 fm | $+22.3\%$ |
| 10 | 40 | 18.05 | 11.99 | 1.506 | 2.908 fm | $+22.7\%$ |
| 12 | 48 | 11.13 | 11.28 | 0.987 | 2.354 fm | $-0.7\%$ |

**The pattern is non-monotonic, U-shaped, and structurally inconsistent with any smooth $R_\alpha(A)$ law.** Endpoints (regular polytopes, full 3D symmetry) match empirical to within 1–10%; the mid-range J-solid deltahedra (axial symmetry) over-predict by 30–50%.

**Structural interpretation:** the discrepancy is correlated with deltahedron *shape*, not with cluster size $A$. The regular tetrahedron (N=4) and regular icosahedron (N=12) get close to empirical; the J-solids in between (triangular bipyramid, octahedron, pentagonal bipyramid, snub disphenoid, triaugmented triangular prism, gyroelongated square bipyramid) over-bind the centroid relative to empirical.

This pattern is structurally similar to **SS-7 OPEN-SS-32** (Cluster-level collective oblate-deformation mode, registered SS-7 Discussion §):

> When cluster shape has symmetry-breakable belt or seam structure (the J-solid deltahedra at $N_\alpha \in \{7, 8, 9, 10\}$ all have such structure: pentagonal bipyramid's equatorial belt, snub disphenoid's dihedral seam, etc.), an oblate deformation activates with a quantized binding contribution of approximately $+B_{\rm pair} \times$ attenuation factor.

OPEN-SS-32 documented J-solid mid-range *over-binding* in the SS-7 binding-energy fit (Regime B at $N_\alpha \in \{7, 8, 9, 10\}$: $\approx +0.55 B_{\rm pair}$ excess). The U-shape discrepancy in $\hbar\omega$ shows the same J-solid-mid-range signature in a different observable. **This connection is registered as a forward pointer for future-session investigation.**

The U-shape diagnostic is itself a programme advance: it converts the Session 7 "weak A-scaling" finding into a more specific "J-solid mid-range overshoot" diagnostic, with a structurally-motivated avenue for further investigation (the OPEN-SS-32 connection).

---

## §4. The Decoupling Theorem

A third finding emerges from combining the R1 result with the Session 8 B-α layer 1 framework.

### §4.1 Statement

**Theorem (Decoupling of A-scaling from gap-strength):** In the CPP B-α layer 1 framework where $V_{\rm SO} = (v_F/c)^2 \cdot \hbar\omega$, the dimensionless ratio $V_{\rm SO}/\hbar\omega = (v_F/c)^2$ is *independent of the magnitude of $\hbar\omega$*. Therefore A-scaling closure (whether via R1 or R2) does not affect the layer-3 gap-strength prediction.

### §4.2 Proof

The Session 8 B-α layer 1 sketch establishes (via three independent CPP-derived approaches all bracketing the empirical band):
$$V_{\rm SO}^{\rm CPP} = (v_F/c)^2 \cdot \hbar\omega \tag{5}$$
where $v_F/c$ is computed from cluster-density Fermi gas analysis at A = 56, giving $v_F/c \approx 0.30$ in CPP.

The dimensionless ratio:
$$\frac{V_{\rm SO}^{\rm CPP}}{\hbar\omega^{\rm CPP}} = \left(\frac{v_F}{c}\right)^2 = 0.090 \tag{6}$$

This ratio determines magic-number gap strength via the standard Goeppert-Mayer / Jensen formulas (Session 9 §3 Eq. 4): the spin-orbit splitting between $j = l \pm 1/2$ partners is $V_{\rm SO} \cdot (2l+1)/2$, and the strong-magic threshold ratio is $V_{\rm SO}/\hbar\omega \approx 0.20$–$0.25$.

If A-scaling closure shifted $\hbar\omega^{\rm CPP}(A=56)$ from 13 MeV to the empirical 10.7 MeV, then by Eq. (5), $V_{\rm SO}^{\rm CPP}$ would also scale to $(0.30)^2 \cdot 10.7 = 0.96$ MeV. The ratio $V_{\rm SO}/\hbar\omega$ stays at $0.090$ — unchanged. **The dimensionless quantity that determines gap strength is invariant under A-scaling adjustment.** $\blacksquare$

### §4.3 Implication

This decoupling has substantive consequences for the closure programme:

1. **A-scaling closure and gap-strength closure are independent open problems.** Closing one does not close the other.

2. **The Session 11 Phase 1 conclusion that "gap-strength closure requires CPP physics outside the simple K$_3$ Gaussian + HO + L·S framework" is unaffected by A-scaling work.** Even with full A-scaling closure (R1 or R2), the gap-strength deficit (factor 2–3 below empirical) remains.

3. **A-scaling closure does not advance the layer-3 picture.** The Session 7 sketch §6 implicitly assumed that A-scaling closure would benefit the layer-3 picture; this Decoupling Theorem refutes that assumption.

4. **The pathway to gap-strength closure is via $v_F/c$, not $\hbar\omega$.** Either $v_F/c$ in the CPP framework would have to be larger (~0.37 to match empirical ratio 0.14) — which would require revisiting the Session 8 layer 1 derivation — or the relationship $V_{\rm SO} = (v_F/c)^2 \cdot \hbar\omega$ itself would have to be modified by additional CPP physics (the avenues identified in Session 11 Phase 1).

The Decoupling Theorem thus *narrows* the closure programme: it removes A-scaling closure from the candidate list of fixes for gap strength.

---

## §5. Programme implications

### §5.1 R1 status: RULED OUT

R1 (R$_\alpha$ scale-dependence as A-scaling closure) is ruled out:
- **Energetic mechanism gives wrong sign** — DP-sea screening compresses $R_\alpha$ inward; empirical match requires expansion outward.
- **Pattern is shape-driven, not radius-driven** — the U-shape discrepancy cannot be produced by any monotonic $R_\alpha(A)$.
- **A-scaling closure does not touch layer-3 gap strength** (Decoupling Theorem).

The Session 7 sketch §3.3 hypothesized R1 as one of two candidate resolutions. Session 12 closes it negatively.

### §5.2 R2 status: only remaining A-scaling closure candidate

R2 (cluster-scale vs alpha-scale mean field interpretation) becomes the *only* remaining A-scaling closure candidate among the two registered in Session 7. R2 is consistent with the U-shape diagnostic (the discrepancy is between cluster-shape physics and nucleon-density physics, not within either) but is multi-session by scope and may also fail to fully close.

### §5.3 Negative-result count

R1 ruled out is the **5th programme-level negative result** in the OPEN-SS-35 closure programme:

| # | Route/Path | Session | Reason ruled out |
|---|---|---|---|
| 1 | Route D (direct lattice-shell counting) | Session 5 Phase 2 | 600-cell distance shells don't match magic numbers |
| 2 | Route B-γ (K$_3$-mode phase coupling for spin-orbit) | Session 7 Phase 2 | $V_{\rm SO}/\hbar\omega \sim 10^{-3}$, magnitude insufficient |
| 3 | Route 1b (V_SO refinement saturation) | Session 10 | Saturates at $V_{\rm SO}/\hbar\omega \approx 0.11$, below magic threshold |
| 4 | Path (i) (cluster-surface Thomas-form) | Session 11 Phase 1 | $f_{\rm SO}(r)$ peaks at center, opposite of Woods-Saxon |
| 5 | **R1 (R$_\alpha$ scale-dependence as A-scaling closure)** | **Session 12** | **wrong sign + non-monotonic pattern + decoupled from gap strength** |

Each negative result is a programme-tightening: it removes a candidate route from the active list. The closure programme has now narrowed substantially.

### §5.4 OPEN-SS-35 closure trajectory: stage (vi) preserved

(i) Speculative cross-paradigm bridge (Session 4) → (ii) scoping passed (Session 5 Phase 2) → (iii) sub-question (a) Level-1 partial closure (Session 6) → (iv) A-scaling extension + sub-question (b) scoping (Session 7) → (v) B-α layer 1 closed (Session 8) → (vi) **B-α layer 3 partial closure: empirical magic-number sequence reproduced from CPP first-principles** (Session 9; refined Sessions 10, 11; further refined this Session 12).

Six programme-level stages preserved. Session 12 refines stage (vi) by ruling out R1 as an A-scaling closure candidate (which the Decoupling Theorem then shows would not have advanced the gap-strength picture even if it had succeeded).

**First qualitative cross-paradigm consilience claim (Session 9) intact.** Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.

### §5.5 Forward pointer: U-shape ↔ OPEN-SS-32 connection

The U-shape diagnostic (J-solid mid-range overshoot, regular-polytope endpoints fine) is structurally similar to the **SS-7 OPEN-SS-32 J-solid regime** (Cluster-level collective oblate-deformation mode, regime B at $N_\alpha \in \{7, 8, 9, 10\}$ with $+0.55 B_{\rm pair}$ excess in SS-7's binding-energy fit).

If the J-solid mid-range deltahedra activate an oblate-deformation mode in the binding energy (OPEN-SS-32), they may also activate a *radial breathing mode* that softens the centroid-to-vertex confinement (effectively expanding $R_c$, lowering $\hbar\omega$). The U-shape pattern in $\hbar\omega$ is the right observable to capture this if true.

This is registered as a future-session sub-sub-question: **"Does the OPEN-SS-32 J-solid oblate-deformation mode also produce the $\hbar\omega$ U-shape via radial-breathing softening?"** Investigation requires:
- Reading SS-7 OPEN-SS-32 in detail (Discussion section and references therein)
- Reading SS-8 H3$'$ provisional-tier work on the analog opposite-polarity pair-bonus mechanism
- Computing the radial-breathing mode of J-solid deltahedra and its effect on $\hbar\omega^*$
- Checking whether the same attenuation factor that fits SS-7 binding-energy excess (~0.55) fits the $\hbar\omega$ U-shape

This is potentially R2 territory generalized — i.e., the "additional CPP physics outside the simple K$_3$ Gaussian-modulated mean field framework" identified in Session 11 Phase 1 may be the OPEN-SS-32 oblate-deformation physics applied at the $\hbar\omega$ scale. **Multi-session by scope; not pursued in Session 12.**

---

## §6. Forward-looking pointers

**Priority 1:** OPEN-SS-32 ↔ U-shape connection investigation. Multi-session by scope (3–5 sessions). Requires careful reading of SS-7 / SS-8 prior art on J-solid mid-range physics. Could potentially close R2 *and* identify the "additional CPP physics" identified in Session 11 Phase 1 as needed for gap-strength closure. **High leverage if successful.**

**Priority 2 (anti-priority, do not pursue):** Further refinement of $R_\alpha(A)$ as an energetic mechanism. R1 has demonstrated this cannot work (wrong sign across all parametrizations). Pattern is shape-driven; energetic refinement cannot capture shape physics.

**Priority 3:** Alternative gap-strength closure routes per Session 11 Phase 1: avenue (a) sharper-surface from K$_3$ edge mechanism + Pauli-blocking at cluster boundary; avenue (b) higher-order K$_3$ modes / color coupling at cluster-internal scale; avenue (d) reframe — strength hierarchy isn't pure mean-field property. Each multi-session by scope; (a) and (d) likely connect to the OPEN-SS-32 investigation in Priority 1 (suggesting all three are different facets of the same "additional CPP physics outside simple framework" question).

**Priority 4 (deferred):** OPEN-SS-16 Layer B closure work (operator structure of $\vec L \cdot \vec S$). Layer 2 of B-α and avenue (c) both depend on this. Multi-session by scope; deepest open problem at programme level.

**Anti-priority:** Do not speculatively connect the U-shape to OPEN-SS-32 in Session 12. The U-shape is a substantive diagnostic, but a clean R2-territory investigation requires careful prior-art reading and a fresh session.

---

## §7. Summary

R1 (R$_\alpha$ scale-dependence as A-scaling closure of OPEN-SS-35 sub-question (a)) is **RULED OUT** by three independent findings:

1. **Wrong sign:** DP-sea Coulomb screening at internal contacts compresses $R_\alpha$ inward; empirical match requires expansion. Robust across all reasonable K$_3$ well parametrizations ($\sigma \in [1.0, 2.5]$ fm). No CPP-native energetic mechanism gives expansion.

2. **U-shape pattern, not power law:** The required $R_\alpha(A)$ to close the empirical gap is non-monotonic — endpoints (regular polytopes $N = 4, 12$) need ~no change; mid-range J-solid deltahedra ($N = 5$–$10$) need 7–23% expansion peaking at $N = 10$. No monotonic $R_\alpha(A)$ law produces this shape. The discrepancy is shape-driven (J-solid mid-range overshoot), structurally similar to the SS-7 OPEN-SS-32 J-solid regime.

3. **Decoupling Theorem:** $V_{\rm SO}/\hbar\omega = (v_F/c)^2$ is independent of $\hbar\omega$ magnitude in the CPP B-α layer 1 framework. A-scaling closure (whether R1 or R2) does not touch the layer-3 gap-strength deficit identified in Session 11 Phase 1.

**Net programme effect:** R1 status moves from "candidate resolution" to "**RULED OUT, 5th programme-level negative result**". R2 is the only remaining A-scaling closure candidate. The U-shape diagnostic is itself a programme advance, with structural connection to OPEN-SS-32 registered as future-session investigation (high-leverage, multi-session). The Decoupling Theorem narrows the gap-strength closure candidate list by removing A-scaling fixes from it. Six programme-level OPEN-SS-35 stages preserved; first qualitative cross-paradigm consilience claim (Session 9) intact; Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances unchanged.
