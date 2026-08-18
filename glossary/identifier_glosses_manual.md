# Hand-written identifier glosses

**Registered Patch 3211.** Plain-language glosses for programme identifiers
that have **no** `**One-line statement:**` in `research_frontier.md` or
`frontier_sectors/`. The other identifiers are harvested automatically from
those files — do not duplicate them here.

Each gloss was written from an actual usage site in the corpus, not inferred
from the identifier's name. Format is `ID | gloss`, one per line, `#` for
comments. Entries marked *(family)* are wildcard stems (`OPEN-CHIR-*`) rather
than single problems.

Edit this file to improve a gloss; then re-run
`python3 code/identifier_glossary.py --build`.

```
OPEN-FP-SF-2 | (family) Open problems of the SF-2 electroweak flagship, chiefly the first-principles derivation of the per-boson holographic dilution factor on absolute electroweak boson masses.
OPEN-DM-DSPH-1 | The reopened missing-physics arc in the dwarf-spheroidal dark-matter analysis, behind which that paper's revision is deferred.
OPEN-FP-1-P3 | An open problem of the SF-1 charged-lepton flagship, inherited openly by later flagship papers rather than resolved.
OPEN-CORPUS-EIGENVAL-CORRECTION | A corpus-wide correction to a spectrum claim in QM-6, parallel to the SF-4 v3 to v3.1 correction.
OPEN-P-EW-1 | An electroweak-corpus open problem feeding the derivation of the cosmic-horizon embedding factor of order ten to the minus seventeen.
OPEN-P-EW-3 | An electroweak-corpus open problem inherited as open, alongside the continuum-limit vector-minus-axial closure.
OPEN-CHIR-F1-LINK | Whether the PCD winding is derived from the chirality director (Scenario A) or is an independent primitive (Scenario B).
OPEN-CHIR | (family) The downstream chirality-derivation programme registered by the chirality structural audit.
OPEN-COSM | (family) Cosmological problems targeting a substrate derivation of the baryon asymmetry.
OPEN-COSMO-DM-3 | The condition on which the corona-dilution risk is retired in the dark-matter cross-section analysis.
OPEN-FP-F1-3 | Publication-grade hardening of identity G1, the 600-cell first-shell inner-product primitive, currently at sketch-document rigour.
OPEN-FP-F1-7 | A reserved identifier for a possible new open problem beyond the F1-5 trajectory, should higher-order extensions be pursued.
OPEN-FP-F1-N | A reserved identifier for a future higher-order extension of the F.1 geometric primitives, should that become a programme priority.
OPEN-FP-SF-2-W0-1 | The first of four open problems on the neutral-W integration in the electroweak flagship.
OPEN-FP-SS | (family) Strong-sector open problems that intersect the chirality programme.
OPEN-EU-1 | An axiom-level derivation of FRW and variable-light-speed homogeneity together with the exact zero-range-process correction; registered, not closed.
OPEN-SR-10 | Exact emergent Lorentz covariance: a viability result at world-call strength rather than a theorem, resting on a hopping-sum proxy.
OPEN-SS-15 | The open step on the z-squared multiplicity in the string-tension derivation.
OPEN-SS-22 | An SS-sector structural hypothesis registered for programme-level closure rather than derived in the paper that raises it.
OPEN-SS-28 | An SS-sector structural hypothesis registered for programme-level closure rather than derived in the paper that raises it.
OPEN-SS-2X | (family) Structural hypotheses at the SS-7 inheritance tier, none derived from the axioms in the paper that registers them.
OPEN-SS-43 | A de-novo derivation of the screening length as a function of rung count, on which the dwarf-core result is conditional.
OPEN-SS-B1 | Layer-4 axiomatic derivation and second-order extension of the Mechanism-A minimal-local framework.
OPEN-P-SM-7-1 | The relationship between the bare strong coupling derived in SM-7 and the running coupling at higher scales.
OPEN-P-SM-7-2 | An explicit construction of the self-energy operator from the 600-cell Green's function, analogous to the SM-6 isotropy proof.
OPEN-QMRG-B1 | The B1 dynamical energy-balance derivation, closed at proportionality grade rather than for every microscopic realisation.
OPEN-QMRG-B1-CONST | The exact coefficient of the canonical normalisation in the B1 energy balance.
OPEN-QMRG-ETA | Mode-independence and the geometric constant in the quantum-mechanics re-grounding arc.
OPEN-QMRG-R4-MULTILINK | The multi-edge-correlated transport kernel question, spun off from the shipped component-diagonal transport class.
OPEN-QMRG-UNIQ | Whether alternative register structures, such as higher-dimensional orientation or discrete cyclic counts, are excluded by the substrate axioms.
OPEN-C23-MAGNETIC-SECTOR-VALIDATION | Numerical validation of the derived magnetic sector; the curl construction and its normalisation are analytic and as yet unmeasured.
OPEN-ORG-012 | Conversion of the SS-9 working draft to LaTeX; retired when SS-9 v0.1 shipped.
```

## Batch 2 — added Patch 3213 (THEO-, FI-, PRED-, CONJ-, PH- families)

```
THEO-DSL-5 | A Dynamical Substrate Law theorem giving a real coefficient in the substrate rate function at the host vertex.
THEO-DSL-6 | The order-10 stabilizer of an oriented first-shell edge in the icosahedral group at the host vertex.
THEO-DSL-7 | Umbrella registration covering first- and second-order edge-aligned coefficient content in the Dynamical Substrate Law.
THEO-DSL-8 | The cross-shell edge orbit closure under the reflection stabilizer of face-aligned Reading C.
THEO-DSL-9 | The candidate coefficient theorem for the face-aligned branch of the substrate law.
THEO-DSL-10 | A Dynamical Substrate Law theorem confirmed by multi-model review.
THEO-DSL-11 | A Dynamical Substrate Law theorem with empirical validation carried out at fourth order.
THEO-DSL-12 | A Dynamical Substrate Law theorem in the registered series running from DSL-1 to DSL-12.
THEO-DSL | (family) The Dynamical Substrate Law theorem series.
THEO-DSL-N | (family) A proposed family registration for the shell-perpendicularity pattern that recurs at every perturbative order.
THEO-CHIR-CHI-1 | The substrate chirality magnitude result fixing the golden-ratio power of the chirality parameter.
THEO-CHIR-MERGE-1 | The first of the chirality merge theorems, unifying parity and time-reversal structure.
THEO-CHIR-MERGE-2 | The chirality merge theorem giving the cycle sign as the product of the director and offset signs.
THEO-CHIR-STATUS-1 | The first chirality status capstone, recording what the chirality programme had established.
THEO-CHIR-STATUS-2 | The chirality status capstone identifying the order parameter as the sign of the 4D director.
THEO-CHIR-TARROW-1 | The temporal-arrow status theorem unifying parity-face and time-face structure under substrate CPT.
THEO-CHIR-TARROW-2 | The successor temporal-arrow theorem in the chirality series.
THEO-CHIR-AUDIT-1 | The chirality structural audit theorem.
THEO-CHIR-CAP-1 | The Capotauro-sector chirality theorem.
THEO-CHIR-BRIDGE-1 | The first bridge theorem linking the chirality sector to the electroweak sector.
THEO-CHIR-VW-1 | The first theorem on the Vafa-Witten route in the chirality programme.
THEO-CHIR-VW-2 | The theorem marking the reachable boundary of the Vafa-Witten route.
THEO-CHIR-PCD-ORIENTATION-1 | A candidate theorem deriving the PCD winding orientation from the chirality director.
THEO-CHIR-CONT-4 | A candidate Layer-4 continuum theorem covering the temporal arrow.
THEO-CHIR-CONT-5 | A candidate Layer-4 continuum theorem covering cosmological vacuum asymmetry.
THEO-CHIR-CONT | (family) Layer-4 continuum-EFT chirality theorems.
THEO-CHIR-CONT-N | (family) The naming convention for Layer-4 continuum-EFT chirality theorems.
THEO-SD-CHIR-3 | A substrate-level chirality theorem reserved for future work.
THEO-SD-CHIR-4 | A candidate substrate-level chirality theorem linked to the Q7 question.
THEO-SD-CHIR-N | (family) The naming convention for cross-sector substrate chirality unification theorems.
THEO-CAP-N | (family) The naming convention for sector-specific Capotauro theorems, as distinct from cross-sector ones.
THEO-SF7-CONSIST-1 | A pairwise consistency theorem between two flagship papers, checking shared observables are sourced consistently.
THEO-SF7-CONSIST-2 | The consistency theorem between the charged-lepton and electroweak flagships.
THEO-SF7-CONSIST-3 | The consistency theorem between the strong-sector and electroweak flagships.
THEO-SF7-CONSIST-4 | The consistency theorem between the gravitation and electroweak flagships.
THEO-SF7-CONSIST-5 | The consistency theorem between the electromagnetism and electroweak flagships.
THEO-SF7-CONSIST-6 | The consistency theorem between the gravitation and strong-sector flagships.
THEO-SF7-CONSIST-7 | The consistency theorem between the charged-lepton and neutrino flagships.
THEO-SR-EIN-1 | The Completion Theorem of the relativity-to-Einstein sequence.
THEO-SR-EIN-2 | The Statics Theorem of the relativity-to-Einstein sequence.
THEO-SR-EIN-3 | The transverse-traceless response, or cancellation, theorem.
THEO-SR-EIN-4 | The Operational-Energy Lemma of the relativity-to-Einstein sequence.
THEO-FP-F1-3 | The first-shell inner-product primitive theorem of the F.1 geometric series.
THEO-SS | (family) Strong-sector theorems; a conjecture is promoted into this series once its open step closes.
FI-C-1 | One of the ten foundational inputs of Capotauro v1.0.
FI-C-2 | The foundational input supplying the K3 base structure used in the composite matrix element.
FI-C-3 | The foundational input supplying the perpendicular-wavefunction structure carrying chirality content.
FI-C-4 | A foundational input combining with FI-C-3 and FI-C-5 to carry chirality without further projection.
FI-C-5 | A foundational input combining with FI-C-3 and FI-C-4 to carry chirality without further projection.
FI-C-6 | The foundational input supplying the perpendicular-wavefunction factor on the twelve-vertex icosahedral cage.
FI-C-7 | The chirality-eigenvalue matching principle identifying the relevant generator eigenvalue.
FI-C-8 | The baryon asymmetry taken as empirical input rather than predicted.
FI-C-9 | The substrate chirality magnitude, a free-magnitude postulate at v1.0 later grounded at v2.0.
FI-C-10 | The last of the ten foundational inputs of Capotauro v1.0, extending cage-shell structure to chirality observables.
FI-C-N | (family) The Capotauro foundational-input inventory; at v1.0 all sat at postulate status, at v2.0 they are graded by epistemic standing.
FI-C-RC-1 | The substrate primitive: a preferred 4D direction in the ambient space where the 600-cell substrate sits, sourcing all parity-sensitive observables.
FI-C-RC-2 | The vertex-aligned reading identifying that 4D direction with the host vertex, fixing the local structure as the icosahedral first shell.
FI-CHIR-CONT-1 | The substrate primitive 4D direction, as inherited at continuum-EFT level.
FI-CHIR-CONT-2 | The substrate chirality magnitude, derived at v2.0 rather than postulated.
FI-CHIR-CONT-3 | The substrate residual symmetry at the host vertex.
FI-CHIR-CONT-9 | The substrate-locality inheritance underwriting gauge interaction at continuum level.
FI-CHIR-CONT-10 | A sector specialization of the polytope-geometric invariants at continuum level.
FI-CHIR-CONT-11 | The Yang-Mills effective-field-theory framework input.
FI-CHIR-CONT-12 | The continuum-EFT chirality-projection structure input.
FI-CHIR-CONT-13 | A sector specialization of the polytope-geometric invariants at continuum level.
FI-CHIR-CONT-14 | The effective free-energy and partition-function framework input for the electroweak sector.
FI-CHIR-CONT-15 | The last of six sector-specific foundational inputs introduced for the continuum sectors.
FI-K-1 | The K3 spectrum, inherited at SM-3 level, as an input to the composite cage-shell theorem.
FI-K-2 | The neutrino identification, inherited at SM-5 level.
FI-K-3 | The K3 base structure, inherited at SM-1 level.
FI-K-4 | The 600-cell distance-shell structure measured from the K3 centroid.
FI-K-5 | The cage-shell mass formula inherited from the neutrino flagship at v3.0.
FI-K-6 | The charged-lepton vertex identification, inherited at SM-4 level.
FI-QMRG-1 | The founder-anchored input that the quantum register is the directional content of the net space-stress vector in the distinguished plane.
CONJ-CHIR-1 | The chirality conjecture discharged, conditional on an interpretive premise, by the first chirality bridge theorem.
CONJ-COSMO-1 | The conjecture that cosmological dark matter consists of charge-neutral substrate aggregates of quark-sector dipole pairs and hybrid tetrahedra.
CONJ-SM-9-2 | A conjecture registered in the axiom registry for the SM-9 sector.
CONJ-SS-2-1 | The heuristic string-tension formula of SS-2, carried as a conjecture.
CONJ-SS-5 | A strong-sector conjecture promoted from an open problem, awaiting one step to become a theorem.
CONJ-SS-10 | The single-bond binding formula of v0.1, superseded by CONJ-SS-11.
CONJ-SS-11 | The nuclear binding conjecture resting on a cascade reinforcement factor and a Pauli penalty coefficient not yet derived from primitives.
CONJ-SS-12 | A structural conjecture relating nuclear binding to Euler's formula for simplicial polytopes.
CONJ-SS-G | (family) Strong-sector gluon-counting conjectures, flagged as forward-looking rather than headline results.
PRED-C-96 | The registered prediction for the scalar spectral index.
PRED-O-16 | The registered prediction extending alpha-chain results to a single larger cluster.
PRED-O-17 | The registered prediction for the transition between single and hierarchical alpha-chain regimes.
PRED-O-18 | The registered prediction for hierarchical slip-plane additivity.
PRED-O-25 | A prediction inherited through the bridge theorem to observable scale.
PRED-O-30 | A registered prediction entering the first-order coefficient closed form.
PRED-O-34 | The registered prediction for the running strong coupling.
PRED-O-35 | A registered gravitational-wave prediction of the relativity sector.
PRED-O-36 | The registered prediction that gravitational-wave propagation speed is exactly the speed of light.
PRED-O-37 | The registered prediction of multiplet integrity under the protection theorem.
PRED-O-38 | The registered prediction of no helicity-dependent vacuum dispersion.
PRED-O-35--38 | (family) The four registered gravitational-wave predictions of the relativity sector.
PH-OPEN-SS-22 | The problem history of a retired open problem whose empirical anchor proved to be an isotope-selection artifact.
PH-OPEN-SS-26 | The problem history recording a programme-level proximity-binding question raised by a Level-3 gap.
```
