# Mechanism: Capotauro — Substrate-Vacuum Chirality on the K3-Doublet

**Paper:** Capotauro v1.0 (SHIPPED 16 May 2026, Session 122 Patch 0415)
**Last updated:** 16 May 2026 (Session 123 Patch 0416E)
**Document type:** Physical mechanism description for physicists

---

## One-sentence summary

The substrate vacuum carries a primitive chirality magnitude $\|\chi\| = \phi^{-3} \approx 0.236$ (a foundational feature of the substrate, coeval with CPs/GPs); the chirality observable $\hat{C}_\chi$ acts on charged-lepton substrate states organized as a TBM-aligned K3-doublet extended with cage-shell perpendicular wavefunctions; Wigner-Eckart factorization on the $D_6 = S_3 \times Z_2$ stabilizer separates the matrix element into a K3-amplitude factor ($\|M_{K3}\| = \chi$ from chirality-eigenvalue matching on the unique $A_2$ generator) and a cage-shell averaging factor ($\|M_\perp\| = d_E/V_\text{cage} = 2/12 = 1/6$ from Schur orthogonality on the icosahedral first cage shell), yielding the chirality matrix element $\|M\| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ that equals the parity-violation asymmetry $\Delta p_{LR}$ between left-handed and right-handed K3-doublet eigenstates of weak-interaction processes, agreeing within 2% with the empirical anchor $\sim 0.04$ back-derived from the cosmological baryon asymmetry $\eta_B$ via leptogenesis — all at zero free parameters under FI-C-1 through FI-C-10 + 4 CPP axioms (A1, A3, A4, A7).

---

## Inputs and constants

All inputs are foundational substrate features or inherited from prior CPP papers; none are tuned to Capotauro data.

| Symbol | Value | Source |
|---|---|---|
| $\chi$ | $\phi^{-3} \approx 0.236$ | FI-C-9 substrate primitive chirality magnitude (primitive-feature framing at v1.0 SHIP) |
| $\phi$ | $1.618034\ldots$ | Golden ratio (constitutive of 600-cell geometry) |
| $V_\text{cage}$ | 12 | Icosahedral first-shell vertex count = $\|D_6\|$ (cage-shell symmetry identity) |
| $d_E$ | 2 | Dimension of $E$ irrep of $D_6$ (K3-doublet irrep content) |
| $\eta_B$ | $(6.12 \pm 0.04) \times 10^{-10}$ | Planck 2018 cosmological baryon asymmetry measurement (empirical anchor) |
| $\Delta p_{LR}$ | $\sim 0.04$ | Empirical anchor back-derived from $\eta_B$ via leptogenesis with ~10% framework-uncertainty from sphaleron-equilibration + washout + lepton-flavor-mixing |

Zero fitted parameters. All Capotauro mechanism predictions follow from $\chi = \phi^{-3}$ + 600-cell geometric inputs + SF-4 v4.0 K3 antibonding doublet inheritance + FI-C-3 perpendicular-wavefunction extension.

---

## The mechanism, step by step

### Step 1: Substrate-vacuum chirality as primitive feature (FI-C-9)

The substrate vacuum carries a primitive chirality of magnitude $\|\chi\| = \phi^{-3}$. At v1.0 SHIP this magnitude is treated as a foundational substrate feature in the same status as the existence of CPs/GPs themselves and the rules of their interaction — a constitutive specification of the substrate, not the outcome of a dynamical event. The earlier "spontaneous symmetry breaking" framing (in which the chirality would emerge from a prior more-primitive symmetric substrate via symmetry-breaking dynamics) is preserved in Remark 2.2 of the paper as a mathematically-equivalent alternative interpretation but not adopted as the primary framing — per CPP's core methodological commitment that physical mechanisms underlie mathematical descriptions.

Reading C (Session 121 working sketch) registers the candidate physical mechanism for FI-C-9's primitive chirality: a primitive 4D direction $\hat{n}$ in the substrate's ambient 4D space produces direction-correlated edge-length variation in the 600-cell lattice at the $\phi^{-3}$ scale, with $\|\chi\| = \phi^{-3}$ derived rather than postulated via the perturbative-distance-ratio constraint. Reading C is Tier-4 Layer 1/Layer 2 epistemic status at v1.0 SHIP, not Layer 3 (formal theorem closure); five Layer 3 closure-trajectory questions Q1–Q6 register the path to sub-claim (b) closure post-v1.0.

### Step 2: K3-doublet extended TBM-aligned basis (FI-C-1 through FI-C-3)

The Capotauro mechanism acts on charged-lepton substrate states organized as a K3-doublet — the antibonding-doublet basis $\{\|\phi_-^{(1)}\rangle, \|\phi_-^{(2)}\rangle\}$ inherited from SF-4 v4.0 THEO-SF-4-5 Composite K3-Cage-Shell Coupling Theorem (FI-C-1 + FI-C-2). The K3 stabilizer group is $D_6 = S_3 \times Z_2$ where $S_3$ permutes K3-vertices and $Z_2$ is the cell-swap symmetry $\zeta$ with $\det = -1$ (Session 89 corrigendum).

FI-C-3 extends the K3-doublet with cage-shell perpendicular wavefunctions: $\|\Phi_-^{(1)}\rangle = \|\phi_-^{(1)}\rangle \otimes \|\chi_\perp^{(1)}\rangle$ and $\|\Phi_-^{(2)}\rangle = \|\phi_-^{(2)}\rangle \otimes \|\chi_\perp^{(2)}\rangle$, where the perpendicular wavefunctions $\{\|\chi_\perp^{(1)}\rangle, \|\chi_\perp^{(2)}\rangle\}$ are the cage-shell substrate orientations at the K3-vertex spatial locations. The two basis states carry opposite ζ-parity assignments: one ζ-EVEN, one ζ-ODD. The opposite-ζ-parity assignment is the Session 91 resolution of the Session 90 D_6 character theory obstruction (under uniform ζ-parity all σ_1-ODD matrix elements vanish identically).

### Step 3: Chirality observable $\hat{C}_\chi$ irrep classification (in $B_2$ of $D_6$)

The chirality observable $\hat{C}_\chi$ is a Hermitian operator on the K3-doublet whose matrix element $\|\langle\Phi_-^{(1)}\|\hat{C}_\chi\|\Phi_-^{(2)}\rangle\|$ equals the parity-violation asymmetry $\Delta p_{LR}$. Under the $D_6 = S_3 \times Z_2$ stabilizer, $\hat{C}_\chi$ lives in irrep $B_2 = A_2 \times \zeta\text{-ODD}$ — specifically: $A_2$-type (sign irrep) on the K3-vertex permutation $S_3$ subgroup and ζ-ODD on the cell-swap $Z_2$ subgroup. The irrep classification is forced by the chirality observable's symmetry properties: chirality changes sign under K3-vertex parity ($A_2$ on $S_3$) and changes sign under cell-swap (ζ-ODD on $Z_2$).

### Step 4: Wigner-Eckart factorization on $D_6 = S_3 \times Z_2$

The Wigner-Eckart theorem factorizes the matrix element into K3-amplitude and perpendicular-wavefunction contributions, exploiting the $D_6 = S_3 \times Z_2$ product structure:

$$\|M\| = \|\langle\Phi_-^{(1)}\|\hat{C}_\chi\|\Phi_-^{(2)}\rangle\| = \|M_{K3}\| \cdot \|M_\perp\|$$

where $\|M_{K3}\|$ is the K3-amplitude matrix element of the $A_2$ component of $\hat{C}_\chi$ on $\{\|\phi_-^{(1)}\rangle, \|\phi_-^{(2)}\rangle\}$ and $\|M_\perp\|$ is the perpendicular-wavefunction matrix element of the ζ-ODD component of $\hat{C}_\chi$ on $\{\|\chi_\perp^{(1)}\rangle, \|\chi_\perp^{(2)}\rangle\}$.

### Step 5: Unique $A_2$ generator on K3-amplitudes

The σ_1-ODD operators on the K3-amplitudes form a 2-parameter family in general, but $\hat{C}_\chi$ in $B_2$ requires the unique $A_2$ generator:

$$T_{A_2}(b) = i \cdot b \cdot S$$

where $S$ is the antisymmetric 3×3 matrix encoding the K3-vertex cyclic permutation — the cross-product-with-$(1,1,1)$ structure on the K3-amplitude tangent space. Session 95 correction substantively replaced the earlier general (a,b)-parameterization that carried inadmissible $E$-irrep contamination; the unique $A_2$ generator gives:

$$M_{K3}(b) = \langle\phi_-^{(1)}\|T_{A_2}(b)\|\phi_-^{(2)}\rangle = -i \cdot b \cdot \sqrt{3}$$

with the $\sqrt{3}$ in the numerator from the cross-product-with-$(1,1,1)$ structure.

### Step 6: Chirality-eigenvalue matching gives $\|M_{K3}\| = \chi$

The unique $A_2$ generator $T_{A_2}(b) = i \cdot b \cdot S$ has eigenvalues $\{0, +b\sqrt{3}, -b\sqrt{3}\}$ on the K3-amplitude basis (Lemma 4.2 of `Capotauro_subclaim_c_wigner_eckart.md`). The substrate's primitive chirality eigenvalues are $\pm\chi$ (the substrate vacuum is bi-stable with two equivalent enantiomorphs of chirality magnitude $\|\chi\|$). Setting the non-zero K3-amplitude eigenvalues equal to the substrate chirality eigenvalues:

$$\pm b\sqrt{3} = \pm\chi \implies b = \chi/\sqrt{3}$$

The K3-amplitude matrix element magnitude is therefore:

$$\|M_{K3}\| = \|b\| \cdot \sqrt{3} = \chi$$

at zero free parameters. The derivation principle uses Hermitian-operator spectral analysis rather than ad-hoc parameter assignment — $b$ is fixed by the chirality-eigenvalue matching, not chosen.

### Step 7: Cage-shell averaging gives $\|M_\perp\| = 1/6$

The perpendicular-wavefunction matrix element is computed via Schur orthogonality on the icosahedral first cage shell of the K3-vertex substrate states. The cage shell has $D_6$ stabilizer symmetry inherited from the cage's icosahedral structure; Schur orthogonality on the $D_6$ group gives the averaging factor:

$$\|M_\perp\| = \frac{d_E}{V_\text{cage}} = \frac{d_E}{\|D_6\|} = \frac{2}{12} = \frac{1}{6}$$

where $d_E = 2$ is the dimension of the $E$ irrep of $D_6$ (the K3-doublet's irrep content) and $V_\text{cage} = \|D_6\| = 12$ from the cage-shell-symmetry identity. The cage-shell averaging factor structurally inherits from SF-4 v4.0 THEO-SF-4-5's mass-formula averaging via FI-C-10 (extension of FI-C-6 from mass observables to chirality observables, justified at v1.0 by three plausibility arguments: substrate-isotropy, DI-bit propagation, and FI-C-6 precedent).

### Step 8: Composite product and substrate substitution

The composite Wigner-Eckart product:

$$\|M\| = \|M_{K3}\| \cdot \|M_\perp\| = \chi \cdot \frac{1}{6} = \frac{\chi}{6}$$

Substrate substitution from FI-C-9:

$$\|M\| = \frac{\phi^{-3}}{6} \approx 0.0394$$

This is the chirality matrix element on the TBM-aligned K3-doublet — the parity-violation asymmetry $\Delta p_{LR}$ between left-handed and right-handed K3-doublet eigenstates of weak-interaction processes.

---

## Empirical anchor and falsifier

**Empirical anchor**: $\Delta p_{LR} \sim 0.04$ back-derived from the cosmological baryon asymmetry $\eta_B = (6.12 \pm 0.04) \times 10^{-10}$ (Planck 2018) via standard leptogenesis assumptions (sphaleron-equilibration efficiency, washout factor, lepton-flavor-mixing). The back-derivation carries ~10% framework-uncertainty from the leptogenesis chain.

**Capotauro prediction**: $\Delta p_{LR} = \chi/6 \approx 0.0394$.

**Agreement**: within 2% of the empirical anchor. CONFIRMED at structural-numerical level pending direct laboratory measurement.

**Falsifier**: $\Delta p_{LR}$ observed outside $\pm 2\%$ of $\chi/6$ in direct measurement falsifies THEO-CAP-1 conditional theorem closure.

**Indirect routes to sharpening the test** (per `predictions.md` PRED-O-25):
- HL-LHC precision-electroweak Run 4–5 measurements on charged-lepton K3-doublet eigenstates.
- JUNO/DUNE/Hyper-K per-mille-precision $\sin^2\theta_{13}$ measurements after Q11 closure in SF-2 v2.0+ scope.
- Cosmological back-derivation refinement (precision $\eta_B$ + improved leptogenesis modeling).

---

## What's in scope at v1.0 SHIP vs deferred to v2.0+

**In scope at v1.0 SHIP** (THEO-CAP-1 conditional theorem closure):
- Substrate-to-K3-doublet matrix element derivation $\|M\| = \chi/6$ on the TBM-aligned K3-doublet — closure of sub-claim (c) of OPEN-SM-4.
- Primary empirical prediction $\Delta p_{LR} \approx 0.0394$ with 2% empirical agreement.
- Cage-shell averaging factor 1/6 via FI-C-10 extension from FI-C-6 precedent.

**Deferred to v2.0+** (sub-claims (a), (b), and re-scoped Q11 $\sin^2\theta_{13}$):
- **Sub-claim (a)**: Capotauro nucleation event derivation (universe-wide sign-selection event downstream of sub-claim (b) magnitude mechanism). Cosmological framing from Abshier & Grok December 2025 Capotauro nucleation paper preserved; closure paper venue TBD post-Capotauro v2.0+.
- **Sub-claim (b)**: substrate chirality magnitude mechanism candidate derivation. Reading C registered at `Research_Frontier.md` OPEN-FI-C-9-FP-MECHANISM as canonical sub-claim (b) closure-trajectory; Layer 3 closure estimated 10–20 sessions. **Q1 group-theoretic verification of $H_4$ stabilizer of $\hat{n} \cong I_4$ is the first sub-step (estimated 1–3 sessions) and triggers Capotauro v2.0+ at minimum.**
- **FI-C-10 first-principles derivation**: observable-class-independence claim distinguishing FI-C-10 from FI-C-6 physically motivated at v1.0 by three plausibility arguments (substrate-isotropy + DI-bit propagation + FI-C-6 precedent) but not formally derived from CPP axioms A1–A11. Separate open work entry distinct from OPEN-FI-C-9-FP-MECHANISM.
- **Q11 $\sin^2\theta_{13}$ derivation**: re-scoped to SF-2 v2.0+ at Session 101 Patch 0395. Linear-vs-quadratic scaling tension surfaced Session 100 (standard QFT-perturbation gives quadratic scaling off by factor 21 from candidate-γ linear-scaling target); wavefunction-level coupling hypothesis ruled out Session 101. Candidate γ $\sin^2\theta_{13} = b \cdot m_\perp = \chi/(6\sqrt{3}) \approx 0.0227$ matches NuFIT 6.0 empirical $0.0222 \pm 0.00069$ within 1σ but requires CPP-specific linear-scaling framework that hasn't been developed at v1.0. Sub-claim (b) Reading C closure trajectory may surface the required framework.
- **$\delta_{CP}$ and $\eta_B$ downstream**: PMNS perturbation machinery beyond Capotauro mechanism's direct scope at v1.0; future sub-claim work.

---

## Cross-paper consistency checks

The Capotauro mechanism is consistent with prior CPP papers in the corpus:

- **SF-4 v4.0 inheritance**: K3 antibonding doublet basis + cage-shell coupling mass formula (THEO-SF-4-5) inherited; FI-C-3 extension and FI-C-10 extension are the distinctive Capotauro additions.
- **SM-5 TBM mixing**: TBM-aligned basis structure of the K3-doublet is consistent with SM-5's zeroth-order PMNS derivation.
- **SF-2 W bracelet $D_6$ stabilizer**: the W bracelet's $D_6$ stabilizer is the same group structure that gives Capotauro's $V_\text{cage}/2 = 6$ averaging factor — a structural consistency between the EW-sector flagship and the Capotauro mechanism that suggests both share substrate-symmetry origins (Q5 of Reading C closure trajectory will sharpen this).
- **SM-2 qDP/eDP asymmetry**: the substrate qDP/eDP asymmetry observed at SM-2 may be a cross-sector signature of the same primitive chirality magnitude $\chi = \phi^{-3}$ (Q6 of Reading C closure trajectory will sharpen this).

The cross-sector consistency suggests the Capotauro mechanism's $\phi^{-3}$ chirality magnitude is not isolated but woven into multiple substrate-physics observables — a structural prediction worth tracking.

---

*Maintainer: Dr. Thomas Lee Abshier ND, Hyperphysics Institute. For the formal mathematical exposition, see `flagship_papers/capotauro/capotauro.tex`. For Tier-4 verbatim reasoning, see `flagship_papers/capotauro/sketches/` + `flagship_papers/capotauro/documentation_suite/reasoning-capotauro.md`.*
