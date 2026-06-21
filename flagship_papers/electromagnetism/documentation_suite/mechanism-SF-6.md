# Mechanism — SF-6 Electromagnetism Unified (v1.0)

**Paper:** SF-6 v1.0 SHIPPED. Synthesis/reframing of c06, the DP-Sea-Polarization model, SR-1, QM-1..6, and EW-1. NO new derivation.

## Overview
The electromagnetic field is the polarization state of the electron-Dipole-Particle (eDP) sea. One organizational unit — the Zero-point Dipole Chain (ZDC) — realizes both inertial mass (standing pattern, pinned by an unpaired-CP nucleation center) and the photon (traveling pattern, no center). Maxwell EM, special relativity, and QED are three limits of this one mechanism.

## The unifying relation (Tier 1)
`E = ℏν_C`. Standing ZDC: ν_C = mc²/ℏ ⇒ mc² = ℏν_C. Traveling ZDC: ν_C = ν ⇒ hν = ℏν_C. These are substrate-level *identifications* matching the standard Compton/Planck–Einstein relations (not derived from ZDC equations of motion here); the dispersion E²=(mc²)²+(pc)² is imported from SR-1. The content is an *ontological reduction* — mass and light are one substrate object under two boundary conditions — not a novel mathematical derivation.

## The three limits
- **Classical (Maxwell):** macroscopic eDP polarization. E = radial dipole displacement; B = its rotational (curl) component — so E and B are locked and μ0,ε0 share one eDP stiffness; c=1/√(μ0ε0), Z₀=√(μ0/ε0). The *numerical values* of μ0,ε0,c are Tier-2 (toy-model).
- **Relativistic (Tier 2):** the DP-Sea "silly-putty" viscous response gives m_eff(v)→m0γ(v) by tuning parameters; SR-1 supplies the higher-rigor kinematic bridge; the photon null trajectory is the m=0 boundary condition.
- **Quantum (QED):** photoelectric/Compton/double-slit as quantized eDP-polarization interactions. Propagation by constructive DI-bit summation ⇒ delocalization, coherence, Newtonian-limit lensing. Emission = ZDC discharge through Z₀ (LC ringdown ⇒ Δν∝ν³, Einstein A). Absorption = pattern-mode overlap = transition matrix element |⟨f|H'|i⟩|². Second quantization = bosonic occupation of 600-cell modes (QM-5), with intrinsic UV band top ω_max=2√3/t_P (λ_max=z=12; TP-1).

## Two-tier rigor (the load-bearing discipline)
Tier 1 (companion-grade, parameter-free): the E=ℏν_C identification, the standing/traveling-ZDC distinction, the constructive-summation consequences. Tier 2 (toy-model, parameter-tuned): the quantitative μ0,ε0,c,γ(v). The verifier `code/1600_verify_sf6_core.py` asserts only the Tier-1 algebraic inter-constant identities against CODATA; it does NOT assert the Tier-2 constants as derivations.

## What is verifiable
`code/1600_verify_sf6_core.py`: c=1/√(μ0ε0), Z₀=√(μ0/ε0)≈376.730 Ω, h=2πℏ, mc²=ℏν_C — all pass. `code/1602_verify_bandtop.py`: √12=2√3, ln(ω_max/ω_g)≈65.0 (TP-1). Both ran clean for two reviewers (Grok, ChatGPT) as SCRIPT-EXECUTED.
