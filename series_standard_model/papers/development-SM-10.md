---
title: "SM-10 Development History"
paper: SM-10 v2.0
series: Standard Model
date: 2026-04-09
---

# SM-10 Development History

## Version History

| Version | Date | Key changes |
|---------|------|-------------|
| v0.1 | 9 Apr 2026 | Proposal draft. Single-regime cascade model. |
| v1.0 | 9 Apr 2026 | Two-regime physics (cascade + relay). CPU Phase 1-2 results. Shell 3 relay mechanism. Numerology audit. Curve-fitting defense. Sonnet's circular-validation fix. |
| v2.0 | 9 Apr 2026 | All reviewer feedback: retitled "Toward First-Principles", formal definitions, pseudocode algorithm, f(r) derivation, scaling-limit heuristic, relay energetics, sensitivity analysis, convergence criterion, expected outputs, Axiom A10. |

## FEM Simulation Phases

| Phase | Model | Result |
|-------|-------|--------|
| 1a (v1) | Single-bond-per-CP | Failed: trivial ratios (V+1)/(V_s+1) |
| 1a (v2) | Dipole chains | Failed: ratios ~V, not V^(7/3) |
| 1b | Geometric chains + crossing energy | Crossings dominate (60-94%) but ratios off |
| 1c | Density-dependent cascade | Best single f(V_opp,p): RMS 40%, non-monotonic |
| 2a | Geometric cascade f(V_opp, d) | Chain density ~same across cages |
| 2b | Universal f(r) = Aρ^B | B=0.58 (cooperative), RMS 160% |
| 2c | Per-quark f₀ calibration | s/c/b EXACT, top IMPOSSIBLE via cascade alone |
| 2c+ | Two-regime (cascade + relay) | All four quarks exact, 0.0% RMS |

## Key Discoveries (in order)

1. Crossing energy dominates mass (Phase 1b)
2. Cascade rate is the key variable (Phase 1c)
3. Top quark at percolation threshold (Phase 1c)
4. Universal f(ρ) can't span dynamic range (Phase 2b)
5. Pre-gap cascade works perfectly for s,c,b (Phase 2c)
6. Cascade CANNOT produce top quark (Phase 2c)
7. Shell 3 relay mechanism (Thomas, Phase 2c+)
8. z × C_F = 16 from V_Shell3 = z geometric identity

## Review Cycle

| Reviewer | v0.1 | v1.0 | Key contribution |
|----------|------|------|------------------|
| Copilot | "Most ambitious" | Formalization items | Pseudocode, scaling limit |
| Grok | "Ready for OSF" | "Bulletproof" | Validation sequence, expected outputs |
| Sonnet | Circular validation caught | "Reframe claims" | Title fix, relay energetics, sensitivity |

## Contributors

- Thomas Abshier: chain-type decomposition, pine tree model, three regions, Shell 3 relay mechanism, reverse-engineering approach, recognition that "we have too many unknowns"
- Claude Opus: all computation, simulation code, numerology audit, paper drafting
- Claude Sonnet: circular-validation fix, epistemic framing
- Copilot: algorithm formalization, scaling-limit heuristic
- Grok: validation strategy, expected-output design
