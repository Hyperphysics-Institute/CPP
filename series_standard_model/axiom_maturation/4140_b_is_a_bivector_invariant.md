# b Is a Bivector Pseudo-Invariant — the Ruling Derived, and 4139 Withdrawn

**Patch:** 4140. **Lane:** EW. **Session:** 234.
**Answers:** TODO-4139-BCOVARIANT (founder ruling, `founders_voice/4140_…`).
**Withdraws:** Patch 4139's drift computation, and with it 4139's "revision" of Patch 4134.
**Verify:** `series_standard_model/code/4140_b_is_a_bivector_invariant.py`.

---

## 1. The question was a false dichotomy, and the ruling rejects both horns

I asked whether V is the absolute SSV_net or the local-sea-relative one. The founder's answer is
neither: *"The CPs do not measure their motion against the universe or the local frame… the
summation yields a Lorentz-modified local reference-frame velocity… resulting in no absolute-frame
signature."* There is no comparison operation. The summation over the PSR environment **is** the
measurement, and what it produces is already the local-frame velocity.

Per PD-008 that is where the work starts, not where it stops. A ruling that says "no
absolute-frame signature" has to be cashed out as a mechanism that can be checked — and checked
specifically against the A channel, which was the whole of 4139's complaint (SR-1 predates the
amendment and does not mention A_i).

## 2. What 4139 actually did wrong

4139 added the drift **u** to every quark's V and **held A fixed**. That is not a transformation
law; it is half of one. If A and V belong to the same Lorentz object, a boost mixes them.

## 3. The structure is forced, not chosen — and F6 is what forces it

A3′ lists LSP′ = (Φ, V_i, Q_ij) as *"the rotationally protected irreps"* — A ⊕ T₁ ⊕ H = 1+3+5 = 9.
Patch 4113 identified A_i as *"the T₁_g channel the **rotation-only** enumeration omitted."*
T₁_u (V_i, polar) and T₁_g (A_i, axial) are both 3-dimensional under rotations and differ only in
**parity**. In four dimensions that pair is not two vectors — it is the six components of **one
antisymmetric rank-2 tensor**.

Which type? There are two, and **F6 decides**:

| pairing | P of a·b | T of a·b | matches b (P-odd, T-even)? |
|---|---|---|---|
| F_μν type (E polar/T-even, B axial/T-odd) | −1 | −1 | no |
| **M_μν type (K polar/T-odd, J axial/T-odd)** | **−1** | **+1** | **yes** |

F6 — b is T-even, derived from CPT at Patch 4085 for entirely unrelated reasons — selects the
**angular-momentum-type** bivector. V is the boost-like part, A_i the rotation-like part. Nothing
was chosen to make this come out.

## 4. Then b is exactly invariant

A·V is the **pseudoscalar invariant** of that bivector — the exact analogue of E·B for F_μν, which
is famously the one quantity a boost cannot change. Checked over 200 000 random pairs and random
boosts up to β = 0.95: worst relative change **2.1×10⁻¹⁰**, i.e. numerical noise.

Explicitly, at the drift velocity 4139 used:

| | A·V |
|---|---|
| rest frame | −0.2000000000 |
| 4139 (V → V + u, A fixed) | −0.1998770000 — spurious drift +1.23×10⁻⁴ |
| correct boost of the pair | −0.2000000000 (change 2.8×10⁻¹⁷) |

The drift term is the residue of boosting one half of a two-part object. Boost both and it cancels
identically: **u** × A is added to V while **u** × V is subtracted from A, and the two cross terms
in the dot product are equal and opposite.

## 5. Consequences, in order of how much they cost me

1. **4139's drift computation is withdrawn.** There is no absolute-frame residual in b.
2. **A3G-2 is no longer conditionally firing on this route.** The sidereal spin-energy modulation
   the comagnetometer bounds is **identically zero**, not merely suppressed. The 10²³ gap was an
   artifact of my own non-covariant step.
3. **4134 stands as originally written.** My 4139 "revision" of it is itself revised away.
4. **The founder's ruling is derived, not accepted.** The escape is not SR-1 extended by hand: b
   was already the right kind of object, and F6 — from 4085, for unrelated reasons — is what says
   so. That is the third time this session a result has turned on F6, and this time F6 *earns* it.

## 6. What is still owed — the real residual

Everything above holds **if** (V_i, A_i) are two halves of one Lorentz object. **A3′ as written
lists them as separate broadcast components of LSP′, not as one tensor.** If they are independent
channels, each transported on its own, a boost need not mix them, A·V is not invariant, and 4139's
problem returns in full.

So the amendment needs one more thing, and it is **derivable rather than a picture question**:

> **TODO-4140-BIVECTOR** — show that the A3′/AP-4 transport mixes A_i and V_i under a boost as one
> antisymmetric rank-2 object.

Until that is shown, this patch has established what the structure **must** be for the ruling to
hold — not that the amendment implements it. I will not record A3G-2 as passing on the strength of
a structure the axiom text does not yet state.

## 7. PD-008 — the convenient branch, marked

Here the convenient branch was the *agreeable* one: take the ruling, mark A3G-2 passed, close
BCOVARIANT, and move on — the founder had answered and the answer went my way. I have instead
derived the mechanism, which had the pleasant consequence of withdrawing my own 4139 alarm, and
the unpleasant one of exposing a gap in A3′'s text that the alarm had not reached. The next window
should check §3's claim that F6 *forces* the M_μν pairing rather than merely permitting it — that
step is doing the most work here and it is mine, not the founder's.

## 8. Status

A3G-2: **not firing, not yet passing** — conditional on TODO-4140-BIVECTOR. Suite: four of nine
stand (A3G-1 no fire; A3G-3, A3G-7 pass; A3G-9 negative). χ₄ provisionally adopted. **F5 remains
the blocker.**
