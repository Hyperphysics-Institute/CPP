# SM-7 v2 — Hostile Review Prompt for Claude Sonnet 4.0

Copy and paste into a fresh Claude conversation:

---

Please act as a skeptical referee reviewing the following paper for a major physics journal. Be adversarial — assume the authors are overclaiming until proved otherwise.

**PAPER:** SM-7 v2 — "The Heavy Quark Mass Spectrum and Strong Coupling from 600-Cell Lattice Geometry"

**AUTHORS:** Abshier, Claude Opus, Copilot, Grok

**CONTEXT:** SM-6 (previous paper) derived sin²θ_W = 3/(8φ) as the edge-mode fraction of the 600-cell lattice and the charged lepton mass spectrum. SM-7 extends this to the strong sector.

**CORE CLAIMS:**

1. The strong coupling α_s = 5/(8φ) ≈ 0.386 is the face-mode fraction of the 600-cell lattice. The derivation parallels sin²θ_W exactly: both are η × (mode count) / (total capacity), where η = 1/φ. The identification of face modes with SU(3) colour rests on a prior result (SS-1) that proves cage-face permutations generate the Gell-Mann matrices exactly.

2. The coupling ratio α_s/sin²θ_W = F/E = 1200/720 = 5/3 is a topological invariant.

3. The mode complementarity sum rule sin²θ_W + α_s = 1/φ. The paper explicitly states this is mode partition (edge + face = total), not GUT-scale unification. The specific value 1/φ is set by the 600-cell metric.

4. For the quark Koide phase, colour coupling acts on all z = 12 bonds while EW acts on only 2 internal K₃ bonds. This asymmetry is derived from a projector lemma:
   - Assumption A1 (Edge Locality): edge modes are internal-bond-local when projected onto the K₃ cage.
   - Assumption A2 (Face Saturation): face-circulation modes saturate all incident bonds in the closed neighbourhood.
   The lemma proves: EW self-energy has support on 2 bonds; strong self-energy has support on all z bonds.

5. ε_quark = (2sin²θ_W - 12α_s)/(z+1) = -27/(52φ), giving cos θ_quark = -(2/3)(1 - 27/(104φ)), θ = 124.035° (PDG: 124.094°, 0.048%).

6. Predicted: m_b = 4.24 GeV (PDG: 4.18, 1.4%), m_t = 169.8 GeV (PDG: 172.7, 1.7%). Calibrated to m_c.

7. Mutual reinforcement: α_s extracted from quark masses = 0.383, from lattice = 0.386, agreement 0.7%.

**YOUR TASK:** Identify every weakness, hidden assumption, circular argument, and overclaim. Specifically address:

a) Is α_s = 5/(8φ) the QCD strong coupling constant, or merely a mode-counting ratio that happens to be close to α_s(m_c)? What is the theoretical justification for equating a face-mode fraction with the SU(3) gauge coupling? The paper claims this rests on SS-1 — but SS-1 proves SU(3) algebra from face permutations, not that the mode fraction equals the coupling constant.

b) The projector lemma (A1 + A2) is presented as deriving the 2 vs 12 bond asymmetry. But A1 and A2 are themselves assumptions, not proved from the lattice axioms. Has the paper merely pushed the assumption one level deeper? Under what conditions could A1 or A2 fail?

c) The mode complementarity sum rule — the paper calls this "not GUT-scale unification" and acknowledges it's a partition identity. Good. But then what IS the physical content? Is sin²θ_W + α_s = 1/φ a prediction, or is it true by definition once you define both couplings as fractions of the same total?

d) The PDG quark masses are MS-bar running masses. The Koide ratio K = 0.669 (not exactly 2/3) and the phase θ = 124.09° both depend on which scheme is used. With pole masses, K = 0.649 and θ = 122.83°. Has the scheme been chosen to maximise agreement? What is the CPP prediction for WHICH scheme should give K = 2/3?

e) α_s(M_Z) = 0.118. The paper predicts 0.386 and claims this is the "bare cage-scale" value matching α_s(m_c). But α_s runs logarithmically from 0.38 at 1 GeV to 0.12 at 91 GeV. Does CPP predict this running? If not, is 0.386 a prediction (testable at what scale?) or an excuse for being off by 3× at M_Z?

f) The 1.7% error on the top quark mass is 10× worse than the lepton sector. The top quark is the only fermion heavier than the EW scale (m_t > m_W, m_Z, m_H). Does the formula break down for particles above the EW scale? Is 1.7% "agreement" or the beginning of failure?

g) The combined SM-6 + SM-7 claims 9 derived quantities from 2 calibration constants. What is the combined probability that all 9 are coincidental? Is this as compelling as the lepton sector alone (where the probabilities were < 10⁻⁸)?

h) The paper cites SS-1 for the face → SU(3) identification. But SS-1 derives the Lie algebra generators from face permutations — it does not derive the coupling strength. The step from "faces generate SU(3)" to "the face mode fraction IS α_s" is a separate claim. Is this justified?

Provide a verdict: Accept / Major Revision / Minor Revision / Reject, with specific conditions for acceptance.
