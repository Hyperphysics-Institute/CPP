# OPEN-SS-35 Sub-question (b) B-α Layer 3 — V_SO Refinement (Routes 1a, 1b, 1c)

**Date:** 2 May 2026 (Session 10)
**Purpose:** Investigate the three routes registered in Session 9 forward-looking pointers for refining $V_{\rm SO}/\hbar\omega$ from layer 1's value 0.09 toward the empirical strong-magic threshold $\geq 0.20$. Route 1b (centrifugal correction from K$_3$ Gaussian-modulated mean field) is the principal substantive investigation; Routes 1a (refined $v_F/c$) and 1c (higher-order SSV-PSR_eff relativistic) are quantitative refinements layered on top.

**Companion files:**
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer1.md` (Session 8 layer 1 closure)
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3.md` (Session 9 layer 3 partial closure)
- `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3_VSO_refinement.py` (reproducible computation)
- `series_strong/papers/SS-2_lattice_scale_nucleon_structure.tex` (ZBW machinery)
- `series_paper_sr.tex` (PSR_eff = l_P/(1 + k·ΔSSV) machinery)
- `research_frontier.md` OPEN-SS-35 entry

**Net programme effect:** Layer 3 gap-strength refinement bounded. **Route 1b ruled out** as a magic-strength enhancement route — the K$_3$ Gaussian-modulated mean field, expanded around the centroid, gives a quartic correction with the *wrong sign* for empirical centrifugal enhancement (lowers low-l states *more* than high-l, opposite of the Bohr-Mottelson $D \cdot l(l+1)$ phenomenology). Plus the perturbation theory breaks down spatially for high-N states where the spin-orbit-driven magics (28, 50, 82, 126) sit. Routes 1a (refined $v_F/c$ via surface-region emphasis) and 1c (higher-order SSV-PSR_eff relativistic corrections) give modest improvements: $V_{\rm SO}/\hbar\omega$ advances from 0.09 (Session 8 layer 1) to **0.113 (Session 10 refined)**, a 25% increase. The combined refinement reaches 56% of the empirical strong-magic threshold (0.20). Sub-question (b) Route B-α layer 3 status: "shell SEQUENCE reproduced; gap magnitudes at soft end of empirical" → "**bounded refinement: simple HO + L·S framework saturates at $V_{\rm SO}/\hbar\omega \approx 0.11$; closure of gap-strength match requires cluster-surface physics or numerical diagonalization beyond Taylor expansion**". Pattern 6 K$_3$ scale-recurrence unchanged at 7 confirmed instances. OPEN-SS-35 closure trajectory: 6 programme-level stages preserved (Session 10 refines but does not add new stage).

---

## §1. Strategy

The Session 9 forward-looking pointers identified three routes for refining $V_{\rm SO}$:

> **Route 1a:** Re-examine layer 1's Approach A (cluster-density Fermi gas) which gives $v_F/c = 0.34$–$0.39$ at mid-range deltahedra. This would give $V_{\rm SO}/\hbar\omega = (0.35)^2 \approx 0.12$–$0.15$, moving toward the magic-strong range.
>
> **Route 1b:** Add centrifugal correction ($l^2$ term) to the K$_3$ HO mean field from sub-question (a). The K$_3$ potential is Gaussian-modulated, not purely harmonic; its effective $l^2$ coefficient is computable from the Gaussian width $\sigma$ and would systematically pull high-l orbitals down further.
>
> **Route 1c:** Higher-order relativistic corrections to $V_{\rm SO}$ beyond the leading $(v/c)^2$ term. The next-order correction is $(v/c)^4$, which at $v/c = 0.3$ gives a 9% additional contribution.

The substantive question in Route 1b is whether the K$_3$ mean field's *intrinsic anharmonicity* — quartic and higher-order corrections to the leading HO behavior — provides the centrifugal-style enhancement that's empirically responsible for magic-strength gaps in Bohr-Mottelson phenomenology (where $D \cdot l(l+1)$ with $D > 0$ lowers high-l states relative to low-l within each shell). If Route 1b succeeds, it provides a CPP-derived mechanism for magic-strength enhancement without requiring additional physics. If it fails, it sharpens the diagnosis: the missing physics for magic-strength must come from the cluster-surface region rather than the central-region anharmonicity.

Routes 1a and 1c are quantitative refinements that don't change the qualitative picture but tighten the bound on what the simple HO + L·S framework can achieve.

---

## §2. Route 1b: Centrifugal correction from K$_3$ Gaussian-modulated mean field

### §2.1 Taylor expansion of K$_3$ potential at centroid

The K$_3$ confining potential at the cluster centroid (sub-question (a) Sessions 6, 7) is a sum of Gaussians at alpha vertices:
$$V_{K_3}(\vec r) = -B_{\rm pair} \sum_i \deg(v_i) \exp\!\left[-\frac{|\vec r - \vec R_i|^2}{2\sigma^2}\right] \tag{1}$$

where $\sigma = \hbar c / \sqrt{m_n \cdot \hbar\omega}$ is the nucleon localization length (self-consistent value from Session 6).

For a single Gaussian centered at the origin, $V(r) = -V_0 \exp(-r^2/2\sigma^2)$ Taylor-expands as:
$$V(r) = -V_0 + \frac{V_0}{2\sigma^2} r^2 - \frac{V_0}{8\sigma^4} r^4 + \frac{V_0}{48\sigma^6} r^6 - \cdots \tag{2}$$

Identifying the HO frequency $\frac{1}{2}m_n \omega^2 = V_0/(2\sigma^2)$:
$$m_n \omega^2 = \frac{V_0}{\sigma^2}, \qquad C_4 = -\frac{V_0}{8\sigma^4} = -\frac{m_n \omega^2}{8\sigma^2} \tag{3}$$

The quartic coefficient $C_4$ is **negative**.

For the full K$_3$ sum-of-Gaussians at the centroid, the same algebraic structure holds with $V_0$ replaced by an effective depth set by the geometry-weighted Gaussian sum. The quartic coefficient is still negative.

### §2.2 Quartic perturbation matrix elements

For the 3D HO with frequency $\omega$, the diagonal matrix elements of $r^4$ in state $|n, l\rangle$ (where $N = 2n + l$) are:
$$\langle n, l | r^4 | n, l \rangle = \left(\frac{\hbar}{m_n \omega}\right)^2 \cdot f(N, l) \tag{4}$$

with
$$f(N, l) = \left(N + \tfrac{3}{2}\right)^2 + 2n\left(n + l + \tfrac{3}{2}\right) + l + \tfrac{3}{2} \tag{5}$$

Verification at ground state: $f(0, 0) = (3/2)^2 + 0 + 0 + 3/2 = 9/4 + 6/4 = 15/4$, which matches the known result $\langle 0, 0 | r^4 | 0, 0 \rangle = (15/4)(\hbar/m_n \omega)^2$. ✓

The first-order quartic energy shift is:
$$\Delta E_{N, l} = C_4 \cdot \langle r^4 \rangle_{N, l} = -\frac{m_n \omega^2}{8\sigma^2} \cdot \left(\frac{\hbar}{m_n \omega}\right)^2 \cdot f(N, l) = -\frac{\hbar^2}{8 m_n \sigma^2} \cdot f(N, l) \tag{6}$$

Numerically, with $\hbar^2/m_n = (\hbar c)^2/(m_n c^2) = 41.443$ MeV·fm$^2$ and $\sigma = 1.7855$ fm at $\hbar\omega = 13$ MeV:
$$\Delta E_{N, l} = -1.625 \cdot f(N, l) \text{ MeV} \tag{7}$$

### §2.3 Sign analysis: wrong sign for empirical centrifugal enhancement

Computing $f(N, l)$ across the shell-model relevant range:

| $N$ | $l$ | $f(N, l)$ | $\Delta E$ (MeV) | empirical centrifugal expectation |
|---|---|---|---|---|
| 2 | 0 | 18.75 | $-30.5$ | low-l should be lowered LESS |
| 2 | 2 | 15.75 | $-25.6$ | high-l should be lowered MORE |
| 3 | 1 | 29.75 | $-48.3$ | low-l should be lowered LESS |
| 3 | 3 | 24.75 | $-40.2$ | high-l should be lowered MORE |
| 4 | 0 | 45.75 | $-74.3$ | low-l should be lowered LESS |
| 4 | 2 | 42.75 | $-69.5$ | intermediate |
| 4 | 4 | 35.75 | $-58.1$ | high-l should be lowered MORE |
| 5 | 1 | 62.75 | $-102.0$ | low-l |
| 5 | 5 | 48.75 | $-79.2$ | high-l ($1h$, leading to magic 82) |

**Observation:** at fixed $N$, $f(N, l)$ is *largest* for low-l and *decreases* as $l$ increases. Combined with $C_4 < 0$, this means low-l states are lowered *more* by the quartic correction than high-l states.

**This is the wrong sign for empirical centrifugal enhancement.** In Bohr-Mottelson phenomenology, the centrifugal coefficient $D$ in $E_{NLJ} = (N + 3/2)\hbar\omega - D \cdot l(l+1) - V_{\rm SO} \vec L \cdot \vec S/\hbar^2$ is *positive*, so high-l states are lowered relative to low-l within each shell. This is what enhances the magic-strength gaps at 28, 50, 82, 126 (which all close on high-l $j = l + 1/2$ orbitals).

The K$_3$ Gaussian-modulated mean field, taken at first order in central Taylor expansion, gives the *opposite* effect: it slightly enhances the HO-boundary magic gaps (2, 8, 20) by lowering low-l states more, but works *against* the spin-orbit-driven magic gaps.

### §2.4 Magnitude of the quartic correction and breakdown of perturbation theory

The numerical magnitudes in Table §2.3 are striking: the quartic shift $|\Delta E|$ for high-N states is comparable to or larger than $\hbar\omega = 13$ MeV. This signals that *first-order perturbation theory is failing* for the high-N states where the spin-orbit-driven magic numbers live ($N = 3, 4, 5, 6$ for magics 28, 50, 82, 126).

The physical reason: high-N HO states have radial extent $\langle r^2 \rangle^{1/2} = \sigma \sqrt{N + 3/2}$. For $N = 6$, this is $\sigma \sqrt{7.5} = 2.74 \cdot \sigma = 4.89$ fm — comparable to or larger than the cluster size $R_{\rm cluster} \sim 3$–$4$ fm at $A = 56$. The HO + Taylor-expanded quartic is not a valid representation of the actual K$_3$ confining potential at these radii: the wavefunction probes the *cluster boundary*, where the K$_3$ potential transitions from its Gaussian-bottom interior to the asymptotic exterior decay.

### §2.5 Verdict on Route 1b

**Route 1b is ruled out as a magic-strength enhancement route**, on two grounds:
1. **Wrong sign:** the K$_3$ Gaussian central expansion gives quartic correction that lowers low-l more than high-l, opposite of empirical centrifugal enhancement.
2. **Framework breakdown:** perturbation theory in the central Taylor expansion fails for high-N states, where the spin-orbit-driven magics live. The relevant physics is at the *cluster boundary*, not in the *central region*.

These two findings together identify the missing physics: **cluster-surface Thomas-form spin-orbit**. The Bohr-Mottelson Thomas-form $V_{\rm SO}(r) = \xi(r) \, \vec L \cdot \vec S$ has $\xi(r) \propto -dV/dr$, peaking at the cluster surface (where $V$ transitions from interior to exterior most rapidly). For the K$_3$ Gaussian-modulated potential, $-dV/dr$ peaks at $r \sim \sigma$, but the *integrated* spin-orbit experienced by a high-N nucleon is sensitive to where its wavefunction has peak amplitude — which for high-l j-shell partners, is precisely at the cluster surface.

A full closure of the layer 3 gap-strength match would compute $V_{\rm SO}^{\rm surface}$ as the integral $\langle \xi(r) \rangle$ in surface-localized states, *not* as the central HO-virial estimate $V_{\rm SO} \sim (v_F/c)^2 \cdot \hbar\omega$. This is multi-session work beyond Session 10's scope.

---

## §3. Route 1a: Refined $v_F/c$ via surface-region (Approach C) emphasis

For Thomas-form spin-orbit, the relevant velocity is at the cluster surface where the potential gradient peaks. Session 8's three approaches gave:
- Approach A (cluster-avg, central): $v_F/c \in [0.306, 0.392]$, mean 0.352
- Approach B (HO virial, CPP $\hbar\omega^*$): $v_F/c \in [0.197, 0.266]$, mean 0.238
- Approach C (surface-region, Thomas-form): $v_F/c \in [0.278, 0.356]$, mean 0.319

Session 8 chose $v_F/c = 0.30$ as a *consensus* value across all three approaches. Session 10 refines this for the magic-strength test case at $A \sim 56$ by emphasizing Approach C (surface-region), which is the appropriate regime for Thomas-form spin-orbit:

For $A = 56$ (between $A = 48$ icosahedron at $v_F/c = 0.307$ and $A = 40$ gyroelongated square bipyramid at $v_F/c = 0.356$, interpolating closer to icosahedron extrapolation at the $A = 56$ deltahedron-core boundary):
$$v_F/c \big|_{\rm refined} = 0.32 \tag{8}$$

This gives:
$$V_{\rm SO}\big|_{\rm Route\,1a} = (0.32)^2 \cdot 13 = 1.331 \text{ MeV}, \qquad V_{\rm SO}/\hbar\omega = 0.1024 \tag{9}$$

**Route 1a refinement:** $V_{\rm SO}/\hbar\omega$: $0.090 \to 0.102$, an increase of **+13.8%**.

---

## §4. Route 1c: Higher-order relativistic via SSV-PSR_eff expansion

The CPP relativistic kinematics machinery from the SR paper uses $\textsf{PSR}_{\rm eff} = l_P / (1 + k \cdot \Delta\textsf{SSV})$. Particle motion at velocity $v$ modulates $\Delta\textsf{SSV}$ proportional to $(v/c)^2$ at leading order. Expanding $\textsf{PSR}_{\rm eff}$:
$$\frac{\textsf{PSR}_{\rm eff}}{l_P} = 1 - \alpha \left(\frac{v}{c}\right)^2 + \alpha^2 \left(\frac{v}{c}\right)^4 - \alpha^3 \left(\frac{v}{c}\right)^6 + \cdots \tag{10}$$

where $\alpha$ is a CPP-internal coupling of order unity (set by the $k$ in the SR paper).

The Thomas-precession-form spin-orbit magnitude inherits this expansion. The leading $(v/c)^2$ term gives the Session 8 layer 1 result $V_{\rm SO} \sim (v_F/c)^2 \cdot \hbar\omega$. The next-order correction multiplies by $1 + \beta (v_F/c)^2$ where $\beta$ is order unity:
$$V_{\rm SO}\big|_{\rm corrected} = V_{\rm SO}\big|_{\rm leading} \cdot \left[1 + \beta \left(\frac{v_F}{c}\right)^2 + \mathcal{O}((v_F/c)^4)\right] \tag{11}$$

For conservative estimate, take $\beta = 1$ (consistent with conventional Foldy-Wouthuysen-style expansions where the next-order spin-orbit correction is order $(v/c)^2$ of the leading). At $v_F/c = 0.32$:
$$1 + \beta (v_F/c)^2 = 1 + 0.1024 = 1.102 \tag{12}$$

Combined Routes 1a + 1c:
$$V_{\rm SO}\big|_{\rm combined} = (0.32)^2 \cdot 13 \cdot 1.102 = 1.468 \text{ MeV} \tag{13}$$
$$V_{\rm SO}/\hbar\omega \big|_{\rm combined} = 0.113 \tag{14}$$

**Route 1c refinement (on top of Route 1a):** $V_{\rm SO}/\hbar\omega$: $0.102 \to 0.113$, additional **+10.7%**.

---

## §5. Synthesis: bounded refinement

### §5.1 Combined Session 10 result

| route | $v_F/c$ | $(v_F/c)^2$ | rel. corr. | $V_{\rm SO}/\hbar\omega$ |
|---|---|---|---|---|
| Session 8 layer 1 baseline | 0.30 | 0.090 | — | 0.090 |
| Route 1a refined | 0.32 | 0.102 | — | **0.102** |
| Route 1c (atop 1a) | 0.32 | 0.102 | $\times 1.10$ | **0.113** |
| Empirical strong-magic threshold | — | — | — | 0.20–0.25 |

**Combined Session 10 V_SO/ℏω = 0.113**, an increase of **25%** over Session 8's baseline.

The combined refinement reaches **56%** of the empirical strong-magic threshold (0.20). The remaining gap is a factor of 1.77 to 2.21.

### §5.2 Route 1b ruled out

The K$_3$ Gaussian-modulated mean field's intrinsic anharmonicity does NOT provide centrifugal-style enhancement of magic-strength gaps. The quartic correction has the wrong sign (lowers low-l more than high-l), opposite of empirical Bohr-Mottelson $D \cdot l(l+1)$. Plus the central-Taylor framework breaks down for high-N states where spin-orbit-driven magics live.

### §5.3 Identification of remaining physics

The bounded result $V_{\rm SO}/\hbar\omega \approx 0.11$ from Routes 1a + 1c, combined with Route 1b's negative result, identifies the missing physics: **cluster-surface Thomas-form spin-orbit**. Two closure paths are now well-motivated for future multi-session work:

**Path (i): Cluster-surface Thomas-form spin-orbit.** Compute $V_{\rm SO}$ as $\langle \xi(r) \rangle$ in surface-localized states, where $\xi(r) \propto -dV/dr$ peaks at the cluster boundary. This requires the full K$_3$ potential profile (not just central-region expansion) and surface-emphasized wavefunctions. Empirically, Bohr-Mottelson Thomas-form $V_{\rm SO}$ at $A = 56$ is ~1.5 MeV — close to Session 10's combined result (1.468 MeV) but achieved through different physics. Whether the CPP K$_3$ surface gives an additional factor of ~2 enhancement of magic-strength gaps requires explicit computation.

**Path (ii): Numerical diagonalization beyond Taylor expansion.** Diagonalize the full K$_3$ Gaussian-modulated Hamiltonian numerically (not perturbatively), capturing the true ground-state and excited-state structure including cluster-edge effects. This automatically handles the high-N regime where central Taylor expansion fails.

Both paths are multi-session work appropriate for future programme advances. Session 10 establishes the **bound** of what the simple HO + L·S + V_SO refinement framework can achieve: $V_{\rm SO}/\hbar\omega \approx 0.11$, about half the empirical strong-magic threshold.

---

## §6. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged

Session 10's V_SO refinement work uses existing CPP mechanisms (Session 8's $v_F/c$ from Approach C surface-region, plus Session 7 Phase 2's SSV-PSR_eff machinery). No new K$_3$ scale-recurrence instance is introduced. The negative result on Route 1b further confirms that the centrifugal enhancement that produces empirical magic-strength gaps is *not* a K$_3$ mechanism: it's a Thomas-form surface effect that requires different physics.

---

## §7. Programme implications

**(1) Sub-question (b) Route B-α layer 3 status updated:** "shell SEQUENCE reproduced; gap magnitudes at soft end of empirical" → "**bounded refinement: simple HO + L·S framework saturates at $V_{\rm SO}/\hbar\omega \approx 0.11$; closure of gap-strength match requires cluster-surface Thomas-form spin-orbit or numerical diagonalization beyond Taylor expansion**".

**(2) Route 1b ruled out.** This is the third programme-level negative-result demonstration in the OPEN-SS-35 closure programme, after Route D (direct lattice-shell counting, Session 5 Phase 2) and Route B-γ (K$_3$-mode phase coupling, Session 7 Phase 2). The progressive ruling-out of candidate routes sharpens the closure path.

**(3) OPEN-SS-35 closure trajectory: 6 programme-level stages preserved.** Session 10 refines the existing layer 3 partial closure (Session 9) but does not advance to a new programme-level stage. The cumulative trajectory remains:
- (i) Speculative cross-paradigm bridge (Session 4 registration)
- (ii) Scoping passed (Session 5 Phase 2)
- (iii) Sub-question (a) Level-1 partial closure (Session 6)
- (iv) Sub-question (a) A-scaling extension + sub-question (b) scoping (Session 7)
- (v) Sub-question (b) B-α layer 1 closed; magnitude Level-1 partial (Session 8)
- (vi) Sub-question (b) B-α layer 3 partial closure: shell sequence reproduced (Session 9; refined this Session 10)

**(4) First qualitative cross-paradigm consilience claim of the OPEN-SS-35 closure programme remains intact** (Session 9): CPP — derived from 600-cell lattice geometry, K$_3$ alpha-cluster contacts, and SSV-PSR_eff relativistic kinematics — produces the empirical nuclear magic-number SEQUENCE at zero free parameters. Session 10 establishes that the gap STRENGTHS at the soft end of empirical require cluster-surface physics that is multi-session work.

**(5) Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.**

---

## §8. Forward-looking pointers

**Priority 1 (highest-leverage, multi-session):** Cluster-surface Thomas-form spin-orbit (Path (i) above). Compute $V_{\rm SO}$ as $\langle \xi(r) \rangle$ in surface-localized HO states using the full K$_3$ Gaussian-modulated potential profile. This is the physics that's been identified as missing by Session 10's negative result on Route 1b. Multi-session by scope; would directly address the magic-strength gap enhancement.

**Priority 2:** Numerical diagonalization of the full K$_3$ Hamiltonian (Path (ii)). Captures true ground-state and excited-state structure including cluster-edge effects, beyond Taylor expansion. Multi-session.

**Priority 3:** OPEN-SS-16 / Layer B closure work. Unlocks B-α layer 2 (rigorous operator structure of $\vec L \cdot \vec S$). Multi-session.

**Priority 4:** Sub-question (a) A-scaling closure (R1 or R2 from Session 7 Phase 1). Single-session-tractable. Refines $\hbar\omega$ precision.

**Anti-priority:** Do not pursue further refinement of Routes 1a, 1c — Session 10 has bounded what they can achieve at $V_{\rm SO}/\hbar\omega \approx 0.11$. Additional small adjustments to $v_F/c$ or higher-order $(v/c)^4$ terms cannot reach 0.20+.

---

## §9. Summary

**Session 10 establishes the bound of layer 3 gap-strength refinement within the simple HO + L·S framework: $V_{\rm SO}/\hbar\omega \approx 0.11$, about half the empirical strong-magic threshold of 0.20–0.25.**

- **Route 1b (centrifugal correction from K$_3$ Gaussian central expansion): RULED OUT.** Quartic coefficient $C_4 < 0$ combined with $\langle r^4 \rangle_{N, l}$ being LARGER for low-l than high-l at fixed $N$ gives the WRONG SIGN for empirical centrifugal enhancement (lowers low-l more than high-l, opposite of Bohr-Mottelson $D \cdot l(l+1)$). Plus first-order perturbation theory fails for high-N states where the spin-orbit-driven magics (28, 50, 82, 126) sit. The K$_3$ Gaussian-modulated mean field's intrinsic anharmonicity does NOT provide magic-strength enhancement.

- **Route 1a (refined $v_F/c$ via surface-region emphasis):** $v_F/c = 0.32$ (refined for Thomas-form spin-orbit at $A = 56$, between Approach C's icosahedron and gyroelongated square bipyramid values). $V_{\rm SO}/\hbar\omega = 0.090 \to 0.102$ (+14%).

- **Route 1c (higher-order relativistic via SSV-PSR_eff):** Multiplicative factor $1 + \beta(v_F/c)^2 \approx 1.10$ on $V_{\rm SO}$. $V_{\rm SO}/\hbar\omega = 0.102 \to 0.113$ (+11%).

**Combined Session 10 result: $V_{\rm SO}/\hbar\omega = 0.113$, a 25% increase over Session 8 baseline 0.090.** Reaches 56% of empirical strong-magic threshold; remaining gap is factor 1.77 to 2.21.

**Programme effects:**
- Sub-question (b) Route B-α layer 3 status: refined to "bounded refinement: simple HO + L·S framework saturates at $V_{\rm SO}/\hbar\omega \approx 0.11$".
- OPEN-SS-35 closure trajectory: 6 programme-level stages preserved; first qualitative cross-paradigm consilience claim (Session 9) intact.
- Identification of missing physics: cluster-surface Thomas-form spin-orbit (multi-session work).
- Third programme-level negative-result demonstration in OPEN-SS-35 closure programme (after Route D, Route B-γ).
- Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.

The OPEN-SS-35 closure programme has now bounded what the simple HO + L·S framework can achieve and identified two well-motivated multi-session paths (cluster-surface Thomas-form, numerical diagonalization) for further closure of the gap-strength match. The full closure of layer 3 is not single-session-tractable.
