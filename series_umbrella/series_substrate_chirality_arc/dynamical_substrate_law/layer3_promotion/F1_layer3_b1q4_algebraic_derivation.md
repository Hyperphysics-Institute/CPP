# B.1.q4 — Full Algebraic Derivation of the General Per-Vertex DI-bit Current Formula at Layer 3

**Sub-question:** B.1.q4 — first-shell current sum identity (Layer 2 closed at Patch 0533 §9; Layer 3 promotion opened at this Patch).

**Promotion scope:** sketch-document Layer 3 — explicit step-by-step algebraic derivation of the general per-vertex DI-bit current formula $\vec{j}_{DI}^{net}(v) = 2 r_0 \delta[(2+\phi)\hat{n} - (4a/\phi)\hat{v}] + \mathcal{O}(\delta^2)$ from CPP primitives + 600-cell first-shell geometric primitives + Schur's-lemma representation theory of $I_h$ on the 3D link hyperplane.

**Patch:** 0541, Session 140 (22 May 2026), first Layer 3 promotion in the F.1 sub-question's trajectory.

**Patch-0541 candidacy:** G.b per Patch 0540 scoping document §4.3 — Target 1 (B.1.q4 full algebraic derivation), the alternative single-session opening selected over G.a (Priority 1 chain Target 2 → Target 3 framework axiomatization) for clean single-Patch closure cleanness and recovery of the §5-condensed derivation preserved at the Session 139 close handover.

---

## §0 Working-session firewall

This Patch promotes B.1.q4's sketch Layer 2 closure (Patch 0533 §9) to sketch-document Layer 3 — explicit closed-form derivation of the general per-vertex current formula with every identity traced step-by-step from primitives. The promotion is per-target and trajectory-bounded per §15.7 of `F1_phase2_foundations_work.md` ("each Layer 3 promotion is its own gated trajectory") and §17.7 of `templates/operating_system.md` (status-upgrade-Patch-style scope-bounded execution applies to Layer 3 closure Patches).

### §0.1 Anti-priorities sustained at this Patch

1. **No Layer 4 work.** The 600-cell first-shell geometric primitives G1 + G2 + $I_h$-symmetry of the icosahedral link are treated as inherited from the substrate geometry; their derivation from CPP axioms A1–A11 is Layer 4 territory, registered as part of the long-term programme target (chirality scale from polytope geometry) per Patch 0539 §15.5.
2. **No other sub-question Layer 3 promotion.** Targets 2–7 from Patch 0540 scoping document §2 (B.2.q1 framework axiomatization, B.1.q1 matter-state independent derivation, B.1.d substrate-locality temporal extension, B.3.q1 corollary, B.1.q3 PT propagation, B.1.q2 zero curl) remain at sketch Layer 2 status and are NOT advanced in this Patch. Each is its own gated trajectory.
3. **No F.1 sub-question status change.** F.1 status remains "SUBSTANTIVE SKETCH-LEVEL CLOSURE at Layer 2 under the minimal-local-first-order realization framework, pending Layer 3 promotion + supplementary work on the 7 open sub-questions and higher-order extensions" per Patch 0539 §15.2. B.1.q4 Layer 3 closure does NOT propagate to F.1 status until Layer 3 promotion arc completes + Layer 3 reviewer-pause cycle + Layer 3 status upgrade per §17 codified discipline.
4. **No v1.0 SHIPPED edits.** Chirality Continuum v1.0, Capotauro v2.0 v1.0, SF-2 v1.0, SM-2 v1.0, SF-4 v4.4 all `.tex` sources frozen.
5. **No Phase 1 §11 / Phase 2 §12 polished content modifications** in `F1_subquestion_pcd_orientation_link.md`. The Patch 0528 §14.17 calibrated framing is immutable per §17.8.
6. **No Patches 0531–0540 immutable content modifications** in `F1_phase2_foundations_work.md` or `F1_layer3_promotion_scoping.md`. Patch 0533 §9 (the Layer 2 sketch this promotion builds on) is preserved as historical record; this Layer 3 document is a separate, additive artifact in `layer3_promotion/`, not an inline edit.
7. **No reviewer-pause checkpoint modifications** at `reviewer_pause/F1_reviewer_pause_checkpoint_patches_0531_0537_v1.0.md` or `reviewer_pause/F1_reviewer_pause_feedback_record_v1.0.md` (preserved as historical records per §17.8).
8. **No F.1 flagship paper assembly trigger.** Per `templates/paper_completion_checklist.md` Reviewer-Pause Cycle Precondition section, flagship paper assembly requires Layer 3 promotion arc completion + Layer 3 reviewer-pause + Layer 3 status upgrade. This Patch closes ONE Layer 3 target; the arc is not yet complete.
9. **No Findings registry promotion.** The general per-vertex current formula $\vec{j}_{DI}^{net}(v)$ remains an intermediate computational result. The Patch 0533 §9.12 anti-priority is sustained: "do NOT promote the §9.4 general per-vertex current formula to a finding (intermediate result, anti-priority sustained)". Layer 3 promotion at sketch-document level does NOT itself trigger Findings registry entry; that is a separate decision.
10. **No F.2 / F.3 substantive content trajectory opening.** Both remain DEFERRED at decision-gate level per Patch 0539 §15.5.
11. **No long-term programme target work** (chirality scale from polytope geometry). REGISTERED + DEFERRED per Patch 0528 §14.17 and Patch 0539 §15.5.

### §0.2 What this Layer 3 promotion IS

- Explicit, closed-form algebraic derivation of the general per-vertex DI-bit current formula at first order in the Mechanism A primitive parameter $\delta$.
- Every load-bearing identity (I1 vertex-projection, I2 perpendicular-magnitude, I3 icosahedral central symmetry, I4 icosahedral tensor sum isotropy, I5 golden-ratio reduction) stated as a self-contained sub-result, derived from primitives with every step shown.
- Schur's lemma applied to the 3D irreducible representation of $I_h$ on the link hyperplane, with the trace computation giving the isotropy coefficient $c = 4$ explicitly.
- Sanity check at $v = v_{\text{host}}$ recovering Phase 1 Finding DSL-1's $(6r_0\delta/\phi^2)\hat{n}$ exactly via Identity I5.
- Resolution of Copilot's Patch 0538 §14.4 calibration concern (numerical verification at machine precision is sufficient for sketch Layer 2 but not a substitute for Layer 3 algebraic derivation).

### §0.3 What this Layer 3 promotion is NOT

- NOT a derivation of the 600-cell first-shell geometric primitives G1 + G2 from CPP axioms (that is Layer 4).
- NOT a derivation of $I_h$-symmetry of the icosahedral link from CPP axioms (that is Layer 4).
- NOT a higher-order ($\mathcal{O}(\delta^2)$) extension (that is B.1.q6 territory, deferred).
- NOT a promotion of the result to programme-level Findings registry.
- NOT a flagship-paper-section draft; it is a sketch-document Layer 3 artifact in `layer3_promotion/`.

---

## §1 Layer 3 promotion context

### §1.1 What Layer 2 established at Patch 0533 §9.4

Patch 0533 §9 closed B.1.q4 at sketch Layer 2 with:

- Generalization of the Phase 1 per-vertex current formula from vertex-aligned $\hat{n} = v_{\text{host}}$ to arbitrary vertex $v$ under fixed framework $\hat{n}$ (§9.2).
- Four-term expansion via decomposition $\hat{u}_j^v = \alpha\hat{v} + \beta\hat{w}_j^v$ (§9.4).
- Boxed result $\vec{j}_{DI}^{net}(v) = 2 r_0 \delta[(2+\phi)\hat{n} - (4a/\phi)\hat{v}] + \mathcal{O}(\delta^2)$ where $a \equiv \hat{v}\cdot\hat{n}$ (§9.4).
- Numerical verification at machine precision via `code/verify_b1q4_first_shell_current_sum.py` (deviations $\leq 2 \times 10^{-15}$ across five test $\delta$ values).
- Sanity check at $v_{\text{host}}$ recovering Phase 1's boxed result $(6 r_0 \delta/\phi^2)\hat{n}$ exactly (§9.4).
- First-shell current sum identity $\sum_i \hat{j}_{DI}^{net}(v_i) = (24/\sqrt{7-\phi})\hat{n} \approx 10.345\hat{n}$ at first order (§9.6).

The §9.4 derivation contains the algebra in compressed form: "Expanding into four terms and using the two icosahedron identities to reduce" without writing the four terms out explicitly, and "Using the golden-ratio identities $1/\phi^2 = 2 - \phi$ and $1/\phi = \phi - 1$" with the algebraic chain in a single line.

### §1.2 What Layer 2 deferred to Layer 3 per Patch 0538 §14.4

Copilot's calibration concern at Patch 0538 §14.4:

> "The (2+φ) and 4/φ coefficients in the general per-vertex current formula are presented as deriving from icosahedral tensor identities but the explicit step-by-step derivation is not fully traced; the existing numerical verification at machine precision is sufficient for sketch Layer 2 but does NOT substitute for Layer 3 algebraic derivation."

Patch 0538 §14.4 closed B.1.q4 at sketch Layer 2 "with numerical verification at machine precision; algebraic derivation deferred to Layer 3" — registering the deferral explicitly.

### §1.3 What Layer 3 means at sketch-document level

Layer 3 promotion at sketch-document level (per Patch 0540 §1.2):

> "Closed-form algebraic derivation from primitives, with every load-bearing identity stated as a self-contained sub-result and each step traced. Numerical verification preserved as independent confirmation but no longer load-bearing."

This is distinct from Layer 4 (deriving the geometric primitives themselves from CPP axioms A1–A11) and from flagship-paper Layer 3 (publication-grade prose + theorem-environment formatting + literature citations + reviewer-grade rigor on every cross-reference).

The sketch-document Layer 3 artifact lives in `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/layer3_promotion/` parallel to the `reviewer_pause/` directory pattern from Patches 0538 / 0539a. Future Layer 3 promotions for other sub-questions create sibling documents in this directory.

---

## §2 Primitives and conventions

### §2.1 CPP primitives

The derivation uses the following CPP axioms and framework constructs as inputs (no others):

- **CPP axiom A1** (DI-bit propagation): conscious points exchange directed information bits along lattice edges at a base rate $r_0$ per Absolute Moment.
- **CPP axiom A5** (PCD cycle): Polarize–Capture–Depolarize cycle as substrate-dynamical primitive carrying ordered cyclicity with T-asymmetry.
- **Mechanism A primitive** (introduced at `F1_subquestion_pcd_orientation_link.md` §2.1, calibrated at Patch 0528 §11.11): under framework chirality direction $\hat{n}$, the DI-bit propagation rate along edge direction $\hat{e}_{ab}$ is perturbed at first order in a chirality-bias magnitude $\delta$:
  $$r(\hat{e}_{ab}) = r_0\big(1 + \delta \cdot \hat{e}_{ab} \cdot \hat{n}\big)$$
- **Reading C** (Capotauro v2.0 substrate-locality framework, registered at `reading_c_substrate_locality.md`): substrate-physics quantities at a vertex are determined by content within the first-shell of that vertex; higher shells enter at higher orders in the perturbation parameter.

### §2.2 600-cell first-shell geometric primitives (inherited; Layer 4 derivation deferred)

The 600-cell polytope in $\mathbb{R}^4$ has 120 vertices, each with 12 first-shell neighbors at edge length $1/\phi$ (taking the unit-radius normalization $|v| = 1$ for all vertices). The two primitives load-bearing for this derivation:

- **G1 — Uniform vertex-pair angle:** for any vertex $v$ and any first-shell neighbor $v_j$ of $v$:
  $$v \cdot v_j = \cos 36° = \frac{\phi}{2} \quad \text{(uniform across all 12 first-shell neighbors)}$$
- **G2 — Icosahedral link:** the 12 first-shell neighbors of $v$ form a regular icosahedron in the 3D hyperplane perpendicular to $\hat{v}$ (the "link" of $v$ in the 600-cell). The icosahedral group $I_h$ (order 120) acts on this link.

Both G1 and G2 are standard 600-cell facts (cf. Coxeter, *Regular Polytopes*); their derivation from CPP axioms is Layer 4 work, deferred.

### §2.3 Framework conventions

- $\phi = (1+\sqrt{5})/2$, golden ratio. Identities used: $\phi^2 = \phi + 1$; $1/\phi = \phi - 1$; $1/\phi^2 = 2 - \phi$.
- $\hat{n}$ — framework chirality direction (unit vector in $\mathbb{R}^4$, fixed throughout).
- $v$ — arbitrary vertex (unit vector, $|v| = 1$). $\hat{v} \equiv v/|v| = v$ since $|v| = 1$.
- $a \equiv \hat{v} \cdot \hat{n}$ — projection of $v$ onto the framework $\hat{n}$.
- $\{v_j\}_{j=1}^{12}$ — the 12 first-shell neighbors of $v$.
- $\hat{u}_j^v \equiv (v_j - v)/|v_j - v|$ — unit edge vector from $v$ toward $v_j$ (the "edge direction" entering Mechanism A's rate formula). Note $|v_j - v| = 1/\phi$ by G1 + the chord-length calculation in §3.1 below.
- $P_{\perp v}$ — projection onto the 3D hyperplane perpendicular to $\hat{v}$. Acts as $P_{\perp v} = \mathbb{1} - \hat{v}\hat{v}^T$ in matrix form.

### §2.4 First-order DI-bit current at vertex $v$

Under Mechanism A, the net DI-bit current at vertex $v$ at first order in $\delta$ is (per Phase 1 derivation, generalized in Patch 0533 §9.2):

$$\vec{j}_{DI}^{net}(v) = 2 r_0 \delta \sum_{j=1}^{12} (\hat{u}_j^v \cdot \hat{n})\,\hat{u}_j^v + \mathcal{O}(\delta^2)$$

The factor of 2 comes from the antisymmetric pairing of outgoing minus incoming rates along each edge per Phase 1 §11; the sum is over the 12 first-shell neighbors per Reading C (higher shells enter at $\mathcal{O}(\delta^2)$ via two-step paths).

**The target of this Layer 3 derivation:** evaluate $\sum_{j=1}^{12} (\hat{u}_j^v \cdot \hat{n})\,\hat{u}_j^v$ in closed form for arbitrary $v$.

---

## §3 Geometric setup at general vertex — Identities I1 and I2

### §3.1 Identity I1 — 600-cell first-shell vertex-projection

**Statement (I1):**

$$\boxed{\;\hat{u}_j^v \cdot \hat{v} = -\frac{1}{2\phi} \quad \text{uniform across all 12 first-shell neighbors $v_j$ of $v$}\;}$$

**Derivation:**

By G1, $v \cdot v_j = \phi/2$. The chord length:

$$|v_j - v|^2 = |v_j|^2 + |v|^2 - 2(v_j \cdot v) = 1 + 1 - 2\cdot\frac{\phi}{2} = 2 - \phi$$

Using $\phi^2 = \phi + 1$:

$$2 - \phi = \frac{(2-\phi)(\phi+1)}{\phi+1} = \frac{2\phi + 2 - \phi^2 - \phi}{\phi+1} = \frac{\phi + 2 - (\phi+1)}{\phi+1} = \frac{1}{\phi+1} = \frac{1}{\phi^2}$$

Therefore $|v_j - v| = 1/\phi$, consistent with the 600-cell edge length.

Now compute $\hat{u}_j^v \cdot \hat{v}$:

$$\hat{u}_j^v \cdot \hat{v} = \frac{(v_j - v) \cdot v}{|v_j - v|} = \frac{(v_j \cdot v) - |v|^2}{1/\phi} = \phi\left(\frac{\phi}{2} - 1\right) = \frac{\phi^2}{2} - \phi$$

Using $\phi^2 = \phi + 1$:

$$\frac{\phi^2}{2} - \phi = \frac{\phi + 1}{2} - \phi = \frac{\phi + 1 - 2\phi}{2} = \frac{1 - \phi}{2}$$

Using $1 - \phi = -1/\phi$ (equivalent to $1/\phi = \phi - 1$):

$$\frac{1 - \phi}{2} = -\frac{1}{2\phi}$$

Therefore $\hat{u}_j^v \cdot \hat{v} = -1/(2\phi)$, uniform across all 12 $j$. □

**Remark.** The negative sign is geometrically intuitive: $\hat{u}_j^v$ points from $v$ outward to $v_j$, but the 12 first-shell neighbors sit on the "far side" of the 600-cell from the antipodal direction $+\hat{v}$, so their edge vectors have negative $\hat{v}$-component. The uniform magnitude $1/(2\phi)$ comes from the rigid 36° polar angle in G1.

### §3.2 Identity I2 — Perpendicular-magnitude

Decompose each $\hat{u}_j^v$ into $\hat{v}$-parallel and $\hat{v}$-perpendicular parts:

$$\hat{u}_j^v = \alpha\hat{v} + \beta\hat{w}_j^v, \quad \alpha = \hat{u}_j^v \cdot \hat{v} = -\frac{1}{2\phi} \text{ (by I1)}, \quad \beta = |\perp_j^v|, \quad \hat{w}_j^v \in H_\perp^v$$

where $H_\perp^v$ is the 3D hyperplane perpendicular to $\hat{v}$ and $\hat{w}_j^v$ is the unit vector in $H_\perp^v$ along the perpendicular component of $\hat{u}_j^v$.

**Statement (I2):**

$$\boxed{\;|\perp_j^v|^2 = \frac{2+\phi}{4}, \quad \text{equivalently } \beta = \frac{\sqrt{2+\phi}}{2} \quad \text{uniform across all 12 $j$}\;}$$

**Derivation:**

Unitarity of $\hat{u}_j^v$ gives $\alpha^2 + \beta^2 = 1$, so:

$$|\perp_j^v|^2 = \beta^2 = 1 - \alpha^2 = 1 - \frac{1}{4\phi^2}$$

Substituting $1/\phi^2 = 2 - \phi$:

$$1 - \frac{1}{4\phi^2} = 1 - \frac{2-\phi}{4} = \frac{4 - (2-\phi)}{4} = \frac{2+\phi}{4}$$

Therefore $\beta^2 = (2+\phi)/4$, and $\beta = \sqrt{2+\phi}/2$. □

**Verification via alternative algebra:**

$$|\perp_j^v|^2 = 1 - \frac{1}{4\phi^2} = \frac{4\phi^2 - 1}{4\phi^2} = \frac{4(\phi+1) - 1}{4(\phi+1)} = \frac{4\phi + 3}{4(\phi+1)}$$

The claim $(2+\phi)/4 = (4\phi+3)/(4(\phi+1))$ requires $(2+\phi)(\phi+1) = 4\phi + 3$:

$$(2+\phi)(\phi+1) = 2\phi + 2 + \phi^2 + \phi = 3\phi + 2 + (\phi+1) = 4\phi + 3 \quad \checkmark$$

Both forms agree. The first form $(2+\phi)/4$ is the more compact statement.

### §3.3 The link icosahedron

By G2, the 12 first-shell neighbors $\{v_j\}$ form a regular icosahedron in the 3D hyperplane $H_\perp^v$ (the link of $v$). Correspondingly, the 12 unit vectors $\{\hat{w}_j^v\}_{j=1}^{12}$ are exactly the 12 vertex-direction unit vectors of a regular icosahedron centered at the origin of $H_\perp^v$.

This is the geometric structure that load-bears Identities I3 and I4 below.

The icosahedral group $I_h$ (order 120) acts on $H_\perp^v$ as its standard 3D representation, permuting the 12 $\{\hat{w}_j^v\}$ among themselves.

---

## §4 Identity I3 — Icosahedral central symmetry

**Statement (I3):**

$$\boxed{\;\sum_{j=1}^{12} \hat{w}_j^v = 0\;}$$

**Derivation:**

The regular icosahedron has central inversion symmetry: the linear map $-\mathbb{1}: H_\perp^v \to H_\perp^v$ (which sends $\hat{w} \mapsto -\hat{w}$) is an element of the icosahedral group $I_h$ (specifically, $-\mathbb{1}$ is the central element of $I_h = I \times \{+\mathbb{1}, -\mathbb{1}\}$ where $I$ is the rotation subgroup).

The 12 icosahedron vertices therefore decompose into 6 antipodal pairs $(\hat{w}_j^v, \hat{w}_{j'}^v)$ with $\hat{w}_{j'}^v = -\hat{w}_j^v$.

Each pair sums to zero:

$$\hat{w}_j^v + \hat{w}_{j'}^v = \hat{w}_j^v + (-\hat{w}_j^v) = 0$$

The total sum over the 12 vertices is the sum of 6 pair-sums, each zero:

$$\sum_{j=1}^{12} \hat{w}_j^v = \sum_{\text{pairs}}\big(\hat{w}_j^v + \hat{w}_{j'}^v\big) = 0$$

□

**Remark — I3 does NOT require Schur's lemma.** The result follows from elementary antipodal-pair cancellation. This is important: I3 and I4 are independent identities, and conflating them as "by Schur's lemma both sum identities follow" would obscure the structural content. Only I4 (the *tensor* sum) requires the Schur-lemma machinery.

---

## §5 Identity I4 — Icosahedron tensor sum isotropy via Schur's lemma

**Statement (I4):**

$$\boxed{\;\sum_{j=1}^{12} \hat{w}_j^v \otimes \hat{w}_j^v = 4\,P_{\perp v}\;}$$

where $P_{\perp v}: \mathbb{R}^4 \to H_\perp^v$ is the projection onto the 3D hyperplane perpendicular to $\hat{v}$ (acting as the identity on $H_\perp^v$ and as zero on $\hat{v}$).

**Derivation:**

Define the tensor:

$$T \equiv \sum_{j=1}^{12} \hat{w}_j^v \otimes \hat{w}_j^v$$

$T$ is a symmetric rank-2 tensor on $H_\perp^v$ (which is 3-dimensional).

**Step 1 — $T$ is $I_h$-invariant.**

For any group element $g \in I_h$ acting on $H_\perp^v$, conjugation acts as:

$$g T g^{-1} = \sum_{j=1}^{12} (g\hat{w}_j^v) \otimes (g\hat{w}_j^v)$$

Since $I_h$ permutes the 12 icosahedron vertex directions $\{\hat{w}_j^v\}$ among themselves (G2), the right-hand sum is identical to the original sum up to re-indexing:

$$\sum_{j=1}^{12} (g\hat{w}_j^v) \otimes (g\hat{w}_j^v) = \sum_{j'=1}^{12} \hat{w}_{j'}^v \otimes \hat{w}_{j'}^v = T$$

Therefore $g T g^{-1} = T$ for all $g \in I_h$, i.e., $T$ commutes with the $I_h$-action on $H_\perp^v$.

**Step 2 — Schur's lemma forces $T = c \cdot P_{\perp v}$ for some scalar $c$.**

The 3D action of $I_h$ on $H_\perp^v$ is the standard 3D irreducible representation (the $T_{1u}$ or $T_1$ irrep in Mulliken notation; this is the unique 3D irrep of $I_h$ that acts faithfully).

Schur's lemma (applied to the real form of an irreducible representation over $\mathbb{R}$): any symmetric tensor on a real irreducible representation that commutes with the group action is a scalar multiple of the identity (where the identity is taken in the representation space).

Since $T$ acts on $H_\perp^v$ (3D) and commutes with the $I_h$-action (Step 1), Schur gives:

$$T\big|_{H_\perp^v} = c \cdot \mathbb{1}_{H_\perp^v} \quad \text{for some scalar } c \in \mathbb{R}$$

Extended to the full ambient $\mathbb{R}^4$ as a rank-2 tensor (with $T$ acting as zero on $\hat{v}$ since each $\hat{w}_j^v \in H_\perp^v$):

$$T = c \cdot P_{\perp v}$$

**Step 3 — Compute $c$ via trace.**

The trace of $T$ on $H_\perp^v$ is:

$$\text{tr}_{H_\perp^v}(T) = \sum_{j=1}^{12} |\hat{w}_j^v|^2 = 12 \cdot 1 = 12$$

The trace of $c \cdot P_{\perp v}$ on $H_\perp^v$ is:

$$\text{tr}_{H_\perp^v}(c\cdot P_{\perp v}) = c \cdot \text{tr}_{H_\perp^v}(\mathbb{1}_{H_\perp^v}) = c \cdot 3 = 3c$$

Equating:

$$12 = 3c \quad \Longrightarrow \quad c = 4$$

Therefore $T = 4 P_{\perp v}$. □

**Remark — why Schur is essential here.** Unlike I3 (which falls out of antipodal-pair cancellation elementary-style), I4 requires the full rep-theoretic statement that the 3D action of $I_h$ on the icosahedral link is irreducible. Without irreducibility, $T$ could be a nontrivial diagonal matrix in some $I_h$-invariant basis decomposition; Schur's lemma is what forces the isotropy (every direction in $H_\perp^v$ is treated identically).

The structure of $I_h$ over $\mathbb{R}$ has exactly one faithful 3D irrep (the "vector" representation), so there is no ambiguity about which irrep $H_\perp^v$ carries.

**Remark — application of Schur on real vs. complex irreps.** $I_h$ is a real reflection group; its 3D vector representation is real-irreducible (does not decompose over $\mathbb{R}$). The Schur statement applied here is the real form: for a real-irreducible representation of a finite group on a real vector space, the commutant of the group action in the space of symmetric tensors is one-dimensional (spanned by the identity). This is a direct consequence of complex Schur + the fact that the 3D rep of $I_h$ is of real type (Frobenius-Schur indicator $+1$), so no degeneracy or quaternionic structure modifies the result.

---

## §6 Main derivation — expansion of $\sum_j (\hat{u}_j^v \cdot \hat{n})\hat{u}_j^v$

Substitute the decomposition $\hat{u}_j^v = \alpha\hat{v} + \beta\hat{w}_j^v$ (from §3.2) into the target sum. Define $a \equiv \hat{v}\cdot\hat{n}$.

### §6.1 Compute $\hat{u}_j^v \cdot \hat{n}$

$$\hat{u}_j^v \cdot \hat{n} = (\alpha\hat{v} + \beta\hat{w}_j^v) \cdot \hat{n} = \alpha a + \beta(\hat{w}_j^v \cdot \hat{n})$$

### §6.2 Expand the product

$$(\hat{u}_j^v \cdot \hat{n})\hat{u}_j^v = \big[\alpha a + \beta(\hat{w}_j^v\cdot\hat{n})\big]\big[\alpha\hat{v} + \beta\hat{w}_j^v\big]$$

Expanding the product:

$$(\hat{u}_j^v \cdot \hat{n})\hat{u}_j^v = \underbrace{\alpha^2 a\,\hat{v}}_{\text{Term A}_j} + \underbrace{\alpha\beta(\hat{w}_j^v\cdot\hat{n})\hat{v}}_{\text{Term B}_j} + \underbrace{\alpha\beta a\,\hat{w}_j^v}_{\text{Term C}_j} + \underbrace{\beta^2(\hat{w}_j^v\cdot\hat{n})\hat{w}_j^v}_{\text{Term D}_j}$$

### §6.3 Sum each term over $j = 1, \ldots, 12$

**Term A:**

$$\sum_{j=1}^{12} \text{Term A}_j = \sum_{j=1}^{12} \alpha^2 a\,\hat{v} = 12 \alpha^2 a\,\hat{v} = 12 \cdot \frac{1}{4\phi^2}\cdot a\,\hat{v} = \frac{3a}{\phi^2}\,\hat{v}$$

**Term B:**

$$\sum_{j=1}^{12} \text{Term B}_j = \alpha\beta\hat{v}\sum_{j=1}^{12} (\hat{w}_j^v\cdot\hat{n})$$

The sum factorizes as $\hat{n} \cdot (\sum_j \hat{w}_j^v) = \hat{n} \cdot \vec{0} = 0$ by **Identity I3**.

$$\sum_{j=1}^{12} \text{Term B}_j = 0$$

**Term C:**

$$\sum_{j=1}^{12} \text{Term C}_j = \alpha\beta a \sum_{j=1}^{12} \hat{w}_j^v = \alpha\beta a \cdot \vec{0} = 0$$

by **Identity I3**.

**Term D:**

$$\sum_{j=1}^{12} \text{Term D}_j = \beta^2 \sum_{j=1}^{12} (\hat{w}_j^v\cdot\hat{n})\hat{w}_j^v$$

Recognize the tensor structure: $(\hat{w}_j^v\cdot\hat{n})\hat{w}_j^v = (\hat{w}_j^v \otimes \hat{w}_j^v)\,\hat{n}$. Therefore:

$$\sum_{j=1}^{12} \text{Term D}_j = \beta^2 \left[\sum_{j=1}^{12} \hat{w}_j^v \otimes \hat{w}_j^v\right]\hat{n} = \beta^2 \cdot 4 P_{\perp v}\hat{n} = 4\beta^2 P_{\perp v}\hat{n}$$

by **Identity I4**.

Substituting $\beta^2 = (2+\phi)/4$ (Identity I2):

$$\sum_{j=1}^{12} \text{Term D}_j = 4 \cdot \frac{2+\phi}{4} \cdot P_{\perp v}\hat{n} = (2+\phi) P_{\perp v}\hat{n}$$

The projection $P_{\perp v}\hat{n} = \hat{n} - (\hat{n}\cdot\hat{v})\hat{v} = \hat{n} - a\hat{v}$, so:

$$\sum_{j=1}^{12} \text{Term D}_j = (2+\phi)(\hat{n} - a\hat{v})$$

### §6.4 Combine all four terms

$$\sum_{j=1}^{12} (\hat{u}_j^v\cdot\hat{n})\hat{u}_j^v = \frac{3a}{\phi^2}\hat{v} + 0 + 0 + (2+\phi)(\hat{n} - a\hat{v})$$

$$= (2+\phi)\hat{n} + a\left[\frac{3}{\phi^2} - (2+\phi)\right]\hat{v}$$

The bracketed coefficient $[3/\phi^2 - (2+\phi)]$ is the load-bearing golden-ratio identity, addressed in §7 below.

---

## §7 Identity I5 — Golden-ratio reduction

**Statement (I5):**

$$\boxed{\;\frac{3}{\phi^2} - (2+\phi) = -\frac{4}{\phi}\;}$$

**Derivation:**

Using $\phi^2 = \phi + 1$:

$$\frac{3}{\phi^2} - (2+\phi) = \frac{3}{\phi+1} - (2+\phi) = \frac{3 - (2+\phi)(\phi+1)}{\phi+1}$$

Compute the numerator using the result from §3.2 verification:

$$(2+\phi)(\phi+1) = 4\phi + 3$$

So:

$$\text{Numerator} = 3 - (4\phi + 3) = -4\phi$$

Therefore:

$$\frac{3}{\phi^2} - (2+\phi) = \frac{-4\phi}{\phi+1} = \frac{-4\phi}{\phi^2} = -\frac{4}{\phi}$$

(using $\phi+1 = \phi^2$ in the denominator). □

**Alternative derivation using $1/\phi^2 = 2-\phi$:**

$$\frac{3}{\phi^2} - 2 - \phi = 3(2-\phi) - 2 - \phi = 6 - 3\phi - 2 - \phi = 4 - 4\phi = 4(1-\phi) = -4(\phi - 1) = -\frac{4}{\phi}$$

(using $\phi - 1 = 1/\phi$ in the last step). Both routes give the same result. □

### §7.1 Substitute I5 into the main result

$$\sum_{j=1}^{12} (\hat{u}_j^v\cdot\hat{n})\hat{u}_j^v = (2+\phi)\hat{n} + a\cdot\left(-\frac{4}{\phi}\right)\hat{v} = (2+\phi)\hat{n} - \frac{4a}{\phi}\hat{v}$$

---

## §8 Final boxed result

Multiply by the Mechanism A first-order prefactor $2 r_0 \delta$ (per §2.4):

$$\boxed{\;\vec{j}_{DI}^{net}(v) = 2 r_0 \delta\left[(2+\phi)\hat{n} - \frac{4a}{\phi}\hat{v}\right] + \mathcal{O}(\delta^2), \quad a \equiv \hat{v}\cdot\hat{n}\;}$$

This is the general per-vertex DI-bit current formula at arbitrary vertex $v$ under the framework chirality direction $\hat{n}$.

**Layer 3 status registered:** the derivation is now fully explicit from primitives — every coefficient $(2+\phi)$ and $4/\phi$ is traced from the 600-cell first-shell geometric primitives G1 + G2 + Schur's-lemma representation theory of $I_h$ on $H_\perp^v$ + golden-ratio identity I5. The Copilot Patch 0538 §14.4 calibration concern is substantively resolved at sketch-document Layer 3 rigor.

---

## §9 Sanity check at $v = v_{\text{host}}$

At the host vertex $v = v_{\text{host}}$, the framework convention is $\hat{v} = \hat{n}$ (i.e., $v_{\text{host}}$ aligns with the framework chirality direction). Therefore $a = \hat{v}\cdot\hat{n} = 1$.

Substituting $a = 1$:

$$\vec{j}_{DI}^{net}(v_{\text{host}}) = 2 r_0 \delta\left[(2+\phi)\hat{n} - \frac{4}{\phi}\hat{n}\right] = 2 r_0 \delta\left[(2+\phi) - \frac{4}{\phi}\right]\hat{n}$$

Using Identity I5 ($3/\phi^2 - (2+\phi) = -4/\phi$, equivalently $(2+\phi) - 4/\phi = 3/\phi^2$):

$$\vec{j}_{DI}^{net}(v_{\text{host}}) = 2 r_0 \delta \cdot \frac{3}{\phi^2}\hat{n} = \frac{6 r_0 \delta}{\phi^2}\hat{n}$$

**This matches Phase 1 Finding DSL-1 (Patch 0524 boxed result) exactly.**

The sanity check is non-trivial: Phase 1 was derived from the host-vertex-specific computation with the simplifying convention $\hat{v} = \hat{n}$; the present §6–§7 derivation is the general-vertex Layer 3 closure. Internal consistency requires the general formula to specialize correctly. The specialization works via Identity I5 — the same golden-ratio reduction that gives the $-4/\phi$ coefficient in the general formula gives the $+3/\phi^2$ coefficient in the host special case.

This internal consistency between Phase 1 (vertex-aligned) and Layer 3 (general-vertex) is a structural check that the derivation has not introduced a sign error, missed term, or convention conflict.

---

## §10 Connection to Layer 2 work

### §10.1 Patch 0533 §9 immutable record

Patch 0533 §9 closed B.1.q4 at sketch Layer 2 with the boxed result and a four-line compressed algebra. That sketch is **immutable per §17.8 of `templates/operating_system.md`** — Patches 0531–0540 content is not modified inline.

This Layer 3 promotion document is a separate, additive artifact in `layer3_promotion/`. It does NOT replace, edit, or supersede Patch 0533 §9; it provides the explicit step-by-step derivation that §9.4 compressed.

### §10.2 Numerical verification preserved as independent confirmation

The verification script at `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/code/verify_b1q4_first_shell_current_sum.py` (Patch 0533) is preserved unchanged. It verifies the five load-bearing identities ($\hat{u}_i \cdot \hat{n} = -1/(2\phi)$, $\sum_i \hat{u}_i = -(6/\phi)\hat{n}$, Phase 1 result, first-shell current magnitude uniformity, B.1.q4 sum identity) at machine precision across five test $\delta$ values.

At Layer 3, the numerical verification is no longer load-bearing for the closure (the algebra is now self-sufficient), but it remains valuable as **independent confirmation** that the algebraic derivation has not made a sign error, units error, or missed-term error. The numerics passed at machine precision $\leq 2 \times 10^{-15}$; the algebra now matches this.

### §10.3 What the Layer 3 promotion resolves at programme level

Patch 0538 §14.4 calibration item:

> "Layer 3 algebraic derivation deferred to flagship paper development."

This deferral is now **substantively resolved at sketch-document Layer 3**. The flagship-paper-grade Layer 3 (publication prose + theorem-environment formatting + literature citations + full reviewer-grade rigor) remains as future work for F.1 flagship paper assembly, but the substantive algebra is done.

### §10.4 What the Layer 3 promotion does NOT promote

- The general per-vertex current formula $\vec{j}_{DI}^{net}(v)$ remains an **intermediate computational result**, not a programme-level Finding. Patch 0533 §9.12 anti-priority sustained.
- The first-shell current sum identity $\sum_i \hat{j}_{DI}^{net}(v_i) = (24/\sqrt{7-\phi})\hat{n}$ from Patch 0533 §9.6 is unchanged at sketch Layer 2; this Layer 3 promotion does NOT extend to the sum identity's promotion (that would be a separate Layer 3 promotion of the §9.6 result, not in scope here).
- The F.1 sub-question status is **unchanged** at "SUBSTANTIVE SKETCH-LEVEL CLOSURE at Layer 2" per Patch 0539 §15.2. Layer 3 promotion arc completion (across multiple targets) + Layer 3 reviewer-pause cycle + Layer 3 status upgrade are required before F.1 status changes again, per §17 codified discipline.

---

## §11 Layer 3 vs Layer 4 distinction

### §11.1 What Layer 3 establishes (this Patch)

- Closed-form algebraic derivation of the general per-vertex current formula from 600-cell first-shell geometric primitives G1 + G2 + $I_h$-symmetry + Schur's-lemma representation theory + golden-ratio identities.
- All inherited inputs are themselves substrate-level structural facts about the 600-cell polytope and the icosahedral group, not derived from CPP axioms.

### §11.2 What Layer 4 would require (deferred)

- Derive G1 (uniform 36° vertex-pair angle) and G2 (icosahedral link structure) from CPP axioms A1–A11 + polytope-emergence machinery.
- Derive the $I_h$-symmetry of the icosahedral link from the substrate-physics structure of the 600-cell as it emerges from CPP primitives (rather than treating it as inherited from the polytope's geometric description).
- Derive the golden ratio $\phi$ itself from CPP first principles rather than inheriting it from the 600-cell coordinate structure.

Layer 4 work touches the **long-term programme target** (chirality scale from polytope geometry) registered at Patch 0528 §14.17 and sustained per Patch 0539 §15.5. It is **REGISTERED + DEFERRED** behind F.1 / F.2 / F.3 stabilization.

### §11.3 Layer 3 → Layer 4 promotion path (for future reference)

If at some future point the programme attempts Layer 4 promotion of the present result, the natural sequence is:

1. Derive 600-cell first-shell structure from CPP axiom-level polytope-emergence (a long-term programme target in its own right).
2. Show that the $I_h$-symmetry of the icosahedral link is itself a derived consequence rather than an axiom-level input.
3. Re-derive Identity I4 (currently using Schur's lemma as inherited rep-theory machinery) from substrate-physics directly.
4. The golden-ratio identities I1, I2, I5 would survive unchanged as algebraic facts about $\phi$.

This sequence is **not** attempted at this Patch.

---

## §12 Self-checkpoint — three places §0–§11 could overstate

Per the §17.5 cross-reviewer convergence weighting discipline and the reviewer-pause self-checkpoint pattern established at Patch 0531 §6, three places where this Layer 3 document could overstate are flagged explicitly:

### §12.1 "Layer 3 algebraic derivation" framing

This document delivers **sketch-document Layer 3** — the explicit step-by-step algebra. It is NOT publication-grade flagship-paper Layer 3, which would require theorem-environment formatting, literature citations to Coxeter / Frobenius-Schur / standard rep-theory references, formal proofs in number-systematic structure, and reviewer-grade rigor on every cross-reference.

The scope qualifier "Layer 3 under the minimal-local-first-order realization framework + Mechanism A primitive + 600-cell first-shell geometric structure G1+G2 + Schur's-lemma rep-theory of $I_h$ on 3D" (per §8.2 of the Session 139 close handover) is preserved and load-bearing. The result is not promoted to "Layer 3 derived" or "from primitives" without that qualifier.

### §12.2 "All identities self-contained" framing

Identities I1, I2, I3, I5 are derived from primitives plus elementary algebra. Identity I4 uses **Schur's lemma applied to the standard 3D irreducible representation of $I_h$**. Schur's lemma itself is inherited mathematical machinery (it is a theorem of representation theory of finite groups over fields of characteristic zero); the 3D irreducibility of $I_h$ on the icosahedral link is inherited from G2 + standard rep theory of the icosahedral group.

The §5 derivation does not re-prove Schur's lemma or re-establish the rep-theoretic structure of $I_h$ — these are treated as inherited inputs. This is appropriate for sketch-document Layer 3 but should not be conflated with "from-scratch derivation".

### §12.3 "Internal consistency check via sanity at $v_{\text{host}}$" framing

The §9 sanity check confirms internal consistency between Phase 1 (Patch 0524) and the present Layer 3 (this Patch) at the host vertex. It does NOT establish that the Layer 3 derivation is correct independently of Phase 1; rather, it shows the two derivations are consistent with each other.

Layer 3 correctness rests on: (i) the algebraic chain in §3–§7 being free of errors, (ii) the inputs G1, G2, $I_h$-symmetry being correctly applied, (iii) Schur's lemma being correctly applied (the 3D action of $I_h$ on $H_\perp^v$ being genuinely irreducible). Numerical verification in §10.2 + sanity check in §9 are two independent confirmations; correctness rests on the algebra + the inputs, not on either confirmation alone.

---

## §13 Programme state after this Layer 3 promotion

### §13.1 What changed at programme level

- B.1.q4 is now at **sketch-document Layer 3 closure** within `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/layer3_promotion/F1_layer3_b1q4_algebraic_derivation.md` (this document).
- Patch 0538 §14.4 calibration item ("Layer 3 algebraic derivation deferred") substantively resolved at sketch-document level.
- **First Layer 3 promotion in the F.1 trajectory.** The Patch 0540 scoping document's seven Layer 3 targets table now shows Target 1 (B.1.q4) at Layer 3 closure; Targets 2–7 unchanged at sketch Layer 2.
- New directory `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/layer3_promotion/` established as venue for F.1 Layer 3 promotion work, parallel to the `reviewer_pause/` directory pattern.

### §13.2 What did NOT change

- F.1 sub-question status unchanged ("SUBSTANTIVE SKETCH-LEVEL CLOSURE at Layer 2 under the minimal-local-first-order realization framework, pending Layer 3 promotion + supplementary work").
- F.2 / F.3 substantive content trajectories remain DEFERRED.
- F.1 flagship paper assembly remains DEFERRED.
- Long-term programme target (chirality scale from polytope geometry, Layer 4) remains REGISTERED + DEFERRED.
- Six other Layer 3 promotion targets (Targets 2–7) unchanged at sketch Layer 2.
- No new Findings registered; the general per-vertex current formula remains an intermediate computational result.
- No v1.0 SHIPPED edits; no Phase 1 §11 / Phase 2 §12 modifications; no Patches 0531–0540 modifications; no reviewer-pause checkpoint modifications.
- Numerical verification script `code/verify_b1q4_first_shell_current_sum.py` unchanged.
- JUNO peer-review update integration when published — DEFERRED, unchanged.

### §13.3 Forward queue post-Patch 0541

- (A) **Patch 0542+ — next Layer 3 promotion target.** Per §4.3 of Patch 0540 scoping document, the natural next target is **Target 2 (B.2.q1 framework axiomatization of $P_{TI}$ rep theory at Layer 3)**, which opens the Priority 1 chain (Target 2 → Target 3) resolving Patch 0538 §14.1 + §14.2 calibration items in coupled fashion. Each Layer 3 promotion is its own gated trajectory per §15.7; Patch 0542 substantive opening requires Thomas's authorization at the next decision gate.
- (B) Subsequent Patches close Targets 3, 4, 5, 6, 7 per Patch 0540 §4.1 priority ordering. Aggregate timeline 10–22 sessions for the full Layer 3 promotion arc.
- (C) Layer 3 reviewer-pause cycle Patch when load-bearing arc of Layer 3 promotions completes, per §17.1 codified trigger conditions.
- (D) Layer 3 status upgrade Patch when reviewer-pause completes positively, per §17.7 status-upgrade-Patch discipline.
- (E) F.1 flagship paper assembly DEFERRED behind (C) + (D) per `templates/paper_completion_checklist.md` Reviewer-Pause Cycle Precondition section.
- (F) F.2 substantive content trajectory DEFERRED at decision-gate level pending (B), (C), (D), (E), + own decision-gate re-engagement per §17.9 (5).
- (G) F.3 substantive content trajectory DEFERRED for same reason as (F).
- (H) Long-term programme target (chirality scale from polytope geometry, Layer 4) REGISTERED + DEFERRED.
- (I) JUNO peer-review update integration when published.
- (J) Future reviewer-pause cycles on-demand at future Layer 3 closure milestones per §17 discipline.
- (K) Cross-window handover at Session 140 close per `templates/operating_system.md` §15.

### §13.4 Anti-priorities sustained going forward

All eleven anti-priorities from §0.1 of this document remain in force at subsequent Patches in the F.1 trajectory. In addition, per Session 139 close handover §8.2:

- Resist pressure to bundle Layer 3 promotion targets — each is its own gated trajectory per §15.7.
- Resist pressure to skip Layer 3 reviewer-pause cycle.
- Watch for scope-qualifier drift — when citing this B.1.q4 Layer 3 result downstream, preserve "Layer 3 under the minimal-local-first-order realization framework + Mechanism A primitive + 600-cell first-shell geometric structure G1+G2 + Schur's-lemma rep-theory of $I_h$ on 3D" qualifier. Don't reduce to "derived" or "from primitives".
- Don't promote intermediate results to Findings registry — the general per-vertex current formula remains an intermediate computational result.
- Don't propagate Layer 2 → Layer 3 promotion to other sub-questions beyond the next authorized Patch 0542+ target.

---

## §14 Closing summary

**Patch 0541 closes B.1.q4 at sketch-document Layer 3 via explicit step-by-step algebraic derivation of the general per-vertex DI-bit current formula from CPP primitives + 600-cell first-shell geometric primitives + Schur's-lemma representation theory of $I_h$ on the 3D link hyperplane.**

The five load-bearing identities I1 (vertex-projection $\hat{u}_j^v\cdot\hat{v} = -1/(2\phi)$), I2 (perpendicular-magnitude $|\perp_j^v|^2 = (2+\phi)/4$), I3 (icosahedral central symmetry $\sum_j \hat{w}_j^v = 0$, elementary), I4 (icosahedral tensor sum isotropy $\sum_j \hat{w}_j^v\otimes\hat{w}_j^v = 4P_{\perp v}$, via Schur), and I5 (golden-ratio reduction $3/\phi^2 - (2+\phi) = -4/\phi$) are each derived self-containedly. The main derivation expands $\sum_j(\hat{u}_j^v\cdot\hat{n})\hat{u}_j^v$ into four terms; Terms B and C vanish via I3; Term D contributes $(2+\phi)(\hat{n} - a\hat{v})$ via I4; combination via I5 yields the boxed result $\vec{j}_{DI}^{net}(v) = 2r_0\delta[(2+\phi)\hat{n} - (4a/\phi)\hat{v}] + \mathcal{O}(\delta^2)$. Sanity check at $v_{\text{host}}$ ($a=1$) recovers Phase 1 Finding DSL-1's $(6r_0\delta/\phi^2)\hat{n}$ exactly.

The Patch 0538 §14.4 calibration concern is substantively resolved at sketch-document Layer 3. The first Layer 3 promotion in the F.1 sub-question trajectory is complete. F.1 status unchanged; the Layer 3 promotion arc continues at Patch 0542+ with Thomas's next gated authorization (recommended next target per Patch 0540 §4.3 is Target 2 B.2.q1 framework axiomatization, opening the Priority 1 chain).

*End of B.1.q4 Layer 3 promotion document. Patch 0541, Session 140, 22 May 2026.*
