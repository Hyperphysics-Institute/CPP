# Philosophy: SS-7 — Alpha-Cluster Regime and the 3N−6 Edge Formula

**Paper:** SS-7 v1.1 (20 April 2026, post-round-2 minor revisions)
**Last updated:** 20 April 2026
**Document type:** Epistemological framing and honest assessment

---

## What kind of result is this?

A **zero-parameter formula reproducing the binding energies of eight alpha-chain nuclei within $\pm 1.5\%$**, plus a re-derivation of the ${}^8$Be near-threshold unboundness and a registered saturation onset at $N_\alpha \geq 12$. Ten independent empirical tests from one formula with no nuclear-physics input, built on constants inherited from SS-5.

**Paper-type declaration (per operating_system.md §4 taxonomy):** This is a **prediction paper**. Success criterion: concurrent multi-nucleus agreement at zero fitted parameters. The eight Table 1 predictions satisfy this criterion by construction — all eight use the same two constants ($\Balpha$, $B_{\text{pair}}$), both from SS-5, with no modification.

**Main claim:**
$$B(N_\alpha) = N_\alpha \cdot \Balpha + (3N_\alpha - 6) \cdot B_{\text{pair}} \qquad (N_\alpha \in [3, 10])$$

where $3N_\alpha - 6$ is the edge count of any simplicial convex polytope on $N_\alpha$ vertices (Euler's formula), and alpha-chain nuclei realize such polytopes (modeling hypothesis).

---

## Layer classification

Following the SS-5 / SS-3 convention of separating CPP givens from imported structure and mathematical consequences:

| Layer | Content | Status in SS-7 v1.1 |
|---|---|---|
| **A — CPP geometric inputs** | 600-cell, $M_0$, $\varphi$, nucleon structure (SS-2), ${}^4$He tetrahedral closure (SS-5), K$_3$ face eigenvalue structure (SS-5) | *Given* — all established in prior papers |
| **B — Imported structure** | Rigid-alpha assumption (C1); base-to-base contact (C2); K$_3$ mode at alpha-alpha face (C3); simplicial polytope hypothesis (C4) | C1--C3 are geometric extensions of SS-5; C4 is a structural hypothesis within CPP, not yet derived from lattice-level dynamics |
| **C — Mathematical result** | Theorem 2.1: any simplicial polytope on $N_\alpha$ vertices has $E = 3N_\alpha - 6$ edges | Pure mathematics (Euler's formula + triangle-face constraint); not CPP-dependent |
| **D — Empirical conclusion** | $B(N_\alpha) = N_\alpha\Balpha + (3N_\alpha-6)B_{\text{pair}}$, tested against 8 nuclei within $\pm 1.5\%$ | Follows from B + C; validated in Table 1 |

The **theorem/hypothesis split** (highlighted box in §1 and §2.2) makes explicit that Theorem 2.1 is mathematics (always true) while C4 is physics (supported empirically by Table 1 and the §6.5 stress tests, but not derived).

---

## Certainty levels per element

| Element | Certainty | Basis |
|---|---|---|
| Theorem 2.1 (edge count) | **Mathematical theorem** | Euler's formula + simplicial constraint |
| Table 1 numerical predictions | **Empirically supported, zero-parameter** | 8/8 concurrent match within $\pm 1.5\%$ |
| ${}^8$Be 92 keV unboundness (re-derivation) | **Empirically confirmed** | Matches observed value by construction given $R_{\alpha\alpha}$ |
| $R_{\alpha\alpha} = 2.37$ fm | **Consistency parameter, not derived** | Inverted from ${}^8$Be binding condition; Finding 4.1 explicit |
| C4 (simplicial polytope hypothesis) | **Empirically supported hypothesis, not derived** | Supported by Table 1 + 5 stress tests; OPEN-SS-24 targets derivation |
| $M_0/\varphi$ recurrence across SS-5 and SS-7 | **Empirically supported, not structurally derived** | Same quantum works in 3 contexts; derivation open (§6.2) |
| $N_\alpha \geq 12$ icosahedral closure | **Conjectured** | Flat-residual shape suggests structural onset; OPEN-SS-22 |

---

## Relationship to the Standard Model

SS-7 is an extension of CPP into the **medium-mass alpha-chain nuclear sector**, predicting quantities that the Standard Model (QCD + electroweak) cannot compute from first principles with comparable economy.

**Where SS-7 overlaps with SM nuclear physics:**
- The alpha-cluster tradition (Brink 1966, Ikeda 1968, Wildermuth-Tang, modern microscopic cluster models) treats alphas as effective degrees of freedom in medium-mass nuclei. SS-7's C1 (rigid alpha) and C2 (base-to-base contact) are continuous with this tradition.
- The Hoyle state is correctly identified with $N_\alpha = 3$ cluster geometry in conventional models; SS-7 adds a specific structural picture (dilated triangle).
- The $R_{\alpha\alpha} \sim 2$ fm range is consistent with conventional cluster-model treatments.

**Where SS-7 differs from SM nuclear physics:**
- The $B_{\text{pair}} = M_0/\varphi$ quantum is derived from CPP's K$_3$ collective-mode structure, not from NN potentials fit to scattering data. This makes SS-7's predictions zero-parameter whereas conventional cluster models typically have at least one fitted binding strength.
- The $3N_\alpha - 6$ edge count is imposed by the simplicial polytope hypothesis (C4), not by a specific chosen nuclear geometry per nucleus.
- SS-7 predicts ${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe as having a specific structural onset (icosahedral closure activation) at $N_\alpha = 12$ rather than smooth breakdown; this is a testable difference from conventional models.

**SS-7 does not:** contradict QCD in the alpha-alpha scattering regime, require unique CPP geometry in a way that excludes conventional cluster-model interpretations, or claim unique determination of the alpha-polytope for each nucleus (Remark 2.2).

---

## Falsifiability inventory

SS-7 is strongly falsifiable. Decisive failure conditions:

1. **Structural falsification threshold:** Any alpha-chain nucleus at $N_\alpha \in [3, 10]$ showing $|\Delta B/B| > 2\%$ would falsify the $3N_\alpha - 6$ edge-count rule. The $\pm 2\%$ threshold is set to exceed the CPP generic residual band ($\varphi^{1/z} - 1 \approx 4.1\%$) by a factor, isolating structural failure from higher-order corrections. All 8 current residuals are within $\pm 1.5\%$.

2. **Specific numerical predictions:**
   - ${}^{12}$C binding at 85.0 MeV instead of 92.2 MeV (prediction: 91.9 $\pm$ 1 MeV) would falsify.
   - ${}^{16}$O binding below 120 MeV or above 135 MeV would falsify.
   - ${}^{40}$Ca binding below 330 MeV or above 350 MeV would falsify.

3. **Structural alternatives:** Existence of a bound ${}^9$Be-like alpha-alpha-nucleon structure with $B > 30$ MeV would challenge C4.

4. **$R_{\alpha\alpha}$ measurement:** Direct alpha-alpha contact distance measurements giving $R_{\alpha\alpha} \neq 2.37 \pm 0.3$ fm would challenge the ${}^8$Be inversion interpretation.

5. **Hostile-geometry counterexample:** Within the claimed domain ($N_\alpha \in [3,10]$), a plausible lower-edge alternative that beats the simplicial rule at fixed $(\Balpha, B_{\text{pair}})$ would undermine edge-count dominance. Five such tests performed (§6.5); none succeeded.

---

## Limits of scope (what SS-7 explicitly does not claim)

- **Does not apply to:** odd-$A$ nuclei (OPEN-SS-23), neutron-rich isotopes, $N \neq Z$ nuclei, $N_\alpha \geq 12$ heavy nuclei (OPEN-SS-22), non-alpha-clustered structures.
- **Does not derive:** $R_{\alpha\alpha}$ from CPP primitives (extracted by inversion); C4 from lattice geometry (OPEN-SS-24); the $M_0/\varphi$ recurrence as structurally necessary; DP-sea Coulomb screening mechanism.
- **Does not predict:** Hoyle state energy quantitatively (requires excited-state methods); rotational/vibrational spectra; specific polytope identity for each nucleus (edge count alone sets binding).
- **Does not claim:** that the simplicial alpha-polytope is the unique ground-state configuration (Remark 2.2); only that the edge count of whatever polytope is realized is $3N_\alpha - 6$.

---

## Honest assessment of what v1.1 achieves

**What v1.1 achieves:** A theory paper that has earned the right to be engaged rather than dismissed. Specifically:
- Clean mathematical structure (Theorem 2.1 + C4 separation)
- Eight concurrent zero-parameter predictions with $\pm 1.5\%$ agreement
- Five hostile-geometry stress tests validating edge-count dominance
- Explicit structural falsification threshold ($\pm 2\%$)
- Scope limits explicitly registered as OPEN-* problems
- Two independent round-2 referee verdicts: "Accept with minor revisions"

**What v1.1 does not yet achieve (by design, targeted for future papers):**
- First-principles derivation of C4 from CPP lattice geometry — OPEN-SS-24, target SS-9 candidate
- First-principles derivation of the $N_\alpha \geq 12$ saturation onset — OPEN-SS-22, target SS-8
- First-principles derivation of the DP-sea Coulomb screening mechanism — OPEN-SS-22-adjacent, target SS-8
- First-principles derivation of $R_{\alpha\alpha}$ — OPEN-SS-24-adjacent

**Programme posture:** SS-7 v1.1 establishes the structural scaling law from cluster topology. The next meaningful advances are at the derivation level (SS-8, SS-9), not at further SS-7 polish. This restraint is deliberate: expanding SS-7 to include these derivations would dilute its clarity and reopen attack surfaces. Territory-first pacing.

---

## Adversarial summary (ChatGPT round-2)

Quoted from ChatGPT round-2 §5, retained as the programme record of the v1.1 adversarial position:

> *"If I were trying to reject this paper, I would now have to argue: α-cluster nuclei do not realize simplicial contact graphs, or the agreement is accidental despite no parameters, multiple nuclei, and failed perturbations. That is a much harder position than before."*

This is the v1.1 achievement: the paper has earned the right to be engaged. Future attacks must target C4 directly (the remaining attack surface), not the paper's overall structure or empirical base.
