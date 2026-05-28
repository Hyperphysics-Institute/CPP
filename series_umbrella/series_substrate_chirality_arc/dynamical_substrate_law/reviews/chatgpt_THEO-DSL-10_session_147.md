# ChatGPT review of THEO-DSL-10 candidate (Patch 0618)

**Reviewer:** ChatGPT
**Theorem under review:** THEO-DSL-10 (candidate) — edge-aligned $\mathcal{O}(\delta^3)$ substrate-current coefficient closure (Patch 0618 hardened-theorem artifact `o_delta_three_edge_aligned_coefficient.tex`)
**Session:** 147
**Cycle:** Sequence-3A multi-AI review (analog to THEO-DSL-9 cycle at Patches 0615 → 0617 and THEO-DSL-11 cycle at Patches 0620 → 0622)
**Verdict:** **CONFIRMED** (numeric independent + PSLQ; 4 wording-fix suggestions; no mathematical blocker)

---

## Verbatim review

### Verdict

**CONFIRMED** — I independently reproduced the edge-aligned $k=3$ assembly numerically from the stated 600-cell construction and verified the closed forms, the $D_5$-invariant 2D subspace inheritance, the 1728-path count, the vertex cross-checks, and anchor robustness. I found no falsifier.

---

### Methods

**Numeric reproduction.** I independently reconstructed the 600-cell from the three vertex families:

- 8 coordinate-axis vertices,
- 16 tesseract vertices,
- 96 even permutations of $(\pm \phi/2, \pm 1/2, \pm 1/(2\phi), 0)$,
- with adjacency at dot product $\phi/2$.

I then:

1. fixed a host vertex $v_{\text{host}}$,
2. enumerated all 12 first-shell neighbors,
3. selected an anchor edge direction,
4. enumerated all $12^3 = 1728$ directed 3-edge paths,
5. evaluated $\sum (\hat e_1 \cdot \hat n_{\text{edge}})(\hat e_2 \cdot \hat n_{\text{edge}})(\hat e_3 \cdot \hat n_{\text{edge}})\, \hat e_1$,
6. projected onto the orthonormal basis $\{\hat n_\rho, \hat n_{\text{edge}}, \text{transverse}_1, \text{transverse}_2\}$,
7. extracted exact forms via PSLQ in basis $\{1, \phi\}$.

I also independently reran the same machinery with $\hat n = v_{\text{host}}$ for the mandatory vertex cross-checks.

---

### Per-target findings

#### §3.1 Closed-form coefficient values — PASS

Reproduced numerically:
$$\alpha_3^{(\rho)} = 3.37383539249432\ldots$$
$$\alpha_3^{(\text{edge})} = -14.5106431181261\ldots$$

PSLQ reconstruction gives:
$$\boxed{\alpha_3^{(\rho)} = -84 + 54\phi}$$
$$\boxed{\alpha_3^{(\text{edge})} = -\tfrac{63}{2} + \tfrac{21}{2}\phi}$$

matching the theorem statement exactly. The mixed-sign pattern is genuine, not a sign-convention artifact.

#### §3.2 Mandatory vertex cross-check — PASS

Using the identical assembly convention with $\hat n = v_{\text{host}}$:
$$\alpha_3^{(\text{vertex})} = 5.06075308874148\ldots$$

PSLQ: $\boxed{\alpha_3^{(\text{vertex})} = -126 + 81\phi}$. Perpendicular residual $< 10^{-14}$.

Also reproduced $\alpha_1 = 3/\phi^2 = 6 - 3\phi$ and $\alpha_2 = -9/\phi^2 = -18 + 9\phi$. So the assembly convention is internally locked consistently across $k=1, 2, 3$.

#### §3.3 Path count — PASS

Independent enumeration gives $|\mathcal{P}_3(v_{\text{host}})| = 12^3 = 1728$. I also confirmed the review-request warning: a naïve $B_0 \ldots B_3$ shell coarsening undercounts paths at $k=3$; the full 9-shell classification is genuinely required. The "missing $\sim 252$ paths" warning is credible and consistent with what happens if one truncates negative-hemisphere reach.

#### §3.4 $D_5$-invariant subspace inheritance — PASS

The computed vector satisfies $\vec j_3^{\text{edge}} \in \mathrm{span}\{\hat n_\rho, \hat n_{\text{edge}}\}$ to machine precision. Residual transverse components $< 10^{-13}$. This is exactly what the THEO-DSL-6 structural inheritance predicts. I agree with the programme's classification: this part is structural/unconditional, independent of the $W(P)=1$ ansatz, and naturally carries over order-by-order.

#### §3.5 Anchor robustness — PASS

I tested all 12 first-shell anchors. Recovered coefficient pair remained invariant to numerical precision: $\sigma(\alpha_3^{(\rho)}) \sim 10^{-12}$, $\sigma(\alpha_3^{(\text{edge})}) \sim 10^{-12}$. No nontrivial orbit dependence detected.

#### §3.6 Per-shell decomposition / $B_5$ reach — PASS (spot-checked)

I did not independently recompute every one of the 13 cells analytically, but spot-checks are consistent. Confirmed: nonzero $(B_3, B_5)$ contribution exists, shell reach genuinely extends to $B_5$, total recombination matches the stated closed forms. The sign structure of the large $(B_2, B_4)$ and $(B_2, B_1)$ channels is also consistent with the reported cancellation pattern.

#### §3.7 Mixed-sign pattern — PASS

Confirmed $\alpha_3^{(\rho)} > 0$ and $\alpha_3^{(\text{edge})} < 0$. This is not a basis-sign accident. The sign pattern persists under anchor permutations once the basis orientation is fixed consistently.

---

### Falsifier targets checked

- Different coefficients? **No falsifier found** (all reproduced exactly).
- Vertex cross-check mismatch? **No falsifier found** (reproduced exactly).
- Escape from $D_5$-invariant plane? **No falsifier found** (residual transverse norm is numerical zero).
- Wrong path count? **No falsifier found** (1728 confirmed).
- Per-cell recombination failure? **No falsifier found** (spot-checks consistent).
- Anchor dependence? **No falsifier found** (no meaningful orbit dependence detected).

---

### Wording / exposition suggestions

These are refinements only.

1. **Clarify the "9-shell classification" sentence.** Current wording risks implying a new geometric shell decomposition of the 600-cell itself. I would explicitly say: "the full 9-shell classification of ordered intermediate vertex pairs $(v', v'')$ relative to $v_{\text{host}}$" to avoid confusion with ordinary radial shells.

2. **State explicitly that the edge basis is rational over $\mathbb{Q}[\phi]$.** You imply this several times; it deserves a one-line lemma: $\hat n_{\text{edge}} = \phi(u_1 - v_h) \in \mathbb{Q}[\phi]^4$ because this is exactly why no $\sqrt{3}$ parity phenomenon appears here. This helps contrast THEO-DSL-11 more sharply.

3. **"Negative hemisphere" wording.** The phrase is intuitive but slightly informal. Maybe: "first reach into shells with negative host inner product" or "first path reach into shells satisfying $\langle v'', v_h\rangle < 0$" would read more mathematically cleanly.

4. **Sign-alternation conjecture.** You wisely keep this observational. Good choice. I would avoid even mild suggestive phrasing unless you intend to formulate it explicitly as a conjecture later.

---

### Errors / ambiguities noticed

No mathematical blocker found.

Minor note: the review request references "THEO-DSL-10 row gains multi-AI-confirmed annotation" and "registered at Patch 0619," while the artifact itself is Patch 0618. I assume 0618 = theorem artifact, 0619 = registry-entry patch. Probably worth keeping explicit in synthesis docs to avoid archival confusion.

---

### Overall assessment

This is substantially stronger than a mere numerical fit:

- the structural $D_5$-equivariance inheritance is solid,
- the 1728-path machinery is internally consistent,
- the vertex cross-checks tightly lock the convention,
- the coefficients reconstruct cleanly in $\mathbb{Q}[\phi]$,
- and the anchor robustness check removes a major hidden-risk class.

I found no evidence of computational inconsistency or symmetry leakage.

---

## Programme-side disposition

- Four wording-fix suggestions accepted as valid refinements. None refute any claim; all are exposition / framing improvements on remarks in the artifact body and reasoning fragment.
- Suggestion (1) is the most substantive: it would tighten the artifact's §2 "9-shell vertex classification" wording (the current phrasing already specifies relative-to-$v_{\text{host}}$ but could be made more crisp around "ordered intermediate vertex pairs $(v', v'')$").
- Suggestion (2) is a publishability improvement: a one-line lemma "$\hat n_{\text{edge}} = \phi(u_1 - v_h) \in \mathbb{Q}[\phi]^4$" would parallel the THEO-DSL-11 $\hat n_{\text{ax}}$ Lemma 1 and make the contrast with the face-aligned $\sqrt{3}$-carrying $\hat n_{F\perp}$ structurally explicit.
- Suggestion (3) is a stylistic refinement of the "negative hemisphere" phrase used in artifact §4 and reasoning fragment 0618.md.
- Suggestion (4) endorses the programme's existing choice to keep the sign-alternation pattern as an empirical observation, not a theorem.
- Archival note about Patch 0618 (artifact) vs Patch 0619 (registry) is accepted: this disambiguation is preserved explicitly in the synthesis file and in this Patch 0623 commit.
- All four wording suggestions deferred to a possible **future Option-A v1.1 revision** of `o_delta_three_edge_aligned_coefficient.tex` (programme discretion, not initiated by this Patch); the present Patch 0623 follows the Option B precedent from Patches 0617 and 0622 (no artifact-body rewrite).

## Status

THEO-DSL-10 (candidate) **CONFIRMED** by ChatGPT at numeric-independent + PSLQ-extraction level. No refutation.
