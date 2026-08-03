# ξ₂ DERIVATION PRE-REGISTRATION — THE O(kd)² RELAY COEFFICIENT: DEFINITION, FROZEN BANDS, FROZEN SIGN-HANDLING, FROZEN REVIEW TIMING

**Patch 2950 (2 Aug 2026). Opens the ξ₂ derivation arc registered in
`future_projects.md` at Patch 2946 (own arc, own prereg — deliberately
not bundled with the 2943/2945 conversion per the no-motive rule).
This document (i) defines ξ₂ verbatim from the frozen 2942 structure,
(ii) states what symmetry already determines at quadratic order,
(iii) freezes verdict bands for every outcome class INCLUDING the
handling of a derived sign, (iv) freezes CONV-011 panel-review timing
per branch, and (v) specifies the derivation with its cross-check
route. NO value of ξ₂ is computed, estimated, or quoted; no
experimental bound is touched; the ACTIVE 2945 ceiling is not
re-evaluated here.**

## §1 — THE QUANTITY (definition inherited, not invented)

ξ₂ is the dimensionless coefficient of the quadratic mesh correction
in the TOF-class (polarization-averaged, orientation-averaged over
the ambient Sea) dispersion of the registered DP-Sea relay:

    ω(k)/ck = 1 + s · (ξ₂/2) · (k·d_DP)² + higher order,

with s the propagation sign (subluminal/superluminal), exactly the
quadratic form the 2942 conversion prereg froze when it registered
the ceiling d_DP ≤ (ℏc/E_lim) · ξ₂^(−1/2) (reaching the d_DP factor
per 2936 M3). Per 2942 §2 (CONV-004), ξ₂ is currently UNDERIVED and
the ACTIVE ceiling (2945) is quoted at the ξ₂ = 1 reference
normalization with scaling explicit. This arc is the registered
successor path: a derived ξ₂ with provenance re-evaluates the ceiling
in a successor patch. Per 2942 §3, sign(ξ₂) is also underived; §4
below freezes NOW, before anyone knows the sign, how a derived sign
is used.

## §2 — WHAT SYMMETRY ALREADY DETERMINES (derivable without dynamics)

**S1 (scalar at this order, conditional on R1-expanded):** under the
realized-state I_h premise of the 2945 conditionality stack, the
quadratic form in k must be I_h-invariant; the icosahedral group
admits no invariant rank-2 anisotropy (its first anisotropic
invariant enters at degree 6), so the O(kd)² TOF coefficient is a
single SCALAR ξ₂ — no direction dependence at this order. This
statement inherits and propagates the R1-expanded condition
verbatim: any realized-state symmetry reduction below I_h reopens it.

**S2 (why the value needs dynamics — stated to prevent overreach):**
the 2940 CASE-Q result was a pure symmetry theorem — every odd-rank
invariant tensor vanishes under I_h-with-inversion (Fact 2 + the
Equivariance Lemma, Fact 2′), so the O(kd) matrix is zero with no
dynamical input. That argument does NOT extend to the even-rank
quadratic order: symmetry permits ξ₂ ≠ 0 and fixes only its scalar
character. The VALUE of ξ₂ is a dynamical property of the relay
normalization. Assuming ξ₂ ~ O(1) "because lattices are quadratic
with O(1) coefficients" would import a normalization no one has
computed; assuming suppression would be the α1 pattern. Hence §5's
derivation, with §3's determinacy question answered first.

**S3 (polarization structure at quadratic order):** symmetry permits
a polarization-dependent (birefringent-class) quadratic piece
distinct from the TOF average. The ceiling's ξ₂ is DEFINED as the
TOF/polarization-averaged coefficient (2942 §4 admissibility:
TOF-class only). Any quadratic birefringent coefficient found by the
derivation is reported as a SEPARATE output with its own registered
symbol, and does not enter the ceiling.

## §3 — THE DETERMINACY QUESTION, SETTLED FIRST

**Q1:** does the registered structure — SF-6 STRUCTURAL relay content
(PCD rule under the R4 intrinsicality condition: no structure
external to the registered data D), the 600-cell local geometry, and
the registered data class of 2940 (I_h-invariant, ω_PCD ∥ n̂) —
DETERMINE ξ₂, or is ξ₂ underdetermined pending relay-dynamics
registration (update-rule normalization, Moment-step structure)?
This is answered before any coefficient extraction is attempted. The
2940 precedent cuts both ways and the prereg says so: CASE-Q needed
no dynamics; ξ₂ may. An underdetermined answer is a legitimate
outcome (CASE-DEP below), not a failure to be papered over.

**Q2 (cross-check route, registered now):** the FP-6-CONSTANTS
Stage B finite-k lattice polarization law (scoping at
`flagship_papers/electromagnetism/sketches/fp6_constants_scoping.md`,
Patch 2947) is the registered independent producer of the same
coefficient. The arcs remain SEPARATE (cross-citation, not merge, per
the 2946/2947 registrations); but a derived ξ₂ from either route is
flagged single-route until confirmed by the other (PR5-class
method-independence discipline). Neither arc waits on the other; the
flag simply persists until discharged.

## §4 — FROZEN VERDICT BANDS (before any derivation)

**CASE-O1 (ξ₂ derived, order-unity class, sign determined).** The
successor patch re-evaluates the ACTIVE ceiling at the derived value
per the 2942 §2 registered successor path. **Frozen sign-handling,
fixed now while the sign is unknown:** the 2942 §3 weaker-sign rule
was premised on an underived sign; once sign(ξ₂) is DERIVED with
registered provenance, the successor ceiling binds at the published
limit of the DERIVED sign (both limits still reported). This is
frozen before computation precisely because the derived sign could
select the STRONGER limit — the choice must not be available after
the sign is visible. If registered physics additionally guarantees
ξ₂ > 0 bounded away from zero, the successor patch states the
GPT-S1 §4 upgrade (conditional-ceiling family → finite bound) — in
the successor patch only, never informally.

**CASE-SUPP (ξ₂ ≪ 1 via derived formula).** Admissible ONLY as a
formula whose smallness has registered provenance (anti-α1 bar,
inherited verbatim from 2942 §2 / a5_disp_prereg.md §2). The
successor ceiling weakens as ξ₂^(−1/2) and is quoted with the full
provenance chain attached. Conservative class.

**CASE-ZERO (ξ₂ ≡ 0; quadratic order also protected).** Then E_QG,2-
class TOF bounds constrain a coefficient the corpus derives to
vanish — the same no-information logic that made birefringence-class
bounds inadmissible at 2942 §4 — and the ACTIVE 2945 ceiling's
constraint content evaporates. Frozen response: this finding is
REOPENER-CLASS against the 2945 ceiling; nothing is kept quietly.
Pre-action review fires (§5), and the expected disposition (panel's
to ratify, not the worker's to enact) is: ceiling VOIDED as
uninformative with its trail preserved, the derived protection
registered as a structural result in its own right, and the
leading-order successor (quartic-class) scoped with fresh bands.

**CASE-DEP (underdetermined by registered structure).** HALT; the
missing dynamical registration is named and filed; no provisional
number, no placeholder normalization. Registered expectation (stated
now so it cannot be invented later): the likely missing object is
the relay's dynamical stiffness normalization — plausibly the SAME
object FP-6 Stage A/B must derive — making FP-6 progress the natural
unblock path via the §3 Q2 cross-citation. Roadblock class.

**In all cases:** the ACTIVE ceiling is touched only by a successor
patch citing these bands verbatim; the ξ₂ symbol acquires a value in
the corpus only through that chain.

## §5 — CONV-011 REVIEW TIMING (frozen BEFORE any computation)

- **CASE-O1, CASE-SUPP** — conservative: combined completed-package
  review (derivation + successor re-evaluation) PERMITTED;
  PANEL-PENDING banner until ratified; overturn or condition ⇒
  successor products VOIDED not revised (2941/2943→2945 mechanism).
  Note the sign-handling of §4 is part of the frozen package: a
  panel seat contesting the derived-sign rule contests THIS prereg,
  which was frozen sign-blind.
- **CASE-ZERO** — falsifier/reopener-class against an ACTIVE corpus
  constraint: PRE-ACTION review REQUIRED before any void, successor,
  or downstream statement about the ceiling.
- **CASE-DEP** — roadblock: panel convenes per the standing economy
  convention.
- Any outcome not matching a frozen band: HALT and register the gap
  (2942 §5 discipline, inherited).

## §6 — INHERITED CONDITIONALITY (propagates to any result)

Every output of this arc carries the 2945 §3 stack and says so:
Mechanism A on both legs (CAPACITY-1 + TARROW-2); vertex-aligned
Reading C (Q1′, C-W37); relay intrinsicality (R4); realized-state
I_h symmetry (R1 expanded); reopeners R1–R4 propagate. S1 above
additionally makes the scalar character of ξ₂ explicitly
R1-conditional.

## §7 — THE DERIVATION (specified, not executed)

One focused session: (i) answer Q1 from the registered relay
structure — enumerate exactly which properties of the PCD rule the
quadratic coefficient depends on, and check each against the
registered data class D (R4 discipline: anything external to D
disqualifies itself and routes to CASE-DEP); (ii) if determined,
extract the O(kd)² TOF coefficient by extending the 2940 machinery
to second order — polarization-resolved, orientation-averaged under
I_h, the Equivariance Lemma available for composite-path closure —
with a verify script committed same-patch (stdlib, per house
convention, in `code/`); (iii) report the TOF scalar and any
birefringent-class quadratic piece separately per §2 S3; (iv)
classify into CASE-O1 / SUPP / ZERO / DEP; (v) the successor
ceiling re-evaluation, if warranted, follows as its own patch citing
these bands verbatim; (vi) the FP-6 Stage B cross-check flag is
attached or discharged per §3 Q2.

## §8 — LEDGER

Nothing moves: six of seven; PR7 PARTIAL; B7 holds; Candidate (B)
79.5%; 2855 PROVISIONAL; M1/M2 frozen; the d_DP ceiling stays ACTIVE
at its 2945 form and normalization. No value of ξ₂, η, d_DP, or n_DP
appears in this document.
