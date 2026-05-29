# THEO-CHIR-AUDIT-1: Scope and Precondition-Gap Inventory

**Working sketch document — Tier-4 reasoning capture per CPP four-tier documentation discipline.**

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_audit/sketches/theo_chir_audit_1_scope.md`

**Status:** Patch 0630 — scope-and-precondition sketch. The audit artifact itself (`theo_chir_audit_1.tex`) is registered for Patch 0631+ (Session 148) once the precondition gaps inventoried below are either cleared or accepted as work to be done in the audit's first §.

**Purpose:** Establish the scope of the chirality audit (THEO-CHIR-AUDIT-1) as the foundational mapping exercise that determines, exhaustively, where chirality enters the current CPP framework. The audit's output is the precondition for all downstream CHIR-sector derivation work — including the open question whether chirality is *primitive* (axiomatized in A1–A9, possibly via consolidated A6′), *emergent* (derivable from the 600-cell geometry + the dynamical cycle), or *unregistered* (currently assumed without being either axiomatized or derived). The audit does not itself answer the primitive-vs-emergent question for any specific chirality-touching element; it produces the *classification map* that names every such element and assigns it provisionally to one of those three categories, with the substantive derivation work then becoming the registered downstream OPEN-CHIR-* programme.

This sketch was drafted at Session 148 close after the Patch 0629 (consolidated Option-A v1.1 revision pass) shipped. The audit was selected as the next substantive programme arc on methodological grounds: chirality is one of the deepest cross-sector questions in CPP, it is *sharply answerable* given the existing layered scaffolding, and its resolution unblocks parallel work in the weak-interaction sector, the neutrino sector, and the Mechanism A derivation (OPEN-FP-F1-2).

---

## §0 Working-session firewall

Subject to revision. The audit's scope as described here is at exploratory-sketch level, not theorem-closure level. The categories of chirality entry points enumerated in §3 below are the working taxonomy; the eventual artifact may refine these as the systematic walkthrough surfaces additional points or merges duplicate ones. The three operational senses of chirality distinguished in §2 below are similarly working definitions; their precise formulation in the eventual artifact may be sharpened. The precondition-gap inventory in §5 is exhaustive to the best of this sketch's knowledge of the current repo state but may be augmented as the audit work proceeds.

Two specific items in this sketch are *not* working-session-firewall content but are reported as findings with citations:

1. The PCD acronym correction (§5.2 below) — the canonical expansion is "Perceive, Compute, Displace" per the original archived definition; the "Polarize, Capture, Depolarize" variant introduced at Session 146 (commit `311bc1e`) is a terminological drift that must be corrected programme-wide.

2. The axiom-count finding (§5.1 below) — the canonical axiom registry says there are **9** axioms, not 11; the conventional "A1–A11" referencing reflects the historical pre-consolidation count, with A6′ consolidating four earlier axioms per the userMemories' notation. The audit's §2 axiom-level pass must use the current 9-axiom registry as its reference, not the legacy 11-axiom enumeration.

These two items are findings of the precondition mapping work, not working-session-firewall sketches.

---

## §1 The audit's three primary questions

The audit's job is to produce an *exhaustive enumeration* of every point in the current CPP framework where chirality enters — whether as an explicit axiom clause, an implicit geometric construction choice, a dynamic coupling, or an unregistered assumption. The output is a classified inventory.

The three primary questions the audit addresses are:

**Q1 (Inventory).** What are all the points in CPP A1–A9 + 600-cell geometry + PCD-cycle dynamics + existing CHIR-sector derivations where chirality is referenced, presupposed, or implicitly used?

**Q2 (Classification).** For each inventory entry, is it (a) primitive (already axiomatized in the current A1–A9 set), (b) emergent (derivable from geometry + dynamics without independent assumption), or (c) unregistered (currently assumed but neither axiomatized nor derived)?

**Q3 (Operational sense).** For each inventory entry, which of the three operational senses of chirality (defined in §2 below) does it produce — spatial, temporal, CP-asymmetric, or some combination?

The audit's conclusion is a theorem in the structural-cataloging sense: "Theorem (chirality entry-point enumeration). The chirality of the CPP framework enters at exactly the following list of points, classified as primitive/emergent/unregistered along the indicated operational senses." The proof is the systematic walkthrough. Falsification: find a chirality-touching element not on the list, or show that an element on the list is misclassified.

Layer target: Publication-grade Layer 3 unconditional. The audit uses the current A1–A9 axiom set and the established 600-cell geometric primitives (G1–G2.4) as given; it does not derive new framework axioms; it maps where chirality lives so that downstream derivations have clear targets.

---

## §2 Three operational senses of chirality

Before the audit can classify entries, it must distinguish three operationally separate senses of "chirality" that may appear:

**(a) Spatial chirality.** The existence of non-superposable mirror images — handedness in 3- or 4-dimensional space. Operationally: there exists an orientation-reversing isometry $\phi$ (e.g., a 4D reflection) such that $\phi$ applied to the configuration yields a configuration that is not superposable onto the original by the rotation group of the substrate. Spatial chirality enters CPP if any geometric or dynamical construction selects between left-handed and right-handed mirror-image realisations.

**(b) Temporal chirality.** An arrow of time — distinguishing forward dynamics from time-reversed dynamics. Operationally: there exists a time-reversal operator $T$ that is *not* a symmetry of the substrate dynamics. Temporal chirality enters CPP if the dynamical evolution of the substrate (i.e., the per-CP per-Absolute-Moment cycle) is not invariant under $t \mapsto -t$.

**(c) CP-asymmetric chirality.** The combined charge-parity asymmetry observed in weak interactions, in the Standard Model sense. Operationally: there exists a combined $CP$ operator that, applied to a process amplitude, yields a different amplitude than the original. This is the sense in which the observed universe is chiral at the deepest empirical level (CP-violation in neutral kaon decay, B-meson decay, etc., and the matter-antimatter asymmetry of the cosmos).

These three senses are operationally distinct but logically interrelated. The audit's classification must record which sense(s) each entry produces, because the downstream derivation work differs sharply depending on which sense is being derived: spatial chirality from geometry is typically a Wythoff-construction choice; temporal chirality from dynamics typically requires showing the cycle has irreversible coupling; CP-asymmetric chirality typically requires a combined argument involving both the geometry and the dynamics interacting with the matter content.

A clean audit will produce, for each entry, a row in a classification table with columns: *source* (axiom/geometry/dynamics/derivation), *operational sense(s)*, *primitive/emergent/unregistered*, *downstream OPEN-CHIR-* problem registered.

---

## §3 Section structure of the eventual THEO-CHIR-AUDIT-1 artifact

The audit artifact walks the framework in four systematic passes, then synthesizes.

### §3.1 — Setup (intended ≈ 40 lines)

Restates the three primary questions (§1 above) and the three operational senses (§2). Names the inputs the audit consumes: (i) the canonical axiom set per `axiom-registry.md` — currently 9 axioms; (ii) the 600-cell construction per the foundational documents; (iii) the canonical PCD-cycle specification per the corrected glossary entry (Perceive, Compute, Displace) — see §5.2 below for the terminology correction precondition; (iv) the existing CHIR-CONT-1/2/3 theorems plus the substrate-chirality work of Capotauro v2.0 (THEO-SD-CHIR-1, THEO-SD-CHIR-2); (v) the F.1 sub-question scoping sketch at `dynamical_substrate_law/sketches/F1_subquestion_pcd_orientation_link.md` and its associated $\hat{n} \mapsto \vec{\omega}_{PCD}$ link work.

### §3.2 — Axiom-level pass (intended ≈ 100 lines)

A1 through A9 (the current canonical set), one at a time, with three questions for each: (i) does this axiom reference direction, orientation, sequence, sign, or handedness in any form? (ii) if so, does it impose a chirality choice, or merely permit one? (iii) what operational sense (spatial/temporal/CP-asymmetric) does it touch?

Each axiom gets a row in the inventory table. Most rows will likely read "no chirality reference" — that is fine and expected; the discipline is to check each one explicitly so nothing is missed.

**Likely candidates** for chirality-touching axioms, to be verified during the walkthrough:

- *The PCD-cycle axiom* (whichever of A1–A9 specifies the per-CP per-Absolute-Moment cycle). The Perceive → Compute → Displace temporal sequence is *not* obviously time-reversal-symmetric: reversing the sequence would have the CP displace first, then compute, then perceive, which is a different dynamics. If the axiom canonically specifies the forward sequence and does not also assert time-reversal symmetry, the axiom itself sources *temporal* chirality. This is a strong candidate.

- *The polarity axiom* (whichever of A1–A9 specifies that CPs have polarity — electric-positive/negative, quark-positive/negative). Polarity itself is not chirality, but the *coupling* between polarity and substrate dynamics (e.g., which polarity captures which partner) may impose a handedness when combined with the geometry.

- *Any axiom defining a substrate primitive direction $\hat{n}$.* The Reading C trajectory of the Capotauro work has established $\hat{n}$ at Layer 3 rigor as a foundational input (FI-C-RC-1), and the F.1 sub-question sketch (`F1_subquestion_pcd_orientation_link.md`) explicitly opens whether $\hat{n}$ induces a PCD-cycle-orientation pseudovector $\vec{\omega}_{PCD}$ or is independent. If $\hat{n}$ is registered as a framework axiom (likely, given its FI-C-RC-1 status), it likely sources *spatial* chirality at the framework-axiom level.

### §3.3 — 600-cell geometric pass (intended ≈ 120 lines)

The 600-cell as a static polytope is achiral: its full symmetry group $H_4$ contains reflections, so any chiral structure is matched by its mirror image. But the polytope has multiple *internal* structures that *are* chiral when a choice is made among them. The audit enumerates these:

**The 5×24-cell partition.** The 120 vertices of the 600-cell partition into 5 disjoint 24-cells in two enantiomorphic ways. Choosing one partition introduces spatial chirality. The audit must determine: is the programme using one partition canonically? Which one? Is the choice arbitrary (and therefore an unregistered chirality entry that must be either eliminated or registered as a primitive) or constrained by some other consideration?

**The 24-cell internal structure.** Each 24-cell has a chiral relationship to the 600-cell embedding via its dual 24-cell.

**The binary icosahedral 2I cover.** The 600-cell as quotient of $S^3$ by the binary icosahedral group 2I. The group 2I has chiral irreducible representations. Does the substrate dynamics distinguish left- and right-spinor representations? The W-bracelet sector (THEO-SD-CHIR-1) and the qDP/eDP sector (THEO-SD-CHIR-2) both touch this question.

**The Wythoff construction orientation.** The polytope can be built from a Coxeter diagram $H_4$ with orientation choices that produce mirror-image embeddings.

**The icosahedral subgroup chain.** $H_4 \supset H_3 \times A_1 \supset I_h \supset I = A_5 \supset \ldots$ — the icosahedral *rotation* group $I = A_5$ is a chiral subgroup of the icosahedral *symmetry* group $I_h$. When the substrate dynamics select for rotations only (e.g., the K3-stabilizer $D_{3d} = D_3 \times Z_2$ retaining only a $C_3$ rotation axis), chirality enters. The Capotauro Reading C trajectory's vertex-aligned $\hat{n} = v_\text{host}$ resolution breaks $H_4 \to H_3 = I_h$, retaining the full icosahedral symmetry; further breaking to chiral subgroups happens in specific sector closures.

**The golden ratio $\phi$ in coordinates.** $\phi$ itself is achiral, but its appearance in coordinate triples with specific sign conventions (e.g., the standard 600-cell vertex set $\{(\pm 1, \pm 1, \pm 1, \pm 1)/2, (\pm \phi, \pm 1, \pm 1/\phi, 0)/\text{permutations}\}$) involves orientation choices.

**Reading C substrate primitive direction $\hat{n}$.** Per FI-C-RC-1 (Capotauro v2.0), $\hat{n}$ is a substrate primitive 4D direction. Its presence already breaks the achiral $H_4$ down to $H_3 = I_h$ at the host vertex — this is a spatial-chirality entry that exists at the foundational-input level, not yet at the axiomatic level.

### §3.4 — Dynamics pass: the PCD cycle (intended ≈ 80 lines)

The dynamics couple to geometry. The audit examines three sub-questions:

**(D1) Does the PCD temporal sequence impose an arrow of time?** The Perceive → Compute → Displace sequence at each Absolute Moment is, on its face, not time-reversible: time-reversed, the cycle would Displace → Compute → Perceive, which is a different operational dynamics. If the canonical specification asserts the forward sequence and does not assert time-reversal symmetry, the cycle itself sources *temporal* chirality at the axiom level.

**(D2) Does the polarization or perception step distinguish left from right?** The Perceive step has the CP detecting its local SSV environment. If perception is implemented as a vector inner product against an oriented sensor frame (a vector that distinguishes $+\hat{x}$ from $-\hat{x}$), no chirality is added. If perception is implemented via an oriented bivector or pseudovector that distinguishes left- from right-handed coordinate frames, *spatial* chirality is added.

**(D3) Does the capture step prefer one handedness of partner?** This is the deepest question. CPs form Dipole Pairs (DPs) by partnering with neighbouring CPs. If the partnering rule prefers one handedness — for example, electric-positive CPs preferentially partnering with quark-negative CPs in a specific orientation — then chirality is sourced at the dynamics level, not the geometry level. The W-bracelet V-A coupling work (SF-2's OPEN-FP-SF-2-CHIR) and the Capotauro K3-doublet chirality work both depend on this question.

**(D4) Does the PCD cycle have an orientation pseudovector $\vec{\omega}_{PCD}$?** The F.1 sub-question sketch (`F1_subquestion_pcd_orientation_link.md`) opens whether $\vec{\omega}_{PCD}(v_\text{host}) = \sigma \cdot \hat{n}$ for some sign convention $\sigma$. The audit registers this as a specific entry in the classification table; its resolution (Scenario A: derived via substrate-mechanism; Scenario B: independent primitive) determines whether the audit's overall classification places this entry under "emergent" or "primitive."

### §3.5 — Existing-derivation pass (intended ≈ 60 lines)

The existing CHIR-CONT-1/2/3 theorems are continuum-EFT projections of chirality-*conserving* currents. They take chirality as input on the operator algebra and derive the continuum form. The audit examines: what do they assume about chirality on input? Where does that assumption come from in the framework? This identifies the chirality entry point that those theorems *consume* but do not themselves derive.

Similarly: THEO-SD-CHIR-1 (W-bracelet sector) and THEO-SD-CHIR-2 (qDP/eDP sector) of Capotauro v2.0 are substrate-level theorems that close the chirality-bias derivation for two of the five manifestations under the OPEN-SD-CHIR-PRIMITIVE umbrella. The audit examines: what foundational inputs do these theorems consume? FI-C-RC-1 ($\hat{n}$) is the obvious one; are there others?

The audit's classification table includes a row for each foundational input identified as a chirality-source by these existing-derivation passes.

### §3.6 — Synthesis (intended ≈ 80 lines)

The inventory tables from §3.2–§3.5 are combined into a single classification table. Each chirality-touching element gets a row with: *source* (axiom/geometry/dynamics/derivation), *operational sense* (spatial/temporal/CP-asymmetric), *category* (primitive/emergent/unregistered), and *proposed handling* (already adequate / requires derivation as OPEN-CHIR-N / requires registration as new framework axiom).

The synthesis identifies for each "emergent" entry the most plausible derivation route given the existing scaffolding; for each "unregistered" entry, the choice between deriving it or registering it as a new framework axiom is named explicitly. The default presumption (per CPP methodological discipline) is to attempt derivation rather than axiom-set expansion.

### §3.7 — Conclusion theorem (intended ≈ 20 lines)

"**Theorem (THEO-CHIR-AUDIT-1).** The chirality of the CPP framework — in the three operational senses of §2 — enters at exactly the following points: [list with N entries]. Of these, $N_1$ are primitive (already in A1–A9 or in registered foundational inputs FI-C-RC-1, etc.); $N_2$ are emergent from the 600-cell + PCD cycle coupling, with derivation routes registered as OPEN-CHIR-1a, 1b, ...; $N_3$ are currently unregistered and require either registered derivation (presumption: yes) or registered framework axiom (presumption: no, only if derivation fails)."

The proof is the systematic enumeration of §3.2–§3.5. The falsifiers are explicit: find a chirality-touching element not on the list, or show an element is misclassified.

### §3.8 — Exclusions, anti-erasure, and open-problem registry outputs (intended ≈ 40 lines)

Standard sections per CPP artifact discipline.

---

## §4 Registry entries the audit creates

One new theorem row: **THEO-CHIR-AUDIT-1**, status "Publication-grade Layer 3 unconditional" (pending multi-AI review). Located in a new CHIR-AUDIT subseries in the CHIR sector of the frontier dashboard.

One new frontier sector file: **`frontier_sectors/CHIR.md`** — if this does not already exist as a standalone file (it currently does not appear to; the CHIR work is scattered across the dashboard and individual paper-folders), the audit will create it and migrate relevant existing entries.

A set of new **OPEN-CHIR-*** problems registered as outputs of the audit, with the specific list determined by the audit's classification table:

- **OPEN-CHIR-1**: derivation of any "emergent" chirality entry points identified by the audit. For each emergent entry, a sub-problem (OPEN-CHIR-1a, 1b, ...) is registered with the specific derivation target.

- **OPEN-CHIR-2**: handling of any "unregistered" entries — either find a derivation (most likely the right answer, to maintain methodological discipline) or register a new framework axiom with explicit justification.

- **OPEN-CHIR-3**: alignment with the observed Standard Model chirality structure — once primitive/emergent entries are mapped, the derivation chain to weak-interaction parity violation and the PMNS/CKM CP-phases becomes a registered downstream programme.

- **OPEN-CHIR-4**: potential interaction with OPEN-FP-F1-2 (Mechanism A derivation). If Mechanism A's derivation passes through chirality (plausible given that Mechanism A specifies the substrate's polarisation response, which is the load-bearing input to the dipole formation that the weak interaction acts on), the dependency is registered.

The audit also updates the `research_frontier.md` dashboard with the new CHIR-AUDIT subseries entry and the `frontier_sectors/FP.md` file with the patch and its outputs.

---

## §5 Precondition gaps that must be cleared before the audit ships

The audit cannot proceed cleanly until certain documentation and terminology gaps are resolved. Some of these can be cleared in Patch 0630 itself (this scope patch); others require dedicated cleanup patches before Patch 0631 (the audit artifact).

### §5.1 — Axiom count: 9 vs 11

**Finding:** The canonical `axiom-registry.md` says there are **9 axioms** ("Axiom set UNCHANGED at 9 axioms" across multiple recent updates). The conventional discussion in the userMemories and the programme-orientation document refers to "A1–A11," reflecting the historical pre-consolidation count. Per the userMemories note "A6′ Walk-Dimension Gauge Principle consolidating four earlier axioms," the count was reduced via consolidation.

**Required clarification before audit:** Confirm the canonical 9-axiom list with their current numbering, and confirm whether the "A1–A11" colloquial reference should be replaced with the canonical "A1–A9" (with A6′ as a refined version of A6) or whether both numbering schemes are tolerated.

**Audit handling:** §3.2 will use the canonical 9-axiom set per `axiom-registry.md`. The eventual artifact will footnote the consolidation history so that an external reader unfamiliar with the A6′ consolidation can locate the axioms.

**Cleanup work registered:** TODO entry in `todolist.md` to align the colloquial "A1–A11" referencing across the repo with the canonical "A1–A9" registry — low-priority hygiene, not blocking the audit.

### §5.2 — PCD acronym: terminology drift correction

**Finding:** The CPP PCD cycle's canonical expansion is **"Perceive, Compute, Displace"** per the original archived definition in `archive/grok-exploratory-SM/SR_companion_papers/c01_absolute_moment_postulate/absolute_moment_postulate.tex` — which explicitly defines "the Perceive-Compute-Displace (PCD) cycle" and uses it in load-bearing argumentation. The phrase "Perceive, Compute, Displace" appears nowhere in the current (non-archive) repo.

The phrase **"Polarize, Capture, Depolarize"** was introduced at Session 146 in commit `311bc1e` (the Session 146 handover commit dated 2026-05-28) as the expansion of "PCD" in `master_glossary.md`. There is no rationalization commit accompanying the change. From that single point, the new expansion propagated to:

- `master_glossary.md` (PCD entry + Conscious Point description)
- `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/dynamical_substrate_law.tex`
- `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/F1_subquestion_pcd_orientation_link.md`
- `series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex` and its companion files
- `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/documentation_suite/glossary-dynamical-substrate-law.md`
- `book_project/chapters/capotauro_what_was_always_there.md`
- `flagship_papers/electroweak/sf-2_electroweak.tex` and its companion
- `frontier_sectors/SS.md`
- and several other files (≈ 13 total, per the Session-148 grep)

**On accuracy:** The original "Perceive, Compute, Displace" framing is methodologically more accurate than the drift, for three reasons:

1. **Consciousness-as-fundamental is the load-bearing axiom of CPP.** The "Conscious" in Conscious Point Physics is not decorative; it is asserting that the CP has primitive agency — perception, computation, action. The Perceive-Compute-Displace expansion preserves this commitment in the acronym itself. The Polarize-Capture-Depolarize expansion reads the CP as field-responsive dynamics, vocabulary appropriate for emergent dipole/oscillator behaviour but inappropriate for the primitive cycle of a Conscious Point.

2. **Distinct from ZBW.** The master glossary defines Zitterbewegung (ZBW) as "the rapid oscillation of a CP between partner DPs" — the *between-CPs* dynamic. The PCD cycle is the *per-CP per-Absolute-Moment* primitive cycle. Polarize/Capture/Depolarize vocabulary partially conflates the two: capture in particular is what happens in DP formation (between CPs), not in the primitive per-CP cycle. Restoring Perceive-Compute-Displace preserves the conceptual separation.

3. **No physics content depends on the new expansion.** A careful read of the dependent files (notably the F.1 sub-question sketch, which is the most physics-laden) shows that the labels are decorative throughout: the substantive physics is about the cycle's *orientation* (the pseudovector $\vec{\omega}_{PCD}$) and its relationship to $\hat{n}$, not about polarisation, capture, or depolarisation as physical operations. Replacing the labels does not alter any derivation.

**Required cleanup work** (registered for a future patch, not blocking the audit's Patch 0631 if the audit uses the corrected expansion):

- `master_glossary.md` PCD entry: revert to "Perceive, Compute, Displace"
- `master_glossary.md` Conscious Point description: revert "the PCD cycle" → "the Perceive-Compute-Displace (PCD) cycle"
- Dependent files (≈ 13): bulk find-and-replace of "Polarize-Capture-Depolarize" → "Perceive-Compute-Displace" and the corresponding "Polarize → Capture → Depolarize" → "Perceive → Compute → Displace" arrow notation; verify no substantive physics claim is affected
- `todolist.md`: register the cleanup work as an item (the expunge note Thomas mentioned was apparently planned but not yet committed)

**Audit handling:** §3.4 will use the canonical "Perceive, Compute, Displace" expansion. The eventual artifact will footnote the terminology history briefly so that an external reader who encounters the legacy expansion in archived files can locate the correction.

### §5.3 — Canonical PCD-cycle dynamics specification

**Gap:** Even with the acronym corrected, the *substantive* specification of the PCD cycle as a dynamical operation needs to be located in canonical form. The master glossary defines it briefly ("the three-phase cycle executed by each CP at every Absolute Moment") but does not specify the dynamics in derivation-grade detail: what perception detects, how computation determines the response, what determines the displacement magnitude/direction. The archived `absolute_moment_postulate.tex` provides some of this content but is archived rather than canonical.

**Required clarification before audit:** Identify whether the canonical PCD-cycle dynamics specification lives in one of the existing axioms (most likely as part of A1 or A2), or whether a dedicated canonical document is required. If the latter, registering it is a precondition for §3.4 of the audit.

**Audit handling:** The audit's §3.1 setup will name the canonical specification; if a gap is identified, the audit will register OPEN-CHIR-DYN-SPEC as a downstream programme task and proceed with the best available approximation.

### §5.4 — ZBW vs PCD relationship

**Gap:** ZBW and PCD are distinct mechanisms per the master glossary, but the *relationship* between them is not canonically specified. Operationally: PCD is the per-CP per-Moment primitive cycle; ZBW is the rapid between-CPs oscillation that appears in relativistic dynamics (electron Zitterbewegung as Hestenes-style internal cycling). Are they:

- Two distinct names for the same underlying dynamic at different abstraction levels?
- Two separate dynamics, with PCD being the substrate primitive and ZBW being the emergent collective oscillation?
- Related but ontologically distinct, with ZBW being a sector-specific phenomenon (relativistic regime) that arises from PCD in some specific limit?

The audit's §3.4 needs an answer because temporal chirality may be sourced from either or both, and the classification must distinguish.

**Required clarification before audit:** Locate canonical statement of the PCD/ZBW relationship, or register OPEN-CHIR-ZBW-LINK as a sub-question to be addressed by the audit's §3.4.

### §5.5 — Reading C $\hat{n}$ primitive and the F.1 sub-question

**Status:** Less a gap than an active workstream that the audit must integrate with. The F.1 sub-question sketch (`F1_subquestion_pcd_orientation_link.md`) opens whether the substrate primitive direction $\hat{n}$ (FI-C-RC-1) induces the cycle-orientation pseudovector $\vec{\omega}_{PCD}$ via a substrate mechanism (Scenario A) or whether $\vec{\omega}_{PCD}$ is an independent primitive (Scenario B). This is itself a chirality-classification question: if Scenario A, $\vec{\omega}_{PCD}$ is *emergent* from $\hat{n}$; if Scenario B, both $\hat{n}$ and $\vec{\omega}_{PCD}$ are *primitive* foundational inputs at the framework-axiom level.

**Audit handling:** The audit's §3.4 includes the $\hat{n} \mapsto \vec{\omega}_{PCD}$ link as a specific classification-table entry; its resolution is registered as OPEN-CHIR-F1-LINK (or as a sub-entry of OPEN-CHIR-1 if Scenario A is the working presumption). The audit does not pre-commit to either scenario; it lays out the classification dependency clearly.

### §5.6 — Existing CHIR work inventory

**Status:** The audit's §3.5 needs a precise enumeration of existing CHIR-sector work to know what foundational inputs to credit. Initial inventory (to be verified in the audit work):

- **THEO-CHIR-CONT-1/2/3.** Continuum-EFT projections of chirality-conserving currents. Layer 4. Located at `series_umbrella/series_substrate_chirality_arc/chirality_continuum/`.
- **THEO-SD-CHIR-1.** W-bracelet sector substrate chirality closure theorem (Capotauro v2.0). Registered Session 132 Patch 0434. Located at the appropriate Capotauro paper section.
- **THEO-SD-CHIR-2.** qDP/eDP sector substrate chirality closure theorem (Capotauro v2.0). Registered Session 133 Patch 0440. Located at the appropriate Capotauro paper section.
- **OPEN-SD-CHIR-PRIMITIVE umbrella.** Programme-level cross-sector unification target across five manifestations (i)–(v). Registered Session 127 Patch 0422.
- **F.1 sub-question sketch.** Active sketch, not yet at theorem-closure level.
- **Capotauro v2.0 dynamical engine epistemology** (§13.6).

**Audit handling:** §3.5 walks each of these and records what foundational inputs each consumes and what chirality entry point each represents. No new theorem registration; the audit only catalogues.

---

## §6 Patch sequence

**Patch 0630 (this patch):** This scope-and-precondition sketch document, committed to `series_umbrella/series_substrate_chirality_arc/chirality_audit/sketches/theo_chir_audit_1_scope.md`. Plus a single-line addition to `todolist.md` registering the PCD-terminology cleanup. No registry edits; no theorem-registry, FP.md, or research_frontier.md updates required at this patch (those happen at Patch 0631 when the audit ships).

**Patch 0631 (Session 148, target):** The THEO-CHIR-AUDIT-1 artifact at `series_umbrella/series_substrate_chirality_arc/chirality_audit/theo_chir_audit_1.tex`, plus reasoning fragment at `chirality_audit/reasoning/0631.md`, plus the theorem-registry row, plus `frontier_sectors/CHIR.md` (newly created), plus updates to `research_frontier.md` dashboard + `frontier_sectors/FP.md`. One patch if all preconditions clear; two if the PCD terminology cleanup is done as a dedicated pre-audit patch.

**Patches 0632+ (multi-session):** Multi-AI review cycle of THEO-CHIR-AUDIT-1 (ChatGPT + Copilot + Grok), then opening of the OPEN-CHIR-* problems the audit identifies, then derivations of emergent chirality entries. The first downstream theorem after the audit is likely **THEO-CHIR-PCD-ORIENTATION-1** addressing the F.1 sub-question's Scenario-A derivation of $\vec{\omega}_{PCD} = \sigma\hat{n}$.

**Patch sequence checkpoint:** At Patch 0631 completion, the programme has (i) the full chirality-entry-point classification map; (ii) the registered downstream OPEN-CHIR-* programme; (iii) Layer-3-unconditional rigor on the catalogue itself. The substantive question — *is chirality primitive, emergent, or some mixture?* — now has a definite, answerable, layered structure, with each entry's primitive/emergent classification subject to derivation rather than assertion.

---

## §7 What the eventual paper will look like

A paper-grade synthesis at the chirality question is not the right deliverable yet. The audit + the downstream OPEN-CHIR-* derivations need to be in hand first. The right moment for the paper is when the classification table is complete, the emergent entries have been derived (or honestly registered as underivable and axiomatized), and the unregistered entries have been resolved.

When that moment arrives, the paper's natural title is something like **"Chirality in the Conscious Point Substrate: Primitive, Emergent, or Both?"** with the structure: (i) the audit's classification map as the framing, (ii) each emergent derivation as a section, (iii) the connection to observed Standard Model chirality (parity violation, CP-violation phases, matter-antimatter asymmetry) as the empirical anchor, (iv) the methodological discussion of why the layered approach is what makes the question well-defined.

The paper writes itself once the proof body answers the question. The audit is the foundation that lets the question be asked in derivation-grade form. That is the right next piece of programme work.

---

## §8 References

- `axiom-registry.md` (canonical axiom registry; currently 9 axioms post-consolidation)
- `master_glossary.md` (canonical glossary; PCD entry currently has the Session-146-drifted expansion that requires correction per §5.2)
- `programme_orientation.md` Postulates 1+2 (the "perceive their local environment and respond according to rules" language preserves the original Perceive-Compute-Displace framing)
- `theorem-registry.md` (current theorems; THEO-CHIR-CONT-1/2/3, THEO-SD-CHIR-1/2 entries)
- `research_frontier.md` dashboard + `frontier_sectors/FP.md` (current frontier state)
- `series_umbrella/series_substrate_chirality_arc/chirality_continuum/chirality_continuum.tex` (existing CHIR-CONT theorems)
- `series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex` (existing substrate-chirality work, THEO-SD-CHIR-1/2)
- `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/F1_subquestion_pcd_orientation_link.md` (the $\hat{n} \mapsto \vec{\omega}_{PCD}$ link sub-question, active workstream)
- `archive/grok-exploratory-SM/SR_companion_papers/c01_absolute_moment_postulate/absolute_moment_postulate.tex` (the original Perceive-Compute-Displace definition; archive but canonical for terminology)
- Session 146 handover documents (introduction of the PCD terminology drift)

---

**Scope document complete.** Patch 0630 commits this sketch plus the todolist entry registering the PCD cleanup. Patch 0631 ships the audit artifact at Session 148.
