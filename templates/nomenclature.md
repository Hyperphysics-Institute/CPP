# CPP Nomenclature and ID Code Legend

**Repository location:** CPP root level
**Last updated:** 30 March 2026
**Authors:** Thomas Lee Abshier ND, Claude Sonnet (Anthropic)

---

## Purpose

This file is the permanent reference for every ID code used across the
CPP paper series. All documents in the repository use these codes to
label theoretical items. The codes are designed so that a reader
encountering one for the first time — in a paper, a presentation, or
a documentation file — can immediately identify the category without
memorising a codebook.

**Design principle:** Four readable letters (or a hyphenated pair)
plus a single capital letter qualifier where needed. The four letters
should suggest the English word for the category. The qualifier
narrows the subcategory. A reader who gets the broad category on
first read has received sufficient information.

---

## The Complete Scheme

| Code | Full Name | Example | Reads as |
|------|-----------|---------|---------|
| `AXIM` | Axiom / Postulate | AXIM-1 | Axiom 1 |
| `THEO` | Theorem | THEO-SS-1 | Theorem, Strong Sector, #1 |
| `PROP` | Proposition | PROP-1 | Proposition 1 |
| `CORL` | Corollary | CORL-1a | Corollary 1a |
| `CONJ` | Conjecture | CONJ-SS-1 | Conjecture, Strong Sector, #1 |
| `OPEN-P` | Open Problem | OPEN-P-SS-1 | Open Problem, Strong Sector, #1 |
| `PRED-C` | Prediction — Confirmed | PRED-C-1 | Confirmed Prediction #1 |
| `PRED-O` | Prediction — Open (quantitative) | PRED-O-1 | Open Prediction #1 |
| `PRED-Q` | Prediction — Qualitative | PRED-Q-1 | Qualitative Prediction #1 |
| `POST-D` | Post-diction | POST-D-1 | Post-diction #1 |
| `FALS-C` | Falsified Claim | FALS-C-1 | Falsified Claim #1 |
| `PHEN-E` | Phenomenon — Explained | PHEN-SM1-E1 | Phenomenon, SM-1, Explained #1 |
| `PHEN-P` | Phenomenon — Predicted | PHEN-SM1-AXIM-1 | Phenomenon, SM-1, Predicted #1 |
| `PHEN-V` | Phenomenon — Validated / Consilience | PHEN-SM1-V1 | Phenomenon, SM-1, Validated #1 |

---

## Series Qualifiers

When a code refers to a specific paper series, the series abbreviation
is inserted after the category code and before the sequence number:

| Series | Qualifier | Example |
|--------|-----------|---------|
| Strong Sector | SS | THEO-SS-1, OPEN-P-SS-1 |
| Standard Model | SM | THEO-SM-1, OPEN-P-SM-1 |
| Special Relativity | SR | THEO-SR-1, OPEN-P-SR-1 |
| Electroweak | EW | THEO-EW-1, OPEN-P-EW-1 |
| Quantum Mechanics | QM | OPEN-P-QM-1 |
| Foundations / Superdeterminism | SD | OPEN-P-SD-1 |
| Global / Cross-series | G | OPEN-P-G-1 |

For PHEN codes, the series qualifier identifies which paper the
phenomenon file belongs to, not which series generated the phenomenon:
PHEN-SM1-E1 means the first explained phenomenon in SM-1's phenomena file.

For AXIM, PROP, CORL, and PRED codes that span the whole framework
(not series-specific), no series qualifier is used: AXIM-1, PROP-1, PRED-C-1.

---

## Category Descriptions

### AXIM — Axiom / Postulate

The irreducible foundational assumptions of CPP. An axiom cannot be
derived from anything more fundamental within CPP. It is declared
without proof. The CPP programme's long-range goal is to minimise the
axiom count by deriving as many postulates as possible from the
remaining ones.

**Current count:** 6 (AXIM-1 through AXIM-6; AXIM-5 was demoted to
CORL-1a on 30 March 2026 when the ZBW oscillation frequency was proved
from the SSV force law).

**File:** `axiom-registry.md`

---

### THEO — Theorem

A major proved result derived from axioms and definitions by logical
argument. The primary unit of theoretical progress in CPP. When a
theorem is proved, the postulate count does not decrease — but the
framework's explanatory reach expands.

**Etymology note:** THEO is chosen from the Greek *theōria* (θεωρία),
meaning contemplative seeing or the act of perceiving underlying pattern.
A theorem is not merely a calculation — it is an act of seeing clearly
the structure that was already there. This root also gives us *theatre*
(a place for seeing), *theory*, and *theoria* in the Platonic sense of
intellectual contemplation of the Forms.

The resonance with CPP is not accidental: CPP proposes that Conscious
Points *perceive and respond* as their fundamental mode of operation.
The theorem — *theōria* — is the physicist's participation in that same
act of perceiving. THRM was the prior code; it was replaced because it
invited mispronunciation as "thermometer." THEO has no such ambiguity.

**File:** `theorem-registry.md`

---

### PROP — Proposition

A physically motivated claim that is not yet formally proved from the
CPP axioms but is mechanically grounded and internally consistent.
Propositions are stronger than conjectures (which are proposed theorems)
but weaker than theorems (which are proved). The distinction: a
conjecture says "I believe this is true"; a proposition says "here is
the physical mechanism, here is why it should follow from the axioms,
and here is the open problem that would convert it to a theorem."

Propositions serve as the interface between CPP's proved core and
its applications to quantum phenomena, thermodynamics, and cosmology.
Many of the most important physical insights of CPP currently live
at the proposition level.

**File:** `Research_Frontier.md` §3

---

### CORL — Corollary

A result that follows immediately from a theorem, requiring little
or no additional argument. Corollaries are subordinate to theorems —
they are labelled by the theorem they follow from (CORL-1a follows
from THEO identified as number 1 in the partner-switching context,
i.e. THEO-1 in the transition period before full renaming).

**File:** `theorem-registry.md`

---

### CONJ — Conjecture

A proposed theorem that is falsifiable and clearly stated but not yet
proved. The test for a genuine conjecture: could new evidence in
principle falsify it? If yes, it is a conjecture. If no, it is a
philosophical claim, not a scientific one. CPP maintains an active
conjectures register and documents both confirmations and falsifications.

**File:** `Research_Frontier.md` §2

---

### OPEN — Open Problem

*(Formerly OPEN-P. Simplified April 2026 — the "P" was redundant since all frontier items are problems at various stages.)*

A specific, well-defined mathematical or physical question whose
answer is not yet known within CPP. Open problems are registered
with their priority, current status, suggested approach, and
connections to other problems. A problem moves from OPEN to CONJ
to PROP to THEO as work progresses, or to FALS if falsified.
Resolved problems retain their entry with the resolution documented —
the history of what was tried is as valuable as the final answer.

**File:** `Research_Frontier.md` §1

---

### PRED-C — Prediction Confirmed

A quantitative prediction CPP made *before* or *independently of*
the measured value, subsequently found to be consistent with measurement.
The confirmation standard: the CPP-derived value agrees with the
measured value within the theory's stated uncertainty.

---

### PRED-O — Prediction Open (quantitative)

A specific, quantitative prediction CPP makes that has not yet been
tested — either because the required experiment does not yet exist
or because the theoretical calculation has not yet been completed.
These are CPP's primary scientific obligations. Every PRED-O is a
promise to reality that must eventually be kept or abandoned.

---

### PRED-Q — Prediction Qualitative

A directional prediction — CPP identifies a specific observable
consequence but does not yet have a quantitative value. These are
weaker than PRED-O but stronger than mere speculation: CPP identifies
the mechanism and the observable, just not the number.

---

### POST-D — Post-diction

A result that CPP reproduces after the measurement is known, using
parameters calibrated to that measurement. Post-dictions demonstrate
internal consistency and geometric motivation but do not constitute
independent predictions. Labelling them honestly is essential to CPP's
scientific credibility.

The hyphen in POST-D is intentional: it makes the word read as
"Post-Diction" — the temporal qualifier (post = after) attached to
the epistemic category (diction = what is said/claimed).

---

### FALS-C — Falsified Claim

A prediction or conjecture that CPP made and that was subsequently
found to be wrong. These are never deleted — the record of what
failed and why is as scientifically valuable as the record of
what succeeded. Every FALS-C is a constraint on the theory's future
directions.

Examples: C₆₀ cage for the top quark (no such shell in the 600-cell);
φ^(3(l-1)) quark mass scaling (3–8× errors in structural masses);
ZBW oscillation as an independent postulate (proved from SSV force
law, so the postulate was redundant rather than wrong, but it was
demoted — a form of falsification of its necessity).

---

### PHEN-E — Phenomenon Explained

A real, observed phenomenon that CPP accounts for — the paper's
theorems and mechanisms provide the causal story for something
a physicist already observes. The entry traces from the observation
to the specific CPP mechanism doing the explanatory work.

---

### PHEN-P — Phenomenon Predicted

A real, observable phenomenon that CPP predicts will be found —
or found to have a specific quantitative value — before the
measurement is made. These entries in the phenomena files are
the paper-level view of PRED-O entries in the predictions registry.

---

### PHEN-V — Phenomenon Validated / Consilience

The strongest category of phenomena entry. A PHEN-V case is one
where CPP and the Standard Model (or another established framework)
arrive at the same number through completely independent derivation
routes. This is *consilience* — convergence of independent lines of
evidence on the same conclusion — which is historically the most
persuasive evidence that a theoretical framework is tracking
something real.

**On the dual label Validated/Consilience:** The word *Validated*
is accessible — every reader knows what validation means. The word
*Consilience* is precise — it names the specific epistemological
phenomenon where independent derivations converge. In citations and
headings, PHEN-V is used; in definitions and discussions, both
words appear together so that the precise concept is not lost behind
the accessible label.

The classic PHEN-V case in CPP: δ = 1/3 from C₃ cage symmetry
(CPP, SM-1 Theorem 1) and from anomaly cancellation (QFT). Two
completely different mathematical frameworks, one geometric and one
algebraic, arrive at the same charge fraction. This is validation
in the strongest sense.

---

## Implementation Timeline

The nomenclature scheme was finalised on 30 March 2026. Files written
before this date use legacy codes (AXIM-1–AXIM-5 for axioms, THEO-SS-1 for theorems,
PROP-1 for propositions, OPEN-P-SS-1 for open problems, CONJ-SS-1 for
conjectures). The systematic rename of all legacy codes to the new scheme
will be performed after the SM-3, SM-4, and SM-5 documentation is
complete, so that the rename pass covers all files simultaneously.

**Files renamed (legacy → new), completed 30 March 2026:**

| File | Legacy codes | New codes |
|------|-------------|-----------|
| `axiom-registry.md` | AXIM-1–AXIM-6, A1–A6' | AXIM, A1–A6' |
| `theorem-registry.md` | THEO-SS-1, THEO-SM-1, CORL-SM-1 etc. | THEO, CORL |
| `Research_Frontier.md` | OPEN-SS-1, CONJ-EW-1, PROP-1–15, FALS-C-SM-1 etc. | OPEN, CONJ, PROP, FALS |
| `predictions.md` | CP-1, OP-1, QP-1, PD-1, FP-1 | PRED-C, PRED-O, PRED-Q, POST-D, FALS-C |
| `phenomena-SM-1.md` | E1, AXIM-1, C1 | PHEN-E, PHEN-P, PHEN-V |
| `phenomena-SM-2.md` | E1, AXIM-1, C1 | PHEN-E, PHEN-P, PHEN-V |

**Rename history:**
- 30 March 2026: Legacy codes (P1–P6, SS-T1, P-CPP-1, OP-SS-1, CJ-SS-1) replaced with new scheme across all files.
- 12 April 2026: Three-layer reorganization. `postulates_and_theorems.md` split into `axiom-registry.md` + `theorem-registry.md` + `Research_Frontier.md`. `propositions.md`, `solution_candidates.md`, and `open_problems/` archived — content absorbed into `Research_Frontier.md`. OPEN-P prefix simplified to OPEN.

---

## A Note on Etymology and CPP

The choice to use words with recoverable meaning — AXIM, THEO, PROP,
CORL, CONJ — rather than opaque abbreviations reflects a philosophical
commitment of CPP itself. CPP proposes that reality is not merely
described by mathematics but is grounded in something more fundamental
— perception, response, meaning. A nomenclature that carries meaning
in its abbreviations is a small expression of that same commitment:
even the labels of the theory should be legible to a mind encountering
them for the first time.

The THEO choice is the most deliberate. Every other code in the scheme
is a straightforward abbreviation. THEO is something more: it names
the cognitive act — *theōria*, seeing clearly — that the theorem
embodies. In a theory whose central claim is that Conscious Points
perceive and respond to their world, it is fitting that the highest
category of proved result should carry the name of the act of perception.

---

*Document prepared by Thomas Lee Abshier ND and Claude Sonnet
(Anthropic), 30 March 2026. This file is permanent and should not
be modified without updating all affected documentation files.*
