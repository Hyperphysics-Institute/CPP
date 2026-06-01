# SR-5 Step C — Deriving the Λ Suppression: the residual-gradient mechanism (PARTIAL)

**Arc:** OPEN-SR-5 (Cosmological Sea-gravitation sector) · **Patch:** 0722 (1 June 2026) · **Sub-item:** OPEN-SR-5b
**Verify:** `scripts/0722_lambda_residual_derivation.py` (CHECK 1/2/3 PASS)
**Status:** PARTIAL. Derives the suppression *scaling* + coefficient + ~factor-2 magnitude + resolves the horizon ambiguity in principle, **replacing the c08 inserted (l_P/R_H)² coincidence-restatement** with a substrate mechanism. The precise coefficient, the horizon choice, and the dynamical w(z) are handed to Step D.

## What had to be replaced

The c08 dev-notes estimate ρ_Λ ≈ α_geom·(E_P/l_P³)·(l_P/R_H)² is a **coincidence-restatement**: (l_P/R_H)² ≈ 10⁻¹²² is just the well-known Λ ~ 1/R_H² near-coincidence, swings ~10× on horizon choice, and nothing in it *derives* why the vacuum SSV is suppressed by (l_P/R_H)² (R2 scoping §3). Step C must derive that scaling from CPP.

## The mechanism (from Step B)

CPP gravity couples to the gradient of the SSV **excess** above the Sea ground state, not to absolute energy density. Two consequences chain into the magnitude:

1. **The bulk Sea energy gravitates zero** (Step B) — so the CC catastrophe (ρ_vac ~ ρ_P, ~120 orders too big) never arises. The naive Planck-density vacuum is simply not a gravitating source in CPP.
2. **The only gravitating residual** is the field energy of the largest SSV gradient the Sea cannot cancel. The Sea is discrete (UV scale l_P), finite, and causally bounded (IR scale R_H): it can be gradient-equilibrated only down to the largest causally-connected scale, leaving one uncancelled **horizon-scale mode**.

## The derivation (CPP-grounded; order-1 coefficient aside)

- **Amplitude.** SSV ↔ time-dilation/PSR (SR-1/c05): the natural amplitude of the SSV-potential is Φ ~ c² (the potential ceiling, Φ/c² ~ 1 at a horizon).
- **Coherence scale.** Information advances at c per Absolute Moment, so the largest scale the Sea can gradient-equilibrate in a Hubble time is R_H = c/H. Beyond it, a residual gradient g_res ~ Φ/R_H ~ c²/R_H necessarily remains.
- **Field energy.** The gravitational field-energy density (Newtonian limit, reproduced by c05/c07) is ρ = g²/(8πG). Hence

  ρ_Λ ~ (c²/R_H)² / (8πG) = **c⁴/(8πG R_H²) = c²H²/(8πG)**.

**This makes the scaling a derivation, not a restatement.** Because E_P/l_P = c⁴/G *exactly*, the result is identically

  c⁴/(8πG R_H²) = (1/8π)·(E_P/l_P³)·(l_P/R_H)² = (1/8π)·ρ_P·(l_P/R_H)²   (CHECK 1, exact).

So both the **(l_P/R_H)² scaling** and the **coefficient 1/8π** come *out* of the field energy of the horizon-scale residual gradient — they are not inserted. The horizon is fixed as the **causal-coherence (Hubble) radius** on principled grounds (the scale the Sea can equilibrate in a Hubble time), resolving the c08 ~10× horizon ambiguity in principle.

## Magnitude

ρ_Λ^CPP = c⁴/(8πG R_H²) = **2.56×10⁻¹⁰ J/m³** vs observed **5.3×10⁻¹⁰ J/m³** — a factor **2.07** (CHECK 2). Equivalently Ω_Λ^CPP = 1/3. The 1/8π is exactly what brings the bare ρ_P(l_P/R_H)² ≈ 6×10⁻⁹ down into the observed band. The residual factor ~2 is an order-1 coefficient (exact horizon definition / residual amplitude).

## Prediction and the honest open tension (→ Step D)

- **Prediction:** Λ is **dynamical** (ρ_Λ ∝ H²), not a true constant — a testable departure (evolving w). With ρ_Λ ∝ H² and Friedmann, ρ_Λ tracks ρ_crit, which addresses "why now" (no fine-tuned coincidence).
- **Open tension (Hsu 2004):** the Hubble-radius form gives a *constant* Ω_Λ ≈ 1/3, which conflicts with the observed deceleration→acceleration transition (Λ negligible during matter domination, dominant now). The standard fix uses the **future event horizon** (Li 2004) instead of the Hubble radius, which changes both the dynamics and the "why now" balance. **Which IR scale CPP selects, the precise coefficient, and the correct w(z) require the full Friedmann dynamics — Step D.**

## Honest caps

- PARTIAL derivation: scaling + coefficient (1/8π) + ~factor-2 magnitude + horizon-in-principle are derived; the exact coefficient, the Hubble-vs-event-horizon choice, and w(z) are open (Step D).
- The value-add over holographic dark energy (which posits the IR cutoff via an entropy bound) is the **substrate mechanism**: gradient-sourcing makes the bulk vacuum inert and singles out the horizon residual — a physical reason for the holographic scaling, not a bound assumed.
- Falsifier C1: if the correct CPP IR scale is the event horizon (not the Hubble radius), the clean 1/8π coefficient and the constant-Ω form are modified — the derivation's specific numbers shift (the scaling survives; the coefficient/dynamics do not).
- Depends on the Step-B forward check (does the CPP GR limit exclude ground-state energy from T_μν?) holding; if it fails (falsifier B1), the whole residual picture is moot.
