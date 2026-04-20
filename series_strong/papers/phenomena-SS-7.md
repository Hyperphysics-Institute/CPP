# Phenomena: SS-7 — Alpha-Cluster Regime and the 3N−6 Edge Formula

**Paper:** SS-7 v1.1 (20 April 2026, post-round-2 minor revisions)
**Last updated:** 20 April 2026

---

## PHEN-P — Quantitative zero-parameter predictions

All predictions use $\Balpha = 28.296$ MeV and $B_{\text{pair}} = 2.342$ MeV, both inherited from SS-5. Zero fitted parameters. Experimental values from AME 2020.

| ID | Quantity | CPP prediction | Measured (MeV) | Error | Params |
|---|---|---|---|---|---|
| PHEN-P-SS-7-1 | ${}^{12}$C binding $B$ | **91.915 MeV** | 92.162 | **−0.27%** | 0 |
| PHEN-P-SS-7-2 | ${}^{16}$O binding $B$ | **127.237 MeV** | 127.619 | **−0.30%** | 0 |
| PHEN-P-SS-7-3 | ${}^{20}$Ne binding $B$ | **162.560 MeV** | 160.645 | **+1.19%** | 0 |
| PHEN-P-SS-7-4 | ${}^{24}$Mg binding $B$ | **197.883 MeV** | 198.257 | **−0.19%** | 0 |
| PHEN-P-SS-7-5 | ${}^{28}$Si binding $B$ | **233.205 MeV** | 236.537 | **−1.41%** | 0 |
| PHEN-P-SS-7-6 | ${}^{32}$S binding $B$ | **268.528 MeV** | 271.781 | **−1.20%** | 0 |
| PHEN-P-SS-7-7 | ${}^{36}$Ar binding $B$ | **303.851 MeV** | 306.716 | **−0.93%** | 0 |
| PHEN-P-SS-7-8 | ${}^{40}$Ca binding $B$ | **339.173 MeV** | 342.052 | **−0.84%** | 0 |

**Statistics:** All 8 predictions within $\pm 1.5\%$. RMS error 0.88%. Maximum deviation $+1.19\%$ (${}^{20}$Ne, consistent with known prolate deformation).

| ID | Quantity | CPP derivation | Extracted value | Status |
|---|---|---|---|---|
| PHEN-P-SS-7-9 | ${}^8$Be unboundness (re-derived from SS-5) | $3N-6 = 0$ at $N_\alpha=2$ + Coulomb | 92 keV above threshold | Confirmed |
| PHEN-P-SS-7-10 | Alpha-alpha contact distance $R_{\alpha\alpha}$ | Inversion from ${}^8$Be (consistency, not forward prediction) | 2.37 fm | Extracted, not derived |

---

## PHEN-E — Empirical phenomena explained

| ID | Phenomenon | CPP account |
|---|---|---|
| PHEN-E-SS-7-1 | Alpha-cluster structure of $A = 4N_\alpha$ nuclei | C1 + C2: rigid tetrahedral alpha units with base-to-base contact |
| PHEN-E-SS-7-2 | Binding energy curve for $A = 12$--$40$ | $B(N_\alpha) = N_\alpha\Balpha + (3N_\alpha-6)B_{\text{pair}}$ formula |
| PHEN-E-SS-7-3 | ${}^8$Be barely unbound (92 keV) | Single alpha-alpha contact + Coulomb at $R_{\alpha\alpha} = 2.37$ fm |
| PHEN-E-SS-7-4 | ${}^{12}$C Hoyle state as three-alpha cluster | $N_\alpha = 3$ dilated triangle geometry (§4.3) |
| PHEN-E-SS-7-5 | Alpha-alpha contact distance ∼ 2 fm in cluster models | $R_{\alpha\alpha} = 2.37$ fm consistent with alpha RMS radius 1.68 fm |
| PHEN-E-SS-7-6 | Onset of deviation near ${}^{48}$Ti / ${}^{56}$Fe | Structural onset at $N_\alpha = 12$ icosahedral closure (OPEN-SS-22) |

---

## PHEN-V — Consilience with other CPP results

| ID | Cross-paper agreement | Nature of consilience |
|---|---|---|
| PHEN-V-SS-7-1 | $B_{\text{pair}} = M_0/\varphi$ shared with SS-5 (nucleon-nucleon) | Same K$_3$ eigenvalue calculation at alpha-scale contact; recurrence across spatial scales |
| PHEN-V-SS-7-2 | $B_{\text{pair}}$ shared with SS-5 (${}^4$He closure bonus) | Same quantum in three contexts: N-N contact, ${}^4$He closure, alpha-alpha contact |
| PHEN-V-SS-7-3 | $M_0$ shared with SM-8 | SS-7 inherits $M_0 = 3.7898$ MeV without re-derivation |
| PHEN-V-SS-7-4 | $\Balpha$ shared with SS-5 | SS-7 uses SS-5's ${}^4$He binding as input to multi-alpha formula |
| PHEN-V-SS-7-5 | Cascade paradigm shared with SS-5 | Both papers use hierarchical rigid-tetrahedral base-to-base bonding; SS-7 is the second level of the cascade |
| PHEN-V-SS-7-6 | Closed-polytope gap shared with SS-5 | SS-5: no closed polytope at $A = 5, 8$ (nucleon level); SS-7: no simplicial polytope at $N_\alpha = 2$ (alpha level; gives ${}^8$Be unboundness) |
| PHEN-V-SS-7-7 | LO stereographic residual band shared with SM-3, SM-6--8, SS-1, SS-3--5 | Table 1 residuals all within $\varphi^{1/z} - 1 \approx 4.1\%$ CPP generic band |

---

## Adversarial test results (§6.5)

Contributed by ChatGPT re-review engagement. At fixed $(\Balpha, B_{\text{pair}})$, the simplicial $E = 3N_\alpha - 6$ rule outperforms plausible lower-edge alternatives in all five tests:

| ID | Nucleus | $N_\alpha$ | $E_{\text{simp}}$ | Error (simp) | $E_{\text{alt}}$ | Alt geometry | Error (alt) |
|---|---|---|---|---|---|---|---|
| PHEN-A-SS-7-1 | ${}^{32}$S | 8 | 18 | −1.20% | 12 | cube | −6.37% |
| PHEN-A-SS-7-2 | ${}^{32}$S | 8 | 18 | −1.20% | 16 | square antiprism | −2.92% |
| PHEN-A-SS-7-3 | ${}^{28}$Si | 7 | 15 | −1.41% | 12 | wheel-like | −4.38% |
| PHEN-A-SS-7-4 | ${}^{36}$Ar | 9 | 21 | −0.94% | 20 | monocapped sq antiprism | −1.70% |
| PHEN-A-SS-7-5 | ${}^{40}$Ca | 10 | 24 | −0.84% | 20 | pentagonal-antiprism-type | −3.58% |

**Net effect:** Edge-count dominance at leading order confirmed. ${}^{36}$Ar is the single-edge-sensitivity diagnostic: dropping $E$ by 1 degrades agreement by exactly $B_{\text{pair}}/B = 0.77\%$, matching the one-quantum difference.
