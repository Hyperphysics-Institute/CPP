# §14.17 / H1 — Independent Scoping + First Result: the Verdict Is One Coupling Comparison, and It Separates from the PCD Mechanism

**Patch:** 0818 (Session 156, 8 June 2026) · **Type:** scoping + infrastructure result · **Lane:** F.1 / `dynamical_substrate_law/` (shared lift infra; verdict stays chirality-lane / DG-3).
**Verify:** `code/0818_h1_critical_coupling.py`. **For:** coordination with the chirality lane's §14.17 scoping (0907 candidate), which this endorses and sharpens.

---

## What I endorse from the chirality-lane scoping

Their reduction is right and I am not re-deriving it: VW-1 (0680) reduced the verdict to one question — is the η-field measure reflection-positive / off-critical (H1)?; the NESS construction (0694) reduced that to the H-NESS lift; the lift scoping (0812) returned GO. The outer wall ("build the whole effective action") is not the wall. And the honest hedge is theirs and correct: 0813's finite χ was on the *idealized product base*; 0814 showed the real Mechanism-A measure departs from product, so the favorable branch is **not in hand** — the season's real work is establishing off-criticality for the **real** measure.

## The disentanglement I want to add (it bears on "how far without Thomas's insight")

The chirality lane called proving H1 "a physics-judgment / PCD-mechanism task." I think that bundles two separable things:

- **Deriving Mechanism A from A1–A11** (OPEN-FP-F1-2) — *this* is the PCD-mechanism creative task. It is upstream, and it is a standing conditionality already.
- **Establishing H1** (off-criticality / reflection-positivity of the measure **given** Mechanism A) — this takes the rate law `r₀(1+δê·n̂)` as given and asks a property of the resulting measure. It is a **measure / coupling calculation**, not a mechanism invention.

H1 does **not** require deriving Mechanism A. So the H1 attack can be pushed substantially without the PCD insight; the PCD layer is needed only for the *separate* OPEN-FP-F1-2, which doesn't gate the verdict.

## The concrete reframe + first result (verify 0818)

Model the lifted η-field measure as an Ising-type measure on the 600-cell: `η_v ∈ {±1}` (local enantiomorph), achiral symmetric base, lift-induced coupling `K`. Then the Landau/VW-1 structure is literal:

- **K < K_c** → disordered, finite χ, `μ² > 0`, `η=0` stable → **chirality PRIMITIVE (V3)**.
- **K > K_c** → spontaneous η condensation, `μ² < 0` → **chirality EMERGENT (V3→V1)**.

So the entire verdict is **one comparison: `sign(K_c − K_lift)`.** The threshold is computed now:

- 600-cell adjacency is degree-12 regular, `λ_max = 12`, so the mean-field/RPA critical coupling is **`K_c = 1/λ_max = 1/12 ≈ 0.0833`**. The RPA susceptibility `χ(K) = (1/N)Σ_i 1/(1−Kλ_i)` is finite below and diverges at `K_c` (verify 0818: χ = 1.00 → 1.35 → diverges as K: 0 → 0.96 K_c → K_c). Fluctuations raise the *true* `K_c` above mean-field, so the off-critical (primitive) window is **at least** `K_lift < 1/12`, and in reality wider.

`K_c` is done and mechanical. **`K_lift` — the lift-induced η-η coupling derived from the Mechanism-A NESS — is the season's target,** and it is a calculation given Mechanism A, not a PCD invention.

## The one honest risk node (theirs, which I keep)

Deriving `K_lift` from the real (non-product, current-carrying) lift — or proving reflection-positivity analytically rather than estimating `K_lift` numerically — *might* bottom out at a place where physical insight about the measure's structure is needed. The VW-1 review flagged that full H1 "may still touch §14.17." The scoping cannot pre-decide this. What it can say: the question is now sharp and singular (one coupling vs one threshold), the threshold is in hand, and the remaining step is a coupling-derivation, not a mechanism-invention. We find out whether *that* step needs insight by attempting it — and surface the PCD requirement only if it becomes the genuine sole remaining path.

## Heuristic lean (NOT a verdict)

0813's achiral base has `⟨η⟩ ≈ 0` (no bare alignment) and the bias is O(δ)-weak, so `K_lift` is plausibly `≪ 1/12` → off-critical → primitive (V3), consistent with 0813's favorable finite χ. The season's job is to *derive* `K_lift` and confirm or refute this — not to assume it.

## Recommendation (for the go/no-go)

**Openable, and openable largely without Thomas's PCD insight** — because the decisive remaining step is `K_lift` (a coupling-derivation given Mechanism A), separable from the PCD mechanism (OPEN-FP-F1-2). Division of labor: **this window drives the H1 measure/coupling infrastructure** (`K_c` done; `K_lift` next — re-run the 0813/0814 machinery on the real measure to extract the effective coupling and attempt the RP argument); **the chirality lane owns the verdict** (`K_lift` vs `K_c` → V3/V1 via VW-1, DG-3). Thomas's creative PCD layer is held in reserve for the one risk node, surfaced only if `K_lift`/RP genuinely bottoms out there.

## Scope held

Infrastructure + scoping only. `K_c` is a lattice computation; the verdict (V3/V1) stays the chirality lane's (DG-3) — not moved here. No THEO, no ID, no CHIR.md / verdict-registry edits. Conditional on Mechanism A (OPEN-FP-F1-2) throughout. Endorses and coordinates with the chirality lane's §14.17 scoping.
