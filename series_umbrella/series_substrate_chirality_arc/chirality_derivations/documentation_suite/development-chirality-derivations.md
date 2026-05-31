# Development — Chirality Derivations

Session vignettes for the chirality-derivations arc (Sessions 148–151, Patches 0632–0670), append-only.
The verbatim per-patch reasoning is in `reasoning/<patch>.md`; these are the curated
paragraph-form vignettes (Tier 3) pointing at it.

---

## Patch 0632 — THEO-CHIR-AUDIT-1 registered (the catalogue)

The 27-entry chirality entry-point enumeration was rebuilt after a working-window overflow and
registered as the new CHIR sector's founding theorem. It classifies every point where chirality
enters CPP (spatial/temporal/CP-asymmetric senses) as primitive / emergent / unregistered, with
the central finding that spatial chirality reduces to the single primitive `n̂`. The audit named
the three downstream targets this folder then discharged: E20 (conditional), E21 (emergent-P,
magnitude), E19 (the deepest unregistered entry).

## Patches 0633–0635 — the AUDIT-1 review cycle

A multi-AI review (Copilot referee-grade, Grok recompute+contribute, ChatGPT meta-review) was
run and integrated. No falsifier was produced; the v1.0→v1.1 calibration sharpened labels only
(graded emergent (E)/(P); E20 → unregistered-conditional; ZBW as exclusion X5). The cycle closed
3/3 on v1.1, and the audit `.tex` was frozen. Two reviewer seeds (Grok's E19 and E21 sketches)
were logged as starting structures, *not* closures — ChatGPT's calibration that a plausibility
sketch is not a derivation set the discipline for the derivations that followed.

## Patch 0636 — E20 resolved (THEO-CHIR-PCD-ORIENTATION-1)

The first downstream theorem. The key move was scoping it as a primitive-*count* question:
`ω_PCD = σ_cycle·n̂` is a product of two already-registered primitives, so no third primitive,
Scenario B refuted, E20 emergent. The §3 precondition (σ_cycle attributed to A1+A4, not the F.1
sketch's pre-canonical "A5") was cleared. Honest cap: emergent (provisional), inheriting the F.1
viability ceiling; the primitive count is robust to the three open F.1 commitments.

## Patches 0637–0638 — E21 / 1d-α resolved (THEO-CHIR-CHI-1)

The scope sketch (0637) found that `χ = φ⁻³` is a foundational input (FI-C-9) whose *value* has
a partial derivation (Finding C-3), corrected the audit's imprecise "CONT-1.3 addresses E21"
note (CONT-1.3 is inheritance, not derivation), and decomposed the gap into 1d-α (ratio
selection) + 1d-β (dynamics). The distance-spectrum exploration (0638) then *succeeded*: a
locality criterion (the symmetric bias of the two nearest 600-cell shells) uniquely selects
`φ⁻³`, excluding `1/√5` and `5−2√5` as non-local. 1d-α closed at Layer 2/2.5; the exponent
question ("why −3") retired. (A leftover patch file swept into the commit by `git add -A` was
caught and removed before delivery — the lesson logged.)

## Patches 0639–0640 — E19 resolved (THEO-CHIR-CAP-1)

The deepest unregistered entry. The scope sketch (0639) led with a no-false-reduction discipline
(E19 is consumed by three shipped theorems) and found the organizing insight: the capture
handedness, as consumed, is the SD-CHIR `ζ`-generator, an *involution* (registered geometry)
that carries no sign by itself — so capture handedness = `ζ × σ_capture`, parallel to E20. The
artifact (0640) ran the decisive 1c-β test by reading the SD-CHIR sign bookkeeping: the
matrix-element sign is carried by the edge-perturbation `ε(ê·n̂)`, whose sign is the `n̂` sign =
the FI-C-9 enantiomorph. **Verdict R1**: `σ_capture = sign(n̂) = FI-C-9`, no independent primitive,
E19 emergent. R3 (new primitive) refuted; R2 (merge with E20's temporal sign) left as a
hypothesis. A first verify-script version found the perturbation field zero on first-shell↔first-
shell edges — recognized as the local-`I_h`-preservation theorem (tangency), not a bug, and the
check moved to the bias-carrying first→second-shell edges.

## Patch 0641 — this documentation-suite consolidation

At the three-derivations milestone, the per-patch verbatim reasoning + scripts (captured
throughout per the reasoning-capture protocol) were consolidated into this `documentation_suite/`
plus the folder README. No physics changed; this is the synthesis layer over the canonical
Tier-4 fragments.

## Patches 0643–0657 (Sessions 148 tail–149) — the unified-sign merge + the primitive/emergent-status capstone

After THEO-CHIR-CAP-1 (E19) the arc turned to the remaining sign question and then to the status crux. **OPEN-CHIR-MERGE** opened (0643, `sketches/theo_chir_merge_1_scope.md`): is the temporal cycle sign σ_cycle the same object as the spatial sign(n̂)? **THEO-CHIR-MERGE-1** (0644, `theo_chir_merge_1.tex` + `code/verify_merge_current_sign.py`) partially resolved it — the primitive-count capstone. The shared dependency was scoped as **OPEN-FP-F1-2** (0646, the Layer-4 axiomatic derivation of Mechanism A from A1–A11; cross-sector, the gate behind both MERGE-β and OPEN-CHIR-2a). **THEO-CHIR-MERGE-2** (0647, `theo_chir_merge_2.tex` + `code/verify_merge_2_parity_decomposition.py`) advanced MERGE-β from M3 → M1-χ (chirality-count half resolved) and delivered OPEN-FP-F1-2 sub-target L4-D; its review cycle (0648–0651) closed **3/3 → v1.2**, verdict M1-χ conditional on MERGE-α (`review/reviews-CHIR-MERGE-2.md`).

The status crux: **OPEN-CHIR-1d-β** scoped (0652, `sketches/chir_open_1d_beta_fi_c_9_emergence_scoping.md`) — the FI-C-9 emergence question, decomposed i–v with the capacity-vs-value distinction. **THEO-CHIR-STATUS-1** (0653, `theo_chir_status_1.tex` + `code/verify_status_1_verdict_partition.py`) formalized the verdict space {V1,V2,V3} (proved exhaustive) and placed current rigor at **V3** (FI-C-9 = the one currently-identified irreducible chirality primitive); the OPEN-CHIR-1d-β ID was reserved for the V1 upgrade. **THEO-CHIR-STATUS-2** (0654, `theo_chir_status_2.tex` + `code/verify_status_2_breaking_chain.py`) gave the chiral-vacuum breaking chain H₄ → H₄⁺ (index-2 ℤ₂; order parameter sign(n̂) = FI-C-9) and the axiom-level V2-exclusion that **pins the emergence upgrade to exactly V1** (emergent mechanism, contingent sign). The STATUS-1/2 review cycle (0655–0656) closed **3/3 → v1.1** (`review/reviews-CHIR-STATUS.md`; ChatGPT's read: STATUS-2's V2-exclusion is what makes the pair a falsifiable constraint, not relabeling). Verdict unchanged — **V3, upgrade pinned to V1.** (Session-close handovers 0657 + 0657a; no physics.)

## Patches 0658–0667 (Session 150) — the temporal capstone (TARROW-1), the dispatch protocol, and the bridge's B-i

**THEO-CHIR-TARROW-1** (0658, `theo_chir_tarrow_1.tex` + `code/verify_tarrow_1_arrow_status.py`) carried the STATUS-1 partition onto the temporal axis: sign(δ) is **W3**, upgrade pinned to **W1**. New content — the T-even-geometry lemma (the substrate geometry is purely T-even, so there is no T-odd geometric quantity and no finite-group breaking chain — the disanalogy with parity) and the CPT unification (the spatial V2-reopener and temporal W2-reopener are, by CPT, the same SM CP/T object). Review cycle (0659, 0661) closed **3/3 → v1.1** (`review/reviews-CHIR-TARROW.md`). **The full status capstone is now closed on both halves** — spatial V3 (STATUS-1/2) + temporal W3 (TARROW-1), unified by one CPT-linked reopener.

Workflow infrastructure (0660): the canonical **"initiate review protocol"** command codified — NEW `templates/review_dispatch_protocol.md` + OS §1/§5, the review-side analog of the §15 handover, turning a finished review package into paste-ready reviewer-addressed dispatch text.

The verdict-moving frontier: the **CHIR↔electroweak bridge** scoped (0662, `sketches/chir_ew_bridge_scoping.md`) — unifying OPEN-CHIR-1d-β-v ∪ OPEN-CHIR-3 (co-owned with OPEN-SM-4), decomposition B-i/B-ii/B-iii/B-iv, the ℤ₂-match lead, and the NEW conjecture **CONJ-CHIR-1** (substrate chiral-vacuum transition = Capotauro activation = EWSB; if true → chirality fully emergent V2/W2 via the SM). **B-i DELIVERED** as **THEO-CHIR-BRIDGE-1** (0663, `theo_chir_bridge_1.tex` + `code/verify_bridge_1_z2_match.py`): a Layer-2.5 structural correspondence — NOT a derivation — identifying the OPEN-SM-4 activation ℤ₂ = the STATUS-2 quotient ℤ₂ = one det-coset object (kinematic, conditional on premise P2) plus the P/T-face dictionary; CONJ-CHIR-1's kinematic half discharged, dynamical half isolated as B-iii. Review cycle (0664–0665; first live use of the new dispatch command + its delivery-mode fallback) closed **3/3 → v1.1** (`review/reviews-CHIR-BRIDGE.md`). **No verdict move — V3/W3 stand.** (Session-close handover 0666; kickoff-line addition 0667.)

## Patches 0668–0670 (Session 151) — the bridge's reachable faces completed (B-iii + B-ii scoped)

Session 150 had closed B-i (the ℤ₂-match + P/T-face dictionary, THEO-CHIR-BRIDGE-1, review-hardened
3/3) and isolated the bridge's dynamical residue as B-iii. Session 151 took up that residue and the
remaining tractable magnitude work, producing two scope sketches and one hygiene fix — no theorem, no
review cycle, and no verdict move.

**B-iii (Patch 0668) — the capacity engine.** The move was to make the capacity question ("does the
det-coset ℤ₂ actually break / does a chiral vacuum form?") structurally precise without charging the
deferred dynamics. Replacing the discrete order parameter `sign(n̂)` by its continuous precursor η (the
det-coset amplitude, on which the ℤ₂ acts as η ↦ −η) turns the qualitative question into a well-posed
one about the effective potential V(η). Because the substrate dynamics are ℤ₂-symmetric (STATUS-2's two
degenerate enantiomorph vacua), V is forced even — V = V₀ + μ²η² + λη⁴ + … with no odd term, the absence
being a consequence of STATUS-2's own partial-1d-β-iii result (no axiom-level pseudoscalar exists except
FI-C-9 = η). The vacuum structure then collapses to a single sign: capacity ⟺ μ² < 0 (double-well, ℤ₂
breaks, V3→V1) vs μ² > 0 (symmetric, no chiral vacuum). The second sub-question — is the break EWSB? —
localizes as the identity of the substrate μ² with the electroweak Higgs μ² (CONJ-CHIR-1's dynamical
content), independent of the capacity sign (the independence is BRIDGE-1 falsifier B2 made explicit).
The ℤ₂-even form is Layer-2.5-reachable now; the sign of μ² is fixed only by the DSL effective action
behind F.1 §14.17 and was deliberately not touched — the verify script exercises both signs as free
inputs and asserts it fixes neither. This is the B-iii analog of STATUS-2 (the breaking chain) and
BRIDGE-1 (the ℤ₂-match): a deep question reduced to one coefficient's sign.

**B-ii (Patch 0669) — the magnitude anchors, and a "tension" that wasn't one.** B-ii decomposes by
depth: the P-face anchor Δp_LR = χ/6 = φ⁻³/6 ≈ 0.0394 is already load-bearing and shipped (CAP-1), while
the T-face anchor δ_CP ≈ 193–195° is a signpost only, its derivation-from-χ being the same §14.17-gated
deep engine as B-iii. The reachable core was the long-flagged χ "φ⁻¹-vs-φ⁻³" reconciliation that
BRIDGE-1 carried as falsifier B4. Tracing every live source showed there is no physics tension: φ⁻³ is
the unambiguous magnitude (FI-C-9, CHI-1, Capotauro v1.0/v2.0), and φ⁻¹ is two other things — a
registered dead end (the pre-Session-86 conjecture, geometrically excluded because φ⁻¹ is the
edge-length scale; C-3 corrected a lost-1/φ arithmetic error that had produced φ⁻²) and the first-shell
distance from which CHI-1 *builds* χ via the symmetric bias (1−φ⁻¹)/(1+φ⁻¹) = φ⁻³. The dead conjecture's
whole error was conflating the input distance with the output bias. Falsifier B4 was reclassified
(resolved as documentation; retained only as a forward hook on sub-claim (b), should a future
first-principles |χ| derivation ever return φ⁻¹/φ⁻² as the magnitude). The root cause — a stale
placeholder in OPEN-SM-4's one-line statement — was corrected in a deliberately separate cross-sector
patch (0670), keeping the CHIR-arc scoping work independent of a registry edit in the SM sector. The
review-closed BRIDGE-1 theorem was left untouched.

With these, the bridge's three reachable faces are mapped (B-i closed, B-ii and B-iii scoped), and the
only verdict-moving work left lives behind the §14.17 viability ceiling.
