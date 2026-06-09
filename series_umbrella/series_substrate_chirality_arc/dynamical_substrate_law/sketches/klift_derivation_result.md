# K_lift Derivation — the Verdict Reduces to the η-Field's Shared-d.o.f. Structure (Same Order as K_c)

**Patch:** 0819 (Session 156, 8 June 2026) · **Type:** infrastructure result (season opener) · **Lane:** F.1 / `dynamical_substrate_law/` (verdict stays chirality-lane / DG-3).
**Predecessor:** the §14.17/H1 reframe (0818). **Verify:** `code/0819_klift_derivation.py`.

---

## What this computed

0818 reduced the entire chirality verdict to one comparison, `sign(K_c − K_lift)`, and computed the threshold `K_c = 1/12`. This patch attacks the other half: **derive `K_lift`**, the lift-induced η–η coupling. Model the lifted η-field as `η_v = sign(g_v)` with `g_v` an orientation-weighted sum of the i.i.d. local substrate d.o.f. that `η_v` reads; for a Gaussian base `⟨η_v η_w⟩_c = (2/π)arcsin(ρ_vw)`, and the effective coupling is `K_lift = arctanh(C_nn)` (mean-field map), with `ρ_nn` set by the **shared-d.o.f. fraction** between neighbours.

## The finding (honest, and it corrects my own earlier heuristic)

1. **`K_lift` is the same order as `K_c`** — both `~1/z` (`z = 12`). My earlier "`K_lift ≪ 1/12` ⇒ comfortably primitive" lean (0818) was **wrong**: this is a genuine knife-edge, not a parametric blowout.

2. **The verdict hinges on the η-field's shared-d.o.f. structure**, which has two knobs:
   - **Reading radius (edge d.o.f., 1 shared edge of `m_read`):** crossover at **`m_read ≈ 8`** — `m_read < 8` → `K_lift > K_c` → **emergent (V1)**; `m_read ≥ 8` → **primitive (V3)**. At the full vertex figure `m_read = 12`, `K_lift/K_c ≈ 0.64` (primitive).
   - **Edge- vs vertex-d.o.f.:** if `η` instead reads neighbour *states* (adjacent vertices share 5 common neighbours), `K_lift/K_c ≈ 3.4` → **emergent**.

3. **The registry actualization leans primitive — but only leans.** 0906's actualization is the **edge pattern `ε(ê·n̂)` on the 720 edges**, read over the full vertex figure — i.e. the **edge / `m_read = 12`** case → `K_lift/K_c ≈ 0.64` → primitive. So the registry-grounded reading favours primitive (V3), consistent with 0813's favourable χ. But it is a *lean*: a more-local or vertex-based effective η would cross to emergent.

## What this means for the season (and the maximal reduction reached)

The verdict is now reduced to **one sharp quantity: the effective η-field's shared-d.o.f. structure (equivalently `K_lift`)**, against a known threshold `K_c = 1/12`. That is the maximal reduction reachable **without** the effective action — the comparison is computed, the threshold is computed, and the only remaining unknown is which effective η-field the dynamics actually produces (its d.o.f.-structure / `K_lift`).

**Pinning that is the §14.17 content** — the effective-action computation that says whether the coarse-grained Mechanism-A dynamics yields the full-vertex-figure edge-pattern η (`m≈12`, primitive) or a more-local / vertex-weighted one (emergent). The next probe is whether *that* coarse-graining is itself a tractable calculation (given Mechanism A) or whether it needs physical insight about the η-field — i.e. whether this is where the PCD layer is finally required. We do not yet know; we have localized the question to the single place where it would be decided.

## Honest status

- **Not a verdict.** `K_lift ~ K_c` with a primitive *lean* on the registry actualization; the verdict (V3/V1) stays the chirality lane's (DG-3). I assert no verdict here.
- **The favourable lean is real but fragile** — it rests on the η-field being the edge-pattern full-vertex-figure indicator, which the lift must confirm.
- **Mean-field map.** `K_lift = arctanh(C_nn)` vs mean-field `K_c = 1/12` is an order-of-magnitude/level-consistent comparison; the true crossover could shift, but the structural finding (same order; hinges on d.o.f.-structure) is robust.
- Conditional on Mechanism A (OPEN-FP-F1-2) throughout.

## Scope held

Infrastructure (`K_lift` derivation + the reduction); no verdict moved, no THEO, no ID, no CHIR.md / verdict-registry edits. Coordinated with the chirality lane; verdict extraction (`K_lift` vs `K_c` → V3/V1) is theirs.
