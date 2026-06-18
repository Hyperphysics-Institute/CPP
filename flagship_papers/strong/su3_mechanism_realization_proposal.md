# Proposal: The Billiard-Ball Realization of the SU(3) Hop
### A mechanism note for the strong sector — prospectus, not yet a paper

*Prepared in the 1500-band (SF-5 / strong) window, June 2026. Corresponds to TODO-019.*

---

## 1. The one-sentence thesis

SS-1b derives the SU(3) colour algebra and its eight gluons as an exact identity from the three-ness of the tetrahedral colour vertices, and explicitly leaves open (`op:strong_primitive`) *why the strong force is tetrahedral hopping in the first place*. This paper proposes the physical answer: the colour hop is a charge-driven ZBW / SSV-gradient transition of a quark between cage vertices, and the trembling oscillation is the physical carrier that performs the generator. It supplies the mechanism beneath the algebra.

## 2. What is already proven (and must be cited, not re-derived)

- **SS-1b:** the eight DI-bit hopping operators on the three colour vertices (six edge, two diagonal) satisfy `[T^a,T^b] = if^abc T^c` with `T^a = λ^a/2` — exact SU(3), forced by three labelled vertices. This is theorem-level and shipped (reframed in SF-5).
- **SS-3:** that realisation is unique within the operator representation.
- **SF-5:** the strong-sector synthesis that carries both.

The proposed paper does **not** touch any of this. The algebra is settled. The paper lives entirely in the layer SS-1b marked open.

## 3. What is new (the paper's actual contribution)

1. **Colour = vertex occupancy.** A quark's colour is which cage vertex its central qCP is bonded to — a relationship to the frame, not a property painted on the quark. (Consistent with SS-1c's "one quark per base vertex" baryon picture.)
2. **The gluon is a vertex hop, physically carried by ZBW.** Each generator `E_ij` is realised as a charge-driven transition in which a quark leaves the superimposed (State 2) bond at one vertex and enters it at another, under the multi-body SSV gradient set by the occupancy of the other vertices. The zitterbewegung oscillation is the muscle that performs the move.
3. **Non-commutativity from inter-vertex coupling.** The reason two hops fail to commute — the heart of "non-abelian" — is that each quark's SSV gradient is conditioned by where the other quarks sit, so doing a hop at one vertex changes the conditions for a hop at another. This is the physical origin of the structure constants, mapped onto the substrate.

## 4. The honest open residual (must be registered, not hidden)

This is a **mechanism note, not a derivation**, and the paper must say so in its first page:

- The construction shows the ZBW/SSV picture is a *candidate carrier* rich enough to host the algebra; it does **not** yet show that the substrate geometry *forces* SU(3) rather than merely *permits* it. Closing that gap is closing `op:strong_primitive`.
- There is an unreconciled seam between two frames: SS-1b's *per-quark colour cage* (apex = that quark's central qCP, base = its three colour states) and the *baryon hTetra* used in the founder's mechanism notes (three quarks on three of four vertices, apex/fourth vertex an open eCP, up/down quarks cageless). The paper must either reconcile these or register the reconciliation as the open core.
- Every attempt this session to make the *raw* oscillation modes (uncoupled, un-hopped) *be* the generators failed — they form a torus (U(1)⁸), not SU(3). The algebra only appears once the moves are defined as inter-vertex hops. The paper should narrate that as the constraint, not bury it.

## 5. Falsifiability status

Honest assessment: the mechanism is **not yet falsifiable on its own** inside a stable baryon, because a stable baryon is an energy eigenstate — the hops are real as structure but silent as activity, so there is no live signal to test. The session's attempt to find an observable (extra short-lived configurations from minor bonding modes) came up *parametrically suppressed* — Fork A. The paper should state plainly that the mechanism's distinctive predictions, if any, live in *non-eigenstate* processes (beta decay, meson formation, high-energy collisions), and point to the beta-decay/chirality work as where the testable physics may actually be.

## 6. Proposed structure (≈ short paper, when written)

1. The open problem SS-1b left (`op:strong_primitive`) — stated precisely.
2. Colour as vertex occupancy (with the SS-1c baryon picture).
3. The hop as a ZBW/SSV-gradient transition — the mechanical sequence.
4. Inter-vertex coupling as the physical origin of non-commutativity.
5. Why raw oscillation modes are *not* the generators (the torus result) — the constraint that forces the hop picture.
6. The unreconciled cage/hTetra seam — registered honestly.
7. Where the testable physics lives (pointer to beta decay / chirality).
8. Status: mechanism, not derivation; `op:strong_primitive` remains open on the forcing question.

## 7. Recommendation

**Write it as a "mechanism note," not a flagship, and not yet to v1.0.** The contribution is real (it fills the layer SS-1b left empty with a concrete, corpus-consistent picture) but it is a *picture*, and the corpus discipline is to ship pictures as registered open mechanisms, not as derivations. My recommendation: draft it at v0.1 as a companion to SF-5 / SS-1b, with the honesty box of §4 front and centre, and hold it pre-SHIP until either (a) the cage/hTetra seam is reconciled, or (b) we decide the note's value is precisely in *posing* the open problem sharply, in which case it ships as an open-problem paper with that as its stated purpose. Either way it should not claim to derive what it pictures.

---

*This is a prospectus for review, not a draft of the paper. It records what the paper would claim, what it must not over-claim, and the open residual it must register. — drafted in the strong window for TLA review.*
