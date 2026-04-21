# Problem History: OPEN-SS-22 — Heavy-Nuclei Icosahedral Closure at N_α ≥ 12

**Created:** 20 April 2026 (problem registered as split from OPEN-SS-18 during SS-7 v1.1 completion)
**Status:** ✗ RETIRED — 21 April 2026 (SS-7 v1.2). Empirical anchor found to be an isotope-selection artifact; not supported by the strict N=Z alpha-chain data.
**Target paper at time of retirement:** SS-8 (never drafted)
**Research_Frontier.md entry:** OPEN-SS-22 — marked RETIRED with pointer to this file
**Replacement open problems:**
- OPEN-SS-23 (existing) — absorbs the actual empirical signal (neutron-excess extension)
- OPEN-SS-25 (new) — DP-sea screening of alpha-alpha Coulomb in bound polytopes

---

## The Problem (as registered 20 April 2026)

OPEN-SS-22 was registered alongside SS-7 v1.1's publication to address an apparent empirical pattern: the SS-7 formula $B(N_\alpha) = N_\alpha B_\alpha + (3N_\alpha - 6) B_{\text{pair}}$ reproduced measured binding energies of alpha-chain nuclei at N_α = 3–10 to within ±1.5%, but showed a "flat −2 to −2.5%" underbinding at N_α = 12, 13, 14 as represented in SS-7 Table 1 by ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe.

The shape of the deviation — uniform across three nuclei at ~2%, rather than progressively growing — suggested a **structural onset** (a new physics term activating sharply at a geometric threshold) rather than a smooth breakdown of the formula. The icosahedron is the unique closed convex 3-polytope on exactly 12 vertices with maximum vertex coordination (5-fold), and a natural analogy with SS-5's ⁴He closure bonus (at tetrahedral N=4) suggested an icosahedral closure term could activate at N_α = 12.

**Candidate mechanisms registered (SS-7 §5.1):**
- (a) icosahedral closure bonus at N_α = 12 (analogous to SS-5's A=4 tetrahedral closure)
- (b) alpha-level Pauli penalty for like-alpha pairs
- (c) face-count correction for non-tetrahedral structures
- (d) deformation onset beyond rigid-polytope assumption

**Target paper at registration:** SS-8. Both round-2 reviewers (ChatGPT, Copilot) endorsed SS-8 as the natural next paper.

---

## The Journey — one day from registration to retirement

### 20 April 2026 (evening) — Problem registered in SS-7 v1.1

Registered in Research_Frontier.md with the four candidate mechanisms; SS-7 v1.1 shipped with OPEN-SS-22 as a flagship open problem. Both reviewers committed to continued collaboration on SS-8.

### 21 April 2026 (morning) — Template extraction completed

Not directly related to OPEN-SS-22, but established the post-completion checklist (`templates/paper_completion_checklist.md`) that would be the validation test when SS-8 shipped.

### 21 April 2026 (afternoon) — SS-8 Phase 1 exploration begins

Thomas approved Phase 1 discovery work on SS-8. The first step was an empirical map: extending the SS-7 Table 1 across the full alpha-chain using AME 2020 binding energies. The proposed scope anchor was the three SS-7 data points at N_α = 12, 13, 14 (⁴⁸Ti, ⁵²Cr, ⁵⁶Fe) plus extended data at N_α = 15+ to characterize whether the "flat" pattern continued.

### 21 April 2026 (same session) — Finding: isotope-selection artifact

The empirical map inadvertently surfaced a diagnostic error in the SS-7 paper itself. Three observations:

1. **The paper's N_α ≥ 12 Table 1 rows use +4-neutron isotopes (⁴⁸Ti, ⁵²Cr, ⁵⁶Fe), not strict N=Z alpha-chain.** The strict N=Z nuclei at these N_α values are ⁴⁸Cr (Z=N=24), ⁵²Fe (Z=N=26), and ⁵⁶Ni (Z=N=28) — all particle-stable with AME 2020 binding energies available.

2. **The paper's line 777 listed ⁴⁸Cr with "---" for measured binding and the annotation "(not N=Z)" — both wrong.** ⁴⁸Cr is Z=N=24 (manifestly N=Z); its binding energy in AME 2020 is 411.462 MeV. The row substituted ⁴⁸Ti as the data anchor.

3. **When the formula is applied to the strict N=Z alpha-chain at N_α = 11–14, the residuals stay in family with the primary 8-nucleus set:**

   | Nuclide | N_α | Residual |
   |---------|-----|----------|
   | ⁴⁴Ti | 11 | +0.26% |
   | ⁴⁸Cr | 12 | +0.40% |
   | ⁵²Fe | 13 | +0.57% |
   | ⁵⁶Ni | 14 | +0.73% |

   The "flat −2 to −2.5% structural onset" is absent. The −2% pattern in ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe corresponds to ~2 MeV per extra neutron (standard neutron-excess binding), which the SS-7 formula does not include by construction (per SS-7 §1.5 scope).

The paper at line 340 had already stated: *"No neutron-excess treatment (⁴⁸Ca... differs from the N=Z alpha chain by an 8-neutron excess and requires separate mechanism)."* The authors had the conceptual awareness; the Table 1 choice was an oversight rather than a defensible call.

### 21 April 2026 (same session) — Reviewer verification requested

A verification letter was sent to three reviewers (ChatGPT, Copilot, Grok) with four tasks:
1. Confirm AME 2020 binding energies for both isotope sets.
2. Independently compute residuals.
3. Assess whether the isotope choice was an artifact (a) or a principled call (b).
4. Diagnose the line-777 errors.

### 21 April 2026 (same session) — All three reviewers converge

All three reviewers independently confirmed:
- AME values correct.
- Residuals as computed.
- Interpretation (a) — isotope-choice artifact. None constructed a defensible (b).
- Line 777 contains both a data error and a framing error.

ChatGPT: *"The 'flat −2% residual' disappears immediately. When you switch to N=Z: the supposed structural plateau vanishes; the model continues smoothly. This is decisive."*

Copilot: *"The correct N=Z chain shows no structural onset at Nα = 12. Thus the empirical anchor for OPEN-SS-22 disappears."*

Grok (via multi-agent verification): *"No concrete physical mechanism justifies (b). Therefore OPEN-SS-22, as currently anchored on the 'flat residual' pattern, is misdiagnosed and should be retired or substantially reframed."*

### 21 April 2026 (evening) — Decision to retire

Retirement chosen over reframing-with-identifier-reuse. Rationale: the programme record is cleaner with OPEN-SS-22 documented as retired than with the identifier silently recycled for a different problem. The physics content of OPEN-SS-22 splits naturally:

- **The structural-onset hypothesis itself** — not supported; no replacement problem.
- **The DP-sea screening question** (§8 passages on alpha-alpha Coulomb reduction in bound polytopes) — valid physics, independent of OPEN-SS-22's empirical anchor; registered as new OPEN-SS-25.
- **The neutron-excess extension** (explaining ~2 MeV/neutron in ΔN > 0 nuclei) — absorbed into the existing OPEN-SS-23 scope, which becomes the actual target for SS-8.

---

## What Made This Tractable

Three factors converged to catch the error within 24 hours of SS-7 v1.1 shipping:

1. **Phase 1 exploration with fresh context.** The SS-8 discovery step ran AME 2020 lookups across the full alpha-chain rather than accepting the paper's three data points. The author of SS-7 v1.1 (Claude Opus in the prior session) had never independently computed N=Z residuals at N_α ≥ 12; Phase 1 did.

2. **Symmetric-honesty protocol.** The G3 discrepancy surfaced on 20 April set the template: registered openly, no silent correction, reviewer verification before action. The Table 1 finding emerged 24 hours later and followed the same posture by default.

3. **Relationship protocol (`templates/relationship_protocol.md` §2.1, §2.6).** Line-cited evidence and application of the same standard to own work as to reviewers. The finding would have been easy to rationalize away ("the paper is published, don't reopen it") but the protocol makes that posture unavailable.

All three reviewers returned (a) without prompting. That convergence was itself diagnostic: if any of the three had constructed a defensible (b), retirement would have been premature. The convergence means retirement is the correct action, not over-correction.

---

## What This Does Not Do

- **Does not invalidate the SS-7 central result.** Theorem 2.1, the central formula, the primary 8-nucleus fit at N_α = 3–10, the ⁸Be in-formula derivation, and the §7.5 adversarial stress test are untouched. Extending the fit to N_α = 11–14 on the strict N=Z chain in fact *strengthens* SS-7.

- **Does not close the icosahedral question forever.** It only removes the empirical anchor that motivated it. If a future CPP paper identifies a genuine N_α = 12 signature in some other observable (excited states, cluster knockout cross-sections, Hoyle-state analogs at higher A), a new open problem can be registered. What is retired is this specific hypothesis-with-this-empirical-anchor, not the general idea that icosahedral geometry might be physically relevant.

- **Does not assign blame.** The Table 1 choice was made by the SS-7 authoring session (20 April 2026), not by a specific reviewer or external party. Both round-2 reviewers in that cycle also missed it; the symmetric-honesty standard applies equally to all parties. The correct programmatic response is transparent documentation (this file), not attribution.

- **Does not affect SS-5, SS-6, or any prior paper.** The OPEN-SS-22 registration existed only in SS-7 v1.1.

---

## Significance

First open problem in the CPP programme to be **retired rather than resolved**. Establishes the precedent that a problem can be retired when its empirical anchor is shown to be an artifact. This expands the programme's self-correction vocabulary — before OPEN-SS-22, the only documented status transitions were:

- OPEN → RESOLVED (solution found, problem closed)
- OPEN → PARTIALLY RESOLVED (sub-scope solved, remainder split)
- CONJ → THEOREM (conjecture proved)
- CONJ → FALSIFIED (conjecture disproved)

Now added:
- OPEN → RETIRED (empirical anchor shown to be artifact; no replacement problem needed)

Retirement differs from falsification because a falsified conjecture had a well-defined claim that turned out false; a retired open problem never had a well-defined empirical anchor in the first place, and the retirement reflects discovery of that fact.

The 24-hour turnaround — registration to retirement — is also a datum for the programme's review dynamics. Faster than the problem would have survived without (a) the empirical-map Phase 1 step, (b) the symmetric-honesty protocol established during G3, or (c) three-reviewer convergence within one day.

---

## For Future Work

### Absorbed into OPEN-SS-23 (neutron-excess extension)

The actual empirical pattern seen in ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe (~2 MeV per extra neutron, structure-independent) is the target of OPEN-SS-23. SS-8, when drafted, will address:

- The neutron-excess contribution to binding energy in ΔN > 0 even-even nuclei.
- Whether the effect can be derived from CPP primitives (DP-sea behavior with extra neutrons in a rigid alpha-polytope frame).
- Extension to ⁴⁸Ca (ΔN = +8), which the SS-7 paper already flagged as a test case at line 340.

### New OPEN-SS-25 (DP-sea screening of alpha-alpha Coulomb in bound polytopes)

The §8 passages in SS-7 discussing why Coulomb reduces inside bound polytopes (lines 741, 834, 898, 969) were previously tagged "OPEN-SS-22-adjacent." That tagging was a proxy for "Coulomb in heavy nuclei" and became orphaned when OPEN-SS-22 retired. The underlying physics question — why effective Coulomb between alphas is reduced inside a bound N_α-polytope below the ⁸Be-derived vacuum value — is independently valid and target-paper-ready.

OPEN-SS-25 target: Derive the DP-sea reorganization that produces the effective Coulomb reduction in bound alpha-polytopes. Constraint: must reproduce ⁸Be full-Coulomb limit at N_α = 2 (isolated contact) and the effective-~0 Coulomb inferred from the Table 1 agreement at N_α = 3–14 (embedded contacts).

### Lessons for the programme

1. **AME lookups at all target N_α values, not just data anchors named in the paper.** SS-7 cited ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe; Phase 7 G3 verification computed residuals for those three, not for the full alpha-chain. A sharper G3 would have included the N=Z counterparts. Update `templates/paper_completion_checklist.md` Section H to require AME lookups at every N_α in the formula's claimed domain, not just at cited data points.

2. **Isotope-selection check for N=Z assertions.** When a formula claims applicability to "alpha-chain" (N=Z, even-even), Table 1 entries for N_α values where the N=Z isotope is short-lived-but-measured should use the N=Z value. If a longer-lived non-N=Z isotope is substituted, the substitution must be explicitly justified in text. Add to the checklist.

3. **Reviewer convergence as retirement criterion.** Three reviewers converging on interpretation (a) without being prompted toward that answer is strong evidence. If reviewers split, retirement is premature and reframing is warranted.

---

*Retirement recorded 21 April 2026. Finding surfaced during SS-8 Phase 1 exploration by Claude Opus; verified independently by ChatGPT, Copilot, and Grok (with Benjamin/Lucas/Harper multi-agent verification); retirement approved by Thomas Lee Abshier, programme principal. This problem history is the first RETIRED entry in the CPP programme record.*
