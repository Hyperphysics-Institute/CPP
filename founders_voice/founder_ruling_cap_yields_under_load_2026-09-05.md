# Founder ruling — a saturated register yields under load (5 Sep 2026, Session 162)

**Status:** verbatim founder text, registered Patch 3638 as **R-CAP-YIELDS-UNDER-LOAD**. It answers 3637 §3's one-line question and REVERSES the reading 3637 was written under (the cap as a rigid saturation floor).

Opus asked (3637): *does demand in excess of the cap ever move a saturated register — a floor that yields under load — or does a saturated register stay saturated? I've read R-FLOOR-REGISTER as the latter.*

> "The saturated register yielding under load is the only way I can
> model reality the way we have constructed it."

*Opus (Patch 3638):* taken as: the cap is not rigid; a register at cap displaces further when loaded. The **yield law** — whether the displacement settles under a steady load (elastic, a stiffness) or continues while the load persists (creep), and whether it is reversible — is not stated and is the next question. The ruling is consistent with the corpus's one-Moment-delay *compliant* surface (3375/3376; the O(kd) compliance deferred since CONV-038) and with 3390's branch (a) for OPEN-GR-SURFACE-STABILITY-1. See `rcore_derivation/3638_cap_yields_consequences.md`.
