---
title: "SM-10 Mechanism Summary"
paper: SM-10 v2.0
series: Standard Model
date: 2026-04-09
---

# How SM-10 Works

## The Question
SM-8 gives the formula M = m_e(z/φ)V^(7/3). SM-9 partially derives the exponent. SM-10 asks: WHY does this formula work? What physical mechanism produces V^(7/3) scaling?

## Two-Regime Answer

### Regime 1: Intra-cage cascade (s, c, b)
The central CP radiates chains to opposite-polarity cage vertices. At each radius, pairs of chains generate cross-links. Each cross-link DP's free ends seek new partners, creating a cascade. The cascade rate f(r) decays exponentially from center (chain density drops as 1/r²) with surface enhancement near the cage boundary.

The scaling emerges from: C(V_opp,2) pairs × ∫ cascade amplification dr ≈ V² × V^(1/3) = V^(7/3).

### Regime 2: Shell 3 relay (top quark)
The cascade alone produces only ~2,100 MeV for the top quark. DPs dissociate to occupy Shell 3's 12 edgeless vertices, forming a synthetic icosahedral relay cage. Each of the 12 relay stations radiates to ~5 Shell 4 vertices, creating 60 secondary criss-crossing chains. The relay web's cascade fills the Shell 3-4 gap, contributing 99% of the top quark's mass.

Enhancement: V_Shell3 × C_F = 12 × 4/3 = 16.

## Key Mechanism: Percolation
The mass hierarchy maps to distance from the percolation threshold. Strange (f₀=0.74) is sub-critical with isolated chains. Bottom (f₀=1.00) is at the threshold. Top requires the relay mechanism to exceed what cascade alone can produce.

## Calibration vs Derivation
The current model calibrates f₀ per quark (4 params, 4 data). The GPU simulation (Phase 3) will test whether f₀ emerges from DP-level dynamics, converting calibration to derivation.
