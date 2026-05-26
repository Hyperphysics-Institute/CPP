# B.1.q2 — Full 4D Curl Vanishing Theorem at Layer 3 (Schur-decomposition discretization-independent proof)

**Sub-question:** B.1.q2 — full 4D curl of the DI-bit current at $v_{\text{host}}$ at $\mathcal{O}(\delta)$ (Layer 2 closed at Patch 0535 §11; Target 6 of Patch 0540 scoping document; Layer 3 promotion opened at this Patch).

**Promotion scope:** sketch-document Layer 3 — promotes Patch 0535 §11's sketch Layer 2 zero-curl result to Layer 3 via explicit Schur-decomposition of the 4D 2-form space at $v_{\text{host}}$ under residual $I_h$ symmetry into 3D irreps $T_{1u}$ (vector-like $F_{0i}$ components) and $T_{1g}$ (pseudovector-like $F_{ij}$ components). Removes Patch 0535 §11.12(i) self-checkpoint's trapezoidal-discretization-dependence caveat — the Schur-decomposition argument is discretization-independent. Substantively addresses Patch 0535 §11.12(iii) self-checkpoint's "promotion to Layer 3 (full theorem-level rigor with explicit cage-shell-factor-style computations) is deferred" deferral.

**Patch:** 0546, Session 140 (22 May 2026), sixth Layer 3 promotion in the F.1 sub-question's trajectory.

**Two corrections from prior forward-queue language.** First, my forward queue across Patches 0541–0545 had Targets 6 and 7 reversed: the actual Patch 0540 §4.1 enumeration is Target 6 = B.1.q2 (this Patch), Target 7 = B.1.q3 (perturbation-theory propagation). Second, **Target 7 (B.1.q3) was substantively closed at Patch 0544 §6 Theorem 6.1** — the Perturbative-Locality Propagation Rule proved from Mechanism A as degree-1 polynomial + $\delta$-power expansion + connected-subgraph argument (not framework local-current-definition) meets all three Target 7 promotion criteria per Patch 0540 §2.7: independent theorem statement, removal of "within framework local-current-definition scope" qualifier from Patch 0538 §14.3, explicit propagation rule at arbitrary order. §8 of this document records this retroactive recognition formally. The Layer 3 promotion arc effectively COMPLETES at this Patch (six of seven Targets explicitly closed + Target 7 retroactively recognized as closed at Patch 0544).

---

## §0 Working-session firewall

This Patch promotes B.1.q2's sketch Layer 2 closure (Patch 0535 §11) to sketch-document Layer 3 via Schur-decomposition discretization-independent proof. The promotion is per-target and trajectory-bounded per §15.7.

### §0.1 Anti-priorities sustained at this Patch

1. **No Target 7 NEW work**; §8 of this document is a retroactive recognition of Patch 0544 §6 Theorem 6.1's already-substantive Target 7 closure, not a fresh Layer 3 promotion.
2. **No F.1 sub-question status change.** F.1 status remains "SUBSTANTIVE SKETCH-LEVEL CLOSURE at Layer 2" per Patch 0539 §15.2. Even with the Layer 3 promotion arc effectively complete at this Patch, F.1 status change requires Layer 3 reviewer-pause cycle + status upgrade Patches per §17 codified discipline.
3. **No v1.0 SHIPPED edits.**
4. **No Phase 1 §11 / Phase 2 §12 polished content modifications.**
5. **No Patches 0531–0545 immutable content modifications.** Patch 0535 §11 (Layer 2 sketch this promotion builds on) is preserved as historical record; this Layer 3 document is a separate, additive artifact in `layer3_promotion/`.
6. **No reviewer-pause checkpoint modifications.**
7. **No F.1 flagship paper assembly trigger.** Even at Layer-3-arc-complete state, flagship paper assembly requires Layer 3 reviewer-pause + Layer 3 status upgrade per §17 discipline.
8. **No higher-order extension to $\mathcal{O}(\delta^2)$** (B.1.q6 territory).
9. **No F.2 / F.3 substantive content trajectory opening.**
10. **No long-term programme target work** (Layer 4 axiomatic derivation).
11. **No promotion of the Full 4D Curl Vanishing Theorem at Layer 3 to Findings registry or theorem registry.** Findings-registry / theorem-registry promotion requires explicit registry-entry Patch with relationship_protocol.md review.

### §0.2 What this Layer 3 promotion IS

- **Explicit Schur-decomposition of the 4D 2-form space at $v_{\text{host}}$** under residual $I_h$ symmetry: $\Lambda^2(\mathbb{R}^4)|_{v_{\text{host}}} = T_{1u} \oplus T_{1g}$ (3D + 3D = 6D), with $T_{1u}$ carrying the polar-vector-like $F_{0i}$ components and $T_{1g}$ carrying the pseudovector-like $F_{ij}$ components.
- **Full 4D Curl Vanishing Theorem at Layer 3** stated as discretization-independent theorem at any 600-cell vertex with residual $I_h$ symmetry: the 4D curl 2-form of any $I_h$-covariant first-order DI-bit current vanishes at $\mathcal{O}(\delta)$.
- **Rigorous proof via Schur orthogonality** + $I_h$-invariance argument: the $I_h$-invariant component (trivial $A_g$ irrep) of $\Lambda^2(\mathbb{R}^4)|_{v_{\text{host}}}$ is zero-dimensional since neither $T_{1u}$ nor $T_{1g}$ contains $A_g$; hence any $I_h$-invariant 4D 2-form at $v_{\text{host}}$ must vanish.
- **Removal of trapezoidal-discretization caveat from Patch 0535 §11.12(i) self-checkpoint** — the Schur-decomposition argument is discretization-independent.
- **Retroactive recognition (§8) that Target 7 (B.1.q3 perturbation-theory propagation Layer 3) was substantively closed at Patch 0544 §6 Theorem 6.1.**
- **Patch 0535 §11.12(iii) self-checkpoint substantively addressed** at sketch-document Layer 3.
- **Layer 3 promotion arc effectively complete** at this Patch — six of seven Targets explicitly closed + Target 7 retroactively recognized.

### §0.3 What this Layer 3 promotion is NOT

- NOT a derivation from CPP axioms A1–A11 alone (Layer 4 territory).
- NOT an extension to $\mathcal{O}(\delta^2)$ (B.1.q6 territory).
- NOT a fresh Target 7 closure (Patch 0544 §6 already substantive).
- NOT a flagship-paper-section draft.
- NOT a promotion of the theorem to Findings registry or theorem registry.
- NOT a Layer 3 reviewer-pause cycle Patch.
- NOT a Layer 3 status upgrade Patch.
- NOT a higher-order extension of the curl-vanishing result beyond $\mathcal{O}(\delta)$ (Patch 0535 §11.11 noted $I_h$-symmetry argument extends but cancellation-mechanism details are higher-order open per B.1.q6).

---

## §1 Layer 3 promotion context

### §1.1 What Layer 2 established at Patch 0535 §11

Patch 0535 §11 closed B.1.q2 at sketch Layer 2 with **STRONGER result than the B.1.b ansatz claimed**:

- §11.5 algebraic trapezoidal-circulation cancellation on the 30 host-first-shell side-face triangles $(v_{\text{host}}, v_i, v_j)$ — uses the K3-base protection identity $\hat{e}_{ij}\cdot\hat{n} = 0$ for first-shell-to-first-shell edges (now Patch 0544 Identity G3 at Layer 3).
- §11.6 $I_h$ residual symmetry argument: 4D curl 2-form at $v_{\text{host}}$ at first order is $I_h$-invariant; the 2-form space decomposes under $I_h$ into "$F_{0i}$ vector-like" + "$F_{ij}$ dual-vector-like" 3D irreps, both non-trivial → any $I_h$-invariant 4D 2-form is zero.
- §11.7 numerical verification at machine precision $\leq 2.8 \times 10^{-17}$ for trapezoidal circulations on all 30 host-first-shell side-face triangles.
- §11.9: result stronger than B.1.b ansatz — full 4D curl 2-form vanishes (all 6 components), not only the 3 perpendicular components $F_{ij}$ the ansatz allowed to be nonzero.

### §1.2 What Patch 0535 §11.12 self-checkpoints flagged for Layer 3 work

**§11.12(i):** "The 'discrete curl via trapezoidal circulation' interpretation chosen in §11.3 is one of several possible discrete-curl operator definitions. Alternative discretizations would give consistent zero-curl results by the §11.6 $I_h$-symmetry argument, but the explicit numerical verification in §11.7 only tests the trapezoidal definition. Other discretizations are robust under $I_h$ but not numerically tested."

→ Layer 3 promotion target (per Patch 0540 §2.6): "Removal of the trapezoidal-discretization caveat from §11.12 self-checkpoint — the Schur-decomposition argument is discretization-independent and provides full Layer 3 rigor." This Patch addresses this directly by formalizing the Schur-decomposition argument explicitly at §4–§6.

**§11.12(ii):** "'The full 4D curl 2-form vanishes' in §11.6 relies on the spanning argument that the 30 face 2-forms span the 6D 2-form space at $v_{\text{host}}$. ... The 3 $\hat{n}$-aligned components $F_{0i}$ vanish by the §11.6 $I_h$-symmetry argument but are not separately probed numerically."

→ Layer 3 work: the Schur-decomposition argument directly establishes that $F_{0i}$ components transform as $T_{1u}$ irrep (non-trivial, hence any $I_h$-invariant $F_{0i}$ vanishes) without needing the spanning argument from trapezoidal circulations. §4–§5 of this Patch make this explicit.

**§11.12(iii):** "The B.1.q2 closure is at sketch Layer 2, matching the Capotauro C-W39 / B.1.d (Patch 0534) rigor level. Promotion to Layer 3 (full theorem-level rigor with explicit cage-shell-factor-style computations) is deferred."

→ This Patch's Layer 3 promotion substantively addresses (iii) by providing the Schur-decomposition full theorem-level rigor — the "explicit cage-shell-factor-style computations" parallel here is the explicit irrep decomposition $\Lambda^2(\mathbb{R}^4) \to T_{1u} \oplus T_{1g}$ at $v_{\text{host}}$.

### §1.3 Patch 0540 §2.6 Target 6 specification

Per Patch 0540 §2.6, Target 6 Layer 3 promotion target:
- Full Schur-decomposition of the 4D curl 2-form under $I_h$ residual symmetry — formal $I_h$-irrep decomposition: $F_{0i}$ vector-like irrep + $F_{ij}$ dual-vector-like irrep, both non-trivial, hence zero curl by $I_h$-invariance at any vertex with full residual $I_h$ symmetry.
- Removal of the trapezoidal-discretization caveat from §11.12 self-checkpoint.
- Explicit theorem statement at any vertex with residual $I_h$ symmetry.

Tractability: 1–2 sessions; well-defined; mostly group theory work using standard $I_h$ irrep tables. Risk: low. Value: medium.

### §1.4 Layer 3 promotion arc nearing completion

With Patch 0546 (Target 6, this Patch) closing the last remaining explicit Layer 3 promotion target, and §8's retroactive recognition that Target 7 (B.1.q3) was substantively closed at Patch 0544 §6 Theorem 6.1, the Layer 3 promotion arc launched at Patch 0540 is effectively complete:

| Target | Sub-question | Layer 3 Patch | Status |
|---|---|---|---|
| 1 | B.1.q4 algebraic derivation | Patch 0541 | CLOSED |
| 2 | B.2.q1 framework axiomatization | Patch 0542 | CLOSED |
| 3 | B.1.q1 matter-state independent derivation | Patch 0543 | CLOSED |
| 4 | B.1.d substrate-locality temporal extension | Patch 0544 | CLOSED |
| 5 | B.3.q1 Substrate-Locality Unification corollary | Patch 0545 | CLOSED |
| 6 | B.1.q2 full 4D curl Schur-decomposition | **Patch 0546 (this Patch)** | **CLOSED** |
| 7 | B.1.q3 perturbation-theory propagation | Patch 0544 §6 Theorem 6.1 (retroactive) | CLOSED |

This positions the F.1 trajectory at Layer-3-arc-complete state. Per §0.1 anti-priority 2 + 7, this state does NOT propagate to F.1 status change or flagship paper assembly — those gates require Layer 3 reviewer-pause cycle + Layer 3 status upgrade Patches per §17 codified discipline. The next gate from this Patch is Patch 0547 = Layer 3 reviewer-pause cycle Patch.

---

## §2 Primitives and inputs

### §2.1 CPP framework primitives (inherited)

- **A1, A11** + **Reading C (vertex-aligned)** + **600-cell geometric primitives** G1 + G2.
- **First-shell vertex parameterization** $v_j = v_{\text{host}} + \phi^{-1}\hat{u}_j$ (Patch 0541 §3).
- **Patch 0541 Identity I1**: $\hat{u}_j\cdot\hat{n} = -1/(2\phi)$ uniform.
- **Patch 0544 Identity G3**: $\hat{e}_{ij}\cdot\hat{n} = 0$ for first-shell-to-first-shell edges.

### §2.2 Patch 0535 §11 Layer 2 source results

- §11.5 trapezoidal-circulation cancellation on 30 host-first-shell side-face triangles.
- §11.6 $I_h$ residual symmetry argument with informal $F_{0i}$ + $F_{ij}$ decomposition.
- §11.7 numerical verification at machine precision $\leq 2.8 \times 10^{-17}$.

### §2.3 Patch 0543 §3 icosahedral irrep tables (Layer 3 inputs)

- $I_h$ has 10 irreps: $A_g, A_u, T_{1g}, T_{1u}, T_{2g}, T_{2u}, G_g, G_u, H_g, H_u$ of dimensions $1, 1, 3, 3, 3, 3, 4, 4, 5, 5$.
- $T_{1u}$: 3D polar-vector irrep (ordinary vectors).
- $T_{1g}$: 3D axial-vector / pseudovector irrep.
- $A_g$: trivial irrep ($I_h$-invariant).
- The character table + Frobenius-Schur indicators were established at Patch 0543 §2.2.

### §2.4 4D 2-form algebra (standard differential-geometry)

The space of 2-forms on $\mathbb{R}^4$ has dimension $\binom{4}{2} = 6$. At a basepoint where $\hat{n}$ is a distinguished direction (here $\hat{n} = \hat{v}_{\text{host}}$ per Reading C), and the orthogonal complement is the 3D tangent hyperplane $H_{v_{\text{host}}}$ spanned by basis $\{\hat{e}_1, \hat{e}_2, \hat{e}_3\}$, the 2-form basis is:

- $\{dx^0 \wedge dx^i\}_{i=1,2,3}$: 3 "$\hat{n}$-aligned" components $F_{0i}$.
- $\{dx^i \wedge dx^j\}_{i<j; i,j=1,2,3}$: 3 "perpendicular" components $F_{ij}$.

Total: 3 + 3 = 6 = $\dim\Lambda^2(\mathbb{R}^4)$ ✓.

---

## §3 The 4D 2-form space at $v_{\text{host}}$ under residual $I_h$

### §3.1 Residual $I_h$ action

Per Patch 0541/0543/0544 setup, the residual symmetry at $v_{\text{host}}$ (the stabilizer of $v_{\text{host}}$ in the 600-cell symmetry group) is $I_h$. This $I_h$ acts on the 3D tangent hyperplane $H_{v_{\text{host}}}$ (perpendicular to $\hat{v}_{\text{host}}$ in 4D) as the standard icosahedral 3D rotation + reflection group, with $\hat{v}_{\text{host}} = \hat{n}$ fixed.

The $I_h$-action on 4D space at $v_{\text{host}}$ is therefore: $\hat{n}$-component fixed (transforms as 1D trivial $A_g$); 3D tangent component transforms as 3D polar vector ($T_{1u}$).

### §3.2 Induced action on 4D 2-forms

The space $\Lambda^2(\mathbb{R}^4)|_{v_{\text{host}}}$ inherits an $I_h$-action from the $I_h$-action on $\mathbb{R}^4$ at $v_{\text{host}}$: for $g \in I_h$ and 2-form $\omega$, $(g\cdot\omega)(v_1, v_2) = \omega(g^{-1}v_1, g^{-1}v_2)$.

Decomposing $\Lambda^2(\mathbb{R}^4)$ under $I_h$ requires decomposing $\mathbb{R}^4 = \langle\hat{n}\rangle \oplus H_{v_{\text{host}}}$, which transforms as $A_g \oplus T_{1u}$ under $I_h$:

$$\Lambda^2(\mathbb{R}^4)|_{v_{\text{host}}} \cong \Lambda^2(A_g \oplus T_{1u}) = (A_g \otimes T_{1u}) \oplus \Lambda^2(T_{1u})$$

where the first term arises from "mixed" 2-forms involving one $\hat{n}$-direction + one tangent direction (i.e., $F_{0i}$ components), and the second term arises from 2-forms involving two tangent directions ($F_{ij}$ components).

### §3.3 Computation of $A_g \otimes T_{1u}$

Tensor product of trivial $A_g$ with 3D polar-vector $T_{1u}$:

$$A_g \otimes T_{1u} = T_{1u}$$

(any irrep tensored with trivial is itself). So the $F_{0i}$ components transform as $T_{1u}$ irrep (3D polar vector) under $I_h$.

### §3.4 Computation of $\Lambda^2(T_{1u})$

The antisymmetric square of the 3D polar-vector irrep $T_{1u}$ under $I_h$ is the 3D axial-vector / pseudovector irrep $T_{1g}$:

$$\Lambda^2(T_{1u}) = T_{1g}$$

This follows from standard rep theory: for 3D polar vectors $v$, the antisymmetric tensor $v\wedge w$ behaves as an axial vector (cross-product $v\times w$). Under inversion: $v, w \to -v, -w$ so $v\wedge w \to v\wedge w$ (even under inversion, hence $g$ subscript). The $T_1$ structure carries over. Combined: $T_{1u} \otimes_{\text{antisym}} T_{1u} = T_{1g}$.

### §3.5 The Schur-decomposition

Combining §3.3 + §3.4:

$$\boxed{\Lambda^2(\mathbb{R}^4)|_{v_{\text{host}}} = T_{1u} \oplus T_{1g} \quad \text{(under } I_h \text{ residual symmetry)}}$$

with:
- **$T_{1u}$ component (3D, polar-vector-like)**: $F_{0i}$ for $i \in \{1, 2, 3\}$ — "$\hat{n}$-aligned" 2-form components.
- **$T_{1g}$ component (3D, pseudovector-like)**: $F_{ij}$ for $i, j \in \{1, 2, 3\}$ antisymmetric — "perpendicular" 2-form components.

Total dimension: $3 + 3 = 6 = \dim\Lambda^2(\mathbb{R}^4)$ ✓.

**Critical fact: neither $T_{1u}$ nor $T_{1g}$ is the trivial $A_g$ irrep.** Both are 3D non-trivial irreps in the $I_h$ character table (Patch 0543 §2.2). The trivial-irrep ($A_g$) component of $\Lambda^2(\mathbb{R}^4)|_{v_{\text{host}}}$ under $I_h$ is zero-dimensional.

---

## §4 The Full 4D Curl Vanishing Theorem at Layer 3

### §4.1 Theorem statement

**Theorem 4.1.1 (Full 4D Curl Vanishing at Layer 3, B.1.q2).**

Let $\mathcal{P}$ be a CPP framework satisfying A1, A11, vertex-aligned Reading C. Let $v_*$ be any 600-cell vertex with residual $I_h$ symmetry (i.e., any 600-cell vertex; the 600-cell is vertex-transitive under its symmetry group, with stabilizer $I_h$ at each vertex). Let $\vec{j}_{DI}^{net}$ be the DI-bit current field at $\mathcal{O}(\delta)$. Then the 4D curl 2-form $F = d\vec{j}_{DI}^{net}|_{v_*}$ vanishes at $v_*$:

$$F = d\vec{j}_{DI}^{net}|_{v_*} = 0 \quad \text{at } \mathcal{O}(\delta)$$

with all 6 components vanishing: 3 "$\hat{n}$-aligned" components $F_{0i}$ AND 3 "perpendicular" components $F_{ij}$.

**Improvement over Patch 0535 §11.6:** the Layer 3 statement is **discretization-independent** — derived from the Schur-decomposition of $\Lambda^2(\mathbb{R}^4)|_{v_*}$ under residual $I_h$ + $I_h$-invariance of the curl 2-form, not from any specific discrete-curl operator (trapezoidal or otherwise). This removes the Patch 0535 §11.12(i) self-checkpoint trapezoidal-discretization caveat.

### §4.2 Why the theorem applies to ANY 600-cell vertex (not only $v_{\text{host}}$)

Patch 0535 §11 framed the curl-vanishing result at $v_{\text{host}}$ specifically. The Layer 3 theorem generalizes: by 600-cell vertex-transitivity, the same residual $I_h$ symmetry applies at EVERY 600-cell vertex; therefore the Layer 3 theorem applies uniformly across the substrate. This is a structural strengthening — at every 600-cell vertex, the 4D curl of the DI-bit current vanishes at $\mathcal{O}(\delta)$.

---

## §5 Rigorous proof at Layer 3

### §5.1 Setup

Let $F = d\vec{j}_{DI}^{net}|_{v_*}$ at $\mathcal{O}(\delta)$. By the first-order perturbation construction of $\vec{j}_{DI}^{net}$ (Mechanism A primitive + Reading C + 600-cell substrate), the current field is $I_h$-covariant at $v_*$ — its construction depends only on the $I_h$-symmetric 600-cell structure + the $I_h$-invariant chirality direction $\hat{n} = \hat{v}_*$.

Therefore the curl 2-form $F$ at $v_*$ is $I_h$-INVARIANT: $g\cdot F = F$ for all $g \in I_h$ acting on 2-forms at $v_*$.

### §5.2 The proof

**Claim:** $F = 0$ at $v_*$ at $\mathcal{O}(\delta)$.

**Proof.** By Maschke + character orthogonality (Patch 0542 §3.2 + Patch 0543 §3 machinery applied to $I_h$ acting on $\Lambda^2(\mathbb{R}^4)|_{v_*}$), the 2-form space decomposes uniquely into $I_h$-isotypic components. Per §3.5:

$$\Lambda^2(\mathbb{R}^4)|_{v_*} = T_{1u} \oplus T_{1g}$$

The trivial $A_g$ isotypic component has dimension 0 in this decomposition — i.e., the $I_h$-invariant subspace of $\Lambda^2(\mathbb{R}^4)|_{v_*}$ is $\{0\}$.

Since $F$ is $I_h$-invariant (per §5.1), $F$ lies in the trivial $A_g$ isotypic component of $\Lambda^2(\mathbb{R}^4)|_{v_*}$. But this component is zero-dimensional. Therefore $F = 0$. $\square$

### §5.3 Discretization-independence of the proof

The proof at §5.2 uses:
(i) $I_h$-covariance of the DI-bit current at $\mathcal{O}(\delta)$ (from CPP primitives + Reading C).
(ii) Schur-decomposition $\Lambda^2(\mathbb{R}^4)|_{v_*} = T_{1u} \oplus T_{1g}$ (from $I_h$ rep theory).
(iii) Absence of trivial $A_g$ component in this decomposition.

None of these depend on a specific discrete-curl operator (trapezoidal, simplicial cohomology, dual-lattice, etc.). The Schur-decomposition is a property of the continuum 2-form space at $v_*$; the $I_h$-covariance of the current is a property of CPP primitives + Reading C. Therefore the proof is **discretization-independent**: the curl 2-form vanishes regardless of which discrete-curl operator is used to compute it from per-vertex current values.

This addresses Patch 0535 §11.12(i) self-checkpoint's concern that "alternative discretizations would give consistent zero-curl results by the §11.6 $I_h$-symmetry argument, but the explicit numerical verification in §11.7 only tests the trapezoidal definition." The Layer 3 Schur-decomposition argument confirms zero-curl across ALL $I_h$-respecting discretizations without separate numerical verification of each.

---

## §6 What this Layer 3 promotion accomplishes

### §6.1 Result stronger than Patch 0535 §11.6

Patch 0535 §11.6 stated: "the 4D 2-form space at $v_{\text{host}}$ decomposes under $I_h$ into two 3D irreps (the $F_{0i}$ and $F_{ij}$ components)... no trivial sub-representation; therefore any $I_h$-invariant 4D 2-form is zero." This was an informal statement of the Schur-decomposition argument at sketch Layer 2.

This Patch's §3 + §4 + §5 formalize this at Layer 3:
- §3 identifies the 3D irreps explicitly as $T_{1u}$ (for $F_{0i}$) and $T_{1g}$ (for $F_{ij}$) via standard $I_h$ rep theory.
- §3.3 + §3.4 derives the decomposition $\Lambda^2(\mathbb{R}^4) = T_{1u} \oplus T_{1g}$ via tensor product + antisymmetric square computations.
- §4.1 states the full theorem at Layer 3.
- §5.2 proves it rigorously via Maschke + Schur orthogonality.

### §6.2 Removal of trapezoidal-discretization caveat from Patch 0535 §11.12(i)

The §5.3 discretization-independence argument substantively removes the Patch 0535 §11.12(i) self-checkpoint's caveat. Layer 3 promotion provides full discretization-independent rigor.

### §6.3 Patch 0535 §11.12(iii) substantively addressed

§11.12(iii) flagged: "Promotion to Layer 3 (full theorem-level rigor with explicit cage-shell-factor-style computations) is deferred." This Patch provides:
- Full theorem-level rigor (§4–§5).
- Explicit irrep-decomposition computation $\Lambda^2(\mathbb{R}^4) = T_{1u} \oplus T_{1g}$ (the "cage-shell-factor-style computation" parallel here is the irrep enumeration + Schur-orthogonality argument).

§11.12(iii) is therefore substantively addressed at sketch-document Layer 3.

---

## §7 Connection to K3-base protection identity (Patch 0544 Identity G3)

### §7.1 The K3-base protection identity at Layer 3

Patch 0535 §11.8 noted the methodological observation: the K3-base protection identity $\hat{e}_{ij}\cdot\hat{n} = 0$ (now Patch 0544 Identity G3 at Layer 3) is doing remarkable structural work — yielding three distinct programme results:
- Capotauro v2.0: K3-base protection from spatial-sector edge-length perturbation at $\mathcal{O}(\varepsilon)$.
- Patch 0534 §10.3 / Patch 0544 (B.1.d): zero first-shell-to-first-shell temporal-sector Mechanism A rate perturbation at $\mathcal{O}(\delta)$.
- Patch 0535 §11 / this Patch (B.1.q2): zero curl at $v_{\text{host}}$ at $\mathcal{O}(\delta)$.

### §7.2 At Layer 3, the K3-base protection identity provides the LATTICE-LEVEL proof complement to the CONTINUUM-LEVEL Schur-decomposition

The Layer 3 Schur-decomposition argument (§5.2) operates at the CONTINUUM level — properties of the 2-form vector space $\Lambda^2(\mathbb{R}^4)|_{v_*}$ under $I_h$ rep theory. The Patch 0535 §11.5 trapezoidal-circulation computation operates at the LATTICE level — explicit per-triangle circulation calculations using Patch 0544 Identity G3.

Both establish zero curl, and they are complementary:
- The Schur-decomposition argument is discretization-independent and applies at every vertex with residual $I_h$.
- The trapezoidal-circulation computation is discretization-specific but gives an explicit machine-precision-numerical verification.

The Layer 3 promotion does NOT supersede the Patch 0535 §11.5 trapezoidal computation; it provides a discretization-independent argument that subsumes its conclusion while preserving the lattice-level verification as an independent confirmation.

---

## §8 Retroactive recognition: Target 7 (B.1.q3 perturbation-theory propagation Layer 3) substantively closed at Patch 0544 §6 Theorem 6.1

### §8.1 The observation

Patch 0540 §2.7 specified Target 7 (B.1.q3 perturbation-theory propagation Layer 3 theorem) with three promotion criteria:
- (i) Independent theorem statement: at $\mathcal{O}(\delta^n)$, the substrate's net DI-bit current at $v_{\text{host}}$ depends only on the first $n$ shells of vertices.
- (ii) Removal of "within framework local-current-definition scope" qualifier (Patch 0538 §14.3 calibration).
- (iii) Explicit perturbation-theory propagation rule statement covering Mechanism A primitive at arbitrary order in $\delta$.

Patch 0544 §6 stated **Theorem 6.1 (Perturbative-Locality Propagation Rule)**: $\vec{j}_{DI}^{net}(v_*)$ at $\mathcal{O}(\delta^n)$ depends only on the substrate-physics content of edges within graph-distance $n$ of $v_*$ in the 600-cell edge graph. Proved via Mechanism A as degree-1 polynomial in $\delta$ per edge + $\delta$-power expansion + connected-subgraph argument.

### §8.2 The retroactive recognition

Theorem 6.1 from Patch 0544 §6 substantively meets all three Target 7 promotion criteria:

(i) ✓ **Independent theorem statement** at $\mathcal{O}(\delta^n)$ for graph-distance-$n$ edges (equivalent to first-$n$-shells of vertices, since each "shell" is a graph-distance ring around $v_*$).

(ii) ✓ **Removal of "within framework local-current-definition scope" qualifier.** The proof at Patch 0544 §6.2 derives the locality from Mechanism A + $\delta$-expansion + connected-subgraph argument — NOT from framework local-current-definition + standard perturbation-theory propagation rules. The Layer 3 derivation is independent.

(iii) ✓ **Explicit perturbation-theory propagation rule covering Mechanism A primitive at arbitrary order in $\delta$.** Theorem 6.1's statement is at general $n$, and the proof handles arbitrary $n$.

Therefore Target 7 (B.1.q3 perturbation-theory propagation Layer 3) was substantively closed at Patch 0544 §6 Theorem 6.1 — even though Patch 0544 framed Theorem 6.1 as supporting Target 4 part (c). The methodology used in Patch 0544 §6 was naturally broader than the narrowest interpretation of Target 4, with the broader scope satisfying Target 7's promotion criteria as a bonus.

### §8.3 Why retroactive recognition vs fresh Layer 3 closure Patch

Three considerations:

(a) **The Layer 3 work at Patch 0544 §6 is already substantive at Layer 3 rigor.** Re-authoring the same theorem in a separate Patch 0547 would be duplicative, not additive.

(b) **METH-L2-009 (cross-target-dependency-chain) precedent applies in reverse direction.** METH-L2-009 noted that when Target B depends on Target A, executing Target A first lets Target B close as a derived consequence. Here, the dependency direction is reversed: Target 7's propagation rule is methodologically a prerequisite for Target 4's substrate-locality, so closing Target 4 (which required proving the propagation rule) also closed Target 7.

(c) **Patch 0540 §6.1 noted "Two-pronged dependency structure enables parallel work threads."** The retroactive recognition that Target 4 + Target 7 share their load-bearing theorem (Patch 0544 §6 Theorem 6.1) is an empirical confirmation of this parallel-thread structure.

### §8.4 Status of Target 7 after this recognition

Target 7 (B.1.q3 perturbation-theory propagation Layer 3) is **CLOSED at sketch-document Layer 3** via Patch 0544 §6 Theorem 6.1. The closure date is recorded as Patch 0544 (the original substantive work) with retroactive recognition at this Patch 0546 (§8).

Patch 0538 §14.3 calibration item ("within framework local-current-definition scope" qualifier) is substantively addressed at Layer 3 by Patch 0544 §6.2's independent derivation.

### §8.5 Layer 3 promotion arc effectively complete

With this retroactive recognition, ALL SEVEN Layer 3 promotion targets in the Patch 0540 enumeration are now closed at sketch-document Layer 3. The Layer 3 promotion arc launched at Patch 0540 is effectively complete:

| Target | Sub-question | Layer 3 Patch | Status |
|---|---|---|---|
| 1 | B.1.q4 algebraic derivation | Patch 0541 | CLOSED |
| 2 | B.2.q1 framework axiomatization | Patch 0542 | CLOSED |
| 3 | B.1.q1 matter-state independent derivation | Patch 0543 | CLOSED |
| 4 | B.1.d substrate-locality temporal extension | Patch 0544 | CLOSED |
| 5 | B.3.q1 Substrate-Locality Unification corollary | Patch 0545 | CLOSED |
| 6 | B.1.q2 full 4D curl Schur-decomposition | Patch 0546 (this Patch) | CLOSED |
| 7 | B.1.q3 perturbation-theory propagation | Patch 0544 §6 Theorem 6.1 (retroactive) | CLOSED |

Per §0.1 anti-priorities 2 + 7 + Patch 0540 §5, the Layer-3-arc-complete state does NOT auto-propagate to F.1 sub-question status change or flagship paper assembly trigger. The next gate is **Patch 0547 = Layer 3 reviewer-pause cycle Patch** per Patch 0540 §5.1 codified workflow + §17 reviewer-pause discipline.

---

## §9 Connection to Layer 2 work + forward queue

### §9.1 Patch 0535 §11 immutable

Patch 0535 §11 (the Layer 2 sketch this promotion builds on) is preserved as immutable historical record per §17.8. This Layer 3 document is ADDITIVE.

### §9.2 What this Layer 3 promotion does NOT do

- Does NOT promote the Full 4D Curl Vanishing Theorem to programme-level Findings registry or theorem registry.
- Does NOT trigger F.1 sub-question status change.
- Does NOT trigger flagship paper assembly.

### §9.3 Forward queue post-Patch 0546

(A) **Patch 0547 = Layer 3 reviewer-pause cycle Patch** per Patch 0540 §5.1 codified workflow. With all seven Layer 3 targets closed at sketch-document Layer 3, the Layer 3 reviewer-pause cycle is the operative next gate.

(B) Following reviewer-pause completion: Layer 3 status upgrade Patch.

(C) F.1 flagship paper assembly DEFERRED behind (A) + (B).

(D) F.2 / F.3 substantive content trajectories DEFERRED at decision-gate level.

(E) Long-term programme target (Layer 4) REGISTERED + DEFERRED.

(F) JUNO peer-review update integration when published.

---

## §10 Layer 3 vs Layer 4 distinction

### §10.1 What Layer 3 establishes (this Patch)

- Full 4D Curl Vanishing Theorem at sketch-document Layer 3 (Theorem 4.1.1).
- Schur-decomposition $\Lambda^2(\mathbb{R}^4)|_{v_*} = T_{1u} \oplus T_{1g}$ at every 600-cell vertex with residual $I_h$.
- Discretization-independent proof (§5.3).
- Trapezoidal-discretization caveat from Patch 0535 §11.12(i) removed.
- Patch 0535 §11.12(iii) substantively addressed.

### §10.2 What Layer 4 would require (deferred)

- Derivation from CPP axioms A1-A11 alone (parallel to Layer 4 deferrals on Targets 1-6).
- Extension to $\mathcal{O}(\delta^2)$ + beyond (B.1.q6 territory; Patch 0535 §11.11 noted that the structural conclusion survives at all orders via $I_h$-symmetry, but specific cancellation mechanisms may need different per-order derivation).
- Promotion to programme-level Findings registry / theorem registry.

---

## §11 Self-checkpoint + programme state + closing summary

### §11.1 Self-checkpoint — three places §0-§10 could overstate

(i) **"Schur-decomposition discretization-independent proof" framing.** §5.3 argues that the Schur-decomposition is discretization-independent because it operates at the continuum 2-form level + $I_h$ rep theory. However, the actual computation of $F = d\vec{j}_{DI}^{net}$ as a 2-form at $v_*$ still requires some operator definition (continuum exterior derivative vs. discrete approximation). The "discretization-independence" should be read as: the conclusion (zero curl) is robust across $I_h$-respecting discretizations, not that the curl operator is discretization-free.

(ii) **"Layer 3 promotion arc effectively complete" framing (§1.4 + §8.5).** The arc is complete at SKETCH-DOCUMENT Layer 3 — the level matching Capotauro v2.0 §3 publication-grade Layer 3 internally but not yet published or reviewer-pause-cycled. F.1 status change requires Layer 3 reviewer-pause + Layer 3 status upgrade Patches.

(iii) **"Target 7 retroactively closed at Patch 0544 §6" framing (§8).** This recognition is supported by Theorem 6.1's three-criteria match per §8.1; Thomas may want to gate-check this recognition (e.g., via reviewer-pause cycle confirmation) before accepting it as final. Stated here as the recognition + supporting evidence; final ratification belongs to the reviewer-pause cycle at Patch 0547+.

### §11.2 Programme state after this Layer 3 promotion

**What changed at programme level:**
- B.1.q2 promoted from sketch Layer 2 closure (Patch 0535 §11) to sketch-document Layer 3 closure.
- Patch 0535 §11.12(i) trapezoidal-discretization caveat substantively removed at sketch-document Layer 3.
- Patch 0535 §11.12(iii) Layer 3 promotion deferral substantively addressed.
- Sixth Layer 3 promotion in F.1 trajectory.
- Retroactive recognition that Target 7 (B.1.q3 PT propagation Layer 3) was closed at Patch 0544 §6 Theorem 6.1.
- **Layer 3 promotion arc effectively COMPLETE** — all seven Patch 0540 targets closed at sketch-document Layer 3.

**What did NOT change:**
- F.1 sub-question status UNCHANGED at Patch 0539 framing.
- No new Findings registered.
- No sub-question reopenings.
- No v1.0 SHIPPED edits.
- No Patches 0531-0545 immutable content modifications.
- No reviewer-pause checkpoint modifications.
- No flagship paper assembly trigger.
- No F.2/F.3 substantive content trajectory opening.
- No long-term programme target work.

### §11.3 Closing summary

Patch 0546 closes B.1.q2 at sketch-document Layer 3 by deriving the Full 4D Curl Vanishing Theorem (Theorem 4.1.1) via explicit Schur-decomposition of $\Lambda^2(\mathbb{R}^4)|_{v_*}$ under residual $I_h$ symmetry: $\Lambda^2(\mathbb{R}^4)|_{v_*} = T_{1u} \oplus T_{1g}$, neither containing the trivial $A_g$ irrep, hence any $I_h$-invariant 4D 2-form at $v_*$ must vanish. The proof is **discretization-independent**, removing the Patch 0535 §11.12(i) self-checkpoint trapezoidal-discretization caveat. Patch 0535 §11.12(iii) Layer 3 deferral substantively addressed.

§8 retroactively recognizes that Target 7 (B.1.q3 perturbation-theory propagation Layer 3) was substantively closed at Patch 0544 §6 Theorem 6.1 — the Perturbative-Locality Propagation Rule. With this recognition, all seven Patch 0540 Layer 3 promotion targets are closed at sketch-document Layer 3; the Layer 3 promotion arc launched at Patch 0540 is effectively complete.

The Layer-3-arc-complete state does NOT propagate to F.1 sub-question status change or flagship paper assembly — those gates require Layer 3 reviewer-pause cycle + Layer 3 status upgrade Patches per §17 codified discipline. The next gate is **Patch 0547 = Layer 3 reviewer-pause cycle Patch** per Patch 0540 §5.1 codified workflow.

F.1 sub-question status UNCHANGED. Findings registry UNCHANGED. v1.0 SHIPPED edits NONE. Patches 0531-0545 immutable content UNCHANGED. Reviewer-pause checkpoint UNCHANGED. Flagship paper assembly NOT triggered. F.2/F.3 trajectories NOT opened. Long-term programme target REGISTERED + DEFERRED.
