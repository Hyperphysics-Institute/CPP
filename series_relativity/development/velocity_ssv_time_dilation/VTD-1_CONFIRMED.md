# VTD-1 — FOUNDER-DELEGATED CONFIRMATION: PASS at SR-1 strength (linear excluded, f_eff unique)

**Patch:** 2038 (22 June 2026) · **Window:** 2000-band · **Status: VTD-1 PASS at SR-1 strength.**
**Authority:** the founder (TLA) judged the orthogonality question outside his intuition and **delegated the
confirm to the worker**, explicitly bounded: *"approve and proceed if your computation confirms this
conclusion."* This file records that delegated confirmation **and the exact boundary of what the computation
licenses.** **Verify:** `scripts/2038_vtd1_linear_excluded_feff_unique.py`.

---

## 1. What was delegated, and the bounded test it reduces to

The §5 hook of `VTD-1_RESOLUTION.md` asked the founder to confirm that the bulk-velocity budget cost is the
**quadrature** fraction f_eff = 1 − 1/γ (fixed-magnitude 4-displacement / invariant-4-velocity reading),
**not** a separate linear consumption. TLA delegated it on the condition that computation decide it.

Computation **can** decide the part that matters for the verdict, because it is an *exclusion*, not a free
mechanism choice. SR-1's exact time-dilation factor γ = 1/√(1−v²/c²) is **externally validated** (A− review;
Appendix H characterises f_eff = 1 − 1/γ as the unique consistent consumed fraction). Treat that validated γ
as the datum and ask which budget reading reproduces it:

| reading | consumed fraction | internal clock rate | matches validated γ? |
|---|---|---|---|
| LINEAR (collinear) | v/c | 1 − v/c | **NO** — gives γ = 1/(1−v/c), a different, falsified factor |
| QUADRATURE = f_eff | 1 − 1/γ | √(1−v²/c²) = 1/γ | **YES** |

**Uniqueness (not a tie-break, a forcing):** demand internal rate = 1/γ (the validated datum); with
internal = 1 − f this gives f = 1 − 1/γ = f_eff, with **no free parameter**. The quadrature/f_eff reading is
the *unique* survivor; the linear reading is **excluded** (it predicts the wrong γ). Verified across
v/c ∈ {0.1 … 0.99} to 1e-12 (f_eff) and as a clean falsification (linear).

## 2. The confirmation (bounded, computation-backed)

**CONFIRMED:** the budget cost is the quadrature fraction f_eff = 1 − 1/γ, not the linear v/c. This is forced,
not chosen — the linear alternative contradicts SR-1's externally-validated exact-γ, and f_eff is the unique
fraction consistent with it. **VTD-1 therefore PASSES at SR-1 strength**, and R2's condition (i) is cleared at
that strength.

This is exactly the claim `VTD-1_RESOLUTION.md` made by reduction (quadrature ≡ f_eff ≡ energy-bridge); 2038
adds the *exclusion + uniqueness* that converts "reduces to an already-validated input" into "the only reading
consistent with the validated datum." No new physics is asserted; the linear competitor is simply ruled out.

## 3. The boundary — what this confirmation does NOT cover (carved out, on purpose)

The delegation was "if your computation confirms." Computation confirms the **exclusion** above. It does
**not**, and cannot, settle the **deeper substrate-mechanism** question:

> Does the PCD / Absolute-Moment cycle *literally* allocate bulk and internal displacement into orthogonal
> subspaces as a primitive geometric fact of how a Conscious Point moves — or is f_eff = 1 − 1/γ an
> **effective** partition that the substrate is merely required to reproduce (with the literal allocation
> mechanism still unspecified)?

That is a mechanism claim about CP dynamics; no numerical check decides it, and I do **not** approve it here.
Crucially, **R2 does not need it.** R2's velocity leg needs only the *effective* γ(v) to be exact — which
f_eff delivers at SR-1 strength. The literal-vs-effective question is a **refinement**, not a gate:

- it does not weaken VTD-1's PASS-at-SR-1-strength or R2's condition (i);
- it is the natural home for a later **founder's-voice capture** (TLA's mechanism intuition, when he has it)
  and/or a fold into OPEN-SR-9 territory (the substrate EM/displacement dynamics);
- registering it as open keeps the discipline honest: VTD-1 inherits **SR-1's** status (a validated effective
  factor whose primitive derivation is App.-H-acknowledged as an *identification*, not a geometric theorem) —
  no stronger, no weaker.

## 4. Honest standing after 2038

- **VTD-1: PASS at SR-1 strength** (linear excluded; f_eff unique-and-validated). Delegated-confirmed.
- **R2 condition (i): CLEARED** at SR-1 strength.
- **R2 overall: still conditional-PASS** — condition (ii) (medium-universality) is grounded but is precisely
  what the next CONV-001 round must stress; and the *deeper* substrate route (literal orthogonality /
  action-level Z₀) remains **OPEN-SR-9**. 2038 does not touch that; it does not upgrade R2 to unconditional.
- **NO THEO.** Conditional finding, owned greenfield path, frontier-tracked. No registry edit here.

### Proposed for integrator (batched, Tier-A — do not let a window edit)
- `mu_eps_closure/R2-STATUS.md`: condition (i) VTD-1 → CLEARED at SR-1 strength (2037+2038); R2 stays
  conditional-PASS pending (ii) review + the OPEN-SR-9 deeper route.
- `frontier_sectors/SR.md`: VTD-1 PASS-at-SR-1-strength; add the literal-vs-effective refinement as a noted
  open sub-item (non-gating), cross-linked to OPEN-SR-9.
- No `theorem-registry.md` / `predictions.md` edit (conditional; NO THEO).
