# CONV-015 DISPATCH — R-4 + OPEN-QMRG-B1 CANDIDATE PACKAGES (PATCHES 3001/3002): SECOND ROUND, EXECUTION CREDIT LIVE

**Patch 3003 (4 Aug 2026).** Second review round of the QM
re-grounding arc, adjudicating the two CONV-014 blocking items now at
candidate status. Question set and decision tree frozen before any
return. Five seats: GPT, Grok, Gemini, Copilot, DeepSeek.
**Copilot condition:** FRESH conversation (standing). **Ledger
disclosed:** Copilot carries one CONV-014 event
(claimed-checks-contradicted-at-HEAD; adjudication §4); DeepSeek ×4
prior fabrications (its CONV-014 honest-no-fetch declaration is on
the credit side); GPT ×1; Gemini self-mislabel ×3. Judge on merits;
tally-from-verbatim-only at adjudication.

## §0 — EXECUTION RULES (first round in this arc with scripts)

Two committed, deterministic verify scripts (seeded RNGs; runtimes
< 2 min each on CPU):

- `series_quantum_mechanics/code/3001_r4_5design_check.py` (seed 31001)
- `series_quantum_mechanics/code/3002_b1_energy_balance_check.py` (seed 31002)

**Withheld keys (per the KEY-E/KEY-F precedent; values computed
nowhere, stored nowhere — the worker has not evaluated them):**

- **KEY-G** = the log-log INTERCEPT of the SCALING-B icosahedron fit
  in the 3001 script (the script prints only the slope; the intercept
  is an unprinted internal of the same `np.polyfit` call).
- **KEY-H** = the log-log INTERCEPT of the check-(a) cycle-distributed
  fit in the 3002 script (same construction).

**Status ladder:** SCRIPT-EXECUTED = full stdout of both scripts PLUS
both keys (to 3 significant figures), obtained by actually running
the committed code. REASONED-VERIFIED = named derivation steps
independently checked against the repo (state which). ACCEPTED =
neither. A claimed execution without both keys and stdout is
self-indicting.

## §1 — What is under review

- **The R-4 package (Patch 3001):**
  `sketches/3001_r4_plane_stability_lemma.md`. Claims: L-1 EXACT
  plane closure for the shipped component-diagonal transport (a
  scalar stencil cannot mix components); L-2 for general single-edge
  kernels T(v)=αI+βvvᵀ, the lattice-anisotropic out-of-plane channel
  is (kΔs)⁴-suppressed because the icosahedral neighbor shell is a
  spherical 5-design (measured slope 4.00; octahedron 3-design
  control 2.00; bound ≈3×10⁻⁹⁰/refresh); L-3 the isotropic (ks)²
  direction-coupled channel is the longitudinal/spin sector, not
  leakage (O-R4-1 Hopf observation registered, UNCONSUMED); L-4
  universality via E=ħν_C (ω ≥ mc²/ℏ > 0 on the support).
- **The B1 package (Patch 3002):**
  `sketches/3002_b1_amplitude_count_derivation.md`. Claims: the
  quadratic-vs-linear fork is DECIDED by ratified AP-2's
  intensity-like clause; elastic energy balance (SF-6 stiffness +
  A3′ turnover + ħω per messenger) yields |SSV_net,⊥|² ∝ Nħ/(μω) —
  the bridge with its constant; the canonical 1/(2ω) normalization is
  RECOVERED as output (circularity cut at its first link; the
  mutual-support prohibition dischargeable); verified with the fork
  as discriminator (1.01 vs 1.99) + ω-scan (−0.97) + statistical
  robustness (1.00).
- Context: CONV-014 adjudication (`conv014_adjudication.md`), the
  PARTIAL bar scope E-1, QM-1 at v2.3.

## §2 — Disclosed weak points (attack first)

- **W-1 (the scoping move in L-1).** L-1 proves exactness for the
  transport class THE SHIPPED MODEL uses. Is that an answer to D-4 —
  which can be read as a question about the MICROSCOPIC substrate
  transport — or a dodge that relocates the question?
- **W-2 (kernel class).** The L-2 bound covers single-edge kernels
  built from the edge direction alone. Multi-edge-correlated
  transport is outside scope by the package's own admission.
- **W-3 (O-R4-1 seduction risk).** The Hopf/spin observation is
  registered as unconsumed. Attack whether anything in L-3's
  "channel B1 is spin, not leakage" identification implicitly LEANS
  on it — if the spin identification fails, does a genuine unbounded
  leakage channel reopen?
- **W-4 (toy status of the B1 verify).** One elastic element; Poisson
  kicks; linear damping standing in for the per-Moment turnover; the
  O(1) turnover factor uncomputed. Does the toy's success carry
  evidential weight for the lattice, or only illustrate the algebra?
- **W-5 (AP-2 deciding a dynamical fork).** The linear-vs-quadratic
  question is dynamical; the package settles it by citing a ratified
  ONTOLOGY clause. Legitimate registry consistency (the substrate
  must realize its ratified ontology) — or a category error that
  launders an open dynamical question through a definitional ruling?
- **W-6 (velocity risk).** Both packages were produced, verified, and
  self-graded by the same worker within one day of the adjudication
  they answer. Scrutinize for adjudication-shaped reasoning: do the
  packages prove what CONV-014 asked, or what was easiest to prove
  near it?

## §3 — THE QUESTIONS (frozen; named verdicts)

**Q1 — The R-4 package.** Does it close R-4 at the claimed derivation
grade? W-1/W-2/W-3 in scope; check the 5-design mathematics if you
can. Verdicts: **CLOSES-R4 / CLOSES-WITH-RESIDUE (name the residue
and whether it blocks) / FAILS (name the broken step)**.

**Q2 — The B1 package.** Does it derive B-QMRG-1 at the claimed
grade? W-4/W-5 in scope; check the energy-balance algebra and the
normalization claim. Verdicts: **DERIVES-B1 / DERIVES-WITH-RESIDUE
(name it, blocking or not) / FAILS**.

**Q3 — The mutual-support prohibition (CONV-014 E-3 rider).** With an
independent derivation on the table, is the QM-1↔QM-5 prohibition
DISCHARGEABLE? Verdicts: **DISCHARGE / RETAIN (state what more is
needed)**.

**Q4 — OPEN-QMRG-UNIQ scoping.** The uniqueness/exclusion obligation
(alternative compactifications) is open and untouched by 3001/3002.
Is it BLOCKING for full lift, or a registered non-blocking research
item (FI-QMRG-1 being an input, not a uniqueness theorem)? Verdicts:
**BLOCKING / NON-BLOCKING (register and proceed) / NON-BLOCKING-WITH-
CRITERION (state the criterion under which it would become blocking)**.

**Q5 — THE BAR RULING, round two.** Given Q1/Q2: (a) should the
E-1 PARTIAL scope move? Verdicts: **FULL-LIFT / WIDEN-PARTIAL (state
exactly what becomes admissible) / HOLD-CURRENT-SCOPE**. (b) Should
the QM sector's CONDITIONAL status resolve? Verdicts:
**RESOLVE-AT-STATED-GRADES / RETAIN-CONDITIONAL (state the trigger)**.

**Decision tree (frozen outcome-blind):** FULL-LIFT requires [Q1
majority CLOSES or CLOSES-WITH-nonblocking-RESIDUE] AND [Q2 majority
DERIVES or DERIVES-WITH-nonblocking-RESIDUE] AND [Q4 majority
NON-BLOCKING (either form)] AND [Q5(a) majority FULL-LIFT]. Failing
FULL-LIFT, the scope WIDENS to the conservative intersection of the
widening returns if [Q1 and Q2 majorities are non-FAILS]; any
sustained FAILS returns that item to derivation with the objection as
charter and freezes the scope. Sector conditionality resolves ONLY on
FULL-LIFT with no sustained FAILS; otherwise RETAIN with the
majority-stated trigger. Mutual-support prohibition discharges on Q3
majority DISCHARGE regardless of the bar outcome (it is a
citation-hygiene rule, not a bar clause). Ledger moves only through
the adjudication patch, tally-from-verbatim-only.

## §4 — Repository pointers

Blob: https://github.com/Hyperphysics-Institute/CPP/blob/main/ · Raw: https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/

- `series_quantum_mechanics/sketches/3001_r4_plane_stability_lemma.md`
- `series_quantum_mechanics/code/3001_r4_5design_check.py`
- `series_quantum_mechanics/sketches/3002_b1_amplitude_count_derivation.md`
- `series_quantum_mechanics/code/3002_b1_energy_balance_check.py`
- `series_quantum_mechanics/conv014_adjudication.md` (the governing round)
- `series_quantum_mechanics/papers/QM-1_schrodinger_emergence.tex` (v2.3)
- `series_quantum_mechanics/sketches/2996_reground_phase_variable_sketch.md` (FI-QMRG-1)

## §5 — Return format

Per question: named verdict + argument; cite lines when attacking.
Declare your execution status per §0 (SCRIPT-EXECUTED requires both
keys + both stdouts; REASONED-VERIFIED names the steps checked;
ACCEPTED is honorable and must be declared). Do not summarize the
packages back; attack them — W-6 in particular invites you to treat
the packages' speed as a reason for suspicion, not deference.
