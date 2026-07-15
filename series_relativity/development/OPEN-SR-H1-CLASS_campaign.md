# OPEN-SR-H1-CLASS campaign — geometric half ANSWERED (continuum-conditional), mechanism half PRE-REGISTERED

**Opened:** 15 July 2026, Patch 2482. **v1.1:** Patch 2484 — first 4 slots folded.
**v1.2:** 15 July 2026, Patch 2486 — DeepSeek return folded; **ROUND 1 COMPLETE: 5/5 slots,
4 unique contents (Copilot verbatim-identical to Gemini, anomaly recorded, founder confirmed
posting order), ALL RATIFY (with changes/calibration); every required change from every
return adopted.**
**Registry entry:** `frontier_sectors/SR.md` § OPEN-SR-H1-CLASS.
**Verify script:** `series_relativity/code/2482_exclusion_family_exponents.py` (stdlib, all checks pass).
**Status: geometric half YES, now explicitly CONTINUUM-CONDITIONAL (§2a); NOTHING promoted;
mechanism phase pre-registered below (M1–M7, K1–K4) and gated on founder ratification of the
single-candidate commitment (§3a).**

---

## 1. Disclosure (G7 — read first) [v1.1: augmented per panel A-findings]

The handover warned: "the pull toward 'find the f² geometry and win the flagship back' is
precisely the pressure that produced the k defect." The following disclosure exists because
of that warning.

**1a (enumeration order).** While designing the enumeration frame — before any mechanism
work, and before this file was written — the enumerating instance observed that the family
"f-neighborhoods of central loci" makes the exponent trivially equal to the codimension,
and therefore that the codim-2 member hits n = 2. The observation could not be un-seen:
**the geometric result was found by systematic enumeration, but the enumerator knew the
target while enumerating.**

**1b (family choice — added at panel instruction).** No other comparably systematic family
was examined before settling on this one, and the continuum 4-ball baseline was adopted
from H.1's own Model-3 setup without independent justification. The panel is right that the
contamination therefore extends to the choice of arena: a continuum ball yields clean
polynomial fractional volumes of exactly the kind capable of matching (1−f²)²; the actual
substrate cell is a flat-faced polytope. Sharper still (DeepSeek): the family E_k(f) was
chosen because it yields integer exponents n = k, making n = 2 appear naturally at
codim-2 — the family selection, while systematic, was itself target-informed. This is now
a derivation obligation (M4), not a modeling convenience.

**1c (burden design — added at panel instruction).** The mechanism burden M1–M7 and kill
conditions K1–K4 were designed AFTER the target was known. The panel must treat the burden
as potentially biased toward selecting the codim-2 tube unless each element is
independently justified — which is precisely why the burden (now M1–M9) has been made maximally
demanding (every panel-proposed addition was adopted) and why K2 routes the eventual
mechanism claim back through the panel.

## 2. The geometric result (verified, C1–C3 in the script)

**Family.** Regions of the round 4-ball (radius l_P) of the form
E_k(f) = {x : |P_k x| ≤ f·l_P}, where P_k projects onto k of the 4 coordinates — the
f-neighborhood of a central locus of codimension k: k = 1 slab, k = 2 tube-about-2-plane,
k = 3 tube-about-axis, k = 4 central ball.

**C1 (exponent law).** Small-f volume exponent = codimension: n = k for k ∈ {1,2,3,4}
(closed forms + fixed-seed MC). **Codim-2 is the unique n = 2 member of this family.**
H.1's prior models slot in as n = 1 structures (Models 1/2) and the boundary-anchored cap
n = 5/2 (Model 3). The corrected exponent set {1, 1, 5/2} brackets 2 as the reopening
predicted.

**C2 (the identity).** The codim-2 tube of radius exactly d = f·l_P has exact fractional
volume V_excl/V₀ = 2f² − f⁴ = 1 − (1−f²)², hence V_free/V₀ = (1−f²)². Under SR-1's strain
rule (V ∝ r⁴, ε = l_P/r − 1):

    ε(f) = (V_free/V₀)^(−1/4) − 1 = (1 − f²)^(−1/2) − 1 = γ_SR(f) − 1

exactly, at all orders in f — **in the continuum-ball model** (see §2a) — machine-precision
verified over f = 0.01–0.99. Three features are individually nontrivial within that model:
(i) n = 2 unique in the family; (ii) coefficient exactly ½ with radius = the displacement
magnitude d itself; (iii) every higher-order term matches γ automatically (the tube's −f⁴
is precisely what the fourth root requires; a generic n = 2 profile fails this).

**What C2 is NOT.** A derivation of γ. The profile (1−f²)² exists by inverse construction;
C2 adds that it is realized by a natural geometric object. Whether CPP **selects** that
object is the whole question.

### 2a. Scope conditions (v1.1 — panel D-findings, all adopted)

1. **Continuum-conditional.** The identity is exact for the round 4-ball. The substrate's
   actual Voronoi cell is a polytope bounded by flat faces (12-neighbor coordination). For
   a polytope arena the tube–cell intersection is piecewise-polynomial, and — sharpening
   the panel's point — the correction enters at LEADING order: the f² coefficient equals
   π·A₂·l_P²/V_cell (A₂ = central 2-section area), which equals the required 2 only for
   the ball. Countervailing substrate fact, to be settled not chosen: the PSR is by
   definition a *sphere* radius — if the displacement arena is the PSR insphere
   (isotropic budget), the ball is exact by definition and no polytope correction arises.
   Which arena the postulates give is derivation obligation **M4**.
2. **Strain-rule-conditional.** The identity holds under SR-1's V ∝ r⁴ / ε = l_P/r − 1
   constitutive rule, which is a minimal ansatz (per the corrected SR-1 abstract), not a
   geometric necessity. Any modification breaks the exact match.
3. **Not a classification theorem.** Geometries outside the family (non-axis-aligned or
   anisotropic tubes, curved loci, weighted projections, unions) can also produce n = 2.
   The claim is existence-of-a-natural-object, not n = 2 ⇒ codim-2 tube.
4. **Coefficient-conditional.** Radius λ·d with λ ≠ 1 collapses the identity; λ = 1 must
   be DERIVED (M5 bans absorbing any constant to rescue it).
5. **Coordinate alignment.** The family privileges coordinate subspaces; a rotationally
   invariant ball does not. The mechanism must derive the plane coordinate-independently
   or show the postulates privilege the alignment (folded into M3).
6. **Unstressed-arena-conditional (DeepSeek).** The identity uses the UNSTRESSED l_P as
   both arena radius and exclusion-radius scale. For a pre-stressed aggregate
   (background SSV ≠ 0, PSR_eff = l_P/g_bg < l_P) the two natural scalings fork:
   exclusion radius d = (v/c)·PSR_eff (local) preserves γ at every background stress
   with exactly multiplicative composition g_bg·γ(v); d = (v/c)·l_P (absolute) breaks
   γ and lowers the local speed ceiling to c/g_bg. Demonstrated (not resolved) in
   `code/2486_stressed_arena_fork.py`; resolution is mechanism obligation **M9**.

## 3. Mechanism phase — PRE-REGISTERED (no mechanism work has been done)

**The question.** Does CPP's postulate set, for a uniformly moving CP aggregate, derive ALL
of M1–M9:

  **M1 (distinguished 2-plane, unique).** A distinguished 2-plane per moving aggregate —
  and the derivation must show it is the CANONICAL one: exactly one 2-plane is
  postulate-distinguished, not one of several with the winner chosen by hand.
  **M2 (exclusion rule).** Forbidden displacement targets are exactly those whose
  projection onto the distinguished pair is ≤ the obligatory displacement scale — the full
  symmetric neighborhood, not a half, sector, or weighted variant.
  **M3 (radius + projection, tightened).** Radius exactly d = v·t_P (coefficient 1, not
  λ·d), derived; the identity must survive the SAME 4D→3D projection treatment as
  corrected SR-1, with explicit statements of (i) the τ-invariance decomposition used,
  (ii) how the distinguished plane interacts with the Absolute-Moment axis, (iii) how the
  projection acts on the exclusion region; (iv) explicit verification that the 4D tube
  projects, under that same treatment, to a 3D structure still carrying exclusion scale
  d = v·t_P (DeepSeek). The plane must be derived coordinate-independently or the
  coordinate alignment shown postulate-privileged. No bespoke re-projection.
  **M4 (arena/polytope constraint — new, panel).** Derive from the postulates whether the
  displacement arena is the PSR insphere (ball exact by definition) or the full Voronoi
  polytope. If the polytope: compute the tube–polytope intersection exactly, including the
  leading-order coefficient π·A₂·l_P²/V_cell, and show the deviation from γ is zero or
  derive its physical status. "Assume the ball" is not available.
  **M5 (prefactor ban — new, panel).** No constant may be absorbed into any normalisation
  to make any coefficient come out right. The √(2/φ)-class move is banned by name. One
  auxiliary parameter, length scale, or selection rule not already in the core postulates
  = fail.
  **M6 (micro-to-macro bridge — new, panel).** The postulates govern single-CP
  displacement. The aggregate-level codim-2 exclusion must be derived from single-CP rules;
  inserting collective relativistic kinematics by hand = fail.
  **M7 (aggregate-independence — new, panel).** The same plane and rule must follow for
  ALL uniformly moving aggregates — any CP composition, internal ZBW structure or phasing,
  motion history, SSV environment. Reliance on a single-CP idealization or a cherry-picked
  special aggregate = fail.
  **M8 (frame-consistency — new, DeepSeek, folded with a circularity caveat).** The plane
  identification must be consistent under composition of motions as computed in the
  absolute lattice frame: for aggregates in relative motion, the construction applied to
  each must yield mutually consistent descriptions, with the observed relativity of
  inertial frames emerging as an OUTPUT. Caveat, recorded so the requirement cannot be
  gamed in reverse: demanding a priori Lorentz covariance of P → P′ would presuppose the
  Lorentz group — the very structure under derivation — so M8 is stated lattice-natively;
  a mechanism that IMPORTS covariance to satisfy M8 fails K3.
  **M9 (stress-composition — new, DeepSeek).** Derive which radius the exclusion scales
  with for a pre-stressed aggregate: (v/c)·PSR_eff (local — preserves γ, multiplicative
  composition with the background factor) or (v/c)·l_P (absolute — breaks γ, ceiling
  c/g_bg). The fork and its consequences are pinned in
  `code/2486_stressed_arena_fork.py`; the answer must come forward from postulates. If
  the derivation lands on the absolute branch, the identity fails for stressed
  aggregates and K1 fires.

**Candidate 2-planes (recorded for completeness; see K4 — no menu-shopping):**
  (a) the (ê_motion, τ̂) motion–time plane; (b) the ZBW rotation plane;
  (c) the (ê_motion, ê_ZBW-axis) plane; (d) an SSV_abs-broadcast-selected plane
  (C0-clause dependent). Reading R1 ("the obligatory drift pre-empts a floor of the
  in-plane budget each Moment") remains a reading, not a derivation.

### 3a. Single-candidate commitment (K4 instrument — **RATIFIED BY FOUNDER, 15 July 2026, Patch 2487**)

Per the panel's anti-shopping mandate, exactly ONE candidate is committed before mechanism
work. **Proposed commitment: candidate (a), the (ê_motion, τ̂) plane.** Rationale, stated
forward and recorded before any mechanism work: γ is universal (every aggregate dilates
identically), so the distinguished plane must be constructible from the motion state plus
universal lattice structure alone; (a) is the only listed candidate satisfying this by
construction — (b) and (c) vary with internal ZBW configuration and would violate M7
unless an alignment mechanism is separately derived; (d) is blocked pending the A3′/C0
source clause. This rationale references universality (an M7 requirement), not the target
exponent. **RATIFIED** — founder ruling, verbatim: "ratified." (15 July 2026, in response
to the v1.2 round-completion notice.) **Candidate (a), the (ê_motion, τ̂) motion–time
plane, is now BINDING under K4.** Evaluating any other candidate in the mechanism session
— including "quick checks" — voids the round per K4.

**Kill conditions (binding):**
  **K1 (no-selection kill).** If, within the founder-bounded effort (default: two focused
  sessions), the committed candidate does not yield M1–M9 forward from postulates, the
  campaign records **NEGATIVE-FOR-MECHANISM**: geometry admits γ; dynamics does not select
  it. OPEN-SR-H1-CLASS closes negative; OPEN-SR-EPSILON stays open; the H.1 successor
  graduates to a four-model Proposition (exponents {1, 1, 2, 5/2}) with the codim-2 member
  marked "geometric existence only (continuum-conditional)."
  **K2 (adjudication-before-billing).** No "γ derived" claim may be registered, billed, or
  added to any registry until a CONV-001 panel has ratified the mechanism derivation, with
  this file (including §1) in the package.
  **K3 (fitting flag — explicit).** Any argument invoking the target at any step ("we need
  n = 2," "γ requires," "the coefficient must be 1") is FITTING regardless of its
  conclusion's truth.
  **K3′ (implicit-target kill — new, panel).** Any step in which an intermediate structure,
  plane, measure, scaling, or symmetry assumption is selected, derived in a particular
  form, or given special emphasis BECAUSE it produces or is consistent with n = 2,
  V_free ∝ (1−f²)², or coefficient 1 is FITTING, even if formally justified from
  postulates and even if γ is never mentioned. Test: would the step have been taken, in
  that form, by a derivation that did not know the target? Structures whose only
  distinguishing virtue is target-consistency fail this test.
  **K3a (intermediate-principle launder + counterfactual test — new, DeepSeek).** Any
  posited intermediate principle (a conservation law, minimization, or symmetry) not
  previously established in CPP's corpus for moving aggregates, whose specific
  functional form yields n = 2, counts as FITTING unless the principle itself is derived
  forward from postulates. Operational counterfactual test, applied at every such step:
  if the target were n = 3, would the same reasoning yield a different result? YES ⇒
  forward derivation; NO (the reasoning bends to whatever target) ⇒ fitting.
  **K4 (single-candidate commitment — new, panel).** Mechanism work proceeds only on the
  §3a-ratified candidate. Evaluating other candidates — including "quick checks" — is
  menu-shopping and voids the round. If the committed candidate fails, K1 fires; a
  DIFFERENT candidate may be opened only as a NEW pre-registered round, with panel
  consent, carrying the full negative record of the failed round in the package.

**Success criterion.** M1–M9 derived forward on the committed candidate, K3/K3′-clean,
panel-ratified (K2) ⇒ candidate closure of OPEN-SR-EPSILON and restoration, in corrected
form, of the claim the 2471–2475 triage withdrew. The all-orders identity means leading
order, coefficient, and the full curve come together or not at all — subject to M4's arena
determination.

**Failure asymmetry (stated so the incentive is visible):** the success branch is the
programme's largest single result; the kill branch is a clean negative that still upgrades
H.1's successor. Both publishable. No branch on which fudging M1–M9 helps.

## 4. Panel round-1 record (v1.2 — ROUND COMPLETE)

**5/5 slots returned; 4 unique contents; ALL RATIFY.** ChatGPT RATIFY-WITH-CHANGES ·
Grok RATIFY-WITH-MANDATORY-CHANGES · Gemini RATIFY-WITH-CHANGES · Copilot
(verbatim-identical to Gemini; anomaly recorded) · DeepSeek CONFIRM-WITH-CALIBRATION.
Verbatim returns: `series_relativity/development/review_h1class_prereg_round1/`.
DeepSeek fold (v1.2, Patch 2486): §1b family-selection sharpening; §2a condition 6 + M9
(the stressed-arena fork, demonstrated in `code/2486_stressed_arena_fork.py`); M8
frame-consistency (folded lattice-natively with the covariance-circularity caveat); M3
sub-check (iv); K3a intermediate-principle clause + the n = 3 counterfactual test.
Earlier v1.1 fold — three unique returns, all RATIFY-WITH-CHANGES (one styled MANDATORY).
Every required
change adopted: §1b/§1c disclosure augmentations; §2a scope conditions 1–5 (incl. the
polytope/continuum finding, sharpened here to the leading coefficient, and the
strain-rule conditionality); M1 uniqueness; M3 tightening; M4–M7 added; K3′ added; K4
single-candidate rule added with the §3a commitment instrument. Two of the returns arrived
as verbatim duplicates — slot attribution (ChatGPT/Grok/Gemini/Copilot/DeepSeek) pending
founder confirmation per the standing attribution-anomaly procedure; the round is recorded
by content. Remaining slots, if any, fold into a v1.2 on arrival.

## 5. Immediate next actions

1. ~~Slot attribution~~ CONFIRMED (posting order); ~~remaining returns~~ ROUND COMPLETE.
2. ~~Founder ratifies the §3a commitment~~ **RATIFIED (Patch 2487)** — candidate (a)
   binding. ALL GATES CLEARED.
3. Mechanism session opens (fresh context, warm keyword SR-MECH-2485) against this v1.2,
   K4-bound. Order: **M4 arena determination first** (cheapest kill, K4-safe: if the
   arena is the polytope and the leading coefficient misses 2, the campaign dies before
   any plane derivation), **M9 stress-scaling second** (second-cheapest kill: the
   absolute branch kills for stressed aggregates), then the committed candidate against
   the full M1–M9 burden with K3/K3′/K3a logged per step.
   **→ M4 PASSED (Patch 2488): arena = the PSR insphere**, derived forward (A3′
   flat-per-hop scalar c + pre-target r_in ≡ l_P normalisation ⇒ reach ball inscribed
   ⇒ ball ∩ polytope = ball identically); coefficient 2 exact by derivation;
   counterfactual polytope (4-cube) gives π/4 — kill was live. §2a condition 1
   discharged. One K2-package caveat (A3′ matter-clause scope) logged. Full derivation
   + K3/K3′/K3a log: `SR-MECH-2485_mechanism_session.md`; verify:
   `../code/2488_m4_arena_coefficient.py` (ALL PASS). Session step 2 = M9.
   **→ M9 RESOLVED-BY-DISSOLUTION, PENDING K2 (Patch 2489):** d = v_abs·t_P is
   kinematically forced (Branch L's formula) and, via c07's pre-target channel
   split (uniform background: rods untouched, clocks slow, v_loc = v_abs·g_bg),
   is IDENTICALLY Branch P's formula in local velocity — the branches are one
   rule in two velocity variables. ε = γ(v_loc)−1 at every stress; composition
   multiplicative g_bg·γ(v_loc); ceiling c/g_bg = the point v_loc = c. The
   dissolution defuses a registered kill trigger and is therefore NOT
   self-certified — panel ratification required (trigger semantics, uniform
   scope, v_loc convention caveats logged in the session file). Verify:
   `../code/2489_m9_stress_scaling.py` (V1–V5 ALL PASS). Session step 3 = the
   committed candidate (a) against the full burden, starting M1.
   **→ M1 PASSED at session level, subject to K2 (Patch 2491, session 2 of the
   K1 clock):** exactly one 2-plane is postulate-distinguished for a uniformly
   moving aggregate — Π = span(τ̂, ê_motion), candidate (a), canonical as the
   span of the data itself. Uniqueness by enumeration over ALL k-planes on
   postulate criteria (constructible + stabilizer-invariant, METH-CHIR-CONT-2
   precedent): k = 1 and k = 3 carry constructible continua (no unique object);
   k = 2 admits exactly two invariant planes {Π, P⊥}, of which only Π contains
   any data. v → 0: stabilizer grows to SO(3), NO invariant 2-plane exists,
   consistent with d = v·t_P = 0. Counterfactual live: a discrete (C₂/trivial)
   stabilizer — the lattice-orientation-participates branch — yields a CONTINUUM
   of invariant planes and kills M1 (machine-verified, kept as V5). Three
   caveats to K2: lattice-orientation scope (shared with M4's caveat); Π-vs-P⊥
   orientation (fallback: unique splitting, orientation transfers to M2);
   distinguishedness-criterion status. Full derivation + K3/K3′/K3a log:
   `SR-MECH-2485_mechanism_session.md` step 3; verify:
   `../code/2491_m1_plane_uniqueness.py` (V1–V6 ALL PASS). Session step 4 = M2
   (exclusion rule).
   **→ M2 NOT DERIVED — UNDERDETERMINED BY THE CURRENT CORPUS; FORK PINNED;
   MECHANISM WORK STOPPED; DISPOSITION TO FOUNDER + PANEL (Patch 2492).** The
   candidate composition rules for drift-meets-budget were enumerated forward;
   the rest-limit continuity filter (grounded in c01's displacement-response
   continuity) kills the half-space floor and the exact-advance slice — notably,
   the corpus's own per-Moment obligation template (c01's τ-advance structure)
   transfers to a slice and dies. Four survivors remain, pairwise inequivalent
   at leading order: R1 translation (ε = 0), R2 lens (n = 1, coeff 8/3π), R3y
   symmetrized slab (n = 1, coeff 16/3π), R4 in-plane magnitude-floor tube
   (n = 2, (1−f²)² exact). The postulates as developed do not discriminate; the
   discriminating input — the per-Moment single-CP content of the motion state —
   is the SF-6 inertia mechanism, UNPINNED and the subject of a registered open
   isolated investigation (Patch 2470, 14 Jul), which OPEN-SR-EPSILON's registry
   text independently flags as the recommended route. Selecting R4 today would
   be selection by target (K3′); three drafted routes to it were abandoned on
   that test and are recorded verbatim in `../reasoning/2492.md`. Disposition
   options shipped upward, each stated against interest: (α) K1 fires —
   NEGATIVE-FOR-MECHANISM per the registered kill branch; (β) explicit founder
   extension gated on the SF-6 isolated investigation, pre-committed so that an
   SF-6 landing on R1/R2/R3y (or nothing) kills with no further extension, and
   with the fork WITHHELD from the SF-6 working instance to preserve its
   blindness. M3/M6/M7/M8 are downstream of the rule and were not worked;
   M5 respected (nothing absorbed); K4 untouched (rule fork, not plane fork).
   Verify: `../code/2492_m2_rule_fork.py` (W1–W3 ALL PASS). NOTHING PROMOTED
   (K2).
4. Any mechanism claim returns to the panel with this file (K2).
