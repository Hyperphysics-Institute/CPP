# Spin-2 Step 4 — the run at the Einstein wall (current axioms) + the emergent route (Patch 1115)

**Sub-arc:** `series_relativity/op_einstein_closure/spin2_construction/` · **Charter:** `README.md`
· **Verify:** `code/1115_step4_superposition_helicity.py`
**Result:** a run at the Einstein GR wall using *only* the current axioms (scalar `φ` + vector
`SSV_net`), per the architect's request. The superposition of SSV vectors — including the explicit
second-order combination — **cannot** reproduce the linear helicity-±2 radiative sector. But the
**emergent/collective** route is *not* ruled out and is principled: CPP's preferred-frame structure
evades the Weinberg–Witten no-go. This **reframes** the 1114 verdict by adding **option D (emergent
spin-2, no new axiom)** alongside A/B/C. **op:einstein (a) still OPEN; NO VERDICT MOVED.**

## The run (TLA's proposal tested directly)
Transverse SSV plane wave along z, `V = (a cos f, b cos f, 0)`, `f = kz − ωt`. Helicity-±2 lives in
the transverse-plane quadrupole `{h_xx−h_yy, h_xy}` (`code/1115_step4_superposition_helicity.py`):

| route | helicity-2 content | verdict |
|---|---|---|
| (1) linear `h_ij ∼ ∂_(i V_j)` (c07 map) | `0` | no helicity-2 |
| (2) **2nd-order `h_ij ∼ V_i V_j`** (TLA's "change on the change") | `h_xx−h_yy=(a²−b²)cos²f`, `h_xy=ab cos²f` | **structure PRESENT, but `∼amp²` and at frequency `2ω`** |
| (3) gradient-bilinear `h_ij ∼ ∂_iV_k ∂_jV_k` | `0` (pure `T_zz`) | no helicity-2 |

**The architect's intuition is correct in form:** the second-order combination `V_i V_j` *does* carry
helicity-2 structure (the tensor is built from the vector after all). **But the scaling disqualifies it
as the observed GW:** it appears at *second order in amplitude* and at *double the frequency*, whereas
the detected gravitational wave is *first-order in strain at the source frequency*. The wall therefore
stands for **any local polynomial in `(φ, V)`**: the superposition of 3D SSV vectors cannot reproduce
the *linear* Einstein radiative sector. (Consistent with the representation-theoretic fact that a
scalar+vector field carries helicities `{0, 0, ±1}` only.)

## Why the emergent route is open — and principled
A no-new-axiom helicity-2 need not be a local polynomial in the fields; it can be an **emergent
collective mode** of the lattice. The relevant theorem is **Weinberg–Witten**: a theory with a
Lorentz-covariant conserved stress tensor cannot host a massless spin-2 *composite* — which would
forbid building a graviton by superposing lower-spin fields *in a Lorentz-invariant theory*. **CPP
evades this:** it has a preferred frame (the 600-cell lattice + the Absolute Moment), and Lorentz
invariance is *emergent* (SR-1), so there is no fundamental Lorentz-covariant stress tensor to which
Weinberg–Witten applies. CPP therefore sits in the **same class as condensed-matter emergent-gravity
models** (Wen string-nets, Volovik superfluid universe), where an emergent helicity-2 mode *is*
permitted precisely because Lorentz symmetry appears only in the long-wavelength limit.

This makes the architect's "no spin-bit axiom" instinct **defensible on deep grounds**, and it is the
*same pattern CPP uses everywhere*: fermion spin-½ emerges from the ZBW orbit; Lorentz invariance
emerges from the lattice; spin-2 could likewise emerge from the **collective** dynamics of the 600-cell
rather than being a fundamental transmitted bit. The granularity intuition maps onto this directly: the
helicity-2 mode would be a long-wavelength *collective* excitation, invisible in the single-GP variable
count (1114) yet present in the many-body limit.

## The honest caveat (why this is not yet a closure)
Emergent gravitons are **non-generic**. Standard lattice elasticity yields only scalar + vector phonons
— *no* spin-2. Realizing an emergent helicity-2 requires *special* lattice structure; the 600-cell's
**H_g (l=2) representation** is a genuine hint that it *might* (the geometric slot exists, 1112; and the
shell-sum would propagate it, 1113), but this is unproven and such calculations are hard. The **default
expectation from generic lattice dynamics is still "no emergent helicity-2"** — so option D is a
*calculation to attempt*, not a result in hand.

## Reframed verdict (updates 1114)
Closing `op:einstein` (a) within CPP has **four** options, not three:
- **A/B/C (fundamental):** add a rank-2 attribute to a flow (CSR / LSP / GP→CP) — the explicit spin-bit
  axiom.
- **D (emergent, no new axiom):** the helicity-2 mode arises as a *collective* excitation of the
  600-cell lattice. **Permitted** (Weinberg–Witten evaded via emergent Lorentz), **consistent** with
  CPP's emergentist pattern (ZBW spin, emergent SR), but **non-generic** — it requires the 600-cell +
  PCD collective dynamics to produce an *independent* transverse-traceless mode.

**The decision the architect faces is now sharper:** not "axiomatize or abandon," but "attempt the
emergent-graviton calculation (option D) first, and only axiomatize (A/B/C) if it fails." The architect's
instinct (no spin bit) is the option-D bet, and it is principled.

## The concrete open calculation (option D)
Does the long-wavelength effective theory of the 600-cell lattice — built from the scalar+vector GP
d.o.f. with the lattice's nonlinear/many-body couplings — contain a propagating transverse-traceless
mode (an *independent* `Q_ij^TT`, not a bilinear of `V`)? This is the emergent-graviton question. It is
substantial (a lattice-effective-field-theory derivation), genuinely uncertain, but well-posed and the
right next pitch before any axiom is added.
