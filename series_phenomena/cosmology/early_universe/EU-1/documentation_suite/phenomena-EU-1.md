# Phenomena — EU-1: The Primordial Scalar Spectral Index from Substrate Inflation

The empirical phenomena EU-1 explains, the data it is measured against, and its place in the
programme-level registry (current state as of Patch 0787).

## The phenomenon: the primordial scalar power spectrum
The seed density perturbations of the universe — the ripples imprinted on the CMB and grown into all
large-scale structure — are nearly, but not exactly, scale-invariant. Parametrized as
$\mathcal{P}_\zeta(k) = A_s (k/k_*)^{n_s - 1}$, the **scalar spectral index** $n_s$ measures the tilt.
A perfectly scale-invariant (Harrison–Zel'dovich) spectrum has $n_s = 1$. The measured slight *red*
tilt ($n_s < 1$) is the single cleanest dynamical probe of the inflationary epoch.

## The data
- **$n_s$:** Planck 2018 measures $n_s = 0.9649 \pm 0.0042$ — excluding $n_s = 1$ at $\sim 8\sigma$.
- **$\alpha_s$ (running):** Planck 2018 gives $\alpha_s = -0.0045 \pm 0.0067$ (consistent with zero;
  weakly constrained).

## What EU-1 predicts
- **PRED-C-96** — $n_s = 1 - 2/N_* = 1 - 2/57 \approx 0.9649$, theory uncertainty $\sim 5\times10^{-4}$
  ($\approx 0.12\,\sigma_{\text{Planck}}$ from the $O(\alpha)$ SSV correction). **Zero free parameters.**
  The robust content is a *red tilt of magnitude $\sim 2/N_*$* ($n_s \approx 0.96$–$0.97$ for
  $N_* \in [50,60]$); the four-digit central match is at the standard adopted pivot $N_* \approx 57$.
- **PRED-O-34** — running $\alpha_s = -2/N_*^2 \approx -0.0006$, consistent with Planck and a falsifiable
  companion prediction (well inside current bounds; a future measurement decisively away from
  $\sim -0.0006$ would falsify).

## Why it counts as a confirmed prediction
$n_s$ is a *forward* zero-parameter output of the substrate-inflation mechanism (A1 → log → $\delta N$),
not a fitted quantity, and it matches the measured central value. It is therefore classified ✅ CONFIRMED
(register term of art = *measured and consistent with the CPP prediction*) — distinct from "derived from
A1–A11 alone," which it is not. It is a **framework-conditional** confirmation: conditional on FRW/VSL
homogeneity, DP-Sea neutrality, and small-$\alpha$ SSV corrections.

## Registry state (current, Patch 0787)
- **Swarm tally:** EU-1 contributes **1** counted correspondence ($n_s$, PRED-C-96), bringing the
  cumulative headline to **108** zero-parameter empirical correspondences from the unchanged 9-axiom
  stack (swarm-to-axiom ratio $108/9 = 12.0\times$). The headline and the by-tier/by-series tables are
  fully reconciled at 108 (Patch 0787; see the Count Provenance Ledger in `predictions.md`).
- **By-series row:** SR / cosmology = **1** (PRED-C-96, framework-conditional) — EU-1 is the *first*
  SR/cosmology-sector swarm contribution.
- **Tier:** Conditional Quantitative-Numerical (D-N cond.), alongside the 55 nuclear-physics conditional
  entries — same kind of object (zero-parameter, matches data, conditional on framework commitments).
- **$\alpha_s$ (PRED-O-34):** open / future-testable (§2), not yet a counted contribution.
- **No THEO** registered (conditional result; the lemmas are finding-level: LEMMA-NS-HTHEOREM,
  LEMMA-NS-ZRP-DERIVE, LEMMA-NS-BATH).
- **Paper catalog:** EU-1 row under *Phenomena Series — Cosmology / Early Universe*, v1.0 SHIPPED.

## Downstream consumer
EU-1 supplies the **generation** of the primordial adiabatic spectrum. The CPP dark-matter programme
(qDP/hTetra-clouds-as-DM) inherits this spectrum as a passive tracer and *processes* it into observed
structure — so EU-1 is the structure-formation backbone the DM-first paper cites, not a part of it.

## Falsifiers (empirical)
- A measured $n_s$ outside $0.9649 \pm \delta$ ($\delta$ = Planck error $\oplus$ $\sim 5\times10^{-4}$
  theory) falsifies the leading-order result.
- A measured $\alpha_s$ inconsistent with $\approx -0.0006$ falsifies the companion.
- Evidence of early-universe CP occupations being effectively *distinguishable* (per-CP history labels)
  would return the excluded cliff $n_s = 1$.
