# Frontier sector: GR (local gravitation series)

**Location:** `/CPP/frontier_sectors/GR.md`
**Created:** 19 Aug 2026, Patch 3229 (Session 149), concurrent with the GR-1
V0 assembly (Patch 3228). Series home: `series_gravitation/`.
**Scope of this sector:** the gravitational series parent GR-1 and its
companions GR-1a–GR-1h (formerly c05, c07–c13; moved to
`series_gravitation/GR_companion_papers/` at Patch 3230 — OPEN-ORG-023
Item 2 executed). GR-1i is reserved for the classical-tests companion.
**Boundary:** LOCAL gravitation only. Cosmology (FRW/Friedmann, dark energy)
is owned by OPEN-EU-1 (`frontier_sectors/SR.md` / CONJ.md) and the DE lane;
nothing in this sector claims it.

---

## OPEN-GR-FE-1 — Derive the general CPP field equations (registered Patch 3229)

**The problem.** The arc reproduces the Schwarzschild (isotropic
coordinates), Kerr, and Kerr–Newman *solutions* exactly, but the general
field *equations* are present only as correspondence claims: c07 states the
CPP self-consistency condition is "≡ Einstein field equations" in the
continuum limit; c08 "identifies the CPP equation that plays the role of
Einstein's field equations" (a nonlinear wave equation for Δ|SSV| reducing
to the linearised Einstein equations in the weak field). Recovering specific
metrics is not the same as deriving the equation family whose solutions they
are, and a GR-literate reader will make exactly that distinction (Patch 3225
scoping assessment §3; founder ruling: V0 claims the solutions and registers
the derivation).

**The target.** Derive the general CPP field equations from the deeper
DI-bit / SSV_abs / SSV_net / DP Sea picture — not by positing correspondence
in the continuum limit. Folded into this item (consequences of the same
underived general equation, 0 mentions each across the eight companions):

- **Birkhoff-type uniqueness** — is the c08 static solution the unique
  spherically symmetric vacuum solution of the CPP equation?
- **The CPP energy-momentum tensor** — the object the field equations are
  equated *to*; currently absent from the corpus.

**What would count as progress.** (i) A stated general equation for the
LSP/SSV field configuration with the c08 nonlinear wave equation as its
static reduction; (ii) proof that Eq. (isotropic_schw) is its unique
spherically symmetric vacuum solution; (iii) identification of the source
tensor and its conservation law within PCD dynamics.

**Dependencies / inheritance.** Rests on the PSR constitutive form whose
SR-1 grounding is W2 viability strength (OPEN-SR-10 caveats inherited
verbatim; k is a normalisation convention, not a derived quantity — see GR-1
§7). Any derivation here inherits, and must not silently upgrade, that
standing.

**GR-1 cycle note (CONV-026, Patch 3242/3243):** Q4 3–2 RESTATE-REQUIRED fired on the Q1 3–2 OVERCLAIMS finding (abstract/thesis outran the ledger); restate EXECUTED at V0.2 — the W2/PSR conditionality promoted into the abstract and thesis. Q2 4–1 COMPLETE, Q3 5–0 SOUND stand. **Confirmation pass returned 3/3 CONFIRMED-DISCHARGED (Patch 3247; one cross-label recorded — the Gemini window signed "ChatGPT"; attributed by receipt): Q4 = SHIP-PATH-CLEAR; CONV-026 CLOSED.** V1.0 prep unblocked; deposit still gated by the founder's ruling + the tests companion. Next papers in the lane, in readiness order: the tests companion (OPEN-GR-TESTS-1, → GR-1i; bounded, targets frozen) then OPEN-GR-FE-1.

**Status:** OPEN — CHARTERED (Session 150, Patch 3254:
`series_gravitation/OPEN-GR-FE-1_derivation_charter.md`). Three theorem
targets frozen (T-1 general equation with the c08 wave equation as static
reduction; T-2 Birkhoff-type uniqueness; T-3 source tensor + PCD
conservation); inheritance bar frozen (W2/PSR standing must not be silently
upgraded); worker pre-picture expectations on record (charter §5, the A1
anti-extraction pattern); **founder physical-picture session ANSWERED —
W-1 EXECUTED (Patch 3255):** all five §6 questions answered same-session;
narrative registered verbatim at
`founders_voice/founder_ruling_GR-FE-1_physical_picture_2026-08-19.md`
(worker commentary labelled, nothing adopted). Picture-set constraints for
W-2, per the labelled commentary: conserved quantity = the conscious
points themselves + the per-Moment DI-bit equal-redistribution invariant
(redirects §5 E-1); PCD executor = the GP (CP displaces per the GP's
computed SSV_net; DI-bits a third conserved CP type — glossary/axiom-impact
flag recorded, not actioned); source = compressed-DP SSV_abs content, no
independent kinetic term posited (narrows §5 E-2); A3′ load-bearing
(symmetry at full-Moment granularity only); lattice zero-freedom + CP-only
configuration freedom + full-occupancy black-hole saturation (T-2 skeleton;
cross-check the new full-occupancy mechanism against GR-1c/GR-1e before
quoting); DP-Entities gravitationally silent at LOCAL scale (founder
expectation, DM-lane confirmation owed); Voronoi-cell-to-PSR ratio OPEN
(~10^30 GPs/PSR quoted; W-2 must not depend on it or carries it
symbolically). **W-2 (T-1 derivation attempt) UNBLOCKED — own session.**
Deliberately deferred out of GR-1 V0 by founder ruling (Session 148
handover §5). The single most consequential open item in the arc; the
big-wave deposit gate (Patch 3231 ruling) rests on it.

---

## OPEN-GR-TESTS-1 — The classical-tests companion (registered Patch 3229)

**The problem.** The three conventional entry-criterion tests of any
gravitational theory (perihelion precession, light deflection, Shapiro
delay) plus gravitational redshift were absent or barely touched across the
eight companions (perihelion 0 mentions, Shapiro 0, geodesic 1 of 8). GR-1
V0 now carries the predicted-versus-observed summary table (GR-1 Table 1),
with every number verified by `series_gravitation/code/3228_classical_tests_verify.py`
(8/8 PASS: closed forms cross-checked against independent numeric
Binet-equation geodesic integration; the c08 isotropic form verified to BE
Schwarzschild at machine precision).

**The target.** ONE dedicated companion paper (founder ruling: not inside
GR-1, not split into three) carrying the full geodesic derivations of all
four tests on the c08 metric — timelike orbit precession, null deflection,
round-trip Shapiro delay, static redshift — as consequences worked out from
the parent's result, exactly as c09 takes c08's core and derives echoes.
Independently citable, because "does it pass the classical tests" is
precisely what a reader will search for.

**Frozen constraints.** The results it must reproduce are frozen in GR-1
Table 1 and the 3228 verify script: perihelion 42.99″/century, deflection
1.75″ at the solar limb, Shapiro ~233 μs (Earth–Venus superior conjunction,
grazing, leading log), redshift gh/c² = 2.46×10⁻¹⁵ (22.5 m) and GPS net
+38.5 μs/day. The claim discipline is also frozen: since the metric is
exactly Schwarzschild, the values are GR-identical by construction — the
tests discriminate CPP from Newton, NOT from GR, and the companion must say
so. Lense–Thirring frame-dragging is already covered (c11 ×16 mentions, c08
×7); do not redo it.

**Numerical cautions for the implementer** (found and fixed at 3228, see
`series_gravitation/reasoning/3228.md`): (1) accumulate the integration
angle as i·dφ from an integer counter — naive `phi += dphi` over ~10⁷ steps
injects rounding drift at percent level against a 5×10⁻⁷ rad/orbit signal;
(2) locate zero crossings by interpolation — first-grid-point stopping
overshoots at 10% level against an 8.5×10⁻⁶ rad deflection.

**Status:** DISCHARGED AT V0 (Session 150, Patch 3252) — final discharge at
panel review/ship. GR-1i drafted:
`series_gravitation/GR_companion_papers/GR-1i_classical_tests/GR-1i_classical_tests.tex`,
full geodesic derivations of all four tests on the c08 metric (standard
coordinates via the machine-verified exact transformation; isotropic form
carries the mechanism section). All frozen Table-1 values reproduced
(42.99″/cy · 1.75″ · ~233 μs · 2.46e-15 / +38.5 μs/day); 3228 verify re-run
8/8 PASS pre-draft; both numerical traps promoted into the paper body;
claim discipline verbatim (W2 conditionality in the abstract's first
sentence — the CONV-026 restate lesson applied from the start; GR-identical
by construction; discriminates from Newton, not GR; Lense–Thirring not
redone). Swarm-Validation subsection written honestly at ZERO new
predictions (entry-criterion compliance, no double-count of GR-1c's
exactness). Compile gate clean. Next lane item: OPEN-GR-FE-1 (charter
first, then founder physical-picture session, per the Session 149
handover).
