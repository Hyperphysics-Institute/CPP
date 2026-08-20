# OPEN-GR-FE1-FTERM — RECONCILIATION (RESOLVED, PENDING RATIFICATION)

**Patch 3259 (20 Aug 2026, Session 150). Executed on the founder's
instruction ("I don't know how to reconcile this. Please examine and
see if you can figure out what the problem is"). Verify:
`series_gravitation/code/3259_fterm_reconciliation_verify.py`, 8/8
PASS, all claims exact-symbolic. GR-1c remains UNEDITED (HALT
discipline); the corrigendum text is PROPOSED here for founder/panel
ratification.**

## §1 — The problem (from Patch 3258)

The 3258 derivation found: (i) the measured-frame curved d'Alembertian
does not annihilate GR-1c's own exact vacuum profile
(□_g Δ|SSV| = −a³/(2kr⁵) + O(a⁴)); (ii) GR-1c's stated compensator
𝓕 = [2k(Δ|SSV|)²/(1+kΔ|SSV|)²]·□ln(1+kΔ|SSV|) is O(a⁴) under every
reading — wrong order to compensate. So the shipped Proposition's
formula appeared inconsistent with the shipped paper's own solution.

## §2 — The resolution: the measured-frame potential is the LOG-LAPSE

The equation was written for the wrong potential. Define

    N ≡ ln √(−g_tt/c²) = ln[(1−ϱ)/(1+ϱ)] = −2·artanh(k·Δ|SSV|/2),
    ϱ = k·Δ|SSV|/2.

**Check C1 (exact):** □_g N = 0 identically on the exact isotropic
Schwarzschild background. The log-lapse — the logarithm of the clock
rate — is the potential for which the measured-frame vacuum statics is
EXACTLY the harmonic equation. (The Piecewise branch at a = 2r is the
horizon-coordinate surface, measure zero; the generic branch is the
statement.)

Written for Δ|SSV| directly, the exact quasilinear form follows by the
chain rule, and its compensator is (**Check C2, exact**):

    □_g(Δ|SSV|) + F_true = 0  in vacuum, with
    F_true = [ (k²·Δ|SSV|/2) / (1 − (k·Δ|SSV|/2)²) ] · |∇Δ|SSV||²_g .

Structure: **O(Δ|SSV|) × gradient-squared** — a first-derivative
quadratic, not a second-derivative form.

## §3 — The equivalence theorem: one equation, two frames

The deeper fact, and the full reconciliation with the Patch-3258
lattice-frame T-1:

**Radial, generic potential (Check C3, exact):** for ANY v(r) (not
assumed harmonic), with the measured metric built pointwise from v,

    □_g artanh(k v/2) = [ 32k / ((2−kv)(2+kv)⁵) ] · ∇²_flat v .

The ratio is a pure algebraic factor — NO derivative terms survive.
Hence □_g artanh(kv/2) = 0 ⟺ ∇²_flat v = 0 (wherever kv ≠ 2).

**Full 3D, no spherical assumption (Check C4, exact):** for pointwise
A(u), B(u) and f = artanh(ku/2), the coefficient identity
f″/f′ + d/du ln(√A·B^{1/2}) = 0 holds identically — which is exactly
the condition for every |∇u|² term to cancel in
□_g f(u), leaving □_g f(u) = [f′(u)/B(u)]·∇²_flat u in three
dimensions.

**Therefore: the measured-frame log-lapse equation and the
lattice-frame flat Laplace equation of the Patch-3258 T-1 are THE SAME
EQUATION**, related by an invertible algebraic factor and the potential
substitution N = −2 artanh(k·Δ|SSV|/2). The 3258 "mismatch" was never
between two physics — it was between the true equation and a
mis-transcribed sketch formula. Both static formulations hold exactly,
in full 3D, with sources mapping through the same factor
(weak field: φ′(0) = k/2 and N = −k·Δ|SSV| + O(Δ|SSV|³), Check C5 —
the linearised sector of 3258 is untouched).

## §4 — Localisation of the GR-1c sketch slip (Check C6)

The sketch was CLOSE. The flat radial identity

    □ ln(1+ku) = k·□u/(1+ku) − k²·(∇u)²/(1+ku)²

shows the stated building block □ln(1+kΔ|SSV|) does contain the
required gradient-squared structure (in vacuum, where □u is
higher-order, □ln(1+ku) ≈ −k²(∇u)²/(1+ku)²). The error is the
prefactor: the stated 2k(Δ|SSV|)²/(1+kΔ|SSV|)² carries **one power of
Δ|SSV| too many** (leading order a² vs the required a¹ — Check C6), and
the resummation shape is (1+ku)-based where the exact potential is
artanh-based, i.e. (1−(ku/2)²)-based. No constant rescaling repairs it.
Classification: a proof-sketch transcription defect in a Proposition
that GR-1c itself marked as correspondence-level — precisely the gap
OPEN-GR-FE-1 was chartered to close.

## §5 — Physical reading (worker commentary; mechanism level)

The measured-frame potential being the LOG of the clock rate is
natural in the substrate picture: clock rates compose multiplicatively
(Moments per oscillation multiply along a chain of frames), so the
additive potential of the measured frame is the logarithm; while the
lattice-frame census is additive in Δ|SSV| directly (DI-bit counts
add). One bookkeeping, two natural variables, one equation. The
measured-frame nonlinearity of gravitation, in the static sector, is
entirely the DICTIONARY (the u → metric map), not the lattice
dynamics — which remain linear in the departure field with the PSR
closure carried by c_*(x). The non-static and non-spherical comparison
against full GR (where GR's constraints are genuinely nonlinear)
remains op:einstein territory: the static superposition-in-Δ|SSV|
structure is a distinctive feature of the CPP formulation, FLAGGED for
future falsifier development, not minted (F-3 discipline from 3258
maintained).

## §6 — PROPOSED corrigendum to GR-1c (NOT applied; ratification owed)

Replace the Proposition field_eq statement with (equivalently either
form):

**(Form A — log-lapse):** the self-consistency condition on the LSP
distribution is □_g N = −(4πG/c²)·ρ_mass·[1 + O(weak-field mapping)]
with N = ln√(−g_tt/c²) = −2 artanh(k·Δ|SSV|/2); vacuum: □_g N = 0,
solved exactly by the Theorem-1 isotropic solution.

**(Form B — Δ|SSV| quasilinear):** □_g(Δ|SSV|) + F_true = source, with
F_true as in §2 above.

Plus the equivalence note (§3): both are algebraically equivalent to
the lattice-frame statement ∇²_flat(Δ|SSV|) = normalized source, which
is the form the Patch-3258 census derivation produces. The weak-field
reduction to linearised Einstein (companion 7) is unchanged under
either form. Panel dispatch (CONV series) + founder ratification
required before GR-1c is edited; this document supplies the dispatch's
technical annex.

## §7 — Consequences and ledger

- **OPEN-GR-FE1-FTERM: DIAGNOSED AND RESOLVED — PENDING RATIFICATION**
  (the corrigendum decision is founder/panel property; GR-1c untouched).
- **The T-1 candidate is STRENGTHENED:** its static sector is now
  proven equivalent to the corrected measured-frame equation in full
  3D, not merely solution-matched in spherical symmetry. The 3258
  HALT's substantive content is discharged: the static reduction IS the
  (corrected) GR-1c equation.
- **W-3 (Birkhoff):** on the lattice frame, uniqueness of the
  spherically symmetric vacuum exterior is the classical uniqueness of
  the harmonic 1/r profile — ready to execute once T-1 is accepted.
- **W-4 (T-3 source tensor):** unlocked by the same acceptance; the
  §3 factor fixes the source-side dictionary.
- Verify 8/8; computation-before-claims; no axiom touched; no paper
  touched.
