# Philosophy — F.1 Dynamical Substrate Law: Substrate-Locality of DI-Bit Currents at Vertex-Aligned Reading C in the 600-Cell

> **v1.0 SHIPPED STATUS NOTE (Patch 0572f, 24 May 2026, Session 143)**: This file is written at F.1 v1.0 SHIPPED state (Patch 0570, Session 142, 24 May 2026). The philosophical position is the **structurally-grounded sketch-document Layer 3 flagship framework preprint** stance: F.1 proves what it can prove (the substrate-locality structure) at the rigor it can prove it (publication-grade Layer 3 trio + sketch-document Layer 3 umbrella), and *explicitly preserves* the Layer distinction + conditionality + open-problem inventory rather than collapsing them into a unified flagship narrative. The position emerged from a six-round ChatGPT reviewer cycle (Patches 0568–0569e) where the recurring reviewer pressure to harden the umbrella beyond its current rigor was answered with the **anti-erasure discipline**: do not erase the uncertainty structure during paper polishing.

**Paper:** `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.tex` (v1.0 SHIPPED 24 May 2026, Session 142 Patch 0570)
**Last updated:** 24 May 2026 (Session 143 Patch 0572f)

---

## What kind of result is this?

F.1 is a **structurally-grounded sketch-document Layer 3 flagship framework preprint with publication-grade hardened components but non-publication-grade umbrella theorem**. This nine-word paper-type declaration is itself a methodological commitment, captured in the title-page scope subtitle (Variant b `\date{}` line scope-framing pattern) at first reader contact. Each clause carries weight:

- **"Structurally-grounded"** — the paper rests on three publication-grade Layer 3 hardened-theorem artifacts at `hardened_theorems/` (Patches 0550 + 0551 + 0552; 741 lines LaTeX combined). The umbrella theorem (Theorem 7.1) does not rest on speculative inputs; its inputs are at the strongest rigor the corpus presently produces.
- **"Sketch-document Layer 3"** — the umbrella theorem's *assembly* is at sketch-document Layer 3, not publication-grade. The umbrella has not been independently hardened with explicit hypothesis tracking + five-class exclusion enumeration of the umbrella-level inputs. This is a real Layer-rigor gap, transparently preserved.
- **"Flagship framework preprint"** — the paper is the first F-line flagship paper in CPP corpus, second flagship paper overall after Capotauro v2.0. "Preprint" rather than "finished publication" because key follow-up work (G1 hardening, umbrella hardening, Layer 4 derivation) is registered as Open Problems rather than completed at v1.0 SHIP.
- **"Publication-grade hardened components but non-publication-grade umbrella theorem"** — the components-vs-umbrella Layer distinction is the central honesty commitment. Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2 are publication-grade Layer 3 (the first two conditional on G1); Theorem 7.1 the umbrella is sketch-document Layer 3 only.

The paper-type declaration is not a hedge or a retreat. It is the **maximally honest framing** of what the paper actually proves at the rigor it actually proves it. The alternative framings considered and rejected during the reviewer cycle: (i) Variant (a) "G1-hardening-first" approach that would push v1.0 SHIP to after OPEN-FP-F1-3 closure; (ii) collapsing the Layer distinction into a single "Layer 3" claim; (iii) softening the umbrella theorem statement to obscure its sketch-document Layer 3 status. Variant (b) was selected on multi-round cross-reviewer convergent verdict + ChatGPT R3–R6 scope-framing convergence + CPP corpus convention.

---

## Layer classification

F.1 stratifies its content across the CPP corpus's Layer hierarchy:

| Element | Layer | Status |
|---|---|---|
| Theorem 5.1 (host-to-first-shell uniform projection) | Layer 3 publication-grade | Conditional on G1 (OPEN-FP-F1-3) |
| Theorem 5.2 (first-shell-to-first-shell perpendicularity) | Layer 3 publication-grade | Conditional on G1 (OPEN-FP-F1-3) |
| Theorem 6.1 (perturbation-theory propagation rule) | Layer 3 publication-grade | Unconditional |
| Corollary 6.2 (shell-locality at $\mathcal{O}(\delta^1)$) | Layer 3 publication-grade | Unconditional (immediate corollary of 6.1) |
| **Theorem 7.1 (substrate-locality umbrella)** | **Layer 3 sketch-document** | Assembly of inputs above; umbrella *itself* not independently hardened |
| Lemma "G1 first-shell inner-product primitive" | Layer 3 sketch-document | Imported from Patch 0541 §3.1; publication-grade hardening is OPEN-FP-F1-3 |
| Axiom MA.1 (Mechanism A propagation-rate asymmetry) | Layer 3 framework axiom input | Layer 4 axiomatic derivation from A1–A11 is OPEN-FP-F1-2 |
| Axiom MA.2 (Mechanism A framework-local current construction) | Layer 3 framework axiom input | Layer 4 axiomatic derivation is OPEN-FP-F1-2 |
| OPEN-SD-CHIR-PRIMITIVE manifestation (iv) closure | Layer 3 sketch-document | Closed at substrate-locality structure level only; thermodynamic-arrow emergence narrative supported but not derived |
| 5 Open Problems (OPEN-FP-F1-1 through OPEN-FP-F1-5) | Various | Registered at body §9 with explicit independence analysis |
| OPEN-FP-F1-6 (prose-density tightening) | Layer 0 (scoping) | Registered separately at Patch 0569e from R6 follow-up |

**The publication-grade Layer 3 trio + sketch-document Layer 3 umbrella architecture is itself a programme-level methodological pattern.** Future F-line flagship trajectories (F.2, F.3, etc.) inherit this pattern: assemble the umbrella theorem from 3+ publication-grade Layer 3 hardened-theorem artifacts; preserve the sketch-document-vs-publication-grade Layer distinction transparently at the umbrella level; register umbrella publication-grade hardening as a candidate follow-up Patch rather than blocking v1.0 SHIP on it.

---

## Certainty levels per element

**HIGH certainty (theorem-level + algorithmically verifiable):**

- The host-to-first-shell uniform projection $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ is verified to floating-point precision at `verify_phase1.py` identity (1) on Coxeter's canonical 600-cell coordinates. The identity is a direct consequence of the 600-cell geometry; conditional on G1 (which itself is at sketch-document Layer 3 but supported by the regular-polytope reference + icosahedral residual symmetry).
- The first-shell-to-first-shell perpendicularity $\hat{e}_{ij} \cdot \hat{n} = 0$ is verified at `verify_b1q2_curl_content.py` and is the same identity Capotauro v2.0 uses for spatial-sector K3-base protection.
- The substrate-locality umbrella coefficient $6/\phi^2 \approx 2.293$ is verified at `verify_phase1.py` identity (4) for any value of $\delta$.

**MEDIUM-HIGH certainty (publication-grade Layer 3, hardened at `hardened_theorems/*.tex`):**

- The perturbation-theory propagation rule (Theorem 6.1) + shell-locality corollary (Corollary 6.2) is at publication-grade Layer 3 unconditional, hardened at `hardened_theorems/perturbation_locality.tex` (Patch 0550) with explicit hypothesis tracking + five-class exclusion enumeration. The hardening covers the trickiest mathematical step (Lemma 6.3.1 connected-subgraph confinement, ChatGPT R2 "least transparent mathematical step").

**MEDIUM certainty (sketch-document Layer 3):**

- The substrate-locality umbrella (Theorem 7.1) is at sketch-document Layer 3 because the three-step assembly itself (shell confinement → first-shell-to-first-shell perpendicularity zeroes 30 contributions → icosahedral rank-1 sum identity gives the coefficient) has not been independently hardened. The constituent steps are individually at publication-grade Layer 3 or higher; the assembly inherits the higher of the input rigors as a *lower bound* on its rigor, but the assembly's own structural exclusions have not been enumerated at publication-grade.

**MEDIUM certainty (framework axiom):**

- Mechanism A axioms MA.1 + MA.2 are at framework-axiom rigor. They are not derived from CPP primitive axioms A1–A11 at this paper's scope. The framework-axiom strategy is methodologically standard for Layer 3 papers; Layer 4 axiomatic derivation is registered as OPEN-FP-F1-2 (long-term programme target).

**LOW certainty (candidate mechanism narrative):**

- The connection from substrate-locality structure to thermodynamic-arrow emergence (entropy production / coarse-graining / macroscopic irreversibility) is a **candidate mechanism narrative supported by** the substrate-locality structure, **not derived from** it. §10 explicit disclaimer states this. The emergence-layer derivation is future work beyond the present paper's framework qualifiers.

---

## Falsifiability inventory (with threshold values)

F.1 has a 10-falsifier inventory spanning theorem-level + framework-level + programme-level falsifications (full enumeration in `phenomena-dynamical-substrate-law.md` PHEN-F section). The threshold values for each:

| Falsifier | Threshold |
|---|---|
| Theorem 5.1 falsifier (host-to-first-shell uniform projection) | Any first-shell vertex with $\hat{u}_i \cdot \hat{n} \neq -1/(2\phi)$ at exact arithmetic on Coxeter's canonical coordinates |
| Theorem 5.2 falsifier (first-shell-to-first-shell perpendicularity) | Any first-shell-to-first-shell edge with $\hat{e}_{ij} \cdot \hat{n} \neq 0$ at exact arithmetic |
| Theorem 6.1 falsifier (perturbation-theory propagation rule) | Any first-order-in-$\delta$ contribution from a vertex beyond first-shell range (graph-distance > 1 at $\mathcal{O}(\delta^1)$) |
| Theorem 7.1 falsifier (closed-form prefactor) | Any valid first-principles calculation yielding a prefactor different from $6/\phi^2$ at $\mathcal{O}(\delta^1)$ |
| Theorem 7.1 falsifier (tangent-to-$\hat{n}$ component) | Any nonzero tangent-to-$\hat{n}$ component of $\vec{j}_{DI}^{\text{net}}(\vhost)$ at $\mathcal{O}(\delta^1)$ |
| Mechanism A Layer 4 falsifier | Demonstration that no derivation from A1–A11 alone can produce the propagation-rate asymmetry primitive (would close OPEN-FP-F1-2 negatively) |
| G1 publication-grade hardening falsifier | Failure of G1 hardening attempt to produce a publication-grade Layer 3 `hardened_theorems/first_shell_inner_product_primitive.tex` artifact (would close OPEN-FP-F1-3 negatively) |
| OPEN-SD-CHIR-PRIMITIVE manifestation (v) existence falsifier | Demonstration that no Sector-5 schema instantiation is identifiable (would close OPEN-FP-F1-4 negatively) |
| Non-vertex-aligned Reading C universality falsifier | Demonstration that edge-aligned or face-aligned Reading C produces qualitatively different substrate-locality structures inconsistent with vertex-aligned (would close OPEN-FP-F1-5 with universality-claim weakening) |
| $\mathcal{O}(\delta^2)$ extension falsifier | Higher-order corrections introducing tangent-to-$\hat{n}$ components inconsistent with first-order parallel-to-$\hat{n}$ structure (would close OPEN-FP-F1-1 with extension-impossibility) |

All theorem-level falsifiers are **directly testable on Coxeter's canonical 600-cell coordinates** with the verification scripts already in `code/`. The framework-level + programme-level falsifiers require open-problem-closure work, but each closure trajectory is independently scoped at the body §9 + post-SHIP follow-up specification.

---

## Relationship to Standard Model

**F.1 does not address Standard Model physics directly.** The substrate-locality theorem and its supporting first-shell geometric identities are internal substrate-physics statements about the 600-cell + DI-bit framework, not Standard Model predictions for measured quantities.

However, the **chirality continuum architecture** (Capotauro v2.0 + chirality continuum sketch document + F.1) does connect to electroweak Standard Model physics via the substrate-direction primitive $\hat{n}$:

- **Manifestation (i) parity violation** — addressed in Capotauro v2.0 (spatial sector, K3-doublet) with explicit Standard Model connection via the $\Delta p_{LR} = \chi/6 \approx 0.0394$ leptogenesis-back-derived empirical anchor.
- **Manifestation (ii) neutrino chirality structure** — addressed in Capotauro v2.0 + SF-2 / SF-4 trajectory with explicit V–A coupling and helicity-limit content.
- **Manifestation (iii) weak isospin assignment** — addressed in Capotauro v2.0 spatial sector.
- **Manifestation (iv) thermodynamic causal arrow** — addressed in F.1 at sketch-document Layer 3. **Not a Standard Model phenomenon**; the arrow of time and macroscopic irreversibility are observed across all of physics, with the conventional explanation invoking either initial-condition asymmetry (Past Hypothesis) or statistical-mechanical coarse-graining of unitary dynamics, neither of which the Standard Model derives at the substrate level.
- **Manifestation (v) Sector-5 schema** — OPEN-FP-F1-4; candidate domains include thermal-equilibrium gauge fixing (potentially connects to electroweak crossover SM physics) + symmetry-restoration dynamics + cosmological-arrow alignment.

F.1's relationship to the Standard Model is therefore **mediated through the chirality continuum**: F.1 closes a sector of the umbrella OPEN-SD-CHIR-PRIMITIVE whose other sectors (Capotauro v2.0 closes (i)–(iii)) do connect to Standard Model phenomenology. F.1 itself is a substrate-physics derivation, not a Standard Model derivation.

---

## Limits of scope

The paper's scope is **honestly bounded** by the framework qualifiers in the title-page scope subtitle and §10 explicit disclaimers. Things F.1 *does not* claim to do:

**Does not derive thermodynamic-arrow emergence.** The substrate-locality structure of Theorem 7.1 *supports* a candidate substrate mechanism for the thermodynamic causal arrow; it does not derive entropy production, coarse-graining, or macroscopic irreversibility in the conventional physics sense. The emergence layer is future work.

**Does not derive Mechanism A.** The propagation-rate-asymmetry primitive + framework-local current construction are taken as Layer 3 framework axiom inputs (MA.1 + MA.2). Layer 4 axiomatic derivation from CPP primitive axioms A1–A11 is OPEN-FP-F1-2.

**Does not harden G1 to publication-grade.** Identity G1 (first-shell inner-product primitive) is imported from Patch 0541 §3.1 at sketch-document Layer 3 with derivation from the 600-cell first-shell-edge dihedral angle $\cos(36°) = \phi/2$ + unit-vertex normalisation. Publication-grade hardening (OPEN-FP-F1-3) is the RECOMMENDED first post-Phase-7 substantive physics Patch per ChatGPT R1–R6 convergent priority.

**Does not extend to $\mathcal{O}(\delta^2)$ or higher orders.** The closed-form result is at $\mathcal{O}(\delta^1)$ only; higher-order corrections (OPEN-FP-F1-1) require second-shell inner-product and edge-projection identities analogous to G1 + G2 + Theorem 5.1 that have not been worked out.

**Does not address non-vertex-aligned Reading C variants.** Edge-aligned ($D_3$ residual symmetry) and face-aligned ($D_2$ residual symmetry) Reading C are out of scope; extension is OPEN-FP-F1-5.

**Does not identify manifestation (v).** Sector-5 schema instantiation is OPEN-FP-F1-4; the question is research-direction-choosing.

**Does not independently harden the umbrella theorem.** Theorem 7.1 is at sketch-document Layer 3 because the three-step assembly itself has not been independently hardened with explicit hypothesis tracking + five-class exclusion enumeration of the umbrella-level inputs. Independent hardening is a candidate follow-up Patch (§7.4 note; not formal Open Problem to preserve in-body 5-OP commitment).

**Does not provide a condensed "core theorem" version.** ChatGPT R6 strategic suggestion: produce a shorter geometry/locality paper focused on Theorem 6.1 + Corollary 6.2 + Theorem 7.1 with minimal CPP interpretation — *"a shorter geometry/locality paper could travel further academically"* than the manifesto-scale flagship framing. This is registered as candidate follow-up Patch (F.1-condensed companion paper trajectory; depends on G1 hardening at OPEN-FP-F1-3 closure).

---

## Honest assessment

### What F.1 IS doing

- Proving that the net DI-bit current at any host vertex of the 600-cell substrate at vertex-aligned Reading C depends only on first-shell content at first order in the Mechanism A asymmetry parameter $\delta$ — the **substrate-locality structure**.
- Producing the closed-form first-order result $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$ with explicit structural-constant signature ($6/\phi^2$) emerging from icosahedral residual symmetry $H_3 = I_h$ + first-shell geometric identities.
- Establishing the publication-grade Layer 3 trio (Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2) supporting the sketch-document Layer 3 umbrella theorem (Theorem 7.1) via the assembly at §7.3.
- Closing OPEN-SD-CHIR-PRIMITIVE manifestation (iv) thermodynamic causal arrow at substrate-locality structure level — the temporal-sector analog of Capotauro v2.0's spatial-sector closure of manifestations (i)–(iii).
- Establishing the **F-line flagship trajectory methodology pattern** for future flagship papers (F.2, F.3, …): reviewer-pause cycle precondition + Layer 3 promotion + hardened-theorems trio + flagship paper assembly + multi-round reviewer cycle + v1.0 SHIP with anti-erasure discipline.
- Sharing the structural constant $-1/(2\phi)$ with Capotauro v2.0 §3 spatial-sector substrate-locality, demonstrating the chirality continuum architecture's geometric universality across spatial-temporal sectors.

### What F.1 is NOT doing

- Not deriving thermodynamic-arrow emergence (entropy production / coarse-graining / macroscopic irreversibility).
- Not deriving Mechanism A from CPP primitive axioms A1–A11 (this is OPEN-FP-F1-2).
- Not hardening G1 to publication-grade (this is OPEN-FP-F1-3).
- Not extending to higher-order corrections in $\delta$ (this is OPEN-FP-F1-1).
- Not addressing non-vertex-aligned Reading C variants (this is OPEN-FP-F1-5).
- Not identifying manifestation (v) of OPEN-SD-CHIR-PRIMITIVE (this is OPEN-FP-F1-4).
- Not independently hardening the umbrella theorem at publication-grade Layer 3 (this is a §7.4 candidate follow-up Patch).
- Not making predictions for directly measured Standard Model quantities (F.1 is a substrate-physics derivation, not a Standard Model phenomenology paper).
- Not claiming to be a finished publication — F.1 is a *flagship framework preprint*, with key follow-up work registered as Open Problems rather than completed.
- Not collapsing the Layer distinction or hiding the sketch-document Layer 3 status of the umbrella theorem — the anti-erasure discipline operationalised at three concrete points in §10 explicitly preserves the Layer-distinction structure end-to-end.

### Weakest link

**The weakest link is the G1 publication-grade hardening status.** G1 (first-shell inner-product primitive) is at sketch-document Layer 3 only; Theorems 5.1 + 5.2 are conditional on G1; Theorem 7.1 inherits the conditionality via the §5 trio. If G1 hardening fails (OPEN-FP-F1-3 closes negatively), Theorems 5.1 + 5.2 would drop from publication-grade Layer 3 conditional to sketch-document Layer 3 unconditional, and Theorem 7.1's conditionality would degrade correspondingly.

However, G1 hardening is **expected to succeed** based on the geometric structure: the first-shell inner-product matrix is fully determined by the icosahedral residual symmetry $H_3 = I_h$ + the 600-cell first-shell-edge dihedral angle $\cos(36°) = \phi/2$ + unit-vertex normalisation on $S^3$ — all three are standard regular-polytope facts (Coxeter reference). The hardening trajectory at OPEN-FP-F1-3 closure is methodologically analogous to the existing hardened-theorems trio (Patches 0550 + 0551 + 0552) and is registered as the RECOMMENDED first post-Phase-7 substantive physics Patch per ChatGPT R1–R6 convergent "single highest-value next action" priority.

**Secondary weakness: the umbrella theorem (Theorem 7.1) is at sketch-document Layer 3 only.** This is honestly preserved per the anti-erasure discipline. Independent publication-grade hardening of Theorem 7.1 is a candidate follow-up Patch (§7.4) but is not blocking on the v1.0 SHIP. The Layer-distinction discipline makes this weakness fully visible.

**Tertiary weakness: Mechanism A is taken as framework axiom rather than derived.** This is the Layer 4 question (OPEN-FP-F1-2) — long-term programme target. The framework-axiom strategy is methodologically standard for Layer 3 papers; the weakness is acknowledged and registered.

A skeptical reader who wishes to challenge the paper should push on G1 hardening (the weakest link); a skeptical reader who accepts G1 should push on the umbrella theorem's sketch-document Layer 3 status; a skeptical reader who accepts both should push on Mechanism A's Layer 4 derivability. The three pressures correspond to the three publication-grade hardening trajectories the paper itself identifies.

---

## Methodological observations

### The anti-erasure discipline as reviewer-pressure-driven methodological pattern

The anti-erasure discipline (named explicitly at §8.3 of the paper) emerged from the six-round ChatGPT reviewer cycle (Patches 0568–0569e). Rounds 1–3 saw recurring pressure to soften the Layer-distinction structure ("strong pre-v1.0 internal flagship draft" but "two decisive hardening steps pending" at R1; "Scenario A closure language still too strong" at R2; "umbrella theorem still weaker than supporting trio" at R3). The methodological response was *not* to soften the umbrella or collapse the Layer distinction. The response was to **make the Layer distinction more visible** at three concrete points in §10:

1. §10 paragraph 1 restates the Layer status of Theorem 7.1 explicitly.
2. §10 paragraph 3 disclaims thermodynamic-arrow emergence derivation explicitly.
3. §10 closing paragraph reaffirms 5-OP commitment as forward-trajectory anchor.

The discipline's name was crystallized at R3 ChatGPT's verbatim: *"the anti-erasure discipline is excellent."* The discipline is now a programme-level methodological pattern for future F-line flagship trajectories.

### Calibration discipline across the SHIP cycle

The six-round reviewer cycle sustained an explicit **calibration discipline**: no theorem statements modified, no proofs modified (Patch 0569a Edit C added clarification AFTER existing Lemma 6.3.1 proof, not within), no Open Problems modified, no `hardened_theorems/*.tex` source artifacts modified, no bibliography body modified. The 5-Open-Problem body §9 commitment was preserved end-to-end across all six ChatGPT rounds + Patches 0568–0570. OPEN-FP-F1-6 (prose-density tightening) was registered separately at Patch 0569e from R6 follow-up rather than inserted into the in-body §9 5-OP set — preserving the body-§9 commitment.

### The diagnostic resolution: TikZ-rendering processing artifact at R6 PDF-upload

Rounds 3–5 saw a **recurring-pattern phenomenon**: ChatGPT reviewer letters at R3, R4, R5 produced four identical recommendations (A + B + C + D) despite Patch 0569b having implemented all four. Patch 0569c documented the recurring pattern; Patch 0569d elevated two candidate hypotheses; Patch 0569e tested hypothesis (a) — TikZ-rendering processing artifact — by switching to PDF upload at Round 6. The R6 verdict (strongest-positive in the F.1 paper's reviewer-engagement history) confirmed hypothesis (a) correct.

The diagnostic resolution surfaces a programme-level reviewer-engagement convention candidate: **METH-PDF-UPLOAD-DEFAULT-REVIEWER** — going-forward protocol is to upload the freshly-compiled PDF (not `.tex` source) for ChatGPT reviewer engagement, especially for papers containing TikZ figures + bibliography environments + LaTeX content requiring compilation. The methodological lesson: reviewer-format-mediated processing artifacts can produce recurring-pattern false-positive recommendations; switching upload format can resolve such patterns without modifying paper content.

### The reviewer-pause cycle as flagship-trajectory precondition

F.1 trajectory is the **canonical worked example** for the reviewer-pause cycle precondition codified at `templates/paper_completion_checklist.md` "Reviewer-Pause Cycle Precondition for Flagship-Paper-Trajectory Work". The trajectory:

1. Phase 2 foundations work (Patches 0531–0537): close seven sub-questions at sketch Layer 2 with anti-priorities sustained throughout.
2. Reviewer-pause cycle (three-Patch sequence): Patch 0538 calibration response → Patch 0539 status upgrade.
3. Further calibration + Layer 3 promotion work (Patches 0540–0552): substantive Layer 2 → Layer 3 promotion + hardened-theorems trio production.
4. Flagship paper assembly (Patches 0554–0570): paper skeleton → 10-Patch body assembly → bibliography → final polish → six-round reviewer cycle → v1.0 SHIP.

The pattern is now corpus-established for future F-line flagship trajectories (F.2, F.3, …).

### Three programme-level conventions extended at this SHIP

Three new convention candidates surfaced for the Phase 7B methods catalogue audit Patch (Patch 0575-ish; methods catalogue audit Patch candidate count now 13):

- **METH-VARIANT-B-SCOPE-SUBTITLE** — Variant (b) `\date{}` line scope-subtitle pattern for v1.0 SHIP framing of Layer 3 + sketch-document content with explicit honesty-of-scope.
- **METH-PDF-UPLOAD-DEFAULT-REVIEWER** — PDF-upload-default protocol for ChatGPT reviewer engagement.
- **METH-GITIGNORE-FLAGSHIP-PDF-EXCEPTION** — `.gitignore` exception pattern `!flagship_papers/*/*.pdf` for v1.0+ SHIP PDFs.

Plus from the Phase 7A doc-suite production sub-arc:

- **METH-PHASE-7A-BUNDLED-AUDIT-CHANGELOG** (Patch 0572) — bundled audit + lowest-risk SHIP-time companion file in single Patch.
- **METH-PHASE-7A-DOCSUITE-PROD-DISCIPLINE** (Patch 0572a) — transcript-only Tier-file audit trail per sub-patch + end-of-sub-arc Vignette + §-entry rollup at Patch 0572g.

---

## Closing philosophical position

F.1 establishes that the CPP corpus can produce a flagship framework theorem paper with **rigorously honest scope** — proving what it can prove at the rigor it can prove it, preserving the Layer distinction + conditionality + open-problem inventory explicitly rather than collapsing them into a unified narrative. The substrate-locality structure of Theorem 7.1 is a meaningful structural result (closed-form first-order DI-bit current with universal coefficient $6/\phi^2$ emerging from icosahedral residual symmetry on the 600-cell), and the meaningful-result status does not require the umbrella theorem to be at publication-grade Layer 3 rigor. Sketch-document Layer 3 rigor with publication-grade Layer 3 trio inputs is a defensible Layer-rigor architecture for a flagship framework preprint that registers explicit hardening trajectory as Open Problems.

The chirality continuum architecture (Capotauro v2.0 + F.1) closes 4 of 5 manifestations of OPEN-SD-CHIR-PRIMITIVE. The remaining manifestation (v) — Sector-5 schema instantiation — is research-direction-choosing rather than derivation. The chirality continuum closure trajectory is approaching saturation of the umbrella OPEN problem at the v1.0 SHIP rigor.

The F.1 v1.0 SHIP is the **first F-line flagship v1.0 SHIP in CPP corpus history.** Future F-line flagship trajectories inherit the F.1 methodology pattern (reviewer-pause cycle precondition + hardened-theorems trio + sketch-document Layer 3 umbrella with publication-grade Layer 3 trio inputs + anti-erasure discipline + 5-OP commitment + scope-framing subtitle convention). The corpus-establishing role is itself a meaningful contribution beyond F.1's specific physics content.

---

*Philosophy file created Session 143 Patch 0572f (24 May 2026) as the seventh (final) SHIP-time companion documentation file in Phase 7A. Per `templates/documentation-suite.md` §5 + checklist §A A4 (Certainty level + Relationship to Standard Model + Falsifiability inventory + Paper-type declaration + Limits of scope + Honest assessment) + Capotauro reference implementation `philosophy-capotauro.md` extended structure (paper-type + Layer classification + certainty levels + falsifiability + SM relationship + limits of scope + methodological observations). Source priorities per docsuite.md §32: items 1 + 3 + 5 + 8 (sketches + Tier 3 development + founders_voice + external reviewer letters). This file is maintained continuously from this Patch forward; future paper-version increments trigger Layer classification updates (e.g., G1 hardening at OPEN-FP-F1-3 closure would promote Theorems 5.1 + 5.2 from conditional to unconditional + promote G1 from sketch-document Layer 3 to publication-grade Layer 3 + change the Weakest link entry accordingly).*
