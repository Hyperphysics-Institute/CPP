# Methods Catalogue

**Status:** STUB seed at Session 133 Patch 0449. Initial entries from Reading C closure trajectory (Patches 0417-0443) plus references to earlier work + Session 134 audit additions Patch 0464; **19 entries (7 L1 + 8 L2 + 4 L3)** carrying METH-L{1,2,3}-NNN identifiers per naming convention adopted Patch 0449a. Full catalog completion is OPEN-ORG-016 (Phase 1 back-fill + Phase 2 per-paper-SHIP + Phase 3 per-session). **Audit-trail of recent additions/removals**: The Patch 0460 additions (METH-L2-007 + METH-L2-008 + METH-L3-007) were reversed at Patch 0461 as out-of-scope (organizational/protocol patterns belong in `templates/operating_system.md`, not the physics methods catalogue); the pre-existing organizational entries METH-L3-004 (Closure trajectory saturation → consolidate via handover + outline) + METH-L3-006 (Meta-conversation surfacing → capture before window close) were removed at Patch 0462 per the explicit physics-derivation-only scope; the METH-L2-007 and METH-L2-008 slots were **refilled with physics-scoped Layer 2 entries at Patch 0464** from the Session 134 Tier-4 audit (delayed §15 Step E run on the Patch 0458 backfill per the Patch 0463 dual-trigger codification): METH-L2-007 (Magnitude-level vs mechanism-level unification distinction) + METH-L2-008 (Substrate-foundational vs substrate-derived FI distinction). METH-L3-007 slot remains vacated for physics-scoped future entries.

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

---

## Layer 3 — Heuristic strategies

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

**Example deployment.** n_s = 0.9649: the tilt needed a thermalized early occupation bath (μ ∝ ln n̄). Rather than add an "early plasma is thermal" axiom, the constraint (a symmetric constant-rate process whose stationary measure is the indistinguishable-Gibbs product-Poisson, giving p = 2) was extracted, then realized by the existing PCD/ZBW dynamics on the 600-cell — identified as a zero-range process for which relaxation is a theorem. Thermalization became emergent, not axiomatic. Anticipated applications: any CPP result that looks like it needs a bespoke initial-condition or property axiom — extract the structural constraint first, attempt a primitives-only mechanism, register a new axiom only if the attempt genuinely fails.

**End of seed catalog.** Total entries: 7 Layer 1 (METH-L1-001 through METH-L1-007) + 8 Layer 2 (METH-L2-001 through METH-L2-008) + 5 Layer 3 (METH-L3-001, METH-L3-002, METH-L3-003, METH-L3-004, METH-L3-005) = **20 entries**. METH-L3-004 was refilled at Patch 0780 with a physics-scoped derivation-strategy entry (the slot was vacated at Patch 0462 and reserved for physics-scoped use; this entry honors that reservation). Numbering slots METH-L3-006 and METH-L3-007 remain vacated (Patch 0462 / Patch 0461) and reserved per the naming-convention rule that numbers are not reused once assigned — future METH-L3-006 and METH-L3-007 entries must be *physics-scoped*. The METH-L2-007 and METH-L2-008 slots were refilled with physics-scoped entries at Patch 0464 from the Session 134 Tier-4 audit. Full catalog completion (back-fill from earlier closure arcs: SF-4, SS-9, SM-line, EW-line) queued as OPEN-ORG-016.
