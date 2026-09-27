# Calibrating N to α Is Legitimate as a Labelled Calibration; the Only Independent Observable Now Tied to N Is the Black-Hole PSR, and It Disagrees With SR-1's Floor by 10¹⁶; Gravity Is the Promising Second Leg but Is Not Yet Written in Counts

**Patch:** 4310. **Lane:** EW → foundations. **Session:** 240.
**Founder:** `founders_voice/4310_proposal_calibrate_n_to_alpha_and_triangulate.md`.
**Verify:** `series_standard_model/code/4310_triangulation_audit.py`.

## 1. Calibration (rows A)

```
    PSR/s = 1.0e+30: N = 9.17e+28 per GP per Moment
    PSR/s = 1.0e+32: N = 9.26e+30 per GP per Moment
```

Yes: fix N by α through α = N s/(4π PSR). It joins the corpus's other calibrated parameters (SF-6's m₀, the DE lane's
sea density, the EU lane's GP spacing) and must be labelled as one: after it, α is *reproduced*, not predicted. N also
inherits the corpus's two GP spacings, which differ by 100. The calibration earns its keep only when a second observable,
computed without α, depends on N. The audit below is of what the corpus offers.

## 2. Candidate triangulations

**(B) The black-hole PSR — available now, and it disagrees.** The founder's surface count (4304, 4308) makes N the
number of GPs on a shell at the smallest PSR, so α predicts PSR_min = √(α s PSR):

```
    PSR/s = 1.0e+30: PSR_min = 8.5e-17 l_P;  SR-1 register floor l_P/2 = 5.0e-01 l_P  -> disagree by 6e+15
```

SR-1's registered PSR_eff = l_P/(1 + k·ΔSSV), with the register floor at l_P/2, cannot reach 10⁻¹⁶ l_P. The founder has
said the floor has no conceptual standing (4300); dropping it, the cross-check becomes a GR-lane computation: **what is
the largest k·ΔSSV the sea admits (at a singularity, not a horizon), and does it reach 10¹⁶?** If it does, the surface
count and α agree; if the PSR cannot shrink below about l_P, the surface-count reading of N is wrong and N's meaning
must be found elsewhere. This is the sharpest test on offer, and as the corpus stands it fails.

**(C) Gravity — the right second leg, not yet in the right form.** GR-1a writes the gravitational SSV quantum as
Q_grav = (mc²/E_P)·Q_Planck with k = α l_P³/E_P, "α cancelling identically" (c02). So G is tied to E_P, k, α_geom and
SSV_crit, none of which is N, and no triangulation exists yet. There is also a tension with AP-4: AP-4 has every GP emit
the same fixed number of DI-bits, while GR-1a's source strength scales with mass-energy. If AP-4 is right, gravity must
be a *modulation* (the SSV_abs-dependent PSR and displacement response) rather than extra emission, and G would then be
expressible in N and the GP occupancy of a mass. The number such a formulation must reproduce is

```
    alpha_G = (m_e/m_P)^2 = 1.752e-45;  alpha_G/alpha = 2.40e-43
```

A count-based G that lands on that ratio would be the mutual validation the founder asks for. Also found on the way:
GR-1a's "(e/e_P)² ≈ 7.3 × 10⁻³ is set by the 600-cell cage geometry (Stiffness C §4.3)" is unsupported; c02's α_geom is
0.559, a Voronoi factor, and its α is a normalisation that cancels. Added to TODO-4300-HBARSWEEP.

**(D) Not checks.** The EU e-fold budget's N = ln(l_P/s) + 1.31 counts e-folds, not emissions. The DE lane's sea density
and QM-6's sea_strength are calibrated separately and are not yet written as functions of N; they become checks only if a
model connects them. The running of α (QED, from sea polarisation) does not involve N at accessible scales: the count
relation changes only inside the crowding radius, about 10⁻⁵¹ m. Everything electromagnetic (a_e, Lamb shift, Rydberg)
uses the same α and cannot triangulate it.

## 3. What I think

Calibrate N to α, label it, and put the two-spacing ambiguity on it. Then the programme has exactly one live cross-check
and one to build. The live one, the black-hole PSR, currently disagrees by sixteen orders, which is either a failure of
the surface-count reading or a statement about how far the PSR can shrink; that is a physics question for the founder
and the GR lane, not an arithmetic one. The one to build is gravity in DI-bit counts, resolving GR-1a's mass-scaled
emission against AP-4's fixed emission; its target number is 2.4 × 10⁻⁴³.

## 4. Founder question (a physical picture)

**Does a massive body emit more DI-bits than an empty region, or the same number with a different effect?** GR-1a has the
source strength scale with mass-energy; AP-4 has every GP emit the same fixed count. If it is the same count, gravity is
in how the sea *responds* (the PSR and displacement per Moment), and G can be written in N. That would give the second
observable your triangulation needs.

## 5. PD-008

- **Convenient branch refused.** Calling α "reproduced" a validation. It is a calibration until a second observable
  bites, and the one that bites now disagrees.
- **What is solid.** The two calibrated N values; the 10¹⁶ mismatch of the surface-count PSR_min with SR-1's floor;
  GR-1a's independence from N and its α cancellation; the target ratio 2.4 × 10⁻⁴³.
