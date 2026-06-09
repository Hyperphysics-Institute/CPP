# Threshold Reconciliation: Both Channels Cleared — Conservative Margin 44%, Favorable 80% (correcting both 0824 and 0912's framings)

**Patch:** 0825 (Session 156, 8 June 2026) · **Type:** reconciliation / infrastructure · **Lane:** F.1 / `dynamical_substrate_law/` (verdict + DG-3 package stay chirality-lane).
**Why:** the chirality lane's DG-3 package (0912) was built on 0823's framing (uniform `K_c`, "staggered orthogonal", margin 42–47%); my 0824 then used the AFM/staggered threshold (margin 80%). These give different margins and contradictory framings. Before the swarm fires, the honest synthesis must be settled. **Verify:** `code/0825_threshold_reconciliation.py`.

---

## The honest synthesis

The lifted η-field's effective coupling has **robust magnitude** `|K_lift| ≈ 0.053` and a **sign that is convention-dependent** (flagged in 0820). `η=0` (the symmetric, primitive state) is stable iff `|K_lift|` is below the *binding* threshold — and which mode binds depends on the sign:

| coupling sign | binding mode | threshold `K_c` | margin |
|---|---|---|---|
| FM (`K>0`) | uniform (`λ_max = 12`) | `1/12 ≈ 0.083` (mf); **≈ 0.095 (true)** | **≈ 44%** |
| AFM (`K<0`, measured) | staggered (`λ_min = −3.71`) | `1/|λ_min| ≈ 0.27` | **≈ 80%** |

`|K_lift| = 0.053` is **below both** thresholds (0.095 and 0.27). So **`η=0` is stable regardless of the coupling sign → η disordered in all modes → primitive, robustly.**

- **Conservative margin ≈ 44%** — against the uniform/FM threshold, which is the *smallest* (since `λ_max` is the largest eigenvalue) and therefore binds for the worst-case sign. **This is the honest headline for the swarm.**
- **Favorable margin ≈ 80%** — against the AFM/staggered threshold, valid for the measured (convention-dependent) sign. Reinforcing, not load-bearing.

## Correcting both prior framings

- **0912 / 0823 ("staggered is orthogonal to V1", uniform `K_c` only).** The *number* (42–47%) is right — it is the conservative margin (uniform = smallest threshold = binds for the worst-case sign). But the *justification* is not quite right: a staggered order **does** break the η→−η (det-coset ℤ₂) symmetry — the two staggered domains are swapped by the global flip — so it is a genuine ordering channel, not orthogonal. The cleaner statement is **"both channels cleared,"** which is also a *stronger* answer to a sharp reviewer (the package's own Q3 probes exactly this).
- **My 0824 ("AFM threshold is THE correct one, 80%").** That is the **favorable** case (it trusts the convention-dependent AFM sign), **not** the conservative margin. I over-framed it as a correction of 0823. The honest status: 0824 supplies the *staggered-channel clearance* (80%), complementing — not replacing — the conservative uniform-channel margin (44%).

## What the swarm package should say

Replace "staggered orthogonal, margin 42–47%" with: **"`|K_lift| = 0.053` is below both the uniform (≈0.095) and staggered (≈0.27) thresholds → η disordered in every mode → primitive. Conservative margin ≈ 44% (uniform, robust to the convention-dependent sign); the measured AFM sign clears the staggered channel at ≈ 80%."** This is robust to the sign convention and preempts the Q3 challenge. The verdict is unchanged (primitive); only the framing is tightened.

## Status

The verdict conclusion is **unchanged and robust** (primitive; η below all thresholds). What changed is the *framing* of the margin: conservative 44% (headline) + staggered cleared at 80%, in place of either "staggered orthogonal" (0912) or "AFM is the threshold" (0824). **Recommendation: the chirality lane should fold this synthesis into the DG-3 package (0912) before firing the swarm.**

## Scope held

Infrastructure / reconciliation. **No verdict moved** (V3/V1 stays chirality-lane, DG-3). No THEO, no ID, no CHIR.md / verdict-registry edits. Corrects the margin *framing* in 0824 and flags the framing in 0912 for the chirality lane to incorporate. Conditional on Mechanism A (OPEN-FP-F1-2).
