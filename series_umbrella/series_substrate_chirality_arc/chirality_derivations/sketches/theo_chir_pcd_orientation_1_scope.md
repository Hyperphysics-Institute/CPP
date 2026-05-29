# THEO-CHIR-PCD-ORIENTATION-1: Scope and Precondition Sketch

## The $\hat{n} \mapsto \vec{\omega}_{PCD}$ Link as a Chirality-Classification Theorem

**Patch 0635, Session 148** (29 May 2026)
**Sector:** CHIR (Substrate Chirality Arc) — first downstream derivation theorem after THEO-CHIR-AUDIT-1.
**Resolves:** audit entry **E20** (the $\hat{n}\mapsto\vec{\omega}_{PCD}$ link) / **OPEN-CHIR-F1-LINK**.
**Status of this document:** scope-and-precondition sketch (the artifact-planning step; the theorem artifact ships in a later patch, after the precondition gaps of §5 are cleared — exactly the Patch-0630→0632 pattern the audit followed).

---

## §0 Working-session firewall

This sketch plans a theorem; it does not prove it. It scopes the question, recaps the
existing F.1 groundwork the theorem will lift, states the honest target finding and the
layer it can be claimed at, and registers the precondition gaps. No registry mutation of
`theorem-registry.md` (no proved-theorem row) happens at this patch; THEO-CHIR-PCD-ORIENTATION-1
is the reserved ID for the eventual artifact. The audit's E20 classification is *not*
changed by this sketch; the reclassification target is recorded for the artifact patch.

This sketch inherits, and must not weaken, the calibration discipline the F.1 trajectory
already imposed on itself (`dynamical_substrate_law/sketches/F1_subquestion_pcd_orientation_link.md`
§14.17): the $\vec{\omega}_{PCD} = \sigma_{cycle}\,\hat{n}$ result is at **viability level**
(Layer 2.5), not Layer 3, with three open structural commitments. The CHIR-classification
question is narrower than the full F.1 closure and can be answered more robustly — but it
inherits the F.1 status as a ceiling, never exceeding it.

---

## §1 The question this theorem answers

### §1.1 The audit's E20, precisely

THEO-CHIR-AUDIT-1 catalogued the PCD-cycle orientation pseudovector $\vec{\omega}_{PCD}$
(audit entry E20 / dynamics-pass sub-question D4) and classified it, at v1.1, as
**unregistered (conditional)**: emergent under Scenario A ($\vec{\omega}_{PCD}$ derived from
$\hat{n}$ via a substrate mechanism) and primitive under Scenario B ($\vec{\omega}_{PCD}$ an
independent primitive parallel to $\hat{n}$). The audit explicitly did not pre-commit
(exclusion X2) and registered the resolution as OPEN-CHIR-F1-LINK.

The precise classification question THEO-CHIR-PCD-ORIENTATION-1 must answer is narrower than
the full F.1 magnitude/empirical closure:

> **Does $\vec{\omega}_{PCD}$ introduce an independent chirality primitive (a third
> foundational input parallel to $\hat{n}$ and the temporal primitive), or does it reduce to
> the chirality primitives already registered by the audit?**

This is a primitive-counting question, not a magnitude question. It does not require the
Mechanism-A magnitude $|\chi|/6$ or the leptogenesis empirical check; it requires only the
structural relation between $\vec{\omega}_{PCD}$ and the registered primitives.

### §1.2 Why E20 is the right first downstream theorem

E20 is the only audit entry whose category is *conditional* — the only row whose
primitive/emergent status the audit left undecided. Resolving it (i) removes the one
conditional cell from the classification map, (ii) directly tests the audit's headline
spatial-reduction claim (if $\vec{\omega}_{PCD}$ were an independent spatial primitive,
"all spatial chirality reduces to $\hat{n}$" would fail), and (iii) is the entry with the
most existing groundwork (the entire F.1 trajectory), so it is the cheapest genuine
derivation to attempt first. The other emergent-provisional rows (E12, E13, E21 →
OPEN-CHIR-1a/1b/1d) and the deep unregistered E19 (OPEN-CHIR-1c/2d) follow.

---

## §2 Existing groundwork the theorem lifts

The F.1 sub-question sketch has already developed the substrate-mechanism content. The
theorem does not re-derive it; it lifts the relevant results and recasts them as a
CHIR-classification statement.

**Phase 1 — net DI-bit current $\parallel \hat{n}$ (F.1 §11, Finding DSL-1, hardened toward
DSL-4).** Under Mechanism A (a direction-correlated DI-bit propagation-rate asymmetry under
$\hat{n}$), the substrate's net DI-bit current at the host vertex is
$\vec{j}_{DI}^{net}(v_{\text{host}}) = (6 r_0 \delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$,
i.e. aligned with $\hat{n}$. Its unit direction is $\hat{j}^{net} = \mathrm{sign}(\delta)\,\hat{n}$.
This is a **polar, TI-even** directional content carrying $\hat{n}$'s spatial-flow direction.

**Phase 2 — the coupling rule (F.1 §12).** The cycle's intrinsic forward direction
P$\to$C$\to$D is a **TI-odd pseudoscalar** $\sigma_{cycle}\in\{+1,-1\}$ (T-odd because
time-reversal reverses the cycle; I-even because the cycle is internal to each CP). The
substrate cycle-orientation pseudovector is the product
$$\vec{\omega}_{PCD}(v) \;=\; \sigma_{cycle}\cdot\hat{j}^{net}(v)\;=\;\sigma_{cycle}\cdot\hat{n},$$
the unique lowest-order TI-odd substrate object constructible from the two framework contents
(TI-odd $\sigma_{cycle}$ $\times$ TI-even $\hat{j}^{net}$). TI-parity verified (F.1 §12.6:
the product is T-even, I-odd, TI-odd, the parity the manifestation-(iv) Wigner–Eckart datum
requires).

**Phase 3/4 (magnitude + phenomenology) are NOT inputs to this theorem.** The
$|M^{thermo}|=|\delta|/6$, the Case A.1 $\delta=\chi$ unification, and the 1.64% leptogenesis
consistency are F.1 magnitude/empirical content. They bear on OPEN-CHIR-1d (E21, $\chi=\phi^{-3}$)
and OPEN-CHIR-3, not on E20's primitive-count. Keeping them out is what lets the
classification be claimed more robustly than the full F.1 closure.

---

## §3 The target finding (and its honest layer)

### §3.1 The structural decomposition

$\vec{\omega}_{PCD}=\sigma_{cycle}\,\hat{n}$ decomposes the cycle-orientation into two factors,
each already registered by the audit:

- **Axis** $\hat{n}$ — the substrate primitive 4D direction, **audit E16** (the unique spatial
  primitive, FI-C-RC-1). The axis of $\vec{\omega}_{PCD}$ is not an independent direction; it
  is $\hat{n}$ itself (via the net DI-bit current being $\parallel\hat{n}$).
- **Sign** $\sigma_{cycle}$ — the cycle's intrinsic TI-odd handedness, which is the handedness
  content of the **temporal primitive** (the ordered PCD sequence, **audit E2/E5/E17**, carried
  by A1+A4). The sign of $\vec{\omega}_{PCD}$ is not an independent chirality; it is the temporal
  primitive's ordering expressed as a pseudoscalar.

### §3.2 The classification statement (target)

> **THEO-CHIR-PCD-ORIENTATION-1 (target).** Under CPP axioms A1–A11 + Reading C ($\hat{n}$ as
> substrate primitive) + Mechanism A, the PCD-cycle-orientation pseudovector decomposes as
> $\vec{\omega}_{PCD}=\sigma_{cycle}\,\hat{n}$, the product of the registered spatial primitive
> $\hat{n}$ (E16) and the registered temporal primitive's handedness $\sigma_{cycle}$
> (E2/E5/E17). It introduces **no independent third chirality primitive**. Scenario B is refuted;
> E20 is **emergent** from the two registered primitives jointly. The audit's headline claim
> "all spatial chirality reduces to $\hat{n}$" is therefore preserved: $\vec{\omega}_{PCD}$ adds
> no new spatial direction.

### §3.3 The honest layer — emergent (provisional), not established

The classification is claimed only at the layer the underlying F.1 result supports. Per F.1
§14.17 the $\vec{\omega}_{PCD}=\sigma_{cycle}\hat{n}$ structure is **viability-level (Layer 2.5)**,
bounded by three open commitments: (1) the local algebraic representation ansatz; (2) the
$\sigma_{cycle}$ algebraization (explicitation beyond the cycle direction's explicit content);
(3) Case A.1 ($\delta=\chi$). Therefore:

- **E20's reclassification target is emergent (P) — provisional**, not emergent (E) — established.
  The v1.1 grading is exactly the right instrument: there is now a registered reduction with a
  viability-level pathway and no second primitive apparent (so it is not *unregistered*), but the
  reduction is not Layer-3 hardened (so it is not *established*).
- **Robustness argument (why the classification is firmer than the full F.1 closure).** The three
  open commitments concern the *ansatz, explicitation, and magnitude* of the link — none of them,
  if they fail, reintroduces an independent direction or an independent handedness. Commitment (1)
  affects how the observable is represented; (2) affects whether $\sigma_{cycle}$ is "explicitated"
  vs "latent" in the temporal primitive — but in either case it is the temporal primitive, not a new
  one; (3) affects the magnitude $\chi$, which is E21's problem, not E20's. So even under the worst
  case for all three commitments, $\vec{\omega}_{PCD}$ remains a function of $\{\hat{n},\sigma_{cycle}\}$
  and introduces no third primitive. The primitive-count is robust; only the magnitude/Layer-3 rigor
  is provisional. **This is the load-bearing economy of scoping E20 as a classification theorem.**

### §3.4 What the theorem does NOT claim

It does not claim the full F.1 Scenario-A closure (that remains provisional at viability level).
It does not claim a Layer-3 derivation of $\vec{\omega}_{PCD}$'s magnitude. It does not derive
$\hat{n}$ or $\sigma_{cycle}$ (both remain primitives — the theorem shows $\vec{\omega}_{PCD}$ is
their product, not that either factor is itself derived). It does not resolve E19 (capture
handedness) — see §5.3, the sign $\sigma_{cycle}$ must be kept distinct from the capture handedness.

---

## §4 Section structure of the eventual artifact (intended)

Modeled on the audit artifact, ~6 sections, Layer target = viability/Layer-2.5-classification
(stated explicitly, per the F.1 ceiling):

1. **Setup** (~40 lines): the E20 question, the primitive-count framing, the three operational
   senses restricted to the spatial+temporal content $\vec{\omega}_{PCD}$ carries.
2. **The decomposition** (~80 lines): recap (cite, do not re-derive) F.1 Phase 1 (net current
   $\parallel\hat{n}$) + Phase 2 (coupling rule), recast as $\vec{\omega}_{PCD}=\sigma_{cycle}\hat{n}$.
3. **Factor classification** (~60 lines): axis $\to$ E16 ($\hat{n}$); sign $\to$ E2/E5/E17
   (temporal primitive). The two-factor TI-parity table.
4. **The primitive-count theorem** (~50 lines): Scenario B refutation; no independent third
   primitive; E20 emergent (provisional). The robustness argument of §3.3.
5. **Layer and open commitments** (~40 lines): inherit the F.1 three open commitments as explicit
   ceilings; state why the primitive-count is robust to all three; register E20 → emergent (P).
6. **Conclusion + falsifiers** (~25 lines). Falsifiers: (F1) exhibit an independent direction in
   $\vec{\omega}_{PCD}$ not equal to $\pm\hat{n}$; (F2) exhibit a sign content in $\vec{\omega}_{PCD}$
   independent of the temporal primitive's ordering; (F3) show $\sigma_{cycle}$ is the capture
   handedness E19 in disguise (which would *merge* E20 into E19 rather than into the temporal
   primitive — a reclassification, not a refutation).

---

## §5 Precondition gaps to clear before the artifact ships

### §5.1 Axiom-attribution reconciliation (REQUIRED)

The F.1 sketch attributes $\sigma_{cycle}$ to "**axiom A5** or equivalent" (F.1 §12.3). In the
canonical post-consolidation **nine-axiom** set, **A5 is the metric** ($\eta=\ell_{edge}/R_{circ}=1/\phi$),
which carries no cycle-direction content. The PCD cycle's ordering is content of **A1** (the CP's
capacity to perceive and respond) **+ A4** (the Nexus / Absolute-Moment cadence) — exactly the
audit's temporal-primitive attribution (E2/E5 = A1+A4; E17 = D1 PCD arrow). The F.1 "A5"
attribution is a pre-canonical-numbering drift. The theorem must attribute $\sigma_{cycle}$ to
**A1+A4** (the temporal primitive), reconciling with the audit. *(This is the same class of
precondition the audit cleared before shipping — axiom-count + PCD-terminology; here it is
axiom-attribution.)* This reconciliation should be recorded; whether it warrants a one-line note
in the F.1 sketch is a separate question deferred to the artifact patch (the F.1 sketch is a prior
immutable workstream — do not edit it inline here).

### §5.2 Inherit, do not relitigate, the F.1 viability status

The artifact must state the F.1 §14.17 three open commitments as inherited ceilings, not attempt
to close them (that is F.1 Phase-2 foundations work, a separate trajectory). The classification
theorem's job is to show the primitive-count is robust *to* those open commitments (§3.3), not to
resolve them.

### §5.3 Keep the cycle sign $\sigma_{cycle}$ distinct from the capture handedness E19

The deepest unregistered entry E19 (D3 capture handedness, consumed by SD-CHIR via $\zeta^W,\zeta^{qDP}$)
is a *spatial/CP* handedness in the partnering rule. $\sigma_{cycle}$ is the *temporal* ordering of
the PCD cycle. These must not be conflated: if a future result shows $\sigma_{cycle}$ and the capture
handedness are the same object, that *merges* E20 with E19 (and reduces two unregistered/provisional
items to one) — a programme-positive reclassification, but a different theorem (it would be
falsifier-F3 of §4 firing in the merge direction). The artifact keeps them distinct and flags the
possible merge as an open cross-link, not a result.

### §5.4 Confirm Mechanism A is the operative mechanism for the axis claim

The axis$\,\parallel\hat{n}$ claim rests on Mechanism A (the leading F.1 candidate). Mechanisms B/C
were registered as alternatives. The classification result is robust across A/B (both align
$\vec{\omega}_{PCD}$ with $\hat{n}$) but the artifact should state the Mechanism-A dependence
explicitly and note that under any of A/B the primitive-count conclusion is unchanged (no independent
direction), so the classification does not hinge on the A-vs-B selection.

---

## §6 Patch sequence

- **Patch 0635 (this patch):** this scope-and-precondition sketch at
  `chirality_derivations/sketches/theo_chir_pcd_orientation_1_scope.md`; reasoning fragment;
  the ChatGPT v1.1 re-review appended to `reviews-CHIR-AUDIT-1.md` (closing the audit cycle 3/3);
  CHIR.md OPEN-CHIR-F1-LINK marked "scoping in progress (Patch 0635)"; registry changelog.
  No theorem-registry proved-row; no E20 reclassification yet.
- **Patch 0636+ (target):** the THEO-CHIR-PCD-ORIENTATION-1 artifact at
  `chirality_derivations/theo_chir_pcd_orientation_1.tex` once §5.1 axiom reconciliation is in hand,
  plus reasoning fragment, plus theorem-registry registration, plus CHIR.md OPEN-CHIR-F1-LINK →
  resolved (provisional) + the audit's E20 reclassified unregistered(conditional) → emergent (P) in
  the CHIR.md record (the audit .tex table itself is v1.1-frozen; the reclassification is tracked in
  CHIR.md and the new theorem, not by re-editing the audit — or by a deliberate audit v1.2 if the
  team prefers, a decision for the artifact patch).
- **After:** OPEN-CHIR-1d (E21, $\chi=\phi^{-3}$, the magnitude the F.1 Phase 3 leaves provisional)
  and OPEN-CHIR-1c/2d (E19 capture handedness) are the next derivation targets, both seeded by the
  recent multi-AI review.

---

## §7 What the eventual artifact contributes to the programme

It removes the single conditional cell from the audit's classification map, confirms the headline
spatial-reduction claim survives ($\vec{\omega}_{PCD}$ adds no spatial direction), and demonstrates
the audit's intended downstream pattern: each emergent/conditional entry receives a derivation that
either reduces it to registered primitives (here: E20 $\to \hat{n}\times$temporal) or honestly
registers a residual gap. It is the proof-of-concept that the OPEN-CHIR-* programme is tractable,
and it does so without overclaiming — the primitive-count is firm, the magnitude/Layer-3 rigor is
inherited-provisional.

---

## §8 References

- `chirality_audit/theo_chir_audit_1.tex` (v1.1) — E20 / D4, the conditional cell; the two registered
  primitives E16 ($\hat{n}$) and E2/E5/E17 (temporal); exclusion X2; the v1.1 emergent (E)/(P) grading.
- `chirality_audit/review/reviews-CHIR-AUDIT-1.md` — the closed review cycle (3/3 on v1.1).
- `dynamical_substrate_law/sketches/F1_subquestion_pcd_orientation_link.md` — §11 (Phase 1 net current
  $\parallel\hat{n}$, DSL-1→DSL-4), §12 (Phase 2 coupling rule $\vec{\omega}_{PCD}=\sigma_{cycle}\hat{j}^{net}$),
  §6 (Scenario A/B/C), §14.17 (PROVISIONAL CLOSURE at viability level — the inherited ceiling).
- `axiom-registry.md` — canonical nine axioms; A1+A4 (temporal primitive content), A5 (metric, NOT the
  cycle direction — the §5.1 reconciliation point).
- `frontier_sectors/CHIR.md` — OPEN-CHIR-F1-LINK; OPEN-CHIR-1d (E21 magnitude); OPEN-CHIR-1c/2d (E19).
- `capotauro/` — Reading C ($\hat{n}=v_{host}$, $H_4\to H_3=I_h$); FI-C-RC-1; $|\chi|=\phi^{-3}$.

---

**Scope document complete.** Patch 0635 commits this sketch + reasoning + the audit-cycle close.
The artifact (Patch 0636+) ships once the §5.1 axiom-attribution reconciliation is in hand. The
honest target: E20 is emergent from the two registered primitives jointly — Scenario B refuted, no
third primitive — at provisional layer, inheriting the F.1 viability ceiling.
