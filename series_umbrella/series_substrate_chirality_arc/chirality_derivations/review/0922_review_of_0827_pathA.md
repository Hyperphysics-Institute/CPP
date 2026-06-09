# Chirality-lane review of 0827 (Path-A weight-concentration closure): **conclusion survives, but the proof has a real gap — do NOT re-fire as written**

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0922_review_of_0827_pathA.md`
**Patch:** 0922 · **Type:** chirality-lane review/assessment of the F.1 result 0827 (verdict + DG-3 + CAPACITY-1 are chirality-lane). **Verify:** independently re-derived; counterexample + fix reproduced on the real 600-cell. Script (added Patch 0929): `chirality_derivations/code/0922_nhat_concentration_counterexample.py`.
**Disposition:** 0827's **conclusion** (Path A closes; η-identity dissolved for the verdict; outcome 1, PCD not called) is **very likely correct**, but its **load-bearing argument is falsified by an explicit counterexample**, and its stated admissibility condition (*mean* / "homogeneous + p>1") is the **wrong** one. The correct condition is a **pointwise** participation floor, under which the closure holds empirically with ≈36% margin — but a clean closing bound is **not yet written**. **Recommendation: do NOT re-fire on 0827 as-is; return to F.1 for the corrected (pointwise) closure.** No verdict moved; V3/W3 stand; CAPACITY-1 reserved.

---

## 1. What 0827 gets right (confirmed)

- **The shared-edge-only coupling (0826) and the per-link sign law** carry over; not re-litigated.
- **The AM–GM / chord average bound is rigorous and correct.** `(2/π)arcsin(z) ≤ z` (arcsin convex ⇒ below its chord), so
  `Σ_v RowSum_v ≤ Σ_edges 2·c^v c^w ≤ Σ_edges (c^v²+c^w²) = Σ_v Σ_{e∈recip} (c^v_e)² ≤ Σ_v 1 = N.`
  So the **average** row sum ≤ 1 for *any* normalized weighting, equality only at full single-edge concentration. **Verified.** This is a genuine, general result.
- **The instinct that vertex-transitivity is what tames the loose ≈1.7 adversary is correct.** The loose adversary (every neighbour of `v` concentrates onto `v`) needs in-degree 12 at one vertex and is non-homogeneous; it is rightly excluded.

## 2. The gap (load-bearing) — "homogeneity ⇒ max = avg" is false for the physical η

The closure needs the **maximum** row sum < 1 (since `ρ(M) ≤ max_v RowSum_v`), and 0827 gets there via *"a single translation-invariant rule on the edge-transitive 600-cell gives every vertex the same row sum, so max = avg ≤ 1."* **This step does not hold for the physical, n̂-dependent η.**

- A *strictly* H₄-invariant rule must, by the 600-cell's **edge-transitivity**, assign **equal** weight magnitudes to all edges → `p = m = 12` (no concentration). Under that reading, the weighted-concentration class ChatGPT raised is simply *out of scope* — i.e. this is Path B (scope-narrowing), **not** a universal closure.
- A rule that is "the same functional form at every vertex" but **depends on the fixed direction n̂** (as the chirality observable does — η is `sign(det[·, n̂, ·, ·])`) is **not** H₄-invariant. Its row sums are **not equal**, so `max ≠ avg`.

**Explicit counterexample (reproduced on the real 600-cell).** Homogeneous rule "weight edge `e` at `v` by `|dir_e·n̂|^γ`, normalized," same form at every vertex:

| rule | mean p | avg row sum | **max row sum** | **ρ(M)** |
|---|---|---|---|---|
| equal weight (γ=0) | 12.0 | 0.637 | 0.637 | 0.637 |
| n̂=(1,1,1,1), γ large | **2.60** | 0.573 | **1.000** | **1.000** |
| n̂=(1,φ,φ²,φ³), γ large | 1.17 | 0.600 | 1.000 | 1.000 |
| n̂ random, γ large | 1.07 | 0.600 | 1.000 | 1.000 |

The average bound holds (≈0.60 ≤ 1) exactly as 0827 proves — but `max/avg ≈ 1.67`, and **ρ(M) reaches 1 at mean participation p ≈ 2.6**, far above the degenerate `p=1`. *Mechanism:* the n̂-extremal vertices concentrate **locally** to `p≈1` and saturate a single shared link to `arc(1)=1`, while the mean participation stays high. So 0827's headline — *"ρ(M) < 1, strict for any p > 1"* — is **false as stated** (with `p` read as the mean/nominal participation), and a floor on the *mean* participation does **not** prevent it. These rules are CHI-1-local and admissible under everything *except* a pointwise orientation condition.

## 3. The fix — a *pointwise* participation floor (and it works)

The orientation argument 0827 gives for the floor is actually **pointwise**: a genuine local enantiomorph indicator must resolve a 4-D orientation **at every vertex**, i.e. `p_v ≥ 4` at **each** `v` (not on average). Imposing this:

- `p_v ≥ 4 ⇒ Σ_e (c^v_e)⁴ ≤ 1/4 ⇒ c_max^v ≤ (1/4)^{1/4} = 0.7071` at every vertex ⇒ the strongest single link is `arc(c_max²) ≤ arc(0.5) = 1/3` — **no link can saturate**, which is exactly what the counterexample exploited.
- **Adversarial search (400 homogeneous rules with pointwise min-participation ≥ 4):** worst `ρ(M) = 0.642` (margin ≈ 36%). Mixing any uniform floor into the n̂-concentration rules (raising every vertex's `p`) collapses `ρ` from 1.0 back to ≈0.63–0.66.

So the closure **survives under the pointwise floor**, and the F.1 window's core instinct (transitivity tames concentration) is vindicated — just via the right lever (pointwise `c_max` bound), not the false "max = avg" lemma.

**Caveat I will not paper over:** the adversarial search is strong evidence, not a proof. A clean closed-form bound on `max_v RowSum_v` under pointwise `p≥4` is **not yet in hand** — the obvious Cauchy–Schwarz step (`RowSum_v ≤ √(Σ_e (c^{w(e)}_e)²)`) is too loose (gives ≈2.4). The genuine control is `c_max ≤ 0.707` **plus** the global average bound **plus** transitivity, and tying those into a single `<1` inequality is the computation that still has to be written.

## 4. Disposition

- **Outcome 1 still the likely truth, not yet proven.** Under the (well-motivated, pointwise) orientation floor, the verdict is robust across the admissible weight class and the η-identity dissolves — Thomas's PCD-layer insight is **not** called. But "outcome 1" now **rests on**: (i) the orientation requirement implying a **pointwise** `p≥4`, and (ii) a clean `ρ<1` bound under that floor. (i) is physically natural; (ii) is empirically solid but unwritten. *If (ii) cannot be closed cleanly, the residual — "what guarantees pointwise non-degeneracy of the dynamical η" — is where outcome 2 (PCD layer) would re-enter.* The door is narrower than before, not shut.
- **Do NOT re-fire on 0827's framing.** Re-firing C1 with "homogeneous + mean p>1" invites a sharp reviewer (ChatGPT, on form) to reconstruct the §2 n̂-concentration counterexample and RESTATE a third time. The admissibility condition must be **pointwise p≥4**, and the supporting argument must be the `c_max`-bound, not "max = avg."

## 5. Recommendation (hand-off to F.1)

Return to the F.1 window with this review attached. Two items:
1. **Drop the "max = avg via homogeneity" lemma** (false for n̂-dependent η; §2 counterexample).
2. **Re-establish the closure under the pointwise floor:** state admissibility as `p_v ≥ 4` at every vertex (from the *local* orientation requirement); derive `c_max ≤ 0.707`; and write a clean `max_v RowSum_v < 1` bound (or, if a closed form resists, present the adversarial-search margin honestly as the evidential basis and scope the claim accordingly).

Once F.1 returns a corrected closure, the chirality lane re-fires C1 with the **pointwise** admissibility condition. Banking **Path B** (the explicit narrowed theorem over the equal-weight / bounded-pointwise-concentration class) in parallel remains free insurance and would pass now.

## Scope held

Chirality-lane review only. **No verdict moved, no THEO registered, no CHIR.md edit, no count change.** CAPACITY-1 reserved; OPEN-CHIR-1d-β OPEN. The weight-concentration falsifier remains **open**, now sharpened: the live question is the **pointwise**-floor closure, not the mean-floor version 0827 established. Conditional on Mechanism A (OPEN-FP-F1-2).
