# SF-1 Charged Leptons — Pre-Survey & Flagship Outline

**Location:** `/CPP/flagship_papers/charged_leptons/sf-1_outline.md`
**Opened:** Session 160, Patch 1302 (SF-7 grand-unification window)
**Status:** OUTLINE + source-corpus pre-survey. Drafting-ready handoff for a spin-off window. Per the SF-1 README, this is the lowest-risk SF-line paper (primarily reframing of shipped SM corpus; 3–5 sessions to v1.0).
**Source corpus surveyed:** SM-1, SM-3 (v6), SM-4, SM-6 (v3) — all shipped.
**Unlocks (post-ship):** §10 members SF-1↔SF-2 and SF-1↔SF-4 (see §9).

---

## 0. Orientation — read this first

SF-1 ships first among the four stub predecessors because it is **reframing, not new derivation**: the charged-lepton physics is already shipped across SM-3/4/6, and at strong rigor. The pre-survey below establishes that the headline is stronger than the SF-1 README assumed — SM-6 (Version 3) *derives* the Koide phase θ to 0.003%, closing for the charged-lepton sector the open problem (OP-SM-7d) that SM-4 had left as "θ undetermined within K3+SSV." The one honest residual is SM-3's Layer-B thermalization postulate P3. SF-1 is also the **cleanest single-m_e sector** in the corpus — zero shape parameters, and none of the m_c quark-route ambiguity flagged in patch 1300 §2. This makes SF-1 the strongest rhetorical anchor for the SF-line's "hierarchy without hierarchy" claim.

---

## 1. Headline result (what SF-1 claims)

> The entire charged-lepton sector — the Koide ratio $K=2/3$, the Koide phase $\theta = 132.73°$, and the masses $m_\mu, m_\tau$ — is derived from a **single calibration ($m_e$) plus 600-cell geometry, with zero free shape parameters**. The Weinberg angle $\sin^2\theta_W = 3/(8\phi)$ emerges as an intermediate result and feeds the phase derivation.

| Quantity | CPP | Experiment | Agreement | Source | Rigor |
|----------|-----|-----------|-----------|--------|-------|
| $\sin^2\theta_W$ | $3/(8\phi) \approx 0.2318$ | $0.23121$ | 0.24% | SM-6 Part I | theorem (mode-counting $\mathrm{Tr}A^2/\mathrm{Tr}A^3$) |
| Koide $K$ | $2/3$ | 11 ppm consistency | exact | SM-3 | theorem, conditional on P1–P3 |
| Koide phase $\theta$ | $132.731°$ | $132.732°$ | 0.003% | SM-6 Part II | derived (EW isotropic shift) |
| $m_\mu$ | $105.47$ MeV | $105.66$ | 0.18% | SM-6 | zero shape param |
| $m_\tau$ | $1774.1$ MeV | $1776.9$ | 0.15% | SM-6 | zero shape param |

Calibration ledger: **1 calibration** ($\mathrm{SSV}_0 = m_e c^2/2$, i.e. $m_e$), **0 shape parameters**. (Contrast SF-3, which carries the open $m_c$ quark-route question — SF-1 has no analog.)

---

## 2. Source-corpus rigor ledger (the pre-survey)

| Paper | Contributes to SF-1 | Epistemic status |
|-------|---------------------|------------------|
| **SM-1** | C3 cage symmetry; $\delta=1/3$ charge quantization; leptons have $\delta=0$ (no cage) → $q_e=-e$; ZBW Hamiltonian foundations | THEOREM (shipped, on OSF) |
| **SM-3 v6** | K3 Spectral Theorem: $K=2/3$ from $K_3$ adjacency spectrum (eigenvalue ratio $2{:}1 \Rightarrow \rho=\sqrt2 \Rightarrow K=2/3$). Explicit Layer A/B/C decomposition | THEOREM **conditional on P1–P3** (see §4) |
| **SM-4** | Applies SM-3 to lepton masses: $\sqrt{m_i}=A(1+\sqrt2\cos(\theta+2\pi i/3))$; **structural theorem (thm:theta_free): $\theta$ undetermined within K3+SSV** → OP-SM-7d | THEOREM (and an honest impossibility theorem) |
| **SM-6 v3** | Part I: $\sin^2\theta_W=3/(8\phi)$ from spectral traces. Part II: **derives** $\theta=132.731°$ via EW isotropic shift $\varepsilon = 2\sin^2\theta_W/(z+1)=3/(52\phi)$ on the K3 face. $m_\mu, m_\tau$ to <0.2% | DERIVED, zero shape param |

**Net:** the physics is shipped and largely theorem-level. The only Layer-B (imported-formalism) dependency is SM-3's P3.

---

## 3. The SM-4 → SM-6 phase arc (key reconciliation; do not garble this in the paper)

There is an *apparent* tension between SM-4 and SM-6 that SF-1 must present as a **closed arc, not a contradiction**:

- **SM-4** proves a *structural impossibility* theorem: the C3 symmetry of K3+SSV leaves $\theta$ undetermined — $\theta$ cannot be fixed from the cage-face structure *alone*. It extracts $\theta=132.73°$ from PDG and labels its derivation the principal open problem gating the EW series (OP-SM-7d).
- **SM-6 v3** *supplies the missing ingredient*: the electroweak isotropic shift $\varepsilon = 2\sin^2\theta_W/(z+1)$ shifts all K3 eigenvalues without breaking C3, changing $\cos\theta_0=-2/3$ to $\cos\theta_{\rm Koide} = -(2/3)(1+\sin^2\theta_W/(z+1))$, yielding $\theta=132.731°$ at 0.003%.

The two are consistent: SM-4 says "θ needs EW input"; SM-6 says "here is the EW input, and θ follows." **SF-1's narrative: OP-SM-7d is resolved for the charged-lepton phase by SM-6's EW correction.** This is a reframing win — SF-1 tells the SM-4→SM-6 story as a completed derivation, with SM-4's impossibility theorem as the motivation for why the EW correction is necessary (not optional).

*Note the cross-sector hook:* the EW correction that fixes $\theta$ is built from $\sin^2\theta_W = 3/(8\phi)$ — the **same** Weinberg-angle spectral-trace quantity SF-2 inherits from SM-6. This is the structural thread for the SF-1↔SF-2 §10 member (§9).

---

## 4. Open inheritances (register honestly, do not close)

Per the SF-1 README and the SS-9 conditional-theorem discipline, inherit — do not attempt to close — the following:

- **P3 (SM-3, Layer B):** equal K3-eigenstate occupation from thermal equilibration with the DP Sea in the high-$T$ limit ($kT_P/\hbar\omega_0 \sim 10^{20}$). The Gibbs formalism is standard; the **system-bath coupling model is imported from open-quantum-systems theory** (Caldeira–Leggett), and is the one Layer-B assumption. Resolution path: open problem SS-4. Register as **OPEN-FP-1-P3** and inherit.
- Finite-$T$ departures from $K=2/3$ are $O(\hbar\omega_0/kT_P)\sim 10^{-20}$, nine orders below the 11 ppm precision — so P3 is empirically harmless, but epistemically Layer B. State this honestly.
- **Scope discipline:** the K3 theorem applies to **leptons only**; quarks carry strong-sector contributions that break Koide by 10–27%. SF-1 must state this scope boundary explicitly (it is also what cleanly separates SF-1 from SF-3).

No new derivation work is anticipated. If a further Layer-B condition surfaces during reframing, register it as `OPEN-FP-1-*` and inherit per SS-9.

---

## 5. Calibration honesty (SF-1 is the clean case)

SF-1 is the sector where the SF-7 single-$m_e$ headline is **uncontested**: one calibration ($m_e$ via $\mathrm{SSV}_0$), zero shape parameters, no second calibration. The 1300 §2 caveats do **not** apply here — the $m_c$ ambiguity is a quark-sector (SF-3) issue, and the $\eta$-dilution caveat is an electroweak-boson (SF-2) issue. SF-1 should state its clean calibration ledger plainly; it is the strongest single-calibration anchor in the corpus and the right paper to establish the "one number → a sector" rhetoric for the SF-line.

---

## 6. Proposed section structure (apex-paper form; ~SF-2/SF-4 template)

- **§1 The charged-lepton mass problem.** Why $m_\mu/m_e \approx 207$, $m_\tau/m_\mu \approx 17$; why Koide holds to 11 ppm; 44 years unexplained. The named known-unknown.
- **§2 The 600-cell substrate + axioms.** Minimal CPP axiom recap; the tetrahedral lepton cage; K3 base graph; C3 symmetry; $\delta=0$ for leptons (SM-1).
- **§3 The K3 Spectral Theorem.** $K=2/3$ from $K_3$ adjacency spectrum; the Layer A/B/C decomposition stated up front (SS-9 conditional-theorem framing). P1, P2 Layer A; P3 Layer B inherited.
- **§4 The Weinberg angle as intermediate result.** $\sin^2\theta_W=3/(8\phi)$ from mode counting $\mathrm{Tr}A^2{:}\mathrm{Tr}A^3$; uniqueness among the six regular 4-polytopes; equals SU(5) GUT value before the $1/\phi$ metric correction.
- **§5 The Koide phase.** SM-4 impossibility theorem (θ needs EW input) → SM-6 EW isotropic shift → $\theta=132.731°$. Present as the closed SM-4→SM-6 arc (§3 above).
- **§6 The mass spectrum.** $\sqrt{m_i}=A(1+\sqrt2\cos(\theta+2\pi i/3))$; $m_\mu, m_\tau$ predictions; residual accounting.
- **§7 Calibration ledger.** One calibration, zero shape parameters (§5 above); the clean-case statement.
- **§8 Conditional accounting (honest §10-analog).** OPEN-FP-1-P3 inherited; lepton-only scope; what would falsify.
- **§9 Falsifiers.** Koide-breaking at improved precision; a 4th charged lepton; phase deviation after EW correction; $\sin^2\theta_W$ running inconsistency.
- **§10 Discussion / SF-line placement.** SF-1 as the clean single-$m_e$ anchor; hooks to SF-2 (shared $\sin^2\theta_W$) and SF-4 (shared $M_0$, cage taxonomy, OP-SM-7d phase/δ_CP handle).

---

## 7. What SF-1 does NOT do

- Does not close P3 (inherited; SS-4 is the resolution path).
- Does not address quarks (Koide-breaking; SF-3 territory).
- Does not derive $m_e$ (it is the calibration).
- Does not register theorems into `theorem-registry.md` until ship (the SM-3/4/6 theorems are already registered under their SM IDs; SF-1 reframes, it does not re-register).

---

## 8. Estimated lift & spin-off readiness

**3–5 sessions** per README, consistent with this survey: all physics is shipped, the SM-4→SM-6 reconciliation is the main intellectual content, and the conditional-theorem framing is a known template (SS-9). A spin-off window can take this outline directly to a `sf-1_charged_leptons.tex` draft. Recommended first drafting move: write §3–§5 (the K3 theorem + Weinberg + phase arc) as the structural core, then wrap §1–§2 and §6–§10 around it.

---

## 9. §10 members this unlocks (post-SF-1-ship)

Once SF-1 ships, two new SF-7 §10 consistency members become buildable, both with strong structural threads already identified:

- **SF-1 ↔ SF-2.** Shared substrate quantity: $\sin^2\theta_W = 3/(8\phi)$, the 600-cell spectral-trace mode fraction, used by SF-1 (phase correction) and SF-2 (Weinberg angle, $m_Z/m_W$). Consistency clause: both source $\sin^2\theta_W$ from the *same* $\mathrm{Tr}A^2{:}\mathrm{Tr}A^3$ structure with no independent calibration.
- **SF-1 ↔ SF-4.** Shared: $M_0 = m_e(z/\phi)$ anchor and the four-cage taxonomy; and the **OP-SM-7d handle** — SF-1's Koide phase and SF-4's δ_CP both route through the EW sector (OP-SM-7d), now partially supplied by SM-6's EW correction. Consistency clause: the EW correction that fixes the charged-lepton phase and the EW handle that SF-4 defers δ_CP to are the same sector-level object.

These follow the THEO-SF7-CONSIST-1 three-clause template (patch 1301): calibration coherence / no-double-counting / shared-observable single-handle.

---

## 10. Collision-coordination

This file is a **new file under `flagship_papers/charged_leptons/`** — no shared-registry edits, no other window's sector files touched. The SF-1 drafting work it scopes reads SM-1/3/4/6 sources (stable, shipped) and, at ship time, will touch shared registries via a flagged integration patch. The OP-SM-7d / EW-handle thread is **δ_CP-adjacent (window 5)** at the §9 SF-1↔SF-4 level, but this outline does not derive δ_CP and does not edit `frontier_sectors/SM.md`.

---

*Patch 1302 — SF-1 flagship outline + source pre-survey. Reframing-ready; no new derivation; no physics verdicts moved; no registries touched. New file under `flagship_papers/charged_leptons/`, collision-free.*
