# Reasoning capture — Patch 0739: the Δc / LPI filter (Brick #4 cheap falsifier)

*SR-1 rederivation pass, Session 154. The cheap falsifier flagged in 0738. Filter + verify:
`series_phenomena/cosmology/early_universe/scripts/0739_delta_c_filter.py`. Writeup:
`series_relativity/development/delta_c_lpi_filter.md`. NO THEO.*

## The one insight that turned a kill-shot into a fork

Naively, a density-dependent c_eff that differs galaxy-to-void looks instantly dead: varying c should
violate the tight bounds on constant-variation. The insight that rescues it: **only DIMENSIONLESS
variation is observable/bounded.** A position-dependent c absorbed into the metric is just gravity —
and CPP's c07 already reproduces gravitational time dilation, which IS a position-dependent rate. The
data bound α = e²/(4πε₀ℏc), not c alone.

In CPP the DP Sea is the EM medium, so c = 1/√(με) (product) and α ∝ √(μ/ε) (ratio/impedance). With
fractional SSV responses d_μ, d_ε:
  Δc/c = −½(d_μ+d_ε),  Δα/α = +½(d_μ−d_ε),  so Δα/α = −A·Δc/c, A=(d_μ−d_ε)/(d_μ+d_ε).
The LPI coupling k_α = A. ONE structural number decides everything.

## Bounds (searched 2026, used as inputs)

- spatial α dipole few×10⁻⁶ over Gpc (Webb/King/Murphy, ~4σ, debated);
- α vs Φ from white dwarf G191-B2B (Berengut–Flambaum–Webb–Barrow 2013): Δα/α=(4.2±1.6)×10⁻⁵ at
  ΔΦ≈5×10⁻⁵ ⇒ k_α≈0.8±0.3 (weak, |k_α|≲1);
- atomic-clock LPI |k_α|≲10⁻⁶ (the tight bound).

## Result

- A=0 (symmetric μ,ε response): Δα/α=0, c-variation is pure metric=gravity=c07. SAFE.
- A≲10⁻⁶: within clock LPI. PASS.
- A~O(1): k_α~1 → falsified by ~6 orders. FAIL.

So Branch V survives iff the DP-Sea SSV response is μ↔ε symmetric to ~1e-6.

## The partial answer that retires half the worry

The GRAVITATIONAL channel is ALREADY known near-symmetric: c07 matches gravitational time dilation
while LPI holds to k_α≲10⁻⁶, so A_grav≲10⁻⁶ is observationally forced. Hence the only open piece is
the COMPOSITION (qDP-density) channel — does density move μ,ε the same symmetric way potential does?
This is decidable from the four-DP-species structure and how SSV polarizes them.

## Honesty / scope

- Order-of-magnitude structural filter, not a precision calc. Numbers are decades, not digits.
- I did NOT claim a pass; I claimed "not falsified, reduced to a decidable symmetry question." The
  fail mode is real and 6 orders wide if the composition response is generically asymmetric.
- This is GOOD for c07: it implies the gravity-SSV response is the symmetric mode, a consistency
  check the rederivation can lean on.
- NO THEO (bound check). No new prediction/term/axiom. Verify script bundled. Clear of chirality.

## Pointer
- Next first-principles targets, both now sharply posed: (1) DP-Sea μ↔ε symmetry of the
  SSV/composition response (this filter's residual); (2) superposition-thinning roll-off law (0738).
  When both resolve, fold semantics into SR-1 and dispatch to the review panel.
