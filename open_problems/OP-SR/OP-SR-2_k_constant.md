# OP-SR-2: Derive $k$ from 600-Cell Voronoi Integral

**Priority:** HIGH — blocks all quantitative SR predictions  
**Status:** OPEN — two inconsistent estimates; integral "in preparation"  
**Series:** SR main paper (V16); Stiffness C companion  
**Last updated:** 23 March 2026

## Statement

Derive a single, consistent, geometrically-motivated value for $k$
— the SSV coupling constant in PSR_eff = l_P / (1 + k·ΔSSV) — from
the 600-cell Voronoi cell structure.

## The Inconsistency

Two estimates appear in the SR paper sessions:

| Estimate | Source | Value | Units |
|---|---|---|---|
| (i) | l_P^4 / E_P from lattice packing | ~3×10⁻¹⁴⁹ | m⁴/J |
| (ii) | Planck saturation condition | ~2.16×10⁻¹¹⁴ | m³/J |

These differ by 35 orders of magnitude and have different units.
One has m⁴/J, the other m³/J. The paper cannot proceed to
quantitative predictions until these are reconciled.

## Resolution Path

The correct $k$ requires:
1. Fixing the units of SSV (see OP-SR-3 — SSV must be defined)
2. Evaluating the Voronoi integral from OP-SR-1
3. Showing that the Planck saturation condition
   k·ΔSSV_max = 1 (PSR → 0 at Planck energy) gives a consistent value

## Consequence

With $k$ known: the three SR predictions (time dilation, length
contraction, E-p relation) become quantitatively testable at
specific energy scales.

## Prerequisite
- OP-SR-1 (PSR formula — needed for the correct form of $k$)
- OP-SR-3 (SSV units — needed for dimensional consistency)

## Feeds Into
- All quantitative SR/GR predictions
