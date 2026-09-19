# The W Bracelet on the Same Footing — TODO-4133-F3CALC Step 3 Discharged

**Patch:** 4135. **Lane:** EW/SS. **Session:** 234.
**Closes:** TODO-4133-F3CALC (steps 1–2 at 4134; step 3 here).
**Verify:** `series_standard_model/code/4135_bracelet_same_footing.py`.

---

## 1. Why this had to be run

4133 flagged it and 4134 left it owed: the W bracelet's D₆ ring **is** inversion-symmetric in
position. If "the structure's geometry cancels the pseudoscalar" were the account, it would
cancel for the bracelet too and the weak sector would come out P-even. The argument would prove
too much. Either the two cases are distinguished on one footing, or F3's derivation is worthless.

## 2. The bracelet as the corpus states it

SF-2 Def. `Wbracelet` + Cor. `Wcp`: six vertices, an induced 6-cycle, regular hexagon at uniform
radius r_B = 0.58779, full D₆ symmetry; each vertex hosts two CPs (one eCP, one qCP), twelve in
all, distributed 3×(+eCP), 3×(−eCP), 3×(+qCP), 3×(−qCP), *"with alternating polarities at
consecutive hexagonal vertices."* Modelled as alternating hDP type A (+qCP/−eCP) and type B
(−qCP/+eCP) per the SF-2 glossary — which reproduces that census exactly. The two CPs at a
vertex are treated as coincident; the corpus does not specify their internal separation and no
result here depends on it.

## 3. What the computation found

**D1 — the danger was real.** 6/6 hexagon vertices have their antipode in the ring. Position
symmetry alone *would* cancel here.

**D2 — but the charges do not respect that pairing.** Polarity alternates around a ring of even
length, and 3 is odd, so **antipodal vertices carry opposite charge**. Plain inversion does not
map the bracelet to itself; **inversion × charge conjugation does.** The difference from the
nucleon is in the polarity assignment, not in the ring's shape.

**D3 — V_{i+3} = −V_i exactly**, for any radial law (checked at 1/r², 1/r, linear; out-of-plane
component identically zero, Σ_i V_i = 0 to 3×10⁻¹⁷).

**D4 — the bracelet's own pseudoscalar is not protected by its shape either.** Over all 64
collinear ±1 spin assignments, **10 give W = 0 and 54 do not** (max |W| = 0.865). The
all-parallel assignments give W = 0 for the same action–reaction reason as at 4134. And the
clean statement: **all 8 inversion-even assignments (s_i = s_{i+3}) give W = 0, without
exception** — the inversion × C symmetry of D2 doing its work on the spin sector.

So the bracelet is in the *same* position as the nucleon cage: its own constituents' pseudoscalar
vanishes for the symmetric spin assignments and is unprotected otherwise. **Neither structure's
handedness comes from its shape.**

## 4. What actually distinguishes them — and it is R-F3-ISO itself

The corpus's filter table (maturation §2aa) already says the discriminator is the **state of
motion of the interacting partner**, not the cage:

| interaction | partner | ⟨b⟩ | P |
|---|---|---|---|
| Weak (bracelet) | **free** incoming charge | ≠ 0 | odd |
| Strong (cage hop) | **confined** quark | 0 | even |

4134 supplied the confined half under the amendment: ⟨n·W⟩ = 0 because an L = 0 ground state's
internal frame is isotropically distributed relative to its spin axis. D5 supplies the free half:
a free particle's V = SSV_net is a single persistent direction (founder, 4097), so every CP reads
a definite bit and a polarised beam reads a biased stream, ⟨b⟩ = O(1).

**The sharp form, and it is what makes the two results one result.** R-F3-ISO — *no correlation
between a structure's internal frame and its spin axis* — is not an add-on to F3. It is the
discriminator:

> A nucleon in its ground state **satisfies** R-F3-ISO (s-wave; frame isotropic) → P-even.
> A bracelet in a scattering event **violates it by construction** — its frame is set by the
> incoming particle's momentum direction, which is exactly a frame–momentum correlation → P-odd.

One requirement, two sectors, opposite outcomes, with no separate stipulation for either. That is
the content F3 needed, and it is stronger than the 4101 version in one respect: it does not
require the arc cohort to lie along cage bond directions (R-F3, closed at 4133), only that a
ground state be a ground state.

## 5. What this does NOT establish

**The P-odd half rests on B3.** That the bracelet's *response* is linear in the bit it reads is
B3, and B3's support was audited at 4128 and found to license considerably less than three
recorded results had leaned on it for. This patch does not repair that, and the P-odd half of the
contrast is therefore weaker than the P-even half. Recorded, not deferred: it is already carried
as the B3 concentration warning in the 4130 handover.

**The spin assignment is still not made.** Both 4134 and this patch enumerate over assignments
because the amendment assigns no spin to any CP (founder, 4107). The D4 result is therefore a
statement about *which* assignments are safe, not a demonstration that the actual one is. That is
TODO-4134-SPINORIENT's territory and it is unchanged by this patch.

**The bracelet's coincident-CP model is monopole-level.** A dipole-resolved bracelet could carry
structure the net-charge model does not. Nothing above turns on it, but a claim about the
bracelet's internal pseudoscalar at dipole order would need the separation the corpus has not
specified.

## 6. Status

**TODO-4133-F3CALC CLOSED** — all three steps run. F3 stands on **R-F3-ISO**, which now does
double duty as the strong sector's protection and the weak sector's mechanism. No verdict moved.
χ₄ remains provisionally adopted. **F5 remains the blocker.**
