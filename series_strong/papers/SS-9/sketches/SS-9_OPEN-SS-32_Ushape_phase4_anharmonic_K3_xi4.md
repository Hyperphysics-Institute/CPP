# SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 4 anharmonic K$_3$ $\xi^4$ scoping

**Date:** 5 May 2026 (Session 16)
**Status:** RULED OUT — tenth programme-level negative result; fifth in the OPEN-SS-32 ↔ U-shape thread.
**Strengthening:** closure extends from "first-order $\xi^4$ ruled out" (the originally-scoped falsifier) to "**all-orders perturbative correction in the Gaussian-K$_3$ framework rigorously ruled out by variational argument**".
**Companion script:** `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-32_Ushape_phase4_anharmonic_K3_xi4.py`.

---

## 1. Strategy

Phase 3B-B (Session 15) formally closed R2 (cluster-scale $\leftrightarrow$ alpha-scale unification at canonical $\sigma_{K3}$) on the **n-vs-N structural argument**: no belt-IRREP-projection mechanism whose variance content scales with the cyclic order $n$ (which is non-monotonic in $N$ across the J-solid range, $n = 3, 5, 2, 3, 4$ for $N = 5, 7, 8, 9, 10$) can produce the empirically monotonic-in-$N$ U-shape. Both registered candidates for OPEN-SS-35 sub-question (a) A-scaling closure are now ruled out (R1 Session 12, R2 Session 15).

Phase 4 attacks the same OPEN-SS-32 ↔ U-shape question from a **different direction**: instead of staying within the harmonic Hessian and asking which IRREP subspace projects right, we ask **what happens at next order in the Gaussian expansion**. The handover-suggested falsifier (Session 15 §4 forward pointer Priority 1) was: compute the perturbative anharmonic correction at order $\xi^4$, sum over edges, and check (i) magnitude ~ 5–10 % of binding and (ii) monotonic-in-$N$ pattern. If both pass, scope a multi-session derivation; if either fails, ruled out.

The actual computation reveals a **third falsifier that the original scoping plan did not anticipate**: the **sign**. The Taylor coefficient of $\xi^4$ in the Gaussian expansion is negative (softening), the harmonic ground-state expectation $\langle \xi^4 \rangle_0 = 3 \langle \xi^2 \rangle_0^2 > 0$, and the perturbative energy shift is therefore negative — *more* binding, not less. The empirical J-solid range needs the opposite sign. This decoupling is structural, and (as developed in §4.2) extends to **all orders in the Gaussian expansion** by a variational argument independent of computation.

## 2. Model and computation

### 2.1 The K$_3$ pair potential and its Taylor expansion

$$ V_{\rm pair}(\xi) \;=\; -\, B_{\rm pair}\,\exp\!\bigl(-\xi^2/2\bigr), \quad \xi \equiv \delta r/\sigma_{K3}. $$

Taylor expansion around equilibrium ($\xi = 0$):

$$ V_{\rm pair}(\xi) \;=\; -B_{\rm pair} \;+\; \tfrac{B_{\rm pair}}{2}\,\xi^2 \;-\; \tfrac{B_{\rm pair}}{8}\,\xi^4 \;+\; \tfrac{B_{\rm pair}}{48}\,\xi^6 \;-\; \tfrac{B_{\rm pair}}{384}\,\xi^8 \;+\; \cdots $$

The **harmonic part** $-B_{\rm pair} + (B_{\rm pair}/2)\xi^2$ is what Phases 2 / 3A / 3B-A / 3B-B used (giving the per-edge spring constant $k_{\rm edge} = B_{\rm pair}/\sigma^2$). The **leading anharmonic** is $V_4 = -(B_{\rm pair}/8)\xi^4$ — Taylor coefficient negative.

### 2.2 First-order perturbation theory

For each polytope, the harmonic Hessian (Phase 3A construction, verbatim) is built and diagonalized. Per-edge zero-point variance $\langle \delta r_{ab}^2 \rangle_0$ is accumulated by summing the contribution from each vibrational normal mode:

$$ \langle \delta r_{ab}^2 \rangle_0 \;=\; \sum_{i \in {\rm vib}} \frac{\hbar c}{2 \sqrt{m_\alpha\, \lambda_i}}\; \bigl| \langle \mathbf{e}_{ab}\, |\, \mathbf{u}_i \rangle \bigr|^2, $$

where $\mathbf{e}_{ab}$ is the unit edge-stretch direction in the $3N$-dimensional displacement space and $\mathbf{u}_i$ are normal-mode eigenvectors. The first-order anharmonic energy correction per cluster, using Wick's theorem ($\langle \xi^4 \rangle_{\rm HOgs} = 3 \langle \xi^2 \rangle_{\rm HOgs}^2$):

$$ \boxed{\; \Delta E^{(1)}_{\rm anharm} \;=\; -\,\frac{3 B_{\rm pair}}{8 \sigma_{K3}^4}\; \sum_{\{ab\} \in E}\; \langle \delta r_{ab}^2 \rangle_0^{\,2} \;<\; 0. \;} $$

### 2.3 All-orders Gaussian average

The perturbative ξ⁴ estimate is dimensionally consistent only when $s \equiv \langle \xi^2 \rangle_0$ is small. Computation reveals $s_{\rm avg} \approx 0.85$ across all polytopes (J-solid range $s_{\rm avg} \in [0.847, 0.853]$), putting the cluster near $\xi_{\rm rms} \approx 0.92$ — close to the inflection point of $\exp(-\xi^2/2)$ at $\xi = 1$. Higher-order Taylor terms are not numerically small. The all-orders Gaussian average computed in the (still-harmonic) ground state, treating the harmonic GS as a Gaussian trial wavefunction with per-edge variance $s$:

$$ \langle V_{\rm pair} \rangle_{\rm HOgs} \;=\; -\,B_{\rm pair}\, (1 + s)^{-1/2}, $$

yielding the all-orders cluster-total anharmonic shift

$$ \Delta E_{\rm anharm}^{\rm all\text{-}orders} \;=\; -\, B_{\rm pair}\; \sum_{\{ab\} \in E}\; \Bigl[(1 + s_{ab})^{-1/2} \;-\; \bigl(1 - \tfrac{s_{ab}}{2}\bigr)\Bigr] \;=\; -\, B_{\rm pair}\, \sum_{\{ab\}}\, f(s_{ab}), $$

with $f(s) \equiv (1+s)^{-1/2} - 1 + s/2$.

### 2.4 The sign theorem

**Theorem (universal sign of Gaussian-K$_3$ anharmonic correction).** For every $s > 0$, the all-orders anharmonic energy shift in the harmonic-GS variational ansatz, $\Delta E_{\rm anharm} = -B_{\rm pair}\, f(s)$, is strictly negative.

**Proof.** $f(0) = 0$. $f'(s) = -\tfrac{1}{2}(1+s)^{-3/2} + \tfrac{1}{2} = \tfrac{1}{2}\bigl[1 - (1+s)^{-3/2}\bigr]$. For $s > 0$, $(1+s)^{-3/2} < 1$, so $f'(s) > 0$. Hence $f$ is strictly increasing on $(0, \infty)$ with $f(0) = 0$, giving $f(s) > 0$. Therefore $\Delta E_{\rm anharm} = -B_{\rm pair}\, f(s) < 0$ for all $s > 0$. $\quad \square$

**Variational corollary.** By Rayleigh-Ritz, the true ground state energy of the full Gaussian Hamiltonian is bounded above by the harmonic-GS-trial expectation: $E^{\rm full}_0 \le \langle T + V_{\rm full} \rangle_{\rm HOgs} = E^{\rm harm}_0 + \Delta E_{\rm anharm}^{\rm all\text{-}orders} < E^{\rm harm}_0$. The true cluster ground state is *more* bound than the harmonic estimate. No reordering or improvement of perturbative scheme can flip this.

## 3. Results

### 3.1 Per-cluster anharmonic correction table

Reproduced verbatim from script run output (canonical $\sigma_{K3} = 1.68$ fm; constants $B_{\rm pair} = M_0/\varphi = 2.342$ MeV, $R_\alpha = 2.37$ fm, $m_\alpha = 3727.4$ MeV/c²; anharmonic prefactor $3 B_{\rm pair}/(8\sigma^4) = 0.1103$ MeV/fm⁴):

| $N$ | sym | $\lvert E\rvert$ | $\langle s \rangle$ | $\Delta E^{(1)}_{\rm an}$ [MeV] | $\Delta E^{(1)}/\alpha$ [MeV] | $\Delta E^{(1)}/B_{K3}$ % | $-d_{\rm emp}$ % |
|-----|-----|------|---------------------|----------------------------------|--------------------------------|--------------------------|------------------|
| 4  | $T_d$  |  6 | 0.8634 |  $-3.93$  | $-0.98$ | $-27.96$ | $+24.56$ |
| 5  | $D_{3h}$ |  9 | 0.8529 |  $-5.75$  | $-1.15$ | $-27.28$ | $-23.86$ |
| 6  | $O_h$  | 12 | 0.8610 |  $-7.81$  | $-1.30$ | $-27.80$ | $-21.27$ |
| 7  | $D_{5h}$ | 15 | 0.8480 |  $-9.48$  | $-1.35$ | $-26.97$ | $-29.50$ |
| 8  | $D_{2d}$ | 18 | 0.8505 | $-11.44$  | $-1.43$ | $-27.13$ | $-31.81$ |
| 9  | $D_{3h}$ | 21 | 0.8493 | $-13.31$  | $-1.48$ | $-27.05$ | $-33.14$ |
| 10 | $D_{4d}$ | 24 | 0.8473 | $-15.14$  | $-1.51$ | $-26.92$ | $-33.58$ |
| 12 | $I_h$   | 30 | 0.8450 | $-18.81$  | $-1.57$ | $-26.77$ |  $+1.41$ |

### 3.2 Sign (F1) — **universal failure across all polytopes**

For every polytope, $\Delta E^{(1)}_{\rm anharm} < 0$ (more binding than harmonic estimate). The empirical J-solid range ($N = 5,\, 7,\, 8,\, 9,\, 10$) has $R_{\rm pct} > 0$ (clusters want to grow), corresponding to empirical binding *less* than the canonical K$_3$ prediction — i.e., requiring $\Delta E_{\rm empirical} > 0$. **Signs are uniformly opposite across the J-solid range.**

This was foreshadowed by the Taylor coefficient: $-(B_{\rm pair}/8)$ on $\xi^4$ is negative, and $\langle \xi^4 \rangle_0 > 0$ in any normalizable ground state, so the first-order shift is automatically negative.

### 3.3 All-orders Gaussian-average extension

| $N$ | sym | $\Delta E^{(1)}_{\xi^4}$ [MeV] | $\Delta E^{\rm all\text{-}orders}$ [MeV] | full / $\xi^4$ | sign |
|-----|-----|--------------------------------|------------------------------------------|----------------|------|
|  4 | $T_d$    |  $-3.93$ |  $-2.31$ | 0.588 | $-$ |
|  5 | $D_{3h}$ |  $-5.75$ |  $-3.40$ | 0.591 | $-$ |
|  6 | $O_h$    |  $-7.81$ |  $-4.60$ | 0.588 | $-$ |
|  7 | $D_{5h}$ |  $-9.48$ |  $-5.61$ | 0.592 | $-$ |
|  8 | $D_{2d}$ | $-11.44$ |  $-6.76$ | 0.591 | $-$ |
|  9 | $D_{3h}$ | $-13.31$ |  $-7.87$ | 0.591 | $-$ |
| 10 | $D_{4d}$ | $-15.14$ |  $-8.96$ | 0.592 | $-$ |
| 12 | $I_h$    | $-18.81$ | $-11.15$ | 0.593 | $-$ |

The all-orders summation reduces magnitude by ~40 % (factor $\sim 0.59$) due to higher-order Taylor terms that alternate in sign and partially cancel the leading $\xi^4$ overshoot. **The sign is preserved** — universally negative — consistent with the §2.4 sign theorem.

The factor $\sim 0.59$ being nearly polytope-independent reflects $\langle s \rangle$ being nearly polytope-independent: across all eight polytopes, $\langle s \rangle \in [0.845, 0.864]$, range only $\sim 2$ %. This near-constancy of mean per-edge variance across very different cluster geometries is itself a non-trivial empirical observation (see §5.2).

### 3.4 Magnitude (F2) — would have passed in isolation

| $N$ | sym | $\lvert\Delta E^{(1)} / B_{K3}\rvert$ % | $\lvert d_{\rm emp}\rvert$ % | ratio |
|-----|-----|------------------------------|------------------------|-------|
|  4 | $T_d$    | 27.96 | 24.56 | 1.14 |
|  5 | $D_{3h}$ | 27.28 | 23.86 | 1.14 |
|  6 | $O_h$    | 27.80 | 21.27 | 1.31 |
|  7 | $D_{5h}$ | 26.97 | 29.50 | 0.91 |
|  8 | $D_{2d}$ | 27.13 | 31.81 | 0.85 |
|  9 | $D_{3h}$ | 27.05 | 33.14 | 0.82 |
| 10 | $D_{4d}$ | 26.92 | 33.58 | 0.80 |
| 12 | $I_h$    | 26.77 |  1.41 | 18.92 |

In the J-solid range, $|\Delta E^{(1)} / B_{K3}|$ is in the range 27 % — within a factor of order unity of $|d_{\rm emp}|$ (21–34 %). Magnitude *would* have been judged consistent under the original Priority-1 scoping criterion. The icosahedron $N = 12$ overshoots empirical by factor $\sim 19$ because the all-orders correction is roughly polytope-independent (~27 % of well-bottom binding regardless of $N$) while the empirical $-d_{\rm emp}$ for $I_h$ is essentially zero (the ground state of ⁴⁸Cr clusters very near the canonical K$_3$ prediction).

### 3.5 Pattern (F3) — qualitatively consistent

Within the J-solid range only:

| $N$ | sym | $\lvert E\rvert$ | $\lvert\Delta E^{(1)}\rvert / \alpha$ [MeV] |
|-----|-----|------|-------------------|
|  5 | $D_{3h}$ |  9 | 1.150 |
|  7 | $D_{5h}$ | 15 | 1.354 |
|  8 | $D_{2d}$ | 18 | 1.430 |
|  9 | $D_{3h}$ | 21 | 1.479 |
| 10 | $D_{4d}$ | 24 | 1.514 |

$|\Delta E^{(1)}| / \alpha$ is monotonically increasing in $N$ across the J-solid range, with rate consistent (since $\langle s \rangle$ is near-constant) with the natural scaling

$$ |\Delta E^{(1)}| / \alpha \;\sim\; (3 B_{\rm pair}\, \langle s \rangle^2 / 8)\; \frac{|E|}{N} \;=\; (3 B_{\rm pair}\, \langle s \rangle^2 / 8)\; \frac{3N - 6}{N}, $$

where $(3N - 6)/N$ is a slowly increasing function of $N$ (1.8, 2.14, 2.25, 2.33, 2.4 for $N = 5, 7, 8, 9, 10$). Pattern is **qualitatively consistent** with empirical monotonic-in-$N$ — but pattern alone is necessary, not sufficient.

## 4. Verdict

### 4.1 F1 dispositive

F1 (sign) is the dispositive falsifier. It fails universally for the J-solid range. F2 and F3 cannot rescue it: if the predicted shift has the wrong sign, no adjustment of magnitude or pattern matters. **Phase 4 anharmonic K$_3$ $\xi^4$ at first order in perturbation theory: RULED OUT.**

### 4.2 The all-orders strengthening — programme-level closure

The §2.4 sign theorem combined with the Rayleigh–Ritz variational corollary establishes:

> **No perturbative or variational improvement of the harmonic K$_3$ ground-state estimate within the Gaussian-K$_3$ framework can produce less-than-harmonic binding.** The true cluster ground state in the full Gaussian-K$_3$ Hamiltonian is, with mathematical certainty, *more* bound than the harmonic prediction, never less.

This is not specific to first-order PT and not specific to the $\xi^4$ truncation. It follows from the fact that $f(s) \equiv (1+s)^{-1/2} - 1 + s/2 > 0$ for all $s > 0$, combined with Rayleigh–Ritz. Any computation within the Gaussian-K$_3$ framework that improves on harmonic must give *additional* binding.

But the empirical U-shape in the J-solid range requires the *opposite* — empirical binding is *less* than canonical K$_3$ at $\sigma_{K3} = 1.68$ fm. The conclusion is therefore **programme-level**:

> **The U-shape mechanism does not live within the Gaussian expansion of K$_3$ at fixed cluster geometry.**

Whatever produces empirical U-shape acts on a different physical channel:

- **(a) Modification of equilibrium geometry.** If the cluster equilibrium itself shifts with $N$ (effective $\sigma_{K3} = \sigma_{K3}(N)$, or equivalently effective $R_\alpha = R_\alpha(N)$), the canonical-$\sigma_{K3}$ K$_3$ prediction would be displaced from the true equilibrium and could give "less binding than canonical predicts" for J-solid $N$. **R1 (Session 12) registered this geometric-shift class as one realization and ruled it out** for the specific $R_\alpha(A)$ form considered. Other geometric-shift forms remain unconstrained.
- **(b) Coupling to inelastic excitations.** Alpha breathing modes, Hoyle-state $0^+_2$ mixing, or other non-rigid-cluster physics — coupling channels that the rigid-K$_3$ framework explicitly excludes. Could *reduce* effective binding by spectral repulsion (Hoyle is below cluster ground state in some kinematic windows).
- **(c) Physics outside K$_3$ entirely.** Surface-energy shape dependence (Strutinsky-like shell corrections, deformation-dependent surface area), Coulomb cluster-arrangement effects (sensitivity to specific geometric arrangement not captured by edge count alone), spin-orbit cluster corrections.

The U-shape mechanism must be sought in one of these channels — **none** of them is a Gaussian-K$_3$-internal correction.

### 4.3 Comparison with prior closures in the OPEN-SS-32 thread

| Phase | Mechanism tested | Falsifier | Status at close |
|-------|------------------|-----------|-----------------|
| Phase 2 | Uniform-only zero-point softening | Wrong magnitude (pattern flat in $N$) | RULED OUT |
| Phase 3A | Naive full-Hessian (all modes) | Wrong magnitude (~$-86$ % vs $-30$ % empirical) | RULED OUT |
| Phase 3B-A | Fixed-dimension belt subspace (monopole + 2D quadrupole) | Wrong shape (anti-correlated in $N$ within axial polytopes) | RULED OUT |
| Phase 3B-B | Full $C_n$ IRREP decomposition (3 variants B-B1/B-B2/B-B3) | n-vs-N structural argument (class-level closure) | RULED OUT — R2 FORMALLY CLOSED |
| **Phase 4** | **Anharmonic $\xi^4$ first-order PT, extended to all-orders Gaussian** | **F1 sign theorem (universal closure of Gaussian-K$_3$ framework)** | **RULED OUT** |

Phase 3B-B closed the harmonic-Hessian-belt-IRREP family at canonical $\sigma$. Phase 4 closes the Gaussian-K$_3$ perturbative-correction family at canonical geometry. Together: **the entire Gaussian-K$_3$ framework at fixed cluster geometry cannot produce the empirical U-shape.**

### 4.4 What this is *not*

This closure does **not** rule out:

- K$_3$ as the binding model (it remains the established framework for SS-7's twelve zero-parameter binding predictions).
- K$_3$-based mechanisms that **modify cluster geometry** (R1 was one specific realization; other geometric-shift forms remain).
- Hybrid mechanisms where K$_3$ is one term among several.
- Sub-question (b) layer 3 gap-strength closure work — this is **Decoupling-Theorem-protected** (Session 12) and unaffected by R2 / Phase 4 closures of the sub-question (a) avenue.

What it does rule out: the conjecture that adding next-order corrections to the harmonic K$_3$ at canonical $\sigma_{K3} = 1.68$ fm and canonical $R_\alpha = 2.37$ fm is the source of the U-shape pattern. Within that framework, the correction has the wrong sign at all orders.

## 5. Programme implications

### 5.1 Negative-result count

This is the **tenth** programme-level negative result (the ninth was Phase 3B-B at Session 15 close). The OPEN-SS-32 ↔ U-shape thread now contains five sequential falsifications. The cumulative effect is to have systematically eliminated the four most natural mechanisms within the Gaussian-K$_3$ framework at fixed canonical geometry:

1. Uniform softening (Phase 2)
2. Full-Hessian belt-projected (Phase 3A)
3. Fixed-dim belt-IRREP (Phase 3B-A)
4. Full $C_n$ belt-IRREP (Phase 3B-B)
5. Anharmonic $\xi^4$ / all-orders Gaussian (Phase 4)

Any future U-shape mechanism candidate must explain **why all five of these failed**. The §4.2 closure provides the unifying explanation: items 2–5 all stay within the Gaussian-K$_3$ framework at fixed geometry, and that framework provably gives the wrong sign of correction. Item 1 (Phase 2 uniform softening) was a different failure mode (pattern shape) but consistent with the closure.

### 5.2 Constructive content from Phase 4

Despite the negative result, Phase 4 contributes constructively:

- **The sign theorem (§2.4)** is a closure tool with broader applicability. Any future Gaussian-K$_3$ refinement must invoke geometry change, inelastic channels, or out-of-framework physics to escape it.
- **The near-constancy of $\langle s \rangle \approx 0.85$** across all eight polytopes (range only $\sim 2$ %) is a non-trivial empirical observation about the K$_3$ harmonic Hessian on rigid alpha-cluster geometry. It says that mean per-edge zero-point variance is essentially independent of cluster topology in the J-solid range. This explains why $|\Delta E / B_{K3}|$ is nearly constant at $\sim 27 %$ across the eight polytopes: the cluster topology drops out of the leading anharmonic correction in any framework where the mean variance is the dominant input.
- **The $\xi_{\rm rms} \approx 0.92$ regime** (near the inflection point of the Gaussian) is a quantitative caution flag for any future programme work assuming small-displacement perturbative expansion of K$_3$. The harmonic GS is past the regime where the expansion converges fast.

### 5.3 R2 closure and Decoupling-Theorem state unchanged

- **R2 remains FORMALLY CLOSED** (Session 15 Phase 3B-B). Phase 4 is a separate closure (Gaussian-K$_3$ framework, not R1/R2 specifically) but reinforces the broader pattern.
- **Decoupling Theorem (Session 12)** remains valid: sub-question (b) layer 3 gap-strength closure is independent of R2 / Phase 4 outcomes.
- **Sub-question (a) A-scaling closure**: both registered candidates (R1, R2) ruled out as of Session 15. After Phase 4, the **Gaussian-K$_3$ framework is provably empty of viable A-scaling closures**, requiring the U-shape mechanism to live in one of the §4.2 channels (a)–(c).

### 5.4 Pattern 6 K$_3$ scale recurrence at $\sigma_{K3} = 1.68$ fm

Phase 4 does not bear on Pattern 6 or its seven empirical instances. The K$_3$ scale recurrence is a fact about *where* the binding profile centers, not about how it deforms under zero-point motion. Phase 4 closure constrains only the latter.

## 6. Forward pointers

### 6.1 New Priority 1 (substantive new investigation)

**Cluster-geometry shift mechanisms beyond R1.** With the Gaussian-K$_3$ framework at fixed canonical geometry now closed (Phase 4 §4.2), the next natural candidate channel is geometric-shift mechanisms not captured by R1. R1 tested the specific $R_\alpha(A)$ form motivated by surface-tension scaling and ruled it out (Session 12). Other geometric-shift candidates remain:

- **(R3)** Cluster compression or expansion driven by **N-dependent boundary conditions**: each J-solid has different "surface" (number of edges per vertex, boundary topology), and equilibrium $R_\alpha$ may shift accordingly. Empirically this would manifest as $R_{\alpha,{\rm eff}}(N)$ values close to but not equal to 2.37 fm.
- **(R4)** Cluster shape distortion: the J-solid geometry minimizes pair-K$_3$ energy assuming uniform edge length, but with anisotropic perturbations the equilibrium shape may distort, breaking the rigid-J-solid assumption. Could couple monotonically with $N$ via the increasing complexity of the J-solid edge graph.

Both R3 and R4 can be made falsifiable in a single-session investigation: parameterize the geometric shift, compute the resulting K$_3$ binding shift, compare sign / magnitude / pattern against empirical.

### 6.2 New Priority 2 (substantive new investigation)

**Inelastic / out-of-framework channels.** §4.2 channels (b) and (c). Hoyle-state mixing, surface-energy shape dependence, Coulomb cluster-arrangement effects. These are multi-session by scope and require literature integration (cluster physics, Strutinsky shell corrections). Single-session scoping investigation feasible: estimate magnitudes of each channel, identify which is consistent with empirical sign/pattern.

### 6.3 Sub-question (b) layer 3 gap-strength closure (unchanged from Session 15)

Decoupling-Theorem-protected and unaffected by Phase 4. Session 11 Phase 1 candidate avenues remain on the table: (i) sharper-surface contributions from K$_3$ edge mechanism + Pauli-blocking; (ii) additional binding terms beyond Gaussian sum; (iii) L·S operator structure beyond Bohr-Mottelson form (intersects OPEN-SS-16 Layer B); (iv) recognition that magic-strength hierarchy may not be purely mean-field.

### 6.4 Anti-priorities (sharpened from Session 15)

The list of mechanisms ruled out within the Gaussian-K$_3$ framework at fixed geometry now includes **all** perturbative corrections at any order:

- Do **not** pursue further perturbative anharmonic refinement (ξ⁶, ξ⁸, hybrid PT schemes) within Gaussian-K$_3$ at fixed geometry — universally closed by §2.4 sign theorem.
- Do **not** pursue further belt-IRREP-projection variants — closed by Phase 3B-B n-vs-N argument.
- Do **not** pursue full point group $D_{nh} / D_{nd}$ extension — also closed by Phase 3B-B n-vs-N argument.
- Do **not** initiate SS-9 v0.3 → v0.1 `.tex` conversion (OPEN-ORG-012). §7 needs reformulation to reflect Phase 4 closure on top of the Phase 3B-B R2 closure. §7 has now shifted **six times** in the OPEN-SS-32 ↔ U-shape thread (was 5 at Session 15 close).
- Do **not** pursue further $V_{\rm SO}$ refinement within simple K$_3$ + HO + L·S framework (Session 11 Phase 1 ruled this out).
- Do **not** pursue further $R_\alpha(A)$ as energetic mechanism (Session 12 R1 ruled this out for the surface-tension form).

## 7. Summary

Phase 4 was scoped at Session 15 close as a **scoping investigation** with a two-criterion falsifier (magnitude + pattern). Computation revealed a third falsifier — sign — that resolves the question on dispositive grounds before either of the originally-planned criteria is needed. The sign analysis extends from "first-order $\xi^4$ has wrong sign" (a Taylor-coefficient observation) to "all-orders Gaussian-K$_3$ perturbative or variational corrections at fixed geometry have wrong sign" (a Rayleigh–Ritz argument with a one-line proof).

**Tenth programme-level negative result. Fifth in OPEN-SS-32 ↔ U-shape thread. R2 remains formally closed. Sub-question (a) A-scaling closure now requires geometric-shift or out-of-framework mechanisms (channels R3, R4, or §4.2 (b)/(c)) — Gaussian-K$_3$ at fixed canonical geometry is provably empty of viable candidates.**
