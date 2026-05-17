# Capotauro Tier 4 Reasoning Document — Verbatim Reasoning Capture

**Paper**: `flagship_papers/capotauro/capotauro.tex` (v1.0 SHIPPED Session 122 Patch 0415)
**Purpose**: Capture verbatim Opus reasoning steps from key derivation sessions per the four-tier documentation discipline (Tier 4 = exact reasoning chain that was followed to reach a substantive result; not the polished paper version, the working version).
**Companion**: `development-capotauro.md` (per-session vignettes, Patch 0416B); `transcript-capotauro.md` (per-session transactions, Patch 0416C); `handover-capotauro.md` (Session 122 close §15 Step H, Patch 0416).

**Convention**: Reasoning is captured as Opus produced it, with light editorial framing for clarity. The reasoning is intentionally raw — preserving the actual thought trajectory that led to substantive results, including dead ends and reframings, is what makes Tier 4 useful for future continuation work and for understanding *why* the v1.0 result is what it is.

**Capotauro convention** (inherited from SF-4 v2.0+): The bulk of Tier 4 verbatim reasoning for the Capotauro closure trajectory lives canonically in the three working-sketch documents at `flagship_papers/capotauro/sketches/`, which grew monotonically across Sessions 86–121 and froze at v1.0 SHIP. This file holds (i) pointer sections to those working sketches with curated framing for what reasoning lives where; (ii) verbatim capture for methodologically critical decisions not already in the working sketches (the Session 120 SSB → primitive-feature framing reframe in particular); (iii) the Tier-4 discipline convention going forward.

---

## Section 1 — Sub-claim (c) closure trajectory (Sessions 86–103) — Pointer

The Tier 4 verbatim reasoning for the sub-claim (c) closure trajectory (Sessions 86–103, Patches 0376–0397) lives canonically in two working-sketch documents that grew monotonically across the closure campaign and froze at the v1.0 SHIP:

### Canonical Tier 4 source: `Capotauro_chi_phi_closure.md` (681 lines, parent sketch)

The parent sketch covers the foundational findings C-1 through C-8 and the early closure-trajectory framework decisions. Key sections in the sketch and the reasoning they preserve verbatim:

- **§1–§2 (closure trajectory framing)**: Three-sub-claim decomposition (a)/(b)/(c) with sub-claim (c) identified as v1.0 closure target; Picture A (foundational substrate-vacuum) + Picture B (transmission mechanism) + Picture C (group-theoretic skeleton) decomposition adopted as load-bearing role assignment.
- **§3 (Finding C-1)**: original $\chi \approx \phi^{-1}$ conjecture failed geometric consistency check against 600-cell structure — reasoning trajectory preserves the geometric-consistency-test derivation and the rejection.
- **§4 (Finding C-2)**: magnitude mismatch with empirical anchor — back-derivation from $\Delta p_{LR} \approx 0.04$ target showed inconsistency with $\chi = \phi^{-1}$.
- **§5 (Finding C-3, methodologically critical)**: OP-SM-4 archive's $\chi = \phi^{-2}$ derivation re-derived from scratch; one-step arithmetic error identified (lost factor $1/\phi$ in the ratio simplification); corrected value $\chi = \phi^{-3} \approx 0.236$ derived from edge-to-first-non-edge-distance ratio in the 600-cell. **Reasoning trajectory preserves the verbatim re-derivation including the arithmetic correction step.** This finding re-grounds the entire Capotauro mechanism.
- **§6 (Findings C-4 through C-6)**: structural alignment findings building on the corrected $\chi = \phi^{-3}$ baseline.
- **§7 (Finding C-7)**: Grok's $\Delta p_{LR} \approx 0.04$ target adopted as the empirical anchor; substrate-to-observable transmission factor $T = V/2 = 6$ identified at numerical-signpost level via $\|M\| = \chi/T$. Reasoning preserves the back-derivation from empirical anchor to $T = 6$ and the recognition that this matches the icosahedral cage's $V_\text{cage}/2$ structural identity.
- **§8 (Finding C-8)**: Picture A + Picture B + Picture C decomposition adopted as load-bearing role assignment for the closure trajectory. Reasoning preserves the role-assignment justification.

### Canonical Tier 4 source: `Capotauro_subclaim_c_wigner_eckart.md` (2146 lines, sub-claim (c) detailed)

The sub-claim (c) detailed sketch covers Sessions 88–101 closure trajectory with theorem-level rigor. Key sections and verbatim reasoning preserved:

- **§3–§4 (Theorem 8.1 + irrep classification)**: Sessions 88–91 closure of sub-sub-claim (c.1a) via Theorem 8.1 anti-diagonal parity structure; D_6 = S_3 × Z_2 stabilizer corrigendum at Session 89 (cell-swap ζ has det = -1 forcing ζ-ODD operators as chirality carriers); FI-C-3 extension at Session 91 with opposite-ζ-parity assignment for the two K3-doublet basis states (one ζ-EVEN + one ζ-ODD) resolving the Session 90 D_6 character theory obstruction. **Reasoning trajectory preserves the obstruction-recognition + resolution-path-design + extension-formalization sequence verbatim.**
- **§3.4 + Lemma 4.2 (unique $A_2$ generator)**: Session 95 correction substantively replacing the earlier general (a,b)-parameterization of σ_1-ODD operators on K3-amplitudes. The (a,b)-parameterization carried E-irrep contamination that produced incorrect K3-amplitude matrix elements; $\hat{C}_\chi$ in $B_2$ of $D_6$ requires the unique $A_2$ generator $T_{A_2}(b) = i \cdot b \cdot S$ specifically. **Reasoning preserves the (a,b)-parameterization → E-irrep-contamination-discovery → unique-$A_2$-generator-derivation sequence verbatim** including Lemma 4.2's spectral analysis showing eigenvalues $\{0, +b\sqrt{3}, -b\sqrt{3}\}$.
- **§5.3 (chirality-eigenvalue matching)**: Session 96 closure of $b = \chi/\sqrt{3}$ via Hermitian-operator spectral analysis. Setting non-zero K3-amplitude eigenvalues equal to substrate chirality eigenvalues $\pm\chi$ yields $b = \chi/\sqrt{3}$ and $\|M_{K3}\| = \chi$. **Reasoning preserves the spectral-matching argument verbatim** with derivation principle: Hermitian-operator spectral analysis rather than ad-hoc parameter assignment.
- **§5.5–§5.6 (cage-shell averaging)**: Session 97 closure of $\|M_\perp\| = d_E/V_\text{cage} = 2/12 = 1/6$ via FI-C-10 + Schur orthogonality on the icosahedral cage. The structural identity $V_\text{cage} = \|D_6\| = 12$ from the cage's $D_6$ stabilizer symmetry makes the averaging factor clean. **Reasoning preserves the Schur orthogonality derivation verbatim** + three plausibility arguments for FI-C-10 extension from FI-C-6 (substrate-isotropy, DI-bit propagation, FI-C-6 precedent).
- **§6 + Theorem 5.1 (THEO-CAP-1 formalization)**: Session 98 formalization of the Composite Capotauro Wigner-Eckart Theorem with eight-step proof + end-to-end numerical verification at machine precision ($10^{-17}$). **Reasoning preserves the eight-step derivation chain verbatim**: (i) extended basis construction; (ii) $\hat{C}_\chi$ irrep classification; (iii) Wigner-Eckart factorization; (iv) unique $A_2$ generator; (v) chirality-eigenvalue matching; (vi) cage-shell averaging; (vii) composite product; (viii) substrate substitution.
- **§7 ($\sin^2\theta_{13}$ scaling tension)**: Sessions 99–101 candidate-scaling enumeration of 22 candidates, only candidate γ ($\sin^2\theta_{13} = b \cdot m_\perp \approx 0.0227$) matches observation within 1σ. Wavefunction-level coupling hypothesis ruled out at Session 101 (Patch 0395) — explicit derivation showed quadratic-in-$\|M\|$ scaling off by factor $1/\chi^2 \approx 18$ from candidate-γ linear-scaling target. **Reasoning preserves the candidate-by-candidate enumeration + rejection-by-magnitude-or-scaling-form decisions verbatim** + the wavefunction-coupling-hypothesis verbatim derivation + re-scoping decision logic.
- **§22 (v1.0 closure narrative)**: Sessions 102–103 closure declaration + packaged trajectory summary as the canonical referent for THEO-CAP-1 registration. Lists four-condition methodological pattern for theorem-registry registration from flagship-paper-pending working sketch: rigorous proof + end-to-end numerical verification + primary empirical prediction validated + honest scope-limitation framing for re-scoped sub-problems.

### What's NOT in the working sketches (Tier 4 only available in commit messages)

Some reasoning lives in commit-message bodies rather than the sketches:

- **Patch 0382 (Session 88 Theorem 8.1 five-step proof)**: commit message body carries the five-step proof structure detail.
- **Patch 0389 (Session 95 unique $A_2$ generator)**: commit message body carries the σ_1-ODD operator parameterization correction with the inadmissibility-of-E-irrep-content reasoning.
- **Patch 0392 (Session 98 THEO-CAP-1 formalization)**: commit message body carries the end-to-end-numerical-verification methodology + machine-precision check details.

See `transcript-capotauro.md` for patch-index of each commit message; `git log` for full commit message content.

---

## Section 2 — Paper production phase (Sessions 104–122) — Brief framing

The paper production phase (Sessions 104–122, Patches 0398–0415) followed the standard v0.1 → v1.0 trajectory and does not require separate verbatim Tier 4 reasoning capture in this file. Reasoning lives in the commit messages of the v0.x → v1.0 patches, the review files at `flagship_papers/capotauro/reviews/`, and the v0.x → v1.0 .tex source itself.

**Exception — Patch 0413 Session 120 v0.9 polish + foundational framing reframe**: this is the methodologically critical decision of the entire Capotauro arc and warrants verbatim Tier 4 capture in this file. See Section 4 below.

---

## Section 3 — Sub-claim (b) Reading C mechanism candidate (Session 121) — Pointer

The Tier 4 verbatim reasoning for the Reading C geometric-chirality mechanism candidate (sub-claim (b) closure-trajectory opening, Session 121 Patch 0414) lives canonically in:

### Canonical Tier 4 source: `Capotauro_chiral_mechanism_candidate.md` (296 lines)

The Reading C sketch preserves verbatim:

- **§1–§2 (Reading C framing)**: The candidate physical mechanism for FI-C-9's primitive chirality magnitude — a primitive 4D direction $\hat{n}$ in the substrate's ambient 4D space produces direction-correlated edge-length variation in the 600-cell lattice at the $\phi^{-3}$ scale. The $H_4 \to I_4$ algebraic structure is the structural consequence of $\hat{n}$ being primitive (a foundational substrate feature) rather than the outcome of a dynamical event. **Reasoning preserves the primitive-vs-dynamical distinction verbatim** — load-bearing for the Session 120 reframe's primitive-feature framing.
- **§3 (chirality magnitude derivation from $\hat{n}$-perturbation)**: $\|\chi\| = \phi^{-3}$ **derived** rather than postulated, via the perturbative-distance-ratio constraint applied to the $\hat{n}$-perturbation in the 600-cell edge-length distribution. **Reasoning preserves the perturbative-distance-ratio derivation verbatim**.
- **§4 (new structural prediction — fractional chirality retention)**: Mass observables retain $O(\chi^2) \approx 0.6\%$; chirality observables retain full $\chi/6 \approx 4\%$; intermediate observables retain calculable fractions. **Reasoning preserves the observable-class-dependent retention derivation verbatim** including the SF-4 mass observable cross-check (retains $O(\chi^2)$ as expected from FI-C-6 mass-formula scaling).
- **§5 (five Layer 3 closure-trajectory questions)**: Q1 group-theoretic verification of $H_4$ stabilizer of $\hat{n} \cong I_4$ (1–3 sessions, first sub-step, triggers Capotauro v2.0+); Q3/Q4 perturbative-distance-ratio sharpening; Q5/Q6 cross-sector consistency with SF-2 W bracelet $D_6$ and SM-2 qDP/eDP asymmetry; sub-claim (a) cosmological-timing interaction. **Reasoning preserves the question-by-question scoping rationale verbatim.**

Tier-4 epistemic status: Layer 1 (physical intuition) + Layer 2 (structural mathematical sketching). NOT Layer 3 (formal theorem closure). Forward queue: Q1 closure (1–3 sessions) is the first sub-step toward Layer 3 closure; triggers Capotauro v2.0+ at minimum.

The Reading C sketch is the working development corresponding to v0.9 paper §9.2 "substrate chirality mechanism candidate derivation" and is registered at `Research_Frontier.md` OPEN-FI-C-9-FP-MECHANISM (Layer 3 closure trajectory estimated 10–20 sessions).

---

## Section 4 — Session 120 foundational framing reframe (verbatim Tier 4 capture)

**This section captures verbatim the reasoning trajectory that led to the Session 120 Patch 0413 reframe of §2 from "Substrate-Vacuum Broken-Symmetry Physics" to "Substrate-Vacuum Chirality as Primitive Feature."** The reframe is the methodologically critical decision of the entire Capotauro arc — it does not have a dedicated working-sketch home and warrants Tier 4 verbatim capture here.

### Context (Session 119 v0.8 reviewer convergence)

At Session 119 Patch 0412, three independent reviewers (ChatGPT round-3, CoPilot round-1, Grok round-1) reviewed v0.8 of the Capotauro paper. Cross-reviewer convergence on SHIP-readiness was achieved (*"mature conditional-theorem flagship paper"* / *"extremely close to v1.0 ship-ready"* / *"Ship as v1.0"*). However, ChatGPT v0.7 round-2 + v0.8 round-3 had both flagged a methodological concern about the §2 SSB framing — paraphrasing: "the SSB framing constitutes a methodological deviation from CPP's distinctive epistemic stance; CPP's commitment is that physical mechanisms underlie mathematical descriptions, but SSB is itself a mathematical description (a Lagrangian/effective-field-theory pattern) rather than a physical mechanism."

ChatGPT did not block the SHIP on this concern but flagged it for v0.9 polish-pass treatment.

### Reasoning trajectory (Session 120 opening)

The opening question at Session 120 was whether the SSB-framing concern was a cosmetic issue (replace some words in §2) or a substantive issue (the SSB framing is structurally inconsistent with CPP's distinctive methodological stance and should be replaced).

The first move was checking whether SSB and "primitive feature" framings are mathematically equivalent. Both produce the same chirality matrix element $\|M\| = \chi/6$ with $\chi = \phi^{-3}$ at v1.0 SHIP. Both produce the same falsifier set, the same THEO-CAP-1 derivation, the same eight-step proof, the same numerical predictions. They are observationally indistinguishable at the v1.0 paper level.

But mathematical equivalence does not entail methodological equivalence. The framings encode different ontological commitments:

- **SSB framing**: the substrate's ground state has a continuous symmetry that is dynamically broken by a vacuum expectation value (the order parameter). The chirality magnitude $\|\chi\|$ is the value of the order parameter at the broken-symmetry minimum. Implicit ontological commitment: there is a dynamical event (the symmetry breaking) that occurred at some moment and the substrate's current configuration is the dynamical-event aftermath.
- **Primitive-feature framing**: the substrate's chirality is a foundational feature coeval with CPs/GPs and the rules of their interaction. The chirality magnitude $\|\chi\|$ is part of the substrate's primitive specification, not the outcome of a dynamical event. Implicit ontological commitment: the chirality is constitutive of the substrate (like the existence of CPs themselves), not derived from a more primitive symmetric substrate via symmetry-breaking dynamics.

### Reasoning trajectory (Session 120 framing comparison)

The question is: which framing better fits CPP's methodological commitment that mathematical descriptions are not physical mechanisms?

The SSB framing imports a mathematical pattern from continuum effective-field-theory traditions (Lagrangian symmetry-breaking, vacuum expectation values, Goldstone modes). In those traditions, SSB is a mathematical description of a class of EFT phenomena. The physical interpretation is the EFT-author's choice: some interpret SSB as describing a real dynamical event in the early universe (the Higgs-mechanism story); others interpret it as a mathematical reorganization of the same physical content.

If the SSB framing in Capotauro is taken as a real dynamical event, then it implies a substrate ontology where chirality is NOT primitive — the chirality is the outcome of a prior symmetric substrate undergoing symmetry-breaking dynamics. But in CPP, the substrate's primitives are CPs/GPs and the rules of their interaction. There is no prior more-primitive-than-CPs substrate from which CPs emerge. The substrate IS the primitive level.

Therefore: a real-dynamical-event reading of SSB in Capotauro is structurally inconsistent with CPP's methodological commitment. The SSB framing must be either (i) interpreted as a mere mathematical reorganization (in which case it is decorative and does not add ontological content); (ii) replaced by a framing that explicitly treats chirality as primitive (in which case the SSB framing was misleading); (iii) preserved as a mathematical-equivalence alternative but not the primary framing.

Option (iii) is the methodologically honest choice. The reframe replaces SSB as the primary framing with the primitive-feature framing; preserves SSB as Remark 2.2 mathematical-equivalence alternative; honors the CPP methodological commitment while preserving the mathematical content for readers familiar with EFT traditions.

### Reasoning trajectory (Session 120 implementation)

The implementation reframe at Patch 0413:

1. §2 reframed from "Substrate-Vacuum Broken-Symmetry Physics" to "Substrate-Vacuum Chirality as Primitive Feature."
2. SSB language demoted to Remark 2.2 with explicit statement: "the mathematical structure here is equivalent to a Lagrangian-level spontaneous-symmetry-breaking pattern with order parameter $\chi$; we preserve that interpretation as a mathematically-equivalent alternative for readers familiar with continuum-EFT traditions but do not adopt it as the primary framing."
3. Sub-claim (b) renamed: "symmetry-breaking dynamics derivation" → "substrate chirality mechanism candidate derivation." This is a substantive rename — the old name implicitly committed to a dynamical-event ontology that the reframe rejects.
4. Sub-claim (a) clarified as universe-wide sign-selection event downstream of sub-claim (b) magnitude mechanism (separating the two sub-claims so that sub-claim (a)'s cosmological framing is independent of sub-claim (b)'s magnitude mechanism).
5. Residual broken-symmetry-language cleanup throughout abstract + plain-English summary + §5 + §6 + §8 + §9 + §13.

The reframe was not a cosmetic word-replacement. It is a methodological-philosophical decision about CPP's ontological commitments applied to the Capotauro mechanism specifically.

### Reasoning trajectory (decision summary at end of Session 120)

Decision: reframe §2 from SSB to primitive-feature framing; demote SSB to Remark 2.2 mathematical-equivalence alternative; rename sub-claim (b).

Methodological pattern noted: this is the kind of decision that v0.x development can defer (because the mathematical content is unchanged) but v1.0 SHIP cannot defer (because the SHIP commits to a primary framing for external readers). The convergence on SHIP-readiness at v0.8 forced the reframe decision at v0.9; postponing to v2.0+ would have been intellectually dishonest since the SHIP-readiness verdict was based on a framing the paper would not commit to.

This decision pattern — methodologically critical framings forced by SHIP-readiness convergence — is a programme-level methodological insight. Worth registering in `operating_system.md` at a future opportunity.

---

## Section 5 — Session 123 post-SHIP doc-suite catch-up (Patches 0416 + 0416A–D) — Pointer

The reasoning for the Session 123 post-SHIP doc-suite catch-up arc lives in:

- **`handover-capotauro.md`** (Patch 0416, §15 Step H paste-ready format): retroactive handover artifact for Session 122 close; §15 Step E per-registry audit reasoning surfacing three drift items.
- **`session_logs/2026-05-16_session_log.md`** (Patch 0416, Template B retrospective synthesis variant): meta-record of session 122 close + session 123 retroactive handover work + drift findings + Patch 0417+ forward queue + methodological observation that §15 Step E per-registry audit caught what v1.0 SHIP commit's bundled framing missed.
- **Commit messages of Patches 0416, 0416A, 0416B, 0416C, 0416D** (this patch): each commit message body carries the reasoning for the patch's specific scope, including Dr. Abshier Session 123 parallelization decision (letter-suffix docs-arc 0416A+ vs integer physics-arc 0417+) + discipline-tightening-after-precedent principle for OPEN-WORKFLOW-DOCS-CATCHUP deferral to post-Section-A completion.

Two methodological observations from Session 123 worth Tier-4 capture in this file:

### Methodological observation 1: §15 Step E per-registry audit catches what bundled framing misses

The Patch 0415 v1.0 SHIP commit message wrote *"All registers UNCHANGED at programme level"* in its summary framing. Re-reading the commit carefully: it was honest about Research_Frontier.md and theorem-registry.md updates per-registry, but its bundled summary framing was silent on predictions.md, master_glossary.md, and problem_histories/. The §15 Step E audit at Patch 0416 handover construction caught three drift items the bundled framing missed: (i) predictions.md PRED-O entry for $\Delta p_{LR}$ missing; (ii) master_glossary.md Capotauro terms section missing; (iii) PH-OPEN-SM-4.md missing.

The §15 anti-pattern warning explicitly names this failure mode: *"bundling them as 'registry updates done' without per-registry verification is the failure mode that registry drift accumulates from."* The protocol working today validated the anti-pattern warning in real-time.

Recommendation: future v1.0 SHIP patches should walk the per-registry audit table as part of commit-message construction, not rely on the §15 handover audit to surface drift after-the-fact.

### Methodological observation 2: Discipline-tightening-after-precedent principle

Dr. Abshier's Session 123 decision to defer OPEN-WORKFLOW-DOCS-CATCHUP registration to post-Section-A-completion (Patch 0416M) rather than immediately register at Patch 0417 captures a methodological principle worth Tier 4 capture: **doing one full example end-to-end before codifying programme-wide discipline makes the discipline credible**.

Codifying-aspirationally-before-executing weakens the discipline because the programme has not demonstrated capability to execute the discipline. Doing one full execution before codifying produces a concrete reference implementation that subsequent discipline-tightening can point to. The Capotauro doc-suite at Patches 0416A–M is the reference implementation; OPEN-WORKFLOW-DOCS-CATCHUP at Patch 0416M is the codification.

Pattern noted: this is the same pattern as the per-paper changelog file convention at Session 115 (Patch 0408 reference implementation in Capotauro doc-suite → Session 116 Patch 0409 programme-wide codification). Paper-specific innovation that becomes programme-wide rule via codification patch. The pattern repeats; recognizing it as a pattern is worth Tier 4 capture.

---

## Tier 4 discipline convention going forward (Capotauro v2.0+ and successor papers)

For Capotauro v2.0+ closure campaigns (sub-claim (b) Reading C Q1+ and sub-claim (a) Capotauro nucleation event work) + future flagship papers in the corpus: the SF-4 v2.0+ convention applies. Tier 4 reasoning for closure campaigns lives in dedicated working-sketch documents in the paper's `sketches/` subdirectory, growing monotonically across the campaign and freezing at SHIP. The four-tier documentation suite's `reasoning-*.md` file holds:

1. **Pointer sections** for closure campaigns where Tier 4 reasoning lives canonically in working sketches.
2. **Verbatim Tier 4 capture** for methodologically critical decisions that do not have a dedicated working-sketch home (the Capotauro precedent: Session 120 SSB → primitive-feature framing reframe captured in Section 4 above).
3. **Methodological-observation capture** for programme-level insights surfaced during the paper's development that warrant durable Tier 4 record (the Capotauro precedent: Session 123 methodological observations 1 + 2 in Section 5 above).

This avoids duplication, keeps reasoning capture co-located with the campaign it documents, and ensures methodologically-critical-but-undocumented-elsewhere decisions are durably captured in the reasoning file.

The convention is the same as SF-4 v2.0+ codified at `flagship_papers/neutrinos/documentation_suite/reasoning-SF-4.md` pointer-section §X (Tier 4 discipline convention going forward). The convention should be added to `templates/documentation-suite.md` template at the next opportunity (currently registered as deferred to OPEN-WORKFLOW-DOCS-CATCHUP Patch 0416M scope).

---

*Maintainer: Dr. Thomas Lee Abshier ND, Hyperphysics Institute. Last updated: 16 May 2026 (Session 123 Patch 0416D creation).*
