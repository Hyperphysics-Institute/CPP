# Phenomena — TP-1: The Truncated Photon and the Lattice Regularization of Shutter-Induced Photon Creation

What TP-1 explains, the result it is measured against, and its place in the programme registry.

## The phenomenon: the truncated photon
Rukan, Gulla and Skaar (PRL 2026, arXiv:2510.21636) show, in standard quantum optics, that passing a single photon through a fast shutter produces a state that is *locally* a single photon on one side and vacuum on the other, but *globally* a $0\to\infty$ photon-number mixture. The effect follows from broken time-translation invariance at the shutter; the expected created-photon number $\langle N\rangle$ diverges only in the idealized instantaneous-shutter limit, regularized in their treatment by a formal high-frequency cutoff "arbitrarily high."

## PHEN-E — empirical / theoretical facts
- The RGS result is a theorem of standard quantized-EM optics (accepted PRL), not itself a CPP claim. CPP inherits its correctness, it does not re-derive it.
- Dynamical-Casimir photon creation from time-dependent boundaries is experimentally established (Wilson et al., *Nature* 2011, superconducting-circuit realization).
- The instantaneous-shutter divergence is logarithmic — derived here directly from the RGS kernel, matching their stated conclusion.

## PHEN-P — zero-parameter predictions
**None.** TP-1 makes no new zero-parameter numerical prediction and adds nothing to the swarm tally. Its framework-specific output is *foundational, not falsifiable in the testable regime*: the substrate supplies the finite ceiling $\langle N\rangle_{\max} = C\ln(\omega_{\max}/\omega_\gamma) \approx 64.5\,C$ that the continuum's instantaneous idealization lacks, with the cutoff grounded as the intrinsic 600-cell band top $\omega_{\max} = \sqrt{12}/t_P$ ($\lambda_{\max} = z = 12$). The ceiling is reached only in the unphysical instantaneous limit; for realistic shutters CPP and the continuum coincide, so there is no experimentally accessible number to predict.

## PHEN-V — consilience with other CPP results
- **QM-5 (600-cell QFT):** the same finite mode spectrum that renders the electron self-energy finite (QM-5) here terminates the truncation $1/\omega$ tail. One mechanism, two regularizations — no new ingredient.
- **QM-4 (measurement as partial trace):** the local-simple/global-complex structure RGS find is the QM-4 partial-trace pattern under the Nexus, with no extra assumption.
- **The band top $\omega_{\max} = \sqrt{12}/t_P$** is fixed by the 600-cell coordination $z = 12$ — the same $z$ that sets gauge mode-fractions and the cage mass formula throughout CPP.

## Registry state
- **Swarm tally:** unchanged (no PRED). Cumulative headline stays at its current value; TP-1 contributes a structural/foundational result, not a counted correspondence.
- **Proposition:** PROP-TP-1-1 (lattice regularization) registered in `frontier_sectors/PROP.md`.
- **Open problem:** OPEN-TP-1 (the $O(1)$ coefficient $C$ from the 600-cell HS mode sum) in `frontier_sectors/QM.md`, status PARTIAL (class closed + cutoff grounded).
- **No THEO** (framework-conditional, embedding not entailment).
- **Paper catalog:** TP-1 row under *Phenomena Series — Quantum Optics*, v1.0 SHIPPED; first quantum-optics-sector paper.

## Falsifiers (structural, not empirical)
- A CPP treatment forcing global non-unitarity would break the compatibility claim.
- A band-top density of states that reshapes the $1/\omega$ tail before $\omega_{\max}$ would modify the ceiling (OPEN-TP-1).
- A computed $C$ far from order unity would shift the $\approx 64.5\,C$ ceiling (but not the logarithmic class).
