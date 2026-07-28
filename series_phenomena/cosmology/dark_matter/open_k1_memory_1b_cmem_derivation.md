# OPEN-K1-MEMORY-1B — C_mem DERIVATION: the first order CANCELS (Patch 2838)

**Filed 2026-07-27 against the panel's 1B specification (2837 K4):
derive |F_mem|/|F_inst| ≤ C_mem(v/c) + O(v²/c²), *"or, if the
first-order term cancels by symmetry, at O(v²/c²)"*. **S1 wrote that
escape clause into the requirement. This note argues the escape clause
is the case that obtains.** CONDITIONAL derivation; 1B is NOT declared
closed.**

## §1 — The classical result S1's clause anticipates

For charges coupled to a field propagating at c, **eliminating the
field does not produce an O(v/c) correction to the instantaneous
Coulomb interaction.** In Coulomb gauge the scalar potential is
*exactly* instantaneous; all retardation resides in the vector
potential, which contributes to the inter-charge interaction only at
second order. The reduced (field-eliminated) description is:

| order | term | status |
|---|---|---|
| (v/c)⁰ | instantaneous Coulomb | F_inst |
| **(v/c)¹** | **— absent —** | **cancels** |
| (v/c)² | **Darwin**: (q₁q₂/2c²r)[**v**₁·**v**₂ + (**v**₁·r̂)(**v**₂·r̂)] | leading memory term |
| (v/c)³ | radiation reaction | subleading |

So the projection-induced memory for a field-mediated charge system
begins at **second** order:

> **δ_mem ≡ |F_mem|/|F_inst| ≤ C₂ (v/c)² + O(v³/c³)**, with **C₂ =
> O(1)** — reading the Darwin term against Coulomb, the bracket
> contributes between ½ and 1 in magnitude for the relative-velocity
> geometries, so **C₂ ∈ [0.5, 1] is the natural range**, and C₂ ≤ 2
> is a conservative cover.

**This is not a new result and is not claimed as one.** It is standard
classical electrodynamics, invoked because the panel's own clause
asked whether the leading order cancels by symmetry. **It does, and
the symmetry is gauge structure.**

## §2 — What this buys, quantitatively

| C₂ | δ_mem ≤ 0.15 requires |
|---|---|
| 0.5 | v/c < 0.548 |
| 1.0 | v/c < 0.387 |
| 2.0 | v/c < 0.274 |
| 4.0 (very conservative) | v/c < 0.194 |

Against the superseded first-order reading (v/c < 0.15) and the dead
Compton branch (v/c < 1.4 × 10⁻⁴), **the requirement on the ambient
Sea is now permissive: any Sea slower than roughly a quarter of c
satisfies clause 2 even under a conservative C₂.**

## §3 — The conditional, stated plainly (the worker will not overclaim a third time)

**This derivation is CONDITIONAL on CPP's field structure being
electrodynamic in the relevant sense** — specifically, that the
DI-bit relay reproduces (i) an instantaneous-in-Coulomb-gauge scalar
sector and (ii) a transverse sector entering at second order.

**Evidence FOR:** AUTOMATON established emergent inverse-square
electrostatics under two independent relay implementations
(±2.9%, ±0.4%); C23 identifies the arc configuration AS the magnetic
field; the arc's fore/aft antisymmetry (founder, 2026-07-25) is
structurally the statement that the first-order longitudinal effect
cancels — *he described the cancellation physically before it was
needed here.*

**NOT established:** that CPP's relay reproduces the transverse sector
with the correct weight. Emergent Coulomb tests the SCALAR sector
only. **No committed artifact tests the magnetic/transverse sector
against electrodynamics.** If CPP's transverse structure differs, C₂
changes and could in principle restore an O(v/c) term.

**Therefore: 1B is NOT closed by this note.** What it does is
(a) satisfy the panel's request for the cancellation analysis,
(b) replace an O(v/c) requirement with an O(v²/c²) one *conditional
on a stated premise*, and (c) **identify the exact missing test**:
does the DI-bit relay reproduce the transverse/magnetic sector at the
correct order?

## §4 — What now closes 1B (three items, all smaller than FEM)

1. **Transverse-sector check.** Verify the relay's magnetic response
   against the electrodynamic form — plausibly by the deterministic
   Moment-dynamics route S1 identified (2837 K5 level 2), measuring
   the arc field around a uniformly moving charge on the automaton and
   comparing to the Biot–Savart/Darwin structure. **This is the same
   apparatus that produced emergent Coulomb, extended from the static
   to the moving source** — arguably the single most valuable
   remaining measurement in the programme, since it would also test
   C23 directly.
2. **Fix C₂** from the verified structure (trivial once item 1 holds).
3. **Bound ambient Sea v/c** — unchanged, and now needing only
   v/c ≲ 0.3 rather than ≲ 0.15.

## §5 — Standing

Nothing enacted. **OPEN-K1-MEMORY-1A MET; 1B OPEN**, with its content
now specified to one physical test rather than an open-ended kernel
derivation. PR7 PARTIAL; six of seven; B7 holds.
