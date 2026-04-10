---
title: "SM-10 Frequently Asked Questions"
paper: SM-10 v2.0
date: 2026-04-09
---

# FAQ — SM-10: Toward First-Principles Quark Mass from FEM Chain Network Simulation

## Category A: The Simulation

**Q: Can the simulation really derive quark masses?**
A: If the GPU simulation produces the correct PDG mass ratios (N_c/N_s = 13.6, N_b/N_s = 44.8, N_t/N_s = 1850) from DP-level dynamics without imposing any scaling law, then yes — V^(7/3) would be derived, not assumed. This is the definition of Level A success.

**Q: What if it fails?**
A: That's Level C (informative failure). It would reveal which physical assumptions are incorrect — the cascade model, the bonding rules, the Sea density, or the relay mechanism. Failures are as valuable as successes because they constrain the correct physics.

**Q: Why use a simulation instead of an analytical derivation?**
A: The chain network is too complex for closed-form analysis. The three bonding regions, cross-linking cascade, and relay mechanism involve N-body interactions that require numerical computation. The simulation is to SM-10 what the Schrödinger equation is to Bohr: it derives the answer from dynamics rather than guessing the formula.

## Category B: The Curve-Fitting Objection

**Q: Isn't this just curve fitting? You have 4 parameters for 4 data points.**
A: The current CPU model (Phase 1-2) is honestly labelled as calibration, not derivation. The 0.0% agreement is tautological with 4 fitted f₀ values. However: (1) The model STRUCTURE (cascade + relay) comes from physics, not fitting. (2) The f₀ values are calibration TARGETS for the GPU. (3) The V^(7/3) formula (SM-8/9) already has 0 parameters and 2.1% RMS — that's the primary result. The FEM adds mechanism, not precision.

**Q: What would convert this from calibration to derivation?**
A: Test A: GPU produces f₀ values from DP dynamics alone. Test B: Model predicts a 5th observable (light quark masses, coupling constants). Test C: GPU reproduces the three-region mass breakdown from emergent dynamics. Any one of these suffices.

**Q: How is this different from fitting a polynomial?**
A: A polynomial has arbitrary coefficients. The cascade model has physically constrained structure: radial chains exist because the central CP attracts cage vertices; cross-links exist because chains pass near each other; the cascade exists because cross-link DPs have free ends that bond. The model's form is dictated by the physics before any fitting occurs.

## Category C: The Shell 3 Relay

**Q: Why do DPs occupy Shell 3 positions?**
A: Shell 3's 12 vertex positions are lattice-determined — they exist in the 600-cell geometry. The central CP's field creates potential minima at these positions. Sea DPs gain energy M₀ by bonding to the radial chains, which exceeds the entropy cost of leaving the disordered Sea. Occupation is energetically favourable.

**Q: Why is the relay needed — why can't the cascade alone produce the top quark?**
A: The CPU simulation (Phase 2c) proved this quantitatively: even with the cascade rate at maximum (f → 1, full percolation), the icosidodecahedral cage can only organise ~360 DPs, producing 1,364 MeV. The PDG value is 172,760 MeV — 127× larger. A qualitatively different mechanism (the relay) is required.

**Q: How does the relay produce ×16?**
A: 12 relay stations at Shell 3 vertices (V_Shell3 = 12 = z from icosahedral symmetry). Each relay bond carries C_F = 4/3 (independently derived in SS-2). Product: z × C_F = 12 × 4/3 = 16. This is a geometric derivation, not algebra.

**Q: Why doesn't the relay create a ×16² quark at Shell 5?**
A: Shell 5 is also edgeless with V = 12. But the three-generation theorem (SM-8 Theorem 8.1) identifies Shell 5 with the neighbouring cell's Shell 3. The relay at Shell 5 IS the relay of the adjacent cell — it doesn't create a new particle.

## Category D: The Percolation Interpretation

**Q: What does percolation have to do with quark mass?**
A: The cascade rate f₀ controls how deeply the cross-linking cascade penetrates. At f₀ < 1 (strange, charm), chains are isolated — low mass. At f₀ ≈ 1 (bottom), the cascade fills the volume — the percolation threshold. Beyond this, the relay mechanism is needed. The mass hierarchy maps directly to distance from the percolation threshold.

**Q: Is the percolation threshold special?**
A: Yes. Bottom sits exactly at f₀ ≈ 1.0, meaning its cascade fills the entire cage volume. This is why the bottom quark has the largest mass achievable by cascade alone. The top quark exceeds this limit, requiring the relay.

## Category E: Next Steps

**Q: When will the GPU simulation run?**
A: Phase 3 requires GPU infrastructure (CUDA or JAX). Target: 1-2 weeks after setup. Isak Gutierrez will provide GPU infrastructure; Claude Code will implement the simulation kernel.

**Q: What are the calibration targets?**
A: f₀(Strange) = 0.738, f₀(Charm) = 0.805, f₀(Bottom) = 1.000, f₀_relay(Top) = 0.998. If the GPU produces these from local DP dynamics, the quark masses are derived from first principles.

**Q: What about light quark masses (u, d)?**
A: The up quark uses a blanket model (no cage), the down quark uses a cage + captured eCP. These are natural extensions of the FEM but require additional model development beyond SM-10's scope.

---

*FAQ prepared by Thomas Lee Abshier ND and Claude Opus (Anthropic), 9 April 2026.*
