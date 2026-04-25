# Philosophy: SS-7 — Alpha-Cluster Regime and the 3N−6 Edge Formula

**Paper:** SS-7 v1.2 (21 April 2026, symmetric-honesty corrections)
**Last updated:** 21 April 2026
**Document type:** Epistemological framing and honest assessment

---

## What kind of result is this?

A **zero-parameter formula reproducing the binding energies of twelve strict $N{=}Z$ alpha-chain nuclei within $\pm 1.5\%$**, plus a re-derivation of the ${}^8$Be near-threshold unboundness. Fourteen independent empirical tests from one formula with no nuclear-physics input, built on constants inherited from SS-5.

**Paper-type declaration (per operating_system.md §4 taxonomy):** This is a **prediction paper**. Success criterion: concurrent multi-nucleus agreement at zero fitted parameters. The twelve Table 1 predictions satisfy this criterion by construction — all twelve use the same two constants ($\Balpha$, $B_{\text{pair}}$), both from SS-5, with no modification.

**Main claim:**
$$B(N_\alpha) = N_\alpha \cdot \Balpha + (3N_\alpha - 6) \cdot B_{\text{pair}} \qquad (N_\alpha \in [3, 14], \text{ strict } N{=}Z)$$

where $3N_\alpha - 6$ is the edge count of any simplicial convex polytope on $N_\alpha$ vertices (Euler's formula), and alpha-chain nuclei realize such polytopes (modeling hypothesis).

---

## Layer classification

Following the SS-5 / SS-3 convention of separating CPP givens from imported structure and mathematical consequences:

| Layer | Content | Status in SS-7 v1.2 |
|---|---|---|
| **A — CPP geometric inputs** | 600-cell, $M_0$, $\varphi$, nucleon structure (SS-2), ${}^4$He tetrahedral closure (SS-5), K$_3$ face eigenvalue structure (SS-5) | *Given* — all established in prior papers |
| **B — Imported structure** | Rigid-alpha assumption (C1); base-to-base contact (C2); K$_3$ mode at alpha-alpha face (C3); simplicial polytope hypothesis (C4) | C1--C3 are geometric extensions of SS-5; C4 is a structural hypothesis within CPP, not yet derived from lattice-level dynamics |
| **C — Mathematical result** | Theorem 2.1: any simplicial polytope on $N_\alpha$ vertices has $E = 3N_\alpha - 6$ edges | Pure mathematics (Euler's formula + triangle-face constraint); not CPP-dependent |
| **D — Empirical conclusion** | $B(N_\alpha) = N_\alpha\Balpha + (3N_\alpha-6)B_{\text{pair}}$, tested against 12 strict $N{=}Z$ nuclei within $\pm 1.5\%$ | Follows from B + C; validated in Table 1 |

The **theorem/hypothesis split** (highlighted box in §1 and §2.2) makes explicit that Theorem 2.1 is mathematics (always true) while C4 is physics (supported empirically by Table 1 and the §6.5 stress tests, but not derived).

---

## Certainty levels per element

| Element | Certainty | Basis |
|---|---|---|
| Theorem 2.1 (edge count) | **Mathematical theorem** | Euler's formula + simplicial constraint |
| Table 1 numerical predictions | **Empirically supported, zero-parameter** | 12/12 concurrent match within $\pm 1.5\%$ (strict $N{=}Z$, $N_\alpha \in [3,14]$); RMS $0.80\%$ |
| ${}^8$Be 92 keV unboundness (re-derivation) | **Empirically confirmed** | Matches observed value by construction given $R_{\alpha\alpha}$ |
| $R_{\alpha\alpha} = 2.37$ fm | **Consistency parameter, not derived** | Inverted from ${}^8$Be binding condition; Finding 4.1 explicit |
| C4 (simplicial polytope hypothesis) | **Empirically supported hypothesis, not derived** | Supported by Table 1 (12 concurrent) + 5 stress tests; OPEN-SS-24 targets derivation |
| $M_0/\varphi$ recurrence across SS-5 and SS-7 | **Empirically supported, not structurally derived** | Same quantum works in 3 contexts; derivation open (§6.2) |
| DP-sea Coulomb screening in bound polytopes | **Inferred from data, not derived** | Required empirically by the agreement of the Coulomb-free formula at $N_\alpha \geq 3$ vs.~full-Coulomb ${}^8$Be analysis; OPEN-SS-25 targets derivation |

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
- SS-7 predicts that the alpha-chain formula should continue to work at the strict $N{=}Z$ extension through ${}^{56}$Ni (confirmed to within $\pm 1\%$ in v1.2). Conventional alpha-cluster models typically require parameter retuning at each nucleus.

**SS-7 does not:** contradict QCD in the alpha-alpha scattering regime, require unique CPP geometry in a way that excludes conventional cluster-model interpretations, or claim unique determination of the alpha-polytope for each nucleus (Remark 2.2).

---

## Falsifiability inventory

SS-7 is strongly falsifiable. Decisive failure conditions:

1. **Structural falsification threshold:** Any strict $N{=}Z$ alpha-chain nucleus at $N_\alpha \in [3, 14]$ showing $|\Delta B/B| > 2\%$ would falsify the $3N_\alpha - 6$ edge-count rule. The $\pm 2\%$ threshold is set to exceed the CPP generic residual band ($\varphi^{1/z} - 1 \approx 4.1\%$) by a factor, isolating structural failure from higher-order corrections. All 12 current residuals are within $\pm 1.5\%$; the largest is ${}^{20}$Ne at $+1.19\%$, and the largest negative is ${}^{28}$Si at $-1.41\%$.

2. **Specific numerical predictions:**
   - ${}^{12}$C binding at 85.0 MeV instead of 92.2 MeV (prediction: 91.9 $\pm$ 1 MeV) would falsify.
   - ${}^{16}$O binding below 120 MeV or above 135 MeV would falsify.
   - ${}^{40}$Ca binding below 330 MeV or above 350 MeV would falsify.
   - ${}^{56}$Ni binding below 470 MeV or above 490 MeV would falsify (v1.2 extension; current prediction 480.5 MeV, measured 484.0 MeV, $-0.73\%$).

3. **Structural alternatives:** Existence of a bound ${}^9$Be-like alpha-alpha-nucleon structure with $B > 30$ MeV would challenge C4.

4. **$R_{\alpha\alpha}$ measurement:** Direct alpha-alpha contact distance measurements giving $R_{\alpha\alpha} \neq 2.37 \pm 0.3$ fm would challenge the ${}^8$Be inversion interpretation.

5. **Hostile-geometry counterexample:** Within the claimed domain ($N_\alpha \in [3,14]$, strict $N{=}Z$), a plausible lower-edge alternative that beats the simplicial rule at fixed $(\Balpha, B_{\text{pair}})$ would undermine edge-count dominance. Five such tests performed (§6.5); none succeeded.

---

## Limits of scope (what SS-7 explicitly does not claim)

- **Does not apply to:** odd-$A$ nuclei, neutron-rich isotopes, $N \neq Z$ nuclei at alpha-chain $N_\alpha$ values (including the ${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe block with $N - Z = +4$), non-alpha-clustered structures. All of these register as OPEN-SS-23, now the primary SS-8 target.
- **Does not apply beyond** $N_\alpha = 14$ with confidence yet; the strict $N{=}Z$ isotopes at $N_\alpha \geq 15$ become increasingly short-lived and AME 2020 precision drops. Extension is future work.
- **Does not derive:** $R_{\alpha\alpha}$ from CPP primitives (extracted by inversion); C4 from lattice geometry (OPEN-SS-24); the $M_0/\varphi$ recurrence as structurally necessary; DP-sea Coulomb screening mechanism (OPEN-SS-25).
- **Does not predict:** Hoyle state energy quantitatively (requires excited-state methods); rotational/vibrational spectra; specific polytope identity for each nucleus (edge count alone sets binding).
- **Does not claim:** that the simplicial alpha-polytope is the unique ground-state configuration (Remark 2.2); only that the edge count of whatever polytope is realized is $3N_\alpha - 6$.

---

## Honest assessment of what v1.2 achieves

**What v1.2 achieves beyond v1.1:**
- Extended the primary claim from 8 to 12 concurrent zero-parameter predictions (RMS $0.80\%$ across all twelve; $0.91\%$ across the original $N_\alpha \in [3,10]$ set).
- Corrected the v1.1 Table 1 isotope-selection error at $N_\alpha = 12, 13, 14$ (non-$N{=}Z$ rows ${}^{48}$Ti/${}^{52}$Cr/${}^{56}$Fe replaced by strict $N{=}Z$ ${}^{48}$Cr/${}^{52}$Fe/${}^{56}$Ni).
- Corrected the v1.1 line-777 factual error on ${}^{48}$Cr (treated as unobserved; actually particle-stable with measured binding 411.462 MeV).
- Retired OPEN-SS-22 (heavy-nuclei icosahedral closure) — the first retirement in the CPP programme record, with narrative documented in `problem_histories/PH-OPEN-SS-22.md`.
- Registered OPEN-SS-25 (DP-sea screening of alpha-alpha Coulomb in bound polytopes) as the correctly-scoped successor to the §5.4 screening physics that had been tagged "OPEN-SS-22-adjacent" in v1.1.
- Updated the RMS citation from $0.88\%$ (seven-nucleus, excluding ${}^{20}$Ne) to $0.91\%$ (first-principles across all eight primary nuclei), resolving the G3 discrepancy registered 20 April.

**What v1.1 achieved (preserved in v1.2):**
- Clean mathematical structure (Theorem 2.1 + C4 separation).
- Five hostile-geometry stress tests validating edge-count dominance.
- Explicit structural falsification threshold ($\pm 2\%$).
- Scope limits explicitly registered as OPEN-* problems.
- Two independent round-2 referee verdicts: "Accept with minor revisions" (ChatGPT, Copilot, 20 April 2026).

**What v1.2 does not yet achieve (by design, targeted for future papers):**
- First-principles derivation of C4 from CPP lattice geometry — OPEN-SS-24, target SS-9 candidate.
- Extension to non-$N{=}Z$ and odd-$A$ nuclei — OPEN-SS-23, target SS-8 (priority upgraded in v1.2).
- First-principles derivation of the DP-sea Coulomb screening mechanism — OPEN-SS-25, target deferred.
- First-principles derivation of $R_{\alpha\alpha}$ — OPEN-SS-24-adjacent.

**What the v1.2 cycle demonstrated about the programme's review dynamics:** The Table 1 finding was discovered 24 hours after v1.1 shipped, during what was supposed to be the SS-8 Phase 1 empirical-map step. The finding could have been suppressed (v1.1 was already published, both reviewers had returned "Accept") or laundered into a new problem ("reframe OPEN-SS-22 to accommodate the correction"). Instead it triggered the symmetric-honesty protocol: a verification letter to three reviewers, all converging on interpretation (a), and a clean retirement in v1.2. This pathway is the relationship-protocol's §2.6 working as designed — same standard applied to own work as to reviewers — and establishes a template for future retirement events.

**Programme posture:** SS-7 v1.2 establishes the structural scaling law from cluster topology, extended through the $N{=}Z$ alpha-chain at $N_\alpha \in [3, 14]$. The next meaningful advances are at the derivation level (SS-8 on OPEN-SS-23, SS-9 candidate on OPEN-SS-24), not at further SS-7 polish. This restraint is deliberate: expanding SS-7 to include these derivations would dilute its clarity and reopen attack surfaces. Territory-first pacing.

---

## Adversarial summary (ChatGPT round-2, v1.1 record)

Quoted from ChatGPT round-2 §5, retained as the programme record of the v1.1 adversarial position:

> *"If I were trying to reject this paper, I would now have to argue: α-cluster nuclei do not realize simplicial contact graphs, or the agreement is accidental despite no parameters, multiple nuclei, and failed perturbations. That is a much harder position than before."*

This was the v1.1 achievement: the paper earned the right to be engaged. Future attacks must target C4 directly (the remaining attack surface), not the paper's overall structure or empirical base.

## Adversarial summary (v1.2 verification, three-reviewer convergence)

The v1.2 cycle added a different adversarial datum: three independent reviewers (ChatGPT, Copilot, Grok) examined a single verification letter and converged without prompting on interpretation (a) — the v1.1 Table 1 plateau was an isotope-selection artifact. None constructed a defensible reason for the non-$N{=}Z$ choice. Quoting the most compact of the three closing positions, from Copilot:

> *"The 'flat −2% residual' disappears immediately. When you switch to $N{=}Z$: the supposed structural plateau vanishes; the model continues smoothly. This is decisive."*

The convergence itself is part of v1.2's adversarial record: if any of the three reviewers had constructed a defensible (b), OPEN-SS-22 would have been reframed rather than retired. Three-reviewer unanimity on (a) made retirement the correct action rather than over-correction.

Combined v1.1 and v1.2 adversarial posture: the paper's primary formula and twelve predictions are now supported across the strict $N{=}Z$ alpha-chain through ${}^{56}$Ni; the v1.1 structural-onset attack surface has been retired rather than defended; the remaining attack surface is C4 itself (derivation pending, OPEN-SS-24) and the assertion that no defensible principled reason exists to include non-$N{=}Z$ isotopes in the primary claim. The latter is now a three-reviewer-verified position.
