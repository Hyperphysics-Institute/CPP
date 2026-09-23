# Critic on 4215: the Rule Implies (1 − β), and With the States' Normalisation the π → eν/μν Ratio Is the SM's Exactly

**Patch:** 4249. **Lane:** EW. **Session:** 238. **Closes:** TODO-4222-CRITIC item (iii) (4215's open question).
**Verify:** `series_standard_model/code/4249_pion_ratio_normalisation.py`.

## 1. Rows verbatim (D-11)

```
mu : p= 29.792 E= 109.778 beta=0.271385  (1-beta)/2=3.6431e-01 = m^2/(2E(E+p))=3.6431e-01   E+p=139.570 (= m_pi)
e  : p= 69.784 E=  69.786 beta=0.999973  (1-beta)/2=1.3405e-05 = m^2/(2E(E+p))=1.3405e-05   E+p=139.570 (= m_pi)

4215 form  p*(1-beta)/2:               e/mu = 8.6186e-05   /SM tree = 0.672
with 2E_l 2E_nu normalisation:         e/mu = 1.2834e-04   /SM tree = 1.000000   (SM tree 1.2834e-04; measured 1.230e-4)
(1-beta^2) alternative, same normalisation: e/mu = 4.7288e-04  -> 3.685 x SM: excluded

-> the rule implies (1-beta); the SM's m^2 IS (1-beta)/2 x 2E_l x 2E_nu; the 0.70 of 4215 was the omitted normalisation, not a discrepancy.
```

## 2. Verdict

**(1 − β).** The ejection rule's wrong-helicity probability (1 − β)/2 = (E − p)/2E = m²/(2E(E + p)) is exactly the squared
overlap of a helicity state with the opposite chirality; (1 − β²) = m²/E² is not what the rule gives and, with the same
normalisation, would put the e/μ ratio at 3.7× the SM — excluded. 4215's factor 0.70 was not a discrepancy in the rule:
it multiplied a per-particle probability by the phase-space momentum p alone, while a rate carries the two outgoing
states' normalisation 2E_l · 2E_ν as well. With that restored, and because E_l + p_l = m_π in the two-body decay, the
model's e/μ ratio equals the SM tree ratio identically (1.000000), i.e. the SM's m² helicity suppression *is*
(1 − β)/2 × 2E_l × 2E_ν. **ONESIGN item 2 now passes in magnitude as well as sign.** The measured 1.230×10⁻⁴ vs tree
1.283×10⁻⁴ is the known radiative correction, not the rule's.

## 3. PD-008

Convenient: none — the result closes a question in the rule's favour, and the step that closes it (2E normalisation)
is standard, not a CPP choice. Attack for the next critic: whether the CPP displacement rule *supplies* the 2E factors
as a statement about the substrate (a rate per Moment per outgoing state) or only inherits them from the SM's field
normalisation; 4215 and this patch use the latter.
