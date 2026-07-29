# ROUTE 2 — FIRST RESULT: the pair centre does not move on a uniform field (Patch 2853)

**Filed 2026-07-27. Route 2 (correlated-Sea derivation) was identified
at 2851 §3 as the only path to the ambient bound that avoids the FEM
wall. First result below. NOT a bound; a structural suppression.**

## §1 — The result

Under C19/C20 both CPs of a bonded pair displace along their own
perceived SSV_net, with polarity sign:

- **CP⁺** displaces along **+SSV_net** at its location;
- **CP⁻** displaces along **−SSV_net** at its location.

**If both CPs perceive the SAME field E, the pair's CENTRE DOES NOT
MOVE.** The two displacements are equal and opposite; only the
*polarisation* changes. Centre-of-mass motion requires the field to
**differ across the pair** — i.e. it is driven by the field
**gradient**, not the field:

> **v_centre / v_CP ~ (∇E · d_DP)/E ~ d_DP / L_field**

with L_field the scale on which the external field varies.

## §2 — What this fixes, including a correction to Patch 2851

**The ambient bound 1B needs is a DIFFERENT and SMALLER quantity than
CPP's primitive ratio.** |SSV_net|/SSV_abs is the **CP-level** speed —
what an individual CP does, dominated by its own partner. The bound
requires the **centre-level** speed, suppressed relative to it by
d_DP/L_field.

**This diagnoses 2851's failure more sharply than 2851 itself did.**
That patch attributed the √N attempt's failure to assuming
independence where C26 commits bonded pairs — correct as far as it
went. The sharper statement: **the √N argument was computing the
CP-level ratio, which is not the quantity 1B asks about at all.** Even
had the scaling held, it would have bounded the wrong velocity. Both
diagnoses stand; this one is prior.

## §3 — Why this is progress but not a bound

The suppression factor is d_DP/L_field, and **L_field is not
established**. In a dense Sea the external field varies on the scale
of neighbouring pair separations, which is itself ~d_DP — giving no
suppression. In a dilute Sea, L_field ≫ d_DP and the suppression is
large. **The dilute/dense distinction is exactly C26's bonded-vs-plasma
phase question**, and the founder has ruled current conditions dilute
and bonded — which argues for suppression, but the ratio has not been
computed.

**Next step in route 2:** compute L_field for the bonded dilute Sea —
i.e. the correlation length of the residual field after each pair's
own partner contribution is subtracted. That is an analytic
statistical-mechanics question about a correlated dipole gas, and it
does not require the arc-inertia specification. **It remains the only
identified path to 1B that does not run into the FEM wall.**

## §4 — Standing

Nothing asserted. 1A MET · CPP-DARWIN RESTORED-CONDITIONAL (conditioned
on OPEN-C23-TRANSVERSE-VALIDATION, 3–2) · 1B OPEN, operative bar
v/c ≤ 0.15 · PR7 PARTIAL · six of seven · B7 holds.
