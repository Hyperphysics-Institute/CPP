# SCR-2 RESOLVED — EMISSION MULTIPLICITY: φ₂ = 1 EXACTLY (per-CP emission, coherently summed, IS the committed dipole model)

**Patch 3073 (11 Aug 2026). The second of the four frozen counting
questions (3068 §3). Resolved by founder ruling R-EMIT-PERCP
(verbatim in `founders_voice/founder_ruling_percp_emission_invariance_
2026-08-11.md`) run through AP-4's register arithmetic as written.
Verify: `scripts/3073_scr2_emission.py` (2/2 PASS). Anti-extraction:
no band reference anywhere in this derivation.**

## §1 — The frozen question

The 3068 enumeration flagged "per-pair vs per-CP imprinting (both
members emit every Moment under AP-4c's fixed-count clause) — a
possible factor 2 in the quadratic content."

## §2 — The two corpus inputs that decide it

1. **R-EMIT-PERCP (founder, this patch):** every CP, every Moment,
   one DI-bit quantum to its PSR shell — invariant under binding.
   The emitter census per pair is TWO, charges ±q at the two member
   positions.
2. **AP-4's register rule (ratified, 3048-era):** formation is "pure
   vector addition over arrivals with no cross-terms between distinct
   arrivals." The receiver SUMS arrival vectors; quadratic content
   (the deficit) is computed on the summed register state, never
   per-arrival.

## §3 — Resolution

Two opposite-charge per-CP emissions, vector-summed at the receiver,
ARE the dipole: monopole content cancels exactly (net pair charge
zero), and the surviving residual is the dipole term of moment
p = qδ — which is precisely the emitter model the committed stage-2
derivation used (g_d = 2, Patch 3066). Numerically (script): the
orientation-averaged quadratic content of the two-emitter model
matches the committed point-dipole content to 1.0000000 at r ≫ δ,
and g_d = 2.000000 is re-verified from the per-CP model directly.

**φ₂ = 1 exactly.** The founder's ruling does not add a factor; it
CONFIRMS that the committed model was already the per-CP physics,
correctly summed. The "possible factor 2" dissolves: it could only
have arisen from incoherent per-arrival quadratic readout, which
AP-4's register rule forbids — and which would not have been a
factor 2 but the r⁻⁴ monopole catastrophe (×10⁴ at r = 100δ, growing
as (r/δ)²; shown in the script for contrast). The construction's
catastrophe-cancellation and the per-CP emission census are the same
fact viewed from two sides.

## §4 — Boundary declarations

- **To SCR-3 (D-ETA-Z):** the normalization of δ — SEPARATION vs
  per-member excursion (a potential factor 4 in δ², since opposite
  member excursions ξ give δ = 2ξ) — is amplitude normalization and
  belongs ENTIRELY to SCR-3, where the founder's superposition
  picture (3072) and the excursion bound will pin it. Nothing in this
  note touches it; no double-count path exists.
- **To D-COMP-WEIGHT:** R-EMIT-PERCP rules (not assumes) full-strength
  imprint from bound structures; the composition correction's
  suppression lives solely in s(coordination) on the excursion side.

## §5 — Running ledger (no verdict computed, per the freeze)

φ₁ = 0.49 ± 0.01 (closed, 3072) · **φ₂ = 1 (closed, exact)** ·
φ₃ = OPEN (SCR-3 / D-ETA-Z) · φ_comp = OPEN (D-COMP-WEIGHT).
Factors multiply once, at the end.
