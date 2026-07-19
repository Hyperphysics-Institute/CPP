# K1a controls executed: CTRL-1 fails under BOTH coupling laws and the diagnosis is a finding — the registered bound geometry is not a pairwise-potential equilibrium; K1a CLOSED BLOCKED (Branch I, CTRL-1 named), routed to founder as the registration question

**Patch 2573, 19 July 2026. Governed by `k1a_preregistration.md` (2572) under charter v1.1.
Artifact: `code/2573_k1a_controls.py`. Status: control battery EXECUTED; production HALTED per
2572 §6; K1a CLOSED BLOCKED — Branch I, control named CTRL-1, finding named below.**

## 1. Faithful-implementation disclosure chain (anti-erasure; three events, 2571-class)

1. **Sign inversion (bug, fixed):** the choreography's internal force array is the NEGATIVE of the
   physical gradient force −∇U (harmless inside the dance, which consumes only magnitude and a
   projection). The first battery run consumed it as Newtonian force — attraction became
   repulsion, ejecting the bound pair at 0.54c. Fixed to −∇U of the registered energy; disclosed.
2. **Charter-transcription correction:** the 2572 §3 rule froze INSTANTANEOUS per-step coupling;
   the governing charter v1.1 §1 licenses the **cycle-averaged** law verbatim ("homes acquire ΔV
   from the cycle-averaged cross-structure force"). The charter governs; the engine was corrected
   to per-Moment-cycle impulses. **The instantaneous variant's behavior is banked as a labeled
   diagnostic finding:** the choreography layer ANTI-DAMPS the scaffold under instantaneous
   coupling — ~26 MeV (the full binding scale) rectified into scaffold kinetic energy within
   ~0.3T, unbinding the pair (ledger: sum −26.45 → +0.26). A choreographed layer is not a thermal
   bath; instantaneous coupling rectifies its fluctuations. Of direct interest to K1b (the energy
   CAN move between layers — but under this coupling it moves the wrong way, uncontrolled).
3. **CTRL-4 redesigns and its design defect:** two trajectory redesigns still showed
   non-convergent reversal error — diagnosis: under the LICENSED cycle-impulse law, the Moment
   cycle is a PHYSICAL timescale that does not shrink with dt, so reversal error is dominated by
   O(cycle-impulse) discretization and cannot dt-converge. CTRL-4's criterion (drafted for a
   smooth integrator) is incompatible with the licensed law — a prereg design defect, disclosed;
   the physical content it aimed at (momentum closure, symmetries) is covered by CTRL-3/3b/5/6.

## 2. Battery verdict

CTRL-2 (zero-coupling regression): **PASS ×6.** CTRL-3 (dead-cell pass-through + momentum):
**PASS ×6**, |ΔP| = 0 exactly (symmetric cell — closure by symmetry, noted); **CTRL-3b
(asymmetric closure, added disclosed): PASS**, |ΔP|/scale = 1.7×10⁻¹⁷ — the impulse layer is
momentum-exact. CTRL-5 (exchange): **PASS** (0.0 mismatch). CTRL-6 (mirror): **PASS** (0.0).
**CTRL-1 (bound-state invariance): FAIL ×6 under BOTH coupling laws** — the contact pair unbinds
(ESC/ESC, final U ≈ 0) with instantaneous AND cycle-averaged back-reaction. CTRL-4: FAIL per §1.3
(design defect, not physics).

## 3. THE FINDING (why CTRL-1 fails, and must fail)

The analytic check settles it: the registered pairwise cross-energy between two stacked qDPs is
**strictly monotone attractive from 3·a_qq to merged centers** —
U(sep/a_qq) = −3.0 / −8.0 / −14.2 / −20.6 / **−26.5 (the registered pitch)** / −33.7 / −42.1 /
−50.6 / −57.2 / −59.7 (0). **The registered stacking geometry is NOT an equilibrium of the
pairwise interaction; no finite-separation minimum exists.** The 2565 C-3 "bound state" was bound
by STATIC HOMES — the scaffold pinning was doing the holding. Freed to respond (either licensed
coupling), the pair has nothing to sit in: it collapses through the pitch, scrambles against the
choreography, and unbinds. CTRL-1's pass expectation encoded physics the registered interaction
does not contain; the O1a layer did not break the bound state — it revealed what was binding it.

**Corpus resonance (stated as resonance, promoted nowhere):** ENDBOND-1 found the pairwise strong
form unregistered; ENDBOND-2's two-plane fragment resolved no bond; ENDBOND-3 found cohesion
COLLECTIVE (~115 MeV cooperative drop as the arc wraps). The corpus already said the bond is not
pairwise; this battery adds the sharper statement: **free two-body capture cannot TERMINATE in
the registered geometry, because that geometry is registration-pinned, not potential-bound.**
Consequence for the 2571 map, stated: DEAD verdicts survive (no equilibrium makes capture
strictly harder); ACCESSIBLE weakens further (accessibility to a well with no floor at the
registered pitch).

## 4. Reading (per 2572 §6, frozen) and the founder routing

**K1a CLOSED BLOCKED: Branch I, control named CTRL-1, finding named "no pairwise scaffold
equilibrium — capture is lattice-registration."** Banked: the O1a engine (momentum-exact to
10⁻¹⁷, symmetry-exact, zero-coupling regression clean — reusable); the classifiers; the
anti-damping diagnostic; the analytic no-equilibrium table. Production never ran; no observable
was produced to tempt anything.

**Routed to the founder (adjudication #3) — the registration question:** what process IS capture,
if the bound geometry is held by registration rather than by the pairwise potential? Options
named, none adopted:
- **F-a — capture = lattice-site registration.** The homes are the physics: an approaching
  structure acquires a home at the lattice pitch under a registration rule (condition + energy
  shed to Sea via the SF-6 channel). This MERGES K1b R-A with the binding question: registration
  and the sink are one event.
- **F-b — two-body capture is not a CPP process.** Assembly is inherently collective/seeded
  (K2-coupled; resonates with the panel's three-body emphasis and the RELIC campaign's registered
  seeded-nucleation direction). K1a's null is then the honest answer and the K-phases re-scope.
- **F-c — a missing repulsive core.** Registered physics the pairwise layer omits (the
  jello/Earnshaw stabilization, ZBW/ponderomotive content — FLOQUET-1 lineage named) may supply
  the short-range repulsion that makes the pitch a true equilibrium; if derivable, CTRL-1's
  expectation becomes physical and K1a re-opens under a completed interaction.

## 5. Bookkeeping

79.5% untouched. Dated line to the standing disclosure queue (which accretes: the queue now holds
the 2567 registrations + this blockage — a candidate future dispatch under rule (a) if the
founder wants panel input on F-a/F-b/F-c, though the adjudication is his). Queue: founder
adjudication #3 → K-phase re-scope or K1a re-charter per his selection; REACH-AUDIT-2 and the
ΔE_n decomposition remain queued and are now attractive interim work (audit-class, founder-input-
free). Next patch: the adjudication capture, or REACH-AUDIT-2 R-A if the founder prefers the
audit to proceed while he considers.
