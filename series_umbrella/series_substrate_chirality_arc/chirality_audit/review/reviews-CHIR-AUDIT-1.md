# Reviews — THEO-CHIR-AUDIT-1: Chirality Entry-Point Enumeration

**Theorem:** THEO-CHIR-AUDIT-1 (registered Patch 0632; review package Patch 0633)
**Sector:** CHIR (Substrate Chirality Arc)
**Review cycle:** Session 148, 29 May 2026
**Reviewers:** Copilot (Microsoft), Grok (xAI), ChatGPT (OpenAI)
**Outcome:** No falsifier produced (F1, F2, F3 all survive). One load-bearing
calibration finding (2-reviewer convergence) → applied as artifact **v1.1** at Patch 0634.

---

## Part 1: Reviewer verdicts (condensed; verbatim verdict lines preserved)

### Review 1 — Copilot (referee-grade structural review)

**Verification tiers:** table structure / per-pass exhaustion — Tier 1 (INSPECTED);
geometric facts (2I, A₅, φ⁻³, H₄) — Tier 2 reasoned from standard definitions, not
recomputed in CPP notation; reduction claims — Tier 1, structural not re-derived.

**F1 (completeness):** No clear missing entry at the axiom, geometric, or
existing-derivation passes — "no Tier-1 F1 hit" at those passes. *One concrete
candidate:* the **ZBW circulation sense**. The audit explicitly distinguishes PCD
from ZBW ("the rapid between-CPs oscillation in dipole pairs") but does not argue
why ZBW is guaranteed chirality-neutral. By the audit's own operational definitions,
ZBW's internal circulation sense is *prima facie* a chirality-touching dynamical
feature (spatial: circulation direction relative to n̂; temporal: whether the ZBW
cycle is T-symmetric). Recommendation: either add a row **E28: ZBW circulation
sense** (likely emergent/unregistered) or explicitly argue ZBW is parity- and
T-symmetric. "That's the strongest F1 pressure point I can see from the text."

**F2 (classification):** *Clean F2 hit.* E12, E13, E15, E21 are flagged "emergent"
but no registered theorem performs the derivations and the audit is explicitly not a
derivation paper — so by the audit's own definition they are "at least unregistered
(derivation owed)." Calling them emergent *now* is "a forward reference to
hoped-for derivations, not a classification grounded in existing theorems."
Recommendation: reclassify E12/E13/E15/E21 emergent → unregistered until the
OPEN-CHIR-* derivations are proved, then upgrade back. Separately, **E20** labeled
"emergent*" *pre-commits to Scenario A* — exactly what the audit says it must not do;
reclassify to "unregistered (conditional: emergent if A, primitive if B)." E16 (n̂
primitive) and E19 (capture handedness unregistered) are correctly classified —
"admirably conservative" on E19.

**F3 (fourth sense):** No falsifier. Amplitude-phase chirality → sub-case of
CP-asymmetric; thermodynamic/statistical arrow, information-theoretic order,
agentive asymmetry, gauge-chirality → all reduce to temporal or spatial. "Your
three-sense taxonomy looks operationally complete for the present CPP framework."

**Central reductions:** Restate spatial→n̂ as a *programme hypothesis at v1.0, not a
proved theorem* ("Conjecturally, all spatial chirality reduces to the single
primitive n̂… At v1.0, this is a programme hypothesis"). Temporal-primitive
classification is honest; note that a future OPEN-CHIR-2a derivation of the PCD arrow
would move E2/E5/E17 down to emergent.

**Contribution (E19/E21):** Cannot honestly claim a derivation; at best speculation,
not Tier-2. Leave as open targets; classify unregistered until derived.

### Review 2 — Grok (independent verifier + contributor)

**Verdict (verbatim):** "THEO-CHIR-AUDIT-1 passes its three falsifiers… The audit is
confirmed."

**Verification tiers (Tier 2 — INDEPENDENTLY RECOMPUTED):** |H₄| = 14,400 = 120×120,
contains improper isometries → 600-cell achiral (E3 correct). 2I (order 120) = double
cover of rotational icosahedral group, carries intrinsic chirality via two
inequivalent 2-dim irreps (G-2). A₅ (order 60) = rotational icosahedral symmetry,
purely proper rotations, chiral (G-3). 600-cell vertices = even permutations of
(0, ±1, ±φ, ±φ⁻¹); sign/parity choices select orientation, gauge-removable under H₄
but emergent once n̂ fixed (G-5). φ⁻³ = 2φ−3 ≈ 0.236 via φ²=φ+1; with η=1/φ (A5) baked
into the geometry, negative powers of φ arise naturally. "All geometric facts line up
exactly with the table."

**F1/F2/F3:** All pass. Notes that 600-cell fibrations / tetrahelices / isoclines are
sub-structures hosted *inside* G-1..G-6, not new entries. Primitives correctly
irreducible; emergent rows "all legitimately derivable once n̂ + 600-cell + dynamics
are given"; unregistered correctly flagged; no fourth sense.

**Contribution attempt (E19, E21):** Cannot supply a full algebraic derivation
because the precise functional form of the "capture" step (D3) and the exact
observable χ multiplies are not in the review package. But sketches both as
structurally available: **E21** — once the handedness observable is written (e.g. a
pseudoscalar ∝ n̂·(v₁×v₂) over a cage/tetrahelix), substituting the coordinate basis
"immediately yields φ⁻³"; "a one-line reduction once the observable is stated."
**E19** — capture handedness = sgn(n̂·(displacement × polarization)) at the capture
instant, constructible from n̂ + A2 + ω_PCD; "no second primitive is required."
Both "available inside the existing primitives… not blocked."

### Review 3 — ChatGPT (after PDF upload; meta-review of the Grok verdict)

**Verdict (verbatim):** "No falsifier currently established, but F2 remains debatable
and E19/E21 remain un-derived." Explicitly *weaker* than Grok's "defect-free."

**Disagreement with Grok's confidence:**
- **E21** — Grok shows φ⁻³ = 2φ−3 and that powers of φ occur, but "does not show why
the chirality magnitude must specifically be φ⁻³ rather than φ⁻¹, φ⁻², φ⁻⁴, (2−φ),
1/√5…" → "plausibly emergent, but not yet actually derived."
- **E19** — Grok's sgn(n̂·(displacement×polarization)) "is a reasonable construction…
but it is not a derivation": it introduces displacement, polarization, a cross
product, and a capture rule "without showing that these are already present in the
registered framework. The difficult part is exactly the step that is omitted." Agrees
E19 stays unregistered.
- **F2 / temporal primitive** — raises a distinct subtlety: the temporal primitive may
be "ordered process" rather than "T-asymmetry" — ordered sequence ≠ irreversible
sequence. "A subtle but real classification issue… not a falsifier… but also not
fully settled." (The audit half-acknowledges this via OPEN-CHIR-2a.)

**Agreement with the cycle:** F3 undefeated (stronger agreement than its earlier
pass); spatial chirality "plausibly collapses to n̂" — n̂ appears to be the only
genuine spatial-orientation primitive, central reduction survives; no definite missing
row — earlier ZBW concern "remains only if ZBW is later shown to carry handedness…
from the material supplied here, I cannot make that case. So F1 survives."

**Proposed synthesis phrasing (verbatim):** "THEO-CHIR-AUDIT-1 succeeds as a
framework-audit theorem. No convincing F1, F2, or F3 falsifier has been produced. The
strongest remaining open points are not missing entries but derivational gaps: E19
(capture handedness) and E21 (χ = φ⁻³) remain plausible targets rather than
established reductions. The spatial-collapse-to-n̂ thesis survives review, and no
fourth operational chirality sense has been identified."

---

## Part 2: Cross-reviewer synthesis

**Bottom line: the audit is confirmed as a cataloging theorem. No reviewer produced a
falsifier (no missing entry per F1, no wrong entry per F2, no fourth sense per F3).**
The convergent finding is not a defect in the catalogue but an *overclaim in the
labeling*: the word "emergent" was used for two epistemically different situations —
rows with a registered derivation and rows where the derivation is only owed.

**Convergence map** (cross-reviewer weighting per `operating_system.md`: 2+ reviewers
= load-bearing):

| Finding | Copilot | Grok | ChatGPT | Weight |
|---------|---------|------|---------|--------|
| "emergent" overclaims for derivation-owed rows (esp. E21) | **flags** | permissive | **flags** | **load-bearing (2/3)** |
| ZBW circulation sense missing / unargued | **flags (candidate)** | — (sub-structure) | flags (conditional, earlier) | moderate (1.5/3) |
| E20 "emergent*" pre-commits to Scenario A | **flags** | — | — | single (consistency fix) |
| Temporal primitive = ordered vs irreversible | — | — | **flags** | single (clarify) |
| F1 completeness survives | yes | yes | yes | **unanimous** |
| F3 no fourth sense | yes | yes | yes | **unanimous** |
| Spatial → n̂ reduction survives | yes (as hypothesis) | yes | yes | **unanimous** |
| E16 primitive, E19 unregistered correct | yes | yes | yes | **unanimous** |
| E19/E21 not actually derived | yes | (sketches only) | yes | **load-bearing (Grok's sketches are not derivations)** |

**On Grok's contribution sketches:** ChatGPT's calibration is correct and is adopted.
Grok's E21 sketch does not fix the *exponent* (−3 vs other φ-powers); its E19 sketch
introduces displacement/polarization/capture-rule terms not shown to be already
registered. They are recorded as **seeds for OPEN-CHIR-1d (E21) and OPEN-CHIR-1c/2d
(E19)** — useful starting structures, not closures. The classifications are not
upgraded on their strength.

---

## Part 3: Triage decisions (applied as artifact v1.1, Patch 0634)

Per the package §7 triage order (F1 > F2 > F3 > confirmations):

1. **F2 — emergent grading (load-bearing).** Introduce a two-grade reading of
   *emergent*: **emergent (established)** = a registered derivation exists at some
   layer (E22, E23 via SD-CHIR-1/2; E24 via DSL-3 sketch-L3; E25 via CONT L4);
   **emergent (provisional)** = structurally reducible to n̂ + geometry + dynamics with
   no second primitive apparent, derivation owed and registered as an OPEN-CHIR target
   (E12, E13, E14, E15, E21, E26, E27). This gives Copilot/ChatGPT the honesty they ask
   (no claiming un-written derivations) and preserves Grok's valid distinction
   (provisional-emergent rows are *not* the same as the deep E19 gap). Category
   definition in §1 Q2 and the synthesis table/tally updated; the headline spatial
   reduction is restated as a **programme hypothesis** for its provisional part.

2. **E20 — consistency fix.** Reclassify E20 from "emergent*" to **unregistered
   (conditional: emergent under Scenario A, primitive under Scenario B)** in the table
   itself, keeping the footnote. Aligns the category with the audit's own no-pre-commit
   stance (exclusion X2).

3. **F1 — ZBW registered as a deferred exclusion (anti-erasure).** Not a confirmed
   falsifier (Grok: sub-structure; ChatGPT: conditional). But the silent exclusion is
   closed: add exclusion **X5** stating the audit defers ZBW circulation chirality
   pending the ZBW dynamical specification, and register **OPEN-CHIR-2e** (determine
   whether ZBW carries a handedness; if non-chiral, argue it; if chiral, add the
   entry). This converts an unargued exclusion into a registered open question without
   overclaiming.

4. **Temporal — ordered vs irreversible (clarify).** Add a remark at D1 / the
   load-bearing finding: the temporal primitive E2/E5/E17 is the **ordered** PCD
   sequence; its **irreversibility** (T-asymmetry) is the separately-registered
   unregistered gap (OPEN-CHIR-2a). Ordered ≠ irreversible; the audit classifies the
   ordering as primitive and the asymmetry-assertion as owed.

5. **F3, central reductions, E16/E19, no-chirality rows — confirmed, no change.**

**Status outcome:** THEO-CHIR-AUDIT-1's "pending multi-AI review" qualifier is
removed. New status: **RESOLVED — multi-AI review complete (no falsifier); v1.1
calibration applied.** The OPEN-CHIR-* programme proceeds to its first downstream
theorem, THEO-CHIR-PCD-ORIENTATION-1 (OPEN-CHIR-F1-LINK).

---

---

## Part 4: v1.1 re-review — cycle close (added Patch 0635)

After v1.1 shipped (Patch 0634), ChatGPT was given the revised artifact for a re-review.

**ChatGPT, v1.1 re-review — verdict (verbatim):** "CONFIRMED with v1.1 calibration accepted."
The revised theorem addresses its prior concerns: emergent-established vs emergent-provisional
distinguished; E19/E21 kept as owed derivations rather than completed reductions; E20
reclassified conditional/unregistered; ZBW added as exclusion/open target X5 rather than
silently omitted. Falsifier check: **F1** — no confirmed missing row (ZBW handled as X5 /
OPEN-CHIR-2e); **F2** — passes after v1.1, labels now honest (E21 emergent-provisional, E19
unregistered, E20 conditional, PCD ordering separated from T-asymmetry); **F3** — no fourth
sense. Remaining caution (accepted): the theorem should keep calling itself a *cataloging*
theorem, not a *derivation* theorem — which v1.1 does correctly (provisional rows are
derivation targets, not established reductions). Overall: "v1.1 resolves the review objections
without overclaiming."

**Cycle outcome: 3/3 reviewers positive on v1.1.** Grok confirmed at v1.0; Copilot's and
ChatGPT's v1.0 concerns were the basis of the v1.1 calibration and are now resolved (ChatGPT
explicitly CONFIRMED on v1.1; Copilot's items — emergent overclaim, E20 pre-commit, ZBW — were
all applied). The THEO-CHIR-AUDIT-1 multi-AI review cycle (Patches 0633→0635) is **closed**.
No further calibration pending. The OPEN-CHIR-* programme proceeds; the first downstream
theorem THEO-CHIR-PCD-ORIENTATION-1 is scoped at Patch 0635
(`chirality_derivations/sketches/theo_chir_pcd_orientation_1_scope.md`).

---

*Review record closed at Patch 0635. The accepted caution — "cataloging theorem, not derivation
theorem" — is carried forward: THEO-CHIR-AUDIT-1 stays a catalogue; the derivations it spawns
(THEO-CHIR-PCD-ORIENTATION-1 first) are the separate downstream theorems, each claimed at its
own honest layer.*
