# F.1 OPEN-FP-F1-1 — $\mathcal{O}(\delta^2)$ Second-Shell Extension Scoping

**Path:** `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/F1_o_delta_squared_extension_scoping.md`
**Opened:** 26 May 2026 (Session 144 Patch 0571i)
**Author:** Opus (Claude)
**Status:** Scoping at sketch level. NOT closure work. Opens the OPEN-FP-F1-1 trajectory as a multi-session arc; this document does not execute any closure work, does not propose framework extensions, does not modify the v1.0 SHIPPED F.1 paper or its hardened-theorem artifacts.
**Scope:** Enumerate the second-shell inner-product identities, edge-projection identities, and framework-extension questions required to extend F.1 Theorem 7.1 from $\mathcal{O}(\delta^1)$ to $\mathcal{O}(\delta^2)$. Articulate three candidate closure routes with their trade-offs. Propose a hardened-theorem artifact sequence parallel to Patches 0550 + 0551 + 0552 + 0571. Identify decision-gate items requiring Thomas input before substantive Layer 3 work begins.

---

## §0 Working-session firewall + anti-priorities

### §0.1 What this sketch IS

This document opens the **OPEN-FP-F1-1 trajectory** — the substantive multi-session physics arc that extends F.1's $\mathcal{O}(\delta^1)$ substrate-locality umbrella to $\mathcal{O}(\delta^2)$. The scope is:

- Enumerate the geometric identities required at second-shell order (second-shell projections + edge-direction projections + path-class structure);
- Surface the framework-extension question (how Mechanism A's framework-local current construction extends from $\mathcal{O}(\delta^1)$ to $\mathcal{O}(\delta^2)$);
- Articulate three candidate closure routes with explicit trade-offs;
- Propose a publication-grade Layer 3 hardened-theorem artifact sequence parallel to the O(δ¹) sequence (Patches 0550 + 0551 + 0552 + 0571);
- Identify decision-gate items requiring Thomas input;
- Register a risk inventory.

The scope is **scoping at sketch level**, NOT closure work. Each identity, each framework question, and each artifact in §5 is its own gated sub-trajectory; this document enumerates them but does not execute any of them.

### §0.2 Anti-priorities sustained at this Patch

Per the cumulative Patch 0571a–0571h discipline + the OPEN-FP-F1-1 scoping window, the following are NOT triggered by this Patch:

1. **NO Layer 3 closure work in this Patch** — this is the scoping document. Each second-shell geometric identity is a separate gated sub-trajectory.
2. **NO modification of v1.0 SHIPPED F.1 paper sources** — `dynamical_substrate_law.tex` and `dynamical_substrate_law.pdf` are frozen at v1.0 SHIPPED per Patch 0570 + §17.8 immutable-checkpoint discipline. Higher-order extensions live in this sketch (and subsequent OPEN-FP-F1-1 trajectory Patches) until a future v1.1 or v2.0 micro-revision integrates them.
3. **NO modification of hardened-theorem artifacts** — Patches 0550 + 0551 + 0552 + 0571 are frozen. Higher-order artifacts will be NEW `.tex` files under `hardened_theorems/` at future Patches.
4. **NO modification of F.1's three programme-level theorems** (THEO-DSL-1 + THEO-DSL-2 + THEO-DSL-3 in `theorem-registry.md` SD section, registered at Patch 0581). New higher-order theorems would be registered as THEO-DSL-4 + THEO-DSL-5 + ... at future Patches when they reach publication-grade Layer 3 rigor.
5. **NO framework-extension commitment in this Patch** — §3.1 surfaces the framework-extension question (how MA.2 extends to $\mathcal{O}(\delta^2)$) but does not commit to a specific extension. The commitment is a decision-gate item (§7) requiring substantive deliberation in a subsequent session.
6. **NO new Open Problem registrations** at programme level in this Patch — the parent Open Problem OPEN-FP-F1-1 is already registered; sub-questions surfaced here are scoping-internal until they crystallize into separately-trackable closure sub-targets.
7. **NO reviewer engagement** on this scoping Patch — Layer 3 scoping Patches do not require external review per `templates/operating_system.md` §17 codified discipline (external reviewers engage at v0.9 → v1.0 SHIP cycles, not at scoping stages).
8. **NO promotion of any sub-target to closure-Patch trajectory in this Patch** — sub-target promotion is a decision-gate item.
9. **NO bundling of multiple sub-targets into single closure Patch** — each Layer 3 sub-target is its own gated trajectory per the four-artifact pattern established at Patches 0550 + 0551 + 0552 + 0571.
10. **NO F.2 / F.3 substantive content trajectory opening** — DEFERRED per `manifestation_inventory.md` (manifestations iii and v remain open with no current closure-trajectory machinery; F.2 / F.3 territory is downstream of OPEN-FP-F1-1 work).

### §0.3 What this sketch IS NOT

- It is NOT an O(δ²) derivation. The derivation is multi-session substantive physics work; this document scopes that work.
- It is NOT a framework-extension proposal. The framework-extension question is surfaced (§3.1) but answered later.
- It is NOT a commitment to a closure route. Three routes are articulated (§4) with trade-offs; route selection is a decision-gate item.
- It is NOT a paper-assembly document. The OPEN-FP-F1-1 closure (when it lands) will be integrated into F.1 v1.1 or v2.0; the sketch does not prefigure paper assembly.

---

## §1 Purpose and structure

### §1.1 Why scope this trajectory now

OPEN-FP-F1-1 was registered as one of six in-body Open Problems at F.1 v1.0 SHIP (Patch 0570, 24 May 2026). Per FP.md, it is independent of OPEN-FP-F1-2 (Layer 4 derivation) and was independent of OPEN-FP-F1-3 (G1 hardening, closed at Patch 0571). After OPEN-FP-F1-3's closure, the two highest-priority remaining substrate-locality programme targets are OPEN-FP-F1-1 (this trajectory) and OPEN-FP-F1-2; either may be pursued first.

Reasons OPEN-FP-F1-1 is the natural next substantive physics target:

- **Closure-trajectory machinery exists.** F.1 Theorem 6.1 (perturbation-locality propagation rule) implies the $\mathcal{O}(\delta^2)$ coefficient at $v_{\text{host}}$ depends only on edges in the 2-ball $E_2(v_{\text{host}})$ of the 600-cell graph. Theorem 6.1's hardened artifact (`perturbation_locality_propagation.tex`, Patch 0550) underwrites the locality at second order without re-derivation.
- **Second-shell geometry is well-characterised.** The 20 second-shell vertices of the 600-cell at $v_{\text{host}}$ form a regular dodecahedron at distance $\sqrt{2 - 2\cos 72^\circ} = \phi^{-1}\sqrt{3 - \phi}$ from $v_{\text{host}}$. The polytope-theoretic data is in the literature (Coxeter, Conway & Sloane); only the substrate-direction-projection structure needs new derivation.
- **Symmetry argument prefigures the structural claim.** Under the $H_3 = I_h$ residual symmetry at $v_{\text{host}}$, the dodecahedron of second-shell vertices is a single $I_h$ orbit, so the host-to-second-shell projection $\hat{w}_j \cdot \hat{n}$ is uniform across all 20 vertices (parallel to F.1 Theorem 5.1 for the first shell). The parallel-to-$\hat{n}$ structure of $\vec{J}_{\text{DI-net}}(v_{\text{host}})$ at $\mathcal{O}(\delta^2)$ follows from $I_h$-invariance, prior to coefficient computation.
- **Foundations sketch exists.** `sketches/F1_phase2_foundations_work.md` (Patch 0531 + subsequent) and `sketches/F1_subquestion_pcd_orientation_link.md` (the Phase 2 closure work) contain the substrate-direction primitive scoping and Reading C framework that the O(δ²) work inherits without re-derivation.

### §1.2 What "scoping at sketch level" means here

Per the handover §13 estimates from `handovers/2026-05-21_session_138_F1_sub_question_provisional_closure.md` (which calibrated multi-session budget for the F.1 sub-question's Phase 2 work), individual closure-target sub-trajectories take 1–6 sessions each. The OPEN-FP-F1-1 trajectory has ~5 sub-targets (per §5 below); the total trajectory budget is therefore estimated at 5–15 sessions of substantive physics work distributed across the artifact sequence.

This scoping document opens the trajectory in 1 Patch (this Patch 0571i) and identifies the sub-trajectories. The substantive closure work happens at subsequent Patches, gated per the four-artifact pattern.

### §1.3 Document structure ahead

- §2 — Recap of the $\mathcal{O}(\delta^1)$ closure structure (what's being extended).
- §3 — The $\mathcal{O}(\delta^2)$ extension challenge in three structural questions.
- §4 — Three candidate closure routes with trade-offs.
- §5 — Proposed hardened-theorem artifact sequence.
- §6 — Pre-existing material to lean on.
- §7 — Decision-gate items requiring Thomas input.
- §8 — Risk register.
- §9 — Session-close discipline + forward queue.

---

## §2 Recap of the $\mathcal{O}(\delta^1)$ closure structure

For traceability, this section reproduces the structural arc of F.1's $\mathcal{O}(\delta^1)$ closure. The $\mathcal{O}(\delta^2)$ work extends this structure to second order; understanding what at first order is *load-bearing* is the prerequisite for identifying what at second order needs derivation.

### §2.1 First-order closure assembly

F.1 v1.0 Theorem 7.1 (substrate-locality umbrella, sketch-document Layer 3) states:

$$\vec{j}_{DI}^{\,\text{net}}(v_{\text{host}}) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$$

The proof at sketch-document Layer 3 assembles three publication-grade Layer 3 inputs:

1. **Theorem 5.1 (host-to-first-shell uniform projection, hardened Patches 0552 + 0571):** $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ uniformly across all 12 first-shell unit vectors at vertex-aligned Reading C.
2. **Theorem 5.2 (first-shell-to-first-shell perpendicularity, hardened Patches 0551 + 0571):** $\hat{e}_{ij} \cdot \hat{n} = 0$ for all 30 first-shell-to-first-shell edges.
3. **Theorem 6.1 + Corollary 6.2 (perturbation-locality propagation rule + shell-locality at $\mathcal{O}(\delta^1)$, hardened Patch 0550):** at $\mathcal{O}(\delta^1)$ the current at $v_{\text{host}}$ depends only on edges incident to $v_{\text{host}}$ (the 12 host-to-first-shell edges).

The assembly applies MA.2 at $\mathcal{O}(\delta^1)$:

$$\vec{j}_{DI}^{\,\text{net}}(v_{\text{host}}) \big|_{\mathcal{O}(\delta^1)} = \sum_{w \sim v_{\text{host}}} (r_{v_{\text{host}}, w} - r_{w, v_{\text{host}}}) \hat{e}_{v_{\text{host}}, w} = 2 r_0 \delta \sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n}) \hat{u}_i$$

The rank-1 sum identity (PRED-O-30):

$$\sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n})\,\hat{u}_i = (3/\phi^2)\,\hat{n}$$

is derived from Theorem 5.1 (uniform projection $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$) + $I_h$ residual symmetry (the icosahedron's vertex set has zero centroid; the projection cancels the orthogonal components leaving only the $\hat{n}$-component). Yielding:

$$\vec{j}_{DI}^{\,\text{net}}(v_{\text{host}}) \big|_{\mathcal{O}(\delta^1)} = 2 r_0 \delta \cdot (3/\phi^2)\,\hat{n} = (6 r_0 \delta/\phi^2)\,\hat{n}$$

### §2.2 What's load-bearing at first order

The first-order closure is *load-bearing* on:

- The **12 host-to-first-shell unit-direction projections** (Theorem 5.1) — a single uniform constant $-1/(2\phi)$.
- The **30 first-shell-to-first-shell edge-direction projections** (Theorem 5.2) — uniformly zero.
- The **icosahedral rank-1 sum identity** (PRED-O-30) — derived from the above + $I_h$ residual symmetry.
- **MA.2 at $\mathcal{O}(\delta^1)$** — the framework-local current construction restricted to edges incident to $v_{\text{host}}$.

Nothing about the second shell, the dodecahedron geometry, the first-shell-to-second-shell edges, or path-structures of length $> 1$ enters the first-order closure. All of these enter at second order.

### §2.3 Why first-order machinery propagates to second order partially

F.1 Theorem 6.1 (perturbation-locality propagation rule) is *order-independent* in its statement: at $\mathcal{O}(\delta^n)$, the current at $v_{\text{host}}$ depends only on edges in the $n$-ball $E_n(v_{\text{host}})$. So Theorem 6.1's hardened artifact (Patch 0550, `perturbation_locality_propagation.tex`) underwrites the second-order locality bound without re-derivation. The $\mathcal{O}(\delta^2)$ work does not re-prove Theorem 6.1 — it inherits the bound and computes within it.

The first-order Theorems 5.1 + 5.2 are *load-bearing only for the first-order computation*. The second shell needs its own analogs of these identities (per §3.2 below).

The framework-local current construction MA.2 is *defined at first order* in F.1 §4. Whether MA.2 extends to second order naturally, or requires explicit higher-order definition, is the framework-extension question of §3.1.

---

## §3 The $\mathcal{O}(\delta^2)$ extension challenge in three structural questions

### §3.1 Question Q1 — Framework-local current construction at $\mathcal{O}(\delta^2)$

**The question.** F.1 §4's framework axiom MA.2 defines $\vec{j}_{DI}^{\,\text{net}}(v)$ at first order in $\delta$ as a sum over edges incident to $v$ with the rate-asymmetry factor $(r_{v,w} - r_{w,v}) \hat{e}_{v,w}$. The rate-asymmetry factor is exactly $2 r_0 \delta (\hat{e}_{v,w} \cdot \hat{n})$, which is first-order in $\delta$. The first-order MA.2 expression therefore yields $\mathcal{O}(\delta^1)$ output from $\mathcal{O}(\delta^1)$ input — what is the analogous expression at $\mathcal{O}(\delta^2)$?

**Three sub-options to evaluate:**

(A) **Direct extension via path-integral structure.** The underlying DI-bit dynamics on the 600-cell graph is a Markov-style propagation; at $\mathcal{O}(\delta^n)$ the net current at $v$ involves contributions from paths of length $n$ from $v$ back to $v$ with $n$ perturbed-edge insertions. At $\mathcal{O}(\delta^2)$, the current at $v_{\text{host}}$ involves paths of length 2 traversing edges in $E_2(v_{\text{host}})$ (consistent with Theorem 6.1). The framework-local current at $\mathcal{O}(\delta^2)$ is a closed-form expression in terms of these path products. MA.2 extends naturally without new framework input.

(B) **Higher-order framework axiom MA.3.** Mechanism A might require a new framework-axiomatic statement at $\mathcal{O}(\delta^2)$ defining the second-order rate-asymmetry corrections or path-product weightings explicitly. MA.3 would be a substrate-physics commitment, parallel to MA.1 + MA.2 at first order, requiring its own conditional-on-Mechanism-A status flag.

(C) **Re-derivation from CPP primitive axioms A1–A11.** If MA.2 at $\mathcal{O}(\delta^2)$ requires framework input that cannot be derived from MA.1 + MA.2 alone, the closure work could engage OPEN-FP-F1-2 (Layer 4 axiomatic derivation) as a prerequisite. This couples OPEN-FP-F1-1 and OPEN-FP-F1-2, contradicting the independence registered in FP.md ("mutually orthogonal at first order").

**Initial assessment** (sketch level): sub-option (A) is the most parsimonious and matches the standard perturbation-theory machinery in physics. Sub-option (B) is acceptable if (A) cannot be derived from MA.1 + MA.2 alone (the framework would acknowledge the higher-order extension as a separate framework commitment). Sub-option (C) would couple the two open problems and substantially escalate scope.

**Decision-gate item:** which sub-option does the closure work proceed under? This is registered as DG-1 in §7 for Thomas's substantive input.

### §3.2 Question Q2 — Second-shell geometric identities required

Assuming Q1 is settled, the $\mathcal{O}(\delta^2)$ computation requires the following second-shell geometric identities. Each is a potential hardened-theorem artifact in the §5 sequence.

#### §3.2.1 Identity G2.1 — Host-to-second-shell uniform projection

**Statement (target):** For each of the 20 second-shell vertices $w_j$ at vertex-aligned Reading C in the 600-cell, the unit vector $\hat{w}_j = (w_j - v_{\text{host}})/|w_j - v_{\text{host}}|$ has projection on $\hat{n}$ equal to a single constant $c_2$ independent of $j$:

$$\hat{w}_j \cdot \hat{n} = c_2, \qquad j = 1, 2, \ldots, 20.$$

**Why it should hold:** $H_3 = I_h$ residual symmetry at $v_{\text{host}}$ acts on the second shell as the full icosahedral group; the 20 second-shell vertices form a single $I_h$ orbit (the regular dodecahedron's vertex set under $I_h$). By orbit-stabilizer transitivity, the inner product $\hat{w}_j \cdot \hat{n}$ is constant on the orbit.

**What needs derivation:** The specific value of $c_2$. By analogy to $c_1 = -1/(2\phi)$ for the first shell, $c_2$ is expected to be a golden-ratio rational. Candidate from second-shell geometry: the dodecahedron's vertices at distance $d_2 = \phi^{-1}\sqrt{3 - \phi}$ from $v_{\text{host}}$ have known $\hat{n}$-projection structure via the substrate's $\phi$-quantization (Patch 0419 Finding C-W37 ratio analysis). Computation should yield $c_2$ in closed form.

**Conditionality:** Conditional on a second-shell inner-product primitive (the analog of G1 for the second shell — call it G2). G2's status (sketch-document vs publication-grade Layer 3) is itself a downstream hardening target. The §5 artifact sequence accordingly has G2.1's first version conditional on G2.

#### §3.2.2 Identity G2.2 — Host-to-second-shell rank-1 sum identity

**Statement (target):** The icosahedral analog of PRED-O-30 for the second shell:

$$\sum_{j=1}^{20} (\hat{w}_j \cdot \hat{n})\,\hat{w}_j = c_3\,\hat{n}$$

for some constant $c_3$ derived from G2.1 + $I_h$ residual symmetry on the dodecahedron orbit.

**Why it should hold:** Parallel to PRED-O-30's derivation. The dodecahedron's vertex set has zero centroid; the projection cancels orthogonal components leaving only the $\hat{n}$-component. Coefficient $c_3 = 20 \cdot c_2^2$ by the trace identity $\text{tr}(\sum_j \hat{w}_j \otimes \hat{w}_j) = 20$ + the $I_h$-invariance forcing rank-2 form $\alpha \hat{n} \otimes \hat{n} + \beta(I - \hat{n} \otimes \hat{n})$. Then $\alpha = 20 c_2^2$ on the $\hat{n}$-component.

**What needs derivation:** The explicit value of $c_3$ in closed form (golden-ratio rational expected).

#### §3.2.3 Identity G2.3 — First-shell-to-second-shell edge-direction projections

**Statement (target):** For each of the 60 first-shell-to-second-shell edges, the edge-direction projection $\hat{e}_{ij'} \cdot \hat{n}$ (where $i$ is a first-shell vertex index, $j'$ a second-shell vertex index).

**Why it's harder than G2.1:** The 60 first-shell-to-second-shell edges do NOT form a single $I_h$ orbit. They decompose into orbit classes under $I_h$ acting on (first-shell, second-shell) ordered pairs subject to the adjacency relation. The first-shell-vertex-stabilizer is $D_{3d}$ (one of the 12 $D_{3d}$ sub-stabilizers of $I_h$, per Capotauro v2.0 Finding C-W37); the adjacency relation under $D_{3d}$ partitions the 60 edges into 5 orbit classes of 12 edges each (one class per first-shell vertex by orbit-stabilizer counting on the $D_{3d}$-fixed-point structure).

**What needs derivation:** Five distinct projection values $a_1, a_2, a_3, a_4, a_5$ (one per orbit class) with closed-form expressions; or alternatively a structural identity proving the sum or weighted-sum over the 60 edges has a closed form.

#### §3.2.4 Identity G2.4 — Second-shell-to-second-shell edge-direction projections

**Statement (target):** For each of the 30 second-shell-to-second-shell edges (the edges of the dodecahedron of second-shell vertices), the edge-direction projection $\hat{e}_{j_1 j_2} \cdot \hat{n}$.

**Why it's analogous to F.1 Theorem 5.2:** The dodecahedron's edges form an $I_h$ orbit; by the same argument as for the icosahedron's edges (F.1 Theorem 5.2), the projection should vanish: $\hat{e}_{j_1 j_2} \cdot \hat{n} = 0$.

**What needs derivation:** Verification that the perpendicularity argument extends to the dodecahedron's edges (or identification of where it breaks down). If perpendicularity holds, the second-shell-to-second-shell edge contributions to the $\mathcal{O}(\delta^2)$ current vanish — substantially simplifying the closure.

### §3.3 Question Q3 — Path-class enumeration for $\mathcal{O}(\delta^2)$ current

**The question.** At $\mathcal{O}(\delta^2)$, the net current at $v_{\text{host}}$ involves contributions from paths of length 2 traversing edges in $E_2(v_{\text{host}})$ with two perturbed-edge insertions. Enumerate the path classes and their contributions.

**Path-class enumeration (preliminary; needs verification at closure):**

(i) **[HH] paths via single edge — host → first-shell → host on same edge.** Two perturbed insertions on the same edge. Contribution: $(r_{v_{\text{host}}, w} \cdot r_{w, v_{\text{host}}}) - (r_{w, v_{\text{host}}} \cdot r_{v_{\text{host}}, w})$ — these are identical products, so the difference vanishes. ZERO contribution.

(ii) **[HFFH] paths — host → first-shell-$i$ → first-shell-$j$ → host.** Two perturbed insertions on distinct edges; closed-loop returning to host through different first-shell vertices via a first-shell-to-first-shell edge. Edges traversed: $(v_{\text{host}}, w_i) + (w_i, w_j) + (w_j, v_{\text{host}})$. Three edges, with two perturbed insertions among them. Contributing to current at $v_{\text{host}}$ via path products at $\mathcal{O}(\delta^2)$.

(iii) **[HFS+SFH] paths — host → first-shell → second-shell → first-shell → host.** Two distinct edges with one perturbed each at $\mathcal{O}(\delta^1) \times \mathcal{O}(\delta^1) = \mathcal{O}(\delta^2)$. Path traverses 4 edges (host-to-first, first-to-second, second-to-first, first-to-host).

(iv) **[HFSSFH] paths — host → first-shell → second-shell → second-shell → first-shell → host.** Path of length 5 with two perturbed-edge insertions; traverses a second-shell-to-second-shell edge.

(v) **[HFFFH] paths — host → first-shell → first-shell → first-shell → host.** Path of length 4 within the first shell after the initial host-to-first-shell hop.

(vi) Higher-order combinations exhausting all paths in $E_2(v_{\text{host}})$ with exactly two perturbed insertions.

**Why class enumeration matters:** Each class contributes a sum over the relevant edge-direction products weighted by the path-product structure (sub-option (A) of Q1). The total $\mathcal{O}(\delta^2)$ current is the sum over classes. The closed-form expression requires evaluating each class's sum analytically using G2.1 + G2.2 + G2.3 + G2.4 + F.1 Theorems 5.1 + 5.2.

**Scope of work:** Path-class enumeration is the most under-specified element of the trajectory at scoping time. A full enumeration and weight-formula derivation is a sub-trajectory of 1–3 sessions of structural exploration parallel to the geometric-identity work.

---

## §4 Three candidate closure routes with trade-offs

### §4.1 Route A — Direct derivation (full computation)

**Approach:** Derive all geometric identities G2.1 + G2.2 + G2.3 + G2.4 + path-class weight formulas from 600-cell coordinates + $I_h$ residual symmetry. Compute the closed-form $\mathcal{O}(\delta^2)$ coefficient explicitly.

**Output:** $\vec{j}_{DI}^{\,\text{net}}(v_{\text{host}}) = (6\delta/\phi^2)\hat{n} + (c_{\mathcal{O}(\delta^2)} \delta^2)\hat{n} + \mathcal{O}(\delta^3)$ with $c_{\mathcal{O}(\delta^2)}$ in closed-form golden-ratio rational expression.

**Strengths:**
- Strongest closure — gives explicit coefficient.
- Parallels F.1 v1.0 methodology directly.
- Falsifiable: the closed-form coefficient can be numerically verified at machine precision.
- Establishes both structural claim (parallel-to-$\hat{n}$) and quantitative claim (specific coefficient).

**Weaknesses:**
- Highest computational burden — requires G2.1 + G2.2 + G2.3 + G2.4 + path-class enumeration + weight-formula derivation, all at publication-grade Layer 3 rigor.
- Most session budget (estimated 5–10 sessions).
- Requires the framework-extension question Q1 to be settled in sub-option (A) — and provides no fallback if (A) turns out to be insufficient.

### §4.2 Route B — Symmetry-only structural closure

**Approach:** Prove that $\vec{j}_{DI}^{\,\text{net}}(v_{\text{host}})$ at $\mathcal{O}(\delta^2)$ is parallel to $\hat{n}$ from $I_h$ residual symmetry alone, without computing the coefficient.

**Argument sketch:** The perturbation $r(\hat{e}) = r_0(1 + \delta \hat{e} \cdot \hat{n})$ breaks $H_4 \to H_3 = I_h$ at $v_{\text{host}}$ but preserves $I_h$. The current $\vec{j}_{DI}^{\,\text{net}}(v_{\text{host}})$ is therefore $I_h$-invariant at all orders in $\delta$ (the perturbation expansion preserves the residual symmetry order-by-order). Any $I_h$-invariant vector at $v_{\text{host}}$ must be parallel to $\hat{n}$ (since $\hat{n}$ is the only $I_h$-invariant direction). Conclusion: $\vec{j}_{DI}^{\,\text{net}}(v_{\text{host}}) \big|_{\mathcal{O}(\delta^2)} \propto \hat{n}$ at second order.

**Output:** Parallel-to-$\hat{n}$ structural theorem at $\mathcal{O}(\delta^2)$ without coefficient.

**Strengths:**
- Minimal computational burden (1–2 sessions to formalize).
- Independent of Q1 sub-option choice (symmetry argument doesn't need framework-current-extension details).
- Falsifies the alternative (tangent components at $\mathcal{O}(\delta^2)$) directly via group-theoretic argument.
- Higher-rigor floor: the symmetry argument is publication-grade Layer 3 from the start.

**Weaknesses:**
- Only structural (parallel-to-$\hat{n}$), not quantitative (no coefficient).
- Does not close the OPEN-FP-F1-1 question fully — the open question asks about both the structure AND the coefficient.
- A future Route A would be required after Route B to compute the coefficient.

### §4.3 Route C — Hybrid

**Approach:** Apply Route B (symmetry-only) for the parallel-to-$\hat{n}$ structural claim; apply Route A (direct derivation) for the coefficient computation. Separate the two epistemic goals into two artifact sequences.

**Output:**
- Artifact sequence 1: Symmetry-only structural theorem (publication-grade Layer 3 from the start, 1–2 sessions).
- Artifact sequence 2: Direct-derivation coefficient (publication-grade Layer 3 conditional on G2, 4–8 sessions).

**Strengths:**
- Best of both: rigorous structural claim early, quantitative claim later.
- Decouples the two epistemic risks (symmetry argument can land before geometric-identity derivations are complete).
- Provides intermediate closure milestones (structural theorem at end of artifact sequence 1 is itself a publication-grade Layer 3 result).
- Strongest fit with the four-artifact pattern (sequence 1 = 1 artifact; sequence 2 = ~4 artifacts, paralleling Patches 0550 + 0551 + 0552 + 0571).

**Weaknesses:**
- Two artifact sequences double the bookkeeping overhead.
- Sequence 2 still has Route A's high computational burden — Route C does not reduce total budget, just stages it.

### §4.4 Initial recommendation

**Route C (Hybrid)** appears strongest for the OPEN-FP-F1-1 trajectory:
- Yields a publication-grade Layer 3 result (the symmetry-only structural theorem) in 1–2 sessions, providing immediate progress and a useful citation point for downstream work.
- Decouples symmetry-rigor from geometric-identity-rigor.
- The coefficient computation (sequence 2) can be pursued at its own cadence without blocking the structural result.

The recommendation is sketch-level (per §0.1 anti-priority 5); route selection is a decision-gate item (§7 DG-2).

---

## §5 Proposed hardened-theorem artifact sequence

Parallel to the O(δ¹) sequence (Patches 0550 + 0551 + 0552 + 0571), the OPEN-FP-F1-1 trajectory proposes the following hardened-theorem artifacts. Each is a separate `.tex` file under `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/hardened_theorems/` at its own gated Patch.

### §5.1 Under Route C — Hybrid sequence

| Artifact | Filename | Rigor | Status | Dependencies | Session budget |
|----------|----------|-------|--------|--------------|----------------|
| **A1** | `second_order_parallel_to_n_structural.tex` | Publication-grade Layer 3 unconditional | Sequence 1 — Route B argument | $I_h$ residual symmetry (Capotauro v2.0 Patch 0419 Finding C-W37); F.1 Theorem 6.1 (perturbation-locality at all orders) | 1–2 sessions |
| **A2** | `second_shell_inner_product_primitive.tex` | Publication-grade Layer 3 unconditional | G2 — analog of G1 hardening | Coxeter 600-cell second-shell geometry; orbit-stabilizer on $I_h$ | 1–2 sessions |
| **A3** | `host_second_shell_uniform_projection.tex` | Publication-grade Layer 3 conditional on G2 | G2.1 — analog of Patch 0552 | G2 (A2 above); orbit-stabilizer transitivity | 1–2 sessions |
| **A4** | `first_shell_second_shell_edge_orbits.tex` | Publication-grade Layer 3 conditional on G2 | G2.3 — five orbit classes derivation | A2 + A3 + $D_{3d}$ first-shell stabilizer | 1–2 sessions |
| **A5** | `second_shell_perpendicularity.tex` | Publication-grade Layer 3 conditional on G2 | G2.4 — analog of Patch 0551 | A2 + dodecahedron $I_h$ orbit structure | 1 session |
| **A6** | `o_delta_squared_path_class_weights.tex` | Sketch-document Layer 3 (framework-extension input from Q1 sub-option (A) or (B)) | Path-class weight formulas | Q1 sub-option choice + A1–A5 | 1–3 sessions |
| **A7** | `o_delta_squared_substrate_locality_umbrella.tex` | Sketch-document Layer 3 (parallel to Theorem 7.1) | $\mathcal{O}(\delta^2)$ umbrella result | A1 through A6 + PRED-O-30 (existing) | 1–2 sessions |

**Total artifact count:** 7 (one structural + six computational).
**Total session budget:** 7–14 sessions.
**Critical-path order:** A1 (independent) → A2 → A3 + A5 (parallel; both conditional on A2) → A4 (conditional on A2 + A3) → A6 (conditional on Q1 decision + A1–A5) → A7 (conditional on all preceding).

### §5.2 Under Route A — Single direct sequence (alternative)

If Route A is selected instead of Route C: drop artifact A1 (no symmetry-only structural theorem); merge A6 + A7 into a single artifact computing the closed-form coefficient directly. 6 artifacts total; same overall session budget but no intermediate structural-closure milestone.

### §5.3 Under Route B — Minimal sequence (alternative)

If Route B is selected instead of Route C: only artifact A1 is produced. 1 artifact total; OPEN-FP-F1-1 closes the structural sub-question only (not the coefficient sub-question). A future trajectory would re-open the coefficient work as a separate Open Problem (e.g., OPEN-FP-F1-7).

---

## §6 Pre-existing material to lean on

### §6.1 Within F.1 paper folder

- `dynamical_substrate_law.tex` v1.0 SHIPPED — §5 first-shell geometric identities; §6 perturbation-locality propagation; §7 substrate-locality umbrella. The $\mathcal{O}(\delta^2)$ work extends §5 + §6 to higher order; the assembly pattern at §7 is the model for the new umbrella artifact A7.
- `hardened_theorems/perturbation_locality_propagation.tex` (Patch 0550) — Theorem 6.1 hardened artifact. The locality propagation rule statement is order-independent; the artifact's structure (proof via three lemmas, five-class exclusion enumeration) is the template for new hardened artifacts at $\mathcal{O}(\delta^2)$.
- `hardened_theorems/first_shell_perpendicularity.tex` (Patch 0551) — Template for A5 (`second_shell_perpendicularity.tex`).
- `hardened_theorems/host_first_shell_uniform_projection.tex` (Patch 0552) — Template for A3 (`host_second_shell_uniform_projection.tex`).
- `hardened_theorems/first_shell_inner_product_primitive.tex` (Patch 0571) — Template for A2 (`second_shell_inner_product_primitive.tex`).
- `sketches/F1_phase2_foundations_work.md` — Reading C scoping + substrate-direction primitive setup; not directly $\mathcal{O}(\delta^2)$ content, but the conditional-closure framework and anti-priority discipline are inherited.
- `sketches/F1_subquestion_pcd_orientation_link.md` — Phase 2 closure work; the Reading C vertex-aligned framework that the second-shell extension inherits.
- `code/verify_phase1.py` — Numerical verification of first-shell identities at machine precision. The pattern extends naturally to second-shell identities; a new `code/verify_second_shell.py` could be authored at A2 + A3 + A5's completion.

### §6.2 In the SSCA arc (Capotauro v2.0 + Chirality Continuum)

- Capotauro v2.0 §3 spatial-sector substrate-locality theorem — shared identity with F.1 Theorem 5.1 (host-to-first-shell uniform projection $-1/(2\phi)$). Second-shell analog would have a parallel relationship to Capotauro v2.0's second-shell sector (if any; Capotauro v2.0's substrate-locality is restricted to the K3 base sector and may not engage second-shell explicitly).
- Capotauro v2.0 §5.6 K3-base protection identity — shared identity with F.1 Theorem 5.2 (first-shell-to-first-shell perpendicularity). Second-shell analog (artifact A5) may have a parallel relationship.
- Chirality Continuum METH-CHIR-CONT-3 — topological substrate quantity. Not directly $\mathcal{O}(\delta^2)$ machinery but the methodology of substrate-handle-via-topological-projection may inform the path-class weight derivation in A6.

### §6.3 At programme level

- `theorem-registry.md` THEO-DSL-1 + THEO-DSL-2 + THEO-DSL-3 entries — the second-order closure would introduce new entries THEO-DSL-4 (artifact A7's umbrella) + possibly THEO-DSL-5 (artifact A1's structural-only) + supporting publication-grade Layer 3 lemmas from A2–A5.
- `predictions.md` PRED-O-28 through PRED-O-32 — the second-order closure would introduce new PRED-O-N entries for $c_2$ (G2.1), $c_3$ (G2.2), the five orbit-class projection values (G2.3), and the closed-form $\mathcal{O}(\delta^2)$ coefficient $c_{\mathcal{O}(\delta^2)}$ (A7). Estimated 5–8 new PRED-O-N entries on closure.
- `frontier_sectors/FP.md` OPEN-FP-F1-1 — the parent Open Problem entry; on closure of artifact A7, the entry transitions OPEN → RESOLVED (or to a derivative status if the closure is partial per Route B).

---

## §7 Decision-gate items requiring Thomas input

The OPEN-FP-F1-1 trajectory has substantive direction decisions that should be made deliberately rather than defaulted. The following are flagged as decision-gate items (DG-N) requiring Thomas's input before the first closure Patch.

### DG-1 — Framework-extension question (Q1 from §3.1)

**Question:** Does MA.2's framework-local current construction extend to $\mathcal{O}(\delta^2)$ naturally via the underlying path-integral structure (sub-option A), via a new framework axiom MA.3 (sub-option B), or via Layer 4 derivation prerequisite from CPP A1–A11 (sub-option C, coupling to OPEN-FP-F1-2)?

**Recommendation:** Sub-option (A) at sketch level; revisit if sub-option (A)'s derivation cannot be made publication-grade Layer 3 without additional framework input.

**Stakes:** Determines the framework-extension status of F.1's Mechanism A; sub-options (B) and (C) substantially escalate the framework-axiomatic commitment.

### DG-2 — Closure-route selection (§4)

**Question:** Which closure route does the trajectory execute under — Route A (direct derivation), Route B (symmetry-only), or Route C (hybrid)?

**Recommendation:** Route C (hybrid) per §4.4 — yields rigorous structural result in 1–2 sessions, then pursues coefficient computation in parallel.

**Stakes:** Determines the artifact sequence count (1 vs 6 vs 7), session budget (1–2 vs 5–10 vs 7–14), and intermediate-milestone visibility.

### DG-3 — Calibration anchor for the trajectory

**Question:** Does the OPEN-FP-F1-1 trajectory anchor calibration on (i) the F.1 v1.0 SHIP's "sketch-document Layer 3 framework preprint" language for the umbrella + publication-grade Layer 3 for the building blocks; or (ii) push for unconditional publication-grade Layer 3 umbrella at second order (which would require pushing through the framework-extension question DG-1 at publication-grade level)?

**Recommendation:** Option (i) — preserve F.1's calibration pattern. The umbrella theorem at $\mathcal{O}(\delta^2)$ remains sketch-document Layer 3 per the F.1 v1.0 SHIP pattern; the building blocks (artifacts A1–A5) reach publication-grade Layer 3.

**Stakes:** Determines whether the OPEN-FP-F1-1 closure satisfies "publication-grade Layer 3 umbrella" or "sketch-document Layer 3 umbrella with publication-grade building blocks."

### DG-4 — Trajectory ordering relative to OPEN-FP-F1-2

**Question:** Does OPEN-FP-F1-1 (this trajectory) execute first, before OPEN-FP-F1-2 (Layer 4 axiomatic derivation of Mechanism A)? Or are they interleaved? Or does OPEN-FP-F1-2 execute first?

**Recommendation:** OPEN-FP-F1-1 first per the trade-off in §1.1 — closure-trajectory machinery exists, second-shell geometry is well-characterised, intermediate closure milestones are visible (Route C). OPEN-FP-F1-2 is deeper but later.

**Stakes:** OPEN-FP-F1-1 first establishes a higher-order extension of Theorem 7.1 first; OPEN-FP-F1-2 first establishes Layer 4 axiomatic status for Mechanism A first.

### DG-5 — Artifact A7's name and umbrella-theorem identity

**Question:** Is the $\mathcal{O}(\delta^2)$ umbrella theorem THEO-DSL-4 (a new entry in the theorem registry)? Or an extension of THEO-DSL-3 (an in-place strengthening of the existing entry)?

**Recommendation:** THEO-DSL-4 — new entry. Preserves THEO-DSL-3's status as the $\mathcal{O}(\delta^1)$ umbrella at sketch-document Layer 3; THEO-DSL-4 is the $\mathcal{O}(\delta^2)$ extension at the same rigor level. This mirrors the convention for cross-paper extensions in the corpus.

**Stakes:** Affects how the closure integrates with F.1's existing theorem chain; THEO-DSL-3 vs THEO-DSL-4 distinction also affects how the H4 finding's legacy-alias convention extends (whether OPEN-FP-F1-1's closure produces a new THEO entry or modifies an existing one).

---

## §8 Risk register

### Risk R1 — Q1 framework-extension turns out to require MA.3 or worse

If MA.2's path-integral extension (sub-option A) cannot be made publication-grade Layer 3 without additional framework input, the trajectory's framework-axiomatic commitment escalates. Mitigation: pursue Route B (symmetry-only) in parallel; Route B doesn't depend on Q1 sub-option choice and provides a structural result independent of framework-extension status.

### Risk R2 — G2.3 first-shell-to-second-shell edge structure too complex

If the 60 first-shell-to-second-shell edges decompose into more than 5 orbit classes under the relevant stabilizer, or if the per-class projection values are not closed-form golden-ratio rationals, the closed-form $\mathcal{O}(\delta^2)$ coefficient becomes computationally intractable. Mitigation: Route B (symmetry-only) closes the structural sub-question regardless; the coefficient sub-question can be deferred or pursued numerically.

### Risk R3 — Second-shell perpendicularity (G2.4) fails

If the dodecahedron's edges are NOT perpendicular to $\hat{n}$ (the analog of F.1 Theorem 5.2 may not hold at second shell), the closed-form $\mathcal{O}(\delta^2)$ expression becomes more complex. Mitigation: this is exactly the kind of result the geometric derivation needs to discover; the trajectory's value is in determining whether the cross-shell structural pattern survives or breaks. Either outcome is informative.

### Risk R4 — Trajectory budget overrun (>14 sessions)

If session budget overruns the 7–14 estimate significantly, the OPEN-FP-F1-1 trajectory could starve other programme priorities. Mitigation: Route C's intermediate-milestone visibility (artifact A1 at end of session 1–2) provides early-progress signal; trajectory can be paused at any post-A1 point with structural result preserved.

### Risk R5 — Coupling to OPEN-FP-F1-2 via Q1 sub-option (C)

If Q1 sub-option (C) turns out to be required, OPEN-FP-F1-1 and OPEN-FP-F1-2 couple, contradicting their FP.md-registered independence ("mutually orthogonal at first order"). Mitigation: register the coupling discovery openly per symmetric-honesty discipline; either escalate scope to joint OPEN-FP-F1-{1,2} trajectory or close OPEN-FP-F1-1 at Route B (structural-only) preserving its independence.

### Risk R6 — Anti-erasure discipline drift across trajectory's session budget

The F.1 v1.0 SHIP cycle's anti-erasure discipline (codified at `programme_orientation.md` Chapter 22i + F.1 §10 + ChatGPT R2–R6 reviewer pressure) requires preserving Layer distinctions and conditionality clauses through revisions. Across a 7–14 session trajectory, drift risk is non-trivial. Mitigation: anti-priority 1 of §0.2 + the reviewer-pause cycle precondition (per `templates/paper_completion_checklist.md` §"Reviewer-Pause Cycle Precondition") + checkpoint Patches at end of each artifact's closure.

---

## §9 Session-close discipline + forward queue

### §9.1 What this Patch (0571i) achieved

- Opened the OPEN-FP-F1-1 trajectory with substantive content scope.
- Enumerated three structural questions (Q1 framework-extension + Q2 second-shell identities + Q3 path-class structure) requiring closure work.
- Articulated three candidate closure routes (A direct + B symmetry-only + C hybrid) with explicit trade-offs.
- Proposed a 7-artifact hardened-theorem sequence under Route C parallel to the O(δ¹) four-artifact pattern.
- Registered 5 decision-gate items (DG-1 through DG-5) requiring Thomas input before substantive closure work begins.
- Registered 6 risks (R1 through R6) with mitigation strategies.

### §9.2 What this Patch did NOT achieve (and isn't supposed to)

- No closure work executed.
- No framework-extension commitment made.
- No closure route selected — Route C recommended but pending Thomas DG-2 confirmation.
- No new theorem registry entries, predictions, or programme-level registrations.
- No modifications to v1.0 SHIPPED F.1 paper or hardened-theorem artifacts.

### §9.3 Forward queue

**Next action (post-Patch-0585):** Substantive closure work continues at Route C sequence 2 artifact A2 (`second_shell_inner_product_primitive.tex` — G2 publication-grade Layer 3 hardening). Per the §5.1 critical-path order, A2 is independent and unlocks A3 + A5 in parallel (both conditional on A2), with A4 conditional on both A2 + A3; A6 (path-class weight enumeration) depends on the framework-extension hypothesis (H5) at sketch-document Layer 3 per DG-1 sub-option (A) plus A1 through A5. The final umbrella result A7 ($\mathcal{O}(\delta^2)$ substrate-locality umbrella) depends on all preceding artifacts and registers as the THEO-DSL-5 candidate (the closed-form $\alpha_2$). Estimated 4–8 sessions for Route C sequence 2.

**Original next action (now superseded by §9.5 Patch 0585 landing):** Thomas review of decision-gate items DG-1 through DG-5. *Bundle accepted as-is at Session 145 open; substantive closure executed at Patch 0585.*

**If Route B selected at DG-2 (alternative path; NOT taken):** the trajectory would have closed after artifact A1; coefficient work would re-open as a new Open Problem. (DG-2 Route C selected at Session 145 open; Route C sequence 2 trajectory remains active.)

**If Route A selected at DG-2 (alternative path; NOT taken):** the trajectory would have skipped A1 and proceeded to A2 directly. (DG-2 Route C selected; A1 landed at Patch 0585; A2 is the natural next sequence-2 artifact under Route C.)

### §9.4 Cross-references for downstream Patches

- This scoping document: `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/F1_o_delta_squared_extension_scoping.md`.
- Parent Open Problem: `frontier_sectors/FP.md` OPEN-FP-F1-1 entry.
- $\mathcal{O}(\delta^1)$ closure paper: `dynamical_substrate_law.tex` v1.0 SHIPPED.
- $\mathcal{O}(\delta^1)$ hardened artifacts: `hardened_theorems/{perturbation_locality_propagation,first_shell_perpendicularity,host_first_shell_uniform_projection,first_shell_inner_product_primitive}.tex`.
- Capotauro v2.0 cross-references: `series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex` §3 spatial-sector substrate-locality + §5.6 K3-base protection.
- Decision-gate discipline reference: `templates/operating_system.md` §17 reviewer-pause cycle + §15 SHIP-trigger protocol (for the eventual OPEN-FP-F1-1 closure if it triggers a v1.1 / v2.0 micro-revision of F.1).

### §9.5 Patch landings

- **Patch 0585** (Session 145, 26 May 2026): **artifact A1 LANDED**. `hardened_theorems/second_order_parallel_to_n_structural.tex` (334 lines LaTeX; 9-page PDF; zero substantive warnings clean three-pass compile). Closes the **structural sub-question** of OPEN-FP-F1-1 at publication-grade Layer 3 unconditional via the symmetry-only Route C sequence 1 argument articulated in §4.2: Lemma 1 (order-by-order $I_h$-invariance of $\vec{j}_k(v_{\text{host}})$ via $I_h$-equivariance of Mechanism A's rate function under stabilization of $\hat{n}$) + Lemma 2 ($I_h$-invariant vectors in $\mathbb{R}^4$ at $v_{\text{host}}$ are spanned by $\hat{n}$, via the central inversion $\iota \in I_h$ acting as $\text{diag}(1,-1,-1,-1)$). All-orders strengthening obtained as a structural bonus: $\vec{j}_k(v_{\text{host}}) \parallel \hat{n}$ holds at every $k \geq 1$, not only at $k = 2$. Decision-gate bundle accepted as-is at Session 145 open: DG-1 sub-option (A) path-integral structure extension + DG-2 Route C Hybrid + DG-3 preserve F.1 v1.0 SHIP calibration + DG-4 OPEN-FP-F1-1 first + DG-5 new THEO-DSL-4 entry. The hardened artifact's five exclusion classes E1–E5 register what is NOT closed; E1 (the coefficient $\alpha_2$ at $\mathcal{O}(\delta^2)$) is the load-bearing remaining open question and the target of Route C sequence 2 artifacts A2–A6.

- **Patch 0585a** (Session 145, 26 May 2026): registry propagation for Patch 0585. `frontier_sectors/FP.md` OPEN-FP-F1-1 entry updated to register partial closure (structural sub-question CLOSED; coefficient sub-question OPEN); header bold tail extended with Patch 0585 announcement. `theorem-registry.md` updated with new THEO-DSL-4 row in SD section ($\mathcal{O}(\delta^k)$ substrate-current parallel-to-$\hat{n}$ structural theorem at all orders $k \geq 1$; publication-grade Layer 3 unconditional; no G1 dependency); SD section header advanced 18 → 19; Summary Statistics SD row 18 → 19, Total 70 → 71. This scoping document updated with §9.5 patch landings record and §9.3 forward-queue revision reflecting the Route C sequence 2 trajectory continuation.

**Route C sequence 1 status:** **CLOSED at Patch 0585**. The sequence-1 trajectory (the symmetry-only structural theorem) was a 1-Patch closure, matching the §4.4 + §5.1 estimate of 1–2 sessions. Sequence-1 artifact count = 1 (artifact A1 only).

**Route C sequence 2 status:** **OPEN; 5 artifacts to land** (A2 through A6). Sequence-2 closure produces a future THEO-DSL-5 candidate (closed-form $\alpha_2$ at $\mathcal{O}(\delta^2)$) at artifact A7 ($\mathcal{O}(\delta^2)$ substrate-locality umbrella). Estimated 4–8 sessions for sequence-2 closure.

---

— Scoping document opened at Patch 0571i (26 May 2026); discipline references `templates/operating_system.md` §15.10 + `templates/paper_completion_checklist.md` §H + `templates/relationship_protocol.md` §2.6 (symmetric-honesty for closure-route trade-off framing); template precedents `sketches/F1_layer3_promotion_scoping.md` + `sketches/F1_phase2_foundations_work.md`.
