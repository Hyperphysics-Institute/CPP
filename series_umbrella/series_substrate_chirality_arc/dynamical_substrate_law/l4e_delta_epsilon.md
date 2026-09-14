# 0972 — L4-E: the δ–ε relation is pinned, and pinning it exposes an unstated physical commitment

**Patch:** 0972, 13 Sep 2026. **Verify:** `code/0972_l4e_delta_epsilon.py` (5/5). **No verdict moved, no claim registered.**

**Target.** L4-E, the last open sub-target of OPEN-FP-F1-2: the magnitude relation between MA.1's rate parameter `δ` and Reading C's edge-length parameter `ε`. F.1 states it is *"not pinned"* and takes both as independent inputs.

**Result.** It is pinned: **δ = −ε** at first order. But the derivation only works because Reading C's `ℓ` is **not a length**, and that has not been stated anywhere.

---

## 1. The parity problem

Reading C (Capotauro v2.0 §2.3, quoted in F.1 §"Structural connection"):

> *"edges of the 600-cell substrate acquire effective lengths"*  `ℓ(ê) = ℓ₀(1 + ε ê·n̂)`

**`ê·n̂` is reversal-odd.** On a first-shell edge it reads −0.3090 forward and +0.3090 backward, so the formula gives that edge two different "lengths" — 0.999691 one way, 1.000309 the other (T1).

**A metric length cannot do that.** A length is a property of the undirected edge. What Reading C actually defines is a **directed traversal cost**, and a substrate with direction-dependent traversal cost is **non-reciprocal**.

That is a physical commitment. F.1 describes it in words as a "length" while using it in the equation as a directed cost, and nothing in the corpus flags the difference.

## 2. Given that formula, the relation is pinned

Constant-speed traversal — one Displace per Absolute Moment at `c` (A6′/A3′) — gives `rate = c/ℓ`, so

`r = r₀ (1 − ε(ê·n̂) + ε²(ê·n̂)² − …)`

Measured over all 1,440 directed edges: **δ = −ε exactly at first order** (T2). 0949's T7 reproduced, and F.1's "not pinned" is superseded **conditional on §1's commitment**.

## 3. A bonus that bears directly on the CONV-048 residuals

The same expansion fixes the **second**-order coefficient at `+ε²(ê·n̂)²` — which is reversal-**even** (T3, measured 1.0000).

**So the reversal-odd quadratic `(ê·n̂)(m̂·n̂)` — the channel found at 0955 and shown superadditive at 0957, and the one carried as a named residual on CAPACITY-1 — has coefficient ZERO under this picture.** Constant-speed traversal does not generate it.

That does not close the residual: it shows the residual is absent *in the Reading-C realisation*, not that no realisation produces it. But it is the first positive statement about that channel rather than a bound on it, and it should be recorded against the residual.

## 4. The counterfactual, which is the finding that matters

**If `ℓ` were a genuine reversal-even length** — depending on the edge midpoint `m̂·n̂` rather than the traversal direction — then `r = c/ℓ` is reversal-**even**, and it generates **the A-term, not δ**: measured `A = −ε`, with the reversal-odd `δ` it produces averaging exactly **0** (T4).

**So MA.1's reversal-odd first harmonic cannot come from a metric length perturbation at all.** The two pictures are distinguishable, not interchangeable (T5):

| picture | generates | `δ` | `A` |
|---|---|---|---|
| directed traversal cost (Reading C as written) | reversal-odd | **−ε** | 0 |
| metric length (reversal-even) | reversal-even | 0 | **−ε** |

**MA.1's form requires non-reciprocity.** That is the real content of L4-E, and it is a stronger statement than the magnitude relation it was asked for.

## 5. What this does and does not settle

- **Settled:** given Reading C as written, `δ = −ε`. F.1's "not pinned" can be replaced, with the commitment stated.
- **Settled:** the Reading-C realisation generates no reversal-odd second harmonic.
- **Not settled, and now visible:** whether the substrate *is* non-reciprocal. The corpus has been assuming it since Reading C was written, in the equation but not in the prose. **This is a founder question in a physical picture (PD-006(a)), not something to decide from here.**
- **Not claimed:** that the A-term is therefore zero. §4 shows an even length perturbation *would* generate A; it does not show the substrate has no even perturbation from some other source. CAPACITY-1's residual stands.

## 6. Owed

- **F.1 wording:** replace "the δ–ε relation is not pinned" with `δ = −ε` plus the non-reciprocity clause. Bundles with the arc's corrigenda queue.
- **Escalated to the founder (PD-006(a)):** is the substrate non-reciprocal — i.e. is Reading C's `ℓ` a directed traversal cost rather than a length? **The equation has always said yes; the prose has always said "length".** One of them should change.
- **Recorded against CAPACITY-1's residual:** the odd second harmonic has zero coefficient in the Reading-C realisation.

**OPEN-FP-F1-2: with L4-E now addressed, all five sub-targets (A, B, C, D, E) have artifacts.** The parent stays OPEN on the named residuals and on the non-reciprocity question.
