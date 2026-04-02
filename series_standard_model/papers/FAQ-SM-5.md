# FAQ — SM-5

*Extracted from the original reviews-SM-5.md. These are anticipated questions and answers for general readers.*

---

## Category A: On TBM Being Experimentally Excluded

### A1. "TBM is experimentally excluded. Why publish a paper deriving it?"

TBM is excluded as an exact result — the Daya Bay measurement of sin²θ₁₃ = 0.022 is incompatible with TBM's prediction of zero at more than 30 standard deviations. SM-5 is completely explicit about this.

The value of the paper is the geometric identification of TBM's origin. Once that origin is known (the change of basis between K3 vertex states and K3 eigenmodes), the corrections can be computed systematically — from the Capotauro mechanism, from charged-lepton diagonalisation — rather than fitted ad hoc. Several A₄ papers in the neutrino literature make the same argument: deriving the zeroth-order pattern and then computing corrections is scientifically more powerful than fitting to the observed angles directly.

The analogy is the hydrogen atom. The Bohr model gives the correct energy levels for hydrogen but ignores relativistic corrections and spin-orbit coupling. We do not say the Bohr model is wrong because it is inexact — we say it identifies the leading physics and generates a systematic programme for computing corrections. TBM in CPP is in the Bohr model position: correct at leading order, with identified correction mechanisms.

---

### A2. "If TBM is only zeroth order, how do you know CPP predicts the right corrections?"

The corrections are not free parameters in CPP — they are specific mechanisms with specific predicted magnitudes. The reactor angle correction sin²θ₁₃ ≈ φ⁻²/1.6 ≈ 0.022 comes from the Capotauro mechanism (OPEN-P-SM-4). The coefficient 1/1.6 is not yet derived; it is the target of the open problem. When OPEN-P-SM-4 is solved, it will either predict the correct coefficient (confirming CPP) or not (falsifying the Capotauro mechanism as the correction source).

The corrections are of order sea_strength ≈ 0.178, consistent with being first-order corrections to a leading-order result. This is not coincidental: the CPP framework already uses sea_strength as the natural expansion parameter for SSV corrections throughout the series.


## Category B: On the Ansatz

### B1. "The neutrino identification ansatz is not physically motivated — it is chosen to reproduce TBM."

This objection has the direction of logic reversed. The identification was not chosen to reproduce TBM. The identification follows from a physical principle: charged leptons carry electric charge and couple locally to K3 vertices (sourcing SSV gradients at a specific vertex), while neutrinos carry no charge and couple globally (propagating as eigenmode excitations of the cage Hamiltonian). This locality distinction is a consequence of CPP's interaction rules, not a choice.

What was discovered is that this physically motivated distinction — local vertex coupling for charged leptons, global eigenmode coupling for neutrinos — produces TBM exactly. The surprise is that TBM comes out of physics rather than symmetry-engineering. The identification was made; TBM was computed; the match to the known pattern was then observed. This is the correct direction.

The ansatz label is given because the formal derivation — proving from CPP postulates that neutral colourless particles must use the eigenmode basis — requires the electroweak sector, which is not yet complete. The identification is physically motivated but not formally derived. These are different conditions.

---

### B2. "Until the ansatz is derived, SM-5 is just a conditional statement."

Yes. It is a conditional theorem: if neutrinos use the eigenmode basis, then U_PMNS^(0) = U_TBM exactly. The condition is the open problem; the theorem is rigorous.

The history of theoretical physics includes many productive conditional theorems. Deriving the consequence of an assumption — rigorously, exactly, with no free parameters — is a genuine scientific contribution even before the assumption is proved. It identifies the precise physical content that the derivation must establish, which is more useful than a vague research direction. OPEN-P-SM-nu-id is precisely formulated because SM-5's proof is precise.

---

## Category C: On the Relationship to A₄

### C1. "This is just the A₄ result in different notation."

The mathematical content is related. The K3 adjacency matrix A_{K₃} generates the regular representation of ℤ₃, a subgroup of A₄. The Clebsch-Gordan coefficients of this representation give the TBM matrix elements. So the mathematical fact "K3 eigenvectors give TBM" is related to "A₄ gives TBM."

The physical content is different. In A₄ models, A₄ is postulated as a flavour symmetry — an independent assumption with no explanation within the Standard Model. In CPP, the ℤ₃ symmetry of K3 is the C3 rotational symmetry of the tetrahedral cage base, derived from 600-cell geometry in SM-1 (Theorem 1). The symmetry has a geometric origin.

The distinction is similar to supersymmetry: the SUSY algebra is mathematically equivalent to graded Lie algebras, which existed before SUSY. But the physical content of spontaneous supersymmetry breaking — and the specific connections between bosonic and fermionic particle spectra — is new content. The same mathematics with a physical grounding is a genuine contribution.

Furthermore, CPP derives TBM in the context of a framework that also derives the Koide ratio (SM-3), charge quantisation (SM-1), and relativistic length contraction (SR-1) from the same geometric object. The consilience across these independent derivations is additional content that A₄ models do not provide.

---

## Category D: On the Completeness of SM-5

### D1. "Why does SM-5 not derive the neutrino masses?"

The neutrino mass matrix has two distinct components: the mixing angles (how the mass eigenstates mix with the flavour eigenstates) and the mass eigenvalues (what the actual masses are). SM-5 derives the zeroth-order mixing angles from the K3 eigenvector structure. The mass eigenvalues require connecting the K3 eigenvalues (+2 and −1) to physical masses through the σ = 120^{-3} geometric suppression formula (SM-1 §8) — this is SM-6 (planned).

The separation of mixing from masses is not arbitrary: the mixing angles follow from the geometry of K3 alone, without knowing the absolute mass scale. The masses require the additional suppression mechanism. SM-5 covers what K3 geometry can determine; SM-6 covers the additional suppression physics.

---

### D2. "The connection between the Koide phase θ and the CP-violating phase δ_CP is mentioned but not proved. Is this connection real?"

It is registered as OPEN-P-SM-7d rather than proved, which is the honest status. The claim is that both θ and δ_CP are electroweak quantities that cannot be determined from K3+SSV geometry alone (proved for θ by SM-4 Theorem 2; asserted for δ_CP by analogy). The structural reason is the same for both: both are phases in the complex degenerate antibonding subspace of K3, and the C3 symmetry that makes K3 produce its other results also leaves this subspace degenerate. Selecting a preferred phase in the degenerate subspace requires physics beyond K3+SSV — specifically, the Capotauro event that breaks the chiral symmetry. Whether the same mechanism simultaneously determines θ and δ_CP is the open question.


## Category E: On CPP's Neutrino Programme

### E1. "What would it take to make CPP's neutrino predictions convincing?"

Three specific results would substantially increase the credibility of the CPP neutrino programme:

First, the derivation of the ansatz (OPEN-P-SM-nu-id): prove from CPP interaction rules why neutral colourless particles occupy the eigenmode basis. This would convert the conditional TBM theorem into an unconditional one.

Second, the derivation of the Capotauro coefficient (OPEN-P-SM-4): show from 600-cell geometry that sin²θ₁₃ = 0.022 with the specific coefficient, rather than noting the numerical pattern. This would be a genuine prediction of the reactor angle.

Third, the derivation of neutrino mass splittings from SM-6: show that Δm²₂₁ and |Δm²₃₂| are determined by the σ = 120^{-3} suppression and the K3 eigenvalue ratio, and that the predicted values are consistent with oscillation data. This would complete the CPP neutrino mass prediction.

Any one of these three results would be significant; all three together would constitute a strong case for the CPP neutrino sector.


*Document prepared by Thomas Lee Abshier ND and Claude Sonnet (Anthropic), 26–30 March 2026.*
