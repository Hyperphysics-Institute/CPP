# SM-3 Chapter Arc — *Two-Thirds*

**Paper:** SM-3 v6 — *The K₃ Spectral Theorem and the Koide Formula*
**Source files:**
- `series_standard_model/papers/SM-3_k3_spectral_theorem_koide_formula.tex`
- `series_standard_model/papers/mechanism-SM-3.md` (substantive content; very rich)
- `series_standard_model/papers/philosophy-SM-3.md`
- `series_standard_model/papers/reviews-SM-3.md`
- `series_standard_model/papers/development-SM-3.md`
- `series_standard_model/papers/phenomena-SM-3.md`

**Proposed chapter title:** *Two-Thirds*
**Proposed length:** 4,500–5,000 words
**Status:** Arc proposed; chapter not yet drafted.

---

## What SM-3 actually does

SM-3 derives the Koide ratio — a famous empirical relation among the three charged lepton masses — from CPP's K₃ spectral structure. The Koide ratio is

$$K = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$$

to 11 parts per million. It was discovered by Yoshio Koide in 1981 as an empirical curiosity. For forty-five years it has been one of the most striking unexplained numerical coincidences in particle physics — the three lepton masses, spanning five orders of magnitude (electron at 0.511 MeV, muon at 105.7 MeV, tau at 1777 MeV), satisfy this specific ratio exactly to within experimental precision. No known principle of the Standard Model predicts this. Many attempted derivations have been published; none has been generally accepted.

SM-3 derives $K = 2/3$ exactly from a four-step proof rooted in the eigenvalue structure of the K₃ graph (the complete graph on three vertices, the same K₃ that appears in the SS-5 → SS-7 → SS-8 cascade). The K₃ adjacency matrix has eigenvalues +2 (with multiplicity 1) and −1 (with multiplicity 2). Thermal equipartition over these eigenstates gives a 1:2 occupation ratio between bonding and antibonding sectors. This forces a specific modulation depth $\rho = \sqrt{2}$ in the Koide parametrization, and the algebraic identity $K = (1 + \rho^2/2)/3$ then gives $K = 2/3$ exactly. Zero free parameters.

The proof is conditional on a thermalisation assumption (Layer B in the paper's terminology) — the assumption that the ZBW orbital is in thermal equilibrium with the Dipole Sea at the Planck temperature, which gives equipartition over K₃ eigenstates. The thermalisation assumption is imported from open-system quantum mechanics rather than derived from CPP primitives in this paper. With that conditional acknowledged, the derivation is exact.

SM-3 also derives the related result that $K = (N+1)/(2N)$ for the general complete graph $K_N$, and that only $N=3$ gives the empirical value $2/3$. The three-vertex structure of the lepton cage base is what forces the specific ratio.

---

## The dramatic centerpiece: a forty-five-year mystery has an answer

This is the chapter where the dramatic centerpiece is the most intrinsically powerful of any in the anthology, because the Koide ratio is *famous* among physicists who care about this kind of question. Anyone who has thought seriously about lepton mass relationships has encountered Koide's formula. Anyone who has tried to derive it has felt the way it resists derivation. Many attempts have been published in respected journals; the empirical fit is too good to be coincidence, but the standard tools of particle physics (gauge symmetries, mass matrix structures, GUT embeddings) have not produced a clean derivation.

SM-3 produces one. The derivation is short — four steps, roughly half a page when written compactly — and exact. The result depends on three eigenvalue facts about K₃, on thermal equipartition (Layer B, conditional), and on an algebraic identity that is just trigonometry. There are no fitted parameters, no chosen forms of the mass matrix, no embeddings in larger groups.

The chapter's centerpiece is the moment when the four steps line up. The reader has been carried through the historical context (Koide 1981, the empirical 11-ppm match, four decades of attempted derivations), through the K₃ graph setup, through the eigenvalue calculation, and then arrives at the four-step proof. The proof itself does the work.

What makes this centerpiece different from SS-7's (the OPEN-SS-22 retirement) and SS-8's (the magnesium-26 octahedron) is its register. SS-7 and SS-8 had drama with stakes — methodology being tested, geometry being recognized. SM-3's drama is *resolution* — a question forty-five years old, dispensed with in four steps. The chapter's craft is to give the reader space to feel the forty-five years before it shows the four steps.

---

## The structural arc

**1. The hook (~400 words).** The chapter opens in 1981, with Yoshio Koide.

Koide was a Japanese theoretical physicist working on particle mass relations. The lepton sector was a puzzle to him: three charged leptons (electron, muon, tau), three masses spanning five orders of magnitude, no obvious pattern. The ratios are odd numbers — $m_\mu/m_e \approx 207$, $m_\tau/m_\mu \approx 17$ — and combinations of these don't give clean fractions. There seemed to be no structure to find.

Koide tried various combinations. Most went nowhere. Then he tried this one: take the three masses, add them, divide by the square of the sum of their square roots. The result was $0.6666\ldots$ — *exactly* 2/3 to within experimental error. He published it.

The paper got attention, then less attention as the years passed. The relation was clearly real — better experimental measurements of the tau mass, in the decades since 1981, have only made the agreement *tighter* (it now holds to 11 parts per million). But no one could explain it. Standard Model phenomenology had no place for this kind of relation; it would require a structural input that the Standard Model does not provide. Many derivations were attempted and most produced approximations rather than the exact 2/3. Some published derivations made the right numerical prediction but at the cost of ad-hoc assumptions that other physicists found unconvincing.

The hook's question: where does $2/3$ come from?

**2. The prior-work landscape (~700 words).** This section is critical because the chapter's case rests on the reader understanding how *unusual* it is for a clean derivation of the Koide ratio to be possible. The chapter should give the reader a sense of the landscape:

- Most attempted derivations rely on flavor-symmetric mass matrices or on specific texture assumptions in the lepton mass matrix. These produce $K = 2/3$ only under specific algebraic constraints that are themselves unmotivated — the symmetry or texture is chosen because it gives the right answer, not because it follows from a deeper principle.

- Some derivations work in the framework of grand unified theories (GUTs), where the lepton mass matrix is constrained by embedding in a larger group structure (SU(5), SO(10), E₆). These derivations are often able to produce *ratios* in the Koide form, but rarely the specific $2/3$ value, and almost never with zero fitted parameters.

- Other approaches use renormalization group arguments — computing how the Koide ratio runs from a high-energy unification scale down to the experimental measurement scale. These give relations between the ratio at different scales but do not predict its value at any specific scale from first principles.

- Koide himself proposed multiple frameworks over the years, none of them generally accepted. His own attempts to derive the formula from yukawon models, from texture flavor-symmetric mass matrices, and from spectator-fermion arrangements all required additional inputs that other physicists found unconvincing.

The chapter should acknowledge that the Koide ratio is in a small class of *empirical results that resist derivation*. The ratio is well-known to anyone who has thought about lepton mass relationships. The forty-five-year history of attempted derivations is itself part of the story; the reader needs to understand why a clean derivation would be remarkable.

The chapter should *not* dismiss the prior attempts as wrong. They were good-faith efforts at a genuinely hard problem. CPP's contribution is not that its derivation is uniquely correct; it is that its derivation produces $2/3$ exactly with zero fitted parameters and a four-step proof, which is structurally cleaner than any prior attempt has achieved.

**3. The setup (~500 words).** What CPP starts with: the K₃ graph (the complete graph on three vertices, three edges between three vertices), and a specific picture of what it represents. The K₃ graph is the base triangle of the lepton's tetrahedral cage — the same cage that the SS-3 chapter introduced. Three colored vertices form the K₃ base; the fourth vertex is the singlet apex that completes the tetrahedron.

The lepton's ZBW orbital — its zitterbewegung internal motion — hops among the three base vertices. The hopping is geometrically symmetric (C3 rotation symmetry) so all three hopping amplitudes are equal. The ZBW Hamiltonian is therefore the K₃ adjacency matrix scaled by a hopping energy:

$$\hat{H}_\text{ZBW} = \hbar\omega_0 \cdot A_{K_3}$$

where $A_{K_3}$ is the K₃ adjacency matrix (a 3×3 matrix with ones off-diagonal and zeros on-diagonal). The hopping energy $\hbar\omega_0 \approx 220$ MeV follows from the framework's confinement-radius and SSV-strength parameters, both established in earlier papers (no new fitting).

The K₃ adjacency matrix has eigenvalues. There are exactly two distinct values: $\lambda_\text{bonding} = +2$ (with eigenvector $(1, 1, 1)/\sqrt{3}$, occurring once) and $\lambda_\text{antibonding} = -1$ (with multiplicity 2, any vector perpendicular to the bonding eigenvector). The eigenvalue ratio is $\lambda_\text{bonding}/|\lambda_\text{antibonding}| = 2:1$. This 2:1 ratio is a theorem of linear algebra applied to the equilateral triangle graph; it is not a free parameter.

The reader should pause here. This 2:1 ratio is what the rest of the chapter will hinge on.

**4. The path through the work (~1,300 words).** The longest section, but it has a specific shape: walk through the four-step proof.

Begin by setting up the lepton mass parametrization. The Koide formula uses the parametrization

$$\sqrt{m_i} = A(1 + \rho \cos \phi_i)$$

where $i = 1, 2, 3$ labels the three lepton generations, $A$ is a normalization, $\rho$ is the modulation depth, and the phases $\phi_i$ are constrained by C3 symmetry to be $\phi_i = \theta + 2\pi i / 3$ for some overall phase $\theta$. This parametrization is general; any three masses can be written this way for some choice of $A$, $\rho$, $\theta$. The Koide ratio in this parametrization works out to

$$K = \frac{1 + \rho^2/2}{3}.$$

This is a pure algebraic identity given the parametrization; no physical input yet. The reader should see this as: *if* we knew $\rho$, *then* we would know $K$. The question is what determines $\rho$.

Now the four-step proof. The chapter should pace this carefully — these are the moments when the result lands.

*Step 1.* The lepton's mass contribution from each color vertex is proportional to $|\psi_i|^2$, the squared wavefunction amplitude at vertex $i$. This follows from the CPP picture of mass as organisational energy: the rate at which the ZBW orbital "visits" each vertex determines how much mass-equivalent organisational structure is stored there.

*Step 2.* The wavefunction is a superposition of K₃ eigenstates: bonding ($|\phi_+\rangle$ with eigenvalue $+2$) and antibonding ($|\phi_-^{(g)}\rangle$ with eigenvalue $-1$, with one state per generation $g$). The weights are $|c_+|^2$ for the bonding component and $|c_-|^2$ for the antibonding components.

*Step 3.* Thermal equipartition (the conditional Layer B input). The ZBW orbital is coupled to the Dipole Sea thermal bath at the Planck temperature, which is enormously larger than the ZBW energy scale ($kT_P / \hbar\omega_0 \sim 10^{20}$). At this temperature ratio, all three K₃ eigenstates are equally populated (state-counting equipartition; not energy-weighted, because all states are effectively at zero in units of $kT$). One bonding eigenstate and two antibonding eigenstates means $|c_+|^2 = 1/3$ and $|c_-|^2 = 2/3$.

*Step 4.* The amplitude ratio determines the modulation depth: $\rho^2 = |c_-|^2 / |c_+|^2 = (2/3)/(1/3) = 2$, so $\rho = \sqrt{2}$. Substituting into the algebraic identity from earlier:

$$K = \frac{1 + 2/2}{3} = \frac{2}{3}.$$

Exactly.

The chapter should stop here for a moment. Forty-five years of attempted derivations, hundreds of papers, and the answer comes out to exactly $2/3$ from the eigenvalue structure of the simplest non-trivial complete graph and a thermal equipartition argument. The reader should be allowed to feel this.

This is also where the conditional-theorem discipline appears. The thermalisation assumption is Layer B — imported from standard open-system formalism rather than derived from CPP primitives. The chapter should be honest about this. The thermal-equipartition step is what makes the proof go through; without it, the K₃ eigenstates would have unequal populations and the modulation depth $\rho$ would be different. CPP imports the thermalisation assumption from standard physics; the rest of the proof is unconditional given the thermalisation. Closing the conditional dependency — deriving thermalisation from CPP's DI-bit exchange mechanism rather than importing it — is registered as a future-work target (the SS-4 paper).

The chapter can mention the robustness check explicitly: at finite temperature, the exact departure from equal occupation gives a correction to $K = 2/3$ that is of order $10^{-20}$. This is twenty orders of magnitude below experimental precision (which sits at $10^{-5}$). The Layer B conditionality is therefore not a numerical concern; it is a methodological one.

This is also a natural place for AI-collaborator work to appear. SM-3 has a substantial review history — the paper went through multiple versions (v1 through v6) with reviewer engagement at each step. The chapter should consult `series_standard_model/papers/development-SM-3.md` and `reviews-SM-3.md` for review texture and name reviewers where their contributions appear. The four-step proof structure may itself have emerged through review iteration; if so, the reviewers who shaped it deserve to be named.

**5. The recognition moment / central result (~600 words).** The recognition moment in this chapter is the four-step proof itself, presented in the previous section. The recognition section can be shorter than usual because the proof did most of the work.

What this section should do: step back and put the result in context. The Koide ratio has been a forty-five-year empirical curiosity. Hundreds of papers have attempted derivations. SM-3's derivation is conditional (Layer B) but otherwise exact and short. The conditional dependency is well-isolated and methodologically tractable. The result sits in the rare class of empirical-relation derivations where the proof is shorter than the empirical-precision history that motivated it.

The chapter should also note the $N$-dependence result. CPP's derivation gives $K = (N+1)/(2N)$ for the complete graph $K_N$. Only $N=3$ gives $K = 2/3$. The reason the Koide ratio is $2/3$ and not some other fraction is that the lepton cage base has *three* colored vertices. The same three-vertex structure that gives the strong interaction its three-color SU(3) symmetry (the SS-3 chapter) gives the lepton sector its specific Koide value. The K₃ graph carries multiple physical results — charge quantization (SM-1), color algebra (SS-3), Koide ratio (SM-3), nuclear binding cascade (SS-5/SS-7/SS-8) — and SM-3 is one of the cleanest of them.

**6. The consequence checks (~400 words).** Three things worth mentioning:

- *The 11-ppm precision agreement.* The empirical Koide ratio agrees with $2/3$ to 11 parts per million; SM-3's prediction is $2/3$ exactly with corrections of order $10^{-20}$ from finite-temperature departures. The headroom between the prediction's precision and the experimental precision is twenty orders of magnitude. There is no reasonable scenario in which experimental precision will tighten enough to falsify the prediction; the prediction is effectively an analytic identity.

- *The structural impossibility of the Koide phase $\theta$.* The C3 phase $\theta$ in the parametrization $\phi_i = \theta + 2\pi i / 3$ is not determined by SM-3's machinery. SM-3 acknowledges this explicitly: the K₃ + SSV (sea-strength variation) structure cannot determine $\theta$, because the structure is C3-symmetric and provides no preferred phase reference. Determining $\theta$ requires additional physics (this is part of the SM-4 paper's content). The chapter should be honest that SM-3 derives the *modulation depth* $\rho$ but not the *phase* $\theta$, and that both pieces are required to predict individual lepton masses. SM-3 gives the relationship $K = 2/3$, not the masses themselves.

- *The cascade of K₃ results across the programme.* SM-1 used K₃'s C3 symmetry to derive charge quantization $\delta = 1/3$. SS-3 used K₃'s adjacency operator structure to derive SU(3). SM-3 uses K₃'s adjacency *eigenvalue* structure to derive the Koide ratio. Three independent results from three independent properties of the same triangle graph. The chapter can mention this as a structural pattern: K₃ is a small object, but it carries multiple physical results each of which uses a different mathematical aspect of the same graph.

**7. The closing reflection (~400 words).** The closing should land what SM-3 means.

The Koide ratio was a forty-five-year empirical curiosity, well-known to anyone who has thought about lepton mass relations. Its exact value $2/3$ resisted derivation through dozens of attempts. The reason it resisted derivation, in retrospect, is that the standard tools of particle physics — gauge symmetries, mass matrices, GUT embeddings — do not naturally produce eigenvalue ratios of $2:1$ from three-fold symmetric structures unless they are imposed by hand. CPP produces the $2:1$ ratio without imposing it; it falls out of the K₃ adjacency matrix because the equilateral triangle has that eigenvalue structure as a theorem of linear algebra.

The closing image: in physics, certain numerical coincidences turn out to be coincidences (the Hubble tension, perhaps), and certain ones turn out to be the visible part of structural realities not yet articulated. The Koide ratio has been in the second category for decades, with the structural reality elusive. SM-3's derivation suggests that the structure is the K₃ graph itself — the simplest non-trivial complete graph, three vertices and three edges, with eigenvalues $+2$ and $-1$ that combine through a thermal equipartition argument to give exactly $2/3$. The structure was always there; the work was finding it.

A possible closing sentence in the Rovelli register: *"The number was waiting to be derived for forty-five years, in the eigenvalues of the simplest triangle graph, in the place no one looked. It is now derived. The reader who has followed this chapter has seen the K₃ graph carry three independent physical results — charge quantization, the color algebra, and the Koide ratio — each from a different mathematical property of the same three-vertex object. K₃ is doing more work than its size suggests."*

---

## Calibration concerns specific to this chapter

**Concern 1: The Layer B conditional dependency must be foregrounded.** The thermalisation assumption (importing standard open-system formalism rather than deriving from CPP primitives) is the conditional dependency that makes the proof work. The chapter should make this visible at the point of the third step in the proof, not bury it. The honest framing is: the derivation is exact given Layer B; Layer B is conditional. The conditional structure should be explicit in the recognition section.

**Concern 2: The chapter should not oversell against prior attempts.** Many published derivations of the Koide ratio exist; some are by serious physicists. The chapter should acknowledge that prior attempts were good-faith efforts at a genuinely hard problem. CPP's contribution is structural cleanness (zero fitted parameters, four-step proof, unconditional given Layer B), not novelty. The reader should come away with the impression that CPP found the right place to look, not that prior physicists were lazy or wrong.

**Concern 3: The chapter has a chronology challenge similar to SS-5's.** Koide's 1981 discovery is forty-five years old; CPP's derivation is from 2026. The chapter is explaining a result that has been famous in particle physics circles for decades, derived in CPP after a particular structural recognition was made. The chapter should be careful to write the historical context with appropriate weight — Koide is a real historical figure, the empirical history of the ratio is a real piece of physics, and CPP's role is as the framework that finally produced a clean derivation, not as the framework that discovered the ratio.

**Concern 4: The phase $\theta$ honesty matters.** SM-3 derives the Koide *ratio*, which constrains the three lepton masses but does not predict them individually. The phase $\theta$ in the C3 parametrization remains undetermined by SM-3 alone (SM-4 picks this up). The chapter should acknowledge this explicitly so the reader does not infer that SM-3 predicts the lepton masses themselves. The constraint $K = 2/3$ is a mass *relation*, not a mass prediction.

---

## What the future Opus should read before drafting

**Required:**
- This arc file
- `templates/anthology_chapter_template.md`
- `series_standard_model/papers/mechanism-SM-3.md` (the substantive content; rich and well-organized)
- `series_standard_model/papers/philosophy-SM-3.md`
- `series_standard_model/papers/reviews-SM-3.md`
- The two existing anthology chapters for register calibration

**Recommended:**
- `series_standard_model/papers/development-SM-3.md` (development texture)
- `series_standard_model/papers/phenomena-SM-3.md`
- The historical context for Koide's 1981 discovery (Wikipedia entry on the Koide formula is reasonable; the original Koide paper is referenced in the .tex bibliography if a more authoritative source is needed)
- The SS-3 chapter, since the SS-3 chapter introduces the K₃ structure that this chapter uses for a different purpose — the two chapters can cross-reference cleanly
- `series_standard_model/papers/SM-3_k3_spectral_theorem_koide_formula.tex` (the actual paper) for specific technical claims if needed

---

## Suggested chapter title alternatives

- *Two-Thirds* — proposed title; references the Koide ratio's specific value, distinctive without being technical
- *The Koide Ratio* — most descriptive; least distinctive
- *What Koide Found* — historical-narrative framing
- *Eleven Parts Per Million* — references the empirical precision; striking but slightly cryptic
- *The Same Triangle* — references the K₃ recurrence across multiple results

The proposed title fits the chapter's specific destination — the value $2/3$ — and is short enough to be memorable. It's also pleasingly ambiguous: a reader who doesn't know the Koide ratio will not know what $2/3$ refers to until they read the chapter, which is the right kind of hook.
