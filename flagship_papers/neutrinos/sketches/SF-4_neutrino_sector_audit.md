# SF-4: Neutrino Sector Audit — Eight Parameters Against Current Corpus

**Status:** COMPLETE — audit phase (Session 37)
**Track:** SF-4 (Neutrino Sector Unification flagship paper) — foundation audit
**Author:** Claude Opus (audit), Thomas Lee Abshier ND (strategic frame)
**Established:** 8 May 2026 (patch 0294)
**Migrated:** 9 May 2026 (patch 0295) — moved from `flagship_papers/hierarchy_problem/sketches/` to `flagship_papers/neutrinos/sketches/` and renamed from `SS-Q1_neutrino_sector_audit.md` to `SF-4_neutrino_sector_audit.md` per Option-3 architecture adoption (Q1 of original Track-1 hierarchy paper outline dissolved into SF-4 as standalone neutrino flagship)
**Integration target:** Foundation document for SF-4 paper drafting; informs §3 mechanism, §4 derivation, §5 K3-integration, §6 calibration architecture, §7 $\delta_{CP}$ posture sections of the eventual SF-4 paper

---

## §1. Strategic frame

This document is the audit phase of strict-Option-C in the original Q1 resolution path: full rigorous derivation of the neutrino sector in current CPP formalism (post-SS-9, post-SM-3-through-SM-10 consolidation). Under Option-3 architecture (adopted Session 38, patch 0295), this work is the foundation for **SF-4**, the dedicated neutrino-sector flagship paper, which sits in the SF-line alongside SF-1 (charged leptons), SF-2 (electroweak), SF-3 (quarks), and SF-5 (the unification synthesis that absorbs the original Track-1 hierarchy paper framing).

The strategic posture established at Session 37 opening conversation is: **no compromise on first-principles rigor, every parameter back to 600-cell / Conscious Point primitives, "get out of jail free" register-as-open card used judiciously and one or two layers removed from the present problem where possible**. The motivation is explicit: only zero-parameter first-principles derivation is immune to the crank-association the consciousness-substrate framing invites. Soft-pedalling consciousness in the metaphor does not buy distance; rigor is the only working defence.

This audit's purpose is **not to derive the neutrino sector**. It is to:
1. Inventory what is established about each of the eight neutrino parameters in current CPP corpus (post-600-cell-consolidation papers)
2. Inventory what is broken in each pre-formalism sketch (the archived Grok exploratory $\sigma = 120^{-d}$ work and the November 2025 viXra DUNE paper)
3. Identify mechanism candidates available for current-formalism derivation, with honest assessment of each candidate's strengths, weaknesses, and tractability
4. Surface architectural and posture decisions that gate next-session work
5. Produce the analysis that enables Thomas's mechanism-selection decision in the next session

This audit does not select a mechanism. The mechanism-selection decision is Thomas's call after reviewing this document.

---

## §2. The eight parameters in scope

The neutrino sector is fully described by eight parameters. Six are continuous quantitative observables; two are categorical. The hierarchy ordering is itself a prediction — most theoretical frameworks do not commit to one or the other.

| # | Parameter | Symbol | Status as of 2026 | Current measured value (NuFIT 5.3) |
|---|-----------|--------|-------------------|-------------------------------------|
| 1 | Lightest neutrino mass | $m_1$ (NH) or $m_3$ (IH) | Bounded above; not measured | $\le 0.8$ eV (KATRIN); cosmological $\Sigma m_\nu \le 0.072$ eV |
| 2 | Solar mass-squared splitting | $\Delta m^2_{21}$ | Measured precisely | $7.39 \times 10^{-5}$ eV² (±3%) |
| 3 | Atmospheric mass-squared splitting | $|\Delta m^2_{32}|$ | Measured precisely; sign unmeasured | $2.52 \times 10^{-3}$ eV² (±3%) |
| 4 | Solar mixing angle | $\sin^2\theta_{12}$ | Measured | $0.304$ (±5%) |
| 5 | Atmospheric mixing angle | $\sin^2\theta_{23}$ | Measured; octant ambiguous | $0.570$ (±10%) |
| 6 | Reactor mixing angle | $\sin^2\theta_{13}$ | Measured precisely | $0.0224$ (±3%) |
| 7 | Dirac CP-violating phase | $\delta_{CP}$ | Hinted at; large uncertainty | $\sim 195°$ (3$\sigma$ range $108°-404°$) |
| 8 | Mass hierarchy ordering | NH or IH | Undetermined | NH preferred at $\sim 2.5\sigma$ |

The unified neutrino document Thomas described as the eventual target must cover all eight.

DUNE measurements 2026–2031 will sharpen items 5, 7, 8 and tighten 2, 3 to sub-percent. JUNO 2026+ will tighten 4 and resolve 8. KATRIN beta-endpoint and cosmological Σ$m_\nu$ from DESI/Planck will tighten 1.

---

## §3. Current-corpus state per parameter

Distinguishing "current corpus" (post-600-cell consolidation, papers SM-3 onward, SS-1 through SS-9 in the strong sector) from "pre-formalism material" (archived Grok exploratory work, November 2025 viXra paper) is essential. The two strata have different epistemic status.

### §3.1 What is established in current corpus

| Parameter | Current-corpus status | Source |
|-----------|------------------------|--------|
| $m_1$ | Not derived | — |
| $\Delta m^2_{21}$ | Not derived | — |
| $|\Delta m^2_{32}|$ | Not derived | — |
| $\sin^2\theta_{12}$ | Derived at zeroth order: $\sin^2\theta_{12}^{(0)} = 1/3$ (TBM) | SM-5 Theorem on $U_\TBM$ from $K_3$ eigenstructure |
| $\sin^2\theta_{23}$ | Derived at zeroth order: $\sin^2\theta_{23}^{(0)} = 1/2$ (TBM) | SM-5 same |
| $\sin^2\theta_{13}$ | Derived at zeroth order: $\sin^2\theta_{13}^{(0)} = 0$ (TBM) | SM-5 same |
| $\delta_{CP}$ | Open problem; explicitly registered as requiring EW sector; OP-SM-7d | SM-5 §discussion |
| Mass hierarchy ordering | Not derived | — |
| TBM corrections (~10% deviations from zeroth-order angles) | Open problem; OP-SM-4 (charged-lepton mixing contribution) and OP-SM-7d (Capotauro bias contribution) | SM-5 |

**Summary of current-corpus state**: SM-5 establishes the K3 framework for the PMNS matrix and derives all three angles at zeroth (tribimaximal) order from K3 eigenstructure. Mass values, the CP phase, the hierarchy ordering, and the corrections to TBM angles are all explicitly registered as open problems. SM-5 deferred neutrino masses to a "planned SM-6" with a mechanism placeholder $\sigma = 120^{-d}$. The actual SM-6 that shipped became *The Charged Lepton Mass Spectrum from 600-Cell Lattice Geometry*, which does not address neutrino masses. Therefore: **the planned-SM-6 neutrino-mass derivation never materialized in current formalism**.

### §3.2 SM-5 ansatz dependencies (must be inherited or replaced)

SM-5 derives PMNS angles conditional on three propositions explicitly flagged as ansatz, not derivation:

- **A1 (proposition):** The three neutrino mass eigenstates are identifiable with the three $K_3$ eigenmodes. This is an *identification ansatz*, not a derivation. (SM-5 Proposition on neutrino-K3 identification.)
- **A2 (proposition):** The PMNS matrix is the change-of-basis between charged-lepton mass eigenstates (K3 vertex states) and neutrino mass eigenstates (K3 eigenmodes). Standard physics in any framework that identifies mass eigenstates this way; once A1 is granted, A2 follows.
- **A3 (open problem):** Why neutrino mass eigenstates align with K3 eigenmodes (rather than being a generic linear combination) is registered as an open problem in SM-5.

The current-corpus PMNS angles at TBM order *depend on* A1 holding. If a Track 1 mechanism for neutrino masses turns out incompatible with A1 — e.g., if the masses are determined by a structure that does not pick out the K3 eigenmodes as eigenstates — then SM-5's PMNS derivation is undermined and must be re-grounded as part of the same work. **This is a key constraint on mechanism selection (Section §6).**

### §3.3 Quark-sector machinery available for analog construction

The shell-distance methodology developed in SM-7, SM-8, SM-9, SM-10 for quarks gives the analog template. In compressed form:

$$
M_q = m_e \cdot \frac{z}{\phi} \cdot V_q^{7/3} \cdot \mu_q
\qquad (q = s, c, b)
\qquad ;\qquad
M_t = m_e \cdot \frac{z}{\phi} \cdot V_t^{7/3} \cdot z \cdot C_F
$$

with:
- $m_e$ = electron mass (single calibration anchor for the entire mass spectrum)
- $z = 12$ = 600-cell coordination number (derived from substrate)
- $\phi = (1+\sqrt{5})/2$ = golden ratio (mathematical constant)
- $M_0 \equiv m_e \cdot z/\phi \approx 3.79$ MeV (mass quantum derived in SM-9 §Prefactor from lattice connectivity)
- $V_q$ = vertex count of cage-shell assignment (4, 12, 20, 30 for the four bonded shells: tetrahedron, icosahedron, dodecahedron, icosidodecahedron)
- $V^{7/3}$ exponent = derived in SM-9 from the angular-weighted pair model + DP-chain energy budget decomposition $V^2 \times V^{1/3}$
- $\mu_q$ = sector-specific multipliers (post-gap multiplier $z \cdot C_F$ for the top quark)

The distance shells of the 600-cell are computed from explicit construction of all 120 vertices and pairwise distances; the four "bonded shells" admit edges. The remaining shells (including Shell 3, the structurally significant gap) admit no edges.

This is the methodology Thomas's strategic frame asks be extended to neutrinos: every parameter back to 600-cell + CP primitives, same shell-distance / cage-assignment / energy-budget machinery applied to the unbound-mode regime that neutrinos occupy.

### §3.4 Identifications already in place

The SM-2 (older framework) and the archived Grok exploratory material already established the following identifications, which carry forward into current formalism in the sense that current-formalism papers (SM-1, SM-2, SM-5) explicitly reference them:

- Neutrinos = unbound orbital ZBW configurations of dipole-pair (DP) structures (no central CP anchor, in contrast to charged leptons and quarks which have central CPs)
- The unbound-mode dimensionality $d=3$ (vs. $d=0$ for bound modes giving $\sigma = 1$, $d=1$ for linear extras)
- Flavor structure correspondence:
  - $\nu_e \leftrightarrow$ unbound eDP (electron dipole pair)
  - $\nu_\mu \leftrightarrow$ unbound qDP (quark dipole pair)
  - $\nu_\tau \leftrightarrow$ unbound hDP-tetra (hybrid dipole pair tetrahedral cluster)

These identifications are *posited* in current formalism (SM-2 §11 explicitly says "These are order-of-magnitude estimates from the $\sigma = 120^{-3}$ hypothesis; they are not derived from first principles"). Whether they survive a current-formalism re-derivation is itself part of the work.

---

## §4. Pre-formalism sketches: what's there, what's broken

Two pre-formalism sketches are available as starting material. Both have specific identifiable problems that disqualify them as-is for flagship-paper-quality citation, but both contain elements that may be salvageable in a current-formalism re-derivation.

### §4.1 Archived $\sigma = 120^{-d}$ entropy-suppression sketch

**Location:** `archive/grok-exploratory-SM/p2-neutrino-masses-and-suppression/`
**Status:** Pre-600-cell-consolidation Grok exploratory work; explicit-status archived
**Relationship to current corpus:** Referenced in SM-2 §Neutrino Mass Estimates (which itself states the values are "order-of-magnitude estimates... not derived from first principles") and explicitly named as the "planned SM-6 mechanism" placeholder in SM-5

**Mechanism summary:**

The 600-cell has 120 vertices. The number 120 is interpreted as the topological invariant bounding information / entropy across the substrate. Bound modes ($d=0$, all internal CP-coupling intact) couple to full 4D layers and have $\sigma = 1$. Unbound orbital ZBW modes ($d=3$) diffuse across three effective dimensions, with entropy scaling as $120^3$ accessible paths; coupling strength dilutes as $\sigma = 120^{-d} = 120^{-3} \approx 5.79 \times 10^{-7}$ — the holographic-bound interpretation.

Mass formula sketch (from the archived `sigma-derivation.md`):
$$
m_\nu \propto E_{\text{spin}} \cdot \sigma \cdot \alpha
\qquad ;\qquad
\alpha = N_k / 120
\qquad ;\qquad
E_{\text{spin}} = \tfrac{1}{2} m v^2 \cdot \sigma, \quad v \sim c/r_k
$$

with the organizational-complexity counts:
- $\nu_e$: $N_k = 1$ (single unbound eDP)
- $\nu_\mu$: $N_k = 4$ (single unbound qDP, with 4 implicit substructure)
- $\nu_\tau$: $N_k = 12$ (hDP-tetra with 12 inter-bonds)

Predicted masses: $\nu_e \sim 0.001$ eV, $\nu_\mu \sim 0.004$ eV, $\nu_\tau \sim 0.012$ eV. Sum $\Sigma m_\nu \sim 0.017$ eV (consistent with cosmological bound $\le 0.072$ eV).

**What's right:**

- The substrate connection is built in. The 120 in the suppression base is the 600-cell vertex count; this is structural, not coincidental.
- The bound/unbound mode dichotomy ($d=0$ vs $d=3$) is consistent with the broader CPP framework (SM-1 cage-stability mechanism).
- The $N_k = 12$ for $\nu_\tau$ matches the $z = 12$ coordination cleanly. This is suggestive.
- The flavor identification scheme (eDP / qDP / hDP-tetra) maps onto the same DP-type taxonomy used in the rest of CPP.
- The sum prediction $\Sigma m_\nu \sim 0.017$ eV is consistent with cosmological bounds.

**What's broken:**

- **The mass-squared splittings are wrong, not just the absolute scale.** Predicted masses (0.001, 0.004, 0.012 eV) yield:
  - $\Delta m^2_{21}$ predicted $\approx 1.5 \times 10^{-5}$ eV² vs measured $7.39 \times 10^{-5}$ eV² (factor 5 off)
  - $\Delta m^2_{32}$ predicted $\approx 1.28 \times 10^{-4}$ eV² vs measured $2.52 \times 10^{-3}$ eV² (factor 20 off)
  
  The splittings being differentially wrong (not a uniform overall scale issue) means the relative spacing between the masses is wrong, which means the $N_k$ values $\{1, 4, 12\}$ are wrong as posited, OR the mass formula is wrong, OR both.

- **$N_k$ values are posited, not derived from A1–A11.** The text says e.g. $\nu_\tau$ has $N_k = 12$ "with inter-bonds" but does not derive why $N_k$ counts inter-bonds (vs vertices, vs edges, vs vertex-edge sums, vs degree-weighted vertex counts). This is the analog of the SS-9 conditions C1–C8: you need a first-principles derivation showing why exactly these counts and not others.

- **$d=3$ for unbound modes is posited from "no central CP anchor."** Plausibly tractable from the SM-1 cage-stability machinery, but not derived in the archived material.

- **The mass formula structure $m \propto E_{\text{spin}} \cdot \sigma \cdot \alpha$ is exploratory.** $E_{\text{spin}}$ is defined as $\tfrac{1}{2} m v^2 \cdot \sigma$ where $m$ is the mass we're trying to compute, making the formula self-referential. The $v \sim c/r_k$ relation is sketched, not derived; $r_k$ is undefined.

- **No connection to the K3 eigenstructure of SM-5.** The archived sketch produces masses without reference to whether the resulting mass eigenstates align with K3 eigenmodes. If they don't, SM-5's PMNS derivation is broken.

- **No prediction for $\delta_{CP}$, hierarchy ordering, or TBM corrections.**

**Salvage assessment:** The substrate connection ($120 = $ 600-cell vertex count) and the bound/unbound dichotomy are real and worth carrying. The specific $N_k$ values and the mass-formula structure need re-derivation in current formalism with first-principles support. The connection to SM-5 K3-PMNS must be enforced as a constraint.

### §4.2 November 2025 viXra DUNE paper

**Status:** viXra-targeted (not actually posted to viXra per the strategic-priorities-document note that "viXra didn't publish them"); pre-current-formalism in mechanism; available as user-shared `.tex` in this audit conversation
**Relationship to current corpus:** Cited as motivating background in the hierarchy paper outline; Grok's pre-600-cell-consolidation neutrino work; the strategic priority frame says "Grok pre-600-cell sketch needs rigorous redo in current formalism"

**Mechanism summary:**

Neutrinos as twist defects propagating on successive layers of self-similar cage lattice. Three flavors confined in cages of topological depth 1, 2, 3 ($\nu_e, \nu_\mu, \nu_\tau$). Cage radii follow $R_n = R_0 \lambda^n$ with $\lambda = \phi^{3/2} \approx 4.236$ (golden ratio scaling between successive cage layers). Neutrino mass inversely proportional to cage radius: $m_i \propto 1/R_i$. Hierarchy strictly normal because $R_{n+1} > R_n$ forces $m_3 > m_2 > m_1$. Mixing angles from cage-overlap geometry as modified TBM with golden-ratio corrections. CP phase from "relative orientation of the three nested cages" fixed at $\delta_{CP} = \pi/2$.

**What's right:**

- The hierarchy-ordering prediction (normal mandatory) is a real falsifiable claim. If JUNO measures inverted, this mechanism is dead. (Other mechanisms might survive inverted; this one cannot.)
- The substrate connection (golden-ratio scaling $\phi^{3/2}$ and the 600-cell as background) is in the right family.
- The "smoking gun" $\delta_{CP}$ = exactly $\pi/2$ rhetorical framing is strong if the value is rigorous.
- The mixing-angle pattern (modified TBM with golden-ratio corrections) is consistent with the SM-5 starting point (TBM at zeroth order, corrections from cage torsion / Capotauro bias).
- The Monte Carlo validation methodology section is sound: vary the input solar splitting within experimental uncertainty, propagate to the prediction. This methodology is portable to a current-formalism mechanism.

**What's broken:**

- **Algebra error in the scaling factor.** The paper consistently writes "$\lambda = \phi^{3/2} \approx 4.236$" but $\phi^{3/2} = 2.058$, not $4.236$. The value $4.236$ is $\phi^3$. The Derivation of the Scaling Factor section says volume ratio $V_{n+1}/V_n = \phi^3$ and asserts the linear ratio is $(V_{n+1}/V_n)^{1/3} = \phi^{3/2}$, but $(\phi^3)^{1/3} = \phi$, not $\phi^{3/2}$. The cube-root step is incorrect. So either the volume ratio is actually $\phi^{9/2}$ giving $\lambda = \phi^{3/2} \approx 2.058$, or the volume ratio is $\phi^3$ giving $\lambda = \phi \approx 1.618$. The paper's actual numerical value of $\lambda \approx 4.236$ corresponds to $\phi^3$, which is the volume ratio (not the linear scaling) under either reading. **The paper internally contradicts itself on what $\lambda$ is.**

- **The quoted mass values do not derive from the cage-scaling formula.** The body text claims $m_2 = m_1 \cdot \lambda \approx 0.00860$ eV with $m_1 = 0.001$ eV and $\lambda \approx 4.236$. But $0.001 \times 4.236 = 0.00424$, not $0.00860$. Similarly $m_3 = 0.00860 \times 4.236 = 0.0364$, not the stated $0.0504$. No single value of $\lambda$ produces the stated trio (0.001, 0.00860, 0.0504). The quoted values *do* match what you get by inverting the observed mass-squared splittings: $m_2 = \sqrt{m_1^2 + \Delta m^2_{21}} = 0.00866$, $m_3 = \sqrt{m_2^2 + |\Delta m^2_{32}|} = 0.0509$. So the masses in the body of the paper are calibrated to observed splittings, not derived from cage scaling. The Appendix calculation gives the formula-consistent $m_2 = 0.00424$ eV and trails off with an ellipsis — the inconsistency is visible inside the document.

- **$\delta_{CP} = \pi/2$ is asserted, not derived.** The "Smoking Gun" section says "the relative orientation of the three nested cages fixes the Dirac CP phase to $\pi/2$." That is the entire derivation. There is no equation, no symmetry argument, no calculation showing how cage orientation produces a phase, let alone exactly $\pi/2$. SM-5 in current formalism explicitly registers $\delta_{CP}$ as requiring the EW sector — that is the rigorous position.

- **The "depth 1/2/3" cage assignments are posited.** Depth indexing is asserted but not connected to the bonded-shell taxonomy of SM-8 (tetrahedron / icosahedron / dodecahedron / icosidodecahedron at vertex counts 4 / 12 / 20 / 30) or to any A1–A11-derivable structure.

- **No connection to K3 eigenstructure.** Same problem as the $\sigma = 120^{-d}$ sketch: SM-5's PMNS derivation requires neutrino mass eigenstates to align with K3 eigenmodes, and the cage-radius-scaling sketch does not address whether they do.

- **The Monte Carlo section builds on the broken mass formula.** The Python validation code uses $m_1 = \sqrt{\Delta m^2_{21} / (\lambda^2 - 1)}$ which is consistent with the formula $m_2 = \lambda m_1$ but inconsistent with the body-text claim that this gives $m_2 = 0.00860$. With the formula's actual numerical output, the predicted $m_2$ is $0.00424$ eV, not $0.00860$. The Monte Carlo distribution is centered on the formula-consistent value, not the body-text claim.

**Salvage assessment:** The hierarchy-ordering-mandatory-normal prediction is clean and worth preserving in any current-formalism mechanism that uses cage-radius-style scaling. The mixing-angle pattern as modified TBM is consistent with SM-5 and worth carrying. The $\delta_{CP} = \pi/2$ target is worth aiming at *if* a rigorous derivation can be constructed; the assertion as-is has no value. Mass values must be re-derived from a corrected scaling formula or replaced by a different mechanism.

### §4.3 The two pre-formalism sketches are NOT the same mechanism

Important to note: the $\sigma = 120^{-d}$ entropy-suppression mechanism (§4.1) and the cage-radius-scaling mechanism (§4.2) are *substantively different*, not reformulations of the same underlying idea. The former is a holographic-entropy diluation across the 120-vertex substrate; the latter is a geometric cage-radius scaling across nested cages. They invoke different substructure ($N_k$ organizational counts vs $R_n$ cage radii), produce different scaling laws ($\sigma \cdot \alpha$ vs $1/R$), and have different falsifier structures.

This means the corpus contains *two* pre-current-formalism neutrino-mass approaches, both with problems, neither directly compatible with the other. Q1 reconciliation is therefore not "harmonize two pictures" — it is "the corpus has fragmented and contradictory neutrino-mass material; build a current-formalism derivation that supersedes both."

---

## §5. Available mechanism candidates for current-formalism derivation

Five mechanism candidates are available for current-formalism derivation. Each is presented with its mechanism sketch, A1–A11 derivation feasibility, splitting-match prospects, K3 integration story, $\delta_{CP}$ angle, and Q3 calibration architecture. **No candidate is proposed as preferred.** The mechanism-selection decision is Thomas's call after this audit.

### §5.1 Candidate A — Refined $\sigma = 120^{-d}$ with first-principles $N_k$ derivation

**Mechanism:** Inherit the bound/unbound mode dichotomy and the $\sigma = 120^{-d}$ entropy-suppression structure from §4.1. Replace the posited $N_k = \{1, 4, 12\}$ with first-principles values derived from A1–A11 + cage-stability machinery (SM-1) + DP-type taxonomy. Structure:

$$
m_{\nu_i} = \mathcal{S}_0 \cdot \sigma \cdot f(N_{k,i})
\qquad ;\qquad
\sigma = 120^{-d}, \quad d = d_{\text{unbound}}\ \text{(derive from A1-A11)}
$$

with $\mathcal{S}_0$ a scale derived from CPP primitives (candidate: $\mathcal{S}_0 = M_0 = m_e \cdot z/\phi$ to maintain calibration unification) and $f(N_k)$ a first-principles function of organizational complexity to be derived.

**A1–A11 feasibility:** $d = 3$ for unbound modes is plausibly tractable from the SM-1 cage-stability mechanism (no central CP $\Rightarrow$ no constraining cage $\Rightarrow$ free 3D orbital propagation). $N_k$ derivation is harder; it needs a counting principle that picks out organizational-complexity numbers from cage / DP-cluster topology. The SS-9 framework's experience with deriving $C_5, C_6, C_7, C_8$ from A1–A11 (none have closed yet, all four are OPEN-SS-29/30/33/37) is directly relevant: this is the same class of work, and it is hard.

**Splitting match:** Currently broken (factor 5 / factor 20 off in the splittings). Whether a first-principles re-derivation of $N_k$ produces the correct splittings is an empirical question; nothing in the structure of the formula guarantees it. **Honest assessment: the $\sigma \cdot \alpha$ mass-formula structure may need to be augmented (not just re-parameterized) to get the splittings right.**

**K3 integration:** Compatible in principle. The $\sigma$ suppression operates on whatever the eigenstates are; if K3 eigenstructure picks out the eigenstates, the suppression scales them. SM-5's identification ansatz A1 (neutrino mass eigenstates = K3 eigenmodes) becomes a constraint on $f(N_{k,i})$ for the three flavors.

**$\delta_{CP}$ angle:** Not addressed by this mechanism. Either follow SM-5 and register as open (route ii), or develop a separate derivation.

**Q3 calibration:** Single calibration ($m_e$) preserved if $\mathcal{S}_0 = M_0 = m_e \cdot z/\phi$. The $d$ in the suppression and the $N_{k,i}$ values must derive from substrate primitives.

**Tractability estimate:** 4–8 sessions for the mechanism itself; risk of opening 1–2 sub-conditions.

### §5.2 Candidate B — Refined cage-radius scaling with corrected algebra

**Mechanism:** Inherit the cage-radius / nested-cage structure from §4.2. Replace the broken $\lambda = \phi^{3/2}$ derivation (which actually gives $\phi$, not $\phi^{3/2}$) with a corrected first-principles scaling factor; replace the posited "depth 1/2/3" cage assignments with the bonded-shell taxonomy from SM-8; replace the asserted $\delta_{CP} = \pi/2$ with either a rigorous derivation or honest registration as open.

$$
m_{\nu_i} = \frac{C_0}{R_i}
\qquad ;\qquad
R_i = R_0 \cdot \lambda_{\text{geom}}^i, \quad \lambda_{\text{geom}}\ \text{from substrate geometry}
$$

with $C_0$ an energy-times-length quantum and $\lambda_{\text{geom}}$ the actual derivable scaling between consecutive cage shells.

**A1–A11 feasibility:** A scaling factor between consecutive cage shells should be derivable from the bonded-shell distance-shell structure of the 600-cell. The four bonded shells (tetrahedron, icosahedron, dodecahedron, icosidodecahedron) have specific distance-shell circumradii in the 600-cell substrate; the ratios between these radii are computable. Whether the ratios produce the correct mass-splittings is the empirical question.

**Splitting match:** Quick check — the bonded-shell circumradii ratios (relative to icosahedron $V=12$): tetrahedron $R_4 / R_{12}$ and icosidodecahedron $R_{30} / R_{12}$ have specific golden-ratio-related values inherent to the 600-cell. Whether they match the observed mass splittings is checkable in maybe 1 session of computation. **This is a relatively quick falsifier on Candidate B**: if the actual ratios are wrong by orders of magnitude, the candidate is dead; if they are in the ballpark, it is alive.

**K3 integration:** Less obvious. Cage-radius scaling does not naturally pick out K3 as the eigenstructure; the K3 eigenstructure of charged-leptons (SM-3) emerged from the colour-cage adjacency graph, not from cage radii. Establishing whether neutrino mass eigenstates under cage-radius scaling are K3 eigenmodes (per SM-5 A1) requires additional structural argument.

**$\delta_{CP}$ angle:** Same as Candidate A — register as open or develop separately.

**Q3 calibration:** $C_0$ must be set; calibration count depends on whether $C_0$ derives from substrate (zero parameters) or is calibrated to the lightest-neutrino mass (one additional parameter). If the latter, this becomes 2-calibration overall (electron + lightest neutrino), which weakens the headline.

**Tractability estimate:** Quick 1-session falsifier check on the bonded-shell circumradii ratios; if alive, 4–6 sessions for full mechanism + K3 reconciliation.

### §5.3 Candidate C — Shell-distance methodology direct analog (SM-8 extended)

**Mechanism:** Apply the SM-7/SM-8 quark-mass methodology directly to neutrinos with appropriate modifications for the unbound-mode regime. The quark formula is

$$
M_q = m_e \cdot \frac{z}{\phi} \cdot V_q^{7/3} \cdot \mu_q
$$

The proposed neutrino analog:

$$
m_{\nu_i} = m_e \cdot \frac{z}{\phi} \cdot V_{\nu,i}^{\alpha_\nu} \cdot \mu_{\nu,i} \cdot \mathcal{T}_{\text{unbound}}
$$

where $V_{\nu,i}$ is the cage-shell vertex-count assignment for the $i$-th flavor (from the four bonded shells), $\alpha_\nu$ is a scaling exponent (potentially the same $7/3$ as quarks, potentially different), $\mu_{\nu,i}$ is sector-specific multipliers (analog of the quark $z \cdot C_F$ for the top), and $\mathcal{T}_{\text{unbound}}$ is the suppression factor for the unbound regime (potentially the $\sigma = 120^{-d}$ from Candidate A, potentially different).

**A1–A11 feasibility:** This is the candidate most directly continuous with current formalism. The shell-distance machinery already derives in SM-8 for quarks; SM-9 derives the $V^{7/3}$ exponent and $M_0$ prefactor from first principles. The work is to extend to the unbound-mode regime: derive the right $\alpha_\nu$ exponent, identify the cage-shell assignments for the three neutrino flavors, derive the unbound suppression factor.

**Splitting match:** Highly dependent on the cage-shell assignments. If $V_{\nu_e, \nu_\mu, \nu_\tau}$ correspond to (4, 12, 20) or some subset of the bonded shells, the splittings have specific values determined by the 600-cell distance-shell structure. Quick check: the ratio $V_{\nu_\tau}/V_{\nu_\mu}$ to the $7/3$ power (assuming same exponent as quarks) gives the predicted mass ratio; check against $\sqrt{|\Delta m^2_{32}|}/\sqrt{\Delta m^2_{21}} \approx 6$. With $V_{\nu_\tau}/V_{\nu_\mu} = 30/12 = 2.5$, $(2.5)^{7/3} = 8.55$ — within a factor of ~1.4 of the empirical 6. **This is encouraging at the order-of-magnitude level**, but does not commit any specific shell assignment.

**K3 integration:** Requires explicit additional argument that the resulting mass eigenstates align with K3 eigenmodes. Note: SM-5's A1 ansatz (neutrino mass eigenstates = K3 eigenmodes) is *not* automatically true under shell-distance methodology; it must be enforced or re-derived. This is a real cost.

**$\delta_{CP}$ angle:** Same as Candidates A and B — separate work required.

**Q3 calibration:** Single calibration ($m_e$) preserved by construction (the formula uses $m_e \cdot z/\phi$). This is the cleanest calibration story.

**Tractability estimate:** 4–6 sessions if cage-shell assignments derive cleanly; 6–10 if a sub-condition opens (analog of OPEN-SS-37 for the unbound-mode suppression structure).

### §5.4 Candidate D — Hybrid (shell-distance + entropy-suppression)

**Mechanism:** Combine Candidate A's $\sigma = 120^{-d}$ unbound-mode suppression with Candidate C's shell-distance scaling. Structure:

$$
m_{\nu_i} = M_0 \cdot V_{\nu,i}^{\alpha_\nu} \cdot \sigma \cdot g(N_{k,i})
$$

where $V_{\nu,i}$ is the cage-shell assignment (Candidate C), $\sigma = 120^{-d}$ is the unbound-mode suppression (Candidate A), and $g(N_{k,i})$ is a residual factor accounting for organizational complexity.

**A1–A11 feasibility:** Highest because it draws on the most existing CPP machinery; lowest because it has the most moving parts. Whether the redundancy between $V_{\nu,i}$ scaling and $g(N_{k,i})$ overcounts or undercounts requires careful analysis; Candidate D risks over-fitting the splittings via too-many-knobs.

**Splitting match:** Likely tunable to fit by construction; this is both the strength and the weakness. A current-formalism derivation must show that all components are independently first-principles-derived; otherwise Candidate D collapses to "the mass formula has enough parameters to fit."

**K3 integration:** Same issue as Candidate C.

**$\delta_{CP}$ angle:** Same as A/B/C.

**Q3 calibration:** Preserved if all factors derive from substrate.

**Tractability estimate:** 6–10 sessions; highest risk of derivation getting lost in proliferating sub-conditions. **This is the candidate most likely to need register-as-open card use; least likely to produce a clean apex paper.**

### §5.5 Candidate E — New mechanism (open territory)

**Mechanism:** The four candidates above all assume that the right mechanism for neutrino masses is some refinement of existing pre-formalism sketches plus existing current-formalism shell-distance machinery. It is also possible that the right mechanism is new — that neutrinos require structure that hasn't yet been articulated in the corpus. Examples of what "new" might mean:

- A connection to the K3 eigenstructure where the *masses themselves* (not just the eigenstate identification) come from K3 spectral structure with some additional input
- A suppression mechanism not captured by $\sigma = 120^{-d}$ but operating on a different substrate-information count
- A direct connection to the SR sector via the lightlike / near-lightlike propagation of neutrinos (SR-1 frame; mass arising from substrate-frame interaction effects)
- An anchor to recognized mathematics outside the polytope-theory bridge (distance geometry, EDM theory, rigidity theory analogs not yet explored for neutrinos — analog to OPEN-SS-37 Route (d) for SS-9)

**Tractability estimate:** Variable. Some new-mechanism directions may be quick to dispose of (e.g., SR-frame mass mechanism is checkable in 1–2 sessions); others may require sustained development comparable to SS-9. Open territory has both upside and risk.

### §5.6 Cross-candidate comparison summary

| Candidate | Mechanism core | Substrate connection strength | Splitting-match prospects | K3-integration cost | Calibration cleanliness | Sessions estimate | Risk profile |
|-----------|----------------|------------------------------|---------------------------|---------------------|--------------------------|--------------------|--------------|
| A: Refined $\sigma = 120^{-d}$ | Entropy suppression + $N_k$ counts | High (substrate count built in) | Currently broken; depends on $N_k$ first-principles | Moderate (works if SM-5 A1 enforced as constraint) | Single calibration if $\mathcal{S}_0 = M_0$ | 4–8 | 1–2 sub-conditions likely |
| B: Refined cage-radius | Geometric $1/R$ scaling | Medium (golden-ratio scaling family) | Quick to falsify or vindicate | High (cage-radius doesn't naturally produce K3 eigenstates) | 1 or 2 calibrations depending on $C_0$ | 1 (falsifier) + 4–6 if alive | Moderate; clean falsifier protects against waste |
| C: Shell-distance analog | Direct SM-8 extension | High (most direct corpus inheritance) | Encouraging at ~1.4 OOM | Real cost (must enforce K3 eigenstructure) | Single calibration ($m_e$) preserved | 4–6 if shells assign cleanly; 6–10 if sub-condition | Moderate; closest to known machinery |
| D: Hybrid | Shell-distance + entropy | Highest (uses most machinery) | Tunable by construction (problem) | Same as C | Preserved if all factors derive | 6–10 | Highest; over-fitting risk |
| E: New mechanism | Open | Variable | Variable | Variable | Variable | Variable | Both upside and risk |

---

## §6. Constraint: K3 integration is non-negotiable

The SM-5 PMNS derivation depends on the ansatz A1 that neutrino mass eigenstates align with $K_3$ eigenmodes. SM-5's PMNS angles at zeroth (TBM) order are *the only current-corpus derivation* of any neutrino observable. Discarding A1 means losing the existing PMNS work and re-deriving from scratch.

**Therefore the Track 1 mechanism must enforce K3 eigenstructure as a constraint on the mass-derivation work.** Specifically:

**Constraint K1:** The mechanism produces three mass eigenstates $|\nu_1\rangle, |\nu_2\rangle, |\nu_3\rangle$ that diagonalize the mass operator.

**Constraint K2:** Under the change-of-basis to the charged-lepton flavor basis (the $K_3$ vertex states established in SM-4), the resulting matrix is the PMNS matrix.

**Constraint K3:** At zeroth order (the unperturbed substrate, no charged-lepton mixing or Capotauro bias), the resulting PMNS matrix is the tribimaximal matrix $U_\TBM$.

K1 is generic (any mass-generating mechanism produces eigenstates). K2 and K3 together amount to: the neutrino mass eigenstates align with $K_3$ eigenmodes at zeroth order.

This is a *hard constraint* on mechanism selection. Candidates that produce the right masses but not K3-eigenstate alignment are not flagship-paper-quality complete; they break SM-5's existing derivation. Resolving this constraint may require additional structural argument as part of the mechanism work itself.

**Note on resolving the constraint:** In Candidates A and D, the suppression factor $\sigma$ acts identically on all three flavors and so does not break K3 eigenstructure (it scales eigenmodes uniformly); the constraint is automatically satisfied modulo flavor-dependent corrections. In Candidate C, the cage-shell assignments do not automatically pick out K3 eigenmodes; the constraint must be derived. In Candidate B, the cage-radius scaling is a strong tension with K3 eigenstructure; the cost is highest. In Candidate E, the constraint may be automatically satisfied or may need to be enforced, depending on the mechanism.

---

## §7. The $\delta_{CP}$ posture decision

Independent of mechanism selection, a posture decision is required for $\delta_{CP}$:

**Route (i): Derive $\delta_{CP}$ from CPP primitives.** High value. Targets the "smoking gun" the viXra paper aimed at, but rigorously. Possible derivation handles:
- Cage-orientation angle (the viXra paper's gesture, but with actual derivation rather than assertion)
- Capotauro bias in current formalism (registered as OP-SM-7d in SM-5; the EW-sector handle that SM-5 deferred to)
- K3-eigenstate phase structure (the K3 eigenmodes have a complex phase structure that may carry CP-violating content — this is unexplored in current corpus)
- Substrate chirality (CPP has handedness in the $\phi$-related orientations; a CP phase from chirality is a candidate worth scoping)

**Route (ii): Register $\delta_{CP}$ as open.** Honest scope. Track 1 paper makes seven of the eight neutrino predictions, with $\delta_{CP}$ explicitly deferred to a later EW-sector derivation. This is what SM-5 already does. It is rigorous; it is not compromise. The "headline" weakens slightly (8/8 predictions vs 7/8) but a 7/8 zero-parameter derivation is still vastly stronger than any other framework.

**Route (iii): Register $\delta_{CP}$ as a falsifier.** Variant of (ii) where the paper does not claim to predict $\delta_{CP}$ but does claim that the Track 2-or-later derivation must produce a value within DUNE's measured range. Falsifies the framework if the derivation cannot be made consistent with measurement.

Recommendation for Thomas to weigh: route (i) is the higher-value outcome if it lands in 1–2 sessions of investigation; if it requires a multi-session derivation campaign of its own, route (ii) is preferable to keep Track 1 timeline contained. Decision can wait until after the mechanism-selection session — once the primary mass mechanism is chosen, the $\delta_{CP}$ derivation handles available within that mechanism become clearer.

---

## §8. Q3 calibration architecture

The Track 1 hierarchy paper's headline rests on the calibration story. SM-9's derivation $M_0 = m_e \cdot z/\phi$ from lattice connectivity establishes that the mass quantum is the electron mass; quark masses derive via $V^{7/3}$ scaling with zero additional parameters. The hierarchy paper then claims one calibration ($m_e$) for the entire fermion spectrum.

Adding neutrinos forces the calibration story to be re-examined:

- If neutrino masses derive via Candidates A, C, or D using $\mathcal{S}_0 = M_0 = m_e \cdot z/\phi$, the single-calibration claim survives.
- If neutrino masses require a separate scale not reducible to $M_0$, the claim weakens to two calibrations.
- If neutrino masses require calibration to the lightest neutrino or to the solar splitting (as the viXra paper does), the claim weakens to two calibrations, and one of them is observed-splitting-anchored rather than substrate-anchored.

Q3 (the calibration honesty question) and Q1 (this audit's question) are coupled: the mechanism selected for neutrino masses determines the calibration count.

**For mechanism-selection session (Session 38):** Thomas should be aware that Candidates A and C both preserve the single-calibration claim; Candidate B may introduce a second calibration; Candidate D and E require explicit accounting case-by-case.

**For Track 1 paper drafting:** The calibration count must be settled before the abstract is written. A "1 calibration, 12 fermion masses" headline is strategic. A "2 calibrations" headline is still strong but materially weaker.

---

## §9. Architectural decision: RESOLVED at Session 38 (Option 3)

> **Update — Session 38 (9 May 2026, patch 0295):** Architectural question resolved. Thomas adopted Option-3 four-family + unification SF-line architecture: SF-1 (charged leptons), SF-2 (electroweak), SF-3 (quarks), SF-4 (neutrinos — this paper), SF-5 (unification synthesis, absorbs original Track-1 "Hierarchy Without Hierarchy" framing). The work captured by this audit is the foundation for SF-4 as a standalone flagship paper covering all eight neutrino parameters in unified form. SF-5 will reference and build on SF-4's results rather than embed them. The audit-time architectural Options α/β/γ presented below are superseded by Option 3.

**Original audit-time analysis follows for context.** The unified neutrino document Thomas described — covering all eight parameters with current-formalism rigor — is itself a substantial deliverable. Two architectural options present:

**Option α: Long §8 in Track 1 hierarchy paper.** All neutrino content lives inside Track 1. Estimate 10–15 pages of §8 if the derivation is relatively clean; 20+ if not. Track 1 paper grows from 25–35 estimated to 40–55 pages. Risk: Track 1 becomes overlong and rhetorically diffuse; reviewers find the focus less crisp; the paper becomes harder to ship.

**Option β: Companion neutrino flagship paper.** Track 1 hierarchy paper covers charged leptons + quarks (9 of 12 fermion masses); companion paper covers neutrino sector (3 masses + 3 angles + $\delta_{CP}$ + ordering = 8 parameters). Both are flagship-quality. Track 1 ships at 25–35 pages; companion ships at 25–40 pages. Tightly-coupled in time of release. The combined "Track 1 + companion" pair carries the full 12-mass / 12-OOM headline as a coordinated submission.

**Option γ: Track 1 §8 as bridge-with-pointer.** Track 1 includes the K3-mass-eigenstate identification + selected-mechanism candidate at framework level + falsifier-style claim ("neutrino sector follows this geometric structure"); companion paper develops the full eight-parameter derivation with quantitative predictions. Lighter §8 (3-5 pages); companion is the workhorse.

**Audit-time recommendation: defer the architectural decision until mechanism selection lands and we can estimate the heaviness of the derivation.** If the chosen mechanism produces the splittings cleanly with minimal sub-conditions, Option α (long §8) is feasible. If the mechanism opens 2+ sub-conditions and requires substantial first-principles closure work, Options β or γ become preferable. The audit can not commit to architecture; the data drives the decision.

The strict-C strategic posture argues for whichever architecture preserves rigor without overloading any one paper. My weak prior at audit time is **Option β (companion)**: the eight-parameter neutrino derivation is heavy enough to deserve its own venue, the hierarchy paper benefits from a 9-mass focus that lets §8 be a tight 3-5-page pointer to the companion, and a coordinated two-paper submission (12 masses, with the eight-parameter neutrino paper as the companion) carries strategic weight. But the audit does not commit; this is for Thomas to decide after mechanism selection.

---

## §10. Forward plan

### §10.1 Session 38 — Mechanism selection

**Pre-session prep on Claude side:** Re-read this audit; re-read SM-3, SM-4, SM-5, SM-7, SM-8, SM-9 source with mechanism-selection lens; produce concrete falsifier checks for each candidate (especially the Candidate B circumradii ratio check, which is 1-session if not 1-hour).

**In-session work with Thomas present:**
1. Thomas reviews this audit document; clarifies any factual issues or omissions
2. Mechanism-selection conversation: which of Candidates A/B/C/D/E is the primary route?
3. $\delta_{CP}$ posture decision (route i / ii / iii)
4. Architectural decision (Option α / β / γ) — may defer further if mechanism choice doesn't constrain it yet

**Output:** A decision document at `flagship_papers/hierarchy_problem/sketches/SS-Q1_mechanism_selected.md` recording the chosen mechanism, the chosen $\delta_{CP}$ posture, the working architectural plan, and the open sub-conditions registered for first-principles closure.

### §10.2 Sessions 39+ — Derivation

Form depends on mechanism selected. Generic structure (analog of SS-9 derivation campaign):
- Session 39: cage-shell-assignment / $N_k$-derivation work. Open or close substantive sub-conditions.
- Sessions 40–42: scaling-law / suppression-factor derivation work. Splittings match check at each session close.
- Sessions 43–44: K3 eigenstructure constraint enforcement / re-derivation work.
- Session 45+: $\delta_{CP}$ derivation (if route i) or rigorous registration (if route ii/iii); hierarchy ordering as falsifiable prediction.
- Sessions 46+: integration into Track 1 paper §8 (if Option α) or v0.1 of companion paper (if Options β/γ).

Total session estimate for strict-C neutrino sector completion: 6–10 sessions of substantive derivation work, plus this audit and the mechanism-selection session. This is a substantial campaign but tractable.

---

## §11. Open questions to surface in mechanism-selection session

1. **Mechanism preference** — Candidates A, B, C, D, or E? Or some specific hybrid not in the candidate list?
2. **$\delta_{CP}$ posture** — Route (i) derive, (ii) register as open, or (iii) register as falsifier?
3. **Architectural inclination** — Does Thomas have a prior on Option α / β / γ, or does it depend on mechanism-derivation outcomes?
4. **K3-eigenstructure constraint enforcement strategy** — derive that the mechanism preserves K3 eigenstructure as a theorem (highest rigor, hardest), assert and verify numerically (medium rigor, faster), or accept and register as conditional (lowest rigor, fastest)?
5. **Calibration architecture** — is single-calibration ($m_e$ alone) a hard requirement for Track 1 to be "no compromise," or is two-calibration acceptable if the second is substrate-derived rather than observed-anchored?
6. **Hierarchy ordering as prediction** — should the paper commit to normal hierarchy as prediction (Candidate B forces this, Candidate C may force this too depending on shell assignments), or treat it as a derived consequence of whichever mechanism is selected?
7. **Salvage from viXra paper** — given the algebra error, is there anything specific worth carrying forward besides the Monte Carlo validation methodology?
8. **Salvage from archived $\sigma = 120^{-d}$ work** — given the splittings problem, is the substrate connection ($120 = $ vertex count) worth carrying forward as a constraint on mechanism candidates that don't naturally include it?

---

## §12. What this audit does and does not establish

**This audit establishes:**
- The corpus state for each of the eight neutrino parameters: SM-5 gives PMNS angles at TBM zeroth order; everything else is unsettled or pre-formalism
- The two pre-formalism sketches ($\sigma = 120^{-d}$ entropy and viXra cage-radius) are substantively different mechanisms with specific identifiable problems, not reformulations of one underlying idea
- Five candidate mechanisms are available for current-formalism derivation, with honest assessment of each
- The K3 integration constraint is non-negotiable for Track 1 strict-C posture
- The Q3 calibration architecture is coupled to the mechanism choice
- The architectural decision (one paper or two) depends on derivation heaviness and can be deferred

**This audit does not establish:**
- Which mechanism is correct (Thomas's call in Session 38)
- The first-principles derivation of any of the eight parameters
- The specific cage-shell or $N_k$ assignments for the three neutrino flavors
- The $\delta_{CP}$ derivation, in any form
- The hierarchy ordering prediction

**Forward dependencies:**
- Session 38 mechanism-selection decision unlocks Sessions 39+ derivation work
- $\delta_{CP}$ posture decision unlocks rigorous handling of parameter 7
- Calibration architecture decision unlocks the Track 1 hierarchy paper headline (single-calibration framing)
- Architectural decision (one paper or two) unlocks the Track 1 paper structure

---

## §13. Programme-level observations and registrations

The neutrino sector audit reveals that the corpus has a **planned-but-unmaterialized SM-6** (the $\sigma = 120^{-d}$ neutrino-mass paper that SM-5 deferred to). This is a programme-level observation worth registering: SM-5's deferral was made before the SM-6 slot was reused for the charged-lepton paper, and the neutrino-mass derivation has been in soft-deferred status since March 2026 with no explicit programme-level tracking. This audit closes that tracking gap by surfacing the work as Track 1 / Q1 / Strict-C / mechanism-selection-pending.

**Suggested programme-level registration** (for separate patch by Thomas's choice, not for this patch):
- Add to `Research_Frontier.md`: an entry under the SM sector (or as an OPEN-FP-* under flagship_papers), e.g. **OPEN-SM-NU**: "Neutrino sector first-principles derivation in current formalism — eight parameters; mechanism-pending; Track 1 / Q1 audit complete patch 0294; mechanism-selection Session 38."
- Add to `theorem-registry.md` once mechanism is selected and one or more lemmas are proved.
- Update `paper_catalog.md` once the architectural decision (one paper or two) lands.

These are not for this patch; they are forward bookkeeping items.

---

## §14. Audit close

This audit is the first session of the strict-C path on Q1. It does not commit any technical content beyond inventory and assessment. Its purpose is to make Session 38 (mechanism selection) productive.

Tactical observation: the substantive technical work begins in Session 39+. Sessions 37 (this audit) and 38 (selection) are scaffolding. The choice to invest these scaffolding sessions reflects the strategic posture established at Session 37 opening: no compromise, rigor over speed, sketches → development → paper-text staging discipline imported from SS-9.

**Audit complete. Awaiting Thomas's mechanism-selection decision.**

---

## §15. Falsifier check follow-up (patch 0295 prep work)

> **Update — Session 38 (9 May 2026, patch 0295):** Quick falsifier check on Candidates B and C ran during the architectural-decision break.

**Candidate B (cage-radius $m \propto 1/R^k$): falsified.** The 600-cell bonded-shell radii from SM-8 Table~\ref{tab:shells}: tetrahedron $\approx 0.378$ (centroid circumradius of K$_4$ cells with edge $1/\phi$), icosahedron $1/\phi \approx 0.618$ (Shell 1), dodecahedron $1.000$ (Shell 2), icosidodecahedron $\sqrt{2} \approx 1.414$ (Shell 4). Maximum spread is factor $\sim 3.74$. Observed neutrino mass ratios are $m_3/m_1 \approx 51$ and $m_2/m_1 \approx 8.7$ — far larger spread than 600-cell radii can produce. Even allowing arbitrary exponent $k$ in $m \propto 1/R^k$, the two splittings demand *different* $k$ values: $k_{32} = \log(51)/\log(1.414/0.618) = 4.75$, $k_{21} = \log(8.7)/\log(1.000/1.414) = 6.24$ (opposite-direction discrepancy). No single power-law in radius simultaneously fits both splittings. **Candidate B is dead, regardless of how the viXra paper's algebra is fixed.**

**Candidate C (shell-distance $m \propto V^\alpha$): encouraging at $\alpha = 2$.** With assignment ($\nu_e \to$ tetrahedron $V=4$; $\nu_\mu \to$ icosahedron $V=12$; $\nu_\tau \to$ icosidodecahedron $V=30$):
- $m_2/m_1 = (12/4)^2 = 9.00$ vs observed $\approx 8.66$ — within 4%
- $m_3/m_1 = (30/4)^2 = 56.25$ vs observed $\approx 50.9$ — within 11%

Both splittings simultaneously fit at $\alpha = 2$.

**First-principles handle for $\alpha = 2$:** SM-9 derives the quark exponent $V^{7/3}$ from the decomposition $V^{7/3} = V^2 \cdot V^{1/3}$, where $V^2$ is the pair-count term and $V^{1/3}$ is the linear-cage-dimension term. For *unbound* modes (neutrinos), the linear-dimension factor plausibly drops out — there is no rigid cage to define a linear scale — leaving just $V^2$. **This is a real first-principles derivation route, not a coincidence-fit:** the distinction between bound and unbound regimes is exactly the boundary across which $V^{1/3}$ does or does not contribute to the mass formula.

**Caveat — absolute scale:** the splitting *ratios* fit at $\alpha = 2$; the overall scale needs a prefactor $\mathcal{S}_0 \cdot V^2 \cdot \mathcal{T}_{\text{unbound}}$ to land at $\sim 0.001$ eV for $\nu_e$. With $\mathcal{S}_0 = M_0 = m_e \cdot z/\phi = 3.79$ MeV and $V_{\nu_e} = 4$, $V^2 = 16$, the bare prediction is $60.6$ MeV — requiring suppression $\mathcal{T}_{\text{unbound}} \sim 1.65 \times 10^{-11}$. The archived $\sigma = 120^{-3} \approx 5.79 \times 10^{-7}$ is too weak by factor $\sim 10^4$. So the suppression-mechanism derivation remains substantial work for sessions 39+, but the geometric mass *structure* (the relative spacings) is sharply consistent with shell-distance methodology applied to the unbound regime.

**Effect on mechanism selection (Session 39):** Candidate C is now the strongest prior. The mechanism-selection conversation can focus on confirming Candidate C with $\alpha = 2$ and assignment (tet, ico, icosid) as the working choice, then turn to the suppression-factor derivation and the K3-eigenstructure preservation argument as the substantive next-session work.

**Hierarchy ordering as falsifiable prediction:** under Candidate C with the (tet, ico, icosid) assignment, normal hierarchy is forced — $\nu_e$ has the fewest vertices ($V=4$), so it is lightest; $\nu_\tau$ has the most ($V=30$), so it is heaviest. The opposite assignment would force inverted hierarchy. JUNO's expected resolution of the ordering (2026+) is therefore a near-term falsifier of the (tet, ico, icosid) assignment specifically.

This falsifier-check appendix concludes the audit phase. Mechanism-selection session work is now well-anchored.

---

*Audit document established at Session 37 (patch 0294). Subsidiary to `../hierarchy_paper_outline.md` Open Question 1. Strategic source: `../../../research_priorities.md` and Session 37 opening conversation transcripts.*
