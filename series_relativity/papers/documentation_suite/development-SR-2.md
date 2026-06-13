# Development — SR-2: The Spin-Bit Axiom

Tier-3 development narrative for the spin-2 / `op:einstein` (a) arc and the SR-2 paper assembly.
Patch-indexed navigation is in `transcript-SR-2.md`; the verbatim per-step reasoning lives in
`../../op_einstein_closure/` and `../../op_einstein_closure/spin2_construction/`.

## How the arc started

`op:einstein` had two halves. The (b)-half — can a uniform Dipole Sea gravitate (the
cosmological-constant return route)? — was closed first and conditionally (Patches 1107–1108):
the icosahedral 12-edge shell is a spherical 5-design, so Σv̂ = 0 annihilates the absolute-|SSV|
monopole exactly, and the continuum operator is the Laplacian. The (a)-half — does the substrate
carry the radiative tensor sector? — became the summit.

## The diagnosis and the necessity proof (Patches 1109–1119)

The metric map is explicit: |SSV|_abs → g_tt (scalar), SSV_net → g_ij (vector). The transverse-plane
quadrupole that is the GW + and × signal has no source in that content (1109); c07 §6 *asserted* but
did not *derive* the tensor modes (1110); the corpus has no rank-2 d.o.f. (1114). Three assaults then
closed every no-new-axiom route: amplitude/gradient bilinears (helicity-2 only at 2nd order, double
frequency; 1115), the full collective-mode spectrum (four branches of helicity {0,0,±1} for any
icosahedral couplings; 1116), and the most general per-edge connection — the "non-radial twist"
(representation bound + Planck-scale gap + empirical exclusion to ~1e-46; 1119). Verdict: a
fundamental rank-2 degree of freedom is necessary.

## The construction (Patches 1112, 1120–1129)

The seat was already in the geometry: the icosahedral shell's H (l=2) irrep resolves the quadrupole
at rank 5, and its m=±2 content is exactly the + and × polarizations (1112). The flow choice put the
new field in the GP→GP broadcast (flow B), not the CP register (A) or the displacement readout (C),
because A or C would each still induce B while B induces neither (1121). The axiom text A3 → A3′ was
written as an amendment with clauses C1–C5 (1123). The coupling λ = 16πG/c⁴ was derived from
G-consistency, making c08's asserted wave equation a theorem (1124). The response was shown pure
tensor via the cancellation theorem + the redundant trace completion (1125, 1127). The strong-sector
test (1120) found tensor mesons reachable from orbital angular momentum without Q_ij — so the axiom
is mono-sectoral, and it returned the geometric bonus that the icosahedral group protects the 5-fold
multiplet (cubic would split 2+3). Registration and the DG-3 close came at 1129 (see
`reviews-SR-2.md`).

## The paper assembly — Phases 7A/7B/7C (Patches 1131–1142)

- **7A (1131–1135):** section-skeleton + gap inventory; C14 methods audit; figure regeneration;
  SKELETON LOCK with the architect settling all five decisions, including paper ID **SR-2** and
  "draft now."
- **7B (1136–1137):** first full draft transcribed from the 13 step docs onto the locked 10-section
  skeleton (v0.1); C14 step-5 audit-trail sweep (added METH-L3-003, METH-L3-004); figure PDFs +
  `\includegraphics`; full `pdflatex ×3 + bibtex` verified clean (19 pp). 7B CLEAR.
- **7C (1138–1142):** framing/over-claim review. Package dispatched per CONV-001; several passes
  (root-caused to raw-CDN stale-cache) integrating necessity scoping, the §11 guard, and the
  universal-motif retirement; closed 3/3 CONFIRM. v0.6 release candidate.

## SHIP-time (Patches 1143–)

- **1143:** registry/index navigation + frontier flip (OPEN-SR-4 → PARTIAL).
- **1144:** H6 final audit — body confirmed SHIP-clean; four registry/orientation FAILs cleared.
- **this suite:** the documentation suite (the last H6 FAIL).

## The throughline

The arc is the programme's cleanest example of axiom discipline: a new axiom was not reached for but
*forced* by exhausting every alternative, then made to pay for itself (zero new parameters), then
made to survive the first axiom-level adversarial review. "Why was the world built this way" gets a
structural answer here — the broadcast carries exactly what the lattice protects, and no more.
