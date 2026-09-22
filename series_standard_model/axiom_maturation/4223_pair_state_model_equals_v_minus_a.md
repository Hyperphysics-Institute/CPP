# The Pair-State Inheritance Model Reproduces the V−A Correlations Exactly — and Names What Is Left

**Patch:** 4223. **Lane:** EW. **Session:** 237.
**Works:** the boot card's STEP-2 task, item 2 — *two-GP coherent ejection → singlet → Fermi limit → full
a, A, B*. **Result:** done at the level of the pair's spin state, not yet at the level of the two-GP
mechanism. The ejection rule, the pair's spin state fixed by angular momentum, and c03's amplitude
addition give a, A, B for every λ and every β, equal to the full V−A Dirac amplitude to 10⁻¹⁵.
**Verify:** `series_standard_model/code/4223_pair_state_correlations.py`.
**Amends:** SF-2 §5.7.1 postdiction paragraph (v1.06 → v1.07; PDF recompile owed, founder).
**Status of the claim, PD-008 first:** this is a *reduction*, not a derivation of V−A from the substrate.
Premise (2) below is imported from angular-momentum conservation; it is the thing the two-GP coherent
ejection has to *produce*, and that is now the named, computable target.

---

## 1. Three levels, rows verbatim (D-11)

**Level 1 — the target.** M = [ū_p γ^μ(1 − λγ₅)u_n][ū_e γ_μ(1 − γ₅)v_ν], nucleons at rest with exact Dirac
spinors, |M|² summed over the electron, antineutrino and proton spins, neutron spin +z, fitted to
W = 1 + a β cos θ_eν + A β σ·p̂_e + B σ·p̂_ν. (Its λ sign is opposite to JTW's by the γ₅ convention; the
JTW row is the check.)

**Level 2 — the pair-state inheritance model.** No Dirac algebra, no γ₅. Three ingredients only:
1. **Helicity by the ejection rule (4199/4201):** the electron leaves along −(own spin) with bias β; the
   antineutrino along +(own spin) with bias 1.
2. **The pair's spin state, fixed by angular momentum:** same-sense refill (Fermi) → the pair is a
   **singlet** — nothing leaves the nucleon's spin, and *neither lepton has a spin along the quark axis*;
   opposite-sense refill (GT) → the pair is the **triplet the vector operator σ writes on the neutron**,
   Σ_i (σ_i|n⟩)⊗|T_i⟩, **all three components**, so the channel weight is 3λ², not λ².
3. **The two senses add as amplitudes with ratio λ (c03, 4207)**, and interfere only through the m = 0
   triplet component, which is the one that leaves the proton in the same state as the singlet does.
   W = Tr[ρ_pair (1 − β p̂_e·σ_e)(1 + p̂_ν·σ_ν)].

**Level 3 — 4206's classical model**, for contrast: electron spin = the departed quark's spin, in both
channels; each lepton ejected independently about the quark axis.

```
                                                         a       A       B   (beta = 0.999)
LEVEL 1 V-A, lambda = -1.2754                       -0.107  -0.987  +0.119
LEVEL 1 V-A, lambda = +1.2754                       -0.107  -0.119  +0.987
LEVEL 1 V-A, lambda = -100.0000                     -0.333  -0.673  +0.660
LEVEL 1 V-A, lambda = +0.0000                       +1.000  -0.000  -0.000
JTW formula, lambda = -1.2754                       -0.107  -0.119  +0.987

LEVEL 2 pair-state model (sqrt3 fixed), lambda = -1.2754  -0.107  -0.119  +0.987
LEVEL 2 pair-state model (sqrt3 fixed), lambda = +1.2754  -0.107  -0.987  +0.119
LEVEL 2 pair-state model (sqrt3 fixed), lambda = -100.0000  -0.333  -0.660  +0.673
LEVEL 2 pair-state model (sqrt3 fixed), lambda = +0.0000  +1.000  -0.000  -0.000

LEVEL 3 classical (4206), pure GT, pol 2/3          -0.328  -0.687  +0.735
LEVEL 3 classical (4206), pure Fermi, pol 2/3       +0.325  -0.646  -0.728
LEVEL 3 classical (4206), g=0.83, pol 2/3           -0.216  -0.680  +0.484

LEVEL 2 vs LEVEL 1, max |difference| over (a, A, B), lambda sign matched (the two gamma5/lambda conventions differ by a sign):
   beta = 0.300:  max |L2 - L1| = 1.4e-15
   beta = 0.700:  max |L2 - L1| = 7.8e-16
   beta = 0.999:  max |L2 - L1| = 1.1e-15
```

(Level 3 rows differ from 4206's by the finite-sample scatter of the direction fit; 4206's closed forms
and the 4222 Monte Carlo are the exact ones.)

**The pair-state model equals the full V−A amplitude to machine precision at three β and five λ,
including the Fermi–GT interference, and including the m_e-dependence through β.** The Fermi limit
(a = 1, A = B = 0) is reproduced — the singlet carries no memory of the nucleon spin — and so is the
measured point.

## 2. The one step I got wrong on the way, and what it means physically

My first pair state coupled the triplet to the proton with Clebsch–Gordan coefficients, normalised to a
single J = ½ state. The pure limits came out right and the interference came out wrong (a = +0.174
instead of −0.107, A and B each with the wrong interference sign). The cause: a normalised triplet
weights the GT channel λ² : 1; V−A weights it **3λ² : 1**, because the spin-flip operator is a *vector* and
the pair inherits all three of its components — the reduced matrix element ⟨½‖σ‖½⟩ = √3. **In
inheritance language: the "3" in 1 + 3λ² is the number of directions the opposite-sense refill can flip
into.** With that factor restored the interference is right too, with no further freedom.

## 3. What this settles

- **The 4206 coincidence dissolves.** The model that works does not use the SU(6) d-quark polarisation
  at all. The nucleon spin enters only through how the pair is coupled to it (ingredient 2); Δd enters
  only λ, exactly as in the Standard Model. 4222 §3's finding — that 4206's pure-GT A matched by
  2/3 = 2/3 — is explained: the correct model's pure-GT A is the Clebsch factor, as the SM's is.
- **Ingredient 1 is doing real work.** The electron's bias h = β (4199) is what makes a and A come out
  β-independent in the fit; an h = 1 rule for the electron would scale both by 1/β at low β and fail
  against the m_e-dependence the full amplitude carries.
- **4206 §3 was right about where the failure was and 4207 §3 was right about what it needs.** The
  classical model's single wrong statement is *"the electron carries the quark's spin"* as a definite value
  in both channels. In the same-sense channel the pair leaves as one counter-rotating object with no net
  spin; in the opposite-sense channel it leaves carrying the one unit the nucleon lost.
- **λ's relative sign is now a concrete target.** The measured (A, B) = (−0.119, +0.987) requires the
  same-sense singlet amplitude and the m = 0 opposite-sense amplitude to be **anti-phased**; the in-phase
  choice gives (−0.987, +0.119). This is a *relative* sign, so under 4214's ruling it is derivable in
  principle, and it is what the DP-arc/wake mechanism (4220: unknown) must deliver together with |λ|.
  Filed under TODO-4214-ONESIGN item 4 as the criterion, not as a pass.

## 4. What this does not settle — the named target

Ingredient 2 is imported: "the pair is a singlet when the refill is same-sense, and the σ-written triplet
when it is opposite-sense" is angular-momentum conservation applied to the refill, not a CPP mechanism.
**The two-GP coherent ejection (4207 §3) is exactly the mechanism that has to produce it:** the released
−eCP with its inherited orbital at one GP and the refill's counter-spinning partner at the core's GP must
leave as one event whose *joint* spin state is the singlet or the vector triplet, and not as two
independently spinning leptons. Until that is shown from the 12-edge selection and c03's amplitude sum,
the model is a reduction of V−A to (ejection rule) + (pair spin state) + (c03), with the middle term owed.
Filed as **TODO-4223-PAIRSTATE**, EW lane. It is the next thing to build, and it is smaller than "derive
V−A": it is one two-particle spin-state question about one event.

## 5. PD-008

Convenient branch: calling this "V−A derived." I have not. The pair-state model is V−A's correlation
structure *given* the pair spin state; what CPP adds so far is the ejection rule (helicity) and the
reading of "V" and "A" as same- and opposite-sense refills with a √3 that counts flip directions. The
inconvenient part is that the singlet is not the inheritance picture as the founder stated it in 4205 —
in the Fermi channel the electron does *not* carry the quark's spin as a definite value — and SF-2's
"the inherited orbital carries its spin out unchanged" is true only as a conservation statement, not as a
spin-value statement. The SF-2 sentence is changed accordingly in this patch. Submitted to the next
window for critique with the script.
