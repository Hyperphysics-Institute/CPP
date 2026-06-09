# DG-3 Review Scaffold — THEO-CHIR-CAPACITY-1 (prepared in advance; NOT yet live)

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/dg3_capacity_1_review_scaffold.md`
**Patch:** 0910 · **Type:** review scaffold (verdict-side prep). **Status: NOT a verdict, NOT a review run.** This is the prepared CONV-001 package that **fires only when conditions C1–C3 (below) close** via the F.1 residuals. Until then V3/W3 stand, THEO-CHIR-CAPACITY-1 stays **reserved**, header count unchanged, OPEN-CHIR-1d-β / OPEN-SM-4 stay OPEN.

---

## 1. The claim to be reviewed

**THEO-CHIR-CAPACITY-1 (proposed).** *The substrate does not spontaneously break the vectorial det-coset ℤ₂ (H₄→H₄⁺): the effective enantiomorph field η is disordered (no ordering instability at any wavevector), equivalently μ²>0, equivalently |K_lift| below the relevant critical coupling. Therefore the observed substrate chirality FI-C-9 is **not dynamically generated** — it is a **genuine irreducible primitive (Foundational Input)**.*

**Verdict it would set:** spatial **V3 confirmed, V1 (emergence-by-condensation) excluded.** (Temporal W-axis untouched; OPEN-SM-4 / cross-sector V2-reopener untouched.)

**Framing guard (non-negotiable, the recurring trap):** μ²>0 / off-critical is the **UNBROKEN** branch ⇒ chirality **primitive**, **not** emergent. The *emergent* outcome is the opposite branch (μ²<0 / ordered / V3→V1). Any review wording that reads "off-critical ⇒ emergent" is the inversion and must be rejected.

**What it does NOT claim:** it does **not** derive FI-C-9 (that would be V1); it **confirms FI-C-9 as primitive**. It is a *status* theorem (settles whether chirality is derivable), not a new prediction.

## 2. The three conditions (theorem hypotheses) — each discharged by an F.1 residual

The claim goes live only when all three close. Each has a slot for the discharging result:

| # | Condition | What must be shown | Discharged by | Status |
|---|-----------|--------------------|---------------|--------|
| **C1** | **Dynamical = geometric η** | The dynamically-selected effective η (the coarse-grained slow / order-parameter mode of Mechanism A) **is** the canonical symmetric 12-neighbour vertex-figure indicator — derived, not assumed. (Doubly-grounded target: 0820 geometric canonicity + review-closed CHI-1 locality.) | F.1 residual 1 (slow-mode identification) | ⏳ PENDING |
| **C2** | **No current-induced ordering** | The O(δ³) NESS current neither (a) shifts the effective critical coupling to/below \|K_lift\|, nor (b) drives a non-equilibrium (staggered/current-driven) ordering of η the equilibrium analysis misses. | F.1 residual 2 (current check in the NESS) | ⏳ PENDING |
| **C3** | **Off-critical at all wavevectors** | \|K_lift\| lies below the **correct critical coupling** for the actual ordering mode — note the coupling is **antiferromagnetic**, so the relevant instability is the staggered mode (≈1/\|λ_min\|), not the uniform mean-field 1/12; and AFM order on the frustrated icosahedral/600-cell lattice is shown suppressed. | F.1 residual 3 (frustrated-AFM + beyond-mean-field K_c) | ⏳ PENDING (MF lean: \|K_lift\|/K_c≈0.65) |

**Standing conditionalities (carried into the verdict, not dischargeable here):** conditional on **Mechanism A (OPEN-FP-F1-2)**; all bridge-side statements inherit **BRIDGE-1's kinematic / premise-P2 cap**; the CPT-unified V2-reopener (**OPEN-SM-4**) is untouched and remains the sole cross-sector route that could later reopen the sign.

## 3. The logical chain to be audited

`C1 (η is the vertex-figure field)` + `C3 (|K_lift| < relevant K_c)` ⇒ η disordered ⇒ **no spontaneous H₄→H₄⁺ breaking** ⇒ **μ²>0** ⇒ **V3 confirmed / V1 excluded**, with `C2` guaranteeing the O(δ³) current does not overturn the equilibrium conclusion. Two convergent supports (either alone suffices for no-spontaneous-breaking): the **off-criticality route** (disordered phase, ⟨η⟩=0) and the **VW-1 route** (if the measure is reflection-positive, the vectorial parity cannot break). The off-criticality route is primary; VW-1 is the corroborating no-go (and the route C2 protects, since a current can break reflection positivity).

## 4. Swarm-review question set (CONV-001; reviewers = ChatGPT + Grok + Copilot)

- **Q1 (central — the η-identity).** Does C1 *establish* that the dynamical effective η is the vertex-figure object, or assume it? Is the 0820-canonicity + CHI-1-locality double-grounding sufficient, or is a more-local dynamical η still admissible? *(Analogue of STATUS-1 Q1; the sharpest question — the whole verdict pivots here.)*
- **Q2 (the current).** Is C2 genuinely shown — is "negligible by O(δ³) smallness" replaced by an actual check for staggered/current-induced ordering and for an effective-K_c shift? Is the VW/reflection-positivity route correctly flagged as the one that could fail under a current?
- **Q3 (the comparison).** Is C3 sound with the **correct** critical coupling — AFM/staggered mode, frustrated-lattice, beyond mean-field — not just the uniform 1/12? Is AFM non-ordering on the frustrated lattice established rather than asserted?
- **Q4 (the logic + the framing guard).** Is the chain in §3 valid, and is the **primitive (not emergent)** reading correct? Explicitly: confirm no inversion (μ²>0 ⇒ primitive).
- **Q5 (scope/honesty).** Is the Mechanism-A conditionality correctly stated; does the claim avoid overclaiming (confirms primitive, does not derive); are the temporal axis, BRIDGE-1 P2 cap, and OPEN-SM-4 correctly left untouched?

## 5. DG-3 pass criteria + consequences of a PASS

**Pass:** 3/3 reviewers CONFIRM (no falsifier), C1–C3 each discharged by a cited F.1 result, Mechanism-A conditionality stated. Wording calibrations allowed without re-review (per VW-2 / TARROW-2 precedent) provided no verdict/statement change.

**On PASS, enact (separate patch, post-review):** register **THEO-CHIR-CAPACITY-1** (claim §1); set spatial verdict **V3 confirmed / V1 excluded** in CHIR.md; **resolve OPEN-CHIR-1d-β** as *V1 excluded — chirality is a confirmed primitive* (the V1-upgrade question closes NO); state the result is **conditional on Mechanism A** and reopenable only via OPEN-SM-4 (cross-sector). **Header prediction count:** unchanged (status theorem, not a new prediction) — to be confirmed at enactment.

**On FAIL / RESTATEMENT:** apply calibrations or, if a condition is not in fact established, return to the relevant residual; V3/W3 stand meanwhile.

## 6. CONV-001 presentation (how this fires)

When C1–C3 close, build the reviewer package per CONV-001: one 4-backtick-fenced copy-paste block **per reviewer**, containing (1) GitHub blob + raw links to this scaffold, the CAPACITY-1 statement, and the discharging F.1 result patches; (2) the one-paragraph intro stating the ask ("adjudicate THEO-CHIR-CAPACITY-1 against Q1–Q5; confirm or falsify; the verdict-moving claim is V3-confirmed/V1-excluded conditional on Mechanism A"); (3) the full rendered Markdown (not patch/diff). Template: `templates/presentation_file.md`.

## 7. Scope held

Prepared scaffold only. **No verdict, no THEO registered, no ID consumed, no CHIR.md verdict edit, no review run, no count change.** Fires solely when C1–C3 are discharged by the F.1 residuals. V3/W3 stand; THEO-CHIR-CAPACITY-1 reserved; conditional on Mechanism A (OPEN-FP-F1-2).
