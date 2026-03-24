# OP-SS-7: $\Lambda_\text{QCD}$ from PSR Saturation

**Priority:** MEDIUM  
**Status:** OPEN — mechanism identified  
**Series:** SS\#4; unified v2 Remark 6.1  
**Last updated:** 23 March 2026

---

## Statement

Derive $\Lambda_\text{QCD} \approx 0.218$~GeV from the CPP PSR
(Phase Space Restriction) saturation condition, without using the
PDG value as input.

---

## What is Known

**The PSR mechanism (Grok v1, unified v2 Remark 6.1):**
At short distances ($r \lesssim l_P$), the effective PSR approaches
its minimum value $\text{PSR}_\text{eff} \to l_P/2$.  In this limit,
the DP Sea cannot nucleate new qDP chains fast enough to self-collimate,
so the effective string tension vanishes and $\alpha_s \to 0$.  This
is the CPP physical mechanism for asymptotic freedom.

**The dimensional estimate:**
$$\Lambda_\text{QCD} \sim \sqrt{\frac{\sigma}{\alpha_s}}
\approx \sqrt{\frac{0.9}{0.118}}\ \text{GeV} \approx 2.8\ \text{GeV}$$

This is factor-of-13 above the PDG value (0.218~GeV).  The estimate
uses the string tension $\sigma$ at the scale where it is calibrated,
not at the confinement scale.  A proper derivation uses the running
coupling and the self-consistent confinement scale.

**The self-consistent relation:**
$$\Lambda_\text{QCD} = r_\text{conf}^{-1} \cdot e^{-1/(2\beta_0 \alpha_s(r_\text{conf}))}$$

which requires $r_\text{conf}$ from OP-SS-5 and $\beta_0 = 7$ from
SS\#4.

---

## What Remains

- Formalise the PSR saturation condition into a precise equation for
  $r_\text{conf}$ (or equivalently $\Lambda_\text{QCD}$).
- Verify that the PSR condition $\text{PSR}_\text{eff} \to l_P/2$
  gives $r_\text{conf} \approx 0.161$~fm self-consistently.

**Prerequisite:** OP-SS-5 (derive $r_\text{conf}$ from sea\_strength).

---

## Feeds Into

- Closes the last free parameter in the strong sector
- OP-G-2 (full SM from 600-cell — $\Lambda_\text{QCD}$ without PDG input)
