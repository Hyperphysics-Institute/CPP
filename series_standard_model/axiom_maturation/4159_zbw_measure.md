# The Isotropy Premise — Justified, but Not by What 4158 Said

**Patch:** 4159. **Lane:** EW. **Session:** 234.
**Discharges:** TODO-4158-ZBWMEASURE.
**Verify:** `series_standard_model/code/4159_zbw_measure.py`.

---

## 1. The χ draft's double rotation does NOT sweep the sphere uniformly

4158 assumed an isotropic ZBW measure and named the χ draft's double rotation as the likely
justification, with a Weyl equidistribution argument as the route. **That route fails, and the
failure is structural, not technical.**

For x(t) = (r₁cos ω₁t, r₁sin ω₁t, r₂cos ω₂t, r₂sin ω₂t) on S³ with incommensurate frequencies, Weyl
does give equidistribution — **on the Clifford torus T(r₁,r₂)**. But a Clifford torus is a single
orbit of *fixed* radii, and under the Hopf map S³ → S² it maps to **one latitude circle** at height
r₁² − r₂². Not the sphere. The naive 3-projection fails too: ⟨cos²θ⟩ comes out 0.500, 0.293, 0.100
at r₁ = 0.5, 0.707, 0.9 against the uniform value 0.333.

**So 4158's stated premise is not supplied by the χ draft.** The Weyl argument I filed as the likely
route would not have worked.

## 2. The corpus's actual geometry is discrete, and I should have used it from the start

A CP does not displace along a continuum of directions. It displaces along **one of twelve
icosahedral edges** (the 12-edge selection rule, c03/GR-1b). û is discrete.

Tested directly, a **fixed** lattice orientation gives a staircase, not β:

| β | A along a vertex | A along a face | target |
|---|---|---|---|
| 0.05 | 0.000 | 0.000 | 0.05 |
| 0.20 | 0.000 | 0.500 | 0.20 |
| 0.50 | 0.833 | 0.500 | 0.50 |
| 0.80 | 0.833 | 1.000 | 0.80 |

The 12-point set is a spherical **5-design**, so it reproduces polynomial averages to degree 5
exactly — but **sign() is not a polynomial**, and it is precisely the discontinuity that a design
does not control.

## 3. What does justify it: orientation-averaging, which is physically compulsory

A real particle's cage has no fixed orientation relative to its motion; a beam's particles have no
common cage orientation. Averaging over lattice orientations as well:

| β | ⟨b⟩ orientation-averaged | error |
|---|---|---|
| 0.05 | 0.0501 | +0.0001 |
| 0.20 | 0.2005 | +0.0005 |
| 0.50 | 0.5001 | +0.0001 |
| 0.80 | 0.7998 | −0.0002 |
| 0.95 | 0.9500 | 0.0000 |

**Exactly β.** And for the same Archimedes reason 4158 used: under a uniformly random rotation each
of the twelve directions has its A-component uniform on [−1,1], so the ensemble average is the
continuum answer **even though no single lattice orientation gives it.**

**So 4158's result stands — on a different and better premise than the one it stated.** The
isotropy is not a property of the ZBW orbit; it is a property of the *ensemble*.

## 4. And it predicts a deviation — the distinctive signature the amendment has lacked

Patch 4155 §4 concluded, uncomfortably, that *"A_i currently has no independent empirical
signature."* **This is one.** For an ensemble whose cages are **aligned**, the staircase of §2
survives and ⟨b⟩ departs from the standard v/c law:

| β | vertex-aligned | face-aligned |
|---|---|---|
| 0.2 | −0.200 | +0.300 |
| 0.5 | +0.333 | 0.000 |
| 0.8 | +0.033 | +0.200 |

**An O(10–40%) deviation. Large, not marginal.** No other account of V−A predicts any dependence of
the polarisation law on lattice orientation, because no other account has a lattice.

**What it requires, and what is not established:** a source of polarised particles emitted from an
**oriented** lattice — a single crystal. Whether any real experiment realises that, whether the
substrate lattice's orientation is even tied to a material crystal's, and whether the emitted
particle retains the emitter's cage orientation, are all **unexamined**. The prediction is only as
good as that chain, and the chain has three unverified links. Filed as **TODO-4159-CRYSTAL**.

## 5. PD-008 — the convenient branch, marked

Two declined. First: quietly substitute orientation-averaging for the Weyl argument and let 4158
read as confirmed — the result is identical and nobody would check which premise carried it. §1 says
plainly that the premise I named does not work. Second: present §4 as *the* missing empirical
signature and stop. It is a candidate with three unverified links, and a large predicted deviation
that requires an unrealised experimental configuration is worth much less than its size suggests.

## 6. Status

TODO-4158-ZBWMEASURE **discharged**: the isotropy premise is justified, by the ensemble rather than
by the orbit. 4158's ⟨b⟩ = (v/c)cos θ stands. **The χ draft's double rotation is NOT the source of
the isotropy** — which does not refute the draft, but removes one thing it was thought to supply.
No verdict moved. χ₄ provisionally adopted. **F5 remains the blocker.**
