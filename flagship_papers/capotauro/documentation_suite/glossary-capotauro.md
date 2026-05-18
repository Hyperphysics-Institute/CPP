# Glossary: Capotauro — Substrate-Vacuum Chirality on the K3-Doublet

**Paper:** Capotauro v1.0 (SHIPPED 16 May 2026, Session 122 Patch 0415)
**Last updated:** 16 May 2026 (Session 123 Patch 0416F)
**Scope:** Paper-specific terminology with section references to `capotauro.tex`. For programme-wide terminology see `master_glossary.md` (Capotauro section appended at Patch 0416A).

---

## Constants and substrate parameters

### $\chi$ — substrate primitive chirality magnitude
The substrate's primitive chirality magnitude, $\|\chi\| = \phi^{-3} \approx 0.236$. At v1.0 SHIP treated as a foundational substrate feature (primitive-feature framing per CPP-core-principle methodological commitment that mathematical descriptions are not physical mechanisms). Registered as FI-C-9. Substrate vacuum is bi-stable with two equivalent enantiomorphs of chirality $\pm\chi$; the universe-wide sign-selection event determining which enantiomorph is realized is sub-claim (a) of OPEN-SM-4 (open). See paper §2.1.

### $\phi$ — golden ratio
$\phi = (1+\sqrt{5})/2 = 1.618034\ldots$ Constitutive of 600-cell geometry; $\phi^{-3}$ is the substrate primitive chirality magnitude per FI-C-9. See paper §1.3.

### $V_\text{cage}$ — icosahedral first-shell vertex count
$V_\text{cage} = 12$ = number of vertices in the first distance shell of the icosahedral cage substrate. Equals $\|D_6\|$ via the cage's $D_6$ stabilizer symmetry — the structural identity that makes the cage-shell averaging factor 1/6 clean. See paper §5.5.

### $d_E$ — dimension of E irrep of D_6
$d_E = 2$ — dimension of the $E$ irrep of $D_6$ to which the K3-doublet states belong. Appears in the cage-shell averaging factor $\|M_\perp\| = d_E/V_\text{cage} = 2/12 = 1/6$. See paper §5.5.

### $\eta_B$ — cosmological baryon asymmetry
$\eta_B = (6.12 \pm 0.04) \times 10^{-10}$ from Planck 2018 cosmological measurement. The empirical anchor for $\Delta p_{LR}$ is back-derived from $\eta_B$ via leptogenesis with ~10% framework-uncertainty (sphaleron-equilibration efficiency + washout factor + lepton-flavor-mixing). See paper §2.4 + §6.1.1.

### $\Delta p_{LR}$ — parity-violation asymmetry
$\Delta p_{LR} \sim 0.04$ empirical anchor (leptogenesis back-derivation), $\chi/6 \approx 0.0394$ Capotauro prediction. The 2% agreement is the primary empirical validation of THEO-CAP-1 at v1.0 SHIP. Registered as PRED-O-25 in `predictions.md`. See paper §6.

---

## Foundational Inputs (FI-C-1 through FI-C-10)

Foundational inputs are CPP substrate features postulated as starting points; FI-C-1 through FI-C-10 are the 10 foundational inputs of the Capotauro paper v1.0. The conditional theorem closure of THEO-CAP-1 is established under FI-C-1 through FI-C-10 + 4 CPP axioms (A1, A3, A4, A7).

### FI-C-1 — TBM-aligned K3-amplitude basis
The K3-amplitude basis $\{\|\phi_-^{(1)}\rangle, \|\phi_-^{(2)}\rangle\}$ on which the Capotauro mechanism acts. Inherited from SF-4 v4.0 THEO-SF-4-5 Composite K3-Cage-Shell Coupling Theorem antibonding-doublet basis. See paper §3.

### FI-C-2 — Charged-lepton substrate-state assignment
The K3-doublet basis states are identified with charged-lepton substrate states. Cross-sector consistency with SM-5 TBM mixing. See paper §3.

### FI-C-3 — Cage-shell perpendicular wavefunctions with opposite ζ-parity
Extension of the K3-doublet with cage-shell perpendicular wavefunctions $\{\|\chi_\perp^{(1)}\rangle, \|\chi_\perp^{(2)}\rangle\}$, with one ζ-EVEN and one ζ-ODD under the cell-swap $Z_2$ subgroup of the $D_6$ stabilizer. Session 91 resolution of the Session 90 D_6 character theory obstruction. See paper §3.

### FI-C-4 through FI-C-8 — Structural inputs
Five structural inputs covering the substrate-vacuum order parameter ansatz, the chirality observable's symmetry properties, the Wigner-Eckart factorization on $D_6$, and the substrate-orientation field. See paper §2 + §4.

### FI-C-9 — Substrate primitive chirality magnitude
$\|\chi\| = \phi^{-3}$ treated as a foundational substrate feature at v1.0 SHIP. The primitive-feature framing (Session 120 Patch 0413 reframe) replaces the earlier SSB framing per CPP-core-principle methodological commitment. SSB framing preserved in Remark 2.2 as mathematically-equivalent alternative. First-principles derivation tracked at `research_frontier.md` OPEN-FI-C-9-FP-MECHANISM with Reading C as candidate physical mechanism (Session 121 working sketch). See paper §2 + Remark 2.2.

### FI-C-10 — Cage-shell observable-class extension
Extension of FI-C-6 (cage-shell coupling mass-formula mechanism from SF-4 v4.0 THEO-SF-4-5) from mass observables to chirality observables. Justified at v1.0 by three plausibility arguments: substrate-isotropy + DI-bit propagation + FI-C-6 precedent. Observable-class-independence claim physically motivated but not formally derived from CPP axioms A1–A11; first-principles closure registered as separate open work entry distinct from OPEN-FI-C-9-FP-MECHANISM. See paper §5.4.

---

## Group-theoretic terms

### $D_6 = S_3 \times Z_2$ — K3 stabilizer group
The stabilizer group of the K3-doublet under the cage substrate's symmetry action. Order 12 = $\|S_3\| \cdot \|Z_2\| = 6 \cdot 2$. $S_3$ permutes K3-vertices; $Z_2$ is the cell-swap $\zeta$ with $\det = -1$ (Session 89 corrigendum replacing earlier informal $\det = +1$). See paper §4.1.

### $A_2$ irrep (of $S_3$)
The sign irrep of $S_3$ — the 1-dimensional irrep on which transpositions act as multiplication by $-1$. The $A_2$ component of $\hat{C}_\chi$ on K3-amplitudes is the chirality observable's K3-vertex permutation transformation type. See paper §4.2.

### $B_2$ irrep (of $D_6$)
$B_2 = A_2 \times \zeta\text{-ODD}$ — the irrep of $D_6 = S_3 \times Z_2$ in which $\hat{C}_\chi$ lives. Combines the $A_2$ sign irrep on $S_3$ with the ζ-ODD antisymmetric irrep on $Z_2$. The irrep classification is forced by the chirality observable's symmetry properties: chirality changes sign under K3-vertex parity and under cell-swap. See paper §4.2.

### $E$ irrep (of $D_6$)
The 2-dimensional irrep of $D_6$ to which the K3-doublet states belong. Has dimension $d_E = 2$ — appears in the cage-shell averaging factor $\|M_\perp\| = d_E/V_\text{cage} = 2/12 = 1/6$. See paper §5.5.

### ζ — cell-swap
The cell-swap $Z_2$ subgroup generator of $D_6$. Acts on K3-doublet basis states by swapping the two cell substrate orientations. Has $\det = -1$ (Session 89 corrigendum) — this fact forces ζ-ODD operators (not ζ-EVEN) as chirality observable carriers. See paper §4.1.

### ζ-EVEN, ζ-ODD
Eigenvalue assignment of K3-doublet basis states under the cell-swap $\zeta$. Per FI-C-3 extension, the two basis states carry opposite ζ-parity (one ζ-EVEN, one ζ-ODD), resolving the Session 90 obstruction that uniform ζ-parity forces all σ_1-ODD matrix elements to zero. See paper §3 + §4.

### Chirality-preserving subgroup $S_3' = \langle r, \sigma_1 \zeta \rangle$
The subgroup of $D_6$ that preserves the chirality observable's sign. Replaces the earlier $C_6$ informal framing at Session 89 corrigendum. See paper §4.1.

---

## Operators

### $\hat{C}_\chi$ — chirality observable
The Hermitian observable operator on the K3-doublet whose matrix element $\|\langle\Phi_-^{(1)}\|\hat{C}_\chi\|\Phi_-^{(2)}\rangle\|$ equals the parity-violation asymmetry $\Delta p_{LR}$. Lives in irrep $B_2 = A_2 \times \zeta\text{-ODD}$ of $D_6$. See paper §4.2.

### $T_{A_2}(b) = i \cdot b \cdot S$ — unique $A_2$ generator
The unique σ_1-ODD operator on K3-amplitudes consistent with $A_2$ irrep purity. $S$ = antisymmetric 3×3 matrix encoding K3-vertex cyclic permutation (cross-product-with-$(1,1,1)$ structure). The Session 95 correction substantively replaced the earlier general (a,b)-parameterization which carried inadmissible $E$-irrep contamination. Eigenvalues on K3-amplitude basis: $\{0, +b\sqrt{3}, -b\sqrt{3}\}$. See paper §4.3 + §5.3.

### $S$ — antisymmetric K3-vertex matrix
The antisymmetric 3×3 matrix encoding K3-vertex cyclic permutation. Structure: cross-product-with-$(1,1,1)$ on the K3-amplitude tangent space. Eigenvalues $\{0, +\sqrt{3}, -\sqrt{3}\}$ (cross-product nullspace + paired imaginary eigenvalues of cross product). See paper §4.3 + Lemma 4.2 of `Capotauro_subclaim_c_wigner_eckart.md`.

---

## States and bases

### K3-doublet
The 2-state basis $\{\|\phi_-^{(1)}\rangle, \|\phi_-^{(2)}\rangle\}$ of K3-amplitudes inherited from SF-4 v4.0 THEO-SF-4-5 antibonding doublet. The basis on which the Capotauro mechanism acts at the K3-amplitude level. See paper §3.1.

### K3-doublet extended TBM-aligned basis
The full Capotauro mechanism basis: $\|\Phi_-^{(1)}\rangle = \|\phi_-^{(1)}\rangle \otimes \|\chi_\perp^{(1)}\rangle$ and $\|\Phi_-^{(2)}\rangle = \|\phi_-^{(2)}\rangle \otimes \|\chi_\perp^{(2)}\rangle$. Tensor-product structure separates K3-amplitude and perpendicular-wavefunction degrees of freedom; opposite ζ-parity assignment per FI-C-3. See paper §3.2.

### Perpendicular wavefunctions
$\{\|\chi_\perp^{(1)}\rangle, \|\chi_\perp^{(2)}\rangle\}$ — cage-shell substrate orientations at the K3-vertex spatial locations. Tensor factors in the FI-C-3 extension of the K3-doublet. See paper §3.2.

---

## Theorems and lemmas

### THEO-CAP-1 — Composite Capotauro Wigner-Eckart Theorem
The flagship theorem of the Capotauro paper v1.0. Statement: $\|M\| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ on the TBM-aligned K3-doublet. Theorem #62 in `theorem-registry.md` SF-Line section. Conditional theorem closure under FI-C-1 through FI-C-10 + 4 CPP axioms (A1, A3, A4, A7). Registered Session 103 Patch 0397 ahead of paper publication (first such pattern in CPP corpus); paper-level confirmation at v1.0 SHIP Session 122 Patch 0415. See paper §5 + Theorem 5.1.

### Theorem 8.1 (anti-diagonal parity structure)
Sub-sub-claim (c.1a) closure result. The K3-doublet matrix of $\hat{C}_\chi$ is rigorously anti-diagonal in the TBM-aligned basis under FI-C-3 + substrate-vacuum chirality input: $M_{11} = M_{22} = 0$ with $M_{12} \neq 0$. Five-step proof at Session 88. See `Capotauro_subclaim_c_wigner_eckart.md` §3.

### Lemma 4.2 (unique $A_2$ generator spectral analysis)
Sub-lemma establishing $T_{A_2}(b) = i \cdot b \cdot S$ as the unique $A_2$ generator and computing its eigenvalues $\{0, +b\sqrt{3}, -b\sqrt{3}\}$ on the K3-amplitude basis. Load-bearing for chirality-eigenvalue matching at Session 96. See `Capotauro_subclaim_c_wigner_eckart.md` §3.4.

### Chirality-eigenvalue matching principle
Derivation principle: setting the non-zero K3-amplitude eigenvalues of $T_{A_2}(b)$ equal to the substrate chirality eigenvalues $\pm\chi$ gives $b = \chi/\sqrt{3}$ and $\|M_{K3}\| = \chi$ at zero free parameters. Uses Hermitian-operator spectral analysis. See paper §5.3.

### Cage-shell averaging principle
Derivation principle: Schur orthogonality on the icosahedral first cage shell of the K3-vertex substrate states gives $\|M_\perp\| = d_E/V_\text{cage} = 2/12 = 1/6$. Structural identity $V_\text{cage} = \|D_6\| = 12$ from cage's $D_6$ stabilizer symmetry. See paper §5.5.

---

## Sub-claim taxonomy of OPEN-SM-4

### Sub-claim (a) — Capotauro nucleation event
The universe-wide sign-selection event determining which enantiomorph of the substrate vacuum is realized in our universe. Distinct from sub-claim (b) magnitude mechanism; the magnitude can be derived independently of the sign-selection. Cosmological framing from Abshier & Grok December 2025 Capotauro nucleation paper preserved. **OPEN.** See paper §9.1.

### Sub-claim (b) — substrate chirality mechanism candidate derivation
First-principles derivation of $\|\chi\| = \phi^{-3}$ from more primitive CPP axioms rather than postulating it as foundational input FI-C-9. Tracked at `research_frontier.md` OPEN-FI-C-9-FP-MECHANISM. Reading C registered Session 121 Patch 0414 as candidate physical mechanism (primitive 4D direction $\hat{n}$ producing direction-correlated edge-length variation in 600-cell). Layer 3 closure trajectory estimated 10–20 sessions; Q1 group-theoretic verification of $H_4$ stabilizer of $\hat{n} \cong I_4$ is the first sub-step (1–3 sessions) triggering Capotauro v2.0+. **OPEN.** See paper §9.2.

### Sub-claim (c) — substrate-to-K3-doublet matrix element
$\|M\| = \chi/6$ on the TBM-aligned K3-doublet at theorem level. **CLOSED at v1.0 SHIP via THEO-CAP-1.** See paper §5 + Theorem 5.1.

---

## Reading C — sub-claim (b) candidate mechanism

### Primitive 4D direction $\hat{n}$
The Reading C candidate physical mechanism for FI-C-9. A primitive 4D direction $\hat{n}$ in the substrate's ambient 4D space; a foundational substrate feature, not the outcome of a dynamical event. Produces direction-correlated edge-length variation in the 600-cell lattice at the $\phi^{-3}$ scale. See sketch `Capotauro_chiral_mechanism_candidate.md` §2.

### $H_4 \to I_4$ stabilizer structure
The breaking of the 600-cell's full $H_4$ symmetry to the $I_4$ stabilizer of $\hat{n}$. Under Reading C, this is the structural consequence of $\hat{n}$ being primitive (not the outcome of dynamical symmetry breaking). Q1 group-theoretic verification of $H_4 \to I_4$ is the first sub-step of sub-claim (b) Layer 3 closure trajectory.

### Fractional chirality retention
Reading C's new structural prediction: chirality magnitude $\|\chi\| = \phi^{-3}$ retains differently across observable classes. Mass observables retain $O(\chi^2) \approx 0.6\%$ (consistent with SF-4 mass-formula scaling); chirality observables retain full $\chi/6 \approx 4\%$; intermediate observables retain calculable fractions. See sketch `Capotauro_chiral_mechanism_candidate.md` §4.

---

## Open work and re-scoped problems

### OPEN-FI-C-9-FP-MECHANISM
`research_frontier.md` entry registering Reading C as the sub-claim (b) closure-trajectory at Layer 3 level. NEW at Session 122 Patch 0415; Layer 1 / Layer 2 epistemic status at v1.0 SHIP.

### Q11 — $\sin^2\theta_{13}$ derivation
Re-scoped to SF-2 v2.0+ at Session 101 Patch 0395. Linear-vs-quadratic scaling tension: standard QFT-perturbation gives quadratic scaling off by factor 21 from candidate-γ linear-scaling target. Candidate γ $\sin^2\theta_{13} = b \cdot m_\perp = \chi/(6\sqrt{3}) \approx 0.0227$ matches NuFIT 6.0 empirical $0.0222 \pm 0.00069$ within 1σ but requires CPP-specific linear-scaling framework. See paper §7.

### Candidate γ
The structural observation $\sin^2\theta_{13} = b \cdot m_\perp = \chi/(6\sqrt{3}) \approx 0.0227$ matching empirical within 1σ but lacking rigorous derivation in standard QFT framework. Re-scoped to SF-2 v2.0+ for CPP-specific perturbation framework development. See paper §7.

### $\delta_{CP}$ and $\eta_B$ downstream
PMNS perturbation machinery beyond Capotauro mechanism's direct scope at v1.0. Future Capotauro sub-claim work. See paper §9.

---

## Framing terminology

### Primitive-feature framing
The methodological framing adopted at Session 120 Patch 0413 reframe: the substrate's primitive chirality is a foundational feature coeval with CPs/GPs and the rules of their interaction. Honors CPP's core methodological commitment that physical mechanisms underlie mathematical descriptions. See paper §2.1.

### SSB framing (Remark 2.2 alternative)
The "spontaneous symmetry breaking" framing in which the chirality emerges from a prior more-primitive symmetric substrate via symmetry-breaking dynamics. Mathematically equivalent to the primitive-feature framing (same predictions, same falsifier set) but imports continuum-EFT methodological commitments that conflict with CPP's discrete-substrate ontology under a real-dynamical-event reading. Preserved in Remark 2.2 of paper §2 as mathematically-equivalent alternative for readers familiar with continuum-EFT traditions. See paper Remark 2.2.

### Picture A / Picture B / Picture C decomposition
The load-bearing role assignment for the closure trajectory adopted at Session 86 Patch 0381. Picture A = foundational substrate-vacuum; Picture B = transmission mechanism (substrate-to-observable); Picture C = group-theoretic skeleton. The role-assignment guided the closure trajectory across Sessions 86–103. See `Capotauro_chi_phi_closure.md` §8.

---

*Maintainer: Dr. Thomas Lee Abshier ND, Hyperphysics Institute. For programme-wide terminology see `master_glossary.md` (Capotauro section appended Patch 0416A).*
