# OPEN-SS-32 ↔ U-shape Unification — Phase 2: Uniform-Scaling Radial-Breathing Model RULED OUT (Session 13 Phase 2)

**Date:** 4 May 2026 (Session 13, Phase 2)
**Purpose:** Execute the Phase 2 single-session-tractable computation registered in `SS-9_OPEN-SS-32_Ushape_unification_phase1.md` §6: compute the uniform-scaling radial-breathing-mode frequency, zero-point amplitude, and fractional $\hbar\omega^*$ softening across the eight canonical alpha-chain deltahedra, and compare with the Session 12 inversion-table U-shape.

**Companion files:**
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase1.md` (Phase 1 prior-art read and Phase 2 work plan)
- `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase2.py` (this Phase 2 reproducible computation)
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a_Ascaling_R1_RULED_OUT.md` §3 (Session 12 inversion table; the empirical U-shape data)

**Net programme effect:** **Uniform-scaling radial-breathing model RULED OUT as a complete R2 closure mechanism** on three independent grounds: wrong magnitude (factor ~7 undershoot at the empirical peak); wrong pattern (model is monotonically decreasing in $N_\alpha$, empirical is U-shaped with peak at $N_\alpha = 10$); wrong sign at endpoints ($N_\alpha = 4, 12$ where empirical needs no softening, model predicts substantial softening). **The unification hypothesis itself is not ruled out** — only its simplest realization (model (a) of Phase 1 §6.3 step 1). Phase 1 §6.3 anticipated this branch and registered model (b), symmetry-resolved breathing decomposition, as the natural next step. **Sixth programme-level negative-result demonstration** in the OPEN-SS-35 closure programme; rules out a specific R2 closure realization but leaves R2 (and the broader unification hypothesis) open at higher-resolution mechanism. R2 is now substantively weakened — the simplest plausible mechanism doesn't work — but not closed. Phase 3 (symmetry-resolved decomposition) is the natural multi-session next step. Six programme-level stages of OPEN-SS-35 closure programme preserved. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.

---

## §1. Strategy

Phase 1 (this session opening) read the SS-7 OPEN-SS-32 prior art and the SS-8 H3$'$ analog, established the unification hypothesis as geometrically natural (Pattern 6 K$_3$ scale-recurrence + six-of-eight empirical coincidence + closure-leverage), identified the $N_\alpha = 6$ octahedron as a discriminating data point between three admissible readings (A: broader breathing selection; B: U-shape false positive; C: distinct partially-overlapping mechanisms), and registered the Phase 2 computation as single-session-tractable.

Phase 1 §6.3 step 1 specified two candidate definitions of the breathing degree of freedom:

> Two candidates: (a) uniform scaling $\vec R_i \to \lambda \vec R_i$ for all vertices (simplest, single dof); (b) symmetry-resolved breathing modes (one dof per irreducible representation of the cluster's point group, with the totally symmetric $A_1$ representation being the analog of the uniform-scaling dof). Phase 2 should start with (a) and revisit (b) if the simple scaling does not produce the observed selection rules.

This Phase 2 executes (a). Outcome below dictates whether (b) is needed.

---

## §2. Model and computation

### §2.1 The uniform-scaling radial-breathing mode

Collective coordinate: scaling factor $\lambda$, with all polytope vertices transforming as $\vec R_i \to \lambda \vec R_i$. Equilibrium at $\lambda = 1$ (all alpha-alpha contacts at $R_\alpha = 2.37$ fm).

**Energy as $\lambda$ varies.** The SS-7 Layer-1 leading-order edge sum $|E| \cdot B_{\rm pair}$ is a graph-topological quantity; the K$_3$ collective-mode eigenvalue $B_{\rm pair} = M_0/\varphi$ is set by the K$_3$ graph, not by the contact distance. But the K$_3$ mode at each contact is detuned spatially when the alpha-alpha distance deviates from the natural $R_\alpha$. The Phase 1 SS-7 §11 / OPEN-SS-25 reading establishes that the alpha overlap scale $R_{\rm RMS}^\alpha = 1.68$ fm is the K$_3$-mode width in space.

Modeling each contact as a Gaussian profile in the alpha-alpha distance with width $\sigma_{K3}$:

$$E_{\rm cluster}(\lambda) = \text{const} - |E| \cdot B_{\rm pair} \cdot \exp\!\left(-\frac{(\lambda - 1)^2 R_\alpha^2}{2 \sigma_{K3}^2}\right) \tag{1}$$

This is the simplest model that (i) gives equilibrium at $\lambda = 1$, (ii) recovers SS-7 LO at $\lambda = 1$, (iii) detunes contacts symmetrically away from equilibrium with a CPP-internal width.

**Spring constant.**

$$k_\lambda \equiv \left.\frac{d^2 E_{\rm cluster}}{d\lambda^2}\right|_{\lambda = 1} = |E| \cdot B_{\rm pair} \cdot \left(\frac{R_\alpha}{\sigma_{K3}}\right)^2 \tag{2}$$

Units: MeV (per dimensionless squared). At canonical $\sigma_{K3} = 1.68$ fm, $(R_\alpha/\sigma_{K3})^2 = (2.37/1.68)^2 = 1.99$, and $k_\lambda \approx 4.66\,|E|$ MeV.

**Effective mass.** Kinetic energy under uniform scaling is $\frac{1}{2} m_\alpha \sum_i |\dot{\vec R_i}|^2 = \frac{1}{2} M_\lambda (d\lambda/dt)^2$ with

$$M_\lambda c^2 = m_\alpha \sum_i |\vec R_i|^2 \tag{3}$$

Units: MeV·fm$^2$.

**Breathing-mode frequency.**

$$\hbar\omega_{\rm br} = \hbar c \sqrt{\frac{k_\lambda}{M_\lambda c^2}} \tag{4}$$

Units: MeV.

**Zero-point amplitude.** Ground-state of harmonic oscillator with mass $M_\lambda$ and spring $k_\lambda$:

$$\langle (\Delta\lambda)^2\rangle = \frac{\hbar c}{2 \sqrt{k_\lambda \cdot M_\lambda c^2}} \tag{5}$$

Dimensionless.

**Fractional softening of $\hbar\omega^*$.** Sub-question (a) self-consistent solution gives $\hbar\omega^* \propto 1/R_c^2 \propto 1/R_\alpha^2$ at fixed shape. Zero-point fluctuation in $\lambda$ broadens $R_\alpha$ to $\langle R_\alpha^2 (1 + \Delta\lambda)^2\rangle = R_\alpha^2 (1 + \langle (\Delta\lambda)^2\rangle)$. Leading-order Taylor of $1/R^2$ gives:

$$\frac{\Delta\hbar\omega^*}{\hbar\omega^*} \approx -2 \langle (\Delta\lambda)^2\rangle \tag{6}$$

### §2.2 Calibration: $\sigma_{K3}$

The K$_3$ mode width $\sigma_{K3}$ is the only free parameter of the model. The natural CPP-internal value is $\sigma_{K3} = R_{\rm RMS}^\alpha = 1.68$ fm — the alpha overlap scale that anchors the SS-7 §11 screening discussion and the SS-5 K$_3$ collective-mode width. Sensitivity scan reported in §5 over $\sigma_{K3} \in \{1.0, 1.4, 1.68, 2.0, 2.5\}$ fm to bracket the result.

---

## §3. Results

### §3.1 Eight-row table

Polytope geometries inherited from Session 7 A-scaling script. All polytopes scaled to minimum-edge-length $R_\alpha = 2.37$ fm. Computed at canonical $\sigma_{K3} = 1.68$ fm.

| $N_\alpha$ | polytope | sym | $|E|$ | $\sum |R_i|^2$ (fm$^2$) | $\hbar\omega_{\rm br}$ (MeV) | $\langle(\Delta\lambda)^2\rangle$ | predicted softening | empirical required | pred/emp |
|---|---|---|---|---|---|---|---|---|---|
| 4 | tetrahedron | $T_d$ | 6 | 8.43 | 5.89 | 0.1053 | $-21.05\%$ | $+11.5\%$ | $-1.83$ |
| 5 | trig. bipyramid | $D_{3h}$ | 9 | 13.11 | 5.78 | 0.0689 | $-13.78\%$ | $-12.2\%$ | $1.13$ |
| 6 | octahedron | $O_h$ | 12 | 16.85 | 5.89 | 0.0526 | $-10.53\%$ | $-21.3\%$ | $0.50$ |
| 7 | pent. bipyramid | $D_{5h}$ | 15 | 23.43 | 5.58 | 0.0399 | $-7.99\%$ | $-29.5\%$ | $0.27$ |
| 8 | snub disphenoid | $D_{2d}$ | 18 | 29.71 | 5.43 | 0.0324 | $-6.47\%$ | $-31.8\%$ | $0.20$ |
| 9 | triaug. tri. prism | $D_{3h}$ | 21 | 36.37 | 5.30 | 0.0271 | $-5.42\%$ | $-33.1\%$ | $0.16$ |
| 10 | gyroel. sq. bipyr. | $D_{4d}$ | 24 | 44.69 | 5.11 | 0.0229 | $-4.57\%$ | $-33.6\%$ | $0.14$ |
| 12 | icosahedron | $I_h$ | 30 | 60.97 | 4.90 | 0.0175 | $-3.50\%$ | $+1.4\%$ | $-2.47$ |

Here "predicted softening" is $-2\langle(\Delta\lambda)^2\rangle$; "empirical required" is $1 - 1/(1 + x)^2$ with $x$ = the Session 12 required-$R_\alpha$-change percentage.

### §3.2 Pattern of predicted softening with $N_\alpha$

The model produces a **monotonically decreasing** softening magnitude with $N_\alpha$:

```
N=4: -21.05%
N=5: -13.78%
N=6: -10.53%
N=7:  -7.99%
N=8:  -6.47%
N=9:  -5.42%
N=10: -4.57%
N=12: -3.50%
```

Largest predicted softening at $N_\alpha = 4$ (tetrahedron); smallest at $N_\alpha = 12$ (icosahedron). The model's behavior in the limits is structurally driven: $\langle(\Delta\lambda)^2\rangle \propto 1/\sqrt{|E| \cdot \sum |R_i|^2}$ via Equation 5. For deltahedra at fixed $R_\alpha$, $|E| = 3N - 6$ grows as $\sim 3N$ and $\sum |R_i|^2 \sim N \cdot R_{\rm circ}^2$, so $\sqrt{|E| \cdot \sum |R_i|^2} \sim N$ and $\langle(\Delta\lambda)^2\rangle \sim 1/N$. The ground-state breathing-mode amplitude is suppressed at large clusters by the increased moment-of-inertia at fixed K$_3$-bond density. This is the wrong N-dependence for the empirical U-shape.

---

## §4. Three diagnostics

### §4.1 Sign

Predicted softening is **uniformly negative** (lowering $\hbar\omega^*$) across all eight polytopes. This is structurally correct: a positive zero-point broadening of $R_\alpha$ always lowers $\hbar\omega^* \propto 1/R_\alpha^2$.

The empirical pattern is **mixed in sign**: $N_\alpha = 4$ requires **compression** (negative $R_\alpha$ change, i.e., positive $\hbar\omega^*$); $N_\alpha = 12$ requires near-zero change. The model gives substantial softening at both endpoints. **Endpoint sign mismatch at $N_\alpha = 4$ and $N_\alpha = 12$.**

### §4.2 Magnitude

At the empirical peak of the U-shape ($N_\alpha = 10$, gyroelongated square bipyramid, requires $-33.6\%$ softening to close the empirical $A^{-1/3}$ scaling), the model predicts only $-4.57\%$ — **factor of 7.4 too small**.

The ratio model/empirical is $0.14$ at the peak and degrades further at $N_\alpha = 9$ (0.16), $N_\alpha = 8$ (0.20), $N_\alpha = 7$ (0.27). Only at $N_\alpha = 5$ does the model magnitude approach the empirical requirement (ratio $1.13$) — but this is a coincidence at one point along curves of opposite shape, not a real match.

### §4.3 Pattern

Empirical pattern is **U-shaped** with peak softening at $N_\alpha = 10$ and endpoints (regular polytopes $N_\alpha = 4, 12$) approximately at zero or slightly compressive. Model pattern is **monotonic in $N_\alpha$** with peak softening at $N_\alpha = 4$ (the smallest deltahedron). **The model gives the wrong shape; it captures bulk-density scaling but not shape-class selection.**

The structural reason: under uniform scaling, every contact contributes equally regardless of belt/seam structure. Pattern 6 K$_3$ scale-recurrence at the cluster-shape scale does occur at every polytope with edges, but the empirical U-shape is precisely a shape-class-selected effect concentrated at J-solid mid-range deltahedra. Uniform scaling doesn't see shape-class structure.

### §4.4 $N_\alpha = 6$ selection-rule test

Model predicts $-10.53\%$ softening at the octahedron. **Non-zero**, structurally trivially consistent with Reading A (broader breathing selection rule than oblate deformation).

But this is a *trivial* consistency: under uniform scaling, every polytope with edges has a breathing mode. The result tells us nothing meaningful about Reading A vs B vs C — it just reflects that the model has no shape-class selection rule whatsoever.

**Real Reading A vs B/C discrimination requires model (b)** (symmetry-resolved decomposition), where the radial-breathing dof can be projected onto specific irreducible representations of each cluster's point group. The octahedron's $O_h$ symmetry forbids belt-localized breathing modes (no $C_n$ axis with $n \geq 3$ that admits belt structure); under model (b), $O_h$ would presumably suppress the relevant component, giving zero (Readings B/C) or near-zero (broader Reading A) breathing-mode softening. Phase 2's model-(a) result here is uninformative on the Reading discrimination.

---

## §5. Sensitivity to $\sigma_{K3}$

| $\sigma_{K3}$ (fm) | $\langle(\Delta\lambda)^2\rangle$ at $N=8$ | predicted softening at $N=8$ |
|---|---|---|
| 1.00 | 0.0193 | $-3.85\%$ |
| 1.40 | 0.0270 | $-5.39\%$ |
| **1.68 (canonical)** | **0.0324** | **$-6.47\%$** |
| 2.00 | 0.0385 | $-7.71\%$ |
| 2.50 | 0.0482 | $-9.63\%$ |

Variation of $\sigma_{K3}$ by factor 2.5 produces variation of softening by factor 2.5. To match empirical $-31.8\%$ at $N_\alpha = 8$ would require $\sigma_{K3} \approx 8.3$ fm — physically unreasonable (alpha overlap scale is 1.68 fm, alpha-alpha contact distance is 2.37 fm; $\sigma_{K3} > 4$ fm means the K$_3$ mode is broader than the cluster itself). **No physically reasonable $\sigma_{K3}$ closes the magnitude gap.**

The pattern (monotonic, peaking at $N_\alpha = 4$) is unchanged across $\sigma_{K3}$ values — only an overall scale factor.

---

## §6. Programme implications

### §6.1 Verdict on uniform-scaling model (a)

**Model (a) — uniform-scaling radial-breathing — is RULED OUT** as a complete R2 closure mechanism on three independent grounds:

1. **Wrong magnitude.** Factor 7 undershoot at the empirical peak ($N_\alpha = 10$). No physically reasonable $\sigma_{K3}$ closes the gap.
2. **Wrong pattern.** Model is monotonically decreasing in $N_\alpha$; empirical is U-shaped with mid-range peak. The model lacks shape-class selection.
3. **Wrong sign at endpoints.** Empirical $N_\alpha = 4, 12$ require near-zero or compressive change; model predicts substantial softening at both endpoints. The simplest realization predicts the LARGEST softening at the tetrahedron, where empirically there is essentially no anomaly.

This is the **sixth programme-level negative-result demonstration** in the OPEN-SS-35 closure programme:

| # | Route/Path | Session | Reason ruled out |
|---|---|---|---|
| 1 | Route D (lattice-shell counting) | Session 5 Phase 2 | distance shells don't match magic numbers |
| 2 | Route B-γ (K$_3$-mode phase coupling) | Session 7 Phase 2 | $V_{\rm SO}/\hbar\omega \sim 10^{-3}$, magnitude insufficient |
| 3 | Route 1b ($V_{\rm SO}$ refinement) | Session 10 | saturates at $V_{\rm SO}/\hbar\omega \approx 0.11$ |
| 4 | Path (i) cluster-surface Thomas | Session 11 Phase 1 | $f_{\rm SO}(r)$ peaks at center, not surface |
| 5 | R1 ($R_\alpha$ scale-dependence) | Session 12 | wrong sign + U-shape + decoupled from gap strength |
| 6 | **Phase 2 model (a) uniform breathing** | **Session 13 Phase 2** | wrong magnitude + wrong pattern + wrong endpoint signs |

### §6.2 Verdict on the unification hypothesis

**The unification hypothesis itself is NOT ruled out.** Phase 1 §6.3 already anticipated this branch: "Phase 2 should start with (a) and revisit (b) if the simple scaling does not produce the observed selection rules." The selection-rule structure of the empirical U-shape is precisely the kind of pattern that uniform scaling cannot produce — it is shape-class-driven, and shape-class is by definition orthogonal to a single isotropic dof. The empirically observed pattern (J-solid mid-range overshoot, regular-polytope endpoints fine) has the structural signature of a mode that activates only at axially-non-trivial cluster shapes, which is precisely what model (b) is designed to capture.

The OPEN-SS-32 mechanism itself selects for J-solid belt/seam structure (SS-7 §2.1 facet (c)). For the unification hypothesis to hold, the breathing-mode analog must also select for belt/seam structure. Model (a)'s isotropic dof is incompatible with this selection by construction.

### §6.3 Verdict on R2

R2 (cluster-scale vs alpha-scale mean field interpretation, Session 7 sketch §3.3) was Session 12's only remaining A-scaling closure candidate. Phase 2 has **substantively weakened R2**: the simplest plausible mechanism for R2 doesn't work, and the magnitude shortfall (factor 7) is large enough that even significant refinements of model (a) (e.g., promoting $\sigma_{K3}$ to a soft $N_\alpha$-dependent quantity, adding subleading mean-field contributions) cannot close the gap by themselves.

R2 is not closed. R2 is not yet ruled out — model (b) (symmetry-resolved breathing) remains untested, and a successful model-(b) computation would close R2. But the simplest realization fails badly, which sharpens the bar for a successful (b).

### §6.4 OPEN-SS-35 closure trajectory

Six programme-level stages preserved. Phase 2 refines stage (vi) by ruling out one realization of R2 closure (uniform breathing); does not advance to a new programme-level stage. First qualitative cross-paradigm consilience claim (Session 9) intact. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.

### §6.5 OPEN-ORG-012 status

The Session 12 anti-trigger continues to apply. §7 of SS-9 v0.3 is shifting (Phase 2 has added a substantial finding to §7 worth integrating). Phase 3 (model b) work would add more. .tex conversion remains deferred until OPEN-SS-32 ↔ U-shape investigation reaches a stable state.

---

## §7. Forward-looking pointers for Session 14

**Priority 1:** Phase 3 — symmetry-resolved breathing decomposition (model (b) of Phase 1 §6.3 step 1). Project the $\lambda$-uniform mode onto irreducible representations of each cluster's point group, identify the belt-localized modes for J-solid deltahedra ($D_{3h}$, $D_{5h}$, $D_{2d}$, $D_{3h}$, $D_{4d}$ at $N_\alpha = 5, 7, 8, 9, 10$), compute their frequencies and zero-point amplitudes separately, and check whether the belt modes alone (excluding the totally-symmetric $A_1$ uniform-scaling mode that Phase 2 just computed) give the U-shape. Multi-session by scope (3–5 sessions). Discriminating tests: pattern (U-shape vs monotonic), magnitude, $N_\alpha = 6$ selection rule (under model (b), $O_h$ symmetry should give zero or near-zero belt-localized mode, distinguishing Reading A from B/C).

**Priority 2 (deferred):** R2 and OPEN-SS-32 attenuation factor derivation. If Phase 3 succeeds, the OPEN-SS-32 mechanism itself can be derived from the same belt-mode framework.

**Priority 3 (parallel, lower priority):** OPEN-SS-16 Layer B closure work. Deepest open problem; deferred.

**Priority 4 (parallel, registered for future session):** Reframing question — whether the U-shape diagnostic has a contribution from the empirical $41/A^{1/3}$ formula being itself an extrapolation at small $A$ (Reading B). The empirical Bohr-Mottelson formula is calibrated against specific data; at $A = 16$ ($N_\alpha = 4$) and $A = 24$ ($N_\alpha = 6$) the calibration may not apply directly. A literature check on the specific $A$-range over which $41/A^{1/3}$ is empirically valid would partially discriminate Reading B from Readings A and C, complementing the Phase 3 mechanistic test.

**Anti-priority:** Do not initiate the SS-9 v0.3 → v0.1 .tex conversion (OPEN-ORG-012) until Phase 3 returns a result. §7 of SS-9 v0.3 will continue to shift as model (b) is developed.

---

## §8. Summary

Phase 2 single-session-tractable computation of the uniform-scaling radial-breathing-mode of J-solid deltahedra is **complete and produces a substantive negative result.** Model (a), the simplest realization of the unification hypothesis registered in Phase 1, **fails on three independent grounds**: factor 7 magnitude undershoot at the empirical U-shape peak, monotonic-vs-U-shape pattern mismatch, and endpoint-sign mismatch at $N_\alpha = 4, 12$.

The unification hypothesis is **not refuted** — only its simplest realization is. Phase 1 §6.3 explicitly registered model (b) (symmetry-resolved breathing decomposition) as the natural fallback if model (a) failed; we are now at that branch. Model (b) is multi-session work and will be Session 14's Priority 1.

**Sixth programme-level negative-result demonstration** in the OPEN-SS-35 closure programme. R2 substantively weakened but not closed. **OPEN-SS-32 ↔ U-shape investigation status:** "Phase 1 prior-art read complete; Phase 2 single-session-tractable" (Session 13 Phase 1) → "**Phase 2 uniform-scaling model (a) ruled out; Phase 3 symmetry-resolved decomposition (model b) registered as Priority 1 multi-session work**" (this Session 13 Phase 2).

Six programme-level stages of OPEN-SS-35 closure programme preserved. First qualitative cross-paradigm consilience claim (Session 9) intact. R1 ruled-out (Session 12) intact. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.

---

*Phase 2 reproducible computation per Phase 1 §6.3 work plan. Substantive negative result on the simplest realization of the unification hypothesis. Sets up Phase 3 (model b, symmetry-resolved breathing decomposition) as Session 14 Priority 1. OPEN-SS-32 ↔ U-shape investigation: Phase 2 ruled out a specific realization but did not close OPEN-SS-32 or close R2; investigation continues.*
