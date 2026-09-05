# OPEN-GR-SATURATION-THRESHOLD-1 CLOSED — the relativistic threshold is a central-lapse condition, N_c = ½, not Buchdahl. Uniform density: C = 5/18 = 0.278 (the lattice-census reading: 36/121 = 0.298). TOV polytropes Γ = 2, 2.5, 3 all reach it ON THE STABLE BRANCH at C ≈ 0.20–0.24. The heaviest observed neutron stars (C ≈ 0.25, central redshift ≈ 1) sit at or past it: "neutron stars do not saturate" (3629 Q6) is wrong for the most massive ones. Spawns OPEN-GR-SATURATED-CORE-1 and a founder picture question

**Patch 3634, Session 162, 5 Sep 2026.** Verify `code/3634_saturation_threshold_verify.py` (8/8). Reasoning `reasoning/3634.md`. No paper touched (GR-2 V2.2's compactness paragraph is exposed; see §4).

## §1 What the register is, relativistically
R-CLOCK-RATE-IS-DISPLACEMENT + R-PSR-LAW-LOG: the register *is* the lapse, `v = N⁻¹(lapse)`, `N = (1 − v/2)/(1 + v/2)` — exactly as the exterior `v = M/r̄` is `N⁻¹` of Schwarzschild's isotropic lapse. The cap `v = 2/3` is **lapse ½**. So a body saturates at its centre when its **central lapse reaches ½**. That is a TOV statement, and it replaces 3629 §4's Newtonian one.

## §2 The numbers
- **Uniform density** (Schwarzschild interior): `N_c = (3/2)√(1−2C) − ½ = ½` at **`C = 5/18 = 0.278`**. Buchdahl (4/9) is where `N_c = 0`. 3629 quoted the *isotropic* census ratio `M/R̄ = 4/9` as if it were an areal compactness; mapped through the exterior it is `36/121 = 0.298`. Both thresholds are far below Buchdahl and at the upper edge of the neutron-star range.
- **TOV polytropes** `p = Kρ^Γ`: every one reaches `N_c = ½` on the stable branch, *before* the maximum mass:

| Γ | C at N_c = ½ | C_max | N_c at max mass |
|---|---|---|---|
| 2.0 | 0.204 | 0.213 | 0.47 |
| 2.5 | 0.230 | 0.281 | 0.34 |
| 3.0 | 0.242 | 0.316 | 0.27 |

- **Anchor:** a 2.08 M☉ star at 12.4 km (PSR J0740-like, recollection) has `C = 0.248` and a central redshift of order 1 — **at or past the saturation compactness for every EOS computed.** Ordinary 1.4 M☉ stars (`C ≈ 0.17`) do not reach it.

## §3 What this means
- The corpus's sentence "**in CPP, collapse past Buchdahl is register saturation**" (3629) is superseded by "**central lapse ½ is register saturation**" — a condition every stable sequence crosses before its maximum mass. Saturation is not the end state of collapse; it is a property of the cores of the most massive stable neutron stars.
- 3629 Q6's standing was decided on a threshold that is wrong by a factor of two in compactness. Copilot's EXCLUDED-BY-NS-DATA still does not carry as stated (C = 0.375 was a claim about *surface*-saturated objects), but the dichotomy behind it — "neutron stars unsaturated, R-cores saturated" — is gone: **there is a third class, stars with a saturated core and an unsaturated envelope**, and the heaviest observed pulsars are in it.
- A saturated core is 3375's over-demanded interior: register pinned, clocks at rate ½, no further register response to added count. What that does to the matter — pressure support, the EOS, the maximum mass, cooling, the tidal deformability of the heaviest stars — is not in the corpus. **OPEN-GR-SATURATED-CORE-1** minted.

## §4 Exposure and next
- GR-2 V2.2's compactness paragraph ("neutron stars do not saturate; C = 0.375 is a statement about collapsed objects") owes a correction at its next touch (with V2.3, held with CONV-042): saturation begins inside stable stars at C ≈ 0.2–0.25; the surface-saturated R-core at C = 0.375 remains the collapsed end state.
- **Founder picture asked (one):** inside a heavy neutron star whose central register has reached the cap, what happens to the matter there — does the pinned register change how the core supports itself (the register no longer responds to added count, so the "weight" of the core as read by the lattice stops growing), or is the matter unaffected and only the clocks are capped? The answer decides whether CPP predicts a maximum neutron-star mass different from GR's for a given EOS — a test with existing data.
- OPEN-GR-SATURATION-THRESHOLD-1: **CLOSED** (threshold derived). Successor: OPEN-GR-SATURATED-CORE-1.
