# Flagship assembly scope — "The Spin-Bit Axiom: Necessity, Construction, and the Derived Einstein Quadrupole Formula"

**Register:** PLANNING ARTIFACT — a Phase-7A-style assembly scope, not the paper and not a
commitment to build. Moves no verdict; registers nothing. Created Patch 1132 (spin-2 / op:einstein
lane), Session 159.
**Decision it serves:** lets Thomas see the flagship's shape — section skeleton, artifact-to-section
mapping, the drafting gaps, and the open decisions — before committing drafting effort.
**Precedent followed:** the chirality flagship assembly scope
(`series_umbrella/series_substrate_chirality_arc/flagship_assembly_scope.md`, Patch 0933), the
established Phase 7A opening move for an arc whose results are review-closed but un-assembled.
**Working title:** above; alternates in §7. The frontier's standing name for this venue is the
**"GR companion"** (`frontier_sectors/SR.md`, multiple entries).

---

## 0. The structural fact this scope rests on (read first)

Unlike the chirality flagship (39 existing `.tex` theorem files, one missing centerpiece), the
spin-2 arc has **zero `.tex` files**. Its entire content lives as:

- **13 step/task documents** (`spin2_construction/1112…1129_*.md` + the prequel
  `op_einstein_closure/1107…1110_*.md`) — detailed, reviewed, with full derivations;
- **11 verified standalone scripts** (`spin2_construction/code/` + `op_einstein_closure/code/`),
  all committed, all run clean;
- **16 verbatim Tier-4 reasoning fragments** (`spin2_construction/reasoning/1112…1130`);
- **the DG-3 review suite** (`review/a3prime_axiom_review_package_v1.0.md` v1.1-delta-headed +
  `review/reviews-A3PRIME.md`, both rounds, 3/3 CONFIRM);
- **registry entries** (A3′ in `axiom-registry.md`; THEO-SR-EIN-1..4 in `theorem-registry.md`;
  PRED-O-35..38 in `predictions.md`; the Patch 1117 + 1130 blocks in `frontier_sectors/SR.md`).

So the assembly task is inverted relative to the chirality case: **nothing needs to be derived,
everything needs to be drafted.** Every section below maps to already-reviewed content; the
flagship is a writing-and-framing exercise under the constraint that the prose must not read
stronger than the registered claims (the TARROW-2 v1.0→v1.1 lesson, inherited via the chirality
scope's Gap 4).

## 1. What the flagship claims (the answer to its own title)

**Gravity's radiative tensor sector forced a new fundamental degree of freedom — and the axiom
paid for itself.** Three results, in the order the paper argues them:

1. **Necessity (theorem-grade, three independent assaults):** CPP's scalar+vector LSP cannot
   source the helicity-±2 GW polarizations — not directly (1109), not as composites/bilinears
   (1115), not as emergent collective modes (1116: dynamical-matrix helicity content {0,0,±1}
   for ALL couplings), and not via a non-radial connection / PSR-hop twist (1119: survives three
   ways; data-acting twists are Planck-gapped to 10⁻⁴⁶–10⁻⁵¹). A fundamental rank-2 d.o.f. is
   **required**, as in every working theory of gravity.
2. **Construction (A3′, registered Patch 1129):** the 600-cell supplies the seat natively — the
   icosahedral shell's H_g (l=2) representation, with m=±2 exactly the GR +/× polarizations
   (1112) — and the rank-agnostic shell-sum supplies propagation (1113). The amendment A3 → A3′
   completes the broadcast at the lattice's full protected content: **LSP′ = A⊕T₁⊕H = 9 numbers,
   no fourth rung** (Completion Theorem, THEO-SR-EIN-1: intact icosahedral descents are exactly
   l ∈ {0,1,2}, permanently). **+1 d.o.f., 0 parameters.**
3. **Payoff (derived, zero new parameters):** the coupling is fixed at **λ = 16πG/c⁴** — c08's
   *asserted* field equation becomes a *derived* one — with h^TT = (2G/c⁴r)Q̈^TT, source the
   traceless local stress (quadrupole emergent via ∫T_ij = ½M̈_ij, verified 6×10⁻⁷); statics
   untouched (THEO-SR-EIN-2, virial); response pure tensor, Eardley **N₂** (THEO-SR-EIN-3,
   cancellation theorem + the τ-redundancy discovery, GR-match 10⁻¹⁹); energy ledger closed
   (THEO-SR-EIN-4, Operational-Energy Lemma; flux/Peters 1.000640 grid / 0.999998 analytic;
   Hulse–Taylor −2.4031×10⁻¹², double pulsar −1.2483×10⁻¹², nothing tuned).

It is a **foundations + derivation** paper: it changes the axiom inventory (the programme's first
axiom-level move to pass DG-3 review) AND derives the Einstein quadrupole sector at zero
parameters. Its falsifiers are registered but deliberately **uncounted** (PRED-O-35..38; counting
awaits the panel protocol — queue item 3 of the 1131 handover).

## 2. Section structure + artifact mapping

**Main text — the necessity spine:**

| § | Section | Source artifacts | Role |
|---|---|---|---|
| §1 | Introduction: the GW polarization tension and what closing op:einstein buys | `op_einstein_closure/README.md` charter; 1117 frontier block | frame: CC suppression + DM R2 both rest on c08's op:einstein; the tensor sector is its (a)-half |
| §2 | Diagnosis: scalar–vector gravity's helicity-±2 gap | 1109 (`stepA_helicity2_gap`), 1110 (c07 §6 audit: TT asserted, not derived) | the precise gap; what c07/c08 do and do not provide |
| §3 | Necessity: the three assaults | 1115 (composite/bilinear excluded), 1116 (emergent verdict: {0,0,±1} only), 1119 (connection/twist rerun; Planck-gap exclusion; Nexus frame load-bearing) | the theorem-grade "no existing or emergent route" result |
| §4 | The geometric seat | 1112 (H_g slot; 5-design orthogonality; m=±2 = +/×), 1120 §branching bonus (icosahedral protects l=2 intact; cubic splits 2+3) | the lattice already holds the chair; nothing sits in it |

**Main text — the axiom and its payoff:**

| § | Section | Source artifacts | Role |
|---|---|---|---|
| §5 | The axiom: A3′ | 1121 (flow choice B = LSP broadcast; precedent ladder; no-ZBW + no-static constraints), 1123 (axiom text v0.4; dual accounting 9/10; Completion Theorem) | the registered statement, the amendment form (A6′ precedent), THEO-SR-EIN-1 |
| §6 | The derived quadrupole formula | 1124 (C4 v0.2: traceless-stress source; λ = 16πG/c⁴; h^TT law; statics/virial = THEO-SR-EIN-2; binary-pulsar checks) | **centerpiece**: assertion → derivation at zero parameters |
| §7 | Response and energy | 1125 (cancellation theorem; τ redundancy; Eardley N₂ = THEO-SR-EIN-3; flux 1.000246), 1127 (Operational-Energy Lemma = THEO-SR-EIN-4; eccentric ledger 1.000640) | the kill-switch survival + the review-forged lemma |
| §8 | Emergent spin-2 in matter | 1120 (f₂(1270) ³P₂ from vectors; SS-1e χ_c2 + SS-6 orbital Q_d anchors) | why the axiom is mono-sectoral/multi-evidential; the second motivation *dissolved*, not failed |

**Main text — record and synthesis:**

| § | Section | Source artifacts | Role |
|---|---|---|---|
| §9 | Falsifiers F1–F4 | PRED-O-35..38 (`predictions.md` rows) | pure-tensor polarization; GW speed; multiplet integrity as a **lattice discriminant** (icosahedral vs cubic); dispersion ceiling. Stated as registered-uncounted |
| §10 | Review record, residuals, downstream | `review/reviews-A3PRIME.md`; 1129 registration doc; 1131 handover §queue | the DG-3 two-round history (objection upheld against 2–1, fixed, withdrawn by author); declared refinement (substrate-microscopic energy functional, constrained by THEO-SR-EIN-4); unblocked lanes (CC reconciliation, DM R2 (a)-leg) |

**Prequel / companion decision (§7 below):** 1107–1108 ((b) excess-vs-absolute sourcing; the
5-design monopole annihilation). Recommendation: **one compact subsection inside §1** stating the
(b)-half's conditional closure and pointing at the step docs — not a full section. The flagship is
about the tensor sector; (b) is its sibling, not its content. The alternative (full §) doubles the
paper's scope for material that may belong to the eventual CC-reconciliation paper instead.

## 3. Where the conditionality and residuals are stated

This arc is in **better conditional shape** than the chirality flagship — A3′ is registered
unconditionally (no Mechanism-A analog). The honest residuals, stated in §10 and echoed in §1:

- **Declared refinement (OPEN candidate, not debt):** the substrate-microscopic energy functional
  — must reproduce the C5-operational ledger; THEO-SR-EIN-4 constrains it. Carried per the 1129/
  1131 framing: the energy accounting is *operationally* closed; its microscopic underwriting is
  a refinement target.
- **(b)-half conditionality:** excess-sourcing / inert-uniform-Sea is **conditionally** closed
  (shell-sum reduction rigorization is the named residual, per the op_einstein_closure README).
  If the prequel subsection is included, this conditionality must be stated there verbatim — the
  flagship must not let "op:einstein (a) CLOSED" read as "op:einstein CLOSED."
- **PRED counting:** F1–F4 ship as registered, open, **uncounted** falsifiers. The flagship must
  not count them; the count moves only via the panel protocol (PRED-C-96 precedent).

## 4. Framing guards (inherited disciplines)

- **Do not erase the review's texture.** The Round-1 RESTATE — upheld *against* the 2–1 vote,
  fixed via a new lemma, then withdrawn by its own author on independent recompute — is the
  strongest process evidence in the paper. §10 tells it straight (symmetric-honesty discipline;
  the CAPACITY-1 "stress-test the load-bearing step" lesson).
- **Mono-sectoral is a finding, not a weakness.** §8's framing: the tensor-meson test was run
  *seeking* a second motivation and returned EMERGENT — so the axiom is motivated by gravity
  alone but evidenced by necessity-proofs plus the zero-parameter derivation chain. Normal for
  gravity (the graviton is fundamental in every working theory).
- **Methods citations (C14 catalog-first-then-cite):** the drafting pass must run the
  methods_catalogue audit over the 16 reasoning fragments BEFORE inline-citing the `.tex`
  (paper_completion_checklist C14 workflow).

## 5. Assembly gaps (what must be produced beyond what exists)

1. **The entire `.tex`** — no LaTeX exists. Sourced from the 13 step/task docs (which are
   near-paper-grade) + the 11 scripts + the review suite. **Largest task, but transcription-and-
   framing, not derivation.** Estimate: the step docs map ~1:1 onto §§2–8.
2. **§1 intro narrative** — the op:einstein stakes (CC + DM), the (b) prequel subsection, and
   the "axiom that paid for itself" arc. New prose.
3. **Figure set** — none exists. Candidates: the H_g seat / m=±2 polarization identification
   (from 1112's script output); the dynamical-matrix helicity spectrum (1116); the eccentric
   energy ledger vs Peters f(e) (1127). All regenerable from committed scripts.
4. **Bibliography** — Eardley classification, Hulse–Taylor / double-pulsar timing, GW170817
   speed bound, tensor-meson PDG entries; plus internal c07/c08/SS-1e/SS-6 cites. Check
   `bibliography/cpp_references.bib` for what exists before adding (C11).
5. **Conditionality harmonization** — §1/§3/§10 must state identically: (a) CLOSED, (b)
   conditionally closed with named residual, energy functional a declared refinement.
6. **Verification-notebook formalization (B1–B5)** — the 11 scripts are already
   standalone-clean; the gap is the required notebook headers + INDEX entries, not new code.

## 6. Recommended build sequence (within Phase 7A/B/C)

- **7A (pre-draft, this phase):** lock the §-skeleton (this scope); make the §7-decisions below;
  run the C14 methods audit over the reasoning corpus; regenerate the figure candidates.
  *Gate: skeleton locked, methods catalogued, figures exist.*
- **7B (assembly):** draft §§2–8 from the step docs (the 1:1 mapping); write §1 and §§9–10;
  harmonize conditionality (Gap 5); build the bibliography. *Gate: full draft compiles,
  conditionality consistent, F1–F4 stated as uncounted.*
- **7C (review/ship):** cross-reviewer pass **scoped to framing + over-claim, not new math** —
  the components are DG-3-closed 3/3 over two rounds; the review question is "does the assembly
  claim more than the registry holds." Then the per-paper completion checklist fires on SHIP
  (the 10-file documentation suite, registries, anthology chapter C13, audit H6).

The Reviewer-Pause Cycle precondition (`paper_completion_checklist.md` final section) is
**satisfied in substance**: the DG-3 axiom-level cycle (1126–1128, two rounds, 3/3, one upheld
objection integrated) is this arc's closure-milestone external review. The 7C pass is the
chirality-style framing review, not a new closure gate.

## 7. The open decisions (Thomas's calls before drafting starts)

1. **Paper ID / venue.** Options: (i) **SR-2** in `series_relativity/` (catalog shows only SR-1
   shipped; SR-5 is the CC-reconciliation *concept*, unclaimed as a file); (ii) a flagship-line
   designation under `flagship_papers/` (the arc is flagship-grade: first axiom-level DG-3 pass +
   zero-parameter Einstein-sector derivation); (iii) the standing frontier name "GR companion."
   **Recommendation: SR-2** — it is the SR sector's natural successor paper, and the F-line is
   currently reserved for substrate-law trajectories (F.1).
2. **Title.** Working title above; alternates: "One Scalar, One Vector, One Tensor: the Completed
   Broadcast Axiom and the Einstein Quadrupole Formula at Zero Parameters"; "No Fourth Rung."
3. **Prequel scope** ((b)-half 1107–1108): compact §1 subsection (recommended) vs full section
   vs deferred entirely to the CC-reconciliation paper.
4. **Sequencing vs the unconditionalization lanes.** The flagship does not block on them, and
   they do not block on it. But if the CC-reconciliation lane lands soon, §1's stakes paragraph
   strengthens from "unblocks" to "delivered." Drafting now is bounded and worth doing either
   way (the chirality-scope argument, verbatim).
5. **PRED counting timing.** If the panel-count protocol (queue item 3) runs before 7C, the
   flagship ships with counted predictions; otherwise registered-uncounted with the count as a
   v1.x upgrade. No drafting dependency either way — §9 is written conditionality-stable.

---

## 8. SKELETON LOCK + decisions record (addendum, Patch 1135 — Session 159, 12 June 2026)

**Architect sign-off received in-session ("Proceed with your recommendations"). The five §7
decisions are settled and the skeleton is LOCKED:**

1. **Paper ID = SR-2.** Lives at `series_relativity/papers/` per series convention; canonical
   filename `SR-2_spin_bit_axiom_quadrupole_formula.tex` (no version suffix, per OS §11).
2. **Title (working, lockable at 7C polish):** *"The Spin-Bit Axiom: Necessity, Construction,
   and the Derived Einstein Quadrupole Formula."*
3. **Prequel scope:** the 1107–1108 (b)-half enters as a **compact §1 subsection** (conditional
   closure stated verbatim, shell-sum residual named); full treatment deferred to the CC-
   reconciliation paper.
4. **Sequencing:** drafting proceeds now; no blocking either way against the
   unconditionalization lanes.
5. **PRED counting:** F1–F4 ship **registered-uncounted**; the panel count is a clean v1.x
   upgrade (PRED-C-96 protocol precedent).

**The 10-section skeleton of §2 is LOCKED as the build plan.** Changes to section structure
from here forward require a dated note in this addendum (drift guard).

**Gate status (per §6, 7A pre-draft):**

| Gate item | Status | Record |
|---|---|---|
| C14 methods audit (catalog-first) | **DONE, Patch 1133** | +8 catalogue entries (METH-L1-008..012, L2-010..011, L3-006) + L3-004 examples + footer correction; audit trail + STRAIGHT-REUSE citation map at `spin2_construction/1133_c14_methods_audit.md` |
| Figure candidates regenerated | **DONE, Patch 1134** | 4 figures (SVG+PDF) at `series_relativity/figures/figures-SR-2/`; B2-headered notebook `series_relativity/notebooks/SR-2_figures.py`; eccentric-ledger one-period average **0.999998** = the review's independent analytic recompute |
| Skeleton locked | **DONE, Patch 1135** | this addendum |

**7A gate: CLEAR.** Next phase per §6 is **7B assembly**: draft §§2–8 from the step docs
(the ~1:1 mapping), write §1 (stakes + prequel subsection) and §§9–10 (falsifiers; review
record + residuals), harmonize the conditionality language (Gap 5), build the bibliography
(Gap 4 of §5), and execute the C14 step-4 inline citations per the 1133 citation map. The 7C
review pass remains scoped to framing + over-claim, not new math.

**Figure-to-section map (locked with the skeleton):** fig1 (H_g seat) → §4; fig2 (two
assaults) → §3; fig3 (eccentric ledger) → §7; fig4 (lattice discriminant) → §9. Final art
direction (palette, sizing, the ×-panel sparseness note — 8 of 12 shell vertices have xy = 0
exactly, so the sparse support is physical and will be stated in the caption) is 7B work.

---

## 9. 7B drafting note (addendum, Patch 1136 — 12 June 2026)

**Phase 7B first full draft landed:** `series_relativity/papers/SR-2_spin_bit_axiom_quadrupole_formula.tex`
(v0.1) + `SR-2_references.bib` + `documentation_suite/changelog-SR-2.md`. Transcribed from
the 13 step/task docs + DG-3 suite onto the locked 10-section skeleton (§8 LOCK). No verdict
moved; prose held to the registered claims (A3′ amendment count 9 / audit note 10;
THEO-SR-EIN-1..4 verbatim; PRED-O-35..38 open-uncounted). Conditionality harmonized per Gap 5
((a) CLOSED / (b) conditionally closed, shell-sum-rigor residual / energy functional declared
refinement). Inline `[METH-Lx-NNN]` citations placed per the 1133 plan. Figures slotted per the
locked map (fig1→§4, fig2→§3, fig3→§7, fig4→§9) via `\includesvg`.

**Drift-guard disclosures (skeleton respected; two standard-scaffolding folds recorded):**
1. The locked 10-section spine is preserved 1:1 as the content map. A standard **§11 Conclusion**
   was added beyond the spine to carry the PD-001-required subsections (Swarm-Validation
   Contribution; Problem Status After This Paper) — scaffolding mandated by `paper-formatting.md`
   §4.1, not a change to the locked content structure.
2. The locked §8 ("Emergent spin-2 in matter") absorbs the **Physical Interpretation** role and
   carries the PD-001-required **CP/GP Signature at this scale** subsection. The locked §1 carries
   the required **Open Problems Addressed** subsection. No content section was added, removed, or
   reordered.

**7B remaining (before 7C dispatch):** C14 step-5 audit-trail sweep for uncited substantive method
invocations; optional figure-PDF pre-generation if the build host lacks inkscape; then the 7C
framing/over-claim review (not new math).

**7B COMPLETE (Patch 1137, 12 June 2026 — draft → v0.2):** C14 step-5 audit-trail sweep done
(added METH-L3-003 §3 + METH-L3-004 §3/§7; all 13 plan methods now cited); figure PDFs
generated from the notebook and the four includes switched to `\includegraphics{...pdf}`
(no inkscape needed); full `pdflatex ×3 + bibtex` cycle verified clean (rc=0 throughout, no
undefined refs/citations, 6 bib entries resolved, 19 pages). **Gate: 7B CLEAR.** Next phase
is **7C** — framing + over-claim review only (not new math; components are DG-3-closed).
