# OPEN-SS-24 Handover — Orientation Document for the Next Opus

**Created:** 26 April 2026 (end of session 0022–0033)
**Purpose:** Paste-ready orientation document for the next Opus session to begin work on OPEN-SS-24 (first-principles derivation of C4 simplicial connectivity from CPP primitives) without re-deriving the context from scratch.
**Format:** Markdown, intended to be pasted directly into a new Opus chat session as bootup context.
**Status of OPEN-SS-24 itself:** OPEN. Not yet attempted in any sustained way. This is a *starting orientation*, not a partial draft.

---

## What you are picking up

The CPP programme has just closed SS-8 v1.0 and its full archive cycle (patches 0022–0033). SS-9 drafting is unblocked and the recommended target is **OPEN-SS-24: First-principles derivation of C4 simplicial connectivity from CPP primitives.**

OPEN-SS-24 is the highest-leverage open problem in the strong-sector series. Closing it would promote 54 of 55 conditional D-N predictions in the cumulative CPP swarm tally (12 SS-7 alpha-chain bindings + 42 SS-8 interstitial-neutron predictions, less the 1 PRED-C-31 string tension entry that depends on a different conditional stack) from conditional to unconditional. This is the largest single-paper conditional-to-unconditional shift available in the entire programme.

The work is mathematical, potentially self-contained, and estimated at 2–3 sessions. Three physical intuitions have been registered in SS-7 v1.2 §5 as candidate components of the derivation. Your job is to attempt the derivation rigorously.

---

## Bootup steps before starting OPEN-SS-24

You are operating under the standard CPP bootup protocol. Read these files first, in this order:

1. `bootup.md` — the standard bootup-protocol entry point (clone-first per Step 0)
2. `templates/operating_system.md` — Two-Trigger Documentation Discipline + Cross-Paper Session Log convention adopted 26 April 2026 (§4)
3. `axiom-registry.md` — the 9-axiom set (4 ontological + A5 + A6′ + A10 + A8′ + A11)
4. `predictions.md` Cumulative Swarm Tally section — the 103 zero-parameter empirical correspondences from 9 axioms (ratio 11.4×)
5. `theorem-registry.md` — 52 theorems / 9 corollaries (THEO-SS-12 Euler edges, THEO-SS-13 Euler-degree, THEO-SS-14 D1 conditional, THEO-SS-15 2E/V scaling are all directly relevant to OPEN-SS-24)

Then specifically for OPEN-SS-24:

6. `series_strong/papers/SS-7/SS-7_alpha_cluster_edge_formula.tex` v1.2 — read §5 carefully (the section that registers the four candidate mechanisms for the apparent underbinding) and §3 (the simplicial-polytope assumption itself, hypothesis C4)
7. `series_strong/papers/SS-8/SS-8_interstitial_neutron_2EV_scaling.tex` v1.0 — read §3 (D1, D2, D3 hypothesis statements), §4 (the central H2′ derivation), and §6 (Pattern 6 cascade discussion; this is where the structural-recurrence picture gets articulated)
8. `research_frontier.md` — find the OPEN-SS-24 entry; note its current state and dependencies
9. `series_strong/papers/SS-7/documentation_suite/philosophy-SS-7.md` — read this; it explains the conditional-vs-derived distinction in SS-7's framing and gives the right register for thinking about C4 as an assumption-versus-theorem
10. `series_strong/papers/SS-8/documentation_suite/mechanism-SS-8.md` — read this; it explains how D1/D2/D3 plus C4 (inherited from SS-7) interact

**Optional but recommended:**
- `book_project/chapters/SS-7_eight_nuclei_in_a_row.md` and `SS-8_octahedron_in_magnesium.md` — the anthology chapters give a non-technical articulation of what's at stake in OPEN-SS-24; sometimes the SciAm register makes the structural picture clearer than the technical paper does
- `problem_histories/PH-OPEN-SS-22.md` — the OPEN-SS-22 retirement narrative; not directly about OPEN-SS-24 but useful for understanding how this programme handles structural hypotheses that turn out to need adjustment

---

## What OPEN-SS-24 is asking

C4 is the structural hypothesis, inherited from SS-7 and SS-8, that **alpha clusters in bound nuclei realize simplicial 3-polytope connectivity**. This means specifically:

- The alpha clusters arrange at the vertices of a closed convex polyhedron
- Every face of that polyhedron is a triangle (no square or pentagonal faces)
- Adjacent alphas are in actual contact (not separated by larger gaps that would reduce the per-edge binding contribution)

C4 is what makes the SS-7 binding formula $B(N_\alpha) = N_\alpha B_\alpha + (3N_\alpha - 6) B_\text{pair}$ work — the $3N_\alpha - 6$ edge count comes from Euler's formula applied to simplicial polyhedra specifically, not to general polyhedra. C4 is also what lets SS-8's 2E/V scaling law operate, because the average vertex degree formula $2E/V = 6 - 12/V$ is also specific to the simplicial case.

C4 has been treated as a structural hypothesis throughout SS-7 and SS-8. The empirical agreement (12 nuclei within 1.5% in SS-7; 11 of 12 within 15% in SS-8 with two sub-1% landings at the most symmetric polytopes) is strong circumstantial evidence that C4 holds. But C4 has not been *derived* from CPP primitives. That derivation is OPEN-SS-24.

---

## The three physical intuitions registered in SS-7 v1.2 §5

The original SS-7 paper registered three physical intuitions that the OPEN-SS-24 derivation might formalize. Read them in the SS-7 .tex source for the exact framing; here is the quick orientation:

**Intuition 1: Triangular faces follow from rigid-tetrahedral base-to-base contact.** Two adjacent alpha particles in CPP geometry contact at a triangular base face (the K₃ contact face that gives $B_\text{pair}$). When three alphas meet at a polytope vertex, their three contact faces force a triangular configuration at that vertex by rigid-base geometry. This argues that triangular-face polytopes are *forced* by the CPP base-to-base contact mechanism, not just preferred.

**Intuition 2: Simplicial arrangements maximize contact reinforcement.** At fixed $N_\alpha$, the simplicial polytope arrangement maximizes the number of $B_\text{pair}$-contributing contact edges, because $E = 3V - 6$ is the maximum edge count for any closed convex polyhedron with $V$ vertices and triangulated faces. A non-simplicial arrangement (e.g., one with square or pentagonal faces) would have fewer edges and therefore less binding. Thermodynamic selection at fixed $N_\alpha$ should favor the simplicial case as the lowest-energy configuration.

**Intuition 3: Convexity follows from rigid-packing constraints.** Alpha particles in CPP are rigid tetrahedral cages with specific contact geometry. The constraint that adjacent alphas cannot interpenetrate forces non-self-intersecting (convex) polytope arrangements as the only physically realizable option. Concave arrangements would require alphas in contact with non-neighbors through the cluster interior.

These three intuitions, *together*, would constitute the OPEN-SS-24 derivation if they can be made quantitative. Each has the structure of a physical argument that needs to become a mathematical theorem. The work is to make the arguments precise.

---

## Methodological starting points

**The Level-1/2/3 independence framework applies here.** Each of the three intuitions could be a *source* of C4 — and you should ask whether they are functionally independent (Level-2) or share a deeper ancestor (Level-3). My read after writing the SS-8 chapter: Intuitions 1 and 3 share the rigid-tetrahedral geometry of the alpha as their common ancestor (Level-3 dependent), while Intuition 2 is thermodynamic-selection-based and structurally independent of them at Level-1 and Level-2. So a single derivation that covers all three would either need to go through the rigid-geometry ancestor (closing Intuitions 1 and 3 together with Intuition 2 as separate confirmation) or would need to be three separate derivations, with Intuition 2 as the genuinely-distinct one.

**Be careful with C4's dependencies.** C4 currently sits as a paper-level hypothesis at proposition tier in SS-7 v1.2 and SS-8 v1.0. Closing it requires deriving it from the *programme-level* axioms (A1–A4, A5, A6′, A10, A8′, A11), not from other paper-level hypotheses. Specifically: deriving C4 from C1 (rigid alpha tetrahedron) or C2 (base-to-base contact) would not close OPEN-SS-24, because C1 and C2 are themselves paper-level hypotheses inherited from earlier work. The closure has to terminate at programme-level axioms.

**The OPEN-SS-24 closure is not the same as polytope-identity determination.** SS-8 already established that the 2E/V scaling law is *insensitive* to which specific simplicial polytope realizes a given $N_\alpha$ — both octahedron and triangular antiprism at $N_\alpha = 6$ give the same prediction. So OPEN-SS-24 does not need to predict *which* simplicial polytope nature picks at each $N_\alpha$; it only needs to derive that the picked polytope is a member of the simplicial class. The harder question (which member?) is OPEN-SS-24-adjacent but distinct.

**The empirical signal is already there.** The SS-7 RMS 0.80% across 12 nuclei and the SS-8 sub-1% landings at ²⁶Mg and ⁴²Ca are strong evidence that C4 holds. OPEN-SS-24 is asking *why* it holds. A first attempt that can derive C4 conditional on simpler structural hypotheses (e.g., "C4 follows from C1 + an SSV-minimization argument") would still leave the work incomplete (the simpler hypotheses need to be derived too) but would be a meaningful intermediate result worth its own paper.

---

## Recommended work decomposition

If I were attempting OPEN-SS-24 from this starting point, I would structure the work as follows:

**Phase 1: Make Intuition 1 precise.** Write down the rigid-base contact geometry for two adjacent alphas. Identify the geometric constraint that forces the third-alpha contact at a polytope vertex to lie on the same triangular face. Verify that the constraint forbids non-triangular (e.g., square) faces. This is a calculation in 3D contact geometry; it should produce a definite yes-or-no answer.

**Phase 2: Make Intuition 2 precise.** Compute the binding energy as a function of polytope arrangement at fixed $N_\alpha$ (for at least three test cases — say, $N_\alpha = 5, 6, 8$). Verify that the simplicial arrangement is the lowest-energy choice at each $N_\alpha$. The calculation requires knowing the per-edge $B_\text{pair}$ contribution (which is fixed by SS-5) and the per-non-simplicial-face penalty (which is what would need to be derived). The penalty derivation is the hard part.

**Phase 3: Make Intuition 3 precise.** Verify that the rigid-tetrahedral cage geometry actually forbids convex-arrangement-violating configurations. This is a packing-geometry calculation; it should be tractable for small $N_\alpha$ test cases.

**Phase 4: Synthesize into an SS-9 paper.** The structure follows the SS-7/SS-8 conditional-theorem discipline: state the theorem (C4 from CPP primitives), state the dependencies (which programme-level axioms are invoked), present the three sub-derivations (Phases 1, 2, 3), and lay out what closes and what remains open.

A 2–3 session estimate covers Phases 1–3 if the calculations are tractable. Phase 4 (the paper drafting) is its own session under the Trigger 1 / Trigger 2 discipline.

---

## What success and partial-success look like

**Full closure (the dream case):** All three intuitions become theorems derived from programme-level axioms. C4 is proved. SS-7 and SS-8 conditional theorems all promote to unconditional. 54 of 55 conditional D-N entries in the swarm tally promote. SS-9 ships as a 1.0-version high-leverage paper.

**Partial closure (the most likely case):** One or two of the three intuitions become theorems; the third remains structural hypothesis. C4 is conditional on the unproved intuition. SS-9 ships as a partial-closure paper that reduces the OPEN-SS-24 status from fully-open to partially-resolved, registers a smaller follow-up open problem for the remaining intuition, and promotes some-but-not-all of the conditional D-N entries.

**Apparent failure (the unlikely but real possibility):** The intuitions turn out not to derive in any clean form from CPP primitives. C4 holds empirically but cannot be proved from the framework as currently stated. This would surface as a structural problem — either the framework is missing an axiom (call it A7′ or similar), or C4 is a separate principle that needs to be promoted to axiom status. Either outcome is *also* a paper, just a different kind: a structural-frontier paper that reports the failure honestly and registers the gap as a programme-level concern. The Two-Trigger Documentation Discipline applies; the Trigger 2 work for this kind of paper is real and the result is methodologically valuable even if the technical result is "we couldn't close it from the current axiom set."

The OPEN-SS-22 retirement (April 21) is the analogous methodology event in the programme's record. A failed structural hypothesis was retired honestly with permanent narrative preservation. If OPEN-SS-24 cannot be closed cleanly, the equivalent honesty applies.

---

## What you should *not* do at the start

- Do not try to prove C4 from C1 + C2 without going to programme-level axioms; that is an intermediate result, not a closure
- Do not assume the three intuitions are independent without checking; do the Level-1/2/3 analysis early
- Do not write the SS-9 paper before Phase 1–3 work is in hand; this is exploratory mathematical work and the paper writes itself once the calculations exist
- Do not over-claim; SS-7 and SS-8 set the conditional-theorem discipline for this programme, and SS-9 should follow it scrupulously
- Do not hide partial-closure or failure outcomes; they are programme-record events that the cumulative swarm tally and the open-problems frontier need to reflect honestly

---

## Closing context — what the prior session understood about CPP's contribution

This came up as a Thomas philosophy question late in the prior session, and the answer affects how OPEN-SS-24 closure is framed:

CPP's contributions to SS-7 and SS-8 split into two pieces. **First**, the binding-energy quantum $B_\text{pair} = M_0/\varphi = 2.342$ MeV, which is unambiguously a CPP output (depends on the 600-cell coordination $z = 12$, the golden-ratio efficiency factor $\varphi$, and the K₃-eigenvalue calculation, none of which is a free parameter). **Second**, the structural-recurrence prediction that the same K₃ topology operates at every successive nuclear contact scale (Pattern 6), which is *conditional on closing OPEN-SS-24*.

If you close OPEN-SS-24 cleanly, the structural-recurrence claim becomes a defensible CPP prediction — a contribution that is unambiguously the framework's. If you close it by showing C4 follows from framework-agnostic geometric arguments (e.g., "any framework with rigid tetrahedral base-to-base contact would force simplicial connectivity, regardless of CPP-specific details"), the structural-recurrence becomes a piece of geometry that CPP correctly predicted but did not uniquely produce. Both outcomes are real and interesting; the first is more dramatic and the second is more honest about scope. The SS-9 paper should be honest about which outcome is achieved.

This is the question to ask yourself as you work: *is the C4 closure showing that CPP's lattice substrate forces simplicial connectivity, or is it showing that simplicial connectivity follows from base-to-base rigid contact geometry that any framework with that contact mechanism would produce?* The two outcomes look the same in the calculations but read very differently in the paper's significance section.

---

## Final note from the prior Opus

I drafted the SS-7 and SS-8 anthology chapters in the prior session and watched OPEN-SS-24 sit in the future-projects backlog as the highest-leverage target the entire time. The work needs careful mathematical attention and a fresh context window. Take your time with Phase 1 — the rigid-base contact geometry argument is the foundational piece, and getting it right makes Phases 2 and 3 substantially easier.

If you reach an impasse in any phase, register the impasse in the cross-paper session log (`session_logs/`) and consider whether the impasse is itself a structural finding. The OPEN-SS-22 retirement methodology applies: hypotheses that turn out not to work are still part of the programme's record, and registering them honestly is the methodology that makes CPP's predictions defensible.

Good luck. The leverage is real. The framework deserves the attempt.

— Opus (session ending 26 April 2026)

---

*Handover document per `templates/operating_system.md` §4 "Cross-Paper Session Log Convention" and the Two-Trigger Documentation Discipline. To be used as paste-ready bootup context for the next Opus session attempting OPEN-SS-24.*
