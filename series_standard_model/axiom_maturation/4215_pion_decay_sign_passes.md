# ONESIGN Item 2: Pion Decay — the Sign Passes, and the Rule's β-Dependence Is Close to Right

**Patch:** 4215. **Lane:** EW. **Session:** 236.
**Verify:** `series_standard_model/code/4215_pion_decay_helicity_test.py`.
**Works:** TODO-4214-ONESIGN item 2. **Corrects:** that item's wording ("μ⁺ right-handed" was
wrong; the μ⁺ is *left*-handed, and that is the whole point of the test).

---

## 1. The test

π⁺ has spin 0 and decays to two bodies, so μ⁺ and ν_μ leave back to back with spins that cancel.
The ν_μ carries label q = −1 and is ejected against its spin: left-handed. Spin cancellation then
**forces the μ⁺ to be left-handed as well** — the "wrong" helicity for an antiparticle. The ejection
rule allows the wrong helicity only with probability (1 − β)/2, so the decay is suppressed, most for
the lightest lepton. This is the famous helicity suppression of π → eν.

## 2. Rows verbatim (D-11)

```
mu+: p = 29.79 MeV, beta = 0.271, P(wrong helicity) = (1-beta)/2 = 0.364
e+ : p = 69.78 MeV, beta = 0.999973, P(wrong helicity) = 1.34e-05

Gamma(pi->e nu)/Gamma(pi->mu nu):  model 8.62e-05   SM tree 1.28e-04   measured 1.230e-4
model/measured = 0.70

SIGN: mu+ left-handed (wrong for an antiparticle), forced by the left-handed neutrino: model agrees.
MAGNITUDE: the rule's (1-beta) versus the SM's m^2 -- same order, off by ~1.4 in the e/mu ratio.
```

## 3. Verdict

- **Sign: passes.** One primitive (the ν is left-handed) plus spin conservation gives the μ⁺ its
  measured wrong-way helicity. No freedom.
- **Magnitude: near, not exact.** The rule's suppression is (1 − β) ∝ m²/(E + p)²; the SM's is m².
  They agree in order and differ by a kinematic factor, giving an e/μ ratio 0.70 of measured. **The
  bias form h = β is the thing tested here** — a rule that ejected with full bias (h = 1) would forbid
  the decay entirely, and a rule with h independent of β would give no suppression. The measured
  1.23 × 10⁻⁴ says h = β is close, and the residual factor is a question about the rule's exact
  form, not its sign.

## 4. PD-008

No convenient branch. Attack: the (1 − β)/2 is the *classical* wrong-helicity probability for a
1 + β cos distribution; the SM amplitude carries m/E, whose square is (1 − β²), not (1 − β) — a
critic should decide which the rule actually implies before treating the 0.70 as a discrepancy.
