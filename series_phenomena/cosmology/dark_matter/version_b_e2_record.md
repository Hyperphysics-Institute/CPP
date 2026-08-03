# E-2 RECORD — VERSION B TOY VERIFICATION: 7/7 PASS; FACT G1 CONFIRMED IN MECHANISM; ONE STRUCTURAL FINDING (THE FRONT IS A BAND)

**Patch 2959 (2 Aug 2026). Executes E-2 (charter §5, re-scoped 2958
§4) on the founder's Version B algorithm. Script
`code/2959_version_b_toy.py` (stdlib, N = 12 hops, exact-split +
integer runs), 7/7 PASS. Conservative outcome per charter §6 →
queued for combined review with E-1. No value of any open physical
quantity appears; toy units (edges, hops) only.**

## §1 — VERIFIED (toy grade)

1. **Conservation exact** (total mass 1.000000000000 across 12
   hops) — the counting premise of inverse-square.
2. **Ballistic:** mean radius linear in hop count (residual <0.5%
   after the disclosed 3-hop seed transient); mean radial speed
   ≈ 0.57 edge-lengths/hop (sub-unity because outward hops are
   generally oblique — see §2).
3. **Uniformity:** hemispheric dipole asymmetry < 10⁻¹⁷ over 200
   random axes; angular power A₁…A₅ at the 10⁻⁶–10⁻⁴ finite-size
   floor while **A₆ = 0.17 — five orders larger: FACT G1's
   prediction (exact isotropy through degree 5, first lattice
   anisotropy at degree 6) is confirmed IN THE MECHANISM**, not
   only in the stencil moments. The founder's smoothness question
   is answered at toy grade: reasonably smooth = degree-6-limited.
4. **1/r² as corollary:** conservation + isotropy + ballistics ⇒
   flux through any sphere constant ⇒ intensity ~ 1/r². Disclosed
   toy limitation: icosahedral directions form a quasi-lattice
   (positions proliferate; 94,878 sites at hop 12), so per-SITE
   density is not directly measurable here; the corollary is
   analytic given 1–3, and the lattice-density version belongs to
   the full derivation.
5. **Remainder rule benign at scale:** an integer run (10⁷
   DI-bits, random-remainder assignment) tracks the exact split to
   3×10⁻⁷ on all major sites with exact count conservation —
   supporting the 2958 shot-noise framing: remainder effects
   matter only at small counts (the A5-SHOT regime).

## §2 — FINDING F-E2-3 (structural; question back to the founder)

**The arriving front is a BAND, not a sharp sphere:** σ_r/⟨r⟩ ≈
0.096 (~10% fractional thickness), stable across hops. Cause:
even splitting over ALL outward edges lets paths differ in radial
obliquity, so equal hop count does not give equal radius. Options
for the physics (founder's to weigh, not the worker's to pick):
(a) the PSR arrival is genuinely a band — the "shell" has intrinsic
~10% thickness, with possible physical content; (b) the split rule
carries radial weighting (e.g., shares ∝ outward projection),
which sharpens the front — a small protocol change with derivable
consequences; (c) the PSR condition is radius-triggered rather
than hop-triggered (DI-bits stop at radius, not at count N),
making the band a transit property only. Each option is
formalizable; none is assumed.

## §3 — DISPOSITION AND LEDGER

E-2 COMPLETE (conservative class). Next: E-1 (AUTOMATON re-read,
classifying the two implementations against Version A/B), then the
K1-MEMORY derivation charter; the combined CONV-001 review takes
E-1+E-2 together with the queued 2951 roadblock item. Ledger
untouched: six of seven; PR7 PARTIAL; B7 holds; Candidate (B)
79.5%; 2855 PROVISIONAL; d_DP ceiling ACTIVE. New: the §1
verifications (toy grade), F-E2-3 with its three-option question.
