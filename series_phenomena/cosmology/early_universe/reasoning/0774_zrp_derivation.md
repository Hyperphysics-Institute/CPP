# Reasoning capture — Patch 0774: ZRP identification derived (LEMMA-NS-ZRP-DERIVE)

*Session 154. Deepest leg-1 hardening (Thomas chose sub-arc 1). Derives the ZRP identification (LEMMA-NS-
HTHEOREM's residual premise) from CPP primitives to leading order + quantifies the only correction. Finding:
`zrp_derivation.md`. Script: `scripts/0774_zrp_derivation_corrections.py`. NO THEO.*

## Three ZRP properties derived
(i) Independence: PCD = per-CP cycle (glossary); elementary moves single-CP; only inter-CP coupling = shared
    SSV field (O(Gamma)~O(alpha), bounded 0764-0768).
(ii) g(n)=n: A1 identical CPs + Absolute Moment (every CP 1 PCD cycle/tick at universal rate 1/t_P) -> same
    per-CP rate -> total site rate = n/t_P. Non-linear g(n) only via SSV coupling (O(alpha)).
(iii) Symmetric kernel: 600-cell vertex-transitive (z=12, group 2I) + homogeneous/isotropic inflationary
    background (no SSV gradient) -> uniform 1/12 kernel. Bias needs SSV gradient (absent at leading order).

## Structural payoff
ZRP general theorem: independence+symmetry => product stationary measure for ANY g(n). g(n)=n => Poisson
marginal => A1 Gibbs, mu=kT ln rho => exactly p=2 => n_s=0.9649 (verified dmu/dlnrho=1 to ~1e-12). Product
form for any g(n) => no inter-site correlations => leg 2 mean-field cancellation untouched.

## Correction quantified (script)
SSV coupling: g(n)->n(1+lambda(n-1)), lambda~Gamma~alpha. Keeps product form; deforms marginal. eta=dmu/dlnrho-1
linear in lambda. Delta n_s=2 eta/N_*: at lambda=alpha, Delta n_s~5e-4 (~0.12 sigma_Planck); reaches Planck
err only at ~10 alpha. So n_s=0.9649 +/- ~5e-4 (theory), 8x inside Planck err 0.0042.

## Upgrade
Leg 1 residual: 'assume ZRP' -> 'ZRP is leading-order PCD dynamics forced by {A1, per-CP PCD, vertex-trans
600-cell, homogeneous inflation}, correction = SSV coupling ~alpha -> ~5e-4 theory uncertainty inside Planck.'
With 0772: leg 1 DERIVED TO LEADING ORDER (independence+symmetry+g(n)=n => product-Poisson => H-theorem
relaxation => p=2 => n_s=0.9649 +/- ~5e-4).

## Honest residuals
- Inflationary homogeneity/isotropy (for symmetric kernel) -- epoch input, not derived here.
- Correction sign/magnitude model-dependent; toy fixes only scale (~alpha->~5e-4). n_s carries ~5e-4 theory
  uncertainty, not exact 4-decimal.
- PCD compute step's full content read as local/per-CP/SSV-driven (faithful to glossary, minimal interpretive).
- n_s STILL conditional/grounded; NOT promoted to Section-1/counted. Promotion = panel judgement.

## Honesty discipline
- Reported Delta n_s~5e-4 at alpha as ~0.12 sigma (within Planck but NOT vanishing at 4th decimal) -- gave
  n_s a theory error bar rather than claiming exact 0.9649 unconditionally.
- Named all three residuals explicitly; did not claim 'leg 1 fully derived / n_s unconditional'.
- Tied the correction channel to the already-closed sqrt(n)/Gamma thread (same alpha) -- no new free knob.

## Pointer
- Remaining for full leg-1 derivation: inflationary homogeneity as an established epoch property (or its CPP
  derivation). Parallel: leg 2 A1-A11 derivation of DP-pair neutrality. Either + panel sign-off could
  promote n_s toward Section-1/counted. PCD = Perceive/Compute/Displace.
