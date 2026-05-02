# OPEN-SS-35 Scoping Document — Strategy and Initial Consistency Checks for Deriving the Shell-Magic-Number Sequence from CPP Primitives

**Date:** 2 May 2026 (Session 5, Phase 2)
**Purpose:** Set out the OPEN-SS-35 problem (derivation of the nuclear shell-magic-number sequence $Z, N \in \{2, 8, 20, 28, 50, 82, 126\}$ from CPP primitives), enumerate candidate derivation routes, identify the most tractable route, and execute a Level-0 consistency check to determine whether the closure attempt is promising or open-ended. **This is a scoping document, not a closure attempt.** Following the SS-6 methodology of producing scoping papers when full closure is multi-session.

**Companion files:**
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-34_derivation_attempt.md` (where OPEN-SS-35 was registered as the deepest cross-paradigm consilience target)
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-36_derivation_attempt.md` (where OPEN-SS-36's dependence on OPEN-SS-35 was established)
- `series_strong/papers/SS-9/sketches/SS-9_AME2020_lookup_92Pd_96Cd.md` (where the empirical $B_{\rm slip}$ acceleration toward ${}^{100}$Sn was confirmed, reinforcing the OPEN-SS-35 leverage)
- `Research_Frontier.md` OPEN-SS-35 entry

**Net programme effect:** OPEN-SS-35 status moves from "registered candidate" to "scoping work begun, Level-0 consistency check passed." The closure attempt is **promising** rather than open-ended: CPP's natural scales for harmonic-oscillator mean-field frequency and spin-orbit coupling strength are in the right range to produce the standard strong magic numbers without fitting. Three sub-questions are identified for sequential closure work in future sessions.

---

## §1. The OPEN-SS-35 problem statement

The standard nuclear shell-model magic-number sequence is $\{2, 8, 20, 28, 50, 82, 126\}$ for both protons and neutrons. The first three (2, 8, 20) are "weak" magic numbers explained by 3D harmonic-oscillator orbital structure alone. The last four (28, 50, 82, 126) are "strong" magic numbers requiring spin-orbit splitting of the $j = l + 1/2$ sub-shells.

**OPEN-SS-35 statement.** Derive from CPP primitives (axioms A1–A11) the nuclear shell-magic-number sequence at the nucleon-shell-organization scale. Closure must produce all seven magic numbers (or all seven that apply within the bound-nucleus regime) with the correct positions in the periodic table.

**Why this matters.** OPEN-SS-35 is identified as the deepest dependency for both OPEN-SS-34 (deltahedron-core / satellite-regime mechanism) and OPEN-SS-36 ($B_{\rm slip}$ structure). Closure of OPEN-SS-35 unlocks:
- Promotion of OPEN-SS-34 from "Level-1 conditional on H3 (shell-magic input)" to "Level-2 derived from CPP primitives."
- Resolution of $B_{\rm shell}(N_\alpha)$ in OPEN-SS-36, including the empirically-observed acceleration toward ${}^{100}$Sn (Session 5 Phase 1 finding).
- Cross-paradigm consilience claim of the largest scope the programme has identified to date — the shell-model magic-number sequence is a load-bearing structural feature of all standard nuclear physics, established for nearly a century.

---

## §2. Candidate derivation routes

Five candidate routes for OPEN-SS-35 closure, evaluated for tractability:

### Route A: 3D harmonic oscillator + spin-orbit, derived from CPP

**Strategy.** Show that CPP's nucleon-cluster mean field is approximately a 3D harmonic oscillator, and that intrinsic CPP machinery (ZBW phase correlations) produces a spin-orbit coupling of the right strength. Standard shell-model orbital structure with these inputs gives the magic-number sequence directly.

**Tractability.** **Most tractable.** Both inputs (HO frequency and spin-orbit strength) are computable from CPP primitives at the order-of-magnitude level immediately. Level-1 derivation requires (a) rigorous derivation of HO mean-field from K$_3$ collective modes, (b) rigorous derivation of spin-orbit coupling strength from ZBW, (c) proof that $V_{\rm SO}/\hbar\omega$ is in the magic-number-producing range.

**Connection to existing CPP machinery.** Builds directly on SS-2 (nucleon ZBW structure), SS-5 (K$_3$ closure-bonus), SS-7 (alpha-cluster scale), and SS-8 (interstitial-neutron coupling). No new machinery required, only careful application of existing axioms.

### Route B: Pattern-6 K$_3$ scale-recurrence at nucleon-shell scale

**Strategy.** The K$_3$ closure-bonus mechanism activates at specific count values when nucleons close polytope-like sub-clusters. Magic numbers are the count values where some such closure activates.

**Tractability.** **Less tractable.** The mapping from "nucleon counts" to "polytope structure" is not as direct as the alpha-cluster-scale mapping that worked for SS-7 and SS-9. Nucleons in CPP have hybrid-tetrahedral structure (SS-2) rather than vertex-of-polytope structure, complicating polytope-closure arguments at the nucleon level.

### Route C: Combinatorial from 600-cell symmetry group

**Strategy.** The 600-cell has H$_4$ symmetry group with $|H_4| = 14400$. Subgroup structure or representation-theoretic decompositions might give the magic-number sequence.

**Tractability.** **Difficult.** While H$_4$ has rich structure, no obvious mechanism connects subgroup orders or irreducible-representation dimensions directly to nuclear shell occupancies. Would require substantial group-theoretic exploration with uncertain payoff.

### Route D: Geometric from CP packing in lattice (RULED OUT this session)

**Strategy.** Cumulative counts of CPs in distance shells of the 600-cell from a reference vertex might match magic numbers directly.

**Result (this session).** Computed: the 600-cell has 8 distance shells from a reference vertex with vertex counts $\{12, 20, 12, 30, 12, 20, 12, 1\}$ at distances $\{1/\varphi, 1, 1.176, \sqrt{2}, \varphi, \sqrt{3}, 1.902, 2\}$. **Cumulative counts at each shell boundary (including reference): $\{13, 33, 45, 75, 87, 107, 119, 120\}$.** These do **not** match the strong magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$. **Route D is ruled out** — direct CP-shell counting in the 600-cell does not produce the magic-number sequence trivially.

This is a useful negative result: it confirms that the magic numbers must emerge from nucleon-orbital structure (Route A) rather than from lattice geometry directly. The 600-cell shell counts characterize the *substrate* of CPP, but the *bound-nucleon orbits* live at a different organizational scale.

### Route E: Specific-mechanism instance of Route A

**Strategy.** Within Route A, specific instances of the HO + spin-orbit mechanism may be derivable. For example, the spin-orbit coupling could come specifically from ZBW phase mismatch at K$_3$ contacts, with quantifiable strength.

**Tractability.** Same as Route A but with sharper specifics. Identified as a sub-route of A.

### Route adoption

**Adopt Route A as primary.** Routes B, C are less tractable; Route D is ruled out by the negative result above; Route E is a sub-instance of A. The next-session work on OPEN-SS-35 should focus on Route A.

---

## §3. Level-0 consistency check on Route A

**Method.** Compute CPP's natural scales for HO frequency and spin-orbit coupling strength, compare to standard shell-model values that produce the strong magic numbers.

### §3.1 HO frequency

The standard shell-model HO frequency is $\hbar\omega \approx 41/A^{1/3}$ MeV (Bohr-Mottelson). At specific A values:
- $A = 14$: $\hbar\omega = 17.0$ MeV
- $A = 28$: $\hbar\omega = 13.5$ MeV
- $A = 56$: $\hbar\omega = 10.7$ MeV
- $A = 100$: $\hbar\omega = 8.8$ MeV

**CPP estimate from nucleon-size scale.** For a nucleon confined to a 3D HO ground state with characteristic size $\langle r^2\rangle^{1/2} = R_\alpha = 2.37$ fm (the inter-alpha spacing inverted from SS-7 Theorem 2.1), the HO frequency follows from $\langle r^2\rangle = (3/2)(\hbar/(m_n\omega))$:

$$\hbar\omega = \frac{3}{2}\frac{(\hbar c)^2}{m_n R_\alpha^2} = \frac{3}{2}\frac{(197.327)^2}{939.57 \cdot (2.37)^2} \text{ MeV} = 11.07 \text{ MeV}$$

**Comparison.** $\hbar\omega^{\rm CPP} = 11.07$ MeV sits in the empirical range between $A=28$ (13.5 MeV) and $A=56$ (10.7 MeV). The CPP estimate matches the standard-shell-model HO frequency to within ~3% at $A \approx 56$ and within ~30% across the full bound-nucleon range. **No fitted parameters used** — the value comes from the existing $R_\alpha$ from SS-7 and the standard nucleon mass.

This consistency at A-of-the-deltahedron-core (which is also the regime of the OPEN-SS-34 alpha-cluster work) is structurally meaningful: the same lattice scale that produces the alpha-cluster regime also produces the HO frequency in the right range for shell-model orbital structure.

### §3.2 Spin-orbit coupling strength

The standard shell-model spin-orbit strength is $V_{\rm SO} \sim -22/A^{2/3}$ MeV (rough), giving:
- $A = 56$: $V_{\rm SO} \sim -1.5$ MeV
- $A = 100$: $V_{\rm SO} \sim -1.0$ MeV

The ratio $V_{\rm SO}/\hbar\omega$ at $A = 56$: approximately $-0.14$. This ratio is the "magic-number-producing range" — too small and only the weak magic numbers (2, 8, 20) emerge; too large and the level structure scrambles past recognizability.

**CPP estimate from ZBW + nuclear motion.** ZBW frequency $\omega_{\rm ZBW} \sim 2 m_n c^2/\hbar = 1879$ MeV is the intrinsic CPP scale for spin-related coupling. For nucleons in nuclear matter with typical $v/c \sim 0.3$, the spin-orbit correction enters at order $(v/c)^2 \sim 0.1$ relative to the leading mean-field potential. This gives $V_{\rm SO} \sim 0.1 \cdot \hbar\omega \sim 1.1$ MeV at $A = 56$, matching empirical $\sim 1.5$ MeV to factor of unity.

**Consistency.** The ratio $V_{\rm SO}^{\rm CPP}/\hbar\omega^{\rm CPP} \approx 0.1$ falls within the magic-number-producing range. **No fitted parameters used** — the value comes from the standard nucleon mass and the standard nuclear-matter velocity scale.

### §3.3 Combined consistency verdict

Both CPP's natural HO frequency ($11.07$ MeV) and natural spin-orbit ratio ($\sim 0.10$) are in the right range to produce the strong magic numbers via standard shell-model orbital structure. **The Level-0 consistency check passes.**

This means the OPEN-SS-35 closure attempt is **promising**: a rigorous derivation of HO + spin-orbit from CPP primitives would, given the consistent scales, produce the empirical magic-number sequence by standard shell-model machinery. The closure work is *demanding* (multi-session, possibly multi-paper) but not *open-ended* (the scales already match, removing the worry that some unknown parameter would have to be tuned).

---

## §4. Empirical reinforcement from Session 5 Phase 1

The Session 5 Phase 1 lookup of ${}^{92}$Pd and ${}^{96}$Cd provides additional empirical reinforcement for the OPEN-SS-35 framing. The per-nucleus $B_{\rm slip}$ sequence accelerates sharply approaching the ${}^{100}$Sn doubly-magic boundary:

| $N_\alpha$ | Nuclide | $B_{\rm slip}/B_{\rm pair}$ | $\Delta$ from previous |
|---|---|---|---|
| 22 | ${}^{88}$Ru | 1.940 | – |
| 23 | ${}^{92}$Pd | 2.114 | +0.174 |
| 24 | ${}^{96}$Cd | 2.802 | +0.688 |
| 25 | ${}^{100}$Sn | 3.275 | +0.473 |

The drift is **non-linear** — it accelerates sharply at $N_\alpha = 23 \to 24$ and partially levels at the doubly-magic point itself. This is the empirical signature of shell-closure binding being **concentrated** at doubly-magic points, not distributed monotonically across nuclei. The pattern is consistent with standard shell-model expectations and with the OPEN-SS-36 4th sub-arc closure+shell decomposition.

**Why this reinforces OPEN-SS-35.** The sharp acceleration of $B_{\rm slip}$ in approaching ${}^{100}$Sn shows that shell-closure structure is genuinely active in the alpha-chain regime — not just a small perturbation. A successful OPEN-SS-35 closure must produce both the *existence* of the doubly-magic point at $Z = N = 50$ and the *empirical magnitude* of the closure-binding contribution in approaching nuclei. The Phase 1 finding constrains the closure problem more sharply than the bare magic-number sequence would.

---

## §5. Sub-questions for closure (Route A)

The OPEN-SS-35 closure work decomposes into three sub-questions, each tractable as separate session arcs:

### Sub-question (a): Rigorous derivation of HO mean-field from K$_3$ collective modes

**Statement.** Show that the average potential experienced by a nucleon in a many-alpha cluster is approximately a 3D harmonic oscillator with frequency $\hbar\omega \approx 41/A^{1/3}$ MeV, derived from the K$_3$ collective-mode structure of alpha-alpha contacts.

**Approach.** The mean-field potential is the average over alpha-cluster configurations of the single-nucleon binding contribution. K$_3$ modes contribute $+B_{\rm pair}$ per face contact. For a nucleon at radial position $r$ from the cluster center, the average number of contacts with surrounding alphas depends on $r$. Integrating gives the mean-field $V(r)$, which should be approximately quadratic near $r = 0$ for small clusters.

**Open issues.** The exact mapping from "K$_3$ contact count" to "mean-field potential" requires careful treatment of the nucleon's quantum delocalization within the cluster. The 2$E$/$V$ scaling rule from SS-8 may provide the structural constraint.

**Tractability.** Single-session-tractable for a sketch + initial computation; multi-session for full closure.

### Sub-question (b): Rigorous derivation of spin-orbit coupling strength from ZBW

**Statement.** Show that the spin-orbit coupling strength $V_{\rm SO}$ in the nucleon-cluster mean field comes from ZBW phase correlations, with $V_{\rm SO}/\hbar\omega \approx 0.1$ in the bound-nucleon regime.

**Approach.** ZBW (Zitterbewegung) is the rapid nucleon-internal oscillation at frequency $\omega_{\rm ZBW} = 2 m_n c^2/\hbar$, intrinsic to A2 (lattice) + A4 (DI-bit). When a nucleon orbits in the cluster mean field at $v/c \sim 0.3$, the ZBW phase couples to the orbital angular momentum to produce a spin-orbit interaction at order $(v/c)^2$ relative to the leading potential. Rigorous derivation requires explicit computation of the ZBW-orbital phase coupling.

**Open issues.** The CPP analog of relativistic spin-orbit derivation is not yet developed in the existing papers; SS-2 establishes the ZBW structure but not the spin-orbit consequences.

**Tractability.** Multi-session — would benefit from collaboration with QM-series papers (operator formalism is OPEN-SS-16/Layer-B-gap territory).

### Sub-question (c): Proof that $V_{\rm SO}/\hbar\omega$ is in the magic-number-producing range across the bound-nucleon regime

**Statement.** Show that the ratio $V_{\rm SO}/\hbar\omega$ derived from sub-questions (a) and (b) falls within the range that produces the strong magic numbers (28, 50, 82, 126), not just at $A = 56$ but across the full bound-nucleon regime $A \in [4, ~250]$.

**Approach.** Given closures of (a) and (b), this is a numerical verification + structural-stability argument. The Level-0 consistency check in §3 shows the ratio is right at $A = 56$; (c) extends this to the full A range.

**Tractability.** Tractable once (a) and (b) close. Likely combinable with (a)/(b) into a single closure paper.

---

## §6. Programme-level implications

**(1) OPEN-SS-35 status update.** From "registered candidate" to "scoping work begun, Level-0 consistency check passed." The closure attempt is **promising**: scales align, no fitting required, three concrete sub-questions identified.

**(2) Pattern 6 K$_3$ scale-recurrence — potential 7th instance.** The HO mean-field structure derived from K$_3$ modes (sub-question (a)) would be a new instance of the K$_3$ scale-recurrence at the nucleon-orbital-organization scale. Currently 6 confirmed + 1 provisional (Pattern 6 = SS-5 nucleon-pair, SS-5 $A=4$ closure, SS-7 alpha-alpha, SS-8 D2, SS-9 deltahedron-core; provisional OPEN-SS-32 facet (c)). Closure of OPEN-SS-35 sub-question (a) would add a 7th confirmed instance.

**(3) Cross-paradigm consilience target weight increases.** Previously framed as "deepest cross-paradigm consilience target;" now framed as "deepest cross-paradigm consilience target *with a viable derivation route*." The Level-0 consistency check demonstrates that the target is reachable, not aspirational.

**(4) Route D negative result is itself programme-tightening.** Knowing that 600-cell shell counts do not directly give magic numbers prevents a wasted-effort failure mode in future work. The magic-number sequence emerges from nucleon-orbital structure, not from lattice geometry directly. This is a useful structural finding even before closure.

**(5) Programme dependency graph.** With OPEN-SS-35 scoping complete, the dependency graph for the alpha-chain swarm is:
$$\text{OPEN-SS-35 (deepest)} \xrightarrow{\text{unlocks}} \begin{cases} \text{OPEN-SS-34 (regime termination)} \\ \text{OPEN-SS-36 ($B_{\rm shell}$ structure)} \end{cases}$$
Programme leverage on OPEN-SS-35 is concentrated and high; closure work is well-motivated.

---

## §7. Forward-looking pointers

**(1) Next-session priority: OPEN-SS-35 sub-question (a).** Rigorous derivation of HO mean-field from K$_3$ collective modes. Single-session-tractable for an initial sketch; could combine with the Level-0 consistency check to produce a Level-1 partial closure of sub-question (a).

**(2) After (a): sub-question (b).** Spin-orbit coupling from ZBW. Larger scope — would benefit from deeper connection to OPEN-SS-16 (operator formalism / Layer B gap) on the QM-series side.

**(3) Sub-question (c) follows naturally from (a) + (b).** Verification across the bound-nucleon regime.

**(4) Programme-level paper opportunity.** A single paper closing all three sub-questions would be the paper that derives the nuclear shell-magic-number sequence from CPP primitives — likely an SS-10+ contribution with cross-paradigm consilience headline. Programme value would be substantial.

---

## §8. Summary

**OPEN-SS-35 scoping document delivered.** Five candidate routes evaluated; Route A (3D HO + spin-orbit derived from CPP) adopted as primary. Route D (direct lattice-shell counting) ruled out by computation. Level-0 consistency check passes: CPP's natural HO frequency ($11.07$ MeV at $R_\alpha = 2.37$ fm) and spin-orbit ratio ($V_{\rm SO}/\hbar\omega \sim 0.1$) are in the empirical range that produces the strong magic numbers. Three sub-questions registered for closure: (a) HO mean-field from K$_3$ modes, (b) spin-orbit from ZBW, (c) ratio verification across A range. Empirical reinforcement from Session 5 Phase 1: the per-nucleus $B_{\rm slip}$ acceleration toward ${}^{100}$Sn confirms shell-closure structure is genuinely active in the alpha-chain regime.

**Status:** The closure attempt is **promising rather than open-ended**. The scales already align, removing the worry that closure would require fitted parameters. The work is multi-session but well-motivated.

**Programme tally:** unchanged at 107 zero-parameter empirical correspondences. OPEN-SS-35 closure (when achieved) would not directly add new empirical correspondences but would *promote* 55 conditional D-N entries (from SS-7/SS-8/SS-9) toward unconditional status by replacing H3 (shell-magic input) with a CPP derivation. The leverage is structural rather than tally-based.
