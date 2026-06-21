# Mechanism — TP-1: The Truncated Photon and the Lattice Regularization of Shutter-Induced Photon Creation

How the CPP substrate realizes the Rukan–Gulla–Skaar (RGS) truncated photon, step by step, each tied to the paper and to the numerical verification (`../scripts/1700_*.py`, `1701_*.py`, `1706_band_top_cutoff.py`).

## The picture in one paragraph
A single photon is a perturbation of the DP-Sea. A fast shutter is a time-dependent boundary condition imposed on that medium. Standard quantum optics (RGS) shows the truncation turns the one-photon state into a $0\to\infty$ photon-number mixture — locally a single photon on one side, vacuum on the other — with an expected number $\langle N\rangle$ that diverges only as the shutter approaches instantaneous. CPP does not predict this effect; it *embeds* it: every structure RGS assume (a real medium, a mode basis, a partial-trace environment, a driven boundary) is a standing CPP mechanism, and the divergence is tamed not by an imposed cutoff but by the fact that the 600-cell lattice has a finite mode spectrum with a hard band top.

## Mechanism 1 — the cuttable photon is a DP-Sea perturbation
Standard QFT photons are excitations of an abstract field with no medium; "cutting" one is awkward. In CPP the photon is a propagating perturbation of the Dipole-Pair Sea, so subjecting it to a shutter is just a boundary manipulation of a real medium. *This is an embedding, not a new mechanism* — it supplies the medium the RGS construction tacitly needs.

## Mechanism 2 — the 0→∞ Fock mixture is bosonic 600-cell occupation (QM-5)
RGS's photon-number mixture lives in a second-quantized Fock space. QM-5 builds exactly that from the 600-cell normal modes: bosonic occupation because DI-bits can pile up on a Grid Point. The RGS construction lives inside QM-5 without strain.

## Mechanism 3 — local-simple / global-complex is the QM-4 partial trace under the Nexus
RGS find a single photon locally on one side and vacuum on the other, while the global state is an entangled superposition — their own reasoning traces over the unobserved (backward) modes, Unruh-style. QM-4 implements exactly this: measurement is a partial trace over DP-Sea modes under the Nexus, which keeps the global state unitary while the local reductions look simple.

## Mechanism 4 — the shutter is a driven DP-Sea boundary (dynamical Casimir)
RGS attribute the creation to broken time-translation invariance (Noether). In CPP that is a time-dependent reconfiguration of the DP-Sea boundary by the shutter — a dynamical-Casimir process. The Nexus preserves global unitarity while permitting local non-conservation in the open, driven subsystem: precisely the bookkeeping RGS invoke.

## Mechanism 5 — the regularization is intrinsic: the 600-cell band top
This is the one place CPP adds content. RGS regularize the instantaneous-shutter divergence with a formal cutoff "arbitrarily high." CPP does not impose a cutoff: QM-5's dispersion $\omega_k = c\sqrt{|\lambda_k|}/\ell_P$ together with the 600-cell's largest adjacency eigenvalue $\lambda_{\max} = z = 12$ gives a hard band top $\omega_{\max} = \sqrt{12}\,c/\ell_P = \sqrt{12}/t_P = 2\sqrt3/t_P$, above which **no modes exist**. The $1/\omega$ tail simply terminates. *Intuition:* the divergence is an artifact of pretending the medium supports arbitrarily high frequencies; a real finite lattice does not, and its top carries the coordination $z=12$ as a fingerprint — distinct from a generic Planck cutoff at $1/t_P$.

## Assembling the result
The logarithmic divergence class is derived from the RGS kernel (Heaviside truncation → $1/\omega$ Fourier tail → $\times\sqrt\omega$ mode normalization → $1/\omega$ spectrum → $\int d\omega/\omega$ = log; TP-1 §Derivation, Lemma). Capping the integral at the band top gives $\langle N\rangle_{\max} = C\ln(\omega_{\max}/\omega_\gamma) \approx 64.5\,C$ for an optical photon — order tens, finite. Two regimes: realistic shutters ($T \gg 1/\omega_\gamma$) self-regularize via the RGS gradual bound and the lattice is dormant ($t_P$ is $\sim28$ orders below the optical period); the lattice caps only the idealized instantaneous limit.

## Failure modes
- If a careful CPP treatment required violating *global* unitarity (not just the open driven subsystem), the QM-4 account — and the compatibility claim — would fail.
- If the band-top density of states reshaped the $1/\omega$ tail before $\omega_{\max}$, the clean $\ln(\omega_{\max}/\omega_\gamma)$ ceiling would be modified (the open edge of **OPEN-TP-1**).
- The $O(1)$ coefficient $C$ is not yet pinned from the lattice (the 600-cell Hilbert–Schmidt mode sum) — **OPEN-TP-1**.
