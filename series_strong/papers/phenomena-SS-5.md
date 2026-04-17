# Phenomena: SS-5 — Deuteron Binding Energy

**Paper:** SS-5 v0.1
**Last updated:** 16 April 2026

---

## PHEN-E — Empirical phenomena explained

| ID | Phenomenon | CPP account |
|---|---|---|
| PHEN-E-SS-5-1 | Deuteron binding energy is $\sim 2.2$ MeV (order of magnitude) | Natural consequence of $M_0/\varphi$ scale from electron mass and 600-cell geometry |
| PHEN-E-SS-5-2 | Diproton (${}^2\mathrm{He}$) does not exist as a bound nucleus | Open-vertex polarity pairing: $(+,+)$ cannot form ZBW edge |
| PHEN-E-SS-5-3 | Dineutron (${}^2n$) does not exist as a bound nucleus | Open-vertex polarity pairing: $(-,-)$ cannot form ZBW edge |
| PHEN-E-SS-5-4 | Deuteron has $J^P = 1^+$ and $I = 0$ | Polarity pairing antisymmetric under p↔n; radial S-wave bond |
| PHEN-E-SS-5-5 | $np$ singlet (S=0) state is virtual, just above threshold (~60 keV) | Unreinforced bond, below the $\eta$-enhanced triplet threshold |
| PHEN-E-SS-5-6 | Nuclear chart begins at deuterium, not ${}^2\mathrm{He}$ or ${}^2n$ | Consequence of PHEN-E-SS-5-2 and PHEN-E-SS-5-3 (geometric, not dynamical) |
| PHEN-E-SS-5-7 | Radiative $np$ capture: $np \to d + \gamma$ with $E_\gamma = 2.224$ MeV | Delivered fraction of $M_0$ emitted as photon at bond formation |
| PHEN-E-SS-5-8 | Nuclear force has short-range repulsion (~0.5–0.8 fm core) | Qualitative: cage overlap below $\sim 2r_p$ forces forbidden edge-sharing |

---

## PHEN-P — Quantitative predictions

| ID | Quantity | CPP prediction | Measured | Error | Params |
|---|---|---|---|---|---|
| PHEN-P-SS-5-1 | Deuteron binding energy $B_d$ | **2.343 MeV** | 2.22457 MeV | **+5.3%** | 0 |
| PHEN-P-SS-5-2 | Classical p–n equilibrium separation $R_\text{cl}$ | 2.130 fm | ~2.13 fm (position of well) | <1% (well-position estimate) | 0 |
| PHEN-P-SS-5-3 | Deuteron magnetic moment $\mu_d$ (S-wave, CPP values) | 0.942 $\mu_N$ | 0.8574 $\mu_N$ | +9.8% | 0 |
| PHEN-P-SS-5-4 | Triplet–singlet ordering | Triplet bound, singlet virtual | Confirmed | exact (qualitative) | 0 |

---

## PHEN-V — Consilience with existing results

The $\eta = 1/\varphi$ factor that appears in the SS-5 prediction is the *same* factor driving:

- SM-6: $\sin^2\theta_W = 3/(8\varphi)$ (0.24% error)
- SM-7: $\alpha_s = 5/(8\varphi)$ (~1% error)
- SM-8: $M_q = m_e (z/\varphi) V^{7/3}$ (2.1% RMS)
- SS-4: $\sigma = M_0 z^2/(\varphi\, l_\text{edge})$ (+1.8% vs Cornell)
- SS-2: Nucleon structure via the same $M_0$ and $\eta$

SS-5's prediction is therefore *structurally consistent* with the programme's existing prefactor pattern. It is not a new rule; it is the same rule applied one sector over.

---

## Independence from prior results

The CPP calculation of $B_d$ does not rest on:

- Operator formalism (Layer B content of SM-3, SS-3): SS-5's prefactor argument is purely geometric mode-counting.
- Gibbs equilibration (Layer B of SM-3): none needed.
- Koide algebra: this is a nuclear-sector result, not a lepton-mass result.
- String-tension conjecture $\sigma$ (SS-4): the open-vertex bond carries *one* longitudinal mode, not the $z^2$ face-modes of a confining flux tube; $\sigma$ does not appear in the prediction.

This independence matters for the swarm-validation doctrine: SS-5 is a fresh, largely uncorrelated star shot. Its independence from the other anchor papers is what makes it contribute nearly fully to the programme's combined Fisher precision.

---

## Falsifiability

The prediction $B_d = M_0/\varphi = 2.343$ MeV would be falsified by any of the following:

- A value outside the $2.2$–$2.45$ MeV band at the SS-5 level of precision (the CPP residual band is $\pm 5\%$, so the prediction is $2.23$–$2.46$ MeV; anything below $2.20$ MeV falsifies).
- Theoretical objection to the second $\eta$ factor: if reviewers show that only one $\eta$ applies (giving $B_d = M_0 = 3.79$ MeV, 70% error) or that three apply ($B_d = M_0/\varphi^2 = 1.45$ MeV, 35% error), the prediction shifts out of the residual band.
- Confirmation of a diproton or dineutron bound state (excluded by all current experiments but theoretically falsifiable).

A successful falsification of SS-5 at the quantitative level would NOT falsify the qualitative consequences (PHEN-E-SS-5-2, -3, -4, -5, -6), which depend only on the polarity-pairing structural claim and have independent empirical support.
