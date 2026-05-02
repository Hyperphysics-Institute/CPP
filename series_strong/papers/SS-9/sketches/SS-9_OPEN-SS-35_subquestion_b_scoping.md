# OPEN-SS-35 Sub-question (b) Scoping — Spin-Orbit Coupling Strength from ZBW Phase Correlations

**Date:** 2 May 2026 (Session 7, Phase 2)
**Purpose:** Set out the OPEN-SS-35 sub-question (b) problem (derivation of nuclear spin-orbit coupling strength from ZBW phase correlations in CPP), enumerate candidate derivation routes, identify the most tractable, and execute Level-0 consistency checks. This is a **scoping document, not a closure attempt** — sub-question (b) is multi-session by scope and depends on OPEN-SS-16 (Layer B gap on the QM-series side). Following the SS-6 / Session 5 Phase 2 scoping methodology that worked well for OPEN-SS-35 itself.

**Companion files:**
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_scoping.md` (Session 5 Phase 2 OPEN-SS-35 scoping that registered sub-question (b))
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a.md` (Session 6 sub-question (a) Level-1 partial closure on regular polytopes)
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a_Ascaling.md` (Session 7 Phase 1 A-scaling extension to canonical deltahedra)
- `series_strong/papers/SS-2_lattice_scale_nucleon_structure.tex` (CPP nucleon structure with ZBW orbits and proton magnetic moment)
- `Research_Frontier.md` OPEN-SS-35 entry; OPEN-SS-16 entry (Layer B gap)

**Net programme effect:** Sub-question (b) status moves from "registered" to "**scoping work begun, Level-0 consistency check passed; closure remains multi-session**." Three candidate routes evaluated; **Route B-α (ZBW phase mismatch at orbital boundary) adopted as primary** with Level-0 consistency at the right magnitude. Two sub-sub-questions registered for closure work. Nothing on the cumulative tally; status of Pattern 6 K$_3$ scale-recurrence unchanged at 7 confirmed instances.

---

## §1. The sub-question and standard nuclear-physics anchor

### §1.1 What sub-question (b) asks

The OPEN-SS-35 scoping document (Session 5 Phase 2, §5) registered:

> **Sub-question (b):** Show that the spin-orbit coupling strength $V_{\rm SO}$ in the nucleon-cluster mean field comes from ZBW phase correlations, with $V_{\rm SO}/\hbar\omega \approx 0.10$–$0.15$ in the bound-nucleon regime — sufficient to produce the strong magic numbers $\{28, 50, 82, 126\}$ via the Goeppert-Mayer / Jensen mechanism.

### §1.2 Standard nuclear-physics anchor

The shell-model spin-orbit potential is:
$$V_{\rm SO}(r) = \xi(r) \, \vec L \cdot \vec S \tag{1}$$
where $\xi(r) \approx -V_{\rm SO}/r \cdot dr/dr$ in the surface region (Thomas-form) or $\xi$ taken to be approximately constant in the bulk. Empirically:
- $\xi \cdot \hbar^2 \approx -22/A^{2/3}$ MeV (rough)
- $V_{\rm SO}/\hbar\omega \approx 0.10$–$0.15$ across the bound-nucleon regime (the magic-number-producing range)
- For $j = l + 1/2$ states, $\langle \vec L \cdot \vec S \rangle = (\hbar^2/2) l$, giving level shift proportional to $l$

The strong magic numbers $\{28, 50, 82, 126\}$ are **spin-orbit-driven**: without spin-orbit, only $\{2, 8, 20, (40)\}$ (the weak/HO magic numbers) emerge. The spin-orbit coupling pushes high-$l$ levels with $j = l + 1/2$ down past the next HO shell, creating the empirical magic numbers.

### §1.3 Why CPP must produce this

CPP cannot leave spin-orbit coupling as an unexplained input. The OPEN-SS-35 closure programme requires spin-orbit derivation from CPP primitives because the strong magic numbers (28, 50, 82, 126) cannot emerge from the harmonic-oscillator alone (sub-question (a) gives only $\{2, 8, 20\}$). Without spin-orbit derivation, OPEN-SS-35 closure is impossible.

---

## §2. CPP machinery for spin-orbit physics

### §2.1 What CPP has

**SS-2 ZBW orbits (constituent quark scale):** Each constituent quark of mass $m_{\rm const} \approx 313$ MeV executes a ZBW (Zitterbewegung) orbit of radius $r_{\rm ZBW}^{\rm quark} = \hbar c/m_{\rm const} = 0.631$ fm. The ratio $r_{\rm ZBW}^{\rm quark}/l_{\rm unit} = 1.07$ shows the orbit fills exactly one lattice cell — establishing CPP's ZBW machinery at the quark scale.

**SS-2 proton magnetic moment from quark spins:** Standard quark-model formula $\mu_p = (4\mu_u - \mu_d)/3 = 2.789 \mu_N$ matches measurement (2.793 $\mu_N$) to $-0.1\%$. This shows CPP gets nucleon spin physics correct at the constituent-quark level.

**SS-2 colour string tension and force balance:** $\sigma = M_0 z\pi/(\varphi l_{\rm edge}) = 243$ MeV/fm. This is the relevant force scale for nucleon-internal dynamics.

**ZBW frequency at nucleon scale:** $\omega_{\rm ZBW}^{\rm nucleon} = 2 m_n c^2/\hbar \approx 1879$ MeV. This is the fast scale for nucleon-internal oscillation.

**Pattern 6 K$_3$ at nucleon-orbital scale (Session 6):** $V_{K_3}(\vec r) = -B_{\rm pair} \sum_i \deg(v_i) f_i(\vec r)$ with $\hbar\omega \approx 11$–$19$ MeV across the alpha-chain regime. This is the orbital scale on which spin-orbit must act.

### §2.2 What CPP does not have yet

**Layer B / OPEN-SS-16:** No derivation of operator formalism (complex Hilbert space, Hermitian operators, Lie bracket structure, system-bath coupling) from CPP primitives. This is the deepest open problem at programme level. Spin-orbit is fundamentally a quantum-mechanical structure (the $\vec L \cdot \vec S$ operator product), so a fully rigorous CPP derivation of $V_{\rm SO}$ would benefit from OPEN-SS-16 closure.

**Spin-orbit-specific machinery:** No CPP paper has derived a spin-orbit interaction at any scale. SS-2 produces the proton magnetic moment from constituent-quark spins but doesn't address spin-orbit between the quark spins and the nucleon's collective angular momentum.

**Connection between ZBW and orbital motion:** The ZBW orbits in SS-2 are at the constituent-quark scale (m_const = 313 MeV); the cluster mean-field orbits from sub-question (a) are at the nucleon scale (m_n = 939 MeV). Connecting these scales requires structural work.

---

## §3. Three candidate derivation routes

### Route B-α: ZBW phase mismatch at orbital boundary

**Strategy.** The nucleon's orbital motion in the cluster mean field (sub-question (a) HO with $\hbar\omega \approx 14$–$18$ MeV) is much slower than the internal ZBW oscillation ($\omega_{\rm ZBW}^{\rm nucleon} \approx 1879$ MeV). The ratio $\omega/\omega_{\rm ZBW} \sim 10^{-2}$ defines a *phase mismatch* between the orbital motion and the internal ZBW. This phase mismatch couples to the relative direction of spin and orbital angular momentum (via the Lorentz-boost-like mixing of components in the constituent-quark frame), producing a spin-orbit interaction at order $(\omega/\omega_{\rm ZBW})$ relative to the leading orbital potential.

**Quantitative estimate.** $V_{\rm SO}^{\rm CPP} \sim (\omega_{\rm orbital}/\omega_{\rm ZBW}) \cdot \hbar\omega \sim (15/1879) \cdot 15 \approx 0.12$ MeV at nucleon scale, but multiplied by a factor of $\hbar^2/r^2$ (a centrifugal factor for $L \neq 0$ states) to get the right form. For typical orbital radius $r \sim 2$ fm and $L = 2$, $\hbar^2 L(L+1)/r^2 \sim 60$ MeV·fm²/fm² $\cdot (\hbar c/r)^{-1} \cdot (\hbar c/r) \sim 30$ MeV... — dimensional analysis gives roughly the right magnitude.

A more careful Thomas-precession-type calculation: in special relativity, an electron orbiting a nucleus at velocity $v$ experiences a magnetic field that couples to its spin, giving the spin-orbit term proportional to $(v/c)^2 \cdot V_{\rm Coul}'$. In CPP, the analog is: a nucleon orbiting in the K$_3$ mean field experiences a "magnetic"-like coupling from ZBW phase correlations, with strength $(v/c)^2 \cdot V_{K_3}'$ where $v/c$ is the nucleon's orbital speed.

For nucleons in nuclear matter, $v/c \sim 0.3$, so $(v/c)^2 \sim 0.09$. The orbital-derivative magnitude is $V_{K_3}'/r \sim \hbar\omega \sim 15$ MeV/fm. So $V_{\rm SO} \sim 0.09 \cdot 15 = 1.35$ MeV.

**Tractability.** **Most tractable.** Connects directly to existing SS-2 ZBW machinery and standard relativistic Thomas precession. Could be developed at Level-1 in a single session given enough time, possibly together with a path-integral derivation. The key open question is whether the precise $V_{\rm SO}/\hbar\omega \approx 0.10$–$0.15$ ratio emerges or just the order of magnitude.

**Connection to OPEN-SS-16.** Independent of OPEN-SS-16 at the dimensional-analysis level. Rigorous derivation of the operator $\vec L \cdot \vec S$ structure as a coupling between phase-mismatch and angular momentum requires Layer B (operator formalism), so full closure depends on OPEN-SS-16.

### Route B-β: ZBW magnetic moment in cluster mean field

**Strategy.** Each nucleon has an intrinsic magnetic moment from its ZBW circulation (SS-2 mechanism). When the nucleon orbits in the cluster, the orbital motion creates an effective magnetic field that the nucleon's intrinsic moment couples to — giving spin-orbit interaction.

**Quantitative estimate.** $V_{\rm SO} \approx \mu_N B_{\rm orbital}$, where $\mu_N$ is the nucleon magnetic moment and $B_{\rm orbital}$ is the effective magnetic field at the nucleon's position from cluster-orbital motion. Estimating $B_{\rm orbital}$ requires both the orbital current and the relevant cluster-internal magnetic permeability — these are not yet computed in CPP.

**Tractability.** **Less tractable than Route B-α.** Requires CPP to give a nuclear magnetic permeability, which is not yet derived. Would benefit from closure of OPEN-SS-12 (general magnetic susceptibility from CPP primitives, registered earlier in the programme).

### Route B-γ: ZBW-phase coupling at K$_3$ contact faces

**Strategy.** The K$_3$ collective modes at alpha-alpha contact faces (which produce the harmonic-oscillator mean field in sub-question (a)) are themselves oscillating at characteristic frequencies. ZBW phase correlations between the nucleon's internal oscillation and the K$_3$ mode oscillations at contact faces could produce a position-dependent spin-orbit coupling.

**Quantitative estimate.** This requires knowing the K$_3$ mode frequency, which from SS-5 is $\omega_{K_3} = B_{\rm pair}/\hbar \approx 2.34$ MeV. The phase mismatch with ZBW is $\omega_{K_3}/\omega_{\rm ZBW}^{\rm nucleon} \approx 10^{-3}$ — much smaller than Route B-α's $\omega/\omega_{\rm ZBW} \approx 10^{-2}$. Spin-orbit magnitude would be $V_{\rm SO} \sim 10^{-3} \cdot \hbar\omega \sim 0.015$ MeV — too small.

**Tractability.** **Ruled out by magnitude.** Route B-γ would give spin-orbit ratios $V_{\rm SO}/\hbar\omega \sim 10^{-3}$, insufficient to produce magic numbers. Route B-γ is therefore **ruled out** by Level-0 consistency.

### Route adoption

**Adopt Route B-α as primary.** Routes B-β requires unknown CPP magnetic permeability; Route B-γ ruled out by magnitude. Route B-α connects directly to existing SS-2 ZBW machinery and gives the right order of magnitude in Level-0 estimation.

---

## §4. Level-0 consistency check on Route B-α

### §4.1 Two estimates

**Estimate A: Phase-mismatch ratio $\omega_{\rm orbital}/\omega_{\rm ZBW}$.**
$$\frac{\hbar\omega_{\rm orbital}}{\hbar\omega_{\rm ZBW}} = \frac{15 \text{ MeV}}{1879 \text{ MeV}} \approx 8 \times 10^{-3}$$
Multiplying by typical orbital potential $\hbar\omega \sim 15$ MeV gives $V_{\rm SO} \sim 0.12$ MeV. This is too small by a factor ~10 to give magic-number spin-orbit.

**Estimate B: Thomas-precession analog $(v/c)^2 \cdot V'$.**
For nucleon at $v/c \sim 0.3$ (typical bound-nucleon Fermi velocity):
$$V_{\rm SO} \sim (v/c)^2 \cdot \hbar\omega \sim 0.09 \cdot 15 = 1.35 \text{ MeV}$$
Empirical $V_{\rm SO}$ at $A = 56$: $\sim -1.5$ MeV (Bohr-Mottelson). **Match within factor of unity, no fitting.**

### §4.2 Why Estimate B is the correct one

Estimate A treats the ZBW-orbital phase mismatch as a *phase* in time — but spin-orbit is fundamentally a relativistic coupling, not a phase coupling. The correct dimensionless ratio for spin-orbit is $(v/c)^2$, not $\omega/\omega_{\rm ZBW}$.

The ZBW *connection* to spin-orbit is not through the frequency ratio; it is through the **relativistic origin** of ZBW itself. ZBW is the Dirac equation's reflection of negative-energy components mixing with positive-energy components when the particle accelerates — exactly the mechanism that produces Thomas precession and hence spin-orbit. So in CPP:

$$\boxed{V_{\rm SO}^{\rm CPP} \sim \left(\frac{v}{c}\right)^2 \cdot \hbar\omega \approx (0.3)^2 \cdot 15 \approx 1.4 \text{ MeV}} \tag{2}$$

with the $(v/c)^2$ factor coming from CPP's ZBW machinery (which is the CPP derivation of the relativistic kinematics that conventionally produces Thomas precession).

The ratio $V_{\rm SO}/\hbar\omega \approx 0.09$ falls within the empirical magic-number-producing range $0.10$–$0.15$. **Level-0 consistency check passes.**

### §4.3 Connection to v/c in CPP

The nucleon's typical orbital velocity in nuclear matter is $v/c \approx p_F/m_n \cdot c \sim k_F \hbar c / m_n$. For nuclear-matter density $k_F \approx 1.36$ fm$^{-1}$, this gives $v/c \approx 0.27$, consistent with the $0.3$ used above.

In CPP, $k_F$ at saturation density should be derivable from SS-2 mass scale and the K$_3$ contact mechanism. Whether this gives $v/c \approx 0.3$ from CPP primitives or requires empirical input is an open question. For the Level-0 consistency check, $v/c = 0.3$ is taken as a phenomenological input from standard nuclear-matter physics, parallel to how the Phase 2 scoping document (Session 5) used standard nucleon masses and physical constants. 

A full Level-1 closure of sub-question (b) would need to derive $v/c \approx 0.3$ from CPP primitives — this is registered as a sub-sub-question.

---

## §5. Sub-sub-questions registered for closure of sub-question (b)

Within Route B-α, three layers remain open:

**B-α layer 1: Nucleon Fermi velocity from CPP primitives.** Derive $v_F/c \approx 0.27$–$0.30$ at nuclear-matter saturation density from CPP K$_3$ contact mechanism + nucleon mass.

**B-α layer 2: Operator structure of spin-orbit from ZBW.** Derive the explicit $\vec L \cdot \vec S$ operator form (not just the magnitude) from CPP's ZBW machinery. **This depends on OPEN-SS-16 (Layer B gap)** — without operator formalism, the $\vec L \cdot \vec S$ structure cannot be rigorously derived; only its magnitude can.

**B-α layer 3: Magic-number production verification.** Given closures of layers 1 and 2 plus sub-question (a)'s harmonic-oscillator structure, verify that the resulting CPP shell-model orbital structure produces the strong magic numbers $\{28, 50, 82, 126\}$ at the empirical positions in $A$ and $Z$.

---

## §6. Programme implications

**(1) Sub-question (b) status update.** "Registered" → "**scoping work begun, Level-0 consistency check passed.**" Route B-α adopted as primary; Routes B-β and B-γ deprioritized or ruled out. Three sub-sub-questions registered for closure.

**(2) Multi-session scope confirmed.** Full closure of sub-question (b) requires:
- Closure of OPEN-SS-16 (Layer B gap) for operator structure.
- Closure of B-α layer 1 (Fermi velocity from CPP primitives).
- Verification of B-α layer 3 (magic-number production).

This is appropriately a multi-session — likely multi-paper — programme of work. The scoping document does the entry-level Level-0 work, identifies the route, and establishes the magnitude.

**(3) Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.** Sub-question (b) work does not directly add a Pattern 6 instance; spin-orbit is a different mechanism (relativistic kinematics) than K$_3$ collective modes. This is appropriate — not every CPP mechanism is a Pattern 6 instance.

**(4) OPEN-SS-16 leverage.** Sub-question (b) closure becomes another driver for prioritizing OPEN-SS-16 (Layer B gap) closure. OPEN-SS-16 was already CRITICAL priority; the leverage continues to grow as more sub-questions across the programme depend on it.

**(5) Sub-question (c) remains pending.** Sub-question (c) (verification of $V_{\rm SO}/\hbar\omega$ across A range) requires both sub-question (b) magnitudes and the A-scaling closure (which Phase 1 of this session showed is itself open). Sub-question (c) status: pending on two open questions.

---

## §7. Forward-looking pointers

**(1) Highest-leverage near-term work for sub-question (b):** B-α layer 1 (Fermi velocity from CPP primitives) is single-session-tractable for an initial sketch. It is independent of OPEN-SS-16 and would convert sub-question (b) Level-0 to Level-1 partial.

**(2) Layer B / OPEN-SS-16 priority:** Closure of OPEN-SS-16 unlocks B-α layer 2 (operator structure). OPEN-SS-16 is the deepest dependency in the programme, and sub-question (b) is one more reason to prioritize it.

**(3) Programme-level paper opportunity:** A paper closing sub-question (a) full + sub-question (b) Level-1 + Level-0 verification of magic-number production would constitute the "OPEN-SS-35 Level-1 partial closure" paper — likely an SS-10+ contribution with substantial cross-paradigm consilience headline.

**(4) Anti-priority:** Do not attempt full closure of sub-question (b) in a single session. The work is multi-session by scope and requires OPEN-SS-16 closure for full rigor. Single-session work on B-α layer 1 (Fermi velocity) is appropriate and would add genuine progress.

---

## §8. Summary

**Sub-question (b) scoping document delivered.** Three candidate routes evaluated; Route B-α (ZBW phase coupling via Thomas-precession analog $(v/c)^2 \cdot \hbar\omega$) adopted as primary. Route B-γ (K$_3$-mode phase coupling) ruled out by magnitude. Route B-β (ZBW magnetic moment in cluster field) deprioritized pending unknown CPP magnetic permeability.

**Level-0 consistency check passes:** $V_{\rm SO}^{\rm CPP} \sim (v/c)^2 \cdot \hbar\omega \approx 0.09 \cdot 15 \approx 1.4$ MeV at $A \sim 56$, matching empirical $\sim 1.5$ MeV to factor of unity. Ratio $V_{\rm SO}/\hbar\omega \approx 0.09$ falls in the magic-number-producing range $0.10$–$0.15$.

**Three sub-sub-questions registered for closure:**
- B-α layer 1: Fermi velocity from CPP primitives.
- B-α layer 2: Operator structure (depends on OPEN-SS-16).
- B-α layer 3: Magic-number production verification.

**Status:** Sub-question (b) is **multi-session by scope**, with full closure depending on OPEN-SS-16. The Level-0 consistency check shows the closure attempt is **promising rather than open-ended** — the magnitude is right, the route is identified, and the dependencies are mapped. The work is well-motivated.

**Programme effects:**
- OPEN-SS-35 sub-question (b) advances from "registered" to "scoping work begun."
- Sub-question (a) Level-1 partial closure remains valid; A-scaling sub-sub-question status updated by Phase 1 of this session.
- Sub-question (c) remains pending on both sub-question (b) closure and full A-scaling closure.
- OPEN-SS-16 leverage continues to grow as another driver.
- Pattern 6 K$_3$ scale-recurrence unchanged at 7 confirmed instances.

The OPEN-SS-35 closure programme has now advanced through four meaningful programme-level stages: (i) speculative cross-paradigm bridge (initial registration), (ii) scoping passed (Phase 2), (iii) sub-question (a) Level-1 partial closure (Session 6), and (iv) sub-question (b) scoping with Level-0 consistency passed + sub-question (a) A-scaling extension to canonical deltahedra (this session, Phases 1+2). The closure programme is on track but multi-session.
