# The founder's PD-007 challenge computed — his bet on irregular patches is CONFIRMED, and his force rule is confirmed with one sharp refinement: the aggregation is not spread along bonds but is confined ENTIRELY to the mismatch walls, because a domain interior cancels his forces exactly. The walls are the only thing still moving. But the wall field's spectrum is PEAKED, not scale-free — so C-3 supplies slowness and collectivity and still does not supply scale invariance

**Patch 3829, Session 174, 9 Sep 2026. Lane: EU.** Founder text verbatim: `founders_voice/founder_picture_frustrated_patches_2026-09-09.md`. Verify `scripts/3829_frustration_patch_dynamics.py` (7/7). Reasoning `reasoning/3829_frustration_patch_dynamics.md`. Nothing adopted; no constant minted (PD-007); PRED-C-96 untouched; 3710 not retired.

## §0 Method and its honest limits
The 600-cell's local shell is z = 12 with mutually-adjacent neighbours (3827). The 3D lattice in that same frustration class is **FCC** — coordination 12, triangulated, and the textbook geometrically-frustrated Ising antiferromagnet. Computations run on FCC at L = 24 (6912 sites, periodic), which gives bulk statistics the 120-vertex 600-cell cannot. **This is a proxy for the local frustration physics, not the 600-cell itself**; conclusions about *bulk domain behaviour* transfer, conclusions about *global topology* do not, and none are claimed.

## §1 His bet on irregular patches — CONFIRMED (verify T4, T5)
Annealing from random reaches a frustrated fraction of **0.359**, just above the forced bound of 1/3 (3827). The ordered reference state (type-I layered, alternating (001) planes) saturates the bound **exactly** at 0.33333 — verified, and a satisfying independent confirmation of 3827's triangle argument from a completely different direction.

The relaxed state is **not** a single regular arrangement. Classifying each site by which of the three stacking orientations it locally realises gives populations of roughly **0.35 / 0.39 / 0.26** — all three present in comparable measure. The lattice breaks into patches of different stacking orientation with mismatch surfaces between them. **That is exactly the founder's bet, and the reason he gave for it is the right reason:** because some edges necessarily join like charges and some join unlike, no single global arrangement is available, and the system fragments.

## §2 His force rule — CONFIRMED, with a refinement that matters (verify T3, T6)
Implementing his rule literally (repel along like-charge bonds, attract along unlike-charge bonds, unit vectors along the twelve bond directions):

**In a perfect domain interior the net force is EXACTLY zero.** Not small — identically zero, max |F| = 0.00×10⁰. The reason is the same symmetry that gave T-1 its result: within a type-I domain each site has 4 in-plane like bonds (repulsive) whose directions sum to zero, and 8 out-of-plane unlike bonds (attractive) whose directions also sum to zero. The attractions and repulsions he describes are both present and both cancel.

**All of the net force lives on the walls.** In the annealed state, mean |F| in true domain interiors is 0.00×10⁰ against 1.05 on non-interior sites, and the wall sites carry **100.0%** of the total force.

So the refinement is this: he expected aggregation *along the oppositely-charged edges* and rarefaction *along the like-charged edges*, distributed through the bulk. What the computation gives is that in the bulk those two effects annihilate one another exactly, and the aggregation and rarefaction he predicts survive **only where the pattern fails to be locally regular — at the mismatch walls.** His mechanism is right; its support is the wall set, not the bond set.

**This answers the standing picture question in the affirmative.** Asked whether the walls are what is still moving after everything else has settled: yes, and exactly so. The interiors are force-balanced by symmetry and are static; the walls carry every unit of net force in the system.

## §3 The spectrum — the honest negative (verify T7)
C-3 owes two things (3827 §5): a bridge to the end condition, and a near-scale-invariant spectrum. This patch tests the second.

The structure factor of the wall field is **peaked at finite k**, with S_max exceeding the small-scale value by a factor ~21. That is a **characteristic scale**, not a power law. Domain patterns of this kind carry one length — the typical patch size — and a peaked spectrum is what a single length produces.

*Limit stated:* the run does not cleanly resolve how that scale *evolves*, because L = 24 is small and the wall fraction changes with annealing depth; no coarsening exponent is claimed. What is robust is the peak's existence.

**Consequence for C-3:** frustration supplies slowness and collectivity for free — the two properties every prior candidate lacked — and supplies scale invariance not at all. A peaked spectrum seeds a feature, not the observed near-power-law P_ζ. C-3 is therefore **not** a solution to the amplitude problem as it stands.

## §4 Two hazards C-3 inherits by joining a known class
Registering frustration walls as a ζ candidate places C-3 in the class of **topological-defect seeds**, which carries two well-established observational problems the corpus should confront now rather than later:
1. **The domain-wall problem.** Stable domain walls are cosmologically catastrophic — their energy density redshifts more slowly than matter or radiation and overcloses the universe unless they annihilate or inflate away.
2. **Defect seeds are excluded as the primary source of CMB anisotropy.** Active, incoherent seeds do not reproduce the observed acoustic-peak structure; this is why cosmic-defect models were ruled out as the dominant perturbation source. A defect-like C-3 inherits that exclusion.

## §5 The dilemma this creates, stated plainly
These two hazards and the seeding requirement pull in opposite directions, and CPP's own results tighten the vice:
- **If the walls survive**, C-3 inherits the domain-wall problem and the defect-seed exclusion of §4.
- **If the walls annihilate**, they seed nothing. And CPP's own ignition computation (3805) says every start pairs into a neutral sea **within 15 Moments** — before a single e-fold. On that result these walls are gone essentially immediately, which is comfortable for §4 and fatal for C-3's candidacy.

**Either the walls persist long enough to seed, in which case they must clear the defect exclusion; or they pair away in fifteen Moments, in which case they seed nothing.** No computation here decides which, and the honest position is that C-3's prospects are now materially worse than they looked at 3827, not better. That is worth saying plainly one patch after registering it with enthusiasm.

## §6 Standing
- **Founder's bet CONFIRMED** (irregular patches, all three orientations, frustration forced just above the 1/3 bound).
- **Founder's force rule CONFIRMED and REFINED:** interiors cancel exactly; 100% of net force is on the walls; aggregation is a wall phenomenon. Standing picture question answered: the walls are what is still moving.
- **C-3's spectrum debt: NOT discharged — peaked, not scale-free.** C-3 does not solve the amplitude problem as it stands.
- **C-3's end-condition debt: still open**, and now sharpened by §5's dilemma (persistence vs the 15-Moment pairing result).
- Two inherited hazards registered (§4).
- **Recommendation:** before further work on C-3, settle §5 — do these walls survive the pairing of 3805, or not? That question is cheaper than any spectrum computation and it decides whether C-3 is alive.
- T-1, the e-fold budget, PRED-C-96: all untouched. C-2 (edge) is unaffected by this patch and remains the better-standing candidate.
