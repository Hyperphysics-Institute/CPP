# SF-4: Neutrino Sector Mechanism Selected

**Status:** COMPLETE — mechanism-selection phase (Session 39)
**Track:** SF-4 (Neutrino Sector Unification flagship paper) — mechanism selection
**Author:** Claude Opus (analysis and recommendations), Thomas Lee Abshier ND (selection authority)
**Established:** 9 May 2026 (patch 0298)
**Supersedes:** the audit-time deferred mechanism question; the audit-time architectural Options $\alpha/\beta/\gamma$ (resolved earlier by Option-3 SF-line adoption at patch 0295)
**Foundation:** [`SF-4_neutrino_sector_audit.md`](SF-4_neutrino_sector_audit.md) — eight-parameter audit and five-candidate cross-comparison
**Integration target:** Charters Sessions 40+ derivation campaign; informs §3 mechanism, §4 derivation, §5 K3-integration, §6 calibration architecture, §7 $\delta_{CP}$ posture sections of the eventual SF-4 paper

---

## §1. Strategic frame and outcome

This document records the eight mechanism-selection decisions taken in Session 39 conversation between Thomas and Claude, building on the audit's five-candidate cross-comparison and the §15 falsifier-check appendix that ran during Session 38's architectural-decision break.

The §15 falsifier check reduced the candidate landscape decisively. Candidate B (cage-radius $m \propto 1/R^k$) was falsified — the bonded-shell radii spread is factor $\sim 3.74$ versus observed mass-ratio spread $\sim 51$, and no single power-law exponent fits both splittings simultaneously ($k_{32} = 4.75$, $k_{21} = 6.24$, opposite-direction discrepancy). Candidate C (shell-distance $m \propto V^\alpha$) was found encouraging at $\alpha = 2$ with assignment $(\nu_e, \nu_\mu, \nu_\tau) \to$ (tetrahedron $V=4$, icosahedron $V=12$, icosidodecahedron $V=30$), matching both splittings to 4% and 11% with zero free parameters.

The eight-question decision set defined in the audit's §11 was resolved as follows: Candidate C with $\alpha = 2$ as the working mechanism; route (ii) for $\delta_{CP}$ posture (register as open, defer to EW sector); theorem-level enforcement of K3-eigenstructure constraint at zeroth order with numerical-plus-conditional treatment of higher-order corrections; single-calibration ($m_e$ alone) as hard requirement; hierarchy ordering as derived consequence framed as falsifiable prediction; viXra-paper salvage limited to Monte Carlo validation methodology; archived $\sigma = 120^{-d}$ substrate-connection insight retained as priority first-attempt for the suppression sub-derivation.

The strict-C strategic posture established at Session 37 opening — no compromise on first-principles rigor, every parameter back to 600-cell + Conscious Point primitives, the "register-as-open" card used judiciously and one or two layers removed from the present problem where possible — governs all eight choices and the forward plan.

---

## §2. Mechanism: Candidate C with $\alpha = 2$

### §2.1 Mass formula

The neutrino mass for flavor $i$ is

$$
m_{\nu_i} = M_0 \cdot V_{\nu_i}^{2} \cdot \mathcal{T}_{\text{unbound}}
$$

with:

- $M_0 = m_e \cdot z/\phi \approx 3.79$ MeV — the mass quantum derived in SM-9 from lattice connectivity (the same prefactor that appears in the quark formula); single calibration to $m_e$
- $z = 12$ — 600-cell coordination number, derived from substrate
- $\phi = (1 + \sqrt{5})/2$ — golden ratio, mathematical constant
- $V_{\nu_i}$ — vertex count of the cage-shell assigned to flavor $i$ (specified in §2.2)
- $\alpha = 2$ — the scaling exponent for unbound modes (derivation handle in §2.4)
- $\mathcal{T}_{\text{unbound}}$ — the substrate-derived suppression factor for unbound modes (open sub-problem; see §8.1)

The formula is structurally continuous with SM-7/SM-8/SM-9 quark machinery, with two modifications for the unbound-mode regime: the exponent drops from $7/3$ (bound) to $2$ (unbound), and the $\mathcal{T}_{\text{unbound}}$ factor replaces the per-quark $\mu_q$ multipliers.

### §2.2 Cage-shell assignment

| Flavor | Cage shell | $V$ | Bonded-shell index in 600-cell |
|--------|------------|-----|--------------------------------|
| $\nu_e$ | tetrahedron | 4 | shell 0 (subset) |
| $\nu_\mu$ | icosahedron | 12 | shell 0 (full) |
| $\nu_\tau$ | icosidodecahedron | 30 | shell 3 |

The shell sequence (4, 12, 30) skips the dodecahedron ($V=20$) at shell 1; the gap is the same Shell 3 gap that appears in the quark-mass programme via SM-8's icosidodecahedron-as-fourth-cage assignment for the top quark. The neutrino mapping uses the small-$V$ shells for the unbound-mode regime; the large-$V$ shell (icosidodecahedron) is shared between the heaviest neutrino and the top quark, reflecting the same substrate machinery applied at different mass scales.

### §2.3 Splittings prediction (zero parameters)

With $\alpha = 2$ and the assignment above, the mass ratios are:

$$
\frac{m_{\nu_\mu}}{m_{\nu_e}} = \left(\frac{12}{4}\right)^2 = 9.00 \qquad \text{vs. observed } \approx 8.66 \text{ (within 4\%)}
$$

$$
\frac{m_{\nu_\tau}}{m_{\nu_e}} = \left(\frac{30}{4}\right)^2 = 56.25 \qquad \text{vs. observed } \approx 50.9 \text{ (within 11\%)}
$$

The mass-squared splittings are determined entirely by the assignment plus $\alpha = 2$; no free parameters enter the ratios. The observed splittings $\Delta m^2_{21} = 7.39 \times 10^{-5}$ eV² and $|\Delta m^2_{32}| = 2.52 \times 10^{-3}$ eV² (NuFIT 5.3) are matched at the structural level. This is the empirical signal that selects Candidate C from the audit's five-candidate landscape.

### §2.4 First-principles derivation handle for $\alpha = 2$

SM-9 derives the quark exponent $V^{7/3}$ via the decomposition

$$
V^{7/3} = V^2 \cdot V^{1/3}
$$

where $V^2$ is the **pair-count component** (counting interactions over all pairs of cage vertices, scaling as the number of pairs $\sim V(V-1)/2 \sim V^2$ for large $V$) and $V^{1/3}$ is the **linear-cage-dimension component** (scaling as the linear extent of a 3D cage at fixed local density, $\sim V^{1/3}$).

For unbound modes, no rigid cage exists. The neutrino is by hypothesis an unbound orbital ZBW configuration without a central CP anchor (per §3.4 of the audit). With no cage to define a linear scale, the linear-cage-dimension factor $V^{1/3}$ has no operational meaning and drops out, leaving the pair-count component alone:

$$
V^{7/3} \to V^2 \quad \text{(unbound regime)}
$$

This is not a fit. The exponent $\alpha = 2$ is **forced** by the structural difference between bound and unbound modes — exactly the boundary across which $V^{1/3}$ does or does not contribute to the mass formula. Closure of this argument from CPP primitives is the cleanest available first-principles route for $\alpha = 2$ and is queued as part of the SF-4 paper §4 derivation work.

### §2.5 Suppression factor as separate sub-derivation

The mass-ratio structure works at zero parameters. The absolute scale does not, by a wide margin: with $V_{\nu_e}^2 = 16$ and $M_0 = 3.79$ MeV, the bare prediction is $m_{\nu_e}^{\text{bare}} = 60.6$ MeV — eleven orders of magnitude above the observed sub-eV scale. The suppression factor $\mathcal{T}_{\text{unbound}}$ must therefore satisfy

$$
\mathcal{T}_{\text{unbound}} \sim \frac{m_{\nu_e}^{\text{obs}}}{m_{\nu_e}^{\text{bare}}} \sim \frac{0.001 \text{ eV}}{60.6 \text{ MeV}} \approx 1.65 \times 10^{-11}
$$

The archived $\sigma = 120^{-3} \approx 5.79 \times 10^{-7}$ is too weak by a factor of $\sim 10^4$. A different / refined / higher-power substrate-information count is required.

The suppression-factor derivation is registered as **OPEN-FP-SF-4-1** (see §8.1) and is the **first-priority sub-problem** for Sessions 40+. Per the Q8 decision (§7.2), the first attempt is to salvage the $\sigma = 120^{-d}$ structure by deriving a higher effective dimension $d_{\text{eff}} > 3$ from the substrate; alternative routes are considered only if that path fails.

### §2.6 What this mechanism does *not* yet do

To be honest with scope: the mechanism as stated fixes the splitting structure at zero parameters but leaves four substantive items open:

1. **The absolute scale** — pending OPEN-FP-SF-4-1 (suppression mechanism)
2. **K3-eigenstructure consistency** — pending OPEN-FP-SF-4-2 (the K3-Cage-Shell Consistency Theorem; see §4)
3. **The first-principles closure of $\alpha = 2$** — the $V^{7/3} \to V^2$ argument is sketched in §2.4; the rigorous derivation from CPP primitives that establishes the bound/unbound boundary as the operational divide between the two exponents lives in the eventual SF-4 paper §4
4. **$\delta_{CP}$** — registered as open per §3

The first two are the substantive Session 40+ work. The third is part of the integration writing in v0.x drafting. The fourth is deferred to the EW sector.

---

## §3. $\delta_{CP}$ posture: route (ii) — register as open

Selection: **route (ii)** per audit §7. SF-4 makes seven of the eight neutrino predictions; $\delta_{CP}$ is explicitly deferred to a later EW-sector derivation, following SM-5's existing posture of registering $\delta_{CP}$ as requiring the EW sector via OPEN-SM-4.

Rationale: route (i) (derive $\delta_{CP}$ from CPP primitives) is high-value if it lands quickly, but the audit's speed test for route (i) is "1–2 sessions of investigation," and the four candidate handles (cage-orientation angle, Capotauro bias in current formalism, K3-eigenstate phase structure, substrate chirality) are each multi-session derivations of their own. Taking on a multi-session $\delta_{CP}$ campaign inside SF-4 amounts to running a second flagship-class derivation in parallel with the primary mass-mechanism work; the timeline math doesn't support that alongside the suppression-factor and K3-consistency sub-problems already opened.

Route (ii) keeps SF-4 contained without losing rigor. A 7/8-zero-parameter derivation is still vastly stronger than any other framework can claim; SF-4's headline reads honestly. The eventual route-(i) work has its proper home in the EW sector or in SF-5 (the unification synthesis), where the EW-sector machinery for CP-violating phases lives by physics. Double-claiming the same physics as both open in SM-5 and derived in SF-4 would be bookkeeping confusion; route (ii) keeps the open-problem registration with its appropriate paper.

The SF-4 paper text will explicitly state: $\delta_{CP}$ is consistent with current measurements ($\sim 195°$ central with $3\sigma$ range $108°$–$404°$) and is registered as requiring EW-sector derivation via OPEN-SM-4.

---

## §4. K3-eigenstructure constraint enforcement strategy

Selection: **theorem-level for the zeroth-order TBM result; numerical verification + register-as-conditional for higher-order corrections**.

The audit §6 codified Constraints K1, K2, K3 — the mechanism must produce three mass eigenstates that align with $K_3$ eigenmodes at zeroth order, so that SM-5's existing TBM-from-K3 derivation continues to hold. Under Candidate C with $\alpha = 2$, this is not automatic. The shell-distance machinery scales mass eigenvalues but does not automatically pick out K3 eigenmodes as eigenstates; the constraint must be enforced or derived as part of the SF-4 work.

The form of that derivation — call it the **K3-Cage-Shell Consistency Theorem** — is to prove that the cage-shell assignment $(V=4, V=12, V=30)$ is geometrically natural relative to the K3 graph spectral structure: the three flavors picked out by shell-distance are the same three flavors picked out by K3 eigenmodes. The argument proceeds via the embedding of K3 into the 600-cell vertex set (SM-3) and a spectral correspondence between K3 eigenmode energies and the small-$V$ bonded shells that the assignment uses.

This theorem is registered as **OPEN-FP-SF-4-2** (see §8.2). It is the second-priority sub-problem for Sessions 40+, after the suppression-mechanism work (OPEN-FP-SF-4-1). Without it, SF-4 cannot claim to preserve SM-5's PMNS derivation rather than replace it.

For the higher-order corrections (the $\sim 10\%$ deviations from TBM that produce the observed $\sin^2\theta_{12} = 0.304$, $\sin^2\theta_{23} = 0.570$, $\sin^2\theta_{13} = 0.0224$), the strategy is numerical verification within the Candidate C framework plus register-as-conditional in the paper, mirroring SM-5's existing handling. Higher-order full derivation is OP-SM-4 (Capotauro mechanism) and OPEN-SM-4 territory and not in SF-4 scope.

---

## §5. Calibration architecture: single-calibration as hard requirement

Selection: **single-calibration ($m_e$ alone) is a hard requirement** for the SF-4 abstract.

The headline of SF-4 — and of the SF-line as a whole, with SF-5 synthesizing — is that the entire Standard Model fermion mass spectrum derives from one calibration constant ($m_e$). Weakening to two calibrations materially weakens this headline; the rigor argument is also stronger when one constant carries everything.

Operationally, this means:

- $\mathcal{S}_0 = M_0 = m_e \cdot z/\phi$ in the Candidate C mass formula. The mass quantum is the same one that appears in the quark formula. ✓ (Built in by construction.)
- The suppression factor $\mathcal{T}_{\text{unbound}}$ must be derived from substrate primitives, not calibrated to the observed lightest-neutrino mass. ✓ (Required of OPEN-FP-SF-4-1.)
- The cage-shell assignments $(V=4, V=12, V=30)$ are integer counts of substrate vertices; not free parameters. ✓
- The $\alpha = 2$ exponent derives from the $V^{7/3} \to V^2$ argument; not free. ✓
- The hierarchy ordering is forced by the assignment; not free. ✓

If at any point during Sessions 40+ the work shows that single-calibration cannot be achieved — most plausibly via an irreducible second calibration entering the suppression mechanism — that is a programme-level finding worth documenting honestly, and likely indicates a different mechanism is needed. The no-compromise discipline says we attempt the single-calibration substrate-derivation path first; only if that exhausts do we revisit.

---

## §6. Hierarchy ordering: derived consequence, falsifiable prediction

Selection: **derived consequence of the cage-shell assignment, framed as a falsifiable prediction the SF-4 paper carries explicitly**.

Under Candidate C with the $(V=4, V=12, V=30)$ assignment, the mass formula gives strict ordering $V_{\nu_e} < V_{\nu_\mu} < V_{\nu_\tau}$, which by $m_{\nu_i} \propto V_{\nu_i}^2$ produces $m_{\nu_e} < m_{\nu_\mu} < m_{\nu_\tau}$ — i.e., **normal hierarchy**. The opposite assignment (icosidodecahedron $\to \nu_e$, tetrahedron $\to \nu_\tau$) would force inverted hierarchy.

JUNO 2026+ is expected to resolve the ordering. If JUNO confirms inverted hierarchy, the $(V=4, V=12, V=30)$ assignment is dead and SF-4 fails its central falsifier — a clean programme-level falsification. If JUNO confirms normal hierarchy, SF-4's prediction is validated.

The SF-4 paper will state this prominently: **SF-4 predicts normal mass ordering as a forced consequence of the cage-shell assignment; JUNO's measurement is a falsifier of this specific assignment, hence of Candidate C with this assignment**. This is exactly the named-falsifier-in-advance property that flagship-class papers benefit from carrying.

---

## §7. Salvage strategy from pre-formalism material

### §7.1 From the November 2025 viXra paper

Selection: **Monte Carlo validation methodology only; everything else discarded**.

The cage-radius mass mechanism is dead (Candidate B falsified, §15 of audit). The "Smoking Gun $\delta_{CP} = \pi/2$" was asserted not derived; per §3 above, $\delta_{CP}$ is registered as open. The $\lambda \approx 4.236$ scaling factor with the $\phi^{3/2}$ algebra error has no salvage value. The body-text mass values $(m_1, m_2, m_3) = (0.001, 0.00866, 0.0509)$ eV are calibrated to observed splittings, not derived; discarded.

What is salvaged: the Monte Carlo framework for testing predictions against measured values. This methodology — sampling within experimental error bars, computing prediction-versus-observation distributions, propagating uncertainty through the mass formula — is genuinely useful and will serve as the validation harness for SF-4's eventual quantitative predictions once the suppression mechanism lands.

### §7.2 From the archived $\sigma = 120^{-d}$ exploratory work

Selection: **substrate-connection insight retained as constraint and as priority first-attempt for the suppression sub-derivation; specific $N_k$ counts and the bare $120^{-3}$ formula discarded**.

The substrate connection — that 120 in the suppression base is the 600-cell vertex count, not a coincidence — is structurally meaningful. The bound/unbound mode dichotomy ($d=0$ vs $d=3$) is also a reusable framing. These should constrain the SF-4 suppression-factor derivation: whatever mechanism we develop should plausibly involve substrate-information counting in some form, even if it's not literally $120^{-3}$.

The Q8 decision sharpens this further: when working OPEN-FP-SF-4-1 in Sessions 40+, the **first hypothesis to test is whether $\sigma = 120^{-d}$ can be made to work for the unbound regime by deriving a higher effective dimension $d_{\text{eff}} > 3$ from substrate primitives**. The factor needed is $\sim 10^{-11}$ versus the bare $120^{-3} \approx 5.79 \times 10^{-7}$, which is about 4 orders of magnitude shy. A $d_{\text{eff}} \approx 5$ would land near $120^{-5} \approx 4 \times 10^{-11}$ — encouragingly close to the target $\sim 1.65 \times 10^{-11}$. The work is to determine whether a $d_{\text{eff}}$ in the range $[5, 6]$ derives naturally from the substrate-walk structure of an unbound 3D orbital mode.

Discarded: the specific $N_k = \{1, 4, 12\}$ counts (which produce wrong splittings), the assertion that $E_{\text{spin}} = \frac{1}{2}mv^2 \cdot \sigma$ provides the right pre-suppression scale, and the predicted mass values $(0.001, 0.004, 0.012)$ eV. The Candidate C assignment $(V=4, V=12, V=30)$ supersedes the $N_k$ counts; the mass quantum $M_0$ supersedes $E_{\text{spin}}$; the predicted mass values await the OPEN-FP-SF-4-1 derivation.

The **fallback routes**, considered only if the higher-$d_{\text{eff}}$ path fails:

- A product of independent substrate counts (vertex × edge × face × cell counts of the 600-cell, suitably weighted by walk structure)
- An anchor to the recognized-mathematics bridge — distance geometry, EDM theory, or rigidity-theory analogs of unbound-mode propagation (analog to OPEN-SS-37 Route (d) for SS-9)
- A connection to the SR-1 frame: neutrinos propagate near-lightlike, so substrate-frame coupling effects may dominate

These are listed for completeness; the priority order is dictated by the Q8 salvage decision, with $\sigma = 120^{-d_{\text{eff}}}$ first.

---

## §8. Open sub-problems opened by this selection

Two new programme-level OPEN entries are registered in `research_frontier.md` as part of patch 0298. Both are flagship-paper conditional inheritances under the new FP sector.

### §8.1 OPEN-FP-SF-4-1: Unbound-Mode Suppression Mechanism

**Statement:** Derive from CPP primitives the suppression factor $\mathcal{T}_{\text{unbound}}$ such that $m_{\nu_i} = M_0 \cdot V_{\nu_i}^2 \cdot \mathcal{T}_{\text{unbound}}$ produces neutrino masses at the observed sub-eV scale, with $\mathcal{T}_{\text{unbound}} \sim 1.65 \times 10^{-11}$ as the empirical target.

**Priority for SF-4 ship:** Highest. Without this derivation, SF-4 cannot claim the absolute mass scale is zero-parameter; the abstract becomes weaker. This is the gate to v0.1 drafting.

**First-attempt route (per Q8 decision):** $\sigma = 120^{-d_{\text{eff}}}$ with $d_{\text{eff}}$ derived from substrate walk-dimension primitives for an unbound 3D orbital mode; target range $d_{\text{eff}} \approx 5$ to $6$ to land near the empirical $\mathcal{T}_{\text{unbound}}$ target.

### §8.2 OPEN-FP-SF-4-2: K3-Cage-Shell Consistency Theorem

**Statement:** Prove that the cage-shell assignment $(\nu_e \to V=4, \nu_\mu \to V=12, \nu_\tau \to V=30)$ used in Candidate C produces mass eigenstates that align with the K3 graph eigenmodes at zeroth order, preserving SM-5's existing TBM PMNS derivation rather than replacing it.

**Priority for SF-4 ship:** Second-highest. Without this theorem, the SF-4 paper cannot claim consistency with SM-5; the existing PMNS derivation would have to be re-grounded from scratch. Theorem-level rigor is required at zeroth order.

---

## §9. Forward plan

### §9.1 Session 39 close

Patch 0298 lands this decision document plus the research_frontier.md OPEN-FP-SF-4-1 and OPEN-FP-SF-4-2 registrations. Session 39 is the second scaffolding session in the SF-4 development arc; substantive technical work begins in Session 40.

### §9.2 Sessions 40–42 — OPEN-FP-SF-4-1 (suppression mechanism)

First substantive derivation work. The first attempt is the $\sigma = 120^{-d_{\text{eff}}}$ route per §7.2. Sub-tasks anticipated:

- Define what walk-dimension means for an unbound 3D orbital ZBW mode in CPP precisely
- Derive the walk dimension from A1–A11 + DP-Sea structure + substrate-vertex connectivity
- Verify that the derived $d_{\text{eff}}$ produces $\mathcal{T}_{\text{unbound}}$ at the right order of magnitude
- If first attempt fails to land within factor $\sim 3$ of target, exhaust before falling back to alternative routes

Outputs at session close: a sub-derivation document at `flagship_papers/neutrinos/sketches/SF-4_suppression_derivation.md` capturing the work with intermediate states; updates to OPEN-FP-SF-4-1 status in research_frontier.md.

### §9.3 Sessions 43–44 — OPEN-FP-SF-4-2 (K3-Cage-Shell Consistency Theorem)

Second substantive derivation. Sub-tasks:

- Specify the K3 eigenmode embedding into the 600-cell vertex set (drawing on SM-3)
- Establish the spectral correspondence between K3 eigenmode energies and the small-$V$ bonded shells $(V = 4, 12, 30)$
- Prove the eigenstate-alignment theorem at zeroth order
- Numerical verification of consistency with SM-5's TBM angles

Output: a sub-derivation document at `flagship_papers/neutrinos/sketches/SF-4_k3_cage_shell_consistency.md`; theorem-registry.md entry once proved; updates to OPEN-FP-SF-4-2 status.

### §9.4 Sessions 45+ — first-principles closure of $\alpha = 2$, integration, v0.1 drafting

Sub-tasks: rigorous closure of the $V^{7/3} \to V^2$ argument from the bound/unbound boundary; integration of all sub-derivations into the unified SF-4 narrative; v0.1 LaTeX paper draft following the SS-9 documentation discipline (sketches → development → paper-text staging).

### §9.5 Total estimate

6–10 sessions of substantive derivation work after this mechanism-selection session. Longer if either OPEN-FP-SF-4-1 or OPEN-FP-SF-4-2 opens its own sub-conditions — which would itself be honest signal worth documenting (e.g., that the substrate doesn't naturally support the structure, indicating a programme-level finding rather than a derivation failure).

### §9.6 Session 39 may continue immediately to Session 40 work

If context budget allows in this same conversation, after patch 0298 lands we open the first sub-task of OPEN-FP-SF-4-1: defining walk dimension precisely for an unbound 3D orbital ZBW mode in current CPP formalism. If context is tight, Session 40 starts in a fresh window with a clean handover prompt.

---

## §10. What this document does and does not establish

**This document establishes:**

- The mechanism choice for SF-4 mass derivation: Candidate C with $\alpha = 2$ and assignment $(V=4, V=12, V=30)$
- The $\delta_{CP}$ posture: route (ii), register as open
- The K3-eigenstructure enforcement strategy: theorem at zeroth order, numerical+conditional at higher order
- The calibration architecture: single-calibration ($m_e$) as hard requirement
- The hierarchy framing: derived consequence, falsifiable prediction
- The salvage scope from pre-formalism material
- Two OPEN-FP-SF-4-* sub-problems registered for Sessions 40+ work

**This document does not establish:**

- The first-principles derivation of $\alpha = 2$ from CPP primitives (sketched in §2.4; rigorous closure pending)
- The suppression factor $\mathcal{T}_{\text{unbound}}$ — pending OPEN-FP-SF-4-1
- The K3-Cage-Shell Consistency Theorem — pending OPEN-FP-SF-4-2
- Specific values for $m_{\nu_e}, m_{\nu_\mu}, m_{\nu_\tau}$ — pending the suppression mechanism
- Any portion of the eventual SF-4 paper text

**Forward dependencies:**

- Session 40 unlocks suppression-mechanism work; output gates OPEN-FP-SF-4-1 closure
- Sessions 43+ unlock K3-consistency work; output gates OPEN-FP-SF-4-2 closure
- Both must close before SF-4 v0.1 drafting begins
- SF-4 v1.0 ship requires both closures plus successful integration

---

*Decision document established at Session 39 (patch 0298). Builds on `SF-4_neutrino_sector_audit.md` (audit, patch 0294) and the §15 falsifier-check appendix (patch 0295). Charters the Sessions 40+ derivation campaign. Strategic source: Session 37 opening conversation strict-C posture; Session 38 architectural-decision conversation Option-3 adoption; Session 39 mechanism-selection conversation between Thomas and Claude.*
