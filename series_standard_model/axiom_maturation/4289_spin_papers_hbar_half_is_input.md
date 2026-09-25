# SPIN-1 and SPIN-2 Take ħ/2 as Input: Solved Backwards It Is "Exact"; Read Forwards the Pair Carries 0.168 × ħ/2

**Patch:** 4289. **Lane:** EW → QM/SPIN. **Session:** 240.
**Verify:** `series_quantum_mechanics/spin_papers/code/4289_spin_L_non_circular.py`.
**Works:** TODO-4286-GMOMENT (C′) (redo SPIN-1 with the founder's lily-pad inner). The first step of the redo showed that
there is no derivation of ħ/2 to redo.
**Touches work prepared for print:** SPIN-1 v2 carries a Zenodo-ready abstract claiming "No free parameters are
introduced". It is not deposited (no DOI, not approved). SPIN-1 and SPIN-2 are **held from deposit** at this patch.

## 1. What SPIN-1 and SPIN-2 claim

- **SPIN-1 (abstract):** L equals ħ/2 exactly "when the orbital radii take the values determined by the Coulomb force
  balance and the standing-wave boundary condition. No free parameter is adjusted to achieve this."
- **SPIN-2:** the ZBW cloud's mode-2 standing wave fixes the *ratio* r_out = 2r_in, from the pair anchoring at the
  antinode r_th/3 and the node 2r_th/3. "The Coulomb force balance and spin quantization condition of Spin I" fix the
  *scale*. "The two papers together constitute a complete derivation of the electron spin quantum number … with no free
  parameters."

## 2. ħ/2 is the input (rows 1)

```
  r_in =    0.33 x (r_th/3) = 2.145e-14 m:  L = 0.0972 hbar/2
  r_in =    1.00 x (r_th/3) = 6.436e-14 m:  L = 0.1684 hbar/2
  r_in =   10.00 x (r_th/3) = 6.436e-13 m:  L = 0.5325 hbar/2
  r_in =   35.27 x (r_th/3) = 2.270e-12 m:  L = 1.0000 hbar/2
  r_in =  100.00 x (r_th/3) = 6.436e-12 m:  L = 1.6839 hbar/2
  L/(hbar/2) = 2(1+sqrt2) sqrt(r_in/a0) -- a continuous family; nothing in the balance selects hbar/2.
  SPIN-1's r_in = a0/(4(1+sqrt2)^2) = 2.2698e-12 m is the solution of L(r_in) = hbar/2: L = 1.000000 hbar/2
```

Coulomb balance allows a circular pair at **every** radius, with L growing as √r_in. SPIN-1's own proof of thm:spin
reads "Set L = ħ/2 … solving yields" r_in. **The spin is the input that fixes the radius.** The verification table's
"exact match to all digits" recomputes that input. SPIN-2 says the same thing in its own words: the scale comes from
"the spin quantization condition of Spin I".

## 3. Read forwards, the pair carries about one-sixth of the spin (rows 2)

The only reading with no free parameter takes **both** radii from SPIN-2's anchoring points and lets Coulomb balance
set the motion:

```
  r_in = r_th/3 = alpha a0/6 = 6.4360e-14 m;  v_in/c = sqrt(6 alpha) = 0.2092
  L = (1+sqrt2) sqrt(alpha/6) hbar = 0.0842 hbar = 0.1684 x hbar/2  (1/5.94 of the electron's spin)
```

**Parameter-free, SPIN-1 + SPIN-2 give L = (1+√2)√(α/6) ħ = 0.084ħ, not ħ/2.**

## 4. The scale connection moves the pair off its anchors (rows 3)

```
  r_in(SPIN-1)/(r_th/3) = 35.27;  there, r = 11.76 r_th and 23.51 r_th -- beyond r_th,
  where SPIN-2's mode-2 wave (defined on 0..r_th, free boundary at r_th) has no node or antinode to anchor to.
```

SPIN-2's anchoring condition is that the CPs *sit at* the antinode and the node. Moving the pair 35 times outward takes
it past the free boundary of the wave that defined those points. r_out = 2r_in is carried to a scale where its reason
does not apply. The spin-arc development notes (SPIN-3 development, l. 491) called the 35.27 "not a problem — it is a
result". It is the gap.

## 5. D-10: earlier windows asserted the opposite

- GR-1c development notes (l. 1388): an earlier window "expected it to require a free parameter … It didn't."
- Spin-arc notes (l. 491, 505, 526): the scale mismatch "is not a problem; it is a result".

Neither tested the forward reading of §3. No correction was on file before this patch (unscoped search for
SPIN-1/Spin I/c20 with circular, tautolog, free parameter, input, imposed or assumed).

## 6. Downstream (D-6)

- **4090 (EW, TODO-4090-EW):** "CONSTRAINT MET: SPIN-1 already contains a derived detuned pair … 2√2 'not assumed'."
  2√2 follows from r_out = 2r_in, which (§4) has no anchoring basis at the orbital scale. **4090's constraint reverts to
  unmet by owned structure.** 4090 itself concluded that the ratio "does no work" and "predicts nothing", so no number
  moves.
- **4286–4288:** they used SPIN-1 only as the comparison carrier. g = 3 − 2√2 is SPIN-1's moment on SPIN-1's premises and
  stands as a statement about that model. The general formula (4288) does not depend on SPIN-1.
- **phenomena-SM-1, FAQ, SR companions:** any "spin ħ/2 derived with no free parameter" citation inherits §2. Filed as a
  sweep (TODO-4289-SPINSWEEP).

## 7. What this does to (C′)

There is no derivation of ħ/2 to transfer into the founder's lily-pad picture. **The electron's spin is presently
input, not output, everywhere in the corpus.** On the founder's picture (4287, 4288), the outer −eCP carries all of it
and the lily-pad inner none. What must be derived is why the outer CP's action is ħ/2. His 4288 intuition ("the Planck
constant amount of angular momentum is what the CPs carry") is the natural place to start. Put in physical terms: a
tangential motion on the lattice cannot carry less than a minimum action, and the electron's circulation carries exactly
the minimum. Whether that minimum is ħ/2 rather than ħ is the question, and whole-ħ amounts cannot make ħ/2 (4288 row 3).

## 8. PD-008

- **Convenient branch refused.** The convenient course was to take SPIN-1's ħ/2 as derived and graft the lily-pad onto it,
  leaving the published-ready claim intact. Both papers are held instead.
- **What is not claimed.** That SPIN-2's standing wave is wrong, or that r_out = 2r_in is false. It is exact *at the
  anchoring radii*. The finding is that the two papers use it at one scale and fix the radius at another, and that the
  radius-fixing step is the spin itself.
- **Founder's physics not needed for this step.** It is logic plus one computation. The next physics question (§7, what
  sets the minimum action of a circulation) will need his picture.
