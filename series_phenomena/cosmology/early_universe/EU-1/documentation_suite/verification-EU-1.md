# Verification — EU-1: The Primordial Scalar Spectral Index

Section-B verification record. The executable artifact is
`../scripts/0781_eu1_numerics.py` (Python standard library only; no third-party dependencies).
Run: `python3 series_phenomena/cosmology/early_universe/scripts/0781_eu1_numerics.py`.
Status: **ALL PASS** (8 checks). This file documents what is verified and the expected output.

## What the script verifies

1. **Central result.** $n_s = 1 - 2/57 = 0.964912$ and $\alpha_s = -2/57^2 = -0.000616$ — matching
   Planck 2018 central $n_s = 0.9649$ and consistent with $\alpha_s = -0.0045 \pm 0.0067$.
2. **E-fold bookkeeping.** $N_* = \tfrac13\ln(N_{\text{CP}}/N_{\text{GP}}) = \tfrac13\ln(10^{80}/13)
   = 60.55$ total e-folds; observable pivot $N_* = 57$ (~3.5 e-folds before the end).
3. **Ideal-ZRP slope → $p = 2$.** Grand-canonical Poisson site has $d\mu/d\ln\bar n = 1$ to $\sim10^{-9}$,
   giving the tilt exponent $p = 2$ exactly in the ideal limit.
4. **$O(\alpha)$ SSV-correction table.** Perturbed ZRP $g(n) = n[1 + \lambda(n-1)]$, $\lambda \sim \alpha$:
   $\Delta n_s = 2\eta/N_*$; at the physical coupling $\Delta n_s \approx 4.9\times10^{-4} \approx
   0.117\,\sigma_{\text{Planck}}$; reaches $1\sigma_{\text{Planck}}$ only near $10\times$ the physical
   coupling.
5. **Debye/$\Gamma$ reframing.** $|\mu_{\text{excess}}|/kT = c\,\Gamma^{3/2}$ with $\Gamma = \alpha/\kappa$,
   $\kappa \sim 1$: residual $\approx 3.6\times10^{-4} \ll \ln\bar n \approx 170$; failure threshold
   $\Gamma \approx 44$ (deep strong coupling, opposite the hot tilt epoch).

## Expected output (summary)
```
[PASS] n_s = 1 - 2/57 = 0.9649        n_s = 0.964912
[PASS] alpha_s = -2/57^2 = -0.0006    alpha_s = -0.000616
[PASS] N_efold = (1/3) ln(1e80/13) ~ 60   N_efold = 60.55
[PASS] ideal ZRP slope d mu/d ln rho = 1 (=> p = 2)
[PASS] Delta n_s = 2 eta/N_* scaling matches 0774 table
[PASS] physical-coupling theory error ~5e-4 ~ 0.12 sigma_Planck
[PASS] Debye residual c*Gamma^{3/2} << ln nbar ~ 170   |mu_ex|/kT = 3.60e-04
[PASS] FAIL only at strong coupling Gamma ~ tens        Gamma ~ 44.3
ALL PASS
```

## Notebook policy note (Section B4)
No separate notebook is created for LaTeX compilation or file-format checks. The single stdlib script
above is the canonical verification artifact for EU-1's paper-body numerical claims; it is referenced
from the paper appendix (§Numerical Verification) and the changelog. Independent reproduction by the
review panel (Grok and Copilot recomputed; ChatGPT and Grok SCRIPT-EXECUTED) is recorded in
`reviews-EU-1.md`.
