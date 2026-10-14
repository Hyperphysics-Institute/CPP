# The Census Around a Moving CP: if the Census Obeys GR-1j's Wave Equation, a Light-Speed Relay Makes It Exactly the Liénard–Wiechert Potential, Flattened by 1/γ (4410's Contraction). A Raw Vector Sum of Arrivals Is Lopsided at First Order, Which Would Make Bound Pairs Drive Themselves, and Which Is What the Coasting Conjecture CONJ-FP-1 Needs. Its 2895 "Closed by Inspection" Rested on a False Step

**Patch:** 4411. **Lane:** foundations, with GR and EM. **Session:** 242. **Claude-initiated** (4410 owed item (b), first
part); no new founder input.
**Script:** `series_standard_model/code/4411_census_from_a_moving_cp.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the mathematics, and
required: saying the 1/R weight is assumed, reopening 2895's Condition B verdict, correcting the record-inconsistency claim,
replacing the pair-distortion claim and its wrong citation, restating the way through as two receiver rules, and the D-9
entry. All six are taken in.

## 1. The question

4410 found that a moving crystal must contract along its motion, with the classical mechanism a moving charge's field,
relayed at light speed, flattened by 1/γ. Owed: does CPP's DI-bit relay give that? First step: what does a light-speed relay
give around a CP moving uniformly through the absolute frame?

## 2. The setup

A CP moving at v broadcasts DI-bits each Moment; they travel at light speed from where it was. At a receiving GP they
arrive from the retarded position (distance R, direction n), compressed by 1/(1 − n·v) per receiver Moment (more ahead,
fewer behind), for an emitter isotropic in the absolute frame. Two ways to build the receiver's count:
- **(i) a flux:** each arrival weighted by inverse-square spreading, 1/R² (what simply counting arriving bits gives);
- **(ii) the census:** each arrival weighted 1/R from its emission point. **This weight is assumed, not derived from the
  DI-bit rule:** it is the retarded solution of GR-1j's wave equation for Δ|SSV| (whose static sector is 1/r). AP-4
  defines SSV_abs as a sum over arrivals; why that sum would carry 1/R per arrival rather than 1/R² is not shown. The
  model also treats arrivals as coming straight from the retarded CP position, while AP-4's relay is multi-hop.

## 3. Results (script)

Distances ahead and behind at which each count equals its value one unit to the side:

| v | (i) flux: ahead / behind | (ii) census: ahead / behind | 1/γ |
|---|---|---|---|
| 0.001 | 0.99950 / 1.00050 | 0.999999 / 0.999999 | 0.999999 |
| 0.1 | 0.9487 / 1.0488 | 0.99499 / 0.99499 | 0.99499 |
| 0.5 | 0.7071 / 1.2247 | 0.8660 / 0.8660 | 0.8660 |
| 0.9 | 0.3162 / 1.3784 | 0.4359 / 0.4359 | 0.4359 |

- **The census (ii) is exactly the Liénard–Wiechert potential**: R(1 − n·v) equals the present-position distance
  √(X² + (1 − v²)ρ²), so its surfaces of equal value are Heaviside's ellipsoid (checked at seven angles), front-back
  symmetric at all orders and flattened by exactly 1/γ. For co-moving test charges the full force is exactly −(1 − v²)
  times the gradient of this potential, so **the census gradient alone gives equal and opposite forces within a co-moving
  pair and the 1/γ equilibrium shape**; the vector (magnetic) channel supplies only the overall (1 − v²) factor and the
  dynamics. **So if the census obeys GR-1j's wave equation for moving sources, CPP's census channel supplies 4410's
  contraction.**
- **The flux (i) is lopsided at first order** (ahead ~√(1 − v), behind ~√(1 + v)).
- **A raw vector sum of arrivals** (each n/R², compressed), computed on the axis at unit present distance, gives (1 − v)
  ahead and (1 + v) behind, while the true field of a uniformly moving charge is (1 − v²) on both sides.

## 4. What the lopsided channel would do

If forces between CPs followed a raw vector sum of arrivals, then for two CPs moving together, one behind the other, the
trailer would feel (1 + v) and the leader (1 − v). Their mutual pull stays the same at first order, but the pair as a whole
gets a net push of about 2v, forward if they attract, backward if they repel: **a self-drive proportional to the pair's
speed through the absolute frame.** In CPP's dynamics (displacement set by SSV_net) that has the same form as CONJ-FP-1's
coasting drive. The consequence is that bound and free matter would coast differently: atoms would drive themselves
relative to free particles, depending on their internal binding, which is grossly excluded. (For uniform co-motion,
Liénard–Wiechert forces are exactly equal and opposite with constant field momentum, so the equal-force criterion is valid
here. The direct experimental tests of forces between co-moving charges are Trouton–Noble and Trouton–Rankine.) It would
also contradict the founder's 4410 principle: the same force at the same measured distance in a moving crystal.

## 5. The tension with CONJ-FP-1, and the 2895 verdict

**CONJ-FP-1** (the founder's 2 August 2026 ruling,
`founders_voice/founder_mechanism_roundtrip_timing_inertia_2026-08-02.md`) makes inertial coasting come from a round-trip
asymmetry: a moving CP's DI-bits reflected back from the DPs of the sea return sooner from ahead than from behind (Δt =
4rv/(c² − v²), first order in v). Its Condition B records that under Liénard–Wiechert propagation the drive is exactly zero,
so "the mechanism requires the relay to NOT reproduce LW structure".

**2895 closed Condition B "by inspection"** (branch1_verification.md §5), on the reasoning that a retarded relay cannot
give the Liénard–Wiechert cancellation. **This patch shows that premise is false:** Liénard–Wiechert is itself built from
retarded arrivals (§3). Whether a ballistic, retarded relay is Liénard–Wiechert depends on what the receiver does with
the arrivals: a vector sum or flux is not; a census gradient is. So **Condition B reduces to the receiver-rule question and
is reopened**, not closed. The 2889 automaton result (A_vol ≈ −1) measured a vector-sum observable; it agrees with (i) and
is not evidence against the census result.

**Record note:** the CONJ-FP-1 entry in frontier_sectors/CONJ.md (line 477) never recorded 2895's closure and still
describes the moving-source test as what settles Condition B, while the mobile-sea records say CLOSED-VERIFIED (2895).
(transport_family_unification.md's "OPEN" is from 2890, before 2895, and is historical.) The clean M = 128 discriminant run
owed since 2889 was never filed.

**The way through, restated:** a DI-bit carries only an origin-GP address, and the DP-sea reflectors are themselves made of
CPs, so nothing in the messenger distinguishes "a CP's own reflections" from "another CP". The workable distinction is a
**receiver rule**: DPs (at rest in the sea) respond to the vector sum of arrivals (retarded, not LW), while a CP's force
follows the census gradient (LW). That is two rules, probably an axiom-level question. One empirical constraint bears on
it: detectors at rest are reported to see the field of a uniformly moving relativistic beam pointing at its present
position (a 2015 experiment; citation to be verified), and DPs are at-rest responders.

## 6. What stays open

- **The 1/R weight:** why AP-4's sum over arrivals carries the census weight 1/R rather than 1/R² (or that the census obeys
  GR-1j's wave equation for moving sources).
- **The vector and magnetic channel** (4410 (b) continued; overall factor and dynamics).
- **The receiver rule** (census gradient versus AP-4's vector sum; the two-rule question) and CONJ-FP-1 Condition B,
  reopened.
- **Records:** CONJ.md's CONJ-FP-1 entry lacks the 2895 status, and 2895's inspection argument needs re-adjudication; the
  M = 128 run.
- **Darwin:** the Darwin adjudication finds no first-order retardation term (Liénard–Wiechert-type), which conflicts with
  CONJ-FP-1's first-order drive; reconcile.
- **Cross-link:** TODO-4364-PREFFRAME asks for exactly this moving-source rule; 4411 supplies its scalar sector.

## 7. Question to the founder (physical picture)

Two charged CPs move together through the absolute frame, one directly ahead of the other. **Does the one behind feel
exactly the same push from the one ahead as the one ahead feels from the one behind?** Your 4410 principle (the same force
at the same measured distance) says yes, and the census relayed at light speed gives exactly that. Your 2 August
round-trip ruling makes inertia come from a front-back difference in what a moving CP gets back from the DPs around it,
which sit at rest in the sea while the CP moves through them. **Is that the difference that matters, a moving CP against
DPs at rest, rather than two CPs moving together?**

## 8. PD-008

- **Convenient branch, marked:** "CPP's relay gives Liénard–Wiechert." It does if the census obeys GR-1j's wave equation
  (the 1/R weight per arrival is assumed); the vector part is not shown.
- **Inconvenient result surfaced:** a raw vector sum of arrivals (the natural reading of SSV_net) is lopsided at first order
  and would make bound pairs drive themselves; the coasting conjecture needs that lopsidedness; and 2895's closure of
  Condition B rested on a false step. Stated, not resolved.
- Nothing registered.
