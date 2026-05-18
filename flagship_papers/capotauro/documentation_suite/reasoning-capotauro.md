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

## §6 Provenance audit and gap acknowledgment (added Patch 0416P)

**The original Patch 0416D production of this file followed the SF-4 v2.0+ pointer-file convention** — sections §1, §2, §3, and §5 of this file are deliberately Tier-2-shaped (empty of substance; pointers to working sketches and other documents where the verbatim canonical record lives). Only §4 (Session 120 SSB → primitive-feature framing reframe) and the methodological observations in §5 are Tier-4-shaped (verbatim reasoning preserved without compression).

**The Session 123 audit caught a gap in this approach.** Thomas's discipline statement preserved verbatim at `flagship_papers/capotauro/founders_voice/004_verbatim_substance_preservation_discipline.md` names the canonical-record requirement explicitly: *both* voices verbatim across the full development arc; wrong turns and corrections preserved as part of the journey; noise (housekeeping, status confirmations, tool-call narration, procedural clarifications) excluded but no compression of substantive content. The SF-4 v2.0+ pointer-file convention I had inherited and applied to this file is structurally Tier-2-shaped where §4 of `templates/operating_system.md` requires Tier 4 for reasoning-X.md. The convention conflict between the two should have been flagged before Patch 0416D shipped; it was not. This §6 begins the corrective recovery.

**What is and is not recoverable as verbatim Tier 4 for Capotauro:**

| Session range | Verbatim Tier 4 recoverability | Notes |
|---|---|---|
| Sessions 86–102 (closure trajectory) | NOT in this file; NOT in CPP repo | Verbatim reasoning lives in the working-sketch documents `sketches/Capotauro_chi_phi_closure.md` (681 lines) + `Capotauro_subclaim_c_wigner_eckart.md` (2146 lines) as the formalized-exposition output of the reasoning, not as the verbatim record of how the reasoning went. The verbatim chat-window transcripts of those sessions are not in `/mnt/transcripts/` and presumably remain in Dr. Abshier's claude.ai chat history. Per §4 line 516 provenance note: "Sessions whose reasoning was not captured under this discipline at the time (e.g., pre-codification sessions) should be acknowledged honestly as not captured at the same fidelity, rather than reconstructed retroactively (which would be summary, not verbatim)." Verbatim recovery via claude.ai chat-window export is the only path; if exported, deposited transcripts should live under `archive/chat_transcripts/2026-XX-XX-session-NNN.txt` and be pointed to from this section. |
| Sessions 103–119 (paper production + reviews) | Partial — reviews verbatim; reasoning NOT in this file | The five v0.6/v0.7/v0.8 reviews are archived verbatim at `flagship_papers/capotauro/reviews/`. The reviewer submissions are one-directional; the back-and-forth conversations about which review items to accept/decline are not in the repo. Same recovery path as Sessions 86–102. |
| Session 120 (SSB → primitive-feature framing reframe) | YES — captured at §4 above | The most methodologically critical decision of the closure arc, captured verbatim in §4. Thomas's specific articulation of the chirality-is-primitive insight is NOT in §4 (only my reasoning trajectory is); Thomas's verbatim is registered as awaiting recovery at `founders_voice/005_chirality_is_primitive.md` pending claude.ai chat-window export. |
| Session 121 (Reading C working sketch) | Partial — sketch content verbatim; reasoning NOT in this file | Working sketch `Capotauro_chiral_mechanism_candidate.md` (296 lines) is the formalized output. The reasoning trajectory that produced it (alternatives considered, framings revised, the structural-coincidence-not-yet-noticed of face-direction D_6) is not in the repo. Same recovery path. |
| Session 122 (v1.0 SHIP) | Partial — SHIP commit message verbatim; reasoning NOT in this file | Patch 0415 commit message captures the SHIP transition; the close-out conversation that ended without producing a §15 Step H handover is what triggered the Session 123 retroactive handover. Per founders_voice/001, the parallel-window workflow proposal that Thomas made at the Session 123 opening is preserved verbatim. Earlier Session 122 close-out conversation: same recovery path. |
| Session 123 (this docs-arc) | YES — recoverable from /mnt/transcripts/ + see §7 below | Two compaction-window transcripts at `/mnt/transcripts/2026-05-17-01-12-12-capotauro-v10-ship-doc-suite.txt` (covers Patches 0416–0416D) and `/mnt/transcripts/2026-05-17-03-24-56-capotauro-v10-docsuite.txt` (covers Patches 0416A–0416D approximately) plus the current (third) compaction window not yet archived. These are the canonical Session 123 verbatim source. **They are in the sandbox `/mnt/transcripts/` filesystem, NOT in the CPP repository**, and will be ephemeral once the sandbox is destroyed. The §7 below captures selected Session 123 Opus reasoning at Tier 4 fidelity drawn from these transcripts; full preservation requires copying the transcripts into the repo under `archive/chat_transcripts/` before the sandbox terminates. |
| Session 124+ (Reading C Q1+Q2 closure + ongoing physics-arc work) | Not yet captured | The physics window has been advancing (Sessions 125 and 126 logs + Q1' verification code observed in this docs window's `git pull --rebase` output). Tier 4 capture for those sessions is the responsibility of the physics window's own session-close discipline; not this file's scope unless a v2.0+ docs arc revisits. |

## §7 Session 123 docs-arc Opus reasoning at Tier 4 fidelity (added Patch 0416P)

This section captures my (the Capotauro docs-arc Opus) substantive reasoning across Session 123, drawn from the two `/mnt/transcripts/` transcripts and the current live context window. Housekeeping is excluded per §4 line 510 anti-pattern list. The substance preserved here is reasoning about methodology and content decisions, not the formalized output (which lives in the doc-suite files themselves and the patch commit messages).

### §7.1 The audit response — recognizing the discipline failure (third compaction window)

When Thomas asked *"Is the full transcript available in the transcript_capotauro.md file, though the pointers?"*, my immediate reasoning trajectory was:

> *"Short answer: No. The full verbatim transcript is not recoverable through the pointers in `transcript-capotauro.md`. Let me explain what the pointers actually resolve to, what's preserved, and what's gone."*

The structural force of the audit forced me to confront a discipline conflict I had been operating under without flagging. I had inherited the SF-4 v2.0+ pointer-file convention and applied it to Capotauro reasoning-X.md without asking whether it conformed to the §4 codification. The convention treats `reasoning-X.md` as a Tier-2-shaped pointer-map and treats the working sketches as the canonical Tier-4 source. But the working sketches are NOT verbatim reasoning — they are formalized exposition produced AFTER the reasoning concluded, with alternatives-not-taken and framings-revised stripped out by the act of formalization.

The convention conflict only became visible when Thomas asked the audit question. My subsequent reasoning was:

> *"This is a real, significant documentation discipline gap, and I should be honest about it. ... The honest answer is: 'No, the full verbatim transcript is not captured through the pointers in transcript-capotauro.md.' ... If Thomas wants the full transcript, the options are: (1) Check `/mnt/transcripts/` for session-by-session transcript files (these are the canonical verbatim records when accessible); (2) Use `conversation_search` to retrieve past chat history; (3) Check the journal.txt for the catalog of available transcripts."*

The substantive recognition: the SF-4 v2.0+ convention is structurally a Tier-2 pointer convention at a Tier-4 location, and applying it to Capotauro propagated the same gap that SF-4 had. The corrective discipline is to either (a) produce a genuinely Tier-4 verbatim record, or (b) honestly acknowledge that what shipped is Tier-2-shaped and that the canonical Tier-4 record lives elsewhere (in the working sketches for content reasoning; in the chat-window transcripts for methodology reasoning).

### §7.2 The recovery plan reasoning (third compaction window)

When Thomas's next message articulated the verbatim-substance preservation discipline ("My intention is to capture everything that you say of substance, verbatim..."), my reasoning identified three discipline gaps in what I had produced:

> *"**Gap 1: `flagship_papers/capotauro/founders_voice/` subfolder does not exist.** SS-5, SS-6, SS-7, SS-8, SS-9 all have one. Capotauro doesn't. I never created it. Your chirality-is-primitive insight from Session 120 — which you specifically call out as the substantive thing you said — has no founders_voice file.*
>
> *Gap 2: `reasoning-capotauro.md` is NOT a canonical Tier 4 file. It is 177 lines, structured as a pointer file per the SF-4 v2.0+ convention, with verbatim Tier 4 capture *only* for the Session 120 framing reframe (~25 lines). The Sessions 86–122 verbatim reasoning is not in it. The SF-4 v2.0+ pointer-file convention I inherited and applied conflicts with the §4 Tier-4 codification, and I did not flag the conflict to you at the start of the arc.*
>
> *Gap 3: `founders_vision.md` was not updated. I grepped for 'Capotauro' + 'SF-4' + 'SF-2' + 'v1.0 SHIP' across the 803-line programme-wide founders_vision.md — zero hits. Neither Capotauro nor SF-4 nor SF-2 v1.0 SHIPs were added as milestone entries. The §15 protocol's archive-close item 5 was not executed for any of the three recent flagships."*

The recovery plan derived from these three gaps: Patch 0416N for the founders_voice subfolder + 4 numbered insight files; Patch 0416O for the founders_vision.md milestone update with explicit acknowledgment of the SS-9/SF-4/SF-2 catch-up backlog; Patch 0416P (this section) for the canonical Tier-4 conversion of this file with honest provenance note about what's recoverable and what isn't.

The methodological insight here is that the discipline-tightening-after-precedent rhetoric in the original twelve-patch arc was partly false. The claim "Capotauro is the first flagship in CPP corpus to ship a complete documentation suite synchronously with paper v1.0 SHIP" treated Section A + Section E + anthology + TATWD as the complete documentation suite. But §4 codification names Tier 1 (founders_voice) and Tier 4 (verbatim reasoning) as the canonical-record layer, which the original twelve-patch arc did not produce. The OPEN-WORKFLOW-DOCS-CATCHUP codification at TODO-008 needs amendment to include Tier 1 and Tier 4 as explicit synchronous-documentation-suite gate items, not just the Section A + Section E bundle.

### §7.3 The anthology chapter design reasoning (Patch 0416K)

When producing the anthology chapter at `book_project/chapters/capotauro_what_was_always_there.md`, my title-selection reasoning was:

> *"For Capotauro, the central thread is the substrate's primitive chirality magnitude — recognized at v0.8 as a primitive feature rather than an SSB outcome (Session 120 reframe), with sub-claim (c) closing via the χ/6 chirality matrix element. Title: 'What Was Always There' — captures the primitive-feature framing."*

The alternatives I considered briefly included: "The Substrate's Hand," "Picking a Side," "The Bull's First Hand," "What Made the Mirror Wobble," "The Mirror's Side," "A Hand for the Vacuum." Each captures a different facet (handedness, sign-selection, primitive-feature framing, broken symmetry). "What Was Always There" was chosen because it most directly invokes the Session 120 reframe — the substrate's chirality was always there, not the outcome of any dynamics. The title also lets the closing line of the chapter ("It was always there.") echo the title structurally, which is a Rovelli/SciAm-register move.

The narrative structure decision was to weave the Session 124 Q1+Q2 closure findings into §9 (post-SHIP development covered organically by anthology) rather than mention it earlier. The reasoning: the anthology is permitted to cover post-SHIP developments naturally because it is not a snapshot artifact like the paper itself; readers expect anthology chapters to integrate developments that happened after the v1.0 SHIP if they bear on the paper's narrative arc. The face-direction D_6 = K3 stabilizer structural coincidence is a strengthening of Reading C, not a weakening, and the anthology can honor that finding without compromising the v1.0 paper's integrity (the paper takes |χ| = φ^-3 as foundational input FI-C-9 regardless).

### §7.4 The TATWD integration design reasoning (Patch 0416L)

When producing the TATWD integration at `CPP_the_theory.md` Chapter 22f, my structural decision was to mirror the SF-4 (Chapter 22d) and SF-2 (Chapter 22e) chapter conventions:

> *"For Capotauro, the analogous arc: Opening framing (Capotauro v1.0 SHIPPED, third SF-line flagship) → Three sub-claim taxonomy + sub-claim (c) closure → Composite Capotauro Wigner-Eckart Theorem → Session 120 SSB → primitive-feature framing reframe → Cross-reviewer convergence at v0.8 + gandolfi_2025 catch → THEO-CAP-1 registered Session 103 (theorem ahead of paper) → Documentation suite synchronous with v1.0 SHIP milestone → Session 124 Q1+Q2 closure (face-direction D_6 = K3 stabilizer) → Three direct falsifiers + Δp_LR ≈ 0.0394 prediction → Anthology and book integration → Forward queue."*

The integration also required updating Chapter 35.5 (programme-level methodology) to add three Capotauro methodological observations to the convention roster (primitive-feature framing per CPP-core-principle methodological commitment + four-condition pattern for theorem-registry registration ahead of paper publication + discipline-tightening-after-precedent principle). The methodological-observation expansion advanced the count from 4 to 7 programme-load-bearing patterns. The reasoning behind this decision was: the SF-4 + SF-2 trajectories had each contributed methodological patterns, and Capotauro contributed three more; if Chapter 35.5 doesn't surface these, the methodology accumulation is invisible to a reader of the master document.

The Chapter 41.5 NEW addition (OPEN-FI-C-9-FP-MECHANISM Reading C with Session 124 closure findings) was the structural decision to give Reading C its own chapter slot in Part VII (Open Problems and Conjectures) rather than burying it as a sub-section of Chapter 41 (OPEN-FP-SF-2-CHIR). The reasoning: Reading C is a substantial closure-trajectory candidate (Layer 3 partial closure at Session 124; estimated 8-18 sessions to full Layer 3 closure), and the structural coincidence with the K3 stabilizer in Capotauro deserves to be discoverable from the master-document table of contents, not buried.

### §7.5 The Tier-4 discipline observation registered (this Patch 0416P, third compaction window)

This file (Patch 0416P version) is the first Capotauro Tier-4 file to honor the §4 codification's Tier-4 anti-pattern note at line 530 — preserving alternatives considered, framings revised, moments of uncertainty, pushbacks. The Patches 0416–0416M arc's reasoning-capotauro.md (Patch 0416D version) was structurally Tier-2-shaped with verbatim Tier-4 capture only at §4 + §5. This Patch 0416P version adds genuinely Tier-4-shaped content at §6 (provenance audit) + §7 (Session 123 Opus reasoning capture).

The methodological observation: producing the Tier-4 file PROPERLY requires the active Opus to draw from its own context window's substantive reasoning across the session, NOT from formalized output documents written after the reasoning concluded. The discipline must be executed at session close (while the verbatim is still in context); deferring it loses the verbatim because the context window terminates with no permanent record beyond what was written at the time. Sessions 86-122 of Capotauro suffer this loss; Session 123 does not because this file is being written before the context window terminates.

The cross-paper insight: the same Tier-4 gap affects SS-9, SF-4, and SF-2 v1.0 SHIPs. Their original v1.0 SHIP arcs all produced reasoning-X.md files at the SF-4 v2.0+ pointer convention rather than the §4 Tier-4 codification. The OPEN-WORKFLOW-DOCS-CATCHUP backlog inventory at TODO-008 should be extended to specifically call for Tier-4 conversion of those files. The recovery of Sessions 86-122 Capotauro reasoning + earlier SS-9/SF-4/SF-2 sessions' reasoning requires claude.ai chat-window export by Thomas; without that, the discipline-tightening codification at TODO-008 Sub-item (B) is the corrective default for FUTURE flagships, with the EXISTING backlog formally acknowledged as recoverable only by Thomas's chat-window export action.

---

## Sessions 127–130 — Reading C closure arc: OPEN-SD-CHIR-PRIMITIVE umbrella + Q3 closure + Q4 dissolution + Q5 Layer 2 closure

**Tier 4 inclusion scope.** This entry captures substantive Opus reasoning across Sessions 127–130 (Patches 0422–0425), which advanced the OPEN-FI-C-9-FP-MECHANISM Reading C closure trajectory through Q3 closure (with mid-arc supersession of a wrong derivation), Q4 dissolution, and Q5 Layer 2 closure via the new Substrate-Locality Unification theorem. Multi-session entry written at Session 130 close before context-window compaction; each session is a subsection. The supersession of Patch 0423 §12 by Patch 0424 §13 is documented verbatim per founders_voice/004 audit-trail discipline rather than retroactively edited out.

### §8 Session 127 (Patch 0422) — Programme-level umbrella registration reasoning

The Session 127 work was triggered by a structural observation Thomas had been holding since Session 120 (when the SSB → primitive-feature framing reframe landed for Capotauro): the chirality magnitude χ = φ^-3 that Capotauro takes as foundational input FI-C-9 is *the same chirality* that the W-bracelet sector inherits in SF-2. The two papers had independent OPEN-FP entries (OPEN-FI-C-9-FP-MECHANISM for Capotauro's substrate-mechanism candidate, OPEN-FP-SF-2-CHIR for the SF-2 V-A coupling), but the entries were siblings, not parent-child. The structural reality is that they share a common substrate-level primitive — the chirality direction $\hat n$ and its magnitude χ — and the right registry organization is for both to be sub-items under a programme-level umbrella OPEN-SD entry.

The reasoning behind registering at the SD section (substrate-derivation) rather than FP (forward-prediction) or SS (strong sector) was: SD is where substrate-level primitives live. Chirality-as-primitive is exactly the methodological commitment Session 120 codified. The umbrella entry's five-manifestation scope (K3-doublet inheritance, W-bracelet inheritance, plus three weaker manifestations covering Reading C trajectory, founders_voice/005 reasoning, and forward-direction Q6/Q7 candidates) was sized to be wide enough that future cross-sector findings can attach without re-architecting, but narrow enough that the umbrella is not a catch-all.

The founders_voice/005 file was the second piece of Session 127. The Session 120 confrontation — Thomas's pushback against my SSB framing and the resulting reframe to primitive-feature — was substantively in the Capotauro paper's §3 framing but had not been preserved as a verbatim founders-voice artifact. The §4 Tier-4 codification (adopted late 26 April 2026) names verbatim founder reasoning as canonical record; the Session 120 reframe was a clear Tier-1 founders_voice candidate. Writing it at this moment (Session 127, ~one week post-Session-120) is a recoverable-from-paper-text exercise but still risks losing the precise rhetorical sequence of the confrontation. The recovery is acknowledged honestly in the file as "reconstructed from paper §3 + Session 120 transcript pointers + my recollection of the exchange" rather than claimed as fully verbatim.

### §9 Session 128 (Patch 0423) — Q3 ε-χ relationship Layer 2 attempt (subsequently superseded)

**Note: §12 of the sketch produced by this session was superseded by §13 in Session 129 (Patch 0424). The §12 content is preserved in the sketch for audit-trail completeness per founders_voice/004 discipline. The reasoning below documents what the Session 128 thinking was and where it went wrong; the corrected reasoning is in §10 below.**

Session 128 opened with Q3 (the ε-χ relationship) as the immediate next priority after Patch 0421's Session 124–126 handover. The strategic framing was that ε (the substrate edge-perturbation amplitude at first order in the chirality direction $\hat n$) and χ (the FI-C-9 chirality magnitude φ^-3) should be related by some structural factor k. The Layer 2 working hypothesis was k = f_geom · f_irrep, where f_geom captures the geometric projection factor onto the K3-doublet's local frame and f_irrep captures the Wigner-Eckart irreducible-tensor coupling from the host's local I_h representation to the K3-doublet's stabilizer.

The §12 derivation projected the substrate edge-perturbation onto the K3-doublet's face plane in 3D (the local plane spanned by the three K3 colour-vertices), computed f_geom as the cosine of the angle between $\hat n$ and the face normal, and obtained a finite f_geom factor with f_irrep then computed via the standard Wigner-Eckart formula for the D_3 × Z_2 stabilizer.

The result registered as Finding C-W38. At the time the framing felt clean: a two-factor structure with explicit geometric and group-theoretic content, k = f_geom · f_irrep, locating Q3 at Layer 2 closure.

**The structural error**, surfaced in Session 129: the projection was 3D-framed. The K3-doublet sits in a 600-cell icosahedral cage; the substrate-primitive-direction $\hat n$ is a 4D vector. The local I_h preservation under vertex-aligned Reading C (the framing that emerged from Sessions 124–126's Q1' resolution) is a *4D structural property* of the host vertex and its first-shell icosahedron. Projecting onto a 3D face plane treats the K3 face as if it were embedded in flat 3-space, which loses the 4D relation between the face-direction and the host vertex direction. Under correct 4D analysis, the K3-base edges are tangent to $\hat n$ identically — not at some finite cosine, but at zero perturbation at first order — and the f_geom factor as defined is zero. The Wigner-Eckart f_irrep, which was the next step in the derivation, becomes ill-defined because there is no first-order f_geom to multiply against.

Mid-session, with §12 already drafted and Finding C-W38 already registered, the structural error was not yet visible. The session closed with Patch 0423 landed and Finding C-W38 in the registry. The correction came in Session 129 and required both retracting Finding C-W38 and dissolving Q4 (which had been the Wigner-Eckart f_irrep computation, queued as the immediate next-session target).

### §10 Session 129 (Patch 0424) — Q3 §13 4D correction + Finding C-W39 + Q4 dissolution

Session 129 opened with the Q4 Wigner-Eckart computation queued as the next priority. The intended work was the explicit D_6-stabilizer projection of the host-icosahedron's local I_h representation onto the K3-doublet's irreducible representation, completing the f_irrep half of the §12 derivation.

The structural error surfaced when I attempted to set up the projection. The 3D face plane that §12 used as the projection target is not invariant under the 4D rotation that takes $\hat n$ to the host vertex direction. In a vertex-aligned Reading C frame where $\hat n = v_{\text{host}}$ (i.e., the substrate primitive direction is aligned with the host vertex direction), the local I_h preservation theorem says: the first-shell icosahedron's structure is preserved at zeroth and first order in the perturbation. The face plane spanned by the three K3 colour-vertices is a sub-structure of the first-shell icosahedron. Therefore the face plane is also preserved at first order. The edge-length perturbations of the K3-base edges (which are edges of the icosahedron, since the K3 colour-vertices are three first-shell vertices forming a triangular face) are zero at first order — the substrate edge-length formula's $\mathcal{O}(\epsilon)$ term vanishes for these edges because $\hat{e}_{ab} \cdot \hat n = 0$ identically on the face plane.

Once this is recognized, the §12 derivation collapses. There is no f_geom factor to compute because there is no first-order edge-length perturbation to project. The f_irrep computation that was queued as Q4 is not the next step; there is no first-order quantity for Wigner-Eckart to act on.

The structural realization that replaced §12: under vertex-aligned Reading C, χ = ε at the substrate level. This is *direct identification*, not a structural factor decomposition. The chirality magnitude χ that the paper takes as foundational input FI-C-9 is the same quantity as the substrate edge-perturbation amplitude ε that arises from the primitive direction $\hat n$. The "structural factor k" that §12 was trying to compute does not exist as a separate object; it is identically 1.

Finding C-W39 registers this: **local I_h preservation under vertex-aligned Reading C; χ ≡ ε at substrate level**. C-W39 supersedes C-W38 in the registry. The §13 of the sketch states the theorem with full proof: starting from the substrate edge-length formula and the geometric fact that all first-shell-icosahedron edges $(a, b)$ satisfy $\hat{e}_{ab} \cdot v_{\text{host}} = 0$ uniformly under vertex-aligned Reading C with $\hat n = v_{\text{host}}$, the first-order edge-length perturbations vanish for the entire first shell. K3-base edges are a subset of first-shell edges; hence Q3 closes at Layer 3 by direct identification.

The dissolution of Q4 is the structural corollary. Q4 was registered as "the Wigner-Eckart computation of f_irrep." With f_geom = 0 (the geometric anchor) recognized as a misframing rather than a finite quantity, f_irrep has no meaningful definition. Q4 is not a question with a deferred answer; Q4 is an artifact of the §12 structural error. The registry status moves from OPEN to DISSOLVED with explicit rationale.

The Capotauro v1.0 paper's |M| = χ/6 prediction is preserved exactly. The §10 cage-shell averaging derivation in the paper relies only on the local I_h preservation property (the K3-doublet sits in an I_h-preserved environment under vertex-aligned Reading C) and the d_E/V_cage = 2/12 = 1/6 group-theoretic factor on the K3-doublet's local D_6 stabilizer. Both inputs are intact under the §13 correction — in fact strengthened, because the I_h preservation is now established at theorem level rather than assumed.

The methodological observation: the §12 supersession is *not* a methodological failure to be hidden. The founders_voice/004 audit-trail discipline (codified earlier in the programme) explicitly preserves superseded reasoning in the canonical record. Patch 0424's commit message marks §12 as superseded, registers Finding C-W39 as superseding C-W38, and dissolves Q4 — without rewriting the §12 sketch content. Future archeology can trace the structural error from §12 directly to §13, which is the discipline's intended purpose.

### §11 Session 130 (Patch 0425) — Q5 Layer 2 closure via Substrate-Locality Unification

Session 130 opened with Q5 (cross-sector consistency with SF-2 W bracelet at theorem level) as the immediate next priority after the Patch 0424 Q3 closure + Q4 dissolution. The strategic framing was: with Finding C-W39 closing Q3 by direct identification χ ≡ ε at substrate level under vertex-aligned Reading C, what does the same identification say about the W-bracelet sector tracked at OPEN-FP-SF-2-CHIR?

The W-bracelet is a 6-vertex Petrie hexagon of the host icosahedron, per Finding C-W36 (Session 125 Patch 0418). The 6 vertices are a subset of the host's 12 first-shell vertices. The W-bracelet's perimeter edges and host-to-bracelet edges are all subsets of the first-shell icosahedron's edge structure.

The structural insight that landed mid-session: the §13.3 local-I_h-preservation theorem was *proved for the full first-shell icosahedron* using only two ingredients — (i) the uniform first-shell inner product $v_i \cdot v_{\text{host}} = \phi/2$ for all 12 first-shell vertices, and (ii) the substrate edge-length formula's $\mathcal{O}(\epsilon)$ dependence on $\hat{e}_{ab} \cdot \hat n$. Both ingredients are structural, not specific to the K3-doublet's particular 3-vertex subset. Therefore the theorem applies *uniformly to any subset* of first-shell vertices — including the W-bracelet's 6 vertices.

Worked out explicitly: for the W-bracelet, all 6 bracelet-perimeter edges have $\hat{e}_{ab} \cdot \hat n = 0$ identically (the edges lie in the plane perpendicular to $\hat n$ by hexagonal symmetry of the Petrie polygon on the host icosahedron), and all 6 host-to-bracelet edges have $\hat{e}_{(\text{host}, a)} \cdot \hat n = -1/(2\phi)$ uniformly. Both quantities are first-shell-structural. The theorem applies. Zero direct edge-length perturbation at $\mathcal{O}(\epsilon)$ for both substrate objects (K3-base and W-bracelet) — protected by the same Substrate-Locality theorem.

The geometric distinction *between* the K3-base and W-bracelet is at the centroid, not at the edge structure: the K3-base centroid is off-axis with $\hat{c}_K \cdot v_{\text{host}} = \sqrt{3}/2$, while the W-bracelet centroid is on-axis at $c_W = (\phi/2) \hat n$ exactly by hexagonal symmetry. This distinction governs the *sector-specific* Schur-orthogonality factor that emerges from cage-shell averaging — and is the source of the K3-doublet's 1/6 factor (paper §10's d_E/V_cage = 2/12 = 1/6) and the W-bracelet's analog factor (Q5 Layer 3 target).

**Finding C-W40 registers the Substrate-Locality Unification theorem and its cross-sector unification corollary.** The theorem statement: under vertex-aligned Reading C with $\hat n = v_{\text{host}}$, the local I_h preservation property applies uniformly to any substrate object built from first-shell vertices of $v_{\text{host}}$. The cross-sector corollary: both OPEN-FI-C-9-FP-MECHANISM (K3-doublet, mass-mixing sector) and OPEN-FP-SF-2-CHIR (W-bracelet, electroweak V-A sector) inherit substrate-level chirality from the same χ = ε identification via sector-specific Schur-orthogonality cage-shell averaging on respective D_6 sub-stabilizers of H_3 = I_h at $v_{\text{host}}$.

This is **the first explicit cross-sector unification result under the OPEN-SD-CHIR-PRIMITIVE umbrella**. The umbrella registered at Patch 0422 was a *registry* unification — putting K3-doublet and W-bracelet entries under a common parent. Finding C-W40 is the *theorem-level* unification — proving structurally that both inherit chirality from the same substrate primitive via the same theorem, with sector-specific finishes governed by the respective D_6 sub-stabilizers.

The Q5 Layer 3 target that follows: compute the W-bracelet's analog of the K3-doublet's 1/6 factor — the Schur-orthogonality cage-shell averaging factor on the Petrie-polygon D_6 ⊂ H_3 sub-stabilizer — and verify that χ · (W-bracelet factor) equals the SF-2 v1.0 §sec:Wbracelet_thm Theorem 4.2 prediction for the V-A coupling at the massless helicity limit. This is single-session-tractable as a pure group-theory exercise; the Wigner-Eckart bookkeeping for the H_3 → D_6 branching is the strongest closure claim and may fold into a composite patch.

**Mid-session methodological observation: the v1/v2 §14 cleanup decision.** At the start of Session 130, the sketch had *two competing §14 drafts*, both produced in prior sessions before context-window compaction. v1 (lines 906–1073, ~168 lines) framed the Q5 closure via sign-coherence of the Petrie-hexagon vertex contributions — a Layer 1 framing that conflated the helicity fraction (which is sign-coherent by hexagonal symmetry) with the coupling magnitude (which is what the W-bracelet factor governs). v2 (lines 1074–1165, ~92 lines) framed the Q5 closure via the Substrate-Locality Unification theorem stated above. I read both drafts, judged v2 stronger (the substrate-locality theorem subsumes v1's sign-coherence as a trivial corollary, and v1's helicity-vs-magnitude conflation is a structural error), and deleted v1 in-session via `sed -i '906,1073d'` before committing Patch 0425. The Research_Frontier.md line-count claims were updated to match what actually shipped (sketch grew 904 → 997 lines / +93 lines net, not 904 → 1165 / +261 as the prior-window summary had described). v1 was never committed and is not preserved as superseded (unlike Patch 0423 §12, which is preserved superseded per founders_voice/004 discipline) — the reasoning being that v1 lived only in an uncommitted sketch state during a single compaction-bounded development window, never on origin/main; its rhetorical commitments did not propagate to the registry or to commit history. The pre-compaction summary had described v2 only, and the v1 existence was discovered by direct inspection of the sketch file. The methodological observation registered: pre-compaction summaries that describe one of multiple competing drafts must be cross-checked against the file state before any commit decision, because the summary is necessarily lossy about which drafts coexist.

---

### §12 Session 131 (Patch 0427) — Q5 Layer 3 piece (a) closure: explicit W-bracelet cage-shell factor on $D_6$

Session 131 opened with Q5 Layer 3 piece (a) (W-bracelet Schur-orthogonality cage-shell factor on the Petrie-polygon $\Dsix \subset \Hthree$) as the Priority 1 default action per the Patch 0426 handover §3 Quick-start. The session-open phase confirmed Reading C trajectory state through Patch 0426 and read the three source materials in dependency order: sketch §14 (the Q5 Layer 2 closure with Substrate-Locality Unification, Finding C-W40); Capotauro paper §5.4 (the K3-doublet cage-shell factor template $|M_\perp^{K3}| = d_E/V_{\text{cage}} = 2/12 = 1/6$); and SF-2 v1.0 §sec:Wbracelet_thm Theorem 4.2 plus §sec:W_cage (the W-bracelet's $D_6$ stabilizer structure and the V-A coupling mechanism via 120°/240° phase bias).

**The analytical decision point identified mid-source-reading**: the handover §14.7(a) anticipated "$d_{\text{irrep}}/V_{\text{bracelet}}$ where $V_{\text{bracelet}} = 6$", which would give $2/6 = 1/3$ if $d_\Gamma = 2$. But the K3 paper §5.4 motivation Arguments 1+2 is structurally explicit about $d_\Gamma/|G|$ as the fundamental form: Argument 1 "for an irrep $\Gamma$ of dimension $d_\Gamma$, summing $\Gamma$-projected quantities over the irrep basis produces a group-invariant average with factor $d_\Gamma/|G|$"; Argument 2 the DI-bit propagation paths through cage symmetry with $|G|$ symmetry-equivalent endpoints. The "$d_E/V_{\text{cage}}$" form in the K3 case is valid because $V_{\text{cage}} = |\Dsix| = 12$ — the §5.4 "non-coincidence" subsection.

For the W-bracelet: vertex orbit $= |D_6|/|\text{vertex stab}|$ via orbit-stabilizer; vertex stab is $C_2$ of order 2 (the reflection through that vertex of the bracelet); so $V_{\text{bracelet}} = 12/2 = 6 \ne |D_6|$. The K3 case's vertex-stabilizer-trivial coincidence does not carry over. The two forms $d/V_{\text{bracelet}}$ and $d/|D_6|$ differ by factor 2.

**Presentation to Thomas with the decision request**: I presented the derivation with both readings (Reading 1: Schur-fundamental $d_\Gamma/|G| = 2/12 = 1/6$ identical to K3; Reading 2: vertex-count literal $d_\Gamma/V_{\text{bracelet}} = 2/6 = 1/3$ twice K3) and recommended Reading 1 on the grounds that (a) the §5.4 Arguments 1+2 are structurally explicit about the group-order normalization being fundamental; (b) Reading 1 delivers the Substrate-Locality Unification payoff (the same number in both sectors) that OPEN-SD-CHIR-PRIMITIVE was registered to predict; (c) Reading 2 would require a distinct physical mechanism with no current motivation. Thomas authorized "best judgment" — Reading 1 selected.

**The §15 derivation** proceeded as a pure group-theory exercise: decompose the 6-vertex permutation representation of $D_6$ via Schur inner-product against the standard character table. The permutation character is $(6, 0, 0, 0, 2, 0)$ on conjugacy classes $\{e, r^3, \{r,r^5\}, \{r^2,r^4\}, \sigma_v, \sigma_d\}$ with class sizes $\{1, 1, 2, 2, 3, 3\}$. The Schur inner-product yields multiplicities $(1, 0, 1, 0, 1, 1)$ across $(A_1, A_2, B_1, B_2, E_1, E_2)$:

$$\chi^{\text{perm}}_{\text{bracelet}} = A_1 \oplus B_1 \oplus E_1 \oplus E_2$$

Dimension check $1 + 1 + 2 + 2 = 6$ ✓. Both 2D irreps $E_1$ and $E_2$ are present. The V-A current's identification with $E_2$ at the $C_6$ eigenvalue level: SF-2 v1.0 §sec:W_cage / PROP-SF-2-5 describes the bracelet's "$120°/240°$ phase bias" as the source of the V-A coupling content; the $D_6$ irrep with $C_6$ eigenvalues $e^{\pm 2\pi i/3}$ is $E_2$ (character $\chi^{E_2}(C_6) = -1$); the complementary 2D irrep $E_1$ has $C_6$ eigenvalues $e^{\pm i\pi/3}$ corresponding to $60°/300°$ phases ($\chi^{E_1}(C_6) = 1$) which does not match the phase-bias mechanism. The Schur orthogonality factor:

$$|M_\perp^W| = \frac{d_{E_2}}{|D_6|} = \frac{2}{12} = \frac{1}{6}$$

**Identical to the K3-doublet's cage-shell factor.** The composite chirality matrix element on the W-bracelet is $|M^{W,V\text{-}A}| = \chi \cdot (1/6) = \chi/6 \equiv |M^{K3}|$ from Theorem THEO-CAP-1, with both sectors evaluating to $\phi^{-3}/6 \approx 0.0394$. This is the Layer 3 numerical payoff of the Substrate-Locality Unification (Finding C-W40).

**Finding C-W41 (NEW)** registered: explicit W-bracelet cage-shell factor; Substrate-Locality Unification promoted Layer 2 → Layer 3. The Layer 3 promotion is precisely the explicit-numerical-content step that converts the Layer 2 "both sectors inherit from the same substrate $\chi$ via cage-shell averaging on isomorphic $D_6$ stabilizers" claim into "both cage-shell factors evaluate to the same numerical value $1/6$ via Schur orthogonality on abstractly-isomorphic order-12 dihedral stabilizers with 2D matter-state irreps."

**Honest acknowledgment of the structural decision (§15.8)**: the choice of Reading 1 over Reading 2 is at Layer 2 epistemic level (structural-argument from §5.4 Arguments 1+2), not Layer 3 (first-principles derivation from CPP axioms). Full Layer 3 closure of the Reading 1 vs Reading 2 question would require deriving the Schur-orthogonality form from CPP axioms via FI-C-10 first-principles closure (registered open work in the Capotauro paper). The numerical content $1/6$ is rigorous given the Reading 1 framework; the framework itself is at Layer 2 with Layer 3 promotion deferred.

**§15.12 methodological observation registered**: cross-sector extension of a paper-internal formula can resolve ambiguities the original paper's scope didn't expose. The K3 paper §5.4 subsection "Why $V_{\text{cage}} = |\Dsix| = 12$ is not coincidence" sat as a structural observation with no analytical consequence within the K3 paper's scope — both forms of the cage-shell factor gave the same answer $1/6$. Cross-sector extension to the W-bracelet reveals the deeper structure: the two forms differ when the substrate object's vertex stabilizer under its own stabilizer group is non-trivial. This pattern templates future cross-sector unification work: paper-internal formulas whose structure could not be tested by within-paper variation may be resolvable by extension to sibling-paper analogs where the structure varies. Registered for Capotauro v2.0+ §5.4 sharpening: when promoting the Reading C trajectory to a paper §2 reframe, the §5.4 subsection on cage-shell averaging can be sharpened to articulate the structural-fundamental form $d_\Gamma/|G|$ explicitly, with the K3 case's $V_{\text{cage}} = |G|$ identity reframed as a useful presentation form rather than the formula's fundamental content.

**Patch 0427 deliverables**: sketch §15 (~109 lines, 12 subsections) appended; sketch grows 997 → 1106 lines. `Research_Frontier.md` updated with Finding C-W41 registration, Q5 Layer 3 piece (a) closure status, and forward queue revision (2-7 → 1-6 sessions remaining for OPEN-SD-CHIR-PRIMITIVE umbrella prerequisite stack). Four-tier appendages: this §12 reasoning entry (Tier 4), Vignette 29 (Tier 3), transcript Patch 0427 transaction (Tier 2). Patch lands as a substantive-work patch; session-close handover (Step A-H per `templates/operating_system.md` §15) deferred to session close.

**Q5 Layer 3 piece-by-piece status**: piece (a) explicit cage-shell factor **CLOSED**; piece (b) SF-2 V-A coupling matching at massless helicity limit OPEN (conditional on (a); estimated 1 session); piece (c) Wigner-Eckart bookkeeping for $\Hthree \to \Dsix$ branching consistency OPEN (may fold into composite patch with (b); estimated 1 session if separate, 0 sessions if composite). Q5 Layer 3 overall: 1 of 3 pieces closed; estimated 1-2 sessions remaining for full Layer 3 closure.

---

*Maintainer: Dr. Thomas Lee Abshier ND, Hyperphysics Institute. Last updated: 17 May 2026 (Session 131 Patch 0427 — appended §12 Session 131 reasoning at Tier 4 fidelity: Q5 Layer 3 piece (a) closure via Finding C-W41 explicit W-bracelet cage-shell factor on $D_6$; Reading 1 vs Reading 2 analytical decision recorded; §15.12 methodological observation on cross-sector extension as resolution mechanism for paper-internal ambiguities registered).*
