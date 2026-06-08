# Leg-2 neutrality: a derivation attempt (closed-substrate Gauss law)

*Patch 1300, Phase-0 parallel round, worker window **W3**. Attempts to push EU-1 leg 2 —
charge neutrality of the early CP plasma, n₊ = n₋ at all occupations — from **grounded**
(framework commitment, Patch 0770, `neutrality_grounding.md`) to **derived from A1–A11**.
This is part of the OPEN-EU-1 residual (specifically the leg-2 A1–A11 sub-mark, named the
"most tractable" of the three open marks in the Session-154 handover).*
*Script: `scripts/1300_neutrality_topology.py` (ALL PASS). Reasoning: `reasoning/1300_neutrality_derivation.md`.*
*Status: **substantially derived — no new axiom required**; reduces to A1 + A2 + A3 + A6′ modulo
two named bridging lemmas. **NO THEO registered by this window** (registry-freeze this round;
THEO proposed in the Registry Handoff Note for panel review). Does NOT touch `neutrality_grounding.md`.*

---

## 1. What leg 2 actually requires (restated from 0756 / 0770)

The interacting MC (0756) showed the tilt is uncontaminated **iff the early CP plasma is charge-neutral**:
a balanced ± plasma gives a flat μ_excess (ideal, K = K_att), an unbalanced one gives a spurious slope.
The grounding doc (0770) makes the operative quantity explicit: it is the **mean-field Coulomb term ∝ Q²**,
where Q is the *global* net electric charge. "Global ± balance kills the mean-field; the local √n̄ Poisson
fluctuation is the separately-bounded Debye thread (0764–0768)." So **leg 2 needs exactly Q = 0 (global), at
every occupation n** — not local pairing per se. This is the target of the derivation below.

## 2. Current status and why it is not yet a derivation

Patch 0770 grounds Q = 0 in the **glossary** definition: DP = "a bound pair of opposite-polarity CPs … a DP
is electrically and colour-neutral"; DP Sea = the vacuum built entirely of DPs. If every unit is a neutral
pair, n₊ = n₋ trivially. This is honest grounding, but it **assumes the structural fact it needs** — that the
substrate is built from ± pairs is a framework-level commitment, not a consequence of A1–A11. The derivation
below removes that assumption: it shows ± balance is forced by the *topology* of the substrate, and in doing so
**explains** why the DP-pair structure holds rather than positing it.

## 3. The derivation — global neutrality from the closed substrate

The argument is the CPP instance of a standard result: **the total electric charge of a spatially closed
universe is exactly zero.** Here it is grounded step-by-step in the CPP axioms.

**Step 1 — A2 ⇒ the substrate is closed and boundaryless.** A2 places CPs on the tessellated 600-cell {3,3,5}.
The 600 tetrahedral cells of {3,3,5} are the regular tessellation of the **3-sphere S³** — a compact 3-manifold
**without boundary**. (Sanity check, script [1]: the f-vector V−E+F−C = 120−720+1200−600 = 0 = χ(S³).) The
substrate therefore has no boundary across which any flux can escape. *(This is the closed-substrate reading of
A2, consistent with CPP's closed-FRW/VSL spatial section; see residual R1 for the open/flat alternative.)*

**Step 2 — A1 ⇒ each CP carries ± unit electric polarity.** A1 states CPs "exist with polarity (±)." Identify
the electric polarity with a charge ±q. The global net charge is then Q = q·(n₊ − n₋), so **Q = 0 ⇔ n₊ = n₋.**

**Step 3 — A3 + A6′ ⇒ a U(1) flux field with a local Gauss law (bridging lemma L1).** The edge sector of A6′ is
the Abelian U(1) electromagnetic sector; A3 propagates the DI-bit field that mediates it. Read in the standard
Maxwellian form, the edge-sector field **D** obeys a *local* Gauss law ∇·**D** = ρ_charge, with the CP ± polarities
as its **sole** sources (no free monopoles, no other charged species). This is the one step that is *implied by*
the axioms rather than literally written; it is isolated as **LEMMA-EU-NEUTRAL-GAUSS (L1)** below.

**Step 4 — closed-manifold Gauss law ⇒ Q = 0 identically.** Integrate Step 3 over the whole substrate. By the
divergence theorem on a manifold *without boundary*,
   ∫_{S³} ρ_charge dV = ∮_{∂S³} **D**·d**A** = 0   (because ∂S³ = ∅).
Hence **Q_total = q·(n₊ − n₋) = 0 exactly ⇒ n₊ = n₋ exactly.** No appeal to the DP-pair definition is made.

**Step 5 — conservation ⇒ neutrality at *all* occupations.** "No boundary" also means charge cannot flux in or
out: Q is a conserved invariant, ΔQ = 0. As the lattice dilutes during inflation (n̄ ∝ e^{−3N}), occupation
units are removed in net-neutral increments, so n₊(n) = n₋(n) at **every** occupation n — exactly the "at all
occupations" requirement and the 0770 table (n = 10, 10³, 10⁵ → Q = 0). (Script [3]: closed system stays neutral
at all n; an open system with boundary flux drifts — the case S³ topology forbids.)

**Step 6 — no topological-flux loophole on S³ (check L2, passes).** The only way a closed 2-surface could carry
net flux *without* enclosed local charge is a nontrivial harmonic 2-form sector, i.e. H²≠0. For S³ the Betti
numbers are (b₀,b₁,b₂,b₃) = (1,0,0,1): **b₂ = 0**, so there are no harmonic 2-forms and **no loophole** (script
[2]; contrast a 3-torus, b₂ = 3, where the argument would fail). The closed-manifold argument is airtight *because*
the substrate is S³ specifically.

**Conclusion.** Under A1 + A2 + A3 + A6′ (plus L1), global ± balance is a **topological theorem**, exact and
occupation-independent. The mean-field Coulomb term ∝ Q² vanishes identically — leg 2 supplied, *derived* rather
than asserted.

## 4. What this upgrades beyond the 0770 grounding

1. **DP-pair structure becomes a consequence, not a premise.** Topology forces Q = 0 globally (Steps 1–4);
   A10-type attraction between opposite polarities then makes the *local* ground state pair every + with a − →
   the DP Sea. So "the vacuum is built from ± pairs" is *derived* (global balance from topology + local pairing
   from binding), inverting the 0770 logic that took it as given.
2. **The 10⁻⁹ caveat is removed for the charge channel.** 0770 flagged that a ~10⁻⁹ asymmetry "breaks exact
   balance." That caveat conflates two quantities. The closed-manifold law makes the *electric* charge — the
   quantity entering the Coulomb mean-field ∝ Q² — **exactly** zero, with no 10⁻⁹ floor. The ~10⁻⁹ figure is the
   **baryon/matter** asymmetry (which species survive annihilation; cf. Capotauro leptogenesis), a CP-violation
   quantity that does **not** source the Coulomb term. Leg 2 therefore needs no "imbalance ≪ 1" hedge: it is 0.
3. **Independent of the glossary route.** The derivation does not use the DP-pair definition at all, so it is a
   genuinely independent confirmation of leg-2 neutrality — the swarm-validation pattern (two independent routes
   to the same requirement) the programme prizes.

## 5. Honest scope — residuals, and the escalation check

**This does NOT bottom out at a new axiom.** It grounds in A1 + A2 + A3 + A6′. Per the round's escalation clause,
no new postulate is invented. Two bridging lemmas remain to be hardened before a clean "derived from A1–A11"
stamp; both follow from existing axioms under standard readings, and neither is a new axiom:

- **R1 (A2 ⇒ closed S³, no boundary).** The {3,3,5} tessellation of S³ is standard mathematics; what needs an
  explicit one-line registration is that CPP *adopts the closed reading* of A2 (vs. an infinite flat R³ tiling).
  Under the closed reading the result is topological (Step 4). Under an open/flat reading the same Q = 0 follows
  instead from the physical boundary condition **D** → 0 at infinity (no net charge at the horizon) — also
  standard, but a boundary condition rather than a topological identity. Either reading delivers Q = 0; the
  closed reading is the stronger, assumption-free one and is consistent with CPP's closed-FRW cosmology.
- **R2 = LEMMA-EU-NEUTRAL-GAUSS (L1).** "The U(1) edge-sector field obeys a local Gauss law ∇·D = ρ sourced
  solely by CP ± polarity." This is the Maxwellian content of A6′'s U(1) edge sector + A3 propagation; it is the
  single load-bearing bridge. Hardening = showing the edge-mode field has a conserved current whose density is
  the CP polarity and admits no other (monopole/auxiliary) sources. Recommended as a registered lemma feeding
  both EU-1 and the broader edge-sector EM treatment.
- **R3 (no-flux-loophole on S³).** Already discharged: H²(S³) = 0 (Step 6, script [2]). No residual.

**Verdict.** Leg-2 global neutrality is **derivable from A1–A11** via the closed-substrate Gauss law, contingent
only on bridging lemma L1 (and the closed-reading registration R1) — a strict upgrade from the 0770 glossary
grounding, with the 10⁻⁹ caveat eliminated for the charge channel. Recommended disposition: promote leg 2 from
*grounded* to *derived (conditional on LEMMA-EU-NEUTRAL-GAUSS)*, and — at panel discretion — register the result
as a theorem. Whether this also lifts the *whole* PRED-C-96 from "framework-conditional" toward "derived" is a
separate question: leg 1 (bath reality) and the FRW/VSL homogeneity input (the core of OPEN-EU-1) are untouched
here, so the headline count and conditional status are **unchanged** by this window's result.

## 6. Pointers

- Requirement: `neutrality_grounding.md` (0770) §"What leg 2 needs"; interacting MC 0756.
- Axioms used: A1 (± polarity), A2 (600-cell ≅ S³ tessellation, closed), A3 (DI-bit field), A6′ (U(1) edge sector).
- Topology: 600-cell {3,3,5} = S³ tessellation; Betti(S³) = (1,0,0,1); script `scripts/1300_neutrality_topology.py`.
- Standard physics analog: total electric charge of a spatially-closed universe = 0 (compact-manifold Gauss law).
- Reasoning fragment: `reasoning/1300_neutrality_derivation.md`.

---

## REGISTRY HANDOFF NOTE (no shared files touched this round)

*The round forbids editing shared registries / `frontier_sectors/`. The following are the updates this result
**implies**, for the integrator to apply (or reject) after panel review.*

**`frontier_sectors/SR.md`** — under the OPEN-EU-1 block, add a leg-2 sub-entry:
> *Leg-2 (DP-pair charge neutrality) — derivation attempt (Patch 1300, W3): global ± balance (n₊ = n₋, Q = 0 at
> all occupations) **derived** from A1 + A2 (closed-S³ substrate) + A3 + A6′ via the closed-manifold Gauss law,
> independent of the DP-pair glossary route; the mean-field Coulomb term ∝ Q² vanishes identically. No new axiom.
> Residual: bridging LEMMA-EU-NEUTRAL-GAUSS (edge-sector U(1) local Gauss law) + closed-reading registration of
> A2. The 10⁻⁹ caveat in 0770 is reassigned to the baryon/matter sector (does not source the Coulomb term).
> Does NOT close OPEN-EU-1 (homogeneity + ZRP-correction untouched); does NOT change the PRED-C-96 count/status.*
> Update the leg-2 status token: **grounded → derived (conditional on LEMMA-EU-NEUTRAL-GAUSS).**

**`theorem-registry.md`** — *proposed* new entries (panel sign-off required; this window registers nothing):
> - **THEO-EU-NEUTRAL (proposed):** "On the closed 600-cell (S³) substrate, the total electric charge sourced by
>   ± CP polarities under the U(1) edge-sector Gauss law vanishes identically and is conserved; hence n₊ = n₋ at
>   all occupations." Hypotheses: A1, A2 (closed reading), A3, A6′, LEMMA-EU-NEUTRAL-GAUSS. Supports EU-1 leg 2.
> - **LEMMA-EU-NEUTRAL-GAUSS (proposed):** "The U(1) edge-sector field obeys a local Gauss law ∇·D = ρ with CP ±
>   polarity as its sole source (no free monopoles)." Follows from A6′ (Maxwellian U(1)) + A3. Load-bearing for
>   THEO-EU-NEUTRAL; reusable across the edge-sector EM treatment.
> Note the standing **no-THEO-for-conditional** discipline: register THEO-EU-NEUTRAL only if the panel accepts L1
> as discharged (or accepts the conditional-on-L1 phrasing); otherwise keep leg 2 at "derived (conditional)".

**`predictions.md` / `problem_histories/PH-OPEN-EU-1.md`** — no count change. Optional: footnote PRED-C-96 §1 that
leg 2 now has an independent topological derivation (L1-conditional), and log the leg-2 sub-mark progress in the
PH-OPEN-EU-1 history. Headline **108 unchanged**; PRED-C-96 status **unchanged** (homogeneity leg still open).

**Axiom registry** — **no change** (no new axiom; A1+A2+A3+A6′ only).
