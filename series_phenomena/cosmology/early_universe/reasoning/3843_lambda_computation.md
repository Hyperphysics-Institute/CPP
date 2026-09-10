# Reasoning capture — Patch 3843: computing λ

*Session 181, 9 Sep 2026, EU lane. Verbatim at-patch capture. Finding: `eu1_derivation/lambda_computation.md`. Verify 8/8.*

The debt was to compute λ, and the mechanism 3841 pointed at was the constraint that a CP displaces to one of twelve neighbouring grid points. So I computed that anisotropy first, exactly, before arguing about anything.

The natural measure is how badly twelve discrete axes represent a continuous direction: the covering function, max over the twelve of the dot product. Its covering radius is 37.3 degrees and it ranges over about twenty-two percent. Decomposing it gave a pleasing independent check — ℓ = 1 through 5 came out at Monte-Carlo noise and the leading anisotropy at ℓ = 6, which is T-1's result recovered from a completely different function, the covering function rather than the census. That was worth having for its own sake.

The number is λ_hard = 0.052, and taken as a potential it puts the mode at m/H = 7×10⁴, which is the register spring's wall to within a factor. So the naive reading of "the lattice grips the orientation" kills C-4 outright, exactly as 3841 §4 warned. For a while that looked like the session's answer and I was prepared to write it.

Then I made myself ask whether the covering anisotropy is actually a potential, because a mass needs a restoring force and I had been sloppy about which physical slot the number occupies. Three things came out, and the third is the one that matters.

The first is that at single-DP order the energy is exactly flat. The twelve axes are icosahedrally equivalent, and a DP axis joins two grid points so it is quantised to those twelve; a rigid reorientation of the mean director is therefore not a rotation of individual DPs but a repopulation among equivalent states, and with equal per-axis energy the total does not depend on the populations at all. There is no first-order potential to be had.

The second is that the constraint is on displacement, which is a mobility. An orientation-dependent displacement efficiency makes relaxation direction-dependent; it does not pull the director back toward a preferred orientation. A Goldstone with anisotropic damping is still massless, because the k → 0 uniform rotation still costs nothing, and that is what the gap means.

The third is decisive and I did not see it coming. The displacement is the only operation in the whole protocol that breaks continuous rotational symmetry — the register computation is exactly rotation-covariant, since SSV_abs is a sum of magnitudes and SSV_net is a vector sum. And in the homogeneous saturated era the displacement does not happen: S-HENGINE-HELD §2.2 establishes SSV_net = 0 exactly, because the twelve icosahedral neighbour vectors sum to zero. That is T-1's dipole cancellation, which I verified as an identity at 3820. So the operation that would gap the Goldstone never fires during inflation. λ is not of order λ_hard; it is proportional to however far SSV_net departs from zero, and that departure is itself the perturbation.

That is now the third independent job T-1 has done. It was delivered as a symmetry curiosity with no observable attached, re-graded to load-bearing for the mass two patches ago, and is now the reason the symmetry breaking is idle. A result that keeps turning out to be load-bearing in unrelated places is usually telling you something, and I flagged it for the panel on that basis.

For what remains I wrote λ ≈ λ_hard x^p with x the fractional departure from cancellation, and I want to be clear with myself that this is a scaling ansatz and not a derivation. But it does what a good ansatz should: it isolates the risk into a single integer. At the perturbation scale, p = 2 leaves m/H at 3.2 and C-4 fails, while p = 3 or more clears comfortably. Set against the register spring's 1.3×10⁵, the candidate has gone from eleven orders away from death to one integer away, with the pessimistic branch a factor of three rather than a factor of a hundred thousand.

I made a point of not writing this up as though C-4 had cleared. It has not. p is uncomputed and one of its plausible values kills the candidate. What changed is the shape of the risk, and that is worth saying precisely rather than optimistically, because a factor of three is exactly the regime where wishful arithmetic does the most damage.
