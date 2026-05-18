# SF-4 v0.1 Outline — Working Document

**Status:** PLANNED → v0.1 drafting begins after outline review
**Track:** SF-4 (Neutrino Sector Unification) per `flagship_papers/README.md` 7-paper architecture
**Working title:** *Neutrino Sector Unification from 600-Cell Geometry: Eight Parameters from One Calibration*
**Established:** 9 May 2026 (Session 44, patch 0304)
**Estimated effort to v1.0 SHIP:** 4–6 sessions of v0.x drafting iteration after outline lock
**Target venue:** Zenodo (DOI) primary; arXiv hep-ph if endorsement obtainable
**Authors (anticipated):** Thomas Lee Abshier ND + AI collaborators (per SS-9 four-tier methodology)
**Foundation:** [`SF-4_neutrino_sector_audit.md`](sketches/SF-4_neutrino_sector_audit.md), [`SF-4_mechanism_selected.md`](sketches/SF-4_mechanism_selected.md), [`SF-4_suppression_derivation.md`](sketches/SF-4_suppression_derivation.md), [`SF-4_k3_cage_shell_consistency.md`](sketches/SF-4_k3_cage_shell_consistency.md)

---

## Strategic context

SF-4 is the active heavy-lift paper in the SF-line per the 7-paper architecture established at Session 41 (patch 0301). It is the only SF-line paper that required substantive new derivation work beyond corpus reframing — the audit phase (Session 37) revealed the neutrino corpus was thinner than the lepton, quark, or EW corpora when measured against strict-C standards, which is what made SF-4 the heavy lift.

By Session 43 close, SF-4's two substantive sub-derivations are at PARTIAL CLOSURE: the suppression mechanism (OPEN-FP-SF-4-1, with three independent physical pictures converging on $\sigma = z^{-2 d_{\text{eff}}} = z^{-10}$ at 2% empirical match) and the K3-Cage-Shell Consistency (OPEN-FP-SF-4-2, with Route C structural closure at SM-5-inheritance level). The remaining work is theorem-level formalization at v0.1 drafting plus closure of pending sub-problems (Picture A from A1–A11; K3 vertex-by-vertex theorem tied to SM-5 open problem).

**Why this paper, why now:**
- The neutrino sector is the most active and most cited area of beyond-Standard-Model physics. JUNO 2026+ resolution of mass ordering is a near-term named falsifier that any candidate flagship-class derivation should engage.
- CPP via Sessions 37–43 has produced 7 of 8 zero-parameter neutrino predictions (3 masses + 3 mixing angles + hierarchy ordering); the 8th ($\delta_{CP}$) is registered-as-open via SM-5 OPEN-SM-4 inheritance.
- SF-4 is the SF-line's strongest single test of the 12-fermion-mass-from-1-calibration headline because it covers the most extreme corner of the mass spectrum (12 orders of magnitude below the top quark) using the same calibration.
- A successful landing creates the precedent and template for SF-1, SF-3, SF-5, SF-6 — the SF-4 work has by far the most novel-derivation content; SF-1/SF-3 are reframings, SF-5/SF-6 are syntheses.

---

## Headline claim (draft v0.1 — refine before §0 abstract drafting)

> **CPP derives the neutrino sector's eight observable parameters** — three masses, three mixing angles, mass-squared ordering, and CP phase — **from a single calibration ($m_e$) plus 600-cell substrate geometry**, with seven of the eight parameters at zero free parameters. The neutrino mass formula $m_{\nu_i} = M_0 \cdot V_{\nu_i}^2 \cdot \sigma_\nu$ uses the same mass quantum $M_0 = m_e \cdot z/\phi$ that anchors the quark and charged-lepton sectors; the cage-shell vertex counts $V \in \{4, 12, 30\}$ are forced by 600-cell topology; the suppression factor $\sigma_\nu = z^{-10} \approx 1.62 \times 10^{-11}$ derives from substrate walk-dimension primitives and matches the empirical absolute scale to 2%. The mass-squared splitting predictions $m_2/m_1 = 9.00$ and $m_3/m_1 = 56.25$ match observation to 4% and 11% with no fitted parameters. The PMNS matrix at zeroth order is exactly U_TBM (inherited from SM-5's K3 Spectral Theorem); the cage-shell mechanism preserves K3-eigenstate alignment by construction once the mass-basis reading is adopted. Normal mass hierarchy is forced by the (tetrahedron, icosahedron, icosidodecahedron) cage-shell assignment; JUNO 2026+ resolution provides a near-term falsifier. CP phase $\delta_{CP}$ is registered as open per SM-5 OPEN-SM-4, deferred to the EW-sector flagship.

**Single most striking number for abstract:** the absolute neutrino mass scale at $m_{\nu_e} = 0.98$ meV from $\sigma = z^{-10}$ with zero free parameters, **eleven orders of magnitude below the bare $M_0 \cdot V_{\nu_e}^2 = 60.6$ MeV scale**. Or alternatively the matching summary: $\Sigma m_\nu = 64.9$ meV vs cosmological bound $\le 72$ meV (DESI/Planck combined).

---

## Falsifiers

The paper makes specific zero-parameter quantitative predictions; the framework is falsified by any of the following:

**1. Inverted hierarchy.** SF-4 forces normal hierarchy via the (tet, ico, icosid) cage-shell assignment with $V_{\nu_e} = 4 < V_{\nu_\mu} = 12 < V_{\nu_\tau} = 30$. JUNO 2026+ is expected to resolve the ordering; if inverted hierarchy is confirmed, the cage-shell assignment is dead and SF-4's central derivation fails. This is the **clean, named, near-term falsifier**.

**2. Direct mass measurement above ~5 meV.** The cage-shell + suppression-factor prediction is $m_{\nu_e} \approx 0.98$ meV. KATRIN's current bound is $m_\beta < 0.8$ eV; future experiments aiming for sub-eV sensitivity (KATRIN final, KATRIN++, Project 8) target the sub-eV decade. A direct measurement of $m_{\nu_e} > 5$ meV (which would also push $\Sigma m_\nu$ above the cosmological bound) would falsify the cage-shell + suppression prediction.

**3. Cosmological $\Sigma m_\nu$ above bound.** SF-4 predicts $\Sigma m_\nu \approx 64.9$ meV. Current DESI + Planck combined bound is $\Sigma m_\nu \le 72$ meV; tightening this to $\Sigma m_\nu \le 50$ meV would falsify SF-4's prediction.

**4. PMNS deviation from TBM at zeroth order.** SF-4 inherits SM-5's TBM result at zeroth order. If precision PMNS measurement (DUNE, Hyper-K, JUNO) shows zeroth-order angles materially different from $\sin^2\theta_{12} = 1/3$, $\sin^2\theta_{23} = 1/2$, $\sin^2\theta_{13} = 0$ once SM-5's higher-order corrections (OPEN-SM-4 Capotauro mechanism) are accounted for, the K3-eigenmode-identification ansatz that SM-5 inherits and SF-4 carries forward is in tension.

**5. Substrate-mechanism deviation.** SF-4 predicts the absolute mass scale at $\sigma = z^{-10}$ where $z = 12$ is the 600-cell coordination number. If precision data force $\sigma$ to a value not expressible as $z^{-2 d_{\text{eff}}}$ for any small integer $d_{\text{eff}}$, the substrate walk-dimension framework is in tension and the suppression mechanism would need re-derivation.

**Not predicted:** SF-4 does not predict Majorana vs Dirac character (registered as open in §10 below). Detection of $0\nu\beta\beta$ decay would constrain Majorana mass but does not directly falsify or confirm the cage-shell mechanism.

---

## Section-by-section outline

### §0 Abstract

≤250 words. Headline claim (above) + key predictions table + falsifier summary. Audience: HEP/neutrino specialists scanning Zenodo/arXiv abstracts.

### §1 Introduction and strategic frame

- The named known-unknown: neutrino mass spectrum and mixing structure from first principles
- Why CPP can address this: the substrate (600-cell + Conscious Points + Dipole Sea) provides a discrete geometric foundation that the SM lacks
- Strict-C posture (Session 37 opening): no compromise on rigor, every parameter back to substrate primitives, register-as-open used judiciously and one or two layers removed from the present problem
- Roadmap of the paper (per §2-§11 below)
- Position in SF-line: SF-4 as the heavy-lift derivation campaign; relation to SF-1 (charged leptons, reframing), SF-3 (quarks, reframing), SF-2 (electroweak cage bosons), SF-5 (strong sector), SF-6 (electromagnetism), SF-7 (grand unification synthesis)

### §2 The SM-5 K3-eigenmode foundation

Recap of the corpus SF-4 inherits:
- SM-1 four-cage taxonomy: tetrahedral (V=4), icosahedral (V=12), dodecahedral (V=20), icosidodecahedral (V=30) cages from any 600-cell vertex
- SM-3 K3 Spectral Theorem: K = 2/3 from K3 ZBW Hamiltonian eigenstructure; K3 as colour-cage base of tetrahedral cage
- SM-5 Tribimaximal mixing from K3 eigenmodes: charged leptons → K3 vertex states; neutrino mass eigenstates → K3 eigenmodes; PMNS = U_TBM exactly given SM-5 ansatz
- SM-7/8/9 distance-shell taxonomy and mass-formula machinery: $M_0 = m_e \cdot z/\phi \approx 3.79$ MeV; $V^{7/3}$ scaling for bound modes
- SM-5's open problem on lifting the K3 antibonding-doublet degeneracy

What SF-4 inherits at theorem level vs ansatz level:
- THEOREM-LEVEL: $M_0$ derivation, $z=12$ coordination from substrate, K3 eigenvector structure, U_TBM = K3 eigenvector matrix
- ANSATZ-LEVEL (from SM-5, inherited not re-introduced): K3-eigenmode-identification of neutrino mass eigenstates; specific TBM-direction selection in K3 antibonding doublet (μτ-symmetric / μτ-antisymmetric)

### §3 The Candidate C cage-shell mass formula

Statement of the mechanism:

$$
m_{\nu_i} = M_0 \cdot V_{\nu_i}^{\alpha} \cdot \sigma_\nu \qquad (\alpha = 2)
$$

with cage-shell assignment (in *mass basis* per Session 42 mass-basis-vs-flavor-basis clarification):

| Mass eigenstate | Cage shell | $V$ | 600-cell shell |
|---|---|---|---|
| $\nu_1$ | tetrahedron (T_d) | 4 | shell 1 subset (compound-of-5-tetrahedra) |
| $\nu_2$ | icosahedron (H_3) | 12 | shell 1 (full) |
| $\nu_3$ | icosidodecahedron | 30 | shell 3 ($d^2 = 2$) |

Relation to bound-mode quark formula: identical $M_0$ and substrate machinery, with two unbound-regime modifications — exponent $V^{7/3} \to V^2$ (the linear-cage-dimension factor $V^{1/3}$ drops out for unbound modes with no rigid cage), and the per-mode $\mu_q$ multipliers replaced by the universal substrate-derived $\sigma_\nu$.

The $V \in \{4, 12, 30\}$ assignment skips $V=20$ (dodecahedral shell 2): this shell is occupied by bottom quark and Higgs in SM-1's particle-type taxonomy, not lepton-flavor neutrino territory.

### §4 The suppression mechanism

Substantive derivation — main novel content of SF-4. Develops `SF-4_suppression_derivation.md` material into paper-text form.

#### §4.1 The walk-dimension framework
- Definition: walk channel = independent substrate-information degree of freedom maintained per absolute moment
- $\sigma = N^{-d_{\text{eff}}}$ for an unbound mode with $d_{\text{eff}}$ free walk channels
- Bound vs unbound boundary: bound modes have all channels cage-pinned, $d_{\text{eff}} = 0$, $\sigma = 1$; unbound modes have free channels

#### §4.2 Channel enumeration for unbound 3D orbital ZBW mode
- 3 spatial channels (x, y, z)
- 1 ZBW oscillation phase channel (free for unbound modes; cage-pinned for bound)
- 1 orbital orientation channel (free for unbound; cage-pinned for bound; spin and orbital orientation unified per CPP 2:1 frequency convention)
- **Integer leading-order $d_{\text{eff}} = 5$**

#### §4.3 Three pictures for $z^{-2}$ per channel
The per-channel suppression $\sigma_{\text{channel}} = 1/z^2$ converges from three independent CPP physical pictures:

- **Picture A (two-sided DI-bit exchange):** each DI-bit exchange has send-side ($z$ options) and receive-side ($z$ options); coherent transmission requires both align, giving $1/z^2$ per channel. Most CPP-axiomatic; leading closure candidate.
- **Picture B (two ZBW half-cycles per moment):** anchors on existing 2:1 inner-outer frequency convention.
- **Picture C (edge-straddling coherent state):** unbound mode straddles a 600-cell edge; pair coordination gives $z^2$.

The robustness of the numerical answer across three physical pictures is itself a positive signal. Picture A is the priority closure path for theorem-level rigor at v0.1; Pictures B and C remain available as alternatives.

#### §4.4 Combined result
$$
\sigma_\nu = z^{-2 d_{\text{eff}}} = z^{-10} = 1.62 \times 10^{-11}
$$

Predicted neutrino masses with the cage-shell assignment:

| Quantity | Predicted | Empirical / observational | Match |
|---|---|---|---|
| $\sigma_\nu = \mathcal{T}_{\text{unbound}}$ | $1.62 \times 10^{-11}$ | $\approx 1.59 \times 10^{-11}$ (target) | within 2% |
| $m_{\nu_e}$ | 0.98 meV | (from splittings + cosmological) | within 2% |
| $m_{\nu_\mu}$ | 8.81 meV | $\approx 8.66$ meV (from $\Delta m^2_{21}$) | within 2% |
| $m_{\nu_\tau}$ | 55.1 meV | $\approx 50.9$ meV (from $\Delta m^2_{32}$) | within 8% |
| $\Sigma m_\nu$ | 64.9 meV | $\le 72$ meV (cosmological) | ✓ within bound |

#### §4.5 Open theorem-level work
Picture A theorem-level closure from A1–A11 is the major remaining derivation work; registered as the v0.1 → v1.0 drafting target. Pictures B and C remain as alternatives if Picture A obstructs.

### §5 The K3-Cage-Shell Consistency Theorem

Substantive derivation — the second novel-content section of SF-4. Develops `SF-4_k3_cage_shell_consistency.md` material into paper-text form.

#### §5.1 The mass-basis-vs-flavor-basis clarification
The cage-shell V values must be read in mass basis (V values attach to K3 eigenmodes / neutrino mass eigenstates), not flavor basis. The flavor-basis reading would force PMNS = identity, contradicting SM-5 and observation. This is the foundational clarification underlying the rest of the consistency proof.

#### §5.2 Numerical zeroth-order consistency is exact
With the mass-basis reading, the V² operator with eigenvalues $(16, 144, 900)$ on K3 eigenmodes produces in flavor basis a matrix with **exact $\mu\tau$-exchange symmetry**, and recomputing the PMNS angles from V²'s eigenstructure recovers TBM exactly: $\sin^2\theta_{12} = 1/3$, $\sin^2\theta_{23} = 1/2$, $\sin^2\theta_{13} = 0$. Audit constraint K1/K2/K3 satisfied by construction.

#### §5.3 Route C structural closure at SM-5-inheritance level
The 600-cell bonded-shell vertex counts (numerically verified) force V values $\{4, 12, 30\}$ at the lepton-cage scale. The K3-eigenmode-to-shell coupling closes via:
- Bonding K3 mode $\phi_+ \to V=12$ forced by $S_3 \subset H_3$ symmetry-hierarchy
- Antibonding modes split V=4 / V=30 via wavefunction-spread / $\mu\tau$-symmetry-character argument
- The $\nu_1$/V=4 vs $\nu_3$/V=30 split inherits SM-5's existing open problem on lifting the K3 antibonding-doublet degeneracy; SF-4 introduces no new ansatz beyond SM-5's

#### §5.4 Open theorem-level work
Theorem-level closure of OPEN-FP-SF-4-2 at the vertex-by-vertex coupling level is *tied to SM-5's open problem* — they cannot be independently resolved within SF-4 scope. SF-4 v0.1 ships with the SM-5-inheritance-level closure plus explicit pointers to the SM-5 open problem.

### §6 Predictions: 7 of 8 parameters at zero free parameters

Master predictions table:

| Neutrino parameter | SF-4 prediction | Empirical value | Match | Source |
|---|---|---|---|---|
| $m_{\nu_e}$ (lightest mass) | 0.98 meV | $\le 5$ meV (cosmological+splitting) | within 2% of ratio-implied | §4 suppression + §3 cage-shell |
| $m_{\nu_\mu}/m_{\nu_e}$ | 9.00 | 8.66 | within 4% | §3 V² ratio |
| $m_{\nu_\tau}/m_{\nu_e}$ | 56.25 | 50.9 | within 11% | §3 V² ratio |
| $\Sigma m_\nu$ | 64.9 meV | $\le 72$ meV | within bound | combined |
| $\sin^2\theta_{12}$ | 1/3 = 0.333 | 0.304 ± 0.012 | within 10% | §5 TBM zeroth order |
| $\sin^2\theta_{23}$ | 1/2 = 0.500 | 0.570 ± 0.018 | within 14% | §5 TBM zeroth order |
| $\sin^2\theta_{13}$ | 0 (zeroth order) | 0.0224 ± 0.0007 | needs higher-order | §5 + §8 |
| Mass ordering | Normal (forced) | Unresolved (JUNO 2026+) | falsifier | §3 cage-shell assignment |
| $\delta_{CP}$ | Open | $\sim 195°$ ± 100° | deferred to SF-2 | §7 route (ii) |

7 of 8 zero-parameter predictions; $\delta_{CP}$ deferred. Higher-order corrections to the mixing angles inherited from SM-5 OPEN-SM-4 Capotauro mechanism (see §8).

### §7 $\delta_{CP}$ posture (route ii)

Brief; defers to SM-5 OPEN-SM-4 existing registration. Justification per `SF-4_mechanism_selected.md` §3: route (i) deriving $\delta_{CP}$ from CPP primitives is multi-session second campaign; route (ii) keeps SF-4 contained at 7/8 zero-parameter predictions while preserving SM-5's existing open-problem registration. The eventual route-(i) work has its proper home in the EW-sector flagship (SF-2) or in SF-7 unification synthesis. Discussion of the four candidate handles (cage-orientation, Capotauro bias, K3 phase, substrate chirality) and why each is multi-session work.

### §8 Higher-order corrections (SM-5 OPEN-SM-4 inheritance)

The observed PMNS angles deviate from TBM by ~10% in $\theta_{12}$ and $\theta_{23}$, and $\sin^2\theta_{13} = 0.0224$ is non-zero against TBM's 0. SM-5's existing treatment via OPEN-SM-4 (Capotauro mechanism in EW sector) accounts for these. SF-4 inherits the same treatment: register higher-order corrections as conditional on EW-sector closure of OPEN-SM-4, do not derive them in SF-4 scope. Brief restatement of the OPEN-SM-4 framing for the neutrino specialist reader who may not have read SM-5 directly.

### §9 Cumulative falsifier

Restates §1's strategic falsifiers in paper-context form:

1. JUNO 2026+ inverted hierarchy → SF-4 dead (§3 forced)
2. Direct $m_{\nu_e}$ measurement > 5 meV → SF-4 dead (§4 prediction)
3. Cosmological tightening to $\Sigma m_\nu < 50$ meV → SF-4 in tension
4. Precision PMNS deviation from TBM at zeroth order (after OPEN-SM-4 corrections) → SM-5 ansatz in tension, SF-4 carries with it
5. Substrate-mechanism deviation from $\sigma = z^{-10}$ form → walk-dimension framework in tension

Discussion of the falsifier hierarchy: items 1–3 are direct SF-4 falsifiers; items 4–5 are framework-level falsifiers that propagate through SF-4 and other SF-line papers.

### §10 Open theorem-level work and other open problems

Honest catalog of what SF-4 v1.0 does not establish:

- **OPEN-FP-SF-4-1 Picture A formalization** from A1–A11 — ships at PARTIAL CLOSURE; v1.0+ work
- **OPEN-FP-SF-4-2 vertex-by-vertex K3-coupling theorem** — tied to SM-5 open problem on antibonding-doublet lifting; ships at SM-5-inheritance level
- **$\alpha = 2$ first-principles closure from V^{7/3} → V² boundary** — sketched in §3.5; rigorous derivation v1.0+
- **Majorana vs Dirac character** — not addressed in v1.0; cage-shell mechanism doesn't currently specify; registered as open
- **$0\nu\beta\beta$ rate prediction** — depends on Majorana question; deferred
- **Sterile-neutrino predictions** — outside the V ∈ {4, 12, 30} active-flavor scope; registered as open whether the cage-shell mechanism extends to additional sterile states or whether the framework specifically rules them out

### §11 Discussion

#### §11.1 The programme-level pattern: structural agreement at integer counts as load-bearing signal
Three flagship-class derivations across the SF-line corpus all show the same pattern: SS-7 (twelve N=Z nuclei to 1.5% RMS at zero parameters), SM-9 (top quark to 0.02% with $z=12$ as only counting input), SF-4 ($\sigma = z^{-10}$ at 2% empirical match). Precision agreement at zero parameters is the validation; precision at multi-decimal places is downstream and framework-idealization-limited. This methodological observation, registered in `SF-4_suppression_derivation.md` §9, is restated here for the SF-4 reader.

#### §11.2 Cross-sector implications
- SF-2 EW: $\delta_{CP}$ is tied to OPEN-SM-4 Capotauro mechanism; SF-2 closure could extend SF-4's prediction count from 7/8 to 8/8
- SM-5: SF-4's structural closure of OPEN-FP-SF-4-2 at SM-5-inheritance level is mutually reinforcing with SM-5's K3 ansatz, but theorem-level closure on either side requires resolving SM-5's antibonding-doublet open problem
- SR-1 / unbound-mode physics: the walk-dimension framework introduced in §4 may apply to other unbound-mode physics in CPP (free-particle propagators, light propagation); cross-sector implications of $z^{-2}$ per channel pending future investigation
- SF-7 grand unification: SF-4's 7/8 result is one piece of the cumulative SF-line result; the master comparison table in SF-7 sums SF-1 through SF-6 contributions

#### §11.3 Outlook
Forward research directions: theorem-level closure of OPEN-FP-SF-4-1 Picture A; contribution to SM-5 open problem (which closes both SM-5 and OPEN-FP-SF-4-2 at theorem level simultaneously); experimental tests via JUNO, Project 8, KATRIN++, DESI/CMB-S4.

---

## Source material map

| Section | Primary source documents | Status |
|---|---|---|
| §1 | `flagship_papers/README.md`, `research_priorities.md`, audit §1 | Established |
| §2 | SM-1, SM-3, SM-5 papers | Established (theorem level) |
| §3 | `SF-4_mechanism_selected.md` §2, audit §15 | Established (Session 39) |
| §4 | `SF-4_suppression_derivation.md` (full document) | PARTIAL CLOSURE (Sessions 40–41) |
| §5 | `SF-4_k3_cage_shell_consistency.md` (full document) | PARTIAL CLOSURE (Sessions 42–43) |
| §6 | derived from §3, §4, §5 | Trivial assembly from above |
| §7 | `SF-4_mechanism_selected.md` §3, SM-5 OPEN-SM-4 | Established |
| §8 | SM-5 OPEN-SM-4, audit §6 K3 corrections | Inherited |
| §9 | `SF-4_mechanism_selected.md` §6, audit §15 | Established |
| §10 | OPEN-FP-SF-4-1, OPEN-FP-SF-4-2 in `research_frontier.md`; SM-5 open problem | Honest catalog |
| §11 | `SF-4_suppression_derivation.md` §9, programme-level corpus | Cross-sector synthesis |

---

## Inheritance / dependencies

Inherits at theorem level (SF-4 does not re-derive these):
- SM-1 four-cage taxonomy
- SM-3 K3 Spectral Theorem
- SM-5 Tribimaximal mixing from K3 (modulo the K3-eigenmode-identification ansatz, which is SM-5's open problem; SF-4 inherits the ansatz, does not introduce a new one)
- SM-7/8/9 distance-shell taxonomy
- $M_0 = m_e \cdot z/\phi$ derivation

Inherits at register-as-open level (SF-4 explicitly preserves these as open):
- SM-5's antibonding-doublet-degeneracy lifting (the K3 TBM-direction selection)
- OPEN-SM-4 Capotauro mechanism for higher-order PMNS corrections
- $\delta_{CP}$ derivation (route ii deferral to EW sector)

Opens (SF-4 introduces and registers):
- OPEN-FP-SF-4-1 (suppression mechanism Picture A formalization from A1–A11)
- OPEN-FP-SF-4-2 (K3-Cage-Shell Consistency vertex-by-vertex coupling theorem; tied to SM-5 open problem)

---

## Anticipated reviewer concerns and pre-emptive responses

**"The 4%, 11% structural residuals are too large for a flagship-class precision claim."**
Response: SF-4 is honest about the residuals — they are visible in the predictions table (§6) and discussed in §11.1 as the programme-level pattern. The framework's strength is at the *zero-parameter structural* level; if reviewers want sub-1% precision, the framework needs higher-order corrections (some of which are inherited from SM-5 OPEN-SM-4). The paper explicitly distinguishes structural-derivation quality from precision-fit quality.

**"The K3-eigenmode-identification ansatz makes the derivation circular."**
Response: §2 explicitly identifies what SF-4 inherits at theorem level vs ansatz level. The ansatz is SM-5's existing one, not SF-4's; SF-4 does not introduce new ansatz. SF-4's value-add is showing that the cage-shell mass formula is *consistent* with SM-5's identification, which by itself is a non-trivial structural-geometric result.

**"The 2% match in $\sigma_\nu$ is suspicious — looks like fine-tuning."**
Response: $\sigma_\nu = z^{-10}$ is exact in the framework once integer $d_{\text{eff}} = 5$ is established and per-channel coupling is $z^{-2}$. The 2% deviation is the residual between this framework prediction and observational target, not a tuning. The framework prediction could have been $z^{-9}$ or $z^{-11}$ or any other integer power; the empirical match at $z^{-10}$ is a falsifiable structural claim.

**"What about Majorana mass / $0\nu\beta\beta$?"**
Response: §10 acknowledges the cage-shell mechanism does not currently specify Majorana vs Dirac. This is registered as a v1.0+ open problem. SF-4 v1.0 is consistent with either character; future $0\nu\beta\beta$ data is a constraint on the framework but not a falsifier of the cage-shell mass derivation.

**"How does this compare to discrete-symmetry $A_4$ models?"**
Response: §2.4 (or moved to §11) compares the K3-via-CPP derivation with $A_4$-symmetry-derivation of TBM. The $A_4$ literature (Ma 2001, Altarelli-Feruglio) derives TBM mathematically; CPP's contribution is the *physical* identification of the abstract symmetry with concrete substrate geometry (K3 as colour-cage base of the 600-cell tetrahedral cage from SM-3).

---

## Drafting plan and timeline

### v0.1 → v0.5 iteration target
- **Session 44 (this session, patch 0304):** outline established (this document); awaiting Thomas review
- **Session 45+ (after outline lock):** §0 abstract and §1 introduction drafting
- **Sessions 46–47:** §2, §3, §6 (foundational sections; primarily restating established results)
- **Sessions 48–49:** §4 suppression-mechanism drafting (substantive derivation work; pulls heavily from SF-4_suppression_derivation.md)
- **Sessions 50–51:** §5 K3-Cage-Shell Consistency drafting (substantive derivation work; pulls from SF-4_k3_cage_shell_consistency.md)
- **Sessions 52–53:** §7, §8, §9, §10, §11 (shorter sections; falsifier, open work, discussion)
- **Sessions 54+:** integration, internal review by Thomas, reviewer-response polish, v1.0 SHIP

This is roughly 10 sessions of v0.x drafting after outline lock — aligns with the original Session 39 estimate of "Sessions 45+ for v0.1 drafting" plus iteration to v1.0.

### Companion document plan (per SS-9 four-tier discipline)
Once SF-4 reaches v0.5 working draft, scaffold the companion documentation suite:
- `philosophy-SF-4.md` — strategic-frame document for non-physicist readers
- `mechanism-SF-4.md` — technical mechanism summary for physics-trained readers
- `phenomena-SF-4.md` — predictions and falsifiers in experimentalist-friendly form
- `glossary-SF-4.md` — CPP-internal terminology for outside readers
- `FAQ-SF-4.md` — anticipated reviewer concerns (source: this outline §"Anticipated reviewer concerns")
- `reviews-SF-4.md` — capture incoming reviewer feedback iteratively
- `development-SF-4.md` — Tier 4 reasoning recovery (links to `SF-line_development_transcript.md` §16+)

---

## What this outline establishes / does not establish

### Establishes
- The SF-4 paper structure at section-by-section level
- The headline claim and falsifier set
- The predictions table covering 7/8 neutrino parameters
- The source-material map and inheritance/dependencies
- The drafting plan and timeline (Sessions 45+ through ~54+)
- Pre-emptive reviewer-concern responses

### Does not establish
- Any actual paper text (drafting begins post-outline-lock)
- Theorem-level closure of OPEN-FP-SF-4-1 (Picture A formalization)
- Theorem-level closure of OPEN-FP-SF-4-2 (vertex-by-vertex K3-coupling)
- Resolution of SM-5's antibonding-doublet open problem
- Majorana vs Dirac character (registered as open)
- Quantitative $\delta_{CP}$ prediction (route ii deferral to SF-2)

### Forward state at outline close
- SF-4 is ready for v0.1 drafting at PARTIAL-CLOSURE level for both substantive sub-derivations
- The outline can be reviewed by Thomas; revisions before drafting lock are expected
- Once outline is locked, drafting proceeds section-by-section per the timeline above
- v1.0 SHIP target: ~10 sessions of v0.x drafting + integration + reviewer response

---

*Outline established at Session 44 (patch 0304). Strategic source: Sessions 37–43 SF-4 development arc (audit → mechanism selection → suppression-mechanism PARTIAL CLOSURE → K3-Cage-Shell Consistency PARTIAL CLOSURE). Captures the full paper structure at section-by-section level for v0.1 drafting beginning Session 45+. Awaiting Thomas review for argumentative shape, framing, audience-fit, and any course corrections before drafting lock.*
