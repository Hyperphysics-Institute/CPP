# Mechanism — EU-1: The Primordial Scalar Spectral Index from Substrate Inflation

How the CPP substrate actually produces the CMB tilt, in physical terms, with each step tied to the
derivation and the numerical verification (`../scripts/0781_eu1_numerics.py`, ALL PASS).

## The picture in one paragraph
The early universe is a near-saturated lattice of Grid Points (GPs), each over-occupied by many
Conscious Points (CPs) bound into Dipole Pairs. Their Zitterbewegung (ZBW) switching is a fast bath
that constantly re-shuffles which CP sits where; because CPs carry no identity (axiom A1), only the
*occupation number* of each GP is physical. An over-occupied GP carries a configurational "pressure to
disperse" — the chemical potential $\mu \propto \ln\bar n$ — and that dispersal pressure is what drives
the expansion. As the universe expands, occupancy dilutes, the pressure falls *logarithmically*, and
the slight scale-dependence of the frozen CMB modes is exactly the logarithmic-derivative slope of
that pressure: $n_s - 1 = -2/N_*$.

## Mechanism 1 — expansion by dilution, not stretching
CPP does not grow the lattice spacing (fixed at $l_P$); it expands by **DP-Sea unstacking on a fixed
scaffold**. Mean occupancy obeys $\bar n(N) = \bar n_{\text{init}}\,e^{-3N}$, so $\ln\bar n = 3N_{\text{rem}}$
(e-folds remaining). The total e-fold budget is set by the CP count,
$N_* = \tfrac{1}{3}\ln(N_{\text{CP}}/N_{\text{GP}}) \approx 60.5$ (verified: $\tfrac13\ln(10^{80}/13) = 60.55$);
the observable pivot sits at $N_* \approx 57$. *Intuition:* the universe is a compressed crowd thinning
out; "how thinned" is just the log of the crowding, and the crowd's total size sets how long it thins.

## Mechanism 2 — the logarithmic dispersal pressure (the engine of the tilt)
Identical CPs on a GP are occupation-number objects (A1) → Gibbs $1/n!$ → grand-canonical Poisson site
($Z = e^{z_1}$) → $\mu(\bar n) = kT\ln\bar n + \text{const}$. The expansion boost couples linearly to
this excess pressure, $H_{\text{eff}} = \kappa_0(\mu(\bar n) - \mu(1)) \propto \ln\bar n \propto N_{\text{rem}}$.
*Intuition:* the pressure that disperses a crowd of *indistinguishable* members is entropic
(microstate-counting), and entropy of occupation goes as the log — not as a mechanical force-per-member.
This is why the boost is logarithmic and not a power law; every power-law alternative gives an absurd
tilt ($n_s = 1 - 6q$), so near-scale-invariance selects the log. (Verified: ideal-ZRP slope
$d\mu/d\ln\bar n = 1 \Rightarrow p = 2$.)

## Mechanism 3 — the bath reaches the indistinguishable state, fast
For $\mu \propto \ln\bar n$ to be the *operative* pressure, the occupations must actually thermalize to
the indistinguishable Gibbs (Poisson) distribution before inflation ends. The minimal ZBW dynamics is a
symmetric constant-rate **zero-range process** (independent per-CP hops at the universal clock rate,
$g(n)=n$, symmetric $1/12$ kernel from the vertex-transitive 600-cell). It relaxes to product-Poisson
via a KL-divergence $H$-theorem (LEMMA-NS-HTHEOREM), with an $O(1)$ spectral gap → relaxation $\ll$
Hubble time. *Intuition:* the shuffling bath erases any "which-CP-where" memory; the only memory it can't
erase is *how many*, which settles to the maximum-entropy occupation. The labelled ("distinguishable")
state that would give $n_s = 1$ is not even a stationary state of this bath.

## Mechanism 4 — neutrality keeps the tilt clean
A generic $\pm$ plasma would source a mean-field $\mu_{\text{excess}} \propto \bar n$ that swamps the
log at $\bar n \sim 10^{74}$. The DP Sea is built of bound $\pm$ pairs, so $n_+ = n_-$ exactly, net
charge $= 0$ at every $\bar n$, and the leading mean-field cancels. *Intuition:* the substrate is
charge-balanced by construction, so the only surviving occupation-dependence is the entropic log.

## Mechanism 5 — the long-range Debye scare is a phantom
After neutrality cancels the mean-field, the next residual is Debye–Hückel, $\propto -\sqrt{\bar n}$ —
naively enormous. But for a Coulomb plasma it is governed by the coupling $\Gamma$ through
$|\mu_{\text{excess}}|/kT = c\,\Gamma^{3/2}$, and in the hot ZBW substrate bath ($kT \sim E_{\text{Pl}}$,
$\kappa \sim 1$) one has $\Gamma \sim \alpha \approx 0.0073$, so the residual is $\sim 3.6\times10^{-4}
\ll \ln\bar n \approx 170$ (verified). *Intuition:* a hot plasma self-screens; the $\sqrt{\bar n}$ term
is only large in a *cold, strongly coupled* plasma — the opposite of the tilt epoch.

## Assembling the tilt
$\mathcal{P}_\zeta \propto H_{\text{eff}}^2$ ($\delta N$ spectator) and $H_{\text{eff}} \propto N_{\text{rem}}$
give $n_s - 1 = 2\,d\ln H_{\text{eff}}/dN = -2/N_{\text{rem}}$. At the pivot $N_* \approx 57$:
**$n_s = 1 - 2/57 \approx 0.9649$, $\alpha_s = -2/57^2 \approx -0.0006$** — the coefficients
$\kappa_0, kT, z_1$, and the offset all drop out of the logarithmic derivative (verified:
$n_s$ invariant across wide ranges). Remove the $1/n!$ (distinguishable labels) and the pressure goes
flat → the excluded $n_s = 1$ cliff. The indistinguishability is the whole mechanism.
