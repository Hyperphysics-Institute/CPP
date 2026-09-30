# CPP Theory Overview — Current State

**Location:** `/CPP/theory-overview.md`
**Purpose:** Snapshot of all CPP results, open problems, and next targets. Read at the start of each session.
**Last updated:** 29 September 2026 (Patch 4342: catalog refreshed (Capotauro v2.4, SS-8 v1.4). Patch 4341: m_Z/m_W row corrected (SF-2 arithmetic erratum). Patch 4340: catalog refreshed after the cosmology wording sweep. Patch 4339: gravity rows corrected — OPEN-GR-FE-1 was closed at 3267. Patch 4338: scorecard paragraph and σ row follow the tally audit. Patch 4337, Session 241 — **full refresh**: stage 1 at 4336 (header, headline basis, one-paragraph theory); stage 2 here (papers by series, quantitative results re-audited row by row, axioms, formulas, derivation chains with status, open problems keyed to `pre_deposit_roadmap.md`). Where this file conflicts with the live registries, the registries win.) Previous header: 17 May 2026 (Session 127
Patch 0422B), with a 6 June 2026 EU-1 note.

---

## Current state and headline basis (29 September 2026)

**Counts, from the live registries (authoritative there, not here):** 9 axioms (`axiom-registry.md`; AP-4 and AP-5 are
ratified clauses, count unchanged); 108 counted empirical correspondences (`predictions.md` Cumulative Swarm Tally, as
of 6 June 2026, 60 of them conditional; PRED-C-96's quoted n_s updated to 0.9654 one-sided at 3852); 82 theorems + 9
corollaries (`theorem-registry.md`); 123 papers in the deposit queue
(`osf_deposit_queue.md`, 6 never-deposit); **nothing is deposited yet** — deposits go to the CERN repository (Zenodo)
via Isak (CONV-012). What must be settled before the deposit is `pre_deposit_roadmap.md`.

**What each headline rests on** (derived / calibrated / conditional / conjecture / input). A result is stated here at
the strength its own paper or registry gives it:

| Headline | Basis | Where recorded |
|---|---|---|
| sin²θ_W = 3/(8φ), α_s = 5/(8φ), their sum 1/φ | derived at zero parameters (as claimed by SM-6/SM-7) | SM-6, SM-7 |
| Koide K = 2/3 | **conditional** on Layer B (OPEN-SS-16) | SM-3, `frontier_sectors/SS.md` |
| Charged-lepton masses (μ, τ) | **1 calibration** (m_e) + Koide phase; inherits Koide's Layer-B condition | SM-6 |
| Heavy-quark masses (RMS 2.1%) | **1 calibration** (m_e; SF-3 v1.0 demoted m_c to derived) | SM-8/9, SF-3 |
| W, Z, H absolute masses | **calibrated** dilution factors η_W, η_Z, η_H; the ratio m_Z/m_W = 1.141 is zero-parameter | SF-2 |
| Nuclear bindings (SS-5, SS-7, SS-8, SS-9) | **conditional** on hypothesis stacks (C1–C8, D1–D3) | SS papers, `predictions.md` |
| Neutrino sector | 8 parameters from **1 calibration** | SF-4 v3.4 |
| n_s ≈ 0.9654 | **framework-conditional**, leading-order (OPEN-EU-1) | EU-1, PRED-C-96 |
| g_A (nucleon axial coupling) | **not pinned**: with one quark mass, 1.242–1.282; the r_p "prediction" withdrawn (4284) | `series_standard_model/axiom_maturation/4284…` |
| α (fine-structure constant) | **calibrated relation**: α = PSR/(2L), one calibrated swing (CAL-ZBW1-SWING, 4326–4330); passes local position invariance, running has the right sign; running law needs a cloud model (4331) | `series_standard_model/axiom_maturation/4322–4331` |
| ħ | **identified, not derived** (c03); the Planck ZBW half-swing carries ħ/2 (founder, 4320/4325; c04 v2.3) | c03, c04, 4300 |
| Spin ħ/2 | **input** throughout; SPIN-1 and SPIN-2 **held from deposit** (4289) | TODO-4289-SPINREV |
| G and the Planck mass | GR-1/GR-1a's "fixed by the 600-cell lattice, no free parameters" is **an overstatement** (TODO-4300-HBARSWEEP); the general static field equation, a Birkhoff-type uniqueness and a conserved source current are **derived conditionally** (GR-1j V1.0; OPEN-GR-FE-1 CLOSED at 3267, founder-confirmed) on the PSR constitutive form at W2 strength, k a registered normalisation; the full nonlinear Einstein equations + Λ remain open (OPEN-SR-4) | `frontier_sectors/GR.md`, GR-1j |
| Exterior GR solutions (Schwarzschild, Kerr, Kerr–Newman) | reproduced as solutions; equations by correspondence only | GR series |
| Special-relativistic ε(v) = γ − 1 | **recorded satisfied at W2 strength** for closed self-bound patterns (founder, 2502); theorem-grade debts remain | `frontier_sectors/SR.md` |
| Electromagnetic constants μ₀, ε₀, c | **parameter-tuned** toy model (OPEN-FP-6-CONSTANTS) | SF-6 |
| Dark energy / Λ | **Λ-like, Λ from calibration**; no dynamical prediction (3430); TN-SR-1's 10⁻¹²² suppression is a **conjecture** | `frontier_sectors/DMDE.md`, TN-SR-1 |
| Dark matter | **conjecture** (CONJ-COSMO-1); the 11.26 GeV ring is 31 orders short on clumping amplitude and fails on shape (3884); DM-1/DM-3 never-deposit | `frontier_sectors/CONJ.md`, `research_frontier.md` |
| Chirality (weak-interaction handedness) | **primitive** (OPEN-SD-CHIR-PRIMITIVE), not derived | `frontier_sectors/SD.md` |

**Corrections to the 17 May overview (recorded when it was replaced, 4336–4337):** its "108 zero-parameter from 9 axioms
and 2 calibrations (m_e, m_c)" is replaced by the tally read at its own breakdown (below); m_c is no longer a calibration
(SF-3); SF-4's "v4.4" was pre-ship numbering (current v3.4); r_p, μ_p and the SS-5/SS-9 nuclear rows are held; α_s(m_H)
is calibrated in effect; SS-7 uses the measured B(⁴He); "67 theorems, 7.4 per axiom" is withdrawn; OSF is no longer the
deposit route. **Erratum on stage 1 (4336):** it said the tally itself states "2 calibrations"; it does not — the
"2 calibrations" wording was the May overview's.

---

## The Theory in One Paragraph

Conscious Point Physics models the physical world as Conscious Points on a lattice of Grid Points with the local
structure of the 600-cell polytope (120 vertices, 720 edges, 1200 faces, 600 cells, coordination 12), exchanging
DI-bits once per Absolute Moment under nine axioms. From that geometry it obtains, at zero adjustable parameters, the
weak mixing angle 3/(8φ) and a strong coupling 5/(8φ); with one calibration (the electron mass) it reproduces the charged-
lepton and heavy-quark masses to percent level and the neutrino sector; its nuclear-binding results hold conditionally on
stated structural hypotheses; it derives a general static gravitational field equation and reproduces the exterior solutions of general relativity,
conditional on a constitutive form graded at W2 strength (the full nonlinear Einstein equations remain open); its fine-structure constant, ħ, electromagnetic constants and cosmological constant enter as
calibrations or identifications, not derivations; and dark matter and the chirality of the weak interaction are,
respectively, a conjecture and a primitive. The table above says which is which.

### The 17 May 2026 paragraph (kept for the record; superseded by the paragraph above)

Conscious Point Physics derives the Standard Model from the 600-cell polytope (120 vertices, 720 edges, 1200 faces, 600 cells, coordination z=12). All gauge couplings are mode fractions of the lattice weighted by η = 1/φ. All fermion masses follow from the K₃ eigenvalue structure (bonding eigenvalue +2, antibonding −1) perturbed by isotropic gauge shifts, and from the zero-parameter cage mass formula M = m_e(z/φ)V^(7/3). The SS-5/SS-7/SS-8 nuclear cascade extends the K₃ mechanism across three structural scales — nucleon-nucleon (SS-5), alpha-alpha (SS-7), and interstitial-alpha (SS-8) — with the recurring binding quantum B_pair = M₀/φ = 2.342 MeV unrescaled at each scale (Pattern 6 scale recurrence). SS-9 v1.0 derives the simplicial-alpha-polytope connectivity (closing OPEN-SS-24 conditionally) via a bridge to Steinitz 1922 + Freudenthal-van der Waerden 1947. The SF-line flagship papers extend the framework across sectors: SF-4 v4.4 unifies the neutrino sector at first cross-sector closure with SM-5 op:nu_id (8 parameters from 1 calibration, normal hierarchy forced); SF-2 v1.0 unifies electroweak cage bosons (W±, W⁰, Z, H) via 4 cage-shape uniqueness theorems; Capotauro v1.0 closes OPEN-SM-4 sub-claim (c) via the Composite Capotauro Wigner-Eckart Theorem, predicting $\Delta p_{LR} = \chi/6 \approx 0.0394$ within 2% of leptogenesis; Capotauro v2.0 extends this to three-way substrate-level cross-sector unification $\|M^{K3}\| = \|M^W\| = \|M^{qDP}\| = \chi/6$; and Chirality Continuum v1.0 closes OPEN-FP-SF-2-CHIR at Layer 4 jointly with SM-2 v2.0+ chiral-polarity-bias via three theorems (THEO-CHIR-CONT-1+2+3) deriving Michel $\rho = 3/4$, 100% LH at massless helicity limit, and leptogenesis CP-asymmetry at zero parameters from the substrate handle $\chi/6$. The theory has 9 axioms (7 core + A8' + A11), 2 calibration constants (m_e, m_c), and 0 shape parameters. As of 20 May 2026 it predicts **108 zero-parameter empirical correspondences** (per `predictions.md` Cumulative Swarm Tally; chirality continuum elevates structural rigor of substrate-handle predictions to Layer 4 EFT operative-falsifier status without adding new swarm contributions per programme convention), of which 78+ are quantitative numerical with stated empirical residuals. **Theorem count advanced to 67** (47 → 62 → 67 over the last 2 months; +5 theorems from Capotauro v2.0 substrate-level cross-sector unification (THEO-SD-CHIR-1+2) + chirality continuum Layer 4 EFT closure (THEO-CHIR-CONT-1+2+3)); **Theorems:Axioms ratio = 67:9 ≈ 7.4 theorems per axiom**. **EU-1 (6 June 2026)** extends the framework to its first cosmology / early-universe result: the CMB scalar spectral index $n_s = 1 - 2/N_* \approx 0.9649$ (and running $\alpha_s \approx -0.0006$) derived from substrate inflation — the expansion boost tracking the logarithm of Grid-Point occupancy, $H_{\text{eff}} \propto \ln\bar n$, because the dispersal pressure of indistinguishable Conscious Points (axiom A1, Gibbs's $1/n!$) is the configurational chemical potential $\mu \propto \ln\bar n$ — zero-new-axiom, framework-conditional (PRED-C-96, the 108th swarm contribution and first SR/cosmology-sector entry; NO THEO; open residual OPEN-EU-1).

---

## Papers (29 September 2026)

**Per-paper detail lives in two generated files, not here:** `paper_catalog.md` (title, version, last touch; rebuilt by
`code/rebuild_paper_catalog.py`, 128 live papers) and `osf_deposit_queue.md` / `osf_deposit_manifest.json` (the 123
deposit candidates, waves, holds; rebuilt by `code/build_osf_queue.py`). The file names still say "osf"; the deposit
route is the CERN repository (Zenodo), done by Isak, who builds the PDFs (CONV-012). **No paper is approved for
deposit** (APPROVED column empty for all 123). An earlier OSF project registration exists (DOI 10.17605/OSF.IO/JXE8D).

| Series (folder) | Deposit candidates | Lead papers and current versions | Deposit status |
|---|---|---|---|
| Flagships (`flagship_papers/`) | 9 | SF-1 v1.3 (leptons), SF-2 v1.08 (electroweak; v1.09 owed), SF-3 v1.6 (quarks), SF-4 v3.4 (neutrinos — the "v4.4" of May was pre-ship numbering), SF-5 v1.04 (strong), SF-6 v1.6 (electromagnetism), SF-8 v0.5 (emergent Coulomb), SF-7 v0.11 | SF-7 **never deposit** (placeholder) |
| Strong (`series_strong/`) | 15 | SS-1 (+1a–1f), SS-3 v1.7, SS-4 v0.4, SS-5 v1.2, SS-7 v1.6, SS-8 v1.0, SS-9 v1.3 | **SS-2, SS-5, SS-6, SS-9 held pending critique** (the 1.07/0.62 fm frame superseded by founder rulings 4275/4276; TODO-4264-PASSTHROUGH) |
| Standard Model (`series_standard_model/`) | 14 | SM-1…SM-12, SM-TN-2 (SM-8 v4.1, SM-9 v2.4, SM-7 v2.5) | SM-3's all-tetrahedral-lepton premise vs founder 4212 open (TODO-4212-CAGETABLE) |
| Gravitation (`series_gravitation/`) | 12 | GR-1 v1.0.3, GR-1a v3.1, GR-1c v2.4, GR-1b, GR-1d–1j (GR-1j v1.0: the field equations), GR-2 v2.11 | the OPEN-ORG-023 gate's FE-1 condition is **discharged** (3267); **GR-1d V3 still predicts a 2.15 ms echo that AP-5 / GR-2 V2.11 withdrew** (TODO-4339-GR1DECHO); GR-1i reviewed, version bump owed |
| Relativity (`series_relativity/`) | 7 | SR-1 v1.2, SR-2 v1.5, companions c01–c05 (c03 v2.2, c04 v2.3) | publishable with theorem debts stated (roadmap item 6) |
| Quantum mechanics (`series_quantum_mechanics/`) | 9 | QM-1…QM-6 (v3.x), SPIN-1/2/3 | **SPIN-1, SPIN-2 never deposit until revised** (ħ/2 taken as input; TODO-4289-SPINREV) |
| Electroweak (`series_electroweak/`) | 5 | EW-1…EW-5 (v1.1) | — |
| Foundations (`series_foundations/`) | 8 | SD-1…SD-5, TN-SR-1, DP-sea, silly-putty note | SD-5 **never deposit** (unfinished); TN-SR-1 only as the labelled conjecture it is |
| Phenomena (`series_phenomena/`) | 5 | EU-1 v1.6, TP-1 v1.4, DM-1 v1.8, DM-2 v1.0, DM-3 v1.2 | **DM-1, DM-3 never deposit** (record, not release); DM-2 not approved |
| Umbrella / chirality arc (`series_umbrella/`) | 39 | Capotauro v2.3, Chirality Continuum v1.0, F.1 Dynamical Substrate Law v1.0, hardened theorems, THEO-CHIR-* notes | chirality is a **primitive** (roadmap item 8) |

---

## Quantitative Results — current status (audited 29 September 2026)

Rewritten from the 17 May table after a row-by-row audit against `predictions.md`, `todolist.md`, the sector files and
the papers. **Basis** says what each row rests on. "Zero-param" means no input beyond the axioms and the 600-cell;
"1 cal (m_e)" means the electron mass sets the scale. Where the registry and this table disagree, the registry wins and
this table is the thing to fix.

| Result | Value | Observed | Residual | Basis | Source |
|---|---|---|---|---|---|
| Weinberg angle 3/(8φ) | 0.23176 | 0.23122 (MS-bar) | +0.24% | zero-param, as claimed by SM-6 | SM-6, PRED-C-67 |
| Strong coupling 5/(8φ) | 0.386 | ~0.38 (no fixed scale) | ~1% | zero-param; scale of the comparison not fixed | SM-7 |
| α_s / sin²θ_W = F/E; sum | 5/3; 1/φ | — | exact | zero-param (topological) | SM-7 |
| Koide ratio K | 2/3 | 0.666661 | 11 ppm | **conditional on Layer B** (OPEN-SS-16) | SM-3 |
| Lepton Koide phase | 132.731° | 132.732° | 0.003% | zero-param given K = 2/3 | SM-6 |
| m_μ, m_τ | 105.47, 1774.1 MeV | 105.66, 1776.9 | 0.18%, 0.15% | 1 cal (m_e); inherits K's Layer-B condition | SM-6 |
| Quark Koide phase | 124.035° | 124.094° | 0.048% | SF-3 Prop. 5.1 (a proposition, not a theorem) | SM-7, SF-3 |
| m_s, m_c, m_b, m_t | 96.3, 1249, 4115, 169 571 MeV | 93.4, 1270, 4180, 172 760 | RMS 2.1% | 1 cal (m_e) + A8′; m_t carries z·C_F = 16 | SM-8/9, SF-3 |
| m_b, m_t by Koide + m_c | 4.24, 169.8 GeV | — | 1.4%, 1.7% | **demoted**: non-canonical two-calibration route (SF-3) | SM-7 |
| m_Z/m_W | 1.1409 | 1.1344 | 0.57% | zero-param ratio; the tree relation is exact on-shell, so the ~0.6% gap is of radiative-correction size (SF-2 v1.08.1; the earlier 1.1405/0.54% used the observed angle in place of 3/(8φ)) | SF-2 |
| m_W, m_Z, m_H | observed values | — | — | **calibrated** (η_W, η_Z, η_H) | SF-2 |
| Neutrinos: m₂, m₃, Σm_ν, σ_ν | 8.81, 55.1, 64.9 meV; 1.62e-11 | 8.66, 50.9, ≤72 meV; 1.59e-11 | 1.7%, 8.3%, in bound, 2.0% | 1 cal (m_e); conditional theorem level | SF-4 v3.4 |
| PMNS sin²θ₁₂, sin²θ₂₃ | 1/3, 1/2 | 0.307, 0.572 | 8%, 13% | zero-param TBM zeroth order | SM-5, SF-4 |
| Dirac neutrinos, no 0νββ | — | untested | — | forward prediction PRED-O-42 | 4219 |
| Chirality matrix element | χ/6 = 0.0393 | ~0.04 (leptogenesis-inferred) | ~1.6% | magnitude only, on FI-C-1…10; the hand is a **primitive** | Capotauro |
| String tension σ | 926.5 MeV/fm | ~910 | +1.8% | **conditional** on CONJ-SS-5 (SS-4's z² replacement, not derived); the registries' old citation of CONJ-SS-2-1 corrected at 4338 | SS-4, PRED-C-31 |
| r_p | 0.883 fm | 0.841 | +5.0% | **held**: SS-2 frame superseded; with one quark mass no frame reaches r_p | SS-2, TODO-4284-RPFLOOR |
| μ_p | 2.789 μ_N | 2.793 | −0.1% | **held**: rests on m_q = m_p/3, assigned not derived | SS-2 |
| g_A | 1.242–1.282 | 1.2754 | brackets it | **not pinned** (4284); zero-param exchange-off value 1.312 | EW lane 4234–4284 |
| α_s(m_H) | 0.1132 | 0.1130 | +0.2% | **calibrated in effect**: SS-2 runs from a matched α_s(m_Z) (A11) | SS-2 |
| B_d, B(³H), B(³He), B(⁴He) | 2.342, 8.474, 7.642, 27.90 MeV | 2.225, 8.482, 7.718, 28.30 | +5.3 … −1.4% | **conditional** (C-stack); SS-5 **held** | SS-5 |
| ⁵He, ⁵Li, ⁸Be, ²He, 2n unbound | unbound | unbound | qualitative | conditional; SS-5 held | SS-5 |
| Alpha-chain, 12 nuclei ¹²C→⁵⁶Ni | RMS 0.80% | AME 2020 | — | **conditional** on C1–C4, and **uses the measured B(⁴He)** as input (the paper says so; the LO-CPP variant uses 27.904) | SS-7 |
| Interstitial-n Δ₁ (²⁶Mg, ⁴²Ca) | 9.37, 11.24 MeV | 9.39, 11.36 | −0.2%, −1.0% | conditional on C1–C4 + D1–D3 | SS-8 |
| ⁸⁴Mo, ⁸⁸Ru, ⁹²Pd | 698.92, 729.56, 760.20 MeV | 699.27, 730.10, 761.15 | 0.05–0.13% | **calibrated** (B_slip from ⁵⁶Ni, measured B_α); SS-9 **held** | SS-9 |
| n_s | 0.9654 | 0.9649 ± 0.0042 | 0.12σ | framework-conditional, leading order (OPEN-EU-1) | EU-1, PRED-C-96 |
| Classical tests of gravity | GR values (43″/cy, 1.75″, …) | GR values | — | W2-conditional (reviewed 5–0, CONV-029) | GR-1i v0.1 |
| Coulomb's law from the lattice | ±0.4% pointwise at R = 4 | Ewald | — | cellular-automaton measurement; scalar sector only, no coupling constant predicted | SF-8 v0.5 |
| α | 1/137.036 | — | — | **calibrated relation** α = PSR/(2L), L ≈ 68.5 PSR (CAL-ZBW1-SWING); passes local position invariance; running has the right sign, law owed | 4322–4331 |

**Scorecard.** `predictions.md` headlines **"108 zero-parameter empirical correspondences from a 9-axiom stack"** (tally as of 6 June). Read at its own breakdown: 23 unconditional quantitative, **60 conditional** quantitative, the rest structural or qualitative; the mass rows use the m_e calibration and the SS-9 rows a calibrated B_slip, so "zero-parameter" does not hold for every entry. Since 4338 the tally carries an audit-status block and per-row tags: 20 counted rows rest on held papers (SS-2, SS-5, SS-9), two SS-2 rows are calibrated in effect, and the 12 SS-7 rows use the measured B(⁴He). **Theorems:** 82 theorems + 9 corollaries (+7 propositions, 1 lemma) in `theorem-registry.md` (summary as of Patch 2407); many are conditional, and a theorem count is not a measure of evidence. The May "67 : 9 ≈ 7.4" ratio is withdrawn.

---

## The Axiom Set (as registered, `axiom-registry.md`)

| ID | Name | Statement (short) |
|----|------|--------------------|
| A1′ | CP existence (three types) | Grid Points (fixed lattice sites that compute and broadcast), DI-bits, and charged Conscious Points |
| A2 | 600-cell topology | the 600-cell (V=120, E=720, F=1200, z=12); the cage need not be exactly regular — the deficit is strain (founder, 4061) |
| A3′ | Completed Broadcast (LSP′) | each GP broadcasts its Lattice State Packet to its PSR shell at c every Absolute Moment; AP-4 (fixed-N emission) and AP-5 (saturation protocol) are ratified clauses |
| A4 | Nexus | a global consistency constraint at each Absolute Moment |
| A5 | Propagation efficiency | η = l_edge/R_circ = 1/φ |
| A6′ | Walk-Dimension Gauge Principle | walk dimensionality sets the gauge structure; z = 12 post-gap multiplier |
| A10 | Colour attraction | colour self-energy is negative |
| A8′ | Cage-Volume Scaling | M ∝ m_e(z/φ)V^(7/3) |
| A11 | Lattice-Scale Grounding | l_unit = ħc/Λ_QCD = 0.589 fm, matched to α_s(m_Z) running |

**Calibrations and identifications beside the axioms:** m_e (scale); η_W, η_Z, η_H (boson masses); CAL-ZBW1-SWING (α);
Λ (dark energy); ħ identified (c03); spin ħ/2 input. **Pending registration:** the founder's 4288 ruling that a CP has no
mass of its own, only DP-arc inertia (TODO-4316-CPMASSAXIOM). **Potential reductions:** A5 → A2, A10 → A2 + A6′.

---

## Key Formulas (reference card)

```
sin²θ_W = η × Tr(A²)/N = (1/φ)(1440/3840) = 3/(8φ) ≈ 0.23176
α_s     = η × [Tr(A³)/3]/N = (1/φ)(2400/3840) = 5/(8φ) ≈ 0.3863
α_s/sin²θ_W = F/E = 1200/720 = 5/3 ;   sin²θ_W + α_s = 1/φ ≈ 0.618

ε_lepton = +2sin²θ_W/(z+1) = +3/(52φ) ;   ε_quark = (2sin²θ_W − 12α_s)/(z+1) = −27/(52φ)
cos θ_lepton = −(2/3)(1 + 3/(104φ)) → 132.731° ;   cos θ_quark = −(2/3)(1 − 27/(104φ)) → 124.035°
K = λ₊/(λ₊ + |λ₋|) = 2/3   [K₃ eigenvalues +2, −1, −1; conditional on Layer B]
N = Tr(A²) + Tr(A³)/3 = 3840 ;  φ = (1+√5)/2 ;  z = 12

Quark masses (SM-8 v4.1 / SM-9; single m_e calibration per SF-3):
  M_q = m_e (z/φ) V^(7/3), q = s, c, b ;  M_t = m_e (z/φ) V_t^(7/3) × z·C_F (= 16) ;  M₀ = m_e z/φ = 3.790 MeV

Nuclear (conditional):  B_pair = M₀/φ = 2.342 MeV ;  alpha-chain E = 3N_α − 6 ;  2E/V = 6 − 12/V
String tension (SS-4, conditional): σ = M₀z²/(φ l_edge) = 926.5 MeV/fm
  [CONJ-SS-5; it supersedes SS-2's CONJ-SS-2-1, σ = M₀zπ/(φ l_edge) = 243 MeV/fm]

Fine-structure constant (calibrated relation, 4330):  α = PSR/(2L),  L ≈ 68.5 PSR (the Planck ZBW swing)
  running requirement (4331): dL/d ln r = (PSR/3π) Σ_f N_c Q_f²  inside each species' reduced Compton length
Unit of action (founder 4320/4325; c04 v2.3): the Planck ZBW half-swing carries ħ/2 over many Moments;
  one Compton radian = m_P/m Absolute Moments
Spectral index (EU-1): n_s = 1 − 2/N_* ≈ 0.9654 (one-sided)
```

---

## Derivation Chains (with their present status)

- **SM-6 (leptons):** 600-cell → K₃ → K = 2/3 [Layer B] → traces → 3/8 → η = 1/φ → sin²θ_W = 3/(8φ) → ε = 3/(52φ) → θ = 132.73° → masses [1 cal].
- **SM-7 / SF-3 (quarks):** the same chain + α_s = 5/(8φ) from face modes → ε = −27/(52φ) → θ = 124.04°; masses from A8′ on m_e.
- **SS-1/SS-3 (strong):** K₃ face permutations → 8 generators → SU(3), unique among 3-vertex algebras (THEO-SS-10) → β₀ = 7.
- **SS-5 → SS-9 (nuclei):** open-vertex cascade → alpha-polytope 3N−6 → 2E/V → Steinitz/FvdW bridge (THEO-SS-16); every step conditional on its hypothesis stack; SS-5 and SS-9 held.
- **SF-4 (neutrinos):** SM-5 K₃ eigenmodes → cage-shell taxonomy (V = 4, 12, 30) → m ∝ V² → σ_ν = z⁻¹⁰ (Picture A) → cross-sector closure with SM-5 (THEO-SF-4-5).
- **SF-2 (electroweak):** first/second distance shells → W bracelet, Z icosahedron, H dodecahedron, mass gap → m_Z/m_W at zero parameters; absolute masses calibrated.
- **Capotauro / chirality:** K₃ doublet → |M| = χ/6 (THEO-CAP-1); the magnitude is derived on FI-C-1…10, the hand is a primitive; the EM-handedness leg of the three-way unification was found spurious (4069/4070).
- **QM-1 → QM-6:** DI-bit hopping → Schrödinger → Born rule [OPEN-QM-1] → Bell 2√2 → Lindblad → QFT; spin ħ/2 is input (OPEN-QM-3); the sector awaits OPEN-QM-1-REGROUND.
- **SR / GR:** SSV compression → Lorentz factor (ε(v) = γ − 1 satisfied at W2, 2502) → SSV shell broadcast → Newtonian gravity → Schwarzschild, Kerr, Kerr–Newman *solutions* → the general static field equation, Birkhoff-type uniqueness and a conserved census current (GR-1j, OPEN-GR-FE-1 closed at 3267), all conditional on the PSR form at W2; radiative sector via SR-2/A3′ (λ = 16πG/c⁴); full nonlinear EFE + Λ open (OPEN-SR-4).
- **α (4301 → 4331):** DI-bit count rule → α = c/2 → α = c·PSR/(2L) → α = PSR/(2L) with one calibrated swing; local position invariance passes via family exclusion (R-DIBIT-FAMILY-EXCLUSION) and saturation.
- **EU-1 (cosmology):** diluting saturated lattice → A1 indistinguishability gives μ ∝ ln n̄ → ZBW bath reaches a constant-rate ZRP → H_eff ∝ N_rem → δN → n_s = 1 − 2/N_* (framework-conditional).

---

## Physical Mechanisms (from founders_vision.md)

### Electric interaction (edge modes)
Push-pull, attract/repel, linear, reversible. Single qDP bond with one degree of freedom. Composition commutes. U(1).

### Colour interaction (face-bond circulation)
Displacement pulses circulate on closed triangular K₃ loops. 8 standing-wave patterns = 8 Gell-Mann generators. Non-commutative because each pulse changes the vertex SSV_abs. Energy trapped in loop = confinement. SU(3).

### Isotropic shift mechanism
Uniform perturbation ε·I₃ on K₃ preserves C₃ symmetry (eigenvectors unchanged) but shifts the eigenvalue RATIO because {+2,−1,−1} is asymmetric. This changes the Koide phase without breaking the triangle symmetry.

### Walk-Dimension Gauge Principle
1D edge walks commute (Abelian). 2D face loops don't commute in a Lorentzian lattice (non-Abelian). Walk dimensionality determines gauge group.

### Zitterbewegung as a pass-through swing (founder rulings 4264/4265, 4320–4327)
The ZBW is a conservative pass-through oscillation, not stop-and-reverse. At the Planck level the swing's CPs move at
their own V_i each Moment (never at c); a half-swing carries ħ/2 and spans many Moments; DP-arcs move by SSV_net with
their scale set by SSV_abs; each DI-bit steps only to a Grid Point holding no other DI-bit of its own family, which sets
the 2–10% shell width.

---

## Open Problems — pre-deposit priority (from `pre_deposit_roadmap.md`)

| # | Problem | IDs | Status (29 Sep) |
|---|---|---|---|
| 0 | Honest labelling and this scorecard | TODO-4335-OVERVIEW | overview refreshed (4336–4337); tally audited and σ citation fixed (4338); the corpus-wide wording sweep remains |
| 1 | Gravity: records into line (the FE-1 gate was discharged at 3267) | TODO-4339-GR1DECHO, TODO-4300-HBARSWEEP, TODO-4339-GR1IV1, OPEN-ORG-023 | GR-1/1a/1c wording done 4339; GR-1d echo, GR-1i bump, test-run set remain |
| 2 | Lattice-to-SI scale; the PSR floor | OPEN-SD-lattice-scale | open; black-hole PSR vs l_P/2 now a factor 4.1 (4322), not re-adjudicated |
| 3 | Spin and the unit of action | OPEN-QM-3, TODO-4289-SPINREV/SPINSWEEP | ħ/2 has a carrier (half-swing) but its size is calibrated; SPIN-1/2 held |
| 4 | Layer B and the QM foundation | OPEN-SS-16, OPEN-QM-1-REGROUND, OPEN-QM-1 | open; conditions Koide and much of the strong sector |
| 5 | Electromagnetic constants and α | OPEN-FP-6-CONSTANTS, CAL-ZBW1-SWING | α a calibrated relation with two tests; the running law needs a DP-arc cloud model |
| 6 | SR residual theorem debt | OPEN-SR-10 (i), SF-6 debt (b) | not verdict-bearing; SR-1 publishable with debts stated |
| 7 | Cosmology scope (DM, DE, Λ) | CONJ-COSMO-1, OPEN-SR-5, OPEN-EU-1 | not prerequisites if deposited papers do not claim them; wording sweep owed |
| 8 | Chirality | OPEN-SD-CHIR-PRIMITIVE | primitive; publishable as a stated axiom |

**Sector problems still open from the May list** (detail in `frontier_sectors/`): OPEN-P-SM-cage-1 (the 7/3 exponent;
SM-10 FEM), light-quark masses, OPEN-SS-5 (σ from the mode spectrum), OPEN-SS-19 (cascade factor), OPEN-SS-25…37 (the
SS-8/SS-9 hypothesis closures), OPEN-FP-SF-2-* (six), OPEN-FP-3-CKM, OPEN-FP-5-GLUEBALL, g_A's residual and the m_q
tension (TODO-4234-DELTA), OPEN-EU-1, OPEN-TP-1. Retired or closed since: OPEN-SS-22 (retired), OPEN-SS-24 (conditional,
SS-9), OPEN-SM-4 (c) (magnitude only), OPEN-FP-SF-4-1/-2.

---

## Pending Tasks

The task queue is `todolist.md`; the deposit order is `pre_deposit_roadmap.md` and `osf_deposit_queue.md`. The May
list of "Register X on OSF" items is withdrawn (OSF is no longer used; deposits go to Zenodo via Isak).

---

*Refresh this document when a scorecard registry changes (predictions.md, theorem-registry.md, axiom-registry.md,
paper_catalog.md); `code/overview_staleness_gate.py` enforces it. It is the AI's primary orientation document for new
sessions.*
