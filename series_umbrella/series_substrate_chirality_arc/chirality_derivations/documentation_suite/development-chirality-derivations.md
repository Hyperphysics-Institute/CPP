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

---

# Session 228 — Patches 0936–0974 (13 Sep 2026)

*Tier-3 vignettes, written at Patch 0977 (14 Sep 2026), one window after the work. Step C of the
§15 close was deferred at 0974 for context budget and filed as TODO-0974a-CAPTURE.*

**Placement decision (the choice TODO-0974a-CAPTURE asked a later window to make and record).**
Session 228's work splits cleanly by subject, not by session, so it is filed by subject rather than
into one cross-paper file. The rate-law derivations (L4-A/B/C/E), the `δ = −ε` pinning and the
non-reciprocity result are F.1's and are filed in
`dynamical_substrate_law/documentation_suite/development-dynamical-substrate-law.md`. The arc-level
work — C-W46, piece 1, the CONV panels, the CAPACITY-1 and TARROW-2 re-bases, 1d-β — is filed here.
The SM-2 and Capotauro corrigenda were produced cross-lane by this lane and are recorded here in
summary, with their substance in `series_standard_model/corrigenda/SM-2_composition_corrigendum.md`
and the 0937 review file. No cross-paper vignette file is created; a session is not a subject.

## Patches 0936–0937 — C-W46's flags closed; the qDP chirality operator is the charge sign

The session opened on a cross-lane question from the DM lane and closed three flags (F1–F3) left on
Finding C-W46. The result is a genuine correction, not a confirmation: **the antipodal-pair
configuration space carries no pseudoscalar operator at all.** `A_u(I_h)` restricts to `A₁u(D₅d)`,
which has no support on the pair, so a purely geometric pseudoscalar has vanishing matrix element
there. What is actually nonzero is the **charge sign**: `Ĉ^qDP = χ·(1/6)·ŝ`, geometrically trivial,
sitting in `A₁g(D₅d) ⊗ C-odd` under the extended group `D₅d × Z₂^C`. The pseudoscalar content is
carried by the coefficient `χ`, not by a `D₅d` irrep. The previously printed `A₂u` assignment had
described a polar axial coordinate.

The consequence for the DM lane was decisive and was the reason the question came: reading E1 is
case (c), `S = +qCP`, **unconditional on a reading** rather than contingent on one. The inversion
referent was also pinned — `v ↦ −v` is the local point group's `p ↦ φn̂ − p`, while `n̂ ↦ −n̂` is
the substrate mirror and not a group element at all, a distinction the prose had been eliding.
Verified at `code/0937_d5d_extended_group_bookkeeping.py`, 14/14.

## Patch 0938 — the owed items filed, because a review file is not a queue

The founder asked whether 0936/0937's corrections and flags were recorded anywhere retrievable and
actionable. They were in the review file, in `frontier_sectors/CHIR.md`'s resolved entry, and in a
dated `theorem-registry.md` bullet — three records, no queue. `TODO-0937-CHIR` was registered in
`todolist.md`. This was the third arc in a row to lose owed items the same way (after TODO-3930-EU
and TODO-3938-DM), which is what produced the next patch.

## Patch 0939 — the deferral gate (D-9)

The rule was generalised and made mechanical: a deferral is a write, in the same commit, gated.
Any patch whose text puts something aside files it in `todolist.md` in the same `git am`, checked by
`code/deferral_gate.py` before `git format-patch`. The insight behind the rule is that the moment of
a deferral is the **patch**, not the session close — the operating system had already said a session
identifying a deferral adds it to the queue, but that rule was audited at a session close that,
under D-8, rarely fires.

## Patches 0942–0948 — SM-2's charge defect, found, extended, and closed

Writing the Capotauro corrigendum surfaced something larger: **SM-2's as-written cage list
contradicts SM-2's own charge section.** A central `−qCP` with a neutral extra DP screens to −2/3
where −1/3 is required. The founder ruled the fix extends, and a full audit
(`0943_sm2_charge_audit.py`, 6/6) showed the defect is exactly the down-type family — down, strange
and bottom — and nothing else among the fermions; up-type at +2/3, charged leptons at −1 and the
neutrals are all correct as written. The gap is −1 for all three despite cage occupancies of
N_k = 2.5, 30 and 3000, so it is cage-independent and the repair generalises exactly. Mass fits are
label-level; no published number moves.

The same audit then found a defect **outside** the down-type family that the ruling did not cover:
the W. The cage list read "Linear hDP chain", but an hDP chain is a chain of bound neutral pairs and
carries charge 0, while W^± carries ±1 — the single residual entry in SM-2 that could not reproduce
its own charge. It was not closable by arithmetic. The founder ruled the W⁰ neutral, a ring of three
qDPs and three eDPs; harmonising that against the Weak Sector lane (SF-2 v1.0 Thm 4.2, via
`capotauro.tex`) identified the ring as the **Petrie hexagon of the first-shell icosahedron**, six
vertices, one DP object per site, 12 CPs — preserving SM-2's existing member count while correcting
both topology and species. The closing audit (`0945_sm2_charge_audit_closure.py`, 6/6) shows zero
residual charge defects across all 17 cage entries.

The ring's *order* remained. Applying the founder's empirics criterion honestly **excluded** the
chiral arrangement: `χ` is odd under all 60 orientation-reversing lattice elements, so with `χ ≠ 0`
the reflections are not symmetries of the physical substrate, under which a chiral order splits into
two inequivalent neutral ring states — against the Standard Model's single W³. Of the two achiral
orders the founder chose alternating, on symmetry economy, recorded explicitly as a structural
assignment pending an observable, on the same epistemic footing as SM-2's N_k values. No observable
yet selects it; that falls to the EW lane with `OPEN-EW-5`.

## Patches 0950–0951 — the V3 re-read: all three CAPACITY-1 conditions survive

With L4-A's residual named (see the F.1 vignettes), the question was whether CAPACITY-1's three
conditions still hold. **C1 robust**: both residual terms are per-edge functions, so no
distinct-edge coupling is introduced, and the 0828 spectral bound never references the rate law at
all. **C2 robust where it claims**: a constant `A` promotes the steady current from `δ³` to `~A²δ`,
two orders, but C2 is stated at the physical bias, where the current spread across `A ∈ [0,1]` is a
factor of 2 with `O(J²) ≤ 1.1e-9`. **C3 clears**: `K_lift` is 0.0526–0.0532 across the scanned
domain against thresholds giving 36–80% margin. The structural reason C3 barely moves is worth
keeping: **η is a sign**, so a reversal-even per-edge scale reaches the correlator only through
relative within-vertex weighting, second order on ρ. This also corrected 0950, which had over-weighted
a 10.9% measure shift that does not transfer to `K_lift` at all.

## Patches 0952–0960 — CONV-047 fails quorum, CONV-048 costs nine turns and is enacted

CONV-047 was dispatched to five seats and **failed quorum: 2 valid returns, 3 rejected.** One seat
stated in its own reasoning that it was simulating the whole panel; one reported sub-second timings
for a 47-second script. A five-slot win cannot be carried on two seats, so the registered wording
stood. The two valid seats nonetheless established the result that mattered — the reversal-odd
uniqueness survives independent audit — and both independently demanded the admissible `A`-domain,
which was computed and adopted.

The re-dispatch as CONV-048 was **reformatted on the founder's report that the package was confusing
to read**, and the diagnosis is worth preserving: the package asked questions *about* C1/C2/C3 while
never defining them, which is exactly how one rejected seat invented a "C2 class" and another
misnumbered every question. Adding a glossary, moving internal bookkeeping to a wrapper, putting
questions last and telling reviewers that honest failure beats invention fixed most of it — Gemini,
which had fabricated five seats at CONV-047, disclosed honestly that it could not run the scripts.

CONV-048 then ran five more turns. Grok and Copilot independently demanded the **joint corner**
(negative `A` × odd quadratic); it was untested, and running it found two things the lane had not
known: the admissible domain is **not a rectangle** (the published `|A| ≤ 1.025` is a `C = 0` slice;
at `A = −1, C = +φ⁻³` the rate goes negative), and stacking is **superadditive** — the joint `J²` is
4.0× the sum of separates. Enacted at 0960 with five named residuals, the binding one being that
**residuals are coupled, so no general compositional-robustness principle may be inferred and any new
residual must be assessed jointly.**

## Patch 0959 — R-1 and R-2, enacted at the founder's cost, not the lane's

The founder's report on CONV-048 was "nine turns is a lot of effort for me," and the cause recorded
against the lane is exact: the panel produced three of four substantive findings, but **every
correction to the lane's own text came from the lane, after dispatch** — the founder's dispatch
cycles had been used as a debugging loop, and all four hostile tests were cheap and runnable
beforehand. **R-1**: run the hostile pass before dispatch, testing parameters *jointly*, the full
admissibility domain rather than one slice, and the next order of any expansion proposed for
truncation. **R-2**: two full dispatches per claim, then enact on reviewers' stated conditions or
abandon and bank what stands alone. An extra round costs the lane minutes and the founder a full
manual five-seat dispatch.

## Patches 0961–0968 — piece 1: symmetry route closed, then discharged in the dissent's form

Scoping (0961) closed the obvious route: four of nine shells have edge orbits `[1,1,5,5]` under
`Stab_v`, so a covariant observable may put all weight on a singleton and reach `p = 1`. **Symmetry
permits exactly the collapse piece 1 must exclude** — Route B eliminated, not untried. That
reframed the problem as the **η-identity** question: not "is some observable non-degenerate" but
"which observable does the dynamics single out, and what are its weights?"

Route A found the corpus already pinned them: every η construction (0819, 0820, 0821) builds the
per-edge weight as `sign det[·]`, unit magnitude; for unit weights participation equals support; and
the 4-D orientation floor argument was already on file. The hostile pass (0964, R-1's first use)
cleared all three checks and found the reviewer trap in our own corpus — 0820 §(2)'s superseded
"4-edge det reads only 4 (⇒ emergent)", two paragraphs from the uniform-weight claim, which reads
cold as our corpus contradicting our floor.

Two rounds of pre-dispatch returns were unanimous HOLD and produced four corrections, of which two
should be kept in mind permanently. Grok's: *the MC freezes the weights and moves only edge means,
so it cannot show the substrate is incapable of deforming them* — adopted verbatim as a named limit.
GPT's: *four vectors to define chirality does not imply four coefficients to read it* — correct, and
it withdrew link (c)'s universal form. The headline was withdrawn on both seats' independent ruling:
not "V3 unconditional on the axioms" but the floor **replaced** by a structural identification,
GPT's formulation being that this prevents the last assumption disappearing by renaming rather than
deriving it.

CONV-049 was then dispatched **with its effort bound written at dispatch** — the CONV-047/048 miss
not repeated — and closed in one round. The adjudication is the part worth preserving: A was 5/5 YES
and B was 3 YES / 2 NO, so the rule's condition was met, **but it was enacted in the dissent's
form.** The two NO seats were right and the three YES seats did not defend their inference: "whole
vertex figure" names the *index set* of a sum and does not force nonzero terms, which is the exact
smuggling question B was written to prevent; one YES was itself reasoned from the dissent's geometry.
Link (c) became Grok's **3-plane lemma** — at most 5 of the 12 first-shell directions lie in any
admissible `span{n̂,r̂₁,r̂₂}`, so support ≥ 7 everywhere and `p ≥ 7 > 4`, stronger than required, and
it explains 0964's hostile minimum of exactly 7, which had been measuring this lemma without naming
it. CAPACITY-1 now carries the axioms, the derived first harmonic, and an explicit structural
premise — **not unconditional, and never to be described as such.**

## Patches 0969–0971 — dissents recorded as satisfied; TARROW-2 re-read

0969 recorded that both CONV-049 dissents were **satisfied, not overridden** — a distinction that
decays fast if not written down, since the vote tally alone would suggest otherwise. 0971 then
tested the 1d-β problem history's prediction that discharging Mechanism A would unconditionalize the
temporal verdict as well. **Half right, and the half that matters is right.** Reproduced at `A = 0`:
1200 faces, `a+b+c = 0` to 2e-16, exactly 420 with nonzero `abc`, slope 3.00. With a constant
`A = 0.3` the slope drops to 0.99, because the effective tilt becomes position-dependent and the
per-face `O(δ¹)` cancellation fails — so TARROW-2's order-counting **consumes** `A = 0`. But the same
420 faces violate detailed balance at every `A` tested: the residual changes the **order** of
failure, not **whether** it fails, and it fails **earlier**. Structurally identical to CONV-048's C2
finding, and the same repair applies — a scope clause, not a re-derivation and not a panel.

## Patch 0970 — 1d-β scoped, and a correction to the lane's own framing

1d-β asks whether FI-C-9 is primitive or emergent, **not** to derive it. Its problem history names
two closure routes, and both arms of the first were discharged the same day — Mechanism A at 0960,
pointwise non-degeneracy at 0968. The status line was stale in two places and was corrected. The
lane's own earlier framing of 1d-β as "derive FI-C-9 itself" was **wrong**; that is OPEN-SM-4(b), a
flagship programme, cross-sector, gated on EW development, and it was scoped and declined twice
rather than opened from inside this lane.

---

# Session 229 — Patch 0976 (14 Sep 2026): the ruling executed and the corrigenda applied

*Tier-3 vignette, written at Patch 0981 in the window that produced the work. The rest of Session 229 was
governance and documentation with no paper scope; its record is `session_logs/2026-09-14_session_229_log.md`
and the Tier-4 fragments at `reasoning/0975.md`, `0976.md`, `0977.md`, `0979.md`.*

The founder ruled on the question 0972/0973 had put under PD-006(a): **relabel accepted.** Reading C's `ℓ`
is a directed traversal cost — equivalently a hop time — and not a metric edge length. The equation is
unchanged; only its description was wrong. The ruling adds nothing to the ontology, and that is the part
worth carrying forward: the 1-form permitting a directed cost is a Randers/Finsler `β = ε n̂` built from `n̂`,
already a substrate primitive, and with THEO-CHIR-MERGE-2 the non-reciprocity **is** the T-arrow the arc
already carries as W3. The substrate's geometry stays reciprocal; its dynamics do not, which is what an arrow
of time means.

With the ruling in hand the arc's five paste-ready corrigenda — carried since 0937, 0942, 0971 and 0972 —
were written into source: Capotauro §20 and the relabel footnote, `chirality_continuum.tex`, SM-2 edits
(a)–(f), the TARROW-2 claim (i) scope remark, and the F.1 wording bundle (MA.2 vertex-independence, the
`r(−ê;v)` referent, exclusion class E1 narrowed, `δ = −ε` pinned, and the relabel).

**One instruction was wrong as written, and this is the vignette's finding.** The corrigendum directed that
`chirality_continuum.tex` *"cites the A₂u label at four places (grep `A_{2u}`) — same correction."* It is not
the same correction at all of them. Three occurrences are the matter-doublet **state space**, the 2D subspace
of `A₁g ⊕ A₂u`, which 0937 never touched and which are correct as written; 0937 changed the **operator**
assignment. A grep-and-substitute would have fixed two statements and corrupted three. This is D-7 in its
exact shape — one symbol naming two objects in one file — and it is recorded because the instruction will be
read again at the recompile by someone who may not re-derive the distinction.

**SM-2 edit (g) was held deliberately.** The Mass Contribution Breakdown W row still reads `Linear 6-hDP
chain` on purpose, gated on `OPEN-EW-5`: it is the only place a published SM-2 number can still move, and
applying it now would assert a pure relabel that may be false. Edits (a)–(f) are independent of it.

**PDF recompiles remain owed** (`TODO-0976-RECOMPILE`), founder-mechanical.

## H1 and the Vafa–Witten route (Session 231, Patches 0983–0985, 15 Sep 2026)

The EW lane had spent forty patches on H1 and closed with it refuted (4056/4057) and then, in an
unpushed critique, conditionally restored (4062). The CHIR audit those patches owed turned out to be a
reading question before it was a classification one. VW-2 v1.1 defines H1 as Osterwalder–Schrader
positivity for the Euclidean time-reflection, equivalent to VW-a-4, and its bridge remark records that
its own v1.0 had conflated that reflection with the spatial parity and withdrawn the conflation. The EW
arc, opening at 4022 with Θ = diag(1,1,1,−1) on the single-time occupation law, tested exactly the
withdrawn reading throughout. Neither the refutation nor the restoration is a statement about H1, which
stands where VW-2 left it: open, with the δ = 0 base case proved from detailed balance. Only four EW
bookkeeping files had absorbed the wrong status; none of the theorem sources or scoping documents had.

Attacking that result produced a larger one. The Vafa–Witten bound is |∫dμ e^{iλO}| ≤ ∫dμ, and it needs
the parity-odd source to be a phase — in Vafa–Witten's setting a Lorentz-invariant pseudoscalar carries
a time index and Wick rotation supplies the i. On the substrate the Moment is time, η is a real
pseudoscalar of the 4D ambient space at fixed Moment, its source is real, and Jensen gives the opposite
inequality: the symmetric point maximises Z. Definition 2.1's "no sign problem" clause, automatic for a
probability measure, carries nothing. VW-1 v1.1's review had folded "the measure-class transposition"
into H1's scope; isolated, that step does not go through. The route H1 ⇒ μ² > 0 is inapplicable as
posed, whatever H1's truth value. V3 confirmed / V1 excluded rest on CAPACITY-1 and do not move. VW-1
carries a v1.5 corrigendum stating the missing hypothesis H1′; the one escape — a P-odd and Moment-odd
order parameter carrying the time index — is named and not built.

The exact-rate probe of the Θ_OS pairing on the single-walker toy returned λ_min = −3.5×10⁻¹⁵ at
δ = 0.35, t = 1, identical at 30 and 45 digits and seventeen orders above the arithmetic floor, against a
genuine spectral tail of ~10⁻¹⁶. Under the rule pre-committed before the run it adjudicates as "claim
nothing," because the rule's thresholds had been sized before the tail scale was known. The rule was
corrected and re-committed before a second run; a confirmed negative would be a toy result — a
non-reversible chain's single-time pairing going negative at large tilt — and moves no verdict.
