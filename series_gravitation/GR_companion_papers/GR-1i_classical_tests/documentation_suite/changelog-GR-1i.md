# Changelog — GR-1i: The Classical Tests of Gravitation

**Paper:** `series_gravitation/GR_companion_papers/GR-1i_classical_tests/GR-1i_classical_tests.tex`
**Convention:** canonical filename never carries a version suffix; version history lives here only.

---

## V0 — 19 August 2026, Patch 3252 (Session 150)

Initial complete draft, discharging **OPEN-GR-TESTS-1** (registered Patch
3229, `frontier_sectors/GR.md`) per the founder's bounded-scope ruling:
ONE tests companion, standard derivations, results equal to the frozen
GR-1 Table 1 values.

Content:
- Full geodesic machinery on the GR-1c isotropic Schwarzschild metric
  (Eq. iso), derived in standard coordinates via the exact transformation
  r = r_iso(1+ϱ)² (machine-verified, 3228 check 0), with coordinate
  invariance of the four observables stated.
- Test I: perihelion precession — perturbative Binet solution,
  Δφ = 6πGM/(a(1−e²)c²), Mercury 42.99″/century; numeric RK4 cross-check
  agreement to four decimals (42.9917 vs 42.9917).
- Test II: light deflection — photon Binet perturbation, α = 4GM/(c²b),
  1.75″ at the solar limb (numeric 1.7517″, 0.006%); the factor-of-two
  section ties the scalar/vector split to the two-component LSP (GR-1b).
- Test III: Shapiro delay — leading-log round trip 4GM/c³·ln(4 r_E r_V/b²),
  232.6 ≈ 233 μs Earth–Venus grazing superior conjunction; γ-discipline
  stated (CPP has γ = 1 identically; Cassini bound quoted).
- Test IV: gravitational redshift — static clock rates, Pound–Rebka
  2.46×10⁻¹⁵ over 22.5 m; GPS +45.7 (grav) − 7.2 (SR) = +38.5 μs/day.
- Summary table reproducing GR-1 Table 1 verbatim (frozen targets).
- Numerical-verification section documenting the two 3228 traps
  (φ-accumulation drift; crossing-overshoot) for reimplementers.
- CPP Physical Mechanism section (graded-index Sea picture; per-test
  mechanism), with the required CP/GP Signature subsection (PD-001).
- CPP-to-Conventional-Physics Mapping table.
- Conclusion with the required Swarm-Validation Contribution (honest:
  ZERO new zero-parameter predictions minted — GR-identical by
  construction; contribution = entry-criterion compliance) and Problem
  Status (OPEN-GR-TESTS-1 → DISCHARGED at V0, final at review/ship;
  OPEN-GR-FE-1 untouched).

Claim discipline (frozen, from GR-1 §5 and the founder rulings):
conditional on the PSR constitutive form at W2 strength (SR-1
inheritance, not upgraded); values GR-identical by construction; the
tests discriminate CPP from Newton, NOT from GR; Lense–Thirring not
redone (GR-1f/GR-1c).

Verify: `series_gravitation/code/3228_classical_tests_verify.py` re-run
this session, 8/8 PASS (isotropic≡Schwarzschild 3.3e-16; perihelion
42.9917/42.9917; deflection 1.7516/1.7517; Shapiro 232.6 μs; PR
2.455e-15; GPS +45.7/−7.2/net 38.5). The paper derives what the script
checks; no new script minted.

Compile gate: pdflatex ×2, zero errors.

---

## V0.1 — 20 August 2026, Patch 3269 (Session 150)

CONV-029 adjudicated: unanimous across all six questions;
OPEN-GR-TESTS-1 FINALLY DISCHARGED 5–0; SHIP-PATH-CLEAR 5–0. Five
editorial adoptions folded in: (1) the Constants-provenance-and-
sensitivity subsection (script-GM vs IAU, 0.028%, per-entry shifts,
full constants list, panel SCRIPT-EXECUTED runs as archival artifact);
(2) PPN β = γ = 1 structural note + Shapiro relabelled a coarse
consistency check; (3) the reproduces-vs-shares claim-discipline
sentence; (4) the achromatic-bending falsifiable-feature remark
(unminted); (5) the implementation-cross-check caution on numeric-vs-
closed-form agreement. Compile gate clean. V1.0 prep may begin.
