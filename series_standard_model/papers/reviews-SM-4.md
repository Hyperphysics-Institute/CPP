# Reviews and FAQ: SM-4 — Charged Lepton Masses from the K3 Spectral Theorem

**Series:** 600-Cell Standard Model Emergence
**Document type:** Living review record and FAQ
**Last updated:** 30 March 2026


# PART 1: FORMAL REVIEWS


## Review 1: Claude Sonnet Internal Review and Harmonisation (March 2026)

**Reviewers:** Claude Sonnet (Anthropic) — iterative review across sessions
**Date:** March 2026
**Context:** SM-4 was written after the iterative sessions that developed
SM-3. The paper's main revisions concerned precision of language (prediction
vs consistency check), the formal proof of Theorem 2, and harmonisation.


### Objection 1.1: The Consistency Check Was Presented as a Prediction

**The objection:** Early versions described the 0.004% and 0.001% mass
agreements as CPP predictions. Since A and θ are calibrated from the same
PDG data used to evaluate the agreement, these are consistency checks, not
independent predictions.

**Assessment: VALID — fundamental distinction**

A prediction uses derived or separately calibrated inputs to forecast an
untested value. A consistency check confirms that a constraint is satisfied
by data already used in calibration. SM-4 calibrates A and θ from all three
lepton masses and then confirms that the Koide formula holds to 11 ppm.
The non-trivial content is that one derived constraint (K = 2/3) reduces
three parameters to two without inconsistency.

**Response/revision (v5):** Language changed throughout. The Proposition in
§3 is now "Lepton mass consistency check at 11 ppm." A Remark explicitly
states that the residuals reflect how precisely nature satisfies K = 2/3,
not the precision of a CPP prediction.

**Status: RESOLVED**


### Objection 1.2: Theorem 2 (Structural Impossibility of θ) Was Absent

**The objection:** Early versions noted that θ is "not derived" from K3+SSV
and registered OPEN-P-SM-7d, but without proving the structural reason. This
left open the possibility that θ could still be found within the framework.

**Assessment: VALID — the negative result is the paper's deepest content**

After 11 mechanisms were tested and falsified (Sessions B through L of SM-3
development), the structural reason emerged: C3 symmetry protects the
antibonding degeneracy exactly. A formal proof was needed.

**Response/revision (v5):** Theorem 2 added with the Löwdin downfolding
proof. Key steps: effective Hamiltonian H_eff(E) = A_{K₃} − (1/E) v vᵀ;
apex darkness ⟨φ₋|v⟩ = 0 exactly; antibonding eigenvalues remain −1 for all
E; θ is structurally undetermined.

**Status: RESOLVED**


### Objection 1.3: Parameter Counting Was Implicit

**The objection:** The paper used "two free parameters" without making the
count explicit or showing where each comes from.

**Assessment: VALID — clarity**

**Response/revision (v5):** The Remark in §2 explicitly audits the count:
three initial parameters (m_e, m_μ, m_τ); SM-3 derives ρ = √2 (reduces to
two); SM-4 calibrates A from m_e and θ from PDG (both calibrated, zero
remaining). Goal state after EW: one calibrated (A from m_e), one derived (θ).

**Status: RESOLVED**


### Objection 1.4: Series Harmonisation

**The objection:** "Paper 3" and "Paper 4" references; incomplete author
line; no bibliography; incorrect series name.

**Assessment: VALID**

**Response/revision (v5):** Eight harmonisation changes (H1–H8): series ID,
author line, institution, date, packages, bibliography, acknowledgements,
reference updates from "Paper N" to "SM-N."

**Status: RESOLVED**


## Summary Table

| # | Objection | Assessment | Status |
|---|-----------|-----------|--------|
| 1.1 | Consistency check labelled as prediction | Valid — fundamental | Resolved (v5) |
| 1.2 | Theorem 2 absent | Valid — deepest result | Resolved (v5) |
| 1.3 | Parameter counting implicit | Valid — clarity | Resolved (v5) |
| 1.4 | Series harmonisation | Valid — standard | Resolved (v5) |


# PART 2: FAQ — CONVENTIONAL PHYSICS PERSPECTIVE

---

*FAQ content has been moved to FAQ-SM-4.md.*
