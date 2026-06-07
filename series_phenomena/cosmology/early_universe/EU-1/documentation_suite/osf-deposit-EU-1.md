# OSF Deposit Record — EU-1

Section-F registration record. Claude cannot deposit to OSF directly; this file is the prepared
metadata for Thomas (or Isak) to create the OSF component under the parent CPP project. Fill the DOI
back into this file and the paper header once minted.

## Parent project
- CPP parent OSF project DOI: `10.17605/OSF.IO/JXE8D` (per the EU-1 paper title block).
- Create EU-1 as a **component** of the parent project (consistent with prior paper deposits).

## Component metadata

**Title:** EU-1: The Primordial Scalar Spectral Index from Substrate Inflation — A Zero-New-Axiom
Derivation of $n_s = 1 - 2/N_* \approx 0.9649$ from A1 Indistinguishability and Zitterbewegung Bath
Thermalization

**Contributors:** Thomas Lee Abshier, ND (Hyperphysics Institute); Claude Opus (Anthropic).

**Category:** Project / Paper preprint.

**License:** match the parent project's license (confirm at deposit time).

**Tags:** scalar spectral index; inflation; Conscious Point Physics; CMB; n_s; zero-range process;
indistinguishability; chemical potential; delta-N formalism; zero-parameter prediction; 600-cell;
early universe; cosmology.

**Description / abstract (deposit abstract — honest-scope version):**
> EU-1 derives the CMB scalar spectral index from the substrate dynamics of Conscious Point Physics
> (CPP) with no new axiom. The inflationary expansion boost tracks the logarithm of Grid-Point
> occupancy, $H_{\text{eff}} \propto \ln\bar n$, because the dispersal pressure of over-occupied
> *indistinguishable* Conscious Points is the configurational chemical potential $\mu \propto \ln\bar n$
> (axiom A1). The $\delta N$ relation then fixes the canonical slow-roll tilt $n_s = 1 - 2/N_*$ with the
> pivot $N_* \approx 57$ set by the Conscious-Point count, giving $n_s \approx 0.9649$ and running
> $\alpha_s \approx -0.0006$ — the former matching Planck 2018's central value with zero free
> parameters. The result is leading-order derived and consistent with Planck, framework-conditional
> (FRW/VSL homogeneity, DP-Sea charge neutrality, small-$\alpha$ SSV corrections; not yet derived from
> A1–A11), with $O(\alpha)$ theory uncertainty $\sim 5\times10^{-4}$. Both supporting legs are standing
> CPP commitments: the bath is derived to leading order as a symmetric constant-rate zero-range process
> with a provable $H$-theorem, and neutrality follows from the $\pm$ pair structure of the DP Sea.

## Files to upload
- `EU-1_primordial_spectral_index.tex` (v1.0 source).
- Compiled `EU-1_primordial_spectral_index.pdf` (build locally: `pdflatex` ×3; the repo does not commit
  the v1.0 PDF by default — generate at deposit time, or add the `!.../*.pdf` `.gitignore` exception per
  the F.1 SHIP convention).
- `scripts/0781_eu1_numerics.py` (verification; ALL PASS).
- Optionally the documentation suite (`documentation_suite/*.md`) as supplementary materials.

## Linkages
- Predictions: PRED-C-96 ($n_s$), PRED-O-34 ($\alpha_s$) in `predictions.md`. No THEO.
- Cite the parent CPP theory document and Planck 2018 X (inflation) — both in `bibliography/cpp_references.bib`
  (`abshier_eu1_2026`, `planck2018_inflation`).

## Post-deposit checklist
- [ ] Component created under parent `JXE8D`.
- [ ] DOI minted; recorded here and in the paper title block (`% OSF DOI:` line) — schedule as a small
      follow-on patch.
- [ ] Files uploaded; abstract + tags set.
- [ ] Public/embargo status set per Thomas's first-to-publish strategy (note: the DM-first paper cites
      EU-1; coordinate visibility timing with the DM publication plan).
