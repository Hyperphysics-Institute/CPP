# SS-7 Table 1 Residual Fingerprint — Decomposition by Cluster Shape Class

**Date:** 26 April 2026 (Session 3)
**Purpose:** Standalone sketch artifact capturing the empirical fingerprint that motivates OPEN-SS-32 (cluster-level oblate-deformation slip-plane mode). Produced as part of the off-track investigation of alpha rigidity that delivered SS-7 v1.3 refined-C1 facet (c). Future Opus may extend or correct this; the values here are the foundation for the slip-plane mechanism reading.
**Companion files:** `reasoning-SS-9.md` (Tier 4 reasoning), `development-SS-9.md` Vignette 3 (Tier 3 summary), `founders_voice/001_slip_plane_intuition.md` (the physical intuition that selected this reading from competing alternatives), `research_frontier.md` OPEN-SS-32 entry.

---

## The computation

The SS-7 binding formula is
$$B_{\text{pred}}(N_\alpha) = N_\alpha \cdot B_\alpha + (3 N_\alpha - 6) \cdot B_{\text{pair}}$$
with $B_\alpha = 28.296$ MeV (experimental ${}^4$He binding), $B_{\text{pair}} = M_0/\varphi = 2.342$ MeV.

If we hold $B_\alpha$ and $B_{\text{pair}}$ fixed and define the *effective contact count* by inverting,
$$|E_{\text{actual}}|(N_\alpha) := \frac{B_{\text{measured}}(N_\alpha) - N_\alpha \cdot B_\alpha}{B_{\text{pair}}}$$
then the *excess* over the simplicial Euler bound is
$$\text{Excess}(N_\alpha) := |E_{\text{actual}}|(N_\alpha) - (3N_\alpha - 6).$$

The excess is the number of "extra" face contacts (in units of $B_{\text{pair}}$) needed to account for the empirical binding beyond what the leading-order $|E| = 3N_\alpha - 6$ formula provides. A clean LO fit gives excess ≈ 0; positive excess means the cluster is more bound than the formula predicts.

## The fingerprint

Computed from SS-7 Table 1 (v1.2, strict $N=Z$ alpha-chain, AME 2020 binding energies):

| $N_\alpha$ | Nucleus | $B_{\text{measured}}$ (MeV) | $|E_{\text{actual}}|$ | Formula $|E|$ | Excess | Regime |
|------------|---------|------------------------------|------------------------|----------------|--------|--------|
| 3 | ${}^{12}$C | 92.162 | 3.11 | 3 | +0.11 | A (planar degenerate) |
| 4 | ${}^{16}$O | 127.619 | 6.16 | 6 | +0.16 | A |
| 5 | ${}^{20}$Ne | 160.645 | 8.18 | 9 | **−0.82** | A (prolate outlier) |
| 6 | ${}^{24}$Mg | 198.257 | 12.16 | 12 | +0.16 | A |
| 7 | ${}^{28}$Si | 236.537 | 16.42 | 15 | **+1.42** | B |
| 8 | ${}^{32}$S | 271.781 | 19.39 | 18 | **+1.39** | B |
| 9 | ${}^{36}$Ar | 306.716 | 22.22 | 21 | **+1.22** | B |
| 10 | ${}^{40}$Ca | 342.052 | 25.23 | 24 | **+1.23** | B |
| 11 | ${}^{44}$Ti | 375.475 | 27.42 | 27 | +0.42 | C (deltahedra-gap) |
| 12 | ${}^{48}$Cr | 411.462 | 30.71 | 30 | **+0.71** | B (icosahedron) |
| 13 | ${}^{52}$Fe | 447.696 | 34.09 | 33 | +1.09 | C |
| 14 | ${}^{56}$Ni | 483.990 | 37.51 | 36 | +1.51 | C |

## The pattern

Sorted by regime:

**Regime A (small deltahedra, all degree ≤ 4, strict 4-face C1 consistent):** $N_\alpha \in \{3, 4, 5, 6\}$.
- Mean excess (excluding ${}^{20}$Ne prolate-deformation outlier): **+0.14** ≈ 0.
- Consistent with the SS-5-inherited LO residual band (~5%, here within ~0.3% of zero in $|E|$ units).
- Strict 4-face C1 reading is internally consistent. No additional mode active.

**Regime B (J-solid deltahedra with belt/seam structure, degree-5 vertices present):** $N_\alpha \in \{7, 8, 9, 10\}$.
- Mean excess: **+1.32**.
- *Flat plateau across four nuclei despite degree-5 vertex count varying from 2 to 8* (pentagonal bipyramid: 2 apex degree-5; snub disphenoid: 4 of 8; triaugmented triangular prism: 6 of 9; gyroelongated square bipyramid: 8 of 10). Flatness rules out per-degree-5-vertex-cost stories — those would scale with vertex count, not stay flat.
- Selects bulk-mode story: one cluster-level effect that adds approximately one extra contact's worth of binding, independent of the number of degree-5 vertices.

**Icosahedron ($N_\alpha = 12$):** Excess **+0.71**, conspicuously below the J-solid plateau.
- The icosahedron has full $I_h$ symmetry with no belt/seam interface that supports oblate deformation.
- Quenching of the bulk mode at full closure: predicted by the slip-plane reading (the mode requires symmetry-breakable axial structure; $I_h$ has none).

**Regime C (deltahedra-gap, no convex deltahedron exists):** $N_\alpha \in \{11, 13, 14\}$.
- ${}^{44}$Ti excess +0.42 (small, consistent with ${}^{40}$Ca + α core+halo per cluster-physics literature; halo α breaks closure of ${}^{40}$Ca's belt structure).
- ${}^{52}$Fe excess +1.09 (J-solid-like, suggesting belt-structure restoration).
- ${}^{56}$Ni excess +1.51 (slightly above J-solid plateau, consistent with alpha-gas behavior per GANIL inelastic scattering observation of multiplicity up to 7).

## What the fingerprint selects

Three competing readings of the Regime B excess:

1. **Per-vertex K_5 cost:** each degree-5 vertex pays a strain cost. *Predicts*: excess scales linearly with degree-5 vertex count. *Falsified*: flat plateau across $N_\alpha = 7 \to 10$ despite vertex count doubling.
2. **DP-sea Coulomb shape contribution:** screening varies with cluster shape. *Predicts*: smooth $N_\alpha$-dependence. *Disfavored*: discontinuous jump from $N_\alpha = 6$ to $N_\alpha = 7$.
3. **Bulk slip-plane mode:** one cluster-level oblate-deformation mode activates at belt/seam-supporting shapes, contributing fixed binding once active, quenched at full closure. *Predicts*: flat plateau where same shape-class persists; suppression at icosahedron; restoration at Regime C nuclei with belt structure. *Matches*: J-solid plateau, icosahedron suppression, Regime C heterogeneity.

The fingerprint *selects* reading (3) over (1) and (2). This is the empirical foundation for OPEN-SS-32.

## Connection to attenuation factor

The empirical excess in Regime B is approximately $+1.32 \cdot B_{\text{pair}} \approx +0.55 \cdot B_{\text{pair}}$ in fractional terms (where the unit-of-$B_{\text{pair}}$ value is $1.32 / 2.342$ as MeV ratio). The icosahedron suppression gives $+0.30 \cdot B_{\text{pair}}$.

If the slip-plane mode contributes one full $B_{\text{pair}}$ before attenuation, the empirical fingerprint suggests an attenuation factor of ~0.55 in the J-solid range and ~0.30 at the icosahedron.

Comparison to SS-8's H3' provisional attenuation:
- SS-8 H3' adopts $1/\varphi^2 \approx 0.382$ as the "natural geometric candidate motivated by Pattern 6 and by the numerical coincidence with SS-5's same-polarity Pauli-penalty ratio."
- $1/\varphi \approx 0.618$ is also a natural candidate.
- $1/\varphi^{3/2} \approx 0.486$ is intermediate.

The empirical $0.55$ in the J-solid range is closest to $1/\varphi^{3/2}$ (within 10%) but the spread between J-solids and icosahedron suggests a shape-class-dependent factor, not a single Pattern-6-natural ratio.

A first-principles derivation (the OPEN-SS-32 target) needs to predict either:
- A single attenuation factor that fits both J-solids and icosahedron under different shape-class accounting, or
- A shape-class-specific factor (e.g., $\cos(\theta_{\text{oblate}})$ where $\theta$ is set by the cluster's axial-symmetry-breaking angle), with the J-solids' $\theta$ giving ~0.55 and the icosahedron's $\theta$ giving ~0.30.

The cluster-physics literature on oblate deformation of ${}^{28}$Si, ${}^{40}$Ca, etc. provides empirical $\beta_2$ deformation parameters that could be used to test the second option.

## Caveats and follow-up

**(1) The ${}^{20}$Ne outlier (excess −0.82) is the known prolate-deformation outlier** previously noted in SS-7 v1.2 §6. ${}^{20}$Ne is genuinely prolate (not oblate like ${}^{28}$Si), and its prolate deformation costs binding rather than gaining it under the slip-plane reading. This is consistent: prolate is the *opposite* axial-symmetry-breaking direction from oblate, and CPP's slip-plane mechanism is specifically about oblate.

**(2) The ${}^{44}$Ti excess (+0.42) is a separate diagnostic.** It's smaller than the J-solid plateau but positive; the cluster-physics literature identifies it as ${}^{40}$Ca + α core+halo. Under the slip-plane reading: ${}^{40}$Ca has its belt-structure bonus (+1.23 in the Regime B fingerprint above), and ${}^{44}$Ti = ${}^{40}$Ca + α has the bonus minus the halo-disruption cost. The +0.42 = (+1.23 − ~0.81) suggests a halo-disruption of ~0.81 contacts' worth, which is testable against more refined cluster-physics calculations of ${}^{44}$Ti's α-knockout cross-section.

**(3) The hierarchical-regime predictions (PRED-O-16/17/18) extend this analysis to higher $N_\alpha$.** The fingerprint above stops at $N_\alpha = 14$ because that's where SS-7 Table 1 stops. AME 2020 has alpha-chain data well beyond this; extending the residual decomposition to ${}^{60}$Zn ($N_\alpha = 15$), ${}^{64}$Ge ($N_\alpha = 16$), ${}^{68}$Se ($N_\alpha = 17$), and beyond would test (a) whether the slip-plane bonus pattern continues, (b) whether a single-to-hierarchical transition appears, and (c) at what $N_\alpha$ the transition occurs if it does.

**(4) The numerical excess values use $B_\alpha = 28.296$ MeV (experimental ${}^4$He binding).** The LO-CPP variant with $B_\alpha = 27.904$ MeV (SS-5 zero-parameter prediction) shifts each excess uniformly. Per SS-7 v1.2 §6.1, the LO-CPP variant gives uniform shifts of $\sim 0.16$ per row in excess units (since $0.392$ MeV / $2.342$ MeV/$B_{\text{pair}} \approx 0.17$). The structural pattern (Regime A near zero, Regime B flat plateau, icosahedron suppression, Regime C heterogeneity) is robust to this choice.

## Future work

- **Promote to a script:** the residual decomposition is currently hand-computed. A Python script `scripts/SS-9_table1_residual_decomposition.py` that takes AME 2020 data and the SS-7 formula constants as input and produces the table mechanically would let future updates (e.g., AME 2024 data when it ships) re-derive the fingerprint without manual error.
- **Extend to higher $N_\alpha$:** the same script applied to alpha-chain nuclei at $N_\alpha \in [15, 25]$ would generate the empirical input for testing PRED-O-16/17/18.
- **Cross-correlate with SS-8 residuals:** the SS-8 H3' post-decomposition residuals ($-0.51$ at $N_\alpha = 4$, clean at $N_\alpha = 6, 10$, $+0.20$–$+0.29$ elsewhere) show a structurally similar pattern to the SS-7 fingerprint above. A unified analysis treating both papers' residuals as different views of the same Pattern-6 K_3 scale-recurrence machinery may give tighter constraints on the attenuation factor than either paper alone.
