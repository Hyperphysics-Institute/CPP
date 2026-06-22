# The Missing Machinery: Photon ≠ Phonon — Why R2's FAIL Is Not Secure, and γ Is Exact

**Patch:** 2024 (22 June 2026) · **Window:** 2000-band · **Status: substantive — resolves VTD-1 & VTD-2,
and REOPENS R2 from "leaning FAIL" to genuinely OPEN.** Doing the velocity calculation surfaced a category
error in the R2 retraction: it used the DP-lattice **phonon** speed (c∝√C) for the **photon**. Three results:
(1) VTD-1 exact-γ passes via the quadrature budget; (2) VTD-2 (velocity α) is resolved (Lorentz scalar);
(3) R2's FAIL is not secure — the photon speed's C-dependence is undetermined, not √C, and the
unified-budget principle would give α-constancy WITH variable c (VSL + R2-PASS together).
**Verify:** `budget_and_photon_phonon.py`.

---

## 1. VTD-1 — exact γ from the quadrature budget (PASS, conditional)

SR-1's displacement budget is a 4D speed limit: total displacement ≤ l_P per Absolute Moment. Bulk motion
consumes v·t_P along the direction of travel; internal processes get the remainder. If that remainder is the
**orthogonal (Pythagorean)** part, √(l_P² − (v t_P)²) = l_P√(1−v²/c²), then internal rates scale by exactly
1/γ ⇒ **γ_CPP = 1/√(1−v²/c²) EXACTLY** (verified to 1e-9 across v/c up to 0.99). The naive linear form
(1 − v/c) is wrong. SR-1 has the quadrature structure (R₄D² = r₃D² + τ²). **VTD-1 passes iff bulk and
internal displacements are orthogonal in the budget** — the one assumption to nail.

## 2. VTD-2 — velocity α is resolved (it is not an independent threat)

Once VTD-1 holds, the moving frame is an exact Lorentz boost of rest. α is a **Lorentz scalar**, so it is
preserved automatically — a moving atom has the rest α, with all rates dilated by γ (transverse Doppler;
Ives–Stilwell). The velocity frame does **not** independently threaten α. VTD-2 ⇐ VTD-1. (Last patch I called
VTD-2 "≡ R2"; that was too strong — for *velocity* it is protected by scalar invariance, which gravity lacks.)

## 3. R2 — the FAIL used the PHONON speed for the PHOTON (category error)

The identity is solid: Z₀ = 1/(ε₀c) = C/c, ε₀ ∝ 1/C. R2 PASS ⟺ c ∝ C. The 2021 retraction took c ∝ √C and
concluded FAIL. **But c ∝ √C is the DP-lattice acoustic/elastic wave speed √(C/m)·a — a PHONON.** c06 says
the **photon** advances one PSR shell per Absolute Moment — the **budget** speed c_photon = PSR_eff/t_P — and
Patch 2011 already established the photon is **not** the acoustic mode. So 2021 plugged the phonon speed into
the photon's impedance.

- **The photon speed's C-dependence is set by the ΔSSV↔C relation, which is currently unspecified** — it is
  NOT the phonon's √C. So "Z₀ ∝ √C" is not established; R2's c was the wrong object.
- Honest correction to 2021: the secure statement is **Z₀ = C/c_photon with c_photon's C-scaling
  undetermined ⇒ R2 OPEN**, not "leaning FAIL." The FAIL over-committed by conflating phonon and photon.

## 4. The resolution this points to — the unified-budget principle

c06 (photon = budget) + SR-1 (clocks/matter = budget) jointly imply **light and matter draw from the SAME
displacement budget (PSR)**. Then under any SSV change both c_photon and the electron orbital velocity scale
by the same 1/γ, so **α = v_orbit/c_photon is invariant while c varies** — VSL (c varies = gravity) and
R2-PASS (α fixed) **simultaneously**, from one principle. The 2021 FAIL appeared only because the
decoupled-mechanical model let c (phonon) and the matter structure (ε₀) scale independently — which
contradicts CPP's own unified-budget picture.

| model | c_light | α under SSV | status |
|---|---|---|---|
| decoupled-mechanical (2021) | c_phonon ∝ √C | drifts ∝ √C | the FAIL — uses wrong (phonon) speed |
| **unified-budget (c06+SR-1)** | **c_photon = budget** | **invariant** | VSL ✓ + R2 PASS ✓ |

## 5. Honest status

- **VTD-1:** PASS, conditional on the quadrature (orthogonality) assumption. (SR-1 has the structure.)
- **VTD-2:** RESOLVED — velocity α preserved by Lorentz-scalar invariance, given VTD-1. Not an independent gate.
- **R2:** REOPENED from "leaning FAIL" → **OPEN**. The FAIL used the phonon speed; the photon speed's
  C-dependence is undetermined. The unified-budget principle would give PASS, and is grounded in c06 + SR-1.
- **The missing machinery, now named:** (a) confirm c_light = the photon/budget speed, NOT the phonon
  √(C/m)·a (c06 + 2011 strongly imply this); (b) derive the ΔSSV↔C relation that fixes c_photon(C); (c) show
  ε₀ (matter structure) co-scales with c_photon under the budget so Z₀ is held fixed. (a) is nearly in hand;
  (b)+(c) are the real remaining work — and they are the SAME work for gravity (R2) and velocity (VTD).
- **Not overclaimed:** this does NOT revive R2 to a clean PASS. It shows the FAIL was insecure (a category
  error) and identifies the unified-budget route to PASS. R2 is honestly OPEN, with a resolution path.

NO THEO. The arc, stated plainly: 2016/17 PASS (circular) → 2021 FAIL (phonon-speed category error) → 2024
OPEN (photon ≠ phonon; unified budget is the route). Each step followed the physics, including this one
correcting the last.
