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

*This sketch opens Phase 2 foundations work (Phase 2.5 of F.1 trajectory) at Session 139 Patch 0531. Three commitments registered at Patch 0528 §14.17 (B.1 local algebraic representation ansatz, B.2 $\sigma_{cycle}$ algebraization + uniqueness, B.3 Case A.1 derivational support) are addressed at sketch-level structural exploration. B.1 receives the bulk of substantive work as the largest open question; B.2 and B.3 receive forward sketches. Fourteen sub-questions queued for future sessions. No closures claimed; no findings registered; no anti-priorities violated. Reviewer-pause checkpoint discipline applied at session close.*

*Future Patches in this trajectory: Phase 2 foundations work progress on B.1.q5 (review-pause on layered disambiguation) and B.1.q4 (first-shell current sum identity) is the recommended next priority per §5.3.*
