# Phenomena — F.1 Dynamical Substrate Law: Substrate-Locality of DI-Bit Currents at Vertex-Aligned Reading C in the 600-Cell

> **v1.0 SHIPPED STATUS NOTE (Patch 0572e, 24 May 2026, Session 143)**: This file is written at F.1 v1.0 SHIPPED state (Patch 0570, Session 142, 24 May 2026). The phenomenon F.1 addresses is **OPEN-SD-CHIR-PRIMITIVE manifestation (iv) thermodynamic causal arrow** — closed at sketch-document Layer 3 via Theorem 7.1 substrate-locality umbrella. **Important scope clarification preserved end-to-end:** F.1 closes manifestation (iv) at the *substrate-locality structure* level only; the candidate thermodynamic-arrow emergence narrative (entropy production / coarse-graining / macroscopic irreversibility) is *supported by* but *not derived from* the closure. The emergence layer is registered as future work beyond the present paper's framework qualifiers (§10 explicit disclaimer). Predictions are structural mathematical constants (not empirical-comparison predictions in the SS-7 / SF-4 / SM-2 sense); the swarm-validation contribution is at the structural-constant + cross-sector-consistency level.

**Paper:** `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.tex` (v1.0 SHIPPED 24 May 2026, Session 142 Patch 0570)
**Verification scripts:** `flagship_papers/dynamical_substrate_law/code/` (5 Python scripts; all 12 mathematical-correspondence-table claims numerically verified)
**Last updated:** 24 May 2026 (Session 143 Patch 0572e)

---

## PHEN-E — Empirical phenomena addressed

### 1. OPEN-SD-CHIR-PRIMITIVE manifestation (iv): thermodynamic causal arrow

- **SM status:** The arrow of time and macroscopic irreversibility are observed empirical phenomena across all of physics (cosmological + thermodynamic + radiative + biological arrows). The Standard Model itself does not derive the arrow of time; conventional explanations invoke either initial-condition asymmetry (Past Hypothesis) or statistical-mechanical coarse-graining of unitary dynamics. The substrate-level origin of the arrow remains an open foundational question.
- **CPP derivation status at v1.0 SHIP:** F.1 closes manifestation (iv) at **sketch-document Layer 3** via Theorem 7.1 substrate-locality umbrella. The closure is at the **substrate-locality structure level** — the closed-form first-order DI-bit current $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$ supports the candidate substrate mechanism for the thermodynamic causal arrow.
- **What the paper does NOT derive (explicit §10 disclaimer):** entropy production, coarse-graining, or macroscopic irreversibility in the conventional physics sense. Those derivations are future work beyond F.1's framework qualifiers. The substrate-locality structure is the *foundation upon which* an emergence-layer derivation would build, not a finished thermodynamic-arrow theory.
- **Closure status across the chirality continuum at v1.0 SHIP:** (i) parity violation, (ii) neutrino chirality structure, (iii) weak isospin assignment — all CLOSED at Layer 3 in Capotauro v2.0 (spatial sector); (iv) thermodynamic causal arrow — CLOSED at sketch-document Layer 3 in F.1 (this paper, temporal sector); (v) Sector-5 schema — OPEN as OPEN-FP-F1-4.

### 2. F.1 sub-question of OPEN-SD-CHIR-PRIMITIVE

- **SM status:** Not addressed in the Standard Model (the F.1 sub-question is internal to the CPP programme's chirality continuum architecture).
- **CPP closure status at v1.0 SHIP:** F.1 sub-question SHIPPED at v1.0 with strongest-positive cross-reviewer convergent verdict. The question "Does CPP imply substrate-locality of DI-bit currents at vertex-aligned Reading C?" has its v1.0 SHIPPED answer: YES, at sketch-document Layer 3, via Theorem 7.1 with three publication-grade Layer 3 trio inputs (Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2).

---

## PHEN-P — Zero-parameter structural predictions

F.1's predictions are structural mathematical constants emerging from the 600-cell geometric structure + Mechanism A framework axiom. Unlike SS-7 / SF-4 / Capotauro v2.0 (which produce predictions for measured empirical quantities), F.1's predictions are at the **internal substrate-physics level** — they are first-principle calculations on the 600-cell substrate that any future emergence-layer derivation must respect.

### 3. Host-to-first-shell uniform projection constant

- **Prediction:** $\hat{u}_i \cdot \hat{n} = -1/(2\phi) \approx -0.309$ uniformly across all 12 first-shell neighbours at vertex-aligned Reading C in the 600-cell.
- **Numerical value:** $-1/(2\phi) = -(\sqrt{5}-1)/2 = -0.309017\ldots$
- **Testable:** Computationally verified to floating-point precision at `code/verify_phase1.py` identity (1). Analytically derived from G1 first-shell inner-product primitive + icosahedral residual symmetry $H_3 = I_h$.
- **Falsifier:** Demonstration via explicit 600-cell calculation that $\hat{u}_i \cdot \hat{n} \neq -1/(2\phi)$ for some first-shell vertex. Testable on Coxeter's canonical 600-cell coordinates.
- **Cross-sector consistency:** Identical structural constant appears in Capotauro v2.0 §3 spatial-sector substrate-locality theorem.

### 4. First-shell unit-vector sum identity

- **Prediction:** $\sum_{i=1}^{12} \hat{u}_i = -(6/\phi)\,\hat{n} \approx -3.708\,\hat{n}$.
- **Numerical value:** $6/\phi = 6(\phi - 1) = 3.708204\ldots$
- **Testable:** Computationally verified at `code/verify_phase1.py` identity (2). Analytically follows from item 3 (uniform projection $-1/(2\phi)$) + orthogonal-component cancellation by $I_h$ residual symmetry: the sum of 12 unit vectors in a regular icosahedron with uniform $\hat{n}$-projection has only the $\hat{n}$-component surviving.

### 5. Icosahedral rank-1 sum identity

- **Prediction:** $\sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n})\,\hat{u}_i = (3/\phi^2)\,\hat{n} \approx 1.146\,\hat{n}$.
- **Numerical value:** $3/\phi^2 = 3(2-\phi) = 1.145898\ldots$
- **Testable:** Computationally verified at `code/verify_phase1.py` identity (3). Algebraically: combining items 3 + 4 with the uniform-projection factor gives $(\hat{u}_i \cdot \hat{n})\,\hat{u}_i = -(1/(2\phi))\,\hat{u}_i$, summed over $i$ this becomes $-(1/(2\phi))(-(6/\phi)\,\hat{n}) = (3/\phi^2)\,\hat{n}$.

### 6. Substrate-locality umbrella coefficient $6/\phi^2$

- **Prediction:** $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$ at the host vertex at first order in the Mechanism A asymmetry parameter $\delta$.
- **Numerical value:** $6/\phi^2 = 6(2-\phi) = 2.291796\ldots$ (the universal structural constant for the temporal sector at vertex-aligned Reading C in the 600-cell substrate).
- **Testable:** Computationally verified at `code/verify_phase1.py` identity (4) for any value of $\delta$. Analytically derived from item 5 (icosahedral rank-1 sum) + Mechanism A's framework-local current construction at $\mathcal{O}(\delta^1)$ (per-edge contribution factor of 2).
- **Falsifier:** Demonstration of a different prefactor on $\hat{n}$ at $\mathcal{O}(\delta^1)$ from any valid first-principles calculation on the 600-cell with Mechanism A inputs. Also falsifiable by demonstration of any tangent-to-$\hat{n}$ component at first order.

### 7. First-shell-to-first-shell edge perpendicularity

- **Prediction:** $\hat{e}_{ij} \cdot \hat{n} = 0$ for all 30 first-shell-to-first-shell edges at vertex-aligned Reading C.
- **Testable:** Computationally verified at `code/verify_b1q2_curl_content.py` (the K3-base protection identity that makes first-order curl content vanish at the host vertex).
- **Falsifier:** Demonstration of $\hat{e}_{ij} \cdot \hat{n} \neq 0$ for some first-shell-to-first-shell edge. Testable on Coxeter's canonical 600-cell coordinates.
- **Cross-sector consistency:** This is the **same identity Capotauro v2.0 uses for spatial-sector K3-base protection** (§5.6 cross-reference in F.1).

### 8. First-shell-vertex current magnitude (foundations-work prediction; not in paper body)

- **Prediction:** $|\vec{j}(v_i)| = 2 r_0 \delta \sqrt{7-\phi}$ uniform across all 12 first-shell vertices.
- **Numerical value:** $\sqrt{7-\phi} = 2.317216\ldots$ ⟹ $|\vec{j}(v_i)| \approx 4.634\, r_0 \delta$.
- **Testable:** Computationally verified at `code/verify_b1q4_first_shell_current_sum.py` identity (4). Analytically derived in sub-question B.1.q4 of F.1 foundations work.
- **Note:** Not part of the paper body's main result; appears in foundations-work artifacts at `sketches/F1_phase2_foundations_work.md`.

### 9. First-shell-vertex sum identity (foundations-work prediction; not in paper body)

- **Prediction:** $\sum_{i=1}^{12} \hat{j}(v_i) = (24/\sqrt{7-\phi})\,\hat{n} \approx 10.345\,\hat{n}$.
- **Numerical value:** $24/\sqrt{7-\phi} = 10.357\ldots$ (the foundations-work B.1.q4 identity).
- **Testable:** Computationally verified at `code/verify_b1q4_first_shell_current_sum.py` identity (5).
- **Note:** Not part of paper body's main result; appears in foundations-work artifacts.

### 10. Discrete curl vanishing at host vertex (foundations-work prediction)

- **Prediction:** The discrete curl of $\vec{j}_{DI}^{\text{net}}$ at the host vertex vanishes at first order in $\delta$: $(\nabla \times \vec{j}_{DI}^{\text{net}})(\vhost) = 0$ at $\mathcal{O}(\delta)$.
- **Testable:** Computationally verified at `code/verify_b1q2_curl_content.py` via the trapezoidal circulation of $\vec{j}_{DI}^{\text{net}}$ around any of the 30 host-first-shell side-face triangles. The 30 face 2-forms span the full 6D 2-form space at $\vhost$ under $I_h$ symmetry; zero circulation on all 30 side faces ⟹ full 4D curl 2-form vanishes.
- **Structural origin:** The cancellation follows from item 7 (first-shell-to-first-shell perpendicularity $\hat{e}_{ij} \cdot \hat{n} = 0$) — the K3-base protection identity that Capotauro shares.
- **Significance:** The curl-free property at first order is STRONGER than sub-question B.1.b's ansatz (which required only no perpendicular-to-$\hat{n}$ component); it confirms the substrate current is conservative (locally gradient-like) at the host vertex.

---

## PHEN-V — Consilience with other CPP results

### 11. Shared structural constant $-1/(2\phi)$ with Capotauro v2.0

- **Capotauro v2.0 §3 spatial-sector substrate-locality theorem** uses the identical structural constant $-1/(2\phi)$ for the first-shell host-to-first-shell projection in the K3-doublet spatial sector. F.1 and Capotauro v2.0 share the same first-shell geometric identities (G1 + G2 + Theorem 5.1 analog + Theorem 5.2 analog) despite different physical-sector contexts (spatial vs temporal). This is the methodological pattern of "shared first-shell identities governing both spatial and temporal sectors" that Grok R1 emphasized as a structural payoff.

### 12. Chirality continuum closure pattern (4 of 5 manifestations now closed)

- **Closed manifestations (4 of 5):**
  - (i) Parity violation — Capotauro v2.0 spatial sector at Layer 3.
  - (ii) Neutrino chirality structure — Capotauro v2.0 spatial sector at Layer 3.
  - (iii) Weak isospin assignment — Capotauro v2.0 spatial sector at Layer 3.
  - (iv) Thermodynamic causal arrow — **F.1 (this paper) temporal sector at sketch-document Layer 3**.
- **Open manifestation:**
  - (v) Sector-5 schema — OPEN-FP-F1-4 (candidate domains: thermal-equilibrium gauge fixing, symmetry-restoration dynamics at electroweak crossover, cosmological-arrow alignment).

### 13. CPP corpus track record grounding (programme epistemic methodology)

The substrate-locality umbrella result extends the CPP corpus's swarm-validation track record into the temporal sector. The corpus track record at v1.0 SHIP:

- **SS-7 v1.2** — 12 zero-parameter predictions for alpha-chain nuclei ¹²C–⁴⁸Cr within ±1.5%; RMS 0.80%.
- **SS-2** — proton charge radius 0.851–0.883 fm at zero parameters.
- **SS-4** — QCD string tension $\sigma = M_0 z^2/(\phi \cdot l_{\text{edge}}) = 926.5$ MeV/fm at zero parameters.
- **SS-5** — deuteron binding energy $B_d = 2.222$ MeV at $-0.09\%$ at zero parameters.
- **SM-8** — derivation $M_0 = m_e \cdot z/\phi = 3.79$ MeV.
- **SF-4 v1.0** — 7/8 zero-parameter neutrino-sector predictions including $\theta_{23} = 0.86$ at 5/2 mass-hierarchy precision.
- **Capotauro v2.0 v1.0 SHIPPED** — three-way cross-sector substrate-chirality unification $|M^{K_3}| = |M^W| = |M^{qDP}| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ at zero free parameters across three structurally distinct sector mechanisms at full Layer 3 rigor.
- **F.1 v1.0 SHIPPED (this paper)** — substrate-locality structure with closed-form coefficient $6/\phi^2$ at sketch-document Layer 3; first F-line flagship v1.0 SHIP in CPP corpus.

The corpus track record grounds the F.1 programme epistemic methodology at the precedent-validated level: the same 600-cell substrate + golden ratio + foundational-input + Layer-discipline architecture that produces SS-7's 12 zero-parameter alpha-chain predictions also produces F.1's substrate-locality umbrella. The methodological consistency is the swarm-validation contribution.

### 14. Hardened-theorems trio convention establishment

The F.1 paper's three publication-grade hardened-theorem artifacts (`hardened_theorems/perturbation_locality.tex`, `first_shell_perpendicularity.tex`, `host_first_shell_projection.tex`; 741 lines LaTeX combined, Patches 0550 + 0551 + 0552) establish the hardened-theorems trio convention for F-line flagship trajectories. Future F-line flagship papers (F.2, F.3, etc.) inherit this convention: at v1.0 SHIP, the umbrella theorem assembles 3+ publication-grade Layer 3 hardened-theorem artifacts at `hardened_theorems/` of the flagship paper directory.

---

## PHEN-F — Falsifiers

### Theorem-level falsifiers (direct mathematical falsification channels):

| # | Falsifier | Theorem | Status at v1.0 SHIP |
|---|---|---|---|
| F1.1 | $\hat{u}_i \cdot \hat{n} \neq -1/(2\phi)$ for some 600-cell first-shell vertex | Theorem 5.1 | Verified false at `verify_phase1.py` (identity holds) |
| F1.2 | $\hat{e}_{ij} \cdot \hat{n} \neq 0$ for some first-shell-to-first-shell edge | Theorem 5.2 | Verified false at `verify_b1q2_curl_content.py` |
| F1.3 | First-order-in-$\delta$ contribution beyond first-shell range | Theorem 6.1 + Corollary 6.2 | Verified false at `verify_phase4.py` shell-confinement check |
| F1.4 | Closed-form prefactor on $\hat{n}$ different from $6/\phi^2$ at $\mathcal{O}(\delta^1)$ | Theorem 7.1 | Verified false at `verify_phase1.py` identity (4) |
| F1.5 | Tangent-to-$\hat{n}$ component of $\vec{j}_{DI}^{\text{net}}(\vhost)$ at $\mathcal{O}(\delta^1)$ | Theorem 7.1 | Verified false (parallel-to-$\hat{n}$ structure) |

### Framework-level falsifiers (Mechanism A as input):

| # | Falsifier | Open Problem | Status at v1.0 SHIP |
|---|---|---|---|
| F1.6 | Mechanism A is not derivable from CPP primitive axioms A1–A11 | OPEN-FP-F1-2 (Layer 4 axiomatic derivation) | Open (long-term programme target) |
| F1.7 | G1 first-shell inner-product primitive fails publication-grade hardening | OPEN-FP-F1-3 (G1 publication-grade hardening) | Open (RECOMMENDED first post-Phase-7 substantive physics Patch) |

### Programme-level falsifiers (chirality continuum architecture):

| # | Falsifier | Status at v1.0 SHIP |
|---|---|---|
| F1.8 | Manifestation (v) of OPEN-SD-CHIR-PRIMITIVE does not exist or is not identifiable | OPEN-FP-F1-4 (Sector-5 schema instantiation) |
| F1.9 | Non-vertex-aligned Reading C variants produce qualitatively different substrate-locality structures (weakens universality claim) | OPEN-FP-F1-5 (non-vertex-aligned Reading C variants) |
| F1.10 | Higher-order corrections at $\mathcal{O}(\delta^2)$ introduce tangent-to-$\hat{n}$ components inconsistent with first-order parallel-to-$\hat{n}$ structure | OPEN-FP-F1-1 ($\mathcal{O}(\delta^2)$ extension) |

---

## PHEN-O — Out of scope at v1.0 SHIP (deferred to v2.0+ or future trajectory)

### Substrate-physics emergence layer (the largest scope item out of scope):

- **Thermodynamic-arrow emergence** in the conventional physics sense (entropy production / coarse-graining / macroscopic irreversibility) — explicitly disclaimed at §10. The substrate-locality structure of Theorem 7.1 *supports* the candidate substrate mechanism for the thermodynamic causal arrow but does not derive emergence. Future work beyond F.1's framework qualifiers.
- **Continuum-limit field theory** for the substrate-locality structure — not attempted at this paper.

### Hardening trajectory:

- **OPEN-FP-F1-3** G1 publication-grade hardening (RECOMMENDED first post-Phase-7 substantive physics Patch).
- **§7.4 candidate follow-up Patch** independent publication-grade hardening of Theorem 7.1 umbrella (not formal Open Problem to preserve 5-OP commitment).

### Extension trajectory:

- **OPEN-FP-F1-1** extension to $\mathcal{O}(\delta^2)$ + higher orders.
- **OPEN-FP-F1-2** Layer 4 axiomatic derivation of Mechanism A from A1–A11.

### Reading C variant trajectory:

- **OPEN-FP-F1-5** non-vertex-aligned Reading C variants (edge-aligned $D_3$ + face-aligned $D_2$).

### Chirality continuum trajectory:

- **OPEN-FP-F1-4** Sector-5 schema instantiation (manifestation (v)).

### Companion-paper trajectory:

- **OPEN-FP-F1-6** prose-density tightening Patch + F.1-condensed companion paper trajectory (registered post-SHIP from ChatGPT R6 strategic suggestion).

### Cross-flagship-paper trajectory (F.2, F.3, …):

- F.2 / F.3 sub-question trajectory openings — not yet scoped at v1.0 SHIP; candidates for future flagship trajectories building on F.1's methodology pattern.

---

## PHEN-X — Cross-sector consistency checks at v1.0 SHIP

### Capotauro v2.0 cross-reference (§5.6 of F.1)

- **Shared first-shell identity G1**: F.1's Theorem 5.1 + Theorem 5.2 + Capotauro v2.0 §3 spatial-sector theorems all depend on the same first-shell inner-product primitive structure. G1 hardening (OPEN-FP-F1-3) would simultaneously discharge conditionality in both papers.
- **Shared structural constant $-1/(2\phi)$**: appears identically in F.1 host-to-first-shell uniform projection + Capotauro v2.0 spatial-sector substrate-locality projection.
- **Shared first-shell-to-first-shell perpendicularity (K3-base protection)**: F.1 Theorem 5.2 + Capotauro v2.0 K3-base protection identity are the same geometric fact ($\hat{e}_{ij} \cdot \hat{n} = 0$).

### OPEN-SD-CHIR-PRIMITIVE manifestation closure pattern

The chirality continuum architecture (Capotauro v2.0 + chirality continuum sketch document) anticipates that the substrate-direction primitive $\hat{n}$ manifests across multiple sectors. At v1.0 SHIP of F.1:

- 4 of 5 manifestations closed (i, ii, iii at Capotauro v2.0; iv at F.1)
- 1 of 5 manifestations open (v as OPEN-FP-F1-4)

The closure pattern is consistent with the chirality continuum architecture's prediction that substrate-direction primitive manifestations span both spatial-sector and temporal-sector physics; F.1 is the first temporal-sector closure.

### Reviewer-pause cycle convention precedent

F.1 trajectory establishes the **canonical reviewer-pause cycle worked example** for future F-line flagship trajectories per `templates/operating_system.md` §17 + `templates/paper_completion_checklist.md` "Reviewer-Pause Cycle Precondition for Flagship-Paper-Trajectory Work". Pre-paper-assembly arc: Patches 0531–0537 closed seven sub-questions at sketch Layer 2 → Patch 0538 calibration response → Patch 0539 status upgrade → Layer 3 promotion + flagship paper assembly Patches 0554–0570.

---

## Swarm-validation contribution at v1.0 SHIP

F.1's contribution to the CPP corpus swarm-validation track record:

1. **Two structural constants at zero free parameters**: $-1/(2\phi)$ (host-to-first-shell uniform projection) + $6/\phi^2$ (substrate-locality umbrella coefficient). Both verified computationally to floating-point precision.
2. **Cross-sector consistency with Capotauro v2.0**: shared structural constant $-1/(2\phi)$ + shared first-shell geometric identities. This cross-sector consistency is itself a swarm-validation contribution — the methodological pattern of "shared first-shell identities governing both spatial and temporal sectors" is corpus-establishing.
3. **First F-line flagship v1.0 SHIP**: methodologically establishes the F-line flagship trajectory template (hardened-theorems trio convention + reviewer-pause cycle precondition + scope-framing subtitle convention + anti-erasure discipline + 5-OP commitment + sketch-document Layer 3 umbrella with publication-grade Layer 3 trio inputs).
4. **Closes chirality continuum manifestation (iv)** at sketch-document Layer 3. The chirality continuum architecture's 4 of 5 manifestations are now closed.

The swarm-validation contribution at v1.0 SHIP is **structural-consistency-driven**, not empirical-prediction-driven (unlike SS-7's 12 alpha-chain nuclei predictions or SF-4's 7/8 neutrino-sector predictions). The structural-consistency contribution is the appropriate swarm-validation mode for a flagship framework theorem paper at sketch-document Layer 3.

---

*Phenomena file created Session 143 Patch 0572e (24 May 2026) as the sixth SHIP-time companion documentation file in Phase 7A. Per `templates/documentation-suite.md` §4 + checklist §A A3 (PHEN-E + PHEN-P + PHEN-V) + Capotauro reference implementation `phenomena-capotauro.md` extended structure (PHEN-E + PHEN-P + PHEN-F + PHEN-O + PHEN-X + swarm-validation contribution). Source priorities per docsuite.md §32: items 6 + 9 + current registry state (scripts + `.tex` source + predictions.md + paper_catalog.md). This file is maintained continuously from this Patch forward; future paper-version increments trigger PHEN-P additions (new zero-parameter predictions), PHEN-V additions (new cross-paper consilience), and PHEN-O retirements (as out-of-scope items get closed at follow-up Patches).*
