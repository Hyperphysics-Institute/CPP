# Verification — TP-1

Verification scripts (stdlib Python; `../scripts/`) and their checks. All run clean.

## Scripts
- **`1700_truncation_regularization.py`** — sets up the truncation/regularization arithmetic: the gradual-shutter bound $\langle n\rangle \le \kappa_0/(4T) + \kappa_0^2/(16T^2)$, the optical reference $\omega_\gamma/2\pi = 10^{15}$ Hz, and the $t_P$-to-optical gap ($\sim 27.5$ orders).
- **`1701_divergence_class.py`** — confirms the logarithmic class: integrates the $1/\omega$ spectrum to $C\ln(\omega_{\mathrm{cut}}/\omega_\gamma)$ and tabulates $\langle n\rangle/C$ at several cutoffs; checks $\ln(\omega_P/\omega_\gamma) = 63.25$ at the naive $1/t_P$.
- **`1706_band_top_cutoff.py`** — the band-top result: the six 600-cell eigenvalues, $\lambda_{\max} = 12$, $\omega_{\max} = \sqrt{12}/t_P = 2\sqrt3/t_P = 6.43\times10^{43}$ rad/s, and $\ln(\omega_{\max}/\omega_\gamma) = 64.49 \Rightarrow \langle N\rangle_{\max} \approx 64.5\,C$.

## Reference values (reproduced by the scripts)
| Quantity | Value |
|---|---|
| $t_P$ | $5.391247\times10^{-44}$ s |
| $1/t_P = c/\ell_P$ | $1.855\times10^{43}$ rad/s |
| $\omega_\gamma = 2\pi\times10^{15}$ Hz | $6.283\times10^{15}$ rad/s |
| $\lambda_{\max}$ (600-cell) | $12 = z$ |
| $\omega_{\max} = \sqrt{12}/t_P$ | $6.43\times10^{43}$ rad/s |
| $\ln(\omega_{\max}/\omega_\gamma)$ | $64.49$ |
| ceiling | $\approx 64.5\,C$ |
| gradual bound at $T = 10^{-14}$ s | $\langle n\rangle \lesssim 1.43$ |
| $t_P \to$ optical-period gap | $\sim 27.5$ orders |

## Cutoff comparison (1706)
| Cutoff | $\ln(\cdot/\omega_\gamma)$ |
|---|---|
| naive $1/t_P$ (v0.3 placeholder) | 63.25 |
| continuum-limit $\pi/\ell_P = \pi/t_P$ | 64.40 |
| **intrinsic band top $\sqrt{12}/t_P$** | **64.49** |

## Open (not yet a verification target)
OPEN-TP-1 — the $O(1)$ coefficient $C$ from the 600-cell Hilbert–Schmidt mode sum $\|T_2\|^2_{\mathrm{HS}}$ with the band-top density of states. No script yet; this is the post-v1.0 computation.

## LaTeX
`../TP-1_truncated_photon.tex` compiles clean (pdflatex ×3 + bibtex) against the master bibliography; 14 pp; 0 undefined citations.
