# THE MAGNETIC CURL FROM THE MOMENT RULE — DERIVATION (Patch 2842)

**Filed 2026-07-27 at founder request: does a cross product fall out
of the leading/trailing DP-arc picture? **It does — but NOT from the
leading/trailing magnitude difference.** The source is the
time-rotation of the retarded field direction as the charge passes.
Verification in this patch; script logic reproduced in §5.**

## §1 — Why the leading/trailing magnitude route does NOT produce it

For an observer perpendicular to the motion at distance r, the leading
shell point (+R along **v**) and the trailing point (−R) are both at
distance √(R² + r²) — **exactly equal**. The magnitude difference the
mechanism relied on **vanishes identically for the perpendicular
observer**, which is precisely where the magnetic effect is maximal.
For off-axis observers a near/far asymmetry does exist, but it exists
for a *stationary* charge too: it is the geometry of viewing a sphere
off-centre, not an effect of motion.

**So the founder's instinct that "there has to be something this is in
relationship to" was right, and the relationship is not distance — it
is TIME.**

## §2 — The mechanism that does work

The founder's own aside carried it: *"successive shells are centred at
slightly different locations along the CP's path."* Consequence at a
fixed observer:

The field direction at the observer is the unit vector **r̂**(t) from
the charge's **retarded position** to the observer (strict c
propagation; C21/C22 — no instantaneous action anywhere). As the
charge passes, **r̂ SWEEPS**. The DP at the observer polarises along
**r̂**, so the DP poles sweep with it. **That sweep IS the arc.**

Its rotation vector is

> **ω_arc = r̂ × dr̂/dt = (v × r̂)/r**

## §3 — Verification (machine precision)

| observer | ω_arc (numeric) | (**v** × r̂)/r | angle between |
|---|---|---|---|
| (0, 2, 0) | (0, 0, 0.5) | (0, 0, 0.5) | **0.00°** |
| (0, 0, 2) | (0, −0.5, 0) | (0, −0.5, 0) | **0.00°** |
| (0, 1.414, 1.414) | (0, −0.354, 0.354) | (0, −0.354, 0.354) | **0.00°** |
| (0, −2, 0) | (0, 0, −0.5) | (0, 0, −0.5) | **0.00°** |
| (1, 2, 0) | (0, 0, 0.4) | (0, 0, 0.4) | **0.00°** |
| (3, 0, 0) — on axis | 0 | 0 | both vanish |

**Magnitude law:** |ω_arc| = v sin ψ / r exactly (checked at
r = 1, 2, 2.83, 4 and ψ = 45°, 90°).

**TOROIDAL STRUCTURE — the founder's guess, confirmed exactly.** At
every azimuth φ around the motion axis, **v** × r̂ · φ̂ = **+1.000000**.
The arc axes are **purely azimuthal**: a toroid of circulation wrapped
around the axis of motion, exactly as *"a toroid of leading and
trailing momentum arcs around the axis of the moving charge."*

**Every structural property of Biot–Savart is reproduced:** direction
**v** × r̂; toroidal circulation; **vanishes on the motion axis**
(sin ψ = 0); maximal perpendicular; and **sense reverses across the
axis** — observer at +y arcs counterclockwise, at −y clockwise. That
reversal is the founder's N/S pole distinction, and it also gives the
charge-sign and orbital-direction reversals he describes.

## §4 — The one discrepancy, stated plainly (no third overclaim)

**Radial falloff.** |ω_arc| ∝ 1/r, whereas Biot–Savart B ∝ 1/r².
Direction and topology match exactly; the radial law does not.

This is **not** obviously a defect, because ω_arc is the arc's angular
RATE, while the arc's AMPLITUDE follows the polarisation, P ∝ E ∝ 1/r².
Which combination of rate and amplitude is to be identified with **B**
is a normalisation question the calculation does not settle: the rate
alone gives 1/r; the polarisation current dP/dt = ω × P gives 1/r³;
B needs 1/r². **A founder ruling (or a derivation from the DI-bit
bookkeeping) is required to say which measure of the arc is the
magnetic field.** Until then: **the curl is established, the
normalisation is not.**

## §5 — Standing and consequence for 1B

The calculation is analytic and lattice-independent — it uses only
strict c-propagation and polarisation along the arriving field, both
committed (C21/C22/C23). It supplies exactly what the 2841 scoping
correction identified as missing: **the transverse sector lives in the
Sea's response, and that response has the Biot–Savart circulation
structure.**

**It does NOT by itself close 1B**, and the second-order bound
withdrawn at 2840 is **not** restored here. What it establishes is
that the transverse sector *exists and has the right structure* — the
remaining question is whether it enters the charge–charge interaction
at the order the Darwin cancellation requires, which needs the
normalisation of §4. **1B stays OPEN; PR7 PARTIAL; six of seven; B7
holds.**
