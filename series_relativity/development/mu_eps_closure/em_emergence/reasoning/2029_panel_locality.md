# Reasoning capture — Patch 2029: panel REVISE accepted; locality residual quantified

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.

ChatGPT: CONFIRM the 2028 advance (channel split answers birefringence nontrivially), REVISE the claim. Three
points, all correct, all accepted:
1. grounded != established ('uniformly affected' is interpretation, not calc).
2. attack shifts anisotropy -> LOCALITY (null cone c^2 ~ g_tt/g_ij; is local alpha insensitive to spatial
   sector beyond leading order?).
3. Schur (support 3) weakest -- unperturbed isotropy != perturbed isotropy. Supports 1+2 are the argument.

I accepted all three without defensiveness. Key honesty move: I had conflated 'universality grounded' with
'one fewer assumption / VTD-1 alone'. The accurate statement is the universality assumption was REPLACED by a
NARROWER one (scalar-channel isolation beyond leading order), not removed. Corrected the label. Demoted Schur
to suggestive.

Then I did the thing that adds value: quantified ChatGPT's narrowed (locality) concern. In a uniform region
the c07 form gives g_ij = delta_ij EXACTLY, so isolation is exact there; the only breaking is the gradient.
Estimated its size for terrestrial atomic-clock LPI: L_atom/L_grad ~ 1e-10/6.4e6 ~ 1.6e-17, ~11 orders below
the LPI bound (1e-6). So the spatial-sector contribution to local alpha is gradient-suppressed far beyond R2's
test precision.

Held honesty hard on the caveats:
- (a) order-of-magnitude estimate, not a rigorous bound (coefficient not computed).
- (b) relies on c07 static-metric COMPLETENESS -- the 1110 audit flagged c07's metric is limited for GW
  radiation (no TT modes); static-sector completeness is plausible but NOT established. If c07 static has
  extra spatial terms, the estimate needs revisiting. I surfaced this myself rather than letting it pass.

Status: PASS conditional on (i) VTD-1 + (ii) scalar-channel isolation beyond leading order, with (ii) now
quantitatively supported (~11 orders) modulo c07 static completeness. Real narrowing of (ii), NOT closure.
The residual is now precise and twofold: c07 static completeness + VTD-1 quadrature. Both concrete targets.

This is the review working as designed: it CONFIRMed the mechanism, narrowed the residual to a sharper
question, and I answered the sharper question with an estimate while naming exactly what the estimate rests
on. No status inflation -- still PASS-conditional, just with a much smaller, precisely-located residual.

Action: finding + script + R2-STATUS update. NO THEO. Owned path. Files via bash; verified.
