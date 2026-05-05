# OPEN-SS-32 ↔ U-shape Unification — Phase 3 Phase A: Full-Hessian Decomposition Gives FLAT Pattern (Session 13 Phase 3A)

**Date:** 4 May 2026 (Session 13, Phase 3A — same context window as Phase 1 + Phase 2)
**Purpose:** Execute Phase 3 Phase A: full $3N - 6$ vibrational-mode Hessian decomposition of the K$_3$ Gaussian pair-potential at each canonical alpha-chain deltahedron's equilibrium configuration, summed over ALL modes. Test whether enriching the mode basis from Phase 2's single uniform-scaling dof to the full vibrational space reproduces the empirical U-shape.

**Companion files:**
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase2.md` (Phase 2 model (a) ruled out)
- `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase3a.py` (this Phase 3A reproducible computation)
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a_Ascaling_R1_RULED_OUT.md` §3 (Session 12 inversion table; the empirical U-shape data)

**Net programme effect:** **Phase 3 Phase A "naive full-Hessian" approach RULED OUT** as a complete R2 closure mechanism on three structural grounds — flat pattern across all 8 deltahedra (no shape-class selection), magnitude factor 2.5 OVERSHOOT at canonical $\sigma_{K3}$ (vs Phase 2's factor 7 undershoot), and identical $N_\alpha = 6$ vs $N_\alpha = 8$ behavior. **Seventh programme-level negative-result demonstration** in OPEN-SS-35 closure programme. **But also a constructive benchmark:** the empirical magnitude (-33.6% at peak) lies BETWEEN Phase 2 (lower bound, -4.6%) and Phase 3A (upper bound, -85%), demonstrating that the full mode space contains sufficient zero-point fluctuation to reach empirical levels if appropriately selected. The unification hypothesis is now sharply constrained: neither single-mode (Phase 2) nor all-modes (Phase 3A) gives shape-class selection; Phase 3 Phase B — IRREP-selective decomposition projecting onto belt-localized modes — is the only remaining candidate. R2 is severely weakened but not formally closed pending Phase 3B test. Six programme-level stages preserved. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.

---

## §1. Strategy

Phase 2 ruled out model (a) — uniform scaling of all vertices, single dof — on three independent grounds (wrong magnitude, wrong pattern, wrong endpoint signs). The Phase 1 §6.3 step 1 work plan then specified model (b), symmetry-resolved breathing modes, as the natural fallback. Phase 3 Phase A is the **first sub-step of model (b)**: enrich the mode basis from a single uniform-scaling dof to the full vibrational mode space ($3N - 6$ modes per polytope), summed over all modes. This is the simplest enrichment of model (a) — model (b)'s zeroth-order realization, before IRREP-selective subset selection.

The full-Hessian decomposition allows arbitrary vertex displacement patterns and uses each mode's own zero-point amplitude. If the empirical U-shape comes from a richer mode space than Phase 2 admits, it should appear here. If it doesn't, the mechanism must be more selective than "all modes count equally."

Three diagnostics:
1. **Magnitude.** Does the full mode space contain sufficient zero-point fluctuation to reach empirical magnitudes (which Phase 2 missed by factor 7)?
2. **Pattern.** Does the full mode space produce the U-shape (J-solid mid-range overshoot, regular-polytope endpoints fine), where Phase 2 produced monotonic decrease?
3. **N$_\alpha$ = 6 selection rule test.** Does the full mode space discriminate $O_h$ symmetry (octahedron, no belt) from $D_{2d}$ (snub disphenoid, belt-active)?

---

## §2. Model and computation

### §2.1 The K$_3$ Gaussian pair-potential Hessian

Each polytope edge $(i, j)$ at equilibrium $|R_i - R_j| = R_\alpha$ contributes a Gaussian pair potential $V_{\rm pair}(r) = -B_{\rm pair} \exp(-(r - R_\alpha)^2/(2\sigma_{K3}^2))$. At equilibrium: $V_{\rm pair}(R_\alpha) = -B_{\rm pair}$ (recovers SS-7 LO), $V_{\rm pair}'(R_\alpha) = 0$ (Gaussian peak, no tension), $V_{\rm pair}''(R_\alpha) = B_{\rm pair}/\sigma_{K3}^2$ (spring constant per edge).

The Hessian of the total energy with respect to all $3N$ vertex coordinates is the standard "spring-network" Hessian, where each edge $(i, j)$ contributes a 6×6 block coupled by the unit vector $\hat n_{ij} = (R_i - R_j)/R_\alpha$:

$$H_{(i,a),(i,b)} \mathrel{+}= k_{\rm edge} \cdot \hat n_{ij,a} \hat n_{ij,b} \qquad H_{(j,a),(j,b)} \mathrel{+}= k_{\rm edge} \cdot \hat n_{ij,a} \hat n_{ij,b}$$
$$H_{(i,a),(j,b)} \mathrel{-}= k_{\rm edge} \cdot \hat n_{ij,a} \hat n_{ij,b} \qquad H_{(j,a),(i,b)} \mathrel{-}= k_{\rm edge} \cdot \hat n_{ij,a} \hat n_{ij,b}$$

with $k_{\rm edge} = B_{\rm pair}/\sigma_{K3}^2 = 2.342/(1.68)^2 = 0.830$ MeV/fm² at canonical $\sigma_{K3} = 1.68$ fm.

### §2.2 Diagonalization and zero-point amplitudes

Diagonalize $H$ to obtain $3N$ eigenvalues $\lambda_k$ and orthonormal eigenvectors $v_k$ (each a $3N$-vector). Six eigenvalues are numerically zero (rigid-body modes — three translations + three rotations); the remaining $3N - 6$ are vibrational modes.

For each non-rigid-body mode $k$ ($\lambda_k > 0$):

$$\hbar\omega_k = \hbar c \sqrt{\frac{\lambda_k}{m_\alpha c^2}} \quad [\text{MeV}]$$

The mode-$k$ contribution to the variance of edge $(i, j)$'s length:

$$\langle (\delta r_{ij})^2 \rangle_k = \frac{\hbar c}{2 \sqrt{m_\alpha c^2 \cdot \lambda_k}} \cdot \left[(v_k(i) - v_k(j)) \cdot \hat n_{ij}\right]^2 \quad [\text{fm}^2]$$

Total mean-square edge-length fluctuation, averaged over edges and summed over all modes:

$$\langle (\delta r)^2 \rangle_{\rm avg} = \frac{1}{|E|} \sum_{\rm edges} \sum_{\rm modes} \langle (\delta r_{ij})^2 \rangle_k$$

Fractional softening of nucleon-orbital $\hbar\omega^*$:

$$\frac{\Delta\hbar\omega^*}{\hbar\omega^*} \approx -\frac{2 \langle (\delta r)^2 \rangle_{\rm avg}}{R_\alpha^2}$$

---

## §3. Results

### §3.1 Eight-row table

Polytope geometries inherited from Phase 2 script. All polytopes scaled to minimum-edge-length $R_\alpha = 2.37$ fm. Computed at canonical $\sigma_{K3} = 1.68$ fm.

| $N_\alpha$ | polytope | sym | $|E|$ | $n_{\rm vib}$ | $\hbar\omega_{\rm min}$ | $\hbar\omega_{\rm max}$ | $\langle(\delta r)^2\rangle$ | predicted softening | empirical req | pred/emp |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | tetrahedron | $T_d$ | 6 | 6 | 2.94 | 5.89 | 2.437 | $-86.77\%$ | $+11.5\%$ | $-7.54$ |
| 5 | trig. bipyramid | $D_{3h}$ | 9 | 9 | 2.29 | 6.08 | 2.407 | $-85.71\%$ | $-12.2\%$ | $7.05$ |
| 6 | octahedron | $O_h$ | 12 | 12 | 2.94 | 5.89 | 2.430 | $-86.53\%$ | $-21.3\%$ | $4.07$ |
| 7 | pent. bipyramid | $D_{5h}$ | 15 | 15 | 2.12 | 5.81 | 2.394 | $-85.22\%$ | $-29.5\%$ | $2.89$ |
| 8 | snub disphenoid | $D_{2d}$ | 18 | 18 | 2.03 | 5.89 | 2.400 | $-85.47\%$ | $-31.8\%$ | $2.69$ |
| 9 | triaug. tri. prism | $D_{3h}$ | 21 | 21 | 2.18 | 5.78 | 2.397 | $-85.35\%$ | $-33.1\%$ | $2.58$ |
| 10 | gyroel. sq. bipyr. | $D_{4d}$ | 24 | 24 | 2.10 | 5.86 | 2.391 | $-85.15\%$ | $-33.6\%$ | $2.54$ |
| 12 | icosahedron | $I_h$ | 30 | 30 | 2.25 | 5.45 | 2.385 | $-84.92\%$ | $+1.4\%$ | $-60.02$ |

Predicted softening is essentially constant at **-85±1%** across all eight polytopes. The vibrational frequency spectrum is also similar: $\hbar\omega$ ranges from ~2 MeV (lowest mode, typically a soft tilt) to ~6 MeV (highest mode), across all polytopes.

### §3.2 Pattern is FLAT (not U-shape, not monotonic)

Phase 2 model (a) gave a monotonically decreasing softening with $N_\alpha$. Phase 3 Phase A gives an approximately constant softening with $N_\alpha$:

$$\text{N: } 4, 5, 6, 7, 8, 9, 10, 12 \implies \text{softening: } -86.8, -85.7, -86.5, -85.2, -85.5, -85.4, -85.2, -84.9 \text{ (\%)}$$

Variation across the entire range is only **2%** (-84.9% to -86.8%) — essentially no $N_\alpha$ dependence. Empirical varies from $+12\%$ to $-34\%$ (46% range). **The model and empirical have qualitatively different shape signatures.**

### §3.3 Magnitude: factor 2.5 overshoot at empirical peak (vs Phase 2's factor 7 undershoot)

At empirical U-shape peak ($N_\alpha = 10$, requires $-33.6\%$ softening), Phase 3 Phase A gives $-85.15\%$ — **factor 2.5 too large**. Phase 2 model (a) at the same point gave $-4.57\%$ (factor 7 too small).

Improvement factor Phase 3A / Phase 2: 18.6× (Phase 3A produces 18.6× more softening than Phase 2 at $N_\alpha = 10$). This is the magnitude of the "all-modes-vs-uniform-only" enrichment.

### §3.4 $N_\alpha = 6$ selection-rule test

| polytope | sym | softening |
|---|---|---|
| octahedron | $O_h$ (no belt) | $-86.53\%$ |
| snub disphenoid | $D_{2d}$ (belt-active) | $-85.47\%$ |

Ratio $N=6/N=8$: **1.012**. Octahedron and snub disphenoid produce essentially identical full-Hessian softening despite their structurally different symmetry classes. **Naive full-Hessian has no shape-class selection** — same failure mode as Phase 2 model (a), but for a different structural reason.

---

## §4. Structural interpretation

### §4.1 Why the pattern is flat

The per-edge zero-point variance for an isolated alpha pair (only one pair, no cluster context) is

$$\langle(\delta r)^2\rangle_{\rm isolated} = \frac{\hbar c}{2 \sqrt{m_\alpha c^2 \cdot k_{\rm edge}}} \cdot \frac{1}{\sqrt{2}} \cdot 2 \approx 2.51 \text{ fm}^2$$

at $k_{\rm edge} = 0.830$ MeV/fm². The reduced-mass factor (m_α/2 for two-body) and the pair-counting cancel out approximately to give this value.

The full-Hessian computation gives per-edge variance ~2.4 fm² across all polytopes — only ~2% smaller than the isolated-pair value. **Edges are nearly independent in this potential.** Vertex-coupling through shared edges reduces zero-point fluctuation by only ~2% relative to isolated pairs, regardless of cluster topology, because the K$_3$ Gaussian pair-potential at $\sigma_{K3} = 1.68$ fm is too weak to produce strong inter-edge correlations.

Structural reading: in the canonical $\sigma_{K3}$, the system is in a "weakly-coupled-edges" regime where the cluster is barely bound against zero-point fluctuations. The empirical behavior (well-defined alpha-alpha separations at ~2.37 fm) requires either a stiffer K$_3$ mode (smaller $\sigma_{K3}$) or additional binding beyond the simple Gaussian model.

### §4.2 Phase 2 vs Phase 3A as bounds on model (b)

Phase 2 model (a) is the **lower bound** — only one collective coordinate (uniform scaling, the totally-symmetric $A_1$ mode); all other zero-point fluctuation is artificially set to zero.

Phase 3 Phase A is the **upper bound** — every vibrational mode contributes, including modes whose effect on the K$_3$ mean field is incomplete.

Empirical $-33.6\%$ at peak lies cleanly between Phase 2's $-4.57\%$ and Phase 3A's $-85\%$. **The full mode space contains enough zero-point fluctuation to reach empirical magnitudes** if approximately 40% of the available mode-space-summed variance contributes. The remaining 60% must be modes that DON'T affect the K$_3$ mean field at the centroid (e.g., shape-modes that preserve mean edge length).

This is constructive: **the question for Phase 3 Phase B is selection, not strength**. The mode space contains the necessary fluctuation. Phase 3 Phase A's failure is in HOW the modes are summed (equal-weighted, no shape selection), not in WHAT modes are available.

### §4.3 Why model (b)-naive lacks shape-class selection

Naive full-Hessian counts all modes, weighted by their own zero-point amplitudes. Soft modes (low $\omega$) contribute most. Across all eight deltahedra, the LOWEST-frequency modes are similarly soft (~2 MeV) — they correspond to the "easy" deformations that any deltahedron has (rocking of one vertex relative to neighbors, etc.). These soft modes contribute most of the per-edge variance, and they're shape-class-insensitive because they're local rather than collective.

To get U-shape selection, the relevant modes must be **collective, belt-localized, and present only in certain symmetry classes**. These are the SS-7 OPEN-SS-32 oblate-deformation modes. In group-theoretic terms: the breathing dof's projection onto the belt-deformation IRREP of each cluster's point group (a non-trivial IRREP that exists for $D_{nh}, D_{nd}$ but is suppressed for $T_d, O_h, I_h$).

Phase 3 Phase A summed over all IRREPs equally. Phase 3 Phase B must restrict to the belt-IRREP subset.

---

## §5. Programme implications

### §5.1 Verdict on Phase 3 Phase A

**Phase 3 Phase A — naive full-Hessian sum-over-all-modes — is RULED OUT** as a complete R2 closure mechanism on three independent grounds: flat pattern across all 8 deltahedra (no shape selection), magnitude factor 2.5 overshoot at empirical peak, identical $N_\alpha = 6$ vs $N_\alpha = 8$ behavior.

This is the **seventh programme-level negative-result demonstration** in the OPEN-SS-35 closure programme:

| # | Route/Path | Session | Reason ruled out |
|---|---|---|---|
| 1 | Route D (lattice-shell counting) | Session 5 Phase 2 | distance shells don't match magic numbers |
| 2 | Route B-γ (K$_3$-mode phase coupling) | Session 7 Phase 2 | $V_{\rm SO}/\hbar\omega \sim 10^{-3}$, magnitude insufficient |
| 3 | Route 1b ($V_{\rm SO}$ refinement) | Session 10 | saturates at $V_{\rm SO}/\hbar\omega \approx 0.11$ |
| 4 | Path (i) cluster-surface Thomas | Session 11 Phase 1 | $f_{\rm SO}(r)$ peaks at center, not surface |
| 5 | R1 ($R_\alpha$ scale-dependence) | Session 12 | wrong sign + U-shape + decoupled from gap strength |
| 6 | Phase 2 model (a) uniform breathing | Session 13 Phase 2 | wrong magnitude + wrong pattern + wrong endpoint signs |
| 7 | **Phase 3A naive full-Hessian** | **Session 13 Phase 3A** | flat pattern + wrong magnitude + no shape selection |

### §5.2 Constructive content of Phase 3 Phase A

Phase 3 Phase A is also a **useful benchmark**:

- Establishes that the **full mode space contains sufficient zero-point fluctuation** to reach empirical U-shape magnitudes. The empirical $-33.6\%$ at peak is $\sim 40\%$ of the full-mode-space upper bound $-85\%$.
- Establishes that **shape-class selection is the bottleneck**, not magnitude. The mode space is rich enough; the selection rule needs to be discovered.
- Establishes that **per-edge near-independence** is a structural feature of the canonical K$_3$ potential at $\sigma_{K3} = 1.68$ fm — vertex-coupling reduces fluctuations by only ~2% relative to isolated pairs.
- **Sharply constrains Phase 3 Phase B**: the IRREP-selective subset must produce ~40% of the full-mode-space softening at J-solid mid-range polytopes ($N_\alpha = 7-10$) and near-zero at regular polytopes ($N_\alpha = 4, 12$).

### §5.3 Verdict on R2 and the unification hypothesis

R2 (cluster-scale vs alpha-scale mean field interpretation) is now **severely weakened** but not formally closed. Two extreme realizations of the breathing mechanism (uniform-only and all-modes) both fail. R2 closure now depends on the IRREP-selective subset (Phase 3 Phase B) producing the required shape-class pattern.

The unification hypothesis itself is still not refuted — Phase 3 Phase B remains untested — but the constraint it must satisfy is now sharp:
- Magnitude: produce $-33.6\%$ softening at $N_\alpha = 10$ (not $-85\%$)
- Shape selection: produce near-zero softening at $N_\alpha = 4$ ($T_d$) and $N_\alpha = 12$ ($I_h$); peak softening at $N_\alpha = 8-10$ (J-solid mid-range)
- $N_\alpha = 6$ test: produce significantly less softening at the octahedron ($O_h$) than at the snub disphenoid ($D_{2d}$) — discriminating Reading A from B/C

If Phase 3 Phase B fails to produce these patterns, R2 (and the unification hypothesis at the canonical $\sigma_{K3}$) would be ruled out.

### §5.4 OPEN-SS-35 closure trajectory

Six programme-level stages preserved. Phase 3 Phase A refines stage (vi) by ruling out a second realization of R2 closure (naive full-Hessian); does not advance to a new programme-level stage. First qualitative cross-paradigm consilience claim (Session 9) intact. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.

### §5.5 OPEN-ORG-012 status

The Session 12 anti-trigger continues to apply. §7 of SS-9 v0.3 has now shifted twice in this session (Phase 2 negative result and Phase 3A negative result with constructive benchmark). .tex conversion remains deferred.

---

## §6. Forward-looking pointers

**Priority 1 (Session 14):** Phase 3 Phase B — IRREP-selective decomposition. For each cluster's point group, project the Hessian eigenvectors onto the belt-deformation IRREP. Sum zero-point variance contributions only from belt-localized modes. Test whether this produces (a) approximately $-33\%$ softening at $N_\alpha = 8-10$, (b) near-zero softening at $N_\alpha = 4$ and $12$, (c) substantially less at $N_\alpha = 6$ ($O_h$) than at $N_\alpha = 8$ ($D_{2d}$). Multi-session by scope; Phase 3 Phase B is the central test.

**Priority 2 (deferred):** OPEN-SS-32 attenuation-factor derivation; reading B literature check.

**Priority 3 (parallel):** OPEN-SS-16 Layer B closure work.

**Anti-priority:** SS-9 v0.3 → v0.1 .tex conversion deferred until Phase 3 Phase B completes.

---

## §7. Summary

Phase 3 Phase A — full $3N - 6$ vibrational-mode Hessian decomposition of the K$_3$ Gaussian pair-potential, summed over all modes — is **complete and produces a substantive negative result with constructive benchmark content**. The naive sum-over-all-modes approach is RULED OUT as an R2 closure mechanism on three structural grounds (flat pattern, factor 2.5 magnitude overshoot, no shape selection). **Seventh programme-level negative-result demonstration.**

But Phase 3 Phase A also establishes the **upper-bound benchmark**: empirical $-33.6\%$ softening at peak is $\sim 40\%$ of the full-mode-space upper bound $-85\%$. The mode space is rich enough; the question is selection, not strength. Phase 3 Phase B (IRREP-selective decomposition with belt-mode projection) is now sharply constrained — must produce $\sim 40\%$ of full-mode-space softening at J-solid mid-range polytopes and near-zero at regular polytopes.

R2 is severely weakened — two of three plausible realizations of the unification hypothesis (uniform-only Phase 2; all-modes Phase 3A) have failed — but not formally closed pending Phase 3 Phase B test. The unification hypothesis itself is now under stronger pressure but remains technically open.

Six programme-level stages preserved. First qualitative cross-paradigm consilience claim (Session 9) intact. Pattern 6 K$_3$ scale-recurrence at 7 confirmed instances unchanged. R1 ruled-out (Session 12) intact.

---

*Phase 3 Phase A reproducible computation. Substantive negative result on naive full-Hessian sum-over-all-modes. Establishes upper-bound benchmark for Phase 3 Phase B. Phase 3 Phase B (IRREP-selective decomposition) registered as Session 14 Priority 1 with sharply constrained quantitative targets.*
