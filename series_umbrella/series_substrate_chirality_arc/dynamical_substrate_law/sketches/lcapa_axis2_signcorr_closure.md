# L-CAP-A(ii)′ established — Axis 2 closes via the sign-correlation row-sum bound (the entrywise-domination route is *false*; this is the correct invariant)

**Patch:** 0826 (Session 156, 8 June 2026) · **Type:** infrastructure (L-CAP-A(ii)′, the Axis-2 monotonicity lemma) · **Lane:** F.1 / `dynamical_substrate_law/` (verdict + DG-3 + CAPACITY-1 stay chirality-lane).
**Answers:** chirality-lane 0917/0918 — Axis 2 via the **Perron route**, NOT Gershgorin. **Verify:** `code/0826_lcapa_signcorr_rowsum.py`. Builds on Axis 1 (0918, established). I read 0917+0918 first; this does **not** re-run the refuted Gershgorin argument.

---

## Headline

Axis 2 closes for the entire admissible observable class, but the route 0918 proposed (`|C(m′)| ≤ 0.053` entrywise) is **false** — and computing more `{4,6,8,12}`-style samples would have hidden that. The correct closure is a closed-form **row-sum invariant** from the Gaussian sign-correlation law. Net: `ρ(M(m′)) < 1` for every admissible η with support `m ≥ 2`, so the verdict is robust across the η-identity — no PCD layer called.

## 1. The connected coupling is shared-edge-only (rigorous, verified)

Each `η_v = sign(Σ_{e∈R_v} w_e x_e)`, with `x_e = δ·bias_e + ξ_e`, `ξ_e` i.i.d. The only fluctuating input common to neighbours `v,w` is the **shared edge variable** `x_{vw}` (common neighbours contribute *different* edge variables → independent → no covariance). So the connected `C_vw` is first-order in the shared edge; `d ≥ 2` correlations are second-order response, not coupling. Measured: `|C|(d≥2) ≈ 0.005 ≈ 0` ✓. **M is nearest-neighbour-only.**

## 2. The sign-correlation law (closed form, verified)

For jointly-Gaussian pre-sign sums with shared-edge correlation `ρ_{vw} = w_v w_w / m` (Var(S_v)=m), the sign correlation is `C_vw = (2/π)·arcsin(1/m)` per reciprocally-read link. Verified on the real measure (δ=0.08):

| m | (2/π)arcsin(1/m) | measured /edge |
|---|---|---|
| 12 | 0.0531 | 0.0537 |
| 4 | 0.1609 | 0.1601 |
| 2 | 0.3333 | 0.3316 |

## 3. Why the proposed entrywise route is FALSE

`|C(m′)| ≤ 0.053` does **not** hold: a more-local observable is **more** strongly per-link correlated, not less (`m=4 → 0.16 > m=12 → 0.053`). The `{4,6,8,12}` scan's apparent "more-local → weaker" was an artdefact of averaging each link's correlation over the many links where the small-`m` read set *excludes* the shared edge (diluted mean), not the per-edge entry. So entrywise domination is the wrong sufficient condition; a bigger scan would have kept missing this.

## 4. The correct closure — Perron row-sum invariant (rigorous)

Perron–Frobenius: `ρ(M) ≤ ρ(|M|) ≤ max_v Σ_w |M_vw|` (this is what handles 0918's worry (b) — sign-coherence/non-uniformity is irrelevant once we bound `|M|`). Each vertex reads `m` edges, so at most `m` reciprocal links, each `≤ (2/π)arcsin(1/m)`:

> **`ρ(M(m)) ≤ R(m) := m·(2/π)·arcsin(1/m)`.**

`R(m)` is monotonically decreasing, `R(1)=1`, `R(2)=2/3`, `R(∞)=2/π≈0.637`:

| m | 1 | 2 | 4 | 12 | →∞ |
|---|---|---|---|---|---|
| R(m) | 1.000 | 0.667 | 0.643 | 0.637 | 0.637 |
| margin | 0% | 33% | 36% | 36% | 36% |

So **`R(m) < 1` for every `m ≥ 2`** (critical only at the degenerate `m=1`). The fewer-but-stronger trade-off is exact: more-local = fewer links × proportionally stronger links = invariant row sum ≈ 2/π, rising to 1 *only* at a single edge. Measured `ρ(M(m))` (nn-only coupling): 0.59–0.64 across `m=2…12`, matching `R(m)`; `m=1 → ρ≈1.0`. ✓

## 5. The residual, located precisely — and it is *not* the PCD layer

The only critical observable is `m=1`: `η_v = sign(w_e x_e)` for a single edge — the sign of one edge variable times a fixed weight, carrying no intrinsic orientation. A genuine local enantiomorph indicator must resolve a handedness, i.e. an oriented frame; in 4-D an orientation is the sign of a `4×4` determinant, needing **≥ 4** independent directions. So the physical admissibility floor is `m ≥ 4` (`R(4)=0.643`, margin 36%), far from the `m=1` critical point. The "which η is dynamical" ambiguity (the η-identity, surfacing here as Axis 2) is therefore **dissolved for the verdict**: *every* admissible observable (`m ≥ 2`, certainly `m ≥ 4`) is sub-critical, so the verdict does not depend on pinning the dynamical η. Thomas's PCD-layer insight is **not** called.

## 6. The one load-bearing caveat

The shared-edge-only structure (§1), hence the whole closure, rests on **per-edge independence** of the substrate fluctuations (the 0821 / Mechanism-A measure). If Mechanism A's measure carries long-range fluctuation correlations, the `d≥2` coupling would not vanish and `R(m)` would need re-derivation. This is a sub-case of the standing Mechanism-A conditionality, but it is the load-bearing input and is stated as such.

## 7. Decision-gate outcome

Per 0918's gate: the structural fact **is** established (not as entrywise domination, but as the row-sum invariant `R(m)<1` for `m≥2`), so **Axis 2 closes via the Perron route**. With Axis 1 (0918), L-CAP-A is complete. Recommend the chirality lane assess this for the re-fire of a genuinely universal CAPACITY-1 — replacing the C1 mode-scan with the `R(m)<1` bound (a proof over the whole class, not a sample), and reporting the entrywise-route correction so the re-fire's Q1 answer is the row-sum invariant, not a larger scan.

## Scope held

F.1 infrastructure: the Axis-2 lemma, established via the corrected route. **No verdict moved** (V3/W3 stand; CAPACITY-1 reserved). No THEO, no ID, no CHIR.md / package / verdict-registry edits. Corrects 0918's proposed sufficient condition; builds on 0918 Axis 1. Conditional on Mechanism A (OPEN-FP-F1-2), with the per-edge-independence sub-caveat in §6 made explicit.
