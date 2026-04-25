# FAQ — SS-8: Interstitial-Neutron Binding and the 2E/V Scaling Law on the Alpha-Polytope

**Location:** `/CPP/series_strong/papers/SS-8/documentation_suite/FAQ-SS-8.md`
**Last updated:** 26 April 2026 (v1.0 currency)
**Companion to:** `SS-8_interstitial_neutron_2EV_scaling.tex` (v1.0)

This is a living document. New questions are added as they arrive from readers, seminars, web traffic, or future AI sessions.

---

## Conceptual Questions

### Q: What does SS-8 actually predict?

**A:** When you add a neutron to an alpha-cluster nucleus (one already made of $N_\alpha$ alpha particles in a strict-$N=Z$ configuration), how much extra binding energy does that neutron get? SS-8 says: $\Delta_1 = (6 - 12/N_\alpha) \cdot 2.342$ MeV, with no adjustable parameters. The number 2.342 MeV is inherited from earlier CPP papers; the $(6 - 12/N_\alpha)$ factor is pure graph theory (the average vertex degree of any simplicial 3-polytope, by Euler's formula). For ${}^{26}$Mg ($N_\alpha = 6$) the prediction is 9.37 MeV; observed is 9.39 MeV — a 0.2% match.

### Q: Why is this interesting?

**A:** Most nuclear-physics calculations require fitting multiple parameters per shell or per mass region. SS-8's prediction has zero new parameters and reproduces observed binding to better than 15% across 11 of 12 nuclei from ${}^{12}$C through ${}^{56}$Ni, with two sub-1% matches at the most symmetric polytopes. The geometric content is also striking: the binding depends only on $N_\alpha$ via a simple combinatorial formula, not on which specific polyhedron the alpha cluster realizes.

### Q: What's an "alpha-polytope"?

**A:** A geometric arrangement where the $N_\alpha$ alpha particles in a nucleus sit at the vertices of a closed convex polyhedron with all-triangular faces. SS-8 inherits this picture from SS-7. For $N_\alpha = 4$ it's a tetrahedron; for $N_\alpha = 6$ it's an octahedron (the same shape as a polished gemstone with 8 triangular faces); for $N_\alpha = 12$ it's an icosahedron. The polyhedron's structure determines how many alpha-alpha contacts there are, and SS-8's central result is that the per-neutron binding strength depends on the average vertex degree.

### Q: Where does the 2.342 MeV come from?

**A:** It comes from SS-5 (light-nuclei binding paper). At the nucleon-nucleon contact face inside an alpha particle, a particular collective mode of the K₃ graph (the complete graph on 3 vertices) has an eigenvalue that, when combined with the electron-mass calibration constant from earlier CPP work, gives 2.342 MeV. SS-7 then showed the same eigenvalue produces the same 2.342 MeV at a different physical scale — alpha-alpha contact faces. SS-8 is the third scale: interstitial-neutron contact at an alpha-vertex, same 2.342 MeV. Same quantum, three scales, no rescaling.

### Q: What's a "conditional theorem"?

**A:** A theorem proved under stated hypotheses that are not themselves proved. SS-8's central scaling law (THEO-SS-15) is conditional on hypotheses C1–C4 (inherited from SS-7) plus D1–D3 (introduced in SS-8 itself). The conditional dependencies are spelled out explicitly in the theorem statement, in the abstract, and in the swarm-tally header. None of them are CPP axioms; all are paper-level structural assumptions tracked as open problems for future derivation.

### Q: What's the cascade between SS-5, SS-7, and SS-8?

**A:** SS-5 derived $B_\text{pair} = 2.342$ MeV at the nucleon-nucleon contact scale (light nuclei: deuteron, triton, helium-3, helium-4). SS-7 used the same quantum at the alpha-alpha contact scale (medium-mass nuclei: ${}^{12}$C through ${}^{56}$Ni). SS-8 uses it again at the interstitial-alpha contact scale. The same K₃ graph structure operates at each scale, only at successively coarser physical resolution. This three-scale recurrence is documented in the axiom registry as Pattern 6.

---

## Technical Questions

### Q: Why specifically $6 - 12/V$?

**A:** Pure graph theory. For any simplicial 3-polytope with $V$ vertices, Euler's formula $V - E + F = 2$ combined with the triangle constraint $2E = 3F$ gives $E = 3V - 6$. The average vertex degree is $\bar{d}_v = 2E/V$, where the factor of 2 accounts for each edge contributing to two endpoints. So $\bar{d}_v = 2(3V-6)/V = 6 - 12/V$. As $V$ grows, the average vertex degree approaches 6 — the same average that holds for the infinite hexagonal-ish triangulation of the plane, and for the same reason.

### Q: How do you handle polytope-identity ambiguity?

**A:** At certain $N_\alpha$ values, more than one simplicial deltahedron exists. At $N_\alpha = 6$, the octahedron and the triangular antiprism are both simplicial deltahedra. SS-8 v1.0 doesn't try to pick one — the central scaling law's prediction depends only on $V = N_\alpha$, not on which specific polyhedron is realized, so the prediction is the same in both cases. This polytope-insensitivity is precisely why SS-8 succeeds at the polytope-identity-ambiguous cases ${}^{26}$Mg ($N_\alpha = 6$) and the $N_\alpha = 12$ case to within 1–2%. Identifying which polytope is realized in nature is OPEN-SS-24 (a separate research target).

### Q: What's "$N_\text{ex}$"?

**A:** The number of interstitial neutrons added to the strict-$N=Z$ alpha-chain baseline. The primary regime studied is $N_\text{ex} = 2$ (two extra neutrons, like ${}^{26}$Mg = 6 alphas + 2 extra neutrons). The secondary 30-cell extension covers $N_\text{ex} \in \{3, \ldots, 8\}$ at acknowledged-looser precision (8–15% rather than the primary band's <15%) because the bulk-regime averaging assumption D3 weakens as $N_\text{ex}/V$ grows.

### Q: What is D1, D2, D3?

**A:** Three paper-level structural hypotheses introduced in SS-8 to enable the derivation:
- **D1**: An interstitial neutron localizes at an alpha-vertex (rather than at an edge-midpoint, face-center, or polytope centroid). Promoted to a conditional theorem at Level-1+2 independence under two functionally independent realizations (Models A and B). Level-3 independence open as OPEN-SS-26 PARTIAL.
- **D2**: The K₃-edge bonds of contact faces incident at the host vertex couple to the host alpha's outer-nucleon contact face, transmitting binding strength $B_\text{pair}$ per edge. Proposition tier; OPEN-SS-27 targets the derivation via an A6′ extension.
- **D3**: Under bulk-regime conditions ($N_\text{ex}/V \ll 1$), interstitial neutrons distribute approximately uniformly across alpha-vertices, so the per-neutron binding averages to $\bar{d}_v \cdot B_\text{pair} = (6 - 12/V) \cdot B_\text{pair}$. Proposition tier; OPEN-SS-28 targets the derivation with explicit error bounds.

### Q: What is the Q2 algebraic-reduction analysis?

**A:** A test conducted during the SS-8 development cycle (22 April 2026) to verify that two distinct physical models for D1 — Model A (K₃-edge counting under D2) and Model B (short-range Yukawa pair physics) — do not reduce to one another by symbolic manipulation. Three discriminators distinguish them: multiplicity vectors (Model A predicts integer multiplicities; Model B predicts continuous decay), non-vertex orderings (Model A and Model B order non-vertex sites differently), and vertex-degree scaling (the two models predict different scaling exponents at high $\deg_v$). All three discriminators confirmed Models A and B are functionally independent, supporting D1's promotion to a Level-1+2 conditional theorem.

### Q: What's "Level-1/2/3 independence"?

**A:** A discipline introduced in SS-8 for evaluating multi-premise theorems:
- **Level-1**: Algebraic independence — the premises do not reduce to one another by symbolic manipulation.
- **Level-2**: Functional independence — the premises produce empirically distinguishable predictions.
- **Level-3**: Physical-principle independence — the premises do not share a deeper ancestor principle.
SS-8's D1 achieves Level-1+2; Level-3 is OPEN-SS-26 PARTIAL because both Models A and B share an implicit "proximity-binding" preprinciple (interstitials prefer to be near the alpha core).

---

## Comparison with Standard Model

### Q: How does this differ from the SM explanation of nuclear binding?

**A:** The Standard Model (specifically the nuclear shell model and liquid-drop model) treats binding energies as parameterized fits with multiple coefficients per shell or per mass region — pairing energies, symmetry coefficients, and so on. SS-8 derives a specific binding contribution (the single-neutron interstitial term) from pure geometry plus one programme-level inherited constant ($B_\text{pair}$), with zero SS-8-specific fitting. The SM and SS-8 agree on the empirical numbers; they disagree on whether those numbers require parameters to reproduce or follow from structural principles.

### Q: Does SS-8 replace the shell model?

**A:** No. SS-8 derives one specific contribution (interstitial-neutron binding on alpha-cluster nuclei) and inherits other contributions from earlier CPP papers (alpha-particle internal binding from SS-5; alpha-alpha contact binding from SS-7). The full nuclear-binding picture across the chart of nuclei is OPEN-SS-23 (currently partially resolved). SS-8 is one piece of the cascade, not a complete alternative framework.

### Q: How does the K₃-mode quantum compare to standard nuclear-physics constants?

**A:** $B_\text{pair} = 2.342$ MeV is roughly the deuteron binding energy (2.225 MeV) — that's not a coincidence; SS-5 derived $B_\text{pair}$ from K₃-mode analysis at the nucleon-nucleon contact scale and the deuteron is the simplest two-nucleon bound state, so the agreement is structural, not numerical luck. In standard nuclear physics, the deuteron binding is treated as an empirical input. In CPP, it falls out of the K₃-eigenvalue calculation.

---

## Challenges and Limitations

### Q: What's the strongest objection to SS-8 v1.0?

**A:** The Level-3 independence gap on D1. The two models for D1 (Model A — K₃-edge counting, Model B — short-range Yukawa pair physics) both invoke an implicit "proximity-binding" preprinciple. A skeptical reviewer can correctly point out that this is a shared physical-principle ancestor, so D1 is not fully independent at Level-3. SS-8 v1.0 acknowledges this explicitly in the theorem statement and registers it as OPEN-SS-26 PARTIAL. Closing the Level-3 gap requires either deriving proximity-binding from CPP primitives or constructing a third model that produces D1 without invoking proximity.

### Q: What if the bulk-regime approximation fails badly somewhere unexpected?

**A:** That's the falsification route for SS-8's secondary 30-cell extension. The 8–15% precision band is the explicit signature of D3's bulk-regime approximation degrading as $N_\text{ex}/V$ grows. If a future application of SS-8's formula to a bulk-regime polytope ($N_\alpha \gg N_\text{ex}$) shows residuals systematically larger than 15%, that would falsify D3 directly and force a re-examination of the central scaling law itself. Conversely, if the H4′ Pauli-decrement modification of D3 brings the secondary 30-cell residuals below 5%, that would tighten confidence in D3 substantially.

### Q: Why should I trust the "zero-parameter" claim if $B_\text{pair}$ depends on $m_e$?

**A:** "Zero-parameter" in the CPP programme means "zero new parameters relative to the inherited stack." The electron mass calibration is one programme-level constant carried unchanged from SS-7 → SS-8. SS-8 adds 42 predictions without introducing any SS-8-specific parameters; that's the precise sense of zero-parameter the paper claims. The paper is explicit about this in §4.2's zero-parameter-integrity audit. A more stringent reading ("zero parameters anywhere in the chain") is not what CPP claims and not what the paper asserts.

### Q: What if Pattern 6 fails at a fourth scale?

**A:** That's the test SS-9 (or a future paper) might run by applying $B_\text{pair} = 2.342$ MeV unchanged at a fourth physical scale where K₃-graph-structured contact occurs. Candidate scales: alpha-deuteron contact in ${}^6$Li, alpha-triton contact in ${}^7$Li. Preliminary inspection of ${}^6$Li gave residual alpha-deuteron binding 1.47 MeV vs. predicted $2 B_\text{pair}/3 \approx 1.56$ MeV — within 6%, suggestive but not yet a confirming fourth-scale test. If the fourth-scale test fails (the K₃ structure does not appear, or appears with a different quantum), Pattern 6 is downgraded from "structurally suggestive" to "three-scale coincidence." If it succeeds, the case for Pattern 6 as a forced rather than permitted recurrence strengthens.

### Q: What's the most ambitious follow-on from SS-8?

**A:** OPEN-SS-24 — first-principles derivation of C4 (alpha clusters realize simplicial polytope connectivity in bound nuclei) from CPP primitives. Closing OPEN-SS-24 would promote 54 of 55 conditional D-N predictions in the cumulative CPP swarm tally (12 SS-7 + 42 SS-8) from conditional to unconditional. That's the largest single-paper conditional-to-unconditional shift available in the programme, and it's the recommended SS-9 candidate per `future_projects.md` Project 0f.
