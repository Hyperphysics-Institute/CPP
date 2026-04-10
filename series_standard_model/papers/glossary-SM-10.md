---
title: "SM-10 Glossary"
paper: SM-10 v2.0
series: Standard Model
date: 2026-04-09
---

# SM-10 Glossary

**Bonding region** — One of three zones in the chain network: Region 1 (r < 0.2d, dense cross-linking), Region 2 (0.2-0.8d, web mesh), Region 3 (r > 0.8d, surface convergence).

**Calibration target** — The cascade rate f₀ per quark that the GPU simulation must reproduce from first principles. Strange: 0.738, Charm: 0.805, Bottom: 1.000, Top relay: 0.998.

**Cascade amplification** — The factor f(r)/(1-f(r)) by which cross-link DPs multiply at radius r. Diverges as f → 1 (percolation).

**Cascade rate f(r)** — Probability that a cross-link DP's free end finds another chain within one lattice spacing. Parameterised as f₀ exp(-r/λd) + f_surf exp(-(r-d)²/2σ²).

**Chain** — Maximal connected sequence of organised DPs bonded end-to-end: ...⁺DP⁻·⁺DP⁻...

**Chain census** — Count of chains by type (radial, tangential, cross-link), length, and region.

**Convergence criterion** — DP count ratios stable to <1% across 50+ runs and factor-of-10 density change.

**Criss-cross web** — The 60 secondary chains between Shell 3 relay stations and Shell 4 vertices, bonding tangentially.

**Cross-link DP** — A DP bonding two parallel chains at the same radius. Count scales as C(V_opp,2).

**Organised DP** — A DP with both CPs bonded to the chain network (Definition 2.1 in paper).

**Percolation threshold** — The cascade rate f₀ at which the chain network fills the entire confinement volume. Bottom sits at threshold (f₀ ≈ 1.0).

**Relay station** — One of 12 Shell 3 vertices occupied by organised DPs, acting as secondary central CP for the top quark.

**Scaling-limit heuristic** — N_org ~ C(V,2) × ∫ f/(1-f) dr ~ V² × V^(1/3) = V^(7/3).

**Sensitivity analysis** — Scanning ρ_Sea (10²–10⁴), r_bond (0.3–1.0 l_edge), r_therm (1.5–3d).

**Shell 3 gap** — Edgeless distance shell at d ≈ 1.176, V = 12, E = 0. Forces relay mechanism for top quark.

**Synthetic cage** — The DP-chain icosahedral structure at Shell 3, formed by organised DPs occupying lattice vertex positions without lattice edge support.

**Two-regime physics** — Pre-gap quarks use cascade; post-gap (top) uses cascade + relay.
