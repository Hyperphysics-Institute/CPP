# R2 — Panel (ChatGPT) CONFIRMs the advance, REVISEs the claim: attack shifts anisotropy → locality

**Patch:** 2029 (22 June 2026) · **Window:** 2000-band · **Status: panel REVISE accepted. Label corrected to
PASS conditional on VTD-1 + scalar-channel isolation beyond leading order. The locality residual is now
QUANTIFIED (~11 orders below the LPI bound) but rests on c07 metric completeness.** **Verify:**
`scripts/2029_gradient_suppression.py`.

---

## 1. The panel verdict (ChatGPT)

- **On the 2028 advance: CONFIRM.** The channel split (scalar SSV_abs→g_tt sets c_photon; gradient→g_ij
  carries anisotropy) answers the original f(C,Σ) birefringence objection in a nontrivial way. "The burden
  has moved."
- **On the claim "PASS conditional on VTD-1 alone": REVISE.** Universality is narrowed, not eliminated. The
  honest label is "PASS conditional on VTD-1 **plus the scalar-channel isolation holding beyond leading
  order**."
- **Three sharp points, all accepted:**
  1. *Grounded ≠ established.* The "uniformly affected" premise is still a physical interpretation, not a
     calculation. Status = "structurally motivated and corpus-consistent," not "demonstrated."
  2. *The attack shifts anisotropy → locality.* The null cone is c² ~ g_tt/g_ij; in a uniform region
     g_ij=δ_ij, but is local α truly insensitive to higher-order spatial-sector contributions?
  3. *Schur (support 3) is the weakest.* It shows the *unperturbed* medium is isotropic; it does not prove
     *perturbations* preserve isotropy (strained symmetric lattices can develop anisotropic response).
     Supports 1+2 are the real argument; 3 is suggestive.

## 2. Accepted — and the label corrected

All three are right. I conflated "universality grounded" with "one fewer assumption"; the accurate statement
is that the universality assumption was **replaced by a narrower one** — scalar-channel isolation beyond
leading order — not removed. Schur is demoted to suggestive. The real argument is **supports 1+2**: SSV_abs
(scalar magnitude) sets PSR→c_photon (`pcd_boost_law` l.15/18), and the c07 metric puts all anisotropy in the
gradient g_ij.

## 3. The locality residual, QUANTIFIED

ChatGPT's narrowed question is concrete enough to estimate. In a uniform region the c07 form gives
**g_ij = δ_ij exactly**, so the scalar-channel isolation is exact there; the *only* breaking is the gradient
∇SSV. Its size for terrestrial atomic-clock LPI:

- L_grad = |SSV|/|∇SSV| ≈ Φ/g ≈ 6.4×10⁶ m (≈ Earth radius, as expected).
- L_atom ≈ 10⁻¹⁰ m.
- Spatial-sector contribution to local α, relative to the scalar effect: **L_atom/L_grad ≈ 1.6×10⁻¹⁷**.
- LPI bound ≈ 10⁻⁶ ⇒ the spatial-sector contribution is **≈ 11 orders of magnitude BELOW the bound**.

So the higher-order spatial contribution to local α is gradient-suppressed to ~10⁻¹⁷ — far beyond the
precision R2 tests. The scalar-channel isolation holds to the needed precision for terrestrial LPI.

## 4. Honest caveats and status

- **Caveat (a):** order-of-magnitude estimate, not a rigorous bound. A full treatment would compute the
  coefficient, not just the scaling L_atom/L_grad.
- **Caveat (b):** the estimate relies on the c07 metric form g_ij = δ_ij + k|∇SSV| being **complete for the
  static local-α sector**. The 1110 audit flagged that c07's metric map is *limited for GW radiation* (it
  lacks TT modes); completeness for the *static* sector is plausible but not established. If c07's static
  metric has additional spatial terms, the isolation estimate would need revisiting.
- **Status (honest):** **R2 PASS conditional on (i) VTD-1 + (ii) scalar-channel isolation beyond leading
  order**, where (ii) is now *quantitatively supported* (~11 orders of suppression for terrestrial LPI) but
  rests on the c07 static-metric completeness. This is a real narrowing of (ii) from "unproven" → "estimated
  to hold by ~11 orders, modulo c07 static completeness." Not closure; a much smaller residual.
- **The residual is now precise and twofold:** (1) is c07's static metric complete (no extra spatial terms in
  the local-α sector)? (2) does VTD-1's quadrature assumption hold? Both are concrete, separable targets.

NO THEO. Arc: …2025 PASS-cond → 2027 REVISE(universality) → 2028 universality grounded (channel split) →
**2029 REVISE accepted: PASS conditional on VTD-1 + scalar-channel isolation (~11 orders supported, modulo
c07 static completeness).**
