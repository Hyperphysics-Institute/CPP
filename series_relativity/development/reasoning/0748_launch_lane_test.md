# Reasoning capture — Patch 0748: the crowded-launch-lane tested — packing gives power laws

*Session 154. Tests the swarm's (Thomas + Copilot) "crowded launch lane" mechanism. Writeup:
`.../development/launch_lane_test_finding.md`. Toy+sim: `.../scripts/0748_launch_lane_test.py`. NO THEO.*

## Standard held

Copilot asserted the launch-lane order statistics are "plausibly harmonic" -> ln n. I held the
simulate-don't-assert standard and actually SIMULATED the mechanism (1D no-passing lane; 3D radial fill).

## Result (simulated)

- 1D no-passing lane: outermost reach CONSTANT (= L; first CP always reaches the end), later CPs pack
  inward. PSR_base ~ const -> n_s = 1 (HZ cliff). Mean reach linear-decreasing. Cannot hold n~1e79.
- 3D radial fill: R(n) ~ n^0.29 (~ n^1/3; finite-size sim slightly low) -> PSR_base ~ n^1/3 -> n_s=-1.
  A log would go 5.3->9.5 over the n-range; sim went 5.7->19.0: clearly power-law, not log.

Both excluded. The "order statistics -> harmonic" claim is a misapplication: positions/gaps of packed
points are uniform or power-law (R~n^1/d), NEVER harmonic. The harmonic series in probability comes from
records/coupon-collector counts (sum 1/k) or the entropic d ln(n!)/dn ~ ln n -- not from where particles
land under packing.

## Credit to the transcript
The negatives were CORRECT: geometry -> k^-2/3, diffusion -> Gaussian (not exponential, not harmonic),
linear -> n, (n-1)/n -> cliff. All consistent with 0747. Thomas's self-flag ("we chose the values we
wanted") was the right instinct. The architecture (count-driven, decoupled from gravity SSV) stands.

## The pattern (the real lesson, worth recording)
Across 0745-0748, EVERY mechanical/geometric/packing primitive gives a power law or constant -> all
excluded (n^q -> n_s = 1-6q; const -> 1; n^1/3 -> -1). The log appears ONLY from a genuinely statistical-
combinatorial source: configurational chemical potential mu = dF/dn, F ~ -T ln(W) (W = microstates),
i.e. d ln(n!)/dn ~ ln n; or records/coupon-collector. CPP's placement/geometry primitives keep
returning power laws. Getting ln n needs a microstate-COUNTING (entropic) ingredient -- a stack entropy
S(n) with dS/dn ~ ln n driving PSR_base -- which is a different KIND of thing than any placement rule.

## Honesty calibration
- Credited the correct negatives and the right architecture.
- Did NOT accept "plausibly harmonic"; simulated and found power-law (excluded).
- Did NOT over-kill: n_s=0.9649 remains viable & favored (only non-absurd value), not derived.
- Constructive + honest: identified that ONLY microstate-counting (configurational entropy / chemical
  potential) gives ln n, and that this is the sharp remaining target -- while being clear I do not have
  a CPP-native stack entropy in hand either. Did not substitute my own reverse-engineered rule.
- NO THEO; no prediction registered.

## Pointer
- THE target: a CPP-native configurational stack entropy S(n) with dS/dn ~ ln n driving PSR_base
  (microstate counting), the only route to a derived ln n. Clear of chirality. PCD = Perceive/Compute/Displace.
