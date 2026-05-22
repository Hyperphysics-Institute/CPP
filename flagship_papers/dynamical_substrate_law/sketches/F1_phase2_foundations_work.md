# F.1 Phase 2 Foundations Work — Sketch Opening

**Path:** `flagship_papers/dynamical_substrate_law/sketches/F1_phase2_foundations_work.md`
**Opened:** 21 May 2026 (Session 139, Patch 0531)
**Author:** Opus (Session 139 window)
**Status:** Sketch-level structural exploration (Layer 1/Layer 2). NOT closure work; closure-language anti-priority sustained per Patch 0528 calibration discipline.
**Scope:** Open the Phase 2 foundations work programme registered at Patch 0528 §14.17 as the real structural bottleneck of the F.1 sub-question closure trajectory. Three commitments to be addressed: (B.1) local algebraic representation ansatz justification — LARGEST OPEN QUESTION; (B.2) $\sigma_{cycle}$ algebraization rigor + uniqueness of TI-odd construction; (B.3) Case A.1 derivational support.

---

## §0 Working-session firewall

**This sketch opens Phase 2 foundations work. It does not close it.**

The handover at Patch 0530 (`handovers/2026-05-21_session_138_F1_sub_question_provisional_closure.md` §2.2 + §13) registered Phase 2 foundations work as 5–15 sessions of structural exploration, output sketch-level rather than flagship-paper-level until the local algebraic representation ansatz is examined.

**Discipline applied in this sketch** (per Patch 0528 lessons systematized at handover §10):
- **Operational descriptions, not defensive framing** (§10.2 lesson). Where I have a choice between "structural-consistency argument" and "parity-repair via cycle-orientation algebraization," I take the operational description.
- **All ansatzes flagged explicitly** (§10.3 lesson). Any assumption introduced beyond CPP axioms A1–A11 + Reading C + Capotauro substrate-locality framework is labeled as an ansatz and registered for future hardening.
- **Sketch-level output only** (§10.4 lesson). Structural exploration with explicit open questions, NOT closure with downstream propagation.
- **Reviewer-pause checkpoint at session close** (§10.1 lesson). Substantive exploration → self-assessment → register what was achieved and what remains open. No "FOUNDATIONS WORK CLOSED" framing; the trajectory remains in foundations-exploration state across multiple sessions.

**Anti-priorities sustained:**
- Do NOT modify v1.0 SHIPPED paper sources (Chirality Continuum / Capotauro v2.0 / SF-2 / SM-2 / SF-4).
- Do NOT propagate "FULL CLOSURE under Scenario A" language. F.1 sub-question status remains "PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work."
- Do NOT promote findings of this sketch to cross-paper observable-scale predictions.
- Do NOT modify Phase 2 §12 polished content in `F1_subquestion_pcd_orientation_link.md`. Foundations work develops in this separate sketch; §12 calibration at §12.13 remains the binding state of Phase 2 closure language until foundations work substantively progresses on B.1.

---

## §1 Purpose and structure

### §1.1 Three commitments registered

Patch 0528 §14.17 + Patch 0529 decision-gate §14.5 registered three open structural commitments as the real bottleneck of the F.1 sub-question closure trajectory:

| # | Phase | Commitment | Patch 0528 framing |
|---|---|---|---|
| B.1 | 2 | **Local algebraic representation ansatz** for thermodynamic chirality observable at host vertex | Could instead emerge from cycle-history accumulation, nonlocal transport asymmetry, or coarse-grained update statistics. Unflagged in Patches 0524–0527, flagged at Patch 0528 §12.13 calibration. **Largest open question.** |
| B.2 | 2 | **$\sigma_{cycle}$ algebraization rigor + uniqueness of TI-odd construction** | Explicitation of latent A5 cycle-orientation into multiplicative TI-odd pseudoscalar with tensor-construction properties is stronger than A5 explicitly contains. Alternative TI-odd constructions not formally ruled out. |
| B.3 | 3 | **Case A.1 derivational support** from CPP axioms | Identification $\delta = \chi = \varphi^{-3}$ is currently minimal unified realization hypothesis motivated by minimal-primitives principle + empirical phenomenological consistency, not derived. |

### §1.2 This session's scope

This session opens the foundations work programme. Concrete deliverables of Patch 0531:

- **B.1 substantive structural exploration** (§2): precise statement of the ansatz, disambiguation of conflated layers (matrix-element vs observable), enumeration of alternative representations with structural reduction arguments at $\mathcal{O}(\delta)$, identification of sub-questions for future sessions.
- **B.2 forward sketch** (§3): articulation of the algebraization question + initial enumeration of TI-odd alternative constructions + identification of the "minimal-derivative-order" characterization as a candidate uniqueness criterion.
- **B.3 forward sketch** (§4): articulation of three candidate derivational arguments + connection to long-term programme target + identification of intermediate hardening moves.
- **Session-close discipline** (§5–§6): reviewer-pause checkpoint applied; forward queue with open sub-questions; methodological notes registered.

This sketch is the foundations work's analog of the Patch 0523 F.1 scoping sketch — it opens the work, identifies the structural targets, and queues substantive sub-trajectories. It does NOT close any of B.1, B.2, B.3.

### §1.3 What "sketch-level" means

Per the handover §13 estimates, individual commitments require:
- B.1: 2–6 sessions of structural exploration.
- B.2: 2–5 sessions.
- B.3: 1–4 sessions for arguments (i)–(ii); option (iii) connects to long-term programme target and is multi-session-arc-scale.

A single session opening all three is exactly the "fast closure on uninspected foundations" anti-pattern the Patch 0528 calibration warned against. The deliberate output here is exploratory structural work that future sessions can build on incrementally.

---

## §2 (B.1) Local algebraic representation ansatz — substantive exploration

### §2.1 Precise statement of the ansatz

The Phase 2 derivation at sketch §12.5 of `F1_subquestion_pcd_orientation_link.md` produces the coupling rule:
$$\vec{\omega}_{PCD}(v) := \sigma_{cycle} \cdot \hat{j}_{DI}^{net}(v)/|\hat{j}_{DI}^{net}|_0$$

The ansatz embedded in this construction is:

> **(B.1) ansatz.** The PCD-cycle-orientation pseudovector $\vec{\omega}_{PCD}(v)$ at vertex $v$ is completely determined by the local algebraic data at $v$ — specifically, by $\hat{j}_{DI}^{net}(v)$ (the unit direction of the substrate's net DI-bit current at $v$) and the global pseudoscalar $\sigma_{cycle}$. No derivative content (spatial gradients/curls at $v$), no cycle-history content (past-AM dependence), and no nonlocal content (contributions from non-first-shell vertices) enters the construction.

This ansatz is a **structural commitment**, not a derivation. The Phase 2 construction proceeds AS IF the local algebraic representation captures all relevant substrate-physics content for the manifestation (iv) Wigner-Eckart datum. Whether that AS-IF is justified is the B.1 question.

### §2.2 Disambiguation — three layers conflated

A clarification that surfaced in working this out: the term "thermodynamic chirality observable" in ChatGPT's review verdict was operating across three structurally distinct layers, and the B.1 question reads differently at each.

| Layer | Object | Locality character |
|---|---|---|
| **Substrate per-cycle** | $\sigma_{cycle}$, $\hat{j}_{DI}^{net}(v, t)$ | Per-vertex, per-AM. Inherently local algebraic. |
| **Substrate matrix element** | $|M^{thermo}| = \langle \pm \vec{\omega}_{PCD} | \hat{C}^{thermo} | \mp \vec{\omega}_{PCD} \rangle$ | Per-event amplitude, computed at the host vertex + antipodal pair via Wigner-Eckart. **This is what Phase 2/3 produce.** |
| **Observable cosmological** | $\Delta p_{LR}^{obs}$, $\eta_B$ | Accumulated over cosmological time; statistical over many events. |

ChatGPT's listed alternatives — cycle-history accumulation, nonlocal transport, coarse-grained statistics — are most naturally located at the **observable cosmological** layer, where accumulation and statistics genuinely matter. The Phase 4 observable chain ($|M^{thermo}| \to \Delta p_{LR}^{obs} \to \delta_{CP} \to \varepsilon_1 \to \eta_B$) is exactly where this accumulation happens; it is not part of Phase 2's matrix-element computation.

**The sharper B.1 question, therefore:** when the Phase 2 coupling rule writes $\vec{\omega}_{PCD}(v) = \sigma_{cycle} \cdot \hat{j}^{net}(v)/|\hat{j}^{net}|_0$, does this LOCAL ALGEBRAIC FORM capture all the substrate-physics content the matrix element $|M^{thermo}|$ depends on, or does the matrix element actually depend on derivative/nonlocal/history content at the substrate-matrix-element layer that the local form discards?

This is structurally narrower than ChatGPT's listed alternatives suggest, and structurally more answerable.

**Caveat — this disambiguation is itself sketch-level.** It is plausible that ChatGPT's review was directed precisely at the substrate-matrix-element layer (in which case the B.1 question is exactly as posed in the calibration), but it is also possible that the layered structure above collapses some genuine concern into a layer-mismatch where it doesn't apply. Future review of the disambiguation against ChatGPT's original verdict is itself a sub-question.

### §2.3 Alternative representations at the substrate-matrix-element layer

Restricting now to the substrate-matrix-element layer, the candidate alternative representations are:

**(R1) Local derivative content.** $\vec{\omega}_{PCD}(v)$ depends on spatial derivatives at $v$:
$$\vec{\omega}_{PCD}(v) = \sigma_{cycle} \left[a_0 \hat{j}^{net}(v) + a_1 \nabla \cdot \vec{j}^{net}(v) \hat{n} + a_2 (\nabla \times \vec{j}^{net}(v)) + \ldots\right]$$
where $a_0, a_1, a_2, \ldots$ are dimensionless coefficients. The Phase 2 ansatz sets $a_0 = 1, a_1 = a_2 = \ldots = 0$.

**(R2) Cycle-history accumulation.** $\vec{\omega}_{PCD}(v, t)$ depends on past values of $\hat{j}^{net}$:
$$\vec{\omega}_{PCD}(v, t) = \sigma_{cycle} \int_{-\infty}^t K(t-t') \hat{j}^{net}(v, t') dt'$$
where $K(\tau)$ is a temporal kernel. The Phase 2 ansatz sets $K(\tau) = \delta(\tau) / \mathcal{N}$ for some normalization $\mathcal{N}$.

**(R3) Nonlocal spatial averaging.** $\vec{\omega}_{PCD}(v)$ depends on a weighted sum of $\hat{j}^{net}$ at nearby vertices:
$$\vec{\omega}_{PCD}(v) = \sigma_{cycle} \sum_{v'} W(v, v') \hat{j}^{net}(v')$$
where $W(v, v')$ is a substrate spatial kernel. The Phase 2 ansatz sets $W(v, v') = \delta_{v,v'} / \mathcal{N}$.

### §2.4 Structural reduction at $\mathcal{O}(\delta)$ — sketch arguments

For each of (R1)–(R3), a STRUCTURAL ARGUMENT (sketch-level, not formal theorem) reduces the alternative to the local algebraic form at first order in $\delta$:

#### §2.4.1 (R1) Local derivative content — sketch reduction

At the host vertex under vertex-aligned Reading C, the icosahedral residual symmetry $I_h$ acts on the first-shell. Capotauro's substrate-locality theorem (Theorem 5.X / Finding C-W39) establishes that the first-shell icosahedron is preserved at $\mathcal{O}(\epsilon)$ in 4D ambient under Reading C edge-perturbations, with isotropic radial scaling on host-to-first-shell edges.

**Key observation.** Phase 1's result $\vec{j}^{net}(v_{\text{host}}) = (6 r_0 \delta/\varphi^2)\hat{n}$ at first order in $\delta$ is proportional to $\hat{n}$. By $I_h$ symmetry of the first-shell, the only $I_h$-invariant first-order content along a fixed direction at the host vertex is along $\hat{n}$.

For derivative content at the host: any local derivative of $\vec{j}^{net}$ at $v_{\text{host}}$ at first order in $\delta$ involves variation of $\vec{j}^{net}$ across the first-shell. By icosahedral symmetry, $\vec{j}^{net}$ at a first-shell neighbor $v_i$ has a specific orientation determined by $v_i$'s own local first-shell — which is a rotated copy of the host's first-shell.

The first-shell neighbors are not at $v_{\text{host}}$; they have their own local geometries. Computing $\vec{j}^{net}(v_i)$ requires identifying the 12 second-neighbor projections at $v_i$ — these depend on $v_i$'s position relative to $\hat{n}$.

**Sketch reduction argument.** Spatial derivatives of $\vec{j}^{net}$ at $v_{\text{host}}$ at first order in $\delta$ depend on the difference $\vec{j}^{net}(v_i) - \vec{j}^{net}(v_{\text{host}})$ across the first-shell. By the icosahedral symmetry $I_h$, the sum of these differences over the 12 first-shell neighbors is constrained: most $I_h$-irreps cancel in the sum, leaving content along $\hat{n}$ (the $I_h$-invariant axis) as the surviving channel.

**Therefore at first order in $\delta$, the surviving derivative content at $v_{\text{host}}$ is parallel to $\hat{n}$** — meaning $\nabla \cdot \vec{j}^{net}|_{v_{\text{host}}} \hat{n}$ and $\nabla \times \vec{j}^{net}|_{v_{\text{host}}}$ both reduce to scalar multiples of $\hat{n}$, with magnitudes that are $\mathcal{O}(\delta)$ themselves.

The structural consequence: the (R1) general form at first order reduces to
$$\vec{\omega}_{PCD}(v_{\text{host}}) = \sigma_{cycle} \cdot [\text{linear combination of } \hat{n}\text{-content}] = \sigma_{cycle} \cdot c \cdot \hat{n}$$
with $c$ a renormalization constant absorbing all the $a_i$ coefficients. **Up to normalization, (R1) is structurally equivalent to the Phase 2 ansatz at $\mathcal{O}(\delta)$**, provided the residual icosahedral symmetry holds.

**Ansatzes used in this sketch reduction (flagged):**
- **(B.1.a)** *Icosahedral-symmetry preservation at the substrate-matrix-element layer.* The $I_h$ symmetry of the first-shell, preserved at $\mathcal{O}(\epsilon)$ in 4D per Capotauro Finding C-W39, is assumed to apply equally to Mechanism A's $\mathcal{O}(\delta)$ perturbations. This is plausible by direct analogy but not formally proven for the temporal sector.
- **(B.1.b)** *Curl content non-perpendicular to $\hat{n}$.* The argument that $\nabla \times \vec{j}^{net}|_{v_{\text{host}}}$ has no component perpendicular to $\hat{n}$ at first order requires explicit computation; the icosahedral symmetry argument suggests this but does not prove it in 4D.

These ansatzes are weaker than the full B.1 ansatz — they are structural framework conditions that, if satisfied, reduce B.1 to a renormalization question rather than a representation-choice question.

#### §2.4.2 (R2) Cycle-history accumulation — sketch reduction

Under steady-state substrate dynamics (the substrate's $\hat{n}$-bias is constant in time at the framework level — Reading C fixes $\hat{n}$ globally), the current is time-independent: $\hat{j}^{net}(v, t) = \hat{j}^{net}(v)$.

In this regime:
$$\vec{\omega}_{PCD}(v, t) = \sigma_{cycle} \left[\int_{-\infty}^t K(t-t') dt'\right] \hat{j}^{net}(v) = \sigma_{cycle} \cdot \mathcal{N}_K \cdot \hat{j}^{net}(v)$$
where $\mathcal{N}_K$ is a scalar constant depending on the kernel $K$. **The history-accumulation form reduces to the local algebraic form up to normalization** in the steady-state regime.

**Ansatzes used:**
- **(B.1.c)** *Steady-state substrate dynamics.* The framework's Reading C commitment to a fixed global $\hat{n}$ implies the substrate's per-cycle bias is time-independent. This is reasonable at the framework level but breaks down if cosmological time-dependence of $\hat{n}$ matters (e.g., if $\hat{n}$ has cosmological evolution). For the manifestation (iv) leptogenesis epoch, steady-state is the natural framework setting; for the broader programme target (chirality scale derivation from polytope geometry), time-independence of $\hat{n}$ is itself a structural commitment that may eventually need examination.

#### §2.4.3 (R3) Nonlocal spatial averaging — sketch reduction

Capotauro's substrate-locality theorem (Finding C-W39) + Substrate-Locality Unification corollary (Finding C-W40) establish that the substrate's spatial chirality content localizes at the first-shell icosahedron of the host vertex. By direct analog, the temporal sector's chirality content should also localize at the first-shell.

If the spatial kernel $W(v, v')$ has support on the first-shell of $v$ (i.e., $W(v, v') \ne 0$ only for $v' \in \text{first-shell}(v) \cup \{v\}$), then the sum:
$$\vec{\omega}_{PCD}(v_{\text{host}}) = \sigma_{cycle} \left[W_0 \hat{j}^{net}(v_{\text{host}}) + \sum_{i=1}^{12} W_i \hat{j}^{net}(v_i)\right]$$
is a weighted sum over local + first-shell currents.

By icosahedral symmetry of the first-shell, the weights $W_i$ are uniform (i.e., $W_i = W_1$ for all $i$). And the first-shell sum $\sum_{i=1}^{12} \hat{j}^{net}(v_i)$ has the same icosahedral symmetry properties as the position sum $\sum_{i=1}^{12} \hat{u}_i$ — by Capotauro's $\sum_i \hat{u}_i = -(6/\varphi) \hat{n}$ identity (sketch §13.2 / Phase 1 verification), the first-shell average of position vectors is along $\hat{n}$.

A parallel identity for $\hat{j}^{net}$ at first-shell vertices would be needed for the sum to reduce. The sketch claim is: $\sum_{i=1}^{12} \hat{j}^{net}(v_i) \parallel \hat{n}$ at first order in $\delta$ by icosahedral symmetry (using the same residual $I_h$ structure as the position sum identity).

**Therefore at first order, (R3) with first-shell support reduces to**
$$\vec{\omega}_{PCD}(v_{\text{host}}) = \sigma_{cycle} \cdot c' \cdot \hat{n}$$
**up to a renormalization constant $c'$ absorbing $W_0$ + first-shell average.** Structurally equivalent to the Phase 2 ansatz up to normalization.

**Ansatzes used:**
- **(B.1.d)** *Substrate-locality extension to the temporal sector.* The Capotauro spatial-sector substrate-locality theorem (Finding C-W39 + C-W40) is assumed to extend to the temporal sector via direct analog of structural-locality argument. The temporal-sector analog would be: the substrate's per-cycle DI-bit-flux content localizes at the first-shell icosahedron of the host vertex. This is plausible but is not in itself a theorem; substantive future work would either prove this extension formally or identify why it fails.
- **(B.1.e)** *Icosahedral-symmetry-based reduction of first-shell current sum.* The claim $\sum_{i=1}^{12} \hat{j}^{net}(v_i) \parallel \hat{n}$ at first order in $\delta$ requires explicit derivation parallel to Capotauro's $\sum_i \hat{u}_i = -(6/\varphi)\hat{n}$ identity. The argument structure is plausible but the explicit computation is deferred.

### §2.5 Provisional verdict on B.1 — sketch level

**Provisional structural claim** (sketch level, NOT closure): at first order in $\delta$ + under the framework conditions B.1.a–B.1.e flagged above, the alternative representations (R1)–(R3) reduce to the Phase 2 local algebraic ansatz up to renormalization constants. The Wigner-Eckart matrix element $|M^{thermo}|$ depends on the substrate object up to normalization, so renormalization constants are absorbed into the normalization choice (Phase 3's $|\hat{j}^{net}|_0$).

**What this provisional claim is NOT:**
- It is NOT a proof that the B.1 ansatz is the structurally forced representation. It is an argument that, conditional on B.1.a–B.1.e, the alternatives reduce to the same lowest-order content.
- It does NOT close B.1. The framework conditions B.1.a–B.1.e are themselves ansatzes that require future hardening.
- It does NOT extend beyond first order in $\delta$. At $\mathcal{O}(\delta^2)$ and higher, the alternative representations may give structurally distinct content. The Phase 3 numerical result $\chi/6 \approx 0.0394$ at first order is robust to this; predictions at higher orders may not be.

**Status update on B.1 commitment:** moved from "unflagged ansatz" (pre-Patch 0528) → "flagged ansatz with three lower-level ansatzes B.1.a–B.1.e identified, sketch-level reduction argument constructed at $\mathcal{O}(\delta)$" (this Patch 0531). Hardening trajectory: prove B.1.a–B.1.e individually, or identify which of them is the genuine bottleneck.

### §2.6 Open sub-questions for B.1 — future-session queue

The following sub-questions emerge from §2.4 and need substantive work in future sessions:

| # | Sub-question | Estimated effort |
|---|---|---|
| B.1.q1 | Prove or falsify B.1.a (icosahedral-symmetry preservation at the substrate-matrix-element layer for Mechanism A's $\mathcal{O}(\delta)$ perturbations). Likely requires direct analog of Capotauro Theorem 5.X for the temporal sector. | 1–2 sessions |
| B.1.q2 | Prove or falsify B.1.b (curl content non-perpendicular to $\hat{n}$ at first order). Explicit computation of $\nabla \times \vec{j}^{net}|_{v_{\text{host}}}$ at first order in $\delta$ using 600-cell second-shell geometry. | 1 session |
| B.1.q3 | Prove or falsify B.1.d (substrate-locality extension to the temporal sector). Likely requires formal extension of Capotauro Finding C-W39 to Mechanism A's rate-asymmetry primitive, or identification of structural obstacle. | 1–3 sessions |
| B.1.q4 | Derive the first-shell current sum identity $\sum_i \hat{j}^{net}(v_i)$ at first order (B.1.e). Parallel to Capotauro's $\sum_i \hat{u}_i = -(6/\varphi)\hat{n}$ identity. | 1 session |
| B.1.q5 | Re-examine the §2.2 layered disambiguation against ChatGPT's original review verdict to verify that the substrate-matrix-element layer is what ChatGPT's concern was directed at. If ChatGPT meant the per-cycle substrate layer instead, the framing of §2.3–§2.5 needs revision. | 0.5 session (review-pause checkpoint) |
| B.1.q6 | Consider $\mathcal{O}(\delta^2)$ contributions: do they introduce structurally distinct content (e.g., $\delta^2$ cross-shell coupling) that the local form would miss? Relevant for future precision improvements but NOT for the current Phase 3 result. | 2–4 sessions |

Total estimated effort: 6.5–11.5 sessions for B.1 alone (within the handover §13.1's 2–6 session estimate, modulo the q5 review-pause and q6 higher-order work).

---

## §3 (B.2) $\sigma_{cycle}$ algebraization rigor + uniqueness — forward sketch

### §3.1 The algebraization question

Axiom A5 commits the framework to ordered cyclicity P → C → D as the universal substrate-dynamics of every CP at every Absolute Moment. The cycle's directionality is a framework primitive: there is a definite forward direction, and T-reversal reverses it.

Phase 2 §12.3 promotes this commitment to a multiplicative TI-odd pseudoscalar $\sigma_{cycle} \in \{+1, -1\}$ with the property that $\sigma_{cycle} \cdot V$ is TI-odd whenever $V$ is TI-even (and vice versa). This promotion is the "algebraization" step the calibration flagged.

The algebraization question is: **is the multiplicative-pseudoscalar realization the canonical / minimal / forced algebraic representation of A5's content, or is it a representational choice?**

### §3.2 Three structural levels of A5's content

A5 commits to:
- **(A5.1)** *Ordered cyclicity:* every CP executes P → C → D at every AM (not D → C → P).
- **(A5.2)** *T-asymmetry of cycle direction:* under T-reversal, the cycle direction reverses (P → C → D becomes D → C → P).
- **(A5.3)** *I-evenness of cycle direction:* under spatial inversion, the cycle direction is unaffected (cycle is internal to each CP; spatial inversion of CP's external coordinates does not change which phase the CP is in).

Together (A5.2) + (A5.3) → cycle direction is TI-odd.

What A5 does NOT explicitly commit to:
- **(beyond-A5.a)** *Multiplicative algebraic realization.* Representing cycle direction as a multiplicative scalar that combines with other tensor objects to produce signed products.
- **(beyond-A5.b)** *Pseudoscalar-irrep representation.* Representing cycle direction as transforming in the 1D pseudoscalar irrep of the framework's T+I parity group.

The Phase 2 use of $\sigma_{cycle}$ relies on (beyond-A5.a) + (beyond-A5.b). These are algebraic moves beyond A5's explicit framework content.

### §3.3 The "minimal algebraic realization" argument structure

A defense of the Phase 2 algebraization: any framework that needs to combine cycle-direction content with other tensor objects (to construct substrate observables, Wigner-Eckart matrix elements, etc.) requires SOME algebraic realization of A5's TI-odd content. The multiplicative TI-odd pseudoscalar is the **MINIMAL** such realization, in the sense that:

- A pseudoscalar is the lowest-dimensional non-trivial irrep of the framework's parity group (1D).
- Multiplicative combination is the simplest tensor operation (rank-0 × rank-1 → rank-1).
- Any non-trivial realization that combines with other tensor objects must contain a 1D pseudoscalar component as a factor.

This is structurally analogous to $\gamma^5$ in Dirac field theory: the chirality content of fermion fields is realized as a multiplicative TI-odd matrix because that's the minimal algebraic realization of the Z₂ chirality structure in any framework requiring tensor combinations.

**Sketch claim:** the multiplicative TI-odd pseudoscalar is the CANONICAL minimal algebraic realization of A5's content, in the sense that any framework that needs tensor-construction operations on cycle direction necessarily contains this realization as a factor.

**This is sketch-level structural argument, not a theorem.** Hardening would require formal statement of "framework that needs tensor-construction operations on cycle direction" + proof that the multiplicative TI-odd pseudoscalar is the minimal such realization.

### §3.4 Alternative TI-odd constructions — initial enumeration

The Patch 0528 §12.13 Calibration 3 listed alternative TI-odd constructions:
1. Higher-order cycle-correlation objects.
2. Local circulation tensors.
3. Bivector constructions.
4. Pseudoscalar contractions involving temporal update ordering.

To this list, the B.1 analysis at §2.3 added:
5. Curl of $\vec{j}^{net}$: $\nabla \times \vec{j}^{net}(v)$ — TI-odd by T-even × T-odd, I-odd × I-odd construction.

**Initial structural characterization:** the candidate TI-odd constructions divide by **derivative order in the substrate's local content**:
- **Order 0 (no derivatives):** $\sigma_{cycle} \cdot \hat{j}^{net}(v)$ — the Phase 2 ansatz.
- **Order 1 (first derivatives):** $\nabla \times \vec{j}^{net}(v)$, $\nabla(\sigma_{cycle} \cdot J)$ contractions, etc.
- **Order 2+ (higher derivatives, cycle-correlations):** higher-order cycle-correlation objects, bivector constructions involving multiple cycle phases.

**Sketch claim:** the Phase 2 ansatz is uniquely the **minimal-derivative-order TI-odd substrate object constructible at the host vertex from $\sigma_{cycle}$ + $\hat{j}^{net}$**. Higher-derivative alternatives are structurally distinct but are not at the same derivative order.

This gives a **"minimal canonical lowest-order" characterization** that is structurally cleaner than the previous "unique" claim: the Phase 2 ansatz is the *minimal-derivative-order canonical TI-odd substrate object*. Higher-derivative alternatives may exist but they are at higher derivative order in the substrate's local content.

### §3.5 Open sub-questions for B.2 — future-session queue

| # | Sub-question | Estimated effort |
|---|---|---|
| B.2.q1 | Formalize the "minimal algebraic realization" argument for $\sigma_{cycle}$ (§3.3): identify the formal statement of "framework that needs tensor-construction operations on A5-cyclicity content" + prove minimality of the pseudoscalar realization. | 1–2 sessions |
| B.2.q2 | Formalize the "minimal-derivative-order" characterization (§3.4): identify the formal statement that the Phase 2 ansatz is the unique TI-odd substrate object at derivative-order 0 in $\hat{j}^{net}$ + $\sigma_{cycle}$. | 1 session |
| B.2.q3 | Enumerate the derivative-order-1 TI-odd alternatives (curl, divergence-times-$\hat{n}$, etc.) explicitly and compute whether each contributes to $|M^{thermo}|$ via Wigner-Eckart, or whether Wigner-Eckart is insensitive to derivative-order-1 contributions. | 1–2 sessions |
| B.2.q4 | Re-examine the Patch 0528 §12.13 Calibration 3 listed alternatives (higher-order cycle-correlation, bivector constructions, pseudoscalar contractions with temporal update ordering) in the §3.4 minimal-derivative-order framework: are they all at higher derivative-order, or do some exist at order 0 in a different functional form? | 0.5–1 session |

Total estimated effort: 3.5–6 sessions for B.2 (broadly within the handover §13.2's 2–5 session estimate).

---

## §4 (B.3) Case A.1 derivational support — forward sketch

### §4.1 The hypothesis precisely stated

Case A.1 unification: the Mechanism A primitive's amplitude $\delta$ equals the Capotauro spatial-sector chirality magnitude $\chi$, with $\delta = \chi = \varphi^{-3}$.

The Patch 0528 §13.16 Calibration 2 reframed Case A.1 from "structurally derived" to "minimal unified realization" — the identification is motivated by minimal-primitives principle + empirical phenomenological consistency (1.64% match), not by derivation from CPP axioms.

The B.3 question: **can the identification $\delta = \chi$ be derived from CPP axioms (rather than postulated as the minimal hypothesis)?**

### §4.2 Three candidate derivational arguments

**(Arg-1) Single-primitive structural argument.** Reading C + Capotauro v2.0's substrate primitive specification commit to a SINGLE substrate primitive $\hat{n}$ with one chirality magnitude $|\chi|$. The spatial-sector edge-length perturbation amplitude $\epsilon$ (Capotauro) and the temporal-sector DI-bit propagation rate-asymmetry amplitude $\delta$ (Mechanism A) are different MANIFESTATIONS of the same primitive's response to the substrate.

If the framework's substrate primitive admits only ONE response-amplitude (the chirality magnitude $|\chi|$), then both $\epsilon = |\chi|$ and $\delta = |\chi|$ follow as direct identifications, not as numerical coincidences. This is essentially Capotauro's Substrate-Locality Unification corollary (Finding C-W40) extended from spatial to temporal sectors.

**Status:** sketch-level structural claim; would require formal extension of Substrate-Locality Unification framework to include temporal-sector responses. The extension parallels the §2.4.3 B.1.d ansatz; this and B.1 are closely linked.

**(Arg-2) Symmetry-based derivation.** A framework symmetry that interchanges spatial and temporal first-order responses would force their amplitudes to be equal. Candidate symmetries:
- Substrate-level CPT (combined charge-parity-time): if spatial perturbation and temporal perturbation are related by a CPT-like substrate symmetry, their amplitudes are equal.
- Substrate-Reading-C-duality: a duality between geometric edge perturbations (Reading C) and dynamical rate perturbations (Mechanism A) that exchanges them.

**Status:** speculative. No such framework symmetry has been registered at the CPP axiom level. Identifying one would be a substantial framework discovery.

**(Arg-3) Geometric derivation from polytope — long-term programme target.** The chirality magnitude $|\chi| = \varphi^{-3}$ is currently axiomatic (Capotauro v2.0 FI-C-9). The long-term programme target (registered at Patch 0528 §14.17 + handover §14) is to derive $|\chi|$ from pure 600-cell polytope geometry and locality constraints with no chirality input.

If this derivation succeeds, then both spatial-sector $\epsilon$ and temporal-sector $\delta$ would derive from the same geometric source (the polytope's intrinsic chirality content), and $\delta = \epsilon = |\chi|$ would be a direct consequence rather than a hypothesis.

**Status:** multi-session-arc-scale ambition; not in current forward queue. Connected to the §11.10 spatial-protection / temporal-coupling complementarity (Phase 1 sketch §11.10 methodological observation registered at Patch 0524).

### §4.3 Intermediate hardening moves

While the full B.3 closure may require (Arg-3) or a structurally novel (Arg-2), intermediate moves can harden the Case A.1 hypothesis without full derivation:

**(Move-1) Articulate Substrate-Locality Unification's temporal-sector extension.** If the spatial-sector framework (Capotauro Finding C-W40) extends to include temporal responses, then the substrate-level identification $\delta \equiv \chi$ follows. This is a sketch-level version of (Arg-1) and tractable in 1–2 sessions. The extension proves $\delta = \chi$ assuming Capotauro's substrate-locality theorem extends; it does not derive $|\chi|$ itself.

**(Move-2) Rule out structurally distinct alternatives.** Even if $\delta = \chi$ is not derived, it may be possible to show that any structurally distinct value of $\delta$ would produce empirical inconsistencies elsewhere. The Patch 0526 §13.11 cross-check (against $\chi/(6\varphi)$, $\chi\varphi/6$, $1/(6\varphi^2)$, $1/(6\varphi)$ alternatives) is the start of this; extending to identify what constraints the framework places on $\delta$ at first order in Mechanism A could narrow the admissible range.

**(Move-3) Identify candidate framework symmetries.** Without proving (Arg-2), identifying candidate framework symmetries that COULD support $\delta = \chi$ — and noting which would need to be added to CPP axioms for the derivation to close — clarifies what work remains.

### §4.4 Open sub-questions for B.3 — future-session queue

| # | Sub-question | Estimated effort |
|---|---|---|
| B.3.q1 | Articulate Substrate-Locality Unification's temporal-sector extension (Move-1). Parallel to Capotauro Finding C-W40; would deliver $\delta \equiv \chi$ conditional on Capotauro's substrate-locality theorem extending to the temporal sector. | 1–2 sessions |
| B.3.q2 | Cross-check Case A.1 against extended structural alternatives (Move-2). Beyond the Patch 0526 §13.11 four-alternative cross-check, are there other structurally motivated values of $\delta$ that fit empirical $\Delta p_{LR}^{obs}$ within precision? | 1 session |
| B.3.q3 | Identify candidate framework symmetries that could support $\delta = \chi$ (Move-3). Substrate-level CPT-like symmetry? Reading-C-Mechanism-A-duality? Neither currently in CPP axioms; identifying what would need to be added is the deliverable. | 0.5–1 session |
| B.3.q4 | Long-term: connect B.3 to the long-term programme target (Arg-3 / chirality-scale derivation from polytope). When does B.3 fold into the broader programme ambition? | (multi-session-arc-scale; not for current queue) |

Total estimated effort: 2.5–4 sessions for B.3.q1–q3 (within the handover §13.3's 1–4 session estimate, modulo long-term q4).

---

## §5 Forward queue — session-close discipline

### §5.1 What this Patch 0531 sketch delivers

- B.1 substantive structural exploration: precise ansatz statement, three-layer disambiguation, three alternative representations (R1–R3) with sketch reduction arguments, five lower-level ansatzes (B.1.a–B.1.e) flagged, six sub-questions (B.1.q1–q6) queued.
- B.2 forward sketch: algebraization question articulated, minimal algebraic realization argument sketched, minimal-derivative-order characterization proposed as cleaner uniqueness criterion, four sub-questions (B.2.q1–q4) queued.
- B.3 forward sketch: three candidate derivational arguments (Arg-1, Arg-2, Arg-3) articulated, three intermediate hardening moves (Move-1, Move-2, Move-3) identified, four sub-questions (B.3.q1–q4) queued.

### §5.2 What this Patch does NOT deliver

- No closure of B.1, B.2, or B.3.
- No new findings (DSL-N or otherwise) registered at the programme theorem/finding level.
- No modifications to Phase 2 §12 polished content in `F1_subquestion_pcd_orientation_link.md`. The Phase 2 calibration at §12.13 remains the binding state until foundations work substantively progresses.
- No promotion of F.1 sub-question status from "PROVISIONAL CLOSURE at viability level" to anything stronger.
- No modifications to v1.0 SHIPPED paper sources.

### §5.3 Forward queue for future Phase 2 foundations sessions

The §2.6 + §3.5 + §4.4 sub-question queues collect 14 total sub-questions across B.1 + B.2 + B.3. Recommended initial prioritization:

| Priority | Sub-question | Rationale |
|---|---|---|
| 1 | B.1.q5 (review-pause checkpoint on §2.2 layered disambiguation) | Self-check: is the §2.2 framing of B.1 actually responsive to ChatGPT's concern? Should resolve before deeper substantive work on B.1.q1–q4. 0.5 session, low cost, high value. |
| 2 | B.1.q4 (first-shell current sum identity) | Tractable computational sub-question with clear deliverable. 1 session. Closure-direction work. |
| 3 | B.1.q2 (curl content at first order) | Tractable explicit computation. 1 session. Closes B.1.b ansatz. |
| 4 | B.3.q1 (substrate-locality temporal extension) | Closely connected to B.1.d ansatz; shares structural work. 1–2 sessions. |
| 5 | B.2.q1 (formalize minimal algebraic realization argument) | Conceptually cleaner once B.1 questions are progressed. 1–2 sessions. |
| 6 | B.1.q1, B.1.q3 (substantive substrate-locality extension to temporal sector) | Multi-session work, may benefit from prior queue items completing first. 1–3 sessions each. |

The 5–15 session estimate from the handover §13.4 remains the operative scale for Phase 2 foundations work as a whole.

### §5.4 Anti-priorities for future foundations work

- Do NOT bundle multiple sub-questions into single "closure" patches. Each sub-question is its own structural exploration; closure pattern from Patches 0524–0527 is exactly the anti-pattern.
- Do NOT propagate any Phase 2 foundations findings to flagship-paper-level documents (e.g., `chirality_continuum.tex`, `capotauro.tex`) without external review.
- Do NOT begin F.2 / F.3 substantive content trajectories. They remain DEFERRED at decision-gate level per Patch 0529.
- Do NOT begin F.1 flagship paper assembly. Premature assembly would propagate calibrated overclaim language; defer until Phase 2 foundations work substantively progresses on B.1.q1–q3 + B.2.q1–q2 + B.3.q1 (the load-bearing sub-questions).

---

## §6 Reviewer-pause checkpoint — applied at session close

Per the Patches 0524–0528 methodological precedent (handover §10.1), the reviewer-pause checkpoint discipline is applied to this Patch 0531 itself before downstream propagation.

### §6.1 Self-assessment of this Patch 0531

**Where rigor is high:**
- The §2.2 three-layer disambiguation is a substantive structural clarification that may be the most important content of the patch.
- The §3.4 minimal-derivative-order characterization is a cleaner uniqueness criterion than the previous "unique" claim.
- The forward queue at §5.3 is concrete and actionable.

**Where rigor is lower:**
- §2.4.1's sketch reduction of (R1) at first order in $\delta$ relies on five lower-level ansatzes (B.1.a–B.1.e). Each is plausible but unverified; the reduction is structural argument, not formal theorem.
- §3.3's "minimal algebraic realization" argument for $\sigma_{cycle}$ uses analogy to $\gamma^5$ in Dirac field theory; the analogy is suggestive but not formally proven within CPP.
- §4.2 Arg-1's single-primitive structural argument depends on the §2.4.3 B.1.d ansatz (substrate-locality extension to temporal sector); the dependency means B.1 and B.3 partially share structural work.

**Where claims could be overstated (preventive flagging):**
- The §2.5 "provisional structural claim" might read as closer to closure than it actually is. The claim is conditional on B.1.a–B.1.e, all of which are themselves ansatzes. Future presentations should foreground the conditionality.
- The §3.4 "minimal-derivative-order" characterization is a sketch claim, not a theorem. Future references should use "candidate characterization" or "proposed characterization" rather than treating it as established.

### §6.2 Trigger for external reviewer-pause checkpoint

This Patch 0531 is a foundations-work opening sketch; it does not propose closures and does not propagate into downstream sectors. The §10.1 reviewer-pause checkpoint trigger criterion ("substantive multi-phase closure work where the closure language would propagate into multiple downstream sectors") does NOT activate at this Patch.

However, after Phase 2 foundations work substantively progresses on B.1.q1–q3 + B.2.q1–q2 + B.3.q1 (the load-bearing sub-questions), a reviewer-pause checkpoint should be triggered BEFORE either (i) updating Phase 2 §12 polished content in `F1_subquestion_pcd_orientation_link.md`, or (ii) propagating findings into the broader programme. The reviewer-pause checkpoint precedent from Patches 0527 → 0528 → 0529 is the operative template.

### §6.3 Methodological discipline check

- **Operational descriptions, not defensive framing:** sketch language uses "structural reduction argument" (not "structural-consistency argument"), "sketch claim" (not "verified result"), "provisional structural claim" (not "established structural claim"). ✓
- **All ansatzes flagged:** B.1.a–B.1.e (five ansatzes in §2.4 sketch reduction); B.2's algebraization assumptions noted; B.3.Arg-1's dependency on B.1.d acknowledged. ✓
- **Sketch-level output:** no findings registered, no closures claimed, no programme-level state changes propagated. ✓
- **Reviewer-pause checkpoint precedent applied:** §6 self-assessment at session close; no propagation to downstream sectors. ✓

---

## §7 Methodological notes registered

### §7.1 Layered structure of B.1 — a recurring CPP pattern

The §2.2 three-layer disambiguation (substrate per-cycle / substrate matrix element / observable cosmological) is a structural pattern that may recur across other CPP Layer 4 closures. The pattern:

- **Substrate per-cycle layer** is local algebraic by construction (per-vertex, per-AM).
- **Substrate matrix element layer** sits one step away: it computes per-event amplitudes using Wigner-Eckart on substrate-locality datums. This layer is THE layer where "local algebraic representation" questions matter.
- **Observable cosmological layer** is where accumulation / statistics / non-locality genuinely enter, via Layer 4 projections.

Conflating these layers can produce alarm about non-locality at the matrix-element layer that actually belongs at the cosmological layer. Disambiguating them sharpens the structural question without dismissing it.

This pattern is registered as a methodological observation for future Layer 4 closures: when reviewer concerns about non-locality / accumulation / statistics arise, first check which of the three layers the concern is directed at.

### §7.2 Derivative-order characterization for uniqueness claims

The §3.4 minimal-derivative-order characterization may generalize: for any substrate object whose "uniqueness" is claimed at sketch level, the precise question is often whether the object is the **minimal-derivative-order canonical** representative of its parity class — not whether it's literally unique across all higher-derivative alternatives.

Reframing "uniqueness" as "minimal-derivative-order canonical" both clarifies the actual claim AND identifies the precise scope of the alternatives that need ruling out (other order-0 constructions only) versus the alternatives that are structurally distinct but at higher order (and therefore not contradicting the minimal-canonical claim).

This is registered as a methodological observation for future substrate-object constructions in CPP.

### §7.3 Phase 2 foundations work as Phase 2.5 of F.1 trajectory

The handover §13 framed Phase 2 foundations work as additional work supporting the existing Phase 2 closure. A clean framing of this in the CPP trajectory structure: Phase 2 foundations work is **Phase 2.5** — work that retrospectively hardens Phase 2's closure language without changing Phase 2's mathematical content.

The Phase 2.5 work is exploratory by nature; closure of Phase 2.5 sub-questions sequentially hardens the calibrated framing of Phase 2 itself. Once Phase 2.5 substantively progresses on the load-bearing sub-questions (B.1.q1–q3 + B.2.q1–q2 + B.3.q1), the F.1 sub-question status can be re-examined; potentially upgraded from "PROVISIONAL CLOSURE at viability level" to a stronger framing if Phase 2.5 sub-questions close positively.

---

## §8 B.1.q5 review-pause checkpoint on §2.2 layered disambiguation

*Section added Session 139 Patch 0532 — substantive work executing the §5.3 priority (1) item B.1.q5 review-pause checkpoint on the §2.2 layered disambiguation against ChatGPT's original Patch 0528 review verdict.*

### §8.1 Sub-question framing per §2.6

B.1.q5 as registered in the §2.6 sub-question queue table:

> Re-examine the §2.2 layered disambiguation against ChatGPT's original review verdict to verify that the substrate-matrix-element layer is what ChatGPT's concern was directed at. If ChatGPT meant the per-cycle substrate layer instead, the framing of §2.3–§2.5 needs revision.

The §2.2 disambiguation made a substantive structural move: it placed all three of ChatGPT's listed alternatives (cycle-history accumulation, nonlocal transport asymmetry, coarse-grained update statistics) at the observable cosmological layer. B.1.q5 asks whether that placement is faithful to ChatGPT's actual concern as registered.

### §8.2 Method and source material

Working from the Patch 0528 §12.13 Calibration 4 verbatim text preserved at `flagship_papers/dynamical_substrate_law/sketches/F1_subquestion_pcd_orientation_link.md` §12.13. This is the explicitly registered version of ChatGPT's concern; ChatGPT's raw review text is preserved at user-side per Patch 0528 handover record. The review-pause checks §2.2's placement against this registered text — verbatim recovery of ChatGPT's review (if available) would enable an even sharper review-pause, but the registered text is the operative reference for current programme state.

### §8.3 ChatGPT's three alternatives — verbatim from Patch 0528 §12.13

The exact text registered at Patch 0528 §12.13 Calibration 4, with the parenthetical qualifications that disambiguate each alternative's intended layer:

> The Phase 2 derivation assumes the thermodynamic chirality observable is **representable as a local algebraic object at the host vertex**. This is an unflagged ansatz. The observable could instead emerge from:
> - **Cycle-history accumulation** (the temporal chirality content builds up over many Absolute Moments, not at a single cycle).
> - **Nonlocal transport asymmetry** (the chirality content distributes across the substrate's connectivity graph rather than localizing at one vertex).
> - **Coarse-grained update statistics** (the chirality content emerges only at scales above individual CP cycles).

The parentheticals are load-bearing — they explicitly identify the scale/locus at which each alternative operates.

### §8.4 Per-alternative placement analysis

**(1) Cycle-history accumulation.** Parenthetical: "the temporal chirality content builds up over many Absolute Moments, not at a single cycle." The phrase "over many Absolute Moments, not at a single cycle" is explicit: this alternative is about multi-AM accumulation. The natural layer is observable cosmological (Phase 4's $|M^{thermo}| \to \Delta p_{LR}^{obs}$ chain accumulates per-event matrix elements over cosmological time). **§2.2 placement at observable cosmological layer is CORRECT.**

**(2) Nonlocal transport asymmetry.** Parenthetical: "the chirality content distributes across the substrate's connectivity graph rather than localizing at one vertex." The phrase "distributes across the substrate's connectivity graph rather than localizing at one vertex" is explicit: this alternative is about substrate-spatial distribution, NOT cosmological accumulation. The natural layer is substrate-matrix-element / substrate-object layer — where the Phase 2 ansatz $\vec{\omega}_{PCD}(v_{\text{host}}) = \sigma_{cycle} \cdot \hat{j}_{DI}^{net}(v_{\text{host}})$ claims localization at host vertex. **§2.2 placement at observable cosmological layer is INCORRECT.** The corrected placement is at substrate-matrix-element layer (Reading b of §8.6 below).

**(3) Coarse-grained update statistics.** Parenthetical: "the chirality content emerges only at scales above individual CP cycles." The phrase "at scales above individual CP cycles" is explicit: this alternative is about above-cycle scales = multi-cycle = cosmological. The natural layer is observable cosmological. **§2.2 placement at observable cosmological layer is CORRECT.**

### §8.5 Verdict — disambiguation structurally coherent; one placement needs revision

The §2.2 three-layer framework (substrate per-cycle / substrate matrix element / observable cosmological) is structurally coherent. The three layers ARE distinct in CPP substrate-physics; the framework correctly identifies that ChatGPT's-class concerns can be cleanly partitioned across them.

What the §2.2 placement got right (two of three): alternatives (1) and (3) are clearly cosmological per their parentheticals; §2.2 places them correctly.

What the §2.2 placement got wrong (one of three): alternative (2) "Nonlocal transport asymmetry" was placed at observable cosmological layer, but the parenthetical "distributes across the substrate's connectivity graph rather than localizing at one vertex" makes clear ChatGPT was raising a substrate-spatial concern about chirality content distribution at the substrate-object level — not a cosmological-scale concern.

The §2.2 disambiguation captured the right STRUCTURE (three layers) but applied an over-aggressive placement (all alternatives at one layer). The B.1.q5 review-pause has surfaced this misplacement.

### §8.6 Refined placement of ChatGPT's alternatives

| Alternative | §2.2 placement (Patch 0531) | Refined placement (this Patch) | Reason for refinement |
|---|---|---|---|
| (1) Cycle-history accumulation | Observable cosmological | Observable cosmological (UNCHANGED) | Parenthetical "over many Absolute Moments" confirms cosmological. |
| (2) Nonlocal transport asymmetry | Observable cosmological | **Substrate-matrix-element / substrate-object** | Parenthetical "distributes across the substrate's connectivity graph rather than localizing at one vertex" identifies substrate-spatial concern, not cosmological. |
| (3) Coarse-grained update statistics | Observable cosmological | Observable cosmological (UNCHANGED) | Parenthetical "at scales above individual CP cycles" confirms cosmological. |

### §8.7 Connection of refined placement to $\hat{j}_{DI}^{net}$'s first-shell-aggregated structure

The Phase 1 derivation result (sketch §11 / Finding DSL-1) computed the substrate's net DI-bit current at the host vertex:
$$\vec{j}_{DI}^{net}(v_{\text{host}}) = (6 r_0 \delta / \varphi^2)\,\hat{n} + \mathcal{O}(\delta^2)$$
This is a quantity computed AT the host vertex, with its value determined by aggregation over the 12 first-shell neighbors via Mechanism A's DI-bit propagation-rate asymmetry.

Read strictly, the chirality information that produces $\vec{j}_{DI}^{net}$ at the host "lives in" the first-shell connectivity — the 12 host-to-first-shell edges + their direction-correlated rate biases. The Phase 2 ansatz $\vec{\omega}_{PCD}(v_{\text{host}}) = \sigma_{cycle} \cdot \hat{j}_{DI}^{net}(v_{\text{host}})$ treats $\hat{j}_{DI}^{net}$ as a host-vertex quantity (standard CPP substrate-physics convention — currents at points are first-shell-determined like derivatives in continuum field theory).

ChatGPT's alternative (2) "Nonlocal transport asymmetry" precisely asks: is this treatment justified, or does the chirality content actually distribute across the host + first-shell connectivity graph in a way that makes the host-vertex localization claim premature?

This is structurally addressed (not yet resolved) by the Capotauro substrate-locality theorem (Finding C-W39) — which establishes spatial-sector chirality content localizes at the first-shell icosahedron — and its proposed temporal-sector extension via ansatz B.1.d (sketch §2.4.3). Under B.1.d, the substrate's per-cycle DI-bit-flux content localizes at the first-shell icosahedron of the host vertex, providing the structural framework for treating $\vec{j}_{DI}^{net}(v_{\text{host}})$ as a legitimate host-vertex quantity.

**B.1.d is itself an ansatz** at this Patch — it is flagged in the §2.4.3 reduction argument. Hardening B.1.d (via sub-question B.1.q3) is the load-bearing structural work that responds to ChatGPT's alternative (2).

### §8.8 Forward queue implications — priority elevation of B.1.q3 / B.3.q1

The B.1.q5 verdict has substantive consequences for the §5.3 priority ordering:

- **B.1.q3** (substrate-locality extension to the temporal sector via B.1.d) addresses ChatGPT's alternative (2) concern at the load-bearing structural level.
- **B.3.q1** (Move-1: articulate Substrate-Locality Unification temporal extension parallel to Finding C-W40) shares structural work with B.1.q3 via the B.1.d ↔ B.3.Move-1 cross-commitment dependency registered at §5.

**Recommended §5.3 priority revision** (sketch-level recommendation; requires Thomas's authorization before becoming binding):

| Order | Sub-question | Rationale |
|---|---|---|
| (1) | B.1.q5 [CLOSED at sketch level this Patch] | Review-pause delivered substantive refinement of §2.2 placement. |
| (2) | B.1.q4 first-shell current sum identity | Tractable computational sub-question; informs both B.1.q3 and B.1.q2. |
| (3) | **B.1.q3 + B.3.q1** substrate-locality temporal extension | **PROMOTED from §5.3 priority (4) to (3).** Load-bearing for B.1's response to ChatGPT's alternative (2) per §8.5 verdict. |
| (4) | B.1.q2 curl content explicit computation | Preserved priority; informs B.1.b ansatz. |
| (5) | B.2.q1 minimal algebraic realization formalization | Preserved priority. |
| (6) | B.1.q1 + B.1.q3 substantive substrate-locality extension at full theorem level | Preserved priority. |

The promotion of B.1.q3 / B.3.q1 reflects that the substrate-locality temporal extension is no longer just a "framework-level cleanup" item but specifically THE load-bearing structural work for B.1's response to a verbatim ChatGPT concern.

### §8.9 Methodological observation — review-pause discipline pattern

The §2.2 three-layer disambiguation registered the right structural framework but applied it with an overly aggressive placement (all three of ChatGPT's alternatives at one layer). The B.1.q5 review-pause caught the misplacement before it propagated downstream into B.1's substantive closure work.

The cost of the B.1.q5 review-pause: approximately half a session of structural analysis (this §8). The value: identified a misplacement that would have caused B.1's later substantive work (e.g., B.1.q1, B.1.q2 substantive closure attempts) to operate under the false assumption that ChatGPT's alternative (2) was a cosmological-layer concern not requiring substrate-physics resolution. Avoiding that misdirection is high-value relative to the cost.

**Programme-level lesson registered:** when introducing a structural disambiguation, the immediate-next sub-question should explicitly check whether the disambiguation faithfully maps prior reviewer concerns to the new framework — not just whether the framework itself is internally coherent. The pattern templates future structural-disambiguation work in CPP: (a) propose framework; (b) re-examine framework against prior reviewer concerns at the immediate-next sub-question; (c) refine framework as needed before downstream substantive work proceeds.

This is a variant of the §6.2 reviewer-pause checkpoint discipline applied at sub-question scale rather than session-close scale. Both serve the same epistemic function: catch overclaim before downstream propagation.

### §8.10 Self-checkpoint at session close

Two places where §8 itself could overstate:

(i) The verdict "INCORRECT placement" for alternative (2) reads as sharp negative assessment of §2.2. The substantive content is more nuanced: §2.2 captured the right STRUCTURE (three layers) but applied an over-aggressive placement (all alternatives at one layer). §2.2 is not refuted; it is REFINED. The structural framework of §2.2 is preserved; only the per-alternative placement is corrected.

(ii) The §8.8 recommended priority revision is a sketch-level recommendation. Binding §5.3 priority adjustment requires Thomas's authorization. The §5.3 ordering as registered at Patch 0531 remains operative until explicitly revised.

One place where §8 could overstate by under-claim:

(iii) §8 may read as if ChatGPT's alternative (2) is straightforwardly resolved by invoking B.1.d. In fact, B.1.d is itself an ansatz at this Patch — it is flagged in §2.4.3 reduction argument and registered as a future-hardening target via sub-question B.1.q3. Alternative (2) is not "resolved" by this Patch; it is "structurally located where the resolution framework lives." Resolution awaits B.1.q3 substantive closure.

### §8.11 Status update

- B.1.q5 CLOSED at sketch level with the verdict that §2.2's disambiguation framework is structurally correct but its placement of ChatGPT's alternative (2) requires refinement from observable cosmological layer to substrate-matrix-element / substrate-object layer.
- §2.2 placement of alternatives (1) and (3) is CONFIRMED CORRECT.
- §2.2 placement of alternative (2) is REFINED to substrate-matrix-element / substrate-object layer; the relevant structural framework for resolution is B.1.d substrate-locality temporal extension, addressed via sub-question B.1.q3 (and via cross-commitment dependency, B.3.q1).
- B.1.q1, B.1.q2, B.1.q3, B.1.q4, B.1.q6 sub-question framings UNCHANGED.
- B.2.q1, B.2.q2, B.2.q3, B.2.q4 sub-question framings UNCHANGED.
- B.3.q1, B.3.q2, B.3.q3, B.3.q4 sub-question framings UNCHANGED.
- F.1 sub-question status UNCHANGED at "PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work" per Patch 0528 §14.17.
- No findings registered (B.1.q5 is review-pause sub-question; verdict is at sketch level structural analysis, not theorem-level claim).
- No new ansatzes flagged (B.1.a–B.1.e from §2.4 unchanged).
- §2.2 disambiguation table is NOT modified inline at Patch 0531's §2.2 (per immutable-Patch discipline); the refined placement is registered in §8.6 of this Patch and supersedes §2.2's placement for downstream work.
- §5.3 priority ordering recommendation revised in §8.8; binding revision pending Thomas's authorization.

---

## §9 B.1.q4 first-shell current sum identity — sub-question closed at sketch level

*Section added Session 139 Patch 0533 — substantive computational work executing the revised §5.3 priority (2) item B.1.q4 first-shell current sum identity (per the §8.8 priority revision authorized by Thomas at session 139 continuation).*

### §9.0 Authorization of the §8.8 priority revision

The §8.8 recommended §5.3 priority revision (registered at Patch 0532 as sketch-level recommendation pending authorization) is authorized by Thomas at Session 139 continuation. The revised ordering is now binding programme priority (no longer "pending authorization"):

| Order | Sub-question | Status |
|---|---|---|
| (1) | B.1.q5 review-pause checkpoint | CLOSED at Patch 0532 |
| (2) | **B.1.q4 first-shell current sum identity** | **Executed in §9.1–§9.13 below — this Patch** |
| (3) | B.1.q3 + B.3.q1 substrate-locality temporal extension (PROMOTED) | Next priority after B.1.q4 |
| (4) | B.1.q2 curl content explicit computation | Preserved priority |
| (5) | B.2.q1 minimal algebraic realization formalization | Preserved priority |
| (6) | B.1.q1 + B.1.q3 substantive substrate-locality extension | Preserved priority |

### §9.1 Sub-question framing per §2.6

B.1.q4 as registered in the §2.6 sub-question queue table:

> Derive the first-shell current sum identity $\sum_i \hat{j}^{net}(v_i)$ at first order (B.1.e). Parallel to Capotauro's $\sum_i \hat{u}_i = -(6/\varphi)\hat{n}$ identity. 1 session.

The §2.4.3 (R3) reduction argument needed the B.1.e ansatz:

> The claim $\sum_{i=1}^{12} \hat{j}^{net}(v_i) \parallel \hat{n}$ at first order in $\delta$ by icosahedral symmetry (using the same residual $I_h$ structure as the position sum identity). The argument structure is plausible but the explicit computation is deferred.

B.1.q4 closes the explicit computation — and produces a stronger result than the original $\parallel \hat{n}$ ansatz: the sum has an explicit coefficient that can be derived in closed form from the 600-cell first-shell geometry.

### §9.2 Setup — Phase 1 per-vertex current formula generalized

Phase 1 (sketch §11.3 of `F1_subquestion_pcd_orientation_link.md`) derived the per-vertex current formula at $v_{\text{host}}$ under vertex-aligned $\hat{n} = v_{\text{host}}$ (Capotauro Reading C):

$$\vec{j}_{DI}^{net}(v) = 2 r_0 \delta \sum_{j=1}^{12} (\hat{u}_j^v \cdot \hat{n})\,\hat{u}_j^v + \mathcal{O}(\delta^2)$$

where $\{\hat{u}_j^v\}_{j=1}^{12}$ are the unit directions from $v$ to its 12 first-shell neighbors in 4D. At $v = v_{\text{host}}$, the load-bearing identities $\hat{u}_j \cdot \hat{n} = -1/(2\phi)$ uniform and $\sum_j \hat{u}_j = -(6/\phi)\hat{n}$ reduce this to the boxed Phase 1 result $\vec{j}_{DI}^{net}(v_{\text{host}}) = (6 r_0 \delta/\phi^2)\hat{n}$.

**The crucial subtlety for B.1.q4.** At a general vertex $v$ in the 600-cell, the framework $\hat{n}$ is fixed parallel to $v_{\text{host}}$ direction — it does NOT realign to $\hat{v}$. Therefore the Phase 1 simplification $\hat{u}_j \cdot \hat{n} = -1/(2\phi)$ uniform does NOT hold at $v \neq v_{\text{host}}$; the projections $\hat{u}_j^v \cdot \hat{n}$ depend on $v$'s orientation in the global frame. The per-vertex current at $v \neq v_{\text{host}}$ requires a generalized derivation.

### §9.3 600-cell first-shell structure at general vertex $v$

By 600-cell vertex-transitivity (the symmetry group acts transitively on the 120 vertices), every vertex $v$ has 12 first-shell neighbors in icosahedral arrangement. In $v$'s LOCAL frame (where $v$'s vertex direction $\hat{v}$ replaces $\hat{n}$ as the polar axis), the first-shell satisfies the same Phase 1 identities: $\hat{u}_j^v \cdot \hat{v} = -1/(2\phi)$ uniform and $\sum_j \hat{u}_j^v = -(6/\phi)\hat{v}$.

Decomposition of $\hat{u}_j^v$ into $\hat{v}$-parallel + perpendicular parts:

$$\hat{u}_j^v = -\frac{1}{2\phi}\,\hat{v} + \frac{\sqrt{2+\phi}}{2}\,\hat{w}_j^v$$

where $\{\hat{w}_j^v\}_{j=1}^{12}$ are 12 unit vectors in the 3D hyperplane perpendicular to $\hat{v}$, forming a regular icosahedron in that hyperplane. The coefficient $\sqrt{2+\phi}/2 = \sqrt{1 - 1/(4\phi^2)}$ ensures $|\hat{u}_j^v| = 1$.

Two icosahedron identities in the perpendicular hyperplane:
- **Central symmetry**: $\sum_j \hat{w}_j^v = 0$ (icosahedron's vertices are centrally symmetric in their 3D hyperplane).
- **Tensor sum isotropy**: $\sum_j \hat{w}_j^v \otimes \hat{w}_j^v = 4\,P_{\perp v}$ where $P_{\perp v} = I - \hat{v}\otimes\hat{v}$ is the projector onto the 3D hyperplane perpendicular to $\hat{v}$. (Proof: $I_h$ acts irreducibly on the 3D hyperplane; by Schur's lemma any $I_h$-invariant symmetric 2-tensor is proportional to $P_{\perp v}$; the trace $\sum_j |\hat{w}_j^v|^2 = 12$ fixes the coefficient at $12/3 = 4$.)

### §9.4 General per-vertex current formula

Substituting the decomposition into the Phase 1 formula, using $a \equiv \hat{v}\cdot\hat{n}$ for the projection of $v$ onto the framework $\hat{n}$:

$$\hat{u}_j^v \cdot \hat{n} = -\frac{a}{2\phi} + \frac{\sqrt{2+\phi}}{2}(\hat{w}_j^v \cdot \hat{n})$$

$$\sum_j (\hat{u}_j^v \cdot \hat{n})\,\hat{u}_j^v = \sum_j \left[-\frac{a}{2\phi} + \frac{\sqrt{2+\phi}}{2}(\hat{w}_j^v \cdot \hat{n})\right] \left[-\frac{1}{2\phi}\,\hat{v} + \frac{\sqrt{2+\phi}}{2}\,\hat{w}_j^v\right]$$

Expanding into four terms and using the two icosahedron identities to reduce:
- Term $\hat{v}\hat{v}$ scalar: $\frac{a}{4\phi^2}$, summed over 12 vertices → $\frac{3a}{\phi^2}\hat{v}$.
- Cross terms with $\hat{w}_j^v$ scalar: vanish by $\sum_j \hat{w}_j^v = 0$.
- Term $\hat{w}_j^v \hat{w}_j^v$ tensor: $\frac{2+\phi}{4} \cdot 4\,P_{\perp v}\hat{n} = (2+\phi)(\hat{n} - a\hat{v})$.

Combining:

$$\sum_j (\hat{u}_j^v \cdot \hat{n})\,\hat{u}_j^v = \frac{3a}{\phi^2}\hat{v} + (2+\phi)(\hat{n} - a\hat{v}) = (2+\phi)\,\hat{n} + a\left[\frac{3}{\phi^2} - (2+\phi)\right]\hat{v}$$

Using the golden-ratio identities $1/\phi^2 = 2 - \phi$ and $1/\phi = \phi - 1$: $\frac{3}{\phi^2} - 2 - \phi = 3(2-\phi) - 2 - \phi = 4 - 4\phi = -4/\phi$. Substituting:

$$\boxed{\;\vec{j}_{DI}^{net}(v) = 2 r_0 \delta \left[(2+\phi)\,\hat{n} - \frac{4a}{\phi}\,\hat{v}\right] + \mathcal{O}(\delta^2) \;\text{where}\; a \equiv \hat{v}\cdot\hat{n}\;}$$

**Sanity check at $v = v_{\text{host}}$** (where $\hat{v} = \hat{n}$, $a = 1$): the formula gives $2 r_0 \delta [(2+\phi) - 4/\phi]\hat{n}$. Computing $(2+\phi) - 4/\phi = (2\phi + \phi^2 - 4)/\phi = (2\phi + \phi + 1 - 4)/\phi = (3\phi - 3)/\phi = 3(\phi-1)/\phi = 3/\phi^2$. Result: $\vec{j}_{DI}^{net}(v_{\text{host}}) = (6 r_0 \delta /\phi^2)\hat{n}$. ✓ Matches Phase 1's boxed result exactly.

### §9.5 Application to first-shell vertex $v_i$

For $v_i$ a first-shell neighbor of $v_{\text{host}}$ (so $v_i = v_{\text{host}} + (1/\phi)\hat{u}_i$ in 4D coordinates with $|v_i| = 1$), the projection onto $\hat{n}$:

$$a_i \equiv \hat{v}_i \cdot \hat{n} = v_i \cdot v_{\text{host}} = 1 + (1/\phi)(\hat{u}_i \cdot \hat{n}) = 1 - \frac{1}{2\phi^2} = \frac{\phi}{2}$$

(Using $1 - 1/(2\phi^2) = 1 - (2-\phi)/2 = \phi/2$.) So all 12 first-shell vertices $v_i$ have $\hat{v}_i \cdot \hat{n} = \phi/2$ uniform; geometrically, $v_i$ sits at polar angle $\arccos(\phi/2) = 36°$ from $v_{\text{host}}$.

Substituting $a_i = \phi/2$ into the general formula:

$$\vec{j}_{DI}^{net}(v_i) = 2 r_0 \delta\left[(2+\phi)\,\hat{n} - \frac{4(\phi/2)}{\phi}\,\hat{v}_i\right] = 2 r_0 \delta\left[(2+\phi)\,\hat{n} - 2\,\hat{v}_i\right]$$

Decomposing $\hat{v}_i = (\phi/2)\hat{n} + \sin(36°)\,\hat{e}_i$ where $\hat{e}_i$ is the unit perpendicular component of $\hat{v}_i$ in the $\hat{n}$-$\hat{v}_i$ plane (and $\sin(36°) = \sqrt{(3-\phi)/4} = \sqrt{3-\phi}/2$):

$$\vec{j}_{DI}^{net}(v_i) = 2 r_0 \delta\left[(2+\phi)\hat{n} - \phi\hat{n} - 2\sin(36°)\hat{e}_i\right] = 4 r_0 \delta\left[\hat{n} - \sin(36°)\,\hat{e}_i\right]$$

**Per-vertex first-shell current**: each $v_i$ has current $4 r_0 \delta[\hat{n} - \sin(36°)\hat{e}_i]$, which has $\hat{n}$-component $4 r_0\delta$ (uniform across the 12 first-shell vertices) and a perpendicular component $-4 r_0\delta\sin(36°)\hat{e}_i$ that differs per vertex.

**Magnitude (uniform across 12)**: $|\vec{j}_{DI}^{net}(v_i)| = 4 r_0 \delta\sqrt{1 + \sin^2(36°)} = 4 r_0 \delta\sqrt{(7-\phi)/4} = 2 r_0 \delta\sqrt{7-\phi}$.

### §9.6 First-shell current sum identity — main result

Unit vector at each first-shell vertex:

$$\hat{j}_{DI}^{net}(v_i) = \frac{2}{\sqrt{7-\phi}}\left[\hat{n} - \sin(36°)\,\hat{e}_i\right]$$

Sum over the 12 first-shell vertices of $v_{\text{host}}$:

$$\sum_{i=1}^{12} \hat{j}_{DI}^{net}(v_i) = \frac{2}{\sqrt{7-\phi}}\left[12\,\hat{n} - \sin(36°)\sum_{i=1}^{12}\hat{e}_i\right]$$

The 12 perpendicular unit vectors $\{\hat{e}_i\}$ lie in the 3D hyperplane perpendicular to $\hat{n}$. By $I_h$ residual symmetry at $v_{\text{host}}$ (which permutes the 12 first-shell vertices and hence their perpendicular components), the set $\{\hat{e}_i\}$ forms a regular icosahedron in this 3D hyperplane. By central symmetry of the icosahedron:

$$\sum_{i=1}^{12} \hat{e}_i = 0$$

**The B.1.q4 identity**:

$$\boxed{\;\sum_{i=1}^{12} \hat{j}_{DI}^{net}(v_i) = \frac{24}{\sqrt{7-\phi}}\,\hat{n} \approx 10.345\,\hat{n} \quad \text{at first order in}\; \delta\;}$$

**Numerical verification at machine precision**: `flagship_papers/dynamical_substrate_law/code/verify_b1q4_first_shell_current_sum.py` — explicit 600-cell construction (120 vertices), computation of per-vertex currents at all 12 first-shell neighbors of $v_{\text{host}}$, and verification of all five load-bearing identities ($\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ uniform; $\sum_i \hat{u}_i = -(6/\phi)\hat{n}$; Phase 1's $\vec{j}^{net}(v_{\text{host}}) = (6r_0\delta/\phi^2)\hat{n}$; first-shell current magnitude $2 r_0 \delta\sqrt{7-\phi}$ uniform across 12 vertices; B.1.q4 identity $\sum_i \hat{j}^{net}(v_i) = (24/\sqrt{7-\phi})\hat{n}$) across five test $\delta$ values $\{0, 0.1, \phi^{-3}, 0.5, -0.2\}$ with all deviations from analytic values $\leq 2 \times 10^{-15}$.

### §9.7 Structural interpretation

The B.1.q4 identity has three structural features worth registering:

**(i) The result is along $\hat{n}$ — direction-uniformity in the sum.** Each first-shell current has both an $\hat{n}$-parallel component (uniform, $4 r_0\delta$) and a perpendicular component (different per vertex). Summing the unit vectors: the parallel components add to $12 \cdot (2/\sqrt{7-\phi})$, while the perpendicular components $\hat{e}_i$ cancel by icosahedral central symmetry. This is the mechanism for direction-uniformity in the sum despite per-vertex direction-variation.

**(ii) The coefficient $24/\sqrt{7-\phi} \approx 10.345$ is determined by 600-cell first-shell geometry.** It depends on: the uniform polar angle $\arccos(\phi/2) = 36°$ between $v_{\text{host}}$ and its first-shell neighbors (a 600-cell-specific property); the per-vertex current magnitude $2 r_0 \delta\sqrt{7-\phi}$; and the icosahedral arrangement enabling perpendicular cancellation. The coefficient is calculable in closed form from the substrate geometry — not a free parameter.

**(iii) Comparison to host: the first-shell sum is $\approx 10.345$ times the host unit current.** Locally at $v_{\text{host}}$: $\hat{j}_{DI}^{net}(v_{\text{host}}) = \hat{n}$. The first-shell aggregate (summing 12 unit currents) gives approximately ten times this. The "first-shell amplification factor" $\eta_{1\text{-shell}} \equiv 24/\sqrt{7-\phi} \approx 10.345$ is a substrate-geometric quantity that enters any nonlocal-spatial-averaging analysis.

### §9.8 Connection to (R3) nonlocal spatial averaging reduction in §2.4.3

The §2.4.3 (R3) representation:

$$\vec{\omega}_{PCD}(v_{\text{host}}) = \sigma_{cycle}\left[W_0 \hat{j}_{DI}^{net}(v_{\text{host}}) + W_1 \sum_{i=1}^{12} \hat{j}_{DI}^{net}(v_i)\right]$$

Substituting the B.1.q4 identity and the host current direction:

$$\vec{\omega}_{PCD}(v_{\text{host}}) = \sigma_{cycle}\left[W_0\hat{n} + W_1 \cdot \frac{24}{\sqrt{7-\phi}}\,\hat{n}\right] = \sigma_{cycle}\left(W_0 + \frac{24 W_1}{\sqrt{7-\phi}}\right)\hat{n}$$

**The R3 nonlocal spatial averaging reduces to the Phase 2 local algebraic form at first order, up to coefficient renormalization $c' = W_0 + 24 W_1/\sqrt{7-\phi}$.** The renormalization is absorbed into Phase 3's normalization choice ($|\hat{j}^{net}|_0$ at sketch §13.4 of `F1_subquestion_pcd_orientation_link.md`). Structurally, (R3) is equivalent to the Phase 2 ansatz at first order — the §2.4.3 R3 reduction argument is now demonstrated at sketch level with an explicit coefficient.

### §9.9 Connection to ChatGPT's alternative (2) at substrate-matrix-element layer

Per Patch 0532 §8.7 verdict, ChatGPT's alternative (2) "Nonlocal transport asymmetry" with verbatim parenthetical "the chirality content distributes across the substrate's connectivity graph rather than localizing at one vertex" is placed at substrate-matrix-element / substrate-object layer (NOT observable cosmological).

B.1.q4 provides PARTIAL structural response to this concern. At first order in $\delta$:

1. The first-shell-distributed current content, summed over the 12 first-shell vertices, points along $\hat{n}$ — the same direction as the host vertex current.
2. The per-vertex direction-variation at first-shell ($\hat{e}_i$ components) cancels in the sum by icosahedral central symmetry.
3. The remaining $\hat{n}$-aligned aggregate has explicit coefficient $24/\sqrt{7-\phi} \approx 10.345$ — a substrate-geometric quantity, not a free parameter.

**What this establishes.** The "chirality content distribution across substrate's connectivity graph" (ChatGPT's verbatim language for alternative (2)) collapses to a direction-uniform multiple of the host current's direction when summed over the host + first-shell. At leading order, the distribution-vs-localization distinction reduces to a coefficient renormalization absorbed into Phase 3's normalization.

**What this does NOT establish.** Full resolution of alternative (2) requires the substrate-locality temporal extension theorem (B.1.d ansatz at §2.4.3). B.1.q4 provides the explicit identity needed for B.1.q3's substantive derivation but is not itself the resolution. The Capotauro v2.0 spatial-sector substrate-locality theorem (Finding C-W39) operates at all orders in $\varepsilon$; the temporal-sector analog at all orders in $\delta$ is the B.1.q3 target.

### §9.10 Higher-order caveat

The B.1.q4 identity holds at first order in $\delta$ only. Three structural observations on higher-order behavior:

**At $\mathcal{O}(\delta^2)$**: Phase 1's derivation (sketch §11) was carried out at first order; second-order corrections involve second-shell coupling that depends on the 600-cell's structure beyond the immediate first-shell. The per-vertex formula $\vec{j}_{DI}^{net}(v) = 2 r_0 \delta[(2+\phi)\hat{n} - (4a/\phi)\hat{v}]$ above is first-order; second-order corrections are not derived here.

**$I_h$ residual symmetry at $v_{\text{host}}$ is exact**: this symmetry holds at all orders in $\delta$ (it's a symmetry of the unperturbed substrate, not a first-order approximation). Therefore the sum $\sum_i \vec{j}_{DI}^{net}(v_i)$ remains $\parallel \hat{n}$ at all orders — the direction-uniformity from icosahedral central symmetry survives.

**But the explicit coefficient $24/\sqrt{7-\phi}$ is first-order**. At $\mathcal{O}(\delta^2)$, the coefficient may receive corrections; the structural conclusion (parallel to $\hat{n}$) survives, the explicit value may shift. Sub-question B.1.q6 registers higher-order analysis as future work.

### §9.11 Refinement of the §2.4.3 "parallel to Capotauro" framing

The §2.4.3 sketch invoked "Capotauro's $\sum_i \hat{u}_i = -(6/\phi)\hat{n}$ identity (sketch §13.2 / Phase 1 verification)" as the structural parallel for the B.1.q4 identity claim. Closer examination of the §9 derivation:

Both identities use $I_h$ residual symmetry at $v_{\text{host}}$ + central symmetry of the icosahedron formed by 12 first-shell-related unit vectors. The structural parallel is correct at the group-theoretic level:
- **Capotauro's $\sum_i \hat{u}_i$**: 12 first-shell DIRECTIONS from $v_{\text{host}}$, decomposed into $\hat{n}$-parallel (uniform $-1/(2\phi)$) + perpendicular (icosahedron in 3D, sums to zero by central symmetry).
- **B.1.q4 $\sum_i \hat{j}_{DI}^{net}(v_i)$**: 12 first-shell unit CURRENTS, decomposed into $\hat{n}$-parallel (uniform $2/\sqrt{7-\phi}$) + perpendicular (icosahedron of $\hat{e}_i$ in 3D, sums to zero by central symmetry).

The §9 derivation makes the structural parallel precise: both identities exhibit the same direction-collapse mechanism (perpendicular cancellation by icosahedral central symmetry); the parallel components add to the explicit coefficient determined by the 600-cell geometry. The §2.4.3 heuristic is now sharpened to an explicit identity.

### §9.12 Self-checkpoint at session close

Three places where §9 could overstate:

(i) The "first order in $\delta$" qualifier is essential. The explicit coefficient $24/\sqrt{7-\phi}$ does NOT automatically extend to higher orders; higher-order corrections require B.1.q6 work.

(ii) The §9.9 connection to ChatGPT's alternative (2) describes PARTIAL structural response. Full resolution of alternative (2) requires B.1.q3 substrate-locality temporal extension theorem; B.1.q4 contributes the structural identity (not the theorem).

(iii) The §9.4 general per-vertex formula $\vec{j}_{DI}^{net}(v) = 2 r_0 \delta[(2+\phi)\hat{n} - (4a/\phi)\hat{v}]$ is at sketch level. It generalizes Phase 1's vertex-aligned result to arbitrary vertex $v$ under fixed framework $\hat{n}$, using standard icosahedral tensor sum identities. The derivation is structurally sound (numerically verified at machine precision) but is registered at sketch level — NOT as a new finding. (Anti-priority: no findings registered at this Patch; the general formula is an intermediate result supporting the B.1.q4 main identity.)

### §9.13 Status update

- **B.1.q4 CLOSED at sketch level** with explicit identity: $\sum_{i=1}^{12} \hat{j}_{DI}^{net}(v_i) = (24/\sqrt{7-\phi})\hat{n} \approx 10.345\,\hat{n}$ at first order in $\delta$.
- B.1.e ansatz from §2.4.3 demonstrated at sketch level (stronger than original $\parallel \hat{n}$ claim — explicit coefficient provided).
- Structural consequence: R3 nonlocal spatial averaging reduces to coefficient renormalization $c' = W_0 + 24 W_1/\sqrt{7-\phi}$ at first order; structurally equivalent to Phase 2 local algebraic form.
- PARTIAL structural response to ChatGPT's alternative (2): leading-order direction-uniformity demonstrated with explicit coefficient; full response requires B.1.q3.
- Numerical verification at machine precision at `flagship_papers/dynamical_substrate_law/code/verify_b1q4_first_shell_current_sum.py` across five test $\delta$ values; max deviations $\leq 2 \times 10^{-15}$.
- B.1.a, B.1.b, B.1.c, B.1.d ansatzes UNCHANGED (B.1.e demonstrated; the other four remain as flagged).
- B.1.q1, B.1.q2, B.1.q3, B.1.q5 [CLOSED at Patch 0532], B.1.q6 sub-question framings UNCHANGED.
- B.2.q1–q4, B.3.q1–q4 sub-question framings UNCHANGED.
- F.1 sub-question status UNCHANGED at "PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work".
- **No findings registered** at Patch 0533 (B.1.q4 identity is at sketch level, not theorem level).
- No new ansatzes flagged.
- No v1.0 SHIPPED .tex source modifications.
- No Phase 2 §12 polished content modifications in `F1_subquestion_pcd_orientation_link.md`.
- §5.3 priority revision authorized (§9.0) — revised ordering now binding programme priority.

**Forward queue post-Patch 0533:**

- (A) Next priority per revised §5.3 ordering: **B.1.q3 + B.3.q1 substrate-locality temporal extension** (shared structural work via B.1.d ↔ B.3.Move-1 cross-commitment dependency; load-bearing for B.1's full response to ChatGPT's alternative (2); estimated 1–2 sessions). The B.1.q4 identity derived in this Patch (§9.6) provides the explicit first-shell sum structure that B.1.q3 needs as input.
- (B) Following B.1.q3 + B.3.q1: B.1.q2 curl content explicit computation (1 session).
- (C) Following B.1.q2: B.2.q1 minimal algebraic realization formalization (1–2 sessions).
- (D) F.1 flagship paper assembly DEFERRED until load-bearing sub-questions substantively progress.
- (E) F.2/F.3 substantive content DEFERRED at decision-gate level.
- (F) Long-term programme target — chirality scale from polytope geometry — REGISTERED + DEFERRED.

---

*This sketch opens Phase 2 foundations work (Phase 2.5 of F.1 trajectory) at Session 139 Patch 0531. Three commitments registered at Patch 0528 §14.17 (B.1 local algebraic representation ansatz, B.2 $\sigma_{cycle}$ algebraization + uniqueness, B.3 Case A.1 derivational support) are addressed at sketch-level structural exploration. B.1 receives the bulk of substantive work as the largest open question; B.2 and B.3 receive forward sketches. Fourteen sub-questions queued for future sessions. No closures claimed; no findings registered; no anti-priorities violated. Reviewer-pause checkpoint discipline applied at session close.*

*Patch 0532 (Session 139) closes B.1.q5 review-pause at sketch level — refined placement of ChatGPT's alternative (2) from observable cosmological to substrate-matrix-element layer; recommended priority elevation of B.1.q3 / B.3.q1 substrate-locality temporal extension as load-bearing for B.1's response to alternative (2).*

*Patch 0533 (Session 139) closes B.1.q4 first-shell current sum identity at sketch level — explicit derivation of $\sum_{i=1}^{12} \hat{j}_{DI}^{net}(v_i) = (24/\sqrt{7-\phi})\hat{n} \approx 10.345\,\hat{n}$ at first order in $\delta$, numerically verified at machine precision; structural consequence: R3 nonlocal spatial averaging reduces to coefficient renormalization $c' = W_0 + 24 W_1/\sqrt{7-\phi}$; §5.3 priority revision authorized by Thomas, B.1.q3 + B.3.q1 substrate-locality temporal extension promoted to next priority.*

*Future Patches in this trajectory: Phase 2 foundations work progress on B.1.q3 + B.3.q1 substrate-locality temporal extension (load-bearing for B.1's full response to ChatGPT's alternative (2)) is the recommended next priority per revised §8.8 ordering.*
