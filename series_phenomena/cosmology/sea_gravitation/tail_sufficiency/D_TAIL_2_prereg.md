# PREREGISTRATION — **D-TAIL-2: DOES THE CALIBRATED SPACING ITSELF MOVE UNDER MATCHED-VARIANCE TAIL CHANGES?** The question D-TAIL-1 made sharp: if d_s^emp depends on the drive's SHAPE at fixed σ, the cosmological-constant calibration inherits a dependence nobody has measured

**Patch 3194, 22 August 2026. Container. Frozen before computation.**

## §1 — Why this is the consequential follow-up

3131/3129 measured d_s^emp nearly IMMUNE to the drive's MAGNITUDE
(σ_n halved or ×1.5 moves it ≤ 0.021 — half a percent across a
factor-3 bracket). **That immunity is the reason the calibration was
considered well-conditioned.** D-TAIL-1 then showed the Sea's
equilibrium observables respond strongly to the drive's SHAPE at
fixed variance (f_dwell by 41.7 SE). **Immunity to magnitude does not
imply immunity to shape**, and the calibration's conditioning has only
ever been tested against magnitude.

## §2 — Method (frozen; the inversion machinery UNCHANGED)

The 3129 inversion, reused exactly: run_cell over the frozen grid
d_s ∈ {2.6, 3.0, 3.5, 4.0, 4.5, 5.5} at n = 5, seed 5; Φ from the
certified `phi()`; the CLI curve from `cli()`; d_s^emp by the same
linear inversion at TARGET = 0.80. **Nothing about the inversion,
the grid, the target, or Φ is touched.** The ONLY change is the drive
channel: a `tail` parameter added to `run_cell` such that
`tail=None` leaves the Gaussian line and its RNG draw byte-identical
(verified before this prereg was committed).

**Arms, all at σ_n = 0.30 (variance matched by construction,
amp = σ/√p):**
- **G** — Gaussian (the operating drive; reproduces the banked
  baseline).
- **S05** — 0.5% burst rate — the arm that produced D-TAIL-1's
  largest f_b effect.
- **S2** — 2% burst rate — D-TAIL-1's largest f_dwell effect.

## §3 — Frozen statistic, floor, falsifier

- **Statistic:** d_s^emp per arm, from the identical inversion.
- **Floor:** the 3129 §1 record establishes the scale against which a
  shift counts — **σ_n perturbations of ±50–100% moved d_s^emp by
  ≤ 0.021.** That is the comparison bar, stated before the numbers
  exist. A seed-class difference of 0.019 is also on record (3129
  §1 nuance), so **0.021 is treated as the noise scale.**
- **Falsifier / abort:** if any arm's CLI curve fails to bracket
  TARGET on the frozen grid, that arm returns NO-INVERSION and is
  reported as such — no grid extension, no target adjustment.

## §4 — FROZEN READINGS

Let Δ = max over arms of |d_s^emp(arm) − d_s^emp(G)|.
- **SHAPE-IMMUNE** iff Δ ≤ 0.021 (the magnitude-perturbation scale)
  ⇒ the calibration's conditioning extends to tail shape; D-TAIL-1's
  effects do not propagate to the inverted quantity; **the
  calibration is safer than D-TAIL-1 suggested.**
- **SHAPE-SENSITIVE-MINOR** iff 0.021 < Δ ≤ 0.218 (the gas-threshold
  variant's already-accepted definitional sensitivity, 3129 §2)
  ⇒ a real dependence, bounded by a sensitivity the corpus has
  already absorbed; the calibration label must name it.
- **SHAPE-SENSITIVE-MAJOR** iff Δ > 0.218 ⇒ **the drive's tail
  structure is a first-order input to the cosmological-constant
  calibration, and d_s^emp = 4.636 carries an unquantified systematic
  from a choice (Gaussian noise) that was never physically
  motivated** — the Sea's own force series being intermittent (3183).

## §5 — Hazard direction (declared)

SHAPE-IMMUNE protects the corpus. SHAPE-SENSITIVE-MAJOR damages the
headline calibration and would oblige a labelled systematic on
d_s^emp. **Worker's pre-declared expectation: SHAPE-SENSITIVE-MINOR.**
Reasoning recorded now: D-TAIL-1's effects were large in dwell and
swap but modest in f_b (7.8 SE ≈ 1.8% shift), and Φ's plateau is
98.6% gas-channel (3129 §3) — a single-regime quantity is less
exposed to partner-exchange statistics than f_dwell is. **Five
consecutive pre-declarations have now missed; this one is exposed
identically.**

## §6 — Fence

No Kila6 time (β-ladder running steady, ~2–3 days, outranks all). No
change to Λ, to the frozen d_s* = 2.450, to DISP-I3, or to any DM
quantity. The calibration label (OBL-CAL-LABEL: d_s^emp is
cosmology-calibrated) is unaffected in kind by any outcome — what may
change is whether it must also carry a tail-shape systematic.
