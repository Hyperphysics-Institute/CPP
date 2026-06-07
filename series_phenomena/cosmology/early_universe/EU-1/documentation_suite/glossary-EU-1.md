# Glossary — EU-1: The Primordial Scalar Spectral Index from Substrate Inflation

Technical terms as used in the EU-1 derivation. CPP-wide terms are in `master_glossary.md`; this file
covers terms specific to or specially used by EU-1.

**Scalar spectral index ($n_s$)** — the tilt of the primordial scalar power spectrum,
$\mathcal{P}_\zeta(k) \propto k^{n_s - 1}$. $n_s = 1$ is scale-invariant; the measured red tilt
$n_s = 0.9649$ is EU-1's central result, $n_s = 1 - 2/N_*$.

**Running ($\alpha_s$)** — the scale-dependence of the tilt, $\alpha_s \equiv dn_s/d\ln k = -2/N_*^2
\approx -0.0006$ (PRED-O-34).

**$N_*$ (e-folds; pivot)** — number of e-folds of expansion. Total $N_* = \tfrac13\ln(N_{\text{CP}}/N_{\text{GP}})
\approx 60.5$, fixed by the Conscious-Point count; the observable CMB *pivot* sits at $N_* \approx 57$.
$N_{\text{rem}} = N_{\text{end}} - N$ is "e-folds remaining," with $\ln\bar n = 3N_{\text{rem}}$.

**Occupation number ($\bar n$)** — mean number of Conscious Points stacked on a Grid Point. Dilutes as
$\bar n(N) = \bar n_{\text{init}}\,e^{-3N}$. The driver of the expansion boost via its logarithm.

**Configurational chemical potential ($\mu$)** — the entropic "pressure to disperse" of indistinguishable
occupation, $\mu(\bar n) = kT\ln\bar n + \text{const}$. The logarithm is the source of $p = 2$.

**Effective expansion boost ($H_{\text{eff}}$)** — $H_{\text{eff}} = \kappa_0(\mu(\bar n) - \mu(1))
\propto \ln\bar n \propto N_{\text{rem}}$; couples the chemical potential to the Hubble rate.

**Zero-range process (ZRP)** — an interacting-particle stochastic process where a site of occupation
$n$ emits at a rate $g(n)$ depending only on that site's occupation. The minimal PCD/ZBW bath reduces to
a *symmetric constant-rate* ZRP ($g(n) = n$, symmetric $1/12$ kernel) at leading order
(LEMMA-NS-ZRP-DERIVE); its product-Poisson stationary measure gives $\mu \propto \ln\bar n$.

**LEMMA-NS-HTHEOREM** — the $H$-theorem establishing that the symmetric constant-rate ZRP relaxes to its
indistinguishable (product-Poisson) Gibbs state via a monotone KL-divergence Lyapunov function, with an
$O(1)$ spectral gap (relaxation $\ll$ Hubble time).

**LEMMA-NS-ZRP-DERIVE** — the leading-order identification of the PCD/ZBW dynamics with the symmetric
constant-rate ZRP, from {A1, per-CP PCD cycle, vertex-transitive 600-cell, homogeneous inflation}.

**LEMMA-NS-BATH** — the bath-temperature closure showing the long-range Debye residual is bounded by the
plasma coupling $\Gamma = \alpha/\kappa \sim \alpha$ in the ZBW substrate bath, so
$|\mu_{\text{excess}}|/kT = c\,\Gamma^{3/2} \sim 3.6\times10^{-4} \ll \ln\bar n$.

**Plasma coupling ($\Gamma$)** — $\Gamma = q^2/(a\,kT) = \alpha/\kappa$, with $\kappa = kT_{\text{bath}}/E_{\text{Pl}}$.
$\Gamma \lesssim 1$ is weak coupling (Debye–Hückel valid); the Debye residual is large only at
$\Gamma \sim$ tens (cold, strongly coupled — the opposite of the hot tilt epoch).

**$\delta N$ formalism** — the standard separate-universe method relating the curvature perturbation to
the e-fold fluctuation, $\zeta = \delta N$. For a spectator-like boost, $\mathcal{P}_\zeta \propto H_{\text{eff}}^2$,
giving $n_s - 1 = 2\,d\ln H_{\text{eff}}/dN$.

**DP Sea / Dipole Pair** — the CPP vacuum: the lattice with all sites occupied by Dipole Pairs (bound
$\pm$ CP pairs, electrically/colour neutral). Its $\pm$ pair structure supplies exact charge neutrality
(leg 2).

**SSV (Space Stress Vector)** — the substrate field mediating CP–CP interaction; Coulomb-like
($V(r) \propto q^2/r$). Its smallness ($\sim\alpha$) bounds the only correction channel (the $O(\alpha)$
theory uncertainty $\Delta n_s \sim 5\times10^{-4}$).

**Framework-conditional** — the status of $n_s$: leading-order derived and consistent with data,
conditional on standing CPP cosmology commitments (FRW/VSL homogeneity, DP-Sea neutrality, small-$\alpha$
SSV), not yet derived from A1–A11.
