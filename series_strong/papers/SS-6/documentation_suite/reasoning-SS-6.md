# Tier 4 Reasoning Archive — SS-6 v0.2

**Paper:** SS-6 v0.2 (Deuteron Observables Beyond Binding: Scope and Limits of the Base-to-Base Picture)
**Tier:** 4 — substantive Opus reasoning verbatim, housekeeping excluded but no compression
**Companion files:**
- Tier 1: `SS-6_deuteron_observables_beyond_binding.tex/.pdf`
- Tier 2/3: `documentation_suite/` (companion files; some still pending under the post-review documentation-deferral protocol adopted during this paper's cycle)
- Tier 3: `letters/SS-6_v02_copilot_review_response.md` (reviewer-response document for the v0.2 round of external review)
**Created:** 2 May 2026 (retroactive recovery from chat-window pasted 2 May 2026)

---

## Scope note — single-window v0.1 → v0.2 recovery

This file recovers the **SS-6 v0.1 → v0.2 development arc (17–19 April 2026)** at Tier 4 fidelity from the long chat-window that also produced `reasoning-SS-5.md` (and that is the source for `reasoning-SS-7.md`'s v0.1 → v1.1 production cycle). The arc covers paper birth, the Q_d sign discovery, the three-category classification, v0.1 drafting, v0.1 self-review catching three substantive errors, v0.2 production with framing sharpening, and the first external-review cycle which yielded the formalization of the reviewer-response protocol mid-cycle. The session also produced two programme-level methodological decisions that landed in `templates/operating_system.md`: the version-nomenclature standardization (v0.x / v1.0 / v1.x / v2.0) and the documentation-suite-deferral protocol.

**Honest scope limitation.** The recovery is from the chat-window text only. The paper's later development past v0.2 (any subsequent revisions, OSF registration cycle, retrospective companion-suite production) is not captured here and would be a candidate for retroactive recovery if relevant chat-windows surface. The reviewer-response document for the v0.2 Copilot review is preserved at full fidelity in `letters/SS-6_v02_copilot_review_response.md` and is not duplicated here; this file captures the *reasoning that produced* the response document, not the document itself.

**Programme-methodology content arising from this same chat-window — not duplicated here.** The cycle produced four codifiable methodology updates: (1) the version-nomenclature convention, (2) the documentation-suite-deferral protocol, (3) the reviewer-response document protocol (formalized as Phase 4 of `templates/operating_system.md`), and (4) the paper-type taxonomy (theorem / prediction / derivation / scoping / infrastructure). All four are preserved at canonical fidelity in their respective home files and are referenced in this file's "What is preserved elsewhere" section rather than duplicated. The Tier 4 reasoning specific to SS-6 is sessions 1–5 below.

---

## Session 1 — Birth as the bipyramid paper, and the scope question (17 April 2026, evening of SS-5 v6 close)

*[Note: SS-6 entered existence as a deliberate scope decision after SS-5 v6 was complete. The strategic question — what is the highest-value next star shot? — was resolved in favor of probing whether the bipyramid mechanism that successfully produced B_d could also predict additional deuteron observables (Q_d, P_D, μ_d, scattering lengths) from the same geometry. The reasoning below captures the case for breadth-over-depth and the specific scope decision.]*

I like your idea of broadening the search, giving us more independent stars to shoot to locate our position more precisely.

Two observations made this the right move at this moment:

1. The 5% deuteron residual is hard to close without curve-fitting risk. Any specific NLO mechanism we propose — chain-length corrections, contact-gap stretch, ZBW-phase incoherence — would need a coefficient that lands the deuteron at 2.224 MeV. Three independent candidates already identified (9-edge bipartite contact, non-zero gap, phase incoherence) with different mechanisms but similar magnitude; selecting any one of them after the fact would be exactly the post-hoc-selection mode that v4 was rejected for.

2. Predicting additional deuteron observables from the same bipyramid geometry — without any new parameters — is *more* valuable than closing the last 5% of the binding. It converts SS-5 from "good binding number, mechanism plausible" to "geometry constrains an entire suite of observables consistently." The D-state admixture P_D, magnetic moment μ_d, and intrinsic quadrupole Q_d all live downstream of the same bipyramid structure; if it predicts them within reasonable residuals, the structure is doing real work.

**Scope decision (medium-broad, three linked observables):** intrinsic quadrupole Q_d, D-state admixture P_D, magnetic moment μ_d. These form a single chain from one geometric calculation: Q_d comes from bipyramid geometry; P_D follows via standard quadrupole-to-D-wave conversion; μ_d follows from P_D via standard spin algebra. Three clean predictions from one geometric premise matches SS-5's caliber and keeps the paper tight. Deferring scattering length / effective range to a follow-up because they require constructing V(r), which is a different (messier) computational object.

**Paper ID decision: SS-6.** Reasoning: "test the existing mechanism with new observables before extending to new regimes" is the right epistemological order. The alpha-cluster work (previously slated as SS-6) moves to SS-7 and remains OPEN-SS-18. The bipyramid paper is the natural continuation because it stress-tests SS-5's core geometric claim at higher resolution — if the bipyramid predicts Q_d, P_D, μ_d all within the CPP residual band, the base-to-base mechanism is confirmed from an independent direction.

*[Outcome: Phase 1 numerical exploration began on this scope. The plan was to compute Q_d first (simplest, geometric), then derive P_D from Q_d via the D-wave admixture relation, then compute μ_d from P_D via the standard spin algebra. The three-observables chain was clean in principle. What followed in Session 2 broke the chain at the very first link and forced a complete rescoping of the paper.]*

---

## Session 2 — The Q_d sign discovery: chain-prediction breaks at step 1 (17 April 2026, late evening)

*[Note: This is the substantive physics turn where SS-6's intended scope — three linked deuteron observables predicted from bipyramid geometry — was diagnosed as unworkable, and the *reason it was unworkable* turned out to be a substantive structural finding rather than a setback. The Q_d sign computation is the load-bearing physics content for everything that follows.]*

**Phase 1 numerical computation:** the rigid base-to-base bipyramid has all electromagnetic charge concentrated in the equatorial contact plane (the three net-+1/3 quark-pair positions where proton u-quarks coincide with neutron d-quarks), while the apices (along the symmetry axis) carry polarity but no EM charge. Computing the body-frame intrinsic quadrupole moment of this charge distribution:

$$Q_0^{\text{body}} = -\frac{1}{3}\left[\frac{r_{uu}^2}{2} + y_3^2\right] = -0.224 \text{ fm}^2$$

at SS-2's lattice-edge distances ($r_{uu} = 1.07$ fm and $r_{ud} = 0.62$ fm, with appropriate equatorial geometry), where the negative sign reflects the *oblate* charge distribution (charges in the equatorial plane, not along the axis).

**Observed:** $Q_d = +0.286$ fm² (prolate, axial elongation of the deuteron charge distribution).

**The signs are opposite.** Initial reaction: this is a problem. The chain Q_d → P_D → μ_d that SS-6 was supposed to derive falls apart at step 1.

**Reframing — this is a diagnostic, not a failure.** The observed Q_d is well-known in conventional nuclear physics to arise from the D-wave (L=2) component of the deuteron wavefunction at orbital separation $r_{np} \sim 2$ fm. The relationship (standard):

$$Q_d \approx \frac{\sqrt{2}}{10} \int_0^{\infty} u(r) w(r) r^2 \, dr - \frac{1}{20} \int_0^{\infty} w(r)^2 r^2 \, dr$$

where $u(r)$ is the S-wave radial wavefunction and $w(r)$ is the D-wave wavefunction, weights $Q_d$ heavily with the *large-r* structure of the wavefunction. With $\langle r^2 \rangle \approx 15$ fm² for the deuteron, the dominant contribution to $Q_d$ comes from $r \gtrsim 2$ fm — far outside the $\lesssim 1$ fm bipyramid core.

The rigid bipyramid predicts $-0.22$ fm²; the orbital wavefunction must produce $+0.286 + 0.22 = +0.506$ fm² of outward-pointing prolate contribution to cancel the bipyramid's oblate intrinsic moment and reach the observed value. In other words, the orbital-dominated quadrupole contribution must be *roughly twice as large* as the observed Q_d and of *opposite sign* to the bipyramid core's contribution.

**This is not a failure of the bipyramid mechanism. It is a diagnostic.** The bipyramid is doing what it should; it is the rigid-core part of the deuteron, and its quadrupole signature is exactly what such a core would produce. The dominant Q_d comes from physics at a different scale (the orbital wavefunction at $r \sim 2$ fm), which the bipyramid does not and cannot describe alone.

*[Outcome: this finding *is* substantive content, not a negative result. It tells us where the bipyramid mechanism's domain of validity ends and where the next layer of physics — the orbital wavefunction — begins. The right SS-6 is no longer "predict three deuteron observables"; it is "classify which observables the bipyramid reaches and which require physics at the orbital scale."]*

---

## Session 3 — v0.1 drafting with the three-category classification (17–18 April 2026)

*[Note: The recognition in Session 2 that the bipyramid couldn't predict Q_d directly led to a complete rescoping of SS-6. Instead of making three predictions, the paper would *classify* every deuteron observable by which scale of physics dominates it. This classification IS the paper's contribution. The category split is the substantive structural content.]*

The paper becomes a scoping document, organized around the three-category classification:

**Category A — bipyramid-geometric (3 observables, already derived in SS-5):**
- Binding energy $B_d = M_0/\varphi$
- Spin-parity $J^P = 1^+$
- Isospin $I = 0$

These follow from the bipyramid contact geometry alone. The K_3 face structure delivers the bonding eigenvalue +2 (giving $M_0/\varphi$ binding); the antisymmetry of the base-to-base alignment under p↔n exchange forces I=0; the parallel-spin correlation across three q-q DP chains forces S=1 hence $J^P = 1^+$.

**Category B — bipyramid-via-V_{SR} (3 observables, await V_{SR}(r) derivation):**
- Scattering length $a_{np}$
- Effective range $r_0$
- Singlet ${}^1S_0$ virtual state energy

These are determined by the *shape* of the short-range potential $V_{SR}(r)$ rather than just the binding-energy magnitude. The bipyramid contact at $r \sim l_{\text{edge}} = 0.36$ fm sets the depth; the K_3 mode's spatial structure and the eDP/qDP chain dynamics set the *radial profile* of the attractive-then-repulsive potential as the contact deforms. The Bethe-Peierls zero-range approximation $a = 1/\kappa = 4.32$ fm follows from $B_d$ alone (universal physics, not CPP-specific); to reach the observed 5.43 fm, $V_{SR}(r)$ shape information is needed. **Register OPEN-SS-20 (V_{SR}(r) shape from CPP primitives).**

**Category C — orbital-dominated (5 observables, await orbital wavefunction):**
- Quadrupole moment $Q_d$
- Charge radius $r_d$
- Matter radius $r_c$
- D-state admixture $P_D$
- Magnetic moment $\mu_d$

These are dominated by the orbital wavefunction at $r \sim 2$–4 fm, far outside the bipyramid core. CPP cannot reach these from rigid bipyramid geometry alone. The deuteron's relative-motion wavefunction $\psi_{np}(r)$, with its $1/\kappa = 4.32$ fm exponential tail, is the dominant contributor. **Register OPEN-SS-21 (deuteron orbital wavefunction from CPP framework).**

The classification is *the paper's contribution*. It honestly delineates what the bipyramid mechanism reaches and what it does not, and it identifies two specific open problems (V_{SR}(r) shape and orbital wavefunction) as the natural next research targets.

**New propositions registered:**

- **PROP-SS-6-1:** Observed deuteron quadrupole $Q_d$ is orbital-dominated, not bipyramid-dominated. SUPPORTED by the explicit calculation in §4.1: rigid bipyramid intrinsic $Q_d^{\text{int}} = -0.22$ fm² (oblate) vs observed $+0.286$ fm² (prolate); the orbital D-wave contribution must dominate by roughly a factor of two with opposite sign.

- **PROP-SS-6-2:** Zero-range Bethe-Peierls relation gives $a_{np} = 1/\kappa = 4.32$ fm from $B_d$ input alone. This is a universal physics result (not CPP-specific) but it is worth recording because it sets the precision-floor for the scattering-length prediction: any improvement on $-20\%$ requires $V_{SR}(r)$ from CPP.

*[Outcome: v0.1 was drafted as a 12-page scoping paper with the three-category classification in §4 and the open-problem registrations in §5. The paper's epistemic posture is honest: this is what the bipyramid does and does not do; here are the two specific targets for closing the gaps. Paper-type declaration: this is a scoping paper, not a prediction paper. The classification framework is itself the deliverable.]*

---

## Session 4 — v0.1 self-review: three errors caught (19 April 2026)

*[Note: A self-review pass on v0.1 — applying the same hostile-reviewer treatment that the SS-5 v4 stress test applied to in-house derivations — caught three substantive errors. One was an arithmetic inversion that flipped a key result by a factor of ~30 and reversed its rhetorical effect. The other two were category confusions or numerical errors. All three are preserved in detail because the v0.2 corrections rest on these catches.]*

### Issue 1 — The Q_d comparison is category-confused

What §4.2 of v0.1 says: "bipyramid intrinsic $Q_d^{\text{int}} = -0.22$ fm² vs observed $Q_d = +0.286$ fm² — signs opposite."

That comparison, as stated, conflates body-frame intrinsic quadrupole with lab-frame spectroscopic quadrupole, which are different quantities.

- What I computed is $Q_0$ in the body frame (bipyramid symmetry axis = z).
- What is observed is $Q$ in the J=1, M=1 (lab-aligned) state.
- For a rigid prolate rotor, $Q_{\text{obs}} = Q_0 \times J(2J-1)/[(J+1)(2J+3)] = Q_0/10$ at $J=K=1$.

So if the bipyramid dominated, the predicted $Q_{\text{obs}}$ would be $\approx -0.022$ fm², not $-0.22$.

The conceptual conclusion ($Q_d$ is orbital-dominated, not bipyramid-dominated) is still correct and well-supported — both the sign and the order of magnitude are wrong for the bipyramid alone. But v0.1 as written misstates the numerical comparison, and a careful reader will catch it.

**v0.2 fix:** Present the comparison as: "The bipyramid's body-frame intrinsic quadrupole is oblate. Even converting to a spectroscopic value via the J=K=1 rigid-rotor relation gives $Q_{\text{obs}} \approx -0.022$ fm² — an order of magnitude too small *and* wrong sign. The observed $+0.286$ fm² cannot come from the bipyramid; it is orbital-dominated."

### Issue 2 — Effective-range formula is wrong

In §4.5.1 ("Status"), I inverted the Bethe-Peierls relation as $r_0 \approx 2(a - 1/\kappa)$, giving $r_0 = 2.21$ fm vs experimental 1.749 fm, a claimed 26% error.

**The inversion formula is wrong.** The correct formula from $1/a = \kappa - r_0 \kappa^2/2$ is:

$$r_0 = \frac{2(\kappa - 1/a)}{\kappa^2}$$

which gives $r_0 = 1.76$ fm — a **+0.8% agreement** with experiment, not −26%.

This is an embarrassing mistake and it flips the rhetorical effect of the paragraph: what I wrote as "the expansion has significant higher-order terms" is actually "the leading-order effective-range expansion works to 1% for the deuteron." That's a much friendlier result for the programme than v0.1 claims.

**v0.2 fix:** Replace the §4.5 paragraph with the correct algebra and the $r_0 = 1.76$ fm result. Reframe as a *positive* finding: the effective-range expansion is extremely well-behaved for the deuteron at leading order, indicating a smooth short-range potential that whatever CPP eventually derives must reproduce. This becomes a constraint on V_{SR}(r) shape (OPEN-SS-20) — not an additional Bethe-Peierls credit-claim for CPP, but a precision target for any future V_{SR} derivation.

### Issue 3 — Kinetic energy number wrong

§2.3 says "kinetic energy ~20 MeV, potential depth ~35 MeV." Standard deuteron textbook values are $T \approx 33$ MeV, $V \approx 35$ MeV (both large, nearly cancelling to give the 2.2 MeV net binding). My 20 MeV is off by ~40%. Minor but should fix.

**v0.2 fix:** $T \approx 33$ MeV throughout §2.3.

### Issue 4 — Framing, not error: "$a_{np}$ from $B_d$ alone" is not a CPP prediction

§4.5 frames the Bethe-Peierls $a_{np} = 1/\kappa = 4.32$ fm result as noteworthy. The text is careful ("a standard-physics result"), but the framing in §1.1 and the abstract can be read as giving CPP credit for a universal textbook result. Any theory that predicts $B_d$ gets this for free via two-body scattering theory. The −20% error is just the deuteron's well-known zero-range shortfall.

With the corrected $r_0$ inversion giving 0.8% agreement, this actually becomes a more interesting observation: the effective-range expansion is extremely well-behaved for the deuteron, suggesting $V_{SR}(r)$ is smooth and relatively well-characterized by $r_0$ alone.

**v0.2 fix:** Sharpen the "CPP prediction vs standard physics" framing. The Bethe-Peierls relation is *not* a CPP prediction — it is *infrastructure*. What CPP predicts (once OPEN-SS-20 is solved) is $V_{SR}(r)$, from which $r_0$ follows. v0.1's framing is careful but could be crisper.

*[Outcome: the four issues above became the v0.2 fix-list. The Q_d body-frame/lab-frame correction and the effective-range formula correction are substantive math fixes; the kinetic-energy fix is a numerical hygiene item; the framing sharpening is a presentation item. None of the four required changing the three-category classification or the OPEN-SS-20/SS-21 registrations — those structural contributions of v0.1 survived intact. v0.2 is a correctness-and-sharpening pass, not a structural rewrite.]*

---

## Session 5 — v0.2 production with framing sharpening (19 April 2026)

*[Note: v0.2 production applied the four fixes from Session 4 plus the framing sharpening. The most consequential change is the effective-range correction: v0.1's claimed 26% error becomes v0.2's 0.8% match — a positive empirical result rather than a flagged limitation. Two programme-level methodology decisions also crystallized during the v0.2 cycle: the version-nomenclature convention and the documentation-deferral protocol. Both became OS-level codifications.]*

### v0.2 substantive changes (paper-level)

1. §4.2 Q_d analysis rewritten: body-frame $Q_0^{\text{body}} = -0.224$ fm² → lab-frame conversion via $J(2J-1)/[(J+1)(2J+3)] = 1/10$ at $J=K=1$ → predicted $Q_{\text{obs}} \approx -0.022$ fm² → observed $+0.286$ fm². Finding 4.1 strengthened: "ten times smaller AND wrong sign."

2. §4.5 effective-range section rewritten: correct Bethe-Peierls inversion $r_0 = 2(\kappa - 1/a)/\kappa^2 = 1.76$ fm against experimental 1.749 fm at +0.8%. Reframed as positive finding (well-behaved expansion → smooth V_{SR}) rather than as flagged limitation.

3. §2.3 kinetic-energy correction: $T \approx 33$ MeV.

4. Framing throughout: Bethe-Peierls a_{np} = 4.32 fm clearly labeled as universal physics (not CPP-specific). Abstract, §1.1 finding-list, §1.2 deliverables, §1.3 open-problems, §6.5 closing all updated to make this distinction unmistakable.

5. §1.1 finding-list now leads with: "The bipyramid mechanism predicts the deuteron's binding ($B_d = M_0/\varphi$) and quantum numbers ($J^P = 1^+$, $I = 0$) but does NOT reach the orbital-scale observables ($Q_d, r_d, P_D, \mu_d$). The 0.8% effective-range agreement is a precision target for future V_{SR}(r) derivation, not a CPP-specific prediction."

### Programme-methodology decisions arising during the v0.2 cycle (codified at OS level)

**Decision 1 — Version nomenclature standardization.** Diagnosed during the v0.2 numbering question: the v0.x → v1.0 promotion ritual that v0.1 was supposed to signal had fallen off. SS-5 went from v0.1 → v0.2 → v3 → v4 → v5 → v6 and was publication-ready well before any "v1.0" label. That's incoherent: a paper that's OSF-ready should not be labeled "draft" forever.

**Convention adopted (codified in `templates/operating_system.md` §11):**
- v0.x → pre-review preliminary drafts (exploratory, may change substantially)
- v1.0 → first "release" version, after at least one external review pass and the first round of corrections
- v1.1, v1.2, … → minor revisions, bug fixes, clarifications
- v2.0 → major revisions with substantive new content or reframing

Under this convention, SS-6 v0.2 (the work being produced in this session) is properly v0.2 because it has not yet seen external review. After ChatGPT and Copilot review return and their feedback is integrated, it will promote to v1.0. The grandfather clause: existing papers retain their current numbers; the convention applies forward.

**Decision 2 — Documentation-suite-deferral protocol.** The 7-file companion suite costs ~1 full session to produce per paper. Producing it concurrently with the paper means redoing it after external review costs another ~full session if any substantive mechanism changes (e.g., if a reviewer finds something that reshapes the Q_d framing — which, given what the v0.1 self-review just caught, is plausible). **Better:** produce the documentation suite ONCE when the paper is stable (passed external review, at v1.0+). What stays continuous regardless: development transcript, CHANGELOG, registry files, paper catalog. What waits: mechanism, phenomena, glossary, keywords, philosophy, development, reviews companion files.

What we'd lose: nothing substantive, as long as the development transcript is kept current and the paper's CHANGELOG tracks what a future documentation pass will need to reflect.
What we'd gain: not burning one full session's work when a reviewer tells us something needs rethinking.

**Codified in `templates/operating_system.md` §4 Phase 7 with explicit "DEFERRED" protocol, rationale, trigger conditions, and list of what IS maintained continuously.**

*[Outcome of v0.2 build: 13 pages, clean compile. The three correctness fixes plus the framing sharpening together substantially improve the paper's credibility. The Bethe-Peierls 0.8% match becomes a positive empirical observation rather than a flagged limitation. The Q_d category-confusion correction tightens the argument: 10× smaller AND wrong sign is decisively worse than just "wrong sign," and it forecloses any escape via geometric corrections at the bipyramid scale. v0.2 is ready for external review.]*

---

## Forward-looking pointers

- **OPEN-SS-20** — Derive V_{SR}(r) shape from CPP primitives. Controls $a_{np}$, $r_0$, singlet virtual state, low-energy phase shifts. Is the natural target for promoting Category B observables from "awaiting derivation" to "derived from CPP." Per research_frontier.md registration (18 April 2026).
- **OPEN-SS-21** — Derive the deuteron orbital wavefunction in the CPP framework. Multi-scale problem connecting the bipyramid core at ~0.4 fm to the orbital tail at ~2–4 fm. Is the natural target for promoting Category C observables. Per research_frontier.md registration (18 April 2026).
- **PROP-SS-6-1** — Observed deuteron $Q_d$ is orbital-dominated, not bipyramid-dominated. Status: SUPPORTED by explicit body-frame calculation. Strengthened by lab-frame conversion in v0.2: bipyramid contributes $\approx -0.022$ fm² at lab-frame, ten times smaller than observed AND wrong sign.
- **PROP-SS-6-2** — Zero-range Bethe-Peierls relation gives $a_{np} = 1/\kappa = 4.32$ fm from $B_d$ alone. Status: derived; **v0.2 framing sharpened** to clarify this is universal physics infrastructure, not a CPP-specific prediction. The 0.8% effective-range agreement adds precision-target context for OPEN-SS-20.
- **External review cycle.** v0.2 went out for ChatGPT and Copilot review during the same chat-window as the v0.2 production. Both reviewers returned substantive feedback. The Copilot v0.2 review-response document is preserved at full fidelity in `letters/SS-6_v02_copilot_review_response.md`; the ChatGPT v0.2 review-response is referenced in the development record. The reviewer-response document protocol that operationalizes these responses was *itself formalized* during this same chat-window — see "What is preserved elsewhere" below.

---

## What is preserved elsewhere

- **`research_frontier.md`** — OPEN-SS-20, OPEN-SS-21, PROP-SS-6-1, PROP-SS-6-2 all formally registered with full metadata. The "Propositions registered from SS-6 v0.1 (18 April 2026)" header section provides the canonical statements.
- **`series_strong/papers/SS-6/SS-6_deuteron_observables_beyond_binding.tex/.pdf`** — the paper itself at v0.2, with the three correctness fixes integrated, the three-category classification in §4 and Table 4, the Q_d body-frame-vs-lab-frame analysis, the corrected effective-range result, and the open-problem registrations.
- **`series_strong/papers/SS-6/letters/SS-6_v02_copilot_review_response.md`** — the v0.2 Copilot reviewer-response document, the second use of the reviewer-response protocol after the SS-7 cycle's first uses. Contains the full ChatGPT-vs-Copilot cross-cutting analysis (e.g., ChatGPT's "do not overclaim" advisory constraining how Copilot's schematic-figure request is captioned) that is itself programme-methodology content.
- **`templates/operating_system.md` §11 "Version management"** — the v0.x / v1.0 / v1.x / v2.0 convention codified during this paper's cycle. Adopted 19 April 2026. Grandfather clause for existing papers; applies forward.
- **`templates/operating_system.md` §4 Phase 7 "Documentation Suite"** — the documentation-deferral protocol codified during this paper's cycle. Companion suite produced ONCE when paper is stable (post-review, at v1.0+). What stays continuous: development transcript, CHANGELOG, registry files. What waits: the seven companion files.
- **`templates/operating_system.md` §4 Phase 4 "Multi-AI Review Cycle"** — the reviewer-response document protocol formalized during this paper's cycle. Standard filename `[S]-[N]_v[X.Y]_[reviewer]_review_response.md`, eight-section structure (Executive summary / A-accept / B-partial / C-decline / Summary table / Net effect / Strategic observations / Next steps). The protocol exists *because* this paper's cycle made the value of structured reviewer responses visible.
- **`templates/operating_system.md` §3 "Paper-type taxonomy"** — five paper types formally defined (theorem / prediction / derivation / scoping / infrastructure) with success criteria, review protocol per type, type declaration convention. SS-6 is the canonical *scoping paper*; declaring this in the paper's abstract preempts the reviewer-mismatch failure mode (where a reviewer expects a prediction paper and dismisses a scoping paper for not being one).
- **`programmatic_decisions/PD-001-signature-thread-and-swarm-convention.md`** (24 April 2026) and **`templates/paper-formatting.md` §§4.1A and 4.1B** — the swarm-validation and CP/GP-signature subsection conventions that apply to all CPP papers including SS-6, codified shortly after SS-6 v0.2 shipped.

*End of reasoning-SS-6.md (recovery patch 0024, 2 May 2026). Future appends as new chat-window content surfaces — post-v0.2 development (any subsequent revisions, v1.0 promotion after external-review integration, retrospective companion-suite production) is not yet captured at Tier 4 fidelity and would be a candidate for retroactive recovery if relevant chat-windows surface.*
