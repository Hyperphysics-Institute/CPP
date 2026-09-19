# Calibrating the Founder's GP-Summation Picture — b Needs No New Channel

**Patch:** 4109. **Lane:** EW. **Discharges:** TODO-4101-F3 / the 4108 sharpened question.
**Founder verbatim:** `founders_voice/4109_ruling_gp_summation_and_the_4d_element.md`.
**Verify:** `series_standard_model/code/4109_lsp_pseudoscalar_verify.py` (ALL CHECKS PASS).

---

## 1. The question I posed was a false dichotomy

Patch 4108 asked: is b written per ARC, or for the cohort's VECTOR SUM? The founder's answer
is **neither**. The bit is declared **per CP, per Moment, to its own GP**; the **summation
happens at the receiving GP** over its PSR shell.

That is not a new mechanism — it is **A3′ and AP-4 as already ratified**: at every Absolute
Moment each GP broadcasts to its PSR shell the packet LSP′ = (x_GP, t_abs; Φ, V_i, Q_ij), and
receiving GPs sum what arrives. The founder's picture *is* the corpus mechanism.

## 2. The thing he flagged — and the calibration result

He named "the CP carrying the 4D element/Helicity bit" as *"a new concept that has never been
used,"* declined to assert it, and asked that it be checked against the corpus.

**Checked. It does not need to be new.**

b is a **pseudoscalar**: rotation-invariant and P-odd. A3′ calls LSP′ "the complete set of
rotationally protected irreps." Searching the invariants buildable from its content:

| invariant | rotation-invariant | parity |
|---|---|---|
| Φ, V·V, tr Q, V·QV, det Q | yes | **EVEN** |
| **det[V, QV, Q²V]** | yes | **ODD** |

**A pseudoscalar already exists inside LSP′.** Three vectors — V, QV, Q²V — are all built from
the packet's own V and Q; their determinant is a rotational invariant, and it is P-odd because
the polar V enters an odd number of times (three). Verified: generically nonzero (mean 3.59,
zero in 0/5000 draws) and sign-flipping under P in **5000/5000** draws.

> **A3′ does not need amending. χ₄'s carrier is a composite of irreps the GP already
> broadcasts, not a new primitive.**

This materially lowers χ₄'s cost. The axiom had been carrying an implied axiom-level amendment
nobody had priced.

## 3. An unexpected result: F2 falls out for free

det[V, QV, Q²V] vanishes **identically** when Q is isotropic (Q ∝ I), because then QV ∥ V and
the three vectors are degenerate. Verified: max |b| = 3.5×10⁻³⁰ over 5000 isotropic draws.

> **An unperturbed, isotropic DP sea carries no pseudoscalar at all.**

So EM stays P-even **automatically** — F2 by a second route, **independent of DP-CAL-1 and of
any assumption about DP spins.** The calibration you supplied at 4107 is no longer load-bearing
for F2; it is corroborated by a mechanism that needed no calibration.

Meanwhile det[V, QV, Q²V] is nonzero in 5000/5000 anisotropic draws — so a **quadrupole-distorted**
region (a cage, a W bracelet) *can* carry a handedness. The pseudoscalar is absent exactly where
parity must hold and available exactly where the weak sector needs it. That division is
structural, not tuned.

## 4. Honest limits

1. **This is a candidate identification, not a derivation.** I have shown LSP′ *can* carry a
   pseudoscalar and that it has the right vanishing behaviour. I have **not** shown that CPP's
   b *is* this determinant. Pinning that requires deriving b's normalisation and sign
   convention from the broadcast dynamics.
2. **Adjacency to Patch 4071 needs checking.** 4071 found a CP needs ≥4 independent internal
   *directions* to carry any pseudoscalar (k = 1,2,3 identically zero). Q is a rank-2 object,
   not a direction vector, so the constructions differ — but the two results sit close enough
   together that the relationship should be established rather than assumed. Filed as
   **TODO-4109-4071**.
3. F3 is **not** discharged here. The cancellation for a confined quark still needs the
   per-Moment average of its own b to vanish; this patch changes where b comes from, not that
   requirement.

## 5. Status

No verdict moved. **F5 remains χ₄'s blocker** (missing mechanism, Patch 4103). But χ₄'s cost
is now lower than believed: no axiom amendment, and F2 secured twice over.
