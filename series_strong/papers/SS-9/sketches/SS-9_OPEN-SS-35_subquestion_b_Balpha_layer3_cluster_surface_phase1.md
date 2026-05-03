# OPEN-SS-35 Sub-question (b) B-α Layer 3 — Cluster-Surface Form Factor (Path (i) Phase 1)

**Date:** 2 May 2026 (Session 11)
**Purpose:** First phase of the multi-session arc identified in Session 10 as Priority 1: cluster-surface Thomas-form spin-orbit. Compute matrix elements $\langle (1/r) \cdot dV_{K_3}/dr \rangle_{n,l}$ in HO basis to determine whether the K$_3$ Gaussian-modulated mean field's surface profile enhances $V_{\rm SO}^{\rm eff}$ for high-l states (which house the spin-orbit-driven empirical magics 28, 50, 82, 126).

**Companion files:**
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3_VSO_refinement.md` (Session 10 Routes 1a, 1b, 1c)
- `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3_cluster_surface_phase1.py` (reproducible computation)
- `Research_Frontier.md` OPEN-SS-35 entry

**Net programme effect:** **Path (i) cluster-surface Thomas-form spin-orbit RULED OUT as a magic-strength enhancement route.** The spherically-averaged K$_3$ Gaussian-modulated mean field at $A \sim 56$ produces an isotropic potential $V_{\rm avg}(r)$ whose Thomas-form weight $f_{\rm SO}(r) = (1/r) \cdot dV_{\rm avg}/dr$ peaks at the cluster *center* and decreases monotonically outward — the opposite of Bohr-Mottelson Woods-Saxon $df/dr/r$ which peaks sharply at the surface. Consequently, matrix elements $\langle f_{\rm SO} \rangle_{0,l}$ in HO basis *decrease* monotonically with $l$, from 7.41 MeV/fm$^2$ at $l=0$ to 2.14 MeV/fm$^2$ at $l=6$ (factor 3.5× reduction). With calibration $K \cdot \langle f_{\rm SO} \rangle_{0,0} = V_{\rm SO}^{\rm central} = 1.17$ MeV (Session 8 baseline), $V_{\rm SO}^{\rm eff}(l=6) = 0.338$ MeV — only 29% of central, *worse* than the uniform $V_{\rm SO}$ assumption of Session 9. The structural reason is identical to Session 10's Route 1b: the K$_3$ Gaussian-modulated mean field has a *fuzzy* surface ($\sigma_{\rm Gauss} \approx R_{\rm cluster}$, ratio 0.75), in contrast to Woods-Saxon's sharp surface ($a \ll R$, ratio $\sim 0.1$), so the surface-localized states see a gradually-varying gradient rather than a peak. This is the **fourth programme-level negative-result demonstration** in the OPEN-SS-35 closure programme (after Route D in Session 5 Phase 2, Route B-γ in Session 7 Phase 2, Route 1b in Session 10). Combined with Routes 1b, 1a-bound, and 1c-bound from Session 10, the diagnosis sharpens: **gap-strength closure of OPEN-SS-35 sub-question (b) Route B-α layer 3 cannot be achieved within the K$_3$ Gaussian-modulated mean field + HO + L·S + V_SO refinement framework**, regardless of how V_SO is parametrized (central, surface, higher-order relativistic). Closure of layer 3 gap-strength requires CPP physics *beyond* the simple K$_3$ Gaussian mean field. Sub-question (b) Route B-α layer 3 status: "bounded refinement: simple HO + L·S framework saturates at $V_{\rm SO}/\hbar\omega \approx 0.11$" (Session 10) → "**the K$_3$ Gaussian-modulated mean field framework is fundamentally insufficient for magic-strength gap closure; gap-strength match requires additional CPP physics beyond the smooth Gaussian-bottom mean field**" (this Session 11 Phase 1). Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged. OPEN-SS-35 closure trajectory: 6 programme-level stages preserved (Phase 1 refines stage (vi) but does not add new stage). Path (ii) numerical diagonalization status: still formally open but with substantially reduced expectations — the structural deficiency identified in Phase 1 is geometric (Gaussian shape, fuzzy surface), not perturbative.

---

## §1. Strategy

Session 10 established the bound of the simple HO + L·S + V_SO refinement framework at $V_{\rm SO}/\hbar\omega \approx 0.11$, about half the empirical strong-magic threshold (0.20–0.25). The diagnosis identified two multi-session paths for further closure:

> **Path (i):** Cluster-surface Thomas-form spin-orbit. Compute $V_{\rm SO}^{\rm eff}$ as $\langle \xi(r) \rangle_{n,l}$ with $\xi(r) \propto -(1/r) \cdot dV/dr$ peaking at the cluster boundary — the Bohr-Mottelson form factor that empirically produces magic-strength gaps for high-l j-shell partners.
>
> **Path (ii):** Numerical diagonalization beyond Taylor expansion. Captures cluster-edge effects and high-N physics where central Taylor expansion fails.

Phase 1 of Path (i) tests the central question: **does the K$_3$ Gaussian-modulated mean field's spherically-averaged form factor amplify $V_{\rm SO}^{\rm eff}$ for high-l surface-localized states, in the way Bohr-Mottelson Woods-Saxon does?**

The empirical magic-strength gaps at 28, 50, 82, 126 close on high-l j-shell partners (1f$_{7/2}$, 1g$_{9/2}$, 1h$_{11/2}$, 1i$_{13/2}$). For these orbitals to produce *strong* gaps, $V_{\rm SO}^{\rm eff}$ must be sufficient to push the j=l+1/2 orbital below the next HO shell. In Bohr-Mottelson, this works because the surface form factor enhances spin-orbit precisely for these high-l states. The CPP question: does the K$_3$ mean field do the same?

If Phase 1 shows enhancement, layer 3 magic-strength closure is achievable through Path (i). If Phase 1 shows reduction or l-independence, Path (i) is ruled out and the closure path must move outside the simple K$_3$ Gaussian-modulated mean field framework.

---

## §2. Cluster geometry and spherically-averaged K$_3$ potential

For the magic-strength test case $A = 56$ (deltahedron-core configuration with $N_\alpha = 14$ alphas), model the cluster as a thin spherical shell of $N_\alpha$ alphas at radius $R_{\rm cluster}$. Each alpha contributes a Gaussian to $V_{K_3}$ with depth $V_0 = B_{\rm pair} \cdot \langle\deg\rangle = 2.342 \cdot 5 = 11.71$ MeV and width $\sigma = \hbar c / \sqrt{m_n c^2 \cdot \hbar\omega} = 1.7855$ fm.

**Spherically-averaged K$_3$ shell potential:**
$$V_{\rm avg}(r) = -\frac{N_\alpha V_0 \sigma^2}{2 r R_{\rm cluster}} \left[ \exp\!\left(-\frac{(r-R_{\rm cluster})^2}{2\sigma^2}\right) - \exp\!\left(-\frac{(r+R_{\rm cluster})^2}{2\sigma^2}\right) \right] \tag{1}$$

(Standard derivation via $\int_{\rm shell} \exp(-|r - R'|^2/2\sigma^2) \, d\Omega_{R'}$ for shell of radius $R$.)

With $R_{\rm cluster} = 2.37$ fm (alpha-vertex radius, using $A = 48$ icosahedron value as proxy for $A = 56$ deltahedron-core):

$$V_{\rm avg}(0) = -N_\alpha V_0 \exp(-R_{\rm cluster}^2/2\sigma^2) = -14 \cdot 11.71 \cdot \exp(-0.881) = -67.93 \text{ MeV}$$

| $r$ (fm) | $V_{\rm avg}(r)$ (MeV) |
|---|---|
| 0.0 | $-67.93$ |
| 1.0 | $-63.57$ |
| 2.0 | $-51.20$ |
| 2.37 | $-45.15$ |
| 3.0 | $-34.13$ |
| 5.0 | $-7.45$ |
| 7.0 | $-0.55$ |
| 10.0 | $-0.001$ |

The potential has a Gaussian-bottom interior and decays to zero exterior to the cluster. Crucially, the surface region is **fuzzy**: $\sigma/R_{\rm cluster} = 0.75$, so the Gaussian width is comparable to the cluster radius, giving a smooth, slow transition rather than the sharp Woods-Saxon surface ($a/R \sim 0.1$).

---

## §3. Thomas-form weight $f_{\rm SO}(r) = (1/r) \cdot dV_{\rm avg}/dr$

The Bohr-Mottelson Thomas-form spin-orbit term involves the spatial weight $\xi(r) = K \cdot (1/r) \cdot dV/dr$ where $K$ is a coupling constant with units of fm$^2$. The matrix element $\langle \xi(r) \rangle_{n,l}$ in state $|n,l\rangle$ gives the effective spin-orbit strength for that orbital.

Numerical profile of $f_{\rm SO}(r) = (1/r) \cdot dV_{\rm avg}/dr$ for the K$_3$ cluster shell:

| $r$ (fm) | $f_{\rm SO}(r)$ (MeV/fm$^2$) |
|---|---|
| 0.01 | 8.794 |
| 0.5 | 8.764 |
| 1.0 | 8.640 |
| 1.5 | 8.338 |
| 2.0 | 7.779 |
| 2.37 (= $R_{\rm cluster}$) | 7.178 |
| 3.0 | 5.844 |
| 4.0 | 3.432 |
| 5.0 | 1.526 |
| 7.0 | 0.124 |

**Key observation:** $f_{\rm SO}(r)$ peaks at the cluster center ($r \to 0$) and decreases *monotonically* outward. This is the **opposite** of the Bohr-Mottelson Woods-Saxon $f_{\rm SO}^{\rm WS}(r)$, which peaks at the cluster surface (where $df/dr$ is sharp). The structural reason: for the K$_3$ Gaussian-modulated mean field with $\sigma \approx R$, the gradient $-dV/dr$ peaks at intermediate $r \sim \sigma$ but is divided by the same $r$, and the smooth Gaussian shape gives a peak at the origin rather than a peak displaced to the surface.

For comparison, pure HO would give $f_{\rm SO}^{\rm HO}(r) = m_n \omega^2 = 4.08$ MeV/fm$^2$ uniformly. The K$_3$ shell exceeds this in the interior ($f_{\rm SO}(r=0) = 8.79$ MeV/fm$^2$, factor 2.16× higher than asymptotic HO) and falls below it in the exterior ($f_{\rm SO}(r=5) = 1.53$ MeV/fm$^2$, factor 0.37× lower).

---

## §4. Matrix elements $\langle f_{\rm SO} \rangle_{0,l}$ in HO basis

For ground-state HO orbitals $|n=0, l\rangle$ with width $a = \sigma$ (self-consistent K$_3$/HO matching):
$$R_{0,l}(r) = \sqrt{\frac{2}{a^3 \Gamma(l+3/2)}} \cdot \left(\frac{r}{a}\right)^l \exp\!\left(-\frac{r^2}{2a^2}\right) \tag{2}$$

Spatial extent (mean radius $\langle r \rangle$ and rms radius):

| $l$ | orbital | $\langle r \rangle$ (fm) | $\sqrt{\langle r^2 \rangle}$ (fm) | location relative to $R_{\rm cluster} = 2.37$ fm |
|---|---|---|---|---|
| 0 | 1s | 2.015 | 2.187 | inside cluster |
| 3 | 1f | 3.684 | 3.788 | beyond cluster surface |
| 4 | 1g | 4.093 | 4.187 | well beyond surface |
| 5 | 1h | 4.465 | 4.552 | well beyond surface |
| 6 | 1i | 4.809 | 4.890 | well beyond surface |

The spin-orbit-driven magic orbitals (1f, 1g, 1h, 1i) have wavefunctions that peak *outside* the cluster shell, in the region where $f_{\rm SO}(r)$ has decayed substantially.

**Matrix elements** $\langle 0, l | f_{\rm SO}(r) | 0, l \rangle = \int_0^\infty |R_{0,l}(r)|^2 \cdot f_{\rm SO}(r) \cdot r^2 \, dr$:

| $l$ | orbital | $\langle f_{\rm SO} \rangle_{0,l}$ (MeV/fm$^2$) | ratio to $l=0$ |
|---|---|---|---|
| 0 | 1s | 7.4098 | 1.000 |
| 1 | 1p | 6.3112 | 0.852 |
| 2 | 1d | 5.2432 | 0.708 |
| 3 | 1f | 4.2742 | 0.577 |
| 4 | 1g | 3.4326 | 0.463 |
| 5 | 1h | 2.7234 | 0.367 |
| 6 | 1i | 2.1391 | 0.289 |

**Matrix elements decrease monotonically with $l$, from 7.41 MeV/fm$^2$ at $l=0$ to 2.14 MeV/fm$^2$ at $l=6$ — a factor of 3.5× reduction.**

---

## §5. $V_{\rm SO}^{\rm eff}(l)$ via calibration to Session 8 baseline

Anchor the proportionality constant $K$ to the Session 8 baseline value $V_{\rm SO}^{\rm central} = 1.17$ MeV at $l = 0$:
$$K = \frac{V_{\rm SO}^{\rm central}}{\langle f_{\rm SO} \rangle_{0,0}} = \frac{1.17}{7.4098} = 0.158 \text{ fm}^2 \tag{3}$$

(For reference: bare relativistic Thomas value $K_{\rm bare} = (\hbar c)^2/[2(m_n c^2)^2] = 0.022$ fm$^2$. The CPP-internal calibration gives $K$ about 7× larger, consistent with the $(v_F/c)^2 \cdot \hbar\omega$ formulation in Session 8 which incorporates non-Thomas SSV-PSR_eff coupling.)

**Resulting $V_{\rm SO}^{\rm eff}(l)$:**

| $l$ | orbital | empirical magic | $V_{\rm SO}^{\rm eff}$ (MeV) | $V_{\rm SO}^{\rm eff}/\hbar\omega$ | fraction of strong-magic threshold (0.20) |
|---|---|---|---|---|---|
| 0 | 1s | – | 1.170 | 0.0900 | 45% |
| 1 | 1p | 8 | 0.997 | 0.0767 | 38% |
| 2 | 1d | 20 | 0.828 | 0.0637 | 32% |
| 3 | 1f | **28** | 0.675 | 0.0519 | 26% |
| 4 | 1g | **50** | 0.542 | 0.0417 | 21% |
| 5 | 1h | **82** | 0.430 | 0.0331 | 17% |
| 6 | 1i | **126** | 0.338 | 0.0260 | 13% |

**The orbitals responsible for empirical strong magics 28, 50, 82, 126 (l = 3, 4, 5, 6) get** *progressively weaker* **$V_{\rm SO}^{\rm eff}$ in the cluster-surface treatment**, reaching only 13% of the strong-magic threshold at $l=6$. This is *worse* than Session 9's uniform $V_{\rm SO} = 1.17$ MeV assumption (which gave 45% of threshold for all l).

---

## §6. Why the K$_3$ Gaussian-modulated mean field gives the wrong direction

The structural reason for the wrong-direction result is **identical to Session 10's Route 1b finding**: the K$_3$ Gaussian-modulated mean field has a *fuzzy* surface, in contrast to the *sharp* Woods-Saxon surface that Bohr-Mottelson uses.

**Comparison of surface profiles:**

| profile | depth $V_0$ | width $a$ or $\sigma$ | $a/R$ ratio | gradient peak |
|---|---|---|---|---|
| Bohr-Mottelson WS | $\sim 50$ MeV | $a \approx 0.5$ fm | $\sim 0.1$ | sharply at $r = R$ |
| CPP K$_3$ Gaussian shell | 67.9 MeV (well depth) | $\sigma = 1.785$ fm | 0.75 | smoothly displaced from $R$ |

For Woods-Saxon with $a/R \sim 0.1$, the form factor $df/dr$ has FWHM $\sim a$ centered at $r = R$, giving a sharp peak that strongly weights surface-localized wavefunctions. For CPP K$_3$ with $\sigma/R = 0.75$, the gradient is broad and peaks near the origin (after dividing by $r$), giving negligible enhancement at the surface.

**This is a structural property of the K$_3$ Gaussian-modulated mean field at A~56 that cannot be fixed by parameter adjustment within the same mean-field shape.** To reach Bohr-Mottelson-like surface enhancement, the K$_3$ mean field would need an effective "sharpness ratio" $a/R \sim 0.1$ rather than 0.75 — a structural change requiring additional physics beyond the smooth Gaussian-bottom shape.

---

## §7. Path (i) verdict: RULED OUT

**Path (i) cluster-surface Thomas-form spin-orbit is ruled out as a magic-strength enhancement route in the K$_3$ Gaussian-modulated mean field framework**, on the same structural grounds as Session 10's Route 1b:

1. **Wrong sign:** $V_{\rm SO}^{\rm eff}(l)$ *decreases* monotonically with $l$, opposite of empirical Bohr-Mottelson where surface form factor enhances high-l spin-orbit.
2. **Magnitude:** at $l = 6$ (1i$_{13/2}$, magic 126), $V_{\rm SO}^{\rm eff} = 0.338$ MeV — only 29% of the central baseline 1.17 MeV, and only 13% of the empirical strong-magic threshold.
3. **Structural origin:** the K$_3$ Gaussian-modulated mean field has a fuzzy surface ($\sigma/R = 0.75$), in contrast to the sharp Woods-Saxon surface ($a/R \sim 0.1$) that produces empirical enhancement.

This is the **fourth programme-level negative-result demonstration** in the OPEN-SS-35 closure programme:

| # | route | session | finding |
|---|---|---|---|
| 1 | Route D | Session 5 Phase 2 | direct lattice-shell counting fails |
| 2 | Route B-γ | Session 7 Phase 2 | K$_3$-mode phase coupling fails |
| 3 | Route 1b | Session 10 | central anharmonic correction wrong sign |
| 4 | Path (i) | Session 11 Phase 1 | cluster-surface form factor wrong direction |

The progressive ruling-out of candidate routes sharpens the diagnosis: **the empirical magic-strength gap closure of OPEN-SS-35 sub-question (b) Route B-α layer 3 cannot be achieved within the K$_3$ Gaussian-modulated mean field + simple HO + L·S + V_SO refinement framework, regardless of how V_SO is parametrized.**

---

## §8. Implications for Path (ii) numerical diagonalization

**Path (ii)** (numerical diagonalization of the full K$_3$ Gaussian-modulated Hamiltonian) remains formally open but with substantially reduced expectations after Phase 1.

The structural deficiency identified in Phase 1 is **geometric**, not perturbative: the K$_3$ Gaussian shape has a fuzzy surface that doesn't produce sharp gradient features. Numerical diagonalization can capture cluster-edge effects more accurately than HO-basis perturbation theory, but it cannot change the fundamental shape of the mean field. If the smooth Gaussian-bottom shape is the issue, no amount of computational refinement of the same shape will fix it.

Path (ii) might still produce a different result if:
- The actual K$_3$ mean field eigenstates have substantially different surface localization than HO basis suggests (e.g., bound only to the cluster, not extending beyond)
- The full deltahedron geometry (not spherical average) produces sharper local features at vertex positions

But the *qualitative* expectation is that Path (ii) will refine but not reverse Phase 1's conclusion.

---

## §9. Programme implications

**Sub-question (b) Route B-α layer 3 status further refined:** "bounded refinement: simple HO + L·S framework saturates at $V_{\rm SO}/\hbar\omega \approx 0.11$" (Session 10) → "**the K$_3$ Gaussian-modulated mean field framework is fundamentally insufficient for magic-strength gap closure; gap-strength match requires additional CPP physics beyond the smooth Gaussian-bottom mean field**" (this Session 11 Phase 1).

**Path (i) RULED OUT** (4th programme-level negative result).

**Path (ii) status:** still formally open but with reduced expectations. Geometric deficiency (fuzzy surface) is shape-level, not perturbation-level.

**OPEN-SS-35 closure trajectory: 6 programme-level stages preserved.** Phase 1 refines stage (vi) but does not advance to a new stage. The first qualitative cross-paradigm consilience claim (Session 9: empirical magic-number sequence reproduced from CPP first-principles) remains intact. **Magic-strength closure is now identified as outside the simple K$_3$ Gaussian + HO + L·S framework.**

**Identification of further-future physics needed:** to achieve empirical magic-strength gap closure, CPP needs to bring in physics beyond the smooth K$_3$ Gaussian-modulated mean field. Candidate avenues:
- **(a)** Sharper-surface contributions to the K$_3$ mean field (e.g., from K$_3$ edge mechanism interacting with Pauli-blocking at the cluster boundary)
- **(b)** Additional binding terms beyond the Gaussian sum (e.g., higher-order K$_3$ modes, color-coupling terms at cluster-internal scale)
- **(c)** L·S operator structure beyond Bohr-Mottelson form (interacts with OPEN-SS-16 Layer B work)
- **(d)** Recognition that empirical magic-strength hierarchy may not be solely a mean-field-shell-model property: pairing, deformation, and other nuclear-structure effects could contribute, and CPP's simple shell-model framework may not be the right comparison

These are all multi-session avenues. Phase 1's negative result substantially clarifies what the closure programme cannot rely on; pivoting to alternative avenues is appropriate.

**Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.** Phase 1 uses existing K$_3$ mean field machinery (instance 7: K$_3$ at nucleon-orbital scale); no new K$_3$ scale-recurrence instance.

---

## §10. Forward-looking pointers

**Priority 1 (programme pivot):** Recognize that gap-strength closure requires physics outside the simple K$_3$ Gaussian + HO + L·S framework, and pivot the OPEN-SS-35 closure programme accordingly. Multi-session decision point. Single-session-tractable subtasks:
- Survey OPEN-SS-16 Layer B (operator structure of L·S) for whether layer 2 closure can produce relevant new physics
- Survey sub-question (a) A-scaling closure (R1 or R2 from Session 7 Phase 1) for whether $\hbar\omega$ refinement affects the closure picture

**Priority 2 (Path (ii) with reduced expectations):** Numerical diagonalization of full K$_3$ Hamiltonian to confirm Phase 1's qualitative conclusion. Multi-session by scope, reduced priority after Phase 1 result.

**Priority 3:** Pursue avenues (a)-(d) above for additional CPP physics that could close gap-strength match. Each is multi-session by scope; (d) might reframe the closure programme entirely.

**Priority 4:** Sub-question (a) A-scaling closure (R1 or R2). Single-session-tractable. May yield refined $\hbar\omega$ or alternative interpretation that affects the layer 3 picture.

**Anti-priority:** Do not pursue further refinement of V_SO within the simple K$_3$ Gaussian + HO + L·S framework. Phase 1 has demonstrated that this framework cannot achieve gap-strength closure regardless of how V_SO is parametrized.

---

## §11. Summary

**Session 11 Phase 1 establishes that the K$_3$ Gaussian-modulated mean field's spherically-averaged Thomas-form spin-orbit weight $f_{\rm SO}(r) = (1/r) \cdot dV_{\rm avg}/dr$ peaks at the cluster center, not the surface** (in contrast to Bohr-Mottelson Woods-Saxon, whose $df/dr/r$ peaks at the surface). Consequently, matrix elements $\langle f_{\rm SO} \rangle_{0,l}$ in HO basis decrease monotonically from 7.41 MeV/fm$^2$ at $l = 0$ to 2.14 MeV/fm$^2$ at $l = 6$ — factor 3.5× reduction. With calibration to Session 8 baseline at $l = 0$, $V_{\rm SO}^{\rm eff}(l = 6) = 0.338$ MeV, only 13% of the empirical strong-magic threshold.

**Path (i) cluster-surface Thomas-form spin-orbit RULED OUT** as a magic-strength enhancement route in the K$_3$ Gaussian-modulated mean field framework. Fourth programme-level negative-result demonstration in OPEN-SS-35 closure programme.

**Structural diagnosis:** the K$_3$ Gaussian-modulated mean field has a *fuzzy* surface ($\sigma/R = 0.75$ at $A = 56$), in contrast to Woods-Saxon's *sharp* surface ($a/R \sim 0.1$). The geometric deficiency is shape-level and cannot be fixed by parameter adjustment within the same Gaussian-bottom shape.

**Programme effects:**
- Sub-question (b) Route B-α layer 3 status further refined: gap-strength closure requires physics *beyond* the simple K$_3$ Gaussian + HO + L·S + V_SO refinement framework.
- Path (i) RULED OUT.
- Path (ii) status: reduced expectations (geometric deficiency is shape-level, not perturbation-level).
- OPEN-SS-35 closure trajectory: 6 programme-level stages preserved; Phase 1 refines stage (vi).
- First qualitative cross-paradigm consilience claim (Session 9) remains intact.
- Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.

**The OPEN-SS-35 closure programme has now narrowed substantially: four candidate routes/paths have been ruled out, with the diagnosis pointing toward additional CPP physics outside the simple K$_3$ Gaussian-modulated mean field as the requirement for magic-strength gap closure.**
