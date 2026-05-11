# Conditional Closure Framework

**Location:** `/CPP/templates/conditional_closure_framework.md`
**Purpose:** Programme-level methodology document for conditional theorem closure, foundational input (FI) accounting, the "RESOLVED" terminology convention, and cross-sector closure as a structural pattern. The framework's first paper-level instance is SF-4 v4.2+ (Remark `rem:conditional_closure`); this document generalizes that framing to programme-wide convention.

**Adopted:** 11 May 2026 (Session 79, patch 0340) following the SF-4 v4.0 → v4.3 ChatGPT review trajectory which surfaced the need for programme-level convention on closure-level terminology and FI accounting.

**Status:** Programme convention. All future SF-line flagship papers inherit this framework by default; deviations require explicit registration in the deviating paper.

---

## 1. The conditional vs full closure distinction

A theorem-level closure in a CPP flagship paper is **conditional** when its proof depends on a named stack of foundational inputs (FIs) inherited from prior papers in the programme, plus a named subset of CPP axioms. The closure is **full** (or **derivational**) when every step of the proof traces back to CPP axioms alone — no FIs, no inheritance from prior papers.

In practice, every flagship-paper closure in CPP to date is conditional. Full derivational closure is the limit case that would obtain only if a paper were to re-derive every piece of structure it uses from CPP primitives, which would be impractical and would defeat the purpose of having a multi-paper programme with named theorems available for inheritance.

The distinction matters because **"RESOLVED" can be misread as "full closure" when the closure is in fact conditional**. A conditional theorem closure is a real and strong result — it establishes the theorem at the level of the programme's current foundation — but it is not the same epistemic claim as "derived from CPP primitives with nothing else assumed." The convention adopted here is to use "RESOLVED" with the conditional sense as the default reading and to mark exceptions explicitly.

## 2. Foundational Inputs (FIs): definition and accounting

A **Foundational Input (FI)** is a named input that a theorem-level closure inherits from an elsewhere-derived source. FIs are typically:

- **Theorems from prior papers** in the programme (e.g., the K3 Spectral Theorem from SM-3, the charged-lepton K3-vertex identification from SM-4)
- **Operational definitions** load-bearing for an earlier closure (e.g., the rigid-cage operational definition from SM-9; the unbound 3D orbital ZBW identification from the SF-4 v2.0 Picture A closure)
- **Mathematical facts** about the substrate geometry that are not produced by CPP itself (e.g., the 600-cell distance-shell structure, the irreducible representations of $S_3$, the standard $S_3 \to S_2$ branching rule)

The accounting convention for FIs:

1. **Naming.** Each FI is named with a sector prefix and a numbering scheme. For SF-4 v3.0 ($\alpha$-exponent closure), FIs are FI-$\alpha$-1, FI-$\alpha$-2, FI-$\alpha$-3, FI-$\alpha$-4. For SF-4 v4.0 (cross-sector closure), FIs are FI-K-1 through FI-K-6. The sector letter is paper-specific or campaign-specific; no programme-wide enumeration of FIs is required.

2. **Traceability.** Each FI's derivation source is named (paper citation + section or theorem reference) such that a reviewer can trace any FI back to its derivation in the named source.

3. **Load-bearing identification.** Within the 11-axiom CPP axiom set, the subset of axioms load-bearing for the closure is identified explicitly. For SF-4 v4.0, the load-bearing axioms are A1 (DI-bit exchange), A4 (substrate isotropy at vertex level), A7 (substrate-stress framework), A9 (mass-operator definition), with A1+A7+A9 most load-bearing. The remaining axioms are not used in the closure proof.

4. **Counting.** The closure's "FI count" is the total number of distinct FIs in the inheritance scope. SF-4 v3.0 has 4 FIs; SF-4 v4.0 has 6 FIs. Higher FI counts reflect more cross-sector entanglement and a wider foundational inheritance, not weaker closure.

5. **Closure boundary statement.** Every conditional theorem closure ships with an explicit closure-boundary statement: "This closure rests on [N FIs] (named: ...) plus [M CPP axioms] (named: ...). It is not a full derivational closure from CPP primitives alone." The statement is typically housed in a paper-level Remark (e.g., SF-4 v4.2's `rem:conditional_closure`).

The FI-accounting structure is the programme's primary tool for honest epistemic bookkeeping. It makes the inheritance pattern of each closure visible at the closure boundary, traceable to source, and quantifiable for cross-paper comparison.

## 3. The "RESOLVED" terminology convention

Throughout the programme, the following terminology convention applies:

| Term | Reading |
|---|---|
| "RESOLVED" (unqualified) | Conditional theorem closure within the current CPP theorem stack inheritance level. Default reading. |
| "RESOLVED at conditional theorem closure level" | Same as "RESOLVED" but with the conditional sense made explicit. Used in conclusion-adjacent sections where readers might otherwise read "full closure" into "RESOLVED." |
| "RESOLVED at full derivational closure" | The theorem is derived from CPP axioms alone, with no FIs and no inheritance from prior papers. **Rare; not used in any current flagship paper.** When used, requires explicit named justification (e.g., "the proof uses only axioms A1, A2, A4; no theorems from other papers are invoked"). |
| "PARTIAL CLOSURE" | The closure is incomplete at the theorem level; the result is structurally consistent with CPP but a load-bearing step remains an ansatz or has been deferred to a future paper. Used historically for SF-4 v1.0-v3.0 OPEN-FP-SF-4-2 status before v4.0 cross-sector closure. |
| "OPEN" | No closure attempted; the problem is registered for future work. |
| "INHERITED ANSATZ" | The result depends on an ansatz that is itself unresolved in another paper. Used for SF-4 v1.0-v3.0 K3-eigenmode identification before v4.0 cross-sector closure resolved SM-5 op:nu_id. |

The convention sets the default reading globally for each paper via a single Remark or note in the closure section. SF-4 v4.2+ uses `rem:conditional_closure` immediately after the Composite K3-Cage-Shell Coupling Theorem; future flagship papers should follow the same pattern.

**Programme practice:** never use "RESOLVED" without the conditional sense being either (a) set globally by an early Remark, or (b) made explicit at the point of use. The risk to avoid is that a reader skimming the abstract or roadmap sees "RESOLVED" and reads "full derivational closure," when the actual claim is "conditional theorem closure within the current theorem stack."

## 4. When to inherit vs when to re-derive

A theorem-level closure faces a choice at each load-bearing step: inherit the step from a prior paper (creating an FI), or re-derive the step from CPP primitives. The choice has trade-offs:

**Inherit (create FI):**
- Shorter closure proof
- Cleaner scope (the new paper closes its specific question without re-doing prior work)
- Wider inheritance scope (higher FI count)
- Closure conditional on the inherited result's own closure level

**Re-derive:**
- Longer closure proof
- Tighter scope (fewer FIs)
- More work, potentially out of scope for the current paper
- Closure independent of (and potentially stronger than) the inherited source

The default convention: **inherit when the FI is itself at theorem-level closure in its source paper; re-derive when the FI would otherwise depend on an ansatz or unresolved open problem in its source.**

The SF-4 v4.0 closure of OPEN-FP-SF-4-2 is an instance of inheritance through to the theorem level: 6 FIs, all themselves at theorem-level closure in their source papers (SM-1, SM-3, SM-4, SM-5, SF-4 v3.0). The closure is conditional but well-grounded.

In contrast, the SF-4 v1.0-v3.0 partial closure of OPEN-FP-SF-4-2 was via *ansatz inheritance* — the K3-eigenmode identification was inherited from SM-5 as an ansatz, not a theorem. That partial-closure state was honest but unstable: it depended on a result that SM-5 itself acknowledged as an open problem (op:nu_id). The v4.0 cross-sector closure resolved both simultaneously.

**Lesson registered programme-wide:** when an FI you would inherit is itself an ansatz or unresolved open problem in its source paper, the current paper's closure inherits that unresolved status. The honest framing is "PARTIAL CLOSURE" or "INHERITED ANSATZ," not "RESOLVED." The closure-level upgrade to "RESOLVED" requires either re-deriving the FI in the current paper, or closing the FI in its source paper (potentially via a cross-sector closure).

## 5. Cross-sector closure as a structural pattern

A **cross-sector closure** is a theorem-level closure in which a single derivation chain simultaneously resolves open problems in two or more distinct papers (typically in different sectors of the programme). The first cross-sector closure in CPP is SF-4 v4.0's Composite K3-Cage-Shell Coupling Theorem (THEO-SF-4-5), which resolves both OPEN-FP-SF-4-2 in SF-4 and op:nu_id in SM-5.

The structural pattern (Finding $\beta$-10 of the OPEN-FP-SF-4-2 closure campaign):

> Foundational inputs from one sector + substrate dynamics from CPP axioms + standard representation theory $\to$ structural derivation resolving open problems in both sectors.

The pattern exploits the fact that when two open problems in different papers are "tied together" (each paper's closure depending on the other), the standard outcome is that both remain conditional indefinitely. Cross-sector closure inverts this: instead of waiting for either paper to close independently, a single derivation chain that uses foundational inputs from both sectors can resolve both problems jointly.

The conditions under which cross-sector closure is feasible:

1. **The foundational inputs of one sector are sufficiently rich to determine the closure in another sector.** For SF-4 v4.0: the K3 spectrum (SM-3), neutrino identification (SM-5 prop:nu_id), K3 base structure (SM-1), 600-cell distance-shell structure, SF-4 v3.0 mass formula, and charged-lepton K3-vertex identification (SM-4) — six FIs collectively sufficient to derive both the OPEN-FP-SF-4-2 cage-shell coupling and the op:nu_id K3-eigenmode identification.

2. **The substrate dynamics from CPP axioms supply the bridge.** For SF-4 v4.0: A1+A7+A9 (DI-bit exchange + substrate stress + mass-energy) supply the rank-one perturbation $\Delta H = \epsilon_L|V_k\rangle\langle V_k|$; A4 supplies vertex-level isotropy.

3. **Standard representation theory completes the closure.** For SF-4 v4.0: the standard $S_3 \to S_2$ branching rule $\mathbf{2}|_{S_2} = \mathbf{1}_+ \oplus \mathbf{1}_-$ uniquely selects the TBM-aligned basis once the residual stabilizer is identified.

When all three conditions hold, cross-sector closure is structurally available even when neither sector can close its problem independently within its own scope.

**Candidate future cross-sector closure pairs registered in the programme:**

- **SF-2 (electroweak) $\leftrightarrow$ SM-5 OP-SM-4** — $\delta_{CP}$ derivation via the Capotauro mechanism. SF-2 would close $\delta_{CP}$ as the 8th zero-parameter neutrino-sector prediction; SM-5 OP-SM-4 would close the Capotauro mechanism at theorem level. Both currently inherit-as-open.

- **SS-corpus $\leftrightarrow$ SF-5 (strong unification flagship)** — gluon counting and confinement. The CONJ-SS-Gluon-4Vertex conjecture (that the 8-fold SU(3) gluon octet is phenomenological dressing of 4-tetrahedral-vertex bonding relationships) and the SF-5 strong-sector synthesis would close jointly.

- **SR-corpus $\leftrightarrow$ SF-6 (electromagnetism flagship)** — substrate polarization structure that lives partly in special-relativity territory and partly in EM-sector territory.

These are conjectured cross-sector closure pairs, not registered closures. The methodology is to identify the pairing, enumerate the candidate FI stack from both sides, attempt the derivation, and either close (cross-sector closure achieved) or surface an obstruction that gets registered as an open problem in either sector.

## 6. Programme practice for flagship papers

Every flagship paper after SF-4 v4.2 should:

1. **Declare closure level explicitly** in the abstract and §1.4 (What this paper delivers): use "conditional theorem closure" language with cross-reference to a paper-level Remark setting the conditional-closure framing globally.

2. **Account for FIs at the closure boundary**: enumerate FIs by name, identify the load-bearing CPP axiom subset, name the inheritance source for each FI.

3. **Use "RESOLVED" with conditional sense as default**: state once early in the paper that "RESOLVED" should be read in the conditional sense unless explicitly qualified; preserve historical narrative where v1.0-v3.x partial-closure language is accurate.

4. **Distinguish partial closure, conditional closure, and full closure** explicitly when changing the closure level of an open problem.

5. **Register potential cross-sector closure pairs** when applicable: if a paper's open problem is tied to another paper's open problem, note it as a candidate for cross-sector closure following Finding $\beta$-10 methodology.

The conditional-closure framework is paper-load-bearing through Remark `rem:conditional_closure` in SF-4 v4.2+. For future flagship papers, the equivalent remark should appear in the corresponding closure section of the paper.

## 7. Reference: SF-4 v4.x as first instance

SF-4 v4.2 (patch 0337) introduced the conditional-closure framing to the programme via Remark `rem:conditional_closure` immediately after the Composite K3-Cage-Shell Coupling Theorem in §5.7. The Remark text:

> The Composite K3-Cage-Shell Coupling Theorem closes OPEN-FP-SF-4-2 and SM-5's op:nu_id at the *conditional theorem closure* level within the current CPP theorem stack — that is, the resolution depends on the six foundational inputs FI-K-1 through FI-K-6 (all elsewhere-derived from SM-corpus and SF-4 v3.0) plus the four CPP axioms A1, A4, A7, A9 (A1+A7+A9 most load-bearing). It is not a full derivational closure from CPP primitives alone; the foundational inputs are themselves load-bearing and would each have to be re-derived from CPP primitives for the closure to ascend to full derivational level. The closure is the strongest theorem-level result achievable without re-deriving the foundational inputs — inheritance pattern consistent with the v2.0 Picture A axiomatic closure (3 FIs) and the v3.0 $\alpha$-exponent residual closure (4 FIs). **References to OPEN-FP-SF-4-2 and op:nu_id as "RESOLVED" throughout this paper should be read in this conditional sense** — i.e., resolved at the current CPP theorem stack inheritance level, not as full unconditional derivational closure.

This Remark is the canonical paper-level instantiation of the framework. Future flagship papers should produce equivalent remarks with appropriate FI count and axiom subset for their own closure scope.

## 8. Connection to the four-cycle review trajectory

The conditional-closure framework was not adopted at SF-4 v1.0 ship; it emerged through the v4.0 → v4.3 ChatGPT review trajectory. Specifically:

- **v4.0**: Closure language was "RESOLVED at theorem level" without conditional qualification. ChatGPT v4.0 review identified internal contradictions between updated and stale sections; structural fixes incorporated at v4.1.

- **v4.1**: Lemma 3.1 overclaimed exact vanishing where O(1/V^2) suppression was actual content; Theorem 5.2 overclaimed "uniquely forced" where structural selection was actual content. ChatGPT v4.1 review identified these calibration issues.

- **v4.2**: Calibration fixes incorporated; **NEW Remark `rem:conditional_closure` added globalizing the conditional-closure framing** as the answer to "what does 'RESOLVED' actually mean in this paper?" ChatGPT v4.2 review identified residual stale phrases in §1 that survived earlier cleanup waves.

- **v4.3**: Final textual consistency fixes incorporated. ChatGPT v4.3 verdict: **(a) v1.0 SHIP-ready, no further substantive edits required.**

The framework as captured in this document is the v4.2 Remark generalized to programme-wide convention. The four-cycle trajectory is itself a piece of methodological evidence: external review at scale identifies the conditional-vs-full closure distinction as the critical interpretive lens. Internal review tends to elide the distinction because the framework's authors hold the FI accounting in their head implicitly. External readers do not, and they correctly identify "RESOLVED" without qualifier as a potential overclaim.

## 9. Forward applications

The conditional-closure framework applies to all future flagship papers in the SF-line. For each new flagship:

- The closure-level statement in §1.4 should match the framework's terminology.
- The paper-level Remark setting the conditional-closure framing should appear in the closure section.
- The FI accounting should be enumerated explicitly at the closure boundary.
- If the paper enables a cross-sector closure (resolving an open problem in another paper jointly), the methodology of Finding $\beta$-10 should be invoked and the cross-sector closure narrative registered both in the paper and in the programme registries (`theorem-registry.md`, `paper_catalog.md`, `Research_Frontier.md`).

The framework is also retroactively applicable to existing closed flagship and series papers. Where a prior paper uses "RESOLVED" without the conditional sense made explicit, future revisions can add the conditional qualifier without changing mathematical content — the framework adds epistemic precision, not new theorems.

---

**Related programme documents:**
- `theorem-registry.md` — formal registration of theorems by ID; counts (THEO-* / PROP-* / LEMMA-* / CORL-*) reflect this framework's conditional-closure conventions.
- `theorem-dependency-graph.md` — programme-level theorem dependency map; conditional closures show their FI dependencies and downstream theorems.
- `templates/operating_system.md` § Binary Artifact Workflow — companion infrastructure document for paper-compilation discipline.
- `axiom-registry.md` — formal CPP axiom set; load-bearing subsets are identified per-closure in this framework.

**Maintenance cadence:** This document is updated when a new closure pattern emerges that the framework does not yet describe (e.g., a second cross-sector closure that surfaces methodological variations). The v1.0 of this document is canonical; future revisions are appended as a CHANGELOG section at the bottom rather than rewritten in place.
