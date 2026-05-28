# Copilot Review of THEO-DSL-9 (Patch 0615) — face-aligned $V_4$/2-D correction to THEO-DSL-8

## Metadata

- **Reviewer**: Copilot (Microsoft)
- **Subject reviewed**: THEO-DSL-9 (candidate) — `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/hardened_theorems/o_delta_two_face_aligned_coefficient.tex` (Patch 0615) — and the embedded structural correction to THEO-DSL-8 (Patch 0597) registered there.
- **Subject version commit**: `8893f86` (Patch 0616 origin/main head, i.e. immediately post-shipping of 0615+0616)
- **Review session**: Session 147
- **Review archived by**: Patch 0617 (this file)
- **Review delivered**: 28 May 2026 (Session 147 multi-AI review cycle for the THEO-DSL-8 $C_s\to V_4$ correction)
- **Reviewer panel position**: Round 1 of the THEO-DSL-9 / THEO-DSL-8-correction review cycle. Copilot continues to occupy the tertiary-reviewer position behind ChatGPT (strongest) and Grok (secondary).
- **Review character**: **Analytic-only PARTIAL/UNCERTAIN verdict with no refutation and full analytic confirmation of the non-decisive sub-questions**. Copilot independently confirmed Q3 (basis degeneracy) unconditionally, Q2 ($V_4$ group and 2-D invariant subspace) analytically *conditional* on $\sigma_F$ being an automorphism, Q4 (direction part) by the same conditional symmetry argument, and Q5 (no enlargement beyond $V_4$) by orbit-stabiliser ($|I_h|/30=4$). It explicitly states it **cannot independently certify Q1** (whether $\sigma_F$ permutes the 120-vertex set) because doing so requires either an $H_4$-root identification or a coordinate-level numeric check that it does not execute in this environment; it likewise does not redo the 144-path coefficient sum. **No refutation; no claimed counterexample; no displaced vertex; no nonzero $\hat n_{\perp 3}$ component**. The "PARTIAL/UNCERTAIN" verdict is therefore a tooling/scope limitation (no numerics executed), not analytic dissent — Copilot's structural reasoning is in full agreement with the THEO-DSL-9 claim wherever it actually evaluates it.
- **Programme-level reviewer ranking**: Copilot occupies the tertiary-reviewer position. The review correctly identifies Q1 as the load-bearing decisive question and correctly notes that it requires the kind of numeric/root-level check the analytic-only mode does not perform — which is exactly the gap that the ChatGPT and Grok numeric reviews (this same cycle) close.
- **Verdict-state classification**: **PARTIAL/UNCERTAIN (analytic-confirm-conditional-on-Q1, no refutation)**. Synthesised against ChatGPT + Grok (both numeric CONFIRMED, both produced explicit $\sigma_F = \mathrm{diag}(1,1,1,-1)$ witness for the canonical host and verified 120-vertex set-stability), the cross-reviewer position is THREE-FOR-THREE no-refutation, with TWO independent numeric confirmations of Q1 closing Copilot's stated gap. THEO-DSL-9's $V_4$/2-D/$1\!\to\!2\!\to\!2$ correction stands.

---

## Reviewer letter (verbatim)

**Verdict:** **PARTIAL/UNCERTAIN**

I can analytically confirm the *structure* of the $V_4$/2‑D story (Q2–Q3) **conditional** on $\sigma_F$ being a genuine 600‑cell automorphism, but I cannot independently *prove* that $\sigma_F$ is in the 600‑cell symmetry group (Q1), nor can I recompute the full 2‑edge current (Q4) from scratch here. So the decisive load‑bearing point (Q1) remains unproven on my side.

Below I'll go question by question and be explicit about what is solid vs what is conditional.

> "The $\Vfour$-invariant subspace of $\Reals^4$ at $\vhost$ is the $2$-dimensional
> $\operatorname{span}\{\nrho, \nax\} = (\ui-\uj)^\perp \cap \operatorname{span}\{\vhost,\ui,\uj\}$."

> "Independently, THEO-DSL-8's claimed basis $\{\nrho,\nax,\nperpF\}$ for its (over-stated) $3$D subspace is linearly \emph{dependent}: by \eqref{eq:nFdegenerate}, $\nperpF\in\operatorname{span}\{\nrho,\nax\}$, so those three vectors span only $2$D."

---

### Q1 — is $\sigma_F$ a 600‑cell automorphism that fixes $v_h$ and $\hat n_{F\perp}$?

**Method:** conceptual group/geometry analysis using the standard 600‑cell coordinates and the given construction of $\sigma_F$ as the reflection in the 3‑flat $\operatorname{span}\{v_h,u_i,u_j\}$.

- **What is clear:**
  - By construction, $\hat n_{\perp3}$ is orthogonal to $\operatorname{span}\{v_h,u_i,u_j\}$, so
    \[
    \sigma_F x = x - 2(\hat n_{\perp3}\cdot x)\hat n_{\perp3}
    \]
    fixes every vector in that 3‑flat and flips the $\hat n_{\perp3}$ component.
  - Therefore $\sigma_F v_h = v_h$, $\sigma_F u_i = u_i$, $\sigma_F u_j = u_j$, and hence
    \[
    \sigma_F (v_h+u_i+u_j) = v_h+u_i+u_j \;\Rightarrow\; \sigma_F \hat n_{F\perp} = \hat n_{F\perp}.
    \]
    So **if** $\sigma_F$ is in the 600‑cell symmetry group, it automatically preserves the rate function.

- **What is *not* fully established here:**
  - To be a 600‑cell automorphism, $\sigma_F$ must map the entire 120‑vertex set to itself. That is equivalent to saying that the hyperplane orthogonal to $\hat n_{\perp3}$ is a genuine **mirror** of the $H_4$ Coxeter group (the automorphism group of the 600‑cell). [Wolfram MathWorld](https://mathworld.wolfram.com/600-Cell.html)
  - Proving that requires either:
    - showing $\hat n_{\perp3}$ is proportional to an $H_4$ root (so its orthogonal hyperplane is a Coxeter mirror), or
    - explicitly checking that $\sigma_F$ sends each of the 120 listed vertices to another vertex in the same list.

I can't carry out that full root‑identification or 120‑vertex check numerically here, so I **cannot independently certify** that $\sigma_F$ is indeed an automorphism of the 600‑cell.

**Status for Q1:**
- *Analytically*: If $\sigma_F$ is an automorphism, it certainly fixes $v_h$ and $\hat n_{F\perp}$ and preserves the rate function.
- *But*: I cannot prove from first principles here that $\sigma_F$ maps the 120‑vertex set onto itself.

So Q1 remains **unresolved** on my side, and with your own falsifier standard that means the correction is **not fully confirmed**.

---

### Q2 — does $\langle\sigma_E,\sigma_F\rangle$ give $V_4$ with 2‑D invariant subspace?

**Method:** pure linear algebra in the orthonormal frame
\(\{\hat n_\rho,\hat n_{\text{ax}},\hat n_{\perp3},\hat n_{\text{diff}}\}\).

- In that frame:
  - $\sigma_E$ is reflection in $(u_i-u_j)^\perp$, i.e. it acts as:
    - $+1$ on $\hat n_\rho,\hat n_{\text{ax}},\hat n_{\perp3}$,
    - $-1$ on $\hat n_{\text{diff}}$.
  - $\sigma_F$ is reflection in $\operatorname{span}\{v_h,u_i,u_j\}$, i.e. it acts as:
    - $+1$ on $\hat n_\rho,\hat n_{\text{ax}},\hat n_{\text{diff}}$,
    - $-1$ on $\hat n_{\perp3}$.

- The group generated by two commuting reflections with orthogonal normals is
  \[
  \langle\sigma_E,\sigma_F\rangle = \{e,\sigma_E,\sigma_F,\sigma_E\sigma_F\} \cong V_4,
  \]
  because:
  - $\sigma_E^2=\sigma_F^2=e$,
  - $\sigma_E\sigma_F=\sigma_F\sigma_E$ (their normals are orthogonal),
  - $\sigma_E\sigma_F$ has order 2 and is distinct from both.

- The **common invariant subspace** is the intersection of the $+1$ eigenspaces:
  \[
  \operatorname{Fix}(\sigma_E)\cap\operatorname{Fix}(\sigma_F)
  = (u_i-u_j)^\perp \cap \operatorname{span}\{v_h,u_i,u_j\}.
  \]
  Inside the 3‑flat $\operatorname{span}\{v_h,u_i,u_j\}$, the condition $(u_i-u_j)^\perp$ removes the $\hat n_{\text{diff}}$ direction, leaving exactly the 2‑D span of $\hat n_\rho$ and the in‑face axial direction $\hat n_{\text{ax}}$. This matches the paper's Lemma 2:
  > "A vector fixed by both lies in $(\ui-\uj)^\perp \cap \operatorname{span}\{\vhost,\ui,\uj\}$. The latter equals $\operatorname{span}\{\vhost,\ \ui+\uj\} = \operatorname{span}\{\nrho,\nax\}$, which is $2$-dimensional…"

**Status for Q2:**
- **Confirmed analytically**, *conditional* on $\sigma_E,\sigma_F$ being actual automorphisms. The representation‑theoretic statement "if these two reflections are symmetries, their invariant subspace is exactly $\operatorname{span}\{\hat n_\rho,\hat n_{\text{ax}}\}$ and the group is $V_4$" is solid.

---

### Q3 — is $\{\hat n_\rho,\hat n_{\text{ax}},\hat n_{F\perp}\}$ linearly dependent?

**Method:** direct decomposition of $u_i+u_j$ relative to $v_h$.

You already gave the key identity:
\[
u_i+u_j = \phi\,v_h + P_{\perp v_h}(u_i+u_j),
\]
with
\[
\hat n_{\text{ax}} = \operatorname{normalize}\bigl(P_{\perp v_h}(u_i+u_j)\bigr).
\]
Then
\[
v_h + u_i + u_j = (1+\phi)\,v_h + P_{\perp v_h}(u_i+u_j),
\]
so
\[
\hat n_{F\perp} \propto (1+\phi)\,\hat n_\rho + \|P_{\perp v_h}(u_i+u_j)\|\,\hat n_{\text{ax}}
\in \operatorname{span}\{\hat n_\rho,\hat n_{\text{ax}}\}.
\]
This is exactly your equation (2.3):
> "The centroid direction of \eqref{eq:nperp} is \emph{not} independent of this frame:
> \[
> \nperpF \;\propto\; (1+\phi)\,\nrho + \lVert P_{\perp\vhost}(\ui+\uj)\rVert\,\nax
> \;\in\; \operatorname{span}\{\nrho, \nax\}.
> \]"

Since $\hat n_\rho$ and $\hat n_{\text{ax}}$ are orthonormal and nonzero, this shows $\hat n_{F\perp}$ is a nontrivial linear combination of them, so the triple has rank 2, not 3.

**Status for Q3:**
- **Confirmed analytically.** The prior 3‑vector basis is indeed degenerate; the "3‑D invariant subspace" was at most 2‑D even before invoking any symmetry.

---

### Q4 — does $\vec j_2$ lie in $\operatorname{span}\{\hat n_\rho,\hat n_{\text{ax}}\}$ with the stated coefficients?

**Method:** symmetry + structural reasoning, but **no full path‑sum recomputation**.

- **Direction constraint:**
  If Q1 and Q2 hold (i.e. $\sigma_E,\sigma_F$ are genuine symmetries preserving the rate function), then the order‑2 current
  \[
  \vec j_2 = \sum_{v_h\to u\to v'} (\hat e_1\cdot\hat n_{F\perp})(\hat e_2\cdot\hat n_{F\perp})\,\hat e_1
  \]
  is built from:
  - a $\V_4$‑invariant rate function (since $\hat n_{F\perp}$ is fixed), and
  - a path set permuted by $\V_4$ as graph automorphisms fixing $v_h$.

  Under those assumptions, the usual re‑indexing argument shows $\vec j_2$ is $\V_4$‑invariant, hence must lie in the 2‑D invariant subspace $\operatorname{span}\{\hat n_\rho,\hat n_{\text{ax}}\}$, so its $\hat n_{\text{diff}}$ and $\hat n_{\perp3}$ components vanish. This matches your Lemma 3 and Theorem 1.

- **Coefficient values:**
  The specific closed forms
  \[
  \alpha_2^{(\rho)} = -14+7\phi = -\frac{7}{\phi^2},\qquad
  \alpha_2^{(\text{ax})} = -6+2\phi
  \]
  and the per‑class decomposition in Table 1 are the result of an explicit 144‑path sum. I cannot redo that full combinatorial and algebraic computation here, nor can I numerically cross‑check the "vertex‑aligned" sanity check $\alpha_2=-9/\phi^2$.

**Status for Q4:**
- **Direction (no $\hat n_{\text{diff}}$ / $\hat n_{\perp3}$ components):** confirmed *conditionally* on Q1/Q2 (the symmetry argument is sound).
- **Exact coefficients:** **not independently verified** here; I have to treat them as unconfirmed.

---

### Q5 — any extra symmetries or failures among $\sigma_E,\sigma_F,C_2$?

**Method:** group‑theoretic constraints from the known automorphism group of the 600‑cell.

- The full automorphism group of the 600‑cell is the Coxeter group $H_4$ of order $14400$, with vertex stabiliser isomorphic to the icosahedral group $I_h$ of order $120$. [Wikipedia](https://en.wikipedia.org/wiki/600-cell) [Wolfram MathWorld](https://mathworld.wolfram.com/600-Cell.html)
- Within that vertex stabiliser, the stabiliser of an **unordered face** through $v_h$ must have order $4$, because:
  - there are 30 faces through $v_h$, and
  - $|I_h|/30 = 4$ by orbit–stabiliser.
- So **if** $\sigma_E$ and $\sigma_F$ are both in the vertex stabiliser and both fix the face (as they do by construction), then the subgroup they generate must already be the full face stabiliser; there is no room for a larger host‑fixing, face‑fixing subgroup beyond $V_4$.

On the other side, I also cannot exhibit any explicit failure of $\sigma_E,\sigma_F,$ or $C_2$ as automorphisms without doing the full coordinate check.

**Status for Q5:**
- **No evidence** (from group‑size constraints) for a larger host‑fixing, $\hat n_{F\perp}$‑preserving subgroup than $V_4$, *assuming* $\sigma_E,\sigma_F$ are valid automorphisms.
- **No explicit refutation** of any of $\sigma_E,\sigma_F,C_2$ as automorphisms, because that would require the same kind of coordinate‑level check as Q1.

---

### Overall assessment

- **What I can say firmly:**
  - The prior "3‑D invariant subspace" basis is definitely degenerate: $\hat n_{F\perp}\in\operatorname{span}\{\hat n_\rho,\hat n_{\text{ax}}\}$, so the old $(u_i-u_j)^\perp$ story was at most 2‑D at the level of actual vectors (Q3).
  - If $\sigma_E$ and $\sigma_F$ are indeed 600‑cell automorphisms preserving the rate function, then:
    - the residual group is $V_4$,
    - the invariant subspace is exactly $\operatorname{span}\{\hat n_\rho,\hat n_{\text{ax}}\}$,
    - and all currents $\vec j_k$ (including $\vec j_2$) must lie in that 2‑D subspace (Q2, direction part of Q4).

- **What I cannot certify here:**
  - That $\sigma_F$ (reflection in $\operatorname{span}\{v_h,u_i,u_j\}$) actually maps the 120‑vertex set to itself (Q1).
  - The exact numerical values of the second‑order coefficients (Q4).

Given your falsifier criteria, that leaves me with a **PARTIAL/UNCERTAIN** verdict: the *structural* $V_4$/2‑D/$1\to2\to2$ picture is internally consistent and analytically well‑motivated, but the decisive geometric fact—"$\sigma_F$ is a 600‑cell automorphism"—has not been independently proved or disproved here.
