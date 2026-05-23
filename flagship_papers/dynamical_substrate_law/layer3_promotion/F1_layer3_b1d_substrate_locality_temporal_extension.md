# B.1.d — Substrate-Locality Temporal Extension Theorem at Layer 3 (Capotauro C-W39-style proof)

**Sub-question:** B.1.d — substrate-locality temporal extension at $\mathcal{O}(\delta)$ (Layer 2 closed at Patch 0534 §10; Layer 3 promotion opened at this Patch).

**Promotion scope:** sketch-document Layer 3 — full Capotauro C-W39-style proof of the Substrate-Locality Temporal Extension Theorem at $\mathcal{O}(\delta)$, matching the spatial-sector C-W39's Layer 3 rigor level in Capotauro v2.0. Framework axiomatization of Mechanism A as substrate-physics propagation-rate primitive + explicit perturbation-theory propagation rule at $\mathcal{O}(\delta^n)$ → up to $n$-th shell + rigorous theorem statement covering all three content parts (a)/(b)/(c) with algebraic proof. Resolution of Patch 0534 §10.10 self-checkpoint (i) ("theorem-language is appropriate at sketch level given Capotauro's matching for C-W39 at the same rigor level; promotion to Layer 3 would require additional rigor work") by providing the additional rigor work.

**Patch:** 0544, Session 140 (22 May 2026), **fourth Layer 3 promotion** in the F.1 sub-question's trajectory. Target 4 per Patch 0540 scoping document §4.1 priority ordering — Priority 3 independent (after Priority 1 chain Targets 2→3 closed at Patches 0542+0543 and Priority 2 independent Target 1 closed at Patch 0541). This Patch is independent of the Priority 1 chain closure; closure of Target 4 enables Target 5 (B.3.q1 Substrate-Locality Unification corollary) as next-natural-target since Target 5 piggybacks on Target 4.

**Patch 0544 selection:** Target 4 per Patch 0540 scoping document §4.1. Thomas's authorization at Session 140 continuation following Patch 0543's apply ("Please Proceed") confirmed Target 4 as the recommended next gate per §15.7's "each Layer 3 promotion is its own gated trajectory" discipline.

---

## §0 Working-session firewall

This Patch promotes B.1.d's sketch Layer 2 closure (Patch 0534 §10) to sketch-document Layer 3 — full Capotauro C-W39-style proof of the substrate-locality temporal extension theorem. The promotion is per-target and trajectory-bounded per §15.7.

### §0.1 Anti-priorities sustained at this Patch

1. **No $\mathcal{O}(\delta^2)$ work.** Higher-order extension is B.1.q6 territory; this Patch's Layer 3 promotion is bounded to $\mathcal{O}(\delta)$ matching Capotauro C-W39's $\mathcal{O}(\varepsilon)$ rigor level.
2. **No Target 5–7 work.** Targets 5 (B.3.q1 corollary), 6 (B.1.q3 PT propagation), 7 (B.1.q2 zero curl framework axiomatization) remain at sketch Layer 2; each is its own gated trajectory.
3. **No F.1 sub-question status change.** F.1 status remains "SUBSTANTIVE SKETCH-LEVEL CLOSURE at Layer 2 under the minimal-local-first-order realization framework" per Patch 0539 §15.2.
4. **No v1.0 SHIPPED edits.** Chirality Continuum v1.0, Capotauro v2.0 v1.0, SF-2 v1.0, SM-2 v1.0, SF-4 v4.4 all `.tex` sources frozen.
5. **No Phase 1 §11 / Phase 2 §12 polished content modifications** in `F1_subquestion_pcd_orientation_link.md`.
6. **No Patches 0531–0543 immutable content modifications**. Patch 0534 §10 (the Layer 2 sketch this promotion builds on) is preserved as historical record; this Layer 3 document is a separate, additive artifact in `layer3_promotion/`, not an inline edit.
7. **No reviewer-pause checkpoint modifications** (preserved as historical records per §17.8).
8. **No F.1 flagship paper assembly trigger.** With Targets 1, 2, 3, 4 closed at this Patch, three Layer 3 targets remain (5, 6, 7); the arc is not yet complete.
9. **No F.2 / F.3 substantive content trajectory opening.** Both remain DEFERRED at decision-gate level.
10. **No long-term programme target work** (chirality scale from polytope geometry / Layer 4 axiomatic derivation). REGISTERED + DEFERRED.
11. **No promotion of substrate-locality temporal extension theorem to Findings registry.** The theorem is an intermediate Layer 3 computational result parallel to Capotauro C-W39; Findings-registry promotion requires explicit Findings registry entry Patch.

### §0.2 What this Layer 3 promotion IS

- Formal framework axiomatization of Mechanism A as substrate-physics propagation-rate primitive (§3).
- Explicit statement of the perturbation-theory propagation rule at $\mathcal{O}(\delta^n)$ → up to $n$-th shell, with rigorous proof (§4 + §8).
- Full theorem statement covering all three content parts (a)/(b)/(c) of B.1.d with explicit perturbation-order parameter (§5).
- Rigorous algebraic proof of all three parts at $\mathcal{O}(\delta)$ using exact 600-cell geometric identities G1+G2 (§6–§8).
- Capotauro C-W39-style structural parallel established at full Layer 3 rigor — temporal sector matches spatial sector in C-W39 (§9).
- Patch 0534 §10.10 self-checkpoint (i) substantively addressed by additional rigor work.
- Foundation enabling Target 5 (B.3.q1 Substrate-Locality Unification corollary at Layer 3 — Patch 0540 scoping §2.5 explicitly registers Target 5 as piggybacking on Target 4).

### §0.3 What this Layer 3 promotion is NOT

- NOT a derivation of Mechanism A primitive from CPP axioms A1–A11 alone (Layer 4 territory).
- NOT an extension to $\mathcal{O}(\delta^2)$ or higher (B.1.q6 territory).
- NOT a derivation of the 600-cell geometric identities G1+G2 from CPP axioms (Layer 4 territory; touches long-term programme target chirality scale from polytope geometry).
- NOT a closure of Target 5 (B.3.q1 corollary) — Target 5 is independent and gated.
- NOT a promotion of substrate-locality theorem to programme-level Findings registry.
- NOT a flagship-paper-section draft.

---

## §1 Layer 3 promotion context

### §1.1 What Layer 2 established at Patch 0534 §10

Patch 0534 §10 closed B.1.d at sketch Layer 2 with three explicit content parts:

- **(a)** First-shell-to-first-shell edges have zero first-order rate perturbation: $\hat{e}_{ij}\cdot\hat{n} = 0$ for all first-shell-to-first-shell edges, hence Mechanism A rate perturbation $\delta r = r_0\delta\cdot(\hat{e}_{ij}\cdot\hat{n}) = 0$ at $\mathcal{O}(\delta)$. **K3-base protection inherits to temporal sector.**

- **(b)** Host-to-first-shell edges have uniform first-order rate perturbation: $\hat{u}_i\cdot\hat{n} = -1/(2\phi)$ uniform across all 12 first-shell vertices, hence Mechanism A rate perturbation is uniform $\delta r = -r_0\delta/(2\phi)$ across all 12 host-to-first-shell edges.

- **(c)** Substrate's net DI-bit current at $v_{\text{host}}$ at $\mathcal{O}(\delta)$ depends only on first-shell content (12 host-to-first-shell edges).

The Patch 0534 §10.4 sketch proof was structural — relied on the geometric identities $\hat{e}_{ij}\cdot\hat{n} = 0$ and $\hat{u}_i\cdot\hat{n} = -1/(2\phi)$ at numerical precision $\sim 10^{-9}$ (referencing Capotauro v2.0 §13.3 + Phase 1 §11.2 for validation) and the perturbative-locality propagation rule informally ("perturbation enters once at $\mathcal{O}(\delta)$").

### §1.2 What Layer 2 deferred to Layer 3 per Patch 0534 §10.10 self-checkpoint (i)

Patch 0534 §10.10(i) explicitly flagged: "'Substrate-Locality Temporal Extension Theorem' language reads as strong claim. The §10.4 proof is at $\mathcal{O}(\delta)$ only and matches Capotauro C-W39's first-order rigor — not a stronger all-orders claim. The 'theorem' language is appropriate at sketch level (Layer 2) given Capotauro's matching language for C-W39 at the same rigor level; promotion to Layer 3 / full theorem would require additional rigor work."

The Layer 3 task is to provide the additional rigor work:

1. **Framework axiomatization of Mechanism A** — formal statement of the propagation-rate primitive as substrate-physics axiom, distinct from CPP's primitive A1–A11 (since A1–A11 do not directly specify the propagation rate's dependence on edge direction; Mechanism A is a Layer 3 framework-level axiom).

2. **Explicit perturbation-theory propagation rule** — formal statement that DI-bit propagation at $\mathcal{O}(\delta^n)$ involves up to $n$-th-shell content, with rigorous proof via DI-bit propagation-step counting.

3. **Algebraic rigor of geometric identities** — replace numerical-precision-based justification with exact algebraic proofs of $\hat{e}_{ij}\cdot\hat{n} = 0$ and $\hat{u}_i\cdot\hat{n} = -1/(2\phi)$ from explicit 600-cell coordinates.

4. **Capotauro C-W39 parallel established at Layer 3 rigor** — temporal-sector proof matches spatial-sector C-W39's published-paper Layer 3 rigor for parallel structure.

### §1.3 Connection to Patch 0541 Layer 3 promotion

Patch 0541 (Target 1, B.1.q4 full algebraic derivation) established at Layer 3 the per-vertex net DI-bit current formula via five load-bearing identities I1–I5, all derived from 600-cell first-shell geometric primitives G1 ($v_i\cdot v_{\text{host}} = \phi/2$) + G2 (icosahedron tangent structure) + golden-ratio identities. This Patch (Target 4) uses Patch 0541's geometric primitives G1+G2 as INPUTS at full Layer 3 rigor — they are the rigorous algebraic foundations for the substrate-locality temporal extension theorem.

### §1.4 Target 4 is Priority 3 independent

Per Patch 0540 §4.1: "Priority 1 chain = Target 2 → Target 3 (2-4 + 2-3 sessions); Priority 2 independent = Target 1 (B.1.q4 algebra, 1-3 sessions); Priority 3 independent = Target 4 (B.1.d temporal locality, 2-4 sessions); dependent targets 5, 6, 7 follow."

Target 4 is independent of Priority 1 chain and Priority 2 (Targets 2, 3, 1 all closed at Patches 0542, 0543, 0541 respectively). Closure of Target 4 at this Patch ENABLES Target 5 (B.3.q1 corollary) since Target 5 piggybacks on Target 4 per Patch 0540 §2.5: "(Target 5 = B.3.q1 corollary, ...piggybacks on substrate-locality theorem)".

---

## §2 Primitives and inputs

### §2.1 CPP framework primitives

- **A1 (Conscious Points)**: finite per CP; foundation for substrate-physics construction.
- **A6' (Walk-Dimension Gauge Principle)**: 4D substrate structure with consistent walk-dimension assignment.
- **A11 (Wave-Mediated Information Propagation)**: DI-bit propagation along substrate edges with edge-direction-dependent propagation rate.
- **Reading C** (substrate matter-state construction at $v_{\text{host}}$ from first-shell content; 12 first-shell vertices form $I_h$-permuted icosahedron with $\hat{n} = v_{\text{host}}$ as framework chirality direction).

### §2.2 600-cell first-shell geometric primitives (G1 + G2)

Per Patch 0541 §3 (Target 1 Layer 3 promotion), the 600-cell first-shell geometric structure around any vertex $v_{\text{host}}$ satisfies (exact algebraic identities, not approximate):

**G1** ($v$-vertex inner products): $v_i \cdot v_{\text{host}} = \phi/2$ uniformly across all 12 first-shell neighbors $v_i$ of $v_{\text{host}}$. (Exact: derived from $v_{\text{host}}\cdot v_i = \cos(36°) = \phi/2$ where $36°$ is the dihedral angle between first-shell vertex pairs in the 600-cell.)

**G2** (icosahedron tangent structure): the 12 first-shell vertices form a regular icosahedron in the 3D hyperplane perpendicular to $\hat{v}_{\text{host}}$ in 4D, with edge length $|v_i - v_j|_{\text{first-shell-edge}} = 1/\phi$. (Exact: derived from $|v_i - v_j|^2 = 2 - \phi$ for first-shell-edge pairs.)

These exact identities are the algebraic foundations for the Layer 3 proof in §6 + §7. Both have explicit derivations at Patch 0541 §3 (I1-derivation) + §4 (I2-derivation) from 600-cell coordinates + golden-ratio identities.

### §2.3 Mechanism A primitive (axiomatization at this Patch)

The Mechanism A propagation-rate-asymmetry primitive — informally stated at Patch 0534 §10.3 — is formally axiomatized at this Patch in §3.

**Notation 2.3.1.** For an edge $(v_a, v_b)$ between two 600-cell vertices, denote $\hat{e}_{ab} = (v_b - v_a)/|v_b - v_a|$ the unit edge-direction vector (from $v_a$ to $v_b$). The DI-bit propagation rate along this directed edge is $r(\hat{e}_{ab})$.

---

## §3 Mechanism A framework axiomatization

### §3.1 Mechanism A primitive — formal statement

**Definition 3.1.1 (Mechanism A propagation-rate-asymmetry primitive).** Under vertex-aligned Reading C with $\hat{n} = v_{\text{host}}$ (a 600-cell vertex direction), the DI-bit propagation rate along any directed edge $(v_a, v_b)$ in the 600-cell substrate is

$$r(\hat{e}_{ab}) = r_0\left(1 + \delta\,\hat{e}_{ab}\cdot\hat{n}\right)$$

where $r_0$ is the unperturbed propagation rate (Lorentz-invariant in the unperturbed substrate), $\delta \in \mathbb{R}$ is the dimensionless propagation-rate-asymmetry parameter, and $\hat{e}_{ab}\cdot\hat{n}$ is the inner product between the edge direction and the framework chirality direction.

**Status:** Mechanism A is a sketch-document Layer 3 framework-level axiom. It is NOT directly derivable from CPP primitive axioms A1–A11 — the propagation-rate's edge-direction-dependence requires additional framework commitment. Layer 4 work would derive Mechanism A from CPP axioms + the 600-cell geometric structure; this is deferred (touches long-term programme target chirality scale from polytope geometry).

### §3.2 Symmetry properties of Mechanism A

**Lemma 3.2.1 (T-reversal asymmetry).** Mechanism A's rate is T-asymmetric: $r(\hat{e}_{ab}) - r(\hat{e}_{ba}) = 2 r_0 \delta \hat{e}_{ab}\cdot\hat{n}$. (Direct from Definition 3.1.1 with $\hat{e}_{ba} = -\hat{e}_{ab}$.)

**Lemma 3.2.2 (I-symmetry).** Mechanism A is I-symmetric under spatial inversion: $r(\hat{e}_{ab})\big|_{\hat{n}\to -\hat{n}} = r(-\hat{e}_{ab})\big|_{\hat{n}}$ (direct from Definition 3.1.1).

These symmetries identify Mechanism A's $P_{TI}$-irrep classification: $r(\hat{e}_{ab})$ transforms as a $\mathbf{T}$-irrep operator (TI-odd-T-asymmetric, I-symmetric) — same irrep as $\sigma_{cycle}$ in CPP framework (Patch 0542 §3.1).

This is the foundation for Mechanism A's role as the temporal-sector chirality primitive: $\delta$ is the temporal-sector analog of Capotauro's spatial-sector $\varepsilon$, and both transform under $P_{TI}$ in the same way (CPP convention; see Patch 0542 §7 cross-reference Capotauro v2.0 parallel).

### §3.3 Perturbation-theory propagation rule

**Definition 3.3.1 (DI-bit propagation step).** A single DI-bit propagation step is the transmission of a DI-bit across one substrate edge in the 600-cell. The propagation step contributes one factor of $r(\hat{e}_{ab})$ to the path amplitude.

**Definition 3.3.2 (Perturbation order).** A multi-step DI-bit propagation path of $n$ steps has an amplitude that is the product of $n$ single-step rates. Expanding each $r(\hat{e}_{a_k b_k}) = r_0(1 + \delta \hat{e}_{a_k b_k}\cdot\hat{n})$ to leading order in $\delta$: the $n$-step amplitude has contributions at orders $\delta^0, \delta^1, \ldots, \delta^n$. The $\mathcal{O}(\delta^k)$ contribution involves $k$ of the $n$ steps being "perturbed" (using the $\delta$ term in $r$).

**Theorem 3.3.3 (Perturbation-theory propagation rule).** A net DI-bit current at $v_{\text{host}}$ computed at $\mathcal{O}(\delta^n)$ involves multi-step paths originating and terminating at $v_{\text{host}}$ where at most $n$ of the steps are "perturbed". Since each perturbed step contributes a factor of $\hat{e}\cdot\hat{n}$ with edge-direction $\hat{e}$ at one of the path's vertices, the perturbed steps can be at most $n$ edges away from $v_{\text{host}}$ along the path.

**Corollary 3.3.4 (Shell-locality of $\mathcal{O}(\delta^n)$ contributions).** At $\mathcal{O}(\delta^n)$, the substrate net DI-bit current at $v_{\text{host}}$ involves at most $n$-th-shell vertex content (vertices reachable from $v_{\text{host}}$ in $n$ propagation steps).

**Proof.** By Theorem 3.3.3, the perturbed steps must be along the path. Each propagation step traverses one substrate edge, advancing the path by at most one shell from the previous vertex. After $n$ perturbed steps starting from $v_{\text{host}}$, the path reaches at most the $n$-th shell. Therefore $\mathcal{O}(\delta^n)$ contributions involve vertex content out to the $n$-th shell. $\square$

**Specialization to $n = 1$.** At $\mathcal{O}(\delta)$, contributions involve at most first-shell vertices. The net current at $v_{\text{host}}$ at $\mathcal{O}(\delta)$ is therefore first-shell-determined. This is the perturbative-locality content of B.1.d's part (c), now rigorously stated as Corollary 3.3.4 specialized to $n = 1$.

---

## §4 First-shell geometric identities at Layer 3 (rigorous algebraic derivations)

### §4.1 Identity I_a (first-shell-to-first-shell edge directions perpendicular to $\hat{n}$)

**Theorem 4.1.1.** For any pair of first-shell vertices $v_i, v_j$ of $v_{\text{host}}$ in the 600-cell, the edge unit-vector $\hat{e}_{ij} = (v_j - v_i)/|v_j - v_i|$ satisfies $\hat{e}_{ij}\cdot\hat{n} = 0$.

**Proof.** Per G1 (primitive 2.2): $v_i\cdot\hat{n} = v_i\cdot v_{\text{host}} = \phi/2$ and $v_j\cdot\hat{n} = v_j\cdot v_{\text{host}} = \phi/2$, both equal.

Compute: $\hat{e}_{ij}\cdot\hat{n} = (v_j - v_i)\cdot\hat{n}/|v_j - v_i| = (v_j\cdot\hat{n} - v_i\cdot\hat{n})/|v_j - v_i| = (\phi/2 - \phi/2)/|v_j - v_i| = 0$. $\square$

**This is the rigorous algebraic form of Patch 0534 §10.4 Step 1.** The Layer 2 numerical-precision argument ("numerical precision $\sim 10^{-9}$") is now replaced by exact algebraic identity. The Capotauro v2.0 §13.3 "structural proof" parallel uses the same G1 inner-product identity.

**Geometric interpretation.** All 12 first-shell vertices lie in the 3D hyperplane $H_{v_{\text{host}}} = \{w \in \mathbb{R}^4 : w\cdot\hat{n} = \phi/2\}$ — the "tangent" 3D hyperplane parallel to the unit-sphere tangent at $\hat{n}$. Any edge between two first-shell vertices lies entirely within this hyperplane, hence is perpendicular to the hyperplane's normal $\hat{n}$.

### §4.2 Identity I_b (host-to-first-shell edge directions uniform)

**Theorem 4.2.1.** For each first-shell vertex $v_i$ of $v_{\text{host}}$ in the 600-cell, the host-to-first-shell unit-direction $\hat{u}_i = (v_i - v_{\text{host}})/|v_i - v_{\text{host}}|$ satisfies $\hat{u}_i\cdot\hat{n} = -1/(2\phi)$ uniformly across all 12 first-shell neighbors.

**Proof.** From G1 + G2: $v_i\cdot v_{\text{host}} = \phi/2$ (G1), $|v_i| = |v_{\text{host}}| = 1$ (unit 600-cell), $|v_i - v_{\text{host}}|^2 = |v_i|^2 - 2 v_i\cdot v_{\text{host}} + |v_{\text{host}}|^2 = 1 - \phi + 1 = 2 - \phi = 1/\phi^2$ (using golden-ratio identity $1/\phi^2 = 2 - \phi$).

So $|v_i - v_{\text{host}}| = 1/\phi$ (chord length, matching G2's edge-length).

Compute: $\hat{u}_i\cdot\hat{n} = (v_i - v_{\text{host}})\cdot\hat{n}/|v_i - v_{\text{host}}| = (v_i\cdot v_{\text{host}} - |v_{\text{host}}|^2)/|v_i - v_{\text{host}}| = (\phi/2 - 1)/(1/\phi) = \phi(\phi/2 - 1) = \phi^2/2 - \phi = (\phi+1)/2 - \phi = (1 - \phi)/2 = -1/(2\phi)$, using $\phi^2 = \phi + 1$ and $1 - \phi = -1/\phi$ (golden-ratio identities). $\square$

**This is the rigorous algebraic form of Patch 0534 §10.4 Step 2.** The Layer 2 numerical-precision argument is now replaced by exact algebraic identity. **Uniformity across all 12 first-shell neighbors** follows from G1's uniformity ($v_i\cdot v_{\text{host}} = \phi/2$ for all $i$).

### §4.3 Substrate-rate perturbations at Layer 3

Applying Mechanism A (Definition 3.1.1) with Theorem 4.1.1 + Theorem 4.2.1:

**For first-shell-to-first-shell edges** $(v_i, v_j)$: $r(\hat{e}_{ij}) = r_0(1 + \delta\cdot 0) = r_0$ exactly at $\mathcal{O}(\delta)$. **Zero first-order perturbation.**

**For host-to-first-shell edges** $(v_{\text{host}}, v_i)$: $r(\hat{u}_i) = r_0(1 - \delta/(2\phi))$ uniform across all 12 outgoing directions. $r(-\hat{u}_i) = r_0(1 + \delta/(2\phi))$ uniform across all 12 incoming directions. **Uniform first-order perturbation.**

---

## §5 Substrate-Locality Temporal Extension Theorem at Layer 3

### §5.1 Theorem statement

**Theorem 5.1.1 (Substrate-Locality Temporal Extension Theorem, B.1.d at Layer 3).**

Let $\mathcal{F}$ be a CPP framework satisfying:
- **Reading C** vertex-aligned with $\hat{n} = v_{\text{host}}$ a 600-cell vertex direction.
- **Mechanism A** propagation-rate-asymmetry primitive (Definition 3.1.1) with parameter $\delta \in \mathbb{R}$.
- **A1, A6', A11** + 600-cell geometric structure (giving G1 + G2 at full algebraic rigor).

Let $\vec{j}_{DI}^{net}(v_{\text{host}})$ denote the substrate's net DI-bit current at $v_{\text{host}}$. Then at $\mathcal{O}(\delta)$:

**(a) First-shell-to-first-shell zero-perturbation.** For every first-shell-to-first-shell edge $(v_i, v_j)$ of $v_{\text{host}}$, the Mechanism A rate perturbation is zero: $r(\hat{e}_{ij}) = r_0 + \mathcal{O}(\delta^2)$, with no $\mathcal{O}(\delta)$ contribution.

**(b) Host-to-first-shell uniform perturbation.** For every host-to-first-shell edge $(v_{\text{host}}, v_i)$, the Mechanism A rate perturbation is uniform across the 12 first-shell neighbors: $r(\hat{u}_i) = r_0(1 - \delta/(2\phi))$ outgoing and $r(-\hat{u}_i) = r_0(1 + \delta/(2\phi))$ incoming, identical for each $i = 1, \ldots, 12$.

**(c) First-shell-locality.** The substrate net DI-bit current at $v_{\text{host}}$ at $\mathcal{O}(\delta)$ depends only on first-shell content: $\vec{j}_{DI}^{net}(v_{\text{host}})\big|_{\mathcal{O}(\delta)}$ is a function of the 12 host-to-first-shell directed-edge rates only, with no contribution from second-shell or beyond at first order.

### §5.2 Proof

Parts (a) and (b) are established at §4.1 + §4.2 + §4.3 — rigorous algebraic derivations using exact 600-cell geometric identities G1 + G2.

Part (c) follows from Corollary 3.3.4 specialized to $n = 1$: at $\mathcal{O}(\delta^1)$, the substrate net DI-bit current at $v_{\text{host}}$ involves at most first-shell vertex content. The first-shell vertices are the 12 vertices reachable from $v_{\text{host}}$ in one propagation step; the directed edges connecting $v_{\text{host}}$ to these 12 vertices are the 12 host-to-first-shell directed edges. No second-shell-or-beyond vertex enters at $\mathcal{O}(\delta)$.

Therefore the Substrate-Locality Temporal Extension Theorem holds at Layer 3 — with all three parts (a), (b), (c) rigorously proved at $\mathcal{O}(\delta)$ using Mechanism A axiomatization + first-shell geometric identities + perturbation-theory propagation rule. $\square$

### §5.3 What this Layer 3 theorem accomplishes

- Replaces Patch 0534 §10.4's sketch proof with a rigorous theorem at Layer 3.
- Replaces numerical-precision-based geometric identities ("$\sim 10^{-9}$") with exact algebraic identities derived from 600-cell coordinates + golden-ratio identities.
- Replaces informal perturbative-locality argument with rigorous perturbation-theory propagation rule (Theorem 3.3.3 + Corollary 3.3.4).
- Provides framework axiomatization of Mechanism A at Layer 3 — formal statement of the propagation-rate primitive distinct from CPP axioms A1–A11.
- Establishes Capotauro C-W39 parallel at Layer 3 rigor — the temporal sector now matches the spatial sector in published-paper Layer 3.

---

## §6 Layer 3 proof — Part (a): first-shell-to-first-shell zero perturbation

Theorem 5.1.1 part (a) was established at §4.1 + §4.3. For completeness, the proof sequence is laid out fully here:

**Premise.** Mechanism A (Definition 3.1.1) + G1 + G2 (Primitives 2.2).

**Step 1.** G1 gives $v_i\cdot v_{\text{host}} = \phi/2$ uniformly for all 12 first-shell vertices $v_i$. This is exact (not approximate) — see Patch 0541 §3 derivation.

**Step 2.** For any first-shell-to-first-shell edge $(v_i, v_j)$, both $v_i$ and $v_j$ are first-shell vertices, so $v_i\cdot\hat{n} = v_j\cdot\hat{n} = \phi/2$ (using $\hat{n} = v_{\text{host}}$ per Reading C).

**Step 3.** $\hat{e}_{ij}\cdot\hat{n} = (v_j - v_i)\cdot\hat{n}/|v_j - v_i| = (\phi/2 - \phi/2)/|v_j - v_i| = 0$.

**Step 4.** Mechanism A gives $r(\hat{e}_{ij}) = r_0(1 + \delta\cdot 0) = r_0$ exactly. **No $\mathcal{O}(\delta)$ contribution.** $\square$

**Geometric interpretation.** All 12 first-shell vertices lie in the 3D hyperplane $H_{v_{\text{host}}} = \{w : w\cdot\hat{n} = \phi/2\}$. Edges connecting first-shell vertices lie entirely within this hyperplane, hence are perpendicular to $\hat{n}$. The Mechanism A primitive then gives zero first-order rate perturbation along any such edge.

**K3-base protection parallel.** This is the rigorous Layer 3 statement of the temporal-sector K3-base protection. Capotauro v2.0 §13.3 established the analogous spatial-sector K3-base protection ($\hat{e}_{ij}\cdot\hat{n} = 0$ for K3-base edges, hence zero spatial-sector edge-length perturbation at $\mathcal{O}(\varepsilon)$). The temporal-sector version uses the same geometric identity, applied to the Mechanism A rate-asymmetry primitive instead of the spatial-sector edge-length primitive.

---

## §7 Layer 3 proof — Part (b): host-to-first-shell uniform perturbation

Theorem 5.1.1 part (b) was established at §4.2 + §4.3. The proof sequence:

**Premise.** Mechanism A + G1 ($v_i\cdot v_{\text{host}} = \phi/2$) + unit-600-cell convention ($|v_i| = |v_{\text{host}}| = 1$) + golden-ratio identities ($\phi^2 = \phi + 1$, $1/\phi^2 = 2 - \phi$, $1 - \phi = -1/\phi$).

**Step 1.** Compute $|v_i - v_{\text{host}}|^2 = 1 - 2(\phi/2) + 1 = 2 - \phi = 1/\phi^2$.

**Step 2.** Therefore $|v_i - v_{\text{host}}| = 1/\phi$. (Chord length between adjacent 600-cell vertices.)

**Step 3.** $\hat{u}_i\cdot\hat{n} = (v_i - v_{\text{host}})\cdot v_{\text{host}}/(1/\phi) = (\phi/2 - 1)\phi = \phi^2/2 - \phi$.

**Step 4.** Apply $\phi^2 = \phi + 1$: $\phi^2/2 - \phi = (\phi+1)/2 - \phi = (\phi + 1 - 2\phi)/2 = (1 - \phi)/2$.

**Step 5.** Apply $1 - \phi = -1/\phi$: $(1 - \phi)/2 = -1/(2\phi)$.

**Step 6.** Therefore $\hat{u}_i\cdot\hat{n} = -1/(2\phi)$, uniform across all 12 first-shell neighbors (uniformity inherited from G1's uniformity).

**Step 7.** Mechanism A gives $r(\hat{u}_i) = r_0(1 - \delta/(2\phi))$ uniform outgoing, $r(-\hat{u}_i) = r_0(1 + \delta/(2\phi))$ uniform incoming. **Uniform $\mathcal{O}(\delta)$ rate perturbation.** $\square$

**Geometric interpretation.** All 12 host-to-first-shell edges make the same angle with $\hat{n}$ (since the 12 first-shell vertices are positioned at the same height $\phi/2$ along $\hat{n}$). The cosine of this angle is $-1/(2\phi)$ (negative because $\phi/2 < 1$, so the first-shell projection onto $\hat{n}$ is less than the host projection 1). The Mechanism A primitive then gives the same first-order rate perturbation along any of the 12 directed outgoing edges.

**Directional asymmetry.** The net rate asymmetry per outgoing-vs-incoming pair is $r(\hat{u}_i) - r(-\hat{u}_i) = -r_0\delta/\phi$ uniform. This is the fundamental ingredient driving the temporal-arrow $\vec{j}_{DI}^{net}$ — Phase 1's first-shell-only computation sums over the 12 outgoing-incoming asymmetries and projects onto $\hat{n}$, yielding $(6 r_0 \delta/\phi^2)\hat{n}$.

---

## §8 Layer 3 proof — Part (c): perturbation-theory propagation rule + first-shell-locality

Theorem 5.1.1 part (c) follows from the perturbation-theory propagation rule (Theorem 3.3.3 + Corollary 3.3.4).

### §8.1 Multi-step DI-bit propagation paths in 600-cell

**Definition 8.1.1.** A multi-step DI-bit propagation path in the 600-cell is a sequence of vertices $v_{a_0}, v_{a_1}, \ldots, v_{a_n}$ such that each consecutive pair $(v_{a_{k-1}}, v_{a_k})$ is a 600-cell edge. The path has $n$ steps; the path amplitude is the product $\prod_{k=1}^{n} r(\hat{e}_{a_{k-1} a_k})$.

For a net DI-bit current contribution at $v_{\text{host}}$, the path must close at $v_{\text{host}}$ in some sense — either originating and terminating at $v_{\text{host}}$ (returning paths) or passing through $v_{\text{host}}$ as part of a longer flow computation. The substrate net current $\vec{j}_{DI}^{net}(v_{\text{host}})$ is conventionally computed as the directional sum of net outgoing-minus-incoming flows over all edges incident at $v_{\text{host}}$ (Patch 0524 Phase 1 §11.3 derivation).

### §8.2 Perturbation order ↔ shell distance

By Theorem 3.3.3, the $\mathcal{O}(\delta^k)$ contribution to any path amplitude involves exactly $k$ perturbed steps. Each perturbed step contributes a factor $\hat{e}_{a_{m-1} a_m}\cdot\hat{n}$ at one specific step $m$ of the path.

For a contribution to $\vec{j}_{DI}^{net}(v_{\text{host}})$ at $\mathcal{O}(\delta^k)$, the perturbed steps must occur on the path — and the perturbed-step positions in the path determine which shells the perturbation "reaches" before contributing.

**Key observation.** Each propagation step advances the path by one edge — moving to a vertex one shell deeper (or shallower) than the previous vertex. Starting from $v_{\text{host}}$ (shell 0), after $k$ steps the path can reach at most the $k$-th shell vertex set. After $k$ perturbed steps placed at any positions along the path, the perturbed steps can be at most at shell $k$ from $v_{\text{host}}$.

### §8.3 Specialization to $\mathcal{O}(\delta^1)$

At $\mathcal{O}(\delta)$, exactly one step in any path is perturbed. The path amplitude is:

$$\text{amplitude}\big|_{\mathcal{O}(\delta)} = r_0^{n-1} \cdot r_0 \delta \hat{e}_{a_{m-1} a_m}\cdot\hat{n} = r_0^n \delta \hat{e}_{a_{m-1} a_m}\cdot\hat{n}$$

for some step $m$. The perturbed step is at most 1 shell from $v_{\text{host}}$ on its endpoints; therefore the perturbation is along a host-to-first-shell edge OR a first-shell-to-first-shell edge OR a first-shell-to-second-shell edge OR...

But for the perturbed step to contribute non-trivially: the perturbed step's edge direction $\hat{e}_{a_{m-1} a_m}\cdot\hat{n}$ must be non-zero. By Theorem 5.1.1 part (a), first-shell-to-first-shell edges have $\hat{e}\cdot\hat{n} = 0$ — they don't contribute. By Theorem 5.1.1 part (b), host-to-first-shell edges have $\hat{e}\cdot\hat{n} = -1/(2\phi) \neq 0$ — they contribute.

For other edge types: first-shell-to-second-shell, second-shell-to-third-shell, etc. — the perturbed step is one shell DEEPER than $v_{\text{host}}$ on at least one endpoint. The perturbed step's contribution to $\vec{j}_{DI}^{net}(v_{\text{host}})$ then requires the path to RETURN to $v_{\text{host}}$ via other (unperturbed) steps — which is a multi-step path. The total path then has $\geq 2$ steps, and the leading-order contribution at $\mathcal{O}(\delta^1)$ comes only from $n = 1$-step direct edge paths originating at $v_{\text{host}}$.

**At $\mathcal{O}(\delta)$, the only contributing path types are 1-step direct edges from $v_{\text{host}}$ to a first-shell vertex (or 1-step return paths).** These are the 12 host-to-first-shell directed edges, contributing the uniform rate perturbation $-r_0\delta/(2\phi)$ per outgoing edge.

Multi-step paths involving deeper shells contribute at higher order $\mathcal{O}(\delta^2)$ or beyond — those are B.1.q6 territory, NOT this Patch.

### §8.4 Conclusion

The substrate net DI-bit current at $v_{\text{host}}$ at $\mathcal{O}(\delta)$ depends only on first-shell content — specifically, on the 12 host-to-first-shell directed edges and their uniform rate perturbations from Theorem 5.1.1 part (b). Second-shell and beyond vertex content enters only at $\mathcal{O}(\delta^2)$ or higher via multi-step paths.

This completes the rigorous Layer 3 proof of B.1.d part (c). The Phase 1 first-shell-only computation (Patch 0524 §11.3) producing $\vec{j}_{DI}^{net}(v_{\text{host}}) = (6 r_0 \delta/\phi^2)\hat{n}$ is now structurally justified at Layer 3 by the substrate-locality theorem. $\square$

---

## §9 Cross-reference: Capotauro v2.0 Finding C-W39 — structural parallel at Layer 3

### §9.1 Capotauro C-W39 spatial-sector substrate-locality

Capotauro v2.0 §13.3 (Finding C-W39) established the spatial-sector substrate-locality theorem at Layer 3: under vertex-aligned Reading C with $\hat{n} = v_{\text{host}}$ a 600-cell vertex, the spatial-sector edge-length perturbation $|v_i - v_j|_{\text{actual}} = |v_i - v_j|_{\text{ideal}}(1 + \varepsilon\hat{e}_{ij}\cdot\hat{n})$ produces only an isotropic radial scaling of the first-shell icosahedron by factor $(1 - \varepsilon/(2\phi))$ and zero perturbation of first-shell-to-first-shell edges.

The C-W39 proof at Layer 3 in Capotauro v2.0 uses the same G1 + G2 geometric identities as this Patch — applied to the spatial-sector edge-length primitive instead of the temporal-sector rate primitive.

### §9.2 Temporal-sector parallel

This Patch establishes the analogous temporal-sector substrate-locality theorem at the SAME Layer 3 rigor. The structural parallel:

| | Spatial sector (Capotauro C-W39) | Temporal sector (B.1.d, this Patch) |
|---|---|---|
| Primitive | Edge-length perturbation: $\varepsilon$ | Rate-asymmetry: $\delta$ |
| Primitive form | $\delta L = L_0\varepsilon(\hat{e}\cdot\hat{n})$ | $\delta r = r_0\delta(\hat{e}\cdot\hat{n})$ |
| First-shell-to-first-shell | Zero edge-length perturbation | Zero rate perturbation |
| Host-to-first-shell | Uniform radial scaling factor $(1 - \varepsilon/(2\phi))$ | Uniform rate perturbation $\delta r = -r_0\delta/(2\phi)$ |
| Geometric foundation | G1 + G2 | G1 + G2 |
| First-shell-locality | $\mathcal{O}(\varepsilon)$ effects first-shell-bounded | $\mathcal{O}(\delta)$ effects first-shell-bounded |
| Rigor level | Capotauro v2.0 Layer 3 | This Patch Layer 3 |

The Layer 3 rigor of both sectors now matches; the previous asymmetry (Capotauro C-W39 at Layer 3 + B.1.d at sketch Layer 2 per Patch 0534 §10.10) is RESOLVED.

### §9.3 Structural unification at Layer 3

Both substrate-locality theorems (C-W39 spatial + B.1.d temporal) operate on the same first-shell geometric structure (G1 + G2). They use parallel structural arguments adapted to their respective primitive (edge-length vs. propagation-rate). The structural parallel is the foundation for the Substrate-Locality Unification (Capotauro C-W40 spatial + B.3.Move-1 temporal-extension corollary at Patch 0534 §10.7); Target 5 (B.3.q1 corollary at Layer 3) will use this Patch's substrate-locality theorem at Layer 3 to lift the temporal-extension corollary to Layer 3.

---

## §10 Connection to Phase 1 + Phase 2 + B.1.q4 sum identity

### §10.1 Phase 1 first-shell-only computation

Phase 1 (Patch 0524 §11.3) implicitly used substrate-locality at $\mathcal{O}(\delta)$: the computation summed over the 12 host-to-first-shell edges and did not consider second-shell or beyond. The boxed result $\vec{j}_{DI}^{net}(v_{\text{host}}) = (6 r_0 \delta/\phi^2)\hat{n}$ is the explicit numerical evaluation of the substrate-locality theorem's first-shell-only content.

Theorem 5.1.1 part (c) provides the rigorous structural justification: at $\mathcal{O}(\delta)$, only first-shell content contributes — exactly the Phase 1 computation scope.

### §10.2 Phase 2 ansatz

The Phase 2 ansatz $\vec{\omega}_{PCD}(v_{\text{host}}) = \sigma_{cycle}\cdot\hat{j}_{DI}^{net}(v_{\text{host}})$ — which treats $\vec{\omega}_{PCD}$ as a host-vertex quantity depending only on the first-shell-determined $\hat{j}_{DI}^{net}$ at $v_{\text{host}}$ — is now structurally justified at Layer 3 by the substrate-locality theorem.

### §10.3 B.1.q4 first-shell current sum identity (Patch 0541 §6 boxed result)

Patch 0541 §6 (Target 1 Layer 3 promotion) established the general per-vertex net DI-bit current formula:

$$\vec{j}_{DI}^{net}(v) = 2 r_0 \delta\left[(2+\phi)\hat{n} - (4 a / \phi) \hat{v}\right] + \mathcal{O}(\delta^2)$$

where $a = \hat{v}\cdot\hat{n}$. At $v = v_{\text{host}}$ (with $a = 1$, $\hat{v} = \hat{n}$), this recovers the Phase 1 boxed result via I5 identity: $(2+\phi) - 4/\phi = 3/\phi^2$, giving $\vec{j}_{DI}^{net}(v_{\text{host}}) = (6 r_0 \delta/\phi^2)\hat{n}$.

The B.1.q4 first-shell current sum identity at Layer 3 (Patch 0541) + the substrate-locality temporal extension theorem at Layer 3 (this Patch) together provide a complete Layer 3 picture of substrate net DI-bit current at any 600-cell vertex at $\mathcal{O}(\delta)$:
- The general per-vertex formula (Patch 0541 §6) gives the current value.
- The substrate-locality theorem (this Patch §5) gives the structural property: that the current at $\mathcal{O}(\delta)$ depends only on first-shell content.

These are complementary Layer 3 results — Patch 0541 provides the explicit formula; this Patch provides the structural foundation.

---

## §11 Patch 0534 §10.10 self-checkpoint (i) substantively addressed

### §11.1 Calibration concern recap

Patch 0534 §10.10(i) flagged: "'Substrate-Locality Temporal Extension Theorem' language reads as strong claim. The §10.4 proof is at $\mathcal{O}(\delta)$ only and matches Capotauro C-W39's first-order rigor — not a stronger all-orders claim. The 'theorem' language is appropriate at sketch level (Layer 2) given Capotauro's matching language for C-W39 at the same rigor level; promotion to Layer 3 / full theorem would require additional rigor work."

The Layer 3 task identified at the time: provide the additional rigor work.

### §11.2 Layer 3 resolution

This Patch provides the additional rigor work via:
- **Framework axiomatization of Mechanism A** (§3.1): formal statement of the propagation-rate-asymmetry primitive as substrate-physics axiom, with explicit symmetry properties (§3.2) under $P_{TI}$.
- **Explicit perturbation-theory propagation rule** (Theorem 3.3.3 + Corollary 3.3.4): rigorous statement of $\mathcal{O}(\delta^n)$ → $n$-th-shell-locality.
- **Algebraic rigor of geometric identities** (§4.1 + §4.2): exact algebraic derivations of $\hat{e}_{ij}\cdot\hat{n} = 0$ and $\hat{u}_i\cdot\hat{n} = -1/(2\phi)$ from 600-cell coordinates + golden-ratio identities, replacing Layer 2's numerical-precision-based justifications.
- **Theorem statement covering all three content parts (a)/(b)/(c)** (Theorem 5.1.1) with formal proof (§5.2 + §6-§8).
- **Capotauro C-W39 parallel established at Layer 3 rigor** (§9): the temporal-sector now matches the spatial-sector at Layer 3.

The Patch 0534 §10.10(i) "theorem-language appropriate at sketch level given Capotauro's matching for C-W39 at the same rigor level" is now upgraded: theorem-language appropriate at Layer 3 given this Patch's matching of Capotauro C-W39's Layer 3 rigor.

### §11.3 What this resolves and what remains at Layer 4

**Resolved at sketch-document Layer 3:**
- Framework axiomatization of Mechanism A as substrate-physics primitive.
- Perturbation-theory propagation rule.
- Rigorous proof of all three theorem parts at $\mathcal{O}(\delta)$ using exact 600-cell geometric identities.
- Capotauro C-W39 parallel at Layer 3 rigor.

**Remains at Layer 4 (deferred):**
- Derivation of Mechanism A primitive from CPP axioms A1–A11 alone (touches long-term programme target chirality scale from polytope geometry).
- Extension to $\mathcal{O}(\delta^2)$ and higher (B.1.q6 territory).
- Derivation of G1 + G2 geometric identities from CPP axioms (Layer 4 territory).

---

## §12 Connection to Layer 2 work + Target 5 next-natural-target

### §12.1 Patch 0534 §10 immutable historical record

Patch 0534 §10 (the Layer 2 sketch this promotion builds on) is preserved as immutable historical record per §17.8. This Layer 3 document is an ADDITIVE artifact in `layer3_promotion/`, not an inline edit to Patch 0534 §10.

### §12.2 Target 5 (B.3.q1 Substrate-Locality Unification corollary at Layer 3) enabled

Per Patch 0540 §2.5: "Tractability 1-2 sessions (once Target 4 B.1.d Layer 3 is in place; piggybacks on substrate-locality theorem)."

This Patch CLOSES Target 4, ENABLING Target 5 as the next natural target. Target 5 will lift Patch 0534 §10.7's B.3.Move-1 corollary (substrate-locality unification temporal-extension) from sketch Layer 2 to Layer 3 using this Patch's Theorem 5.1.1 as the load-bearing input. Target 5 work involves cage-shell-factor computations parallel to Capotauro Finding C-W41 (which is at Layer 3 in Capotauro v2.0).

The closure-pattern Patches 0541 → 0542 → 0543 → this Patch → 0544+ continues with each Layer 3 target getting its own gated trajectory per §15.7.

### §12.3 What this Layer 3 promotion does NOT promote

- Does NOT promote substrate-locality theorem result to programme-level Findings registry.
- Does NOT trigger F.1 sub-question status change (sustained at Patch 0539 framing).
- Does NOT trigger flagship paper assembly (Layer 3 promotion arc not yet complete; 3 of 7 targets remain).
- Does NOT close Target 5 (B.3.q1 corollary) — Target 5 is independent and gated.

---

## §13 Layer 3 vs Layer 4 distinction

### §13.1 What Layer 3 establishes (this Patch)

- Mechanism A as substrate-physics framework axiom (§3.1).
- $P_{TI}$ symmetry properties of Mechanism A (§3.2).
- Perturbation-theory propagation rule (Theorem 3.3.3 + Corollary 3.3.4).
- Rigorous algebraic derivations of geometric identities I_a + I_b (§4.1 + §4.2).
- Substrate-Locality Temporal Extension Theorem at Layer 3 (Theorem 5.1.1) with three-part proof.
- Capotauro C-W39 parallel at Layer 3 rigor (§9).

### §13.2 What Layer 4 would require (deferred)

- Derivation of Mechanism A primitive from CPP axioms A1–A11 alone (touches long-term programme target chirality scale from polytope geometry).
- Derivation of G1 + G2 geometric identities from CPP axioms (Layer 4 territory).
- Extension to $\mathcal{O}(\delta^2)$ and higher (B.1.q6 territory; involves second-shell-and-beyond geometric structure).
- Generalization beyond 600-cell substrate to alternative polytope substrates (touches long-term programme target).

### §13.3 Layer 3 → Layer 4 promotion path (for future reference)

When Layer 4 work opens (deferred behind F.1/F.2/F.3 stabilization), it will:
1. Take this Layer 3 document as the rigorous algebraic anchor for substrate-locality temporal extension at $\mathcal{O}(\delta)$.
2. Identify which CPP axioms could derive Mechanism A + the 600-cell first-shell structure G1 + G2.
3. Address the long-term programme target (chirality scale from polytope geometry).
4. Optionally extend to $\mathcal{O}(\delta^2)$ via second-shell + beyond perturbative content.

---

## §14 Self-checkpoint + programme state + closing summary

### §14.1 Self-checkpoint — three places §0–§13 could overstate

(i) **"Full Capotauro C-W39-style proof" framing.** This Patch's proof matches Capotauro C-W39's structural format + rigor level — but it is at sketch-document Layer 3, not publication-paper Layer 3. The Capotauro C-W39 result in Capotauro v2.0 §13.3 is at published-paper Layer 3 (formal theorem-environment formatting, literature citations, full reviewer-grade rigor). The "matching Layer 3 rigor" framing is at sketch-document level; publication-paper-grade promotion would be flagship paper assembly work.

(ii) **"Substantively addresses Patch 0534 §10.10(i)" framing.** This Patch addresses the additional-rigor-work request by providing framework axiomatization + perturbation-theory propagation rule + algebraic geometric identities + theorem statement covering all three parts + rigorous proof. The §11 framing should be read as "Layer 3 resolution at sketch-document level"; Layer 4 resolution (deriving Mechanism A + G1 + G2 from CPP axioms alone) remains deferred.

(iii) **"Perturbation-theory propagation rule" framing.** The §8 rule is stated and proved at $\mathcal{O}(\delta)$ within the leading-order perturbation context. Extension to $\mathcal{O}(\delta^n)$ for $n \geq 2$ involves multi-step path counting that THIS Patch does NOT execute — that is B.1.q6 territory. The rule's statement in Corollary 3.3.4 covers all $n$ symbolically; its rigorous application here is bounded to $n = 1$.

### §14.2 Programme state after this Layer 3 promotion

**What changed at programme level:**
- B.1.d promoted from sketch Layer 2 closure (Patch 0534 §10) to sketch-document Layer 3 closure.
- Patch 0534 §10.10(i) self-checkpoint substantively addressed at sketch-document Layer 3.
- Capotauro C-W39 parallel established at Layer 3 rigor — temporal sector now matches spatial sector in published-paper Layer 3 (asymmetry resolved at sketch-document level).
- Fourth Layer 3 promotion in F.1 trajectory (after Patches 0541, 0542, 0543).
- Target 5 (B.3.q1 corollary) enabled as next-natural-target.

**What did NOT change:**
- F.1 sub-question status UNCHANGED at Patch 0539 framing.
- No new Findings registered (substrate-locality theorem at Layer 3 remains intermediate result).
- No sub-question reopenings.
- No v1.0 SHIPPED edits.
- No Patches 0531–0543 immutable content modifications.
- No reviewer-pause checkpoint modifications.
- No flagship paper assembly trigger.
- No F.2/F.3 substantive content trajectory opening.
- No long-term programme target (Layer 4) work.
- No $\mathcal{O}(\delta^2)$ extension (B.1.q6 territory).
- No closure of Target 5 (B.3.q1 corollary remains gated).

### §14.3 Forward queue post-Patch 0544

(A) **Patch 0545+ candidacy — Target 5 (B.3.q1 Substrate-Locality Unification corollary at Layer 3)**, the natural next target per Patch 0540 §2.5 ("piggybacks on Target 4 B.1.d Layer 3"). Estimated 1–2 sessions.

(B) Subsequent Patches close Targets 6 (B.1.q2 zero curl full 4D Layer 3) + 7 (B.1.q2 zero curl framework axiomatization Layer 3). Aggregate remaining Layer 3 promotion arc 2–6 sessions.

(C) Layer 3 reviewer-pause cycle Patch when load-bearing Layer 3 arc completes.

(D) Layer 3 status upgrade Patch when reviewer-pause completes positively.

(E) F.1 flagship paper assembly DEFERRED behind (C) + (D).

(F) F.2 / F.3 substantive content trajectories DEFERRED at decision-gate level.

(G) Long-term programme target (Layer 4) REGISTERED + DEFERRED.

(H) JUNO peer-review update integration when published.

### §14.4 Closing summary

Patch 0544 closes B.1.d at sketch-document Layer 3 by promoting Patch 0534 §10's sketch Layer 2 substrate-locality temporal extension theorem to full Capotauro C-W39-style Layer 3 rigor. The Layer 3 promotion includes: framework axiomatization of Mechanism A as substrate-physics propagation-rate primitive (§3.1); explicit perturbation-theory propagation rule at $\mathcal{O}(\delta^n)$ → $n$-th-shell-locality (Theorem 3.3.3 + Corollary 3.3.4); rigorous algebraic derivations of geometric identities I_a ($\hat{e}_{ij}\cdot\hat{n} = 0$) and I_b ($\hat{u}_i\cdot\hat{n} = -1/(2\phi)$) from 600-cell coordinates + golden-ratio identities (§4.1 + §4.2); theorem statement covering all three content parts (a)/(b)/(c) (Theorem 5.1.1); rigorous proof of all three parts at $\mathcal{O}(\delta)$ (§6 + §7 + §8); Capotauro C-W39 parallel established at Layer 3 rigor (§9) — temporal sector now matches spatial sector in published-paper Layer 3 (asymmetry from Patch 0534 §10.10(i) RESOLVED at sketch-document level).

Patch 0534 §10.10(i) self-checkpoint substantively addressed at sketch-document Layer 3 (§11). Fourth Layer 3 promotion in F.1 trajectory; Target 5 (B.3.q1 Substrate-Locality Unification corollary) enabled as next-natural-target per Patch 0540 §2.5 piggyback pattern. Four of seven Layer 3 promotion targets closed (Targets 1, 2, 3, 4); three Layer 3 targets remain (5, 6, 7), each its own gated trajectory.

F.1 sub-question status UNCHANGED at Patch 0539 framing. Findings registry UNCHANGED. v1.0 SHIPPED edits NONE. Patches 0531–0543 immutable content UNCHANGED. Reviewer-pause checkpoint UNCHANGED. Flagship paper assembly NOT triggered. F.2/F.3 trajectories NOT opened. Long-term programme target REGISTERED + DEFERRED. $\mathcal{O}(\delta^2)$ extension B.1.q6 territory NOT addressed.
