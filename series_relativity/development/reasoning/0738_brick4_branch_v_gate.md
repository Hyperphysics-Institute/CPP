# Reasoning capture — Patch 0738: Brick #4, Branch-V construction adopted + spectrum gate passed (toy)

*SR-1 rederivation pass, Session 154. Brick #4 (handover task item 3 + the spectrum thread). Decision
out of the Q2 fork (0737). Framing: `series_relativity/development/brick4_branch_v_adoption_and_toy_spec.md`.
Toy + verify: `series_phenomena/cosmology/early_universe/scripts/0738_brick4_spectrum_gate.py`.*

## The decision and the one correction that mattered

Thomas chose "Fixed l_P_base + H axiom" as best-of-both-worlds. The load-bearing correction I made
before adopting: **this is Branch V, not Branch F with a bonus.** Branch F's free dissolution of the
first-Moment infinity required the *operative reach ceiling* to be the fixed finite length. Once H can
boost PSR_base, the operative reach (c_eff) is state-dependent = Branch V cosmologically. The tell:
Thomas had to add the finite-patch IC to kill the infinity — precisely because fixing the UNIT
l_P_base no longer does that job once PSR_base is boostable. So the infinity-killing work is done by
the IC, not the fixed length. What the fixed unit DOES buy (and why keep it): present-epoch anchoring
— unboosted, baseline-SSV ⇒ l_P_eff = l_P_base = standard Planck length ⇒ k = l_P_base³/E_P ⇒ five SR
predictions intact (Brick #2 invariants). This is consistent with Thomas's own framing ("constant c
is a relative term").

## Division of labour — the key reasoning is that the pieces are NON-substitutable

- Finite patch = regulator + seed (ballistic spreading ≤ c_eff, NOT an engine).
- H-axiom = the exponential engine.
- CLT/ZBW = the statistics (Gaussian, stationary).
- qCP/qDP = the morphology.
- early high c_eff = the horizon solution (no e-folds needed for horizon).
- interlock (stationary injection + constant-H freezing) = the spectrum.

Reframe of "is inflation needed?": for the HORIZON, no (high c_eff). For the SPECTRUM, yes — a
constant-H freezing phase is needed to convert stationary temporal injection into spatial
scale-invariance. **Inflation in CPP is repurposed as the spectrum generator, not the horizon fix.**

## Why the interlock gives scale-invariance (the mechanism, stated honestly)

CLT does NOT give scale-invariance by itself (independent kicks summed are white = wrong shape). The
mechanism is: each comoving mode freezes at horizon crossing with the local fluctuation amplitude. A
STATIONARY injection (same statistics every Moment during the superposed phase — which CLT+constant
ZBW physics provides) under a CONSTANT-H (exponential) background imprints CONSTANT power per log-k =>
scale-invariant. Analytically n_s − 1 = d ln σ²/dN. A slow roll-off of σ²/H near the end
(superposition thinning) ⇒ n_s < 1 (red, correct direction). This is the SAME freezing mechanism as
standard inflation; CPP's contribution is a concrete engine (H) + concrete stationary source
(ZBW/CLT), not a new reason for scale-invariance.

## Toy results (seed 20260603, all PASS)

- A: additive excess-kurtosis −0.012 at N=512 (Gaussian) vs multiplicative ~1.6e5 (heavy-tailed).
- B: stationary→n_s=1.000; analytic β=−0.035→predicted 0.965, measured 0.965; roll-off→n_s≈0.965 in
  Planck band; skewness ~0.036 (small f_NL).
- C: N_efold=(1/3)ln(N_CP/13); observable-universe N_CP~1e80 → ~60 e-folds. Depth sets total, H sets
  rate — decouples the two tunings Thomas worried about.

## What PASS means (the honesty boundary)

PASS = internal coherence + capability. NOT a parameter-free prediction of n_s. The tilt roll-off is a
free function; A_s is one tuning (as in standard inflation). I refused to let "capable" become
"predicts." The two upgrades that would make it a prediction: (1) derive the roll-off from the
superposition-thinning law (n_s tuning → prediction); (2) derive σ_ZBW → A_s. Plus the cheap Δc filter
(density-dependent c_eff vs varying-constants bounds) which could falsify the whole density-c_eff
picture and should be run first.

## High-risk debt I flagged rather than claimed

Degeneracy pressure as an H-bonus is NOT free: Fermi pressure is precisely measured (Chandrasekhar
1.4 M_sun, WD/NS mass-radius). H-anti-collapse must reproduce those numbers if replacing, or risk
double-counting if adding. AND it must be kept distinct from Patch 0731's occupancy-fraction f→1
(stacking-per-GP ≠ occupancy-across-GPs) or the two stories collide.

## Conventions

- NO THEO (program decision + conditional numerical evidence). No new prediction/term registered
  (the toy is capability evidence, not a parameter-free result). H-axiom status changed in its
  evaluation doc (evaluated→adopted-working, gate-passed-at-toy). Verify script bundled
  (computation present). Clear of chirality. PCD = Perceive/Compute/Displace.

## Pointer
- Next (both cheap, parallel): the Δc bound filter (could falsify), and the superposition-thinning
  roll-off law (upgrades n_s tuning→prediction). Then fold semantics into SR-1 and dispatch to review.
