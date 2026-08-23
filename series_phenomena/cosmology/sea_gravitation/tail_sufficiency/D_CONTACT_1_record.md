# **D-CONTACT-1: CONTACT-DRIVEN (10.0 SE) — THE FOUNDER'S MECHANISM IS SUPPORTED.** At fixed geometry and identical drive variance, raising the inter-DP contact rate LOWERS the bound fraction, in both arms, with opposite signs throughout: **free-DP formation tracks contact events.** R_c is measured for the first time in this programme (**0.0332–0.0360 contacts per CP per Moment ≈ 8.3 per Moment in a 250-CP Sea**) — and the counts turn out to be **POISSON, not bursty** (measured CV 0.350–0.359 against the Poisson benchmark 1/√λ = 0.347), **which resolves an apparent contradiction with the intermittency arc: the number of contacts per Moment is steady; it is their DEPTH that is heavy-tailed.** The worker's pre-declaration (CONTACT-DECOUPLED) is **WRONG** — six misses in seven

**Patch 3198 (22 Aug 2026). Executes `D_CONTACT_1_prereg.md` (Patch
3197, committed BEFORE any arm ran). Container; no Kila6 time.**

## §1 — The measurement

d_s = 4.636, n = 5, seeds {5, 11}; three matched-variance drives.

| arm | f_b | R_c (contacts/CP/Moment) | CV | ρ_swap |
|---|---|---|---|---|
| G | 0.44425 ± 0.00201 | 0.03316 ± 0.00012 | 0.359 | 0.4939 |
| S05 | 0.43740 ± 0.00072 | 0.03367 ± 0.00061 | 0.350 | 0.4806 |
| S2 | 0.44287 ± 0.00036 | **0.03601 ± 0.00026** | 0.351 | 0.4816 |

| arm | Δf_b | ΔR_c | signs |
|---|---|---|---|
| S05 | −0.00685 (3.2 SE) | +0.00051 (0.8 SE) | **OPPOSITE** |
| S2 | −0.00138 (0.7 SE) | **+0.00286 (10.0 SE)** | **OPPOSITE** |

**VERDICT (frozen words): CONTACT-DRIVEN** — both arms opposite in
sign, largest ΔR_c at 10.0 SE.

## §2 — What this establishes

**The founder's mechanism has its observable, and the observable
behaves as the mechanism predicts.** More inter-DP contact ⇒ fewer
bound pairs, at fixed spacing and fixed drive variance. Nothing
geometric and nothing about drive strength can explain it: the arms
differ ONLY in the tail shape of the drive.

**It also connects this week's two arcs for the first time.** D-TAIL-1
and D-TAIL-2 showed tail shape moves f_b and the calibration without
offering a mechanism. Here is the mechanism: **tail shape modulates
the inter-DP contact rate, and contact rate sets the free
population.** That is a chain from drive statistics to a physical
process to a calibrated number, and every link is now measured.

## §3 — A SPECIFICATION ERROR IN THE FROZEN PREREG, OWNED

§2 stated CV benchmarks — "CV ≈ 1 is Poisson" — that belong to the
INTERVAL distribution (exponential intervals have CV = 1). The
instrument measures the COUNT distribution, whose Poisson CV is
**1/√λ**, not 1. With λ = 8.29 contacts per Moment, the Poisson
benchmark is **0.347**, and the measured values are **0.350, 0.351,
0.359** — essentially exactly Poisson, ~1–3% above.

**The frozen CV thresholds are therefore inapplicable as written.**
They carried NO verdict (§4's readings rest solely on ΔR_c and Δf_b),
so **no verdict is affected**, and the correct benchmark is reported
as a diagnostic rather than substituted into a rule. The error is the
worker's and is recorded rather than quietly fixed.

## §4 — The physical synthesis (the part worth keeping)

The contact COUNT is Poisson — independent, unclustered, steady. The
force a CP experiences is strongly BURSTY (3183: 20–110× Gaussian
extremes). **Both are true, and together they say something specific:
the intermittency of this substrate lives in the DEPTH of encounters,
not in their TIMING.** Contacts arrive at a regular statistical rate;
what varies wildly is how close each one gets, and an r⁻² force turns
that depth variation into heavy tails.

**For the founder's picture this is a refinement, not a
contradiction:** ZBW-driven CPs do make intermittent contact with
those of other DPs, and that rate does control free-DP formation —
but the *rate* is steady, and the *violence* is what fluctuates.
**Stated as the reading of these numbers; the microstructure remains
unresolved at Moment cadence (the ZBW cycle is sub-Moment), so this
describes the aggregate process, not the individual event.**

## §5 — What this does NOT do

No DM claim: the DM engine has no drive (3196 §2), so nothing here
transfers to that lane. No change to Λ, d_s^emp, the 0.043 systematic,
the frozen 2.450, DISP-I3, or the ledger. R_c is a new observable, not
a new prediction — **nothing here meets the sky.** D-SALT-2 (the DM
bridge) remains chartered and unrun.
