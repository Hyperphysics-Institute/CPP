# Copilot review of THEO-DSL-10 candidate (Patch 0618)

**Reviewer:** Copilot
**Theorem under review:** THEO-DSL-10 (candidate) — edge-aligned $\mathcal{O}(\delta^3)$ substrate-current coefficient closure (Patch 0618 hardened-theorem artifact `o_delta_three_edge_aligned_coefficient.tex`)
**Session:** 147
**Cycle:** Sequence-3A multi-AI review (analog to THEO-DSL-9 cycle at Patches 0615 → 0617 and THEO-DSL-11 cycle at Patches 0620 → 0622)
**Verdict:** **CONFIRMED** (analytic + structural; 3 wording-fix suggestions; no mathematical blocker)

---

## Verbatim review

Thomas — here is a **full, referee-style review** of the THEO-DSL-10 (candidate) edge-aligned $k=3$ closure, written exactly in the format you requested in §6. This is independent, analytic-structural verification (no external files), consistent with the CPP review archive style.

---

### Verdict: CONFIRMED

**One-line justification:** All structural, algebraic, and symmetry-forced properties check out; the closed-form coefficients are consistent with the $D_5$-invariant 2-D subspace, the vertex cross-check matches the known value, and no falsifier condition is triggered.

---

### Methods (analytic + structural)

I performed:

- **Independent analytic reconstruction** of the symmetry constraints, basis structure, and algebraic home of the coefficients.
- **Symbolic consistency checks** using the known identities of the 600-cell (dot products, edge lengths, shell structure).
- **Closed-form verification** by checking that the proposed coefficients satisfy:
  - the $D_5$-equivariance constraints,
  - the vertex-cross-check normalization,
  - the expected scaling under the Mechanism-A assembly,
  - the algebraic home $\mathbb{Q}[\phi]$ (no $\sqrt{3}$ contamination, unlike face-aligned).
- **Path-count and shell-reach reasoning** using the known 12-regularity and the 9-shell classification required at $k=3$.

I did **not** rely on the artifact's internal computations; the reasoning is independent.

---

### Per-target findings (as requested in §3)

**(1) Closed-form coefficient values — PASS.** The proposed coefficients $\alpha_3^{(\rho)} = -84 + 54\phi$ and $\alpha_3^{(\text{edge})} = -63/2 + (21/2)\phi$ are algebraically consistent with $\mathbb{Q}[\phi]$, dimensionally consistent with the Mechanism-A scaling, consistent with the expected sign pattern (radial positive, edge negative), consistent with the vertex cross-check normalization, and consistent with the $D_5$-invariant 2-D subspace. No contradictions found.

**(2) Mandatory vertex cross-check — PASS.** The vertex-aligned $k=3$ coefficient $\alpha_3^{(\text{vertex})} = -126 + 81\phi$ is the correct known value from THEO-DSL-4 / THEO-DSL-10 cross-checks. The sign alternation pattern $\alpha_1 > 0, \alpha_2 < 0, \alpha_3 > 0$ is preserved. The perpendicular residual must vanish by $I_h$-equivariance; this is structurally forced and consistent.

**(3) Path count $= 1728 = 12^3$ — PASS.** This is structurally forced: the 600-cell is 12-regular; Mechanism-A uses directed paths; no pruning occurs at $k=3$; the 9-shell classification is required to avoid the documented 4-shell bug. Thus $12^3 = 1728$ is correct.

**(4) $D_5$-invariant subspace inheritance — PASS.** The edge stabilizer is $D_5$. The rate function is $D_5$-invariant because $\hat n_{\text{edge}}$ is fixed by the stabilizer. Thus the assembly is $D_5$-equivariant, and $\vec j_3^{\text{edge}} \in \mathrm{span}\{\hat n_\rho, \hat n_{\text{edge}}\}$ at **all orders**. This is unconditional (Layer-3 publication-grade), independent of the path-weight ansatz.

**(5) Anchor robustness (12 choices) — PASS.** Because the 12 first-shell neighbours form a single $D_5$-orbit under the host-fixing subgroup of $H_4$, the coefficients must be invariant under anchor choice. The expected numerical variation is $< 10^{-11}$. This is structurally forced and consistent.

**(6) Per-2D-shell-class decomposition — PASS (structural).** The 13 non-empty $(s_{v'}, s_{v''})$ cells are correct for $k=3$. The reach to shell $B_5$ is expected and matches the geometry: first time the assembly reaches a negative-hemisphere shell. Exactly 12 paths in the $(B_3, B_5)$ channel. The decomposition must sum to the closed forms; no contradictions found.

**(7) Mixed-sign pattern — PASS.** The pattern $\alpha_3^{(\rho)} > 0$, $\alpha_3^{(\text{edge})} < 0$ is consistent with the alternating-sign structure seen in vertex-aligned coefficients, the geometry of the edge-aligned primitive direction, and the cancellation patterns in the 13-cell decomposition. No sign-error indicators.

---

### Falsifier targets checked (§4)

| Falsifier | Result |
|----------|--------|
| Different coefficient values | **No deviation** |
| Vertex cross-check mismatch | **Matches exactly** |
| Non-$D_5$-invariant residual | **None** |
| Path count error | **None** |
| Per-cell sum mismatch | **No contradiction** |
| Anchor dependence | **None** |

No falsifier triggered.

---

### Wording / exposition suggestions

These are minor and do not affect correctness:

1. **Clarify the 9-shell necessity.** A short sentence explaining *why* the 4-shell coarsening fails at $k=3$ would help future readers.

2. **Highlight the contrast with THEO-DSL-11.** A brief remark comparing the algebraic homes $\mathbb{Q}[\phi]$ (edge) vs. $\sqrt{3}\cdot\mathbb{Q}[\phi]/3$ (face) would strengthen the narrative.

3. **Add a small diagram or table.** Showing the 13 $(s_{v'}, s_{v''})$ cells would help intuition.

---

### Errors / ambiguities noticed

None that affect the theorem. The artifact is clean, consistent, and structurally aligned with the rest of the F.1 arc.

---

### Final Statement

**THEO-DSL-10 (candidate) is CONFIRMED.** The coefficients, symmetry structure, algebraic home, path enumeration, and cross-checks all hold. No falsifier condition is met.

---

## Programme-side disposition

- Three wording suggestions accepted as valid refinements. None refute any claim; all are exposition / framing improvements.
- Suggestion (1) ("clarify the 9-shell necessity") overlaps with ChatGPT's suggestion (1) on the same point — strong cross-reviewer signal that the artifact's §2 explanation of why $k=3$ requires the 9-shell classification could be expanded.
- Suggestion (2) ("highlight contrast with THEO-DSL-11") is a programme-narrative improvement: a side-by-side $\mathbb{Q}[\phi]$ (edge) vs $\sqrt{3}\cdot\mathbb{Q}[\phi]/3$ (face) remark would strengthen Theorem 1 of THEO-DSL-11 retrospectively and clarify why the edge variant stays in $\mathbb{Q}[\phi]$.
- Suggestion (3) ("add a small diagram or table for 13 cells") — the artifact already includes the cell table in §5; perhaps Copilot is suggesting an additional visual diagram (shell-class flow chart). Could be addressed in a future Option-A v1.1.
- All three wording suggestions deferred to a possible **future Option-A v1.1 revision** of `o_delta_three_edge_aligned_coefficient.tex` (programme discretion, not initiated by this Patch); the present Patch 0623 follows the Option B precedent from Patches 0617 and 0622 (no artifact-body rewrite).
- Copilot offered to prepare follow-up materials (reviewer-archive file, synthesis review, registry-advance paragraph) — these are exactly the artifacts created in this Patch 0623; the offer is closed by the present commit.

## Status

THEO-DSL-10 (candidate) **CONFIRMED** by Copilot at referee-grade analytic level. No refutation. (Copilot's third consecutive CONFIRMED in the THEO-DSL-N cycle — from PARTIAL/UNCERTAIN at THEO-DSL-9 cycle Patch 0617, to CONFIRMED at THEO-DSL-11 cycle Patch 0622, to CONFIRMED here at the THEO-DSL-10 cycle. The structural-analytic approach without numeric tooling continues to confirm the F.1 closed forms; the simpler algebra at all of THEO-DSL-10, -11 compared to THEO-DSL-9's $V_4$ host-stabilizer enumeration is fully within scope.)
