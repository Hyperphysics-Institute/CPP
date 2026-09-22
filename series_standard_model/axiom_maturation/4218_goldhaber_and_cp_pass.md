# ONESIGN Items 6 and 7: the Goldhaber Helicity and CP Consistency Pass

**Patch:** 4218. **Lane:** EW. **Session:** 236.
**Works:** TODO-4214-ONESIGN items 6 and 7. **No new computation** — both are sign bookkeeping on
the rule already tested at 4199, 4215, 4216, 4217. Six of seven signs pass; item 4 is blocked.

---

## 1. Item 6 — electron capture (Goldhaber 1958): ν_e helicity −1

SF-2's EC walkthrough (v1.06 unchanged here): the bracelet captures the atomic electron's bare
−eCP; **the electron's orbital ZBW, released from its host, propagates as a free spinning eDP = ν_e**
(matter-type: the original orbital, not a reactive induction); the −eCP is transferred to an up
quark core as its linear oscillator.

Under inheritance this is the exact reverse of β⁻: there the escaping −eCP *took* the quark's
orbital DP; here the arriving −eCP *leaves* its orbital DP behind. The shed DP carries label q = −1
(matter-type) and by the ejection rule leaves **against its spin: left-handed, helicity −1.**
Goldhaber measured −1 (via the circular polarisation of the de-excitation γ from ¹⁵²Sm*). **Passes.**

One consistency the walkthrough must also satisfy, and does: with β⁻'s antineutrino being the
*refill's* partner (4201) and EC's neutrino being the *electron's own* orbital, the two are different
objects with different histories — the distinction 4217 §4 flagged as the Majorana question's hinge.
EC is the case where it is sharpest: the ν_e here is not a Sea partner at all.

## 2. Item 7 — CP consistency of the χ₄ polarity clause

χ₄'s polarity clause (4120, forced by CPT): antiparticle = opposite polarity = opposite handedness.
The ejection rule is "leave along q × spin." Charge conjugation flips q and leaves spin alone, so
it flips the ejection direction relative to spin: **the antiparticle has the opposite helicity, by
construction.** Applied to items 1–6: e⁻ left / e⁺ right (4199); μ⁺ left in π⁺ decay ⇒ μ⁻ right in
π⁻ decay (measured); ν̄ right / ν left (4217); the neutral-current drift flips for a positron probe
(4216 §1). All consistent. **Passes**, and it could not have failed independently: the rule's q is
the same q as the polarity clause. The content is that no *second* sign was needed anywhere.

## 3. Status of TODO-4214-ONESIGN

| item | observable | result |
|---|---|---|
| 1 | β⁻ electron vs antineutrino helicity | pass (4199) |
| 2 | π⁺ → μ⁺ν, μ⁺ left-handed | pass, magnitude 0.70 (4215) |
| 3 | atomic PV sign vs W throw | pass, weight = −Q_W (4216) |
| 4 | λ < 0 as refill anti-phase | **blocked** on the persistence picture (4203) |
| 5 | ν only left-handed | pass; Dirac, no 0νββ (4217) |
| 6 | Goldhaber EC helicity | pass |
| 7 | CP / polarity clause | pass |

**No relative sign has failed.** The Dirac / no-0νββ prediction of 4217 is now conditional on item
4 alone; registration in `predictions.md` and SF-4 waits for it, as promised.

## 4. PD-008

No convenient branch. Item 7's pass is structural (one q throughout) and a critic may reasonably
call it a consistency check rather than a test; recorded as such.
