# Reasoning capture — Patch 3806: the bath-depth lag bound

*Session 167, 9 Sep 2026, EU lane. Verbatim at-patch capture. Finding: `bath_depth_lag_bound.md`. Verify: `scripts/3806_bath_depth_lag_bound.py` (6/6).*

GPT's objection at CONV-045 was fair: I had said a slow bath at depth 10⁷⁴ could only produce O(α) corrections inside the theory error, and I had not computed anything. The right response was to find what the corpus already measures — 0769's R = τ_eq H and 0772's spectral gap — and ask precisely what AP-5 changes in them.

The first thing to settle was whether depth is serial or parallel, because that is a 74-order question. I read D1 and D2 again for their tense: layer n+1 "activates at that GP for that Moment"; the copy is "repositioned each Moment." Every active layer runs its cycle every Moment. A serial reading would make a black hole's register take 10⁷⁴ Moments to respond to one arrival, which contradicts the GR lane's whole ringdown result (the wave is relayed whole each Moment, D3). So parallel is not my choice; it is what the ratified text and the GR results already require. I recorded the serial alternative in the verify as the thing the structure excludes (R ~ 10⁷⁰), because a reader should see how bad the other reading would be.

The second thing is what the clip does to the mixing. The ZRP's hops are between GPs — layer 1. At the cap the lapse is ½, so a hop takes two Moments. I ran 0772's exact generator with the rate halved; the gap halved exactly, as it must (the generator scales). So τ_eq at most doubles. The deeper layers move CPs within cells, not between GPs, so they are irrelevant to the count statistics either way.

Then the lag → tilt map. I set up first-order relaxation of μ toward 3kT N_rem with N_rem falling at H, found the steady offset 3kT R, and saw immediately that an additive constant in μ is an additive constant in the effective N_rem: n_s − 1 = −2/(N_* + R). I integrated the ODE anyway and differentiated numerically, because a formula I found in two lines is exactly the kind I should check. It matched to 1 % at R = 0.1 and 2 % at R = 0.81.

The bound then writes itself: R ≤ 2·30·(4.7×10¹³/1.22×10¹⁹) = 2.3×10⁻⁴, Δn_s ≤ 1.4×10⁻⁷. The theory-error budget of 5×10⁻⁴ needs R = 0.81, i.e. H ≥ 1.7×10¹⁷ GeV — the Planckian case 0769 already excluded twice. I noticed the sign: a lag makes the tilt less red, so even a bad lag cannot fake a redder spectrum.

The premise I cannot derive here and must name: that the ZBW hop is per-CP and independent, not lockstepped. 3701 derived lockstep for SSV-driven repositioning of co-located CPs seeing one census; the ZBW is the CP's own cycle with random phase (0738). If someone reads saturation as lockstepping the ZBW too, the ZRP freezes and the bound does not apply — the Gibbs state would then have to be carried rather than reached. I put that in §4 rather than hiding it, because it is the one place the argument could be attacked at the picture level.

No panel: this discharges a reviewer's owed computation inside an already-adjudicated round; the result is a bound, not a new claim.
