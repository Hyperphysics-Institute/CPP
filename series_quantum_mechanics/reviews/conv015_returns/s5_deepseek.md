<!-- CONV-015 return, filed verbatim at Patch 3004. Founder attribution: DeepSeek. Extended thinking preamble preserved (chat archive) — shows deliberation about execution status and concludes correctly that ACCEPTED is the honest declaration. Final status line: ACCEPTED with a claim of having read the sketches/code via raw URLs; its Q1 residue (the 3001 sketch lacks a formal proof/citation of the 5-design property) is CONSISTENT WITH ACTUAL READING — the sketch as committed states the property as a "theorem input" with numerical confirmation but carries no bibliographic citation. Fair criticism; no integrity event. Factual slip noted at adjudication: "SF-6 (which is part of the QM-5 context)" — SF-6 is the EM flagship, not QM-5 context; weighed accordingly on Q3. -->

**Execution Status:** ACCEPTED — I cannot run the scripts to obtain the keys and stdout, but I have examined the provided sketches and code files by reading their content via the raw URLs.

### Q1 — The R-4 package
**Verdict:** CLOSES-WITH-RESIDUE
**Residue:** The package does not prove that the icosahedral neighbor shell is a spherical 5-design; it only measures a slope of 4.00 in a numerical check. A mathematical proof (or citation of a known result) that the icosahedral shell of the 600-cell is a spherical 5-design is missing. Without that, the suppression claim rests on a numerical measurement that could be coincidental for the chosen wave-vectors and kernel class. This residue is **blocking** for a rigorous derivation grade, because the entire suppression argument hinges on the 5-design property.
**Attack on weak points:**
- **W-1:** L-1's exact plane closure for component-diagonal transport is a valid answer to D-4 *for the shipped model*, but D-4 was about the microscopic substrate transport in general. The scoping move is legitimate only if the shipped model's transport class is known to be the only one allowed by the axioms. That has not been proven.
- **W-2:** The restriction to single-edge kernels leaves multi-edge-correlated transport unaddressed. Since the lattice dynamics could involve such correlations, this is a significant limitation.
- **W-3:** L-3's identification of the isotropic (ks)² channel as spin/longitudinal does not lean on the Hopf observation; it is a separate classification. However, if that classification is wrong, the channel could still be a leakage channel, and the suppression argument would not cover it.

### Q2 — The B1 package
**Verdict:** DERIVES-WITH-RESIDUE
**Residue:** The derivation uses AP-2's "intensity-like" clause to decide the quadratic-vs-linear fork. This is a category error: AP-2 is an ontological clause about how the substrate represents information, not a dynamical law. Deciding a dynamical fork by fiat from ontology launders an open question. The residue is **blocking** because the entire amplitude–count relation depends on that fork being dynamically correct.
**Attack on weak points:**
- **W-4:** The toy verification (3002 script) is a helpful illustration but does not carry evidential weight for the lattice. It assumes a single elastic element and a linear-damping approximation for turnover; the O(1) turnover factor is uncomputed. The lattice involves many coupled elements and a different turnover mechanism.
- **W-5:** As above, using AP-2 to decide the fork is illegitimate. The fork should be decided by the equations of motion of the substrate, not by a ratified ontology clause.

### Q3 — The mutual-support prohibition
**Verdict:** RETAIN
**What more is needed:** The prohibition is a hygiene rule to avoid circularity. The B1 package provides an independent derivation, but that derivation itself relies on AP-2 (an ontological clause) and on SF-6 (which is part of the QM-5 context). The derivation is not fully independent of the QM sector's structure. To discharge the prohibition, the amplitude–count relation must be derived from the substrate's dynamical equations without invoking any elements that themselves presuppose the relation (including AP-2's intensity-like clause, which was ratified *after* the QM papers were written and may have been shaped by them).

### Q4 — OPEN-QMRG-UNIQ scoping
**Verdict:** NON-BLOCKING-WITH-CRITERION
**Criterion:** Becomes blocking only if a concrete alternative is proposed that (a) fits the Madelung register mapping (A-2) equally well, and (b) leads to different empirical predictions. Until such an alternative is on the table, FI-QMRG-1 can be treated as an input assumption; the programme must register OPEN-QMRG-UNIQ and revisit if a viable alternative emerges.

### Q5 — THE BAR RULING, round two
**(a) Scope motion:** HOLD-CURRENT-SCOPE
Both packages leave blocking residues (Q1 and Q2). Until the 5-design proof is supplied and the dynamical fork is derived without ontological fiat, the partial scope cannot widen.
**(b) Sector conditionality:** RETAIN-CONDITIONAL
**Trigger:** Resolves only when the residues in Q1 and Q2 are cleared (a mathematical proof of the 5-design property and a dynamical derivation of the quadratic fork). Until then, all QM papers must carry a conditional note referencing these pending derivations.

**Overall:** The packages show rapid progress but are shaped by the adjudication's demands (W-6). They address the letter of the obligations but leave substantive gaps that must be filled before the bar can lift or the sector can be considered unconditionally grounded.
