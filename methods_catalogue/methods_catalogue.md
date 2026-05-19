# Methods Catalogue

**Status:** STUB seed at Session 133 Patch 0449. Initial entries from Reading C closure trajectory (Patches 0417-0443) plus references to earlier work; **17 entries (7 L1 + 6 L2 + 4 L3)** carrying METH-L{1,2,3}-NNN identifiers per naming convention adopted Patch 0449a. Full catalog completion is OPEN-ORG-016 (Phase 1 back-fill + Phase 2 per-paper-SHIP + Phase 3 per-session). The Patch 0460 additions (METH-L2-007 + METH-L2-008 + METH-L3-007) were reversed at Patch 0461 as out-of-scope, and the pre-existing organizational entries METH-L3-004 (Closure trajectory saturation → consolidate via handover + outline) + METH-L3-006 (Meta-conversation surfacing → capture before window close) were removed at Patch 0462 per the explicit physics-derivation-only scope clarified at `README-methods_catalogue.md`: this catalog covers *physics derivation methods* only; protocol patterns and workflow heuristics live in `templates/operating_system.md` (or `relationship_protocol.md` / `founders_voice/` / `opus_voice/` as appropriate).

**Format:** Each entry has *Name* / *Description* / *Canonical citation* / *Example applications*. Layered as Layer 1 (mathematical techniques) → Layer 2 (methodological disciplines) → Layer 3 (heuristic strategies). The three layers are independent inventories, not a strict hierarchy; cross-layer references appear inline.

---

## Layer 1 — Mathematical techniques

### METH-L1-001: Schur orthogonality for cage-shell averaging

**Description.** Average a tensor operator over a finite group's irreducible representations using Schur orthogonality relations to extract the irrep-specific projection magnitudes. Reduces cage-shell averaging to evaluation of $d_{\text{irrep}}/|G|$ for the relevant 2D irreps.

**Canonical citation.** Capotauro v1.0 §10 (`flagship_papers/capotauro/capotauro.tex`), Patch 0397 THEO-CAP-1 derivation step 8.

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

**Canonical citation.** Patch 0424 §13 local-$I_h$-preservation verification (`flagship_papers/capotauro/code/sketch_section_13_local_ih_preservation.py`).

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

**End of seed catalog.** Total entries: 7 Layer 1 (METH-L1-001 through METH-L1-007) + 6 Layer 2 (METH-L2-001 through METH-L2-006) + 4 Layer 3 (METH-L3-001, METH-L3-002, METH-L3-003, METH-L3-005) = **17 entries**. Numbering slots METH-L3-004 and METH-L3-006 vacated at Patch 0462 (organizational entries removed per the explicit physics-derivation-only scope of `README-methods_catalogue.md`); slots remain reserved per the naming-convention rule that numbers are not reused once assigned — future METH-L3-004 and METH-L3-006 entries must be *physics-scoped*. Full catalog completion (back-fill from earlier closure arcs: SF-4, SS-9, SM-line, EW-line) queued as OPEN-ORG-016.
