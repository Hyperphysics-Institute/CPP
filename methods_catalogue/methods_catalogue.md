# Methods Catalogue

**Status:** 29 entries (12 L1 + 11 L2 + 6 L3) as of **Patch 1133** (SR-2 pre-draft C14 audit of the spin-2/op:einstein arc, Patches 1107–1130: +5 L1, +2 L2, +1 L3 filling the reserved METH-L3-006 slot; footer count corrected — see footer note). Previously: STUB seed at Session 133 Patch 0449 from the Reading C closure trajectory (Patches 0417-0443) + Session 134 audit additions Patch 0464 + METH-L2-009 at Patch 0540 + METH-L3-004 refill at Patch 0780. Naming per the METH-L{1,2,3}-NNN convention adopted Patch 0449a. Full catalog completion is OPEN-ORG-016 (Phase 1 back-fill + Phase 2 per-paper-SHIP + Phase 3 per-session). **Audit-trail of recent additions/removals**: The Patch 0460 additions (METH-L2-007 + METH-L2-008 + METH-L3-007) were reversed at Patch 0461 as out-of-scope (organizational/protocol patterns belong in `templates/operating_system.md`, not the physics methods catalogue); the pre-existing organizational entries METH-L3-004 (Closure trajectory saturation → consolidate via handover + outline) + METH-L3-006 (Meta-conversation surfacing → capture before window close) were removed at Patch 0462 per the explicit physics-derivation-only scope; the METH-L2-007 and METH-L2-008 slots were **refilled with physics-scoped Layer 2 entries at Patch 0464** from the Session 134 Tier-4 audit (delayed §15 Step E run on the Patch 0458 backfill per the Patch 0463 dual-trigger codification): METH-L2-007 (Magnitude-level vs mechanism-level unification distinction) + METH-L2-008 (Substrate-foundational vs substrate-derived FI distinction). METH-L3-007 slot remains vacated for physics-scoped future entries.

**Format:** Each entry has *Name* / *Description* / *Canonical citation* / *Example applications*. Layered as Layer 1 (mathematical techniques) → Layer 2 (methodological disciplines) → Layer 3 (heuristic strategies). The three layers are independent inventories, not a strict hierarchy; cross-layer references appear inline.

---

## Layer 1 — Mathematical techniques

### METH-L1-001: Schur orthogonality for cage-shell averaging

**Description.** Average a tensor operator over a finite group's irreducible representations using Schur orthogonality relations to extract the irrep-specific projection magnitudes. Reduces cage-shell averaging to evaluation of $d_{\text{irrep}}/|G|$ for the relevant 2D irreps.

**Canonical citation.** Capotauro v1.0 §10 (`series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex`), Patch 0397 THEO-CAP-1 derivation step 8.

**Example applications.** K3-doublet cage-shell factor $|M_\perp^{K3}| = d_E/|I_h| = 2/12 = 1/6$ (Capotauro v1.0). W-bracelet identical factor on $D_6$ stabilizer (Finding C-W41, Patch 0427). qDP/eDP factor on $D_{5d}$ after antipodal-pair refinement (Finding C-W45, Patch 0438).

### METH-L1-002: Wigner-Eckart factorization

**Description.** Factor a matrix element $\langle f | \hat{O} | i \rangle$ where $\hat{O}$ transforms as a definite irrep of the symmetry group, into a geometric Clebsch-Gordan coefficient times a reduced matrix element. Used here to factor cross-sector matrix elements into (chirality-coupling factor) × (cage-shell factor).

**Canonical citation.** Standard quantum-mechanical textbook (Sakurai); applied in CPP at Capotauro v1.0 §5.3-§5.4.

**Example applications.** K3-doublet $|M^{K3}|$ factorization (Capotauro v1.0). W-bracelet $|M^W|$ factorization on $E_2 \oplus E_1$ in $D_6$ (Finding C-W43, Patch 0429). qDP/eDP $|M^{qDP}|$ factorization on $A_{1g} \oplus A_{2u}$ in $D_{5d}$ (Finding C-W46, Patch 0439).

### METH-L1-003: Branching rule analysis ($G \downarrow H$)

**Description.** Decompose irreps of a group $G$ into irreps of a subgroup $H \subset G$. Used to track how chirality operators transform under sector-specific stabilizer subgroups.

**Canonical citation.** Standard representation theory; applied in CPP at sketch §17.10 (W-bracelet $E_2 \oplus E_1$ in $D_6$ via $I_h \downarrow D_6$ branching).

**Example applications.** qDP/eDP $A_u(I_h) \downarrow A_2(C_{5v})$ branching (sketch §19, Patch 0438). $D_{5d}$ chirality operator $A_{2u}$ identification (sketch §20, Patch 0439).

### METH-L1-004: Coxeter parabolic-subgroup theory

**Description.** Use Coxeter group structure to identify which subgroup-fixed subspaces of a Coxeter polytope contain the chirality-bearing direction. Applied here to identify $H_3 = I_h$ as the vertex-aligned stabilizer of $\hat{n}$ in $H_4$.

**Canonical citation.** Humphreys, *Reflection Groups and Coxeter Groups*; applied in CPP at sketch §11-§12 (Patch 0417).

**Example applications.** Q1+Q2 closure identifying $\hat{n}$ stabilizer as $H_3 = I_h$ (Patch 0417).

### METH-L1-005: Antipodal-pair refinement of stabilizers

**Description.** When a 1-vertex framing produces a vanishing matrix element, refine the substrate object's effective stabilizer by pairing the vertex with its antipode, producing a larger stabilizer ($D_{nd}$ rather than $C_{nv}$) that supports non-vanishing irrep content.

**Canonical citation.** sketch §20 (Patch 0439), introduced in qDP/eDP Q6-PAIRING resolution.

**Example applications.** qDP/eDP $C_{5v}$ → $D_{5d}$ refinement (sketch §20). Anticipated for future manifestations (iv)+(v) closures.

### METH-L1-006: Combined-symmetry generators extending purely-geometric ones

**Description.** When a substrate sector has additional internal degrees of freedom beyond geometric structure (e.g., qCP sign, time direction), the $\zeta$ generator that produces non-vanishing matrix elements may need to combine geometric inversion with operations on the internal degrees. CP combines spatial inversion with charge conjugation.

**Canonical citation.** sketch §20.4-§20.5 (Patch 0439), introduced for qDP/eDP $\zeta^{qDP} = $ host-CP-centered spatial inversion + $\hat{n}$-flip + qCP-sign flip.

**Example applications.** qDP/eDP Q6-PAIRING resolution (Patch 0439). Anticipated extension for manifestations (iv) thermodynamic causal arrow (likely incorporates time-direction reversal) and (v) cosmological-vacuum asymmetry (likely incorporates cosmological-epoch sign).

### METH-L1-007: Numerical verification at machine precision

**Description.** When a derivation depends on a geometric identity (e.g., 4D edge tangency, dot product evaluation), implement the geometry numerically and verify the claimed identity holds to $< 10^{-9}$. Catches geometric errors that purely symbolic reasoning misses.

**Canonical citation.** Patch 0424 §13 local-$I_h$-preservation verification (`series_umbrella/series_substrate_chirality_arc/capotauro/code/sketch_section_13_local_ih_preservation.py`).

**Example applications.** §13 §12 geometric error caught and corrected (Finding C-W39 supersedes C-W38, Patch 0424). Q1' vertex-alignment verification (Patch 0418-0419).

### METH-L1-008: Little-group helicity classification of lattice mode content

**Description.** To determine whether a lattice field theory can carry a mode of given helicity, classify the per-site degrees of freedom under the little group SO(2) about the propagation direction $\hat{k}$, then confirm with the explicit dynamical matrix $D(k)$: the helicity content of the propagating branches is fixed by the *representation* of the carried data, not by the couplings (couplings set dispersions only). A helicity-$\pm h$ mode requires an $e^{\pm ih\theta}$ basis vector in the per-site space; if absent, no choice of couplings produces it. Converts "can the substrate carry X" questions into finite representation-theory checks.

**Canonical citation.** Spin-2 Step 5 emergent-graviton verdict (`series_relativity/op_einstein_closure/spin2_construction/1116_step5_emergent_graviton_verdict.md` + `code/1116_step5_emergent_graviton_modes.py`, Patch 1116); helicity decomposition first deployed at Patch 1109 (`op_einstein_closure/1109_stepA_helicity2_gap.md`).

**Example applications.** Scalar+vector LSP on the 600-cell: branches $\{0,0,\pm1\}$ for ANY couplings — no emergent helicity-2, forcing the spin-bit axiom (Patch 1116). Scalar+gradient-of-vector metric map cannot source $h_{xx}-h_{yy}$, $h_{xy}$ (Patch 1109). Reusable for any future "does the substrate support mode X" question (e.g., candidate dark-sector carriers).

### METH-L1-009: Spherical-design moment annihilation in shell-sums

**Description.** Convert a physics question about a lattice shell-sum (what survives, what cancels, what operator emerges in the continuum) into a pure question about the shell's spherical-design degree. The icosahedral 12-neighbor shell of the 600-cell is a spherical 5-design: $\sum \hat{v} = 0$ (monopole annihilated exactly), $\sum \hat{v}\hat{v}^\top = 4I$ (quadrupole exactly isotropic), all angular moments exact through degree 5, first anisotropy at degree 6. Consequences extracted by this method: the shell-sum Laplacian is exact at leading order; the operator is rank-agnostic (acts component-wise on any broadcast tensor); per-edge rotation sums evaluate in closed form.

**Canonical citation.** Shell-sum monopole annihilation (`series_relativity/op_einstein_closure/1108_stepBprime_shellsum_monopole.md` + `code/`, Patch 1108).

**Example applications.** Absolute-$|SSV|$ monopole annihilated exactly ⇒ inert uniform Sea at leading order (Patch 1108). $l=2$ fully resolved and orthogonal to $l=0,1$ on the shell (Patch 1112). Rank-agnostic propagation $\Box Q_{ij}$ = same operator as scalar/vector (Patch 1113). Closed-form gap $\sum R_j(\theta) = (8\cos\theta+4)I$ in the connection re-run (Patch 1119). Side-prediction: degree-6 anisotropic gravity correction (frontier flag, Patch 1108).

### METH-L1-010: Discrete per-edge connection formalization (antipodal-consistent transport)

**Description.** To test a "the hop turns the data" mechanism rigorously, formalize it as a discrete connection: a per-edge transport $R_j$ acting on the carried components, with (i) antipodal consistency $R_{-j} = R_j^\top$ (round trip = identity; required for Hermiticity of the dynamical matrix), (ii) the equivariant family constructed from the only per-edge vector available ($R_j(\theta)$ = rotation about $\hat{n}_j$), and (iii) a generality backstop of random antipodal-consistent draws so the conclusion does not hinge on equivariance. Key analytic outputs: the $k=0$ gap formula ($M = 4|\sin(\theta/2)|$ Planck masses for the icosahedral shell) and the $O(k)$ chiral (circular-birefringence) term $\propto \sin\theta\,[k]_\times$, which is m-diagonal (cannot raise helicity rank).

**Canonical citation.** Spin-2 Step 6 third assault (`series_relativity/op_einstein_closure/spin2_construction/1119_step6_nonradial_connection_rerun.md` + `code/1119_step6_connection_covariant_modes.py`, Patch 1119).

**Example applications.** The non-radiality/PSR-hop twist: any data-acting twist Planck-gaps the field (empirical $\theta < 10^{-46}$–$10^{-51}$), forcing flat absolute-frame carriage — the Nexus frame revealed as load-bearing (Patch 1119). The chiral $O(k)$ term as a substrate-chirality order parameter with a known empirical ceiling (cross-lane hook, fenced).

### METH-L1-011: Conservation-identity far-field reduction (ADAPTED from standard GR radiation theory)

**Description.** Source a radiative field by the *local* stress (origin-independent, point-perceivable) rather than by a global multipole density, and let the multipole emerge in the far field through the conservation identity $\int T_{ij}\,d^3x = \tfrac{1}{2}\ddot{M}_{ij}$; mass conservation kills the monopole, momentum conservation the dipole. Companion theorem (constraint inheritance): retarded solutions of $\Box\bar{h}_{\mu\nu} = -\lambda T_{\mu\nu}$ with $\partial^\mu T_{\mu\nu}=0$ satisfy the harmonic constraint automatically. The CPP adaptation anchors the conservation laws in substrate bookkeeping (CP-count conservation; displacement-rule momentum) rather than in diffeomorphism invariance, and uses the identity chain to convert design constraints into theorems (statics: perfect-fluid $T^{TF} \equiv 0$; tensor virial for bounded static systems).

**Canonical citation.** Task 3 coupling derivation (`series_relativity/op_einstein_closure/spin2_construction/1124_task3_coupling_quadrupole_formula.md` + `code/1124_task3_quadrupole_verification.py`, Patch 1124); constraint inheritance at Task 4 (Patch 1125).

**Example applications.** The origin-dependence defect of C4 v0.1 caught and repaired (source = traceless local stress; Patch 1124). $\lambda = 16\pi G/c^4$ at zero new parameters; no-dipole upgraded from evidential leg to derived consequence (Patch 1124). The TT-only response cancellation inherits via one-metric + one-conserved-source (Patch 1125).

### METH-L1-012: Protected-content enumeration via irrep dimension bound (ADAPTED from METH-L1-003)

**Description.** To determine which angular-momentum content a lattice point group protects *intact*, combine the branching table ($SO(3) \downarrow G$, per METH-L1-003) with the dimension bound: $D^{(l)}$ can descend irreducibly only if $2l+1 \le \dim$(largest irrep of $G$). For the icosahedral group (largest irrep $H$, dim 5): intact $l$-values are exactly $\{0,1,2\}$, permanently ($2l+1 \ge 7$ for $l \ge 3$). The bound converts a finite branching computation into a *termination theorem* — the protected ladder provably ends, licensing "completion, not increment" claims about packet content.

**Canonical citation.** Task 2 completion theorem (`series_relativity/op_einstein_closure/spin2_construction/1123_task2_axiom_text_A3prime.md` + `code/1123_task2_completion_check.py`, Patch 1123); registered as THEO-SR-EIN-1 (Patch 1130).

**Example applications.** LSP′ = $A \oplus T_1 \oplus H$ = 9 = the lattice's full protected content; no fourth rung (Patch 1123). The icosahedral-vs-cubic discriminant: under $O$, $l=2 \to E \oplus T_2$ (splits 2+3), under $I$, $l=2 \to H$ intact — the basis of PRED-O-37's lattice-discriminant falsifier (Patch 1120).

### METH-L1-013: Registration-level response-order counting

**Description.** To decide the order at which a suppression constant enters a response function, ask first at what LEVEL the constant is REGISTERED — amplitude (per-vertex matrix element) or probability (per-process) — then count vertex insertions in the response's structure under hermiticity (perceive-side and source-side legs of the same channel operator equal in magnitude). The order is then forced: a two-insertion polarization carries the *square* of an amplitude-registered constant; alternative orders require either re-registering the constant at a different level or asymmetric legs — both contradictions of registered structure, making the excluded orders NOT CONSTRUCTIBLE rather than merely disfavored. Extension: the same registration audit answers tensor-character questions — the registered datum's convention parity (e.g. a $\zeta$-ODD operator placement, sign convention-relative) combined with the registered transport structure fixes what a vertex sources under composition, with the excluded composition classes carrying the same not-constructible status.

**Canonical citation.** SS43-Q4a response-order derivation (`series_phenomena/cosmology/dark_matter/code/2399_ss43_q4a_response_order.py` + `reasoning/2399.md`, Patch 2399).

**Example applications.** The linear-vs-$\sqrt{\chi}$ gap order (Patch 2399: $\Pi_{\rm res}/\Pi_{\rm color} = \chi^2$, $R_s = 25.42$ fm in-demand; $\sqrt{\chi}$ excluded by registration). The vertex-class derivation (Patch 2401: Class S excluded — an unsigned per-unit source requires probability-level registration or a $\zeta$-EVEN operator, both contradicting the datum; Class V-t derived). The Q4c protected/residual decomposition (Patch 2403, the 2400 handover's named recurrence trigger — this entry registered catalog-first at that session): first order exactly protected for every closure-preserving configuration; the residual enters at second order through closure-breaking virtual states.

---

## Layer 2 — Methodological disciplines

### METH-L2-001: Layer A/B/C epistemic decomposition

**Description.** Decompose a derivation into Layer A (CPP-derived content), Layer B (imported formalism whose CPP-derivation is open), Layer C (empirical inputs). The decomposition makes the load-bearing inputs explicit so each can be audited independently.

**Canonical citation.** SM-3 K3/Koide work (Sessions 14-22), applied programme-wide.

**Example applications.** THEO-CAP-1 audit: Layer A = chirality matching + cage-shell averaging; Layer B = Wigner-Eckart formalism (registered as OPEN-SS-16); Layer C = empirical $\Delta p_{LR}$ value.

### METH-L2-002: Register-then-resolve discipline

**Description.** When an analytical complication surfaces during a closure attempt, register it explicitly as a sub-question (with letter ID, e.g., Q5-PAIRING, Q6-PAIRING) and defer its resolution to a dedicated patch rather than trying to resolve it under deadline pressure within the active patch.

**Canonical citation.** sketch §16.12 (Patch 0428), §21.6 (Patch 0441). Pattern formalized at sketch §16.12 from prior occurrences.

**Example applications.** Q5-PAIRING registered Patch 0428, resolved Patch 0429. Q6-PAIRING registered Patch 0438, resolved Patch 0439. Q7 scoping at Patch 0441 applied this discipline at scoping level (four sub-questions Q7.1-Q7.4 registered without forced closure attempts).

### METH-L2-003: Three converging arguments standard for Layer 2 closures

**Description.** A Layer 2 closure (structural argument, not yet full Layer 3 rigor) is registered as adequate when three structurally independent arguments converge on the same identification. Single arguments are tentative; three converging arguments are load-bearing.

**Canonical citation.** Patch 0419 Q1'+Q1'.A resolution (three converging arguments for vertex-aligned reading: paper-internal hosting language + cross-sector unification with SF-2 + SM-1 first-shell preservation).

**Example applications.** Q1' vertex-alignment resolution (Patch 0419). Anticipated for Q7.1 substrate-level sign-selection mechanism when assessed against CPP axioms.

### METH-L2-004: Symmetric-honesty discipline

**Description.** Apply the same epistemic standards to own work as to reviewer feedback. If you would push back on a reviewer claiming a Layer 2 result is Layer 3, push back equally hard when tempted to claim your own Layer 2 work is Layer 3.

**Canonical citation.** `founders_voice/004_verbatim_substance_preservation_discipline.md`. Originated from Session 132 reviewer-suspension event (Grok vocabulary contamination).

**Example applications.** §13 §12 geometric error preservation as substantive correction rather than silent fix (Patch 0424). Q5-PAIRING and Q6-PAIRING explicit registration rather than glossing.

### METH-L2-005: Cross-sector unification audit

**Description.** When a result is derived for one sector, audit whether sister sectors inherit the result structurally. The audit operates at two levels — mechanism-level (do sister sectors share the same closure pattern?) and magnitude-level (do they produce identical numerical magnitude?).

**Canonical citation.** sketch §14 Finding C-W40 (Patch 0425) for mechanism-level. sketch §20.14 (Patch 0439) for magnitude-level.

**Example applications.** Reading C closure trajectory itself — K3-doublet result audited and found to extend to W-bracelet (THEO-SD-CHIR-1) and qDP/eDP (THEO-SD-CHIR-2).

### METH-L2-006: Three-step closure pattern

**Description.** Cross-sector closures under the OPEN-SD-CHIR-PRIMITIVE umbrella follow a uniform three-step pattern: (i) substrate-locality at Layer 2 with sector-specific stabilizer identified; (ii) cage-shell factor at Layer 3 via Schur orthogonality on the stabilizer; (iii) pairing-convention identification at Layer 3 via sector-specific $\zeta$ generator.

**Canonical citation.** Patches 0429 (K3/W) + 0439 (qDP/eDP). Formalized at sketch §19.11 + §20.14.

**Example applications.** All three Reading C closure trajectory manifestations followed this pattern. Anticipated template for manifestations (iv)+(v).

### METH-L2-007: Magnitude-level vs mechanism-level unification distinction

**Description.** Cross-sector unification claims come in two kinds with different rigor levels. *Mechanism-level unification* claims that all manifestations inherit from the same primitive (e.g., Substrate-Locality Unification: all chirality manifestations inherit from primitive direction $\hat{n}$ via the Substrate-Locality Theorem); achievable at Layer 2 via substrate-locality argument. *Magnitude-level unification* claims that the unified parent produces identical numerical content across structurally distinct sector mechanisms with distinct generators (e.g., three-way unification $|M^{K3}| = |M^W| = |M^{qDP}| = \chi/6 \approx 0.0394$ via parallel three-step closure pattern on shared icosahedral cage with structurally distinct stabilizers $D_{3d}/D_6/D_{5d}$ and distinct $\zeta$ generators); requires Layer 3 sector-specific cage-shell factor + pairing-convention identification closure work per sector. The two claims are structurally distinct: mechanism-level is necessary but not sufficient for magnitude-level. Distinguishing them is methodologically important for articulating cross-sector unification at appropriate rigor and avoiding overclaim — mechanism-level unification (everyone inheriting from same parent) is often achievable cheaply via substrate-locality arguments; magnitude-level unification (everyone producing the same number) requires sector-specific Layer 3 closure work and is the rigor target. The distinction also clarifies what counts as substantive cross-sector progress: a mechanism-level result reached after a magnitude-level result is already in hand is a structural backfill of an already-stronger claim; a magnitude-level result reached after only mechanism-level is the substantive cross-sector rigor advance.

**Canonical citation.** Capotauro v2.0 §13.2 (Patch 0454, Session 134); pattern surfaced from the Reading C closure trajectory work spanning Finding C-W40 (mechanism-level Substrate-Locality Unification at Patch 0425, Session 130) through Patches 0427–0439 (magnitude-level $\chi/6$ across three sectors at Layer 3).

**Example applications.** K3 + W + qDP/eDP three-way magnitude-level unification in Capotauro v2.0 (the canonical instance — three structurally distinct sectors with distinct $\zeta$ generators producing identical $\chi/6$). Templates future closure work for OPEN-SD-CHIR-PRIMITIVE umbrella manifestations (iv) thermodynamic causal arrow and (v) cosmological vacuum asymmetry — mechanism-level extension may be achievable by analogous substrate-locality argument, but magnitude-level claim requires sector-specific Layer 3 closure work per manifestation. Applies generally to umbrella-class cross-sector targets in future flagship work where multiple manifestations share an underlying primitive but the question of whether they produce identical numerical content is separately decidable.

### METH-L2-008: Substrate-foundational vs substrate-derived FI distinction

**Description.** Foundational inputs come in two epistemic classes by provenance. *Substrate-foundational FIs* are postulated at the level of the substrate's primitive features — at the same epistemic footing as the substrate's existence postulate itself (e.g., FI-C-RC-1 primitive 4D direction $\hat{n}$ in ambient $\mathbb{R}^4$ where the 600-cell substrate sits; FI-C-RC-2 vertex-aligned reading $\hat{n} = v_{\text{host}}$ established at Layer 2 via three converging arguments). Their first-principles closure is open work at the deepest Layer 3 promotion target (e.g., Q1$'$+Q1$'$.A for FI-C-RC-1/RC-2). *Substrate-derived FIs* are derived from substrate-foundational features via structural constraints (e.g., FI-C-9 chirality magnitude $|\chi| = \phi^{-3}$ derived from FI-C-RC-1 via FI-C-RC-2 + perturbative-distance-ratio constraint; FI-C-10 cage-shell extension to chirality observables; FI-C-1 through FI-C-8 inherited from sibling flagship papers as substrate-derived). The distinction is methodologically important for pedagogical framing (substrate-foundational FIs are deep epistemic commitments requiring substantial framing; substrate-derived FIs are derivation chains presentable as structural arguments) and for v1.0 SHIP closeout deliverables (anthology chapter and 7-file documentation suite must convey the distinction to non-specialist readers without conflating what is *postulated at substrate level* with what is *derived from substrate primitives*). Distinct from METH-L2-001 Layer A/B/C epistemic decomposition: METH-L2-001 axes are derived-content / imported-formalism / empirical-inputs; METH-L2-008 is about FI provenance specifically (postulated at substrate-primitive level vs derived from substrate primitives via structural constraints). The two methods are complementary — METH-L2-001 classifies the *origin* of content used in a derivation (where it came from); METH-L2-008 classifies the *epistemic role* of a foundational input within the substrate-physics framework.

**Canonical citation.** Capotauro v2.0 §13.5 (Patch 0454, Session 134); emerges from the v2.0 FI inventory expansion from 10 v1.0 FIs to 12 v2.0 FIs at Patch 0455 §14 (FI-C-RC-1 + FI-C-RC-2 registered as substrate-foundational additions to the existing v1.0 FI-C-1 through FI-C-10 substrate-derived inventory).

**Example applications.** Capotauro v2.0 12-FI inventory (canonical instance — explicit two-class structure). Applies to FI inventory work across all flagship papers: when a paper registers new FIs, the substrate-foundational vs substrate-derived classification clarifies the epistemic role and informs the depth of pedagogical framing required at v1.0 SHIP closeout. Anticipated application: SF-2 v2.0+ work that inherits from Capotauro's substrate handles will register substrate-derived FIs grounded in Capotauro's substrate-foundational $\hat{n}$; SM-2 v2.0+ work similarly.

### METH-L2-009: Cross-target-dependency-chain in multi-question trajectory execution

**Description.** When a multi-question trajectory contains sub-question closures with structural inter-dependencies — one sub-question's resolution provides framework input to, or strengthens the structural foundation for, another sub-question's closure — the dependent pair should be sequenced as a chain (or closed together in coupled fashion within a single Patch) rather than executed as fully independent gated trajectories. The discipline operates in two phases: (1) at trajectory scoping, surface the dependency graph across all sub-question targets — which targets depend on which others, which are independent starting points; (2) at execution-priority ordering, the dependency-chained pairs are higher-priority than equally-tractable independent targets because closing the chain resolves multiple structural commitments in coupled fashion rather than serial-independent fashion. Distinct from METH-L2-002 register-then-resolve discipline (which defers analytical complications to future Patches) and from METH-L2-006 three-step closure pattern (which structures a single closure rather than sequencing across multiple closures). Distinct also from METH-L2-005 cross-sector unification audit (which checks for sister-sector inheritance after a single closure; METH-L2-009 operates at the trajectory-planning level before closures execute). The threshold for applying METH-L2-009: at least two sub-question targets with a clear structural dependency where the dependent target's closure is materially easier or more rigorous if the foundational target closes first. Below this threshold, sub-questions are treated as independent and ordered by tractability/value/risk alone.

**Canonical citation.** F.1 Layer 3 Promotion Scoping document §3 (Patch 0540, Session 139); the pattern is named and applied at the trajectory-scoping level after emerging implicitly at Patch 0534 (Session 139, sketch Layer 2 closure of B.1.q3 + B.3.q1 in coupled fashion via B.1.d ↔ B.3.Move-1 cross-commitment dependency). The Patch 0540 articulation generalizes the Patch 0534 instance from a within-Patch coupled-closure to a trajectory-scoping prioritization discipline.

**Example applications.**
- **Patch 0534 (sketch Layer 2, originating instance)**: B.1.q3 (perturbation-theory propagation rule) + B.3.q1 (Substrate-Locality Unification temporal-extension corollary) closed together within Patch 0534 because B.1.d (substrate-locality temporal extension theorem) provides the structural framework that both B.1.q3 and B.3.q1 depend on; closing them in coupled fashion was more coherent than treating as independent gated closures.
- **Patch 0540 (Layer 3 promotion scoping, generalized instance)**: Priority 1 chain identified as Target 2 (B.2.q1 framework axiomatization of $P_{TI}$ rep theory) → Target 3 (B.1.q1 matter-state $I_h$-covariance independent derivation at Layer 3). Target 3's matter-state Layer 3 work benefits from Target 2's framework axiomatization done first because matter-state irrep enumeration + Schur-orthogonality CG factor computation are easier with the $P_{TI}$ rep theory + finite-dimensional Wigner-Eckart machinery axiomatized rather than inherited from framework. The Priority 1 chain ordering elevates Target 2 → Target 3 above the equally-tractable independent Target 1 (B.1.q4 algebra) because closing the chain resolves the two strongest cross-reviewer-convergent calibration items (Patch 0538 §14.1 + §14.2) in coupled fashion rather than only one of them.
- **Anticipated applications**: future flagship trajectories opening multi-question Layer 3 promotion arcs (or analogous multi-question closure arcs at any rigor level) should examine their target dependency graph at scoping time per METH-L2-009. The pattern is not specific to F.1 or to Layer 3 promotion; it applies whenever a trajectory contains multiple sub-question closures with structural dependencies.

### METH-L2-010: Falsification-first attack ordering (cheapest kill before the summit)

**Description.** When opening an attack on a multi-part conjecture or open problem, identify the *cheapest potential falsifier* — the sub-question whose negative answer would kill the whole target at lowest cost — and run it FIRST, before investing in the hard constructive core. If the cheap kill fires, the program is saved the summit attempt; if it does not fire, the cap is narrowed and the constructive work proceeds on firmer ground. The discipline includes stating before the run what a kill would look like, so the test is genuinely armed. Distinct from METH-L2-002 register-then-resolve (which defers complications); this orders *which question to ask first* within a single attack.

**Canonical citation.** The op:einstein attack ordering — Step (b) excess-vs-absolute sourcing run before Step (a) GR-recovery, per the kickoff handover's falsification-first entry (`series_relativity/op_einstein_closure/1107_stepB_excess_vs_absolute.md`, Patch 1107).

**Example applications.** op:einstein (b): the uniform-Sea re-entry routes (source + metric background) tested first; neither fired; the cap narrowed and the (a) assault proceeded (Patches 1107–1110). Within (a): the degrees-of-freedom count (cheapest probe) run before any nonlinear analysis, localizing the summit to the helicity-2 gap (Patch 1109).

### METH-L2-011: Counterfactual-armed verification (adversarial parameter choice + documented failure mode)

**Description.** Design numerical verifications so the failure mode is *visible*, then demonstrate the test can see it: (i) choose source/parameter regimes adversarially so the channel under test is excited (a hidden channel can pass a test that never excites it); (ii) run the documented counterfactual (the assembly with the claimed ingredient removed) and exhibit the O(1) violation, proving the test's sensitivity and the ingredient's load-bearing status. A verification without a demonstrated failure mode certifies less than it appears to. Extends METH-L1-007 (machine-precision verification) from "check the identity" to "prove the check has teeth."

**Canonical citation.** Task 4 Eardley six-mode test at $e = 0.6$ (circular orbits have $\ddot{M}_{kk}=0$ and *hide* the trace channel) with the documented $\tau = 0$ counterfactual showing $2.6\times10^{-2}$ O(1)-relative breathing+longitudinal violation (`series_relativity/op_einstein_closure/spin2_construction/1125_task4_tt_response_energy.md` + `code/1125_task4_tt_response_energy.py`, Patch 1125).

**Example applications.** The $e=0.6$ test + $\tau=0$ counterfactual: a reviewer testing only circular waveforms would miss the completion's load-bearing role (Patch 1125). The eccentric energy ledger closing the operational-energy objection where it could still hide (TT flux vs full Peters $f(e)$ decay, ratio 1.000640; Patch 1127). Sister instance in the chirality lane: 400 adversarial $\eta$-dependent rules against the refined-chord bound (CAPACITY-1 closure, Patch 0828 — convergent independent deployment).

### METH-L2-012: Strict-point experimental-curve gate

**Description.** When grading a prediction against a measured exclusion curve whose value at the relevant parameter point is UNPINNED (e.g. a mass at or below the experiment's published coverage edge), grade against the STRICTEST point of the entire registered curve. The logic is deliberately one-way: a PASS at the strictest point is insensitive to the unpinned value (edge-independent, no new data pin needed); a FAIL below the published coverage edge is EDGE-CONDITIONAL and is recorded as a named pin, never promoted to an unconditional kill. The discipline prevents both false kills (over-extending a curve beyond its coverage) and false survivals (under-reading it), and separates in-coverage failures (binding) from edge-conditional ones (pinned) so a branch verdict can be rested only on the former.

**Citation.** SS43-Q3 ring-composition ladder (`series_phenomena/cosmology/dark_matter/code/2395_ss43_q3_ring_ladder.py` + campaign file §34.11 named-pin 1, Patch 2395; LZ_STRICT = 9.2e-48 gate; carried as a registration candidate at the 2396/2398 handovers with the Q4c re-confrontation as the named recurrence — fired at Patch 2402).

**Example deployment.** The 2395 branch verdict deliberately rested on DAMIC (squarely in-coverage) with the N = 4–6 LZ failures recorded edge-conditional and N = 7–8 unconditional; reused verbatim at the Q4c residual re-confrontation (Patch 2403).

### METH-L2-013: Differential-vs-total cross-section channel discipline

**Description.** For forward-peaked interactions (light mediators, range ≫ target nuclear size), assign each experimental channel the cross-section OBJECT its physics actually gates. DETECTION channels integrate the differential spectrum $d\sigma/dE_R$ above the instrument threshold, halo-folded — total σ counts the forward-peak scatters that deposit below threshold and overstates the detectable rate by orders. SHIELDING/overburden ceilings use TOTAL σ — any collision degrades kinetic energy regardless of the recoil it would deposit in a detector, so the threshold is irrelevant there. Mixing the two objects across channel types silently flips verdicts in either direction; the discipline is to declare the object per channel before computing.

**Citation.** SS43-Q3 DAMIC-shallow treatment vs rock-overburden convention (`series_phenomena/cosmology/dark_matter/code/2395_ss43_q3_ring_ladder.py` + `reasoning/2395.md` §3, Patch 2395; carried as a registration candidate at the 2396/2398 handovers with the Q4c re-confrontation as the named recurrence — fired at Patch 2402).

**Example deployment.** The 2395 DAMIC kill of the envelope end (3.4e7–1.5e8 events above the 550 eV threshold vs N90 = 123) was computable only differentially, while the same species' shielding columns were graded by total σ per the registered 1880 convention; reused verbatim at the Q4c residual re-confrontation (Patch 2403).

---

## Layer 3 — Heuristic strategies

### METH-L2-014: External-data authentication battery (independent anchors + provenance factors + block-scoped parse)

**Category:** NEW METHOD (Patch 2411; used twice in-session at Patches 2409/2410, where it caught a live wrong-number verdict).

**Statement.** When consuming an external experimental data product (a published limit curve, a digitized table, a mirrored release file), the consuming instrument must carry an authentication battery run BEFORE any verdict is trusted: (1) **independent text anchors** — at least one value quoted in the source publication's prose must be reproduced by the file (two anchors at opposite ends of the curve is the strong form); (2) **provenance factors** — the file self-identifies (registry naming convention, in-header DOI matching the registered pin, data-file name matching the analysis); (3) **cross-channel match** where available — a second independent delivery channel (e.g. a rendered-table screenshot vs the CSV export) agreeing digit-for-digit; (4) **block-scoped parsing** — parse ONLY the named observed-value block; stacked-column exports (HEPData CSV stacks each dependent variable as its own `mass,<name>` block) are a named hazard for naive row parsers; (5) **convention-agreement check** — where the registered pin admits multiple reading conventions (nearest tabulated mass vs log-interpolation), verify the verdict is convention-independent; a disagreement routes the branch to the founder undecided rather than picking one.

**Empirical basis.** Patch 2410: the first parser version mixed the HEPData CSV's stacked blocks and produced σ(9.86 GeV) = 1.13×10⁻⁴⁶ — a wrong number that would have failed the N=7 clear by a hair's-width ×1.03; the battery's screenshot-match (factor 3) and text-anchor (factor 1) checks BOTH failed and stopped the verdict pre-trust; the corrected block-scoped parse passed 11/11 with the true value 5.40×10⁻⁴⁷ (fail ×2.15, convention-independent). Patch 2409: the same battery (factors 1+2) authenticated a third-party vendored mirror of an official HEPData release file, licensing three exclusion verdicts at 10²–10⁷ margins without site access.

**Reuse condition.** Any future consumption of external experimental or observational data — direct-detection curves, PDG values pulled from secondary files, digitized figures, mirrored data releases — where the consuming patch fires a registered verdict. The battery scales: margins ≫ any transcription-error mode may relax factor 3; verdicts within ~one order of the read value make the full battery mandatory.

### METH-L3-001: Vanishing matrix element → look for combined-symmetry generators

**Description.** When a matrix element computation produces zero under a naive choice of $\zeta$ generator (typically purely-geometric inversion), the resolution is usually identification of a combined-symmetry generator that incorporates additional substrate degrees of freedom beyond the geometric ones.

**Citation.** sketch §20.4-§20.5 (Patch 0439). Heuristic identified retroactively from qDP/eDP $\zeta^{qDP}$ combined CP identification.

**Example deployment.** qDP/eDP Q6-PAIRING resolution.

### METH-L3-002: Sector instance → audit sister sectors

**Description.** When a structural result is derived for one sector under a programme-wide umbrella (e.g., OPEN-SD-CHIR-PRIMITIVE), immediately audit whether sister sectors inherit. The audit is cheap; the cross-sector unification it surfaces is valuable.

**Citation.** Reading C closure trajectory at scope level (Patch 0422 umbrella registration).

**Example deployment.** Patch 0425 Finding C-W40 (Substrate-Locality Unification) — K3 result audited for W-bracelet inheritance, then qDP/eDP inheritance.

### METH-L3-003: Suspicious foundational input → numerical verification at machine precision

**Description.** When a derivation depends on a foundational input whose geometric content is not obviously verified, implement the geometry numerically and check at $< 10^{-9}$. The verification often catches errors that pure symbolic reasoning misses.

**Citation.** Patch 0424 §13 verification, retroactively from §12 geometric error.

**Example deployment.** Local-$I_h$-preservation verification (Patch 0424), surfacing Finding C-W39 superseding C-W38.

### METH-L3-005: Recurring problem shape → name it and register it

**Description.** When the same analytical pattern surfaces in two or more independent contexts, give it a name (e.g., "PAIRING", "three-step closure pattern") and register it explicitly. Naming the pattern makes it reusable as a Layer 2 discipline.

**Citation.** Q5-PAIRING (Patch 0428) and Q6-PAIRING (Patch 0438) → three-step closure pattern (sketch §19.11, Patch 0438).

**Example deployment.** Both PAIRING registrations and the subsequent pattern naming.

---

### METH-L3-004: Would-be-axiom → extract the constraint, then build the mechanism (emergent-over-axiomatic)

**Description.** When a derivation appears to require a new axiom (an asserted initial condition, an assumed property, a postulated relation), do not add it. First extract the *exact mathematical structure* the answer must satisfy — the precise functional form, the integer, the symmetry, the sign — as a constraint on any acceptable mechanism. Then construct a mechanism from the *existing primitives* that produces that structure. If it can be built, the would-be axiom is demoted to an emergent consequence; the axiom list stays short and the result is correspondingly stronger. The discipline is to refuse the new axiom for as long as the primitives can be made to do the work, and only to add one when a genuine gap survives the attempt. (The complementary human↔AI division of labour that operationalizes this — one party holding the constraint, the other the substrate mechanism — is the collaboration pattern in `templates/operating_system.md`; this METH entry is the *derivation strategy* itself, which a solo derivation can also apply.)

**Citation.** The n_s spectral-index arc (Patches 0736–0778; canonical instance Patch 0755 fork "log = A1, no new axiom; bath = emergent dynamical clause," discharged via LEMMA-NS-HTHEOREM 0772 + LEMMA-NS-ZRP-DERIVE 0774). Named retroactively at Patch 0780. Reasoning narrative: `opus_voice/003_the_ns_arc_constraint_and_mechanism.md`.

**Example deployment.** n_s = 0.9649: the tilt needed a thermalized early occupation bath (μ ∝ ln n̄). Rather than add an "early plasma is thermal" axiom, the constraint (a symmetric constant-rate process whose stationary measure is the indistinguishable-Gibbs product-Poisson, giving p = 2) was extracted, then realized by the existing PCD/ZBW dynamics on the 600-cell — identified as a zero-range process for which relaxation is a theorem. Thermalization became emergent, not axiomatic. Anticipated applications: any CPP result that looks like it needs a bespoke initial-condition or property axiom — extract the structural constraint first, attempt a primitives-only mechanism, register a new axiom only if the attempt genuinely fails. **Spin-2 arc deployments (Patches 1112–1129):** (i) the *terminal branch* exercised for the first time — the primitives-only attempt genuinely failed three independent ways (METH-L3-006) and the axiom A3′ was added, demonstrating that the discipline's "only when a genuine gap survives" clause has real content; (ii) the *refusal branch* exercised within the same arc at the missing-trace crisis — the apparently-missing tenth component τ was NOT added as a second scalar d.o.f. but derived as constraint-redundant (τ = 3(h̄_tt − n̂n̂:Q), agreeing with GR to 4×10⁻¹⁹), keeping the packet at 9 (Patch 1125).

### METH-L3-006: Axiom-necessity by exhaustive route closure (the multi-assault standard)

**Description.** Before registering a new fundamental degree of freedom or axiom, close *every* no-axiom route independently, each with its own armed falsifier: (1) the **local-polynomial/composite route** (can existing fields combine locally — bilinears, gradients — to carry the needed structure at the right order?); (2) the **emergent/collective route** (does the long-wavelength effective theory of the existing content produce the mode? — classify by representation, METH-L1-008, so the exclusion holds for ALL couplings); (3) the **transport/connection route** (can the lattice's carriage of existing data — per-edge transports, METH-L1-010 — manufacture the structure?). Only when all routes are closed does the axiom acquire *necessity* status, which is a categorically stronger justification than breadth of motivation (necessity vs multi-motivation: "the justification's strength is of a different kind"). The complement of METH-L3-004: L3-004 governs the refusal-and-attempt; L3-006 specifies what a complete failed attempt looks like, licensing the addition.

**Citation.** The three assaults of the spin-2 arc: bilinears/local polynomials excluded (Patch 1115, right structure / wrong scaling — 2nd order, double frequency); emergent collective modes excluded for all couplings (Patch 1116, dynamical-matrix helicity {0,0,±1}); per-edge connection excluded three ways (Patch 1119, rank preservation + Planck gap + static-channel argument). Registered as the necessity basis of A3′ (Patch 1129).

**Example deployment.** A3′: "by necessity, not by convenience" — the registration language is licensed precisely because the three routes were closed independently before the axiom was drafted. Anticipated applications: any future would-be d.o.f. (dark-sector carriers, additional packet content) must clear the same three-route closure before registration; conversely, a single closed route does NOT license an axiom (the Weinberg–Witten evasion at Patch 1115 made the emergent route *permitted*, and 1116 still had to test whether it was *realized*).

**End of seed catalog (totals corrected and updated at Patch 1133).** Total entries: 12 Layer 1 (METH-L1-001 through METH-L1-012) + 11 Layer 2 (METH-L2-001 through METH-L2-011) + 6 Layer 3 (METH-L3-001 through METH-L3-006) = **29 entries**. *Footer-count correction note (symmetric honesty, Patch 1133):* the previous footer read "8 Layer 2 … = 20 entries" but METH-L2-009 had been added at Patch 0540 without a footer update — the pre-1133 actual count was 21 (7+9+5), not 20. METH-L3-004 was refilled at Patch 0780 with a physics-scoped derivation-strategy entry (the slot was vacated at Patch 0462 and reserved for physics-scoped use; this entry honors that reservation). **METH-L3-006 was filled at Patch 1133** with a physics-scoped derivation-strategy entry (the multi-assault necessity standard), honoring the Patch 0462 reservation; METH-L3-007 remains vacated and reserved for a future *physics-scoped* entry. The METH-L2-007 and METH-L2-008 slots were refilled with physics-scoped entries at Patch 0464 from the Session 134 Tier-4 audit. Spin-2-arc additions at Patch 1133 (SR-2 pre-draft C14 audit): METH-L1-008..012 (3 NEW + 2 ADAPTED), METH-L2-010..011 (2 NEW), METH-L3-006 (1 NEW), plus example-application updates to METH-L3-004. Full catalog completion (back-fill from earlier closure arcs: SF-4, SS-9, SM-line, EW-line) queued as OPEN-ORG-016.

**Patch 2402 additions (SS43 DM-lane carried triggers fired, catalog-first per the 2400 handover's binding note):** METH-L1-013 (registration-level response-order counting — the named METH-L1 trigger, fired on the Q4c residual-order derivation's confirmed reuse), METH-L2-012 + METH-L2-013 (the 2396/2398 carried strict-point experimental-curve gate and differential-vs-total σ disciplines — both reused by the Q4c ladder re-confrontation). Updated totals: **13 Layer 1 + 13 Layer 2 + 6 Layer 3 = 32 entries** (METH-L3-007 remains vacated and reserved).
**Patch 2654 addition (DM-lane session-close audit; discharges the Step-E deferral named at Patch 2648 §J4 — panel-adopted at 4/5, Grok minority recorded same font):** METH-L2-018 — **Instrument-construction discipline set (the J4 sextet)** — NEW, panel-directed. Six binding practices for building or modifying computational instruments: (1) every pre-registration introducing new or modified instrumentation carries a spec-to-code trace table mapping each prereg quantity to its code location; (2) every classifier states its guard dependencies and each guard is deliberately triggered in a test stage before production use; (3) every inherited engine runs a minimal semantic-control suite before production; (4) modified implementations demonstrate that the intended code path actually changed; (5) defects are tracked as CLASSES (the instrument-hazard lineage upgraded to a defect-class ledger), not only as instances; (6) periodic adversarial instrument audits at arc boundaries. Provenance: the four-member defect lineage (fixed-column 2612, borrowed-gate 2622, economy re-settle 2631/2638, sink-referential conjunct 2640) read by the panel as implemented-semantics drift the controls were racing rather than preventing. First full exercise: the C7-discriminant campaign (Patches 2649–2653: trace tables in all three verify scripts, deliberate guard triggers ×3, a clean-room second classifier implementation with 24/24 cell agreement, checkpoint-mechanism disclosure) — closed with ZERO new instrument defects, the defect-class ledger's first positive entry. Reusable in any lane that builds or inherits numerical instruments. Distinct from METH-L2-017 (which protects a union's legs at run time; L2-018 protects the instrument's construction before any run). Updated totals: **13 Layer 1 + 18 Layer 2 + 6 Layer 3 = 37 entries** (METH-L3-007 remains vacated and reserved).


**Patch 2411 addition (SS43 DM-lane session-close audit, catalog-first):** METH-L2-014 (external-data authentication battery — NEW; used at 2409/2410 where it caught a live wrong-number verdict pre-trust). Updated totals: **13 Layer 1 + 14 Layer 2 + 6 Layer 3 = 33 entries** (METH-L3-007 remains vacated and reserved).

**Patch 2619 addition (DM-lane session-close audit, catalog-first, sourced from the session's at-patch reasoning fragments per the sector capture convention):** METH-L2-015 — **Convention-pin control (reproduce-the-registered-record gate)** — NEW. When a re-derivation must inherit a convention the original record states only implicitly (e.g., which mass enters a formula), the ambiguity is resolved by a CONTROL, not by the author: every candidate convention is computed, the one reproducing the registered recorded output (within stated tolerance) is inherited, and the losing alternatives are PRINTED in the artifact so the selection is auditable. The control must pass before any new number is read; failure stops the campaign. First use: Patch 2606/2607 C1 (reduced-mass vs per-CP lag convention pinned by the recorded 0.74/0.68; the per-CP alternative printed and failing). Reusable in any re-derivation, extension, or replication against a registered record whose conventions are under-documented. Distinct from METH-L2-014 (external-data authentication): L2-014 authenticates inputs from outside the programme; L2-015 pins conventions inside the programme's own record. Updated totals: **13 Layer 1 + 15 Layer 2 + 6 Layer 3 = 34 entries** (METH-L3-007 remains vacated and reserved).

**Patch 2636 addition (DM-lane session-close audit, catalog-first, sourced from the session's at-patch reasoning fragments per the sector capture convention):** METH-L2-016 — **Baseline-exposure guard (gated readings vs own-cell instrument drift)** — NEW. When a gated quantity shares a cell with a measured instrument baseline (e.g., integrator energy drift), every reading that enters a gate is printed beside its own cell's baseline, and any reading within a declared multiple of that baseline (3× at first use) is flagged BASELINE-EXPOSED, excluded from gating, and reported raw; a struck anchor reads UNGATEABLE-AT-THIS-INSTRUMENT — neither pass nor adverse. Companion hazard class banked in-sector the same arc: BORROWED-GATE TRANSFER (a threshold licensed in one regime applied in another without a scaling check; second N3-hazard member after fixed-column/drift). First use: Patch 2623/2624 (DISC-1-2, designed from the 2622 dt-scaling diagnostic). Reusable wherever finite-dt or finite-statistics baselines coexist with thresholded verdicts. Distinct from METH-L2-015 (convention-pin): L2-015 pins an implicit convention; L2-016 protects a gate from its own instrument's noise floor. Updated totals: **13 Layer 1 + 16 Layer 2 + 6 Layer 3 = 35 entries** (METH-L3-007 remains vacated and reserved).

**Patch 2645 addition (DM-lane session-close audit, catalog-first, sourced from the session's at-patch reasoning fragments per the sector capture convention):** METH-L2-017 — **Matched-launch dt-union (identical initial data per leg)** — NEW. A dt-union verdict (agreement of an observable's class or value across two integration steps) is licensed only when every leg of the union launches from bitwise-identical initial data; any per-leg state preparation (re-settles, per-dt equilibration, "economy" legs) makes the union read initial-condition sensitivity instead of discretization sensitivity, and its disagreements convict the instrument, not the physics. Corollary banked with it: finer dt earns trust about integration error only — a fine-dt leg differing from a coarse one via a different launch state is not the more truthful leg. First use: Patch 2637/2638 (N2B-ROB-2: removing the 2611 launcher's per-leg economy re-settle converted a self-disagreeing instrument into 30/30 dt-agreements across ROB-2/ROB-3 and resolved both previously undrawn cells as dt-stable walls; the economy leg's fine-dt "captures" were initial-condition artifacts). Companion instrument-hazard member banked in-sector the same session: SINK-REFERENTIAL CLASSIFIER CONJUNCT (a classifier condition referencing a quantity that is degenerate/machine-zero in the tested limit — the Sea > 0 conjunct at η = 0 read the sign of ~10⁻¹³ residue; fourth hazard-lineage member, Patch 2640). Reusable in any dt-union, resolution-union, or mesh-refinement verdict protocol. Distinct from METH-L2-016 (baseline-exposure): L2-016 protects a gate from its instrument's noise floor; L2-017 protects a union from its legs' unequal initial states. Updated totals: **13 Layer 1 + 17 Layer 2 + 6 Layer 3 = 36 entries** (METH-L3-007 remains vacated and reserved).

**Patch 2661 addition (DM-lane session-close audit, catalog-first, sourced from the session's at-patch reasoning fragments per the sector capture convention):** METH-L2-019 — **Two-sided mechanism-discriminator holdout (frozen opposing predictions from named competitor accounts)** — NEW. When a derivation's quantitative arm fails and the failure's diagnosis surfaces a competitor mechanism, BOTH accounts are named, BOTH write their prediction for the same holdout cell (with the class line two-sided so either outcome classifies), and the predictions are frozen before the instrument runs; no catch-all "mixed" reading class is admitted (a reading that cannot fail is not a reading). First use: Patches 2656/2658 (FB-MECH-A phase-sample decoherence vs FB-MECH-B multi-mode chaotic divergence; the w=4 {1/400,1/800} discriminator fired B and killed A in one cell). Reusable wherever a registered negative leaves two live mechanism candidates and a single affordable cell separates them. Distinct from METH-L2-018 (which governs instrument construction; L2-019 governs mechanism adjudication after a tier failure) and from the C7 composite-only rule (which withholds adjudication until all arcs run; L2-019 designs a single arc whose either outcome adjudicates a mechanism class without touching any registry claim). Updated totals: **13 Layer 1 + 19 Layer 2 + 6 Layer 3 = 38 entries** (METH-L3-007 remains vacated and reserved).

**Patch 2667 addition (DM-lane session-close audit, catalog-first, sourced from the session's at-patch reasoning fragments per the sector capture convention):** METH-L2-020 — **Founder-picture validation gate (mechanism verbatim → non-negotiable formalization gate → two-strikes routing)** — NEW. When a derivation stage formalizes a founders_voice mechanism picture, the picture's own internal logic is converted into a pre-frozen validation gate the formalization must pass before any target quantity is computed (first use: G1 — the lossless limit of the iterated PSR re-radiation kernel must recover the registered inverse-square superposition, because the founder's stated fading is geometric dilution, not absorption); gate failure returns the stage once with the failure registered, and a SECOND consecutive failure closes the stage adversely (FG-NEG-KERNEL class) and routes to a founder-picture amendment — no third attempt, so the worker cannot iterate formalizations against the gate. The gate is derived from the picture, never from the target: a formalization judged against what the founder actually said, with the failure mode owned by whichever party (statement or formalization) the second strike convicts. First use: Patch 2666 (FA-SEA-GREEN charter §2 S1a/G1, from `founders_voice/kernel_psr_reradiation_2026-07-20.md`). Reusable wherever a founders_voice capture is the input to a pre-registered derivation (the S2/S3 pattern's formal successor). Distinct from METH-L2-019 (which adjudicates between two competitor mechanisms; L2-020 validates one mechanism's formalization against its own source) and from the blind-session protocol class (which hides target values; L2-020 constrains the formalization independent of any target). Updated totals: **13 Layer 1 + 20 Layer 2 + 6 Layer 3 = 39 entries** (METH-L3-007 remains vacated and reserved).

**Patch 2676 addition (DM-lane, queued-condition discharge: the 2673 handover queued this entry IF the panel sustained Q1 on the 2672 packet; sustained 5–0 at Patch 2674):** METH-L2-021 — **Envelope readout in a sign-staggered regime (magnitude-times-radius fit with band-disclosed uncertainty and staggering severed from decay)** — NEW, codified at observation grade with its own hardening battery attached. When a discrete response field is sign-staggered at lattice scale but exponentially enveloped at long range, the decay observable is the envelope of |f|·r (not f itself, whose sign oscillation defeats naive log-linear fits), extracted with the fitting window and finite-size band disclosed and folded into the quoted uncertainty; the staggered component is reported as a separate structural finding and never enters the decay constant. Codified WITH the panel's J4 conditions as the method's own robustness battery (mandatory on any promotion of a value it produces beyond observation grade): multi-window fits, Fourier-filter removal of the staggered component as an independent cross-check, and robustness against observable definition and lattice-size choices. First use: Patch 2671 (FA-SEA-GREEN S2 readout — clean exponential envelope over seven decades, ℓ = 0.091 ± 0.002 fm, in a field whose site values alternate sign; the envelope method is what made a decay length readable at all in that regime). Reusable wherever gapped-medium screening coexists with lattice-scale alternation (Friedel-type evanescent responses). Distinct from METH-L2-017 (which disciplines dt-union verdicts; L2-021 disciplines the decay observable itself) and from METH-L2-020 (which validates a kernel formalization; L2-021 reads the assembled operator's output). Updated totals: **13 Layer 1 + 21 Layer 2 + 6 Layer 3 = 40 entries** (METH-L3-007 remains vacated and reserved).
