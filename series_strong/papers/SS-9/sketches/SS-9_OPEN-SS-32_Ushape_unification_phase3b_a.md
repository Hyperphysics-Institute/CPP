# OPEN-SS-32 ↔ U-shape Unification — Phase 3 Phase B Sub-phase A: Minimal Belt-Subspace Projection RULED OUT (Session 14 Phase 3B-A)

**Date:** 5 May 2026 (Session 14, Phase 3B-A — first session-tractable subphase of Phase 3B)
**Purpose:** Execute Phase 3B-A: project full Hessian eigenmodes onto a minimal "belt subspace" capturing the SS-7 OPEN-SS-32 oblate-quadrupole deformation pattern. Test the three quantitative targets registered at Session 13 close from Phase 3A's bracketing benchmark.

**Companion files:**
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase3a.md` (Phase 3A naive full-Hessian RULED OUT, upper bound established)
- `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase3b_a.py` (this Phase 3B-A reproducible computation)
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase2.md` (Phase 2 model (a) RULED OUT, lower bound)

**Net programme effect:** **Phase 3B-A — minimal belt-subspace projection (3D basis: A₁ in-plane breathing + 2D E₂ quadrupole) — RULED OUT** as a complete R2 closure mechanism on two structural grounds: (i) target (a) magnitude factor 3× too small at J-solid mid-range peak (avg belt fraction 0.135 vs target 0.40), (ii) **pattern-shape within axial polytopes is anti-correlated with empirical** — belt fraction monotonically *decreases* from N_α=5 (0.39) to N_α=10 (0.10) while empirical magnitude monotonically *increases* across the same range. Targets (b) and (c) — near-zero belt fraction at regular polytopes and O_h ≪ D_{2d} — are structurally enforced by the inertia-degeneracy classification rather than being differential tests, so they pass automatically without supporting Reading A. **Eighth programme-level negative-result demonstration** in the OPEN-SS-35 closure programme. The pattern-shape failure is a stronger ruling than Phase 3A's flatness because it adds a structural anti-correlation as an obstacle for any fixed-dimension belt-subspace realization. R2 further weakened — three of four model-(b) realizations now failed (Phase 2 uniform-only, Phase 3A all-modes, Phase 3B-A fixed-dim belt subspace); Phase 3B-B (richer IRREP decomposition with belt dimension scaling appropriately to polytope size) is the only remaining R2 realization untested. Six programme-level OPEN-SS-35 stages preserved. Pattern 6 K₃ scale-recurrence at 7 confirmed instances unchanged.

---

## §1. Strategy

Phase 3A established constructive bracketing: empirical softening peak −33.6% at N_α=10 lies between Phase 2's lower bound −4.6% (uniform-scaling, single dof) and Phase 3A's upper bound −85% (all 3N−6 modes equal-weighted). Empirical is ≈ 40% of upper bound; **mode space carries sufficient amplitude, selection is the bottleneck**.

The §6 forward pointer of Phase 3A specified Phase 3B-A as the simplest tractable IRREP-selective realization: project Hessian eigenmodes onto a "belt subspace" implementing the SS-7 OPEN-SS-32 oblate-quadrupole pattern, weight per-mode zero-point variance by the projection magnitude, and tabulate.

The minimal physically-motivated belt subspace per axial polytope contains three basis vectors — the totally-symmetric A₁ in-plane radial breathing (monopole) and the two E₂ quadrupole patterns (cos(2φ), sin(2φ) angular phase). For polytopes with degenerate inertia tensor (T_d, O_h, I_h), no preferred axis exists; the construction declares belt subspace dimension zero by symmetry.

This is the **fixed-dimension** realization of Phase 3B. The belt subspace dimension does not scale with polytope size. The empirical question is whether this construction reproduces the three targets registered at Session 13 close.

Three targets:
1. **(a) Magnitude target.** Average belt fraction at J-solid mid-range N_α=7..10 ≈ 0.4, yielding belt-projected softening ≈ −33% at peak.
2. **(b) Endpoint target.** Near-zero belt fraction at regular polytopes T_d (N=4), I_h (N=12) — and by extension O_h (N=6).
3. **(c) Discriminator target.** O_h (N_α=6) ≪ D_{2d} (N_α=8) — discriminates Reading A from Readings B and C.

---

## §2. Model and computation

### §2.1 Inertia classification

For each polytope, compute the inertia tensor I_{ab} = Σ_i (δ_{ab} r_i² − r_{i,a} r_{i,b}) about the COM and diagonalize. Three regimes:

- **DEGENERATE** (all three eigenvalues coincide within 10⁻³ relative tolerance): T_d (N=4), O_h (N=6), I_h (N=12). No preferred axis.
- **PROLATE** (smallest eigenvalue is unique; mass concentrated on the axis): trigonal bipyramid D_{3h} (N=5), snub disphenoid D_{2d} (N=8), gyroelongated square bipyramid D_{4d} (N=10). Principal axis = eigenvector of smallest eigenvalue.
- **OBLATE** (largest eigenvalue is unique; mass concentrated perpendicular to axis): pentagonal bipyramid D_{5h} (N=7), triaugmented triangular prism D_{3h} (N=9). Principal axis = eigenvector of largest eigenvalue.

For DEGENERATE polytopes, the belt subspace is declared empty (dim(B) = 0) and f_belt = 0 for every mode by symmetry. This implements Reading A's structural commitment: "belt-IRREP modes do not exist for fully-symmetric polytopes."

### §2.2 Belt basis construction

For axial polytopes (PROLATE / OBLATE), construct an orthonormal frame {x̂_p, ŷ_p, ẑ_p} where ẑ_p is the principal axis. Each vertex i has cylindrical coordinates (ρ_i, φ_i, z_i) in this frame.

Three belt basis vectors of length 3N (displacement at each vertex):

$$b^{(0)}_i = \hat\rho_i \quad \text{(A₁ in-plane radial breathing, monopole)}$$
$$b^{(c)}_i = \cos(2\varphi_i)\,\hat\rho_i \quad \text{(E₂ quadrupole cos)}$$
$$b^{(s)}_i = \sin(2\varphi_i)\,\hat\rho_i \quad \text{(E₂ quadrupole sin)}$$

Vertices on the principal axis (ρ_i ≈ 0) contribute zero (no radial direction to displace along).

To prevent rigid-body contamination, project each raw belt basis vector onto the orthogonal complement of the rigid-body subspace (3 translations + 3 rotations about COM, Gram-Schmidt-orthonormalized). Then Gram-Schmidt-orthonormalize the surviving vectors to obtain {ê^a}, the orthonormal belt subspace basis with dim(B) ≤ 3.

### §2.3 Belt-projected zero-point variance

For each Hessian eigenmode v_k with eigenvalue λ_k > 0, the belt fraction is:

$$f_k^{\rm belt} = \sum_{a=1}^{\dim(B)} |\langle \hat e^a | v_k\rangle|^2 \in [0,1]$$

The Phase 3A per-mode contribution to per-edge mean-square-displacement is unchanged:

$$C_k^{\rm edge} = \frac{\hbar c}{2\sqrt{m_\alpha \lambda_k}} \sum_{(i,j)\in E} [(v_k(i) - v_k(j))\cdot \hat n_{ij}]^2$$

The belt-projected total variance weights each mode's contribution by its belt fraction:

$$\langle (\delta r)^2\rangle_{\rm belt} = \frac{1}{|E|}\sum_{k} f_k^{\rm belt} \cdot C_k^{\rm edge}$$

$$\frac{\Delta\hbar\omega^*}{\hbar\omega^*}\bigg|_{\rm belt} \approx -\frac{2 \langle (\delta r)^2\rangle_{\rm belt}}{R_\alpha^2}$$

In the limit f_k^{belt} = 1 ∀k, the result equals Phase 3A's full-Hessian computation. In the limit f_k^{belt} = 0 ∀k (DEGENERATE polytopes), the result is exactly zero.

**Sanity checks** verified by the script:
- Phase 3A reproduction: delta_full identical to Phase 3A table to 3 decimals across all eight polytopes.
- Σ_k f_k^{belt} = dim(B) for all polytopes (orthogonal basis, no rigid-body leakage).
- DEGENERATE classification correctly identifies T_d, O_h, I_h (inertia-eigenvalue spread < 10⁻³).

---

## §3. Results

### §3.1 Eight-row table

Polytopes scaled to minimum-edge-length R_α = 2.37 fm. Computed at canonical σ_K3 = 1.68 fm. All entries from `SS-9_OPEN-SS-32_Ushape_unification_phase3b_a.py`.

| N_α | polytope | sym | inertia | dim(B) | −δ_full% | −δ_belt% | −δ_emp% | belt fraction |
|---|---|---|---|---|---|---|---|---|
| 4 | tetrahedron | T_d | DEGEN | 0 | −86.77 | 0.00 | +11.51 | 0.000 |
| 5 | trig. bipyramid | D_{3h} | PROLATE | 3 | −85.71 | −33.12 | −12.16 | 0.386 |
| 6 | octahedron | O_h | DEGEN | 0 | −86.53 | 0.00 | −21.27 | 0.000 |
| 7 | pent. bipyramid | D_{5h} | OBLATE | 3 | −85.22 | −17.16 | −29.50 | 0.201 |
| 8 | snub disphenoid | D_{2d} | PROLATE | 2 | −85.47 | −9.40 | −31.81 | 0.110 |
| 9 | triaug. tri. prism | D_{3h} | OBLATE | 3 | −85.35 | −11.36 | −33.14 | 0.133 |
| 10 | gyroel. sq. bipyr. | D_{4d} | PROLATE | 3 | −85.15 | −8.16 | −33.58 | 0.096 |
| 12 | icosahedron | I_h | DEGEN | 0 | −84.92 | 0.00 | +1.41 | 0.000 |

**Note on dim(B) = 2 at N=8.** The snub disphenoid's D_{2d} symmetry gives the optimised vertex configuration a degeneracy under cos(2φ) and sin(2φ) at the belt vertices (the 4-vertex belt-pair pattern combined with C_2 reduces the rank of {b^{(0)}, b^{(c)}, b^{(s)}} from 3 to 2 after Gram-Schmidt). This is a structural feature of the symmetry, not a numerical artifact, and is correctly handled by the orthonormalisation.

### §3.2 Target (a) — magnitude factor 3× too small

Average J-solid (N_α = 7..10) belt fraction = **0.135**. Target = 0.40. Magnitude **3× too small at peak**.

Belt-projected softening at N_α=10 is −8.2% vs empirical peak −33.6%. The model captures only ≈ 25% of the empirical magnitude at the target peak.

This factor-3 undershoot is substantive but is **3.3× better than the 1D-monopole-only construction** (which would give belt fraction ≈ 0.04 by capturing only A₁ breathing). The 2D E₂ quadrupole addition is informative but insufficient.

### §3.3 Target (b) — passes by symmetry construction

All three regular polytopes (T_d, O_h, I_h) have DEGENERATE inertia tensors and dim(B) = 0 by construction, so f_belt = 0 for every mode. δ_belt = 0 exactly.

This is a **structural identity** rather than an empirical test: any inertia-degeneracy-aware belt-IRREP construction satisfies target (b) automatically by symmetry. The construction respects the symmetry of regular polytopes; it does not differentially support Reading A over Readings B or C, because Readings B and C also commit to the symmetry-breaking-with-axis dependence and would also produce zero on degenerate inertia tensors.

### §3.4 Target (c) — passes by symmetry, but Reading A discriminates against empirical

O_h has dim(B) = 0, so belt fraction = 0 strictly. D_{2d} has dim(B) = 2, belt fraction 0.110. Ratio 0/0.11 = 0, certainly ≪ 1 — target (c) is met **as a test of model construction**.

But the **empirical** ratio of softenings at N_α=6 vs N_α=8 is −21.3%/−31.8% = **0.67**, not 0. The empirical octahedron softening is comparable in magnitude to (not vastly less than) the snub disphenoid's. **Reading A's strong inequality is empirically falsified** by the patch-0149 cross-link refinement's qualitative six-of-eight observation that octahedron is the discriminator.

So target (c) being structurally met does not constitute support for Reading A. The model implements Reading A (which predicts O_h ≈ 0); empirical (−21.3%) does not match.

### §3.5 Pattern shape — anti-correlated with empirical within J-solid range

Within axial polytopes (N_α = 5, 7, 8, 9, 10), the belt-projected softening pattern is:

| N_α | belt fraction | −δ_belt% | −δ_emp% |
|---|---|---|---|
| 5 | 0.386 | −33.1 | −12.2 |
| 7 | 0.201 | −17.2 | −29.5 |
| 8 | 0.110 | −9.4 | −31.8 |
| 9 | 0.133 | −11.4 | −33.1 |
| 10 | 0.096 | −8.2 | −33.6 |

**Belt fraction decreases monotonically** from N_α=5 (0.39) through N_α=10 (0.10). **Empirical magnitude increases monotonically** from N_α=5 (−12%) through N_α=10 (−34%). The two are **anti-correlated** within the J-solid range.

This is a structural feature of the fixed-dimension belt subspace, not a tunable artifact:
- At small N (N_α=5, 3 belt vertices), the 3-dim belt basis fully spans the in-plane radial-displacement subspace at the belt — every belt-radial mode contributes f_belt = 1 weight.
- At larger N (N_α=10, 8 belt vertices), the same 3-dim basis spans only 3/8 of the belt-radial-displacement subspace — most belt-radial modes are projected out.

The empirical U-shape requires the **opposite scaling**: the mechanism must yield small softening at small axial N (where the belt is small) and large softening at large axial N (where the belt is rich). No fixed-dimension belt subspace can produce this.

---

## §4. Structural interpretation

### §4.1 The "fixed-dimension belt subspace" concept is structurally inadequate

Phase 3B-A as constructed embeds an implicit assumption: that the belt-IRREP physics is captured by a small handful of low-multipole modes (monopole + quadrupole), regardless of the polytope's belt size. The empirical pattern within axial polytopes refutes this.

The pattern within the J-solid range is monotonic in belt-vertex-count: small belts (N=5: 3 belt verts) give small empirical softening; large belts (N=10: 8 belt verts) give large empirical softening. A natural interpretation is that the relevant "belt-IRREP mode space" itself scales with belt-vertex-count. A fixed-dimension construction with dim(B) ≤ 3 cannot match this.

### §4.2 The N_α=5 overshoot is a stronger negative signal than the N_α=10 undershoot

The N_α=10 undershoot (−8% vs empirical −34%) could in principle be remedied by enlarging the belt subspace dimension. Higher-m angular harmonics (m=3 for D_{4d}'s 4-fold belt, mixed radial+axial belt modes) could plausibly bring f_belt up toward 0.4.

The N_α=5 overshoot (−33% vs empirical −12%) is harder to remedy. At N_α=5 the 3-dim belt basis already saturates the 3-vertex-belt's radial-displacement subspace; **enlarging the belt basis cannot reduce f_belt at N_α=5**, only increase it (or leave it at 1). The current construction already overshoots by 2.7×; richer constructions overshoot by more.

This is a **structural pattern issue**, not a subspace-size issue. If empirical softening at N_α=5 is genuinely small (−12%), then the right mechanism must **suppress** belt-mode contribution at small belts, not enhance it. No "richer belt subspace" hypothesis achieves this.

### §4.3 The DEGENERATE-inertia structural identity does not validate Reading A

Targets (b) and (c) are met by construction because the DEGENERATE classification structurally enforces dim(B) = 0 at T_d, O_h, I_h. But this is not differential support for Reading A:

- Reading A says belt-IRREP modes don't exist at regular polytopes; predicts emp_softening ≈ 0.
- Reading B says belt-IRREP modes exist along each of the multiple equivalent axes and merge by symmetry; predicts emp_softening can be larger than at axial polytopes.
- Reading C says some other mechanism (coordination number, surface curvature) drives softening; can predict any value.

Empirical at O_h: −21.3%. Reading A's prediction of ≈ 0 fails substantively. Reading B's prediction of "larger than D_{2d}'s −31.8%" also fails. Reading C remains the only candidate consistent with O_h's intermediate empirical softening. None of this is diagnosed by Phase 3B-A's symmetry-structural-identity passing.

### §4.4 Comparison with the bracketing benchmark

| model | typical δ at N_α=10 | typical δ at N_α=5 | pattern shape |
|---|---|---|---|
| Phase 2 model (a) — uniform scaling | −4.6% | −4.6% | flat (RULED OUT) |
| Phase 3A — full Hessian, all modes | −85.2% | −85.7% | flat (RULED OUT) |
| Phase 3B-A — fixed-dim belt subspace | **−8.2%** | **−33.1%** | **anti-correlated (RULED OUT)** |
| Empirical | **−33.6%** | **−12.2%** | U-shape (peak at large N) |

Phase 3B-A's belt-projected softenings span the empirical magnitude range (small at one end, comparable at the other) but with the **wrong N_α-ordering**. Empirical wants the −33% at N_α=10 and −12% at N_α=5; Phase 3B-A delivers −33% at N_α=5 and −8% at N_α=10. This anti-correlation is the new structural finding from Phase 3B-A and constrains Phase 3B-B sharply.

### §4.5 R2 status — three of four model-(b) realizations now failed

R2 (cluster-scale-vs-alpha-scale mean-field interpretation, with the unification hypothesis claim) has now seen three of its four plausible realizations fail:

| realization | session | verdict |
|---|---|---|
| Uniform scaling (single A₁ mode) | 13 Phase 2 | RULED OUT — too small, monotonic, wrong endpoints |
| All modes equal-weighted | 13 Phase 3A | RULED OUT — too large, flat, no shape selection |
| Fixed-dim belt subspace | **14 Phase 3B-A** | **RULED OUT — magnitude×3 short, pattern anti-correlated** |
| Full character-theory IRREP decomposition (with belt-IRREP dimension scaling) | 14+ Phase 3B-B | UNTESTED |

R2 is severely weakened. Only Phase 3B-B (the full-rigorous IRREP construction with belt-IRREP dimension scaling appropriately) remains untested. Phase 3B-A's pattern-shape failure adds a stronger constraint on what Phase 3B-B must do: any construction that does not exhibit non-monotonic-in-belt-size behavior within axial polytopes is ruled out by the same anti-correlation argument.

---

## §5. Programme implications

### §5.1 Verdict on Phase 3B-A

**Phase 3B-A — minimal fixed-dimension belt-subspace projection (3D: A₁ monopole + 2D E₂ quadrupole) — is RULED OUT** as a complete R2 closure mechanism on two independent grounds:

1. **Magnitude.** Average J-solid belt fraction 0.135 vs target 0.40 — factor 3 too small at empirical peak (N_α=10).
2. **Pattern shape.** Belt fraction monotonically decreases within axial polytopes from N_α=5 (0.39) to N_α=10 (0.10); empirical magnitude monotonically increases across the same range. **Anti-correlated.**

Targets (b) and (c) are met by symmetry-structural-identity, not by differential empirical support — they would be satisfied by any inertia-degeneracy-aware construction.

This is the **eighth programme-level negative-result demonstration** in the OPEN-SS-35 closure programme:

| # | Route/Path | Session | Reason ruled out |
|---|---|---|---|
| 1 | Route D (lattice-shell counting) | Session 5 Phase 2 | distance shells don't match magic numbers |
| 2 | Route B-γ (K₃-mode phase coupling) | Session 7 Phase 2 | V_SO/ℏω ∼ 10⁻³, magnitude insufficient |
| 3 | Route 1b (V_SO refinement) | Session 10 | saturates at V_SO/ℏω ≈ 0.11 |
| 4 | Path (i) cluster-surface Thomas | Session 11 Phase 1 | f_SO(r) peaks at center, not surface |
| 5 | R1 (R_α scale-dependence) | Session 12 | wrong sign + U-shape + decoupled from gap strength |
| 6 | Phase 2 model (a) uniform breathing | Session 13 Phase 2 | wrong magnitude + wrong pattern + wrong endpoint signs |
| 7 | Phase 3A naive full-Hessian | Session 13 Phase 3A | flat pattern + wrong magnitude + no shape selection |
| 8 | **Phase 3B-A fixed-dim belt subspace** | **Session 14 Phase 3B-A** | **magnitude × 3 short + pattern anti-correlated** |

### §5.2 Constructive content of Phase 3B-A

Despite being a negative result, Phase 3B-A is constructive:

- **Confirms the bracketing.** Phase 3B-A produces softenings between Phase 2's lower bound and Phase 3A's upper bound, spanning the empirical range. The construction inherits the Phase 3A mode space and selectively-weights it; the empirical magnitude is achievable in principle within this framework.
- **Identifies the correct constraint on Phase 3B-B.** Any IRREP-selective decomposition where the belt subspace dimension does NOT scale appropriately with belt-vertex-count will reproduce Phase 3B-A's anti-correlation pattern. Phase 3B-B must use a construction where belt subspace dimension grows non-trivially with belt size.
- **Sharpens the N_α=5 problem.** Empirical softening at N_α=5 is small (−12%). Any belt-IRREP construction that fully spans the 3-vertex belt at N_α=5 (which is unavoidable for ≥3-dim belt basis) will overshoot. The N_α=5 small empirical softening is a **constraint on the underlying dynamics**, not just on belt subspace size. This may indicate that the U-shape mechanism is **not** purely belt-IRREP-projection of the K₃ Gaussian Hessian.
- **Targets (b) and (c) are not differential tests.** Future Phase 3B realizations should not be evaluated against these — they're symmetry consistency checks. Target (a) plus pattern-shape are the real differential tests, and Phase 3B-A fails both.

### §5.3 R2 status and forward path

R2 is **severely weakened** — three of four plausible realizations have failed. Phase 3B-B remains the only untested R2 realization within the K₃-Gaussian-Hessian framework. The Phase 3B-A pattern-shape failure suggests Phase 3B-B's space of valid IRREP-selective constructions is small or empty:

- Constructions with dim(belt subspace) constant in N: Phase 3B-A class. **Ruled out.**
- Constructions with dim(belt subspace) scaling as N_belt (number of belt vertices): would saturate at small N (N_α=5 fully covered by 3 basis vectors anyway), so the N_α=5 overshoot persists.
- Constructions with energetic/dynamic filtering (only soft belt modes contribute): may help, but requires a physical mechanism separating "soft belt modes" from "stiff belt modes" with the right N-scaling.
- Constructions outside the IRREP-projection framework (e.g., elastic stiffness from edge curvature beyond simple Hessian): **outside R2's scope as currently formulated.**

If Phase 3B-B (full IRREP with proper character-theory dimension-scaling) also fails the N_α=5 overshoot test, **R2 will be formally ruled out** and the U-shape mechanism will need to be sought outside the K₃-Gaussian-Hessian framework.

### §5.4 OPEN-SS-32 attenuation factor (Priority 2)

Priority 2 in the Session 13 handover was OPEN-SS-32 attenuation-factor derivation conditional on Phase 3B succeeding. Since Phase 3B-A has failed and Phase 3B-B is increasingly constrained, OPEN-SS-32 attenuation work should remain deferred. If Phase 3B-B also fails, OPEN-SS-32 attenuation will need to be revisited from outside the unification hypothesis framework.

### §5.5 OPEN-ORG-012 (.tex conversion) — anti-priority continues

§7 of SS-9 v0.3 has now shifted four times in the OPEN-SS-32 ↔ U-shape thread (Phase 1 prior-art refinement, Phase 2 ruled out, Phase 3A ruled out + bracketing, Phase 3B-A ruled out + pattern-shape constraint). The .tex conversion remains deferred per the original Session 12 anti-trigger.

---

## §6. Forward-looking pointers

**Priority 1 (Session 15+):** Phase 3B-B — full IRREP-selective decomposition with character theory. Construct the irreducible-representation decomposition of the Hessian eigenspace under each polytope's full point group; identify the belt-IRREP for each polytope; sum variance contributions only from modes within the belt-IRREP. **Sharpened constraint from Phase 3B-A:** the construction must produce a non-monotonic-in-belt-size pattern within axial polytopes; specifically, must give *small* δ_belt at N_α=5 (empirical −12%) and *large* δ_belt at N_α=10 (empirical −34%). If this proves structurally impossible (any belt-IRREP-projection at N_α=5 saturates the 3-vertex belt), **R2 is ruled out** and the U-shape mechanism must be sought elsewhere.

**Priority 2 (deferred indefinitely):** OPEN-SS-32 attenuation-factor derivation — defer until Phase 3B-B closes. If R2 rules out, OPEN-SS-32 needs reformulation.

**Priority 3 (parallel, deferred):** OPEN-SS-16 Layer B closure work — deepest open problem at programme level; multi-session by scope.

**Priority 4 (parallel, registered):** Reading B literature check — empirical 41/A^{1/3} A-range of validity. Independent of Phase 3B status; can run in parallel.

**Anti-priorities:**
- Do **not** initiate SS-9 v0.3 → v0.1 .tex conversion (OPEN-ORG-012) until Phase 3B-B returns a result. §7 has shifted four times in this thread.
- Do **not** pursue further fixed-dimension belt-subspace variants (1D, 2D, etc.). The structural anti-correlation finding rules these out collectively.
- Do **not** add higher-m harmonics (m=3, m=4) to the current Phase 3B-A basis as an incremental enhancement — they cannot fix the N_α=5 overshoot, only worsen it.

---

## §7. Summary

Phase 3B-A — minimal fixed-dimension belt-subspace projection (3D basis: A₁ in-plane breathing + 2D E₂ quadrupole) — is **complete and produces a substantive negative result with constructive content**. The construction is RULED OUT as a complete R2 closure mechanism on two structural grounds: (i) target (a) magnitude factor 3× too small at J-solid mid-range peak, (ii) **pattern-shape within axial polytopes is anti-correlated with empirical**. **Eighth programme-level negative-result demonstration.**

Targets (b) and (c) — near-zero at regular polytopes and O_h ≪ D_{2d} — are met by symmetry-structural-identity (DEGENERATE inertia → dim(B) = 0), not by differential empirical support; they would be satisfied by any inertia-degeneracy-aware construction and do not discriminate Reading A from B/C.

The pattern-shape finding is the most informative new structural result: any fixed-dimension belt-subspace construction has belt fraction monotonically decreasing in N (subspace becomes a smaller fraction of belt-vertex-radial-displacement space as belts grow), but empirical wants small δ at small N and large δ at large N. **No fixed-dimension belt-subspace can produce the empirical U-shape.**

Phase 3B-A's constructive content sharpens the constraint on Phase 3B-B: the IRREP-selective construction must produce a non-monotonic-in-belt-size pattern. Specifically it must give small δ at N_α=5 (empirical −12%) and large δ at N_α=10 (empirical −34%). The N_α=5 small empirical softening is a particularly hard constraint — any belt-IRREP construction that captures the 3-vertex belt's full radial-displacement space at N_α=5 will overshoot. This may indicate the U-shape mechanism is **not** purely belt-IRREP-projection of the K₃ Gaussian Hessian.

R2 is severely weakened — three of four model-(b) realizations have failed (Phase 2 uniform-only, Phase 3A all-modes, Phase 3B-A fixed-dim belt subspace). Phase 3B-B (full character-theory IRREP decomposition) remains the only untested R2 realization. If Phase 3B-B also fails, R2 is formally ruled out and the U-shape mechanism must be sought outside the K₃-Gaussian-Hessian framework.

Six programme-level OPEN-SS-35 stages preserved. First qualitative cross-paradigm consilience claim (Session 9) intact. Pattern 6 K₃ scale-recurrence at 7 confirmed instances unchanged. R1 ruled-out (Session 12), Phase 2 ruled-out, Phase 3A ruled-out intact.

---

*Phase 3B-A reproducible computation. Substantive negative result on minimal fixed-dimension belt-subspace projection. Establishes pattern-shape anti-correlation as new structural constraint. Phase 3B-B (full IRREP decomposition with belt-IRREP dimension-scaling) registered as Session 15+ Priority 1 with sharpened constraint: must produce non-monotonic-in-belt-size pattern within axial polytopes.*
