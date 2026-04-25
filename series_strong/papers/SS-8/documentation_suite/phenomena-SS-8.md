# Phenomena — SS-8: Interstitial-Neutron Binding and the 2E/V Scaling Law on the Alpha-Polytope

**Location:** `/CPP/series_strong/papers/SS-8/documentation_suite/phenomena-SS-8.md`
**Last updated:** 26 April 2026 (v1.0 currency)
**Companion to:** `SS-8_interstitial_neutron_2EV_scaling.tex` (v1.0)

---

## Phenomena Explained

### 1. Single-neutron interstitial binding strength on the strict $N=Z$ alpha-chain at $N_\text{ex} = 2$
- **SM status:** Phenomenological (shell model + pairing energies; multiple fitted parameters per shell). No first-principles geometric account.
- **CPP derivation:** $\Delta_1(N_\alpha) = (2E/V) \cdot B_\text{pair} = (6 - 12/N_\alpha) \cdot B_\text{pair}$, with $B_\text{pair} = M_0/\varphi = 2.342$ MeV inherited unchanged from SS-5. Conditional on C1–C4 (SS-7) + D1–D3 (SS-8 paper-level structural hypotheses).
- **Accuracy:** 11 of 12 rows within 15% in $k_\text{eff}$; 5 of 6 even-$N_\alpha$ validation nuclei within 10% in $\Delta_\text{pred}$ vs. $\Delta_\text{obs}$. Two sub-1% agreements at the most symmetric polytopes:
  - $N_\alpha = 6$ (${}^{26}\mathrm{Mg}$, octahedron): predicted $\Delta_1 = 9.37$ MeV, observed 9.39 MeV — **−0.2%**
  - $N_\alpha = 10$ (${}^{42}\mathrm{Ca}$, gyroelongated square bipyramid): predicted 11.24 MeV, observed 11.36 MeV — **−1.0%**

### 2. Bulk-regime residual sign and magnitude
- **SM status:** Not addressed at this granularity in the SM framework.
- **CPP derivation:** The provisional H3′ model (opposite-polarity pair bonus, transported from SS-5 with $1/\varphi^2$ geometric attenuation) predicts +0.98 MeV per pair from inheritance alone. Empirically the +0.21 mean residual in $k_\text{eff}$ corresponds to +0.98 MeV per pair, **within 10% of the inheritance prediction**.
- **Accuracy:** Sign and magnitude both consistent with the H3′ inheritance prediction; no parameter fitting. The match across $N_\alpha \in \{6, 8, 10, 12, 13, 14\}$ rows is the H3′ falsification test result.

### 3. Polytope-identity insensitivity at non-unique $N_\alpha$
- **SM status:** N/A — the SM framework does not predict a polytope identity.
- **CPP derivation:** The 2E/V law is a function only of $N_\alpha$, not of which specific simplicial deltahedron realizes it. The octahedron and triangular antiprism at $N_\alpha = 6$ both have 12 edges and both predict the same $\Delta_1 = 9.37$ MeV.
- **Accuracy:** Sub-2% agreement at $N_\alpha = 6$ (the polytope-identity-ambiguous case) confirms the prediction is insensitive to the specific identity choice. SS-8 §6 documents that the polytope-identity-ambiguity cases at $N_\alpha = 6$ and $N_\alpha = 12$ do not show larger residuals than the non-ambiguous cases.

### 4. Small-polytope attenuation pattern
- **SM status:** Light-nuclei binding is treated case-by-case in the SM framework with no general structural account of the small-polytope regime.
- **CPP derivation:** The H5′ provisional attenuation accounts for the deviation at $N_\alpha \leq 4$ as a violation of the bulk-regime averaging assumption (D3): with so few vertices the uniform-distribution approximation breaks down. $N_\alpha = 3$ (planar degenerate) is the most extreme case at $-29.8\%$ residual; $N_\alpha = 4$ at $+11.9\%$.
- **Accuracy:** Qualitative — H5′ correctly predicts that the attenuation grows as $N_\alpha$ decreases, but quantitative attenuation form is not yet derived (OPEN-SS-28).

---

## Phenomena Predicted

### 5. Bulk extension to $N_\text{ex} \in \{3, \ldots, 8\}$ — H4′ Pauli-decrement scaling
- **Prediction:** SS-8 §5 extends the central 2E/V scaling law to $N_\text{ex} > 2$ with a per-pair Pauli decrement $c_\text{Pauli} \approx 1/\varphi \approx 0.618$ inherited from SS-5's same-polarity ratio. 30 secondary predictions across $N_\alpha \in \{6, 8, 10, 12, 14\}$ × $N_\text{ex} \in \{3, \ldots, 8\}$. Residuals 8–15%, systematically negative (suggesting $c_\text{Pauli}^\text{true}$ closer to 0.7–0.8 — a higher-order correction).
- **Testable:** Already empirically tested against AME 2020 binding energies (per the SS-8 v1.0 §5 secondary table). Future test: regenerate the residual map with full AME 2020 data and check whether the systematic negative residual closes under a higher-order correction or persists as evidence of a missing mechanism. Falsification: predicted residuals reverse sign or grow beyond the 15% precision band on more than half the secondary cells.

### 6. Polytope-identity prediction at $N_\alpha = 6$ if degeneracy lifts
- **Prediction:** SS-8 v1.0 predicts both octahedron and triangular antiprism realizations give the same $\Delta_1 = 9.37$ MeV at $N_\alpha = 6$. If a future measurement or first-principles calculation distinguishes which polytope ${}^{26}\mathrm{Mg}$ realizes (OPEN-SS-24 closure), SS-8's prediction does not depend on the answer — the agreement at sub-1% holds either way.
- **Testable:** Indirect via OPEN-SS-24's first-principles polytope-identification work. Falsification: empirical evidence that ${}^{26}\mathrm{Mg}$ binding deviates from 9.37 MeV by more than 2% under any specific polytope identification, ruling out the polytope-insensitivity claim.

### 7. Pattern 6 scale recurrence at a fourth scale
- **Prediction:** If the K₃ collective-mode structure is *forced* to recur (rather than merely *permitted*) by the CPP axiom set, then a fourth physical scale where K₃-graph-structured contact occurs should yield the same $B_\text{pair}$ quantum without rescaling. Candidate fourth scales: alpha-deuteron contact in ${}^6$Li, alpha-triton contact in ${}^7$Li, alpha-helion contact in ${}^7$Be.
- **Testable:** Compute alpha-cluster binding contributions in odd-$A$ light nuclei using $B_\text{pair} = 2.342$ MeV unchanged. Preliminary SS-7 inspection of ${}^6$Li gave residual alpha-deuteron binding 1.47 MeV vs. $2 B_\text{pair}/3 \approx 1.56$ MeV (suggestive but not yet a SS-8-confirming test). Falsification: the alpha-deuteron contact in ${}^6$Li requires a different K₃-eigenvalue quantum than 2.342 MeV. SS-9 candidate (OPEN-SS-23 remainder) would be the natural test.

### 8. Forward prediction for unmapped alpha-chain rows
- **Prediction:** SS-8's central law extends mechanically to nuclei beyond ${}^{56}\mathrm{Ni}$ ($N_\alpha > 14$) under the same hypotheses. Predicted $\Delta_1 = (6 - 12/N_\alpha) \cdot 2.342$ MeV scales asymptotically toward $6 \cdot B_\text{pair} = 14.05$ MeV as $N_\alpha \to \infty$.
- **Testable:** Apply the formula to ${}^{60}\mathrm{Zn}$ ($N_\alpha = 15$), ${}^{64}\mathrm{Ge}$ (16), ${}^{68}\mathrm{Se}$ (17), and so on, comparing against AME 2020 data. Falsification: systematic deviation of the precision band beyond 15% across multiple unmapped rows, indicating breakdown of the bulk-regime assumption or onset of new physics. (Note: heavy-nucleus regime is OPEN-SS-23 inheritance and is scope-disclosed as out of v1.0 coverage.)

---

## Cumulative swarm contribution

SS-8 v1.0 contributes **42 conditional zero-parameter predictions** to the running CPP swarm total of 103 (per `predictions.md` Cumulative Swarm Tally section, 26 April 2026):
- 12 primary at $N_\text{ex} = 2$ across $N_\alpha \in [3, 14]$ (PRED-C-54 through PRED-C-65)
- 30 secondary at $N_\text{ex} \in [3, 8]$ across $N_\alpha \in \{6, 8, 10, 12, 14\}$ (PRED-C-66 composite entry)

All 42 are conditional on hypotheses C1–C4 (inherited from SS-7) plus D1–D3 (introduced in SS-8). Promotion path: closing OPEN-SS-24 (C4 from primitives) + OPEN-SS-26 (D1 Level-3) + OPEN-SS-27 (D2 derivation) + OPEN-SS-28 (D3 derivation) would jointly promote all 42 to unconditional D-N — the largest single-paper conditional-to-unconditional shift available in the programme.
