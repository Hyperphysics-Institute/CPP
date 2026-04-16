# FAQ — SM-3

*Extracted from the original reviews-SM-3.md. These are anticipated questions and answers for general readers.*

---

## Category A: On the Koide Formula Itself

### A1. "The Koide formula is a numerological curiosity — it works for three numbers, and with three numbers you can always find a relation."

This objection has real force for weak relations, but not for the Koide formula specifically. The formula is not a loose fit — it holds to 11 ppm. The masses span a factor of 3477 (electron to tau), and the formula constrains all three simultaneously with a single equality. Any formula of the form f(m₁, m₂, m₃) = constant for three numbers can be trivially constructed after the fact. What makes Koide different:

First, the formula was noted in 1982 when only the electron and muon masses were known precisely. The tau mass prediction was within the error bars at the time and has remained consistent as measurements improved. The formula has survived 40 years of increasingly precise measurement — this is not the behaviour of a lucky coincidence.

Second, the CPP derivation does not use any of the three lepton masses as input. It derives K = 2/3 from the graph spectrum of an equilateral triangle, completely independently of the measured values. The fact that the measured ratio equals the derived ratio to 11 ppm is either a remarkable coincidence or evidence that the geometric derivation is capturing something real about lepton mass structure.

Third, the 11 ppm agreement is specific enough to be falsified by measurement improvement. If future mass measurements find K ≠ 2/3 at the 10 ppm level, SM-3 is wrong. A relation that can be falsified is not numerology.

---

### A2. "Yoshio Koide proposed the formula 40 years ago. Why has no one derived it before CPP?"

The standard approaches in theoretical physics — supersymmetry, extra dimensions, technicolor, flavour symmetries — all look for the origin of the Koide ratio in symmetries of the Lagrangian, in representations of gauge groups, or in fixed points of renormalisation group equations. These approaches have not succeeded because the Koide formula is not a symmetry of the Lagrangian in any obvious way.

SM-3 approaches from a completely different direction: the formula arises from the graph spectrum of the lattice substructure that the CPP framework identifies as the cage base. This is not a Lagrangian symmetry approach — it is a geometric approach in which the "symmetry" responsible is the C3 rotational symmetry of an equilateral triangle.

The reason this was not found before is that deriving it this way requires both the prior identification of the equilateral triangle as the relevant structure (which itself required the full CPP cage picture) and the recognition that the eigenvalue ratio 2:1 maps directly onto the Koide modulation depth ρ = √2 via P3 equipartition. Neither step is accessible without the CPP framework.

---

## Category B: On the Three Propositions

### B1. "P3 (thermal equipartition) seems too convenient — you need the eigenstates to be equally populated to get ρ = √2, and you obtain this by choosing the right temperature limit."

P3 is not chosen to get the right answer — it follows from the physical temperature of the system. The DP Sea temperature is T ≈ T_Planck. The ZBW energy scale is ℏω₀ ≈ 88 MeV. The ratio kT_P/ℏω₀ ≈ 10²⁰. For any system where kT >> Δε (the energy level spacing), the Boltzmann distribution approaches the uniform distribution regardless of the specific energy values. This is not a convenient choice — it is an unavoidable consequence of the DP Sea being at the Planck temperature.

The objection would be valid if CPP had chosen the temperature to get equal occupation. CPP did not — the Planck temperature is fixed by the Absolute Moment (t_P ≈ 5.39 × 10⁻⁴⁴ s gives T_P = ℏ/k_B t_P ≈ 1.42 × 10³² K), and the ZBW energy scale is fixed by sea_strength and r_conf. Their ratio being 10²⁰ is a consequence of CPP's basic scales, not a tunable parameter.

**Epistemic status (v6):** The statistical mechanics of the high-temperature limit is standard and uncontroversial. What remains as a Layer B assumption is the chain from CPP's DI-bit exchange mechanism to a full Gibbs thermal state — specifically, the Caldeira–Leggett coupling form, the rapid thermalisation timescale, and whether the coupling produces full Gibbs equilibration rather than dephasing only. These are modelling choices consistent with CPP but not yet derived from CPP primitives. See SM-3 §3.2 for the explicit Layer B decomposition.

**Robustness (v6):** At finite temperature, the exact departure from equal occupation is |c₋|²/|c₊|² = 2e^{3x} where x = ℏω₀/kT_P ~ 10⁻²⁰. The correction to K = 2/3 is of order 10⁻²⁰ — algebraically tiny, nine orders of magnitude below the 11 ppm experimental precision.

---

### B2. "P2 (mass proportional to |ψ|²) is just the Born rule renamed for mass. You are postulating quantum mechanics within CPP."

P2 is not postulated — it is derived from the CPP DI-bit visit rate (Layer A). The ZBW orbital spends a fraction |ψᵢ|² of its time at vertex Vᵢ (this is standard quantum mechanics applied to the finite K₃ system). Mass = stored ZBW energy. The ZBW energy stored at Vᵢ per unit time is proportional to the time spent there, which is |ψᵢ|². Hence mᵢ ∝ |ψᵢ|².

The derivation is: time at Vᵢ ∝ |ψᵢ|² (quantum mechanics in the K₃ system, given P1) → DI-bits processed at Vᵢ ∝ time at Vᵢ (CPP DI-bit rate) → mass contribution from Vᵢ ∝ DI-bits at Vᵢ (CPP mass as organisational energy). Each step follows from CPP axioms and P1 without independently assuming the Born rule.

The CPP account of the Born rule for probability detection (OP-QM-1) is separate from P2. P2 is a mass relation, not a measurement relation.

---

### B3. "If P3 depends on imported open-system formalism (Layer B), isn't the Koide derivation circular — you're assuming quantum mechanics to derive a quantum-mechanical result?"

No, and the Layer A/B/C decomposition makes clear why not. The result has three logically distinct components:

**Layer A (geometry):** The K₃ graph has eigenvalues {+2, −1, −1}. This is a mathematical fact about a triangle — no quantum mechanics is needed. The 2:1 degeneracy ratio is purely geometric.

**Layer B (thermal model):** The system thermalises to a Gibbs state at the Planck temperature. This uses standard open-system quantum mechanics (Caldeira–Leggett coupling, Gibbs equilibration). This is imported, not derived from CPP primitives.

**Layer C (algebra):** Given equal eigenstate occupation (from Layer B applied to Layer A), K = 2/3 follows by algebra.

The potential circularity objection would apply if Layer B were smuggling in the answer. But Layer B provides only the *weighting* (equal occupation per eigenstate in the high-T limit) — a generic result that applies to any three-level system at high temperature. The *content* — why K = 2/3 rather than any other value — comes entirely from Layer A (the 2:1 eigenvalue degeneracy of K₃). A different graph with different eigenvalue multiplicities would give a different K even with the same Layer B thermalisation model.

The honest summary: the derivation is conditional on Layer B. Deriving Layer B from CPP primitives (the programme's SS-4 target) would make it unconditional. But even conditionally, the result is nontrivial — it explains *why* K = 2/3 rather than any other value, given standard thermalisation.

---

## Category C: On the Proof Architecture

### C1. "The proof has four steps but the key step is Step 3 — ρ² = 2 from P3. The rest is algebra. Is the theorem really just P3?"

The theorem has three independent inputs (P1, P2, P3) and the algebra connecting them. Each input does different work:

P1 identifies the Hamiltonian as ℏω₀ × A_{K₃} — without P1, the K₃ spectrum has no physical connection to lepton masses. P2 connects wavefunction amplitude to mass — without P2, the eigenstates of Ĥ_ZBW have no mass interpretation. P3 fixes the occupation ratio — without P3, ρ could be anything.

Yes, Step 3 (ρ = √2 from P3) is the pivot of the proof — it is where the physical content enters the algebra. But P1 and P2 are necessary to make Step 3 physically meaningful. The theorem is the conjunction of all three, not just P3.

The correct characterisation: P3 is necessary but not sufficient. The full logical chain P1 ∧ P2 ∧ P3 → K = 2/3 requires all three.

---

### C2. "K = 2/3 from K_N gives K = (N+1)/(2N). For N=3 this is 2/3. But why does the lepton cage have N=3 vertices rather than some other number?"

The three-colour structure of the lepton cage (N=3) follows from a separate argument: quarks have three colour states (red, green, blue), and leptons couple to the same cage base through the neutral lepton-quark vertex coupling. The cage base is a triangle — the minimal symmetric graph that supports three-fold rotational symmetry — because there are three colour charges. The number 3 enters from the strong-sector colour structure (derived in SS-1) rather than from any assumption in SM-3. SM-3 takes N=3 as established by SS-1 and derives the Koide consequence.

The K_N formula shows that K = 2/3 is specific to exactly N=3 — other values of N give different Koide ratios. This is both a consistency check (CPP must have N=3, not N=4 or N=5, for K = 2/3 to hold) and a prediction (if there were a fourth colour, the lepton Koide ratio would be 5/8, not 2/3).

---

## Category D: On the Completeness of SM-3

### D1. "SM-3 proves K = 2/3 but cannot derive the individual lepton masses. Without the masses, what has been achieved?"

A constraint has been established. K = 2/3 is one equation constraining three masses. With three masses and one constraint, two degrees of freedom remain free — one for the overall mass scale (calibrated to the electron mass in SM-4) and one for the phase θ (open: OPEN-P-SM-7d). Establishing the constraint K = 2/3 from first principles means that when SM-4 calibrates A and when OPEN-P-SM-7d is eventually resolved (θ from the EW sector), the three individual masses will be fully determined with zero remaining free parameters.

The analogy: knowing that three numbers lie on a circle (K = 2/3 constraint) plus knowing the circle's radius (A calibrated in SM-4) plus knowing where one point is on the circle (θ from EW) fully determines all three. SM-3 proves the circle; SM-4 measures the radius; EW gives the angle. Each step is genuine progress.

---

*Document prepared by Thomas Lee Abshier ND and Claude Sonnet (Anthropic), 30 March 2026. Updated 16 April 2026 by Claude Opus (Anthropic) after ChatGPT referee review: B1 revised for Layer B status and robustness; B2 updated for Layer A label; B3 added for Layer B circularity question.*
