# TODO-4140-BIVECTOR Pressed — It Does Not Discharge, and the Reason Is Older Than the Amendment

**Patch:** 4141. **Lane:** EW/GR. **Session:** 234.
**Downgrades:** Patch 4140 §3 ("forced, not chosen").
**Verify:** `series_standard_model/code/4141_bivector_partner_absent.py`.

---

## 1. What 4140 claimed, and what the axiom text says

4140 claimed T₁_u (V_i, polar) and T₁_g (A_i, axial) are the six components of one antisymmetric
rank-2 tensor, so b = A·V is its pseudoscalar invariant. I called that **forced**.

`master_glossary`, LSP′ entry, verbatim: *"nine dynamical components — scalar Φ = |SSV|_abs
(icosahedral irrep A, l=0; **g_tt**), vector V_i = SSV_net (T₁, l=1; spatial
curvature/**gravitomagnetism**), and the symmetric-traceless Q_ij (H, l=2; the **radiative
tensor** / gravitational-wave sector) — exactly the lattice's rotationally protected
representation content."*

1 + 3 + 5 = 9 is the **traceless symmetric** rank-2 tensor — the metric perturbation. Φ = g_tt,
V_i = g_ti, Q_ij the radiative tensor. **A component of a symmetric rank-2 tensor cannot also be
half of an antisymmetric one.** V_i is not available as A_i's bivector partner.

**4140's "forced" is withdrawn.** What survives of it: F6 fixes the *parities* any partner must
have (polar, T-odd, so that A·partner is P-odd and T-even). That is real and non-trivial. It does
not supply a partner from LSP′ as written.

## 2. What a genuine partner would have to be

A_i is axial. Its partner must be a polar 3-vector that boosts into it. In the GR sector that
object exists and is standard — the gravito-electromagnetic field tensor, built from Φ and V_i the
way F_μν is built from the EM potentials:

  E^G = −∇Φ − ∂_t V,  B^G = ∇ × V

(E^G, B^G) is a genuine bivector with invariant E^G·B^G. **But then A_i's partner is E^G, not
V_i** — and b would have to be **A·E^G**, not A·V. Those are different quantities: E^G is built
from *derivatives* of the potentials; V_i is the potential itself.

## 3. And this exposes something older than the amendment

The corpus uses **SSV_net in two roles**, and b = A·V does not say which it means:

- **Role 1 — the CP's local displacement instruction.** *"Every CP executes one Displace step per
  its GP's computed SSV_net"* (`master_glossary`, A1′ division of labor). Velocity-like.
- **Role 2 — the l=1 broadcast component V_i = g_ti**, the gravitomagnetic *potential*
  (`master_glossary`, LSP′ entry). Potential-like.

They do not transform the same way. A potential is gauge-dependent, so A·(potential) is not even
gauge-invariant, let alone Lorentz-invariant. A velocity is frame-dependent in the ordinary way and
needs a bivector partner to be protected — which is 4140's argument, requiring role 1.

**The conflation predates the amendment.** It did not matter while nothing contracted V_i with an
axial vector. **b = A·V is the first construction in the corpus that does**, which is why it
surfaces here and not in SR-1 or GR-1.

## 4. Status of what depended on 4140

| | |
|---|---|
| 4140's "F6 forces the M_μν pairing" | **withdrawn as stated** — F6 fixes the partner's parities, not its existence |
| b = A·V is Lorentz-invariant | **unproven, not disproven** — true if a partner exists *and* is what b contracts A with |
| 4139's drift term | **stays withdrawn** — that calculation boosted one half of a two-part object, wrong under either reading |

## 5. PD-008 — the convenient branch, marked

Convenient: leave 4140 standing. It was one patch old, it had resolved a crisis, it agreed with the
founder's ruling, and the founder had already moved on. Nothing external would have caught this.
The inconvenient branch is that my "forced" overreached — F6 constrains the partner's quantum
numbers and I wrote as if it conjured the partner.

**Second time today the same shape of error:** at 4138 I found a *computed table* whose prose
inverted it; here I find *my own* inference stated one modal notch stronger than the argument
carried ("forced" for "required-if-it-exists"). Both are gaps between what was established and what
was written down. TODO-4138-TABLEPROSE was scoped to script tables; on this evidence the underlying
discipline is broader and the next window should consider widening it.

## 6. What is owed

**TODO-4141-SSVROLE** — resolve the two-role use of SSV_net: is the quantity a CP displaces by the
same object as the l=1 broadcast component V_i = g_ti, or a derived one? This is **upstream of the
amendment** — it touches SR-1/GR-1 usage, not just χ₄ — and it decides what b even contracts A
with. Derivable, so mine under PD-008, but it is a corpus-wide terminology ruling and the founder
should see the result.

**TODO-4140-BIVECTOR stays open**, re-scoped: identify A_i's polar partner (candidate: E^G) and
determine whether b contracts A with that partner or with V_i.

## 7. Status

A3G-2 remains **not firing and not passing** — for a sharper reason than yesterday: not "the
transport law is unstated" but "the object b contracts A with is ambiguous between a velocity and a
potential." Suite: four of nine. χ₄ provisionally adopted. **F5 remains the blocker.**
