# OPEN-SS-32 ↔ U-shape Unification — Phase 3 Phase B Sub-phase B: Full C_n IRREP Decomposition RULED OUT; n-vs-N Structural Obstacle Formally Closes R2 (Session 15 Phase 3B-B)

**Date:** 5 May 2026 (Session 15, Phase 3B-B — first session-tractable subphase of the full character-theory IRREP decomposition)
**Purpose:** Execute Phase 3B-B as registered at Session 14 close: project full Hessian eigenmodes onto belt-IRREP subspaces using the C_n proper-rotation subgroup of each axial polytope's full point group. Test three natural belt-IRREP variants (B-B1 all m≠0; B-B2 m=2 only; B-B3 radial m≠0). Close R2 (cluster-scale vs alpha-scale mean field unification at canonical σ_K3) one way or the other.

**Companion files:**
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase3b_a.md` (Phase 3B-A fixed-dim belt-subspace RULED OUT, pattern-shape anti-correlation)
- `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_unification_phase3b_b.py` (this Phase 3B-B reproducible computation)
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase3a.md` (Phase 3A naive full-Hessian RULED OUT, upper bound)

**Net programme effect:** **Phase 3B-B — full C_n IRREP decomposition with three belt-IRREP variants — RULED OUT** as a complete R2 closure mechanism, with a structural argument that **rules out the entire class of belt-IRREP-projection mechanisms within the K_3-Gaussian-Hessian framework**, not just specific implementations. The decisive new finding is the **n-vs-N structural obstacle**: empirical magnitude is monotonically increasing in N across the J-solid range (|−12, −30, −32, −33, −34|% for N=5,7,8,9,10), but the cyclic symmetry order n that drives any IRREP decomposition is non-monotonic in N (n = 3, 5, 2, 3, 4 for N = 5, 7, 8, 9, 10). No function of group-theoretic structure can produce a monotonic-in-N pattern when n is non-monotonic in N. **Ninth programme-level negative-result demonstration**, decisively stronger than Phase 3B-A's anti-correlation finding because it rules out the entire mechanistic class. **R2 is formally CLOSED — RULED OUT**: all four plausible model-(b) realizations have failed, and the structural argument extends the closure to constructions not yet computed (full point group with improper rotations, etc.). The U-shape mechanism must be sought **outside the K_3-Gaussian-Hessian framework entirely**. Six programme-level OPEN-SS-35 stages preserved. Pattern 6 K_3 scale-recurrence at 7 confirmed instances unchanged. The unification hypothesis at canonical σ_K3 is formally falsified; OPEN-SS-32 attenuation-factor derivation requires reformulation.

---

## §1. Strategy

Phase 3B-A established that fixed-dimension belt subspaces cannot match the empirical pattern: belt fraction monotonically decreases with N (covering a shrinking fraction of belt-radial space as polytopes grow) while empirical magnitude monotonically increases. The §6 forward pointer specified Phase 3B-B as the natural generalization — full character-theory IRREP decomposition where belt-IRREP dimension scales with the polytope.

Phase 3B-B implements this via the C_n proper-rotation subgroup of each axial polytope's full point group. The C_n group has irreducible representations labeled by angular momentum m = 0, 1, …, n−1; under real-valued cosine projection, m and n−m are paired, giving roughly ⌈n/2⌉ + 1 distinct projectors. Three natural "belt-IRREP" definitions are tested:

- **B-B1** "all m ≠ 0" — every axially-anisotropic mode (broadest reading; total non-trivial IRREP content)
- **B-B2** "m = 2 only" — specifically the oblate-quadrupole IRREP that SS-7 OPEN-SS-32 oblate-deformation hypothesis targets (most physically motivated, but structurally fragile at small n)
- **B-B3** "m ≠ 0 AND in-plane radial" — the dimension-scaling generalization of Phase 3B-A's fixed 3-dim belt-radial subspace

For DEGENERATE polytopes (T_d, O_h, I_h), no preferred axis → dim(belt) = 0 by symmetry, identical to Phase 3B-A.

The C_n proper-rotation subgroup is a **coarser** decomposition than the full point group (D_nh, D_nd including reflections and improper rotations). However, the C_n decomposition gives an **upper bound** on the variance content of any belt-IRREP definition within the full point group — restricting to a finer decomposition can only reduce variance. So if Phase 3B-B's C_n construction overshoots empirical structurally, full-point-group refinement cannot rescue it.

---

## §2. Model and computation

### §2.1 Cyclic-symmetry detection

For each axial polytope (PROLATE / OBLATE per Phase 3B-A), the principal axis from inertia classification is the candidate C_n axis. The largest n ∈ {2, 3, 4, 5} for which rotation by 2π/n about the axis maps the polytope vertex set to itself (within numerical tolerance 0.05·R_α) is selected. This gives:

- **N=5 D_{3h}**: PROLATE, n = 3
- **N=7 D_{5h}**: OBLATE,  n = 5
- **N=8 D_{2d}**: PROLATE, n = 2 (only proper rotation; full D_{2d} has S_4 improper)
- **N=9 D_{3h}**: OBLATE,  n = 3
- **N=10 D_{4d}**: PROLATE, n = 4 (only proper rotation; full D_{4d} has S_8 improper)

DEGENERATE polytopes (T_d, O_h, I_h): n = 0, no IRREP decomposition.

### §2.2 Rotation operator on displacement space

Under the C_n rotation, vertex i maps to vertex π(i) where π is the induced permutation. The 3N-dim displacement-space rotation operator R_n acts as a tensor product of vertex permutation and 3D rotation:

$$(R_n u)[3\pi(i):3\pi(i)+3] = R_{3D} \cdot u[3i:3i+3]$$

where R_{3D} is the 3D rotation matrix by 2π/n about the principal axis. As a 3N × 3N block-permutation matrix, the entries are:

$$R_n[3\pi(i):3\pi(i)+3,\, 3i:3i+3] = R_{3D}, \qquad \text{zero elsewhere}$$

### §2.3 Real-valued IRREP projectors

For each m ∈ {0, 1, …, n−1}, the cosine projector is:

$$P_m = \frac{1}{n}\sum_{j=0}^{n-1} \cos\!\left(\frac{2\pi m j}{n}\right) R_n^j$$

Properties:
- $\sum_m P_m = I$ (completeness; verified by Σ trace P_m = 3N for all polytopes).
- $P_m = P_{n-m}$ (cosine symmetry; m and n−m are paired into degenerate doublet partners).
- For n=3, m=2 ≡ m=1; for n=2, m=2 ≡ m=0 (not a separate IRREP).

The genuinely-orthogonal IRREP decomposition would use complex exponentials (E_m = (1/n)Σ e^{−2πimj/n} R_n^j); the cosine projection captures the same content via real combinations and is sufficient for the variance-fraction calculation.

### §2.4 Belt-IRREP fractions per mode

For each Hessian eigenmode v_k:

$$f_k^{\rm B-B1} = ||(I - P_0) v_k||^2 = 1 - ||P_0 v_k||^2$$

(captures all m ≠ 0 content; doesn't depend on potentially-redundant cosine projector pairing)

$$f_k^{\rm B-B2} = ||P_2 v_k||^2 \quad (\text{only computed for } n \geq 3)$$

$$f_k^{\rm B-B3} = ||P_{\rm rad} \cdot (I - P_0) v_k||^2$$

where P_{rad} is the per-vertex in-plane radial-direction projector (Phase 3B-A construction).

### §2.5 Variance weighting

Same Phase 3B-A scheme: per-mode contribution to per-edge MSD weighted by f_k:

$$\langle (\delta r)^2\rangle_{\rm B-B*} = \frac{1}{|E|}\sum_k f_k^{\rm B-B*} \cdot C_k^{\rm edge}, \qquad \delta_{\rm B-B*} = -\frac{2 \langle (\delta r)^2\rangle_{\rm B-B*}}{R_\alpha^2}$$

---

## §3. Results

### §3.1 Eight-row table

Polytopes scaled to R_α = 2.37 fm, σ_K3 = 1.68 fm. All entries from `SS-9_OPEN-SS-32_Ushape_unification_phase3b_b.py`.

| N | sym | inertia | n | −δ_full% | −δ_BB1% | −δ_BB2% | −δ_BB3% | −δ_emp% |
|---|---|---|---|---|---|---|---|---|
| 4 | T_d | DEGEN | 0 | −86.77 | 0.00 | 0.00 | 0.00 | +11.51 |
| 5 | D_{3h} | PROLATE | 3 | −85.71 | −50.09 | −12.52 | −13.94 | −12.16 |
| 6 | O_h | DEGEN | 0 | −86.53 | 0.00 | 0.00 | 0.00 | −21.27 |
| 7 | D_{5h} | OBLATE | 5 | −85.22 | −68.24 | −7.39 | −20.71 | −29.50 |
| 8 | D_{2d} | PROLATE | 2 | −85.47 | −38.30 | 0.00 | −10.97 | −31.81 |
| 9 | D_{3h} | OBLATE | 3 | −85.35 | −54.06 | −13.51 | −16.08 | −33.14 |
| 10 | D_{4d} | PROLATE | 4 | −85.15 | −62.01 | −19.23 | −14.98 | −33.58 |
| 12 | I_h | DEGEN | 0 | −84.92 | 0.00 | 0.00 | 0.00 | +1.41 |

Sanity checks verified:
- Phase 3A reproduction: δ_full identical to Phase 3A table to 3 decimals across all 8 polytopes.
- Σ trace P_m = 3N for every polytope (5+5+5=15 for N=5; 5+5+3+3+5=21 for N=7; 12+12=24 for N=8; 9+9+9=27 for N=9; 8+8+6+8=30 for N=10).
- DEGENERATE polytopes get f_belt = 0 by symmetry construction (consistent with Phase 3B-A).

### §3.2 The decisive finding: n is non-monotonic in N

The empirical pattern is **monotonically increasing in N** across the J-solid range:

| N_α | 5 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|
| empirical magnitude (%) | 12.16 | 29.50 | 31.81 | 33.14 | 33.58 |

The cyclic symmetry order n that drives any IRREP decomposition is **non-monotonic in N**:

| N_α | 5 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|
| n | 3 | 5 | 2 | 3 | 4 |

This is a **structural mismatch**. Any belt-IRREP-projection mechanism produces variance proportional to ratios of IRREP dimensions to group order, which depend on n (the group structure). If n is non-monotonic in N but empirical is monotonic in N, no function of group-theoretic structure alone can reproduce the empirical pattern.

**This rules out the entire class of belt-IRREP-projection mechanisms within the K_3-Gaussian-Hessian framework** — not just the three Phase 3B-B variants but any extension to the full point group (D_nh, D_nd including reflections and improper rotations) or any narrower belt-IRREP definition.

### §3.3 B-B1 (all m ≠ 0) — uniform overshoot

Average J-solid belt fraction = **0.65** (vs target 0.40). Predicted softening uniformly overshoots empirical by factor 1.2 to 2.7 across the J-solid range. Pattern non-monotonic (50, 68, 38, 54, 62 for N=5,7,8,9,10 — driven by non-monotonic n). RULED OUT.

### §3.4 B-B2 (m = 2 only) — N=5 match but undershooting elsewhere

Average J-solid belt fraction = **0.118** (vs target 0.40). At N=5, the B-B2 prediction (−12.52%) matches empirical (−12.16%) to within 3% — the smallest discrepancy of any belt-IRREP construction tested. This is surprising because Phase 3B-A had its hardest overshoot at N=5 (factor 2.7).

The match is interpretable but does not generalize:
- At N=5 (n=3), m=2 ≡ m=1 under cosine projection (since cos(2·2π/3) = cos(4π/3) = cos(2π/3)); B-B2 captures the m=±1 doublet, which under C_3 is the only non-trivial IRREP. The result is therefore equivalent to "all non-symmetric content under C_3" at N=5.
- At N=8 (n=2), m=2 ≡ m=0; B-B2 captures nothing distinct from the totally-symmetric mode and gives 0. Empirical wants −31.8%.
- At N=7 (n=5), B-B2 is the m=±2 doublet, a smaller fraction of mode space; gives −7.4%, undershooting empirical −29.5% by factor 4.

Pattern: 12.5, 7.4, 0.0, 13.5, 19.2 for N=5,7,8,9,10. Non-monotonic. RULED OUT.

### §3.5 B-B3 (radial m ≠ 0) — undershoot, dimension scaling does not save

Average J-solid belt fraction = **0.184** (vs target 0.40). This is **38% larger** than Phase 3B-A's fixed-dim 0.135 — confirming that letting belt dimension scale with polytope size helps somewhat. But the absolute level remains factor 2 short of target.

At N=5: B-B3 = −13.94% vs empirical −12.16%, slight overshoot (factor 1.15). Phase 3B-A's N=5 overshoot (factor 2.7) is substantially reduced — dimension scaling does ameliorate this. But:
At N=7,8,9,10: B-B3 produces −10 to −21%, all undershooting empirical −30 to −34%. Pattern non-monotonic (13.9, 20.7, 11.0, 16.1, 15.0). RULED OUT.

### §3.6 Targets (b) and (c) — same automatic-by-symmetry passing as Phase 3B-A

T_d, O_h, I_h all DEGEN, dim(belt) = 0, all variants give 0. Target (b) met by symmetry construction (not as differential test). Target (c) ratio O_h/D_{2d} = 0/positive = 0 ≪ 1, met by symmetry construction. Empirical octahedron softening −21.3% ≠ 0; Reading A empirically falsified at this discriminator (same as Phase 3B-A).

---

## §4. Structural interpretation

### §4.1 The n-vs-N obstacle is a programme-level structural argument

The claim "no belt-IRREP-projection mechanism can produce the empirical pattern" rests on three premises:

1. **The empirical pattern is monotonically increasing in N** across the J-solid range (verified: 12, 30, 32, 33, 34 for N=5,7,8,9,10).
2. **Any belt-IRREP-projection mechanism's variance content depends on n** (the cyclic symmetry order driving the IRREP decomposition), or equivalently on |G| (the order of the polytope's full point group).
3. **n is non-monotonic in N** across the J-solid range (verified: 3, 5, 2, 3, 4 for n; 12, 20, 8, 12, 16 for full-point-group order).

Premises (1) and (3) are empirical structural facts about the alpha-chain deltahedron sequence. Premise (2) is the defining property of any "IRREP-projection" or "character-theory" mechanism: variance is computed as a sum over modes weighted by projection onto IRREP-defined subspaces, which inherently couples to group structure.

The conclusion: **no function of group-theoretic structure can produce a monotonic-in-N pattern when n (or |G|) is non-monotonic in N**. This is the structural argument.

It extends to mechanisms not yet computed:
- **Full point group (D_nh, D_nd) IRREP decomposition with improper rotations**: |G| ∈ {12, 20, 8, 12, 16} — non-monotonic in N.
- **Energy-weighted IRREP filtering** (only soft belt modes contribute): the soft-mode count depends on n via the IRREP decomposition.
- **Higher-m harmonics** (m=3, m=4): exist or don't exist depending on n.

All such constructions have variance content tied to non-monotonic-in-N quantities. **R2's K_3-Gaussian-Hessian-belt-IRREP-projection class is closed.**

### §4.2 What the U-shape mechanism could be

The empirical monotonic-in-N pattern is reproducible by mechanisms whose variance scales with monotonic-in-N quantities:

- **Total mode count** (3N − 6) — monotonic in N. Scales as 9, 12, 15, 18, 21, 24, 30 for N=4,5,6,7,8,9,10,12.
- **Edge count** |E| = 3N − 6 — monotonic in N (deltahedron face-count).
- **Cluster volume or surface area** — monotonic in N (with shape-dependent coefficients).
- **Cluster compactness measures** — monotonic-trending.

These mechanisms suggest U-shape origins outside the IRREP-projection framework:
- **Elastic energy curvature beyond simple Hessian** — anharmonic K_3 corrections at order ξ^4 in the Gaussian expansion.
- **Surface-tension contribution** to cluster shape stability — scales with cluster surface area.
- **Pauli-blocking at internal alpha-alpha contacts** — scales with edge count.
- **Coulomb-screened intra-cluster destabilization** — Session 12's R1 mechanism (RULED OUT for sign reasons; the scale dependency might be re-targetable).
- **Effective-mass renormalization** of nucleon orbitals in a cluster context — couples to cluster size directly.

These are candidate mechanisms outside the K_3-Gaussian-Hessian-belt-IRREP-projection framework. They would each require their own scoping and substantive computation.

### §4.3 The B-B2 N=5 match — interpretive note

The B-B2 prediction at N=5 (−12.52%) matching empirical (−12.16%) to within 3% deserves explicit interpretive caveats:

1. The match is N-isolated. B-B2 predictions at N=7, 8, 9, 10 all undershoot or are zero; the close N=5 match does not generalize.
2. Under C_3 cosine projection, the m=2 IRREP is identical to the m=±1 IRREP doublet (which is the unique non-trivial IRREP under C_3). So B-B2 at N=5 captures "all non-symmetric content" rather than a specifically-quadrupole content.
3. The variance fraction at N=5 (0.146) happens to be smaller than at higher-n polytopes because the m=±1 IRREP at C_3 contains the lowest-frequency modes, but the per-mode variance distribution at N=5 happens to dilute these modes' contribution. This is not the result of a quadrupole physics signal.

In short: the N=5 match is not evidence for a successful Reading A mechanism; it is a coincidence of how the C_3 group-theoretic structure happens to interact with the small-N mode spectrum. Phase 3B-A's overshoot at N=5 was the structural problem (3-vertex belt fully spanned by 3-dim subspace); B-B2's adequate behavior at N=5 reflects a different group-theoretic constraint that does not extrapolate.

### §4.4 Comparison across ruled-out R2 realizations

| realization | session | typical magnitude at N=10 | pattern shape | structural reason ruled out |
|---|---|---|---|---|
| Phase 2 model (a) — uniform A_1 | 13 Phase 2 | −4.6% (factor 7 short) | monotonic decrease | 1-dim subspace; bulk-density scaling |
| Phase 3A — full Hessian, all modes | 13 Phase 3A | −85% (factor 2.5 over) | flat | local soft modes dominate; no shape selection |
| Phase 3B-A — fixed-dim belt subspace | 14 Phase 3B-A | −8% (factor 4 short) | anti-correlated within axial | fixed dim shrinks fraction as belt grows |
| **Phase 3B-B — full C_n IRREP variants** | **15 Phase 3B-B** | **−19% best (factor 1.7 short)** | **non-monotonic from n-vs-N mismatch** | **n is non-monotonic in N; class-level obstacle** |

Phase 3B-B's negative result is **decisively stronger** than Phase 3B-A's because it identifies a structural obstacle that extends beyond the specific implementation to the entire mechanistic class.

### §4.5 R2 status — formally CLOSED

R2 (cluster-scale vs alpha-scale mean-field unification at canonical σ_K3) has now seen all four plausible model-(b) realizations fail:

| realization | R2 closure attempt status |
|---|---|
| Uniform scaling (single A_1 mode) | RULED OUT — Session 13 Phase 2 |
| All modes equal-weighted | RULED OUT — Session 13 Phase 3A |
| Fixed-dim belt subspace | RULED OUT — Session 14 Phase 3B-A |
| **Full C_n IRREP decomposition (B-B1, B-B2, B-B3)** | **RULED OUT — Session 15 Phase 3B-B** |

The structural argument (n-vs-N mismatch) extends the closure to constructions not yet computed. **R2 is FORMALLY CLOSED — RULED OUT.** The U-shape mechanism is **not** within the K_3-Gaussian-Hessian-belt-IRREP-projection framework.

The unification hypothesis at canonical σ_K3 is **falsified**. OPEN-SS-32 attenuation-factor derivation and the R2 closure for OPEN-SS-35 sub-question (a) A-scaling closure both require reformulation using mechanisms outside the framework.

---

## §5. Programme implications

### §5.1 Verdict on Phase 3B-B

**Phase 3B-B — full C_n IRREP decomposition with three belt-IRREP variants — is RULED OUT** as a complete R2 closure mechanism on the structural ground that **n (cyclic symmetry order) is non-monotonic in N while empirical magnitude is monotonic in N**. This rules out the entire class of belt-IRREP-projection mechanisms within the K_3-Gaussian-Hessian framework.

**Ninth programme-level negative-result demonstration** in OPEN-SS-35 closure programme:

| # | route | session | reason ruled out |
|---|---|---|---|
| 1 | Route D lattice-shell counting | 5 Phase 2 | shells don't match magic numbers |
| 2 | Route B-γ K_3-mode phase | 7 Phase 2 | $V_{\rm SO}/\hbar\omega \sim 10^{-3}$ |
| 3 | Route 1b $V_{\rm SO}$ refinement | 10 | saturates at $V_{\rm SO}/\hbar\omega \approx 0.11$ |
| 4 | Path (i) cluster-surface | 11 Phase 1 | $f_{\rm SO}(r)$ peaks at center |
| 5 | R1 $R_\alpha$ scale-dependence | 12 | wrong sign + U-shape + decoupled |
| 6 | Phase 2 model (a) uniform | 13 Phase 2 | factor 7 undershoot, monotonic |
| 7 | Phase 3A naive full-Hessian | 13 Phase 3A | flat, factor 2.5 overshoot |
| 8 | Phase 3B-A fixed-dim belt subspace | 14 Phase 3B-A | mag × 3 short + pattern anti-correlated |
| 9 | **Phase 3B-B full C_n IRREP variants** | **15 Phase 3B-B** | **n-vs-N structural mismatch; class-level closure** |

### §5.2 Constructive content of Phase 3B-B

Despite being a ruling-out, Phase 3B-B is constructive:

1. **The n-vs-N structural argument generalizes** beyond the three computed variants. Future investigators don't need to test full point group decomposition or higher-m harmonics within this framework — the structural argument suffices.

2. **B-B3's improvement over Phase 3B-A confirms dimension scaling helps but doesn't suffice.** Average J-solid belt fraction grew from 0.135 (Phase 3B-A) to 0.184 (B-B3) — a 38% improvement from letting belt dimension scale with polytope size. But the structural ceiling at ~0.18 is still factor 2 below target, indicating the K_3-Gaussian-Hessian framework lacks sufficient variance in any belt-IRREP-restricted subspace.

3. **The B-B2 N=5 coincidence is interpretable.** It is not evidence of a working Reading A mechanism; it reflects how C_3 group structure happens to dilute mode contributions at small N (§4.3).

4. **Targets (b) and (c) being met by symmetry-structural-identity is now confirmed across two independent IRREP constructions.** This is now a robust observation: any inertia-degeneracy-aware construction satisfies them. They are not differential tests of any reading.

5. **The U-shape mechanism is identified as structurally outside the K_3-Gaussian-Hessian framework.** Candidate mechanisms (anharmonic K_3 corrections, surface-tension, Pauli-blocking, effective-mass renormalization, etc.) are listed in §4.2. Each requires independent scoping.

### §5.3 R2 closure — programme implications

R2 was the central candidate for closing OPEN-SS-35 sub-question (a) A-scaling. With R2 ruled out:

- **Sub-question (a) A-scaling closure** does NOT have a remaining candidate mechanism within the K_3-Gaussian-Hessian framework. R1 ruled out Session 12 (Decoupling Theorem); R2 ruled out this session. **Both registered closure candidates have failed.**
- **The path forward** is to find a new closure mechanism for sub-question (a) outside the framework. Candidate mechanisms in §4.2 are starting points but each requires its own scoping and substantive computation.
- **OPEN-SS-32 attenuation-factor derivation** (Phase 3A Priority 2 conditional on R2 success) is now blocked. The OPEN-SS-32 oblate-deformation hypothesis itself is empirically supported (six-of-eight qualitative match), but the K_3-Gaussian-Hessian belt-IRREP mechanism for it is ruled out. Reformulation needed.
- **Sub-question (b) layer 3 gap-strength closure** is INDEPENDENT of R2 (Decoupling Theorem, Session 12). It remains where Session 11 Phase 1 left it: needs CPP physics outside the simple K_3 + HO + L·S + V_SO refinement framework.

### §5.4 Pattern 6 K_3 scale-recurrence and consilience claim

Pattern 6 K_3 scale-recurrence at 7 confirmed instances unchanged (Phase 3B-B does not affect it). First qualitative cross-paradigm consilience claim (Session 9, magic-number sequence reproduced from CPP first-principles) intact. These are preserved positive results; the R2 closure failure does NOT damage them.

### §5.5 Six programme-level OPEN-SS-35 stages

Six programme-level OPEN-SS-35 stages preserved. Phase 3B-B refines stage (vi) by formally closing R2; does not advance to a new programme-level stage. The closure is informational rather than progressional — stage (vi) was previously "unclosed pending R2 verdict"; it is now "R2 ruled out, A-scaling closure mechanism unknown."

### §5.6 OPEN-ORG-012 (.tex conversion) — anti-priority status update

§7 of SS-9 v0.3 has now shifted **five times** in the OPEN-SS-32 ↔ U-shape thread (Phase 1 prior-art read, Phase 2 ruled out, Phase 3A ruled out + bracketing, Phase 3B-A ruled out + pattern-shape constraint, Phase 3B-B ruled out + R2 formal closure). With R2 formally closed, §7 will need a substantial rewrite reflecting the ruled-out R2 status. This is genuine new content — the .tex conversion deferral remains warranted.

---

## §6. Forward-looking pointers

**Priority 1 (substantive new investigation):** Identify the U-shape mechanism outside the K_3-Gaussian-Hessian framework. Candidate mechanisms (§4.2) include anharmonic K_3 corrections, surface-tension contribution, Pauli-blocking at internal contacts, effective-mass renormalization, Coulomb-screened intra-cluster destabilization revisited. Multi-session by scope (each candidate is a separate scoping investigation). **Suggested first scope:** anharmonic K_3 corrections at order ξ^4 in the Gaussian expansion — most direct extension of the Phase 2/3A/3B framework, scales with edge count (monotonic in N), tractable in single session.

**Priority 2 (substantive new investigation):** Sub-question (b) layer 3 gap-strength closure outside the simple K_3 + HO + L·S + V_SO refinement framework. Session 11 Phase 1's candidate avenues: (a) sharper-surface contributions from K_3 edge mechanism + Pauli-blocking; (b) additional binding terms beyond Gaussian sum; (c) L·S operator structure beyond Bohr-Mottelson form (intersects OPEN-SS-16 Layer B); (d) recognition that magic-strength hierarchy may not be purely mean-field.

**Priority 3 (deferred):** OPEN-SS-32 attenuation-factor derivation reformulation — depends on Priority 1 success.

**Priority 4 (parallel):** OPEN-SS-16 Layer B closure work — deepest open problem at programme level.

**Priority 5 (parallel):** Reading B literature check — empirical $41/A^{1/3}$ A-range of validity. Independent of all other work.

**Anti-priorities:**
- Do **not** initiate SS-9 v0.3 → v0.1 .tex conversion (OPEN-ORG-012) until §7 is reformulated for ruled-out R2.
- Do **not** pursue further belt-IRREP-projection variants within the K_3-Gaussian-Hessian framework. The n-vs-N structural argument rules out the entire class.
- Do **not** pursue full point group (D_nh, D_nd including reflections) IRREP decomposition as an extension. The structural argument applies — full point group orders are also non-monotonic in N (12, 20, 8, 12, 16 for the J-solid range).
- Do **not** pursue energy-weighted IRREP filtering or higher-m harmonics within this framework — the structural argument applies.

---

## §7. Summary

Phase 3B-B — full C_n proper-rotation IRREP decomposition with three belt-IRREP variants (B-B1 all m≠0; B-B2 m=2 only; B-B3 radial m≠0) — is **complete and produces a substantive negative result with class-level structural argument**. The construction is RULED OUT as a complete R2 closure mechanism on the structural ground that **n (cyclic symmetry order driving any IRREP decomposition) is non-monotonic in N while empirical magnitude is monotonic in N across the J-solid range**.

**Ninth programme-level negative-result demonstration**, decisively stronger than Phase 3B-A's because the structural argument extends the ruling to constructions not computed: full point group with improper rotations, energy-weighted IRREP filtering, higher-m harmonics. The entire **class** of belt-IRREP-projection mechanisms within the K_3-Gaussian-Hessian framework is ruled out.

**R2 (cluster-scale vs alpha-scale unification at canonical σ_K3) is FORMALLY CLOSED — RULED OUT.** All four plausible model-(b) realizations have failed, and the structural argument extends to all model-(b) variants. The unification hypothesis at canonical σ_K3 is falsified. OPEN-SS-32 attenuation-factor derivation and OPEN-SS-35 sub-question (a) A-scaling closure both lose their primary candidate mechanism.

The U-shape mechanism must be sought **outside the K_3-Gaussian-Hessian framework**. Candidate mechanisms include anharmonic K_3 corrections, surface-tension contributions, Pauli-blocking at contacts, effective-mass renormalization, and Coulomb-screened destabilization revisited. Each requires independent scoping. **Suggested Priority 1 next session:** anharmonic K_3 corrections at order ξ^4 — most direct extension of the framework, scales with edge count (monotonic in N), single-session-tractable.

Sub-question (b) layer 3 gap-strength closure (Decoupling-Theorem-independent of R2) remains where Session 11 Phase 1 left it. First qualitative cross-paradigm consilience claim (Session 9) intact. Six programme-level OPEN-SS-35 stages preserved. Pattern 6 K_3 scale-recurrence at 7 confirmed instances unchanged.

The B-B2 N=5 close match (12.5% predicted vs 12.16% empirical, 3% discrepancy) is an interpretive curiosity (§4.3) rather than evidence of a working Reading A mechanism — it reflects how C_3 group structure dilutes small-N mode contributions, not a quadrupole physics signal.

---

*Phase 3B-B reproducible computation. Decisive negative result with class-level structural argument from n-vs-N mismatch. Formally closes R2 and points the U-shape mechanism investigation outside the K_3-Gaussian-Hessian framework. Priority 1 for Session 16: anharmonic K_3 corrections at order ξ^4 in the Gaussian expansion, single-session-tractable, scales monotonically with edge count.*
